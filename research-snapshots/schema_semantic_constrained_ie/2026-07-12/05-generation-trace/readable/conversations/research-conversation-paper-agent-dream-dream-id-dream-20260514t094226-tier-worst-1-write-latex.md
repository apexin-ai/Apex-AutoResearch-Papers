# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T094226 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/2ebf8474-508b-47ef-8b53-5e664546d2e0.jsonl`
- **Structured JSON:** [`5596e9915af6f59a9ae3.json`](../../sessions/55/5596e9915af6f59a9ae3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T10:37:14.986Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T10:37:14.986Z",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T094226 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：放弃 \"composable dual-layer near-complete\" 叙事。论文 pivot 为三个独立贡献： (1) Violation Landscape Study（首次系统测量跨 ontology 复杂度的 violation 分布，占 40% 篇幅）， (2) Grammar-constrained decoding 作为 universal zero-cost structural validity layer（ET→0%、RV→0% 完美跨数据集泛化）， (3) Semantic layer 作为 tight ontology proof-of-concept（显式标记 'scaling to complex ontologies remains open'）。 Title 改为 'How LLMs Violate Ontology Constraints: A Landscape Study and Grammar-Based Mitigation'。 DocRED 10.19% 残留 DR 直接标注 open problem。Tightness-DR null result 作为 empirical finding 报告。 S1/S2 比较降为 appendix。核心 selling point 从 method paper 转向 empirical study + targeted solution。 EMNLP 2026 empirical analysis track 是合理 venue。风险：novelty 感知下降， 但 violation landscape 数据的 reusability 和 grammar 层 clean result 仍可撑 acceptance。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T10:37:14.990Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T10:37:14.990Z",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-14T10:37:15.014Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T094226 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：放弃 "composable dual-layer near-complete" 叙事。论文 pivot 为三个独立贡献： (1) Violation Landscape Study（首次系统测量跨 ontology 复杂度的 violation 分布，占 40% 篇幅）， (2) Grammar-constrained decoding 作为 universal zero-cost structural validity layer（ET→0%、RV→0% 完美跨数据集泛化）， (3) Semantic layer 作为 tight ontology proof-of-concept（显式标记 'scaling to complex ontologies remains open'）。 Title 改为 'How LLMs Violate Ontology Constraints: A Landscape Study and Grammar-Based Mitigation'。 DocRED 10.19% 残留 DR 直接标注 open problem。Tightness-DR null result 作为 empirical finding 报告。 S1/S2 比较降为 appendix。核心 selling point 从 method paper 转向 empirical study + targeted solution。 EMNLP 2026 empirical analysis track 是合理 venue。风险：novelty 感知下降， 但 violation landscape 数据的 reusability 和 grammar 层 clean result 仍可撑 acceptance。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "bf085e6b-de2b-42eb-9731-c83a8642823c",
  "type": "user",
  "uuid": "ae1d475b-b17a-4cab-ab67-e1c68225e6a7",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T10:37:15.013Z_

```json
{
  "parentUuid": "ae1d475b-b17a-4cab-ab67-e1c68225e6a7",
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
  "uuid": "7bb6efc0-9bad-4bcf-b11c-d049a7787f6a",
  "timestamp": "2026-05-14T10:37:15.013Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T10:37:15.013Z_

```json
{
  "parentUuid": "7bb6efc0-9bad-4bcf-b11c-d049a7787f6a",
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
  "uuid": "07741276-6c16-4982-a41f-b7bcdb012f8e",
  "timestamp": "2026-05-14T10:37:15.013Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T10:37:15.013Z_

```json
{
  "parentUuid": "07741276-6c16-4982-a41f-b7bcdb012f8e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "47e1a005-93d7-407a-862b-526df9ea5bf8",
  "timestamp": "2026-05-14T10:37:15.013Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
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
  "aiTitle": "Generate simulation paper for dream research",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0"
}
```

---

### Assistant

_source line 8 · 2026-05-14T10:37:20.374Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47e1a005-93d7-407a-862b-526df9ea5bf8",
  "isSidechain": false,
  "requestId": "req_011Cb2KEQgjaGLmQqhUXKeRD",
  "type": "assistant",
  "uuid": "de30fe4e-a060-45b3-b244-5e2432505e9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fo3YBxNBGytE3LmwWZTnwJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11802,
      "cache_read_input_tokens": 11447,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11802
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

_source line 9 · 2026-05-14T10:37:21.339Z_

<details open><summary>🔧 Tool call — Read · `toolu_016hwYqoH9auqpSDvCX7NZpf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de30fe4e-a060-45b3-b244-5e2432505e9f",
  "isSidechain": false,
  "requestId": "req_011Cb2KEQgjaGLmQqhUXKeRD",
  "type": "assistant",
  "uuid": "067f7849-7b9e-490c-854b-28c19d9b699c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fo3YBxNBGytE3LmwWZTnwJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11802,
      "cache_read_input_tokens": 11447,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11802
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

_source line 10 · 2026-05-14T10:37:21.618Z_

<details><summary>↩ Tool result · `toolu_016hwYqoH9auqpSDvCX7NZpf`</summary>

```text
1	[
2	  {
3	    "name": "DocRED Phase 2 unconstrained baseline",
4	    "description": "使用 Phase 2 pipeline 重跑 DocRED unconstrained，与 constrained 实验共用相同 prompt/generation config/post-processing，确保消融表 F1/violation 对比公平。",
5	    "results": {
6	      "documents_checked": 975,
7	      "parse_failures": 23,
8	      "total_entities": 19800,
9	      "total_triples": 16200,
10	      "entity_type_violation_rate": 0.068,
11	      "relation_vocabulary_violation_rate": 0.265,
12	      "domain_range_violation_rate": 0.158,
13	      "cross_field_consistency_violation_rate": 0.001,
14	      "relation_f1": 0.0808,
15	      "entity_f1": 0.585,
16	      "json_parse_rate": 0.977,
17	      "dr_reduction_vs_full_s1_pct": 35.5
18	    },
19	    "tables": [
20	      {
21	        "name": "DocRED Phase 2 Full Ablation Table",
22	        "columns": [
23	          "Mode",
24	          "DR(%)",
25	          "RV(%)",
26	          "ET(%)",
27	          "CF(%)",
28	          "R-F1",
29	          "Triples"
30	        ],
31	        "rows": [
32	          [
33	            "Unconstrained",
34	            15.8,
35	            26.5,
36	            6.8,
37	            0.1,
38	            8.08,
39	            16200
40	          ],
41	          [
42	            "Grammar-only",
43	            26.17,
44	            0.03,
45	            0.0,
46	            0.08,
47	            8.24,
48	            17341
49	          ],
50	          [
51	            "Semantic-only",
52	            11.2,
53	            24.8,
54	            5.9,
55	            3.8,
56	            7.95,
57	            16050
58	          ],
59	          [
60	            "Full S1",
61	            10.19,
62	            0.03,
63	            0.0,
64	            2.99,
65	            8.17,
66	            17372
67	          ]
68	        ]
69	      }
70	    ],
71	    "figures": [],
72	    "analysis": "DR reduction 35.5% 远低于 SciERC 94%，直接挑战 cross-dataset generalization claim。 Grammar-only DR=26.17% > unconstrained DR=15.8% 的现象需要 §5.4 专门解释： grammar 消除 ~27% 的 RV violations 后，原先有 invalid relation name 的 triples 现在有了 valid relation name，可以被 DR checker 评估，暴露大量新 DR violations。 这不是 grammar 变差了，而是 Phase 0 的 DR=18.7% 本身就低估了（被 RV 掩盖了真实 DR）。 如果用 grammar-only 26.17% 作为 \"真实 baseline\"， full_s1 的 DR reduction = (26.17-10.19)/26.17 = 61.1%——但这个 framing 有 cherry-picking 嫌疑。 论文需要同时报告两个 baseline 的 reduction%，让 reader 自行判断。\n\n\nPhase 2 code path 使用统一 prompt template（含 JSON schema instruction）和 generation config （temperature=0.6, top_p=0.95, thinking mode /no_think），与 Phase 0 minimal prompt 存在细微差异。 预期 DR 从 Phase 0 的 18.7% 降至 ~15.8%，原因三重： (a) Phase 2 统一 JSON instruction 隐式提供了更清晰的 type 格式指导，\n    模型对 domain/range 的 implicit adherence 轻微提升；\n(b) Phase 0 使用 raw minimal prompt，Phase 2 code path 的 prompt wrapper 结构更整洁，\n    部分 Phase 0 边界 case 在 Phase 2 中被分类为 parse failure（23 failures vs Phase 0 的 36 failures），\n    denominator 缩小使 DR 的百分比下降；\n(c) generation config 的差异（max_new_tokens=4096 统一设定 vs Phase 0 可能不同）\n    影响长文档的 truncation behavior，改变 tail triples 的 violation 分布。\nDR=15.8% 使 full_s1 的 DR reduction 仅为 (15.8-10.19)/15.8 = 35.5%， 远低于 SciERC 的 94%（0.93/15.37）和 Phase 0 基线计算的 45.5%（10.19/18.7）。 这是 worst tier 的核心数字痛点：fair-comparison baseline 偏低导致 improvement narrative 被压缩。 RV/ET 保持 Phase 0 水平（~27%/~7%），因为无 grammar 约束。\n"
73	  },
74	  {
75	    "name": "DocRED Phase 2 semantic-only constrained decoding",
76	    "description": "仅启用 semantic layer（TypeConstraintProcessor），不启用 grammar layer（XGrammar），验证 grammar enabling dependency 是否在复杂 ontology 上复现。",
77	    "results": {
78	      "documents_checked": 970,
79	      "total_triples": 16050,
80	      "total_entities": 19600,
81	      "entity_type_violation_rate": 0.059,
82	      "relation_vocabulary_violation_rate": 0.248,
83	      "domain_range_violation_rate": 0.112,
84	      "cross_field_consistency_violation_rate": 0.038,
85	      "relation_f1": 0.0795,
86	      "entity_f1": 0.58,
87	      "semantic_enabling_ratio": 1.1,
88	      "semantic_dr_reduction_vs_unconstrained_pct": 29.1
89	    },
90	    "tables": [
91	      {
92	        "name": "Enabling Dependency Cross-Dataset Comparison",
93	        "columns": [
94	          "Dataset",
95	          "Ontology_Size",
96	          "semantic_only_DR(%)",
97	          "full_s1_DR(%)",
98	          "Enabling_Ratio",
99	          "Interpretation"
100	        ],
101	        "rows": [
102	          [
103	            "SciERC",
104	            "7 rels",
105	            11.65,
106	            0.93,
107	            12.5,
108	            "Strong enabling: grammar prerequisite"
109	          ],
110	          [
111	            "DocRED",
112	            "96 rels",
113	            11.2,
114	            10.19,
115	            1.1,
116	            "No enabling: layers independent"
117	          ]
118	        ]
119	      }
120	    ],
121	    "figures": [],
122	    "analysis": "Enabling ratio=1.1 摧毁 Claim 3 的 composable with enabling dependency 叙事。 Reframe 策略：grammar 和 semantic 是两个独立 constraint layer， 各自解决不同 violation type（grammar→ET/RV 100% elimination, semantic→partial DR reduction）， 在 tight ontology 上 grammar 是 semantic 的 prerequisite（SciERC，12.5x）， 在 loose ontology 上两者 independently contribute（DocRED，1.1x）。 论文放弃 \"enabling dependency\" 作为 universal mechanism， 改为 \"enabling relationship modulated by constraint tightness and ontology vocabulary design\"。 这个 reframe 将 enabling ratio 的跨数据集差异转化为 empirical finding 而非 method failure。\n\n\nWorst tier 核心预测：semantic_only DR ≈ 11.2%，full_s1 DR = 10.19%， enabling ratio = 11.2/10.19 = 1.10。对比 SciERC enabling ratio = 11.65/0.93 = 12.5。 Grammar 对 semantic 的 enabling 在 DocRED 上几乎不存在，原因三层： (a) DocRED 使用 Wikidata property ID（P31, P17, P131 等短 ID），\n    模型生成 invalid relation name 后，这些 ID 仍有较高概率恰好是某个 valid relation\n    （96 relations 覆盖了大量常见 Pxxx pattern），\n    因此 semantic layer 在无 grammar 时仍能对多数 triples 做 constraint lookup；\n(b) SciERC 使用自然语言 relation name（\"Used-for\", \"Feature-of\"），\n    无 grammar 时 RV violation 率高（1.51%），这些 triples 的 relation 不在 ontology 中，\n    semantic layer 直接 skip，无法 enforce DR constraint——这才是 enabling 的来源；\n(c) DocRED semantic layer 的 per-relation constraints 本身宽松（avg 5.68 valid pairs，\n    但高频 relations 如 P131_located_in 允许几乎所有 type pair），\n    能 enforce 的 DR reduction 空间有限，grammar 的 enabling 效应被 constraint looseness 稀释。\nRV（~25%）和 ET（~6%）保持高位确认 semantic 无法替代 grammar 的 structural 功能—— 但这只证明 grammar 独立有用，不证明 grammar enables semantic。 Enabling dependency 退化为 \"grammar 独立有用 + semantic 独立有用\"，不再是 prerequisite 关系。\n"
123	  },
124	  {
125	    "name": "DocRED tightness-DR Spearman correlation analysis",
126	    "description": "计算 DocRED 96 relations 的 constraint tightness（valid_pairs / all_possible_entity_type_pairs）与 full_s1 residual DR 的 Spearman rank correlation，验证 SciERC 的 tightness→high DR pattern 是否跨数据集复现。",
127	    "results": {
128	      "spearman_rho": 0.14,
129	      "spearman_p_value": 0.18,
130	      "direction": "positive but not significant",
131	      "per_rel_near_zero_fraction": 0.38,
132	      "relations_with_dr_above_10pct": 28,
133	      "relations_with_dr_zero": 37,
134	      "tight_relations_with_unexpectedly_low_dr": 12,
135	      "loose_relations_with_unexpectedly_high_dr": 8,
136	      "kendall_tau": 0.1
137	    },
138	    "tables": [
139	      {
140	        "name": "DocRED Tightness-DR by Quartile",
141	        "columns": [
142	          "Tightness_Quartile",
143	          "N_rels",
144	          "Median_Triples",
145	          "Mean_DR(%)",
146	          "Near_Zero_Frac"
147	        ],
148	        "rows": [
149	          [
150	            "Q1 (tightest)",
151	            24,
152	            42,
153	            12.8,
154	            0.33
155	          ],
156	          [
157	            "Q2",
158	            24,
159	            85,
160	            9.5,
161	            0.42
162	          ],
163	          [
164	            "Q3",
165	            24,
166	            120,
167	            10.2,
168	            0.38
169	          ],
170	          [
171	            "Q4 (loosest)",
172	            24,
173	            210,
174	            8.9,
175	            0.42
176	          ]
177	        ]
178	      },
179	      {
180	        "name": "Counter-examples to Tightness-DR Hypothesis",
181	        "columns": [
182	          "Relation",
183	          "Tightness",
184	          "Valid_Pairs",
185	          "Triples",
186	          "DR(%)",
187	          "Explanation"
188	        ],
189	        "rows": [
190	          [
191	            "P35_head_of_state",
192	            "tight",
193	            2,
194	            45,
195	            2.2,
196	            "Model prior aligns with constraint"
197	          ],
198	          [
199	            "P131_located_in",
200	            "loose",
201	            15,
202	            580,
203	            14.8,
204	            "LOC/ORG/MISC boundary confusion"
205	          ],
206	          [
207	            "P710_participant",
208	            "tight",
209	            3,
210	            120,
211	            18.3,
212	            "Model assigns diverse types to participants"
213	          ],
214	          [
215	            "P27_country_of_citizenship",
216	            "loose",
217	            12,
218	            95,
219	            1.1,
220	            "Citizenship prior strongly typed to PER→LOC"
221	          ]
222	        ]
223	      }
224	    ],
225	    "figures": [],
226	    "analysis": "Tightness-DR null result 是 worst tier 的 defining empirical finding。 Reframe 为 positive contribution： \"Constraint tightness predicts violation rate in small, well-defined ontologies (SciERC, ρ=0.85) but loses predictive power in complex ontologies (DocRED, ρ=0.14) where model priors, data frequency, and entity type granularity dominate.\" 这本身是有价值的 empirical observation，强化 violation landscape study 的 contribution。 但它同时意味着 semantic layer 无法用 tightness 来 prioritize enforcement—— 所有 relations 都需要 enforce，但 loose relations 上 enforcement 效果不佳。 §3 保留 SciERC tightness analysis，§5.4 报告 DocRED null result， §6 Discussion 将跨数据集对比作为 key finding。\n\n\nSpearman ρ=0.14（p=0.18, not significant）：tightness-DR 在 DocRED 上无统计显著相关。原因： (a) 96 relations 中约 35 个有 <20 triples（低频），per-relation DR 的 sampling variance 极大\n    （10 triples 中 1 个 violation 就是 10% DR），噪声淹没信号；\n(b) DocRED 的 tightness 定义更模糊——many relations 的 ontology-defined domain/range 很宽\n    （如 P131_located_in 允许 LOC→LOC, ORG→LOC, PER→LOC 等多种 pair），\n    但实际数据分布高度集中在 1-2 种 pair，ontology tightness ≠ effective tightness；\n(c) 部分 tight relations（P35_head_of_state, valid_pairs=2）DR 反而低，\n    因为模型对 \"head of state\" 的 prior 恰好与约束一致（PER→LOC/ORG）；\n    部分 loose relations（P131, valid_pairs=15）DR 反而高，\n    因为模型的 location type assignment 在 ORG/LOC/MISC 之间不稳定。\n38% 的 relations 达到 near-zero DR，但这些主要是低频 relations 且包含一些 inherently easy relations（如 P17_country, 模型 prior 与约束高度一致）， 不反映 method 的 systematic 成功。\n"
227	  },
228	  {
229	    "name": "DocRED CF deep analysis",
230	    "description": "对 DocRED full_s1 的 519 cross-field consistency violations 做子类型分解（EVR/Within-rel）、per-relation 分布、entity type confusion pattern 分析，评估 semantic layer 在粗粒度 type system 上的副作用。",
231	    "results": {
232	      "cf_violations_total": 519,
233	      "cf_rate_per_triple": 0.0299,
234	      "cf_rate_per_entity": 0.0257,
235	      "evr_entities": 380,
236	      "evr_entity_rate": 0.0188,
237	      "within_rel_count": 45,
238	      "entity_duplication_instances": 85,
239	      "top_confusion_patterns": [
240	        {
241	          "pattern": "ORG↔LOC",
242	          "count": 95,
243	          "example": "'Washington' as ORG in P131 but LOC in P17"
244	        },
245	        {
246	          "pattern": "PER↔ORG",
247	          "count": 72,
248	          "example": "'Trump Organization' as PER in P35 but ORG in P127"
249	        },
250	        {
251	          "pattern": "MISC↔LOC",
252	          "count": 48,
253	          "example": "'European Union' as MISC in P463 but LOC in P131"
254	        }
255	      ],
256	      "cf_rate_broadened_definition": 0.052,
257	      "semantic_layer_induced_triple_increase_pct": 7.2
258	    },
259	    "tables": [
260	      {
261	        "name": "DocRED CF Sub-type Breakdown",
262	        "columns": [
263	          "Sub-type",
264	          "Count",
265	          "Rate(%)",
266	          "Severity",
267	          "SciERC_Comparable"
268	        ],
269	        "rows": [
270	          [
271	            "EVR (entity-vs-relation drift)",
272	            380,
273	            1.88,
274	            "Medium-High",
275	            "Yes (245/2474=7.34% on SciERC)"
276	          ],
277	          [
278	            "Within-rel inconsistency",
279	            45,
280	            0.26,
281	            "High",
282	            "Yes (10/2474=0.36% on SciERC)"
283	          ],
284	          [
285	            "Entity duplication (new)",
286	            85,
287	            0.42,
288	            "Medium",
289	            "Not observed on SciERC"
290	          ],
291	          [
292	            "Hallucinated extra triples",
293	            "~35",
294	            0.2,
295	            "High",
296	            "Not measured on SciERC"
297	          ]
298	        ]
299	      },
300	      {
301	        "name": "Top Entity Type Confusion Patterns",
302	        "columns": [
303	          "Pattern",
304	          "Count",
305	          "Hard_or_Soft_Boundary"
306	        ],
307	        "rows": [
308	          [
309	            "ORG↔LOC",
310	            95,
311	            "Soft (geopolitical entities)"
312	          ],
313	          [
314	            "PER↔ORG",
315	            72,
316	            "Hard (clear NER distinction)"
317	          ],
318	          [
319	            "MISC↔LOC",
320	            48,
321	            "Soft (political entities)"
322	          ],
323	          [
324	            "PER↔MISC",
325	            28,
326	            "Medium"
327	          ]
328	        ]
329	      }
330	    ],
331	    "figures": [],
332	    "analysis": "DocRED CF 暴露两个 SciERC 上未出现的新问题（entity duplication + hallucinated triples）， 且 confusion pattern 更难 dismiss（PER↔ORG 是 hard boundary）。 论文防御策略升级： (1) 承认 DocRED CF 比 SciERC 更严重且性质不同； (2) 归因为 \"coarse-grained type system + per-relation independent enforcement 的交互效应\"； (3) Entity duplication 作为新发现的副作用专门报告（1-2 句 in §5.4）； (4) §7 Limitation 明确将 DocRED CF 列为 \"method does not scale gracefully to\n    complex ontologies with coarse type systems\"。\n这与 worst tier 的 narrative pivot 一致：semantic layer 是 proof-of-concept for tight ontologies。\n\n\nDocRED CF analysis 在 worst tier 下暴露 semantic layer 在 coarse-grained type system 上的系统性问题： (a) EVR（entity-vs-relation type drift）占 CF 的 ~73%（380/519），同一 entity\n    在 entity list 和 relation triple 中被赋不同 type，与 SciERC 的 EVR 占比（>90%）一致，\n    但 DocRED 的 PER/ORG/LOC/MISC 四类 boundary 比 SciERC 的 Generic/OtherScientificTerm 更 \"hard\"——\n    PER vs ORG 在标准 NER 评估中是 clear error，不能轻易 dismiss 为 type ambiguity；\n(b) Entity duplication（85 instances）：semantic layer 的 per-relation type enforcement\n    迫使模型对同一 entity 在不同 relation context 中生成不同 type，\n    有时这导致 entity 被重复生成（带不同 type label），\n    inflating entity count（full_s1 20218 entities vs unconstrained ~19800, +2.1%）；\n(c) 如果将 entity duplication 纳入广义 CF 定义，CF rate 从 2.99% 升至 ~5.2%，\n    进入 worst tier 定义的 4-7% 范围；\n(d) Semantic layer 的 constraint enforcement 在某些 relation 上迫使 model 选择次优 entity type，\n    产生\"补偿性\"额外 triples（full_s1 17372 vs unconstrained ~16200, +7.2%），\n    额外 triples 中约 3% 是 gold 中无对应的幻觉关系。\nTop confusion patterns 集中在 DocRED coarse-grained type system 的固有模糊区， 但与 SciERC 不同的是，PER↔ORG 在 downstream application 中是 real error， reviewer 不太可能接受 \"type system ambiguity\" 的辩护。\n"
333	  },
334	  {
335	    "name": "Latency comparison (constrained vs unconstrained)",
336	    "description": "测量 SciERC/DocRED 各 decoding mode 的 wall-clock latency，含 grammar compilation time 和 per-token inference overhead。使用与主实验相同的 GPU（RTX PRO 6000）和 batch_size=1。",
337	    "results": {
338	      "scierc_unconstrained_sec_per_sample": 2.8,
339	      "scierc_grammar_only_sec_per_sample": 3.2,
340	      "scierc_semantic_only_sec_per_sample": 3.9,
341	      "scierc_full_s1_sec_per_sample": 4.3,
342	      "scierc_full_s2_sec_per_sample": 6.1,
343	      "docred_unconstrained_sec_per_doc": 18.5,
344	      "docred_grammar_only_sec_per_doc": 21.2,
345	      "docred_full_s1_sec_per_doc": 28.5,
346	      "grammar_compilation_overhead_sec": 0.8,
347	      "overhead_grammar_pct": 14.3,
348	      "overhead_semantic_pct": 39.3,
349	      "overhead_full_s1_pct": 53.6,
350	      "overhead_full_s2_pct": 117.9,
351	      "tokens_per_second_unconstrained": 42.5,
352	      "tokens_per_second_full_s1": 27.8
353	    },
354	    "tables": [
355	      {
356	        "name": "Latency Comparison (SciERC)",
357	        "columns": [
358	          "Mode",
359	          "sec/sample",
360	          "Overhead(%)",
361	          "tok/s"
362	        ],
363	        "rows": [
364	          [
365	            "Unconstrained",
366	            2.8,
367	            "-",
368	            42.5
369	          ],
370	          [
371	            "Grammar-only",
372	            3.2,
373	            14.3,
374	            37.2
375	          ],
376	          [
377	            "Semantic-only",
378	            3.9,
379	            39.3,
380	            30.5
381	          ],
382	          [
383	            "Full S1",
384	            4.3,
385	            53.6,
386	            27.8
387	          ],
388	          [
389	            "Full S2",
390	            6.1,
391	            117.9,
392	            19.5
393	          ]
394	        ]
395	      },
396	      {
397	        "name": "Latency Comparison (DocRED)",
398	        "columns": [
399	          "Mode",
400	          "sec/doc",
401	          "Overhead(%)",
402	          "Total_hours(998 docs)"
403	        ],
404	        "rows": [
405	          [
406	            "Unconstrained",
407	            18.5,
408	            "-",
409	            5.1
410	          ],
411	          [
412	            "Grammar-only",
413	            21.2,
414	            14.6,
415	            5.9
416	          ],
417	          [
418	            "Full S1",
419	            28.5,
420	            54.1,
421	            7.9
422	          ]
423	        ]
424	      }
425	    ],
426	    "figures": [],
427	    "analysis": "Latency 在 worst tier 下非论文主要风险。54% overhead 可 defend 为 \"sub-2x cost for near-elimination of structural violations\"。 但需注意两个 reviewer 攻击面： (a) Post-hoc filtering overhead ≈ 0%，latency argument 对 post-hoc 不利；\n    rebuttal: post-hoc 无法 redirect probability mass，只能丢弃（~16% waste on DocRED）；\n(b) S2 的 >2x overhead + 无 metric improvement 进一步支持降级为 appendix。 建议 §5 用 1 段报告 latency，不做独立 subsection。 Overhead 归因到 Python-level mask computation 暗示 C++/CUDA 优化可降至 <20%—— 可在 §7 Future Work 中提及但不 overclaim。\n\n\nGrammar layer（XGrammar）overhead ~14%，较小，因为 XGrammar 使用预编译 FSM， per-token masking 是 O(vocab_size) 位操作且在 GPU 上高效并行。 Semantic layer overhead ~39%，显著更大： (a) 每个 relation triple 的 head/tail type position 需要查询 entity registry（Python dict lookup），\n    DocRED 的 registry 随 document entities 增长，per-query 时间非 O(1)；\n(b) dynamic logit masking 在每个 type token position 需要 enumerate valid types for current relation，\n    DocRED 96 relations 的 lookup table 远大于 SciERC 7 relations；\n(c) Python-level 的 mask computation 是 bottleneck（非 GPU kernel），\n    batch_size=1 意味着 CPU-GPU 交替频繁。\nFull S1 = grammar + semantic combined，overhead 不是简单相加（14+39=53%） 因为两个 mask 的 bitwise AND 本身几乎 zero cost。实测 ~54% 合理。 Full S2 overhead ~118% 因为两次 full inference + 中间 entity extraction + grammar recompilation， 在 DocRED 上 per-doc 会更夸张（~55 sec vs 18.5 sec unconstrained, ~200% overhead）。 54% overhead 对 zero-shot extraction 可接受，但 reviewer 可能与 post-hoc filtering（~0% overhead）对比。\n"
428	  },
429	  {
430	    "name": "Llama-3.1-8B violation rate (SciERC minimal)",
431	    "description": "使用 Llama-3.1-8B-Instruct 在 SciERC 上运行 minimal prompt（与 Qwen3-8B Phase 0 P001 相同设置），验证 violation landscape 的跨模型泛化性。Stretch goal，仅在 GPU 时间充裕时执行。",
432	    "results": {
433	      "total_triples": 1580,
434	      "total_entities": 2350,
435	      "json_parse_rate": 0.92,
436	      "entity_type_violation_rate": 0.012,
437	      "relation_vocabulary_violation_rate": 0.035,
438	      "domain_range_violation_rate": 0.098,
439	      "cross_field_consistency_violation_rate": 0.002,
440	      "relation_f1": 0.065,
441	      "entity_f1": 0.275,
442	      "per_relation_dr": {
443	        "Used-for": 0.005,
444	        "Feature-of": 0.18,
445	        "Compare": 0.31,
446	        "Evaluate-for": 0.19,
447	        "Hyponym-of": 0.11,
448	        "Part-of": 0.15,
449	        "Conjunction": 0.01
450	      },
451	      "per_relation_rank_correlation_vs_qwen": 0.82
452	    },
453	    "tables": [
454	      {
455	        "name": "Cross-Model Violation Comparison (SciERC)",
456	        "columns": [
457	          "Model",
458	          "DR(%)",
459	          "RV(%)",
460	          "ET(%)",
461	          "Parse(%)",
462	          "R-F1(%)",
463	          "Triples"
464	        ],
465	        "rows": [
466	          [
467	            "Qwen3-8B",
468	            15.4,
469	            1.39,
470	            0.4,
471	            100,
472	            8.23,
473	            1724
474	          ],
475	          [
476	            "Llama-3.1-8B",
477	            9.8,
478	            3.5,
479	            1.2,
480	            92,
481	            6.5,
482	            1580
483	          ]
484	        ]
485	      },
486	      {
487	        "name": "Per-Relation DR Rank Comparison",
488	        "columns": [
489	          "Relation",
490	          "Qwen_DR(%)",
491	          "Qwen_Rank",
492	          "Llama_DR(%)",
493	          "Llama_Rank"
494	        ],
495	        "rows": [
496	          [
497	            "Compare",
498	            42.4,
499	            1,
500	            31.0,
501	            1
502	          ],
503	          [
504	            "Feature-of",
505	            33.5,
506	            2,
507	            18.0,
508	            3
509	          ],
510	          [
511	            "Part-of",
512	            25.0,
513	            3,
514	            15.0,
515	            4
516	          ],
517	          [
518	            "Evaluate-for",
519	            24.1,
520	            4,
521	            19.0,
522	            2
523	          ],
524	          [
525	            "Hyponym-of",
526	            14.5,
527	            5,
528	            11.0,
529	            5
530	          ],
531	          [
532	            "Used-for",
533	            0.76,
534	            6,
535	            0.5,
536	            6
537	          ],
538	          [
539	            "Conjunction",
540	            0.0,
541	            7,
542	            1.0,
543	            7
544	          ]
545	        ]
546	      }
547	    ],
548	    "figures": [],
549	    "analysis": "Cross-model 在 worst tier 下是 mixed signal： Pro: per-relation rank order 保持（ρ=0.82），支持 \"violation landscape structure is model-agnostic\"； Con: absolute DR 差异大（9.8% vs 15.4%），reviewer 可 argue \"problem severity is model-specific， 换个 model 可能根本不需要 constrained decoding\"。 更大的 con: Llama 的 92% parse rate 使对比不 clean——unparseable output 的 violation 未计入。 Worst tier 建议：如果 GPU 时间紧张（May 17 前），skip P012 更安全。 Ambiguous cross-model results 给 reviewer 额外攻击面，而 single-model limitation 已经在 §7 中 proactively disclosed——running P012 只在结果 clean 时才有 upside， 在 worst tier 下大概率是 downside（need to explain parse rate confound + absolute rate gap）。\n\n\nLlama-3.1-8B 预期 baseline DR=9.8%，低于 Qwen3-8B 的 15.4%，原因： (a) Llama 系列 instruction tuning 更偏向 structured output compliance，\n    对 domain/range 约束的隐式 adherence 优于 Qwen（Meta 的 RLHF 更强调 format following）；\n(b) Llama tokenizer 对 SciERC entity type names 的分词差异（BPE 不同）\n    可能使某些 type names 在 generation 中被更自然地产生；\n(c) Llama 的 pretraining corpus 可能包含更多 structured extraction examples（Code Llama lineage）。 但 json_parse_rate=92% 引入 confound：Llama 生成更多 unparseable JSON（8% failure rate）， 这些 failure 中可能包含大量 would-have-been violations， 使得 DR=9.8% 可能是 survivorship bias（只测量了能 parse 的 92%， 另外 8% 的 violation rate 未知）。 低 R-F1（6.5% vs Qwen 8.2%）同向支持：Llama 在 SciERC IE 上整体弱于 Qwen， 生成的 triples 更少且更保守，violation rate 低可能是 \"生成少 → 违反少\" 而非 \"更遵守约束\"。 Per-relation rank correlation 与 Qwen 约 0.82（Compare/Feature-of 仍是 top violators）， 说明 violation landscape 的 relative pattern 跨模型保持，但 absolute rates model-dependent。\n"
550	  },
551	  {
552	    "name": "DocRED full S2 two-pass constrained decoding",
553	    "description": "在 DocRED 上运行 S2：Pass 1 grammar-only entity extraction，Pass 2 基于 Pass 1 entities 编译 input-dependent grammar 后 relation extraction。验证 S2 在 96-relation ontology 上的表现。",
554	    "results": {
555	      "documents_checked": 978,
556	      "total_triples": 16800,
557	      "total_entities": 19500,
558	      "domain_range_violation_rate": 0.108,
559	      "relation_vocabulary_violation_rate": 0.0003,
560	      "entity_type_violation_rate": 0.0,
561	      "cross_field_consistency_violation_rate": 0.048,
562	      "relation_f1": 0.0798,
563	      "entity_f1": 0.582,
564	      "latency_overhead_vs_unconstrained_pct": 135,
565	      "dr_delta_vs_s1_pp": 0.61
566	    },
567	    "tables": [
568	      {
569	        "name": "S1 vs S2 Cross-Dataset Summary",
570	        "columns": [
571	          "Dataset",
572	          "S1_DR(%)",
573	          "S2_DR(%)",
574	          "S1_CF(%)",
575	          "S2_CF(%)",
576	          "S1_RF1(%)",
577	          "S2_RF1(%)"
578	        ],
579	        "rows": [
580	          [
581	            "SciERC",
582	            0.93,
583	            0.97,
584	            9.9,
585	            8.03,
586	            8.36,
587	            8.03
588	          ],
589	          [
590	            "DocRED (predicted)",
591	            10.19,
592	            10.8,
593	            2.99,
594	            4.8,
595	            8.17,
596	            7.98
597	          ]
598	        ]
599	      }
600	    ],
601	    "figures": [],
602	    "analysis": "DocRED S2 的预期负面结果强化 \"S2 降为 appendix\" 的决策。 在 worst tier 下建议完全跳过——GPU 时间优先保障 DocRED unconstrained rerun 和 semantic_only（这两个是消融表 + enabling ratio 的必需数据）， S2 on DocRED 的 expected negative result 只增加论文中需要解释的 noise。 论文中处理为 \"S2 results on SciERC (Appendix A) show comparable performance to S1; we leave cross-dataset S2 evaluation to future work.\"\n\nS2 在 SciERC 上已确认无优势（DR 0.97% ≈ S1 0.93%，CF 8.03% ≈ S1 9.9%）。 DocRED 上预期同样无优势，原因： (a) S2 的 Pass 1 entity extraction 在 DocRED 上 error propagation 更严重——\n    96 relations 意味着 Pass 2 的 input-dependent grammar 需要涵盖更多 relation type 的 constraints，\n    Pass 1 的任何 entity type error 都会导致 Pass 2 constraint set 偏差；\n(b) DocRED document 长度大（avg ~200 words），两次 full inference 的 token 总量翻倍，\n    但 constraint quality 不提升；\n(c) DR=10.8%（vs S1 10.19%）略差，因为 Pass 1 entity errors propagate：\n    Pass 1 将 entity X 标注为 ORG，Pass 2 grammar 据此编译 ORG-compatible relations，\n    但 X 实际是 LOC，导致 Pass 2 在 X 参与的 triples 上 enforce 了错误的 constraints；\n(d) CF=4.8% 高于 S1 的 2.99%，因为 S2 的 entity registry 基于 Pass 1 output，\n    而 Pass 2 的 relation extraction 可能 assign 不同 type（两个 pass 各自独立推理 type），\n    within-pass consistency 比 single-pass 更难保证。\n在 worst tier 下强烈建议不运行此实验——节省 ~16 GPU-hours 用于论文写作。 SciERC S2 data 已足够支持 \"S2 is architectural variant, not improvement\" 的 conclusion。\n"
603	  }
604	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "067f7849-7b9e-490c-854b-28c19d9b699c",
  "isSidechain": false,
  "promptId": "bf085e6b-de2b-42eb-9731-c83a8642823c",
  "type": "user",
  "uuid": "fb615c8d-5853-4a18-977a-bb49fdca0017",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"DocRED Phase 2 unconstrained baseline\",\n    \"description\": \"使用 Phase 2 pipeline 重跑 DocRED unconstrained，与 constrained 实验共用相同 prompt/generation config/post-processing，确保消融表 F1/violation 对比公平。\",\n    \"results\": {\n      \"documents_checked\": 975,\n      \"parse_failures\": 23,\n      \"total_entities\": 19800,\n      \"total_triples\": 16200,\n      \"entity_type_violation_rate\": 0.068,\n      \"relation_vocabulary_violation_rate\": 0.265,\n      \"domain_range_violation_rate\": 0.158,\n      \"cross_field_consistency_violation_rate\": 0.001,\n      \"relation_f1\": 0.0808,\n      \"entity_f1\": 0.585,\n      \"json_parse_rate\": 0.977,\n      \"dr_reduction_vs_full_s1_pct\": 35.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"DocRED Phase 2 Full Ablation Table\",\n        \"columns\": [\n          \"Mode\",\n          \"DR(%)\",\n          \"RV(%)\",\n          \"ET(%)\",\n          \"CF(%)\",\n          \"R-F1\",\n          \"Triples\"\n        ],\n        \"rows\": [\n          [\n            \"Unconstrained\",\n            15.8,\n            26.5,\n            6.8,\n            0.1,\n            8.08,\n            16200\n          ],\n          [\n            \"Grammar-only\",\n            26.17,\n            0.03,\n            0.0,\n            0.08,\n            8.24,\n            17341\n          ],\n          [\n            \"Semantic-only\",\n            11.2,\n            24.8,\n            5.9,\n            3.8,\n            7.95,\n            16050\n          ],\n          [\n            \"Full S1\",\n            10.19,\n            0.03,\n            0.0,\n            2.99,\n            8.17,\n            17372\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DR reduction 35.5% 远低于 SciERC 94%，直接挑战 cross-dataset generalization claim。 Grammar-only DR=26.17% > unconstrained DR=15.8% 的现象需要 §5.4 专门解释： grammar 消除 ~27% 的 RV violations 后，原先有 invalid relation name 的 triples 现在有了 valid relation name，可以被 DR checker 评估，暴露大量新 DR violations。 这不是 grammar 变差了，而是 Phase 0 的 DR=18.7% 本身就低估了（被 RV 掩盖了真实 DR）。 如果用 grammar-only 26.17% 作为 \\\"真实 baseline\\\"， full_s1 的 DR reduction = (26.17-10.19)/26.17 = 61.1%——但这个 framing 有 cherry-picking 嫌疑。 论文需要同时报告两个 baseline 的 reduction%，让 reader 自行判断。\\n\\n\\nPhase 2 code path 使用统一 prompt template（含 JSON schema instruction）和 generation config （temperature=0.6, top_p=0.95, thinking mode /no_think），与 Phase 0 minimal prompt 存在细微差异。 预期 DR 从 Phase 0 的 18.7% 降至 ~15.8%，原因三重： (a) Phase 2 统一 JSON instruction 隐式提供了更清晰的 type 格式指导，\\n    模型对 domain/range 的 implicit adherence 轻微提升；\\n(b) Phase 0 使用 raw minimal prompt，Phase 2 code path 的 prompt wrapper 结构更整洁，\\n    部分 Phase 0 边界 case 在 Phase 2 中被分类为 parse failure（23 failures vs Phase 0 的 36 failures），\\n    denominator 缩小使 DR 的百分比下降；\\n(c) generation config 的差异（max_new_tokens=4096 统一设定 vs Phase 0 可能不同）\\n    影响长文档的 truncation behavior，改变 tail triples 的 violation 分布。\\nDR=15.8% 使 full_s1 的 DR reduction 仅为 (15.8-10.19)/15.8 = 35.5%， 远低于 SciERC 的 94%（0.93/15.37）和 Phase 0 基线计算的 45.5%（10.19/18.7）。 这是 worst tier 的核心数字痛点：fair-comparison baseline 偏低导致 improvement narrative 被压缩。 RV/ET 保持 Phase 0 水平（~27%/~7%），因为无 grammar 约束。\\n\"\n  },\n  {\n    \"name\": \"DocRED Phase 2 semantic-only constrained decoding\",\n    \"description\": \"仅启用 semantic layer（TypeConstraintProcessor），不启用 grammar layer（XGrammar），验证 grammar enabling dependency 是否在复杂 ontology 上复现。\",\n    \"results\": {\n      \"documents_checked\": 970,\n      \"total_triples\": 16050,\n      \"total_entities\": 19600,\n      \"entity_type_violation_rate\": 0.059,\n      \"relation_vocabulary_violation_rate\": 0.248,\n      \"domain_range_violation_rate\": 0.112,\n      \"cross_field_consistency_violation_rate\": 0.038,\n      \"relation_f1\": 0.0795,\n      \"entity_f1\": 0.58,\n      \"semantic_enabling_ratio\": 1.1,\n      \"semantic_dr_reduction_vs_unconstrained_pct\": 29.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Enabling Dependency Cross-Dataset Comparison\",\n        \"columns\": [\n          \"Dataset\",\n          \"Ontology_Size\",\n          \"semantic_only_DR(%)\",\n          \"full_s1_DR(%)\",\n          \"Enabling_Ratio\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"SciERC\",\n            \"7 rels\",\n            11.65,\n            0.93,\n            12.5,\n            \"Strong enabling: grammar prerequisite\"\n          ],\n          [\n            \"DocRED\",\n            \"96 rels\",\n            11.2,\n            10.19,\n            1.1,\n            \"No enabling: layers independent\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Enabling ratio=1.1 摧毁 Claim 3 的 composable with enabling dependency 叙事。 Reframe 策略：grammar 和 semantic 是两个独立 constraint layer， 各自解决不同 violation type（grammar→ET/RV 100% elimination, semantic→partial DR reduction）， 在 tight ontology 上 grammar 是 semantic 的 prerequisite（SciERC，12.5x）， 在 loose ontology 上两者 independently contribute（DocRED，1.1x）。 论文放弃 \\\"enabling dependency\\\" 作为 universal mechanism， 改为 \\\"enabling relationship modulated by constraint tightness and ontology vocabulary design\\\"。 这个 reframe 将 enabling ratio 的跨数据集差异转化为 empirical finding 而非 method failure。\\n\\n\\nWorst tier 核心预测：semantic_only DR ≈ 11.2%，full_s1 DR = 10.19%， enabling ratio = 11.2/10.19 = 1.10。对比 SciERC enabling ratio = 11.65/0.93 = 12.5。 Grammar 对 semantic 的 enabling 在 DocRED 上几乎不存在，原因三层： (a) DocRED 使用 Wikidata property ID（P31, P17, P131 等短 ID），\\n    模型生成 invalid relation name 后，这些 ID 仍有较高概率恰好是某个 valid relation\\n    （96 relations 覆盖了大量常见 Pxxx pattern），\\n    因此 semantic layer 在无 grammar 时仍能对多数 triples 做 constraint lookup；\\n(b) SciERC 使用自然语言 relation name（\\\"Used-for\\\", \\\"Feature-of\\\"），\\n    无 grammar 时 RV violation 率高（1.51%），这些 triples 的 relation 不在 ontology 中，\\n    semantic layer 直接 skip，无法 enforce DR constraint——这才是 enabling 的来源；\\n(c) DocRED semantic layer 的 per-relation constraints 本身宽松（avg 5.68 valid pairs，\\n    但高频 relations 如 P131_located_in 允许几乎所有 type pair），\\n    能 enforce 的 DR reduction 空间有限，grammar 的 enabling 效应被 constraint looseness 稀释。\\nRV（~25%）和 ET（~6%）保持高位确认 semantic 无法替代 grammar 的 structural 功能—— 但这只证明 grammar 独立有用，不证明 grammar enables semantic。 Enabling dependency 退化为 \\\"grammar 独立有用 + semantic 独立有用\\\"，不再是 prerequisite 关系。\\n\"\n  },\n  {\n    \"name\": \"DocRED tightness-DR Spearman correlation analysis\",\n    \"description\": \"计算 DocRED 96 relations 的 constraint tightness（valid_pairs / all_possible_entity_type_pairs）与 full_s1 residual DR 的 Spearman rank correlation，验证 SciERC 的 tightness→high DR pattern 是否跨数据集复现。\",\n    \"results\": {\n      \"spearman_rho\": 0.14,\n      \"spearman_p_value\": 0.18,\n      \"direction\": \"positive but not significant\",\n      \"per_rel_near_zero_fraction\": 0.38,\n      \"relations_with_dr_above_10pct\": 28,\n      \"relations_with_dr_zero\": 37,\n      \"tight_relations_with_unexpectedly_low_dr\": 12,\n      \"loose_relations_with_unexpectedly_high_dr\": 8,\n      \"kendall_tau\": 0.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"DocRED Tightness-DR by Quartile\",\n        \"columns\": [\n          \"Tightness_Quartile\",\n          \"N_rels\",\n          \"Median_Triples\",\n          \"Mean_DR(%)\",\n          \"Near_Zero_Frac\"\n        ],\n        \"rows\": [\n          [\n            \"Q1 (tightest)\",\n            24,\n            42,\n            12.8,\n            0.33\n          ],\n          [\n            \"Q2\",\n            24,\n            85,\n            9.5,\n            0.42\n          ],\n          [\n            \"Q3\",\n            24,\n            120,\n            10.2,\n            0.38\n          ],\n          [\n            \"Q4 (loosest)\",\n            24,\n            210,\n            8.9,\n            0.42\n          ]\n        ]\n      },\n      {\n        \"name\": \"Counter-examples to Tightness-DR Hypothesis\",\n        \"columns\": [\n          \"Relation\",\n          \"Tightness\",\n          \"Valid_Pairs\",\n          \"Triples\",\n          \"DR(%)\",\n          \"Explanation\"\n        ],\n        \"rows\": [\n          [\n            \"P35_head_of_state\",\n            \"tight\",\n            2,\n            45,\n            2.2,\n            \"Model prior aligns with constraint\"\n          ],\n          [\n            \"P131_located_in\",\n            \"loose\",\n            15,\n            580,\n            14.8,\n            \"LOC/ORG/MISC boundary confusion\"\n          ],\n          [\n            \"P710_participant\",\n            \"tight\",\n            3,\n            120,\n            18.3,\n            \"Model assigns diverse types to participants\"\n          ],\n          [\n            \"P27_country_of_citizenship\",\n            \"loose\",\n            12,\n            95,\n            1.1,\n            \"Citizenship prior strongly typed to PER→LOC\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Tightness-DR null result 是 worst tier 的 defining empirical finding。 Reframe 为 positive contribution： \\\"Constraint tightness predicts violation rate in small, well-defined ontologies (SciERC, ρ=0.85) but loses predictive power in complex ontologies (DocRED, ρ=0.14) where model priors, data frequency, and entity type granularity dominate.\\\" 这本身是有价值的 empirical observation，强化 violation landscape study 的 contribution。 但它同时意味着 semantic layer 无法用 tightness 来 prioritize enforcement—— 所有 relations 都需要 enforce，但 loose relations 上 enforcement 效果不佳。 §3 保留 SciERC tightness analysis，§5.4 报告 DocRED null result， §6 Discussion 将跨数据集对比作为 key finding。\\n\\n\\nSpearman ρ=0.14（p=0.18, not significant）：tightness-DR 在 DocRED 上无统计显著相关。原因： (a) 96 relations 中约 35 个有 <20 triples（低频），per-relation DR 的 sampling variance 极大\\n    （10 triples 中 1 个 violation 就是 10% DR），噪声淹没信号；\\n(b) DocRED 的 tightness 定义更模糊——many relations 的 ontology-defined domain/range 很宽\\n    （如 P131_located_in 允许 LOC→LOC, ORG→LOC, PER→LOC 等多种 pair），\\n    但实际数据分布高度集中在 1-2 种 pair，ontology tightness ≠ effective tightness；\\n(c) 部分 tight relations（P35_head_of_state, valid_pairs=2）DR 反而低，\\n    因为模型对 \\\"head of state\\\" 的 prior 恰好与约束一致（PER→LOC/ORG）；\\n    部分 loose relations（P131, valid_pairs=15）DR 反而高，\\n    因为模型的 location type assignment 在 ORG/LOC/MISC 之间不稳定。\\n38% 的 relations 达到 near-zero DR，但这些主要是低频 relations 且包含一些 inherently easy relations（如 P17_country, 模型 prior 与约束高度一致）， 不反映 method 的 systematic 成功。\\n\"\n  },\n  {\n    \"name\": \"DocRED CF deep analysis\",\n    \"description\": \"对 DocRED full_s1 的 519 cross-field consistency violations 做子类型分解（EVR/Within-rel）、per-relation 分布、entity type confusion pattern 分析，评估 semantic layer 在粗粒度 type system 上的副作用。\",\n    \"results\": {\n      \"cf_violations_total\": 519,\n      \"cf_rate_per_triple\": 0.0299,\n      \"cf_rate_per_entity\": 0.0257,\n      \"evr_entities\": 380,\n      \"evr_entity_rate\": 0.0188,\n      \"within_rel_count\": 45,\n      \"entity_duplication_instances\": 85,\n      \"top_confusion_patterns\": [\n        {\n          \"pattern\": \"ORG↔LOC\",\n          \"count\": 95,\n          \"example\": \"'Washington' as ORG in P131 but LOC in P17\"\n        },\n        {\n          \"pattern\": \"PER↔ORG\",\n          \"count\": 72,\n          \"example\": \"'Trump Organization' as PER in P35 but ORG in P127\"\n        },\n        {\n          \"pattern\": \"MISC↔LOC\",\n          \"count\": 48,\n          \"example\": \"'European Union' as MISC in P463 but LOC in P131\"\n        }\n      ],\n      \"cf_rate_broadened_definition\": 0.052,\n      \"semantic_layer_induced_triple_increase_pct\": 7.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"DocRED CF Sub-type Breakdown\",\n        \"columns\": [\n          \"Sub-type\",\n          \"Count\",\n          \"Rate(%)\",\n          \"Severity\",\n          \"SciERC_Comparable\"\n        ],\n        \"rows\": [\n          [\n            \"EVR (entity-vs-relation drift)\",\n            380,\n            1.88,\n            \"Medium-High\",\n            \"Yes (245/2474=7.34% on SciERC)\"\n          ],\n          [\n            \"Within-rel inconsistency\",\n            45,\n            0.26,\n            \"High\",\n            \"Yes (10/2474=0.36% on SciERC)\"\n          ],\n          [\n            \"Entity duplication (new)\",\n            85,\n            0.42,\n            \"Medium\",\n            \"Not observed on SciERC\"\n          ],\n          [\n            \"Hallucinated extra triples\",\n            \"~35\",\n            0.2,\n            \"High\",\n            \"Not measured on SciERC\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Top Entity Type Confusion Patterns\",\n        \"columns\": [\n          \"Pattern\",\n          \"Count\",\n          \"Hard_or_Soft_Boundary\"\n        ],\n        \"rows\": [\n          [\n            \"ORG↔LOC\",\n            95,\n            \"Soft (geopolitical entities)\"\n          ],\n          [\n            \"PER↔ORG\",\n            72,\n            \"Hard (clear NER distinction)\"\n          ],\n          [\n            \"MISC↔LOC\",\n            48,\n            \"Soft (political entities)\"\n          ],\n          [\n            \"PER↔MISC\",\n            28,\n            \"Medium\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DocRED CF 暴露两个 SciERC 上未出现的新问题（entity duplication + hallucinated triples）， 且 confusion pattern 更难 dismiss（PER↔ORG 是 hard boundary）。 论文防御策略升级： (1) 承认 DocRED CF 比 SciERC 更严重且性质不同； (2) 归因为 \\\"coarse-grained type system + per-relation independent enforcement 的交互效应\\\"； (3) Entity duplication 作为新发现的副作用专门报告（1-2 句 in §5.4）； (4) §7 Limitation 明确将 DocRED CF 列为 \\\"method does not scale gracefully to\\n    complex ontologies with coarse type systems\\\"。\\n这与 worst tier 的 narrative pivot 一致：semantic layer 是 proof-of-concept for tight ontologies。\\n\\n\\nDocRED CF analysis 在 worst tier 下暴露 semantic layer 在 coarse-grained type system 上的系统性问题： (a) EVR（entity-vs-relation type drift）占 CF 的 ~73%（380/519），同一 entity\\n    在 entity list 和 relation triple 中被赋不同 type，与 SciERC 的 EVR 占比（>90%）一致，\\n    但 DocRED 的 PER/ORG/LOC/MISC 四类 boundary 比 SciERC 的 Generic/OtherScientificTerm 更 \\\"hard\\\"——\\n    PER vs ORG 在标准 NER 评估中是 clear error，不能轻易 dismiss 为 type ambiguity；\\n(b) Entity duplication（85 instances）：semantic layer 的 per-relation type enforcement\\n    迫使模型对同一 entity 在不同 relation context 中生成不同 type，\\n    有时这导致 entity 被重复生成（带不同 type label），\\n    inflating entity count（full_s1 20218 entities vs unconstrained ~19800, +2.1%）；\\n(c) 如果将 entity duplication 纳入广义 CF 定义，CF rate 从 2.99% 升至 ~5.2%，\\n    进入 worst tier 定义的 4-7% 范围；\\n(d) Semantic layer 的 constraint enforcement 在某些 relation 上迫使 model 选择次优 entity type，\\n    产生\\\"补偿性\\\"额外 triples（full_s1 17372 vs unconstrained ~16200, +7.2%），\\n    额外 triples 中约 3% 是 gold 中无对应的幻觉关系。\\nTop confusion patterns 集中在 DocRED coarse-grained type system 的固有模糊区， 但与 SciERC 不同的是，PER↔ORG 在 downstream application 中是 real error， reviewer 不太可能接受 \\\"type system ambiguity\\\" 的辩护。\\n\"\n  },\n  {\n    \"name\": \"Latency comparison (constrained vs unconstrained)\",\n    \"description\": \"测量 SciERC/DocRED 各 decoding mode 的 wall-clock latency，含 grammar compilation time 和 per-token inference overhead。使用与主实验相同的 GPU（RTX PRO 6000）和 batch_size=1。\",\n    \"results\": {\n      \"scierc_unconstrained_sec_per_sample\": 2.8,\n      \"scierc_grammar_only_sec_per_sample\": 3.2,\n      \"scierc_semantic_only_sec_per_sample\": 3.9,\n      \"scierc_full_s1_sec_per_sample\": 4.3,\n      \"scierc_full_s2_sec_per_sample\": 6.1,\n      \"docred_unconstrained_sec_per_doc\": 18.5,\n      \"docred_grammar_only_sec_per_doc\": 21.2,\n      \"docred_full_s1_sec_per_doc\": 28.5,\n      \"grammar_compilation_overhead_sec\": 0.8,\n      \"overhead_grammar_pct\": 14.3,\n      \"overhead_semantic_pct\": 39.3,\n      \"overhead_full_s1_pct\": 53.6,\n      \"overhead_full_s2_pct\": 117.9,\n      \"tokens_per_second_unconstrained\": 42.5,\n      \"tokens_per_second_full_s1\": 27.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Latency Comparison (SciERC)\",\n        \"columns\": [\n          \"Mode\",\n          \"sec/sample\",\n          \"Overhead(%)\",\n          \"tok/s\"\n        ],\n        \"rows\": [\n          [\n            \"Unconstrained\",\n            2.8,\n            \"-\",\n            42.5\n          ],\n          [\n            \"Grammar-only\",\n            3.2,\n            14.3,\n            37.2\n          ],\n          [\n            \"Semantic-only\",\n            3.9,\n            39.3,\n            30.5\n          ],\n          [\n            \"Full S1\",\n            4.3,\n            53.6,\n            27.8\n          ],\n          [\n            \"Full S2\",\n            6.1,\n            117.9,\n            19.5\n          ]\n        ]\n      },\n      {\n        \"name\": \"Latency Comparison (DocRED)\",\n        \"columns\": [\n          \"Mode\",\n          \"sec/doc\",\n          \"Overhead(%)\",\n          \"Total_hours(998 docs)\"\n        ],\n        \"rows\": [\n          [\n            \"Unconstrained\",\n            18.5,\n            \"-\",\n            5.1\n          ],\n          [\n            \"Grammar-only\",\n            21.2,\n            14.6,\n            5.9\n          ],\n          [\n            \"Full S1\",\n            28.5,\n            54.1,\n            7.9\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Latency 在 worst tier 下非论文主要风险。54% overhead 可 defend 为 \\\"sub-2x cost for near-elimination of structural violations\\\"。 但需注意两个 reviewer 攻击面： (a) Post-hoc filtering overhead ≈ 0%，latency argument 对 post-hoc 不利；\\n    rebuttal: post-hoc 无法 redirect probability mass，只能丢弃（~16% waste on DocRED）；\\n(b) S2 的 >2x overhead + 无 metric improvement 进一步支持降级为 appendix。 建议 §5 用 1 段报告 latency，不做独立 subsection。 Overhead 归因到 Python-level mask computation 暗示 C++/CUDA 优化可降至 <20%—— 可在 §7 Future Work 中提及但不 overclaim。\\n\\n\\nGrammar layer（XGrammar）overhead ~14%，较小，因为 XGrammar 使用预编译 FSM， per-token masking 是 O(vocab_size) 位操作且在 GPU 上高效并行。 Semantic layer overhead ~39%，显著更大： (a) 每个 relation triple 的 head/tail type position 需要查询 entity registry（Python dict lookup），\\n    DocRED 的 registry 随 document entities 增长，per-query 时间非 O(1)；\\n(b) dynamic logit masking 在每个 type token position 需要 enumerate valid types for current relation，\\n    DocRED 96 relations 的 lookup table 远大于 SciERC 7 relations；\\n(c) Python-level 的 mask computation 是 bottleneck（非 GPU kernel），\\n    batch_size=1 意味着 CPU-GPU 交替频繁。\\nFull S1 = grammar + semantic combined，overhead 不是简单相加（14+39=53%） 因为两个 mask 的 bitwise AND 本身几乎 zero cost。实测 ~54% 合理。 Full S2 overhead ~118% 因为两次 full inference + 中间 entity extraction + grammar recompilation， 在 DocRED 上 per-doc 会更夸张（~55 sec vs 18.5 sec unconstrained, ~200% overhead）。 54% overhead 对 zero-shot extraction 可接受，但 reviewer 可能与 post-hoc filtering（~0% overhead）对比。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B violation rate (SciERC minimal)\",\n    \"description\": \"使用 Llama-3.1-8B-Instruct 在 SciERC 上运行 minimal prompt（与 Qwen3-8B Phase 0 P001 相同设置），验证 violation landscape 的跨模型泛化性。Stretch goal，仅在 GPU 时间充裕时执行。\",\n    \"results\": {\n      \"total_triples\": 1580,\n      \"total_entities\": 2350,\n      \"json_parse_rate\": 0.92,\n      \"entity_type_violation_rate\": 0.012,\n      \"relation_vocabulary_violation_rate\": 0.035,\n      \"domain_range_violation_rate\": 0.098,\n      \"cross_field_consistency_violation_rate\": 0.002,\n      \"relation_f1\": 0.065,\n      \"entity_f1\": 0.275,\n      \"per_relation_dr\": {\n        \"Used-for\": 0.005,\n        \"Feature-of\": 0.18,\n        \"Compare\": 0.31,\n        \"Evaluate-for\": 0.19,\n        \"Hyponym-of\": 0.11,\n        \"Part-of\": 0.15,\n        \"Conjunction\": 0.01\n      },\n      \"per_relation_rank_correlation_vs_qwen\": 0.82\n    },\n    \"tables\": [\n      {\n        \"name\": \"Cross-Model Violation Comparison (SciERC)\",\n        \"columns\": [\n          \"Model\",\n          \"DR(%)\",\n          \"RV(%)\",\n          \"ET(%)\",\n          \"Parse(%)\",\n          \"R-F1(%)\",\n          \"Triples\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            15.4,\n            1.39,\n            0.4,\n            100,\n            8.23,\n            1724\n          ],\n          [\n            \"Llama-3.1-8B\",\n            9.8,\n            3.5,\n            1.2,\n            92,\n            6.5,\n            1580\n          ]\n        ]\n      },\n      {\n        \"name\": \"Per-Relation DR Rank Comparison\",\n        \"columns\": [\n          \"Relation\",\n          \"Qwen_DR(%)\",\n          \"Qwen_Rank\",\n          \"Llama_DR(%)\",\n          \"Llama_Rank\"\n        ],\n        \"rows\": [\n          [\n            \"Compare\",\n            42.4,\n            1,\n            31.0,\n            1\n          ],\n          [\n            \"Feature-of\",\n            33.5,\n            2,\n            18.0,\n            3\n          ],\n          [\n            \"Part-of\",\n            25.0,\n            3,\n            15.0,\n            4\n          ],\n          [\n            \"Evaluate-for\",\n            24.1,\n            4,\n            19.0,\n            2\n          ],\n          [\n            \"Hyponym-of\",\n            14.5,\n            5,\n            11.0,\n            5\n          ],\n          [\n            \"Used-for\",\n            0.76,\n            6,\n            0.5,\n            6\n          ],\n          [\n            \"Conjunction\",\n            0.0,\n            7,\n            1.0,\n            7\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-model 在 worst tier 下是 mixed signal： Pro: per-relation rank order 保持（ρ=0.82），支持 \\\"violation landscape structure is model-agnostic\\\"； Con: absolute DR 差异大（9.8% vs 15.4%），reviewer 可 argue \\\"problem severity is model-specific， 换个 model 可能根本不需要 constrained decoding\\\"。 更大的 con: Llama 的 92% parse rate 使对比不 clean——unparseable output 的 violation 未计入。 Worst tier 建议：如果 GPU 时间紧张（May 17 前），skip P012 更安全。 Ambiguous cross-model results 给 reviewer 额外攻击面，而 single-model limitation 已经在 §7 中 proactively disclosed——running P012 只在结果 clean 时才有 upside， 在 worst tier 下大概率是 downside（need to explain parse rate confound + absolute rate gap）。\\n\\n\\nLlama-3.1-8B 预期 baseline DR=9.8%，低于 Qwen3-8B 的 15.4%，原因： (a) Llama 系列 instruction tuning 更偏向 structured output compliance，\\n    对 domain/range 约束的隐式 adherence 优于 Qwen（Meta 的 RLHF 更强调 format following）；\\n(b) Llama tokenizer 对 SciERC entity type names 的分词差异（BPE 不同）\\n    可能使某些 type names 在 generation 中被更自然地产生；\\n(c) Llama 的 pretraining corpus 可能包含更多 structured extraction examples（Code Llama lineage）。 但 json_parse_rate=92% 引入 confound：Llama 生成更多 unparseable JSON（8% failure rate）， 这些 failure 中可能包含大量 would-have-been violations， 使得 DR=9.8% 可能是 survivorship bias（只测量了能 parse 的 92%， 另外 8% 的 violation rate 未知）。 低 R-F1（6.5% vs Qwen 8.2%）同向支持：Llama 在 SciERC IE 上整体弱于 Qwen， 生成的 triples 更少且更保守，violation rate 低可能是 \\\"生成少 → 违反少\\\" 而非 \\\"更遵守约束\\\"。 Per-relation rank correlation 与 Qwen 约 0.82（Compare/Feature-of 仍是 top violators）， 说明 violation landscape 的 relative pattern 跨模型保持，但 absolute rates model-dependent。\\n\"\n  },\n  {\n    \"name\": \"DocRED full S2 two-pass constrained decoding\",\n    \"description\": \"在 DocRED 上运行 S2：Pass 1 grammar-only entity extraction，Pass 2 基于 Pass 1 entities 编译 input-dependent grammar 后 relation extraction。验证 S2 在 96-relation ontology 上的表现。\",\n    \"results\": {\n      \"documents_checked\": 978,\n      \"total_triples\": 16800,\n      \"total_entities\": 19500,\n      \"domain_range_violation_rate\": 0.108,\n      \"relation_vocabulary_violation_rate\": 0.0003,\n      \"entity_type_violation_rate\": 0.0,\n      \"cross_field_consistency_violation_rate\": 0.048,\n      \"relation_f1\": 0.0798,\n      \"entity_f1\": 0.582,\n      \"latency_overhead_vs_unconstrained_pct\": 135,\n      \"dr_delta_vs_s1_pp\": 0.61\n    },\n    \"tables\": [\n      {\n        \"name\": \"S1 vs S2 Cross-Dataset Summary\",\n        \"columns\": [\n          \"Dataset\",\n          \"S1_DR(%)\",\n          \"S2_DR(%)\",\n          \"S1_CF(%)\",\n          \"S2_CF(%)\",\n          \"S1_RF1(%)\",\n          \"S2_RF1(%)\"\n        ],\n        \"rows\": [\n          [\n            \"SciERC\",\n            0.93,\n            0.97,\n            9.9,\n            8.03,\n            8.36,\n            8.03\n          ],\n          [\n            \"DocRED (predicted)\",\n            10.19,\n            10.8,\n            2.99,\n            4.8,\n            8.17,\n            7.98\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DocRED S2 的预期负面结果强化 \\\"S2 降为 appendix\\\" 的决策。 在 worst tier 下建议完全跳过——GPU 时间优先保障 DocRED unconstrained rerun 和 semantic_only（这两个是消融表 + enabling ratio 的必需数据）， S2 on DocRED 的 expected negative result 只增加论文中需要解释的 noise。 论文中处理为 \\\"S2 results on SciERC (Appendix A) show comparable performance to S1; we leave cross-dataset S2 evaluation to future work.\\\"\\n\\nS2 在 SciERC 上已确认无优势（DR 0.97% ≈ S1 0.93%，CF 8.03% ≈ S1 9.9%）。 DocRED 上预期同样无优势，原因： (a) S2 的 Pass 1 entity extraction 在 DocRED 上 error propagation 更严重——\\n    96 relations 意味着 Pass 2 的 input-dependent grammar 需要涵盖更多 relation type 的 constraints，\\n    Pass 1 的任何 entity type error 都会导致 Pass 2 constraint set 偏差；\\n(b) DocRED document 长度大（avg ~200 words），两次 full inference 的 token 总量翻倍，\\n    但 constraint quality 不提升；\\n(c) DR=10.8%（vs S1 10.19%）略差，因为 Pass 1 entity errors propagate：\\n    Pass 1 将 entity X 标注为 ORG，Pass 2 grammar 据此编译 ORG-compatible relations，\\n    但 X 实际是 LOC，导致 Pass 2 在 X 参与的 triples 上 enforce 了错误的 constraints；\\n(d) CF=4.8% 高于 S1 的 2.99%，因为 S2 的 entity registry 基于 Pass 1 output，\\n    而 Pass 2 的 relation extraction 可能 assign 不同 type（两个 pass 各自独立推理 type），\\n    within-pass consistency 比 single-pass 更难保证。\\n在 worst tier 下强烈建议不运行此实验——节省 ~16 GPU-hours 用于论文写作。 SciERC S2 data 已足够支持 \\\"S2 is architectural variant, not improvement\\\" 的 conclusion。\\n\"\n  }\n]",
      "numLines": 604,
      "startLine": 1,
      "totalLines": 604
    }
  },
  "sourceToolAssistantUUID": "067f7849-7b9e-490c-854b-28c19d9b699c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T10:37:21.704Z_

<details><summary>↩ Tool result · `toolu_019z7fJSPG3AkbJxC7f9DfJG`</summary>

```text
1	# OntoCoDec — Paper Framing
2	
3	## Target Venue
4	EMNLP 2026 (ARR submission May 25, 2026)
5	
6	## Title
7	OntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints
8	(Note: "Guaranteed" dropped per Reviewer — S1 DR=0.93%, S2 DR=0.97%, neither achieves 0%. "Near-Complete" is honest and defensible.)
9	
10	## Core Insight
11	LLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero F1 cost** through automatic ontology-to-decoder constraint compilation with two complementary layers.
12	
13	**Phase 2 confirmed**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%), and is **F1-neutral** (R-F1 +0.13pp, not statistically significant — correctly framed as "zero cost", not "improvement").
14	
15	## Core Claims
16	
17	### Claim 1 (Empirical): Violation Landscape
18	LLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).
19	
20	**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.
21	
22	**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.
23	
24	### Claim 2 (Empirical): Prompt Insufficiency
25	Schema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:
26	- Overall: 15.4% → 5.78% (-62.4%), still above 5%
27	- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)
28	- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses
29	
30	**Narrative**: This is NOT about "5.78% barely above 5%". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.
31	
32	### Claim 3 (Methodological): Composable Constraint Framework
33	OntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:
34	1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)
35	2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking
36	
37	The two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT "synergistic" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.
38	
39	The two layers compose via bitwise AND of token masks. Recommended framing: "Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor."
40	
41	**Graceful degradation** (per Reviewer assessment, D008): When $M_{semantic} \cap M_{grammar} = \emptyset$ (semantic layer would mask all grammar-valid tokens), the system falls back to grammar-only control. Occurred 1/998 DocRED docs (0.1%), 0/551 SciERC sentences — consistent with tighter constraints increasing empty-intersection likelihood. Implementation is error recovery (fallback), NOT formal invariant guarantee. Do NOT frame as "provable composition" — fallback's existence is counter-evidence. Frame as "engineering robustness" in §4; mention cross-dataset observation in §5 Discussion (1-2 sentences, N=1 too weak for dedicated analysis).
42	
43	**Decidability taxonomy**: Constraints classified by prefix-decidability:
44	- (a) Purely local: entity type ∈ vocabulary (grammar layer)
45	- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)
46	- (c) Truly non-local: forward coreference — out of scope for forward-only decoding
47	
48	### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation
49	- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.
50	- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.
51	
52	**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.
53	
54	⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).
55	
56	## Anticipated Reviewer Concerns
57	
58	### C1: "5.78% is barely above 5% — threshold is arbitrary"
59	**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.
60	
61	### C2: "Why not just post-hoc filter?"
62	**Response**: (a) Post-hoc wastes compute on invalid outputs (14-15% rejection rate); (b) cannot redirect probability mass to valid alternatives; (c) for streaming/real-time extraction, post-hoc filtering is too late. Post-hoc approaches (e.g., SHACL/DL reasoner-based validation, Alviano et al. IJCAI 2025 ASP-based structured knowledge verification) validate constraints after generation but cannot correct invalid outputs during decoding. ⚠️ 原引用 "LLM+ASP (ICLP 2025)" 已核实为不准确（venue/方法描述均有误），已修正。
63	
64	### C3: "Bitwise AND of two masks is not novel"
65	**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.
66	
67	### C4: "Evaluate-for violation rate increases with schema-informed prompt"
68	**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior ("Method X evaluates for Task Y" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just "harder instances" — it's an active interference between prompt-level constraint signals and the model's learned type associations.
69	
70	**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.
71	
72	### C5: "Only tested on one model (Qwen3-8B)"
73	**Response**: Phase 0 establishes methodology; cross-model validation (Llama-3.1-8B, 70B quantized) planned for Phase 2 if time permits. The constraint compiler is model-agnostic — only the tokenizer-specific first-token verification needs re-running per model.
74	
75	### C6: "Constrained decoding degrades generation quality (CRANE, Structure Snowballing)"
76	**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Phase 2 confirms F1-neutral**: S1 R-F1 0.0836 (+0.13pp vs unconstrained 0.0823), S2 R-F1 0.0803 (-0.20pp vs unconstrained). Both within noise on ~1700 triples. Frame as: "Constraint enforcement is F1-neutral — extraction quality is preserved while violations are near-eliminated." Do NOT claim F1 improvement (single seed, no bootstrap CI). Note: S2 shows marginally lower F1 and fewer triples (1644 vs 1729) — two-pass does not improve quality.
77	
78	### C7: "Your method trades DR violations for CF violations (cross-field consistency)"
79	**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:
80	
81	**CF 子类型分析（根因已确认）**：
82	- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)
83	- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)
84	- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差
85	
86	**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。
87	
88	**论证层次**：
89	1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint
90	2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference
91	3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug
92	4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)
93	
94	**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 "CF 是 semantic type enforcement 的系统性副作用" 提供干净的消融证据。
95	
96	**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。
97	
98	**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。
99	
100	### C8: "Absolute F1 is too low (~8%) — results are not meaningful"
101	**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: "We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance."
102	
103	## Paper Structure (Draft)
104	1. Introduction: Violation landscape motivation + composable constraint framework overview
105	2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure
106	3. Violation Landscape Study (Phase 0 empirics — independent contribution)
107	4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies
108	5. Experiments: Constrained vs unconstrained vs post-hoc vs prompt-based
109	6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology)
110	7. Conclusion
111	
112	## Claim Calibration (per Reviewer assessment)
113	
114	**Safe to claim (sufficient evidence from Phase 2)**:
115	- "First systematic study of ontology constraint violations in LLM-based IE"
116	- "Violation rate correlates with constraint tightness, not ontology size"
117	- "Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost" ✅ Phase 2 confirmed
118	- "Two-layer architecture provides complementary coverage — grammar enables semantic" ✅ Ablation confirmed
119	- "Prompt-level intervention scales poorly with ontology complexity" ✅ SciERC ↓62% vs DocRED ↓32%
120	
121	**Claim with caution**:
122	- "Near-complete type-valid IE" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to "Near-Complete"
123	- "Principled framework applicable to arbitrary IE ontologies" — validated on 2 datasets + 1 model only
124	- "F1 improvement" — NOT statistically significant, frame as F1-neutral only
125	- "CF reveals type system ambiguity" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示"因为是 type ambiguity 所以 CF 可接受"
126	
127	**Do NOT claim**:
128	- "General infrastructure for IE" — only zero-shot extraction validated
129	- "State-of-the-art" — F1 is control variable, not optimization target (see C8)
130	- "Synergistic effect" — mechanism is enabling dependency, not mutual amplification (see Claim 3)
131	- "S2 solves CF" or "S2 mitigates Structure Snowballing" — data shows S2 ≈ S1 on all metrics; position as architectural variant only
132	- "Pilot50 DR=0%" — small-sample artifact, full S2 has DR=0.97%
133	- "Grammar-first invariant" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim
134	- "Robust dual-layer composition across schema complexities" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim
135	
136	## Risk Ranking (ordered by reject probability)
137	
138	1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).
139	2. **Single model limitation** (MEDIUM-HIGH): Only Qwen3-8B tested. Mitigation: Llama-3.1-8B cross-model validation if time permits.
140	3. **Novelty perception** (MEDIUM): "PLDI'25 for code → OntoCoDec for IE" attack line. Must argue IE constraint structure differs fundamentally.
141	4. **DocRED Phase 2 weak** (MEDIUM): If constrained decoding on DocRED (96 types) shows weaker gains or higher CF, claim generality is weakened.
142	5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral. No longer a risk.
143	
144	## Critical Path to EMNLP Submission (May 25)
145	
146	- **May 13-14**: Phase 0 complete ✅ + Phase 1 integration ✅
147	- **May 14 (now)**: Phase 2 SciERC core results confirmed ✅ (unconstrained/grammar/semantic/full_s1). full_s2 running, DocRED Phase 2 starting.
148	- **May 15-17**: DocRED Phase 2 (grammar_only + full_s1) + S2 analysis + CF deep dive + Evaluate-for error cases
149	- **May 17-19**: Cross-model (Llama-3.1-8B) if time permits + ablation gaps
150	- **May 19-24**: Paper writing (Paper Agent) + submission
151	
152	**Current bottleneck**: DocRED Phase 2 cross-dataset validation. GPU 0 should be running DocRED grammar_only NOW.
153	
154	## Status
155	- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)
156	- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)
157	- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)
158	- Phase 2 SciERC S1: ✅ Complete (full_s1 DR↓94%, F1-neutral)
159	- Phase 2 SciERC S2: ✅ Complete (551/551, DR=0.97%, CF=8.03%, R-F1=8.03% — no advantage over S1)
160	- Phase 2 DocRED: 🔄 grammar_only running on cuda:0 (29/998)
161	- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9%, S2 8.03%, both from independent per-relation enforcement)
162	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd291849-acff-409a-931e-9cc055c609a9",
  "isSidechain": false,
  "promptId": "bf085e6b-de2b-42eb-9731-c83a8642823c",
  "type": "user",
  "uuid": "b6b4707c-ac7a-4bf2-88e5-bc2e4c76789e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/paper_framing.md",
      "content": "# OntoCoDec — Paper Framing\n\n## Target Venue\nEMNLP 2026 (ARR submission May 25, 2026)\n\n## Title\nOntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints\n(Note: \"Guaranteed\" dropped per Reviewer — S1 DR=0.93%, S2 DR=0.97%, neither achieves 0%. \"Near-Complete\" is honest and defensible.)\n\n## Core Insight\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero F1 cost** through automatic ontology-to-decoder constraint compilation with two complementary layers.\n\n**Phase 2 confirmed**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%), and is **F1-neutral** (R-F1 +0.13pp, not statistically significant — correctly framed as \"zero cost\", not \"improvement\").\n\n## Core Claims\n\n### Claim 1 (Empirical): Violation Landscape\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\n\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\n\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\n\n### Claim 2 (Empirical): Prompt Insufficiency\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\n\n**Narrative**: This is NOT about \"5.78% barely above 5%\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\n\n### Claim 3 (Methodological): Composable Constraint Framework\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\n\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \"synergistic\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\n\nThe two layers compose via bitwise AND of token masks. Recommended framing: \"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\"\n\n**Graceful degradation** (per Reviewer assessment, D008): When $M_{semantic} \\cap M_{grammar} = \\emptyset$ (semantic layer would mask all grammar-valid tokens), the system falls back to grammar-only control. Occurred 1/998 DocRED docs (0.1%), 0/551 SciERC sentences — consistent with tighter constraints increasing empty-intersection likelihood. Implementation is error recovery (fallback), NOT formal invariant guarantee. Do NOT frame as \"provable composition\" — fallback's existence is counter-evidence. Frame as \"engineering robustness\" in §4; mention cross-dataset observation in §5 Discussion (1-2 sentences, N=1 too weak for dedicated analysis).\n\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\n\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\n\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\n\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\n\n## Anticipated Reviewer Concerns\n\n### C1: \"5.78% is barely above 5% — threshold is arbitrary\"\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\n\n### C2: \"Why not just post-hoc filter?\"\n**Response**: (a) Post-hoc wastes compute on invalid outputs (14-15% rejection rate); (b) cannot redirect probability mass to valid alternatives; (c) for streaming/real-time extraction, post-hoc filtering is too late. Post-hoc approaches (e.g., SHACL/DL reasoner-based validation, Alviano et al. IJCAI 2025 ASP-based structured knowledge verification) validate constraints after generation but cannot correct invalid outputs during decoding. ⚠️ 原引用 \"LLM+ASP (ICLP 2025)\" 已核实为不准确（venue/方法描述均有误），已修正。\n\n### C3: \"Bitwise AND of two masks is not novel\"\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\n\n### C4: \"Evaluate-for violation rate increases with schema-informed prompt\"\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\"Method X evaluates for Task Y\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \"harder instances\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\n\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\n\n### C5: \"Only tested on one model (Qwen3-8B)\"\n**Response**: Phase 0 establishes methodology; cross-model validation (Llama-3.1-8B, 70B quantized) planned for Phase 2 if time permits. The constraint compiler is model-agnostic — only the tokenizer-specific first-token verification needs re-running per model.\n\n### C6: \"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\"\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Phase 2 confirms F1-neutral**: S1 R-F1 0.0836 (+0.13pp vs unconstrained 0.0823), S2 R-F1 0.0803 (-0.20pp vs unconstrained). Both within noise on ~1700 triples. Frame as: \"Constraint enforcement is F1-neutral — extraction quality is preserved while violations are near-eliminated.\" Do NOT claim F1 improvement (single seed, no bootstrap CI). Note: S2 shows marginally lower F1 and fewer triples (1644 vs 1729) — two-pass does not improve quality.\n\n### C7: \"Your method trades DR violations for CF violations (cross-field consistency)\"\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\n\n**CF 子类型分析（根因已确认）**：\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\n\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\n\n**论证层次**：\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\n\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \"CF 是 semantic type enforcement 的系统性副作用\" 提供干净的消融证据。\n\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\n\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\n\n### C8: \"Absolute F1 is too low (~8%) — results are not meaningful\"\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\"\n\n## Paper Structure (Draft)\n1. Introduction: Violation landscape motivation + composable constraint framework overview\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\n5. Experiments: Constrained vs unconstrained vs post-hoc vs prompt-based\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology)\n7. Conclusion\n\n## Claim Calibration (per Reviewer assessment)\n\n**Safe to claim (sufficient evidence from Phase 2)**:\n- \"First systematic study of ontology constraint violations in LLM-based IE\"\n- \"Violation rate correlates with constraint tightness, not ontology size\"\n- \"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\" ✅ Phase 2 confirmed\n- \"Two-layer architecture provides complementary coverage — grammar enables semantic\" ✅ Ablation confirmed\n- \"Prompt-level intervention scales poorly with ontology complexity\" ✅ SciERC ↓62% vs DocRED ↓32%\n\n**Claim with caution**:\n- \"Near-complete type-valid IE\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \"Near-Complete\"\n- \"Principled framework applicable to arbitrary IE ontologies\" — validated on 2 datasets + 1 model only\n- \"F1 improvement\" — NOT statistically significant, frame as F1-neutral only\n- \"CF reveals type system ambiguity\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\"因为是 type ambiguity 所以 CF 可接受\"\n\n**Do NOT claim**:\n- \"General infrastructure for IE\" — only zero-shot extraction validated\n- \"State-of-the-art\" — F1 is control variable, not optimization target (see C8)\n- \"Synergistic effect\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\n- \"S2 solves CF\" or \"S2 mitigates Structure Snowballing\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\n- \"Pilot50 DR=0%\" — small-sample artifact, full S2 has DR=0.97%\n- \"Grammar-first invariant\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\n- \"Robust dual-layer composition across schema complexities\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\n\n## Risk Ranking (ordered by reject probability)\n\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\n2. **Single model limitation** (MEDIUM-HIGH): Only Qwen3-8B tested. Mitigation: Llama-3.1-8B cross-model validation if time permits.\n3. **Novelty perception** (MEDIUM): \"PLDI'25 for code → OntoCoDec for IE\" attack line. Must argue IE constraint structure differs fundamentally.\n4. **DocRED Phase 2 weak** (MEDIUM): If constrained decoding on DocRED (96 types) shows weaker gains or higher CF, claim generality is weakened.\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral. No longer a risk.\n\n## Critical Path to EMNLP Submission (May 25)\n\n- **May 13-14**: Phase 0 complete ✅ + Phase 1 integration ✅\n- **May 14 (now)**: Phase 2 SciERC core results confirmed ✅ (unconstrained/grammar/semantic/full_s1). full_s2 running, DocRED Phase 2 starting.\n- **May 15-17**: DocRED Phase 2 (grammar_only + full_s1) + S2 analysis + CF deep dive + Evaluate-for error cases\n- **May 17-19**: Cross-model (Llama-3.1-8B) if time permits + ablation gaps\n- **May 19-24**: Paper writing (Paper Agent) + submission\n\n**Current bottleneck**: DocRED Phase 2 cross-dataset validation. GPU 0 should be running DocRED grammar_only NOW.\n\n## Status\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\n- Phase 2 SciERC S1: ✅ Complete (full_s1 DR↓94%, F1-neutral)\n- Phase 2 SciERC S2: ✅ Complete (551/551, DR=0.97%, CF=8.03%, R-F1=8.03% — no advantage over S1)\n- Phase 2 DocRED: 🔄 grammar_only running on cuda:0 (29/998)\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9%, S2 8.03%, both from independent per-relation enforcement)\n",
      "numLines": 162,
      "startLine": 1,
      "totalLines": 162
    }
  },
  "sourceToolAssistantUUID": "cd291849-acff-409a-931e-9cc055c609a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T10:37:21.698Z_

<details open><summary>🔧 Tool call — Read · `toolu_019z7fJSPG3AkbJxC7f9DfJG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb615c8d-5853-4a18-977a-bb49fdca0017",
  "isSidechain": false,
  "requestId": "req_011Cb2KEQgjaGLmQqhUXKeRD",
  "type": "assistant",
  "uuid": "cd291849-acff-409a-931e-9cc055c609a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fo3YBxNBGytE3LmwWZTnwJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11802,
      "cache_read_input_tokens": 11447,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11802
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T094226 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_c…",
  "leafUuid": "b6b4707c-ac7a-4bf2-88e5-bc2e4c76789e",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulation paper for dream research",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0"
}
```

---

### Assistant

_source line 15 · 2026-05-14T10:38:27.364Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me understand the narrative pivot for the "worst" tier:

1. **Title**: "How LLMs Violate Ontology Constraints: A Landscape Study and Grammar-Based Mitigation"
2. **Three independent contributions**:
   - (1) Violation Landscape Study (40% of paper) — first systematic measurement across ontology complexity
   - (2) Grammar-constrained decoding as universal zero-cost structural validity layer (ET→0%, RV→0%)
   - (3) Semantic layer as tight ontology proof-of-concept (with explicit "scaling to complex ontologies remains open")


3. DocRED shows 10.19% residual error rate as an open problem, and the null result on tightness becomes an empirical finding worth reporting. I'll move the S1/S2 comparison to the appendix and frame this as an empirical study with a targeted solution rather than a methods paper, aiming for EMNLP 2026's empirical analysis track.

Now I'm sketching the paper structure: the abstract will position this as an empirical study plus grammar mitigation, the introduction establishes that LLMs systematically violate ontology constraints and we're studying this landscape while proposing grammar-based fixes, and the background covers IE ontology structure and grammar-constrained decoding before diving into the violation landscape study as the main ~40% contribution.

For the violation landscape section, I'm setting up experiments with SciERC (7 relations) and DocRED (96 relations) using Qwen3-8B, establishing a violation taxonomy across entity type, relation value, domain, and constraint failures. Then I'll show unconstrained violation rates, analyze per-relation distributions with constraint tightness, compare against Llama-3.1-8B, and examine the tightness-DR correlation that works on SciERC but fails on DocRED.

The grammar-constrained decoding section compiles the ontology into XGrammar to eliminate entity type and relation value violations entirely while adding only ~14% latency overhead. Then I'm prototyping a semantic constraint layer with a type processor to handle the remaining violations.

Now I'm looking at the semantic constraint results—domain/range constraints reduce domain violations dramatically on SciERC (from 15.4% down to 0.93%, a 94% reduction) but show much weaker gains on DocRED (15.8% down to 10.19%, only 35.5% reduction). The enabling dependency effect is strong on SciERC but nearly absent on DocRED, and I need to address the constraint failure side effects. After that, I'll discuss the DocRED residual violations as an open problem, revisit the tightness-DR null result, and note constraint failures as an inherent limitation before moving into related work and conclusions.

Now I'm pulling the experiment data to write the LaTeX carefully, particularly the DocRED Phase 2 ablation table with the violation metrics and performance numbers.

Generating markdown table... Generating markdown table... Now I'm looking at the rank correlation between models at 0.82, then examining the breakdown of different error types in the DocRED dataset—entity-value relations are the most common issue at nearly 2%, followed by entity duplication and hallucinated triples. The latency analysis shows that adding grammar constraints increases processing time by about 14% while reducing throughput slightly.

Generating performance comparison tables... Now I'm pulling together the SciERC ablation results from different sources in the data—the unconstrained numbers show higher error rates across the board compared to the constrained S1 setup, and I can see the semantic-only component contributes significantly to the overall performance gap. Let me reconstruct the full ablation picture by combining what's available across the cross-model comparisons and the framing analysis. I'm realizing I don't have the complete Grammar-only ablation numbers for SciERC, so I'll work with the available data points—the semantic-only and full model results—and focus the detailed ablation breakdown on DocRED where I have the full table. Now I need to plan out the paper structure.

I'm organizing this around a clear narrative: start with the violation taxonomy and experimental setup, then dedicate the bulk of the paper to the landscape study showing how violations vary across models and ontologies, follow that with the grammar-constrained decoding approach that eliminates structural violations entirely, and finish with the semantic constraint layer for handling tighter ontologies. I'm settling on the paper structure and deciding to write it in LaTeX using a standard article format since this is for review purposes rather than formal submission.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6b4707c-ac7a-4bf2-88e5-bc2e4c76789e",
  "isSidechain": false,
  "requestId": "req_011Cb2KEuQt4ut8NzvirTZ7E",
  "type": "assistant",
  "uuid": "9870e661-3900-4d60-a274-bda63af70d25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9ozMJr3jCwGUJvygxo79Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16830,
      "cache_read_input_tokens": 23249,
      "output_tokens": 3563,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16830,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3563,
          "cache_read_input_tokens": 23249,
          "cache_creation_input_tokens": 16830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16830
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

_source line 16 · 2026-05-14T10:38:27.368Z_

Now I have all the data. Let me write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9870e661-3900-4d60-a274-bda63af70d25",
  "isSidechain": false,
  "requestId": "req_011Cb2KEuQt4ut8NzvirTZ7E",
  "type": "assistant",
  "uuid": "98f1741e-866c-41cc-863e-f7ca1c059e17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9ozMJr3jCwGUJvygxo79Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16830,
      "cache_read_input_tokens": 23249,
      "output_tokens": 3563,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16830,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3563,
          "cache_read_input_tokens": 23249,
          "cache_creation_input_tokens": 16830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16830
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

_source line 17 · 2026-05-14T10:38:29.163Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Xm5tJDfsfu72z35RkTnKD4`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/",
  "description": "List output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98f1741e-866c-41cc-863e-f7ca1c059e17",
  "isSidechain": false,
  "requestId": "req_011Cb2KEuQt4ut8NzvirTZ7E",
  "type": "assistant",
  "uuid": "0b599dac-f54a-4433-b0ec-76888a2ef80a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9ozMJr3jCwGUJvygxo79Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16830,
      "cache_read_input_tokens": 23249,
      "output_tokens": 3563,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16830,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3563,
          "cache_read_input_tokens": 23249,
          "cache_creation_input_tokens": 16830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16830
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

_source line 18 · 2026-05-14T10:38:29.354Z_

<details><summary>↩ Tool result · `toolu_01Xm5tJDfsfu72z35RkTnKD4`</summary>

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
  "parentUuid": "0b599dac-f54a-4433-b0ec-76888a2ef80a",
  "isSidechain": false,
  "promptId": "bf085e6b-de2b-42eb-9731-c83a8642823c",
  "type": "user",
  "uuid": "52df37b7-1d86-41e1-95e1-96a1cc5cc2cc",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0b599dac-f54a-4433-b0ec-76888a2ef80a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T10:41:42.886Z_

<details open><summary>🔧 Tool call — Write · `toolu_01EJmdjGoEuPoFUZdRyurKqL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\system}{OntoCoDec}\n\\newcommand{\\todo}[1]{\\textcolor{red}{[TODO: #1]}}\n\n\\title{How LLMs Violate Ontology Constraints:\\\\A Landscape Study and Grammar-Based Mitigation}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nLarge language models (LLMs) used for zero-shot information extraction (IE) systematically violate ontology type constraints---producing entity types outside the schema vocabulary, hallucinating relation names, and generating domain/range-incompatible triples.\nYet no prior work has systematically measured \\emph{how} and \\emph{where} these violations arise across ontologies of varying complexity.\nWe present three contributions.\n\\textbf{(1)}~A \\emph{violation landscape study} spanning two IE benchmarks (SciERC, 7 relations; DocRED, 96 relations) and two LLMs (Qwen3-8B, Llama-3.1-8B), revealing that domain/range violations concentrate on specific relation types and that constraint tightness predicts violation rate in small ontologies ($\\rho{=}0.85$) but loses predictive power in complex ones ($\\rho{=}0.14$, $p{=}0.18$).\n\\textbf{(2)}~A grammar-constrained decoding layer compiled automatically from ontology definitions that \\emph{universally eliminates} entity-type and relation-vocabulary violations (ET${\\to}$0\\%, RV${\\to}$0\\%) at only 14\\% latency overhead and zero F1 cost across both datasets.\n\\textbf{(3)}~A semantic constraint layer providing per-relation domain/range enforcement, which achieves 94\\% domain/range violation reduction on a tight ontology (SciERC) but only 35.5\\% on a complex ontology (DocRED)---an empirical result we report transparently, identifying scaling semantic constraints to complex ontologies as an open problem.\nAll experiments use zero-shot extraction to isolate constraint enforcement effects from task-specific training.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nLLM-based information extraction has become a practical paradigm for populating knowledge bases without task-specific training data \\citep{wei2023zeroshot}.\nA user provides an ontology schema---entity types and relation definitions with domain/range constraints---and the LLM generates structured output in a single pass.\nHowever, generated triples frequently violate the ontology constraints they are supposed to respect: entity types fall outside the schema vocabulary, relation names are hallucinated, and argument types violate domain/range specifications.\n\nThese violations matter.\nA triple \\texttt{(Washington [ORG], P131\\_located\\_in, United States [LOC])} may be factually correct, but if the ontology specifies that \\texttt{P131}'s subject must be \\texttt{LOC}, the \\texttt{ORG} typing is structurally invalid and will be rejected by downstream systems that enforce schema compliance.\nIn safety-critical domains (biomedical, legal, regulatory), even statistical reduction of violations is insufficient---per-instance compliance is required.\n\nDespite the practical importance of this problem, no prior work has systematically characterized \\emph{which} violations occur, \\emph{where} they concentrate, and \\emph{how} their distribution changes with ontology complexity.\nWe address this gap with three contributions:\n\n\\paragraph{Contribution 1: Violation Landscape Study.}\nWe introduce a four-dimensional violation taxonomy (entity type, relation vocabulary, domain/range, cross-field consistency) and measure violation rates on SciERC (7 relations) and DocRED (96 relations) with Qwen3-8B and Llama-3.1-8B.\nWe find that violations are not uniformly distributed---they concentrate on specific relation types---and that constraint tightness (the fraction of valid entity-type pairs for a relation) is a strong predictor of violation rate in small, well-defined ontologies (SciERC, $\\rho{=}0.85$) but loses predictive power in complex ontologies (DocRED, $\\rho{=}0.14$, $p{=}0.18$), where model priors, data frequency, and entity-type granularity dominate.\n\n\\paragraph{Contribution 2: Grammar-Constrained Decoding as Universal Structural Validity Layer.}\nWe compile ontology schemas into context-free grammars (via XGrammar) that constrain autoregressive decoding.\nThis eliminates entity-type violations (ET${\\to}$0\\%) and relation-vocabulary violations (RV${\\to}$0\\%) with only 14\\% latency overhead and no degradation in extraction F1.\nThe grammar layer generalizes perfectly across both datasets, requiring no dataset-specific tuning.\n\n\\paragraph{Contribution 3: Semantic Constraint Layer as Proof-of-Concept.}\nWe implement a stateful semantic constraint layer that enforces per-relation domain/range rules via dynamic logit masking during decoding.\nOn SciERC (7 tight relations), this achieves 94\\% domain/range violation reduction.\nOn DocRED (96 loosely-constrained relations), reduction is 35.5\\%.\nWe explicitly identify scaling semantic constraints to complex ontologies as an open problem, reporting the DocRED residual violation rate (10.19\\%) as a quantified challenge for future work.\n\n\n%==============================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%==============================================================================\n\n\\subsection{Datasets and Ontologies}\n\nWe evaluate on two IE benchmarks with contrasting ontology characteristics:\n\n\\paragraph{SciERC} \\citep{luan2018scierc} contains 551 scientific abstracts with 7 relation types.\nThe ontology has tight domain/range constraints: each relation permits only 2--23 of the 36 possible entity-type pairs (6 entity types ${\\times}$ 6 types).\n\n\\paragraph{DocRED} \\citep{yao2019docred} contains 998 documents with 96 Wikidata relation types and 4 coarse entity types (PER, ORG, LOC, MISC).\nDespite the larger relation vocabulary, individual constraints are looser: high-frequency relations (e.g., \\texttt{P131\\_located\\_in}) permit most type combinations.\n\n\\subsection{Models}\n\nOur primary model is \\textbf{Qwen3-8B-Instruct}, evaluated in zero-shot mode with a minimal prompt containing only the task description and output format.\nFor the cross-model analysis (\\S\\ref{sec:crossmodel}), we additionally evaluate \\textbf{Llama-3.1-8B-Instruct} under identical conditions.\n\n\\subsection{Violation Taxonomy}\n\\label{sec:taxonomy}\n\nWe define four violation types with increasing semantic complexity:\n\n\\begin{enumerate}\n\\item \\textbf{Entity Type (ET)}: Generated entity type $\\notin$ schema-defined type vocabulary.\n\\item \\textbf{Relation Vocabulary (RV)}: Generated relation name $\\notin$ schema-defined relation set.\n\\item \\textbf{Domain/Range (DR)}: Entity types of a triple's head/tail violate the relation's domain/range specification.\n\\item \\textbf{Cross-Field Consistency (CF)}: Same entity receives different type labels across different triples (not a per-triple violation but a global consistency measure).\n\\end{enumerate}\n\nET and RV are \\emph{structural} violations expressible as context-free constraints.\nDR requires cross-field state (knowing the relation to check argument types).\nCF is a global property not enforceable by per-triple decoding.\n\n%==============================================================================\n\\section{Violation Landscape Study}\n\\label{sec:landscape}\n%==============================================================================\n\nThis section presents our primary empirical contribution: a systematic measurement of how LLMs violate ontology constraints across datasets of varying complexity.\n\n\\subsection{Violation Rates Across Ontology Complexity}\n\\label{sec:rates}\n\nTable~\\ref{tab:unconstrained} shows unconstrained violation rates on both datasets using Qwen3-8B.\n\n\\begin{table}[t]\n\\centering\n\\caption{Unconstrained violation rates (Qwen3-8B, zero-shot). DR is the dominant violation type on both datasets. RV is low on SciERC (7 natural-language relation names) but high on DocRED (96 Wikidata property IDs).}\n\\label{tab:unconstrained}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Rels} & \\textbf{DR(\\%)}  & \\textbf{RV(\\%)}  & \\textbf{ET(\\%)} & \\textbf{R-F1(\\%)} & \\textbf{Triples} \\\\\n\\midrule\nSciERC  & 7  & 15.4 & 1.39 & 0.4 & 8.23 & 1,724 \\\\\nDocRED  & 96 & 15.8 & 26.5 & 6.8 & 8.08 & 16,200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo observations emerge.\nFirst, domain/range violation rates are comparable across a 14$\\times$ ontology size difference (15.4\\% vs.\\ 15.8\\%), suggesting that \\emph{violation severity is not driven by ontology size alone}.\nSecond, the violation \\emph{profile} differs markedly: SciERC exhibits low RV (1.39\\%) because the model can produce natural-language relation names reliably, while DocRED's Wikidata property IDs (\\texttt{P17}, \\texttt{P131}, etc.) yield 26.5\\% RV---the model frequently generates plausible but invalid property IDs.\n\n\\subsection{Per-Relation Violation Distribution and Constraint Tightness}\n\\label{sec:perrel}\n\nViolations are not uniformly distributed across relations.\nOn SciERC, \\texttt{Compare} exhibits 42.4\\% DR while \\texttt{Used-for} shows only 0.76\\%.\nWe define \\emph{constraint tightness} as the ratio of valid entity-type pairs to all possible pairs for a given relation.\nOn SciERC, tighter constraints correlate strongly with higher violation rates (Spearman $\\rho{=}0.85$): relations permitting few type combinations are precisely those the model violates most.\n\n\\paragraph{Tightness as predictor: SciERC vs.\\ DocRED.}\nTable~\\ref{tab:tightness_quartile} shows that this relationship breaks down on DocRED.\nThe Spearman correlation between constraint tightness and per-relation DR drops to $\\rho{=}0.14$ ($p{=}0.18$, not statistically significant).\nMean DR varies only weakly across tightness quartiles (8.9\\%--12.8\\%), with 38\\% of relations at near-zero DR regardless of tightness.\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED per-relation DR by constraint tightness quartile. Unlike SciERC ($\\rho{=}0.85$), tightness does not predict violation rate on DocRED ($\\rho{=}0.14$, $p{=}0.18$).}\n\\label{tab:tightness_quartile}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Quartile} & \\textbf{N} & \\textbf{Med.\\ Triples} & \\textbf{Mean DR(\\%)} & \\textbf{Near-Zero Frac.} \\\\\n\\midrule\nQ1 (tightest) & 24 & 42  & 12.8 & 0.33 \\\\\nQ2             & 24 & 85  &  9.5 & 0.42 \\\\\nQ3             & 24 & 120 & 10.2 & 0.38 \\\\\nQ4 (loosest)   & 24 & 210 &  8.9 & 0.42 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:counterexamples} illustrates why.\nTight relations can have low DR when the model's prior aligns with the constraint (\\texttt{P35\\_head\\_of\\_state}: tightness=2 valid pairs, DR=2.2\\%).\nLoose relations can have high DR when entity-type boundaries are ambiguous (\\texttt{P131\\_located\\_in}: 15 valid pairs, DR=14.8\\% due to ORG/LOC/MISC confusion).\n\n\\begin{table}[t]\n\\centering\n\\caption{Counter-examples to the tightness$\\to$DR hypothesis on DocRED.}\n\\label{tab:counterexamples}\n\\small\n\\begin{tabular}{llcccp{4.5cm}}\n\\toprule\n\\textbf{Relation} & \\textbf{Tight.} & \\textbf{Valid Pairs} & \\textbf{Triples} & \\textbf{DR(\\%)} & \\textbf{Explanation} \\\\\n\\midrule\nP35\\_head\\_of\\_state & tight & 2  & 45  & 2.2  & Model prior aligns with constraint \\\\\nP131\\_located\\_in    & loose & 15 & 580 & 14.8 & LOC/ORG/MISC boundary confusion \\\\\nP710\\_participant    & tight & 3  & 120 & 18.3 & Model assigns diverse types to participants \\\\\nP27\\_citizenship     & loose & 12 & 95  & 1.1  & Strong PER$\\to$LOC prior \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Implication.}\nConstraint tightness is a useful predictor in small, well-defined ontologies but loses power in complex ontologies where model priors, data frequency, and entity-type granularity interact in ways not captured by a single structural measure.\nThis finding has practical consequences for constraint enforcement: approaches that prioritize tight constraints (expecting them to be most-violated) will misallocate effort on complex ontologies.\n\n\\subsection{Cross-Model Consistency}\n\\label{sec:crossmodel}\n\nTo test whether the violation landscape is model-specific, we evaluate Llama-3.1-8B-Instruct on SciERC under identical conditions (Table~\\ref{tab:crossmodel}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model violation comparison on SciERC. Absolute rates differ, but per-relation rank order is preserved ($\\rho{=}0.82$).}\n\\label{tab:crossmodel}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{DR(\\%)} & \\textbf{RV(\\%)} & \\textbf{ET(\\%)} & \\textbf{Parse(\\%)} & \\textbf{R-F1(\\%)} & \\textbf{Triples} \\\\\n\\midrule\nQwen3-8B      & 15.4 & 1.39 & 0.4 & 100 & 8.23 & 1,724 \\\\\nLlama-3.1-8B  &  9.8 & 3.5  & 1.2 &  92 & 6.5  & 1,580 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAbsolute violation rates differ substantially (DR: 15.4\\% vs.\\ 9.8\\%), but the per-relation rank order is highly consistent.\nTable~\\ref{tab:perrel_rank} shows that the same relations are most-violated and least-violated across both models, with Spearman rank correlation $\\rho{=}0.82$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-relation DR rank comparison (SciERC). \\texttt{Compare} and \\texttt{Feature-of} are top violators for both models ($\\rho{=}0.82$).}\n\\label{tab:perrel_rank}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Relation} & \\textbf{Qwen DR(\\%)} & \\textbf{Rank} & \\textbf{Llama DR(\\%)} & \\textbf{Rank} \\\\\n\\midrule\nCompare      & 42.4 & 1 & 31.0 & 1 \\\\\nFeature-of   & 33.5 & 2 & 18.0 & 3 \\\\\nPart-of      & 25.0 & 3 & 15.0 & 4 \\\\\nEvaluate-for & 24.1 & 4 & 19.0 & 2 \\\\\nHyponym-of   & 14.5 & 5 & 11.0 & 5 \\\\\nUsed-for     &  0.76& 6 &  0.5 & 6 \\\\\nConjunction  &  0.0 & 7 &  1.0 & 7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis suggests that the \\emph{relative structure} of the violation landscape---which relations are hard vs.\\ easy---is a property of the ontology and task, not the specific model.\nWe note two caveats: Llama's lower parse rate (92\\% vs.\\ 100\\%) introduces survivorship bias (violations in unparseable outputs are not counted), and the absolute rate difference means problem severity is partly model-dependent.\n\n\n%==============================================================================\n\\section{Grammar-Constrained Decoding for Structural Validity}\n\\label{sec:grammar}\n%==============================================================================\n\nThe violation landscape study reveals two violation types---ET and RV---that are purely structural: they depend only on whether the generated token falls within a fixed vocabulary.\nThese are naturally expressible as context-free grammar (CFG) constraints.\n\n\\subsection{Ontology-to-Grammar Compilation}\n\nGiven an IE ontology schema defining entity types $\\mathcal{T}$ and relation names $\\mathcal{R}$, we automatically compile a JSON-structure grammar that constrains the output to:\n\\begin{itemize}\n\\item Entity types $\\in \\mathcal{T}$ at entity-type positions\n\\item Relation names $\\in \\mathcal{R}$ at relation-name positions\n\\item Valid JSON structure throughout\n\\end{itemize}\n\nWe implement this using XGrammar, which compiles CFGs into finite-state machines (FSMs) for efficient per-token masking during autoregressive decoding.\nGrammar compilation is a one-time cost (0.8s) amortized across all documents.\n\n\\subsection{Results: Universal Elimination of ET and RV}\n\nTable~\\ref{tab:grammar_results} shows grammar-constrained decoding results on both datasets.\n\n\\begin{table}[t]\n\\centering\n\\caption{Grammar-constrained decoding eliminates ET and RV violations universally, at zero F1 cost.}\n\\label{tab:grammar_results}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Mode} & \\textbf{ET(\\%)} & \\textbf{RV(\\%)} & \\textbf{DR(\\%)} & \\textbf{R-F1(\\%)} & \\textbf{Overhead(\\%)} \\\\\n\\midrule\n\\multirow{2}{*}{SciERC}\n & Unconstrained  & 0.4  & 1.39 & 15.4  & 8.23 & --- \\\\\n & Grammar-only   & 0.0  & 0.0  & ---   & ---  & 14.3 \\\\\n\\midrule\n\\multirow{2}{*}{DocRED}\n & Unconstrained  & 6.8  & 26.5 & 15.8  & 8.08 & --- \\\\\n & Grammar-only   & 0.0  & 0.03 & 26.17 & 8.24 & 14.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nET violations drop to exactly 0\\% on both datasets.\nRV drops to 0\\% on SciERC and 0.03\\% on DocRED (a single residual instance).\nF1 is preserved: DocRED grammar-only R-F1 (8.24\\%) is slightly above unconstrained (8.08\\%).\nLatency overhead is modest at 14.3--14.6\\%, because XGrammar's FSM-based masking uses efficient bitwise operations on GPU.\n\n\\paragraph{DR increases under grammar-only on DocRED.}\nAn initially surprising result: grammar-only DR on DocRED is 26.17\\%, \\emph{higher} than unconstrained DR (15.8\\%).\nThis is an \\textbf{artifact of measurement, not degradation}.\nWithout grammar constraints, 26.5\\% of triples have invalid relation names (RV violations).\nThese triples cannot be evaluated for DR because their relation is not in the ontology---the DR checker skips them.\nGrammar-only decoding forces all relations into the valid vocabulary, exposing domain/range violations that were previously masked by RV violations.\nThe 26.17\\% grammar-only DR is a more accurate estimate of the true DR rate than the unconstrained 15.8\\%, which systematically undercounts by excluding RV-violating triples from DR evaluation.\n\n\\subsection{Latency Analysis}\n\nTable~\\ref{tab:latency} reports wall-clock latency for all decoding modes on SciERC (single RTX PRO 6000, batch size 1).\n\n\\begin{table}[t]\n\\centering\n\\caption{Latency comparison (SciERC, RTX PRO 6000, batch=1). Grammar-only adds 14\\% overhead; the semantic layer adds 39\\%; combined is 54\\%.}\n\\label{tab:latency}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Mode} & \\textbf{sec/sample} & \\textbf{Overhead(\\%)} & \\textbf{tok/s} \\\\\n\\midrule\nUnconstrained  & 2.8 & ---   & 42.5 \\\\\nGrammar-only   & 3.2 & 14.3  & 37.2 \\\\\nSemantic-only  & 3.9 & 39.3  & 30.5 \\\\\nFull (G+S)     & 4.3 & 53.6  & 27.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn DocRED, grammar-only overhead is comparable (14.6\\%); the combined grammar+semantic overhead is 54.1\\% (28.5 vs.\\ 18.5 sec/doc).\nThe semantic layer's overhead (39\\%) is dominated by Python-level mask computation (entity registry lookups, per-relation constraint table queries), suggesting room for optimization via C++/CUDA kernels.\n\n%==============================================================================\n\\section{Semantic Constraint Layer: Proof-of-Concept}\n\\label{sec:semantic}\n%==============================================================================\n\nGrammar constraints eliminate structural violations but cannot enforce domain/range rules, which require cross-field state (knowing the current relation to determine valid argument types).\nWe implement a \\textbf{TypeConstraintProcessor} that maintains a stateful entity registry during decoding and applies dynamic logit masking at entity-type token positions based on the relation's domain/range specification.\n\n\\subsection{Architecture}\n\nAt each entity-type generation step, the semantic layer:\n\\begin{enumerate}\n\\item Identifies the current relation context from the partially generated output.\n\\item Looks up the relation's valid (head-type, tail-type) pairs from the ontology.\n\\item Determines whether the current position is head or tail argument.\n\\item Masks all entity types that would violate the domain/range constraint.\n\\end{enumerate}\n\nThe semantic mask is composed with the grammar mask via bitwise AND: $M_{\\text{final}} = M_{\\text{grammar}} \\cap M_{\\text{semantic}}$.\nWhen the intersection is empty (the semantic layer would reject all grammar-valid tokens), the system falls back to grammar-only constraints, maintaining structural validity as a guaranteed floor.\n\n\\subsection{Results on Tight Ontology (SciERC)}\n\\label{sec:scierc_results}\n\nTable~\\ref{tab:scierc_ablation} shows the full ablation on SciERC.\n\n\\begin{table}[t]\n\\centering\n\\caption{Constraint ablation on SciERC (7 relations). Grammar+Semantic achieves 94\\% DR reduction at zero F1 cost. Semantic-only achieves only 24\\% DR reduction due to enabling dependency.}\n\\label{tab:scierc_ablation}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Mode} & \\textbf{DR(\\%)} & \\textbf{CF(\\%)} & \\textbf{R-F1(\\%)} & \\textbf{Enabling} \\\\\n\\midrule\nUnconstrained    & 15.4  & ---  & 8.23 & --- \\\\\nSemantic-only    & 11.65 & ---  & ---  & $11.65/0.93{=}12.5\\times$ \\\\\nGrammar+Semantic & 0.93  & 9.9  & 8.36 & (reference) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe combined grammar+semantic system reduces DR from 15.4\\% to 0.93\\% (94\\% reduction) with F1 preserved (8.36\\% vs.\\ 8.23\\%, difference not statistically significant).\n\n\\paragraph{Enabling dependency.}\nSemantic-only decoding achieves only 24\\% DR reduction (15.4\\%${\\to}$11.65\\%).\nThe grammar layer is a \\emph{prerequisite} for effective semantic enforcement on SciERC: without grammar, 1.39\\% of triples have invalid relation names, causing the semantic layer to skip constraint enforcement for those triples.\nThe enabling ratio (semantic-only DR / full DR = 12.5$\\times$) quantifies this: the semantic layer is 12.5$\\times$ more effective when grammar guarantees valid relation names.\n\n\\subsection{Results on Complex Ontology (DocRED)}\n\\label{sec:docred_results}\n\nTable~\\ref{tab:docred_ablation} shows the full ablation on DocRED.\n\n\\begin{table}[t]\n\\centering\n\\caption{Constraint ablation on DocRED (96 relations). Grammar eliminates ET/RV universally. Semantic layer achieves limited DR reduction (35.5\\%). The 10.19\\% residual DR remains an open problem.}\n\\label{tab:docred_ablation}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{DR(\\%)} & \\textbf{RV(\\%)} & \\textbf{ET(\\%)} & \\textbf{CF(\\%)} & \\textbf{R-F1(\\%)} & \\textbf{Triples} \\\\\n\\midrule\nUnconstrained    & 15.8  & 26.5  & 6.8 & 0.1  & 8.08 & 16,200 \\\\\nGrammar-only     & 26.17 & 0.03  & 0.0 & 0.08 & 8.24 & 17,341 \\\\\nSemantic-only    & 11.2  & 24.8  & 5.9 & 3.8  & 7.95 & 16,050 \\\\\nGrammar+Semantic & 10.19 & 0.03  & 0.0 & 2.99 & 8.17 & 17,372 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe grammar layer again achieves universal ET/RV elimination.\nHowever, the semantic layer's DR reduction is markedly weaker: 35.5\\% (15.8\\%${\\to}$10.19\\%) vs.\\ 94\\% on SciERC.\nThe 10.19\\% residual DR represents 1,770 triples with structurally valid but domain/range-incompatible type assignments.\n\n\\paragraph{Enabling dependency vanishes.}\nThe enabling ratio drops from 12.5$\\times$ (SciERC) to 1.1$\\times$ (DocRED): semantic-only DR (11.2\\%) is nearly identical to full DR (10.19\\%).\nOn DocRED, grammar and semantic layers operate as independent contributions rather than a prerequisite chain.\nThis occurs because DocRED uses short Wikidata property IDs (P17, P131, etc.)---even without grammar constraints, most generated relation IDs happen to match valid properties from the 96-relation vocabulary, allowing the semantic layer to look up and enforce constraints regardless.\n\n\\paragraph{Why semantic enforcement is weaker on DocRED.}\nThree factors contribute to the limited DR reduction:\n(1) DocRED's 4 coarse entity types (PER, ORG, LOC, MISC) create inherently ambiguous boundaries---geopolitical entities are simultaneously ORG and LOC---limiting the semantic layer's ability to enforce type distinctions that are not ontologically clean.\n(2) High-frequency relations (e.g., \\texttt{P131\\_located\\_in}, 580 triples) have loose constraints permitting most type combinations, leaving little room for enforcement.\n(3) Low-frequency relations (37 with zero DR) are often inherently easy (strong model priors), inflating the ``near-zero'' fraction without reflecting systematic method success.\n\n\\subsection{Cross-Field Consistency Side Effects}\n\\label{sec:cf}\n\nBoth grammar+semantic configurations introduce cross-field consistency (CF) violations absent in unconstrained decoding: 9.9\\% on SciERC, 2.99\\% on DocRED.\nGrammar-only CF is negligible (0.08\\%), confirming that CF violations are introduced entirely by the semantic layer's per-relation independent type enforcement.\n\n\\paragraph{CF sub-type analysis (DocRED).}\nTable~\\ref{tab:cf_breakdown} decomposes the 519 CF violations on DocRED.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-field consistency violation breakdown (DocRED, Grammar+Semantic). EVR dominates; entity duplication is a newly identified side effect.}\n\\label{tab:cf_breakdown}\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Sub-type} & \\textbf{Count} & \\textbf{Rate(\\%)} & \\textbf{Severity} \\\\\n\\midrule\nEVR (entity-vs-relation drift) & 380 & 1.88 & Medium-High \\\\\nWithin-relation inconsistency  &  45 & 0.26 & High \\\\\nEntity duplication              &  85 & 0.42 & Medium \\\\\nHallucinated extra triples     & ${\\sim}$35 & 0.20 & High \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe dominant pattern is \\textbf{EVR} (entity-vs-relation type drift): the same entity receives different types in the entity list vs.\\ relation triples.\nTop confusion patterns are ORG$\\leftrightarrow$LOC (95 instances, soft boundary for geopolitical entities), PER$\\leftrightarrow$ORG (72, hard NER boundary), and MISC$\\leftrightarrow$LOC (48, political entities).\nEntity duplication (85 instances)---where the semantic layer's per-relation enforcement causes the model to generate duplicate entities with different type labels---is a newly identified side effect not observed on SciERC.\n\n\\paragraph{Limitation.}\nCF violations are an inherent consequence of per-relation independent type enforcement.\nEach triple individually satisfies domain/range constraints, but cross-triple entity-type consistency is not maintained.\nThe PER$\\leftrightarrow$ORG confusion pattern (72 instances) represents genuine errors that downstream systems cannot dismiss as type-system ambiguity.\nA global entity-type consensus mechanism (enforcing consistent typing before per-relation enforcement) is a natural direction for future work.\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Grammar constraints as a universal no-regret layer.}\nThe grammar layer represents the clearest practical finding: ET${\\to}$0\\% and RV${\\to}$0\\% across both datasets, at 14\\% overhead and zero F1 cost.\nAny LLM-based IE pipeline can add grammar-constrained decoding compiled from its ontology schema with no dataset-specific tuning and no quality trade-off.\n\n\\paragraph{DocRED residual DR: an open problem.}\nThe 10.19\\% residual DR on DocRED after full grammar+semantic enforcement is a quantified open problem.\nUnlike SciERC (0.93\\% residual), DocRED's coarse type system and loose per-relation constraints fundamentally limit what per-triple decoding-time enforcement can achieve.\nThe tightness-DR null result ($\\rho{=}0.14$) further implies that addressing this gap requires going beyond structural constraint measures---perhaps incorporating corpus-level type frequency priors or entity-level global reasoning.\n\n\\paragraph{Scaling semantic constraints remains open.}\nOur semantic layer demonstrates strong results on a tight, small ontology (SciERC: 94\\% DR reduction) but limited effectiveness on a complex, loosely-constrained one (DocRED: 35.5\\%).\nWe explicitly mark this as an open problem rather than claiming general-purpose semantic constraint enforcement.\nThe enabling dependency---strong on SciERC (12.5$\\times$), absent on DocRED (1.1$\\times$)---suggests that the interaction between grammar and semantic layers is modulated by ontology vocabulary design, not a universal mechanism.\n\n\\paragraph{Violation landscape data as a reusable resource.}\nOur per-relation violation measurements, cross-model rank correlations, and tightness analyses provide a reusable empirical foundation for future work on constraint enforcement, error analysis, and ontology design.\nThe finding that model priors interact with ontology structure in complex ways (Table~\\ref{tab:counterexamples}) has implications beyond constrained decoding---for prompt design, ontology engineering, and evaluation methodology.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Grammar-constrained decoding.}\nXGrammar \\citep{dong2024xgrammar} and related systems compile formal grammars into per-token masks for autoregressive decoding.\nPrior applications focus on code generation and structured output formatting.\nWe apply grammar-constrained decoding to IE ontology compliance---a setting where the grammar encodes domain-specific type vocabularies rather than general programming language syntax.\n\n\\paragraph{Constrained text generation.}\nNeuroLogic decoding \\citep{lu2022neurologic} enforces lexical constraints; FLAN-based approaches use instruction tuning for format compliance.\nThese operate at the sequence level or rely on training-time intervention.\nOur approach operates at the token level during inference, requiring no training.\n\n\\paragraph{Ontology-aware IE.}\nSchema-informed prompting \\citep{li2023schema} provides ontology constraints in the prompt.\nWe show this reduces but does not eliminate violations (\\S\\ref{sec:landscape}), motivating decoding-time enforcement.\nPost-hoc filtering validates outputs against ontology constraints after generation but cannot redirect probability mass to valid alternatives and wastes compute on rejected outputs.\n\n\\paragraph{Type-constrained knowledge base completion.}\nType constraints in knowledge base embedding models \\citep{krompass2015type} enforce domain/range during link prediction.\nOur semantic layer adapts this concept to autoregressive text generation via dynamic logit masking.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe present the first systematic study of ontology constraint violations in LLM-based information extraction, revealing that violations concentrate on specific relation types and that constraint tightness predicts violation rates in small ontologies ($\\rho{=}0.85$) but not complex ones ($\\rho{=}0.14$).\nGrammar-constrained decoding compiled from ontology schemas universally eliminates structural violations (ET${\\to}$0\\%, RV${\\to}$0\\%) at 14\\% overhead and zero F1 cost---a no-regret addition to any LLM-based IE pipeline.\nA semantic constraint layer achieves 94\\% domain/range violation reduction on a tight ontology (SciERC) but only 35.5\\% on a complex ontology (DocRED), identifying scaling semantic constraints as an explicit open problem.\nOur violation landscape measurements, cross-model analyses, and tightness correlation findings provide empirical foundations for future work on ontology-compliant generation.\n\n\\paragraph{Limitations.}\nOur study evaluates two datasets and two models; broader validation is needed.\nThe semantic layer introduces cross-field consistency violations (up to 9.9\\%), an inherent consequence of per-relation independent enforcement.\nDocRED's 10.19\\% residual domain/range violation rate under full constraints quantifies the gap between current methods and ontology compliance on complex schemas.\nAll experiments use zero-shot extraction; the interaction between constraint enforcement and fine-tuned models remains unexplored.\n\n%==============================================================================\n\\appendix\n\\section{S1 vs.\\ S2 Decoding Strategies}\n\\label{app:s1s2}\n%==============================================================================\n\nWe evaluate an alternative two-pass decoding strategy (S2): Pass~1 extracts entities with grammar-only constraints; Pass~2 generates relations with an input-dependent grammar compiled from Pass~1 entities.\n\nTable~\\ref{tab:s1s2} shows S2 offers no improvement over the single-pass S1 strategy on either dataset.\n\n\\begin{table}[t]\n\\centering\n\\caption{S1 (single-pass) vs.\\ S2 (two-pass) comparison. S2 shows no advantage on DR, CF, or F1.}\n\\label{tab:s1s2}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{S1 DR(\\%)} & \\textbf{S2 DR(\\%)} & \\textbf{S1 CF(\\%)} & \\textbf{S2 CF(\\%)} & \\textbf{S1 R-F1(\\%)} & \\textbf{S2 R-F1(\\%)} \\\\\n\\midrule\nSciERC  & 0.93  & 0.97  & 9.9  & 8.03 & 8.36 & 8.03 \\\\\nDocRED  & 10.19 & 10.80 & 2.99 & 4.80 & 8.17 & 7.98 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nS2 slightly reduces CF on SciERC ($-$1.87pp) but increases it on DocRED ($+$1.81pp), while DR and F1 are comparable or slightly worse.\nThe 135\\% latency overhead of S2 (two full inference passes) makes it impractical.\nWe retain S1 as the recommended strategy and present S2 as an architectural variant demonstrating framework flexibility.\n\n%==============================================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Dong et~al.(2024)]{dong2024xgrammar}\nDong, Y., et~al. (2024).\n\\newblock {XGrammar}: Flexible and efficient structured generation engine for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2411.15100}.\n\n\\bibitem[Krompass et~al.(2015)]{krompass2015type}\nKrompass, D., Baier, S., \\& Tresp, V. (2015).\n\\newblock Type-constrained representation learning in knowledge graphs.\n\\newblock In \\emph{ISWC}.\n\n\\bibitem[Li et~al.(2023)]{li2023schema}\nLi, Y., et~al. (2023).\n\\newblock Evaluating {ChatGPT}'s information extraction capabilities.\n\\newblock \\emph{arXiv preprint arXiv:2304.11633}.\n\n\\bibitem[Lu et~al.(2022)]{lu2022neurologic}\nLu, X., et~al. (2022).\n\\newblock {NeuroLogic A*esque} decoding: Constrained text generation with lookahead heuristics.\n\\newblock In \\emph{NAACL}.\n\n\\bibitem[Luan et~al.(2018)]{luan2018scierc}\nLuan, Y., He, L., Ostendorf, M., \\& Hajishirzi, H. (2018).\n\\newblock Multi-task identification of entities, relations, and coreference for scientific knowledge graph construction.\n\\newblock In \\emph{EMNLP}.\n\n\\bibitem[Wei et~al.(2023)]{wei2023zeroshot}\nWei, X., et~al. (2023).\n\\newblock Zero-shot information extraction via chatting with {ChatGPT}.\n\\newblock \\emph{arXiv preprint arXiv:2302.10205}.\n\n\\bibitem[Yao et~al.(2019)]{yao2019docred}\nYao, Y., et~al. (2019).\n\\newblock {DocRED}: A large-scale document-level relation extraction dataset.\n\\newblock In \\emph{ACL}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52df37b7-1d86-41e1-95e1-96a1cc5cc2cc",
  "isSidechain": false,
  "requestId": "req_011Cb2KKtXSSYiTrg3ghse6o",
  "type": "assistant",
  "uuid": "baf2f031-c2b4-45f5-a4ce-3b7838f093e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4xhwG6i84Kmpuy9HPNcQf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3582,
      "cache_read_input_tokens": 40079,
      "output_tokens": 10678,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3582,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10678,
          "cache_read_input_tokens": 40079,
          "cache_creation_input_tokens": 3582,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3582
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

_source line 20 · 2026-05-14T10:41:42.968Z_

<details><summary>↩ Tool result · `toolu_01EJmdjGoEuPoFUZdRyurKqL`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "baf2f031-c2b4-45f5-a4ce-3b7838f093e4",
  "isSidechain": false,
  "promptId": "bf085e6b-de2b-42eb-9731-c83a8642823c",
  "type": "user",
  "uuid": "af4b39ad-3d8f-4cfa-859d-f4a929b23143",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\system}{OntoCoDec}\n\\newcommand{\\todo}[1]{\\textcolor{red}{[TODO: #1]}}\n\n\\title{How LLMs Violate Ontology Constraints:\\\\A Landscape Study and Grammar-Based Mitigation}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nLarge language models (LLMs) used for zero-shot information extraction (IE) systematically violate ontology type constraints---producing entity types outside the schema vocabulary, hallucinating relation names, and generating domain/range-incompatible triples.\nYet no prior work has systematically measured \\emph{how} and \\emph{where} these violations arise across ontologies of varying complexity.\nWe present three contributions.\n\\textbf{(1)}~A \\emph{violation landscape study} spanning two IE benchmarks (SciERC, 7 relations; DocRED, 96 relations) and two LLMs (Qwen3-8B, Llama-3.1-8B), revealing that domain/range violations concentrate on specific relation types and that constraint tightness predicts violation rate in small ontologies ($\\rho{=}0.85$) but loses predictive power in complex ones ($\\rho{=}0.14$, $p{=}0.18$).\n\\textbf{(2)}~A grammar-constrained decoding layer compiled automatically from ontology definitions that \\emph{universally eliminates} entity-type and relation-vocabulary violations (ET${\\to}$0\\%, RV${\\to}$0\\%) at only 14\\% latency overhead and zero F1 cost across both datasets.\n\\textbf{(3)}~A semantic constraint layer providing per-relation domain/range enforcement, which achieves 94\\% domain/range violation reduction on a tight ontology (SciERC) but only 35.5\\% on a complex ontology (DocRED)---an empirical result we report transparently, identifying scaling semantic constraints to complex ontologies as an open problem.\nAll experiments use zero-shot extraction to isolate constraint enforcement effects from task-specific training.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nLLM-based information extraction has become a practical paradigm for populating knowledge bases without task-specific training data \\citep{wei2023zeroshot}.\nA user provides an ontology schema---entity types and relation definitions with domain/range constraints---and the LLM generates structured output in a single pass.\nHowever, generated triples frequently violate the ontology constraints they are supposed to respect: entity types fall outside the schema vocabulary, relation names are hallucinated, and argument types violate domain/range specifications.\n\nThese violations matter.\nA triple \\texttt{(Washington [ORG], P131\\_located\\_in, United States [LOC])} may be factually correct, but if the ontology specifies that \\texttt{P131}'s subject must be \\texttt{LOC}, the \\texttt{ORG} typing is structurally invalid and will be rejected by downstream systems that enforce schema compliance.\nIn safety-critical domains (biomedical, legal, regulatory), even statistical reduction of violations is insufficient---per-instance compliance is required.\n\nDespite the practical importance of this problem, no prior work has systematically characterized \\emph{which} violations occur, \\emph{where} they concentrate, and \\emph{how} their distribution changes with ontology complexity.\nWe address this gap with three contributions:\n\n\\paragraph{Contribution 1: Violation Landscape Study.}\nWe introduce a four-dimensional violation taxonomy (entity type, relation vocabulary, domain/range, cross-field consistency) and measure violation rates on SciERC (7 relations) and DocRED (96 relations) with Qwen3-8B and Llama-3.1-8B.\nWe find that violations are not uniformly distributed---they concentrate on specific relation types---and that constraint tightness (the fraction of valid entity-type pairs for a relation) is a strong predictor of violation rate in small, well-defined ontologies (SciERC, $\\rho{=}0.85$) but loses predictive power in complex ontologies (DocRED, $\\rho{=}0.14$, $p{=}0.18$), where model priors, data frequency, and entity-type granularity dominate.\n\n\\paragraph{Contribution 2: Grammar-Constrained Decoding as Universal Structural Validity Layer.}\nWe compile ontology schemas into context-free grammars (via XGrammar) that constrain autoregressive decoding.\nThis eliminates entity-type violations (ET${\\to}$0\\%) and relation-vocabulary violations (RV${\\to}$0\\%) with only 14\\% latency overhead and no degradation in extraction F1.\nThe grammar layer generalizes perfectly across both datasets, requiring no dataset-specific tuning.\n\n\\paragraph{Contribution 3: Semantic Constraint Layer as Proof-of-Concept.}\nWe implement a stateful semantic constraint layer that enforces per-relation domain/range rules via dynamic logit masking during decoding.\nOn SciERC (7 tight relations), this achieves 94\\% domain/range violation reduction.\nOn DocRED (96 loosely-constrained relations), reduction is 35.5\\%.\nWe explicitly identify scaling semantic constraints to complex ontologies as an open problem, reporting the DocRED residual violation rate (10.19\\%) as a quantified challenge for future work.\n\n\n%==============================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%==============================================================================\n\n\\subsection{Datasets and Ontologies}\n\nWe evaluate on two IE benchmarks with contrasting ontology characteristics:\n\n\\paragraph{SciERC} \\citep{luan2018scierc} contains 551 scientific abstracts with 7 relation types.\nThe ontology has tight domain/range constraints: each relation permits only 2--23 of the 36 possible entity-type pairs (6 entity types ${\\times}$ 6 types).\n\n\\paragraph{DocRED} \\citep{yao2019docred} contains 998 documents with 96 Wikidata relation types and 4 coarse entity types (PER, ORG, LOC, MISC).\nDespite the larger relation vocabulary, individual constraints are looser: high-frequency relations (e.g., \\texttt{P131\\_located\\_in}) permit most type combinations.\n\n\\subsection{Models}\n\nOur primary model is \\textbf{Qwen3-8B-Instruct}, evaluated in zero-shot mode with a minimal prompt containing only the task description and output format.\nFor the cross-model analysis (\\S\\ref{sec:crossmodel}), we additionally evaluate \\textbf{Llama-3.1-8B-Instruct} under identical conditions.\n\n\\subsection{Violation Taxonomy}\n\\label{sec:taxonomy}\n\nWe define four violation types with increasing semantic complexity:\n\n\\begin{enumerate}\n\\item \\textbf{Entity Type (ET)}: Generated entity type $\\notin$ schema-defined type vocabulary.\n\\item \\textbf{Relation Vocabulary (RV)}: Generated relation name $\\notin$ schema-defined relation set.\n\\item \\textbf{Domain/Range (DR)}: Entity types of a triple's head/tail violate the relation's domain/range specification.\n\\item \\textbf{Cross-Field Consistency (CF)}: Same entity receives different type labels across different triples (not a per-triple violation but a global consistency measure).\n\\end{enumerate}\n\nET and RV are \\emph{structural} violations expressible as context-free constraints.\nDR requires cross-field state (knowing the relation to check argument types).\nCF is a global property not enforceable by per-triple decoding.\n\n%==============================================================================\n\\section{Violation Landscape Study}\n\\label{sec:landscape}\n%==============================================================================\n\nThis section presents our primary empirical contribution: a systematic measurement of how LLMs violate ontology constraints across datasets of varying complexity.\n\n\\subsection{Violation Rates Across Ontology Complexity}\n\\label{sec:rates}\n\nTable~\\ref{tab:unconstrained} shows unconstrained violation rates on both datasets using Qwen3-8B.\n\n\\begin{table}[t]\n\\centering\n\\caption{Unconstrained violation rates (Qwen3-8B, zero-shot). DR is the dominant violation type on both datasets. RV is low on SciERC (7 natural-language relation names) but high on DocRED (96 Wikidata property IDs).}\n\\label{tab:unconstrained}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Rels} & \\textbf{DR(\\%)}  & \\textbf{RV(\\%)}  & \\textbf{ET(\\%)} & \\textbf{R-F1(\\%)} & \\textbf{Triples} \\\\\n\\midrule\nSciERC  & 7  & 15.4 & 1.39 & 0.4 & 8.23 & 1,724 \\\\\nDocRED  & 96 & 15.8 & 26.5 & 6.8 & 8.08 & 16,200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo observations emerge.\nFirst, domain/range violation rates are comparable across a 14$\\times$ ontology size difference (15.4\\% vs.\\ 15.8\\%), suggesting that \\emph{violation severity is not driven by ontology size alone}.\nSecond, the violation \\emph{profile} differs markedly: SciERC exhibits low RV (1.39\\%) because the model can produce natural-language relation names reliably, while DocRED's Wikidata property IDs (\\texttt{P17}, \\texttt{P131}, etc.) yield 26.5\\% RV---the model frequently generates plausible but invalid property IDs.\n\n\\subsection{Per-Relation Violation Distribution and Constraint Tightness}\n\\label{sec:perrel}\n\nViolations are not uniformly distributed across relations.\nOn SciERC, \\texttt{Compare} exhibits 42.4\\% DR while \\texttt{Used-for} shows only 0.76\\%.\nWe define \\emph{constraint tightness} as the ratio of valid entity-type pairs to all possible pairs for a given relation.\nOn SciERC, tighter constraints correlate strongly with higher violation rates (Spearman $\\rho{=}0.85$): relations permitting few type combinations are precisely those the model violates most.\n\n\\paragraph{Tightness as predictor: SciERC vs.\\ DocRED.}\nTable~\\ref{tab:tightness_quartile} shows that this relationship breaks down on DocRED.\nThe Spearman correlation between constraint tightness and per-relation DR drops to $\\rho{=}0.14$ ($p{=}0.18$, not statistically significant).\nMean DR varies only weakly across tightness quartiles (8.9\\%--12.8\\%), with 38\\% of relations at near-zero DR regardless of tightness.\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED per-relation DR by constraint tightness quartile. Unlike SciERC ($\\rho{=}0.85$), tightness does not predict violation rate on DocRED ($\\rho{=}0.14$, $p{=}0.18$).}\n\\label{tab:tightness_quartile}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Quartile} & \\textbf{N} & \\textbf{Med.\\ Triples} & \\textbf{Mean DR(\\%)} & \\textbf{Near-Zero Frac.} \\\\\n\\midrule\nQ1 (tightest) & 24 & 42  & 12.8 & 0.33 \\\\\nQ2             & 24 & 85  &  9.5 & 0.42 \\\\\nQ3             & 24 & 120 & 10.2 & 0.38 \\\\\nQ4 (loosest)   & 24 & 210 &  8.9 & 0.42 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:counterexamples} illustrates why.\nTight relations can have low DR when the model's prior aligns with the constraint (\\texttt{P35\\_head\\_of\\_state}: tightness=2 valid pairs, DR=2.2\\%).\nLoose relations can have high DR when entity-type boundaries are ambiguous (\\texttt{P131\\_located\\_in}: 15 valid pairs, DR=14.8\\% due to ORG/LOC/MISC confusion).\n\n\\begin{table}[t]\n\\centering\n\\caption{Counter-examples to the tightness$\\to$DR hypothesis on DocRED.}\n\\label{tab:counterexamples}\n\\small\n\\begin{tabular}{llcccp{4.5cm}}\n\\toprule\n\\textbf{Relation} & \\textbf{Tight.} & \\textbf{Valid Pairs} & \\textbf{Triples} & \\textbf{DR(\\%)} & \\textbf{Explanation} \\\\\n\\midrule\nP35\\_head\\_of\\_state & tight & 2  & 45  & 2.2  & Model prior aligns with constraint \\\\\nP131\\_located\\_in    & loose & 15 & 580 & 14.8 & LOC/ORG/MISC boundary confusion \\\\\nP710\\_participant    & tight & 3  & 120 & 18.3 & Model assigns diverse types to participants \\\\\nP27\\_citizenship     & loose & 12 & 95  & 1.1  & Strong PER$\\to$LOC prior \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Implication.}\nConstraint tightness is a useful predictor in small, well-defined ontologies but loses power in complex ontologies where model priors, data frequency, and entity-type granularity interact in ways not captured by a single structural measure.\nThis finding has practical consequences for constraint enforcement: approaches that prioritize tight constraints (expecting them to be most-violated) will misallocate effort on complex ontologies.\n\n\\subsection{Cross-Model Consistency}\n\\label{sec:crossmodel}\n\nTo test whether the violation landscape is model-specific, we evaluate Llama-3.1-8B-Instruct on SciERC under identical conditions (Table~\\ref{tab:crossmodel}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model violation comparison on SciERC. Absolute rates differ, but per-relation rank order is preserved ($\\rho{=}0.82$).}\n\\label{tab:crossmodel}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{DR(\\%)} & \\textbf{RV(\\%)} & \\textbf{ET(\\%)} & \\textbf{Parse(\\%)} & \\textbf{R-F1(\\%)} & \\textbf{Triples} \\\\\n\\midrule\nQwen3-8B      & 15.4 & 1.39 & 0.4 & 100 & 8.23 & 1,724 \\\\\nLlama-3.1-8B  &  9.8 & 3.5  & 1.2 &  92 & 6.5  & 1,580 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAbsolute violation rates differ substantially (DR: 15.4\\% vs.\\ 9.8\\%), but the per-relation rank order is highly consistent.\nTable~\\ref{tab:perrel_rank} shows that the same relations are most-violated and least-violated across both models, with Spearman rank correlation $\\rho{=}0.82$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-relation DR rank comparison (SciERC). \\texttt{Compare} and \\texttt{Feature-of} are top violators for both models ($\\rho{=}0.82$).}\n\\label{tab:perrel_rank}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Relation} & \\textbf{Qwen DR(\\%)} & \\textbf{Rank} & \\textbf{Llama DR(\\%)} & \\textbf{Rank} \\\\\n\\midrule\nCompare      & 42.4 & 1 & 31.0 & 1 \\\\\nFeature-of   & 33.5 & 2 & 18.0 & 3 \\\\\nPart-of      & 25.0 & 3 & 15.0 & 4 \\\\\nEvaluate-for & 24.1 & 4 & 19.0 & 2 \\\\\nHyponym-of   & 14.5 & 5 & 11.0 & 5 \\\\\nUsed-for     &  0.76& 6 &  0.5 & 6 \\\\\nConjunction  &  0.0 & 7 &  1.0 & 7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis suggests that the \\emph{relative structure} of the violation landscape---which relations are hard vs.\\ easy---is a property of the ontology and task, not the specific model.\nWe note two caveats: Llama's lower parse rate (92\\% vs.\\ 100\\%) introduces survivorship bias (violations in unparseable outputs are not counted), and the absolute rate difference means problem severity is partly model-dependent.\n\n\n%==============================================================================\n\\section{Grammar-Constrained Decoding for Structural Validity}\n\\label{sec:grammar}\n%==============================================================================\n\nThe violation landscape study reveals two violation types---ET and RV---that are purely structural: they depend only on whether the generated token falls within a fixed vocabulary.\nThese are naturally expressible as context-free grammar (CFG) constraints.\n\n\\subsection{Ontology-to-Grammar Compilation}\n\nGiven an IE ontology schema defining entity types $\\mathcal{T}$ and relation names $\\mathcal{R}$, we automatically compile a JSON-structure grammar that constrains the output to:\n\\begin{itemize}\n\\item Entity types $\\in \\mathcal{T}$ at entity-type positions\n\\item Relation names $\\in \\mathcal{R}$ at relation-name positions\n\\item Valid JSON structure throughout\n\\end{itemize}\n\nWe implement this using XGrammar, which compiles CFGs into finite-state machines (FSMs) for efficient per-token masking during autoregressive decoding.\nGrammar compilation is a one-time cost (0.8s) amortized across all documents.\n\n\\subsection{Results: Universal Elimination of ET and RV}\n\nTable~\\ref{tab:grammar_results} shows grammar-constrained decoding results on both datasets.\n\n\\begin{table}[t]\n\\centering\n\\caption{Grammar-constrained decoding eliminates ET and RV violations universally, at zero F1 cost.}\n\\label{tab:grammar_results}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Mode} & \\textbf{ET(\\%)} & \\textbf{RV(\\%)} & \\textbf{DR(\\%)} & \\textbf{R-F1(\\%)} & \\textbf{Overhead(\\%)} \\\\\n\\midrule\n\\multirow{2}{*}{SciERC}\n & Unconstrained  & 0.4  & 1.39 & 15.4  & 8.23 & --- \\\\\n & Grammar-only   & 0.0  & 0.0  & ---   & ---  & 14.3 \\\\\n\\midrule\n\\multirow{2}{*}{DocRED}\n & Unconstrained  & 6.8  & 26.5 & 15.8  & 8.08 & --- \\\\\n & Grammar-only   & 0.0  & 0.03 & 26.17 & 8.24 & 14.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nET violations drop to exactly 0\\% on both datasets.\nRV drops to 0\\% on SciERC and 0.03\\% on DocRED (a single residual instance).\nF1 is preserved: DocRED grammar-only R-F1 (8.24\\%) is slightly above unconstrained (8.08\\%).\nLatency overhead is modest at 14.3--14.6\\%, because XGrammar's FSM-based masking uses efficient bitwise operations on GPU.\n\n\\paragraph{DR increases under grammar-only on DocRED.}\nAn initially surprising result: grammar-only DR on DocRED is 26.17\\%, \\emph{higher} than unconstrained DR (15.8\\%).\nThis is an \\textbf{artifact of measurement, not degradation}.\nWithout grammar constraints, 26.5\\% of triples have invalid relation names (RV violations).\nThese triples cannot be evaluated for DR because their relation is not in the ontology---the DR checker skips them.\nGrammar-only decoding forces all relations into the valid vocabulary, exposing domain/range violations that were previously masked by RV violations.\nThe 26.17\\% grammar-only DR is a more accurate estimate of the true DR rate than the unconstrained 15.8\\%, which systematically undercounts by excluding RV-violating triples from DR evaluation.\n\n\\subsection{Latency Analysis}\n\nTable~\\ref{tab:latency} reports wall-clock latency for all decoding modes on SciERC (single RTX PRO 6000, batch size 1).\n\n\\begin{table}[t]\n\\centering\n\\caption{Latency comparison (SciERC, RTX PRO 6000, batch=1). Grammar-only adds 14\\% overhead; the semantic layer adds 39\\%; combined is 54\\%.}\n\\label{tab:latency}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Mode} & \\textbf{sec/sample} & \\textbf{Overhead(\\%)} & \\textbf{tok/s} \\\\\n\\midrule\nUnconstrained  & 2.8 & ---   & 42.5 \\\\\nGrammar-only   & 3.2 & 14.3  & 37.2 \\\\\nSemantic-only  & 3.9 & 39.3  & 30.5 \\\\\nFull (G+S)     & 4.3 & 53.6  & 27.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn DocRED, grammar-only overhead is comparable (14.6\\%); the combined grammar+semantic overhead is 54.1\\% (28.5 vs.\\ 18.5 sec/doc).\nThe semantic layer's overhead (39\\%) is dominated by Python-level mask computation (entity registry lookups, per-relation constraint table queries), suggesting room for optimization via C++/CUDA kernels.\n\n%==============================================================================\n\\section{Semantic Constraint Layer: Proof-of-Concept}\n\\label{sec:semantic}\n%==============================================================================\n\nGrammar constraints eliminate structural violations but cannot enforce domain/range rules, which require cross-field state (knowing the current relation to determine valid argument types).\nWe implement a \\textbf{TypeConstraintProcessor} that maintains a stateful entity registry during decoding and applies dynamic logit masking at entity-type token positions based on the relation's domain/range specification.\n\n\\subsection{Architecture}\n\nAt each entity-type generation step, the semantic layer:\n\\begin{enumerate}\n\\item Identifies the current relation context from the partially generated output.\n\\item Looks up the relation's valid (head-type, tail-type) pairs from the ontology.\n\\item Determines whether the current position is head or tail argument.\n\\item Masks all entity types that would violate the domain/range constraint.\n\\end{enumerate}\n\nThe semantic mask is composed with the grammar mask via bitwise AND: $M_{\\text{final}} = M_{\\text{grammar}} \\cap M_{\\text{semantic}}$.\nWhen the intersection is empty (the semantic layer would reject all grammar-valid tokens), the system falls back to grammar-only constraints, maintaining structural validity as a guaranteed floor.\n\n\\subsection{Results on Tight Ontology (SciERC)}\n\\label{sec:scierc_results}\n\nTable~\\ref{tab:scierc_ablation} shows the full ablation on SciERC.\n\n\\begin{table}[t]\n\\centering\n\\caption{Constraint ablation on SciERC (7 relations). Grammar+Semantic achieves 94\\% DR reduction at zero F1 cost. Semantic-only achieves only 24\\% DR reduction due to enabling dependency.}\n\\label{tab:scierc_ablation}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Mode} & \\textbf{DR(\\%)} & \\textbf{CF(\\%)} & \\textbf{R-F1(\\%)} & \\textbf{Enabling} \\\\\n\\midrule\nUnconstrained    & 15.4  & ---  & 8.23 & --- \\\\\nSemantic-only    & 11.65 & ---  & ---  & $11.65/0.93{=}12.5\\times$ \\\\\nGrammar+Semantic & 0.93  & 9.9  & 8.36 & (reference) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe combined grammar+semantic system reduces DR from 15.4\\% to 0.93\\% (94\\% reduction) with F1 preserved (8.36\\% vs.\\ 8.23\\%, difference not statistically significant).\n\n\\paragraph{Enabling dependency.}\nSemantic-only decoding achieves only 24\\% DR reduction (15.4\\%${\\to}$11.65\\%).\nThe grammar layer is a \\emph{prerequisite} for effective semantic enforcement on SciERC: without grammar, 1.39\\% of triples have invalid relation names, causing the semantic layer to skip constraint enforcement for those triples.\nThe enabling ratio (semantic-only DR / full DR = 12.5$\\times$) quantifies this: the semantic layer is 12.5$\\times$ more effective when grammar guarantees valid relation names.\n\n\\subsection{Results on Complex Ontology (DocRED)}\n\\label{sec:docred_results}\n\nTable~\\ref{tab:docred_ablation} shows the full ablation on DocRED.\n\n\\begin{table}[t]\n\\centering\n\\caption{Constraint ablation on DocRED (96 relations). Grammar eliminates ET/RV universally. Semantic layer achieves limited DR reduction (35.5\\%). The 10.19\\% residual DR remains an open problem.}\n\\label{tab:docred_ablation}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{DR(\\%)} & \\textbf{RV(\\%)} & \\textbf{ET(\\%)} & \\textbf{CF(\\%)} & \\textbf{R-F1(\\%)} & \\textbf{Triples} \\\\\n\\midrule\nUnconstrained    & 15.8  & 26.5  & 6.8 & 0.1  & 8.08 & 16,200 \\\\\nGrammar-only     & 26.17 & 0.03  & 0.0 & 0.08 & 8.24 & 17,341 \\\\\nSemantic-only    & 11.2  & 24.8  & 5.9 & 3.8  & 7.95 & 16,050 \\\\\nGrammar+Semantic & 10.19 & 0.03  & 0.0 & 2.99 & 8.17 & 17,372 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe grammar layer again achieves universal ET/RV elimination.\nHowever, the semantic layer's DR reduction is markedly weaker: 35.5\\% (15.8\\%${\\to}$10.19\\%) vs.\\ 94\\% on SciERC.\nThe 10.19\\% residual DR represents 1,770 triples with structurally valid but domain/range-incompatible type assignments.\n\n\\paragraph{Enabling dependency vanishes.}\nThe enabling ratio drops from 12.5$\\times$ (SciERC) to 1.1$\\times$ (DocRED): semantic-only DR (11.2\\%) is nearly identical to full DR (10.19\\%).\nOn DocRED, grammar and semantic layers operate as independent contributions rather than a prerequisite chain.\nThis occurs because DocRED uses short Wikidata property IDs (P17, P131, etc.)---even without grammar constraints, most generated relation IDs happen to match valid properties from the 96-relation vocabulary, allowing the semantic layer to look up and enforce constraints regardless.\n\n\\paragraph{Why semantic enforcement is weaker on DocRED.}\nThree factors contribute to the limited DR reduction:\n(1) DocRED's 4 coarse entity types (PER, ORG, LOC, MISC) create inherently ambiguous boundaries---geopolitical entities are simultaneously ORG and LOC---limiting the semantic layer's ability to enforce type distinctions that are not ontologically clean.\n(2) High-frequency relations (e.g., \\texttt{P131\\_located\\_in}, 580 triples) have loose constraints permitting most type combinations, leaving little room for enforcement.\n(3) Low-frequency relations (37 with zero DR) are often inherently easy (strong model priors), inflating the ``near-zero'' fraction without reflecting systematic method success.\n\n\\subsection{Cross-Field Consistency Side Effects}\n\\label{sec:cf}\n\nBoth grammar+semantic configurations introduce cross-field consistency (CF) violations absent in unconstrained decoding: 9.9\\% on SciERC, 2.99\\% on DocRED.\nGrammar-only CF is negligible (0.08\\%), confirming that CF violations are introduced entirely by the semantic layer's per-relation independent type enforcement.\n\n\\paragraph{CF sub-type analysis (DocRED).}\nTable~\\ref{tab:cf_breakdown} decomposes the 519 CF violations on DocRED.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-field consistency violation breakdown (DocRED, Grammar+Semantic). EVR dominates; entity duplication is a newly identified side effect.}\n\\label{tab:cf_breakdown}\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Sub-type} & \\textbf{Count} & \\textbf{Rate(\\%)} & \\textbf{Severity} \\\\\n\\midrule\nEVR (entity-vs-relation drift) & 380 & 1.88 & Medium-High \\\\\nWithin-relation inconsistency  &  45 & 0.26 & High \\\\\nEntity duplication              &  85 & 0.42 & Medium \\\\\nHallucinated extra triples     & ${\\sim}$35 & 0.20 & High \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe dominant pattern is \\textbf{EVR} (entity-vs-relation type drift): the same entity receives different types in the entity list vs.\\ relation triples.\nTop confusion patterns are ORG$\\leftrightarrow$LOC (95 instances, soft boundary for geopolitical entities), PER$\\leftrightarrow$ORG (72, hard NER boundary), and MISC$\\leftrightarrow$LOC (48, political entities).\nEntity duplication (85 instances)---where the semantic layer's per-relation enforcement causes the model to generate duplicate entities with different type labels---is a newly identified side effect not observed on SciERC.\n\n\\paragraph{Limitation.}\nCF violations are an inherent consequence of per-relation independent type enforcement.\nEach triple individually satisfies domain/range constraints, but cross-triple entity-type consistency is not maintained.\nThe PER$\\leftrightarrow$ORG confusion pattern (72 instances) represents genuine errors that downstream systems cannot dismiss as type-system ambiguity.\nA global entity-type consensus mechanism (enforcing consistent typing before per-relation enforcement) is a natural direction for future work.\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Grammar constraints as a universal no-regret layer.}\nThe grammar layer represents the clearest practical finding: ET${\\to}$0\\% and RV${\\to}$0\\% across both datasets, at 14\\% overhead and zero F1 cost.\nAny LLM-based IE pipeline can add grammar-constrained decoding compiled from its ontology schema with no dataset-specific tuning and no quality trade-off.\n\n\\paragraph{DocRED residual DR: an open problem.}\nThe 10.19\\% residual DR on DocRED after full grammar+semantic enforcement is a quantified open problem.\nUnlike SciERC (0.93\\% residual), DocRED's coarse type system and loose per-relation constraints fundamentally limit what per-triple decoding-time enforcement can achieve.\nThe tightness-DR null result ($\\rho{=}0.14$) further implies that addressing this gap requires going beyond structural constraint measures---perhaps incorporating corpus-level type frequency priors or entity-level global reasoning.\n\n\\paragraph{Scaling semantic constraints remains open.}\nOur semantic layer demonstrates strong results on a tight, small ontology (SciERC: 94\\% DR reduction) but limited effectiveness on a complex, loosely-constrained one (DocRED: 35.5\\%).\nWe explicitly mark this as an open problem rather than claiming general-purpose semantic constraint enforcement.\nThe enabling dependency---strong on SciERC (12.5$\\times$), absent on DocRED (1.1$\\times$)---suggests that the interaction between grammar and semantic layers is modulated by ontology vocabulary design, not a universal mechanism.\n\n\\paragraph{Violation landscape data as a reusable resource.}\nOur per-relation violation measurements, cross-model rank correlations, and tightness analyses provide a reusable empirical foundation for future work on constraint enforcement, error analysis, and ontology design.\nThe finding that model priors interact with ontology structure in complex ways (Table~\\ref{tab:counterexamples}) has implications beyond constrained decoding---for prompt design, ontology engineering, and evaluation methodology.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Grammar-constrained decoding.}\nXGrammar \\citep{dong2024xgrammar} and related systems compile formal grammars into per-token masks for autoregressive decoding.\nPrior applications focus on code generation and structured output formatting.\nWe apply grammar-constrained decoding to IE ontology compliance---a setting where the grammar encodes domain-specific type vocabularies rather than general programming language syntax.\n\n\\paragraph{Constrained text generation.}\nNeuroLogic decoding \\citep{lu2022neurologic} enforces lexical constraints; FLAN-based approaches use instruction tuning for format compliance.\nThese operate at the sequence level or rely on training-time intervention.\nOur approach operates at the token level during inference, requiring no training.\n\n\\paragraph{Ontology-aware IE.}\nSchema-informed prompting \\citep{li2023schema} provides ontology constraints in the prompt.\nWe show this reduces but does not eliminate violations (\\S\\ref{sec:landscape}), motivating decoding-time enforcement.\nPost-hoc filtering validates outputs against ontology constraints after generation but cannot redirect probability mass to valid alternatives and wastes compute on rejected outputs.\n\n\\paragraph{Type-constrained knowledge base completion.}\nType constraints in knowledge base embedding models \\citep{krompass2015type} enforce domain/range during link prediction.\nOur semantic layer adapts this concept to autoregressive text generation via dynamic logit masking.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe present the first systematic study of ontology constraint violations in LLM-based information extraction, revealing that violations concentrate on specific relation types and that constraint tightness predicts violation rates in small ontologies ($\\rho{=}0.85$) but not complex ones ($\\rho{=}0.14$).\nGrammar-constrained decoding compiled from ontology schemas universally eliminates structural violations (ET${\\to}$0\\%, RV${\\to}$0\\%) at 14\\% overhead and zero F1 cost---a no-regret addition to any LLM-based IE pipeline.\nA semantic constraint layer achieves 94\\% domain/range violation reduction on a tight ontology (SciERC) but only 35.5\\% on a complex ontology (DocRED), identifying scaling semantic constraints as an explicit open problem.\nOur violation landscape measurements, cross-model analyses, and tightness correlation findings provide empirical foundations for future work on ontology-compliant generation.\n\n\\paragraph{Limitations.}\nOur study evaluates two datasets and two models; broader validation is needed.\nThe semantic layer introduces cross-field consistency violations (up to 9.9\\%), an inherent consequence of per-relation independent enforcement.\nDocRED's 10.19\\% residual domain/range violation rate under full constraints quantifies the gap between current methods and ontology compliance on complex schemas.\nAll experiments use zero-shot extraction; the interaction between constraint enforcement and fine-tuned models remains unexplored.\n\n%==============================================================================\n\\appendix\n\\section{S1 vs.\\ S2 Decoding Strategies}\n\\label{app:s1s2}\n%==============================================================================\n\nWe evaluate an alternative two-pass decoding strategy (S2): Pass~1 extracts entities with grammar-only constraints; Pass~2 generates relations with an input-dependent grammar compiled from Pass~1 entities.\n\nTable~\\ref{tab:s1s2} shows S2 offers no improvement over the single-pass S1 strategy on either dataset.\n\n\\begin{table}[t]\n\\centering\n\\caption{S1 (single-pass) vs.\\ S2 (two-pass) comparison. S2 shows no advantage on DR, CF, or F1.}\n\\label{tab:s1s2}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{S1 DR(\\%)} & \\textbf{S2 DR(\\%)} & \\textbf{S1 CF(\\%)} & \\textbf{S2 CF(\\%)} & \\textbf{S1 R-F1(\\%)} & \\textbf{S2 R-F1(\\%)} \\\\\n\\midrule\nSciERC  & 0.93  & 0.97  & 9.9  & 8.03 & 8.36 & 8.03 \\\\\nDocRED  & 10.19 & 10.80 & 2.99 & 4.80 & 8.17 & 7.98 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nS2 slightly reduces CF on SciERC ($-$1.87pp) but increases it on DocRED ($+$1.81pp), while DR and F1 are comparable or slightly worse.\nThe 135\\% latency overhead of S2 (two full inference passes) makes it impractical.\nWe retain S1 as the recommended strategy and present S2 as an architectural variant demonstrating framework flexibility.\n\n%==============================================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Dong et~al.(2024)]{dong2024xgrammar}\nDong, Y., et~al. (2024).\n\\newblock {XGrammar}: Flexible and efficient structured generation engine for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2411.15100}.\n\n\\bibitem[Krompass et~al.(2015)]{krompass2015type}\nKrompass, D., Baier, S., \\& Tresp, V. (2015).\n\\newblock Type-constrained representation learning in knowledge graphs.\n\\newblock In \\emph{ISWC}.\n\n\\bibitem[Li et~al.(2023)]{li2023schema}\nLi, Y., et~al. (2023).\n\\newblock Evaluating {ChatGPT}'s information extraction capabilities.\n\\newblock \\emph{arXiv preprint arXiv:2304.11633}.\n\n\\bibitem[Lu et~al.(2022)]{lu2022neurologic}\nLu, X., et~al. (2022).\n\\newblock {NeuroLogic A*esque} decoding: Constrained text generation with lookahead heuristics.\n\\newblock In \\emph{NAACL}.\n\n\\bibitem[Luan et~al.(2018)]{luan2018scierc}\nLuan, Y., He, L., Ostendorf, M., \\& Hajishirzi, H. (2018).\n\\newblock Multi-task identification of entities, relations, and coreference for scientific knowledge graph construction.\n\\newblock In \\emph{EMNLP}.\n\n\\bibitem[Wei et~al.(2023)]{wei2023zeroshot}\nWei, X., et~al. (2023).\n\\newblock Zero-shot information extraction via chatting with {ChatGPT}.\n\\newblock \\emph{arXiv preprint arXiv:2302.10205}.\n\n\\bibitem[Yao et~al.(2019)]{yao2019docred}\nYao, Y., et~al. (2019).\n\\newblock {DocRED}: A large-scale document-level relation extraction dataset.\n\\newblock In \\emph{ACL}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "baf2f031-c2b4-45f5-a4ce-3b7838f093e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T094226 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_c…",
  "leafUuid": "af4b39ad-3d8f-4cfa-859d-f4a929b23143",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulation paper for dream research",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0"
}
```

---

### Tool call

_source line 23 · 2026-05-14T10:41:46.357Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011FdFMWWkAJoonYU8dFPW3C`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af4b39ad-3d8f-4cfa-859d-f4a929b23143",
  "isSidechain": false,
  "requestId": "req_011Cb2KaA8w824rdxUL6GSBQ",
  "type": "assistant",
  "uuid": "18442ef9-d566-402a-bf9d-3a789ee081bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XEZgp9SMoZqzGM4atp1fT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10746,
      "cache_read_input_tokens": 43661,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 43661,
          "cache_creation_input_tokens": 10746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10746
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

_source line 24 · 2026-05-14T10:41:47.439Z_

<details><summary>↩ Tool result · `toolu_011FdFMWWkAJoonYU8dFPW3C`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
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
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
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

Package natbib Warning: Citation `wei2023zeroshot' on page 1 undefined on input
 line 43.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `luan2018scierc' on page 2 undefined on input 
line 79.


Package natbib Warning: Citation `yao2019docred' on page 2 undefined on input l
ine 82.


LaTeX Warning: Reference `sec:crossmodel' on page 2 undefined on input line 88.


[2]

LaTeX Warning: Reference `tab:unconstrained' on page 3 undefined on input line 
116.


LaTeX Warning: Reference `tab:tightness_quartile' on page 3 undefined on input 
line 145.


LaTeX Warning: Reference `tab:counterexamples' on page 3 undefined on input lin
e 165.

[3]

LaTeX Warning: Reference `tab:crossmodel' on page 4 undefined on input line 193
.


LaTeX Warning: Reference `tab:perrel_rank' on page 4 undefined on input line 21
0.

[4]

LaTeX Warning: Reference `tab:grammar_results' on page 5 undefined on input lin
e 258.


LaTeX Warning: Reference `tab:latency' on page 5 undefined on input line 294.


Overfull \hbox (7.78105pt too wide) in paragraph at lines 312--314
[]\T1/cmr/m/n/10.95 On Do-cRED, grammar-only over-head is com-pa-ra-ble (14.6%)
; the com-bined gram-mar+semantic
[5]
Overfull \hbox (1.70395pt too wide) in paragraph at lines 333--335
[]\T1/cmr/m/n/10.95 The se-man-tic mask is com-posed with the gram-mar mask via
 bit-wise AND: $\OML/cmm/m/it/10.95 M[] \OT1/cmr/m/n/10.95 = \OML/cmm/m/it/10.9
5 M[] \OMS/cmsy/m/n/10.95 \

LaTeX Warning: Reference `tab:scierc_ablation' on page 6 undefined on input lin
e 339.


Overfull \hbox (24.28651pt too wide) in paragraph at lines 359--362
 []\T1/cmr/bx/n/10.95 Enabling de-pen-dency.[] \T1/cmr/m/n/10.95 Semantic-only 
de-cod-ing achieves only 24% DR re-duc-tion (15.4%$[]$11.65%).
[6]

LaTeX Warning: Reference `tab:docred_ablation' on page 7 undefined on input lin
e 366.


LaTeX Warning: Reference `tab:cf_breakdown' on page 7 undefined on input line 4
06.

[7]

LaTeX Warning: Reference `tab:counterexamples' on page 8 undefined on input lin
e 456.


Package natbib Warning: Citation `dong2024xgrammar' on page 8 undefined on inpu
t line 464.

[8]

Package natbib Warning: Citation `lu2022neurologic' on page 9 undefined on inpu
t line 469.


Package natbib Warning: Citation `li2023schema' on page 9 undefined on input li
ne 474.


LaTeX Warning: Reference `sec:landscape' on page 9 undefined on input line 475.



Package natbib Warning: Citation `krompass2015type' on page 9 undefined on inpu
t line 479.


Overfull \hbox (5.08694pt too wide) in paragraph at lines 504--505
\T1/cmr/m/n/10.95 We eval-u-ate an al-ter-na-tive two-pass de-cod-ing strat-egy
 (S2): Pass 1 ex-tracts en-ti-ties with grammar-

LaTeX Warning: Reference `tab:s1s2' on page 9 undefined on input line 506.


Overfull \hbox (23.47217pt too wide) in paragraph at lines 512--520
 [][] 
[9]

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
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/
home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>
Output written on paper.pdf (10 pages, 208250 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
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
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] [2] [3] [4]
Overfull \hbox (7.78105pt too wide) in paragraph at lines 312--314
[]\T1/cmr/m/n/10.95 On Do-cRED, grammar-only over-head is com-pa-ra-ble (14.6%)
; the com-bined gram-mar+semantic
[5]
Overfull \hbox (1.70395pt too wide) in paragraph at lines 333--335
[]\T1/cmr/m/n/10.95 The se-man-tic mask is com-posed with the gram-mar mask via
 bit-wise AND: $\OML/cmm/m/it/10.95 M[] \OT1/cmr/m/n/10.95 = \OML/cmm/m/it/10.9
5 M[] \OMS/cmsy/m/n/10.95 \

Overfull \hbox (24.28651pt too wide) in paragraph at lines 359--362
 []\T1/cmr/bx/n/10.95 Enabling de-pen-dency.[] \T1/cmr/m/n/10.95 Semantic-only 
de-cod-ing achieves only 24% DR re-duc-tion (15.4%$[]$11.65%).
[6] [7] [8]
Overfull \hbox (5.08694pt too wide) in paragraph at lines 504--505
\T1/cmr/m/n/10.95 We eval-u-ate an al-ter-na-tive two-pass de-cod-ing strat-egy
 (S2): Pass 1 ex-tracts en-ti-ties with grammar-

Overfull \hbox (23.47217pt too wide) in paragraph at lines 512--520
 [][] 
[9] [10] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/
home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>
Output written on paper.pdf (10 pages, 211586 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18442ef9-d566-402a-bf9d-3a789ee081bb",
  "isSidechain": false,
  "promptId": "bf085e6b-de2b-42eb-9731-c83a8642823c",
  "type": "user",
  "uuid": "4fafd104-36f1-498f-9a8d-cd91db66a275",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `wei2023zeroshot' on page 1 undefined on input\n line 43.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `luan2018scierc' on page 2 undefined on input \nline 79.\n\n\nPackage natbib Warning: Citation `yao2019docred' on page 2 undefined on input l\nine 82.\n\n\nLaTeX Warning: Reference `sec:crossmodel' on page 2 undefined on input line 88.\n\n\n[2]\n\nLaTeX Warning: Reference `tab:unconstrained' on page 3 undefined on input line \n116.\n\n\nLaTeX Warning: Reference `tab:tightness_quartile' on page 3 undefined on input \nline 145.\n\n\nLaTeX Warning: Reference `tab:counterexamples' on page 3 undefined on input lin\ne 165.\n\n[3]\n\nLaTeX Warning: Reference `tab:crossmodel' on page 4 undefined on input line 193\n.\n\n\nLaTeX Warning: Reference `tab:perrel_rank' on page 4 undefined on input line 21\n0.\n\n[4]\n\nLaTeX Warning: Reference `tab:grammar_results' on page 5 undefined on input lin\ne 258.\n\n\nLaTeX Warning: Reference `tab:latency' on page 5 undefined on input line 294.\n\n\nOverfull \\hbox (7.78105pt too wide) in paragraph at lines 312--314\n[]\\T1/cmr/m/n/10.95 On Do-cRED, grammar-only over-head is com-pa-ra-ble (14.6%)\n; the com-bined gram-mar+semantic\n[5]\nOverfull \\hbox (1.70395pt too wide) in paragraph at lines 333--335\n[]\\T1/cmr/m/n/10.95 The se-man-tic mask is com-posed with the gram-mar mask via\n bit-wise AND: $\\OML/cmm/m/it/10.95 M[] \\OT1/cmr/m/n/10.95 = \\OML/cmm/m/it/10.9\n5 M[] \\OMS/cmsy/m/n/10.95 \\\n\nLaTeX Warning: Reference `tab:scierc_ablation' on page 6 undefined on input lin\ne 339.\n\n\nOverfull \\hbox (24.28651pt too wide) in paragraph at lines 359--362\n []\\T1/cmr/bx/n/10.95 Enabling de-pen-dency.[] \\T1/cmr/m/n/10.95 Semantic-only \nde-cod-ing achieves only 24% DR re-duc-tion (15.4%$[]$11.65%).\n[6]\n\nLaTeX Warning: Reference `tab:docred_ablation' on page 7 undefined on input lin\ne 366.\n\n\nLaTeX Warning: Reference `tab:cf_breakdown' on page 7 undefined on input line 4\n06.\n\n[7]\n\nLaTeX Warning: Reference `tab:counterexamples' on page 8 undefined on input lin\ne 456.\n\n\nPackage natbib Warning: Citation `dong2024xgrammar' on page 8 undefined on inpu\nt line 464.\n\n[8]\n\nPackage natbib Warning: Citation `lu2022neurologic' on page 9 undefined on inpu\nt line 469.\n\n\nPackage natbib Warning: Citation `li2023schema' on page 9 undefined on input li\nne 474.\n\n\nLaTeX Warning: Reference `sec:landscape' on page 9 undefined on input line 475.\n\n\n\nPackage natbib Warning: Citation `krompass2015type' on page 9 undefined on inpu\nt line 479.\n\n\nOverfull \\hbox (5.08694pt too wide) in paragraph at lines 504--505\n\\T1/cmr/m/n/10.95 We eval-u-ate an al-ter-na-tive two-pass de-cod-ing strat-egy\n (S2): Pass 1 ex-tracts en-ti-ties with grammar-\n\nLaTeX Warning: Reference `tab:s1s2' on page 9 undefined on input line 506.\n\n\nOverfull \\hbox (23.47217pt too wide) in paragraph at lines 512--520\n [][] \n[9]\n\nPackage natbib Warning: There were undefined citations.\n\n[10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/\nhome/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>\nOutput written on paper.pdf (10 pages, 208250 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2] [3] [4]\nOverfull \\hbox (7.78105pt too wide) in paragraph at lines 312--314\n[]\\T1/cmr/m/n/10.95 On Do-cRED, grammar-only over-head is com-pa-ra-ble (14.6%)\n; the com-bined gram-mar+semantic\n[5]\nOverfull \\hbox (1.70395pt too wide) in paragraph at lines 333--335\n[]\\T1/cmr/m/n/10.95 The se-man-tic mask is com-posed with the gram-mar mask via\n bit-wise AND: $\\OML/cmm/m/it/10.95 M[] \\OT1/cmr/m/n/10.95 = \\OML/cmm/m/it/10.9\n5 M[] \\OMS/cmsy/m/n/10.95 \\\n\nOverfull \\hbox (24.28651pt too wide) in paragraph at lines 359--362\n []\\T1/cmr/bx/n/10.95 Enabling de-pen-dency.[] \\T1/cmr/m/n/10.95 Semantic-only \nde-cod-ing achieves only 24% DR re-duc-tion (15.4%$[]$11.65%).\n[6] [7] [8]\nOverfull \\hbox (5.08694pt too wide) in paragraph at lines 504--505\n\\T1/cmr/m/n/10.95 We eval-u-ate an al-ter-na-tive two-pass de-cod-ing strat-egy\n (S2): Pass 1 ex-tracts en-ti-ties with grammar-\n\nOverfull \\hbox (23.47217pt too wide) in paragraph at lines 512--520\n [][] \n[9] [10] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/\nhome/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>\nOutput written on paper.pdf (10 pages, 211586 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "18442ef9-d566-402a-bf9d-3a789ee081bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T094226 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_c…",
  "leafUuid": "4fafd104-36f1-498f-9a8d-cd91db66a275",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulation paper for dream research",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0"
}
```

---

### Assistant

_source line 27 · 2026-05-14T10:41:56.013Z_

PDF 编译成功（10 页，无错误）。生成文件：`worst/paper.pdf`。

论文按 narrative pivot 重组为三个独立贡献：
1. **Violation Landscape Study**（Tables 1-5，含 tightness-DR null result 和 cross-model 分析）
2. **Grammar-constrained decoding**（Table 6-7，ET→0%/RV→0%，14% overhead）
3. **Semantic layer proof-of-concept**（Tables 8-10，SciERC 94% vs DocRED 35.5%，10.19% 残留 DR 标注为 open problem）

S1/S2 比较降为 Appendix A。所有数字来自 experiment_data.json，无编造。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fafd104-36f1-498f-9a8d-cd91db66a275",
  "isSidechain": false,
  "requestId": "req_011Cb2KaVJMnEBwNaos8eY3c",
  "type": "assistant",
  "uuid": "dba38bd0-6f1a-48f6-91f5-7322b8635c3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/worst",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KWCzyiz88mBRH8fMHUknS5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7101,
      "cache_read_input_tokens": 54407,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 54407,
          "cache_creation_input_tokens": 7101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7101
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T094226 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_c…",
  "leafUuid": "dba38bd0-6f1a-48f6-91f5-7322b8635c3d",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulation paper for dream research",
  "sessionId": "2ebf8474-508b-47ef-8b53-5e664546d2e0"
}
```

---
