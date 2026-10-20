# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T111643 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/ca99f461-2386-45ba-9b4d-04158cd2e830.jsonl`
- **Structured JSON:** [`95fa98303f23ae0bb36f.json`](../../sessions/95/95fa98303f23ae0bb36f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T11:34:44.405Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T11:34:44.405Z",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T111643 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：SOPBench强复制（Δ≥25pp，rule-based verifier独立确认），审稿人认可model×type交互为genuinely novel contribution。论文定位为4-domain（retail/airline/healthcare/banking）跨基准因果研究，C1因果claim以matched-pair+perturbation+cross-benchmark三重证据链支撑，为agent safety文献最强因果推断。C4 model×type interaction（52pp auth_scope range）连接B&K到alignment，incompleteness universally dangerous作为safety training blind spot。投稿时main text加cross-benchmark summary paragraph，appendix放完整SOPBench结果。expected_review_avg 3.75，claims_surviving_without_revision 5/5。\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T11:34:44.408Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T11:34:44.408Z",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830"
}
```

---

## Round 1

45 recorded events

### User

_source line 3 · 2026-05-22T11:34:44.428Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T111643 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：SOPBench强复制（Δ≥25pp，rule-based verifier独立确认），审稿人认可model×type交互为genuinely novel contribution。论文定位为4-domain（retail/airline/healthcare/banking）跨基准因果研究，C1因果claim以matched-pair+perturbation+cross-benchmark三重证据链支撑，为agent safety文献最强因果推断。C4 model×type interaction（52pp auth_scope range）连接B&K到alignment，incompleteness universally dangerous作为safety training blind spot。投稿时main text加cross-benchmark summary paragraph，appendix放完整SOPBench结果。expected_review_avg 3.75，claims_surviving_without_revision 5/5。
- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d65c2e8d-79bc-4128-97c7-582868b89531",
  "type": "user",
  "uuid": "548a8af1-5e45-4853-baf3-0a18a92c3258",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T11:34:44.427Z_

```json
{
  "parentUuid": "548a8af1-5e45-4853-baf3-0a18a92c3258",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "e251c672-5fb9-4771-a25c-3d56bb6d859c",
  "timestamp": "2026-05-22T11:34:44.427Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T11:34:44.427Z_

```json
{
  "parentUuid": "e251c672-5fb9-4771-a25c-3d56bb6d859c",
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
  "uuid": "41fe5991-a352-4dbc-994a-199a746e20a5",
  "timestamp": "2026-05-22T11:34:44.427Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T11:34:44.427Z_

```json
{
  "parentUuid": "41fe5991-a352-4dbc-994a-199a746e20a5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c309fc94-2f68-4dc6-8014-066f0ec12a58",
  "timestamp": "2026-05-22T11:34:44.427Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for policy ambiguity safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830"
}
```

---

### Assistant

_source line 8 · 2026-05-22T11:34:48.074Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c309fc94-2f68-4dc6-8014-066f0ec12a58",
  "isSidechain": false,
  "requestId": "req_011CbHY61P7un7pztkQvPGyk",
  "type": "assistant",
  "uuid": "2a48a9e5-d7a2-4183-a125-b61132e03e31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKpeFLBf3UZDvEX3u6WR76",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12794,
      "cache_read_input_tokens": 11447,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12794
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

_source line 9 · 2026-05-22T11:34:48.796Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PkQCC8udtKjSaAsrnWDX8g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a48a9e5-d7a2-4183-a125-b61132e03e31",
  "isSidechain": false,
  "requestId": "req_011CbHY61P7un7pztkQvPGyk",
  "type": "assistant",
  "uuid": "c1c9062e-d967-4be0-8fc3-1c1f0e4811e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKpeFLBf3UZDvEX3u6WR76",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12794,
      "cache_read_input_tokens": 11447,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12794
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

_source line 10 · 2026-05-22T11:34:49.056Z_

<details open><summary>🔧 Tool call — Read · `toolu_011aAvVT33MLVcCQb2dpC1zu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1c9062e-d967-4be0-8fc3-1c1f0e4811e1",
  "isSidechain": false,
  "requestId": "req_011CbHY61P7un7pztkQvPGyk",
  "type": "assistant",
  "uuid": "fd898afb-216c-4575-ae1c-c54cfc9120e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKpeFLBf3UZDvEX3u6WR76",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12794,
      "cache_read_input_tokens": 11447,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12794
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

_source line 11 · 2026-05-22T11:34:49.078Z_

<details><summary>↩ Tool result · `toolu_01PkQCC8udtKjSaAsrnWDX8g`</summary>

```text
1	[
2	  {
3	    "name": "full_study_clause_generation",
4	    "description": "生成300条clause pairs（50/type × 6 types），涵盖coreferential（50 new）、authorization_scope（50 new）、lexical（+20）、incompleteness（+20）。CP混合labeled+unlabeled格式。全量Chantree-style质量验证+cross-type token delta均衡检查。",
5	    "results": {
6	      "total_clauses": 300,
7	      "clauses_per_type": 50,
8	      "chantree_quality_pass_rate": 0.98,
9	      "mean_token_delta_spec_layer": 34.2,
10	      "mean_token_delta_ling_layer": 11.6,
11	      "token_delta_within_type_cv": 0.18,
12	      "cross_type_balance_chi2_p": 0.72,
13	      "cp_labeled_ratio": 0.4,
14	      "cp_unlabeled_ratio": 0.6,
15	      "flesch_kincaid_mean": 11.8,
16	      "flesch_kincaid_sd": 2.1,
17	      "domain_split_retail": 150,
18	      "domain_split_airline": 150
19	    },
20	    "tables": [
21	      {
22	        "title": "Clause Distribution by Type × Domain",
23	        "columns": [
24	          "Type",
25	          "Layer",
26	          "Retail",
27	          "Airline",
28	          "Total",
29	          "Mean Token Delta"
30	        ],
31	        "rows": [
32	          [
33	            "authorization_scope",
34	            "Specification",
35	            "25",
36	            "25",
37	            "50",
38	            "36.1"
39	          ],
40	          [
41	            "conditional_precedence",
42	            "Specification",
43	            "25",
44	            "25",
45	            "50",
46	            "28.4"
47	          ],
48	          [
49	            "incompleteness",
50	            "Specification",
51	            "25",
52	            "25",
53	            "50",
54	            "34.6"
55	          ],
56	          [
57	            "scopal",
58	            "Linguistic",
59	            "25",
60	            "25",
61	            "50",
62	            "14.2"
63	          ],
64	          [
65	            "lexical",
66	            "Linguistic",
67	            "25",
68	            "25",
69	            "50",
70	            "12.8"
71	          ],
72	          [
73	            "coreferential",
74	            "Linguistic",
75	            "25",
76	            "25",
77	            "50",
78	            "7.8"
79	          ]
80	        ]
81	      }
82	    ],
83	    "figures": [],
84	    "analysis": "300 clauses质量均达到EMNLP出版标准。token delta的层级差异（spec >> ling）不是confound而是substantive finding——直接映射到Disambiguation Channel Framework中'外部消歧通道可用性'的概念。CP混合格式避免了'artificial conflict presentation'的reviewer concern。Chantree-style pass rate 98%意味着≤6条需minor修订，无系统性质量问题。\n\nbest档下clause generation利用已有pilot（10 clauses/type经MVP和diag验证）+ DRIP-R cross-walk作为template anchor。98%通过Chantree-style validation因为迭代优化了edge cases（e.g., coreferential RC attachment的pragmatic naturalness，auth_scope permission boundary的domain plausibility）。token delta的type-level差异（spec 34.2 vs ling 11.6）反映了真实的disambiguation complexity差异——spec-layer需要更多token来消除歧义因为涉及domain knowledge（auth boundaries, missing conditions），这本身是Disambiguation Channel Framework的经验支撑。CV=0.18表明within-type变异控制良好。CP混合格式（40% labeled / 60% unlabeled）遵循Reviewer建议以提高ecological validity。"
85	  },
86	  {
87	    "name": "new_type_mini_pilot",
88	    "description": "Coreferential + authorization_scope小规模验证：5 clauses/type × 2 conditions × 1 model（gpt-5.4）= 20 episodes。验证新类型clause设计的基本有效性。",
89	    "results": {
90	      "total_episodes": 20,
91	      "auth_scope_amb_violation_rate": 0.6,
92	      "auth_scope_unamb_violation_rate": 0.0,
93	      "auth_scope_delta_pp": 60,
94	      "coreferential_amb_violation_rate": 0.2,
95	      "coreferential_unamb_violation_rate": 0.0,
96	      "coreferential_delta_pp": 20,
97	      "systematic_issues_found": 0,
98	      "proceed_to_full_study": true
99	    },
100	    "tables": [
101	      {
102	        "title": "Mini-Pilot Results (gpt-5.4)",
103	        "columns": [
104	          "Type",
105	          "N",
106	          "Amb Rate",
107	          "Unamb Rate",
108	          "Delta (pp)",
109	          "Issues"
110	        ],
111	        "rows": [
112	          [
113	            "authorization_scope",
114	            "10",
115	            "60%",
116	            "0%",
117	            "+60",
118	            "None"
119	          ],
120	          [
121	            "coreferential",
122	            "10",
123	            "20%",
124	            "0%",
125	            "+20",
126	            "None"
127	          ]
128	        ]
129	      }
130	    ],
131	    "figures": [],
132	    "analysis": "两类型均通过基本有效性检验：ambiguous condition产生violations而unambiguous control clean。auth_scope的高violation rate预示了它在C4中作为model-differentiating type的角色。coreferential的较低rate预示了其作为boundary case的特性（partial disambiguation via tool responses）。N=5太小无法做统计推断，但signal清晰且无red flags，可安全进入full study。\n\nbest档下两个新类型均表现出清晰的ambiguity效应。auth_scope在gpt-5.4上高达60%（与后续full study的64%一致），因为gpt-5.4对authorization boundary特别脆弱——其action-oriented training倾向于'assume permission and proceed'。coreferential较低（20%）因为gpt-5.4部分通过tool response获得referential disambiguation。unamb均为0%因为N=5×1时control condition大概率全clean。无systematic issues意味着clause设计无需返工，pipeline直接进full study。"
133	  },
134	  {
135	    "name": "full_study_api",
136	    "description": "300 clauses × 2 conditions × 3 API models（gpt-5.4, gpt-4.1, claude-sonnet-4-6）= 1,800 episodes。Cross-judge evaluation（互评：gpt-4.1评gpt-5.4，gpt-5.4评gpt-4.1和Claude）。",
137	    "results": {
138	      "total_episodes": 1800,
139	      "gpt54_amb_rate": 0.41,
140	      "gpt54_unamb_rate": 0.027,
141	      "gpt54_delta_pp": 38.3,
142	      "gpt54_mcnemar_p": 1e-28,
143	      "gpt41_amb_rate": 0.407,
144	      "gpt41_unamb_rate": 0.06,
145	      "gpt41_delta_pp": 34.7,
146	      "gpt41_mcnemar_p": 1e-24,
147	      "claude_amb_rate": 0.303,
148	      "claude_unamb_rate": 0.047,
149	      "claude_delta_pp": 25.7,
150	      "claude_mcnemar_p": 1e-17,
151	      "pooled_amb_rate": 0.373,
152	      "pooled_unamb_rate": 0.044,
153	      "pooled_delta_pp": 32.9,
154	      "pooled_or": 13.2,
155	      "cross_judge_kappa": 0.74
156	    },
157	    "tables": [
158	      {
159	        "title": "API Model Binary Effect (C1)",
160	        "columns": [
161	          "Model",
162	          "Amb Rate",
163	          "Unamb Rate",
164	          "Delta (pp)",
165	          "OR",
166	          "95% CI",
167	          "McNemar p"
168	        ],
169	        "rows": [
170	          [
171	            "gpt-5.4",
172	            "41.0%",
173	            "2.7%",
174	            "+38.3",
175	            "25.3",
176	            "[14.8, 43.2]",
177	            "<1e-28"
178	          ],
179	          [
180	            "gpt-4.1",
181	            "40.7%",
182	            "6.0%",
183	            "+34.7",
184	            "10.9",
185	            "[7.1, 16.6]",
186	            "<1e-24"
187	          ],
188	          [
189	            "claude-sonnet-4-6",
190	            "30.3%",
191	            "4.7%",
192	            "+25.7",
193	            "8.9",
194	            "[5.5, 14.5]",
195	            "<1e-17"
196	          ],
197	          [
198	            "Pooled (3 API)",
199	            "37.3%",
200	            "4.4%",
201	            "+32.9",
202	            "13.2",
203	            "[9.8, 17.7]",
204	            "<1e-50"
205	          ]
206	        ]
207	      },
208	      {
209	        "title": "API Model × Type Interaction (Amb Condition Violation Rates)",
210	        "columns": [
211	          "Type",
212	          "gpt-5.4",
213	          "gpt-4.1",
214	          "Claude",
215	          "Range (pp)"
216	        ],
217	        "rows": [
218	          [
219	            "authorization_scope",
220	            "64%",
221	            "46%",
222	            "12%",
223	            "52"
224	          ],
225	          [
226	            "incompleteness",
227	            "46%",
228	            "58%",
229	            "48%",
230	            "12"
231	          ],
232	          [
233	            "lexical",
234	            "42%",
235	            "34%",
236	            "32%",
237	            "10"
238	          ],
239	          [
240	            "scopal",
241	            "42%",
242	            "38%",
243	            "32%",
244	            "10"
245	          ],
246	          [
247	            "conditional_precedence",
248	            "34%",
249	            "36%",
250	            "36%",
251	            "2"
252	          ],
253	          [
254	            "coreferential",
255	            "18%",
256	            "32%",
257	            "22%",
258	            "14"
259	          ]
260	        ]
261	      }
262	    ],
263	    "figures": [],
264	    "analysis": "3 API模型完整确认C1（binary effect universal across architectures）和C4（model×type interaction）。关键发现：auth_scope 52pp range是整个interaction矩阵的最大值，直接指向safety training selectivity。Claude的auth_scope robustness（12%）是其最distinctive特征，暗示Anthropic RLHF中authorization boundary handling被explicitly addressed。gpt-5.4的highest overall rate但lowest coreferential（18%）暗示不同failure mechanism——frontier model在referential ambiguity上能部分self-resolve但在permission boundaries上over-confident。\n\nbest档下3个API模型全部展示massive binary effect。gpt-5.4最高（+38.3pp）因为frontier model的action-orientation最强——更倾向于'confident execution'而非'pause and ask'。Claude最低（+25.7pp）因为Anthropic的RLHF显式训练了authorization boundary awareness和conservative behavior。gpt-4.1居中（+34.7pp）作为mid-tier模型在capability和safety之间平衡。unamb baseline均<6%表明control condition clean——matched-pair设计成功隔离了ambiguity effect。cross-judge κ=0.74（substantial agreement）表明judge评估可靠。这些结果与plan_010 perturbation control（Δ_perturb=3.33pp）对比形成causal inference gold standard。"
265	  },
266	  {
267	    "name": "full_study_opensource",
268	    "description": "300 clauses × 2 conditions × 2 open-source models via OpenRouter（qwen3-235b-a22b, deepseek-chat-v3-0324）= 1,200 episodes。与plan_002并行运行。",
269	    "results": {
270	      "total_episodes": 1200,
271	      "qwen3_amb_rate": 0.431,
272	      "qwen3_unamb_rate": 0.107,
273	      "qwen3_delta_pp": 32.4,
274	      "qwen3_mcnemar_p": 1e-19,
275	      "deepseek_amb_rate": 0.497,
276	      "deepseek_unamb_rate": 0.107,
277	      "deepseek_delta_pp": 39.0,
278	      "deepseek_mcnemar_p": 1e-25,
279	      "qwen3_type_chi2_p": 0.007,
280	      "qwen3_type_V": 0.23,
281	      "deepseek_type_chi2_p": 0.277,
282	      "deepseek_type_V": 0.14
283	    },
284	    "tables": [
285	      {
286	        "title": "Open-Source Model Binary Effect (C1)",
287	        "columns": [
288	          "Model",
289	          "Architecture",
290	          "Amb Rate",
291	          "Unamb Rate",
292	          "Delta (pp)",
293	          "OR",
294	          "McNemar p"
295	        ],
296	        "rows": [
297	          [
298	            "Qwen3-235B",
299	            "MoE (22B active)",
300	            "43.1%",
301	            "10.7%",
302	            "+32.4",
303	            "6.4",
304	            "<1e-19"
305	          ],
306	          [
307	            "DeepSeek-V3",
308	            "MoE (37B active)",
309	            "49.7%",
310	            "10.7%",
311	            "+39.0",
312	            "8.3",
313	            "<1e-25"
314	          ]
315	        ]
316	      },
317	      {
318	        "title": "Open-Source Model × Type Violation Rates (Amb Condition)",
319	        "columns": [
320	          "Type",
321	          "Qwen3",
322	          "DeepSeek",
323	          "Range (pp)"
324	        ],
325	        "rows": [
326	          [
327	            "authorization_scope",
328	            "26%",
329	            "60%",
330	            "34"
331	          ],
332	          [
333	            "incompleteness",
334	            "62%",
335	            "54%",
336	            "8"
337	          ],
338	          [
339	            "lexical",
340	            "52%",
341	            "54%",
342	            "2"
343	          ],
344	          [
345	            "scopal",
346	            "37%",
347	            "48%",
348	            "11"
349	          ],
350	          [
351	            "conditional_precedence",
352	            "40%",
353	            "38%",
354	            "2"
355	          ],
356	          [
357	            "coreferential",
358	            "42%",
359	            "44%",
360	            "2"
361	          ]
362	        ]
363	      }
364	    ],
365	    "figures": [],
366	    "analysis": "Open-source模型data完成后5-model矩阵齐全。DeepSeek的uniform vulnerability（type χ² p=0.277, NOT significant）是C4的关键对照——当safety training不够type-specific时，所有ambiguity types equally dangerous。Qwen3的moderate differentiation（p=0.007）介于DeepSeek（undifferentiated）和GPT-5.4/Claude（highly differentiated）之间。5-model spectrum从Claude（lowest, most differentiated）到DeepSeek（highest, least differentiated）形成完美narrative gradient，支撑'safety training selectivity'的核心theoretical claim。\n\nbest档下open-source模型均replicate C1 binary effect。DeepSeek最高vulnerability（49.7%）且type differentiation不显著（V=0.14, p=0.277），因为其safety training较less type-specific——uniformly high across all types暗示safety guardrails未针对特定ambiguity pattern调优。Qwen3居中（43.1%）但显示moderate type differentiation（V=0.23, p=0.007），特别是high incompleteness+lexical与low auth_scope的组合模式。unamb baseline较高（10.7%）反映了open-source模型in general less calibrated的baseline safety——但这使得delta effect更conservative（实际ambiguity-specific impact可能更大）。这些结果对C4至关重要：提供了dense vs MoE architecture comparison和proprietary vs open-source safety training comparison。"
367	  },
368	  {
369	    "name": "full_study_analysis",
370	    "description": "2,997 episodes全量统计分析：C1 binary effect、C2 type hierarchy（omnibus + pairwise + TOST）、C3 layer effect + within-judge check、C4 model×type interaction + logistic regression。含power analysis、MDE报告、inter-model agreement、info delta mediator分析。",
371	    "results": {
372	      "total_episodes": 2997,
373	      "c1_pooled_delta_pp": 34.0,
374	      "c1_pooled_or": 15.1,
375	      "c1_or_ci": "[10.78, 21.17]",
376	      "c1_bootstrap_ci": "[31.2, 36.9]",
377	      "c1_mcnemar_p": 1e-100,
378	      "c1_logistic_condition_coef": 2.278,
379	      "c1_logistic_condition_z": 19.65,
380	      "c2_omnibus_chi2": 28.02,
381	      "c2_omnibus_p": 3.6e-05,
382	      "c2_V": 0.137,
383	      "c2_power": 0.993,
384	      "c2_MDE": 0.093,
385	      "c2_tost_15pp_equivalent_pairs": "8/15",
386	      "c2_tost_10pp_equivalent_pairs": "4/15",
387	      "c3_layer_delta_pp": 6.08,
388	      "c3_layer_p": 0.017,
389	      "c3_layer_V": 0.062,
390	      "c3_within_judge_gpt41_judged_p": 0.059,
391	      "c3_within_judge_gpt54_judged_p": 0.157,
392	      "c4_model_chi2": 31.02,
393	      "c4_model_p": 3e-06,
394	      "c4_model_V": 0.102,
395	      "c4_amb_only_chi2": 24.01,
396	      "c4_amb_only_p": 7.9e-05,
397	      "c4_fleiss_kappa": 0.384,
398	      "c4_auth_scope_range_pp": 52,
399	      "c4_incomp_range_pp": 16,
400	      "info_delta_logistic_coef": 0.022,
401	      "info_delta_logistic_z": 3.49,
402	      "info_delta_logistic_p": 0.0005,
403	      "inter_model_systematic_nocuity_rate": 0.27
404	    },
405	    "tables": [
406	      {
407	        "title": "C1 Binary Effect Summary (5 Models Pooled)",
408	        "columns": [
409	          "Metric",
410	          "Value",
411	          "95% CI"
412	        ],
413	        "rows": [
414	          [
415	            "Delta (pp)",
416	            "+34.0",
417	            "[31.2, 36.9]"
418	          ],
419	          [
420	            "Odds Ratio",
421	            "15.1",
422	            "[10.78, 21.17]"
423	          ],
424	          [
425	            "McNemar p",
426	            "<1e-100",
427	            "—"
428	          ],
429	          [
430	            "Logistic coef (condition_amb)",
431	            "2.278",
432	            "z=19.65, p<0.001"
433	          ],
434	          [
435	            "N models replicating",
436	            "5/5",
437	            "all p<1e-17"
438	          ]
439	        ]
440	      },
441	      {
442	        "title": "C2 Type Hierarchy (3-Tier Structure)",
443	        "columns": [
444	          "Tier",
445	          "Types",
446	          "Violation Rate Range",
447	          "Key Property"
448	        ],
449	        "rows": [
450	          [
451	            "High",
452	            "incompleteness",
453	            "53.6%",
454	            "Universally dangerous across all models"
455	          ],
456	          [
457	            "Mid",
458	            "lexical, auth_scope, scopal, CP",
459	            "36.8%–42.8%",
460	            "Pairwise equivalent at ±15pp"
461	          ],
462	          [
463	            "Low",
464	            "coreferential",
465	            "31.6%",
466	            "Partial disambiguation via tool responses"
467	          ]
468	        ]
469	      },
470	      {
471	        "title": "C4 Model × Type Interaction Matrix (Amb Violation Rates)",
472	        "columns": [
473	          "Type",
474	          "GPT-5.4",
475	          "GPT-4.1",
476	          "Claude",
477	          "Qwen3",
478	          "DeepSeek",
479	          "Range"
480	        ],
481	        "rows": [
482	          [
483	            "auth_scope",
484	            "64%",
485	            "46%",
486	            "12%",
487	            "26%",
488	            "60%",
489	            "52pp"
490	          ],
491	          [
492	            "incompleteness",
493	            "46%",
494	            "58%",
495	            "48%",
496	            "62%",
497	            "54%",
498	            "16pp"
499	          ],
500	          [
501	            "lexical",
502	            "42%",
503	            "34%",
504	            "32%",
505	            "52%",
506	            "54%",
507	            "22pp"
508	          ],
509	          [
510	            "scopal",
511	            "42%",
512	            "38%",
513	            "32%",
514	            "37%",
515	            "48%",
516	            "16pp"
517	          ],
518	          [
519	            "cond_prec",
520	            "34%",
521	            "36%",
522	            "36%",
523	            "40%",
524	            "38%",
525	            "6pp"
526	          ],
527	          [
528	            "coreferential",
529	            "18%",
530	            "32%",
531	            "22%",
532	            "42%",
533	            "44%",
534	            "26pp"
535	          ]
536	        ]
537	      },
538	      {
539	        "title": "C2 TOST Equivalence Analysis",
540	        "columns": [
541	          "Margin",
542	          "Equivalent Pairs",
543	          "Non-Equivalent Pairs",
544	          "Interpretation"
545	        ],
546	        "rows": [
547	          [
548	            "±15pp",
549	            "8/15",
550	            "7/15",
551	            "Types NOT interchangeable"
552	          ],
553	          [
554	            "±10pp",
555	            "4/15",
556	            "11/15",
557	            "Strong type differentiation"
558	          ]
559	        ]
560	      },
561	      {
562	        "title": "C3 Layer Effect (Aggregate + Within-Judge)",
563	        "columns": [
564	          "Analysis",
565	          "Spec Rate",
566	          "Ling Rate",
567	          "Delta (pp)",
568	          "p-value",
569	          "Status"
570	        ],
571	        "rows": [
572	          [
573	            "5-model aggregate",
574	            "44.0%",
575	            "37.9%",
576	            "+6.08",
577	            "0.017",
578	            "Significant"
579	          ],
580	          [
581	            "Within-judge (gpt-4.1 judged)",
582	            "—",
583	            "—",
584	            "+8.0",
585	            "0.059",
586	            "Marginal"
587	          ],
588	          [
589	            "Within-judge (gpt-5.4 judged)",
590	            "—",
591	            "—",
592	            "+4.8",
593	            "0.157",
594	            "Not significant"
595	          ]
596	        ]
597	      },
598	      {
599	        "title": "Per-Model Layer Gap (C3 feeds C4)",
600	        "columns": [
601	          "Model",
602	          "Spec Rate",
603	          "Ling Rate",
604	          "Layer Gap (pp)",
605	          "Primary Driver"
606	        ],
607	        "rows": [
608	          [
609	            "GPT-5.4",
610	            "48.0%",
611	            "34.0%",
612	            "+14.0",
613	            "auth_scope 64%"
614	          ],
615	          [
616	            "GPT-4.1",
617	            "46.7%",
618	            "34.7%",
619	            "+12.0",
620	            "auth_scope 46%"
621	          ],
622	          [
623	            "Claude",
624	            "32.0%",
625	            "28.7%",
626	            "+3.3",
627	            "auth_scope only 12%"
628	          ],
629	          [
630	            "DeepSeek",
631	            "50.7%",
632	            "48.7%",
633	            "+2.0",
634	            "Uniformly high"
635	          ],
636	          [
637	            "Qwen3",
638	            "42.7%",
639	            "43.6%",
640	            "-0.9",
641	            "auth_scope only 26%"
642	          ]
643	        ]
644	      },
645	      {
646	        "title": "Per-Model Type χ² (C4 Differentiation)",
647	        "columns": [
648	          "Model",
649	          "Type χ²",
650	          "p-value",
651	          "V",
652	          "Pattern"
653	        ],
654	        "rows": [
655	          [
656	            "GPT-5.4",
657	            "23.44",
658	            "0.0003",
659	            "0.28",
660	            "Very high auth_scope, very low coref"
661	          ],
662	          [
663	            "Claude",
664	            "17.87",
665	            "0.003",
666	            "0.24",
667	            "Very low auth_scope, moderate others"
668	          ],
669	          [
670	            "Qwen3",
671	            "15.89",
672	            "0.007",
673	            "0.23",
674	            "High incomp+lex, low auth_scope"
675	          ],
676	          [
677	            "GPT-4.1",
678	            "9.89",
679	            "0.078",
680	            "0.18",
681	            "Borderline differentiation"
682	          ],
683	          [
684	            "DeepSeek",
685	            "6.31",
686	            "0.277",
687	            "0.14",
688	            "Uniformly high — NOT significant"
689	          ]
690	        ]
691	      }
692	    ],
693	    "figures": [],
694	    "analysis": "统计分析完整确认所有5个claims在best档下的强度排序：C1（最强，triple causal evidence）> C4（star finding，52pp interaction）> C2（well-powered small effect）> C5（qualitative depth）> C3（suggestive, honestly reported fragility）。关键methodological贡献：(a) power=0.993下接受V=0.137为'real but small'是sophisticated统计论证，(b) TOST双margin分析显示types genuinely non-equivalent，(c) within-judge fragility透明报告建立credibility。审稿人最可能challenge C3 fragility——但best档下这被C4的model×type interaction absorb：layer effect is itself model-dependent, making the interaction the more fundamental finding。systematic nocuity rate 27%是unexpected finding，提出B&K third category作为Discussion贡献。\n\nbest档下所有统计分析产出与paper_framing完全一致的强结果。C1以OR=15.1（CI不含1）成为agent safety文献最强因果证据——matched-pair + perturbation control + 5-model replication的三重支撑无可挑战。C2的V=0.137虽small但power=0.993（MDE=0.093远小于observed V），审稿人接受'effect real but small, 3-tier structure captures heterogeneity better than single V'的论证——这比声称large effect更honest且更sophisticated。C3 within-judge fragility在best档下被审稿人视为'honest reporting'而非fatal flaw，因为(a)aggregate p=0.017仍significant，(b)paper明确将C3降级为'suggestive'并在Limitations披露，(c)C4 model×type interaction提供了更fundamental的explanation（layer effect is itself model-dependent）。C4的52pp auth_scope range是整篇论文的star statistic——连接B&K nocuous ambiguity theory到modern alignment research的桥梁。Fleiss κ=0.384（fair）quantifies inter-model disagreement on WHICH clauses trigger violations，支撑Differential Nocuity框架。systematic nocuity rate 27%发现所有模型converge on same WRONG interpretation——提出B&K extension。"
695	  },
696	  {
697	    "name": "error_analysis",
698	    "description": "从full study中采样violation traces进行qualitative failure mode分析：每type 50条traces × 6 types = 300 total（across 5 models × 2 domains）。分类failure modes，建立type-specific signatures，验证Ambiguity Blindness，对比cross-model consistency。",
699	    "results": {
700	      "total_traces_coded": 300,
701	      "failure_modes_identified": 4,
702	      "type_diagnostic_accuracy": 0.83,
703	      "ambiguity_awareness_rate": 0.046,
704	      "surface_adoption_rate": 0.89,
705	      "escalate_to_user_rate": 0.008,
706	      "cross_model_dominant_mode_agreement": "5/6",
707	      "cross_domain_max_delta_pp": 13,
708	      "coreferential_conservative_refusal_rate": 0.085,
709	      "inter_coder_agreement": 0.8,
710	      "inter_coder_kappa_4cat": 0.594,
711	      "gwet_ac1": 0.73
712	    },
713	    "tables": [
714	      {
715	        "title": "Type-Specific Failure Mode Signatures",
716	        "columns": [
717	          "Type",
718	          "Dominant Mode",
719	          "Rate (5-model)",
720	          "Secondary Mode",
721	          "Rate",
722	          "Layer Pattern"
723	        ],
724	        "rows": [
725	          [
726	            "auth_scope",
727	            "unauthorized_escalation",
728	            "75%",
729	            "inappropriate_action",
730	            "18%",
731	            "Spec: guess-and-act"
732	          ],
733	          [
734	            "incompleteness",
735	            "assumption_based_action",
736	            "63%",
737	            "unauthorized_escalation",
738	            "22%",
739	            "Spec: guess-and-act"
740	          ],
741	          [
742	            "scopal",
743	            "scope_misapplication",
744	            "75%",
745	            "assumption_based_action",
746	            "15%",
747	            "Ling: misparse"
748	          ],
749	          [
750	            "lexical",
751	            "assumption_based_action",
752	            "62%",
753	            "scope_misapplication",
754	            "20%",
755	            "Ling: misparse-hybrid"
756	          ],
757	          [
758	            "cond_prec",
759	            "scope_misapplication",
760	            "35%",
761	            "arbitrary_rule_selection",
762	            "29%",
763	            "Spec: mixed"
764	          ],
765	          [
766	            "coreferential",
767	            "scope_misapplication",
768	            "38%",
769	            "assumption_based_action",
770	            "33%",
771	            "Ling: flat distribution"
772	          ]
773	        ]
774	      },
775	      {
776	        "title": "Ambiguity Blindness Metrics (5 Models)",
777	        "columns": [
778	          "Metric",
779	          "GPT-5.4",
780	          "GPT-4.1",
781	          "Claude",
782	          "Qwen3",
783	          "DeepSeek",
784	          "Pooled"
785	        ],
786	        "rows": [
787	          [
788	            "Awareness rate",
789	            "4.1%",
790	            "10.7%",
791	            "5.2%",
792	            "3.8%",
793	            "2.4%",
794	            "4.6%"
795	          ],
796	          [
797	            "Surface adoption",
798	            "91%",
799	            "85%",
800	            "88%",
801	            "90%",
802	            "93%",
803	            "89%"
804	          ],
805	          [
806	            "Escalate to user",
807	            "0.8%",
808	            "1.6%",
809	            "1.2%",
810	            "0.4%",
811	            "0.2%",
812	            "0.8%"
813	          ]
814	        ]
815	      },
816	      {
817	        "title": "Inter-Coder Agreement (Automated Cross-Coding)",
818	        "columns": [
819	          "Metric",
820	          "Value",
821	          "Interpretation"
822	        ],
823	        "rows": [
824	          [
825	            "4-category agreement",
826	            "80%",
827	            "Good"
828	          ],
829	          [
830	            "Cohen's κ (4-cat)",
831	            "0.594",
832	            "Moderate (kappa paradox deflated)"
833	          ],
834	          [
835	            "Gwet's AC1 (primary)",
836	            "0.73",
837	            "Good — robust to prevalence imbalance"
838	          ],
839	          [
840	            "Types with κ paradox",
841	            "2/6",
842	            "lexical (91.7% agree, κ=0.0), scopal (100%, κ undef)"
843	          ]
844	        ]
845	      }
846	    ],
847	    "figures": [],
848	    "analysis": "Error analysis提供了C1-C4量化发现的mechanistic explanation。核心insight：spec-layer failure是'active guessing in absence of information'而ling-layer failure是'unconscious misparse of grammatical structure'——两种根本不同的cognitive（computational）机制。这映射到Disambiguation Channel Framework：ling-layer有partial external channels（tool responses可disambiguate referent, context可clarify word sense）但spec-layer没有（missing policy info无法从external source补充）。Ambiguity Blindness的model-level variation（gpt-4.1 10.7% vs DeepSeek 2.4%）暗示mid-tier models may paradoxically be more 'cautious' than frontier models——higher awareness但still act（only 1.6% escalation），构成Discussion中interesting nuance。\n\nbest档下error analysis产出clean的type-specific failure signatures——这是EMNLP reviewers最看重的qualitative depth（distilled insight: CL论文需要linguistic WHY behind quantitative WHAT）。4个failure modes（unauthorized_escalation, assumption_based_action, scope_misapplication, arbitrary_rule_selection）形成2×2矩阵映射到2 layers：spec→guess-and-act (escalation+assumption), ling→misparse-and-apply (scope_misapplication)。5/6 types cross-model dominant mode一致（仅coreferential diverge）——failure modes是type-specific而非model-specific，支撑taxonomy的construct validity。Ambiguity Blindness<5%是empirical hard evidence（非merely named concept），>88% surface adoption直接challenge了'models understand instructions'的assumption。coreferential conservative refusal 8.5%（vs avg 2-3%）解释了其作为boundary case的low violation rate。κ=0.594 deflated by kappa paradox但Gwet's AC1=0.73（good）作为primary metric。"
849	  },
850	  {
851	    "name": "reliability_test",
852	    "description": "Test-retest reliability：30 clauses（5/type）× 3 replicates × 2 conditions × 2 models（gpt-5.4, gpt-4.1）= 360 episodes。计算per-clause violation rates的ICC。",
853	    "results": {
854	      "total_episodes": 360,
855	      "icc_overall": 0.919,
856	      "icc_ci": "[0.892, 0.940]",
857	      "icc_binary": 0.847,
858	      "icc_gpt54": 0.921,
859	      "icc_gpt41": 0.918,
860	      "per_type_icc_min": 0.807,
861	      "per_type_icc_max": 0.989,
862	      "ling_layer_icc_mean": 0.982,
863	      "spec_layer_icc_mean": 0.84,
864	      "bootstrap_ci_width_key_comparisons": "<10pp"
865	    },
866	    "tables": [
867	      {
868	        "title": "ICC Results by Level and Model",
869	        "columns": [
870	          "Level",
871	          "ICC",
872	          "95% CI",
873	          "Rating"
874	        ],
875	        "rows": [
876	          [
877	            "Overall (continuous)",
878	            "0.919",
879	            "[0.892, 0.940]",
880	            "Excellent"
881	          ],
882	          [
883	            "Binary (0/1)",
884	            "0.847",
885	            "[0.804, 0.883]",
886	            "Good"
887	          ],
888	          [
889	            "gpt-5.4 only",
890	            "0.921",
891	            "[0.886, 0.948]",
892	            "Excellent"
893	          ],
894	          [
895	            "gpt-4.1 only",
896	            "0.918",
897	            "[0.882, 0.946]",
898	            "Excellent"
899	          ]
900	        ]
901	      },
902	      {
903	        "title": "Per-Type ICC (Layer Pattern)",
904	        "columns": [
905	          "Type",
906	          "Layer",
907	          "ICC",
908	          "Interpretation"
909	        ],
910	        "rows": [
911	          [
912	            "scopal",
913	            "Linguistic",
914	            "0.989",
915	            "Near-perfect reproducibility"
916	          ],
917	          [
918	            "lexical",
919	            "Linguistic",
920	            "0.981",
921	            "Near-perfect"
922	          ],
923	          [
924	            "coreferential",
925	            "Linguistic",
926	            "0.976",
927	            "Near-perfect"
928	          ],
929	          [
930	            "auth_scope",
931	            "Specification",
932	            "0.857",
933	            "Good — agents guess differently"
934	          ],
935	          [
936	            "cond_prec",
937	            "Specification",
938	            "0.856",
939	            "Good"
940	          ],
941	          [
942	            "incompleteness",
943	            "Specification",
944	            "0.807",
945	            "Good — most variable (missing info → stochastic)"
946	          ]
947	        ]
948	      }
949	    ],
950	    "figures": [],
951	    "analysis": "Reliability analysis accomplishes three goals in best档：(a) methodological validation——ICC=0.919消除sampling noise concern，(b) construct validity for Disambiguation Channel Framework——ling/spec ICC differential is independent evidence for the framework, not derivable from violation rates alone, (c) practical implication——single-run design justified for main study, 3-replicate design unnecessary for future work using this paradigm。per-type ICC pattern is itself a finding worth reporting（spec-layer less reproducible = agents guess more）。\n\nbest档下ICC=0.919（excellent）直接解决了Reviewer concern about ±8pp sampling noise。三次独立replicates产出highly reproducible per-clause violation rates——同一clause在同一model上反复运行得到几乎相同的violation probability。per-type ICC pattern（ling 0.982 > spec 0.840）提供了convergent evidence for Disambiguation Channel Framework：ling-layer更reproducible因为agents consistently resolve（or fail to resolve）linguistic ambiguity in the same way（deterministic misparse），而spec-layer less reproducible因为agents在missing info下guess differently each run（stochastic guessing）。binary ICC=0.847（good）表明even binary classification（violation/no-violation）跨replicates稳定。这使得main study的single-run design methodologically justified。"
952	  },
953	  {
954	    "name": "realism_validation",
955	    "description": "Synthetic ambiguity injection的ecological validity验证：与DRIP-R natural ambiguities比较linguistic properties（sentence length, parse depth, Flesch-Kincaid, TTR）+ KS tests。",
956	    "results": {
957	      "ks_sentence_length_p": 0.34,
958	      "ks_parse_depth_p": 0.21,
959	      "ks_flesch_kincaid_p": 0.48,
960	      "ks_ttr_p": 0.15,
961	      "all_ks_nonsignificant": true,
962	      "mean_sentence_length_ours": 22.4,
963	      "mean_sentence_length_dripr": 21.8,
964	      "mean_flesch_kincaid_ours": 11.8,
965	      "mean_flesch_kincaid_dripr": 12.3,
966	      "discriminator_accuracy": 0.56,
967	      "discriminator_accuracy_ci": "[0.48, 0.64]"
968	    },
969	    "tables": [
970	      {
971	        "title": "Linguistic Property Comparison (Ours vs DRIP-R)",
972	        "columns": [
973	          "Property",
974	          "Ours (mean±sd)",
975	          "DRIP-R (mean±sd)",
976	          "KS D",
977	          "KS p",
978	          "Significant?"
979	        ],
980	        "rows": [
981	          [
982	            "Sentence length (words)",
983	            "22.4±6.2",
984	            "21.8±7.1",
985	            "0.08",
986	            "0.34",
987	            "No"
988	          ],
989	          [
990	            "Parse depth",
991	            "5.3±1.4",
992	            "5.6±1.6",
993	            "0.11",
994	            "0.21",
995	            "No"
996	          ],
997	          [
998	            "Flesch-Kincaid grade",
999	            "11.8±2.1",
1000	            "12.3±2.4",
1001	            "0.07",
1002	            "0.48",
1003	            "No"
1004	          ],
1005	          [
1006	            "Type-token ratio",
1007	            "0.82±0.06",
1008	            "0.80±0.07",
1009	            "0.12",
1010	            "0.15",
1011	            "No"
1012	          ]
1013	        ]
1014	      }
1015	    ],
1016	    "figures": [],
1017	    "analysis": "Realism validation在best档下完全化解RC4。所有KS tests non-significant且discriminator at chance——synthetic clauses与naturally occurring policy ambiguities distributional equivalent。这支撑了matched-pair design的external validity：effect sizes measured on synthetic pairs likely generalize to natural policy ambiguities。唯一caveat是DRIP-R仅covers retail domain——但combined with SOPBench cross-domain replication（plan_017），coverage extends to 4 domains。\n\nbest档下synthetic clauses与DRIP-R natural ambiguities在所有linguistic properties上statistically indistinguishable（all KS p>0.05）。这因为clause generation遵循了policy document的register和style conventions——使用了real τ²-bench policy templates作为base并仅修改specific ambiguity-bearing elements。discriminator accuracy 56%（CI含50%）表明even a trained classifier cannot reliably distinguish synthetic from natural。这是RC4（ecological validity）的strongest possible response：our synthetic injection preserves the distributional properties of natural policy ambiguity。sentence length几乎identical（22.4 vs 21.8 words）因为minimal-edit injection strategy不改变clause structure。Flesch-Kincaid相近（11.8 vs 12.3）因为both are professional policy language at roughly the same readability level。"
1018	  },
1019	  {
1020	    "name": "judge_calibration",
1021	    "description": "LLM-as-judge calibration：100 episodes stratified by type×model×condition，2 human annotators标注，计算human-LLM agreement（precision/recall/F1）+ inter-annotator κ。",
1022	    "results": {
1023	      "n_episodes": 100,
1024	      "human_inter_annotator_kappa": 0.762,
1025	      "human_llm_pooled_kappa_weighted": 0.807,
1026	      "human_llm_binary_kappa": 0.87,
1027	      "human_llm_binary_f1": 0.92,
1028	      "human_llm_binary_precision": 0.94,
1029	      "human_llm_binary_recall": 0.9,
1030	      "per_severity_agreement_severe": 0.91,
1031	      "per_severity_agreement_moderate": 0.78,
1032	      "per_severity_agreement_none": 0.95,
1033	      "cross_judge_kappa_weighted": 0.685,
1034	      "cross_judge_exact_agreement": 0.76,
1035	      "cross_judge_binary_kappa": 0.74
1036	    },
1037	    "tables": [
1038	      {
1039	        "title": "Human-LLM Agreement (Pooled)",
1040	        "columns": [
1041	          "Metric",
1042	          "Value",
1043	          "Interpretation"
1044	        ],
1045	        "rows": [
1046	          [
1047	            "Weighted κ (3-tier)",
1048	            "0.807",
1049	            "Strong agreement"
1050	          ],
1051	          [
1052	            "Binary κ (violation/no-violation)",
1053	            "0.87",
1054	            "Strong agreement"
1055	          ],
1056	          [
1057	            "Binary F1",
1058	            "0.92",
1059	            "High accuracy"
1060	          ],
1061	          [
1062	            "Binary Precision",
1063	            "0.94",
1064	            "Very few false positives"
1065	          ],
1066	          [
1067	            "Binary Recall",
1068	            "0.90",
1069	            "10% borderline cases missed"
1070	          ],
1071	          [
1072	            "Human inter-annotator κ",
1073	            "0.762",
1074	            "Substantial (ceiling)"
1075	          ]
1076	        ]
1077	      },
1078	      {
1079	        "title": "Per-Severity Agreement Rates",
1080	        "columns": [
1081	          "Severity",
1082	          "Human-LLM Agreement",
1083	          "N",
1084	          "Main Disagreement Pattern"
1085	        ],
1086	        "rows": [
1087	          [
1088	            "Severe violation",
1089	            "91%",
1090	            "38",
1091	            "Rare: LLM sometimes downgrades to moderate"
1092	          ],
1093	          [
1094	            "Moderate violation",
1095	            "78%",
1096	            "27",
1097	            "Boundary cases with partial compliance"
1098	          ],
1099	          [
1100	            "No violation",
1101	            "95%",
1102	            "35",
1103	            "Near-perfect on clean episodes"
1104	          ]
1105	        ]
1106	      },
1107	      {
1108	        "title": "Cross-Judge Agreement (gpt-4.1 vs gpt-5.4 as judges)",
1109	        "columns": [
1110	          "Metric",
1111	          "Value",
1112	          "Note"
1113	        ],
1114	        "rows": [
1115	          [
1116	            "Exact agreement",
1117	            "76%",
1118	            "—"
1119	          ],
1120	          [
1121	            "Weighted κ",
1122	            "0.685",
1123	            "Substantial"
1124	          ],
1125	          [
1126	            "Binary κ",
1127	            "0.74",
1128	            "Substantial"
1129	          ],
1130	          [
1131	            "Bias direction",
1132	            "gpt-5.4 slightly stricter",
1133	            "Reports ~3% more violations"
1134	          ]
1135	        ]
1136	      }
1137	    ],
1138	    "figures": [],
1139	    "analysis": "Judge calibration在best档下提供了measurement validity的gold standard。κ=0.807 > human inter-annotator κ=0.762的finding本身值得报告——LLM judges can be more reliable than individual human coders for this task。这使得paper的整个quantitative infrastructure（C1-C4）站在validated foundation上。cross-judge divergence（24%）已知且quantified——paper在Method中disclose并在Limitations中discuss。per-severity pattern（severe 91% > moderate 78% > none 95%）合理：borderline cases是genuinely hard for ANY coder。dream best-tier reviewers identified这为'single most critical missing validation'——现在resolved。\n\nbest档下human-LLM κ=0.807（strong agreement）验证了整个measurement chain。binary F1=0.92意味着LLM judge在violation detection上precision 94%（很少false positive）且recall 90%（漏检率10%——这些是borderline cases where human annotators also disagree）。human inter-annotator κ=0.762设定了agreement ceiling——LLM judge的0.807 actually exceeds human baseline，因为LLM judge is more consistent（less annotator fatigue/drift）。per-severity agreement在severe tier最高（0.91）因为clear-cut violations（e.g., unauthorized refund）easy to judge；moderate tier最低（0.78）因为borderline cases（e.g., partial compliance）genuinely ambiguous even for humans。cross-judge（gpt-4.1 vs gpt-5.4作为judges）κ=0.685（substantial）显示两个LLM judges mostly agree但有meaningful divergence on ~24% episodes——paper需disclose cross-judge asymmetry in Method。"
1140	  },
1141	  {
1142	    "name": "perturbation_control",
1143	    "description": "非歧义扰动对照：30 clause pairs（15 synonym substitution + 15 clause reordering）× 2 conditions × 2+ models = 120-300 episodes。区分ambiguity-specific harm vs general prompt brittleness。",
1144	    "results": {
1145	      "total_episodes": 300,
1146	      "delta_perturb_pp": -0.67,
1147	      "delta_perturb_ci": "[-8.0, 6.67]",
1148	      "ci_upper_bound": 6.67,
1149	      "ci_width_pp": 14.67,
1150	      "mcnemar_p": 1.0,
1151	      "ambiguity_delta_pp": 34.0,
1152	      "net_delta_pp": 34.67,
1153	      "ratio": 0.0,
1154	      "verdict": "PASS",
1155	      "synonym_delta_pp": 1.33,
1156	      "reorder_delta_pp": -2.67
1157	    },
1158	    "tables": [
1159	      {
1160	        "title": "Perturbation Control Results",
1161	        "columns": [
1162	          "Condition",
1163	          "Original Rate",
1164	          "Perturbed Rate",
1165	          "Delta (pp)",
1166	          "95% CI",
1167	          "p-value"
1168	        ],
1169	        "rows": [
1170	          [
1171	            "Synonym substitution",
1172	            "40.0%",
1173	            "41.3%",
1174	            "+1.33",
1175	            "[-10.7, 13.3]",
1176	            "1.0"
1177	          ],
1178	          [
1179	            "Clause reordering",
1180	            "42.7%",
1181	            "40.0%",
1182	            "-2.67",
1183	            "[-14.7, 9.3]",
1184	            "0.82"
1185	          ],
1186	          [
1187	            "Combined perturbation",
1188	            "41.3%",
1189	            "40.7%",
1190	            "-0.67",
1191	            "[-8.0, 6.67]",
1192	            "1.0"
1193	          ],
1194	          [
1195	            "Ambiguity (reference)",
1196	            "4.4%",
1197	            "38.4%",
1198	            "+34.0",
1199	            "[31.2, 36.9]",
1200	            "<1e-100"
1201	          ]
1202	        ]
1203	      },
1204	      {
1205	        "title": "5-Tier Verdict Assessment",
1206	        "columns": [
1207	          "Criterion",
1208	          "Threshold",
1209	          "Observed",
1210	          "Status"
1211	        ],
1212	        "rows": [
1213	          [
1214	            "Delta_perturb",
1215	            "<5pp (CI含0)",
1216	            "-0.67pp (CI含0)",
1217	            "PASS"
1218	          ],
1219	          [
1220	            "Ratio (perturb/ambiguity)",
1221	            "<0.15",
1222	            "0.0",
1223	            "PASS"
1224	          ],
1225	          [
1226	            "Net effect",
1227	            ">20pp",
1228	            "+34.67pp",
1229	            "PASS"
1230	          ],
1231	          [
1232	            "Overall verdict",
1233	            "—",
1234	            "—",
1235	            "PASS (strongest form)"
1236	          ]
1237	        ]
1238	      }
1239	    ],
1240	    "figures": [],
1241	    "analysis": "Perturbation control是C1因果claim的keystone evidence。PASS verdict使得paper可以声称'strongest causal evidence in the agent safety literature'——no prior work has both matched-pair AND perturbation control for agent policy ambiguity。ratio=0.0（perturbation effect is essentially zero）意味着all 34pp can be attributed to ambiguity。这也preempts RC11（prompt sensitivity confound）——最aggressive reviewer也难以challenge a 10:1 effect ratio with CI not overlapping。\n\nbest档下perturbation control产出PASS verdict——non-ambiguity surface changes（synonym substitution, clause reordering）cause zero meaningful effect（Δ=-0.67pp, CI含0）。这与ambiguity Δ=+34.0pp形成stark contrast：10:1 signal-to-noise ratio。PASS verdict意味着C1因果claim以最强形式成立——'+34pp是ambiguity-specific causation，不是general prompt sensitivity'。CI upper bound 6.67pp远低于WARNING阈值（15pp），net effect +34.67pp overwhelming。synonym substitution略positive（+1.33pp）和clause reordering略negative（-2.67pp）的差异在noise范围内（|Δ|<3pp），表明两种perturbation types equally benign。verdict=PASS使得paper可写'Perturbation control confirms that the observed +34pp effect is specific to ambiguity, not an artifact of surface-level policy modifications (synonym substitution: +1.33pp, clause reordering: -2.67pp, combined: -0.67pp, CI includes zero). This constitutes the strongest causal evidence for ambiguity-specific harm in the agent safety literature。'"
1242	  },
1243	  {
1244	    "name": "sopbench_cross_benchmark",
1245	    "description": "SOPBench跨基准C1复制：Healthcare + Bank domains，100 clause pairs（50/domain）× 2 conditions × 5 models = 1,000 episodes。Rule-based verifier替代LLM judge。验证C1 generalizability + C2 type ranking correlation。",
1246	    "results": {
1247	      "total_episodes": 1000,
1248	      "domains": [
1249	        "Healthcare",
1250	        "Bank"
1251	      ],
1252	      "types_covered": [
1253	        "incompleteness",
1254	        "auth_scope",
1255	        "lexical",
1256	        "conditional_precedence"
1257	      ],
1258	      "sopbench_c1_delta_pp": 31.2,
1259	      "sopbench_c1_or": 12.8,
1260	      "sopbench_c1_p": 1e-38,
1261	      "sopbench_c1_ci": "[27.0, 35.4]",
1262	      "sopbench_healthcare_delta_pp": 33.8,
1263	      "sopbench_bank_delta_pp": 28.6,
1264	      "sopbench_incompleteness_rate": 0.56,
1265	      "sopbench_auth_scope_rate": 0.42,
1266	      "sopbench_lexical_rate": 0.38,
1267	      "sopbench_cond_prec_rate": 0.33,
1268	      "sopbench_type_rank_rho": 0.8,
1269	      "sopbench_type_rank_p": 0.042,
1270	      "cross_benchmark_effect_correlation": 0.89,
1271	      "rule_based_vs_llm_agreement": 0.91,
1272	      "rule_based_verifier_advantage": "eliminates LLM-judge single dependency",
1273	      "per_model_sopbench": {
1274	        "gpt54_delta_pp": 35.4,
1275	        "gpt41_delta_pp": 31.8,
1276	        "claude_delta_pp": 22.6,
1277	        "qwen3_delta_pp": 29.0,
1278	        "deepseek_delta_pp": 37.2
1279	      },
1280	      "auth_scope_range_sopbench_pp": 48,
1281	      "incompleteness_range_sopbench_pp": 14
1282	    },
1283	    "tables": [
1284	      {
1285	        "title": "SOPBench C1 Replication Summary",
1286	        "columns": [
1287	          "Metric",
1288	          "τ²-bench (primary)",
1289	          "SOPBench (replication)",
1290	          "Agreement"
1291	        ],
1292	        "rows": [
1293	          [
1294	            "Delta (pp)",
1295	            "+34.0",
1296	            "+31.2",
1297	            "Within CI overlap"
1298	          ],
1299	          [
1300	            "Odds Ratio",
1301	            "15.1",
1302	            "12.8",
1303	            "Same order of magnitude"
1304	          ],
1305	          [
1306	            "p-value",
1307	            "<1e-100",
1308	            "<1e-38",
1309	            "Both highly significant"
1310	          ],
1311	          [
1312	            "Models replicating",
1313	            "5/5",
1314	            "5/5",
1315	            "Universal"
1316	          ],
1317	          [
1318	            "Domains",
1319	            "Retail + Airline",
1320	            "Healthcare + Bank",
1321	            "4 total (no overlap)"
1322	          ],
1323	          [
1324	            "Verifier",
1325	            "LLM judge",
1326	            "Rule-based",
1327	            "Independent methods"
1328	          ]
1329	        ]
1330	      },
1331	      {
1332	        "title": "SOPBench Per-Model Results",
1333	        "columns": [
1334	          "Model",
1335	          "Amb Rate",
1336	          "Unamb Rate",
1337	          "Delta (pp)",
1338	          "p-value",
1339	          "τ²-bench Delta"
1340	        ],
1341	        "rows": [
1342	          [
1343	            "GPT-5.4",
1344	            "43.0%",
1345	            "7.6%",
1346	            "+35.4",
1347	            "<1e-10",
1348	            "+38.3"
1349	          ],
1350	          [
1351	            "DeepSeek",
1352	            "46.0%",
1353	            "8.8%",
1354	            "+37.2",
1355	            "<1e-11",
1356	            "+39.0"
1357	          ],
1358	          [
1359	            "GPT-4.1",
1360	            "38.4%",
1361	            "6.6%",
1362	            "+31.8",
1363	            "<1e-8",
1364	            "+34.7"
1365	          ],
1366	          [
1367	            "Qwen3",
1368	            "37.0%",
1369	            "8.0%",
1370	            "+29.0",
1371	            "<1e-7",
1372	            "+32.4"
1373	          ],
1374	          [
1375	            "Claude",
1376	            "28.0%",
1377	            "5.4%",
1378	            "+22.6",
1379	            "<1e-5",
1380	            "+25.7"
1381	          ]
1382	        ]
1383	      },
1384	      {
1385	        "title": "SOPBench Type Ranking vs τ²-bench",
1386	        "columns": [
1387	          "Rank",
1388	          "τ²-bench Type",
1389	          "τ²-bench Rate",
1390	          "SOPBench Type",
1391	          "SOPBench Rate"
1392	        ],
1393	        "rows": [
1394	          [
1395	            "1",
1396	            "incompleteness",
1397	            "53.6%",
1398	            "incompleteness",
1399	            "56.0%"
1400	          ],
1401	          [
1402	            "2",
1403	            "auth_scope",
1404	            "41.6%",
1405	            "auth_scope",
1406	            "42.0%"
1407	          ],
1408	          [
1409	            "3",
1410	            "lexical",
1411	            "42.8%",
1412	            "lexical",
1413	            "38.0%"
1414	          ],
1415	          [
1416	            "4",
1417	            "cond_prec",
1418	            "36.8%",
1419	            "cond_prec",
1420	            "33.0%"
1421	          ]
1422	        ]
1423	      },
1424	      {
1425	        "title": "SOPBench Per-Domain Results",
1426	        "columns": [
1427	          "Domain",
1428	          "Amb Rate",
1429	          "Unamb Rate",
1430	          "Delta (pp)",
1431	          "N Episodes",
1432	          "Top Risk Type"
1433	        ],
1434	        "rows": [
1435	          [
1436	            "Healthcare",
1437	            "41.2%",
1438	            "7.4%",
1439	            "+33.8",
1440	            "500",
1441	            "incompleteness (61%)"
1442	          ],
1443	          [
1444	            "Bank",
1445	            "35.0%",
1446	            "6.4%",
1447	            "+28.6",
1448	            "500",
1449	            "incompleteness (51%)"
1450	          ]
1451	        ]
1452	      },
1453	      {
1454	        "title": "Cross-Benchmark Convergence Evidence",
1455	        "columns": [
1456	          "Evidence",
1457	          "Value",
1458	          "Interpretation"
1459	        ],
1460	        "rows": [
1461	          [
1462	            "Type rank ρ (Spearman)",
1463	            "0.80",
1464	            "Strong positive correlation (p=0.042)"
1465	          ],
1466	          [
1467	            "Per-model effect correlation",
1468	            "0.89",
1469	            "Very strong — same model ordering"
1470	          ],
1471	          [
1472	            "Rule-based vs LLM judge agreement",
1473	            "91%",
1474	            "Independent verifiers converge"
1475	          ],
1476	          [
1477	            "Incompleteness #1 in both?",
1478	            "Yes",
1479	            "Universal highest-risk type"
1480	          ],
1481	          [
1482	            "auth_scope range (SOPBench)",
1483	            "48pp",
1484	            "Confirms model×type interaction"
1485	          ]
1486	        ]
1487	      }
1488	    ],
1489	    "figures": [],
1490	    "analysis": "SOPBench replication是best档与median/worst档的核心区分因素。Δ=31.2pp强复制（在[25,40] range内）将paper从'customer service domain finding'升级为'cross-domain generalization across 4 sectors'。rule-based verifier独立确认消除了LLM-judge single-dependency concern（审稿人最常见的methodological objection之一）。type ranking ρ=0.80显著相关证明incompleteness的#1 position不是τ²-bench artifact。cross-benchmark effect correlation r=0.89表明per-model vulnerability patterns是stable model properties而非benchmark-specific artifacts。Healthcare delta > Bank delta的差异本身is interesting——healthcare policies have higher stakes and more complex boundary conditions，可能amplify ambiguity effects。Main text加一段'Cross-Benchmark Replication: SOPBench (Healthcare + Bank) independently confirms the binary effect (Δ=31.2pp, OR=12.8, rule-based verifier) and type hierarchy (incompleteness > auth_scope > lexical > CP, ρ=0.80 with τ²-bench ranking). Effect generalizes across 4 domains, 2 benchmarks, and 2 verification methods.'即可。\n\nbest档下SOPBench强复制C1（Δ=31.2pp, p<1e-38）——效应略低于τ²-bench的34.0pp因为(a)不同domains（Healthcare/Bank vs retail/airline）有不同的policy complexity baseline，(b)rule-based verifier比LLM judge更严格（tends to under-count borderline violations），(c)SOPBench task structure（SOP execution vs customer service）对ambiguity的exposure pattern不同。但31.2pp仍在key metric range [25,40]内且OR=12.8 massive。type ranking correlation ρ=0.80（p=0.042, significant）确认incompleteness universally highest-risk——即使在完全不同的benchmark、不同的domains、不同的verifier下仍然排第一。cross-benchmark effect correlation r=0.89表示per-model effect sizes高度一致（Claude always lowest, DeepSeek always highest）。rule-based verifier与LLM judge 91% agreement消除了'LLM-as-judge single point of failure'的reviewer concern。Healthcare domain delta（33.8pp）> Bank domain（28.6pp）可能因为healthcare policies have more safety-critical boundary conditions。auth_scope range 48pp in SOPBench（vs 52pp in τ²-bench）independently confirms model×type interaction as robust finding。这些结果将paper从'retail/airline finding'升级为'cross-domain finding spanning 4 domains'。"
1491	  },
1492	  {
1493	    "name": "classifier_poc",
1494	    "description": "Binary ambiguity detector PoC：DeBERTa-v3-large在annotated clause pairs上fine-tune，5-fold CV评估。验证findings的practical applicability。",
1495	    "results": {
1496	      "binary_f1": 0.81,
1497	      "binary_precision": 0.83,
1498	      "binary_recall": 0.79,
1499	      "binary_fpr": 0.044,
1500	      "macro_f1": 0.63,
1501	      "best_type_f1_cp": 0.94,
1502	      "worst_type_f1_incomp": 0.34,
1503	      "per_type_f1": {
1504	        "conditional_precedence": 0.94,
1505	        "scopal": 0.75,
1506	        "coreferential": 0.7,
1507	        "authorization_scope": 0.58,
1508	        "lexical": 0.39,
1509	        "incompleteness": 0.34
1510	      },
1511	      "total_clauses": 500,
1512	      "folds": 5,
1513	      "gpu_hours": 6.5
1514	    },
1515	    "tables": [
1516	      {
1517	        "title": "DeBERTa Classifier Performance (5-fold CV)",
1518	        "columns": [
1519	          "Metric",
1520	          "Value",
1521	          "Note"
1522	        ],
1523	        "rows": [
1524	          [
1525	            "Binary F1",
1526	            "0.81",
1527	            "Ambiguous vs unambiguous"
1528	          ],
1529	          [
1530	            "Binary Precision",
1531	            "0.83",
1532	            "Few false positives"
1533	          ],
1534	          [
1535	            "Binary Recall",
1536	            "0.79",
1537	            "Misses 21% (mostly incompleteness)"
1538	          ],
1539	          [
1540	            "Binary FPR",
1541	            "4.4%",
1542	            "Practical for deployment"
1543	          ],
1544	          [
1545	            "Macro F1 (6-type)",
1546	            "0.63",
1547	            "High variance across types"
1548	          ]
1549	        ]
1550	      },
1551	      {
1552	        "title": "Per-Type Classification Performance",
1553	        "columns": [
1554	          "Type",
1555	          "F1",
1556	          "Precision",
1557	          "Recall",
1558	          "Detection Difficulty"
1559	        ],
1560	        "rows": [
1561	          [
1562	            "conditional_precedence",
1563	            "0.94",
1564	            "0.92",
1565	            "0.96",
1566	            "Easy — explicit conflict markers"
1567	          ],
1568	          [
1569	            "scopal",
1570	            "0.75",
1571	            "0.78",
1572	            "0.72",
1573	            "Moderate — structural cues learnable"
1574	          ],
1575	          [
1576	            "coreferential",
1577	            "0.70",
1578	            "0.73",
1579	            "0.67",
1580	            "Moderate — pronoun/RC patterns"
1581	          ],
1582	          [
1583	            "authorization_scope",
1584	            "0.58",
1585	            "0.62",
1586	            "0.55",
1587	            "Hard — subtle boundary language"
1588	          ],
1589	          [
1590	            "lexical",
1591	            "0.39",
1592	            "0.42",
1593	            "0.36",
1594	            "Very hard — context-dependent polysemy"
1595	          ],
1596	          [
1597	            "incompleteness",
1598	            "0.34",
1599	            "0.38",
1600	            "0.31",
1601	            "Hardest — absence has no signal"
1602	          ]
1603	        ]
1604	      }
1605	    ],
1606	    "figures": [],
1607	    "analysis": "Classifier PoC在best档下scoped为appendix-level practical contribution，不overclaim为core contribution。binary F1=0.81 sufficient for'automated pre-screening tool that flags potentially ambiguous clauses for human review'的framing。per-type performance的inverse relationship with danger level（incompleteness: highest danger + lowest detectability）是a sobering practical finding——reinforces the need for domain experts in the loop, not just automated tools。PoC demonstrates that our taxonomy has practical discriminative power（types differ in surface detectability），but also that the most safety-critical type resists automated detection。\n\nbest档下DeBERTa PoC在binary detection达F1=0.81——足以demonstrate practical value但不overclaim。per-type F1的extreme variance（CP 0.94 vs incompleteness 0.34）本身是interesting finding：(a) CP最easy to detect因为explicit conflict markers（'but', 'however', 'unless'等surface cues）在training data中high-frequency，(b) incompleteness最hard因为absence of information has no surface signal——you can't detect what's NOT there from text features alone。这mirrors C2 type hierarchy in an unexpected way：most dangerous type（incompleteness）is also hardest to automatically detect，creating a dangerous blind spot。scopal（0.75）和coreferential（0.70）intermediate因为structural cues（quantifier scope, pronoun chains）are learnable but require syntactic understanding。auth_scope（0.58）moderate因为permission language有some surface patterns但boundary vagueness is subtle。macro F1=0.63 reflects per-type imbalance。binary FPR=0.044（<5%）意味着very few false alarms——practical for deployment as pre-filter。"
1608	  }
1609	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1c9062e-d967-4be0-8fc3-1c1f0e4811e1",
  "isSidechain": false,
  "promptId": "d65c2e8d-79bc-4128-97c7-582868b89531",
  "type": "user",
  "uuid": "8336972d-be85-4234-a6fa-0102ca227786",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"full_study_clause_generation\",\n    \"description\": \"生成300条clause pairs（50/type × 6 types），涵盖coreferential（50 new）、authorization_scope（50 new）、lexical（+20）、incompleteness（+20）。CP混合labeled+unlabeled格式。全量Chantree-style质量验证+cross-type token delta均衡检查。\",\n    \"results\": {\n      \"total_clauses\": 300,\n      \"clauses_per_type\": 50,\n      \"chantree_quality_pass_rate\": 0.98,\n      \"mean_token_delta_spec_layer\": 34.2,\n      \"mean_token_delta_ling_layer\": 11.6,\n      \"token_delta_within_type_cv\": 0.18,\n      \"cross_type_balance_chi2_p\": 0.72,\n      \"cp_labeled_ratio\": 0.4,\n      \"cp_unlabeled_ratio\": 0.6,\n      \"flesch_kincaid_mean\": 11.8,\n      \"flesch_kincaid_sd\": 2.1,\n      \"domain_split_retail\": 150,\n      \"domain_split_airline\": 150\n    },\n    \"tables\": [\n      {\n        \"title\": \"Clause Distribution by Type × Domain\",\n        \"columns\": [\n          \"Type\",\n          \"Layer\",\n          \"Retail\",\n          \"Airline\",\n          \"Total\",\n          \"Mean Token Delta\"\n        ],\n        \"rows\": [\n          [\n            \"authorization_scope\",\n            \"Specification\",\n            \"25\",\n            \"25\",\n            \"50\",\n            \"36.1\"\n          ],\n          [\n            \"conditional_precedence\",\n            \"Specification\",\n            \"25\",\n            \"25\",\n            \"50\",\n            \"28.4\"\n          ],\n          [\n            \"incompleteness\",\n            \"Specification\",\n            \"25\",\n            \"25\",\n            \"50\",\n            \"34.6\"\n          ],\n          [\n            \"scopal\",\n            \"Linguistic\",\n            \"25\",\n            \"25\",\n            \"50\",\n            \"14.2\"\n          ],\n          [\n            \"lexical\",\n            \"Linguistic\",\n            \"25\",\n            \"25\",\n            \"50\",\n            \"12.8\"\n          ],\n          [\n            \"coreferential\",\n            \"Linguistic\",\n            \"25\",\n            \"25\",\n            \"50\",\n            \"7.8\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"300 clauses质量均达到EMNLP出版标准。token delta的层级差异（spec >> ling）不是confound而是substantive finding——直接映射到Disambiguation Channel Framework中'外部消歧通道可用性'的概念。CP混合格式避免了'artificial conflict presentation'的reviewer concern。Chantree-style pass rate 98%意味着≤6条需minor修订，无系统性质量问题。\\n\\nbest档下clause generation利用已有pilot（10 clauses/type经MVP和diag验证）+ DRIP-R cross-walk作为template anchor。98%通过Chantree-style validation因为迭代优化了edge cases（e.g., coreferential RC attachment的pragmatic naturalness，auth_scope permission boundary的domain plausibility）。token delta的type-level差异（spec 34.2 vs ling 11.6）反映了真实的disambiguation complexity差异——spec-layer需要更多token来消除歧义因为涉及domain knowledge（auth boundaries, missing conditions），这本身是Disambiguation Channel Framework的经验支撑。CV=0.18表明within-type变异控制良好。CP混合格式（40% labeled / 60% unlabeled）遵循Reviewer建议以提高ecological validity。\"\n  },\n  {\n    \"name\": \"new_type_mini_pilot\",\n    \"description\": \"Coreferential + authorization_scope小规模验证：5 clauses/type × 2 conditions × 1 model（gpt-5.4）= 20 episodes。验证新类型clause设计的基本有效性。\",\n    \"results\": {\n      \"total_episodes\": 20,\n      \"auth_scope_amb_violation_rate\": 0.6,\n      \"auth_scope_unamb_violation_rate\": 0.0,\n      \"auth_scope_delta_pp\": 60,\n      \"coreferential_amb_violation_rate\": 0.2,\n      \"coreferential_unamb_violation_rate\": 0.0,\n      \"coreferential_delta_pp\": 20,\n      \"systematic_issues_found\": 0,\n      \"proceed_to_full_study\": true\n    },\n    \"tables\": [\n      {\n        \"title\": \"Mini-Pilot Results (gpt-5.4)\",\n        \"columns\": [\n          \"Type\",\n          \"N\",\n          \"Amb Rate\",\n          \"Unamb Rate\",\n          \"Delta (pp)\",\n          \"Issues\"\n        ],\n        \"rows\": [\n          [\n            \"authorization_scope\",\n            \"10\",\n            \"60%\",\n            \"0%\",\n            \"+60\",\n            \"None\"\n          ],\n          [\n            \"coreferential\",\n            \"10\",\n            \"20%\",\n            \"0%\",\n            \"+20\",\n            \"None\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"两类型均通过基本有效性检验：ambiguous condition产生violations而unambiguous control clean。auth_scope的高violation rate预示了它在C4中作为model-differentiating type的角色。coreferential的较低rate预示了其作为boundary case的特性（partial disambiguation via tool responses）。N=5太小无法做统计推断，但signal清晰且无red flags，可安全进入full study。\\n\\nbest档下两个新类型均表现出清晰的ambiguity效应。auth_scope在gpt-5.4上高达60%（与后续full study的64%一致），因为gpt-5.4对authorization boundary特别脆弱——其action-oriented training倾向于'assume permission and proceed'。coreferential较低（20%）因为gpt-5.4部分通过tool response获得referential disambiguation。unamb均为0%因为N=5×1时control condition大概率全clean。无systematic issues意味着clause设计无需返工，pipeline直接进full study。\"\n  },\n  {\n    \"name\": \"full_study_api\",\n    \"description\": \"300 clauses × 2 conditions × 3 API models（gpt-5.4, gpt-4.1, claude-sonnet-4-6）= 1,800 episodes。Cross-judge evaluation（互评：gpt-4.1评gpt-5.4，gpt-5.4评gpt-4.1和Claude）。\",\n    \"results\": {\n      \"total_episodes\": 1800,\n      \"gpt54_amb_rate\": 0.41,\n      \"gpt54_unamb_rate\": 0.027,\n      \"gpt54_delta_pp\": 38.3,\n      \"gpt54_mcnemar_p\": 1e-28,\n      \"gpt41_amb_rate\": 0.407,\n      \"gpt41_unamb_rate\": 0.06,\n      \"gpt41_delta_pp\": 34.7,\n      \"gpt41_mcnemar_p\": 1e-24,\n      \"claude_amb_rate\": 0.303,\n      \"claude_unamb_rate\": 0.047,\n      \"claude_delta_pp\": 25.7,\n      \"claude_mcnemar_p\": 1e-17,\n      \"pooled_amb_rate\": 0.373,\n      \"pooled_unamb_rate\": 0.044,\n      \"pooled_delta_pp\": 32.9,\n      \"pooled_or\": 13.2,\n      \"cross_judge_kappa\": 0.74\n    },\n    \"tables\": [\n      {\n        \"title\": \"API Model Binary Effect (C1)\",\n        \"columns\": [\n          \"Model\",\n          \"Amb Rate\",\n          \"Unamb Rate\",\n          \"Delta (pp)\",\n          \"OR\",\n          \"95% CI\",\n          \"McNemar p\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            \"41.0%\",\n            \"2.7%\",\n            \"+38.3\",\n            \"25.3\",\n            \"[14.8, 43.2]\",\n            \"<1e-28\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"40.7%\",\n            \"6.0%\",\n            \"+34.7\",\n            \"10.9\",\n            \"[7.1, 16.6]\",\n            \"<1e-24\"\n          ],\n          [\n            \"claude-sonnet-4-6\",\n            \"30.3%\",\n            \"4.7%\",\n            \"+25.7\",\n            \"8.9\",\n            \"[5.5, 14.5]\",\n            \"<1e-17\"\n          ],\n          [\n            \"Pooled (3 API)\",\n            \"37.3%\",\n            \"4.4%\",\n            \"+32.9\",\n            \"13.2\",\n            \"[9.8, 17.7]\",\n            \"<1e-50\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"API Model × Type Interaction (Amb Condition Violation Rates)\",\n        \"columns\": [\n          \"Type\",\n          \"gpt-5.4\",\n          \"gpt-4.1\",\n          \"Claude\",\n          \"Range (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"authorization_scope\",\n            \"64%\",\n            \"46%\",\n            \"12%\",\n            \"52\"\n          ],\n          [\n            \"incompleteness\",\n            \"46%\",\n            \"58%\",\n            \"48%\",\n            \"12\"\n          ],\n          [\n            \"lexical\",\n            \"42%\",\n            \"34%\",\n            \"32%\",\n            \"10\"\n          ],\n          [\n            \"scopal\",\n            \"42%\",\n            \"38%\",\n            \"32%\",\n            \"10\"\n          ],\n          [\n            \"conditional_precedence\",\n            \"34%\",\n            \"36%\",\n            \"36%\",\n            \"2\"\n          ],\n          [\n            \"coreferential\",\n            \"18%\",\n            \"32%\",\n            \"22%\",\n            \"14\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"3 API模型完整确认C1（binary effect universal across architectures）和C4（model×type interaction）。关键发现：auth_scope 52pp range是整个interaction矩阵的最大值，直接指向safety training selectivity。Claude的auth_scope robustness（12%）是其最distinctive特征，暗示Anthropic RLHF中authorization boundary handling被explicitly addressed。gpt-5.4的highest overall rate但lowest coreferential（18%）暗示不同failure mechanism——frontier model在referential ambiguity上能部分self-resolve但在permission boundaries上over-confident。\\n\\nbest档下3个API模型全部展示massive binary effect。gpt-5.4最高（+38.3pp）因为frontier model的action-orientation最强——更倾向于'confident execution'而非'pause and ask'。Claude最低（+25.7pp）因为Anthropic的RLHF显式训练了authorization boundary awareness和conservative behavior。gpt-4.1居中（+34.7pp）作为mid-tier模型在capability和safety之间平衡。unamb baseline均<6%表明control condition clean——matched-pair设计成功隔离了ambiguity effect。cross-judge κ=0.74（substantial agreement）表明judge评估可靠。这些结果与plan_010 perturbation control（Δ_perturb=3.33pp）对比形成causal inference gold standard。\"\n  },\n  {\n    \"name\": \"full_study_opensource\",\n    \"description\": \"300 clauses × 2 conditions × 2 open-source models via OpenRouter（qwen3-235b-a22b, deepseek-chat-v3-0324）= 1,200 episodes。与plan_002并行运行。\",\n    \"results\": {\n      \"total_episodes\": 1200,\n      \"qwen3_amb_rate\": 0.431,\n      \"qwen3_unamb_rate\": 0.107,\n      \"qwen3_delta_pp\": 32.4,\n      \"qwen3_mcnemar_p\": 1e-19,\n      \"deepseek_amb_rate\": 0.497,\n      \"deepseek_unamb_rate\": 0.107,\n      \"deepseek_delta_pp\": 39.0,\n      \"deepseek_mcnemar_p\": 1e-25,\n      \"qwen3_type_chi2_p\": 0.007,\n      \"qwen3_type_V\": 0.23,\n      \"deepseek_type_chi2_p\": 0.277,\n      \"deepseek_type_V\": 0.14\n    },\n    \"tables\": [\n      {\n        \"title\": \"Open-Source Model Binary Effect (C1)\",\n        \"columns\": [\n          \"Model\",\n          \"Architecture\",\n          \"Amb Rate\",\n          \"Unamb Rate\",\n          \"Delta (pp)\",\n          \"OR\",\n          \"McNemar p\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B\",\n            \"MoE (22B active)\",\n            \"43.1%\",\n            \"10.7%\",\n            \"+32.4\",\n            \"6.4\",\n            \"<1e-19\"\n          ],\n          [\n            \"DeepSeek-V3\",\n            \"MoE (37B active)\",\n            \"49.7%\",\n            \"10.7%\",\n            \"+39.0\",\n            \"8.3\",\n            \"<1e-25\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Open-Source Model × Type Violation Rates (Amb Condition)\",\n        \"columns\": [\n          \"Type\",\n          \"Qwen3\",\n          \"DeepSeek\",\n          \"Range (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"authorization_scope\",\n            \"26%\",\n            \"60%\",\n            \"34\"\n          ],\n          [\n            \"incompleteness\",\n            \"62%\",\n            \"54%\",\n            \"8\"\n          ],\n          [\n            \"lexical\",\n            \"52%\",\n            \"54%\",\n            \"2\"\n          ],\n          [\n            \"scopal\",\n            \"37%\",\n            \"48%\",\n            \"11\"\n          ],\n          [\n            \"conditional_precedence\",\n            \"40%\",\n            \"38%\",\n            \"2\"\n          ],\n          [\n            \"coreferential\",\n            \"42%\",\n            \"44%\",\n            \"2\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Open-source模型data完成后5-model矩阵齐全。DeepSeek的uniform vulnerability（type χ² p=0.277, NOT significant）是C4的关键对照——当safety training不够type-specific时，所有ambiguity types equally dangerous。Qwen3的moderate differentiation（p=0.007）介于DeepSeek（undifferentiated）和GPT-5.4/Claude（highly differentiated）之间。5-model spectrum从Claude（lowest, most differentiated）到DeepSeek（highest, least differentiated）形成完美narrative gradient，支撑'safety training selectivity'的核心theoretical claim。\\n\\nbest档下open-source模型均replicate C1 binary effect。DeepSeek最高vulnerability（49.7%）且type differentiation不显著（V=0.14, p=0.277），因为其safety training较less type-specific——uniformly high across all types暗示safety guardrails未针对特定ambiguity pattern调优。Qwen3居中（43.1%）但显示moderate type differentiation（V=0.23, p=0.007），特别是high incompleteness+lexical与low auth_scope的组合模式。unamb baseline较高（10.7%）反映了open-source模型in general less calibrated的baseline safety——但这使得delta effect更conservative（实际ambiguity-specific impact可能更大）。这些结果对C4至关重要：提供了dense vs MoE architecture comparison和proprietary vs open-source safety training comparison。\"\n  },\n  {\n    \"name\": \"full_study_analysis\",\n    \"description\": \"2,997 episodes全量统计分析：C1 binary effect、C2 type hierarchy（omnibus + pairwise + TOST）、C3 layer effect + within-judge check、C4 model×type interaction + logistic regression。含power analysis、MDE报告、inter-model agreement、info delta mediator分析。\",\n    \"results\": {\n      \"total_episodes\": 2997,\n      \"c1_pooled_delta_pp\": 34.0,\n      \"c1_pooled_or\": 15.1,\n      \"c1_or_ci\": \"[10.78, 21.17]\",\n      \"c1_bootstrap_ci\": \"[31.2, 36.9]\",\n      \"c1_mcnemar_p\": 1e-100,\n      \"c1_logistic_condition_coef\": 2.278,\n      \"c1_logistic_condition_z\": 19.65,\n      \"c2_omnibus_chi2\": 28.02,\n      \"c2_omnibus_p\": 3.6e-05,\n      \"c2_V\": 0.137,\n      \"c2_power\": 0.993,\n      \"c2_MDE\": 0.093,\n      \"c2_tost_15pp_equivalent_pairs\": \"8/15\",\n      \"c2_tost_10pp_equivalent_pairs\": \"4/15\",\n      \"c3_layer_delta_pp\": 6.08,\n      \"c3_layer_p\": 0.017,\n      \"c3_layer_V\": 0.062,\n      \"c3_within_judge_gpt41_judged_p\": 0.059,\n      \"c3_within_judge_gpt54_judged_p\": 0.157,\n      \"c4_model_chi2\": 31.02,\n      \"c4_model_p\": 3e-06,\n      \"c4_model_V\": 0.102,\n      \"c4_amb_only_chi2\": 24.01,\n      \"c4_amb_only_p\": 7.9e-05,\n      \"c4_fleiss_kappa\": 0.384,\n      \"c4_auth_scope_range_pp\": 52,\n      \"c4_incomp_range_pp\": 16,\n      \"info_delta_logistic_coef\": 0.022,\n      \"info_delta_logistic_z\": 3.49,\n      \"info_delta_logistic_p\": 0.0005,\n      \"inter_model_systematic_nocuity_rate\": 0.27\n    },\n    \"tables\": [\n      {\n        \"title\": \"C1 Binary Effect Summary (5 Models Pooled)\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"Delta (pp)\",\n            \"+34.0\",\n            \"[31.2, 36.9]\"\n          ],\n          [\n            \"Odds Ratio\",\n            \"15.1\",\n            \"[10.78, 21.17]\"\n          ],\n          [\n            \"McNemar p\",\n            \"<1e-100\",\n            \"—\"\n          ],\n          [\n            \"Logistic coef (condition_amb)\",\n            \"2.278\",\n            \"z=19.65, p<0.001\"\n          ],\n          [\n            \"N models replicating\",\n            \"5/5\",\n            \"all p<1e-17\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"C2 Type Hierarchy (3-Tier Structure)\",\n        \"columns\": [\n          \"Tier\",\n          \"Types\",\n          \"Violation Rate Range\",\n          \"Key Property\"\n        ],\n        \"rows\": [\n          [\n            \"High\",\n            \"incompleteness\",\n            \"53.6%\",\n            \"Universally dangerous across all models\"\n          ],\n          [\n            \"Mid\",\n            \"lexical, auth_scope, scopal, CP\",\n            \"36.8%–42.8%\",\n            \"Pairwise equivalent at ±15pp\"\n          ],\n          [\n            \"Low\",\n            \"coreferential\",\n            \"31.6%\",\n            \"Partial disambiguation via tool responses\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"C4 Model × Type Interaction Matrix (Amb Violation Rates)\",\n        \"columns\": [\n          \"Type\",\n          \"GPT-5.4\",\n          \"GPT-4.1\",\n          \"Claude\",\n          \"Qwen3\",\n          \"DeepSeek\",\n          \"Range\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"64%\",\n            \"46%\",\n            \"12%\",\n            \"26%\",\n            \"60%\",\n            \"52pp\"\n          ],\n          [\n            \"incompleteness\",\n            \"46%\",\n            \"58%\",\n            \"48%\",\n            \"62%\",\n            \"54%\",\n            \"16pp\"\n          ],\n          [\n            \"lexical\",\n            \"42%\",\n            \"34%\",\n            \"32%\",\n            \"52%\",\n            \"54%\",\n            \"22pp\"\n          ],\n          [\n            \"scopal\",\n            \"42%\",\n            \"38%\",\n            \"32%\",\n            \"37%\",\n            \"48%\",\n            \"16pp\"\n          ],\n          [\n            \"cond_prec\",\n            \"34%\",\n            \"36%\",\n            \"36%\",\n            \"40%\",\n            \"38%\",\n            \"6pp\"\n          ],\n          [\n            \"coreferential\",\n            \"18%\",\n            \"32%\",\n            \"22%\",\n            \"42%\",\n            \"44%\",\n            \"26pp\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"C2 TOST Equivalence Analysis\",\n        \"columns\": [\n          \"Margin\",\n          \"Equivalent Pairs\",\n          \"Non-Equivalent Pairs\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"±15pp\",\n            \"8/15\",\n            \"7/15\",\n            \"Types NOT interchangeable\"\n          ],\n          [\n            \"±10pp\",\n            \"4/15\",\n            \"11/15\",\n            \"Strong type differentiation\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"C3 Layer Effect (Aggregate + Within-Judge)\",\n        \"columns\": [\n          \"Analysis\",\n          \"Spec Rate\",\n          \"Ling Rate\",\n          \"Delta (pp)\",\n          \"p-value\",\n          \"Status\"\n        ],\n        \"rows\": [\n          [\n            \"5-model aggregate\",\n            \"44.0%\",\n            \"37.9%\",\n            \"+6.08\",\n            \"0.017\",\n            \"Significant\"\n          ],\n          [\n            \"Within-judge (gpt-4.1 judged)\",\n            \"—\",\n            \"—\",\n            \"+8.0\",\n            \"0.059\",\n            \"Marginal\"\n          ],\n          [\n            \"Within-judge (gpt-5.4 judged)\",\n            \"—\",\n            \"—\",\n            \"+4.8\",\n            \"0.157\",\n            \"Not significant\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Per-Model Layer Gap (C3 feeds C4)\",\n        \"columns\": [\n          \"Model\",\n          \"Spec Rate\",\n          \"Ling Rate\",\n          \"Layer Gap (pp)\",\n          \"Primary Driver\"\n        ],\n        \"rows\": [\n          [\n            \"GPT-5.4\",\n            \"48.0%\",\n            \"34.0%\",\n            \"+14.0\",\n            \"auth_scope 64%\"\n          ],\n          [\n            \"GPT-4.1\",\n            \"46.7%\",\n            \"34.7%\",\n            \"+12.0\",\n            \"auth_scope 46%\"\n          ],\n          [\n            \"Claude\",\n            \"32.0%\",\n            \"28.7%\",\n            \"+3.3\",\n            \"auth_scope only 12%\"\n          ],\n          [\n            \"DeepSeek\",\n            \"50.7%\",\n            \"48.7%\",\n            \"+2.0\",\n            \"Uniformly high\"\n          ],\n          [\n            \"Qwen3\",\n            \"42.7%\",\n            \"43.6%\",\n            \"-0.9\",\n            \"auth_scope only 26%\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Per-Model Type χ² (C4 Differentiation)\",\n        \"columns\": [\n          \"Model\",\n          \"Type χ²\",\n          \"p-value\",\n          \"V\",\n          \"Pattern\"\n        ],\n        \"rows\": [\n          [\n            \"GPT-5.4\",\n            \"23.44\",\n            \"0.0003\",\n            \"0.28\",\n            \"Very high auth_scope, very low coref\"\n          ],\n          [\n            \"Claude\",\n            \"17.87\",\n            \"0.003\",\n            \"0.24\",\n            \"Very low auth_scope, moderate others\"\n          ],\n          [\n            \"Qwen3\",\n            \"15.89\",\n            \"0.007\",\n            \"0.23\",\n            \"High incomp+lex, low auth_scope\"\n          ],\n          [\n            \"GPT-4.1\",\n            \"9.89\",\n            \"0.078\",\n            \"0.18\",\n            \"Borderline differentiation\"\n          ],\n          [\n            \"DeepSeek\",\n            \"6.31\",\n            \"0.277\",\n            \"0.14\",\n            \"Uniformly high — NOT significant\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"统计分析完整确认所有5个claims在best档下的强度排序：C1（最强，triple causal evidence）> C4（star finding，52pp interaction）> C2（well-powered small effect）> C5（qualitative depth）> C3（suggestive, honestly reported fragility）。关键methodological贡献：(a) power=0.993下接受V=0.137为'real but small'是sophisticated统计论证，(b) TOST双margin分析显示types genuinely non-equivalent，(c) within-judge fragility透明报告建立credibility。审稿人最可能challenge C3 fragility——但best档下这被C4的model×type interaction absorb：layer effect is itself model-dependent, making the interaction the more fundamental finding。systematic nocuity rate 27%是unexpected finding，提出B&K third category作为Discussion贡献。\\n\\nbest档下所有统计分析产出与paper_framing完全一致的强结果。C1以OR=15.1（CI不含1）成为agent safety文献最强因果证据——matched-pair + perturbation control + 5-model replication的三重支撑无可挑战。C2的V=0.137虽small但power=0.993（MDE=0.093远小于observed V），审稿人接受'effect real but small, 3-tier structure captures heterogeneity better than single V'的论证——这比声称large effect更honest且更sophisticated。C3 within-judge fragility在best档下被审稿人视为'honest reporting'而非fatal flaw，因为(a)aggregate p=0.017仍significant，(b)paper明确将C3降级为'suggestive'并在Limitations披露，(c)C4 model×type interaction提供了更fundamental的explanation（layer effect is itself model-dependent）。C4的52pp auth_scope range是整篇论文的star statistic——连接B&K nocuous ambiguity theory到modern alignment research的桥梁。Fleiss κ=0.384（fair）quantifies inter-model disagreement on WHICH clauses trigger violations，支撑Differential Nocuity框架。systematic nocuity rate 27%发现所有模型converge on same WRONG interpretation——提出B&K extension。\"\n  },\n  {\n    \"name\": \"error_analysis\",\n    \"description\": \"从full study中采样violation traces进行qualitative failure mode分析：每type 50条traces × 6 types = 300 total（across 5 models × 2 domains）。分类failure modes，建立type-specific signatures，验证Ambiguity Blindness，对比cross-model consistency。\",\n    \"results\": {\n      \"total_traces_coded\": 300,\n      \"failure_modes_identified\": 4,\n      \"type_diagnostic_accuracy\": 0.83,\n      \"ambiguity_awareness_rate\": 0.046,\n      \"surface_adoption_rate\": 0.89,\n      \"escalate_to_user_rate\": 0.008,\n      \"cross_model_dominant_mode_agreement\": \"5/6\",\n      \"cross_domain_max_delta_pp\": 13,\n      \"coreferential_conservative_refusal_rate\": 0.085,\n      \"inter_coder_agreement\": 0.8,\n      \"inter_coder_kappa_4cat\": 0.594,\n      \"gwet_ac1\": 0.73\n    },\n    \"tables\": [\n      {\n        \"title\": \"Type-Specific Failure Mode Signatures\",\n        \"columns\": [\n          \"Type\",\n          \"Dominant Mode\",\n          \"Rate (5-model)\",\n          \"Secondary Mode\",\n          \"Rate\",\n          \"Layer Pattern\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"unauthorized_escalation\",\n            \"75%\",\n            \"inappropriate_action\",\n            \"18%\",\n            \"Spec: guess-and-act\"\n          ],\n          [\n            \"incompleteness\",\n            \"assumption_based_action\",\n            \"63%\",\n            \"unauthorized_escalation\",\n            \"22%\",\n            \"Spec: guess-and-act\"\n          ],\n          [\n            \"scopal\",\n            \"scope_misapplication\",\n            \"75%\",\n            \"assumption_based_action\",\n            \"15%\",\n            \"Ling: misparse\"\n          ],\n          [\n            \"lexical\",\n            \"assumption_based_action\",\n            \"62%\",\n            \"scope_misapplication\",\n            \"20%\",\n            \"Ling: misparse-hybrid\"\n          ],\n          [\n            \"cond_prec\",\n            \"scope_misapplication\",\n            \"35%\",\n            \"arbitrary_rule_selection\",\n            \"29%\",\n            \"Spec: mixed\"\n          ],\n          [\n            \"coreferential\",\n            \"scope_misapplication\",\n            \"38%\",\n            \"assumption_based_action\",\n            \"33%\",\n            \"Ling: flat distribution\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Ambiguity Blindness Metrics (5 Models)\",\n        \"columns\": [\n          \"Metric\",\n          \"GPT-5.4\",\n          \"GPT-4.1\",\n          \"Claude\",\n          \"Qwen3\",\n          \"DeepSeek\",\n          \"Pooled\"\n        ],\n        \"rows\": [\n          [\n            \"Awareness rate\",\n            \"4.1%\",\n            \"10.7%\",\n            \"5.2%\",\n            \"3.8%\",\n            \"2.4%\",\n            \"4.6%\"\n          ],\n          [\n            \"Surface adoption\",\n            \"91%\",\n            \"85%\",\n            \"88%\",\n            \"90%\",\n            \"93%\",\n            \"89%\"\n          ],\n          [\n            \"Escalate to user\",\n            \"0.8%\",\n            \"1.6%\",\n            \"1.2%\",\n            \"0.4%\",\n            \"0.2%\",\n            \"0.8%\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Inter-Coder Agreement (Automated Cross-Coding)\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"4-category agreement\",\n            \"80%\",\n            \"Good\"\n          ],\n          [\n            \"Cohen's κ (4-cat)\",\n            \"0.594\",\n            \"Moderate (kappa paradox deflated)\"\n          ],\n          [\n            \"Gwet's AC1 (primary)\",\n            \"0.73\",\n            \"Good — robust to prevalence imbalance\"\n          ],\n          [\n            \"Types with κ paradox\",\n            \"2/6\",\n            \"lexical (91.7% agree, κ=0.0), scopal (100%, κ undef)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Error analysis提供了C1-C4量化发现的mechanistic explanation。核心insight：spec-layer failure是'active guessing in absence of information'而ling-layer failure是'unconscious misparse of grammatical structure'——两种根本不同的cognitive（computational）机制。这映射到Disambiguation Channel Framework：ling-layer有partial external channels（tool responses可disambiguate referent, context可clarify word sense）但spec-layer没有（missing policy info无法从external source补充）。Ambiguity Blindness的model-level variation（gpt-4.1 10.7% vs DeepSeek 2.4%）暗示mid-tier models may paradoxically be more 'cautious' than frontier models——higher awareness但still act（only 1.6% escalation），构成Discussion中interesting nuance。\\n\\nbest档下error analysis产出clean的type-specific failure signatures——这是EMNLP reviewers最看重的qualitative depth（distilled insight: CL论文需要linguistic WHY behind quantitative WHAT）。4个failure modes（unauthorized_escalation, assumption_based_action, scope_misapplication, arbitrary_rule_selection）形成2×2矩阵映射到2 layers：spec→guess-and-act (escalation+assumption), ling→misparse-and-apply (scope_misapplication)。5/6 types cross-model dominant mode一致（仅coreferential diverge）——failure modes是type-specific而非model-specific，支撑taxonomy的construct validity。Ambiguity Blindness<5%是empirical hard evidence（非merely named concept），>88% surface adoption直接challenge了'models understand instructions'的assumption。coreferential conservative refusal 8.5%（vs avg 2-3%）解释了其作为boundary case的low violation rate。κ=0.594 deflated by kappa paradox但Gwet's AC1=0.73（good）作为primary metric。\"\n  },\n  {\n    \"name\": \"reliability_test\",\n    \"description\": \"Test-retest reliability：30 clauses（5/type）× 3 replicates × 2 conditions × 2 models（gpt-5.4, gpt-4.1）= 360 episodes。计算per-clause violation rates的ICC。\",\n    \"results\": {\n      \"total_episodes\": 360,\n      \"icc_overall\": 0.919,\n      \"icc_ci\": \"[0.892, 0.940]\",\n      \"icc_binary\": 0.847,\n      \"icc_gpt54\": 0.921,\n      \"icc_gpt41\": 0.918,\n      \"per_type_icc_min\": 0.807,\n      \"per_type_icc_max\": 0.989,\n      \"ling_layer_icc_mean\": 0.982,\n      \"spec_layer_icc_mean\": 0.84,\n      \"bootstrap_ci_width_key_comparisons\": \"<10pp\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"ICC Results by Level and Model\",\n        \"columns\": [\n          \"Level\",\n          \"ICC\",\n          \"95% CI\",\n          \"Rating\"\n        ],\n        \"rows\": [\n          [\n            \"Overall (continuous)\",\n            \"0.919\",\n            \"[0.892, 0.940]\",\n            \"Excellent\"\n          ],\n          [\n            \"Binary (0/1)\",\n            \"0.847\",\n            \"[0.804, 0.883]\",\n            \"Good\"\n          ],\n          [\n            \"gpt-5.4 only\",\n            \"0.921\",\n            \"[0.886, 0.948]\",\n            \"Excellent\"\n          ],\n          [\n            \"gpt-4.1 only\",\n            \"0.918\",\n            \"[0.882, 0.946]\",\n            \"Excellent\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Per-Type ICC (Layer Pattern)\",\n        \"columns\": [\n          \"Type\",\n          \"Layer\",\n          \"ICC\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"scopal\",\n            \"Linguistic\",\n            \"0.989\",\n            \"Near-perfect reproducibility\"\n          ],\n          [\n            \"lexical\",\n            \"Linguistic\",\n            \"0.981\",\n            \"Near-perfect\"\n          ],\n          [\n            \"coreferential\",\n            \"Linguistic\",\n            \"0.976\",\n            \"Near-perfect\"\n          ],\n          [\n            \"auth_scope\",\n            \"Specification\",\n            \"0.857\",\n            \"Good — agents guess differently\"\n          ],\n          [\n            \"cond_prec\",\n            \"Specification\",\n            \"0.856\",\n            \"Good\"\n          ],\n          [\n            \"incompleteness\",\n            \"Specification\",\n            \"0.807\",\n            \"Good — most variable (missing info → stochastic)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Reliability analysis accomplishes three goals in best档：(a) methodological validation——ICC=0.919消除sampling noise concern，(b) construct validity for Disambiguation Channel Framework——ling/spec ICC differential is independent evidence for the framework, not derivable from violation rates alone, (c) practical implication——single-run design justified for main study, 3-replicate design unnecessary for future work using this paradigm。per-type ICC pattern is itself a finding worth reporting（spec-layer less reproducible = agents guess more）。\\n\\nbest档下ICC=0.919（excellent）直接解决了Reviewer concern about ±8pp sampling noise。三次独立replicates产出highly reproducible per-clause violation rates——同一clause在同一model上反复运行得到几乎相同的violation probability。per-type ICC pattern（ling 0.982 > spec 0.840）提供了convergent evidence for Disambiguation Channel Framework：ling-layer更reproducible因为agents consistently resolve（or fail to resolve）linguistic ambiguity in the same way（deterministic misparse），而spec-layer less reproducible因为agents在missing info下guess differently each run（stochastic guessing）。binary ICC=0.847（good）表明even binary classification（violation/no-violation）跨replicates稳定。这使得main study的single-run design methodologically justified。\"\n  },\n  {\n    \"name\": \"realism_validation\",\n    \"description\": \"Synthetic ambiguity injection的ecological validity验证：与DRIP-R natural ambiguities比较linguistic properties（sentence length, parse depth, Flesch-Kincaid, TTR）+ KS tests。\",\n    \"results\": {\n      \"ks_sentence_length_p\": 0.34,\n      \"ks_parse_depth_p\": 0.21,\n      \"ks_flesch_kincaid_p\": 0.48,\n      \"ks_ttr_p\": 0.15,\n      \"all_ks_nonsignificant\": true,\n      \"mean_sentence_length_ours\": 22.4,\n      \"mean_sentence_length_dripr\": 21.8,\n      \"mean_flesch_kincaid_ours\": 11.8,\n      \"mean_flesch_kincaid_dripr\": 12.3,\n      \"discriminator_accuracy\": 0.56,\n      \"discriminator_accuracy_ci\": \"[0.48, 0.64]\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Linguistic Property Comparison (Ours vs DRIP-R)\",\n        \"columns\": [\n          \"Property\",\n          \"Ours (mean±sd)\",\n          \"DRIP-R (mean±sd)\",\n          \"KS D\",\n          \"KS p\",\n          \"Significant?\"\n        ],\n        \"rows\": [\n          [\n            \"Sentence length (words)\",\n            \"22.4±6.2\",\n            \"21.8±7.1\",\n            \"0.08\",\n            \"0.34\",\n            \"No\"\n          ],\n          [\n            \"Parse depth\",\n            \"5.3±1.4\",\n            \"5.6±1.6\",\n            \"0.11\",\n            \"0.21\",\n            \"No\"\n          ],\n          [\n            \"Flesch-Kincaid grade\",\n            \"11.8±2.1\",\n            \"12.3±2.4\",\n            \"0.07\",\n            \"0.48\",\n            \"No\"\n          ],\n          [\n            \"Type-token ratio\",\n            \"0.82±0.06\",\n            \"0.80±0.07\",\n            \"0.12\",\n            \"0.15\",\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Realism validation在best档下完全化解RC4。所有KS tests non-significant且discriminator at chance——synthetic clauses与naturally occurring policy ambiguities distributional equivalent。这支撑了matched-pair design的external validity：effect sizes measured on synthetic pairs likely generalize to natural policy ambiguities。唯一caveat是DRIP-R仅covers retail domain——但combined with SOPBench cross-domain replication（plan_017），coverage extends to 4 domains。\\n\\nbest档下synthetic clauses与DRIP-R natural ambiguities在所有linguistic properties上statistically indistinguishable（all KS p>0.05）。这因为clause generation遵循了policy document的register和style conventions——使用了real τ²-bench policy templates作为base并仅修改specific ambiguity-bearing elements。discriminator accuracy 56%（CI含50%）表明even a trained classifier cannot reliably distinguish synthetic from natural。这是RC4（ecological validity）的strongest possible response：our synthetic injection preserves the distributional properties of natural policy ambiguity。sentence length几乎identical（22.4 vs 21.8 words）因为minimal-edit injection strategy不改变clause structure。Flesch-Kincaid相近（11.8 vs 12.3）因为both are professional policy language at roughly the same readability level。\"\n  },\n  {\n    \"name\": \"judge_calibration\",\n    \"description\": \"LLM-as-judge calibration：100 episodes stratified by type×model×condition，2 human annotators标注，计算human-LLM agreement（precision/recall/F1）+ inter-annotator κ。\",\n    \"results\": {\n      \"n_episodes\": 100,\n      \"human_inter_annotator_kappa\": 0.762,\n      \"human_llm_pooled_kappa_weighted\": 0.807,\n      \"human_llm_binary_kappa\": 0.87,\n      \"human_llm_binary_f1\": 0.92,\n      \"human_llm_binary_precision\": 0.94,\n      \"human_llm_binary_recall\": 0.9,\n      \"per_severity_agreement_severe\": 0.91,\n      \"per_severity_agreement_moderate\": 0.78,\n      \"per_severity_agreement_none\": 0.95,\n      \"cross_judge_kappa_weighted\": 0.685,\n      \"cross_judge_exact_agreement\": 0.76,\n      \"cross_judge_binary_kappa\": 0.74\n    },\n    \"tables\": [\n      {\n        \"title\": \"Human-LLM Agreement (Pooled)\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Weighted κ (3-tier)\",\n            \"0.807\",\n            \"Strong agreement\"\n          ],\n          [\n            \"Binary κ (violation/no-violation)\",\n            \"0.87\",\n            \"Strong agreement\"\n          ],\n          [\n            \"Binary F1\",\n            \"0.92\",\n            \"High accuracy\"\n          ],\n          [\n            \"Binary Precision\",\n            \"0.94\",\n            \"Very few false positives\"\n          ],\n          [\n            \"Binary Recall\",\n            \"0.90\",\n            \"10% borderline cases missed\"\n          ],\n          [\n            \"Human inter-annotator κ\",\n            \"0.762\",\n            \"Substantial (ceiling)\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Per-Severity Agreement Rates\",\n        \"columns\": [\n          \"Severity\",\n          \"Human-LLM Agreement\",\n          \"N\",\n          \"Main Disagreement Pattern\"\n        ],\n        \"rows\": [\n          [\n            \"Severe violation\",\n            \"91%\",\n            \"38\",\n            \"Rare: LLM sometimes downgrades to moderate\"\n          ],\n          [\n            \"Moderate violation\",\n            \"78%\",\n            \"27\",\n            \"Boundary cases with partial compliance\"\n          ],\n          [\n            \"No violation\",\n            \"95%\",\n            \"35\",\n            \"Near-perfect on clean episodes\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Cross-Judge Agreement (gpt-4.1 vs gpt-5.4 as judges)\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"Note\"\n        ],\n        \"rows\": [\n          [\n            \"Exact agreement\",\n            \"76%\",\n            \"—\"\n          ],\n          [\n            \"Weighted κ\",\n            \"0.685\",\n            \"Substantial\"\n          ],\n          [\n            \"Binary κ\",\n            \"0.74\",\n            \"Substantial\"\n          ],\n          [\n            \"Bias direction\",\n            \"gpt-5.4 slightly stricter\",\n            \"Reports ~3% more violations\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Judge calibration在best档下提供了measurement validity的gold standard。κ=0.807 > human inter-annotator κ=0.762的finding本身值得报告——LLM judges can be more reliable than individual human coders for this task。这使得paper的整个quantitative infrastructure（C1-C4）站在validated foundation上。cross-judge divergence（24%）已知且quantified——paper在Method中disclose并在Limitations中discuss。per-severity pattern（severe 91% > moderate 78% > none 95%）合理：borderline cases是genuinely hard for ANY coder。dream best-tier reviewers identified这为'single most critical missing validation'——现在resolved。\\n\\nbest档下human-LLM κ=0.807（strong agreement）验证了整个measurement chain。binary F1=0.92意味着LLM judge在violation detection上precision 94%（很少false positive）且recall 90%（漏检率10%——这些是borderline cases where human annotators also disagree）。human inter-annotator κ=0.762设定了agreement ceiling——LLM judge的0.807 actually exceeds human baseline，因为LLM judge is more consistent（less annotator fatigue/drift）。per-severity agreement在severe tier最高（0.91）因为clear-cut violations（e.g., unauthorized refund）easy to judge；moderate tier最低（0.78）因为borderline cases（e.g., partial compliance）genuinely ambiguous even for humans。cross-judge（gpt-4.1 vs gpt-5.4作为judges）κ=0.685（substantial）显示两个LLM judges mostly agree但有meaningful divergence on ~24% episodes——paper需disclose cross-judge asymmetry in Method。\"\n  },\n  {\n    \"name\": \"perturbation_control\",\n    \"description\": \"非歧义扰动对照：30 clause pairs（15 synonym substitution + 15 clause reordering）× 2 conditions × 2+ models = 120-300 episodes。区分ambiguity-specific harm vs general prompt brittleness。\",\n    \"results\": {\n      \"total_episodes\": 300,\n      \"delta_perturb_pp\": -0.67,\n      \"delta_perturb_ci\": \"[-8.0, 6.67]\",\n      \"ci_upper_bound\": 6.67,\n      \"ci_width_pp\": 14.67,\n      \"mcnemar_p\": 1.0,\n      \"ambiguity_delta_pp\": 34.0,\n      \"net_delta_pp\": 34.67,\n      \"ratio\": 0.0,\n      \"verdict\": \"PASS\",\n      \"synonym_delta_pp\": 1.33,\n      \"reorder_delta_pp\": -2.67\n    },\n    \"tables\": [\n      {\n        \"title\": \"Perturbation Control Results\",\n        \"columns\": [\n          \"Condition\",\n          \"Original Rate\",\n          \"Perturbed Rate\",\n          \"Delta (pp)\",\n          \"95% CI\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"Synonym substitution\",\n            \"40.0%\",\n            \"41.3%\",\n            \"+1.33\",\n            \"[-10.7, 13.3]\",\n            \"1.0\"\n          ],\n          [\n            \"Clause reordering\",\n            \"42.7%\",\n            \"40.0%\",\n            \"-2.67\",\n            \"[-14.7, 9.3]\",\n            \"0.82\"\n          ],\n          [\n            \"Combined perturbation\",\n            \"41.3%\",\n            \"40.7%\",\n            \"-0.67\",\n            \"[-8.0, 6.67]\",\n            \"1.0\"\n          ],\n          [\n            \"Ambiguity (reference)\",\n            \"4.4%\",\n            \"38.4%\",\n            \"+34.0\",\n            \"[31.2, 36.9]\",\n            \"<1e-100\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"5-Tier Verdict Assessment\",\n        \"columns\": [\n          \"Criterion\",\n          \"Threshold\",\n          \"Observed\",\n          \"Status\"\n        ],\n        \"rows\": [\n          [\n            \"Delta_perturb\",\n            \"<5pp (CI含0)\",\n            \"-0.67pp (CI含0)\",\n            \"PASS\"\n          ],\n          [\n            \"Ratio (perturb/ambiguity)\",\n            \"<0.15\",\n            \"0.0\",\n            \"PASS\"\n          ],\n          [\n            \"Net effect\",\n            \">20pp\",\n            \"+34.67pp\",\n            \"PASS\"\n          ],\n          [\n            \"Overall verdict\",\n            \"—\",\n            \"—\",\n            \"PASS (strongest form)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Perturbation control是C1因果claim的keystone evidence。PASS verdict使得paper可以声称'strongest causal evidence in the agent safety literature'——no prior work has both matched-pair AND perturbation control for agent policy ambiguity。ratio=0.0（perturbation effect is essentially zero）意味着all 34pp can be attributed to ambiguity。这也preempts RC11（prompt sensitivity confound）——最aggressive reviewer也难以challenge a 10:1 effect ratio with CI not overlapping。\\n\\nbest档下perturbation control产出PASS verdict——non-ambiguity surface changes（synonym substitution, clause reordering）cause zero meaningful effect（Δ=-0.67pp, CI含0）。这与ambiguity Δ=+34.0pp形成stark contrast：10:1 signal-to-noise ratio。PASS verdict意味着C1因果claim以最强形式成立——'+34pp是ambiguity-specific causation，不是general prompt sensitivity'。CI upper bound 6.67pp远低于WARNING阈值（15pp），net effect +34.67pp overwhelming。synonym substitution略positive（+1.33pp）和clause reordering略negative（-2.67pp）的差异在noise范围内（|Δ|<3pp），表明两种perturbation types equally benign。verdict=PASS使得paper可写'Perturbation control confirms that the observed +34pp effect is specific to ambiguity, not an artifact of surface-level policy modifications (synonym substitution: +1.33pp, clause reordering: -2.67pp, combined: -0.67pp, CI includes zero). This constitutes the strongest causal evidence for ambiguity-specific harm in the agent safety literature。'\"\n  },\n  {\n    \"name\": \"sopbench_cross_benchmark\",\n    \"description\": \"SOPBench跨基准C1复制：Healthcare + Bank domains，100 clause pairs（50/domain）× 2 conditions × 5 models = 1,000 episodes。Rule-based verifier替代LLM judge。验证C1 generalizability + C2 type ranking correlation。\",\n    \"results\": {\n      \"total_episodes\": 1000,\n      \"domains\": [\n        \"Healthcare\",\n        \"Bank\"\n      ],\n      \"types_covered\": [\n        \"incompleteness\",\n        \"auth_scope\",\n        \"lexical\",\n        \"conditional_precedence\"\n      ],\n      \"sopbench_c1_delta_pp\": 31.2,\n      \"sopbench_c1_or\": 12.8,\n      \"sopbench_c1_p\": 1e-38,\n      \"sopbench_c1_ci\": \"[27.0, 35.4]\",\n      \"sopbench_healthcare_delta_pp\": 33.8,\n      \"sopbench_bank_delta_pp\": 28.6,\n      \"sopbench_incompleteness_rate\": 0.56,\n      \"sopbench_auth_scope_rate\": 0.42,\n      \"sopbench_lexical_rate\": 0.38,\n      \"sopbench_cond_prec_rate\": 0.33,\n      \"sopbench_type_rank_rho\": 0.8,\n      \"sopbench_type_rank_p\": 0.042,\n      \"cross_benchmark_effect_correlation\": 0.89,\n      \"rule_based_vs_llm_agreement\": 0.91,\n      \"rule_based_verifier_advantage\": \"eliminates LLM-judge single dependency\",\n      \"per_model_sopbench\": {\n        \"gpt54_delta_pp\": 35.4,\n        \"gpt41_delta_pp\": 31.8,\n        \"claude_delta_pp\": 22.6,\n        \"qwen3_delta_pp\": 29.0,\n        \"deepseek_delta_pp\": 37.2\n      },\n      \"auth_scope_range_sopbench_pp\": 48,\n      \"incompleteness_range_sopbench_pp\": 14\n    },\n    \"tables\": [\n      {\n        \"title\": \"SOPBench C1 Replication Summary\",\n        \"columns\": [\n          \"Metric\",\n          \"τ²-bench (primary)\",\n          \"SOPBench (replication)\",\n          \"Agreement\"\n        ],\n        \"rows\": [\n          [\n            \"Delta (pp)\",\n            \"+34.0\",\n            \"+31.2\",\n            \"Within CI overlap\"\n          ],\n          [\n            \"Odds Ratio\",\n            \"15.1\",\n            \"12.8\",\n            \"Same order of magnitude\"\n          ],\n          [\n            \"p-value\",\n            \"<1e-100\",\n            \"<1e-38\",\n            \"Both highly significant\"\n          ],\n          [\n            \"Models replicating\",\n            \"5/5\",\n            \"5/5\",\n            \"Universal\"\n          ],\n          [\n            \"Domains\",\n            \"Retail + Airline\",\n            \"Healthcare + Bank\",\n            \"4 total (no overlap)\"\n          ],\n          [\n            \"Verifier\",\n            \"LLM judge\",\n            \"Rule-based\",\n            \"Independent methods\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"SOPBench Per-Model Results\",\n        \"columns\": [\n          \"Model\",\n          \"Amb Rate\",\n          \"Unamb Rate\",\n          \"Delta (pp)\",\n          \"p-value\",\n          \"τ²-bench Delta\"\n        ],\n        \"rows\": [\n          [\n            \"GPT-5.4\",\n            \"43.0%\",\n            \"7.6%\",\n            \"+35.4\",\n            \"<1e-10\",\n            \"+38.3\"\n          ],\n          [\n            \"DeepSeek\",\n            \"46.0%\",\n            \"8.8%\",\n            \"+37.2\",\n            \"<1e-11\",\n            \"+39.0\"\n          ],\n          [\n            \"GPT-4.1\",\n            \"38.4%\",\n            \"6.6%\",\n            \"+31.8\",\n            \"<1e-8\",\n            \"+34.7\"\n          ],\n          [\n            \"Qwen3\",\n            \"37.0%\",\n            \"8.0%\",\n            \"+29.0\",\n            \"<1e-7\",\n            \"+32.4\"\n          ],\n          [\n            \"Claude\",\n            \"28.0%\",\n            \"5.4%\",\n            \"+22.6\",\n            \"<1e-5\",\n            \"+25.7\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"SOPBench Type Ranking vs τ²-bench\",\n        \"columns\": [\n          \"Rank\",\n          \"τ²-bench Type\",\n          \"τ²-bench Rate\",\n          \"SOPBench Type\",\n          \"SOPBench Rate\"\n        ],\n        \"rows\": [\n          [\n            \"1\",\n            \"incompleteness\",\n            \"53.6%\",\n            \"incompleteness\",\n            \"56.0%\"\n          ],\n          [\n            \"2\",\n            \"auth_scope\",\n            \"41.6%\",\n            \"auth_scope\",\n            \"42.0%\"\n          ],\n          [\n            \"3\",\n            \"lexical\",\n            \"42.8%\",\n            \"lexical\",\n            \"38.0%\"\n          ],\n          [\n            \"4\",\n            \"cond_prec\",\n            \"36.8%\",\n            \"cond_prec\",\n            \"33.0%\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"SOPBench Per-Domain Results\",\n        \"columns\": [\n          \"Domain\",\n          \"Amb Rate\",\n          \"Unamb Rate\",\n          \"Delta (pp)\",\n          \"N Episodes\",\n          \"Top Risk Type\"\n        ],\n        \"rows\": [\n          [\n            \"Healthcare\",\n            \"41.2%\",\n            \"7.4%\",\n            \"+33.8\",\n            \"500\",\n            \"incompleteness (61%)\"\n          ],\n          [\n            \"Bank\",\n            \"35.0%\",\n            \"6.4%\",\n            \"+28.6\",\n            \"500\",\n            \"incompleteness (51%)\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Cross-Benchmark Convergence Evidence\",\n        \"columns\": [\n          \"Evidence\",\n          \"Value\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Type rank ρ (Spearman)\",\n            \"0.80\",\n            \"Strong positive correlation (p=0.042)\"\n          ],\n          [\n            \"Per-model effect correlation\",\n            \"0.89\",\n            \"Very strong — same model ordering\"\n          ],\n          [\n            \"Rule-based vs LLM judge agreement\",\n            \"91%\",\n            \"Independent verifiers converge\"\n          ],\n          [\n            \"Incompleteness #1 in both?\",\n            \"Yes\",\n            \"Universal highest-risk type\"\n          ],\n          [\n            \"auth_scope range (SOPBench)\",\n            \"48pp\",\n            \"Confirms model×type interaction\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SOPBench replication是best档与median/worst档的核心区分因素。Δ=31.2pp强复制（在[25,40] range内）将paper从'customer service domain finding'升级为'cross-domain generalization across 4 sectors'。rule-based verifier独立确认消除了LLM-judge single-dependency concern（审稿人最常见的methodological objection之一）。type ranking ρ=0.80显著相关证明incompleteness的#1 position不是τ²-bench artifact。cross-benchmark effect correlation r=0.89表明per-model vulnerability patterns是stable model properties而非benchmark-specific artifacts。Healthcare delta > Bank delta的差异本身is interesting——healthcare policies have higher stakes and more complex boundary conditions，可能amplify ambiguity effects。Main text加一段'Cross-Benchmark Replication: SOPBench (Healthcare + Bank) independently confirms the binary effect (Δ=31.2pp, OR=12.8, rule-based verifier) and type hierarchy (incompleteness > auth_scope > lexical > CP, ρ=0.80 with τ²-bench ranking). Effect generalizes across 4 domains, 2 benchmarks, and 2 verification methods.'即可。\\n\\nbest档下SOPBench强复制C1（Δ=31.2pp, p<1e-38）——效应略低于τ²-bench的34.0pp因为(a)不同domains（Healthcare/Bank vs retail/airline）有不同的policy complexity baseline，(b)rule-based verifier比LLM judge更严格（tends to under-count borderline violations），(c)SOPBench task structure（SOP execution vs customer service）对ambiguity的exposure pattern不同。但31.2pp仍在key metric range [25,40]内且OR=12.8 massive。type ranking correlation ρ=0.80（p=0.042, significant）确认incompleteness universally highest-risk——即使在完全不同的benchmark、不同的domains、不同的verifier下仍然排第一。cross-benchmark effect correlation r=0.89表示per-model effect sizes高度一致（Claude always lowest, DeepSeek always highest）。rule-based verifier与LLM judge 91% agreement消除了'LLM-as-judge single point of failure'的reviewer concern。Healthcare domain delta（33.8pp）> Bank domain（28.6pp）可能因为healthcare policies have more safety-critical boundary conditions。auth_scope range 48pp in SOPBench（vs 52pp in τ²-bench）independently confirms model×type interaction as robust finding。这些结果将paper从'retail/airline finding'升级为'cross-domain finding spanning 4 domains'。\"\n  },\n  {\n    \"name\": \"classifier_poc\",\n    \"description\": \"Binary ambiguity detector PoC：DeBERTa-v3-large在annotated clause pairs上fine-tune，5-fold CV评估。验证findings的practical applicability。\",\n    \"results\": {\n      \"binary_f1\": 0.81,\n      \"binary_precision\": 0.83,\n      \"binary_recall\": 0.79,\n      \"binary_fpr\": 0.044,\n      \"macro_f1\": 0.63,\n      \"best_type_f1_cp\": 0.94,\n      \"worst_type_f1_incomp\": 0.34,\n      \"per_type_f1\": {\n        \"conditional_precedence\": 0.94,\n        \"scopal\": 0.75,\n        \"coreferential\": 0.7,\n        \"authorization_scope\": 0.58,\n        \"lexical\": 0.39,\n        \"incompleteness\": 0.34\n      },\n      \"total_clauses\": 500,\n      \"folds\": 5,\n      \"gpu_hours\": 6.5\n    },\n    \"tables\": [\n      {\n        \"title\": \"DeBERTa Classifier Performance (5-fold CV)\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"Note\"\n        ],\n        \"rows\": [\n          [\n            \"Binary F1\",\n            \"0.81\",\n            \"Ambiguous vs unambiguous\"\n          ],\n          [\n            \"Binary Precision\",\n            \"0.83\",\n            \"Few false positives\"\n          ],\n          [\n            \"Binary Recall\",\n            \"0.79\",\n            \"Misses 21% (mostly incompleteness)\"\n          ],\n          [\n            \"Binary FPR\",\n            \"4.4%\",\n            \"Practical for deployment\"\n          ],\n          [\n            \"Macro F1 (6-type)\",\n            \"0.63\",\n            \"High variance across types\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Per-Type Classification Performance\",\n        \"columns\": [\n          \"Type\",\n          \"F1\",\n          \"Precision\",\n          \"Recall\",\n          \"Detection Difficulty\"\n        ],\n        \"rows\": [\n          [\n            \"conditional_precedence\",\n            \"0.94\",\n            \"0.92\",\n            \"0.96\",\n            \"Easy — explicit conflict markers\"\n          ],\n          [\n            \"scopal\",\n            \"0.75\",\n            \"0.78\",\n            \"0.72\",\n            \"Moderate — structural cues learnable\"\n          ],\n          [\n            \"coreferential\",\n            \"0.70\",\n            \"0.73\",\n            \"0.67\",\n            \"Moderate — pronoun/RC patterns\"\n          ],\n          [\n            \"authorization_scope\",\n            \"0.58\",\n            \"0.62\",\n            \"0.55\",\n            \"Hard — subtle boundary language\"\n          ],\n          [\n            \"lexical\",\n            \"0.39\",\n            \"0.42\",\n            \"0.36\",\n            \"Very hard — context-dependent polysemy\"\n          ],\n          [\n            \"incompleteness\",\n            \"0.34\",\n            \"0.38\",\n            \"0.31\",\n            \"Hardest — absence has no signal\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Classifier PoC在best档下scoped为appendix-level practical contribution，不overclaim为core contribution。binary F1=0.81 sufficient for'automated pre-screening tool that flags potentially ambiguous clauses for human review'的framing。per-type performance的inverse relationship with danger level（incompleteness: highest danger + lowest detectability）是a sobering practical finding——reinforces the need for domain experts in the loop, not just automated tools。PoC demonstrates that our taxonomy has practical discriminative power（types differ in surface detectability），but also that the most safety-critical type resists automated detection。\\n\\nbest档下DeBERTa PoC在binary detection达F1=0.81——足以demonstrate practical value但不overclaim。per-type F1的extreme variance（CP 0.94 vs incompleteness 0.34）本身是interesting finding：(a) CP最easy to detect因为explicit conflict markers（'but', 'however', 'unless'等surface cues）在training data中high-frequency，(b) incompleteness最hard因为absence of information has no surface signal——you can't detect what's NOT there from text features alone。这mirrors C2 type hierarchy in an unexpected way：most dangerous type（incompleteness）is also hardest to automatically detect，creating a dangerous blind spot。scopal（0.75）和coreferential（0.70）intermediate因为structural cues（quantifier scope, pronoun chains）are learnable but require syntactic understanding。auth_scope（0.58）moderate因为permission language有some surface patterns但boundary vagueness is subtle。macro F1=0.63 reflects per-type imbalance。binary FPR=0.044（<5%）意味着very few false alarms——practical for deployment as pre-filter。\"\n  }\n]",
      "numLines": 1609,
      "startLine": 1,
      "totalLines": 1609
    }
  },
  "sourceToolAssistantUUID": "c1c9062e-d967-4be0-8fc3-1c1f0e4811e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T111643 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguit…",
  "leafUuid": "8336972d-be85-4234-a6fa-0102ca227786",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for policy ambiguity safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830"
}
```

---

### Tool result

_source line 14 · 2026-05-22T11:34:49.466Z_

<details><summary>↩ Tool result · `toolu_011aAvVT33MLVcCQb2dpC1zu`</summary>

````text
1	# Paper Framing — policy_ambiguity_safety
2	
3	> 最后更新: 2026-05-20 19:30 UTC | 状态: 5-model analysis complete, C3/C4 framing revised
4	> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)
5	> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)
6	> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)
7	
8	## Core Insight
9	
10	Policy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.
11	
12	## Title (Working)
13	
14	"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families"
15	
16	Alternative: "Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents"
17	
18	Note: Pivoted from "Uniformly Nocuous" → "Specification-Layer Dominant" (2-model) → "Differential Nocuity with Model Interaction" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.
19	
20	## Core Claims
21	
22	### C1: Binary Effect (PRIMARY — confirmed, 5 models)
23	Ambiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.
24	- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].
25	- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.
26	- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.
27	- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.
28	- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.
29	
30	### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)
31	**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.
32	- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)
33	  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)
34	  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp
35	  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)
36	- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.
37	- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).
38	- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).
39	- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.
40	
41	### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)
42	**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.
43	- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].
44	- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: "suggestive" or "a moderate tendency," NOT "confirmed." Disclose within-judge non-significance in Limitations.
45	- **Per-model layer gaps** (THE KEY FINDING — feeds C4):
46	  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong
47	  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong
48	  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak
49	  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible
50	  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!
51	- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.
52	- **Framing decision**: C3 is NOT "spec-layer nearly twice as dangerous" (that was 2-model artifact). The correct framing is: "Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4)."
53	- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).
54	- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).
55	- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.
56	- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.
57	
58	### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)
59	**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.
60	- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.
61	  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%
62	  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.
63	- **Model × Type interaction matrix** (ambiguous condition, violation rates):
64	  ```
65	  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek
66	  authorization_scope     64%     46%      12%     26%     60%
67	  conditional_precedence  34%     36%      36%     40%     38%
68	  incompleteness          46%     58%      48%     62%     54%
69	  lexical                 42%     34%      32%     52%     54%
70	  coreferential           18%     32%      22%     42%     44%
71	  scopal                  42%     38%      32%     37%     48%
72	  ```
73	- **Key interaction patterns**:
74	  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.
75	  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.
76	  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.
77	  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.
78	- **Per-model type χ²** (which models show type-specific vulnerability patterns):
79	  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)
80	  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)
81	  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)
82	  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline
83	  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)
84	- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.
85	- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a "safety training blind spot" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.
86	- **Framing**: C4 from "models agree" → "Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality."
87	- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.
88	- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.
89	
90	### C5: Error Analysis (CONFIRMED — EMNLP core)
91	Different ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).
92	- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:
93	  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)
94	  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.
95	  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = "misparse"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = "active guessing" → explains higher violation rates
96	  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more "confident," act without hesitation)
97	  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)
98	  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity
99	  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse
100	- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).
101	  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to "dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)" instead of specific percentages; (5) Fine-grained 6-type as appendix with "automated coding" caveat.
102	  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from "moderate automated" to validated.
103	- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. "Ambiguity Blindness" upgraded from named concept to empirical finding with <5-11% awareness hard data.
104	
105	## Narrative Structure (CL-first for EMNLP)
106	
107	### Intro Logic Chain
108	1. Agent policies are written in NL → contain ambiguity (established)
109	2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact
110	3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.
111	4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?
112	5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.
113	6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a "safety training blind spot."
114	
115	### Section Map
116	- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)
117	- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R
118	- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R
119	- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation
120	- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)
121	- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.
122	- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).
123	- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.
124	
125	## Anticipated Reviewer Concerns
126	
127	### RC1: "Type effect could be artifact of taxonomy granularity"
128	**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).
129	
130	### RC2: "Taxonomy is ad hoc / why these 6 types"
131	**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).
132	
133	### RC3: "Only API models, no open-source"
134	**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.
135	**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.
136	
137	### RC4: "Synthetic ambiguity injection lacks ecological validity"
138	**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.
139	
140	### RC5: "τ²-bench limited to retail/airline"
141	**Response**: ✅ ADDRESSED (plan_017). Cross-benchmark replication on SOPBench (Li et al., 2025) — Healthcare + Bank domains, 100 clause pairs × 5 models = 1,000 episodes with rule-based verifier. If C1 replicates, paper moves from "customer service finding" to "cross-domain finding" spanning 4 domains (retail, airline, healthcare, banking). Result in Appendix with main-text summary. τ²-bench remains primary; SOPBench provides independent cross-domain confirmation.
142	
143	### RC6: "Binary effect is obvious — of course ambiguity causes errors"
144	**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.
145	
146	### RC7: "Incompleteness matched-pair confound (information asymmetry)"
147	**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.
148	
149	### RC8: "RC attachment in coreferential overlaps with scopal / structural ambiguity"
150	**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.
151	
152	### RC9: "authorization_scope is just a subtype of incompleteness"
153	**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., "authorized personnel" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.
154	
155	### RC10: "API sampling noise undermines reliability"
156	**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.
157	
158	### RC11: "Prompt sensitivity confound" [Dream A9 — best tier "strongest point"]
159	**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.
160	**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.
161	
162	## Concept Naming (distill insight: 命名即贡献)
163	
164	Core phenomenon: **"Differential Nocuity"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.
165	
166	Secondary phenomenon: **"Ambiguity Blindness"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.
167	
168	Tertiary phenomenon: **"Disambiguation Channel Framework"** [renamed from "Hypothesis" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).
169	
170	Quaternary phenomenon: **"Systematic Nocuity"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears "correct" until compared against ground truth. Proposed as B&K extension in Discussion.
171	
172	## Opening Hook Strategy (distill insight: 具体案例, 不要 "Recently...")
173	
174	Open with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says "items may be returned within 30 days" (scopal: "items" scopes over all categories including custom). The unambiguous version specifies "standard items only" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.
175	
176	## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)
177	
178	"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones."
179	
180	## Benchmark Comparison Table (distill insight: 必有 feature matrix)
181	
182	| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |
183	|---------|--------|---------------|------------|----------|----------|
184	| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |
185	| Causal design | — | — | — | — | **matched pairs** |
186	| Safety violation metric | — | binary | — | procedural | **3-tier severity** |
187	| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |
188	| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |
189	| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |
190	
191	## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]
192	
193	1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.
194	2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.
195	3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity ("Ambiguity Blindness"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.
196	
197	NOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. "Disambiguation channel" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.
198	
199	## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]
200	
201	Current plan has thin references. Must add (≥25 total in final paper):
202	- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.
203	- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.
204	- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)
205	- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.
206	- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) "Ambiguity" encyclopedia entry.
207	- **Surprisal/expectation-based**: Levy (2008); Hale (2001)
208	- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)
209	- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)
210	- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent
211	- **Formal semantics of vagueness**: Lassiter & Goodman (2017)
212	- **Garden-path**: Frazier & Rayner (1982)
213	- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)
214	- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份
215	
216	## Code/Data Release Plan [Dream A6 — three-tier consistent]
217	
218	Must commit to releasing:
219	1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels
220	2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)
221	3. Statistical analysis code (all tests, bootstrap CI computation)
222	4. Agent trace samples (anonymized) for reproducibility of C5
223	
224	## Figure Plan [Dream A12]
225	
226	Minimum figures for paper (zero-figure paper flagged in dream):
227	1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)
228	2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)
229	3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)
230	4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)
231	5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)
232	6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)
233	7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)
234	
235	## Berry & Kamsties Operationalization Note [Dream best Q5]
236	
237	Berry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.
238	
239	## Contingency Framing [RESOLVED — Scenario C occurred]
240	
241	> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。
242	> Framing 已 pivot 到 "Differential Nocuity" + "Layer Hierarchy" (D020)。本节仅保留历史记录。
243	
244	## Claude Baseline — RESOLVED [2026-05-20]
245	
246	✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).
247	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "fd898afb-216c-4575-ae1c-c54cfc9120e4",
  "isSidechain": false,
  "promptId": "d65c2e8d-79bc-4128-97c7-582868b89531",
  "type": "user",
  "uuid": "8f1eb2b7-023f-4f83-821b-040a6f45aa3e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/paper_framing.md",
      "content": "# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-20 19:30 UTC | 状态: 5-model analysis complete, C3/C4 framing revised\n> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)\n> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)\n> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)\n\n## Core Insight\n\nPolicy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.\n\n## Title (Working)\n\n\"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\"\n\nAlternative: \"Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents\"\n\nNote: Pivoted from \"Uniformly Nocuous\" → \"Specification-Layer Dominant\" (2-model) → \"Differential Nocuity with Model Interaction\" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed, 5 models)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.\n- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].\n- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.\n- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.\n- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.\n- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.\n\n### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)\n**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.\n- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)\n  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)\n  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp\n  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)\n- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.\n- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).\n- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).\n- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.\n\n### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)\n**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.\n- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].\n- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: \"suggestive\" or \"a moderate tendency,\" NOT \"confirmed.\" Disclose within-judge non-significance in Limitations.\n- **Per-model layer gaps** (THE KEY FINDING — feeds C4):\n  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong\n  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong\n  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak\n  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible\n  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!\n- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.\n- **Framing decision**: C3 is NOT \"spec-layer nearly twice as dangerous\" (that was 2-model artifact). The correct framing is: \"Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4).\"\n- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).\n- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).\n- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.\n- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.\n\n### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)\n**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.\n- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.\n  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%\n  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.\n- **Model × Type interaction matrix** (ambiguous condition, violation rates):\n  ```\n  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek\n  authorization_scope     64%     46%      12%     26%     60%\n  conditional_precedence  34%     36%      36%     40%     38%\n  incompleteness          46%     58%      48%     62%     54%\n  lexical                 42%     34%      32%     52%     54%\n  coreferential           18%     32%      22%     42%     44%\n  scopal                  42%     38%      32%     37%     48%\n  ```\n- **Key interaction patterns**:\n  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.\n  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.\n  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.\n  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.\n- **Per-model type χ²** (which models show type-specific vulnerability patterns):\n  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)\n  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)\n  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)\n  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline\n  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)\n- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.\n- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a \"safety training blind spot\" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.\n- **Framing**: C4 from \"models agree\" → \"Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality.\"\n- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.\n- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.\n\n### C5: Error Analysis (CONFIRMED — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).\n- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:\n  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)\n  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.\n  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = \"misparse\"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = \"active guessing\" → explains higher violation rates\n  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more \"confident,\" act without hesitation)\n  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)\n  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity\n  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse\n- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).\n  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to \"dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)\" instead of specific percentages; (5) Fine-grained 6-type as appendix with \"automated coding\" caveat.\n  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from \"moderate automated\" to validated.\n- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. \"Ambiguity Blindness\" upgraded from named concept to empirical finding with <5-11% awareness hard data.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?\n5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.\n6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a \"safety training blind spot.\"\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R\n- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation\n- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.\n- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).\n- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Type effect could be artifact of taxonomy granularity\"\n**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.\n**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: ✅ ADDRESSED (plan_017). Cross-benchmark replication on SOPBench (Li et al., 2025) — Healthcare + Bank domains, 100 clause pairs × 5 models = 1,000 episodes with rule-based verifier. If C1 replicates, paper moves from \"customer service finding\" to \"cross-domain finding\" spanning 4 domains (retail, airline, healthcare, banking). Result in Appendix with main-text summary. τ²-bench remains primary; SOPBench provides independent cross-domain confirmation.\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"RC attachment in coreferential overlaps with scopal / structural ambiguity\"\n**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.\n\n### RC9: \"authorization_scope is just a subtype of incompleteness\"\n**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., \"authorized personnel\" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.\n\n### RC10: \"API sampling noise undermines reliability\"\n**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.\n\n### RC11: \"Prompt sensitivity confound\" [Dream A9 — best tier \"strongest point\"]\n**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.\n**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.\n\n## Concept Naming (distill insight: 命名即贡献)\n\nCore phenomenon: **\"Differential Nocuity\"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.\n\nSecondary phenomenon: **\"Ambiguity Blindness\"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.\n\nTertiary phenomenon: **\"Disambiguation Channel Framework\"** [renamed from \"Hypothesis\" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).\n\nQuaternary phenomenon: **\"Systematic Nocuity\"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears \"correct\" until compared against ground truth. Proposed as B&K extension in Discussion.\n\n## Opening Hook Strategy (distill insight: 具体案例, 不要 \"Recently...\")\n\nOpen with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says \"items may be returned within 30 days\" (scopal: \"items\" scopes over all categories including custom). The unambiguous version specifies \"standard items only\" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.\n\n## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)\n\n\"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones.\"\n\n## Benchmark Comparison Table (distill insight: 必有 feature matrix)\n\n| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |\n|---------|--------|---------------|------------|----------|----------|\n| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |\n| Causal design | — | — | — | — | **matched pairs** |\n| Safety violation metric | — | binary | — | procedural | **3-tier severity** |\n| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |\n| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |\n| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |\n\n## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]\n\n1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.\n2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.\n3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity (\"Ambiguity Blindness\"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.\n\nNOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. \"Disambiguation channel\" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.\n\n## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]\n\nCurrent plan has thin references. Must add (≥25 total in final paper):\n- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.\n- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.\n- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)\n- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.\n- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) \"Ambiguity\" encyclopedia entry.\n- **Surprisal/expectation-based**: Levy (2008); Hale (2001)\n- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)\n- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)\n- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent\n- **Formal semantics of vagueness**: Lassiter & Goodman (2017)\n- **Garden-path**: Frazier & Rayner (1982)\n- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)\n- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份\n\n## Code/Data Release Plan [Dream A6 — three-tier consistent]\n\nMust commit to releasing:\n1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels\n2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)\n3. Statistical analysis code (all tests, bootstrap CI computation)\n4. Agent trace samples (anonymized) for reproducibility of C5\n\n## Figure Plan [Dream A12]\n\nMinimum figures for paper (zero-figure paper flagged in dream):\n1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)\n2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)\n3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)\n4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)\n5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)\n6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)\n7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)\n\n## Berry & Kamsties Operationalization Note [Dream best Q5]\n\nBerry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.\n\n## Contingency Framing [RESOLVED — Scenario C occurred]\n\n> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。\n> Framing 已 pivot 到 \"Differential Nocuity\" + \"Layer Hierarchy\" (D020)。本节仅保留历史记录。\n\n## Claude Baseline — RESOLVED [2026-05-20]\n\n✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).\n",
      "numLines": 247,
      "startLine": 1,
      "totalLines": 247
    }
  },
  "sourceToolAssistantUUID": "fd898afb-216c-4575-ae1c-c54cfc9120e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T111643 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguit…",
  "leafUuid": "8f1eb2b7-023f-4f83-821b-040a6f45aa3e",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for policy ambiguity safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830"
}
```

---

### Assistant

_source line 17 · 2026-05-22T11:34:58.690Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me also load the paper-writing-norms skill since this is a paper writing task.

Let me now write the full LaTeX paper. I need to:

1. Cover all experiments from experiment_data.json
2. Follow the narrative guidance and paper_framing.md
3. Target EMNLP 2026 format (8-page main text limit)
4. Include Abstract, Introduction, Method, Experiments/Results, Analysis, Discussion, Conclusion
5. Cover all claims C1-C5

Let me first check if the directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f1eb2b7-023f-4f83-821b-040a6f45aa3e",
  "isSidechain": false,
  "requestId": "req_011CbHY6Nj1geWRXVbXejtmL",
  "type": "assistant",
  "uuid": "4668c3dd-e428-4f9f-a6f9-4f63c378cf47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PkcTUWb4eGsWn2pa9yves",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31682,
      "cache_read_input_tokens": 24241,
      "output_tokens": 355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31682,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 355,
          "cache_read_input_tokens": 24241,
          "cache_creation_input_tokens": 31682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31682
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

_source line 18 · 2026-05-22T11:34:59.309Z_

Now let me check the target directory and load the paper-writing-norms skill.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4668c3dd-e428-4f9f-a6f9-4f63c378cf47",
  "isSidechain": false,
  "requestId": "req_011CbHY6Nj1geWRXVbXejtmL",
  "type": "assistant",
  "uuid": "8547cc90-1c55-4175-ad48-fe3f0982ac32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PkcTUWb4eGsWn2pa9yves",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31682,
      "cache_read_input_tokens": 24241,
      "output_tokens": 355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31682,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 355,
          "cache_read_input_tokens": 24241,
          "cache_creation_input_tokens": 31682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31682
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

_source line 19 · 2026-05-22T11:35:02.199Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014moD5JksUjC3ZZHoJuQPqv`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8547cc90-1c55-4175-ad48-fe3f0982ac32",
  "isSidechain": false,
  "requestId": "req_011CbHY6Nj1geWRXVbXejtmL",
  "type": "assistant",
  "uuid": "93ebaa69-3494-4928-a518-c45d2ecf46b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PkcTUWb4eGsWn2pa9yves",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31682,
      "cache_read_input_tokens": 24241,
      "output_tokens": 355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31682,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 355,
          "cache_read_input_tokens": 24241,
          "cache_creation_input_tokens": 31682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31682
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

_source line 20 · 2026-05-22T11:35:02.718Z_

<details><summary>↩ Tool result · `toolu_01DvWJoriAJ57HUGbiZuctJt`</summary>

````text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "175a2916-97a6-4084-be04-0bb449637732",
  "isSidechain": false,
  "promptId": "d65c2e8d-79bc-4128-97c7-582868b89531",
  "type": "user",
  "uuid": "ad9da02d-a0f3-4c9d-adbb-88d06882587c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "175a2916-97a6-4084-be04-0bb449637732",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Tool result

_source line 21 · 2026-05-22T11:35:02.355Z_

<details><summary>↩ Tool result · `toolu_014moD5JksUjC3ZZHoJuQPqv`</summary>

```text
experiment_data.json
imagined_experiments.yaml
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93ebaa69-3494-4928-a518-c45d2ecf46b1",
  "isSidechain": false,
  "promptId": "d65c2e8d-79bc-4128-97c7-582868b89531",
  "type": "user",
  "uuid": "200158c9-c665-4c63-b517-dfac28d4e16f",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "93ebaa69-3494-4928-a518-c45d2ecf46b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T11:35:02.712Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DvWJoriAJ57HUGbiZuctJt`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "200158c9-c665-4c63-b517-dfac28d4e16f",
  "isSidechain": false,
  "requestId": "req_011CbHY6Nj1geWRXVbXejtmL",
  "type": "assistant",
  "uuid": "175a2916-97a6-4084-be04-0bb449637732",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PkcTUWb4eGsWn2pa9yves",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31682,
      "cache_read_input_tokens": 24241,
      "output_tokens": 355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31682,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 355,
          "cache_read_input_tokens": 24241,
          "cache_creation_input_tokens": 31682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31682
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

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T111643 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguit…",
  "leafUuid": "ad9da02d-a0f3-4c9d-adbb-88d06882587c",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for policy ambiguity safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830"
}
```

---

### Assistant

_source line 25 · 2026-05-22T11:35:36.817Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have everything I need. Let me write the full LaTeX paper. Key considerations:

1. EMNLP 2026 format (8-page main text, acl style)
2. Cover all 11 experiments from experiment_data.json
3. Follow the narrative guidance and paper framing
4. No em-dashes (AI style marker)
5. Use booktabs for tables
6. Claims: C1 (binary effect), C2 (type hierarchy), C3 (layer effect), C4 (model×type interaction), C5 (error analysis)


7. Mapping the experiments across sections: the clause generation study and mini pilot go in methods, the API and open-source results form the main findings, statistical analysis validates all claims, error analysis provides qualitative support, and reliability and realism tests strengthen the methodology.

8. Organizing the paper structure with abstract, introduction, related work, the taxonomy framework, detailed methods including the matched-pair design and evaluation approach, comprehensive results section covering all claims plus perturbation control and cross-benchmark validation, error analysis, discussion, conclusion, limitations, and appendix materials for the classifier proof-of-concept and supplementary validation studies.

9. Now I need to determine what goes where—the classifier application and mini-pilot belong in the appendix, while the main narrative flows through taxonomy definition, methodological validation, empirical results, and qualitative analysis.

10. Checking the available resources for the LaTeX setup—I see acl.sty and acl_natbib.bst are already in the docs/paper directory, so I can use the ACL format directly for EMNLP 2026 compliance rather than falling back to a generic article class.

Now I'm planning out the key tables I need to include: the clause distribution breakdown, binary effect summaries across the five models, the type hierarchy structure, model-by-type interactions, perturbation control validation, and cross-benchmark replication results from SOPBench.

Then I'll add the failure mode signatures and ambiguity metrics tables, followed by appendix tables covering reliability measures, judge calibration, realism validation, the classifier proof-of-concept, pilot results, and the statistical breakdowns by model and layer.

I need to be careful about formatting constraints like avoiding em-dashes and keeping the LaTeX clean and compilable.

Writing the paper now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad9da02d-a0f3-4c9d-adbb-88d06882587c",
  "isSidechain": false,
  "requestId": "req_011CbHY7MX7HbgkR7oU4uKih",
  "type": "assistant",
  "uuid": "4e3c4b5b-9217-4b5f-a02e-765981b06ee3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D85Rf9mAgjv5vo3okUuLGe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5919,
      "cache_read_input_tokens": 55923,
      "output_tokens": 15569,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5919,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15569,
          "cache_read_input_tokens": 55923,
          "cache_creation_input_tokens": 5919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5919
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

_source line 26 · 2026-05-22T11:35:36.822Z_

Now I'll write the complete LaTeX paper. This covers all 11 experiments across the appropriate sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e3c4b5b-9217-4b5f-a02e-765981b06ee3",
  "isSidechain": false,
  "requestId": "req_011CbHY7MX7HbgkR7oU4uKih",
  "type": "assistant",
  "uuid": "9dc2b79f-85cb-4a36-acc1-bc4b85391248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D85Rf9mAgjv5vo3okUuLGe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5919,
      "cache_read_input_tokens": 55923,
      "output_tokens": 15569,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5919,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15569,
          "cache_read_input_tokens": 55923,
          "cache_creation_input_tokens": 5919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5919
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

_source line 27 · 2026-05-22T11:40:21.324Z_

<details open><summary>🔧 Tool call — Write · `toolu_01AuPHaVtWCAZeCrHaF9eQPu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\aclfinalcopy\n\n\\title{Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWhen a customer service policy states that ``authorized personnel may process returns,'' a human agent draws on organizational context to resolve the vague permission boundary. Large Language Model (LLM) agents lack this context and must guess. We present the first causal, type-granular, cross-model study of how policy ambiguity drives safety violations in LLM agents. Using a matched-pair design with 300 clause pairs spanning six ambiguity types and a two-layer taxonomy (specification vs.\\ linguistic), we evaluate five architecturally diverse models across 2,997 episodes on the $\\tau^2$-bench framework. Ambiguous policies cause a +34.0 percentage point (pp) increase in safety violations (OR=15.1, $p<10^{-100}$), replicated across all five models. A perturbation control confirms this effect is ambiguity-specific ($\\Delta_\\text{perturb}=-0.67$pp). Beyond this universal effect, we find a significant model $\\times$ type interaction: authorization scope vulnerability ranges 52pp across models (12\\% for Claude to 64\\% for GPT-5.4), while incompleteness remains universally dangerous (46--62\\%). Cross-benchmark replication on SOPBench across healthcare and banking domains independently confirms the binary effect ($\\Delta=31.2$pp, rule-based verifier). Error analysis of 300 violation traces reveals type-specific failure signatures and pervasive ``ambiguity blindness'' ($<$5\\% awareness rate). These findings establish \\textit{differential nocuity} as a framework connecting Berry \\& Kamsties' ambiguity theory to modern safety alignment.\n\\end{abstract}\n\n\\section{Introduction}\n\nA retail policy states: ``Items purchased with a promotional discount may be exchanged within 14 days.'' An LLM agent interprets ``items'' as covering all categories, including custom orders, and processes a \\$200 return with free shipping. The unambiguous variant specifies ``standard catalog items only,'' and the same agent correctly declines. One word of ambiguity produces an unauthorized refund.\n\nThis scenario is not hypothetical. As LLM agents are deployed in customer-facing, healthcare, and financial settings, they operate under natural language policy specifications that inevitably contain ambiguity \\cite{berry2003ambiguity,massey2014identifying}. Human agents resolve such ambiguity through shared organizational context, training, and escalation norms. LLM agents lack these disambiguation channels and must act under uncertainty.\n\nPrior work has established taxonomies of policy ambiguity in requirements engineering \\cite{berry2003ambiguity,massey2014identifying} and NLP \\cite{li2024ambiguity}. Recent benchmarks evaluate agent safety under policy specifications \\cite{yao2024tau2bench,li2025sopbench}, and several studies probe agent robustness to adversarial or underspecified instructions \\cite{ruan2024toolemu,zhou2023ifeval}. However, no prior work provides \\textit{causal, type-granular} evidence linking specific ambiguity types to safety violation rates, nor examines how this relationship varies across model families.\n\nWe address this gap with three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Causal quantification.} A matched-pair design with perturbation control isolates ambiguity as the causal driver of safety violations. The effect is massive: +34.0pp (OR=15.1) across five architecturally diverse models, with perturbation controls confirming specificity ($\\Delta_\\text{perturb}=-0.67$pp). This constitutes the strongest causal evidence for ambiguity-specific harm in the agent safety literature.\n\n\\item \\textbf{Differential nocuity and model $\\times$ type interaction.} We introduce a two-layer, six-type ambiguity taxonomy and show that types form a three-tier risk hierarchy (incompleteness $>$ mid-cluster $>$ coreferential). The deeper finding is a significant model $\\times$ type interaction: authorization scope vulnerability spans 52pp across models, while incompleteness remains universally dangerous (46--62\\%), revealing that safety training differentially mitigates specific ambiguity types.\n\n\\item \\textbf{Type-specific failure modes and ambiguity blindness.} Qualitative analysis of 300 violation traces uncovers type-diagnostic failure signatures (specification-layer: guess-and-act; linguistic-layer: misparse-and-apply) and documents that agents exhibit $<$5\\% awareness of encountered ambiguity, with $>$88\\% surface interpretation adoption.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Ambiguity in requirements engineering.}\nBerry and Kamsties \\shortcite{berry2003ambiguity} distinguish \\textit{nocuous} ambiguity (causing divergent interpretations among stakeholders) from \\textit{innocuous} ambiguity (where interpretations converge). Massey et al.\\ \\shortcite{massey2014identifying} develop a six-type classification for privacy policy ambiguity. Chantree et al.\\ \\shortcite{chantree2006identifying} build the first computational nocuous ambiguity detector. Ferrari et al.\\ \\shortcite{ferrari2017detecting} extend NLP-based ambiguity detection to cross-domain requirements. Willis et al.\\ \\shortcite{willis2008automatic} and Ezzini et al.\\ \\shortcite{ezzini2022taphsir} automate ambiguity identification in software requirements. Our work operationalizes nocuity in the context of LLM agent safety, extending Berry \\& Kamsties' binary framework to a differential model.\n\n\\paragraph{LLM ambiguity processing.}\nLinguistic studies show that LLMs exhibit garden-path effects \\cite{frazier1982making,li2024gardenpath} and process ambiguity differently from humans \\cite{levy2008expectation,ferreira2002good}. Poesio and Artstein \\shortcite{poesio2005annotating} study anaphoric ambiguity annotation, and Lassiter and Goodman \\shortcite{lassiter2017adjectival} formalize vagueness in formal semantics. Our taxonomy draws on Li et al.\\ \\shortcite{li2024ambiguity}, who classify eleven NLP ambiguity types, and the DRIP-R benchmark \\cite{li2024dripr}, which measures model disagreement across five requirement ambiguity types but does not link disagreement to safety violations.\n\n\\paragraph{Agent safety evaluation.}\n$\\tau^2$-bench \\cite{yao2024tau2bench} and SOPBench \\cite{li2025sopbench} evaluate agent policy compliance. ToolEmu \\cite{ruan2024toolemu} and R-Judge \\cite{yuan2024rjudge} assess tool-use safety. InjecAgent \\cite{zhan2024injecagent} tests prompt injection. PolicyBank \\cite{chen2024policybank} classifies three types of policy gaps. IFEval \\cite{zhou2023ifeval} and ToolBench \\cite{qin2024toolbench} measure instruction-following robustness. Studies on prompt sensitivity \\cite{sclar2024quantifying,lu2022fantastically} show that surface-level perturbations affect model behavior. Unlike these works, we provide matched-pair causal evidence at type granularity, distinguishing ambiguity-specific effects from general prompt sensitivity.\n\n\\section{Ambiguity Taxonomy}\n\nWe adopt a two-layer taxonomy of policy ambiguity grounded in the intersection of NLP ambiguity classification \\cite{li2024ambiguity} and requirements engineering typologies \\cite{massey2014identifying,berry2003ambiguity}.\n\n\\paragraph{Specification layer.} These types arise from what the policy says (or fails to say) about domain-specific rules, not from grammatical structure. They cannot be resolved by linguistic analysis alone.\n\n\\begin{itemize}\n\\item \\textbf{Authorization scope}: Permission boundaries are stated but vague (e.g., ``authorized personnel may process returns'' without specifying which functions).\n\\item \\textbf{Incompleteness}: Conditions, exceptions, or boundaries are missing entirely (e.g., a return policy that omits the handling of opened electronics).\n\\item \\textbf{Conditional precedence}: Two or more rules apply to the same situation with conflicting outcomes (e.g., ``all items are returnable'' vs.\\ ``custom orders are final sale'').\n\\end{itemize}\n\n\\paragraph{Linguistic layer.} These types arise from the grammatical or lexical structure of policy language and can, in principle, be resolved through careful linguistic analysis.\n\n\\begin{itemize}\n\\item \\textbf{Scopal}: Quantifier, negation, or modal scope is unclear (e.g., ``customers may not return items purchased during the sale'' admits two scope readings).\n\\item \\textbf{Lexical}: A word has multiple contextually plausible senses (e.g., ``charge'' meaning financial charge vs.\\ battery charge in a device return policy).\n\\item \\textbf{Coreferential}: Pronouns or relative clauses have ambiguous antecedents (e.g., ``the manager approved the refund for the customer who complained'' admits two relative clause attachments).\n\\end{itemize}\n\nThis taxonomy maps onto prior work: our specification layer aligns with Massey et al.'s domain-specific categories, while the linguistic layer draws on Li et al.'s syntactic and lexical types. We provide a full cross-walk with DRIP-R's five types in Appendix~\\ref{app:crosswalk}.\n\n\\section{Method}\n\n\\subsection{Matched-Pair Design}\n\nFor each of 300 policy clauses, we construct an \\textit{ambiguous} variant and a matched \\textit{unambiguous} variant, differing only in the ambiguity-bearing element. This matched-pair design isolates ambiguity as the causal variable while controlling for clause content, domain, and task structure. Table~\\ref{tab:clause_dist} shows the distribution across types and domains.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Clause distribution by type, layer, and domain. Token delta measures the number of tokens added to create the unambiguous variant.}\n\\label{tab:clause_dist}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{Retail} & \\textbf{Airline} & \\textbf{$\\Delta$ Tok.} \\\\\n\\midrule\nauth\\_scope & Spec. & 25 & 25 & 36.1 \\\\\ncond\\_prec & Spec. & 25 & 25 & 28.4 \\\\\nincompleteness & Spec. & 25 & 25 & 34.6 \\\\\nscopal & Ling. & 25 & 25 & 14.2 \\\\\nlexical & Ling. & 25 & 25 & 12.8 \\\\\ncoreferential & Ling. & 25 & 25 & 7.8 \\\\\n\\midrule\n\\textbf{Total} & & \\textbf{150} & \\textbf{150} & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nClause generation followed an iterative process: pilot clauses (10 per type) were validated through the experimental pipeline, then expanded to 50 per type using real policy document templates. Each clause underwent Chantree-style quality validation \\cite{chantree2006identifying}, achieving a 98\\% pass rate. Token deltas were balanced within type (CV=0.18) and across types ($\\chi^2$ balance $p=0.72$). Conditional precedence clauses used a mix of labeled (40\\%) and unlabeled (60\\%) conflict formats to increase ecological validity. Mean Flesch-Kincaid grade level was 11.8 ($\\pm$2.1), consistent with professional policy language.\n\n\\subsection{Ecological Validity}\n\nTo validate that our synthetic ambiguity injection preserves the properties of naturally occurring policy ambiguity, we compared clause distributions against DRIP-R's corpus of natural ambiguities using Kolmogorov-Smirnov tests (Table~\\ref{tab:realism}). No significant differences were found across four linguistic properties (all $p > 0.15$). A trained discriminator achieved only 56\\% accuracy (95\\% CI: [48\\%, 64\\%], containing chance), confirming distributional equivalence.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ecological validity: synthetic clauses vs.\\ DRIP-R natural ambiguities. No significant distributional differences.}\n\\label{tab:realism}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Property} & \\textbf{Ours} & \\textbf{DRIP-R} & \\textbf{KS $p$} \\\\\n\\midrule\nSentence length & 22.4$\\pm$6.2 & 21.8$\\pm$7.1 & 0.34 \\\\\nParse depth & 5.3$\\pm$1.4 & 5.6$\\pm$1.6 & 0.21 \\\\\nFlesch-Kincaid & 11.8$\\pm$2.1 & 12.3$\\pm$2.4 & 0.48 \\\\\nType-token ratio & 0.82$\\pm$0.06 & 0.80$\\pm$0.07 & 0.15 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Models and Evaluation}\n\nWe evaluate five architecturally diverse models: GPT-5.4 and GPT-4.1 (proprietary dense), Claude Sonnet 4.6 (proprietary dense), Qwen3-235B (open-source MoE, 22B active), and DeepSeek-V3 (open-source MoE, 37B active). Each model processes all 300 clause pairs under both conditions, yielding 2,997 total episodes (3 API models $\\times$ 600 + 2 open-source models $\\times$ 600, with 3 episodes lost to API errors).\n\nEvaluation uses cross-judge LLM assessment: GPT-4.1 judges GPT-5.4 and DeepSeek; GPT-5.4 judges GPT-4.1, Claude, and Qwen3. Each episode receives a three-tier severity label (severe violation, moderate violation, no violation), collapsed to binary (violation/no-violation) for primary analysis. Cross-judge agreement is $\\kappa=0.74$ (substantial).\n\n\\paragraph{Judge calibration.}\nWe validated the LLM judge against human annotation on 100 stratified episodes coded by two human annotators (Table~\\ref{tab:judge_cal}). Human-LLM binary $\\kappa=0.87$ (strong) with F1=0.92, exceeding human inter-annotator $\\kappa=0.762$. The LLM judge is more consistent than individual human coders, with disagreements concentrated at moderate-severity boundaries (78\\% agreement) rather than clear violations (91\\%) or clean episodes (95\\%).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Judge calibration: human-LLM agreement on 100 stratified episodes. LLM judge agreement exceeds human inter-annotator baseline.}\n\\label{tab:judge_cal}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Interp.} \\\\\n\\midrule\nHuman-LLM binary $\\kappa$ & 0.87 & Strong \\\\\nHuman-LLM binary F1 & 0.92 & High \\\\\nPrecision / Recall & 0.94 / 0.90 & Balanced \\\\\nHuman inter-annot.\\ $\\kappa$ & 0.762 & Ceiling \\\\\nCross-judge $\\kappa$ (weighted) & 0.685 & Substantial \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Perturbation Control}\n\nTo distinguish ambiguity-specific effects from general prompt sensitivity, we constructed 30 clause pairs with non-ambiguity surface perturbations: 15 synonym substitutions and 15 clause reorderings. These pairs were evaluated under the same conditions as the main study (300 episodes total). Results appear in Section~\\ref{sec:perturbation}.\n\n\\section{Results}\n\n\\subsection{C1: Universal Binary Effect}\n\\label{sec:c1}\n\nAmbiguous policy specifications cause massive increases in safety violation rates across all five models (Table~\\ref{tab:c1}). The pooled effect is +34.0pp (bootstrap 95\\% CI: [31.2, 36.9]), with an odds ratio of 15.1 (CI: [10.78, 21.17]) and McNemar $p < 10^{-100}$. Every model individually replicates the effect with $p < 10^{-17}$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{C1: Binary effect across five models. All models show massive violation rate increases under ambiguous policies.}\n\\label{tab:c1}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} & \\textbf{OR [95\\% CI]} \\\\\n\\midrule\nGPT-5.4 & 41.0\\% & 2.7\\% & +38.3 & 25.3 [14.8, 43.2] \\\\\nDeepSeek-V3 & 49.7\\% & 10.7\\% & +39.0 & 8.3 \\\\\nGPT-4.1 & 40.7\\% & 6.0\\% & +34.7 & 10.9 [7.1, 16.6] \\\\\nQwen3-235B & 43.1\\% & 10.7\\% & +32.4 & 6.4 \\\\\nClaude S-4.6 & 30.3\\% & 4.7\\% & +25.7 & 8.9 [5.5, 14.5] \\\\\n\\midrule\n\\textbf{Pooled} & \\textbf{37.3\\%} & \\textbf{4.4\\%} & \\textbf{+34.0} & \\textbf{15.1 [10.8, 21.2]} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLogistic regression confirms ambiguity as the dominant predictor even after controlling for token delta, model, and type (condition coefficient = 2.278, $z=19.65$, $p<0.001$). Token delta is a significant but secondary predictor (coefficient = 0.022, $z=3.49$, $p=0.0005$), suggesting that specification-layer clauses, which require more tokens to disambiguate, are partly more dangerous because they contain more missing information.\n\n\\subsection{Perturbation Control: Ambiguity-Specific Causation}\n\\label{sec:perturbation}\n\nNon-ambiguity surface modifications produce no meaningful effect (Table~\\ref{tab:perturb}). Synonym substitution causes +1.33pp ($p=1.0$) and clause reordering causes $-2.67$pp ($p=0.82$). The combined perturbation effect is $-0.67$pp (95\\% CI: [$-8.0$, 6.67], containing zero). Against the ambiguity effect of +34.0pp, the ratio of perturbation-to-ambiguity effect is 0.0, passing all causal attribution criteria.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation control: non-ambiguity surface changes cause zero meaningful effect, confirming ambiguity-specific causation.}\n\\label{tab:perturb}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{$\\Delta$pp} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nSynonym subst. & +1.33 & [$-$10.7, 13.3] & 1.0 \\\\\nClause reorder & $-$2.67 & [$-$14.7, 9.3] & 0.82 \\\\\nCombined perturb. & $-$0.67 & [$-$8.0, 6.67] & 1.0 \\\\\n\\midrule\nAmbiguity (ref.) & \\textbf{+34.0} & [31.2, 36.9] & $<10^{-100}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{C2: Three-Tier Type Hierarchy}\n\nThe six ambiguity types differ significantly in violation rates (omnibus $\\chi^2=28.02$, $p=3.6 \\times 10^{-5}$, Cram\\'{e}r's $V=0.137$). Although the effect size is small, statistical power is 0.993 with a minimum detectable effect of $V=0.093$, confirming that the type effect is real. TOST equivalence analysis shows that only 4 of 15 type pairs are equivalent at $\\pm$10pp, demonstrating genuine heterogeneity.\n\nA three-tier structure emerges (Table~\\ref{tab:c2}): incompleteness stands alone as the highest-risk type (53.6\\%), four types form a mid-tier cluster (36.8--42.8\\%), and coreferential occupies the lowest tier (31.6\\%). The 22pp gap between the extremes is practically significant even though the overall $V$ is small.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{C2: Three-tier type hierarchy. Violation rates for ambiguous conditions, pooled across five models.}\n\\label{tab:c2}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Tier} & \\textbf{Type} & \\textbf{Rate} & \\textbf{Key Property} \\\\\n\\midrule\nHigh & incompleteness & 53.6\\% & Universally dangerous \\\\\n\\midrule\n\\multirow{4}{*}{Mid} & lexical & 42.8\\% & \\multirow{4}{*}{Pairwise equiv.\\ $\\pm$15pp} \\\\\n & auth\\_scope & 41.6\\% & \\\\\n & scopal & 39.4\\% & \\\\\n & cond\\_prec & 36.8\\% & \\\\\n\\midrule\nLow & coreferential & 31.6\\% & Partial disambig.\\ via tools \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCoreferential ambiguity occupies the lowest tier despite still producing substantial violations (+18.7pp vs.\\ unambiguous). Error analysis (Section~\\ref{sec:error}) reveals that agents sometimes obtain disambiguating information through tool responses, partially resolving referential ambiguity. This aligns with the disambiguation channel framework: linguistic ambiguity has external resolution paths that specification ambiguity lacks.\n\n\\subsection{C3: Layer Effect (Suggestive)}\n\nSpecification-layer types show higher violation rates than linguistic-layer types in aggregate (44.0\\% vs.\\ 37.9\\%, $\\Delta=6.08$pp, $p=0.017$, $V=0.062$). However, within-judge subgroup analysis reveals fragility: the effect is marginal when restricted to episodes judged by GPT-4.1 ($\\Delta=8.0$pp, $p=0.059$) and non-significant for GPT-5.4-judged episodes ($\\Delta=4.8$pp, $p=0.157$). We report this effect as suggestive rather than confirmed and note that it is subsumed by the model $\\times$ type interaction (C4).\n\nPer-model layer gaps vary dramatically: GPT-5.4 shows +14.0pp, GPT-4.1 +12.0pp, Claude +3.3pp, DeepSeek +2.0pp, and Qwen3 $-0.9$pp (reversed). The primary driver is authorization scope, where GPT models score 46--64\\% while Claude and Qwen3 score 12--26\\%. The layer effect is itself model-dependent, making the interaction the more fundamental finding.\n\nConvergent evidence from test-retest reliability (Appendix~\\ref{app:reliability}) supports the layer distinction: linguistic-layer types show near-perfect reproducibility (ICC 0.976--0.989), while specification-layer types show good but lower reproducibility (ICC 0.807--0.857). Agents consistently misparse linguistic ambiguity the same way but guess differently each run when specification information is missing.\n\n\\subsection{C4: Model $\\times$ Type Interaction}\n\\label{sec:c4}\n\nThe most novel finding is a significant model $\\times$ type interaction (Table~\\ref{tab:c4}). While the binary effect is universal, vulnerability \\textit{profiles} differ dramatically across models (overall $\\chi^2=31.02$, $p=3.0 \\times 10^{-6}$, $V=0.102$; ambiguous-only $\\chi^2=24.01$, $p=7.9 \\times 10^{-5}$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{C4: Model $\\times$ type interaction matrix. Violation rates (\\%) under ambiguous conditions. Range column shows cross-model spread.}\n\\label{tab:c4}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Type} & \\textbf{G-5.4} & \\textbf{G-4.1} & \\textbf{Cld.} & \\textbf{Qw3} & \\textbf{DS} & \\textbf{Rng.} \\\\\n\\midrule\nauth\\_scope & 64 & 46 & \\textbf{12} & 26 & 60 & 52 \\\\\nincomp. & 46 & 58 & 48 & 62 & 54 & 16 \\\\\nlexical & 42 & 34 & 32 & 52 & 54 & 22 \\\\\nscopal & 42 & 38 & 32 & 37 & 48 & 16 \\\\\ncond\\_prec & 34 & 36 & 36 & 40 & 38 & 6 \\\\\ncoref. & 18 & 32 & 22 & 42 & 44 & 26 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree interaction patterns are central to our differential nocuity framework:\n\n\\textbf{Authorization scope as the model-differentiating type.} The 52pp range (Claude 12\\% to GPT-5.4 64\\%) is the largest in the interaction matrix. Claude's robustness suggests that its safety training explicitly addresses authorization boundary awareness. GPT-5.4's high rate indicates that action-oriented frontier training can amplify permission-boundary violations. Per-model type $\\chi^2$ confirms that GPT-5.4 ($V=0.28$, $p=0.0003$) and Claude ($V=0.24$, $p=0.003$) show the strongest type differentiation.\n\n\\textbf{Incompleteness as a safety training blind spot.} All five models fail at high rates (46--62\\%, range only 16pp), regardless of architecture or training approach. When information is genuinely missing, no amount of safety training compensates, because the correct action (escalation) requires recognizing the absence of information, which all models fail to do.\n\n\\textbf{DeepSeek's uniform vulnerability.} DeepSeek shows the highest overall rate (49.7\\%) and no significant type differentiation ($\\chi^2=6.31$, $p=0.277$, $V=0.14$), suggesting less type-specific safety training. Qwen3 shows moderate differentiation ($V=0.23$, $p=0.007$), while GPT-4.1 is borderline ($V=0.18$, $p=0.078$). This gradient from uniform vulnerability (DeepSeek) to sharp differentiation (GPT-5.4, Claude) maps directly onto safety training specificity.\n\nInter-model agreement on which specific clauses trigger violations is only fair (Fleiss $\\kappa=0.384$). The binary effect is universal, but the \\textit{which-clauses} question is model-dependent, supporting our claim that vulnerability profiles, not just aggregate rates, carry diagnostic information.\n\n\\subsection{Cross-Benchmark Replication}\n\nTo test generalizability beyond retail and airline domains, we replicated the study on SOPBench \\cite{li2025sopbench} across healthcare and banking domains using 100 clause pairs (4 types) $\\times$ 2 conditions $\\times$ 5 models = 1,000 episodes, with a rule-based verifier replacing the LLM judge (Table~\\ref{tab:sopbench}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-benchmark replication on SOPBench. Effect replicates across 4 domains, 2 benchmarks, and 2 verification methods.}\n\\label{tab:sopbench}\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{$\\tau^2$-bench} & \\textbf{SOPBench} & \\textbf{Agreement} \\\\\n\\midrule\n$\\Delta$pp & +34.0 & +31.2 & CI overlap \\\\\nOR & 15.1 & 12.8 & Same magnitude \\\\\n$p$-value & $<10^{-100}$ & $<10^{-38}$ & Both sig. \\\\\nModels 5/5 & Yes & Yes & Universal \\\\\nDomains & Retail, Air. & Health., Bank & 4 total \\\\\nVerifier & LLM judge & Rule-based & Independent \\\\\n\\midrule\nType rank $\\rho$ & \\multicolumn{2}{c}{0.80 ($p=0.042$)} & Strong \\\\\nEffect corr.\\ $r$ & \\multicolumn{2}{c}{0.89} & Very strong \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSOPBench replicates C1 with $\\Delta=31.2$pp (OR=12.8, $p<10^{-38}$) across all five models. The per-model ranking is preserved (Claude lowest at +22.6pp, DeepSeek highest at +37.2pp, $r=0.89$). The type hierarchy also replicates: incompleteness ranks first in both benchmarks ($\\rho=0.80$, $p=0.042$). Healthcare shows a larger effect than banking (+33.8pp vs.\\ +28.6pp), consistent with the hypothesis that higher-stakes domains with more complex boundary conditions amplify ambiguity effects. The rule-based verifier agrees with the LLM judge at 91\\%, eliminating single-method dependency as a concern.\n\nThe authorization scope range on SOPBench (48pp) independently confirms the model $\\times$ type interaction observed on $\\tau^2$-bench (52pp), establishing this as a robust cross-domain finding.\n\n\\section{Error Analysis}\n\\label{sec:error}\n\nWe coded 300 violation traces (50 per type, stratified across five models and two domains) into four failure modes. Coding used automated cross-coding with inter-coder agreement of 80\\% (Gwet's AC1=0.73, good; Cohen's $\\kappa=0.594$, moderate, deflated by kappa paradox in two high-agreement types).\n\n\\subsection{Type-Specific Failure Signatures}\n\nEach ambiguity type produces a distinctive failure mode distribution (Table~\\ref{tab:failure_modes}), with 5 of 6 types showing the same dominant failure mode across all models. Only coreferential diverges, showing a flat distribution across modes rather than a single dominant pattern.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Type-specific failure modes. Dominant mode rate is the 5-model average. Types show distinctive signatures that are model-invariant.}\n\\label{tab:failure_modes}\n\\begin{tabular}{llc}\n\\toprule\n\\textbf{Type} & \\textbf{Dominant Mode} & \\textbf{Rate} \\\\\n\\midrule\nauth\\_scope & unauth.\\ escalation & 75\\% \\\\\nincompleteness & assumption-based action & 63\\% \\\\\nscopal & scope misapplication & 75\\% \\\\\nlexical & assumption-based action & 62\\% \\\\\ncond\\_prec & scope misapplication & 35\\% \\\\\ncoreferential & scope misapplication & 38\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA clear layer pattern emerges in the failure mechanisms. Specification-layer failures are dominated by ``guess-and-act'' behaviors: agents fill information gaps through unauthorized escalation (authorization scope) or ungrounded assumptions (incompleteness). Linguistic-layer failures are dominated by ``misparse-and-apply'': agents adopt an incorrect structural interpretation and apply it consistently (scopal, coreferential). This mechanistic distinction provides the qualitative foundation for the quantitative layer effect (C3) and explains why specification-layer types have lower test-retest reproducibility: guessing introduces stochasticity, while misparsing is deterministic.\n\n\\subsection{Ambiguity Blindness}\n\nAcross all five models and 300 coded traces, agents exhibit awareness of the encountered ambiguity in only 4.6\\% of violation episodes (Table~\\ref{tab:blindness}). In 89\\% of episodes, agents adopt the surface interpretation without any hedging or qualification. Only 0.8\\% of episodes involve escalation to the user.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ambiguity blindness: agents rarely recognize ambiguity. Rates are percentages of violation episodes.}\n\\label{tab:blindness}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Aware} & \\textbf{Surface} & \\textbf{Escalate} \\\\\n\\midrule\nGPT-5.4 & 4.1\\% & 91\\% & 0.8\\% \\\\\nGPT-4.1 & 10.7\\% & 85\\% & 1.6\\% \\\\\nClaude S-4.6 & 5.2\\% & 88\\% & 1.2\\% \\\\\nQwen3-235B & 3.8\\% & 90\\% & 0.4\\% \\\\\nDeepSeek-V3 & 2.4\\% & 93\\% & 0.2\\% \\\\\n\\midrule\n\\textbf{Pooled} & \\textbf{4.6\\%} & \\textbf{89\\%} & \\textbf{0.8\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGPT-4.1 shows the highest awareness rate (10.7\\%), 2.6$\\times$ higher than frontier GPT-5.4 (4.1\\%). This counterintuitive pattern suggests that awareness may inversely correlate with action-orientation: frontier models are more ``confident'' and act without hesitation, while mid-tier models occasionally pause. Yet even GPT-4.1's elevated awareness rarely translates to safe behavior (only 1.6\\% escalation), indicating that ambiguity detection must be externalized rather than relied upon as an emergent model capability.\n\nCross-domain consistency is high: failure mode profiles differ by less than 13pp between retail and airline domains, with the largest domain effect in unauthorized escalation (retail 38.6\\% vs.\\ airline 26.1\\%). Coreferential ambiguity produces the highest conservative refusal rate (8.5\\% vs.\\ 2--3\\% average), partially explaining its position as the lowest-risk type.\n\n\\section{Discussion}\n\n\\paragraph{Differential nocuity.}\nBerry and Kamsties \\shortcite{berry2003ambiguity} distinguish nocuous from innocuous ambiguity based on whether human readers diverge. Our results extend this framework to LLM agents with two findings. First, all tested policy ambiguity types are nocuous for agents (+34.0pp universal effect), unlike human settings where shared context renders much ambiguity innocuous. Second, nocuity is \\textit{differential}: the combination of ambiguity type and model family jointly determines risk level. Authorization scope is a ``canary type'' that reveals safety training quality, while incompleteness is a universal blind spot. This differential structure suggests that both type-aware policy auditing and model-specific risk assessment are necessary for safe agent deployment.\n\n\\paragraph{Systematic nocuity.}\nIn 27\\% of ambiguous episodes, all five models converge on the \\textit{same incorrect} interpretation. This pattern, which we term \\textit{systematic nocuity}, extends Berry and Kamsties' binary nocuous/innocuous distinction. Systematic nocuity is arguably more dangerous than divergent nocuity: when all agents agree on the wrong action, the error is invisible to inter-model agreement checks and appears ``correct'' until compared against ground truth.\n\n\\paragraph{Disambiguation channel framework.}\nThe layer hierarchy, type-specific failure modes, and ICC patterns converge on an explanatory framework: the availability of external disambiguation channels shapes vulnerability. Linguistic ambiguity (coreferential, lexical) can sometimes be resolved through tool responses, user context, or world knowledge, providing partial external channels. Specification ambiguity (authorization scope, incompleteness) has no external resolution path, forcing agents to guess. This framework is supported by observational evidence (linguistic ICC 0.976--0.989 vs.\\ specification ICC 0.807--0.857; coreferential's elevated conservative refusal rate; distinct failure mechanisms) but is not a tested causal hypothesis. A manipulation experiment (injecting disambiguation information into tool responses for specification-layer types) could test this framework directly.\n\n\\paragraph{Practical implications.}\nThe DeBERTa-based ambiguity classifier achieves binary F1=0.81 (Appendix~\\ref{app:classifier}), sufficient for pre-screening but with an important limitation: the most dangerous type (incompleteness, F1=0.34) is also the hardest to detect automatically, because absence of information has no surface signal. This inverse relationship between danger and detectability reinforces the need for human domain experts in policy review. Our type hierarchy provides a principled triage ordering: incompleteness clauses should receive the most careful human review.\n\n\\section{Conclusion}\n\nWe have presented the first causal, type-granular, cross-model study of policy ambiguity in LLM agents. Three findings stand out. First, the causal effect is massive and universal: +34.0pp across five models, confirmed by perturbation control and cross-benchmark replication across four domains. Second, a model $\\times$ type interaction reveals that safety training differentially addresses ambiguity types, with authorization scope as the model-differentiating canary (52pp range) and incompleteness as a universal blind spot (46--62\\%). Third, agents are effectively blind to the ambiguity they encounter ($<$5\\% awareness). These findings establish differential nocuity as a framework for understanding how ambiguity type, model architecture, and safety training jointly determine agent safety risk.\n\n\\section*{Limitations}\n\nOur study has three main limitations. First, the matched-pair design uses synthetic ambiguity injection, which may not capture all properties of naturally occurring policy ambiguity despite our realism validation (KS tests non-significant, discriminator at chance). Second, the within-judge analysis of the layer effect (C3) does not reach significance, and we report this claim as suggestive. The aggregate significance ($p=0.017$) may partly reflect between-judge variance rather than a true layer effect. Third, while SOPBench extends coverage to four domains, our primary study covers only retail and airline, and generalization to other high-stakes domains (e.g., legal, military) requires further investigation.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\n\\section{Taxonomy Cross-Walk}\n\\label{app:crosswalk}\n\nOur six types map onto prior taxonomies as follows. DRIP-R's five types (referential, scopal, attachment, lexical, ellipsis) align with our linguistic layer. Massey et al.'s six categories (vagueness, incompleteness, ambiguity, incorrectness, internal inconsistency, policy gap) provide antecedents for our specification layer. Li et al.'s eleven NLP types are subsumed by our two-layer structure.\n\n\\section{Test-Retest Reliability}\n\\label{app:reliability}\n\nWe assessed measurement reliability through test-retest analysis: 30 clauses (5 per type) $\\times$ 3 replicates $\\times$ 2 conditions $\\times$ 2 models (GPT-5.4, GPT-4.1) = 360 episodes (Table~\\ref{tab:icc}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Test-retest reliability (ICC). Linguistic-layer types show near-perfect reproducibility; specification-layer types show good but lower consistency.}\n\\label{tab:icc}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{ICC} & \\textbf{Rating} \\\\\n\\midrule\nscopal & Ling. & 0.989 & Excellent \\\\\nlexical & Ling. & 0.981 & Excellent \\\\\ncoreferential & Ling. & 0.976 & Excellent \\\\\nauth\\_scope & Spec. & 0.857 & Good \\\\\ncond\\_prec & Spec. & 0.856 & Good \\\\\nincompleteness & Spec. & 0.807 & Good \\\\\n\\midrule\n\\textbf{Overall} & & \\textbf{0.919} & \\textbf{Excellent} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe overall ICC of 0.919 (95\\% CI: [0.892, 0.940]) confirms excellent measurement reliability, justifying the single-run design of the main study. The layer-specific pattern (linguistic mean ICC 0.982 vs.\\ specification mean ICC 0.840) provides convergent evidence for the disambiguation channel framework: agents consistently misparse linguistic ambiguity the same way (deterministic) but guess differently under specification ambiguity (stochastic).\n\n\\section{DeBERTa Classifier}\n\\label{app:classifier}\n\nAs a proof-of-concept for practical ambiguity detection, we fine-tuned DeBERTa-v3-large on 500 annotated clauses with 5-fold cross-validation (Table~\\ref{tab:classifier}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DeBERTa ambiguity classifier (5-fold CV). Per-type F1 inversely correlates with violation severity.}\n\\label{tab:classifier}\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Type} & \\textbf{F1} & \\textbf{Prec./Rec.} & \\textbf{Difficulty} \\\\\n\\midrule\ncond\\_prec & 0.94 & 0.92/0.96 & Easy \\\\\nscopal & 0.75 & 0.78/0.72 & Moderate \\\\\ncoreferential & 0.70 & 0.73/0.67 & Moderate \\\\\nauth\\_scope & 0.58 & 0.62/0.55 & Hard \\\\\nlexical & 0.39 & 0.42/0.36 & Very hard \\\\\nincompleteness & 0.34 & 0.38/0.31 & Hardest \\\\\n\\midrule\n\\textbf{Binary} & \\textbf{0.81} & \\textbf{0.83/0.79} & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBinary detection achieves F1=0.81 with a false positive rate of 4.4\\%, sufficient for deployment as a pre-screening filter. The per-type performance reveals an inverse relationship between danger and detectability: the most safety-critical type (incompleteness, 53.6\\% violation rate) has the lowest detection F1 (0.34), because absence of information produces no surface signal. Conditional precedence is easiest to detect (F1=0.94) due to explicit conflict markers in the text.\n\n\\section{Mini-Pilot Validation}\n\\label{app:minipilot}\n\nBefore the full study, we validated the two novel ambiguity types (authorization scope and coreferential) through a mini-pilot: 5 clauses per type $\\times$ 2 conditions $\\times$ 1 model (GPT-5.4) = 20 episodes. Authorization scope showed a 60pp effect (60\\% ambiguous vs.\\ 0\\% unambiguous), and coreferential showed a 20pp effect (20\\% vs.\\ 0\\%). Both patterns confirmed basic validity with no systematic issues, enabling the full study to proceed.\n\n\\section{SOPBench Per-Model and Per-Domain Results}\n\\label{app:sopbench_detail}\n\nHealthcare shows a consistently larger effect (+33.8pp) than banking (+28.6pp). Per-model SOPBench results closely track $\\tau^2$-bench: GPT-5.4 +35.4pp (vs.\\ +38.3), DeepSeek +37.2pp (vs.\\ +39.0), GPT-4.1 +31.8pp (vs.\\ +34.7), Qwen3 +29.0pp (vs.\\ +32.4), Claude +22.6pp (vs.\\ +25.7). Incompleteness ranks first in both domains (healthcare 61\\%, banking 51\\%).\n\n\\section{Per-Model Type Differentiation}\n\\label{app:permodel_chi2}\n\nPer-model $\\chi^2$ tests reveal a gradient of type-specific vulnerability (Table~\\ref{tab:permodel}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-model type $\\chi^2$ on ambiguous-condition violation rates. Models range from strong differentiation (GPT-5.4) to uniform vulnerability (DeepSeek).}\n\\label{tab:permodel}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{$\\chi^2$} & \\textbf{$p$} & \\textbf{$V$} \\\\\n\\midrule\nGPT-5.4 & 23.44 & 0.0003 & 0.28 \\\\\nClaude S-4.6 & 17.87 & 0.003 & 0.24 \\\\\nQwen3-235B & 15.89 & 0.007 & 0.23 \\\\\nGPT-4.1 & 9.89 & 0.078 & 0.18 \\\\\nDeepSeek-V3 & 6.31 & 0.277 & 0.14 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Berry and Kamsties}2003]{berry2003ambiguity}\nDaniel~M. Berry and Erik Kamsties.\n\\newblock 2003.\n\\newblock Ambiguity in requirements specification.\n\\newblock In {\\em Perspectives on Software Requirements}, pages 7--44. Springer.\n\n\\bibitem[\\protect\\citename{Chantree \\bgroup et al.\\egroup}2006]{chantree2006identifying}\nFrancis Chantree, Bashar Nuseibeh, Anne de~Roeck, and Alistair Willis.\n\\newblock 2006.\n\\newblock Identifying nocuous ambiguities in natural language requirements.\n\\newblock In {\\em Proceedings of ASE}, pages 149--158.\n\n\\bibitem[\\protect\\citename{Chen \\bgroup et al.\\egroup}2024]{chen2024policybank}\nJiaming Chen et~al.\n\\newblock 2024.\n\\newblock {PolicyBank}: Benchmarking {LLM} agents on policy compliance.\n\\newblock {\\em arXiv preprint arXiv:2404.xxxxx}.\n\n\\bibitem[\\protect\\citename{Ezzini \\bgroup et al.\\egroup}2022]{ezzini2022taphsir}\nSaad Ezzini, Sallam Abualhaija, and Chetan Arora.\n\\newblock 2022.\n\\newblock {TAPHSIR}: Towards {AnaPHoric} ambiguity detection and resolution in requirements.\n\\newblock In {\\em Proceedings of ICSE}, pages 1--12.\n\n\\bibitem[\\protect\\citename{Ferreira \\bgroup et al.\\egroup}2002]{ferreira2002good}\nFernanda Ferreira, Karl G.~D. Bailey, and Vittoria Ferraro.\n\\newblock 2002.\n\\newblock Good-enough representations in language comprehension.\n\\newblock {\\em Current Directions in Psychological Science}, 11(1):11--15.\n\n\\bibitem[\\protect\\citename{Ferrari \\bgroup et al.\\egroup}2017]{ferrari2017detecting}\nAlessio Ferrari, Giorgio~O. Spagnolo, and Stefania Gnesi.\n\\newblock 2017.\n\\newblock Detecting requirements defects with {NLP} patterns.\n\\newblock In {\\em Proceedings of ASE}, pages 1--12.\n\n\\bibitem[\\protect\\citename{Frazier and Rayner}1982]{frazier1982making}\nLyn Frazier and Keith Rayner.\n\\newblock 1982.\n\\newblock Making and correcting errors during sentence comprehension.\n\\newblock {\\em Cognitive Psychology}, 14(2):178--210.\n\n\\bibitem[\\protect\\citename{Lassiter and Goodman}2017]{lassiter2017adjectival}\nDaniel Lassiter and Noah~D. Goodman.\n\\newblock 2017.\n\\newblock Adjectival vagueness in a {Bayesian} model of interpretation.\n\\newblock {\\em Synthese}, 194(10):3801--3836.\n\n\\bibitem[\\protect\\citename{Levy}2008]{levy2008expectation}\nRoger Levy.\n\\newblock 2008.\n\\newblock Expectation-based syntactic comprehension.\n\\newblock {\\em Cognition}, 106(3):1126--1177.\n\n\\bibitem[\\protect\\citename{Li \\bgroup et al.\\egroup}2024a]{li2024ambiguity}\nCheng Li et~al.\n\\newblock 2024a.\n\\newblock A survey of ambiguity in natural language processing.\n\\newblock {\\em ACL Rolling Review}.\n\n\\bibitem[\\protect\\citename{Li \\bgroup et al.\\egroup}2024b]{li2024dripr}\nCheng Li et~al.\n\\newblock 2024b.\n\\newblock {DRIP-R}: Disagreement-based ranking of ambiguous instructions in policy requirements.\n\\newblock {\\em arXiv preprint arXiv:2405.xxxxx}.\n\n\\bibitem[\\protect\\citename{Li \\bgroup et al.\\egroup}2024c]{li2024gardenpath}\nBai Li et~al.\n\\newblock 2024c.\n\\newblock Incremental comprehension of garden-path sentences by large language models.\n\\newblock In {\\em Proceedings of EMNLP}, pages 1--15.\n\n\\bibitem[\\protect\\citename{Li \\bgroup et al.\\egroup}2025]{li2025sopbench}\nZhi Li et~al.\n\\newblock 2025.\n\\newblock {SOPBench}: Benchmarking {LLM} agents on standard operating procedures.\n\\newblock In {\\em Proceedings of NAACL}.\n\n\\bibitem[\\protect\\citename{Lu \\bgroup et al.\\egroup}2022]{lu2022fantastically}\nYao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, and Pontus Stenetorp.\n\\newblock 2022.\n\\newblock Fantastically ordered prompts and where to find them.\n\\newblock In {\\em Proceedings of ACL}, pages 8086--8098.\n\n\\bibitem[\\protect\\citename{Massey \\bgroup et al.\\egroup}2014]{massey2014identifying}\nAaron~K. Massey, Richard~L. Rutledge, Annie~I. Ant\\'{o}n, and Peter~P. Swire.\n\\newblock 2014.\n\\newblock Identifying and classifying ambiguity for regulatory requirements.\n\\newblock In {\\em Proceedings of RE}, pages 83--92.\n\n\\bibitem[\\protect\\citename{Poesio and Artstein}2005]{poesio2005annotating}\nMassimo Poesio and Ron Artstein.\n\\newblock 2005.\n\\newblock Annotating (anaphoric) ambiguity.\n\\newblock In {\\em Proceedings of the Corpus Linguistics Conference}.\n\n\\bibitem[\\protect\\citename{Qin \\bgroup et al.\\egroup}2024]{qin2024toolbench}\nYujia Qin et~al.\n\\newblock 2024.\n\\newblock {ToolBench}: An open platform for evaluating {LLMs} as tool learners.\n\\newblock {\\em NeurIPS}.\n\n\\bibitem[\\protect\\citename{Ruan \\bgroup et al.\\egroup}2024]{ruan2024toolemu}\nYangjun Ruan et~al.\n\\newblock 2024.\n\\newblock {ToolEmu}: Identifying risks of {LLM} agents with an emulation framework.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Sclar \\bgroup et al.\\egroup}2024]{sclar2024quantifying}\nMelanie Sclar et~al.\n\\newblock 2024.\n\\newblock Quantifying language models' sensitivity to spurious features in prompt design.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Willis \\bgroup et al.\\egroup}2008]{willis2008automatic}\nAlistair Willis, Francis Chantree, and Anne de~Roeck.\n\\newblock 2008.\n\\newblock Automatic identification of nocuous ambiguity.\n\\newblock {\\em Research on Language and Computation}, 6(3):355--374.\n\n\\bibitem[\\protect\\citename{Yao \\bgroup et al.\\egroup}2024]{yao2024tau2bench}\nShunyu Yao et~al.\n\\newblock 2024.\n\\newblock {$\\tau^2$-bench}: Benchmarking agents on real-world customer service.\n\\newblock {\\em arXiv preprint arXiv:2406.xxxxx}.\n\n\\bibitem[\\protect\\citename{Yuan \\bgroup et al.\\egroup}2024]{yuan2024rjudge}\nTianle Yuan et~al.\n\\newblock 2024.\n\\newblock {R-Judge}: Benchmarking safety risk awareness for {LLM} agents.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Zhan \\bgroup et al.\\egroup}2024]{zhan2024injecagent}\nQiusi Zhan et~al.\n\\newblock 2024.\n\\newblock {InjecAgent}: Benchmarking indirect prompt injections in tool-integrated {LLM} agents.\n\\newblock In {\\em Proceedings of ACL Findings}.\n\n\\bibitem[\\protect\\citename{Zhou \\bgroup et al.\\egroup}2023]{zhou2023ifeval}\nJeffrey Zhou et~al.\n\\newblock 2023.\n\\newblock Instruction-following evaluation for large language models.\n\\newblock {\\em arXiv preprint arXiv:2311.07911}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dc2b79f-85cb-4a36-acc1-bc4b85391248",
  "isSidechain": false,
  "requestId": "req_011CbHY7MX7HbgkR7oU4uKih",
  "type": "assistant",
  "uuid": "2c38328d-d853-4156-9aa1-d3313e2734f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D85Rf9mAgjv5vo3okUuLGe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5919,
      "cache_read_input_tokens": 55923,
      "output_tokens": 15569,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5919,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15569,
          "cache_read_input_tokens": 55923,
          "cache_creation_input_tokens": 5919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5919
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

_source line 28 · 2026-05-22T11:40:21.351Z_

<details><summary>↩ Tool result · `toolu_01AuPHaVtWCAZeCrHaF9eQPu`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c38328d-d853-4156-9aa1-d3313e2734f5",
  "isSidechain": false,
  "promptId": "d65c2e8d-79bc-4128-97c7-582868b89531",
  "type": "user",
  "uuid": "503c68e4-0a71-4569-a0fc-a7433a6dffa2",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\aclfinalcopy\n\n\\title{Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWhen a customer service policy states that ``authorized personnel may process returns,'' a human agent draws on organizational context to resolve the vague permission boundary. Large Language Model (LLM) agents lack this context and must guess. We present the first causal, type-granular, cross-model study of how policy ambiguity drives safety violations in LLM agents. Using a matched-pair design with 300 clause pairs spanning six ambiguity types and a two-layer taxonomy (specification vs.\\ linguistic), we evaluate five architecturally diverse models across 2,997 episodes on the $\\tau^2$-bench framework. Ambiguous policies cause a +34.0 percentage point (pp) increase in safety violations (OR=15.1, $p<10^{-100}$), replicated across all five models. A perturbation control confirms this effect is ambiguity-specific ($\\Delta_\\text{perturb}=-0.67$pp). Beyond this universal effect, we find a significant model $\\times$ type interaction: authorization scope vulnerability ranges 52pp across models (12\\% for Claude to 64\\% for GPT-5.4), while incompleteness remains universally dangerous (46--62\\%). Cross-benchmark replication on SOPBench across healthcare and banking domains independently confirms the binary effect ($\\Delta=31.2$pp, rule-based verifier). Error analysis of 300 violation traces reveals type-specific failure signatures and pervasive ``ambiguity blindness'' ($<$5\\% awareness rate). These findings establish \\textit{differential nocuity} as a framework connecting Berry \\& Kamsties' ambiguity theory to modern safety alignment.\n\\end{abstract}\n\n\\section{Introduction}\n\nA retail policy states: ``Items purchased with a promotional discount may be exchanged within 14 days.'' An LLM agent interprets ``items'' as covering all categories, including custom orders, and processes a \\$200 return with free shipping. The unambiguous variant specifies ``standard catalog items only,'' and the same agent correctly declines. One word of ambiguity produces an unauthorized refund.\n\nThis scenario is not hypothetical. As LLM agents are deployed in customer-facing, healthcare, and financial settings, they operate under natural language policy specifications that inevitably contain ambiguity \\cite{berry2003ambiguity,massey2014identifying}. Human agents resolve such ambiguity through shared organizational context, training, and escalation norms. LLM agents lack these disambiguation channels and must act under uncertainty.\n\nPrior work has established taxonomies of policy ambiguity in requirements engineering \\cite{berry2003ambiguity,massey2014identifying} and NLP \\cite{li2024ambiguity}. Recent benchmarks evaluate agent safety under policy specifications \\cite{yao2024tau2bench,li2025sopbench}, and several studies probe agent robustness to adversarial or underspecified instructions \\cite{ruan2024toolemu,zhou2023ifeval}. However, no prior work provides \\textit{causal, type-granular} evidence linking specific ambiguity types to safety violation rates, nor examines how this relationship varies across model families.\n\nWe address this gap with three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Causal quantification.} A matched-pair design with perturbation control isolates ambiguity as the causal driver of safety violations. The effect is massive: +34.0pp (OR=15.1) across five architecturally diverse models, with perturbation controls confirming specificity ($\\Delta_\\text{perturb}=-0.67$pp). This constitutes the strongest causal evidence for ambiguity-specific harm in the agent safety literature.\n\n\\item \\textbf{Differential nocuity and model $\\times$ type interaction.} We introduce a two-layer, six-type ambiguity taxonomy and show that types form a three-tier risk hierarchy (incompleteness $>$ mid-cluster $>$ coreferential). The deeper finding is a significant model $\\times$ type interaction: authorization scope vulnerability spans 52pp across models, while incompleteness remains universally dangerous (46--62\\%), revealing that safety training differentially mitigates specific ambiguity types.\n\n\\item \\textbf{Type-specific failure modes and ambiguity blindness.} Qualitative analysis of 300 violation traces uncovers type-diagnostic failure signatures (specification-layer: guess-and-act; linguistic-layer: misparse-and-apply) and documents that agents exhibit $<$5\\% awareness of encountered ambiguity, with $>$88\\% surface interpretation adoption.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Ambiguity in requirements engineering.}\nBerry and Kamsties \\shortcite{berry2003ambiguity} distinguish \\textit{nocuous} ambiguity (causing divergent interpretations among stakeholders) from \\textit{innocuous} ambiguity (where interpretations converge). Massey et al.\\ \\shortcite{massey2014identifying} develop a six-type classification for privacy policy ambiguity. Chantree et al.\\ \\shortcite{chantree2006identifying} build the first computational nocuous ambiguity detector. Ferrari et al.\\ \\shortcite{ferrari2017detecting} extend NLP-based ambiguity detection to cross-domain requirements. Willis et al.\\ \\shortcite{willis2008automatic} and Ezzini et al.\\ \\shortcite{ezzini2022taphsir} automate ambiguity identification in software requirements. Our work operationalizes nocuity in the context of LLM agent safety, extending Berry \\& Kamsties' binary framework to a differential model.\n\n\\paragraph{LLM ambiguity processing.}\nLinguistic studies show that LLMs exhibit garden-path effects \\cite{frazier1982making,li2024gardenpath} and process ambiguity differently from humans \\cite{levy2008expectation,ferreira2002good}. Poesio and Artstein \\shortcite{poesio2005annotating} study anaphoric ambiguity annotation, and Lassiter and Goodman \\shortcite{lassiter2017adjectival} formalize vagueness in formal semantics. Our taxonomy draws on Li et al.\\ \\shortcite{li2024ambiguity}, who classify eleven NLP ambiguity types, and the DRIP-R benchmark \\cite{li2024dripr}, which measures model disagreement across five requirement ambiguity types but does not link disagreement to safety violations.\n\n\\paragraph{Agent safety evaluation.}\n$\\tau^2$-bench \\cite{yao2024tau2bench} and SOPBench \\cite{li2025sopbench} evaluate agent policy compliance. ToolEmu \\cite{ruan2024toolemu} and R-Judge \\cite{yuan2024rjudge} assess tool-use safety. InjecAgent \\cite{zhan2024injecagent} tests prompt injection. PolicyBank \\cite{chen2024policybank} classifies three types of policy gaps. IFEval \\cite{zhou2023ifeval} and ToolBench \\cite{qin2024toolbench} measure instruction-following robustness. Studies on prompt sensitivity \\cite{sclar2024quantifying,lu2022fantastically} show that surface-level perturbations affect model behavior. Unlike these works, we provide matched-pair causal evidence at type granularity, distinguishing ambiguity-specific effects from general prompt sensitivity.\n\n\\section{Ambiguity Taxonomy}\n\nWe adopt a two-layer taxonomy of policy ambiguity grounded in the intersection of NLP ambiguity classification \\cite{li2024ambiguity} and requirements engineering typologies \\cite{massey2014identifying,berry2003ambiguity}.\n\n\\paragraph{Specification layer.} These types arise from what the policy says (or fails to say) about domain-specific rules, not from grammatical structure. They cannot be resolved by linguistic analysis alone.\n\n\\begin{itemize}\n\\item \\textbf{Authorization scope}: Permission boundaries are stated but vague (e.g., ``authorized personnel may process returns'' without specifying which functions).\n\\item \\textbf{Incompleteness}: Conditions, exceptions, or boundaries are missing entirely (e.g., a return policy that omits the handling of opened electronics).\n\\item \\textbf{Conditional precedence}: Two or more rules apply to the same situation with conflicting outcomes (e.g., ``all items are returnable'' vs.\\ ``custom orders are final sale'').\n\\end{itemize}\n\n\\paragraph{Linguistic layer.} These types arise from the grammatical or lexical structure of policy language and can, in principle, be resolved through careful linguistic analysis.\n\n\\begin{itemize}\n\\item \\textbf{Scopal}: Quantifier, negation, or modal scope is unclear (e.g., ``customers may not return items purchased during the sale'' admits two scope readings).\n\\item \\textbf{Lexical}: A word has multiple contextually plausible senses (e.g., ``charge'' meaning financial charge vs.\\ battery charge in a device return policy).\n\\item \\textbf{Coreferential}: Pronouns or relative clauses have ambiguous antecedents (e.g., ``the manager approved the refund for the customer who complained'' admits two relative clause attachments).\n\\end{itemize}\n\nThis taxonomy maps onto prior work: our specification layer aligns with Massey et al.'s domain-specific categories, while the linguistic layer draws on Li et al.'s syntactic and lexical types. We provide a full cross-walk with DRIP-R's five types in Appendix~\\ref{app:crosswalk}.\n\n\\section{Method}\n\n\\subsection{Matched-Pair Design}\n\nFor each of 300 policy clauses, we construct an \\textit{ambiguous} variant and a matched \\textit{unambiguous} variant, differing only in the ambiguity-bearing element. This matched-pair design isolates ambiguity as the causal variable while controlling for clause content, domain, and task structure. Table~\\ref{tab:clause_dist} shows the distribution across types and domains.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Clause distribution by type, layer, and domain. Token delta measures the number of tokens added to create the unambiguous variant.}\n\\label{tab:clause_dist}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{Retail} & \\textbf{Airline} & \\textbf{$\\Delta$ Tok.} \\\\\n\\midrule\nauth\\_scope & Spec. & 25 & 25 & 36.1 \\\\\ncond\\_prec & Spec. & 25 & 25 & 28.4 \\\\\nincompleteness & Spec. & 25 & 25 & 34.6 \\\\\nscopal & Ling. & 25 & 25 & 14.2 \\\\\nlexical & Ling. & 25 & 25 & 12.8 \\\\\ncoreferential & Ling. & 25 & 25 & 7.8 \\\\\n\\midrule\n\\textbf{Total} & & \\textbf{150} & \\textbf{150} & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nClause generation followed an iterative process: pilot clauses (10 per type) were validated through the experimental pipeline, then expanded to 50 per type using real policy document templates. Each clause underwent Chantree-style quality validation \\cite{chantree2006identifying}, achieving a 98\\% pass rate. Token deltas were balanced within type (CV=0.18) and across types ($\\chi^2$ balance $p=0.72$). Conditional precedence clauses used a mix of labeled (40\\%) and unlabeled (60\\%) conflict formats to increase ecological validity. Mean Flesch-Kincaid grade level was 11.8 ($\\pm$2.1), consistent with professional policy language.\n\n\\subsection{Ecological Validity}\n\nTo validate that our synthetic ambiguity injection preserves the properties of naturally occurring policy ambiguity, we compared clause distributions against DRIP-R's corpus of natural ambiguities using Kolmogorov-Smirnov tests (Table~\\ref{tab:realism}). No significant differences were found across four linguistic properties (all $p > 0.15$). A trained discriminator achieved only 56\\% accuracy (95\\% CI: [48\\%, 64\\%], containing chance), confirming distributional equivalence.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ecological validity: synthetic clauses vs.\\ DRIP-R natural ambiguities. No significant distributional differences.}\n\\label{tab:realism}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Property} & \\textbf{Ours} & \\textbf{DRIP-R} & \\textbf{KS $p$} \\\\\n\\midrule\nSentence length & 22.4$\\pm$6.2 & 21.8$\\pm$7.1 & 0.34 \\\\\nParse depth & 5.3$\\pm$1.4 & 5.6$\\pm$1.6 & 0.21 \\\\\nFlesch-Kincaid & 11.8$\\pm$2.1 & 12.3$\\pm$2.4 & 0.48 \\\\\nType-token ratio & 0.82$\\pm$0.06 & 0.80$\\pm$0.07 & 0.15 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Models and Evaluation}\n\nWe evaluate five architecturally diverse models: GPT-5.4 and GPT-4.1 (proprietary dense), Claude Sonnet 4.6 (proprietary dense), Qwen3-235B (open-source MoE, 22B active), and DeepSeek-V3 (open-source MoE, 37B active). Each model processes all 300 clause pairs under both conditions, yielding 2,997 total episodes (3 API models $\\times$ 600 + 2 open-source models $\\times$ 600, with 3 episodes lost to API errors).\n\nEvaluation uses cross-judge LLM assessment: GPT-4.1 judges GPT-5.4 and DeepSeek; GPT-5.4 judges GPT-4.1, Claude, and Qwen3. Each episode receives a three-tier severity label (severe violation, moderate violation, no violation), collapsed to binary (violation/no-violation) for primary analysis. Cross-judge agreement is $\\kappa=0.74$ (substantial).\n\n\\paragraph{Judge calibration.}\nWe validated the LLM judge against human annotation on 100 stratified episodes coded by two human annotators (Table~\\ref{tab:judge_cal}). Human-LLM binary $\\kappa=0.87$ (strong) with F1=0.92, exceeding human inter-annotator $\\kappa=0.762$. The LLM judge is more consistent than individual human coders, with disagreements concentrated at moderate-severity boundaries (78\\% agreement) rather than clear violations (91\\%) or clean episodes (95\\%).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Judge calibration: human-LLM agreement on 100 stratified episodes. LLM judge agreement exceeds human inter-annotator baseline.}\n\\label{tab:judge_cal}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Interp.} \\\\\n\\midrule\nHuman-LLM binary $\\kappa$ & 0.87 & Strong \\\\\nHuman-LLM binary F1 & 0.92 & High \\\\\nPrecision / Recall & 0.94 / 0.90 & Balanced \\\\\nHuman inter-annot.\\ $\\kappa$ & 0.762 & Ceiling \\\\\nCross-judge $\\kappa$ (weighted) & 0.685 & Substantial \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Perturbation Control}\n\nTo distinguish ambiguity-specific effects from general prompt sensitivity, we constructed 30 clause pairs with non-ambiguity surface perturbations: 15 synonym substitutions and 15 clause reorderings. These pairs were evaluated under the same conditions as the main study (300 episodes total). Results appear in Section~\\ref{sec:perturbation}.\n\n\\section{Results}\n\n\\subsection{C1: Universal Binary Effect}\n\\label{sec:c1}\n\nAmbiguous policy specifications cause massive increases in safety violation rates across all five models (Table~\\ref{tab:c1}). The pooled effect is +34.0pp (bootstrap 95\\% CI: [31.2, 36.9]), with an odds ratio of 15.1 (CI: [10.78, 21.17]) and McNemar $p < 10^{-100}$. Every model individually replicates the effect with $p < 10^{-17}$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{C1: Binary effect across five models. All models show massive violation rate increases under ambiguous policies.}\n\\label{tab:c1}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} & \\textbf{OR [95\\% CI]} \\\\\n\\midrule\nGPT-5.4 & 41.0\\% & 2.7\\% & +38.3 & 25.3 [14.8, 43.2] \\\\\nDeepSeek-V3 & 49.7\\% & 10.7\\% & +39.0 & 8.3 \\\\\nGPT-4.1 & 40.7\\% & 6.0\\% & +34.7 & 10.9 [7.1, 16.6] \\\\\nQwen3-235B & 43.1\\% & 10.7\\% & +32.4 & 6.4 \\\\\nClaude S-4.6 & 30.3\\% & 4.7\\% & +25.7 & 8.9 [5.5, 14.5] \\\\\n\\midrule\n\\textbf{Pooled} & \\textbf{37.3\\%} & \\textbf{4.4\\%} & \\textbf{+34.0} & \\textbf{15.1 [10.8, 21.2]} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLogistic regression confirms ambiguity as the dominant predictor even after controlling for token delta, model, and type (condition coefficient = 2.278, $z=19.65$, $p<0.001$). Token delta is a significant but secondary predictor (coefficient = 0.022, $z=3.49$, $p=0.0005$), suggesting that specification-layer clauses, which require more tokens to disambiguate, are partly more dangerous because they contain more missing information.\n\n\\subsection{Perturbation Control: Ambiguity-Specific Causation}\n\\label{sec:perturbation}\n\nNon-ambiguity surface modifications produce no meaningful effect (Table~\\ref{tab:perturb}). Synonym substitution causes +1.33pp ($p=1.0$) and clause reordering causes $-2.67$pp ($p=0.82$). The combined perturbation effect is $-0.67$pp (95\\% CI: [$-8.0$, 6.67], containing zero). Against the ambiguity effect of +34.0pp, the ratio of perturbation-to-ambiguity effect is 0.0, passing all causal attribution criteria.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation control: non-ambiguity surface changes cause zero meaningful effect, confirming ambiguity-specific causation.}\n\\label{tab:perturb}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{$\\Delta$pp} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nSynonym subst. & +1.33 & [$-$10.7, 13.3] & 1.0 \\\\\nClause reorder & $-$2.67 & [$-$14.7, 9.3] & 0.82 \\\\\nCombined perturb. & $-$0.67 & [$-$8.0, 6.67] & 1.0 \\\\\n\\midrule\nAmbiguity (ref.) & \\textbf{+34.0} & [31.2, 36.9] & $<10^{-100}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{C2: Three-Tier Type Hierarchy}\n\nThe six ambiguity types differ significantly in violation rates (omnibus $\\chi^2=28.02$, $p=3.6 \\times 10^{-5}$, Cram\\'{e}r's $V=0.137$). Although the effect size is small, statistical power is 0.993 with a minimum detectable effect of $V=0.093$, confirming that the type effect is real. TOST equivalence analysis shows that only 4 of 15 type pairs are equivalent at $\\pm$10pp, demonstrating genuine heterogeneity.\n\nA three-tier structure emerges (Table~\\ref{tab:c2}): incompleteness stands alone as the highest-risk type (53.6\\%), four types form a mid-tier cluster (36.8--42.8\\%), and coreferential occupies the lowest tier (31.6\\%). The 22pp gap between the extremes is practically significant even though the overall $V$ is small.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{C2: Three-tier type hierarchy. Violation rates for ambiguous conditions, pooled across five models.}\n\\label{tab:c2}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Tier} & \\textbf{Type} & \\textbf{Rate} & \\textbf{Key Property} \\\\\n\\midrule\nHigh & incompleteness & 53.6\\% & Universally dangerous \\\\\n\\midrule\n\\multirow{4}{*}{Mid} & lexical & 42.8\\% & \\multirow{4}{*}{Pairwise equiv.\\ $\\pm$15pp} \\\\\n & auth\\_scope & 41.6\\% & \\\\\n & scopal & 39.4\\% & \\\\\n & cond\\_prec & 36.8\\% & \\\\\n\\midrule\nLow & coreferential & 31.6\\% & Partial disambig.\\ via tools \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCoreferential ambiguity occupies the lowest tier despite still producing substantial violations (+18.7pp vs.\\ unambiguous). Error analysis (Section~\\ref{sec:error}) reveals that agents sometimes obtain disambiguating information through tool responses, partially resolving referential ambiguity. This aligns with the disambiguation channel framework: linguistic ambiguity has external resolution paths that specification ambiguity lacks.\n\n\\subsection{C3: Layer Effect (Suggestive)}\n\nSpecification-layer types show higher violation rates than linguistic-layer types in aggregate (44.0\\% vs.\\ 37.9\\%, $\\Delta=6.08$pp, $p=0.017$, $V=0.062$). However, within-judge subgroup analysis reveals fragility: the effect is marginal when restricted to episodes judged by GPT-4.1 ($\\Delta=8.0$pp, $p=0.059$) and non-significant for GPT-5.4-judged episodes ($\\Delta=4.8$pp, $p=0.157$). We report this effect as suggestive rather than confirmed and note that it is subsumed by the model $\\times$ type interaction (C4).\n\nPer-model layer gaps vary dramatically: GPT-5.4 shows +14.0pp, GPT-4.1 +12.0pp, Claude +3.3pp, DeepSeek +2.0pp, and Qwen3 $-0.9$pp (reversed). The primary driver is authorization scope, where GPT models score 46--64\\% while Claude and Qwen3 score 12--26\\%. The layer effect is itself model-dependent, making the interaction the more fundamental finding.\n\nConvergent evidence from test-retest reliability (Appendix~\\ref{app:reliability}) supports the layer distinction: linguistic-layer types show near-perfect reproducibility (ICC 0.976--0.989), while specification-layer types show good but lower reproducibility (ICC 0.807--0.857). Agents consistently misparse linguistic ambiguity the same way but guess differently each run when specification information is missing.\n\n\\subsection{C4: Model $\\times$ Type Interaction}\n\\label{sec:c4}\n\nThe most novel finding is a significant model $\\times$ type interaction (Table~\\ref{tab:c4}). While the binary effect is universal, vulnerability \\textit{profiles} differ dramatically across models (overall $\\chi^2=31.02$, $p=3.0 \\times 10^{-6}$, $V=0.102$; ambiguous-only $\\chi^2=24.01$, $p=7.9 \\times 10^{-5}$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{C4: Model $\\times$ type interaction matrix. Violation rates (\\%) under ambiguous conditions. Range column shows cross-model spread.}\n\\label{tab:c4}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Type} & \\textbf{G-5.4} & \\textbf{G-4.1} & \\textbf{Cld.} & \\textbf{Qw3} & \\textbf{DS} & \\textbf{Rng.} \\\\\n\\midrule\nauth\\_scope & 64 & 46 & \\textbf{12} & 26 & 60 & 52 \\\\\nincomp. & 46 & 58 & 48 & 62 & 54 & 16 \\\\\nlexical & 42 & 34 & 32 & 52 & 54 & 22 \\\\\nscopal & 42 & 38 & 32 & 37 & 48 & 16 \\\\\ncond\\_prec & 34 & 36 & 36 & 40 & 38 & 6 \\\\\ncoref. & 18 & 32 & 22 & 42 & 44 & 26 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree interaction patterns are central to our differential nocuity framework:\n\n\\textbf{Authorization scope as the model-differentiating type.} The 52pp range (Claude 12\\% to GPT-5.4 64\\%) is the largest in the interaction matrix. Claude's robustness suggests that its safety training explicitly addresses authorization boundary awareness. GPT-5.4's high rate indicates that action-oriented frontier training can amplify permission-boundary violations. Per-model type $\\chi^2$ confirms that GPT-5.4 ($V=0.28$, $p=0.0003$) and Claude ($V=0.24$, $p=0.003$) show the strongest type differentiation.\n\n\\textbf{Incompleteness as a safety training blind spot.} All five models fail at high rates (46--62\\%, range only 16pp), regardless of architecture or training approach. When information is genuinely missing, no amount of safety training compensates, because the correct action (escalation) requires recognizing the absence of information, which all models fail to do.\n\n\\textbf{DeepSeek's uniform vulnerability.} DeepSeek shows the highest overall rate (49.7\\%) and no significant type differentiation ($\\chi^2=6.31$, $p=0.277$, $V=0.14$), suggesting less type-specific safety training. Qwen3 shows moderate differentiation ($V=0.23$, $p=0.007$), while GPT-4.1 is borderline ($V=0.18$, $p=0.078$). This gradient from uniform vulnerability (DeepSeek) to sharp differentiation (GPT-5.4, Claude) maps directly onto safety training specificity.\n\nInter-model agreement on which specific clauses trigger violations is only fair (Fleiss $\\kappa=0.384$). The binary effect is universal, but the \\textit{which-clauses} question is model-dependent, supporting our claim that vulnerability profiles, not just aggregate rates, carry diagnostic information.\n\n\\subsection{Cross-Benchmark Replication}\n\nTo test generalizability beyond retail and airline domains, we replicated the study on SOPBench \\cite{li2025sopbench} across healthcare and banking domains using 100 clause pairs (4 types) $\\times$ 2 conditions $\\times$ 5 models = 1,000 episodes, with a rule-based verifier replacing the LLM judge (Table~\\ref{tab:sopbench}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-benchmark replication on SOPBench. Effect replicates across 4 domains, 2 benchmarks, and 2 verification methods.}\n\\label{tab:sopbench}\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{$\\tau^2$-bench} & \\textbf{SOPBench} & \\textbf{Agreement} \\\\\n\\midrule\n$\\Delta$pp & +34.0 & +31.2 & CI overlap \\\\\nOR & 15.1 & 12.8 & Same magnitude \\\\\n$p$-value & $<10^{-100}$ & $<10^{-38}$ & Both sig. \\\\\nModels 5/5 & Yes & Yes & Universal \\\\\nDomains & Retail, Air. & Health., Bank & 4 total \\\\\nVerifier & LLM judge & Rule-based & Independent \\\\\n\\midrule\nType rank $\\rho$ & \\multicolumn{2}{c}{0.80 ($p=0.042$)} & Strong \\\\\nEffect corr.\\ $r$ & \\multicolumn{2}{c}{0.89} & Very strong \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSOPBench replicates C1 with $\\Delta=31.2$pp (OR=12.8, $p<10^{-38}$) across all five models. The per-model ranking is preserved (Claude lowest at +22.6pp, DeepSeek highest at +37.2pp, $r=0.89$). The type hierarchy also replicates: incompleteness ranks first in both benchmarks ($\\rho=0.80$, $p=0.042$). Healthcare shows a larger effect than banking (+33.8pp vs.\\ +28.6pp), consistent with the hypothesis that higher-stakes domains with more complex boundary conditions amplify ambiguity effects. The rule-based verifier agrees with the LLM judge at 91\\%, eliminating single-method dependency as a concern.\n\nThe authorization scope range on SOPBench (48pp) independently confirms the model $\\times$ type interaction observed on $\\tau^2$-bench (52pp), establishing this as a robust cross-domain finding.\n\n\\section{Error Analysis}\n\\label{sec:error}\n\nWe coded 300 violation traces (50 per type, stratified across five models and two domains) into four failure modes. Coding used automated cross-coding with inter-coder agreement of 80\\% (Gwet's AC1=0.73, good; Cohen's $\\kappa=0.594$, moderate, deflated by kappa paradox in two high-agreement types).\n\n\\subsection{Type-Specific Failure Signatures}\n\nEach ambiguity type produces a distinctive failure mode distribution (Table~\\ref{tab:failure_modes}), with 5 of 6 types showing the same dominant failure mode across all models. Only coreferential diverges, showing a flat distribution across modes rather than a single dominant pattern.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Type-specific failure modes. Dominant mode rate is the 5-model average. Types show distinctive signatures that are model-invariant.}\n\\label{tab:failure_modes}\n\\begin{tabular}{llc}\n\\toprule\n\\textbf{Type} & \\textbf{Dominant Mode} & \\textbf{Rate} \\\\\n\\midrule\nauth\\_scope & unauth.\\ escalation & 75\\% \\\\\nincompleteness & assumption-based action & 63\\% \\\\\nscopal & scope misapplication & 75\\% \\\\\nlexical & assumption-based action & 62\\% \\\\\ncond\\_prec & scope misapplication & 35\\% \\\\\ncoreferential & scope misapplication & 38\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA clear layer pattern emerges in the failure mechanisms. Specification-layer failures are dominated by ``guess-and-act'' behaviors: agents fill information gaps through unauthorized escalation (authorization scope) or ungrounded assumptions (incompleteness). Linguistic-layer failures are dominated by ``misparse-and-apply'': agents adopt an incorrect structural interpretation and apply it consistently (scopal, coreferential). This mechanistic distinction provides the qualitative foundation for the quantitative layer effect (C3) and explains why specification-layer types have lower test-retest reproducibility: guessing introduces stochasticity, while misparsing is deterministic.\n\n\\subsection{Ambiguity Blindness}\n\nAcross all five models and 300 coded traces, agents exhibit awareness of the encountered ambiguity in only 4.6\\% of violation episodes (Table~\\ref{tab:blindness}). In 89\\% of episodes, agents adopt the surface interpretation without any hedging or qualification. Only 0.8\\% of episodes involve escalation to the user.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ambiguity blindness: agents rarely recognize ambiguity. Rates are percentages of violation episodes.}\n\\label{tab:blindness}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Aware} & \\textbf{Surface} & \\textbf{Escalate} \\\\\n\\midrule\nGPT-5.4 & 4.1\\% & 91\\% & 0.8\\% \\\\\nGPT-4.1 & 10.7\\% & 85\\% & 1.6\\% \\\\\nClaude S-4.6 & 5.2\\% & 88\\% & 1.2\\% \\\\\nQwen3-235B & 3.8\\% & 90\\% & 0.4\\% \\\\\nDeepSeek-V3 & 2.4\\% & 93\\% & 0.2\\% \\\\\n\\midrule\n\\textbf{Pooled} & \\textbf{4.6\\%} & \\textbf{89\\%} & \\textbf{0.8\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGPT-4.1 shows the highest awareness rate (10.7\\%), 2.6$\\times$ higher than frontier GPT-5.4 (4.1\\%). This counterintuitive pattern suggests that awareness may inversely correlate with action-orientation: frontier models are more ``confident'' and act without hesitation, while mid-tier models occasionally pause. Yet even GPT-4.1's elevated awareness rarely translates to safe behavior (only 1.6\\% escalation), indicating that ambiguity detection must be externalized rather than relied upon as an emergent model capability.\n\nCross-domain consistency is high: failure mode profiles differ by less than 13pp between retail and airline domains, with the largest domain effect in unauthorized escalation (retail 38.6\\% vs.\\ airline 26.1\\%). Coreferential ambiguity produces the highest conservative refusal rate (8.5\\% vs.\\ 2--3\\% average), partially explaining its position as the lowest-risk type.\n\n\\section{Discussion}\n\n\\paragraph{Differential nocuity.}\nBerry and Kamsties \\shortcite{berry2003ambiguity} distinguish nocuous from innocuous ambiguity based on whether human readers diverge. Our results extend this framework to LLM agents with two findings. First, all tested policy ambiguity types are nocuous for agents (+34.0pp universal effect), unlike human settings where shared context renders much ambiguity innocuous. Second, nocuity is \\textit{differential}: the combination of ambiguity type and model family jointly determines risk level. Authorization scope is a ``canary type'' that reveals safety training quality, while incompleteness is a universal blind spot. This differential structure suggests that both type-aware policy auditing and model-specific risk assessment are necessary for safe agent deployment.\n\n\\paragraph{Systematic nocuity.}\nIn 27\\% of ambiguous episodes, all five models converge on the \\textit{same incorrect} interpretation. This pattern, which we term \\textit{systematic nocuity}, extends Berry and Kamsties' binary nocuous/innocuous distinction. Systematic nocuity is arguably more dangerous than divergent nocuity: when all agents agree on the wrong action, the error is invisible to inter-model agreement checks and appears ``correct'' until compared against ground truth.\n\n\\paragraph{Disambiguation channel framework.}\nThe layer hierarchy, type-specific failure modes, and ICC patterns converge on an explanatory framework: the availability of external disambiguation channels shapes vulnerability. Linguistic ambiguity (coreferential, lexical) can sometimes be resolved through tool responses, user context, or world knowledge, providing partial external channels. Specification ambiguity (authorization scope, incompleteness) has no external resolution path, forcing agents to guess. This framework is supported by observational evidence (linguistic ICC 0.976--0.989 vs.\\ specification ICC 0.807--0.857; coreferential's elevated conservative refusal rate; distinct failure mechanisms) but is not a tested causal hypothesis. A manipulation experiment (injecting disambiguation information into tool responses for specification-layer types) could test this framework directly.\n\n\\paragraph{Practical implications.}\nThe DeBERTa-based ambiguity classifier achieves binary F1=0.81 (Appendix~\\ref{app:classifier}), sufficient for pre-screening but with an important limitation: the most dangerous type (incompleteness, F1=0.34) is also the hardest to detect automatically, because absence of information has no surface signal. This inverse relationship between danger and detectability reinforces the need for human domain experts in policy review. Our type hierarchy provides a principled triage ordering: incompleteness clauses should receive the most careful human review.\n\n\\section{Conclusion}\n\nWe have presented the first causal, type-granular, cross-model study of policy ambiguity in LLM agents. Three findings stand out. First, the causal effect is massive and universal: +34.0pp across five models, confirmed by perturbation control and cross-benchmark replication across four domains. Second, a model $\\times$ type interaction reveals that safety training differentially addresses ambiguity types, with authorization scope as the model-differentiating canary (52pp range) and incompleteness as a universal blind spot (46--62\\%). Third, agents are effectively blind to the ambiguity they encounter ($<$5\\% awareness). These findings establish differential nocuity as a framework for understanding how ambiguity type, model architecture, and safety training jointly determine agent safety risk.\n\n\\section*{Limitations}\n\nOur study has three main limitations. First, the matched-pair design uses synthetic ambiguity injection, which may not capture all properties of naturally occurring policy ambiguity despite our realism validation (KS tests non-significant, discriminator at chance). Second, the within-judge analysis of the layer effect (C3) does not reach significance, and we report this claim as suggestive. The aggregate significance ($p=0.017$) may partly reflect between-judge variance rather than a true layer effect. Third, while SOPBench extends coverage to four domains, our primary study covers only retail and airline, and generalization to other high-stakes domains (e.g., legal, military) requires further investigation.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\n\\section{Taxonomy Cross-Walk}\n\\label{app:crosswalk}\n\nOur six types map onto prior taxonomies as follows. DRIP-R's five types (referential, scopal, attachment, lexical, ellipsis) align with our linguistic layer. Massey et al.'s six categories (vagueness, incompleteness, ambiguity, incorrectness, internal inconsistency, policy gap) provide antecedents for our specification layer. Li et al.'s eleven NLP types are subsumed by our two-layer structure.\n\n\\section{Test-Retest Reliability}\n\\label{app:reliability}\n\nWe assessed measurement reliability through test-retest analysis: 30 clauses (5 per type) $\\times$ 3 replicates $\\times$ 2 conditions $\\times$ 2 models (GPT-5.4, GPT-4.1) = 360 episodes (Table~\\ref{tab:icc}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Test-retest reliability (ICC). Linguistic-layer types show near-perfect reproducibility; specification-layer types show good but lower consistency.}\n\\label{tab:icc}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{ICC} & \\textbf{Rating} \\\\\n\\midrule\nscopal & Ling. & 0.989 & Excellent \\\\\nlexical & Ling. & 0.981 & Excellent \\\\\ncoreferential & Ling. & 0.976 & Excellent \\\\\nauth\\_scope & Spec. & 0.857 & Good \\\\\ncond\\_prec & Spec. & 0.856 & Good \\\\\nincompleteness & Spec. & 0.807 & Good \\\\\n\\midrule\n\\textbf{Overall} & & \\textbf{0.919} & \\textbf{Excellent} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe overall ICC of 0.919 (95\\% CI: [0.892, 0.940]) confirms excellent measurement reliability, justifying the single-run design of the main study. The layer-specific pattern (linguistic mean ICC 0.982 vs.\\ specification mean ICC 0.840) provides convergent evidence for the disambiguation channel framework: agents consistently misparse linguistic ambiguity the same way (deterministic) but guess differently under specification ambiguity (stochastic).\n\n\\section{DeBERTa Classifier}\n\\label{app:classifier}\n\nAs a proof-of-concept for practical ambiguity detection, we fine-tuned DeBERTa-v3-large on 500 annotated clauses with 5-fold cross-validation (Table~\\ref{tab:classifier}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DeBERTa ambiguity classifier (5-fold CV). Per-type F1 inversely correlates with violation severity.}\n\\label{tab:classifier}\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Type} & \\textbf{F1} & \\textbf{Prec./Rec.} & \\textbf{Difficulty} \\\\\n\\midrule\ncond\\_prec & 0.94 & 0.92/0.96 & Easy \\\\\nscopal & 0.75 & 0.78/0.72 & Moderate \\\\\ncoreferential & 0.70 & 0.73/0.67 & Moderate \\\\\nauth\\_scope & 0.58 & 0.62/0.55 & Hard \\\\\nlexical & 0.39 & 0.42/0.36 & Very hard \\\\\nincompleteness & 0.34 & 0.38/0.31 & Hardest \\\\\n\\midrule\n\\textbf{Binary} & \\textbf{0.81} & \\textbf{0.83/0.79} & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBinary detection achieves F1=0.81 with a false positive rate of 4.4\\%, sufficient for deployment as a pre-screening filter. The per-type performance reveals an inverse relationship between danger and detectability: the most safety-critical type (incompleteness, 53.6\\% violation rate) has the lowest detection F1 (0.34), because absence of information produces no surface signal. Conditional precedence is easiest to detect (F1=0.94) due to explicit conflict markers in the text.\n\n\\section{Mini-Pilot Validation}\n\\label{app:minipilot}\n\nBefore the full study, we validated the two novel ambiguity types (authorization scope and coreferential) through a mini-pilot: 5 clauses per type $\\times$ 2 conditions $\\times$ 1 model (GPT-5.4) = 20 episodes. Authorization scope showed a 60pp effect (60\\% ambiguous vs.\\ 0\\% unambiguous), and coreferential showed a 20pp effect (20\\% vs.\\ 0\\%). Both patterns confirmed basic validity with no systematic issues, enabling the full study to proceed.\n\n\\section{SOPBench Per-Model and Per-Domain Results}\n\\label{app:sopbench_detail}\n\nHealthcare shows a consistently larger effect (+33.8pp) than banking (+28.6pp). Per-model SOPBench results closely track $\\tau^2$-bench: GPT-5.4 +35.4pp (vs.\\ +38.3), DeepSeek +37.2pp (vs.\\ +39.0), GPT-4.1 +31.8pp (vs.\\ +34.7), Qwen3 +29.0pp (vs.\\ +32.4), Claude +22.6pp (vs.\\ +25.7). Incompleteness ranks first in both domains (healthcare 61\\%, banking 51\\%).\n\n\\section{Per-Model Type Differentiation}\n\\label{app:permodel_chi2}\n\nPer-model $\\chi^2$ tests reveal a gradient of type-specific vulnerability (Table~\\ref{tab:permodel}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-model type $\\chi^2$ on ambiguous-condition violation rates. Models range from strong differentiation (GPT-5.4) to uniform vulnerability (DeepSeek).}\n\\label{tab:permodel}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{$\\chi^2$} & \\textbf{$p$} & \\textbf{$V$} \\\\\n\\midrule\nGPT-5.4 & 23.44 & 0.0003 & 0.28 \\\\\nClaude S-4.6 & 17.87 & 0.003 & 0.24 \\\\\nQwen3-235B & 15.89 & 0.007 & 0.23 \\\\\nGPT-4.1 & 9.89 & 0.078 & 0.18 \\\\\nDeepSeek-V3 & 6.31 & 0.277 & 0.14 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Berry and Kamsties}2003]{berry2003ambiguity}\nDaniel~M. Berry and Erik Kamsties.\n\\newblock 2003.\n\\newblock Ambiguity in requirements specification.\n\\newblock In {\\em Perspectives on Software Requirements}, pages 7--44. Springer.\n\n\\bibitem[\\protect\\citename{Chantree \\bgroup et al.\\egroup}2006]{chantree2006identifying}\nFrancis Chantree, Bashar Nuseibeh, Anne de~Roeck, and Alistair Willis.\n\\newblock 2006.\n\\newblock Identifying nocuous ambiguities in natural language requirements.\n\\newblock In {\\em Proceedings of ASE}, pages 149--158.\n\n\\bibitem[\\protect\\citename{Chen \\bgroup et al.\\egroup}2024]{chen2024policybank}\nJiaming Chen et~al.\n\\newblock 2024.\n\\newblock {PolicyBank}: Benchmarking {LLM} agents on policy compliance.\n\\newblock {\\em arXiv preprint arXiv:2404.xxxxx}.\n\n\\bibitem[\\protect\\citename{Ezzini \\bgroup et al.\\egroup}2022]{ezzini2022taphsir}\nSaad Ezzini, Sallam Abualhaija, and Chetan Arora.\n\\newblock 2022.\n\\newblock {TAPHSIR}: Towards {AnaPHoric} ambiguity detection and resolution in requirements.\n\\newblock In {\\em Proceedings of ICSE}, pages 1--12.\n\n\\bibitem[\\protect\\citename{Ferreira \\bgroup et al.\\egroup}2002]{ferreira2002good}\nFernanda Ferreira, Karl G.~D. Bailey, and Vittoria Ferraro.\n\\newblock 2002.\n\\newblock Good-enough representations in language comprehension.\n\\newblock {\\em Current Directions in Psychological Science}, 11(1):11--15.\n\n\\bibitem[\\protect\\citename{Ferrari \\bgroup et al.\\egroup}2017]{ferrari2017detecting}\nAlessio Ferrari, Giorgio~O. Spagnolo, and Stefania Gnesi.\n\\newblock 2017.\n\\newblock Detecting requirements defects with {NLP} patterns.\n\\newblock In {\\em Proceedings of ASE}, pages 1--12.\n\n\\bibitem[\\protect\\citename{Frazier and Rayner}1982]{frazier1982making}\nLyn Frazier and Keith Rayner.\n\\newblock 1982.\n\\newblock Making and correcting errors during sentence comprehension.\n\\newblock {\\em Cognitive Psychology}, 14(2):178--210.\n\n\\bibitem[\\protect\\citename{Lassiter and Goodman}2017]{lassiter2017adjectival}\nDaniel Lassiter and Noah~D. Goodman.\n\\newblock 2017.\n\\newblock Adjectival vagueness in a {Bayesian} model of interpretation.\n\\newblock {\\em Synthese}, 194(10):3801--3836.\n\n\\bibitem[\\protect\\citename{Levy}2008]{levy2008expectation}\nRoger Levy.\n\\newblock 2008.\n\\newblock Expectation-based syntactic comprehension.\n\\newblock {\\em Cognition}, 106(3):1126--1177.\n\n\\bibitem[\\protect\\citename{Li \\bgroup et al.\\egroup}2024a]{li2024ambiguity}\nCheng Li et~al.\n\\newblock 2024a.\n\\newblock A survey of ambiguity in natural language processing.\n\\newblock {\\em ACL Rolling Review}.\n\n\\bibitem[\\protect\\citename{Li \\bgroup et al.\\egroup}2024b]{li2024dripr}\nCheng Li et~al.\n\\newblock 2024b.\n\\newblock {DRIP-R}: Disagreement-based ranking of ambiguous instructions in policy requirements.\n\\newblock {\\em arXiv preprint arXiv:2405.xxxxx}.\n\n\\bibitem[\\protect\\citename{Li \\bgroup et al.\\egroup}2024c]{li2024gardenpath}\nBai Li et~al.\n\\newblock 2024c.\n\\newblock Incremental comprehension of garden-path sentences by large language models.\n\\newblock In {\\em Proceedings of EMNLP}, pages 1--15.\n\n\\bibitem[\\protect\\citename{Li \\bgroup et al.\\egroup}2025]{li2025sopbench}\nZhi Li et~al.\n\\newblock 2025.\n\\newblock {SOPBench}: Benchmarking {LLM} agents on standard operating procedures.\n\\newblock In {\\em Proceedings of NAACL}.\n\n\\bibitem[\\protect\\citename{Lu \\bgroup et al.\\egroup}2022]{lu2022fantastically}\nYao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, and Pontus Stenetorp.\n\\newblock 2022.\n\\newblock Fantastically ordered prompts and where to find them.\n\\newblock In {\\em Proceedings of ACL}, pages 8086--8098.\n\n\\bibitem[\\protect\\citename{Massey \\bgroup et al.\\egroup}2014]{massey2014identifying}\nAaron~K. Massey, Richard~L. Rutledge, Annie~I. Ant\\'{o}n, and Peter~P. Swire.\n\\newblock 2014.\n\\newblock Identifying and classifying ambiguity for regulatory requirements.\n\\newblock In {\\em Proceedings of RE}, pages 83--92.\n\n\\bibitem[\\protect\\citename{Poesio and Artstein}2005]{poesio2005annotating}\nMassimo Poesio and Ron Artstein.\n\\newblock 2005.\n\\newblock Annotating (anaphoric) ambiguity.\n\\newblock In {\\em Proceedings of the Corpus Linguistics Conference}.\n\n\\bibitem[\\protect\\citename{Qin \\bgroup et al.\\egroup}2024]{qin2024toolbench}\nYujia Qin et~al.\n\\newblock 2024.\n\\newblock {ToolBench}: An open platform for evaluating {LLMs} as tool learners.\n\\newblock {\\em NeurIPS}.\n\n\\bibitem[\\protect\\citename{Ruan \\bgroup et al.\\egroup}2024]{ruan2024toolemu}\nYangjun Ruan et~al.\n\\newblock 2024.\n\\newblock {ToolEmu}: Identifying risks of {LLM} agents with an emulation framework.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Sclar \\bgroup et al.\\egroup}2024]{sclar2024quantifying}\nMelanie Sclar et~al.\n\\newblock 2024.\n\\newblock Quantifying language models' sensitivity to spurious features in prompt design.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Willis \\bgroup et al.\\egroup}2008]{willis2008automatic}\nAlistair Willis, Francis Chantree, and Anne de~Roeck.\n\\newblock 2008.\n\\newblock Automatic identification of nocuous ambiguity.\n\\newblock {\\em Research on Language and Computation}, 6(3):355--374.\n\n\\bibitem[\\protect\\citename{Yao \\bgroup et al.\\egroup}2024]{yao2024tau2bench}\nShunyu Yao et~al.\n\\newblock 2024.\n\\newblock {$\\tau^2$-bench}: Benchmarking agents on real-world customer service.\n\\newblock {\\em arXiv preprint arXiv:2406.xxxxx}.\n\n\\bibitem[\\protect\\citename{Yuan \\bgroup et al.\\egroup}2024]{yuan2024rjudge}\nTianle Yuan et~al.\n\\newblock 2024.\n\\newblock {R-Judge}: Benchmarking safety risk awareness for {LLM} agents.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Zhan \\bgroup et al.\\egroup}2024]{zhan2024injecagent}\nQiusi Zhan et~al.\n\\newblock 2024.\n\\newblock {InjecAgent}: Benchmarking indirect prompt injections in tool-integrated {LLM} agents.\n\\newblock In {\\em Proceedings of ACL Findings}.\n\n\\bibitem[\\protect\\citename{Zhou \\bgroup et al.\\egroup}2023]{zhou2023ifeval}\nJeffrey Zhou et~al.\n\\newblock 2023.\n\\newblock Instruction-following evaluation for large language models.\n\\newblock {\\em arXiv preprint arXiv:2311.07911}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "2c38328d-d853-4156-9aa1-d3313e2734f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T111643 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguit…",
  "leafUuid": "503c68e4-0a71-4569-a0fc-a7433a6dffa2",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for policy ambiguity safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830"
}
```

---

### Assistant

_source line 31 · 2026-05-22T11:40:25.859Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to copy the acl.sty file to the target directory and compile. Let me check what's available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "503c68e4-0a71-4569-a0fc-a7433a6dffa2",
  "isSidechain": false,
  "requestId": "req_011CbHYWqhQBZirJnrBZNJ6n",
  "type": "assistant",
  "uuid": "9b47f2c2-e38c-477e-927f-1f880377e6bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019oUrEJbKtg1pz1LQnZ78ch",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15634,
      "cache_read_input_tokens": 61842,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15634,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 317,
          "cache_read_input_tokens": 61842,
          "cache_creation_input_tokens": 15634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15634
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

_source line 32 · 2026-05-22T11:40:26.658Z_

Now I need to copy the ACL style file and compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b47f2c2-e38c-477e-927f-1f880377e6bd",
  "isSidechain": false,
  "requestId": "req_011CbHYWqhQBZirJnrBZNJ6n",
  "type": "assistant",
  "uuid": "f6ba4f56-7cd7-4b21-9f6c-8d9f3c0d35c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019oUrEJbKtg1pz1LQnZ78ch",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15634,
      "cache_read_input_tokens": 61842,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15634,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 317,
          "cache_read_input_tokens": 61842,
          "cache_creation_input_tokens": 15634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15634
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

_source line 33 · 2026-05-22T11:40:29.005Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014yepFrgZUTg6oExjRPhLFh`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/acl.sty /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/ && cp /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/acl_natbib.bst /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/",
  "description": "Copy ACL style files to target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6ba4f56-7cd7-4b21-9f6c-8d9f3c0d35c4",
  "isSidechain": false,
  "requestId": "req_011CbHYWqhQBZirJnrBZNJ6n",
  "type": "assistant",
  "uuid": "1637b1c4-a71f-4089-b792-371da16e4e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019oUrEJbKtg1pz1LQnZ78ch",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15634,
      "cache_read_input_tokens": 61842,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15634,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 317,
          "cache_read_input_tokens": 61842,
          "cache_creation_input_tokens": 15634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15634
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

_source line 34 · 2026-05-22T11:40:29.071Z_

<details><summary>↩ Tool result · `toolu_014yepFrgZUTg6oExjRPhLFh`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1637b1c4-a71f-4089-b792-371da16e4e0c",
  "isSidechain": false,
  "promptId": "d65c2e8d-79bc-4128-97c7-582868b89531",
  "type": "user",
  "uuid": "ec0b4fee-a1f3-4b2b-ba73-d02bb9d0e1e7",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "1637b1c4-a71f-4089-b792-371da16e4e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-22T11:40:29.074Z_

```json
{
  "parentUuid": "ec0b4fee-a1f3-4b2b-ba73-d02bb9d0e1e7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4666ec83-bcd6-41be-930e-869c47b784d3",
  "timestamp": "2026-05-22T11:40:29.074Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 36 · 2026-05-22T11:40:33.271Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CezLfwru49voqBf69ogL1e`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex compilation pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4666ec83-bcd6-41be-930e-869c47b784d3",
  "isSidechain": false,
  "requestId": "req_011CbHYXQcp5DH4sUjjcfRoZ",
  "type": "assistant",
  "uuid": "2f1338f3-36eb-4b5c-837e-8ec140e0e0c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EA387SEu4C9dXsbstDcMHp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 439,
      "cache_read_input_tokens": 77476,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 439,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 77476,
          "cache_creation_input_tokens": 439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 439
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

_source line 37 · 2026-05-22T11:40:33.826Z_

<details><summary>↩ Tool result · `toolu_01CezLfwru49voqBf69ogL1e`</summary>

```text
[9] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/ti
mes/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb
>
Output written on paper.pdf (9 pages, 192934 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f1338f3-36eb-4b5c-837e-8ec140e0e0c5",
  "isSidechain": false,
  "promptId": "d65c2e8d-79bc-4128-97c7-582868b89531",
  "type": "user",
  "uuid": "60261a9c-902d-457b-a95c-607c253e0b59",
  "toolUseResult": {
    "stdout": "[9] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/ti\nmes/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb\n>\nOutput written on paper.pdf (9 pages, 192934 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2f1338f3-36eb-4b5c-837e-8ec140e0e0c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-22T11:40:37.236Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011gBPwDJACBEn1sqBp97AX1`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -15",
  "description": "Second pdflatex compilation pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60261a9c-902d-457b-a95c-607c253e0b59",
  "isSidechain": false,
  "requestId": "req_011CbHYXkvwGEhm9nNsHjxYM",
  "type": "assistant",
  "uuid": "61864e40-7eb8-4543-b16a-89c113432cf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DdLE8FQn4rMRHFg5CtFZdo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 832,
      "cache_read_input_tokens": 77915,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 77915,
          "cache_creation_input_tokens": 832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 832
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

_source line 39 · 2026-05-22T11:40:37.801Z_

<details><summary>↩ Tool result · `toolu_011gBPwDJACBEn1sqBp97AX1`</summary>

```text
nts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/ti
mes/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb
>
Output written on paper.pdf (9 pages, 195972 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61864e40-7eb8-4543-b16a-89c113432cf9",
  "isSidechain": false,
  "promptId": "d65c2e8d-79bc-4128-97c7-582868b89531",
  "type": "user",
  "uuid": "e5b1692c-d46d-423f-a933-65fa224c7fb3",
  "toolUseResult": {
    "stdout": "nts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/ti\nmes/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb\n>\nOutput written on paper.pdf (9 pages, 195972 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "61864e40-7eb8-4543-b16a-89c113432cf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-22T11:40:45.060Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01K1JAuxutoUVLf1kMZxsRAg`</summary>

```json
{
  "command": "grep -c \"Warning\" paper.log | head -1 && grep \"LaTeX Warning\" paper.log",
  "description": "Check for remaining LaTeX warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5b1692c-d46d-423f-a933-65fa224c7fb3",
  "isSidechain": false,
  "requestId": "req_011CbHYY3w8iWfM4C7kkpVfk",
  "type": "assistant",
  "uuid": "288620bf-cc2e-4a18-b286-1ec2f07625ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xmhp6Xp3yYpkEsqGvBM2aX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 78747,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 78747,
          "cache_creation_input_tokens": 628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 628
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

_source line 41 · 2026-05-22T11:40:45.130Z_

<details><summary>↩ Tool result · `toolu_01K1JAuxutoUVLf1kMZxsRAg`</summary>

```text
44
LaTeX Warning: `h' float specifier changed to `ht'.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "288620bf-cc2e-4a18-b286-1ec2f07625ce",
  "isSidechain": false,
  "promptId": "d65c2e8d-79bc-4128-97c7-582868b89531",
  "type": "user",
  "uuid": "92a3d7ce-cae7-49d1-ac0a-e074265c8ed3",
  "toolUseResult": {
    "stdout": "44\nLaTeX Warning: `h' float specifier changed to `ht'.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "288620bf-cc2e-4a18-b286-1ec2f07625ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-22T11:40:48.855Z_

Compilation successful. 9 pages, one minor float placement warning. Let me verify the PDF exists and check page count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92a3d7ce-cae7-49d1-ac0a-e074265c8ed3",
  "isSidechain": false,
  "requestId": "req_011CbHYYbJn9DXWBZgTUCrrp",
  "type": "assistant",
  "uuid": "dacec9fc-c30c-4791-910a-36d6daa34fb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AddQeX5C6qxCa49jgtVM3s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 127,
      "cache_read_input_tokens": 79375,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 127,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 79375,
          "cache_creation_input_tokens": 127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 127
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

_source line 43 · 2026-05-22T11:40:51.337Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JkiJrTKHAP5e2bxa9aQKZV`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/paper.pdf",
  "description": "Verify PDF output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dacec9fc-c30c-4791-910a-36d6daa34fb7",
  "isSidechain": false,
  "requestId": "req_011CbHYYbJn9DXWBZgTUCrrp",
  "type": "assistant",
  "uuid": "1c90f442-3ec4-40b9-bed1-07373ffd9a54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AddQeX5C6qxCa49jgtVM3s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 127,
      "cache_read_input_tokens": 79375,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 127,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 79375,
          "cache_creation_input_tokens": 127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 127
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

_source line 44 · 2026-05-22T11:40:51.386Z_

<details><summary>↩ Tool result · `toolu_01JkiJrTKHAP5e2bxa9aQKZV`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 195972 May 22 11:40 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c90f442-3ec4-40b9-bed1-07373ffd9a54",
  "isSidechain": false,
  "promptId": "d65c2e8d-79bc-4128-97c7-582868b89531",
  "type": "user",
  "uuid": "3ed7aea4-ba0b-439c-a415-3d0e8f648d5d",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 195972 May 22 11:40 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best/paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1c90f442-3ec4-40b9-bed1-07373ffd9a54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-22T11:41:00.116Z_

Paper compiled successfully: 9 pages (main text + appendix), 196KB PDF.

Coverage of all 11 experiments from `experiment_data.json`:
- **clause_generation** → Table 1 (§4.1)
- **new_type_mini_pilot** → Appendix D
- **full_study_api** → Table 2 (§5.1, C1)
- **full_study_opensource** → Table 2 (§5.1, C1)
- **full_study_analysis** → Tables 2-4 (§5.1-5.4, C1-C4), Appendix F
- **error_analysis** → Tables 6-7 (§6, C5)
- **reliability_test** → Appendix B (ICC)
- **realism_validation** → Table 3 (§4.2)
- **judge_calibration** → Table 4 (§4.3)
- **perturbation_control** → Table 5 (§5.2)
- **sopbench_cross_benchmark** → Table 8 (§5.5)
- **classifier_poc** → Appendix C (DeBERTa)

All quantitative claims use numbers directly from `experiment_data.json`. No numbers were fabricated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ed7aea4-ba0b-439c-a415-3d0e8f648d5d",
  "isSidechain": false,
  "requestId": "req_011CbHYZ44brmCVsu6uBMULu",
  "type": "assistant",
  "uuid": "23bf1c7e-f022-47a4-a9ea-463be57a8eb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/best",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTSds6tKgGcUNQAxEgRGKq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 242,
      "cache_read_input_tokens": 79502,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 79502,
          "cache_creation_input_tokens": 242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 242
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

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T111643 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguit…",
  "leafUuid": "23bf1c7e-f022-47a4-a9ea-463be57a8eb8",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for policy ambiguity safety",
  "sessionId": "ca99f461-2386-45ba-9b4d-04158cd2e830"
}
```

---
