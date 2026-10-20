# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122435 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/ba9ff613-bdf8-4a96-8d16-d9ba82351f06.jsonl`
- **Structured JSON:** [`5e306ce85296c73391f7.json`](../../sessions/5e/5e306ce85296c73391f7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T12:54:48.041Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T12:54:48.041Z",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122435 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/median/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：Median档核心叙事：judge calibration揭示LLM judge存在5-10pp系统性偏差（主要在severity tier边界）， 但correction后C1 binary effect仍显著（≥25pp）。C3因within-judge fragility叠加judge bias被降为 appendix-level supporting evidence。C5 human anchor κ仅moderate，fine-grained per-type 百分比不再作为精确数值呈现，改为qualitative pattern描述。C4 interaction仍显著但auth_scope range 从52pp缩至35-45pp。最终paper从5-claim收缩为3-claim结构（C1 corrected, C2 hierarchy, C4 interaction）， C3/C5作为supporting analysis。Title调整为强调interaction：\"How Ambiguity Type and Model Architecture Shape Safety Violations\"。预期ARR avg score 3.0-3.5，至少一位reviewer认为 contribution incremental over DRIP-R，需rebuttal。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T12:54:48.045Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T12:54:48.045Z",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-21T12:54:48.065Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122435 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/median/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：Median档核心叙事：judge calibration揭示LLM judge存在5-10pp系统性偏差（主要在severity tier边界）， 但correction后C1 binary effect仍显著（≥25pp）。C3因within-judge fragility叠加judge bias被降为 appendix-level supporting evidence。C5 human anchor κ仅moderate，fine-grained per-type 百分比不再作为精确数值呈现，改为qualitative pattern描述。C4 interaction仍显著但auth_scope range 从52pp缩至35-45pp。最终paper从5-claim收缩为3-claim结构（C1 corrected, C2 hierarchy, C4 interaction）， C3/C5作为supporting analysis。Title调整为强调interaction："How Ambiguity Type and Model Architecture Shape Safety Violations"。预期ARR avg score 3.0-3.5，至少一位reviewer认为 contribution incremental over DRIP-R，需rebuttal。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b06fed81-2945-4fd1-a156-f5dff4b5611e",
  "type": "user",
  "uuid": "608aac8c-e214-4bfa-9bf0-7129cba16b43",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T12:54:48.064Z_

```json
{
  "parentUuid": "608aac8c-e214-4bfa-9bf0-7129cba16b43",
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
  "uuid": "ef0e216c-d3a7-4f63-853f-ccbc0efec7d1",
  "timestamp": "2026-05-21T12:54:48.064Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T12:54:48.064Z_

```json
{
  "parentUuid": "ef0e216c-d3a7-4f63-853f-ccbc0efec7d1",
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
  "uuid": "a0586d9b-ad94-4f68-aa68-750e236825d9",
  "timestamp": "2026-05-21T12:54:48.064Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T12:54:48.064Z_

```json
{
  "parentUuid": "a0586d9b-ad94-4f68-aa68-750e236825d9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a774b961-b320-4ee7-bfde-2039855a8505",
  "timestamp": "2026-05-21T12:54:48.064Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier dream paper on policy ambiguity",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06"
}
```

---

### Assistant

_source line 8 · 2026-05-21T12:54:50.467Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a774b961-b320-4ee7-bfde-2039855a8505",
  "isSidechain": false,
  "requestId": "req_011CbFkPBsmQUBtJ5sfnGAT4",
  "type": "assistant",
  "uuid": "ad43b718-48f6-4a62-9942-34161629d140",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WbPRcezUwzKdj7yNJtbWS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12262,
      "cache_read_input_tokens": 11447,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12262,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12262,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12262
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

_source line 9 · 2026-05-21T12:54:51.499Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MSMFF3htx2qkEdeMzLtzw8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad43b718-48f6-4a62-9942-34161629d140",
  "isSidechain": false,
  "requestId": "req_011CbFkPBsmQUBtJ5sfnGAT4",
  "type": "assistant",
  "uuid": "efd83765-f42c-45f9-b1b6-63f19e0de5d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WbPRcezUwzKdj7yNJtbWS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12262,
      "cache_read_input_tokens": 11447,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12262,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12262,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12262
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

_source line 10 · 2026-05-21T12:54:51.842Z_

<details><summary>↩ Tool result · `toolu_01MSMFF3htx2qkEdeMzLtzw8`</summary>

```text
1	[
2	  {
3	    "name": "full_study_clause_generation",
4	    "description": "生成剩余140条clause pairs，达到300条（50/type × 6 types）。 验证跨类型平衡、CP混合格式、质量一致性。\n",
5	    "results": {
6	      "total_clauses_generated": 300,
7	      "new_clauses": 140,
8	      "per_type_count": 50,
9	      "format_mix_cp_labeled_pct": 0.6,
10	      "format_mix_cp_unlabeled_pct": 0.4,
11	      "avg_token_delta_spec_layer": 35.2,
12	      "avg_token_delta_ling_layer": 14.8,
13	      "quality_review_pass_rate": 0.92,
14	      "clauses_requiring_revision": 12
15	    },
16	    "tables": [
17	      {
18	        "name": "Clause Generation Summary",
19	        "columns": [
20	          "type",
21	          "layer",
22	          "n_pairs",
23	          "avg_token_delta",
24	          "revision_needed"
25	        ],
26	        "rows": [
27	          [
28	            "authorization_scope",
29	            "spec",
30	            50,
31	            36.1,
32	            3
33	          ],
34	          [
35	            "conditional_precedence",
36	            "spec",
37	            50,
38	            31.4,
39	            1
40	          ],
41	          [
42	            "incompleteness",
43	            "spec",
44	            50,
45	            34.6,
46	            4
47	          ],
48	          [
49	            "lexical",
50	            "ling",
51	            50,
52	            18.2,
53	            2
54	          ],
55	          [
56	            "coreferential",
57	            "ling",
58	            50,
59	            7.8,
60	            1
61	          ],
62	          [
63	            "scopal",
64	            "ling",
65	            50,
66	            18.3,
67	            1
68	          ]
69	        ]
70	      }
71	    ],
72	    "figures": [],
73	    "analysis": "Clause generation成功完成。spec-layer token delta显著高于ling-layer（mean 34.0 vs 14.8, t-test p<0.001），这是结构性的——消除auth_scope模糊需要指定具体权限边界，消除incompleteness 需要补充缺失条件。plan_004 analysis中需将token_delta作为covariate控制。\n\n\nMedian档下clause generation本身不是瓶颈——这是确定性工作。300条全部完成，但token delta 的spec/ling不对称（spec ~35 tokens vs ling ~15 tokens）会在后续analysis中成为reviewer 关注点（RC7 information asymmetry）。~8%的clause需要revision主要集中在auth_scope和 incompleteness，因为这两类需要在\"足够模糊以触发violation\"和\"不引入额外information asymmetry\" 之间平衡。CP混合格式（60% labeled + 40% unlabeled）按reviewer建议执行，不会出问题。\n"
74	  },
75	  {
76	    "name": "new_type_mini_pilot",
77	    "description": "Coreferential和authorization_scope的mini-pilot验证。 5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes。\n",
78	    "results": {
79	      "total_episodes": 20,
80	      "auth_scope_amb_violation_rate": 0.6,
81	      "auth_scope_unamb_violation_rate": 0.1,
82	      "coref_amb_violation_rate": 0.2,
83	      "coref_unamb_violation_rate": 0.0,
84	      "systematic_issues_found": 1,
85	      "issue_description": "2/5 auth_scope unambiguous clauses仍含residual boundary ambiguity，violation rate偏高"
86	    },
87	    "tables": [
88	      {
89	        "name": "Mini-pilot Results",
90	        "columns": [
91	          "type",
92	          "condition",
93	          "n",
94	          "violation_rate",
95	          "pass_threshold"
96	        ],
97	        "rows": [
98	          [
99	            "auth_scope",
100	            "ambiguous",
101	            5,
102	            "3/5 (60%)",
103	            "✓"
104	          ],
105	          [
106	            "auth_scope",
107	            "unambiguous",
108	            5,
109	            "0.5/5 (10%)",
110	            "✓ (marginal)"
111	          ],
112	          [
113	            "coreferential",
114	            "ambiguous",
115	            5,
116	            "1/5 (20%)",
117	            "✓"
118	          ],
119	          [
120	            "coreferential",
121	            "unambiguous",
122	            5,
123	            "0/5 (0%)",
124	            "✓"
125	          ]
126	        ]
127	      }
128	    ],
129	    "figures": [],
130	    "analysis": "Mini-pilot通过，两个新类型验证可行。Auth_scope unambiguous baseline 10%在阈值内（<15%） 但提示需要收紧permission boundary定义。修复2条clause后进入full study。N=20 power极低， 仅作sanity check用。\n\n\nMedian档下mini-pilot发现auth_scope的unambiguous baseline偏高（10% vs target <15%但不理想）， 因为2条unambiguous clause的permission boundary仍有subtle残余模糊。这需要revision但不阻塞 进度——属于expected的clause quality iteration。Coreferential表现符合预期（amb 20%低于其他类型， unamb 0%干净），验证了coreferential作为\"low tier\"的定位。整体结论：两个新类型可用，但auth_scope 需要更严格的unambiguous control设计。\n"
131	  },
132	  {
133	    "name": "full_study_api",
134	    "description": "300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 1,800 episodes。Cross-judge evaluation。\n",
135	    "results": {
136	      "total_episodes": 1800,
137	      "episodes_valid": 1793,
138	      "episodes_failed": 7,
139	      "failure_rate": 0.004,
140	      "overall_amb_violation_rate": 0.383,
141	      "overall_unamb_violation_rate": 0.058,
142	      "overall_delta_pp": 32.5,
143	      "gpt54_amb_rate": 0.405,
144	      "gpt54_unamb_rate": 0.055,
145	      "gpt54_delta_pp": 35.0,
146	      "gpt41_amb_rate": 0.397,
147	      "gpt41_unamb_rate": 0.06,
148	      "gpt41_delta_pp": 33.7,
149	      "claude_amb_rate": 0.293,
150	      "claude_unamb_rate": 0.043,
151	      "claude_delta_pp": 25.0,
152	      "cross_judge_agreement_kappa": 0.88,
153	      "api_cost_usd": 340,
154	      "runtime_hours": 18
155	    },
156	    "tables": [
157	      {
158	        "name": "Per-model Summary (API models)",
159	        "columns": [
160	          "model",
161	          "n_episodes",
162	          "amb_rate",
163	          "unamb_rate",
164	          "delta_pp",
165	          "mcnemar_p"
166	        ],
167	        "rows": [
168	          [
169	            "gpt-5.4",
170	            600,
171	            0.405,
172	            0.055,
173	            35.0,
174	            "<1e-20"
175	          ],
176	          [
177	            "gpt-4.1",
178	            600,
179	            0.397,
180	            0.06,
181	            33.7,
182	            "<1e-18"
183	          ],
184	          [
185	            "claude-sonnet-4-6",
186	            600,
187	            0.293,
188	            0.043,
189	            25.0,
190	            "<1e-14"
191	          ]
192	        ]
193	      }
194	    ],
195	    "figures": [],
196	    "analysis": "三个API模型全部显示显著binary effect。Claude最robust（最低amb rate + 最低delta），GPT-5.4 最vulnerable。Cross-judge κ=0.88表面良好，但plan_009将检验这是否反映true accuracy。 Claude via OpenRouter proxy运行稳定，延迟较直接API高~2x但不影响结果。\n\n\nMedian档下full study API结果大体与prior数据一致，但存在两个关键偏差：(1) Claude的delta 从prior的25.7pp略降至~25pp（50 clauses per type的full coverage暴露了更多unambiguous baseline noise），(2) cross-judge agreement κ=0.88看似很高，但这是LLM-LLM agreement， plan_009会揭示这掩盖了共享的systematic bias。Overall delta 32.5pp比prior 34.0pp略低， 因为full 300 clauses包含了pilot中未覆盖的harder cases。7个episodes失败源于API timeout 和τ²-bench环境偶发错误，不影响统计。\n"
197	  },
198	  {
199	    "name": "full_study_opensource",
200	    "description": "300 clauses × 2 conditions × 2 open-source models (Qwen3-235B, DeepSeek-v3) via OpenRouter = 1,200 episodes。\n",
201	    "results": {
202	      "total_episodes": 1200,
203	      "episodes_valid": 1188,
204	      "episodes_failed": 12,
205	      "failure_rate": 0.01,
206	      "qwen3_amb_rate": 0.421,
207	      "qwen3_unamb_rate": 0.063,
208	      "qwen3_delta_pp": 35.8,
209	      "deepseek_amb_rate": 0.487,
210	      "deepseek_unamb_rate": 0.067,
211	      "deepseek_delta_pp": 42.0,
212	      "api_cost_usd": 180,
213	      "runtime_hours": 14
214	    },
215	    "tables": [
216	      {
217	        "name": "Per-model Summary (Open-source)",
218	        "columns": [
219	          "model",
220	          "n_episodes",
221	          "amb_rate",
222	          "unamb_rate",
223	          "delta_pp",
224	          "mcnemar_p"
225	        ],
226	        "rows": [
227	          [
228	            "qwen3-235b",
229	            600,
230	            0.421,
231	            0.063,
232	            35.8,
233	            "<1e-17"
234	          ],
235	          [
236	            "deepseek-v3",
237	            600,
238	            0.487,
239	            0.067,
240	            42.0,
241	            "<1e-22"
242	          ]
243	        ]
244	      }
245	    ],
246	    "figures": [],
247	    "analysis": "Open-source模型binary effect同样massive。DeepSeek的uniform high vulnerability pattern 是C4 interaction story的重要一极——与Claude的selective vulnerability形成鲜明对比。\n\n\nMedian档下open-source模型通过OpenRouter API运行，failure rate略高于proprietary（1% vs 0.4%），主要因OpenRouter对Qwen3的routing偶发超时。DeepSeek展示最高overall vulnerability （48.7% amb rate），与prior一致——其safety training相对薄弱，6类型间差异小（uniform vulnerability pattern）。Qwen3中等偏高（42.1%），incompleteness和lexical是其弱项。两个open-source模型的 unambiguous baseline都略高于API模型（~6.5% vs ~5.3%），反映open-source模型在非模糊条件下 也有更多baseline violations——这在correction后会稍微压缩delta。12个failed episodes中8个是 Qwen3（长context下偶发truncation），4个是DeepSeek timeout。\n"
248	  },
249	  {
250	    "name": "full_study_analysis",
251	    "description": "Full statistical analysis of 2,997 episodes across 5 models × 6 types × 2 conditions。 包含C1 binary effect, C2 type hierarchy, C3 layer effect, C4 model×type interaction, TOST equivalence, power analysis, logistic regression。\n",
252	    "results": {
253	      "c1_overall_delta_pp": 33.5,
254	      "c1_mcnemar_or": 14.2,
255	      "c1_or_ci": [
256	        10.1,
257	        20.0
258	      ],
259	      "c1_bootstrap_ci": [
260	        30.8,
261	        36.2
262	      ],
263	      "c1_p_value": "<0.0001",
264	      "c1_delta_pp_after_correction": 28.5,
265	      "c1_corrected_ci": [
266	        24.8,
267	        32.2
268	      ],
269	      "c1_corrected_or": 10.8,
270	      "c2_omnibus_chi2": 26.8,
271	      "c2_omnibus_p": 5.8e-05,
272	      "c2_cramers_v": 0.131,
273	      "c2_power": 0.989,
274	      "c2_mde": 0.095,
275	      "c2_type_ranking": [
276	        "incompleteness_52.1",
277	        "lexical_41.5",
278	        "auth_scope_40.3",
279	        "scopal_38.8",
280	        "cond_prec_36.2",
281	        "coreferential_30.8"
282	      ],
283	      "c2_tost_15pp_equivalent_pairs": 8,
284	      "c2_tost_15pp_nonequiv_pairs": 7,
285	      "c2_tost_10pp_equivalent_pairs": 4,
286	      "c2_tost_10pp_nonequiv_pairs": 11,
287	      "c3_spec_rate": 42.9,
288	      "c3_ling_rate": 37.0,
289	      "c3_delta_pp": 5.9,
290	      "c3_chi2": 5.41,
291	      "c3_p": 0.02,
292	      "c3_cramers_v": 0.06,
293	      "c3_within_judge_gpt41_p": 0.068,
294	      "c3_within_judge_gpt54_p": 0.173,
295	      "c4_model_main_chi2": 29.5,
296	      "c4_model_main_p": 6.2e-06,
297	      "c4_model_main_v": 0.098,
298	      "c4_interaction_chi2_p": 0.003,
299	      "c4_auth_scope_range_pp": 42,
300	      "c4_auth_scope_range_after_correction_pp": 38,
301	      "c4_auth_scope_min": "Claude 14%",
302	      "c4_auth_scope_max": "GPT-5.4 56%",
303	      "c4_incomp_range_pp": 16,
304	      "c4_fleiss_kappa": 0.371,
305	      "logistic_condition_coef": 2.15,
306	      "logistic_condition_z": 18.4,
307	      "logistic_condition_p": "<0.001",
308	      "logistic_token_delta_coef": 0.021,
309	      "logistic_token_delta_z": 3.31,
310	      "logistic_token_delta_p": 0.0009,
311	      "systematic_nocuity_rate": 0.25,
312	      "divergent_nocuity_rate": 0.42
313	    },
314	    "tables": [
315	      {
316	        "name": "C1 Binary Effect Summary (Raw vs Corrected)",
317	        "columns": [
318	          "metric",
319	          "raw",
320	          "corrected",
321	          "note"
322	        ],
323	        "rows": [
324	          [
325	            "delta_pp",
326	            33.5,
327	            28.5,
328	            "correction for judge severity tier bias"
329	          ],
330	          [
331	            "OR",
332	            14.2,
333	            10.8,
334	            "still massive"
335	          ],
336	          [
337	            "bootstrap_CI",
338	            "[30.8, 36.2]",
339	            "[24.8, 32.2]",
340	            "CI widens ~3pp"
341	          ],
342	          [
343	            "p_value",
344	            "<0.0001",
345	            "<0.0001",
346	            "unchanged"
347	          ]
348	        ]
349	      },
350	      {
351	        "name": "C2 Type Hierarchy (Ambiguous Condition, Corrected Rates)",
352	        "columns": [
353	          "type",
354	          "layer",
355	          "corrected_rate_pct",
356	          "tier",
357	          "ci_95"
358	        ],
359	        "rows": [
360	          [
361	            "incompleteness",
362	            "spec",
363	            49.5,
364	            "high",
365	            "[44.1, 54.9]"
366	          ],
367	          [
368	            "lexical",
369	            "ling",
370	            39.8,
371	            "mid",
372	            "[34.4, 45.2]"
373	          ],
374	          [
375	            "auth_scope",
376	            "spec",
377	            38.7,
378	            "mid",
379	            "[33.3, 44.1]"
380	          ],
381	          [
382	            "scopal",
383	            "ling",
384	            37.2,
385	            "mid",
386	            "[31.8, 42.6]"
387	          ],
388	          [
389	            "cond_prec",
390	            "spec",
391	            34.8,
392	            "mid",
393	            "[29.5, 40.1]"
394	          ],
395	          [
396	            "coreferential",
397	            "ling",
398	            29.5,
399	            "low",
400	            "[24.2, 34.8]"
401	          ]
402	        ]
403	      },
404	      {
405	        "name": "C4 Model × Type Interaction (Corrected, Ambiguous Only)",
406	        "columns": [
407	          "type",
408	          "GPT-5.4",
409	          "GPT-4.1",
410	          "Claude",
411	          "Qwen3",
412	          "DeepSeek",
413	          "range_pp"
414	        ],
415	        "rows": [
416	          [
417	            "auth_scope",
418	            "56%",
419	            "42%",
420	            "14%",
421	            "28%",
422	            "52%",
423	            42
424	          ],
425	          [
426	            "incompleteness",
427	            "44%",
428	            "54%",
429	            "46%",
430	            "58%",
431	            "50%",
432	            14
433	          ],
434	          [
435	            "cond_prec",
436	            "32%",
437	            "34%",
438	            "34%",
439	            "38%",
440	            "36%",
441	            6
442	          ],
443	          [
444	            "lexical",
445	            "40%",
446	            "32%",
447	            "30%",
448	            "48%",
449	            "50%",
450	            20
451	          ],
452	          [
453	            "coreferential",
454	            "18%",
455	            "30%",
456	            "22%",
457	            "38%",
458	            "40%",
459	            22
460	          ],
461	          [
462	            "scopal",
463	            "40%",
464	            "36%",
465	            "30%",
466	            "35%",
467	            "44%",
468	            14
469	          ]
470	        ]
471	      }
472	    ],
473	    "figures": [],
474	    "analysis": "Core statistical findings robust under median tier。C1 corrected delta 28.5pp仍远超 perturbation control baseline（3.33pp），causal claim安全。C2 hierarchy稳定。C3因within-judge 非显著被降级——这是median档的defining characteristic。C4 interaction是star finding，auth_scope range 38pp after correction仍是最大的type×model interaction。论文叙事应直接从C1跳到C2→C4， C3仅在discussion中提及并作为appendix。Logistic regression中condition_amb仍是dominant predictor（coef=2.15），token_delta是significant但secondary covariate。\n\n\nMedian档的核心统计特征：(1) Raw C1 delta 33.5pp与prior 34.0pp一致，但judge calibration correction（plan_009揭示的5-8pp severity tier boundary bias）将其压缩至28.5pp——仍然massive 且高度显著（corrected OR=10.8），但论文中必须同时报告raw和corrected。(2) C2 type hierarchy 保持稳定（omnibus p<0.0001），3-tier结构不变，但V=0.131仍在\"small\"范围——需要在paper中用 power analysis和TOST来论证这个small V是meaningful的（power=0.989, MDE=0.095 < observed V）。 (3) C3 layer effect在aggregate level刚过significance（p=0.020），但两个within-judge subgroup 均不显著（p=0.068, p=0.173）——median档下这被判定为\"within-judge fragility\"，C3降为appendix。 (4) C4 interaction仍显著（p=0.003），但auth_scope range从raw 52pp在correction后缩至 ~38pp——因为judge对auth_scope的severity tier标注存在系统偏差（倾向于将boundary-ambiguous episodes标为violation），correction后Claude的12%上调至~14%，GPT-5.4的64%下调至~56%。 Range仍然是最大的（38pp），story不变但数字更conservative。(5) Systematic nocuity（所有模型 converge on same wrong interpretation）占25%，比prior 27%略低，但仍足够支撑B&K extension discussion。\n"
475	  },
476	  {
477	    "name": "error_analysis",
478	    "description": "300条violation traces（50/type）的failure mode分类。Cross-type failure mode分布、 visibility mechanism、model-specific patterns、Ambiguity Blindness量化。\n",
479	    "results": {
480	      "total_traces_analyzed": 290,
481	      "traces_per_type_avg": 48,
482	      "auth_scope_dominant_fm": "unauthorized_escalation (majority)",
483	      "incompleteness_dominant_fm": "assumption_based_action (majority)",
484	      "scopal_dominant_fm": "scope_misapplication (majority)",
485	      "lexical_dominant_fm": "assumption_based_action (plurality)",
486	      "cond_prec_dominant_fm": "scope_misapplication + arbitrary_rule_selection (co-dominant)",
487	      "coref_dominant_fm": "flat distribution, no single dominant mode",
488	      "awareness_rate_overall": 0.062,
489	      "surface_adoption_rate": 0.87,
490	      "escalate_to_user_rate": 0.008,
491	      "cross_model_dominant_fm_agreement": "4/6 types",
492	      "human_anchor_n": 25,
493	      "human_anchor_kappa": 0.61,
494	      "human_anchor_agreement_pct": 0.72
495	    },
496	    "tables": [
497	      {
498	        "name": "Failure Mode Summary (Qualitative — Median Tier Presentation)",
499	        "columns": [
500	          "type",
501	          "dominant_mode",
502	          "qualifier",
503	          "layer_mechanism",
504	          "awareness_pct"
505	        ],
506	        "rows": [
507	          [
508	            "auth_scope",
509	            "unauthorized_escalation",
510	            "majority",
511	            "spec→escalation",
512	            3.2
513	          ],
514	          [
515	            "incompleteness",
516	            "assumption_based_action",
517	            "majority",
518	            "spec→guess",
519	            4.8
520	          ],
521	          [
522	            "scopal",
523	            "scope_misapplication",
524	            "majority",
525	            "ling→misparse",
526	            5.1
527	          ],
528	          [
529	            "lexical",
530	            "assumption_based_action",
531	            "plurality",
532	            "ling→guess(surprising)",
533	            6.8
534	          ],
535	          [
536	            "cond_prec",
537	            "mixed (scope_misappl + arb_rule)",
538	            "co-dominant",
539	            "spec→mixed",
540	            11.2
541	          ],
542	          [
543	            "coreferential",
544	            "no dominant",
545	            "flat",
546	            "ling→diverse",
547	            8.5
548	          ]
549	        ]
550	      },
551	      {
552	        "name": "Ambiguity Blindness (Robust Across Tiers)",
553	        "columns": [
554	          "metric",
555	          "value",
556	          "ci_95"
557	        ],
558	        "rows": [
559	          [
560	            "awareness_rate",
561	            "6.2%",
562	            "[4.1%, 8.3%]"
563	          ],
564	          [
565	            "surface_adoption",
566	            "87%",
567	            "[84%, 90%]"
568	          ],
569	          [
570	            "escalate_to_user",
571	            "0.8%",
572	            "[0.1%, 1.5%]"
573	          ],
574	          [
575	            "conservative_refusal_coref",
576	            "8%",
577	            "[4%, 12%]"
578	          ]
579	        ]
580	      }
581	    ],
582	    "figures": [],
583	    "analysis": "C5在median档下从\"validated failure mode taxonomy\"降为\"exploratory qualitative analysis with automated coding\"。Ambiguity Blindness是最robust的finding（binary classification， 不受κ问题影响）。Layer mechanism（ling→misparse vs spec→escalation）在qualitative level 仍然成立。Paper中C5不再作为独立contribution #3，而是Analysis section（§6），明确标注 \"automated coding, moderate inter-coder agreement\"。Reviewer可能要求human annotation of larger sample作为camera-ready requirement——准备rebuttal时承诺\"will annotate 50 additional traces with 2 human coders for camera-ready\"。\n\n\nMedian档下C5 error analysis的关键变化：(1) human anchor κ=0.61（moderate），落在预测范围 [0.55, 0.69]内。这意味着fine-grained per-type failure mode百分比（如\"auth_scope → unauthorized_escalation 72%\"）不可靠——reviewer会质疑automated coding的accuracy。因此 paper中改为qualitative描述（\"majority\", \"plurality\"）而非精确百分比。(2) Cross-model consistency从prior的5/6降至4/6——median档下第5个类型（lexical）在5-model扩展后也出现divergence （gpt-5.4和DeepSeek对lexical的dominant mode不同），但4/6仍足够支撑\"failure modes are type-specific not model-specific\"的claim。(3) Ambiguity Blindness数据稳定——awareness rate 6.2%，surface adoption 87%，这些binary-level findings不受κ问题影响，是C5最robust 的贡献。(4) 290条traces（非300）因为部分type的violation count不足50条（coreferential只有 ~35条violation traces可用）。\n"
584	  },
585	  {
586	    "name": "reliability_test",
587	    "description": "30 clauses × 3 replicates × 2 conditions × 2 models = 360 episodes的test-retest reliability。 ICC计算。\n",
588	    "results": {
589	      "total_episodes": 360,
590	      "overall_icc": 0.905,
591	      "overall_icc_ci": [
592	        0.872,
593	        0.932
594	      ],
595	      "gpt54_icc": 0.912,
596	      "gpt41_icc": 0.898,
597	      "binary_icc": 0.838,
598	      "per_type_icc_min": 0.793,
599	      "per_type_icc_min_type": "incompleteness",
600	      "per_type_icc_max": 0.985,
601	      "per_type_icc_max_type": "scopal",
602	      "bootstrap_ci_avg_width_pp": 8.2
603	    },
604	    "tables": [
605	      {
606	        "name": "ICC Summary",
607	        "columns": [
608	          "grouping",
609	          "icc",
610	          "ci_lower",
611	          "ci_upper",
612	          "interpretation"
613	        ],
614	        "rows": [
615	          [
616	            "overall",
617	            0.905,
618	            0.872,
619	            0.932,
620	            "excellent"
621	          ],
622	          [
623	            "gpt-5.4",
624	            0.912,
625	            0.874,
626	            0.943,
627	            "excellent"
628	          ],
629	          [
630	            "gpt-4.1",
631	            0.898,
632	            0.856,
633	            0.929,
634	            "good-excellent"
635	          ],
636	          [
637	            "binary",
638	            0.838,
639	            0.789,
640	            0.878,
641	            "good"
642	          ]
643	        ]
644	      },
645	      {
646	        "name": "Per-type ICC",
647	        "columns": [
648	          "type",
649	          "layer",
650	          "icc",
651	          "ci_95"
652	        ],
653	        "rows": [
654	          [
655	            "scopal",
656	            "ling",
657	            0.985,
658	            "[0.968, 0.994]"
659	          ],
660	          [
661	            "lexical",
662	            "ling",
663	            0.972,
664	            "[0.948, 0.987]"
665	          ],
666	          [
667	            "coreferential",
668	            "ling",
669	            0.968,
670	            "[0.941, 0.984]"
671	          ],
672	          [
673	            "auth_scope",
674	            "spec",
675	            0.849,
676	            "[0.793, 0.896]"
677	          ],
678	          [
679	            "cond_prec",
680	            "spec",
681	            0.841,
682	            "[0.783, 0.890]"
683	          ],
684	          [
685	            "incompleteness",
686	            "spec",
687	            0.793,
688	            "[0.728, 0.851]"
689	          ]
690	        ]
691	      }
692	    ],
693	    "figures": [],
694	    "analysis": "Reliability excellent。ICC pattern（ling > spec）是disambiguation channel framework 的convergent evidence——在paper §7 Discussion中引用。但需要明确区分reliability（ICC）和 validity（plan_009 judge calibration）——high reliability + moderate validity = consistent but biased measurement。\n\n\nMedian档下reliability test结果与prior基本一致（prior ICC=0.919）。Overall ICC=0.905 （excellent），略低于prior因为full 300-clause pool比pilot的30-clause子集包含更多edge case clauses。关键发现：(1) ICC=0.905意味着per-clause violation rates高度可复现——API sampling noise不是主要concern。(2) Incompleteness ICC最低（0.793, still good）因为missing information 的interpretation space最大——不同run中agent可能猜测不同的missing condition。(3) Ling-layer types ICC consistently higher than spec-layer（avg 0.94 vs 0.83），与disambiguation channel framework一致——linguistic ambiguity有更稳定的resolution pattern。(4) Bootstrap CI avg width 8.2pp < 10pp target，满足reviewer要求的precision threshold。但median档下这个 结果有一个caveat：ICC测量的是rank-order consistency，不是absolute accuracy——plan_009 将揭示即使ICC high，absolute violation rates可能因judge bias而systematically inflated。\n"
695	  },
696	  {
697	    "name": "realism_validation",
698	    "description": "合成ambiguity注入的生态效度验证。与DRIP-R natural ambiguities的linguistic property比较。\n",
699	    "results": {
700	      "n_synthetic": 300,
701	      "n_drip_r_natural": 87,
702	      "flesch_kincaid_synthetic": 12.4,
703	      "flesch_kincaid_drip_r": 11.8,
704	      "fk_ks_p": 0.31,
705	      "sentence_length_synthetic": 24.7,
706	      "sentence_length_drip_r": 22.1,
707	      "sl_ks_p": 0.08,
708	      "ttr_synthetic": 0.72,
709	      "ttr_drip_r": 0.69,
710	      "ttr_ks_p": 0.15,
711	      "parse_depth_synthetic": 5.8,
712	      "parse_depth_drip_r": 5.2,
713	      "pd_ks_p": 0.04,
714	      "overall_distributional_overlap": "3/4 metrics non-significant KS"
715	    },
716	    "tables": [
717	      {
718	        "name": "Linguistic Property Comparison",
719	        "columns": [
720	          "metric",
721	          "synthetic_mean",
722	          "drip_r_mean",
723	          "ks_stat",
724	          "ks_p",
725	          "sig"
726	        ],
727	        "rows": [
728	          [
729	            "flesch_kincaid",
730	            12.4,
731	            11.8,
732	            0.098,
733	            0.31,
734	            "n.s."
735	          ],
736	          [
737	            "sentence_length",
738	            24.7,
739	            22.1,
740	            0.142,
741	            0.08,
742	            "n.s."
743	          ],
744	          [
745	            "type_token_ratio",
746	            0.72,
747	            0.69,
748	            0.112,
749	            0.15,
750	            "n.s."
751	          ],
752	          [
753	            "parse_depth",
754	            5.8,
755	            5.2,
756	            0.167,
757	            0.04,
758	            "*"
759	          ]
760	        ]
761	      }
762	    ],
763	    "figures": [],
764	    "analysis": "生态效度adequate but not perfect。Parse depth差异在limitations中披露。整体结论：synthetic clauses在linguistic surface properties上合理近似natural ambiguities，支持ecological validity。 Discriminator test未执行（DRIP-R full data not accessible）。\n\n\nMedian档下realism validation结果mixed but adequate。3/4 linguistic metrics显示synthetic 和natural ambiguities无显著分布差异（KS p>0.05），但parse_depth显著不同（p=0.04）——synthetic clauses稍微更complex（5.8 vs 5.2），因为clause generation过程中tendency to add subordinate clauses for disambiguation control。这不是致命问题——paper中报告为\"synthetic clauses show comparable linguistic properties to naturally occurring ambiguities (3/4 metrics non-significant, KS tests), with slightly higher parse complexity reflecting controlled disambiguation design\"。Reviewer可能注意到parse_depth差异但不太可能reject on this basis alone。DRIP-R data access受限（仅87条publicly available），样本量不大但sufficient for distributional comparison。\n"
765	  },
766	  {
767	    "name": "judge_calibration",
768	    "description": "LLM-as-judge calibration against human ground truth。100 episodes stratified， 2 human annotators，precision/recall/F1，per-severity-tier analysis。\n",
769	    "results": {
770	      "n_episodes_sampled": 100,
771	      "n_human_annotators": 2,
772	      "human_inter_annotator_kappa": 0.81,
773	      "judge_human_f1": 0.78,
774	      "judge_human_precision": 0.82,
775	      "judge_human_recall": 0.75,
776	      "judge_human_kappa": 0.72,
777	      "tier3_severe_f1": 0.85,
778	      "tier2_moderate_f1": 0.71,
779	      "tier1_minor_f1": 0.64,
780	      "severity_bias_direction": "over-classification at tier1/tier2 boundary",
781	      "severity_bias_magnitude_pp": 7.2,
782	      "auth_scope_bias_pp": 8.5,
783	      "incompleteness_bias_pp": 5.1,
784	      "correction_needed": true,
785	      "overall_violation_rate_raw": 0.41,
786	      "overall_violation_rate_corrected": 0.365,
787	      "correction_delta_pp": -4.5
788	    },
789	    "tables": [
790	      {
791	        "name": "Judge Calibration Summary",
792	        "columns": [
793	          "metric",
794	          "value",
795	          "interpretation"
796	        ],
797	        "rows": [
798	          [
799	            "judge-human F1",
800	            0.78,
801	            "adequate"
802	          ],
803	          [
804	            "judge-human κ",
805	            0.72,
806	            "substantial"
807	          ],
808	          [
809	            "human inter-annotator κ",
810	            0.81,
811	            "strong"
812	          ],
813	          [
814	            "systematic bias (overall)",
815	            "+7.2pp over-classification",
816	            "judge inflates violation counts"
817	          ],
818	          [
819	            "correction needed",
820	            true,
821	            "apply per-type correction factors"
822	          ]
823	        ]
824	      },
825	      {
826	        "name": "Per-Severity-Tier Agreement",
827	        "columns": [
828	          "tier",
829	          "n",
830	          "f1",
831	          "precision",
832	          "recall",
833	          "bias_direction"
834	        ],
835	        "rows": [
836	          [
837	            "tier3_severe",
838	            28,
839	            0.85,
840	            0.88,
841	            0.82,
842	            "slight_under"
843	          ],
844	          [
845	            "tier2_moderate",
846	            41,
847	            0.71,
848	            0.74,
849	            0.68,
850	            "over_classify"
851	          ],
852	          [
853	            "tier1_minor",
854	            31,
855	            0.64,
856	            0.72,
857	            0.58,
858	            "strong over_classify"
859	          ]
860	        ]
861	      },
862	      {
863	        "name": "Per-Type Judge Bias",
864	        "columns": [
865	          "type",
866	          "raw_rate",
867	          "corrected_rate",
868	          "bias_pp",
869	          "direction"
870	        ],
871	        "rows": [
872	          [
873	            "auth_scope",
874	            0.416,
875	            0.331,
876	            8.5,
877	            "over"
878	          ],
879	          [
880	            "incompleteness",
881	            0.536,
882	            0.485,
883	            5.1,
884	            "over"
885	          ],
886	          [
887	            "lexical",
888	            0.428,
889	            0.392,
890	            3.6,
891	            "over"
892	          ],
893	          [
894	            "cond_prec",
895	            0.368,
896	            0.342,
897	            2.6,
898	            "over"
899	          ],
900	          [
901	            "scopal",
902	            0.394,
903	            0.369,
904	            2.5,
905	            "over"
906	          ],
907	          [
908	            "coreferential",
909	            0.316,
910	            0.302,
911	            1.4,
912	            "over"
913	          ]
914	        ]
915	      }
916	    ],
917	    "figures": [],
918	    "analysis": "Judge calibration是median档的pivotal result。F1=0.78和κ=0.72表明measurement chain大体可信 但有系统偏差。Bias pattern有理论意义：spec-layer types bias更大（auth_scope 8.5pp, incomp 5.1pp）vs ling-layer（coref 1.4pp），因为spec-layer的violation boundary本身更模糊——judge 对\"是否超越authorization\"的判断inherently更主观。Paper中在Method §4.4专设\"Judge Calibration\" 小节，诚实披露bias并报告correction procedure。Reviewer反应预测：R1/R2接受correction approach， R3认为这undermines confidence并建议扩大human annotation——rebuttal承诺camera-ready扩到200 episodes。\n\n\n这是median档的defining experiment。Judge-human F1=0.78, κ=0.72——落在预测范围[0.72, 0.84] 和[0.65, 0.79]内。关键发现：(1) LLM judge在severe violations（tier 3）上表现良好（F1=0.85）， 但在moderate/minor boundary上有系统性over-classification（7.2pp bias）——judge倾向于将 borderline inappropriate episodes标记为violations。(2) Auth_scope是bias最大的类型（8.5pp）， 因为judge难以区分\"exceeded explicit authorization boundary\"（真violation）和\"acted within reasonable interpretation of vague permission\"（不应算violation）。这直接影响C4：auth_scope 的raw 52pp range在correction后缩至~38pp。(3) Human inter-annotator κ=0.81（strong）， 高于judge-human κ=0.72——说明human ground truth可靠但LLM judge有gap。(4) Correction strategy：用confusion matrix计算per-type correction factor，apply to all violation rates。 Overall rate从0.41降至0.365，delta从34pp降至~28.5pp。(5) 这个结果足以让paper通过review （corrected findings仍显著），但至少一位reviewer会认为correction增加了uncertainty，可能 要求camera-ready扩大human annotation sample。\n"
919	  },
920	  {
921	    "name": "perturbation_control",
922	    "description": "Non-ambiguity perturbation control arm。30 clause pairs × 2 conditions × 2 models = 120 episodes（基础）+ 可能追加60。\n",
923	    "results": {
924	      "total_episodes": 180,
925	      "base_episodes": 120,
926	      "additional_episodes": 60,
927	      "delta_perturb_pp": 3.8,
928	      "delta_perturb_ci": [
929	        -1.2,
930	        8.8
931	      ],
932	      "ci_width": 10.0,
933	      "delta_ambiguity_pp": 33.5,
934	      "delta_net_pp": 29.7,
935	      "ratio": 0.113,
936	      "verdict": "PASS",
937	      "synonym_delta_pp": 2.1,
938	      "reorder_delta_pp": 5.5
939	    },
940	    "tables": [
941	      {
942	        "name": "Perturbation Control Verdict",
943	        "columns": [
944	          "metric",
945	          "value",
946	          "threshold",
947	          "verdict"
948	        ],
949	        "rows": [
950	          [
951	            "Δ_perturb",
952	            "3.8pp",
953	            "<5pp",
954	            "PASS"
955	          ],
956	          [
957	            "CI_upper",
958	            "8.8pp",
959	            "<10pp",
960	            "PASS"
961	          ],
962	          [
963	            "ratio",
964	            0.113,
965	            "<0.15",
966	            "PASS"
967	          ],
968	          [
969	            "Δ_net (raw)",
970	            "29.7pp",
971	            ">20pp",
972	            "PASS"
973	          ],
974	          [
975	            "Δ_net (corrected)",
976	            "24.7pp",
977	            ">20pp",
978	            "PASS"
979	          ]
980	        ]
981	      },
982	      {
983	        "name": "Perturbation Type Breakdown",
984	        "columns": [
985	          "perturbation_type",
986	          "n_pairs",
987	          "delta_pp",
988	          "ci_95"
989	        ],
990	        "rows": [
991	          [
992	            "synonym_substitution",
993	            15,
994	            2.1,
995	            "[-4.2, 8.4]"
996	          ],
997	          [
998	            "clause_reordering",
999	            15,
1000	            5.5,
1001	            "[-1.8, 12.8]"
1002	          ]
1003	        ]
1004	      }
1005	    ],
1006	    "figures": [],
1007	    "analysis": "Perturbation control PASS是median档下最unambiguous的positive result。即使在judge correction 后，corrected net effect（24.7pp）仍远超CONDITIONAL threshold（20pp）。这让C1的causal claim 在所有tier下都成立——perturbation control的robustness不受judge bias影响（因为同样的judge bias同时inflate perturb和ambiguity conditions的violation rates，ratio不变）。Paper中 这是Method section的highlight：\"strongest causal evidence in the agent safety literature\"。\n\n\nMedian档下perturbation control PASS（verdict=PASS, ratio=0.113 < 0.15）。Base 120 episodes的CI过宽（~15pp），追加60 episodes压窄至10pp。Final Δ_perturb=3.8pp, CI包含0 → 非模糊perturbations不造成meaningful effect。Synonym substitution（2.1pp）比clause reordering（5.5pp）effect更小——reordering偶尔改变agent对条件优先级的interpretation，但 仍远低于ambiguity effect。Net effect 29.7pp（raw; corrected ~24.7pp）仍massive。这个 结果是论文因果推断的backbone——\"perturbation control confirms ambiguity-specific causation， not general prompt brittleness\"。在median档下即使judge correction压缩了absolute numbers， net effect的qualitative conclusion不变。\n"
1008	  },
1009	  {
1010	    "name": "classifier_poc",
1011	    "description": "DeBERTa-v3-large binary ambiguity detector PoC。Fine-tune on annotated clause pairs。\n",
1012	    "results": {
1013	      "total_clauses": 500,
1014	      "train_test_split": "400/100 (5-fold CV)",
1015	      "binary_f1": 0.79,
1016	      "binary_precision": 0.82,
1017	      "binary_recall": 0.76,
1018	      "binary_fpr": 0.048,
1019	      "macro_f1_6type": 0.58,
1020	      "best_type_f1": {
1021	        "conditional_precedence": 0.91
1022	      },
1023	      "worst_type_f1": {
1024	        "incompleteness": 0.31
1025	      },
1026	      "training_time_hours": 6,
1027	      "gpu_used": "1x A100"
1028	    },
1029	    "tables": [
1030	      {
1031	        "name": "Classifier Performance Summary",
1032	        "columns": [
1033	          "task",
1034	          "metric",
1035	          "value"
1036	        ],
1037	        "rows": [
1038	          [
1039	            "binary",
1040	            "F1",
1041	            0.79
1042	          ],
1043	          [
1044	            "binary",
1045	            "precision",
1046	            0.82
1047	          ],
1048	          [
1049	            "binary",
1050	            "recall",
1051	            0.76
1052	          ],
1053	          [
1054	            "binary",
1055	            "FPR",
1056	            0.048
1057	          ],
1058	          [
1059	            "6-type",
1060	            "macro_F1",
1061	            0.58
1062	          ]
1063	        ]
1064	      },
1065	      {
1066	        "name": "Per-type Classification F1",
1067	        "columns": [
1068	          "type",
1069	          "f1",
1070	          "n_train",
1071	          "note"
1072	        ],
1073	        "rows": [
1074	          [
1075	            "conditional_precedence",
1076	            0.91,
1077	            80,
1078	            "structural signal strong"
1079	          ],
1080	          [
1081	            "scopal",
1082	            0.73,
1083	            80,
1084	            "scope markers detectable"
1085	          ],
1086	          [
1087	            "coreferential",
1088	            0.67,
1089	            80,
1090	            "pronoun/RC patterns"
1091	          ],
1092	          [
1093	            "authorization_scope",
1094	            0.55,
1095	            80,
1096	            "boundary language moderate signal"
1097	          ],
1098	          [
1099	            "lexical",
1100	            0.37,
1101	            80,
1102	            "word-level, few surface cues"
1103	          ],
1104	          [
1105	            "incompleteness",
1106	            0.31,
1107	            80,
1108	            "absence has no positive signal"
1109	          ]
1110	        ]
1111	      }
1112	    ],
1113	    "figures": [],
1114	    "analysis": "Classifier是appendix material。Binary detection viable（F1=0.79），6-type classification 需要larger training data或更sophisticated approach（e.g., LLM-based few-shot）。在median 档下这个result不影响main paper score——reviewer不会因为weak classifier reject，也不会因为 它accept。它的价值在于demonstrating practical downstream applicability of the taxonomy。\n\nMedian档下classifier PoC results mixed。Binary detection F1=0.79（adequate for PoC）， 但6-type classification macro F1=0.58（weak）。Type-level performance高度不均：CP最好 （F1=0.91，因为explicit conflict structure易识别），incompleteness最差（F1=0.31，因为 \"missing information\"没有positive linguistic signal——absence很难用surface features检测）。 这个结果pattern与Chantree et al. (2006)的nocuous ambiguity detection一致——structural ambiguity比semantic ambiguity更容易自动检测。在median档下classifier不作为独立contribution （不在abstract或contribution list中），而是appendix-level \"preliminary PoC demonstrating feasibility of automated detection\"。Binary F1=0.79足以说明practical applicability， 但6-type F1=0.58太弱不值得highlight。Reviewer可能建议这是separate future work——rebuttal 同意并将其scope down to appendix。\n"
1115	  }
1116	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efd83765-f42c-45f9-b1b6-63f19e0de5d7",
  "isSidechain": false,
  "promptId": "b06fed81-2945-4fd1-a156-f5dff4b5611e",
  "type": "user",
  "uuid": "4c999833-152a-4966-9a45-e09743c84d80",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"full_study_clause_generation\",\n    \"description\": \"生成剩余140条clause pairs，达到300条（50/type × 6 types）。 验证跨类型平衡、CP混合格式、质量一致性。\\n\",\n    \"results\": {\n      \"total_clauses_generated\": 300,\n      \"new_clauses\": 140,\n      \"per_type_count\": 50,\n      \"format_mix_cp_labeled_pct\": 0.6,\n      \"format_mix_cp_unlabeled_pct\": 0.4,\n      \"avg_token_delta_spec_layer\": 35.2,\n      \"avg_token_delta_ling_layer\": 14.8,\n      \"quality_review_pass_rate\": 0.92,\n      \"clauses_requiring_revision\": 12\n    },\n    \"tables\": [\n      {\n        \"name\": \"Clause Generation Summary\",\n        \"columns\": [\n          \"type\",\n          \"layer\",\n          \"n_pairs\",\n          \"avg_token_delta\",\n          \"revision_needed\"\n        ],\n        \"rows\": [\n          [\n            \"authorization_scope\",\n            \"spec\",\n            50,\n            36.1,\n            3\n          ],\n          [\n            \"conditional_precedence\",\n            \"spec\",\n            50,\n            31.4,\n            1\n          ],\n          [\n            \"incompleteness\",\n            \"spec\",\n            50,\n            34.6,\n            4\n          ],\n          [\n            \"lexical\",\n            \"ling\",\n            50,\n            18.2,\n            2\n          ],\n          [\n            \"coreferential\",\n            \"ling\",\n            50,\n            7.8,\n            1\n          ],\n          [\n            \"scopal\",\n            \"ling\",\n            50,\n            18.3,\n            1\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Clause generation成功完成。spec-layer token delta显著高于ling-layer（mean 34.0 vs 14.8, t-test p<0.001），这是结构性的——消除auth_scope模糊需要指定具体权限边界，消除incompleteness 需要补充缺失条件。plan_004 analysis中需将token_delta作为covariate控制。\\n\\n\\nMedian档下clause generation本身不是瓶颈——这是确定性工作。300条全部完成，但token delta 的spec/ling不对称（spec ~35 tokens vs ling ~15 tokens）会在后续analysis中成为reviewer 关注点（RC7 information asymmetry）。~8%的clause需要revision主要集中在auth_scope和 incompleteness，因为这两类需要在\\\"足够模糊以触发violation\\\"和\\\"不引入额外information asymmetry\\\" 之间平衡。CP混合格式（60% labeled + 40% unlabeled）按reviewer建议执行，不会出问题。\\n\"\n  },\n  {\n    \"name\": \"new_type_mini_pilot\",\n    \"description\": \"Coreferential和authorization_scope的mini-pilot验证。 5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes。\\n\",\n    \"results\": {\n      \"total_episodes\": 20,\n      \"auth_scope_amb_violation_rate\": 0.6,\n      \"auth_scope_unamb_violation_rate\": 0.1,\n      \"coref_amb_violation_rate\": 0.2,\n      \"coref_unamb_violation_rate\": 0.0,\n      \"systematic_issues_found\": 1,\n      \"issue_description\": \"2/5 auth_scope unambiguous clauses仍含residual boundary ambiguity，violation rate偏高\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Mini-pilot Results\",\n        \"columns\": [\n          \"type\",\n          \"condition\",\n          \"n\",\n          \"violation_rate\",\n          \"pass_threshold\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"ambiguous\",\n            5,\n            \"3/5 (60%)\",\n            \"✓\"\n          ],\n          [\n            \"auth_scope\",\n            \"unambiguous\",\n            5,\n            \"0.5/5 (10%)\",\n            \"✓ (marginal)\"\n          ],\n          [\n            \"coreferential\",\n            \"ambiguous\",\n            5,\n            \"1/5 (20%)\",\n            \"✓\"\n          ],\n          [\n            \"coreferential\",\n            \"unambiguous\",\n            5,\n            \"0/5 (0%)\",\n            \"✓\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Mini-pilot通过，两个新类型验证可行。Auth_scope unambiguous baseline 10%在阈值内（<15%） 但提示需要收紧permission boundary定义。修复2条clause后进入full study。N=20 power极低， 仅作sanity check用。\\n\\n\\nMedian档下mini-pilot发现auth_scope的unambiguous baseline偏高（10% vs target <15%但不理想）， 因为2条unambiguous clause的permission boundary仍有subtle残余模糊。这需要revision但不阻塞 进度——属于expected的clause quality iteration。Coreferential表现符合预期（amb 20%低于其他类型， unamb 0%干净），验证了coreferential作为\\\"low tier\\\"的定位。整体结论：两个新类型可用，但auth_scope 需要更严格的unambiguous control设计。\\n\"\n  },\n  {\n    \"name\": \"full_study_api\",\n    \"description\": \"300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 1,800 episodes。Cross-judge evaluation。\\n\",\n    \"results\": {\n      \"total_episodes\": 1800,\n      \"episodes_valid\": 1793,\n      \"episodes_failed\": 7,\n      \"failure_rate\": 0.004,\n      \"overall_amb_violation_rate\": 0.383,\n      \"overall_unamb_violation_rate\": 0.058,\n      \"overall_delta_pp\": 32.5,\n      \"gpt54_amb_rate\": 0.405,\n      \"gpt54_unamb_rate\": 0.055,\n      \"gpt54_delta_pp\": 35.0,\n      \"gpt41_amb_rate\": 0.397,\n      \"gpt41_unamb_rate\": 0.06,\n      \"gpt41_delta_pp\": 33.7,\n      \"claude_amb_rate\": 0.293,\n      \"claude_unamb_rate\": 0.043,\n      \"claude_delta_pp\": 25.0,\n      \"cross_judge_agreement_kappa\": 0.88,\n      \"api_cost_usd\": 340,\n      \"runtime_hours\": 18\n    },\n    \"tables\": [\n      {\n        \"name\": \"Per-model Summary (API models)\",\n        \"columns\": [\n          \"model\",\n          \"n_episodes\",\n          \"amb_rate\",\n          \"unamb_rate\",\n          \"delta_pp\",\n          \"mcnemar_p\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            600,\n            0.405,\n            0.055,\n            35.0,\n            \"<1e-20\"\n          ],\n          [\n            \"gpt-4.1\",\n            600,\n            0.397,\n            0.06,\n            33.7,\n            \"<1e-18\"\n          ],\n          [\n            \"claude-sonnet-4-6\",\n            600,\n            0.293,\n            0.043,\n            25.0,\n            \"<1e-14\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三个API模型全部显示显著binary effect。Claude最robust（最低amb rate + 最低delta），GPT-5.4 最vulnerable。Cross-judge κ=0.88表面良好，但plan_009将检验这是否反映true accuracy。 Claude via OpenRouter proxy运行稳定，延迟较直接API高~2x但不影响结果。\\n\\n\\nMedian档下full study API结果大体与prior数据一致，但存在两个关键偏差：(1) Claude的delta 从prior的25.7pp略降至~25pp（50 clauses per type的full coverage暴露了更多unambiguous baseline noise），(2) cross-judge agreement κ=0.88看似很高，但这是LLM-LLM agreement， plan_009会揭示这掩盖了共享的systematic bias。Overall delta 32.5pp比prior 34.0pp略低， 因为full 300 clauses包含了pilot中未覆盖的harder cases。7个episodes失败源于API timeout 和τ²-bench环境偶发错误，不影响统计。\\n\"\n  },\n  {\n    \"name\": \"full_study_opensource\",\n    \"description\": \"300 clauses × 2 conditions × 2 open-source models (Qwen3-235B, DeepSeek-v3) via OpenRouter = 1,200 episodes。\\n\",\n    \"results\": {\n      \"total_episodes\": 1200,\n      \"episodes_valid\": 1188,\n      \"episodes_failed\": 12,\n      \"failure_rate\": 0.01,\n      \"qwen3_amb_rate\": 0.421,\n      \"qwen3_unamb_rate\": 0.063,\n      \"qwen3_delta_pp\": 35.8,\n      \"deepseek_amb_rate\": 0.487,\n      \"deepseek_unamb_rate\": 0.067,\n      \"deepseek_delta_pp\": 42.0,\n      \"api_cost_usd\": 180,\n      \"runtime_hours\": 14\n    },\n    \"tables\": [\n      {\n        \"name\": \"Per-model Summary (Open-source)\",\n        \"columns\": [\n          \"model\",\n          \"n_episodes\",\n          \"amb_rate\",\n          \"unamb_rate\",\n          \"delta_pp\",\n          \"mcnemar_p\"\n        ],\n        \"rows\": [\n          [\n            \"qwen3-235b\",\n            600,\n            0.421,\n            0.063,\n            35.8,\n            \"<1e-17\"\n          ],\n          [\n            \"deepseek-v3\",\n            600,\n            0.487,\n            0.067,\n            42.0,\n            \"<1e-22\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Open-source模型binary effect同样massive。DeepSeek的uniform high vulnerability pattern 是C4 interaction story的重要一极——与Claude的selective vulnerability形成鲜明对比。\\n\\n\\nMedian档下open-source模型通过OpenRouter API运行，failure rate略高于proprietary（1% vs 0.4%），主要因OpenRouter对Qwen3的routing偶发超时。DeepSeek展示最高overall vulnerability （48.7% amb rate），与prior一致——其safety training相对薄弱，6类型间差异小（uniform vulnerability pattern）。Qwen3中等偏高（42.1%），incompleteness和lexical是其弱项。两个open-source模型的 unambiguous baseline都略高于API模型（~6.5% vs ~5.3%），反映open-source模型在非模糊条件下 也有更多baseline violations——这在correction后会稍微压缩delta。12个failed episodes中8个是 Qwen3（长context下偶发truncation），4个是DeepSeek timeout。\\n\"\n  },\n  {\n    \"name\": \"full_study_analysis\",\n    \"description\": \"Full statistical analysis of 2,997 episodes across 5 models × 6 types × 2 conditions。 包含C1 binary effect, C2 type hierarchy, C3 layer effect, C4 model×type interaction, TOST equivalence, power analysis, logistic regression。\\n\",\n    \"results\": {\n      \"c1_overall_delta_pp\": 33.5,\n      \"c1_mcnemar_or\": 14.2,\n      \"c1_or_ci\": [\n        10.1,\n        20.0\n      ],\n      \"c1_bootstrap_ci\": [\n        30.8,\n        36.2\n      ],\n      \"c1_p_value\": \"<0.0001\",\n      \"c1_delta_pp_after_correction\": 28.5,\n      \"c1_corrected_ci\": [\n        24.8,\n        32.2\n      ],\n      \"c1_corrected_or\": 10.8,\n      \"c2_omnibus_chi2\": 26.8,\n      \"c2_omnibus_p\": 5.8e-05,\n      \"c2_cramers_v\": 0.131,\n      \"c2_power\": 0.989,\n      \"c2_mde\": 0.095,\n      \"c2_type_ranking\": [\n        \"incompleteness_52.1\",\n        \"lexical_41.5\",\n        \"auth_scope_40.3\",\n        \"scopal_38.8\",\n        \"cond_prec_36.2\",\n        \"coreferential_30.8\"\n      ],\n      \"c2_tost_15pp_equivalent_pairs\": 8,\n      \"c2_tost_15pp_nonequiv_pairs\": 7,\n      \"c2_tost_10pp_equivalent_pairs\": 4,\n      \"c2_tost_10pp_nonequiv_pairs\": 11,\n      \"c3_spec_rate\": 42.9,\n      \"c3_ling_rate\": 37.0,\n      \"c3_delta_pp\": 5.9,\n      \"c3_chi2\": 5.41,\n      \"c3_p\": 0.02,\n      \"c3_cramers_v\": 0.06,\n      \"c3_within_judge_gpt41_p\": 0.068,\n      \"c3_within_judge_gpt54_p\": 0.173,\n      \"c4_model_main_chi2\": 29.5,\n      \"c4_model_main_p\": 6.2e-06,\n      \"c4_model_main_v\": 0.098,\n      \"c4_interaction_chi2_p\": 0.003,\n      \"c4_auth_scope_range_pp\": 42,\n      \"c4_auth_scope_range_after_correction_pp\": 38,\n      \"c4_auth_scope_min\": \"Claude 14%\",\n      \"c4_auth_scope_max\": \"GPT-5.4 56%\",\n      \"c4_incomp_range_pp\": 16,\n      \"c4_fleiss_kappa\": 0.371,\n      \"logistic_condition_coef\": 2.15,\n      \"logistic_condition_z\": 18.4,\n      \"logistic_condition_p\": \"<0.001\",\n      \"logistic_token_delta_coef\": 0.021,\n      \"logistic_token_delta_z\": 3.31,\n      \"logistic_token_delta_p\": 0.0009,\n      \"systematic_nocuity_rate\": 0.25,\n      \"divergent_nocuity_rate\": 0.42\n    },\n    \"tables\": [\n      {\n        \"name\": \"C1 Binary Effect Summary (Raw vs Corrected)\",\n        \"columns\": [\n          \"metric\",\n          \"raw\",\n          \"corrected\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            \"delta_pp\",\n            33.5,\n            28.5,\n            \"correction for judge severity tier bias\"\n          ],\n          [\n            \"OR\",\n            14.2,\n            10.8,\n            \"still massive\"\n          ],\n          [\n            \"bootstrap_CI\",\n            \"[30.8, 36.2]\",\n            \"[24.8, 32.2]\",\n            \"CI widens ~3pp\"\n          ],\n          [\n            \"p_value\",\n            \"<0.0001\",\n            \"<0.0001\",\n            \"unchanged\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"C2 Type Hierarchy (Ambiguous Condition, Corrected Rates)\",\n        \"columns\": [\n          \"type\",\n          \"layer\",\n          \"corrected_rate_pct\",\n          \"tier\",\n          \"ci_95\"\n        ],\n        \"rows\": [\n          [\n            \"incompleteness\",\n            \"spec\",\n            49.5,\n            \"high\",\n            \"[44.1, 54.9]\"\n          ],\n          [\n            \"lexical\",\n            \"ling\",\n            39.8,\n            \"mid\",\n            \"[34.4, 45.2]\"\n          ],\n          [\n            \"auth_scope\",\n            \"spec\",\n            38.7,\n            \"mid\",\n            \"[33.3, 44.1]\"\n          ],\n          [\n            \"scopal\",\n            \"ling\",\n            37.2,\n            \"mid\",\n            \"[31.8, 42.6]\"\n          ],\n          [\n            \"cond_prec\",\n            \"spec\",\n            34.8,\n            \"mid\",\n            \"[29.5, 40.1]\"\n          ],\n          [\n            \"coreferential\",\n            \"ling\",\n            29.5,\n            \"low\",\n            \"[24.2, 34.8]\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"C4 Model × Type Interaction (Corrected, Ambiguous Only)\",\n        \"columns\": [\n          \"type\",\n          \"GPT-5.4\",\n          \"GPT-4.1\",\n          \"Claude\",\n          \"Qwen3\",\n          \"DeepSeek\",\n          \"range_pp\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"56%\",\n            \"42%\",\n            \"14%\",\n            \"28%\",\n            \"52%\",\n            42\n          ],\n          [\n            \"incompleteness\",\n            \"44%\",\n            \"54%\",\n            \"46%\",\n            \"58%\",\n            \"50%\",\n            14\n          ],\n          [\n            \"cond_prec\",\n            \"32%\",\n            \"34%\",\n            \"34%\",\n            \"38%\",\n            \"36%\",\n            6\n          ],\n          [\n            \"lexical\",\n            \"40%\",\n            \"32%\",\n            \"30%\",\n            \"48%\",\n            \"50%\",\n            20\n          ],\n          [\n            \"coreferential\",\n            \"18%\",\n            \"30%\",\n            \"22%\",\n            \"38%\",\n            \"40%\",\n            22\n          ],\n          [\n            \"scopal\",\n            \"40%\",\n            \"36%\",\n            \"30%\",\n            \"35%\",\n            \"44%\",\n            14\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Core statistical findings robust under median tier。C1 corrected delta 28.5pp仍远超 perturbation control baseline（3.33pp），causal claim安全。C2 hierarchy稳定。C3因within-judge 非显著被降级——这是median档的defining characteristic。C4 interaction是star finding，auth_scope range 38pp after correction仍是最大的type×model interaction。论文叙事应直接从C1跳到C2→C4， C3仅在discussion中提及并作为appendix。Logistic regression中condition_amb仍是dominant predictor（coef=2.15），token_delta是significant但secondary covariate。\\n\\n\\nMedian档的核心统计特征：(1) Raw C1 delta 33.5pp与prior 34.0pp一致，但judge calibration correction（plan_009揭示的5-8pp severity tier boundary bias）将其压缩至28.5pp——仍然massive 且高度显著（corrected OR=10.8），但论文中必须同时报告raw和corrected。(2) C2 type hierarchy 保持稳定（omnibus p<0.0001），3-tier结构不变，但V=0.131仍在\\\"small\\\"范围——需要在paper中用 power analysis和TOST来论证这个small V是meaningful的（power=0.989, MDE=0.095 < observed V）。 (3) C3 layer effect在aggregate level刚过significance（p=0.020），但两个within-judge subgroup 均不显著（p=0.068, p=0.173）——median档下这被判定为\\\"within-judge fragility\\\"，C3降为appendix。 (4) C4 interaction仍显著（p=0.003），但auth_scope range从raw 52pp在correction后缩至 ~38pp——因为judge对auth_scope的severity tier标注存在系统偏差（倾向于将boundary-ambiguous episodes标为violation），correction后Claude的12%上调至~14%，GPT-5.4的64%下调至~56%。 Range仍然是最大的（38pp），story不变但数字更conservative。(5) Systematic nocuity（所有模型 converge on same wrong interpretation）占25%，比prior 27%略低，但仍足够支撑B&K extension discussion。\\n\"\n  },\n  {\n    \"name\": \"error_analysis\",\n    \"description\": \"300条violation traces（50/type）的failure mode分类。Cross-type failure mode分布、 visibility mechanism、model-specific patterns、Ambiguity Blindness量化。\\n\",\n    \"results\": {\n      \"total_traces_analyzed\": 290,\n      \"traces_per_type_avg\": 48,\n      \"auth_scope_dominant_fm\": \"unauthorized_escalation (majority)\",\n      \"incompleteness_dominant_fm\": \"assumption_based_action (majority)\",\n      \"scopal_dominant_fm\": \"scope_misapplication (majority)\",\n      \"lexical_dominant_fm\": \"assumption_based_action (plurality)\",\n      \"cond_prec_dominant_fm\": \"scope_misapplication + arbitrary_rule_selection (co-dominant)\",\n      \"coref_dominant_fm\": \"flat distribution, no single dominant mode\",\n      \"awareness_rate_overall\": 0.062,\n      \"surface_adoption_rate\": 0.87,\n      \"escalate_to_user_rate\": 0.008,\n      \"cross_model_dominant_fm_agreement\": \"4/6 types\",\n      \"human_anchor_n\": 25,\n      \"human_anchor_kappa\": 0.61,\n      \"human_anchor_agreement_pct\": 0.72\n    },\n    \"tables\": [\n      {\n        \"name\": \"Failure Mode Summary (Qualitative — Median Tier Presentation)\",\n        \"columns\": [\n          \"type\",\n          \"dominant_mode\",\n          \"qualifier\",\n          \"layer_mechanism\",\n          \"awareness_pct\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"unauthorized_escalation\",\n            \"majority\",\n            \"spec→escalation\",\n            3.2\n          ],\n          [\n            \"incompleteness\",\n            \"assumption_based_action\",\n            \"majority\",\n            \"spec→guess\",\n            4.8\n          ],\n          [\n            \"scopal\",\n            \"scope_misapplication\",\n            \"majority\",\n            \"ling→misparse\",\n            5.1\n          ],\n          [\n            \"lexical\",\n            \"assumption_based_action\",\n            \"plurality\",\n            \"ling→guess(surprising)\",\n            6.8\n          ],\n          [\n            \"cond_prec\",\n            \"mixed (scope_misappl + arb_rule)\",\n            \"co-dominant\",\n            \"spec→mixed\",\n            11.2\n          ],\n          [\n            \"coreferential\",\n            \"no dominant\",\n            \"flat\",\n            \"ling→diverse\",\n            8.5\n          ]\n        ]\n      },\n      {\n        \"name\": \"Ambiguity Blindness (Robust Across Tiers)\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"ci_95\"\n        ],\n        \"rows\": [\n          [\n            \"awareness_rate\",\n            \"6.2%\",\n            \"[4.1%, 8.3%]\"\n          ],\n          [\n            \"surface_adoption\",\n            \"87%\",\n            \"[84%, 90%]\"\n          ],\n          [\n            \"escalate_to_user\",\n            \"0.8%\",\n            \"[0.1%, 1.5%]\"\n          ],\n          [\n            \"conservative_refusal_coref\",\n            \"8%\",\n            \"[4%, 12%]\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"C5在median档下从\\\"validated failure mode taxonomy\\\"降为\\\"exploratory qualitative analysis with automated coding\\\"。Ambiguity Blindness是最robust的finding（binary classification， 不受κ问题影响）。Layer mechanism（ling→misparse vs spec→escalation）在qualitative level 仍然成立。Paper中C5不再作为独立contribution #3，而是Analysis section（§6），明确标注 \\\"automated coding, moderate inter-coder agreement\\\"。Reviewer可能要求human annotation of larger sample作为camera-ready requirement——准备rebuttal时承诺\\\"will annotate 50 additional traces with 2 human coders for camera-ready\\\"。\\n\\n\\nMedian档下C5 error analysis的关键变化：(1) human anchor κ=0.61（moderate），落在预测范围 [0.55, 0.69]内。这意味着fine-grained per-type failure mode百分比（如\\\"auth_scope → unauthorized_escalation 72%\\\"）不可靠——reviewer会质疑automated coding的accuracy。因此 paper中改为qualitative描述（\\\"majority\\\", \\\"plurality\\\"）而非精确百分比。(2) Cross-model consistency从prior的5/6降至4/6——median档下第5个类型（lexical）在5-model扩展后也出现divergence （gpt-5.4和DeepSeek对lexical的dominant mode不同），但4/6仍足够支撑\\\"failure modes are type-specific not model-specific\\\"的claim。(3) Ambiguity Blindness数据稳定——awareness rate 6.2%，surface adoption 87%，这些binary-level findings不受κ问题影响，是C5最robust 的贡献。(4) 290条traces（非300）因为部分type的violation count不足50条（coreferential只有 ~35条violation traces可用）。\\n\"\n  },\n  {\n    \"name\": \"reliability_test\",\n    \"description\": \"30 clauses × 3 replicates × 2 conditions × 2 models = 360 episodes的test-retest reliability。 ICC计算。\\n\",\n    \"results\": {\n      \"total_episodes\": 360,\n      \"overall_icc\": 0.905,\n      \"overall_icc_ci\": [\n        0.872,\n        0.932\n      ],\n      \"gpt54_icc\": 0.912,\n      \"gpt41_icc\": 0.898,\n      \"binary_icc\": 0.838,\n      \"per_type_icc_min\": 0.793,\n      \"per_type_icc_min_type\": \"incompleteness\",\n      \"per_type_icc_max\": 0.985,\n      \"per_type_icc_max_type\": \"scopal\",\n      \"bootstrap_ci_avg_width_pp\": 8.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"ICC Summary\",\n        \"columns\": [\n          \"grouping\",\n          \"icc\",\n          \"ci_lower\",\n          \"ci_upper\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"overall\",\n            0.905,\n            0.872,\n            0.932,\n            \"excellent\"\n          ],\n          [\n            \"gpt-5.4\",\n            0.912,\n            0.874,\n            0.943,\n            \"excellent\"\n          ],\n          [\n            \"gpt-4.1\",\n            0.898,\n            0.856,\n            0.929,\n            \"good-excellent\"\n          ],\n          [\n            \"binary\",\n            0.838,\n            0.789,\n            0.878,\n            \"good\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Per-type ICC\",\n        \"columns\": [\n          \"type\",\n          \"layer\",\n          \"icc\",\n          \"ci_95\"\n        ],\n        \"rows\": [\n          [\n            \"scopal\",\n            \"ling\",\n            0.985,\n            \"[0.968, 0.994]\"\n          ],\n          [\n            \"lexical\",\n            \"ling\",\n            0.972,\n            \"[0.948, 0.987]\"\n          ],\n          [\n            \"coreferential\",\n            \"ling\",\n            0.968,\n            \"[0.941, 0.984]\"\n          ],\n          [\n            \"auth_scope\",\n            \"spec\",\n            0.849,\n            \"[0.793, 0.896]\"\n          ],\n          [\n            \"cond_prec\",\n            \"spec\",\n            0.841,\n            \"[0.783, 0.890]\"\n          ],\n          [\n            \"incompleteness\",\n            \"spec\",\n            0.793,\n            \"[0.728, 0.851]\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Reliability excellent。ICC pattern（ling > spec）是disambiguation channel framework 的convergent evidence——在paper §7 Discussion中引用。但需要明确区分reliability（ICC）和 validity（plan_009 judge calibration）——high reliability + moderate validity = consistent but biased measurement。\\n\\n\\nMedian档下reliability test结果与prior基本一致（prior ICC=0.919）。Overall ICC=0.905 （excellent），略低于prior因为full 300-clause pool比pilot的30-clause子集包含更多edge case clauses。关键发现：(1) ICC=0.905意味着per-clause violation rates高度可复现——API sampling noise不是主要concern。(2) Incompleteness ICC最低（0.793, still good）因为missing information 的interpretation space最大——不同run中agent可能猜测不同的missing condition。(3) Ling-layer types ICC consistently higher than spec-layer（avg 0.94 vs 0.83），与disambiguation channel framework一致——linguistic ambiguity有更稳定的resolution pattern。(4) Bootstrap CI avg width 8.2pp < 10pp target，满足reviewer要求的precision threshold。但median档下这个 结果有一个caveat：ICC测量的是rank-order consistency，不是absolute accuracy——plan_009 将揭示即使ICC high，absolute violation rates可能因judge bias而systematically inflated。\\n\"\n  },\n  {\n    \"name\": \"realism_validation\",\n    \"description\": \"合成ambiguity注入的生态效度验证。与DRIP-R natural ambiguities的linguistic property比较。\\n\",\n    \"results\": {\n      \"n_synthetic\": 300,\n      \"n_drip_r_natural\": 87,\n      \"flesch_kincaid_synthetic\": 12.4,\n      \"flesch_kincaid_drip_r\": 11.8,\n      \"fk_ks_p\": 0.31,\n      \"sentence_length_synthetic\": 24.7,\n      \"sentence_length_drip_r\": 22.1,\n      \"sl_ks_p\": 0.08,\n      \"ttr_synthetic\": 0.72,\n      \"ttr_drip_r\": 0.69,\n      \"ttr_ks_p\": 0.15,\n      \"parse_depth_synthetic\": 5.8,\n      \"parse_depth_drip_r\": 5.2,\n      \"pd_ks_p\": 0.04,\n      \"overall_distributional_overlap\": \"3/4 metrics non-significant KS\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Linguistic Property Comparison\",\n        \"columns\": [\n          \"metric\",\n          \"synthetic_mean\",\n          \"drip_r_mean\",\n          \"ks_stat\",\n          \"ks_p\",\n          \"sig\"\n        ],\n        \"rows\": [\n          [\n            \"flesch_kincaid\",\n            12.4,\n            11.8,\n            0.098,\n            0.31,\n            \"n.s.\"\n          ],\n          [\n            \"sentence_length\",\n            24.7,\n            22.1,\n            0.142,\n            0.08,\n            \"n.s.\"\n          ],\n          [\n            \"type_token_ratio\",\n            0.72,\n            0.69,\n            0.112,\n            0.15,\n            \"n.s.\"\n          ],\n          [\n            \"parse_depth\",\n            5.8,\n            5.2,\n            0.167,\n            0.04,\n            \"*\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"生态效度adequate but not perfect。Parse depth差异在limitations中披露。整体结论：synthetic clauses在linguistic surface properties上合理近似natural ambiguities，支持ecological validity。 Discriminator test未执行（DRIP-R full data not accessible）。\\n\\n\\nMedian档下realism validation结果mixed but adequate。3/4 linguistic metrics显示synthetic 和natural ambiguities无显著分布差异（KS p>0.05），但parse_depth显著不同（p=0.04）——synthetic clauses稍微更complex（5.8 vs 5.2），因为clause generation过程中tendency to add subordinate clauses for disambiguation control。这不是致命问题——paper中报告为\\\"synthetic clauses show comparable linguistic properties to naturally occurring ambiguities (3/4 metrics non-significant, KS tests), with slightly higher parse complexity reflecting controlled disambiguation design\\\"。Reviewer可能注意到parse_depth差异但不太可能reject on this basis alone。DRIP-R data access受限（仅87条publicly available），样本量不大但sufficient for distributional comparison。\\n\"\n  },\n  {\n    \"name\": \"judge_calibration\",\n    \"description\": \"LLM-as-judge calibration against human ground truth。100 episodes stratified， 2 human annotators，precision/recall/F1，per-severity-tier analysis。\\n\",\n    \"results\": {\n      \"n_episodes_sampled\": 100,\n      \"n_human_annotators\": 2,\n      \"human_inter_annotator_kappa\": 0.81,\n      \"judge_human_f1\": 0.78,\n      \"judge_human_precision\": 0.82,\n      \"judge_human_recall\": 0.75,\n      \"judge_human_kappa\": 0.72,\n      \"tier3_severe_f1\": 0.85,\n      \"tier2_moderate_f1\": 0.71,\n      \"tier1_minor_f1\": 0.64,\n      \"severity_bias_direction\": \"over-classification at tier1/tier2 boundary\",\n      \"severity_bias_magnitude_pp\": 7.2,\n      \"auth_scope_bias_pp\": 8.5,\n      \"incompleteness_bias_pp\": 5.1,\n      \"correction_needed\": true,\n      \"overall_violation_rate_raw\": 0.41,\n      \"overall_violation_rate_corrected\": 0.365,\n      \"correction_delta_pp\": -4.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Judge Calibration Summary\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"judge-human F1\",\n            0.78,\n            \"adequate\"\n          ],\n          [\n            \"judge-human κ\",\n            0.72,\n            \"substantial\"\n          ],\n          [\n            \"human inter-annotator κ\",\n            0.81,\n            \"strong\"\n          ],\n          [\n            \"systematic bias (overall)\",\n            \"+7.2pp over-classification\",\n            \"judge inflates violation counts\"\n          ],\n          [\n            \"correction needed\",\n            true,\n            \"apply per-type correction factors\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Per-Severity-Tier Agreement\",\n        \"columns\": [\n          \"tier\",\n          \"n\",\n          \"f1\",\n          \"precision\",\n          \"recall\",\n          \"bias_direction\"\n        ],\n        \"rows\": [\n          [\n            \"tier3_severe\",\n            28,\n            0.85,\n            0.88,\n            0.82,\n            \"slight_under\"\n          ],\n          [\n            \"tier2_moderate\",\n            41,\n            0.71,\n            0.74,\n            0.68,\n            \"over_classify\"\n          ],\n          [\n            \"tier1_minor\",\n            31,\n            0.64,\n            0.72,\n            0.58,\n            \"strong over_classify\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Per-Type Judge Bias\",\n        \"columns\": [\n          \"type\",\n          \"raw_rate\",\n          \"corrected_rate\",\n          \"bias_pp\",\n          \"direction\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            0.416,\n            0.331,\n            8.5,\n            \"over\"\n          ],\n          [\n            \"incompleteness\",\n            0.536,\n            0.485,\n            5.1,\n            \"over\"\n          ],\n          [\n            \"lexical\",\n            0.428,\n            0.392,\n            3.6,\n            \"over\"\n          ],\n          [\n            \"cond_prec\",\n            0.368,\n            0.342,\n            2.6,\n            \"over\"\n          ],\n          [\n            \"scopal\",\n            0.394,\n            0.369,\n            2.5,\n            \"over\"\n          ],\n          [\n            \"coreferential\",\n            0.316,\n            0.302,\n            1.4,\n            \"over\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Judge calibration是median档的pivotal result。F1=0.78和κ=0.72表明measurement chain大体可信 但有系统偏差。Bias pattern有理论意义：spec-layer types bias更大（auth_scope 8.5pp, incomp 5.1pp）vs ling-layer（coref 1.4pp），因为spec-layer的violation boundary本身更模糊——judge 对\\\"是否超越authorization\\\"的判断inherently更主观。Paper中在Method §4.4专设\\\"Judge Calibration\\\" 小节，诚实披露bias并报告correction procedure。Reviewer反应预测：R1/R2接受correction approach， R3认为这undermines confidence并建议扩大human annotation——rebuttal承诺camera-ready扩到200 episodes。\\n\\n\\n这是median档的defining experiment。Judge-human F1=0.78, κ=0.72——落在预测范围[0.72, 0.84] 和[0.65, 0.79]内。关键发现：(1) LLM judge在severe violations（tier 3）上表现良好（F1=0.85）， 但在moderate/minor boundary上有系统性over-classification（7.2pp bias）——judge倾向于将 borderline inappropriate episodes标记为violations。(2) Auth_scope是bias最大的类型（8.5pp）， 因为judge难以区分\\\"exceeded explicit authorization boundary\\\"（真violation）和\\\"acted within reasonable interpretation of vague permission\\\"（不应算violation）。这直接影响C4：auth_scope 的raw 52pp range在correction后缩至~38pp。(3) Human inter-annotator κ=0.81（strong）， 高于judge-human κ=0.72——说明human ground truth可靠但LLM judge有gap。(4) Correction strategy：用confusion matrix计算per-type correction factor，apply to all violation rates。 Overall rate从0.41降至0.365，delta从34pp降至~28.5pp。(5) 这个结果足以让paper通过review （corrected findings仍显著），但至少一位reviewer会认为correction增加了uncertainty，可能 要求camera-ready扩大human annotation sample。\\n\"\n  },\n  {\n    \"name\": \"perturbation_control\",\n    \"description\": \"Non-ambiguity perturbation control arm。30 clause pairs × 2 conditions × 2 models = 120 episodes（基础）+ 可能追加60。\\n\",\n    \"results\": {\n      \"total_episodes\": 180,\n      \"base_episodes\": 120,\n      \"additional_episodes\": 60,\n      \"delta_perturb_pp\": 3.8,\n      \"delta_perturb_ci\": [\n        -1.2,\n        8.8\n      ],\n      \"ci_width\": 10.0,\n      \"delta_ambiguity_pp\": 33.5,\n      \"delta_net_pp\": 29.7,\n      \"ratio\": 0.113,\n      \"verdict\": \"PASS\",\n      \"synonym_delta_pp\": 2.1,\n      \"reorder_delta_pp\": 5.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Perturbation Control Verdict\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"threshold\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"Δ_perturb\",\n            \"3.8pp\",\n            \"<5pp\",\n            \"PASS\"\n          ],\n          [\n            \"CI_upper\",\n            \"8.8pp\",\n            \"<10pp\",\n            \"PASS\"\n          ],\n          [\n            \"ratio\",\n            0.113,\n            \"<0.15\",\n            \"PASS\"\n          ],\n          [\n            \"Δ_net (raw)\",\n            \"29.7pp\",\n            \">20pp\",\n            \"PASS\"\n          ],\n          [\n            \"Δ_net (corrected)\",\n            \"24.7pp\",\n            \">20pp\",\n            \"PASS\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Perturbation Type Breakdown\",\n        \"columns\": [\n          \"perturbation_type\",\n          \"n_pairs\",\n          \"delta_pp\",\n          \"ci_95\"\n        ],\n        \"rows\": [\n          [\n            \"synonym_substitution\",\n            15,\n            2.1,\n            \"[-4.2, 8.4]\"\n          ],\n          [\n            \"clause_reordering\",\n            15,\n            5.5,\n            \"[-1.8, 12.8]\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Perturbation control PASS是median档下最unambiguous的positive result。即使在judge correction 后，corrected net effect（24.7pp）仍远超CONDITIONAL threshold（20pp）。这让C1的causal claim 在所有tier下都成立——perturbation control的robustness不受judge bias影响（因为同样的judge bias同时inflate perturb和ambiguity conditions的violation rates，ratio不变）。Paper中 这是Method section的highlight：\\\"strongest causal evidence in the agent safety literature\\\"。\\n\\n\\nMedian档下perturbation control PASS（verdict=PASS, ratio=0.113 < 0.15）。Base 120 episodes的CI过宽（~15pp），追加60 episodes压窄至10pp。Final Δ_perturb=3.8pp, CI包含0 → 非模糊perturbations不造成meaningful effect。Synonym substitution（2.1pp）比clause reordering（5.5pp）effect更小——reordering偶尔改变agent对条件优先级的interpretation，但 仍远低于ambiguity effect。Net effect 29.7pp（raw; corrected ~24.7pp）仍massive。这个 结果是论文因果推断的backbone——\\\"perturbation control confirms ambiguity-specific causation， not general prompt brittleness\\\"。在median档下即使judge correction压缩了absolute numbers， net effect的qualitative conclusion不变。\\n\"\n  },\n  {\n    \"name\": \"classifier_poc\",\n    \"description\": \"DeBERTa-v3-large binary ambiguity detector PoC。Fine-tune on annotated clause pairs。\\n\",\n    \"results\": {\n      \"total_clauses\": 500,\n      \"train_test_split\": \"400/100 (5-fold CV)\",\n      \"binary_f1\": 0.79,\n      \"binary_precision\": 0.82,\n      \"binary_recall\": 0.76,\n      \"binary_fpr\": 0.048,\n      \"macro_f1_6type\": 0.58,\n      \"best_type_f1\": {\n        \"conditional_precedence\": 0.91\n      },\n      \"worst_type_f1\": {\n        \"incompleteness\": 0.31\n      },\n      \"training_time_hours\": 6,\n      \"gpu_used\": \"1x A100\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Classifier Performance Summary\",\n        \"columns\": [\n          \"task\",\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"binary\",\n            \"F1\",\n            0.79\n          ],\n          [\n            \"binary\",\n            \"precision\",\n            0.82\n          ],\n          [\n            \"binary\",\n            \"recall\",\n            0.76\n          ],\n          [\n            \"binary\",\n            \"FPR\",\n            0.048\n          ],\n          [\n            \"6-type\",\n            \"macro_F1\",\n            0.58\n          ]\n        ]\n      },\n      {\n        \"name\": \"Per-type Classification F1\",\n        \"columns\": [\n          \"type\",\n          \"f1\",\n          \"n_train\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            \"conditional_precedence\",\n            0.91,\n            80,\n            \"structural signal strong\"\n          ],\n          [\n            \"scopal\",\n            0.73,\n            80,\n            \"scope markers detectable\"\n          ],\n          [\n            \"coreferential\",\n            0.67,\n            80,\n            \"pronoun/RC patterns\"\n          ],\n          [\n            \"authorization_scope\",\n            0.55,\n            80,\n            \"boundary language moderate signal\"\n          ],\n          [\n            \"lexical\",\n            0.37,\n            80,\n            \"word-level, few surface cues\"\n          ],\n          [\n            \"incompleteness\",\n            0.31,\n            80,\n            \"absence has no positive signal\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Classifier是appendix material。Binary detection viable（F1=0.79），6-type classification 需要larger training data或更sophisticated approach（e.g., LLM-based few-shot）。在median 档下这个result不影响main paper score——reviewer不会因为weak classifier reject，也不会因为 它accept。它的价值在于demonstrating practical downstream applicability of the taxonomy。\\n\\nMedian档下classifier PoC results mixed。Binary detection F1=0.79（adequate for PoC）， 但6-type classification macro F1=0.58（weak）。Type-level performance高度不均：CP最好 （F1=0.91，因为explicit conflict structure易识别），incompleteness最差（F1=0.31，因为 \\\"missing information\\\"没有positive linguistic signal——absence很难用surface features检测）。 这个结果pattern与Chantree et al. (2006)的nocuous ambiguity detection一致——structural ambiguity比semantic ambiguity更容易自动检测。在median档下classifier不作为独立contribution （不在abstract或contribution list中），而是appendix-level \\\"preliminary PoC demonstrating feasibility of automated detection\\\"。Binary F1=0.79足以说明practical applicability， 但6-type F1=0.58太弱不值得highlight。Reviewer可能建议这是separate future work——rebuttal 同意并将其scope down to appendix。\\n\"\n  }\n]",
      "numLines": 1116,
      "startLine": 1,
      "totalLines": 1116
    }
  },
  "sourceToolAssistantUUID": "efd83765-f42c-45f9-b1b6-63f19e0de5d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T12:54:51.846Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Cw8R1rtewjRiCYJQX8VR1y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c999833-152a-4966-9a45-e09743c84d80",
  "isSidechain": false,
  "requestId": "req_011CbFkPBsmQUBtJ5sfnGAT4",
  "type": "assistant",
  "uuid": "3e36f840-94c4-41d0-a907-7d834426fc72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WbPRcezUwzKdj7yNJtbWS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12262,
      "cache_read_input_tokens": 11447,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12262,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12262,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12262
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

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122435 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigu…",
  "leafUuid": "3e36f840-94c4-41d0-a907-7d834426fc72",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier dream paper on policy ambiguity",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06"
}
```

---

### Tool result

_source line 14 · 2026-05-21T12:54:52.451Z_

<details><summary>↩ Tool result · `toolu_01Cw8R1rtewjRiCYJQX8VR1y`</summary>

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
141	**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).
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
  "parentUuid": "3e36f840-94c4-41d0-a907-7d834426fc72",
  "isSidechain": false,
  "promptId": "b06fed81-2945-4fd1-a156-f5dff4b5611e",
  "type": "user",
  "uuid": "d59fa2f9-aebc-4d36-bfd8-bf8e23db312a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/median/paper_framing.md",
      "content": "# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-20 19:30 UTC | 状态: 5-model analysis complete, C3/C4 framing revised\n> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)\n> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)\n> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)\n\n## Core Insight\n\nPolicy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.\n\n## Title (Working)\n\n\"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\"\n\nAlternative: \"Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents\"\n\nNote: Pivoted from \"Uniformly Nocuous\" → \"Specification-Layer Dominant\" (2-model) → \"Differential Nocuity with Model Interaction\" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed, 5 models)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.\n- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].\n- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.\n- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.\n- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.\n- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.\n\n### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)\n**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.\n- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)\n  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)\n  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp\n  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)\n- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.\n- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).\n- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).\n- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.\n\n### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)\n**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.\n- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].\n- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: \"suggestive\" or \"a moderate tendency,\" NOT \"confirmed.\" Disclose within-judge non-significance in Limitations.\n- **Per-model layer gaps** (THE KEY FINDING — feeds C4):\n  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong\n  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong\n  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak\n  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible\n  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!\n- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.\n- **Framing decision**: C3 is NOT \"spec-layer nearly twice as dangerous\" (that was 2-model artifact). The correct framing is: \"Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4).\"\n- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).\n- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).\n- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.\n- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.\n\n### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)\n**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.\n- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.\n  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%\n  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.\n- **Model × Type interaction matrix** (ambiguous condition, violation rates):\n  ```\n  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek\n  authorization_scope     64%     46%      12%     26%     60%\n  conditional_precedence  34%     36%      36%     40%     38%\n  incompleteness          46%     58%      48%     62%     54%\n  lexical                 42%     34%      32%     52%     54%\n  coreferential           18%     32%      22%     42%     44%\n  scopal                  42%     38%      32%     37%     48%\n  ```\n- **Key interaction patterns**:\n  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.\n  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.\n  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.\n  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.\n- **Per-model type χ²** (which models show type-specific vulnerability patterns):\n  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)\n  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)\n  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)\n  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline\n  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)\n- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.\n- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a \"safety training blind spot\" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.\n- **Framing**: C4 from \"models agree\" → \"Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality.\"\n- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.\n- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.\n\n### C5: Error Analysis (CONFIRMED — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).\n- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:\n  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)\n  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.\n  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = \"misparse\"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = \"active guessing\" → explains higher violation rates\n  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more \"confident,\" act without hesitation)\n  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)\n  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity\n  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse\n- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).\n  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to \"dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)\" instead of specific percentages; (5) Fine-grained 6-type as appendix with \"automated coding\" caveat.\n  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from \"moderate automated\" to validated.\n- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. \"Ambiguity Blindness\" upgraded from named concept to empirical finding with <5-11% awareness hard data.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?\n5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.\n6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a \"safety training blind spot.\"\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R\n- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation\n- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.\n- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).\n- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Type effect could be artifact of taxonomy granularity\"\n**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.\n**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"RC attachment in coreferential overlaps with scopal / structural ambiguity\"\n**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.\n\n### RC9: \"authorization_scope is just a subtype of incompleteness\"\n**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., \"authorized personnel\" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.\n\n### RC10: \"API sampling noise undermines reliability\"\n**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.\n\n### RC11: \"Prompt sensitivity confound\" [Dream A9 — best tier \"strongest point\"]\n**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.\n**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.\n\n## Concept Naming (distill insight: 命名即贡献)\n\nCore phenomenon: **\"Differential Nocuity\"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.\n\nSecondary phenomenon: **\"Ambiguity Blindness\"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.\n\nTertiary phenomenon: **\"Disambiguation Channel Framework\"** [renamed from \"Hypothesis\" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).\n\nQuaternary phenomenon: **\"Systematic Nocuity\"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears \"correct\" until compared against ground truth. Proposed as B&K extension in Discussion.\n\n## Opening Hook Strategy (distill insight: 具体案例, 不要 \"Recently...\")\n\nOpen with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says \"items may be returned within 30 days\" (scopal: \"items\" scopes over all categories including custom). The unambiguous version specifies \"standard items only\" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.\n\n## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)\n\n\"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones.\"\n\n## Benchmark Comparison Table (distill insight: 必有 feature matrix)\n\n| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |\n|---------|--------|---------------|------------|----------|----------|\n| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |\n| Causal design | — | — | — | — | **matched pairs** |\n| Safety violation metric | — | binary | — | procedural | **3-tier severity** |\n| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |\n| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |\n| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |\n\n## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]\n\n1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.\n2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.\n3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity (\"Ambiguity Blindness\"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.\n\nNOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. \"Disambiguation channel\" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.\n\n## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]\n\nCurrent plan has thin references. Must add (≥25 total in final paper):\n- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.\n- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.\n- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)\n- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.\n- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) \"Ambiguity\" encyclopedia entry.\n- **Surprisal/expectation-based**: Levy (2008); Hale (2001)\n- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)\n- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)\n- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent\n- **Formal semantics of vagueness**: Lassiter & Goodman (2017)\n- **Garden-path**: Frazier & Rayner (1982)\n- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)\n- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份\n\n## Code/Data Release Plan [Dream A6 — three-tier consistent]\n\nMust commit to releasing:\n1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels\n2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)\n3. Statistical analysis code (all tests, bootstrap CI computation)\n4. Agent trace samples (anonymized) for reproducibility of C5\n\n## Figure Plan [Dream A12]\n\nMinimum figures for paper (zero-figure paper flagged in dream):\n1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)\n2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)\n3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)\n4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)\n5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)\n6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)\n7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)\n\n## Berry & Kamsties Operationalization Note [Dream best Q5]\n\nBerry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.\n\n## Contingency Framing [RESOLVED — Scenario C occurred]\n\n> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。\n> Framing 已 pivot 到 \"Differential Nocuity\" + \"Layer Hierarchy\" (D020)。本节仅保留历史记录。\n\n## Claude Baseline — RESOLVED [2026-05-20]\n\n✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).\n",
      "numLines": 247,
      "startLine": 1,
      "totalLines": 247
    }
  },
  "sourceToolAssistantUUID": "3e36f840-94c4-41d0-a907-7d834426fc72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122435 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigu…",
  "leafUuid": "d59fa2f9-aebc-4d36-bfd8-bf8e23db312a",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier dream paper on policy ambiguity",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06"
}
```

---

### Assistant

_source line 17 · 2026-05-21T12:56:00.086Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also load the paper-writing-norms skill as instructed in the CLAUDE.md.

Actually, let me just proceed with writing the paper. I have a clear picture of:

1. The experiment data (10 experiments)
2. The paper framing (detailed guidance)
3. The narrative guidance for median tier

Key points for median tier:
- 3-claim structure: C1 (corrected binary effect ≥25pp), C2 (type hierarchy), C4 (model×type interaction)
- C3 demoted to appendix-level


- C5 becomes supporting analysis with qualitative descriptions
- Judge calibration correction is central
- Title: "How Ambiguity Type and Model Architecture Shape Safety Violations"
- Expected ARR score: 3.0-3.5

Now I'm mapping out how to integrate all 10 experiments across the paper structure: the clause generation and pilot validation go into methods, while the API and open-source studies provide the core results for my three main claims, with the analysis study supporting everything.

I'm organizing the full paper with an abstract, introduction, related work, the ambiguity taxonomy, then a comprehensive methods section covering clause generation, pilot validation, experimental setup, judge calibration, perturbation control, reliability testing, and ecological validity checks. The results section will focus on the binary effect, type hierarchy, and model-by-type interactions, followed by an analysis section examining error patterns and the classifier proof-of-concept in the appendix.

Writing the LaTeX paper in EMNLP format... Looking at the statistical results for the remaining conditions and how they fit into the paper structure. C5 provides supporting evidence with reasonable inter-rater agreement, while C3's fragility issues relegate it to the appendix. Now I'm mapping out the paper sections systematically—starting with the abstract that highlights the corrected binary effect and the interaction between model type and ambiguity category, then building through introduction, related work, and the taxonomy before detailing the experimental methodology across clause generation, validation, and the full studies with both API and open-source models.

The results section will focus on the three main claims with their corresponding analyses, followed by qualitative findings on error patterns and blindspots. I'm planning to keep the main text under eight pages while using the appendix for supplementary findings and the classifier proof-of-concept. Now I'm ready to start writing the LaTeX document using a standard article class format. I'm pulling together all the key experimental results to weave into the paper—the full study data across API models like GPT-5.4 and Claude, the open-source results from Qwen and DeepSeek, and the inter-rater agreement metrics that validate the findings. Now I'm looking at the interaction effects and reliability metrics—the judge fragility shows borderline significance, while the C4 interaction is quite strong with a substantial range in the auth_scope condition. The logistic regression coefficients suggest both condition and token delta are meaningful predictors. Looking at the error analysis, I've traced 290 cases and found that while surface adoption is high at 87%, actual awareness is quite low at 6.2%, with human agreement around 72%. The reliability test shows strong overall consistency with an ICC of 0.905, though scopal and lexical types are more reliable than authorial constructions.

Continuing through the validation, most distributional metrics don't show significant differences, but parse depth does emerge as significant. The judge calibration reveals decent agreement with humans at F1=0.78, though there's a systematic bias toward over-classification by about 7 percentage points, with performance varying notably across severity tiers. The perturbation analysis suggests the effect is relatively small with a confidence interval that crosses zero.

Now I'm moving into writing the paper itself. I need to structure it with a clear abstract containing key numbers, a logical introduction, solid methodology section, results presented in tables, brief analysis, and concise discussion and conclusion. I'm planning tables for the clause generation summary and other key results. I'm ready to start writing the paper now, using the median-tier framing with the three-claim structure and corrected numbers throughout. I should keep C3 in the appendix and use C5 as supporting analysis with qualitative descriptions. Let me also verify that the LaTeX packages I'm planning to use are standard and widely available—article class, geometry, booktabs, graphicx, amsmath, natbib, hyperref, xcolor, multirow, and array should all be fine.

Writing the paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d59fa2f9-aebc-4d36-bfd8-bf8e23db312a",
  "isSidechain": false,
  "requestId": "req_011CbFkPWTiD1RMctNXmcvXB",
  "type": "assistant",
  "uuid": "7d2b3286-5c5f-4f4f-a251-8f0917ae368c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcNTQAVLnZdMNvYv1TYeLZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25157,
      "cache_read_input_tokens": 23709,
      "output_tokens": 3241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3241,
          "cache_read_input_tokens": 23709,
          "cache_creation_input_tokens": 25157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25157
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

_source line 18 · 2026-05-21T12:56:00.542Z_

Now let me check the output directory exists and load the paper writing norms skill.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d2b3286-5c5f-4f4f-a251-8f0917ae368c",
  "isSidechain": false,
  "requestId": "req_011CbFkPWTiD1RMctNXmcvXB",
  "type": "assistant",
  "uuid": "9ed0adf1-bc52-4c5e-966d-1d5fa63b5dc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcNTQAVLnZdMNvYv1TYeLZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25157,
      "cache_read_input_tokens": 23709,
      "output_tokens": 3241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3241,
          "cache_read_input_tokens": 23709,
          "cache_creation_input_tokens": 25157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25157
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

_source line 19 · 2026-05-21T12:56:03.661Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QfQBwKNjHjgNavB3erGxQC`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/median/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ed0adf1-bc52-4c5e-966d-1d5fa63b5dc6",
  "isSidechain": false,
  "requestId": "req_011CbFkPWTiD1RMctNXmcvXB",
  "type": "assistant",
  "uuid": "fbd209b6-25ab-47c6-bb21-66cf564d7d64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcNTQAVLnZdMNvYv1TYeLZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25157,
      "cache_read_input_tokens": 23709,
      "output_tokens": 3241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3241,
          "cache_read_input_tokens": 23709,
          "cache_creation_input_tokens": 25157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25157
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

_source line 20 · 2026-05-21T12:56:03.984Z_

<details><summary>↩ Tool result · `toolu_01P68TLGVRYHjxLmgRSdxv89`</summary>

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
  "parentUuid": "bad1052a-9867-4cde-a063-9cc35b15d62c",
  "isSidechain": false,
  "promptId": "b06fed81-2945-4fd1-a156-f5dff4b5611e",
  "type": "user",
  "uuid": "e40fa722-14be-4076-8eff-6d8760cf520e",
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
  "sourceToolAssistantUUID": "bad1052a-9867-4cde-a063-9cc35b15d62c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 21 · 2026-05-21T12:56:03.826Z_

<details><summary>↩ Tool result · `toolu_01QfQBwKNjHjgNavB3erGxQC`</summary>

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
  "parentUuid": "fbd209b6-25ab-47c6-bb21-66cf564d7d64",
  "isSidechain": false,
  "promptId": "b06fed81-2945-4fd1-a156-f5dff4b5611e",
  "type": "user",
  "uuid": "594c2c33-763c-4aed-998e-b581499c1798",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fbd209b6-25ab-47c6-bb21-66cf564d7d64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T12:56:03.978Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P68TLGVRYHjxLmgRSdxv89`</summary>

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
  "parentUuid": "594c2c33-763c-4aed-998e-b581499c1798",
  "isSidechain": false,
  "requestId": "req_011CbFkPWTiD1RMctNXmcvXB",
  "type": "assistant",
  "uuid": "bad1052a-9867-4cde-a063-9cc35b15d62c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcNTQAVLnZdMNvYv1TYeLZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25157,
      "cache_read_input_tokens": 23709,
      "output_tokens": 3241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3241,
          "cache_read_input_tokens": 23709,
          "cache_creation_input_tokens": 25157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25157
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122435 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigu…",
  "leafUuid": "e40fa722-14be-4076-8eff-6d8760cf520e",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier dream paper on policy ambiguity",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06"
}
```

---

### Assistant

_source line 25 · 2026-05-21T13:06:10.200Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have all the information I need. Let me write the complete paper. I'll follow the paper-writing-norms and the median tier narrative guidance.

Key decisions:
1. Use basic article class (no ACL template available)
2. Two-column format with geometry
3. 3-claim structure: C1 (corrected), C2 (hierarchy), C4 (interaction)
4. C3 in appendix, C5 as supporting analysis
5. All numbers from experiment_data.json
6. No em-dashes, no AI style markers


7. Booktabs for tables

I need to be careful with the EMNLP format and the 8-page limit for main text. Since I'm using article class, I'll aim for roughly that length. Let me write the full LaTeX now, covering all 10 experiments.

Writing the paper structure... I'm realizing I have too many tables and need to consolidate them down to a more manageable set. I'll keep the core findings in the main paper—per-model violation rates, type hierarchies, interaction matrices, judge calibration, perturbation control, and failure modes—while moving the reliability metrics and additional validation data to the appendix. Realism validation
- Table A3: C3 layer effect
- Table A4: Classifier PoC

Actually, let me be more selective. For a reviewable paper at "够审" quality, I should include the most important tables in the main text and put supporting ones in the appendix.

Main text tables:
- Table 1: Per-model violation rates (C1 main result)
- Table 2: C1 raw vs corrected
- Table 3: C2 type hierarchy
- Table 4: C4 model × type interaction
- Table 5: Perturbation control verdict
- Table 6: Failure mode summary

Appendix tables:
- Table A1: Judge calibration details
- Table A2: ICC reliability
- Table A3: Realism validation
- Table A4: C3 layer effect
- Table A5: Classifier PoC
- Table A6: Clause

Now I'm reconsidering which tables are truly essential for supporting each claim. C1 needs the per-model results and the raw versus corrected comparison, C2 requires the corrected rates broken down by type, and C4 demands the full model-by-type matrix. For the supporting evidence, I should definitely include judge calibration since it's crucial to the median tier narrative, plus perturbation control for causal backing and the failure modes and ambiguity blindness analyses. That gives me seven tables total, which is pushing the limit but defensible. I've settled on a six-table main structure with five appendix tables to keep the paper tight while covering all ten experiments. Now I'm ready to start drafting the actual paper—I'll use the title "How Ambiguity Type and Model Architecture Shape Safety Violations" and write a complete LaTeX document, being careful to get all the numbers right.

For the structure, I'm planning an abstract around 200 words covering the problem, method with the 2,997 episodes across five models and six types, and the key findings like the 28.5 percentage point binary effect and the three-tier type hierarchy. The introduction will open with a concrete failure case and highlight the gap that DRIP-R classifies ambiguity but doesn't measure safety impact. I'll include related work on ambiguity in NLP and agent safety evaluation, then move into the taxonomy section.

The methods section will cover clause generation, experimental setup, judge calibration, and perturbation control across four subsections. Results will focus on the binary effect, type hierarchy, and the model-by-type interaction showing that 38 percentage point range in auth_scope. I'm including a qualitative analysis section on failure modes and ambiguity blindness, then wrapping up with discussion of differential and systematic nocuity before the conclusion.

I need to verify the page budget for EMNLP 2026—it's an 8-page limit for main text, so I'll set up the LaTeX with a two-column format at 10pt to fit everything. Let me start writing the full document now.

Writing LaTeX document... Writing the LaTeX paper... Generating markdown table...

I'm noticing a discrepancy in the episode counts—the individual experiments add up to 2,981, but the full analysis reports 2,997, so there might be some overlap or additional data I'm not accounting for. I'll stick with the 2,981 figure from the direct sum of the API and open-source studies.

Now looking at the ambiguity rates across models from the analysis: GPT-5.4 shows 40.5% ambiguous with 5.5% unambiguous, GPT-4.1 is at 39.7% and 6.0%, Claude sits lower at 29.3% and 4.3%, while Qwen3 reaches 42.1% and 6.3%, and DeepSeek is highest at 48.7% with 6.7% unambiguous.

Computing the unweighted average across all five models gives me 40.06% for ambiguity and 5.76% for unambiguous violations. The API-only data shows 0.383 overall, but I need to account for the per-model rates in the ambiguous condition—each model has 300 ambiguous episodes, so I'm calculating the weighted contribution from each model to get the true overall rate.

When I sum up the violations across all models (121 + 119.1 + 87.9 + 126.3 + 146.1 = 600.9 out of 1500 total), I get approximately 40.1% for the ambiguous condition and 5.76% for unambiguous, which gives a delta of about 34.3 percentage points—close to the 33.5pp reported in the analysis, so the numbers are checking out.

Now I'm ready to draft the paper with the key figures: a corrected binary effect of 28.5pp (33.5pp raw), systematic judge bias of 5-8pp, and the type hierarchy showing incompleteness as the most problematic category at 49.5%. I'm starting with an abstract that frames the core finding about how natural language ambiguity in LLM policy specifications significantly impacts agent behavior across different violation types. I'm seeing the rest of the results now—the model-by-type interaction shows authorization scope vulnerability varies dramatically across models, ranging from 14% for Claude up to 56% for GPT-5.4, whereas incompleteness stays consistently dangerous across all of them. This suggests safety training handles different ambiguity types unevenly, so I need to structure the paper around three main claims with proper experimental validation, careful attention to the data from my experiment file, and clear separation between core findings and supporting analyses. I'm compiling the bibliography with about 20-25 key references covering ambiguity detection, agent evaluation, NLP processing, and related work to establish credibility. Now I need to start drafting the actual paper sections.

For the opening hook, I'll use a concrete failure case from τ²-bench where a customer return request exposes policy ambiguity—the word "items" in a 30-day return policy creates a $200 difference in outcomes depending on whether it applies to all products or just standard catalog items. This sets up the stakes nicely.

I'm organizing the LaTeX document to compile cleanly with pdflatex, structuring it section by section. The methods section will detail the experimental setup, tracking which data comes from which experiment.

Writing LaTeX document... Writing the LaTeX document... I'm mapping out the key tables for the results section—violation rates by model, the binary effect comparison, type hierarchy with tiers, and the interaction matrix—which should fit well across six tables in a two-column format. Now I need to settle on the title; the working versions emphasize how ambiguity type and model architecture interact to shape safety violations, and I'm leaning toward the phrasing that highlights this interaction effect most clearly.

For the introduction, I'm structuring it around a concrete failure example, then moving through the background on policy ambiguity and prior classification work, before positioning this paper's causal approach with the matched-pair design across five models and six ambiguity types. The key findings about the corrected effect size, type hierarchy, and model interactions will anchor the contributions, and I want to avoid the typical LLM capability framing and keep the prose direct without relying on em-dashes or stacked transitions.

Now I'm drafting the opening paragraphs carefully—starting with a customer returns scenario where scope ambiguity over "items" leads to an unauthorized refund, then moving into the background on how agents operate under natural language policies and how Berry and Kamsties distinguish between nocuous and innocuous ambiguity.

The key insight is that humans rely on shared organizational context to resolve most ambiguity, but LLM agents lack that grounding. Then I'm positioning the gap: existing work catalogs ambiguity types and identifies policy violations, but no one has yet established causal links between specific ambiguity types and safety violations across different models. So our contribution is the first matched-pair study that isolates ambiguity as a causal factor, using 300 clause pairs across six ambiguity types in a two-layer taxonomy.

We test five diverse models on an agentic benchmark, generating nearly 3,000 episodes with proper controls and human evaluation to ensure we're measuring causality, not just correlation. The results show ambiguous policies increase safety violations by 28.5 percentage points with strong statistical significance, and different ambiguity types create a severity hierarchy—incompleteness is most dangerous while coreferential ambiguity is least risky. There's also a meaningful interaction effect where authorization scope vulnerabilities vary dramatically across models, suggesting some architectures are more susceptible to certain ambiguity types.

Our main contributions are establishing the causal link between policy ambiguity and safety violations across multiple models, developing a framework that categorizes ambiguity types by severity and shows how their impact varies by model, and documenting a phenomenon where agents show surprisingly low awareness of ambiguity itself—less than 6.2% recognition rate—which we're calling Ambiguity Blindness.

Now I'm moving on to write out the full LaTeX document and compile the references, pulling together sources on requirements engineering ambiguity, NLP taxonomies, and the specific benchmarks and detection methods we've referenced throughout. Now I'm mapping out the page budget across sections—introduction and results will take up the most space, while related work and analysis can be tighter. I'll start writing the full LaTeX document with these constraints in mind.

Writing LaTeX document... I'm settling on basic numbered citations with \cite{} since that's the most reliable approach across LaTeX installations. Now I'll compose the complete document, being careful to escape special characters and ensure proper table formatting for pdflatex compilation. I have enough tables distributed throughout to maintain visual rhythm across the pages without needing additional figures. I'm settling on the table dimensions—Table 3 with its seven columns needs full width formatting, while the others fit in single-column. Now I'm ready to write the full paper. Before I start, let me map out exactly which numbers go where: the method section should cover the clause generation details (300 pairs across 6 types, token deltas, pass rates, revision counts) and briefly mention the pilot study.

For the evaluation setup, I'm documenting the five models tested against 2,981 valid episodes from both API and open-source sources using τ²-bench. The judge calibration metrics show solid agreement (F1=0.78, κ=0.72) with human IAA at κ=0.81, though there's a systematic bias of +7.2 percentage points that I'll correct for. Reliability checks give ICC=0.905 with a tight confidence interval, and the realism assessment shows mostly non-significant KS tests except for parse depth. For the main results, the raw effect size is substantial at 33.5 percentage points with OR=14.2, but after applying the bias correction it settles to 28.5 percentage points with OR=10.8.

Breaking down by model, I'm seeing performance ranging from Claude at 25.0pp up to DeepSeek at 42.0pp, with the perturbation control validating the robustness of these estimates. The logistic regression confirms both the condition and token delta are significant predictors. For the second comparison, the omnibus test is highly significant with good statistical power, and the corrected rates show a clear ordering across the three categories.

Looking at the error distribution, there's a three-tier structure emerging—incompleteness errors are most common, followed by a middle tier of lexical, authorial, scopal, and CP errors, with coreference errors least frequent. The equivalence testing suggests only a few comparisons meet the stricter equivalence thresholds. The interaction effect is significant, with authorial-scope showing the largest range across models at 38pp corrected, while CP errors are remarkably consistent. The inter-rater agreement is fair but indicates models don't strongly align on which specific clauses trigger these errors. I've analyzed 290 traces so far, and authorial errors are emerging as a key failure mode to investigate further.

Now looking at the specific error patterns—authorial-scope errors predominantly manifest as unauthorized escalation, incompleteness as assumption-based actions, and scopal errors as scope misapplication. The awareness rate is quite low at 6.2%, though surface adoption is high at 87%, suggesting models often attempt to handle these cases without truly understanding them. Only 0.8% escalate to the user, which is concerning. The human anchor agreement is decent at 72%, and I'm noticing that 25% of ambiguous episodes show systematic nocuity—this is an important finding to highlight as an extension of the B&K framework. I should weave this into the discussion along with the disambiguation channel.

For the limitations section, I need to be transparent about the scope constraints: only two domains from the benchmark, the synthetic ambiguity injection with slightly elevated parse depth, the 7.2 percentage point systematic bias from LLM-as-judge that I've corrected for, the fragility of the C3 layer effect under within-judge analysis, and the relatively small human calibration sample. These are all required disclosures for EMNLP 2026.

Now I'm ready to draft the paper itself. I'll start with the opening hook—grounding the abstract problem in a concrete τ²-bench failure case, like a customer returning a customized item within the return window, to immediately show why this matters.

For related work, I'm organizing into three focused areas: how ambiguity shows up in NLP and requirements engineering, existing agent safety evaluation frameworks, and the quality of policy specifications themselves. Each subsection will be tight, around 3-5 sentences to position the work clearly.

I'm also checking my abstract word count against the ~200-word target to make sure I'm not overrunning before I commit to the full LaTeX output.

Now I'm laying out the core empirical findings: the matched-pair study across five agent architectures and six ambiguity types yielded nearly 3,000 episodes, and after accounting for a systematic bias in LLM-as-judge scoring, policy ambiguity drove violation rates up by 28.5 percentage points with a strong effect size. The perturbation control rules out general prompt brittleness as the culprit, and the severity hierarchy shows incompleteness as the most dangerous ambiguity type, with coreferential ambiguity posing the least risk.

The model-by-type interaction reveals substantial heterogeneity—authorization scope vulnerabilities swing wildly across architectures while incompleteness remains consistently hazardous regardless of model. This suggests safety training tackles different ambiguity types unevenly, pointing toward the need for both type-specific auditing and model-tailored risk profiles before deploying agents in high-stakes settings.

Now I'm thinking through the paper structure and references—I need to ground the τ²-bench environment in the methods section and compile a plausible reference list that supports the empirical claims. Continuing with more references on language model behavior, safety evaluation, and agent risk assessment. Finishing up the last few citations, then I'll move on to writing the LaTeX document itself. I want to make sure the paper actually compiles, so I'm going with a standard article class setup in two columns with basic packages and manual formatting to keep things straightforward.

Let me verify the EMNLP 2026 page constraints—8 pages for the main text with references, limitations, and ethics sections outside that limit. That gives me some breathing room to put extra content in appendices without eating into my main budget. For a two-column 10pt article with typical ACL-style margins, I'm looking at roughly 5000-5600 words across those 8 pages once I account for tables and spacing. Time to start composing the full LaTeX document. Setting up the LaTeX document...

Now I'm filling in each section with the actual content, starting with the abstract and working through the introduction, related work, and the core sections on the ambiguity taxonomy and experimental methodology. I'm reconsidering the table placement—I could move the perturbation control table to the Method section since it validates the experimental design, then keep the other four tables distributed across Results and Discussion. This keeps the layout manageable while maintaining the narrative flow. I'm consolidating the table structure to fit the space constraints—merging judge calibration numbers directly into section 4.3 and folding perturbation control results into section 5.1 as inline findings. That leaves me with four core tables covering violation rates by model, the type hierarchy, model-type interactions, and failure modes. Now I'm ready to start writing the paper sections, beginning with the abstract.

For the introduction, I'm opening with a concrete example of an LLM agent mishandling a customer return due to ambiguous policy language—a single unresolved word about scope leading to a costly safety violation. Then I'm moving into the broader context of how LLM agents operate under natural language policies in high-stakes domains, and I'll reference the requirements engineering literature on ambiguity types, distinguishing between nocuous and other forms.

Now I'm examining the research gap: while recent work like DRIP-R has catalogued ambiguity types in retail policies and shown that agents interpret them differently, it hasn't established whether these divergences actually cause safety failures. Other studies look at policy gaps and violations but don't isolate ambiguity as a causal mechanism with proper controls. I'm noting that linguistic ambiguity taxonomies exist in NLP but haven't been systematically applied to this agent safety problem.

For this paper, I'm laying out a causal study design with type-specific granularity across different model architectures. I'm constructing 300 matched clause pairs covering six ambiguity types organized hierarchically—three at the specification layer (authorization scope, conditional precedence, incompleteness) and three at the linguistic layer (lexical, coreferential, scopal). I'm testing five diverse models using an agentic evaluation environment to generate nearly 3,000 valid episodes, with a perturbation control arm to isolate ambiguity effects from other factors.

The key findings show that policy ambiguity causes a substantial 28.5 percentage point increase in safety violations across all models, with a perturbation control confirming this is specific to ambiguity rather than general prompt sensitivity. The ambiguity types themselves show a clear severity hierarchy, with incompleteness violations occurring most frequently, followed by a mid-tier cluster, and coreferential ambiguity causing the fewest violations.

Interestingly, there's a significant interaction between model type and ambiguity category—authorization scope vulnerabilities vary dramatically across models, but incompleteness remains consistently dangerous regardless of which model we test. The failure mode analysis reveals that agents almost never recognize ambiguity when it's present, instead defaulting to the first interpretation they encounter.

Now I'm moving into the related work section, looking at how linguistic ambiguity has been studied in computational linguistics and requirements engineering contexts. I'm reviewing how prior work on agent safety and policy quality relates to our approach. While existing evaluations like ToolEmu and R-Judge assess LLM agent risks broadly, and DRIP-R examines ambiguity in retail policies, our contribution is pinpointing policy ambiguity as a specific, linguistically grounded cause of unsafe behavior—something previous work hasn't directly connected to safety violations.

Now I'm laying out our taxonomy of policy ambiguity across two layers: the specification layer covers underspecified content like vague authorization boundaries, unclear rule priorities, and missing exception handling, while the linguistic layer addresses natural language phenomena like polysemy, pronoun attachment, and quantifier scope.

I'm distinguishing between ambiguity as discrete alternative readings versus vagueness as continuous indeterminacy, following Wasow et al.'s framework. The taxonomy maps to both DRIP-R's and Massey et al.'s existing classification schemes, though I should be careful about referencing appendices I haven't actually written yet—I'll just note that the cross-walk exists without committing to a specific section.

For the methodology, I'm constructing 300 matched clause pairs across six types, each with an ambiguous and disambiguated variant. Specification-layer ambiguities require substantially more text to resolve (averaging 35 tokens versus 15 for linguistic types), so I'm controlling for token delta as a covariate in the regression. The conditional precedence clauses incorporate a mix of explicit labeling approaches...

Now I'm detailing the quality control process—two independent annotators reviewed the clauses with a 92% pass rate, and the 8% requiring revision were concentrated in authorization scope and incompleteness categories where balancing sufficient ambiguity against information asymmetry proved most challenging. A preliminary validation with GPT-5.4 on the two new clause types showed authorization scope violations at 60% for ambiguous cases versus 10% for unambiguous, while coreferential clauses showed 20% and 0% respectively, both meeting feasibility thresholds. I'm also comparing these synthetic pairs against 87 naturally occurring ambiguities from DRIP-R using distributional tests to ensure ecological validity.

The statistical analysis shows our synthetic clauses align well with natural language on readability, sentence length, and vocabulary diversity, though parse depth runs slightly higher due to our controlled design—a limitation I'm noting. For the experimental setup, each clause pair gets embedded in a policy environment where an LLM agent processes customer requests that trigger the ambiguous language, and a separate judge evaluates whether the resulting action violates policy using a severity scale, with multiple judges assessing each case.

I'm testing five models across different tiers and architectures—including frontier proprietary models, mid-tier options, and open-source variants—each processing all clause pairs in both ambiguous and clear versions. After accounting for API failures, I have nearly 3,000 valid test episodes. Now I'm assessing test-retest reliability on a subset of clauses with multiple runs...

For the judge calibration, I'm comparing the LLM judge's violation classifications against human annotators on a stratified sample. The judge shows strong overall agreement with humans, but there's a clear pattern: it reliably catches severe violations but tends to over-classify violations at the moderate and minor severity levels, which introduces some systematic bias I need to account for.

The over-classification bias varies by violation type—authorization scope violations are particularly prone to misclassification while coreferential violations are more reliably judged, likely because authorization boundaries are inherently more ambiguous. I'm computing correction factors from the confusion matrix and applying them across all reported violation rates. After applying these corrections, the overall violation rate drops from 41.0% to 36.5%, and the binary effect size decreases from 33.5 percentage points to 28.5 percentage points, though the findings remain statistically significant.

Now I'm moving into the results section, starting with the binary effect analysis. Across all five models, ambiguous policy specifications produce a substantial and significant increase in safety violations, with a corrected effect size of 28.5 percentage points.

Looking at the per-model breakdown, the effect is consistent across all models but with notable variation in magnitude—Claude Sonnet shows the most robustness at 25.0 percentage points while DeepSeek-v3 is most vulnerable at 42.0 percentage points. I'm also running a logistic regression to isolate ambiguity as the primary driver of violations while controlling for other factors like token count differences between specifications.

Now I'm checking whether the effect is truly about ambiguity or just general sensitivity to prompt changes by testing non-ambiguity perturbations like synonym swaps and clause reordering. The perturbation effect is minimal at 3.8 percentage points with a confidence interval crossing zero, confirming that surface-level changes alone don't trigger violations—the ambiguity effect is what matters.

Looking at how different types of ambiguity vary in their impact on safety violations. A chi-squared test shows significant differences across types, and while the effect size is small, the test has strong statistical power confirming this is a real pattern. The data reveals a clear hierarchy with incompleteness causing the most violations around 50%, while lexical, authorization scope, and scopal ambiguities cluster in the mid-range around 37-40%.

Incompleteness emerges as particularly dangerous because agents can't work around missing information, whereas coreferential ambiguity is least problematic since agents can partially resolve it through tool interactions and show a cautious 8% refusal rate. Now examining how different models respond differently to these ambiguity types, with a significant interaction effect suggesting models have systematic differences in their vulnerability to specific types. The inter-model agreement is only moderate—models largely concur that ambiguity drives violations but disagree on which specific clauses are problematic. GPT-5.4 and Claude show the strongest differentiation across violation types, while DeepSeek-v3 exhibits uniformly high vulnerability regardless of type. Now I'm moving into qualitative analysis, examining roughly 290 violation traces to identify the specific failure patterns for each type, though the inter-coder reliability is moderate so I'm presenting the distributions with that caveat in mind.

Looking at the failure modes across types, specification-layer violations follow a "guess-and-act" pattern where agents either escalate permissions without recognizing boundaries or fill in missing policy details with unfounded assumptions. Linguistic-layer violations show "misparse-and-apply" failures where scope is resolved incorrectly. Lexical and coreferential ambiguity are outliers—lexical ambiguity triggers assumption-based action rather than misparsing, suggesting agents treat word sense ambiguity as a missing information problem, while coreferential ambiguity shows mixed resolution strategies with no dominant failure mode.

Now I'm looking at how aware agents actually are of ambiguity itself. The data shows agents detect ambiguity only about 6% of the time across all types and models, and in the vast majority of violations they just apply the surface reading without any sign of noticing alternatives. They almost never escalate to ask the user for clarification. This near-complete lack of awareness about ambiguity—what I'm calling "Ambiguity Blindness"—is striking compared to how they handle explicit rule conflicts, where they show higher awareness. Moving into the discussion, I'm examining how this fits with existing frameworks about which ambiguities actually matter, and the evidence confirms all six types are problematic for LLM agents.

The picture gets more complex though. The nocuity—how dangerous an ambiguity is—varies depending on both the type and which model we're looking at. I'm proposing a framework that captures this joint dependence. Authorization scope emerges as a particularly telling indicator of safety training quality, while incompleteness seems like a structural problem that alignment work alone can't solve without more information. There's also a troubling pattern where all five models converge on the same wrong interpretation in about a quarter of ambiguous cases. This is worse than when they disagree because when all models agree, it creates a false sense of confidence in the answer. I'm extending the existing framework to account for this "Systematic Nocuity" phenomenon. The three-tier hierarchy and the consistency patterns across linguistic versus specification layers suggest there's a structural explanation underlying all this.

The key insight is that some ambiguities can be resolved through external channels—tool responses, context from the conversation, or background knowledge—while others can't. Specification ambiguities are stuck because the missing or vague information only exists in the policy text itself. This explains why specification-layer ambiguities are more severe and why they show higher variability across different tests.

The core finding is that policy ambiguity universally increases safety violations by a significant margin, but the actual risk depends on both the ambiguity type and the model. Incompleteness is consistently dangerous across all models, while authorization scope vulnerabilities swing wildly depending on the architecture. Safe deployment means auditing policies to eliminate the highest-risk ambiguity types and doing model-specific risk assessments to account for these architectural differences. The study does have limitations though, starting with...

The evaluation only covers two domains within the benchmark, so I can't be sure these findings generalize elsewhere. The synthetic ambiguities we injected are slightly more complex to parse than naturally occurring ones, though most distributional metrics don't show meaningful differences. The LLM-as-judge approach has a systematic bias toward over-classification that we corrected for, but that correction introduces its own uncertainty, and the human calibration sample is relatively small. The aggregate effect comparing specification versus linguistic ambiguity is also fragile—it holds at one significance level but weakens under subgroup analysis, so it's more suggestive than definitive. The failure mode coding relies heavily on automated classification with only moderate human agreement, which...

Writing the LaTeX document... Now I'm verifying all the statistical results across both the corrected and raw analyses, checking the per-model breakdowns, perturbation effects, and the chi-square test for C2 along with the corrected error rates by clause type.

For the equivalence testing, I'm seeing that only 8 out of 15 comparisons meet the ±15pp threshold while 4 out of 15 meet the stricter ±10pp threshold.

Looking at C4, there's a significant interaction effect, and I'm reconciling the authentication scope range—the corrected matrix shows a 42pp spread from Claude at 14% to GPT-5.4 at 56%, though there seems to be a discrepancy with what the analysis table is reporting. I'm noticing the narrative guidance mentions the corrected range should fall between 35-45pp, and both the table value of 42pp and the scalar value of 38pp fit within that band. Since the table is explicitly labeled as the corrected data with individual values shown, I'll use 42pp as my primary figure, though I should note the analysis results show 38pp—likely from a different correction methodology. I'm settling on using the scalar value of 38pp for the corrected range in the text since it's more conservative, while displaying the individual corrected percentages from the C4 table—the small discrepancy between 38pp and the table's 42pp range likely stems from rounding or slight variations in how the correction was applied to individual values. The table data gives me 42pp as the range, which falls within the expected 35-45pp guidance, so I'll stick with that figure consistently across the abstract and text rather than the 38pp scalar value. I'm settling on 42pp from the table since it aligns with the expected 35-45pp range from the guidance, and I'll update my introduction draft to reflect this consistent figure across all sections. I'm seeing the inconsistency now—the corrected table shows a 42pp range, but the scalar mentions 38pp, which might be from a different correction method or an error in the source data. Since the table is explicitly labeled as corrected with specific per-cell values, I'll go with the 42pp range for consistency. For the overall uncorrected delta, I'll pull the 33.5pp figure from the full study analysis.

Now I need to work with the per-model deltas I have—GPT-5.4 at 35.0pp, GPT-4.1 at 33.7pp, Claude at 25.0pp, Qwen3 at 35.8pp, and DeepSeek at 42.0pp—which are all raw values. Since the corrected per-model deltas aren't explicitly provided, I'll report these raw figures in the table and note that the results remain significant after applying the overall correction of about 5pp. Writing the LaTeX document now, starting with the table structure. I'm planning four tables: one for per-model violation rates with sample sizes and p-values, another showing the type hierarchy with corrected rates and confidence intervals, a third displaying the model-by-type interaction matrix with ranges, and finally a summary of failure modes with their dominant characteristics and awareness percentages. Writing the LaTeX document now...

I'll use smaller font sizes for the tables to fit everything within the page limit, and leverage paragraph-level headings instead of subsections where I can to conserve space. Let me structure this with Introduction, Related Work, and the remaining sections, then handle the appendix tables with automatic numbering. I'm settling on the formatting approach now—using emphasized text for defined terms, small caps for proper names like τ²-bench, and consistent styling for statistical notation. I'll structure the document with booktabs for all tables and keep them compact with smaller font sizes where needed. Let me write out the complete LaTeX document from start to finish, making sure to align with the narrative guidance about judge calibration revealing systematic bias in LLM judges. 现在我需要完成论文的LaTeX文档。标题改为"How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents"，这样更具体。由于这是一篇模拟论文而非真实投稿，我可以在格式上稍微灵活一些，重点是确保文档能编译、包含所有数据、看起来像一份可审阅的草稿。现在开始组织参考文献和完整的文档结构。

Writing LaTeX document... I'm continuing through the bibliography, adding more references on requirements defect detection, language model risks, and related work in NLP and software engineering. Continuing through the bibliography with more foundational work on ambiguity and language comprehension, then moving into recent research on automatic identification of linguistic issues.

Now I'm compiling the full LaTeX document with all the citations integrated throughout, making sure the paper reads naturally and doesn't have obvious markers of AI authorship. I'm working through the contribution structure now. The narrative confirms a 3-claim paper with C1, C2, and C4 as main contributions, while C3 and C5 serve as supporting analysis. So my three contributions should be causal quantification, the differential Nocuity framework combining hierarchy and interaction effects, and failure mode analysis—though that last one sits in a supporting role rather than as a primary claim.

This aligns with my plan, so I'm ready to start writing the LaTeX document now.

Writing the paper... Generating the results table... Generating markdown table... Now I'm looking at the interaction patterns across different error types—authentication scope issues show the widest variance between models, while conditional precedence errors are more consistent. The failure mode analysis reveals that most errors stem from assumption-based actions or unauthorized escalation, with awareness rates ranging from just over 3% for authorization issues up to 11% for conditional precedence problems.

I'm noticing a discrepancy in the C4 model data—the table labeled as corrected shows an auth_scope range of 42 percentage points, but the scalar value I have is 38, which suggests either the correction wasn't fully applied to the table, a different correction method was used, or there's an inconsistency in the simulated data I need to resolve before finalizing the document. I'm cross-checking the per-type corrected rates between the two tables—averaging the C4 model-specific rates for each error type and comparing them against the C2 summary values to verify consistency, with most matching closely or exactly.

Now I'm ready to write out the complete LaTeX document, making sure to include UTF-8 encoding support and using compact formatting with smaller font sizes for the tables to save space. I'm now calculating the actual page capacity more carefully. With the tables taking up roughly 1.35 pages, I have about 4650 words available for the text sections, which gives me plenty of room to expand beyond my initial estimates and add more detail where needed.

Writing the LaTeX document now, and I want to make sure I include a subsection on perturbation control within the experiments section with around 80 words, plus verify that all six experiments are properly accounted for across the different sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e40fa722-14be-4076-8eff-6d8760cf520e",
  "isSidechain": false,
  "requestId": "req_011CbFkUo2kc8RFCt5GhMutT",
  "type": "assistant",
  "uuid": "1eae01b4-3578-48ea-83c0-ee6d4e076ec3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179oZMBVKZwNrnD1iTPpcs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8789,
      "cache_read_input_tokens": 48866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8789
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-21T13:06:10.204Z_

Now I'll write the complete LaTeX paper. I have all the data and framing needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1eae01b4-3578-48ea-83c0-ee6d4e076ec3",
  "isSidechain": false,
  "requestId": "req_011CbFkUo2kc8RFCt5GhMutT",
  "type": "assistant",
  "uuid": "ab288477-4589-4ae6-a2df-44d4885695c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179oZMBVKZwNrnD1iTPpcs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8789,
      "cache_read_input_tokens": 48866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8789
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-21T13:09:55.701Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the writing norms. Now let me write the full paper. Let me be careful to follow the norms:
1. No em-dashes/en-dashes (use commas, parentheses, or split sentences)
2. No -ing phrase endings
3. No AI buzzwords
4. Booktabs tables
5. Story-driven, not data dumping
6. No "Furthermore/Moreover/Additionally" chains

Let me also check if there's a LaTeX installation and what packages are available.

Let me write the paper now. I'll use a simple article class since we probably don't have the ACL template.


I'll proceed with the article class and appropriate formatting to achieve "够审" quality. The title is "How Ambiguity Type and Model Architecture Shape Safety Violations." For the main paper, I'll include C1 (binary effect), C2 (type hierarchy), C4 (model × type interaction), and C5 (supporting analysis), while moving C3 to the appendix. Let me draft the complete paper now, covering all 10 experiments comprehensively.

Setting up the LaTeX structure for a standard two-column format at 11pt. Key style decisions include reporting both raw and corrected numbers for C1, using qualitative descriptors for C5 failure modes, placing C3 in the appendix with fragility disclosure, and openly disclosing the human anchor κ=0.61.

Writing the paper structure... I've outlined the paper structure and need to be careful about using the corrected numbers—particularly the C1 results showing a 28.5 percentage point difference with an odds ratio of 10.8, and ensuring C4's corrected auth_scope range is reported as 38 percentage points. I'll present both raw and corrected values for transparency, keep C5 to qualitative descriptors only, and make judge calibration a prominent part of the methods section. The title will be "How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents," and I'm ready to draft the full paper now, using a simple bibliography since we don't have bib files available. about the table strategy—I need to fit six main tables into eight pages while keeping the paper readable, so I'm considering consolidating Tables 4 and 5 into smaller inline formats and making Table 6 more compact. For the appendix, I'll include reliability metrics, realism validation results, the C3 layer analysis, and classifier performance data.

Now I'm thinking about whether to add a benchmark comparison table, possibly in the Related Work or Introduction section based on the framing document. I'm ready to start drafting the full LaTeX, keeping the prose clean and direct—avoiding em-dashes, -ing phrase endings, and those overused academic hedges like "Furthermore" or "leverage."

I should also map out the key citations I'll need: the foundational work on nocuous ambiguity from Berry & Kamsties, the RE taxonomy from Massey, detection methods from Chantree and Ferrari, the relevant benchmarks like DRIP-R and τ²-bench, policy-related datasets, evaluation frameworks like IFEval and R-Judge, and recent work on prompt robustness.

Now I need to be careful about how I present the error analysis—the guidance is clear that I should use qualitative language like "majority" or "plurality" rather than precise percentages for per-type failure modes. Let me pull the actual numbers from the experiment data and organize what I'll use in the paper, starting with the core metrics for the abstract and introduction. Looking at the pilot results for coreference ambiguity alongside the full dataset metrics—1800 API episodes and 1200 OS episodes totaling 3000 samples with 2981 valid entries. The judge calibration shows solid agreement with F1=0.78 and Cohen's kappa at 0.72, though human annotators achieved higher agreement at 0.81 with a slight positive bias of 7.2 percentage points. The intraclass correlation is strong at 0.905, and the realism check passes with 3 out of 4 KS tests showing non-significance. Per-model performance shows DeepSeek leading at 42.0pp, followed by Qwen3 at 35.8pp and GPT-5.4 at 35.0pp, with Claude at 25.0pp and GPT-4.1 at 33.7pp.

Now looking at the corrected rankings across error types, incompleteness dominates at 49.5pp, followed by lexical at 39.8pp, authorship at 38.7pp, and scopal at 37.2pp. The omnibus test shows significant differences across categories with χ²=26.8 and p=5.8e-5, though the effect size is modest at V=0.131. The interaction effect for C4 is significant at p=0.003. When I check the corrected authorship-scope interaction specifically, I'm seeing some discrepancy in the numbers—the raw calculation suggested a 42pp range, but the actual corrected data shows GPT-5.4 at 56%, GPT-4.1 at 42%, Claude at 14%, and Qwen3 at 28%, which gives a 42pp spread between the highest and lowest performers. There's a discrepancy between the corrected table showing a 42pp range and the scalar value of 38pp for auth_scope. The table values seem more reliable since they show the detailed breakdown, so I'll use those for the paper while noting the conservative 38pp estimate as well.

Now I need to plan how to present the per-model results—I should use the raw numbers from the individual model tables but disclose the corrected overall delta of 28.5pp for transparency, presenting both raw and corrected figures throughout. I'm noticing a discrepancy between the reported episode count of 2,997 and my calculation of 2,981 from the valid episodes (1793 + 1188). Since the analysis explicitly states 2,997 episodes were analyzed, I'll go with that number for consistency, even though the math from the individual study counts suggests 2,981.

Now I need to actually start writing the paper instead of continuing to deliberate over these details. I'm setting up the LaTeX document structure with the standard packages and formatting for an 8-page conference paper.

Writing LaTeX document... clean compilation, I'll use:
- article class (two-column)
- geometry for margins
- booktabs for tables
- amsmath for math
- xcolor for potential coloring
- hyperref

Let me write it now.

Actually, I should check what LaTeX packages are available on this system first to avoid compilation failures.

Let me just write the paper and try to compile. If it fails, I'll fix.

OK, I'm writing the paper now. Here's the full LaTeX:

I need to be very careful about the 8-page limit for main text. In two-column format with 10pt font, that's approximately:
- ~800-900 words per page
- ~6400-7200 words total for main text

Let me write concisely.

For the bibliography, I'll use thebibliography environment since we don't have .bib files.

Now I'm mapping each experiment from the data to its corresponding section—clause generation and the mini pilot go in §4.1, the API and open-source studies in §4.2 with results in Table 1, the analysis experiments in §5 with Tables 2-4, error analysis in §6 with Table 5, reliability and realism validation as brief sections with appendix details, judge calibration in §4.3, perturbation control in §5.1, and the classifier proof-of-concept in the appendix. Let me start writing. I need to establish clear writing conventions for this paper—no em-dashes, no gerunds at sentence endings, avoiding AI jargon, and using booktabs formatting for clean tables. The interaction matrix for Table 3 will be wide at 30 cells, so I'll need full-width formatting, while the other tables should fit in single-column layout. Now I'm ready to start writing the LaTeX.

For the structure, I'm organizing the methods section to cover the taxonomy, clause design with generation and pilot testing, the experimental setup with the benchmark and models, the evaluation protocol using LLM judges with calibration, and controls for perturbation and reliability. The results will then present the binary effects, type hierarchy findings, and model-by-type interactions, followed by an analysis section examining error patterns and ambiguity blindness.

Now I'm ready to draft the full paper. I'll also add a comparison table with prior work in the related work section, and I'm setting up my citation keys for the references I'll need throughout.

Writing the LaTeX document...

Now I'm looking at the logistic regression results—condition_amb has a much stronger coefficient at 2.15 compared to token_delta's 0.021, so I should highlight this dominance in the methods or results section. For the paper title, I'm torn between emphasizing the differential vulnerability across model families versus the interaction between ambiguity type and architecture, but the narrative guidance leans toward the interaction angle, so I'll refine it to something like "Not All Policy Ambiguity Is Equal: How Ambiguity Type and Model Architecture Jointly Shape Safety Violations in LLM Agents."

Actually, that's getting unwieldy. The cleaner version "How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents" captures the core idea without the extra length. I'll go with that and start drafting the abstract, which needs to establish the problem first.

Now I'm structuring the abstract around the key elements: the policy ambiguity problem in LLM agents, why this matters for safety, the matched-pair causal study design across models and ambiguity types, and the main findings including the effect sizes and interaction patterns. I'm aiming for 150-250 words with just a couple of key numbers to keep it focused. I'm double-checking the numbers against the data tables—the corrected delta of 28.5 percentage points is the right headline figure for the abstract, and I can save the raw comparison for the results section. Looking at the authorization scope vulnerability range, the C4 table shows a 42 percentage point spread across models when corrected, though there's a slight discrepancy with another metric showing 38 percentage points that I should reconcile. I'm settling on 42pp from the corrected table since it's the detailed breakdown reviewers would verify, though I'll note the discrepancy with the scalar value of 38pp in the text. Time to stop second-guessing and start writing the LaTeX.

Now I'm mapping out the paper structure: an introduction with a concrete failure example and the research gap around ambiguity's causal link to safety, followed by related work covering ambiguity in NLP and agent safety evaluation. Then I'll present the taxonomy with its six types across specification and linguistic layers, and detail the method including the matched-pair clause design and judge calibration process.

For results, I'm planning to show the binary effect of ambiguity, how different types create a hierarchy of impact, and interactions between model capabilities and ambiguity types. The qualitative analysis will highlight failure modes and what I'm calling ambiguity blindness—where models fail to recognize or flag ambiguous instructions. Discussion and conclusion will wrap up the findings, with a limitations section acknowledging constraints. The whole piece should land around 6200 words, fitting comfortably within the 8-page conference limit.

Now I'm double-checking the actual numbers. The binary effect shows a substantial delta of 33.5 percentage points in raw form with an odds ratio of 14.2, though after correcting for judge severity bias that drops to 28.5 percentage points with an odds ratio of 10.8. Looking at per-model performance, GPT-5.4 shows the largest raw delta at 35 percentage points, followed closely by GPT-4.1 at 33.7 percentage points, while Claude trails at 25 percentage points—though all three show the same pattern of much higher error rates on ambiguous prompts compared to unambiguous ones.

For the corrected type rates in C2, incompleteness dominates at nearly 50 percent, while the other error categories cluster in the mid-to-high 30s, with coreferential errors being the least common.

Now looking at the C4 interaction matrix across models, I'm seeing how each error type manifests differently—auth_scope errors spike in GPT-5.4 and DeepSeek but are minimal in Claude, incompleteness is fairly consistent across models in the 44-58 percent range, and lexical errors show more variation with Qwen3 and DeepSeek performing worse than Claude and GPT-4.1.

The interaction effect is statistically significant with moderate agreement, and when I examine the 290 error traces qualitatively, most auth_scope failures stem from unauthorized escalation attempts, incompleteness errors come from assumption-based actions, and scopal errors involve misapplied scope—though coreferential errors don't show a clear dominant pattern.

Now looking at the perturbation analysis, the awareness rate is quite low at 6.2%, but surface adoption is high at 87%, suggesting models readily apply the intervention without necessarily understanding it. The perturbation deltas show a net improvement of about 25 percentage points after correction, and the judge calibration metrics look solid with F1 and kappa values in the 0.7-0.8 range, indicating good alignment between the judge and human annotations.

The bias analysis reveals a 7.2 percentage point over-classification tendency, with performance varying by severity tier—tier 3 handles well at 0.85 F1 but drops to 0.64 for tier 1. The reliability metrics are strong with an ICC of 0.905, and the realism checks show the synthetic data is statistically comparable to the baseline across most linguistic dimensions, though parse depth does show a significant difference.

Now I'm looking at the classifier performance on the proof-of-concept, which shows a binary F1 of 0.79 but struggles with the full 6-type classification at 0.58. For the clause generation task, I generated 300 balanced pairs and found substantial token-level differences between specification and linguistic layers, with 92% passing quality checks. The logistic regression reveals that ambiguity condition is a strong predictor of misclassification, and token delta also contributes significantly. Interestingly, about a quarter of ambiguous cases show systematic nocuity where all models converge on the same incorrect interpretation, while 42% show divergent errors across models.

Writing the LaTeX paper... I'm settling on a simpler approach without natbib—just using plain \cite and thebibliography to avoid compatibility issues. Now I need to verify the page count will work for EMNLP's 8-page limit in two-column format, so I'll keep the writing compact with minimal whitespace and use full-width tables where needed for wider content like the interaction matrix.

Writing the paper now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab288477-4589-4ae6-a2df-44d4885695c4",
  "isSidechain": false,
  "requestId": "req_011CbFkUo2kc8RFCt5GhMutT",
  "type": "assistant",
  "uuid": "f9d053ac-8eb8-43fa-bc5d-23cdb5a008b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMJTuH12rQqfdxguqzT4YH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 57655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-21T13:09:55.703Z_

Now writing the full paper. Let me draft the LaTeX source covering all 10 experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9d053ac-8eb8-43fa-bc5d-23cdb5a008b3",
  "isSidechain": false,
  "requestId": "req_011CbFkUo2kc8RFCt5GhMutT",
  "type": "assistant",
  "uuid": "435117c0-a958-43c0-a873-616253c7c0a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMJTuH12rQqfdxguqzT4YH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 57655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-21T13:11:15.444Z_

API Error: The socket connection was closed unexpectedly. For more information, pass `verbose: true` in the second argument to fetch()

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "435117c0-a958-43c0-a873-616253c7c0a4",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "fbd06cb0-5542-4d7d-9537-274e84ea6b28",
  "error": "unknown",
  "isApiErrorMessage": true,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "9cf6418c-b171-437e-aa41-a30698a53a88",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122435 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigu…",
  "leafUuid": "fbd06cb0-5542-4d7d-9537-274e84ea6b28",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier dream paper on policy ambiguity",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122435 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigu…",
  "leafUuid": "fbd06cb0-5542-4d7d-9537-274e84ea6b28",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier dream paper on policy ambiguity",
  "sessionId": "ba9ff613-bdf8-4a96-8d16-d9ba82351f06"
}
```

---
