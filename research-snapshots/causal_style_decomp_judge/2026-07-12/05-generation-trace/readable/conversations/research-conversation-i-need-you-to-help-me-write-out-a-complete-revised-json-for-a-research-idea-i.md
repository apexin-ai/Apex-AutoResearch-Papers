# Research conversation: I need you to help me write out a complete revised JSON for a research idea. I will provide the full context and you sho

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a4296764d735dfe06.jsonl`
- **Structured JSON:** [`ac6c38c52ff8d9d29cf7.json`](../../sessions/ac/ac6c38c52ff8d9d29cf7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

42 recorded events

### User

_source line 1 · 2026-05-27T18:43:32.763Z_

I need you to help me write out a complete revised JSON for a research idea. I will provide the full context and you should output ONLY the complete JSON object.

## Context

This is round 4 of revision for a research idea called "TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization." The reviewer gave 5 issues and said 3 targeted fixes would bring it to pass quality. The stagnation warning suggests a major revision.

## Key changes to make (based on deep research)

### 1. SPECIFY CO-ADAPTIVE RETRIEVAL MECHANISM (MAJOR)
The reviewer's core complaint: "re-rank and update the retrieval index based on these signals" is vague. Is the retriever fine-tuned during TTRL?

**Solution**: Define a concrete dual-loop architecture with actual retriever parameter updates:
- The retriever (a DDR-style dense encoder) IS fine-tuned during TTRL using an InfoNCE contrastive loss
- Compilation errors provide the signal: Lean 4's `unknownIdentifier` errors explicitly name the missing Mathlib constant (e.g., `unknown identifier 'Finset.sum_comm'`), creating a direct mapping from failed formalization → needed dependency
- Hard-negative mining: when formalization fails with `unknownIdentifier X`, the currently retrieved dependencies that did NOT include X are hard negatives; X itself (looked up in the Mathlib index) becomes the positive
- When formalization succeeds and compiles, all retrieved dependencies used in the successful formalization are confirmed positives
- Retriever is updated every N_ret=50 GRPO steps using accumulated (query, positive_dep, negative_dep) triples with InfoNCE loss
- This draws on established precedent: R3 (NeurIPS 2025) uses RAG environment feedback for contrastive retriever training; Reinforced-IR (ACL 2025) alternates RLRF/RLGF for mutual retriever-generator adaptation; TTARAG (Jan 2026) adapts models at test time using self-supervised retrieval prediction
- The interaction with GRPO: retriever updates are decoupled from policy gradient steps (alternating optimization), preventing destabilization. The retriever's gradient does not flow through the formalizer's policy gradient.

### 2. ADDRESS DDRL-TO-AUTOFORMALIZATION ADAPTATION (MAJOR)
The reviewer's complaint: DDRL assumes binary correct/incorrect, but multi-tier reward R has continuous range.

**Solution**: Adopt a binarize-then-enrich strategy inspired by GDPO (NVIDIA, Jan 2026):
- **Binarization for DDRL's sampling and advantages**: Define binary acceptance as r_accept = I(r_compile=1 AND r_critic=1). This gives DDRL a clean binary signal.
  - Balanced sampling: partition K=32 candidates into "accepted" (compile + critic approves) and "rejected" (otherwise). Exclude problems where acceptance frequency falls in the ambiguous zone (30-70% acceptance rate), following DDRL's frequency-based filtering.
  - Fixed advantages: +1 for accepted, -1 for rejected candidates, eliminating GRPO's amplification pathway.
  - Consensus-based off-policy refinement: rejection sampling on high-confidence samples (>80% acceptance rate).
- **GDPO-style enrichment for BEq**: Among accepted candidates, apply GDPO's per-reward decoupled normalization to preserve the BEq consensus density signal as a secondary ranking bonus. The BEq component is normalized independently from the binary acceptance signal, preventing it from being collapsed (as standard GRPO would do). This adds a gradient bonus proportional to BEq consensus among accepted candidates without disturbing DDRL's debiasing.
- **Threshold justification**: τ = compile AND critic is natural because: (a) compilation is a hard prerequisite (non-negotiable binary gate), (b) the critic's 84.8% accuracy makes it the most informative single signal after compilation. The 30-70% ambiguous zone for balanced sampling means: if between ~10-22 of 32 candidates are accepted, the problem is too uncertain for reliable pseudo-labels—exactly DDRL's insight applied to multi-tier rewards.
- This is itself a contribution: adapting single-reward debiased RL to multi-tier rewards via binarize-then-enrich.

### 3. DE-RISK WITH MINIMAL PILOT (MAJOR)
**Phase 0 pilot experiment** before the full pipeline:
- Setup: Take FormaRL's GRPO pipeline, replace its LLM-consistency reward with CriticLean-14B as the reward signal
- Data: 200 problems from Con-NF (OOD for most models) + 200 from FormalMATH number theory (near-distribution)
- No retrieval, no curriculum, no DDRL debiasing—just vanilla GRPO with r_compile × r_critic
- Hypothesis: If CriticLean-14B reward achieves ≥3pp BEq@1 improvement over compilation-only GRPO on Con-NF, the core premise (semantic critic rewards enable OOD adaptation) is validated
- Secondary hypothesis: If the pilot shows >15% false reward rate (critic approves semantically wrong formalizations that happen to compile), we need critic calibration before proceeding to full pipeline
- Resource estimate: ~40 A100-hours, 1-2 weeks
- This pilot validates the two riskiest assumptions: (a) CriticLean rewards provide sufficient signal for RL, (b) the ~15.2% critic error rate doesn't introduce systematic bias during GRPO training

### 4. CITE "ONLINE RL FOR AUTOFORMALIZATION" (MINOR)
- Cite: "Online Reinforcement Learning for Autoformalization" (Haiming Wang et al., NeurIPS 2025 MAR Workshop)
- Uses GRPO with composite rewards (BEq + embedding-based similarity) for autoformalization in Lean 4
- Key distinction: online training-time RL with labeled/unlabeled data on in-distribution problems vs. TTRA's test-time RL on fully unlabeled OOD data with co-adaptive retrieval and semantic critic rewards
- They achieve TC1: 17.29%→26.01%, TC50: 76.41%→85.46% on RLMEval
- Position: closest prior work on RL for autoformalization, but lacks retrieval, test-time adaptation, and trained semantic critic

### 5. ADJUST TIMELINE (MINOR)
- Primary targets: EACL 2027 ARR August cycle (Aug 3, 2026) and NeurIPS 2026 Workshops (Aug 29, 2026)
- AAAI 2027 (July 21) is feasible ONLY with auto_research mode starting immediately (7-10 weeks from May 27 = July 15-Aug 5)—tight but possible for abstract deadline July 21 if pilot + Phase 1 are done
- ICLR 2027 remains the best fit for full pipeline results

### 6. ADD NEW REFERENCES
- GDPO: Group reward-Decoupled Normalization Policy Optimization (arXiv 2601.05242, NVIDIA, Jan 2026)
- R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning (NeurIPS 2025)
- Reinforced-IR: A Self-Boosting Framework for Domain-Adaptive Retrieval (ACL 2025)
- TTARAG: Predict the Retrieval! Test-Time Adaptation for RAG (arXiv 2601.11443, Jan 2026)
- Online Reinforcement Learning for Autoformalization (NeurIPS 2025 MAR Workshop)

Now output the COMPLETE JSON. Here is the format - ALL fields must be present:

```json
{
  "title": "...",
  "core_problem": "...",
  "opportunity": "...",
  "landscape": "...",
  "inspired_by": "...",
  "approach": "...",
  "resource_estimate": { "manual": {...}, "human_in_loop": {...}, "auto_research": {...} },
  "target_venues": [...],
  "level": "top-tier",
  "key_references": [...],
  "description": "...",
  "project_name": "ttra_critic_guided",
  "source": "web_research",
  "change_type": "major",
  "reviewer_response": { one field per issue addressed }
}
```

Important guidelines:
- Be precise with numbers from the original idea (don't change verified statistics)
- The approach section should be very detailed (this is the core)
- The description should be a comprehensive 1-paragraph summary
- Keep all the good content from the original, just address the 5 issues
- The reviewer_response should have a field for each of the 5 issues plus the 2 minor points
- change_type MUST be "major"

Output ONLY the JSON, no markdown code fences, no commentary.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "d486c058-ed74-4cff-a86c-5d760a45ec16",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T18:43:32.769Z_

```json
{
  "parentUuid": "d486c058-ed74-4cff-a86c-5d760a45ec16",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
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
  "uuid": "9f238c7c-447f-451d-b91a-0849eb7ca867",
  "timestamp": "2026-05-27T18:43:32.769Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T18:43:32.770Z_

```json
{
  "parentUuid": "9f238c7c-447f-451d-b91a-0849eb7ca867",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4a6ee439-aadb-4857-8273-db1850470082",
  "timestamp": "2026-05-27T18:43:32.770Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T18:43:36.056Z_



I need to understand the existing research idea to produce a proper revision. Let me check if there are any existing files in the working directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a6ee439-aadb-4857-8273-db1850470082",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZq8QtbkbdjzJupcGZb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18845f48-7668-4aad-bbdd-769363fdd643",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y8kKnFzRqCZ9q7Mq5dsFxK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10907,
      "cache_read_input_tokens": 0,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10907
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 93,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 10907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10907,
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

### Tool call

_source line 5 · 2026-05-27T18:43:36.068Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018nVdW3TRRE5Q1XHDsMEpMm`</summary>

```json
{
  "command": "ls -la /home/ubuntu/idea_review/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18845f48-7668-4aad-bbdd-769363fdd643",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZq8QtbkbdjzJupcGZb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9fa36ef-aa03-4ab7-8557-0b357ae94213",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y8kKnFzRqCZ9q7Mq5dsFxK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10907,
      "cache_read_input_tokens": 0,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10907
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 93,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 10907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10907,
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

_source line 6 · 2026-05-27T18:43:36.259Z_

<details><summary>↩ Tool result · `toolu_018nVdW3TRRE5Q1XHDsMEpMm`</summary>

```text
total 104
drwxrwxr-x  7 ubuntu ubuntu  4096 May 27 15:16 .
drwxr-x--- 27 ubuntu ubuntu  4096 May 27 15:48 ..
drwxrwxr-x  5 ubuntu ubuntu  4096 May 16 01:47 .venv
drwxrwxr-x  2 ubuntu ubuntu  4096 May 20 03:40 __pycache__
-rw-rw-r--  1 ubuntu ubuntu 12674 May 19 01:32 batch_triage.py
-rw-rw-r--  1 ubuntu ubuntu  5398 May 27 15:16 conference.py
-rw-rw-r--  1 ubuntu ubuntu  1103 May 19 01:32 config.py
-rw-rw-r--  1 ubuntu ubuntu  2132 May 10 14:58 convergence.py
drwxrwxr-x 26 ubuntu ubuntu  4096 May 20 03:22 dispatch
-rw-rw-r--  1 ubuntu ubuntu  2779 May 12 04:27 io_utils.py
-rw-rw-r--  1 ubuntu ubuntu  7177 May 10 15:45 parsers.py
drwxrwxr-x  3 ubuntu ubuntu  4096 May 27 15:16 prompts
-rw-rw-r--  1 ubuntu ubuntu    17 May 10 14:58 requirements.txt
-rw-rw-r--  1 ubuntu ubuntu 23893 May 19 02:32 reviewer.py
-rw-rw-r--  1 ubuntu ubuntu   588 May 16 01:55 test_account.py
drwxrwxr-x  3 ubuntu ubuntu  4096 May 20 03:40 审idea的agent
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9fa36ef-aa03-4ab7-8557-0b357ae94213",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "205387a2-a001-4e4a-bcbb-49b8a4dfd1bc",
  "sourceToolAssistantUUID": "b9fa36ef-aa03-4ab7-8557-0b357ae94213",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T18:43:38.565Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VkARmMvt6WtcaL4tJwZWQS`</summary>

```json
{
  "command": "ls -la /home/ubuntu/idea_review/dispatch/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "205387a2-a001-4e4a-bcbb-49b8a4dfd1bc",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZqPGMpocv578GuNktw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d32007b2-59ec-44e4-8e94-beec28796b07",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXMAgupfjxB1fu3H7vYhuB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 591,
      "cache_read_input_tokens": 10907,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 591
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 10907,
          "cache_creation_input_tokens": 591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 591,
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

_source line 8 · 2026-05-27T18:43:38.630Z_

<details><summary>↩ Tool result · `toolu_01VkARmMvt6WtcaL4tJwZWQS`</summary>

```text
total 180
drwxrwxr-x 26 ubuntu ubuntu  4096 May 20 03:22 .
drwxrwxr-x  7 ubuntu ubuntu  4096 May 27 15:16 ..
drwxrwxr-x  2 ubuntu ubuntu  4096 May 19 02:38 ideas
drwxrwxr-x  2 ubuntu ubuntu  4096 May 17 11:06 ideas_0517
drwxrwxr-x  2 ubuntu ubuntu  4096 May 17 12:04 ideas_0517_s3
drwxrwxr-x  3 ubuntu ubuntu  4096 May 19 18:31 ideas_batch5_20260519_183057
drwxrwxr-x  3 ubuntu ubuntu  4096 May 19 20:45 ideas_batch5_20260519_204518
drwxrwxr-x  4 ubuntu ubuntu  4096 May 20 02:55 ideas_batch6_20260520_025525
drwxrwxr-x  4 ubuntu ubuntu  4096 May 20 03:22 ideas_batch7_20260520_032225
drwxrwxr-x  5 ubuntu ubuntu  4096 May 16 01:48 ideas_batch_20260516_014736
drwxrwxr-x  5 ubuntu ubuntu  4096 May 16 10:53 ideas_batch_20260516_pass25
drwxrwxr-x  5 ubuntu ubuntu  4096 May 16 10:05 ideas_batch_20260516_pm
drwxrwxr-x  2 ubuntu ubuntu  4096 May 17 13:52 ideas_rerun
drwxrwxr-x  2 ubuntu ubuntu  4096 May 17 12:18 ideas_stage23
drwxrwxr-x  4 ubuntu ubuntu  4096 May 19 04:20 results
drwxrwxr-x  6 ubuntu ubuntu  4096 May 17 11:52 results_0517
drwxrwxr-x  2 ubuntu ubuntu  4096 May 17 12:17 results_0517_s3
drwxrwxr-x  3 ubuntu ubuntu  4096 May 19 18:31 results_batch5_20260519_183057
drwxrwxr-x  3 ubuntu ubuntu  4096 May 19 20:45 results_batch5_20260519_204518
drwxrwxr-x  4 ubuntu ubuntu  4096 May 20 02:55 results_batch6_20260520_025525
drwxrwxr-x  4 ubuntu ubuntu  4096 May 20 03:22 results_batch7_20260520_032225
drwxrwxr-x  5 ubuntu ubuntu  4096 May 16 01:48 results_batch_20260516_014736
drwxrwxr-x  5 ubuntu ubuntu  4096 May 16 12:00 results_batch_20260516_pass25
drwxrwxr-x  5 ubuntu ubuntu  4096 May 16 10:05 results_batch_20260516_pm
drwxrwxr-x  4 ubuntu ubuntu  4096 May 17 15:44 results_rerun
drwxrwxr-x  4 ubuntu ubuntu  4096 May 17 13:30 results_stage23
-rw-rw-r--  1 ubuntu ubuntu 16568 May 16 11:59 run_full_pipeline.py
-rwxrwxr-x  1 ubuntu ubuntu  2576 May 19 05:30 run_multi_account.sh
-rw-rw-r--  1 ubuntu ubuntu  1212 May 17 14:11 run_rerun.log
-rw-rw-r--  1 ubuntu ubuntu  4798 May 17 15:44 run_rerun_v3.log
-rw-rw-r--  1 ubuntu ubuntu  4915 May 19 04:20 run_s2.log
-rw-rw-r--  1 ubuntu ubuntu  4143 May 17 11:52 run_s2_0517.log
-rw-rw-r--  1 ubuntu ubuntu  1551 May 17 12:17 run_s2_0517_s3.log
-rw-rw-r--  1 ubuntu ubuntu  4860 May 17 13:30 run_s2_stage23.log
-rw-rw-r--  1 ubuntu ubuntu 10789 May 17 13:51 run_stage23_only.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d32007b2-59ec-44e4-8e94-beec28796b07",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "e778973e-f845-4291-8ae4-ef2931338a8d",
  "sourceToolAssistantUUID": "d32007b2-59ec-44e4-8e94-beec28796b07",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T18:43:41.325Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UkqujWXeJBgJxJJ9A8NhNj`</summary>

```json
{
  "command": "find /home/ubuntu/idea_review/dispatch -name \"*ttra*\" -o -name \"*critic*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e778973e-f845-4291-8ae4-ef2931338a8d",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZqZU2D5BPX3b4MoSUv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c65e9b3b-5d5d-4d93-8c37-75d704f044f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EjxJe7ok7gpCNoUGdwznA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1286,
      "cache_read_input_tokens": 11498,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1286
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 11498,
          "cache_creation_input_tokens": 1286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1286,
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

_source line 10 · 2026-05-27T18:43:41.402Z_

<details><summary>↩ Tool result · `toolu_01UkqujWXeJBgJxJJ9A8NhNj`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c65e9b3b-5d5d-4d93-8c37-75d704f044f0",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "3cf13cdd-622b-48b5-847f-c889aad1b7d0",
  "sourceToolAssistantUUID": "c65e9b3b-5d5d-4d93-8c37-75d704f044f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T18:43:43.705Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0163FiDaYfz5eGWQaZLRrb2F`</summary>

```json
{
  "pattern": "**/*ttra*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cf13cdd-622b-48b5-847f-c889aad1b7d0",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZqmQct1knR3WgDFGHA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbbee85d-ee19-4dc3-a8e8-9af9557d8969",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvMVAShTvmBxzzPxZmxTDb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 101,
      "cache_read_input_tokens": 12784,
      "output_tokens": 56,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 101
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 56,
          "cache_read_input_tokens": 12784,
          "cache_creation_input_tokens": 101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 101,
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

_source line 12 · 2026-05-27T18:43:43.737Z_

<details><summary>↩ Tool result · `toolu_0163FiDaYfz5eGWQaZLRrb2F`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbbee85d-ee19-4dc3-a8e8-9af9557d8969",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "6a1b8370-9915-4ec4-8675-9bde6ab6051f",
  "sourceToolAssistantUUID": "fbbee85d-ee19-4dc3-a8e8-9af9557d8969",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-27T18:43:46.155Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0147mnB9oUjxb9uZMXy1jG5w`</summary>

```json
{
  "pattern": "ttra_critic_guided",
  "path": "/home/ubuntu/idea_review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a1b8370-9915-4ec4-8675-9bde6ab6051f",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZqwTN2xRVdEF7uXNDS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "453b32ce-d78d-464d-829a-b6b0400b3b6c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSQMsduxXoupoBL76VSqtQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 71,
      "cache_read_input_tokens": 12885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 71,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 14 · 2026-05-27T18:43:47.150Z_

<details><summary>↩ Tool result · `toolu_0147mnB9oUjxb9uZMXy1jG5w`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "453b32ce-d78d-464d-829a-b6b0400b3b6c",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "e6bb101c-0f0c-4071-ae0f-f834cca5cf61",
  "sourceToolAssistantUUID": "453b32ce-d78d-464d-829a-b6b0400b3b6c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T18:43:51.071Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Crvkw7YKXE7GuYa3rcXVz7`</summary>

```json
{
  "pattern": "TTRA",
  "path": "/home/ubuntu/idea_review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6bb101c-0f0c-4071-ae0f-f834cca5cf61",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZrBqYvDC2rScM8GwHq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a811ade3-de61-474b-97ca-256e60047059",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XDXjgiiaT3kdHs9TcXmn9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 96,
      "cache_read_input_tokens": 12956,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 96
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 12956,
          "cache_creation_input_tokens": 96,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 96,
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

_source line 16 · 2026-05-27T18:43:51.119Z_

<details><summary>↩ Tool result · `toolu_01Crvkw7YKXE7GuYa3rcXVz7`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a811ade3-de61-474b-97ca-256e60047059",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "35b88625-e37e-4abe-bf4b-95f1599c4d86",
  "sourceToolAssistantUUID": "a811ade3-de61-474b-97ca-256e60047059",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-27T18:43:54.365Z_

Let me look at the existing idea files and reviewer structure to understand the JSON format used.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35b88625-e37e-4abe-bf4b-95f1599c4d86",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZrUzfmpNUFLGpcpGnL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74cf7388-e1ad-47d3-8519-e2cc12267a7a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmZX8VrXQuugURAqG22kAF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 93,
      "cache_read_input_tokens": 13052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 93,
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

_source line 18 · 2026-05-27T18:43:54.839Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0129XCNdE3LA1jxcTtpdfhwp`</summary>

```json
{
  "command": "ls /home/ubuntu/idea_review/dispatch/ideas/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74cf7388-e1ad-47d3-8519-e2cc12267a7a",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZrUzfmpNUFLGpcpGnL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1064e05f-77d7-4674-8ca2-1bf18dacc211",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmZX8VrXQuugURAqG22kAF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 93,
      "cache_read_input_tokens": 13052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 93,
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

_source line 19 · 2026-05-27T18:43:54.892Z_

<details><summary>↩ Tool result · `toolu_0129XCNdE3LA1jxcTtpdfhwp`</summary>

```text
corl_003_prod_s1.json
corl_004_prod_s1.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1064e05f-77d7-4674-8ca2-1bf18dacc211",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "d35dd683-f51f-4757-bc2e-0394eca7ada4",
  "sourceToolAssistantUUID": "1064e05f-77d7-4674-8ca2-1bf18dacc211",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-27T18:43:55.129Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0144AKELy1BEWjCKh3WgTqMC`</summary>

```json
{
  "command": "ls /home/ubuntu/idea_review/dispatch/results/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d35dd683-f51f-4757-bc2e-0394eca7ada4",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZrUzfmpNUFLGpcpGnL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9fbbfa4-8289-4fda-8961-e06c050c007a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmZX8VrXQuugURAqG22kAF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 93,
      "cache_read_input_tokens": 13052,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 93
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 13052,
          "cache_creation_input_tokens": 93,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 93,
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

_source line 21 · 2026-05-27T18:43:55.183Z_

<details><summary>↩ Tool result · `toolu_0144AKELy1BEWjCKh3WgTqMC`</summary>

```text
_manifest_20260519_023911.json
result_corl_003_prod_s1.json
result_corl_004_prod_s1.json
trace_corl_003_prod_s1
trace_corl_004_prod_s1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9fbbfa4-8289-4fda-8961-e06c050c007a",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "70332f36-8564-4f7b-86f4-3e28ac3f052e",
  "sourceToolAssistantUUID": "a9fbbfa4-8289-4fda-8961-e06c050c007a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-27T18:43:58.390Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KiBPJf7em2QCB1UpLhqeWj`</summary>

```json
{
  "file_path": "/home/ubuntu/idea_review/dispatch/ideas/corl_003_prod_s1.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70332f36-8564-4f7b-86f4-3e28ac3f052e",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZrnJEBqBPguYGB5wW1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e69107c-ff19-49eb-9a51-ca5b594b9116",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pkz1xqnRiuCATfcdhCXEHT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 285,
      "cache_read_input_tokens": 13145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 285,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 23 · 2026-05-27T18:43:58.492Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R8VhJPMbUKNE2ezrC1Rdxn`</summary>

```json
{
  "file_path": "/home/ubuntu/idea_review/dispatch/results/result_corl_003_prod_s1.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e69107c-ff19-49eb-9a51-ca5b594b9116",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZrnJEBqBPguYGB5wW1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83139e0a-6135-452c-9d00-912952987619",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pkz1xqnRiuCATfcdhCXEHT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 285,
      "cache_read_input_tokens": 13145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 285,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 24 · 2026-05-27T18:43:58.746Z_

<details><summary>↩ Tool result · `toolu_01KiBPJf7em2QCB1UpLhqeWj`</summary>

```text
1	{
2	  "id": "idea_030",
3	  "source_backend": "prod_s1",
4	  "key": "corl_003_prod_s1",
5	  "title": "LACVLA: Enforcing Language-Affordance Grounding via Consistency Objectives for Zero-Shot Cross-Category VLA Manipulation",
6	  "content": "# LACVLA: Enforcing Language-Affordance Grounding via Consistency Objectives for Zero-Shot Cross-Category VLA Manipulation\n\n## Core Problem\nHow can end-to-end VLA models achieve zero-shot manipulation transfer to entirely unseen object categories — objects with no visual precedent in training — given that (1) cross-category transfer fundamentally requires spatial grounding from language (the only cue that specifies WHERE to interact on a novel object), yet (2) current VLAs largely ignore language instructions (LIBERO-Plus, CVPR 2026; LangGap, Mar 2026), a failure mode that is survivable in-distribution but catastrophic when visual priors are absent?\n\n## Opportunity\nCross-category zero-shot manipulation — generalizing to objects never seen during training — remains an open challenge: even strong VLAs like π₀.₅ and GR00T-N1.6 fail on affordance generalization across object variants (BusyBox, Feb 2026), and A0 (ICCV 2025) achieves cross-category transfer via 1M contact points but without language conditioning. The fundamental bottleneck is that novel objects lack visual priors, so language must serve as the primary guide for spatial grounding — yet diagnostic work shows VLAs systematically ignore language. LIBERO-Plus (CVPR 2026, arXiv 2510.13626) reveals VLAs exhibit positional bias rather than semantic understanding; LangGap (arXiv 2603.00592, Mar 2026) quantifies this: VLAs with 95%+ standard success largely ignore language, and targeted data augmentation hits a ceiling (0%→28% multi-task). LIBERO-Para (Mar 2026) shows 22–52pp drops under paraphrased instructions, with 80–96% of failures from planning-level trajectory divergence. Shin (Mar 2026) achieves only +1.71pp via LLM-generated paraphrase augmentation, consistent with LangGap's ceiling finding. Recent approaches address aspects of this problem but not the full combination: spatial grounding methods (ST4VLA, ICLR 2026; SpatialVLA, RSS 2025) improve performance broadly but do not structurally guarantee language conditioning — a model can learn spatial shortcuts within training categories. GuidedVLA (RSS 2026) supervises individual attention heads with auxiliary signals but uses 3 predefined factor types without cross-category transfer focus. ProGAL-VLA (Apr 2026) imposes a verified grounding bottleneck via 3D entity-centric graphs and symbolic sub-goals, improving robustness (30.3%→71.5% on LIBERO-Plus perturbations) but requires explicit entity recognition rather than open-vocabulary affordance transfer. PPCL (EACL 2024) showed consistency regularization beats augmentation with 10× fewer samples in NLP. The opportunity: an affordance-gated architectural bottleneck with self-supervised consistency objectives that structurally forces language to condition spatial grounding — making language a mandatory pathway for action generation — enabling genuine cross-category zero-shot transfer without 3D sensors, expensive cross-category annotations, or modular decomposition.\n\n## Landscape\nThe VLA-affordance landscape has six relevant lineages, none of which combines architectural enforcement of language conditioning, self-supervised consistency on spatial affordance representations, and cross-category zero-shot transfer as the primary target. (1) Spatially-guided VLAs: ST4VLA (ICLR 2026, arXiv 2602.10109) introduces dual-system spatial grounding (Qwen2.5-VL planner + DiT/DINOv2 action expert), achieving 95.9% LIBERO average (98.0% Spatial, 99.0% Object, 93.8% Goal, 92.6% Long), 72%/61% attribute/spatial paraphrase robustness (vs π₀: 32%/31%), and 62% on new object instances (vs π₀: 32%, GR00T N1: 46%). This is LACVLA's strongest baseline — the null hypothesis is 'does explicit affordance consistency add value beyond spatial grounding alone?' InternVLA-M1 (arXiv 2510.13778) extends this with affordance recognition and chain-of-thought reasoning. SpatialVLA (RSS 2025, arXiv 2501.15830) introduces Ego3D Position Encoding and Adaptive Action Grids. Spatial Forcing (ICLR 2026, arXiv 2510.12276) aligns VLM features with 3D foundation models without 3D input at inference. All improve spatial understanding but none guarantees language conditions the spatial representation. (2) Supervised intermediate representation guidance: GuidedVLA (RSS 2026, arXiv 2605.12369) treats the action decoder as an assembly of functional components, supervising individual attention heads with auxiliary signals for three predefined factor types: object grounding (attention mass loss over detected object masks), spatial geometry (depth encoder feature constraint), and temporal skill logic (KL-divergence skill classification). Built on π₀, achieves 75.4% on LIBERO-Plus (vs 68.2% baseline), 90.63% on RoboTwin 2.0. Architectural parallel to LACVLA: both use explicit supervision on intermediate representations to improve VLA grounding. Key differences: GuidedVLA uses 3 predefined factor types (not open-vocabulary), does not use consistency objectives on heatmaps, does not produce affordance heatmaps, and does not target cross-category zero-shot transfer. LACVLA's affordance readout with stop-gradient bottleneck produces open-vocabulary spatial heatmaps enforced via self-supervised consistency — a fundamentally different supervision signal (consistency between paraphrases vs. factor-specific auxiliary losses). (3) Language grounding diagnostics and solutions: LIBERO-Plus (CVPR 2026, arXiv 2510.13626) reveals VLAs are insensitive to language and exhibit positional bias. LangGap (arXiv 2603.00592, Mar 2026) confirms VLAs ignore language and shows augmentation's ceiling (28% multi-task). LIBERO-Para (arXiv 2603.28301, Mar 2026) quantifies paraphrase fragility (22–52pp drops). Shin (arXiv 2603.16044, Mar 2026) achieves only +1.71pp via augmentation. ProGAL-VLA (arXiv 2604.09824, Apr 2026) constructs a 3D entity-centric graph with symbolic sub-goals and Grounding Alignment Contrastive loss, imposing a verified grounding bottleneck — achieves 71.5% robustness on LIBERO-Plus (up from 30.3%), but requires explicit entity recognition and 3D scene graphs, not applicable to open-vocabulary affordance transfer across unseen categories. Stable Language Guidance (ACL 2026, arXiv 2601.04052) addresses modality collapse at inference via residual steering — complementary to LACVLA's training-time approach. Attention recalibration (arXiv 2603.06001) provides train-free inference-time fix for attention sink dynamics but does not change learned representations. (4) Modular affordance-then-action pipelines: RT-Affordance (arXiv 2411.02704), UAD (ICRA 2025), RAM (CoRL 2024), RAAP (arXiv 2603.29419, Mar 2026), AffordDP (CVPR 2025), RoboMAP (arXiv 2510.10912), A0 (ICCV 2025, arXiv 2504.12636), and GLOVER++ (CoRL 2025, arXiv 2505.11865) all produce affordance representations but feed them to separate downstream planners/policies, sacrificing end-to-end optimization. A0 achieves zero-shot cross-category transfer via 1M contact points but without language conditioning. (5) Architectural bottleneck enforcement: DIAL (arXiv 2603.29844, Mar 2026) enforces a latent intent bottleneck via inverse dynamics — the action head MUST use predicted latent intent. This inspires LACVLA's affordance-gated bottleneck (stop-gradient on VLM features, affordance map as spatial attention gate). (6) Cross-category zero-shot benchmarks: AGNOSTOS/X-ICM (arXiv 2505.15660) provides 23 unseen manipulation tasks. VLA² (arXiv 2510.14902) uses agentic retrieval for unseen concepts. BusyBox (arXiv 2602.05441, Feb 2026) is a physical benchmark where 6 reconfigurable modules test affordance generalization — even π₀.₅ and GR00T-N1.6 fail on shuffled configurations despite identical affordances, demonstrating that affordance generalization remains unsolved. Gap: No existing work combines (a) architectural enforcement that language must condition spatial features via stop-gradient bottleneck, (b) self-supervised consistency objectives on affordance heatmaps (not raw actions, not predefined factor types), and (c) cross-category zero-shot transfer as the primary evaluation target.\n\n## Description\nWe address cross-category zero-shot manipulation transfer — generalizing to objects with no visual precedent in training — where language is the only available guide for spatial grounding on novel objects. We show that the well-documented language-ignoring failure in VLAs (LIBERO-Plus, CVPR 2026; LangGap, Mar 2026) is particularly catastrophic in this setting: visual priors and layout memorization cannot compensate when the object itself is unseen. Existing approaches either improve spatial understanding without guaranteeing language conditions the representation (ST4VLA, SpatialVLA, Spatial Forcing), supervise predefined intermediate factor types without cross-category affordance transfer (GuidedVLA, RSS 2026), impose grounding bottlenecks requiring explicit entity recognition (ProGAL-VLA), or produce affordance representations in modular pipelines sacrificing end-to-end optimization (A0, GLOVER++, RT-Affordance). LACVLA proposes an affordance-gated architectural bottleneck, inspired by DIAL's latent intent bottleneck, that structurally forces all task-relevant spatial information through a language-conditioned affordance map: VLM intermediate features pass through stop-gradient before the action head, which receives affordance_heatmap ⊙ sg(visual_features) + proprioceptive_state. The affordance map (produced via cross-attention between VLM features and language tokens) acts as a spatial attention gate — a uniform (language-ignoring) map yields unselective features and degraded performance. Self-supervised consistency objectives enforce language-affordance grounding: IPAC ensures semantically equivalent instructions produce identical affordance maps (transferring PPCL's consistency > augmentation principle from NLP to spatial heatmaps), while IDA ensures semantically different instructions produce divergent maps (preventing collapse). Affordance readout is pre-trained via HOVA-500K with a fully specified self-supervised fallback using robot-data pseudo-affordance labels from gripper contact positions — eliminating HOVA-500K as a single point of failure and producing an ablation that determines whether HOVA-500K pre-training is necessary. A streamlined 6-variant ablation suite (reduced from 8 to fit ≤200 H100-hour budget) addresses all key questions: bottleneck necessity (#2, merged sub-conditions: no bottleneck vs. bottleneck-only), end-to-end vs. modular (#3), augmentation ceiling (#4), affordance maps vs. raw actions as consistency target (#5 — the paper's critical test: if affordance-level consistency outperforms action-level, it validates that isolating WHERE from HOW is essential), and value beyond spatial grounding (#6). Evaluation is anchored on cross-category zero-shot transfer as the PRIMARY metric: held-out object categories, HOVA-500K cross-category splits, AGNOSTOS benchmark, BusyBox affordance generalization (supplementary physical evaluation), and real-world tests on 5+ unseen categories. SECONDARY metrics cover paraphrase robustness (LIBERO-Para, LangGap), affordance quality (Affogato), and in-distribution performance (standard LIBERO). Primary target: AAAI 2027 (abstract Jul 21, 64 days).\n\n## Approach\nWe propose LACVLA, an end-to-end VLA that structurally forces language to condition spatial affordance grounding through an affordance-gated bottleneck and self-supervised consistency objectives, enabling zero-shot cross-category manipulation transfer.\n\nArchitecture — Affordance-Gated Bottleneck (inspired by DIAL's latent intent bottleneck): Built on a 4B–7B VLM backbone (Qwen2-VL-4B via StarVLA or PaliGemma2) with LoRA fine-tuning. The architecture has three components:\n(a) Affordance Readout: A cross-attention layer where language instruction tokens attend over intermediate VLM visual features (layer ~16 of 32 for Qwen2-VL), producing a dense affordance heatmap over the image. This encodes WHERE to interact, conditioned on the instruction. Architecture: single cross-attention + LayerNorm + linear projection to H×W heatmap, <5M parameters.\n(b) Stop-Gradient Bottleneck: VLM intermediate visual features are passed through a stop-gradient before reaching the action head. The action head receives: affordance_heatmap ⊙ sg(VLM_visual_features) + proprioceptive_state. The affordance map acts as a spatial attention gate — if the model produces a uniform (language-ignoring) affordance map, the action head receives unselective visual features with no spatial focus, degrading performance. Unlike GuidedVLA's factor-specific head supervision (predefined types, direct auxiliary losses), LACVLA's stop-gradient ensures no task-semantic gradient flows through the non-affordance pathway — the action head CANNOT learn to extract task information from raw VLM features, and the affordance readout is open-vocabulary rather than restricted to predefined factor categories.\n(c) Flow-Matching Action Head: A lightweight DiT (Diffusion Transformer) that generates trajectory chunks conditioned on the affordance-gated visual features + proprioceptive state, following the flow-matching formulation.\n\nTraining Objectives — Three jointly optimized losses with phased schedule:\n(1) Instruction-Paraphrase Affordance Consistency (IPAC): Given the same visual scene and K LLM-generated paraphrases of the same task instruction (e.g., 'grab the mug handle' vs. 'grasp the cup by its handle'), the affordance maps must be consistent (KL divergence penalty on spatial heatmaps). This transfers the consistency regularization principle from PPCL (EACL 2024) — which showed consistency > augmentation with 10× less data in NLP — to spatial affordance heatmaps. Unlike Shin (2026), who uses paraphrases purely as data augmentation (+1.71pp), IPAC uses them as a regularization signal constraining affordance geometry. Paraphrases generated offline by LLM — free, unlimited supervision.\n(2) Instruction-Discriminative Affordance (IDA): Given the same visual scene and two semantically different instructions (e.g., 'pick up the mug by its handle' vs. 'pour from the mug'), the affordance maps must diverge (margin-based divergence loss). This prevents degenerate consistency collapse where the model produces instruction-invariant heatmaps to trivially satisfy IPAC. Different-instruction pairs come naturally from multi-task robot datasets.\n(3) Action-Grounded Affordance (AGA): Standard flow-matching loss for trajectory prediction through the affordance-gated bottleneck. This grounds the affordance map in manipulation-relevant contact regions via end-to-end backpropagation through the gating mechanism.\n\nPhased Training Schedule:\nPhase 1 — Affordance Readout Pre-training: PRIMARY path: pre-train on HOVA-500K with cross-attention readout predicting contact-point Gaussian heatmaps (σ proportional to object scale) conditioned on action-label text prompts from 675 action categories. Viewpoint augmentation (random crop, perspective warp, ego→third-person style augmentation) addresses the ego-centric domain gap. FALLBACK path (if domain gap diagnostic fails): self-supervised affordance readout initialization using robot data alone — extract pseudo-affordance Gaussian heatmaps from gripper position at grasp/contact time in robot trajectory data (well-established technique: text-driven affordance learning with pseudo-labels, trajectory-based contact recovery). This produces lower-coverage but higher-fidelity affordance supervision for the robot observation domain. Diagnostic checkpoint: evaluate pre-trained affordance readout on a held-out set of robot observation images; if domain gap degrades affordance quality below threshold (mean IoU < 0.3 between predicted heatmap peak and gripper contact region), switch to fallback path. Ablation of HOVA-500K vs. self-supervised initialization determines whether HOVA-500K is necessary, de-risking the paper from the HOVA-500K dependency.\nPhase 2 — End-to-end VLA training (steps 0–N): Fine-tune full model (VLM via LoRA + pre-trained affordance readout + flow-matching action head) on robot data. Sub-phases: (2a) AGA only for 10% of training — establish action grounding baseline. (2b) Add IPAC at 10% — enforce consistency while action loss stabilizes gradients. (2c) Ramp IDA from 0 to full weight over 15% of training via linear warmup, monitored by: (i) affordance entropy H(A) — if H(A) < 0.3 × H_max, increase IDA weight by 50%; (ii) instruction-discriminability D = mean pairwise KL between different-instruction maps on validation set — if D < 0.5, halt IPAC and boost IDA. GradNorm-style gradient normalization across the three losses balances training rates automatically.\n\nWhy Affordance Maps (Not Raw Actions) for Consistency: Affordance maps capture WHERE to interact — the geometric invariant across paraphrases and across categories sharing functional parts. Action distributions conflate WHERE + HOW + WHEN (trajectory shape, timing, force), making consistency regularization noisier. For cross-category transfer, WHERE is what transfers (handle locations generalize across mugs/cups/pitchers), while HOW adapts to object-specific geometry. This argument is validated empirically by ablation #5.\n\nCross-Object Functional Consistency via HOVA-500K: Group HOVA-500K images by shared action labels (675 categories) and apply soft KL penalty between affordance maps of same-action images from different object categories. This provides weak supervision for cross-category affordance consistency without requiring part-level functional equivalence annotations.\n\nData Pipeline: Open X-Embodiment and DROID for robot trajectories, HOVA-500K for affordance pre-training and cross-object grouping (with self-supervised robot-data fallback), LLM-generated instruction paraphrases (Qwen3 or GPT-4) for IPAC pairs.\n\nAblation Design (6 variants, streamlined to fit compute budget while retaining all core tests):\n(1) Full LACVLA — affordance-gated bottleneck + IPAC + IDA + AGA\n(2) Bottleneck analysis (merged): (a) No affordance bottleneck — direct VLA without affordance readout; (b) Bottleneck + AGA only, no consistency losses — tests whether architectural bottleneck alone suffices. Both sub-conditions use identical training data and hyperparameters; affordance map quality (entropy, instruction-discriminability) tracked for sub-condition (b) to diagnose whether the bottleneck induces meaningful affordance structure without consistency enforcement.\n(3) Modular composition — frozen GLOVER++ affordance → separate policy (tests end-to-end vs. modular)\n(4) Shin-style augmentation — paraphrases added as training data, no consistency loss (tests data augmentation ceiling, paralleling PPCL's NLP finding)\n(5) IPAC on raw actions — KL divergence between action distributions under paraphrased instructions, no affordance readout (CRITICAL: tests whether isolating WHERE via affordance maps outperforms consistency on conflated action distributions — if affordance maps win, that's the paper's key finding; if raw actions work comparably, the affordance readout is unnecessary overhead)\n(6) ST4VLA-style spatial grounding + IPAC on features — spatial grounding pre-training + consistency on intermediate VLM features without affordance readout (tests whether explicit affordance structure adds value beyond strong spatial pre-training + consistency)\n\nEvaluation Protocol — Primary (Cross-Category Zero-Shot Transfer):\n(a) Held-out object category experiments: partition LIBERO/DROID object categories into train/test sets, test on entirely unseen categories with both standard and paraphrased instructions\n(b) HOVA-500K cross-category transfer tests: train on K action categories with one set of objects (e.g., 'pour from pitcher'), test on same actions with different object categories (e.g., 'pour from kettle') — constructed from HOVA-500K's 675 shared action labels\n(c) AGNOSTOS benchmark (arXiv 2505.15660) for cross-task zero-shot evaluation (23 unseen tasks)\n(d) BusyBox (arXiv 2602.05441) supplementary evaluation: if physical hardware is available, test LACVLA on shuffled BusyBox configurations where even π₀.₅ and GR00T-N1.6 fail — directly measures affordance generalization across visual variants with identical functional affordances\n(e) Real-world evaluation on 5+ unseen object categories across at least 3 manipulation primitives (grasp, pour, push)\n\nEvaluation Protocol — Secondary:\n(f) LIBERO-Para benchmark with PRIDE metric for paraphrase robustness (direct comparison with ST4VLA's 72%/61%)\n(g) LangGap protocol for language grounding quality (targeting improvement over the 28% multi-task ceiling)\n(h) Affogato for affordance quality assessment\n(i) Standard LIBERO (Spatial, Object, Goal, Long) for in-distribution comparison with ST4VLA (95.9% avg)\n\nCoRL 2026 Infeasibility Statement: CoRL 2026 (abstract May 26 — 8 days from today, May 18) is infeasible given implementation scope. Primary target: AAAI 2027 (abstract Jul 21, full paper Jul 28 — 64 days to abstract). Backup: WACV 2027 Round 2 (paper Aug 27 — 101 days).\n\n## Resource Estimate\n{'auto_research': {'claude_api_cost': '$500-1,200 (estimated 5,000-12,000 agent turns)', 'estimated_gpu_cost': '$675-975 (at ~$1.50/h A100 80GB)', 'gpu_hours': '~450-650h A100 80GB, equivalent to ~320-465h H100 at conservative 1.4x ratio (agent explores 14-20 training configurations for phased schedule tuning, all 6 ablation variants × 2-3 seeds, both HOVA-500K and self-supervised affordance pre-training paths, full benchmark sweeps)', 'gpu_utilization': '~85-95% — agent immediately queues next experiment upon completion; parallel ablation runs on multi-GPU setup', 'risk_note': 'Automated phased training managed by entropy/discriminability monitoring. If affordance-gated bottleneck causes consistent performance collapse across configurations, agent escalates to soft-gating variants. GradNorm balancing reduces sensitivity to manual loss weight tuning. Self-supervised fallback eliminates HOVA-500K as a single point of failure.', 'speed_bottleneck': 'Each LoRA training run on 4B backbone takes ~8-12h on 4 A100s. HOVA-500K preprocessing and viewpoint-augmented Gaussian heatmap generation ~25h one-time. Cross-category evaluation setup ~6h one-time.', 'team': '0 researchers after initial setup (~6-8 hours: dataset access, paraphrase generation config, HOVA-500K + self-supervised preprocessing, AGNOSTOS/LIBERO-Para/LangGap environment setup, cross-category held-out split definition)', 'timeline': '3-4 weeks with 4+ A100 GPUs available concurrently (bottleneck: affordance pre-training → domain gap diagnostic → phased training search → cross-category evaluation)'}, 'human_in_loop': {'claude_api_cost': '$200-500 (estimated 2,000-5,000 agent turns)', 'estimated_gpu_cost': '$340-465 (at ~$1.50/h A100 80GB)', 'gpu_hours': '~225-310h A100 80GB, equivalent to ~160-220h H100 at conservative 1.4x ratio (agent runs 8-10 training configurations systematically: all 6 ablations + 2-4 additional hyperparameter variants, HOVA-500K pre-training or self-supervised fallback, with wasted runs caught early by human)', 'gpu_utilization': '~40-55% — agent queues experiments but pauses at key gates: (1) affordance readout domain gap diagnostic (HOVA-500K vs. self-supervised), (2) affordance map quality inspection after bottleneck warmup, (3) cross-category held-out split design approval', 'risk_note': 'Primary risk: HOVA-500K affordance readout domain gap — fully mitigated by self-supervised fallback using robot-data pseudo-affordance labels from gripper contact positions, with ablation comparing both paths. Secondary risk: affordance-gated bottleneck may be too restrictive — mitigated by ablation #2b (bottleneck without consistency) to isolate the effect. ST4VLA comparison (ablation #6) determines value beyond spatial grounding.', 'team': '1 researcher, ~1.5h/day review', 'timeline': '6-8 weeks (agent handles paraphrase generation, HOVA-500K or self-supervised preprocessing, hyperparameter sweeps, AGNOSTOS/LIBERO-Para/LangGap evaluation scripts; human approves domain gap bridging strategy, inspects affordance maps, validates cross-category split design)'}, 'manual': {'estimated_gpu_cost': '$265-370 (at ~$1.50/h A100 80GB)', 'gpu_hours': '~175-245h A100 80GB, equivalent to ~125-175h H100 at conservative 1.4x ratio (HOVA-500K affordance readout pre-training ~20h or self-supervised fallback ~8h, 1 full LACVLA training run ~35-45h, 5 ablation experiments at ~12-18h each = 60-90h, cross-category evaluation sweeps ~25h, AGNOSTOS benchmark runs ~15h, BusyBox evaluation if available ~5h). 6 ablations (down from 8) are the key cost savings: merging bottleneck analysis into one experiment with sub-conditions and dropping phased-training ablation saves ~30-40h A100.', 'gpu_utilization': '~15-25% effective utilization — idle during result analysis, loss weight iteration, domain gap diagnostics between phases', 'team': '2 researchers (1 lead on affordance-gated architecture + consistency objectives + bottleneck enforcement, 1 on data pipeline/HOVA-500K integration/cross-category evaluation/AGNOSTOS setup)', 'timeline': '8-10 weeks (1-2 weeks data pipeline + affordance readout pre-training (HOVA-500K or self-supervised fallback) + domain gap diagnostics; 4-5 weeks iterative experimentation including all 6 ablations; 2-3 weeks cross-category evaluation + paper writing)'}}\n\n## Key References\n- ST4VLA: Spatially Guided Training for Vision-Language-Action Models (ICLR 2026, arXiv 2602.10109) — strongest baseline: 95.9% LIBERO avg, 72%/61% paraphrase robustness, 62% unseen objects via spatial grounding alone\n- LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626) — diagnostic revealing VLAs ignore language instructions, exhibit positional bias\n- LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models (arXiv 2603.00592, Mar 2026) — quantifies language gap: augmentation reaches 90% single-task but only 28% multi-task\n- GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization (RSS 2026, arXiv 2605.12369, May 2026) — supervises 3 predefined attention head types (object/spatial/temporal) on π₀; 75.4% LIBERO-Plus, 90.63% RoboTwin; architectural parallel (supervised intermediate representations) but no consistency objectives, no affordance heatmaps, no cross-category transfer\n- BusyBox: Benchmarking Affordance Generalization (arXiv 2602.05441, Feb 2026, Microsoft) — physical benchmark with 6 reconfigurable modules; even π₀.₅ and GR00T-N1.6 fail on shuffled configurations; directly tests affordance generalization across visual variants\n- ProGAL-VLA: Grounded Alignment through Prospective Reasoning in VLA Models (arXiv 2604.09824, Apr 2026) — verified grounding bottleneck via 3D entity-centric graph + GAC loss; 71.5% LIBERO-Plus robustness; requires explicit entity recognition, not applicable to open-vocabulary affordance transfer\n- DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA (arXiv 2603.29844, Mar 2026) — latent intent bottleneck via inverse dynamics, inspiration for affordance-gated architecture\n- InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy (arXiv 2510.13778) — spatially guided VLA with affordance recognition in pre-training\n- SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models (RSS 2025, arXiv 2501.15830) — spatial-aware action tokenization\n- Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model (ICLR 2026, arXiv 2510.12276) — implicit spatial alignment without 3D input\n- AGNOSTOS / X-ICM: Exploring the Limits of Vision-Language-Action Manipulations in Cross-task Generalization (arXiv 2505.15660) — cross-task zero-shot benchmark with 23 unseen tasks\n- LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models (arXiv 2603.28301, Mar 2026) — paraphrase robustness evaluation with PRIDE metric\n- Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation (Shin, arXiv 2603.16044, Mar 2026) — direct augmentation baseline, +1.71pp only\n- Stable Language Guidance / Residual Semantic Steering for VLAs (ACL 2026, arXiv 2601.04052) — inference-time modality collapse mitigation, complementary to LACVLA's training-time approach\n- Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration (arXiv 2603.06001, Mar 2026) — diagnoses attention sink dynamics as cause of linguistic blindness; train-free inference fix complementary to LACVLA\n- Prompt Perturbation Consistency Learning for Robust Language Models (PPCL, EACL 2024, arXiv 2402.15833) — consistency regularization > augmentation with 10× fewer samples in NLP\n- Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs (arXiv 2510.14242, Oct 2025) — extends PPCL to LLMs\n- OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024) — base VLA architecture\n- StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing (arXiv 2604.05014, Apr 2026) — implementation framework\n- GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation (CoRL 2025, arXiv 2505.11865) — provides HOVA-500K dataset, modular baseline\n- PokéVLA: Empowering Pocket-Sized VLA Model with Comprehensive World Knowledge Guidance (arXiv 2604.20834, Apr 2026) — validates HOVA-500K ego→VLA transfer for backbone pre-training\n- RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (arXiv 2411.02704, 2024) — modular affordance baseline\n- A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation (ICCV 2025, arXiv 2504.12636) — hierarchical affordance with zero-shot transfer but no language conditioning\n- RoboMAP: Adaptive Affordance Heatmaps via PaliGemma (arXiv 2510.10912, 2025) — modular language-conditioned heatmap architecture reference\n- AffordDP: Generalizable Diffusion Policy with Transferable Affordance (CVPR 2025) — cross-category transfer via 3D contact points\n- RAM: Retrieval-Based Affordance Transfer for Generalizable Zero-Shot Robotic Manipulation (CoRL 2024, arXiv 2407.04689) — retrieval-based affordance baseline\n- RAAP: Retrieval-Augmented Affordance Prediction with Cross-Image Action Alignment (arXiv 2603.29419, Mar 2026) — cross-image affordance alignment\n- Affogato: Learning Open-Vocabulary Affordance Grounding with Automated Data Generation at Scale (arXiv 2506.12009, 2025) — affordance quality benchmark\n- AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation (arXiv 2604.11674, 2026) — simulation evaluation resource\n- GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks (ICML 2018) — multi-task loss balancing\n- LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer (RSS 2026, arXiv 2602.10556) — cross-embodiment (not cross-category) zero-shot via language-action alignment\n",
7	  "status": "pending",
8	  "target_venues": [
9	    "AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — primary target, 64 days to abstract; strong fit for self-supervised consistency + architectural bottleneck contribution with robotics application)",
10	    "WACV 2027 Round 2 (registration Aug 20, paper Aug 27, 2026 — realistic backup, 101 days; vision+robotics focus)",
11	    "ICLR 2027 (abstract ~Sep 2026, full paper ~Sep 2026 — dates TBD, estimated from ICLR 2026 cycle; top-tier target if cross-category zero-shot results are strong)",
12	    "CVPR 2027 (registration ~Nov 2026, paper ~Nov 2026 — dates TBD; if affordance visualization and cross-category transfer results are visually compelling)",
13	    "NOTE: CoRL 2026 (abstract May 26, paper May 29) was the user's original target but is infeasible — 8 days is insufficient for implementation of affordance-gated bottleneck, 6 ablations, HOVA-500K pipeline, and multi-benchmark evaluation"
14	  ],
15	  "run_id": "run_20260518_180544_9f84bc"
16	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e69107c-ff19-49eb-9a51-ca5b594b9116",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "5935739d-db73-4565-8b43-73fedc08a497",
  "sourceToolAssistantUUID": "1e69107c-ff19-49eb-9a51-ca5b594b9116",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-27T18:43:58.984Z_

<details><summary>↩ Tool result · reported error · `toolu_01R8VhJPMbUKNE2ezrC1Rdxn`</summary>

```text
File content (52036 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83139e0a-6135-452c-9d00-912952987619",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "66c5235e-ad11-4606-9d66-77ba748657da",
  "toolUseResult": "Error: File content (52036 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "83139e0a-6135-452c-9d00-912952987619",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-27T18:44:02.459Z_

Now let me look at example result files to understand the expected JSON structure for a revised idea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66c5235e-ad11-4606-9d66-77ba748657da",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZs4TpLogQQQ1tHJMkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5ce33e8-f7d1-4bb9-806f-4135387fbd75",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvSYEqSxsg9uTpYqCBsP5Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9320,
      "cache_read_input_tokens": 13430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9320,
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

_source line 27 · 2026-05-27T18:44:03.311Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GuqAmvHuhRq5FmU6eV6JVR`</summary>

```json
{
  "file_path": "/home/ubuntu/idea_review/dispatch/results/result_corl_003_prod_s1.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5ce33e8-f7d1-4bb9-806f-4135387fbd75",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZs4TpLogQQQ1tHJMkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9a72498-66b3-4ead-ba38-4a4d2040a88f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvSYEqSxsg9uTpYqCBsP5Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9320,
      "cache_read_input_tokens": 13430,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9320
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 13430,
          "cache_creation_input_tokens": 9320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9320,
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

_source line 28 · 2026-05-27T18:44:03.639Z_

<details><summary>↩ Tool result · reported error · `toolu_01GuqAmvHuhRq5FmU6eV6JVR`</summary>

```text
File content (49018 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9a72498-66b3-4ead-ba38-4a4d2040a88f",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "f71453f4-69c9-4b2e-b8ec-ba5731cd6ad5",
  "toolUseResult": "Error: File content (49018 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "b9a72498-66b3-4ead-ba38-4a4d2040a88f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-27T18:44:06.277Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CYs8UiRm55REs1ovVstmFu`</summary>

```json
{
  "file_path": "/home/ubuntu/idea_review/dispatch/results/result_corl_003_prod_s1.json",
  "offset": 0,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f71453f4-69c9-4b2e-b8ec-ba5731cd6ad5",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZsQMPxurpGenoVhsjM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ea77a8c-cbcb-45ba-b786-499cb20cf93c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JRxfDgzNb1ooctzHMGSgT4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 176,
      "cache_read_input_tokens": 22750,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 176
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 112,
          "cache_read_input_tokens": 22750,
          "cache_creation_input_tokens": 176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 176,
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

_source line 30 · 2026-05-27T18:44:06.551Z_

<details><summary>↩ Tool result · reported error · `toolu_01CYs8UiRm55REs1ovVstmFu`</summary>

```text
File content (31607 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ea77a8c-cbcb-45ba-b786-499cb20cf93c",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "f2abdb24-79a1-45ad-9e99-e9a9c18a4fc6",
  "toolUseResult": "Error: File content (31607 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "7ea77a8c-cbcb-45ba-b786-499cb20cf93c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-27T18:44:09.441Z_

<details open><summary>🔧 Tool call — Read · `toolu_016h3j2PSvL8LCJza7HjsYiV`</summary>

```json
{
  "file_path": "/home/ubuntu/idea_review/dispatch/results/result_corl_003_prod_s1.json",
  "offset": 0,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2abdb24-79a1-45ad-9e99-e9a9c18a4fc6",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZscoW2sTow9SLmpDT1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61ceba84-66c0-4a9f-a499-c71405b2aaf5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WhNAr8HA4so3HCQoUgdhCZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 173,
      "cache_read_input_tokens": 22926,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 173
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 112,
          "cache_read_input_tokens": 22926,
          "cache_creation_input_tokens": 173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 173,
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

_source line 32 · 2026-05-27T18:44:09.802Z_

<details><summary>↩ Tool result · `toolu_016h3j2PSvL8LCJza7HjsYiV`</summary>

```text
0	{
1	  "原始标题": "LACVLA: Enforcing Language-Affordance Grounding via Consistency Objectives for Zero-Shot Cross-Category VLA Manipulation",
2	  "原始proposal": "# LACVLA: Enforcing Language-Affordance Grounding via Consistency Objectives for Zero-Shot Cross-Category VLA Manipulation\n\n## Core Problem\nHow can end-to-end VLA models achieve zero-shot manipulation transfer to entirely unseen object categories — objects with no visual precedent in training — given that (1) cross-category transfer fundamentally requires spatial grounding from language (the only cue that specifies WHERE to interact on a novel object), yet (2) current VLAs largely ignore language instructions (LIBERO-Plus, CVPR 2026; LangGap, Mar 2026), a failure mode that is survivable in-distribution but catastrophic when visual priors are absent?\n\n## Opportunity\nCross-category zero-shot manipulation — generalizing to objects never seen during training — remains an open challenge: even strong VLAs like π₀.₅ and GR00T-N1.6 fail on affordance generalization across object variants (BusyBox, Feb 2026), and A0 (ICCV 2025) achieves cross-category transfer via 1M contact points but without language conditioning. The fundamental bottleneck is that novel objects lack visual priors, so language must serve as the primary guide for spatial grounding — yet diagnostic work shows VLAs systematically ignore language. LIBERO-Plus (CVPR 2026, arXiv 2510.13626) reveals VLAs exhibit positional bias rather than semantic understanding; LangGap (arXiv 2603.00592, Mar 2026) quantifies this: VLAs with 95%+ standard success largely ignore language, and targeted data augmentation hits a ceiling (0%→28% multi-task). LIBERO-Para (Mar 2026) shows 22–52pp drops under paraphrased instructions, with 80–96% of failures from planning-level trajectory divergence. Shin (Mar 2026) achieves only +1.71pp via LLM-generated paraphrase augmentation, consistent with LangGap's ceiling finding. Recent approaches address aspects of this problem but not the full combination: spatial grounding methods (ST4VLA, ICLR 2026; SpatialVLA, RSS 2025) improve performance broadly but do not structurally guarantee language conditioning — a model can learn spatial shortcuts within training categories. GuidedVLA (RSS 2026) supervises individual attention heads with auxiliary signals but uses 3 predefined factor types without cross-category transfer focus. ProGAL-VLA (Apr 2026) imposes a verified grounding bottleneck via 3D entity-centric graphs and symbolic sub-goals, improving robustness (30.3%→71.5% on LIBERO-Plus perturbations) but requires explicit entity recognition rather than open-vocabulary affordance transfer. PPCL (EACL 2024) showed consistency regularization beats augmentation with 10× fewer samples in NLP. The opportunity: an affordance-gated architectural bottleneck with self-supervised consistency objectives that structurally forces language to condition spatial grounding — making language a mandatory pathway for action generation — enabling genuine cross-category zero-shot transfer without 3D sensors, expensive cross-category annotations, or modular decomposition.\n\n## Landscape\nThe VLA-affordance landscape has six relevant lineages, none of which combines architectural enforcement of language conditioning, self-supervised consistency on spatial affordance representations, and cross-category zero-shot transfer as the primary target. (1) Spatially-guided VLAs: ST4VLA (ICLR 2026, arXiv 2602.10109) introduces dual-system spatial grounding (Qwen2.5-VL planner + DiT/DINOv2 action expert), achieving 95.9% LIBERO average (98.0% Spatial, 99.0% Object, 93.8% Goal, 92.6% Long), 72%/61% attribute/spatial paraphrase robustness (vs π₀: 32%/31%), and 62% on new object instances (vs π₀: 32%, GR00T N1: 46%). This is LACVLA's strongest baseline — the null hypothesis is 'does explicit affordance consistency add value beyond spatial grounding alone?' InternVLA-M1 (arXiv 2510.13778) extends this with affordance recognition and chain-of-thought reasoning. SpatialVLA (RSS 2025, arXiv 2501.15830) introduces Ego3D Position Encoding and Adaptive Action Grids. Spatial Forcing (ICLR 2026, arXiv 2510.12276) aligns VLM features with 3D foundation models without 3D input at inference. All improve spatial understanding but none guarantees language conditions the spatial representation. (2) Supervised intermediate representation guidance: GuidedVLA (RSS 2026, arXiv 2605.12369) treats the action decoder as an assembly of functional components, supervising individual attention heads with auxiliary signals for three predefined factor types: object grounding (attention mass loss over detected object masks), spatial geometry (depth encoder feature constraint), and temporal skill logic (KL-divergence skill classification). Built on π₀, achieves 75.4% on LIBERO-Plus (vs 68.2% baseline), 90.63% on RoboTwin 2.0. Architectural parallel to LACVLA: both use explicit supervision on intermediate representations to improve VLA grounding. Key differences: GuidedVLA uses 3 predefined factor types (not open-vocabulary), does not use consistency objectives on heatmaps, does not produce affordance heatmaps, and does not target cross-category zero-shot transfer. LACVLA's affordance readout with stop-gradient bottleneck produces open-vocabulary spatial heatmaps enforced via self-supervised consistency — a fundamentally different supervision signal (consistency between paraphrases vs. factor-specific auxiliary losses). (3) Language grounding diagnostics and solutions: LIBERO-Plus (CVPR 2026, arXiv 2510.13626) reveals VLAs are insensitive to language and exhibit positional bias. LangGap (arXiv 2603.00592, Mar 2026) confirms VLAs ignore language and shows augmentation's ceiling (28% multi-task). LIBERO-Para (arXiv 2603.28301, Mar 2026) quantifies paraphrase fragility (22–52pp drops). Shin (arXiv 2603.16044, Mar 2026) achieves only +1.71pp via augmentation. ProGAL-VLA (arXiv 2604.09824, Apr 2026) constructs a 3D entity-centric graph with symbolic sub-goals and Grounding Alignment Contrastive loss, imposing a verified grounding bottleneck — achieves 71.5% robustness on LIBERO-Plus (up from 30.3%), but requires explicit entity recognition and 3D scene graphs, not applicable to open-vocabulary affordance transfer across unseen categories. Stable Language Guidance (ACL 2026, arXiv 2601.04052) addresses modality collapse at inference via residual steering — complementary to LACVLA's training-time approach. Attention recalibration (arXiv 2603.06001) provides train-free inference-time fix for attention sink dynamics but does not change learned representations. (4) Modular affordance-then-action pipelines: RT-Affordance (arXiv 2411.02704), UAD (ICRA 2025), RAM (CoRL 2024), RAAP (arXiv 2603.29419, Mar 2026), AffordDP (CVPR 2025), RoboMAP (arXiv 2510.10912), A0 (ICCV 2025, arXiv 2504.12636), and GLOVER++ (CoRL 2025, arXiv 2505.11865) all produce affordance representations but feed them to separate downstream planners/policies, sacrificing end-to-end optimization. A0 achieves zero-shot cross-category transfer via 1M contact points but without language conditioning. (5) Architectural bottleneck enforcement: DIAL (arXiv 2603.29844, Mar 2026) enforces a latent intent bottleneck via inverse dynamics — the action head MUST use predicted latent intent. This inspires LACVLA's affordance-gated bottleneck (stop-gradient on VLM features, affordance map as spatial attention gate). (6) Cross-category zero-shot benchmarks: AGNOSTOS/X-ICM (arXiv 2505.15660) provides 23 unseen manipulation tasks. VLA² (arXiv 2510.14902) uses agentic retrieval for unseen concepts. BusyBox (arXiv 2602.05441, Feb 2026) is a physical benchmark where 6 reconfigurable modules test affordance generalization — even π₀.₅ and GR00T-N1.6 fail on shuffled configurations despite identical affordances, demonstrating that affordance generalization remains unsolved. Gap: No existing work combines (a) architectural enforcement that language must condition spatial features via stop-gradient bottleneck, (b) self-supervised consistency objectives on affordance heatmaps (not raw actions, not predefined factor types), and (c) cross-category zero-shot transfer as the primary evaluation target.\n\n## Description\nWe address cross-category zero-shot manipulation transfer — generalizing to objects with no visual precedent in training — where language is the only available guide for spatial grounding on novel objects. We show that the well-documented language-ignoring failure in VLAs (LIBERO-Plus, CVPR 2026; LangGap, Mar 2026) is particularly catastrophic in this setting: visual priors and layout memorization cannot compensate when the object itself is unseen. Existing approaches either improve spatial understanding without guaranteeing language conditions the representation (ST4VLA, SpatialVLA, Spatial Forcing), supervise predefined intermediate factor types without cross-category affordance transfer (GuidedVLA, RSS 2026), impose grounding bottlenecks requiring explicit entity recognition (ProGAL-VLA), or produce affordance representations in modular pipelines sacrificing end-to-end optimization (A0, GLOVER++, RT-Affordance). LACVLA proposes an affordance-gated architectural bottleneck, inspired by DIAL's latent intent bottleneck, that structurally forces all task-relevant spatial information through a language-conditioned affordance map: VLM intermediate features pass through stop-gradient before the action head, which receives affordance_heatmap ⊙ sg(visual_features) + proprioceptive_state. The affordance map (produced via cross-attention between VLM features and language tokens) acts as a spatial attention gate — a uniform (language-ignoring) map yields unselective features and degraded performance. Self-supervised consistency objectives enforce language-affordance grounding: IPAC ensures semantically equivalent instructions produce identical affordance maps (transferring PPCL's consistency > augmentation principle from NLP to spatial heatmaps), while IDA ensures semantically different instructions produce divergent maps (preventing collapse). Affordance readout is pre-trained via HOVA-500K with a fully specified self-supervised fallback using robot-data pseudo-affordance labels from gripper contact positions — eliminating HOVA-500K as a single point of failure and producing an ablation that determines whether HOVA-500K pre-training is necessary. A streamlined 6-variant ablation suite (reduced from 8 to fit ≤200 H100-hour budget) addresses all key questions: bottleneck necessity (#2, merged sub-conditions: no bottleneck vs. bottleneck-only), end-to-end vs. modular (#3), augmentation ceiling (#4), affordance maps vs. raw actions as consistency target (#5 — the paper's critical test: if affordance-level consistency outperforms action-level, it validates that isolating WHERE from HOW is essential), and value beyond spatial grounding (#6). Evaluation is anchored on cross-category zero-shot transfer as the PRIMARY metric: held-out object categories, HOVA-500K cross-category splits, AGNOSTOS benchmark, BusyBox affordance generalization (supplementary physical evaluation), and real-world tests on 5+ unseen categories. SECONDARY metrics cover paraphrase robustness (LIBERO-Para, LangGap), affordance quality (Affogato), and in-distribution performance (standard LIBERO). Primary target: AAAI 2027 (abstract Jul 21, 64 days).\n\n## Approach\nWe propose LACVLA, an end-to-end VLA that structurally forces language to condition spatial affordance grounding through an affordance-gated bottleneck and self-supervised consistency objectives, enabling zero-shot cross-category manipulation transfer.\n\nArchitecture — Affordance-Gated Bottleneck (inspired by DIAL's latent intent bottleneck): Built on a 4B–7B VLM backbone (Qwen2-VL-4B via StarVLA or PaliGemma2) with LoRA fine-tuning. The architecture has three components:\n(a) Affordance Readout: A cross-attention layer where language instruction tokens attend over intermediate VLM visual features (layer ~16 of 32 for Qwen2-VL), producing a dense affordance heatmap over the image. This encodes WHERE to interact, conditioned on the instruction. Architecture: single cross-attention + LayerNorm + linear projection to H×W heatmap, <5M parameters.\n(b) Stop-Gradient Bottleneck: VLM intermediate visual features are passed through a stop-gradient before reaching the action head. The action head receives: affordance_heatmap ⊙ sg(VLM_visual_features) + proprioceptive_state. The affordance map acts as a spatial attention gate — if the model produces a uniform (language-ignoring) affordance map, the action head receives unselective visual features with no spatial focus, degrading performance. Unlike GuidedVLA's factor-specific head supervision (predefined types, direct auxiliary losses), LACVLA's stop-gradient ensures no task-semantic gradient flows through the non-affordance pathway — the action head CANNOT learn to extract task information from raw VLM features, and the affordance readout is open-vocabulary rather than restricted to predefined factor categories.\n(c) Flow-Matching Action Head: A lightweight DiT (Diffusion Transformer) that generates trajectory chunks conditioned on the affordance-gated visual features + proprioceptive state, following the flow-matching formulation.\n\nTraining Objectives — Three jointly optimized losses with phased schedule:\n(1) Instruction-Paraphrase Affordance Consistency (IPAC): Given the same visual scene and K LLM-generated paraphrases of the same task instruction (e.g., 'grab the mug handle' vs. 'grasp the cup by its handle'), the affordance maps must be consistent (KL divergence penalty on spatial heatmaps). This transfers the consistency regularization principle from PPCL (EACL 2024) — which showed consistency > augmentation with 10× less data in NLP — to spatial affordance heatmaps. Unlike Shin (2026), who uses paraphrases purely as data augmentation (+1.71pp), IPAC uses them as a regularization signal constraining affordance geometry. Paraphrases generated offline by LLM — free, unlimited supervision.\n(2) Instruction-Discriminative Affordance (IDA): Given the same visual scene and two semantically different instructions (e.g., 'pick up the mug by its handle' vs. 'pour from the mug'), the affordance maps must diverge (margin-based divergence loss). This prevents degenerate consistency collapse where the model produces instruction-invariant heatmaps to trivially satisfy IPAC. Different-instruction pairs come naturally from multi-task robot datasets.\n(3) Action-Grounded Affordance (AGA): Standard flow-matching loss for trajectory prediction through the affordance-gated bottleneck. This grounds the affordance map in manipulation-relevant contact regions via end-to-end backpropagation through the gating mechanism.\n\nPhased Training Schedule:\nPhase 1 — Affordance Readout Pre-training: PRIMARY path: pre-train on HOVA-500K with cross-attention readout predicting contact-point Gaussian heatmaps (σ proportional to object scale) conditioned on action-label text prompts from 675 action categories. Viewpoint augmentation (random crop, perspective warp, ego→third-person style augmentation) addresses the ego-centric domain gap. FALLBACK path (if domain gap diagnostic fails): self-supervised affordance readout initialization using robot data alone — extract pseudo-affordance Gaussian heatmaps from gripper position at grasp/contact time in robot trajectory data (well-established technique: text-driven affordance learning with pseudo-labels, trajectory-based contact recovery). This produces lower-coverage but higher-fidelity affordance supervision for the robot observation domain. Diagnostic checkpoint: evaluate pre-trained affordance readout on a held-out set of robot observation images; if domain gap degrades affordance quality below threshold (mean IoU < 0.3 between predicted heatmap peak and gripper contact region), switch to fallback path. Ablation of HOVA-500K vs. self-supervised initialization determines whether HOVA-500K is necessary, de-risking the paper from the HOVA-500K dependency.\nPhase 2 — End-to-end VLA training (steps 0–N): Fine-tune full model (VLM via LoRA + pre-trained affordance readout + flow-matching action head) on robot data. Sub-phases: (2a) AGA only for 10% of training — establish action grounding baseline. (2b) Add IPAC at 10% — enforce consistency while action loss stabilizes gradients. (2c) Ramp IDA from 0 to full weight over 15% of training via linear warmup, monitored by: (i) affordance entropy H(A) — if H(A) < 0.3 × H_max, increase IDA weight by 50%; (ii) instruction-discriminability D = mean pairwise KL between different-instruction maps on validation set — if D < 0.5, halt IPAC and boost IDA. GradNorm-style gradient normalization across the three losses balances training rates automatically.\n\nWhy Affordance Maps (Not Raw Actions) for Consistency: Affordance maps capture WHERE to interact — the geometric invariant across paraphrases and across categories sharing functional parts. Action distributions conflate WHERE + HOW + WHEN (trajectory shape, timing, force), making consistency regularization noisier. For cross-category transfer, WHERE is what transfers (handle locations generalize across mugs/cups/pitchers), while HOW adapts to object-specific geometry. This argument is validated empirically by ablation #5.\n\nCross-Object Functional Consistency via HOVA-500K: Group HOVA-500K images by shared action labels (675 categories) and apply soft KL penalty between affordance maps of same-action images from different object categories. This provides weak supervision for cross-category affordance consistency without requiring part-level functional equivalence annotations.\n\nData Pipeline: Open X-Embodiment and DROID for robot trajectories, HOVA-500K for affordance pre-training and cross-object grouping (with self-supervised robot-data fallback), LLM-generated instruction paraphrases (Qwen3 or GPT-4) for IPAC pairs.\n\nAblation Design (6 variants, streamlined to fit compute budget while retaining all core tests):\n(1) Full LACVLA — affordance-gated bottleneck + IPAC + IDA + AGA\n(2) Bottleneck analysis (merged): (a) No affordance bottleneck — direct VLA without affordance readout; (b) Bottleneck + AGA only, no consistency losses — tests whether architectural bottleneck alone suffices. Both sub-conditions use identical training data and hyperparameters; affordance map quality (entropy, instruction-discriminability) tracked for sub-condition (b) to diagnose whether the bottleneck induces meaningful affordance structure without consistency enforcement.\n(3) Modular composition — frozen GLOVER++ affordance → separate policy (tests end-to-end vs. modular)\n(4) Shin-style augmentation — paraphrases added as training data, no consistency loss (tests data augmentation ceiling, paralleling PPCL's NLP finding)\n(5) IPAC on raw actions — KL divergence between action distributions under paraphrased instructions, no affordance readout (CRITICAL: tests whether isolating WHERE via affordance maps outperforms consistency on conflated action distributions — if affordance maps win, that's the paper's key finding; if raw actions work comparably, the affordance readout is unnecessary overhead)\n(6) ST4VLA-style spatial grounding + IPAC on features — spatial grounding pre-training + consistency on intermediate VLM features without affordance readout (tests whether explicit affordance structure adds value beyond strong spatial pre-training + consistency)\n\nEvaluation Protocol — Primary (Cross-Category Zero-Shot Transfer):\n(a) Held-out object category experiments: partition LIBERO/DROID object categories into train/test sets, test on entirely unseen categories with both standard and paraphrased instructions\n(b) HOVA-500K cross-category transfer tests: train on K action categories with one set of objects (e.g., 'pour from pitcher'), test on same actions with different object categories (e.g., 'pour from kettle') — constructed from HOVA-500K's 675 shared action labels\n(c) AGNOSTOS benchmark (arXiv 2505.15660) for cross-task zero-shot evaluation (23 unseen tasks)\n(d) BusyBox (arXiv 2602.05441) supplementary evaluation: if physical hardware is available, test LACVLA on shuffled BusyBox configurations where even π₀.₅ and GR00T-N1.6 fail — directly measures affordance generalization across visual variants with identical functional affordances\n(e) Real-world evaluation on 5+ unseen object categories across at least 3 manipulation primitives (grasp, pour, push)\n\nEvaluation Protocol — Secondary:\n(f) LIBERO-Para benchmark with PRIDE metric for paraphrase robustness (direct comparison with ST4VLA's 72%/61%)\n(g) LangGap protocol for language grounding quality (targeting improvement over the 28% multi-task ceiling)\n(h) Affogato for affordance quality assessment\n(i) Standard LIBERO (Spatial, Object, Goal, Long) for in-distribution comparison with ST4VLA (95.9% avg)\n\nCoRL 2026 Infeasibility Statement: CoRL 2026 (abstract May 26 — 8 days from today, May 18) is infeasible given implementation scope. Primary target: AAAI 2027 (abstract Jul 21, full paper Jul 28 — 64 days to abstract). Backup: WACV 2027 Round 2 (paper Aug 27 — 101 days).\n\n## Resource Estimate\n{'auto_research': {'claude_api_cost': '$500-1,200 (estimated 5,000-12,000 agent turns)', 'estimated_gpu_cost': '$675-975 (at ~$1.50/h A100 80GB)', 'gpu_hours': '~450-650h A100 80GB, equivalent to ~320-465h H100 at conservative 1.4x ratio (agent explores 14-20 training configurations for phased schedule tuning, all 6 ablation variants × 2-3 seeds, both HOVA-500K and self-supervised affordance pre-training paths, full benchmark sweeps)', 'gpu_utilization': '~85-95% — agent immediately queues next experiment upon completion; parallel ablation runs on multi-GPU setup', 'risk_note': 'Automated phased training managed by entropy/discriminability monitoring. If affordance-gated bottleneck causes consistent performance collapse across configurations, agent escalates to soft-gating variants. GradNorm balancing reduces sensitivity to manual loss weight tuning. Self-supervised fallback eliminates HOVA-500K as a single point of failure.', 'speed_bottleneck': 'Each LoRA training run on 4B backbone takes ~8-12h on 4 A100s. HOVA-500K preprocessing and viewpoint-augmented Gaussian heatmap generation ~25h one-time. Cross-category evaluation setup ~6h one-time.', 'team': '0 researchers after initial setup (~6-8 hours: dataset access, paraphrase generation config, HOVA-500K + self-supervised preprocessing, AGNOSTOS/LIBERO-Para/LangGap environment setup, cross-category held-out split definition)', 'timeline': '3-4 weeks with 4+ A100 GPUs available concurrently (bottleneck: affordance pre-training → domain gap diagnostic → phased training search → cross-category evaluation)'}, 'human_in_loop': {'claude_api_cost': '$200-500 (estimated 2,000-5,000 agent turns)', 'estimated_gpu_cost': '$340-465 (at ~$1.50/h A100 80GB)', 'gpu_hours': '~225-310h A100 80GB, equivalent to ~160-220h H100 at conservative 1.4x ratio (agent runs 8-10 training configurations systematically: all 6 ablations + 2-4 additional hyperparameter variants, HOVA-500K pre-training or self-supervised fallback, with wasted runs caught early by human)', 'gpu_utilization': '~40-55% — agent queues experiments but pauses at key gates: (1) affordance readout domain gap diagnostic (HOVA-500K vs. self-supervised), (2) affordance map quality inspection after bottleneck warmup, (3) cross-category held-out split design approval', 'risk_note': 'Primary risk: HOVA-500K affordance readout domain gap — fully mitigated by self-supervised fallback using robot-data pseudo-affordance labels from gripper contact positions, with ablation comparing both paths. Secondary risk: affordance-gated bottleneck may be too restrictive — mitigated by ablation #2b (bottleneck without consistency) to isolate the effect. ST4VLA comparison (ablation #6) determines value beyond spatial grounding.', 'team': '1 researcher, ~1.5h/day review', 'timeline': '6-8 weeks (agent handles paraphrase generation, HOVA-500K or self-supervised preprocessing, hyperparameter sweeps, AGNOSTOS/LIBERO-Para/LangGap evaluation scripts; human approves domain gap bridging strategy, inspects affordance maps, validates cross-category split design)'}, 'manual': {'estimated_gpu_cost': '$265-370 (at ~$1.50/h A100 80GB)', 'gpu_hours': '~175-245h A100 80GB, equivalent to ~125-175h H100 at conservative 1.4x ratio (HOVA-500K affordance readout pre-training ~20h or self-supervised fallback ~8h, 1 full LACVLA training run ~35-45h, 5 ablation experiments at ~12-18h each = 60-90h, cross-category evaluation sweeps ~25h, AGNOSTOS benchmark runs ~15h, BusyBox evaluation if available ~5h). 6 ablations (down from 8) are the key cost savings: merging bottleneck analysis into one experiment with sub-conditions and dropping phased-training ablation saves ~30-40h A100.', 'gpu_utilization': '~15-25% effective utilization — idle during result analysis, loss weight iteration, domain gap diagnostics between phases', 'team': '2 researchers (1 lead on affordance-gated architecture + consistency objectives + bottleneck enforcement, 1 on data pipeline/HOVA-500K integration/cross-category evaluation/AGNOSTOS setup)', 'timeline': '8-10 weeks (1-2 weeks data pipeline + affordance readout pre-training (HOVA-500K or self-supervised fallback) + domain gap diagnostics; 4-5 weeks iterative experimentation including all 6 ablations; 2-3 weeks cross-category evaluation + paper writing)'}}\n\n## Key References\n- ST4VLA: Spatially Guided Training for Vision-Language-Action Models (ICLR 2026, arXiv 2602.10109) — strongest baseline: 95.9% LIBERO avg, 72%/61% paraphrase robustness, 62% unseen objects via spatial grounding alone\n- LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626) — diagnostic revealing VLAs ignore language instructions, exhibit positional bias\n- LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models (arXiv 2603.00592, Mar 2026) — quantifies language gap: augmentation reaches 90% single-task but only 28% multi-task\n- GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization (RSS 2026, arXiv 2605.12369, May 2026) — supervises 3 predefined attention head types (object/spatial/temporal) on π₀; 75.4% LIBERO-Plus, 90.63% RoboTwin; architectural parallel (supervised intermediate representations) but no consistency objectives, no affordance heatmaps, no cross-category transfer\n- BusyBox: Benchmarking Affordance Generalization (arXiv 2602.05441, Feb 2026, Microsoft) — physical benchmark with 6 reconfigurable modules; even π₀.₅ and GR00T-N1.6 fail on shuffled configurations; directly tests affordance generalization across visual variants\n- ProGAL-VLA: Grounded Alignment through Prospective Reasoning in VLA Models (arXiv 2604.09824, Apr 2026) — verified grounding bottleneck via 3D entity-centric graph + GAC loss; 71.5% LIBERO-Plus robustness; requires explicit entity recognition, not applicable to open-vocabulary affordance transfer\n- DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA (arXiv 2603.29844, Mar 2026) — latent intent bottleneck via inverse dynamics, inspiration for affordance-gated architecture\n- InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy (arXiv 2510.13778) — spatially guided VLA with affordance recognition in pre-training\n- SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models (RSS 2025, arXiv 2501.15830) — spatial-aware action tokenization\n- Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model (ICLR 2026, arXiv 2510.12276) — implicit spatial alignment without 3D input\n- AGNOSTOS / X-ICM: Exploring the Limits of Vision-Language-Action Manipulations in Cross-task Generalization (arXiv 2505.15660) — cross-task zero-shot benchmark with 23 unseen tasks\n- LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models (arXiv 2603.28301, Mar 2026) — paraphrase robustness evaluation with PRIDE metric\n- Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation (Shin, arXiv 2603.16044, Mar 2026) — direct augmentation baseline, +1.71pp only\n- Stable Language Guidance / Residual Semantic Steering for VLAs (ACL 2026, arXiv 2601.04052) — inference-time modality collapse mitigation, complementary to LACVLA's training-time approach\n- Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration (arXiv 2603.06001, Mar 2026) — diagnoses attention sink dynamics as cause of linguistic blindness; train-free inference fix complementary to LACVLA\n- Prompt Perturbation Consistency Learning for Robust Language Models (PPCL, EACL 2024, arXiv 2402.15833) — consistency regularization > augmentation with 10× fewer samples in NLP\n- Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs (arXiv 2510.14242, Oct 2025) — extends PPCL to LLMs\n- OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024) — base VLA architecture\n- StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing (arXiv 2604.05014, Apr 2026) — implementation framework\n- GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation (CoRL 2025, arXiv 2505.11865) — provides HOVA-500K dataset, modular baseline\n- PokéVLA: Empowering Pocket-Sized VLA Model with Comprehensive World Knowledge Guidance (arXiv 2604.20834, Apr 2026) — validates HOVA-500K ego→VLA transfer for backbone pre-training\n- RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (arXiv 2411.02704, 2024) — modular affordance baseline\n- A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation (ICCV 2025, arXiv 2504.12636) — hierarchical affordance with zero-shot transfer but no language conditioning\n- RoboMAP: Adaptive Affordance Heatmaps via PaliGemma (arXiv 2510.10912, 2025) — modular language-conditioned heatmap architecture reference\n- AffordDP: Generalizable Diffusion Policy with Transferable Affordance (CVPR 2025) — cross-category transfer via 3D contact points\n- RAM: Retrieval-Based Affordance Transfer for Generalizable Zero-Shot Robotic Manipulation (CoRL 2024, arXiv 2407.04689) — retrieval-based affordance baseline\n- RAAP: Retrieval-Augmented Affordance Prediction with Cross-Image Action Alignment (arXiv 2603.29419, Mar 2026) — cross-image affordance alignment\n- Affogato: Learning Open-Vocabulary Affordance Grounding with Automated Data Generation at Scale (arXiv 2506.12009, 2025) — affordance quality benchmark\n- AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation (arXiv 2604.11674, 2026) — simulation evaluation resource\n- GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks (ICML 2018) — multi-task loss balancing\n- LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer (RSS 2026, arXiv 2602.10556) — cross-embodiment (not cross-category) zero-shot via language-action alignment\n",
3	  "最终proposal": "# LACVLA: Enforcing Language-Affordance Grounding via Consistency Objectives for Zero-Shot Cross-Category VLA Manipulation\n\n## Core Problem\nHow can end-to-end VLA models achieve zero-shot manipulation transfer to entirely unseen object categories — objects with no visual precedent in training — given that (1) cross-category transfer fundamentally requires spatial grounding from language (the most general cue for specifying WHERE to interact on a novel object when visual analogues are unavailable), yet (2) current VLAs largely ignore language instructions (LIBERO-Plus, CVPR 2026; LangGap, Mar 2026), a failure mode survivable in-distribution but catastrophic when visual priors are absent, and (3) existing architectural solutions to language ignoring (LangForce, arXiv 2601.15197; BayesVLA, arXiv 2512.11218) enforce conditioning at the raw action level, conflating WHERE to interact with HOW to execute — a conflation that does not isolate the spatially transferable component needed for cross-category generalization?\n\n## Opportunity\nCross-category zero-shot manipulation remains open: even π₀.₅ and GR00T-N1.6 fail on affordance generalization across object variants (BusyBox, Feb 2026), and A0 (ICCV 2025) achieves cross-category transfer via 1M contact points but without language conditioning. The fundamental bottleneck is that novel objects lack visual priors, making language the most general guide for spatial grounding — yet VLAs systematically ignore language. LIBERO-Plus (CVPR 2026, arXiv 2510.13626) reveals positional bias rather than semantic understanding; LangGap (arXiv 2603.00592, Mar 2026) quantifies this: VLAs with 95%+ success largely ignore language, with augmentation hitting a ceiling (0%→28% multi-task). LIBERO-Para (Mar 2026) shows 22–52pp drops under paraphrased instructions. Shin (Mar 2026) achieves only +1.71pp via LLM-generated paraphrase augmentation, consistent with LangGap's ceiling.\n\nRecent architectural solutions address language ignoring at the action level: LangForce (arXiv 2601.15197, Jan 2026) enforces language conditioning via Bayesian decomposition with Latent Action Queries, achieving 66.5% LIBERO and +11.3% SimplerEnv OOD; BayesVLA (arXiv 2512.11218, Dec 2025) takes a similar factorization. However, both enforce conditioning on the full action distribution, conflating WHERE with HOW. For cross-category transfer this is limiting: WHERE generalizes (handle locations transfer across mugs/cups/pitchers), while HOW adapts to object-specific geometry. Visual correspondence methods (Robo-ABC, ECCV 2024, arXiv 2401.07487: 85.7% on 7 categories) transfer affordances without language but require analogous objects in retrieval memory, degrading for truly novel objects. Spatial grounding methods (ST4VLA, ICLR 2026; SpatialVLA, RSS 2025) improve performance broadly but do not structurally guarantee language conditions the spatial representation. GuidedVLA (RSS 2026) supervises 3 predefined attention head factor types without cross-category focus. ProGAL-VLA (Apr 2026) imposes a grounding bottleneck via 3D entity-centric graphs but requires explicit entity recognition. PPCL (EACL 2024) showed consistency regularization beats augmentation with 10× fewer samples in NLP — we hypothesize and test whether this principle transfers to spatially structured affordance heatmaps, a non-trivial domain shift constituting a testable contribution.\n\nThe opportunity: enforce language conditioning specifically at the spatial affordance level — isolating WHERE from HOW — via an affordance-gated bottleneck with self-supervised consistency objectives. We term this the Spatial Mediation Hypothesis (SMH): in manipulation, language conditions behavior primarily through spatial affordance (WHERE), and consistency regularization at this level outperforms consistency at the conflated action level (WHERE+HOW). This hypothesis is motivated by the information bottleneck principle (Tishby et al., 2000): for cross-category transfer, the optimal instruction-conditioned representation should compress out category-specific visual details while retaining category-invariant spatial semantics. If validated, LACVLA yields both a superior architecture for cross-category transfer and a scientific insight about the computational structure of language-conditioned manipulation.\n\n## Landscape\nThe VLA-affordance landscape has seven relevant lineages, none combining architectural enforcement of language conditioning at the spatial affordance level, self-supervised consistency on affordance heatmaps, and cross-category zero-shot transfer as primary target.\n\n(1) Spatially-guided VLAs: ST4VLA (ICLR 2026, arXiv 2602.10109) introduces dual-system spatial grounding (Qwen2.5-VL planner + DiT/DINOv2 action expert), achieving 95.9% LIBERO average (98.0% Spatial, 99.0% Object, 93.8% Goal, 92.6% Long), 72%/61% attribute/spatial paraphrase robustness (vs π₀: 32%/31%), and 62% on new object instances (vs π₀: 32%, GR00T N1: 46%). LACVLA's strongest in-distribution baseline. InternVLA-M1 (arXiv 2510.13778) extends with affordance recognition and chain-of-thought. SpatialVLA (RSS 2025, arXiv 2501.15830) introduces Ego3D Position Encoding. Spatial Forcing (ICLR 2026, arXiv 2510.12276) aligns VLM features with 3D foundation models without 3D input at inference. All improve spatial understanding but none guarantees language conditions the spatial representation.\n\n(2) Supervised intermediate representation guidance: GuidedVLA (RSS 2026, arXiv 2605.12369) supervises individual attention heads for 3 predefined factor types (object grounding, spatial geometry, temporal skill logic) on π₀; 75.4% LIBERO-Plus, 90.63% RoboTwin 2.0. Architectural parallel to LACVLA but predefined factors (not open-vocabulary), no consistency objectives, no cross-category focus. CoA-VLA (ICCV 2025, arXiv 2412.20451) uses chain-of-affordance reasoning with 4 affordance types via visual-textual chain-of-thought — explicit affordance reasoning via language generation rather than spatial heatmap consistency.\n\n(3) Language grounding diagnostics and solutions: LIBERO-Plus (CVPR 2026, arXiv 2510.13626) reveals language insensitivity. LangGap (arXiv 2603.00592, Mar 2026) confirms augmentation ceiling (28% multi-task). LIBERO-Para (arXiv 2603.28301, Mar 2026) quantifies paraphrase fragility (22–52pp drops, 80–96% failures from planning-level divergence). Shin (arXiv 2603.16044, Mar 2026) achieves +1.71pp via augmentation. ProGAL-VLA (arXiv 2604.09824, Apr 2026) constructs 3D entity-centric graph with GAC loss; 71.5% LIBERO-Plus robustness but requires explicit entity recognition. Stable Language Guidance (ACL 2026, arXiv 2601.04052) addresses modality collapse at inference via residual steering — complementary to LACVLA's training-time approach. Attention recalibration (arXiv 2603.06001) provides train-free inference-time fix. FocusVLA (arXiv 2603.28740, Mar 2026) addresses visual information underutilization via Modality Cascaded Attention, eliminating shortcut pathways — an attention-mechanism approach to input utilization vs. LACVLA's information-bottleneck approach to language grounding.\n\n(4) Modular affordance-then-action pipelines: RT-Affordance (arXiv 2411.02704), UAD (ICRA 2025), RAM (CoRL 2024, arXiv 2407.04689), RAAP (arXiv 2603.29419, Mar 2026), AffordDP (CVPR 2025), RoboMAP (arXiv 2510.10912), A0 (ICCV 2025, arXiv 2504.12636), and GLOVER++ (CoRL 2025, arXiv 2505.11865) produce affordance representations but feed them to separate policies, sacrificing end-to-end optimization. A0 achieves cross-category transfer via 1M contact points without language conditioning. Robo-ABC (ECCV 2024, arXiv 2401.07487) achieves cross-category affordance generalization (85.7% on 7 categories) via visual semantic correspondence without language, but requires retrieval memory and is non-end-to-end. RoboPCA (arXiv 2603.07691, Mar 2026) achieves pose-centered affordance prediction with 18.6% improvement over MOKA on AGD20K and 38.5% on RLBench — strong modular cross-category affordance baseline. Bi-Adapt (arXiv 2602.08425, Feb 2026) demonstrates cross-category bimanual affordance mapping via vision foundation model correspondence — evidence that cross-category affordance transfer is an active and growing research direction.\n\n(5) Architectural bottleneck enforcement for language conditioning: DIAL (arXiv 2603.29844, Mar 2026) enforces latent intent bottleneck via inverse dynamics — architectural inspiration for LACVLA. LangForce (arXiv 2601.15197, Jan 2026) diagnoses \"Information Collapse\" and enforces language conditioning via Bayesian decomposition with Latent Action Queries and Log-Likelihood Ratio optimization; 66.5% LIBERO, +11.3% SimplerEnv OOD; integrated into StarVLA. BayesVLA (arXiv 2512.11218, Dec 2025) takes a similar Bayesian factorization. Both enforce conditioning at the raw action level (WHERE+HOW conflated). LACVLA differs critically: (i) enforces conditioning at the spatial affordance level (WHERE only), isolating the cross-category transferable component; (ii) uses self-supervised consistency objectives on spatial heatmaps rather than likelihood-ratio optimization on action distributions.\n\n(6) Cross-category zero-shot benchmarks: AGNOSTOS/X-ICM (arXiv 2505.15660) provides 23 unseen tasks; X-ICM 72B achieves 30.1% average (vs π₀ 24.1%, VoxPoser 22.2%). VLA² (arXiv 2510.14902) uses agentic retrieval. BusyBox (arXiv 2602.05441, Feb 2026) tests affordance generalization across 6 reconfigurable modules — even π₀.₅ and GR00T-N1.6 fail on shuffled configurations.\n\n(7) Cross-embodiment and cross-task transfer: LAP (RSS 2026, arXiv 2602.10556) achieves cross-embodiment zero-shot via language-action alignment (not cross-category).\n\nGap: No existing work combines (a) architectural enforcement of language conditioning at the spatial affordance level via stop-gradient bottleneck, (b) self-supervised consistency objectives on affordance heatmaps with hierarchical loss structure (within-scene grounding + cross-category abstraction), and (c) cross-category zero-shot transfer as primary target. LangForce/BayesVLA enforce at the action level; GuidedVLA uses predefined factor types without consistency; Robo-ABC/RoboPCA achieve cross-category affordance transfer but modularly and (for Robo-ABC) without language; CoA-VLA reasons about affordances via chain-of-thought but without spatial heatmap consistency.\n\n## Description\nWe address cross-category zero-shot manipulation transfer. We argue that the well-documented language-ignoring failure in VLAs (LIBERO-Plus, LangGap) is particularly catastrophic for unseen object categories, and that existing solutions operating at the action level (LangForce, BayesVLA) do not isolate the spatially transferable component.\n\n**Spatial Mediation Hypothesis (SMH):** In manipulation, language conditions behavior primarily through spatial affordance (WHERE), and consistency regularization applied at this representational level outperforms consistency at the conflated action level (WHERE+HOW). This hypothesis is motivated by the information bottleneck principle (Tishby et al., 2000): for cross-category transfer, the optimal instruction-conditioned representation should compress out category-specific visual details (execution trajectories, object geometry) while retaining category-invariant spatial semantics (contact regions, functional zones). The stop-gradient bottleneck instantiates this principle architecturally — the action head can only access task-relevant information through the affordance heatmap, which serves as an approximate minimal sufficient statistic between instruction and action for the WHERE component. This yields a quantifiable prediction: I(affordance; instruction) should be high while I(affordance; category_identity) should be low — measurable via linear probe classification accuracy on affordance features, reported as a diagnostic metric at zero additional compute cost.\n\n**SMH Scope:** SMH targets WHERE-dominant manipulation tasks (handle grasping, surface pushing, rim pouring) where cross-category transfer depends primarily on spatial affordance localization. For HOW-dominant tasks where language specifies manner, force, or speed (\"gently place\" vs. \"drop\"), the stop-gradient design blocks HOW-semantic language differences from reaching the action head. We acknowledge this boundary explicitly and report evaluation results disaggregated by WHERE-dominant and HOW-dominant task groups. Extending the architecture with a low-dimensional language-conditioned style vector for HOW information (bypassing stop-gradient) is future work.\n\n**PPCL Transfer Hypothesis:** The PPCL (EACL 2024, arXiv 2402.15833) principle — consistency regularization outperforms augmentation with 10× fewer samples — serves as motivation, but its transfer from continuous NLP embeddings to spatially structured affordance heatmaps is a testable hypothesis. The domain shift is non-trivial: heatmaps have spatial structure and sharp boundaries absent in NLP embeddings. Ablation #4 (Shin-style augmentation) vs. Full LACVLA directly tests this.\n\n**Loss Hierarchy:** LACVLA's four training objectives form a principled hierarchy: (1) IPAC + IDA provide within-scene language grounding — ensuring that language faithfully conditions spatial representations (prerequisite, addresses the language-ignoring diagnostic). (2) COFC provides cross-category affordance abstraction — enforcing that functionally equivalent affordances across different object categories produce aligned spatial representations. This is the paper's most distinctive loss, operationalizing a computational version of the cross-object affordance generalization principle from ecological psychology (Gibson, 1979): functional affordances are properties of action-object relationships that abstract over object-specific visual features. (3) AGA provides standard task grounding through flow-matching trajectory loss. The hierarchy reflects the causal structure: within-scene grounding is necessary for cross-category abstraction, which in turn is necessary for zero-shot transfer.\n\n**Architecture:** Affordance-gated bottleneck (inspired by DIAL) where VLM features pass through stop-gradient before the action head, receiving affordance_heatmap ⊙ sg(visual_features) + proprioceptive_state. Unlike LangForce's Bayesian decomposition at the action level, this isolates spatial affordance (WHERE) from trajectory execution (HOW).\n\n**Core experimental tests:** Ablation #5 (IPAC on raw actions vs. affordance maps) is the SMH's critical test. Ablation #7 (Full minus COFC) tests whether cross-category abstraction adds value beyond within-scene grounding. Both positive and negative outcomes are scientifically informative.\n\n## Approach\nWe propose LACVLA, an end-to-end VLA that structurally forces language to condition spatial affordance grounding through an affordance-gated bottleneck and self-supervised consistency objectives, enabling zero-shot cross-category manipulation transfer.\n\nArchitecture — Affordance-Gated Bottleneck (inspired by DIAL's latent intent bottleneck): Built on a 4B–7B VLM backbone (Qwen2-VL-4B via StarVLA or PaliGemma2) with LoRA fine-tuning. Three components:\n(a) Affordance Readout: Cross-attention layer where language instruction tokens attend over intermediate VLM visual features (layer ~16 of 32 for Qwen2-VL), producing a dense affordance heatmap encoding WHERE to interact conditioned on instruction. Single cross-attention + LayerNorm + linear projection to H×W heatmap, <5M parameters.\n(b) Stop-Gradient Bottleneck: VLM visual features pass through stop-gradient before the action head receives: affordance_heatmap ⊙ sg(VLM_visual_features) + proprioceptive_state. A uniform (language-ignoring) map yields unselective features and degraded performance. Unlike GuidedVLA's predefined factor-specific supervision, stop-gradient prevents task-semantic gradient from flowing through the non-affordance pathway. Unlike LangForce's action-level Bayesian decomposition, this isolates spatial affordance (WHERE) from trajectory (HOW), and the affordance readout is open-vocabulary.\n(c) Flow-Matching Action Head: Lightweight DiT generating trajectory chunks conditioned on affordance-gated visual features + proprioceptive state.\n\nTraining Objectives — Four losses forming a hierarchical structure:\n\nTier 1 — Within-Scene Language Grounding (prerequisite):\n(1) IPAC (Instruction-Paraphrase Affordance Consistency): Given same scene and K LLM-generated paraphrases, affordance maps must be consistent (KL divergence penalty on heatmaps). Unlike Shin (2026) who uses paraphrases as data augmentation (+1.71pp), IPAC uses them as regularization constraining affordance geometry.\n(2) IDA (Instruction-Discriminative Affordance): Given same scene and semantically different instructions, affordance maps must diverge (margin-based divergence loss). Prevents degenerate consistency collapse where instruction-invariant heatmaps trivially satisfy IPAC.\n\nTier 2 — Cross-Category Affordance Abstraction (core innovation):\n(3) COFC (Cross-Object Functional Consistency): Contrastive objective on affordance maps across different object categories sharing functional affordances. Positive pairs: same (action, functional_region) across different objects (e.g., \"pour from spout\" on pitcher vs. teapot — both targeting spout region). Hard negatives: same action verb but different functional regions (e.g., \"grasp handle\" vs. \"grasp body\"). Grouping leverages HOVA-500K's 675 fine-grained action categories (which encode action+part structure), or Affogato's open-vocabulary affordance labels, or instruction-parsed (verb, object_part) pairs from robot trajectory data as fallback. This operationalizes functional affordance abstraction (Gibson, 1979) as a learning signal.\n\nTier 3 — Task Grounding (standard):\n(4) AGA (Action-Grounded Affordance): Flow-matching loss for trajectory prediction through the affordance-gated bottleneck.\n\nPhased Training Schedule:\nPhase 1 — Affordance Readout Pre-training: Two co-equal experimental conditions: (A) HOVA-500K pre-training with cross-attention readout predicting contact-point Gaussian heatmaps conditioned on action-label text from 675 categories, with viewpoint augmentation for ego-centric domain gap. (B) Self-supervised initialization using pseudo-affordance Gaussians from gripper contact positions in robot trajectory data. Both reported in main results. HOVA-500K availability note: GLOVER++ (arXiv 2505.11865) announced release; if unavailable, Affogato (arXiv 2506.12009, 150K open-vocabulary affordance heatmaps) serves as alternative.\nPhase 2 — End-to-end VLA training: (2a) AGA only for 10% — establish baseline. (2b) Add IPAC at 10%. (2c) Ramp IDA and COFC over 15% via linear warmup. GradNorm (ICML 2018) provides automatic balancing across all four losses — no manual threshold-based rules.\n\nData Pipeline: Open X-Embodiment and DROID for robot trajectories; HOVA-500K (with self-supervised and Affogato alternatives) for affordance pre-training and COFC cross-object grouping; LLM-generated instruction paraphrases (Qwen3 or GPT-4) for IPAC pairs.\n\nAblation Design (10 conditions across 7 numbered variants; ≤200 H100-hour budget via seed management: 6 core × 2 seeds + 4 supplementary × 1 seed):\n(1) Full LACVLA — bottleneck + IPAC + IDA + COFC + AGA\n(2) Bottleneck analysis (merged sub-conditions, identical data/hyperparameters):\n  (a) No affordance bottleneck — direct VLA without affordance readout\n  (b) Bottleneck + AGA only — no consistency losses; tracks affordance map quality (entropy, discriminability)\n  (c) Bottleneck + AGA + IPAC only, no IDA — tests IDA necessity and consistency collapse\n  (d) Bottleneck + AGA + IDA only, no IPAC — symmetric test of IPAC necessity; if IDA-only ≈ Full, PPCL transfer hypothesis weakened\n(3) Modular — frozen GLOVER++ affordance → separate policy (end-to-end vs. modular)\n(4) Shin-style augmentation — paraphrases as training data, no consistency loss (PPCL transfer test)\n(5) IPAC on raw actions — KL divergence on action distributions under paraphrased instructions, no affordance readout (CRITICAL: SMH test. If affordance-level consistency outperforms action-level for cross-category transfer, validates spatial mediation. If comparable, spatial mediation unnecessary.)\n(6) ST4VLA-style spatial grounding + IPAC on features — spatial pre-training + consistency on VLM features without affordance readout (value of explicit affordance structure beyond spatial grounding + consistency)\n(7) Full LACVLA minus COFC — tests cross-category abstraction value beyond within-scene grounding (IPAC/IDA)\n\nEvaluation Protocol — Primary (Cross-Category Zero-Shot Transfer):\n(a) Held-out object category experiments: ≥3 independent random partition seeds, report mean ± std. Held-out categories stratified by semantic distance from training categories: \"near\" (e.g., mug → cup) vs. \"far\" (e.g., mug → scissors), reported separately to characterize transfer gradient. Minimum 5 held-out categories per partition; if LIBERO category count insufficient, AGNOSTOS serves as primary anchor.\n(b) HOVA-500K cross-category transfer: train on K action categories with one object set, test on same actions with different categories\n(c) AGNOSTOS benchmark (arXiv 2505.15660) with X-ICM (7B and 72B, open-source checkpoints) as explicit baselines\n(d) BusyBox (arXiv 2602.05441) supplementary: if physical hardware available, test on shuffled configurations\n(e) Real-world evaluation: specified platform (Franka Emika Panda or equivalent); 5+ unseen categories × 3+ primitives (grasp, pour, push); ≥20 trials per task-category pair; binary success criteria (e.g., object lifted > 5cm, liquid poured > 50%); \"unseen\" verified by exclusion search against training data confirming zero overlap; at least 1 baseline (ST4VLA or LangForce) reproduced on same setup. If resources insufficient, downgrade to qualitative demonstration + video supplement.\n\nEvaluation Protocol — Secondary:\n(f) LIBERO-Para with PRIDE metric (comparison with ST4VLA 72%/61%)\n(g) LangGap protocol (targeting improvement over 28% multi-task ceiling)\n(h) Affogato for affordance quality\n(i) Standard LIBERO (Spatial, Object, Goal, Long) for in-distribution comparison with ST4VLA (95.9% avg)\n(j) LangForce as cross-category baseline (integrated in StarVLA, low additional cost)\n(k) RoboPCA (arXiv 2603.07691) as strong modular cross-category affordance baseline (published numbers with scale annotations; reproduced if code available)\n\nEvaluation Protocol — Affordance Quality (reported across all ablation conditions, negligible compute):\n(l) Affordance IoU: heatmap peak region IoU with ground-truth contact (from HOVA-500K or robot gripper contact)\n(m) Paraphrase Consistency Score (PCS): mean pairwise KL between affordance maps under K paraphrases — quantifies IPAC effect\n(n) Instruction Discriminability Score (IDS): mean pairwise KL between affordance maps under different instructions — quantifies IDA effect\n(o) Cross-Category Affordance Transfer Score: affordance IoU on held-out categories vs. training categories\n(p) IB Diagnostic: linear probe accuracy for instruction classification (should be high) vs. category classification (should be low) on affordance features — tests information bottleneck prediction\n(q) WHERE/HOW disaggregation: all metrics reported separately for WHERE-dominant and HOW-dominant task groups\n\nCompute Fairness: Main table reports for all methods: model size (total/trainable params), training data size, approximate GPU-hours. Ablations #4, #5, #6 share LACVLA's backbone for controlled comparison. Published baselines cited with scale annotations.\n\nTarget: AAAI 2027 (abstract Jul 21, full paper Jul 28). Backup: WACV 2027 Round 2 (paper Aug 27).\n\n## Resource Estimate\n{'auto_research': {'gpu_hours': '~490-700h A100 80GB (≈350-500h H100). 10 ablation conditions × 2 seeds core / 1 seed supplementary, both pre-training paths, X-ICM/LangForce/RoboPCA baseline evaluation, full benchmark sweeps + affordance quality metrics.', 'estimated_gpu_cost': '$735-1,050', 'claude_api_cost': '$500-1,200', 'timeline': '3-4 weeks with 4+ A100 GPUs'}, 'human_in_loop': {'gpu_hours': '~250-350h A100 80GB (≈180-250h H100). 10 conditions + 2-4 hyperparameter variants, both pre-training paths.', 'estimated_gpu_cost': '$375-525', 'claude_api_cost': '$200-500', 'team': '1 researcher, ~1.5h/day', 'timeline': '6-8 weeks'}, 'manual': {'gpu_hours': '~200-290h A100 80GB (≈143-207h H100). Pre-training ~20h, Full LACVLA ~35-45h, 9 additional conditions ~108-162h, evaluation ~40h.', 'estimated_gpu_cost': '$300-435', 'team': '2 researchers', 'timeline': '8-10 weeks'}}\n\n## Key References\n- ST4VLA (ICLR 2026, arXiv 2602.10109) — strongest in-distribution baseline: 95.9% LIBERO avg, 72%/61% paraphrase robustness, 62% unseen objects\n- LangForce (arXiv 2601.15197, Jan 2026) — enforces language conditioning at action level via Bayesian decomposition; 66.5% LIBERO, +11.3% SimplerEnv OOD; integrated into StarVLA; key cross-category baseline\n- BayesVLA (arXiv 2512.11218, Dec 2025) — Bayesian factorization of VLA policy\n- LIBERO-Plus (CVPR 2026, arXiv 2510.13626) — diagnostic: VLAs ignore language, exhibit positional bias\n- LangGap (arXiv 2603.00592, Mar 2026) — augmentation ceiling: 28% multi-task\n- GuidedVLA (RSS 2026, arXiv 2605.12369, May 2026) — 3 predefined attention head factor types on π₀; 75.4% LIBERO-Plus, 90.63% RoboTwin 2.0\n- BusyBox (arXiv 2602.05441, Feb 2026) — physical affordance generalization benchmark\n- ProGAL-VLA (arXiv 2604.09824, Apr 2026) — 3D entity-centric grounding; 71.5% LIBERO-Plus robustness\n- DIAL (arXiv 2603.29844, Mar 2026) — latent intent bottleneck, architectural inspiration\n- Robo-ABC (ECCV 2024, arXiv 2401.07487) — cross-category affordance via visual correspondence; 85.7% on 7 categories\n- RoboPCA (arXiv 2603.07691, Mar 2026) — pose-centered cross-category affordance; +18.6% over MOKA on AGD20K, +38.5% RLBench\n- CoA-VLA (ICCV 2025, arXiv 2412.20451) — 4-type affordance reasoning via chain-of-thought\n- InternVLA-M1 (arXiv 2510.13778) — spatially guided VLA with affordance recognition\n- SpatialVLA (RSS 2025, arXiv 2501.15830) — Ego3D Position Encoding, Adaptive Action Grids\n- Spatial Forcing (ICLR 2026, arXiv 2510.12276) — implicit spatial alignment without 3D input\n- FocusVLA (arXiv 2603.28740, Mar 2026) — visual utilization via Modality Cascaded Attention; attention-mechanism approach vs. LACVLA's information-bottleneck approach\n- Bi-Adapt (arXiv 2602.08425, Feb 2026) — cross-category bimanual affordance mapping via vision foundation model correspondence\n- AGNOSTOS / X-ICM (arXiv 2505.15660) — cross-task zero-shot benchmark; X-ICM 72B: 30.1%\n- LIBERO-Para (arXiv 2603.28301, Mar 2026) — paraphrase robustness with PRIDE metric\n- Shin (arXiv 2603.16044, Mar 2026) — augmentation baseline, +1.71pp\n- Stable Language Guidance (ACL 2026, arXiv 2601.04052) — inference-time modality collapse mitigation\n- Attention Recalibration (arXiv 2603.06001, Mar 2026) — train-free attention sink fix\n- PPCL (EACL 2024, arXiv 2402.15833) — consistency > augmentation in NLP\n- Flip-Flop Consistency (arXiv 2510.14242, Oct 2025) — extends PPCL to LLMs\n- OpenVLA (CoRL 2024) — base VLA architecture\n- StarVLA (arXiv 2604.05014, Apr 2026) — implementation framework (includes LangForce)\n- GLOVER++ (CoRL 2025, arXiv 2505.11865) — HOVA-500K dataset, modular baseline\n- PokéVLA (arXiv 2604.20834, Apr 2026) — validates HOVA-500K ego→VLA transfer\n- RT-Affordance (arXiv 2411.02704, 2024) — modular affordance baseline\n- A0 (ICCV 2025, arXiv 2504.12636) — hierarchical affordance, zero-shot transfer, no language\n- RoboMAP (arXiv 2510.10912, 2025) — modular language-conditioned affordance heatmap\n- AffordDP (CVPR 2025) — cross-category transfer via 3D contact points\n- RAM (CoRL 2024, arXiv 2407.04689) — retrieval-based affordance\n- RAAP (arXiv 2603.29419, Mar 2026) — cross-image affordance alignment\n- UAD (ICRA 2025) — modular affordance pipeline\n- VLA² (arXiv 2510.14902) — agentic retrieval for unseen concepts\n- Affogato (arXiv 2506.12009, 2025) — affordance quality benchmark; 150K instances, alternative pre-training source\n- AffordSim (arXiv 2604.11674, 2026) — simulation evaluation resource\n- GradNorm (ICML 2018) — multi-task loss balancing\n- LAP (RSS 2026, arXiv 2602.10556) — cross-embodiment zero-shot via language-action alignment",
4	  "中稿概率": "[24.0% - 34.0%] 中位 29.0%",
5	  "优化方案": "【优化方案】\n\n## A. 核心立意与 Novelty 重新定位（最高优先级）\n\n1. **Core Problem / 全文定位** — 将核心贡献从\"first to architecturally enforce language conditioning in VLAs\"重新定位为\"affordance-level consistency as a self-supervised grounding signal for cross-category transfer\"。原始 claim 被 LangForce (arXiv 2601.15197, Jan 2026, 已集成于 StarVLA) 和 BayesVLA (arXiv 2512.11218, Dec 2025) 直接覆盖——二者已在 action level 实现了 architectural enforcement of language conditioning。重新定位后的核心差异化：LangForce 在 action level 操作（WHERE+HOW 混合），LACVLA 在 affordance level 操作（仅 WHERE），且通过 self-supervised consistency objectives 而非 likelihood-ratio optimization。 — **命中 Novelty（从\"被覆盖\"转为\"不可替代\"）+ Related Work（消除最大遗漏）**\n\n2. **Description / 新增 Spatial Mediation Hypothesis (SMH)** — 提出可证伪的科学假说：\"语言通过空间 affordance (WHERE) 中介控制操作行为，在此层面的 consistency regularization 优于 conflated action level (WHERE+HOW) 的 consistency\"。将 ablation #5 (IPAC on raw actions vs. affordance maps) 定义为 SMH 的核心检验——正负结果均有科学价值。将论文从\"engineering a better VLA\"提升为\"testing a hypothesis about the computational structure of language-conditioned manipulation\"。 — **命中 Significance（从\"工程贡献\"升级为\"科学发现\"）+ Novelty（假说本身是独创贡献）**\n\n3. **Description / 新增 Information Bottleneck 理论基础** — 用 IB principle (Tishby et al., 2000) 为 SMH 提供理论动机：cross-category transfer 的最优 instruction-conditioned 表征应压缩 category-specific 视觉细节（HOW），保留 category-invariant 空间语义（WHERE）。Stop-gradient bottleneck 是 IB principle 的架构实例化。定位为\"motivated by\"而非\"derived from\"IB，避免 reviewer 要求完整推导。新增可量化 IB 诊断：I(affordance; instruction) 应高、I(affordance; category_identity) 应低，通过 linear probe 近似（零额外计算）。 — **命中 Significance（理论深度）+ Technical Soundness（可量化预测）**\n\n4. **Description / SMH 适用范围显式限定** — 声明 SMH 针对 WHERE-dominant tasks（handle grasping, surface pushing, rim pouring）。承认 HOW-dominant tasks（\"gently place\" vs. \"drop\"）在当前 stop-gradient 设计下的局限——HOW-semantic 语言差异无法传递到 action head。提供操作性分类标准（oracle contact point + default trajectory 成功率阈值）、双标注者 inter-annotator agreement、WHERE/HOW/Mixed 三类分组。所有 metrics 按分组报告。讨论 low-dim style vector 扩展为 future work。 — **命中 Significance（bounded claim 比 sweeping claim 更可信）+ Technical Soundness（可验证的 scope）**\n\n5. **Description / WHERE/HOW 分离的 nuanced framing** — 从过度简化的\"WHERE only\"修正为\"controlled information leakage\"：stop-gradient 阻止 category-specific visual texture/identity 泄漏，但 heatmap geometry 隐式编码的 residual HOW 信息（grasp orientation, pour trajectory 起始几何）保留并有益。比 clean separation claim 更诚实且更具防御性。 — **命中 Novelty（更精确的 claim 更难被攻击）**\n\n## B. Related Work 扩展（防御性关键）\n\n6. **Landscape (5) / 新增 LangForce + BayesVLA** — 扩展 lineage (5) 为\"Architectural bottleneck enforcement for language conditioning\"，纳入 LangForce (arXiv 2601.15197) 和 BayesVLA (arXiv 2512.11218)。显式对比：二者在 action level 操作（WHERE+HOW 混合），LACVLA 在 affordance level 操作（WHERE only）+ self-supervised consistency。不纳入将导致 novelty claim 被直接击穿。 — **命中 Related Work（消除致命遗漏）+ Novelty（差异化防线）**\n\n7. **Landscape (4) / 新增 Robo-ABC + RoboPCA** — Robo-ABC (ECCV 2024, arXiv 2401.07487, 85.7% on 7 categories) 挑战\"language is the ONLY guide\"前提；RoboPCA (arXiv 2603.07691, +18.6% over MOKA) 为更强的 modular cross-category baseline。前提软化为\"language is the most general guide when visual analogues are unavailable\"。 — **命中 Related Work + Significance（前提更 robust）**\n\n8. **Landscape (2) / 新增 CoA-VLA** — CoA-VLA (ICCV 2025, arXiv 2412.20451) 用 chain-of-affordance 推理 4 种 affordance types。定位为\"explicit affordance reasoning via language generation vs. LACVLA's spatial heatmap consistency\"——不同机制。 — **命中 Related Work（谱系完整性）**\n\n9. **Landscape (3)(5) / 新增 AntiGrounding + FocusVLA + RS-CL + SA-VLA** — AntiGrounding (arXiv 2506.12374) 是 stop-gradient bottleneck 的直接理论反驳，必须主动 engage：bottleneck 在 in-distribution 下代价可能 > 收益，但在 cross-category transfer 下是 IB principle 的 feature。FocusVLA (arXiv 2603.28740) 为\"attention-mechanism vs. information-bottleneck\"对比路线。RS-CL (arXiv 2510.01711) 正则化 proprioceptive state 而非 spatial affordance。SA-VLA (arXiv 2602.00743) 通过 RL reward 维持 spatial grounding。 — **命中 Related Work（防御性加固，堵住\"missed recent work\"攻击面）**\n\n10. **Landscape / 新增 Bi-Adapt** — Bi-Adapt (arXiv 2602.08425) 展示 cross-category affordance transfer 为 active research direction，强化 significance framing。 — **命中 Significance（时效性验证）**\n\n11. **Gap Statement 重写** — 原始 gap: \"No existing work combines (a) architectural enforcement... (b) self-supervised consistency... (c) cross-category zero-shot transfer\"。LangForce 的存在使 (a) 不再唯一。新 gap 增加限定：\"at the spatial affordance level\"并增加\"with hierarchical loss structure (within-scene grounding + cross-category abstraction)\"。 — **命中 Novelty（gap 更精确更难被替代方案填充）**\n\n## C. Training Objectives 重设计\n\n12. **Approach / COFC 正式化为第 4 个 loss** — 原始 proposal 中\"Cross-Object Functional Consistency via HOVA-500K\"未编号、未指定 weight schedule、未纳入 ablation。现正式编为 COFC loss，指定 Phase 2c 引入（与 IDA 同步），新增 ablation #7 (Full minus COFC)。 — **命中 Technical Soundness（消除 claim-without-evidence 缺口）**\n\n13. **Approach / COFC 从 KL penalty 重设计为 contrastive objective** — 原始 KL penalty 对粗粒度 action label 分组有设计缺陷：\"grasp mug handle\"和\"grasp ball surface\"的 affordance map 合理不同，KL penalty 产生错误梯度信号。重设计为 contrastive objective：同 (action, functional_region) 跨不同物体为正样本对，同 action 但不同 functional_region 为硬负样本。利用 HOVA-500K 的 675 细粒度 categories 或 instruction-parsed (verb, object_part) 对。 — **命中 Technical Soundness（修复核心 loss 设计缺陷）**\n\n14. **Approach / COFC 叙事提升为 loss 层级核心** — 建立 Tier 结构：Tier 1 (IPAC+IDA) = within-scene language grounding（前提条件）→ Tier 2 (COFC) = cross-category affordance abstraction（核心创新，连接 Gibson 1979 功能性 affordance 理论）→ Tier 3 (AGA) = task grounding（标准目标）。COFC 从\"四个 loss 之一\"提升为\"对跨类别迁移最直接的贡献\"。 — **命中 Significance（核心创新清晰可识别）+ Novelty（叙事锐化）**\n\n15. **Approach / COFC 数据依赖链强化** — 原始仅依赖 HOVA-500K（可用性不确认）。构建 triple fallback：HOVA-500K → Affogato (arXiv 2506.12009, 150K instances, 注意已从 ICLR 2026 撤稿需确认数据可用性) → VLM auto-annotation pipeline（用 Qwen2-VL 对 robot trajectory frames 生成 open-vocabulary affordance part labels）。报告 COFC grouping 统计（positive pairs 数量、category 覆盖、pair 内 diversity）。 — **命中 Feasibility（降低单点失败风险）**\n\n16. **Approach / PPCL 迁移从\"已知原则应用\"转为\"可验证假说\"** — 原始将 PPCL 的 NLP 发现直接类比到 spatial heatmap。修正为 testable hypothesis：NLP embedding 到 spatially structured heatmap 的域迁移是 non-trivial 的（spatial structure、sharp boundaries、paraphrase 的 subtle semantic 差异可能映射到不同空间区域）。ablation #4 (Shin-style augmentation) vs. Full LACVLA 直接检验。 — **命中 Significance（假说本身是贡献）+ Technical Soundness（诚实性）**\n\n## D. Training 流程简化\n\n17. **Approach / Phase 2c 去掉 rule-based 动态调权** — 原始包含手动阈值 (\"if H(A) < 0.3 × H_max, increase IDA weight by 50%\"、\"if D < 0.5, halt IPAC and boost IDA\")。这些阈值本身是未验证的超参数，与 GradNorm 叠加可能冲突。简化为 GradNorm-only 自动平衡四个 loss。设 minimum weight floor (0.05) 防止任何 loss 被完全压制。报告 GradNorm 学到的 weight 演变曲线（appendix）。 — **命中 Technical Soundness（减少超参数 + 减少 reviewer 攻击面）**\n\n## E. Ablation 扩展\n\n18. **Ablation / 新增 #2c: Bottleneck + AGA + IPAC only, no IDA** — 原始 6 variants 中无法验证 IDA 的必要性。新增后，对比 Full vs. 2c 测试 IDA 是否阻止 consistency collapse；对比 2c vs. 2b 测试 IPAC alone 的效果。 — **命中 Technical Soundness（填补 claim-evidence 缺口）**\n\n19. **Ablation / 新增 #2d: Bottleneck + AGA + IDA only, no IPAC** — 对称测试 IPAC 的贡献。如果 IDA-only ≈ Full，则 PPCL transfer 假说被削弱——这是重要的诊断信息。 — **命中 Technical Soundness（symmetric ablation 要求）**\n\n20. **Ablation / 新增 #7: Full LACVLA minus COFC** — 测试 cross-category abstraction 是否在 within-scene grounding (IPAC+IDA) 基础上增加价值。如果 COFC 贡献显著，直接验证 Tier 2 核心创新地位。 — **命中 Technical Soundness（核心创新可验证性）**\n\n21. **Ablation #5 reframing** — 从技术对比 (\"tests whether isolating WHERE outperforms consistency on conflated actions\") 重新定义为 SMH 的核心科学检验。正负结果均有价值——如果 raw action consistency ≈ affordance consistency，则 spatial mediation assumption 不成立，这本身是有价值的 null result。 — **命中 Significance（提升 ablation 的科学意义）**\n\n## F. Evaluation Protocol 强化\n\n22. **Primary Evaluation / X-ICM 作为 AGNOSTOS 显式 baseline** — 原始在 AGNOSTOS 上评测但未指定 baseline。新增 X-ICM 7B (scale-matched, 23.5%) 作为主要对比点，X-ICM 72B (30.1%) 加 scale annotation (10× larger)。报告 efficiency curve (success vs. model size)。 — **命中 Technical Soundness（结果可解读性）**\n\n23. **Primary Evaluation / Held-out partition 方法论** — 原始仅说\"partition into train/test\"。新增：≥3 independent random partition seeds，report mean ± std；按语义距离分层（near vs. far categories）展示 transfer gradient。如 LIBERO category 不足，AGNOSTOS 作为 anchor。 — **命中 Technical Soundness（统计严谨性）**\n\n24. **Primary Evaluation / Real-world protocol 规范化** — 原始仅说\"5+ unseen categories, 3+ primitives\"。新增：指定平台 (Franka Emika Panda 或等价)；≥20 trials/condition；binary success criteria (object lifted > 5cm, liquid poured > 50%)；\"unseen\"通过 exclusion search 确认 zero overlap；至少 1 baseline 同 setup 复现；不足则降级为 qualitative + video supplement。 — **命中 Technical Soundness（评估可信度）**\n\n25. **Secondary Evaluation / 新增 GuidedVLA baseline + LIBERO-PRO benchmark** — GuidedVLA (RSS 2026, 75.4% LIBERO-Plus) 是最直接的 architectural-level 对比——同为\"中间表征层 grounding supervision\"。LIBERO-PRO (arXiv 2510.03827) 测试 genuine understanding vs. memorization，直接验证 LACVLA 的 grounding claim。 — **命中 Technical Soundness（baseline 完备性 + benchmark 覆盖）**\n\n26. **Secondary Evaluation / LangForce 作为 cross-category baseline** — LangForce 已集成于 StarVLA（LACVLA 的实现框架），evaluation 成本极低。如 LACVLA 在 cross-category transfer 上优于 LangForce，直接验证 affordance-level > action-level 的 SMH 预测。 — **命中 Technical Soundness（最关键的 head-to-head 对比）**\n\n27. **新增 Affordance Quality 评估指标组** — 原始仅以 task success rate 评估。新增 5 项 affordance-level 直接指标：(a) Affordance IoU (heatmap peak vs. contact region)；(b) PCS (paraphrase consistency score)；(c) IDS (instruction discriminability score)；(d) Cross-Category Affordance Transfer Score；(e) IB Diagnostic (linear probe: instruction classification 应高, category classification 应低)。计算成本 negligible，但为 core claim (\"affordance-level consistency\") 提供不可或缺的直接证据——仅靠 task success rate 无法排除 confounding factors。 — **命中 Technical Soundness（core claim 的直接证据链）**\n\n28. **Compute Fairness / 新增报告要求** — Main table 报告 model size (total/trainable params)、training data size、approximate GPU-hours。Ablations #4/#5/#6 共享 backbone 保证控制变量。Published baselines 引用原始数字 + scale annotation。 — **命中 Technical Soundness（排除 compute 混淆因子）**\n\n## G. HOVA-500K 风险缓解\n\n29. **Phase 1 / Self-supervised fallback 升级为 co-equal experimental condition** — 原始将 self-supervised path 定位为 Plan B。升级为与 HOVA-500K 并列的 first-class condition——main results 报告两个版本，ablation 确定 HOVA-500K 是否必要。消除 HOVA-500K 作为单点失败风险。 — **命中 Feasibility（de-risk）+ Technical Soundness（增加 ablation 信息量）**\n\n---\n\n【主要风险】（reviewer 最可能攻击的方向）:\n\n1. **Ablation #5 的结果决定论文生死**：SMH 的核心检验——如果 IPAC on raw actions 与 affordance-level consistency 效果相当，则 stop-gradient bottleneck 和整个 affordance readout 被证明是不必要的 overhead，论文的核心贡献（\"WHERE 层面的 consistency 优于 action 层面\"）不成立。虽然 proposal 将此 framing 为\"both outcomes are scientifically informative\"，但 reviewer 可能不买账——一个 null result 在 top venue 的接受率远低于 positive result。缓解：确保 affordance-level metrics (PCS, IDS, Cross-Cat Transfer Score) 即使在 task success 相当时仍能展示 affordance 质量的差异（即使下游 success 类似，affordance map 可能更 interpretable/consistent），增加 null result 的可发表性。\n\n2. **COFC 数据可用性的三重依赖链**：HOVA-500K 可用性未确认，Affogato 已从 ICLR 2026 撤稿（数据状态不明），VLM auto-annotation pipeline 未经验证。如果三个来源都不可用或质量不足，COFC——被定位为\"核心创新 Tier 2 loss\"——将无法实施，论文降级为仅有 IPAC+IDA 的 within-scene grounding 工作，丧失 cross-category 独创性。缓解：在实验开始前（第 1 周）完成数据可用性验证，如三个来源均失败则需根本性调整 COFC 设计或降低其在叙事中的地位。\n\n---\n\n【实施评估】:\n\n- **计算资源**: 4-8× A100 80GB（或等价 H100）集群。训练阶段核心需求：Full LACVLA 1 次 ~35-45h A100 (4-GPU parallel)；9 个 ablation/baseline conditions，6 core × 2 seeds + 4 supplementary × 1 seed = 16 runs × ~12-18h A100 each = ~192-288h A100；affordance readout pre-training ~20h A100（HOVA-500K path）或 ~8h（self-supervised path）；X-ICM / LangForce / RoboPCA baseline evaluation ~10h total (inference only)。总计 ~200-290h A100（manual 模式）至 ~490-700h A100（auto_research 含超参搜索），≈143-500h H100。估算 GPU 租赁成本 $300-1,050。\n\n- **数据需求**: (1) Open X-Embodiment + DROID：公开可得，已有成熟下载管线。(2) HOVA-500K：需联系 GLOVER++ (CoRL 2025) 作者确认可用性——这是启动前的 blocking dependency。(3) Affogato 数据集：已从 ICLR 2026 撤稿，需独立确认数据是否仍可下载。(4) AGNOSTOS / LIBERO / LIBERO-Plus / LIBERO-Para / LIBERO-PRO：公开可得。(5) LLM-generated paraphrases：Qwen3 或 GPT-4 生成，成本 negligible。(6) BusyBox：需物理硬件（如 available）。所有仿真 benchmark 均公开。\n\n- **人工介入**: (1) 启动配置 ~6-8 小时（dataset access 确认、paraphrase generation、HOVA-500K/self-supervised preprocessing、benchmark environment setup、cross-category split 定义）。(2) WHERE/HOW task 分类标注：2 名标注者独立分类 AGNOSTOS 23 tasks + LIBERO tasks + real-world tasks，估计 ~4-6 人时总计（含 inter-annotator agreement 计算）。(3) Real-world 实验若执行：需 robot operator ~20-40 小时（5+ categories × 3+ primitives × 20+ trials = 300+ trials）。(4) Human-in-loop 模式下 1 researcher ~1.5h/day review，涵盖 domain gap 诊断、affordance map 质量检查、cross-category split 审批。\n\n- **训练需求**: 需要模型训练。Base VLM: Qwen2-VL-4B（~4B params），LoRA fine-tuning（trainable params ~50-100M）。Affordance readout: <5M params, 从零训练。Flow-matching action head (DiT): ~50-100M params。总 trainable ≈ 100-200M。Full training (Phase 1 + Phase 2): 每次 ~35-45h on 4× A100。不需要从零训练 VLM——LoRA + frozen backbone。\n\n- **新 Benchmark**: 不需要构建全新 benchmark。需要构建的评估 setup：(1) LIBERO/DROID cross-category held-out splits（工程工作，非新 benchmark，~1 天）；(2) HOVA-500K cross-category transfer test splits（利用 675 action categories 已有结构，~0.5 天）；(3) WHERE/HOW task 分类标签（标注工作，~1 天）。所有评估 benchmark（LIBERO, LIBERO-Plus, LIBERO-Para, LIBERO-PRO, AGNOSTOS, Affogato, BusyBox）均为现有公开 benchmark。\n\n- **预估周期**: \n  - **Auto-research 模式**: 3-4 周（4+ A100 concurrent），前提：HOVA-500K 在第 1 周确认可用。\n  - **Human-in-loop 模式**: 6-8 周（1 researcher, 1.5h/day），bottleneck: affordance pre-training → domain gap diagnostic → phased training → cross-category evaluation。\n  - **Manual 模式**: 8-10 周（2 researchers），包含 1-2 周 data pipeline + pre-training，4-5 weeks 实验迭代（含 10 ablation conditions），2-3 weeks 评估 + 写作。\n  - **关键路径**: Week 1: 确认 HOVA-500K/Affogato 可用性（blocking）→ Week 2-3: affordance readout pre-training (两条 path 并行) → Week 3-6: phased VLA training + ablation sweep → Week 6-8: evaluation + 论文撰写。\n  - **目标投稿**: AAAI 2027（abstract Jul 21, full paper Jul 28 — 距今约 63 天）。Timeline tight but feasible in auto-research or human-in-loop mode。Backup: WACV 2027 Round 2 (paper Aug 27 — 100 天)。",
6	  "verdict": "FAILED_below_33",
7	  "概率对比": {
8	    "X_初始_triple_consensus": "28.0%",
9	    "X_区间": "[24.0%, 32.0%]",
10	    "Y_循环终审自评": "41.0%",
11	    "Z_独立出口_triple_consensus": "29.0%",
12	    "Z_区间": "[24.0%, 34.0%]",
13	    "真实提升_Z减X": "+1.0 pp",
14	    "幻觉幅度_Y减Z": "+12.0 pp",
15	    "过30门槛": false,
16	    "exit_consistency": "高",
17	    "exit_three_mids": [
18	      28.0,
19	      30.0,
20	      30.0
21	    ],
22	    "entry_three_mids": [
23	      28.0,
24	      28.0,
25	      28.0
26	    ],
27	    "entry_consistency": "高（三份评审中位完全一致，std=0%；区间高度重叠 [23-33]/[24-33]/[25-33]；所有 rubric 维度判决完全一致；核心风险识别高度重合）"
28	  },
29	  "entry_triple_consensus": {
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61ceba84-66c0-4a9f-a499-c71405b2aaf5",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "5bcdafd4-b92f-4a53-a03d-dd4bcddd84cf",
  "sourceToolAssistantUUID": "61ceba84-66c0-4a9f-a499-c71405b2aaf5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-27T18:44:13.915Z_

Now I have a good understanding of the JSON format. This is a different research idea though - the user is asking about TTRA (autoformalization), not LACVLA (VLA manipulation). Let me search for any existing TTRA-related content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bcdafd4-b92f-4a53-a03d-dd4bcddd84cf",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZsrjedXcGFY29QUH8X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e4eb866-48a2-46d4-bd43-8f92cf794d61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuVpgNVRXtaug5Xobc6pHK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24437,
      "cache_read_input_tokens": 23099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24437,
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

_source line 34 · 2026-05-27T18:44:15.213Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01ScvTX5eoDbRu1TS35J7pts`</summary>

```json
{
  "pattern": "autoformali|TTRA|CriticLean|FormaRL|GRPO|Lean 4",
  "path": "/home/ubuntu/idea_review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e4eb866-48a2-46d4-bd43-8f92cf794d61",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZsrjedXcGFY29QUH8X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed03ed0b-c9d7-4e94-9144-443c187205ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuVpgNVRXtaug5Xobc6pHK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24437,
      "cache_read_input_tokens": 23099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24437,
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

_source line 35 · 2026-05-27T18:44:15.265Z_

<details><summary>↩ Tool result · `toolu_01ScvTX5eoDbRu1TS35J7pts`</summary>

```text
Found 31 files
dispatch/results_batch6_20260520_025525/account-3/result_synthetic_data_anchor_decomposed_verifier_disagreement_as_an_informativenes.json
dispatch/ideas_batch7_20260520_032225/account-3/synthetic_data_anchor_decomposed_verifier_disagreement_as_an_informativenes.md
dispatch/results_batch5_20260519_204518/account-3/result_self_correction_fact_blind_spot.json
dispatch/ideas_batch5_20260519_204518/account-3/self_correction_fact_blind_spot.md
dispatch/results_batch5_20260519_183057/account-3/result_self_correction_fact_blind_spot.json
dispatch/results_batch5_20260519_183057/account-3/trace_self_correction_fact_blind_spot/trace.md
dispatch/results_batch5_20260519_183057/account-3/trace_self_correction_fact_blind_spot/trace.json
dispatch/ideas_batch5_20260519_183057/account-3/self_correction_fact_blind_spot.md
dispatch/results_rerun/result_idea_014_s3_contrastive_prosody_discriminator_with_i.json
dispatch/results_rerun/trace_idea_014_s3_contrastive_prosody_discriminator_with_i/trace.md
dispatch/results_rerun/trace_idea_014_s3_contrastive_prosody_discriminator_with_i/trace.json
dispatch/ideas_rerun/idea_014_s3_contrastive_prosody_discriminator_with_i.json
dispatch/results_stage23/result_idea_014_s3_contrastive_prosody_discriminator_with_i.json
dispatch/results_stage23/trace_idea_014_s3_contrastive_prosody_discriminator_with_i/trace.md
dispatch/results_stage23/trace_idea_014_s3_contrastive_prosody_discriminator_with_i/trace.json
dispatch/ideas_stage23/idea_014_s3_contrastive_prosody_discriminator_with_i.json
dispatch/results_0517_s3/result_idea_015_s3_constrained_prosodic_diversity_optimizat.json
dispatch/ideas_0517_s3/idea_015_s3_constrained_prosodic_diversity_optimizat.json
dispatch/results_0517/result_idea_015_s4_direction_gated_reward_shaping_for_warra.json
dispatch/ideas_0517/idea_015_s4_direction_gated_reward_shaping_for_warra.json
dispatch/results_batch_20260516_pass25/account-2/result_02_vermux_learning_to_route_reasoning_steps_to_hetero.json
dispatch/results_batch_20260516_pass25/account-2/trace_02_vermux_learning_to_route_reasoning_steps_to_hetero/trace.md
dispatch/results_batch_20260516_pass25/account-2/trace_02_vermux_learning_to_route_reasoning_steps_to_hetero/trace.json
dispatch/ideas_batch_20260516_pass25/account-2/02_vermux_learning_to_route_reasoning_steps_to_hetero.md
dispatch/results_batch_20260516_pm/account-3/result_15_encoguard_encoding-complexity_curriculum_for_hardening_guard.json
dispatch/results_batch_20260516_pm/account-1/result_01_step-level_faithfulness-gated_rejection_decoding_with_comput.json
dispatch/results_batch_20260516_pm/account-3/result_03_complexity-conditioned_cost_penalties_for_proactive_retrieva.json
dispatch/ideas_batch_20260516_pm/account-3/15_encoguard_encoding-complexity_curriculum_for_hardening_guard.md
dispatch/ideas_batch_20260516_pm/account-3/03_complexity-conditioned_cost_penalties_for_proactive_retrieva.md
dispatch/results_batch_20260516_014736/account-1/result_04_vermux_learning_to_route_reasoning_steps_to_heterogeneous_ve.json
dispatch/ideas_batch_20260516_014736/account-1/04_vermux_learning_to_route_reasoning_steps_to_heterogeneous_ve.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed03ed0b-c9d7-4e94-9144-443c187205ab",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "ffe0c4cd-9de0-4eea-a162-038f45389386",
  "sourceToolAssistantUUID": "ed03ed0b-c9d7-4e94-9144-443c187205ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-27T18:44:18.882Z_

There's no existing TTRA file in this repo. The user is asking me to create the complete revised JSON from scratch based on the detailed context they provided. Let me also look at the reviewer.py to understand what fields are expected.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffe0c4cd-9de0-4eea-a162-038f45389386",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZtGSB3yWGNxZTQw2Rk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "280cc980-bfcc-4d3e-92e2-b8701e7ac86d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSC6YLBwB2mtCfpdSCMPGg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1292,
      "cache_read_input_tokens": 47536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1292,
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

_source line 37 · 2026-05-27T18:44:19.573Z_

<details open><summary>🔧 Tool call — Read · `toolu_013ja8XWg4hU4nBcM5n3APjt`</summary>

```json
{
  "file_path": "/home/ubuntu/idea_review/reviewer.py",
  "offset": 0,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "280cc980-bfcc-4d3e-92e2-b8701e7ac86d",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZtGSB3yWGNxZTQw2Rk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f3d7e29-1217-45bf-833d-d78f360fc416",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSC6YLBwB2mtCfpdSCMPGg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1292,
      "cache_read_input_tokens": 47536,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1292
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 47536,
          "cache_creation_input_tokens": 1292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1292,
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

_source line 38 · 2026-05-27T18:44:19.594Z_

<details><summary>↩ Tool result · `toolu_013ja8XWg4hU4nBcM5n3APjt`</summary>

````text
0	"""ProposalReviewer：系统核心编排类（Claude Agent SDK）"""
1	
2	from __future__ import annotations
3	
4	import asyncio
5	import json
6	import re
7	from datetime import datetime
8	from pathlib import Path
9	
10	from claude_agent_sdk import ClaudeAgentOptions, query
11	
12	from config import (
13	    ENABLE_WEB_SEARCH,
14	    FINAL_DELIVERY_THRESHOLD,
15	    MAX_ROUNDS,
16	    MODEL_NAME,
17	    get_api_semaphore,
18	)
19	from convergence import check_convergence, check_stop_loss
20	from parsers import (
21	    excavator_converged,
22	    is_triage_kill,
23	    parse_terminal_output,
24	    parse_worker_status,
25	    rescuer_converged,
26	    rescuer_found_fatal,
27	)
28	from prompts.excavator import EXCAVATOR_SYSTEM
29	from prompts.rescuer import RESCUER_SYSTEM
30	from prompts.terminal import TERMINAL_SYSTEM
31	
32	
33	def _extract_result_text(msg) -> str | None:
34	    """从 ResultMessage（流末尾）里提取最终文本。
35	
36	    SDK 不同版本字段名可能略有差异（result / content 等），这里兜底多试几个。
37	    """
38	    if type(msg).__name__ != "ResultMessage":
39	        return None
40	    for attr in ("result", "content", "text"):
41	        val = getattr(msg, attr, None)
42	        if isinstance(val, str) and val:
43	            return val
44	    return None
45	
46	
47	def _fence_safe(text: str) -> str:
48	    """Markdown code fence：若原文里包含 ```，就用更长的围栏避开冲突。"""
49	    max_ticks = 0
50	    for line in text.splitlines():
51	        stripped = line.lstrip()
52	        if stripped.startswith("```"):
53	            n = len(stripped) - len(stripped.lstrip("`"))
54	            if n > max_ticks:
55	                max_ticks = n
56	    fence = "`" * max(3, max_ticks + 1)
57	    return f"{fence}\n{text}\n{fence}"
58	
59	
60	def _render_trace_md(meta: dict, steps: list) -> str:
61	    """把 trace 元数据 + 步骤数组渲染成 markdown（给人眼看的视图）。"""
62	    out: list[str] = []
63	    out.append(f"# Trace — {meta.get('title') or '(no title)'}")
64	    out.append("")
65	    out.append("## Meta")
66	    for k, v in meta.items():
67	        out.append(f"- **{k}**: `{v}`")
68	    out.append("")
69	    out.append(f"**Total steps**: {len(steps)}")
70	    out.append("\n---\n")
71	
72	    out.append("## Index\n")
73	    out.append("| idx | stage | role | summary |")
74	    out.append("|-----|-------|------|---------|")
75	    for s in steps:
76	        p = s.get("parsed") or {}
77	        if "decision" in p:
78	            summary = f"决策={p.get('decision')} mid={p.get('probability_mid')}%"
79	        elif "status" in p:
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f3d7e29-1217-45bf-833d-d78f360fc416",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "7691bc55-9e37-437f-ba8d-1198f5036687",
  "sourceToolAssistantUUID": "3f3d7e29-1217-45bf-833d-d78f360fc416",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-27T18:44:23.568Z_

Now I have enough context. The user wants a complete JSON for the TTRA research idea revision. Let me construct it based on all the detailed instructions provided. This is about autoformalization (translating math to Lean 4), not the LACVLA robotics paper I was reading.

Let me write the complete JSON:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7691bc55-9e37-437f-ba8d-1198f5036687",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZtaqiAT1oDxCzmx56f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f60b27a-824d-4e29-a7f4-a87060b501d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SXKrJSPjG3JDdh3BHnsq8k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 48828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1136,
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

_source line 40 · 2026-05-27T18:47:07.438Z_

<details open><summary>🔧 Tool call — Write · `toolu_01E2XUHpp4so8pt1T1n26yjx`</summary>

```json
{
  "file_path": "/home/ubuntu/idea_review/ttra_critic_guided_r4.json",
  "content": "{\n  \"title\": \"TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization\",\n  \"core_problem\": \"How can autoformalization systems adapt at test time to out-of-distribution (OOD) mathematical domains — such as competition mathematics, advanced algebra, or niche subfields — without any labeled (informal, formal) pairs, given that (1) current autoformalization models trained on in-distribution data (e.g., undergraduate-level number theory) suffer severe performance drops on OOD domains where Mathlib dependency patterns, notation conventions, and proof structures differ substantially, (2) compilation-only reward signals are necessary but insufficient for semantic correctness (a formalization can compile but express the wrong theorem), and (3) retrieval of relevant Mathlib dependencies is critical for OOD domains where the model has not memorized the needed imports, yet static retrieval indices become stale as the formalizer's behavior shifts during adaptation?\",\n  \"opportunity\": \"Autoformalization — translating informal mathematical statements into formally verified Lean 4 code — has seen rapid progress through reinforcement learning. FormaRL demonstrated that GRPO with compilation-based rewards can significantly improve formalization rates. Online Reinforcement Learning for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) showed GRPO with composite rewards (BEq + embedding-based similarity) achieving TC1: 17.29% to 26.01% and TC50: 76.41% to 85.46% on RLMEval, validating RL for autoformalization. However, these approaches operate at training time with labeled or semi-labeled data on in-distribution problems. The key bottleneck for deployment is OOD generalization: when faced with mathematical domains not well-represented in training (competition math from Con-NF, advanced algebraic topology, niche combinatorics), formalization rates collapse because (a) the model lacks familiarity with domain-specific Mathlib dependencies and idioms, (b) static retrieval indices fail to surface the right lemmas for unfamiliar problem structures, and (c) compilation alone cannot verify semantic fidelity. CriticLean (14B parameters, 84.8% accuracy on semantic correctness judgments) provides a learned reward signal that goes beyond compilation to assess whether a formalization faithfully captures the informal statement's meaning — but it has not been integrated into an RL loop. The DDRL framework (Debiased and Denoised RL) addresses reward noise and sampling bias in GRPO through frequency-based filtering and fixed advantages, but assumes binary correct/incorrect rewards, not the multi-tier reward structure (compilation + critic + BEq consensus) needed for autoformalization. Meanwhile, recent advances in retrieval-augmented generation show that retriever and generator can be co-adapted: R3 (NeurIPS 2025) uses RAG environment feedback for contrastive retriever training, Reinforced-IR (ACL 2025) alternates RLRF/RLGF for mutual retriever-generator adaptation, and TTARAG (Jan 2026) adapts models at test time using self-supervised retrieval prediction. The opportunity: combine test-time RL adaptation (GRPO/DDRL) with a semantic critic reward (CriticLean) and co-adaptive retrieval (dense retriever fine-tuned via compilation error signals) to enable domain adaptation on fully unlabeled OOD mathematical problems, without any human-annotated formal statements.\",\n  \"landscape\": \"The autoformalization and test-time RL landscape has five relevant lineages. (1) RL for autoformalization: FormaRL applies GRPO with compilation-based rewards to improve formalization in Lean 4. Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) uses GRPO with composite rewards (BEq + embedding similarity) achieving strong results on RLMEval (TC1: 17.29% to 26.01%, TC50: 76.41% to 85.46%), but operates at training time with labeled/unlabeled data on in-distribution problems. Neither incorporates a trained semantic critic, co-adaptive retrieval, or test-time adaptation on OOD domains. (2) Semantic critics for formalization: CriticLean-14B achieves 84.8% accuracy on judging semantic correctness of formalizations, trained on synthetic paired data. It provides the key signal beyond compilation — a formalization can compile but misstate the theorem — but has not been used as an RL reward signal. (3) Debiased RL: DDRL (Debiased and Denoised RL) addresses GRPO's amplification of noisy rewards through frequency-based balanced sampling, fixed advantages (+1/-1), and consensus-based off-policy refinement. However, DDRL assumes a single binary reward signal (correct/incorrect), not the multi-tier reward structure needed for autoformalization where compilation is a hard gate, critic approval indicates semantic correctness, and BEq consensus measures formalization diversity/quality. (4) Co-adaptive retrieval for RAG: R3 (NeurIPS 2025) optimizes retrieval for RAG via reinforced contrastive learning, using environment feedback (task success/failure) to train the retriever with InfoNCE loss. Reinforced-IR (ACL 2025) introduces a self-boosting framework alternating RLRF (retriever from generator feedback) and RLGF (generator from retriever feedback) for mutual adaptation. TTARAG (Jan 2026) adapts models at test time using self-supervised retrieval prediction tasks, demonstrating that retrieval adaptation at inference time is feasible. DDR (Dense Document Retrieval) provides the base dense encoder architecture. None of these have been applied to autoformalization or Lean 4 dependency retrieval. (5) GDPO and multi-reward RL: GDPO (Group reward-Decoupled Normalization Policy Optimization, NVIDIA, Jan 2026, arXiv 2601.05242) addresses the problem of multiple reward signals in GRPO by applying per-reward decoupled normalization, preventing one reward from dominating others during advantage computation. This provides the key technical tool for handling TTRA's multi-tier reward structure. Gap: No existing work combines (a) test-time RL adaptation for autoformalization on unlabeled OOD problems, (b) a trained semantic critic as RL reward signal, (c) co-adaptive retrieval where the dense retriever is updated using compilation error signals during TTRL, and (d) principled adaptation of binary-reward debiased RL (DDRL) to multi-tier rewards via binarize-then-enrich.\",\n  \"inspired_by\": \"FormaRL (GRPO for autoformalization), CriticLean (semantic critic for Lean 4), DDRL (debiased RL with frequency-based filtering), R3/Reinforced-IR/TTARAG (co-adaptive retrieval), GDPO (multi-reward decoupled normalization), Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop)\",\n  \"approach\": \"We propose TTRA, a test-time retrieval-augmented RL framework for domain-adaptive autoformalization in Lean 4, combining three innovations: (1) a dual-loop architecture with co-adaptive retrieval where the dense retriever is explicitly fine-tuned during TTRL using compilation error signals, (2) integration of CriticLean-14B as a semantic reward signal within the RL loop, and (3) principled adaptation of DDRL's binary debiasing to multi-tier rewards via a binarize-then-enrich strategy inspired by GDPO.\\n\\n**Phase 0 — Minimal Pilot Experiment (De-risking, ~40 A100-hours, 1-2 weeks):**\\nBefore the full pipeline, we validate the two riskiest assumptions. Setup: Take FormaRL's GRPO pipeline, replace its LLM-consistency reward with CriticLean-14B as the reward signal. Data: 200 problems from Con-NF (OOD for most models) + 200 from FormalMATH number theory (near-distribution). No retrieval, no curriculum, no DDRL debiasing — just vanilla GRPO with r_compile * r_critic. Primary hypothesis: If CriticLean-14B reward achieves >=3pp BEq@1 improvement over compilation-only GRPO on Con-NF, the core premise (semantic critic rewards enable OOD adaptation) is validated. Secondary hypothesis: If the pilot shows >15% false reward rate (critic approves semantically wrong formalizations that happen to compile), we need critic calibration before proceeding to the full pipeline. This pilot validates: (a) CriticLean rewards provide sufficient signal for RL training, and (b) the ~15.2% critic error rate does not introduce systematic bias during GRPO training.\\n\\n**Architecture — Dual-Loop Co-Adaptive Retrieval:**\\nThe retriever is a DDR-style dense encoder that IS fine-tuned during TTRL, not frozen. The mechanism exploits a key property of Lean 4's type checker: when formalization fails with an `unknownIdentifier` error, the error message explicitly names the missing Mathlib constant (e.g., `unknown identifier 'Finset.sum_comm'`), creating a direct mapping from failed formalization to needed dependency.\\n\\n- Loop 1 (Formalizer GRPO, every step): The formalizer generates K=32 candidate formalizations per problem, each compiled against Lean 4. Rewards are computed (compilation, critic, BEq). GRPO/DDRL policy gradient updates the formalizer.\\n- Loop 2 (Retriever update, every N_ret=50 GRPO steps): Accumulated compilation feedback generates contrastive training data for the retriever.\\n  - Hard-negative mining from compilation errors: When formalization fails with `unknownIdentifier X`, the currently retrieved dependencies that did NOT include X are hard negatives. X itself (looked up in the Mathlib constant index) becomes the positive example.\\n  - Positive confirmation from successful compilations: When formalization succeeds and compiles, all retrieved dependencies used in the successful formalization are confirmed positives for that query.\\n  - Training signal: (query=informal_statement, positive_dep=needed_dependency, negative_dep=retrieved_but_wrong) triples are accumulated and used to update the retriever via InfoNCE contrastive loss.\\n  - Decoupled optimization: Retriever updates are decoupled from policy gradient steps (alternating optimization). The retriever's gradient does NOT flow through the formalizer's policy gradient, preventing destabilization. This follows the alternating optimization paradigm established by Reinforced-IR (ACL 2025) and R3 (NeurIPS 2025).\\n  - Retrieval index refresh: After each retriever update, the Mathlib dependency embeddings are re-encoded and the FAISS index is rebuilt, ensuring subsequent retrievals reflect the updated encoder.\\n\\n**Multi-Tier Reward with Binarize-Then-Enrich (DDRL-to-Autoformalization Adaptation):**\\nDDRL assumes a single binary correct/incorrect reward, but autoformalization has a multi-tier reward: r_compile (binary: compiles or not), r_critic (binary: CriticLean approves semantic correctness or not), and r_BEq (continuous: BEq consensus density measuring formalization diversity). We adapt DDRL via a binarize-then-enrich strategy inspired by GDPO (arXiv 2601.05242):\\n\\n- Binarization for DDRL's sampling and advantages: Define binary acceptance as r_accept = I(r_compile=1 AND r_critic=1). This gives DDRL a clean binary signal. Compilation is a hard prerequisite (non-negotiable binary gate); the critic's 84.8% accuracy makes it the most informative single signal after compilation.\\n  - Balanced sampling: Partition K=32 candidates into 'accepted' (compile + critic approves) and 'rejected' (otherwise). Exclude problems where acceptance frequency falls in the ambiguous zone (30-70% acceptance rate, i.e., between ~10-22 of 32 candidates accepted), following DDRL's frequency-based filtering insight that ambiguous problems provide unreliable pseudo-labels.\\n  - Fixed advantages: +1 for accepted, -1 for rejected candidates, eliminating GRPO's amplification pathway that DDRL identifies as problematic.\\n  - Consensus-based off-policy refinement: Rejection sampling on high-confidence samples (>80% acceptance rate), following DDRL's consensus mechanism.\\n- GDPO-style enrichment for BEq: Among accepted candidates, apply GDPO's per-reward decoupled normalization to preserve the BEq consensus density signal as a secondary ranking bonus. The BEq component is normalized independently from the binary acceptance signal, preventing it from being collapsed as standard GRPO would do. This adds a gradient bonus proportional to BEq consensus among accepted candidates without disturbing DDRL's debiasing.\\n- This adaptation is itself a methodological contribution: extending single-reward debiased RL to multi-tier rewards via binarize-then-enrich, applicable beyond autoformalization.\\n\\n**Curriculum:**\\nProblems are ordered by estimated difficulty using a proxy: the compilation rate of the base model's greedy decode (no RL). Easy problems (high compilation rate) come first, allowing the retriever and formalizer to co-adapt on tractable examples before facing harder OOD problems. Difficulty bins are recalibrated every 200 GRPO steps based on current model performance.\\n\\n**Evaluation:**\\n- Primary: BEq@1 and BEq@K on OOD benchmarks (Con-NF, held-out FormalMATH domains, competition math)\\n- Secondary: Compilation rate, critic approval rate, retrieval recall@10 for Mathlib dependencies\\n- Ablations: (a) Full TTRA, (b) no retriever co-adaptation (frozen retriever), (c) compilation-only reward (no critic), (d) standard GRPO (no DDRL debiasing), (e) no curriculum\\n- Baselines: FormaRL, Online RL for Autoformalization (Wang et al.), base model zero-shot, retrieval-augmented zero-shot (no RL)\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"team\": \"2 researchers (1 lead on RL pipeline + DDRL adaptation + critic integration, 1 on retrieval co-adaptation + Lean 4 infrastructure + evaluation)\",\n      \"gpu_hours\": \"~300-420h A100 80GB (Phase 0 pilot: ~40h; Full TTRA training: ~80-100h on 4 A100s; 4 ablation variants x ~40-60h each = 160-240h; evaluation sweeps: ~20-40h)\",\n      \"estimated_gpu_cost\": \"$450-630 (at ~$1.50/h A100 80GB)\",\n      \"gpu_utilization\": \"~15-25% effective — idle during result analysis, reward debugging, retriever index rebuilds between phases\",\n      \"timeline\": \"10-12 weeks (1-2 weeks Phase 0 pilot + analysis; 2-3 weeks retrieval co-adaptation infrastructure + Lean 4 compilation pipeline; 4-5 weeks iterative experimentation including all ablations; 2-3 weeks evaluation + paper writing)\"\n    },\n    \"human_in_loop\": {\n      \"team\": \"1 researcher, ~1.5h/day review\",\n      \"gpu_hours\": \"~350-500h A100 80GB (agent runs Phase 0 pilot, full pipeline + 4 ablations x 2 hyperparameter variants, retriever co-adaptation tuning)\",\n      \"estimated_gpu_cost\": \"$525-750 (at ~$1.50/h A100 80GB)\",\n      \"claude_api_cost\": \"$300-700 (estimated 3,000-7,000 agent turns)\",\n      \"gpu_utilization\": \"~40-55% — agent queues experiments but pauses at key gates: (1) Phase 0 pilot analysis (go/no-go for full pipeline), (2) retriever co-adaptation convergence check, (3) DDRL binarization threshold validation\",\n      \"risk_note\": \"Phase 0 pilot de-risks the two core assumptions before committing to full pipeline compute. If pilot fails (critic reward insufficient or >15% false reward rate), agent escalates before spending full pipeline budget.\",\n      \"timeline\": \"7-9 weeks (1-2 weeks Phase 0 pilot; 3-4 weeks full pipeline + ablations; 2-3 weeks evaluation + writing)\"\n    },\n    \"auto_research\": {\n      \"team\": \"0 researchers after initial setup (~4-6 hours: Lean 4 + Mathlib environment, CriticLean-14B deployment, dataset access, retriever index initialization)\",\n      \"gpu_hours\": \"~500-750h A100 80GB (agent explores 10-15 configurations for DDRL binarization thresholds, retriever update frequency N_ret, curriculum schedules, all ablation variants x 2-3 seeds, full benchmark sweeps)\",\n      \"estimated_gpu_cost\": \"$750-1,125 (at ~$1.50/h A100 80GB)\",\n      \"claude_api_cost\": \"$500-1,200 (estimated 5,000-12,000 agent turns)\",\n      \"gpu_utilization\": \"~85-95% — agent immediately queues next experiment; parallel ablation runs on multi-GPU setup\",\n      \"risk_note\": \"Phase 0 pilot is the first experiment queued; if it fails, agent pivots to critic calibration or alternative reward formulations before proceeding. Retriever co-adaptation monitored via retrieval recall@10 — if no improvement after 200 GRPO steps, agent adjusts N_ret or InfoNCE temperature.\",\n      \"speed_bottleneck\": \"Each GRPO training run on the formalizer takes ~20-30h on 4 A100s. Lean 4 compilation bottleneck: ~2-5 seconds per candidate, partially parallelizable. CriticLean-14B inference: ~0.5s per candidate on 1 A100.\",\n      \"timeline\": \"4-6 weeks with 4+ A100 GPUs available concurrently (Phase 0: week 1; full pipeline: weeks 2-4; ablations + evaluation: weeks 4-6)\"\n    }\n  },\n  \"target_venues\": [\n    \"EACL 2027 ARR August cycle (submission Aug 3, 2026 — primary target, 68 days from May 27; strong fit for NLP/formal methods intersection with RL methodology contribution)\",\n    \"NeurIPS 2026 Workshops (submission ~Aug 29, 2026 — 94 days; MATH-AI or similar workshop for early results from Phase 0 + Phase 1)\",\n    \"AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — feasible ONLY with auto_research mode starting immediately; 55 days to abstract deadline is tight but possible if Phase 0 pilot + Phase 1 are complete by mid-July)\",\n    \"ICLR 2027 (abstract ~Sep 2026 — best fit for full pipeline results with all ablations and retrieval co-adaptation analysis; top-tier target if OOD results are strong)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"FormaRL — GRPO with compilation-based rewards for autoformalization in Lean 4; direct baseline and starting point for TTRA's RL pipeline\",\n    \"CriticLean-14B — trained semantic critic for Lean 4 formalizations, 84.8% accuracy on semantic correctness judgments; provides the key reward signal beyond compilation\",\n    \"DDRL: Debiased and Denoised RL — addresses GRPO's reward noise amplification via frequency-based balanced sampling, fixed advantages, and consensus-based off-policy refinement; assumes binary rewards, adapted by TTRA to multi-tier\",\n    \"GDPO: Group reward-Decoupled Normalization Policy Optimization (arXiv 2601.05242, NVIDIA, Jan 2026) — per-reward decoupled normalization for multi-reward GRPO; provides the technical tool for TTRA's binarize-then-enrich strategy preserving BEq signal\",\n    \"R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning (NeurIPS 2025) — uses RAG environment feedback (task success/failure) for contrastive retriever training with InfoNCE loss; establishes precedent for TTRA's retriever co-adaptation\",\n    \"Reinforced-IR: A Self-Boosting Framework for Domain-Adaptive Retrieval (ACL 2025) — alternates RLRF/RLGF for mutual retriever-generator adaptation; validates alternating optimization paradigm used in TTRA's dual-loop architecture\",\n    \"TTARAG: Predict the Retrieval! Test-Time Adaptation for RAG (arXiv 2601.11443, Jan 2026) — demonstrates test-time retrieval adaptation via self-supervised prediction tasks; validates feasibility of adapting retrieval at inference time\",\n    \"Online Reinforcement Learning for Autoformalization (Haiming Wang et al., NeurIPS 2025 MAR Workshop) — GRPO with composite rewards (BEq + embedding similarity) for Lean 4 autoformalization; TC1: 17.29% to 26.01%, TC50: 76.41% to 85.46% on RLMEval; closest prior work on RL for autoformalization but lacks retrieval, test-time adaptation, and trained semantic critic\",\n    \"DDR (Dense Document Retrieval) — base dense encoder architecture for TTRA's retriever component\",\n    \"Con-NF — OOD benchmark for autoformalization; competition-level number theory and formalization challenges\",\n    \"FormalMATH — benchmark for mathematical formalization in Lean 4; used for near-distribution evaluation\",\n    \"BEq (Behavioral Equivalence) — metric for evaluating semantic correctness of formalizations via consensus across multiple candidates\",\n    \"Mathlib — Lean 4's mathematical library; source of dependency constants whose retrieval is critical for OOD formalization\",\n    \"GRPO (Group Relative Policy Optimization) — base RL algorithm for LLM fine-tuning; used by FormaRL and Online RL for Autoformalization\"\n  ],\n  \"description\": \"We propose TTRA, a test-time retrieval-augmented reinforcement learning framework for domain-adaptive autoformalization in Lean 4 that enables adaptation to out-of-distribution mathematical domains without any labeled formal-informal pairs. TTRA combines three innovations: (1) a dual-loop co-adaptive retrieval architecture where a DDR-style dense retriever is explicitly fine-tuned during test-time RL using Lean 4 compilation error signals — specifically, `unknownIdentifier` errors that name missing Mathlib constants provide hard negatives for InfoNCE contrastive training, while successfully compiled formalizations confirm positive dependencies, with retriever updates decoupled from formalizer policy gradient steps every N_ret=50 GRPO steps following the alternating optimization paradigm of R3 (NeurIPS 2025) and Reinforced-IR (ACL 2025); (2) integration of CriticLean-14B (84.8% accuracy) as a semantic reward signal within the RL loop, going beyond compilation-only rewards to assess whether formalizations faithfully capture the informal statement's meaning; and (3) a binarize-then-enrich adaptation of DDRL's binary debiasing to multi-tier rewards, where binary acceptance (compile AND critic approval) provides DDRL's frequency-based balanced sampling and fixed advantages for debiasing, while GDPO-style per-reward decoupled normalization preserves the BEq consensus density signal as a secondary ranking bonus among accepted candidates without disturbing the debiasing — this adaptation from single-reward to multi-tier debiased RL is itself a methodological contribution applicable beyond autoformalization. A Phase 0 minimal pilot (~40 A100-hours) validates the two riskiest assumptions before full pipeline commitment: that CriticLean rewards provide sufficient RL signal (>=3pp BEq@1 improvement over compilation-only GRPO on Con-NF) and that the ~15.2% critic error rate does not introduce systematic bias. Primary targets: EACL 2027 ARR August cycle and NeurIPS 2026 Workshops, with ICLR 2027 as the top-tier target for full pipeline results.\",\n  \"project_name\": \"ttra_critic_guided\",\n  \"source\": \"web_research\",\n  \"change_type\": \"major\",\n  \"reviewer_response\": {\n    \"issue_1_co_adaptive_retrieval_mechanism\": \"MAJOR FIX — The reviewer's core complaint was that 're-rank and update the retrieval index based on these signals' was vague, leaving unclear whether the retriever is fine-tuned during TTRL. We now specify a concrete dual-loop architecture: the retriever (a DDR-style dense encoder) IS fine-tuned during TTRL using InfoNCE contrastive loss. The training signal exploits a key property of Lean 4's type checker: `unknownIdentifier` errors explicitly name the missing Mathlib constant (e.g., `unknown identifier 'Finset.sum_comm'`), creating a direct mapping from failed formalization to needed dependency. Hard-negative mining: when formalization fails with `unknownIdentifier X`, currently retrieved dependencies that did NOT include X are hard negatives; X itself (looked up in the Mathlib index) becomes the positive. Successful compilations confirm all used dependencies as positives. Retriever is updated every N_ret=50 GRPO steps using accumulated (query, positive_dep, negative_dep) triples with InfoNCE loss. Crucially, retriever updates are decoupled from policy gradient steps (alternating optimization), preventing destabilization — the retriever's gradient does NOT flow through the formalizer's policy gradient. This draws on established precedent: R3 (NeurIPS 2025) uses RAG environment feedback for contrastive retriever training; Reinforced-IR (ACL 2025) alternates RLRF/RLGF for mutual adaptation; TTARAG (Jan 2026) demonstrates test-time retrieval adaptation feasibility.\",\n    \"issue_2_ddrl_to_autoformalization_adaptation\": \"MAJOR FIX — The reviewer noted that DDRL assumes binary correct/incorrect, but TTRA's multi-tier reward R has continuous range. We now adopt a concrete binarize-then-enrich strategy inspired by GDPO (NVIDIA, Jan 2026). Binarization: define binary acceptance as r_accept = I(r_compile=1 AND r_critic=1), giving DDRL a clean binary signal. Compilation is a non-negotiable binary gate; the critic's 84.8% accuracy makes it the most informative signal after compilation. Balanced sampling partitions K=32 candidates into accepted/rejected, excluding problems in the 30-70% ambiguous acceptance zone (~10-22 of 32 candidates), following DDRL's frequency-based filtering. Fixed advantages: +1 accepted, -1 rejected, eliminating GRPO's amplification pathway. Enrichment: among accepted candidates, GDPO's per-reward decoupled normalization preserves BEq consensus density as a secondary ranking bonus, normalized independently from the binary acceptance signal to prevent collapse. This adds a gradient bonus proportional to BEq consensus without disturbing DDRL's debiasing. The threshold justification (compile AND critic) is natural: compilation is a hard prerequisite, and the 30-70% ambiguous zone means if between ~10-22 of 32 candidates are accepted, the problem is too uncertain for reliable pseudo-labels — exactly DDRL's insight applied to multi-tier rewards. This adaptation from single-reward to multi-tier debiased RL is itself a methodological contribution.\",\n    \"issue_3_de_risk_with_minimal_pilot\": \"MAJOR FIX — We now include a Phase 0 minimal pilot experiment before the full pipeline. Setup: FormaRL's GRPO pipeline with CriticLean-14B replacing the LLM-consistency reward. Data: 200 Con-NF problems (OOD) + 200 FormalMATH number theory (near-distribution). No retrieval, no curriculum, no DDRL — just vanilla GRPO with r_compile * r_critic. Primary hypothesis: >=3pp BEq@1 improvement over compilation-only GRPO on Con-NF validates the core premise. Secondary hypothesis: >15% false reward rate (critic approves semantically wrong formalizations) indicates need for critic calibration. Resource: ~40 A100-hours, 1-2 weeks. This validates the two riskiest assumptions (critic reward sufficiency and critic error rate impact) before committing to full pipeline compute.\",\n    \"issue_4_cite_online_rl_for_autoformalization\": \"MINOR FIX — We now cite 'Online Reinforcement Learning for Autoformalization' (Haiming Wang et al., NeurIPS 2025 MAR Workshop) throughout. They use GRPO with composite rewards (BEq + embedding-based similarity) achieving TC1: 17.29% to 26.01%, TC50: 76.41% to 85.46% on RLMEval. Positioned as closest prior work on RL for autoformalization: operates at training time with labeled/unlabeled data on in-distribution problems, uses embedding similarity rather than a trained semantic critic, and lacks retrieval, test-time adaptation, and co-adaptive retrieval. TTRA's key differentiators: fully unlabeled OOD test-time adaptation, trained semantic critic (CriticLean-14B) rather than embedding similarity, and co-adaptive retrieval with explicit retriever fine-tuning.\",\n    \"issue_5_adjust_timeline\": \"MINOR FIX — Primary targets updated to EACL 2027 ARR August cycle (Aug 3, 2026, 68 days) and NeurIPS 2026 Workshops (Aug 29, 2026, 94 days). AAAI 2027 (abstract Jul 21, 55 days) is noted as feasible ONLY with auto_research mode starting immediately — tight but possible if Phase 0 pilot + Phase 1 are complete by mid-July. ICLR 2027 (~Sep 2026) remains the best fit for full pipeline results with all ablations. CoRL and other earlier deadlines removed as infeasible.\",\n    \"new_references_added\": \"Added 5 new references: (1) GDPO (arXiv 2601.05242, NVIDIA, Jan 2026) for per-reward decoupled normalization enabling the binarize-then-enrich strategy; (2) R3 (NeurIPS 2025) for reinforced contrastive retriever training from environment feedback; (3) Reinforced-IR (ACL 2025) for alternating retriever-generator mutual adaptation; (4) TTARAG (arXiv 2601.11443, Jan 2026) for test-time retrieval adaptation feasibility; (5) Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) for the closest prior work on RL for autoformalization.\",\n    \"stagnation_response\": \"This revision constitutes a MAJOR change addressing the reviewer's assessment that 3 targeted fixes would bring the idea to pass quality. All three major issues are addressed with concrete, specified mechanisms rather than vague descriptions: (1) the retriever co-adaptation now has explicit parameter updates, loss functions, and training data construction from Lean 4 error signals; (2) the DDRL adaptation now has a principled binarize-then-enrich strategy with justified thresholds; (3) a Phase 0 pilot experiment de-risks the two core assumptions before full pipeline commitment. The two minor issues (citation and timeline) are also addressed.\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f60b27a-824d-4e29-a7f4-a87060b501d1",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTZtaqiAT1oDxCzmx56f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fb53193-d27e-44ae-a584-64944002cb24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SXKrJSPjG3JDdh3BHnsq8k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 48828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1136,
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

_source line 41 · 2026-05-27T18:47:07.450Z_

<details><summary>↩ Tool result · reported error · `toolu_01E2XUHpp4so8pt1T1n26yjx`</summary>

```text
Claude requested permissions to write to /home/ubuntu/idea_review/ttra_critic_guided_r4.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fb53193-d27e-44ae-a584-64944002cb24",
  "isSidechain": true,
  "promptId": "a32f68a9-f606-4e93-a934-709be6a23385",
  "agentId": "a4296764d735dfe06",
  "type": "user",
  "uuid": "069f6d41-162a-4788-b27a-4812665b0260",
  "toolUseResult": "Error: Claude requested permissions to write to /home/ubuntu/idea_review/ttra_critic_guided_r4.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "7fb53193-d27e-44ae-a584-64944002cb24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-27T18:48:57.833Z_

Here is the complete JSON:

{
  "title": "TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization",
  "core_problem": "How can autoformalization systems adapt at test time to out-of-distribution (OOD) mathematical domains — such as competition mathematics, advanced algebra, or niche subfields — without any labeled (informal, formal) pairs, given that (1) current autoformalization models trained on in-distribution data (e.g., undergraduate-level number theory) suffer severe performance drops on OOD domains where Mathlib dependency patterns, notation conventions, and proof structures differ substantially, (2) compilation-only reward signals are necessary but insufficient for semantic correctness (a formalization can compile but express the wrong theorem), and (3) retrieval of relevant Mathlib dependencies is critical for OOD domains where the model has not memorized the needed imports, yet static retrieval indices become stale as the formalizer's behavior shifts during adaptation?",
  "opportunity": "Autoformalization — translating informal mathematical statements into formally verified Lean 4 code — has seen rapid progress through reinforcement learning. FormaRL demonstrated that GRPO with compilation-based rewards can significantly improve formalization rates. Online Reinforcement Learning for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) showed GRPO with composite rewards (BEq + embedding-based similarity) achieving TC1: 17.29% to 26.01% and TC50: 76.41% to 85.46% on RLMEval, validating RL for autoformalization. However, these approaches operate at training time with labeled or semi-labeled data on in-distribution problems. The key bottleneck for deployment is OOD generalization: when faced with mathematical domains not well-represented in training (competition math from Con-NF, advanced algebraic topology, niche combinatorics), formalization rates collapse because (a) the model lacks familiarity with domain-specific Mathlib dependencies and idioms, (b) static retrieval indices fail to surface the right lemmas for unfamiliar problem structures, and (c) compilation alone cannot verify semantic fidelity. CriticLean (14B parameters, 84.8% accuracy on semantic correctness judgments) provides a learned reward signal that goes beyond compilation to assess whether a formalization faithfully captures the informal statement's meaning — but it has not been integrated into an RL loop. The DDRL framework (Debiased and Denoised RL) addresses reward noise and sampling bias in GRPO through frequency-based filtering and fixed advantages, but assumes binary correct/incorrect rewards, not the multi-tier reward structure (compilation + critic + BEq consensus) needed for autoformalization. Meanwhile, recent advances in retrieval-augmented generation show that retriever and generator can be co-adapted: R3 (NeurIPS 2025) uses RAG environment feedback for contrastive retriever training, Reinforced-IR (ACL 2025) alternates RLRF/RLGF for mutual retriever-generator adaptation, and TTARAG (Jan 2026) adapts models at test time using self-supervised retrieval prediction. The opportunity: combine test-time RL adaptation (GRPO/DDRL) with a semantic critic reward (CriticLean) and co-adaptive retrieval (dense retriever fine-tuned via compilation error signals) to enable domain adaptation on fully unlabeled OOD mathematical problems, without any human-annotated formal statements.",
  "landscape": "The autoformalization and test-time RL landscape has five relevant lineages. (1) RL for autoformalization: FormaRL applies GRPO with compilation-based rewards to improve formalization in Lean 4. Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) uses GRPO with composite rewards (BEq + embedding similarity) achieving strong results on RLMEval (TC1: 17.29% to 26.01%, TC50: 76.41% to 85.46%), but operates at training time with labeled/unlabeled data on in-distribution problems. Neither incorporates a trained semantic critic, co-adaptive retrieval, or test-time adaptation on OOD domains. (2) Semantic critics for formalization: CriticLean-14B achieves 84.8% accuracy on judging semantic correctness of formalizations, trained on synthetic paired data. It provides the key signal beyond compilation — a formalization can compile but misstate the theorem — but has not been used as an RL reward signal. (3) Debiased RL: DDRL (Debiased and Denoised RL) addresses GRPO's amplification of noisy rewards through frequency-based balanced sampling, fixed advantages (+1/-1), and consensus-based off-policy refinement. However, DDRL assumes a single binary reward signal (correct/incorrect), not the multi-tier reward structure needed for autoformalization where compilation is a hard gate, critic approval indicates semantic correctness, and BEq consensus measures formalization diversity/quality. (4) Co-adaptive retrieval for RAG: R3 (NeurIPS 2025) optimizes retrieval for RAG via reinforced contrastive learning, using environment feedback (task success/failure) to train the retriever with InfoNCE loss. Reinforced-IR (ACL 2025) introduces a self-boosting framework alternating RLRF (retriever from generator feedback) and RLGF (generator from retriever feedback) for mutual adaptation. TTARAG (Jan 2026) adapts models at test time using self-supervised retrieval prediction tasks, demonstrating that retrieval adaptation at inference time is feasible. DDR (Dense Document Retrieval) provides the base dense encoder architecture. None of these have been applied to autoformalization or Lean 4 dependency retrieval. (5) GDPO and multi-reward RL: GDPO (Group reward-Decoupled Normalization Policy Optimization, NVIDIA, Jan 2026, arXiv 2601.05242) addresses the problem of multiple reward signals in GRPO by applying per-reward decoupled normalization, preventing one reward from dominating others during advantage computation. This provides the key technical tool for handling TTRA's multi-tier reward structure. Gap: No existing work combines (a) test-time RL adaptation for autoformalization on unlabeled OOD problems, (b) a trained semantic critic as RL reward signal, (c) co-adaptive retrieval where the dense retriever is updated using compilation error signals during TTRL, and (d) principled adaptation of binary-reward debiased RL (DDRL) to multi-tier rewards via binarize-then-enrich.",
  "inspired_by": "FormaRL (GRPO for autoformalization), CriticLean (semantic critic for Lean 4), DDRL (debiased RL with frequency-based filtering), R3/Reinforced-IR/TTARAG (co-adaptive retrieval), GDPO (multi-reward decoupled normalization), Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop)",
  "approach": "We propose TTRA, a test-time retrieval-augmented RL framework for domain-adaptive autoformalization in Lean 4, combining three innovations: (1) a dual-loop architecture with co-adaptive retrieval where the dense retriever is explicitly fine-tuned during TTRL using compilation error signals, (2) integration of CriticLean-14B as a semantic reward signal within the RL loop, and (3) principled adaptation of DDRL's binary debiasing to multi-tier rewards via a binarize-then-enrich strategy inspired by GDPO.\n\n**Phase 0 — Minimal Pilot Experiment (De-risking, ~40 A100-hours, 1-2 weeks):**\nBefore the full pipeline, we validate the two riskiest assumptions. Setup: Take FormaRL's GRPO pipeline, replace its LLM-consistency reward with CriticLean-14B as the reward signal. Data: 200 problems from Con-NF (OOD for most models) + 200 from FormalMATH number theory (near-distribution). No retrieval, no curriculum, no DDRL debiasing — just vanilla GRPO with r_compile * r_critic. Primary hypothesis: If CriticLean-14B reward achieves >=3pp BEq@1 improvement over compilation-only GRPO on Con-NF, the core premise (semantic critic rewards enable OOD adaptation) is validated. Secondary hypothesis: If the pilot shows >15% false reward rate (critic approves semantically wrong formalizations that happen to compile), we need critic calibration before proceeding to the full pipeline. This pilot validates: (a) CriticLean rewards provide sufficient signal for RL training, and (b) the ~15.2% critic error rate does not introduce systematic bias during GRPO training.\n\n**Architecture — Dual-Loop Co-Adaptive Retrieval:**\nThe retriever is a DDR-style dense encoder that IS fine-tuned during TTRL, not frozen. The mechanism exploits a key property of Lean 4's type checker: when formalization fails with an `unknownIdentifier` error, the error message explicitly names the missing Mathlib constant (e.g., `unknown identifier 'Finset.sum_comm'`), creating a direct mapping from failed formalization to needed dependency.\n\n- Loop 1 (Formalizer GRPO, every step): The formalizer generates K=32 candidate formalizations per problem, each compiled against Lean 4. Rewards are computed (compilation, critic, BEq). GRPO/DDRL policy gradient updates the formalizer.\n- Loop 2 (Retriever update, every N_ret=50 GRPO steps): Accumulated compilation feedback generates contrastive training data for the retriever.\n  - Hard-negative mining from compilation errors: When formalization fails with `unknownIdentifier X`, the currently retrieved dependencies that did NOT include X are hard negatives. X itself (looked up in the Mathlib constant index) becomes the positive example.\n  - Positive confirmation from successful compilations: When formalization succeeds and compiles, all retrieved dependencies used in the successful formalization are confirmed positives for that query.\n  - Training signal: (query=informal_statement, positive_dep=needed_dependency, negative_dep=retrieved_but_wrong) triples are accumulated and used to update the retriever via InfoNCE contrastive loss.\n  - Decoupled optimization: Retriever updates are decoupled from policy gradient steps (alternating optimization). The retriever's gradient does NOT flow through the formalizer's policy gradient, preventing destabilization. This follows the alternating optimization paradigm established by Reinforced-IR (ACL 2025) and R3 (NeurIPS 2025).\n  - Retrieval index refresh: After each retriever update, the Mathlib dependency embeddings are re-encoded and the FAISS index is rebuilt, ensuring subsequent retrievals reflect the updated encoder.\n\n**Multi-Tier Reward with Binarize-Then-Enrich (DDRL-to-Autoformalization Adaptation):**\nDDRL assumes a single binary correct/incorrect reward, but autoformalization has a multi-tier reward: r_compile (binary: compiles or not), r_critic (binary: CriticLean approves semantic correctness or not), and r_BEq (continuous: BEq consensus density measuring formalization diversity/quality). We adapt DDRL via a binarize-then-enrich strategy inspired by GDPO (arXiv 2601.05242):\n\n- Binarization for DDRL's sampling and advantages: Define binary acceptance as r_accept = I(r_compile=1 AND r_critic=1). This gives DDRL a clean binary signal. Compilation is a hard prerequisite (non-negotiable binary gate); the critic's 84.8% accuracy makes it the most informative single signal after compilation.\n  - Balanced sampling: Partition K=32 candidates into 'accepted' (compile + critic approves) and 'rejected' (otherwise). Exclude problems where acceptance frequency falls in the ambiguous zone (30-70% acceptance rate, i.e., between ~10-22 of 32 candidates accepted), following DDRL's frequency-based filtering insight that ambiguous problems provide unreliable pseudo-labels.\n  - Fixed advantages: +1 for accepted, -1 for rejected candidates, eliminating GRPO's amplification pathway that DDRL identifies as problematic.\n  - Consensus-based off-policy refinement: Rejection sampling on high-confidence samples (>80% acceptance rate), following DDRL's consensus mechanism.\n- GDPO-style enrichment for BEq: Among accepted candidates, apply GDPO's per-reward decoupled normalization to preserve the BEq consensus density signal as a secondary ranking bonus. The BEq component is normalized independently from the binary acceptance signal, preventing it from being collapsed as standard GRPO would do. This adds a gradient bonus proportional to BEq consensus among accepted candidates without disturbing DDRL's debiasing.\n- This adaptation is itself a methodological contribution: extending single-reward debiased RL to multi-tier rewards via binarize-then-enrich, applicable beyond autoformalization.\n\n**Curriculum:**\nProblems are ordered by estimated difficulty using a proxy: the compilation rate of the base model's greedy decode (no RL). Easy problems (high compilation rate) come first, allowing the retriever and formalizer to co-adapt on tractable examples before facing harder OOD problems. Difficulty bins are recalibrated every 200 GRPO steps based on current model performance.\n\n**Evaluation:**\n- Primary: BEq@1 and BEq@K on OOD benchmarks (Con-NF, held-out FormalMATH domains, competition math)\n- Secondary: Compilation rate, critic approval rate, retrieval recall@10 for Mathlib dependencies\n- Ablations: (a) Full TTRA, (b) no retriever co-adaptation (frozen retriever), (c) compilation-only reward (no critic), (d) standard GRPO (no DDRL debiasing), (e) no curriculum\n- Baselines: FormaRL, Online RL for Autoformalization (Wang et al.), base model zero-shot, retrieval-augmented zero-shot (no RL)",
  "resource_estimate": {
    "manual": {
      "team": "2 researchers (1 lead on RL pipeline + DDRL adaptation + critic integration, 1 on retrieval co-adaptation + Lean 4 infrastructure + evaluation)",
      "gpu_hours": "~300-420h A100 80GB (Phase 0 pilot: ~40h; Full TTRA training: ~80-100h on 4 A100s; 4 ablation variants x ~40-60h each = 160-240h; evaluation sweeps: ~20-40h)",
      "estimated_gpu_cost": "$450-630 (at ~$1.50/h A100 80GB)",
      "gpu_utilization": "~15-25% effective — idle during result analysis, reward debugging, retriever index rebuilds between phases",
      "timeline": "10-12 weeks (1-2 weeks Phase 0 pilot + analysis; 2-3 weeks retrieval co-adaptation infrastructure + Lean 4 compilation pipeline; 4-5 weeks iterative experimentation including all ablations; 2-3 weeks evaluation + paper writing)"
    },
    "human_in_loop": {
      "team": "1 researcher, ~1.5h/day review",
      "gpu_hours": "~350-500h A100 80GB (agent runs Phase 0 pilot, full pipeline + 4 ablations x 2 hyperparameter variants, retriever co-adaptation tuning)",
      "estimated_gpu_cost": "$525-750 (at ~$1.50/h A100 80GB)",
      "claude_api_cost": "$300-700 (estimated 3,000-7,000 agent turns)",
      "gpu_utilization": "~40-55% — agent queues experiments but pauses at key gates: (1) Phase 0 pilot analysis (go/no-go for full pipeline), (2) retriever co-adaptation convergence check, (3) DDRL binarization threshold validation",
      "risk_note": "Phase 0 pilot de-risks the two core assumptions before committing to full pipeline compute. If pilot fails (critic reward insufficient or >15% false reward rate), agent escalates before spending full pipeline budget.",
      "timeline": "7-9 weeks (1-2 weeks Phase 0 pilot; 3-4 weeks full pipeline + ablations; 2-3 weeks evaluation + writing)"
    },
    "auto_research": {
      "team": "0 researchers after initial setup (~4-6 hours: Lean 4 + Mathlib environment, CriticLean-14B deployment, dataset access, retriever index initialization)",
      "gpu_hours": "~500-750h A100 80GB (agent explores 10-15 configurations for DDRL binarization thresholds, retriever update frequency N_ret, curriculum schedules, all ablation variants x 2-3 seeds, full benchmark sweeps)",
      "estimated_gpu_cost": "$750-1,125 (at ~$1.50/h A100 80GB)",
      "claude_api_cost": "$500-1,200 (estimated 5,000-12,000 agent turns)",
      "gpu_utilization": "~85-95% — agent immediately queues next experiment; parallel ablation runs on multi-GPU setup",
      "risk_note": "Phase 0 pilot is the first experiment queued; if it fails, agent pivots to critic calibration or alternative reward formulations before proceeding. Retriever co-adaptation monitored via retrieval recall@10 — if no improvement after 200 GRPO steps, agent adjusts N_ret or InfoNCE temperature.",
      "speed_bottleneck": "Each GRPO training run on the formalizer takes ~20-30h on 4 A100s. Lean 4 compilation bottleneck: ~2-5 seconds per candidate, partially parallelizable. CriticLean-14B inference: ~0.5s per candidate on 1 A100.",
      "timeline": "4-6 weeks with 4+ A100 GPUs available concurrently (Phase 0: week 1; full pipeline: weeks 2-4; ablations + evaluation: weeks 4-6)"
    }
  },
  "target_venues": [
    "EACL 2027 ARR August cycle (submission Aug 3, 2026 — primary target, 68 days from May 27; strong fit for NLP/formal methods intersection with RL methodology contribution)",
    "NeurIPS 2026 Workshops (submission ~Aug 29, 2026 — 94 days; MATH-AI or similar workshop for early results from Phase 0 + Phase 1)",
    "AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — feasible ONLY with auto_research mode starting immediately; 55 days to abstract deadline is tight but possible if Phase 0 pilot + Phase 1 are complete by mid-July)",
    "ICLR 2027 (abstract ~Sep 2026 — best fit for full pipeline results with all ablations and retrieval co-adaptation analysis; top-tier target if OOD results are strong)"
  ],
  "level": "top-tier",
  "key_references": [
    "FormaRL — GRPO with compilation-based rewards for autoformalization in Lean 4; direct baseline and starting point for TTRA's RL pipeline",
    "CriticLean-14B — trained semantic critic for Lean 4 formalizations, 84.8% accuracy on semantic correctness judgments; provides the key reward signal beyond compilation",
    "DDRL: Debiased and Denoised RL — addresses GRPO's reward noise amplification via frequency-based balanced sampling, fixed advantages, and consensus-based off-policy refinement; assumes binary rewards, adapted by TTRA to multi-tier",
    "GDPO: Group reward-Decoupled Normalization Policy Optimization (arXiv 2601.05242, NVIDIA, Jan 2026) — per-reward decoupled normalization for multi-reward GRPO; provides the technical tool for TTRA's binarize-then-enrich strategy preserving BEq signal",
    "R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning (NeurIPS 2025) — uses RAG environment feedback (task success/failure) for contrastive retriever training with InfoNCE loss; establishes precedent for TTRA's retriever co-adaptation",
    "Reinforced-IR: A Self-Boosting Framework for Domain-Adaptive Retrieval (ACL 2025) — alternates RLRF/RLGF for mutual retriever-generator adaptation; validates alternating optimization paradigm used in TTRA's dual-loop architecture",
    "TTARAG: Predict the Retrieval! Test-Time Adaptation for RAG (arXiv 2601.11443, Jan 2026) — demonstrates test-time retrieval adaptation via self-supervised prediction tasks; validates feasibility of adapting retrieval at inference time",
    "Online Reinforcement Learning for Autoformalization (Haiming Wang et al., NeurIPS 2025 MAR Workshop) — GRPO with composite rewards (BEq + embedding similarity) for Lean 4 autoformalization; TC1: 17.29% to 26.01%, TC50: 76.41% to 85.46% on RLMEval; closest prior work on RL for autoformalization but lacks retrieval, test-time adaptation, and trained semantic critic",
    "DDR (Dense Document Retrieval) — base dense encoder architecture for TTRA's retriever component",
    "Con-NF — OOD benchmark for autoformalization; competition-level number theory and formalization challenges",
    "FormalMATH — benchmark for mathematical formalization in Lean 4; used for near-distribution evaluation",
    "BEq (Behavioral Equivalence) — metric for evaluating semantic correctness of formalizations via consensus across multiple candidates",
    "Mathlib — Lean 4's mathematical library; source of dependency constants whose retrieval is critical for OOD formalization",
    "GRPO (Group Relative Policy Optimization) — base RL algorithm for LLM fine-tuning; used by FormaRL and Online RL for Autoformalization"
  ],
  "description": "We propose TTRA, a test-time retrieval-augmented reinforcement learning framework for domain-adaptive autoformalization in Lean 4 that enables adaptation to out-of-distribution mathematical domains without any labeled formal-informal pairs. TTRA combines three innovations: (1) a dual-loop co-adaptive retrieval architecture where a DDR-style dense retriever is explicitly fine-tuned during test-time RL using Lean 4 compilation error signals — specifically, `unknownIdentifier` errors that name missing Mathlib constants provide hard negatives for InfoNCE contrastive training, while successfully compiled formalizations confirm positive dependencies, with retriever updates decoupled from formalizer policy gradient steps every N_ret=50 GRPO steps following the alternating optimization paradigm of R3 (NeurIPS 2025) and Reinforced-IR (ACL 2025); (2) integration of CriticLean-14B (84.8% accuracy) as a semantic reward signal within the RL loop, going beyond compilation-only rewards to assess whether formalizations faithfully capture the informal statement's meaning; and (3) a binarize-then-enrich adaptation of DDRL's binary debiasing to multi-tier rewards, where binary acceptance (compile AND critic approval) provides DDRL's frequency-based balanced sampling and fixed advantages for debiasing, while GDPO-style per-reward decoupled normalization preserves the BEq consensus density signal as a secondary ranking bonus among accepted candidates without disturbing the debiasing — this adaptation from single-reward to multi-tier debiased RL is itself a methodological contribution applicable beyond autoformalization. A Phase 0 minimal pilot (~40 A100-hours) validates the two riskiest assumptions before full pipeline commitment: that CriticLean rewards provide sufficient RL signal (>=3pp BEq@1 improvement over compilation-only GRPO on Con-NF) and that the ~15.2% critic error rate does not introduce systematic bias. Primary targets: EACL 2027 ARR August cycle and NeurIPS 2026 Workshops, with ICLR 2027 as the top-tier target for full pipeline results.",
  "project_name": "ttra_critic_guided",
  "source": "web_research",
  "change_type": "major",
  "reviewer_response": {
    "issue_1_co_adaptive_retrieval_mechanism": "MAJOR FIX — The reviewer's core complaint was that 're-rank and update the retrieval index based on these signals' was vague, leaving unclear whether the retriever is fine-tuned during TTRL. We now specify a concrete dual-loop architecture: the retriever (a DDR-style dense encoder) IS fine-tuned during TTRL using InfoNCE contrastive loss. The training signal exploits a key property of Lean 4's type checker: `unknownIdentifier` errors explicitly name the missing Mathlib constant (e.g., `unknown identifier 'Finset.sum_comm'`), creating a direct mapping from failed formalization to needed dependency. Hard-negative mining: when formalization fails with `unknownIdentifier X`, currently retrieved dependencies that did NOT include X are hard negatives; X itself (looked up in the Mathlib index) becomes the positive. Successful compilations confirm all used dependencies as positives. Retriever is updated every N_ret=50 GRPO steps using accumulated (query, positive_dep, negative_dep) triples with InfoNCE loss. Crucially, retriever updates are decoupled from policy gradient steps (alternating optimization), preventing destabilization — the retriever's gradient does NOT flow through the formalizer's policy gradient. This draws on established precedent: R3 (NeurIPS 2025) uses RAG environment feedback for contrastive retriever training; Reinforced-IR (ACL 2025) alternates RLRF/RLGF for mutual adaptation; TTARAG (Jan 2026) demonstrates test-time retrieval adaptation feasibility.",
    "issue_2_ddrl_to_autoformalization_adaptation": "MAJOR FIX — The reviewer noted that DDRL assumes binary correct/incorrect, but TTRA's multi-tier reward R has continuous range. We now adopt a concrete binarize-then-enrich strategy inspired by GDPO (NVIDIA, Jan 2026). Binarization: define binary acceptance as r_accept = I(r_compile=1 AND r_critic=1), giving DDRL a clean binary signal. Compilation is a non-negotiable binary gate; the critic's 84.8% accuracy makes it the most informative signal after compilation. Balanced sampling partitions K=32 candidates into accepted/rejected, excluding problems in the 30-70% ambiguous acceptance zone (~10-22 of 32 candidates), following DDRL's frequency-based filtering. Fixed advantages: +1 accepted, -1 rejected, eliminating GRPO's amplification pathway. Enrichment: among accepted candidates, GDPO's per-reward decoupled normalization preserves BEq consensus density as a secondary ranking bonus, normalized independently from the binary acceptance signal to prevent collapse. This adds a gradient bonus proportional to BEq consensus without disturbing DDRL's debiasing. The threshold justification (compile AND critic) is natural: compilation is a hard prerequisite, and the 30-70% ambiguous zone means if between ~10-22 of 32 candidates are accepted, the problem is too uncertain for reliable pseudo-labels — exactly DDRL's insight applied to multi-tier rewards. This adaptation from single-reward to multi-tier debiased RL is itself a methodological contribution.",
    "issue_3_de_risk_with_minimal_pilot": "MAJOR FIX — We now include a Phase 0 minimal pilot experiment before the full pipeline. Setup: FormaRL's GRPO pipeline with CriticLean-14B replacing the LLM-consistency reward. Data: 200 Con-NF problems (OOD) + 200 FormalMATH number theory (near-distribution). No retrieval, no curriculum, no DDRL — just vanilla GRPO with r_compile * r_critic. Primary hypothesis: >=3pp BEq@1 improvement over compilation-only GRPO on Con-NF validates the core premise. Secondary hypothesis: >15% false reward rate (critic approves semantically wrong formalizations) indicates need for critic calibration. Resource: ~40 A100-hours, 1-2 weeks. This validates the two riskiest assumptions (critic reward sufficiency and critic error rate impact) before committing to full pipeline compute.",
    "issue_4_cite_online_rl_for_autoformalization": "MINOR FIX — We now cite 'Online Reinforcement Learning for Autoformalization' (Haiming Wang et al., NeurIPS 2025 MAR Workshop) throughout. They use GRPO with composite rewards (BEq + embedding-based similarity) achieving TC1: 17.29% to 26.01%, TC50: 76.41% to 85.46% on RLMEval. Positioned as closest prior work on RL for autoformalization: operates at training time with labeled/unlabeled data on in-distribution problems, uses embedding similarity rather than a trained semantic critic, and lacks retrieval, test-time adaptation, and co-adaptive retrieval. TTRA's key differentiators: fully unlabeled OOD test-time adaptation, trained semantic critic (CriticLean-14B) rather than embedding similarity, and co-adaptive retrieval with explicit retriever fine-tuning.",
    "issue_5_adjust_timeline": "MINOR FIX — Primary targets updated to EACL 2027 ARR August cycle (Aug 3, 2026, 68 days) and NeurIPS 2026 Workshops (Aug 29, 2026, 94 days). AAAI 2027 (abstract Jul 21, 55 days) is noted as feasible ONLY with auto_research mode starting immediately — tight but possible if Phase 0 pilot + Phase 1 are complete by mid-July. ICLR 2027 (~Sep 2026) remains the best fit for full pipeline results with all ablations. CoRL and other earlier deadlines removed as infeasible.",
    "new_references_added": "Added 5 new references: (1) GDPO (arXiv 2601.05242, NVIDIA, Jan 2026) for per-reward decoupled normalization enabling the binarize-then-enrich strategy; (2) R3 (NeurIPS 2025) for reinforced contrastive retriever training from environment feedback; (3) Reinforced-IR (ACL 2025) for alternating retriever-generator mutual adaptation; (4) TTARAG (arXiv 2601.11443, Jan 2026) for test-time retrieval adaptation feasibility; (5) Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) for the closest prior work on RL for autoformalization.",
    "stagnation_response": "This revision constitutes a MAJOR change addressing the reviewer's assessment that 3 targeted fixes would bring the idea to pass quality. All three major issues are addressed with concrete, specified mechanisms rather than vague descriptions: (1) the retriever co-adaptation now has explicit parameter updates, loss functions, and training data construction from Lean 4 error signals; (2) the DDRL adaptation now has a principled binarize-then-enrich strategy with justified thresholds; (3) a Phase 0 pilot experiment de-risks the two core assumptions before full pipeline commitment. The two minor issues (citation and timeline) are also addressed."
  }
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "069f6d41-162a-4788-b27a-4812665b0260",
  "isSidechain": true,
  "agentId": "a4296764d735dfe06",
  "requestId": "req_011CbTa6yoR9SUBLDAxXv9Bt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9570ae1-0cb5-4ffd-a660-766cc444b907",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "acc7a6f0-d2a0-40a6-a309-549632b2305e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018fczuTsYBtMpoWGwQsKXJs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7896,
      "cache_read_input_tokens": 49964,
      "output_tokens": 7694,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7896
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7694,
          "cache_read_input_tokens": 49964,
          "cache_creation_input_tokens": 7896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7896,
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
