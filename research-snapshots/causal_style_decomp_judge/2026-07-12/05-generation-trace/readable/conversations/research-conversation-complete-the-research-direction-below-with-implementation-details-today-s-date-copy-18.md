# Research conversation: Complete the research direction below with implementation details. **Today's date: 2026-05-27 (UTC).** Only recommend ve

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 73
- **Recorded user turns:** 5
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/d50cf128-39c2-46f2-abb0-ee1a4faf1620.jsonl`
- **Structured JSON:** [`65741aaa6ce85d92ae06.json`](../../sessions/65/65741aaa6ce85d92ae06.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T12:17:40.314Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T12:17:40.314Z",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "content": "Complete the research direction below with implementation details.\n\n**Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.\n\n{\n  \"title\": \"Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition\",\n  \"core_problem\": \"How can we achieve near-formal-verification reliability for natural language mathematical proof checking while keeping cost tractable, by selectively routing only the most uncertain proof blocks to formal verification?\",\n  \"opportunity\": \"Pseudo-Formalization (Barkallah et al., May 2026) introduced modular proof blocks with explicit premises, conclusions, and dependencies — but verifies them only via LLM, missing ~50% of research-level errors. Safe (Liu et al., ACL 2025) achieves step-level formal verification at 80% proof success but imposes 4-8x cost overhead by verifying ALL steps uniformly. No prior work has exploited PF's self-contained modular structure as a bridge to targeted autoformalization: each PF block's explicit claim statement and premises are far closer to a formal theorem statement than raw NL text, potentially making block-level autoformalization significantly more reliable than whole-proof autoformalization. By using Block Verification confidence as a triage signal, we can route only the 10-20% most uncertain blocks to formal verification, catching errors that LLM verification misses while avoiding the prohibitive cost of universal formalization.\",\n  \"landscape\": \"Current proof verification spans a cost-reliability spectrum with no effective middle ground: LLM-as-judge is cheap but unreliable (best PRM drops from 78.3% to 37.3% on Hard2Verify; Barkallah et al., 2026; Zheng et al., 2025); PF+Block Verification Pareto-dominates LLM-as-judge on olympiad and research-level benchmarks but still leaves ~50% of errors undetected on ArxivMathGradingBench (Barkallah et al., 2026); Safe verifies each step in Lean 4 with ~80% success but costs 4-8x more compute per step than process reward models (Liu et al., ACL 2025); end-to-end autoformalization pipelines achieve only ~36% success because autoformalization accuracy (97%) and theorem proving success (~70%) compound poorly across the full pipeline (miniF2F-Lean Revisited, 2025). Adjacent work on uncertainty-guided selective verification has shown 14-100% error reduction with minimal abstention in SMT-based formalization (Bhatt et al., 2025) and adaptive verification allocation achieves 44% fewer verifier calls with higher accuracy on MATH (Mu et al., 2026), but neither has been applied to the NL proof verification domain with pseudo-formal structure as the intermediary.\",\n  \"inspired_by\": \"Gap: PF (May 2026) only uses LLM verification despite its formal-like modular structure; Safe (ACL 2025) applies formal verification uniformly without selectivity. Pattern: Adaptive compute allocation across verification tiers (Mu et al., 2026; Bhatt et al., 2025) has proven effective but has not been applied to the informal-formal proof verification spectrum. Untried combination: PF's self-contained blocks (explicit premises + conclusions) as autoformalization targets + uncertainty-guided routing between LLM and formal verification.\"\n}\n\nADD these fields (keep all existing fields):\n{\n  \"approach\": \"Proposed method — what you would actually do (3-5 sentences)\",\n  \"resource_estimate\": {\n      \"manual\": {\"gpu_hours\": \"...\", \"timeline\": \"...\", \"estimated_gpu_cost\": \"...\"},\n      \"human_in_loop\": {\"gpu_hours\": \"...\", \"timeline\": \"...\", \"claude_api_cost\": \"...\", \"estimated_gpu_cost\": \"...\"},\n      \"auto_research\": {\"gpu_hours\": \"...\", \"timeline\": \"...\", \"claude_api_cost\": \"...\", \"estimated_gpu_cost\": \"...\", \"speed_bottleneck\": \"...\"}\n  },\n  \"target_venues\": [\"Only venues with deadlines after 2026-05-27\"],\n  \"level\": \"top-tier | solid | incremental\",\n  \"key_references\": [\"Paper title (VENUE YEAR)\", ...],\n  \"description\": \"Executive summary (150-200 words)\",\n  \"project_name\": \"snake_case_identifier (max 30 chars)\",\n  \"source\": \"web_research\"\n}\n\nFor key_references, verify with web_search that cited papers are real. Drop unverifiable ones.\n\n**Model freshness rule**: When the approach involves pretrained models, use web_search to find current top-performing open-source models — do NOT default to models from your training data.\n\n## 竞争论文 & Concurrent Work 搜索\n\n在设计 approach 之前，必须确认没有人正在做同样的事情：\n- 搜索 `{core_problem} 2026` 和 `{approach_keyword} {task} 2026`\n- 在 arXiv 上搜索过去 3 个月的相关提交\n- 在 OpenReview 上搜索即将举行的会议提交\n- 如果发现高度相似的 concurrent work，必须在 landscape 中明确提及\n\n## 可行性验证\n\n1. 搜索类似方法的已有实现（GitHub）\n2. 查找需要打败的具体 baseline 数字\n3. 了解类似实验的硬件/数据需求\n\nOutput ONLY a single JSON object with ALL fields merged. No markdown fences."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T12:17:40.318Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T12:17:40.318Z",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

## Round 1

23 recorded events

### User

_source line 3 · 2026-05-27T12:17:40.369Z_

Complete the research direction below with implementation details.

**Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.

{
  "title": "Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition",
  "core_problem": "How can we achieve near-formal-verification reliability for natural language mathematical proof checking while keeping cost tractable, by selectively routing only the most uncertain proof blocks to formal verification?",
  "opportunity": "Pseudo-Formalization (Barkallah et al., May 2026) introduced modular proof blocks with explicit premises, conclusions, and dependencies — but verifies them only via LLM, missing ~50% of research-level errors. Safe (Liu et al., ACL 2025) achieves step-level formal verification at 80% proof success but imposes 4-8x cost overhead by verifying ALL steps uniformly. No prior work has exploited PF's self-contained modular structure as a bridge to targeted autoformalization: each PF block's explicit claim statement and premises are far closer to a formal theorem statement than raw NL text, potentially making block-level autoformalization significantly more reliable than whole-proof autoformalization. By using Block Verification confidence as a triage signal, we can route only the 10-20% most uncertain blocks to formal verification, catching errors that LLM verification misses while avoiding the prohibitive cost of universal formalization.",
  "landscape": "Current proof verification spans a cost-reliability spectrum with no effective middle ground: LLM-as-judge is cheap but unreliable (best PRM drops from 78.3% to 37.3% on Hard2Verify; Barkallah et al., 2026; Zheng et al., 2025); PF+Block Verification Pareto-dominates LLM-as-judge on olympiad and research-level benchmarks but still leaves ~50% of errors undetected on ArxivMathGradingBench (Barkallah et al., 2026); Safe verifies each step in Lean 4 with ~80% success but costs 4-8x more compute per step than process reward models (Liu et al., ACL 2025); end-to-end autoformalization pipelines achieve only ~36% success because autoformalization accuracy (97%) and theorem proving success (~70%) compound poorly across the full pipeline (miniF2F-Lean Revisited, 2025). Adjacent work on uncertainty-guided selective verification has shown 14-100% error reduction with minimal abstention in SMT-based formalization (Bhatt et al., 2025) and adaptive verification allocation achieves 44% fewer verifier calls with higher accuracy on MATH (Mu et al., 2026), but neither has been applied to the NL proof verification domain with pseudo-formal structure as the intermediary.",
  "inspired_by": "Gap: PF (May 2026) only uses LLM verification despite its formal-like modular structure; Safe (ACL 2025) applies formal verification uniformly without selectivity. Pattern: Adaptive compute allocation across verification tiers (Mu et al., 2026; Bhatt et al., 2025) has proven effective but has not been applied to the informal-formal proof verification spectrum. Untried combination: PF's self-contained blocks (explicit premises + conclusions) as autoformalization targets + uncertainty-guided routing between LLM and formal verification."
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
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "type": "user",
  "uuid": "5cf95e0b-e424-4dc7-89c7-a30245d3a625",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T12:17:40.368Z_

```json
{
  "parentUuid": "5cf95e0b-e424-4dc7-89c7-a30245d3a625",
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
  "uuid": "7a3b6e8c-3763-4469-8b99-e4b725dd599c",
  "timestamp": "2026-05-27T12:17:40.368Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T12:17:40.368Z_

```json
{
  "parentUuid": "7a3b6e8c-3763-4469-8b99-e4b725dd599c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "361c59b3-7568-437d-8d03-6a6079259ab1",
  "timestamp": "2026-05-27T12:17:40.368Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
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
  "aiTitle": "Uncertainty-guided selective proof block formalization",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Assistant

_source line 7 · 2026-05-27T12:17:44.582Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to complete a research direction with implementation details. I need to:

1. Search for concurrent work and competing papers
2. Verify feasibility
3. Find current top-performing models
4. Verify references
5. Check venue deadlines
6. Compile everything into a JSON object

Let me start by doing multiple searches in parallel to gather the information I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "361c59b3-7568-437d-8d03-6a6079259ab1",
  "isSidechain": false,
  "requestId": "req_011CbT4QU4GRnpuvgv1XwKCb",
  "type": "assistant",
  "uuid": "71de9467-3b63-426d-a726-13f0dd2ff3da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSArFpUDyA54TY9ok9THbT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2713,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2072,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2072,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2713
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

_source line 8 · 2026-05-27T12:17:52.625Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01US71XcUTtVTniJ93XX1yzB`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search concurrent work 2026",
  "prompt": "I need you to search for concurrent and competing work on the following research idea. Use WebSearch extensively.\n\nResearch idea: \"Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition\" — the idea is to use pseudo-formal proof blocks (modular NL proof blocks with explicit premises/conclusions) as targets for selective autoformalization, routing only uncertain blocks to formal verification (e.g., Lean 4) while verifying confident blocks with LLM-based verification.\n\nSearch queries to run (use WebSearch for each):\n1. \"selective formal verification uncertainty 2026\"\n2. \"pseudo-formal autoformalization 2026\"\n3. \"adaptive verification mathematical proof 2026\"\n4. \"uncertainty guided proof verification\"\n5. \"selective autoformalization natural language proof 2026\"\n6. Search arXiv for: \"autoformalization selective verification 2026\"\n7. Search arXiv for: \"proof verification uncertainty routing 2026\"\n8. Search OpenReview for: \"selective formal verification\"\n9. Search OpenReview for: \"pseudo-formal verification\"\n10. \"Barkallah pseudo-formalization 2026\"\n11. \"Safe Liu ACL 2025 formal verification lean\"\n12. \"Mu adaptive verification allocation 2026\"\n13. \"Bhatt uncertainty guided selective verification 2025\"\n\nFor each search, report:\n- The query used\n- Key results found (titles, authors, dates, venues)\n- Whether any result is highly similar to the proposed idea\n\nBe thorough — this is critical for novelty checking. Report ALL findings, even tangentially related ones.",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71de9467-3b63-426d-a726-13f0dd2ff3da",
  "isSidechain": false,
  "requestId": "req_011CbT4QU4GRnpuvgv1XwKCb",
  "type": "assistant",
  "uuid": "4f566e9b-acb6-4b78-aca1-fab30622e0d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSArFpUDyA54TY9ok9THbT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2713,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2072,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2072,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2713
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

_source line 9 · 2026-05-27T12:17:52.636Z_

<details><summary>↩ Tool result · `toolu_01US71XcUTtVTniJ93XX1yzB`</summary>

```text
Async agent launched successfully.
agentId: aefc7761e04a79fe8 (internal ID - do not mention to user. Use SendMessage with to: 'aefc7761e04a79fe8' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/aefc7761e04a79fe8.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f566e9b-acb6-4b78-aca1-fab30622e0d6",
  "isSidechain": false,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "type": "user",
  "uuid": "d7b0177a-c9b7-4a14-9f45-e1d0fc2fcfc2",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "aefc7761e04a79fe8",
    "description": "Search concurrent work 2026",
    "prompt": "I need you to search for concurrent and competing work on the following research idea. Use WebSearch extensively.\n\nResearch idea: \"Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition\" — the idea is to use pseudo-formal proof blocks (modular NL proof blocks with explicit premises/conclusions) as targets for selective autoformalization, routing only uncertain blocks to formal verification (e.g., Lean 4) while verifying confident blocks with LLM-based verification.\n\nSearch queries to run (use WebSearch for each):\n1. \"selective formal verification uncertainty 2026\"\n2. \"pseudo-formal autoformalization 2026\"\n3. \"adaptive verification mathematical proof 2026\"\n4. \"uncertainty guided proof verification\"\n5. \"selective autoformalization natural language proof 2026\"\n6. Search arXiv for: \"autoformalization selective verification 2026\"\n7. Search arXiv for: \"proof verification uncertainty routing 2026\"\n8. Search OpenReview for: \"selective formal verification\"\n9. Search OpenReview for: \"pseudo-formal verification\"\n10. \"Barkallah pseudo-formalization 2026\"\n11. \"Safe Liu ACL 2025 formal verification lean\"\n12. \"Mu adaptive verification allocation 2026\"\n13. \"Bhatt uncertainty guided selective verification 2025\"\n\nFor each search, report:\n- The query used\n- Key results found (titles, authors, dates, venues)\n- Whether any result is highly similar to the proposed idea\n\nBe thorough — this is critical for novelty checking. Report ALL findings, even tangentially related ones.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/aefc7761e04a79fe8.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "4f566e9b-acb6-4b78-aca1-fab30622e0d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T12:18:15.930Z_

<details><summary>↩ Tool result · `toolu_01CqcPm1MMzpTMV7zADkxjLE`</summary>

```text
Async agent launched successfully.
agentId: ac969755edb559a37 (internal ID - do not mention to user. Use SendMessage with to: 'ac969755edb559a37' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/ac969755edb559a37.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a0020b9-309e-417f-9593-d048e33c66ea",
  "isSidechain": false,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "type": "user",
  "uuid": "36c7a6e9-78a2-42a1-98f8-661df9daf0a8",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "ac969755edb559a37",
    "description": "Check venue deadlines 2026",
    "prompt": "I need to find AI/ML/NLP conference deadlines that are AFTER 2026-05-27 (today's date). Use WebSearch to find the submission deadlines for the following venues in 2026 or early 2027:\n\nSearch for each:\n1. \"NeurIPS 2026 submission deadline\" \n2. \"ICLR 2027 submission deadline\"\n3. \"AAAI 2027 submission deadline\"\n4. \"NAACL 2027 submission deadline\"\n5. \"EMNLP 2026 submission deadline\"\n6. \"ICML 2026 submission deadline\"\n7. \"ACL 2027 submission deadline\"\n8. \"COLM 2026 submission deadline\"\n9. \"COLT 2026 submission deadline\"\n10. \"ITP 2026 submission deadline\" (Interactive Theorem Proving)\n11. \"CPP 2027 submission deadline\" (Certified Programs and Proofs)\n12. \"LICS 2026 submission deadline\"\n13. \"IJCAI 2026 submission deadline\"\n14. \"CoNLL 2026 submission deadline\"\n15. \"EACL 2027 submission deadline\"\n16. \"CAV 2026 submission deadline\"\n\nFor each venue, report:\n- The exact submission deadline (with date)\n- Whether it is BEFORE or AFTER 2026-05-27\n- The conference dates\n- Any relevant tracks (e.g., NeurIPS has a Datasets & Benchmarks track)\n\nOnly recommend venues whose deadline is definitively AFTER May 27, 2026. If you can't find a confirmed deadline, note that.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/ac969755edb559a37.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "4a0020b9-309e-417f-9593-d048e33c66ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T12:18:00.795Z_

<details open><summary>🔧 Tool call — Agent · `toolu_018jnnUy67G9qXWG6rRVFjK1`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify references and baselines",
  "prompt": "I need you to verify that several academic papers are real and find their specific baseline numbers. Use WebSearch for each.\n\nPapers to verify:\n1. \"Pseudo-Formalization\" by Barkallah et al., May 2026 — search for this paper, its venue, its key results on ArxivMathGradingBench (specifically the ~50% error detection claim)\n2. \"Safe\" by Liu et al., ACL 2025 — search for this paper about step-level formal verification in Lean 4 with ~80% proof success\n3. \"Hard2Verify\" or process reward models dropping from 78.3% to 37.3% — Zheng et al., 2025\n4. \"miniF2F-Lean Revisited\" 2025 — about autoformalization accuracy\n5. Bhatt et al., 2025 — uncertainty-guided selective verification with SMT\n6. Mu et al., 2026 — adaptive verification allocation, 44% fewer verifier calls on MATH\n\nFor each paper, report:\n- Whether you found it (with URL if possible)\n- The actual venue and year\n- Key quantitative results/numbers\n- If NOT found, say so clearly\n\nAlso search for these specific baseline numbers that the approach would need to beat:\n- Best PRM accuracy on research-level math proofs\n- Safe's formal verification success rate and cost overhead\n- State of the art on ArxivMathGradingBench\n- autoformalization success rates (NL to Lean 4)\n\nReport all findings in detail.",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7b0177a-c9b7-4a14-9f45-e1d0fc2fcfc2",
  "isSidechain": false,
  "requestId": "req_011CbT4QU4GRnpuvgv1XwKCb",
  "type": "assistant",
  "uuid": "92cf22af-cf06-432f-9cd7-71a150688353",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSArFpUDyA54TY9ok9THbT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2713,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2072,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2072,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2713
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

_source line 12 · 2026-05-27T12:18:00.800Z_

<details><summary>↩ Tool result · `toolu_018jnnUy67G9qXWG6rRVFjK1`</summary>

```text
Async agent launched successfully.
agentId: a9a2f7dc93ea0cae4 (internal ID - do not mention to user. Use SendMessage with to: 'a9a2f7dc93ea0cae4' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/a9a2f7dc93ea0cae4.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92cf22af-cf06-432f-9cd7-71a150688353",
  "isSidechain": false,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "type": "user",
  "uuid": "3e28edd7-e308-49ae-96d1-55d63fb575cf",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a9a2f7dc93ea0cae4",
    "description": "Verify references and baselines",
    "prompt": "I need you to verify that several academic papers are real and find their specific baseline numbers. Use WebSearch for each.\n\nPapers to verify:\n1. \"Pseudo-Formalization\" by Barkallah et al., May 2026 — search for this paper, its venue, its key results on ArxivMathGradingBench (specifically the ~50% error detection claim)\n2. \"Safe\" by Liu et al., ACL 2025 — search for this paper about step-level formal verification in Lean 4 with ~80% proof success\n3. \"Hard2Verify\" or process reward models dropping from 78.3% to 37.3% — Zheng et al., 2025\n4. \"miniF2F-Lean Revisited\" 2025 — about autoformalization accuracy\n5. Bhatt et al., 2025 — uncertainty-guided selective verification with SMT\n6. Mu et al., 2026 — adaptive verification allocation, 44% fewer verifier calls on MATH\n\nFor each paper, report:\n- Whether you found it (with URL if possible)\n- The actual venue and year\n- Key quantitative results/numbers\n- If NOT found, say so clearly\n\nAlso search for these specific baseline numbers that the approach would need to beat:\n- Best PRM accuracy on research-level math proofs\n- Safe's formal verification success rate and cost overhead\n- State of the art on ArxivMathGradingBench\n- autoformalization success rates (NL to Lean 4)\n\nReport all findings in detail.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/a9a2f7dc93ea0cae4.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "92cf22af-cf06-432f-9cd7-71a150688353",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-27T12:18:09.408Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UZgYuPVWuJECo9kN87MZ6T`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Find models and implementations",
  "prompt": "I need you to search for the current state-of-the-art in several areas relevant to a research project on selective formal verification of mathematical proofs. Use WebSearch for each query.\n\n1. CURRENT TOP OPEN-SOURCE MODELS FOR AUTOFORMALIZATION (NL math to Lean 4):\n   - Search \"best open source model autoformalization Lean 4 2026\"\n   - Search \"autoformalization language model 2026 state of the art\"\n   - Search \"natural language to Lean 4 translation model 2026\"\n   - What are the top-performing open-source models as of May 2026?\n\n2. CURRENT TOP OPEN-SOURCE MODELS FOR MATHEMATICAL REASONING:\n   - Search \"best open source math reasoning model 2026\"\n   - Search \"top math LLM open source 2026 benchmark\"\n   - What models would be best for LLM-based proof block verification?\n\n3. EXISTING IMPLEMENTATIONS ON GITHUB:\n   - Search GitHub for \"pseudo-formalization proof verification\"\n   - Search GitHub for \"autoformalization Lean 4\"\n   - Search GitHub for \"selective formal verification\"\n   - Search GitHub for \"Safe ACL 2025 formal verification\"\n   - What codebases exist that could be built upon?\n\n4. HARDWARE/DATA REQUIREMENTS:\n   - Search \"autoformalization compute cost GPU hours\"\n   - Search \"Lean 4 theorem proving compute requirements\"\n   - What are typical GPU requirements for autoformalization experiments?\n\n5. LEAN 4 THEOREM PROVERS:\n   - Search \"Lean 4 automated theorem prover 2026 state of the art\"\n   - Search \"LeanDojo ReProver 2026\"\n   - What are the best current Lean 4 proof search tools?\n\nReport all findings with specifics (model names, sizes, benchmark scores, URLs).",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e28edd7-e308-49ae-96d1-55d63fb575cf",
  "isSidechain": false,
  "requestId": "req_011CbT4QU4GRnpuvgv1XwKCb",
  "type": "assistant",
  "uuid": "2544c7de-4af9-44d9-83ff-5839d1919f65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSArFpUDyA54TY9ok9THbT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2713,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2072,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2072,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2713
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

_source line 14 · 2026-05-27T12:18:09.419Z_

<details><summary>↩ Tool result · `toolu_01UZgYuPVWuJECo9kN87MZ6T`</summary>

```text
Async agent launched successfully.
agentId: a8ad2fc8d499fe316 (internal ID - do not mention to user. Use SendMessage with to: 'a8ad2fc8d499fe316' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/a8ad2fc8d499fe316.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2544c7de-4af9-44d9-83ff-5839d1919f65",
  "isSidechain": false,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "type": "user",
  "uuid": "682e4678-1076-4502-9152-d0db4c82230e",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a8ad2fc8d499fe316",
    "description": "Find models and implementations",
    "prompt": "I need you to search for the current state-of-the-art in several areas relevant to a research project on selective formal verification of mathematical proofs. Use WebSearch for each query.\n\n1. CURRENT TOP OPEN-SOURCE MODELS FOR AUTOFORMALIZATION (NL math to Lean 4):\n   - Search \"best open source model autoformalization Lean 4 2026\"\n   - Search \"autoformalization language model 2026 state of the art\"\n   - Search \"natural language to Lean 4 translation model 2026\"\n   - What are the top-performing open-source models as of May 2026?\n\n2. CURRENT TOP OPEN-SOURCE MODELS FOR MATHEMATICAL REASONING:\n   - Search \"best open source math reasoning model 2026\"\n   - Search \"top math LLM open source 2026 benchmark\"\n   - What models would be best for LLM-based proof block verification?\n\n3. EXISTING IMPLEMENTATIONS ON GITHUB:\n   - Search GitHub for \"pseudo-formalization proof verification\"\n   - Search GitHub for \"autoformalization Lean 4\"\n   - Search GitHub for \"selective formal verification\"\n   - Search GitHub for \"Safe ACL 2025 formal verification\"\n   - What codebases exist that could be built upon?\n\n4. HARDWARE/DATA REQUIREMENTS:\n   - Search \"autoformalization compute cost GPU hours\"\n   - Search \"Lean 4 theorem proving compute requirements\"\n   - What are typical GPU requirements for autoformalization experiments?\n\n5. LEAN 4 THEOREM PROVERS:\n   - Search \"Lean 4 automated theorem prover 2026 state of the art\"\n   - Search \"LeanDojo ReProver 2026\"\n   - What are the best current Lean 4 proof search tools?\n\nReport all findings with specifics (model names, sizes, benchmark scores, URLs).",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/a8ad2fc8d499fe316.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "2544c7de-4af9-44d9-83ff-5839d1919f65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T12:18:15.924Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01CqcPm1MMzpTMV7zADkxjLE`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check venue deadlines 2026",
  "prompt": "I need to find AI/ML/NLP conference deadlines that are AFTER 2026-05-27 (today's date). Use WebSearch to find the submission deadlines for the following venues in 2026 or early 2027:\n\nSearch for each:\n1. \"NeurIPS 2026 submission deadline\" \n2. \"ICLR 2027 submission deadline\"\n3. \"AAAI 2027 submission deadline\"\n4. \"NAACL 2027 submission deadline\"\n5. \"EMNLP 2026 submission deadline\"\n6. \"ICML 2026 submission deadline\"\n7. \"ACL 2027 submission deadline\"\n8. \"COLM 2026 submission deadline\"\n9. \"COLT 2026 submission deadline\"\n10. \"ITP 2026 submission deadline\" (Interactive Theorem Proving)\n11. \"CPP 2027 submission deadline\" (Certified Programs and Proofs)\n12. \"LICS 2026 submission deadline\"\n13. \"IJCAI 2026 submission deadline\"\n14. \"CoNLL 2026 submission deadline\"\n15. \"EACL 2027 submission deadline\"\n16. \"CAV 2026 submission deadline\"\n\nFor each venue, report:\n- The exact submission deadline (with date)\n- Whether it is BEFORE or AFTER 2026-05-27\n- The conference dates\n- Any relevant tracks (e.g., NeurIPS has a Datasets & Benchmarks track)\n\nOnly recommend venues whose deadline is definitively AFTER May 27, 2026. If you can't find a confirmed deadline, note that.",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "682e4678-1076-4502-9152-d0db4c82230e",
  "isSidechain": false,
  "requestId": "req_011CbT4QU4GRnpuvgv1XwKCb",
  "type": "assistant",
  "uuid": "4a0020b9-309e-417f-9593-d048e33c66ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSArFpUDyA54TY9ok9THbT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2713,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2072,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2072,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2713
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

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Uncertainty-Guided Selec…",
  "leafUuid": "36c7a6e9-78a2-42a1-98f8-661df9daf0a8",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective proof block formalization",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Assistant

_source line 18 · 2026-05-27T12:18:19.725Z_

<details><summary>Logged reasoning block</summary>

```text
I've launched 4 background agents to research in parallel:
1. Concurrent work search
2. Reference verification and baselines
3. Models and implementations
4. Venue deadlines

I'll wait for all of them to complete before synthesizing the final JSON output. Let me let the user know what's happening.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36c7a6e9-78a2-42a1-98f8-661df9daf0a8",
  "isSidechain": false,
  "requestId": "req_011CbT4T6FBVydanJWgt6nj3",
  "type": "assistant",
  "uuid": "7b086975-a654-4135-89ff-38ac240dcbaf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6m8oKZxwH3jxKxU43grsG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3108,
      "cache_read_input_tokens": 13727,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 302,
          "cache_read_input_tokens": 13727,
          "cache_creation_input_tokens": 3108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3108
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

_source line 19 · 2026-05-27T12:18:21.988Z_

I've launched four parallel research agents to gather all the information needed:

1. **Concurrent work search** — checking arXiv, OpenReview, and the web for competing/similar papers from 2025-2026
2. **Reference verification** — verifying all cited papers are real and collecting baseline numbers
3. **Models & implementations** — finding current SOTA open-source models for autoformalization and math reasoning, plus existing codebases
4. **Venue deadlines** — checking which top-tier venues still have open deadlines after May 27, 2026

I'll synthesize everything into the final JSON once all agents report back.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b086975-a654-4135-89ff-38ac240dcbaf",
  "isSidechain": false,
  "requestId": "req_011CbT4T6FBVydanJWgt6nj3",
  "type": "assistant",
  "uuid": "1dbf4cc0-bb70-4a77-a2cc-2af5aff1d04f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6m8oKZxwH3jxKxU43grsG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3108,
      "cache_read_input_tokens": 13727,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 302,
          "cache_read_input_tokens": 13727,
          "cache_creation_input_tokens": 3108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3108
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

_source line 20 · 2026-05-27T12:18:22.493Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SQ8rhrsBj2qt4E1CYMTmuE`</summary>

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
  "parentUuid": "1dbf4cc0-bb70-4a77-a2cc-2af5aff1d04f",
  "isSidechain": false,
  "requestId": "req_011CbT4T6FBVydanJWgt6nj3",
  "type": "assistant",
  "uuid": "dba6a07d-a4b0-490e-9d92-b29229229a0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6m8oKZxwH3jxKxU43grsG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3108,
      "cache_read_input_tokens": 13727,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 302,
          "cache_read_input_tokens": 13727,
          "cache_creation_input_tokens": 3108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3108
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

_source line 21 · 2026-05-27T12:18:22.499Z_

<details><summary>↩ Tool result · `toolu_01SQ8rhrsBj2qt4E1CYMTmuE`</summary>

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
  "parentUuid": "dba6a07d-a4b0-490e-9d92-b29229229a0d",
  "isSidechain": false,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "type": "user",
  "uuid": "33cbbbe1-ddc8-4a6f-85a9-a79077377005",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "dba6a07d-a4b0-490e-9d92-b29229229a0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-27T12:18:25.363Z_

<details><summary>Logged reasoning block</summary>

```text
Good, WebSearch is now loaded. Let me wait for the background agents to complete before proceeding. I'll be notified when they finish.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33cbbbe1-ddc8-4a6f-85a9-a79077377005",
  "isSidechain": false,
  "requestId": "req_011CbT4TaUZNoDqtZkrXRgyT",
  "type": "assistant",
  "uuid": "f01a7186-6970-4c31-b5dd-2ff269cfc827",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCdoZGSxyL2Kb4ctULe79e",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 16835,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 81,
          "cache_read_input_tokens": 16835,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 829
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

_source line 23 · 2026-05-27T12:18:25.630Z_

Good, WebSearch is loaded. I'm waiting for all four background research agents to complete their work. I'll be notified automatically when each finishes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f01a7186-6970-4c31-b5dd-2ff269cfc827",
  "isSidechain": false,
  "requestId": "req_011CbT4TaUZNoDqtZkrXRgyT",
  "type": "assistant",
  "uuid": "9c51d4a2-c54c-4e3d-9f6c-35ca7b9c8701",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCdoZGSxyL2Kb4ctULe79e",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 16835,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 81,
          "cache_read_input_tokens": 16835,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 829
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

_source line 24 · 2026-05-27T12:20:04.925Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T12:20:04.925Z",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "content": "&lt;task-notification>\n&lt;task-id>ac969755edb559a37&lt;/task-id>\n&lt;tool-use-id>toolu_01CqcPm1MMzpTMV7zADkxjLE&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/ac969755edb559a37.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Check venue deadlines 2026\" completed&lt;/summary>\n&lt;result>Now I have comprehensive information for all 16 venues. Here is my complete report:\n\n---\n\n## Conference Deadline Report (relative to today: May 27, 2026)\n\n### VENUES WITH DEADLINES DEFINITIVELY AFTER MAY 27, 2026 (Recommended)\n\n**1. AAAI 2027**\n- Abstract deadline: **July 21, 2026** | Full paper deadline: **July 28, 2026** (11:59 PM UTC-12)\n- Supplementary material/code: July 31, 2026\n- Conference dates: February 16-23, 2027, Montreal, Canada\n- Tracks: Main Technical Track + additional special tracks (track-specific deadlines on their respective CFPs)\n- Status: **AFTER** today -- RECOMMENDED\n\n**2. EACL 2027**\n- ARR submission deadline: **August 3, 2026** (11:59 PM AoE)\n- Conference dates: March 9-14, 2027, Athens, Greece\n- Note: This is the only viable ARR cycle since EACL is earlier than usual in 2027\n- Status: **AFTER** today -- RECOMMENDED\n\n**3. EMNLP 2026** (two pathways)\n- ARR submission deadline: **May 25, 2026** -- this deadline has PASSED (2 days ago)\n- ARR commitment deadline: **August 2, 2026** (AoE) -- if you already have ARR reviews, you can still commit\n- Conference dates: October 24-29, 2026, Budapest, Hungary\n- Status: ARR submission is **BEFORE** today (missed by 2 days). Commitment deadline is **AFTER** today, but only useful if you have existing ARR reviews from another cycle.\n\n**4. COLM 2026 Workshops**\n- Main conference paper deadline (March 31, 2026) has PASSED\n- Workshop contribution suggested deadline: **June 23, 2026**\n- Conference dates: October 6-9, 2026, San Francisco, USA (Hilton Union Square)\n- Status: Main track is **BEFORE** today. Workshop deadline is **AFTER** today.\n\n**5. ACL 2027** (via ARR)\n- ACL 2026 (San Diego, July 2-7, 2026) commitment deadline was March 14, 2026 -- PASSED\n- ACL 2027 dates and deadlines are not yet officially announced\n- You can submit to any upcoming ARR cycle and commit to ACL 2027 when announced\n- Status: **Not yet announced** -- likely to be AFTER today\n\n**6. NAACL 2027** (via ARR)\n- Predicted conference dates: ~April-May 2027 (location TBA)\n- Specific ARR submission/commitment deadlines not yet announced\n- Status: **Not yet announced** -- likely to be AFTER today\n\n---\n\n### VENUES WITH DEADLINES BEFORE MAY 27, 2026 (Already Passed)\n\n**7. NeurIPS 2026**\n- Abstract deadline: May 4, 2026 (AoE) -- **PASSED**\n- Full paper deadline: May 6, 2026 (AoE) -- **PASSED**\n- Conference dates: December 6-12, 2026, Sydney, Australia (satellites in Atlanta and Paris)\n- Tracks: Main Submission, Evaluations &amp; Datasets (renamed from Datasets &amp; Benchmarks), Position Papers. All tracks shared the same deadlines.\n- Status: **BEFORE** today -- NOT recommended\n\n**8. ICML 2026**\n- Paper submission deadline: January 28, 2026 -- **PASSED**\n- Position papers deadline: January 29, 2026 -- **PASSED**\n- Conference dates: July 6-11, 2026, COEX Convention Center, Seoul, South Korea\n- Status: **BEFORE** today -- NOT recommended\n\n**9. COLM 2026** (main track)\n- Abstract deadline: March 26, 2026 -- **PASSED**\n- Full paper deadline: March 31, 2026 -- **PASSED**\n- Conference dates: October 6-9, 2026, San Francisco, USA\n- Status: **BEFORE** today -- NOT recommended\n\n**10. COLT 2026**\n- Submission deadline: February 4, 2026 (AoE) -- **PASSED**\n- Conference dates: June 29 - July 3, 2026, San Diego, USA\n- Status: **BEFORE** today -- NOT recommended\n\n**11. ITP 2026**\n- Abstract deadline: February 12, 2026 -- **PASSED**\n- Paper deadline: February 19, 2026 -- **PASSED**\n- Conference dates: July 26-29, 2026, Lisbon, Portugal (part of FLoC 2026)\n- Status: **BEFORE** today -- NOT recommended\n\n**12. LICS 2026**\n- Abstract deadline: January 15, 2026 -- **PASSED**\n- Full paper deadline: January 22, 2026 -- **PASSED**\n- Conference dates: July 20-23, 2026, Lisbon, Portugal (part of FLoC 2026)\n- Status: **BEFORE** today -- NOT recommended\n\n**13. IJCAI 2026**\n- Abstract deadline: January 12, 2026 -- **PASSED**\n- Full paper deadline: January 19, 2026 -- **PASSED**\n- Conference dates: August 15-21, 2026, Bremen, Germany\n- Tracks: Main Track, Human-Centred AI, AI for Social Good, AI4Tech, AI and Health, AI and Robotics, Survey Track, Demonstrations Track\n- Status: **BEFORE** today -- NOT recommended\n\n**14. CoNLL 2026**\n- Submission deadline: February 19, 2026 (AoE) -- **PASSED**\n- Conference dates: July 3-4, 2026, San Diego (co-located with ACL 2026)\n- Status: **BEFORE** today -- NOT recommended\n\n**15. CAV 2026**\n- Paper submission deadline: January 28, 2026 (AoE) -- **PASSED**\n- Conference dates: July 26-29, 2026, Lisbon, Portugal (part of FLoC 2026)\n- Status: **BEFORE** today -- NOT recommended\n\n**16. CPP 2027**\n- Co-located with POPL 2027 (Mexico City), January 2027\n- Submission deadline: **Not yet announced**. Based on past years (e.g., CPP 2025 had a September 2024 deadline), expect around **September 2026**.\n- PC Chairs: Nikhil Swamy and Cyril Cohen\n- Status: **Not yet announced** -- likely to be AFTER today (estimated ~September 2026)\n\n---\n\n### SUMMARY: Definitive Recommendations (deadlines after May 27, 2026)\n\n| Venue | Deadline | Conference Dates |\n|-------|----------|-----------------|\n| **AAAI 2027** | July 21/28, 2026 | Feb 16-23, 2027 (Montreal) |\n| **EACL 2027** | Aug 3, 2026 (ARR) | Mar 9-14, 2027 (Athens) |\n| **EMNLP 2026** (commitment only) | Aug 2, 2026 | Oct 24-29, 2026 (Budapest) |\n| **CPP 2027** (estimated) | ~Sep 2026 (TBA) | Jan 2027 (Mexico City) |\n| **NAACL 2027** (TBA) | TBA | ~Apr-May 2027 (TBA) |\n| **ACL 2027** (TBA) | TBA | TBA |\n\nThe two strongest, confirmed-deadline options are **AAAI 2027** (abstract July 21, paper July 28) and **EACL 2027** (ARR submission August 3). If you have existing ARR-reviewed papers, the **EMNLP 2026 commitment deadline** (August 2) is also viable.\n\nSources:\n- [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates)\n- [NeurIPS 2026 Call for Papers](https://neurips.cc/Conferences/2026/CallForPapers)\n- [NeurIPS 2026 Evaluations &amp; Datasets Track](https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets)\n- [ICLR 2026 Dates](https://iclr.cc/Conferences/2026/Dates)\n- [AAAI-27 Conference](https://aaai.org/conference/aaai/aaai-27/)\n- [AAAI-27 Main Technical Track](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)\n- [EMNLP 2026](https://2026.emnlp.org/)\n- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n- [ICML 2026 Dates](https://icml.cc/Conferences/2026/Dates)\n- [ICML 2026 Call for Papers](https://icml.cc/Conferences/2026/CallForPapers)\n- [ACL 2026](https://2026.aclweb.org/)\n- [COLM 2026 Key Dates](https://colmweb.org/dates.html)\n- [COLM 2026 Call for Papers](https://colmweb.org/cfp.html)\n- [COLT 2026 Call for Papers](https://learningtheory.org/colt2026/cfp.html)\n- [ITP 2026](https://itp-conference-2026.github.io/)\n- [CPP Conference (SIGPLAN)](https://sigplan.org/Conferences/CPP/)\n- [LICS 2026 Call for Papers](https://lics.siglog.org/lics26/cfp.php)\n- [IJCAI 2026 Important Dates](https://2026.ijcai.org/important-dates/)\n- [IJCAI 2026](https://2026.ijcai.org/)\n- [CoNLL 2026](https://conll.org/)\n- [EACL 2027](https://2027.eacl.org/)\n- [EACL 2027 Call for Papers](https://2027.eacl.org/calls/papers/)\n- [CAV 2026](http://conferences.i-cav.org/2026/)\n- [CAV 2026 Call for Papers](http://conferences.i-cav.org/2026/cfp/)\n- [ARR Dates and Venues](http://aclrollingreview.org/dates)\n- [POPL 2027](https://popl27.sigplan.org/)\n- [AI Conference Deadlines](https://mlciv.com/ai-deadlines/)&lt;/result>\n&lt;usage>&lt;total_tokens>31480&lt;/total_tokens>&lt;tool_uses>29&lt;/tool_uses>&lt;duration_ms>108998&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 25 · 2026-05-27T12:20:04.949Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T12:20:04.949Z",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

## Round 2

7 recorded events

### User

_source line 26 · 2026-05-27T12:20:04.964Z_

&lt;task-notification>
&lt;task-id>ac969755edb559a37&lt;/task-id>
&lt;tool-use-id>toolu_01CqcPm1MMzpTMV7zADkxjLE&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/ac969755edb559a37.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Check venue deadlines 2026" completed&lt;/summary>
&lt;result>Now I have comprehensive information for all 16 venues. Here is my complete report:

---

## Conference Deadline Report (relative to today: May 27, 2026)

### VENUES WITH DEADLINES DEFINITIVELY AFTER MAY 27, 2026 (Recommended)

**1. AAAI 2027**
- Abstract deadline: **July 21, 2026** | Full paper deadline: **July 28, 2026** (11:59 PM UTC-12)
- Supplementary material/code: July 31, 2026
- Conference dates: February 16-23, 2027, Montreal, Canada
- Tracks: Main Technical Track + additional special tracks (track-specific deadlines on their respective CFPs)
- Status: **AFTER** today -- RECOMMENDED

**2. EACL 2027**
- ARR submission deadline: **August 3, 2026** (11:59 PM AoE)
- Conference dates: March 9-14, 2027, Athens, Greece
- Note: This is the only viable ARR cycle since EACL is earlier than usual in 2027
- Status: **AFTER** today -- RECOMMENDED

**3. EMNLP 2026** (two pathways)
- ARR submission deadline: **May 25, 2026** -- this deadline has PASSED (2 days ago)
- ARR commitment deadline: **August 2, 2026** (AoE) -- if you already have ARR reviews, you can still commit
- Conference dates: October 24-29, 2026, Budapest, Hungary
- Status: ARR submission is **BEFORE** today (missed by 2 days). Commitment deadline is **AFTER** today, but only useful if you have existing ARR reviews from another cycle.

**4. COLM 2026 Workshops**
- Main conference paper deadline (March 31, 2026) has PASSED
- Workshop contribution suggested deadline: **June 23, 2026**
- Conference dates: October 6-9, 2026, San Francisco, USA (Hilton Union Square)
- Status: Main track is **BEFORE** today. Workshop deadline is **AFTER** today.

**5. ACL 2027** (via ARR)
- ACL 2026 (San Diego, July 2-7, 2026) commitment deadline was March 14, 2026 -- PASSED
- ACL 2027 dates and deadlines are not yet officially announced
- You can submit to any upcoming ARR cycle and commit to ACL 2027 when announced
- Status: **Not yet announced** -- likely to be AFTER today

**6. NAACL 2027** (via ARR)
- Predicted conference dates: ~April-May 2027 (location TBA)
- Specific ARR submission/commitment deadlines not yet announced
- Status: **Not yet announced** -- likely to be AFTER today

---

### VENUES WITH DEADLINES BEFORE MAY 27, 2026 (Already Passed)

**7. NeurIPS 2026**
- Abstract deadline: May 4, 2026 (AoE) -- **PASSED**
- Full paper deadline: May 6, 2026 (AoE) -- **PASSED**
- Conference dates: December 6-12, 2026, Sydney, Australia (satellites in Atlanta and Paris)
- Tracks: Main Submission, Evaluations &amp; Datasets (renamed from Datasets &amp; Benchmarks), Position Papers. All tracks shared the same deadlines.
- Status: **BEFORE** today -- NOT recommended

**8. ICML 2026**
- Paper submission deadline: January 28, 2026 -- **PASSED**
- Position papers deadline: January 29, 2026 -- **PASSED**
- Conference dates: July 6-11, 2026, COEX Convention Center, Seoul, South Korea
- Status: **BEFORE** today -- NOT recommended

**9. COLM 2026** (main track)
- Abstract deadline: March 26, 2026 -- **PASSED**
- Full paper deadline: March 31, 2026 -- **PASSED**
- Conference dates: October 6-9, 2026, San Francisco, USA
- Status: **BEFORE** today -- NOT recommended

**10. COLT 2026**
- Submission deadline: February 4, 2026 (AoE) -- **PASSED**
- Conference dates: June 29 - July 3, 2026, San Diego, USA
- Status: **BEFORE** today -- NOT recommended

**11. ITP 2026**
- Abstract deadline: February 12, 2026 -- **PASSED**
- Paper deadline: February 19, 2026 -- **PASSED**
- Conference dates: July 26-29, 2026, Lisbon, Portugal (part of FLoC 2026)
- Status: **BEFORE** today -- NOT recommended

**12. LICS 2026**
- Abstract deadline: January 15, 2026 -- **PASSED**
- Full paper deadline: January 22, 2026 -- **PASSED**
- Conference dates: July 20-23, 2026, Lisbon, Portugal (part of FLoC 2026)
- Status: **BEFORE** today -- NOT recommended

**13. IJCAI 2026**
- Abstract deadline: January 12, 2026 -- **PASSED**
- Full paper deadline: January 19, 2026 -- **PASSED**
- Conference dates: August 15-21, 2026, Bremen, Germany
- Tracks: Main Track, Human-Centred AI, AI for Social Good, AI4Tech, AI and Health, AI and Robotics, Survey Track, Demonstrations Track
- Status: **BEFORE** today -- NOT recommended

**14. CoNLL 2026**
- Submission deadline: February 19, 2026 (AoE) -- **PASSED**
- Conference dates: July 3-4, 2026, San Diego (co-located with ACL 2026)
- Status: **BEFORE** today -- NOT recommended

**15. CAV 2026**
- Paper submission deadline: January 28, 2026 (AoE) -- **PASSED**
- Conference dates: July 26-29, 2026, Lisbon, Portugal (part of FLoC 2026)
- Status: **BEFORE** today -- NOT recommended

**16. CPP 2027**
- Co-located with POPL 2027 (Mexico City), January 2027
- Submission deadline: **Not yet announced**. Based on past years (e.g., CPP 2025 had a September 2024 deadline), expect around **September 2026**.
- PC Chairs: Nikhil Swamy and Cyril Cohen
- Status: **Not yet announced** -- likely to be AFTER today (estimated ~September 2026)

---

### SUMMARY: Definitive Recommendations (deadlines after May 27, 2026)

| Venue | Deadline | Conference Dates |
|-------|----------|-----------------|
| **AAAI 2027** | July 21/28, 2026 | Feb 16-23, 2027 (Montreal) |
| **EACL 2027** | Aug 3, 2026 (ARR) | Mar 9-14, 2027 (Athens) |
| **EMNLP 2026** (commitment only) | Aug 2, 2026 | Oct 24-29, 2026 (Budapest) |
| **CPP 2027** (estimated) | ~Sep 2026 (TBA) | Jan 2027 (Mexico City) |
| **NAACL 2027** (TBA) | TBA | ~Apr-May 2027 (TBA) |
| **ACL 2027** (TBA) | TBA | TBA |

The two strongest, confirmed-deadline options are **AAAI 2027** (abstract July 21, paper July 28) and **EACL 2027** (ARR submission August 3). If you have existing ARR-reviewed papers, the **EMNLP 2026 commitment deadline** (August 2) is also viable.

Sources:
- [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates)
- [NeurIPS 2026 Call for Papers](https://neurips.cc/Conferences/2026/CallForPapers)
- [NeurIPS 2026 Evaluations &amp; Datasets Track](https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets)
- [ICLR 2026 Dates](https://iclr.cc/Conferences/2026/Dates)
- [AAAI-27 Conference](https://aaai.org/conference/aaai/aaai-27/)
- [AAAI-27 Main Technical Track](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)
- [EMNLP 2026](https://2026.emnlp.org/)
- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ICML 2026 Dates](https://icml.cc/Conferences/2026/Dates)
- [ICML 2026 Call for Papers](https://icml.cc/Conferences/2026/CallForPapers)
- [ACL 2026](https://2026.aclweb.org/)
- [COLM 2026 Key Dates](https://colmweb.org/dates.html)
- [COLM 2026 Call for Papers](https://colmweb.org/cfp.html)
- [COLT 2026 Call for Papers](https://learningtheory.org/colt2026/cfp.html)
- [ITP 2026](https://itp-conference-2026.github.io/)
- [CPP Conference (SIGPLAN)](https://sigplan.org/Conferences/CPP/)
- [LICS 2026 Call for Papers](https://lics.siglog.org/lics26/cfp.php)
- [IJCAI 2026 Important Dates](https://2026.ijcai.org/important-dates/)
- [IJCAI 2026](https://2026.ijcai.org/)
- [CoNLL 2026](https://conll.org/)
- [EACL 2027](https://2027.eacl.org/)
- [EACL 2027 Call for Papers](https://2027.eacl.org/calls/papers/)
- [CAV 2026](http://conferences.i-cav.org/2026/)
- [CAV 2026 Call for Papers](http://conferences.i-cav.org/2026/cfp/)
- [ARR Dates and Venues](http://aclrollingreview.org/dates)
- [POPL 2027](https://popl27.sigplan.org/)
- [AI Conference Deadlines](https://mlciv.com/ai-deadlines/)&lt;/result>
&lt;usage>&lt;total_tokens>31480&lt;/total_tokens>&lt;tool_uses>29&lt;/tool_uses>&lt;duration_ms>108998&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c51d4a2-c54c-4e3d-9f6c-35ca7b9c8701",
  "isSidechain": false,
  "promptId": "9b06605d-7e70-447b-9d1c-b9dfe27e0c9d",
  "type": "user",
  "uuid": "d03cc9e9-6b97-4015-902d-666d488665c6",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-27T12:20:09.677Z_

<details><summary>Logged reasoning block</summary>

```text
The venue deadlines agent has completed. Key findings:
- AAAI 2027: July 21/28, 2026 deadline — AFTER today ✓
- EACL 2027: Aug 3, 2026 (ARR) — AFTER today ✓
- EMNLP 2026: commitment only Aug 2, 2026 — only if you have existing ARR reviews
- CPP 2027: ~Sep 2026 (TBA)
- NeurIPS 2026: PASSED (May 4/6)
- ICML 2026: PASSED

Still waiting for the other 3 agents. 

Waiting on the remaining agents...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d03cc9e9-6b97-4015-902d-666d488665c6",
  "isSidechain": false,
  "requestId": "req_011CbT4b88m5tMteH8PKT46G",
  "type": "assistant",
  "uuid": "17895a5c-cac2-415a-8e4e-170bde65fe1f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01136zqGshbEkNiVKvVqEzV4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3038,
      "cache_read_input_tokens": 17664,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3038,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 289,
          "cache_read_input_tokens": 17664,
          "cache_creation_input_tokens": 3038,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3038
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

_source line 28 · 2026-05-27T12:20:10.683Z_

Venue deadlines agent completed. Key findings:
- **AAAI 2027** (July 28, 2026 deadline) ✓
- **EACL 2027** (Aug 3, 2026 ARR deadline) ✓
- NeurIPS 2026, ICML 2026, IJCAI 2026 — all passed

Still waiting on the other three research agents (concurrent work, references, models/implementations).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17895a5c-cac2-415a-8e4e-170bde65fe1f",
  "isSidechain": false,
  "requestId": "req_011CbT4b88m5tMteH8PKT46G",
  "type": "assistant",
  "uuid": "04ff1d63-17c6-4ce4-98ec-edf48f40f16f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01136zqGshbEkNiVKvVqEzV4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3038,
      "cache_read_input_tokens": 17664,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3038,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 289,
          "cache_read_input_tokens": 17664,
          "cache_creation_input_tokens": 3038,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3038
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

_source line 29 · 2026-05-27T12:20:51.275Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T12:20:51.275Z",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "content": "&lt;task-notification>\n&lt;task-id>a8ad2fc8d499fe316&lt;/task-id>\n&lt;tool-use-id>toolu_01UZgYuPVWuJECo9kN87MZ6T&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/a8ad2fc8d499fe316.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Find models and implementations\" completed&lt;/summary>\n&lt;result>I now have comprehensive findings across all five areas. Here is the full report.\n\n---\n\n# Research Landscape: Selective Formal Verification of Mathematical Proofs (May 2026)\n\n## 1. TOP OPEN-SOURCE MODELS FOR AUTOFORMALIZATION (NL Math to Lean 4)\n\n### Tier 1: Purpose-Built Autoformalization Models\n\n- **Leanstral (Mistral AI, March 2026)** -- The first open-source AI agent built specifically for Lean 4. 120B total parameters, only 6B active per token (sparse MoE). Apache 2.0 license. On the FLTEval benchmark (Fermat's Last Theorem formalization), it scores 26.3 pass@2 at $36 cost, beating Claude Sonnet 4.6 (23.7 at $549). Integrates with Lean LSP via MCP. Weights available for self-deployment.\n  - GitHub/API: Free endpoint `labs-leanstral-2603`\n\n- **StepFun-Formalizer (StepFun AI)** -- Available in 7B and 32B variants, Apache 2.0. Specifically designed for NL-to-Lean-4 translation. StepFun-Formalizer-32B achieves SOTA BEq@1 scores of 40.5% on FormalMATH-Lite and 26.7% on ProverBench. Training takes ~56 hours for the 32B model. Weights on HuggingFace (`stepfun-ai/StepFun-Formalizer-32B`).\n  - GitHub: [github.com/stepfun-ai/StepFun-Formalizer](https://github.com/stepfun-ai/StepFun-Formalizer)\n\n- **Herald Translator** -- Fine-tuned on the Herald dataset (580K valid statements, 44K NL-FL theorem pairs from Mathlib4). Achieves 96.7% accuracy on miniF2F-test for statement formalization. Model size not explicitly documented.\n  - GitHub: [github.com/frenzymath/herald_translator](https://github.com/frenzymath/herald_translator)\n\n- **ATLAS Translator** -- Iterative data generation framework. Achieves 91.60% on miniF2F, 80.59% on ProofNet, 65.47% on MathQual (pass@8). At pass@128: 96.93%, 92.99%, 84.72% respectively.\n\n### Tier 2: General Autoformalization Approaches\n\n- **ProofBridge** -- Joint embedding model for translating entire NL theorems+proofs into Lean 4. Reported to outperform GPT-5 and Gemini-2.5 baselines.\n- **NL2Lean** -- Uses curriculum learning + multi-reward model for NL-to-Lean-4 translation (EMNLP 2025).\n- **MASA (Multi-Agent Autoformalization)** -- Multi-agent system with LLM, knowledge base, retriever, and theorem prover components.\n  - GitHub: [github.com/lanzhang128/multi_agent_autoformalization](https://github.com/lanzhang128/multi_agent_autoformalization)\n- **Process-Driven Autoformalization (PDA)** -- Uses Lean 4 compiler feedback to refine autoformalization iteratively. Published with the FORML4 dataset.\n  - GitHub: [github.com/rookie-joe/PDA](https://github.com/rookie-joe/PDA)\n\n## 2. TOP OPEN-SOURCE MODELS FOR MATHEMATICAL REASONING\n\n### Best for LLM-Based Proof Block Verification\n\n- **DeepSeek-R1** -- Elite-level reasoning, comparable to OpenAI o1. Strong chain-of-thought with extended reasoning traces. Best raw reasoning performance among open-source models.\n- **Qwen/QwQ-32B** -- Best balance of capability and efficiency. Strong math reasoning in a 32B package.\n- **Qwen 3 235B** -- Leads broadest range of benchmarks (Apache 2.0). Top-tier reasoning, coding, multilingual.\n- **GLM-5 (THUDM)** -- Scores 94.2 HumanEval, 95.7 AIME 2025, 85.7 GPQA Diamond.\n- **GLM-Z1-9B-0414** -- Surprisingly strong math in a lightweight 9B package, good for resource-constrained deployments.\n- **DeepSeek V3.2/V4** -- Unified thinking-mode models that integrate reasoning into standard chat, better for production deployments.\n\n**Recommendation for proof block verification:** DeepSeek-R1 or QwQ-32B for reasoning quality; GLM-Z1-9B for efficiency. For a selective verification pipeline, QwQ-32B offers the best quality-to-cost tradeoff.\n\n## 3. EXISTING IMPLEMENTATIONS ON GITHUB\n\n### Directly Relevant Codebases\n\n- **Safe (ACL 2025 Main)** -- **Most directly relevant to your project.** Retrospective step-aware formal verification of LLM mathematical reasoning. Translates each reasoning step to Lean 4, then proves correctness. Includes the FormalStep dataset (30,809 formal statements). Authors: Chengwu Liu et al.\n  - GitHub: [github.com/liuchengwucn/Safe](https://github.com/liuchengwucn/Safe)\n  - Paper: [aclanthology.org/2025.acl-long.594](https://aclanthology.org/2025.acl-long.594/)\n\n- **Goedel-Prover / Goedel-Prover-V2** -- Open-source ATP for Lean 4. V2-32B: 88.1% pass@32 on MiniF2F (90.4% with self-correction). Outperforms DeepSeek-Prover-V2-671B with 1/20th the parameters. The 8B variant hits 84.6% pass@32.\n  - GitHub: [github.com/Goedel-LM/Goedel-Prover](https://github.com/Goedel-LM/Goedel-Prover)\n\n- **LeanAide** -- AI tools for Lean 4 using autoformalization as core technique.\n  - GitHub: [github.com/siddhartha-gadgil/LeanAide](https://github.com/siddhartha-gadgil/LeanAide)\n\n- **LeanDojo / ReProver / LeanCopilot** -- Comprehensive ecosystem for AI-assisted theorem proving in Lean 4. ReProver is retrieval-augmented. LeanCopilot provides in-editor tactic suggestion, proof search, and premise selection. LeanDojo-v2 presented at NeurIPS 2025.\n  - GitHub: [github.com/lean-dojo/LeanCopilot](https://github.com/lean-dojo/LeanCopilot)\n  - GitHub: [github.com/lean-dojo/ReProver](https://github.com/lean-dojo/ReProver)\n  - Docs: [leandojo.readthedocs.io](https://leandojo.readthedocs.io/en/latest/index.html)\n\n- **LeanInteract** -- Python interface for Lean 4, useful for running autoformalization benchmarks (MiniF2F, ProofNet) programmatically.\n  - GitHub: [github.com/augustepoiroux/LeanInteract](https://github.com/augustepoiroux/LeanInteract)\n\n- **DL4TP** -- Comprehensive survey repo on deep learning for theorem proving (COLM 2024).\n  - GitHub: [github.com/zhaoyu-li/DL4TP](https://github.com/zhaoyu-li/DL4TP)\n\n### Datasets\n\n- **FormalStep** (from Safe): 30,809 formal statements for step-correctness verification\n- **FORML4** (from PDA): Autoformalization dataset built by informalizing Mathlib 4 theorems\n- **Herald**: 580K statements, 44K NL-FL pairs from Mathlib4\n- **Numina-ATF**: 750K synthetic formal statements for ATP research\n- **StepFun-Formalizer-Training**: Training data on HuggingFace\n\n## 4. HARDWARE / DATA REQUIREMENTS\n\n### Fine-Tuning Autoformalization Models (LoRA/QLoRA)\n\n| Model Size | Technique | VRAM Required | Hardware | Time Estimate |\n|-----------|-----------|--------------|----------|--------------|\n| 7B | QLoRA (4-bit) | ~8 GB | Single RTX 4070 Ti | Hours (afternoon) |\n| 7B | LoRA | ~16 GB | Single RTX 4090 / A5000 | Hours |\n| 32B | QLoRA (4-bit) | ~24 GB | Single RTX 4090 / A6000 | ~46-56 hours |\n| 70B | QLoRA (4-bit) | ~46 GB | Single A100-80GB | Days |\n\n**Specific autoformalization training times reported:**\n- StepFun-Formalizer-7B: 45.38 hours training time\n- StepFun-Formalizer-32B: 55.85 hours training time\n- Context length: 16,384 tokens\n\n### Theorem Proving / Proof Search\n\n- **ReProver**: Only ~1 GPU-week of training (very affordable)\n- **Goedel-Prover-V2**: Reduced compute budget vs. DeepSeek-Prover-V2-671B while outperforming it\n- **Lean 4 compilation/verification**: CPU-bound, does not require GPU. The Lean kernel itself runs on CPU.\n- **LLM inference for proof search**: 1 GPU sufficient for 7B-8B models; multiple GPUs for 32B+ models\n\n### Recommended Practical Setup\n\nFor a research project: 1-2 A100-80GB GPUs (or equivalent) would cover fine-tuning a 7B-32B autoformalization model and running proof search. A single RTX 4090 (24GB) is viable for 7B models with QLoRA.\n\n## 5. LEAN 4 THEOREM PROVERS (Proof Search Tools)\n\n### State of the Art (Ranked by MiniF2F Performance)\n\n| System | Size | MiniF2F (pass@N) | PutnamBench | Open Source |\n|--------|------|------------------|-------------|------------|\n| Goedel-Prover-V2-32B | 32B | 88.1% (pass@32), 90.4% w/ self-correction | 86/658 (pass@184) | Yes |\n| DeepSeek-Prover-V2 | 671B (37B active) | 88.9% (pass@N) | 49/658 (pass@1024) | Yes |\n| Goedel-Prover-V2-8B | 8B | 84.6% (pass@32) | -- | Yes |\n| Leanstral | 120B (6B active) | -- (FLTEval focused) | -- | Yes (Apache 2.0) |\n| AlphaProof (Google) | Undisclosed | IMO gold-level | -- | **No** |\n\n### Key Tools and Frameworks\n\n- **Goedel-Prover-V2** -- Current open-source SOTA. Uses scalable data synthesis, verifier-guided self-correction, model averaging. The 32B model beats 671B competitors.\n- **DeepSeek-Prover-V2** -- 671B MoE (37B active, 256 experts). Recursive theorem proving pipeline. Also available in a 7B variant (~76-78% on MiniF2F).\n- **LeanCopilot** -- In-editor LLM-based tactic suggestion, proof search, and premise selection for Lean 4. Supports local or cloud models. Actively maintained.\n- **ReProver (LeanDojo)** -- Retrieval-augmented prover. Only 1 GPU-week to train. LeanDojo-v2 released.\n- **LeanProgress** -- Guides proof search via progress prediction. Collected ~80K proof trajectories from Lean Workbook Plus and Mathlib4. Published in TMLR 2025.\n- **Leanstral** -- Agent-based approach that interacts with Lean LSP. Cost-efficient for proof generation.\n- **Gauss (Math Inc.)** -- Formalized the strong Prime Number Theorem in 3 weeks (vs. 18+ months of human expert effort). Likely proprietary.\n\n---\n\n## Summary Recommendations for Your Project\n\n1. **For autoformalization (NL to Lean 4):** Start with StepFun-Formalizer-7B/32B (open weights, Apache 2.0, well-documented training) or Leanstral (if using as an agent). The Safe framework's step-level formalization approach is the closest match to \"selective formal verification.\"\n\n2. **For proof block verification via LLM:** QwQ-32B or DeepSeek-R1 for reasoning; pair with Goedel-Prover-V2-8B/32B for formal proof search.\n\n3. **Primary codebase to build upon:** The **Safe** repository ([github.com/liuchengwucn/Safe](https://github.com/liuchengwucn/Safe)) is the most directly aligned with selective formal verification of mathematical proofs -- it already does step-aware formalization and verification in Lean 4.\n\n4. **Hardware:** A single A100-80GB or 2x RTX 4090 is sufficient for fine-tuning 7B-32B models and running proof search. ReProver needs only 1 GPU-week.\n\n5. **Lean 4 proof search:** Goedel-Prover-V2-32B is the clear open-source leader (88.1% MiniF2F, beats 671B models).\n\n---\n\nSources:\n- [Leanstral - Mistral's Open-Source Proof Agent](https://rits.shanghai.nyu.edu/ai/leanstral-mistrals-open-source-proof-agent-for-lean-4/)\n- [StepFun-Formalizer on HuggingFace](https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B)\n- [StepFun-Formalizer GitHub](https://github.com/stepfun-ai/StepFun-Formalizer)\n- [Safe: Step-aware Formal Verification (ACL 2025)](https://aclanthology.org/2025.acl-long.594/)\n- [Safe GitHub Repository](https://github.com/liuchengwucn/Safe)\n- [Goedel-Prover GitHub](https://github.com/Goedel-LM/Goedel-Prover)\n- [Goedel-Prover-V2 Overview](https://www.emergentmind.com/topics/goedel-prover-v2)\n- [DeepSeek-Prover-V2 Paper](https://arxiv.org/abs/2504.21801)\n- [LeanDojo / ReProver GitHub](https://github.com/lean-dojo/ReProver)\n- [LeanCopilot GitHub](https://github.com/lean-dojo/LeanCopilot)\n- [LeanDojo Documentation](https://leandojo.readthedocs.io/en/latest/index.html)\n- [Herald Translator GitHub](https://github.com/frenzymath/herald_translator)\n- [Herald Dataset Paper](https://arxiv.org/abs/2410.10878)\n- [ATLAS Autoformalization Paper](https://arxiv.org/pdf/2502.05567)\n- [Process-Driven Autoformalization (PDA) GitHub](https://github.com/rookie-joe/PDA)\n- [ProofBridge Paper](https://arxiv.org/abs/2510.15681)\n- [Multi-Agent Autoformalization GitHub](https://github.com/lanzhang128/multi_agent_autoformalization)\n- [LeanInteract GitHub](https://github.com/augustepoiroux/LeanInteract)\n- [LeanProgress](https://leandojo.org/leanprogress.html)\n- [NL2Lean (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1586.pdf)\n- [Lean 4 Survey Paper](https://arxiv.org/abs/2501.18639)\n- [Best Open Source LLM for Math 2026](https://www.siliconflow.com/articles/en/best-open-source-LLM-for-math)\n- [Top Open-Source Reasoning Models 2026](https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026)\n- [DL4TP Survey GitHub](https://github.com/zhaoyu-li/DL4TP)\n- [LeanAide GitHub](https://github.com/siddhartha-gadgil/LeanAide)\n- [LoRA/QLoRA Fine-Tuning Guide 2026](https://effloow.com/articles/llm-fine-tuning-lora-qlora-guide-2026)\n- [Leanstral on The Register](https://www.theregister.com/2026/03/17/mistral_leanstral_ai_code_verification_tool/)\n- [Major Breakthroughs in Lean 4 Auto-Formalized Mathematics](https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html)\n- [Lean Atlas Paper](https://arxiv.org/abs/2604.16347)\n- [LeanSearch v2](https://arxiv.org/html/2605.13137)\n- [FormaRL Paper](https://arxiv.org/abs/2508.18914)&lt;/result>\n&lt;usage>&lt;total_tokens>28873&lt;/total_tokens>&lt;tool_uses>23&lt;/tool_uses>&lt;duration_ms>161864&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Uncertainty-Guided Selec…",
  "leafUuid": "04ff1d63-17c6-4ce4-98ec-edf48f40f16f",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective proof block formalization",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Runtime record

_source line 32 · 2026-05-27T12:20:51.363Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T12:20:51.363Z",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

## Round 3

7 recorded events

### User

_source line 33 · 2026-05-27T12:20:51.371Z_

&lt;task-notification>
&lt;task-id>a8ad2fc8d499fe316&lt;/task-id>
&lt;tool-use-id>toolu_01UZgYuPVWuJECo9kN87MZ6T&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/a8ad2fc8d499fe316.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Find models and implementations" completed&lt;/summary>
&lt;result>I now have comprehensive findings across all five areas. Here is the full report.

---

# Research Landscape: Selective Formal Verification of Mathematical Proofs (May 2026)

## 1. TOP OPEN-SOURCE MODELS FOR AUTOFORMALIZATION (NL Math to Lean 4)

### Tier 1: Purpose-Built Autoformalization Models

- **Leanstral (Mistral AI, March 2026)** -- The first open-source AI agent built specifically for Lean 4. 120B total parameters, only 6B active per token (sparse MoE). Apache 2.0 license. On the FLTEval benchmark (Fermat's Last Theorem formalization), it scores 26.3 pass@2 at $36 cost, beating Claude Sonnet 4.6 (23.7 at $549). Integrates with Lean LSP via MCP. Weights available for self-deployment.
  - GitHub/API: Free endpoint `labs-leanstral-2603`

- **StepFun-Formalizer (StepFun AI)** -- Available in 7B and 32B variants, Apache 2.0. Specifically designed for NL-to-Lean-4 translation. StepFun-Formalizer-32B achieves SOTA BEq@1 scores of 40.5% on FormalMATH-Lite and 26.7% on ProverBench. Training takes ~56 hours for the 32B model. Weights on HuggingFace (`stepfun-ai/StepFun-Formalizer-32B`).
  - GitHub: [github.com/stepfun-ai/StepFun-Formalizer](https://github.com/stepfun-ai/StepFun-Formalizer)

- **Herald Translator** -- Fine-tuned on the Herald dataset (580K valid statements, 44K NL-FL theorem pairs from Mathlib4). Achieves 96.7% accuracy on miniF2F-test for statement formalization. Model size not explicitly documented.
  - GitHub: [github.com/frenzymath/herald_translator](https://github.com/frenzymath/herald_translator)

- **ATLAS Translator** -- Iterative data generation framework. Achieves 91.60% on miniF2F, 80.59% on ProofNet, 65.47% on MathQual (pass@8). At pass@128: 96.93%, 92.99%, 84.72% respectively.

### Tier 2: General Autoformalization Approaches

- **ProofBridge** -- Joint embedding model for translating entire NL theorems+proofs into Lean 4. Reported to outperform GPT-5 and Gemini-2.5 baselines.
- **NL2Lean** -- Uses curriculum learning + multi-reward model for NL-to-Lean-4 translation (EMNLP 2025).
- **MASA (Multi-Agent Autoformalization)** -- Multi-agent system with LLM, knowledge base, retriever, and theorem prover components.
  - GitHub: [github.com/lanzhang128/multi_agent_autoformalization](https://github.com/lanzhang128/multi_agent_autoformalization)
- **Process-Driven Autoformalization (PDA)** -- Uses Lean 4 compiler feedback to refine autoformalization iteratively. Published with the FORML4 dataset.
  - GitHub: [github.com/rookie-joe/PDA](https://github.com/rookie-joe/PDA)

## 2. TOP OPEN-SOURCE MODELS FOR MATHEMATICAL REASONING

### Best for LLM-Based Proof Block Verification

- **DeepSeek-R1** -- Elite-level reasoning, comparable to OpenAI o1. Strong chain-of-thought with extended reasoning traces. Best raw reasoning performance among open-source models.
- **Qwen/QwQ-32B** -- Best balance of capability and efficiency. Strong math reasoning in a 32B package.
- **Qwen 3 235B** -- Leads broadest range of benchmarks (Apache 2.0). Top-tier reasoning, coding, multilingual.
- **GLM-5 (THUDM)** -- Scores 94.2 HumanEval, 95.7 AIME 2025, 85.7 GPQA Diamond.
- **GLM-Z1-9B-0414** -- Surprisingly strong math in a lightweight 9B package, good for resource-constrained deployments.
- **DeepSeek V3.2/V4** -- Unified thinking-mode models that integrate reasoning into standard chat, better for production deployments.

**Recommendation for proof block verification:** DeepSeek-R1 or QwQ-32B for reasoning quality; GLM-Z1-9B for efficiency. For a selective verification pipeline, QwQ-32B offers the best quality-to-cost tradeoff.

## 3. EXISTING IMPLEMENTATIONS ON GITHUB

### Directly Relevant Codebases

- **Safe (ACL 2025 Main)** -- **Most directly relevant to your project.** Retrospective step-aware formal verification of LLM mathematical reasoning. Translates each reasoning step to Lean 4, then proves correctness. Includes the FormalStep dataset (30,809 formal statements). Authors: Chengwu Liu et al.
  - GitHub: [github.com/liuchengwucn/Safe](https://github.com/liuchengwucn/Safe)
  - Paper: [aclanthology.org/2025.acl-long.594](https://aclanthology.org/2025.acl-long.594/)

- **Goedel-Prover / Goedel-Prover-V2** -- Open-source ATP for Lean 4. V2-32B: 88.1% pass@32 on MiniF2F (90.4% with self-correction). Outperforms DeepSeek-Prover-V2-671B with 1/20th the parameters. The 8B variant hits 84.6% pass@32.
  - GitHub: [github.com/Goedel-LM/Goedel-Prover](https://github.com/Goedel-LM/Goedel-Prover)

- **LeanAide** -- AI tools for Lean 4 using autoformalization as core technique.
  - GitHub: [github.com/siddhartha-gadgil/LeanAide](https://github.com/siddhartha-gadgil/LeanAide)

- **LeanDojo / ReProver / LeanCopilot** -- Comprehensive ecosystem for AI-assisted theorem proving in Lean 4. ReProver is retrieval-augmented. LeanCopilot provides in-editor tactic suggestion, proof search, and premise selection. LeanDojo-v2 presented at NeurIPS 2025.
  - GitHub: [github.com/lean-dojo/LeanCopilot](https://github.com/lean-dojo/LeanCopilot)
  - GitHub: [github.com/lean-dojo/ReProver](https://github.com/lean-dojo/ReProver)
  - Docs: [leandojo.readthedocs.io](https://leandojo.readthedocs.io/en/latest/index.html)

- **LeanInteract** -- Python interface for Lean 4, useful for running autoformalization benchmarks (MiniF2F, ProofNet) programmatically.
  - GitHub: [github.com/augustepoiroux/LeanInteract](https://github.com/augustepoiroux/LeanInteract)

- **DL4TP** -- Comprehensive survey repo on deep learning for theorem proving (COLM 2024).
  - GitHub: [github.com/zhaoyu-li/DL4TP](https://github.com/zhaoyu-li/DL4TP)

### Datasets

- **FormalStep** (from Safe): 30,809 formal statements for step-correctness verification
- **FORML4** (from PDA): Autoformalization dataset built by informalizing Mathlib 4 theorems
- **Herald**: 580K statements, 44K NL-FL pairs from Mathlib4
- **Numina-ATF**: 750K synthetic formal statements for ATP research
- **StepFun-Formalizer-Training**: Training data on HuggingFace

## 4. HARDWARE / DATA REQUIREMENTS

### Fine-Tuning Autoformalization Models (LoRA/QLoRA)

| Model Size | Technique | VRAM Required | Hardware | Time Estimate |
|-----------|-----------|--------------|----------|--------------|
| 7B | QLoRA (4-bit) | ~8 GB | Single RTX 4070 Ti | Hours (afternoon) |
| 7B | LoRA | ~16 GB | Single RTX 4090 / A5000 | Hours |
| 32B | QLoRA (4-bit) | ~24 GB | Single RTX 4090 / A6000 | ~46-56 hours |
| 70B | QLoRA (4-bit) | ~46 GB | Single A100-80GB | Days |

**Specific autoformalization training times reported:**
- StepFun-Formalizer-7B: 45.38 hours training time
- StepFun-Formalizer-32B: 55.85 hours training time
- Context length: 16,384 tokens

### Theorem Proving / Proof Search

- **ReProver**: Only ~1 GPU-week of training (very affordable)
- **Goedel-Prover-V2**: Reduced compute budget vs. DeepSeek-Prover-V2-671B while outperforming it
- **Lean 4 compilation/verification**: CPU-bound, does not require GPU. The Lean kernel itself runs on CPU.
- **LLM inference for proof search**: 1 GPU sufficient for 7B-8B models; multiple GPUs for 32B+ models

### Recommended Practical Setup

For a research project: 1-2 A100-80GB GPUs (or equivalent) would cover fine-tuning a 7B-32B autoformalization model and running proof search. A single RTX 4090 (24GB) is viable for 7B models with QLoRA.

## 5. LEAN 4 THEOREM PROVERS (Proof Search Tools)

### State of the Art (Ranked by MiniF2F Performance)

| System | Size | MiniF2F (pass@N) | PutnamBench | Open Source |
|--------|------|------------------|-------------|------------|
| Goedel-Prover-V2-32B | 32B | 88.1% (pass@32), 90.4% w/ self-correction | 86/658 (pass@184) | Yes |
| DeepSeek-Prover-V2 | 671B (37B active) | 88.9% (pass@N) | 49/658 (pass@1024) | Yes |
| Goedel-Prover-V2-8B | 8B | 84.6% (pass@32) | -- | Yes |
| Leanstral | 120B (6B active) | -- (FLTEval focused) | -- | Yes (Apache 2.0) |
| AlphaProof (Google) | Undisclosed | IMO gold-level | -- | **No** |

### Key Tools and Frameworks

- **Goedel-Prover-V2** -- Current open-source SOTA. Uses scalable data synthesis, verifier-guided self-correction, model averaging. The 32B model beats 671B competitors.
- **DeepSeek-Prover-V2** -- 671B MoE (37B active, 256 experts). Recursive theorem proving pipeline. Also available in a 7B variant (~76-78% on MiniF2F).
- **LeanCopilot** -- In-editor LLM-based tactic suggestion, proof search, and premise selection for Lean 4. Supports local or cloud models. Actively maintained.
- **ReProver (LeanDojo)** -- Retrieval-augmented prover. Only 1 GPU-week to train. LeanDojo-v2 released.
- **LeanProgress** -- Guides proof search via progress prediction. Collected ~80K proof trajectories from Lean Workbook Plus and Mathlib4. Published in TMLR 2025.
- **Leanstral** -- Agent-based approach that interacts with Lean LSP. Cost-efficient for proof generation.
- **Gauss (Math Inc.)** -- Formalized the strong Prime Number Theorem in 3 weeks (vs. 18+ months of human expert effort). Likely proprietary.

---

## Summary Recommendations for Your Project

1. **For autoformalization (NL to Lean 4):** Start with StepFun-Formalizer-7B/32B (open weights, Apache 2.0, well-documented training) or Leanstral (if using as an agent). The Safe framework's step-level formalization approach is the closest match to "selective formal verification."

2. **For proof block verification via LLM:** QwQ-32B or DeepSeek-R1 for reasoning; pair with Goedel-Prover-V2-8B/32B for formal proof search.

3. **Primary codebase to build upon:** The **Safe** repository ([github.com/liuchengwucn/Safe](https://github.com/liuchengwucn/Safe)) is the most directly aligned with selective formal verification of mathematical proofs -- it already does step-aware formalization and verification in Lean 4.

4. **Hardware:** A single A100-80GB or 2x RTX 4090 is sufficient for fine-tuning 7B-32B models and running proof search. ReProver needs only 1 GPU-week.

5. **Lean 4 proof search:** Goedel-Prover-V2-32B is the clear open-source leader (88.1% MiniF2F, beats 671B models).

---

Sources:
- [Leanstral - Mistral's Open-Source Proof Agent](https://rits.shanghai.nyu.edu/ai/leanstral-mistrals-open-source-proof-agent-for-lean-4/)
- [StepFun-Formalizer on HuggingFace](https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B)
- [StepFun-Formalizer GitHub](https://github.com/stepfun-ai/StepFun-Formalizer)
- [Safe: Step-aware Formal Verification (ACL 2025)](https://aclanthology.org/2025.acl-long.594/)
- [Safe GitHub Repository](https://github.com/liuchengwucn/Safe)
- [Goedel-Prover GitHub](https://github.com/Goedel-LM/Goedel-Prover)
- [Goedel-Prover-V2 Overview](https://www.emergentmind.com/topics/goedel-prover-v2)
- [DeepSeek-Prover-V2 Paper](https://arxiv.org/abs/2504.21801)
- [LeanDojo / ReProver GitHub](https://github.com/lean-dojo/ReProver)
- [LeanCopilot GitHub](https://github.com/lean-dojo/LeanCopilot)
- [LeanDojo Documentation](https://leandojo.readthedocs.io/en/latest/index.html)
- [Herald Translator GitHub](https://github.com/frenzymath/herald_translator)
- [Herald Dataset Paper](https://arxiv.org/abs/2410.10878)
- [ATLAS Autoformalization Paper](https://arxiv.org/pdf/2502.05567)
- [Process-Driven Autoformalization (PDA) GitHub](https://github.com/rookie-joe/PDA)
- [ProofBridge Paper](https://arxiv.org/abs/2510.15681)
- [Multi-Agent Autoformalization GitHub](https://github.com/lanzhang128/multi_agent_autoformalization)
- [LeanInteract GitHub](https://github.com/augustepoiroux/LeanInteract)
- [LeanProgress](https://leandojo.org/leanprogress.html)
- [NL2Lean (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1586.pdf)
- [Lean 4 Survey Paper](https://arxiv.org/abs/2501.18639)
- [Best Open Source LLM for Math 2026](https://www.siliconflow.com/articles/en/best-open-source-LLM-for-math)
- [Top Open-Source Reasoning Models 2026](https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026)
- [DL4TP Survey GitHub](https://github.com/zhaoyu-li/DL4TP)
- [LeanAide GitHub](https://github.com/siddhartha-gadgil/LeanAide)
- [LoRA/QLoRA Fine-Tuning Guide 2026](https://effloow.com/articles/llm-fine-tuning-lora-qlora-guide-2026)
- [Leanstral on The Register](https://www.theregister.com/2026/03/17/mistral_leanstral_ai_code_verification_tool/)
- [Major Breakthroughs in Lean 4 Auto-Formalized Mathematics](https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html)
- [Lean Atlas Paper](https://arxiv.org/abs/2604.16347)
- [LeanSearch v2](https://arxiv.org/html/2605.13137)
- [FormaRL Paper](https://arxiv.org/abs/2508.18914)&lt;/result>
&lt;usage>&lt;total_tokens>28873&lt;/total_tokens>&lt;tool_uses>23&lt;/tool_uses>&lt;duration_ms>161864&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04ff1d63-17c6-4ce4-98ec-edf48f40f16f",
  "isSidechain": false,
  "promptId": "6c3f38f9-fafd-47f3-9f71-5e57d73fa4b4",
  "type": "user",
  "uuid": "b675791a-0d8a-4d26-b796-013ce29bf77a",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-27T12:21:02.203Z_

<details><summary>Logged reasoning block</summary>

```text
The models/implementations agent has completed with very detailed findings. Key takeaways:

**Autoformalization models:**
- Leanstral (Mistral, March 2026) - 120B MoE, 6B active, Apache 2.0
- StepFun-Formalizer-32B - 40.5% BEq@1 on FormalMATH-Lite
- Herald Translator - 96.7% on miniF2F-test statement formalization

**Math reasoning models:**
- DeepSeek-R1, QwQ-32B, Qwen 3 235B


- Goedel-Prover-V2-32B achieves 88.1% pass@32 on MiniF2F as the leading open-source option, while DeepSeek-Prover-V2 reaches 88.9% pass@N

For implementation, the most relevant codebases are Safe, Goedel-Prover, and the LeanDojo/ReProver/LeanCopilot ecosystem. On the hardware side, running a 32B QLoRA setup requires around 24GB VRAM.

Training timelines vary significantly—the full pipeline takes roughly 56 hours, while ReProver alone needs about a GPU-week. An A100-80GB or dual RTX 4090 setup would be sufficient for this work. I'm still waiting on the concurrent work from the search and reference verification agents.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b675791a-0d8a-4d26-b796-013ce29bf77a",
  "isSidechain": false,
  "requestId": "req_011CbT4eYdVVba84SAMfLtc8",
  "type": "assistant",
  "uuid": "d3346c44-a9d1-46e0-a4a9-98afa188e0d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ty921oPBDTywYqhYkhb1W",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5050,
      "cache_read_input_tokens": 20702,
      "output_tokens": 543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5050,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 543,
          "cache_read_input_tokens": 20702,
          "cache_creation_input_tokens": 5050,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5050
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

_source line 35 · 2026-05-27T12:21:02.363Z_

Models/implementations agent completed with excellent findings. Key highlights:
- **Autoformalization SOTA**: StepFun-Formalizer-32B (40.5% BEq@1), Leanstral (120B MoE), Herald Translator (96.7% miniF2F)
- **Lean 4 prover SOTA**: Goedel-Prover-V2-32B (88.1% MiniF2F pass@32)
- **Safe codebase** available at github.com/liuchengwucn/Safe
- Hardware: A100-80GB sufficient for 32B fine-tuning

Still waiting on concurrent work search and reference verification agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3346c44-a9d1-46e0-a4a9-98afa188e0d1",
  "isSidechain": false,
  "requestId": "req_011CbT4eYdVVba84SAMfLtc8",
  "type": "assistant",
  "uuid": "d2bf4b1b-743d-4ed0-a69b-9b15992c1905",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ty921oPBDTywYqhYkhb1W",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5050,
      "cache_read_input_tokens": 20702,
      "output_tokens": 543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5050,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 543,
          "cache_read_input_tokens": 20702,
          "cache_creation_input_tokens": 5050,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5050
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

_source line 36 · 2026-05-27T12:21:17.701Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T12:21:17.701Z",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "content": "&lt;task-notification>\n&lt;task-id>aefc7761e04a79fe8&lt;/task-id>\n&lt;tool-use-id>toolu_01US71XcUTtVTniJ93XX1yzB&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/aefc7761e04a79fe8.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Search concurrent work 2026\" completed&lt;/summary>\n&lt;result>I now have comprehensive results. Here is the full report.\n\n---\n\n## Novelty Search Report: \"Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition\"\n\n### CRITICAL FINDING: Highly Similar Prior Work Exists\n\n---\n\n### Search 1: \"selective formal verification uncertainty 2026\"\n\n**Key results:**\n- **\"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks\"** -- NeurIPS 2025. Introduces a PCFG framework for uncertainty quantification in LLM-generated formal artifacts, enabling **selective verification** that reduces errors 14-100% with minimal abstention. Uses uncertainty signals (grammar entropy, AUROC &gt; 0.93) to decide when to trust LLM outputs. **HIGHLY RELEVANT** -- addresses the \"uncertainty-guided selective verification\" component directly.\n- ICML 2026 Workshop on \"Statistical Frameworks for Uncertainty in Agentic Systems\"\n- TransferLab article on \"Formal Verification under Uncertainty\"\n\n**Similarity:** The \"Grammars of Formal Uncertainty\" paper is **moderately-to-highly similar** in its use of uncertainty signals to enable selective verification of LLM-generated formal artifacts.\n\n---\n\n### Search 2: \"pseudo-formal autoformalization 2026\"\n\n**Key results:**\n- **\"Pseudo-Formalization for Automatic Proof Verification\" (arXiv:2605.20531, May 2026)** -- Authors: **Slim Barkallah, Luke Bailey, Kaiyue Wen, Mohammed Abouzaid, Tengyu Ma**. This paper is **EXTREMELY SIMILAR** to the proposed idea. It proposes:\n  - **Pseudo-Formal (PF) proof format**: decomposes proofs into self-contained modular blocks, each with explicit premises, conclusions, and proof in natural language\n  - **Block Verification (BV)**: an LLM verifies each module independently\n  - Evaluated on Olympiad and research-level math benchmarks\n  - Pareto-dominates LLM-as-judge baselines\n  - Releases ArxivMathGradingBench (35 research papers, 40 known errors)\n\n- **\"130k Lines of Formal Topology in Two Weeks\" (arXiv:2601.03298, Jan 2026)** -- Demonstrates cheap, large-scale autoformalization using LLM + proof checker feedback loops.\n\n- **\"Towards a Common Framework for Autoformalization\" (AAAI 2025)** -- Proposes unified framework for autoformalization across research fields.\n\n**Similarity:** The Barkallah et al. paper is **EXTREMELY SIMILAR** -- it implements the core \"pseudo-formal decomposition\" concept with modular NL proof blocks having explicit premises/conclusions. The key difference is that their paper does NOT include the uncertainty-guided routing to formal verification (Lean 4); instead, all blocks are verified by LLM-based Block Verification only.\n\n---\n\n### Search 3: \"adaptive verification mathematical proof 2026\"\n\n**Key results:**\n- **ADAPT (Adaptive Proof Refinement with LLM-Guided Strategy Selection)** -- Uses an LLM decision-maker to dynamically select refinement strategies for incorrect proofs. Proves 16-18% more theorems than baselines.\n- **MiniF2F-Dafny (POPL 2026)** -- First translation of miniF2F to Dafny; auto-verifies 40-44% of test sets.\n- **StepProof** -- Step-by-step autoformalisation for sentence-level verification of NL proofs.\n\n**Similarity:** ADAPT is tangentially related (adaptive strategy selection, not uncertainty-guided routing). StepProof is moderately relevant (step-level NL proof verification via autoformalization).\n\n---\n\n### Search 4: \"uncertainty guided proof verification\"\n\n**Key results:**\n- **\"Uncertainty-Aware Step-wise Verification with Generative Reward Models\" (arXiv:2502.11250, Feb 2025)** -- Introduces CoT Entropy to quantify process reward model uncertainty in step-wise verification. Improves robustness of LLM-based judge models. **RELEVANT** -- uses uncertainty to improve proof step verification reliability.\n- **\"A Protocol for Trustless Verification Under Uncertainty\" (arXiv:2507.00631)**\n\n**Similarity:** The CoT Entropy paper is **moderately similar** -- it uses uncertainty quantification for step-level verification, but does not involve routing to formal provers.\n\n---\n\n### Search 5: \"selective autoformalization natural language proof 2026\"\n\n**Key results:**\n- **FormalEvolve (arXiv:2603.19828, March 2026)** -- Neuro-symbolic evolutionary search for autoformalization of NL math to compilable formal statements.\n- **AI for Math Workshop at ICML 2026** -- Challenge track for generating Lean 4 proofs from NL informal proofs (May-June 2026).\n- **ProofBridge (arXiv:2510.15681)** -- Unified framework for translating entire NL theorems and proofs into Lean 4 via joint embeddings.\n- **Autoformalization robustness evaluations (arXiv:2511.12784)** -- Evaluating LLM robustness in autoformalization via paraphrasing.\n\n**Similarity:** These are relevant as components (autoformalization pipelines) but none implement selective/uncertainty-guided routing between LLM verification and formal verification.\n\n---\n\n### Search 6: arXiv \"autoformalization selective verification 2026\"\n\n**Key results:**\n- **\"Faithful Autoformalization via Roundtrip Verification and Repair\" (arXiv:2604.25031, April 2026)** -- Roundtrip verification: formalize, back-translate, re-formalize, check logical equivalence. Raises formal equivalence from 45-61% to 83-85%. **RELEVANT** -- addresses verification quality in autoformalization but not selective routing.\n- **MerLean (arXiv:2602.16554, Feb 2026)** -- Agentic autoformalization for quantum computation; reduces verification burden to only new definitions/axioms.\n\n**Similarity:** MerLean's idea of \"reducing the verification burden\" to a subset is conceptually related to selective verification, though the mechanism is different.\n\n---\n\n### Search 7: arXiv \"proof verification uncertainty routing 2026\"\n\n**Key results:**\n- **UCCI (arXiv:2605.18796, May 2026)** -- Calibrated uncertainty for cost-optimal LLM cascade routing. Uses isotonic regression to map uncertainty to error probability, then selects escalation threshold via cost minimization. **RELEVANT** -- the general framework of uncertainty-based routing between verification tiers is conceptually very close to the proposed idea, though applied to LLM cascades rather than proof verification.\n- **CP-Router (arXiv:2505.19970)** -- Routes prompts between LLM and LRM based on complexity.\n\n**Similarity:** UCCI provides a direct methodological precedent for uncertainty-based routing between verification approaches.\n\n---\n\n### Search 8: OpenReview \"selective formal verification\"\n\n**Key results:**\n- **FVEL** -- Interactive formal verification environment with LLMs via theorem proving.\n- **AlphaVerus** -- Self-improving framework for formally verified code generation.\n- **VeriBench** -- Lean 4 benchmark for LLM-powered agents translating Python to proved implementations.\n\n**Similarity:** These are infrastructure/benchmark papers, not directly competing with the proposed idea.\n\n---\n\n### Search 9: OpenReview \"pseudo-formal verification\"\n\n**Key results:**\n- **StepProof (OpenReview:EXaKfdsw04)** -- Step-by-step verification of NL mathematical proofs via autoformalization. Breaks proofs into subproofs for sentence-level verification.\n- **Re:Form** -- Reducing human priors in scalable formal software verification with RL in LLMs.\n\n**Similarity:** StepProof is **moderately similar** in its decomposition approach, but uses full formalization for each step rather than selective routing.\n\n---\n\n### Search 10: \"Barkallah pseudo-formalization 2026\"\n\n**Key results:**\n- Confirmed: **Slim Barkallah** is the first author of the \"Pseudo-Formalization for Automatic Proof Verification\" paper (arXiv:2605.20531). A different Barkallah (Manel) presented at FMTea 2026 on formal methods teaching -- unrelated.\n\n**Similarity:** The Slim Barkallah paper is the **most critical competing work** found.\n\n---\n\n### Search 11: \"Safe Liu ACL 2025 formal verification lean\"\n\n**Key results:**\n- **Safe (ACL 2025 Main)** -- Authors: Chengwu Liu, Ye Yuan, Yichun Yin, et al. Retrospective step-aware formal verification: articulates mathematical claims in Lean 4 at each reasoning step and provides formal proofs. First work to use Lean 4 for verifying LLM-generated content. Proposes FormalStep benchmark (30,809 formal statements). **RELEVANT** -- demonstrates step-level formal verification of LLM reasoning, but applies it uniformly rather than selectively.\n\n**Similarity:** Safe is **moderately similar** -- it formalizes each step into Lean 4 for verification but does not do selective routing based on uncertainty.\n\n---\n\n### Search 12: \"Mu adaptive verification allocation 2026\"\n\n**Key results:** No relevant academic results. The search returned Mumbai University admission results.\n\n**Similarity:** No competing work found under this query.\n\n---\n\n### Search 13: \"Bhatt uncertainty guided selective verification 2025\"\n\n**Key results:**\n- Redirected to \"Grammars of Formal Uncertainty\" (already covered in Search 1). No specific paper by \"Bhatt\" found.\n- **\"Uncertainty-Guided Selective Adaptation\" (arXiv:2511.12006)** -- About fluorescence microscopy, not proof verification.\n\n**Similarity:** No specific \"Bhatt\" paper on this topic found.\n\n---\n\n### Additional Highly Relevant Papers Found in Follow-up Searches\n\n- **VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv:2601.20055, Jan 2026)** -- Decomposes LLM outputs into atomic claims, autoformalizes to FOL, verifies via SMT solvers. Features **\"Semantic Routing\"**: dynamically classifies atomic claims -- verifiable logic goes to SMT solvers (Z3), ambiguous claims go to a consensus-based \"soft verifier.\" **HIGHLY RELEVANT** -- implements a form of routing between formal and informal verification, though for general reasoning rather than mathematical proofs specifically.\n\n- **HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (arXiv:2511.18760, ICML 2026 poster)** -- First tool-assisted agent that **explicitly interleaves informal reasoning with formally verified proof steps in Lean**. Comprises LLM + translator + Lean prover + feedback module. 67% accuracy improvement on AIME'25 with 80% fewer FLOPs. **HIGHLY RELEVANT** -- bridges informal and formal verification within the same pipeline.\n\n- **ProofSketcher: Hybrid LLM + Lightweight Proof Checker (arXiv:2604.06401, April 2026)** -- LLM produces typed proof sketch with explicit step tags and typed holes; a trusted kernel expands sketches into proof obligations. Returns localized failure feedback. **MODERATELY RELEVANT** -- hybrid verification approach but without uncertainty-guided routing.\n\n- **Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads (arXiv:2511.06209)** -- Trains lightweight UHeads (&lt;10M params) on frozen LLM internal states to estimate uncertainty of reasoning steps. Matches/surpasses PRMs 810x larger. **RELEVANT** -- provides the uncertainty estimation component that could be used for routing.\n\n- **ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (arXiv:2510.15981)** -- Constructs DAG of logical dependencies between proof steps, formalizes each as intermediate lemma. New SOTA for autoformalization (ProofScore 0.545 vs 0.123 baseline). **MODERATELY RELEVANT** -- modular/structured autoformalization.\n\n---\n\n### Summary Assessment\n\n| Aspect of Proposed Idea | Prior Work Coverage | Key Papers |\n|---|---|---|\n| Pseudo-formal decomposition (modular NL blocks with premises/conclusions) | **DIRECTLY COVERED** | Barkallah et al. 2605.20531 |\n| Block-level LLM verification of decomposed proof modules | **DIRECTLY COVERED** | Barkallah et al. 2605.20531 |\n| Uncertainty-guided routing/selection | **COVERED in adjacent domains** | Grammars of Formal Uncertainty (NeurIPS'25), UCCI, Reasoning with Confidence |\n| Routing uncertain blocks to formal verification (Lean 4) | **PARTIALLY COVERED** | VERGE (semantic routing), HERMES (interleaved formal/informal) |\n| Combined system: pseudo-formal decomposition + uncertainty routing to Lean 4 | **NOT DIRECTLY COVERED as a single system** | -- |\n\n### Verdict\n\nThe **most critical competing paper** is **Barkallah et al. \"Pseudo-Formalization for Automatic Proof Verification\" (arXiv:2605.20531, May 2026)**, which implements the core pseudo-formal decomposition with modular NL proof blocks having explicit premises/conclusions, verified by LLM-based Block Verification. This paper was posted very recently (May 2026) and directly overlaps with the \"pseudo-formal decomposition\" component of the proposed idea.\n\nThe specific **novelty gap** that the proposed idea could still claim is the **uncertainty-guided selective routing to formal verification (Lean 4)**. Barkallah et al. verify all blocks with LLMs only; the proposed idea would route uncertain blocks to Lean 4 while keeping confident blocks with LLM verification. However, the individual components (uncertainty estimation for verification, routing between formal/informal, and the pseudo-formal decomposition itself) all have strong prior art. The integration of these specific components into a single pipeline is where novelty would need to be argued.\n\nAdditionally, **VERGE** (Jan 2026) already implements a form of semantic routing between formal (SMT) and informal (consensus) verification, and **HERMES** (ICML 2026) interleaves informal reasoning with Lean 4 formal verification steps.\n\n---\n\n### Sources\n\n- [Pseudo-Formalization for Automatic Proof Verification (Barkallah et al.)](https://arxiv.org/abs/2605.20531)\n- [Grammars of Formal Uncertainty (NeurIPS 2025)](https://arxiv.org/abs/2505.20047)\n- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)\n- [HERMES: Efficient and Verifiable Mathematical Reasoning (ICML 2026)](https://arxiv.org/abs/2511.18760)\n- [Safe: Step-aware Formal Verification (ACL 2025)](https://arxiv.org/abs/2506.04592)\n- [Reasoning with Confidence: Uncertainty Heads](https://arxiv.org/abs/2511.06209)\n- [UCCI: Calibrated Uncertainty for LLM Cascade Routing](https://arxiv.org/abs/2605.18796)\n- [ProofSketcher: Hybrid LLM + Lightweight Proof Checker](https://arxiv.org/abs/2604.06401)\n- [StepProof: Step-by-step Verification](https://arxiv.org/abs/2506.10558)\n- [ProofFlow: Dependency Graph Autoformalization](https://arxiv.org/abs/2510.15981)\n- [ProofBridge: Auto-Formalization in Lean via Joint Embeddings](https://arxiv.org/abs/2510.15681)\n- [FormalEvolve: Neuro-Symbolic Evolutionary Autoformalization](https://arxiv.org/abs/2603.19828)\n- [Faithful Autoformalization via Roundtrip Verification](https://arxiv.org/abs/2604.25031)\n- [130k Lines of Formal Topology](https://arxiv.org/abs/2601.03298)\n- [Uncertainty-Aware Step-wise Verification (CoT Entropy)](https://arxiv.org/abs/2502.11250)\n- [ADAPT: Adaptive Proof Refinement](https://arxiv.org/abs/2510.25103)\n- [ICML 2026 Workshop: Statistical Frameworks for Uncertainty in Agentic Systems](https://agentic-uncertainty-icml2026.github.io/)\n- [AI for Math Workshop at ICML 2026](https://ai4math2026.github.io/)\n- [OpenReview: Grammars of Formal Uncertainty](https://openreview.net/forum?id=QfKpJ00t2L)&lt;/result>\n&lt;usage>&lt;total_tokens>31868&lt;/total_tokens>&lt;tool_uses>29&lt;/tool_uses>&lt;duration_ms>205070&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Uncertainty-Guided Selec…",
  "leafUuid": "d2bf4b1b-743d-4ed0-a69b-9b15992c1905",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective proof block formalization",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Runtime record

_source line 39 · 2026-05-27T12:21:17.751Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T12:21:17.751Z",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

## Round 4

5 recorded events

### User

_source line 40 · 2026-05-27T12:21:17.757Z_

&lt;task-notification>
&lt;task-id>aefc7761e04a79fe8&lt;/task-id>
&lt;tool-use-id>toolu_01US71XcUTtVTniJ93XX1yzB&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/aefc7761e04a79fe8.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Search concurrent work 2026" completed&lt;/summary>
&lt;result>I now have comprehensive results. Here is the full report.

---

## Novelty Search Report: "Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition"

### CRITICAL FINDING: Highly Similar Prior Work Exists

---

### Search 1: "selective formal verification uncertainty 2026"

**Key results:**
- **"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks"** -- NeurIPS 2025. Introduces a PCFG framework for uncertainty quantification in LLM-generated formal artifacts, enabling **selective verification** that reduces errors 14-100% with minimal abstention. Uses uncertainty signals (grammar entropy, AUROC &gt; 0.93) to decide when to trust LLM outputs. **HIGHLY RELEVANT** -- addresses the "uncertainty-guided selective verification" component directly.
- ICML 2026 Workshop on "Statistical Frameworks for Uncertainty in Agentic Systems"
- TransferLab article on "Formal Verification under Uncertainty"

**Similarity:** The "Grammars of Formal Uncertainty" paper is **moderately-to-highly similar** in its use of uncertainty signals to enable selective verification of LLM-generated formal artifacts.

---

### Search 2: "pseudo-formal autoformalization 2026"

**Key results:**
- **"Pseudo-Formalization for Automatic Proof Verification" (arXiv:2605.20531, May 2026)** -- Authors: **Slim Barkallah, Luke Bailey, Kaiyue Wen, Mohammed Abouzaid, Tengyu Ma**. This paper is **EXTREMELY SIMILAR** to the proposed idea. It proposes:
  - **Pseudo-Formal (PF) proof format**: decomposes proofs into self-contained modular blocks, each with explicit premises, conclusions, and proof in natural language
  - **Block Verification (BV)**: an LLM verifies each module independently
  - Evaluated on Olympiad and research-level math benchmarks
  - Pareto-dominates LLM-as-judge baselines
  - Releases ArxivMathGradingBench (35 research papers, 40 known errors)

- **"130k Lines of Formal Topology in Two Weeks" (arXiv:2601.03298, Jan 2026)** -- Demonstrates cheap, large-scale autoformalization using LLM + proof checker feedback loops.

- **"Towards a Common Framework for Autoformalization" (AAAI 2025)** -- Proposes unified framework for autoformalization across research fields.

**Similarity:** The Barkallah et al. paper is **EXTREMELY SIMILAR** -- it implements the core "pseudo-formal decomposition" concept with modular NL proof blocks having explicit premises/conclusions. The key difference is that their paper does NOT include the uncertainty-guided routing to formal verification (Lean 4); instead, all blocks are verified by LLM-based Block Verification only.

---

### Search 3: "adaptive verification mathematical proof 2026"

**Key results:**
- **ADAPT (Adaptive Proof Refinement with LLM-Guided Strategy Selection)** -- Uses an LLM decision-maker to dynamically select refinement strategies for incorrect proofs. Proves 16-18% more theorems than baselines.
- **MiniF2F-Dafny (POPL 2026)** -- First translation of miniF2F to Dafny; auto-verifies 40-44% of test sets.
- **StepProof** -- Step-by-step autoformalisation for sentence-level verification of NL proofs.

**Similarity:** ADAPT is tangentially related (adaptive strategy selection, not uncertainty-guided routing). StepProof is moderately relevant (step-level NL proof verification via autoformalization).

---

### Search 4: "uncertainty guided proof verification"

**Key results:**
- **"Uncertainty-Aware Step-wise Verification with Generative Reward Models" (arXiv:2502.11250, Feb 2025)** -- Introduces CoT Entropy to quantify process reward model uncertainty in step-wise verification. Improves robustness of LLM-based judge models. **RELEVANT** -- uses uncertainty to improve proof step verification reliability.
- **"A Protocol for Trustless Verification Under Uncertainty" (arXiv:2507.00631)**

**Similarity:** The CoT Entropy paper is **moderately similar** -- it uses uncertainty quantification for step-level verification, but does not involve routing to formal provers.

---

### Search 5: "selective autoformalization natural language proof 2026"

**Key results:**
- **FormalEvolve (arXiv:2603.19828, March 2026)** -- Neuro-symbolic evolutionary search for autoformalization of NL math to compilable formal statements.
- **AI for Math Workshop at ICML 2026** -- Challenge track for generating Lean 4 proofs from NL informal proofs (May-June 2026).
- **ProofBridge (arXiv:2510.15681)** -- Unified framework for translating entire NL theorems and proofs into Lean 4 via joint embeddings.
- **Autoformalization robustness evaluations (arXiv:2511.12784)** -- Evaluating LLM robustness in autoformalization via paraphrasing.

**Similarity:** These are relevant as components (autoformalization pipelines) but none implement selective/uncertainty-guided routing between LLM verification and formal verification.

---

### Search 6: arXiv "autoformalization selective verification 2026"

**Key results:**
- **"Faithful Autoformalization via Roundtrip Verification and Repair" (arXiv:2604.25031, April 2026)** -- Roundtrip verification: formalize, back-translate, re-formalize, check logical equivalence. Raises formal equivalence from 45-61% to 83-85%. **RELEVANT** -- addresses verification quality in autoformalization but not selective routing.
- **MerLean (arXiv:2602.16554, Feb 2026)** -- Agentic autoformalization for quantum computation; reduces verification burden to only new definitions/axioms.

**Similarity:** MerLean's idea of "reducing the verification burden" to a subset is conceptually related to selective verification, though the mechanism is different.

---

### Search 7: arXiv "proof verification uncertainty routing 2026"

**Key results:**
- **UCCI (arXiv:2605.18796, May 2026)** -- Calibrated uncertainty for cost-optimal LLM cascade routing. Uses isotonic regression to map uncertainty to error probability, then selects escalation threshold via cost minimization. **RELEVANT** -- the general framework of uncertainty-based routing between verification tiers is conceptually very close to the proposed idea, though applied to LLM cascades rather than proof verification.
- **CP-Router (arXiv:2505.19970)** -- Routes prompts between LLM and LRM based on complexity.

**Similarity:** UCCI provides a direct methodological precedent for uncertainty-based routing between verification approaches.

---

### Search 8: OpenReview "selective formal verification"

**Key results:**
- **FVEL** -- Interactive formal verification environment with LLMs via theorem proving.
- **AlphaVerus** -- Self-improving framework for formally verified code generation.
- **VeriBench** -- Lean 4 benchmark for LLM-powered agents translating Python to proved implementations.

**Similarity:** These are infrastructure/benchmark papers, not directly competing with the proposed idea.

---

### Search 9: OpenReview "pseudo-formal verification"

**Key results:**
- **StepProof (OpenReview:EXaKfdsw04)** -- Step-by-step verification of NL mathematical proofs via autoformalization. Breaks proofs into subproofs for sentence-level verification.
- **Re:Form** -- Reducing human priors in scalable formal software verification with RL in LLMs.

**Similarity:** StepProof is **moderately similar** in its decomposition approach, but uses full formalization for each step rather than selective routing.

---

### Search 10: "Barkallah pseudo-formalization 2026"

**Key results:**
- Confirmed: **Slim Barkallah** is the first author of the "Pseudo-Formalization for Automatic Proof Verification" paper (arXiv:2605.20531). A different Barkallah (Manel) presented at FMTea 2026 on formal methods teaching -- unrelated.

**Similarity:** The Slim Barkallah paper is the **most critical competing work** found.

---

### Search 11: "Safe Liu ACL 2025 formal verification lean"

**Key results:**
- **Safe (ACL 2025 Main)** -- Authors: Chengwu Liu, Ye Yuan, Yichun Yin, et al. Retrospective step-aware formal verification: articulates mathematical claims in Lean 4 at each reasoning step and provides formal proofs. First work to use Lean 4 for verifying LLM-generated content. Proposes FormalStep benchmark (30,809 formal statements). **RELEVANT** -- demonstrates step-level formal verification of LLM reasoning, but applies it uniformly rather than selectively.

**Similarity:** Safe is **moderately similar** -- it formalizes each step into Lean 4 for verification but does not do selective routing based on uncertainty.

---

### Search 12: "Mu adaptive verification allocation 2026"

**Key results:** No relevant academic results. The search returned Mumbai University admission results.

**Similarity:** No competing work found under this query.

---

### Search 13: "Bhatt uncertainty guided selective verification 2025"

**Key results:**
- Redirected to "Grammars of Formal Uncertainty" (already covered in Search 1). No specific paper by "Bhatt" found.
- **"Uncertainty-Guided Selective Adaptation" (arXiv:2511.12006)** -- About fluorescence microscopy, not proof verification.

**Similarity:** No specific "Bhatt" paper on this topic found.

---

### Additional Highly Relevant Papers Found in Follow-up Searches

- **VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv:2601.20055, Jan 2026)** -- Decomposes LLM outputs into atomic claims, autoformalizes to FOL, verifies via SMT solvers. Features **"Semantic Routing"**: dynamically classifies atomic claims -- verifiable logic goes to SMT solvers (Z3), ambiguous claims go to a consensus-based "soft verifier." **HIGHLY RELEVANT** -- implements a form of routing between formal and informal verification, though for general reasoning rather than mathematical proofs specifically.

- **HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (arXiv:2511.18760, ICML 2026 poster)** -- First tool-assisted agent that **explicitly interleaves informal reasoning with formally verified proof steps in Lean**. Comprises LLM + translator + Lean prover + feedback module. 67% accuracy improvement on AIME'25 with 80% fewer FLOPs. **HIGHLY RELEVANT** -- bridges informal and formal verification within the same pipeline.

- **ProofSketcher: Hybrid LLM + Lightweight Proof Checker (arXiv:2604.06401, April 2026)** -- LLM produces typed proof sketch with explicit step tags and typed holes; a trusted kernel expands sketches into proof obligations. Returns localized failure feedback. **MODERATELY RELEVANT** -- hybrid verification approach but without uncertainty-guided routing.

- **Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads (arXiv:2511.06209)** -- Trains lightweight UHeads (&lt;10M params) on frozen LLM internal states to estimate uncertainty of reasoning steps. Matches/surpasses PRMs 810x larger. **RELEVANT** -- provides the uncertainty estimation component that could be used for routing.

- **ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (arXiv:2510.15981)** -- Constructs DAG of logical dependencies between proof steps, formalizes each as intermediate lemma. New SOTA for autoformalization (ProofScore 0.545 vs 0.123 baseline). **MODERATELY RELEVANT** -- modular/structured autoformalization.

---

### Summary Assessment

| Aspect of Proposed Idea | Prior Work Coverage | Key Papers |
|---|---|---|
| Pseudo-formal decomposition (modular NL blocks with premises/conclusions) | **DIRECTLY COVERED** | Barkallah et al. 2605.20531 |
| Block-level LLM verification of decomposed proof modules | **DIRECTLY COVERED** | Barkallah et al. 2605.20531 |
| Uncertainty-guided routing/selection | **COVERED in adjacent domains** | Grammars of Formal Uncertainty (NeurIPS'25), UCCI, Reasoning with Confidence |
| Routing uncertain blocks to formal verification (Lean 4) | **PARTIALLY COVERED** | VERGE (semantic routing), HERMES (interleaved formal/informal) |
| Combined system: pseudo-formal decomposition + uncertainty routing to Lean 4 | **NOT DIRECTLY COVERED as a single system** | -- |

### Verdict

The **most critical competing paper** is **Barkallah et al. "Pseudo-Formalization for Automatic Proof Verification" (arXiv:2605.20531, May 2026)**, which implements the core pseudo-formal decomposition with modular NL proof blocks having explicit premises/conclusions, verified by LLM-based Block Verification. This paper was posted very recently (May 2026) and directly overlaps with the "pseudo-formal decomposition" component of the proposed idea.

The specific **novelty gap** that the proposed idea could still claim is the **uncertainty-guided selective routing to formal verification (Lean 4)**. Barkallah et al. verify all blocks with LLMs only; the proposed idea would route uncertain blocks to Lean 4 while keeping confident blocks with LLM verification. However, the individual components (uncertainty estimation for verification, routing between formal/informal, and the pseudo-formal decomposition itself) all have strong prior art. The integration of these specific components into a single pipeline is where novelty would need to be argued.

Additionally, **VERGE** (Jan 2026) already implements a form of semantic routing between formal (SMT) and informal (consensus) verification, and **HERMES** (ICML 2026) interleaves informal reasoning with Lean 4 formal verification steps.

---

### Sources

- [Pseudo-Formalization for Automatic Proof Verification (Barkallah et al.)](https://arxiv.org/abs/2605.20531)
- [Grammars of Formal Uncertainty (NeurIPS 2025)](https://arxiv.org/abs/2505.20047)
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)
- [HERMES: Efficient and Verifiable Mathematical Reasoning (ICML 2026)](https://arxiv.org/abs/2511.18760)
- [Safe: Step-aware Formal Verification (ACL 2025)](https://arxiv.org/abs/2506.04592)
- [Reasoning with Confidence: Uncertainty Heads](https://arxiv.org/abs/2511.06209)
- [UCCI: Calibrated Uncertainty for LLM Cascade Routing](https://arxiv.org/abs/2605.18796)
- [ProofSketcher: Hybrid LLM + Lightweight Proof Checker](https://arxiv.org/abs/2604.06401)
- [StepProof: Step-by-step Verification](https://arxiv.org/abs/2506.10558)
- [ProofFlow: Dependency Graph Autoformalization](https://arxiv.org/abs/2510.15981)
- [ProofBridge: Auto-Formalization in Lean via Joint Embeddings](https://arxiv.org/abs/2510.15681)
- [FormalEvolve: Neuro-Symbolic Evolutionary Autoformalization](https://arxiv.org/abs/2603.19828)
- [Faithful Autoformalization via Roundtrip Verification](https://arxiv.org/abs/2604.25031)
- [130k Lines of Formal Topology](https://arxiv.org/abs/2601.03298)
- [Uncertainty-Aware Step-wise Verification (CoT Entropy)](https://arxiv.org/abs/2502.11250)
- [ADAPT: Adaptive Proof Refinement](https://arxiv.org/abs/2510.25103)
- [ICML 2026 Workshop: Statistical Frameworks for Uncertainty in Agentic Systems](https://agentic-uncertainty-icml2026.github.io/)
- [AI for Math Workshop at ICML 2026](https://ai4math2026.github.io/)
- [OpenReview: Grammars of Formal Uncertainty](https://openreview.net/forum?id=QfKpJ00t2L)&lt;/result>
&lt;usage>&lt;total_tokens>31868&lt;/total_tokens>&lt;tool_uses>29&lt;/tool_uses>&lt;duration_ms>205070&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2bf4b1b-743d-4ed0-a69b-9b15992c1905",
  "isSidechain": false,
  "promptId": "28415887-e53e-4d69-9605-a560114deea1",
  "type": "user",
  "uuid": "aad2913e-d4d8-4edc-ac95-36db03026a2a",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-27T12:21:28.295Z_

<details><summary>Logged reasoning block</summary>

```text
The concurrent work search agent has completed with very detailed findings. Now let me wait for the last agent (reference verification) to complete.

Key findings from concurrent work search:
1. Barkallah et al. (arXiv:2605.20531) is the PF paper referenced in the proposal - it's the foundation, not a competitor
2. VERGE (Jan 2026) implements semantic routing between formal (SMT) and informal verification
3. HERMES (ICML 2026) interleaves informal reasoning with Lean 4 formal verification


4. Several other recent papers address related aspects: uncertainty-guided selective verification, calibrated uncertainty for routing decisions, hybrid LLM and proof checker approaches, and step-by-step proof verification through autoformalization

The novelty gap is confirmed—combining PF's modular blocks with uncertainty-guided routing to Lean 4 hasn't been explored yet, though the individual components are appearing across the literature. I should also flag that "Bhatt et al., 2025" didn't surface in my search results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aad2913e-d4d8-4edc-ac95-36db03026a2a",
  "isSidechain": false,
  "requestId": "req_011CbT4gVMM2EEjUL3EN1iLy",
  "type": "assistant",
  "uuid": "828c505c-0a63-44e4-82b6-7e378253a7ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135n19NXT397FQxoKfiNzdC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4944,
      "cache_read_input_tokens": 25752,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 464,
          "cache_read_input_tokens": 25752,
          "cache_creation_input_tokens": 4944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4944
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

_source line 42 · 2026-05-27T12:21:29.015Z_

Concurrent work search agent completed. Critical findings:
- **VERGE** (Jan 2026) implements semantic routing between formal/informal verification
- **HERMES** (ICML 2026) interleaves informal reasoning with Lean 4 formal verification
- The specific PF + uncertainty-guided routing to Lean 4 combination is **NOT directly covered** — novelty gap confirmed
- "Bhatt et al. 2025" and "Mu et al. 2026" may not be verifiable papers

Still waiting on the reference verification agent.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "828c505c-0a63-44e4-82b6-7e378253a7ea",
  "isSidechain": false,
  "requestId": "req_011CbT4gVMM2EEjUL3EN1iLy",
  "type": "assistant",
  "uuid": "b86219f2-d605-4b6b-8874-691d5cbe364f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135n19NXT397FQxoKfiNzdC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4944,
      "cache_read_input_tokens": 25752,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 464,
          "cache_read_input_tokens": 25752,
          "cache_creation_input_tokens": 4944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4944
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

_source line 43 · 2026-05-27T12:24:25.221Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T12:24:25.221Z",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "content": "&lt;task-notification>\n&lt;task-id>a9a2f7dc93ea0cae4&lt;/task-id>\n&lt;tool-use-id>toolu_018jnnUy67G9qXWG6rRVFjK1&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/a9a2f7dc93ea0cae4.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Verify references and baselines\" completed&lt;/summary>\n&lt;result>Now I have all the information needed. Here is my comprehensive report:\n\n---\n\n## Paper Verification Report\n\n### 1. \"Pseudo-Formalization\" by Barkallah et al., May 2026\n\n**FOUND.** The paper is titled \"Pseudo-Formalization for Automatic Proof Verification\" by Slim Barkallah, Luke Bailey, Kaiyue Wen, Mohammed Abouzaid, and Tengyu Ma. It was posted to arXiv on May 19, 2026 (arXiv:2605.20531). Note the first author's first name is **Slim**, not a different Barkallah.\n\n- **Venue/Year:** arXiv preprint, May 2026 (no confirmed conference venue yet)\n- **Key results:** Pseudo-Formalization (PF) is a proof format combining formal modularity with natural language flexibility. Block Verification (BV) verifies each module independently. PF+BV Pareto-dominates LLM-as-judge baselines on error-finding precision and recall across olympiad and research-level math benchmarks. The authors release **ArxivMathGradingBench**, a research-level proof verification benchmark.\n- **On the ~50% error detection claim:** I could not confirm the specific \"~50%\" number from search results alone. The paper reports precision-recall curves where PF+BV dominates baselines, but the exact 50% figure would require reading the full paper tables.\n\nSources: [arXiv abs](https://arxiv.org/abs/2605.20531), [arXiv HTML](https://arxiv.org/html/2605.20531)\n\n---\n\n### 2. \"Safe\" by Liu et al., ACL 2025\n\n**FOUND.** The paper is \"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification\" by Chengwu Liu et al. (Peking University, Huawei Noah's Ark Lab, HKUST, HK PolyU).\n\n- **Venue/Year:** ACL 2025 Main Conference (published June 2025, arXiv:2506.04592)\n- **Key results:** First work to use Lean 4 for verifying LLM-generated natural language reasoning step by step. Proposes **FormalStep** benchmark with 30,809 formal statements. The framework auto-formalizes each step, validates the Lean 4 theorem via Lean REPL, attempts proof with an LLM-based prover, then verifies. Demonstrates \"significant performance improvement\" across multiple LLMs and math datasets.\n- **On the ~80% proof success claim:** The specific \"~80%\" figure was not confirmed from search snippets. The full paper's tables would need to be consulted for exact proof success rates on FormalStep.\n\nSources: [ACL Anthology](https://aclanthology.org/2025.acl-long.594/), [GitHub](https://github.com/liuchengwucn/Safe), [arXiv](https://arxiv.org/abs/2506.04592)\n\n---\n\n### 3. \"Hard2Verify\" -- Zheng et al., 2025\n\n**FOUND, but authorship correction needed.** The paper is \"Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math\" (arXiv:2510.13744, October 2025). It is from **Salesforce AI Research** and authored by **Shrey Pandit, Austin Xu, Xuan-Phi Nguyen, Yifei Ming, Caiming Xiong, and Shafiq Joty** -- NOT \"Zheng et al.\" The name \"Zheng\" may be confused with the ProcessBench paper (Zheng et al., 2024) which is cited by Hard2Verify.\n\n- **Venue/Year:** arXiv preprint, October 2025 (500+ hours of human annotation)\n- **Key results:** The specific numbers you cited are **confirmed**: Qwen2.5-Math-PRM-72B drops from **78.3** on ProcessBench to **37.3** on Hard2Verify for error identification. This demonstrates that existing PRMs trained on competition-level math fail dramatically on frontier/research-level math.\n\nSources: [arXiv abs](https://arxiv.org/abs/2510.13744), [arXiv HTML](https://arxiv.org/html/2510.13744v1), [ResearchGate](https://www.researchgate.net/publication/396517985_Hard2Verify_A_Step-Level_Verification_Benchmark_for_Open-Ended_Frontier_Math)\n\n---\n\n### 4. \"miniF2F-Lean Revisited\" 2025\n\n**FOUND.** The paper is \"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward\" (arXiv:2511.03108).\n\n- **Venue/Year:** **NeurIPS 2025** (poster)\n- **Key results (confirmed numbers):**\n  - Herald autoformalization reports **97%** accuracy when evaluated by LLM, but human review reveals actual accuracy is only **66%** -- a 31-point gap\n  - Kimina Prover achieves **70.8%** on miniF2F\n  - Combined end-to-end pipeline accuracy drops to **34.8%** when comparing final proofs against original informal problem statements\n  - On corrected **miniF2F-v2**, best accuracy improves to **70%** (up from 40% on original miniF2F)\n\nSources: [arXiv](https://arxiv.org/abs/2511.03108), [NeurIPS 2025 poster](https://neurips.cc/virtual/2025/poster/118598), [OpenReview](https://openreview.net/forum?id=KtaHv0YUyh)\n\n---\n\n### 5. Bhatt et al., 2025 -- Uncertainty-guided selective verification with SMT\n\n**NOT CONFIRMED as \"Bhatt et al.\"** The closest matching paper is \"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks\" (arXiv:2505.20047, May 2025), presented at **NeurIPS 2025**. However, the authors are **Debargha Ganguly, Vikash Singh, Sreehari Sankar, Biyao Zhang, Xuecen Zhang, Srinivasan Iyengar, Xiaotian Han, Amit Sharma, Shivkumar Kalyanaraman, and Vipin Chaudhary** -- no author named \"Bhatt\" appears.\n\n- **Venue/Year:** NeurIPS 2025\n- **Key results:** Evaluates 5 frontier LLMs on SMT-LIB autoformalization. SMT accuracy varies by domain: +34.8% on logical tasks, -44.5% on factual ones. Introduces PCFG framework with 25 uncertainty metrics. Lightweight fusion of uncertainty signals enables selective verification that cuts error rates by **14-100%** with minimal abstention. Grammar entropy achieves AUROC &gt; 0.93 for logic tasks.\n- **Assessment:** The topic matches exactly (uncertainty-guided selective verification with SMT), but the authorship \"Bhatt et al.\" does not match. Either the attribution is incorrect, or there is a different paper by Bhatt that I could not find.\n\nSources: [arXiv](https://arxiv.org/abs/2505.20047), [NeurIPS poster](https://neurips.cc/virtual/2025/poster/118114), [Microsoft Research](https://www.microsoft.com/en-us/research/publication/grammars-of-formal-uncertainty-when-to-trust-llms-in-automated-reasoning-tasks/), [GitHub](https://github.com/DebarghaG/grammars-formal-uncertainty)\n\n---\n\n### 6. Mu et al., 2026 -- Adaptive verification allocation, 44% fewer verifier calls on MATH\n\n**FOUND, but authorship correction needed.** The paper is \"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure\" (arXiv:2602.03975, February 2026). The author listed is **Shuhui Qu** (Stanford University) -- not \"Mu et al.\"\n\n- **Venue/Year:** arXiv preprint, February 2026\n- **Key results:** Proposes state-level selective verification combining deterministic feasibility gating, hybrid pre-verification ranking, and adaptive verifier call allocation based on local uncertainty. Achieves higher accuracy than best-of-N, majority voting, and beam search while using **44% fewer verifier calls** on the MATH benchmark with Llama 3.2 1B as the generator and a PRM as verifier.\n- **Assessment:** The \"44% fewer verifier calls\" claim is confirmed, but the authorship is \"Qu\" not \"Mu.\"\n\nSources: [arXiv abs](https://arxiv.org/abs/2602.03975), [arXiv HTML](https://arxiv.org/html/2602.03975)\n\n---\n\n## Baseline Numbers\n\n### Best PRM accuracy on research-level math proofs\n- **ProcessBench SOTA:** Qwen2.5-Math-PRM-72B achieves **78.3** on ProcessBench (competition-level), but drops to **37.3** on Hard2Verify (frontier/research-level)\n- **R-PRM** surpasses baselines by **11.9** and **8.5** F1 points on ProcessBench and PRMBench respectively\n- **ThinkPRM** beats PRM800K-trained discriminative verifiers by **8%** and **4.5%** on GPQA-Diamond and LiveCodeBench\n- Bottom line: No PRM achieves reliable accuracy on research-level proofs; the best models barely exceed 37% on frontier math\n\n### Safe's formal verification success rate and cost overhead\n- Exact success rate percentage (the \"~80%\" claim) was **not confirmed** from search results. The paper reports \"significant performance improvement\" but specific numbers require reading the full paper tables. The FormalStep benchmark contains 30,809 formal statements. Cost overhead details were not retrievable from web search.\n\n### State of the art on ArxivMathGradingBench\n- This benchmark was **just released** with the Pseudo-Formalization paper (May 2026). PF+BV Pareto-dominates LLM-as-judge baselines. No other published work appears to report results on it yet, making the Barkallah et al. results the current (and only) SOTA.\n\n### Autoformalization success rates (NL to Lean 4)\n- **LLM-judged autoformalization:** up to 97% (Herald on miniF2F) -- but this is **inflated**\n- **Human-judged autoformalization:** only **66%** (same Herald outputs reviewed by humans)\n- **End-to-end (autoformalize + prove + verify):** **34.8%** on original miniF2F\n- **On corrected miniF2F-v2:** **70%** best accuracy\n- **Other benchmarks:** 68.4% pass rate reported on miniF2F by other methods; 87% task success rate for agentic proof automation on System Capless (Xu &amp; Odersky, 2026)\n\n---\n\n## Summary of Issues Found\n\nThree of the six papers have **incorrect author attributions** in your list:\n1. **Hard2Verify** is by Pandit, Xu, Nguyen et al. (Salesforce), not \"Zheng et al.\" (Zheng wrote ProcessBench, which Hard2Verify cites)\n2. **\"Bhatt et al.\"** does not match any found paper. The closest match (Ganguly et al., \"Grammars of Formal Uncertainty\") has no author named Bhatt\n3. **\"Mu et al.\"** does not match -- the adaptive verification paper is by **Shuhui Qu** (Stanford), not \"Mu\"\n\nAll six papers' core claims and topics are real and verifiable, but the specific quantitative claims for Safe (~80%) and Pseudo-Formalization (~50%) could not be confirmed or denied from web search alone -- the full paper PDFs would need to be read.&lt;/result>\n&lt;usage>&lt;total_tokens>30373&lt;/total_tokens>&lt;tool_uses>27&lt;/tool_uses>&lt;duration_ms>384425&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 44 · 2026-05-27T12:24:25.284Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T12:24:25.284Z",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

## Round 5

29 recorded events

### User

_source line 45 · 2026-05-27T12:24:25.292Z_

&lt;task-notification>
&lt;task-id>a9a2f7dc93ea0cae4&lt;/task-id>
&lt;tool-use-id>toolu_018jnnUy67G9qXWG6rRVFjK1&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/d50cf128-39c2-46f2-abb0-ee1a4faf1620/tasks/a9a2f7dc93ea0cae4.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Verify references and baselines" completed&lt;/summary>
&lt;result>Now I have all the information needed. Here is my comprehensive report:

---

## Paper Verification Report

### 1. "Pseudo-Formalization" by Barkallah et al., May 2026

**FOUND.** The paper is titled "Pseudo-Formalization for Automatic Proof Verification" by Slim Barkallah, Luke Bailey, Kaiyue Wen, Mohammed Abouzaid, and Tengyu Ma. It was posted to arXiv on May 19, 2026 (arXiv:2605.20531). Note the first author's first name is **Slim**, not a different Barkallah.

- **Venue/Year:** arXiv preprint, May 2026 (no confirmed conference venue yet)
- **Key results:** Pseudo-Formalization (PF) is a proof format combining formal modularity with natural language flexibility. Block Verification (BV) verifies each module independently. PF+BV Pareto-dominates LLM-as-judge baselines on error-finding precision and recall across olympiad and research-level math benchmarks. The authors release **ArxivMathGradingBench**, a research-level proof verification benchmark.
- **On the ~50% error detection claim:** I could not confirm the specific "~50%" number from search results alone. The paper reports precision-recall curves where PF+BV dominates baselines, but the exact 50% figure would require reading the full paper tables.

Sources: [arXiv abs](https://arxiv.org/abs/2605.20531), [arXiv HTML](https://arxiv.org/html/2605.20531)

---

### 2. "Safe" by Liu et al., ACL 2025

**FOUND.** The paper is "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification" by Chengwu Liu et al. (Peking University, Huawei Noah's Ark Lab, HKUST, HK PolyU).

- **Venue/Year:** ACL 2025 Main Conference (published June 2025, arXiv:2506.04592)
- **Key results:** First work to use Lean 4 for verifying LLM-generated natural language reasoning step by step. Proposes **FormalStep** benchmark with 30,809 formal statements. The framework auto-formalizes each step, validates the Lean 4 theorem via Lean REPL, attempts proof with an LLM-based prover, then verifies. Demonstrates "significant performance improvement" across multiple LLMs and math datasets.
- **On the ~80% proof success claim:** The specific "~80%" figure was not confirmed from search snippets. The full paper's tables would need to be consulted for exact proof success rates on FormalStep.

Sources: [ACL Anthology](https://aclanthology.org/2025.acl-long.594/), [GitHub](https://github.com/liuchengwucn/Safe), [arXiv](https://arxiv.org/abs/2506.04592)

---

### 3. "Hard2Verify" -- Zheng et al., 2025

**FOUND, but authorship correction needed.** The paper is "Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math" (arXiv:2510.13744, October 2025). It is from **Salesforce AI Research** and authored by **Shrey Pandit, Austin Xu, Xuan-Phi Nguyen, Yifei Ming, Caiming Xiong, and Shafiq Joty** -- NOT "Zheng et al." The name "Zheng" may be confused with the ProcessBench paper (Zheng et al., 2024) which is cited by Hard2Verify.

- **Venue/Year:** arXiv preprint, October 2025 (500+ hours of human annotation)
- **Key results:** The specific numbers you cited are **confirmed**: Qwen2.5-Math-PRM-72B drops from **78.3** on ProcessBench to **37.3** on Hard2Verify for error identification. This demonstrates that existing PRMs trained on competition-level math fail dramatically on frontier/research-level math.

Sources: [arXiv abs](https://arxiv.org/abs/2510.13744), [arXiv HTML](https://arxiv.org/html/2510.13744v1), [ResearchGate](https://www.researchgate.net/publication/396517985_Hard2Verify_A_Step-Level_Verification_Benchmark_for_Open-Ended_Frontier_Math)

---

### 4. "miniF2F-Lean Revisited" 2025

**FOUND.** The paper is "miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward" (arXiv:2511.03108).

- **Venue/Year:** **NeurIPS 2025** (poster)
- **Key results (confirmed numbers):**
  - Herald autoformalization reports **97%** accuracy when evaluated by LLM, but human review reveals actual accuracy is only **66%** -- a 31-point gap
  - Kimina Prover achieves **70.8%** on miniF2F
  - Combined end-to-end pipeline accuracy drops to **34.8%** when comparing final proofs against original informal problem statements
  - On corrected **miniF2F-v2**, best accuracy improves to **70%** (up from 40% on original miniF2F)

Sources: [arXiv](https://arxiv.org/abs/2511.03108), [NeurIPS 2025 poster](https://neurips.cc/virtual/2025/poster/118598), [OpenReview](https://openreview.net/forum?id=KtaHv0YUyh)

---

### 5. Bhatt et al., 2025 -- Uncertainty-guided selective verification with SMT

**NOT CONFIRMED as "Bhatt et al."** The closest matching paper is "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks" (arXiv:2505.20047, May 2025), presented at **NeurIPS 2025**. However, the authors are **Debargha Ganguly, Vikash Singh, Sreehari Sankar, Biyao Zhang, Xuecen Zhang, Srinivasan Iyengar, Xiaotian Han, Amit Sharma, Shivkumar Kalyanaraman, and Vipin Chaudhary** -- no author named "Bhatt" appears.

- **Venue/Year:** NeurIPS 2025
- **Key results:** Evaluates 5 frontier LLMs on SMT-LIB autoformalization. SMT accuracy varies by domain: +34.8% on logical tasks, -44.5% on factual ones. Introduces PCFG framework with 25 uncertainty metrics. Lightweight fusion of uncertainty signals enables selective verification that cuts error rates by **14-100%** with minimal abstention. Grammar entropy achieves AUROC &gt; 0.93 for logic tasks.
- **Assessment:** The topic matches exactly (uncertainty-guided selective verification with SMT), but the authorship "Bhatt et al." does not match. Either the attribution is incorrect, or there is a different paper by Bhatt that I could not find.

Sources: [arXiv](https://arxiv.org/abs/2505.20047), [NeurIPS poster](https://neurips.cc/virtual/2025/poster/118114), [Microsoft Research](https://www.microsoft.com/en-us/research/publication/grammars-of-formal-uncertainty-when-to-trust-llms-in-automated-reasoning-tasks/), [GitHub](https://github.com/DebarghaG/grammars-formal-uncertainty)

---

### 6. Mu et al., 2026 -- Adaptive verification allocation, 44% fewer verifier calls on MATH

**FOUND, but authorship correction needed.** The paper is "Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure" (arXiv:2602.03975, February 2026). The author listed is **Shuhui Qu** (Stanford University) -- not "Mu et al."

- **Venue/Year:** arXiv preprint, February 2026
- **Key results:** Proposes state-level selective verification combining deterministic feasibility gating, hybrid pre-verification ranking, and adaptive verifier call allocation based on local uncertainty. Achieves higher accuracy than best-of-N, majority voting, and beam search while using **44% fewer verifier calls** on the MATH benchmark with Llama 3.2 1B as the generator and a PRM as verifier.
- **Assessment:** The "44% fewer verifier calls" claim is confirmed, but the authorship is "Qu" not "Mu."

Sources: [arXiv abs](https://arxiv.org/abs/2602.03975), [arXiv HTML](https://arxiv.org/html/2602.03975)

---

## Baseline Numbers

### Best PRM accuracy on research-level math proofs
- **ProcessBench SOTA:** Qwen2.5-Math-PRM-72B achieves **78.3** on ProcessBench (competition-level), but drops to **37.3** on Hard2Verify (frontier/research-level)
- **R-PRM** surpasses baselines by **11.9** and **8.5** F1 points on ProcessBench and PRMBench respectively
- **ThinkPRM** beats PRM800K-trained discriminative verifiers by **8%** and **4.5%** on GPQA-Diamond and LiveCodeBench
- Bottom line: No PRM achieves reliable accuracy on research-level proofs; the best models barely exceed 37% on frontier math

### Safe's formal verification success rate and cost overhead
- Exact success rate percentage (the "~80%" claim) was **not confirmed** from search results. The paper reports "significant performance improvement" but specific numbers require reading the full paper tables. The FormalStep benchmark contains 30,809 formal statements. Cost overhead details were not retrievable from web search.

### State of the art on ArxivMathGradingBench
- This benchmark was **just released** with the Pseudo-Formalization paper (May 2026). PF+BV Pareto-dominates LLM-as-judge baselines. No other published work appears to report results on it yet, making the Barkallah et al. results the current (and only) SOTA.

### Autoformalization success rates (NL to Lean 4)
- **LLM-judged autoformalization:** up to 97% (Herald on miniF2F) -- but this is **inflated**
- **Human-judged autoformalization:** only **66%** (same Herald outputs reviewed by humans)
- **End-to-end (autoformalize + prove + verify):** **34.8%** on original miniF2F
- **On corrected miniF2F-v2:** **70%** best accuracy
- **Other benchmarks:** 68.4% pass rate reported on miniF2F by other methods; 87% task success rate for agentic proof automation on System Capless (Xu &amp; Odersky, 2026)

---

## Summary of Issues Found

Three of the six papers have **incorrect author attributions** in your list:
1. **Hard2Verify** is by Pandit, Xu, Nguyen et al. (Salesforce), not "Zheng et al." (Zheng wrote ProcessBench, which Hard2Verify cites)
2. **"Bhatt et al."** does not match any found paper. The closest match (Ganguly et al., "Grammars of Formal Uncertainty") has no author named Bhatt
3. **"Mu et al."** does not match -- the adaptive verification paper is by **Shuhui Qu** (Stanford), not "Mu"

All six papers' core claims and topics are real and verifiable, but the specific quantitative claims for Safe (~80%) and Pseudo-Formalization (~50%) could not be confirmed or denied from web search alone -- the full paper PDFs would need to be read.&lt;/result>
&lt;usage>&lt;total_tokens>30373&lt;/total_tokens>&lt;tool_uses>27&lt;/tool_uses>&lt;duration_ms>384425&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b86219f2-d605-4b6b-8874-691d5cbe364f",
  "isSidechain": false,
  "promptId": "6c520205-97f1-438f-ab6f-f4fa04854d77",
  "type": "user",
  "uuid": "733ecb0c-2c7f-4217-b947-2106a4ddb843",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 46 · 2026-05-27T12:24:25.291Z_

```json
{
  "parentUuid": "733ecb0c-2c7f-4217-b947-2106a4ddb843",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0b30d661-b4ec-4b18-aaca-c87610e4c3b8",
  "timestamp": "2026-05-27T12:24:25.291Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Uncertainty-Guided Selec…",
  "leafUuid": "0b30d661-b4ec-4b18-aaca-c87610e4c3b8",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective proof block formalization",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Assistant

_source line 49 · 2026-05-27T12:26:04.423Z_

<details><summary>Logged reasoning block</summary>

```text
All four agents have completed. Let me now synthesize everything into the final JSON output. Let me gather all the key findings:

**Concurrent Work:**
- Barkallah et al. (arXiv:2605.20531, May 2026) - PF paper, foundation not competitor
- VERGE (arXiv:2601.20055, Jan 2026) - semantic routing between formal/informal
- HERMES (arXiv:2511.18760, ICML 2026) - interleaves informal with Lean 4


- Grammars of Formal Uncertainty (NeurIPS 2025) - uncertainty-guided selective verification with SMT
- UCCI (arXiv:2605.18796, May 2026) - calibrated uncertainty for routing
- ProofSketcher (arXiv:2604.06401, April 2026) - hybrid LLM + proof checker
- StepProof - step-by-step NL proof verification via autoformalization
- Uncertainty Heads (arXiv:2511.06209) - lightweight uncertainty estimation for reasoning steps

The key novelty here is combining PF blocks with uncertainty-driven routing to Lean 4, which hasn't been explored yet. Now I need to verify the references and finalize the output. Now I'm looking at the key models and implementations for this approach—there's StepFun-Formalizer and Leanstral for autoformalization, DeepSeek-R1 and QwQ for math reasoning, and Goedel-Prover-V2 achieving strong performance on MiniF2F benchmarks. The infrastructure requirements show that A100 GPUs are sufficient, with training times around 56 hours for smaller quantized models.

I'm also tracking the relevant conference deadlines—AAAI 2027 in late July and EACL 2027 in early August are both viable targets after my May cutoff. Now I need to clean up the references and verify the model names are current, then structure everything into a proper JSON format with only the venues and citations that actually check out.

For the approach, I'm extending Pseudo-Formalization by layering in a two-tier verification system that uses uncertainty signals to decide which proof blocks need formal verification. The pipeline decomposes proofs into modular blocks, runs LLM verification with calibrated confidence scores derived from ensemble disagreement and entropy metrics, then selectively routes the most uncertain blocks to autoformalization and formal checking with specialized tools. This targeted approach catches errors the LLM alone would miss while keeping computational overhead reasonable at around 1.5-2x the base cost.

The implementation requires about 200-400 GPU-hours for fine-tuning and experiments on standard benchmarks, with a 3-4 month timeline. Using Claude API support could trim that by roughly 30%, though the Lean 4 integration will still need hands-on debugging. I'm targeting AAAI 2027 and EACL 2027 as submission venues.

This is a solid contribution—combining existing strong components in a novel way without being fundamentally paradigm-shifting. I'm pulling from verified recent work on pseudo-formalization, step-aware verification, and formal uncertainty estimation, with the key references spanning 2025-2026 publications.

Now I need to verify a few of the more recent citations the agents surfaced—particularly VERGE, HERMES, Goedel-Prover-V2, and StepFun-Formalizer—to make sure they're legitimate before finalizing the answer.

Looking at what the agents found, VERGE implements semantic routing between formal and informal verification approaches, while HERMES interleaves informal reasoning with Lean 4 formal verification. Both are worth highlighting in the landscape update.

I'm also working through the resource estimates more carefully—breaking down GPU hours for fine-tuning uncertainty calibration, running inference on the formalizer, and executing the prover on the most uncertain blocks.

The manual approach comes to around 300 GPU-hours total with a 10-14 week timeline and $600-900 in cloud costs. The human-in-loop version keeps similar GPU requirements but adds Claude API costs and compresses the timeline to 7-10 weeks. The auto research approach is fastest at 4-6 weeks but requires more GPU exploration and higher API spending, though the real bottleneck is going to be Lean 4 compilation and proof search latency.

Now I'm settling on a project name and writing up the description. I'm thinking "unc_guided_pf_verify" captures the core idea of using uncertainty to guide which proofs get formally verified. For the description, I'm outlining a two-tier pipeline where we first decompose proofs into modular blocks, run LLM verification with confidence scoring based on ensemble disagreement and token entropy, then selectively formalize the most uncertain blocks to Lean 4.

The key insight is that these self-contained blocks with explicit premises and conclusions are much easier to autoformalize reliably than raw natural language, so we can achieve near-formal verification quality at a fraction of the cost by concentrating resources where uncertainty is highest.

Now I need to audit the references and correct any misattributions—looks like I have some papers listed with wrong author names or future dates that I should verify and fix. I'm going through the remaining references to verify them—checking the titles, authors, venues, and years to make sure everything's accurate before finalizing the list. I need to be careful here—the user wants me to keep all existing fields as-is, even if there are attribution errors in the landscape text. So I'll add the new fields with corrected references while preserving the original content unchanged, and I can note the concurrent work findings separately in the key_references or approach sections.

For the approach, I'm describing a two-tier verification system that starts with Pseudo-Formalization, then uses an LLM to verify blocks with confidence scoring based on ensemble disagreement and token-level entropy calibrated through isotonic regression. Lower-confidence blocks get autoformalized to Lean 4 and formally verified through a proof checker.

Now I'm working through the resource estimates more carefully. The manual approach requires around 300-400 GPU hours spread across calibration, formalization inference, proof search, and baseline comparisons, taking 10-14 weeks with 2-3 researchers at roughly $600-1200 in costs. The human-in-loop variant cuts this down to about 300 GPU hours over 7-10 weeks.

For the fully automated approach, I'm looking at roughly 350 GPU hours over 4-6 weeks with Claude API costs between $500-800 and GPU costs around $700-1050, though the real constraint here is that Lean 4 proof search runs sequentially—each block takes minutes and depends on previous results, so there's a hard limit on parallelization.

I need to finalize the JSON output now, but I'm also reconsidering the landscape section. The instructions emphasize keeping existing fields while adding new ones, and they specifically note that concurrent work should be explicitly mentioned in the landscape if found. I think the right approach is to update the landscape field to incorporate those concurrent work references rather than leaving them separate.

Writing the final JSON... SOTA models

Let me finalize the key_references list. Each needs to be "Paper title (VENUE YEAR)":

1. "Pseudo-Formalization for Automatic Proof Verification (arXiv 2026)" - verified
2. "Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)" - verified
3. "Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (arXiv 2025)" - verified
4. "miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward (NeurIPS 2025)" - verified
5. "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (NeurIPS 2025)" - verified
6. "Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (arXiv 2026)" - verified
7. "VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv 2026)" - verified
8. "HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (ICML 2026)" - verified
9. "Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads (arXiv 2025)" - verified
10. "Goedel-Prover-V2 (arXiv 2026)" - need to track down the actual paper venue since the agent only mentioned the GitHub repo. I should also double-check the ProcessBench reference from Zheng et al. that was mentioned earlier.

I'm clarifying the performance metrics now—Hard2Verify shows Qwen2.5-Math-PRM-72B dropping from 78.3% on ProcessBench down to 37.3% on their benchmark, so both numbers come from the Hard2Verify paper's comparison. I need to finalize the JSON output while being careful about the landscape updates with concurrent work, ensuring references have correct attributions, and noting that only AAAI 2027 and EACL 2027 have confirmed deadlines after May 27, 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b30d661-b4ec-4b18-aaca-c87610e4c3b8",
  "isSidechain": false,
  "requestId": "req_011CbT4vKAosLaGJaeBpwJgZ",
  "type": "assistant",
  "uuid": "e79c1d7b-4b29-4e8b-86c1-2dba0f9d474b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLh9anH3fzuJiFgHHA1kZx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3747,
      "cache_read_input_tokens": 30696,
      "output_tokens": 5264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5264,
          "cache_read_input_tokens": 30696,
          "cache_creation_input_tokens": 3747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3747
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

_source line 50 · 2026-05-27T12:26:04.425Z_

All four agents have completed. Let me do a few targeted verification searches before composing the final output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e79c1d7b-4b29-4e8b-86c1-2dba0f9d474b",
  "isSidechain": false,
  "requestId": "req_011CbT4vKAosLaGJaeBpwJgZ",
  "type": "assistant",
  "uuid": "b0f35b98-5474-45a9-9249-02b7b447d921",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLh9anH3fzuJiFgHHA1kZx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3747,
      "cache_read_input_tokens": 30696,
      "output_tokens": 5264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5264,
          "cache_read_input_tokens": 30696,
          "cache_creation_input_tokens": 3747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3747
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

_source line 51 · 2026-05-27T12:26:04.737Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QVyG6dNEUQXUNd8hYaMaER`</summary>

```json
{
  "query": "ICLR 2027 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0f35b98-5474-45a9-9249-02b7b447d921",
  "isSidechain": false,
  "requestId": "req_011CbT4vKAosLaGJaeBpwJgZ",
  "type": "assistant",
  "uuid": "ee7f61e2-b518-4e3f-8c6a-b11b7fb147cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLh9anH3fzuJiFgHHA1kZx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3747,
      "cache_read_input_tokens": 30696,
      "output_tokens": 5264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5264,
          "cache_read_input_tokens": 30696,
          "cache_creation_input_tokens": 3747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3747
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

_source line 52 · 2026-05-27T12:26:05.196Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019TfcD5KHvpMUBiTrSwRRB2`</summary>

```json
{
  "query": "Goedel-Prover-V2 paper arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee7f61e2-b518-4e3f-8c6a-b11b7fb147cc",
  "isSidechain": false,
  "requestId": "req_011CbT4vKAosLaGJaeBpwJgZ",
  "type": "assistant",
  "uuid": "ad9477ec-fc48-4eda-8338-0dba4e9663dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLh9anH3fzuJiFgHHA1kZx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3747,
      "cache_read_input_tokens": 30696,
      "output_tokens": 5264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5264,
          "cache_read_input_tokens": 30696,
          "cache_creation_input_tokens": 3747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3747
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

_source line 53 · 2026-05-27T12:26:05.904Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015zuc9jSaj7nFhtwQuBQm2x`</summary>

```json
{
  "query": "VERGE formal refinement guidance engine arxiv 2601.20055"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad9477ec-fc48-4eda-8338-0dba4e9663dc",
  "isSidechain": false,
  "requestId": "req_011CbT4vKAosLaGJaeBpwJgZ",
  "type": "assistant",
  "uuid": "e3e10827-548d-43e6-a0f8-454db55b00bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLh9anH3fzuJiFgHHA1kZx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3747,
      "cache_read_input_tokens": 30696,
      "output_tokens": 5264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5264,
          "cache_read_input_tokens": 30696,
          "cache_creation_input_tokens": 3747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3747
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

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Uncertainty-Guided Selec…",
  "leafUuid": "e3e10827-548d-43e6-a0f8-454db55b00bb",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective proof block formalization",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Tool result

_source line 56 · 2026-05-27T12:26:09.505Z_

<details><summary>↩ Tool result · `toolu_01QVyG6dNEUQXUNd8hYaMaER`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline call for papers"

Links: [{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"Call for Papers","url":"https://iclr.cc/Conferences/2025/CallForPapers"},{"title":"ICLR | OpenReview","url":"https://openreview.net/group?id=ICLR.cc"}]

Based on the search results, I found information about ICLR 2026 but not specific details about ICLR 2027 yet. Here's what I found:

**ICLR 2026:**
The International Conference on Learning Representations welcomes submissions from all areas of machine learning. The conference will be held April 23-25, 2026.

**ICLR 2027:**
ICLR 2027 is predicted to be held April 24-28, 2027, based on previous year schedules, though the official conference website should be verified for confirmed details and deadlines.

The search results show that official 2027 Call for Papers with specific submission deadlines have not yet been published. For the most up-to-date information about ICLR 2027 submission deadlines, I recommend checking the official ICLR website at iclr.cc directly, as the call for papers is typically announced closer to the conference date.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee7f61e2-b518-4e3f-8c6a-b11b7fb147cc",
  "isSidechain": false,
  "promptId": "6c520205-97f1-438f-ab6f-f4fa04854d77",
  "type": "user",
  "uuid": "909dd77b-9de2-4b9f-8e7e-d94b600ad086",
  "toolUseResult": {
    "query": "ICLR 2027 submission deadline call for papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Sef6pDhZkTzJQ24FA6EekG",
        "content": [
          {
            "title": "2026 Dates and Deadlines",
            "url": "https://iclr.cc/Conferences/2026/Dates"
          },
          {
            "title": "International Conference on Learning Representations ICLR in August 2027 in Sydney",
            "url": "https://waset.org/learning-representations-conference-in-august-2027-in-sydney"
          },
          {
            "title": "AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "Key deadlines in AI and ML conferences",
            "url": "https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "Year-Round Deadlines - Imranur Rahman",
            "url": "https://imranur-rahman.github.io/deadlines/"
          },
          {
            "title": "ICLR 2026 Call for Papers",
            "url": "https://iclr.cc/Conferences/2026/CallForPapers"
          },
          {
            "title": "ICLR 2026",
            "url": "https://iclr.cc/"
          },
          {
            "title": "Call for Papers",
            "url": "https://iclr.cc/Conferences/2025/CallForPapers"
          },
          {
            "title": "ICLR | OpenReview",
            "url": "https://openreview.net/group?id=ICLR.cc"
          }
        ]
      },
      "Based on the search results, I found information about ICLR 2026 but not specific details about ICLR 2027 yet. Here's what I found:\n\n**ICLR 2026:**\nThe International Conference on Learning Representations welcomes submissions from all areas of machine learning. The conference will be held April 23-25, 2026.\n\n**ICLR 2027:**\nICLR 2027 is predicted to be held April 24-28, 2027, based on previous year schedules, though the official conference website should be verified for confirmed details and deadlines.\n\nThe search results show that official 2027 Call for Papers with specific submission deadlines have not yet been published. For the most up-to-date information about ICLR 2027 submission deadlines, I recommend checking the official ICLR website at iclr.cc directly, as the call for papers is typically announced closer to the conference date."
    ],
    "durationSeconds": 4.740881326000031,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ee7f61e2-b518-4e3f-8c6a-b11b7fb147cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-27T12:26:13.067Z_

<details><summary>↩ Tool result · `toolu_015zuc9jSaj7nFhtwQuBQm2x`</summary>

```text
Web search results for query: "VERGE formal refinement guidance engine arxiv 2601.20055"

Links: [{"title":"[Literature Review] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://www.themoonlight.io/en/review/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning"},{"title":"[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/abs/2601.20055"},{"title":"Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://huggingface.co/papers/2601.20055"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/pastweek?skip=1181&show=2000"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/pdf/2601.20055"},{"title":"dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"},{"title":"Verge: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning | Hacker News","url":"https://news.ycombinator.com/item?id=46813257"},{"title":"Formal Refinement and Guidance Engine for Verifiable ...","url":"https://www.researchgate.net/publication/400178327_VERGE_Formal_Refinement_and_Guidance_Engine_for_Verifiable_LLM_Reasoning"},{"title":"Adaptive Proof Refinement with LLM-Guided Strategy Selection","url":"https://arxiv.org/pdf/2510.25103"},{"title":"The 4/$\\delta$ Bound: Designing Predictable LLM-Verifier Systems for Formal Method Guarantee","url":"https://arxiv.org/pdf/2512.02080"}]

Based on the search results, here's what I found about VERGE (arxiv 2601.20055):

## Overview

VERGE is a neurosymbolic framework that combines LLMs with SMT solvers to produce verification-guided answers through iterative refinement. The approach decomposes LLM outputs into atomic claims, autoformalizes them into first-order logic, and verifies their logical consistency using automated theorem proving.

## Key Innovations

The framework introduces three key innovations: (1) multi-model consensus via formal semantic equivalence checking to ensure logic-level alignment between candidates, eliminating the syntactic bias of surface-form metrics, (2) semantic routing that directs different claim types to appropriate verification strategies—symbolic solvers for logical claims and LLM ensembles for commonsense reasoning, and (3) precise logical error localization via Minimal Correction Subsets (MCS), which pinpoint the exact subset of claims to revise.

## Authors and Publication

The paper was authored by Vikash Singh, Darion Cassel, Nathaniel Weir, Nick Feng, and Sam Bayless, submitted on January 27, 2026 with a revised version on May 2, 2026.

The paper addresses the challenge of ensuring logical correctness in Large Language Models, particularly in high-stakes applications where provable guarantees are essential.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3e10827-548d-43e6-a0f8-454db55b00bb",
  "isSidechain": false,
  "promptId": "6c520205-97f1-438f-ab6f-f4fa04854d77",
  "type": "user",
  "uuid": "f5ad7014-b6fb-489b-81f3-a0be7adb0506",
  "toolUseResult": {
    "query": "VERGE formal refinement guidance engine arxiv 2601.20055",
    "results": [
      {
        "tool_use_id": "srvtoolu_01K5PQZX2Wey7frojqUwvSxh",
        "content": [
          {
            "title": "[Literature Review] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://www.themoonlight.io/en/review/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning"
          },
          {
            "title": "[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://arxiv.org/abs/2601.20055"
          },
          {
            "title": "Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://huggingface.co/papers/2601.20055"
          },
          {
            "title": "Computer Science",
            "url": "https://www.arxiv.org/list/cs/pastweek?skip=1181&show=2000"
          },
          {
            "title": "VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://arxiv.org/pdf/2601.20055"
          },
          {
            "title": "dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.",
            "url": "https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"
          },
          {
            "title": "Verge: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning | Hacker News",
            "url": "https://news.ycombinator.com/item?id=46813257"
          },
          {
            "title": "Formal Refinement and Guidance Engine for Verifiable ...",
            "url": "https://www.researchgate.net/publication/400178327_VERGE_Formal_Refinement_and_Guidance_Engine_for_Verifiable_LLM_Reasoning"
          },
          {
            "title": "Adaptive Proof Refinement with LLM-Guided Strategy Selection",
            "url": "https://arxiv.org/pdf/2510.25103"
          },
          {
            "title": "The 4/$\\delta$ Bound: Designing Predictable LLM-Verifier Systems for Formal Method Guarantee",
            "url": "https://arxiv.org/pdf/2512.02080"
          }
        ]
      },
      "Based on the search results, here's what I found about VERGE (arxiv 2601.20055):\n\n## Overview\n\nVERGE is a neurosymbolic framework that combines LLMs with SMT solvers to produce verification-guided answers through iterative refinement. The approach decomposes LLM outputs into atomic claims, autoformalizes them into first-order logic, and verifies their logical consistency using automated theorem proving.\n\n## Key Innovations\n\nThe framework introduces three key innovations: (1) multi-model consensus via formal semantic equivalence checking to ensure logic-level alignment between candidates, eliminating the syntactic bias of surface-form metrics, (2) semantic routing that directs different claim types to appropriate verification strategies—symbolic solvers for logical claims and LLM ensembles for commonsense reasoning, and (3) precise logical error localization via Minimal Correction Subsets (MCS), which pinpoint the exact subset of claims to revise.\n\n## Authors and Publication\n\nThe paper was authored by Vikash Singh, Darion Cassel, Nathaniel Weir, Nick Feng, and Sam Bayless, submitted on January 27, 2026 with a revised version on May 2, 2026.\n\nThe paper addresses the challenge of ensuring logical correctness in Large Language Models, particularly in high-stakes applications where provable guarantees are essential."
    ],
    "durationSeconds": 7.1602661070000035,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e3e10827-548d-43e6-a0f8-454db55b00bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-27T12:26:13.506Z_

<details><summary>↩ Tool result · `toolu_019TfcD5KHvpMUBiTrSwRRB2`</summary>

```text
Web search results for query: "Goedel-Prover-V2 paper arxiv 2026"

Links: [{"title":"Goedel-Prover: the self improving super human AI mathematician | by Anatol Wegner | Apr, 2026 | Medium","url":"https://medium.com/@AIchats/goedel-prover-the-self-improving-super-human-ai-mathematician-fb03a004dc8b"},{"title":"[2508.03613v1] Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction","url":"https://arxiv.org/abs/2508.03613v1"},{"title":"[2508.03613] Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction","url":"https://arxiv.org/abs/2508.03613"},{"title":"Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction | OpenReview","url":"https://openreview.net/forum?id=j4C0nALrgK"},{"title":"[2604.08388] Awakening the Sleeping Agent: Lean-Specific Agentic Data Reactivates General Tool Use in Goedel Prover","url":"https://arxiv.org/abs/2604.08388"},{"title":"Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction - Paper Detail","url":"https://deeplearn.org/arxiv/626596/goedel-prover-v2:-scaling-formal-theorem-proving-with-scaffolded-data-synthesis-and-self-correction"},{"title":"Technical Report GOEDEL-PROVER-V2: SCALING FORMAL THEOREM","url":"https://arxiv.org/pdf/2508.03613"},{"title":"Paper page - Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction","url":"https://huggingface.co/papers/2508.03613"},{"title":"Goedel-Code-Prover: Hierarchical Proof Search for Open State-of-the-Art Code Verification","url":"https://arxiv.org/html/2603.19329v1"}]

Based on the search results, I found information about the Goedel-Prover-V2 paper on arXiv:

## Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction

Goedel-Prover-V2 is a series of open-source language models that set a new state-of-the-art in automated theorem proving.

**Key Innovations:**
The approach incorporates three key innovations: (1) Scaffolded data synthesis: generating synthetic tasks of increasing difficulty; (2) Verifier-guided self-correction: enabling the model to iteratively revise its proofs by leveraging feedback from the Lean compiler; (3) Model averaging: merging model checkpoints to mitigate the decrease in model output diversity in later stages of training.

**Performance:**
The small model, Goedel-Prover-V2-8B, reaches 84.6% pass@32 on MiniF2F and outperforms DeepSeek-Prover-V2-671B under the same metric, despite being 80X smaller. The flagship model, Goedel-Prover-V2-32B, achieves 88.1% on MiniF2F at pass@32 in standard mode and 90.4% in self-correction mode, outperforming prior SOTA by a large margin.

**Paper Details:**
The paper is available on arXiv as [2508.03613](https://arxiv.org/abs/2508.03613) and was published on January 26, 2026, with the last modification on April 11, 2026 as an ICLR 2026 Poster.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad9477ec-fc48-4eda-8338-0dba4e9663dc",
  "isSidechain": false,
  "promptId": "6c520205-97f1-438f-ab6f-f4fa04854d77",
  "type": "user",
  "uuid": "29e118b6-13eb-47e3-b050-7b6272d1d09d",
  "toolUseResult": {
    "query": "Goedel-Prover-V2 paper arxiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MXP5MU9xTd1V6Rrun5PsQa",
        "content": [
          {
            "title": "Goedel-Prover: the self improving super human AI mathematician | by Anatol Wegner | Apr, 2026 | Medium",
            "url": "https://medium.com/@AIchats/goedel-prover-the-self-improving-super-human-ai-mathematician-fb03a004dc8b"
          },
          {
            "title": "[2508.03613v1] Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction",
            "url": "https://arxiv.org/abs/2508.03613v1"
          },
          {
            "title": "[2508.03613] Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction",
            "url": "https://arxiv.org/abs/2508.03613"
          },
          {
            "title": "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction | OpenReview",
            "url": "https://openreview.net/forum?id=j4C0nALrgK"
          },
          {
            "title": "[2604.08388] Awakening the Sleeping Agent: Lean-Specific Agentic Data Reactivates General Tool Use in Goedel Prover",
            "url": "https://arxiv.org/abs/2604.08388"
          },
          {
            "title": "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction - Paper Detail",
            "url": "https://deeplearn.org/arxiv/626596/goedel-prover-v2:-scaling-formal-theorem-proving-with-scaffolded-data-synthesis-and-self-correction"
          },
          {
            "title": "Technical Report GOEDEL-PROVER-V2: SCALING FORMAL THEOREM",
            "url": "https://arxiv.org/pdf/2508.03613"
          },
          {
            "title": "Paper page - Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction",
            "url": "https://huggingface.co/papers/2508.03613"
          },
          {
            "title": "Goedel-Code-Prover: Hierarchical Proof Search for Open State-of-the-Art Code Verification",
            "url": "https://arxiv.org/html/2603.19329v1"
          }
        ]
      },
      "Based on the search results, I found information about the Goedel-Prover-V2 paper on arXiv:\n\n## Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction\n\nGoedel-Prover-V2 is a series of open-source language models that set a new state-of-the-art in automated theorem proving.\n\n**Key Innovations:**\nThe approach incorporates three key innovations: (1) Scaffolded data synthesis: generating synthetic tasks of increasing difficulty; (2) Verifier-guided self-correction: enabling the model to iteratively revise its proofs by leveraging feedback from the Lean compiler; (3) Model averaging: merging model checkpoints to mitigate the decrease in model output diversity in later stages of training.\n\n**Performance:**\nThe small model, Goedel-Prover-V2-8B, reaches 84.6% pass@32 on MiniF2F and outperforms DeepSeek-Prover-V2-671B under the same metric, despite being 80X smaller. The flagship model, Goedel-Prover-V2-32B, achieves 88.1% on MiniF2F at pass@32 in standard mode and 90.4% in self-correction mode, outperforming prior SOTA by a large margin.\n\n**Paper Details:**\nThe paper is available on arXiv as [2508.03613](https://arxiv.org/abs/2508.03613) and was published on January 26, 2026, with the last modification on April 11, 2026 as an ICLR 2026 Poster."
    ],
    "durationSeconds": 8.307262921000016,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ad9477ec-fc48-4eda-8338-0dba4e9663dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-27T12:26:24.576Z_

<details><summary>Logged reasoning block</summary>

```text
Good, now I have verified:
1. ICLR 2027: Deadlines not yet announced (expected ~October 2026 based on patterns)
2. Goedel-Prover-V2: arXiv:2508.03613, ICLR 2026 Poster. 88.1% MiniF2F pass@32.
3. VERGE: arXiv:2601.20055, confirmed real.

Let me do a couple more searches for HERMES and the Uncertainty Heads paper, and also check NeurIPS 2026 Workshops deadline.


I should verify the HERMES paper exists and double-check a few other details I want to confirm.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29e118b6-13eb-47e3-b050-7b6272d1d09d",
  "isSidechain": false,
  "requestId": "req_011CbT54HqfK4GYP9tbw7Dn1",
  "type": "assistant",
  "uuid": "19d357b8-d51e-4dd0-99d9-c3184a94ab1f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhYvoDpRmdWTKL7eZWfEz3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 6973,
      "cache_read_input_tokens": 34443,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 902,
          "output_tokens": 360,
          "cache_read_input_tokens": 34443,
          "cache_creation_input_tokens": 6973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6973
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

_source line 60 · 2026-05-27T12:26:24.815Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WUZE1FDfAggZs9iesUa5kC`</summary>

```json
{
  "query": "HERMES efficient verifiable mathematical reasoning LLMs arxiv 2511.18760 ICML 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19d357b8-d51e-4dd0-99d9-c3184a94ab1f",
  "isSidechain": false,
  "requestId": "req_011CbT54HqfK4GYP9tbw7Dn1",
  "type": "assistant",
  "uuid": "e8389fdc-bbb4-450d-990b-dd70988481d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhYvoDpRmdWTKL7eZWfEz3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 6973,
      "cache_read_input_tokens": 34443,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 902,
          "output_tokens": 360,
          "cache_read_input_tokens": 34443,
          "cache_creation_input_tokens": 6973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6973
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

_source line 61 · 2026-05-27T12:26:25.322Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MGRHamympMneEhgncBaz27`</summary>

```json
{
  "query": "NeurIPS 2026 workshop proposals deadline submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8389fdc-bbb4-450d-990b-dd70988481d5",
  "isSidechain": false,
  "requestId": "req_011CbT54HqfK4GYP9tbw7Dn1",
  "type": "assistant",
  "uuid": "f8d5b90c-ee63-4441-8fe4-cbabfa30a2ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhYvoDpRmdWTKL7eZWfEz3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 6973,
      "cache_read_input_tokens": 34443,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 902,
          "output_tokens": 360,
          "cache_read_input_tokens": 34443,
          "cache_creation_input_tokens": 6973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6973
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

_source line 62 · 2026-05-27T12:26:25.586Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015mUvzysTQxLb1vdam8Kqmp`</summary>

```json
{
  "query": "\"Uncertainty Heads\" reasoning verification arxiv 2511.06209"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8d5b90c-ee63-4441-8fe4-cbabfa30a2ea",
  "isSidechain": false,
  "requestId": "req_011CbT54HqfK4GYP9tbw7Dn1",
  "type": "assistant",
  "uuid": "8e48b1b1-54e9-4fbe-b809-08189ff5e868",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhYvoDpRmdWTKL7eZWfEz3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 6973,
      "cache_read_input_tokens": 34443,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 902,
          "output_tokens": 360,
          "cache_read_input_tokens": 34443,
          "cache_creation_input_tokens": 6973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6973
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

_source line 63 · 2026-05-27T12:26:31.127Z_

<details><summary>↩ Tool result · `toolu_01MGRHamympMneEhgncBaz27`</summary>

```text
Web search results for query: "NeurIPS 2026 workshop proposals deadline submission"

Links: [{"title":"NeurIPS 2026 Call for Workshops","url":"https://neurips.cc/Conferences/2026/CallForWorkshops"},{"title":"Guidance for NeurIPS Workshop Proposals 2026","url":"https://neurips.cc/Conferences/2026/WorkshopsGuidance"},{"title":"NeurIPS 2026 Call For Competitions","url":"https://neurips.cc/Conferences/2026/CallForCompetitions"},{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"NeurIPS Newsletter – April 2026 – NeurIPS Blog","url":"https://blog.neurips.cc/2026/04/22/neurips-newsletter-april-2026/"},{"title":"Workshops","url":"https://neurips.cc/FAQ/Workshops-Submissions"}]

Based on the search results, here's the information about NeurIPS 2026 workshop proposals:

## Important Dates for Workshop Submissions

Workshop Application Open: April 21, 2026, AoE
Workshop Application Deadline: June 06, 2026, AoE
Workshop Acceptance Notification: July 11, 2026, AoE

## Additional Key Deadlines

Suggested Submission Date for Workshop Contributions: August 29, 2026, AoE
Mandatory Accept/Reject Notification Date: September 29, 2026, AoE

## Submission Details

Proposals should be submitted through an application using the OpenReview system at https://openreview.net/group?id=NeurIPS.cc/2026/Workshop_Proposals

Submissions for workshop organization should be no more than three pages of proposal, plus no more than two pages of organizer information, and unlimited references.

## Important Constraints

This year's limits include no more than 8 organizers per proposal and no more than 2 proposals sharing the same author.

Opening a new Open Review account can take two weeks or more, so it's recommended to set this up early if needed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8d5b90c-ee63-4441-8fe4-cbabfa30a2ea",
  "isSidechain": false,
  "promptId": "6c520205-97f1-438f-ab6f-f4fa04854d77",
  "type": "user",
  "uuid": "f5dd6b91-5414-4c51-b7f4-9c637f6659aa",
  "toolUseResult": {
    "query": "NeurIPS 2026 workshop proposals deadline submission",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CcGqV3QKEr3chEpznejQQm",
        "content": [
          {
            "title": "NeurIPS 2026 Call for Workshops",
            "url": "https://neurips.cc/Conferences/2026/CallForWorkshops"
          },
          {
            "title": "Guidance for NeurIPS Workshop Proposals 2026",
            "url": "https://neurips.cc/Conferences/2026/WorkshopsGuidance"
          },
          {
            "title": "NeurIPS 2026 Call For Competitions",
            "url": "https://neurips.cc/Conferences/2026/CallForCompetitions"
          },
          {
            "title": "2026 Dates and Deadlines",
            "url": "https://neurips.cc/Conferences/2026/Dates"
          },
          {
            "title": "Call for Papers 2026",
            "url": "https://neurips.cc/Conferences/2026/CallForPapers"
          },
          {
            "title": "NeurIPS 2026",
            "url": "https://neurips.cc/"
          },
          {
            "title": "2026 Conference – NeurIPS Blog",
            "url": "https://blog.neurips.cc/category/2026-conference/"
          },
          {
            "title": "NeurIPS Newsletter – April 2026 – NeurIPS Blog",
            "url": "https://blog.neurips.cc/2026/04/22/neurips-newsletter-april-2026/"
          },
          {
            "title": "Workshops",
            "url": "https://neurips.cc/FAQ/Workshops-Submissions"
          }
        ]
      },
      "Based on the search results, here's the information about NeurIPS 2026 workshop proposals:\n\n## Important Dates for Workshop Submissions\n\nWorkshop Application Open: April 21, 2026, AoE\nWorkshop Application Deadline: June 06, 2026, AoE\nWorkshop Acceptance Notification: July 11, 2026, AoE\n\n## Additional Key Deadlines\n\nSuggested Submission Date for Workshop Contributions: August 29, 2026, AoE\nMandatory Accept/Reject Notification Date: September 29, 2026, AoE\n\n## Submission Details\n\nProposals should be submitted through an application using the OpenReview system at https://openreview.net/group?id=NeurIPS.cc/2026/Workshop_Proposals\n\nSubmissions for workshop organization should be no more than three pages of proposal, plus no more than two pages of organizer information, and unlimited references.\n\n## Important Constraints\n\nThis year's limits include no more than 8 organizers per proposal and no more than 2 proposals sharing the same author.\n\nOpening a new Open Review account can take two weeks or more, so it's recommended to set this up early if needed."
    ],
    "durationSeconds": 5.801702667999896,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f8d5b90c-ee63-4441-8fe4-cbabfa30a2ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-27T12:26:31.353Z_

<details><summary>↩ Tool result · `toolu_015mUvzysTQxLb1vdam8Kqmp`</summary>

```text
Web search results for query: ""Uncertainty Heads" reasoning verification arxiv 2511.06209"

Links: [{"title":"Paper page - Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads","url":"https://huggingface.co/papers/2511.06209"},{"title":"Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads | OpenReview","url":"https://openreview.net/forum?id=svQuvBYaCA"},{"title":"(PDF) Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads","url":"https://www.researchgate.net/publication/397480546_Reasoning_with_Confidence_Efficient_Verification_of_LLM_Reasoning_Steps_via_Uncertainty_Heads"},{"title":"Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads","url":"https://arxiv.org/html/2511.06209v2"},{"title":"efficient verification of llm reasoning steps","url":"https://arxiv.org/pdf/2511.06209"},{"title":"Uncertainty-Aware Step-wise Verification with Generative Reward Models","url":"https://arxiv.org/pdf/2502.11250"},{"title":"[2511.06209] Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models","url":"https://arxiv.org/abs/2511.06209"}]

Based on the search results, here's what I found about arxiv 2511.06209:

## Paper Overview

The paper "Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads" uses transformer-based uncertainty quantification heads to improve step-level reasoning verification in LLMs by estimating uncertainty from internal states.

## Key Contribution

The researchers train transformer-based uncertainty quantification heads (UHeads) that use the internal states of a frozen LLM to estimate the uncertainty of its reasoning steps during generation, with target labels generated either by another larger LLM (e.g., DeepSeek R1) or in a self-supervised manner by the original model itself.

## Problem it Addresses

Existing verification approaches such as Process Reward Models (PRMs) are computationally expensive, limited to specific domains, or require large-scale human or model-generated annotations. The paper proposes a lightweight alternative for step-level reasoning verification based on data-driven uncertainty scores.

## Key Finding

The findings suggest that the internal states of LLMs encode their confidence in reasoning processes and can serve as reliable signals for reasoning step verification.

The paper was submitted in November 2025 and is under review for ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e48b1b1-54e9-4fbe-b809-08189ff5e868",
  "isSidechain": false,
  "promptId": "6c520205-97f1-438f-ab6f-f4fa04854d77",
  "type": "user",
  "uuid": "1c6778c1-2e4e-41cd-add4-d5448f1dd651",
  "toolUseResult": {
    "query": "\"Uncertainty Heads\" reasoning verification arxiv 2511.06209",
    "results": [
      {
        "tool_use_id": "srvtoolu_01W5HcYdaXPmZ4tFQyvhu9CS",
        "content": [
          {
            "title": "Paper page - Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads",
            "url": "https://huggingface.co/papers/2511.06209"
          },
          {
            "title": "Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads | OpenReview",
            "url": "https://openreview.net/forum?id=svQuvBYaCA"
          },
          {
            "title": "(PDF) Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads",
            "url": "https://www.researchgate.net/publication/397480546_Reasoning_with_Confidence_Efficient_Verification_of_LLM_Reasoning_Steps_via_Uncertainty_Heads"
          },
          {
            "title": "Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads",
            "url": "https://arxiv.org/html/2511.06209v2"
          },
          {
            "title": "efficient verification of llm reasoning steps",
            "url": "https://arxiv.org/pdf/2511.06209"
          },
          {
            "title": "Uncertainty-Aware Step-wise Verification with Generative Reward Models",
            "url": "https://arxiv.org/pdf/2502.11250"
          },
          {
            "title": "[2511.06209] Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models",
            "url": "https://arxiv.org/abs/2511.06209"
          }
        ]
      },
      "Based on the search results, here's what I found about arxiv 2511.06209:\n\n## Paper Overview\n\nThe paper \"Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads\" uses transformer-based uncertainty quantification heads to improve step-level reasoning verification in LLMs by estimating uncertainty from internal states.\n\n## Key Contribution\n\nThe researchers train transformer-based uncertainty quantification heads (UHeads) that use the internal states of a frozen LLM to estimate the uncertainty of its reasoning steps during generation, with target labels generated either by another larger LLM (e.g., DeepSeek R1) or in a self-supervised manner by the original model itself.\n\n## Problem it Addresses\n\nExisting verification approaches such as Process Reward Models (PRMs) are computationally expensive, limited to specific domains, or require large-scale human or model-generated annotations. The paper proposes a lightweight alternative for step-level reasoning verification based on data-driven uncertainty scores.\n\n## Key Finding\n\nThe findings suggest that the internal states of LLMs encode their confidence in reasoning processes and can serve as reliable signals for reasoning step verification.\n\nThe paper was submitted in November 2025 and is under review for ICLR 2026."
    ],
    "durationSeconds": 5.764769014000078,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8e48b1b1-54e9-4fbe-b809-08189ff5e868",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 65_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Uncertainty-Guided Selec…",
  "leafUuid": "1c6778c1-2e4e-41cd-add4-d5448f1dd651",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective proof block formalization",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Tool result

_source line 67 · 2026-05-27T12:26:32.453Z_

<details><summary>↩ Tool result · `toolu_01WUZE1FDfAggZs9iesUa5kC`</summary>

```text
Web search results for query: "HERMES efficient verifiable mathematical reasoning LLMs arxiv 2511.18760 ICML 2026"

Links: [{"title":"[2511.18760] HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/abs/2511.18760"},{"title":"[2511.18760v1] HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/abs/2511.18760v1"},{"title":"Hermes: Verified Math Reasoning for LLMs - YouTube","url":"https://www.youtube.com/watch?v=LHbloXgSd-c"},{"title":"ICML Poster HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://icml.cc/virtual/2026/poster/60844"},{"title":"HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/pdf/2511.18760"},{"title":"(PDF) HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://www.researchgate.net/publication/397933683_HERMES_Towards_Efficient_and_Verifiable_Mathematical_Reasoning_in_LLMs"},{"title":"Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads","url":"https://arxiv.org/html/2511.06209v1"}]

Based on the search results, here's information about HERMES:

## HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs

HERMES is the first tool-assisted agent that explicitly interleaves informal reasoning with formally verified proof steps in Lean.

### Key Features

The framework performs intermediate formal checking to prevent reasoning drift and employs a memory module that maintains proof continuity across long, multi-step reasoning chains, enabling both exploration and verification within a single workflow.

### Problem It Addresses

Informal mathematics offers flexibility and efficient argument construction, but is prone to logical gaps and subtle errors that are difficult to detect. Formal theorem proving provides rigorous, verifiable mathematical reasoning, but lacks the exploratory freedom of informal problem solving.

### Performance

The framework was evaluated on four challenging mathematical reasoning benchmarks using LLMs of varying parameter scales, and reliably improves the reasoning accuracy of base models while substantially reducing token usage and computational cost compared to reward-based approaches.

### Publication Details

The paper (arxiv 2511.18760) was submitted on November 24, 2025, with authors including Azim Ospanov, Zijin Feng, Jiacheng Sun, Haoli Bai, Xin Shen, and Farzan Farnia. The work has been presented at ICML 2026 as a poster.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8389fdc-bbb4-450d-990b-dd70988481d5",
  "isSidechain": false,
  "promptId": "6c520205-97f1-438f-ab6f-f4fa04854d77",
  "type": "user",
  "uuid": "f94099c6-c48c-4aa3-8101-82314ceadf9d",
  "toolUseResult": {
    "query": "HERMES efficient verifiable mathematical reasoning LLMs arxiv 2511.18760 ICML 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014V2eRt9uwYCv5LBo3jz6a8",
        "content": [
          {
            "title": "[2511.18760] HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs",
            "url": "https://arxiv.org/abs/2511.18760"
          },
          {
            "title": "[2511.18760v1] HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs",
            "url": "https://arxiv.org/abs/2511.18760v1"
          },
          {
            "title": "Hermes: Verified Math Reasoning for LLMs - YouTube",
            "url": "https://www.youtube.com/watch?v=LHbloXgSd-c"
          },
          {
            "title": "ICML Poster HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs",
            "url": "https://icml.cc/virtual/2026/poster/60844"
          },
          {
            "title": "HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs",
            "url": "https://arxiv.org/pdf/2511.18760"
          },
          {
            "title": "(PDF) HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs",
            "url": "https://www.researchgate.net/publication/397933683_HERMES_Towards_Efficient_and_Verifiable_Mathematical_Reasoning_in_LLMs"
          },
          {
            "title": "Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads",
            "url": "https://arxiv.org/html/2511.06209v1"
          }
        ]
      },
      "Based on the search results, here's information about HERMES:\n\n## HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs\n\nHERMES is the first tool-assisted agent that explicitly interleaves informal reasoning with formally verified proof steps in Lean.\n\n### Key Features\n\nThe framework performs intermediate formal checking to prevent reasoning drift and employs a memory module that maintains proof continuity across long, multi-step reasoning chains, enabling both exploration and verification within a single workflow.\n\n### Problem It Addresses\n\nInformal mathematics offers flexibility and efficient argument construction, but is prone to logical gaps and subtle errors that are difficult to detect. Formal theorem proving provides rigorous, verifiable mathematical reasoning, but lacks the exploratory freedom of informal problem solving.\n\n### Performance\n\nThe framework was evaluated on four challenging mathematical reasoning benchmarks using LLMs of varying parameter scales, and reliably improves the reasoning accuracy of base models while substantially reducing token usage and computational cost compared to reward-based approaches.\n\n### Publication Details\n\nThe paper (arxiv 2511.18760) was submitted on November 24, 2025, with authors including Azim Ospanov, Zijin Feng, Jiacheng Sun, Haoli Bai, Xin Shen, and Farzan Farnia. The work has been presented at ICML 2026 as a poster."
    ],
    "durationSeconds": 7.636381944999914,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e8389fdc-bbb4-450d-990b-dd70988481d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-27T12:28:16.383Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compose the final JSON output.

Key findings consolidated:

**References verified:**
1. Barkallah et al. "Pseudo-Formalization" (arXiv 2026) ✓
2. Liu et al. "Safe" (ACL 2025) ✓
3. Pandit et al. "Hard2Verify" (arXiv 2025) ✓ - NOT Zheng et al.
4. "miniF2F-Lean Revisited" (NeurIPS 2025) ✓


5. Ganguly et al. "Grammars of Formal Uncertainty" (NeurIPS 2025) ✓ - NOT Bhatt et al.
6. Qu "Adaptive Test-Time Compute" (arXiv 2026) ✓ - NOT Mu et al.
7. VERGE (arXiv 2026) ✓
8. HERMES (ICML 2026) ✓
9. Uncertainty Heads (arXiv 2025, under review ICLR 2026) ✓
10. Goedel-Prover-V2 (ICLR 2026) ✓
11. StepFun-F

I need to drop the duplicate citations where I mistakenly attributed papers to Bhatt, Mu, and Zheng when they're actually by Ganguly, Qu, and Pandit respectively. I'm also noting the upcoming conference deadlines that fall after my knowledge cutoff, particularly AAAI 2027 and ICLR 2027, along with the current state-of-the-art models as of May 2026, with StepFun-Formalizer-32B leading in autoformalization tasks.

There's also a cluster of concurrent work I should acknowledge in the landscape—VERGE, HERMES, ProofSketcher, and UCCI all represent different approaches to hybrid verification that emerged between January and May 2026. Now I'm moving into the approach section where I'll describe a two-tier verification pipeline built on top of Pseudo-Formalization.

The core idea is to decompose proofs into PF blocks with explicit structure, then use QwQ-32B with calibrated uncertainty scoring to identify which blocks need formal verification. I'm extracting confidence through ensemble disagreement and token-level entropy, calibrated via isotonic regression on ArxivMathGradingBench. Blocks below a cost-optimized threshold get autoformalized to Lean 4 using StepFun-Formalizer-32B—the explicit premises and conclusions from each PF block give the autoformalization much better structure than raw natural language—then verified with Goedel-Prover-V2-32B. I'll evaluate this on ArxivMathGradingBench to measure error detection rates. is that PF blocks' self-contained structure makes them far more amenable to reliable autoformalization than raw natural language, achieving substantially higher success rates than whole-proof approaches. While concurrent work like VERGE and HERMES explores formal-informal routing, neither leverages PF's modularity or uncertainty-guided selectivity for mathematical proofs. I'm targeting near-formal-verification reliability at roughly 1.5-2x cost overhead compared to Safe's 4-8x for universal formalization, evaluated across ArxivMathGradingBench and miniF2F.

Now I'm estimating the resource requirements—GPU hours for calibration training, StepFun-Formalizer inference and fine-tuning, Goedel-Prover proof search, and baseline experiments.

For manual work without AI assistance, I'm looking at 300-400 GPU hours over 12-16 weeks with 2-3 researchers, costing around $900-1200. With Claude helping on coding and analysis, I can reduce that to 250-350 GPU hours over 8-11 weeks for $750-1050 in GPU costs plus $200-400 in API expenses. If Claude drives most of the implementation, the GPU hours stay similar at 300-400 since compute is compute, but the timeline compresses to 5-7 weeks with $500-900 in API costs—though the real bottleneck is that Lean 4 proof search runs sequentially, taking minutes per block.

I'm targeting AAAI 2027 and EACL 2027 with deadlines in July and August 2026. The work sits at a "solid" level—it's a novel combination with strong existing components that fills a real gap, even though the individual techniques aren't new.

Now I need to finalize the JSON with all existing fields plus the new ones, and update the landscape section to mention VERGE and HERMES as concurrent work.

Writing complete JSON... but imposes 4-8x cost overhead by verifying ALL steps uniformly. No prior work has exploited PF's self-contained modular structure as a bridge to targeted autoformalization: each PF block's explicit claim statement and premises are far closer to a formal theorem statement than raw NL text, potentially making block-level autoformalization significantly more reliable than whole-proof autoformalization. By using Block Verification confidence as a triage signal, we can route only the 10-20% most uncertain blocks to formal verification, catching errors that LLM verification misses while avoiding the prohibitive cost of universal formalization.

Looking at the empirical landscape, the current approaches show a stark tradeoff: LLM verification is fast but drops dramatically on harder problems (78.3% down to 37.3%), while Safe achieves ~80% success through full Lean 4 formalization at massive computational cost. End-to-end autoformalization pipelines struggle because the individual components—autoformalization accuracy around 66% and theorem proving success at ~70%—compound poorly across the pipeline, bottoming out around 35% overall. Uncertainty-guided selective verification in related work has demonstrated significant error reduction with minimal abstention, suggesting that targeted formalization could bridge this gap. Ganguly et al., NeurIPS 2025) and adaptive verification allocation achieves 44% fewer verifier calls with higher accuracy on MATH (Qu, arXiv 2026), but neither has been applied to the NL proof verification domain with pseudo-formal structure as the intermediary. Concurrent work update (May 2026): VERGE (Singh et al., arXiv 2026) implements semantic routing between SMT solvers and LLM-ensemble verification for general reasoning but targets first-order logic claims rather than mathematical proof blocks; HERMES (Ospanov et al., ICML 2026) interleaves informal reasoning with Lean 4 formal verification steps but applies uniform formalization without uncertainty-guided selectivity; UCCI (arXiv 2026) provides calibrated uncertainty for cost-optimal LLM cascade routing but operates on model cascades rather than formal/informal verification tiers. None of these systems leverage the modular block structure of pseudo-formal proofs as an autoformalization target or combine uncertainty-guided routing with pseudo-formal decomposition for mathematical proof verification.

The key gap is that existing approaches either use LLM verification alone despite having formal-like structure, or apply formal verification uniformly without selectivity. Adaptive compute allocation across verification tiers has proven effective elsewhere, but the untried combination is using pseudo-formal blocks—with their explicit premises and conclusions—as autoformalization targets paired with uncertainty-guided routing between LLM and formal verification.

I'm building a two-tier verification pipeline on top of Pseudo-Formalization... Looking at the resource estimates across different execution modes—manual annotation requires the most GPU hours and timeline, while the auto-research approach is faster but hits a bottleneck with Lean 4's sequential proof search, and I'm also factoring in the comparative baselines including HERMES and various ablation studies on threshold selection and uncertainty calibration. Continuing through the key references on formal verification and LLM reasoning...

The core idea here is a two-tier verification system that uses uncertainty scoring to decide which proof blocks need formal verification versus which can be trusted through LLM checking alone. By leveraging the modular structure of pseudo-formalized proofs, we can selectively formalize only the most uncertain blocks to Lean 4, dramatically improving success rates compared to trying to formalize entire proofs at once. I'm verifying all the citations in this project description against their sources — checking arXiv IDs and conference venues to make sure everything is accurate and properly attributed. I've corrected the attributions for those earlier citations—Bhatt et al., Mu et al., and Zheng et al. are now properly mapped to Ganguly et al., Qu, and Pandit et al. respectively. I'm skipping the StepFun-Formalizer paper since it appears to be just a model release without a formal publication. I also want to verify the autoformalization metrics one more time—the miniF2F-Lean Revisited paper shows 97% for LLM-judged results but only 66% for human-judged, with the end-to-end pipeline at 34.8%, which I've already incorporated into the landscape. Now I'm ready to finalize the JSON output. I'm verifying the arxiv ID timing for Goedel-Prover-V2 — the 2508 prefix indicates an August 2025 submission, though the January 2026 publication date likely reflects the camera-ready version for ICLR 2026. The paper checks out, so I'm ready to finalize the output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f94099c6-c48c-4aa3-8101-82314ceadf9d",
  "isSidechain": false,
  "requestId": "req_011CbT55gqoCPoH488XQKh1s",
  "type": "assistant",
  "uuid": "c670a479-5ece-4edd-89c4-fe3b527f67da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018jKgsTYoeTf9MqYGLgNk2m",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1347,
      "cache_creation_input_tokens": 2001,
      "cache_read_input_tokens": 41416,
      "output_tokens": 7669,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1347,
          "output_tokens": 7669,
          "cache_read_input_tokens": 41416,
          "cache_creation_input_tokens": 2001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2001
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

_source line 69 · 2026-05-27T12:28:36.708Z_

All four research agents have completed. Let me now compose the final consolidated JSON output.

{
  "title": "Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition",
  "core_problem": "How can we achieve near-formal-verification reliability for natural language mathematical proof checking while keeping cost tractable, by selectively routing only the most uncertain proof blocks to formal verification?",
  "opportunity": "Pseudo-Formalization (Barkallah et al., May 2026) introduced modular proof blocks with explicit premises, conclusions, and dependencies — but verifies them only via LLM, missing ~50% of research-level errors. Safe (Liu et al., ACL 2025) achieves step-level formal verification at 80% proof success but imposes 4-8x cost overhead by verifying ALL steps uniformly. No prior work has exploited PF's self-contained modular structure as a bridge to targeted autoformalization: each PF block's explicit claim statement and premises are far closer to a formal theorem statement than raw NL text, potentially making block-level autoformalization significantly more reliable than whole-proof autoformalization. By using Block Verification confidence as a triage signal, we can route only the 10-20% most uncertain blocks to formal verification, catching errors that LLM verification misses while avoiding the prohibitive cost of universal formalization.",
  "landscape": "Current proof verification spans a cost-reliability spectrum with no effective middle ground: LLM-as-judge is cheap but unreliable (best PRM drops from 78.3% to 37.3% on Hard2Verify; Barkallah et al., 2026; Pandit et al., 2025); PF+Block Verification Pareto-dominates LLM-as-judge on olympiad and research-level benchmarks but still leaves ~50% of errors undetected on ArxivMathGradingBench (Barkallah et al., 2026); Safe verifies each step in Lean 4 with ~80% success but costs 4-8x more compute per step than process reward models (Liu et al., ACL 2025); end-to-end autoformalization pipelines achieve only ~35% success because autoformalization accuracy (66% human-judged, not the 97% reported under LLM-judging) and theorem proving success (~70%) compound poorly across the full pipeline (miniF2F-Lean Revisited, NeurIPS 2025). Adjacent work on uncertainty-guided selective verification has shown 14-100% error reduction with minimal abstention in SMT-based formalization (Ganguly et al., NeurIPS 2025) and adaptive verification allocation achieves 44% fewer verifier calls with higher accuracy on MATH (Qu, arXiv 2026), but neither has been applied to the NL proof verification domain with pseudo-formal structure as the intermediary. Concurrent work update (May 2026): VERGE (Singh et al., arXiv 2026) implements semantic routing between SMT solvers and LLM-ensemble soft verification for general reasoning claims but targets first-order logic rather than mathematical proof blocks and does not exploit modular proof structure; HERMES (Ospanov et al., ICML 2026) is the first agent to interleave informal reasoning with formally verified Lean 4 proof steps, achieving 67% accuracy improvement with 80% fewer FLOPs, but applies uniform formalization without uncertainty-guided selectivity; UCCI (arXiv 2026) provides calibrated uncertainty for cost-optimal LLM cascade routing but operates on model cascades rather than formal/informal verification tiers; ProofSketcher (arXiv 2026) produces typed proof sketches with trusted kernel expansion but without uncertainty-guided routing. None of these concurrent systems exploit PF's modular block structure as autoformalization targets nor combine uncertainty-guided routing with pseudo-formal decomposition for mathematical proof verification.",
  "inspired_by": "Gap: PF (May 2026) only uses LLM verification despite its formal-like modular structure; Safe (ACL 2025) applies formal verification uniformly without selectivity. Pattern: Adaptive compute allocation across verification tiers (Qu, arXiv 2026; Ganguly et al., NeurIPS 2025) has proven effective but has not been applied to the informal-formal proof verification spectrum. Untried combination: PF's self-contained blocks (explicit premises + conclusions) as autoformalization targets + uncertainty-guided routing between LLM and formal verification.",
  "approach": "We build a two-tier verification pipeline atop Pseudo-Formalization (Barkallah et al., 2026): given a mathematical proof, we decompose it into PF blocks with explicit premises, conclusions, and dependency graphs, then run LLM-based Block Verification using QwQ-32B augmented with calibrated uncertainty scoring via ensemble disagreement (N=5 stochastic forward passes with temperature sampling) and token-level CoT entropy, calibrated via isotonic regression on held-out ArxivMathGradingBench annotations. Blocks below a cost-optimized confidence threshold (targeting the bottom 10-20% by uncertainty) are autoformalized to Lean 4 using StepFun-Formalizer-32B — leveraging each PF block's explicit premises and conclusion as structured autoformalization targets for substantially higher translation fidelity than raw NL text — then formally verified via Goedel-Prover-V2-32B proof search with verifier-guided self-correction. We evaluate on ArxivMathGradingBench (error detection recall vs. verification cost), miniF2F (end-to-end correctness), and compare against PF+BV-only, Safe (universal formalization), PRM baselines, and HERMES, with ablations on threshold selection, uncertainty calibration method, and the autoformalization advantage of PF blocks over raw NL.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "300-400 (uncertainty calibration ~50h, StepFun-Formalizer inference/adaptation ~80h, Goedel-Prover-V2 proof search ~100h, baselines and ablations ~70-100h; all on A100-80GB)",
      "timeline": "12-16 weeks (2-3 researchers)",
      "estimated_gpu_cost": "$900-1200"
    },
    "human_in_loop": {
      "gpu_hours": "250-350 (better experiment planning reduces wasted runs)",
      "timeline": "8-11 weeks",
      "claude_api_cost": "$200-400",
      "estimated_gpu_cost": "$750-1050"
    },
    "auto_research": {
      "gpu_hours": "300-400 (compute-bound tasks unchanged)",
      "timeline": "5-7 weeks",
      "claude_api_cost": "$500-900",
      "estimated_gpu_cost": "$900-1200",
      "speed_bottleneck": "Lean 4 proof search is inherently sequential (~2-5 min per block via Goedel-Prover-V2); formal verification throughput cannot be parallelized across dependent proof blocks, and Lean kernel type-checking is CPU-bound"
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract: July 21, 2026; full paper: July 28, 2026)",
    "EACL 2027 (ARR submission: August 3, 2026)"
  ],
  "level": "solid",
  "key_references": [
    "Pseudo-Formalization for Automatic Proof Verification (arXiv 2026)",
    "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (ACL 2025)",
    "Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (arXiv 2025)",
    "miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward (NeurIPS 2025)",
    "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (NeurIPS 2025)",
    "Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (arXiv 2026)",
    "VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv 2026)",
    "HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (ICML 2026)",
    "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (ICLR 2026)",
    "Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads (arXiv 2025)"
  ],
  "description": "We propose Uncertainty-Guided Selective Formal Verification, a two-tier proof verification pipeline that bridges the cost-reliability gap between cheap LLM-based verification and expensive universal formal verification of mathematical proofs. Building on Pseudo-Formalization's modular proof blocks — each with explicit premises, conclusions, and inter-block dependencies — we add calibrated uncertainty scoring to Block Verification using ensemble disagreement and CoT entropy. Blocks exceeding a learned confidence threshold are accepted via LLM verification alone; the remaining 10-20% most uncertain blocks are autoformalized to Lean 4 using StepFun-Formalizer-32B and formally verified via Goedel-Prover-V2-32B proof search. A key insight is that PF blocks' self-contained structure makes them far more amenable to reliable autoformalization than raw natural language text, enabling block-level formal verification success rates substantially higher than whole-proof autoformalization (which achieves only ~35% end-to-end on miniF2F). Concurrent work VERGE and HERMES explore formal-informal integration but neither exploits PF's modular structure nor uses uncertainty-guided selectivity for mathematical proof verification. We target near-formal reliability at ~1.5-2x cost overhead versus Safe's 4-8x for universal formalization.",
  "project_name": "unc_guided_pf_verify",
  "source": "web_research"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c670a479-5ece-4edd-89c4-fe3b527f67da",
  "isSidechain": false,
  "requestId": "req_011CbT55gqoCPoH488XQKh1s",
  "type": "assistant",
  "uuid": "40101165-002c-4938-8832-565ca548457d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018jKgsTYoeTf9MqYGLgNk2m",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1347,
      "cache_creation_input_tokens": 2001,
      "cache_read_input_tokens": 41416,
      "output_tokens": 7669,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1347,
          "output_tokens": 7669,
          "cache_read_input_tokens": 41416,
          "cache_creation_input_tokens": 2001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2001
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

_source line 70_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Uncertainty-Guided Selec…",
  "leafUuid": "40101165-002c-4938-8832-565ca548457d",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective proof block formalization",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Runtime record

_source line 72_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Uncertainty-Guided Selec…",
  "leafUuid": "40101165-002c-4938-8832-565ca548457d",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---

### Runtime record

_source line 73_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective proof block formalization",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620"
}
```

---
