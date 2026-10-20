# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/92616111-09cc-4079-a3df-7d5669f885d3.jsonl`
- **Structured JSON:** [`9bbab854960b514e4e8d.json`](../../sessions/9b/9bbab854960b514e4e8d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T16:45:51.695Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T16:45:51.695Z",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：全 18 runs（9 seeds × 2 encoders × 3 strategies）完整复现 pilot pattern。 Embedding mining 在两个 encoder 上均显著优于 random（Qwen +2.0pp, StarCoder +1.5pp, 95% CI 下界 > 0）。 Dataflow 在 Qwen 上条件性获益（+1.0pp, CI 下界 > 0），StarCoder 上无显著差异（-0.2pp, CI 含零）。 BM25 baseline 实证关闭 CoCoHaNeRe 论证（BM25 vs random: Qwen -2.5pp, StarCoder -2.7pp）。 SWE-bench Lite downstream +2.5pp embedding, +3.2pp dataflow resolve rate delta。 三条 claim 原样成立，EMNLP Main 强投 framing 无需调整。 M2 full anchors — Qwen random R@1=0.545, embedding=0.565, dataflow=0.555; StarCoder random R@1=0.460, embedding=0.475, dataflow=0.458。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T16:45:51.699Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T16:45:51.699Z",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-14T16:45:51.719Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：全 18 runs（9 seeds × 2 encoders × 3 strategies）完整复现 pilot pattern。 Embedding mining 在两个 encoder 上均显著优于 random（Qwen +2.0pp, StarCoder +1.5pp, 95% CI 下界 > 0）。 Dataflow 在 Qwen 上条件性获益（+1.0pp, CI 下界 > 0），StarCoder 上无显著差异（-0.2pp, CI 含零）。 BM25 baseline 实证关闭 CoCoHaNeRe 论证（BM25 vs random: Qwen -2.5pp, StarCoder -2.7pp）。 SWE-bench Lite downstream +2.5pp embedding, +3.2pp dataflow resolve rate delta。 三条 claim 原样成立，EMNLP Main 强投 framing 无需调整。 M2 full anchors — Qwen random R@1=0.545, embedding=0.565, dataflow=0.555; StarCoder random R@1=0.460, embedding=0.475, dataflow=0.458。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "7dbbfae7-135c-4257-9519-f147e9c1c35b",
  "type": "user",
  "uuid": "a8e7f610-bc8d-463d-9f31-aafd14ece5d6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T16:45:51.718Z_

```json
{
  "parentUuid": "a8e7f610-bc8d-463d-9f31-aafd14ece5d6",
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
  "uuid": "390dd805-3543-4830-ad28-86574bf1e8a3",
  "timestamp": "2026-05-14T16:45:51.718Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T16:45:51.718Z_

```json
{
  "parentUuid": "390dd805-3543-4830-ad28-86574bf1e8a3",
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
  "uuid": "d3537fa7-a445-4ece-bc69-09b80f77a979",
  "timestamp": "2026-05-14T16:45:51.718Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T16:45:51.718Z_

```json
{
  "parentUuid": "d3537fa7-a445-4ece-bc69-09b80f77a979",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f927361c-a0ad-4d0a-b454-c2ae95e0f5ef",
  "timestamp": "2026-05-14T16:45:51.718Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
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
  "aiTitle": "Generate complete simulation paper with experimental data",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3"
}
```

---

### Assistant

_source line 8 · 2026-05-14T16:45:56.807Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f927361c-a0ad-4d0a-b454-c2ae95e0f5ef",
  "isSidechain": false,
  "requestId": "req_011Cb2oLj4DCtPTWbbDJWY3b",
  "type": "assistant",
  "uuid": "af3bebc0-4b45-4adb-b084-9c484fa03ca3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PMEDfKvgddkXzYGkN38Ab",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11736,
      "cache_read_input_tokens": 11447,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11736
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

_source line 9 · 2026-05-14T16:45:57.340Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QRcXBqwrZQwWT47FL3jfBX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af3bebc0-4b45-4adb-b084-9c484fa03ca3",
  "isSidechain": false,
  "requestId": "req_011Cb2oLj4DCtPTWbbDJWY3b",
  "type": "assistant",
  "uuid": "64e68f0d-17f7-400c-bef0-85f46478cc5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PMEDfKvgddkXzYGkN38Ab",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11736,
      "cache_read_input_tokens": 11447,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11736
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

_source line 10 · 2026-05-14T16:45:57.633Z_

<details><summary>↩ Tool result · `toolu_01QRcXBqwrZQwWT47FL3jfBX`</summary>

```text
1	[
2	  {
3	    "name": "SWE-bench Lite End-to-End Evaluation",
4	    "description": "3 strategies × best Qwen checkpoint, Qwen3.6-27B agent, 300 SWE-bench Lite instances. Retriever 提供 top-k context files，agent 生成 patch，评估 resolve rate。\n",
5	    "results": {
6	      "random_resolve_rate": 0.22,
7	      "random_resolved_count": 66,
8	      "embedding_resolve_rate": 0.245,
9	      "embedding_resolved_count": 73,
10	      "dataflow_resolve_rate": 0.252,
11	      "dataflow_resolved_count": 76,
12	      "embedding_minus_random_pp": 2.5,
13	      "dataflow_minus_random_pp": 3.2,
14	      "dataflow_minus_embedding_pp": 0.7,
15	      "total_instances": 300,
16	      "retriever_top_k": 5,
17	      "agent_model": "Qwen3.6-27B"
18	    },
19	    "tables": [
20	      {
21	        "name": "Table 4: SWE-bench Lite Resolve Rate",
22	        "columns": [
23	          "Strategy",
24	          "Resolved",
25	          "Total",
26	          "Rate (%)",
27	          "Δ vs Random (pp)"
28	        ],
29	        "rows": [
30	          [
31	            "random",
32	            66,
33	            300,
34	            22.0,
35	            "—"
36	          ],
37	          [
38	            "embedding",
39	            73,
40	            300,
41	            24.3,
42	            "+2.3"
43	          ],
44	          [
45	            "dataflow",
46	            76,
47	            300,
48	            25.3,
49	            "+3.3"
50	          ]
51	        ]
52	      },
53	      {
54	        "name": "Table 4b: SWE-bench by Patch Complexity",
55	        "columns": [
56	          "Patch Type",
57	          "N",
58	          "random (%)",
59	          "embedding (%)",
60	          "dataflow (%)"
61	        ],
62	        "rows": [
63	          [
64	            "single-file",
65	            189,
66	            28.0,
67	            30.7,
68	            30.2
69	          ],
70	          [
71	            "multi-file",
72	            111,
73	            11.7,
74	            14.4,
75	            17.1
76	          ]
77	        ]
78	      }
79	    ],
80	    "figures": [],
81	    "analysis": "Multi-file patches（占 37%）是 dataflow 拉开差距的主要来源：dataflow 在 multi-file 上 +5.4pp vs random，远大于 single-file 的 +2.2pp。这与 Claim 2 一致——dataflow negatives 使 retriever 更好地理解跨模块依赖。Embedding vs random 在 multi-file 上也有 +2.7pp，说明更难的 negatives 普遍有益。总体 resolve rate 22-25% 与 SweRank/SWE-Fixer 文献报告的 retriever-only baseline 一致。\n\n\nEmbedding retriever 在 SWE-bench 上提升 +2.5pp，因为 bug-fix patch 通常涉及与 issue 描述 语义相似但非完全匹配的文件——embedding mining 训练使 retriever 更擅长区分\"近似但无关\" 与\"近似且相关\"的文件。Dataflow 额外提升 +0.7pp（总 +3.2pp vs random）因为 SWE-bench patch 经常跨函数/跨模块（约 40% 涉及 caller-callee 关系），dataflow negatives 训练使 retriever 理解\"调用链上的文件更可能共同出现在 patch 中\"。Delta 幅度从 retrieval R@1 的 +2.0/+1.0pp 放大到下游 resolve rate 的 +2.5/+3.2pp，符合检索质量在端到端任务中 的杠杆效应——正确检索一个关键文件可以使原本完全失败的 patch 变为可解决。 效果幅度在 swebench_resolve_rate_delta_pp [1.5, 4.0] 范围内。\n"
82	  },
83	  {
84	    "name": "RepoBench-R Cross-File Retrieval with Multi-Seed CIs",
85	    "description": "RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 9 seeds × 3 strategies × 2 encoders，报告 R@1 均值 + 95% bootstrap CI。\n",
86	    "results": {
87	      "qwen_test_hard": {
88	        "random_R1_mean": 0.621,
89	        "random_R1_ci": [
90	          0.614,
91	          0.628
92	        ],
93	        "embedding_R1_mean": 0.642,
94	        "embedding_R1_ci": [
95	          0.634,
96	          0.65
97	        ],
98	        "dataflow_R1_mean": 0.633,
99	        "dataflow_R1_ci": [
100	          0.624,
101	          0.642
102	        ],
103	        "embedding_minus_random_pp": 2.1,
104	        "dataflow_minus_random_pp": 1.2
105	      },
106	      "qwen_test_easy": {
107	        "random_R1_mean": 0.843,
108	        "embedding_R1_mean": 0.855,
109	        "dataflow_R1_mean": 0.85,
110	        "embedding_minus_random_pp": 1.2
111	      },
112	      "starcoder_test_hard": {
113	        "random_R1_mean": 0.574,
114	        "random_R1_ci": [
115	          0.566,
116	          0.582
117	        ],
118	        "embedding_R1_mean": 0.589,
119	        "embedding_R1_ci": [
120	          0.58,
121	          0.598
122	        ],
123	        "dataflow_R1_mean": 0.572,
124	        "dataflow_R1_ci": [
125	          0.562,
126	          0.582
127	        ],
128	        "embedding_minus_random_pp": 1.5,
129	        "dataflow_minus_random_pp": -0.2
130	      },
131	      "starcoder_test_easy": {
132	        "random_R1_mean": 0.812,
133	        "embedding_R1_mean": 0.822,
134	        "dataflow_R1_mean": 0.81
135	      },
136	      "repobench_R1_delta_pp_embedding_avg": 1.8,
137	      "bootstrap_CI_width_R1_pp_avg": 1.2
138	    },
139	    "tables": [
140	      {
141	        "name": "Table 5: RepoBench-R Results (test_hard, pool≈18)",
142	        "columns": [
143	          "Encoder",
144	          "Strategy",
145	          "R@1 (%)",
146	          "95% CI",
147	          "Δ vs Random (pp)"
148	        ],
149	        "rows": [
150	          [
151	            "Qwen",
152	            "random",
153	            62.1,
154	            "[61.4, 62.8]",
155	            "—"
156	          ],
157	          [
158	            "Qwen",
159	            "embedding",
160	            64.2,
161	            "[63.4, 65.0]",
162	            "+2.1"
163	          ],
164	          [
165	            "Qwen",
166	            "dataflow",
167	            63.3,
168	            "[62.4, 64.2]",
169	            "+1.2"
170	          ],
171	          [
172	            "StarCoder",
173	            "random",
174	            57.4,
175	            "[56.6, 58.2]",
176	            "—"
177	          ],
178	          [
179	            "StarCoder",
180	            "embedding",
181	            58.9,
182	            "[58.0, 59.8]",
183	            "+1.5"
184	          ],
185	          [
186	            "StarCoder",
187	            "dataflow",
188	            57.2,
189	            "[56.2, 58.2]",
190	            "−0.2"
191	          ]
192	        ]
193	      }
194	    ],
195	    "figures": [],
196	    "analysis": "Cross-benchmark 一致性是 best tier 的关键证据：embedding mining 在 SWE-smith 和 RepoBench-R 上均显著提升两个 encoder，dataflow 条件性获益仅限 Qwen。这排除了 \"结果仅限单一 benchmark\" 的 reviewer concern。Test_easy 上 delta 被压缩（pool=6 ceiling effect）是预期行为，反向验证了 pool size 对绝对效果幅度的调节作用。\n\n\nRepoBench-R 是 cross-file completion 任务，pool 更小（6-18），绝对 R@1 更高。 Embedding mining 在两个 encoder 上均显著提升 test_hard R@1（Qwen +2.1pp, StarCoder +1.5pp）， 因为 pool=18 仍有足够 distractors 使 mining 质量差异体现。Test_easy pool=6 接近 ceiling，delta 被压缩但方向一致。Dataflow 在 Qwen test_hard 上 +1.2pp 但 CI 刚好 排除零，StarCoder 上无效（-0.2pp，CI 含零）——与 SWE-smith 上的 encoder-strategy interaction 完全一致，说明 pattern 跨 benchmark 稳定。CI 宽度 ~1.2pp 在 bootstrap_CI_width_R1_pp [0.5, 2.0] 范围内，9 seeds 提供足够统计功效。\n"
197	  },
198	  {
199	    "name": "Stratified Analysis with Structural Coverage & Neg Difficulty Quartiles",
200	    "description": "5 层分层分析：repo size / pool size / query-positive similarity / structural data availability (34% vs 66%) / neg_difficulty quartile。使用 M2 best checkpoints 在 SWE-smith validation 上重新评估。\n",
201	    "results": {
202	      "stratum_structural_available": {
203	        "with_dataflow_34pct": {
204	          "qwen_dataflow_minus_random_pp": 2.8,
205	          "qwen_dataflow_minus_embedding_pp": 1.3,
206	          "starcoder_dataflow_minus_random_pp": 0.1,
207	          "n_instances": "~5200"
208	        },
209	        "fallback_66pct": {
210	          "qwen_dataflow_minus_random_pp": 0.1,
211	          "qwen_dataflow_minus_embedding_pp": -0.2,
212	          "starcoder_dataflow_minus_random_pp": -0.3,
213	          "n_instances": "~10000"
214	        }
215	      },
216	      "stratum_neg_difficulty_quartile": {
217	        "Q1_easiest": {
218	          "qwen_embedding_minus_random_pp": 0.8,
219	          "qwen_dataflow_minus_random_pp": 0.3
220	        },
221	        "Q2": {
222	          "qwen_embedding_minus_random_pp": 1.5,
223	          "qwen_dataflow_minus_random_pp": 0.7
224	        },
225	        "Q3": {
226	          "qwen_embedding_minus_random_pp": 2.4,
227	          "qwen_dataflow_minus_random_pp": 1.2
228	        },
229	        "Q4_hardest": {
230	          "qwen_embedding_minus_random_pp": 3.2,
231	          "qwen_dataflow_minus_random_pp": 2.1
232	        }
233	      },
234	      "stratum_repo_size": {
235	        "small_lt50": {
236	          "embedding_delta_pp": 2.8,
237	          "n": "~500"
238	        },
239	        "medium_50_200": {
240	          "embedding_delta_pp": 2.2,
241	          "n": "~4100"
242	        },
243	        "large_200_500": {
244	          "embedding_delta_pp": 1.8,
245	          "n": "~5500"
246	        },
247	        "xlarge_500plus": {
248	          "embedding_delta_pp": 1.6,
249	          "n": "~5100"
250	        }
251	      },
252	      "stratum_pool_size": {
253	        "pool_lt20": {
254	          "embedding_delta_pp": 1.0,
255	          "dataflow_delta_pp": 0.3
256	        },
257	        "pool_20_50": {
258	          "embedding_delta_pp": 2.1,
259	          "dataflow_delta_pp": 1.0
260	        },
261	        "pool_gt50": {
262	          "embedding_delta_pp": 2.5,
263	          "dataflow_delta_pp": 1.4
264	        }
265	      },
266	      "stratum_query_pos_sim": {
267	        "high_sim_gt095": {
268	          "embedding_delta_pp": 2.6,
269	          "dataflow_delta_pp": 1.8
270	        },
271	        "medium_sim_085_095": {
272	          "embedding_delta_pp": 1.9,
273	          "dataflow_delta_pp": 0.8
274	        },
275	        "low_sim_lt085": {
276	          "embedding_delta_pp": 1.2,
277	          "dataflow_delta_pp": 0.2
278	        }
279	      }
280	    },
281	    "tables": [
282	      {
283	        "name": "Table 7: Stratified R@1 Delta by Structural Data Availability (Qwen)",
284	        "columns": [
285	          "Stratum",
286	          "N",
287	          "random R@1",
288	          "embedding R@1",
289	          "dataflow R@1",
290	          "df−rand (pp)"
291	        ],
292	        "rows": [
293	          [
294	            "With dataflow (34%)",
295	            "~5.2K",
296	            53.1,
297	            55.4,
298	            55.9,
299	            "+2.8"
300	          ],
301	          [
302	            "Fallback (66%)",
303	            "~10K",
304	            55.2,
305	            57.3,
306	            55.3,
307	            "+0.1"
308	          ],
309	          [
310	            "Overall",
311	            "~15.2K",
312	            54.5,
313	            56.5,
314	            55.5,
315	            "+1.0"
316	          ]
317	        ]
318	      },
319	      {
320	        "name": "Table 7b: R@1 Delta by Neg Difficulty Quartile (Qwen)",
321	        "columns": [
322	          "Quartile",
323	          "margin_mean",
324	          "emb−rand (pp)",
325	          "df−rand (pp)"
326	        ],
327	        "rows": [
328	          [
329	            "Q1 (easiest)",
330	            0.142,
331	            "+0.8",
332	            "+0.3"
333	          ],
334	          [
335	            "Q2",
336	            0.078,
337	            "+1.5",
338	            "+0.7"
339	          ],
340	          [
341	            "Q3",
342	            0.031,
343	            "+2.4",
344	            "+1.2"
345	          ],
346	          [
347	            "Q4 (hardest)",
348	            0.008,
349	            "+3.2",
350	            "+2.1"
351	          ]
352	        ]
353	      }
354	    ],
355	    "figures": [],
356	    "analysis": "Stratified analysis 提供了论文中最强的 mechanistic 证据。Neg_difficulty Q4 的 +3.2pp embedding delta 是 overall +2.0pp 的 1.6 倍——越难的 instances 从 harder negatives 获益越多，这是 representation saturation 理论的直接预测。Structural-available vs fallback 分解消除了 \"diluted signal\" concern 并揭示 dataflow 的真实 per-instance 效果（+2.8pp）远大于 pooled 报告值。\n\n\nStructural-available stratum（34%）上 dataflow 优势放大到 +2.8pp（Qwen），因为这些 instance 实际接收了 dataflow-disconnected negatives——真实训练信号未被 fallback 稀释。 Fallback stratum（66%）上 dataflow ≈ embedding（±0.2pp），因为 fallback 时 dataflow 策略退化为 embedding 或 random 选择，无结构信号注入。这一分解直接回应 reviewer 关于 \"34% coverage 稀释 signal\" 的 concern——真实 per-instance 效果是 +2.8pp 而非 pooled +1.0pp。Neg_difficulty Q4（最难 quartile）上 delta 最大（embedding +3.2pp, dataflow +2.1pp），符合 representation saturation 理论——Qwen 在高 pos_sim 区域最需要 harder negatives，而 Q4 恰好是 margin 最小、分辨最难的 instances。Q1（最容易）delta 最小 因为 random negatives 已经足够容易区分。Repo size 上 small repo delta 更大因为 小 repo 的 candidate pool 更集中，mining 策略差异更容易体现。\n"
357	  },
358	  {
359	    "name": "Call-Graph Hop Depth Ablation (1/2/3-hop)",
360	    "description": "比较 1-hop / 2-hop / 3-hop call-graph bounding 对 dataflow negative 质量的影响。 Qwen encoder, 1 seed, SWE-smith validation。\n",
361	    "results": {
362	      "hop_1": {
363	        "R1": 0.548,
364	        "connected_coverage_pct": 12.4,
365	        "negatives_per_query_mean": 18.2
366	      },
367	      "hop_2": {
368	        "R1": 0.555,
369	        "connected_coverage_pct": 34.3,
370	        "negatives_per_query_mean": 31.7
371	      },
372	      "hop_3": {
373	        "R1": 0.551,
374	        "connected_coverage_pct": 58.6,
375	        "negatives_per_query_mean": 42.1
376	      },
377	      "optimal_hop": 2,
378	      "hop2_minus_hop1_pp": 0.7,
379	      "hop3_minus_hop2_pp": -0.4
380	    },
381	    "tables": [
382	      {
383	        "name": "Table 9: Hop Depth Ablation (Qwen, dataflow strategy)",
384	        "columns": [
385	          "Hops",
386	          "Coverage (%)",
387	          "Neg/query",
388	          "R@1 (%)",
389	          "Δ vs 2-hop (pp)"
390	        ],
391	        "rows": [
392	          [
393	            1,
394	            12.4,
395	            18.2,
396	            54.8,
397	            "−0.7"
398	          ],
399	          [
400	            2,
401	            34.3,
402	            31.7,
403	            55.5,
404	            "—"
405	          ],
406	          [
407	            3,
408	            58.6,
409	            42.1,
410	            55.1,
411	            "−0.4"
412	          ]
413	        ]
414	      }
415	    ],
416	    "figures": [],
417	    "analysis": "2-hop optimal 符合 inter-procedural dataflow 的语义：1-hop = 直接 caller/callee， 2-hop = caller 的 caller 或 callee 的 callee（一层间接调用），3-hop 开始包含 过于间接的关系。论文可以强调 2-hop 选择有 principled 依据而非纯粹 empirical tuning。\n\n\n2-hop 是最优平衡点。1-hop 太保守——仅 12.4% coverage 意味着大部分 instance 没有足够的 connected 节点来定义 \"disconnected\" negatives，退化为 random。3-hop 过于宽松——58.6% coverage 下 \"disconnected\" 的定义变得太窄，许多语义相关但间接连接的文件被错误排除在 negative pool 外，引入噪声。2-hop 的 34.3% coverage（与 M1 extraction 的 structural data rate 一致）在 \"enough connected nodes to define meaningful disconnection\" 和 \"disconnected set still contains genuinely unrelated files\" 之间取得平衡。\n"
418	  },
419	  {
420	    "name": "Training Data Size Scaling (1K/3K/5K)",
421	    "description": "固定 Qwen encoder + embedding strategy，训练数据从 1K / 3K / 5K instances 增长， 观察 R@1 变化和策略排名稳定性。\n",
422	    "results": {
423	      "size_1K": {
424	        "random_R1": 0.51,
425	        "embedding_R1": 0.522,
426	        "dataflow_R1": 0.515,
427	        "embedding_minus_random_pp": 1.2,
428	        "seed_std": 0.015
429	      },
430	      "size_3K": {
431	        "random_R1": 0.532,
432	        "embedding_R1": 0.55,
433	        "dataflow_R1": 0.541,
434	        "embedding_minus_random_pp": 1.8,
435	        "seed_std": 0.01
436	      },
437	      "size_5K": {
438	        "random_R1": 0.545,
439	        "embedding_R1": 0.565,
440	        "dataflow_R1": 0.555,
441	        "embedding_minus_random_pp": 2.0,
442	        "seed_std": 0.008
443	      },
444	      "ranking_stable": true,
445	      "monotonic_improvement": true
446	    },
447	    "tables": [
448	      {
449	        "name": "Table 10: Data Size Scaling (Qwen)",
450	        "columns": [
451	          "Size",
452	          "random R@1",
453	          "embedding R@1",
454	          "dataflow R@1",
455	          "emb−rand (pp)",
456	          "σ across seeds"
457	        ],
458	        "rows": [
459	          [
460	            "1K",
461	            51.0,
462	            52.2,
463	            51.5,
464	            "+1.2",
465	            1.5
466	          ],
467	          [
468	            "3K",
469	            53.2,
470	            55.0,
471	            54.1,
472	            "+1.8",
473	            1.0
474	          ],
475	          [
476	            "5K",
477	            54.5,
478	            56.5,
479	            55.5,
480	            "+2.0",
481	            0.8
482	          ]
483	        ]
484	      }
485	    ],
486	    "figures": [],
487	    "analysis": "Monotonic scaling + stable ranking 表明结果不是 small-data artifact。5K 时未见 diminishing returns，暗示更大数据集可能进一步放大差异。这对 reviewer \"effect size marginal\" concern 有价值——delta 仍在增长，当前 +2.0pp 是下界而非上界。\n\n\n策略排名在 1K/3K/5K 三个尺度上保持一致（embedding > dataflow > random），但 delta 幅度随数据量增大而增大——1K 时 +1.2pp，5K 时 +2.0pp。这是因为更大的训练集提供更多 diverse negatives，使 mining 策略的差异更充分地体现。1K 时 seed 方差较大（std=0.015） 因为 negative 多样性不足，个别 seed 的 negative 采样偶然性影响结果。5K 时方差收敛 （std=0.008），mining 策略的信号超过采样噪声。No diminishing returns at 5K suggests further scaling could help, but is beyond scope。\n"
488	  },
489	  {
490	    "name": "Fusion Head Ablation",
491	    "description": "比较 embedding-only / structural-features-only / combined fusion head， 隔离 training-time mining 价值与 inference-time feature injection。\n",
492	    "results": {
493	      "embedding_only": {
494	        "qwen_R1": 0.565,
495	        "starcoder_R1": 0.475
496	      },
497	      "structural_features_only": {
498	        "qwen_R1": 0.498,
499	        "starcoder_R1": 0.421
500	      },
501	      "combined_fusion": {
502	        "qwen_R1": 0.561,
503	        "starcoder_R1": 0.472
504	      },
505	      "embedding_only_minus_combined_pp": 0.4,
506	      "conclusion": "mining > fusion; structural features at inference add noise"
507	    },
508	    "tables": [
509	      {
510	        "name": "Table 11: Fusion Head Ablation",
511	        "columns": [
512	          "Configuration",
513	          "Qwen R@1 (%)",
514	          "StarCoder R@1 (%)"
515	        ],
516	        "rows": [
517	          [
518	            "embedding-only (ours)",
519	            56.5,
520	            47.5
521	          ],
522	          [
523	            "structural-features-only",
524	            49.8,
525	            42.1
526	          ],
527	          [
528	            "combined fusion",
529	            56.1,
530	            47.2
531	          ]
532	        ]
533	      }
534	    ],
535	    "figures": [],
536	    "analysis": "训练时注入 structural signal 通过 negative mining（间接信号）比 inference 时直接注入 structural features（直接信号）更有效。可能原因：mining 让 encoder 自己学习结构相关的 representation，而直接注入 features 绕过了 encoder 的学习过程，且 CodeQL 34% coverage 意味着 66% instance 在 inference 时收到 zero-vector structural features，引入 noise。\n\n\nEmbedding-only（仅用 embedding mining 训练的 retriever，inference 时不注入结构特征） 表现最好或 tied with combined。Combined fusion 略低 0.4pp 因为 inference-time structural features 引入了不精确的 CodeQL connectivity 信号——recall 某些 CodeQL extraction 失败的 instance 反而被错误降权。Structural-features-only（不用 mining 训练， 仅在 inference 注入结构特征）远低于 embedding-only（-6.7pp Qwen），证明核心价值在 training-time negative mining 而非 inference-time feature engineering。 这一结果对 paper framing 极为重要：StructFuse 的贡献是 mining strategy，不是 fusion。\n"
537	  },
538	  {
539	    "name": "Dataflow-Distance Weighted vs Binary Negatives",
540	    "description": "比较 binary connected/disconnected 与 dataflow-distance weighted negative sampling。 Weighted: disconnected 且 hop-distance 更远的文件被赋予更高采样概率。\n",
541	    "results": {
542	      "binary_qwen_R1": 0.555,
543	      "weighted_qwen_R1": 0.558,
544	      "binary_starcoder_R1": 0.458,
545	      "weighted_starcoder_R1": 0.459,
546	      "weighted_minus_binary_qwen_pp": 0.3,
547	      "weighted_minus_binary_starcoder_pp": 0.1
548	    },
549	    "tables": [
550	      {
551	        "name": "Table S1: Weighted vs Binary Dataflow Negatives",
552	        "columns": [
553	          "Method",
554	          "Qwen R@1 (%)",
555	          "StarCoder R@1 (%)",
556	          "Δ vs Binary (pp)"
557	        ],
558	        "rows": [
559	          [
560	            "Binary (default)",
561	            55.5,
562	            45.8,
563	            "—"
564	          ],
565	          [
566	            "Distance-weighted",
567	            55.8,
568	            45.9,
569	            "+0.3 / +0.1"
570	          ]
571	        ]
572	      }
573	    ],
574	    "figures": [],
575	    "analysis": "Binary is sufficient — complexity of weighted sampling not justified. 论文可在 ablation section 用一句话报告这一 negative result， 强化 \"simple binary structural signal is the key insight\" 的 narrative。\n\n\nWeighted 在 Qwen 上仅微弱提升 +0.3pp（不显著），StarCoder 上几乎无差异。 原因：binary disconnected/connected 已经捕获了最关键的 structural distinction—— \"是否在调用链上\"。进一步按 hop distance 加权引入的额外信号被 noise 抵消：距离更远 不一定意味着更好的 negative（一个完全无关的 utility 文件可能 hop=∞ 但也是 trivial negative）。 Binary 的简洁性是优势——fewer hyperparameters, same effect。\n"
576	  },
577	  {
578	    "name": "SWE-bench Failure Analysis (50 cases)",
579	    "description": "从 random retriever 的 SWE-bench 失败案例中抽样 50 个，人工分类失败原因， 标注 dataflow 信号是否可能帮助。\n",
580	    "results": {
581	      "total_analyzed": 50,
582	      "category_breakdown": {
583	        "retrieval_failure_wrong_files": 22,
584	        "retrieval_success_but_agent_fail": 15,
585	        "insufficient_context_window": 7,
586	        "test_environment_issue": 4,
587	        "ambiguous_issue_description": 2
588	      },
589	      "dataflow_could_help": {
590	        "true": 14,
591	        "partially": 5,
592	        "false": 31
593	      },
594	      "dataflow_help_rate": 0.28,
595	      "key_pattern": "14/22 retrieval failures involve cross-module dependencies where the gold file is a caller/callee of a retrieved-but-wrong file — dataflow connectivity would directly address these.\n"
596	    },
597	    "tables": [
598	      {
599	        "name": "Table S2: Failure Category Breakdown",
600	        "columns": [
601	          "Category",
602	          "Count",
603	          "% of 50",
604	          "Dataflow Could Help?"
605	        ],
606	        "rows": [
607	          [
608	            "Retrieval: wrong files",
609	            22,
610	            44,
611	            "14/22 (64%)"
612	          ],
613	          [
614	            "Retrieval OK, agent fail",
615	            15,
616	            30,
617	            "N/A"
618	          ],
619	          [
620	            "Context window limit",
621	            7,
622	            14,
623	            "5/7 partially"
624	          ],
625	          [
626	            "Test env issue",
627	            4,
628	            8,
629	            "No"
630	          ],
631	          [
632	            "Ambiguous issue",
633	            2,
634	            4,
635	            "No"
636	          ]
637	        ]
638	      }
639	    ],
640	    "figures": [],
641	    "analysis": "28% of failures could benefit from dataflow signal, consistent with the observed +3.2pp resolve rate improvement. The 64% rate within retrieval failures confirms that cross-module dependency is the primary retrieval challenge, directly supporting Claim 2's motivation.\n\n\n50 个失败中 22 个是 retrieval failure（检索到错误文件），其中 14 个涉及跨模块依赖—— 被检索的文件和 gold 文件有高文本相似度但分属不同 call chain。Dataflow negatives 训练 恰好针对这类 confound。15 个 retrieval success but agent fail 说明 retrieval 不是 唯一瓶颈——agent 的 patch 生成能力也是限制因素。这为论文提供了 \"ceiling analysis\"： 即使 perfect retrieval，resolve rate 上限约 85%（15% 是 agent 能力限制）。\n"
642	  },
643	  {
644	    "name": "Qualitative Examples (5-10 cases)",
645	    "description": "从 SWE-bench 和 SWE-smith 中选取 5-10 个 dataflow negatives 改变检索结果的典型案例， 展示 structural signal 的具体作用机制。\n",
646	    "results": {
647	      "total_examples": 8,
648	      "example_categories": {
649	        "caller_callee_confusion": 3,
650	        "utility_file_distraction": 2,
651	        "cross_module_import_chain": 2,
652	        "test_file_vs_source": 1
653	      },
654	      "illustrative_example": {
655	        "issue": "django/django#12345 — QuerySet.filter() returns wrong results with nested Q objects",
656	        "random_retriever_top1": "django/db/models/query.py (text match on 'filter')",
657	        "dataflow_retriever_top1": "django/db/models/sql/query.py (actual SQL generation called by filter)",
658	        "gold": "django/db/models/sql/query.py",
659	        "explanation": "Random retriever picks query.py (contains 'filter' method signature) but the bug is in sql/query.py (the downstream SQL builder called by filter). Dataflow training teaches the model that sql/query.py is structurally connected to query.py via 2-hop call chain, making it a better negative for other instances, which in turn improves the model's ability to rank the actual implementation file higher.\n"
660	      }
661	    },
662	    "tables": [],
663	    "figures": [],
664	    "analysis": "Qualitative examples serve as the paper's \"aha moment\" — they make the abstract representation geometry argument concrete. Reviewer-facing value: even skeptics who question statistical significance can see the mechanism operating on real code.\n\n\n8 个案例覆盖 4 个失败模式：caller-callee confusion（3 个，最常见——文本相似的 wrapper 函数 vs 实际实现）、utility file distraction（2 个——高文本重叠的 helper 文件干扰）、 cross-module import chain（2 个——A 导入 B 导入 C，bug 在 C 但文本匹配 A）、test vs source（1 个——test file 包含几乎完整的 source code 复制）。这些案例具体展示了 \"lexical similarity ≠ structural relevance\" 的核心 insight。\n"
665	  },
666	  {
667	    "name": "Temperature Ablation τ ∈ {0.05, 0.1, 0.2}",
668	    "description": "3 temperatures × 3 strategies × 2 encoders, 1 seed each. 测试 strategy ranking 是否 regime-specific。\n",
669	    "results": {
670	      "tau_005": {
671	        "qwen_random_R1": 0.558,
672	        "qwen_embedding_R1": 0.577,
673	        "qwen_dataflow_R1": 0.569,
674	        "qwen_embedding_minus_random_pp": 1.9,
675	        "starcoder_random_R1": 0.47,
676	        "starcoder_embedding_R1": 0.485,
677	        "starcoder_dataflow_R1": 0.467,
678	        "starcoder_embedding_minus_random_pp": 1.5
679	      },
680	      "tau_010": {
681	        "qwen_random_R1": 0.545,
682	        "qwen_embedding_R1": 0.565,
683	        "qwen_dataflow_R1": 0.555,
684	        "qwen_embedding_minus_random_pp": 2.0,
685	        "starcoder_random_R1": 0.46,
686	        "starcoder_embedding_R1": 0.475,
687	        "starcoder_dataflow_R1": 0.458,
688	        "starcoder_embedding_minus_random_pp": 1.5
689	      },
690	      "tau_020": {
691	        "qwen_random_R1": 0.53,
692	        "qwen_embedding_R1": 0.546,
693	        "qwen_dataflow_R1": 0.538,
694	        "qwen_embedding_minus_random_pp": 1.6,
695	        "starcoder_random_R1": 0.448,
696	        "starcoder_embedding_R1": 0.461,
697	        "starcoder_dataflow_R1": 0.447,
698	        "starcoder_embedding_minus_random_pp": 1.3
699	      },
700	      "ranking_preserved_across_tau": true,
701	      "optimal_tau": 0.05
702	    },
703	    "tables": [
704	      {
705	        "name": "Table 8: Temperature Ablation (R@1 %)",
706	        "columns": [
707	          "τ",
708	          "Encoder",
709	          "random",
710	          "embedding",
711	          "dataflow",
712	          "emb−rand (pp)"
713	        ],
714	        "rows": [
715	          [
716	            0.05,
717	            "Qwen",
718	            55.8,
719	            57.7,
720	            56.9,
721	            "+1.9"
722	          ],
723	          [
724	            0.05,
725	            "StarCoder",
726	            47.0,
727	            48.5,
728	            46.7,
729	            "+1.5"
730	          ],
731	          [
732	            0.1,
733	            "Qwen",
734	            54.5,
735	            56.5,
736	            55.5,
737	            "+2.0"
738	          ],
739	          [
740	            0.1,
741	            "StarCoder",
742	            46.0,
743	            47.5,
744	            45.8,
745	            "+1.5"
746	          ],
747	          [
748	            0.2,
749	            "Qwen",
750	            53.0,
751	            54.6,
752	            53.8,
753	            "+1.6"
754	          ],
755	          [
756	            0.2,
757	            "StarCoder",
758	            44.8,
759	            46.1,
760	            44.7,
761	            "+1.3"
762	          ]
763	        ]
764	      }
765	    ],
766	    "figures": [],
767	    "analysis": "Ranking stability across τ 是重要的 robustness evidence。τ=0.2 下 delta 缩小但 不翻转，说明 mining quality 的价值在不同 loss sharpness 下都存在。Paper 可以报告 τ=0.05 作为 alternative best configuration 但选择 τ=0.1 作为 default（更常见的 literature default）。\n\n\nStrategy ranking（embedding > dataflow > random for Qwen; embedding > random ≈ dataflow for StarCoder）在三个 temperature 下保持一致。τ=0.05 绝对性能最高因为 sharper temperature 使 contrastive loss 更有效地区分相似度差异（harder gradient signal）。 τ=0.2 下所有策略性能下降且 delta 缩小（1.6pp vs 2.0pp），因为 softer temperature 减弱了 negative 选择质量的影响——当所有 similarity 被压缩到窄范围内，hard vs easy negatives 的梯度差异变小。关键结论：findings 不是 temperature-regime-specific， 直接回应 median reviewer 的 \"τ=0.05 unusually low\" concern。\n"
768	  },
769	  {
770	    "name": "Dynamic vs Static Embedding Mining",
771	    "description": "Dynamic: 每 epoch 重新用当前 encoder 挖 embedding negatives。 Static: 仅用 pretrained encoder 挖一次（当前做法）。 Qwen + StarCoder, 1 seed each。\n",
772	    "results": {
773	      "qwen_static_R1": 0.565,
774	      "qwen_dynamic_R1": 0.568,
775	      "qwen_dynamic_minus_static_pp": 0.3,
776	      "starcoder_static_R1": 0.475,
777	      "starcoder_dynamic_R1": 0.477,
778	      "starcoder_dynamic_minus_static_pp": 0.2,
779	      "dynamic_significant": false,
780	      "curriculum_confound_ruled_out": true
781	    },
782	    "tables": [
783	      {
784	        "name": "Table 13: Static vs Dynamic Embedding Mining",
785	        "columns": [
786	          "Encoder",
787	          "Static R@1 (%)",
788	          "Dynamic R@1 (%)",
789	          "Δ (pp)",
790	          "p-value"
791	        ],
792	        "rows": [
793	          [
794	            "Qwen",
795	            56.5,
796	            56.8,
797	            "+0.3",
798	            0.41
799	          ],
800	          [
801	            "StarCoder",
802	            47.5,
803	            47.7,
804	            "+0.2",
805	            0.53
806	          ]
807	        ]
808	      }
809	    ],
810	    "figures": [],
811	    "analysis": "Static ≈ dynamic 是 clean negative result，强化了论文 narrative：关键是 negative 的 semantic quality（embedding vs random vs dataflow），不是 freshness。 也简化了 practitioner recommendation——mine once from pretrained, no need for per-epoch re-mining。\n\n\nDynamic mining 仅微弱提升 +0.2-0.3pp（不显著），因为 LoRA rank 16 的 fine-tuning 只轻微改变 embedding space——pretrained encoder 的 nearest neighbors 在训练后 仍然大部分相同。这排除了 \"static mining 的优势来自 curriculum effect（early epochs 看到 harder negatives 然后 negatives 变 stale）\" 的 confound——即使更新 negatives， 效果几乎不变。对 Claim 2 很重要：说明 mining strategy 的选择（what to mine）比 mining schedule（when to mine）更关键。Dynamic mining 的 compute overhead（每 epoch 重新 encode + kNN）不 justified。\n"
812	  },
813	  {
814	    "name": "Bootstrap CIs for SWE-bench Lite Resolve Rate",
815	    "description": "对 plan_003 的 SWE-bench 结果计算 10K bootstrap resamples 的 95% CI， 报告 paired difference CIs 和 p-values。\n",
816	    "results": {
817	      "embedding_minus_random": {
818	        "delta_pp": 2.5,
819	        "ci_95": [
820	          0.7,
821	          4.3
822	        ],
823	        "p_value": 0.018,
824	        "significant": true
825	      },
826	      "dataflow_minus_random": {
827	        "delta_pp": 3.2,
828	        "ci_95": [
829	          1.0,
830	          5.5
831	        ],
832	        "p_value": 0.008,
833	        "significant": true
834	      },
835	      "dataflow_minus_embedding": {
836	        "delta_pp": 0.7,
837	        "ci_95": [
838	          -1.5,
839	          2.9
840	        ],
841	        "p_value": 0.134,
842	        "significant": false
843	      },
844	      "bootstrap_n": 10000,
845	      "sample_size": 300
846	    },
847	    "tables": [
848	      {
849	        "name": "Table 4c: SWE-bench Bootstrap Significance Tests",
850	        "columns": [
851	          "Comparison",
852	          "Δ (pp)",
853	          "95% CI",
854	          "p-value"
855	        ],
856	        "rows": [
857	          [
858	            "embedding − random",
859	            "+2.5",
860	            "[+0.7, +4.3]",
861	            0.018
862	          ],
863	          [
864	            "dataflow − random",
865	            "+3.2",
866	            "[+1.0, +5.5]",
867	            0.008
868	          ],
869	          [
870	            "dataflow − embedding",
871	            "+0.7",
872	            "[−1.5, +2.9]",
873	            0.134
874	          ]
875	        ]
876	      }
877	    ],
878	    "figures": [],
879	    "analysis": "CI 下界 > 0 for both mining strategies vs random 是 EMNLP reviewer 需要的统计保证。 Dataflow vs embedding 不显著是 honest reporting 且与 Claim 2 的 \"conditional\" framing 一致——dataflow 的额外价值不是 universally separable at SWE-bench scale。\n\n\nEmbedding vs random CI [0.7, 4.3] 排除零（p=0.018），确认 embedding mining 在下游 任务上的统计显著提升。Dataflow vs random 更显著（p=0.008）因为 delta 更大且 SWE-bench 中 cross-module patches 对 dataflow signal 响应一致。Dataflow vs embedding 不显著 （p=0.134, CI 含零）——300 instances 的 power 不足以区分 +0.7pp 的小 delta，这是 expected：retrieval level 的 ~1pp 差异在下游 binary resolve 结果上被放大和噪声化。 CI 宽度 ~3.6pp 反映 300 样本的 inherent variance——SWE-bench Lite 不是为精确 delta 估计设计的 benchmark。\n"
880	  },
881	  {
882	    "name": "Inference-Time Graph Method Literature Comparison",
883	    "description": "文献分析（非实验）：与 CodexGraph, LocAgent, RANGER 等 inference-time 图方法的 系统比较。已完成 8 篇论文 survey。\n",
884	    "results": {
885	      "papers_surveyed": 8,
886	      "key_distinction": "training-time mining (ours) vs inference-time graph navigation",
887	      "complementarity_evidence": "All 8 methods operate at inference time; StructFuse mines at training time. The two approaches are complementary — StructFuse improves the base retriever that graph methods navigate over.\n",
888	      "papers_list": [
889	        "CodexGraph",
890	        "LocAgent",
891	        "RANGER",
892	        "GraphCoder",
893	        "ARISE",
894	        "RepoGraph",
895	        "CodeGRAG",
896	        "CodeRAG"
897	      ]
898	    },
899	    "tables": [
900	      {
901	        "name": "Table S3: Comparison with Inference-Time Graph Methods",
902	        "columns": [
903	          "Method",
904	          "Graph Stage",
905	          "Graph Type",
906	          "Complementary?"
907	        ],
908	        "rows": [
909	          [
910	            "StructFuse (ours)",
911	            "Training",
912	            "Dataflow (CodeQL)",
913	            "—"
914	          ],
915	          [
916	            "CodexGraph",
917	            "Inference",
918	            "Code graph DB",
919	            "Yes"
920	          ],
921	          [
922	            "LocAgent",
923	            "Inference",
924	            "Repo structure",
925	            "Yes"
926	          ],
927	          [
928	            "RANGER",
929	            "Inference",
930	            "Call graph",
931	            "Yes"
932	          ],
933	          [
934	            "ARISE",
935	            "Inference",
936	            "Intra-proc dataflow",
937	            "Partially (intra only)"
938	          ]
939	        ]
940	      }
941	    ],
942	    "figures": [],
943	    "analysis": "Discussion 中用 2 段落即可。不要 overclaim StructFuse 优于这些方法——它们解决不同问题。 Highlight: StructFuse 是唯一在 training time 利用结构信号的方法，且不增加 inference cost。\n\n\n8 篇 inference-time graph 方法均在推理阶段构建/遍历代码图，而 StructFuse 在训练阶段 通过 negative mining 将结构信号蒸馏进 encoder。两者正交：StructFuse 产出更好的 base retriever，inference-time 方法在此基础上进一步 re-rank/navigate。无直接可比性因为 实验设置完全不同（LocAgent 用 LLM agent + tool calls，我们用 embedding retrieval）。 Discussion section 应明确 \"complementary, not competing\" 的定位。\n"
944	  },
945	  {
946	    "name": "BM25 Negative Baseline — Closing CoCoHaNeRe Argument",
947	    "description": "BM25-based hard negatives 作为第 4 策略，1+ seed × 2 encoders。 验证 CoCoHaNeRe 报告的 \"embedding negatives harm\" 实际是 BM25-proxy artifact。\n",
948	    "results": {
949	      "qwen": {
950	        "bm25_R1": 0.52,
951	        "random_R1": 0.545,
952	        "embedding_R1": 0.565,
953	        "dataflow_R1": 0.555,
954	        "bm25_minus_random_pp": -2.5,
955	        "embedding_minus_bm25_pp": 4.5
956	      },
957	      "starcoder": {
958	        "bm25_R1": 0.433,
959	        "random_R1": 0.46,
960	        "embedding_R1": 0.475,
961	        "dataflow_R1": 0.458,
962	        "bm25_minus_random_pp": -2.7,
963	        "embedding_minus_bm25_pp": 4.2
964	      },
965	      "bm25_harms_both_encoders": true,
966	      "cocohanere_artifact_confirmed": true,
967	      "bm25_minus_random_avg_pp": -2.6
968	    },
969	    "tables": [
970	      {
971	        "name": "Table 3: Full 4-Strategy Comparison Including BM25 Baseline",
972	        "columns": [
973	          "Encoder",
974	          "Strategy",
975	          "R@1 (%)",
976	          "95% CI",
977	          "Δ vs Random (pp)"
978	        ],
979	        "rows": [
980	          [
981	            "Qwen",
982	            "BM25",
983	            52.0,
984	            "[51.2, 52.8]",
985	            "−2.5"
986	          ],
987	          [
988	            "Qwen",
989	            "random",
990	            54.5,
991	            "[53.8, 55.2]",
992	            "—"
993	          ],
994	          [
995	            "Qwen",
996	            "dataflow",
997	            55.5,
998	            "[54.6, 56.4]",
999	            "+1.0"
1000	          ],
1001	          [
1002	            "Qwen",
1003	            "embedding",
1004	            56.5,
1005	            "[55.8, 57.2]",
1006	            "+2.0"
1007	          ],
1008	          [
1009	            "StarCoder",
1010	            "BM25",
1011	            43.3,
1012	            "[42.3, 44.3]",
1013	            "−2.7"
1014	          ],
1015	          [
1016	            "StarCoder",
1017	            "random",
1018	            46.0,
1019	            "[45.1, 46.9]",
1020	            "—"
1021	          ],
1022	          [
1023	            "StarCoder",
1024	            "dataflow",
1025	            45.8,
1026	            "[44.8, 46.8]",
1027	            "−0.2"
1028	          ],
1029	          [
1030	            "StarCoder",
1031	            "embedding",
1032	            47.5,
1033	            "[46.6, 48.4]",
1034	            "+1.5"
1035	          ]
1036	        ]
1037	      }
1038	    ],
1039	    "figures": [],
1040	    "analysis": "BM25 baseline 是 best tier 论文的 crown jewel experiment。它将 Claim 1 从 \"argumentative correction\" 升级为 \"empirical demonstration\"：我们不仅指出 CoCoHaNeRe 用了 BM25 proxy， 还实际运行 BM25 negatives 复现了 harm effect，然后展示 true embedding negatives 方向相反。 4-strategy ordering BM25 < random < dataflow ≤ embedding 清晰展示了 negative mining strategy 的 quality spectrum。Reviewer 对 \"correction without evidence\" 的 concern 被彻底关闭。\n\n\nBM25 negatives 在两个 encoder 上均 harm performance（Qwen -2.5pp, StarCoder -2.7pp vs random），直接复现了 CoCoHaNeRe 报告的负面效果方向。关键 insight：BM25 negatives 选取的是 lexically similar 但 semantically ambiguous 的文件——它们与 query 共享大量 token overlap（function names, variable names, import patterns），但这种 overlap 恰恰是 contrastive learning 需要利用来区分 positive/negative 的信号。用 BM25 选的 negatives 让模型学会 ignore lexical cues，但这些 cues 在 code retrieval 中是有效信号。 相比之下，true embedding distance negatives 选取的是 semantically similar（在 pretrained embedding space 中近）但与 query 不同的文件，这迫使模型学习更 fine-grained semantic distinctions。BM25 vs embedding 的 4.5pp 差距（Qwen）是论文中最大的 single pairwise comparison，构成 Claim 1 correction argument 的 empirical closure。 效果幅度在 bm25_minus_random_R1_pp [-4.0, -1.5] 范围内。\n"
1041	  },
1042	  {
1043	    "name": "Pool Size Sensitivity (50/100/200/500)",
1044	    "description": "在 SWE-smith validation 上用 pool={50, 100, 200, 500} 重新评估 M2 best checkpoints， 测试 strategy ranking 在更 realistic pool sizes 下的稳定性。\n",
1045	    "results": {
1046	      "qwen": {
1047	        "pool_50": {
1048	          "random_R1": 0.545,
1049	          "embedding_R1": 0.565,
1050	          "dataflow_R1": 0.555,
1051	          "embedding_minus_random_pp": 2.0
1052	        },
1053	        "pool_100": {
1054	          "random_R1": 0.428,
1055	          "embedding_R1": 0.447,
1056	          "dataflow_R1": 0.438,
1057	          "embedding_minus_random_pp": 1.9
1058	        },
1059	        "pool_200": {
1060	          "random_R1": 0.342,
1061	          "embedding_R1": 0.359,
1062	          "dataflow_R1": 0.351,
1063	          "embedding_minus_random_pp": 1.7
1064	        },
1065	        "pool_500": {
1066	          "random_R1": 0.261,
1067	          "embedding_R1": 0.276,
1068	          "dataflow_R1": 0.269,
1069	          "embedding_minus_random_pp": 1.5
1070	        }
1071	      },
1072	      "starcoder": {
1073	        "pool_50": {
1074	          "random_R1": 0.46,
1075	          "embedding_R1": 0.475,
1076	          "dataflow_R1": 0.458,
1077	          "embedding_minus_random_pp": 1.5
1078	        },
1079	        "pool_100": {
1080	          "random_R1": 0.358,
1081	          "embedding_R1": 0.372,
1082	          "dataflow_R1": 0.357,
1083	          "embedding_minus_random_pp": 1.4
1084	        },
1085	        "pool_200": {
1086	          "random_R1": 0.282,
1087	          "embedding_R1": 0.295,
1088	          "dataflow_R1": 0.281,
1089	          "embedding_minus_random_pp": 1.3
1090	        },
1091	        "pool_500": {
1092	          "random_R1": 0.214,
1093	          "embedding_R1": 0.225,
1094	          "dataflow_R1": 0.213,
1095	          "embedding_minus_random_pp": 1.1
1096	        }
1097	      },
1098	      "ranking_stable_across_pools": true,
1099	      "pool_ranking_stable_pct": 100,
1100	      "delta_shrinkage_rate": "~0.15pp per doubling of pool size"
1101	    },
1102	    "tables": [
1103	      {
1104	        "name": "Table 12: Pool Size Sensitivity (R@1 %)",
1105	        "columns": [
1106	          "Pool",
1107	          "Encoder",
1108	          "random",
1109	          "embedding",
1110	          "dataflow",
1111	          "emb−rand (pp)",
1112	          "Ranking"
1113	        ],
1114	        "rows": [
1115	          [
1116	            50,
1117	            "Qwen",
1118	            54.5,
1119	            56.5,
1120	            55.5,
1121	            "+2.0",
1122	            "E>D>R"
1123	          ],
1124	          [
1125	            100,
1126	            "Qwen",
1127	            42.8,
1128	            44.7,
1129	            43.8,
1130	            "+1.9",
1131	            "E>D>R"
1132	          ],
1133	          [
1134	            200,
1135	            "Qwen",
1136	            34.2,
1137	            35.9,
1138	            35.1,
1139	            "+1.7",
1140	            "E>D>R"
1141	          ],
1142	          [
1143	            500,
1144	            "Qwen",
1145	            26.1,
1146	            27.6,
1147	            26.9,
1148	            "+1.5",
1149	            "E>D>R"
1150	          ],
1151	          [
1152	            50,
1153	            "StarCoder",
1154	            46.0,
1155	            47.5,
1156	            45.8,
1157	            "+1.5",
1158	            "E>R>D"
1159	          ],
1160	          [
1161	            100,
1162	            "StarCoder",
1163	            35.8,
1164	            37.2,
1165	            35.7,
1166	            "+1.4",
1167	            "E>R>D"
1168	          ],
1169	          [
1170	            200,
1171	            "StarCoder",
1172	            28.2,
1173	            29.5,
1174	            28.1,
1175	            "+1.3",
1176	            "E>R≈D"
1177	          ],
1178	          [
1179	            500,
1180	            "StarCoder",
1181	            21.4,
1182	            22.5,
1183	            21.3,
1184	            "+1.1",
1185	            "E>R≈D"
1186	          ]
1187	        ]
1188	      }
1189	    ],
1190	    "figures": [],
1191	    "analysis": "Pool size sensitivity 是外部有效性的关键证据。100% ranking stability 在 50→500 全程保持是 best tier 的标志。Delta 的 graceful degradation（非 collapse）说明 mining strategy 的价值是 robust 的。论文可以明确声明：\"Strategy rankings are stable across pool sizes spanning an order of magnitude (50–500), with embedding mining maintaining a statistically significant advantage even at the largest pool tested.\"\n\nStrategy ranking（embedding > dataflow > random for Qwen; embedding > random ≈ dataflow for StarCoder）在 pool 50→500 全程保持稳定（pool_ranking_stable_pct = 100%）。 绝对 R@1 随 pool 增大而下降（50→500 约 halved），因为 larger pool = more distractors = harder task。Embedding-random delta 从 2.0pp (pool=50) 缓慢缩小至 1.5pp (pool=500)， 缩小幅度约 25%，但方向和显著性保持。原因：pool=500 时 random negatives 中偶然出现 \"hard\" negative 的概率增加（base rate effect），部分缩小了 mining 策略的差异。 但核心 signal 不消失——embedding mining 在 pool=500 仍有 +1.5pp Qwen, +1.1pp StarCoder。 Dataflow 在 Qwen 上从 +1.0pp (pool=50) 降至 +0.8pp (pool=500) 但保持正值。 这直接回应 reviewer \"pool=50 unrealistically small\" concern：即使 10x pool 扩大， strategy ranking 完全不翻转。\n"
1192	  }
1193	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64e68f0d-17f7-400c-bef0-85f46478cc5a",
  "isSidechain": false,
  "promptId": "7dbbfae7-135c-4257-9519-f147e9c1c35b",
  "type": "user",
  "uuid": "23fbf0d4-8959-4f35-8c66-9c8b8eb8d06b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"SWE-bench Lite End-to-End Evaluation\",\n    \"description\": \"3 strategies × best Qwen checkpoint, Qwen3.6-27B agent, 300 SWE-bench Lite instances. Retriever 提供 top-k context files，agent 生成 patch，评估 resolve rate。\\n\",\n    \"results\": {\n      \"random_resolve_rate\": 0.22,\n      \"random_resolved_count\": 66,\n      \"embedding_resolve_rate\": 0.245,\n      \"embedding_resolved_count\": 73,\n      \"dataflow_resolve_rate\": 0.252,\n      \"dataflow_resolved_count\": 76,\n      \"embedding_minus_random_pp\": 2.5,\n      \"dataflow_minus_random_pp\": 3.2,\n      \"dataflow_minus_embedding_pp\": 0.7,\n      \"total_instances\": 300,\n      \"retriever_top_k\": 5,\n      \"agent_model\": \"Qwen3.6-27B\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: SWE-bench Lite Resolve Rate\",\n        \"columns\": [\n          \"Strategy\",\n          \"Resolved\",\n          \"Total\",\n          \"Rate (%)\",\n          \"Δ vs Random (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"random\",\n            66,\n            300,\n            22.0,\n            \"—\"\n          ],\n          [\n            \"embedding\",\n            73,\n            300,\n            24.3,\n            \"+2.3\"\n          ],\n          [\n            \"dataflow\",\n            76,\n            300,\n            25.3,\n            \"+3.3\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4b: SWE-bench by Patch Complexity\",\n        \"columns\": [\n          \"Patch Type\",\n          \"N\",\n          \"random (%)\",\n          \"embedding (%)\",\n          \"dataflow (%)\"\n        ],\n        \"rows\": [\n          [\n            \"single-file\",\n            189,\n            28.0,\n            30.7,\n            30.2\n          ],\n          [\n            \"multi-file\",\n            111,\n            11.7,\n            14.4,\n            17.1\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Multi-file patches（占 37%）是 dataflow 拉开差距的主要来源：dataflow 在 multi-file 上 +5.4pp vs random，远大于 single-file 的 +2.2pp。这与 Claim 2 一致——dataflow negatives 使 retriever 更好地理解跨模块依赖。Embedding vs random 在 multi-file 上也有 +2.7pp，说明更难的 negatives 普遍有益。总体 resolve rate 22-25% 与 SweRank/SWE-Fixer 文献报告的 retriever-only baseline 一致。\\n\\n\\nEmbedding retriever 在 SWE-bench 上提升 +2.5pp，因为 bug-fix patch 通常涉及与 issue 描述 语义相似但非完全匹配的文件——embedding mining 训练使 retriever 更擅长区分\\\"近似但无关\\\" 与\\\"近似且相关\\\"的文件。Dataflow 额外提升 +0.7pp（总 +3.2pp vs random）因为 SWE-bench patch 经常跨函数/跨模块（约 40% 涉及 caller-callee 关系），dataflow negatives 训练使 retriever 理解\\\"调用链上的文件更可能共同出现在 patch 中\\\"。Delta 幅度从 retrieval R@1 的 +2.0/+1.0pp 放大到下游 resolve rate 的 +2.5/+3.2pp，符合检索质量在端到端任务中 的杠杆效应——正确检索一个关键文件可以使原本完全失败的 patch 变为可解决。 效果幅度在 swebench_resolve_rate_delta_pp [1.5, 4.0] 范围内。\\n\"\n  },\n  {\n    \"name\": \"RepoBench-R Cross-File Retrieval with Multi-Seed CIs\",\n    \"description\": \"RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 9 seeds × 3 strategies × 2 encoders，报告 R@1 均值 + 95% bootstrap CI。\\n\",\n    \"results\": {\n      \"qwen_test_hard\": {\n        \"random_R1_mean\": 0.621,\n        \"random_R1_ci\": [\n          0.614,\n          0.628\n        ],\n        \"embedding_R1_mean\": 0.642,\n        \"embedding_R1_ci\": [\n          0.634,\n          0.65\n        ],\n        \"dataflow_R1_mean\": 0.633,\n        \"dataflow_R1_ci\": [\n          0.624,\n          0.642\n        ],\n        \"embedding_minus_random_pp\": 2.1,\n        \"dataflow_minus_random_pp\": 1.2\n      },\n      \"qwen_test_easy\": {\n        \"random_R1_mean\": 0.843,\n        \"embedding_R1_mean\": 0.855,\n        \"dataflow_R1_mean\": 0.85,\n        \"embedding_minus_random_pp\": 1.2\n      },\n      \"starcoder_test_hard\": {\n        \"random_R1_mean\": 0.574,\n        \"random_R1_ci\": [\n          0.566,\n          0.582\n        ],\n        \"embedding_R1_mean\": 0.589,\n        \"embedding_R1_ci\": [\n          0.58,\n          0.598\n        ],\n        \"dataflow_R1_mean\": 0.572,\n        \"dataflow_R1_ci\": [\n          0.562,\n          0.582\n        ],\n        \"embedding_minus_random_pp\": 1.5,\n        \"dataflow_minus_random_pp\": -0.2\n      },\n      \"starcoder_test_easy\": {\n        \"random_R1_mean\": 0.812,\n        \"embedding_R1_mean\": 0.822,\n        \"dataflow_R1_mean\": 0.81\n      },\n      \"repobench_R1_delta_pp_embedding_avg\": 1.8,\n      \"bootstrap_CI_width_R1_pp_avg\": 1.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: RepoBench-R Results (test_hard, pool≈18)\",\n        \"columns\": [\n          \"Encoder\",\n          \"Strategy\",\n          \"R@1 (%)\",\n          \"95% CI\",\n          \"Δ vs Random (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            \"random\",\n            62.1,\n            \"[61.4, 62.8]\",\n            \"—\"\n          ],\n          [\n            \"Qwen\",\n            \"embedding\",\n            64.2,\n            \"[63.4, 65.0]\",\n            \"+2.1\"\n          ],\n          [\n            \"Qwen\",\n            \"dataflow\",\n            63.3,\n            \"[62.4, 64.2]\",\n            \"+1.2\"\n          ],\n          [\n            \"StarCoder\",\n            \"random\",\n            57.4,\n            \"[56.6, 58.2]\",\n            \"—\"\n          ],\n          [\n            \"StarCoder\",\n            \"embedding\",\n            58.9,\n            \"[58.0, 59.8]\",\n            \"+1.5\"\n          ],\n          [\n            \"StarCoder\",\n            \"dataflow\",\n            57.2,\n            \"[56.2, 58.2]\",\n            \"−0.2\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-benchmark 一致性是 best tier 的关键证据：embedding mining 在 SWE-smith 和 RepoBench-R 上均显著提升两个 encoder，dataflow 条件性获益仅限 Qwen。这排除了 \\\"结果仅限单一 benchmark\\\" 的 reviewer concern。Test_easy 上 delta 被压缩（pool=6 ceiling effect）是预期行为，反向验证了 pool size 对绝对效果幅度的调节作用。\\n\\n\\nRepoBench-R 是 cross-file completion 任务，pool 更小（6-18），绝对 R@1 更高。 Embedding mining 在两个 encoder 上均显著提升 test_hard R@1（Qwen +2.1pp, StarCoder +1.5pp）， 因为 pool=18 仍有足够 distractors 使 mining 质量差异体现。Test_easy pool=6 接近 ceiling，delta 被压缩但方向一致。Dataflow 在 Qwen test_hard 上 +1.2pp 但 CI 刚好 排除零，StarCoder 上无效（-0.2pp，CI 含零）——与 SWE-smith 上的 encoder-strategy interaction 完全一致，说明 pattern 跨 benchmark 稳定。CI 宽度 ~1.2pp 在 bootstrap_CI_width_R1_pp [0.5, 2.0] 范围内，9 seeds 提供足够统计功效。\\n\"\n  },\n  {\n    \"name\": \"Stratified Analysis with Structural Coverage & Neg Difficulty Quartiles\",\n    \"description\": \"5 层分层分析：repo size / pool size / query-positive similarity / structural data availability (34% vs 66%) / neg_difficulty quartile。使用 M2 best checkpoints 在 SWE-smith validation 上重新评估。\\n\",\n    \"results\": {\n      \"stratum_structural_available\": {\n        \"with_dataflow_34pct\": {\n          \"qwen_dataflow_minus_random_pp\": 2.8,\n          \"qwen_dataflow_minus_embedding_pp\": 1.3,\n          \"starcoder_dataflow_minus_random_pp\": 0.1,\n          \"n_instances\": \"~5200\"\n        },\n        \"fallback_66pct\": {\n          \"qwen_dataflow_minus_random_pp\": 0.1,\n          \"qwen_dataflow_minus_embedding_pp\": -0.2,\n          \"starcoder_dataflow_minus_random_pp\": -0.3,\n          \"n_instances\": \"~10000\"\n        }\n      },\n      \"stratum_neg_difficulty_quartile\": {\n        \"Q1_easiest\": {\n          \"qwen_embedding_minus_random_pp\": 0.8,\n          \"qwen_dataflow_minus_random_pp\": 0.3\n        },\n        \"Q2\": {\n          \"qwen_embedding_minus_random_pp\": 1.5,\n          \"qwen_dataflow_minus_random_pp\": 0.7\n        },\n        \"Q3\": {\n          \"qwen_embedding_minus_random_pp\": 2.4,\n          \"qwen_dataflow_minus_random_pp\": 1.2\n        },\n        \"Q4_hardest\": {\n          \"qwen_embedding_minus_random_pp\": 3.2,\n          \"qwen_dataflow_minus_random_pp\": 2.1\n        }\n      },\n      \"stratum_repo_size\": {\n        \"small_lt50\": {\n          \"embedding_delta_pp\": 2.8,\n          \"n\": \"~500\"\n        },\n        \"medium_50_200\": {\n          \"embedding_delta_pp\": 2.2,\n          \"n\": \"~4100\"\n        },\n        \"large_200_500\": {\n          \"embedding_delta_pp\": 1.8,\n          \"n\": \"~5500\"\n        },\n        \"xlarge_500plus\": {\n          \"embedding_delta_pp\": 1.6,\n          \"n\": \"~5100\"\n        }\n      },\n      \"stratum_pool_size\": {\n        \"pool_lt20\": {\n          \"embedding_delta_pp\": 1.0,\n          \"dataflow_delta_pp\": 0.3\n        },\n        \"pool_20_50\": {\n          \"embedding_delta_pp\": 2.1,\n          \"dataflow_delta_pp\": 1.0\n        },\n        \"pool_gt50\": {\n          \"embedding_delta_pp\": 2.5,\n          \"dataflow_delta_pp\": 1.4\n        }\n      },\n      \"stratum_query_pos_sim\": {\n        \"high_sim_gt095\": {\n          \"embedding_delta_pp\": 2.6,\n          \"dataflow_delta_pp\": 1.8\n        },\n        \"medium_sim_085_095\": {\n          \"embedding_delta_pp\": 1.9,\n          \"dataflow_delta_pp\": 0.8\n        },\n        \"low_sim_lt085\": {\n          \"embedding_delta_pp\": 1.2,\n          \"dataflow_delta_pp\": 0.2\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Stratified R@1 Delta by Structural Data Availability (Qwen)\",\n        \"columns\": [\n          \"Stratum\",\n          \"N\",\n          \"random R@1\",\n          \"embedding R@1\",\n          \"dataflow R@1\",\n          \"df−rand (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"With dataflow (34%)\",\n            \"~5.2K\",\n            53.1,\n            55.4,\n            55.9,\n            \"+2.8\"\n          ],\n          [\n            \"Fallback (66%)\",\n            \"~10K\",\n            55.2,\n            57.3,\n            55.3,\n            \"+0.1\"\n          ],\n          [\n            \"Overall\",\n            \"~15.2K\",\n            54.5,\n            56.5,\n            55.5,\n            \"+1.0\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7b: R@1 Delta by Neg Difficulty Quartile (Qwen)\",\n        \"columns\": [\n          \"Quartile\",\n          \"margin_mean\",\n          \"emb−rand (pp)\",\n          \"df−rand (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Q1 (easiest)\",\n            0.142,\n            \"+0.8\",\n            \"+0.3\"\n          ],\n          [\n            \"Q2\",\n            0.078,\n            \"+1.5\",\n            \"+0.7\"\n          ],\n          [\n            \"Q3\",\n            0.031,\n            \"+2.4\",\n            \"+1.2\"\n          ],\n          [\n            \"Q4 (hardest)\",\n            0.008,\n            \"+3.2\",\n            \"+2.1\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Stratified analysis 提供了论文中最强的 mechanistic 证据。Neg_difficulty Q4 的 +3.2pp embedding delta 是 overall +2.0pp 的 1.6 倍——越难的 instances 从 harder negatives 获益越多，这是 representation saturation 理论的直接预测。Structural-available vs fallback 分解消除了 \\\"diluted signal\\\" concern 并揭示 dataflow 的真实 per-instance 效果（+2.8pp）远大于 pooled 报告值。\\n\\n\\nStructural-available stratum（34%）上 dataflow 优势放大到 +2.8pp（Qwen），因为这些 instance 实际接收了 dataflow-disconnected negatives——真实训练信号未被 fallback 稀释。 Fallback stratum（66%）上 dataflow ≈ embedding（±0.2pp），因为 fallback 时 dataflow 策略退化为 embedding 或 random 选择，无结构信号注入。这一分解直接回应 reviewer 关于 \\\"34% coverage 稀释 signal\\\" 的 concern——真实 per-instance 效果是 +2.8pp 而非 pooled +1.0pp。Neg_difficulty Q4（最难 quartile）上 delta 最大（embedding +3.2pp, dataflow +2.1pp），符合 representation saturation 理论——Qwen 在高 pos_sim 区域最需要 harder negatives，而 Q4 恰好是 margin 最小、分辨最难的 instances。Q1（最容易）delta 最小 因为 random negatives 已经足够容易区分。Repo size 上 small repo delta 更大因为 小 repo 的 candidate pool 更集中，mining 策略差异更容易体现。\\n\"\n  },\n  {\n    \"name\": \"Call-Graph Hop Depth Ablation (1/2/3-hop)\",\n    \"description\": \"比较 1-hop / 2-hop / 3-hop call-graph bounding 对 dataflow negative 质量的影响。 Qwen encoder, 1 seed, SWE-smith validation。\\n\",\n    \"results\": {\n      \"hop_1\": {\n        \"R1\": 0.548,\n        \"connected_coverage_pct\": 12.4,\n        \"negatives_per_query_mean\": 18.2\n      },\n      \"hop_2\": {\n        \"R1\": 0.555,\n        \"connected_coverage_pct\": 34.3,\n        \"negatives_per_query_mean\": 31.7\n      },\n      \"hop_3\": {\n        \"R1\": 0.551,\n        \"connected_coverage_pct\": 58.6,\n        \"negatives_per_query_mean\": 42.1\n      },\n      \"optimal_hop\": 2,\n      \"hop2_minus_hop1_pp\": 0.7,\n      \"hop3_minus_hop2_pp\": -0.4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Hop Depth Ablation (Qwen, dataflow strategy)\",\n        \"columns\": [\n          \"Hops\",\n          \"Coverage (%)\",\n          \"Neg/query\",\n          \"R@1 (%)\",\n          \"Δ vs 2-hop (pp)\"\n        ],\n        \"rows\": [\n          [\n            1,\n            12.4,\n            18.2,\n            54.8,\n            \"−0.7\"\n          ],\n          [\n            2,\n            34.3,\n            31.7,\n            55.5,\n            \"—\"\n          ],\n          [\n            3,\n            58.6,\n            42.1,\n            55.1,\n            \"−0.4\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"2-hop optimal 符合 inter-procedural dataflow 的语义：1-hop = 直接 caller/callee， 2-hop = caller 的 caller 或 callee 的 callee（一层间接调用），3-hop 开始包含 过于间接的关系。论文可以强调 2-hop 选择有 principled 依据而非纯粹 empirical tuning。\\n\\n\\n2-hop 是最优平衡点。1-hop 太保守——仅 12.4% coverage 意味着大部分 instance 没有足够的 connected 节点来定义 \\\"disconnected\\\" negatives，退化为 random。3-hop 过于宽松——58.6% coverage 下 \\\"disconnected\\\" 的定义变得太窄，许多语义相关但间接连接的文件被错误排除在 negative pool 外，引入噪声。2-hop 的 34.3% coverage（与 M1 extraction 的 structural data rate 一致）在 \\\"enough connected nodes to define meaningful disconnection\\\" 和 \\\"disconnected set still contains genuinely unrelated files\\\" 之间取得平衡。\\n\"\n  },\n  {\n    \"name\": \"Training Data Size Scaling (1K/3K/5K)\",\n    \"description\": \"固定 Qwen encoder + embedding strategy，训练数据从 1K / 3K / 5K instances 增长， 观察 R@1 变化和策略排名稳定性。\\n\",\n    \"results\": {\n      \"size_1K\": {\n        \"random_R1\": 0.51,\n        \"embedding_R1\": 0.522,\n        \"dataflow_R1\": 0.515,\n        \"embedding_minus_random_pp\": 1.2,\n        \"seed_std\": 0.015\n      },\n      \"size_3K\": {\n        \"random_R1\": 0.532,\n        \"embedding_R1\": 0.55,\n        \"dataflow_R1\": 0.541,\n        \"embedding_minus_random_pp\": 1.8,\n        \"seed_std\": 0.01\n      },\n      \"size_5K\": {\n        \"random_R1\": 0.545,\n        \"embedding_R1\": 0.565,\n        \"dataflow_R1\": 0.555,\n        \"embedding_minus_random_pp\": 2.0,\n        \"seed_std\": 0.008\n      },\n      \"ranking_stable\": true,\n      \"monotonic_improvement\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Data Size Scaling (Qwen)\",\n        \"columns\": [\n          \"Size\",\n          \"random R@1\",\n          \"embedding R@1\",\n          \"dataflow R@1\",\n          \"emb−rand (pp)\",\n          \"σ across seeds\"\n        ],\n        \"rows\": [\n          [\n            \"1K\",\n            51.0,\n            52.2,\n            51.5,\n            \"+1.2\",\n            1.5\n          ],\n          [\n            \"3K\",\n            53.2,\n            55.0,\n            54.1,\n            \"+1.8\",\n            1.0\n          ],\n          [\n            \"5K\",\n            54.5,\n            56.5,\n            55.5,\n            \"+2.0\",\n            0.8\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Monotonic scaling + stable ranking 表明结果不是 small-data artifact。5K 时未见 diminishing returns，暗示更大数据集可能进一步放大差异。这对 reviewer \\\"effect size marginal\\\" concern 有价值——delta 仍在增长，当前 +2.0pp 是下界而非上界。\\n\\n\\n策略排名在 1K/3K/5K 三个尺度上保持一致（embedding > dataflow > random），但 delta 幅度随数据量增大而增大——1K 时 +1.2pp，5K 时 +2.0pp。这是因为更大的训练集提供更多 diverse negatives，使 mining 策略的差异更充分地体现。1K 时 seed 方差较大（std=0.015） 因为 negative 多样性不足，个别 seed 的 negative 采样偶然性影响结果。5K 时方差收敛 （std=0.008），mining 策略的信号超过采样噪声。No diminishing returns at 5K suggests further scaling could help, but is beyond scope。\\n\"\n  },\n  {\n    \"name\": \"Fusion Head Ablation\",\n    \"description\": \"比较 embedding-only / structural-features-only / combined fusion head， 隔离 training-time mining 价值与 inference-time feature injection。\\n\",\n    \"results\": {\n      \"embedding_only\": {\n        \"qwen_R1\": 0.565,\n        \"starcoder_R1\": 0.475\n      },\n      \"structural_features_only\": {\n        \"qwen_R1\": 0.498,\n        \"starcoder_R1\": 0.421\n      },\n      \"combined_fusion\": {\n        \"qwen_R1\": 0.561,\n        \"starcoder_R1\": 0.472\n      },\n      \"embedding_only_minus_combined_pp\": 0.4,\n      \"conclusion\": \"mining > fusion; structural features at inference add noise\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Fusion Head Ablation\",\n        \"columns\": [\n          \"Configuration\",\n          \"Qwen R@1 (%)\",\n          \"StarCoder R@1 (%)\"\n        ],\n        \"rows\": [\n          [\n            \"embedding-only (ours)\",\n            56.5,\n            47.5\n          ],\n          [\n            \"structural-features-only\",\n            49.8,\n            42.1\n          ],\n          [\n            \"combined fusion\",\n            56.1,\n            47.2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"训练时注入 structural signal 通过 negative mining（间接信号）比 inference 时直接注入 structural features（直接信号）更有效。可能原因：mining 让 encoder 自己学习结构相关的 representation，而直接注入 features 绕过了 encoder 的学习过程，且 CodeQL 34% coverage 意味着 66% instance 在 inference 时收到 zero-vector structural features，引入 noise。\\n\\n\\nEmbedding-only（仅用 embedding mining 训练的 retriever，inference 时不注入结构特征） 表现最好或 tied with combined。Combined fusion 略低 0.4pp 因为 inference-time structural features 引入了不精确的 CodeQL connectivity 信号——recall 某些 CodeQL extraction 失败的 instance 反而被错误降权。Structural-features-only（不用 mining 训练， 仅在 inference 注入结构特征）远低于 embedding-only（-6.7pp Qwen），证明核心价值在 training-time negative mining 而非 inference-time feature engineering。 这一结果对 paper framing 极为重要：StructFuse 的贡献是 mining strategy，不是 fusion。\\n\"\n  },\n  {\n    \"name\": \"Dataflow-Distance Weighted vs Binary Negatives\",\n    \"description\": \"比较 binary connected/disconnected 与 dataflow-distance weighted negative sampling。 Weighted: disconnected 且 hop-distance 更远的文件被赋予更高采样概率。\\n\",\n    \"results\": {\n      \"binary_qwen_R1\": 0.555,\n      \"weighted_qwen_R1\": 0.558,\n      \"binary_starcoder_R1\": 0.458,\n      \"weighted_starcoder_R1\": 0.459,\n      \"weighted_minus_binary_qwen_pp\": 0.3,\n      \"weighted_minus_binary_starcoder_pp\": 0.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S1: Weighted vs Binary Dataflow Negatives\",\n        \"columns\": [\n          \"Method\",\n          \"Qwen R@1 (%)\",\n          \"StarCoder R@1 (%)\",\n          \"Δ vs Binary (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Binary (default)\",\n            55.5,\n            45.8,\n            \"—\"\n          ],\n          [\n            \"Distance-weighted\",\n            55.8,\n            45.9,\n            \"+0.3 / +0.1\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Binary is sufficient — complexity of weighted sampling not justified. 论文可在 ablation section 用一句话报告这一 negative result， 强化 \\\"simple binary structural signal is the key insight\\\" 的 narrative。\\n\\n\\nWeighted 在 Qwen 上仅微弱提升 +0.3pp（不显著），StarCoder 上几乎无差异。 原因：binary disconnected/connected 已经捕获了最关键的 structural distinction—— \\\"是否在调用链上\\\"。进一步按 hop distance 加权引入的额外信号被 noise 抵消：距离更远 不一定意味着更好的 negative（一个完全无关的 utility 文件可能 hop=∞ 但也是 trivial negative）。 Binary 的简洁性是优势——fewer hyperparameters, same effect。\\n\"\n  },\n  {\n    \"name\": \"SWE-bench Failure Analysis (50 cases)\",\n    \"description\": \"从 random retriever 的 SWE-bench 失败案例中抽样 50 个，人工分类失败原因， 标注 dataflow 信号是否可能帮助。\\n\",\n    \"results\": {\n      \"total_analyzed\": 50,\n      \"category_breakdown\": {\n        \"retrieval_failure_wrong_files\": 22,\n        \"retrieval_success_but_agent_fail\": 15,\n        \"insufficient_context_window\": 7,\n        \"test_environment_issue\": 4,\n        \"ambiguous_issue_description\": 2\n      },\n      \"dataflow_could_help\": {\n        \"true\": 14,\n        \"partially\": 5,\n        \"false\": 31\n      },\n      \"dataflow_help_rate\": 0.28,\n      \"key_pattern\": \"14/22 retrieval failures involve cross-module dependencies where the gold file is a caller/callee of a retrieved-but-wrong file — dataflow connectivity would directly address these.\\n\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S2: Failure Category Breakdown\",\n        \"columns\": [\n          \"Category\",\n          \"Count\",\n          \"% of 50\",\n          \"Dataflow Could Help?\"\n        ],\n        \"rows\": [\n          [\n            \"Retrieval: wrong files\",\n            22,\n            44,\n            \"14/22 (64%)\"\n          ],\n          [\n            \"Retrieval OK, agent fail\",\n            15,\n            30,\n            \"N/A\"\n          ],\n          [\n            \"Context window limit\",\n            7,\n            14,\n            \"5/7 partially\"\n          ],\n          [\n            \"Test env issue\",\n            4,\n            8,\n            \"No\"\n          ],\n          [\n            \"Ambiguous issue\",\n            2,\n            4,\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"28% of failures could benefit from dataflow signal, consistent with the observed +3.2pp resolve rate improvement. The 64% rate within retrieval failures confirms that cross-module dependency is the primary retrieval challenge, directly supporting Claim 2's motivation.\\n\\n\\n50 个失败中 22 个是 retrieval failure（检索到错误文件），其中 14 个涉及跨模块依赖—— 被检索的文件和 gold 文件有高文本相似度但分属不同 call chain。Dataflow negatives 训练 恰好针对这类 confound。15 个 retrieval success but agent fail 说明 retrieval 不是 唯一瓶颈——agent 的 patch 生成能力也是限制因素。这为论文提供了 \\\"ceiling analysis\\\"： 即使 perfect retrieval，resolve rate 上限约 85%（15% 是 agent 能力限制）。\\n\"\n  },\n  {\n    \"name\": \"Qualitative Examples (5-10 cases)\",\n    \"description\": \"从 SWE-bench 和 SWE-smith 中选取 5-10 个 dataflow negatives 改变检索结果的典型案例， 展示 structural signal 的具体作用机制。\\n\",\n    \"results\": {\n      \"total_examples\": 8,\n      \"example_categories\": {\n        \"caller_callee_confusion\": 3,\n        \"utility_file_distraction\": 2,\n        \"cross_module_import_chain\": 2,\n        \"test_file_vs_source\": 1\n      },\n      \"illustrative_example\": {\n        \"issue\": \"django/django#12345 — QuerySet.filter() returns wrong results with nested Q objects\",\n        \"random_retriever_top1\": \"django/db/models/query.py (text match on 'filter')\",\n        \"dataflow_retriever_top1\": \"django/db/models/sql/query.py (actual SQL generation called by filter)\",\n        \"gold\": \"django/db/models/sql/query.py\",\n        \"explanation\": \"Random retriever picks query.py (contains 'filter' method signature) but the bug is in sql/query.py (the downstream SQL builder called by filter). Dataflow training teaches the model that sql/query.py is structurally connected to query.py via 2-hop call chain, making it a better negative for other instances, which in turn improves the model's ability to rank the actual implementation file higher.\\n\"\n      }\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Qualitative examples serve as the paper's \\\"aha moment\\\" — they make the abstract representation geometry argument concrete. Reviewer-facing value: even skeptics who question statistical significance can see the mechanism operating on real code.\\n\\n\\n8 个案例覆盖 4 个失败模式：caller-callee confusion（3 个，最常见——文本相似的 wrapper 函数 vs 实际实现）、utility file distraction（2 个——高文本重叠的 helper 文件干扰）、 cross-module import chain（2 个——A 导入 B 导入 C，bug 在 C 但文本匹配 A）、test vs source（1 个——test file 包含几乎完整的 source code 复制）。这些案例具体展示了 \\\"lexical similarity ≠ structural relevance\\\" 的核心 insight。\\n\"\n  },\n  {\n    \"name\": \"Temperature Ablation τ ∈ {0.05, 0.1, 0.2}\",\n    \"description\": \"3 temperatures × 3 strategies × 2 encoders, 1 seed each. 测试 strategy ranking 是否 regime-specific。\\n\",\n    \"results\": {\n      \"tau_005\": {\n        \"qwen_random_R1\": 0.558,\n        \"qwen_embedding_R1\": 0.577,\n        \"qwen_dataflow_R1\": 0.569,\n        \"qwen_embedding_minus_random_pp\": 1.9,\n        \"starcoder_random_R1\": 0.47,\n        \"starcoder_embedding_R1\": 0.485,\n        \"starcoder_dataflow_R1\": 0.467,\n        \"starcoder_embedding_minus_random_pp\": 1.5\n      },\n      \"tau_010\": {\n        \"qwen_random_R1\": 0.545,\n        \"qwen_embedding_R1\": 0.565,\n        \"qwen_dataflow_R1\": 0.555,\n        \"qwen_embedding_minus_random_pp\": 2.0,\n        \"starcoder_random_R1\": 0.46,\n        \"starcoder_embedding_R1\": 0.475,\n        \"starcoder_dataflow_R1\": 0.458,\n        \"starcoder_embedding_minus_random_pp\": 1.5\n      },\n      \"tau_020\": {\n        \"qwen_random_R1\": 0.53,\n        \"qwen_embedding_R1\": 0.546,\n        \"qwen_dataflow_R1\": 0.538,\n        \"qwen_embedding_minus_random_pp\": 1.6,\n        \"starcoder_random_R1\": 0.448,\n        \"starcoder_embedding_R1\": 0.461,\n        \"starcoder_dataflow_R1\": 0.447,\n        \"starcoder_embedding_minus_random_pp\": 1.3\n      },\n      \"ranking_preserved_across_tau\": true,\n      \"optimal_tau\": 0.05\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Temperature Ablation (R@1 %)\",\n        \"columns\": [\n          \"τ\",\n          \"Encoder\",\n          \"random\",\n          \"embedding\",\n          \"dataflow\",\n          \"emb−rand (pp)\"\n        ],\n        \"rows\": [\n          [\n            0.05,\n            \"Qwen\",\n            55.8,\n            57.7,\n            56.9,\n            \"+1.9\"\n          ],\n          [\n            0.05,\n            \"StarCoder\",\n            47.0,\n            48.5,\n            46.7,\n            \"+1.5\"\n          ],\n          [\n            0.1,\n            \"Qwen\",\n            54.5,\n            56.5,\n            55.5,\n            \"+2.0\"\n          ],\n          [\n            0.1,\n            \"StarCoder\",\n            46.0,\n            47.5,\n            45.8,\n            \"+1.5\"\n          ],\n          [\n            0.2,\n            \"Qwen\",\n            53.0,\n            54.6,\n            53.8,\n            \"+1.6\"\n          ],\n          [\n            0.2,\n            \"StarCoder\",\n            44.8,\n            46.1,\n            44.7,\n            \"+1.3\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ranking stability across τ 是重要的 robustness evidence。τ=0.2 下 delta 缩小但 不翻转，说明 mining quality 的价值在不同 loss sharpness 下都存在。Paper 可以报告 τ=0.05 作为 alternative best configuration 但选择 τ=0.1 作为 default（更常见的 literature default）。\\n\\n\\nStrategy ranking（embedding > dataflow > random for Qwen; embedding > random ≈ dataflow for StarCoder）在三个 temperature 下保持一致。τ=0.05 绝对性能最高因为 sharper temperature 使 contrastive loss 更有效地区分相似度差异（harder gradient signal）。 τ=0.2 下所有策略性能下降且 delta 缩小（1.6pp vs 2.0pp），因为 softer temperature 减弱了 negative 选择质量的影响——当所有 similarity 被压缩到窄范围内，hard vs easy negatives 的梯度差异变小。关键结论：findings 不是 temperature-regime-specific， 直接回应 median reviewer 的 \\\"τ=0.05 unusually low\\\" concern。\\n\"\n  },\n  {\n    \"name\": \"Dynamic vs Static Embedding Mining\",\n    \"description\": \"Dynamic: 每 epoch 重新用当前 encoder 挖 embedding negatives。 Static: 仅用 pretrained encoder 挖一次（当前做法）。 Qwen + StarCoder, 1 seed each。\\n\",\n    \"results\": {\n      \"qwen_static_R1\": 0.565,\n      \"qwen_dynamic_R1\": 0.568,\n      \"qwen_dynamic_minus_static_pp\": 0.3,\n      \"starcoder_static_R1\": 0.475,\n      \"starcoder_dynamic_R1\": 0.477,\n      \"starcoder_dynamic_minus_static_pp\": 0.2,\n      \"dynamic_significant\": false,\n      \"curriculum_confound_ruled_out\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Static vs Dynamic Embedding Mining\",\n        \"columns\": [\n          \"Encoder\",\n          \"Static R@1 (%)\",\n          \"Dynamic R@1 (%)\",\n          \"Δ (pp)\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            56.5,\n            56.8,\n            \"+0.3\",\n            0.41\n          ],\n          [\n            \"StarCoder\",\n            47.5,\n            47.7,\n            \"+0.2\",\n            0.53\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Static ≈ dynamic 是 clean negative result，强化了论文 narrative：关键是 negative 的 semantic quality（embedding vs random vs dataflow），不是 freshness。 也简化了 practitioner recommendation——mine once from pretrained, no need for per-epoch re-mining。\\n\\n\\nDynamic mining 仅微弱提升 +0.2-0.3pp（不显著），因为 LoRA rank 16 的 fine-tuning 只轻微改变 embedding space——pretrained encoder 的 nearest neighbors 在训练后 仍然大部分相同。这排除了 \\\"static mining 的优势来自 curriculum effect（early epochs 看到 harder negatives 然后 negatives 变 stale）\\\" 的 confound——即使更新 negatives， 效果几乎不变。对 Claim 2 很重要：说明 mining strategy 的选择（what to mine）比 mining schedule（when to mine）更关键。Dynamic mining 的 compute overhead（每 epoch 重新 encode + kNN）不 justified。\\n\"\n  },\n  {\n    \"name\": \"Bootstrap CIs for SWE-bench Lite Resolve Rate\",\n    \"description\": \"对 plan_003 的 SWE-bench 结果计算 10K bootstrap resamples 的 95% CI， 报告 paired difference CIs 和 p-values。\\n\",\n    \"results\": {\n      \"embedding_minus_random\": {\n        \"delta_pp\": 2.5,\n        \"ci_95\": [\n          0.7,\n          4.3\n        ],\n        \"p_value\": 0.018,\n        \"significant\": true\n      },\n      \"dataflow_minus_random\": {\n        \"delta_pp\": 3.2,\n        \"ci_95\": [\n          1.0,\n          5.5\n        ],\n        \"p_value\": 0.008,\n        \"significant\": true\n      },\n      \"dataflow_minus_embedding\": {\n        \"delta_pp\": 0.7,\n        \"ci_95\": [\n          -1.5,\n          2.9\n        ],\n        \"p_value\": 0.134,\n        \"significant\": false\n      },\n      \"bootstrap_n\": 10000,\n      \"sample_size\": 300\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4c: SWE-bench Bootstrap Significance Tests\",\n        \"columns\": [\n          \"Comparison\",\n          \"Δ (pp)\",\n          \"95% CI\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"embedding − random\",\n            \"+2.5\",\n            \"[+0.7, +4.3]\",\n            0.018\n          ],\n          [\n            \"dataflow − random\",\n            \"+3.2\",\n            \"[+1.0, +5.5]\",\n            0.008\n          ],\n          [\n            \"dataflow − embedding\",\n            \"+0.7\",\n            \"[−1.5, +2.9]\",\n            0.134\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CI 下界 > 0 for both mining strategies vs random 是 EMNLP reviewer 需要的统计保证。 Dataflow vs embedding 不显著是 honest reporting 且与 Claim 2 的 \\\"conditional\\\" framing 一致——dataflow 的额外价值不是 universally separable at SWE-bench scale。\\n\\n\\nEmbedding vs random CI [0.7, 4.3] 排除零（p=0.018），确认 embedding mining 在下游 任务上的统计显著提升。Dataflow vs random 更显著（p=0.008）因为 delta 更大且 SWE-bench 中 cross-module patches 对 dataflow signal 响应一致。Dataflow vs embedding 不显著 （p=0.134, CI 含零）——300 instances 的 power 不足以区分 +0.7pp 的小 delta，这是 expected：retrieval level 的 ~1pp 差异在下游 binary resolve 结果上被放大和噪声化。 CI 宽度 ~3.6pp 反映 300 样本的 inherent variance——SWE-bench Lite 不是为精确 delta 估计设计的 benchmark。\\n\"\n  },\n  {\n    \"name\": \"Inference-Time Graph Method Literature Comparison\",\n    \"description\": \"文献分析（非实验）：与 CodexGraph, LocAgent, RANGER 等 inference-time 图方法的 系统比较。已完成 8 篇论文 survey。\\n\",\n    \"results\": {\n      \"papers_surveyed\": 8,\n      \"key_distinction\": \"training-time mining (ours) vs inference-time graph navigation\",\n      \"complementarity_evidence\": \"All 8 methods operate at inference time; StructFuse mines at training time. The two approaches are complementary — StructFuse improves the base retriever that graph methods navigate over.\\n\",\n      \"papers_list\": [\n        \"CodexGraph\",\n        \"LocAgent\",\n        \"RANGER\",\n        \"GraphCoder\",\n        \"ARISE\",\n        \"RepoGraph\",\n        \"CodeGRAG\",\n        \"CodeRAG\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S3: Comparison with Inference-Time Graph Methods\",\n        \"columns\": [\n          \"Method\",\n          \"Graph Stage\",\n          \"Graph Type\",\n          \"Complementary?\"\n        ],\n        \"rows\": [\n          [\n            \"StructFuse (ours)\",\n            \"Training\",\n            \"Dataflow (CodeQL)\",\n            \"—\"\n          ],\n          [\n            \"CodexGraph\",\n            \"Inference\",\n            \"Code graph DB\",\n            \"Yes\"\n          ],\n          [\n            \"LocAgent\",\n            \"Inference\",\n            \"Repo structure\",\n            \"Yes\"\n          ],\n          [\n            \"RANGER\",\n            \"Inference\",\n            \"Call graph\",\n            \"Yes\"\n          ],\n          [\n            \"ARISE\",\n            \"Inference\",\n            \"Intra-proc dataflow\",\n            \"Partially (intra only)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Discussion 中用 2 段落即可。不要 overclaim StructFuse 优于这些方法——它们解决不同问题。 Highlight: StructFuse 是唯一在 training time 利用结构信号的方法，且不增加 inference cost。\\n\\n\\n8 篇 inference-time graph 方法均在推理阶段构建/遍历代码图，而 StructFuse 在训练阶段 通过 negative mining 将结构信号蒸馏进 encoder。两者正交：StructFuse 产出更好的 base retriever，inference-time 方法在此基础上进一步 re-rank/navigate。无直接可比性因为 实验设置完全不同（LocAgent 用 LLM agent + tool calls，我们用 embedding retrieval）。 Discussion section 应明确 \\\"complementary, not competing\\\" 的定位。\\n\"\n  },\n  {\n    \"name\": \"BM25 Negative Baseline — Closing CoCoHaNeRe Argument\",\n    \"description\": \"BM25-based hard negatives 作为第 4 策略，1+ seed × 2 encoders。 验证 CoCoHaNeRe 报告的 \\\"embedding negatives harm\\\" 实际是 BM25-proxy artifact。\\n\",\n    \"results\": {\n      \"qwen\": {\n        \"bm25_R1\": 0.52,\n        \"random_R1\": 0.545,\n        \"embedding_R1\": 0.565,\n        \"dataflow_R1\": 0.555,\n        \"bm25_minus_random_pp\": -2.5,\n        \"embedding_minus_bm25_pp\": 4.5\n      },\n      \"starcoder\": {\n        \"bm25_R1\": 0.433,\n        \"random_R1\": 0.46,\n        \"embedding_R1\": 0.475,\n        \"dataflow_R1\": 0.458,\n        \"bm25_minus_random_pp\": -2.7,\n        \"embedding_minus_bm25_pp\": 4.2\n      },\n      \"bm25_harms_both_encoders\": true,\n      \"cocohanere_artifact_confirmed\": true,\n      \"bm25_minus_random_avg_pp\": -2.6\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Full 4-Strategy Comparison Including BM25 Baseline\",\n        \"columns\": [\n          \"Encoder\",\n          \"Strategy\",\n          \"R@1 (%)\",\n          \"95% CI\",\n          \"Δ vs Random (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            \"BM25\",\n            52.0,\n            \"[51.2, 52.8]\",\n            \"−2.5\"\n          ],\n          [\n            \"Qwen\",\n            \"random\",\n            54.5,\n            \"[53.8, 55.2]\",\n            \"—\"\n          ],\n          [\n            \"Qwen\",\n            \"dataflow\",\n            55.5,\n            \"[54.6, 56.4]\",\n            \"+1.0\"\n          ],\n          [\n            \"Qwen\",\n            \"embedding\",\n            56.5,\n            \"[55.8, 57.2]\",\n            \"+2.0\"\n          ],\n          [\n            \"StarCoder\",\n            \"BM25\",\n            43.3,\n            \"[42.3, 44.3]\",\n            \"−2.7\"\n          ],\n          [\n            \"StarCoder\",\n            \"random\",\n            46.0,\n            \"[45.1, 46.9]\",\n            \"—\"\n          ],\n          [\n            \"StarCoder\",\n            \"dataflow\",\n            45.8,\n            \"[44.8, 46.8]\",\n            \"−0.2\"\n          ],\n          [\n            \"StarCoder\",\n            \"embedding\",\n            47.5,\n            \"[46.6, 48.4]\",\n            \"+1.5\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"BM25 baseline 是 best tier 论文的 crown jewel experiment。它将 Claim 1 从 \\\"argumentative correction\\\" 升级为 \\\"empirical demonstration\\\"：我们不仅指出 CoCoHaNeRe 用了 BM25 proxy， 还实际运行 BM25 negatives 复现了 harm effect，然后展示 true embedding negatives 方向相反。 4-strategy ordering BM25 < random < dataflow ≤ embedding 清晰展示了 negative mining strategy 的 quality spectrum。Reviewer 对 \\\"correction without evidence\\\" 的 concern 被彻底关闭。\\n\\n\\nBM25 negatives 在两个 encoder 上均 harm performance（Qwen -2.5pp, StarCoder -2.7pp vs random），直接复现了 CoCoHaNeRe 报告的负面效果方向。关键 insight：BM25 negatives 选取的是 lexically similar 但 semantically ambiguous 的文件——它们与 query 共享大量 token overlap（function names, variable names, import patterns），但这种 overlap 恰恰是 contrastive learning 需要利用来区分 positive/negative 的信号。用 BM25 选的 negatives 让模型学会 ignore lexical cues，但这些 cues 在 code retrieval 中是有效信号。 相比之下，true embedding distance negatives 选取的是 semantically similar（在 pretrained embedding space 中近）但与 query 不同的文件，这迫使模型学习更 fine-grained semantic distinctions。BM25 vs embedding 的 4.5pp 差距（Qwen）是论文中最大的 single pairwise comparison，构成 Claim 1 correction argument 的 empirical closure。 效果幅度在 bm25_minus_random_R1_pp [-4.0, -1.5] 范围内。\\n\"\n  },\n  {\n    \"name\": \"Pool Size Sensitivity (50/100/200/500)\",\n    \"description\": \"在 SWE-smith validation 上用 pool={50, 100, 200, 500} 重新评估 M2 best checkpoints， 测试 strategy ranking 在更 realistic pool sizes 下的稳定性。\\n\",\n    \"results\": {\n      \"qwen\": {\n        \"pool_50\": {\n          \"random_R1\": 0.545,\n          \"embedding_R1\": 0.565,\n          \"dataflow_R1\": 0.555,\n          \"embedding_minus_random_pp\": 2.0\n        },\n        \"pool_100\": {\n          \"random_R1\": 0.428,\n          \"embedding_R1\": 0.447,\n          \"dataflow_R1\": 0.438,\n          \"embedding_minus_random_pp\": 1.9\n        },\n        \"pool_200\": {\n          \"random_R1\": 0.342,\n          \"embedding_R1\": 0.359,\n          \"dataflow_R1\": 0.351,\n          \"embedding_minus_random_pp\": 1.7\n        },\n        \"pool_500\": {\n          \"random_R1\": 0.261,\n          \"embedding_R1\": 0.276,\n          \"dataflow_R1\": 0.269,\n          \"embedding_minus_random_pp\": 1.5\n        }\n      },\n      \"starcoder\": {\n        \"pool_50\": {\n          \"random_R1\": 0.46,\n          \"embedding_R1\": 0.475,\n          \"dataflow_R1\": 0.458,\n          \"embedding_minus_random_pp\": 1.5\n        },\n        \"pool_100\": {\n          \"random_R1\": 0.358,\n          \"embedding_R1\": 0.372,\n          \"dataflow_R1\": 0.357,\n          \"embedding_minus_random_pp\": 1.4\n        },\n        \"pool_200\": {\n          \"random_R1\": 0.282,\n          \"embedding_R1\": 0.295,\n          \"dataflow_R1\": 0.281,\n          \"embedding_minus_random_pp\": 1.3\n        },\n        \"pool_500\": {\n          \"random_R1\": 0.214,\n          \"embedding_R1\": 0.225,\n          \"dataflow_R1\": 0.213,\n          \"embedding_minus_random_pp\": 1.1\n        }\n      },\n      \"ranking_stable_across_pools\": true,\n      \"pool_ranking_stable_pct\": 100,\n      \"delta_shrinkage_rate\": \"~0.15pp per doubling of pool size\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Pool Size Sensitivity (R@1 %)\",\n        \"columns\": [\n          \"Pool\",\n          \"Encoder\",\n          \"random\",\n          \"embedding\",\n          \"dataflow\",\n          \"emb−rand (pp)\",\n          \"Ranking\"\n        ],\n        \"rows\": [\n          [\n            50,\n            \"Qwen\",\n            54.5,\n            56.5,\n            55.5,\n            \"+2.0\",\n            \"E>D>R\"\n          ],\n          [\n            100,\n            \"Qwen\",\n            42.8,\n            44.7,\n            43.8,\n            \"+1.9\",\n            \"E>D>R\"\n          ],\n          [\n            200,\n            \"Qwen\",\n            34.2,\n            35.9,\n            35.1,\n            \"+1.7\",\n            \"E>D>R\"\n          ],\n          [\n            500,\n            \"Qwen\",\n            26.1,\n            27.6,\n            26.9,\n            \"+1.5\",\n            \"E>D>R\"\n          ],\n          [\n            50,\n            \"StarCoder\",\n            46.0,\n            47.5,\n            45.8,\n            \"+1.5\",\n            \"E>R>D\"\n          ],\n          [\n            100,\n            \"StarCoder\",\n            35.8,\n            37.2,\n            35.7,\n            \"+1.4\",\n            \"E>R>D\"\n          ],\n          [\n            200,\n            \"StarCoder\",\n            28.2,\n            29.5,\n            28.1,\n            \"+1.3\",\n            \"E>R≈D\"\n          ],\n          [\n            500,\n            \"StarCoder\",\n            21.4,\n            22.5,\n            21.3,\n            \"+1.1\",\n            \"E>R≈D\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pool size sensitivity 是外部有效性的关键证据。100% ranking stability 在 50→500 全程保持是 best tier 的标志。Delta 的 graceful degradation（非 collapse）说明 mining strategy 的价值是 robust 的。论文可以明确声明：\\\"Strategy rankings are stable across pool sizes spanning an order of magnitude (50–500), with embedding mining maintaining a statistically significant advantage even at the largest pool tested.\\\"\\n\\nStrategy ranking（embedding > dataflow > random for Qwen; embedding > random ≈ dataflow for StarCoder）在 pool 50→500 全程保持稳定（pool_ranking_stable_pct = 100%）。 绝对 R@1 随 pool 增大而下降（50→500 约 halved），因为 larger pool = more distractors = harder task。Embedding-random delta 从 2.0pp (pool=50) 缓慢缩小至 1.5pp (pool=500)， 缩小幅度约 25%，但方向和显著性保持。原因：pool=500 时 random negatives 中偶然出现 \\\"hard\\\" negative 的概率增加（base rate effect），部分缩小了 mining 策略的差异。 但核心 signal 不消失——embedding mining 在 pool=500 仍有 +1.5pp Qwen, +1.1pp StarCoder。 Dataflow 在 Qwen 上从 +1.0pp (pool=50) 降至 +0.8pp (pool=500) 但保持正值。 这直接回应 reviewer \\\"pool=50 unrealistically small\\\" concern：即使 10x pool 扩大， strategy ranking 完全不翻转。\\n\"\n  }\n]",
      "numLines": 1193,
      "startLine": 1,
      "totalLines": 1193
    }
  },
  "sourceToolAssistantUUID": "64e68f0d-17f7-400c-bef0-85f46478cc5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T16:45:57.865Z_

<details><summary>↩ Tool result · `toolu_01XM5ediYSpGoaYa5Z7hMLR8`</summary>

```text
1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3)
8	
9	1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported "harm" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).
10	
11	2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.
12	
13	3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]
14	
15	## Story Spine
16	
17	- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.
18	
19	- **Existing approaches & gaps**:
20	  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies
21	  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal
22	  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only
23	  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance
24	  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works
25	
26	- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.
27	
28	- **Headline result template**: "True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis."
29	
30	## Core Insight
31	
32	The effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.
33	
34	## Dual-Pillar Motivation
35	
36	1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.
37	2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.
38	
39	## Formal Definition
40	
41	Given retrieval domain D, structural graph G, similarity function s, query q:
42	**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)
43	
44	The structural graph is externally fixed and does not update with the encoder (drift-immune).
45	
46	## Title Options
47	
48	- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
49	- Alternative: "StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval"
50	- Backup: "Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally"
51	
52	## Venue Fit
53	
54	1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
55	2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
56	3. **Against "incremental" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.
57	
58	## Anticipated Reviewer Concerns
59	
60	| Concern | Response | Evidence |
61	|---------|----------|----------|
62	| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |
63	| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |
64	| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |
65	| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |
66	| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |
67	| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |
68	| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |
69	| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |
70	| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |
71	| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |
72	| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |
73	| "Complementary signal" overstatement | Temper: "conditionally beneficial" not "always complementary" | Writing discipline |
74	| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |
75	
76	## Evidence Status
77	
78	### Confirmed findings (basis for claims):
79	- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact
80	- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction
81	- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)
82	- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only
83	- plan_006: CodeQL scalability confirmed at 123-repo scale
84	
85	### In progress:
86	- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)
87	- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)
88	- m1_reextract_v2: expanded extraction for higher coverage
89	
90	### Planned (priority order):
91	- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)
92	- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
93	- plan_019: Pool size sensitivity (Dream consensus — external validity)
94	- plan_014: Temperature ablation (Dream reviewer concern)
95	- plan_004: RepoBench-R second benchmark (with multi-seed CIs)
96	- plan_015: Dynamic mining baseline
97	- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)
98	- plan_007/008/009: Additional ablations
99	
100	## Contingency (if full M2 results weaken claims)
101	
102	### All 18 runs confirm pilot pattern: Best case
103	- Full statistical power, paper as framed above
104	- Target: EMNLP Main
105	
106	### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
107	- Drop Claim 2 to analysis observation
108	- Paper becomes: "True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions"
109	- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main
110	
111	### Embedding mining also loses advantage at full scale: Major reassessment needed
112	- Recheck data pipeline for bugs (full-scale data may have distribution differences)
113	- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
114	- Discuss with user before committing direction
115	
116	## Deprecated Claims (with reason)
117	
118	- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0caf526-ec89-4596-a26a-bf7b5792e5e2",
  "isSidechain": false,
  "promptId": "7dbbfae7-135c-4257-9519-f147e9c1c35b",
  "type": "user",
  "uuid": "ab116609-f6c0-4b6c-8577-5063fe0e82c0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/paper_framing.md",
      "content": "# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \"harm\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).\n\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\n\n- **Headline result template**: \"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\"\n\n## Core Insight\n\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\"\n- Backup: \"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\n- m1_reextract_v2: expanded extraction for higher coverage\n\n### Planned (priority order):\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\n- plan_015: Dynamic mining baseline\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  },
  "sourceToolAssistantUUID": "b0caf526-ec89-4596-a26a-bf7b5792e5e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T16:45:57.860Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XM5ediYSpGoaYa5Z7hMLR8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23fbf0d4-8959-4f35-8c66-9c8b8eb8d06b",
  "isSidechain": false,
  "requestId": "req_011Cb2oLj4DCtPTWbbDJWY3b",
  "type": "assistant",
  "uuid": "b0caf526-ec89-4596-a26a-bf7b5792e5e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PMEDfKvgddkXzYGkN38Ab",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11736,
      "cache_read_input_tokens": 11447,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11736
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context…",
  "leafUuid": "ab116609-f6c0-4b6c-8577-5063fe0e82c0",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper with experimental data",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3"
}
```

---

### Assistant

_source line 15 · 2026-05-14T16:46:09.504Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me write the full LaTeX paper. I need to:

1. Cover all 13 experiments from the JSON
2. Follow the paper framing
3. Use the narrative guidance
4. Write a complete LaTeX document

Let me organize the paper structure:

- Abstract
- Introduction (correct CoCoHaNeRe misconception, introduce StructFuse)
- Related Work
- Method (negative mining strategies, CodeQL pipeline, contrastive training)
- Experiments
  - Setup
  - Main Results (Table 3: 4-strategy comparison with BM25)
  - SWE-bench Lite and RepoBench-R evaluations (Tables 4-5)
  - Stratified analysis across different code types (Table 7)
  - Ablation studies examining temperature, hop depth, data scaling, fusion head design, pool size sensitivity, mining strategies, and weighting schemes (Tables 8-13 and S1)
  - Failure cases and literature comparisons (Tables S2-S3)
- Discussion
- Conclusion

Now I'm ready to draft the full paper with sufficient depth for publication.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab116609-f6c0-4b6c-8577-5063fe0e82c0",
  "isSidechain": false,
  "requestId": "req_011Cb2oMBzwrcJsHHhh9chRU",
  "type": "assistant",
  "uuid": "883f8b64-3926-4170-9093-c03bc279a120",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeGPAHksDeXhNYz8FL4VQv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21299,
      "cache_read_input_tokens": 23183,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21299,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 23183,
          "cache_creation_input_tokens": 21299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21299
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

_source line 16 · 2026-05-14T16:46:09.506Z_

Now I'll write the full LaTeX paper and compile it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "883f8b64-3926-4170-9093-c03bc279a120",
  "isSidechain": false,
  "requestId": "req_011Cb2oMBzwrcJsHHhh9chRU",
  "type": "assistant",
  "uuid": "93cc449d-ec02-4f3b-9266-e2491b3375de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeGPAHksDeXhNYz8FL4VQv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21299,
      "cache_read_input_tokens": 23183,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21299,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 23183,
          "cache_creation_input_tokens": 21299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21299
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

_source line 17 · 2026-05-14T16:46:11.396Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gf8qKUsf2K1gQVTmiUGAwe`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93cc449d-ec02-4f3b-9266-e2491b3375de",
  "isSidechain": false,
  "requestId": "req_011Cb2oMBzwrcJsHHhh9chRU",
  "type": "assistant",
  "uuid": "c065fe40-f30e-4469-8ea2-5b2b5b2e9bdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeGPAHksDeXhNYz8FL4VQv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21299,
      "cache_read_input_tokens": 23183,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21299,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 23183,
          "cache_creation_input_tokens": 21299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21299
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

_source line 18 · 2026-05-14T16:46:11.574Z_

<details><summary>↩ Tool result · `toolu_01Gf8qKUsf2K1gQVTmiUGAwe`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c065fe40-f30e-4469-8ea2-5b2b5b2e9bdf",
  "isSidechain": false,
  "promptId": "7dbbfae7-135c-4257-9519-f147e9c1c35b",
  "type": "user",
  "uuid": "ba7a3402-79e2-4b9c-83b2-9e440c2058f0",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "c065fe40-f30e-4469-8ea2-5b2b5b2e9bdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T16:49:49.128Z_

<details open><summary>🔧 Tool call — Write · `toolu_01WToSKQdqS8BoP8iq8HP3Uf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\n\\title{What Makes Hard Negatives Work for Code Retrieval?\\\\A Systematic Study of Mining Strategies and Representation Geometry}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nHard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\nPrior work (CoCoHaNeRe) reports that embedding-distance hard negatives \\emph{harm} code retrieval, but this finding was derived from BM25-proxy negatives mislabeled as embedding-distance.\nWe present a controlled comparison of four negative mining strategies---random, BM25, true embedding-distance, and structure-grounded (dataflow)---for contrastive code retrieval across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with 9 seeds each.\nOur results show that (1)~true embedding-distance mining \\emph{consistently improves} retrieval over random baselines (+2.0pp R@1 Qwen, +1.5pp StarCoder), correcting the prior misconception;\n(2)~BM25 negatives \\emph{harm} both encoders ($-$2.5pp, $-$2.7pp), confirming the artifact;\nand (3)~structure-grounded negatives via inter-procedural dataflow provide conditional additional benefit (+1.0pp Qwen) when encoder representations are saturated, but not when the representation space has healthy separation (StarCoder).\nWe provide mechanistic explanation via representation geometry analysis: negative difficulty scales monotonically with improvement (Q4 hardest quartile: +3.2pp vs Q1: +0.8pp).\nDownstream, embedding mining improves SWE-bench Lite resolve rate by +2.5pp ($p=0.018$) and dataflow by +3.2pp ($p=0.008$).\nStrategy rankings are stable across temperatures ($\\tau \\in \\{0.05, 0.1, 0.2\\}$), pool sizes (50--500), and data scales (1K--5K), establishing robust practical guidance.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nRepository-level code repair requires selecting relevant files from large codebases given a natural-language issue description.\nContrastive learning with hard negative mining is the dominant paradigm for training dense retrievers in this setting.\nThe quality of negatives directly determines representation quality: too-easy negatives waste gradient signal, while poorly chosen ``hard'' negatives can introduce noise.\n\nDespite its importance, the field lacks systematic understanding of what negative mining strategies work for code retrieval.\nThe most relevant prior study, CoCoHaNeRe, reports that embedding-distance hard negatives \\emph{harm} code search performance by $-$27pp R@1.\nThis finding has influenced subsequent work to avoid embedding-based mining for code.\nHowever, we identify that CoCoHaNeRe used BM25-based retrieval as a proxy for embedding distance---a critical methodological conflation, as BM25 selects lexically similar negatives that destroy useful token-overlap signals during contrastive training.\n\nWe present StructFuse, a systematic study comparing four negative mining strategies: random, BM25, true embedding-distance, and structure-grounded (dataflow) negatives derived from inter-procedural call-graph analysis via CodeQL.\nOur study spans two decoder-only code encoders with distinct pretraining objectives and representation geometries, 9 random seeds per configuration, and evaluation on both SWE-smith file retrieval and SWE-bench Lite end-to-end repair.\n\nOur contributions are threefold:\n\n\\begin{enumerate}\n\\item We \\textbf{correct the misconception} that embedding-distance hard negatives harm code retrieval.\nTrue embedding mining yields +1.6--2.0pp R@1 across two encoders, while BM25 negatives reproduce the reported harm ($-$2.5 to $-$2.7pp).\nThe ordering BM25 $<$ random $<$ dataflow $\\leq$ embedding constitutes a quality spectrum for negative mining strategies.\n\n\\item We introduce \\textbf{structure-grounded negatives} via inter-procedural dataflow and characterize when they provide additional benefit.\nWhen pretrained encoder representations are saturated (pos\\_sim $>$ 0.98, Qwen), dataflow negatives provide +1.0pp beyond random.\nWhen representation space has healthy separation (pos\\_sim $\\sim$ 0.80, StarCoder), embedding mining alone suffices.\nStratified analysis reveals the true per-instance dataflow effect is +2.8pp on instances with structural data, diluted to +1.0pp overall by the 66\\% fallback stratum.\n\n\\item We provide \\textbf{mechanistic explanation} via representation geometry analysis.\nNegative difficulty quartile analysis shows monotonically increasing benefit: Q4 (hardest) yields +3.2pp vs Q1 (easiest) at +0.8pp.\nThis encoder-strategy interaction explains contradictory findings in prior work and enables practitioners to predict which strategy suits their encoder.\n\\end{enumerate}\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Code Retrieval for Software Engineering.}\nDense retrieval has become the dominant paradigm for repository-level code search.\nSweRank~and SWE-Fixer train contrastive retrievers on issue-file pairs mined from GitHub, achieving strong results on SWE-bench.\nThese methods rely on text-based similarity alone, ignoring structural dependencies between code files.\n\n\\paragraph{Hard Negative Mining.}\nIn general dense retrieval, hard negative mining is well-studied.\nANCE proposes asynchronous index refresh for dynamic mining.\nCurriculum-based approaches gradually increase negative difficulty.\nFor code, CoCoHaNeRe reports that embedding-distance negatives harm code search, recommending against their use.\nWe show this conclusion stems from a BM25-proxy artifact.\n\n\\paragraph{Graph-Based Code Understanding.}\nSeveral methods leverage code structure at inference time.\nCodexGraph builds a code graph database for LLM navigation.\nLocAgent uses repository structure trees for fault localization.\nRANGER employs call graphs for code navigation.\nARISE uses intra-procedural dataflow for code understanding.\nGraphCodeBERT incorporates data flow into pretraining objectives.\nAll operate at inference time; StructFuse is the first to inject structural signal via training-time negative mining, making it complementary to these approaches (Table~\\ref{tab:lit_comparison}).\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Problem Setup}\n\nGiven a natural-language issue description $q$ and a repository with files $\\mathcal{F} = \\{f_1, \\ldots, f_n\\}$, the retriever scores each file $s(q, f_i)$ and returns the top-$k$ files.\nWe train a bi-encoder using InfoNCE contrastive loss with temperature $\\tau$:\n\\begin{equation}\n\\mathcal{L} = -\\log \\frac{\\exp(s(q, f^+)/\\tau)}{\\exp(s(q, f^+)/\\tau) + \\sum_{j=1}^{K} \\exp(s(q, f_j^-)/\\tau)}\n\\end{equation}\nwhere $f^+$ is the gold file and $\\{f_j^-\\}_{j=1}^K$ are negative files.\nThe choice of how to select negatives is the focus of this study.\n\n\\subsection{Negative Mining Strategies}\n\nWe compare four strategies for selecting $\\{f_j^-\\}$:\n\n\\paragraph{Random.}\nSample uniformly from $\\mathcal{F} \\setminus \\{f^+\\}$.\nThis is the standard baseline in contrastive learning.\n\n\\paragraph{BM25.}\nSelect the top-scoring BM25 results for query $q$ that are not $f^+$.\nBM25 negatives have high lexical overlap with the query.\n\n\\paragraph{Embedding-distance.}\nUsing the pretrained encoder, compute embeddings for all files and select the nearest neighbors of $q$ (excluding $f^+$) as negatives.\nThese are semantically similar but non-relevant files.\nMining is performed once using the pretrained checkpoint (static mining).\n\n\\paragraph{Dataflow (structure-grounded).}\nUsing inter-procedural call-graph analysis, we define:\n\\begin{equation}\nf^-_{\\text{struct}} = \\arg\\max_{f \\in \\mathcal{F}: s(f,q) > \\tau_{\\text{sim}} \\;\\wedge\\; \\neg\\text{reachable}_G(f, f^+)} s(f, q)\n\\end{equation}\nwhere $G$ is the 2-hop call graph extracted via CodeQL.\nDataflow negatives are semantically similar to the query \\emph{and} structurally disconnected from the gold file---they are textually confusable but functionally unrelated.\nWhen structural data is unavailable (66\\% of instances), we fall back to embedding-distance mining.\n\n\\subsection{Structural Extraction via CodeQL}\n\nWe extract inter-procedural call graphs from Python repositories using CodeQL.\nFor each repository, we build a CodeQL database and query for function-level call relationships, yielding a directed graph where nodes are functions and edges represent caller--callee relationships.\nFile-level connectivity is derived by projecting function-level edges: two files are connected if any function in one calls any function in the other within 2 hops.\n\nAt scale (5K training instances, 131 repositories), the pipeline achieves 0\\% timeout rate, with 123/131 repositories successfully processed.\n78\\% of extracted file pairs are connected-but-not-gold, providing a rich pool of structurally-informed negatives.\nStructural data is available for 34\\% of query--positive pairs.\n\n\\subsection{Hop Depth Selection}\n\nWe ablate the hop depth parameter for call-graph bounding (Section~\\ref{sec:hop_ablation}).\n2-hop is optimal: 1-hop provides only 12.4\\% coverage (too sparse for meaningful ``disconnected'' definition), while 3-hop reaches 58.6\\% coverage where the disconnected set becomes too narrow and noisy.\n2-hop achieves 34.3\\% coverage with a principled semantic boundary: direct callers/callees and their immediate neighbors.\n\n\\subsection{Training Details}\n\nWe fine-tune two decoder-only code encoders with LoRA (rank 16): Qwen2.5-Coder-3B and StarCoder2-3B.\nTraining uses 5K instances from SWE-smith with InfoNCE loss at $\\tau = 0.1$.\nEach configuration is trained with 9 random seeds for statistical robustness.\nAll mining is static (computed once from pretrained checkpoints).\n\n%==============================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n%==============================================================================\n\n\\subsection{Evaluation Setup}\n\n\\paragraph{SWE-smith.}\nFile-level retrieval on SWE-smith validation split ($\\sim$15.2K instances).\nPrimary metric: R@1 with pool size 50 (default).\nWe report mean and 95\\% bootstrap confidence intervals across 9 seeds.\n\n\\paragraph{SWE-bench Lite.}\nEnd-to-end evaluation on 300 SWE-bench Lite instances.\nThe retriever provides top-5 context files to a Qwen3.6-27B agent that generates patches.\nMetric: resolve rate (percentage of correctly patched instances).\n\n\\paragraph{RepoBench-R.}\nCross-file code completion retrieval on RepoBench-R test\\_hard (pool $\\approx$ 18) and test\\_easy (pool $\\approx$ 6).\n\n%------------------------------------------------------------------------------\n\\subsection{Main Results: Four-Strategy Comparison}\n\\label{sec:main_results}\n%------------------------------------------------------------------------------\n\nTable~\\ref{tab:main_4strategy} presents the full four-strategy comparison on SWE-smith validation.\nThe ordering is consistent across both encoders: BM25 $<$ random $<$ dataflow $\\leq$ embedding.\n\n\\begin{table}[h]\n\\centering\n\\caption{Full four-strategy comparison on SWE-smith validation (R@1 \\%, pool=50, 9-seed mean $\\pm$ 95\\% CI). BM25 negatives harm both encoders, confirming the CoCoHaNeRe artifact. True embedding mining consistently improves over random.}\n\\label{tab:main_4strategy}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Strategy} & \\textbf{R@1 (\\%)} & \\textbf{95\\% CI} & \\textbf{$\\Delta$ vs Random (pp)} \\\\\n\\midrule\nQwen & BM25 & 52.0 & [51.2, 52.8] & $-$2.5 \\\\\nQwen & random & 54.5 & [53.8, 55.2] & --- \\\\\nQwen & dataflow & 55.5 & [54.6, 56.4] & +1.0 \\\\\nQwen & embedding & 56.5 & [55.8, 57.2] & +2.0 \\\\\n\\midrule\nStarCoder & BM25 & 43.3 & [42.3, 44.3] & $-$2.7 \\\\\nStarCoder & random & 46.0 & [45.1, 46.9] & --- \\\\\nStarCoder & dataflow & 45.8 & [44.8, 46.8] & $-$0.2 \\\\\nStarCoder & embedding & 47.5 & [46.6, 48.4] & +1.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBM25 negatives harm performance for both encoders ($-$2.5pp Qwen, $-$2.7pp StarCoder vs random).\nBM25 selects lexically similar files that share function names, variable names, and import patterns with the query.\nThese are precisely the signals that contrastive learning should leverage for discrimination; training the encoder to ignore them degrades retrieval.\n\nTrue embedding-distance mining improves both encoders (+2.0pp Qwen, +1.5pp StarCoder), selecting files that are semantically similar in the pretrained embedding space but not relevant to the query.\nThis forces the encoder to learn finer-grained semantic distinctions.\n\nDataflow negatives benefit Qwen (+1.0pp, CI lower bound $>$ 0) but not StarCoder ($-$0.2pp, CI includes zero).\nSection~\\ref{sec:stratified} provides mechanistic explanation for this interaction.\n\n%------------------------------------------------------------------------------\n\\subsection{SWE-bench Lite End-to-End Evaluation}\n\\label{sec:swebench}\n%------------------------------------------------------------------------------\n\n\\begin{table}[h]\n\\centering\n\\caption{SWE-bench Lite resolve rate (300 instances, Qwen3.6-27B agent, top-5 retrieval).}\n\\label{tab:swebench}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Resolved} & \\textbf{Total} & \\textbf{Rate (\\%)} & \\textbf{$\\Delta$ vs Random (pp)} \\\\\n\\midrule\nrandom & 66 & 300 & 22.0 & --- \\\\\nembedding & 73 & 300 & 24.3 & +2.3 \\\\\ndataflow & 76 & 300 & 25.3 & +3.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRetrieval quality improvements amplify at the downstream task level.\nEmbedding mining yields +2.5pp resolve rate ($p = 0.018$, 95\\% CI [+0.7, +4.3]), and dataflow yields +3.2pp ($p = 0.008$, CI [+1.0, +5.5]) over random (Table~\\ref{tab:swebench_bootstrap}).\nThe difference between dataflow and embedding is +0.7pp but not significant ($p = 0.134$, CI [$-$1.5, +2.9]).\n\n\\begin{table}[h]\n\\centering\n\\caption{Bootstrap significance tests for SWE-bench Lite (10K resamples).}\n\\label{tab:swebench_bootstrap}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} & \\textbf{$p$-value} \\\\\n\\midrule\nembedding $-$ random & +2.5 & [+0.7, +4.3] & 0.018 \\\\\ndataflow $-$ random & +3.2 & [+1.0, +5.5] & 0.008 \\\\\ndataflow $-$ embedding & +0.7 & [$-$1.5, +2.9] & 0.134 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Breakdown by Patch Complexity.}\nMulti-file patches (37\\% of instances) are the primary source of dataflow advantage: dataflow achieves +5.4pp over random on multi-file patches (17.1\\% vs 11.7\\%) compared to +2.2pp on single-file patches (30.2\\% vs 28.0\\%).\nThis is consistent with the mechanism: dataflow negatives train the retriever to understand cross-module dependencies, which matters most when the gold patch spans multiple files.\n\n\\begin{table}[h]\n\\centering\n\\caption{SWE-bench resolve rate by patch complexity.}\n\\label{tab:swebench_complexity}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Patch Type} & \\textbf{N} & \\textbf{random (\\%)} & \\textbf{embedding (\\%)} & \\textbf{dataflow (\\%)} \\\\\n\\midrule\nsingle-file & 189 & 28.0 & 30.7 & 30.2 \\\\\nmulti-file & 111 & 11.7 & 14.4 & 17.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------------------\n\\subsection{RepoBench-R Cross-File Retrieval}\n\\label{sec:repobench}\n%------------------------------------------------------------------------------\n\nTable~\\ref{tab:repobench} shows results on RepoBench-R test\\_hard (pool $\\approx$ 18).\nEmbedding mining significantly improves R@1 for both encoders (+2.1pp Qwen, +1.5pp StarCoder), confirming cross-benchmark generalization.\nDataflow provides +1.2pp for Qwen (CI marginally excludes zero) but is ineffective for StarCoder ($-$0.2pp, CI includes zero)---the same encoder-strategy interaction observed on SWE-smith.\n\n\\begin{table}[h]\n\\centering\n\\caption{RepoBench-R test\\_hard results (pool $\\approx$ 18, 9-seed mean $\\pm$ 95\\% CI).}\n\\label{tab:repobench}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Strategy} & \\textbf{R@1 (\\%)} & \\textbf{95\\% CI} & \\textbf{$\\Delta$ vs Random (pp)} \\\\\n\\midrule\nQwen & random & 62.1 & [61.4, 62.8] & --- \\\\\nQwen & embedding & 64.2 & [63.4, 65.0] & +2.1 \\\\\nQwen & dataflow & 63.3 & [62.4, 64.2] & +1.2 \\\\\n\\midrule\nStarCoder & random & 57.4 & [56.6, 58.2] & --- \\\\\nStarCoder & embedding & 58.9 & [58.0, 59.8] & +1.5 \\\\\nStarCoder & dataflow & 57.2 & [56.2, 58.2] & $-$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn test\\_easy (pool $\\approx$ 6), deltas are compressed due to ceiling effects: Qwen embedding +1.2pp (84.3\\% $\\to$ 85.5\\%), StarCoder embedding +1.0pp (81.2\\% $\\to$ 82.2\\%).\nThis is expected---smaller pools leave fewer distractors for mining quality to differentiate.\n\n%------------------------------------------------------------------------------\n\\subsection{Stratified Analysis}\n\\label{sec:stratified}\n%------------------------------------------------------------------------------\n\n\\paragraph{Structural Data Availability.}\nTable~\\ref{tab:stratified_structural} decomposes dataflow performance by whether structural data was available for each instance.\nOn the 34\\% of instances with dataflow connectivity, the dataflow advantage is +2.8pp (Qwen)---substantially larger than the pooled +1.0pp.\nOn the 66\\% fallback stratum where dataflow degrades to embedding or random selection, the advantage is +0.1pp (effectively zero).\nThis decomposition directly addresses the concern that 34\\% coverage dilutes the signal: the true per-instance effect is +2.8pp, not +1.0pp.\n\n\\begin{table}[h]\n\\centering\n\\caption{Stratified R@1 delta by structural data availability (Qwen encoder).}\n\\label{tab:stratified_structural}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Stratum} & \\textbf{N} & \\textbf{random} & \\textbf{embedding} & \\textbf{dataflow} & \\textbf{df$-$rand (pp)} \\\\\n\\midrule\nWith dataflow (34\\%) & $\\sim$5.2K & 53.1 & 55.4 & 55.9 & +2.8 \\\\\nFallback (66\\%) & $\\sim$10K & 55.2 & 57.3 & 55.3 & +0.1 \\\\\n\\midrule\nOverall & $\\sim$15.2K & 54.5 & 56.5 & 55.5 & +1.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Negative Difficulty Quartiles.}\nTable~\\ref{tab:neg_difficulty} presents the strongest mechanistic evidence.\nWe partition instances by negative difficulty (margin between positive and hardest negative similarity).\nThe benefit of mining strategies scales monotonically with difficulty: Q4 (hardest, margin 0.008) shows +3.2pp embedding delta, while Q1 (easiest, margin 0.142) shows only +0.8pp.\nThis confirms the representation saturation hypothesis: when random negatives are already easy to distinguish (large margin), better mining adds little; when the margin is thin, mining quality is critical.\n\n\\begin{table}[h]\n\\centering\n\\caption{R@1 delta by negative difficulty quartile (Qwen encoder).}\n\\label{tab:neg_difficulty}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Quartile} & \\textbf{Margin (mean)} & \\textbf{emb$-$rand (pp)} & \\textbf{df$-$rand (pp)} \\\\\n\\midrule\nQ1 (easiest) & 0.142 & +0.8 & +0.3 \\\\\nQ2 & 0.078 & +1.5 & +0.7 \\\\\nQ3 & 0.031 & +2.4 & +1.2 \\\\\nQ4 (hardest) & 0.008 & +3.2 & +2.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Repo Size and Pool Size Strata.}\nEmbedding delta is inversely related to repository size: small repos ($<$50 files) show +2.8pp, while extra-large repos ($>$500 files) show +1.6pp.\nPool size strata show a complementary pattern: embedding delta increases from +1.0pp (pool $<$ 20) to +2.5pp (pool $>$ 50), as larger pools provide more distractors where mining quality matters.\n\n\\paragraph{Query--Positive Similarity.}\nWhen query-positive similarity is high ($>$0.95), embedding delta is largest (+2.6pp) and dataflow delta is also substantial (+1.8pp).\nAt low similarity ($<$0.85), both deltas shrink (+1.2pp embedding, +0.2pp dataflow).\nHigh-similarity instances are precisely those where the retriever struggles to separate the positive from near-duplicates, making negative quality most impactful.\n\n%------------------------------------------------------------------------------\n\\subsection{Ablation Studies}\n\\label{sec:ablations}\n%------------------------------------------------------------------------------\n\n\\subsubsection{Temperature Ablation}\n\\label{sec:temp_ablation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature ablation (R@1 \\%). Strategy rankings are preserved across all three temperatures.}\n\\label{tab:temperature}\n\\begin{tabular}{clcccc}\n\\toprule\n$\\tau$ & \\textbf{Encoder} & \\textbf{random} & \\textbf{embedding} & \\textbf{dataflow} & \\textbf{emb$-$rand (pp)} \\\\\n\\midrule\n0.05 & Qwen & 55.8 & 57.7 & 56.9 & +1.9 \\\\\n0.05 & StarCoder & 47.0 & 48.5 & 46.7 & +1.5 \\\\\n0.10 & Qwen & 54.5 & 56.5 & 55.5 & +2.0 \\\\\n0.10 & StarCoder & 46.0 & 47.5 & 45.8 & +1.5 \\\\\n0.20 & Qwen & 53.0 & 54.6 & 53.8 & +1.6 \\\\\n0.20 & StarCoder & 44.8 & 46.1 & 44.7 & +1.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStrategy rankings (embedding $>$ dataflow $>$ random for Qwen; embedding $>$ random $\\approx$ dataflow for StarCoder) are preserved across all three temperatures (Table~\\ref{tab:temperature}).\n$\\tau = 0.05$ achieves the highest absolute performance due to sharper gradient signals.\n$\\tau = 0.20$ compresses deltas (1.6pp vs 2.0pp) but does not reverse rankings, confirming findings are not temperature-regime-specific.\nWe use $\\tau = 0.1$ as the default, following literature convention.\n\n\\subsubsection{Call-Graph Hop Depth Ablation}\n\\label{sec:hop_ablation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Hop depth ablation for dataflow negatives (Qwen encoder).}\n\\label{tab:hop_depth}\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Hops} & \\textbf{Coverage (\\%)} & \\textbf{Neg/query} & \\textbf{R@1 (\\%)} & \\textbf{$\\Delta$ vs 2-hop (pp)} \\\\\n\\midrule\n1 & 12.4 & 18.2 & 54.8 & $-$0.7 \\\\\n2 & 34.3 & 31.7 & 55.5 & --- \\\\\n3 & 58.6 & 42.1 & 55.1 & $-$0.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n2-hop call-graph bounding is optimal (Table~\\ref{tab:hop_depth}).\n1-hop is too conservative: only 12.4\\% coverage means most instances lack sufficient connected nodes to define meaningful ``disconnected'' negatives.\n3-hop is too permissive: 58.6\\% coverage narrows the disconnected set excessively, excluding structurally related files that would serve as good negatives.\n2-hop captures direct callers/callees and their immediate neighbors, providing a principled boundary at 34.3\\% coverage.\n\n\\subsubsection{Training Data Size Scaling}\n\\label{sec:data_scaling}\n\n\\begin{table}[h]\n\\centering\n\\caption{Data size scaling (Qwen encoder). Strategy rankings and monotonic improvement are stable across scales.}\n\\label{tab:data_scaling}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Size} & \\textbf{random} & \\textbf{embedding} & \\textbf{dataflow} & \\textbf{emb$-$rand (pp)} & $\\sigma$ \\textbf{seeds} \\\\\n\\midrule\n1K & 51.0 & 52.2 & 51.5 & +1.2 & 1.5 \\\\\n3K & 53.2 & 55.0 & 54.1 & +1.8 & 1.0 \\\\\n5K & 54.5 & 56.5 & 55.5 & +2.0 & 0.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStrategy ranking (embedding $>$ dataflow $>$ random) is preserved across 1K, 3K, and 5K training instances (Table~\\ref{tab:data_scaling}).\nThe embedding--random delta grows from +1.2pp at 1K to +2.0pp at 5K, with no sign of diminishing returns.\nSeed variance decreases from $\\sigma = 1.5$ at 1K to $\\sigma = 0.8$ at 5K as larger datasets reduce sampling noise.\n\n\\subsubsection{Fusion Head Ablation}\n\\label{sec:fusion_ablation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Fusion head ablation: training-time mining vs inference-time feature injection.}\n\\label{tab:fusion}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Configuration} & \\textbf{Qwen R@1 (\\%)} & \\textbf{StarCoder R@1 (\\%)} \\\\\n\\midrule\nembedding-only (ours) & 56.5 & 47.5 \\\\\nstructural-features-only & 49.8 & 42.1 \\\\\ncombined fusion & 56.1 & 47.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:fusion} isolates the value of training-time mining versus inference-time structural feature injection.\nEmbedding-only (our approach: mine negatives during training, no structural features at inference) performs best or ties with combined fusion.\nStructural-features-only (no mining, inject CodeQL connectivity features at inference) is far worse ($-$6.7pp Qwen).\nCombined fusion slightly underperforms embedding-only ($-$0.4pp) because inference-time structural features introduce noise from the 66\\% of instances without CodeQL coverage.\nThe core value of StructFuse is in the \\emph{mining strategy}, not in feature engineering.\n\n\\subsubsection{Pool Size Sensitivity}\n\\label{sec:pool_sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\caption{Pool size sensitivity (R@1 \\%). Strategy rankings are 100\\% stable across pool sizes spanning an order of magnitude.}\n\\label{tab:pool_size}\n\\begin{tabular}{clccccc}\n\\toprule\n\\textbf{Pool} & \\textbf{Encoder} & \\textbf{random} & \\textbf{embedding} & \\textbf{dataflow} & \\textbf{emb$-$rand (pp)} & \\textbf{Ranking} \\\\\n\\midrule\n50 & Qwen & 54.5 & 56.5 & 55.5 & +2.0 & E$>$D$>$R \\\\\n100 & Qwen & 42.8 & 44.7 & 43.8 & +1.9 & E$>$D$>$R \\\\\n200 & Qwen & 34.2 & 35.9 & 35.1 & +1.7 & E$>$D$>$R \\\\\n500 & Qwen & 26.1 & 27.6 & 26.9 & +1.5 & E$>$D$>$R \\\\\n\\midrule\n50 & StarCoder & 46.0 & 47.5 & 45.8 & +1.5 & E$>$R$>$D \\\\\n100 & StarCoder & 35.8 & 37.2 & 35.7 & +1.4 & E$>$R$>$D \\\\\n200 & StarCoder & 28.2 & 29.5 & 28.1 & +1.3 & E$>$R$\\approx$D \\\\\n500 & StarCoder & 21.4 & 22.5 & 21.3 & +1.1 & E$>$R$\\approx$D \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStrategy rankings are 100\\% stable across pool sizes from 50 to 500 (Table~\\ref{tab:pool_size}).\nAbsolute R@1 drops as expected with larger pools, and the embedding--random delta degrades gracefully from 2.0pp to 1.5pp (Qwen) and 1.5pp to 1.1pp (StarCoder) at approximately $-$0.15pp per pool-size doubling.\nThe delta does not collapse, confirming the mining strategy's value is not an artifact of small pool sizes.\n\n\\subsubsection{Dynamic vs Static Embedding Mining}\n\\label{sec:dynamic_mining}\n\n\\begin{table}[h]\n\\centering\n\\caption{Static vs dynamic embedding mining. Static mining (one-time, from pretrained) is sufficient.}\n\\label{tab:dynamic}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Static R@1 (\\%)} & \\textbf{Dynamic R@1 (\\%)} & \\textbf{$\\Delta$ (pp)} & $p$\\textbf{-value} \\\\\n\\midrule\nQwen & 56.5 & 56.8 & +0.3 & 0.41 \\\\\nStarCoder & 47.5 & 47.7 & +0.2 & 0.53 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDynamic mining (re-computing negatives each epoch using the current encoder) provides negligible improvement over static mining (+0.3pp Qwen, +0.2pp StarCoder, both non-significant; Table~\\ref{tab:dynamic}).\nLoRA rank-16 fine-tuning changes the embedding space only slightly, so pretrained nearest neighbors remain valid throughout training.\nThis rules out the curriculum-effect confound and simplifies the practical recommendation: mine once from the pretrained checkpoint.\n\n\\subsubsection{Weighted vs Binary Dataflow Negatives}\n\\label{sec:weighted}\n\n\\begin{table}[h]\n\\centering\n\\caption{Weighted (by hop distance) vs binary dataflow negatives. Binary is sufficient.}\n\\label{tab:weighted}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Qwen R@1 (\\%)} & \\textbf{StarCoder R@1 (\\%)} & \\textbf{$\\Delta$ vs Binary (pp)} \\\\\n\\midrule\nBinary (default) & 55.5 & 45.8 & --- \\\\\nDistance-weighted & 55.8 & 45.9 & +0.3 / +0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWeighting dataflow negatives by hop distance (farther = higher sampling probability) provides no significant improvement over binary connected/disconnected classification (+0.3pp Qwen, +0.1pp StarCoder; Table~\\ref{tab:weighted}).\nThe binary signal---``on the call chain or not''---captures the essential structural distinction.\nFurther distance-based refinement adds complexity without benefit.\n\n%------------------------------------------------------------------------------\n\\subsection{Failure Analysis}\n\\label{sec:failure}\n%------------------------------------------------------------------------------\n\nWe manually analyzed 50 failure cases from the random retriever on SWE-bench Lite (Table~\\ref{tab:failure}).\n44\\% (22/50) are retrieval failures (wrong files retrieved), of which 64\\% (14/22) involve cross-module dependencies where the gold file is a caller/callee of a retrieved-but-wrong file.\nThese are precisely the cases dataflow training targets.\n30\\% (15/50) are retrieval successes where the agent fails to generate correct patches, establishing a ceiling: even with perfect retrieval, $\\sim$85\\% is the maximum achievable resolve rate given agent limitations.\n\n\\begin{table}[h]\n\\centering\n\\caption{Failure category breakdown (50 random-retriever failures from SWE-bench Lite).}\n\\label{tab:failure}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Category} & \\textbf{Count} & \\textbf{\\% of 50} & \\textbf{Dataflow Could Help?} \\\\\n\\midrule\nRetrieval: wrong files & 22 & 44\\% & 14/22 (64\\%) \\\\\nRetrieval OK, agent fail & 15 & 30\\% & N/A \\\\\nContext window limit & 7 & 14\\% & 5/7 partially \\\\\nTest env issue & 4 & 8\\% & No \\\\\nAmbiguous issue & 2 & 4\\% & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Illustrative Example.}\nConsider a Django issue about \\texttt{QuerySet.filter()} returning wrong results with nested Q objects.\nThe random retriever ranks \\texttt{django/db/models/query.py} first (text match on ``filter''), but the bug resides in \\texttt{django/db/models/sql/query.py} (the downstream SQL builder invoked by \\texttt{filter}).\nThe dataflow-trained retriever correctly ranks the SQL builder file higher, having learned that structurally connected files along the call chain are more likely to co-occur in patches.\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Why Does the Encoder--Strategy Interaction Exist?}\nQwen2.5-Coder-3B exhibits representation saturation (mean pos\\_sim = 0.9855), compressing positive and negative embeddings into a narrow similarity band.\nRandom negatives are trivially separable and provide weak gradient signal.\nEmbedding mining selects negatives that are genuinely close in this compressed space, providing the difficulty gradient the encoder needs.\nDataflow negatives add an orthogonal structural dimension that further assists discrimination.\n\nStarCoder2-3B has healthier separation (mean pos\\_sim = 0.7985).\nRandom negatives already provide moderate difficulty, and embedding mining further refines the boundary.\nDataflow negatives offer no additional benefit because the embedding space is not saturated---the encoder can already separate structural from textual similarity using learned features alone.\n\n\\paragraph{Relationship to Inference-Time Graph Methods.}\nStructFuse operates at training time, distilling structural knowledge into encoder representations via negative mining.\nInference-time graph methods (CodexGraph, LocAgent, RANGER, ARISE, and others; Table~\\ref{tab:lit_comparison}) navigate or re-rank over code graphs at inference time.\nThe two approaches are complementary: StructFuse produces a better base retriever that graph-based methods can navigate over.\nWe do not claim superiority over these methods, as they solve different problems and operate under different computational budgets.\n\n\\begin{table}[h]\n\\centering\n\\caption{Comparison with inference-time graph methods. StructFuse is the only method that leverages structural signal at training time without inference-time overhead.}\n\\label{tab:lit_comparison}\n\\begin{tabular}{llll}\n\\toprule\n\\textbf{Method} & \\textbf{Graph Stage} & \\textbf{Graph Type} & \\textbf{Complementary?} \\\\\n\\midrule\nStructFuse (ours) & Training & Dataflow (CodeQL) & --- \\\\\nCodexGraph & Inference & Code graph DB & Yes \\\\\nLocAgent & Inference & Repo structure & Yes \\\\\nRANGER & Inference & Call graph & Yes \\\\\nARISE & Inference & Intra-proc dataflow & Partially \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Practical Recommendations.}\nBased on our findings: (1) Always use true embedding-distance mining over random negatives---the improvement is consistent across encoders, benchmarks, temperatures, pool sizes, and data scales. (2) Never use BM25 negatives for code retrieval contrastive training. (3) Consider dataflow negatives when encoder representations are saturated (check pos\\_sim distribution); static mining suffices. (4) Binary structural signal is sufficient; weighted variants add complexity without benefit.\n\n\\paragraph{Limitations.}\nOur study is limited to two 3B-parameter decoder-only code encoders; generalization to encoder-only architectures (e.g., CodeBERT) and larger models remains to be verified.\nCodeQL structural extraction achieves 34\\% coverage, limiting the effective reach of dataflow negatives.\nSWE-bench Lite evaluation uses 300 instances with a single agent model, providing limited statistical power for pairwise comparisons between mining strategies.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe presented a systematic study of hard negative mining strategies for contrastive code retrieval.\nOur controlled comparison of four strategies---BM25, random, dataflow, and embedding-distance---across two encoders, three benchmarks, and extensive ablations establishes three findings:\n(1)~True embedding-distance mining consistently improves code retrieval, correcting the prior misconception that embedding negatives are harmful (the reported harm stems from BM25-proxy negatives).\n(2)~Structure-grounded dataflow negatives provide conditional benefit when encoder representations are saturated, with the true per-instance effect (+2.8pp) masked by coverage-driven dilution in pooled results.\n(3)~Negative difficulty quartile analysis provides mechanistic explanation: harder instances benefit more from better negatives (Q4: +3.2pp vs Q1: +0.8pp), linking mining strategy effectiveness to representation geometry.\n\nThese findings transfer to downstream tasks (SWE-bench Lite: +2.5pp embedding, +3.2pp dataflow resolve rate) and are robust across temperatures, pool sizes, data scales, and a second benchmark (RepoBench-R).\nStrategy rankings never reverse across any experimental condition tested.\n\n\\bibliographystyle{plainnat}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba7a3402-79e2-4b9c-83b2-9e440c2058f0",
  "isSidechain": false,
  "requestId": "req_011Cb2oNBuGeke1Yn29zoUbR",
  "type": "assistant",
  "uuid": "419a8e83-32a7-4309-9a71-69a575fed846",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZxNzDEJTrm8SKK7UEayC7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 44482,
      "output_tokens": 11157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11157,
          "cache_read_input_tokens": 44482,
          "cache_creation_input_tokens": 481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 481
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

_source line 20 · 2026-05-14T16:49:49.145Z_

<details><summary>↩ Tool result · `toolu_01WToSKQdqS8BoP8iq8HP3Uf`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "419a8e83-32a7-4309-9a71-69a575fed846",
  "isSidechain": false,
  "promptId": "7dbbfae7-135c-4257-9519-f147e9c1c35b",
  "type": "user",
  "uuid": "a0942bcf-b7ea-4e59-8727-ef23bd20776e",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\n\\title{What Makes Hard Negatives Work for Code Retrieval?\\\\A Systematic Study of Mining Strategies and Representation Geometry}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nHard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\nPrior work (CoCoHaNeRe) reports that embedding-distance hard negatives \\emph{harm} code retrieval, but this finding was derived from BM25-proxy negatives mislabeled as embedding-distance.\nWe present a controlled comparison of four negative mining strategies---random, BM25, true embedding-distance, and structure-grounded (dataflow)---for contrastive code retrieval across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with 9 seeds each.\nOur results show that (1)~true embedding-distance mining \\emph{consistently improves} retrieval over random baselines (+2.0pp R@1 Qwen, +1.5pp StarCoder), correcting the prior misconception;\n(2)~BM25 negatives \\emph{harm} both encoders ($-$2.5pp, $-$2.7pp), confirming the artifact;\nand (3)~structure-grounded negatives via inter-procedural dataflow provide conditional additional benefit (+1.0pp Qwen) when encoder representations are saturated, but not when the representation space has healthy separation (StarCoder).\nWe provide mechanistic explanation via representation geometry analysis: negative difficulty scales monotonically with improvement (Q4 hardest quartile: +3.2pp vs Q1: +0.8pp).\nDownstream, embedding mining improves SWE-bench Lite resolve rate by +2.5pp ($p=0.018$) and dataflow by +3.2pp ($p=0.008$).\nStrategy rankings are stable across temperatures ($\\tau \\in \\{0.05, 0.1, 0.2\\}$), pool sizes (50--500), and data scales (1K--5K), establishing robust practical guidance.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nRepository-level code repair requires selecting relevant files from large codebases given a natural-language issue description.\nContrastive learning with hard negative mining is the dominant paradigm for training dense retrievers in this setting.\nThe quality of negatives directly determines representation quality: too-easy negatives waste gradient signal, while poorly chosen ``hard'' negatives can introduce noise.\n\nDespite its importance, the field lacks systematic understanding of what negative mining strategies work for code retrieval.\nThe most relevant prior study, CoCoHaNeRe, reports that embedding-distance hard negatives \\emph{harm} code search performance by $-$27pp R@1.\nThis finding has influenced subsequent work to avoid embedding-based mining for code.\nHowever, we identify that CoCoHaNeRe used BM25-based retrieval as a proxy for embedding distance---a critical methodological conflation, as BM25 selects lexically similar negatives that destroy useful token-overlap signals during contrastive training.\n\nWe present StructFuse, a systematic study comparing four negative mining strategies: random, BM25, true embedding-distance, and structure-grounded (dataflow) negatives derived from inter-procedural call-graph analysis via CodeQL.\nOur study spans two decoder-only code encoders with distinct pretraining objectives and representation geometries, 9 random seeds per configuration, and evaluation on both SWE-smith file retrieval and SWE-bench Lite end-to-end repair.\n\nOur contributions are threefold:\n\n\\begin{enumerate}\n\\item We \\textbf{correct the misconception} that embedding-distance hard negatives harm code retrieval.\nTrue embedding mining yields +1.6--2.0pp R@1 across two encoders, while BM25 negatives reproduce the reported harm ($-$2.5 to $-$2.7pp).\nThe ordering BM25 $<$ random $<$ dataflow $\\leq$ embedding constitutes a quality spectrum for negative mining strategies.\n\n\\item We introduce \\textbf{structure-grounded negatives} via inter-procedural dataflow and characterize when they provide additional benefit.\nWhen pretrained encoder representations are saturated (pos\\_sim $>$ 0.98, Qwen), dataflow negatives provide +1.0pp beyond random.\nWhen representation space has healthy separation (pos\\_sim $\\sim$ 0.80, StarCoder), embedding mining alone suffices.\nStratified analysis reveals the true per-instance dataflow effect is +2.8pp on instances with structural data, diluted to +1.0pp overall by the 66\\% fallback stratum.\n\n\\item We provide \\textbf{mechanistic explanation} via representation geometry analysis.\nNegative difficulty quartile analysis shows monotonically increasing benefit: Q4 (hardest) yields +3.2pp vs Q1 (easiest) at +0.8pp.\nThis encoder-strategy interaction explains contradictory findings in prior work and enables practitioners to predict which strategy suits their encoder.\n\\end{enumerate}\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Code Retrieval for Software Engineering.}\nDense retrieval has become the dominant paradigm for repository-level code search.\nSweRank~and SWE-Fixer train contrastive retrievers on issue-file pairs mined from GitHub, achieving strong results on SWE-bench.\nThese methods rely on text-based similarity alone, ignoring structural dependencies between code files.\n\n\\paragraph{Hard Negative Mining.}\nIn general dense retrieval, hard negative mining is well-studied.\nANCE proposes asynchronous index refresh for dynamic mining.\nCurriculum-based approaches gradually increase negative difficulty.\nFor code, CoCoHaNeRe reports that embedding-distance negatives harm code search, recommending against their use.\nWe show this conclusion stems from a BM25-proxy artifact.\n\n\\paragraph{Graph-Based Code Understanding.}\nSeveral methods leverage code structure at inference time.\nCodexGraph builds a code graph database for LLM navigation.\nLocAgent uses repository structure trees for fault localization.\nRANGER employs call graphs for code navigation.\nARISE uses intra-procedural dataflow for code understanding.\nGraphCodeBERT incorporates data flow into pretraining objectives.\nAll operate at inference time; StructFuse is the first to inject structural signal via training-time negative mining, making it complementary to these approaches (Table~\\ref{tab:lit_comparison}).\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Problem Setup}\n\nGiven a natural-language issue description $q$ and a repository with files $\\mathcal{F} = \\{f_1, \\ldots, f_n\\}$, the retriever scores each file $s(q, f_i)$ and returns the top-$k$ files.\nWe train a bi-encoder using InfoNCE contrastive loss with temperature $\\tau$:\n\\begin{equation}\n\\mathcal{L} = -\\log \\frac{\\exp(s(q, f^+)/\\tau)}{\\exp(s(q, f^+)/\\tau) + \\sum_{j=1}^{K} \\exp(s(q, f_j^-)/\\tau)}\n\\end{equation}\nwhere $f^+$ is the gold file and $\\{f_j^-\\}_{j=1}^K$ are negative files.\nThe choice of how to select negatives is the focus of this study.\n\n\\subsection{Negative Mining Strategies}\n\nWe compare four strategies for selecting $\\{f_j^-\\}$:\n\n\\paragraph{Random.}\nSample uniformly from $\\mathcal{F} \\setminus \\{f^+\\}$.\nThis is the standard baseline in contrastive learning.\n\n\\paragraph{BM25.}\nSelect the top-scoring BM25 results for query $q$ that are not $f^+$.\nBM25 negatives have high lexical overlap with the query.\n\n\\paragraph{Embedding-distance.}\nUsing the pretrained encoder, compute embeddings for all files and select the nearest neighbors of $q$ (excluding $f^+$) as negatives.\nThese are semantically similar but non-relevant files.\nMining is performed once using the pretrained checkpoint (static mining).\n\n\\paragraph{Dataflow (structure-grounded).}\nUsing inter-procedural call-graph analysis, we define:\n\\begin{equation}\nf^-_{\\text{struct}} = \\arg\\max_{f \\in \\mathcal{F}: s(f,q) > \\tau_{\\text{sim}} \\;\\wedge\\; \\neg\\text{reachable}_G(f, f^+)} s(f, q)\n\\end{equation}\nwhere $G$ is the 2-hop call graph extracted via CodeQL.\nDataflow negatives are semantically similar to the query \\emph{and} structurally disconnected from the gold file---they are textually confusable but functionally unrelated.\nWhen structural data is unavailable (66\\% of instances), we fall back to embedding-distance mining.\n\n\\subsection{Structural Extraction via CodeQL}\n\nWe extract inter-procedural call graphs from Python repositories using CodeQL.\nFor each repository, we build a CodeQL database and query for function-level call relationships, yielding a directed graph where nodes are functions and edges represent caller--callee relationships.\nFile-level connectivity is derived by projecting function-level edges: two files are connected if any function in one calls any function in the other within 2 hops.\n\nAt scale (5K training instances, 131 repositories), the pipeline achieves 0\\% timeout rate, with 123/131 repositories successfully processed.\n78\\% of extracted file pairs are connected-but-not-gold, providing a rich pool of structurally-informed negatives.\nStructural data is available for 34\\% of query--positive pairs.\n\n\\subsection{Hop Depth Selection}\n\nWe ablate the hop depth parameter for call-graph bounding (Section~\\ref{sec:hop_ablation}).\n2-hop is optimal: 1-hop provides only 12.4\\% coverage (too sparse for meaningful ``disconnected'' definition), while 3-hop reaches 58.6\\% coverage where the disconnected set becomes too narrow and noisy.\n2-hop achieves 34.3\\% coverage with a principled semantic boundary: direct callers/callees and their immediate neighbors.\n\n\\subsection{Training Details}\n\nWe fine-tune two decoder-only code encoders with LoRA (rank 16): Qwen2.5-Coder-3B and StarCoder2-3B.\nTraining uses 5K instances from SWE-smith with InfoNCE loss at $\\tau = 0.1$.\nEach configuration is trained with 9 random seeds for statistical robustness.\nAll mining is static (computed once from pretrained checkpoints).\n\n%==============================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n%==============================================================================\n\n\\subsection{Evaluation Setup}\n\n\\paragraph{SWE-smith.}\nFile-level retrieval on SWE-smith validation split ($\\sim$15.2K instances).\nPrimary metric: R@1 with pool size 50 (default).\nWe report mean and 95\\% bootstrap confidence intervals across 9 seeds.\n\n\\paragraph{SWE-bench Lite.}\nEnd-to-end evaluation on 300 SWE-bench Lite instances.\nThe retriever provides top-5 context files to a Qwen3.6-27B agent that generates patches.\nMetric: resolve rate (percentage of correctly patched instances).\n\n\\paragraph{RepoBench-R.}\nCross-file code completion retrieval on RepoBench-R test\\_hard (pool $\\approx$ 18) and test\\_easy (pool $\\approx$ 6).\n\n%------------------------------------------------------------------------------\n\\subsection{Main Results: Four-Strategy Comparison}\n\\label{sec:main_results}\n%------------------------------------------------------------------------------\n\nTable~\\ref{tab:main_4strategy} presents the full four-strategy comparison on SWE-smith validation.\nThe ordering is consistent across both encoders: BM25 $<$ random $<$ dataflow $\\leq$ embedding.\n\n\\begin{table}[h]\n\\centering\n\\caption{Full four-strategy comparison on SWE-smith validation (R@1 \\%, pool=50, 9-seed mean $\\pm$ 95\\% CI). BM25 negatives harm both encoders, confirming the CoCoHaNeRe artifact. True embedding mining consistently improves over random.}\n\\label{tab:main_4strategy}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Strategy} & \\textbf{R@1 (\\%)} & \\textbf{95\\% CI} & \\textbf{$\\Delta$ vs Random (pp)} \\\\\n\\midrule\nQwen & BM25 & 52.0 & [51.2, 52.8] & $-$2.5 \\\\\nQwen & random & 54.5 & [53.8, 55.2] & --- \\\\\nQwen & dataflow & 55.5 & [54.6, 56.4] & +1.0 \\\\\nQwen & embedding & 56.5 & [55.8, 57.2] & +2.0 \\\\\n\\midrule\nStarCoder & BM25 & 43.3 & [42.3, 44.3] & $-$2.7 \\\\\nStarCoder & random & 46.0 & [45.1, 46.9] & --- \\\\\nStarCoder & dataflow & 45.8 & [44.8, 46.8] & $-$0.2 \\\\\nStarCoder & embedding & 47.5 & [46.6, 48.4] & +1.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBM25 negatives harm performance for both encoders ($-$2.5pp Qwen, $-$2.7pp StarCoder vs random).\nBM25 selects lexically similar files that share function names, variable names, and import patterns with the query.\nThese are precisely the signals that contrastive learning should leverage for discrimination; training the encoder to ignore them degrades retrieval.\n\nTrue embedding-distance mining improves both encoders (+2.0pp Qwen, +1.5pp StarCoder), selecting files that are semantically similar in the pretrained embedding space but not relevant to the query.\nThis forces the encoder to learn finer-grained semantic distinctions.\n\nDataflow negatives benefit Qwen (+1.0pp, CI lower bound $>$ 0) but not StarCoder ($-$0.2pp, CI includes zero).\nSection~\\ref{sec:stratified} provides mechanistic explanation for this interaction.\n\n%------------------------------------------------------------------------------\n\\subsection{SWE-bench Lite End-to-End Evaluation}\n\\label{sec:swebench}\n%------------------------------------------------------------------------------\n\n\\begin{table}[h]\n\\centering\n\\caption{SWE-bench Lite resolve rate (300 instances, Qwen3.6-27B agent, top-5 retrieval).}\n\\label{tab:swebench}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Resolved} & \\textbf{Total} & \\textbf{Rate (\\%)} & \\textbf{$\\Delta$ vs Random (pp)} \\\\\n\\midrule\nrandom & 66 & 300 & 22.0 & --- \\\\\nembedding & 73 & 300 & 24.3 & +2.3 \\\\\ndataflow & 76 & 300 & 25.3 & +3.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRetrieval quality improvements amplify at the downstream task level.\nEmbedding mining yields +2.5pp resolve rate ($p = 0.018$, 95\\% CI [+0.7, +4.3]), and dataflow yields +3.2pp ($p = 0.008$, CI [+1.0, +5.5]) over random (Table~\\ref{tab:swebench_bootstrap}).\nThe difference between dataflow and embedding is +0.7pp but not significant ($p = 0.134$, CI [$-$1.5, +2.9]).\n\n\\begin{table}[h]\n\\centering\n\\caption{Bootstrap significance tests for SWE-bench Lite (10K resamples).}\n\\label{tab:swebench_bootstrap}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} & \\textbf{$p$-value} \\\\\n\\midrule\nembedding $-$ random & +2.5 & [+0.7, +4.3] & 0.018 \\\\\ndataflow $-$ random & +3.2 & [+1.0, +5.5] & 0.008 \\\\\ndataflow $-$ embedding & +0.7 & [$-$1.5, +2.9] & 0.134 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Breakdown by Patch Complexity.}\nMulti-file patches (37\\% of instances) are the primary source of dataflow advantage: dataflow achieves +5.4pp over random on multi-file patches (17.1\\% vs 11.7\\%) compared to +2.2pp on single-file patches (30.2\\% vs 28.0\\%).\nThis is consistent with the mechanism: dataflow negatives train the retriever to understand cross-module dependencies, which matters most when the gold patch spans multiple files.\n\n\\begin{table}[h]\n\\centering\n\\caption{SWE-bench resolve rate by patch complexity.}\n\\label{tab:swebench_complexity}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Patch Type} & \\textbf{N} & \\textbf{random (\\%)} & \\textbf{embedding (\\%)} & \\textbf{dataflow (\\%)} \\\\\n\\midrule\nsingle-file & 189 & 28.0 & 30.7 & 30.2 \\\\\nmulti-file & 111 & 11.7 & 14.4 & 17.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------------------\n\\subsection{RepoBench-R Cross-File Retrieval}\n\\label{sec:repobench}\n%------------------------------------------------------------------------------\n\nTable~\\ref{tab:repobench} shows results on RepoBench-R test\\_hard (pool $\\approx$ 18).\nEmbedding mining significantly improves R@1 for both encoders (+2.1pp Qwen, +1.5pp StarCoder), confirming cross-benchmark generalization.\nDataflow provides +1.2pp for Qwen (CI marginally excludes zero) but is ineffective for StarCoder ($-$0.2pp, CI includes zero)---the same encoder-strategy interaction observed on SWE-smith.\n\n\\begin{table}[h]\n\\centering\n\\caption{RepoBench-R test\\_hard results (pool $\\approx$ 18, 9-seed mean $\\pm$ 95\\% CI).}\n\\label{tab:repobench}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Strategy} & \\textbf{R@1 (\\%)} & \\textbf{95\\% CI} & \\textbf{$\\Delta$ vs Random (pp)} \\\\\n\\midrule\nQwen & random & 62.1 & [61.4, 62.8] & --- \\\\\nQwen & embedding & 64.2 & [63.4, 65.0] & +2.1 \\\\\nQwen & dataflow & 63.3 & [62.4, 64.2] & +1.2 \\\\\n\\midrule\nStarCoder & random & 57.4 & [56.6, 58.2] & --- \\\\\nStarCoder & embedding & 58.9 & [58.0, 59.8] & +1.5 \\\\\nStarCoder & dataflow & 57.2 & [56.2, 58.2] & $-$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn test\\_easy (pool $\\approx$ 6), deltas are compressed due to ceiling effects: Qwen embedding +1.2pp (84.3\\% $\\to$ 85.5\\%), StarCoder embedding +1.0pp (81.2\\% $\\to$ 82.2\\%).\nThis is expected---smaller pools leave fewer distractors for mining quality to differentiate.\n\n%------------------------------------------------------------------------------\n\\subsection{Stratified Analysis}\n\\label{sec:stratified}\n%------------------------------------------------------------------------------\n\n\\paragraph{Structural Data Availability.}\nTable~\\ref{tab:stratified_structural} decomposes dataflow performance by whether structural data was available for each instance.\nOn the 34\\% of instances with dataflow connectivity, the dataflow advantage is +2.8pp (Qwen)---substantially larger than the pooled +1.0pp.\nOn the 66\\% fallback stratum where dataflow degrades to embedding or random selection, the advantage is +0.1pp (effectively zero).\nThis decomposition directly addresses the concern that 34\\% coverage dilutes the signal: the true per-instance effect is +2.8pp, not +1.0pp.\n\n\\begin{table}[h]\n\\centering\n\\caption{Stratified R@1 delta by structural data availability (Qwen encoder).}\n\\label{tab:stratified_structural}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Stratum} & \\textbf{N} & \\textbf{random} & \\textbf{embedding} & \\textbf{dataflow} & \\textbf{df$-$rand (pp)} \\\\\n\\midrule\nWith dataflow (34\\%) & $\\sim$5.2K & 53.1 & 55.4 & 55.9 & +2.8 \\\\\nFallback (66\\%) & $\\sim$10K & 55.2 & 57.3 & 55.3 & +0.1 \\\\\n\\midrule\nOverall & $\\sim$15.2K & 54.5 & 56.5 & 55.5 & +1.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Negative Difficulty Quartiles.}\nTable~\\ref{tab:neg_difficulty} presents the strongest mechanistic evidence.\nWe partition instances by negative difficulty (margin between positive and hardest negative similarity).\nThe benefit of mining strategies scales monotonically with difficulty: Q4 (hardest, margin 0.008) shows +3.2pp embedding delta, while Q1 (easiest, margin 0.142) shows only +0.8pp.\nThis confirms the representation saturation hypothesis: when random negatives are already easy to distinguish (large margin), better mining adds little; when the margin is thin, mining quality is critical.\n\n\\begin{table}[h]\n\\centering\n\\caption{R@1 delta by negative difficulty quartile (Qwen encoder).}\n\\label{tab:neg_difficulty}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Quartile} & \\textbf{Margin (mean)} & \\textbf{emb$-$rand (pp)} & \\textbf{df$-$rand (pp)} \\\\\n\\midrule\nQ1 (easiest) & 0.142 & +0.8 & +0.3 \\\\\nQ2 & 0.078 & +1.5 & +0.7 \\\\\nQ3 & 0.031 & +2.4 & +1.2 \\\\\nQ4 (hardest) & 0.008 & +3.2 & +2.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Repo Size and Pool Size Strata.}\nEmbedding delta is inversely related to repository size: small repos ($<$50 files) show +2.8pp, while extra-large repos ($>$500 files) show +1.6pp.\nPool size strata show a complementary pattern: embedding delta increases from +1.0pp (pool $<$ 20) to +2.5pp (pool $>$ 50), as larger pools provide more distractors where mining quality matters.\n\n\\paragraph{Query--Positive Similarity.}\nWhen query-positive similarity is high ($>$0.95), embedding delta is largest (+2.6pp) and dataflow delta is also substantial (+1.8pp).\nAt low similarity ($<$0.85), both deltas shrink (+1.2pp embedding, +0.2pp dataflow).\nHigh-similarity instances are precisely those where the retriever struggles to separate the positive from near-duplicates, making negative quality most impactful.\n\n%------------------------------------------------------------------------------\n\\subsection{Ablation Studies}\n\\label{sec:ablations}\n%------------------------------------------------------------------------------\n\n\\subsubsection{Temperature Ablation}\n\\label{sec:temp_ablation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature ablation (R@1 \\%). Strategy rankings are preserved across all three temperatures.}\n\\label{tab:temperature}\n\\begin{tabular}{clcccc}\n\\toprule\n$\\tau$ & \\textbf{Encoder} & \\textbf{random} & \\textbf{embedding} & \\textbf{dataflow} & \\textbf{emb$-$rand (pp)} \\\\\n\\midrule\n0.05 & Qwen & 55.8 & 57.7 & 56.9 & +1.9 \\\\\n0.05 & StarCoder & 47.0 & 48.5 & 46.7 & +1.5 \\\\\n0.10 & Qwen & 54.5 & 56.5 & 55.5 & +2.0 \\\\\n0.10 & StarCoder & 46.0 & 47.5 & 45.8 & +1.5 \\\\\n0.20 & Qwen & 53.0 & 54.6 & 53.8 & +1.6 \\\\\n0.20 & StarCoder & 44.8 & 46.1 & 44.7 & +1.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStrategy rankings (embedding $>$ dataflow $>$ random for Qwen; embedding $>$ random $\\approx$ dataflow for StarCoder) are preserved across all three temperatures (Table~\\ref{tab:temperature}).\n$\\tau = 0.05$ achieves the highest absolute performance due to sharper gradient signals.\n$\\tau = 0.20$ compresses deltas (1.6pp vs 2.0pp) but does not reverse rankings, confirming findings are not temperature-regime-specific.\nWe use $\\tau = 0.1$ as the default, following literature convention.\n\n\\subsubsection{Call-Graph Hop Depth Ablation}\n\\label{sec:hop_ablation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Hop depth ablation for dataflow negatives (Qwen encoder).}\n\\label{tab:hop_depth}\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Hops} & \\textbf{Coverage (\\%)} & \\textbf{Neg/query} & \\textbf{R@1 (\\%)} & \\textbf{$\\Delta$ vs 2-hop (pp)} \\\\\n\\midrule\n1 & 12.4 & 18.2 & 54.8 & $-$0.7 \\\\\n2 & 34.3 & 31.7 & 55.5 & --- \\\\\n3 & 58.6 & 42.1 & 55.1 & $-$0.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n2-hop call-graph bounding is optimal (Table~\\ref{tab:hop_depth}).\n1-hop is too conservative: only 12.4\\% coverage means most instances lack sufficient connected nodes to define meaningful ``disconnected'' negatives.\n3-hop is too permissive: 58.6\\% coverage narrows the disconnected set excessively, excluding structurally related files that would serve as good negatives.\n2-hop captures direct callers/callees and their immediate neighbors, providing a principled boundary at 34.3\\% coverage.\n\n\\subsubsection{Training Data Size Scaling}\n\\label{sec:data_scaling}\n\n\\begin{table}[h]\n\\centering\n\\caption{Data size scaling (Qwen encoder). Strategy rankings and monotonic improvement are stable across scales.}\n\\label{tab:data_scaling}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Size} & \\textbf{random} & \\textbf{embedding} & \\textbf{dataflow} & \\textbf{emb$-$rand (pp)} & $\\sigma$ \\textbf{seeds} \\\\\n\\midrule\n1K & 51.0 & 52.2 & 51.5 & +1.2 & 1.5 \\\\\n3K & 53.2 & 55.0 & 54.1 & +1.8 & 1.0 \\\\\n5K & 54.5 & 56.5 & 55.5 & +2.0 & 0.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStrategy ranking (embedding $>$ dataflow $>$ random) is preserved across 1K, 3K, and 5K training instances (Table~\\ref{tab:data_scaling}).\nThe embedding--random delta grows from +1.2pp at 1K to +2.0pp at 5K, with no sign of diminishing returns.\nSeed variance decreases from $\\sigma = 1.5$ at 1K to $\\sigma = 0.8$ at 5K as larger datasets reduce sampling noise.\n\n\\subsubsection{Fusion Head Ablation}\n\\label{sec:fusion_ablation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Fusion head ablation: training-time mining vs inference-time feature injection.}\n\\label{tab:fusion}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Configuration} & \\textbf{Qwen R@1 (\\%)} & \\textbf{StarCoder R@1 (\\%)} \\\\\n\\midrule\nembedding-only (ours) & 56.5 & 47.5 \\\\\nstructural-features-only & 49.8 & 42.1 \\\\\ncombined fusion & 56.1 & 47.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:fusion} isolates the value of training-time mining versus inference-time structural feature injection.\nEmbedding-only (our approach: mine negatives during training, no structural features at inference) performs best or ties with combined fusion.\nStructural-features-only (no mining, inject CodeQL connectivity features at inference) is far worse ($-$6.7pp Qwen).\nCombined fusion slightly underperforms embedding-only ($-$0.4pp) because inference-time structural features introduce noise from the 66\\% of instances without CodeQL coverage.\nThe core value of StructFuse is in the \\emph{mining strategy}, not in feature engineering.\n\n\\subsubsection{Pool Size Sensitivity}\n\\label{sec:pool_sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\caption{Pool size sensitivity (R@1 \\%). Strategy rankings are 100\\% stable across pool sizes spanning an order of magnitude.}\n\\label{tab:pool_size}\n\\begin{tabular}{clccccc}\n\\toprule\n\\textbf{Pool} & \\textbf{Encoder} & \\textbf{random} & \\textbf{embedding} & \\textbf{dataflow} & \\textbf{emb$-$rand (pp)} & \\textbf{Ranking} \\\\\n\\midrule\n50 & Qwen & 54.5 & 56.5 & 55.5 & +2.0 & E$>$D$>$R \\\\\n100 & Qwen & 42.8 & 44.7 & 43.8 & +1.9 & E$>$D$>$R \\\\\n200 & Qwen & 34.2 & 35.9 & 35.1 & +1.7 & E$>$D$>$R \\\\\n500 & Qwen & 26.1 & 27.6 & 26.9 & +1.5 & E$>$D$>$R \\\\\n\\midrule\n50 & StarCoder & 46.0 & 47.5 & 45.8 & +1.5 & E$>$R$>$D \\\\\n100 & StarCoder & 35.8 & 37.2 & 35.7 & +1.4 & E$>$R$>$D \\\\\n200 & StarCoder & 28.2 & 29.5 & 28.1 & +1.3 & E$>$R$\\approx$D \\\\\n500 & StarCoder & 21.4 & 22.5 & 21.3 & +1.1 & E$>$R$\\approx$D \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStrategy rankings are 100\\% stable across pool sizes from 50 to 500 (Table~\\ref{tab:pool_size}).\nAbsolute R@1 drops as expected with larger pools, and the embedding--random delta degrades gracefully from 2.0pp to 1.5pp (Qwen) and 1.5pp to 1.1pp (StarCoder) at approximately $-$0.15pp per pool-size doubling.\nThe delta does not collapse, confirming the mining strategy's value is not an artifact of small pool sizes.\n\n\\subsubsection{Dynamic vs Static Embedding Mining}\n\\label{sec:dynamic_mining}\n\n\\begin{table}[h]\n\\centering\n\\caption{Static vs dynamic embedding mining. Static mining (one-time, from pretrained) is sufficient.}\n\\label{tab:dynamic}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Static R@1 (\\%)} & \\textbf{Dynamic R@1 (\\%)} & \\textbf{$\\Delta$ (pp)} & $p$\\textbf{-value} \\\\\n\\midrule\nQwen & 56.5 & 56.8 & +0.3 & 0.41 \\\\\nStarCoder & 47.5 & 47.7 & +0.2 & 0.53 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDynamic mining (re-computing negatives each epoch using the current encoder) provides negligible improvement over static mining (+0.3pp Qwen, +0.2pp StarCoder, both non-significant; Table~\\ref{tab:dynamic}).\nLoRA rank-16 fine-tuning changes the embedding space only slightly, so pretrained nearest neighbors remain valid throughout training.\nThis rules out the curriculum-effect confound and simplifies the practical recommendation: mine once from the pretrained checkpoint.\n\n\\subsubsection{Weighted vs Binary Dataflow Negatives}\n\\label{sec:weighted}\n\n\\begin{table}[h]\n\\centering\n\\caption{Weighted (by hop distance) vs binary dataflow negatives. Binary is sufficient.}\n\\label{tab:weighted}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Qwen R@1 (\\%)} & \\textbf{StarCoder R@1 (\\%)} & \\textbf{$\\Delta$ vs Binary (pp)} \\\\\n\\midrule\nBinary (default) & 55.5 & 45.8 & --- \\\\\nDistance-weighted & 55.8 & 45.9 & +0.3 / +0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWeighting dataflow negatives by hop distance (farther = higher sampling probability) provides no significant improvement over binary connected/disconnected classification (+0.3pp Qwen, +0.1pp StarCoder; Table~\\ref{tab:weighted}).\nThe binary signal---``on the call chain or not''---captures the essential structural distinction.\nFurther distance-based refinement adds complexity without benefit.\n\n%------------------------------------------------------------------------------\n\\subsection{Failure Analysis}\n\\label{sec:failure}\n%------------------------------------------------------------------------------\n\nWe manually analyzed 50 failure cases from the random retriever on SWE-bench Lite (Table~\\ref{tab:failure}).\n44\\% (22/50) are retrieval failures (wrong files retrieved), of which 64\\% (14/22) involve cross-module dependencies where the gold file is a caller/callee of a retrieved-but-wrong file.\nThese are precisely the cases dataflow training targets.\n30\\% (15/50) are retrieval successes where the agent fails to generate correct patches, establishing a ceiling: even with perfect retrieval, $\\sim$85\\% is the maximum achievable resolve rate given agent limitations.\n\n\\begin{table}[h]\n\\centering\n\\caption{Failure category breakdown (50 random-retriever failures from SWE-bench Lite).}\n\\label{tab:failure}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Category} & \\textbf{Count} & \\textbf{\\% of 50} & \\textbf{Dataflow Could Help?} \\\\\n\\midrule\nRetrieval: wrong files & 22 & 44\\% & 14/22 (64\\%) \\\\\nRetrieval OK, agent fail & 15 & 30\\% & N/A \\\\\nContext window limit & 7 & 14\\% & 5/7 partially \\\\\nTest env issue & 4 & 8\\% & No \\\\\nAmbiguous issue & 2 & 4\\% & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Illustrative Example.}\nConsider a Django issue about \\texttt{QuerySet.filter()} returning wrong results with nested Q objects.\nThe random retriever ranks \\texttt{django/db/models/query.py} first (text match on ``filter''), but the bug resides in \\texttt{django/db/models/sql/query.py} (the downstream SQL builder invoked by \\texttt{filter}).\nThe dataflow-trained retriever correctly ranks the SQL builder file higher, having learned that structurally connected files along the call chain are more likely to co-occur in patches.\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Why Does the Encoder--Strategy Interaction Exist?}\nQwen2.5-Coder-3B exhibits representation saturation (mean pos\\_sim = 0.9855), compressing positive and negative embeddings into a narrow similarity band.\nRandom negatives are trivially separable and provide weak gradient signal.\nEmbedding mining selects negatives that are genuinely close in this compressed space, providing the difficulty gradient the encoder needs.\nDataflow negatives add an orthogonal structural dimension that further assists discrimination.\n\nStarCoder2-3B has healthier separation (mean pos\\_sim = 0.7985).\nRandom negatives already provide moderate difficulty, and embedding mining further refines the boundary.\nDataflow negatives offer no additional benefit because the embedding space is not saturated---the encoder can already separate structural from textual similarity using learned features alone.\n\n\\paragraph{Relationship to Inference-Time Graph Methods.}\nStructFuse operates at training time, distilling structural knowledge into encoder representations via negative mining.\nInference-time graph methods (CodexGraph, LocAgent, RANGER, ARISE, and others; Table~\\ref{tab:lit_comparison}) navigate or re-rank over code graphs at inference time.\nThe two approaches are complementary: StructFuse produces a better base retriever that graph-based methods can navigate over.\nWe do not claim superiority over these methods, as they solve different problems and operate under different computational budgets.\n\n\\begin{table}[h]\n\\centering\n\\caption{Comparison with inference-time graph methods. StructFuse is the only method that leverages structural signal at training time without inference-time overhead.}\n\\label{tab:lit_comparison}\n\\begin{tabular}{llll}\n\\toprule\n\\textbf{Method} & \\textbf{Graph Stage} & \\textbf{Graph Type} & \\textbf{Complementary?} \\\\\n\\midrule\nStructFuse (ours) & Training & Dataflow (CodeQL) & --- \\\\\nCodexGraph & Inference & Code graph DB & Yes \\\\\nLocAgent & Inference & Repo structure & Yes \\\\\nRANGER & Inference & Call graph & Yes \\\\\nARISE & Inference & Intra-proc dataflow & Partially \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Practical Recommendations.}\nBased on our findings: (1) Always use true embedding-distance mining over random negatives---the improvement is consistent across encoders, benchmarks, temperatures, pool sizes, and data scales. (2) Never use BM25 negatives for code retrieval contrastive training. (3) Consider dataflow negatives when encoder representations are saturated (check pos\\_sim distribution); static mining suffices. (4) Binary structural signal is sufficient; weighted variants add complexity without benefit.\n\n\\paragraph{Limitations.}\nOur study is limited to two 3B-parameter decoder-only code encoders; generalization to encoder-only architectures (e.g., CodeBERT) and larger models remains to be verified.\nCodeQL structural extraction achieves 34\\% coverage, limiting the effective reach of dataflow negatives.\nSWE-bench Lite evaluation uses 300 instances with a single agent model, providing limited statistical power for pairwise comparisons between mining strategies.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe presented a systematic study of hard negative mining strategies for contrastive code retrieval.\nOur controlled comparison of four strategies---BM25, random, dataflow, and embedding-distance---across two encoders, three benchmarks, and extensive ablations establishes three findings:\n(1)~True embedding-distance mining consistently improves code retrieval, correcting the prior misconception that embedding negatives are harmful (the reported harm stems from BM25-proxy negatives).\n(2)~Structure-grounded dataflow negatives provide conditional benefit when encoder representations are saturated, with the true per-instance effect (+2.8pp) masked by coverage-driven dilution in pooled results.\n(3)~Negative difficulty quartile analysis provides mechanistic explanation: harder instances benefit more from better negatives (Q4: +3.2pp vs Q1: +0.8pp), linking mining strategy effectiveness to representation geometry.\n\nThese findings transfer to downstream tasks (SWE-bench Lite: +2.5pp embedding, +3.2pp dataflow resolve rate) and are robust across temperatures, pool sizes, data scales, and a second benchmark (RepoBench-R).\nStrategy rankings never reverse across any experimental condition tested.\n\n\\bibliographystyle{plainnat}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "419a8e83-32a7-4309-9a71-69a575fed846",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context…",
  "leafUuid": "a0942bcf-b7ea-4e59-8727-ef23bd20776e",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper with experimental data",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3"
}
```

---

### Tool call

_source line 23 · 2026-05-14T16:49:53.252Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01H35p4xWRB6kALZP8fBhXXc`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0942bcf-b7ea-4e59-8727-ef23bd20776e",
  "isSidechain": false,
  "requestId": "req_011Cb2oeEAtbSzn6995Rmngc",
  "type": "assistant",
  "uuid": "568da508-b533-4333-93aa-81f5c9b2487a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDxJt5H3erGyJDdQ2Fk8vq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11222,
      "cache_read_input_tokens": 44963,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 44963,
          "cache_creation_input_tokens": 11222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11222
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

_source line 24 · 2026-05-14T16:49:54.847Z_

<details><summary>↩ Tool result · `toolu_01H35p4xWRB6kALZP8fBhXXc`</summary>

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)
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
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (0.78954pt too wide) in paragraph at lines 41--44
\T1/cmr/m/n/10.95 language is-sue de-scrip-tion. Con-trastive learn-ing with ha
rd neg-a-tive min-ing is the dom-i-nant paradigm
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

LaTeX Warning: Reference `tab:lit_comparison' on page 2 undefined on input line
 94.

[2]

LaTeX Warning: Reference `sec:hop_ablation' on page 3 undefined on input line 1
49.


Overfull \hbox (16.4952pt too wide) in paragraph at lines 155--159
\T1/cmr/m/n/10.95 We fine-tune two decoder-only code en-coders with LoRA (rank 
16): Qwen2.5-Coder-3B and StarCoder2-
[3]

LaTeX Warning: Reference `tab:main_4strategy' on page 4 undefined on input line
 185.


LaTeX Warning: Reference `sec:stratified' on page 4 undefined on input line 217
.

[4]

LaTeX Warning: Reference `tab:swebench_bootstrap' on page 5 undefined on input 
line 240.


LaTeX Warning: Reference `tab:repobench' on page 5 undefined on input line 281.



LaTeX Warning: `h' float specifier changed to `ht'.

[5]

LaTeX Warning: Reference `tab:stratified_structural' on page 6 undefined on inp
ut line 313.


LaTeX Warning: Reference `tab:neg_difficulty' on page 6 undefined on input line
 335.

[6]

LaTeX Warning: Reference `tab:temperature' on page 7 undefined on input line 39
1.


LaTeX Warning: Reference `tab:hop_depth' on page 7 undefined on input line 414.


[7]

LaTeX Warning: Reference `tab:data_scaling' on page 8 undefined on input line 4
37.


LaTeX Warning: Reference `tab:fusion' on page 8 undefined on input line 459.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:pool_size' on page 8 undefined on input line 489.



LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:dynamic' on page 8 undefined on input line 510.

[8]

LaTeX Warning: Reference `tab:weighted' on page 9 undefined on input line 531.


LaTeX Warning: Reference `tab:failure' on page 9 undefined on input line 540.


LaTeX Warning: `h' float specifier changed to `ht'.

[9]

LaTeX Warning: Reference `tab:lit_comparison' on page 10 undefined on input lin
e 584.

[10] [11] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk>
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0600
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0600
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0600.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf
 Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]
[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]
[183] [184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf
 Ok [25] [26] [28] [27] [29] [30] [31])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf
 Ok) ) ) )
Font metrics written on ecrm0600.tfm.
Output written on ecrm0600.600gf (256 characters, 32624 bytes).
Transcript written on ecrm0600.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk: successfully generated.
 &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/
home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy8.pfb>
Output written on paper.pdf (11 pages, 238189 bytes).
Transcript written on paper.log.
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)
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
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (0.78954pt too wide) in paragraph at lines 41--44
\T1/cmr/m/n/10.95 language is-sue de-scrip-tion. Con-trastive learn-ing with ha
rd neg-a-tive min-ing is the dom-i-nant paradigm
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2]
Overfull \hbox (16.4952pt too wide) in paragraph at lines 155--159
\T1/cmr/m/n/10.95 We fine-tune two decoder-only code en-coders with LoRA (rank 
16): Qwen2.5-Coder-3B and StarCoder2-
[3] [4]

LaTeX Warning: `h' float specifier changed to `ht'.

[5] [6] [7]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[8]

LaTeX Warning: `h' float specifier changed to `ht'.

[9] [10] [11] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/
home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy8.pfb>
Output written on paper.pdf (11 pages, 240920 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "568da508-b533-4333-93aa-81f5c9b2487a",
  "isSidechain": false,
  "promptId": "7dbbfae7-135c-4257-9519-f147e9c1c35b",
  "type": "user",
  "uuid": "9683e76a-22c2-4e4c-931d-b93e804cadac",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (0.78954pt too wide) in paragraph at lines 41--44\n\\T1/cmr/m/n/10.95 language is-sue de-scrip-tion. Con-trastive learn-ing with ha\nrd neg-a-tive min-ing is the dom-i-nant paradigm\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nLaTeX Warning: Reference `tab:lit_comparison' on page 2 undefined on input line\n 94.\n\n[2]\n\nLaTeX Warning: Reference `sec:hop_ablation' on page 3 undefined on input line 1\n49.\n\n\nOverfull \\hbox (16.4952pt too wide) in paragraph at lines 155--159\n\\T1/cmr/m/n/10.95 We fine-tune two decoder-only code en-coders with LoRA (rank \n16): Qwen2.5-Coder-3B and StarCoder2-\n[3]\n\nLaTeX Warning: Reference `tab:main_4strategy' on page 4 undefined on input line\n 185.\n\n\nLaTeX Warning: Reference `sec:stratified' on page 4 undefined on input line 217\n.\n\n[4]\n\nLaTeX Warning: Reference `tab:swebench_bootstrap' on page 5 undefined on input \nline 240.\n\n\nLaTeX Warning: Reference `tab:repobench' on page 5 undefined on input line 281.\n\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5]\n\nLaTeX Warning: Reference `tab:stratified_structural' on page 6 undefined on inp\nut line 313.\n\n\nLaTeX Warning: Reference `tab:neg_difficulty' on page 6 undefined on input line\n 335.\n\n[6]\n\nLaTeX Warning: Reference `tab:temperature' on page 7 undefined on input line 39\n1.\n\n\nLaTeX Warning: Reference `tab:hop_depth' on page 7 undefined on input line 414.\n\n\n[7]\n\nLaTeX Warning: Reference `tab:data_scaling' on page 8 undefined on input line 4\n37.\n\n\nLaTeX Warning: Reference `tab:fusion' on page 8 undefined on input line 459.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:pool_size' on page 8 undefined on input line 489.\n\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:dynamic' on page 8 undefined on input line 510.\n\n[8]\n\nLaTeX Warning: Reference `tab:weighted' on page 9 undefined on input line 531.\n\n\nLaTeX Warning: Reference `tab:failure' on page 9 undefined on input line 540.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9]\n\nLaTeX Warning: Reference `tab:lit_comparison' on page 10 undefined on input lin\ne 584.\n\n[10] [11] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0600\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0600\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0600.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecrm0600.tfm.\nOutput written on ecrm0600.600gf (256 characters, 32624 bytes).\nTranscript written on ecrm0600.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/\nhome/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy8.pfb>\nOutput written on paper.pdf (11 pages, 238189 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (0.78954pt too wide) in paragraph at lines 41--44\n\\T1/cmr/m/n/10.95 language is-sue de-scrip-tion. Con-trastive learn-ing with ha\nrd neg-a-tive min-ing is the dom-i-nant paradigm\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2]\nOverfull \\hbox (16.4952pt too wide) in paragraph at lines 155--159\n\\T1/cmr/m/n/10.95 We fine-tune two decoder-only code en-coders with LoRA (rank \n16): Qwen2.5-Coder-3B and StarCoder2-\n[3] [4]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5] [6] [7]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9] [10] [11] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/\nhome/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy8.pfb>\nOutput written on paper.pdf (11 pages, 240920 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "568da508-b533-4333-93aa-81f5c9b2487a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context…",
  "leafUuid": "9683e76a-22c2-4e4c-931d-b93e804cadac",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper with experimental data",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3"
}
```

---

### Assistant

_source line 27 · 2026-05-14T16:50:03.914Z_

编译成功，11 页 PDF，无错误（仅有少量 overfull hbox 警告）。

论文已写入 `paper.tex` 并编译为 `paper.pdf`，位于指定目录。覆盖全部 13 个实验：

- **Main results**: 4-strategy comparison (BM25/random/dataflow/embedding) — Table 3
- **SWE-bench Lite**: resolve rate + bootstrap CIs + patch complexity breakdown — Tables 4, 4b, 4c
- **RepoBench-R**: cross-benchmark validation — Table 5
- **Stratified analysis**: structural availability + neg difficulty quartiles — Tables 7, 7b
- **Ablations**: temperature (Table 8), hop depth (Table 9), data scaling (Table 10), fusion head (Table 11), pool size (Table 12), dynamic vs static (Table 13), weighted vs binary (Table S1)
- **Failure analysis**: 50-case breakdown — Table S2
- **Literature comparison**: inference-time graph methods — Table S3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9683e76a-22c2-4e4c-931d-b93e804cadac",
  "isSidechain": false,
  "requestId": "req_011Cb2oeeSPyR6twDYmbbmct",
  "type": "assistant",
  "uuid": "35861a07-6d37-49a3-b82e-b7e3474c2f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJrnnQrzrR14RuzFW11V1x",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8642,
      "cache_read_input_tokens": 56185,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8642,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 56185,
          "cache_creation_input_tokens": 8642,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8642
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

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context…",
  "leafUuid": "35861a07-6d37-49a3-b82e-b7e3474c2f66",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper with experimental data",
  "sessionId": "92616111-09cc-4079-a3df-7d5669f885d3"
}
```

---
