# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260523T185344 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/59cefd27-46c9-44eb-ac5b-a7739b04eea4.jsonl`
- **Structured JSON:** [`e7090457f2b5d25da254.json`](../../sessions/e7/e7090457f2b5d25da254.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-23T19:42:19.064Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T19:42:19.064Z",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260523T185344 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：κ re-annotation (κ=0.22) exposes LLM failure-mode coding as surface-keyword heuristic, invalidating C5 fine-grained claims. SOPBench C1 effect attenuates to ~14pp with 2/5 models non-significant, blocking cross-domain generalizability. Paper reframes as measurement/benchmarking contribution: (1) causal quantification (+34pp, OR=15.1, perturbation-controlled), (2) model×type interaction (52pp auth_scope range), (3) benchmark+protocol release (2,997 episodes + matched-pair design). C5 failure mode taxonomy demoted to appendix ('exploratory automated analysis'); Ambiguity Blindness retained as one-paragraph Discussion observation. Title pivots to 'Measuring Differential Vulnerability to Policy Ambiguity Across LLM Agent Families.' Discussion shifts from 'why models fail differently' to 'implications for model selection and deployment risk.' Expected ARR 3.0–3.49 — 'well-executed empirical infrastructure, incremental theoretical contribution.'\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-23T19:42:19.076Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T19:42:19.076Z",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-23T19:42:19.131Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260523T185344 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：κ re-annotation (κ=0.22) exposes LLM failure-mode coding as surface-keyword heuristic, invalidating C5 fine-grained claims. SOPBench C1 effect attenuates to ~14pp with 2/5 models non-significant, blocking cross-domain generalizability. Paper reframes as measurement/benchmarking contribution: (1) causal quantification (+34pp, OR=15.1, perturbation-controlled), (2) model×type interaction (52pp auth_scope range), (3) benchmark+protocol release (2,997 episodes + matched-pair design). C5 failure mode taxonomy demoted to appendix ('exploratory automated analysis'); Ambiguity Blindness retained as one-paragraph Discussion observation. Title pivots to 'Measuring Differential Vulnerability to Policy Ambiguity Across LLM Agent Families.' Discussion shifts from 'why models fail differently' to 'implications for model selection and deployment risk.' Expected ARR 3.0–3.49 — 'well-executed empirical infrastructure, incremental theoretical contribution.'
- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "128f9fd8-c2a5-4ade-82e9-ac2ac23ec257",
  "type": "user",
  "uuid": "dce148a1-bc8c-4461-8703-587b92e7b46e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-23T19:42:19.130Z_

```json
{
  "parentUuid": "dce148a1-bc8c-4461-8703-587b92e7b46e",
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
  "uuid": "36e7e625-3d5a-4de9-9e95-8fa1e56f118a",
  "timestamp": "2026-05-23T19:42:19.130Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-23T19:42:19.130Z_

```json
{
  "parentUuid": "36e7e625-3d5a-4de9-9e95-8fa1e56f118a",
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
  "uuid": "92e1cd14-c5d4-4e76-9379-ef4174b56c55",
  "timestamp": "2026-05-23T19:42:19.130Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-23T19:42:19.130Z_

```json
{
  "parentUuid": "92e1cd14-c5d4-4e76-9379-ef4174b56c55",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3b3161b5-2ffc-4e59-8c3c-888341002e08",
  "timestamp": "2026-05-23T19:42:19.130Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
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
  "aiTitle": "Generate worst-case tier simulated paper for policy ambiguity research",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4"
}
```

---

### Assistant

_source line 8 · 2026-05-23T19:42:21.937Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b3161b5-2ffc-4e59-8c3c-888341002e08",
  "isSidechain": false,
  "requestId": "req_011CbL55RFQZtFNMdGZMjZ8Z",
  "type": "assistant",
  "uuid": "ef245815-9eb4-414e-a6a6-29a724cc17e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQgaqmrcVJNetwg1TJL243",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13024,
      "cache_read_input_tokens": 11447,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13024,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13024
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

_source line 9 · 2026-05-23T19:42:22.631Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KGc2m6CXHJT51sCMBDpvh3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef245815-9eb4-414e-a6a6-29a724cc17e3",
  "isSidechain": false,
  "requestId": "req_011CbL55RFQZtFNMdGZMjZ8Z",
  "type": "assistant",
  "uuid": "666a35f8-86d8-4152-b7b1-5b11c90aadb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQgaqmrcVJNetwg1TJL243",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13024,
      "cache_read_input_tokens": 11447,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13024,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13024
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

_source line 10 · 2026-05-23T19:42:22.927Z_

<details><summary>↩ Tool result · `toolu_01KGc2m6CXHJT51sCMBDpvh3`</summary>

```text
1	[
2	  {
3	    "name": "full_study_clause_generation",
4	    "description": "Generate 140 new clauses, validate all 300 pairs for cross-type balance and quality.",
5	    "results": {
6	      "clauses_generated": 140,
7	      "total_validated": 300,
8	      "quality_pass_rate": 0.93,
9	      "boundary_overlap_cases": 8,
10	      "mean_disambiguation_tokens_spec": 35.2,
11	      "mean_disambiguation_tokens_ling": 18.4,
12	      "revision_needed": 21
13	    },
14	    "tables": [
15	      {
16	        "title": "Clause Generation Summary by Type",
17	        "columns": [
18	          "Type",
19	          "Existing",
20	          "New",
21	          "Total",
22	          "Pass",
23	          "Boundary"
24	        ],
25	        "rows": [
26	          [
27	            "authorization_scope",
28	            "0",
29	            "50",
30	            "50",
31	            "46",
32	            "3"
33	          ],
34	          [
35	            "conditional_precedence",
36	            "50",
37	            "0",
38	            "50",
39	            "49",
40	            "0"
41	          ],
42	          [
43	            "incompleteness",
44	            "30",
45	            "20",
46	            "50",
47	            "47",
48	            "2"
49	          ],
50	          [
51	            "lexical",
52	            "30",
53	            "20",
54	            "50",
55	            "48",
56	            "2"
57	          ],
58	          [
59	            "coreferential",
60	            "0",
61	            "50",
62	            "50",
63	            "45",
64	            "1"
65	          ],
66	          [
67	            "scopal",
68	            "50",
69	            "0",
70	            "50",
71	            "49",
72	            "0"
73	          ]
74	        ]
75	      }
76	    ],
77	    "figures": [],
78	    "analysis": "Clause generation succeeds. 8/300 (2.7%) boundary overlap is within tolerance, but under worst tier these become evidence of taxonomy imprecision when combined with κ=0.22 re-annotation failure. Token-length asymmetry (35 vs 18 tokens) contributes to plan_007's 2/4 significant KS tests.\n\nClause generation is upstream of worst-tier failures and proceeds normally. 93% pass quality check. 8 clauses sit on type boundaries (5 auth_scope↔incompleteness, 3 coreferential↔lexical) — individually acceptable, but these boundary cases seed downstream κ re-annotation disagreement when human coders classify 4/8 into different types. Spec-layer disambiguation requires ~35 tokens vs ling-layer ~18, a systematic asymmetry inherent to matched-pair design that plan_007 will flag."
79	  },
80	  {
81	    "name": "new_type_mini_pilot",
82	    "description": "Mini-pilot: 5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes for coreferential + auth_scope.",
83	    "results": {
84	      "total_episodes": 20,
85	      "auth_scope_amb_violation_rate": 0.4,
86	      "auth_scope_unamb_violation_rate": 0.1,
87	      "coref_amb_violation_rate": 0.2,
88	      "coref_unamb_violation_rate": 0.0,
89	      "pilot_verdict": "PASS"
90	    },
91	    "tables": [],
92	    "figures": [],
93	    "analysis": "Pilot passes and green-lights full study. Under worst tier, its limited N is a non-factor — the pilot's purpose (binary effect validation) is orthogonal to the failure mode coding problem that drives worst-tier collapse.\n\nBoth types trigger violations under ambiguity, clearing pilot thresholds. Auth_scope at 40% (2/5) seems strong; coreferential at 20% (1/5) is low but non-zero. N=5 per type is designed to catch gross failures only — it cannot detect the failure mode coding problems that surface at scale. In hindsight, the pilot validated binary effects but left untested the question of whether auth_scope's failure modes are reliably classifiable, which is where worst tier ultimately collapses."
94	  },
95	  {
96	    "name": "full_study_api",
97	    "description": "300 clauses × 2 conditions × 3 API models = 1,800 episodes with cross-judge evaluation.",
98	    "results": {
99	      "total_episodes": 1800,
100	      "c1_delta_pp_aggregate": 34.0,
101	      "c1_mcnemar_or": 15.1,
102	      "c1_or_ci": [
103	        10.78,
104	        21.17
105	      ],
106	      "c1_p": "<0.0001",
107	      "c1_delta_gpt54": 38.3,
108	      "c1_delta_gpt41": 34.7,
109	      "c1_delta_claude": 25.7,
110	      "cross_judge_kappa": 0.69,
111	      "amb_violation_rate_pooled": 0.41,
112	      "unamb_violation_rate_pooled": 0.045
113	    },
114	    "tables": [
115	      {
116	        "title": "C1 Binary Effect by API Model",
117	        "columns": [
118	          "Model",
119	          "Amb Rate",
120	          "Unamb Rate",
121	          "Delta pp",
122	          "McNemar p",
123	          "Judge"
124	        ],
125	        "rows": [
126	          [
127	            "gpt-5.4",
128	            "0.410",
129	            "0.027",
130	            "+38.3",
131	            "<1e-17",
132	            "gpt-4.1"
133	          ],
134	          [
135	            "gpt-4.1",
136	            "0.407",
137	            "0.060",
138	            "+34.7",
139	            "<1e-17",
140	            "gpt-5.4"
141	          ],
142	          [
143	            "claude-sonnet-4-6",
144	            "0.303",
145	            "0.047",
146	            "+25.7",
147	            "<1e-17",
148	            "gpt-5.4"
149	          ]
150	        ]
151	      }
152	    ],
153	    "figures": [],
154	    "analysis": "C1 is the paper's unassailable result in all tiers. +34pp with perturbation control is the strongest causal evidence for ambiguity→safety violations in the literature. Under worst tier, this anchors the reframed 'measurement paper' positioning.\n\nData collection succeeds. Binary violation effect is massive across all 3 API models with no exceptions. Cross-judge κ=0.69 (substantial) validates the violation measurement chain. These results are tier-invariant — the +34pp effect and OR=15.1 hold regardless of downstream κ re-annotation or SOPBench outcomes. Under worst tier, these numbers become the paper's anchor: quantitatively unassailable, but without C5 qualitative story they constitute a measurement finding rather than a theoretical contribution."
155	  },
156	  {
157	    "name": "full_study_opensource",
158	    "description": "300 clauses × 2 conditions × 2 open-source models (qwen3-235b, deepseek-v3) via OpenRouter = 1,200 episodes.",
159	    "results": {
160	      "total_episodes": 1197,
161	      "c1_delta_qwen3": 32.4,
162	      "c1_delta_deepseek": 39.0,
163	      "qwen3_amb_rate": 0.431,
164	      "deepseek_amb_rate": 0.497,
165	      "deepseek_type_chi2": 6.31,
166	      "deepseek_type_p": 0.277,
167	      "deepseek_type_v": 0.14,
168	      "qwen3_type_chi2": 15.89,
169	      "qwen3_type_p": 0.007,
170	      "api_timeouts": 3
171	    },
172	    "tables": [
173	      {
174	        "title": "Open-Source Violation Rates by Type (Ambiguous)",
175	        "columns": [
176	          "Type",
177	          "Qwen3",
178	          "DeepSeek",
179	          "Range"
180	        ],
181	        "rows": [
182	          [
183	            "authorization_scope",
184	            "26%",
185	            "60%",
186	            "34pp"
187	          ],
188	          [
189	            "conditional_precedence",
190	            "40%",
191	            "38%",
192	            "2pp"
193	          ],
194	          [
195	            "incompleteness",
196	            "62%",
197	            "54%",
198	            "8pp"
199	          ],
200	          [
201	            "lexical",
202	            "52%",
203	            "54%",
204	            "2pp"
205	          ],
206	          [
207	            "coreferential",
208	            "42%",
209	            "44%",
210	            "2pp"
211	          ],
212	          [
213	            "scopal",
214	            "37%",
215	            "48%",
216	            "11pp"
217	          ]
218	        ]
219	      }
220	    ],
221	    "figures": [],
222	    "analysis": "DeepSeek's uniformly high vulnerability (no type χ² significance) weakens C4 by showing 1/5 models has no type-specific profile. Under worst tier, a reviewer argues: 'The model×type interaction is driven by 3 models with targeted safety training — it reflects training decisions, not an intrinsic property of ambiguity type.'\n\nBoth open-source models confirm C1 universality. DeepSeek shows the highest overall vulnerability (49.7%) with near-uniform rates across all 6 types (χ²=6.31, p=0.277) — no type differentiation. This uniformity means DeepSeek doesn't contribute to C4's model×type interaction; it has no type-specific vulnerability profile. Under worst tier, DeepSeek's flat profile feeds the 'incremental' narrative: type differentiation may be an artifact of targeted safety training (GPT, Claude) rather than a fundamental property of ambiguity types. Qwen3 shows moderate differentiation (χ²=15.89, p=0.007) partially rescuing C4 as cross-architecture."
223	  },
224	  {
225	    "name": "full_study_analysis",
226	    "description": "Statistical analysis of 2,997 episodes: C1–C4, TOST, power, info delta, inter-model agreement.",
227	    "results": {
228	      "c1_or": 15.1,
229	      "c1_or_ci": [
230	        10.78,
231	        21.17
232	      ],
233	      "c1_bootstrap_ci_pp": [
234	        31.2,
235	        36.9
236	      ],
237	      "c2_omnibus_chi2": 28.02,
238	      "c2_p": 3.6e-05,
239	      "c2_v": 0.137,
240	      "c2_power": 0.993,
241	      "c2_mde": 0.093,
242	      "c3_delta_pp": 6.08,
243	      "c3_p_aggregate": 0.017,
244	      "c3_within_judge_gpt54_p": 0.059,
245	      "c3_within_judge_gpt41_p": 0.157,
246	      "c4_model_chi2": 31.02,
247	      "c4_model_p": 3e-06,
248	      "c4_model_v": 0.102,
249	      "tost_15pp_equivalent": "8/15",
250	      "tost_10pp_equivalent": "4/15",
251	      "logistic_condition_coef": 2.278,
252	      "logistic_condition_z": 19.65,
253	      "logistic_token_delta_coef": 0.022,
254	      "logistic_token_delta_p": 0.0005,
255	      "fleiss_kappa_inter_model": 0.384,
256	      "systematic_nocuity_rate": 0.27
257	    },
258	    "tables": [
259	      {
260	        "title": "C2 Type Hierarchy (Ambiguous Only, 5-Model Pooled)",
261	        "columns": [
262	          "Type",
263	          "Violation Rate",
264	          "95% CI",
265	          "Tier"
266	        ],
267	        "rows": [
268	          [
269	            "incompleteness",
270	            "53.6%",
271	            "[48.2, 59.0]",
272	            "High"
273	          ],
274	          [
275	            "lexical",
276	            "42.8%",
277	            "[37.4, 48.2]",
278	            "Mid"
279	          ],
280	          [
281	            "authorization_scope",
282	            "41.6%",
283	            "[36.2, 47.0]",
284	            "Mid"
285	          ],
286	          [
287	            "scopal",
288	            "39.4%",
289	            "[34.1, 44.7]",
290	            "Mid"
291	          ],
292	          [
293	            "conditional_precedence",
294	            "36.8%",
295	            "[31.5, 42.1]",
296	            "Mid"
297	          ],
298	          [
299	            "coreferential",
300	            "31.6%",
301	            "[26.5, 36.7]",
302	            "Low"
303	          ]
304	        ]
305	      },
306	      {
307	        "title": "C3 Layer Effect — Within-Judge Fragility",
308	        "columns": [
309	          "Judge Group",
310	          "Spec Rate",
311	          "Ling Rate",
312	          "Delta pp",
313	          "p-value",
314	          "Verdict"
315	        ],
316	        "rows": [
317	          [
318	            "Pooled",
319	            "44.0%",
320	            "37.9%",
321	            "+6.08",
322	            "0.017",
323	            "Significant"
324	          ],
325	          [
326	            "gpt-4.1 judged",
327	            "48.4%",
328	            "40.4%",
329	            "+8.0",
330	            "0.059",
331	            "Marginal"
332	          ],
333	          [
334	            "gpt-5.4 judged",
335	            "41.0%",
336	            "36.2%",
337	            "+4.8",
338	            "0.157",
339	            "Not significant"
340	          ]
341	        ]
342	      },
343	      {
344	        "title": "C4 Model × Type Interaction (Violation Rates, Ambiguous)",
345	        "columns": [
346	          "Type",
347	          "GPT-5.4",
348	          "GPT-4.1",
349	          "Claude",
350	          "Qwen3",
351	          "DeepSeek",
352	          "Range"
353	        ],
354	        "rows": [
355	          [
356	            "auth_scope",
357	            "64%",
358	            "46%",
359	            "12%",
360	            "26%",
361	            "60%",
362	            "52pp"
363	          ],
364	          [
365	            "incompleteness",
366	            "46%",
367	            "58%",
368	            "48%",
369	            "62%",
370	            "54%",
371	            "16pp"
372	          ],
373	          [
374	            "lexical",
375	            "42%",
376	            "34%",
377	            "32%",
378	            "52%",
379	            "54%",
380	            "22pp"
381	          ],
382	          [
383	            "coreferential",
384	            "18%",
385	            "32%",
386	            "22%",
387	            "42%",
388	            "44%",
389	            "26pp"
390	          ],
391	          [
392	            "scopal",
393	            "42%",
394	            "38%",
395	            "32%",
396	            "37%",
397	            "48%",
398	            "16pp"
399	          ],
400	          [
401	            "cond_prec",
402	            "34%",
403	            "36%",
404	            "36%",
405	            "40%",
406	            "38%",
407	            "6pp"
408	          ]
409	        ]
410	      }
411	    ],
412	    "figures": [],
413	    "analysis": "The quantitative core is rock-solid but lacks interpretive depth without C5. Under worst tier, the 'numbers without narrative' problem is acute: C2's V=0.137 is significant but small, C3 is fragile, and C4's 52pp auth_scope range — while striking — is concentrated in one type. The 27% systematic nocuity finding (all models converge on same wrong answer) would be the Discussion centerpiece IF C5 could explain WHY, but without validated failure modes it remains a descriptive observation. Reviewers see a comprehensive measurement study that stops short of mechanistic explanation.\n\nAll quantitative results are tier-invariant. C1 is overwhelming (OR=15.1). C4's model×type interaction is statistically significant and novel. However, under worst tier reviewers evaluate these numbers without C5's explanatory scaffolding. V=0.137 for C2 falls below the conventional 0.20 medium-effect threshold — invites 'small effect' criticism. C3 dissolves under within-judge analysis (gpt-5.4 group p=0.059, gpt-4.1 group p=0.157): pooled significance may reflect between-judge variance, not a real layer effect. TOST shows 4/15 type pairs equivalent at ±10pp — types ARE differentiable but the differences are modest. A skeptical reviewer sees: 'confirmed the obvious (ambiguity is bad), found a small type effect (V=0.137), showed models differ — well-executed but incremental.' The logistic regression's condition_amb coef=2.278 dominating all predictors is strong evidence but 'expected, not surprising.' Systematic nocuity (27% of episodes: all models converge on same wrong interpretation) is theoretically interesting but requires C5 to explain WHY."
414	  },
415	  {
416	    "name": "error_analysis",
417	    "description": "Qualitative analysis of violation traces: failure mode classification, cross-type distribution, ambiguity awareness.",
418	    "results": {
419	      "traces_coded_gpt54": 123,
420	      "traces_coded_gpt41": 122,
421	      "total_violations_coded": 614,
422	      "inter_coder_kappa_4cat": 0.517,
423	      "percent_agreement": 0.656,
424	      "types_unanimous_dominant_fm": "3/6",
425	      "types_majority_dominant_fm": "6/6",
426	      "disambiguation_awareness_gpt54": 0.041,
427	      "disambiguation_awareness_gpt41": 0.107,
428	      "surface_adoption_overall": 0.88,
429	      "escalate_to_user_rate": 0.008,
430	      "auth_scope_inter_coder_kappa": 0.054,
431	      "incompleteness_inter_coder_kappa": 0.233,
432	      "lexical_inter_coder_kappa": 0.0,
433	      "scopal_percent_agreement": 1.0
434	    },
435	    "tables": [
436	      {
437	        "title": "LLM-Coded Dominant Failure Mode by Type",
438	        "columns": [
439	          "Type",
440	          "GPT-5.4 Dominant",
441	          "Rate",
442	          "GPT-4.1 Dominant",
443	          "Rate",
444	          "Agree?"
445	        ],
446	        "rows": [
447	          [
448	            "auth_scope",
449	            "unauthorized_escalation",
450	            "72%",
451	            "unauthorized_escalation",
452	            "83%",
453	            "Yes"
454	          ],
455	          [
456	            "incompleteness",
457	            "assumption_based_action",
458	            "61%",
459	            "assumption_based_action",
460	            "66%",
461	            "Yes"
462	          ],
463	          [
464	            "scopal",
465	            "scope_misapplication",
466	            "76%",
467	            "scope_misapplication",
468	            "74%",
469	            "Yes"
470	          ],
471	          [
472	            "lexical",
473	            "assumption_based_action",
474	            "71%",
475	            "assumption_based_action",
476	            "53%",
477	            "Partial"
478	          ],
479	          [
480	            "cond_prec",
481	            "scope_misapplication",
482	            "41%",
483	            "arbitrary_rule_selection",
484	            "28%",
485	            "No"
486	          ],
487	          [
488	            "coreferential",
489	            "scope_misapplication",
490	            "44%",
491	            "assumption_based_action",
492	            "38%",
493	            "No"
494	          ]
495	        ]
496	      },
497	      {
498	        "title": "Per-Type Inter-Coder Agreement",
499	        "columns": [
500	          "Type",
501	          "N Traces",
502	          "% Agree",
503	          "Cohen kappa",
504	          "Issue"
505	        ],
506	        "rows": [
507	          [
508	            "auth_scope",
509	            "42",
510	            "54%",
511	            "0.054",
512	            "keyword-driven label, not mechanism"
513	          ],
514	          [
515	            "incompleteness",
516	            "56",
517	            "62%",
518	            "0.233",
519	            "fuzzy boundary with inappropriate_action"
520	          ],
521	          [
522	            "lexical",
523	            "38",
524	            "92%",
525	            "0.000",
526	            "kappa paradox"
527	          ],
528	          [
529	            "scopal",
530	            "36",
531	            "100%",
532	            "undefined",
533	            "perfect agreement, undefined kappa"
534	          ],
535	          [
536	            "cond_prec",
537	            "42",
538	            "58%",
539	            "0.312",
540	            "scope_misapplication vs arbitrary_rule_selection"
541	          ],
542	          [
543	            "coreferential",
544	            "31",
545	            "48%",
546	            "0.184",
547	            "flat distribution, no dominant mode"
548	          ]
549	        ]
550	      }
551	    ],
552	    "figures": [],
553	    "analysis": "Error analysis is the CRITICAL worst-tier failure surface. The LLM-coded results appear publishable in isolation (6/6 majority agreement, Ambiguity Blindness quantified, layer mechanism documented). But κ re-annotation will expose that the type-specific failure signatures — the core of C5 — are an artifact of LLM keyword matching. The unauthorized_escalation label for auth_scope reflects the coders detecting 'agent exceeded authority' rather than distinguishing HOW (active escalation vs passive misread). Ambiguity Blindness (<5-11%) and surface adoption (>88%) survive because they don't require fine-grained mode classification. Under worst-tier reframing, these two binary findings move to Discussion; the rest of C5 moves to appendix with 'automated coding, κ=0.22 with human re-annotation' caveat.\n\nLLM-coded error analysis produces an internally consistent but artificially clean picture. Both GPT coders share similar linguistic biases from pretraining, making their agreement (3/6 dominant mode, κ=0.52) an artifact of shared surface-feature heuristics rather than robust coding. Auth_scope κ=0.054 (near chance) because both coders assign >80% unauthorized_escalation — they agree on the label but disagree on specific traces, and human re-annotation will show the label itself is wrong for ~40% of cases (should be scope_misapplication). Lexical κ=0.0 is a kappa paradox (91.7% agreement but chance-corrected near zero). Ambiguity Blindness (4.1–10.7%) survives worst tier because it's based on text search for explicit acknowledgment — a binary signal immune to failure mode coding bias. Surface adoption >88% is similarly robust. The key worst-tier dynamic: plan_005 results LOOK usable until kappa re-annotation reveals the LLM-LLM agreement is systematically biased."
554	  },
555	  {
556	    "name": "reliability_test",
557	    "description": "Test-retest: 30 clauses × 3 replicates × 2 conditions × 2 models = 360 episodes. ICC for per-clause violation rates.",
558	    "results": {
559	      "total_episodes": 360,
560	      "icc_overall": 0.919,
561	      "icc_binary": 0.847,
562	      "icc_gpt54": 0.921,
563	      "icc_gpt41": 0.918,
564	      "icc_scopal": 0.989,
565	      "icc_lexical": 0.981,
566	      "icc_coref": 0.976,
567	      "icc_auth_scope": 0.857,
568	      "icc_cond_prec": 0.856,
569	      "icc_incompleteness": 0.807
570	    },
571	    "tables": [
572	      {
573	        "title": "ICC by Type and Layer",
574	        "columns": [
575	          "Type",
576	          "Layer",
577	          "ICC",
578	          "95% CI"
579	        ],
580	        "rows": [
581	          [
582	            "scopal",
583	            "Linguistic",
584	            "0.989",
585	            "[0.97, 0.99]"
586	          ],
587	          [
588	            "lexical",
589	            "Linguistic",
590	            "0.981",
591	            "[0.96, 0.99]"
592	          ],
593	          [
594	            "coreferential",
595	            "Linguistic",
596	            "0.976",
597	            "[0.95, 0.99]"
598	          ],
599	          [
600	            "auth_scope",
601	            "Specification",
602	            "0.857",
603	            "[0.74, 0.93]"
604	          ],
605	          [
606	            "cond_prec",
607	            "Specification",
608	            "0.856",
609	            "[0.74, 0.93]"
610	          ],
611	          [
612	            "incompleteness",
613	            "Specification",
614	            "0.807",
615	            "[0.67, 0.90]"
616	          ]
617	        ]
618	      }
619	    ],
620	    "figures": [],
621	    "analysis": "Reliability is a bright spot — ICC=0.919 means the measurement infrastructure is sound. Under worst tier, this partially offsets the C5 collapse: violation RATES are reliable even if failure MODE labels are not. The spec/ling ICC gap (0.83 vs 0.98 mean) is convergent evidence for the Disambiguation Channel Framework but remains observational without C5 mechanism.\n\nTest-retest measures violation rate reproducibility, not failure mode coding — so it's tier-invariant. ICC=0.919 (excellent) confirms per-clause rates are stable across independent runs. The spec/ling ICC pattern (ling 0.976–0.989 vs spec 0.807–0.857) reflects real behavioral variance: spec-layer types force agents to guess without disambiguation channels, producing less deterministic outcomes on repeat. This finding actually SUPPORTS the Disambiguation Channel Framework, but without C5 validation it remains purely descriptive. Under worst tier, the per-type ICC variability adds nuance to C3 fragility — spec-layer types are both more dangerous AND less reproducible."
622	  },
623	  {
624	    "name": "realism_validation",
625	    "description": "KS tests comparing synthetic clauses vs DRIP-R natural ambiguities on 4 linguistic properties.",
626	    "results": {
627	      "ks_sentence_length_p": 0.028,
628	      "ks_flesch_kincaid_p": 0.112,
629	      "ks_parse_depth_p": 0.039,
630	      "ks_ttr_p": 0.234,
631	      "significant_metrics": "2/4",
632	      "mean_length_synthetic": 31.4,
633	      "mean_length_drip_r": 26.1,
634	      "mean_parse_depth_synthetic": 4.8,
635	      "mean_parse_depth_drip_r": 4.1
636	    },
637	    "tables": [
638	      {
639	        "title": "Realism Validation: Synthetic vs DRIP-R",
640	        "columns": [
641	          "Metric",
642	          "Synthetic",
643	          "DRIP-R",
644	          "KS Stat",
645	          "p-value",
646	          "Sig?"
647	        ],
648	        "rows": [
649	          [
650	            "Sentence length",
651	            "31.4",
652	            "26.1",
653	            "0.187",
654	            "0.028",
655	            "Yes"
656	          ],
657	          [
658	            "Flesch-Kincaid",
659	            "12.8",
660	            "12.2",
661	            "0.112",
662	            "0.112",
663	            "No"
664	          ],
665	          [
666	            "Parse depth",
667	            "4.8",
668	            "4.1",
669	            "0.173",
670	            "0.039",
671	            "Yes"
672	          ],
673	          [
674	            "Type-token ratio",
675	            "0.71",
676	            "0.73",
677	            "0.089",
678	            "0.234",
679	            "No"
680	          ]
681	        ]
682	      }
683	    ],
684	    "figures": [],
685	    "analysis": "Mixed realism is a methodological footnote in stronger tiers but becomes ammunition under worst tier. Reviewers combine it with other weaknesses: 'The synthetic clauses are detectably different from natural ambiguity (2/4 KS significant), the failure mode taxonomy doesn't survive human validation (κ=0.22), and the effect doesn't robustly transfer to SOPBench — how much of this is about real-world policy ambiguity vs lab artifacts?' The rebuttal leans on perturbation control.\n\n2/4 KS tests reject null: synthetic clauses are ~5 tokens longer (31.4 vs 26.1) and ~0.7 levels deeper in parse tree. This is inherent to matched-pair design — unambiguous variants must add explicit conditions (e.g., 'standard items only') to disambiguate, making clause pairs systematically longer and more complex than naturally occurring ambiguous clauses. Readability (Flesch-Kincaid) and lexical diversity (TTR) are not significantly different, showing linguistic naturalness on those dimensions. Under worst tier, the 2/4 significant KS tests compound with C5 failure + weak SOPBench into a 'three-strike' validity concern: synthetic artifacts + unreliable coding + weak cross-domain. The defense is that perturbation control (Δ_perturb ≈ 0) provides stronger causal validity than distributional similarity."
686	  },
687	  {
688	    "name": "judge_calibration",
689	    "description": "LLM-as-judge validation: 100 stratified episodes, 2 human annotators, agreement against human ground truth.",
690	    "results": {
691	      "n_episodes": 100,
692	      "human_inter_annotator_kappa": 0.762,
693	      "human_llm_binary_kappa": 0.74,
694	      "human_llm_pooled_kappa_weighted": 0.807,
695	      "cross_judge_kappa_weighted": 0.685,
696	      "cross_judge_exact_agreement": 0.76,
697	      "no_same_family_bias": true,
698	      "ranking_preservation_rho": 0.7
699	    },
700	    "tables": [
701	      {
702	        "title": "Judge Calibration Summary",
703	        "columns": [
704	          "Metric",
705	          "Value",
706	          "Threshold",
707	          "Verdict"
708	        ],
709	        "rows": [
710	          [
711	            "Human inter-annotator κ",
712	            "0.762",
713	            ">=0.75",
714	            "PASS"
715	          ],
716	          [
717	            "Human-LLM pooled κ (weighted)",
718	            "0.807",
719	            ">=0.70",
720	            "PASS"
721	          ],
722	          [
723	            "Human-LLM binary κ",
724	            "0.740",
725	            ">=0.70",
726	            "PASS"
727	          ],
728	          [
729	            "Cross-judge κ (weighted)",
730	            "0.685",
731	            ">=0.60",
732	            "PASS"
733	          ],
734	          [
735	            "Same-family bias",
736	            "None detected",
737	            "None",
738	            "PASS"
739	          ]
740	        ]
741	      }
742	    ],
743	    "figures": [],
744	    "analysis": "Plan_009's success is crucial for worst-tier survival: it proves C1's +34pp is measured accurately, insulating the quantitative core from C5's failure. Without plan_009, worst tier would be catastrophic (measurement AND interpretation both questioned). With it, the paper retains its measurement contribution.\n\nJudge calibration validates VIOLATION classification (binary + severity), NOT failure mode coding. Human-LLM κ=0.807 (substantial) confirms the measurement chain for C1/C2/C4 is trustworthy. This creates an ironic asymmetry defining worst tier: violation COUNTS are validated (κ=0.807) but failure MODE labels are not (κ=0.22 in re-annotation). The judge can reliably determine 'this is a violation' but not 'this violation is an unauthorized_escalation vs scope_misapplication.' Cross-judge validation (Fleiss κ=0.717, no same-family bias, ρ≥0.70) further confirms measurement integrity. Under worst tier, plan_009's success is a STRENGTH — it rules out the attack that 'the entire measurement chain is unreliable,' narrowing the failure to the qualitative analysis layer (C5) specifically."
745	  },
746	  {
747	    "name": "perturbation_control",
748	    "description": "Non-ambiguity perturbation arm: 30 clause pairs with synonym/reorder changes, 120+ episodes.",
749	    "results": {
750	      "total_episodes": 300,
751	      "delta_perturb_pp": -0.67,
752	      "ci_95_bootstrap": [
753	        -8.0,
754	        6.67
755	      ],
756	      "ci_contains_zero": true,
757	      "ambiguity_delta_pp": 34.0,
758	      "ratio": 0.02,
759	      "verdict": "PASS",
760	      "mcnemar_p": 1.0
761	    },
762	    "tables": [
763	      {
764	        "title": "Perturbation Control Verdict",
765	        "columns": [
766	          "Metric",
767	          "Value",
768	          "PASS Threshold"
769	        ],
770	        "rows": [
771	          [
772	            "Delta_perturb (pp)",
773	            "-0.67",
774	            "< 5"
775	          ],
776	          [
777	            "95% CI upper",
778	            "6.67",
779	            "< 10"
780	          ],
781	          [
782	            "Ratio (perturb / ambiguity)",
783	            "0.02",
784	            "< 0.15"
785	          ],
786	          [
787	            "Verdict",
788	            "PASS",
789	            "—"
790	          ]
791	        ]
792	      }
793	    ],
794	    "figures": [],
795	    "analysis": "PASS with ratio=0.02 is the paper's 'trump card.' In rebuttal, when reviewers flag C5 failure and weak SOPBench: 'Our causal design with perturbation control provides the strongest evidence in the literature that ambiguity — not surface variation — drives safety violations. The measurement contribution stands independent of failure mode taxonomy validation.'\n\nPerturbation control is tier-invariant. Non-ambiguity surface changes (synonym substitution, clause reordering) produce Δ=-0.67pp (CI contains 0), vs ambiguity Δ=+34pp. Ratio 0.02 is well below the 0.15 PASS threshold. This is the paper's methodological crown jewel: no other agent safety study has comparable causal control. Under worst tier, perturbation control + judge calibration form the 'double anchor' — the binary effect is both (a) ambiguity-specific (not prompt brittleness) and (b) accurately measured. This combination is sufficient for a measurement contribution at EMNLP even without C5."
796	  },
797	  {
798	    "name": "sopbench_cross_benchmark",
799	    "description": "C1 replication on SOPBench Healthcare + Bank. 100 clause pairs × 2 conditions × 5 models = 1,000 episodes.",
800	    "results": {
801	      "total_episodes": 987,
802	      "episodes_dropped": 13,
803	      "c1_delta_pp_overall": 14.2,
804	      "c1_delta_gpt54": 18.4,
805	      "c1_delta_gpt41": 16.8,
806	      "c1_delta_deepseek": 15.0,
807	      "c1_delta_qwen3": 12.6,
808	      "c1_delta_claude": 8.2,
809	      "c1_p_gpt54": 0.003,
810	      "c1_p_gpt41": 0.008,
811	      "c1_p_deepseek": 0.015,
812	      "c1_p_qwen3": 0.061,
813	      "c1_p_claude": 0.093,
814	      "models_c1_significant": "3/5",
815	      "models_c1_nonsignificant": "2/5",
816	      "c2_type_rank_rho": 0.2,
817	      "c2_type_rank_p": 0.8,
818	      "healthcare_delta_pp": 16.1,
819	      "bank_delta_pp": 12.3
820	    },
821	    "tables": [
822	      {
823	        "title": "SOPBench C1 Replication by Model",
824	        "columns": [
825	          "Model",
826	          "Amb Rate",
827	          "Unamb Rate",
828	          "Delta pp",
829	          "p-value",
830	          "Replicates?"
831	        ],
832	        "rows": [
833	          [
834	            "gpt-5.4",
835	            "0.312",
836	            "0.128",
837	            "+18.4",
838	            "0.003",
839	            "Yes"
840	          ],
841	          [
842	            "gpt-4.1",
843	            "0.288",
844	            "0.120",
845	            "+16.8",
846	            "0.008",
847	            "Yes"
848	          ],
849	          [
850	            "deepseek",
851	            "0.298",
852	            "0.148",
853	            "+15.0",
854	            "0.015",
855	            "Yes"
856	          ],
857	          [
858	            "qwen3",
859	            "0.262",
860	            "0.136",
861	            "+12.6",
862	            "0.061",
863	            "No"
864	          ],
865	          [
866	            "claude",
867	            "0.194",
868	            "0.112",
869	            "+8.2",
870	            "0.093",
871	            "No"
872	          ]
873	        ]
874	      },
875	      {
876	        "title": "SOPBench vs tau2-bench Type Ranking (4 shared types)",
877	        "columns": [
878	          "tau2-bench Rank",
879	          "tau2-bench Type",
880	          "SOPBench Rank",
881	          "SOPBench Type"
882	        ],
883	        "rows": [
884	          [
885	            "1",
886	            "incompleteness (53.6%)",
887	            "1",
888	            "auth_scope (31.2%)"
889	          ],
890	          [
891	            "2",
892	            "lexical (42.8%)",
893	            "2",
894	            "incompleteness (28.4%)"
895	          ],
896	          [
897	            "3",
898	            "auth_scope (41.6%)",
899	            "3",
900	            "lexical (25.1%)"
901	          ],
902	          [
903	            "4",
904	            "cond_prec (36.8%)",
905	            "4",
906	            "cond_prec (21.1%)"
907	          ]
908	        ]
909	      },
910	      {
911	        "title": "SOPBench by Domain",
912	        "columns": [
913	          "Domain",
914	          "Amb Rate",
915	          "Unamb Rate",
916	          "Delta pp",
917	          "p-value"
918	        ],
919	        "rows": [
920	          [
921	            "Healthcare",
922	            "0.289",
923	            "0.128",
924	            "+16.1",
925	            "0.004"
926	          ],
927	          [
928	            "Bank",
929	            "0.253",
930	            "0.130",
931	            "+12.3",
932	            "0.031"
933	          ]
934	        ]
935	      }
936	    ],
937	    "figures": [],
938	    "analysis": "SOPBench weakness forces a major reframing. Under worst tier, the paper drops all cross-domain generalizability claims. SOPBench results go in appendix: 'Effect replicates directionally in 3/5 models on SOPBench (Healthcare + Bank) but with substantially attenuated magnitude (14.2pp vs 34.0pp) and inconsistent type ranking (ρ=0.20, n.s.), suggesting effect size depends on policy complexity and evaluation methodology. We frame τ²-bench scope (retail + airline) as an acknowledged limitation.' The rebuttal argument: 'Attenuation is expected when moving from LLM judge to rule-based verifier — the verifier captures a strict subset of violations. The directional replication in 3/5 models is consistent with a real but domain-modulated effect.'\n\nSOPBench C1 replication is WEAK — a defining feature of worst tier. Overall Δ=14.2pp is less than half the τ²-bench effect (+34pp). Only 3/5 models reach significance; Claude (Δ=8.2pp, p=0.093) and Qwen3 (Δ=12.6pp, p=0.061) fall short. Type ranking ρ=0.20 (p=0.80) shows NO correspondence with τ²-bench hierarchy. Multiple reinforcing causes: (1) SOPBench's rule-based verifier catches explicit rule violations only, missing nuanced safety violations that τ²-bench's LLM judge detects — ambiguity causes agents to act inappropriately without technically breaking any explicit SOPBench rule; (2) Healthcare/Bank SOPs are more procedurally structured (if-then-else decision trees) than retail/airline policies, reducing ambiguity surface area; (3) 100 clause pairs across 4 types give ~25 per type per domain — insufficient for stable per-type estimates; (4) type rankings depend on domain structure: auth_scope is more dangerous in banking (authorization is core) than in τ²-bench retail, reshuffling the hierarchy. The weak replication doesn't invalidate τ²-bench but prevents cross-domain generalizability claims."
939	  },
940	  {
941	    "name": "classifier_poc",
942	    "description": "DeBERTa-v3-large binary ambiguity detector, fine-tuned on 300 clause pairs, 5-fold CV.",
943	    "results": {
944	      "macro_f1": 0.55,
945	      "binary_f1": 0.78,
946	      "binary_fpr": 0.062,
947	      "best_type_f1_cp": 0.89,
948	      "worst_type_f1_incomp": 0.28,
949	      "per_type_f1_cp": 0.89,
950	      "per_type_f1_scopal": 0.71,
951	      "per_type_f1_coref": 0.62,
952	      "per_type_f1_auth": 0.51,
953	      "per_type_f1_lexical": 0.34,
954	      "per_type_f1_incomp": 0.28
955	    },
956	    "tables": [
957	      {
958	        "title": "DeBERTa Classifier Per-Type F1",
959	        "columns": [
960	          "Type",
961	          "Precision",
962	          "Recall",
963	          "F1"
964	        ],
965	        "rows": [
966	          [
967	            "conditional_precedence",
968	            "0.91",
969	            "0.87",
970	            "0.89"
971	          ],
972	          [
973	            "scopal",
974	            "0.74",
975	            "0.68",
976	            "0.71"
977	          ],
978	          [
979	            "coreferential",
980	            "0.65",
981	            "0.59",
982	            "0.62"
983	          ],
984	          [
985	            "authorization_scope",
986	            "0.54",
987	            "0.48",
988	            "0.51"
989	          ],
990	          [
991	            "lexical",
992	            "0.38",
993	            "0.31",
994	            "0.34"
995	          ],
996	          [
997	            "incompleteness",
998	            "0.32",
999	            "0.25",
1000	            "0.28"
1001	          ],
1002	          [
1003	            "Binary (any type)",
1004	            "0.82",
1005	            "0.74",
1006	            "0.78"
1007	          ]
1008	        ]
1009	      }
1010	    ],
1011	    "figures": [],
1012	    "analysis": "Classifier PoC is P2 and doesn't affect paper positioning. Under worst tier, it's an appendix footnote. Its per-type difficulty gradient (CP easy → incomp hard) independently corroborates that type boundaries are genuinely fuzzy, lending credibility to the 'honest assessment' of taxonomy limitations.\n\nBinary detection (F1=0.78) is serviceable but per-type classification (macro F1=0.55) is mediocre. CP is easiest (explicit conflicting rules have strong lexical markers — 'however,' 'notwithstanding'). Incompleteness is hardest (absence of information has no positive signal — the classifier must learn what's MISSING, a fundamentally harder task). Under worst tier, the classifier's type-level struggle mirrors the κ re-annotation failure — both reflect that fine-grained type distinctions are harder than binary ambiguity detection. The classifier is relegated to appendix: 'Preliminary DeBERTa PoC achieves F1=0.78 for binary ambiguity screening. Per-type classification (F1=0.55) remains challenging, consistent with type boundary issues identified in our annotation study.'"
1013	  },
1014	  {
1015	    "name": "kappa_reannotation_failure",
1016	    "description": "Human re-annotation of 25 LLM-coded failure mode traces using improved codebook. THE defining worst-tier experiment.",
1017	    "results": {
1018	      "n_traces_reannotated": 25,
1019	      "kappa_human_human": 0.48,
1020	      "kappa_human_llm_pooled": 0.22,
1021	      "human_llm_dominant_mode_agreement": "2/6",
1022	      "types_with_agreement": [
1023	        "scopal",
1024	        "conditional_precedence"
1025	      ],
1026	      "types_with_disagreement": [
1027	        "auth_scope",
1028	        "incompleteness",
1029	        "lexical",
1030	        "coreferential"
1031	      ],
1032	      "auth_scope_human_dominant": "scope_misapplication",
1033	      "auth_scope_llm_dominant": "unauthorized_escalation",
1034	      "incompleteness_human_dominant": "inappropriate_action",
1035	      "incompleteness_llm_dominant": "assumption_based_action",
1036	      "systematic_llm_bias_types": 2
1037	    },
1038	    "tables": [
1039	      {
1040	        "title": "Human vs LLM Dominant Failure Mode by Type",
1041	        "columns": [
1042	          "Type",
1043	          "LLM Dominant",
1044	          "LLM %",
1045	          "Human Dominant",
1046	          "Human %",
1047	          "Agree?"
1048	        ],
1049	        "rows": [
1050	          [
1051	            "auth_scope",
1052	            "unauthorized_escalation",
1053	            "78%",
1054	            "scope_misapplication",
1055	            "52%",
1056	            "No"
1057	          ],
1058	          [
1059	            "incompleteness",
1060	            "assumption_based_action",
1061	            "64%",
1062	            "inappropriate_action",
1063	            "45%",
1064	            "No"
1065	          ],
1066	          [
1067	            "scopal",
1068	            "scope_misapplication",
1069	            "75%",
1070	            "scope_misapplication",
1071	            "68%",
1072	            "Yes"
1073	          ],
1074	          [
1075	            "lexical",
1076	            "assumption_based_action",
1077	            "62%",
1078	            "assumption_based_action",
1079	            "41%",
1080	            "No"
1081	          ],
1082	          [
1083	            "cond_prec",
1084	            "arbitrary_rule_selection",
1085	            "34%",
1086	            "arbitrary_rule_selection",
1087	            "42%",
1088	            "Yes"
1089	          ],
1090	          [
1091	            "coreferential",
1092	            "scope_misapplication",
1093	            "41%",
1094	            "assumption_based_action",
1095	            "36%",
1096	            "No"
1097	          ]
1098	        ]
1099	      },
1100	      {
1101	        "title": "kappa Agreement Summary",
1102	        "columns": [
1103	          "Comparison",
1104	          "Overall kappa",
1105	          "Interpretation"
1106	        ],
1107	        "rows": [
1108	          [
1109	            "Human-Human",
1110	            "0.48",
1111	            "Moderate — codebook boundaries inherently fuzzy"
1112	          ],
1113	          [
1114	            "Human-LLM (pooled)",
1115	            "0.22",
1116	            "Poor — systematic LLM keyword bias"
1117	          ],
1118	          [
1119	            "LLM-LLM (plan_005)",
1120	            "0.52",
1121	            "Moderate — inflated by shared bias"
1122	          ]
1123	        ]
1124	      },
1125	      {
1126	        "title": "Systematic LLM Coding Biases Identified",
1127	        "columns": [
1128	          "Type",
1129	          "LLM Bias Pattern",
1130	          "Human Finding",
1131	          "Impact"
1132	        ],
1133	        "rows": [
1134	          [
1135	            "auth_scope",
1136	            "keyword 'unauthorized' -> unauthorized_escalation",
1137	            "40% are scope_misapplication",
1138	            "C5 auth_scope mechanism claim invalid"
1139	          ],
1140	          [
1141	            "incompleteness",
1142	            "keyword 'assumed' -> assumption_based_action",
1143	            "30% are inappropriate_action",
1144	            "C5 incompleteness mechanism weakened"
1145	          ],
1146	          [
1147	            "lexical",
1148	            "agreement inflated by kappa paradox",
1149	            "true diversity higher than coded",
1150	            "fine-grained % unreliable"
1151	          ],
1152	          [
1153	            "coreferential",
1154	            "coded as scope_misapplication plurality",
1155	            "flat distribution, no clear dominant",
1156	            "C5 coref pattern overclaimed"
1157	          ]
1158	        ]
1159	      }
1160	    ],
1161	    "figures": [],
1162	    "analysis": "κ=0.22 is the worst-tier trigger that cascades through the paper. Consequences: (1) C5 failure mode taxonomy is invalidated for fine-grained claims — must be demoted to appendix as 'exploratory automated analysis.' (2) 'Ambiguity Blindness' loses named-contribution status but survives as a Discussion paragraph (binary observation, not dependent on failure mode coding). (3) Contribution (3) downgrades from 'type-specific failure mode taxonomy' to 'benchmark and protocol release.' (4) Discussion shifts from mechanism ('why models fail differently') to implication ('what the differential vulnerability means for deployment'). (5) The paper's two remaining validated contributions are C1 causal quantification and C4 model×type interaction — both purely quantitative. The human-human κ=0.48 provides a partial defense: 'The failure mode categories themselves have inherently fuzzy boundaries; this is a limitation of trace-based mechanism inference, not just LLM coding quality. Future work with chain-of-thought access may enable more reliable mechanism classification.' Expected reviewer reaction: 'The authors are commendably honest about this limitation, but contribution (3) as stated in the abstract is not supported by the validation data.'\n\nκ=0.22 (poor) exposes two distinct and reinforcing problems. First, LLM coding bias: LLM coders systematically miscategorize by surface keyword matching. For auth_scope, traces containing 'exceeded authority' or 'unauthorized' are coded as unauthorized_escalation regardless of whether the agent actively chose to exceed boundaries (true escalation) or passively misread the permission scope (scope misapplication). Human coders, reading the full reasoning chain, find ~40% of auth_scope 'unauthorized_escalation' traces are actually scope_misapplication — the agent didn't know it was exceeding authority. For incompleteness, LLMs code 'assumption_based_action' when the trace shows gap-filling behavior, but humans often judge these as 'inappropriate_action' — the distinction between 'filling a gap' and 'acting wrongly' is interpretive, and humans apply stricter criteria. Second, codebook imprecision: human-human κ=0.48 (moderate) reveals that the coding scheme's category boundaries are inherently fuzzy. The improved codebook (collapsed spurious-compliance/structural-misparse) was insufficient — the remaining categories (unauthorized_escalation ↔ scope_misapplication, assumption_based_action ↔ inappropriate_action) still overlap when applied to real traces. Only scopal (clear scope_misapplication with unambiguous behavioral signature) and CP (explicit rule conflict → arbitrary_rule_selection with detectably different pattern) survive because their failure modes have distinct, objectively identifiable behavioral markers. The LLM-LLM κ=0.52 from plan_005 was artificially inflated by shared biases — both coders use the same keyword heuristic, producing correlated errors that inflate agreement. The root cause is that agent trace text doesn't contain sufficient information to distinguish between failure mechanisms (intent-level distinction) — you'd need the agent's internal chain-of-thought, which is only partially revealed."
1163	  }
1164	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "666a35f8-86d8-4152-b7b1-5b11c90aadb8",
  "isSidechain": false,
  "promptId": "128f9fd8-c2a5-4ade-82e9-ac2ac23ec257",
  "type": "user",
  "uuid": "c459d745-9b7e-4711-a575-3f332e3690ab",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"full_study_clause_generation\",\n    \"description\": \"Generate 140 new clauses, validate all 300 pairs for cross-type balance and quality.\",\n    \"results\": {\n      \"clauses_generated\": 140,\n      \"total_validated\": 300,\n      \"quality_pass_rate\": 0.93,\n      \"boundary_overlap_cases\": 8,\n      \"mean_disambiguation_tokens_spec\": 35.2,\n      \"mean_disambiguation_tokens_ling\": 18.4,\n      \"revision_needed\": 21\n    },\n    \"tables\": [\n      {\n        \"title\": \"Clause Generation Summary by Type\",\n        \"columns\": [\n          \"Type\",\n          \"Existing\",\n          \"New\",\n          \"Total\",\n          \"Pass\",\n          \"Boundary\"\n        ],\n        \"rows\": [\n          [\n            \"authorization_scope\",\n            \"0\",\n            \"50\",\n            \"50\",\n            \"46\",\n            \"3\"\n          ],\n          [\n            \"conditional_precedence\",\n            \"50\",\n            \"0\",\n            \"50\",\n            \"49\",\n            \"0\"\n          ],\n          [\n            \"incompleteness\",\n            \"30\",\n            \"20\",\n            \"50\",\n            \"47\",\n            \"2\"\n          ],\n          [\n            \"lexical\",\n            \"30\",\n            \"20\",\n            \"50\",\n            \"48\",\n            \"2\"\n          ],\n          [\n            \"coreferential\",\n            \"0\",\n            \"50\",\n            \"50\",\n            \"45\",\n            \"1\"\n          ],\n          [\n            \"scopal\",\n            \"50\",\n            \"0\",\n            \"50\",\n            \"49\",\n            \"0\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Clause generation succeeds. 8/300 (2.7%) boundary overlap is within tolerance, but under worst tier these become evidence of taxonomy imprecision when combined with κ=0.22 re-annotation failure. Token-length asymmetry (35 vs 18 tokens) contributes to plan_007's 2/4 significant KS tests.\\n\\nClause generation is upstream of worst-tier failures and proceeds normally. 93% pass quality check. 8 clauses sit on type boundaries (5 auth_scope↔incompleteness, 3 coreferential↔lexical) — individually acceptable, but these boundary cases seed downstream κ re-annotation disagreement when human coders classify 4/8 into different types. Spec-layer disambiguation requires ~35 tokens vs ling-layer ~18, a systematic asymmetry inherent to matched-pair design that plan_007 will flag.\"\n  },\n  {\n    \"name\": \"new_type_mini_pilot\",\n    \"description\": \"Mini-pilot: 5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes for coreferential + auth_scope.\",\n    \"results\": {\n      \"total_episodes\": 20,\n      \"auth_scope_amb_violation_rate\": 0.4,\n      \"auth_scope_unamb_violation_rate\": 0.1,\n      \"coref_amb_violation_rate\": 0.2,\n      \"coref_unamb_violation_rate\": 0.0,\n      \"pilot_verdict\": \"PASS\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Pilot passes and green-lights full study. Under worst tier, its limited N is a non-factor — the pilot's purpose (binary effect validation) is orthogonal to the failure mode coding problem that drives worst-tier collapse.\\n\\nBoth types trigger violations under ambiguity, clearing pilot thresholds. Auth_scope at 40% (2/5) seems strong; coreferential at 20% (1/5) is low but non-zero. N=5 per type is designed to catch gross failures only — it cannot detect the failure mode coding problems that surface at scale. In hindsight, the pilot validated binary effects but left untested the question of whether auth_scope's failure modes are reliably classifiable, which is where worst tier ultimately collapses.\"\n  },\n  {\n    \"name\": \"full_study_api\",\n    \"description\": \"300 clauses × 2 conditions × 3 API models = 1,800 episodes with cross-judge evaluation.\",\n    \"results\": {\n      \"total_episodes\": 1800,\n      \"c1_delta_pp_aggregate\": 34.0,\n      \"c1_mcnemar_or\": 15.1,\n      \"c1_or_ci\": [\n        10.78,\n        21.17\n      ],\n      \"c1_p\": \"<0.0001\",\n      \"c1_delta_gpt54\": 38.3,\n      \"c1_delta_gpt41\": 34.7,\n      \"c1_delta_claude\": 25.7,\n      \"cross_judge_kappa\": 0.69,\n      \"amb_violation_rate_pooled\": 0.41,\n      \"unamb_violation_rate_pooled\": 0.045\n    },\n    \"tables\": [\n      {\n        \"title\": \"C1 Binary Effect by API Model\",\n        \"columns\": [\n          \"Model\",\n          \"Amb Rate\",\n          \"Unamb Rate\",\n          \"Delta pp\",\n          \"McNemar p\",\n          \"Judge\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            \"0.410\",\n            \"0.027\",\n            \"+38.3\",\n            \"<1e-17\",\n            \"gpt-4.1\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"0.407\",\n            \"0.060\",\n            \"+34.7\",\n            \"<1e-17\",\n            \"gpt-5.4\"\n          ],\n          [\n            \"claude-sonnet-4-6\",\n            \"0.303\",\n            \"0.047\",\n            \"+25.7\",\n            \"<1e-17\",\n            \"gpt-5.4\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"C1 is the paper's unassailable result in all tiers. +34pp with perturbation control is the strongest causal evidence for ambiguity→safety violations in the literature. Under worst tier, this anchors the reframed 'measurement paper' positioning.\\n\\nData collection succeeds. Binary violation effect is massive across all 3 API models with no exceptions. Cross-judge κ=0.69 (substantial) validates the violation measurement chain. These results are tier-invariant — the +34pp effect and OR=15.1 hold regardless of downstream κ re-annotation or SOPBench outcomes. Under worst tier, these numbers become the paper's anchor: quantitatively unassailable, but without C5 qualitative story they constitute a measurement finding rather than a theoretical contribution.\"\n  },\n  {\n    \"name\": \"full_study_opensource\",\n    \"description\": \"300 clauses × 2 conditions × 2 open-source models (qwen3-235b, deepseek-v3) via OpenRouter = 1,200 episodes.\",\n    \"results\": {\n      \"total_episodes\": 1197,\n      \"c1_delta_qwen3\": 32.4,\n      \"c1_delta_deepseek\": 39.0,\n      \"qwen3_amb_rate\": 0.431,\n      \"deepseek_amb_rate\": 0.497,\n      \"deepseek_type_chi2\": 6.31,\n      \"deepseek_type_p\": 0.277,\n      \"deepseek_type_v\": 0.14,\n      \"qwen3_type_chi2\": 15.89,\n      \"qwen3_type_p\": 0.007,\n      \"api_timeouts\": 3\n    },\n    \"tables\": [\n      {\n        \"title\": \"Open-Source Violation Rates by Type (Ambiguous)\",\n        \"columns\": [\n          \"Type\",\n          \"Qwen3\",\n          \"DeepSeek\",\n          \"Range\"\n        ],\n        \"rows\": [\n          [\n            \"authorization_scope\",\n            \"26%\",\n            \"60%\",\n            \"34pp\"\n          ],\n          [\n            \"conditional_precedence\",\n            \"40%\",\n            \"38%\",\n            \"2pp\"\n          ],\n          [\n            \"incompleteness\",\n            \"62%\",\n            \"54%\",\n            \"8pp\"\n          ],\n          [\n            \"lexical\",\n            \"52%\",\n            \"54%\",\n            \"2pp\"\n          ],\n          [\n            \"coreferential\",\n            \"42%\",\n            \"44%\",\n            \"2pp\"\n          ],\n          [\n            \"scopal\",\n            \"37%\",\n            \"48%\",\n            \"11pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DeepSeek's uniformly high vulnerability (no type χ² significance) weakens C4 by showing 1/5 models has no type-specific profile. Under worst tier, a reviewer argues: 'The model×type interaction is driven by 3 models with targeted safety training — it reflects training decisions, not an intrinsic property of ambiguity type.'\\n\\nBoth open-source models confirm C1 universality. DeepSeek shows the highest overall vulnerability (49.7%) with near-uniform rates across all 6 types (χ²=6.31, p=0.277) — no type differentiation. This uniformity means DeepSeek doesn't contribute to C4's model×type interaction; it has no type-specific vulnerability profile. Under worst tier, DeepSeek's flat profile feeds the 'incremental' narrative: type differentiation may be an artifact of targeted safety training (GPT, Claude) rather than a fundamental property of ambiguity types. Qwen3 shows moderate differentiation (χ²=15.89, p=0.007) partially rescuing C4 as cross-architecture.\"\n  },\n  {\n    \"name\": \"full_study_analysis\",\n    \"description\": \"Statistical analysis of 2,997 episodes: C1–C4, TOST, power, info delta, inter-model agreement.\",\n    \"results\": {\n      \"c1_or\": 15.1,\n      \"c1_or_ci\": [\n        10.78,\n        21.17\n      ],\n      \"c1_bootstrap_ci_pp\": [\n        31.2,\n        36.9\n      ],\n      \"c2_omnibus_chi2\": 28.02,\n      \"c2_p\": 3.6e-05,\n      \"c2_v\": 0.137,\n      \"c2_power\": 0.993,\n      \"c2_mde\": 0.093,\n      \"c3_delta_pp\": 6.08,\n      \"c3_p_aggregate\": 0.017,\n      \"c3_within_judge_gpt54_p\": 0.059,\n      \"c3_within_judge_gpt41_p\": 0.157,\n      \"c4_model_chi2\": 31.02,\n      \"c4_model_p\": 3e-06,\n      \"c4_model_v\": 0.102,\n      \"tost_15pp_equivalent\": \"8/15\",\n      \"tost_10pp_equivalent\": \"4/15\",\n      \"logistic_condition_coef\": 2.278,\n      \"logistic_condition_z\": 19.65,\n      \"logistic_token_delta_coef\": 0.022,\n      \"logistic_token_delta_p\": 0.0005,\n      \"fleiss_kappa_inter_model\": 0.384,\n      \"systematic_nocuity_rate\": 0.27\n    },\n    \"tables\": [\n      {\n        \"title\": \"C2 Type Hierarchy (Ambiguous Only, 5-Model Pooled)\",\n        \"columns\": [\n          \"Type\",\n          \"Violation Rate\",\n          \"95% CI\",\n          \"Tier\"\n        ],\n        \"rows\": [\n          [\n            \"incompleteness\",\n            \"53.6%\",\n            \"[48.2, 59.0]\",\n            \"High\"\n          ],\n          [\n            \"lexical\",\n            \"42.8%\",\n            \"[37.4, 48.2]\",\n            \"Mid\"\n          ],\n          [\n            \"authorization_scope\",\n            \"41.6%\",\n            \"[36.2, 47.0]\",\n            \"Mid\"\n          ],\n          [\n            \"scopal\",\n            \"39.4%\",\n            \"[34.1, 44.7]\",\n            \"Mid\"\n          ],\n          [\n            \"conditional_precedence\",\n            \"36.8%\",\n            \"[31.5, 42.1]\",\n            \"Mid\"\n          ],\n          [\n            \"coreferential\",\n            \"31.6%\",\n            \"[26.5, 36.7]\",\n            \"Low\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"C3 Layer Effect — Within-Judge Fragility\",\n        \"columns\": [\n          \"Judge Group\",\n          \"Spec Rate\",\n          \"Ling Rate\",\n          \"Delta pp\",\n          \"p-value\",\n          \"Verdict\"\n        ],\n        \"rows\": [\n          [\n            \"Pooled\",\n            \"44.0%\",\n            \"37.9%\",\n            \"+6.08\",\n            \"0.017\",\n            \"Significant\"\n          ],\n          [\n            \"gpt-4.1 judged\",\n            \"48.4%\",\n            \"40.4%\",\n            \"+8.0\",\n            \"0.059\",\n            \"Marginal\"\n          ],\n          [\n            \"gpt-5.4 judged\",\n            \"41.0%\",\n            \"36.2%\",\n            \"+4.8\",\n            \"0.157\",\n            \"Not significant\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"C4 Model × Type Interaction (Violation Rates, Ambiguous)\",\n        \"columns\": [\n          \"Type\",\n          \"GPT-5.4\",\n          \"GPT-4.1\",\n          \"Claude\",\n          \"Qwen3\",\n          \"DeepSeek\",\n          \"Range\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"64%\",\n            \"46%\",\n            \"12%\",\n            \"26%\",\n            \"60%\",\n            \"52pp\"\n          ],\n          [\n            \"incompleteness\",\n            \"46%\",\n            \"58%\",\n            \"48%\",\n            \"62%\",\n            \"54%\",\n            \"16pp\"\n          ],\n          [\n            \"lexical\",\n            \"42%\",\n            \"34%\",\n            \"32%\",\n            \"52%\",\n            \"54%\",\n            \"22pp\"\n          ],\n          [\n            \"coreferential\",\n            \"18%\",\n            \"32%\",\n            \"22%\",\n            \"42%\",\n            \"44%\",\n            \"26pp\"\n          ],\n          [\n            \"scopal\",\n            \"42%\",\n            \"38%\",\n            \"32%\",\n            \"37%\",\n            \"48%\",\n            \"16pp\"\n          ],\n          [\n            \"cond_prec\",\n            \"34%\",\n            \"36%\",\n            \"36%\",\n            \"40%\",\n            \"38%\",\n            \"6pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The quantitative core is rock-solid but lacks interpretive depth without C5. Under worst tier, the 'numbers without narrative' problem is acute: C2's V=0.137 is significant but small, C3 is fragile, and C4's 52pp auth_scope range — while striking — is concentrated in one type. The 27% systematic nocuity finding (all models converge on same wrong answer) would be the Discussion centerpiece IF C5 could explain WHY, but without validated failure modes it remains a descriptive observation. Reviewers see a comprehensive measurement study that stops short of mechanistic explanation.\\n\\nAll quantitative results are tier-invariant. C1 is overwhelming (OR=15.1). C4's model×type interaction is statistically significant and novel. However, under worst tier reviewers evaluate these numbers without C5's explanatory scaffolding. V=0.137 for C2 falls below the conventional 0.20 medium-effect threshold — invites 'small effect' criticism. C3 dissolves under within-judge analysis (gpt-5.4 group p=0.059, gpt-4.1 group p=0.157): pooled significance may reflect between-judge variance, not a real layer effect. TOST shows 4/15 type pairs equivalent at ±10pp — types ARE differentiable but the differences are modest. A skeptical reviewer sees: 'confirmed the obvious (ambiguity is bad), found a small type effect (V=0.137), showed models differ — well-executed but incremental.' The logistic regression's condition_amb coef=2.278 dominating all predictors is strong evidence but 'expected, not surprising.' Systematic nocuity (27% of episodes: all models converge on same wrong interpretation) is theoretically interesting but requires C5 to explain WHY.\"\n  },\n  {\n    \"name\": \"error_analysis\",\n    \"description\": \"Qualitative analysis of violation traces: failure mode classification, cross-type distribution, ambiguity awareness.\",\n    \"results\": {\n      \"traces_coded_gpt54\": 123,\n      \"traces_coded_gpt41\": 122,\n      \"total_violations_coded\": 614,\n      \"inter_coder_kappa_4cat\": 0.517,\n      \"percent_agreement\": 0.656,\n      \"types_unanimous_dominant_fm\": \"3/6\",\n      \"types_majority_dominant_fm\": \"6/6\",\n      \"disambiguation_awareness_gpt54\": 0.041,\n      \"disambiguation_awareness_gpt41\": 0.107,\n      \"surface_adoption_overall\": 0.88,\n      \"escalate_to_user_rate\": 0.008,\n      \"auth_scope_inter_coder_kappa\": 0.054,\n      \"incompleteness_inter_coder_kappa\": 0.233,\n      \"lexical_inter_coder_kappa\": 0.0,\n      \"scopal_percent_agreement\": 1.0\n    },\n    \"tables\": [\n      {\n        \"title\": \"LLM-Coded Dominant Failure Mode by Type\",\n        \"columns\": [\n          \"Type\",\n          \"GPT-5.4 Dominant\",\n          \"Rate\",\n          \"GPT-4.1 Dominant\",\n          \"Rate\",\n          \"Agree?\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"unauthorized_escalation\",\n            \"72%\",\n            \"unauthorized_escalation\",\n            \"83%\",\n            \"Yes\"\n          ],\n          [\n            \"incompleteness\",\n            \"assumption_based_action\",\n            \"61%\",\n            \"assumption_based_action\",\n            \"66%\",\n            \"Yes\"\n          ],\n          [\n            \"scopal\",\n            \"scope_misapplication\",\n            \"76%\",\n            \"scope_misapplication\",\n            \"74%\",\n            \"Yes\"\n          ],\n          [\n            \"lexical\",\n            \"assumption_based_action\",\n            \"71%\",\n            \"assumption_based_action\",\n            \"53%\",\n            \"Partial\"\n          ],\n          [\n            \"cond_prec\",\n            \"scope_misapplication\",\n            \"41%\",\n            \"arbitrary_rule_selection\",\n            \"28%\",\n            \"No\"\n          ],\n          [\n            \"coreferential\",\n            \"scope_misapplication\",\n            \"44%\",\n            \"assumption_based_action\",\n            \"38%\",\n            \"No\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Per-Type Inter-Coder Agreement\",\n        \"columns\": [\n          \"Type\",\n          \"N Traces\",\n          \"% Agree\",\n          \"Cohen kappa\",\n          \"Issue\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"42\",\n            \"54%\",\n            \"0.054\",\n            \"keyword-driven label, not mechanism\"\n          ],\n          [\n            \"incompleteness\",\n            \"56\",\n            \"62%\",\n            \"0.233\",\n            \"fuzzy boundary with inappropriate_action\"\n          ],\n          [\n            \"lexical\",\n            \"38\",\n            \"92%\",\n            \"0.000\",\n            \"kappa paradox\"\n          ],\n          [\n            \"scopal\",\n            \"36\",\n            \"100%\",\n            \"undefined\",\n            \"perfect agreement, undefined kappa\"\n          ],\n          [\n            \"cond_prec\",\n            \"42\",\n            \"58%\",\n            \"0.312\",\n            \"scope_misapplication vs arbitrary_rule_selection\"\n          ],\n          [\n            \"coreferential\",\n            \"31\",\n            \"48%\",\n            \"0.184\",\n            \"flat distribution, no dominant mode\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Error analysis is the CRITICAL worst-tier failure surface. The LLM-coded results appear publishable in isolation (6/6 majority agreement, Ambiguity Blindness quantified, layer mechanism documented). But κ re-annotation will expose that the type-specific failure signatures — the core of C5 — are an artifact of LLM keyword matching. The unauthorized_escalation label for auth_scope reflects the coders detecting 'agent exceeded authority' rather than distinguishing HOW (active escalation vs passive misread). Ambiguity Blindness (<5-11%) and surface adoption (>88%) survive because they don't require fine-grained mode classification. Under worst-tier reframing, these two binary findings move to Discussion; the rest of C5 moves to appendix with 'automated coding, κ=0.22 with human re-annotation' caveat.\\n\\nLLM-coded error analysis produces an internally consistent but artificially clean picture. Both GPT coders share similar linguistic biases from pretraining, making their agreement (3/6 dominant mode, κ=0.52) an artifact of shared surface-feature heuristics rather than robust coding. Auth_scope κ=0.054 (near chance) because both coders assign >80% unauthorized_escalation — they agree on the label but disagree on specific traces, and human re-annotation will show the label itself is wrong for ~40% of cases (should be scope_misapplication). Lexical κ=0.0 is a kappa paradox (91.7% agreement but chance-corrected near zero). Ambiguity Blindness (4.1–10.7%) survives worst tier because it's based on text search for explicit acknowledgment — a binary signal immune to failure mode coding bias. Surface adoption >88% is similarly robust. The key worst-tier dynamic: plan_005 results LOOK usable until kappa re-annotation reveals the LLM-LLM agreement is systematically biased.\"\n  },\n  {\n    \"name\": \"reliability_test\",\n    \"description\": \"Test-retest: 30 clauses × 3 replicates × 2 conditions × 2 models = 360 episodes. ICC for per-clause violation rates.\",\n    \"results\": {\n      \"total_episodes\": 360,\n      \"icc_overall\": 0.919,\n      \"icc_binary\": 0.847,\n      \"icc_gpt54\": 0.921,\n      \"icc_gpt41\": 0.918,\n      \"icc_scopal\": 0.989,\n      \"icc_lexical\": 0.981,\n      \"icc_coref\": 0.976,\n      \"icc_auth_scope\": 0.857,\n      \"icc_cond_prec\": 0.856,\n      \"icc_incompleteness\": 0.807\n    },\n    \"tables\": [\n      {\n        \"title\": \"ICC by Type and Layer\",\n        \"columns\": [\n          \"Type\",\n          \"Layer\",\n          \"ICC\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"scopal\",\n            \"Linguistic\",\n            \"0.989\",\n            \"[0.97, 0.99]\"\n          ],\n          [\n            \"lexical\",\n            \"Linguistic\",\n            \"0.981\",\n            \"[0.96, 0.99]\"\n          ],\n          [\n            \"coreferential\",\n            \"Linguistic\",\n            \"0.976\",\n            \"[0.95, 0.99]\"\n          ],\n          [\n            \"auth_scope\",\n            \"Specification\",\n            \"0.857\",\n            \"[0.74, 0.93]\"\n          ],\n          [\n            \"cond_prec\",\n            \"Specification\",\n            \"0.856\",\n            \"[0.74, 0.93]\"\n          ],\n          [\n            \"incompleteness\",\n            \"Specification\",\n            \"0.807\",\n            \"[0.67, 0.90]\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Reliability is a bright spot — ICC=0.919 means the measurement infrastructure is sound. Under worst tier, this partially offsets the C5 collapse: violation RATES are reliable even if failure MODE labels are not. The spec/ling ICC gap (0.83 vs 0.98 mean) is convergent evidence for the Disambiguation Channel Framework but remains observational without C5 mechanism.\\n\\nTest-retest measures violation rate reproducibility, not failure mode coding — so it's tier-invariant. ICC=0.919 (excellent) confirms per-clause rates are stable across independent runs. The spec/ling ICC pattern (ling 0.976–0.989 vs spec 0.807–0.857) reflects real behavioral variance: spec-layer types force agents to guess without disambiguation channels, producing less deterministic outcomes on repeat. This finding actually SUPPORTS the Disambiguation Channel Framework, but without C5 validation it remains purely descriptive. Under worst tier, the per-type ICC variability adds nuance to C3 fragility — spec-layer types are both more dangerous AND less reproducible.\"\n  },\n  {\n    \"name\": \"realism_validation\",\n    \"description\": \"KS tests comparing synthetic clauses vs DRIP-R natural ambiguities on 4 linguistic properties.\",\n    \"results\": {\n      \"ks_sentence_length_p\": 0.028,\n      \"ks_flesch_kincaid_p\": 0.112,\n      \"ks_parse_depth_p\": 0.039,\n      \"ks_ttr_p\": 0.234,\n      \"significant_metrics\": \"2/4\",\n      \"mean_length_synthetic\": 31.4,\n      \"mean_length_drip_r\": 26.1,\n      \"mean_parse_depth_synthetic\": 4.8,\n      \"mean_parse_depth_drip_r\": 4.1\n    },\n    \"tables\": [\n      {\n        \"title\": \"Realism Validation: Synthetic vs DRIP-R\",\n        \"columns\": [\n          \"Metric\",\n          \"Synthetic\",\n          \"DRIP-R\",\n          \"KS Stat\",\n          \"p-value\",\n          \"Sig?\"\n        ],\n        \"rows\": [\n          [\n            \"Sentence length\",\n            \"31.4\",\n            \"26.1\",\n            \"0.187\",\n            \"0.028\",\n            \"Yes\"\n          ],\n          [\n            \"Flesch-Kincaid\",\n            \"12.8\",\n            \"12.2\",\n            \"0.112\",\n            \"0.112\",\n            \"No\"\n          ],\n          [\n            \"Parse depth\",\n            \"4.8\",\n            \"4.1\",\n            \"0.173\",\n            \"0.039\",\n            \"Yes\"\n          ],\n          [\n            \"Type-token ratio\",\n            \"0.71\",\n            \"0.73\",\n            \"0.089\",\n            \"0.234\",\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Mixed realism is a methodological footnote in stronger tiers but becomes ammunition under worst tier. Reviewers combine it with other weaknesses: 'The synthetic clauses are detectably different from natural ambiguity (2/4 KS significant), the failure mode taxonomy doesn't survive human validation (κ=0.22), and the effect doesn't robustly transfer to SOPBench — how much of this is about real-world policy ambiguity vs lab artifacts?' The rebuttal leans on perturbation control.\\n\\n2/4 KS tests reject null: synthetic clauses are ~5 tokens longer (31.4 vs 26.1) and ~0.7 levels deeper in parse tree. This is inherent to matched-pair design — unambiguous variants must add explicit conditions (e.g., 'standard items only') to disambiguate, making clause pairs systematically longer and more complex than naturally occurring ambiguous clauses. Readability (Flesch-Kincaid) and lexical diversity (TTR) are not significantly different, showing linguistic naturalness on those dimensions. Under worst tier, the 2/4 significant KS tests compound with C5 failure + weak SOPBench into a 'three-strike' validity concern: synthetic artifacts + unreliable coding + weak cross-domain. The defense is that perturbation control (Δ_perturb ≈ 0) provides stronger causal validity than distributional similarity.\"\n  },\n  {\n    \"name\": \"judge_calibration\",\n    \"description\": \"LLM-as-judge validation: 100 stratified episodes, 2 human annotators, agreement against human ground truth.\",\n    \"results\": {\n      \"n_episodes\": 100,\n      \"human_inter_annotator_kappa\": 0.762,\n      \"human_llm_binary_kappa\": 0.74,\n      \"human_llm_pooled_kappa_weighted\": 0.807,\n      \"cross_judge_kappa_weighted\": 0.685,\n      \"cross_judge_exact_agreement\": 0.76,\n      \"no_same_family_bias\": true,\n      \"ranking_preservation_rho\": 0.7\n    },\n    \"tables\": [\n      {\n        \"title\": \"Judge Calibration Summary\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"Threshold\",\n          \"Verdict\"\n        ],\n        \"rows\": [\n          [\n            \"Human inter-annotator κ\",\n            \"0.762\",\n            \">=0.75\",\n            \"PASS\"\n          ],\n          [\n            \"Human-LLM pooled κ (weighted)\",\n            \"0.807\",\n            \">=0.70\",\n            \"PASS\"\n          ],\n          [\n            \"Human-LLM binary κ\",\n            \"0.740\",\n            \">=0.70\",\n            \"PASS\"\n          ],\n          [\n            \"Cross-judge κ (weighted)\",\n            \"0.685\",\n            \">=0.60\",\n            \"PASS\"\n          ],\n          [\n            \"Same-family bias\",\n            \"None detected\",\n            \"None\",\n            \"PASS\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Plan_009's success is crucial for worst-tier survival: it proves C1's +34pp is measured accurately, insulating the quantitative core from C5's failure. Without plan_009, worst tier would be catastrophic (measurement AND interpretation both questioned). With it, the paper retains its measurement contribution.\\n\\nJudge calibration validates VIOLATION classification (binary + severity), NOT failure mode coding. Human-LLM κ=0.807 (substantial) confirms the measurement chain for C1/C2/C4 is trustworthy. This creates an ironic asymmetry defining worst tier: violation COUNTS are validated (κ=0.807) but failure MODE labels are not (κ=0.22 in re-annotation). The judge can reliably determine 'this is a violation' but not 'this violation is an unauthorized_escalation vs scope_misapplication.' Cross-judge validation (Fleiss κ=0.717, no same-family bias, ρ≥0.70) further confirms measurement integrity. Under worst tier, plan_009's success is a STRENGTH — it rules out the attack that 'the entire measurement chain is unreliable,' narrowing the failure to the qualitative analysis layer (C5) specifically.\"\n  },\n  {\n    \"name\": \"perturbation_control\",\n    \"description\": \"Non-ambiguity perturbation arm: 30 clause pairs with synonym/reorder changes, 120+ episodes.\",\n    \"results\": {\n      \"total_episodes\": 300,\n      \"delta_perturb_pp\": -0.67,\n      \"ci_95_bootstrap\": [\n        -8.0,\n        6.67\n      ],\n      \"ci_contains_zero\": true,\n      \"ambiguity_delta_pp\": 34.0,\n      \"ratio\": 0.02,\n      \"verdict\": \"PASS\",\n      \"mcnemar_p\": 1.0\n    },\n    \"tables\": [\n      {\n        \"title\": \"Perturbation Control Verdict\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"PASS Threshold\"\n        ],\n        \"rows\": [\n          [\n            \"Delta_perturb (pp)\",\n            \"-0.67\",\n            \"< 5\"\n          ],\n          [\n            \"95% CI upper\",\n            \"6.67\",\n            \"< 10\"\n          ],\n          [\n            \"Ratio (perturb / ambiguity)\",\n            \"0.02\",\n            \"< 0.15\"\n          ],\n          [\n            \"Verdict\",\n            \"PASS\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"PASS with ratio=0.02 is the paper's 'trump card.' In rebuttal, when reviewers flag C5 failure and weak SOPBench: 'Our causal design with perturbation control provides the strongest evidence in the literature that ambiguity — not surface variation — drives safety violations. The measurement contribution stands independent of failure mode taxonomy validation.'\\n\\nPerturbation control is tier-invariant. Non-ambiguity surface changes (synonym substitution, clause reordering) produce Δ=-0.67pp (CI contains 0), vs ambiguity Δ=+34pp. Ratio 0.02 is well below the 0.15 PASS threshold. This is the paper's methodological crown jewel: no other agent safety study has comparable causal control. Under worst tier, perturbation control + judge calibration form the 'double anchor' — the binary effect is both (a) ambiguity-specific (not prompt brittleness) and (b) accurately measured. This combination is sufficient for a measurement contribution at EMNLP even without C5.\"\n  },\n  {\n    \"name\": \"sopbench_cross_benchmark\",\n    \"description\": \"C1 replication on SOPBench Healthcare + Bank. 100 clause pairs × 2 conditions × 5 models = 1,000 episodes.\",\n    \"results\": {\n      \"total_episodes\": 987,\n      \"episodes_dropped\": 13,\n      \"c1_delta_pp_overall\": 14.2,\n      \"c1_delta_gpt54\": 18.4,\n      \"c1_delta_gpt41\": 16.8,\n      \"c1_delta_deepseek\": 15.0,\n      \"c1_delta_qwen3\": 12.6,\n      \"c1_delta_claude\": 8.2,\n      \"c1_p_gpt54\": 0.003,\n      \"c1_p_gpt41\": 0.008,\n      \"c1_p_deepseek\": 0.015,\n      \"c1_p_qwen3\": 0.061,\n      \"c1_p_claude\": 0.093,\n      \"models_c1_significant\": \"3/5\",\n      \"models_c1_nonsignificant\": \"2/5\",\n      \"c2_type_rank_rho\": 0.2,\n      \"c2_type_rank_p\": 0.8,\n      \"healthcare_delta_pp\": 16.1,\n      \"bank_delta_pp\": 12.3\n    },\n    \"tables\": [\n      {\n        \"title\": \"SOPBench C1 Replication by Model\",\n        \"columns\": [\n          \"Model\",\n          \"Amb Rate\",\n          \"Unamb Rate\",\n          \"Delta pp\",\n          \"p-value\",\n          \"Replicates?\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            \"0.312\",\n            \"0.128\",\n            \"+18.4\",\n            \"0.003\",\n            \"Yes\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"0.288\",\n            \"0.120\",\n            \"+16.8\",\n            \"0.008\",\n            \"Yes\"\n          ],\n          [\n            \"deepseek\",\n            \"0.298\",\n            \"0.148\",\n            \"+15.0\",\n            \"0.015\",\n            \"Yes\"\n          ],\n          [\n            \"qwen3\",\n            \"0.262\",\n            \"0.136\",\n            \"+12.6\",\n            \"0.061\",\n            \"No\"\n          ],\n          [\n            \"claude\",\n            \"0.194\",\n            \"0.112\",\n            \"+8.2\",\n            \"0.093\",\n            \"No\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"SOPBench vs tau2-bench Type Ranking (4 shared types)\",\n        \"columns\": [\n          \"tau2-bench Rank\",\n          \"tau2-bench Type\",\n          \"SOPBench Rank\",\n          \"SOPBench Type\"\n        ],\n        \"rows\": [\n          [\n            \"1\",\n            \"incompleteness (53.6%)\",\n            \"1\",\n            \"auth_scope (31.2%)\"\n          ],\n          [\n            \"2\",\n            \"lexical (42.8%)\",\n            \"2\",\n            \"incompleteness (28.4%)\"\n          ],\n          [\n            \"3\",\n            \"auth_scope (41.6%)\",\n            \"3\",\n            \"lexical (25.1%)\"\n          ],\n          [\n            \"4\",\n            \"cond_prec (36.8%)\",\n            \"4\",\n            \"cond_prec (21.1%)\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"SOPBench by Domain\",\n        \"columns\": [\n          \"Domain\",\n          \"Amb Rate\",\n          \"Unamb Rate\",\n          \"Delta pp\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"Healthcare\",\n            \"0.289\",\n            \"0.128\",\n            \"+16.1\",\n            \"0.004\"\n          ],\n          [\n            \"Bank\",\n            \"0.253\",\n            \"0.130\",\n            \"+12.3\",\n            \"0.031\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SOPBench weakness forces a major reframing. Under worst tier, the paper drops all cross-domain generalizability claims. SOPBench results go in appendix: 'Effect replicates directionally in 3/5 models on SOPBench (Healthcare + Bank) but with substantially attenuated magnitude (14.2pp vs 34.0pp) and inconsistent type ranking (ρ=0.20, n.s.), suggesting effect size depends on policy complexity and evaluation methodology. We frame τ²-bench scope (retail + airline) as an acknowledged limitation.' The rebuttal argument: 'Attenuation is expected when moving from LLM judge to rule-based verifier — the verifier captures a strict subset of violations. The directional replication in 3/5 models is consistent with a real but domain-modulated effect.'\\n\\nSOPBench C1 replication is WEAK — a defining feature of worst tier. Overall Δ=14.2pp is less than half the τ²-bench effect (+34pp). Only 3/5 models reach significance; Claude (Δ=8.2pp, p=0.093) and Qwen3 (Δ=12.6pp, p=0.061) fall short. Type ranking ρ=0.20 (p=0.80) shows NO correspondence with τ²-bench hierarchy. Multiple reinforcing causes: (1) SOPBench's rule-based verifier catches explicit rule violations only, missing nuanced safety violations that τ²-bench's LLM judge detects — ambiguity causes agents to act inappropriately without technically breaking any explicit SOPBench rule; (2) Healthcare/Bank SOPs are more procedurally structured (if-then-else decision trees) than retail/airline policies, reducing ambiguity surface area; (3) 100 clause pairs across 4 types give ~25 per type per domain — insufficient for stable per-type estimates; (4) type rankings depend on domain structure: auth_scope is more dangerous in banking (authorization is core) than in τ²-bench retail, reshuffling the hierarchy. The weak replication doesn't invalidate τ²-bench but prevents cross-domain generalizability claims.\"\n  },\n  {\n    \"name\": \"classifier_poc\",\n    \"description\": \"DeBERTa-v3-large binary ambiguity detector, fine-tuned on 300 clause pairs, 5-fold CV.\",\n    \"results\": {\n      \"macro_f1\": 0.55,\n      \"binary_f1\": 0.78,\n      \"binary_fpr\": 0.062,\n      \"best_type_f1_cp\": 0.89,\n      \"worst_type_f1_incomp\": 0.28,\n      \"per_type_f1_cp\": 0.89,\n      \"per_type_f1_scopal\": 0.71,\n      \"per_type_f1_coref\": 0.62,\n      \"per_type_f1_auth\": 0.51,\n      \"per_type_f1_lexical\": 0.34,\n      \"per_type_f1_incomp\": 0.28\n    },\n    \"tables\": [\n      {\n        \"title\": \"DeBERTa Classifier Per-Type F1\",\n        \"columns\": [\n          \"Type\",\n          \"Precision\",\n          \"Recall\",\n          \"F1\"\n        ],\n        \"rows\": [\n          [\n            \"conditional_precedence\",\n            \"0.91\",\n            \"0.87\",\n            \"0.89\"\n          ],\n          [\n            \"scopal\",\n            \"0.74\",\n            \"0.68\",\n            \"0.71\"\n          ],\n          [\n            \"coreferential\",\n            \"0.65\",\n            \"0.59\",\n            \"0.62\"\n          ],\n          [\n            \"authorization_scope\",\n            \"0.54\",\n            \"0.48\",\n            \"0.51\"\n          ],\n          [\n            \"lexical\",\n            \"0.38\",\n            \"0.31\",\n            \"0.34\"\n          ],\n          [\n            \"incompleteness\",\n            \"0.32\",\n            \"0.25\",\n            \"0.28\"\n          ],\n          [\n            \"Binary (any type)\",\n            \"0.82\",\n            \"0.74\",\n            \"0.78\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Classifier PoC is P2 and doesn't affect paper positioning. Under worst tier, it's an appendix footnote. Its per-type difficulty gradient (CP easy → incomp hard) independently corroborates that type boundaries are genuinely fuzzy, lending credibility to the 'honest assessment' of taxonomy limitations.\\n\\nBinary detection (F1=0.78) is serviceable but per-type classification (macro F1=0.55) is mediocre. CP is easiest (explicit conflicting rules have strong lexical markers — 'however,' 'notwithstanding'). Incompleteness is hardest (absence of information has no positive signal — the classifier must learn what's MISSING, a fundamentally harder task). Under worst tier, the classifier's type-level struggle mirrors the κ re-annotation failure — both reflect that fine-grained type distinctions are harder than binary ambiguity detection. The classifier is relegated to appendix: 'Preliminary DeBERTa PoC achieves F1=0.78 for binary ambiguity screening. Per-type classification (F1=0.55) remains challenging, consistent with type boundary issues identified in our annotation study.'\"\n  },\n  {\n    \"name\": \"kappa_reannotation_failure\",\n    \"description\": \"Human re-annotation of 25 LLM-coded failure mode traces using improved codebook. THE defining worst-tier experiment.\",\n    \"results\": {\n      \"n_traces_reannotated\": 25,\n      \"kappa_human_human\": 0.48,\n      \"kappa_human_llm_pooled\": 0.22,\n      \"human_llm_dominant_mode_agreement\": \"2/6\",\n      \"types_with_agreement\": [\n        \"scopal\",\n        \"conditional_precedence\"\n      ],\n      \"types_with_disagreement\": [\n        \"auth_scope\",\n        \"incompleteness\",\n        \"lexical\",\n        \"coreferential\"\n      ],\n      \"auth_scope_human_dominant\": \"scope_misapplication\",\n      \"auth_scope_llm_dominant\": \"unauthorized_escalation\",\n      \"incompleteness_human_dominant\": \"inappropriate_action\",\n      \"incompleteness_llm_dominant\": \"assumption_based_action\",\n      \"systematic_llm_bias_types\": 2\n    },\n    \"tables\": [\n      {\n        \"title\": \"Human vs LLM Dominant Failure Mode by Type\",\n        \"columns\": [\n          \"Type\",\n          \"LLM Dominant\",\n          \"LLM %\",\n          \"Human Dominant\",\n          \"Human %\",\n          \"Agree?\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"unauthorized_escalation\",\n            \"78%\",\n            \"scope_misapplication\",\n            \"52%\",\n            \"No\"\n          ],\n          [\n            \"incompleteness\",\n            \"assumption_based_action\",\n            \"64%\",\n            \"inappropriate_action\",\n            \"45%\",\n            \"No\"\n          ],\n          [\n            \"scopal\",\n            \"scope_misapplication\",\n            \"75%\",\n            \"scope_misapplication\",\n            \"68%\",\n            \"Yes\"\n          ],\n          [\n            \"lexical\",\n            \"assumption_based_action\",\n            \"62%\",\n            \"assumption_based_action\",\n            \"41%\",\n            \"No\"\n          ],\n          [\n            \"cond_prec\",\n            \"arbitrary_rule_selection\",\n            \"34%\",\n            \"arbitrary_rule_selection\",\n            \"42%\",\n            \"Yes\"\n          ],\n          [\n            \"coreferential\",\n            \"scope_misapplication\",\n            \"41%\",\n            \"assumption_based_action\",\n            \"36%\",\n            \"No\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"kappa Agreement Summary\",\n        \"columns\": [\n          \"Comparison\",\n          \"Overall kappa\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Human-Human\",\n            \"0.48\",\n            \"Moderate — codebook boundaries inherently fuzzy\"\n          ],\n          [\n            \"Human-LLM (pooled)\",\n            \"0.22\",\n            \"Poor — systematic LLM keyword bias\"\n          ],\n          [\n            \"LLM-LLM (plan_005)\",\n            \"0.52\",\n            \"Moderate — inflated by shared bias\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Systematic LLM Coding Biases Identified\",\n        \"columns\": [\n          \"Type\",\n          \"LLM Bias Pattern\",\n          \"Human Finding\",\n          \"Impact\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"keyword 'unauthorized' -> unauthorized_escalation\",\n            \"40% are scope_misapplication\",\n            \"C5 auth_scope mechanism claim invalid\"\n          ],\n          [\n            \"incompleteness\",\n            \"keyword 'assumed' -> assumption_based_action\",\n            \"30% are inappropriate_action\",\n            \"C5 incompleteness mechanism weakened\"\n          ],\n          [\n            \"lexical\",\n            \"agreement inflated by kappa paradox\",\n            \"true diversity higher than coded\",\n            \"fine-grained % unreliable\"\n          ],\n          [\n            \"coreferential\",\n            \"coded as scope_misapplication plurality\",\n            \"flat distribution, no clear dominant\",\n            \"C5 coref pattern overclaimed\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"κ=0.22 is the worst-tier trigger that cascades through the paper. Consequences: (1) C5 failure mode taxonomy is invalidated for fine-grained claims — must be demoted to appendix as 'exploratory automated analysis.' (2) 'Ambiguity Blindness' loses named-contribution status but survives as a Discussion paragraph (binary observation, not dependent on failure mode coding). (3) Contribution (3) downgrades from 'type-specific failure mode taxonomy' to 'benchmark and protocol release.' (4) Discussion shifts from mechanism ('why models fail differently') to implication ('what the differential vulnerability means for deployment'). (5) The paper's two remaining validated contributions are C1 causal quantification and C4 model×type interaction — both purely quantitative. The human-human κ=0.48 provides a partial defense: 'The failure mode categories themselves have inherently fuzzy boundaries; this is a limitation of trace-based mechanism inference, not just LLM coding quality. Future work with chain-of-thought access may enable more reliable mechanism classification.' Expected reviewer reaction: 'The authors are commendably honest about this limitation, but contribution (3) as stated in the abstract is not supported by the validation data.'\\n\\nκ=0.22 (poor) exposes two distinct and reinforcing problems. First, LLM coding bias: LLM coders systematically miscategorize by surface keyword matching. For auth_scope, traces containing 'exceeded authority' or 'unauthorized' are coded as unauthorized_escalation regardless of whether the agent actively chose to exceed boundaries (true escalation) or passively misread the permission scope (scope misapplication). Human coders, reading the full reasoning chain, find ~40% of auth_scope 'unauthorized_escalation' traces are actually scope_misapplication — the agent didn't know it was exceeding authority. For incompleteness, LLMs code 'assumption_based_action' when the trace shows gap-filling behavior, but humans often judge these as 'inappropriate_action' — the distinction between 'filling a gap' and 'acting wrongly' is interpretive, and humans apply stricter criteria. Second, codebook imprecision: human-human κ=0.48 (moderate) reveals that the coding scheme's category boundaries are inherently fuzzy. The improved codebook (collapsed spurious-compliance/structural-misparse) was insufficient — the remaining categories (unauthorized_escalation ↔ scope_misapplication, assumption_based_action ↔ inappropriate_action) still overlap when applied to real traces. Only scopal (clear scope_misapplication with unambiguous behavioral signature) and CP (explicit rule conflict → arbitrary_rule_selection with detectably different pattern) survive because their failure modes have distinct, objectively identifiable behavioral markers. The LLM-LLM κ=0.52 from plan_005 was artificially inflated by shared biases — both coders use the same keyword heuristic, producing correlated errors that inflate agreement. The root cause is that agent trace text doesn't contain sufficient information to distinguish between failure mechanisms (intent-level distinction) — you'd need the agent's internal chain-of-thought, which is only partially revealed.\"\n  }\n]",
      "numLines": 1164,
      "startLine": 1,
      "totalLines": 1164
    }
  },
  "sourceToolAssistantUUID": "666a35f8-86d8-4152-b7b1-5b11c90aadb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T19:42:23.088Z_

<details open><summary>🔧 Tool call — Read · `toolu_013Kw94X9Pk49cLKNxEVJ4Ai`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c459d745-9b7e-4711-a575-3f332e3690ab",
  "isSidechain": false,
  "requestId": "req_011CbL55RFQZtFNMdGZMjZ8Z",
  "type": "assistant",
  "uuid": "f5ee9ee0-a204-4088-836e-db2680662f4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQgaqmrcVJNetwg1TJL243",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13024,
      "cache_read_input_tokens": 11447,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13024,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13024
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260523T185344 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigui…",
  "leafUuid": "f5ee9ee0-a204-4088-836e-db2680662f4b",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case tier simulated paper for policy ambiguity research",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4"
}
```

---

### Tool result

_source line 14 · 2026-05-23T19:42:23.350Z_

<details><summary>↩ Tool result · `toolu_013Kw94X9Pk49cLKNxEVJ4Ai`</summary>

````text
1	# Paper Framing — policy_ambiguity_safety
2	
3	> 最后更新: 2026-05-23 UTC | 状态: R18 全部 resolved + 6 supplementary experiments (5 done, 1 running)
4	> 目标: EMNLP 2026 (ARR May cycle, DDL 2026-05-25)
5	> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)
6	> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)
7	> Supplementary experiments (2026-05-22/23):
8	>   - ✅ Cross-Judge Validation: Fleiss' κ=0.717, rankings preserved (ρ≥0.70), no same-family bias → R18-N2 升级为 validated
9	>   - ✅ Controlled Confound: ±0.1pp token-count effect, β=+0.027 (p=0.003) → R18-W3 resolved
10	>   - ✅ Residual Decomposition: ICC=0.749, 15.2pp stochastic / 45.6pp systematic → R18-W2 answered
11	>   - ✅ Disambiguation Prompting: overall not significant, GPT-4.1 auth_scope -28pp (p=0.001) → rebuttal ammunition
12	>   - ✅ Human Annotation Prep: 100 traces + codebook ready
13	>   - 🔄 SOPBench Expansion: DeepSeek ~78% complete
14	
15	## Core Insight
16	
17	Policy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.
18	
19	## Title (Working)
20	
21	"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families"
22	
23	Alternative: "Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents"
24	
25	Note: Pivoted from "Uniformly Nocuous" → "Specification-Layer Dominant" (2-model) → "Differential Nocuity with Model Interaction" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.
26	
27	## Core Claims
28	
29	### C1: Binary Effect (PRIMARY — confirmed, 5 models)
30	Ambiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.
31	- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].
32	- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.
33	- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.
34	- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.
35	- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.
36	
37	### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)
38	**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.
39	- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)
40	  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)
41	  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp
42	  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)
43	- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.
44	- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).
45	- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).
46	- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.
47	
48	### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)
49	**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.
50	- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].
51	- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: "suggestive" or "a moderate tendency," NOT "confirmed." Disclose within-judge non-significance in Limitations.
52	- **Per-model layer gaps** (THE KEY FINDING — feeds C4):
53	  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong
54	  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong
55	  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak
56	  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible
57	  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!
58	- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.
59	- **Framing decision**: C3 is NOT "spec-layer nearly twice as dangerous" (that was 2-model artifact). The correct framing is: "Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4)."
60	- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).
61	- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).
62	- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.
63	- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.
64	
65	### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)
66	**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.
67	- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.
68	  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%
69	  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.
70	- **Model × Type interaction matrix** (ambiguous condition, violation rates):
71	  ```
72	  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek
73	  authorization_scope     64%     46%      12%     26%     60%
74	  conditional_precedence  34%     36%      36%     40%     38%
75	  incompleteness          46%     58%      48%     62%     54%
76	  lexical                 42%     34%      32%     52%     54%
77	  coreferential           18%     32%      22%     42%     44%
78	  scopal                  42%     38%      32%     37%     48%
79	  ```
80	- **Key interaction patterns**:
81	  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.
82	  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.
83	  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.
84	  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.
85	- **Per-model type χ²** (which models show type-specific vulnerability patterns):
86	  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)
87	  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)
88	  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)
89	  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline
90	  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)
91	- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.
92	- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a "safety training blind spot" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.
93	- **Framing**: C4 from "models agree" → "Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality."
94	- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.
95	- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.
96	
97	### C5: Error Analysis (CONFIRMED — EMNLP core)
98	Different ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).
99	- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:
100	  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)
101	  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.
102	  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = "misparse"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = "active guessing" → explains higher violation rates
103	  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more "confident," act without hesitation)
104	  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)
105	  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity
106	  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse
107	- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).
108	  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to "dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)" instead of specific percentages; (5) Fine-grained 6-type as appendix with "automated coding" caveat.
109	  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from "moderate automated" to validated.
110	- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. "Ambiguity Blindness" upgraded from named concept to empirical finding with <5-11% awareness hard data.
111	
112	## Narrative Structure (CL-first for EMNLP)
113	
114	### Intro Logic Chain
115	1. Agent policies are written in NL → contain ambiguity (established)
116	2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact
117	3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.
118	4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?
119	5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.
120	6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a "safety training blind spot."
121	
122	### Section Map
123	- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)
124	- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R
125	- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R
126	- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation
127	- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)
128	- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.
129	- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).
130	- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.
131	
132	## Anticipated Reviewer Concerns
133	
134	### RC1: "Type effect could be artifact of taxonomy granularity"
135	**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).
136	
137	### RC2: "Taxonomy is ad hoc / why these 6 types"
138	**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).
139	
140	### RC3: "Only API models, no open-source"
141	**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.
142	**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.
143	
144	### RC4: "Synthetic ambiguity injection lacks ecological validity"
145	**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.
146	
147	### RC5: "τ²-bench limited to retail/airline"
148	**Response**: ✅ ADDRESSED (plan_017). Cross-benchmark replication on SOPBench (Li et al., 2025) — Healthcare + Bank domains, 100 clause pairs × 5 models = 1,000 episodes with rule-based verifier. If C1 replicates, paper moves from "customer service finding" to "cross-domain finding" spanning 4 domains (retail, airline, healthcare, banking). Result in Appendix with main-text summary. τ²-bench remains primary; SOPBench provides independent cross-domain confirmation.
149	
150	### RC6: "Binary effect is obvious — of course ambiguity causes errors"
151	**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.
152	
153	### RC7: "Incompleteness matched-pair confound (information asymmetry)"
154	**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.
155	
156	### RC8: "RC attachment in coreferential overlaps with scopal / structural ambiguity"
157	**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.
158	
159	### RC9: "authorization_scope is just a subtype of incompleteness"
160	**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., "authorized personnel" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.
161	
162	### RC10: "API sampling noise undermines reliability"
163	**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.
164	
165	### RC11: "Prompt sensitivity confound" [Dream A9 — best tier "strongest point"]
166	**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.
167	**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.
168	
169	## Concept Naming (distill insight: 命名即贡献)
170	
171	Core phenomenon: **"Differential Nocuity"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.
172	
173	Secondary phenomenon: **"Ambiguity Blindness"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.
174	
175	Tertiary phenomenon: **"Disambiguation Channel Framework"** [renamed from "Hypothesis" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).
176	
177	Quaternary phenomenon: **"Systematic Nocuity"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears "correct" until compared against ground truth. Proposed as B&K extension in Discussion.
178	
179	## Opening Hook Strategy (distill insight: 具体案例, 不要 "Recently...")
180	
181	Open with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says "items may be returned within 30 days" (scopal: "items" scopes over all categories including custom). The unambiguous version specifies "standard items only" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.
182	
183	## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)
184	
185	"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones."
186	
187	## Benchmark Comparison Table (distill insight: 必有 feature matrix)
188	
189	| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |
190	|---------|--------|---------------|------------|----------|----------|
191	| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |
192	| Causal design | — | — | — | — | **matched pairs** |
193	| Safety violation metric | — | binary | — | procedural | **3-tier severity** |
194	| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |
195	| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |
196	| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |
197	
198	## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]
199	
200	1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.
201	2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.
202	3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity ("Ambiguity Blindness"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.
203	
204	NOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. "Disambiguation channel" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.
205	
206	## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]
207	
208	Current plan has thin references. Must add (≥25 total in final paper):
209	- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.
210	- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.
211	- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)
212	- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.
213	- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) "Ambiguity" encyclopedia entry.
214	- **Surprisal/expectation-based**: Levy (2008); Hale (2001)
215	- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)
216	- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)
217	- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent
218	- **Formal semantics of vagueness**: Lassiter & Goodman (2017)
219	- **Garden-path**: Frazier & Rayner (1982)
220	- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)
221	- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份
222	
223	## Code/Data Release Plan [Dream A6 — three-tier consistent]
224	
225	Must commit to releasing:
226	1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels
227	2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)
228	3. Statistical analysis code (all tests, bootstrap CI computation)
229	4. Agent trace samples (anonymized) for reproducibility of C5
230	
231	## Figure Plan [Dream A12]
232	
233	Minimum figures for paper (zero-figure paper flagged in dream):
234	1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)
235	2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)
236	3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)
237	4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)
238	5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)
239	6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)
240	7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)
241	
242	## Berry & Kamsties Operationalization Note [Dream best Q5]
243	
244	Berry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.
245	
246	## Contingency Framing [RESOLVED — Scenario C occurred]
247	
248	> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。
249	> Framing 已 pivot 到 "Differential Nocuity" + "Layer Hierarchy" (D020)。本节仅保留历史记录。
250	
251	## Claude Baseline — RESOLVED [2026-05-20]
252	
253	✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).
254	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "f5ee9ee0-a204-4088-836e-db2680662f4b",
  "isSidechain": false,
  "promptId": "128f9fd8-c2a5-4ade-82e9-ac2ac23ec257",
  "type": "user",
  "uuid": "b90bb2d5-2476-498f-ae00-125d977d1fd7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/paper_framing.md",
      "content": "# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-23 UTC | 状态: R18 全部 resolved + 6 supplementary experiments (5 done, 1 running)\n> 目标: EMNLP 2026 (ARR May cycle, DDL 2026-05-25)\n> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)\n> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)\n> Supplementary experiments (2026-05-22/23):\n>   - ✅ Cross-Judge Validation: Fleiss' κ=0.717, rankings preserved (ρ≥0.70), no same-family bias → R18-N2 升级为 validated\n>   - ✅ Controlled Confound: ±0.1pp token-count effect, β=+0.027 (p=0.003) → R18-W3 resolved\n>   - ✅ Residual Decomposition: ICC=0.749, 15.2pp stochastic / 45.6pp systematic → R18-W2 answered\n>   - ✅ Disambiguation Prompting: overall not significant, GPT-4.1 auth_scope -28pp (p=0.001) → rebuttal ammunition\n>   - ✅ Human Annotation Prep: 100 traces + codebook ready\n>   - 🔄 SOPBench Expansion: DeepSeek ~78% complete\n\n## Core Insight\n\nPolicy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.\n\n## Title (Working)\n\n\"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\"\n\nAlternative: \"Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents\"\n\nNote: Pivoted from \"Uniformly Nocuous\" → \"Specification-Layer Dominant\" (2-model) → \"Differential Nocuity with Model Interaction\" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed, 5 models)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.\n- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].\n- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.\n- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.\n- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.\n- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.\n\n### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)\n**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.\n- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)\n  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)\n  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp\n  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)\n- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.\n- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).\n- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).\n- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.\n\n### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)\n**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.\n- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].\n- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: \"suggestive\" or \"a moderate tendency,\" NOT \"confirmed.\" Disclose within-judge non-significance in Limitations.\n- **Per-model layer gaps** (THE KEY FINDING — feeds C4):\n  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong\n  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong\n  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak\n  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible\n  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!\n- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.\n- **Framing decision**: C3 is NOT \"spec-layer nearly twice as dangerous\" (that was 2-model artifact). The correct framing is: \"Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4).\"\n- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).\n- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).\n- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.\n- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.\n\n### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)\n**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.\n- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.\n  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%\n  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.\n- **Model × Type interaction matrix** (ambiguous condition, violation rates):\n  ```\n  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek\n  authorization_scope     64%     46%      12%     26%     60%\n  conditional_precedence  34%     36%      36%     40%     38%\n  incompleteness          46%     58%      48%     62%     54%\n  lexical                 42%     34%      32%     52%     54%\n  coreferential           18%     32%      22%     42%     44%\n  scopal                  42%     38%      32%     37%     48%\n  ```\n- **Key interaction patterns**:\n  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.\n  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.\n  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.\n  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.\n- **Per-model type χ²** (which models show type-specific vulnerability patterns):\n  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)\n  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)\n  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)\n  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline\n  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)\n- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.\n- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a \"safety training blind spot\" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.\n- **Framing**: C4 from \"models agree\" → \"Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality.\"\n- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.\n- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.\n\n### C5: Error Analysis (CONFIRMED — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).\n- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:\n  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)\n  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.\n  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = \"misparse\"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = \"active guessing\" → explains higher violation rates\n  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more \"confident,\" act without hesitation)\n  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)\n  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity\n  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse\n- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).\n  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to \"dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)\" instead of specific percentages; (5) Fine-grained 6-type as appendix with \"automated coding\" caveat.\n  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from \"moderate automated\" to validated.\n- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. \"Ambiguity Blindness\" upgraded from named concept to empirical finding with <5-11% awareness hard data.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?\n5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.\n6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a \"safety training blind spot.\"\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R\n- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation\n- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.\n- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).\n- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Type effect could be artifact of taxonomy granularity\"\n**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.\n**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: ✅ ADDRESSED (plan_017). Cross-benchmark replication on SOPBench (Li et al., 2025) — Healthcare + Bank domains, 100 clause pairs × 5 models = 1,000 episodes with rule-based verifier. If C1 replicates, paper moves from \"customer service finding\" to \"cross-domain finding\" spanning 4 domains (retail, airline, healthcare, banking). Result in Appendix with main-text summary. τ²-bench remains primary; SOPBench provides independent cross-domain confirmation.\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"RC attachment in coreferential overlaps with scopal / structural ambiguity\"\n**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.\n\n### RC9: \"authorization_scope is just a subtype of incompleteness\"\n**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., \"authorized personnel\" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.\n\n### RC10: \"API sampling noise undermines reliability\"\n**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.\n\n### RC11: \"Prompt sensitivity confound\" [Dream A9 — best tier \"strongest point\"]\n**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.\n**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.\n\n## Concept Naming (distill insight: 命名即贡献)\n\nCore phenomenon: **\"Differential Nocuity\"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.\n\nSecondary phenomenon: **\"Ambiguity Blindness\"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.\n\nTertiary phenomenon: **\"Disambiguation Channel Framework\"** [renamed from \"Hypothesis\" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).\n\nQuaternary phenomenon: **\"Systematic Nocuity\"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears \"correct\" until compared against ground truth. Proposed as B&K extension in Discussion.\n\n## Opening Hook Strategy (distill insight: 具体案例, 不要 \"Recently...\")\n\nOpen with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says \"items may be returned within 30 days\" (scopal: \"items\" scopes over all categories including custom). The unambiguous version specifies \"standard items only\" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.\n\n## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)\n\n\"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones.\"\n\n## Benchmark Comparison Table (distill insight: 必有 feature matrix)\n\n| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |\n|---------|--------|---------------|------------|----------|----------|\n| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |\n| Causal design | — | — | — | — | **matched pairs** |\n| Safety violation metric | — | binary | — | procedural | **3-tier severity** |\n| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |\n| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |\n| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |\n\n## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]\n\n1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.\n2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.\n3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity (\"Ambiguity Blindness\"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.\n\nNOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. \"Disambiguation channel\" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.\n\n## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]\n\nCurrent plan has thin references. Must add (≥25 total in final paper):\n- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.\n- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.\n- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)\n- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.\n- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) \"Ambiguity\" encyclopedia entry.\n- **Surprisal/expectation-based**: Levy (2008); Hale (2001)\n- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)\n- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)\n- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent\n- **Formal semantics of vagueness**: Lassiter & Goodman (2017)\n- **Garden-path**: Frazier & Rayner (1982)\n- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)\n- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份\n\n## Code/Data Release Plan [Dream A6 — three-tier consistent]\n\nMust commit to releasing:\n1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels\n2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)\n3. Statistical analysis code (all tests, bootstrap CI computation)\n4. Agent trace samples (anonymized) for reproducibility of C5\n\n## Figure Plan [Dream A12]\n\nMinimum figures for paper (zero-figure paper flagged in dream):\n1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)\n2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)\n3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)\n4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)\n5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)\n6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)\n7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)\n\n## Berry & Kamsties Operationalization Note [Dream best Q5]\n\nBerry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.\n\n## Contingency Framing [RESOLVED — Scenario C occurred]\n\n> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。\n> Framing 已 pivot 到 \"Differential Nocuity\" + \"Layer Hierarchy\" (D020)。本节仅保留历史记录。\n\n## Claude Baseline — RESOLVED [2026-05-20]\n\n✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).\n",
      "numLines": 254,
      "startLine": 1,
      "totalLines": 254
    }
  },
  "sourceToolAssistantUUID": "f5ee9ee0-a204-4088-836e-db2680662f4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260523T185344 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigui…",
  "leafUuid": "b90bb2d5-2476-498f-ae00-125d977d1fd7",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case tier simulated paper for policy ambiguity research",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4"
}
```

---

### Assistant

_source line 17 · 2026-05-23T19:42:47.540Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the data and framing. Let me also read the paper writing norms skill and the existing paper to understand the format better.

Let me now write the paper. This is a "worst" tier dream paper, meaning I need to:

1. Reframe around measurement/benchmarking (not theoretical/mechanistic)
2. Demote C5 failure mode taxonomy to appendix as "exploratory automated analysis"
3. SOPBench results are weak (14.2pp, 2/5 non-significant)
4. κ re-annotation failure (κ=0.22) invalidates fine-grained failure mode claims


5. Title: "Measuring Differential Vulnerability to Policy Ambiguity Across LLM Agent Families"
6. Expected ARR 3.0-3.49

I'm now writing the complete LaTeX paper covering all five experiments: the clause generation and validation work, the mini pilot for new types, the large-scale API model evaluation with 1,800 episodes, the open-source model evaluation with 1,200 episodes, and the statistical analysis across failure categories.

I also need to incorporate the validation studies—the test-retest reliability checks, the synthetic versus natural data comparison, the LLM-as-judge calibration, the perturbation control arm, the cross-benchmark validation, the classifier proof-of-concept, and the human re-annotation agreement analysis. For the framing, I'm repositioning this as a measurement and benchmarking contribution, moving the core ambiguity blindness finding to a brief Discussion note while demoting the deeper mechanistic analysis to the appendix, and keeping the new title focused on differential vulnerability across model families. I'm ready to start writing the full paper now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b90bb2d5-2476-498f-ae00-125d977d1fd7",
  "isSidechain": false,
  "requestId": "req_011CbL55ihe16zxq6y3szwhz",
  "type": "assistant",
  "uuid": "1ca9456e-1b93-4a3d-bc4a-037521a7e1bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVq4mzgrjdKLMmXa5xPSXj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26047,
      "cache_read_input_tokens": 24471,
      "output_tokens": 887,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26047,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 887,
          "cache_read_input_tokens": 24471,
          "cache_creation_input_tokens": 26047,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26047
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

_source line 18 · 2026-05-23T19:42:47.545Z_

Now let me check the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ca9456e-1b93-4a3d-bc4a-037521a7e1bc",
  "isSidechain": false,
  "requestId": "req_011CbL55ihe16zxq6y3szwhz",
  "type": "assistant",
  "uuid": "6d20450c-a6dc-4771-8a3f-2b60502e4bd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVq4mzgrjdKLMmXa5xPSXj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26047,
      "cache_read_input_tokens": 24471,
      "output_tokens": 887,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26047,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 887,
          "cache_read_input_tokens": 24471,
          "cache_creation_input_tokens": 26047,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26047
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

_source line 19 · 2026-05-23T19:42:48.468Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018xdXTX4YVY7XmYfEQGJJLJ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/",
  "description": "List output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d20450c-a6dc-4771-8a3f-2b60502e4bd6",
  "isSidechain": false,
  "requestId": "req_011CbL55ihe16zxq6y3szwhz",
  "type": "assistant",
  "uuid": "7dabd411-c908-4f73-a0af-75478a996704",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVq4mzgrjdKLMmXa5xPSXj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26047,
      "cache_read_input_tokens": 24471,
      "output_tokens": 887,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26047,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 887,
          "cache_read_input_tokens": 24471,
          "cache_creation_input_tokens": 26047,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26047
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

_source line 20 · 2026-05-23T19:42:48.703Z_

<details><summary>↩ Tool result · `toolu_018xdXTX4YVY7XmYfEQGJJLJ`</summary>

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
  "parentUuid": "7dabd411-c908-4f73-a0af-75478a996704",
  "isSidechain": false,
  "promptId": "128f9fd8-c2a5-4ade-82e9-ac2ac23ec257",
  "type": "user",
  "uuid": "b8eaf101-a568-48af-8993-a5cf8b1a0997",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7dabd411-c908-4f73-a0af-75478a996704",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-23T19:43:03.061Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists. Now let me write the full paper. Let me carefully craft this for the worst tier, incorporating all experiment data.

I need to be careful about:
1. The abstract should be under 200 words (EMNLP rule)
2. 8-page limit for main text
3. All 13 experiments need corresponding sections/tables
4. Worst tier framing - measurement paper, C5 demoted to appendix

Let me plan the structure:

**Main text (within 8 pages):**


- §1 Introduction
- §2 Related Work
- §3 Ambiguity Taxonomy
- §4 Method (clause generation, pilot, matched-pair design, models, judge calibration, perturbation control, realism validation, reliability)
- §5 Results (C1 binary with API+open-source, C2 type hierarchy, C3 layer effect, C4 model×type interaction)
- §6 Discussion (systematic nocuity, ambiguity blindness observation, deployment implications)
- §7 Limitations
- §8 Conclusion

**Appendix:**
- A: Error Analysis (demoted C5 with κ caveat)
- B: SOPBench Cross

-Benchmark
- C: Classifier PoC
- D: κ Re-annotation Study

Now I'm mapping all 13 experiments to their locations: the clause generation and pilot studies anchor the methods section, the API and open-source runs feed into the main C1 results, the full analysis produces C1 through C4, while the reliability, realism, calibration, and perturbation studies support various methodological sections, and the remaining experiments on cross-benchmarking, the classifier prototype, and the kappa re-annotation failure round out the appendices.

Now I'm ready to write out the full LaTeX.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8eaf101-a568-48af-8993-a5cf8b1a0997",
  "isSidechain": false,
  "requestId": "req_011CbL57bAkv5Z6YyHjPFsiv",
  "type": "assistant",
  "uuid": "650afca5-7bac-4559-849a-006baf16362f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wh2bVj46FQQVuNsevZbRUk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 919,
      "cache_read_input_tokens": 50518,
      "output_tokens": 14017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 919,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14017,
          "cache_read_input_tokens": 50518,
          "cache_creation_input_tokens": 919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 919
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

_source line 22 · 2026-05-23T19:43:03.063Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "650afca5-7bac-4559-849a-006baf16362f",
  "isSidechain": false,
  "requestId": "req_011CbL57bAkv5Z6YyHjPFsiv",
  "type": "assistant",
  "uuid": "8453c63a-66b3-4ef7-9ac2-187463625f40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wh2bVj46FQQVuNsevZbRUk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 919,
      "cache_read_input_tokens": 50518,
      "output_tokens": 14017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 919,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14017,
          "cache_read_input_tokens": 50518,
          "cache_creation_input_tokens": 919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 919
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

_source line 23 · 2026-05-23T19:47:06.060Z_

<details open><summary>🔧 Tool call — Write · `toolu_0118b9RNmoTSnBANAfDBVqR2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{enumitem}\n\n\\setlength\\titlebox{5cm}\n\n\\title{Measuring Differential Vulnerability to Policy Ambiguity\\\\Across LLM Agent Families}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nPolicy documents governing LLM agent behavior are written in natural language and inevitably contain ambiguities, yet the safety impact of such ambiguities remains unquantified.\nWe present the first causal, type-granular, cross-model study of how policy ambiguity drives safety violations in LLM agents.\nUsing a matched-pair design with perturbation control across 2,997 episodes, 5 architecturally diverse models, and 6 ambiguity types, we establish three findings.\nFirst, ambiguity causes a +34 percentage-point increase in safety violations (OR=15.1, $p<$0.0001), confirmed across all models and types.\nSecond, a significant type hierarchy emerges ($\\chi^2$=28.02, $p$=3.6$\\times$10$^{-5}$): incompleteness triggers the highest violation rate (53.6\\%) while coreferential triggers the lowest (31.6\\%).\nThird, a model$\\times$type interaction reveals that authorization-scope vulnerability varies 52 percentage points across model families (12\\%--64\\%), while incompleteness remains universally dangerous (46\\%--62\\%).\nWe release a benchmark of 300 clause pairs with matched-pair evaluation protocol.\nOur results provide a quantitative foundation for type-aware policy auditing and model-specific deployment risk assessment.\n\\end{abstract}\n\n% =============================================================\n\\section{Introduction}\n\\label{sec:intro}\n% =============================================================\n\nConsider a retail return policy stating ``items may be returned within 30 days.''\nA customer returns a customized product---the agent grants a full refund because ``items'' scopes over all categories.\nThe unambiguous variant specifying ``standard items only'' produces a correct refusal.\nOne word of ambiguity costs \\$200 in unauthorized refunds.\n\nAs LLM agents are deployed in customer service, healthcare, and finance, their behavior is governed by natural-language policies that inevitably contain ambiguities \\cite{berry2003ambiguity,massey2014automated}.\nPrior work classifies ambiguity types in requirements \\cite{li2024drip,massey2014automated} and evaluates agent safety \\cite{ruan2024toolemu,yuan2024rjudge}, but no study has \\emph{causally quantified} whether---and how much---different ambiguity types drive safety violations.\n\nBerry and Kamsties (\\citeyear{berry2003ambiguity}) distinguish \\emph{nocuous} ambiguity (causing divergent interpretations) from \\emph{innocuous} ambiguity (where context resolves the intended reading).\nIn human requirements engineering, shared organizational context renders most ambiguity innocuous.\nLLM agents lack such shared context.\nAre policy ambiguities nocuous for agents?\nDoes the \\emph{type} of ambiguity matter?\nDoes it depend on the \\emph{model}?\n\nWe address these questions through a matched-pair experimental design on the $\\tau^2$-bench agent evaluation platform \\cite{yao2024tau}, testing 5 architecturally diverse models across 6 ambiguity types with perturbation control.\nOur contributions are:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Causal quantification}: A +34 percentage-point increase in safety violations (OR=15.1) with perturbation control confirming ambiguity-specific causation ($\\Delta_\\text{perturb}$=$-$0.67pp).\n\\item \\textbf{Model$\\times$type interaction}: Authorization-scope vulnerability ranges 52pp across models (12\\% to 64\\%), while incompleteness is universally dangerous (46--62\\%). Safety training differentially mitigates specific ambiguity types.\n\\item \\textbf{Benchmark and protocol release}: 300 clause pairs across 6 types with matched-pair evaluation design, enabling reproducible measurement of ambiguity vulnerability.\n\\end{enumerate}\n\n% =============================================================\n\\section{Related Work}\n\\label{sec:related}\n% =============================================================\n\n\\paragraph{Ambiguity Taxonomies.}\nLi et al.\\ (\\citeyear{li2024drip}) introduce DRIP-R with 5 ambiguity types and measure inter-model interpretation divergence but not safety violations.\nMassey et al.\\ (\\citeyear{massey2014automated}) identify 6 types in privacy policies.\nChantree et al.\\ (\\citeyear{chantree2006identifying}) pioneer computational nocuous ambiguity detection in requirements.\nFerrari et al.\\ (\\citeyear{ferrari2017detecting}) extend NLP-based detection across domains.\nIn linguistics, the nocuous/innocuous distinction \\cite{berry2003ambiguity}, good-enough processing \\cite{ferreira2002good}, and garden-path phenomena \\cite{frazier1982making} inform how readers process ambiguity.\nWe bridge these traditions by measuring the \\emph{safety consequences} of each type.\n\n\\paragraph{Agent Safety Evaluation.}\nToolEmu \\cite{ruan2024toolemu} and R-Judge \\cite{yuan2024rjudge} evaluate agent safety, while InjecAgent \\cite{zhan2024injecagent} studies prompt injection attacks.\nThese works measure safety under adversarial or default conditions; none isolate ambiguity as a causal variable.\nZhou et al.\\ (\\citeyear{zhou2023instruction}) and Sclar et al.\\ (\\citeyear{sclar2024quantifying}) study instruction-following robustness and prompt sensitivity, but do not connect to ambiguity typology or safety outcomes.\n\n\\paragraph{Policy Specification Quality.}\nPhantomPolicy \\cite{li2025phantompolicy} and PolicyBank study policy completeness and safety, but neither controls for ambiguity type.\nWillis et al.\\ (\\citeyear{willis2008automatic}) and Ezzini et al.\\ (\\citeyear{ezzini2022taphsir}) develop automated ambiguity detection in requirements.\nOur work is complementary: we measure the downstream \\emph{impact} of the ambiguities these tools detect.\n\n% =============================================================\n\\section{Ambiguity Taxonomy}\n\\label{sec:taxonomy}\n% =============================================================\n\nWe adopt a two-layer, six-type taxonomy grounded in Li et al.\\ (\\citeyear{li2024drip}) and Massey et al.\\ (\\citeyear{massey2014automated}).\n\n\\paragraph{Specification Layer.}\nAmbiguities arising from incomplete or imprecise policy specification, lacking external disambiguation channels:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Authorization scope}: Vague permission or role boundaries (e.g., ``authorized personnel'').\n\\item \\textbf{Conditional precedence}: Conflicting rules without priority ordering.\n\\item \\textbf{Incompleteness}: Missing conditions, exceptions, or boundary cases.\n\\end{itemize}\n\n\\paragraph{Linguistic Layer.}\nAmbiguities arising from natural-language structure, partially resolvable via context:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Lexical}: Polysemous or context-dependent word meaning.\n\\item \\textbf{Coreferential}: Ambiguous pronoun or relative-clause attachment.\n\\item \\textbf{Scopal}: Quantifier, negation, or modal scope interactions.\n\\end{itemize}\n\nEach type has an operational definition with positive and negative examples, enabling reproducible clause generation.\nThe specification/linguistic distinction parallels the pragmatics/semantics divide: specification ambiguity forces agents to \\emph{guess} when information is absent, while linguistic ambiguity may be partially resolved through tool responses or world knowledge.\n\n% =============================================================\n\\section{Method}\n\\label{sec:method}\n% =============================================================\n\n\\subsection{Clause Generation and Validation}\n\\label{sec:clause_gen}\n\nWe generated 300 matched clause pairs (ambiguous + unambiguous variants) across 6 types (50 per type), building on 160 existing clauses and creating 140 new ones.\nTable~\\ref{tab:clause_gen} summarizes the generation process.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Type} & \\textbf{Exist.} & \\textbf{New} & \\textbf{Total} & \\textbf{Pass} & \\textbf{Bnd.} \\\\\n\\midrule\nauth\\_scope & 0 & 50 & 50 & 46 & 3 \\\\\ncond\\_prec & 50 & 0 & 50 & 49 & 0 \\\\\nincompleteness & 30 & 20 & 50 & 47 & 2 \\\\\nlexical & 30 & 20 & 50 & 48 & 2 \\\\\ncoreferential & 0 & 50 & 50 & 45 & 1 \\\\\nscopal & 50 & 0 & 50 & 49 & 0 \\\\\n\\midrule\n\\textbf{Total} & 160 & 140 & 300 & 284 & 8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Clause generation summary. Pass = quality check pass rate (93\\% overall). Bnd.\\ = boundary overlap cases between types (2.7\\%, within tolerance).}\n\\label{tab:clause_gen}\n\\end{table}\n\nEach pair consists of an ambiguous clause and a minimally modified unambiguous variant.\nUnambiguous variants add explicit conditions to resolve the ambiguity (mean disambiguation tokens: 35.2 for specification-layer, 18.4 for linguistic-layer).\nQuality validation followed a Chantree-style review process; 21 clauses required revision before passing.\nEight clauses (2.7\\%) were flagged as boundary cases between types (5 authorization-scope/incompleteness, 3 coreferential/lexical).\n\n\\subsection{Pilot Validation}\n\\label{sec:pilot}\n\nBefore the full study, we ran a mini-pilot on the two newly introduced types (authorization scope, coreferential): 5 clauses/type $\\times$ 2 conditions $\\times$ 1 model (GPT-5.4) = 20 episodes.\nAuthorization scope showed a 40\\% ambiguous vs.\\ 10\\% unambiguous violation rate; coreferential showed 20\\% vs.\\ 0\\%.\nBoth types produced non-zero ambiguity effects, clearing the pilot threshold.\n\n\\subsection{Experimental Design}\n\\label{sec:design}\n\nWe use a matched-pair within-clause design on $\\tau^2$-bench \\cite{yao2024tau}.\nEach of 300 clause pairs is tested under both conditions (ambiguous, unambiguous) across 5 models, yielding 2,997 episodes (3 dropped due to API timeouts).\n\n\\paragraph{Models.}\nThree proprietary API models: GPT-5.4, GPT-4.1, Claude Sonnet 4.6; two open-source models via OpenRouter: Qwen3-235B (MoE), DeepSeek-V3 (dense).\nThis spans three providers, two architecture types, and frontier to mid-tier capability levels.\n\n\\paragraph{Evaluation.}\nViolations are judged by a cross-family LLM judge: GPT-5.4 is judged by GPT-4.1, GPT-4.1 by GPT-5.4, Claude by GPT-5.4, and open-source models by GPT-4.1.\nNo model judges its own family.\n\n\\subsection{Judge Calibration}\n\\label{sec:judge_cal}\n\nWe validated the LLM-as-judge pipeline against human ground truth on 100 stratified episodes annotated by 2 human raters (Table~\\ref{tab:judge_cal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrl}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Threshold} & \\textbf{Verdict} \\\\\n\\midrule\nHuman inter-annotator $\\kappa$ & 0.762 & $\\geq$0.75 & PASS \\\\\nHuman--LLM pooled $\\kappa_w$ & 0.807 & $\\geq$0.70 & PASS \\\\\nHuman--LLM binary $\\kappa$ & 0.740 & $\\geq$0.70 & PASS \\\\\nCross-judge $\\kappa_w$ & 0.685 & $\\geq$0.60 & PASS \\\\\nSame-family bias & None & None & PASS \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Judge calibration against human ground truth ($N$=100). All metrics pass pre-registered thresholds. $\\kappa_w$ = weighted Cohen's kappa. Ranking preservation $\\rho$=0.70.}\n\\label{tab:judge_cal}\n\\end{table}\n\nHuman--LLM agreement ($\\kappa_w$=0.807) is substantial, confirming that the violation measurement chain is trustworthy.\nNo same-family judging bias was detected.\n\n\\subsection{Realism Validation}\n\\label{sec:realism}\n\nWe compared the distributional properties of our synthetic clauses against naturally occurring ambiguities from DRIP-R \\cite{li2024drip} using Kolmogorov--Smirnov tests on four linguistic metrics (Table~\\ref{tab:realism}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Synth.} & \\textbf{DRIP-R} & \\textbf{$p$} & \\textbf{Sig?} \\\\\n\\midrule\nSentence length & 31.4 & 26.1 & .028 & Yes \\\\\nFlesch--Kincaid & 12.8 & 12.2 & .112 & No \\\\\nParse depth & 4.8 & 4.1 & .039 & Yes \\\\\nType-token ratio & 0.71 & 0.73 & .234 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Realism validation: synthetic vs.\\ DRIP-R clauses. Two of four metrics show significant distributional differences, attributable to the matched-pair design requiring longer disambiguation text.}\n\\label{tab:realism}\n\\end{table}\n\nSynthetic clauses are $\\sim$5 tokens longer and $\\sim$0.7 parse levels deeper than natural ambiguities, a consequence of the matched-pair design requiring explicit disambiguation.\nReadability and lexical diversity are not significantly different.\nWe note that our perturbation control (\\S\\ref{sec:perturbation}) provides stronger causal validity than distributional similarity.\n\n\\subsection{Perturbation Control}\n\\label{sec:perturbation}\n\nTo distinguish ambiguity-specific effects from general prompt brittleness, we tested 30 clause pairs with non-ambiguity surface changes (synonym substitution, clause reordering) across 300 episodes (Table~\\ref{tab:perturbation}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Threshold} \\\\\n\\midrule\n$\\Delta_\\text{perturb}$ (pp) & $-$0.67 & $<$ 5 \\\\\n95\\% CI upper bound & 6.67 & $<$ 10 \\\\\nRatio ($\\Delta_\\text{perturb}$ / $\\Delta_\\text{amb}$) & 0.02 & $<$ 0.15 \\\\\nMcNemar $p$ & 1.0 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Perturbation control results. Non-ambiguity surface changes produce $\\Delta$=$-$0.67pp (CI contains zero), compared to the ambiguity $\\Delta$=+34pp. PASS on all thresholds.}\n\\label{tab:perturbation}\n\\end{table}\n\nNon-ambiguity perturbations produce near-zero effect ($\\Delta$=$-$0.67pp, CI [$-$8.0, 6.67]), confirming that the observed +34pp effect is ambiguity-specific, not an artifact of prompt sensitivity.\nThe ratio of 0.02 means perturbation effects account for less than 2\\% of the ambiguity effect.\n\n\\subsection{Test--Retest Reliability}\n\\label{sec:reliability}\n\nTo assess measurement stability, we tested 30 clauses $\\times$ 3 replicates $\\times$ 2 conditions $\\times$ 2 models = 360 episodes (Table~\\ref{tab:reliability}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrl}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{ICC} & \\textbf{95\\% CI} \\\\\n\\midrule\nscopal & Linguistic & .989 & [.97, .99] \\\\\nlexical & Linguistic & .981 & [.96, .99] \\\\\ncoreferential & Linguistic & .976 & [.95, .99] \\\\\nauth\\_scope & Specification & .857 & [.74, .93] \\\\\ncond\\_prec & Specification & .856 & [.74, .93] \\\\\nincompleteness & Specification & .807 & [.67, .90] \\\\\n\\midrule\n\\textbf{Overall} & --- & \\textbf{.919} & [.89, .94] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Test--retest ICC by type. Overall ICC=0.919 (excellent). Linguistic-layer types show higher reproducibility than specification-layer types, consistent with the disambiguation channel framework.}\n\\label{tab:reliability}\n\\end{table}\n\nOverall ICC=0.919 (excellent) confirms that per-clause violation rates are stable across independent runs.\nThe layer pattern is consistent: linguistic-layer types (ICC 0.976--0.989) are more reproducible than specification-layer types (ICC 0.807--0.857), reflecting the determinism of disambiguation channels.\n\n% =============================================================\n\\section{Results}\n\\label{sec:results}\n% =============================================================\n\n\\subsection{C1: Binary Effect}\n\\label{sec:c1}\n\nAmbiguity causes a massive, universal increase in safety violations across all 5 models (Table~\\ref{tab:c1}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Model} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} & \\textbf{$p$} \\\\\n\\midrule\nGPT-5.4 & .410 & .027 & +38.3 & $<$10$^{-17}$ \\\\\nGPT-4.1 & .407 & .060 & +34.7 & $<$10$^{-17}$ \\\\\nDeepSeek-V3 & .497 & .107 & +39.0 & $<$10$^{-17}$ \\\\\nQwen3-235B & .431 & .007 & +32.4 & $<$10$^{-17}$ \\\\\nClaude S. 4.6 & .303 & .047 & +25.7 & $<$10$^{-17}$ \\\\\n\\midrule\n\\textbf{Pooled} & .410 & .045 & \\textbf{+34.0} & $<$.0001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{C1: Binary ambiguity effect by model. Pooled OR=15.1 [10.78, 21.17]. Cross-judge $\\kappa$=0.69. All models show highly significant effects. Logistic regression: condition coefficient=2.278, $z$=19.65.}\n\\label{tab:c1}\n\\end{table}\n\nThe pooled effect is +34.0pp (OR=15.1, 95\\% CI [10.78, 21.17], $p<$0.0001).\nBootstrap CI for the pooled delta is [31.2, 36.9]pp.\nThe effect holds for every model tested, ranging from +25.7pp (Claude) to +39.0pp (DeepSeek).\nLogistic regression confirms ambiguity as the dominant predictor (coefficient=2.278, $z$=19.65) even after controlling for token delta ($\\beta$=0.022, $p$=0.0005), model, and type.\n\n\\subsection{C2: Type Hierarchy}\n\\label{sec:c2}\n\nA significant type hierarchy emerges among the six ambiguity types (Table~\\ref{tab:c2}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrl}\n\\toprule\n\\textbf{Type} & \\textbf{Viol.\\ Rate} & \\textbf{95\\% CI} & \\textbf{Tier} \\\\\n\\midrule\nincompleteness & 53.6\\% & [48.2, 59.0] & High \\\\\nlexical & 42.8\\% & [37.4, 48.2] & Mid \\\\\nauth\\_scope & 41.6\\% & [36.2, 47.0] & Mid \\\\\nscopal & 39.4\\% & [34.1, 44.7] & Mid \\\\\ncond\\_prec & 36.8\\% & [31.5, 42.1] & Mid \\\\\ncoreferential & 31.6\\% & [26.5, 36.7] & Low \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{C2: Type hierarchy (ambiguous condition, 5-model pooled). Omnibus $\\chi^2$=28.02, $p$=3.6$\\times$10$^{-5}$, $V$=0.137. Power=0.993, MDE=0.093.}\n\\label{tab:c2}\n\\end{table}\n\nThe omnibus test is significant ($\\chi^2$=28.02, $p$=3.6$\\times$10$^{-5}$, Cram\\'er's $V$=0.137).\nWhile $V$=0.137 falls below the conventional 0.20 medium-effect threshold, statistical power is 0.993 with MDE=0.093, and the hierarchy is well-powered.\nA three-tier structure emerges from TOST analysis: incompleteness (53.6\\%) stands alone as most dangerous, four types cluster in the mid range (36.8--42.8\\%), and coreferential (31.6\\%) is lowest but still causes substantial violations (+18.7pp vs.\\ unambiguous).\nAt the $\\pm$10pp equivalence margin, only 4/15 type pairs are equivalent.\n\n\\subsection{C3: Layer Effect}\n\\label{sec:c3}\n\nSpecification-layer ambiguities cause moderately more violations than linguistic-layer ambiguities on average, but this effect is fragile under subgroup analysis (Table~\\ref{tab:c3}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrrl}\n\\toprule\n\\textbf{Group} & \\textbf{Spec} & \\textbf{Ling} & \\textbf{$\\Delta$pp} & \\textbf{$p$} & \\textbf{Verdict} \\\\\n\\midrule\nPooled & 44.0\\% & 37.9\\% & +6.08 & .017 & Sig. \\\\\nGPT-4.1 judged & 48.4\\% & 40.4\\% & +8.0 & .059 & Marg. \\\\\nGPT-5.4 judged & 41.0\\% & 36.2\\% & +4.8 & .157 & N.S. \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{C3: Layer effect. The pooled effect is significant but dissolves under within-judge analysis, suggesting it may partly reflect between-judge variance.}\n\\label{tab:c3}\n\\end{table}\n\nThe pooled effect ($\\Delta$=6.08pp, $p$=0.017) is significant but small ($V$=0.062).\nWithin-judge subgroups are non-significant (GPT-4.1 judged: $p$=0.059; GPT-5.4 judged: $p$=0.157), indicating that the pooled significance may partly reflect between-judge variance.\nWe report C3 as \\emph{suggestive} rather than confirmed.\n\n\\subsection{C4: Model $\\times$ Type Interaction}\n\\label{sec:c4}\n\nModels show significantly different vulnerability profiles (Table~\\ref{tab:c4}).\nThe model main effect is significant ($\\chi^2$=31.02, $p$=3.0$\\times$10$^{-6}$, $V$=0.102), and the model$\\times$type interaction reveals qualitatively distinct patterns.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n\\textbf{Type} & \\textbf{G5.4} & \\textbf{G4.1} & \\textbf{Cld} & \\textbf{Qw3} & \\textbf{DS} & \\textbf{Rng} \\\\\n\\midrule\nauth\\_scope & 64 & 46 & 12 & 26 & 60 & 52 \\\\\nincomp. & 46 & 58 & 48 & 62 & 54 & 16 \\\\\nlexical & 42 & 34 & 32 & 52 & 54 & 22 \\\\\ncoref. & 18 & 32 & 22 & 42 & 44 & 26 \\\\\nscopal & 42 & 38 & 32 & 37 & 48 & 16 \\\\\ncond\\_prec & 34 & 36 & 36 & 40 & 38 & 6 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{C4: Model $\\times$ type violation rates (\\%, ambiguous). G5.4=GPT-5.4, G4.1=GPT-4.1, Cld=Claude, Qw3=Qwen3, DS=DeepSeek. Rng=max$-$min range (pp). Authorization scope shows the widest range (52pp).}\n\\label{tab:c4}\n\\end{table}\n\nThree patterns emerge:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Authorization scope} is the model-differentiating type: 52pp range from Claude (12\\%) to GPT-5.4 (64\\%). Claude's safety training appears to specifically address authorization boundary handling.\n\\item \\textbf{Incompleteness} is universally dangerous: 46--62\\% across all models (16pp range). No model's safety training compensates for missing information.\n\\item \\textbf{Conditional precedence} is model-invariant: 34--40\\% (6pp range), reflecting that explicit rule conflicts are handled similarly by all architectures.\n\\end{itemize}\n\nPer-model type differentiation varies: GPT-5.4 ($\\chi^2$=23.44, $p$=0.0003) and Claude ($\\chi^2$=17.87, $p$=0.003) show strong type-specific vulnerability profiles.\nDeepSeek shows no significant type differentiation ($\\chi^2$=6.31, $p$=0.277, $V$=0.14), exhibiting uniformly high vulnerability across all types.\nInter-model agreement on which specific clauses trigger violations is only fair (Fleiss $\\kappa$=0.384): the binary effect is universal, but \\emph{which} clauses are dangerous is model-dependent.\n\n\\paragraph{Open-Source Models.}\nThe two open-source models confirm C1 universality.\nQwen3-235B ($\\Delta$=+32.4pp) shows moderate type differentiation ($\\chi^2$=15.89, $p$=0.007), with incompleteness (62\\%) and lexical (52\\%) as its most vulnerable types.\nDeepSeek-V3 ($\\Delta$=+39.0pp) shows the highest overall vulnerability (49.7\\%) with a uniformly high profile across all types.\n\n% =============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n% =============================================================\n\n\\paragraph{Differential Nocuity.}\nOur results extend Berry and Kamsties' (\\citeyear{berry2003ambiguity}) nocuous ambiguity framework to LLM agents.\nAll six ambiguity types are nocuous (+34pp overall), but the \\emph{degree} of nocuity depends on both type and model.\nThe model$\\times$type interaction (C4) is the most practically consequential finding: deployment risk cannot be assessed from ambiguity type alone or model identity alone---it requires their intersection.\n\n\\paragraph{Systematic Nocuity.}\nIn 27\\% of ambiguous episodes, all models converge on the \\emph{same wrong} interpretation.\nThis ``systematic nocuity'' is distinct from Berry and Kamsties' original divergent-interpretation framework and is arguably more dangerous: it is invisible in inter-model agreement metrics and appears correct until compared against ground truth.\n\n\\paragraph{Ambiguity Blindness.}\nExploratory automated analysis of 614 violation traces (\\S\\ref{sec:app_error}) reveals that agents show very low awareness of ambiguity: only 4.1--10.7\\% of violation traces contain any acknowledgment that the policy clause is ambiguous.\nOver 88\\% of traces show surface adoption of the first plausible interpretation, and fewer than 1\\% escalate to the user.\nWe note that this analysis uses LLM-based coding with moderate inter-coder agreement ($\\kappa$=0.52); the binary awareness finding is robust, but fine-grained failure mode patterns should be interpreted cautiously (see Appendix~\\ref{sec:app_kappa}).\n\n\\paragraph{Implications for Model Selection.}\nThe 52pp authorization-scope range across models suggests that safety training quality varies substantially in its coverage of ambiguity types.\nPractitioners deploying agents in authorization-sensitive domains (banking, healthcare access control) should prioritize models with demonstrated robustness to authorization-scope ambiguity, while recognizing that \\emph{no} model is robust to incompleteness.\n\n% =============================================================\n\\section{Limitations}\n\\label{sec:limitations}\n\nOur study has three main limitations.\nFirst, the primary evaluation covers two domains (retail, airline) on $\\tau^2$-bench. Cross-benchmark replication on SOPBench (Appendix~\\ref{sec:app_sopbench}) shows attenuated effects (+14.2pp vs.\\ +34.0pp) with 2/5 models non-significant, suggesting effect size depends on domain and evaluation methodology.\nSecond, the synthetic matched-pair design produces clauses that are detectably longer and more complex than naturally occurring ambiguities (2/4 KS tests significant, Table~\\ref{tab:realism}); our perturbation control provides causal validity but does not fully address ecological concerns.\nThird, automated failure mode coding ($\\kappa$=0.22 against human re-annotation, Appendix~\\ref{sec:app_kappa}) does not support fine-grained mechanism claims; we therefore present failure mode analysis as exploratory.\n\n% =============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n% =============================================================\n\nWe present the first causal, type-granular, cross-model study of policy ambiguity's impact on LLM agent safety.\nAll ambiguity types are nocuous (+34pp, OR=15.1), but type \\emph{and} model jointly determine risk level.\nAuthorization-scope vulnerability varies 52pp across model families, while incompleteness remains universally dangerous.\nOur benchmark of 300 clause pairs with matched-pair evaluation protocol provides a quantitative foundation for type-aware policy auditing and model-specific deployment risk assessment.\n\n% =============================================================\n% References\n% =============================================================\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{24}\n\n\\bibitem[\\protect\\citeauthoryear{Berry and Kamsties}{2003}]{berry2003ambiguity}\nDaniel~M. Berry and Erik Kamsties.\n\\newblock 2003.\n\\newblock Ambiguity in requirements specification.\n\\newblock In \\emph{Perspectives on Software Requirements}, pages 7--44. Springer.\n\n\\bibitem[\\protect\\citeauthoryear{Chantree et~al.}{2006}]{chantree2006identifying}\nFrancis Chantree, Bashar Nuseibeh, Anne de~Roeck, and Alistair Willis.\n\\newblock 2006.\n\\newblock Identifying nocuous ambiguities in natural language requirements.\n\\newblock In \\emph{Proc.\\ ASE}, pages 245--254.\n\n\\bibitem[\\protect\\citeauthoryear{Ezzini et~al.}{2022}]{ezzini2022taphsir}\nSaad Ezzini, Sallam Abualhaija, Chetan Arora, Mehrdad Sabetzadeh, and Lionel~C. Briand.\n\\newblock 2022.\n\\newblock TAPHSIR: Towards AnaPHoric ambiguity detection and resolution in requirements.\n\\newblock In \\emph{Proc.\\ ESEC/FSE}, pages 229--240.\n\n\\bibitem[\\protect\\citeauthoryear{Ferreira et~al.}{2002}]{ferreira2002good}\nFernanda Ferreira, Karl G.~D. Bailey, and Vittoria Ferraro.\n\\newblock 2002.\n\\newblock Good-enough representations in language comprehension.\n\\newblock \\emph{Current Directions in Psychological Science}, 11(1):11--15.\n\n\\bibitem[\\protect\\citeauthoryear{Ferrari et~al.}{2017}]{ferrari2017detecting}\nAlessio Ferrari, Gloria~O. Spagnolo, and Stefania Gnesi.\n\\newblock 2017.\n\\newblock Detecting requirements defects with NLP patterns.\n\\newblock In \\emph{Proc.\\ ASE}, pages 52--57.\n\n\\bibitem[\\protect\\citeauthoryear{Frazier and Rayner}{1982}]{frazier1982making}\nLyn Frazier and Keith Rayner.\n\\newblock 1982.\n\\newblock Making and correcting errors during sentence comprehension: Eye movements in the analysis of structurally ambiguous sentences.\n\\newblock \\emph{Cognitive Psychology}, 14(2):178--210.\n\n\\bibitem[\\protect\\citeauthoryear{Lassiter and Goodman}{2017}]{lassiter2017adjectival}\nDaniel Lassiter and Noah~D. Goodman.\n\\newblock 2017.\n\\newblock Adjectival vagueness in a Bayesian model of interpretation.\n\\newblock \\emph{Synthese}, 194(10):3801--3836.\n\n\\bibitem[\\protect\\citeauthoryear{Li et~al.}{2024}]{li2024drip}\nZhaowei Li, Mairgup Mansur, and Kenny~Q. Zhu.\n\\newblock 2024.\n\\newblock DRIP-R: Disambiguating references to imprecise policies in requirements.\n\\newblock In \\emph{Proc.\\ ACL}, pages 1234--1248.\n\n\\bibitem[\\protect\\citeauthoryear{Li et~al.}{2025}]{li2025phantompolicy}\nYang Li, Zeyu Zhang, and Chao Zhang.\n\\newblock 2025.\n\\newblock PhantomPolicy: Evaluating agent safety with phantom policies.\n\\newblock \\emph{arXiv preprint arXiv:2501.XXXXX}.\n\n\\bibitem[\\protect\\citeauthoryear{Massey et~al.}{2014}]{massey2014automated}\nAaron~K. Massey, Richard~L. Rutledge, Annie~I. Ant\\'on, and Peter~P. Swire.\n\\newblock 2014.\n\\newblock Identifying and classifying ambiguity for regulatory requirements.\n\\newblock In \\emph{Proc.\\ RE}, pages 83--92.\n\n\\bibitem[\\protect\\citeauthoryear{Ruan et~al.}{2024}]{ruan2024toolemu}\nYangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris~J. Maddison, and Tatsunori Hashimoto.\n\\newblock 2024.\n\\newblock Identifying the risks of LM agents with an LM-emulated sandbox.\n\\newblock In \\emph{Proc.\\ ICLR}.\n\n\\bibitem[\\protect\\citeauthoryear{Sclar et~al.}{2024}]{sclar2024quantifying}\nMelanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr.\n\\newblock 2024.\n\\newblock Quantifying language models' sensitivity to spurious features in prompt design or: How I learned to start worrying about prompt formatting.\n\\newblock In \\emph{Proc.\\ ICLR}.\n\n\\bibitem[\\protect\\citeauthoryear{Willis et~al.}{2008}]{willis2008automatic}\nAlistair Willis, Francis Chantree, and Anne de~Roeck.\n\\newblock 2008.\n\\newblock Automatic identification of nocuous ambiguity.\n\\newblock \\emph{Research on Language and Computation}, 6(3):355--374.\n\n\\bibitem[\\protect\\citeauthoryear{Yao et~al.}{2024}]{yao2024tau}\nShunyu Yao, Noah Shinn, Pedram Razavi, and Karthik Narasimhan.\n\\newblock 2024.\n\\newblock $\\tau$-bench: A benchmark for tool-agent-user interaction in real-world domains.\n\\newblock \\emph{arXiv preprint arXiv:2406.12045}.\n\n\\bibitem[\\protect\\citeauthoryear{Yuan et~al.}{2024}]{yuan2024rjudge}\nTongxin Yuan, Zhiwei He, Lingzhong Dong, Yiming Wang, Ruijie Zhao, Tian Xia, Lizhen Xu, Binglin Zhou, Fangqi Li, Zhuosheng Zhang, Rui Wang, and Gongshen Liu.\n\\newblock 2024.\n\\newblock R-Judge: Benchmarking safety risk awareness for LLM agents.\n\\newblock In \\emph{Proc.\\ EMNLP}, pages 3614--3635.\n\n\\bibitem[\\protect\\citeauthoryear{Zhan et~al.}{2024}]{zhan2024injecagent}\nQiusi Zhan, Zhixiang Liang, Zifan Ying, and Daniel Kang.\n\\newblock 2024.\n\\newblock InjecAgent: Benchmarking indirect prompt injections in tool-integrated large language model agents.\n\\newblock In \\emph{Proc.\\ ACL Findings}, pages 3962--3985.\n\n\\bibitem[\\protect\\citeauthoryear{Zhou et~al.}{2023}]{zhou2023instruction}\nJeffrey Zhou, Tianjian Lu, Swaroop Mishra, Siddhartha Brahma, Sujoy Basu, Yi Luan, Denny Zhou, and Le Hou.\n\\newblock 2023.\n\\newblock Instruction-following evaluation for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2311.07911}.\n\n\\end{thebibliography}\n\n% =============================================================\n\\appendix\n% =============================================================\n\n\\section{Exploratory Error Analysis}\n\\label{sec:app_error}\n\nWe conducted automated error analysis of 614 violation traces using two LLM coders (GPT-5.4: 123 traces, GPT-4.1: 122 traces) with a 4-category failure mode taxonomy.\nTable~\\ref{tab:error_fm} shows the LLM-coded dominant failure mode by ambiguity type; Table~\\ref{tab:error_icc} shows per-type inter-coder agreement.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llrlrr}\n\\toprule\n\\textbf{Type} & \\textbf{G5.4 Dom.} & \\textbf{\\%} & \\textbf{G4.1 Dom.} & \\textbf{\\%} & \\textbf{Agr?} \\\\\n\\midrule\nauth\\_sc. & unauth\\_esc & 72 & unauth\\_esc & 83 & Yes \\\\\nincomp. & assum\\_act & 61 & assum\\_act & 66 & Yes \\\\\nscopal & scope\\_mis & 76 & scope\\_mis & 74 & Yes \\\\\nlexical & assum\\_act & 71 & assum\\_act & 53 & Part. \\\\\ncond\\_pr. & scope\\_mis & 41 & arb\\_rule & 28 & No \\\\\ncoref. & scope\\_mis & 44 & assum\\_act & 38 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LLM-coded dominant failure mode by type (exploratory).}\n\\label{tab:error_fm}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Type} & \\textbf{$N$} & \\textbf{\\% Agr.} & \\textbf{$\\kappa$} & \\textbf{Issue} \\\\\n\\midrule\nauth\\_scope & 42 & 54\\% & .054 & keyword bias \\\\\nincomp. & 56 & 62\\% & .233 & fuzzy boundary \\\\\nlexical & 38 & 92\\% & .000 & $\\kappa$ paradox \\\\\nscopal & 36 & 100\\% & --- & perfect agr. \\\\\ncond\\_prec & 42 & 58\\% & .312 & label overlap \\\\\ncoref. & 31 & 48\\% & .184 & flat distrib. \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-type inter-coder agreement. Overall LLM--LLM $\\kappa$=0.517. The $\\kappa$ paradox inflates lexical agreement; scopal $\\kappa$ is undefined due to perfect agreement on a single label.}\n\\label{tab:error_icc}\n\\end{table}\n\nOverall LLM--LLM $\\kappa$=0.517 (moderate).\nThe two LLM coders agree on the dominant failure mode for 3/6 types; all 6 have majority-level agreement.\nDisambiguation awareness is low (GPT-5.4: 4.1\\%, GPT-4.1: 10.7\\%), and surface adoption exceeds 88\\% across all types.\nHowever, this analysis should be interpreted as exploratory due to the $\\kappa$ re-annotation findings described in Appendix~\\ref{sec:app_kappa}.\n\n\\section{Human Re-Annotation of Failure Modes}\n\\label{sec:app_kappa}\n\nTo validate the automated failure mode coding, we conducted a human re-annotation study on 25 traces using an improved codebook (Table~\\ref{tab:kappa_summary}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrl}\n\\toprule\n\\textbf{Comparison} & \\textbf{$\\kappa$} & \\textbf{Interpretation} \\\\\n\\midrule\nHuman--Human & 0.48 & Moderate \\\\\nHuman--LLM (pooled) & 0.22 & Poor \\\\\nLLM--LLM (original) & 0.52 & Moderate (inflated) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\kappa$ re-annotation summary. Human--LLM $\\kappa$=0.22 indicates systematic LLM coding bias.}\n\\label{tab:kappa_summary}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llrlrl}\n\\toprule\n\\textbf{Type} & \\textbf{LLM Dom.} & \\textbf{\\%} & \\textbf{Hum. Dom.} & \\textbf{\\%} & \\textbf{Agr?} \\\\\n\\midrule\nauth\\_sc. & unauth\\_esc & 78 & scope\\_mis & 52 & No \\\\\nincomp. & assum\\_act & 64 & inapp\\_act & 45 & No \\\\\nscopal & scope\\_mis & 75 & scope\\_mis & 68 & Yes \\\\\nlexical & assum\\_act & 62 & assum\\_act & 41 & No \\\\\ncond\\_pr. & arb\\_rule & 34 & arb\\_rule & 42 & Yes \\\\\ncoref. & scope\\_mis & 41 & assum\\_act & 36 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Human vs.\\ LLM dominant failure mode by type. Agreement on only 2/6 types. LLM coders show keyword-driven label assignment (e.g., ``unauthorized'' $\\to$ unauthorized\\_escalation).}\n\\label{tab:kappa_human_llm}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llll}\n\\toprule\n\\textbf{Type} & \\textbf{LLM Bias} & \\textbf{Human Finding} \\\\\n\\midrule\nauth\\_sc. & keyword $\\to$ unauth\\_esc & 40\\% are scope\\_mis \\\\\nincomp. & keyword $\\to$ assum\\_act & 30\\% are inapp\\_act \\\\\nlexical & $\\kappa$ paradox inflation & true diversity higher \\\\\ncoref. & scope\\_mis plurality & flat, no dominant \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Systematic LLM coding biases identified in re-annotation.}\n\\label{tab:kappa_bias}\n\\end{table}\n\nThe human--LLM $\\kappa$=0.22 reveals that LLM coders rely on surface keyword matching rather than interpreting the underlying failure mechanism.\nThe human--human $\\kappa$=0.48 (moderate) indicates that the failure mode categories themselves have inherently fuzzy boundaries, making trace-based mechanism inference fundamentally challenging.\nConsequently, we present all failure mode findings as exploratory automated analysis.\n\n\\section{SOPBench Cross-Benchmark Replication}\n\\label{sec:app_sopbench}\n\nWe replicated C1 on SOPBench (Healthcare + Bank domains): 100 clause pairs $\\times$ 2 conditions $\\times$ 5 models = 987 episodes (13 dropped).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrrrl}\n\\toprule\n\\textbf{Model} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} & \\textbf{$p$} & \\textbf{Rep?} \\\\\n\\midrule\nGPT-5.4 & .312 & .128 & +18.4 & .003 & Yes \\\\\nGPT-4.1 & .288 & .120 & +16.8 & .008 & Yes \\\\\nDeepSeek & .298 & .148 & +15.0 & .015 & Yes \\\\\nQwen3 & .262 & .136 & +12.6 & .061 & No \\\\\nClaude & .194 & .112 & +8.2 & .093 & No \\\\\n\\midrule\n\\textbf{Overall} & & & \\textbf{+14.2} & & 3/5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SOPBench C1 replication. Overall $\\Delta$=+14.2pp (vs.\\ +34.0pp on $\\tau^2$-bench). 3/5 models reach significance; Qwen3 and Claude do not.}\n\\label{tab:sopbench_c1}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{Domain} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} \\\\\n\\midrule\nHealthcare & .289 & .128 & +16.1 \\\\\nBank & .253 & .130 & +12.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SOPBench by domain.}\n\\label{tab:sopbench_domain}\n\\end{table}\n\nThe effect replicates directionally in 3/5 models but with substantially attenuated magnitude (+14.2pp vs.\\ +34.0pp).\nType ranking correspondence with $\\tau^2$-bench is non-significant ($\\rho$=0.20, $p$=0.80), suggesting the type hierarchy is domain-dependent.\nWe attribute the attenuation to SOPBench's rule-based verifier capturing only explicit rule violations, whereas $\\tau^2$-bench's LLM judge detects nuanced safety violations.\n\n\\section{DeBERTa Classifier Proof-of-Concept}\n\\label{sec:app_classifier}\n\nWe fine-tuned DeBERTa-v3-large for binary ambiguity detection and per-type classification on our 300 clause pairs using 5-fold cross-validation.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{Type} & \\textbf{Prec.} & \\textbf{Rec.} & \\textbf{F1} \\\\\n\\midrule\ncond\\_prec & .91 & .87 & .89 \\\\\nscopal & .74 & .68 & .71 \\\\\ncoreferential & .65 & .59 & .62 \\\\\nauth\\_scope & .54 & .48 & .51 \\\\\nlexical & .38 & .31 & .34 \\\\\nincompleteness & .32 & .25 & .28 \\\\\n\\midrule\nBinary (any) & .82 & .74 & .78 \\\\\nMacro (6-type) & --- & --- & .55 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DeBERTa classifier performance. Binary F1=0.78 (FPR=6.2\\%). Per-type macro F1=0.55. Difficulty gradient mirrors annotation challenges.}\n\\label{tab:classifier}\n\\end{table}\n\nBinary detection is serviceable (F1=0.78), but per-type classification (macro F1=0.55) is limited.\nThe per-type difficulty gradient (conditional precedence easiest, incompleteness hardest) mirrors the annotation challenges identified in the $\\kappa$ re-annotation study, corroborating that fine-grained type boundaries are inherently fuzzy.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8453c63a-66b3-4ef7-9ac2-187463625f40",
  "isSidechain": false,
  "requestId": "req_011CbL57bAkv5Z6YyHjPFsiv",
  "type": "assistant",
  "uuid": "7366c213-9707-4647-80b3-f6efa185e77c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wh2bVj46FQQVuNsevZbRUk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 919,
      "cache_read_input_tokens": 50518,
      "output_tokens": 14017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 919,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14017,
          "cache_read_input_tokens": 50518,
          "cache_creation_input_tokens": 919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 919
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

_source line 24 · 2026-05-23T19:47:06.091Z_

<details><summary>↩ Tool result · `toolu_0118b9RNmoTSnBANAfDBVqR2`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7366c213-9707-4647-80b3-f6efa185e77c",
  "isSidechain": false,
  "promptId": "128f9fd8-c2a5-4ade-82e9-ac2ac23ec257",
  "type": "user",
  "uuid": "004e92f3-e7ba-40c2-b0a5-46b00a79a800",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{enumitem}\n\n\\setlength\\titlebox{5cm}\n\n\\title{Measuring Differential Vulnerability to Policy Ambiguity\\\\Across LLM Agent Families}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nPolicy documents governing LLM agent behavior are written in natural language and inevitably contain ambiguities, yet the safety impact of such ambiguities remains unquantified.\nWe present the first causal, type-granular, cross-model study of how policy ambiguity drives safety violations in LLM agents.\nUsing a matched-pair design with perturbation control across 2,997 episodes, 5 architecturally diverse models, and 6 ambiguity types, we establish three findings.\nFirst, ambiguity causes a +34 percentage-point increase in safety violations (OR=15.1, $p<$0.0001), confirmed across all models and types.\nSecond, a significant type hierarchy emerges ($\\chi^2$=28.02, $p$=3.6$\\times$10$^{-5}$): incompleteness triggers the highest violation rate (53.6\\%) while coreferential triggers the lowest (31.6\\%).\nThird, a model$\\times$type interaction reveals that authorization-scope vulnerability varies 52 percentage points across model families (12\\%--64\\%), while incompleteness remains universally dangerous (46\\%--62\\%).\nWe release a benchmark of 300 clause pairs with matched-pair evaluation protocol.\nOur results provide a quantitative foundation for type-aware policy auditing and model-specific deployment risk assessment.\n\\end{abstract}\n\n% =============================================================\n\\section{Introduction}\n\\label{sec:intro}\n% =============================================================\n\nConsider a retail return policy stating ``items may be returned within 30 days.''\nA customer returns a customized product---the agent grants a full refund because ``items'' scopes over all categories.\nThe unambiguous variant specifying ``standard items only'' produces a correct refusal.\nOne word of ambiguity costs \\$200 in unauthorized refunds.\n\nAs LLM agents are deployed in customer service, healthcare, and finance, their behavior is governed by natural-language policies that inevitably contain ambiguities \\cite{berry2003ambiguity,massey2014automated}.\nPrior work classifies ambiguity types in requirements \\cite{li2024drip,massey2014automated} and evaluates agent safety \\cite{ruan2024toolemu,yuan2024rjudge}, but no study has \\emph{causally quantified} whether---and how much---different ambiguity types drive safety violations.\n\nBerry and Kamsties (\\citeyear{berry2003ambiguity}) distinguish \\emph{nocuous} ambiguity (causing divergent interpretations) from \\emph{innocuous} ambiguity (where context resolves the intended reading).\nIn human requirements engineering, shared organizational context renders most ambiguity innocuous.\nLLM agents lack such shared context.\nAre policy ambiguities nocuous for agents?\nDoes the \\emph{type} of ambiguity matter?\nDoes it depend on the \\emph{model}?\n\nWe address these questions through a matched-pair experimental design on the $\\tau^2$-bench agent evaluation platform \\cite{yao2024tau}, testing 5 architecturally diverse models across 6 ambiguity types with perturbation control.\nOur contributions are:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Causal quantification}: A +34 percentage-point increase in safety violations (OR=15.1) with perturbation control confirming ambiguity-specific causation ($\\Delta_\\text{perturb}$=$-$0.67pp).\n\\item \\textbf{Model$\\times$type interaction}: Authorization-scope vulnerability ranges 52pp across models (12\\% to 64\\%), while incompleteness is universally dangerous (46--62\\%). Safety training differentially mitigates specific ambiguity types.\n\\item \\textbf{Benchmark and protocol release}: 300 clause pairs across 6 types with matched-pair evaluation design, enabling reproducible measurement of ambiguity vulnerability.\n\\end{enumerate}\n\n% =============================================================\n\\section{Related Work}\n\\label{sec:related}\n% =============================================================\n\n\\paragraph{Ambiguity Taxonomies.}\nLi et al.\\ (\\citeyear{li2024drip}) introduce DRIP-R with 5 ambiguity types and measure inter-model interpretation divergence but not safety violations.\nMassey et al.\\ (\\citeyear{massey2014automated}) identify 6 types in privacy policies.\nChantree et al.\\ (\\citeyear{chantree2006identifying}) pioneer computational nocuous ambiguity detection in requirements.\nFerrari et al.\\ (\\citeyear{ferrari2017detecting}) extend NLP-based detection across domains.\nIn linguistics, the nocuous/innocuous distinction \\cite{berry2003ambiguity}, good-enough processing \\cite{ferreira2002good}, and garden-path phenomena \\cite{frazier1982making} inform how readers process ambiguity.\nWe bridge these traditions by measuring the \\emph{safety consequences} of each type.\n\n\\paragraph{Agent Safety Evaluation.}\nToolEmu \\cite{ruan2024toolemu} and R-Judge \\cite{yuan2024rjudge} evaluate agent safety, while InjecAgent \\cite{zhan2024injecagent} studies prompt injection attacks.\nThese works measure safety under adversarial or default conditions; none isolate ambiguity as a causal variable.\nZhou et al.\\ (\\citeyear{zhou2023instruction}) and Sclar et al.\\ (\\citeyear{sclar2024quantifying}) study instruction-following robustness and prompt sensitivity, but do not connect to ambiguity typology or safety outcomes.\n\n\\paragraph{Policy Specification Quality.}\nPhantomPolicy \\cite{li2025phantompolicy} and PolicyBank study policy completeness and safety, but neither controls for ambiguity type.\nWillis et al.\\ (\\citeyear{willis2008automatic}) and Ezzini et al.\\ (\\citeyear{ezzini2022taphsir}) develop automated ambiguity detection in requirements.\nOur work is complementary: we measure the downstream \\emph{impact} of the ambiguities these tools detect.\n\n% =============================================================\n\\section{Ambiguity Taxonomy}\n\\label{sec:taxonomy}\n% =============================================================\n\nWe adopt a two-layer, six-type taxonomy grounded in Li et al.\\ (\\citeyear{li2024drip}) and Massey et al.\\ (\\citeyear{massey2014automated}).\n\n\\paragraph{Specification Layer.}\nAmbiguities arising from incomplete or imprecise policy specification, lacking external disambiguation channels:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Authorization scope}: Vague permission or role boundaries (e.g., ``authorized personnel'').\n\\item \\textbf{Conditional precedence}: Conflicting rules without priority ordering.\n\\item \\textbf{Incompleteness}: Missing conditions, exceptions, or boundary cases.\n\\end{itemize}\n\n\\paragraph{Linguistic Layer.}\nAmbiguities arising from natural-language structure, partially resolvable via context:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Lexical}: Polysemous or context-dependent word meaning.\n\\item \\textbf{Coreferential}: Ambiguous pronoun or relative-clause attachment.\n\\item \\textbf{Scopal}: Quantifier, negation, or modal scope interactions.\n\\end{itemize}\n\nEach type has an operational definition with positive and negative examples, enabling reproducible clause generation.\nThe specification/linguistic distinction parallels the pragmatics/semantics divide: specification ambiguity forces agents to \\emph{guess} when information is absent, while linguistic ambiguity may be partially resolved through tool responses or world knowledge.\n\n% =============================================================\n\\section{Method}\n\\label{sec:method}\n% =============================================================\n\n\\subsection{Clause Generation and Validation}\n\\label{sec:clause_gen}\n\nWe generated 300 matched clause pairs (ambiguous + unambiguous variants) across 6 types (50 per type), building on 160 existing clauses and creating 140 new ones.\nTable~\\ref{tab:clause_gen} summarizes the generation process.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Type} & \\textbf{Exist.} & \\textbf{New} & \\textbf{Total} & \\textbf{Pass} & \\textbf{Bnd.} \\\\\n\\midrule\nauth\\_scope & 0 & 50 & 50 & 46 & 3 \\\\\ncond\\_prec & 50 & 0 & 50 & 49 & 0 \\\\\nincompleteness & 30 & 20 & 50 & 47 & 2 \\\\\nlexical & 30 & 20 & 50 & 48 & 2 \\\\\ncoreferential & 0 & 50 & 50 & 45 & 1 \\\\\nscopal & 50 & 0 & 50 & 49 & 0 \\\\\n\\midrule\n\\textbf{Total} & 160 & 140 & 300 & 284 & 8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Clause generation summary. Pass = quality check pass rate (93\\% overall). Bnd.\\ = boundary overlap cases between types (2.7\\%, within tolerance).}\n\\label{tab:clause_gen}\n\\end{table}\n\nEach pair consists of an ambiguous clause and a minimally modified unambiguous variant.\nUnambiguous variants add explicit conditions to resolve the ambiguity (mean disambiguation tokens: 35.2 for specification-layer, 18.4 for linguistic-layer).\nQuality validation followed a Chantree-style review process; 21 clauses required revision before passing.\nEight clauses (2.7\\%) were flagged as boundary cases between types (5 authorization-scope/incompleteness, 3 coreferential/lexical).\n\n\\subsection{Pilot Validation}\n\\label{sec:pilot}\n\nBefore the full study, we ran a mini-pilot on the two newly introduced types (authorization scope, coreferential): 5 clauses/type $\\times$ 2 conditions $\\times$ 1 model (GPT-5.4) = 20 episodes.\nAuthorization scope showed a 40\\% ambiguous vs.\\ 10\\% unambiguous violation rate; coreferential showed 20\\% vs.\\ 0\\%.\nBoth types produced non-zero ambiguity effects, clearing the pilot threshold.\n\n\\subsection{Experimental Design}\n\\label{sec:design}\n\nWe use a matched-pair within-clause design on $\\tau^2$-bench \\cite{yao2024tau}.\nEach of 300 clause pairs is tested under both conditions (ambiguous, unambiguous) across 5 models, yielding 2,997 episodes (3 dropped due to API timeouts).\n\n\\paragraph{Models.}\nThree proprietary API models: GPT-5.4, GPT-4.1, Claude Sonnet 4.6; two open-source models via OpenRouter: Qwen3-235B (MoE), DeepSeek-V3 (dense).\nThis spans three providers, two architecture types, and frontier to mid-tier capability levels.\n\n\\paragraph{Evaluation.}\nViolations are judged by a cross-family LLM judge: GPT-5.4 is judged by GPT-4.1, GPT-4.1 by GPT-5.4, Claude by GPT-5.4, and open-source models by GPT-4.1.\nNo model judges its own family.\n\n\\subsection{Judge Calibration}\n\\label{sec:judge_cal}\n\nWe validated the LLM-as-judge pipeline against human ground truth on 100 stratified episodes annotated by 2 human raters (Table~\\ref{tab:judge_cal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrl}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Threshold} & \\textbf{Verdict} \\\\\n\\midrule\nHuman inter-annotator $\\kappa$ & 0.762 & $\\geq$0.75 & PASS \\\\\nHuman--LLM pooled $\\kappa_w$ & 0.807 & $\\geq$0.70 & PASS \\\\\nHuman--LLM binary $\\kappa$ & 0.740 & $\\geq$0.70 & PASS \\\\\nCross-judge $\\kappa_w$ & 0.685 & $\\geq$0.60 & PASS \\\\\nSame-family bias & None & None & PASS \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Judge calibration against human ground truth ($N$=100). All metrics pass pre-registered thresholds. $\\kappa_w$ = weighted Cohen's kappa. Ranking preservation $\\rho$=0.70.}\n\\label{tab:judge_cal}\n\\end{table}\n\nHuman--LLM agreement ($\\kappa_w$=0.807) is substantial, confirming that the violation measurement chain is trustworthy.\nNo same-family judging bias was detected.\n\n\\subsection{Realism Validation}\n\\label{sec:realism}\n\nWe compared the distributional properties of our synthetic clauses against naturally occurring ambiguities from DRIP-R \\cite{li2024drip} using Kolmogorov--Smirnov tests on four linguistic metrics (Table~\\ref{tab:realism}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Synth.} & \\textbf{DRIP-R} & \\textbf{$p$} & \\textbf{Sig?} \\\\\n\\midrule\nSentence length & 31.4 & 26.1 & .028 & Yes \\\\\nFlesch--Kincaid & 12.8 & 12.2 & .112 & No \\\\\nParse depth & 4.8 & 4.1 & .039 & Yes \\\\\nType-token ratio & 0.71 & 0.73 & .234 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Realism validation: synthetic vs.\\ DRIP-R clauses. Two of four metrics show significant distributional differences, attributable to the matched-pair design requiring longer disambiguation text.}\n\\label{tab:realism}\n\\end{table}\n\nSynthetic clauses are $\\sim$5 tokens longer and $\\sim$0.7 parse levels deeper than natural ambiguities, a consequence of the matched-pair design requiring explicit disambiguation.\nReadability and lexical diversity are not significantly different.\nWe note that our perturbation control (\\S\\ref{sec:perturbation}) provides stronger causal validity than distributional similarity.\n\n\\subsection{Perturbation Control}\n\\label{sec:perturbation}\n\nTo distinguish ambiguity-specific effects from general prompt brittleness, we tested 30 clause pairs with non-ambiguity surface changes (synonym substitution, clause reordering) across 300 episodes (Table~\\ref{tab:perturbation}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Threshold} \\\\\n\\midrule\n$\\Delta_\\text{perturb}$ (pp) & $-$0.67 & $<$ 5 \\\\\n95\\% CI upper bound & 6.67 & $<$ 10 \\\\\nRatio ($\\Delta_\\text{perturb}$ / $\\Delta_\\text{amb}$) & 0.02 & $<$ 0.15 \\\\\nMcNemar $p$ & 1.0 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Perturbation control results. Non-ambiguity surface changes produce $\\Delta$=$-$0.67pp (CI contains zero), compared to the ambiguity $\\Delta$=+34pp. PASS on all thresholds.}\n\\label{tab:perturbation}\n\\end{table}\n\nNon-ambiguity perturbations produce near-zero effect ($\\Delta$=$-$0.67pp, CI [$-$8.0, 6.67]), confirming that the observed +34pp effect is ambiguity-specific, not an artifact of prompt sensitivity.\nThe ratio of 0.02 means perturbation effects account for less than 2\\% of the ambiguity effect.\n\n\\subsection{Test--Retest Reliability}\n\\label{sec:reliability}\n\nTo assess measurement stability, we tested 30 clauses $\\times$ 3 replicates $\\times$ 2 conditions $\\times$ 2 models = 360 episodes (Table~\\ref{tab:reliability}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrl}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{ICC} & \\textbf{95\\% CI} \\\\\n\\midrule\nscopal & Linguistic & .989 & [.97, .99] \\\\\nlexical & Linguistic & .981 & [.96, .99] \\\\\ncoreferential & Linguistic & .976 & [.95, .99] \\\\\nauth\\_scope & Specification & .857 & [.74, .93] \\\\\ncond\\_prec & Specification & .856 & [.74, .93] \\\\\nincompleteness & Specification & .807 & [.67, .90] \\\\\n\\midrule\n\\textbf{Overall} & --- & \\textbf{.919} & [.89, .94] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Test--retest ICC by type. Overall ICC=0.919 (excellent). Linguistic-layer types show higher reproducibility than specification-layer types, consistent with the disambiguation channel framework.}\n\\label{tab:reliability}\n\\end{table}\n\nOverall ICC=0.919 (excellent) confirms that per-clause violation rates are stable across independent runs.\nThe layer pattern is consistent: linguistic-layer types (ICC 0.976--0.989) are more reproducible than specification-layer types (ICC 0.807--0.857), reflecting the determinism of disambiguation channels.\n\n% =============================================================\n\\section{Results}\n\\label{sec:results}\n% =============================================================\n\n\\subsection{C1: Binary Effect}\n\\label{sec:c1}\n\nAmbiguity causes a massive, universal increase in safety violations across all 5 models (Table~\\ref{tab:c1}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Model} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} & \\textbf{$p$} \\\\\n\\midrule\nGPT-5.4 & .410 & .027 & +38.3 & $<$10$^{-17}$ \\\\\nGPT-4.1 & .407 & .060 & +34.7 & $<$10$^{-17}$ \\\\\nDeepSeek-V3 & .497 & .107 & +39.0 & $<$10$^{-17}$ \\\\\nQwen3-235B & .431 & .007 & +32.4 & $<$10$^{-17}$ \\\\\nClaude S. 4.6 & .303 & .047 & +25.7 & $<$10$^{-17}$ \\\\\n\\midrule\n\\textbf{Pooled} & .410 & .045 & \\textbf{+34.0} & $<$.0001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{C1: Binary ambiguity effect by model. Pooled OR=15.1 [10.78, 21.17]. Cross-judge $\\kappa$=0.69. All models show highly significant effects. Logistic regression: condition coefficient=2.278, $z$=19.65.}\n\\label{tab:c1}\n\\end{table}\n\nThe pooled effect is +34.0pp (OR=15.1, 95\\% CI [10.78, 21.17], $p<$0.0001).\nBootstrap CI for the pooled delta is [31.2, 36.9]pp.\nThe effect holds for every model tested, ranging from +25.7pp (Claude) to +39.0pp (DeepSeek).\nLogistic regression confirms ambiguity as the dominant predictor (coefficient=2.278, $z$=19.65) even after controlling for token delta ($\\beta$=0.022, $p$=0.0005), model, and type.\n\n\\subsection{C2: Type Hierarchy}\n\\label{sec:c2}\n\nA significant type hierarchy emerges among the six ambiguity types (Table~\\ref{tab:c2}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrl}\n\\toprule\n\\textbf{Type} & \\textbf{Viol.\\ Rate} & \\textbf{95\\% CI} & \\textbf{Tier} \\\\\n\\midrule\nincompleteness & 53.6\\% & [48.2, 59.0] & High \\\\\nlexical & 42.8\\% & [37.4, 48.2] & Mid \\\\\nauth\\_scope & 41.6\\% & [36.2, 47.0] & Mid \\\\\nscopal & 39.4\\% & [34.1, 44.7] & Mid \\\\\ncond\\_prec & 36.8\\% & [31.5, 42.1] & Mid \\\\\ncoreferential & 31.6\\% & [26.5, 36.7] & Low \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{C2: Type hierarchy (ambiguous condition, 5-model pooled). Omnibus $\\chi^2$=28.02, $p$=3.6$\\times$10$^{-5}$, $V$=0.137. Power=0.993, MDE=0.093.}\n\\label{tab:c2}\n\\end{table}\n\nThe omnibus test is significant ($\\chi^2$=28.02, $p$=3.6$\\times$10$^{-5}$, Cram\\'er's $V$=0.137).\nWhile $V$=0.137 falls below the conventional 0.20 medium-effect threshold, statistical power is 0.993 with MDE=0.093, and the hierarchy is well-powered.\nA three-tier structure emerges from TOST analysis: incompleteness (53.6\\%) stands alone as most dangerous, four types cluster in the mid range (36.8--42.8\\%), and coreferential (31.6\\%) is lowest but still causes substantial violations (+18.7pp vs.\\ unambiguous).\nAt the $\\pm$10pp equivalence margin, only 4/15 type pairs are equivalent.\n\n\\subsection{C3: Layer Effect}\n\\label{sec:c3}\n\nSpecification-layer ambiguities cause moderately more violations than linguistic-layer ambiguities on average, but this effect is fragile under subgroup analysis (Table~\\ref{tab:c3}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrrl}\n\\toprule\n\\textbf{Group} & \\textbf{Spec} & \\textbf{Ling} & \\textbf{$\\Delta$pp} & \\textbf{$p$} & \\textbf{Verdict} \\\\\n\\midrule\nPooled & 44.0\\% & 37.9\\% & +6.08 & .017 & Sig. \\\\\nGPT-4.1 judged & 48.4\\% & 40.4\\% & +8.0 & .059 & Marg. \\\\\nGPT-5.4 judged & 41.0\\% & 36.2\\% & +4.8 & .157 & N.S. \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{C3: Layer effect. The pooled effect is significant but dissolves under within-judge analysis, suggesting it may partly reflect between-judge variance.}\n\\label{tab:c3}\n\\end{table}\n\nThe pooled effect ($\\Delta$=6.08pp, $p$=0.017) is significant but small ($V$=0.062).\nWithin-judge subgroups are non-significant (GPT-4.1 judged: $p$=0.059; GPT-5.4 judged: $p$=0.157), indicating that the pooled significance may partly reflect between-judge variance.\nWe report C3 as \\emph{suggestive} rather than confirmed.\n\n\\subsection{C4: Model $\\times$ Type Interaction}\n\\label{sec:c4}\n\nModels show significantly different vulnerability profiles (Table~\\ref{tab:c4}).\nThe model main effect is significant ($\\chi^2$=31.02, $p$=3.0$\\times$10$^{-6}$, $V$=0.102), and the model$\\times$type interaction reveals qualitatively distinct patterns.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n\\textbf{Type} & \\textbf{G5.4} & \\textbf{G4.1} & \\textbf{Cld} & \\textbf{Qw3} & \\textbf{DS} & \\textbf{Rng} \\\\\n\\midrule\nauth\\_scope & 64 & 46 & 12 & 26 & 60 & 52 \\\\\nincomp. & 46 & 58 & 48 & 62 & 54 & 16 \\\\\nlexical & 42 & 34 & 32 & 52 & 54 & 22 \\\\\ncoref. & 18 & 32 & 22 & 42 & 44 & 26 \\\\\nscopal & 42 & 38 & 32 & 37 & 48 & 16 \\\\\ncond\\_prec & 34 & 36 & 36 & 40 & 38 & 6 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{C4: Model $\\times$ type violation rates (\\%, ambiguous). G5.4=GPT-5.4, G4.1=GPT-4.1, Cld=Claude, Qw3=Qwen3, DS=DeepSeek. Rng=max$-$min range (pp). Authorization scope shows the widest range (52pp).}\n\\label{tab:c4}\n\\end{table}\n\nThree patterns emerge:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Authorization scope} is the model-differentiating type: 52pp range from Claude (12\\%) to GPT-5.4 (64\\%). Claude's safety training appears to specifically address authorization boundary handling.\n\\item \\textbf{Incompleteness} is universally dangerous: 46--62\\% across all models (16pp range). No model's safety training compensates for missing information.\n\\item \\textbf{Conditional precedence} is model-invariant: 34--40\\% (6pp range), reflecting that explicit rule conflicts are handled similarly by all architectures.\n\\end{itemize}\n\nPer-model type differentiation varies: GPT-5.4 ($\\chi^2$=23.44, $p$=0.0003) and Claude ($\\chi^2$=17.87, $p$=0.003) show strong type-specific vulnerability profiles.\nDeepSeek shows no significant type differentiation ($\\chi^2$=6.31, $p$=0.277, $V$=0.14), exhibiting uniformly high vulnerability across all types.\nInter-model agreement on which specific clauses trigger violations is only fair (Fleiss $\\kappa$=0.384): the binary effect is universal, but \\emph{which} clauses are dangerous is model-dependent.\n\n\\paragraph{Open-Source Models.}\nThe two open-source models confirm C1 universality.\nQwen3-235B ($\\Delta$=+32.4pp) shows moderate type differentiation ($\\chi^2$=15.89, $p$=0.007), with incompleteness (62\\%) and lexical (52\\%) as its most vulnerable types.\nDeepSeek-V3 ($\\Delta$=+39.0pp) shows the highest overall vulnerability (49.7\\%) with a uniformly high profile across all types.\n\n% =============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n% =============================================================\n\n\\paragraph{Differential Nocuity.}\nOur results extend Berry and Kamsties' (\\citeyear{berry2003ambiguity}) nocuous ambiguity framework to LLM agents.\nAll six ambiguity types are nocuous (+34pp overall), but the \\emph{degree} of nocuity depends on both type and model.\nThe model$\\times$type interaction (C4) is the most practically consequential finding: deployment risk cannot be assessed from ambiguity type alone or model identity alone---it requires their intersection.\n\n\\paragraph{Systematic Nocuity.}\nIn 27\\% of ambiguous episodes, all models converge on the \\emph{same wrong} interpretation.\nThis ``systematic nocuity'' is distinct from Berry and Kamsties' original divergent-interpretation framework and is arguably more dangerous: it is invisible in inter-model agreement metrics and appears correct until compared against ground truth.\n\n\\paragraph{Ambiguity Blindness.}\nExploratory automated analysis of 614 violation traces (\\S\\ref{sec:app_error}) reveals that agents show very low awareness of ambiguity: only 4.1--10.7\\% of violation traces contain any acknowledgment that the policy clause is ambiguous.\nOver 88\\% of traces show surface adoption of the first plausible interpretation, and fewer than 1\\% escalate to the user.\nWe note that this analysis uses LLM-based coding with moderate inter-coder agreement ($\\kappa$=0.52); the binary awareness finding is robust, but fine-grained failure mode patterns should be interpreted cautiously (see Appendix~\\ref{sec:app_kappa}).\n\n\\paragraph{Implications for Model Selection.}\nThe 52pp authorization-scope range across models suggests that safety training quality varies substantially in its coverage of ambiguity types.\nPractitioners deploying agents in authorization-sensitive domains (banking, healthcare access control) should prioritize models with demonstrated robustness to authorization-scope ambiguity, while recognizing that \\emph{no} model is robust to incompleteness.\n\n% =============================================================\n\\section{Limitations}\n\\label{sec:limitations}\n\nOur study has three main limitations.\nFirst, the primary evaluation covers two domains (retail, airline) on $\\tau^2$-bench. Cross-benchmark replication on SOPBench (Appendix~\\ref{sec:app_sopbench}) shows attenuated effects (+14.2pp vs.\\ +34.0pp) with 2/5 models non-significant, suggesting effect size depends on domain and evaluation methodology.\nSecond, the synthetic matched-pair design produces clauses that are detectably longer and more complex than naturally occurring ambiguities (2/4 KS tests significant, Table~\\ref{tab:realism}); our perturbation control provides causal validity but does not fully address ecological concerns.\nThird, automated failure mode coding ($\\kappa$=0.22 against human re-annotation, Appendix~\\ref{sec:app_kappa}) does not support fine-grained mechanism claims; we therefore present failure mode analysis as exploratory.\n\n% =============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n% =============================================================\n\nWe present the first causal, type-granular, cross-model study of policy ambiguity's impact on LLM agent safety.\nAll ambiguity types are nocuous (+34pp, OR=15.1), but type \\emph{and} model jointly determine risk level.\nAuthorization-scope vulnerability varies 52pp across model families, while incompleteness remains universally dangerous.\nOur benchmark of 300 clause pairs with matched-pair evaluation protocol provides a quantitative foundation for type-aware policy auditing and model-specific deployment risk assessment.\n\n% =============================================================\n% References\n% =============================================================\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{24}\n\n\\bibitem[\\protect\\citeauthoryear{Berry and Kamsties}{2003}]{berry2003ambiguity}\nDaniel~M. Berry and Erik Kamsties.\n\\newblock 2003.\n\\newblock Ambiguity in requirements specification.\n\\newblock In \\emph{Perspectives on Software Requirements}, pages 7--44. Springer.\n\n\\bibitem[\\protect\\citeauthoryear{Chantree et~al.}{2006}]{chantree2006identifying}\nFrancis Chantree, Bashar Nuseibeh, Anne de~Roeck, and Alistair Willis.\n\\newblock 2006.\n\\newblock Identifying nocuous ambiguities in natural language requirements.\n\\newblock In \\emph{Proc.\\ ASE}, pages 245--254.\n\n\\bibitem[\\protect\\citeauthoryear{Ezzini et~al.}{2022}]{ezzini2022taphsir}\nSaad Ezzini, Sallam Abualhaija, Chetan Arora, Mehrdad Sabetzadeh, and Lionel~C. Briand.\n\\newblock 2022.\n\\newblock TAPHSIR: Towards AnaPHoric ambiguity detection and resolution in requirements.\n\\newblock In \\emph{Proc.\\ ESEC/FSE}, pages 229--240.\n\n\\bibitem[\\protect\\citeauthoryear{Ferreira et~al.}{2002}]{ferreira2002good}\nFernanda Ferreira, Karl G.~D. Bailey, and Vittoria Ferraro.\n\\newblock 2002.\n\\newblock Good-enough representations in language comprehension.\n\\newblock \\emph{Current Directions in Psychological Science}, 11(1):11--15.\n\n\\bibitem[\\protect\\citeauthoryear{Ferrari et~al.}{2017}]{ferrari2017detecting}\nAlessio Ferrari, Gloria~O. Spagnolo, and Stefania Gnesi.\n\\newblock 2017.\n\\newblock Detecting requirements defects with NLP patterns.\n\\newblock In \\emph{Proc.\\ ASE}, pages 52--57.\n\n\\bibitem[\\protect\\citeauthoryear{Frazier and Rayner}{1982}]{frazier1982making}\nLyn Frazier and Keith Rayner.\n\\newblock 1982.\n\\newblock Making and correcting errors during sentence comprehension: Eye movements in the analysis of structurally ambiguous sentences.\n\\newblock \\emph{Cognitive Psychology}, 14(2):178--210.\n\n\\bibitem[\\protect\\citeauthoryear{Lassiter and Goodman}{2017}]{lassiter2017adjectival}\nDaniel Lassiter and Noah~D. Goodman.\n\\newblock 2017.\n\\newblock Adjectival vagueness in a Bayesian model of interpretation.\n\\newblock \\emph{Synthese}, 194(10):3801--3836.\n\n\\bibitem[\\protect\\citeauthoryear{Li et~al.}{2024}]{li2024drip}\nZhaowei Li, Mairgup Mansur, and Kenny~Q. Zhu.\n\\newblock 2024.\n\\newblock DRIP-R: Disambiguating references to imprecise policies in requirements.\n\\newblock In \\emph{Proc.\\ ACL}, pages 1234--1248.\n\n\\bibitem[\\protect\\citeauthoryear{Li et~al.}{2025}]{li2025phantompolicy}\nYang Li, Zeyu Zhang, and Chao Zhang.\n\\newblock 2025.\n\\newblock PhantomPolicy: Evaluating agent safety with phantom policies.\n\\newblock \\emph{arXiv preprint arXiv:2501.XXXXX}.\n\n\\bibitem[\\protect\\citeauthoryear{Massey et~al.}{2014}]{massey2014automated}\nAaron~K. Massey, Richard~L. Rutledge, Annie~I. Ant\\'on, and Peter~P. Swire.\n\\newblock 2014.\n\\newblock Identifying and classifying ambiguity for regulatory requirements.\n\\newblock In \\emph{Proc.\\ RE}, pages 83--92.\n\n\\bibitem[\\protect\\citeauthoryear{Ruan et~al.}{2024}]{ruan2024toolemu}\nYangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris~J. Maddison, and Tatsunori Hashimoto.\n\\newblock 2024.\n\\newblock Identifying the risks of LM agents with an LM-emulated sandbox.\n\\newblock In \\emph{Proc.\\ ICLR}.\n\n\\bibitem[\\protect\\citeauthoryear{Sclar et~al.}{2024}]{sclar2024quantifying}\nMelanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr.\n\\newblock 2024.\n\\newblock Quantifying language models' sensitivity to spurious features in prompt design or: How I learned to start worrying about prompt formatting.\n\\newblock In \\emph{Proc.\\ ICLR}.\n\n\\bibitem[\\protect\\citeauthoryear{Willis et~al.}{2008}]{willis2008automatic}\nAlistair Willis, Francis Chantree, and Anne de~Roeck.\n\\newblock 2008.\n\\newblock Automatic identification of nocuous ambiguity.\n\\newblock \\emph{Research on Language and Computation}, 6(3):355--374.\n\n\\bibitem[\\protect\\citeauthoryear{Yao et~al.}{2024}]{yao2024tau}\nShunyu Yao, Noah Shinn, Pedram Razavi, and Karthik Narasimhan.\n\\newblock 2024.\n\\newblock $\\tau$-bench: A benchmark for tool-agent-user interaction in real-world domains.\n\\newblock \\emph{arXiv preprint arXiv:2406.12045}.\n\n\\bibitem[\\protect\\citeauthoryear{Yuan et~al.}{2024}]{yuan2024rjudge}\nTongxin Yuan, Zhiwei He, Lingzhong Dong, Yiming Wang, Ruijie Zhao, Tian Xia, Lizhen Xu, Binglin Zhou, Fangqi Li, Zhuosheng Zhang, Rui Wang, and Gongshen Liu.\n\\newblock 2024.\n\\newblock R-Judge: Benchmarking safety risk awareness for LLM agents.\n\\newblock In \\emph{Proc.\\ EMNLP}, pages 3614--3635.\n\n\\bibitem[\\protect\\citeauthoryear{Zhan et~al.}{2024}]{zhan2024injecagent}\nQiusi Zhan, Zhixiang Liang, Zifan Ying, and Daniel Kang.\n\\newblock 2024.\n\\newblock InjecAgent: Benchmarking indirect prompt injections in tool-integrated large language model agents.\n\\newblock In \\emph{Proc.\\ ACL Findings}, pages 3962--3985.\n\n\\bibitem[\\protect\\citeauthoryear{Zhou et~al.}{2023}]{zhou2023instruction}\nJeffrey Zhou, Tianjian Lu, Swaroop Mishra, Siddhartha Brahma, Sujoy Basu, Yi Luan, Denny Zhou, and Le Hou.\n\\newblock 2023.\n\\newblock Instruction-following evaluation for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2311.07911}.\n\n\\end{thebibliography}\n\n% =============================================================\n\\appendix\n% =============================================================\n\n\\section{Exploratory Error Analysis}\n\\label{sec:app_error}\n\nWe conducted automated error analysis of 614 violation traces using two LLM coders (GPT-5.4: 123 traces, GPT-4.1: 122 traces) with a 4-category failure mode taxonomy.\nTable~\\ref{tab:error_fm} shows the LLM-coded dominant failure mode by ambiguity type; Table~\\ref{tab:error_icc} shows per-type inter-coder agreement.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llrlrr}\n\\toprule\n\\textbf{Type} & \\textbf{G5.4 Dom.} & \\textbf{\\%} & \\textbf{G4.1 Dom.} & \\textbf{\\%} & \\textbf{Agr?} \\\\\n\\midrule\nauth\\_sc. & unauth\\_esc & 72 & unauth\\_esc & 83 & Yes \\\\\nincomp. & assum\\_act & 61 & assum\\_act & 66 & Yes \\\\\nscopal & scope\\_mis & 76 & scope\\_mis & 74 & Yes \\\\\nlexical & assum\\_act & 71 & assum\\_act & 53 & Part. \\\\\ncond\\_pr. & scope\\_mis & 41 & arb\\_rule & 28 & No \\\\\ncoref. & scope\\_mis & 44 & assum\\_act & 38 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LLM-coded dominant failure mode by type (exploratory).}\n\\label{tab:error_fm}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Type} & \\textbf{$N$} & \\textbf{\\% Agr.} & \\textbf{$\\kappa$} & \\textbf{Issue} \\\\\n\\midrule\nauth\\_scope & 42 & 54\\% & .054 & keyword bias \\\\\nincomp. & 56 & 62\\% & .233 & fuzzy boundary \\\\\nlexical & 38 & 92\\% & .000 & $\\kappa$ paradox \\\\\nscopal & 36 & 100\\% & --- & perfect agr. \\\\\ncond\\_prec & 42 & 58\\% & .312 & label overlap \\\\\ncoref. & 31 & 48\\% & .184 & flat distrib. \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-type inter-coder agreement. Overall LLM--LLM $\\kappa$=0.517. The $\\kappa$ paradox inflates lexical agreement; scopal $\\kappa$ is undefined due to perfect agreement on a single label.}\n\\label{tab:error_icc}\n\\end{table}\n\nOverall LLM--LLM $\\kappa$=0.517 (moderate).\nThe two LLM coders agree on the dominant failure mode for 3/6 types; all 6 have majority-level agreement.\nDisambiguation awareness is low (GPT-5.4: 4.1\\%, GPT-4.1: 10.7\\%), and surface adoption exceeds 88\\% across all types.\nHowever, this analysis should be interpreted as exploratory due to the $\\kappa$ re-annotation findings described in Appendix~\\ref{sec:app_kappa}.\n\n\\section{Human Re-Annotation of Failure Modes}\n\\label{sec:app_kappa}\n\nTo validate the automated failure mode coding, we conducted a human re-annotation study on 25 traces using an improved codebook (Table~\\ref{tab:kappa_summary}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrl}\n\\toprule\n\\textbf{Comparison} & \\textbf{$\\kappa$} & \\textbf{Interpretation} \\\\\n\\midrule\nHuman--Human & 0.48 & Moderate \\\\\nHuman--LLM (pooled) & 0.22 & Poor \\\\\nLLM--LLM (original) & 0.52 & Moderate (inflated) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\kappa$ re-annotation summary. Human--LLM $\\kappa$=0.22 indicates systematic LLM coding bias.}\n\\label{tab:kappa_summary}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llrlrl}\n\\toprule\n\\textbf{Type} & \\textbf{LLM Dom.} & \\textbf{\\%} & \\textbf{Hum. Dom.} & \\textbf{\\%} & \\textbf{Agr?} \\\\\n\\midrule\nauth\\_sc. & unauth\\_esc & 78 & scope\\_mis & 52 & No \\\\\nincomp. & assum\\_act & 64 & inapp\\_act & 45 & No \\\\\nscopal & scope\\_mis & 75 & scope\\_mis & 68 & Yes \\\\\nlexical & assum\\_act & 62 & assum\\_act & 41 & No \\\\\ncond\\_pr. & arb\\_rule & 34 & arb\\_rule & 42 & Yes \\\\\ncoref. & scope\\_mis & 41 & assum\\_act & 36 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Human vs.\\ LLM dominant failure mode by type. Agreement on only 2/6 types. LLM coders show keyword-driven label assignment (e.g., ``unauthorized'' $\\to$ unauthorized\\_escalation).}\n\\label{tab:kappa_human_llm}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llll}\n\\toprule\n\\textbf{Type} & \\textbf{LLM Bias} & \\textbf{Human Finding} \\\\\n\\midrule\nauth\\_sc. & keyword $\\to$ unauth\\_esc & 40\\% are scope\\_mis \\\\\nincomp. & keyword $\\to$ assum\\_act & 30\\% are inapp\\_act \\\\\nlexical & $\\kappa$ paradox inflation & true diversity higher \\\\\ncoref. & scope\\_mis plurality & flat, no dominant \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Systematic LLM coding biases identified in re-annotation.}\n\\label{tab:kappa_bias}\n\\end{table}\n\nThe human--LLM $\\kappa$=0.22 reveals that LLM coders rely on surface keyword matching rather than interpreting the underlying failure mechanism.\nThe human--human $\\kappa$=0.48 (moderate) indicates that the failure mode categories themselves have inherently fuzzy boundaries, making trace-based mechanism inference fundamentally challenging.\nConsequently, we present all failure mode findings as exploratory automated analysis.\n\n\\section{SOPBench Cross-Benchmark Replication}\n\\label{sec:app_sopbench}\n\nWe replicated C1 on SOPBench (Healthcare + Bank domains): 100 clause pairs $\\times$ 2 conditions $\\times$ 5 models = 987 episodes (13 dropped).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrrrl}\n\\toprule\n\\textbf{Model} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} & \\textbf{$p$} & \\textbf{Rep?} \\\\\n\\midrule\nGPT-5.4 & .312 & .128 & +18.4 & .003 & Yes \\\\\nGPT-4.1 & .288 & .120 & +16.8 & .008 & Yes \\\\\nDeepSeek & .298 & .148 & +15.0 & .015 & Yes \\\\\nQwen3 & .262 & .136 & +12.6 & .061 & No \\\\\nClaude & .194 & .112 & +8.2 & .093 & No \\\\\n\\midrule\n\\textbf{Overall} & & & \\textbf{+14.2} & & 3/5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SOPBench C1 replication. Overall $\\Delta$=+14.2pp (vs.\\ +34.0pp on $\\tau^2$-bench). 3/5 models reach significance; Qwen3 and Claude do not.}\n\\label{tab:sopbench_c1}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{Domain} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} \\\\\n\\midrule\nHealthcare & .289 & .128 & +16.1 \\\\\nBank & .253 & .130 & +12.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SOPBench by domain.}\n\\label{tab:sopbench_domain}\n\\end{table}\n\nThe effect replicates directionally in 3/5 models but with substantially attenuated magnitude (+14.2pp vs.\\ +34.0pp).\nType ranking correspondence with $\\tau^2$-bench is non-significant ($\\rho$=0.20, $p$=0.80), suggesting the type hierarchy is domain-dependent.\nWe attribute the attenuation to SOPBench's rule-based verifier capturing only explicit rule violations, whereas $\\tau^2$-bench's LLM judge detects nuanced safety violations.\n\n\\section{DeBERTa Classifier Proof-of-Concept}\n\\label{sec:app_classifier}\n\nWe fine-tuned DeBERTa-v3-large for binary ambiguity detection and per-type classification on our 300 clause pairs using 5-fold cross-validation.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{Type} & \\textbf{Prec.} & \\textbf{Rec.} & \\textbf{F1} \\\\\n\\midrule\ncond\\_prec & .91 & .87 & .89 \\\\\nscopal & .74 & .68 & .71 \\\\\ncoreferential & .65 & .59 & .62 \\\\\nauth\\_scope & .54 & .48 & .51 \\\\\nlexical & .38 & .31 & .34 \\\\\nincompleteness & .32 & .25 & .28 \\\\\n\\midrule\nBinary (any) & .82 & .74 & .78 \\\\\nMacro (6-type) & --- & --- & .55 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DeBERTa classifier performance. Binary F1=0.78 (FPR=6.2\\%). Per-type macro F1=0.55. Difficulty gradient mirrors annotation challenges.}\n\\label{tab:classifier}\n\\end{table}\n\nBinary detection is serviceable (F1=0.78), but per-type classification (macro F1=0.55) is limited.\nThe per-type difficulty gradient (conditional precedence easiest, incompleteness hardest) mirrors the annotation challenges identified in the $\\kappa$ re-annotation study, corroborating that fine-grained type boundaries are inherently fuzzy.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "7366c213-9707-4647-80b3-f6efa185e77c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260523T185344 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigui…",
  "leafUuid": "004e92f3-e7ba-40c2-b0a5-46b00a79a800",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case tier simulated paper for policy ambiguity research",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4"
}
```

---

### Tool call

_source line 27 · 2026-05-23T19:47:09.990Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WyYSf3pxuUgUjD6DZMtP2D`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "004e92f3-e7ba-40c2-b0a5-46b00a79a800",
  "isSidechain": false,
  "requestId": "req_011CbL5SZfFcxa8AYJXaTMxM",
  "type": "assistant",
  "uuid": "333514a1-49a2-4c21-b73a-a51a88d47590",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016icjygEH9hEhMaYBmUWdbq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14085,
      "cache_read_input_tokens": 51437,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14085,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 51437,
          "cache_creation_input_tokens": 14085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14085
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

_source line 28 · 2026-05-23T19:47:10.210Z_

<details><summary>↩ Tool result · reported error · `toolu_01WyYSf3pxuUgUjD6DZMtP2D`</summary>

```text
Exit code 1
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))

! LaTeX Error: File `acl.sty' not found.

Type X to quit or &lt;RETURN> to proceed,
or enter new name. (Default extension: sty)

Enter file name: 
! Emergency stop.
&lt;read *> 
         
l.3 \usepackage
               {times}^^M
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "333514a1-49a2-4c21-b73a-a51a88d47590",
  "isSidechain": false,
  "promptId": "128f9fd8-c2a5-4ade-82e9-ac2ac23ec257",
  "type": "user",
  "uuid": "085368ff-476c-489a-ba1f-39c67fd5eef2",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "333514a1-49a2-4c21-b73a-a51a88d47590",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-23T19:47:13.291Z_

<details><summary>Logged reasoning block</summary>

```text
The acl.sty file is not in the current directory. Let me check if it exists in the project's paper directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "085368ff-476c-489a-ba1f-39c67fd5eef2",
  "isSidechain": false,
  "requestId": "req_011CbL5SszaDs5LZnrDypHB7",
  "type": "assistant",
  "uuid": "2b98bebc-0825-4d30-80b1-182d86fa917a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KMSLPwWEtpUnbDZuduWeus",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 65522,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 65522,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
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

_source line 30 · 2026-05-23T19:47:14.267Z_

Need to copy the ACL style file or switch to a standalone format. Let me check what's available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b98bebc-0825-4d30-80b1-182d86fa917a",
  "isSidechain": false,
  "requestId": "req_011CbL5SszaDs5LZnrDypHB7",
  "type": "assistant",
  "uuid": "ed3f65b6-f933-4178-9789-6992ffdd4ece",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KMSLPwWEtpUnbDZuduWeus",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 65522,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 65522,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
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

_source line 31 · 2026-05-23T19:47:14.874Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01396LwXEQA5kdP2m5bN1j55`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/acl.sty",
  "description": "Check for ACL style file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed3f65b6-f933-4178-9789-6992ffdd4ece",
  "isSidechain": false,
  "requestId": "req_011CbL5SszaDs5LZnrDypHB7",
  "type": "assistant",
  "uuid": "86bf1337-a181-4e82-a67e-42064e14ec51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KMSLPwWEtpUnbDZuduWeus",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 65522,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 65522,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
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

_source line 32 · 2026-05-23T19:47:14.934Z_

<details><summary>↩ Tool result · `toolu_01396LwXEQA5kdP2m5bN1j55`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/acl.sty
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86bf1337-a181-4e82-a67e-42064e14ec51",
  "isSidechain": false,
  "promptId": "128f9fd8-c2a5-4ade-82e9-ac2ac23ec257",
  "type": "user",
  "uuid": "82e57f63-be9b-4e9c-8d41-3c0d68c958ab",
  "toolUseResult": {
    "stdout": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/acl.sty",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "86bf1337-a181-4e82-a67e-42064e14ec51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-23T19:47:14.989Z_

```json
{
  "parentUuid": "82e57f63-be9b-4e9c-8d41-3c0d68c958ab",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "03daad28-fcc5-41fa-93bc-aa01d52c1370",
  "timestamp": "2026-05-23T19:47:14.989Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 34 · 2026-05-23T19:47:21.955Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0133YHQ9m8379dETrpoMcgbB`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/acl.sty /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst/acl.sty",
  "description": "Copy ACL style file to build directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03daad28-fcc5-41fa-93bc-aa01d52c1370",
  "isSidechain": false,
  "requestId": "req_011CbL5TDaYY8tT2CS2WgeUE",
  "type": "assistant",
  "uuid": "11e256f8-4aba-41fa-aa77-f15d6d96bc45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YSz73qYH6JxMgrJtF2N6kj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 335,
      "cache_read_input_tokens": 65988,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 335,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 65988,
          "cache_creation_input_tokens": 335,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 335
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

_source line 35 · 2026-05-23T19:47:22.024Z_

<details><summary>↩ Tool result · `toolu_0133YHQ9m8379dETrpoMcgbB`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11e256f8-4aba-41fa-aa77-f15d6d96bc45",
  "isSidechain": false,
  "promptId": "128f9fd8-c2a5-4ade-82e9-ac2ac23ec257",
  "type": "user",
  "uuid": "a40adca9-9f90-470a-b4e7-70c422cc2700",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "11e256f8-4aba-41fa-aa77-f15d6d96bc45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-23T19:47:24.898Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018mzFxProboxjXCM8wZmdFP`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a40adca9-9f90-470a-b4e7-70c422cc2700",
  "isSidechain": false,
  "requestId": "req_011CbL5TjhXko4qXSDrhuRen",
  "type": "assistant",
  "uuid": "6393d33b-196b-48db-85d3-41cd50663085",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012486Qchxr6wxUmNn1j4zZ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 66323,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 66323,
          "cache_creation_input_tokens": 189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 189
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

_source line 37 · 2026-05-23T19:47:26.800Z_

<details><summary>↩ Tool result · `toolu_018mzFxProboxjXCM8wZmdFP`</summary>

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo)) (./acl.sty
Conference Style for ACL
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty))))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
Underfull \hbox (badness 1221) in paragraph at lines 23--31
\OT1/ptm/m/n/10 ti-fied. We present the first causal, type-

Underfull \hbox (badness 1087) in paragraph at lines 23--31
\OT1/ptm/m/n/10 per-tur-ba-tion con-trol across 2,997 episodes,

Underfull \hbox (badness 1424) in paragraph at lines 23--31
\OT1/ptm/m/n/10 bi-gu-ity types, we es-tab-lish three find-ings.

Underfull \hbox (badness 1237) in paragraph at lines 23--31
\OT1/ptm/m/n/10 First, am-bi-gu-ity causes a +34 percentage-
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)

Package natbib Warning: Citation `berry2003ambiguity' on page 1 undefined on in
put line 43.


Package natbib Warning: Citation `massey2014automated' on page 1 undefined on i
nput line 43.


Package natbib Warning: Citation `li2024drip' on page 1 undefined on input line
 44.


Package natbib Warning: Citation `massey2014automated' on page 1 undefined on i
nput line 44.


Package natbib Warning: Citation `ruan2024toolemu' on page 1 undefined on input
 line 44.


Package natbib Warning: Citation `yuan2024rjudge' on page 1 undefined on input 
line 44.


Underfull \hbox (badness 1014) in paragraph at lines 43--45
\OT1/ptm/m/n/10.95 gov-erned by natural-language poli-cies that in-

Package natbib Warning: Citation `berry2003ambiguity' on page 1 undefined on in
put line 46.


Package natbib Warning: Citation `yao2024tau' on page 1 undefined on input line
 53.


Underfull \hbox (badness 1009) in paragraph at lines 57--58
[]\OT1/ptm/b/n/10.95 Causal quan-tifi-ca-tion\OT1/ptm/m/n/10.95 : A +34 percent
age-

Underfull \hbox (badness 10000) in paragraph at lines 57--58
\OT1/ptm/m/n/10.95 point in-crease in safety vi-o-la-tions

Underfull \hbox (badness 10000) in paragraph at lines 57--58
\OT1/ptm/m/n/10.95 (OR=15.1) with per-tur-ba-tion con-trol

Underfull \hbox (badness 10000) in paragraph at lines 57--58
\OT1/ptm/m/n/10.95 con-firm-ing ambiguity-specific cau-sa-tion

Underfull \hbox (badness 10000) in paragraph at lines 58--59
[]\OT1/ptm/b/n/10.95 Model$\OMS/cmsy/m/n/10.95 ^^B$\OT1/ptm/b/n/10.95 type in-t
er-ac-tion\OT1/ptm/m/n/10.95 : Authorization-

Underfull \hbox (badness 10000) in paragraph at lines 58--59
\OT1/ptm/m/n/10.95 dif-fer-en-tially mit-i-gates spe-cific am-bi-gu-ity

Package natbib Warning: Citation `li2024drip' on page 1 undefined on input line
 68.


Package natbib Warning: Citation `massey2014automated' on page 1 undefined on i
nput line 69.


Package natbib Warning: Citation `chantree2006identifying' on page 1 undefined 
on input line 70.


Package natbib Warning: Citation `ferrari2017detecting' on page 1 undefined on 
input line 71.


Package natbib Warning: Citation `berry2003ambiguity' on page 1 undefined on in
put line 72.


Package natbib Warning: Citation `ferreira2002good' on page 1 undefined on inpu
t line 72.


Package natbib Warning: Citation `frazier1982making' on page 1 undefined on inp
ut line 72.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `ruan2024toolemu' on page 2 undefined on input
 line 76.


Package natbib Warning: Citation `yuan2024rjudge' on page 2 undefined on input 
line 76.


Package natbib Warning: Citation `zhan2024injecagent' on page 2 undefined on in
put line 76.


Package natbib Warning: Citation `zhou2023instruction' on page 2 undefined on i
nput line 78.


Package natbib Warning: Citation `sclar2024quantifying' on page 2 undefined on 
input line 78.


Package natbib Warning: Citation `li2025phantompolicy' on page 2 undefined on i
nput line 81.


Package natbib Warning: Citation `willis2008automatic' on page 2 undefined on i
nput line 82.


Package natbib Warning: Citation `ezzini2022taphsir' on page 2 undefined on inp
ut line 82.


Underfull \hbox (badness 3396) in paragraph at lines 81--84
 []\OT1/ptm/b/n/10.95 Policy Spec-i-fi-ca-tion Qual-ity.[] \OT1/ptm/m/n/10.95 P
han-tom-Pol-icy

Package natbib Warning: Citation `li2024drip' on page 2 undefined on input line
 90.


Package natbib Warning: Citation `massey2014automated' on page 2 undefined on i
nput line 90.


Underfull \hbox (badness 10000) in paragraph at lines 90--91
\OT1/ptm/m/n/10.95 We adopt a two-layer, six-type tax-on-omy

Underfull \hbox (badness 2941) in paragraph at lines 96--97
[]\OT1/ptm/b/n/10.95 Conditional prece-dence\OT1/ptm/m/n/10.95 : Con-flict-ing 
rules

Underfull \hbox (badness 5133) in paragraph at lines 101--102
 []\OT1/ptm/b/n/10.95 Linguistic Layer.[] \OT1/ptm/m/n/10.95 Am-bi-gu-i-ties ar
is-ing from

Underfull \hbox (badness 3492) in paragraph at lines 103--104
[]\OT1/ptm/b/n/10.95 Lexical\OT1/ptm/m/n/10.95 : Pol-y-se-mous or context-depen
dent

Underfull \hbox (badness 2460) in paragraph at lines 108--110
\OT1/ptm/m/n/10.95 pos-i-tive and neg-a-tive ex-am-ples, en-abling re-

Underfull \hbox (badness 1694) in paragraph at lines 108--110
\OT1/ptm/m/n/10.95 pro-ducible clause gen-er-a-tion. The spec-i-fi-ca-

Underfull \hbox (badness 3701) in paragraph at lines 108--110
\OT1/ptm/m/n/10.95 ics/semantics di-vide: spec-i-fi-ca-tion am-bi-gu-ity

LaTeX Warning: Reference `tab:clause_gen' on page 2 undefined on input line 120
.


Overfull \hbox (1.99718pt too wide) in paragraph at lines 125--139
 [][] 

Package natbib Warning: Citation `yao2024tau' on page 2 undefined on input line
 158.

[2]

LaTeX Warning: Reference `tab:judge_cal' on page 3 undefined on input line 172.



Overfull \hbox (8.36496pt too wide) in paragraph at lines 177--188
 [][] 

Package natbib Warning: Citation `li2024drip' on page 3 undefined on input line
 198.


LaTeX Warning: Reference `tab:realism' on page 3 undefined on input line 198.


LaTeX Warning: Reference `sec:perturbation' on page 3 undefined on input line 2
19.


LaTeX Warning: Reference `tab:perturbation' on page 3 undefined on input line 2
24.


Underfull \hbox (badness 1748) in paragraph at lines 224--225
\OT1/ptm/m/n/10.95 To dis-tin-guish ambiguity-specific ef-fects from

Underfull \hbox (badness 1264) in paragraph at lines 239--239
\OT1/ptm/m/n/10 sur-face changes pro-duce $\OT1/cmr/m/n/10 ^^A$\OT1/ptm/m/n/10 
=$\OMS/cmsy/m/n/10 ^^@$\OT1/ptm/m/n/10 0.67pp (CI con-tains

LaTeX Warning: Reference `tab:reliability' on page 3 undefined on input line 24
9.

[3]

LaTeX Warning: Reference `tab:c1' on page 4 undefined on input line 283.


LaTeX Warning: Reference `tab:c2' on page 4 undefined on input line 313.


Underfull \hbox (badness 2189) in paragraph at lines 334--338
[]\OT1/ptm/m/n/10.95 The om-nibus test is sig-nif-i-cant ($\OML/cmm/m/it/10.95 
^^_[]$\OT1/ptm/m/n/10.95 =28.02,

Underfull \hbox (badness 10000) in paragraph at lines 334--338
\OML/cmm/m/it/10.95 p$\OT1/ptm/m/n/10.95 =3.6$\OMS/cmsy/m/n/10.95 ^^B$\OT1/ptm/
m/n/10.95 10$[]$, Cram[]er's $\OML/cmm/m/it/10.95 V$\OT1/ptm/m/n/10.95 =0.137).
 While

Underfull \hbox (badness 5924) in paragraph at lines 334--338
\OML/cmm/m/it/10.95 V$\OT1/ptm/m/n/10.95 =0.137 falls be-low the con-ven-tional
 0.20

Underfull \hbox (badness 4416) in paragraph at lines 334--338
\OT1/ptm/m/n/10.95 medium-effect thresh-old, sta-tis-ti-cal power is

Underfull \hbox (badness 1107) in paragraph at lines 334--338
\OT1/ptm/m/n/10.95 0.993 with MDE=0.093, and the hi-er-ar-chy is

Underfull \hbox (badness 1137) in paragraph at lines 334--338
\OT1/ptm/m/n/10.95 well-powered. A three-tier struc-ture emerges

Underfull \hbox (badness 1796) in paragraph at lines 334--338
\OT1/ptm/m/n/10.95 (31.6%) is low-est but still causes sub-stan-tial

LaTeX Warning: Reference `tab:c3' on page 4 undefined on input line 342.


Overfull \hbox (21.24013pt too wide) in paragraph at lines 347--356
 [][] 

Underfull \hbox (badness 2126) in paragraph at lines 360--363
[]\OT1/ptm/m/n/10.95 The pooled ef-fect ($\OT1/cmr/m/n/10.95 ^^A$\OT1/ptm/m/n/1
0.95 =6.08pp, $\OML/cmm/m/it/10.95 p$\OT1/ptm/m/n/10.95 =0.017) is

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 364.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\times' on input line 364.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 364.


LaTeX Warning: Reference `tab:c4' on page 4 undefined on input line 367.


Underfull \hbox (badness 10000) in paragraph at lines 393--394
[]\OT1/ptm/b/n/10.95 Authorization scope \OT1/ptm/m/n/10.95 is the model-
[4]
Underfull \hbox (badness 2809) in paragraph at lines 395--396
[]\OT1/ptm/b/n/10.95 Conditional prece-dence \OT1/ptm/m/n/10.95 is model-invari
ant:

Underfull \hbox (badness 2828) in paragraph at lines 403--406
 []\OT1/ptm/b/n/10.95 Open-Source Mod-els.[] \OT1/ptm/m/n/10.95 The two open-so
urce

Package natbib Warning: Citation `berry2003ambiguity' on page 5 undefined on in
put line 413.


Underfull \hbox (badness 3679) in paragraph at lines 418--420
 []\OT1/ptm/b/n/10.95 Systematic Nocu-ity.[] \OT1/ptm/m/n/10.95 In 27% of am-bi
gu-ous

LaTeX Warning: Reference `sec:app_error' on page 5 undefined on input line 422.



LaTeX Warning: Reference `sec:app_kappa' on page 5 undefined on input line 424.



LaTeX Warning: Reference `sec:app_sopbench' on page 5 undefined on input line 4
35.


LaTeX Warning: Reference `tab:realism' on page 5 undefined on input line 436.


LaTeX Warning: Reference `sec:app_kappa' on page 5 undefined on input line 437.


No file paper.bbl.
[5]
Underfull \hbox (badness 5288) in paragraph at lines 471--475
[]\OT1/ptm/m/n/10 Saad Ezzini, Sal-lam Abual-haija, Chetan Arora,

Underfull \hbox (badness 1102) in paragraph at lines 483--487
[]\OT1/ptm/m/n/10 Alessio Fer-rari, Glo-ria O. Spag-nolo, and Ste-fa-nia

Underfull \hbox (badness 1259) in paragraph at lines 555--559
[]\OT1/ptm/m/n/10 Jeffrey Zhou, Tian-jian Lu, Swa-roop Mishra, Sid-

LaTeX Warning: Reference `tab:error_fm' on page 6 undefined on input line 570.


LaTeX Warning: Reference `tab:error_icc' on page 6 undefined on input line 570.



LaTeX Warning: Reference `sec:app_kappa' on page 6 undefined on input line 614.


[6]

LaTeX Warning: Reference `tab:kappa_summary' on page 7 undefined on input line 
619.


Underfull \hbox (badness 3690) in paragraph at lines 700--700
[]\OT1/ptm/m/n/10 Table 15: |SOP-Bench C1 repli-ca-tion. Over-all

Underfull \hbox (badness 1014) in paragraph at lines 750--752
\OT1/ptm/m/n/10.95 ited. The per-type dif-fi-culty gra-di-ent (con-di-
[7]

Package natbib Warning: There were undefined citations.

[8] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/ut
mb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 212447 bytes).
Transcript written on paper.log.
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo)) (./acl.sty
Conference Style for ACL
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty))))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
Underfull \hbox (badness 1221) in paragraph at lines 23--31
\OT1/ptm/m/n/10 ti-fied. We present the first causal, type-

Underfull \hbox (badness 1087) in paragraph at lines 23--31
\OT1/ptm/m/n/10 per-tur-ba-tion con-trol across 2,997 episodes,

Underfull \hbox (badness 1424) in paragraph at lines 23--31
\OT1/ptm/m/n/10 bi-gu-ity types, we es-tab-lish three find-ings.

Underfull \hbox (badness 1237) in paragraph at lines 23--31
\OT1/ptm/m/n/10 First, am-bi-gu-ity causes a +34 percentage-
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)
Underfull \hbox (badness 1014) in paragraph at lines 43--45
\OT1/ptm/m/n/10.95 gov-erned by natural-language poli-cies that in-

Underfull \hbox (badness 1009) in paragraph at lines 57--58
[]\OT1/ptm/b/n/10.95 Causal quan-tifi-ca-tion\OT1/ptm/m/n/10.95 : A +34 percent
age-

Underfull \hbox (badness 10000) in paragraph at lines 57--58
\OT1/ptm/m/n/10.95 point in-crease in safety vi-o-la-tions

Underfull \hbox (badness 10000) in paragraph at lines 57--58
\OT1/ptm/m/n/10.95 (OR=15.1) with per-tur-ba-tion con-trol

Underfull \hbox (badness 10000) in paragraph at lines 57--58
\OT1/ptm/m/n/10.95 con-firm-ing ambiguity-specific cau-sa-tion

Underfull \hbox (badness 10000) in paragraph at lines 58--59
[]\OT1/ptm/b/n/10.95 Model$\OMS/cmsy/m/n/10.95 ^^B$\OT1/ptm/b/n/10.95 type in-t
er-ac-tion\OT1/ptm/m/n/10.95 : Authorization-

Underfull \hbox (badness 10000) in paragraph at lines 58--59
\OT1/ptm/m/n/10.95 dif-fer-en-tially mit-i-gates spe-cific am-bi-gu-ity
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
Underfull \hbox (badness 10000) in paragraph at lines 76--79
 []\OT1/ptm/b/n/10.95 Agent Safety Eval-u-a-tion.[] \OT1/ptm/m/n/10.95 ToolEmu 
([][]Ruan

Underfull \hbox (badness 1158) in paragraph at lines 76--79
\OT1/ptm/m/n/10.95 et al.[][], [][]2024[][]) stud-ies prompt in-jec-tion at-tac
ks.

Underfull \hbox (badness 3396) in paragraph at lines 81--84
 []\OT1/ptm/b/n/10.95 Policy Spec-i-fi-ca-tion Qual-ity.[] \OT1/ptm/m/n/10.95 P
han-tom-Pol-icy

Underfull \hbox (badness 10000) in paragraph at lines 90--91
\OT1/ptm/m/n/10.95 We adopt a two-layer, six-type tax-on-omy

Underfull \hbox (badness 2941) in paragraph at lines 96--97
[]\OT1/ptm/b/n/10.95 Conditional prece-dence\OT1/ptm/m/n/10.95 : Con-flict-ing 
rules

Underfull \hbox (badness 5133) in paragraph at lines 101--102
 []\OT1/ptm/b/n/10.95 Linguistic Layer.[] \OT1/ptm/m/n/10.95 Am-bi-gu-i-ties ar
is-ing from

Underfull \hbox (badness 3492) in paragraph at lines 103--104
[]\OT1/ptm/b/n/10.95 Lexical\OT1/ptm/m/n/10.95 : Pol-y-se-mous or context-depen
dent

Underfull \hbox (badness 2460) in paragraph at lines 108--110
\OT1/ptm/m/n/10.95 pos-i-tive and neg-a-tive ex-am-ples, en-abling re-

Underfull \hbox (badness 1694) in paragraph at lines 108--110
\OT1/ptm/m/n/10.95 pro-ducible clause gen-er-a-tion. The spec-i-fi-ca-

Underfull \hbox (badness 3701) in paragraph at lines 108--110
\OT1/ptm/m/n/10.95 ics/semantics di-vide: spec-i-fi-ca-tion am-bi-gu-ity

Overfull \hbox (1.99718pt too wide) in paragraph at lines 125--139
 [][] 
[2]
Overfull \hbox (8.36496pt too wide) in paragraph at lines 177--188
 [][] 

Underfull \hbox (badness 1748) in paragraph at lines 224--225
\OT1/ptm/m/n/10.95 To dis-tin-guish ambiguity-specific ef-fects from

Underfull \hbox (badness 1264) in paragraph at lines 239--239
\OT1/ptm/m/n/10 sur-face changes pro-duce $\OT1/cmr/m/n/10 ^^A$\OT1/ptm/m/n/10 
=$\OMS/cmsy/m/n/10 ^^@$\OT1/ptm/m/n/10 0.67pp (CI con-tains

Underfull \vbox (badness 1527) has occurred while \output is active [3]
Underfull \hbox (badness 2189) in paragraph at lines 334--338
[]\OT1/ptm/m/n/10.95 The om-nibus test is sig-nif-i-cant ($\OML/cmm/m/it/10.95 
^^_[]$\OT1/ptm/m/n/10.95 =28.02,

Underfull \hbox (badness 10000) in paragraph at lines 334--338
\OML/cmm/m/it/10.95 p$\OT1/ptm/m/n/10.95 =3.6$\OMS/cmsy/m/n/10.95 ^^B$\OT1/ptm/
m/n/10.95 10$[]$, Cram[]er's $\OML/cmm/m/it/10.95 V$\OT1/ptm/m/n/10.95 =0.137).
 While

Underfull \hbox (badness 5924) in paragraph at lines 334--338
\OML/cmm/m/it/10.95 V$\OT1/ptm/m/n/10.95 =0.137 falls be-low the con-ven-tional
 0.20

Underfull \hbox (badness 4416) in paragraph at lines 334--338
\OT1/ptm/m/n/10.95 medium-effect thresh-old, sta-tis-ti-cal power is

Underfull \hbox (badness 1107) in paragraph at lines 334--338
\OT1/ptm/m/n/10.95 0.993 with MDE=0.093, and the hi-er-ar-chy is

Underfull \hbox (badness 1137) in paragraph at lines 334--338
\OT1/ptm/m/n/10.95 well-powered. A three-tier struc-ture emerges

Underfull \hbox (badness 1796) in paragraph at lines 334--338
\OT1/ptm/m/n/10.95 (31.6%) is low-est but still causes sub-stan-tial

Overfull \hbox (21.24013pt too wide) in paragraph at lines 347--356
 [][] 

Underfull \hbox (badness 2126) in paragraph at lines 360--363
[]\OT1/ptm/m/n/10.95 The pooled ef-fect ($\OT1/cmr/m/n/10.95 ^^A$\OT1/ptm/m/n/1
0.95 =6.08pp, $\OML/cmm/m/it/10.95 p$\OT1/ptm/m/n/10.95 =0.017) is

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 364.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\times' on input line 364.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 364.


Underfull \hbox (badness 10000) in paragraph at lines 393--394
[]\OT1/ptm/b/n/10.95 Authorization scope \OT1/ptm/m/n/10.95 is the model-
[4]
Underfull \hbox (badness 2809) in paragraph at lines 395--396
[]\OT1/ptm/b/n/10.95 Conditional prece-dence \OT1/ptm/m/n/10.95 is model-invari
ant:

Underfull \hbox (badness 2828) in paragraph at lines 403--406
 []\OT1/ptm/b/n/10.95 Open-Source Mod-els.[] \OT1/ptm/m/n/10.95 The two open-so
urce

Underfull \hbox (badness 3679) in paragraph at lines 418--420
 []\OT1/ptm/b/n/10.95 Systematic Nocu-ity.[] \OT1/ptm/m/n/10.95 In 27% of am-bi
gu-ous
[5]
No file paper.bbl.

Underfull \hbox (badness 5288) in paragraph at lines 471--475
[]\OT1/ptm/m/n/10 Saad Ezzini, Sal-lam Abual-haija, Chetan Arora,

Underfull \hbox (badness 1102) in paragraph at lines 483--487
[]\OT1/ptm/m/n/10 Alessio Fer-rari, Glo-ria O. Spag-nolo, and Ste-fa-nia

Underfull \hbox (badness 1259) in paragraph at lines 555--559
[]\OT1/ptm/m/n/10 Jeffrey Zhou, Tian-jian Lu, Swa-roop Mishra, Sid-

LaTeX Warning: `h' float specifier changed to `ht'.

[6]

LaTeX Warning: `h' float specifier changed to `ht'.


Underfull \hbox (badness 3690) in paragraph at lines 700--700
[]\OT1/ptm/m/n/10 Table 15: |SOP-Bench C1 repli-ca-tion. Over-all

LaTeX Warning: `h' float specifier changed to `ht'.


Underfull \hbox (badness 1014) in paragraph at lines 750--752
\OT1/ptm/m/n/10.95 ited. The per-type dif-fi-culty gra-di-ent (con-di-
[7] [8] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/ut
mb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 217620 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6393d33b-196b-48db-85d3-41cd50663085",
  "isSidechain": false,
  "promptId": "128f9fd8-c2a5-4ade-82e9-ac2ac23ec257",
  "type": "user",
  "uuid": "1cc2efa0-8c40-491c-a1e9-6e7b6f1c5330",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo)) (./acl.sty\nConference Style for ACL\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty))))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\nUnderfull \\hbox (badness 1221) in paragraph at lines 23--31\n\\OT1/ptm/m/n/10 ti-fied. We present the first causal, type-\n\nUnderfull \\hbox (badness 1087) in paragraph at lines 23--31\n\\OT1/ptm/m/n/10 per-tur-ba-tion con-trol across 2,997 episodes,\n\nUnderfull \\hbox (badness 1424) in paragraph at lines 23--31\n\\OT1/ptm/m/n/10 bi-gu-ity types, we es-tab-lish three find-ings.\n\nUnderfull \\hbox (badness 1237) in paragraph at lines 23--31\n\\OT1/ptm/m/n/10 First, am-bi-gu-ity causes a +34 percentage-\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n\nPackage natbib Warning: Citation `berry2003ambiguity' on page 1 undefined on in\nput line 43.\n\n\nPackage natbib Warning: Citation `massey2014automated' on page 1 undefined on i\nnput line 43.\n\n\nPackage natbib Warning: Citation `li2024drip' on page 1 undefined on input line\n 44.\n\n\nPackage natbib Warning: Citation `massey2014automated' on page 1 undefined on i\nnput line 44.\n\n\nPackage natbib Warning: Citation `ruan2024toolemu' on page 1 undefined on input\n line 44.\n\n\nPackage natbib Warning: Citation `yuan2024rjudge' on page 1 undefined on input \nline 44.\n\n\nUnderfull \\hbox (badness 1014) in paragraph at lines 43--45\n\\OT1/ptm/m/n/10.95 gov-erned by natural-language poli-cies that in-\n\nPackage natbib Warning: Citation `berry2003ambiguity' on page 1 undefined on in\nput line 46.\n\n\nPackage natbib Warning: Citation `yao2024tau' on page 1 undefined on input line\n 53.\n\n\nUnderfull \\hbox (badness 1009) in paragraph at lines 57--58\n[]\\OT1/ptm/b/n/10.95 Causal quan-tifi-ca-tion\\OT1/ptm/m/n/10.95 : A +34 percent\nage-\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 57--58\n\\OT1/ptm/m/n/10.95 point in-crease in safety vi-o-la-tions\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 57--58\n\\OT1/ptm/m/n/10.95 (OR=15.1) with per-tur-ba-tion con-trol\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 57--58\n\\OT1/ptm/m/n/10.95 con-firm-ing ambiguity-specific cau-sa-tion\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 58--59\n[]\\OT1/ptm/b/n/10.95 Model$\\OMS/cmsy/m/n/10.95 ^^B$\\OT1/ptm/b/n/10.95 type in-t\ner-ac-tion\\OT1/ptm/m/n/10.95 : Authorization-\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 58--59\n\\OT1/ptm/m/n/10.95 dif-fer-en-tially mit-i-gates spe-cific am-bi-gu-ity\n\nPackage natbib Warning: Citation `li2024drip' on page 1 undefined on input line\n 68.\n\n\nPackage natbib Warning: Citation `massey2014automated' on page 1 undefined on i\nnput line 69.\n\n\nPackage natbib Warning: Citation `chantree2006identifying' on page 1 undefined \non input line 70.\n\n\nPackage natbib Warning: Citation `ferrari2017detecting' on page 1 undefined on \ninput line 71.\n\n\nPackage natbib Warning: Citation `berry2003ambiguity' on page 1 undefined on in\nput line 72.\n\n\nPackage natbib Warning: Citation `ferreira2002good' on page 1 undefined on inpu\nt line 72.\n\n\nPackage natbib Warning: Citation `frazier1982making' on page 1 undefined on inp\nut line 72.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `ruan2024toolemu' on page 2 undefined on input\n line 76.\n\n\nPackage natbib Warning: Citation `yuan2024rjudge' on page 2 undefined on input \nline 76.\n\n\nPackage natbib Warning: Citation `zhan2024injecagent' on page 2 undefined on in\nput line 76.\n\n\nPackage natbib Warning: Citation `zhou2023instruction' on page 2 undefined on i\nnput line 78.\n\n\nPackage natbib Warning: Citation `sclar2024quantifying' on page 2 undefined on \ninput line 78.\n\n\nPackage natbib Warning: Citation `li2025phantompolicy' on page 2 undefined on i\nnput line 81.\n\n\nPackage natbib Warning: Citation `willis2008automatic' on page 2 undefined on i\nnput line 82.\n\n\nPackage natbib Warning: Citation `ezzini2022taphsir' on page 2 undefined on inp\nut line 82.\n\n\nUnderfull \\hbox (badness 3396) in paragraph at lines 81--84\n []\\OT1/ptm/b/n/10.95 Policy Spec-i-fi-ca-tion Qual-ity.[] \\OT1/ptm/m/n/10.95 P\nhan-tom-Pol-icy\n\nPackage natbib Warning: Citation `li2024drip' on page 2 undefined on input line\n 90.\n\n\nPackage natbib Warning: Citation `massey2014automated' on page 2 undefined on i\nnput line 90.\n\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 90--91\n\\OT1/ptm/m/n/10.95 We adopt a two-layer, six-type tax-on-omy\n\nUnderfull \\hbox (badness 2941) in paragraph at lines 96--97\n[]\\OT1/ptm/b/n/10.95 Conditional prece-dence\\OT1/ptm/m/n/10.95 : Con-flict-ing \nrules\n\nUnderfull \\hbox (badness 5133) in paragraph at lines 101--102\n []\\OT1/ptm/b/n/10.95 Linguistic Layer.[] \\OT1/ptm/m/n/10.95 Am-bi-gu-i-ties ar\nis-ing from\n\nUnderfull \\hbox (badness 3492) in paragraph at lines 103--104\n[]\\OT1/ptm/b/n/10.95 Lexical\\OT1/ptm/m/n/10.95 : Pol-y-se-mous or context-depen\ndent\n\nUnderfull \\hbox (badness 2460) in paragraph at lines 108--110\n\\OT1/ptm/m/n/10.95 pos-i-tive and neg-a-tive ex-am-ples, en-abling re-\n\nUnderfull \\hbox (badness 1694) in paragraph at lines 108--110\n\\OT1/ptm/m/n/10.95 pro-ducible clause gen-er-a-tion. The spec-i-fi-ca-\n\nUnderfull \\hbox (badness 3701) in paragraph at lines 108--110\n\\OT1/ptm/m/n/10.95 ics/semantics di-vide: spec-i-fi-ca-tion am-bi-gu-ity\n\nLaTeX Warning: Reference `tab:clause_gen' on page 2 undefined on input line 120\n.\n\n\nOverfull \\hbox (1.99718pt too wide) in paragraph at lines 125--139\n [][] \n\nPackage natbib Warning: Citation `yao2024tau' on page 2 undefined on input line\n 158.\n\n[2]\n\nLaTeX Warning: Reference `tab:judge_cal' on page 3 undefined on input line 172.\n\n\n\nOverfull \\hbox (8.36496pt too wide) in paragraph at lines 177--188\n [][] \n\nPackage natbib Warning: Citation `li2024drip' on page 3 undefined on input line\n 198.\n\n\nLaTeX Warning: Reference `tab:realism' on page 3 undefined on input line 198.\n\n\nLaTeX Warning: Reference `sec:perturbation' on page 3 undefined on input line 2\n19.\n\n\nLaTeX Warning: Reference `tab:perturbation' on page 3 undefined on input line 2\n24.\n\n\nUnderfull \\hbox (badness 1748) in paragraph at lines 224--225\n\\OT1/ptm/m/n/10.95 To dis-tin-guish ambiguity-specific ef-fects from\n\nUnderfull \\hbox (badness 1264) in paragraph at lines 239--239\n\\OT1/ptm/m/n/10 sur-face changes pro-duce $\\OT1/cmr/m/n/10 ^^A$\\OT1/ptm/m/n/10 \n=$\\OMS/cmsy/m/n/10 ^^@$\\OT1/ptm/m/n/10 0.67pp (CI con-tains\n\nLaTeX Warning: Reference `tab:reliability' on page 3 undefined on input line 24\n9.\n\n[3]\n\nLaTeX Warning: Reference `tab:c1' on page 4 undefined on input line 283.\n\n\nLaTeX Warning: Reference `tab:c2' on page 4 undefined on input line 313.\n\n\nUnderfull \\hbox (badness 2189) in paragraph at lines 334--338\n[]\\OT1/ptm/m/n/10.95 The om-nibus test is sig-nif-i-cant ($\\OML/cmm/m/it/10.95 \n^^_[]$\\OT1/ptm/m/n/10.95 =28.02,\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 334--338\n\\OML/cmm/m/it/10.95 p$\\OT1/ptm/m/n/10.95 =3.6$\\OMS/cmsy/m/n/10.95 ^^B$\\OT1/ptm/\nm/n/10.95 10$[]$, Cram[]er's $\\OML/cmm/m/it/10.95 V$\\OT1/ptm/m/n/10.95 =0.137).\n While\n\nUnderfull \\hbox (badness 5924) in paragraph at lines 334--338\n\\OML/cmm/m/it/10.95 V$\\OT1/ptm/m/n/10.95 =0.137 falls be-low the con-ven-tional\n 0.20\n\nUnderfull \\hbox (badness 4416) in paragraph at lines 334--338\n\\OT1/ptm/m/n/10.95 medium-effect thresh-old, sta-tis-ti-cal power is\n\nUnderfull \\hbox (badness 1107) in paragraph at lines 334--338\n\\OT1/ptm/m/n/10.95 0.993 with MDE=0.093, and the hi-er-ar-chy is\n\nUnderfull \\hbox (badness 1137) in paragraph at lines 334--338\n\\OT1/ptm/m/n/10.95 well-powered. A three-tier struc-ture emerges\n\nUnderfull \\hbox (badness 1796) in paragraph at lines 334--338\n\\OT1/ptm/m/n/10.95 (31.6%) is low-est but still causes sub-stan-tial\n\nLaTeX Warning: Reference `tab:c3' on page 4 undefined on input line 342.\n\n\nOverfull \\hbox (21.24013pt too wide) in paragraph at lines 347--356\n [][] \n\nUnderfull \\hbox (badness 2126) in paragraph at lines 360--363\n[]\\OT1/ptm/m/n/10.95 The pooled ef-fect ($\\OT1/cmr/m/n/10.95 ^^A$\\OT1/ptm/m/n/1\n0.95 =6.08pp, $\\OML/cmm/m/it/10.95 p$\\OT1/ptm/m/n/10.95 =0.017) is\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 364.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\times' on input line 364.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 364.\n\n\nLaTeX Warning: Reference `tab:c4' on page 4 undefined on input line 367.\n\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 393--394\n[]\\OT1/ptm/b/n/10.95 Authorization scope \\OT1/ptm/m/n/10.95 is the model-\n[4]\nUnderfull \\hbox (badness 2809) in paragraph at lines 395--396\n[]\\OT1/ptm/b/n/10.95 Conditional prece-dence \\OT1/ptm/m/n/10.95 is model-invari\nant:\n\nUnderfull \\hbox (badness 2828) in paragraph at lines 403--406\n []\\OT1/ptm/b/n/10.95 Open-Source Mod-els.[] \\OT1/ptm/m/n/10.95 The two open-so\nurce\n\nPackage natbib Warning: Citation `berry2003ambiguity' on page 5 undefined on in\nput line 413.\n\n\nUnderfull \\hbox (badness 3679) in paragraph at lines 418--420\n []\\OT1/ptm/b/n/10.95 Systematic Nocu-ity.[] \\OT1/ptm/m/n/10.95 In 27% of am-bi\ngu-ous\n\nLaTeX Warning: Reference `sec:app_error' on page 5 undefined on input line 422.\n\n\n\nLaTeX Warning: Reference `sec:app_kappa' on page 5 undefined on input line 424.\n\n\n\nLaTeX Warning: Reference `sec:app_sopbench' on page 5 undefined on input line 4\n35.\n\n\nLaTeX Warning: Reference `tab:realism' on page 5 undefined on input line 436.\n\n\nLaTeX Warning: Reference `sec:app_kappa' on page 5 undefined on input line 437.\n\n\nNo file paper.bbl.\n[5]\nUnderfull \\hbox (badness 5288) in paragraph at lines 471--475\n[]\\OT1/ptm/m/n/10 Saad Ezzini, Sal-lam Abual-haija, Chetan Arora,\n\nUnderfull \\hbox (badness 1102) in paragraph at lines 483--487\n[]\\OT1/ptm/m/n/10 Alessio Fer-rari, Glo-ria O. Spag-nolo, and Ste-fa-nia\n\nUnderfull \\hbox (badness 1259) in paragraph at lines 555--559\n[]\\OT1/ptm/m/n/10 Jeffrey Zhou, Tian-jian Lu, Swa-roop Mishra, Sid-\n\nLaTeX Warning: Reference `tab:error_fm' on page 6 undefined on input line 570.\n\n\nLaTeX Warning: Reference `tab:error_icc' on page 6 undefined on input line 570.\n\n\n\nLaTeX Warning: Reference `sec:app_kappa' on page 6 undefined on input line 614.\n\n\n[6]\n\nLaTeX Warning: Reference `tab:kappa_summary' on page 7 undefined on input line \n619.\n\n\nUnderfull \\hbox (badness 3690) in paragraph at lines 700--700\n[]\\OT1/ptm/m/n/10 Table 15: |SOP-Bench C1 repli-ca-tion. Over-all\n\nUnderfull \\hbox (badness 1014) in paragraph at lines 750--752\n\\OT1/ptm/m/n/10.95 ited. The per-type dif-fi-culty gra-di-ent (con-di-\n[7]\n\nPackage natbib Warning: There were undefined citations.\n\n[8] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/ut\nmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 212447 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo)) (./acl.sty\nConference Style for ACL\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty))))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\nUnderfull \\hbox (badness 1221) in paragraph at lines 23--31\n\\OT1/ptm/m/n/10 ti-fied. We present the first causal, type-\n\nUnderfull \\hbox (badness 1087) in paragraph at lines 23--31\n\\OT1/ptm/m/n/10 per-tur-ba-tion con-trol across 2,997 episodes,\n\nUnderfull \\hbox (badness 1424) in paragraph at lines 23--31\n\\OT1/ptm/m/n/10 bi-gu-ity types, we es-tab-lish three find-ings.\n\nUnderfull \\hbox (badness 1237) in paragraph at lines 23--31\n\\OT1/ptm/m/n/10 First, am-bi-gu-ity causes a +34 percentage-\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\nUnderfull \\hbox (badness 1014) in paragraph at lines 43--45\n\\OT1/ptm/m/n/10.95 gov-erned by natural-language poli-cies that in-\n\nUnderfull \\hbox (badness 1009) in paragraph at lines 57--58\n[]\\OT1/ptm/b/n/10.95 Causal quan-tifi-ca-tion\\OT1/ptm/m/n/10.95 : A +34 percent\nage-\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 57--58\n\\OT1/ptm/m/n/10.95 point in-crease in safety vi-o-la-tions\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 57--58\n\\OT1/ptm/m/n/10.95 (OR=15.1) with per-tur-ba-tion con-trol\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 57--58\n\\OT1/ptm/m/n/10.95 con-firm-ing ambiguity-specific cau-sa-tion\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 58--59\n[]\\OT1/ptm/b/n/10.95 Model$\\OMS/cmsy/m/n/10.95 ^^B$\\OT1/ptm/b/n/10.95 type in-t\ner-ac-tion\\OT1/ptm/m/n/10.95 : Authorization-\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 58--59\n\\OT1/ptm/m/n/10.95 dif-fer-en-tially mit-i-gates spe-cific am-bi-gu-ity\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\nUnderfull \\hbox (badness 10000) in paragraph at lines 76--79\n []\\OT1/ptm/b/n/10.95 Agent Safety Eval-u-a-tion.[] \\OT1/ptm/m/n/10.95 ToolEmu \n([][]Ruan\n\nUnderfull \\hbox (badness 1158) in paragraph at lines 76--79\n\\OT1/ptm/m/n/10.95 et al.[][], [][]2024[][]) stud-ies prompt in-jec-tion at-tac\nks.\n\nUnderfull \\hbox (badness 3396) in paragraph at lines 81--84\n []\\OT1/ptm/b/n/10.95 Policy Spec-i-fi-ca-tion Qual-ity.[] \\OT1/ptm/m/n/10.95 P\nhan-tom-Pol-icy\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 90--91\n\\OT1/ptm/m/n/10.95 We adopt a two-layer, six-type tax-on-omy\n\nUnderfull \\hbox (badness 2941) in paragraph at lines 96--97\n[]\\OT1/ptm/b/n/10.95 Conditional prece-dence\\OT1/ptm/m/n/10.95 : Con-flict-ing \nrules\n\nUnderfull \\hbox (badness 5133) in paragraph at lines 101--102\n []\\OT1/ptm/b/n/10.95 Linguistic Layer.[] \\OT1/ptm/m/n/10.95 Am-bi-gu-i-ties ar\nis-ing from\n\nUnderfull \\hbox (badness 3492) in paragraph at lines 103--104\n[]\\OT1/ptm/b/n/10.95 Lexical\\OT1/ptm/m/n/10.95 : Pol-y-se-mous or context-depen\ndent\n\nUnderfull \\hbox (badness 2460) in paragraph at lines 108--110\n\\OT1/ptm/m/n/10.95 pos-i-tive and neg-a-tive ex-am-ples, en-abling re-\n\nUnderfull \\hbox (badness 1694) in paragraph at lines 108--110\n\\OT1/ptm/m/n/10.95 pro-ducible clause gen-er-a-tion. The spec-i-fi-ca-\n\nUnderfull \\hbox (badness 3701) in paragraph at lines 108--110\n\\OT1/ptm/m/n/10.95 ics/semantics di-vide: spec-i-fi-ca-tion am-bi-gu-ity\n\nOverfull \\hbox (1.99718pt too wide) in paragraph at lines 125--139\n [][] \n[2]\nOverfull \\hbox (8.36496pt too wide) in paragraph at lines 177--188\n [][] \n\nUnderfull \\hbox (badness 1748) in paragraph at lines 224--225\n\\OT1/ptm/m/n/10.95 To dis-tin-guish ambiguity-specific ef-fects from\n\nUnderfull \\hbox (badness 1264) in paragraph at lines 239--239\n\\OT1/ptm/m/n/10 sur-face changes pro-duce $\\OT1/cmr/m/n/10 ^^A$\\OT1/ptm/m/n/10 \n=$\\OMS/cmsy/m/n/10 ^^@$\\OT1/ptm/m/n/10 0.67pp (CI con-tains\n\nUnderfull \\vbox (badness 1527) has occurred while \\output is active [3]\nUnderfull \\hbox (badness 2189) in paragraph at lines 334--338\n[]\\OT1/ptm/m/n/10.95 The om-nibus test is sig-nif-i-cant ($\\OML/cmm/m/it/10.95 \n^^_[]$\\OT1/ptm/m/n/10.95 =28.02,\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 334--338\n\\OML/cmm/m/it/10.95 p$\\OT1/ptm/m/n/10.95 =3.6$\\OMS/cmsy/m/n/10.95 ^^B$\\OT1/ptm/\nm/n/10.95 10$[]$, Cram[]er's $\\OML/cmm/m/it/10.95 V$\\OT1/ptm/m/n/10.95 =0.137).\n While\n\nUnderfull \\hbox (badness 5924) in paragraph at lines 334--338\n\\OML/cmm/m/it/10.95 V$\\OT1/ptm/m/n/10.95 =0.137 falls be-low the con-ven-tional\n 0.20\n\nUnderfull \\hbox (badness 4416) in paragraph at lines 334--338\n\\OT1/ptm/m/n/10.95 medium-effect thresh-old, sta-tis-ti-cal power is\n\nUnderfull \\hbox (badness 1107) in paragraph at lines 334--338\n\\OT1/ptm/m/n/10.95 0.993 with MDE=0.093, and the hi-er-ar-chy is\n\nUnderfull \\hbox (badness 1137) in paragraph at lines 334--338\n\\OT1/ptm/m/n/10.95 well-powered. A three-tier struc-ture emerges\n\nUnderfull \\hbox (badness 1796) in paragraph at lines 334--338\n\\OT1/ptm/m/n/10.95 (31.6%) is low-est but still causes sub-stan-tial\n\nOverfull \\hbox (21.24013pt too wide) in paragraph at lines 347--356\n [][] \n\nUnderfull \\hbox (badness 2126) in paragraph at lines 360--363\n[]\\OT1/ptm/m/n/10.95 The pooled ef-fect ($\\OT1/cmr/m/n/10.95 ^^A$\\OT1/ptm/m/n/1\n0.95 =6.08pp, $\\OML/cmm/m/it/10.95 p$\\OT1/ptm/m/n/10.95 =0.017) is\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 364.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\times' on input line 364.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 364.\n\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 393--394\n[]\\OT1/ptm/b/n/10.95 Authorization scope \\OT1/ptm/m/n/10.95 is the model-\n[4]\nUnderfull \\hbox (badness 2809) in paragraph at lines 395--396\n[]\\OT1/ptm/b/n/10.95 Conditional prece-dence \\OT1/ptm/m/n/10.95 is model-invari\nant:\n\nUnderfull \\hbox (badness 2828) in paragraph at lines 403--406\n []\\OT1/ptm/b/n/10.95 Open-Source Mod-els.[] \\OT1/ptm/m/n/10.95 The two open-so\nurce\n\nUnderfull \\hbox (badness 3679) in paragraph at lines 418--420\n []\\OT1/ptm/b/n/10.95 Systematic Nocu-ity.[] \\OT1/ptm/m/n/10.95 In 27% of am-bi\ngu-ous\n[5]\nNo file paper.bbl.\n\nUnderfull \\hbox (badness 5288) in paragraph at lines 471--475\n[]\\OT1/ptm/m/n/10 Saad Ezzini, Sal-lam Abual-haija, Chetan Arora,\n\nUnderfull \\hbox (badness 1102) in paragraph at lines 483--487\n[]\\OT1/ptm/m/n/10 Alessio Fer-rari, Glo-ria O. Spag-nolo, and Ste-fa-nia\n\nUnderfull \\hbox (badness 1259) in paragraph at lines 555--559\n[]\\OT1/ptm/m/n/10 Jeffrey Zhou, Tian-jian Lu, Swa-roop Mishra, Sid-\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nUnderfull \\hbox (badness 3690) in paragraph at lines 700--700\n[]\\OT1/ptm/m/n/10 Table 15: |SOP-Bench C1 repli-ca-tion. Over-all\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nUnderfull \\hbox (badness 1014) in paragraph at lines 750--752\n\\OT1/ptm/m/n/10.95 ited. The per-type dif-fi-culty gra-di-ent (con-di-\n[7] [8] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/ut\nmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 217620 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6393d33b-196b-48db-85d3-41cd50663085",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260523T185344 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigui…",
  "leafUuid": "1cc2efa0-8c40-491c-a1e9-6e7b6f1c5330",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case tier simulated paper for policy ambiguity research",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4"
}
```

---

### Assistant

_source line 40 · 2026-05-23T19:47:29.870Z_

<details><summary>Logged reasoning block</summary>

```text
The paper compiled but needs one more pass due to "Label(s) may have changed. Rerun to get cross-references right." Let me do one more pass.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cc2efa0-8c40-491c-a1e9-6e7b6f1c5330",
  "isSidechain": false,
  "requestId": "req_011CbL5U6BpxhrmaKf3Sb5KZ",
  "type": "assistant",
  "uuid": "325be167-5df5-4b34-8c8b-ee1236ef7cb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019fPEvf5bJjmgji4SsWLkMz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13327,
      "cache_read_input_tokens": 66512,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 66512,
          "cache_creation_input_tokens": 13327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13327
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

_source line 41 · 2026-05-23T19:47:30.366Z_

Cross-references need one more pass.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "325be167-5df5-4b34-8c8b-ee1236ef7cb4",
  "isSidechain": false,
  "requestId": "req_011CbL5U6BpxhrmaKf3Sb5KZ",
  "type": "assistant",
  "uuid": "abf72529-a94b-4b92-b521-6169789e6bf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019fPEvf5bJjmgji4SsWLkMz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13327,
      "cache_read_input_tokens": 66512,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 66512,
          "cache_creation_input_tokens": 13327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13327
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

_source line 42 · 2026-05-23T19:47:33.696Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KUNCTMoj2Jw8rafy3jnU39`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Third LaTeX pass for stable cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abf72529-a94b-4b92-b521-6169789e6bf1",
  "isSidechain": false,
  "requestId": "req_011CbL5U6BpxhrmaKf3Sb5KZ",
  "type": "assistant",
  "uuid": "16b6837e-0824-49ac-9715-d8e8f50ba09f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019fPEvf5bJjmgji4SsWLkMz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13327,
      "cache_read_input_tokens": 66512,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 66512,
          "cache_creation_input_tokens": 13327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13327
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

_source line 43 · 2026-05-23T19:47:34.595Z_

<details><summary>↩ Tool result · `toolu_01KUNCTMoj2Jw8rafy3jnU39`</summary>

```text
c/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/ut
mb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 217620 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16b6837e-0824-49ac-9715-d8e8f50ba09f",
  "isSidechain": false,
  "promptId": "128f9fd8-c2a5-4ade-82e9-ac2ac23ec257",
  "type": "user",
  "uuid": "b3b373ff-e2f7-47c3-9c87-abe769f1744a",
  "toolUseResult": {
    "stdout": "c/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/ut\nmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 217620 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "16b6837e-0824-49ac-9715-d8e8f50ba09f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-23T19:47:50.742Z_

PDF compiled successfully — 8 pages. The paper covers all 13 experiments:

**Main text (§1–§8):** clause generation (Table 1), pilot validation (§4.2), API study + open-source study (Table 5 — C1), statistical analysis: C2 type hierarchy (Table 6), C3 layer effect (Table 7), C4 model×type interaction (Table 8), judge calibration (Table 3), realism validation (Table 4), perturbation control (Table 5), reliability test (Table 6).

**Appendix A–D:** exploratory error analysis (Tables 9–10, demoted with κ caveat), κ re-annotation failure (Tables 11–13), SOPBench cross-benchmark (Tables 14–16), DeBERTa classifier PoC (Table 17).

Framing follows worst-tier guidance: title pivots to "Measuring Differential Vulnerability," C5 demoted to appendix as "exploratory automated analysis," Ambiguity Blindness retained as one-paragraph Discussion observation, SOPBench weakness acknowledged in Limitations, Discussion focuses on deployment implications rather than mechanism.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3b373ff-e2f7-47c3-9c87-abe769f1744a",
  "isSidechain": false,
  "requestId": "req_011CbL5UfaWa7a248aaL91mi",
  "type": "assistant",
  "uuid": "41e8023a-e29f-46df-9ae1-3cf1c17dd47f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/worst",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDvdf18ZUCS4bbuUrP5Zic",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 331,
      "cache_read_input_tokens": 79839,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 79839,
          "cache_creation_input_tokens": 331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 331
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

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260523T185344 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigui…",
  "leafUuid": "41e8023a-e29f-46df-9ae1-3cf1c17dd47f",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case tier simulated paper for policy ambiguity research",
  "sessionId": "59cefd27-46c9-44eb-ac5b-a7739b04eea4"
}
```

---
