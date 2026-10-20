# Research conversation: Consistency-Regularized RL for Perturbation-Robust Math Reasoning ## Core Problem RL-trained math reasoners suffer 47–73

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/70c05fd7-3f98-4d36-8384-f3f7cae3d6b1.jsonl`
- **Structured JSON:** [`c96fc0d770d092842f6f.json`](../../sessions/c9/c96fc0d770d092842f6f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T05:55:10.844Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T05:55:10.844Z",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "content": "# Consistency-Regularized RL for Perturbation-Robust Math Reasoning\n\n## Core Problem\n\nRL-trained math reasoners suffer 47–73% accuracy drops under trivial surface perturbations despite SOTA on clean benchmarks. Binary reward provides no gradient against surface-form-dependent strategies. Can consistency regularization over equivalent problem pairs during GRPO enforce perturbation invariance?\n\n## Research Opportunity\n\nNo work combines math-equivalence-aware perturbation with consistency regularization during GRPO. ROMA validates the paradigm for visual robustness; augmentation-only methods (TA-GRPO, PrAg-PO) lack invariance objectives. VAR-MATH documents the problem; DAPO/verl provides infrastructure.\n\n## Research Landscape\n\nAbstRaL (ICLR 2026): abstraction RL for GSM robustness only. TA-GRPO: +9.84pp competition math, no consistency loss/robustness eval. MathForge/DGPO (ICLR 2026): difficulty-aware GRPO, no robustness eval. ROMA (arXiv 2605.09262): correctness-conditioned KL for visual corruption robustness (+2.4%/+2.3%), closest cousin but targets images. F2C/PPCL: JS-based consistency, SFT-only/NLU-only. DPH-RL: JS for diversity not invariance. GRPO-CARE (arXiv 2506.16141): consistency-aware RL for video reasoning, not math perturbation. COPO (arXiv 2508.04138): consistency-entropy for zero-advantage, not robustness. CC-LEARN (arXiv 2506.15662): cohort consistency RL for NLU tasks. Diagnostics: VAR-MATH (47-73% drops), MATH-Perturb (ICML 2025), Robust Reasoning Benchmark (up to 54% drops) — none propose math-specific training fixes.\n\n## Proposed Approach\n\nTrain GRPO on Qwen3-8B with JS-divergence consistency loss over SymPy-verified equivalent math problem pairs. A symbolic perturbation generator creates numerical/variable variants preserving solution structure. The loss, correctness-conditioned (active only when both variants solved), penalizes divergent reasoning distributions. A contrastive discrimination loss against surface-similar but semantically-different problems prevents trivial invariance. Built on verl/DAPO infrastructure.\n\n## Detailed Description\n\nRL-trained math reasoners achieve SOTA on clean benchmarks but suffer 47-73% accuracy drops under trivial surface perturbations (VAR-MATH), revealing surface-heuristic dependence. We propose MACR (Math-Aware Consistency Regularization), integrating perturbation-invariance into GRPO training via three components: (1) SymPy-verified symbolic perturbation generator creating equivalent variants through numerical substitution and variable renaming; (2) correctness-conditioned JS-divergence loss over reasoning distributions between original and perturbed inputs, enforcing invariant strategies only on correctly-solved pairs; (3) contrastive discrimination loss against surface-similar but semantically-different problems preventing degenerate invariance. This uniquely synthesizes ROMA's RL-integrated regularization (visual domain), F2C/PPCL's consistency objectives (SFT-only), and VAR-MATH's templates into the first math-specific RL perturbation robustness method. We train Qwen3-8B via verl/DAPO and evaluate on VAR-MATH, MATH-Perturb, and the Robust Reasoning Benchmark, targeting both robustness gains and clean accuracy preservation.\n\n## Key References\n\n- ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation (arXiv 2026)\n- VAR-MATH: Probing True Mathematical Reasoning via Symbolic Benchmarks (arXiv 2025)\n- AbstRaL: Augmenting Reasoning by Reinforcing Abstract Thinking (ICLR 2026)\n- MATH-Perturb: Benchmarking Math Reasoning Against Hard Perturbations (ICML 2025)\n- Robust Reasoning Benchmark (arXiv 2026)\n- TA-GRPO: Transform-Augmented GRPO Improves Pass@k (arXiv 2025)\n- MathForge: Difficulty-Aware GRPO and Multi-Aspect Reformulation (ICLR 2026)\n- DAPO: Open-Source LLM RL System at Scale (arXiv 2025)\n- F2C: Flip-Flop Consistency for Prompt Perturbation Robustness (arXiv 2025)\n- GSM-Symbolic: Understanding Limitations of Math Reasoning (ICLR 2025)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-29T05:55:10.848Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T05:55:10.848Z",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1"
}
```

---

## Round 1

52 recorded events

### User

_source line 3 · 2026-05-29T05:55:10.872Z_

# Consistency-Regularized RL for Perturbation-Robust Math Reasoning

## Core Problem

RL-trained math reasoners suffer 47–73% accuracy drops under trivial surface perturbations despite SOTA on clean benchmarks. Binary reward provides no gradient against surface-form-dependent strategies. Can consistency regularization over equivalent problem pairs during GRPO enforce perturbation invariance?

## Research Opportunity

No work combines math-equivalence-aware perturbation with consistency regularization during GRPO. ROMA validates the paradigm for visual robustness; augmentation-only methods (TA-GRPO, PrAg-PO) lack invariance objectives. VAR-MATH documents the problem; DAPO/verl provides infrastructure.

## Research Landscape

AbstRaL (ICLR 2026): abstraction RL for GSM robustness only. TA-GRPO: +9.84pp competition math, no consistency loss/robustness eval. MathForge/DGPO (ICLR 2026): difficulty-aware GRPO, no robustness eval. ROMA (arXiv 2605.09262): correctness-conditioned KL for visual corruption robustness (+2.4%/+2.3%), closest cousin but targets images. F2C/PPCL: JS-based consistency, SFT-only/NLU-only. DPH-RL: JS for diversity not invariance. GRPO-CARE (arXiv 2506.16141): consistency-aware RL for video reasoning, not math perturbation. COPO (arXiv 2508.04138): consistency-entropy for zero-advantage, not robustness. CC-LEARN (arXiv 2506.15662): cohort consistency RL for NLU tasks. Diagnostics: VAR-MATH (47-73% drops), MATH-Perturb (ICML 2025), Robust Reasoning Benchmark (up to 54% drops) — none propose math-specific training fixes.

## Proposed Approach

Train GRPO on Qwen3-8B with JS-divergence consistency loss over SymPy-verified equivalent math problem pairs. A symbolic perturbation generator creates numerical/variable variants preserving solution structure. The loss, correctness-conditioned (active only when both variants solved), penalizes divergent reasoning distributions. A contrastive discrimination loss against surface-similar but semantically-different problems prevents trivial invariance. Built on verl/DAPO infrastructure.

## Detailed Description

RL-trained math reasoners achieve SOTA on clean benchmarks but suffer 47-73% accuracy drops under trivial surface perturbations (VAR-MATH), revealing surface-heuristic dependence. We propose MACR (Math-Aware Consistency Regularization), integrating perturbation-invariance into GRPO training via three components: (1) SymPy-verified symbolic perturbation generator creating equivalent variants through numerical substitution and variable renaming; (2) correctness-conditioned JS-divergence loss over reasoning distributions between original and perturbed inputs, enforcing invariant strategies only on correctly-solved pairs; (3) contrastive discrimination loss against surface-similar but semantically-different problems preventing degenerate invariance. This uniquely synthesizes ROMA's RL-integrated regularization (visual domain), F2C/PPCL's consistency objectives (SFT-only), and VAR-MATH's templates into the first math-specific RL perturbation robustness method. We train Qwen3-8B via verl/DAPO and evaluate on VAR-MATH, MATH-Perturb, and the Robust Reasoning Benchmark, targeting both robustness gains and clean accuracy preservation.

## Key References

- ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation (arXiv 2026)
- VAR-MATH: Probing True Mathematical Reasoning via Symbolic Benchmarks (arXiv 2025)
- AbstRaL: Augmenting Reasoning by Reinforcing Abstract Thinking (ICLR 2026)
- MATH-Perturb: Benchmarking Math Reasoning Against Hard Perturbations (ICML 2025)
- Robust Reasoning Benchmark (arXiv 2026)
- TA-GRPO: Transform-Augmented GRPO Improves Pass@k (arXiv 2025)
- MathForge: Difficulty-Aware GRPO and Multi-Aspect Reformulation (ICLR 2026)
- DAPO: Open-Source LLM RL System at Scale (arXiv 2025)
- F2C: Flip-Flop Consistency for Prompt Perturbation Robustness (arXiv 2025)
- GSM-Symbolic: Understanding Limitations of Math Reasoning (ICLR 2025)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "217f2f3e-83dc-45a6-a8c0-15a161585922",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T05:55:10.871Z_

```json
{
  "parentUuid": "217f2f3e-83dc-45a6-a8c0-15a161585922",
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
  "uuid": "8cf507d7-bfc7-4881-b7db-1445428908ec",
  "timestamp": "2026-05-29T05:55:10.871Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T05:55:10.871Z_

```json
{
  "parentUuid": "8cf507d7-bfc7-4881-b7db-1445428908ec",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "421c4542-0c4a-4827-b7c0-dd75d692951b",
  "timestamp": "2026-05-29T05:55:10.871Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
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
  "aiTitle": "Math RL robustness via consistency regularization",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1"
}
```

---

### Assistant

_source line 7 · 2026-05-29T05:55:18.972Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the "补救 agent" (remediation agent) to review this research proposal for AAAI 2026. My job is to focus exclusively on experimental design and technical execution — baselines, evaluation, ablation, feasibility — not on novelty or significance.

Let me first read the proposal carefully, then do web searches to understand the current experimental standards in this area before giving my assessment.

The proposal is about "Consistency-Regularized RL for Perturbation-Robust Math Reasoning" (MACR). Key components:


- SymPy-verified symbolic perturbation generator
- Correctness-conditioned JS-divergence loss
- Contrastive discrimination loss
- Built on verl/DAPO, training Qwen3-8B
- Evaluated on VAR-MATH, MATH-Perturb, Robust Reasoning Benchmark

Now I need to search for current experimental standards in this area to properly assess the proposal's technical rigor.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "421c4542-0c4a-4827-b7c0-dd75d692951b",
  "isSidechain": false,
  "requestId": "req_011CbWLrbSNSQ7mwk1ZPTfyD",
  "type": "assistant",
  "uuid": "d53085ac-af4a-4692-9ae4-d52df6420e48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QegwhqiE6QqvG8hjTuDDrA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5577,
      "cache_read_input_tokens": 11014,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5577,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 342,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 5577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5577
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

_source line 8 · 2026-05-29T05:55:19.522Z_

I need to do thorough pre-research before giving any experimental design recommendations. Let me search for the key papers and understand current experimental standards in this area.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d53085ac-af4a-4692-9ae4-d52df6420e48",
  "isSidechain": false,
  "requestId": "req_011CbWLrbSNSQ7mwk1ZPTfyD",
  "type": "assistant",
  "uuid": "71b35bdc-0aec-44ec-87a1-83d5b2bcb5b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QegwhqiE6QqvG8hjTuDDrA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5577,
      "cache_read_input_tokens": 11014,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5577,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 342,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 5577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5577
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

_source line 9 · 2026-05-29T05:55:19.893Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Xr1C9cxLcscouSXRDpqfTo`</summary>

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
  "parentUuid": "71b35bdc-0aec-44ec-87a1-83d5b2bcb5b3",
  "isSidechain": false,
  "requestId": "req_011CbWLrbSNSQ7mwk1ZPTfyD",
  "type": "assistant",
  "uuid": "488a4450-5069-4c34-a249-caf9cc60f06a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QegwhqiE6QqvG8hjTuDDrA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5577,
      "cache_read_input_tokens": 11014,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5577,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 342,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 5577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5577
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

_source line 10 · 2026-05-29T05:55:19.900Z_

<details><summary>↩ Tool result · `toolu_01Xr1C9cxLcscouSXRDpqfTo`</summary>

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
  "parentUuid": "488a4450-5069-4c34-a249-caf9cc60f06a",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "9328d690-62ad-4b38-b855-c9c47fe7a77e",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "488a4450-5069-4c34-a249-caf9cc60f06a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-29T05:55:22.014Z_

Now let me conduct the required pre-research. I'll search for the key related works and their experimental designs in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9328d690-62ad-4b38-b855-c9c47fe7a77e",
  "isSidechain": false,
  "requestId": "req_011CbWLsG9n9jaBJQLZETMLd",
  "type": "assistant",
  "uuid": "67837fdf-a099-45c4-a0e4-32866504b130",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RvjpfFUVNd96tdP8KikmZC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 16591,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 869,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 16591,
          "cache_creation_input_tokens": 869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 869
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

_source line 12 · 2026-05-29T05:55:23.123Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UnChTZEuUHc3yw2oUKRt7L`</summary>

```json
{
  "query": "ROMA Reinforcing Multimodal Reasoning Visual Degradation consistency regularization RL experimental design baselines 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67837fdf-a099-45c4-a0e4-32866504b130",
  "isSidechain": false,
  "requestId": "req_011CbWLsG9n9jaBJQLZETMLd",
  "type": "assistant",
  "uuid": "f358b8c6-fdab-4513-85d6-9e8a236dfa36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RvjpfFUVNd96tdP8KikmZC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 16591,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 869,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 16591,
          "cache_creation_input_tokens": 869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 869
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

_source line 13 · 2026-05-29T05:55:37.932Z_

<details><summary>↩ Tool result · `toolu_01UnChTZEuUHc3yw2oUKRt7L`</summary>

```text
Web search results for query: "ROMA Reinforcing Multimodal Reasoning Visual Degradation consistency regularization RL experimental design baselines 2026"

Links: [{"title":"[2605.09262] Reinforcing Multimodal Reasoning Against Visual Degradation","url":"https://arxiv.org/abs/2605.09262"},{"title":"Reinforcing Multimodal Reasoning Against Visual Degradation","url":"https://arxiv.org/html/2605.09262"},{"title":"Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding","url":"https://arxiv.org/html/2512.17532"},{"title":"Predictive Regularization Against Visual Representation Degradation in Multimodal Large Language Models","url":"https://arxiv.org/html/2603.20808"},{"title":"Perception-Consistency Multimodal Large Language Models Reasoning...","url":"https://arxiv.org/abs/2509.21854v1"},{"title":"Predictive Regularization Against Visual Representation Degradation in Multimodal Large Language Models","url":"https://arxiv.org/pdf/2603.20808"},{"title":"Perception-Consistency Multimodal Large Language Models Reasoning via Caption-Regularized Policy Optimization","url":"https://arxiv.org/html/2509.21854"},{"title":"Perception-Consistency Multimodal Large Language Models Reasoning via Caption-Regularized Policy Optimization","url":"https://arxiv.org/pdf/2509.21854"}]

I found relevant information about ROMA and related research. Here are the key findings:

## ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation

ROMA is an RL fine-tuning framework that modifies the optimization dynamics to reinforce reasoning against visual degradation while preserving clean-input performance.

### Technical Approach

ROMA uses a dual-forward-pass training strategy over a critic-free autoregressive MLLM, where the first pass performs standard RL rollouts on clean images to produce reasoning trajectories and advantages, and the second pass generates multiple degraded views and re-evaluates the frozen trajectory via teacher forcing, computing token-level log-probabilities under each corrupted view without sampling new rollouts.

### Consistency Regularization and RL Design

ROMA employs a token-level surrogate KL penalty that enforces distributional consistency between clean and degraded views, applied in a worst-case fashion against the augmentation with the largest divergence. The framework also applies an auxiliary policy gradient loss anchored to clean-image advantages to preserve a reliable reward signal and uses correctness-conditioned regularization to restrict enforcement to successful trajectories.

### Experimental Results

On Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, ROMA improves robustness by +2.4% on seen and +2.3% on unseen corruptions over GRPO while matching clean accuracy.

The paper was published recently (approximately 3 weeks ago based on the search results), making it a 2026 publication.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f358b8c6-fdab-4513-85d6-9e8a236dfa36",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "d9fabed8-28d8-4658-9fb2-5214607ac7f4",
  "toolUseResult": {
    "query": "ROMA Reinforcing Multimodal Reasoning Visual Degradation consistency regularization RL experimental design baselines 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016624JBSm55r3V9deoMWPZQ",
        "content": [
          {
            "title": "[2605.09262] Reinforcing Multimodal Reasoning Against Visual Degradation",
            "url": "https://arxiv.org/abs/2605.09262"
          },
          {
            "title": "Reinforcing Multimodal Reasoning Against Visual Degradation",
            "url": "https://arxiv.org/html/2605.09262"
          },
          {
            "title": "Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding",
            "url": "https://arxiv.org/html/2512.17532"
          },
          {
            "title": "Predictive Regularization Against Visual Representation Degradation in Multimodal Large Language Models",
            "url": "https://arxiv.org/html/2603.20808"
          },
          {
            "title": "Perception-Consistency Multimodal Large Language Models Reasoning...",
            "url": "https://arxiv.org/abs/2509.21854v1"
          },
          {
            "title": "Predictive Regularization Against Visual Representation Degradation in Multimodal Large Language Models",
            "url": "https://arxiv.org/pdf/2603.20808"
          },
          {
            "title": "Perception-Consistency Multimodal Large Language Models Reasoning via Caption-Regularized Policy Optimization",
            "url": "https://arxiv.org/html/2509.21854"
          },
          {
            "title": "Perception-Consistency Multimodal Large Language Models Reasoning via Caption-Regularized Policy Optimization",
            "url": "https://arxiv.org/pdf/2509.21854"
          }
        ]
      },
      "I found relevant information about ROMA and related research. Here are the key findings:\n\n## ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation\n\nROMA is an RL fine-tuning framework that modifies the optimization dynamics to reinforce reasoning against visual degradation while preserving clean-input performance.\n\n### Technical Approach\n\nROMA uses a dual-forward-pass training strategy over a critic-free autoregressive MLLM, where the first pass performs standard RL rollouts on clean images to produce reasoning trajectories and advantages, and the second pass generates multiple degraded views and re-evaluates the frozen trajectory via teacher forcing, computing token-level log-probabilities under each corrupted view without sampling new rollouts.\n\n### Consistency Regularization and RL Design\n\nROMA employs a token-level surrogate KL penalty that enforces distributional consistency between clean and degraded views, applied in a worst-case fashion against the augmentation with the largest divergence. The framework also applies an auxiliary policy gradient loss anchored to clean-image advantages to preserve a reliable reward signal and uses correctness-conditioned regularization to restrict enforcement to successful trajectories.\n\n### Experimental Results\n\nOn Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, ROMA improves robustness by +2.4% on seen and +2.3% on unseen corruptions over GRPO while matching clean accuracy.\n\nThe paper was published recently (approximately 3 weeks ago based on the search results), making it a 2026 publication."
    ],
    "durationSeconds": 14.802150646000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f358b8c6-fdab-4513-85d6-9e8a236dfa36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-29T05:55:40.344Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UGmqBGQ9kWydED1tUt4NxH`</summary>

```json
{
  "query": "VAR-MATH symbolic benchmark math reasoning perturbation robustness evaluation metrics experimental setup 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9fabed8-28d8-4658-9fb2-5214607ac7f4",
  "isSidechain": false,
  "requestId": "req_011CbWLtb94gJ6ysdwS3ZSYS",
  "type": "assistant",
  "uuid": "6c2c6450-731e-490e-9c27-d2485eda54ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TaouY5vaTCNEfyG6m7K5j7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 17460,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 17460,
          "cache_creation_input_tokens": 854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 854
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

_source line 15 · 2026-05-29T05:55:55.806Z_

<details><summary>↩ Tool result · `toolu_01UGmqBGQ9kWydED1tUt4NxH`</summary>

```text
Web search results for query: "VAR-MATH symbolic benchmark math reasoning perturbation robustness evaluation metrics experimental setup 2025"

Links: [{"title":"VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/html/2507.12885"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in ...","url":"https://arxiv.org/pdf/2507.12885"},{"title":"[2507.12885] VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/abs/2507.12885"},{"title":"Mathematical Reasoning Benchmarks Overview","url":"https://www.emergentmind.com/topics/mathematical-reasoning-benchmarks"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in Large Language Models via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/html/2507.12885v1"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833v1"},{"title":"T-Math Reasoning Benchmark","url":"https://www.emergentmind.com/topics/t-math-reasoning-benchmark"},{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/math-perturb-benchmarking-llms-math-reasoning-abilities"}]

Based on the search results, here's comprehensive information about VAR-MATH:

## Overview

VAR-MATH is a symbolic evaluation framework that systematically variabilizes three widely used benchmarks (AMC23, AIME24, and AIME25), enabling contamination-robust and consistency-based assessment of mathematical reasoning.

## Framework Design

VAR-MATH converts fixed numerical problems into parameterized templates and requires models to solve multiple instantiations of each. The process includes human verification where experts re-solve several instantiated variants using symbolic derivation, and model verification where all variants are checked by a frontier model as a sanity check.

## Evaluation Metrics

The framework evaluates model performance using two complementary metrics: loose and strict. It establishes a principled evaluation protocol that combines loose and strict consistency metrics with a bootstrapping procedure, ensuring statistically reliable comparison across models.

## Experimental Setup

VAR-MATH transforms three popular benchmarks, AMC23, AIME24, and AIME25, into their symbolic counterparts, VAR-AMC23, VAR-AIME24, and VAR-AIME25.

## Key Findings on Robustness

Experimental results show substantial performance drops for RL-trained models on these variabilized benchmarks, especially for smaller models, with average declines of 47.9% on AMC23, 58.8% on AIME24, and 72.9% on AIME25. Even minor perturbations in numeric form or expression structure continue to challenge models lacking robustness-oriented training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c2c6450-731e-490e-9c27-d2485eda54ed",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "3800fcd8-8cd4-4755-888a-1f07923ff68a",
  "toolUseResult": {
    "query": "VAR-MATH symbolic benchmark math reasoning perturbation robustness evaluation metrics experimental setup 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0142MYbckJmcaw4C5spEg8XM",
        "content": [
          {
            "title": "VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks",
            "url": "https://arxiv.org/html/2507.12885"
          },
          {
            "title": "VAR-MATH: Probing True Mathematical Reasoning in ...",
            "url": "https://arxiv.org/pdf/2507.12885"
          },
          {
            "title": "[2507.12885] VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks",
            "url": "https://arxiv.org/abs/2507.12885"
          },
          {
            "title": "Mathematical Reasoning Benchmarks Overview",
            "url": "https://www.emergentmind.com/topics/mathematical-reasoning-benchmarks"
          },
          {
            "title": "VAR-MATH: Probing True Mathematical Reasoning in Large Language Models via Symbolic Multi-Instance Benchmarks",
            "url": "https://arxiv.org/html/2507.12885v1"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/html/2508.08833v1"
          },
          {
            "title": "T-Math Reasoning Benchmark",
            "url": "https://www.emergentmind.com/topics/t-math-reasoning-benchmark"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/math-perturb-benchmarking-llms-math-reasoning-abilities"
          }
        ]
      },
      "Based on the search results, here's comprehensive information about VAR-MATH:\n\n## Overview\n\nVAR-MATH is a symbolic evaluation framework that systematically variabilizes three widely used benchmarks (AMC23, AIME24, and AIME25), enabling contamination-robust and consistency-based assessment of mathematical reasoning.\n\n## Framework Design\n\nVAR-MATH converts fixed numerical problems into parameterized templates and requires models to solve multiple instantiations of each. The process includes human verification where experts re-solve several instantiated variants using symbolic derivation, and model verification where all variants are checked by a frontier model as a sanity check.\n\n## Evaluation Metrics\n\nThe framework evaluates model performance using two complementary metrics: loose and strict. It establishes a principled evaluation protocol that combines loose and strict consistency metrics with a bootstrapping procedure, ensuring statistically reliable comparison across models.\n\n## Experimental Setup\n\nVAR-MATH transforms three popular benchmarks, AMC23, AIME24, and AIME25, into their symbolic counterparts, VAR-AMC23, VAR-AIME24, and VAR-AIME25.\n\n## Key Findings on Robustness\n\nExperimental results show substantial performance drops for RL-trained models on these variabilized benchmarks, especially for smaller models, with average declines of 47.9% on AMC23, 58.8% on AIME24, and 72.9% on AIME25. Even minor perturbations in numeric form or expression structure continue to challenge models lacking robustness-oriented training."
    ],
    "durationSeconds": 15.455674974,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6c2c6450-731e-490e-9c27-d2485eda54ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
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
  "lastPrompt": "# Consistency-Regularized RL for Perturbation-Robust Math Reasoning  ## Core Problem  RL-trained math reasoners suffer 47–73% accuracy drops under trivial surface perturbations despite SOTA on clean b…",
  "leafUuid": "3800fcd8-8cd4-4755-888a-1f07923ff68a",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Math RL robustness via consistency regularization",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1"
}
```

---

### Tool call

_source line 18 · 2026-05-29T05:55:57.946Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011dKgYNJHZJRqDJZz7obFE1`</summary>

```json
{
  "query": "MATH-Perturb ICML 2025 benchmark hard perturbations math reasoning baselines evaluation experimental design"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3800fcd8-8cd4-4755-888a-1f07923ff68a",
  "isSidechain": false,
  "requestId": "req_011CbWLuuMiU96avYqjK5sbu",
  "type": "assistant",
  "uuid": "ad85c1cd-abee-4612-b287-50fe6575aa5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K2dEJ7RGLrYzLQTsqcgGTa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 876,
      "cache_read_input_tokens": 18314,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 876,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 18314,
          "cache_creation_input_tokens": 876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 876
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

_source line 19 · 2026-05-29T05:56:04.622Z_

<details><summary>↩ Tool result · `toolu_011dKgYNJHZJRqDJZz7obFE1`</summary>

```text
Web search results for query: "MATH-Perturb ICML 2025 benchmark hard perturbations math reasoning baselines evaluation experimental design"

Links: [{"title":"MATH-Perturb","url":"https://math-perturb.github.io/"},{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | OpenReview","url":"https://openreview.net/forum?id=OZy70UggXr"},{"title":"GitHub - Kaffaljidhmah2/MATH-Perturb: Evaluation Code and Dataset for [ICML 2025] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://github.com/Kaffaljidhmah2/MATH-Perturb"},{"title":"MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations","url":"https://proceedings.mlr.press/v267/huang25k.html"},{"title":"MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations","url":"https://arxiv.org/html/2502.06453v2"},{"title":"ICML Poster MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://icml.cc/virtual/2025/poster/45435"},{"title":"[2502.06453] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://arxiv.org/abs/2502.06453"},{"title":"ICLR MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://iclr.cc/virtual/2025/32767"},{"title":"Published at ICLR 2025 Workshop on Reasoning and Planning for LLMs","url":"https://openreview.net/pdf?id=M8OLGgYK7e"}]

Based on the search results, here's what I found about MATH-Perturb:

## Overview

MATH-Perturb is a benchmark for evaluating LLMs' math reasoning abilities against hard perturbations, accepted at ICML 2025. The research addresses whether large language models' impressive performance on challenging mathematical reasoning tasks is achieved by true reasoning capability or memorization.

## Benchmark Design

The benchmark constructs MATH-P-Simple and MATH-P-Hard via simple perturbation and hard perturbation, respectively, with each consisting of 279 perturbed math problems derived from level-5 (hardest) problems in the MATH dataset. 

Simple perturbations to problems are non-essential modifications that can be solved using the same method as the original problem, while hard perturbations change the problem fundamentally and require more difficult problem-solving skills.

## Key Findings

Significant performance drops were observed on MATH-P-Hard across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%).

The research raises concerns about a novel form of memorization where models blindly apply learned problem-solving skills without assessing their applicability to modified contexts.

## Resources

Evaluation code and dataset are available for the ICML 2025 paper on GitHub, and the project is available at https://math-perturb.github.io/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad85c1cd-abee-4612-b287-50fe6575aa5c",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "24372436-11ba-4728-bb88-26da990e4365",
  "toolUseResult": {
    "query": "MATH-Perturb ICML 2025 benchmark hard perturbations math reasoning baselines evaluation experimental design",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Nybn6TmmihD6kXStpLZb1x",
        "content": [
          {
            "title": "MATH-Perturb",
            "url": "https://math-perturb.github.io/"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | OpenReview",
            "url": "https://openreview.net/forum?id=OZy70UggXr"
          },
          {
            "title": "GitHub - Kaffaljidhmah2/MATH-Perturb: Evaluation Code and Dataset for [ICML 2025] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
            "url": "https://github.com/Kaffaljidhmah2/MATH-Perturb"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations",
            "url": "https://proceedings.mlr.press/v267/huang25k.html"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations",
            "url": "https://arxiv.org/html/2502.06453v2"
          },
          {
            "title": "ICML Poster MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
            "url": "https://icml.cc/virtual/2025/poster/45435"
          },
          {
            "title": "[2502.06453] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
            "url": "https://arxiv.org/abs/2502.06453"
          },
          {
            "title": "ICLR MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
            "url": "https://iclr.cc/virtual/2025/32767"
          },
          {
            "title": "Published at ICLR 2025 Workshop on Reasoning and Planning for LLMs",
            "url": "https://openreview.net/pdf?id=M8OLGgYK7e"
          }
        ]
      },
      "Based on the search results, here's what I found about MATH-Perturb:\n\n## Overview\n\nMATH-Perturb is a benchmark for evaluating LLMs' math reasoning abilities against hard perturbations, accepted at ICML 2025. The research addresses whether large language models' impressive performance on challenging mathematical reasoning tasks is achieved by true reasoning capability or memorization.\n\n## Benchmark Design\n\nThe benchmark constructs MATH-P-Simple and MATH-P-Hard via simple perturbation and hard perturbation, respectively, with each consisting of 279 perturbed math problems derived from level-5 (hardest) problems in the MATH dataset. \n\nSimple perturbations to problems are non-essential modifications that can be solved using the same method as the original problem, while hard perturbations change the problem fundamentally and require more difficult problem-solving skills.\n\n## Key Findings\n\nSignificant performance drops were observed on MATH-P-Hard across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%).\n\nThe research raises concerns about a novel form of memorization where models blindly apply learned problem-solving skills without assessing their applicability to modified contexts.\n\n## Resources\n\nEvaluation code and dataset are available for the ICML 2025 paper on GitHub, and the project is available at https://math-perturb.github.io/."
    ],
    "durationSeconds": 6.672526312999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ad85c1cd-abee-4612-b287-50fe6575aa5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-29T05:56:07.397Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A1dZUzm2Xsq87rR19KvcdF`</summary>

```json
{
  "query": "AbstRaL augmenting reasoning reinforcing abstract thinking ICLR 2026 experimental setup baselines GSM robustness evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24372436-11ba-4728-bb88-26da990e4365",
  "isSidechain": false,
  "requestId": "req_011CbWLvZ2NiEJPB2AENFXmP",
  "type": "assistant",
  "uuid": "57805a66-6a98-44fb-8622-1cc49af3f8b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmcH8unfsuroJ445PNALf6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 19190,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 19190,
          "cache_creation_input_tokens": 953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 953
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

_source line 21 · 2026-05-29T05:56:16.271Z_

<details><summary>↩ Tool result · `toolu_01A1dZUzm2Xsq87rR19KvcdF`</summary>

```text
Web search results for query: "AbstRaL augmenting reasoning reinforcing abstract thinking ICLR 2026 experimental setup baselines GSM robustness evaluation"

Links: [{"title":"International Conference on Learning Representations (ICLR) 2026 - Apple Machine Learning Research","url":"https://machinelearning.apple.com/updates/apple-at-iclr-2026"},{"title":"ABSTRAL: AUGMENTING LLMS' REASONING BY ...","url":"https://openreview.net/pdf/cc239e2e8102d68f6e31bcda2af53e08d6bb6a91.pdf"},{"title":"EPFL @ ICLR 2026 - EPFL","url":"https://actu.epfl.ch/news/epfl-iclr-2026/"},{"title":"AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/html/2506.07751v4"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/pdf/2506.07751"},{"title":"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking | OpenReview","url":"https://openreview.net/forum?id=49vo7D9LbI"},{"title":"AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/abstral"},{"title":"[2506.07751] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/abs/2506.07751"},{"title":"[PDF] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AbstRaL:-Augmenting-LLMs'-Reasoning-by-Reinforcing-Gao-Bosselut/db59c2208185f3711705387c5baf2aa47ec648c5"}]

Based on the search results, here's information about the AbstRaL paper and ICLR 2026:

## Overview

AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking was presented by Silin Gao (EPFL), Antoine Bosselut (EPFL), Samy Bengio, and Emmanuel Abbe at ICLR 2026 as a poster.

## Problem and Approach

Recent studies have shown that large language models (LLMs), especially smaller ones, often lack robustness in grade school math (GSM) reasoning, particularly when they face distribution shifts such as changes to numerical or nominal variables, or insertions of distracting clauses.

The AbstRaL framework first teaches LLMs to generate mathematical abstraction of input GSM problems, and then connects the abstraction with symbolic tools to stably derive the output solution, regardless of the specific input contexts.

## Experimental Setup and Data

The learning of abstraction relies on Granularly-decomposed Abstract Reasoning (GranulAR) data distilled from an oracle LLM, which integrates symbolic reasoning within socratic problem decomposition and chain-of-thought explanations.

On top of supervised fine-tuning (SFT), AbstRaL uses reinforcement learning (RL) with a new set of model-free rewards to further improve the faithfulness of generated abstraction.

## Robustness Evaluation and Baselines

The method was tested on two benchmarks that evaluate the robustness of GSM reasoning: GSM-Symbolic and GSM-Plus.

## Results

AbstRaL—which promotes abstract reasoning in LLMs using RL on granular abstraction data—significantly mitigates performance degradation on recent GSM perturbation benchmarks. Additionally, improving GSM robustness via AbstRaL is shown to also implicitly benefit LLMs' capabilities on out-of-distribution mathematical and general reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57805a66-6a98-44fb-8622-1cc49af3f8b8",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "827bab8a-c901-4386-bc95-c500a4f33949",
  "toolUseResult": {
    "query": "AbstRaL augmenting reasoning reinforcing abstract thinking ICLR 2026 experimental setup baselines GSM robustness evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HN6iTa4mh54QQgDb6xuiEo",
        "content": [
          {
            "title": "International Conference on Learning Representations (ICLR) 2026 - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/updates/apple-at-iclr-2026"
          },
          {
            "title": "ABSTRAL: AUGMENTING LLMS' REASONING BY ...",
            "url": "https://openreview.net/pdf/cc239e2e8102d68f6e31bcda2af53e08d6bb6a91.pdf"
          },
          {
            "title": "EPFL @ ICLR 2026 - EPFL",
            "url": "https://actu.epfl.ch/news/epfl-iclr-2026/"
          },
          {
            "title": "AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/html/2506.07751v4"
          },
          {
            "title": "Downloads 2026",
            "url": "https://iclr.cc/Downloads/2026"
          },
          {
            "title": "AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/pdf/2506.07751"
          },
          {
            "title": "AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking | OpenReview",
            "url": "https://openreview.net/forum?id=49vo7D9LbI"
          },
          {
            "title": "AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/research/abstral"
          },
          {
            "title": "[2506.07751] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/abs/2506.07751"
          },
          {
            "title": "[PDF] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/AbstRaL:-Augmenting-LLMs'-Reasoning-by-Reinforcing-Gao-Bosselut/db59c2208185f3711705387c5baf2aa47ec648c5"
          }
        ]
      },
      "Based on the search results, here's information about the AbstRaL paper and ICLR 2026:\n\n## Overview\n\nAbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking was presented by Silin Gao (EPFL), Antoine Bosselut (EPFL), Samy Bengio, and Emmanuel Abbe at ICLR 2026 as a poster.\n\n## Problem and Approach\n\nRecent studies have shown that large language models (LLMs), especially smaller ones, often lack robustness in grade school math (GSM) reasoning, particularly when they face distribution shifts such as changes to numerical or nominal variables, or insertions of distracting clauses.\n\nThe AbstRaL framework first teaches LLMs to generate mathematical abstraction of input GSM problems, and then connects the abstraction with symbolic tools to stably derive the output solution, regardless of the specific input contexts.\n\n## Experimental Setup and Data\n\nThe learning of abstraction relies on Granularly-decomposed Abstract Reasoning (GranulAR) data distilled from an oracle LLM, which integrates symbolic reasoning within socratic problem decomposition and chain-of-thought explanations.\n\nOn top of supervised fine-tuning (SFT), AbstRaL uses reinforcement learning (RL) with a new set of model-free rewards to further improve the faithfulness of generated abstraction.\n\n## Robustness Evaluation and Baselines\n\nThe method was tested on two benchmarks that evaluate the robustness of GSM reasoning: GSM-Symbolic and GSM-Plus.\n\n## Results\n\nAbstRaL—which promotes abstract reasoning in LLMs using RL on granular abstraction data—significantly mitigates performance degradation on recent GSM perturbation benchmarks. Additionally, improving GSM robustness via AbstRaL is shown to also implicitly benefit LLMs' capabilities on out-of-distribution mathematical and general reasoning tasks."
    ],
    "durationSeconds": 8.870079932000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "57805a66-6a98-44fb-8622-1cc49af3f8b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-29T05:56:28.644Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0114DM2qEM6iVPFGRVKNcj1G`</summary>

```json
{
  "query": "TA-GRPO transform augmented GRPO math reasoning competition experimental design ablation study baselines 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "827bab8a-c901-4386-bc95-c500a4f33949",
  "isSidechain": false,
  "requestId": "req_011CbWLwQpnbhLXVZApM2218",
  "type": "assistant",
  "uuid": "968667e1-8d67-4c59-b338-d7f401ac1d1b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWPphfi269oJemhxsFLVLH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1138,
      "cache_read_input_tokens": 20143,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1138,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 20143,
          "cache_creation_input_tokens": 1138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1138
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

_source line 23 · 2026-05-29T05:56:41.845Z_

<details><summary>↩ Tool result · `toolu_0114DM2qEM6iVPFGRVKNcj1G`</summary>

```text
Web search results for query: "TA-GRPO transform augmented GRPO math reasoning competition experimental design ablation study baselines 2025"

Links: [{"title":"(PDF) Transform-Augmented GRPO Improves Pass@k","url":"https://www.researchgate.net/publication/400340183_Transform-Augmented_GRPO_Improves_Passk"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/pdf/2601.22478"},{"title":"[2601.22478] Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/abs/2601.22478"},{"title":"Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning","url":"https://arxiv.org/html/2602.03190v1"},{"title":"Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning","url":"https://arxiv.org/pdf/2602.03190"},{"title":"AMIR-GRPO: Inducing Implicit Preference Signals into GRPO","url":"https://arxiv.org/pdf/2601.03661"},{"title":"DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning","url":"https://arxiv.org/pdf/2505.09655"}]

Based on the search results, I found comprehensive information about TA-GRPO and related research:

## TA-GRPO Overview

TA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question (via paraphrasing, variable renaming, and format changes) and computes advantages by pooling rewards across the entire group.

## Problem Addressed

GRPO was designed to improve reasoning, but it worsens the situation through two failure modes: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.

## Key Results and Ablations

TA-GRPO consistently reduces zero-gradient questions compared to GRPO, maintaining a 12–16 percentage point advantage throughout training.

The insight is to present each question in multiple semantically equivalent forms. This approach forces the model to encounter diverse patterns for the same underlying problem.

## Experimental Design

Full Pass@k results are provided on Minerva and GPQA-Diamond (out-of-distribution benchmarks). The research includes theoretical validation, with propositions and corollaries showing that augmentation improves pooled success and providing principled justification for TA-GRPO's improved Pass@k performance.

## Related Baselines

The research compares against several GRPO variants, including DAPO (Yu et al., 2025) which addresses gradient diminishing through dynamic sampling, over-sampling rollouts and filtering out.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "968667e1-8d67-4c59-b338-d7f401ac1d1b",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "85cb63df-b379-4304-9c69-f9e07dcfba99",
  "toolUseResult": {
    "query": "TA-GRPO transform augmented GRPO math reasoning competition experimental design ablation study baselines 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U5kPXdpaNuH3K2vh8gyH2Y",
        "content": [
          {
            "title": "(PDF) Transform-Augmented GRPO Improves Pass@k",
            "url": "https://www.researchgate.net/publication/400340183_Transform-Augmented_GRPO_Improves_Passk"
          },
          {
            "title": "Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/pdf/2601.22478"
          },
          {
            "title": "[2601.22478] Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/abs/2601.22478"
          },
          {
            "title": "Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning",
            "url": "https://arxiv.org/html/2602.03190v1"
          },
          {
            "title": "Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2602.03190"
          },
          {
            "title": "AMIR-GRPO: Inducing Implicit Preference Signals into GRPO",
            "url": "https://arxiv.org/pdf/2601.03661"
          },
          {
            "title": "DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2505.09655"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about TA-GRPO and related research:\n\n## TA-GRPO Overview\n\nTA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question (via paraphrasing, variable renaming, and format changes) and computes advantages by pooling rewards across the entire group.\n\n## Problem Addressed\n\nGRPO was designed to improve reasoning, but it worsens the situation through two failure modes: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.\n\n## Key Results and Ablations\n\nTA-GRPO consistently reduces zero-gradient questions compared to GRPO, maintaining a 12–16 percentage point advantage throughout training.\n\nThe insight is to present each question in multiple semantically equivalent forms. This approach forces the model to encounter diverse patterns for the same underlying problem.\n\n## Experimental Design\n\nFull Pass@k results are provided on Minerva and GPQA-Diamond (out-of-distribution benchmarks). The research includes theoretical validation, with propositions and corollaries showing that augmentation improves pooled success and providing principled justification for TA-GRPO's improved Pass@k performance.\n\n## Related Baselines\n\nThe research compares against several GRPO variants, including DAPO (Yu et al., 2025) which addresses gradient diminishing through dynamic sampling, over-sampling rollouts and filtering out."
    ],
    "durationSeconds": 13.194313735000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "968667e1-8d67-4c59-b338-d7f401ac1d1b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-29T05:56:44.483Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JJ3AbNUMpr7tUBiovvFmMV`</summary>

```json
{
  "query": "GRPO math reasoning robustness training 2025 2026 consistency loss JS divergence KL divergence experimental evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85cb63df-b379-4304-9c69-f9e07dcfba99",
  "isSidechain": false,
  "requestId": "req_011CbWLyJBjQuR7ccigbEi1U",
  "type": "assistant",
  "uuid": "969efd0b-82a6-4fb4-b8a6-7f2f9b3448e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9f9sCtfwc1hbzeT5TafKP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 789,
      "cache_read_input_tokens": 21281,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 21281,
          "cache_creation_input_tokens": 789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 789
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

_source line 25 · 2026-05-29T05:56:53.398Z_

<details><summary>↩ Tool result · `toolu_01JJ3AbNUMpr7tUBiovvFmMV`</summary>

```text
Web search results for query: "GRPO math reasoning robustness training 2025 2026 consistency loss JS divergence KL divergence experimental evaluation"

Links: [{"title":"GRPO Trainer · Hugging Face","url":"https://huggingface.co/docs/trl/en/grpo_trainer"},{"title":"An In-depth Walkthrough of GRPO in NeMo RL — NeMo-RL","url":"https://docs.nvidia.com/nemo/rl/latest/guides/grpo.html"},{"title":"Reinforcement Learning for Reasoning in Large Language Models with One Training Example","url":"https://arxiv.org/html/2504.20571v1"},{"title":"Mitigating Think-Answer Mismatch in LLM Reasoning Through Noise-Aware Advantage Reweighting","url":"https://arxiv.org/pdf/2508.05928"},{"title":"A Unified Framework for Rethinking Policy Divergence Measures in GRPO","url":"https://arxiv.org/pdf/2602.05494"},{"title":"Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning","url":"https://arxiv.org/html/2602.03190v1"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"GRPO Algorithm Overview","url":"https://www.emergentmind.com/topics/grpo-algorithm"},{"title":"Geometric-Mean Policy Optimization","url":"https://arxiv.org/pdf/2507.20673"}]

Based on the search results, I found relevant information about GRPO (Group Relative Policy Optimization), mathematical reasoning, and the various divergence measures and robustness training techniques used in recent research (2025-2026). Here's what the search revealed:

## GRPO Loss Components and Divergence Measures

The GRPO loss function comprises three main components: policy gradient loss, KL divergence loss, and entropy loss. To understand how GRPO works, it can be broken down into four main steps: Generating completions, computing the advantage, estimating the KL divergence, and computing the loss.

The KL3 estimator, a variance-reduced Monte Carlo estimator of the KL divergence, is identified as a key policy divergence constraint. Additionally, Jensen–Shannon divergence (js_divergence_error) is used in GRPO implementations.

## Mathematical Reasoning and Robustness

S-GRPO consistently outperforms standard GRPO on models like Qwen-Math-7B (+2.5%), Llama-3.2-3B (+2.2%), and Qwen-Math-1.5B (+2.4%), and demonstrates remarkable robustness, maintaining stable training with minimal performance degradation even under 20% synthetic label noise where standard GRPO fails.

## Recent Experimental Evaluations

Comprehensive experiments on mathematical reasoning benchmarks demonstrate that KL3 estimator consistently improves training stability and final performance compared to existing state-of-the-art baselines. GMPO (Geometric-Mean Policy Optimization) improves the average Pass@1 accuracy by 4.1% (63.4% vs. 59.3%) compared to GRPO on five mathematical reasoning benchmarks with DeepSeek-R1-Distill-Qwen-7B.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "969efd0b-82a6-4fb4-b8a6-7f2f9b3448e6",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "ed496d91-ea2f-482e-b248-6c30381e64fb",
  "toolUseResult": {
    "query": "GRPO math reasoning robustness training 2025 2026 consistency loss JS divergence KL divergence experimental evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SRaaCZ5s58wai2bC7sKQb5",
        "content": [
          {
            "title": "GRPO Trainer · Hugging Face",
            "url": "https://huggingface.co/docs/trl/en/grpo_trainer"
          },
          {
            "title": "An In-depth Walkthrough of GRPO in NeMo RL — NeMo-RL",
            "url": "https://docs.nvidia.com/nemo/rl/latest/guides/grpo.html"
          },
          {
            "title": "Reinforcement Learning for Reasoning in Large Language Models with One Training Example",
            "url": "https://arxiv.org/html/2504.20571v1"
          },
          {
            "title": "Mitigating Think-Answer Mismatch in LLM Reasoning Through Noise-Aware Advantage Reweighting",
            "url": "https://arxiv.org/pdf/2508.05928"
          },
          {
            "title": "A Unified Framework for Rethinking Policy Divergence Measures in GRPO",
            "url": "https://arxiv.org/pdf/2602.05494"
          },
          {
            "title": "Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning",
            "url": "https://arxiv.org/html/2602.03190v1"
          },
          {
            "title": "Group Relative Policy Optimization (GRPO)",
            "url": "https://cameronrwolfe.substack.com/p/grpo"
          },
          {
            "title": "GRPO Algorithm Overview",
            "url": "https://www.emergentmind.com/topics/grpo-algorithm"
          },
          {
            "title": "Geometric-Mean Policy Optimization",
            "url": "https://arxiv.org/pdf/2507.20673"
          }
        ]
      },
      "Based on the search results, I found relevant information about GRPO (Group Relative Policy Optimization), mathematical reasoning, and the various divergence measures and robustness training techniques used in recent research (2025-2026). Here's what the search revealed:\n\n## GRPO Loss Components and Divergence Measures\n\nThe GRPO loss function comprises three main components: policy gradient loss, KL divergence loss, and entropy loss. To understand how GRPO works, it can be broken down into four main steps: Generating completions, computing the advantage, estimating the KL divergence, and computing the loss.\n\nThe KL3 estimator, a variance-reduced Monte Carlo estimator of the KL divergence, is identified as a key policy divergence constraint. Additionally, Jensen–Shannon divergence (js_divergence_error) is used in GRPO implementations.\n\n## Mathematical Reasoning and Robustness\n\nS-GRPO consistently outperforms standard GRPO on models like Qwen-Math-7B (+2.5%), Llama-3.2-3B (+2.2%), and Qwen-Math-1.5B (+2.4%), and demonstrates remarkable robustness, maintaining stable training with minimal performance degradation even under 20% synthetic label noise where standard GRPO fails.\n\n## Recent Experimental Evaluations\n\nComprehensive experiments on mathematical reasoning benchmarks demonstrate that KL3 estimator consistently improves training stability and final performance compared to existing state-of-the-art baselines. GMPO (Geometric-Mean Policy Optimization) improves the average Pass@1 accuracy by 4.1% (63.4% vs. 59.3%) compared to GRPO on five mathematical reasoning benchmarks with DeepSeek-R1-Distill-Qwen-7B."
    ],
    "durationSeconds": 8.91014332399999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "969efd0b-82a6-4fb4-b8a6-7f2f9b3448e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-29T05:56:56.477Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ErJ6M3SPFxxgFue5QK4PrX`</summary>

```json
{
  "query": "GSM-Symbolic ICLR 2025 evaluation robustness math LLM baselines experimental methodology perturbation types"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed496d91-ea2f-482e-b248-6c30381e64fb",
  "isSidechain": false,
  "requestId": "req_011CbWLz9e4Fhi9K8nVWVs58",
  "type": "assistant",
  "uuid": "19cc5587-ae16-4c15-b537-9d1f2566c8dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tz1axTgN6oBq4PvqR3gwCj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 22070,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 910,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 22070,
          "cache_creation_input_tokens": 910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 910
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

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Consistency-Regularized RL for Perturbation-Robust Math Reasoning  ## Core Problem  RL-trained math reasoners suffer 47–73% accuracy drops under trivial surface perturbations despite SOTA on clean b…",
  "leafUuid": "19cc5587-ae16-4c15-b537-9d1f2566c8dd",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Math RL robustness via consistency regularization",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1"
}
```

---

### Tool result

_source line 29 · 2026-05-29T05:57:04.476Z_

<details><summary>↩ Tool result · `toolu_01ErJ6M3SPFxxgFue5QK4PrX`</summary>

```text
Web search results for query: "GSM-Symbolic ICLR 2025 evaluation robustness math LLM baselines experimental methodology perturbation types"

Links: [{"title":"Published as a conference paper at ICLR 2025 GSM-SYMBOLIC: UNDERSTANDING","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ec2e7a896f8250986b3907f57621ce94-Paper-Conference.pdf"},{"title":"Towards more rigorous evaluations of language models | ICLR Blogposts 2025","url":"https://iclr-blogposts.github.io/2025/blog/towards-more-rigorous-llm-evals/"},{"title":"ICLR Poster GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models","url":"https://iclr.cc/virtual/2025/poster/30620"},{"title":"Published as a conference paper at ICLR 2025 GSM-SYMBOLIC: UNDERSTANDING","url":"https://arxiv.org/pdf/2410.05229"},{"title":"Published as a workshop paper at VerifAI - ICLR 2025","url":"https://openreview.net/pdf?id=nHW2tiGMrb"},{"title":"How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark","url":"https://arxiv.org/pdf/2505.18761"},{"title":"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models","url":"https://arxiv.org/html/2410.05229v1"},{"title":"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/gsm-symbolic"},{"title":"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=AjXkRZIvjB"},{"title":"Published at ICLR 2025 Workshop on Reasoning and Planning for LLMs","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/87_Re_Imagine_Symbolic_Benchmark.pdf"}]

Based on the search results, here's what I found about GSM-Symbolic, the ICLR 2025 paper on evaluation robustness for math reasoning in LLMs:

## Overview

GSM-Symbolic is an improved benchmark created from symbolic templates that allow for the generation of a diverse set of questions and enables more controllable evaluations, providing key insights and more reliable metrics for measuring the reasoning capabilities of models.

## Key Findings on Robustness

The paper evaluates 25 state-of-the-art open and closed models and reveals important insights about robustness:

- LLMs exhibit more robustness to changes in superficial elements like proper names but are very sensitive to changes in numerical values.

- Performance degradation and variance increase as the number of clauses increases, indicating that LLMs' reasoning capabilities struggle with increased complexity.

- The GSM-NoOp dataset demonstrates substantial performance drops (up to 65%) across all state-of-the-art models by adding seemingly relevant but ultimately irrelevant information to problems.

## Experimental Methodology

The authors selected 100 questions from GSM8K and created templates for each, sampling values for the variables to generate 50 new questions from each template, meaning GSM-Symbolic and each of its 4 variants (GSM-M1, GSM-P1, GSM-P2, and GSM-NoOp) contain 50 datasets of 100 questions each.

The research questions the reliability of single-point metrics, showing that the performance of LLMs can be viewed as a distribution with unwarranted variance across different instantiations of the same question.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19cc5587-ae16-4c15-b537-9d1f2566c8dd",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "dc9dea6e-89ec-4032-9d3c-f0e702e77f8e",
  "toolUseResult": {
    "query": "GSM-Symbolic ICLR 2025 evaluation robustness math LLM baselines experimental methodology perturbation types",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LDiBRfMBtpHmuK4KEd3HLQ",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2025 GSM-SYMBOLIC: UNDERSTANDING",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/ec2e7a896f8250986b3907f57621ce94-Paper-Conference.pdf"
          },
          {
            "title": "Towards more rigorous evaluations of language models | ICLR Blogposts 2025",
            "url": "https://iclr-blogposts.github.io/2025/blog/towards-more-rigorous-llm-evals/"
          },
          {
            "title": "ICLR Poster GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models",
            "url": "https://iclr.cc/virtual/2025/poster/30620"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 GSM-SYMBOLIC: UNDERSTANDING",
            "url": "https://arxiv.org/pdf/2410.05229"
          },
          {
            "title": "Published as a workshop paper at VerifAI - ICLR 2025",
            "url": "https://openreview.net/pdf?id=nHW2tiGMrb"
          },
          {
            "title": "How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark",
            "url": "https://arxiv.org/pdf/2505.18761"
          },
          {
            "title": "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models",
            "url": "https://arxiv.org/html/2410.05229v1"
          },
          {
            "title": "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/research/gsm-symbolic"
          },
          {
            "title": "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=AjXkRZIvjB"
          },
          {
            "title": "Published at ICLR 2025 Workshop on Reasoning and Planning for LLMs",
            "url": "https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/87_Re_Imagine_Symbolic_Benchmark.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about GSM-Symbolic, the ICLR 2025 paper on evaluation robustness for math reasoning in LLMs:\n\n## Overview\n\nGSM-Symbolic is an improved benchmark created from symbolic templates that allow for the generation of a diverse set of questions and enables more controllable evaluations, providing key insights and more reliable metrics for measuring the reasoning capabilities of models.\n\n## Key Findings on Robustness\n\nThe paper evaluates 25 state-of-the-art open and closed models and reveals important insights about robustness:\n\n- LLMs exhibit more robustness to changes in superficial elements like proper names but are very sensitive to changes in numerical values.\n\n- Performance degradation and variance increase as the number of clauses increases, indicating that LLMs' reasoning capabilities struggle with increased complexity.\n\n- The GSM-NoOp dataset demonstrates substantial performance drops (up to 65%) across all state-of-the-art models by adding seemingly relevant but ultimately irrelevant information to problems.\n\n## Experimental Methodology\n\nThe authors selected 100 questions from GSM8K and created templates for each, sampling values for the variables to generate 50 new questions from each template, meaning GSM-Symbolic and each of its 4 variants (GSM-M1, GSM-P1, GSM-P2, and GSM-NoOp) contain 50 datasets of 100 questions each.\n\nThe research questions the reliability of single-point metrics, showing that the performance of LLMs can be viewed as a distribution with unwarranted variance across different instantiations of the same question."
    ],
    "durationSeconds": 7.995139680000007,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "19cc5587-ae16-4c15-b537-9d1f2566c8dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-29T05:57:04.481Z_

```json
{
  "parentUuid": "dc9dea6e-89ec-4032-9d3c-f0e702e77f8e",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3f2facd7-23c3-4941-ad0c-7b4207d8d0ae",
  "timestamp": "2026-05-29T05:57:04.481Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-29T05:57:08.179Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AUS3vwy4bNVJheuz48eyqx`</summary>

```json
{
  "query": "Qwen3-8B GRPO training verl DAPO math reasoning compute requirements GPU hours setup 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f2facd7-23c3-4941-ad0c-7b4207d8d0ae",
  "isSidechain": false,
  "requestId": "req_011CbWLzxytYFbSx8B3Asuc7",
  "type": "assistant",
  "uuid": "63475218-afbc-42c1-b505-a7a4d5abadb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fmDtsKZZ7FKcqec3s9PSX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1146,
      "cache_read_input_tokens": 22980,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 22980,
          "cache_creation_input_tokens": 1146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1146
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

_source line 32 · 2026-05-29T05:57:19.069Z_

<details><summary>↩ Tool result · `toolu_01AUS3vwy4bNVJheuz48eyqx`</summary>

```text
Web search results for query: "Qwen3-8B GRPO training verl DAPO math reasoning compute requirements GPU hours setup 2025 2026"

Links: [{"title":"Qwen3-8b-base SFT+GRPO Training Report | My Blog","url":"https://dtianyou.com/en/notes/qwen3-8b-base-training/"},{"title":"Post Training Qwen3 for Math Reasoning Using GRPO - PyImageSearch","url":"https://pyimagesearch.com/2025/09/08/post-training-qwen3-for-math-reasoning-using-grpo/"},{"title":"The Engineering Handbook for GRPO + LoRA with Verl: Training Qwen2.5 on Multi-GPU","url":"https://huggingface.co/blog/Weyaxi/engineering-handbook-grpo-lora-with-verl"},{"title":"The Engineering Handbook for GRPO + LoRA with Verl: Training Qwen2.5 on Multi-GPU | by Yağız Çalık | Jan, 2026 | Medium","url":"https://medium.com/@weyaxi1/the-engineering-handbook-for-grpo-lora-with-verl-training-qwen2-5-on-multi-gpu-b2431a2a8e92"},{"title":"Unsloth - Qwen - Read the Docs","url":"https://qwen.readthedocs.io/en/latest/training/unsloth.html"},{"title":"Qwen3-8B: Specifications and GPU VRAM Requirements","url":"https://apxml.com/models/qwen3-8b"}]

Based on the search results, here's what I found about Qwen3-8B GRPO training with verl and DAPO for math reasoning:

## Hardware Setup

For Qwen3-8B training, eight RTX 4090 GPUs were used, each with 48GB of VRAM, totaling 384GB. The software environment used the official verl DAPO Docker image hiyouga/verl:ngc-th2.6.0-cu126-vllm0.8.3, which integrates all required dependencies.

## Training Approach

The training involved SFT (Supervised Fine-tuning) and GRPO (Group-wise Reward Policy Optimization) stages aimed at enhancing the model's performance on mathematical problem-solving, especially for the GSM8K and AIME24 datasets.

## Key Benefits

GRPO proved that Group Relative Policy Optimization could induce advanced reasoning capabilities by eliminating the memory-heavy value function, significantly reducing the compute overhead compared to traditional PPO.

## Training Tools

RLHF support includes GRPO, DPO, DAPO, RM, PPO, KTO, etc., with verl providing the sophisticated distributed framework required for industrial production environments and being widely used in industry for high-throughput RL.

The search results don't contain specific GPU hour requirements for Qwen3-8B GRPO training. For more detailed compute requirements, you may need to refer to the original training reports or documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63475218-afbc-42c1-b505-a7a4d5abadb2",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "e051bd27-3fd5-46aa-8525-79b158140d90",
  "toolUseResult": {
    "query": "Qwen3-8B GRPO training verl DAPO math reasoning compute requirements GPU hours setup 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UVZTVQjkkB18454yacRsux",
        "content": [
          {
            "title": "Qwen3-8b-base SFT+GRPO Training Report | My Blog",
            "url": "https://dtianyou.com/en/notes/qwen3-8b-base-training/"
          },
          {
            "title": "Post Training Qwen3 for Math Reasoning Using GRPO - PyImageSearch",
            "url": "https://pyimagesearch.com/2025/09/08/post-training-qwen3-for-math-reasoning-using-grpo/"
          },
          {
            "title": "The Engineering Handbook for GRPO + LoRA with Verl: Training Qwen2.5 on Multi-GPU",
            "url": "https://huggingface.co/blog/Weyaxi/engineering-handbook-grpo-lora-with-verl"
          },
          {
            "title": "The Engineering Handbook for GRPO + LoRA with Verl: Training Qwen2.5 on Multi-GPU | by Yağız Çalık | Jan, 2026 | Medium",
            "url": "https://medium.com/@weyaxi1/the-engineering-handbook-for-grpo-lora-with-verl-training-qwen2-5-on-multi-gpu-b2431a2a8e92"
          },
          {
            "title": "Unsloth - Qwen - Read the Docs",
            "url": "https://qwen.readthedocs.io/en/latest/training/unsloth.html"
          },
          {
            "title": "Qwen3-8B: Specifications and GPU VRAM Requirements",
            "url": "https://apxml.com/models/qwen3-8b"
          }
        ]
      },
      "Based on the search results, here's what I found about Qwen3-8B GRPO training with verl and DAPO for math reasoning:\n\n## Hardware Setup\n\nFor Qwen3-8B training, eight RTX 4090 GPUs were used, each with 48GB of VRAM, totaling 384GB. The software environment used the official verl DAPO Docker image hiyouga/verl:ngc-th2.6.0-cu126-vllm0.8.3, which integrates all required dependencies.\n\n## Training Approach\n\nThe training involved SFT (Supervised Fine-tuning) and GRPO (Group-wise Reward Policy Optimization) stages aimed at enhancing the model's performance on mathematical problem-solving, especially for the GSM8K and AIME24 datasets.\n\n## Key Benefits\n\nGRPO proved that Group Relative Policy Optimization could induce advanced reasoning capabilities by eliminating the memory-heavy value function, significantly reducing the compute overhead compared to traditional PPO.\n\n## Training Tools\n\nRLHF support includes GRPO, DPO, DAPO, RM, PPO, KTO, etc., with verl providing the sophisticated distributed framework required for industrial production environments and being widely used in industry for high-throughput RL.\n\nThe search results don't contain specific GPU hour requirements for Qwen3-8B GRPO training. For more detailed compute requirements, you may need to refer to the original training reports or documentation."
    ],
    "durationSeconds": 10.885523375000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "63475218-afbc-42c1-b505-a7a4d5abadb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-29T05:57:22.340Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UHrrKYmKvXJ1iwGhtxFrSC`</summary>

```json
{
  "query": "Robust Reasoning Benchmark arXiv 2026 math LLM perturbation robustness evaluation 54% drops"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e051bd27-3fd5-46aa-8525-79b158140d90",
  "isSidechain": false,
  "requestId": "req_011CbWM23Jrujqgy5FJ8AR7y",
  "type": "assistant",
  "uuid": "f5f4c620-b3bb-4870-a7f3-a31e213c5672",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01493swQJ8QmQHBUrCZujyZD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 865,
      "cache_read_input_tokens": 24126,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 24126,
          "cache_creation_input_tokens": 865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 865
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

_source line 34 · 2026-05-29T05:57:28.941Z_

<details><summary>↩ Tool result · `toolu_01UHrrKYmKvXJ1iwGhtxFrSC`</summary>

```text
Web search results for query: "Robust Reasoning Benchmark arXiv 2026 math LLM perturbation robustness evaluation 54% drops"

Links: [{"title":"Robust Reasoning Benchmark – Paper Detail · SwiftScholar - Review with AI","url":"https://www.swiftscholar.net/paper/69dd894984947a5132b62b34"},{"title":"Robust Reasoning Benchmark","url":"https://arxiv.org/html/2604.08571"},{"title":"Benchmarking Reasoning Robustness in Large Language Models","url":"https://arxiv.org/html/2503.04550v1"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833v1"},{"title":"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of   LLMs as Mathematical Problem Solvers","url":"https://arxiv.org/pdf/2402.19255"},{"title":"MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations","url":"https://arxiv.org/html/2502.06453v2"},{"title":"[2508.08833] An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/abs/2508.08833"}]

Based on the search results, I found information about the Robust Reasoning Benchmark:

The paper was published on March 26, 2026 on arXiv. The paper proposes a perturbation pipeline consisting of 14 techniques to evaluate the robustness of LLM reasoning, which are applied to the AIME 2024 dataset to test 8 state-of-the-art models.

The Robust Reasoning Benchmark (RRB) focuses on evaluating the robustness of Large Language Models (LLMs) in mathematical reasoning when faced with structural perturbations and context pollution, rather than changes in the mathematical logic itself.

Regarding the performance drops you mentioned, the results show a significant gap: "frontier" models (like GPT-5.4 and Gemini 3.1 Pro) exhibit resilience, while "open-weights" reasoning models suffer catastrophic accuracy drops (up to 55% average and 100% on specific perturbations).

The authors are Pavel Golikov, Evgenii Opryshko, Gennady Pekhimenko, and Mark C. Jeffrey, affiliated with the University of Toronto and the Vector Institute.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5f4c620-b3bb-4870-a7f3-a31e213c5672",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "8df4b357-9902-4197-8dc0-4919f692f407",
  "toolUseResult": {
    "query": "Robust Reasoning Benchmark arXiv 2026 math LLM perturbation robustness evaluation 54% drops",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LfKgGafafravxTrMPYHGC4",
        "content": [
          {
            "title": "Robust Reasoning Benchmark – Paper Detail · SwiftScholar - Review with AI",
            "url": "https://www.swiftscholar.net/paper/69dd894984947a5132b62b34"
          },
          {
            "title": "Robust Reasoning Benchmark",
            "url": "https://arxiv.org/html/2604.08571"
          },
          {
            "title": "Benchmarking Reasoning Robustness in Large Language Models",
            "url": "https://arxiv.org/html/2503.04550v1"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/html/2508.08833v1"
          },
          {
            "title": "GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of   LLMs as Mathematical Problem Solvers",
            "url": "https://arxiv.org/pdf/2402.19255"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations",
            "url": "https://arxiv.org/html/2502.06453v2"
          },
          {
            "title": "[2508.08833] An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/abs/2508.08833"
          }
        ]
      },
      "Based on the search results, I found information about the Robust Reasoning Benchmark:\n\nThe paper was published on March 26, 2026 on arXiv. The paper proposes a perturbation pipeline consisting of 14 techniques to evaluate the robustness of LLM reasoning, which are applied to the AIME 2024 dataset to test 8 state-of-the-art models.\n\nThe Robust Reasoning Benchmark (RRB) focuses on evaluating the robustness of Large Language Models (LLMs) in mathematical reasoning when faced with structural perturbations and context pollution, rather than changes in the mathematical logic itself.\n\nRegarding the performance drops you mentioned, the results show a significant gap: \"frontier\" models (like GPT-5.4 and Gemini 3.1 Pro) exhibit resilience, while \"open-weights\" reasoning models suffer catastrophic accuracy drops (up to 55% average and 100% on specific perturbations).\n\nThe authors are Pavel Golikov, Evgenii Opryshko, Gennady Pekhimenko, and Mark C. Jeffrey, affiliated with the University of Toronto and the Vector Institute."
    ],
    "durationSeconds": 6.597820062000014,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f5f4c620-b3bb-4870-a7f3-a31e213c5672",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-29T05:57:32.030Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AcWWBBf2kXBCF8MNknX7HL`</summary>

```json
{
  "query": "F2C flip-flop consistency prompt perturbation robustness JS divergence SFT experimental design NLU 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8df4b357-9902-4197-8dc0-4919f692f407",
  "isSidechain": false,
  "requestId": "req_011CbWM2meodMfgiVCBpTGyp",
  "type": "assistant",
  "uuid": "47d06544-5f5f-48be-80f5-27b1d7837e8a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRzX92jAh8Hz83MeLo6Th4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 24991,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 24991,
          "cache_creation_input_tokens": 750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 750
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

_source line 36 · 2026-05-29T05:57:39.855Z_

<details><summary>↩ Tool result · `toolu_01AcWWBBf2kXBCF8MNknX7HL`</summary>

```text
Web search results for query: "F2C flip-flop consistency prompt perturbation robustness JS divergence SFT experimental design NLU 2025"

Links: [{"title":"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/html/2510.14242v1"},{"title":"[2510.14242v1] Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/abs/2510.14242v1"},{"title":"[2510.14242] Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/abs/2510.14242"},{"title":"Flip-Flop Consistency: Unsupervised Training for ...","url":"https://arxiv.org/pdf/2510.14242"},{"title":"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs | Request PDF","url":"https://www.researchgate.net/publication/396541005_Flip-Flop_Consistency_Unsupervised_Training_for_Robustness_to_Prompt_Perturbations_in_LLMs"},{"title":"Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://arxiv.org/pdf/2402.15833"}]

Based on the search results, I found a highly relevant paper that matches your query:

## Flip-Flop Consistency (F2C) Research Paper

Large Language Models (LLMs) often produce inconsistent answers when faced with different phrasings of the same prompt. The paper proposes Flip-Flop Consistency (F2C), an unsupervised training method that improves robustness to such perturbations.

**Key Components:**

The first component, Consensus Cross-Entropy (CCE), uses a majority vote across prompt variations to create a hard pseudo-label. The second is a representation alignment loss that pulls lower-confidence and non-majority predictors toward the consensus established by high-confidence, majority-voting variations.

**Evaluation and Results:**

The method was evaluated on 11 datasets spanning four NLP tasks, with 4-15 prompt variations per dataset. On average, F2C raises observed agreement by 11.62%, improves mean F1 by 8.94%, and reduces performance variance across formats by 3.29%.

**Technical Details:**

The method minimizes the JS divergence among datapoints within the high-confidence consensus group, and the KL divergence between all other datapoints and the consensus.

The paper was published on arXiv in October 2025 and was authored by researchers from the University of Southern California.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47d06544-5f5f-48be-80f5-27b1d7837e8a",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "abc64ca2-13a4-4cac-a447-36d5e3b0f6d3",
  "toolUseResult": {
    "query": "F2C flip-flop consistency prompt perturbation robustness JS divergence SFT experimental design NLU 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TkuXJyrcJhH8NYcUT5fWNg",
        "content": [
          {
            "title": "Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs",
            "url": "https://arxiv.org/html/2510.14242v1"
          },
          {
            "title": "[2510.14242v1] Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs",
            "url": "https://arxiv.org/abs/2510.14242v1"
          },
          {
            "title": "[2510.14242] Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs",
            "url": "https://arxiv.org/abs/2510.14242"
          },
          {
            "title": "Flip-Flop Consistency: Unsupervised Training for ...",
            "url": "https://arxiv.org/pdf/2510.14242"
          },
          {
            "title": "Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs | Request PDF",
            "url": "https://www.researchgate.net/publication/396541005_Flip-Flop_Consistency_Unsupervised_Training_for_Robustness_to_Prompt_Perturbations_in_LLMs"
          },
          {
            "title": "Prompt Perturbation Consistency Learning for Robust Language Models",
            "url": "https://arxiv.org/pdf/2402.15833"
          }
        ]
      },
      "Based on the search results, I found a highly relevant paper that matches your query:\n\n## Flip-Flop Consistency (F2C) Research Paper\n\nLarge Language Models (LLMs) often produce inconsistent answers when faced with different phrasings of the same prompt. The paper proposes Flip-Flop Consistency (F2C), an unsupervised training method that improves robustness to such perturbations.\n\n**Key Components:**\n\nThe first component, Consensus Cross-Entropy (CCE), uses a majority vote across prompt variations to create a hard pseudo-label. The second is a representation alignment loss that pulls lower-confidence and non-majority predictors toward the consensus established by high-confidence, majority-voting variations.\n\n**Evaluation and Results:**\n\nThe method was evaluated on 11 datasets spanning four NLP tasks, with 4-15 prompt variations per dataset. On average, F2C raises observed agreement by 11.62%, improves mean F1 by 8.94%, and reduces performance variance across formats by 3.29%.\n\n**Technical Details:**\n\nThe method minimizes the JS divergence among datapoints within the high-confidence consensus group, and the KL divergence between all other datapoints and the consensus.\n\nThe paper was published on arXiv in October 2025 and was authored by researchers from the University of Southern California."
    ],
    "durationSeconds": 7.819721451999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "47d06544-5f5f-48be-80f5-27b1d7837e8a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-29T05:57:52.734Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HV2zt2m6azCYRs9TUEfHLC`</summary>

```json
{
  "query": "PrAg-PO prompt augmentation GRPO math reasoning 2025 experimental setup ablation evaluation benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abc64ca2-13a4-4cac-a447-36d5e3b0f6d3",
  "isSidechain": false,
  "requestId": "req_011CbWM3aCWfgQkswsTzF6sy",
  "type": "assistant",
  "uuid": "68cb1a94-9944-47eb-88a9-211301d28f70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUV6es3FLojhwgXZkGa3rD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 25741,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 25741,
          "cache_creation_input_tokens": 805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 805
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

_source line 38 · 2026-05-29T05:58:00.452Z_

<details><summary>↩ Tool result · `toolu_01HV2zt2m6azCYRs9TUEfHLC`</summary>

```text
Web search results for query: "PrAg-PO prompt augmentation GRPO math reasoning 2025 experimental setup ablation evaluation benchmarks"

Links: [{"title":"[2602.03190] Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning","url":"https://arxiv.org/abs/2602.03190"},{"title":"Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning","url":"https://arxiv.org/html/2602.03190v1"},{"title":"Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning","url":"https://arxiv.org/pdf/2602.03190"},{"title":"Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation","url":"https://arxiv.org/html/2601.20614"},{"title":"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.287/"},{"title":"Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation","url":"https://arxiv.org/pdf/2601.20614"}]

Based on the web search results, here's what I found about PrAg-PO (Prompt Augmentation for GRPO):

## Overview

Prompt augmentation is a training strategy that instructs the model to generate reasoning traces under diverse templates and formats, thereby increasing rollout diversity.

## Problem Addressed

Prior work has consistently observed an entropy collapse phenomenon during reinforcement post-training, characterized by a monotonic decrease in policy entropy that ultimately leads to training instability and collapse, resulting in most existing approaches restricting training to short horizons (typically 5-20 epochs).

## Key Innovation

Without a KL regularization term, prompt augmentation enables stable scaling of training duration under a fixed dataset and allows the model to tolerate low-entropy regimes without premature collapse.

## Experimental Results

A Qwen2.5-Math-1.5B model trained with prompt augmentation on the MATH Level 3-5 dataset achieves state-of-the-art performance, reaching 45.2 per-benchmark accuracy and 51.8 per-question accuracy on standard mathematical reasoning benchmarks, including AIME24, AMC, MATH500, Minerva, and OlympiadBench.

The paper was published on February 6, 2026, and the code and model checkpoints are available at https://github.com/wenquanlu/prompt-augmentation-GRPO.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68cb1a94-9944-47eb-88a9-211301d28f70",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "d25d3b4b-8ddb-4e8f-91d5-a64045520383",
  "toolUseResult": {
    "query": "PrAg-PO prompt augmentation GRPO math reasoning 2025 experimental setup ablation evaluation benchmarks",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YT61g2GUf6PjYp5pFraNRF",
        "content": [
          {
            "title": "[2602.03190] Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning",
            "url": "https://arxiv.org/abs/2602.03190"
          },
          {
            "title": "Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning",
            "url": "https://arxiv.org/html/2602.03190v1"
          },
          {
            "title": "Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2602.03190"
          },
          {
            "title": "Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation",
            "url": "https://arxiv.org/html/2601.20614"
          },
          {
            "title": "GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.287/"
          },
          {
            "title": "Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation",
            "url": "https://arxiv.org/pdf/2601.20614"
          }
        ]
      },
      "Based on the web search results, here's what I found about PrAg-PO (Prompt Augmentation for GRPO):\n\n## Overview\n\nPrompt augmentation is a training strategy that instructs the model to generate reasoning traces under diverse templates and formats, thereby increasing rollout diversity.\n\n## Problem Addressed\n\nPrior work has consistently observed an entropy collapse phenomenon during reinforcement post-training, characterized by a monotonic decrease in policy entropy that ultimately leads to training instability and collapse, resulting in most existing approaches restricting training to short horizons (typically 5-20 epochs).\n\n## Key Innovation\n\nWithout a KL regularization term, prompt augmentation enables stable scaling of training duration under a fixed dataset and allows the model to tolerate low-entropy regimes without premature collapse.\n\n## Experimental Results\n\nA Qwen2.5-Math-1.5B model trained with prompt augmentation on the MATH Level 3-5 dataset achieves state-of-the-art performance, reaching 45.2 per-benchmark accuracy and 51.8 per-question accuracy on standard mathematical reasoning benchmarks, including AIME24, AMC, MATH500, Minerva, and OlympiadBench.\n\nThe paper was published on February 6, 2026, and the code and model checkpoints are available at https://github.com/wenquanlu/prompt-augmentation-GRPO."
    ],
    "durationSeconds": 7.711252540999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "68cb1a94-9944-47eb-88a9-211301d28f70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
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
  "lastPrompt": "# Consistency-Regularized RL for Perturbation-Robust Math Reasoning  ## Core Problem  RL-trained math reasoners suffer 47–73% accuracy drops under trivial surface perturbations despite SOTA on clean b…",
  "leafUuid": "d25d3b4b-8ddb-4e8f-91d5-a64045520383",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Math RL robustness via consistency regularization",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1"
}
```

---

### Tool call

_source line 41 · 2026-05-29T05:58:03.105Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015BGWo989MQe8KJoewCvgxN`</summary>

```json
{
  "query": "SymPy math problem perturbation generation symbolic verification equivalent problem pairs automated pipeline 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d25d3b4b-8ddb-4e8f-91d5-a64045520383",
  "isSidechain": false,
  "requestId": "req_011CbWM56DKgrdNukt7PPvrW",
  "type": "assistant",
  "uuid": "11cedf00-0433-4db1-b7fe-58091474a3f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhpALBzfEgJaxFkgy7V2AV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 26546,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 26546,
          "cache_creation_input_tokens": 745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 745
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

_source line 42 · 2026-05-29T05:58:12.170Z_

<details><summary>↩ Tool result · `toolu_015BGWo989MQe8KJoewCvgxN`</summary>

```text
Web search results for query: "SymPy math problem perturbation generation symbolic verification equivalent problem pairs automated pipeline 2025 2026"

Links: [{"title":"Adaptive Problem Generation via Symbolic Representations","url":"https://arxiv.org/html/2602.19187"},{"title":"ASyMOB: Algebraic Symbolic Mathematical Operations Benchmark","url":"https://arxiv.org/html/2505.23851v1"},{"title":"Test-time Scaling Techniques in Theoretical Physics -","url":"https://ml4physicalsciences.github.io/2025/files/NeurIPS_ML4PS_2025_20.pdf"},{"title":"SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation","url":"https://arxiv.org/pdf/2510.25975"},{"title":"Adaptive Problem Generation via Symbolic Representations","url":"https://arxiv.org/pdf/2602.19187"},{"title":"Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment","url":"https://arxiv.org/html/2603.21558"},{"title":"Mixed Symbolic-Numeric Perturbation Theory · Symbolics.jl","url":"https://docs.sciml.ai/Symbolics/stable/examples/perturbation/"},{"title":"Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification","url":"https://arxiv.org/pdf/2603.19715"},{"title":"GitHub - qcode-uni-a/sympt: Symbolic Perturbation Theory (SymPT) is a Python package for symbolic perturbative transformations on quantum systems. SymPT helps compute effective Hamiltonians for both time-independent and time-dependent systems at both operator and matrix level.","url":"https://github.com/qcode-uni-a/SymPT"}]

I found relevant research on this topic. Here are the key findings:

## Recent Work on SymPy Problem Generation and Verification (2025-2026)

Recent research has developed pipelines that represent problems using SymPy symbolic representations and produce problem-answer pairs for training. This represents an advancement beyond traditional natural language-based approaches.

### Symbolic Problem Generation

One key approach performs modifications in a symbolic problem space, representing each problem as a set of symbolic variables and constraints via algebraic frameworks such as SymPy. This converts problems to SymPy representations, abstracting away superficial features, which allows for more diverse and controlled problem generation compared to natural language methods.

### Verification Mechanisms

The research demonstrates sophisticated symbolic verification techniques:

- Symbolic validation simplifies the difference between extracted expressions and correct answers via SymPy.simplify, deeming answers correct if the simplification reduces the difference to zero.

- Advanced approaches verify each arithmetic operation via sympy, check logical flow consistency across reasoning steps, and enforce domain constraints.

### Automated Pipelines

Recent frameworks stabilize iterative self-training by embedding a symbolic verification subsystem that gates training data quality at the reasoning step level. This creates closed-loop pipelines where verification quality directly influences which generated problems enter training datasets.

The research indicates this is an active area with multiple papers published in 2025-2026 exploring different aspects of automated problem generation and verification using symbolic mathematics tools.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11cedf00-0433-4db1-b7fe-58091474a3f5",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "755bcf70-38d4-4f0f-b1f0-21571f226cc8",
  "toolUseResult": {
    "query": "SymPy math problem perturbation generation symbolic verification equivalent problem pairs automated pipeline 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TkDJ4nMVLH9Q4b382bCnEW",
        "content": [
          {
            "title": "Adaptive Problem Generation via Symbolic Representations",
            "url": "https://arxiv.org/html/2602.19187"
          },
          {
            "title": "ASyMOB: Algebraic Symbolic Mathematical Operations Benchmark",
            "url": "https://arxiv.org/html/2505.23851v1"
          },
          {
            "title": "Test-time Scaling Techniques in Theoretical Physics -",
            "url": "https://ml4physicalsciences.github.io/2025/files/NeurIPS_ML4PS_2025_20.pdf"
          },
          {
            "title": "SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation",
            "url": "https://arxiv.org/pdf/2510.25975"
          },
          {
            "title": "Adaptive Problem Generation via Symbolic Representations",
            "url": "https://arxiv.org/pdf/2602.19187"
          },
          {
            "title": "Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment",
            "url": "https://arxiv.org/html/2603.21558"
          },
          {
            "title": "Mixed Symbolic-Numeric Perturbation Theory · Symbolics.jl",
            "url": "https://docs.sciml.ai/Symbolics/stable/examples/perturbation/"
          },
          {
            "title": "Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification",
            "url": "https://arxiv.org/pdf/2603.19715"
          },
          {
            "title": "GitHub - qcode-uni-a/sympt: Symbolic Perturbation Theory (SymPT) is a Python package for symbolic perturbative transformations on quantum systems. SymPT helps compute effective Hamiltonians for both time-independent and time-dependent systems at both operator and matrix level.",
            "url": "https://github.com/qcode-uni-a/SymPT"
          }
        ]
      },
      "I found relevant research on this topic. Here are the key findings:\n\n## Recent Work on SymPy Problem Generation and Verification (2025-2026)\n\nRecent research has developed pipelines that represent problems using SymPy symbolic representations and produce problem-answer pairs for training. This represents an advancement beyond traditional natural language-based approaches.\n\n### Symbolic Problem Generation\n\nOne key approach performs modifications in a symbolic problem space, representing each problem as a set of symbolic variables and constraints via algebraic frameworks such as SymPy. This converts problems to SymPy representations, abstracting away superficial features, which allows for more diverse and controlled problem generation compared to natural language methods.\n\n### Verification Mechanisms\n\nThe research demonstrates sophisticated symbolic verification techniques:\n\n- Symbolic validation simplifies the difference between extracted expressions and correct answers via SymPy.simplify, deeming answers correct if the simplification reduces the difference to zero.\n\n- Advanced approaches verify each arithmetic operation via sympy, check logical flow consistency across reasoning steps, and enforce domain constraints.\n\n### Automated Pipelines\n\nRecent frameworks stabilize iterative self-training by embedding a symbolic verification subsystem that gates training data quality at the reasoning step level. This creates closed-loop pipelines where verification quality directly influences which generated problems enter training datasets.\n\nThe research indicates this is an active area with multiple papers published in 2025-2026 exploring different aspects of automated problem generation and verification using symbolic mathematics tools."
    ],
    "durationSeconds": 9.05912964900001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "11cedf00-0433-4db1-b7fe-58091474a3f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-29T05:58:16.152Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018A5PVmCL6iaTiPEdwEgXTb`</summary>

```json
{
  "query": "\"contrastive discrimination\" \"semantically different\" math reasoning training negative examples hard negatives 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "755bcf70-38d4-4f0f-b1f0-21571f226cc8",
  "isSidechain": false,
  "requestId": "req_011CbWM5xMaAu8PywfgEq4tH",
  "type": "assistant",
  "uuid": "3b288716-d2da-4f6a-8ef0-2dc1d54f95ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AukJ5jkRjS2fkp71B8kA54",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 27291,
      "output_tokens": 76,
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
          "output_tokens": 76,
          "cache_read_input_tokens": 27291,
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

_source line 44 · 2026-05-29T05:58:24.274Z_

<details><summary>↩ Tool result · `toolu_018A5PVmCL6iaTiPEdwEgXTb`</summary>

```text
Web search results for query: ""contrastive discrimination" "semantically different" math reasoning training negative examples hard negatives 2025 2026"

Links: [{"title":"Contrastive Learning with Hard Negatives","url":"https://www.emergentmind.com/topics/contrastive-learning-with-hard-negative-samples"},{"title":"Contrastive Learning with Hard Negative Samples | by It's Amit | Medium","url":"https://mr-amit.medium.com/contrastive-learning-with-hard-negative-samples-2cccb609fa0c"},{"title":"On the Selection of Positive and Negative Samples for Contrastive Math Word Problem Neural Solver","url":"https://educationaldatamining.org/edm2024/proceedings/2024.EDM-long-papers.8/index.html"},{"title":"MMGeoLM: Hard Negative Contrastive Learning for Fine-Grained Geometric Understanding in Large Multimodal Models","url":"https://arxiv.org/html/2505.20152"},{"title":"[2010.06682] Are all negatives created equal in contrastive instance discrimination?","url":"https://ar5iv.labs.arxiv.org/html/2010.06682"},{"title":"Visual Perturbation and Adaptive Hard Negative Contrastive Learning for Compositional Reasoning in Vision-Language Models","url":"https://arxiv.org/pdf/2505.15576"},{"title":"Hard Negative Sampling Strategies for Contrastive Representation   Learning","url":"https://arxiv.org/pdf/2206.01197"}]

Based on my search results, here are the key findings about contrastive discrimination with semantically different examples and hard negatives in math reasoning training:

## Core Concept

Contrastive learning with hard negatives is a technique that uses semantically challenging negative samples to refine embedding spaces and enhance model convergence. Contrastive learning with hard negative samples refers to the incorporation of particularly challenging negative examples—negatives that are semantically or representationally close to an anchor—in the loss-driven framework of contrastive representation learning.

## Application to Math Reasoning

Recent work has specifically applied these techniques to math problem solving. The contrastive learning framework can assist models in identifying semantically similar examples while distinguishing between different mathematical logics. Some studies utilize contrastive learning frameworks to assist models in discovering semantically similar examples while discerning those with different mathematical logics in a fine-grained manner.

## Recent 2025 Work

A notable 2025 paper addresses hard negative contrastive learning specifically for mathematical reasoning: To achieve more robust and semantically meaningful alignment, it is crucial to incorporate hard negative samples—semantically similar but mismatched pairs—which push the vision encoder to learn finer distinctions beyond shallow correlations. The comparison of geometric reasoning performance on MM-Math across LMMs with vision encoders trained with different hard negative data involved two types of hard negative sample construction methods, i.e., image-based and text-based.

The search results emphasize that properly balancing and constructing hard negatives—examples that are semantically similar to positive examples but have important distinctions—is key for training models to develop more discriminative reasoning capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b288716-d2da-4f6a-8ef0-2dc1d54f95ea",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "df88b117-e294-45bc-94f4-cc5d4cfdec00",
  "toolUseResult": {
    "query": "\"contrastive discrimination\" \"semantically different\" math reasoning training negative examples hard negatives 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014EaBAcQDc1JUJNKywu7pVD",
        "content": [
          {
            "title": "Contrastive Learning with Hard Negatives",
            "url": "https://www.emergentmind.com/topics/contrastive-learning-with-hard-negative-samples"
          },
          {
            "title": "Contrastive Learning with Hard Negative Samples | by It's Amit | Medium",
            "url": "https://mr-amit.medium.com/contrastive-learning-with-hard-negative-samples-2cccb609fa0c"
          },
          {
            "title": "On the Selection of Positive and Negative Samples for Contrastive Math Word Problem Neural Solver",
            "url": "https://educationaldatamining.org/edm2024/proceedings/2024.EDM-long-papers.8/index.html"
          },
          {
            "title": "MMGeoLM: Hard Negative Contrastive Learning for Fine-Grained Geometric Understanding in Large Multimodal Models",
            "url": "https://arxiv.org/html/2505.20152"
          },
          {
            "title": "[2010.06682] Are all negatives created equal in contrastive instance discrimination?",
            "url": "https://ar5iv.labs.arxiv.org/html/2010.06682"
          },
          {
            "title": "Visual Perturbation and Adaptive Hard Negative Contrastive Learning for Compositional Reasoning in Vision-Language Models",
            "url": "https://arxiv.org/pdf/2505.15576"
          },
          {
            "title": "Hard Negative Sampling Strategies for Contrastive Representation   Learning",
            "url": "https://arxiv.org/pdf/2206.01197"
          }
        ]
      },
      "Based on my search results, here are the key findings about contrastive discrimination with semantically different examples and hard negatives in math reasoning training:\n\n## Core Concept\n\nContrastive learning with hard negatives is a technique that uses semantically challenging negative samples to refine embedding spaces and enhance model convergence. Contrastive learning with hard negative samples refers to the incorporation of particularly challenging negative examples—negatives that are semantically or representationally close to an anchor—in the loss-driven framework of contrastive representation learning.\n\n## Application to Math Reasoning\n\nRecent work has specifically applied these techniques to math problem solving. The contrastive learning framework can assist models in identifying semantically similar examples while distinguishing between different mathematical logics. Some studies utilize contrastive learning frameworks to assist models in discovering semantically similar examples while discerning those with different mathematical logics in a fine-grained manner.\n\n## Recent 2025 Work\n\nA notable 2025 paper addresses hard negative contrastive learning specifically for mathematical reasoning: To achieve more robust and semantically meaningful alignment, it is crucial to incorporate hard negative samples—semantically similar but mismatched pairs—which push the vision encoder to learn finer distinctions beyond shallow correlations. The comparison of geometric reasoning performance on MM-Math across LMMs with vision encoders trained with different hard negative data involved two types of hard negative sample construction methods, i.e., image-based and text-based.\n\nThe search results emphasize that properly balancing and constructing hard negatives—examples that are semantically similar to positive examples but have important distinctions—is key for training models to develop more discriminative reasoning capabilities."
    ],
    "durationSeconds": 8.117539133000014,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3b288716-d2da-4f6a-8ef0-2dc1d54f95ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-29T05:58:27.436Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SdiLNYGFDd3ucZEMMp1aaT`</summary>

```json
{
  "query": "GRPO-CARE consistency aware RL video reasoning arXiv 2506.16141 experimental design ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df88b117-e294-45bc-94f4-cc5d4cfdec00",
  "isSidechain": false,
  "requestId": "req_011CbWM6r6p4JZuyM5T9PGxN",
  "type": "assistant",
  "uuid": "4dc5394e-845d-4d35-a4d4-5e17b404e18a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PrgzSEzA536pZDtY9gnc5b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 848,
      "cache_read_input_tokens": 28164,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 848,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 28164,
          "cache_creation_input_tokens": 848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 848
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

_source line 46 · 2026-05-29T05:58:35.763Z_

<details><summary>↩ Tool result · `toolu_01SdiLNYGFDd3ucZEMMp1aaT`</summary>

```text
Web search results for query: "GRPO-CARE consistency aware RL video reasoning arXiv 2506.16141 experimental design ablation"

Links: [{"title":"[2506.16141] GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning","url":"https://arxiv.org/abs/2506.16141"},{"title":"GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning | alphaXiv","url":"https://www.alphaxiv.org/abs/2506.16141"},{"title":"GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250616141C/abstract"},{"title":"(PDF) GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning","url":"https://www.researchgate.net/publication/392917728_GRPO-CARE_Consistency-Aware_Reinforcement_Learning_for_Multimodal_Reasoning"},{"title":"GRPO-CARE: Consistency-Aware Reinforcement Learning ...","url":"https://arxiv.org/pdf/2506.16141"},{"title":"TencentARC/GRPO-CARE · Hugging Face","url":"https://huggingface.co/TencentARC/GRPO-CARE"},{"title":"[PDF] GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GRPO-CARE:-Consistency-Aware-Reinforcement-Learning-Chen-Ge/b0dce6b8dcd3f20b04ceff4b0d9db193057fa186"},{"title":"Paper page - GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning","url":"https://huggingface.co/papers/2506.16141"},{"title":"GitHub - TencentARC/GRPO-CARE","url":"https://github.com/TencentARC/GRPO-CARE"}]

Based on the search results, here's what I found about GRPO-CARE:

## Overview
GRPO-CARE addresses the adaptation of reinforcement learning approaches to multimodal LLMs (MLLMs), with the introduction of SEED-Bench-R1, a benchmark with complex real-world videos requiring balanced perception and reasoning.

## Problem Identification
Standard GRPO, while improving answer accuracy, often reduces logical coherence between reasoning steps and answers, with only a 57.9% consistency rate. This stems from reward signals focusing solely on final answers, encouraging shortcuts, and strict KL penalties limiting exploration.

## Proposed Solution
GRPO-CARE introduces a two-tiered reward: (1) a base reward for answer correctness, and (2) an adaptive consistency bonus, computed by comparing the model's reasoning-to-answer likelihood (via a slowly-evolving reference model) against group peers.

## Experimental Design & Evaluation
SEED-Bench-R1 offers a large training set and evaluates generalization across three escalating challenges: in-distribution, cross-environment, and cross-environment-task scenarios.

The paper was published on June 19, 2025, and code is available at the TencentARC GitHub repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dc5394e-845d-4d35-a4d4-5e17b404e18a",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "200fbf04-c4f5-43e3-b4e2-3d92a354e6d1",
  "toolUseResult": {
    "query": "GRPO-CARE consistency aware RL video reasoning arXiv 2506.16141 experimental design ablation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ArWBveYUGRFnp2ix63CrhQ",
        "content": [
          {
            "title": "[2506.16141] GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning",
            "url": "https://arxiv.org/abs/2506.16141"
          },
          {
            "title": "GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2506.16141"
          },
          {
            "title": "GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250616141C/abstract"
          },
          {
            "title": "(PDF) GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning",
            "url": "https://www.researchgate.net/publication/392917728_GRPO-CARE_Consistency-Aware_Reinforcement_Learning_for_Multimodal_Reasoning"
          },
          {
            "title": "GRPO-CARE: Consistency-Aware Reinforcement Learning ...",
            "url": "https://arxiv.org/pdf/2506.16141"
          },
          {
            "title": "TencentARC/GRPO-CARE · Hugging Face",
            "url": "https://huggingface.co/TencentARC/GRPO-CARE"
          },
          {
            "title": "[PDF] GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GRPO-CARE:-Consistency-Aware-Reinforcement-Learning-Chen-Ge/b0dce6b8dcd3f20b04ceff4b0d9db193057fa186"
          },
          {
            "title": "Paper page - GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning",
            "url": "https://huggingface.co/papers/2506.16141"
          },
          {
            "title": "GitHub - TencentARC/GRPO-CARE",
            "url": "https://github.com/TencentARC/GRPO-CARE"
          }
        ]
      },
      "Based on the search results, here's what I found about GRPO-CARE:\n\n## Overview\nGRPO-CARE addresses the adaptation of reinforcement learning approaches to multimodal LLMs (MLLMs), with the introduction of SEED-Bench-R1, a benchmark with complex real-world videos requiring balanced perception and reasoning.\n\n## Problem Identification\nStandard GRPO, while improving answer accuracy, often reduces logical coherence between reasoning steps and answers, with only a 57.9% consistency rate. This stems from reward signals focusing solely on final answers, encouraging shortcuts, and strict KL penalties limiting exploration.\n\n## Proposed Solution\nGRPO-CARE introduces a two-tiered reward: (1) a base reward for answer correctness, and (2) an adaptive consistency bonus, computed by comparing the model's reasoning-to-answer likelihood (via a slowly-evolving reference model) against group peers.\n\n## Experimental Design & Evaluation\nSEED-Bench-R1 offers a large training set and evaluates generalization across three escalating challenges: in-distribution, cross-environment, and cross-environment-task scenarios.\n\nThe paper was published on June 19, 2025, and code is available at the TencentARC GitHub repository."
    ],
    "durationSeconds": 8.323570704999991,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4dc5394e-845d-4d35-a4d4-5e17b404e18a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-29T05:58:38.272Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011CdMyy8UezY99SE9isBc8g`</summary>

```json
{
  "query": "COPO consistency entropy zero advantage GRPO arXiv 2508.04138 experimental methodology baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "200fbf04-c4f5-43e3-b4e2-3d92a354e6d1",
  "isSidechain": false,
  "requestId": "req_011CbWM7hFXwGuWpovTjGp9g",
  "type": "assistant",
  "uuid": "15a9ba90-1368-4bdf-a4d2-94becc690cc9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113GRMVpWA2dHAPvaHw8oKg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 939,
      "cache_read_input_tokens": 29012,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 939,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 29012,
          "cache_creation_input_tokens": 939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 939
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

_source line 48 · 2026-05-29T05:58:49.455Z_

<details><summary>↩ Tool result · `toolu_011CdMyy8UezY99SE9isBc8g`</summary>

```text
Web search results for query: "COPO consistency entropy zero advantage GRPO arXiv 2508.04138 experimental methodology baselines"

Links: [{"title":"COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/html/2508.04138v1"},{"title":"[2508.04138v1] COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/abs/2508.04138v1"},{"title":"COPO: Consistency-Aware Policy Optimization Jinghang Han1*, Jiawei Chen1,2*,","url":"https://arxiv.org/pdf/2508.04138"},{"title":"[2508.04138] COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/abs/2508.04138"},{"title":"EDGE-GRPO: Entropy-Driven GRPO with Guided Error Correction for Advantage Diversity","url":"https://arxiv.org/pdf/2507.21848"}]

Based on the search results, I found information about the paper you're looking for:

## COPO: Consistency-Aware Policy Optimization (arXiv 2508.04138)

The paper addresses a common challenge where when multiple sampled responses under a single prompt converge to identical outcomes, the group-based advantage degenerates to zero, leading to vanishing gradients and rendering the corresponding samples ineffective for learning.

### Key Methodology

COPO proposes a novel consistency-entropy-based policy optimization framework that theoretically addresses the sample wastage and gradient vanishing problem under extreme samples observed in GRPO methods, introducing a structured global reward based on outcome consistency and a global optimization mechanism, with an entropy-based soft blending mechanism that adaptively balances local advantage estimation with global optimization.

### Performance and Baselines

By effectively leveraging the information embedded in challenging training data, COPO achieves an important improvement over GRPO, suggesting that fully utilizing intra-group data with zero advantage values contributes positively to the training process. The paper demonstrates performance improvement of COPO over GRPO methods in mathematical reasoning tasks and conducts extensive ablation studies on various existing improvements to GRPO training schemes.

The research directly addresses how to handle samples with zero advantage values that would otherwise be wasted in GRPO-based training methodologies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15a9ba90-1368-4bdf-a4d2-94becc690cc9",
  "isSidechain": false,
  "promptId": "f952f479-9f01-437b-a39f-4bd60f11e7ee",
  "type": "user",
  "uuid": "591c938c-5fb0-4423-ace6-8e9b02f93a4c",
  "toolUseResult": {
    "query": "COPO consistency entropy zero advantage GRPO arXiv 2508.04138 experimental methodology baselines",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UdVyAqwgjtPmAABJTYpVRm",
        "content": [
          {
            "title": "COPO: Consistency-Aware Policy Optimization",
            "url": "https://arxiv.org/html/2508.04138v1"
          },
          {
            "title": "[2508.04138v1] COPO: Consistency-Aware Policy Optimization",
            "url": "https://arxiv.org/abs/2508.04138v1"
          },
          {
            "title": "COPO: Consistency-Aware Policy Optimization Jinghang Han1*, Jiawei Chen1,2*,",
            "url": "https://arxiv.org/pdf/2508.04138"
          },
          {
            "title": "[2508.04138] COPO: Consistency-Aware Policy Optimization",
            "url": "https://arxiv.org/abs/2508.04138"
          },
          {
            "title": "EDGE-GRPO: Entropy-Driven GRPO with Guided Error Correction for Advantage Diversity",
            "url": "https://arxiv.org/pdf/2507.21848"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\n## COPO: Consistency-Aware Policy Optimization (arXiv 2508.04138)\n\nThe paper addresses a common challenge where when multiple sampled responses under a single prompt converge to identical outcomes, the group-based advantage degenerates to zero, leading to vanishing gradients and rendering the corresponding samples ineffective for learning.\n\n### Key Methodology\n\nCOPO proposes a novel consistency-entropy-based policy optimization framework that theoretically addresses the sample wastage and gradient vanishing problem under extreme samples observed in GRPO methods, introducing a structured global reward based on outcome consistency and a global optimization mechanism, with an entropy-based soft blending mechanism that adaptively balances local advantage estimation with global optimization.\n\n### Performance and Baselines\n\nBy effectively leveraging the information embedded in challenging training data, COPO achieves an important improvement over GRPO, suggesting that fully utilizing intra-group data with zero advantage values contributes positively to the training process. The paper demonstrates performance improvement of COPO over GRPO methods in mathematical reasoning tasks and conducts extensive ablation studies on various existing improvements to GRPO training schemes.\n\nThe research directly addresses how to handle samples with zero advantage values that would otherwise be wasted in GRPO-based training methodologies."
    ],
    "durationSeconds": 11.179118313000014,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "15a9ba90-1368-4bdf-a4d2-94becc690cc9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-29T05:59:34.388Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the landscape. Let me synthesize my findings and provide a comprehensive assessment of the experimental design and feasibility of this proposal.

Key observations from my research:

1. **ROMA** (arXiv 2605.09262): Uses dual-forward-pass, correctness-conditioned KL penalty, worst-case augmentation selection. Tested on Qwen3-VL 4B/8B across 7 benchmarks. This is the closest cousin.

2. **VAR-MATH** (arXiv 2507.12885): Uses loose and strict consistency metrics with bootstrapping on AMC23, AIME24, AIME25 variants. 

VAR-MATH shows significant performance degradation in the 47-73% range.

3. **MATH-Perturb** (ICML 2025): Creates 279 perturbed problems from MATH level-5, varying between simple and hard perturbation types.

4. **AbstRaL** (ICLR 2026): Evaluated on GSM-Symbolic and GSM-Plus using RL with model-free rewards for abstraction, but limited to GSM-level problems.

5. **TA-GRPO**: Takes an augmentation-based approach without consistency loss, evaluated on Minerva and GPQA-Diamond.

6. **GSM-Symbolic**

—a benchmark with 50 instantiations per problem across 100 problems, evaluating 25 models.

7. **GRPO-CARE**: Applies consistency-aware RL to video reasoning with a two-tiered reward structure that includes an adaptive consistency bonus.

8. **F2C**: Uses JS divergence for NLU tasks with SFT-only training.

9. **PrAg-PO**: Applies prompt augmentation to improve GRPO training stability.

Looking at the experimental design, the proposal plans to train Qwen3-8B using verl/DAPO and test it on VAR-MATH, MATH-Perturb, and the Robust Reasoning Benchmark, but I notice the baseline comparisons aren't clearly specified. The most glaring gap is the absence of AbstRaL as a baseline. directly relevant competitor for math robustness via RL (ICLR 2026)
  2. **TA-GRPO/PrAg-PO** - augmentation-only approaches (these are natural ablation baselines showing the value of the consistency loss)
  3. **Standard GRPO** - obvious baseline
  4. **SFT baseline** - standard
  5. **Vanilla Qwen3-8B** - base model
  6. **F2C-style consistency applied to RL** - to show that math-specific perturbation matters vs. generic consistency

**Evaluation Gaps:**
1. The proposal evaluates on VAR-MATH, MATH-Perturb, and Robust Reasoning Benchmark, which are all robustness-focused, but there are some issues. They're missing clean accuracy measurements on standard benchmarks like MATH and GSM8K to ensure no performance degradation, and they haven't included GSM-Symbolic, GSM-Plus (the standard robustness benchmarks from AbstRaL), or AIME 2025 as an out-of-distribution generalization test.

2. **Perturbation types**: The proposal only mentions numerical substitution and variable renaming as SymPy perturbations, which is quite limited compared to what other benchmarks use—MATH-Perturb distinguishes simple vs. hard perturbations, GSM-Symbolic has multiple perturbation types across names, values, and clauses, and the Robust Reasoning Benchmark employs 14 different perturbation techniques. The proposal's coverage here seems narrow.

3. **JS divergence computation**: The proposal mentions JS-divergence over "reasoning distributions" between original and perturbed inputs, but this is vague—what exactly is the "reasoning distribution"? Is it token-level logits or sequence-level distributions? This ambiguity matters for implementation and ablation studies.

**Ablation Design:**
The proposal has three components: (1) SymPy perturbation generator, (2) correctness-conditioned JS-divergence loss, (3) contrastive discrimination loss. A proper ablation would need:
1. GRPO only (no consistency)
2. GRPO + perturbation (augmentation only, like TA-GRPO)
3. GRPO + perturbation + JS loss (without correctness conditioning)
4. GRPO + perturbation + correctness-conditioned JS loss (without contrastive)
5. Full MACR (all three)
6. Variants of JS weighting coefficient

**Feasibility concerns:**
The perturbation generator seems narrower than what these benchmarks test, and the JS-divergence computation needs clarification on what "reasoning distribution" means—whether it's token-level logits or sequence-level distributions. The ablation design is comprehensive but requires careful implementation to isolate each component's contribution.

Training Qwen3-8B on verl/DAPO is feasible with 8x A100/H100 or RTX 4090 GPUs at around $1-2K per run, and the SymPy perturbation generator is implementable with careful engineering. However, the dual-forward-pass approach doubles compute per step, and generating "surface-similar but semantically-different" problems for the contrastive loss is underspecified and potentially harder than creating equivalent variants. The correctness conditioning also adds overhead by requiring both variants to be solved correctly during training.

For fair comparison, I need to account for the fact that this method effectively uses 2x the data and extra forward passes compared to standard GRPO, so compute-normalized comparisons are essential. I'm also realizing several critical gaps: the baseline specification is vague with no explicit list, AbstRaL is missing as the most relevant baseline for math robustness via RL, standard benchmarks like GSM-Symbolic and GSM-Plus aren't mentioned, clean accuracy preservation isn't explicitly planned, and the ablation design is incomplete.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "591c938c-5fb0-4423-ace6-8e9b02f93a4c",
  "isSidechain": false,
  "requestId": "req_011CbWM8hnJgT35B5px6UQtz",
  "type": "assistant",
  "uuid": "d1c9f64c-3fb1-414c-8173-a988b7bee7bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxQX6WoDiANmCtUwgQoExL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 29951,
      "output_tokens": 7308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7308,
          "cache_read_input_tokens": 29951,
          "cache_creation_input_tokens": 654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 654
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

_source line 50 · 2026-05-29T06:01:23.865Z_

Now I have sufficient research to make a thorough assessment. Let me compile my findings.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **ROMA (arXiv 2605.09262, 2026)**: 使用 dual-forward-pass 训练策略，correctness-conditioned token-level KL penalty，worst-case augmentation selection。Baselines 包括 standard GRPO、SFT、vanilla model。评测覆盖 7 个 multimodal reasoning benchmark，分别报告 seen/unseen corruption 和 clean accuracy。Ablation 隔离了 correctness-conditioning、worst-case selection、auxiliary PG loss 各组件。
- **AbstRaL (ICLR 2026)**: 针对 GSM robustness，使用 RL + symbolic abstraction。评测在 GSM-Symbolic 和 GSM-Plus 上进行，同时报告 OOD math reasoning 和 general reasoning 能力。Baselines 包括 SFT、standard RL、各种 prompting 方法。这是当前最直接的 math robustness via RL 竞品。
- **TA-GRPO (arXiv 2601.22478, 2025)**: 使用语义等价变换扩增 GRPO 训练数据（paraphrasing, variable renaming, format changes），但不加 consistency loss。报告 Pass@k 指标和 zero-gradient question 比例。对比 GRPO、DAPO。
- **PrAg-PO (arXiv 2602.03190, 2026)**: Prompt augmentation stabilize GRPO training，评测覆盖 AIME24, AMC, MATH500, Minerva, OlympiadBench。关注 entropy collapse 现象。
- **GSM-Symbolic (ICLR 2025)**: 标准 math robustness 评测 benchmark，每个 template 50 个 instantiation，评测 25 个模型。区分 name/value/clause 等 perturbation 类型。GSM-Plus 是扩展版。
- **MATH-Perturb (ICML 2025)**: 279 道 MATH level-5 题目，区分 simple perturbation (同解法) 和 hard perturbation (需新解法)。
- **Robust Reasoning Benchmark (arXiv 2604.08571, 2026)**: 14 种 perturbation technique 应用于 AIME 2024，区分结构扰动和上下文污染。
- **GRPO-CARE (arXiv 2506.16141, 2025)**: 在 video reasoning 中使用 two-tiered reward (correctness + adaptive consistency bonus)，设计了 SEED-Bench-R1 的 in-distribution / cross-environment / cross-task 三级评估。
- **F2C (arXiv 2510.14242, 2025)**: JS divergence + KL divergence for NLU prompt robustness，SFT-only。评测 11 个 NLU dataset，报告 observed agreement、mean F1、performance variance。
- 调研总结: 该领域当前的实验设计标准要求 **(a)** 明确对比 augmentation-only 和 consistency-regularized 方法，**(b)** 同时报告 clean accuracy 和 robustness gains，**(c)** 在 GSM-Symbolic/GSM-Plus 等标准 robustness benchmark 上评测（这是 ICLR 2025/2026 的标配），**(d)** 通过完整 ablation 隔离每个组件的贡献，**(e)** 讨论 compute overhead 和 compute-normalized comparison。

---

【缺陷 1】
- 类别: baseline 不足或过时
- 问题: Proposal 未明确列出任何对比 baseline。仅提到"train Qwen3-8B via verl/DAPO"，但没有说明会与哪些方法做对比。最关键的遗漏是 **AbstRaL (ICLR 2026)**——这是当前唯一已发表的通过 RL 提升 math reasoning robustness 的方法，且同样针对 GSM-level 问题。如果论文不与 AbstRaL 对比，审稿人几乎必然要求补充。此外，**TA-GRPO** 和 **PrAg-PO** 作为 augmentation-only（无 consistency loss）的 GRPO 变体，是验证 consistency regularization 增量价值的天然对照，也缺失。
- 严重度: 可补救
- 补救方案: 明确列出以下 baseline 层次：
  1. **Vanilla Qwen3-8B**（无 RL fine-tuning）
  2. **Standard GRPO**（verl/DAPO，无任何 augmentation 或 consistency）
  3. **TA-GRPO / PrAg-PO**（augmentation-only GRPO，无 consistency loss——验证 consistency loss 的增量价值）
  4. **AbstRaL**（symbolic abstraction + RL——当前最直接竞品，若无法复现可引用其公开结果并在相同评测 benchmark 上对齐）
  5. **F2C-style consistency applied to RL**（将 generic JS consistency 应用于 GRPO 而不使用 math-specific perturbation——验证 math-aware perturbation 的价值）
  6. **ROMA**（如果 code 可用，适配到 text-only 的变体；否则在 methodology 层面做对比分析）
- 调研依据: AbstRaL (ICLR 2026) 是同领域同任务的 accepted paper；TA-GRPO 和 PrAg-PO 是审稿人最自然会想到的 augmentation-only 对照

【缺陷 2】
- 类别: 实验设计不足
- 问题: 评测 benchmark 覆盖不完整。Proposal 列出了 VAR-MATH、MATH-Perturb 和 Robust Reasoning Benchmark 三个 robustness benchmark，但遗漏了 **GSM-Symbolic** (ICLR 2025) 和 **GSM-Plus**——这两个是 math reasoning robustness 领域最被广泛引用的标准评测，AbstRaL 的核心评测就在这上面。此外，proposal 未明确说明会在哪些 **clean benchmarks** 上评测以验证 "clean accuracy preservation" 这一核心 claim（如 MATH、GSM8K、AIME 2025 等）。
- 严重度: 可补救
- 补救方案: 
  1. 增加 **GSM-Symbolic** 和 **GSM-Plus** 作为 robustness evaluation 标准评测
  2. 明确列出 clean accuracy 评测 benchmark：至少包括 **MATH500**、**GSM8K**、**AIME 2024/2025**
  3. 最好增加 OOD generalization 测试（如 Minerva、OlympiadBench）以验证 robustness training 没有过拟合到特定扰动类型
- 调研依据: GSM-Symbolic (ICLR 2025) 和 GSM-Plus 是 AbstRaL 的核心评测 benchmark；ROMA 同时报告 clean 和 corrupted performance

【缺陷 3】
- 类别: ablation 不完整
- 问题: Proposal 描述了三个核心组件——(1) SymPy perturbation generator, (2) correctness-conditioned JS-divergence loss, (3) contrastive discrimination loss——但未明确设计 ablation study 来隔离每个组件的贡献。ROMA 在其 ablation 中明确隔离了 correctness-conditioning、worst-case selection、auxiliary PG loss 的各自贡献，审稿人会期望类似的分析。
- 严重度: 可补救
- 补救方案: 设计以下 ablation 矩阵：
  - A1: GRPO only（无 augmentation，无 consistency）→ baseline
  - A2: GRPO + perturbation augmentation（仅数据扩增，无 consistency loss）→ 隔离 augmentation 效果
  - A3: GRPO + perturbation + **unconditional** JS loss（不做 correctness conditioning）→ 验证 correctness conditioning 的必要性
  - A4: GRPO + perturbation + correctness-conditioned JS loss（无 contrastive discrimination）→ 核心 consistency 组件
  - A5: Full MACR（所有三个组件）→ 完整方法
  - A6: JS loss weight sensitivity analysis（λ 的不同取值）→ 超参数稳定性
  - A7: 不同 perturbation 类型的贡献（仅 numerical substitution vs. 仅 variable renaming vs. both）
- 调研依据: ROMA 论文的 ablation 设计风格，以及 GRPO-CARE 的 component-wise ablation

【缺陷 4】
- 类别: 实验设计不足
- 问题: Proposal 中"contrastive discrimination loss against surface-similar but semantically-different problems"这一组件的**数据构造方案完全未说明**。生成"表面相似但语义不同"的数学问题比生成等价变体难得多——等价变体可以通过 SymPy 自动验证，但语义不同的 hard negative 需要确保：(a) 表面 token overlap 高但答案不同，(b) 难度相当，(c) 数量足够覆盖训练集。这不是一个 trivial 的数据工程问题。
- 严重度: 可补救
- 补救方案: 明确 hard negative 构造策略，可选方案：
  1. **Answer-preserving vs. answer-changing perturbation**: 在 SymPy 中修改约束条件使答案改变（如改变方程中的一个系数使得最终答案不同），这可以自动化验证
  2. **从同 topic 不同 problem 中采样**: 从训练集中选择与当前 problem 相同数学领域但不同结构的问题作为 negative
  3. **MATH-Perturb 的 hard perturbation 思路**: 用其"改变解法路径"的 perturbation 作为 negative（问题表面相似但需要不同解题方法）
  4. 无论选择哪种，需在 paper 中报告 hard negative 的质量验证（如人工抽样检查 precision）
- 调研依据: MATH-Perturb (ICML 2025) 对 simple vs. hard perturbation 的区分提供了参考框架

【缺陷 5】
- 类别: compute 公平性问题
- 问题: MACR 的训练每个 step 需要处理原始问题 + 扰动变体 + contrastive negative，相当于 2-3x 的 forward pass 开销（类似 ROMA 的 dual-forward-pass）。与 standard GRPO 直接比较性能提升在审稿人看来是不公平的——额外性能可能仅来自看到了更多数据/做了更多 computation，而非 consistency loss 本身的贡献。
- 严重度: 可补救
- 补救方案:
  1. 进行 **compute-normalized comparison**: 给 standard GRPO 相同的额外 compute budget（如训练 2-3x 步数或 2-3x 的 batch size），确保 MACR 的提升不是仅来自额外计算
  2. 或者，像 TA-GRPO 那样，将 augmented data 直接加入 GRPO 训练（不加 consistency loss）作为 compute-matched baseline——这比 standard GRPO 更公平的对照
  3. 报告每个方法的 wall-clock training time 和 GPU hours
- 调研依据: ROMA 论文讨论了 dual-forward-pass 的额外 overhead；TA-GRPO 提供了 augmentation-only 作为 compute-matched baseline 的范例

【缺陷 6】
- 类别: 实验设计不足
- 问题: Proposal 中 JS-divergence 的计算对象——"reasoning distributions between original and perturbed inputs"——定义模糊。具体是 **(a)** token-level logit distribution 的 JS divergence（类似 ROMA 的 token-level KL），**(b)** sequence-level output distribution（如 rollout 的 answer distribution），还是 **(c)** reasoning step 级别的 representation？这三者的实现复杂度、计算开销和预期效果完全不同。ROMA 明确使用 token-level log-probability under teacher forcing；F2C 使用 output-level JS divergence。这一设计选择会直接影响方法的效果和效率。
- 严重度: 可补救
- 补救方案: 明确说明 JS divergence 的计算粒度，并最好在 ablation 中对比不同粒度的效果：
  1. **Token-level** (ROMA 风格): 在 teacher-forcing 下对每个 token 计算 logit distribution 的 JS divergence，优点是信号密集，缺点是可能对 reasoning path 中的无关 token 施加不必要的约束
  2. **Answer-level** (F2C 风格): 仅对最终答案的 distribution 做 JS divergence，优点是计算简单，缺点是信号稀疏
  3. **Reasoning-step-level**: 对关键 reasoning step 的 checkpoint 做 JS divergence（需要 step segmentation）
  推荐首选 token-level（与 ROMA 对齐，有先例），同时在 ablation 中对比 answer-level 以展示粒度选择的影响
- 调研依据: ROMA 明确使用 token-level log-probabilities under teacher forcing；F2C 使用 output-level divergence

【缺陷 7】
- 类别: 可行性问题
- 问题: SymPy perturbation generator 的覆盖范围——proposal 仅提到"numerical substitution and variable renaming"两种扰动类型。但 VAR-MATH 和 GSM-Symbolic 的 perturbation taxonomy 远不止这些：GSM-Symbolic 涵盖 names, values, clauses, structure；MATH-Perturb 区分 simple/hard perturbation；Robust Reasoning Benchmark 使用 14 种 perturbation technique（包括 context pollution, structural perturbation 等）。仅靠 numerical substitution 和 variable renaming 训练出的 robustness 可能在更广泛的 perturbation 类型上泛化不足，导致在评测 benchmark 上表现不佳。
- 严重度: 可补救
- 补救方案:
  1. 扩展 SymPy perturbation generator 的扰动类型：增加 **expression rewriting**（如 a+b → b+a）、**unit conversion**、**constraint reformulation**（如把"A 比 B 多 3"改为"B 比 A 少 3"）
  2. 明确区分 **训练时扰动**（用于 consistency regularization，需要 SymPy 可验证等价性）和 **评测时扰动**（由 benchmark 自身定义，可能包含非等价的 hard perturbation）
  3. 在实验中分析不同扰动类型上的 robustness gain 分布，识别哪些类型受益最大、哪些类型需要更多样化的训练扰动
  4. 可考虑补充 LLM-based paraphrasing（如 TA-GRPO 的方式）作为 SymPy 之外的补充扰动源
- 调研依据: GSM-Symbolic (ICLR 2025) 和 Robust Reasoning Benchmark (arXiv 2026) 的 perturbation taxonomy 远超 proposal 当前的覆盖范围

【缺陷 8】
- 类别: 评估方案缺陷
- 问题: Proposal 未定义 robustness 的量化评估指标。VAR-MATH 使用 loose/strict consistency metrics with bootstrapping；GSM-Symbolic 使用 performance variance across instantiations 和 performance drop rate；Robust Reasoning Benchmark 报告 per-perturbation-type accuracy drop。Proposal 应当明确将使用哪些指标来定义和量化 "perturbation robustness improvement"，否则 claim 缺乏可验证性。
- 严重度: 可补救
- 补救方案: 明确定义以下评估指标体系：
  1. **Clean Accuracy**: 标准 benchmark 上的 Pass@1（MATH500, GSM8K, AIME）
  2. **Robust Accuracy**: 各 perturbation benchmark 上的 Pass@1
  3. **Relative Performance Drop (RPD)**: (Clean - Robust) / Clean × 100%——核心 robustness 指标
  4. **Consistency Rate**: VAR-MATH 的 strict consistency（同一 template 所有 instantiation 全部正确的比例）
  5. **Performance Variance**: 同一 template 不同 instantiation 间的 accuracy variance（GSM-Symbolic 风格）
  6. 报告各指标的 mean ± std（多 seed 运行）
- 调研依据: VAR-MATH 的 loose/strict consistency metrics；GSM-Symbolic 的 variance-based evaluation

---

**总结**: Proposal 的核心 idea 方向（将 consistency regularization 引入 GRPO 进行 math robustness training）有 ROMA 在 visual domain 的成功先例支撑，技术上可行。但当前的实验设计存在 8 个可补救缺陷，主要集中在：**(1)** baseline 列表缺失（尤其是 AbstRaL 这一直接竞品），**(2)** 评测 benchmark 未覆盖标准的 GSM-Symbolic/GSM-Plus，**(3)** ablation 设计未明确，**(4)** contrastive negative 构造方案空白，**(5)** compute-normalized comparison 未考虑。这些缺陷均属实验规划层面，无方向性致命问题，但如果不补救，审稿人很可能要求 major revision 甚至 reject due to insufficient experiments。建议在正式实验前逐一补全上述方案。

Sources:
- [ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation](https://arxiv.org/abs/2605.09262)
- [VAR-MATH: Probing True Mathematical Reasoning](https://arxiv.org/abs/2507.12885)
- [AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking](https://arxiv.org/abs/2506.07751)
- [MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations](https://proceedings.mlr.press/v267/huang25k.html)
- [GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models](https://arxiv.org/abs/2410.05229)
- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478)
- [PrAg-PO: Prompt Augmentation Scales up GRPO Training](https://arxiv.org/abs/2602.03190)
- [GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning](https://arxiv.org/abs/2506.16141)
- [F2C: Flip-Flop Consistency for Prompt Perturbation Robustness](https://arxiv.org/abs/2510.14242)
- [COPO: Consistency-Aware Policy Optimization](https://arxiv.org/abs/2508.04138)
- [Robust Reasoning Benchmark](https://arxiv.org/html/2604.08571)
- [Qwen3-8B GRPO Training with verl](https://huggingface.co/blog/Weyaxi/engineering-handbook-grpo-lora-with-verl)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1c9f64c-3fb1-414c-8173-a988b7bee7bf",
  "isSidechain": false,
  "requestId": "req_011CbWM8hnJgT35B5px6UQtz",
  "type": "assistant",
  "uuid": "fb597862-0363-41c6-b1cc-0aed1b4d7e7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxQX6WoDiANmCtUwgQoExL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 29951,
      "output_tokens": 7308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7308,
          "cache_read_input_tokens": 29951,
          "cache_creation_input_tokens": 654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 654
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

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Consistency-Regularized RL for Perturbation-Robust Math Reasoning  ## Core Problem  RL-trained math reasoners suffer 47–73% accuracy drops under trivial surface perturbations despite SOTA on clean b…",
  "leafUuid": "fb597862-0363-41c6-b1cc-0aed1b4d7e7e",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Math RL robustness via consistency regularization",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Consistency-Regularized RL for Perturbation-Robust Math Reasoning  ## Core Problem  RL-trained math reasoners suffer 47–73% accuracy drops under trivial surface perturbations despite SOTA on clean b…",
  "leafUuid": "fb597862-0363-41c6-b1cc-0aed1b4d7e7e",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Math RL robustness via consistency regularization",
  "sessionId": "70c05fd7-3f98-4d36-8384-f3f7cae3d6b1"
}
```

---
