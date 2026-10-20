# Research conversation: Complete the research direction below with implementation details. **Today's date: 2026-05-27 (UTC).** Only recommend ve

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/78f193f8-febe-4b1b-a19c-57e61b202db0.jsonl`
- **Structured JSON:** [`7d5d66b63f90f13c7d0f.json`](../../sessions/7d/7d5d66b63f90f13c7d0f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:22:45.073Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:22:45.073Z",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
  "content": "Complete the research direction below with implementation details.\n\n**Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.\n\n{\n  \"title\": \"Potential-Valued Process Rewards for Principled Step-Level Credit Assignment\",\n  \"core_problem\": \"Current PRMs are trained as step-correctness classifiers but heuristically repurposed as RL reward signals via aggregation (sum, min, product), causing either reward hacking or information loss. No principled framework connects PRM design to RL training quality, despite potential-based reward shaping (PBRS) theory guaranteeing policy invariance — a well-known result never practically implemented for step-level process rewards in mathematical reasoning.\",\n  \"opportunity\": \"Three independent 2025-2026 findings converge: (1) the RARL survey confirms PBRS 'lacks practical PRM implementation' for reasoning RL; (2) DuaShepherd proves step correctness and step value (potential) are orthogonal signals — yet all existing PRMs train only on correctness; (3) PURE demonstrates that sum-form PRM aggregation causes training collapse, while min-form loses useful gradient information, but provides no theoretical justification for why min works better. Training a PRM as a state value function V(s_t) = P(correct | prefix₁:t) and deriving step rewards as potential differences r_t = γV(s_{t+1}) − V(s_t) would unify these findings: PBRS guarantees no policy distortion, value-function training requires only outcome labels (no expensive step annotations), and the framework naturally subsumes sum/min/product as suboptimal special cases with specific potential-function choices.\",\n  \"landscape\": \"PRM-RL integration is the most contested frontier. PURE (2025) showed min-form credit assignment avoids reward hacking that collapses sum-form training 'even at the beginning,' but provides only empirical justification. TDRM (Sep 2025) applies TD learning to smooth PRM labels, achieving 23.7% improvement in tree-search and 20× data efficiency, but still requires step-level annotations and doesn't address the aggregation problem. CRM (2025) models step rewards as conditional probabilities P(correct|s_{1:t}) causally linked to outcomes, evaluating on best-of-N, beam search, AND RL — but lacks PBRS guarantees and still uses MC-estimated step labels. PRIME (ICLR 2026) extracts implicit process rewards from ORM token probabilities and is acknowledged as 'viewable as PBRS where q-value is the potential,' but uses heuristic extraction rather than explicit value function training. DuaShepherd (June 2025) separates correctness and potential reward heads, achieving SOTA on MATH500/ProcessBench, but evaluates only at inference time (best-of-N), not RL training. DVPO (ICLR 2026) pretrains a Global Value Model for general RLHF with 40% less GPU memory, but operates at response-level, not step-level process supervision. The RARL survey (Feb 2026) catalogs 47+ credit assignment methods and identifies the central open problem: 'Different aggregation schemes produce divergent policy behaviors, yet principled design guidelines remain absent.'\",\n  \"inspired_by\": \"Gap: RARL survey's verified finding that PBRS 'lacks practical PRM implementation' despite theoretical support for policy invariance. Gap: DuaShepherd's proof that correctness and value are orthogonal, implying current correctness-only PRMs are insufficient for RL. Pattern: DVPO's 'pretrain value, not reward' principle applied to step-level reasoning. Combination: PRIME's PBRS connection (implicit, heuristic) + CRM's causal outcome alignment (no PBRS guarantee) + TDRM's temporal consistency (requires step labels) — unified through explicit outcome-supervised value function training with formal PBRS guarantees.\"\n}\n\nADD these fields (keep all existing fields):\n{\n  \"approach\": \"Proposed method — what you would actually do (3-5 sentences)\",\n  \"resource_estimate\": {\n      \"manual\": {\"gpu_hours\": \"...\", \"timeline\": \"...\", \"estimated_gpu_cost\": \"...\"},\n      \"human_in_loop\": {\"gpu_hours\": \"...\", \"timeline\": \"...\", \"claude_api_cost\": \"...\", \"estimated_gpu_cost\": \"...\"},\n      \"auto_research\": {\"gpu_hours\": \"...\", \"timeline\": \"...\", \"claude_api_cost\": \"...\", \"estimated_gpu_cost\": \"...\", \"speed_bottleneck\": \"...\"}\n  },\n  \"target_venues\": [\"Only venues with deadlines after 2026-05-27\"],\n  \"level\": \"top-tier | solid | incremental\",\n  \"key_references\": [\"Paper title (VENUE YEAR)\", ...],\n  \"description\": \"Executive summary (150-200 words)\",\n  \"project_name\": \"snake_case_identifier (max 30 chars)\",\n  \"source\": \"web_research\"\n}\n\nFor key_references, verify with web_search that cited papers are real. Drop unverifiable ones.\n\n**Model freshness rule**: When the approach involves pretrained models, use web_search to find current top-performing open-source models — do NOT default to models from your training data.\n\n## 竞争论文 & Concurrent Work 搜索\n\n在设计 approach 之前，必须确认没有人正在做同样的事情：\n- 搜索 `{core_problem} 2026` 和 `{approach_keyword} {task} 2026`\n- 在 arXiv 上搜索过去 3 个月的相关提交\n- 在 OpenReview 上搜索即将举行的会议提交\n- 如果发现高度相似的 concurrent work，必须在 landscape 中明确提及\n\n## 可行性验证\n\n1. 搜索类似方法的已有实现（GitHub）\n2. 查找需要打败的具体 baseline 数字\n3. 了解类似实验的硬件/数据需求\n\nOutput ONLY a single JSON object with ALL fields merged. No markdown fences."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T08:22:45.077Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:22:45.077Z",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-27T08:22:45.091Z_

Complete the research direction below with implementation details.

**Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.

{
  "title": "Potential-Valued Process Rewards for Principled Step-Level Credit Assignment",
  "core_problem": "Current PRMs are trained as step-correctness classifiers but heuristically repurposed as RL reward signals via aggregation (sum, min, product), causing either reward hacking or information loss. No principled framework connects PRM design to RL training quality, despite potential-based reward shaping (PBRS) theory guaranteeing policy invariance — a well-known result never practically implemented for step-level process rewards in mathematical reasoning.",
  "opportunity": "Three independent 2025-2026 findings converge: (1) the RARL survey confirms PBRS 'lacks practical PRM implementation' for reasoning RL; (2) DuaShepherd proves step correctness and step value (potential) are orthogonal signals — yet all existing PRMs train only on correctness; (3) PURE demonstrates that sum-form PRM aggregation causes training collapse, while min-form loses useful gradient information, but provides no theoretical justification for why min works better. Training a PRM as a state value function V(s_t) = P(correct | prefix₁:t) and deriving step rewards as potential differences r_t = γV(s_{t+1}) − V(s_t) would unify these findings: PBRS guarantees no policy distortion, value-function training requires only outcome labels (no expensive step annotations), and the framework naturally subsumes sum/min/product as suboptimal special cases with specific potential-function choices.",
  "landscape": "PRM-RL integration is the most contested frontier. PURE (2025) showed min-form credit assignment avoids reward hacking that collapses sum-form training 'even at the beginning,' but provides only empirical justification. TDRM (Sep 2025) applies TD learning to smooth PRM labels, achieving 23.7% improvement in tree-search and 20× data efficiency, but still requires step-level annotations and doesn't address the aggregation problem. CRM (2025) models step rewards as conditional probabilities P(correct|s_{1:t}) causally linked to outcomes, evaluating on best-of-N, beam search, AND RL — but lacks PBRS guarantees and still uses MC-estimated step labels. PRIME (ICLR 2026) extracts implicit process rewards from ORM token probabilities and is acknowledged as 'viewable as PBRS where q-value is the potential,' but uses heuristic extraction rather than explicit value function training. DuaShepherd (June 2025) separates correctness and potential reward heads, achieving SOTA on MATH500/ProcessBench, but evaluates only at inference time (best-of-N), not RL training. DVPO (ICLR 2026) pretrains a Global Value Model for general RLHF with 40% less GPU memory, but operates at response-level, not step-level process supervision. The RARL survey (Feb 2026) catalogs 47+ credit assignment methods and identifies the central open problem: 'Different aggregation schemes produce divergent policy behaviors, yet principled design guidelines remain absent.'",
  "inspired_by": "Gap: RARL survey's verified finding that PBRS 'lacks practical PRM implementation' despite theoretical support for policy invariance. Gap: DuaShepherd's proof that correctness and value are orthogonal, implying current correctness-only PRMs are insufficient for RL. Pattern: DVPO's 'pretrain value, not reward' principle applied to step-level reasoning. Combination: PRIME's PBRS connection (implicit, heuristic) + CRM's causal outcome alignment (no PBRS guarantee) + TDRM's temporal consistency (requires step labels) — unified through explicit outcome-supervised value function training with formal PBRS guarantees."
}

ADD these fields (keep all existing fields):
{
  "approach": "Proposed method — what you would actually do (3-5 sentences)",
  "resource_estimate": {
      "manual": {"gpu_hours": "...", "timeline": "...", "estimated_gpu_cost": "..."},
      "human_in_loop": {"gpu_hours": "...", "timeline": "...", "claude_api_cost": "...", "estimated_gpu_cost": "..."},
      "auto_research": {"gpu_hours": "...", "timeline": "...", "claude_api_cost": "...", "estimated_gpu_cost": "...", "speed_bottleneck": "..."}
  },
  "target_venues": ["Only venues with deadlines after 2026-05-27"],
  "level": "top-tier | solid | incremental",
  "key_references": ["Paper title (VENUE YEAR)", ...],
  "description": "Executive summary (150-200 words)",
  "project_name": "snake_case_identifier (max 30 chars)",
  "source": "web_research"
}

For key_references, verify with web_search that cited papers are real. Drop unverifiable ones.

**Model freshness rule**: When the approach involves pretrained models, use web_search to find current top-performing open-source models — do NOT default to models from your training data.

## 竞争论文 & Concurrent Work 搜索

在设计 approach 之前，必须确认没有人正在做同样的事情：
- 搜索 `{core_problem} 2026` 和 `{approach_keyword} {task} 2026`
- 在 arXiv 上搜索过去 3 个月的相关提交
- 在 OpenReview 上搜索即将举行的会议提交
- 如果发现高度相似的 concurrent work，必须在 landscape 中明确提及

## 可行性验证

1. 搜索类似方法的已有实现（GitHub）
2. 查找需要打败的具体 baseline 数字
3. 了解类似实验的硬件/数据需求

Output ONLY a single JSON object with ALL fields merged. No markdown fences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "89e1f898-be85-43fe-bddd-b707ae832929",
  "type": "user",
  "uuid": "caac4af5-0d12-48b8-af91-6402704a23ef",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:22:45.090Z_

```json
{
  "parentUuid": "caac4af5-0d12-48b8-af91-6402704a23ef",
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
  "uuid": "11683154-9c0b-4c43-bf49-2ef88a88fad9",
  "timestamp": "2026-05-27T08:22:45.090Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:22:45.090Z_

```json
{
  "parentUuid": "11683154-9c0b-4c43-bf49-2ef88a88fad9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fe0c0003-5691-489b-98d4-1f6565e0ef12",
  "timestamp": "2026-05-27T08:22:45.090Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
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
  "aiTitle": "Potential-valued process rewards for RL credit assignment",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0"
}
```

---

### Assistant

_source line 7 · 2026-05-27T08:22:49.701Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to complete a research direction with implementation details. I need to:

1. Search for concurrent work on PBRS + PRM for mathematical reasoning
2. Verify feasibility (existing implementations, baseline numbers, hardware requirements)
3. Find current top-performing open-source models
4. Verify conference deadlines after 2026-05-27
5. Verify key references are real
6. Output a complete JSON object

Let me start by launching several research agents in parallel to gather all the information I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe0c0003-5691-489b-98d4-1f6565e0ef12",
  "isSidechain": false,
  "requestId": "req_011CbSkVShx2gF3kRi6nCnyX",
  "type": "assistant",
  "uuid": "d64663b4-a78d-4e4f-9665-e254cb11c58c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpckMn7WiSog3D7KWEcXrZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2854,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1635,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2854
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

_source line 8 · 2026-05-27T08:22:50.291Z_

I'll launch several parallel research agents to gather all the information needed for this research direction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d64663b4-a78d-4e4f-9665-e254cb11c58c",
  "isSidechain": false,
  "requestId": "req_011CbSkVShx2gF3kRi6nCnyX",
  "type": "assistant",
  "uuid": "c9d292ee-ae54-4fc6-bfa5-f0dc9f04bc90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpckMn7WiSog3D7KWEcXrZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2854,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1635,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2854
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

_source line 9 · 2026-05-27T08:22:59.891Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01A4YMf54pth7Z6d3Po1Vr4Z`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search concurrent work PBRS+PRM",
  "prompt": "Search the web thoroughly for concurrent and recent work (2025-2026) on combining Potential-Based Reward Shaping (PBRS) with Process Reward Models (PRMs) for mathematical reasoning or step-level credit assignment in LLM RL training.\n\nSpecifically search for:\n1. \"potential based reward shaping\" \"process reward model\" 2025 OR 2026\n2. \"PBRS\" \"PRM\" mathematical reasoning 2026\n3. \"value function\" \"process reward\" \"reward shaping\" LLM 2026\n4. \"step-level credit assignment\" PBRS 2025 OR 2026\n5. Search arXiv for papers in the last 3 months (March-May 2026) about: process reward models + reward shaping, value-based process rewards, potential-based step rewards\n6. Search OpenReview for NeurIPS 2026, ICML 2026 submissions related to PBRS + PRM or value-function PRM\n\nAlso search for these specific papers and verify they exist (get venue, year, key results):\n- PURE (2025) - about PRM aggregation (sum vs min)\n- TDRM (Sep 2025) - TD learning for PRM labels\n- CRM (2025) - conditional process rewards\n- PRIME (ICLR 2026) - implicit process rewards from ORM\n- DuaShepherd (June 2025) - dual correctness and potential heads\n- DVPO (ICLR 2026) - global value model for RLHF\n- RARL survey (Feb 2026) - survey of 47+ credit assignment methods\n\nFor each paper found, report: title, authors, venue/year, key claim, and whether it's directly competing with the proposed idea of training a PRM as a value function V(s_t) and using PBRS potential differences as step rewards.\n\nReport any highly similar concurrent work that would threaten novelty."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9d292ee-ae54-4fc6-bfa5-f0dc9f04bc90",
  "isSidechain": false,
  "requestId": "req_011CbSkVShx2gF3kRi6nCnyX",
  "type": "assistant",
  "uuid": "3cf1205d-01d6-4093-90dc-60af51881db1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpckMn7WiSog3D7KWEcXrZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2854,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1635,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2854
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

_source line 10 · 2026-05-27T08:23:10.992Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Ra8MoX7by14HP111cEEjJM`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search baselines and implementations",
  "prompt": "Search the web for:\n\n1. EXISTING IMPLEMENTATIONS on GitHub:\n   - Search \"process reward model\" \"value function\" training code\n   - Search \"PBRS\" \"reward shaping\" LLM reinforcement learning implementation\n   - Search for PRIME, PURE, CRM, TDRM, DuaShepherd code repositories\n   - Search for open-source PRM training codebases (e.g., math-shepherd, prm800k)\n   - Search for RL training frameworks for LLM math reasoning (OpenRLHF, veRL, DeepSpeed-Chat, TRL)\n\n2. BASELINE NUMBERS to beat on key benchmarks:\n   - MATH500 accuracy with best-of-N using PRMs (what's SOTA?)\n   - GSM8K accuracy with PRM-guided search\n   - ProcessBench scores\n   - AIME 2024/2025 scores with PRM-guided methods\n   - RL training results: what accuracy improvements do PRIME, PURE, CRM achieve on MATH/GSM8K when used as RL rewards?\n\n3. HARDWARE/DATA REQUIREMENTS for similar experiments:\n   - How many GPUs did PRIME, PURE, TDRM use?\n   - What base models did they fine-tune? (7B, 8B, 70B?)\n   - What datasets were used? (PRM800K, Math-Shepherd, MetaMath, NuminaMath?)\n   - Training duration reported in these papers\n\n4. Current top open-source math reasoning models (as of May 2026):\n   - Search \"best open source math reasoning model 2026\"\n   - Search for Qwen3, Llama 4, DeepSeek-R2, or any newer models\n   - What's the current SOTA open-source model on MATH and AIME benchmarks?\n\nReport specific numbers wherever possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cf1205d-01d6-4093-90dc-60af51881db1",
  "isSidechain": false,
  "requestId": "req_011CbSkVShx2gF3kRi6nCnyX",
  "type": "assistant",
  "uuid": "d561ec27-2f5b-4cfc-bbe2-6393fd506faf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpckMn7WiSog3D7KWEcXrZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2854,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1635,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2854
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

_source line 11 · 2026-05-27T08:23:16.485Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MASLHr65MNaqYExrcXQJtd`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search venue deadlines 2026",
  "prompt": "Search the web for ML/AI conference paper submission deadlines that are AFTER May 27, 2026. I need exact dates.\n\nSearch for these specific venues:\n1. NeurIPS 2026 - paper submission deadline\n2. AAAI 2027 - paper submission deadline  \n3. ICLR 2027 - paper submission deadline\n4. ICML 2026 - paper submission deadline (likely already passed, verify)\n5. COLM 2026 - paper submission deadline\n6. EMNLP 2026 - paper submission deadline\n7. ACL 2027 - paper submission deadline\n8. NAACL 2027 - paper submission deadline\n9. CoRL 2026\n10. AISTATS 2027\n\nAlso search for:\n- \"NeurIPS 2026 deadline\"\n- \"AAAI 2027 deadline\"  \n- \"ICLR 2027 deadline\"\n- \"EMNLP 2026 deadline\"\n- \"COLM 2026 deadline\"\n- Any ML workshop deadlines in late 2026\n\nFor each venue, report:\n- Full name\n- Submission deadline (exact date)\n- Whether it's BEFORE or AFTER May 27, 2026\n- Conference dates\n- Venue tier (top-tier, solid, etc.)\n\nI need only venues whose deadlines have NOT yet passed as of May 27, 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d561ec27-2f5b-4cfc-bbe2-6393fd506faf",
  "isSidechain": false,
  "requestId": "req_011CbSkVShx2gF3kRi6nCnyX",
  "type": "assistant",
  "uuid": "c4459ded-81ca-442c-b602-b390e5fb5e27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpckMn7WiSog3D7KWEcXrZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2854,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1635,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2854
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

_source line 12 · 2026-05-27T08:24:53.939Z_

<details><summary>↩ Tool result · `toolu_01MASLHr65MNaqYExrcXQJtd`</summary>

```text
Now I have all the information I need. Here is the comprehensive report:

---

## ML/AI Conference Deadlines -- Status as of May 27, 2026

### DEADLINES ALREADY PASSED (before May 27, 2026)

| # | Conference | Full Name | Submission Deadline | Status | Tier |
|---|-----------|-----------|-------------------|--------|------|
| 1 | **ICML 2026** | International Conference on Machine Learning | Jan 28, 2026 | PASSED | Top-tier |
| 2 | **COLM 2026** | Conference on Language Modeling | Mar 31, 2026 (abstract: Mar 26) | PASSED | Solid (2nd year) |
| 3 | **NeurIPS 2026** | Neural Information Processing Systems | May 6, 2026 (abstract: May 4) | PASSED | Top-tier |
| 4 | **EMNLP 2026** | Conf. on Empirical Methods in NLP | May 25, 2026 (ARR deadline) | PASSED (by 2 days) | Top-tier (NLP) |

---

### DEADLINES STILL OPEN (after May 27, 2026)

| # | Conference | Full Name | Submission Deadline | Conference Dates | Location | Tier |
|---|-----------|-----------|-------------------|-----------------|----------|------|
| 1 | **CoRL 2026** | Conference on Robot Learning | **May 28, 2026** (EOD) | Nov 9-12, 2026 | Austin, TX, USA | Top-tier (robotics) |
| 2 | **AAAI 2027** | AAAI Conference on Artificial Intelligence | **Jul 28, 2026** (abstract: Jul 21) | Feb 16-23, 2027 | Montreal, Canada | Top-tier |
| 3 | **EACL 2027** | European Chapter of ACL | **Aug 3, 2026** (ARR deadline) | Mar 9-13, 2027 | Athens, Greece | Solid (NLP) |
| 4 | **ICLR 2027** | International Conference on Learning Representations | **~Sep 24, 2026** (estimated; abstract ~Sep 19) | Apr/May 2027 | TBA | Top-tier |
| 5 | **AISTATS 2027** | AI and Statistics | **~Oct 10, 2026** (estimated) | May 16-21, 2027 | Toronto, Canada | Solid |
| 6 | **CVPR 2027** | Computer Vision and Pattern Recognition | **~Nov 13, 2026** (estimated; abstract ~Nov 7) | Jun 14-20, 2027 | Nashville, TN, USA | Top-tier (vision) |

---

### DETAILS ON EACH OPEN VENUE

**1. CoRL 2026 -- URGENT (tomorrow!)**
- Deadline: May 28, 2026 EOD
- Camera-ready: Oct 12, 2026
- Conference: Nov 9 (workshops), Nov 10-12 (main), Austin TX
- Note: The organizers explicitly emphasized "the paper submission deadline is Thursday (5/28) EOD rather than Friday!"

**2. AAAI 2027**
- Author registration opens: Jun 17, 2026
- Paper submission opens: Jun 24, 2026
- Abstract deadline: Jul 21, 2026 (11:59 PM UTC-12)
- Full paper deadline: Jul 28, 2026 (11:59 PM UTC-12)
- Supplementary materials: Jul 31, 2026
- Phase 1 rejection notification: Sep 24, 2026
- Author feedback: Oct 19-25, 2026
- Final decision: Nov 30, 2026
- Conference: Feb 16-23, 2027, Montreal, Canada

**3. EACL 2027**
- ARR submission deadline: Aug 3, 2026 (11:59 PM AoE)
- Commitment deadline: Oct 11, 2026
- Conference: Mar 9-13, 2027, Athens, Greece
- Note: Corrected from an earlier announced date of Aug 6. This is the only viable ARR cycle for EACL 2027.

**4. ICLR 2027 (estimated)**
- Abstract: ~Sep 19, 2026 (estimated based on trybibby.com aggregator)
- Full paper: ~Sep 24, 2026 (estimated)
- Conference: Apr/May 2027
- Note: Official CFP not yet released. Dates are projected from prior-year patterns. ICLR 2026 had the same Sep 19/24 pattern.

**5. AISTATS 2027 (estimated)**
- Deadline: ~Oct 10, 2026 (estimated)
- Conference: May 16-21, 2027, Toronto, Canada
- Note: Official CFP not yet released.

**6. CVPR 2027 (estimated, bonus -- not originally requested)**
- Abstract: ~Nov 7, 2026 (estimated)
- Full paper: ~Nov 13, 2026 (estimated)
- Conference: Jun 14-20, 2027, Nashville, TN

---

### NOT YET ANNOUNCED

| Conference | Status |
|-----------|--------|
| **ACL 2027** | No dates announced. ACL uses ARR; the relevant ARR cycle will likely be late 2026 or early 2027. ACL 2026 used the Oct 2025 and Jan 2026 ARR cycles. |
| **NAACL 2027** | No dates announced. Historically held in Jun with Dec submission deadlines. |

---

### ARR (ACL Rolling Review) Upcoming Cycles

If you target NLP venues via ARR:
- **May 25, 2026 cycle** -- PASSED (feeds into EMNLP 2026, AACL 2026)
- **Aug 3, 2026 cycle** -- feeds into EACL 2027 (commitment deadline: Oct 11, 2026)
- **Oct 12, 2026 cycle** -- feeds into TBA venues (likely ACL 2027)

---

### NeurIPS 2026 Workshop Deadlines (upcoming)

While the main NeurIPS paper deadline has passed, workshop-related deadlines are still open:
- Workshop application deadline: **Jun 6, 2026**
- Workshop acceptance notifications: Jul 11, 2026
- Individual workshop paper deadlines will vary (typically Aug-Sep 2026)

Similarly, **ICML 2026 workshops** (Jul 10-11, 2026 in Seoul) have individual submission deadlines that may still be open.

---

### Summary: Your immediate targets by deadline order

1. **CoRL 2026** -- May 28, 2026 (TOMORROW)
2. **NeurIPS 2026 workshops** -- Jun 6, 2026 (proposals)
3. **AAAI 2027** -- Jul 28, 2026
4. **EACL 2027** (ARR) -- Aug 3, 2026
5. **ICLR 2027** -- ~Sep 24, 2026 (est.)
6. **AISTATS 2027** -- ~Oct 10, 2026 (est.)
7. **CVPR 2027** -- ~Nov 13, 2026 (est.)

Sources:
- [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates)
- [AAAI-27 Main Technical Track](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)
- [AAAI-27 Conference Page](https://aaai.org/conference/aaai/aaai-27/)
- [COLM 2026 Key Dates](https://colmweb.org/dates.html)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [CoRL 2026 Instructions for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [CoRL 2026 Homepage](https://www.corl.org/)
- [ICML 2026 Dates](https://icml.cc/Conferences/2026/Dates)
- [ICLR 2026 Dates (for pattern reference)](https://iclr.cc/Conferences/2026/Dates)
- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)
- [EACL 2027 Website](https://2027.eacl.org/)
- [EACL 2027 Date Correction (X/Twitter)](https://x.com/eaclmeeting/status/2051971432171688436)
- [AI/ML Conference Deadlines 2026-2027 (trybibby)](https://trybibby.com/conference-deadlines)
- [NeurIPS 2026 Submission Update (X/Twitter)](https://x.com/NeurIPSConf/status/2041303457554940336)

agentId: ad65e133cf0bbdf70 (use SendMessage with to: 'ad65e133cf0bbdf70' to continue this agent)
&lt;usage>total_tokens: 27146
tool_uses: 25
duration_ms: 97448&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4459ded-81ca-442c-b602-b390e5fb5e27",
  "isSidechain": false,
  "promptId": "89e1f898-be85-43fe-bddd-b707ae832929",
  "type": "user",
  "uuid": "d62ebd2d-80a4-4a07-bfb4-85363e7d1f6a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for ML/AI conference paper submission deadlines that are AFTER May 27, 2026. I need exact dates.\n\nSearch for these specific venues:\n1. NeurIPS 2026 - paper submission deadline\n2. AAAI 2027 - paper submission deadline  \n3. ICLR 2027 - paper submission deadline\n4. ICML 2026 - paper submission deadline (likely already passed, verify)\n5. COLM 2026 - paper submission deadline\n6. EMNLP 2026 - paper submission deadline\n7. ACL 2027 - paper submission deadline\n8. NAACL 2027 - paper submission deadline\n9. CoRL 2026\n10. AISTATS 2027\n\nAlso search for:\n- \"NeurIPS 2026 deadline\"\n- \"AAAI 2027 deadline\"  \n- \"ICLR 2027 deadline\"\n- \"EMNLP 2026 deadline\"\n- \"COLM 2026 deadline\"\n- Any ML workshop deadlines in late 2026\n\nFor each venue, report:\n- Full name\n- Submission deadline (exact date)\n- Whether it's BEFORE or AFTER May 27, 2026\n- Conference dates\n- Venue tier (top-tier, solid, etc.)\n\nI need only venues whose deadlines have NOT yet passed as of May 27, 2026.",
    "agentId": "ad65e133cf0bbdf70",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information I need. Here is the comprehensive report:\n\n---\n\n## ML/AI Conference Deadlines -- Status as of May 27, 2026\n\n### DEADLINES ALREADY PASSED (before May 27, 2026)\n\n| # | Conference | Full Name | Submission Deadline | Status | Tier |\n|---|-----------|-----------|-------------------|--------|------|\n| 1 | **ICML 2026** | International Conference on Machine Learning | Jan 28, 2026 | PASSED | Top-tier |\n| 2 | **COLM 2026** | Conference on Language Modeling | Mar 31, 2026 (abstract: Mar 26) | PASSED | Solid (2nd year) |\n| 3 | **NeurIPS 2026** | Neural Information Processing Systems | May 6, 2026 (abstract: May 4) | PASSED | Top-tier |\n| 4 | **EMNLP 2026** | Conf. on Empirical Methods in NLP | May 25, 2026 (ARR deadline) | PASSED (by 2 days) | Top-tier (NLP) |\n\n---\n\n### DEADLINES STILL OPEN (after May 27, 2026)\n\n| # | Conference | Full Name | Submission Deadline | Conference Dates | Location | Tier |\n|---|-----------|-----------|-------------------|-----------------|----------|------|\n| 1 | **CoRL 2026** | Conference on Robot Learning | **May 28, 2026** (EOD) | Nov 9-12, 2026 | Austin, TX, USA | Top-tier (robotics) |\n| 2 | **AAAI 2027** | AAAI Conference on Artificial Intelligence | **Jul 28, 2026** (abstract: Jul 21) | Feb 16-23, 2027 | Montreal, Canada | Top-tier |\n| 3 | **EACL 2027** | European Chapter of ACL | **Aug 3, 2026** (ARR deadline) | Mar 9-13, 2027 | Athens, Greece | Solid (NLP) |\n| 4 | **ICLR 2027** | International Conference on Learning Representations | **~Sep 24, 2026** (estimated; abstract ~Sep 19) | Apr/May 2027 | TBA | Top-tier |\n| 5 | **AISTATS 2027** | AI and Statistics | **~Oct 10, 2026** (estimated) | May 16-21, 2027 | Toronto, Canada | Solid |\n| 6 | **CVPR 2027** | Computer Vision and Pattern Recognition | **~Nov 13, 2026** (estimated; abstract ~Nov 7) | Jun 14-20, 2027 | Nashville, TN, USA | Top-tier (vision) |\n\n---\n\n### DETAILS ON EACH OPEN VENUE\n\n**1. CoRL 2026 -- URGENT (tomorrow!)**\n- Deadline: May 28, 2026 EOD\n- Camera-ready: Oct 12, 2026\n- Conference: Nov 9 (workshops), Nov 10-12 (main), Austin TX\n- Note: The organizers explicitly emphasized \"the paper submission deadline is Thursday (5/28) EOD rather than Friday!\"\n\n**2. AAAI 2027**\n- Author registration opens: Jun 17, 2026\n- Paper submission opens: Jun 24, 2026\n- Abstract deadline: Jul 21, 2026 (11:59 PM UTC-12)\n- Full paper deadline: Jul 28, 2026 (11:59 PM UTC-12)\n- Supplementary materials: Jul 31, 2026\n- Phase 1 rejection notification: Sep 24, 2026\n- Author feedback: Oct 19-25, 2026\n- Final decision: Nov 30, 2026\n- Conference: Feb 16-23, 2027, Montreal, Canada\n\n**3. EACL 2027**\n- ARR submission deadline: Aug 3, 2026 (11:59 PM AoE)\n- Commitment deadline: Oct 11, 2026\n- Conference: Mar 9-13, 2027, Athens, Greece\n- Note: Corrected from an earlier announced date of Aug 6. This is the only viable ARR cycle for EACL 2027.\n\n**4. ICLR 2027 (estimated)**\n- Abstract: ~Sep 19, 2026 (estimated based on trybibby.com aggregator)\n- Full paper: ~Sep 24, 2026 (estimated)\n- Conference: Apr/May 2027\n- Note: Official CFP not yet released. Dates are projected from prior-year patterns. ICLR 2026 had the same Sep 19/24 pattern.\n\n**5. AISTATS 2027 (estimated)**\n- Deadline: ~Oct 10, 2026 (estimated)\n- Conference: May 16-21, 2027, Toronto, Canada\n- Note: Official CFP not yet released.\n\n**6. CVPR 2027 (estimated, bonus -- not originally requested)**\n- Abstract: ~Nov 7, 2026 (estimated)\n- Full paper: ~Nov 13, 2026 (estimated)\n- Conference: Jun 14-20, 2027, Nashville, TN\n\n---\n\n### NOT YET ANNOUNCED\n\n| Conference | Status |\n|-----------|--------|\n| **ACL 2027** | No dates announced. ACL uses ARR; the relevant ARR cycle will likely be late 2026 or early 2027. ACL 2026 used the Oct 2025 and Jan 2026 ARR cycles. |\n| **NAACL 2027** | No dates announced. Historically held in Jun with Dec submission deadlines. |\n\n---\n\n### ARR (ACL Rolling Review) Upcoming Cycles\n\nIf you target NLP venues via ARR:\n- **May 25, 2026 cycle** -- PASSED (feeds into EMNLP 2026, AACL 2026)\n- **Aug 3, 2026 cycle** -- feeds into EACL 2027 (commitment deadline: Oct 11, 2026)\n- **Oct 12, 2026 cycle** -- feeds into TBA venues (likely ACL 2027)\n\n---\n\n### NeurIPS 2026 Workshop Deadlines (upcoming)\n\nWhile the main NeurIPS paper deadline has passed, workshop-related deadlines are still open:\n- Workshop application deadline: **Jun 6, 2026**\n- Workshop acceptance notifications: Jul 11, 2026\n- Individual workshop paper deadlines will vary (typically Aug-Sep 2026)\n\nSimilarly, **ICML 2026 workshops** (Jul 10-11, 2026 in Seoul) have individual submission deadlines that may still be open.\n\n---\n\n### Summary: Your immediate targets by deadline order\n\n1. **CoRL 2026** -- May 28, 2026 (TOMORROW)\n2. **NeurIPS 2026 workshops** -- Jun 6, 2026 (proposals)\n3. **AAAI 2027** -- Jul 28, 2026\n4. **EACL 2027** (ARR) -- Aug 3, 2026\n5. **ICLR 2027** -- ~Sep 24, 2026 (est.)\n6. **AISTATS 2027** -- ~Oct 10, 2026 (est.)\n7. **CVPR 2027** -- ~Nov 13, 2026 (est.)\n\nSources:\n- [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates)\n- [AAAI-27 Main Technical Track](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)\n- [AAAI-27 Conference Page](https://aaai.org/conference/aaai/aaai-27/)\n- [COLM 2026 Key Dates](https://colmweb.org/dates.html)\n- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n- [CoRL 2026 Instructions for Authors](https://www.corl.org/contributions/instruction-for-authors)\n- [CoRL 2026 Homepage](https://www.corl.org/)\n- [ICML 2026 Dates](https://icml.cc/Conferences/2026/Dates)\n- [ICLR 2026 Dates (for pattern reference)](https://iclr.cc/Conferences/2026/Dates)\n- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)\n- [EACL 2027 Website](https://2027.eacl.org/)\n- [EACL 2027 Date Correction (X/Twitter)](https://x.com/eaclmeeting/status/2051971432171688436)\n- [AI/ML Conference Deadlines 2026-2027 (trybibby)](https://trybibby.com/conference-deadlines)\n- [NeurIPS 2026 Submission Update (X/Twitter)](https://x.com/NeurIPSConf/status/2041303457554940336)"
      }
    ],
    "totalDurationMs": 97448,
    "totalTokens": 27146,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1595,
      "cache_read_input_tokens": 23256,
      "output_tokens": 2294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1595
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2294,
          "cache_read_input_tokens": 23256,
          "cache_creation_input_tokens": 1595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1595,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 25
    }
  },
  "sourceToolAssistantUUID": "c4459ded-81ca-442c-b602-b390e5fb5e27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Potential-Valued Process…",
  "leafUuid": "d62ebd2d-80a4-4a07-bfb4-85363e7d1f6a",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Potential-valued process rewards for RL credit assignment",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0"
}
```

---

### Tool result

_source line 15 · 2026-05-27T08:26:18.344Z_

<details><summary>↩ Tool result · `toolu_01Ra8MoX7by14HP111cEEjJM`</summary>

```text
Now I have comprehensive data. Here is the full report:

---

# Comprehensive Research Report: Process Reward Models, RL for Math Reasoning, and SOTA Benchmarks

## 1. EXISTING IMPLEMENTATIONS ON GITHUB

### Process Reward Model Repositories

| Project | Repository | Description |
|---------|-----------|-------------|
| **PRIME** | [github.com/PRIME-RL/PRIME](https://github.com/PRIME-RL/PRIME) | Process Reinforcement through Implicit Rewards. Online PRM updates using only policy rollouts and outcome labels. |
| **PURE** | [github.com/CJReinforce/PURE](https://github.com/CJReinforce/PURE) | "Stop Summation: Min-Form Credit Assignment Is All PRM Needs for Reasoning." Min-form value function formulation. |
| **TDRM** | [github.com/THUDM/TDRM](https://github.com/THUDM/TDRM) | Temporal Difference Reward Models. Smoother reward models via TD learning for both RL training and inference-time verification. |
| **DuaShepherd** | [arxiv.org/pdf/2506.17533](https://arxiv.org/pdf/2506.17533) | Integrates stepwise correctness (PRM800K-style) and potential rewards (Math-Shepherd-style) via multi-head multi-task learning. |
| **CRM** | [foundation-model-research.github.io/CRM](https://foundation-model-research.github.io/CRM/) | Conditional Reward Model. Frames step rewards as conditional probabilities linked to final outcome via chain rule. ArXiv: 2509.26578. |
| **PRM800K** | [github.com/openai/prm800k](https://github.com/openai/prm800k) | OpenAI's dataset of 800K step-level correctness labels on LLM solutions to MATH problems. |
| **Math-Shepherd** | Model: `math-shepherd-mistral-7b-prm` on HuggingFace | Label-free step-by-step verifier using Monte Carlo estimation. Mistral-7B base. |
| **Awesome-PRMs** | [github.com/RyanLiu112/Awesome-Process-Reward-Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models) | Curated list of PRM papers and resources. |
| **R-PRM** | [github.com/NJUNLP/R-PRM](https://github.com/NJUNLP/R-PRM) | Reasoning-Driven Process Reward Modeling. |
| **PRMBench** | [github.com/ssmisya/PRMBench](https://github.com/ssmisya/PRMBench) | ACL 2025 benchmark for evaluating PRMs (6,216 problems, 83,456 step-level labels). |

### RL Training Frameworks for LLM Math Reasoning

| Framework | Repository | Key Features |
|-----------|-----------|-------------|
| **OpenRLHF** | [github.com/OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) | Ray + vLLM + DeepSpeed. Supports PPO, GRPO, REINFORCE++, DAPO. Hybrid engine for GPU sharing. 3.1x faster than TRL. Supports VLM RLHF and async RL. |
| **veRL** | [github.com/verl-project/verl](https://github.com/verl-project/verl) | Supports FSDP, Megatron-LM, vLLM/SGLang. Algorithms: PPO, GRPO, ReMax, REINFORCE++, RLOO, PRIME. 3D-HybridEngine for memory efficiency. EuroSys 2025 paper. |
| **TRL** | HuggingFace TRL library | Accessible but slower (~3x slower than OpenRLHF). Good for prototyping. Stepwise supervision datasets available on HuggingFace. |
| **DeepSpeed-Chat** | Part of DeepSpeed | 3D parallelism support but less sophisticated orchestration than OpenRLHF/veRL. |

**Notable achievement with veRL:** DAPO algorithm trained with veRL achieved 50 points on AIME 2024 using Qwen2.5-32B, surpassing DeepSeek's GRPO performance. An RL scaling preview reached O1-level (70.0 pass@1 on AIME).

---

## 2. BASELINE NUMBERS TO BEAT

### MATH500 Accuracy (Best-of-N with PRMs)

| Method/Model | MATH500 Accuracy | Notes |
|-------------|-----------------|-------|
| MetaMath-Mistral-7B (greedy, no PRM) | 24.4% | Baseline |
| Mistral-7B + step-by-step PRM | ~87.2% (GSM8K) | PRM-guided BoN |
| PURE (Qwen2.5-Math-7B + RL) | **82.6%** pass@1 | Beats PRIME, SimpleRL |
| Qwen2.5-Math-PRM-7B | SOTA open-source 7B PRM | Used for BoN reranking |
| GLM-5 (Reasoning) | **92** on MATH500 | Current SOTA open-source (2026) |
| Qwen3-235B-A22B | **93.9%** on MATH500 | Large-scale MoE model |

### GSM8K Accuracy with PRM-Guided Search

| Method | GSM8K Accuracy | Notes |
|--------|---------------|-------|
| Mistral-7B + PRM (step-by-step) | 87.2% | PRM consistently beats ORM |
| EORM (Energy Outcome RM) | **92.8%** | 256 candidate chains |
| Gemma2-9B GenRM-CoT verifier | **93.4%** | Surpassed GPT-4 |

### ProcessBench Scores (F1 for Error Identification)

| Model | ProcessBench F1 |
|-------|----------------|
| Math-Shepherd | 28.9% |
| Skywork-PRM-7B | 42.1% |
| Qwen2.5-Math-PRM-7B | **73.5%** |
| ACTPRM (Active Learning) | **75.0%** |
| Qwen2.5-Math-PRM-72B | **78.3%** |
| o1-mini (proprietary) | 87.9% |
| Human performance | 83.8% |

### PRMBench Scores

| Model | PRMBench Score |
|-------|---------------|
| Gemini-2-Thinking | **68.8** (best model) |
| Human performance | 83.8 |
| Qwen2.5-Math-PRM-7B | SOTA for open-source 7B |

### AIME 2024/2025 Scores

| Model | AIME 2024 | AIME 2025 | Notes |
|-------|-----------|-----------|-------|
| Eurus-2-7B-PRIME (7B, RL) | ~26.7% pass@1 | -- | +20% over SFT on AMC/AIME |
| TDRM (Qwen2.5-Math-7B) | **36.7%** pass@1 | -- | Best among 7B PRM methods |
| DAPO (Qwen2.5-32B, veRL) | **50.0** | -- | Surpasses GRPO |
| Qwen3-235B-A22B | 85.7% | **81.5** (89.2% in some reports) | Large MoE |
| Seed1.5-Thinking | 86.7% | 74.0% | ByteDance |
| DeepSeek-R2 (32B) | -- | **92.7%** | MIT license, single GPU |
| o4-mini (proprietary) | **91.7%** (27.5/30) | -- | |
| Kimi K2.6 (1T params) | -- | -- | **96.4% on AIME 2026** |

### RL Training Improvements (PRIME, PURE, CRM as RL Rewards)

| Method | Base Model | Key Result |
|--------|-----------|------------|
| **PRIME** | Qwen2.5-Math-7B-Base | +16.7% avg across benchmarks over SFT; +20% on AMC/AIME; 2.5x sample efficiency gain over outcome-only RL; +6.9% on math over standard ORM-based RL |
| **PURE** | Qwen2.5-Math-7B | 82.6% MATH500, 82.5% AMC, 53.3% avg across 5 benchmarks. Beats PRIME and SimpleRL with <1/50th RL data or 1/5th compute |
| **TDRM** | Qwen2.5-Math-7B | Beats all other PRM methods by 0.9-4.4% average. 36.7% Pass@1 on AIME24. Works across 8 model variants (0.5B to 9B) |
| **CRM** | -- | Consistently outperforms existing RMs in BoN, beam search, and RL; mitigates reward hacking |

---

## 3. HARDWARE/DATA REQUIREMENTS

### Compute Requirements

| Project | Base Model | GPUs | Training Duration | Data Size |
|---------|-----------|------|-------------------|-----------|
| **PRIME** | Qwen2.5-Math-7B-Base | ~8x H100 (estimated) | ~36 hours | 230K SFT + 150K RL (1/10th of Qwen Math data) |
| **PURE** | Qwen2.5-Math-7B | 5-8 GPUs (first 4 for actor/ref/PRM, rest for vLLM rollout) | Significantly less than PRIME (<1/5th compute) | <1/50th RL data vs. PRIME |
| **TDRM** | Qwen2.5-Math-7B, GLM4-9B, DeepSeek-R1-Distill-Qwen variants | Not explicitly stated | Multiple runs (3x for variance) | Uses PRM800K-style data |
| **R1-Zero-Like (baseline reference)** | Qwen2.5-Math-7B | 8x A100 | 27 hours | MATH Level 3-5 questions |
| **INTELLECT-MATH (decentralized)** | Qwen2.5-Math-7B | Distributed/decentralized | Matched PRIME in 10x fewer GPU-hours (47 vs 592 RL steps) | -- |
| **General 7B RL training** | Any 7B | Min: 4 GPUs (16GB each); Ideal: 2-4 A100 (40GB) or 8x H100 | 8x H100 ~36 hrs, ~$870 (Lambda Cloud) | -- |

### Datasets Used

| Dataset | Size/Description | Used By |
|---------|-----------------|---------|
| **PRM800K** | 800K step-level human correctness labels on MATH solutions | DuaShepherd, TDRM, many PRMs |
| **Math-Shepherd** | Auto-annotated via Monte Carlo; Mistral-7B base | DuaShepherd, various PRMs |
| **MetaMath** | Augmented math training data | Used for Mistral-MetaMath-7B policy models |
| **NuminaMath** | Competition math dataset | Referenced in various PRM training pipelines |
| **HuggingFace TRL stepwise datasets** | Collection at `trl-lib/stepwise-supervision-datasets` | TRL-based training |

### Base Models Fine-Tuned

Most projects in this space use: **Qwen2.5-Math-7B** (dominant choice), Mistral-7B, GLM4-9B, GLM-Z1-9B, DeepSeek-R1-Distill-Qwen (1.5B/7B), Qwen2.5 (0.5B/1.5B). Larger experiments use Qwen2.5-32B and Qwen2.5-Math-72B for PRM training.

---

## 4. CURRENT TOP OPEN-SOURCE MATH REASONING MODELS (May 2026)

### Frontier Open-Source/Open-Weight Models

| Model | Parameters | AIME 2025 | AIME 2026 | MATH/MATH500 | License | Notes |
|-------|-----------|-----------|-----------|-------------|---------|-------|
| **DeepSeek-R2** | 32B dense | **92.7%** | -- | **98.1%** (beats o3's 97.0%) | MIT | Fits on single RTX 4090/A6000. 70% cheaper than Western frontier APIs |
| **Kimi K2.6** | 1T MoE | -- | **96.4%** | -- | Modified MIT | Strongest open-weight on AIME 2026. Ties GPT-5.5 on SWE-Bench |
| **Qwen3-235B-A22B** | 235B MoE (22B active) | ~89.2% | -- | **93.9%** (MATH500) | -- | Competitive with o1, o3-mini, Grok-3 |
| **GLM-5 (Reasoning)** | -- | -- | -- | **92** (MATH500) | -- | Highest MATH500 among open-weight |
| **DeepSeek-V4 Pro** | -- | -- | -- | -- | -- | Leads BenchLM.ai open-weight leaderboard (87 overall) |
| **Qwen3.5 397B** | 397B MoE | -- | -- | -- | -- | Reasoning-focused |
| **GLM-Z1-9B-0414** | 9B | -- | -- | -- | -- | Best lightweight math reasoner |

### Key Takeaway on AIME

AIME 2025 is effectively saturated: five models score 98%+ as of mid-2026. AIME 2026 is now the differentiating competition math benchmark. The gap between the best open-weight model (Kimi K2.6 at 96.4%) and the best proprietary model (GPT-5.4 at 99.2%) is under 3 points.

### Best Value Picks for Research

- **DeepSeek-R2 (32B)**: Best bang-for-buck. 98.1% MATH, 92.7% AIME 2025, runs on a single 24GB GPU, MIT license.
- **QwQ-32B**: Best balance of capability and accessibility.
- **GLM-Z1-9B-0414**: Best lightweight option proving small models can excel at math.

---

Sources:
- [PRIME-RL GitHub](https://github.com/PRIME-RL/PRIME)
- [PURE GitHub](https://github.com/CJReinforce/PURE)
- [TDRM GitHub](https://github.com/THUDM/TDRM)
- [PRIME Paper (arXiv 2502.01456)](https://arxiv.org/abs/2502.01456)
- [PURE Paper (arXiv 2504.15275)](https://arxiv.org/pdf/2504.15275)
- [TDRM Paper (arXiv 2509.15110)](https://arxiv.org/abs/2509.15110)
- [DuaShepherd Paper](https://arxiv.org/pdf/2506.17533)
- [CRM Project Page](https://foundation-model-research.github.io/CRM/)
- [CRM Paper (arXiv 2509.26578)](https://arxiv.org/pdf/2509.26578)
- [OpenAI PRM800K GitHub](https://github.com/openai/prm800k)
- [OpenRLHF GitHub](https://github.com/OpenRLHF/OpenRLHF)
- [veRL GitHub](https://github.com/verl-project/verl)
- [Awesome Process Reward Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)
- [PRMBench GitHub (ACL 2025)](https://github.com/ssmisya/PRMBench)
- [R-PRM GitHub](https://github.com/NJUNLP/R-PRM)
- [ProcessBench Paper (arXiv 2412.06559)](https://arxiv.org/pdf/2412.06559)
- [ACTPRM Paper (arXiv 2504.10559)](https://arxiv.org/pdf/2504.10559)
- [Qwen3 Technical Report](https://arxiv.org/pdf/2505.09388)
- [Qwen2.5-Math-PRM Blog](https://qwenlm.github.io/blog/qwen2.5-math-prm/)
- [DeepSeek-R2 Explained](https://decodethefuture.org/en/deepseek-r2-explained/)
- [Kimi K2.6 Review](https://www.buildfastwithai.com/blogs/kimi-k2-6-review-benchmarks)
- [AIME 2025 Leaderboard (Artificial Analysis)](https://artificialanalysis.ai/evaluations/aime-2025)
- [AIME 2024 Leaderboard](https://llm-stats.com/benchmarks/aime-2024)
- [MATH500 Leaderboard](https://llm-stats.com/benchmarks/math-500)
- [Anyscale: Open Source RL Libraries for LLMs](https://www.anyscale.com/blog/open-source-rl-libraries-for-llms)
- [PRIME HuggingFace Blog](https://huggingface.co/blog/ganqu/prime)
- [Top 10 Open-Source Reasoning Models 2026 (Clarifai)](https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026)
- [Best Open Source LLM for Math 2026 (SiliconFlow)](https://www.siliconflow.com/articles/en/best-open-source-LLM-for-math)
- [veRL + SkyPilot Blog](https://blog.skypilot.co/verl-rl-training/)
- [Eurus-2-7B-PRIME on HuggingFace](https://huggingface.co/PRIME-RL/Eurus-2-7B-PRIME)
- [FreePRM Paper](https://arxiv.org/pdf/2506.03570)
- [ThinkPRM Paper (arXiv 2504.16828)](https://arxiv.org/pdf/2504.16828)

agentId: a1c5eeecca6a51a13 (use SendMessage with to: 'a1c5eeecca6a51a13' to continue this agent)
&lt;usage>total_tokens: 38087
tool_uses: 28
duration_ms: 187349&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d561ec27-2f5b-4cfc-bbe2-6393fd506faf",
  "isSidechain": false,
  "promptId": "89e1f898-be85-43fe-bddd-b707ae832929",
  "type": "user",
  "uuid": "0394c623-4b92-4f55-aaa2-15062b71d321",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for:\n\n1. EXISTING IMPLEMENTATIONS on GitHub:\n   - Search \"process reward model\" \"value function\" training code\n   - Search \"PBRS\" \"reward shaping\" LLM reinforcement learning implementation\n   - Search for PRIME, PURE, CRM, TDRM, DuaShepherd code repositories\n   - Search for open-source PRM training codebases (e.g., math-shepherd, prm800k)\n   - Search for RL training frameworks for LLM math reasoning (OpenRLHF, veRL, DeepSpeed-Chat, TRL)\n\n2. BASELINE NUMBERS to beat on key benchmarks:\n   - MATH500 accuracy with best-of-N using PRMs (what's SOTA?)\n   - GSM8K accuracy with PRM-guided search\n   - ProcessBench scores\n   - AIME 2024/2025 scores with PRM-guided methods\n   - RL training results: what accuracy improvements do PRIME, PURE, CRM achieve on MATH/GSM8K when used as RL rewards?\n\n3. HARDWARE/DATA REQUIREMENTS for similar experiments:\n   - How many GPUs did PRIME, PURE, TDRM use?\n   - What base models did they fine-tune? (7B, 8B, 70B?)\n   - What datasets were used? (PRM800K, Math-Shepherd, MetaMath, NuminaMath?)\n   - Training duration reported in these papers\n\n4. Current top open-source math reasoning models (as of May 2026):\n   - Search \"best open source math reasoning model 2026\"\n   - Search for Qwen3, Llama 4, DeepSeek-R2, or any newer models\n   - What's the current SOTA open-source model on MATH and AIME benchmarks?\n\nReport specific numbers wherever possible.",
    "agentId": "a1c5eeecca6a51a13",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data. Here is the full report:\n\n---\n\n# Comprehensive Research Report: Process Reward Models, RL for Math Reasoning, and SOTA Benchmarks\n\n## 1. EXISTING IMPLEMENTATIONS ON GITHUB\n\n### Process Reward Model Repositories\n\n| Project | Repository | Description |\n|---------|-----------|-------------|\n| **PRIME** | [github.com/PRIME-RL/PRIME](https://github.com/PRIME-RL/PRIME) | Process Reinforcement through Implicit Rewards. Online PRM updates using only policy rollouts and outcome labels. |\n| **PURE** | [github.com/CJReinforce/PURE](https://github.com/CJReinforce/PURE) | \"Stop Summation: Min-Form Credit Assignment Is All PRM Needs for Reasoning.\" Min-form value function formulation. |\n| **TDRM** | [github.com/THUDM/TDRM](https://github.com/THUDM/TDRM) | Temporal Difference Reward Models. Smoother reward models via TD learning for both RL training and inference-time verification. |\n| **DuaShepherd** | [arxiv.org/pdf/2506.17533](https://arxiv.org/pdf/2506.17533) | Integrates stepwise correctness (PRM800K-style) and potential rewards (Math-Shepherd-style) via multi-head multi-task learning. |\n| **CRM** | [foundation-model-research.github.io/CRM](https://foundation-model-research.github.io/CRM/) | Conditional Reward Model. Frames step rewards as conditional probabilities linked to final outcome via chain rule. ArXiv: 2509.26578. |\n| **PRM800K** | [github.com/openai/prm800k](https://github.com/openai/prm800k) | OpenAI's dataset of 800K step-level correctness labels on LLM solutions to MATH problems. |\n| **Math-Shepherd** | Model: `math-shepherd-mistral-7b-prm` on HuggingFace | Label-free step-by-step verifier using Monte Carlo estimation. Mistral-7B base. |\n| **Awesome-PRMs** | [github.com/RyanLiu112/Awesome-Process-Reward-Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models) | Curated list of PRM papers and resources. |\n| **R-PRM** | [github.com/NJUNLP/R-PRM](https://github.com/NJUNLP/R-PRM) | Reasoning-Driven Process Reward Modeling. |\n| **PRMBench** | [github.com/ssmisya/PRMBench](https://github.com/ssmisya/PRMBench) | ACL 2025 benchmark for evaluating PRMs (6,216 problems, 83,456 step-level labels). |\n\n### RL Training Frameworks for LLM Math Reasoning\n\n| Framework | Repository | Key Features |\n|-----------|-----------|-------------|\n| **OpenRLHF** | [github.com/OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) | Ray + vLLM + DeepSpeed. Supports PPO, GRPO, REINFORCE++, DAPO. Hybrid engine for GPU sharing. 3.1x faster than TRL. Supports VLM RLHF and async RL. |\n| **veRL** | [github.com/verl-project/verl](https://github.com/verl-project/verl) | Supports FSDP, Megatron-LM, vLLM/SGLang. Algorithms: PPO, GRPO, ReMax, REINFORCE++, RLOO, PRIME. 3D-HybridEngine for memory efficiency. EuroSys 2025 paper. |\n| **TRL** | HuggingFace TRL library | Accessible but slower (~3x slower than OpenRLHF). Good for prototyping. Stepwise supervision datasets available on HuggingFace. |\n| **DeepSpeed-Chat** | Part of DeepSpeed | 3D parallelism support but less sophisticated orchestration than OpenRLHF/veRL. |\n\n**Notable achievement with veRL:** DAPO algorithm trained with veRL achieved 50 points on AIME 2024 using Qwen2.5-32B, surpassing DeepSeek's GRPO performance. An RL scaling preview reached O1-level (70.0 pass@1 on AIME).\n\n---\n\n## 2. BASELINE NUMBERS TO BEAT\n\n### MATH500 Accuracy (Best-of-N with PRMs)\n\n| Method/Model | MATH500 Accuracy | Notes |\n|-------------|-----------------|-------|\n| MetaMath-Mistral-7B (greedy, no PRM) | 24.4% | Baseline |\n| Mistral-7B + step-by-step PRM | ~87.2% (GSM8K) | PRM-guided BoN |\n| PURE (Qwen2.5-Math-7B + RL) | **82.6%** pass@1 | Beats PRIME, SimpleRL |\n| Qwen2.5-Math-PRM-7B | SOTA open-source 7B PRM | Used for BoN reranking |\n| GLM-5 (Reasoning) | **92** on MATH500 | Current SOTA open-source (2026) |\n| Qwen3-235B-A22B | **93.9%** on MATH500 | Large-scale MoE model |\n\n### GSM8K Accuracy with PRM-Guided Search\n\n| Method | GSM8K Accuracy | Notes |\n|--------|---------------|-------|\n| Mistral-7B + PRM (step-by-step) | 87.2% | PRM consistently beats ORM |\n| EORM (Energy Outcome RM) | **92.8%** | 256 candidate chains |\n| Gemma2-9B GenRM-CoT verifier | **93.4%** | Surpassed GPT-4 |\n\n### ProcessBench Scores (F1 for Error Identification)\n\n| Model | ProcessBench F1 |\n|-------|----------------|\n| Math-Shepherd | 28.9% |\n| Skywork-PRM-7B | 42.1% |\n| Qwen2.5-Math-PRM-7B | **73.5%** |\n| ACTPRM (Active Learning) | **75.0%** |\n| Qwen2.5-Math-PRM-72B | **78.3%** |\n| o1-mini (proprietary) | 87.9% |\n| Human performance | 83.8% |\n\n### PRMBench Scores\n\n| Model | PRMBench Score |\n|-------|---------------|\n| Gemini-2-Thinking | **68.8** (best model) |\n| Human performance | 83.8 |\n| Qwen2.5-Math-PRM-7B | SOTA for open-source 7B |\n\n### AIME 2024/2025 Scores\n\n| Model | AIME 2024 | AIME 2025 | Notes |\n|-------|-----------|-----------|-------|\n| Eurus-2-7B-PRIME (7B, RL) | ~26.7% pass@1 | -- | +20% over SFT on AMC/AIME |\n| TDRM (Qwen2.5-Math-7B) | **36.7%** pass@1 | -- | Best among 7B PRM methods |\n| DAPO (Qwen2.5-32B, veRL) | **50.0** | -- | Surpasses GRPO |\n| Qwen3-235B-A22B | 85.7% | **81.5** (89.2% in some reports) | Large MoE |\n| Seed1.5-Thinking | 86.7% | 74.0% | ByteDance |\n| DeepSeek-R2 (32B) | -- | **92.7%** | MIT license, single GPU |\n| o4-mini (proprietary) | **91.7%** (27.5/30) | -- | |\n| Kimi K2.6 (1T params) | -- | -- | **96.4% on AIME 2026** |\n\n### RL Training Improvements (PRIME, PURE, CRM as RL Rewards)\n\n| Method | Base Model | Key Result |\n|--------|-----------|------------|\n| **PRIME** | Qwen2.5-Math-7B-Base | +16.7% avg across benchmarks over SFT; +20% on AMC/AIME; 2.5x sample efficiency gain over outcome-only RL; +6.9% on math over standard ORM-based RL |\n| **PURE** | Qwen2.5-Math-7B | 82.6% MATH500, 82.5% AMC, 53.3% avg across 5 benchmarks. Beats PRIME and SimpleRL with <1/50th RL data or 1/5th compute |\n| **TDRM** | Qwen2.5-Math-7B | Beats all other PRM methods by 0.9-4.4% average. 36.7% Pass@1 on AIME24. Works across 8 model variants (0.5B to 9B) |\n| **CRM** | -- | Consistently outperforms existing RMs in BoN, beam search, and RL; mitigates reward hacking |\n\n---\n\n## 3. HARDWARE/DATA REQUIREMENTS\n\n### Compute Requirements\n\n| Project | Base Model | GPUs | Training Duration | Data Size |\n|---------|-----------|------|-------------------|-----------|\n| **PRIME** | Qwen2.5-Math-7B-Base | ~8x H100 (estimated) | ~36 hours | 230K SFT + 150K RL (1/10th of Qwen Math data) |\n| **PURE** | Qwen2.5-Math-7B | 5-8 GPUs (first 4 for actor/ref/PRM, rest for vLLM rollout) | Significantly less than PRIME (<1/5th compute) | <1/50th RL data vs. PRIME |\n| **TDRM** | Qwen2.5-Math-7B, GLM4-9B, DeepSeek-R1-Distill-Qwen variants | Not explicitly stated | Multiple runs (3x for variance) | Uses PRM800K-style data |\n| **R1-Zero-Like (baseline reference)** | Qwen2.5-Math-7B | 8x A100 | 27 hours | MATH Level 3-5 questions |\n| **INTELLECT-MATH (decentralized)** | Qwen2.5-Math-7B | Distributed/decentralized | Matched PRIME in 10x fewer GPU-hours (47 vs 592 RL steps) | -- |\n| **General 7B RL training** | Any 7B | Min: 4 GPUs (16GB each); Ideal: 2-4 A100 (40GB) or 8x H100 | 8x H100 ~36 hrs, ~$870 (Lambda Cloud) | -- |\n\n### Datasets Used\n\n| Dataset | Size/Description | Used By |\n|---------|-----------------|---------|\n| **PRM800K** | 800K step-level human correctness labels on MATH solutions | DuaShepherd, TDRM, many PRMs |\n| **Math-Shepherd** | Auto-annotated via Monte Carlo; Mistral-7B base | DuaShepherd, various PRMs |\n| **MetaMath** | Augmented math training data | Used for Mistral-MetaMath-7B policy models |\n| **NuminaMath** | Competition math dataset | Referenced in various PRM training pipelines |\n| **HuggingFace TRL stepwise datasets** | Collection at `trl-lib/stepwise-supervision-datasets` | TRL-based training |\n\n### Base Models Fine-Tuned\n\nMost projects in this space use: **Qwen2.5-Math-7B** (dominant choice), Mistral-7B, GLM4-9B, GLM-Z1-9B, DeepSeek-R1-Distill-Qwen (1.5B/7B), Qwen2.5 (0.5B/1.5B). Larger experiments use Qwen2.5-32B and Qwen2.5-Math-72B for PRM training.\n\n---\n\n## 4. CURRENT TOP OPEN-SOURCE MATH REASONING MODELS (May 2026)\n\n### Frontier Open-Source/Open-Weight Models\n\n| Model | Parameters | AIME 2025 | AIME 2026 | MATH/MATH500 | License | Notes |\n|-------|-----------|-----------|-----------|-------------|---------|-------|\n| **DeepSeek-R2** | 32B dense | **92.7%** | -- | **98.1%** (beats o3's 97.0%) | MIT | Fits on single RTX 4090/A6000. 70% cheaper than Western frontier APIs |\n| **Kimi K2.6** | 1T MoE | -- | **96.4%** | -- | Modified MIT | Strongest open-weight on AIME 2026. Ties GPT-5.5 on SWE-Bench |\n| **Qwen3-235B-A22B** | 235B MoE (22B active) | ~89.2% | -- | **93.9%** (MATH500) | -- | Competitive with o1, o3-mini, Grok-3 |\n| **GLM-5 (Reasoning)** | -- | -- | -- | **92** (MATH500) | -- | Highest MATH500 among open-weight |\n| **DeepSeek-V4 Pro** | -- | -- | -- | -- | -- | Leads BenchLM.ai open-weight leaderboard (87 overall) |\n| **Qwen3.5 397B** | 397B MoE | -- | -- | -- | -- | Reasoning-focused |\n| **GLM-Z1-9B-0414** | 9B | -- | -- | -- | -- | Best lightweight math reasoner |\n\n### Key Takeaway on AIME\n\nAIME 2025 is effectively saturated: five models score 98%+ as of mid-2026. AIME 2026 is now the differentiating competition math benchmark. The gap between the best open-weight model (Kimi K2.6 at 96.4%) and the best proprietary model (GPT-5.4 at 99.2%) is under 3 points.\n\n### Best Value Picks for Research\n\n- **DeepSeek-R2 (32B)**: Best bang-for-buck. 98.1% MATH, 92.7% AIME 2025, runs on a single 24GB GPU, MIT license.\n- **QwQ-32B**: Best balance of capability and accessibility.\n- **GLM-Z1-9B-0414**: Best lightweight option proving small models can excel at math.\n\n---\n\nSources:\n- [PRIME-RL GitHub](https://github.com/PRIME-RL/PRIME)\n- [PURE GitHub](https://github.com/CJReinforce/PURE)\n- [TDRM GitHub](https://github.com/THUDM/TDRM)\n- [PRIME Paper (arXiv 2502.01456)](https://arxiv.org/abs/2502.01456)\n- [PURE Paper (arXiv 2504.15275)](https://arxiv.org/pdf/2504.15275)\n- [TDRM Paper (arXiv 2509.15110)](https://arxiv.org/abs/2509.15110)\n- [DuaShepherd Paper](https://arxiv.org/pdf/2506.17533)\n- [CRM Project Page](https://foundation-model-research.github.io/CRM/)\n- [CRM Paper (arXiv 2509.26578)](https://arxiv.org/pdf/2509.26578)\n- [OpenAI PRM800K GitHub](https://github.com/openai/prm800k)\n- [OpenRLHF GitHub](https://github.com/OpenRLHF/OpenRLHF)\n- [veRL GitHub](https://github.com/verl-project/verl)\n- [Awesome Process Reward Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)\n- [PRMBench GitHub (ACL 2025)](https://github.com/ssmisya/PRMBench)\n- [R-PRM GitHub](https://github.com/NJUNLP/R-PRM)\n- [ProcessBench Paper (arXiv 2412.06559)](https://arxiv.org/pdf/2412.06559)\n- [ACTPRM Paper (arXiv 2504.10559)](https://arxiv.org/pdf/2504.10559)\n- [Qwen3 Technical Report](https://arxiv.org/pdf/2505.09388)\n- [Qwen2.5-Math-PRM Blog](https://qwenlm.github.io/blog/qwen2.5-math-prm/)\n- [DeepSeek-R2 Explained](https://decodethefuture.org/en/deepseek-r2-explained/)\n- [Kimi K2.6 Review](https://www.buildfastwithai.com/blogs/kimi-k2-6-review-benchmarks)\n- [AIME 2025 Leaderboard (Artificial Analysis)](https://artificialanalysis.ai/evaluations/aime-2025)\n- [AIME 2024 Leaderboard](https://llm-stats.com/benchmarks/aime-2024)\n- [MATH500 Leaderboard](https://llm-stats.com/benchmarks/math-500)\n- [Anyscale: Open Source RL Libraries for LLMs](https://www.anyscale.com/blog/open-source-rl-libraries-for-llms)\n- [PRIME HuggingFace Blog](https://huggingface.co/blog/ganqu/prime)\n- [Top 10 Open-Source Reasoning Models 2026 (Clarifai)](https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026)\n- [Best Open Source LLM for Math 2026 (SiliconFlow)](https://www.siliconflow.com/articles/en/best-open-source-LLM-for-math)\n- [veRL + SkyPilot Blog](https://blog.skypilot.co/verl-rl-training/)\n- [Eurus-2-7B-PRIME on HuggingFace](https://huggingface.co/PRIME-RL/Eurus-2-7B-PRIME)\n- [FreePRM Paper](https://arxiv.org/pdf/2506.03570)\n- [ThinkPRM Paper (arXiv 2504.16828)](https://arxiv.org/pdf/2504.16828)"
      }
    ],
    "totalDurationMs": 187349,
    "totalTokens": 38087,
    "totalToolUseCount": 28,
    "usage": {
      "input_tokens": 189,
      "cache_creation_input_tokens": 2460,
      "cache_read_input_tokens": 30579,
      "output_tokens": 4859,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2460
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 189,
          "output_tokens": 4859,
          "cache_read_input_tokens": 30579,
          "cache_creation_input_tokens": 2460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2460,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 28
    }
  },
  "sourceToolAssistantUUID": "d561ec27-2f5b-4cfc-bbe2-6393fd506faf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-27T08:28:58.000Z_

<details><summary>↩ Tool result · `toolu_01A4YMf54pth7Z6d3Po1Vr4Z`</summary>

```text
Now I have all the information needed. Let me compile the comprehensive report.

---

## Comprehensive Literature Search: PBRS + PRM for LLM RL Training (2025-2026)

### EXECUTIVE SUMMARY OF NOVELTY THREAT

**The most direct threat to novelty is SHAPE (April 2026, ACL 2026 Main).** It explicitly uses PBRS with potential differences gamma*Phi(s_{k+1}) - Phi(s_k) as step rewards for LLM mathematical reasoning, citing Ng et al. (1999). However, SHAPE estimates potentials via Monte Carlo rollouts (not a trained neural value function), and uses the shaped rewards only as advantage modifications in GRPO -- not as a standalone PRM training objective. **If the proposed idea trains a neural PRM as V(s_t) via TD learning and uses PBRS differences as step rewards, this is differentiated from SHAPE but must be carefully positioned against it.**

**TDRM (Sep 2025)** is the second-closest competitor. It explicitly trains a PRM as a value function V(s_t) using n-step TD updates with the Bellman equation. However, it does not frame the step rewards as PBRS potential differences -- it uses clamped TD targets as soft labels for cross-entropy training. The connection to PBRS is implicit, not explicit.

**PRIME (ICLR 2026)** derives implicit step rewards as value differences r(y_t) = v(y_{&lt;t+1}) - v(y_{&lt;t}), which is mathematically identical to PBRS with gamma=1. However, this is done via log-probability decomposition of an ORM, not by training a dedicated value network. PRIME does not cite Ng et al. (1999) or frame this as PBRS.

No paper found explicitly proposes the full pipeline of: (1) training a PRM as V(s_t) with TD/Bellman objectives, (2) deriving step rewards via PBRS formula F = gamma*V(s_{t+1}) - V(s_t), and (3) using these as process rewards during RL training. This specific combination appears novel but the individual components all exist in concurrent work.

---

### DETAILED PAPER-BY-PAPER ANALYSIS

#### 1. SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning
- **Authors:** Zhengyang Ai, Zikang Shan, Xiaodong Ai, Jingxian Tang, Hangkai Hu, Pinyan Lu (Huawei Taylor Lab)
- **Venue/Date:** arXiv April 2026; listed as "ACL 2026 Main"
- **Key claim:** Hierarchical credit assignment using PBRS at segment level + entropy redistribution at token level; achieves +3% accuracy with 30% fewer tokens
- **Technical details:** Defines potential Phi(s_k) as Monte Carlo success rate (m rollouts at each segment boundary). Uses PBRS formula F(s_k, s_{k+1}) = gamma_k * Phi(s_{k+1}) - Phi(s_k) with a length-dependent discount gamma_k that creates a "reasoning tax" penalizing verbosity. Explicitly cites Ng et al. (1999).
- **Difference from proposed idea:** SHAPE uses MC rollout-estimated potentials (training-free), NOT a trained neural value function. The potential is empirical success rate, not a learned V(s_t). Also, SHAPE applies PBRS to modify advantages in GRPO, not as a PRM training objective.
- **NOVELTY THREAT: HIGH** -- same theoretical framework (PBRS for LLM reasoning), but different implementation (MC vs. trained value function).

#### 2. TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference
- **Authors:** Dan Zhang, Min Cai, Jonathan Light, Ziniu Hu, Yisong Yue, Jie Tang (Tsinghua/Caltech)
- **Venue/Date:** arXiv Sep 2025
- **Key claim:** TD-trained PRMs improve Best-of-N by 6.6% and tree search by 23.7%; achieves comparable RL performance with 2.5k data vs 50.1k baseline
- **Technical details:** Trains PRM as V(s_t; phi) using n-step TD: v_t = sum_{k=0}^{n-1} gamma^k r_{t+k} + gamma^n V(s_{t+n}). Uses clamped TD target as soft label for cross-entropy loss. Cosine-based reward shaping for intermediate r_t. Output p_t (via sigmoid) represents state values that "serve as process rewards."
- **Difference from proposed idea:** TDRM trains V(s_t) with TD (same), but does NOT explicitly derive step rewards as PBRS differences V(s_{t+1}) - V(s_t). Instead, it uses the value estimates directly as process rewards. The PBRS connection is implicit.
- **NOVELTY THREAT: HIGH** -- trains PRM as value function with TD, but lacks the explicit PBRS framing.

#### 3. PRIME: Process Reinforcement through Implicit Rewards
- **Authors:** Ganqu Cui et al. (Tsinghua/various)
- **Venue/Date:** ICLR 2026 (conference paper). arXiv Feb 2025, revised Sep 2025.
- **Key claim:** +15.1% average improvement on reasoning benchmarks; online PRM updates with only outcome labels
- **Technical details:** Parameterizes reward as r_phi(y) = beta * log(pi_phi(y) / pi_ref(y)). Decomposes into token-level: r_phi(y_t) = beta * log(pi_phi(y_t|y_{&lt;t}) / pi_ref(y_t|y_{&lt;t})). Cumulative sum gives value: v_phi(y_{&lt;t+1}) = sum r_phi(y_i). Step reward = v_phi(y_{&lt;t+1}) - v_phi(y_{&lt;t}), which IS a potential difference with gamma=1.
- **Difference from proposed idea:** The value function arises from log-probability ratios (not a separately trained V network). No explicit PBRS framing or Ng et al. citation. The "value function" is a byproduct of the reward parameterization, not a deliberately trained critic.
- **NOVELTY THREAT: MEDIUM-HIGH** -- mathematically similar (step reward = value difference), but different mechanism (implicit via log-probs vs. explicit trained value function).

#### 4. SPAE: Step Potential Advantage Estimation
- **Authors:** Fei Wu, Zhenrong Zhang, Qikai Chang, Jianshu Zhang, Quan Liu, Jun Du
- **Venue/Date:** arXiv Jan 2026
- **Key claim:** Training-free step potential signal improves credit assignment; amplifies potential gains, penalizes drops
- **Technical details:** Defines Step Potential as Phi(tau) = 1.5*Acc*Conf + 0.5*Acc - Conf (composite of correctness and confidence). Uses potential differences Delta_Phi = Phi(tau_k) - Phi(tau_{k-1}). Cites Ng et al. (1999) as inspiration. Training-free probing (N=5 short continuations to estimate confidence/correctness).
- **Difference from proposed idea:** Training-free (no learned value function). Potential is a heuristic composite metric, not a principled V(s_t).
- **NOVELTY THREAT: MEDIUM** -- uses PBRS-inspired potential differences but without a trained model.

#### 5. PURE: Stop Summation: Min-Form Credit Assignment Is All PRM Needs
- **Authors:** Jie Cheng et al.
- **Venue/Date:** NeurIPS 2025
- **Key claim:** Min-form credit assignment (value = min of future rewards instead of sum) alleviates PRM-induced reward hacking
- **Technical details:** Replaces V(s_t) = sum gamma^k r_{t+k} with V(s_t) = min_{k>=t} r_k. Achieves comparable reasoning performance with only 30% of training steps.
- **Difference from proposed idea:** Redefines the value function aggregation, does not use PBRS. Orthogonal contribution.
- **NOVELTY THREAT: LOW** -- different approach entirely (min aggregation vs. PBRS differences).

#### 6. CRM: Linking Process to Outcome: Conditional Reward Modeling
- **Authors:** Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, Kan Ren
- **Venue/Date:** ICLR 2026 (accepted). arXiv Sep 2025, revised Feb 2026.
- **Key claim:** Frames step rewards as conditional probabilities linked to final outcome; more robust to reward hacking
- **Technical details:** Each step's reward is conditioned on preceding steps AND linked to outcome via conditional probability rules. Captures causal relationships among steps.
- **Difference from proposed idea:** Probabilistic framework, not value-function/PBRS. Orthogonal.
- **NOVELTY THREAT: LOW** -- different theoretical framework.

#### 7. DuaShepherd: Integrating Stepwise Correctness and Potential Rewards
- **Authors:** Yuanhao Wu, Juntong Song, Hanning Zhang, Tong Zhang, Cheng Niu
- **Venue/Date:** arXiv June 2025
- **Key claim:** Dual-head architecture combining correctness and potential signals outperforms either alone
- **Technical details:** Two heads: correctness (evaluates past step errors) and potential (estimates likelihood of reaching correct answer). Combined via multiplication R = R_correctness * R_potential (chain rule of probability). Potential is trained on Math-Shepherd labels.
- **Difference from proposed idea:** "Potential" here means forward-looking success probability, NOT PBRS potential. No potential differences used. Does not cite Ng et al. (1999).
- **NOVELTY THREAT: LOW** -- "potential" is used in a different sense.

#### 8. DVPO: Pretrain Value, Not Reward: Decoupled Value Policy Optimization
- **Authors:** Chenghua Huang et al. (Microsoft)
- **Venue/Date:** ICLR 2026 (poster). arXiv Feb 2025, revised Jan 2026.
- **Key claim:** Directly pretraining a Global Value Model (GVM) is informationally equivalent to training a reward model + online value learning, but simpler
- **Technical details:** GVM predicts return-to-go of partial answers. Frozen GVM serves as universal critic. Token-level credit assignment without critic drift.
- **Difference from proposed idea:** DVPO is for general RLHF (not math reasoning PRMs specifically). Trains a value model but does NOT derive step rewards via PBRS. Focuses on replacing reward models entirely, not augmenting PRMs.
- **NOVELTY THREAT: MEDIUM** -- shares the "train value function, not reward model" insight, but for RLHF, not PRM-based math reasoning. Does not use PBRS.

#### 9. PQM: Process Reward Model with Q-Value Rankings
- **Authors:** (WindyLee0822 on GitHub)
- **Venue/Date:** ICLR 2025
- **Key claim:** Reframes PRM as Q-value ranking problem; +11.6% on MATH500
- **Technical details:** Defines Q-value for each step as probability of correct final answer. Trains PRM to approximate optimal Q-value rankings via comparative loss.
- **Difference from proposed idea:** Uses Q-values not V(s_t); ranking-based loss not PBRS differences.
- **NOVELTY THREAT: LOW-MEDIUM** -- related MDP formalization but different mechanism.

#### 10. "Rewarding Progress" (PAV): Scaling Automated Process Verifiers
- **Authors:** (Google/CMU)
- **Venue/Date:** ICLR 2025
- **Key claim:** Process Advantage Verifiers (PAVs) that reward "progress" (change in success probability) are 5x more compute-efficient than ORMs
- **Technical details:** Step reward = change in prover policy's success rate before and after step. This is essentially V(s_{t+1}) - V(s_t) estimated via MC rollouts.
- **Difference from proposed idea:** PAV uses MC-estimated advantages (not a trained value function). The "progress" concept is closely related to PBRS differences but estimated differently.
- **NOVELTY THREAT: MEDIUM** -- same conceptual idea (step reward = change in value), but MC-estimated, not from a trained V(s_t).

#### 11. AgentPRM: Process Reward Models for LLM Agents
- **Authors:** (various)
- **Venue/Date:** ACM Web Conference 2026. arXiv Nov 2025.
- **Key claim:** TD + GAE for scalable PRM label generation; 8x more compute-efficient than baselines
- **Technical details:** Uses TD-based estimation combined with GAE to generate PRM training labels for agentic (not math reasoning) tasks.
- **Difference from proposed idea:** Focuses on agentic tasks, not math reasoning. Uses TD+GAE for label generation, not as the PRM training objective itself.
- **NOVELTY THREAT: LOW-MEDIUM** -- TD for PRM labels in a different domain.

#### 12. SSVPO: Sequential Shapley Value Policy Optimization
- **Authors:** (various)
- **Venue/Date:** ICLR 2026 (poster)
- **Key claim:** Game-theoretic (Shapley value) approach to step-level credit assignment; +11.6% on math benchmarks
- **Technical details:** Insertion MDP + Sequential Shapley Values measure each step's marginal contribution by reordering steps.
- **Novelty threat: LOW** -- completely different framework (game theory vs. PBRS).

#### 13. RTMC: Rollout-Tree Monte Carlo Step-Level Credit Assignment
- **Authors:** (various)
- **Venue/Date:** arXiv April 2026
- **Key claim:** Aggregates return statistics across rollouts sharing common states; +3.2pp on SWE-bench
- **Difference from proposed idea:** Monte Carlo tree-based, no trained value function, no PBRS.
- **NOVELTY THREAT: LOW**

#### 14. Survey: "From Reasoning to Agentic: Credit Assignment in RL for LLMs"
- **Authors:** Chenchen Zhang
- **Venue/Date:** arXiv April 2026
- **Coverage:** 47 methods (41 core + 6 enablers), 2024-early 2026
- **Key finding:** Taxonomy by granularity (token/segment/step/turn/multi-agent) x methodology (MC/TD/model-based/game-theoretic/information-theoretic). Discusses PBRS in reward semantics section. Covers TDRM, OVM, Math-Shepherd, PQM. Does NOT identify "PRM as V(s_t) + PBRS" as an explicit open problem or existing method -- suggesting the specific combination may still be novel.

#### 15. rePIRL: Learn PRM with Inverse RL for LLM Reasoning
- **Authors:** Xian Wu et al.
- **Venue/Date:** arXiv Feb 2026, revised May 2026
- **Key claim:** IRL framework for PRM learning; unifies online/offline PRM methods
- **NOVELTY THREAT: LOW** -- different framework (inverse RL, not PBRS).

#### 16. Bootstrapped Reward Shaping (BSRS)
- **Authors:** (various)
- **Venue/Date:** AAAI 2025. arXiv Jan 2025.
- **Key claim:** Uses agent's current V estimate as PBRS potential; convergence proofs for tabular case
- **Difference:** General RL method (Atari), not applied to LLM reasoning or PRMs.
- **NOVELTY THREAT: LOW** for direct competition, but relevant as a theoretical foundation.

#### 17. OVM: Outcome-supervised Value Models for Planning in Mathematical Reasoning
- **Venue/Date:** NAACL 2024 Findings
- **Key claim:** Outcome supervision trains a value model for intermediate steps; value focuses on unseen future outcomes
- **Difference:** Earlier work; uses value function but not PBRS differences. Precursor concept.
- **NOVELTY THREAT: LOW** (older work, no PBRS).

---

### PAPERS NOT FOUND / UNVERIFIABLE

- **"RARL survey (Feb 2026)"**: The survey found is "From Reasoning to Agentic" (April 2026), authored by Chenchen Zhang. It covers 47+ methods. I could not find a paper specifically titled "RARL" from Feb 2026. This may be the same survey under a different name, or the name may be incorrect.

---

### SUMMARY: NOVELTY ASSESSMENT

**What exists:**
- SHAPE (2026): PBRS with MC-estimated potentials for LLM reasoning (explicit PBRS)
- TDRM (2025): PRM trained as V(s_t) via TD (no explicit PBRS framing)
- PRIME (2025/ICLR 2026): Step rewards as value differences from log-prob decomposition (implicit PBRS)
- SPAE (2026): Training-free PBRS-inspired potential differences
- PAV (ICLR 2025): "Progress" = change in success probability (MC-estimated, conceptually PBRS)
- DVPO (ICLR 2026): Pretrained value model replaces reward model (general RLHF, not PBRS for math)
- BSRS (AAAI 2025): Agent's V estimate as PBRS potential (general RL, not LLMs)

**What appears to NOT exist (the gap):**
The specific proposal of (1) training a neural PRM explicitly as V(s_t) using TD/Bellman objectives, and then (2) deriving step-level process rewards via the classical PBRS formula F = gamma*V(s_{t+1}) - V(s_t), and (3) using these as dense rewards during LLM RL training for math reasoning -- with formal policy-invariance guarantees from Ng et al. (1999) -- does not appear as a single unified contribution in any paper found.

**Key differentiation points to emphasize:**
1. vs. SHAPE: Trained neural V(s_t) vs. MC rollout estimates (more scalable, no inference-time rollouts needed)
2. vs. TDRM: Explicit PBRS framing with policy-invariance guarantees vs. ad-hoc TD labels
3. vs. PRIME: Dedicated value network vs. implicit log-probability decomposition (potentially more expressive)
4. vs. PAV: Amortized learned potentials vs. costly per-step MC estimation
5. vs. DVPO: Math reasoning focus with PRM integration vs. general RLHF

**Risk level: MODERATE.** The individual components are all well-established in concurrent work, and the conceptual connection between PRMs and PBRS is noted in at least one survey. The specific combination is novel but incremental. SHAPE is the most dangerous competitor as it already applies PBRS to LLM reasoning, just with MC potentials instead of a trained network.

Sources:
- [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation](https://arxiv.org/abs/2604.06636)
- [TDRM: Smooth Reward Models with Temporal Difference](https://arxiv.org/abs/2509.15110)
- [PRIME: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)
- [SPAE: Step Potential Advantage Estimation](https://arxiv.org/abs/2601.03823)
- [PURE: Stop Summation (Min-Form Credit Assignment)](https://arxiv.org/abs/2504.15275)
- [CRM: Conditional Reward Modeling](https://arxiv.org/abs/2509.26578)
- [DuaShepherd](https://arxiv.org/abs/2506.17533)
- [DVPO: Decoupled Value Policy Optimization](https://arxiv.org/abs/2502.16944)
- [PQM: Process Reward Model with Q-Value Rankings](https://arxiv.org/abs/2410.11287)
- [Rewarding Progress (PAV)](https://openreview.net/forum?id=A6Y7AqlzLW)
- [AgentPRM](https://arxiv.org/abs/2511.08325)
- [SSVPO](https://openreview.net/forum?id=g33DGvnHYd)
- [RTMC](https://arxiv.org/abs/2604.11037)
- [Credit Assignment Survey](https://arxiv.org/abs/2604.09459)
- [rePIRL](https://arxiv.org/abs/2602.07832)
- [Bootstrapped Reward Shaping](https://arxiv.org/abs/2501.00989)
- [Reward Modeling Survey (Feb 2026)](https://arxiv.org/abs/2602.09305)
- [Free Process Rewards without Process Labels](https://openreview.net/forum?id=8ThnPFhGm8)
- [PROGRS](https://arxiv.org/abs/2604.02341)
- [From Scalar Rewards to Potential Trends (SLOPE)](https://arxiv.org/abs/2602.03201)
- [Calculus on MDPs: Potential Shaping as a Gradient](https://arxiv.org/abs/2208.09570)

agentId: a9806166cb2ac6c4e (use SendMessage with to: 'a9806166cb2ac6c4e' to continue this agent)
&lt;usage>total_tokens: 59120
tool_uses: 59
duration_ms: 358101&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cf1205d-01d6-4093-90dc-60af51881db1",
  "isSidechain": false,
  "promptId": "89e1f898-be85-43fe-bddd-b707ae832929",
  "type": "user",
  "uuid": "f0583dd8-1b90-43b5-91fe-587fc32587c1",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web thoroughly for concurrent and recent work (2025-2026) on combining Potential-Based Reward Shaping (PBRS) with Process Reward Models (PRMs) for mathematical reasoning or step-level credit assignment in LLM RL training.\n\nSpecifically search for:\n1. \"potential based reward shaping\" \"process reward model\" 2025 OR 2026\n2. \"PBRS\" \"PRM\" mathematical reasoning 2026\n3. \"value function\" \"process reward\" \"reward shaping\" LLM 2026\n4. \"step-level credit assignment\" PBRS 2025 OR 2026\n5. Search arXiv for papers in the last 3 months (March-May 2026) about: process reward models + reward shaping, value-based process rewards, potential-based step rewards\n6. Search OpenReview for NeurIPS 2026, ICML 2026 submissions related to PBRS + PRM or value-function PRM\n\nAlso search for these specific papers and verify they exist (get venue, year, key results):\n- PURE (2025) - about PRM aggregation (sum vs min)\n- TDRM (Sep 2025) - TD learning for PRM labels\n- CRM (2025) - conditional process rewards\n- PRIME (ICLR 2026) - implicit process rewards from ORM\n- DuaShepherd (June 2025) - dual correctness and potential heads\n- DVPO (ICLR 2026) - global value model for RLHF\n- RARL survey (Feb 2026) - survey of 47+ credit assignment methods\n\nFor each paper found, report: title, authors, venue/year, key claim, and whether it's directly competing with the proposed idea of training a PRM as a value function V(s_t) and using PBRS potential differences as step rewards.\n\nReport any highly similar concurrent work that would threaten novelty.",
    "agentId": "a9806166cb2ac6c4e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Let me compile the comprehensive report.\n\n---\n\n## Comprehensive Literature Search: PBRS + PRM for LLM RL Training (2025-2026)\n\n### EXECUTIVE SUMMARY OF NOVELTY THREAT\n\n**The most direct threat to novelty is SHAPE (April 2026, ACL 2026 Main).** It explicitly uses PBRS with potential differences gamma*Phi(s_{k+1}) - Phi(s_k) as step rewards for LLM mathematical reasoning, citing Ng et al. (1999). However, SHAPE estimates potentials via Monte Carlo rollouts (not a trained neural value function), and uses the shaped rewards only as advantage modifications in GRPO -- not as a standalone PRM training objective. **If the proposed idea trains a neural PRM as V(s_t) via TD learning and uses PBRS differences as step rewards, this is differentiated from SHAPE but must be carefully positioned against it.**\n\n**TDRM (Sep 2025)** is the second-closest competitor. It explicitly trains a PRM as a value function V(s_t) using n-step TD updates with the Bellman equation. However, it does not frame the step rewards as PBRS potential differences -- it uses clamped TD targets as soft labels for cross-entropy training. The connection to PBRS is implicit, not explicit.\n\n**PRIME (ICLR 2026)** derives implicit step rewards as value differences r(y_t) = v(y_{&lt;t+1}) - v(y_{&lt;t}), which is mathematically identical to PBRS with gamma=1. However, this is done via log-probability decomposition of an ORM, not by training a dedicated value network. PRIME does not cite Ng et al. (1999) or frame this as PBRS.\n\nNo paper found explicitly proposes the full pipeline of: (1) training a PRM as V(s_t) with TD/Bellman objectives, (2) deriving step rewards via PBRS formula F = gamma*V(s_{t+1}) - V(s_t), and (3) using these as process rewards during RL training. This specific combination appears novel but the individual components all exist in concurrent work.\n\n---\n\n### DETAILED PAPER-BY-PAPER ANALYSIS\n\n#### 1. SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning\n- **Authors:** Zhengyang Ai, Zikang Shan, Xiaodong Ai, Jingxian Tang, Hangkai Hu, Pinyan Lu (Huawei Taylor Lab)\n- **Venue/Date:** arXiv April 2026; listed as \"ACL 2026 Main\"\n- **Key claim:** Hierarchical credit assignment using PBRS at segment level + entropy redistribution at token level; achieves +3% accuracy with 30% fewer tokens\n- **Technical details:** Defines potential Phi(s_k) as Monte Carlo success rate (m rollouts at each segment boundary). Uses PBRS formula F(s_k, s_{k+1}) = gamma_k * Phi(s_{k+1}) - Phi(s_k) with a length-dependent discount gamma_k that creates a \"reasoning tax\" penalizing verbosity. Explicitly cites Ng et al. (1999).\n- **Difference from proposed idea:** SHAPE uses MC rollout-estimated potentials (training-free), NOT a trained neural value function. The potential is empirical success rate, not a learned V(s_t). Also, SHAPE applies PBRS to modify advantages in GRPO, not as a PRM training objective.\n- **NOVELTY THREAT: HIGH** -- same theoretical framework (PBRS for LLM reasoning), but different implementation (MC vs. trained value function).\n\n#### 2. TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference\n- **Authors:** Dan Zhang, Min Cai, Jonathan Light, Ziniu Hu, Yisong Yue, Jie Tang (Tsinghua/Caltech)\n- **Venue/Date:** arXiv Sep 2025\n- **Key claim:** TD-trained PRMs improve Best-of-N by 6.6% and tree search by 23.7%; achieves comparable RL performance with 2.5k data vs 50.1k baseline\n- **Technical details:** Trains PRM as V(s_t; phi) using n-step TD: v_t = sum_{k=0}^{n-1} gamma^k r_{t+k} + gamma^n V(s_{t+n}). Uses clamped TD target as soft label for cross-entropy loss. Cosine-based reward shaping for intermediate r_t. Output p_t (via sigmoid) represents state values that \"serve as process rewards.\"\n- **Difference from proposed idea:** TDRM trains V(s_t) with TD (same), but does NOT explicitly derive step rewards as PBRS differences V(s_{t+1}) - V(s_t). Instead, it uses the value estimates directly as process rewards. The PBRS connection is implicit.\n- **NOVELTY THREAT: HIGH** -- trains PRM as value function with TD, but lacks the explicit PBRS framing.\n\n#### 3. PRIME: Process Reinforcement through Implicit Rewards\n- **Authors:** Ganqu Cui et al. (Tsinghua/various)\n- **Venue/Date:** ICLR 2026 (conference paper). arXiv Feb 2025, revised Sep 2025.\n- **Key claim:** +15.1% average improvement on reasoning benchmarks; online PRM updates with only outcome labels\n- **Technical details:** Parameterizes reward as r_phi(y) = beta * log(pi_phi(y) / pi_ref(y)). Decomposes into token-level: r_phi(y_t) = beta * log(pi_phi(y_t|y_{&lt;t}) / pi_ref(y_t|y_{&lt;t})). Cumulative sum gives value: v_phi(y_{&lt;t+1}) = sum r_phi(y_i). Step reward = v_phi(y_{&lt;t+1}) - v_phi(y_{&lt;t}), which IS a potential difference with gamma=1.\n- **Difference from proposed idea:** The value function arises from log-probability ratios (not a separately trained V network). No explicit PBRS framing or Ng et al. citation. The \"value function\" is a byproduct of the reward parameterization, not a deliberately trained critic.\n- **NOVELTY THREAT: MEDIUM-HIGH** -- mathematically similar (step reward = value difference), but different mechanism (implicit via log-probs vs. explicit trained value function).\n\n#### 4. SPAE: Step Potential Advantage Estimation\n- **Authors:** Fei Wu, Zhenrong Zhang, Qikai Chang, Jianshu Zhang, Quan Liu, Jun Du\n- **Venue/Date:** arXiv Jan 2026\n- **Key claim:** Training-free step potential signal improves credit assignment; amplifies potential gains, penalizes drops\n- **Technical details:** Defines Step Potential as Phi(tau) = 1.5*Acc*Conf + 0.5*Acc - Conf (composite of correctness and confidence). Uses potential differences Delta_Phi = Phi(tau_k) - Phi(tau_{k-1}). Cites Ng et al. (1999) as inspiration. Training-free probing (N=5 short continuations to estimate confidence/correctness).\n- **Difference from proposed idea:** Training-free (no learned value function). Potential is a heuristic composite metric, not a principled V(s_t).\n- **NOVELTY THREAT: MEDIUM** -- uses PBRS-inspired potential differences but without a trained model.\n\n#### 5. PURE: Stop Summation: Min-Form Credit Assignment Is All PRM Needs\n- **Authors:** Jie Cheng et al.\n- **Venue/Date:** NeurIPS 2025\n- **Key claim:** Min-form credit assignment (value = min of future rewards instead of sum) alleviates PRM-induced reward hacking\n- **Technical details:** Replaces V(s_t) = sum gamma^k r_{t+k} with V(s_t) = min_{k>=t} r_k. Achieves comparable reasoning performance with only 30% of training steps.\n- **Difference from proposed idea:** Redefines the value function aggregation, does not use PBRS. Orthogonal contribution.\n- **NOVELTY THREAT: LOW** -- different approach entirely (min aggregation vs. PBRS differences).\n\n#### 6. CRM: Linking Process to Outcome: Conditional Reward Modeling\n- **Authors:** Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, Kan Ren\n- **Venue/Date:** ICLR 2026 (accepted). arXiv Sep 2025, revised Feb 2026.\n- **Key claim:** Frames step rewards as conditional probabilities linked to final outcome; more robust to reward hacking\n- **Technical details:** Each step's reward is conditioned on preceding steps AND linked to outcome via conditional probability rules. Captures causal relationships among steps.\n- **Difference from proposed idea:** Probabilistic framework, not value-function/PBRS. Orthogonal.\n- **NOVELTY THREAT: LOW** -- different theoretical framework.\n\n#### 7. DuaShepherd: Integrating Stepwise Correctness and Potential Rewards\n- **Authors:** Yuanhao Wu, Juntong Song, Hanning Zhang, Tong Zhang, Cheng Niu\n- **Venue/Date:** arXiv June 2025\n- **Key claim:** Dual-head architecture combining correctness and potential signals outperforms either alone\n- **Technical details:** Two heads: correctness (evaluates past step errors) and potential (estimates likelihood of reaching correct answer). Combined via multiplication R = R_correctness * R_potential (chain rule of probability). Potential is trained on Math-Shepherd labels.\n- **Difference from proposed idea:** \"Potential\" here means forward-looking success probability, NOT PBRS potential. No potential differences used. Does not cite Ng et al. (1999).\n- **NOVELTY THREAT: LOW** -- \"potential\" is used in a different sense.\n\n#### 8. DVPO: Pretrain Value, Not Reward: Decoupled Value Policy Optimization\n- **Authors:** Chenghua Huang et al. (Microsoft)\n- **Venue/Date:** ICLR 2026 (poster). arXiv Feb 2025, revised Jan 2026.\n- **Key claim:** Directly pretraining a Global Value Model (GVM) is informationally equivalent to training a reward model + online value learning, but simpler\n- **Technical details:** GVM predicts return-to-go of partial answers. Frozen GVM serves as universal critic. Token-level credit assignment without critic drift.\n- **Difference from proposed idea:** DVPO is for general RLHF (not math reasoning PRMs specifically). Trains a value model but does NOT derive step rewards via PBRS. Focuses on replacing reward models entirely, not augmenting PRMs.\n- **NOVELTY THREAT: MEDIUM** -- shares the \"train value function, not reward model\" insight, but for RLHF, not PRM-based math reasoning. Does not use PBRS.\n\n#### 9. PQM: Process Reward Model with Q-Value Rankings\n- **Authors:** (WindyLee0822 on GitHub)\n- **Venue/Date:** ICLR 2025\n- **Key claim:** Reframes PRM as Q-value ranking problem; +11.6% on MATH500\n- **Technical details:** Defines Q-value for each step as probability of correct final answer. Trains PRM to approximate optimal Q-value rankings via comparative loss.\n- **Difference from proposed idea:** Uses Q-values not V(s_t); ranking-based loss not PBRS differences.\n- **NOVELTY THREAT: LOW-MEDIUM** -- related MDP formalization but different mechanism.\n\n#### 10. \"Rewarding Progress\" (PAV): Scaling Automated Process Verifiers\n- **Authors:** (Google/CMU)\n- **Venue/Date:** ICLR 2025\n- **Key claim:** Process Advantage Verifiers (PAVs) that reward \"progress\" (change in success probability) are 5x more compute-efficient than ORMs\n- **Technical details:** Step reward = change in prover policy's success rate before and after step. This is essentially V(s_{t+1}) - V(s_t) estimated via MC rollouts.\n- **Difference from proposed idea:** PAV uses MC-estimated advantages (not a trained value function). The \"progress\" concept is closely related to PBRS differences but estimated differently.\n- **NOVELTY THREAT: MEDIUM** -- same conceptual idea (step reward = change in value), but MC-estimated, not from a trained V(s_t).\n\n#### 11. AgentPRM: Process Reward Models for LLM Agents\n- **Authors:** (various)\n- **Venue/Date:** ACM Web Conference 2026. arXiv Nov 2025.\n- **Key claim:** TD + GAE for scalable PRM label generation; 8x more compute-efficient than baselines\n- **Technical details:** Uses TD-based estimation combined with GAE to generate PRM training labels for agentic (not math reasoning) tasks.\n- **Difference from proposed idea:** Focuses on agentic tasks, not math reasoning. Uses TD+GAE for label generation, not as the PRM training objective itself.\n- **NOVELTY THREAT: LOW-MEDIUM** -- TD for PRM labels in a different domain.\n\n#### 12. SSVPO: Sequential Shapley Value Policy Optimization\n- **Authors:** (various)\n- **Venue/Date:** ICLR 2026 (poster)\n- **Key claim:** Game-theoretic (Shapley value) approach to step-level credit assignment; +11.6% on math benchmarks\n- **Technical details:** Insertion MDP + Sequential Shapley Values measure each step's marginal contribution by reordering steps.\n- **Novelty threat: LOW** -- completely different framework (game theory vs. PBRS).\n\n#### 13. RTMC: Rollout-Tree Monte Carlo Step-Level Credit Assignment\n- **Authors:** (various)\n- **Venue/Date:** arXiv April 2026\n- **Key claim:** Aggregates return statistics across rollouts sharing common states; +3.2pp on SWE-bench\n- **Difference from proposed idea:** Monte Carlo tree-based, no trained value function, no PBRS.\n- **NOVELTY THREAT: LOW**\n\n#### 14. Survey: \"From Reasoning to Agentic: Credit Assignment in RL for LLMs\"\n- **Authors:** Chenchen Zhang\n- **Venue/Date:** arXiv April 2026\n- **Coverage:** 47 methods (41 core + 6 enablers), 2024-early 2026\n- **Key finding:** Taxonomy by granularity (token/segment/step/turn/multi-agent) x methodology (MC/TD/model-based/game-theoretic/information-theoretic). Discusses PBRS in reward semantics section. Covers TDRM, OVM, Math-Shepherd, PQM. Does NOT identify \"PRM as V(s_t) + PBRS\" as an explicit open problem or existing method -- suggesting the specific combination may still be novel.\n\n#### 15. rePIRL: Learn PRM with Inverse RL for LLM Reasoning\n- **Authors:** Xian Wu et al.\n- **Venue/Date:** arXiv Feb 2026, revised May 2026\n- **Key claim:** IRL framework for PRM learning; unifies online/offline PRM methods\n- **NOVELTY THREAT: LOW** -- different framework (inverse RL, not PBRS).\n\n#### 16. Bootstrapped Reward Shaping (BSRS)\n- **Authors:** (various)\n- **Venue/Date:** AAAI 2025. arXiv Jan 2025.\n- **Key claim:** Uses agent's current V estimate as PBRS potential; convergence proofs for tabular case\n- **Difference:** General RL method (Atari), not applied to LLM reasoning or PRMs.\n- **NOVELTY THREAT: LOW** for direct competition, but relevant as a theoretical foundation.\n\n#### 17. OVM: Outcome-supervised Value Models for Planning in Mathematical Reasoning\n- **Venue/Date:** NAACL 2024 Findings\n- **Key claim:** Outcome supervision trains a value model for intermediate steps; value focuses on unseen future outcomes\n- **Difference:** Earlier work; uses value function but not PBRS differences. Precursor concept.\n- **NOVELTY THREAT: LOW** (older work, no PBRS).\n\n---\n\n### PAPERS NOT FOUND / UNVERIFIABLE\n\n- **\"RARL survey (Feb 2026)\"**: The survey found is \"From Reasoning to Agentic\" (April 2026), authored by Chenchen Zhang. It covers 47+ methods. I could not find a paper specifically titled \"RARL\" from Feb 2026. This may be the same survey under a different name, or the name may be incorrect.\n\n---\n\n### SUMMARY: NOVELTY ASSESSMENT\n\n**What exists:**\n- SHAPE (2026): PBRS with MC-estimated potentials for LLM reasoning (explicit PBRS)\n- TDRM (2025): PRM trained as V(s_t) via TD (no explicit PBRS framing)\n- PRIME (2025/ICLR 2026): Step rewards as value differences from log-prob decomposition (implicit PBRS)\n- SPAE (2026): Training-free PBRS-inspired potential differences\n- PAV (ICLR 2025): \"Progress\" = change in success probability (MC-estimated, conceptually PBRS)\n- DVPO (ICLR 2026): Pretrained value model replaces reward model (general RLHF, not PBRS for math)\n- BSRS (AAAI 2025): Agent's V estimate as PBRS potential (general RL, not LLMs)\n\n**What appears to NOT exist (the gap):**\nThe specific proposal of (1) training a neural PRM explicitly as V(s_t) using TD/Bellman objectives, and then (2) deriving step-level process rewards via the classical PBRS formula F = gamma*V(s_{t+1}) - V(s_t), and (3) using these as dense rewards during LLM RL training for math reasoning -- with formal policy-invariance guarantees from Ng et al. (1999) -- does not appear as a single unified contribution in any paper found.\n\n**Key differentiation points to emphasize:**\n1. vs. SHAPE: Trained neural V(s_t) vs. MC rollout estimates (more scalable, no inference-time rollouts needed)\n2. vs. TDRM: Explicit PBRS framing with policy-invariance guarantees vs. ad-hoc TD labels\n3. vs. PRIME: Dedicated value network vs. implicit log-probability decomposition (potentially more expressive)\n4. vs. PAV: Amortized learned potentials vs. costly per-step MC estimation\n5. vs. DVPO: Math reasoning focus with PRM integration vs. general RLHF\n\n**Risk level: MODERATE.** The individual components are all well-established in concurrent work, and the conceptual connection between PRMs and PBRS is noted in at least one survey. The specific combination is novel but incremental. SHAPE is the most dangerous competitor as it already applies PBRS to LLM reasoning, just with MC potentials instead of a trained network.\n\nSources:\n- [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation](https://arxiv.org/abs/2604.06636)\n- [TDRM: Smooth Reward Models with Temporal Difference](https://arxiv.org/abs/2509.15110)\n- [PRIME: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)\n- [SPAE: Step Potential Advantage Estimation](https://arxiv.org/abs/2601.03823)\n- [PURE: Stop Summation (Min-Form Credit Assignment)](https://arxiv.org/abs/2504.15275)\n- [CRM: Conditional Reward Modeling](https://arxiv.org/abs/2509.26578)\n- [DuaShepherd](https://arxiv.org/abs/2506.17533)\n- [DVPO: Decoupled Value Policy Optimization](https://arxiv.org/abs/2502.16944)\n- [PQM: Process Reward Model with Q-Value Rankings](https://arxiv.org/abs/2410.11287)\n- [Rewarding Progress (PAV)](https://openreview.net/forum?id=A6Y7AqlzLW)\n- [AgentPRM](https://arxiv.org/abs/2511.08325)\n- [SSVPO](https://openreview.net/forum?id=g33DGvnHYd)\n- [RTMC](https://arxiv.org/abs/2604.11037)\n- [Credit Assignment Survey](https://arxiv.org/abs/2604.09459)\n- [rePIRL](https://arxiv.org/abs/2602.07832)\n- [Bootstrapped Reward Shaping](https://arxiv.org/abs/2501.00989)\n- [Reward Modeling Survey (Feb 2026)](https://arxiv.org/abs/2602.09305)\n- [Free Process Rewards without Process Labels](https://openreview.net/forum?id=8ThnPFhGm8)\n- [PROGRS](https://arxiv.org/abs/2604.02341)\n- [From Scalar Rewards to Potential Trends (SLOPE)](https://arxiv.org/abs/2602.03201)\n- [Calculus on MDPs: Potential Shaping as a Gradient](https://arxiv.org/abs/2208.09570)"
      }
    ],
    "totalDurationMs": 358101,
    "totalTokens": 59120,
    "totalToolUseCount": 59,
    "usage": {
      "input_tokens": 736,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 52318,
      "output_tokens": 5356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 710
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 736,
          "output_tokens": 5356,
          "cache_read_input_tokens": 52318,
          "cache_creation_input_tokens": 710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 710,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 59
    }
  },
  "sourceToolAssistantUUID": "3cf1205d-01d6-4093-90dc-60af51881db1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
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
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Potential-Valued Process…",
  "leafUuid": "f0583dd8-1b90-43b5-91fe-587fc32587c1",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Potential-valued process rewards for RL credit assignment",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0"
}
```

---

### Assistant

_source line 19 · 2026-05-27T08:30:30.035Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information from all three agents. Let me synthesize everything into the final JSON object.

Key findings:

**Concurrent work:**
- SHAPE (April 2026, ACL 2026): Most direct competitor - uses PBRS with MC-estimated potentials for LLM reasoning. BUT uses MC rollouts, not a trained neural value function.
- TDRM (Sep 2025): Trains PRM as V(s_t) via TD, but doesn't frame as PBRS explicitly.
- PRIME (ICLR 2026): Step rewards as value differences (implicit PBRS with gamma=1), but from log-prob decomposition.


- SPAE (Jan 2026): Training-free PBRS-inspired potential differences.
- PAV (ICLR 2025): "Progress" = change in success probability via MC.

The specific combination of training a neural PRM as V(s_t) using TD/Bellman, applying the PBRS formula for step rewards, and integrating this into RL training appears to be novel. Against baselines like PURE (82.6% on MATH500) and PRIME (+16.7% average improvement over SFT), this approach should be competitive.

Looking at the performance landscape: TDRM achieves 36.7% on AIME24 and outperforms other PRM methods by nearly 5%. For implementation, I'm considering the hardware requirements—7B models need around 8 H100s and 36 hours for PRIME-scale training, while PURE uses less compute. The strongest base models available are DeepSeek-R2 (32B) with exceptional MATH and AIME scores, and Qwen2.5-Math-7B as the dominant choice for PRM training. For publication timing, I should target venues with deadlines after late May 2026, like AAAI 2027 in July or ICLR 2027 around September.

The core approach I'm exploring frames a PRM as a state value function that estimates the probability of correctness given a solution prefix, then derives step rewards from the difference in value estimates between consecutive states. This satisfies the potential-based reward shaping conditions, which guarantees the policy remains invariant to the reward transformation.

I'll train this value-function PRM on a 7B base model using outcome supervision and temporal difference learning, then use the value differences to generate dense step-level rewards for policy training. I'll compare this against existing baselines like sum-form aggregation, the min-form approach from PURE, and Monte Carlo estimates from SHAPE to demonstrate the theoretical and empirical advantages.

Then I need to evaluate across multiple benchmarks—MATH500, GSM8K, AIME 2024, and ProcessBench—while ablating key hyperparameters like the discount factor and TD(λ) settings. For resources, doing this manually would take 10-14 weeks and around 2000-3000 GPU hours, but with Claude's help I can compress that to 7-10 weeks and 1500-2500 GPU hours while keeping API costs minimal.

The auto research approach would be fastest at 4-6 weeks but still requires the same GPU budget since RL training is the real bottleneck—it's compute-bound and doesn't parallelize well. I'm targeting AAAI 2027 and ICLR 2027 as top-tier venues, though I'm realizing the novelty might be more moderate than I initially thought given existing work like SHAPE and TDRM.

The key insight is that while PRIME, PURE, TDRM, and CRM are all closely related, my specific combination plus the theoretical analysis should be novel enough for top-tier acceptance if the experiments demonstrate clear improvements. I'm now compiling the verified references to ground the work properly. I need to correct the publication date for that RARL survey—it's from April 2026, not February. Let me also make sure SHAPE is properly highlighted as critical concurrent work, then carefully construct the JSON output with the right project name and all the details verified.

On PURE, the arXiv timestamp (2504.15275) indicates April 2025, which aligns with NeurIPS 2025's May deadline and December conference, so that checks out. For the resource estimates, I'm breaking down the main experimental components: training a VF-PRM on Qwen2.5-Math-7B requires roughly 8...

Actually, let me recalculate the total GPU hours more carefully. The PRM training, RL training with multiple ablation runs across different hyperparameters, and evaluation add up to approximately 2,300 GPU-hours, which translates to around $4,600 at typical H100 cloud pricing.

The timeline varies significantly depending on the approach: manual sequential experiments would take 10-14 weeks, a human-in-loop approach cuts that to 7-10 weeks, and full automation gets us down to 4-6 weeks with GPU availability as the limiting factor.

Now I'm drafting the JSON structure and writing an executive summary that explains how Value-Function Process Reward Models derive step-level rewards from outcome-supervised value functions using potential-based reward shaping, where step rewards are computed as the temporal difference in value estimates rather than training separate classifiers. Writing JSON output... I'm verifying the remaining references in the list, checking BSRS and confirming all citations are accurate before finalizing the key references section. I'm settling on the "From Reasoning to Agentic" survey from April 2026 as the right reference since it covers the reward semantics and PBRS discussion I need. Now I'm drafting the technical approach: training a process reward model as a value function on Qwen2.5-Math-7B using temporal difference learning with only outcome supervision, then deriving dense step rewards through the classical PBRS formula to preserve optimality, and finally integrating these into GRPO-based policy training with online value updates.

I also need to prove that sum-form reward aggregation corresponds to a telescoping potential (which explains reward hacking through unbounded shaping) while min-form corresponds to a truncated potential (explaining information loss), tying these theoretical insights to PURE's empirical results. Then I'll benchmark everything against PRIME, PURE, SHAPE, and TDRM on MATH500, GSM8K, AIME 2024, and ProcessBench.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0583dd8-1b90-43b5-91fe-587fc32587c1",
  "isSidechain": false,
  "requestId": "req_011CbSkxvv5wZvP4iUr63rpJ",
  "type": "assistant",
  "uuid": "b1f9c0d5-6601-471c-9642-1a3a0e366b95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012xaVdwfgzrgVUqUQb1QGaf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7350,
      "cache_creation_input_tokens": 7094,
      "cache_read_input_tokens": 13868,
      "output_tokens": 4512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7094,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7350,
          "output_tokens": 4512,
          "cache_read_input_tokens": 13868,
          "cache_creation_input_tokens": 7094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7094
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

_source line 20 · 2026-05-27T08:30:30.036Z_

Now I have all three research streams complete. Let me synthesize everything into the final JSON output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1f9c0d5-6601-471c-9642-1a3a0e366b95",
  "isSidechain": false,
  "requestId": "req_011CbSkxvv5wZvP4iUr63rpJ",
  "type": "assistant",
  "uuid": "45620c1e-c170-4caf-9b31-f9ebc5fc6ca6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012xaVdwfgzrgVUqUQb1QGaf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7350,
      "cache_creation_input_tokens": 7094,
      "cache_read_input_tokens": 13868,
      "output_tokens": 4512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7094,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7350,
          "output_tokens": 4512,
          "cache_read_input_tokens": 13868,
          "cache_creation_input_tokens": 7094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7094
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

_source line 21 · 2026-05-27T08:30:34.970Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BzMPD1923FmAAsZf8VJrqz`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify PURE venue and RARL survey",
  "prompt": "I need to verify two specific papers:\n\n1. PURE: \"Stop Summation: Min-Form Credit Assignment Is All PRM Needs\" - Was this accepted at NeurIPS 2025? Or is it only on arXiv? Search for the exact venue.\n   - arXiv ID: 2504.15275\n   - Search: \"PURE stop summation min-form NeurIPS 2025\"\n\n2. The \"RARL survey\" about credit assignment in RL for LLMs - I found \"From Reasoning to Agentic: Credit Assignment in RL for LLMs\" (arXiv 2604.09459, April 2026). Is there also a separate survey from Feb 2026 about reward modeling for LLMs? \n   - Search: \"reward modeling survey LLM 2026 February arXiv\"\n   - arXiv 2602.09305 - what is this paper exactly?\n\n3. Also verify: Is \"Rewarding Progress: Scaling Automated Process Verifiers\" at ICLR 2025? Search to confirm.\n\nReport exact venues and dates for each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45620c1e-c170-4caf-9b31-f9ebc5fc6ca6",
  "isSidechain": false,
  "requestId": "req_011CbSkxvv5wZvP4iUr63rpJ",
  "type": "assistant",
  "uuid": "bc2e4ebd-b928-47f2-bf46-566738a33cb7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012xaVdwfgzrgVUqUQb1QGaf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7350,
      "cache_creation_input_tokens": 7094,
      "cache_read_input_tokens": 13868,
      "output_tokens": 4512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7094,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7350,
          "output_tokens": 4512,
          "cache_read_input_tokens": 13868,
          "cache_creation_input_tokens": 7094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7094
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

_source line 22 · 2026-05-27T08:31:17.124Z_

<details><summary>↩ Tool result · `toolu_01BzMPD1923FmAAsZf8VJrqz`</summary>

```text
Here are the verified findings for all three papers:

---

**1. PURE: "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning"**
- **arXiv ID:** 2504.15275
- **Venue:** Accepted at **NeurIPS 2025** (confirmed)
- **Presentation:** Poster session, Wednesday December 3, 2025, 4:30-7:30 PM PST, San Diego
- **OpenReview:** https://openreview.net/forum?id=3Sxby0hH1q
- **NeurIPS page:** https://neurips.cc/virtual/2025/poster/120032

This is definitively a NeurIPS 2025 paper, not just an arXiv preprint.

---

**2. The "RARL survey" situation -- two distinct papers exist:**

- **arXiv 2602.09305** — "Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation" by Pei-Chi Pan, Yingbin Liang, and Sen Lin. Submitted **February 10, 2026**. This is an **arXiv-only preprint** with no confirmed conference acceptance. It introduces "Reasoning-Aligned Reinforcement Learning (RARL)" as a unifying framework for reward paradigms in multi-step reasoning. This is the **February 2026 reward modeling survey** you were asking about.

- **arXiv 2604.09459** — "From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models" by Chenchen Zhang. Submitted **April 10, 2026** (v2: April 13, 2026). This is also an **arXiv-only preprint** with no conference acceptance. It surveys 47 credit assignment methods and covers both reasoning RL and agentic RL.

These are **two separate papers** by different authors. The first (2602.09305) focuses on reward modeling/design, while the second (2604.09459) focuses specifically on credit assignment. Both are arXiv preprints only.

---

**3. "Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning"**
- **arXiv ID:** 2410.08146
- **Venue:** Confirmed accepted at **ICLR 2025** (Conference paper, in official proceedings)
- **Proceedings page:** https://proceedings.iclr.cc/paper_files/paper/2025/hash/98711dea460bdefe0e651ca23ec98ba2-Abstract-Conference.html
- **ICLR virtual page:** https://iclr.cc/virtual/2025/poster/30649
- **Authors:** Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, Aviral Kumar

This is definitively an ICLR 2025 conference paper.

---

Sources:
- [PURE on arXiv](https://arxiv.org/abs/2504.15275)
- [PURE on OpenReview (NeurIPS 2025)](https://openreview.net/forum?id=3Sxby0hH1q)
- [PURE NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/poster/120032)
- [arXiv 2602.09305 - Reward Modeling Survey](https://arxiv.org/abs/2602.09305)
- [arXiv 2604.09459 - Credit Assignment Survey](https://arxiv.org/abs/2604.09459)
- [Rewarding Progress on arXiv](https://arxiv.org/abs/2410.08146)
- [Rewarding Progress ICLR 2025 Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/98711dea460bdefe0e651ca23ec98ba2-Abstract-Conference.html)
- [Rewarding Progress ICLR 2025 Poster](https://iclr.cc/virtual/2025/poster/30649)

agentId: a6fbd5a438b62c9c7 (use SendMessage with to: 'a6fbd5a438b62c9c7' to continue this agent)
&lt;usage>total_tokens: 15816
tool_uses: 9
duration_ms: 42149&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc2e4ebd-b928-47f2-bf46-566738a33cb7",
  "isSidechain": false,
  "promptId": "89e1f898-be85-43fe-bddd-b707ae832929",
  "type": "user",
  "uuid": "69670770-a6cd-419c-b174-2a50bd61fd25",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two specific papers:\n\n1. PURE: \"Stop Summation: Min-Form Credit Assignment Is All PRM Needs\" - Was this accepted at NeurIPS 2025? Or is it only on arXiv? Search for the exact venue.\n   - arXiv ID: 2504.15275\n   - Search: \"PURE stop summation min-form NeurIPS 2025\"\n\n2. The \"RARL survey\" about credit assignment in RL for LLMs - I found \"From Reasoning to Agentic: Credit Assignment in RL for LLMs\" (arXiv 2604.09459, April 2026). Is there also a separate survey from Feb 2026 about reward modeling for LLMs? \n   - Search: \"reward modeling survey LLM 2026 February arXiv\"\n   - arXiv 2602.09305 - what is this paper exactly?\n\n3. Also verify: Is \"Rewarding Progress: Scaling Automated Process Verifiers\" at ICLR 2025? Search to confirm.\n\nReport exact venues and dates for each.",
    "agentId": "a6fbd5a438b62c9c7",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the verified findings for all three papers:\n\n---\n\n**1. PURE: \"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning\"**\n- **arXiv ID:** 2504.15275\n- **Venue:** Accepted at **NeurIPS 2025** (confirmed)\n- **Presentation:** Poster session, Wednesday December 3, 2025, 4:30-7:30 PM PST, San Diego\n- **OpenReview:** https://openreview.net/forum?id=3Sxby0hH1q\n- **NeurIPS page:** https://neurips.cc/virtual/2025/poster/120032\n\nThis is definitively a NeurIPS 2025 paper, not just an arXiv preprint.\n\n---\n\n**2. The \"RARL survey\" situation -- two distinct papers exist:**\n\n- **arXiv 2602.09305** — \"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation\" by Pei-Chi Pan, Yingbin Liang, and Sen Lin. Submitted **February 10, 2026**. This is an **arXiv-only preprint** with no confirmed conference acceptance. It introduces \"Reasoning-Aligned Reinforcement Learning (RARL)\" as a unifying framework for reward paradigms in multi-step reasoning. This is the **February 2026 reward modeling survey** you were asking about.\n\n- **arXiv 2604.09459** — \"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models\" by Chenchen Zhang. Submitted **April 10, 2026** (v2: April 13, 2026). This is also an **arXiv-only preprint** with no conference acceptance. It surveys 47 credit assignment methods and covers both reasoning RL and agentic RL.\n\nThese are **two separate papers** by different authors. The first (2602.09305) focuses on reward modeling/design, while the second (2604.09459) focuses specifically on credit assignment. Both are arXiv preprints only.\n\n---\n\n**3. \"Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning\"**\n- **arXiv ID:** 2410.08146\n- **Venue:** Confirmed accepted at **ICLR 2025** (Conference paper, in official proceedings)\n- **Proceedings page:** https://proceedings.iclr.cc/paper_files/paper/2025/hash/98711dea460bdefe0e651ca23ec98ba2-Abstract-Conference.html\n- **ICLR virtual page:** https://iclr.cc/virtual/2025/poster/30649\n- **Authors:** Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, Aviral Kumar\n\nThis is definitively an ICLR 2025 conference paper.\n\n---\n\nSources:\n- [PURE on arXiv](https://arxiv.org/abs/2504.15275)\n- [PURE on OpenReview (NeurIPS 2025)](https://openreview.net/forum?id=3Sxby0hH1q)\n- [PURE NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/poster/120032)\n- [arXiv 2602.09305 - Reward Modeling Survey](https://arxiv.org/abs/2602.09305)\n- [arXiv 2604.09459 - Credit Assignment Survey](https://arxiv.org/abs/2604.09459)\n- [Rewarding Progress on arXiv](https://arxiv.org/abs/2410.08146)\n- [Rewarding Progress ICLR 2025 Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/98711dea460bdefe0e651ca23ec98ba2-Abstract-Conference.html)\n- [Rewarding Progress ICLR 2025 Poster](https://iclr.cc/virtual/2025/poster/30649)"
      }
    ],
    "totalDurationMs": 42149,
    "totalTokens": 15816,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2070,
      "cache_read_input_tokens": 12707,
      "output_tokens": 1038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2070
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1038,
          "cache_read_input_tokens": 12707,
          "cache_creation_input_tokens": 2070,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2070,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 9
    }
  },
  "sourceToolAssistantUUID": "bc2e4ebd-b928-47f2-bf46-566738a33cb7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
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
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Potential-Valued Process…",
  "leafUuid": "69670770-a6cd-419c-b174-2a50bd61fd25",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Potential-valued process rewards for RL credit assignment",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0"
}
```

---

### Assistant

_source line 25 · 2026-05-27T08:32:00.933Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me construct the final JSON object carefully.

Let me organize everything:

**Verified references:**
1. PRIME: Process Reinforcement through Implicit Rewards (ICLR 2026) ✓
2. PURE: Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (NeurIPS 2025) ✓
3. TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference (arXiv 2025) ✓


4. CRM: Linking Process to Outcome: Conditional Reward Modeling (ICLR 2026) ✓
5. DuaShepherd: Integrating Stepwise Correctness and Potential Rewards (arXiv 2025) ✓
6. DVPO: Pretrain Value, Not Reward: Decoupled Value Policy Optimization (ICLR 2026) ✓
7. SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning (ACL 2026) ✓
8. Policy Invariance Under Reward Transformations - Ng, Ha ✓
9. Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning (ICLR 2025) ✓
10. SPAE: Step Potential Advantage Estimation (arXiv 2026) ✓
11. RARL survey: Reward Modeling for Reinforcement Learning-Based LLM Reasoning (arXiv 2026) ✓
12. From Reasoning to Agentic: Credit Assignment in RL for LLMs (arXiv 2026) ✓
13. Bootstrapped Reward Shaping (AAAI 2025) ✓
14. OVM: Outcome-supervised Value Models for Planning in Mathematical Reasoning (NAACL 2024) ✓

I'm going through the list and removing any papers I can't verify, though everything here looks solid so far.

Now I'm deciding which papers are most essential for the key_references section. The foundational work on policy invariance under reward transformations is critical, along with the recent papers that directly address process-based reward shaping for LLM reasoning—particularly the ones tackling aggregation problems, conditional rewards, and the distinction between value and reward pretraining. I'm focusing on papers that either establish core theory or provide novel solutions to the specific challenges in this space.

For submission targets, AAAI 2027 and ICLR 2027 are the primary venues given their deadlines and relevance to this theoretical contribution. The work merits a top-tier classification since it combines formal guarantees with empirical validation and unifies several existing approaches under a principled framework.

The novelty centers on three key elements: explicitly combining PBRS with trained value functions, proving that sum and min aggregations are suboptimal potential choices, and demonstrating end-to-end RL training rather than just advantage modification. While there's some overlap with concurrent work like SHAPE and TDRM, the theoretical unification and practical benefits of eliminating step annotations justify the top-tier positioning. I should note the concurrent work risk but emphasize the distinct contributions.

Now I'm laying out the core technical approach: training a process reward model as a state value function using only binary outcome labels and TD learning, then deriving step rewards through the potential-based reward shaping formula. I'll prove that sum-form aggregation creates unbounded reward hacking while min-form loses gradient information, unifying these findings under PBRS theory. The final system integrates these shaped rewards into policy training with online value updates, benchmarked against existing baselines.

For resource planning, I'm estimating around 2,400 GPU-hours total across PRM training, RL runs with ablations, and evaluation, spanning 12-16 weeks with costs around $5,000-7,000.

The human-in-loop approach cuts the timeline to 8-11 weeks with slightly lower GPU costs but adds Claude API expenses of $300-500. Auto research could compress things further to 5-7 weeks but requires more exploration runs and hits a wall on RL training wallclock time—each GRPO run takes roughly 36 hours on 8 H100s.

For the paper, I'm framing this as Value-Function Process Reward Models that treat PRMs as state value functions and extract step rewards through potential-based reward shaping, which is a more principled approach than the current practice of training PRMs as step classifiers and then repurposing them for RL. through aggregation (sum, min, product), causing reward hacking or information loss with no theoretical justification for aggregation choice. VF-PRM trains V(s_t) ≈ P(correct | prefix₁:t) using TD(λ) with outcome-only supervision, then computes step rewards as F_t = γV(s_{t+1}) − V(s_t). By the Ng et al. (1999) policy invariance theorem, these shaped rewards provably preserve the optimal policy while providing dense gradients. We prove that existing sum-form and min-form aggregations correspond to specific suboptimal potential function choices, providing the first theoretical explanation for PURE's empirical findings and PRIME's implicit PBRS connection. Unlike concurrent work SHAPE which uses expensive Monte Carlo rollout potentials, our amortized neural value function avoids the need for inference-time rollouts. Testing with Qwen2.5-Math-7B and GRPO training shows consistent gains over PURE, PRIME, SHAPE, and TDRM across MATH500, GSM8K, and AIME 2024.

Now I'm updating the related work section to include SHAPE, SPAE, PAV, and the credit assignment survey alongside the existing methods. Let me verify the publication status of TDRM before finalizing the JSON output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69670770-a6cd-419c-b174-2a50bd61fd25",
  "isSidechain": false,
  "requestId": "req_011CbSm9Bhs8finPG9CNeWCm",
  "type": "assistant",
  "uuid": "4582b88a-be17-419b-a94c-dfb2c2c74141",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0134yGuezaqPY4P8XetZp4sJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12982,
      "cache_read_input_tokens": 20962,
      "output_tokens": 5149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12982,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5149,
          "cache_read_input_tokens": 20962,
          "cache_creation_input_tokens": 12982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12982
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

_source line 26 · 2026-05-27T08:32:47.809Z_

Now I have all the data needed. Let me compose the final merged JSON with all fields.

{
  "title": "Potential-Valued Process Rewards for Principled Step-Level Credit Assignment",
  "core_problem": "Current PRMs are trained as step-correctness classifiers but heuristically repurposed as RL reward signals via aggregation (sum, min, product), causing either reward hacking or information loss. No principled framework connects PRM design to RL training quality, despite potential-based reward shaping (PBRS) theory guaranteeing policy invariance — a well-known result never practically implemented for step-level process rewards in mathematical reasoning.",
  "opportunity": "Three independent 2025-2026 findings converge: (1) the RARL survey confirms PBRS 'lacks practical PRM implementation' for reasoning RL; (2) DuaShepherd proves step correctness and step value (potential) are orthogonal signals — yet all existing PRMs train only on correctness; (3) PURE demonstrates that sum-form PRM aggregation causes training collapse, while min-form loses useful gradient information, but provides no theoretical justification for why min works better. Training a PRM as a state value function V(s_t) = P(correct | prefix₁:t) and deriving step rewards as potential differences r_t = γV(s_{t+1}) − V(s_t) would unify these findings: PBRS guarantees no policy distortion, value-function training requires only outcome labels (no expensive step annotations), and the framework naturally subsumes sum/min/product as suboptimal special cases with specific potential-function choices.",
  "landscape": "PRM-RL integration is the most contested frontier. PURE (NeurIPS 2025) showed min-form credit assignment avoids reward hacking that collapses sum-form training 'even at the beginning,' but provides only empirical justification. TDRM (Sep 2025) applies TD learning to smooth PRM labels, achieving 23.7% improvement in tree-search and 20× data efficiency, but still requires step-level annotations and doesn't address the aggregation problem. CRM (ICLR 2026) models step rewards as conditional probabilities P(correct|s_{1:t}) causally linked to outcomes, evaluating on best-of-N, beam search, AND RL — but lacks PBRS guarantees and still uses MC-estimated step labels. PRIME (ICLR 2026) extracts implicit process rewards from ORM token probabilities and is acknowledged as 'viewable as PBRS where q-value is the potential,' but uses heuristic extraction rather than explicit value function training. DuaShepherd (June 2025) separates correctness and potential reward heads, achieving SOTA on MATH500/ProcessBench, but evaluates only at inference time (best-of-N), not RL training. DVPO (ICLR 2026) pretrains a Global Value Model for general RLHF with 40% less GPU memory, but operates at response-level, not step-level process supervision. The RARL survey (Feb 2026) catalogs reward modeling paradigms and identifies the central open problem: 'Different aggregation schemes produce divergent policy behaviors, yet principled design guidelines remain absent.' CRITICAL CONCURRENT WORK: SHAPE (ACL 2026) applies PBRS with Monte Carlo-estimated potentials to LLM reasoning, explicitly citing Ng et al. (1999), achieving +3% accuracy with 30% fewer tokens — but uses training-free MC rollouts (not a learned value function) and only modifies GRPO advantages rather than serving as a standalone PRM training objective. SPAE (Jan 2026) uses training-free PBRS-inspired potential differences with a heuristic composite metric. PAV (ICLR 2025) estimates step 'progress' as change in MC success probability, conceptually identical to PBRS but without formal connection or a trained model. The credit assignment survey (Apr 2026) covers 47 methods across token/segment/step/turn granularity and does NOT identify the specific combination of trained neural V(s_t) + explicit PBRS step rewards + RL training as an existing method — suggesting this precise integration remains an open gap.",
  "inspired_by": "Gap: RARL survey's verified finding that PBRS 'lacks practical PRM implementation' despite theoretical support for policy invariance. Gap: DuaShepherd's proof that correctness and value are orthogonal, implying current correctness-only PRMs are insufficient for RL. Pattern: DVPO's 'pretrain value, not reward' principle applied to step-level reasoning. Combination: PRIME's PBRS connection (implicit, heuristic) + CRM's causal outcome alignment (no PBRS guarantee) + TDRM's temporal consistency (requires step labels) — unified through explicit outcome-supervised value function training with formal PBRS guarantees. Differentiation vs. SHAPE (ACL 2026): amortized neural value function eliminates per-step MC rollouts, enabling scalable online RL integration rather than one-shot advantage modification.",
  "approach": "Train a Process Reward Model as an explicit state value function V(s_t) ≈ P(correct | prefix₁:t) on Qwen2.5-Math-7B using TD(λ) with only binary outcome supervision, requiring no step-level annotations. Derive dense step-level rewards via the classical PBRS formula F_t = γV(s_{t+1}) − V(s_t), which provably preserves the optimal policy under Ng et al. (1999). Provide formal proofs that sum-form aggregation reduces to a telescoping potential with unbounded shaping magnitude (explaining reward hacking) while min-form corresponds to a truncated potential (explaining gradient information loss), thereby unifying PURE's empirical findings under PBRS theory. Integrate these shaped rewards into GRPO training of a policy model with online value function updates, comparing against PRIME, PURE, SHAPE (MC potentials), and TDRM baselines. Evaluate on MATH500, GSM8K, AIME 2024, and ProcessBench, with ablations on discount factor γ, TD(λ) parameters, and amortized neural versus Monte Carlo potential estimation.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~2,400 H100-hours (VF-PRM training ~200h, GRPO RL runs ×6-8 ablations ~2,000h, eval ~200h)",
      "timeline": "12-16 weeks (sequential: 3w infrastructure, 4w VF-PRM training & tuning, 4w RL experiments, 3w analysis & writing)",
      "estimated_gpu_cost": "$5,000-7,000 (H100 at ~$2.50/GPU-hr on Lambda/RunPod)"
    },
    "human_in_loop": {
      "gpu_hours": "~2,000 H100-hours (fewer failed runs via Claude-assisted debugging and config generation)",
      "timeline": "8-11 weeks (2w infra, 3w VF-PRM, 3w RL experiments, 2w writing)",
      "claude_api_cost": "$300-500 (code generation, experiment analysis, paper drafting)",
      "estimated_gpu_cost": "$4,000-6,000"
    },
    "auto_research": {
      "gpu_hours": "~2,500 H100-hours (broader automated hyperparameter sweeps)",
      "timeline": "5-7 weeks (parallelized experiment scheduling, automated analysis)",
      "claude_api_cost": "$600-1,200 (orchestration, iterative experiment design, full paper generation)",
      "estimated_gpu_cost": "$5,000-7,500",
      "speed_bottleneck": "RL training wallclock: ~36h per GRPO run on 8×H100 is irreducibly sequential; 6-8 ablation runs cannot be fully parallelized without 48-64 GPUs"
    }
  },
  "target_venues": [
    "AAAI 2027 (deadline: Jul 28, 2026 — confirmed)",
    "ICLR 2027 (deadline: ~Sep 24, 2026 — estimated from prior-year pattern)",
    "AISTATS 2027 (deadline: ~Oct 10, 2026 — estimated)"
  ],
  "level": "top-tier",
  "key_references": [
    "Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping (ICML 1999)",
    "Process Reinforcement through Implicit Rewards — PRIME (ICLR 2026)",
    "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning — PURE (NeurIPS 2025)",
    "Smooth Reward Models with Temporal Difference for LLM RL and Inference — TDRM (arXiv 2025)",
    "Linking Process to Outcome: Conditional Reward Modeling — CRM (ICLR 2026)",
    "DuaShepherd: Integrating Stepwise Correctness and Potential Rewards (arXiv 2025)",
    "Pretrain Value, Not Reward: Decoupled Value Policy Optimization — DVPO (ICLR 2026)",
    "SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning (ACL 2026)",
    "Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning — PAV (ICLR 2025)",
    "Step Potential Advantage Estimation — SPAE (arXiv 2026)",
    "Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation — RARL survey (arXiv 2026)",
    "From Reasoning to Agentic: Credit Assignment in RL for LLMs (arXiv 2026)",
    "Outcome-supervised Value Models for Planning in Mathematical Reasoning — OVM (NAACL 2024)"
  ],
  "description": "We propose Value-Function Process Reward Models (VF-PRM), a principled framework that trains PRMs as state value functions and derives step-level rewards via potential-based reward shaping (PBRS). Current PRMs are trained as step-correctness classifiers but heuristically repurposed as RL rewards through aggregation (sum, min, product), causing reward hacking or information loss with no theoretical justification for aggregation choice. VF-PRM trains V(s_t) ≈ P(correct | prefix₁:t) using TD(λ) with outcome-only supervision, then computes step rewards as F_t = γV(s_{t+1}) − V(s_t). By the Ng et al. (1999) policy invariance theorem, these shaped rewards provably preserve the optimal policy while providing dense gradients. We prove that existing sum-form and min-form aggregations correspond to specific suboptimal potential function choices, providing the first theoretical explanation for PURE's empirical findings and PRIME's implicit PBRS connection. Unlike concurrent work SHAPE (ACL 2026) which uses expensive Monte Carlo rollout potentials, our amortized neural value function requires no inference-time rollouts and supports online updates during RL training. Experiments with Qwen2.5-Math-7B and GRPO training target consistent improvements over PURE, PRIME, SHAPE, and TDRM baselines across MATH500 (beating PURE's 82.6%), GSM8K, and AIME 2024 (beating TDRM's 36.7%).",
  "project_name": "pbrs_value_prm",
  "source": "web_research"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4582b88a-be17-419b-a94c-dfb2c2c74141",
  "isSidechain": false,
  "requestId": "req_011CbSm9Bhs8finPG9CNeWCm",
  "type": "assistant",
  "uuid": "00169ab3-c575-4395-aefd-ae3205c083ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0134yGuezaqPY4P8XetZp4sJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12982,
      "cache_read_input_tokens": 20962,
      "output_tokens": 5149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12982,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5149,
          "cache_read_input_tokens": 20962,
          "cache_creation_input_tokens": 12982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12982
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
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Potential-Valued Process…",
  "leafUuid": "00169ab3-c575-4395-aefd-ae3205c083ed",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Potential-valued process rewards for RL credit assignment",
  "sessionId": "78f193f8-febe-4b1b-a19c-57e61b202db0"
}
```

---
