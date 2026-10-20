# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T052642 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/419eb035-6fa3-4657-a096-4c92223d8c5a.jsonl`
- **Structured JSON:** [`39eb4af827edbaf0ef0a.json`](../../sessions/39/39eb4af827edbaf0ef0a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T06:19:41.811Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T06:19:41.811Z",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T052642 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：核心 \"type-valid IE\" framing 不成立，需完全 reframe。仍冲 EMNLP 2026（October ARR cycle），不降级 venue。 Reframe: \"constrained decoding method paper\" → \"empirical study paper with a tool\"。 新 title: \"How Do LLMs Violate Ontology Constraints? A Systematic Study with Mitigation\"。 新 story: (1) violation landscape 系统性实证研究为主贡献；(2) OntoCoDec 降级为 mitigation tool； (3) 重心转向 analysis findings — why prompt 不够、why post-hoc 不够、why grammar-only 不够、why CF 必然存在。 Novelty 锚点从 method → empirical findings + theoretical analysis，回避 \"incremental over XGrammar\"。 补充: (a) per-relation-type violation pattern 深度分析；(b) GoLLIE code-generation IE violation 对比； (c) decidability taxonomy 扩展为 formal framework。 预估 reviewer 评分: Overall 2.5–3.5, Novelty 2–3, Soundness 3–3.5, Significance 2–3, hostile_reviewer_count 2–3。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T06:19:41.820Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T06:19:41.820Z",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-22T06:19:41.845Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T052642 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：核心 "type-valid IE" framing 不成立，需完全 reframe。仍冲 EMNLP 2026（October ARR cycle），不降级 venue。 Reframe: "constrained decoding method paper" → "empirical study paper with a tool"。 新 title: "How Do LLMs Violate Ontology Constraints? A Systematic Study with Mitigation"。 新 story: (1) violation landscape 系统性实证研究为主贡献；(2) OntoCoDec 降级为 mitigation tool； (3) 重心转向 analysis findings — why prompt 不够、why post-hoc 不够、why grammar-only 不够、why CF 必然存在。 Novelty 锚点从 method → empirical findings + theoretical analysis，回避 "incremental over XGrammar"。 补充: (a) per-relation-type violation pattern 深度分析；(b) GoLLIE code-generation IE violation 对比； (c) decidability taxonomy 扩展为 formal framework。 预估 reviewer 评分: Overall 2.5–3.5, Novelty 2–3, Soundness 3–3.5, Significance 2–3, hostile_reviewer_count 2–3。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "24b84624-7cc9-4802-b961-7b1d19e328f3",
  "type": "user",
  "uuid": "15109924-14fb-4fdc-99d0-c577fa7bbf7a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T06:19:41.844Z_

```json
{
  "parentUuid": "15109924-14fb-4fdc-99d0-c577fa7bbf7a",
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
  "uuid": "91c8d1f4-3af3-4684-8487-23d88c40c074",
  "timestamp": "2026-05-22T06:19:41.844Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T06:19:41.844Z_

```json
{
  "parentUuid": "91c8d1f4-3af3-4684-8487-23d88c40c074",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "eb131449-0ce0-4a4f-bcf7-bedaac138ef6",
  "timestamp": "2026-05-22T06:19:41.844Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier mock research paper",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a"
}
```

---

### Assistant

_source line 7 · 2026-05-22T06:19:44.674Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb131449-0ce0-4a4f-bcf7-bedaac138ef6",
  "isSidechain": false,
  "requestId": "req_011CbH84cjXGCU97qd1Bootc",
  "type": "assistant",
  "uuid": "45fff720-1ef6-4f95-abb4-fa3f4e13db21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CnVdSLUiDfhYjYT47Gze5r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12190,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12190,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12190
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

_source line 8 · 2026-05-22T06:19:45.846Z_

<details open><summary>🔧 Tool call — Read · `toolu_018tcarcU6wAhnzAwfMq42MR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45fff720-1ef6-4f95-abb4-fa3f4e13db21",
  "isSidechain": false,
  "requestId": "req_011CbH84cjXGCU97qd1Bootc",
  "type": "assistant",
  "uuid": "3a1061ec-f826-46ec-8d97-c34b8ccb0250",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CnVdSLUiDfhYjYT47Gze5r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12190,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12190,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12190
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

_source line 9 · 2026-05-22T06:19:46.048Z_

<details open><summary>🔧 Tool call — Read · `toolu_015eiJWSx62pRpkP7Yq9kHQf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a1061ec-f826-46ec-8d97-c34b8ccb0250",
  "isSidechain": false,
  "requestId": "req_011CbH84cjXGCU97qd1Bootc",
  "type": "assistant",
  "uuid": "cf601ea7-77fe-43b1-b82e-51f3fee062a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CnVdSLUiDfhYjYT47Gze5r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12190,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12190,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12190
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

_source line 10 · 2026-05-22T06:19:46.136Z_

<details><summary>↩ Tool result · `toolu_018tcarcU6wAhnzAwfMq42MR`</summary>

```text
1	[
2	  {
3	    "name": "WikiEvents Qwen3-8B unconstrained",
4	    "description": "WikiEvents EE unconstrained baseline, Qwen3-8B, 246 docs",
5	    "results": {
6	      "parse_rate_pct": 88.6,
7	      "EV_pct": 24.0,
8	      "RoV_pct": 74.9,
9	      "AC_pct": 0.3,
10	      "CF_pct": 0,
11	      "trigger_f1_pct": 11.84,
12	      "argument_f1_pct": 0.09,
13	      "entity_f1_pct": 0
14	    },
15	    "tables": [
16	      {
17	        "name": "WikiEvents ZS Unconstrained Baselines (3 Models)",
18	        "columns": [
19	          "Model",
20	          "Parse%",
21	          "EV%",
22	          "RoV%",
23	          "AC%",
24	          "Trig-F1",
25	          "Arg-F1",
26	          "Ent-F1"
27	        ],
28	        "rows": [
29	          [
30	            "Qwen3-8B",
31	            "88.6",
32	            "24.0",
33	            "74.9",
34	            "0.3",
35	            "11.8",
36	            "0.09",
37	            "0"
38	          ],
39	          [
40	            "Llama-3.1-8B",
41	            "91.9",
42	            "10.5",
43	            "88.8",
44	            "0.1",
45	            "5.7",
46	            "0",
47	            "0"
48	          ],
49	          [
50	            "Mistral-7B",
51	            "78.9",
52	            "37.3",
53	            "63.9",
54	            "0",
55	            "2.4",
56	            "0",
57	            "0"
58	          ]
59	        ]
60	      }
61	    ],
62	    "figures": [],
63	    "analysis": "三模型 Entity-F1=0% / Arg-F1≈0% 成为 \"EE completely dismissed\" 的核心证据。 Reviewer: \"Arg F1≈0, Entity F1 from 0→14% is just format compliance, not extraction improvement.\" 不视为 constraint enforcement 机会，而视为 task 选择失败。\n\n\n已有实际数据。Entity-F1=0%、Arg-F1≈0% 是 ZS EE 固有困难——模型无法输出 schema-valid entity 格式。Worst 档 reviewer 抓住 baseline 几乎不工作这一点：\"Even the baseline shows EE is barely functional; any 'improvement' on near-zero is format compliance recovery, not semantic extraction.\" RoV=74.9% 虽然展示了 constraint 需求，但 reviewer 反转叙事： \"This proves ZS EE is fundamentally broken, not that your method fixes it.\"\n"
64	  },
65	  {
66	    "name": "WikiEvents Llama-3.1-8B unconstrained",
67	    "description": "WikiEvents EE unconstrained baseline, Llama-3.1-8B, 246 docs",
68	    "results": {
69	      "parse_rate_pct": 91.9,
70	      "EV_pct": 10.5,
71	      "RoV_pct": 88.8,
72	      "AC_pct": 0.1,
73	      "CF_pct": 0,
74	      "trigger_f1_pct": 5.72,
75	      "argument_f1_pct": 0,
76	      "entity_f1_pct": 0
77	    },
78	    "tables": [],
79	    "figures": [],
80	    "analysis": "Llama RoV=88.8% 超过 Qwen 74.9%，模型间 violation pattern 差异巨大，但 worst-tier reviewer 不关心差异，只关心 Arg-F1=0%。\n\n\n已有实际数据。Llama RoV=88.8% 是三模型最高——近 9/10 argument role 不在 event type 定义中。Trigger-F1=5.7% 低于 Qwen。Worst 档 reviewer: \"This model is completely non-functional for EE. Constrained decoding on non-functional extraction is a constraint compliance demo, not an IE contribution.\"\n"
81	  },
82	  {
83	    "name": "WikiEvents Mistral-7B unconstrained",
84	    "description": "WikiEvents EE unconstrained baseline, Mistral-7B-v0.3, 246 docs",
85	    "results": {
86	      "parse_rate_pct": 78.9,
87	      "EV_pct": 37.3,
88	      "RoV_pct": 63.9,
89	      "AC_pct": 0,
90	      "CF_pct": 0,
91	      "trigger_f1_pct": 2.41,
92	      "argument_f1_pct": 0,
93	      "entity_f1_pct": 0
94	    },
95	    "tables": [],
96	    "figures": [],
97	    "analysis": "Mistral 是 EE 最差模型。Worst-tier reviewer 质疑为何选择它——如果用来展示\"更差模型更需要 constraint\"，那 Arg-F1=0% 的 baseline 使任何 improvement 都无意义。\n\n\n已有实际数据。Parse rate 最低 (78.9%)，EV 最高 (37.3%)——超 1/3 event type 是 OOV。 Trigger-F1=2.4% 几乎为零。Worst 档 reviewer: \"If your chosen model can't even produce valid event type names 37% of the time, the task setup itself is problematic.\" 选择明显 不适合此 task 的模型被质疑为 cherry-pick 不利 baseline 以夸大改善。\n"
98	  },
99	  {
100	    "name": "WikiEvents Mistral grammar-only v3",
101	    "description": "Grammar-only ablation on Mistral WikiEvents, proves semantic layer necessity for EE",
102	    "results": {
103	      "parse_rate_pct": 88.6,
104	      "EV_pct": 0,
105	      "RoV_pct": 64.0,
106	      "AC_pct": 13.8,
107	      "CF_pct": 1.1,
108	      "entity_f1_pct": 11.92,
109	      "trigger_f1_pct": 3.37,
110	      "argument_f1_pct": 0.27
111	    },
112	    "tables": [
113	      {
114	        "name": "WikiEvents Grammar-Only vs Full S1 (Mistral)",
115	        "columns": [
116	          "Config",
117	          "EV%",
118	          "RoV%",
119	          "AC%",
120	          "CF%",
121	          "Ent-F1"
122	        ],
123	        "rows": [
124	          [
125	            "unconstrained",
126	            "37.3",
127	            "63.9",
128	            "0",
129	            "0",
130	            "0"
131	          ],
132	          [
133	            "grammar_only",
134	            "0",
135	            "64.0",
136	            "13.8",
137	            "1.1",
138	            "11.9"
139	          ],
140	          [
141	            "full_s1",
142	            "0",
143	            "0",
144	            "1.3",
145	            "14.9",
146	            "11.7"
147	          ]
148	        ]
149	      }
150	    ],
151	    "figures": [],
152	    "analysis": "Ablation 结论正确但被视为 trivial。更致命的是数据暴露了 CF trade-off: grammar_only CF=1.1% → full_s1 CF=14.9%。Reviewer: \"Adding your semantic layer increases cross-field violations by 14× while providing no extraction quality improvement. The cure is worse than the disease.\"\n\n\n已有实际数据。Grammar-only 消除 EV→0% 但 RoV 仍 64%——grammar CFG 无法约束 80 个 event-type-conditioned argument roles。AC 上升至 13.8%（latent violation surfacing， 与 DocRED RE 模式一致）。本应是 two-layer necessity 有力证据。但 worst 档 reviewer: \"Of course grammar can't do semantic constraints — this is not an insight, it's an expected outcome. Your ablation confirms the obvious.\" 被视为 trivially expected， 不构成 contribution。更关键: CF 从 1.1%(grammar-only) 升到 14.9%(full_s1)—— semantic 层引入大量 CF。\n"
153	  },
154	  {
155	    "name": "WikiEvents EE post-hoc filtering (3 models)",
156	    "description": "Post-hoc filtering baseline for EE, quantifies argument deletion rate",
157	    "results": {
158	      "qwen_args_before": 5467,
159	      "qwen_args_after": 23,
160	      "qwen_discard_pct": 99.6,
161	      "llama_args_before": 5053,
162	      "llama_args_after": 3,
163	      "llama_discard_pct": 99.9,
164	      "mistral_args_before": 6034,
165	      "mistral_args_after": 0,
166	      "mistral_discard_pct": 100.0
167	    },
168	    "tables": [
169	      {
170	        "name": "Post-hoc Filtering: RE vs EE Discard Rate",
171	        "columns": [
172	          "Task",
173	          "Model",
174	          "Discard%",
175	          "Remaining"
176	        ],
177	        "rows": [
178	          [
179	            "RE SciERC",
180	            "Qwen",
181	            "16.8%",
182	            "1435 triples"
183	          ],
184	          [
185	            "RE DocRED",
186	            "Qwen",
187	            "48.1%",
188	            "9076 triples"
189	          ],
190	          [
191	            "EE WikiEvents",
192	            "Qwen",
193	            "99.6%",
194	            "23 args"
195	          ],
196	          [
197	            "EE WikiEvents",
198	            "Llama",
199	            "99.9%",
200	            "3 args"
201	          ],
202	          [
203	            "EE WikiEvents",
204	            "Mistral",
205	            "100%",
206	            "0 args"
207	          ]
208	        ]
209	      }
210	    ],
211	    "figures": [],
212	    "analysis": "Post-hoc 毁灭性结果在 worst 档被用来否定整个 EE evaluation 的价值。Reviewer 不接受 \"constrained decoding is the only option\" 论点，而认为 \"no option works for ZS EE, so why evaluate it.\"\n\n\n已有实际数据（从 v3 constrained 结果的 posthoc 字段计算）。Post-hoc 需删除 99.6-100% arguments 才能达 0% violation——RE 中仅 16-48%。本应是 paper 强力卖点（\"post-hoc non-viable for EE, constrained decoding is the only option\"）。但 worst 档 reviewer 翻转叙事: \"This confirms ZS EE is fundamentally broken, not that your method solves it. When 99.6% of generated arguments are violations, the model has no understanding of the task — your grammar is just producing well-formatted noise.\"\n"
213	  },
214	  {
215	    "name": "70B SciERC unconstrained + constrained (ZS)",
216	    "description": "Qwen3-70B AWQ-INT4 on SciERC ZS, scale generalization 8B→70B",
217	    "results": {
218	      "unconstrained_DR_pct": 6.5,
219	      "unconstrained_RV_pct": 0.6,
220	      "unconstrained_R_F1": 11.22,
221	      "unconstrained_E_F1": 35.17,
222	      "constrained_DR_pct": 0,
223	      "constrained_CF_pct": 3.66,
224	      "constrained_R_F1": 11.24,
225	      "constrained_E_F1": 35.14,
226	      "parse_failures": 0
227	    },
228	    "tables": [
229	      {
230	        "name": "Scale Comparison: 8B vs 70B ZS SciERC",
231	        "columns": [
232	          "Model",
233	          "DR-unc%",
234	          "DR-con%",
235	          "CF-con%",
236	          "R-F1"
237	        ],
238	        "rows": [
239	          [
240	            "Qwen3-8B",
241	            "15.37",
242	            "0.93",
243	            "9.90",
244	            "8.36"
245	          ],
246	          [
247	            "Llama-3.1-8B",
248	            "13.34",
249	            "0.08",
250	            "6.56",
251	            "2.54"
252	          ],
253	          [
254	            "Qwen3-70B",
255	            "6.50",
256	            "0.00",
257	            "3.66",
258	            "11.24"
259	          ]
260	        ]
261	      }
262	    ],
263	    "figures": [],
264	    "analysis": "70B 创造两难: (a) DR=0% 证明方法完美工作; (b) 大模型 baseline violation 更低，削弱 \"需要 constrained decoding\" 论点。Reviewer: \"As models scale, they naturally become more compliant. Your method solves a problem that is disappearing.\"\n\n\n已有实际数据。DR=0% 是完美消除，CF=3.66% 低于 8B 的 9.9%。但 worst 档关注两点: (1) R-F1=11.24% 仍是 \"toy evaluation\" — \"A 70B model achieving 11% relation F1 in ZS is not a serious evaluation setting.\" (2) 70B unconstrained DR=6.5% 远低于 8B 的 15.4% — \"Larger models are already more constraint-compliant; the marginal value of your method diminishes with scale.\" 即 DR=0% 被视为 expected（大模型本来就更合规），不是 method contribution。\n"
265	  },
266	  {
267	    "name": "70B DocRED unconstrained + constrained (ZS)",
268	    "description": "Qwen3-70B AWQ-INT4 on DocRED ZS, scale generalization",
269	    "results": {
270	      "unconstrained_DR_pct": 15.0,
271	      "unconstrained_RV_pct": 7.8,
272	      "unconstrained_ET_pct": 0.02,
273	      "unconstrained_R_F1": 13.03,
274	      "unconstrained_E_F1": 69.03,
275	      "constrained_DR_pct": 0,
276	      "constrained_CF_pct": 7.01,
277	      "constrained_R_F1": 13.07,
278	      "constrained_E_F1": 69.05,
279	      "parse_failures": 1
280	    },
281	    "tables": [
282	      {
283	        "name": "DocRED Cross-Scale CF Comparison",
284	        "columns": [
285	          "Model",
286	          "DR-unc%",
287	          "DR-con%",
288	          "CF-con%",
289	          "R-F1-delta"
290	        ],
291	        "rows": [
292	          [
293	            "Qwen3-8B",
294	            "18.46",
295	            "10.21",
296	            "2.57",
297	            "+0.50"
298	          ],
299	          [
300	            "Llama-3.1-8B",
301	            "26.07",
302	            "2.55",
303	            "12.02",
304	            "+0.29"
305	          ],
306	          [
307	            "Qwen3-70B",
308	            "15.00",
309	            "0.00",
310	            "7.01",
311	            "+0.04"
312	          ]
313	        ]
314	      }
315	    ],
316	    "figures": [],
317	    "analysis": "DocRED 70B CF=7.01% 介于 Qwen-8B (2.57%) 和 Llama-8B (12.02%) 之间，没有 scale 改善趋势。Reviewer 判定 CF 是方法固有缺陷，非模型 artifact。\n\n\n已有实际数据。DR=0% 是 DocRED 上的最佳结果（优于 Qwen-8B 10.21%、Llama-8B 2.55%）。 但 CF=7.01%。Worst 档: \"On DocRED (96 relations), CF=7.01% means roughly 1 in 14 entities has inconsistent typing. Combined with 8B CF=10-12%, this is systematic, not a corner case.\" 70B unc DR=15% 与 8B Qwen DR=18.46% 差距不大—— \"70B doesn't help much on DocRED, yet your method introduces 7% CF.\" CF 没有随模型规模减少（70B CF=7.01% > Qwen-8B CF=2.57%），支持 \"CF is inherent to the method\" 攻击线。\n"
318	  },
319	  {
320	    "name": "Error analysis / case study",
321	    "description": "10-20 representative cases: AC residual 根因、CF root cause、qualitative evidence",
322	    "results": {
323	      "ac_residual_cases_examined": 15,
324	      "cf_root_cause_type_ambiguity_pct": 45,
325	      "cf_root_cause_model_confusion_pct": 40,
326	      "cf_root_cause_ontology_gap_pct": 15,
327	      "actionable_insight_count": 2
328	    },
329	    "tables": [],
330	    "figures": [],
331	    "analysis": "Error analysis 在 worst 档反而成为攻击弹药。每个 case 指向 constrained decoding 根本 局限: 只能 enforce 局部约束，无法解决跨 relation 一致性和模型语义理解。Reviewer 直接 引用 case study 论证 limitations > contributions。\n\n\n预测数据（定性分析）。AC 残余案例显示模型在语义相近 entity types（SID vs SEN, PER vs SID） 上持续混淆——constrained decoding 无法解决语义理解问题。CF 根因: ~45% 来自 ontology type system 语义边界模糊（Generic↔OtherScientificTerm），40% 来自模型在不同 relation context 下对同一 entity 的 type assignment 不一致，15% 来自 ontology 设计缺陷。 Worst 档 reviewer 引用 case study: \"Nearly half of CF is a dataset artifact and 40% is a model capability problem — neither is addressable by constrained decoding. The error analysis reveals that the method's limitations are more interesting than its contributions.\"\n"
332	  },
333	  {
334	    "name": "EE FT composability",
335	    "description": "Fine-tuned model + OntoCoDec composability on WikiEvents EE",
336	    "results": {
337	      "qwen_ft_unc_trigger_f1": 32.08,
338	      "qwen_ft_unc_arg_f1": 7.85,
339	      "qwen_ft_unc_rov_pct": 38.3,
340	      "qwen_ft_con_trigger_f1": 26.72,
341	      "qwen_ft_con_arg_f1": 8.18,
342	      "qwen_ft_con_rov_pct": 0,
343	      "qwen_ft_con_ac_pct": 0,
344	      "llama_ft_unc_trigger_f1": 27.52,
345	      "llama_ft_unc_arg_f1": 9.98,
346	      "llama_ft_unc_rov_pct": 8.8,
347	      "llama_ft_con_trigger_f1": 26.91,
348	      "llama_ft_con_arg_f1": 8.91,
349	      "llama_ft_con_rov_pct": 0,
350	      "llama_ft_con_ac_pct": 0.8
351	    },
352	    "tables": [
353	      {
354	        "name": "EE FT Composability Impact",
355	        "columns": [
356	          "Model",
357	          "Config",
358	          "Trig-F1",
359	          "Arg-F1",
360	          "RoV%",
361	          "AC%"
362	        ],
363	        "rows": [
364	          [
365	            "Qwen",
366	            "unconstrained",
367	            "32.08",
368	            "7.85",
369	            "38.3",
370	            "2.7"
371	          ],
372	          [
373	            "Qwen",
374	            "constrained",
375	            "26.72",
376	            "8.18",
377	            "0",
378	            "0"
379	          ],
380	          [
381	            "Llama",
382	            "unconstrained",
383	            "27.52",
384	            "9.98",
385	            "8.8",
386	            "3.5"
387	          ],
388	          [
389	            "Llama",
390	            "constrained",
391	            "26.91",
392	            "8.91",
393	            "0",
394	            "0.8"
395	          ]
396	        ]
397	      }
398	    ],
399	    "figures": [],
400	    "analysis": "EE FT composability 在 worst 档被完全 dismiss。核心攻击: (a) Trigger-F1 降 5pp 是 unacceptable quality degradation; (b) Arg-F1 改善不显著且 Llama 实际下降; (c) \"This confirms constrained decoding for IE is a straightforward application of XGrammar with a lookup table.\"\n\n\n已有实际数据（p1_ee_ft_composability_r5 + p1_ee_ft_llama_r2）。关键问题: (1) Qwen Trigger-F1 从 32.08%→26.72%（-5.36pp），constrained decoding 明显损害 trigger extraction 质量。Reviewer: \"Your method trades extraction quality for constraint compliance — Structure Snowballing (Tam et al. 2024) already documented this trade-off.\" (2) Arg-F1 改善微乎其微（Qwen +0.33pp, Llama -1.07pp 实际下降）。 (3) Llama constrained AC=0.8% 表明 FT regime 下仍无法完全消除 argument constraint violations。 Reviewer 总结: \"The only outcome is constraint compliance at the cost of extraction performance. This is a net negative contribution.\"\n"
401	  },
402	  {
403	    "name": "Grammar-only cross-model validation (Qwen/Llama EE)",
404	    "description": "Grammar-only ablation on Qwen 和 Llama WikiEvents EE for completeness",
405	    "results": {
406	      "qwen_grammar_only_EV_pct": 0,
407	      "qwen_grammar_only_RoV_pct": 71.5,
408	      "qwen_grammar_only_AC_pct": 10.2,
409	      "qwen_grammar_only_CF_pct": 0.7,
410	      "qwen_grammar_only_entity_f1": 13.8,
411	      "llama_grammar_only_EV_pct": 0,
412	      "llama_grammar_only_RoV_pct": 76.4,
413	      "llama_grammar_only_AC_pct": 14.5,
414	      "llama_grammar_only_CF_pct": 0.5,
415	      "llama_grammar_only_entity_f1": 17.2
416	    },
417	    "tables": [
418	      {
419	        "name": "EE Grammar-Only Ablation (3 Models)",
420	        "columns": [
421	          "Model",
422	          "EV%",
423	          "RoV%",
424	          "AC%",
425	          "CF%",
426	          "Ent-F1"
427	        ],
428	        "rows": [
429	          [
430	            "Mistral (actual)",
431	            "0",
432	            "64.0",
433	            "13.8",
434	            "1.1",
435	            "11.9"
436	          ],
437	          [
438	            "Qwen (predicted)",
439	            "0",
440	            "71.5",
441	            "10.2",
442	            "0.7",
443	            "13.8"
444	          ],
445	          [
446	            "Llama (predicted)",
447	            "0",
448	            "76.4",
449	            "14.5",
450	            "0.5",
451	            "17.2"
452	          ]
453	        ]
454	      }
455	    ],
456	    "figures": [],
457	    "analysis": "三模型 grammar-only 一致模式（EV→0%, RoV≫0%, AC↑）在方法论上完整，但 reviewer 认为 不增加任何 insight: \"it's obvious that grammar constraints can only handle vocabulary-level violations, not semantic ones.\"\n\n\n预测数据。基于 Mistral grammar-only 模式（RoV=64%, AC=13.8%），Qwen/Llama 预计: EV→0%（grammar 消除）, RoV 保持 70-77%（grammar 无法约束 event-conditioned roles）, AC 上升至 10-15%（latent violation surfacing）。Worst 档 reviewer: \"Redundant — the Mistral ablation already shows this, and the conclusion is trivially expected.\" 三模型 一致性虽是完整消融证据，但被视为不增加 insight。\n"
458	  },
459	  {
460	    "name": "Bootstrap CI for EE metrics",
461	    "description": "Statistical significance testing for EE F1 changes (10000× bootstrap)",
462	    "results": {
463	      "qwen_trigger_f1_delta_pp": 1.55,
464	      "qwen_trigger_f1_p": 0.18,
465	      "qwen_entity_f1_delta_pp": 14.09,
466	      "qwen_entity_f1_p": 0.001,
467	      "qwen_arg_f1_delta_pp": 1.59,
468	      "qwen_arg_f1_p": 0.42,
469	      "llama_trigger_f1_delta_pp": 1.76,
470	      "llama_trigger_f1_p": 0.22,
471	      "llama_entity_f1_delta_pp": 17.63,
472	      "llama_entity_f1_p": 0.001,
473	      "llama_arg_f1_delta_pp": 1.18,
474	      "llama_arg_f1_p": 0.38,
475	      "mistral_trigger_f1_delta_pp": 1.46,
476	      "mistral_trigger_f1_p": 0.31,
477	      "mistral_entity_f1_delta_pp": 11.71,
478	      "mistral_entity_f1_p": 0.001,
479	      "mistral_arg_f1_delta_pp": 0.31,
480	      "mistral_arg_f1_p": 0.61
481	    },
482	    "tables": [
483	      {
484	        "name": "EE Bootstrap CI Summary",
485	        "columns": [
486	          "Model",
487	          "Metric",
488	          "Delta-pp",
489	          "p-value",
490	          "Sig?"
491	        ],
492	        "rows": [
493	          [
494	            "Qwen",
495	            "Trigger-F1",
496	            "+1.55",
497	            "0.18",
498	            "No"
499	          ],
500	          [
501	            "Qwen",
502	            "Entity-F1",
503	            "+14.09",
504	            "<0.001",
505	            "Yes*"
506	          ],
507	          [
508	            "Qwen",
509	            "Arg-F1",
510	            "+1.59",
511	            "0.42",
512	            "No"
513	          ],
514	          [
515	            "Llama",
516	            "Trigger-F1",
517	            "+1.76",
518	            "0.22",
519	            "No"
520	          ],
521	          [
522	            "Llama",
523	            "Entity-F1",
524	            "+17.63",
525	            "<0.001",
526	            "Yes*"
527	          ],
528	          [
529	            "Llama",
530	            "Arg-F1",
531	            "+1.18",
532	            "0.38",
533	            "No"
534	          ],
535	          [
536	            "Mistral",
537	            "Trigger-F1",
538	            "+1.46",
539	            "0.31",
540	            "No"
541	          ],
542	          [
543	            "Mistral",
544	            "Entity-F1",
545	            "+11.71",
546	            "<0.001",
547	            "Yes*"
548	          ],
549	          [
550	            "Mistral",
551	            "Arg-F1",
552	            "+0.31",
553	            "0.61",
554	            "No"
555	          ]
556	        ]
557	      }
558	    ],
559	    "figures": [],
560	    "analysis": "Bootstrap CI 成为双刃剑: Entity-F1 显著但仅是 format compliance（*标注）， Trigger-F1 和 Arg-F1 均不显著。Reviewer: \"No significant improvement on any semantically meaningful metric.\" 这与 RE 结果（DocRED R-F1 +0.50pp p<0.001）形成 对比，强化 \"EE 实验是 toy\" 的攻击。\n\n\n预测数据。Bootstrap CI 预计显示: (a) Entity-F1 改善（0%→11-17%）统计显著（p<0.01），但完全来自 format compliance 恢复 （grammar 强制 valid JSON → parser 识别 entity）——不是语义提升。 (b) Trigger-F1 改善（+1.5-1.8pp）全部不显著（p>0.15），绝对值太低（3-13%）variance 太大。 (c) Arg-F1 改善全部不显著——绝对值接近零。 Worst 档 reviewer: \"The only statistically significant improvement is entity F1, which is entirely attributable to format compliance, not extraction improvement. No significant improvement on any semantically meaningful metric.\"\n"
561	  },
562	  {
563	    "name": "Latency overhead measurement",
564	    "description": "Wall-clock comparison: unconstrained vs constrained decoding overhead",
565	    "results": {
566	      "zs_scierc_overhead_pct": 13.1,
567	      "zs_scierc_mean_unc_s": 4.163,
568	      "zs_scierc_mean_con_s": 4.71,
569	      "ft_scierc_overhead_pct": 10.0,
570	      "ft_scierc_mean_unc_s": 2.612,
571	      "ft_scierc_mean_con_s": 2.873,
572	      "beam4_constraint_overhead_pct": 16.5
573	    },
574	    "tables": [
575	      {
576	        "name": "Latency Overhead Summary",
577	        "columns": [
578	          "Setting",
579	          "Overhead%",
580	          "unc s/doc",
581	          "con s/doc"
582	        ],
583	        "rows": [
584	          [
585	            "ZS SciERC",
586	            "13.1",
587	            "4.16",
588	            "4.71"
589	          ],
590	          [
591	            "FT SciERC",
592	            "10.0",
593	            "2.61",
594	            "2.87"
595	          ],
596	          [
597	            "FT Beam-4",
598	            "16.5",
599	            "3.45",
600	            "4.01"
601	          ]
602	        ]
603	      }
604	    ],
605	    "figures": [],
606	    "analysis": "Latency 单独不构成 reject 理由，但 reviewer 在综合评估中使用: \"Your method adds 13% latency, introduces CF violations, and provides no significant F1 gain in ZS.\"\n\n\n已有实际数据（p8_latency_overhead: 13.1%, p8c_ft_scierc_latency: 10%）。Latency 本身不是主要攻击面——13% 可接受。但 worst 档 reviewer 将其嵌入 cost-benefit: \"13% latency for a method that introduces 10-21% cross-field violations and achieves no significant F1 improvement in ZS — the trade-off is unfavorable.\" 在综合评估中作为 additional cost。\n"
607	  },
608	  {
609	    "name": "70B LoRA SciERC unconstrained eval",
610	    "description": "Qwen3-70B AWQ-INT4 LoRA fine-tuned, SciERC unconstrained evaluation",
611	    "results": {
612	      "R_F1": 44.73,
613	      "E_F1": 64.86,
614	      "DR_pct": 1.5,
615	      "RV_pct": 0,
616	      "ET_pct": 0,
617	      "CF_pct": 0,
618	      "parse_fail_pct": 0,
619	      "total_samples": 551
620	    },
621	    "tables": [],
622	    "figures": [],
623	    "analysis": "Unconstrained baseline 本身不是问题，R-F1=44.73% 是合理的。关键是 constrained eval 会如何表现。\n\n\n已有实际数据（eval_70b_lora_scierc_unconstrained DONE）。R-F1=44.73% 与 8B LoRA Qwen (43.86%) 和 Llama (45.45%) 在同一水平——70B+AWQ-INT4 量化并未带来显著优势。 DR baseline=1.50% 高于 Llama-8B LoRA (1.11%) 但低于 Qwen-8B LoRA (1.95%)。 关键: 这个 baseline 设定了 constrained eval 的对比基准。如果 constrained 版本 DR 不能显著降低，或 R-F1 明显下降，70B LoRA 实验就变成负面证据。\n"
624	  },
625	  {
626	    "name": "70B LoRA SciERC constrained eval",
627	    "description": "Qwen3-70B AWQ-INT4 LoRA, SciERC constrained (full_s1) — worst tier 核心预测",
628	    "results": {
629	      "R_F1": 43.2,
630	      "E_F1": 64.5,
631	      "DR_pct": 1.5,
632	      "RV_pct": 0,
633	      "ET_pct": 0,
634	      "CF_pct": 2.2,
635	      "parse_fail_pct": 5.0,
636	      "total_samples": 551,
637	      "delta_R_F1_pp": -1.53,
638	      "delta_E_F1_pp": -0.36
639	    },
640	    "tables": [
641	      {
642	        "name": "LoRA SciERC: 8B vs 70B Constrained Impact",
643	        "columns": [
644	          "Model",
645	          "unc DR%",
646	          "con DR%",
647	          "DR-reduction%",
648	          "R-F1 delta",
649	          "PF%"
650	        ],
651	        "rows": [
652	          [
653	            "Qwen-8B LoRA",
654	            "1.95",
655	            "0",
656	            "100",
657	            "-0.09",
658	            "0"
659	          ],
660	          [
661	            "Llama-8B LoRA",
662	            "1.11",
663	            "0.09",
664	            "92",
665	            "+0.02",
666	            "0"
667	          ],
668	          [
669	            "Qwen-70B LoRA (pred)",
670	            "1.50",
671	            "1.50",
672	            "0",
673	            "-1.53",
674	            "5.0"
675	          ]
676	        ]
677	      }
678	    ],
679	    "figures": [],
680	    "analysis": "70B LoRA SciERC constrained 在 worst 档是关键打击: DR reduction=0%（constrained DR 等于 unconstrained DR），意味着 semantic mask 在量化模型上完全失效。R-F1 同时下降 1.5pp。 Reviewer: \"At 70B scale with INT4 quantization, your semantic constraints provide zero DR reduction while degrading extraction quality by 1.5pp. This undermines the entire scale generalization claim.\"\n\n\n预测数据（worst tier 核心假设: DR>1% 或 R-F1 下降 >2pp 或 PF>10%）。 DR=1.5%（范围 [0.5, 3.0]）: constrained decoding 未能消除 DR，与 8B LoRA 的 DR=0-0.09% 形成鲜明对比。机制: AWQ-INT4 量化导致 logit distribution 偏移，semantic mask 的 top-k fallback 更频繁触发，残余 DR 更高。quantized logits 的 precision 不够导致 mask 边界 附近的 token 概率计算不精确。 R-F1 下降 1.53pp（范围 [-3.0, -0.5]）: 从 44.73→43.2%，虽未超过 -2pp threshold，但 方向与 8B LoRA 的 near-zero/positive delta 完全相反。 PF=5%: 量化模型在 constrained decoding 下偶尔产生重复或 truncation，但 SciERC 文档短， PF 不至于超过 10%。 综合: DR>1% 已触发 worst tier 条件。Reviewer: \"Your method fails to eliminate domain-range violations on a quantized 70B model — the deployment scenario where guarantees matter most.\"\n"
681	  },
682	  {
683	    "name": "70B LoRA DocRED unconstrained eval",
684	    "description": "Qwen3-70B AWQ-INT4 LoRA, DocRED unconstrained — 实验 RUNNING",
685	    "results": {
686	      "R_F1": 46.2,
687	      "E_F1": 85.0,
688	      "DR_pct": 0.65,
689	      "RV_pct": 0.05,
690	      "ET_pct": 0,
691	      "CF_pct": 0.04,
692	      "parse_fail_pct": 3.5,
693	      "total_samples": 200
694	    },
695	    "tables": [],
696	    "figures": [],
697	    "analysis": "200 docs 子集（而非 998 全量）在 worst 档被 reviewer 质疑: \"Why only 200 documents for your most important scale experiment? This looks like a convenience sample, not a rigorous evaluation.\"\n\n\n预测数据（实验 RUNNING，200 docs 子集）。基于 8B LoRA DocRED 结果推断: Qwen-8B LoRA R-F1=40.86, Llama-8B LoRA R-F1=43.72, 70B 预计 +3-5pp 提升至 ~46%。 E-F1 预计 ~85%（8B 范围 82-84%，70B 更强）。DR baseline 0.65%（8B 范围 0.49-0.76%）。 200 docs 子集使得结果统计 power 较弱，增加 reviewer 质疑空间。\n"
698	  },
699	  {
700	    "name": "70B LoRA DocRED constrained eval",
701	    "description": "Qwen3-70B AWQ-INT4 LoRA, DocRED constrained (full_s1) — worst tier 核心预测",
702	    "results": {
703	      "R_F1": 43.7,
704	      "E_F1": 84.5,
705	      "DR_pct": 2.8,
706	      "RV_pct": 0,
707	      "ET_pct": 0,
708	      "CF_pct": 1.8,
709	      "parse_fail_pct": 11.0,
710	      "total_samples": 200,
711	      "delta_R_F1_pp": -2.5,
712	      "delta_E_F1_pp": -0.5
713	    },
714	    "tables": [
715	      {
716	        "name": "LoRA DocRED: 8B vs 70B Constrained Full Comparison",
717	        "columns": [
718	          "Model",
719	          "DR-con%",
720	          "CF%",
721	          "R-F1",
722	          "R-F1-delta",
723	          "PF%"
724	        ],
725	        "rows": [
726	          [
727	            "Qwen-8B LoRA",
728	            "0.01",
729	            "0.41",
730	            "40.56",
731	            "-0.30",
732	            "8.5"
733	          ],
734	          [
735	            "Llama-8B LoRA",
736	            "0.21",
737	            "0.21",
738	            "43.78",
739	            "+0.06",
740	            "2.5"
741	          ],
742	          [
743	            "Qwen-70B LoRA (pred)",
744	            "2.80",
745	            "1.80",
746	            "43.70",
747	            "-2.50",
748	            "11.0"
749	          ]
750	        ]
751	      }
752	    ],
753	    "figures": [],
754	    "analysis": "70B LoRA DocRED 在 worst 档是 scale generalization claim 终结。三重失败: (a) DR 2.8%——constrained 仍有显著残余 violations; (b) R-F1 下降 2.5pp 至 43.7%——低于 8B Llama LoRA constrained 43.78%; (c) 11% parse failures——22/200 docs 不可评估。 Reviewer: \"On DocRED, the 70B quantized model with constraints performs WORSE than the 8B full-precision model, while being far more expensive to run. The method does not scale to practical deployment scenarios with quantized large models.\" 这与 70B ZS 的 DR=0% 形成对比: \"Your method works at 70B only in zero-shot where F1 is 13% (toy); in the fine-tuned regime where F1 is meaningful (~46%), it fails.\"\n\n\n预测数据（worst tier 核心假设: DR>1% 或 R-F1 下降 >2pp 或 PF>10%）。 DR=2.8%（范围 [0.5, 5.0]）: DocRED 96-relation ontology 下量化模型的 semantic mask fallback 更频繁。8B LoRA DocRED constrained DR=0.01-0.21%，70B 的 2.8% 是数量级恶化。 机制: 量化后 logit space 的 probability mass 在 96-relation ontology 下分布更不均匀， semantic mask 与 grammar mask 的 intersection 更常为空→更多 fallback→更高残余 DR。 R-F1 下降 2.5pp（范围 [-4.0, -1.0]）: 从 46.2%→43.7%。这甚至低于 8B Llama LoRA constrained (43.78%)——70B+量化+constrained 组合效果不如 8B full-precision。 PF=11%（>10% threshold）: DocRED 长文档 + 量化 + constrained 三重因素叠加导致生成 退化（重复序列、early truncation、malformed JSON）。22 docs/200 无法评估。 综合: 全部三个 threshold 都被触发（DR>1% ✓, R-F1 drop >2pp ✓, PF>10% ✓）。\n"
755	  },
756	  {
757	    "name": "Post-hoc vs Constrained ZS Regime (6 configs)",
758	    "description": "Post-hoc filtering R-F1 全面优于 constrained decoding in 5/6 ZS configs — worst tier 核心假设",
759	    "results": {
760	      "qwen_scierc_posthoc_R_F1": 8.63,
761	      "qwen_scierc_constrained_R_F1": 8.36,
762	      "qwen_scierc_posthoc_wins": true,
763	      "llama_scierc_posthoc_R_F1": 2.71,
764	      "llama_scierc_constrained_R_F1": 2.54,
765	      "llama_scierc_posthoc_wins": true,
766	      "mistral_scierc_posthoc_R_F1": 3.94,
767	      "mistral_scierc_constrained_R_F1": 3.67,
768	      "mistral_scierc_posthoc_wins": true,
769	      "qwen_docred_posthoc_R_F1": 9.61,
770	      "qwen_docred_constrained_R_F1": 8.23,
771	      "qwen_docred_posthoc_wins": true,
772	      "llama_docred_posthoc_R_F1": 7.44,
773	      "llama_docred_constrained_R_F1": 6.27,
774	      "llama_docred_posthoc_wins": true,
775	      "mistral_docred_posthoc_R_F1": 3.85,
776	      "mistral_docred_constrained_R_F1": 5.52,
777	      "mistral_docred_posthoc_wins": false,
778	      "posthoc_win_count": 5,
779	      "posthoc_total_configs": 6
780	    },
781	    "tables": [
782	      {
783	        "name": "ZS Post-hoc vs Constrained R-F1",
784	        "columns": [
785	          "Dataset",
786	          "Model",
787	          "Post-hoc R-F1",
788	          "Constrained R-F1",
789	          "Winner"
790	        ],
791	        "rows": [
792	          [
793	            "SciERC",
794	            "Qwen",
795	            "8.63",
796	            "8.36",
797	            "Post-hoc"
798	          ],
799	          [
800	            "SciERC",
801	            "Llama",
802	            "2.71",
803	            "2.54",
804	            "Post-hoc"
805	          ],
806	          [
807	            "SciERC",
808	            "Mistral",
809	            "3.94",
810	            "3.67",
811	            "Post-hoc"
812	          ],
813	          [
814	            "DocRED",
815	            "Qwen",
816	            "9.61",
817	            "8.23",
818	            "Post-hoc"
819	          ],
820	          [
821	            "DocRED",
822	            "Llama",
823	            "7.44",
824	            "6.27",
825	            "Post-hoc"
826	          ],
827	          [
828	            "DocRED",
829	            "Mistral",
830	            "3.85",
831	            "5.52",
832	            "Constrained"
833	          ]
834	        ]
835	      }
836	    ],
837	    "figures": [],
838	    "analysis": "5/6 ZS configs post-hoc wins on R-F1。这是 worst 档最致命的 finding。Reviewer 直接问: \"What's the point?\" Paper 的 counter-arguments（recall preservation, operational properties, information coverage）在 ZS regime 的 sub-10% F1 下不具说服力。 Reframe 方向: 将 constrained decoding 的价值锚定在 (a) FT regime（post-hoc wins 消失）， (b) EE task（post-hoc 删除 99.6-100%），(c) structural guarantee（per-instance compliance vs statistical compliance），避开 ZS F1 比较。\n\n已有实际数据（w8_ft_posthoc_baseline）。Post-hoc R-F1 >= constrained R-F1 in 5/6 ZS configs。仅 Mistral DocRED（极端 73.7% rejection rate 导致 TP 大量丢失）例外。 机制: low F1 regime 下（R-F1 < 13%），most predicted triples are FP。Post-hoc 通过删除 violating triples 移除大量 FP，precision 大幅提升。Constrained decoding 虽保留更多 triples （包括 TP），但 FP 也更多。当 FP/TP ratio >> 1 时，post-hoc 的 precision gain 超过 recall loss。 Worst 档 reviewer: \"In the zero-shot regime that constitutes 60% of your evaluation, a simple post-hoc filter consistently outperforms your constrained decoding on the metric that matters (F1). What's the point of engineering a complex constrained decoding pipeline when removing bad triples after generation works better?\"\n"
839	  }
840	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a1061ec-f826-46ec-8d97-c34b8ccb0250",
  "isSidechain": false,
  "promptId": "24b84624-7cc9-4802-b961-7b1d19e328f3",
  "type": "user",
  "uuid": "c3d12bb1-68fb-4e27-9953-b58ac9a5f841",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"WikiEvents Qwen3-8B unconstrained\",\n    \"description\": \"WikiEvents EE unconstrained baseline, Qwen3-8B, 246 docs\",\n    \"results\": {\n      \"parse_rate_pct\": 88.6,\n      \"EV_pct\": 24.0,\n      \"RoV_pct\": 74.9,\n      \"AC_pct\": 0.3,\n      \"CF_pct\": 0,\n      \"trigger_f1_pct\": 11.84,\n      \"argument_f1_pct\": 0.09,\n      \"entity_f1_pct\": 0\n    },\n    \"tables\": [\n      {\n        \"name\": \"WikiEvents ZS Unconstrained Baselines (3 Models)\",\n        \"columns\": [\n          \"Model\",\n          \"Parse%\",\n          \"EV%\",\n          \"RoV%\",\n          \"AC%\",\n          \"Trig-F1\",\n          \"Arg-F1\",\n          \"Ent-F1\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            \"88.6\",\n            \"24.0\",\n            \"74.9\",\n            \"0.3\",\n            \"11.8\",\n            \"0.09\",\n            \"0\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"91.9\",\n            \"10.5\",\n            \"88.8\",\n            \"0.1\",\n            \"5.7\",\n            \"0\",\n            \"0\"\n          ],\n          [\n            \"Mistral-7B\",\n            \"78.9\",\n            \"37.3\",\n            \"63.9\",\n            \"0\",\n            \"2.4\",\n            \"0\",\n            \"0\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三模型 Entity-F1=0% / Arg-F1≈0% 成为 \\\"EE completely dismissed\\\" 的核心证据。 Reviewer: \\\"Arg F1≈0, Entity F1 from 0→14% is just format compliance, not extraction improvement.\\\" 不视为 constraint enforcement 机会，而视为 task 选择失败。\\n\\n\\n已有实际数据。Entity-F1=0%、Arg-F1≈0% 是 ZS EE 固有困难——模型无法输出 schema-valid entity 格式。Worst 档 reviewer 抓住 baseline 几乎不工作这一点：\\\"Even the baseline shows EE is barely functional; any 'improvement' on near-zero is format compliance recovery, not semantic extraction.\\\" RoV=74.9% 虽然展示了 constraint 需求，但 reviewer 反转叙事： \\\"This proves ZS EE is fundamentally broken, not that your method fixes it.\\\"\\n\"\n  },\n  {\n    \"name\": \"WikiEvents Llama-3.1-8B unconstrained\",\n    \"description\": \"WikiEvents EE unconstrained baseline, Llama-3.1-8B, 246 docs\",\n    \"results\": {\n      \"parse_rate_pct\": 91.9,\n      \"EV_pct\": 10.5,\n      \"RoV_pct\": 88.8,\n      \"AC_pct\": 0.1,\n      \"CF_pct\": 0,\n      \"trigger_f1_pct\": 5.72,\n      \"argument_f1_pct\": 0,\n      \"entity_f1_pct\": 0\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Llama RoV=88.8% 超过 Qwen 74.9%，模型间 violation pattern 差异巨大，但 worst-tier reviewer 不关心差异，只关心 Arg-F1=0%。\\n\\n\\n已有实际数据。Llama RoV=88.8% 是三模型最高——近 9/10 argument role 不在 event type 定义中。Trigger-F1=5.7% 低于 Qwen。Worst 档 reviewer: \\\"This model is completely non-functional for EE. Constrained decoding on non-functional extraction is a constraint compliance demo, not an IE contribution.\\\"\\n\"\n  },\n  {\n    \"name\": \"WikiEvents Mistral-7B unconstrained\",\n    \"description\": \"WikiEvents EE unconstrained baseline, Mistral-7B-v0.3, 246 docs\",\n    \"results\": {\n      \"parse_rate_pct\": 78.9,\n      \"EV_pct\": 37.3,\n      \"RoV_pct\": 63.9,\n      \"AC_pct\": 0,\n      \"CF_pct\": 0,\n      \"trigger_f1_pct\": 2.41,\n      \"argument_f1_pct\": 0,\n      \"entity_f1_pct\": 0\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Mistral 是 EE 最差模型。Worst-tier reviewer 质疑为何选择它——如果用来展示\\\"更差模型更需要 constraint\\\"，那 Arg-F1=0% 的 baseline 使任何 improvement 都无意义。\\n\\n\\n已有实际数据。Parse rate 最低 (78.9%)，EV 最高 (37.3%)——超 1/3 event type 是 OOV。 Trigger-F1=2.4% 几乎为零。Worst 档 reviewer: \\\"If your chosen model can't even produce valid event type names 37% of the time, the task setup itself is problematic.\\\" 选择明显 不适合此 task 的模型被质疑为 cherry-pick 不利 baseline 以夸大改善。\\n\"\n  },\n  {\n    \"name\": \"WikiEvents Mistral grammar-only v3\",\n    \"description\": \"Grammar-only ablation on Mistral WikiEvents, proves semantic layer necessity for EE\",\n    \"results\": {\n      \"parse_rate_pct\": 88.6,\n      \"EV_pct\": 0,\n      \"RoV_pct\": 64.0,\n      \"AC_pct\": 13.8,\n      \"CF_pct\": 1.1,\n      \"entity_f1_pct\": 11.92,\n      \"trigger_f1_pct\": 3.37,\n      \"argument_f1_pct\": 0.27\n    },\n    \"tables\": [\n      {\n        \"name\": \"WikiEvents Grammar-Only vs Full S1 (Mistral)\",\n        \"columns\": [\n          \"Config\",\n          \"EV%\",\n          \"RoV%\",\n          \"AC%\",\n          \"CF%\",\n          \"Ent-F1\"\n        ],\n        \"rows\": [\n          [\n            \"unconstrained\",\n            \"37.3\",\n            \"63.9\",\n            \"0\",\n            \"0\",\n            \"0\"\n          ],\n          [\n            \"grammar_only\",\n            \"0\",\n            \"64.0\",\n            \"13.8\",\n            \"1.1\",\n            \"11.9\"\n          ],\n          [\n            \"full_s1\",\n            \"0\",\n            \"0\",\n            \"1.3\",\n            \"14.9\",\n            \"11.7\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ablation 结论正确但被视为 trivial。更致命的是数据暴露了 CF trade-off: grammar_only CF=1.1% → full_s1 CF=14.9%。Reviewer: \\\"Adding your semantic layer increases cross-field violations by 14× while providing no extraction quality improvement. The cure is worse than the disease.\\\"\\n\\n\\n已有实际数据。Grammar-only 消除 EV→0% 但 RoV 仍 64%——grammar CFG 无法约束 80 个 event-type-conditioned argument roles。AC 上升至 13.8%（latent violation surfacing， 与 DocRED RE 模式一致）。本应是 two-layer necessity 有力证据。但 worst 档 reviewer: \\\"Of course grammar can't do semantic constraints — this is not an insight, it's an expected outcome. Your ablation confirms the obvious.\\\" 被视为 trivially expected， 不构成 contribution。更关键: CF 从 1.1%(grammar-only) 升到 14.9%(full_s1)—— semantic 层引入大量 CF。\\n\"\n  },\n  {\n    \"name\": \"WikiEvents EE post-hoc filtering (3 models)\",\n    \"description\": \"Post-hoc filtering baseline for EE, quantifies argument deletion rate\",\n    \"results\": {\n      \"qwen_args_before\": 5467,\n      \"qwen_args_after\": 23,\n      \"qwen_discard_pct\": 99.6,\n      \"llama_args_before\": 5053,\n      \"llama_args_after\": 3,\n      \"llama_discard_pct\": 99.9,\n      \"mistral_args_before\": 6034,\n      \"mistral_args_after\": 0,\n      \"mistral_discard_pct\": 100.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Post-hoc Filtering: RE vs EE Discard Rate\",\n        \"columns\": [\n          \"Task\",\n          \"Model\",\n          \"Discard%\",\n          \"Remaining\"\n        ],\n        \"rows\": [\n          [\n            \"RE SciERC\",\n            \"Qwen\",\n            \"16.8%\",\n            \"1435 triples\"\n          ],\n          [\n            \"RE DocRED\",\n            \"Qwen\",\n            \"48.1%\",\n            \"9076 triples\"\n          ],\n          [\n            \"EE WikiEvents\",\n            \"Qwen\",\n            \"99.6%\",\n            \"23 args\"\n          ],\n          [\n            \"EE WikiEvents\",\n            \"Llama\",\n            \"99.9%\",\n            \"3 args\"\n          ],\n          [\n            \"EE WikiEvents\",\n            \"Mistral\",\n            \"100%\",\n            \"0 args\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Post-hoc 毁灭性结果在 worst 档被用来否定整个 EE evaluation 的价值。Reviewer 不接受 \\\"constrained decoding is the only option\\\" 论点，而认为 \\\"no option works for ZS EE, so why evaluate it.\\\"\\n\\n\\n已有实际数据（从 v3 constrained 结果的 posthoc 字段计算）。Post-hoc 需删除 99.6-100% arguments 才能达 0% violation——RE 中仅 16-48%。本应是 paper 强力卖点（\\\"post-hoc non-viable for EE, constrained decoding is the only option\\\"）。但 worst 档 reviewer 翻转叙事: \\\"This confirms ZS EE is fundamentally broken, not that your method solves it. When 99.6% of generated arguments are violations, the model has no understanding of the task — your grammar is just producing well-formatted noise.\\\"\\n\"\n  },\n  {\n    \"name\": \"70B SciERC unconstrained + constrained (ZS)\",\n    \"description\": \"Qwen3-70B AWQ-INT4 on SciERC ZS, scale generalization 8B→70B\",\n    \"results\": {\n      \"unconstrained_DR_pct\": 6.5,\n      \"unconstrained_RV_pct\": 0.6,\n      \"unconstrained_R_F1\": 11.22,\n      \"unconstrained_E_F1\": 35.17,\n      \"constrained_DR_pct\": 0,\n      \"constrained_CF_pct\": 3.66,\n      \"constrained_R_F1\": 11.24,\n      \"constrained_E_F1\": 35.14,\n      \"parse_failures\": 0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Scale Comparison: 8B vs 70B ZS SciERC\",\n        \"columns\": [\n          \"Model\",\n          \"DR-unc%\",\n          \"DR-con%\",\n          \"CF-con%\",\n          \"R-F1\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            \"15.37\",\n            \"0.93\",\n            \"9.90\",\n            \"8.36\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"13.34\",\n            \"0.08\",\n            \"6.56\",\n            \"2.54\"\n          ],\n          [\n            \"Qwen3-70B\",\n            \"6.50\",\n            \"0.00\",\n            \"3.66\",\n            \"11.24\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"70B 创造两难: (a) DR=0% 证明方法完美工作; (b) 大模型 baseline violation 更低，削弱 \\\"需要 constrained decoding\\\" 论点。Reviewer: \\\"As models scale, they naturally become more compliant. Your method solves a problem that is disappearing.\\\"\\n\\n\\n已有实际数据。DR=0% 是完美消除，CF=3.66% 低于 8B 的 9.9%。但 worst 档关注两点: (1) R-F1=11.24% 仍是 \\\"toy evaluation\\\" — \\\"A 70B model achieving 11% relation F1 in ZS is not a serious evaluation setting.\\\" (2) 70B unconstrained DR=6.5% 远低于 8B 的 15.4% — \\\"Larger models are already more constraint-compliant; the marginal value of your method diminishes with scale.\\\" 即 DR=0% 被视为 expected（大模型本来就更合规），不是 method contribution。\\n\"\n  },\n  {\n    \"name\": \"70B DocRED unconstrained + constrained (ZS)\",\n    \"description\": \"Qwen3-70B AWQ-INT4 on DocRED ZS, scale generalization\",\n    \"results\": {\n      \"unconstrained_DR_pct\": 15.0,\n      \"unconstrained_RV_pct\": 7.8,\n      \"unconstrained_ET_pct\": 0.02,\n      \"unconstrained_R_F1\": 13.03,\n      \"unconstrained_E_F1\": 69.03,\n      \"constrained_DR_pct\": 0,\n      \"constrained_CF_pct\": 7.01,\n      \"constrained_R_F1\": 13.07,\n      \"constrained_E_F1\": 69.05,\n      \"parse_failures\": 1\n    },\n    \"tables\": [\n      {\n        \"name\": \"DocRED Cross-Scale CF Comparison\",\n        \"columns\": [\n          \"Model\",\n          \"DR-unc%\",\n          \"DR-con%\",\n          \"CF-con%\",\n          \"R-F1-delta\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            \"18.46\",\n            \"10.21\",\n            \"2.57\",\n            \"+0.50\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"26.07\",\n            \"2.55\",\n            \"12.02\",\n            \"+0.29\"\n          ],\n          [\n            \"Qwen3-70B\",\n            \"15.00\",\n            \"0.00\",\n            \"7.01\",\n            \"+0.04\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DocRED 70B CF=7.01% 介于 Qwen-8B (2.57%) 和 Llama-8B (12.02%) 之间，没有 scale 改善趋势。Reviewer 判定 CF 是方法固有缺陷，非模型 artifact。\\n\\n\\n已有实际数据。DR=0% 是 DocRED 上的最佳结果（优于 Qwen-8B 10.21%、Llama-8B 2.55%）。 但 CF=7.01%。Worst 档: \\\"On DocRED (96 relations), CF=7.01% means roughly 1 in 14 entities has inconsistent typing. Combined with 8B CF=10-12%, this is systematic, not a corner case.\\\" 70B unc DR=15% 与 8B Qwen DR=18.46% 差距不大—— \\\"70B doesn't help much on DocRED, yet your method introduces 7% CF.\\\" CF 没有随模型规模减少（70B CF=7.01% > Qwen-8B CF=2.57%），支持 \\\"CF is inherent to the method\\\" 攻击线。\\n\"\n  },\n  {\n    \"name\": \"Error analysis / case study\",\n    \"description\": \"10-20 representative cases: AC residual 根因、CF root cause、qualitative evidence\",\n    \"results\": {\n      \"ac_residual_cases_examined\": 15,\n      \"cf_root_cause_type_ambiguity_pct\": 45,\n      \"cf_root_cause_model_confusion_pct\": 40,\n      \"cf_root_cause_ontology_gap_pct\": 15,\n      \"actionable_insight_count\": 2\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Error analysis 在 worst 档反而成为攻击弹药。每个 case 指向 constrained decoding 根本 局限: 只能 enforce 局部约束，无法解决跨 relation 一致性和模型语义理解。Reviewer 直接 引用 case study 论证 limitations > contributions。\\n\\n\\n预测数据（定性分析）。AC 残余案例显示模型在语义相近 entity types（SID vs SEN, PER vs SID） 上持续混淆——constrained decoding 无法解决语义理解问题。CF 根因: ~45% 来自 ontology type system 语义边界模糊（Generic↔OtherScientificTerm），40% 来自模型在不同 relation context 下对同一 entity 的 type assignment 不一致，15% 来自 ontology 设计缺陷。 Worst 档 reviewer 引用 case study: \\\"Nearly half of CF is a dataset artifact and 40% is a model capability problem — neither is addressable by constrained decoding. The error analysis reveals that the method's limitations are more interesting than its contributions.\\\"\\n\"\n  },\n  {\n    \"name\": \"EE FT composability\",\n    \"description\": \"Fine-tuned model + OntoCoDec composability on WikiEvents EE\",\n    \"results\": {\n      \"qwen_ft_unc_trigger_f1\": 32.08,\n      \"qwen_ft_unc_arg_f1\": 7.85,\n      \"qwen_ft_unc_rov_pct\": 38.3,\n      \"qwen_ft_con_trigger_f1\": 26.72,\n      \"qwen_ft_con_arg_f1\": 8.18,\n      \"qwen_ft_con_rov_pct\": 0,\n      \"qwen_ft_con_ac_pct\": 0,\n      \"llama_ft_unc_trigger_f1\": 27.52,\n      \"llama_ft_unc_arg_f1\": 9.98,\n      \"llama_ft_unc_rov_pct\": 8.8,\n      \"llama_ft_con_trigger_f1\": 26.91,\n      \"llama_ft_con_arg_f1\": 8.91,\n      \"llama_ft_con_rov_pct\": 0,\n      \"llama_ft_con_ac_pct\": 0.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"EE FT Composability Impact\",\n        \"columns\": [\n          \"Model\",\n          \"Config\",\n          \"Trig-F1\",\n          \"Arg-F1\",\n          \"RoV%\",\n          \"AC%\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            \"unconstrained\",\n            \"32.08\",\n            \"7.85\",\n            \"38.3\",\n            \"2.7\"\n          ],\n          [\n            \"Qwen\",\n            \"constrained\",\n            \"26.72\",\n            \"8.18\",\n            \"0\",\n            \"0\"\n          ],\n          [\n            \"Llama\",\n            \"unconstrained\",\n            \"27.52\",\n            \"9.98\",\n            \"8.8\",\n            \"3.5\"\n          ],\n          [\n            \"Llama\",\n            \"constrained\",\n            \"26.91\",\n            \"8.91\",\n            \"0\",\n            \"0.8\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"EE FT composability 在 worst 档被完全 dismiss。核心攻击: (a) Trigger-F1 降 5pp 是 unacceptable quality degradation; (b) Arg-F1 改善不显著且 Llama 实际下降; (c) \\\"This confirms constrained decoding for IE is a straightforward application of XGrammar with a lookup table.\\\"\\n\\n\\n已有实际数据（p1_ee_ft_composability_r5 + p1_ee_ft_llama_r2）。关键问题: (1) Qwen Trigger-F1 从 32.08%→26.72%（-5.36pp），constrained decoding 明显损害 trigger extraction 质量。Reviewer: \\\"Your method trades extraction quality for constraint compliance — Structure Snowballing (Tam et al. 2024) already documented this trade-off.\\\" (2) Arg-F1 改善微乎其微（Qwen +0.33pp, Llama -1.07pp 实际下降）。 (3) Llama constrained AC=0.8% 表明 FT regime 下仍无法完全消除 argument constraint violations。 Reviewer 总结: \\\"The only outcome is constraint compliance at the cost of extraction performance. This is a net negative contribution.\\\"\\n\"\n  },\n  {\n    \"name\": \"Grammar-only cross-model validation (Qwen/Llama EE)\",\n    \"description\": \"Grammar-only ablation on Qwen 和 Llama WikiEvents EE for completeness\",\n    \"results\": {\n      \"qwen_grammar_only_EV_pct\": 0,\n      \"qwen_grammar_only_RoV_pct\": 71.5,\n      \"qwen_grammar_only_AC_pct\": 10.2,\n      \"qwen_grammar_only_CF_pct\": 0.7,\n      \"qwen_grammar_only_entity_f1\": 13.8,\n      \"llama_grammar_only_EV_pct\": 0,\n      \"llama_grammar_only_RoV_pct\": 76.4,\n      \"llama_grammar_only_AC_pct\": 14.5,\n      \"llama_grammar_only_CF_pct\": 0.5,\n      \"llama_grammar_only_entity_f1\": 17.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"EE Grammar-Only Ablation (3 Models)\",\n        \"columns\": [\n          \"Model\",\n          \"EV%\",\n          \"RoV%\",\n          \"AC%\",\n          \"CF%\",\n          \"Ent-F1\"\n        ],\n        \"rows\": [\n          [\n            \"Mistral (actual)\",\n            \"0\",\n            \"64.0\",\n            \"13.8\",\n            \"1.1\",\n            \"11.9\"\n          ],\n          [\n            \"Qwen (predicted)\",\n            \"0\",\n            \"71.5\",\n            \"10.2\",\n            \"0.7\",\n            \"13.8\"\n          ],\n          [\n            \"Llama (predicted)\",\n            \"0\",\n            \"76.4\",\n            \"14.5\",\n            \"0.5\",\n            \"17.2\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三模型 grammar-only 一致模式（EV→0%, RoV≫0%, AC↑）在方法论上完整，但 reviewer 认为 不增加任何 insight: \\\"it's obvious that grammar constraints can only handle vocabulary-level violations, not semantic ones.\\\"\\n\\n\\n预测数据。基于 Mistral grammar-only 模式（RoV=64%, AC=13.8%），Qwen/Llama 预计: EV→0%（grammar 消除）, RoV 保持 70-77%（grammar 无法约束 event-conditioned roles）, AC 上升至 10-15%（latent violation surfacing）。Worst 档 reviewer: \\\"Redundant — the Mistral ablation already shows this, and the conclusion is trivially expected.\\\" 三模型 一致性虽是完整消融证据，但被视为不增加 insight。\\n\"\n  },\n  {\n    \"name\": \"Bootstrap CI for EE metrics\",\n    \"description\": \"Statistical significance testing for EE F1 changes (10000× bootstrap)\",\n    \"results\": {\n      \"qwen_trigger_f1_delta_pp\": 1.55,\n      \"qwen_trigger_f1_p\": 0.18,\n      \"qwen_entity_f1_delta_pp\": 14.09,\n      \"qwen_entity_f1_p\": 0.001,\n      \"qwen_arg_f1_delta_pp\": 1.59,\n      \"qwen_arg_f1_p\": 0.42,\n      \"llama_trigger_f1_delta_pp\": 1.76,\n      \"llama_trigger_f1_p\": 0.22,\n      \"llama_entity_f1_delta_pp\": 17.63,\n      \"llama_entity_f1_p\": 0.001,\n      \"llama_arg_f1_delta_pp\": 1.18,\n      \"llama_arg_f1_p\": 0.38,\n      \"mistral_trigger_f1_delta_pp\": 1.46,\n      \"mistral_trigger_f1_p\": 0.31,\n      \"mistral_entity_f1_delta_pp\": 11.71,\n      \"mistral_entity_f1_p\": 0.001,\n      \"mistral_arg_f1_delta_pp\": 0.31,\n      \"mistral_arg_f1_p\": 0.61\n    },\n    \"tables\": [\n      {\n        \"name\": \"EE Bootstrap CI Summary\",\n        \"columns\": [\n          \"Model\",\n          \"Metric\",\n          \"Delta-pp\",\n          \"p-value\",\n          \"Sig?\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            \"Trigger-F1\",\n            \"+1.55\",\n            \"0.18\",\n            \"No\"\n          ],\n          [\n            \"Qwen\",\n            \"Entity-F1\",\n            \"+14.09\",\n            \"<0.001\",\n            \"Yes*\"\n          ],\n          [\n            \"Qwen\",\n            \"Arg-F1\",\n            \"+1.59\",\n            \"0.42\",\n            \"No\"\n          ],\n          [\n            \"Llama\",\n            \"Trigger-F1\",\n            \"+1.76\",\n            \"0.22\",\n            \"No\"\n          ],\n          [\n            \"Llama\",\n            \"Entity-F1\",\n            \"+17.63\",\n            \"<0.001\",\n            \"Yes*\"\n          ],\n          [\n            \"Llama\",\n            \"Arg-F1\",\n            \"+1.18\",\n            \"0.38\",\n            \"No\"\n          ],\n          [\n            \"Mistral\",\n            \"Trigger-F1\",\n            \"+1.46\",\n            \"0.31\",\n            \"No\"\n          ],\n          [\n            \"Mistral\",\n            \"Entity-F1\",\n            \"+11.71\",\n            \"<0.001\",\n            \"Yes*\"\n          ],\n          [\n            \"Mistral\",\n            \"Arg-F1\",\n            \"+0.31\",\n            \"0.61\",\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bootstrap CI 成为双刃剑: Entity-F1 显著但仅是 format compliance（*标注）， Trigger-F1 和 Arg-F1 均不显著。Reviewer: \\\"No significant improvement on any semantically meaningful metric.\\\" 这与 RE 结果（DocRED R-F1 +0.50pp p<0.001）形成 对比，强化 \\\"EE 实验是 toy\\\" 的攻击。\\n\\n\\n预测数据。Bootstrap CI 预计显示: (a) Entity-F1 改善（0%→11-17%）统计显著（p<0.01），但完全来自 format compliance 恢复 （grammar 强制 valid JSON → parser 识别 entity）——不是语义提升。 (b) Trigger-F1 改善（+1.5-1.8pp）全部不显著（p>0.15），绝对值太低（3-13%）variance 太大。 (c) Arg-F1 改善全部不显著——绝对值接近零。 Worst 档 reviewer: \\\"The only statistically significant improvement is entity F1, which is entirely attributable to format compliance, not extraction improvement. No significant improvement on any semantically meaningful metric.\\\"\\n\"\n  },\n  {\n    \"name\": \"Latency overhead measurement\",\n    \"description\": \"Wall-clock comparison: unconstrained vs constrained decoding overhead\",\n    \"results\": {\n      \"zs_scierc_overhead_pct\": 13.1,\n      \"zs_scierc_mean_unc_s\": 4.163,\n      \"zs_scierc_mean_con_s\": 4.71,\n      \"ft_scierc_overhead_pct\": 10.0,\n      \"ft_scierc_mean_unc_s\": 2.612,\n      \"ft_scierc_mean_con_s\": 2.873,\n      \"beam4_constraint_overhead_pct\": 16.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Latency Overhead Summary\",\n        \"columns\": [\n          \"Setting\",\n          \"Overhead%\",\n          \"unc s/doc\",\n          \"con s/doc\"\n        ],\n        \"rows\": [\n          [\n            \"ZS SciERC\",\n            \"13.1\",\n            \"4.16\",\n            \"4.71\"\n          ],\n          [\n            \"FT SciERC\",\n            \"10.0\",\n            \"2.61\",\n            \"2.87\"\n          ],\n          [\n            \"FT Beam-4\",\n            \"16.5\",\n            \"3.45\",\n            \"4.01\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Latency 单独不构成 reject 理由，但 reviewer 在综合评估中使用: \\\"Your method adds 13% latency, introduces CF violations, and provides no significant F1 gain in ZS.\\\"\\n\\n\\n已有实际数据（p8_latency_overhead: 13.1%, p8c_ft_scierc_latency: 10%）。Latency 本身不是主要攻击面——13% 可接受。但 worst 档 reviewer 将其嵌入 cost-benefit: \\\"13% latency for a method that introduces 10-21% cross-field violations and achieves no significant F1 improvement in ZS — the trade-off is unfavorable.\\\" 在综合评估中作为 additional cost。\\n\"\n  },\n  {\n    \"name\": \"70B LoRA SciERC unconstrained eval\",\n    \"description\": \"Qwen3-70B AWQ-INT4 LoRA fine-tuned, SciERC unconstrained evaluation\",\n    \"results\": {\n      \"R_F1\": 44.73,\n      \"E_F1\": 64.86,\n      \"DR_pct\": 1.5,\n      \"RV_pct\": 0,\n      \"ET_pct\": 0,\n      \"CF_pct\": 0,\n      \"parse_fail_pct\": 0,\n      \"total_samples\": 551\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Unconstrained baseline 本身不是问题，R-F1=44.73% 是合理的。关键是 constrained eval 会如何表现。\\n\\n\\n已有实际数据（eval_70b_lora_scierc_unconstrained DONE）。R-F1=44.73% 与 8B LoRA Qwen (43.86%) 和 Llama (45.45%) 在同一水平——70B+AWQ-INT4 量化并未带来显著优势。 DR baseline=1.50% 高于 Llama-8B LoRA (1.11%) 但低于 Qwen-8B LoRA (1.95%)。 关键: 这个 baseline 设定了 constrained eval 的对比基准。如果 constrained 版本 DR 不能显著降低，或 R-F1 明显下降，70B LoRA 实验就变成负面证据。\\n\"\n  },\n  {\n    \"name\": \"70B LoRA SciERC constrained eval\",\n    \"description\": \"Qwen3-70B AWQ-INT4 LoRA, SciERC constrained (full_s1) — worst tier 核心预测\",\n    \"results\": {\n      \"R_F1\": 43.2,\n      \"E_F1\": 64.5,\n      \"DR_pct\": 1.5,\n      \"RV_pct\": 0,\n      \"ET_pct\": 0,\n      \"CF_pct\": 2.2,\n      \"parse_fail_pct\": 5.0,\n      \"total_samples\": 551,\n      \"delta_R_F1_pp\": -1.53,\n      \"delta_E_F1_pp\": -0.36\n    },\n    \"tables\": [\n      {\n        \"name\": \"LoRA SciERC: 8B vs 70B Constrained Impact\",\n        \"columns\": [\n          \"Model\",\n          \"unc DR%\",\n          \"con DR%\",\n          \"DR-reduction%\",\n          \"R-F1 delta\",\n          \"PF%\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen-8B LoRA\",\n            \"1.95\",\n            \"0\",\n            \"100\",\n            \"-0.09\",\n            \"0\"\n          ],\n          [\n            \"Llama-8B LoRA\",\n            \"1.11\",\n            \"0.09\",\n            \"92\",\n            \"+0.02\",\n            \"0\"\n          ],\n          [\n            \"Qwen-70B LoRA (pred)\",\n            \"1.50\",\n            \"1.50\",\n            \"0\",\n            \"-1.53\",\n            \"5.0\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"70B LoRA SciERC constrained 在 worst 档是关键打击: DR reduction=0%（constrained DR 等于 unconstrained DR），意味着 semantic mask 在量化模型上完全失效。R-F1 同时下降 1.5pp。 Reviewer: \\\"At 70B scale with INT4 quantization, your semantic constraints provide zero DR reduction while degrading extraction quality by 1.5pp. This undermines the entire scale generalization claim.\\\"\\n\\n\\n预测数据（worst tier 核心假设: DR>1% 或 R-F1 下降 >2pp 或 PF>10%）。 DR=1.5%（范围 [0.5, 3.0]）: constrained decoding 未能消除 DR，与 8B LoRA 的 DR=0-0.09% 形成鲜明对比。机制: AWQ-INT4 量化导致 logit distribution 偏移，semantic mask 的 top-k fallback 更频繁触发，残余 DR 更高。quantized logits 的 precision 不够导致 mask 边界 附近的 token 概率计算不精确。 R-F1 下降 1.53pp（范围 [-3.0, -0.5]）: 从 44.73→43.2%，虽未超过 -2pp threshold，但 方向与 8B LoRA 的 near-zero/positive delta 完全相反。 PF=5%: 量化模型在 constrained decoding 下偶尔产生重复或 truncation，但 SciERC 文档短， PF 不至于超过 10%。 综合: DR>1% 已触发 worst tier 条件。Reviewer: \\\"Your method fails to eliminate domain-range violations on a quantized 70B model — the deployment scenario where guarantees matter most.\\\"\\n\"\n  },\n  {\n    \"name\": \"70B LoRA DocRED unconstrained eval\",\n    \"description\": \"Qwen3-70B AWQ-INT4 LoRA, DocRED unconstrained — 实验 RUNNING\",\n    \"results\": {\n      \"R_F1\": 46.2,\n      \"E_F1\": 85.0,\n      \"DR_pct\": 0.65,\n      \"RV_pct\": 0.05,\n      \"ET_pct\": 0,\n      \"CF_pct\": 0.04,\n      \"parse_fail_pct\": 3.5,\n      \"total_samples\": 200\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"200 docs 子集（而非 998 全量）在 worst 档被 reviewer 质疑: \\\"Why only 200 documents for your most important scale experiment? This looks like a convenience sample, not a rigorous evaluation.\\\"\\n\\n\\n预测数据（实验 RUNNING，200 docs 子集）。基于 8B LoRA DocRED 结果推断: Qwen-8B LoRA R-F1=40.86, Llama-8B LoRA R-F1=43.72, 70B 预计 +3-5pp 提升至 ~46%。 E-F1 预计 ~85%（8B 范围 82-84%，70B 更强）。DR baseline 0.65%（8B 范围 0.49-0.76%）。 200 docs 子集使得结果统计 power 较弱，增加 reviewer 质疑空间。\\n\"\n  },\n  {\n    \"name\": \"70B LoRA DocRED constrained eval\",\n    \"description\": \"Qwen3-70B AWQ-INT4 LoRA, DocRED constrained (full_s1) — worst tier 核心预测\",\n    \"results\": {\n      \"R_F1\": 43.7,\n      \"E_F1\": 84.5,\n      \"DR_pct\": 2.8,\n      \"RV_pct\": 0,\n      \"ET_pct\": 0,\n      \"CF_pct\": 1.8,\n      \"parse_fail_pct\": 11.0,\n      \"total_samples\": 200,\n      \"delta_R_F1_pp\": -2.5,\n      \"delta_E_F1_pp\": -0.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"LoRA DocRED: 8B vs 70B Constrained Full Comparison\",\n        \"columns\": [\n          \"Model\",\n          \"DR-con%\",\n          \"CF%\",\n          \"R-F1\",\n          \"R-F1-delta\",\n          \"PF%\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen-8B LoRA\",\n            \"0.01\",\n            \"0.41\",\n            \"40.56\",\n            \"-0.30\",\n            \"8.5\"\n          ],\n          [\n            \"Llama-8B LoRA\",\n            \"0.21\",\n            \"0.21\",\n            \"43.78\",\n            \"+0.06\",\n            \"2.5\"\n          ],\n          [\n            \"Qwen-70B LoRA (pred)\",\n            \"2.80\",\n            \"1.80\",\n            \"43.70\",\n            \"-2.50\",\n            \"11.0\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"70B LoRA DocRED 在 worst 档是 scale generalization claim 终结。三重失败: (a) DR 2.8%——constrained 仍有显著残余 violations; (b) R-F1 下降 2.5pp 至 43.7%——低于 8B Llama LoRA constrained 43.78%; (c) 11% parse failures——22/200 docs 不可评估。 Reviewer: \\\"On DocRED, the 70B quantized model with constraints performs WORSE than the 8B full-precision model, while being far more expensive to run. The method does not scale to practical deployment scenarios with quantized large models.\\\" 这与 70B ZS 的 DR=0% 形成对比: \\\"Your method works at 70B only in zero-shot where F1 is 13% (toy); in the fine-tuned regime where F1 is meaningful (~46%), it fails.\\\"\\n\\n\\n预测数据（worst tier 核心假设: DR>1% 或 R-F1 下降 >2pp 或 PF>10%）。 DR=2.8%（范围 [0.5, 5.0]）: DocRED 96-relation ontology 下量化模型的 semantic mask fallback 更频繁。8B LoRA DocRED constrained DR=0.01-0.21%，70B 的 2.8% 是数量级恶化。 机制: 量化后 logit space 的 probability mass 在 96-relation ontology 下分布更不均匀， semantic mask 与 grammar mask 的 intersection 更常为空→更多 fallback→更高残余 DR。 R-F1 下降 2.5pp（范围 [-4.0, -1.0]）: 从 46.2%→43.7%。这甚至低于 8B Llama LoRA constrained (43.78%)——70B+量化+constrained 组合效果不如 8B full-precision。 PF=11%（>10% threshold）: DocRED 长文档 + 量化 + constrained 三重因素叠加导致生成 退化（重复序列、early truncation、malformed JSON）。22 docs/200 无法评估。 综合: 全部三个 threshold 都被触发（DR>1% ✓, R-F1 drop >2pp ✓, PF>10% ✓）。\\n\"\n  },\n  {\n    \"name\": \"Post-hoc vs Constrained ZS Regime (6 configs)\",\n    \"description\": \"Post-hoc filtering R-F1 全面优于 constrained decoding in 5/6 ZS configs — worst tier 核心假设\",\n    \"results\": {\n      \"qwen_scierc_posthoc_R_F1\": 8.63,\n      \"qwen_scierc_constrained_R_F1\": 8.36,\n      \"qwen_scierc_posthoc_wins\": true,\n      \"llama_scierc_posthoc_R_F1\": 2.71,\n      \"llama_scierc_constrained_R_F1\": 2.54,\n      \"llama_scierc_posthoc_wins\": true,\n      \"mistral_scierc_posthoc_R_F1\": 3.94,\n      \"mistral_scierc_constrained_R_F1\": 3.67,\n      \"mistral_scierc_posthoc_wins\": true,\n      \"qwen_docred_posthoc_R_F1\": 9.61,\n      \"qwen_docred_constrained_R_F1\": 8.23,\n      \"qwen_docred_posthoc_wins\": true,\n      \"llama_docred_posthoc_R_F1\": 7.44,\n      \"llama_docred_constrained_R_F1\": 6.27,\n      \"llama_docred_posthoc_wins\": true,\n      \"mistral_docred_posthoc_R_F1\": 3.85,\n      \"mistral_docred_constrained_R_F1\": 5.52,\n      \"mistral_docred_posthoc_wins\": false,\n      \"posthoc_win_count\": 5,\n      \"posthoc_total_configs\": 6\n    },\n    \"tables\": [\n      {\n        \"name\": \"ZS Post-hoc vs Constrained R-F1\",\n        \"columns\": [\n          \"Dataset\",\n          \"Model\",\n          \"Post-hoc R-F1\",\n          \"Constrained R-F1\",\n          \"Winner\"\n        ],\n        \"rows\": [\n          [\n            \"SciERC\",\n            \"Qwen\",\n            \"8.63\",\n            \"8.36\",\n            \"Post-hoc\"\n          ],\n          [\n            \"SciERC\",\n            \"Llama\",\n            \"2.71\",\n            \"2.54\",\n            \"Post-hoc\"\n          ],\n          [\n            \"SciERC\",\n            \"Mistral\",\n            \"3.94\",\n            \"3.67\",\n            \"Post-hoc\"\n          ],\n          [\n            \"DocRED\",\n            \"Qwen\",\n            \"9.61\",\n            \"8.23\",\n            \"Post-hoc\"\n          ],\n          [\n            \"DocRED\",\n            \"Llama\",\n            \"7.44\",\n            \"6.27\",\n            \"Post-hoc\"\n          ],\n          [\n            \"DocRED\",\n            \"Mistral\",\n            \"3.85\",\n            \"5.52\",\n            \"Constrained\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"5/6 ZS configs post-hoc wins on R-F1。这是 worst 档最致命的 finding。Reviewer 直接问: \\\"What's the point?\\\" Paper 的 counter-arguments（recall preservation, operational properties, information coverage）在 ZS regime 的 sub-10% F1 下不具说服力。 Reframe 方向: 将 constrained decoding 的价值锚定在 (a) FT regime（post-hoc wins 消失）， (b) EE task（post-hoc 删除 99.6-100%），(c) structural guarantee（per-instance compliance vs statistical compliance），避开 ZS F1 比较。\\n\\n已有实际数据（w8_ft_posthoc_baseline）。Post-hoc R-F1 >= constrained R-F1 in 5/6 ZS configs。仅 Mistral DocRED（极端 73.7% rejection rate 导致 TP 大量丢失）例外。 机制: low F1 regime 下（R-F1 < 13%），most predicted triples are FP。Post-hoc 通过删除 violating triples 移除大量 FP，precision 大幅提升。Constrained decoding 虽保留更多 triples （包括 TP），但 FP 也更多。当 FP/TP ratio >> 1 时，post-hoc 的 precision gain 超过 recall loss。 Worst 档 reviewer: \\\"In the zero-shot regime that constitutes 60% of your evaluation, a simple post-hoc filter consistently outperforms your constrained decoding on the metric that matters (F1). What's the point of engineering a complex constrained decoding pipeline when removing bad triples after generation works better?\\\"\\n\"\n  }\n]",
      "numLines": 840,
      "startLine": 1,
      "totalLines": 840
    }
  },
  "sourceToolAssistantUUID": "3a1061ec-f826-46ec-8d97-c34b8ccb0250",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T052642 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_c…",
  "leafUuid": "c3d12bb1-68fb-4e27-9953-b58ac9a5f841",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier mock research paper",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a"
}
```

---

### Tool result

_source line 13 · 2026-05-22T06:19:46.346Z_

<details><summary>↩ Tool result · `toolu_015eiJWSx62pRpkP7Yq9kHQf`</summary>

```text
1	# OntoCoDec — Paper Framing
2	
3	## Target Venue
4	EMNLP 2026 (ARR submission May 25, 2026) — **目标: conference main**（D040, 用户明确指示）
5	
6	## Title
7	OntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints
8	(D015: "Near-Complete" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)
9	
10	**D040 Story 升级方向**: 从 "IE-specific constrained decoding" → "universal ontology-constrained structured generation framework"。WikiEvents Event Extraction 验证跨任务泛化。Continuation masking v2 突破（10-doc: RoV 0%, semantic violations ↓95.8%）初步确认跨任务有效性，全量实验进行中。最终 title 待全量结果后调整。
11	
12	## Core Insight
13	LLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.
14	
15	**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:
16	- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)
17	- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])
18	- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。
19	- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。
20	
21	## Core Claims
22	
23	### Claim 1 (Empirical): Violation Landscape
24	LLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).
25	
26	**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.
27	
28	**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。
29	
30	**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.
31	
32	### Claim 2 (Empirical): Prompt Insufficiency
33	Schema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:
34	- Overall: 15.4% → 5.78% (-62.4%), still above 5%
35	- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)
36	- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses
37	
38	**Narrative**: This is NOT about "5.78% barely above 5%". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.
39	
40	### Claim 3 (Methodological): Composable Constraint Framework
41	OntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:
42	1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)
43	2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking
44	
45	The two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT "synergistic" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.
46	
47	The two layers compose via bitwise AND of token masks. Recommended framing: "Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor."
48	
49	**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):
50	When $M_{semantic} \cap M_{grammar} = \emptyset$, the system falls back to grammar-only control.
51	
52	**关键量化数据（Reviewer 从日志挖掘）**:
53	- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**
54	- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**
55	- DocRED fallback 频率是 SciERC 的 **5.3×**
56	- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）
57	
58	**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。
59	
60	**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 "Constraint Coverage" 指标（semantic masking 实际生效的 token 比例）。这把 "10.19% DR 残余" 从弱点变成可量化分析的 finding。Frame as "engineering robustness" in §4; fallback 频率 + tightness 作为 §5 定量分析。
61	
62	**Decidability taxonomy**: Constraints classified by prefix-decidability:
63	- (a) Purely local: entity type ∈ vocabulary (grammar layer)
64	- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)
65	- (c) Truly non-local: forward coreference — out of scope for forward-only decoding
66	
67	### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation
68	- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.
69	- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.
70	
71	**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.
72	
73	⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).
74	
75	### Claim 5 (Empirical): Cross-Task Generalization — Event Extraction (D040, NEW)
76	**Status**: ✅ All 3 models × 246 docs complete (v3 with collision fix + exact-match fix)
77	
78	OntoCoDec generalizes beyond Relation Extraction to **Event Extraction** (WikiEvents, Li et al. NAACL 2021), demonstrating that the framework is task-agnostic for any IE task with ontology-defined type constraints.
79	
80	**Cross-task framing (Reviewer 评估 confirmed)**:
81	- **RoV 是 DR 的正确对应物**（不是 RV）：EE 中 per-type violation rate 是 RE 的 3-5×，支持 "more complex ontology → more critical constraint enforcement" claim
82	- **三层级联 Grammar→RoV→AC**（比 RE 的 Grammar→DR 两层更丰富）：grammar 消除 EV，使 semantic layer 可以 enforce role restriction (RoV→0%)，进而暴露 AC violations。这强化 architecture contribution 论证。
83	- **Semantic layer 是 EE 的唯一防线**：grammar 层对 role vocabulary 无能力，只有 semantic layer + continuation masking 能 enforce per-event-type role constraints
84	- **"Practical value" 防线**：Arg F1 ≈ 0% 不削弱 claim，因为 (a) mechanism generalization 是 contribution 不是 SOTA performance，(b) FT composability 已在 RE 中证明 high-F1 场景有效
85	
86	**WikiEvents specifics** (DARPA KAIROS ontology):
87	- 56 event types × 80 argument roles × 27 entity types（含 5 个补充 Contact 子类型 + CRM entity type）
88	- 245 组显式 (event_type, role) → allowed_entity_types 约束
89	- Maps directly to OntoCoDec's semantic layer: argument role type constraints ≡ domain/range constraints
90	- 27 entity types（比 ACE05 的 7 个更丰富）→ constraint space 更大，更能展示 semantic layer 价值
91	- 99.98% 数据满足约束 → 约束定义是真实有效的
92	- Hierarchical event names (e.g., Conflict.Attack.DetonateExplode) → 扁平化为 leaf-node 解决 first-token collision（96.1%→3.9%）
93	
94	**数据集选择理由**（MAVEN/RAMS 排除）：
95	- MAVEN (168 types): 无 argument extraction，不适用
96	- MAVEN-Arg (162 types): FrameNet-based，无 role→entity_type schema 约束
97	- RAMS (139 types): 仅 cardinality 约束，无 entity type binding
98	- ACE05 (33 types): LDC 付费，采购周期来不及
99	- **WikiEvents 是唯一同时满足 "免费 + 有显式 role→entity_type 约束" 的数据集**
100	
101	**Violation 分类** (5 类，从 RE 的 4 类扩展):
102	- ET (Entity Type): entity type 不在 ontology 合法类型列表中
103	- EV (Event Vocabulary): event type 不在 ontology 定义中
104	- RoV (Role Vocabulary): argument role 不在该 event type 定义中
105	- AC (Argument Constraint): argument entity type 不满足 role→entity_type 约束（DR 的自然推广）
106	- CF (Cross-Field): 同一 entity 跨 event 被赋予不同 type
107	
108	**Full results (246 docs, v3 final — collision fix + exact-match fix)**:
109	
110	| Metric | Qwen3-8B uncon. | Qwen3-8B Full S1 | Llama-3.1-8B uncon. | Llama-3.1-8B Full S1 | Mistral-7B uncon. | Mistral-7B Full S1 |
111	|--------|-----------------|-------------------|---------------------|----------------------|-------------------|---------------------|
112	| Parse | 88.6% | 83.7% | 91.9% | 84.1% | 88.6% | 88.6% |
113	| EV | 24.0% | **0%** | 10.5% | **0%** | 37.3% | **0%** |
114	| RoV | 74.9% | **0%** | 88.8% | **0%** | 63.9% | **0%** |
115	| AC | 0.3% | 2.1% | 0.1% | 3.8% | 0% | 1.3% |
116	| CF | 0% | 21.1% | 0% | 17.2% | 0% | 14.9% |
117	| Trigger F1 | 11.8% | 13.4% | 5.7% | 7.5% | 2.4% | 3.9% |
118	| Ent F1 | 0% | 14.1% | 0% | 17.6% | 0% | 11.7% |
119	
120	**Grammar-only ablation (Mistral v3, all 3 models)**:
121	- Grammar eliminates EV→0% but RoV remains 64-77%: grammar CFG cannot constrain 80 argument roles conditioned on event context
122	- AC rises to 8-14% under grammar-only (latent violation surfacing pattern, same as DocRED RE)
123	- Proves semantic layer is essential for EE: two-layer architecture is necessary, not just convenient
124	
125	**Post-hoc filtering comparison (devastating)**:
126	- Qwen: 5,467→23 arguments (99.6% discarded) to reach 0% violation
127	- Llama: 5,053→3 arguments (99.9% discarded)
128	- Mistral: 6,034→0 arguments (100% discarded)
129	- Post-hoc is not viable for EE (contrasts with RE where it's expensive but functional)
130	
131	**BPE collision diagnostic (confirmed 2026-05-18)**:
132	- Qwen (BPE, ~152K vocab): **0 collision groups** — all 27 entity types have unique first tokens
133	- Llama (BPE, ~128K vocab): **0 collision groups** — same
134	- Mistral (SentencePiece, ~32K vocab): **2 collision groups** (SID/SEN/SIDE→'S', BAL/BOD→'B')
135	- **Residual AC narrative**: Mistral AC 1.3% = residual after collision fix (was 16.6%); Qwen/Llama AC 2.1-3.8% = purely model semantic confusion (confuses similar entity types like SID vs SEN), NOT tokenizer collision
136	
137	**关键 findings**:
138	- RoV 是压倒性违规（64-89%），远超 RE 的 RV（1-30%）→ 更强力展示 constraint 需求
139	- EV 显著（10-37%）→ grammar 层直接消除
140	- **Entity F1 从 0% 恢复到 11.7-17.6%**: 不是语义改进，是 format compliance 恢复——grammar enforcement 产生 schema-valid JSON，parser 才能识别 entity mentions
141	- Trigger F1 +1.5 to +1.8pp: elimination of OOV event types counted as FP
142	- CF 15-21% 比 RE 更高（EE argument structure 更复杂），沿用 RE 的 CF tradeoff framing
143	
144	**Story upgrade**: WikiEvents results confirm paper narrative: "universal ontology-constrained structured generation framework applicable to any IE task with formal type constraints". Three evidence lines: (1) EV/RoV→0% across all models, (2) grammar-only ablation proves two-layer necessity, (3) post-hoc filtering is non-viable for EE. This is the key differentiator for conference main vs Findings.
145	
146	**70B scale experiment** (P029-P030, in progress): Qwen3-70B AWQ-INT4 on SciERC + DocRED to demonstrate scale generalization. If successful, adds a 4th model to cross-model evidence, strengthening C5.
147	
148	**Remaining risk**:
149	- CF 15-21% higher than RE → continues CF tradeoff framing
150	- 70B experiment timeline tight (need results by May 20 for paper integration)
151	
152	## Anticipated Reviewer Concerns
153	
154	### C1: "5.78% is barely above 5% — threshold is arbitrary"
155	**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.
156	
157	### C2: "Why not just post-hoc filter?"
158	**Response (D013, 实验结果已出)**:
159	
160	Post-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。
161	
162	**论文 framing（不以 F1 论高低，多维对比）**:
163	1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。
164	2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。
165	3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。
166	4. **Precision trade-off（诚实承认）**: "Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters."
167	
168	数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。
169	
170	**Reviewer 补充发现（D013 后）**:
171	5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。
172	6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——"prevent vs detect" 核心论据的具体数据。
173	7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。
174	
175	### C3: "Bitwise AND of two masks is not novel"
176	**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.
177	
178	### C4: "Evaluate-for violation rate increases with schema-informed prompt"
179	**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior ("Method X evaluates for Task Y" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just "harder instances" — it's an active interference between prompt-level constraint signals and the model's learned type associations.
180	
181	**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.
182	
183	### C5: "Only tested on one model (Qwen3-8B)"
184	**Response**: Cross-model validation DONE (D016 bootstrap verified). Llama-3.1-8B 零代码修改：
185	- SciERC: DR 13.34%→0.08% (↓99.4%), R-F1 -0.14pp (p=0.011, negligible), E-F1 NS
186	- DocRED: DR 26.07%→2.55% (↓90.2%), R-F1 +0.29pp (p=0.013, significant), E-F1 -0.64pp (p=0.022, modest decline)
187	- Parse failures: unconstrained 68 vs full_s1 91 (6.8% vs 9.1%)
188	
189	**Cross-model claim 指导（Reviewer 专项评估）**:
190	- ✅ 可声明："OntoCoDec generalizes across model families without code modification"（程序性事实，铁证）
191	- ❌ 不可声明："consistently achieves the same reduction rate"（仅 2 模型，不足以量化声明）
192	- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。
193	- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。
194	- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。
195	- 等 llama_docred_full_s1 出来后定最终 claim 措辞。
196	
197	### C6: "Constrained decoding degrades generation quality (CRANE, Structure Snowballing)"
198	**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Bootstrap CI (10000×, D012 Qwen + D016 Llama, all registry-aligned)**:
199	
200	**Qwen3-8B**: SciERC R-F1 +0.13pp (p=0.58, NS), E-F1 -0.03pp (NS). DocRED R-F1 +0.50pp (p<0.001), E-F1 +1.23pp (p<0.001).
201	**Llama-3.1-8B**: SciERC R-F1 -0.14pp (p=0.011, negligible), E-F1 NS. DocRED R-F1 +0.29pp (p=0.013), E-F1 -0.64pp (p=0.022).
202	
203	**Cross-model pattern**: DocRED R-F1 显著提升（两个模型）。E-F1 model-dependent（Qwen +1.23pp, Llama -0.64pp）。
204	- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。
205	- Frame as: "On DocRED, R-F1 gains are significant for both models. Entity F1 impact is model-dependent."
206	- 不升级为 core claim，但如实报告。
207	
208	### C7: "Your method trades DR violations for CF violations (cross-field consistency)"
209	**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:
210	
211	**CF 子类型分析（根因已确认）**：
212	- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)
213	- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)
214	- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差
215	
216	**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。
217	
218	**论证层次**：
219	1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint
220	2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference
221	3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug
222	4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)
223	
224	**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 "CF 是 semantic type enforcement 的系统性副作用" 提供干净的消融证据。
225	
226	**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。
227	
228	**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。
229	
230	### C8: "Absolute F1 is too low (~8%) — results are not meaningful"
231	**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: "We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance."
232	
233	## Paper Structure (Draft — D040 updated)
234	1. Introduction: Ontology constraint violations in LLM-based structured generation + composable framework overview (story: not just RE, general ontology-constrained generation)
235	2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure
236	3. Violation Landscape Study (Phase 0 empirics — independent contribution)
237	4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies
238	5. Experiments:
239	   - §5.1-5.3: RE experiments (SciERC + DocRED, 3 models, constrained vs unconstrained vs post-hoc vs prompt-based)
240	   - §5.4: **Event Extraction (WikiEvents)** — cross-task generalization (D040)
241	   - §5.5: Ablation + analysis (composability, latency, beam search, etc.)
242	6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology) + event extraction methods
243	7. Conclusion: Framework generality across IE tasks
244	
245	## Claim Calibration (per Reviewer assessment)
246	
247	**Safe to claim (sufficient evidence from Phase 2)**:
248	- "First systematic study of ontology constraint violations in LLM-based IE"
249	- "Violation rate correlates with constraint tightness, not ontology size" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)
250	- "Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost" ✅ Phase 2 confirmed
251	- "Two-layer architecture provides complementary coverage — grammar enables semantic" ✅ Ablation confirmed
252	- "Prompt-level intervention scales poorly with ontology complexity" ✅ SciERC ↓62% vs DocRED ↓32%
253	
254	**Claim with caution**:
255	- "Near-complete type-valid IE" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to "Near-Complete"
256	- "Principled framework applicable to arbitrary IE ontologies" — RE validated on 2 datasets × 2 models; EE (WikiEvents) 10-doc preliminary shows ↓95.8% semantic violations, full results pending
257	- "F1 improvement" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升
258	- "CF reveals type system ambiguity" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示"因为是 type ambiguity 所以 CF 可接受"
259	
260	**Do NOT claim**:
261	- "General infrastructure for IE" — only zero-shot extraction validated
262	- "State-of-the-art" — F1 is control variable, not optimization target (see C8)
263	- "Synergistic effect" — mechanism is enabling dependency, not mutual amplification (see Claim 3)
264	- "S2 solves CF" or "S2 mitigates Structure Snowballing" — data shows S2 ≈ S1 on all metrics; position as architectural variant only
265	- "Pilot50 DR=0%" — small-sample artifact, full S2 has DR=0.97%
266	- "Grammar-first invariant" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim
267	- "Robust dual-layer composition across schema complexities" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim
268	
269	## Risk Ranking (ordered by reject probability)
270	
271	1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).
272	2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。
273	3. **Novelty perception** (MEDIUM): "PLDI'25 for code → OntoCoDec for IE" attack line. Must argue IE constraint structure differs fundamentally.
274	4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.
275	5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.
276	
277	## Critical Path to EMNLP Submission (May 25)
278	
279	- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅
280	- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)
281	- **May 14-15**: Llama DocRED ✅ + Checker 修正 ✅ + post-hoc ✅ + bootstrap CI ✅ + related work ✅
282	- **May 15-17**: Prompt sensitivity ✅ + WikiEvents pipeline 开发 + continuation v2 突破
283	- **May 17-18**: WikiEvents 3 模型 unconstrained baselines (进行中) + constrained 全量
284	- **May 18-19**: WikiEvents 结果分析 + §5.4 Event Extraction 章节撰写
285	- **May 19-20**: Intro/Abstract/Conclusion 升级（cross-task story）+ 内部稿 → submit_paper_to_review
286	- **May 20-24**: Review 修改 + 最终提交
287	
288	**当前瓶颈**: WikiEvents 全量实验完成是关键路径。3 模型 unconstrained baselines 并行进行中（Qwen ~68/246, Mistral ~31/246, Llama 重启中），constrained 实验随后立即启动。
289	
290	## Status
291	- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)
292	- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)
293	- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)
294	- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)
295	- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)
296	- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)
297	- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)
298	- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)
299	- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)
300	- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)
301	- Related work: ✅ 42 bib entries, 4 additions merged
302	- Dream 6/6 actions: ✅ All complete
303	- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)
304	- D014 tightness revision: ✅ Complete (tightness × RV baseline dual-factor)
305	- Llama bootstrap CI (D016): ✅ Fixed + verified (registry-aligned ≤0.05pp, all p-values in paper)
306	- Paper compilation: ✅ 8 pages正文 + appendix
307	- R5 text fixes (N1/N2/N3/W1-W6): ✅ All complete and verified
308	- Prompt sensitivity analysis: ✅ Complete (3 prompts × 2 modes, DR reduction 94.0-94.6%, σ=0.3pp; appendix written)
309	- Doc length breakdown: ✅ Complete (appendix written)
310	- **WikiEvents Event Extraction (D040)**: 🔄 Continuation v2 突破 (10-doc: RoV 0%, semantic ↓95.8%); 3 模型 unconstrained baselines 进行中; constrained 全量待启动
311	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf601ea7-77fe-43b1-b82e-51f3fee062a1",
  "isSidechain": false,
  "promptId": "24b84624-7cc9-4802-b961-7b1d19e328f3",
  "type": "user",
  "uuid": "59bbf952-fe67-430d-a53a-b59ea9df19dd",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/paper_framing.md",
      "content": "# OntoCoDec — Paper Framing\n\n## Target Venue\nEMNLP 2026 (ARR submission May 25, 2026) — **目标: conference main**（D040, 用户明确指示）\n\n## Title\nOntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints\n(D015: \"Near-Complete\" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)\n\n**D040 Story 升级方向**: 从 \"IE-specific constrained decoding\" → \"universal ontology-constrained structured generation framework\"。WikiEvents Event Extraction 验证跨任务泛化。Continuation masking v2 突破（10-doc: RoV 0%, semantic violations ↓95.8%）初步确认跨任务有效性，全量实验进行中。最终 title 待全量结果后调整。\n\n## Core Insight\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.\n\n**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:\n- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)\n- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])\n- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。\n- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。\n\n## Core Claims\n\n### Claim 1 (Empirical): Violation Landscape\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\n\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\n\n**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。\n\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\n\n### Claim 2 (Empirical): Prompt Insufficiency\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\n\n**Narrative**: This is NOT about \"5.78% barely above 5%\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\n\n### Claim 3 (Methodological): Composable Constraint Framework\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\n\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \"synergistic\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\n\nThe two layers compose via bitwise AND of token masks. Recommended framing: \"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\"\n\n**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):\nWhen $M_{semantic} \\cap M_{grammar} = \\emptyset$, the system falls back to grammar-only control.\n\n**关键量化数据（Reviewer 从日志挖掘）**:\n- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**\n- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**\n- DocRED fallback 频率是 SciERC 的 **5.3×**\n- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）\n\n**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。\n\n**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 \"Constraint Coverage\" 指标（semantic masking 实际生效的 token 比例）。这把 \"10.19% DR 残余\" 从弱点变成可量化分析的 finding。Frame as \"engineering robustness\" in §4; fallback 频率 + tightness 作为 §5 定量分析。\n\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\n\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\n\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\n\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\n\n### Claim 5 (Empirical): Cross-Task Generalization — Event Extraction (D040, NEW)\n**Status**: ✅ All 3 models × 246 docs complete (v3 with collision fix + exact-match fix)\n\nOntoCoDec generalizes beyond Relation Extraction to **Event Extraction** (WikiEvents, Li et al. NAACL 2021), demonstrating that the framework is task-agnostic for any IE task with ontology-defined type constraints.\n\n**Cross-task framing (Reviewer 评估 confirmed)**:\n- **RoV 是 DR 的正确对应物**（不是 RV）：EE 中 per-type violation rate 是 RE 的 3-5×，支持 \"more complex ontology → more critical constraint enforcement\" claim\n- **三层级联 Grammar→RoV→AC**（比 RE 的 Grammar→DR 两层更丰富）：grammar 消除 EV，使 semantic layer 可以 enforce role restriction (RoV→0%)，进而暴露 AC violations。这强化 architecture contribution 论证。\n- **Semantic layer 是 EE 的唯一防线**：grammar 层对 role vocabulary 无能力，只有 semantic layer + continuation masking 能 enforce per-event-type role constraints\n- **\"Practical value\" 防线**：Arg F1 ≈ 0% 不削弱 claim，因为 (a) mechanism generalization 是 contribution 不是 SOTA performance，(b) FT composability 已在 RE 中证明 high-F1 场景有效\n\n**WikiEvents specifics** (DARPA KAIROS ontology):\n- 56 event types × 80 argument roles × 27 entity types（含 5 个补充 Contact 子类型 + CRM entity type）\n- 245 组显式 (event_type, role) → allowed_entity_types 约束\n- Maps directly to OntoCoDec's semantic layer: argument role type constraints ≡ domain/range constraints\n- 27 entity types（比 ACE05 的 7 个更丰富）→ constraint space 更大，更能展示 semantic layer 价值\n- 99.98% 数据满足约束 → 约束定义是真实有效的\n- Hierarchical event names (e.g., Conflict.Attack.DetonateExplode) → 扁平化为 leaf-node 解决 first-token collision（96.1%→3.9%）\n\n**数据集选择理由**（MAVEN/RAMS 排除）：\n- MAVEN (168 types): 无 argument extraction，不适用\n- MAVEN-Arg (162 types): FrameNet-based，无 role→entity_type schema 约束\n- RAMS (139 types): 仅 cardinality 约束，无 entity type binding\n- ACE05 (33 types): LDC 付费，采购周期来不及\n- **WikiEvents 是唯一同时满足 \"免费 + 有显式 role→entity_type 约束\" 的数据集**\n\n**Violation 分类** (5 类，从 RE 的 4 类扩展):\n- ET (Entity Type): entity type 不在 ontology 合法类型列表中\n- EV (Event Vocabulary): event type 不在 ontology 定义中\n- RoV (Role Vocabulary): argument role 不在该 event type 定义中\n- AC (Argument Constraint): argument entity type 不满足 role→entity_type 约束（DR 的自然推广）\n- CF (Cross-Field): 同一 entity 跨 event 被赋予不同 type\n\n**Full results (246 docs, v3 final — collision fix + exact-match fix)**:\n\n| Metric | Qwen3-8B uncon. | Qwen3-8B Full S1 | Llama-3.1-8B uncon. | Llama-3.1-8B Full S1 | Mistral-7B uncon. | Mistral-7B Full S1 |\n|--------|-----------------|-------------------|---------------------|----------------------|-------------------|---------------------|\n| Parse | 88.6% | 83.7% | 91.9% | 84.1% | 88.6% | 88.6% |\n| EV | 24.0% | **0%** | 10.5% | **0%** | 37.3% | **0%** |\n| RoV | 74.9% | **0%** | 88.8% | **0%** | 63.9% | **0%** |\n| AC | 0.3% | 2.1% | 0.1% | 3.8% | 0% | 1.3% |\n| CF | 0% | 21.1% | 0% | 17.2% | 0% | 14.9% |\n| Trigger F1 | 11.8% | 13.4% | 5.7% | 7.5% | 2.4% | 3.9% |\n| Ent F1 | 0% | 14.1% | 0% | 17.6% | 0% | 11.7% |\n\n**Grammar-only ablation (Mistral v3, all 3 models)**:\n- Grammar eliminates EV→0% but RoV remains 64-77%: grammar CFG cannot constrain 80 argument roles conditioned on event context\n- AC rises to 8-14% under grammar-only (latent violation surfacing pattern, same as DocRED RE)\n- Proves semantic layer is essential for EE: two-layer architecture is necessary, not just convenient\n\n**Post-hoc filtering comparison (devastating)**:\n- Qwen: 5,467→23 arguments (99.6% discarded) to reach 0% violation\n- Llama: 5,053→3 arguments (99.9% discarded)\n- Mistral: 6,034→0 arguments (100% discarded)\n- Post-hoc is not viable for EE (contrasts with RE where it's expensive but functional)\n\n**BPE collision diagnostic (confirmed 2026-05-18)**:\n- Qwen (BPE, ~152K vocab): **0 collision groups** — all 27 entity types have unique first tokens\n- Llama (BPE, ~128K vocab): **0 collision groups** — same\n- Mistral (SentencePiece, ~32K vocab): **2 collision groups** (SID/SEN/SIDE→'S', BAL/BOD→'B')\n- **Residual AC narrative**: Mistral AC 1.3% = residual after collision fix (was 16.6%); Qwen/Llama AC 2.1-3.8% = purely model semantic confusion (confuses similar entity types like SID vs SEN), NOT tokenizer collision\n\n**关键 findings**:\n- RoV 是压倒性违规（64-89%），远超 RE 的 RV（1-30%）→ 更强力展示 constraint 需求\n- EV 显著（10-37%）→ grammar 层直接消除\n- **Entity F1 从 0% 恢复到 11.7-17.6%**: 不是语义改进，是 format compliance 恢复——grammar enforcement 产生 schema-valid JSON，parser 才能识别 entity mentions\n- Trigger F1 +1.5 to +1.8pp: elimination of OOV event types counted as FP\n- CF 15-21% 比 RE 更高（EE argument structure 更复杂），沿用 RE 的 CF tradeoff framing\n\n**Story upgrade**: WikiEvents results confirm paper narrative: \"universal ontology-constrained structured generation framework applicable to any IE task with formal type constraints\". Three evidence lines: (1) EV/RoV→0% across all models, (2) grammar-only ablation proves two-layer necessity, (3) post-hoc filtering is non-viable for EE. This is the key differentiator for conference main vs Findings.\n\n**70B scale experiment** (P029-P030, in progress): Qwen3-70B AWQ-INT4 on SciERC + DocRED to demonstrate scale generalization. If successful, adds a 4th model to cross-model evidence, strengthening C5.\n\n**Remaining risk**:\n- CF 15-21% higher than RE → continues CF tradeoff framing\n- 70B experiment timeline tight (need results by May 20 for paper integration)\n\n## Anticipated Reviewer Concerns\n\n### C1: \"5.78% is barely above 5% — threshold is arbitrary\"\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\n\n### C2: \"Why not just post-hoc filter?\"\n**Response (D013, 实验结果已出)**:\n\nPost-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。\n\n**论文 framing（不以 F1 论高低，多维对比）**:\n1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。\n2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。\n3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。\n4. **Precision trade-off（诚实承认）**: \"Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters.\"\n\n数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。\n\n**Reviewer 补充发现（D013 后）**:\n5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。\n6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——\"prevent vs detect\" 核心论据的具体数据。\n7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。\n\n### C3: \"Bitwise AND of two masks is not novel\"\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\n\n### C4: \"Evaluate-for violation rate increases with schema-informed prompt\"\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\"Method X evaluates for Task Y\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \"harder instances\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\n\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\n\n### C5: \"Only tested on one model (Qwen3-8B)\"\n**Response**: Cross-model validation DONE (D016 bootstrap verified). Llama-3.1-8B 零代码修改：\n- SciERC: DR 13.34%→0.08% (↓99.4%), R-F1 -0.14pp (p=0.011, negligible), E-F1 NS\n- DocRED: DR 26.07%→2.55% (↓90.2%), R-F1 +0.29pp (p=0.013, significant), E-F1 -0.64pp (p=0.022, modest decline)\n- Parse failures: unconstrained 68 vs full_s1 91 (6.8% vs 9.1%)\n\n**Cross-model claim 指导（Reviewer 专项评估）**:\n- ✅ 可声明：\"OntoCoDec generalizes across model families without code modification\"（程序性事实，铁证）\n- ❌ 不可声明：\"consistently achieves the same reduction rate\"（仅 2 模型，不足以量化声明）\n- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。\n- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。\n- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。\n- 等 llama_docred_full_s1 出来后定最终 claim 措辞。\n\n### C6: \"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\"\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Bootstrap CI (10000×, D012 Qwen + D016 Llama, all registry-aligned)**:\n\n**Qwen3-8B**: SciERC R-F1 +0.13pp (p=0.58, NS), E-F1 -0.03pp (NS). DocRED R-F1 +0.50pp (p<0.001), E-F1 +1.23pp (p<0.001).\n**Llama-3.1-8B**: SciERC R-F1 -0.14pp (p=0.011, negligible), E-F1 NS. DocRED R-F1 +0.29pp (p=0.013), E-F1 -0.64pp (p=0.022).\n\n**Cross-model pattern**: DocRED R-F1 显著提升（两个模型）。E-F1 model-dependent（Qwen +1.23pp, Llama -0.64pp）。\n- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。\n- Frame as: \"On DocRED, R-F1 gains are significant for both models. Entity F1 impact is model-dependent.\"\n- 不升级为 core claim，但如实报告。\n\n### C7: \"Your method trades DR violations for CF violations (cross-field consistency)\"\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\n\n**CF 子类型分析（根因已确认）**：\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\n\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\n\n**论证层次**：\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\n\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \"CF 是 semantic type enforcement 的系统性副作用\" 提供干净的消融证据。\n\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\n\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\n\n### C8: \"Absolute F1 is too low (~8%) — results are not meaningful\"\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\"\n\n## Paper Structure (Draft — D040 updated)\n1. Introduction: Ontology constraint violations in LLM-based structured generation + composable framework overview (story: not just RE, general ontology-constrained generation)\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\n5. Experiments:\n   - §5.1-5.3: RE experiments (SciERC + DocRED, 3 models, constrained vs unconstrained vs post-hoc vs prompt-based)\n   - §5.4: **Event Extraction (WikiEvents)** — cross-task generalization (D040)\n   - §5.5: Ablation + analysis (composability, latency, beam search, etc.)\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology) + event extraction methods\n7. Conclusion: Framework generality across IE tasks\n\n## Claim Calibration (per Reviewer assessment)\n\n**Safe to claim (sufficient evidence from Phase 2)**:\n- \"First systematic study of ontology constraint violations in LLM-based IE\"\n- \"Violation rate correlates with constraint tightness, not ontology size\" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)\n- \"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\" ✅ Phase 2 confirmed\n- \"Two-layer architecture provides complementary coverage — grammar enables semantic\" ✅ Ablation confirmed\n- \"Prompt-level intervention scales poorly with ontology complexity\" ✅ SciERC ↓62% vs DocRED ↓32%\n\n**Claim with caution**:\n- \"Near-complete type-valid IE\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \"Near-Complete\"\n- \"Principled framework applicable to arbitrary IE ontologies\" — RE validated on 2 datasets × 2 models; EE (WikiEvents) 10-doc preliminary shows ↓95.8% semantic violations, full results pending\n- \"F1 improvement\" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升\n- \"CF reveals type system ambiguity\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\"因为是 type ambiguity 所以 CF 可接受\"\n\n**Do NOT claim**:\n- \"General infrastructure for IE\" — only zero-shot extraction validated\n- \"State-of-the-art\" — F1 is control variable, not optimization target (see C8)\n- \"Synergistic effect\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\n- \"S2 solves CF\" or \"S2 mitigates Structure Snowballing\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\n- \"Pilot50 DR=0%\" — small-sample artifact, full S2 has DR=0.97%\n- \"Grammar-first invariant\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\n- \"Robust dual-layer composition across schema complexities\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\n\n## Risk Ranking (ordered by reject probability)\n\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\n2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。\n3. **Novelty perception** (MEDIUM): \"PLDI'25 for code → OntoCoDec for IE\" attack line. Must argue IE constraint structure differs fundamentally.\n4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.\n\n## Critical Path to EMNLP Submission (May 25)\n\n- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅\n- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)\n- **May 14-15**: Llama DocRED ✅ + Checker 修正 ✅ + post-hoc ✅ + bootstrap CI ✅ + related work ✅\n- **May 15-17**: Prompt sensitivity ✅ + WikiEvents pipeline 开发 + continuation v2 突破\n- **May 17-18**: WikiEvents 3 模型 unconstrained baselines (进行中) + constrained 全量\n- **May 18-19**: WikiEvents 结果分析 + §5.4 Event Extraction 章节撰写\n- **May 19-20**: Intro/Abstract/Conclusion 升级（cross-task story）+ 内部稿 → submit_paper_to_review\n- **May 20-24**: Review 修改 + 最终提交\n\n**当前瓶颈**: WikiEvents 全量实验完成是关键路径。3 模型 unconstrained baselines 并行进行中（Qwen ~68/246, Mistral ~31/246, Llama 重启中），constrained 实验随后立即启动。\n\n## Status\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\n- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)\n- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)\n- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)\n- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)\n- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)\n- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)\n- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)\n- Related work: ✅ 42 bib entries, 4 additions merged\n- Dream 6/6 actions: ✅ All complete\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)\n- D014 tightness revision: ✅ Complete (tightness × RV baseline dual-factor)\n- Llama bootstrap CI (D016): ✅ Fixed + verified (registry-aligned ≤0.05pp, all p-values in paper)\n- Paper compilation: ✅ 8 pages正文 + appendix\n- R5 text fixes (N1/N2/N3/W1-W6): ✅ All complete and verified\n- Prompt sensitivity analysis: ✅ Complete (3 prompts × 2 modes, DR reduction 94.0-94.6%, σ=0.3pp; appendix written)\n- Doc length breakdown: ✅ Complete (appendix written)\n- **WikiEvents Event Extraction (D040)**: 🔄 Continuation v2 突破 (10-doc: RoV 0%, semantic ↓95.8%); 3 模型 unconstrained baselines 进行中; constrained 全量待启动\n",
      "numLines": 311,
      "startLine": 1,
      "totalLines": 311
    }
  },
  "sourceToolAssistantUUID": "cf601ea7-77fe-43b1-b82e-51f3fee062a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T052642 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_c…",
  "leafUuid": "59bbf952-fe67-430d-a53a-b59ea9df19dd",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier mock research paper",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a"
}
```

---

### Assistant

_source line 16 · 2026-05-22T06:19:58.438Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me analyze:

This is a "worst" tier dream paper - meaning it should simulate what happens when reviewers are hostile. The narrative guidance says to reframe from "constrained decoding method paper" to "empirical study paper with a tool", with title "How Do LLMs Violate Ontology Constraints? A Systematic Study with Mitigation".

Key points from the narrative guidance:
1. Core "type-valid IE" framing doesn't work, needs complete reframe
2. New story: violation landscape as main contribution, OntoCoDec as mitigation tool


3. Focus on analysis findings
4. Expected reviewer scores: Overall 2.5-3.5

Now I'll write the full LaTeX paper using all the experiment data, following the worst-tier framing with tables for each experiment, and making sure it's review-ready quality. Let me first check if the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59bbf952-fe67-430d-a53a-b59ea9df19dd",
  "isSidechain": false,
  "requestId": "req_011CbH84x9pjgiBxG5V8GADE",
  "type": "assistant",
  "uuid": "78e05d94-6712-4d7a-bec8-182f746df4c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfGi2nwnaR9m2wiHuriQRp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25573,
      "cache_read_input_tokens": 24031,
      "output_tokens": 475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 475,
          "cache_read_input_tokens": 24031,
          "cache_creation_input_tokens": 25573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25573
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

_source line 17 · 2026-05-22T06:19:58.449Z_

Now let me check if the output directory exists and if there's a LaTeX template available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78e05d94-6712-4d7a-bec8-182f746df4c8",
  "isSidechain": false,
  "requestId": "req_011CbH84x9pjgiBxG5V8GADE",
  "type": "assistant",
  "uuid": "a4cc705d-8aa6-4d1d-a124-0141aed3f27c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfGi2nwnaR9m2wiHuriQRp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25573,
      "cache_read_input_tokens": 24031,
      "output_tokens": 475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 475,
          "cache_read_input_tokens": 24031,
          "cache_creation_input_tokens": 25573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25573
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

_source line 18 · 2026-05-22T06:19:59.948Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011o5NQ7SR1C6gZvzcvQDah9`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4cc705d-8aa6-4d1d-a124-0141aed3f27c",
  "isSidechain": false,
  "requestId": "req_011CbH84x9pjgiBxG5V8GADE",
  "type": "assistant",
  "uuid": "ed924ebb-78c8-4d33-b530-af6103363129",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfGi2nwnaR9m2wiHuriQRp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25573,
      "cache_read_input_tokens": 24031,
      "output_tokens": 475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 475,
          "cache_read_input_tokens": 24031,
          "cache_creation_input_tokens": 25573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25573
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

_source line 19 · 2026-05-22T06:20:00.272Z_

<details><summary>↩ Tool result · `toolu_011o5NQ7SR1C6gZvzcvQDah9`</summary>

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
  "parentUuid": "12d16e52-dd2e-4c3f-8aff-e39e139e308b",
  "isSidechain": false,
  "promptId": "24b84624-7cc9-4802-b961-7b1d19e328f3",
  "type": "user",
  "uuid": "617d2a50-b5bc-4fe4-8c18-9c452f6ab7e7",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ed924ebb-78c8-4d33-b530-af6103363129",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-22T06:20:00.101Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q1Ur9pXkZhRytNYt4raJi3`</summary>

```json
{
  "command": "which pdflatex && pdflatex --version | head -3",
  "description": "Check pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed924ebb-78c8-4d33-b530-af6103363129",
  "isSidechain": false,
  "requestId": "req_011CbH84x9pjgiBxG5V8GADE",
  "type": "assistant",
  "uuid": "12d16e52-dd2e-4c3f-8aff-e39e139e308b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfGi2nwnaR9m2wiHuriQRp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25573,
      "cache_read_input_tokens": 24031,
      "output_tokens": 475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 475,
          "cache_read_input_tokens": 24031,
          "cache_creation_input_tokens": 25573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25573
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

_source line 21 · 2026-05-22T06:20:00.377Z_

<details><summary>↩ Tool result · `toolu_01Q1Ur9pXkZhRytNYt4raJi3`</summary>

```text
/usr/bin/pdflatex
pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)
kpathsea version 6.4.1
Copyright 2025 Han The Thanh (pdfTeX) et al.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12d16e52-dd2e-4c3f-8aff-e39e139e308b",
  "isSidechain": false,
  "promptId": "24b84624-7cc9-4802-b961-7b1d19e328f3",
  "type": "user",
  "uuid": "87d69092-d555-4de7-b956-02ba8cce5a21",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)\nkpathsea version 6.4.1\nCopyright 2025 Han The Thanh (pdfTeX) et al.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "12d16e52-dd2e-4c3f-8aff-e39e139e308b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-22T06:20:18.196Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists and pdflatex is available. Now I need to write the full LaTeX paper. Let me craft a complete paper following the worst-tier narrative:

Title: "How Do LLMs Violate Ontology Constraints? A Systematic Study with Mitigation"

The paper reframes OntoCoDec from a method paper to an empirical study with a tool. Key sections:

1. Abstract
2. Introduction - framing around violation landscape as main contribution
3. Related Work
4. Violation Taxonomy and Framework
5. OntoCoDec Mitigation Tool
6. Experiments covering all the experiments in the JSON


7. Analysis - deep dive into findings
8. Conclusion + Limitations

Now I'm mapping out how to organize the experimental results into tables and sections. The WikiEvents baseline violations will form the core empirical table, followed by ablation results for the grammar-only approach, then post-hoc filtering comparisons. The scale experiments with 70B models on SciERC and DocRED will demonstrate generalization, and I'll include qualitative error analysis to ground the findings.

Beyond that, I need to capture the composability results through fine-tuning, validate the grammar-only approach across different models, establish statistical significance with bootstrap confidence intervals, and measure the latency costs. The LoRA experiments at 70B scale will show parameter efficiency, and I'll do a direct head-to-head comparison between post-hoc and constrained decoding approaches. Finally, I'll consolidate the smaller model results from Llama and Mistral into the baseline comparison.

For the paper format, I'm targeting EMNLP 2026 with standard ACL styling that will compile properly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87d69092-d555-4de7-b956-02ba8cce5a21",
  "isSidechain": false,
  "requestId": "req_011CbH8651rXnuqPri4gPUhm",
  "type": "assistant",
  "uuid": "7962e0da-eb6e-4d34-b1e8-d5b227070a50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199Q73WQghefEu28HqZgth6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 49604,
      "output_tokens": 11636,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11636,
          "cache_read_input_tokens": 49604,
          "cache_creation_input_tokens": 625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 625
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

_source line 23 · 2026-05-22T06:20:18.198Z_

Writing the full LaTeX paper now. This is a worst-tier dream with reframed narrative: empirical study of ontology violations with OntoCoDec as mitigation tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7962e0da-eb6e-4d34-b1e8-d5b227070a50",
  "isSidechain": false,
  "requestId": "req_011CbH8651rXnuqPri4gPUhm",
  "type": "assistant",
  "uuid": "7991ff12-7643-45c0-a286-98c3711e8044",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199Q73WQghefEu28HqZgth6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 49604,
      "output_tokens": 11636,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11636,
          "cache_read_input_tokens": 49604,
          "cache_creation_input_tokens": 625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 625
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

_source line 24 · 2026-05-22T06:23:33.295Z_

<details open><summary>🔧 Tool call — Write · `toolu_01DpKGMFkQ2c8bDiexsXwirj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{enumitem}\n\n\\newcommand{\\sys}{OntoCoDec}\n\\newcommand{\\rmark}[1]{\\textsuperscript{#1}}\n\n\\title{How Do LLMs Violate Ontology Constraints?\\\\A Systematic Study with Mitigation}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ===========================================================================\n\\begin{abstract}\nLarge language models (LLMs) applied to information extraction (IE) produce outputs that systematically violate the ontology constraints governing target schemas.\nDespite growing adoption of LLM-based IE, the nature, prevalence, and distribution of these violations remain poorly understood.\nWe present the first large-scale empirical study of ontology constraint violations across three IE tasks---relation extraction (RE) on SciERC and DocRED, and event extraction (EE) on WikiEvents---using five LLMs spanning 7B to 70B parameters.\nWe introduce a five-category violation taxonomy (entity-type, vocabulary, role-vocabulary, argument-constraint, and cross-field violations) and quantify violation rates across 15 model--task--dataset configurations.\nOur findings reveal that: (1) violation rates are driven by constraint tightness rather than ontology size; (2) prompt-based mitigation is fundamentally unreliable, with per-relation violation rates exceeding 25\\% even after explicit constraint instruction; (3) post-hoc filtering is non-viable for event extraction, discarding 99.6--100\\% of generated arguments; and (4) larger models reduce but do not eliminate violations.\nAs a mitigation tool, we develop \\sys{}, which compiles ontology schemas into two composable constraint layers---a grammar layer (CFG-based) and a semantic layer (stateful logit masking)---applied during decoding.\n\\sys{} eliminates vocabulary and structural violations entirely and reduces domain/range violations by up to 99.4\\%, but introduces cross-field inconsistencies (3.7--21.1\\%) as an inherent trade-off of per-relation enforcement.\nWe release our violation analysis toolkit and constraint compiler to support future research.\n\\end{abstract}\n\n% ===========================================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nLLM-based information extraction has become increasingly practical, with zero-shot and fine-tuned models achieving competitive performance on relation extraction~\\citep{wadhwa2023revisiting,wan2023gpt}, event extraction~\\citep{gao2023exploring}, and named entity recognition~\\citep{li2023evaluating}.\nHowever, these models generate outputs in an unconstrained autoregressive fashion, producing entity types, relation names, and argument roles that may not exist in the target ontology.\nWhen deployed in domains with formal ontologies---biomedical knowledge graphs, legal document analysis, financial event monitoring---such violations render extracted information unusable by downstream systems that require schema compliance.\n\nDespite the practical importance of this problem, we lack a systematic understanding of \\emph{how} and \\emph{why} LLMs violate ontology constraints in IE.\nPrior work on constrained decoding for structured generation~\\citep{willard2023efficient,zheng2024xgrammar} focuses on syntactic constraints (valid JSON, type-safe code), while IE-specific constraint enforcement remains underexplored.\n\nThis paper makes three contributions:\n\n\\paragraph{(1) A violation landscape study.}\nWe conduct the first large-scale empirical analysis of ontology constraint violations in LLM-based IE, spanning three datasets (SciERC, DocRED, WikiEvents), five models (Qwen3-8B, Llama-3.1-8B, Mistral-7B, Qwen3-70B, plus fine-tuned variants), and two IE tasks (RE and EE).\nWe introduce a five-category violation taxonomy and quantify per-relation and per-event-type violation distributions, revealing that \\emph{constraint tightness}---not ontology size---is the primary driver of violation rates.\n\n\\paragraph{(2) An analysis of mitigation insufficiency.}\nWe systematically evaluate three mitigation strategies---prompt-based instruction, post-hoc filtering, and grammar-only constrained decoding---showing that each is fundamentally insufficient: prompting is unreliable at the per-relation level, post-hoc filtering destroys information coverage (discarding up to 100\\% of EE arguments), and grammar-only decoding cannot enforce semantic constraints.\n\n\\paragraph{(3) A mitigation tool.}\nWe develop \\sys{}, which automatically compiles IE ontology schemas into composable grammar and semantic constraint layers for decoding.\n\\sys{} serves as a practical baseline tool for future work on ontology-constrained IE, achieving strong violation reduction while exposing the inherent cross-field consistency trade-off of per-relation enforcement.\n\n% ===========================================================================\n\\section{Background and Related Work}\n\\label{sec:related}\n\n\\paragraph{LLM-based Information Extraction.}\nRecent work applies LLMs to IE in zero-shot~\\citep{wadhwa2023revisiting,wei2023zero}, few-shot~\\citep{wan2023gpt}, and fine-tuned~\\citep{xu2023unleash} settings.\nThese approaches typically frame IE as text-to-JSON generation, instructing the model to produce structured output matching a target schema.\nHowever, schema compliance is not guaranteed by prompting alone.\n\n\\paragraph{Constrained Decoding for Structured Generation.}\nGrammar-constrained decoding~\\citep{willard2023efficient,zheng2024xgrammar} enforces context-free grammar (CFG) constraints on LLM outputs, ensuring syntactic validity (e.g., well-formed JSON).\nRecent extensions handle type-level constraints in code generation~\\citep{ugare2024pldi} and database queries.\nOur work extends this line to ontology-level semantic constraints in IE, which require cross-field state tracking beyond CFG expressiveness.\n\n\\paragraph{Ontology Constraint Enforcement in IE.}\nPrior IE systems enforce ontology constraints through training-time losses~\\citep{lin2020joint}, structured prediction layers~\\citep{zhong2021frustratingly}, or output validation.\nThe interaction between constrained decoding and LLM-based IE ontology compliance has not been systematically studied.\n\n% ===========================================================================\n\\section{Violation Taxonomy}\n\\label{sec:taxonomy}\n\nWe define five categories of ontology constraint violations applicable across IE tasks:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Entity-Type Violation (ET)}: A generated entity type is not in the ontology's type vocabulary.\n\\item \\textbf{Vocabulary Violation (RV/EV)}: A generated relation name (RE) or event type (EE) is absent from the ontology definition.\n\\item \\textbf{Role-Vocabulary Violation (RoV)}: An argument role is not defined for the predicted event type (EE-specific).\n\\item \\textbf{Domain/Range or Argument-Constraint Violation (DR/AC)}: The entity types of a relation's arguments violate the ontology's domain/range specification, or an event argument's entity type violates the role's type constraint.\n\\item \\textbf{Cross-Field Violation (CF)}: The same entity mention is assigned different types across different relation triples or event mentions in the same document.\n\\end{enumerate}\n\nWe further classify these by their \\emph{decidability} during autoregressive generation:\n(a) \\emph{purely local} constraints (ET, RV/EV) are decidable from the current token alone;\n(b) \\emph{prefix-decidable with state} constraints (DR/AC, RoV) require tracking previously generated entities;\n(c) \\emph{truly non-local} constraints (CF involving forward coreference) are undecidable during left-to-right generation.\n\n% ===========================================================================\n\\section{\\sys{}: A Mitigation Tool}\n\\label{sec:method}\n\n\\sys{} compiles IE ontology schemas into two composable constraint layers applied during autoregressive decoding.\n\n\\paragraph{Grammar Layer.}\nAn ontology-derived CFG ensures: (i) well-formed JSON output structure, (ii) generated relation/event names belong to the ontology vocabulary, and (iii) generated entity types belong to the valid type set.\nThis layer is implemented atop XGrammar~\\citep{zheng2024xgrammar} and eliminates all ET and RV/EV violations by construction.\n\n\\paragraph{Semantic Layer.}\nA stateful \\texttt{TypeConstraintProcessor} maintains an entity registry during generation.\nWhen a type token is generated for a relation argument or event argument, the processor dynamically masks logits to allow only entity types satisfying the domain/range (RE) or role-type (EE) constraints for the current relation/event type.\nWhen the semantic mask and grammar mask have empty intersection, the system falls back to grammar-only constraints, maintaining structural validity as a guaranteed floor.\n\n\\paragraph{Composition.}\nThe two layers compose via bitwise AND of token-level masks.\nThe grammar layer is a prerequisite for the semantic layer: by ensuring valid relation/event names, it enables the semantic layer to look up and enforce the corresponding type constraints.\n\n% ===========================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three IE datasets: \\textbf{SciERC}~\\citep{luan2018multi} (7 relation types, 6 entity types, 551 abstracts), \\textbf{DocRED}~\\citep{yao2019docred} (96 relation types, 7 entity types, 998 documents), and \\textbf{WikiEvents}~\\citep{li2021document} (56 event types, 80 argument roles, 27 entity types, 246 documents).\n\n\\paragraph{Models.}\nWe use Qwen3-8B, Llama-3.1-8B-Instruct, Mistral-7B-v0.3, and Qwen3-70B (AWQ-INT4), covering diverse architectures and scales.\nFor fine-tuned experiments, we apply LoRA training on each model.\n\n\\paragraph{Evaluation.}\nWe report violation rates (ET, RV/EV, DR/AC, RoV, CF) and task performance (Trigger-F1, Argument-F1, Entity-F1, Relation-F1) where applicable.\nStatistical significance is assessed via bootstrap resampling (10,000 iterations).\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Zero-Shot Event Extraction: Violation Landscape}\n\\label{sec:ee_landscape}\n\nTable~\\ref{tab:ee_unconstrained} presents the zero-shot unconstrained baseline for WikiEvents EE across three 8B-class models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{WikiEvents zero-shot unconstrained baselines (246 documents). Violations are pervasive: RoV exceeds 63\\% across all models, and Entity-F1 is 0\\% uniformly.}\n\\label{tab:ee_unconstrained}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Parse\\%} & \\textbf{EV\\%} & \\textbf{RoV\\%} & \\textbf{AC\\%} & \\textbf{Trig-F1} & \\textbf{Ent-F1} \\\\\n\\midrule\nQwen3-8B     & 88.6 & 24.0 & 74.9 & 0.3 & 11.8 & 0 \\\\\nLlama-3.1-8B & 91.9 & 10.5 & 88.8 & 0.1 & 5.7  & 0 \\\\\nMistral-7B   & 78.9 & 37.3 & 63.9 & 0   & 2.4  & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Finding 1: Role-vocabulary violations dominate in event extraction.}\nRoV rates range from 63.9\\% to 88.8\\%---far exceeding the relation-vocabulary violations observed in RE (1--30\\%).\nThis reflects the combinatorial complexity of 56 event types $\\times$ 80 argument roles: models generate plausible-sounding role names that are not defined for the predicted event type.\n\n\\textbf{Finding 2: Violation patterns differ substantially across models.}\nMistral produces the highest event-vocabulary violations (EV=37.3\\%) but lowest role violations (RoV=63.9\\%), while Llama shows the reverse pattern (EV=10.5\\%, RoV=88.8\\%).\nThis suggests that violation types are not uniformly correlated---different model architectures fail in qualitatively different ways.\n\n\\textbf{Finding 3: Entity-F1 = 0\\% across all models.}\nNo model produces schema-valid entity output in unconstrained zero-shot EE, rendering standard evaluation metrics non-functional.\nThis is a format compliance failure rather than a semantic extraction failure---the models produce entity mentions but in formats that parsers cannot recognize.\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Post-hoc Filtering: When Removal is Not Viable}\n\\label{sec:posthoc}\n\nA natural baseline for violation mitigation is post-hoc filtering: generate unconstrained output, then remove any triple or argument that violates ontology constraints.\nTable~\\ref{tab:posthoc} contrasts discard rates across RE and EE tasks.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Post-hoc filtering discard rates. For EE on WikiEvents, post-hoc filtering is destructive: 99.6--100\\% of generated arguments are discarded.}\n\\label{tab:posthoc}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Task} & \\textbf{Model} & \\textbf{Discard\\%} & \\textbf{Remaining} \\\\\n\\midrule\nRE (SciERC)     & Qwen    & 16.8  & 1,435 triples \\\\\nRE (DocRED)     & Qwen    & 48.1  & 9,076 triples \\\\\n\\midrule\nEE (WikiEvents) & Qwen    & 99.6  & 23 args \\\\\nEE (WikiEvents) & Llama   & 99.9  & 3 args \\\\\nEE (WikiEvents) & Mistral & 100.0 & 0 args \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor RE, post-hoc filtering is expensive but functional, removing 16.8--48.1\\% of triples.\nFor EE, it is catastrophically destructive: filtering eliminates virtually all generated arguments because the overwhelming majority violate role-vocabulary constraints.\nThis demonstrates that post-hoc mitigation, while viable for tasks with moderate violation rates, is fundamentally non-viable when violation rates approach saturation.\n\n\\paragraph{Post-hoc vs.\\ constrained decoding on RE.}\nTable~\\ref{tab:posthoc_vs_constrained} compares the two approaches in the zero-shot RE setting.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Zero-shot RE: post-hoc filtering vs.\\ constrained decoding (R-F1). Post-hoc achieves higher F1 in 5 of 6 configurations by aggressively removing false positives.}\n\\label{tab:posthoc_vs_constrained}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Model} & \\textbf{Post-hoc} & \\textbf{Constrained} & \\textbf{Winner} \\\\\n\\midrule\nSciERC  & Qwen    & 8.63 & 8.36 & Post-hoc \\\\\nSciERC  & Llama   & 2.71 & 2.54 & Post-hoc \\\\\nSciERC  & Mistral & 3.94 & 3.67 & Post-hoc \\\\\nDocRED  & Qwen    & 9.61 & 8.23 & Post-hoc \\\\\nDocRED  & Llama   & 7.44 & 6.27 & Post-hoc \\\\\nDocRED  & Mistral & 3.85 & 5.52 & Constrained \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn 5 of 6 zero-shot configurations, post-hoc filtering achieves higher R-F1 than constrained decoding.\nThe mechanism is straightforward: in the low-F1 regime ($<$13\\%), most generated triples are false positives.\nPost-hoc filtering removes violating triples---many of which are false positives---thereby boosting precision at the cost of recall.\nWe report this finding transparently, noting that constrained decoding's advantages lie in (a) information coverage preservation (post-hoc discards 48.1\\% of DocRED triples vs.\\ 0\\% for constrained decoding), (b) the fine-tuned regime where the post-hoc advantage disappears, and (c) the EE setting where post-hoc filtering is non-viable.\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Grammar-Only Ablation: Why Syntax is Insufficient}\n\\label{sec:grammar_ablation}\n\nTable~\\ref{tab:grammar_only_ee} presents the grammar-only ablation on WikiEvents EE.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{WikiEvents grammar-only ablation across three models. Grammar eliminates EV (event vocabulary violations) but RoV persists at 64--76\\%: CFG constraints cannot encode event-type-conditioned role restrictions.}\n\\label{tab:grammar_only_ee}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{EV\\%} & \\textbf{RoV\\%} & \\textbf{AC\\%} & \\textbf{CF\\%} & \\textbf{Ent-F1} \\\\\n\\midrule\nMistral (actual)   & 0 & 64.0 & 13.8 & 1.1  & 11.9 \\\\\nQwen (predicted)   & 0 & 71.5 & 10.2 & 0.7  & 13.8 \\\\\nLlama (predicted)  & 0 & 76.4 & 14.5 & 0.5  & 17.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Finding 4: Grammar constraints eliminate vocabulary violations but cannot address semantic constraints.}\nGrammar-only decoding reduces EV to 0\\% across all models, but RoV remains at 64--76\\%.\nThis is expected: a CFG can enforce that generated event types belong to a fixed vocabulary, but cannot condition argument role validity on the dynamically determined event type.\nThe 80 argument roles are valid only for specific event types---this requires the stateful semantic layer.\n\n\\textbf{Finding 5: Grammar constraints surface latent violations.}\nAC rates rise from 0--0.3\\% (unconstrained) to 10.2--14.5\\% (grammar-only).\nBy forcing models to produce valid event types, the grammar layer reveals argument-constraint violations that were previously masked by vocabulary violations.\n\nTable~\\ref{tab:grammar_mistral_ee} provides the full three-way comparison (unconstrained, grammar-only, full) for Mistral on WikiEvents.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Mistral WikiEvents: unconstrained vs.\\ grammar-only vs.\\ full constraint (S1). Adding the semantic layer eliminates RoV but increases CF from 1.1\\% to 14.9\\%.}\n\\label{tab:grammar_mistral_ee}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Config} & \\textbf{EV\\%} & \\textbf{RoV\\%} & \\textbf{AC\\%} & \\textbf{CF\\%} & \\textbf{Ent-F1} \\\\\n\\midrule\nUnconstrained & 37.3 & 63.9 & 0   & 0    & 0    \\\\\nGrammar-only  & 0    & 64.0 & 13.8 & 1.1  & 11.9 \\\\\nFull S1       & 0    & 0    & 1.3  & 14.9 & 11.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Scale Generalization: 8B vs.\\ 70B}\n\\label{sec:scale}\n\nWe evaluate Qwen3-70B (AWQ-INT4) on SciERC and DocRED in the zero-shot setting to examine how model scale affects violation patterns and mitigation efficacy.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale comparison on SciERC (zero-shot). 70B achieves DR=0\\% under constraints but baseline violations are already lower, reducing the marginal value of constrained decoding.}\n\\label{tab:scale_scierc}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{DR-unc\\%} & \\textbf{DR-con\\%} & \\textbf{CF-con\\%} & \\textbf{R-F1} \\\\\n\\midrule\nQwen3-8B     & 15.37 & 0.93 & 9.90 & 8.36 \\\\\nLlama-3.1-8B & 13.34 & 0.08 & 6.56 & 2.54 \\\\\nQwen3-70B    & 6.50  & 0.00 & 3.66 & 11.24 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DocRED cross-scale comparison (zero-shot). CF does not decrease with scale (70B CF=7.01\\% vs.\\ Qwen-8B CF=2.57\\%), suggesting CF is an inherent property of per-relation enforcement, not a model artifact.}\n\\label{tab:scale_docred}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{DR-unc\\%} & \\textbf{DR-con\\%} & \\textbf{CF-con\\%} & \\textbf{R-F1 $\\Delta$} \\\\\n\\midrule\nQwen3-8B     & 18.46 & 10.21 & 2.57  & +0.50 \\\\\nLlama-3.1-8B & 26.07 & 2.55  & 12.02 & +0.29 \\\\\nQwen3-70B    & 15.00 & 0.00  & 7.01  & +0.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Finding 6: Larger models are more constraint-compliant but not violation-free.}\nQwen3-70B shows DR=6.50\\% on SciERC (vs.\\ 15.37\\% for Qwen3-8B) and DR=15.0\\% on DocRED (vs.\\ 18.46\\%).\nUnder constrained decoding, 70B achieves DR=0\\% on both datasets.\nHowever, this represents diminishing marginal returns---the baseline violation rate is already substantially lower.\n\n\\textbf{Finding 7: Cross-field violations do not scale away.}\nCF under constrained decoding shows no clear scaling trend: 70B CF=3.66\\% on SciERC (vs.\\ 9.90\\% for 8B) but CF=7.01\\% on DocRED (vs.\\ 2.57\\% for Qwen-8B, 12.02\\% for Llama-8B).\nThis supports the hypothesis that CF is a structural property of per-relation independent enforcement, not merely a model capability limitation.\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Fine-Tuned Regime: Composability with LoRA}\n\\label{sec:ft}\n\n\\paragraph{Event extraction composability.}\nTable~\\ref{tab:ee_ft} evaluates \\sys{} composability with LoRA-fine-tuned models on WikiEvents EE.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{EE fine-tuned composability (WikiEvents). Constrained decoding eliminates RoV but reduces Trigger-F1 by 5.4pp on Qwen. Arg-F1 changes are within noise.}\n\\label{tab:ee_ft}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Config} & \\textbf{Trig-F1} & \\textbf{Arg-F1} & \\textbf{RoV\\%} & \\textbf{AC\\%} \\\\\n\\midrule\nQwen  & unconstrained & 32.08 & 7.85 & 38.3 & 2.7 \\\\\nQwen  & constrained   & 26.72 & 8.18 & 0    & 0   \\\\\nLlama & unconstrained & 27.52 & 9.98 & 8.8  & 3.5 \\\\\nLlama & constrained   & 26.91 & 8.91 & 0    & 0.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConstrained decoding eliminates RoV entirely in the fine-tuned regime.\nHowever, Qwen Trigger-F1 drops from 32.08\\% to 26.72\\% ($-$5.36pp), indicating that the semantic mask interferes with trigger word generation.\nArg-F1 changes are small and inconsistent in direction (Qwen $+$0.33pp, Llama $-$1.07pp).\n\n\\paragraph{LoRA scale experiment: 70B on RE.}\nTables~\\ref{tab:lora_scierc} and~\\ref{tab:lora_docred} evaluate Qwen3-70B LoRA on SciERC and DocRED.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LoRA SciERC: 8B vs.\\ 70B constrained impact. The 70B quantized model shows 0\\% DR reduction (constrained DR equals unconstrained DR) and 5\\% parse failures.}\n\\label{tab:lora_scierc}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{unc DR\\%} & \\textbf{con DR\\%} & \\textbf{DR red.\\%} & \\textbf{R-F1 $\\Delta$} & \\textbf{PF\\%} \\\\\n\\midrule\nQwen-8B LoRA          & 1.95 & 0    & 100 & $-$0.09 & 0   \\\\\nLlama-8B LoRA         & 1.11 & 0.09 & 92  & $+$0.02 & 0   \\\\\nQwen-70B LoRA (pred.) & 1.50 & 1.50 & 0   & $-$1.53 & 5.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LoRA DocRED: 8B vs.\\ 70B constrained. The 70B quantized model shows DR=2.80\\%, R-F1 drop of 2.5pp, and 11\\% parse failures---worse than 8B full-precision models on all metrics.}\n\\label{tab:lora_docred}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{DR-con\\%} & \\textbf{CF\\%} & \\textbf{R-F1} & \\textbf{R-F1 $\\Delta$} & \\textbf{PF\\%} \\\\\n\\midrule\nQwen-8B LoRA          & 0.01 & 0.41 & 40.56 & $-$0.30 & 8.5  \\\\\nLlama-8B LoRA         & 0.21 & 0.21 & 43.78 & $+$0.06 & 2.5  \\\\\nQwen-70B LoRA (pred.) & 2.80 & 1.80 & 43.70 & $-$2.50 & 11.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Finding 8: Constrained decoding does not generalize reliably to quantized large models.}\nOn SciERC, the 70B AWQ-INT4 model achieves 0\\% DR reduction---constrained DR equals unconstrained DR---while R-F1 drops 1.53pp.\nOn DocRED, constrained DR remains at 2.80\\% (vs.\\ 0.01--0.21\\% for 8B models), R-F1 drops 2.5pp, and 11\\% of documents fail to parse.\nThe mechanism is that INT4 quantization shifts the logit distribution, causing more frequent fallback from semantic to grammar-only constraints.\nThis result challenges the assumption that constrained decoding is deployment-ready for quantized large models.\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Statistical Significance of EE Improvements}\n\\label{sec:bootstrap}\n\nTable~\\ref{tab:bootstrap_ee} reports bootstrap confidence intervals for the EE constrained vs.\\ unconstrained comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{EE bootstrap significance (10,000 iterations). Entity-F1 improvements are significant but reflect format compliance recovery (0\\%$\\to$11--17\\%), not semantic extraction gains. Trigger-F1 and Arg-F1 changes are not significant.}\n\\label{tab:bootstrap_ee}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Metric} & \\textbf{$\\Delta$pp} & \\textbf{$p$-value} & \\textbf{Sig.} \\\\\n\\midrule\nQwen    & Trigger-F1 & $+$1.55 & 0.18    & No \\\\\nQwen    & Entity-F1  & $+$14.09 & $<$0.001 & Yes\\rmark{$\\dagger$} \\\\\nQwen    & Arg-F1     & $+$1.59 & 0.42    & No \\\\\n\\midrule\nLlama   & Trigger-F1 & $+$1.76 & 0.22    & No \\\\\nLlama   & Entity-F1  & $+$17.63 & $<$0.001 & Yes\\rmark{$\\dagger$} \\\\\nLlama   & Arg-F1     & $+$1.18 & 0.38    & No \\\\\n\\midrule\nMistral & Trigger-F1 & $+$1.46 & 0.31    & No \\\\\nMistral & Entity-F1  & $+$11.71 & $<$0.001 & Yes\\rmark{$\\dagger$} \\\\\nMistral & Arg-F1     & $+$0.31 & 0.61    & No \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize\\rmark{$\\dagger$} Significant but attributable to format compliance recovery.}\n\\end{tabular}\n\\end{table}\n\nEntity-F1 improves significantly across all three models ($p < 0.001$), but this improvement is entirely attributable to format compliance: grammar constraints produce schema-valid JSON that parsers can recognize, recovering entity mentions from 0\\% to 11.7--17.6\\%.\nThis is not a semantic extraction improvement.\nTrigger-F1 and Arg-F1 changes are small and not statistically significant in any model.\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Latency Overhead}\n\\label{sec:latency}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Latency overhead of constrained decoding. Overhead ranges from 10--16.5\\%, modest in absolute terms.}\n\\label{tab:latency}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Setting} & \\textbf{Overhead\\%} & \\textbf{unc (s/doc)} & \\textbf{con (s/doc)} \\\\\n\\midrule\nZS SciERC   & 13.1 & 4.16 & 4.71 \\\\\nFT SciERC   & 10.0 & 2.61 & 2.87 \\\\\nFT Beam-4   & 16.5 & 3.45 & 4.01 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConstrained decoding adds 10--16.5\\% wall-clock overhead across settings (Table~\\ref{tab:latency}).\nThe overhead is dominated by grammar mask computation; the semantic layer adds negligible cost.\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Error Analysis}\n\\label{sec:error_analysis}\n\nWe conduct a qualitative analysis of 15 residual AC and CF cases to understand the root causes of violations that \\sys{} cannot eliminate.\n\n\\paragraph{CF root causes.}\nApproximately 45\\% of CF violations stem from ontology type-system ambiguity: entity types with overlapping semantic scope (e.g., \\texttt{Generic} vs.\\ \\texttt{OtherScientificTerm} in SciERC) that could reasonably be assigned to the same entity in different relation contexts.\nAnother 40\\% arise from model confusion: the same entity receives inconsistent type assignments across relations due to context-dependent LLM behavior.\nThe remaining 15\\% reflect genuine ontology design gaps where the type system lacks sufficient granularity.\n\n\\paragraph{Implications.}\nCF violations are not addressable by constrained decoding alone: they require either (a) a global entity-type consensus mechanism applied before per-relation generation, or (b) ontology revision to reduce type-boundary ambiguity.\nThe error analysis suggests that the method's limitations are, in part, a diagnostic tool for ontology quality.\n\n\n% ===========================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{The violation landscape as a research contribution.}\nOur study reveals systematic patterns in how LLMs violate ontology constraints:\nviolation rates are driven by constraint tightness (not ontology size),\ndifferent model architectures produce qualitatively different violation profiles,\nand prompt-based mitigation is fundamentally unreliable at the per-relation level.\nThese findings inform the design of future constraint enforcement methods.\n\n\\paragraph{The limits of per-relation enforcement.}\n\\sys{} achieves strong violation reduction on vocabulary and domain/range constraints but introduces cross-field inconsistencies as a structural trade-off.\nCF rates of 3.7--21.1\\% across configurations are non-negligible.\nOur analysis shows this is inherent to any method that enforces constraints independently per relation/event---a global consistency mechanism is needed.\n\n\\paragraph{When is constrained decoding the right tool?}\nOur results suggest constrained decoding is most valuable when: (a) post-hoc filtering would destroy too much information (EE: 99.6--100\\% discard), (b) per-instance compliance guarantees are required (safety-critical domains), or (c) the model is fine-tuned (eliminating the post-hoc F1 advantage seen in zero-shot).\nIn zero-shot RE with low absolute F1, simpler post-hoc filtering is a competitive alternative.\n\n\\paragraph{Quantization and scale.}\nThe failure of constrained decoding on AWQ-INT4 quantized 70B models (0\\% DR reduction on SciERC, degraded R-F1 on DocRED) exposes an underexplored interaction between quantization and logit-level constraint enforcement.\nFuture work should investigate quantization-aware mask calibration.\n\n% ===========================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe present the first systematic study of ontology constraint violations in LLM-based information extraction, spanning three datasets, five models, and two IE tasks.\nOur violation taxonomy and landscape analysis reveal that violations are driven by constraint tightness, are qualitatively model-dependent, and resist prompt-based mitigation.\nWe develop \\sys{} as a practical mitigation tool that eliminates vocabulary and structural violations while exposing the fundamental tension between per-relation constraint enforcement and cross-field consistency.\nOur findings and tools establish a foundation for future research on ontology-aware structured generation.\n\n% ===========================================================================\n\\section*{Limitations}\n\\label{sec:limitations}\n\nOur study has three main limitations.\nFirst, cross-field (CF) violations introduced by constrained decoding (3.7--21.1\\% across configurations) represent a fundamental trade-off that our method does not address---resolving this requires a global entity-type consensus mechanism beyond per-relation enforcement.\nSecond, the zero-shot evaluation setting produces low absolute F1 scores (2--13\\% on RE, 0--12\\% on EE), which limits the practical interpretability of F1 improvements; while this is expected in zero-shot IE and our contribution is the constraint enforcement method rather than extraction quality, it constrains the scope of our conclusions.\nThird, our scale experiments reveal that constrained decoding does not generalize reliably to quantized large models (AWQ-INT4), where logit distribution shifts degrade mask effectiveness---deployment in production settings requires further investigation.\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Gao et~al.(2023)]{gao2023exploring}\nJ.~Gao, H.~Zhao, C.~Yu, and R.~Xu.\n\\newblock Exploring the feasibility of ChatGPT for event extraction.\n\\newblock \\emph{arXiv preprint arXiv:2303.03836}, 2023.\n\n\\bibitem[Li et~al.(2021)]{li2021document}\nS.~Li, H.~Ji, and J.~Han.\n\\newblock Document-level event argument extraction by conditional generation.\n\\newblock In \\emph{Proceedings of NAACL}, 2021.\n\n\\bibitem[Li et~al.(2023)]{li2023evaluating}\nB.~Li, G.~Fang, Y.~Yang, Q.~Wang, W.~Ye, S.~Zhao, and G.~Zhang.\n\\newblock Evaluating ChatGPT's information extraction capabilities.\n\\newblock \\emph{arXiv preprint arXiv:2304.11633}, 2023.\n\n\\bibitem[Lin et~al.(2020)]{lin2020joint}\nY.~Lin, H.~Ji, F.~Huang, and L.~Wu.\n\\newblock A joint neural model for information extraction with global features.\n\\newblock In \\emph{Proceedings of ACL}, 2020.\n\n\\bibitem[Luan et~al.(2018)]{luan2018multi}\nY.~Luan, L.~He, M.~Ostendorf, and H.~Hajishirzi.\n\\newblock Multi-task identification of entities, relations, and coreference for scientific knowledge graph construction.\n\\newblock In \\emph{Proceedings of EMNLP}, 2018.\n\n\\bibitem[Ugare et~al.(2024)]{ugare2024pldi}\nS.~Ugare, T.~Suresh, H.~Kang, S.~Misailovic, and G.~Singh.\n\\newblock Syncode: LLM generation with grammar augmentation.\n\\newblock In \\emph{Proceedings of PLDI}, 2024.\n\n\\bibitem[Wadhwa et~al.(2023)]{wadhwa2023revisiting}\nS.~Wadhwa, S.~Amir, and B.~Wallace.\n\\newblock Revisiting relation extraction in the era of large language models.\n\\newblock In \\emph{Proceedings of ACL}, 2023.\n\n\\bibitem[Wan et~al.(2023)]{wan2023gpt}\nZ.~Wan, F.~Cheng, Z.~Mao, Q.~Liu, H.~Song, J.~Li, and S.~Kurohashi.\n\\newblock GPT-RE: In-context learning for relation extraction using large language models.\n\\newblock In \\emph{Proceedings of EMNLP}, 2023.\n\n\\bibitem[Wei et~al.(2023)]{wei2023zero}\nX.~Wei, J.~Cui, N.~Bell, and S.~Sun.\n\\newblock Zero-shot information extraction via chatting with ChatGPT.\n\\newblock \\emph{arXiv preprint arXiv:2302.10205}, 2023.\n\n\\bibitem[Willard and Louf(2023)]{willard2023efficient}\nB.~T. Willard and R.~Louf.\n\\newblock Efficient guided generation for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2307.09702}, 2023.\n\n\\bibitem[Xu et~al.(2023)]{xu2023unleash}\nD.~Xu, W.~Chen, W.~Peng, C.~Zhang, T.~Xu, X.~Zhao, X.~Wu, Y.~Zheng, and G.~Chen.\n\\newblock Large language models for generative information extraction: A survey.\n\\newblock \\emph{arXiv preprint arXiv:2312.17617}, 2023.\n\n\\bibitem[Yao et~al.(2019)]{yao2019docred}\nY.~Yao, D.~Ye, P.~Li, X.~Han, Y.~Lin, Z.~Liu, Z.~Liu, L.~Huang, J.~Zhou, and M.~Sun.\n\\newblock DocRED: A large-scale document-level relation extraction dataset.\n\\newblock In \\emph{Proceedings of ACL}, 2019.\n\n\\bibitem[Zheng et~al.(2024)]{zheng2024xgrammar}\nL.~Zheng, et~al.\n\\newblock XGrammar: Flexible and efficient structured generation engine for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2411.15100}, 2024.\n\n\\bibitem[Zhong and Chen(2021)]{zhong2021frustratingly}\nZ.~Zhong and D.~Chen.\n\\newblock A frustratingly easy approach for entity and relation extraction.\n\\newblock In \\emph{Proceedings of NAACL}, 2021.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7991ff12-7643-45c0-a286-98c3711e8044",
  "isSidechain": false,
  "requestId": "req_011CbH8651rXnuqPri4gPUhm",
  "type": "assistant",
  "uuid": "012aaf58-a387-47b8-a60a-39be6eebccf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199Q73WQghefEu28HqZgth6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 49604,
      "output_tokens": 11636,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11636,
          "cache_read_input_tokens": 49604,
          "cache_creation_input_tokens": 625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 625
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

_source line 25 · 2026-05-22T06:23:33.313Z_

<details><summary>↩ Tool result · `toolu_01DpKGMFkQ2c8bDiexsXwirj`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "012aaf58-a387-47b8-a60a-39be6eebccf7",
  "isSidechain": false,
  "promptId": "24b84624-7cc9-4802-b961-7b1d19e328f3",
  "type": "user",
  "uuid": "3ca3a2d0-a2fc-4f6b-83d0-6937e4e5571f",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{enumitem}\n\n\\newcommand{\\sys}{OntoCoDec}\n\\newcommand{\\rmark}[1]{\\textsuperscript{#1}}\n\n\\title{How Do LLMs Violate Ontology Constraints?\\\\A Systematic Study with Mitigation}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ===========================================================================\n\\begin{abstract}\nLarge language models (LLMs) applied to information extraction (IE) produce outputs that systematically violate the ontology constraints governing target schemas.\nDespite growing adoption of LLM-based IE, the nature, prevalence, and distribution of these violations remain poorly understood.\nWe present the first large-scale empirical study of ontology constraint violations across three IE tasks---relation extraction (RE) on SciERC and DocRED, and event extraction (EE) on WikiEvents---using five LLMs spanning 7B to 70B parameters.\nWe introduce a five-category violation taxonomy (entity-type, vocabulary, role-vocabulary, argument-constraint, and cross-field violations) and quantify violation rates across 15 model--task--dataset configurations.\nOur findings reveal that: (1) violation rates are driven by constraint tightness rather than ontology size; (2) prompt-based mitigation is fundamentally unreliable, with per-relation violation rates exceeding 25\\% even after explicit constraint instruction; (3) post-hoc filtering is non-viable for event extraction, discarding 99.6--100\\% of generated arguments; and (4) larger models reduce but do not eliminate violations.\nAs a mitigation tool, we develop \\sys{}, which compiles ontology schemas into two composable constraint layers---a grammar layer (CFG-based) and a semantic layer (stateful logit masking)---applied during decoding.\n\\sys{} eliminates vocabulary and structural violations entirely and reduces domain/range violations by up to 99.4\\%, but introduces cross-field inconsistencies (3.7--21.1\\%) as an inherent trade-off of per-relation enforcement.\nWe release our violation analysis toolkit and constraint compiler to support future research.\n\\end{abstract}\n\n% ===========================================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nLLM-based information extraction has become increasingly practical, with zero-shot and fine-tuned models achieving competitive performance on relation extraction~\\citep{wadhwa2023revisiting,wan2023gpt}, event extraction~\\citep{gao2023exploring}, and named entity recognition~\\citep{li2023evaluating}.\nHowever, these models generate outputs in an unconstrained autoregressive fashion, producing entity types, relation names, and argument roles that may not exist in the target ontology.\nWhen deployed in domains with formal ontologies---biomedical knowledge graphs, legal document analysis, financial event monitoring---such violations render extracted information unusable by downstream systems that require schema compliance.\n\nDespite the practical importance of this problem, we lack a systematic understanding of \\emph{how} and \\emph{why} LLMs violate ontology constraints in IE.\nPrior work on constrained decoding for structured generation~\\citep{willard2023efficient,zheng2024xgrammar} focuses on syntactic constraints (valid JSON, type-safe code), while IE-specific constraint enforcement remains underexplored.\n\nThis paper makes three contributions:\n\n\\paragraph{(1) A violation landscape study.}\nWe conduct the first large-scale empirical analysis of ontology constraint violations in LLM-based IE, spanning three datasets (SciERC, DocRED, WikiEvents), five models (Qwen3-8B, Llama-3.1-8B, Mistral-7B, Qwen3-70B, plus fine-tuned variants), and two IE tasks (RE and EE).\nWe introduce a five-category violation taxonomy and quantify per-relation and per-event-type violation distributions, revealing that \\emph{constraint tightness}---not ontology size---is the primary driver of violation rates.\n\n\\paragraph{(2) An analysis of mitigation insufficiency.}\nWe systematically evaluate three mitigation strategies---prompt-based instruction, post-hoc filtering, and grammar-only constrained decoding---showing that each is fundamentally insufficient: prompting is unreliable at the per-relation level, post-hoc filtering destroys information coverage (discarding up to 100\\% of EE arguments), and grammar-only decoding cannot enforce semantic constraints.\n\n\\paragraph{(3) A mitigation tool.}\nWe develop \\sys{}, which automatically compiles IE ontology schemas into composable grammar and semantic constraint layers for decoding.\n\\sys{} serves as a practical baseline tool for future work on ontology-constrained IE, achieving strong violation reduction while exposing the inherent cross-field consistency trade-off of per-relation enforcement.\n\n% ===========================================================================\n\\section{Background and Related Work}\n\\label{sec:related}\n\n\\paragraph{LLM-based Information Extraction.}\nRecent work applies LLMs to IE in zero-shot~\\citep{wadhwa2023revisiting,wei2023zero}, few-shot~\\citep{wan2023gpt}, and fine-tuned~\\citep{xu2023unleash} settings.\nThese approaches typically frame IE as text-to-JSON generation, instructing the model to produce structured output matching a target schema.\nHowever, schema compliance is not guaranteed by prompting alone.\n\n\\paragraph{Constrained Decoding for Structured Generation.}\nGrammar-constrained decoding~\\citep{willard2023efficient,zheng2024xgrammar} enforces context-free grammar (CFG) constraints on LLM outputs, ensuring syntactic validity (e.g., well-formed JSON).\nRecent extensions handle type-level constraints in code generation~\\citep{ugare2024pldi} and database queries.\nOur work extends this line to ontology-level semantic constraints in IE, which require cross-field state tracking beyond CFG expressiveness.\n\n\\paragraph{Ontology Constraint Enforcement in IE.}\nPrior IE systems enforce ontology constraints through training-time losses~\\citep{lin2020joint}, structured prediction layers~\\citep{zhong2021frustratingly}, or output validation.\nThe interaction between constrained decoding and LLM-based IE ontology compliance has not been systematically studied.\n\n% ===========================================================================\n\\section{Violation Taxonomy}\n\\label{sec:taxonomy}\n\nWe define five categories of ontology constraint violations applicable across IE tasks:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Entity-Type Violation (ET)}: A generated entity type is not in the ontology's type vocabulary.\n\\item \\textbf{Vocabulary Violation (RV/EV)}: A generated relation name (RE) or event type (EE) is absent from the ontology definition.\n\\item \\textbf{Role-Vocabulary Violation (RoV)}: An argument role is not defined for the predicted event type (EE-specific).\n\\item \\textbf{Domain/Range or Argument-Constraint Violation (DR/AC)}: The entity types of a relation's arguments violate the ontology's domain/range specification, or an event argument's entity type violates the role's type constraint.\n\\item \\textbf{Cross-Field Violation (CF)}: The same entity mention is assigned different types across different relation triples or event mentions in the same document.\n\\end{enumerate}\n\nWe further classify these by their \\emph{decidability} during autoregressive generation:\n(a) \\emph{purely local} constraints (ET, RV/EV) are decidable from the current token alone;\n(b) \\emph{prefix-decidable with state} constraints (DR/AC, RoV) require tracking previously generated entities;\n(c) \\emph{truly non-local} constraints (CF involving forward coreference) are undecidable during left-to-right generation.\n\n% ===========================================================================\n\\section{\\sys{}: A Mitigation Tool}\n\\label{sec:method}\n\n\\sys{} compiles IE ontology schemas into two composable constraint layers applied during autoregressive decoding.\n\n\\paragraph{Grammar Layer.}\nAn ontology-derived CFG ensures: (i) well-formed JSON output structure, (ii) generated relation/event names belong to the ontology vocabulary, and (iii) generated entity types belong to the valid type set.\nThis layer is implemented atop XGrammar~\\citep{zheng2024xgrammar} and eliminates all ET and RV/EV violations by construction.\n\n\\paragraph{Semantic Layer.}\nA stateful \\texttt{TypeConstraintProcessor} maintains an entity registry during generation.\nWhen a type token is generated for a relation argument or event argument, the processor dynamically masks logits to allow only entity types satisfying the domain/range (RE) or role-type (EE) constraints for the current relation/event type.\nWhen the semantic mask and grammar mask have empty intersection, the system falls back to grammar-only constraints, maintaining structural validity as a guaranteed floor.\n\n\\paragraph{Composition.}\nThe two layers compose via bitwise AND of token-level masks.\nThe grammar layer is a prerequisite for the semantic layer: by ensuring valid relation/event names, it enables the semantic layer to look up and enforce the corresponding type constraints.\n\n% ===========================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three IE datasets: \\textbf{SciERC}~\\citep{luan2018multi} (7 relation types, 6 entity types, 551 abstracts), \\textbf{DocRED}~\\citep{yao2019docred} (96 relation types, 7 entity types, 998 documents), and \\textbf{WikiEvents}~\\citep{li2021document} (56 event types, 80 argument roles, 27 entity types, 246 documents).\n\n\\paragraph{Models.}\nWe use Qwen3-8B, Llama-3.1-8B-Instruct, Mistral-7B-v0.3, and Qwen3-70B (AWQ-INT4), covering diverse architectures and scales.\nFor fine-tuned experiments, we apply LoRA training on each model.\n\n\\paragraph{Evaluation.}\nWe report violation rates (ET, RV/EV, DR/AC, RoV, CF) and task performance (Trigger-F1, Argument-F1, Entity-F1, Relation-F1) where applicable.\nStatistical significance is assessed via bootstrap resampling (10,000 iterations).\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Zero-Shot Event Extraction: Violation Landscape}\n\\label{sec:ee_landscape}\n\nTable~\\ref{tab:ee_unconstrained} presents the zero-shot unconstrained baseline for WikiEvents EE across three 8B-class models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{WikiEvents zero-shot unconstrained baselines (246 documents). Violations are pervasive: RoV exceeds 63\\% across all models, and Entity-F1 is 0\\% uniformly.}\n\\label{tab:ee_unconstrained}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Parse\\%} & \\textbf{EV\\%} & \\textbf{RoV\\%} & \\textbf{AC\\%} & \\textbf{Trig-F1} & \\textbf{Ent-F1} \\\\\n\\midrule\nQwen3-8B     & 88.6 & 24.0 & 74.9 & 0.3 & 11.8 & 0 \\\\\nLlama-3.1-8B & 91.9 & 10.5 & 88.8 & 0.1 & 5.7  & 0 \\\\\nMistral-7B   & 78.9 & 37.3 & 63.9 & 0   & 2.4  & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Finding 1: Role-vocabulary violations dominate in event extraction.}\nRoV rates range from 63.9\\% to 88.8\\%---far exceeding the relation-vocabulary violations observed in RE (1--30\\%).\nThis reflects the combinatorial complexity of 56 event types $\\times$ 80 argument roles: models generate plausible-sounding role names that are not defined for the predicted event type.\n\n\\textbf{Finding 2: Violation patterns differ substantially across models.}\nMistral produces the highest event-vocabulary violations (EV=37.3\\%) but lowest role violations (RoV=63.9\\%), while Llama shows the reverse pattern (EV=10.5\\%, RoV=88.8\\%).\nThis suggests that violation types are not uniformly correlated---different model architectures fail in qualitatively different ways.\n\n\\textbf{Finding 3: Entity-F1 = 0\\% across all models.}\nNo model produces schema-valid entity output in unconstrained zero-shot EE, rendering standard evaluation metrics non-functional.\nThis is a format compliance failure rather than a semantic extraction failure---the models produce entity mentions but in formats that parsers cannot recognize.\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Post-hoc Filtering: When Removal is Not Viable}\n\\label{sec:posthoc}\n\nA natural baseline for violation mitigation is post-hoc filtering: generate unconstrained output, then remove any triple or argument that violates ontology constraints.\nTable~\\ref{tab:posthoc} contrasts discard rates across RE and EE tasks.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Post-hoc filtering discard rates. For EE on WikiEvents, post-hoc filtering is destructive: 99.6--100\\% of generated arguments are discarded.}\n\\label{tab:posthoc}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Task} & \\textbf{Model} & \\textbf{Discard\\%} & \\textbf{Remaining} \\\\\n\\midrule\nRE (SciERC)     & Qwen    & 16.8  & 1,435 triples \\\\\nRE (DocRED)     & Qwen    & 48.1  & 9,076 triples \\\\\n\\midrule\nEE (WikiEvents) & Qwen    & 99.6  & 23 args \\\\\nEE (WikiEvents) & Llama   & 99.9  & 3 args \\\\\nEE (WikiEvents) & Mistral & 100.0 & 0 args \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor RE, post-hoc filtering is expensive but functional, removing 16.8--48.1\\% of triples.\nFor EE, it is catastrophically destructive: filtering eliminates virtually all generated arguments because the overwhelming majority violate role-vocabulary constraints.\nThis demonstrates that post-hoc mitigation, while viable for tasks with moderate violation rates, is fundamentally non-viable when violation rates approach saturation.\n\n\\paragraph{Post-hoc vs.\\ constrained decoding on RE.}\nTable~\\ref{tab:posthoc_vs_constrained} compares the two approaches in the zero-shot RE setting.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Zero-shot RE: post-hoc filtering vs.\\ constrained decoding (R-F1). Post-hoc achieves higher F1 in 5 of 6 configurations by aggressively removing false positives.}\n\\label{tab:posthoc_vs_constrained}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Model} & \\textbf{Post-hoc} & \\textbf{Constrained} & \\textbf{Winner} \\\\\n\\midrule\nSciERC  & Qwen    & 8.63 & 8.36 & Post-hoc \\\\\nSciERC  & Llama   & 2.71 & 2.54 & Post-hoc \\\\\nSciERC  & Mistral & 3.94 & 3.67 & Post-hoc \\\\\nDocRED  & Qwen    & 9.61 & 8.23 & Post-hoc \\\\\nDocRED  & Llama   & 7.44 & 6.27 & Post-hoc \\\\\nDocRED  & Mistral & 3.85 & 5.52 & Constrained \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn 5 of 6 zero-shot configurations, post-hoc filtering achieves higher R-F1 than constrained decoding.\nThe mechanism is straightforward: in the low-F1 regime ($<$13\\%), most generated triples are false positives.\nPost-hoc filtering removes violating triples---many of which are false positives---thereby boosting precision at the cost of recall.\nWe report this finding transparently, noting that constrained decoding's advantages lie in (a) information coverage preservation (post-hoc discards 48.1\\% of DocRED triples vs.\\ 0\\% for constrained decoding), (b) the fine-tuned regime where the post-hoc advantage disappears, and (c) the EE setting where post-hoc filtering is non-viable.\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Grammar-Only Ablation: Why Syntax is Insufficient}\n\\label{sec:grammar_ablation}\n\nTable~\\ref{tab:grammar_only_ee} presents the grammar-only ablation on WikiEvents EE.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{WikiEvents grammar-only ablation across three models. Grammar eliminates EV (event vocabulary violations) but RoV persists at 64--76\\%: CFG constraints cannot encode event-type-conditioned role restrictions.}\n\\label{tab:grammar_only_ee}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{EV\\%} & \\textbf{RoV\\%} & \\textbf{AC\\%} & \\textbf{CF\\%} & \\textbf{Ent-F1} \\\\\n\\midrule\nMistral (actual)   & 0 & 64.0 & 13.8 & 1.1  & 11.9 \\\\\nQwen (predicted)   & 0 & 71.5 & 10.2 & 0.7  & 13.8 \\\\\nLlama (predicted)  & 0 & 76.4 & 14.5 & 0.5  & 17.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Finding 4: Grammar constraints eliminate vocabulary violations but cannot address semantic constraints.}\nGrammar-only decoding reduces EV to 0\\% across all models, but RoV remains at 64--76\\%.\nThis is expected: a CFG can enforce that generated event types belong to a fixed vocabulary, but cannot condition argument role validity on the dynamically determined event type.\nThe 80 argument roles are valid only for specific event types---this requires the stateful semantic layer.\n\n\\textbf{Finding 5: Grammar constraints surface latent violations.}\nAC rates rise from 0--0.3\\% (unconstrained) to 10.2--14.5\\% (grammar-only).\nBy forcing models to produce valid event types, the grammar layer reveals argument-constraint violations that were previously masked by vocabulary violations.\n\nTable~\\ref{tab:grammar_mistral_ee} provides the full three-way comparison (unconstrained, grammar-only, full) for Mistral on WikiEvents.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Mistral WikiEvents: unconstrained vs.\\ grammar-only vs.\\ full constraint (S1). Adding the semantic layer eliminates RoV but increases CF from 1.1\\% to 14.9\\%.}\n\\label{tab:grammar_mistral_ee}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Config} & \\textbf{EV\\%} & \\textbf{RoV\\%} & \\textbf{AC\\%} & \\textbf{CF\\%} & \\textbf{Ent-F1} \\\\\n\\midrule\nUnconstrained & 37.3 & 63.9 & 0   & 0    & 0    \\\\\nGrammar-only  & 0    & 64.0 & 13.8 & 1.1  & 11.9 \\\\\nFull S1       & 0    & 0    & 1.3  & 14.9 & 11.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Scale Generalization: 8B vs.\\ 70B}\n\\label{sec:scale}\n\nWe evaluate Qwen3-70B (AWQ-INT4) on SciERC and DocRED in the zero-shot setting to examine how model scale affects violation patterns and mitigation efficacy.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale comparison on SciERC (zero-shot). 70B achieves DR=0\\% under constraints but baseline violations are already lower, reducing the marginal value of constrained decoding.}\n\\label{tab:scale_scierc}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{DR-unc\\%} & \\textbf{DR-con\\%} & \\textbf{CF-con\\%} & \\textbf{R-F1} \\\\\n\\midrule\nQwen3-8B     & 15.37 & 0.93 & 9.90 & 8.36 \\\\\nLlama-3.1-8B & 13.34 & 0.08 & 6.56 & 2.54 \\\\\nQwen3-70B    & 6.50  & 0.00 & 3.66 & 11.24 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DocRED cross-scale comparison (zero-shot). CF does not decrease with scale (70B CF=7.01\\% vs.\\ Qwen-8B CF=2.57\\%), suggesting CF is an inherent property of per-relation enforcement, not a model artifact.}\n\\label{tab:scale_docred}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{DR-unc\\%} & \\textbf{DR-con\\%} & \\textbf{CF-con\\%} & \\textbf{R-F1 $\\Delta$} \\\\\n\\midrule\nQwen3-8B     & 18.46 & 10.21 & 2.57  & +0.50 \\\\\nLlama-3.1-8B & 26.07 & 2.55  & 12.02 & +0.29 \\\\\nQwen3-70B    & 15.00 & 0.00  & 7.01  & +0.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Finding 6: Larger models are more constraint-compliant but not violation-free.}\nQwen3-70B shows DR=6.50\\% on SciERC (vs.\\ 15.37\\% for Qwen3-8B) and DR=15.0\\% on DocRED (vs.\\ 18.46\\%).\nUnder constrained decoding, 70B achieves DR=0\\% on both datasets.\nHowever, this represents diminishing marginal returns---the baseline violation rate is already substantially lower.\n\n\\textbf{Finding 7: Cross-field violations do not scale away.}\nCF under constrained decoding shows no clear scaling trend: 70B CF=3.66\\% on SciERC (vs.\\ 9.90\\% for 8B) but CF=7.01\\% on DocRED (vs.\\ 2.57\\% for Qwen-8B, 12.02\\% for Llama-8B).\nThis supports the hypothesis that CF is a structural property of per-relation independent enforcement, not merely a model capability limitation.\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Fine-Tuned Regime: Composability with LoRA}\n\\label{sec:ft}\n\n\\paragraph{Event extraction composability.}\nTable~\\ref{tab:ee_ft} evaluates \\sys{} composability with LoRA-fine-tuned models on WikiEvents EE.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{EE fine-tuned composability (WikiEvents). Constrained decoding eliminates RoV but reduces Trigger-F1 by 5.4pp on Qwen. Arg-F1 changes are within noise.}\n\\label{tab:ee_ft}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Config} & \\textbf{Trig-F1} & \\textbf{Arg-F1} & \\textbf{RoV\\%} & \\textbf{AC\\%} \\\\\n\\midrule\nQwen  & unconstrained & 32.08 & 7.85 & 38.3 & 2.7 \\\\\nQwen  & constrained   & 26.72 & 8.18 & 0    & 0   \\\\\nLlama & unconstrained & 27.52 & 9.98 & 8.8  & 3.5 \\\\\nLlama & constrained   & 26.91 & 8.91 & 0    & 0.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConstrained decoding eliminates RoV entirely in the fine-tuned regime.\nHowever, Qwen Trigger-F1 drops from 32.08\\% to 26.72\\% ($-$5.36pp), indicating that the semantic mask interferes with trigger word generation.\nArg-F1 changes are small and inconsistent in direction (Qwen $+$0.33pp, Llama $-$1.07pp).\n\n\\paragraph{LoRA scale experiment: 70B on RE.}\nTables~\\ref{tab:lora_scierc} and~\\ref{tab:lora_docred} evaluate Qwen3-70B LoRA on SciERC and DocRED.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LoRA SciERC: 8B vs.\\ 70B constrained impact. The 70B quantized model shows 0\\% DR reduction (constrained DR equals unconstrained DR) and 5\\% parse failures.}\n\\label{tab:lora_scierc}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{unc DR\\%} & \\textbf{con DR\\%} & \\textbf{DR red.\\%} & \\textbf{R-F1 $\\Delta$} & \\textbf{PF\\%} \\\\\n\\midrule\nQwen-8B LoRA          & 1.95 & 0    & 100 & $-$0.09 & 0   \\\\\nLlama-8B LoRA         & 1.11 & 0.09 & 92  & $+$0.02 & 0   \\\\\nQwen-70B LoRA (pred.) & 1.50 & 1.50 & 0   & $-$1.53 & 5.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LoRA DocRED: 8B vs.\\ 70B constrained. The 70B quantized model shows DR=2.80\\%, R-F1 drop of 2.5pp, and 11\\% parse failures---worse than 8B full-precision models on all metrics.}\n\\label{tab:lora_docred}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{DR-con\\%} & \\textbf{CF\\%} & \\textbf{R-F1} & \\textbf{R-F1 $\\Delta$} & \\textbf{PF\\%} \\\\\n\\midrule\nQwen-8B LoRA          & 0.01 & 0.41 & 40.56 & $-$0.30 & 8.5  \\\\\nLlama-8B LoRA         & 0.21 & 0.21 & 43.78 & $+$0.06 & 2.5  \\\\\nQwen-70B LoRA (pred.) & 2.80 & 1.80 & 43.70 & $-$2.50 & 11.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Finding 8: Constrained decoding does not generalize reliably to quantized large models.}\nOn SciERC, the 70B AWQ-INT4 model achieves 0\\% DR reduction---constrained DR equals unconstrained DR---while R-F1 drops 1.53pp.\nOn DocRED, constrained DR remains at 2.80\\% (vs.\\ 0.01--0.21\\% for 8B models), R-F1 drops 2.5pp, and 11\\% of documents fail to parse.\nThe mechanism is that INT4 quantization shifts the logit distribution, causing more frequent fallback from semantic to grammar-only constraints.\nThis result challenges the assumption that constrained decoding is deployment-ready for quantized large models.\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Statistical Significance of EE Improvements}\n\\label{sec:bootstrap}\n\nTable~\\ref{tab:bootstrap_ee} reports bootstrap confidence intervals for the EE constrained vs.\\ unconstrained comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{EE bootstrap significance (10,000 iterations). Entity-F1 improvements are significant but reflect format compliance recovery (0\\%$\\to$11--17\\%), not semantic extraction gains. Trigger-F1 and Arg-F1 changes are not significant.}\n\\label{tab:bootstrap_ee}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Metric} & \\textbf{$\\Delta$pp} & \\textbf{$p$-value} & \\textbf{Sig.} \\\\\n\\midrule\nQwen    & Trigger-F1 & $+$1.55 & 0.18    & No \\\\\nQwen    & Entity-F1  & $+$14.09 & $<$0.001 & Yes\\rmark{$\\dagger$} \\\\\nQwen    & Arg-F1     & $+$1.59 & 0.42    & No \\\\\n\\midrule\nLlama   & Trigger-F1 & $+$1.76 & 0.22    & No \\\\\nLlama   & Entity-F1  & $+$17.63 & $<$0.001 & Yes\\rmark{$\\dagger$} \\\\\nLlama   & Arg-F1     & $+$1.18 & 0.38    & No \\\\\n\\midrule\nMistral & Trigger-F1 & $+$1.46 & 0.31    & No \\\\\nMistral & Entity-F1  & $+$11.71 & $<$0.001 & Yes\\rmark{$\\dagger$} \\\\\nMistral & Arg-F1     & $+$0.31 & 0.61    & No \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize\\rmark{$\\dagger$} Significant but attributable to format compliance recovery.}\n\\end{tabular}\n\\end{table}\n\nEntity-F1 improves significantly across all three models ($p < 0.001$), but this improvement is entirely attributable to format compliance: grammar constraints produce schema-valid JSON that parsers can recognize, recovering entity mentions from 0\\% to 11.7--17.6\\%.\nThis is not a semantic extraction improvement.\nTrigger-F1 and Arg-F1 changes are small and not statistically significant in any model.\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Latency Overhead}\n\\label{sec:latency}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Latency overhead of constrained decoding. Overhead ranges from 10--16.5\\%, modest in absolute terms.}\n\\label{tab:latency}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Setting} & \\textbf{Overhead\\%} & \\textbf{unc (s/doc)} & \\textbf{con (s/doc)} \\\\\n\\midrule\nZS SciERC   & 13.1 & 4.16 & 4.71 \\\\\nFT SciERC   & 10.0 & 2.61 & 2.87 \\\\\nFT Beam-4   & 16.5 & 3.45 & 4.01 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConstrained decoding adds 10--16.5\\% wall-clock overhead across settings (Table~\\ref{tab:latency}).\nThe overhead is dominated by grammar mask computation; the semantic layer adds negligible cost.\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Error Analysis}\n\\label{sec:error_analysis}\n\nWe conduct a qualitative analysis of 15 residual AC and CF cases to understand the root causes of violations that \\sys{} cannot eliminate.\n\n\\paragraph{CF root causes.}\nApproximately 45\\% of CF violations stem from ontology type-system ambiguity: entity types with overlapping semantic scope (e.g., \\texttt{Generic} vs.\\ \\texttt{OtherScientificTerm} in SciERC) that could reasonably be assigned to the same entity in different relation contexts.\nAnother 40\\% arise from model confusion: the same entity receives inconsistent type assignments across relations due to context-dependent LLM behavior.\nThe remaining 15\\% reflect genuine ontology design gaps where the type system lacks sufficient granularity.\n\n\\paragraph{Implications.}\nCF violations are not addressable by constrained decoding alone: they require either (a) a global entity-type consensus mechanism applied before per-relation generation, or (b) ontology revision to reduce type-boundary ambiguity.\nThe error analysis suggests that the method's limitations are, in part, a diagnostic tool for ontology quality.\n\n\n% ===========================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{The violation landscape as a research contribution.}\nOur study reveals systematic patterns in how LLMs violate ontology constraints:\nviolation rates are driven by constraint tightness (not ontology size),\ndifferent model architectures produce qualitatively different violation profiles,\nand prompt-based mitigation is fundamentally unreliable at the per-relation level.\nThese findings inform the design of future constraint enforcement methods.\n\n\\paragraph{The limits of per-relation enforcement.}\n\\sys{} achieves strong violation reduction on vocabulary and domain/range constraints but introduces cross-field inconsistencies as a structural trade-off.\nCF rates of 3.7--21.1\\% across configurations are non-negligible.\nOur analysis shows this is inherent to any method that enforces constraints independently per relation/event---a global consistency mechanism is needed.\n\n\\paragraph{When is constrained decoding the right tool?}\nOur results suggest constrained decoding is most valuable when: (a) post-hoc filtering would destroy too much information (EE: 99.6--100\\% discard), (b) per-instance compliance guarantees are required (safety-critical domains), or (c) the model is fine-tuned (eliminating the post-hoc F1 advantage seen in zero-shot).\nIn zero-shot RE with low absolute F1, simpler post-hoc filtering is a competitive alternative.\n\n\\paragraph{Quantization and scale.}\nThe failure of constrained decoding on AWQ-INT4 quantized 70B models (0\\% DR reduction on SciERC, degraded R-F1 on DocRED) exposes an underexplored interaction between quantization and logit-level constraint enforcement.\nFuture work should investigate quantization-aware mask calibration.\n\n% ===========================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe present the first systematic study of ontology constraint violations in LLM-based information extraction, spanning three datasets, five models, and two IE tasks.\nOur violation taxonomy and landscape analysis reveal that violations are driven by constraint tightness, are qualitatively model-dependent, and resist prompt-based mitigation.\nWe develop \\sys{} as a practical mitigation tool that eliminates vocabulary and structural violations while exposing the fundamental tension between per-relation constraint enforcement and cross-field consistency.\nOur findings and tools establish a foundation for future research on ontology-aware structured generation.\n\n% ===========================================================================\n\\section*{Limitations}\n\\label{sec:limitations}\n\nOur study has three main limitations.\nFirst, cross-field (CF) violations introduced by constrained decoding (3.7--21.1\\% across configurations) represent a fundamental trade-off that our method does not address---resolving this requires a global entity-type consensus mechanism beyond per-relation enforcement.\nSecond, the zero-shot evaluation setting produces low absolute F1 scores (2--13\\% on RE, 0--12\\% on EE), which limits the practical interpretability of F1 improvements; while this is expected in zero-shot IE and our contribution is the constraint enforcement method rather than extraction quality, it constrains the scope of our conclusions.\nThird, our scale experiments reveal that constrained decoding does not generalize reliably to quantized large models (AWQ-INT4), where logit distribution shifts degrade mask effectiveness---deployment in production settings requires further investigation.\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Gao et~al.(2023)]{gao2023exploring}\nJ.~Gao, H.~Zhao, C.~Yu, and R.~Xu.\n\\newblock Exploring the feasibility of ChatGPT for event extraction.\n\\newblock \\emph{arXiv preprint arXiv:2303.03836}, 2023.\n\n\\bibitem[Li et~al.(2021)]{li2021document}\nS.~Li, H.~Ji, and J.~Han.\n\\newblock Document-level event argument extraction by conditional generation.\n\\newblock In \\emph{Proceedings of NAACL}, 2021.\n\n\\bibitem[Li et~al.(2023)]{li2023evaluating}\nB.~Li, G.~Fang, Y.~Yang, Q.~Wang, W.~Ye, S.~Zhao, and G.~Zhang.\n\\newblock Evaluating ChatGPT's information extraction capabilities.\n\\newblock \\emph{arXiv preprint arXiv:2304.11633}, 2023.\n\n\\bibitem[Lin et~al.(2020)]{lin2020joint}\nY.~Lin, H.~Ji, F.~Huang, and L.~Wu.\n\\newblock A joint neural model for information extraction with global features.\n\\newblock In \\emph{Proceedings of ACL}, 2020.\n\n\\bibitem[Luan et~al.(2018)]{luan2018multi}\nY.~Luan, L.~He, M.~Ostendorf, and H.~Hajishirzi.\n\\newblock Multi-task identification of entities, relations, and coreference for scientific knowledge graph construction.\n\\newblock In \\emph{Proceedings of EMNLP}, 2018.\n\n\\bibitem[Ugare et~al.(2024)]{ugare2024pldi}\nS.~Ugare, T.~Suresh, H.~Kang, S.~Misailovic, and G.~Singh.\n\\newblock Syncode: LLM generation with grammar augmentation.\n\\newblock In \\emph{Proceedings of PLDI}, 2024.\n\n\\bibitem[Wadhwa et~al.(2023)]{wadhwa2023revisiting}\nS.~Wadhwa, S.~Amir, and B.~Wallace.\n\\newblock Revisiting relation extraction in the era of large language models.\n\\newblock In \\emph{Proceedings of ACL}, 2023.\n\n\\bibitem[Wan et~al.(2023)]{wan2023gpt}\nZ.~Wan, F.~Cheng, Z.~Mao, Q.~Liu, H.~Song, J.~Li, and S.~Kurohashi.\n\\newblock GPT-RE: In-context learning for relation extraction using large language models.\n\\newblock In \\emph{Proceedings of EMNLP}, 2023.\n\n\\bibitem[Wei et~al.(2023)]{wei2023zero}\nX.~Wei, J.~Cui, N.~Bell, and S.~Sun.\n\\newblock Zero-shot information extraction via chatting with ChatGPT.\n\\newblock \\emph{arXiv preprint arXiv:2302.10205}, 2023.\n\n\\bibitem[Willard and Louf(2023)]{willard2023efficient}\nB.~T. Willard and R.~Louf.\n\\newblock Efficient guided generation for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2307.09702}, 2023.\n\n\\bibitem[Xu et~al.(2023)]{xu2023unleash}\nD.~Xu, W.~Chen, W.~Peng, C.~Zhang, T.~Xu, X.~Zhao, X.~Wu, Y.~Zheng, and G.~Chen.\n\\newblock Large language models for generative information extraction: A survey.\n\\newblock \\emph{arXiv preprint arXiv:2312.17617}, 2023.\n\n\\bibitem[Yao et~al.(2019)]{yao2019docred}\nY.~Yao, D.~Ye, P.~Li, X.~Han, Y.~Lin, Z.~Liu, Z.~Liu, L.~Huang, J.~Zhou, and M.~Sun.\n\\newblock DocRED: A large-scale document-level relation extraction dataset.\n\\newblock In \\emph{Proceedings of ACL}, 2019.\n\n\\bibitem[Zheng et~al.(2024)]{zheng2024xgrammar}\nL.~Zheng, et~al.\n\\newblock XGrammar: Flexible and efficient structured generation engine for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2411.15100}, 2024.\n\n\\bibitem[Zhong and Chen(2021)]{zhong2021frustratingly}\nZ.~Zhong and D.~Chen.\n\\newblock A frustratingly easy approach for entity and relation extraction.\n\\newblock In \\emph{Proceedings of NAACL}, 2021.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "012aaf58-a387-47b8-a60a-39be6eebccf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T052642 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_c…",
  "leafUuid": "3ca3a2d0-a2fc-4f6b-83d0-6937e4e5571f",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier mock research paper",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a"
}
```

---

### Tool call

_source line 28 · 2026-05-22T06:23:37.659Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TTyhqaaTjYysbSrq39Z7vJ`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ca3a2d0-a2fc-4f6b-83d0-6937e4e5571f",
  "isSidechain": false,
  "requestId": "req_011CbH8MikQJEWikCXMu42gH",
  "type": "assistant",
  "uuid": "19adae52-bb9a-406f-99cd-4dc264735073",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EParsMsWRb2U2qT1jyd1Jx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11702,
      "cache_read_input_tokens": 50229,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 50229,
          "cache_creation_input_tokens": 11702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11702
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

_source line 29 · 2026-05-22T06:23:38.738Z_

<details><summary>↩ Tool result · `toolu_01TTyhqaaTjYysbSrq39Z7vJ`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
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

Package natbib Warning: Citation `wadhwa2023revisiting' on page 1 undefined on 
input line 42.


Package natbib Warning: Citation `wan2023gpt' on page 1 undefined on input line
 42.


Package natbib Warning: Citation `gao2023exploring' on page 1 undefined on inpu
t line 42.


Package natbib Warning: Citation `li2023evaluating' on page 1 undefined on inpu
t line 42.


Package natbib Warning: Citation `willard2023efficient' on page 1 undefined on 
input line 47.


Package natbib Warning: Citation `zheng2024xgrammar' on page 1 undefined on inp
ut line 47.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `wadhwa2023revisiting' on page 2 undefined on 
input line 67.


Package natbib Warning: Citation `wei2023zero' on page 2 undefined on input lin
e 67.


Package natbib Warning: Citation `wan2023gpt' on page 2 undefined on input line
 67.


Package natbib Warning: Citation `xu2023unleash' on page 2 undefined on input l
ine 67.


Package natbib Warning: Citation `willard2023efficient' on page 2 undefined on 
input line 72.


Package natbib Warning: Citation `zheng2024xgrammar' on page 2 undefined on inp
ut line 72.


Package natbib Warning: Citation `ugare2024pldi' on page 2 undefined on input l
ine 73.


Overfull \hbox (7.84602pt too wide) in paragraph at lines 72--75
 []\T1/ptm/b/n/10.95 Constrained De-cod-ing for Struc-tured Gen-er-a-tion.[] \T
1/ptm/m/n/10.95 Grammar-constrained de-cod-ing (\T1/ptm/b/n/10.95 ??\T1/ptm/m/n
/10.95 ) en-forces context-

Package natbib Warning: Citation `lin2020joint' on page 2 undefined on input li
ne 77.


Package natbib Warning: Citation `zhong2021frustratingly' on page 2 undefined o
n input line 77.

[2]

Package natbib Warning: Citation `zheng2024xgrammar' on page 3 undefined on inp
ut line 107.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd)

Package natbib Warning: Citation `luan2018multi' on page 3 undefined on input l
ine 126.


Package natbib Warning: Citation `yao2019docred' on page 3 undefined on input l
ine 126.


Package natbib Warning: Citation `li2021document' on page 3 undefined on input 
line 126.


Overfull \hbox (1.10126pt too wide) in paragraph at lines 129--131
 []\T1/ptm/b/n/10.95 Models.[] \T1/ptm/m/n/10.95 We use Qwen3-8B, Llama-3.1-8B-
Instruct, Mistral-7B-v0.3, and Qwen3-70B (AWQ-INT4), cov-

LaTeX Warning: Reference `tab:ee_unconstrained' on page 3 undefined on input li
ne 141.

[3]

LaTeX Warning: Reference `tab:posthoc' on page 4 undefined on input line 177.


LaTeX Warning: Reference `tab:posthoc_vs_constrained' on page 4 undefined on in
put line 203.


LaTeX Warning: Reference `tab:grammar_only_ee' on page 4 undefined on input lin
e 234.

[4]

LaTeX Warning: Reference `tab:grammar_mistral_ee' on page 5 undefined on input 
line 261.


LaTeX Warning: Reference `tab:ee_ft' on page 5 undefined on input line 333.

[5]

LaTeX Warning: Reference `tab:lora_scierc' on page 6 undefined on input line 35
7.


LaTeX Warning: Reference `tab:lora_docred' on page 6 undefined on input line 35
7.


LaTeX Warning: Reference `tab:bootstrap_ee' on page 6 undefined on input line 4
02.


LaTeX Warning: Reference `tab:latency' on page 6 undefined on input line 454.

[6] [7] [8] [9]

Package natbib Warning: There were undefined citations.

[10] (./paper.aux

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
nts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8
a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 132719 bytes).
Transcript written on paper.log.
Overfull \hbox (20.31824pt too wide) in paragraph at lines 126--127
\T1/ptm/m/n/10.95 551 ab-stracts), \T1/ptm/b/n/10.95 Do-cRED \T1/ptm/m/n/10.95 
[[]Yao et al.[], []2019[]] (96 re-la-tion types, 7 en-tity types, 998 doc-u-men
ts), and \T1/ptm/b/n/10.95 WikiEvents \T1/ptm/m/n/10.95 [[]Li

Overfull \hbox (1.10126pt too wide) in paragraph at lines 129--131
 []\T1/ptm/b/n/10.95 Models.[] \T1/ptm/m/n/10.95 We use Qwen3-8B, Llama-3.1-8B-
Instruct, Mistral-7B-v0.3, and Qwen3-70B (AWQ-INT4), cov-
[3] [4] [5] [6] [7] [8] [9] [10] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8
a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 136454 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19adae52-bb9a-406f-99cd-4dc264735073",
  "isSidechain": false,
  "promptId": "24b84624-7cc9-4802-b961-7b1d19e328f3",
  "type": "user",
  "uuid": "4aef8775-8b92-42b4-aaba-81c9da6fc7b3",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `wadhwa2023revisiting' on page 1 undefined on \ninput line 42.\n\n\nPackage natbib Warning: Citation `wan2023gpt' on page 1 undefined on input line\n 42.\n\n\nPackage natbib Warning: Citation `gao2023exploring' on page 1 undefined on inpu\nt line 42.\n\n\nPackage natbib Warning: Citation `li2023evaluating' on page 1 undefined on inpu\nt line 42.\n\n\nPackage natbib Warning: Citation `willard2023efficient' on page 1 undefined on \ninput line 47.\n\n\nPackage natbib Warning: Citation `zheng2024xgrammar' on page 1 undefined on inp\nut line 47.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `wadhwa2023revisiting' on page 2 undefined on \ninput line 67.\n\n\nPackage natbib Warning: Citation `wei2023zero' on page 2 undefined on input lin\ne 67.\n\n\nPackage natbib Warning: Citation `wan2023gpt' on page 2 undefined on input line\n 67.\n\n\nPackage natbib Warning: Citation `xu2023unleash' on page 2 undefined on input l\nine 67.\n\n\nPackage natbib Warning: Citation `willard2023efficient' on page 2 undefined on \ninput line 72.\n\n\nPackage natbib Warning: Citation `zheng2024xgrammar' on page 2 undefined on inp\nut line 72.\n\n\nPackage natbib Warning: Citation `ugare2024pldi' on page 2 undefined on input l\nine 73.\n\n\nOverfull \\hbox (7.84602pt too wide) in paragraph at lines 72--75\n []\\T1/ptm/b/n/10.95 Constrained De-cod-ing for Struc-tured Gen-er-a-tion.[] \\T\n1/ptm/m/n/10.95 Grammar-constrained de-cod-ing (\\T1/ptm/b/n/10.95 ??\\T1/ptm/m/n\n/10.95 ) en-forces context-\n\nPackage natbib Warning: Citation `lin2020joint' on page 2 undefined on input li\nne 77.\n\n\nPackage natbib Warning: Citation `zhong2021frustratingly' on page 2 undefined o\nn input line 77.\n\n[2]\n\nPackage natbib Warning: Citation `zheng2024xgrammar' on page 3 undefined on inp\nut line 107.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd)\n\nPackage natbib Warning: Citation `luan2018multi' on page 3 undefined on input l\nine 126.\n\n\nPackage natbib Warning: Citation `yao2019docred' on page 3 undefined on input l\nine 126.\n\n\nPackage natbib Warning: Citation `li2021document' on page 3 undefined on input \nline 126.\n\n\nOverfull \\hbox (1.10126pt too wide) in paragraph at lines 129--131\n []\\T1/ptm/b/n/10.95 Models.[] \\T1/ptm/m/n/10.95 We use Qwen3-8B, Llama-3.1-8B-\nInstruct, Mistral-7B-v0.3, and Qwen3-70B (AWQ-INT4), cov-\n\nLaTeX Warning: Reference `tab:ee_unconstrained' on page 3 undefined on input li\nne 141.\n\n[3]\n\nLaTeX Warning: Reference `tab:posthoc' on page 4 undefined on input line 177.\n\n\nLaTeX Warning: Reference `tab:posthoc_vs_constrained' on page 4 undefined on in\nput line 203.\n\n\nLaTeX Warning: Reference `tab:grammar_only_ee' on page 4 undefined on input lin\ne 234.\n\n[4]\n\nLaTeX Warning: Reference `tab:grammar_mistral_ee' on page 5 undefined on input \nline 261.\n\n\nLaTeX Warning: Reference `tab:ee_ft' on page 5 undefined on input line 333.\n\n[5]\n\nLaTeX Warning: Reference `tab:lora_scierc' on page 6 undefined on input line 35\n7.\n\n\nLaTeX Warning: Reference `tab:lora_docred' on page 6 undefined on input line 35\n7.\n\n\nLaTeX Warning: Reference `tab:bootstrap_ee' on page 6 undefined on input line 4\n02.\n\n\nLaTeX Warning: Reference `tab:latency' on page 6 undefined on input line 454.\n\n[6] [7] [8] [9]\n\nPackage natbib Warning: There were undefined citations.\n\n[10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8\na.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 132719 bytes).\nTranscript written on paper.log.\nOverfull \\hbox (20.31824pt too wide) in paragraph at lines 126--127\n\\T1/ptm/m/n/10.95 551 ab-stracts), \\T1/ptm/b/n/10.95 Do-cRED \\T1/ptm/m/n/10.95 \n[[]Yao et al.[], []2019[]] (96 re-la-tion types, 7 en-tity types, 998 doc-u-men\nts), and \\T1/ptm/b/n/10.95 WikiEvents \\T1/ptm/m/n/10.95 [[]Li\n\nOverfull \\hbox (1.10126pt too wide) in paragraph at lines 129--131\n []\\T1/ptm/b/n/10.95 Models.[] \\T1/ptm/m/n/10.95 We use Qwen3-8B, Llama-3.1-8B-\nInstruct, Mistral-7B-v0.3, and Qwen3-70B (AWQ-INT4), cov-\n[3] [4] [5] [6] [7] [8] [9] [10] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8\na.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 136454 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "19adae52-bb9a-406f-99cd-4dc264735073",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-22T06:23:46.774Z_

编译成功，生成 10 页 PDF，无错误（仅有少量 overfull hbox 警告和预期的 citation 格式警告）。

论文已写入 `worst/paper.tex` 并编译为 `worst/paper.pdf`（10 页，136KB）。覆盖了全部 15 个实验数据条目，对应 10 个表格和 8 个核心 finding。按 worst-tier 叙事重构为 empirical study：violation landscape 为主贡献，OntoCoDec 降级为 mitigation tool，透明暴露 post-hoc 在 ZS RE 上 5/6 胜出、70B 量化模型 constrained decoding 失效、CF trade-off 等负面结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4aef8775-8b92-42b4-aaba-81c9da6fc7b3",
  "isSidechain": false,
  "requestId": "req_011CbH8N5JfG5cJaTN9NgfB8",
  "type": "assistant",
  "uuid": "01c1d16a-b36a-4d72-8c81-8f7ab854a5bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/worst",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDDoaEmsFvDMrstncG3DeC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4506,
      "cache_read_input_tokens": 61931,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4506,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 61931,
          "cache_creation_input_tokens": 4506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4506
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T052642 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_c…",
  "leafUuid": "01c1d16a-b36a-4d72-8c81-8f7ab854a5bc",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier mock research paper",
  "sessionId": "419eb035-6fa3-4657-a096-4c92223d8c5a"
}
```

---
