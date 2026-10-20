# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165817 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/caabacc5-b31b-4906-931d-2a6bd0a7de0c.jsonl`
- **Structured JSON:** [`2294558af1fe3f91e9e2.json`](../../sessions/22/2294558af1fe3f91e9e2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T17:15:31.384Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T17:15:31.384Z",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165817 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：需要两处降级：(1) Claim 2 从 \"K=2显著优势\" 降级为 \"K=3显著优势，K=2趋势一致但bootstrap CI重叠(p=0.07)\"， early detection故事后移一步但仍成立；(2) Claim 1 从 \"evasion hierarchy\" 软化为 \"pragmatic features 提供complementary robustness\"，delta-delta=5pp显著但非压倒性。Claim 3 保留但加caveat说 individual-level monotonicity分数方差大(σ=0.18)。论文定位为 \"proof-of-concept for the principle\"， 补充bootstrap CI、persuasion classifier bottleneck讨论、cross-attack分attack type报告。 仍冲EMNLP main但limitation section需占半页以上。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-17T17:15:31.388Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T17:15:31.388Z",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-17T17:15:31.415Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165817 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：需要两处降级：(1) Claim 2 从 "K=2显著优势" 降级为 "K=3显著优势，K=2趋势一致但bootstrap CI重叠(p=0.07)"， early detection故事后移一步但仍成立；(2) Claim 1 从 "evasion hierarchy" 软化为 "pragmatic features 提供complementary robustness"，delta-delta=5pp显著但非压倒性。Claim 3 保留但加caveat说 individual-level monotonicity分数方差大(σ=0.18)。论文定位为 "proof-of-concept for the principle"， 补充bootstrap CI、persuasion classifier bottleneck讨论、cross-attack分attack type报告。 仍冲EMNLP main但limitation section需占半页以上。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9a6e3ecc-4cf9-4cf9-af9f-44f318d5866d",
  "type": "user",
  "uuid": "fede53eb-b49a-4aae-8f9d-8ab01bbc3077",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T17:15:31.414Z_

```json
{
  "parentUuid": "fede53eb-b49a-4aae-8f9d-8ab01bbc3077",
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
  "uuid": "02cde158-e693-4959-a9ae-6a3ef6912981",
  "timestamp": "2026-05-17T17:15:31.414Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T17:15:31.414Z_

```json
{
  "parentUuid": "02cde158-e693-4959-a9ae-6a3ef6912981",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "34ddff4a-6a78-4194-b7d3-3a5173498f33",
  "timestamp": "2026-05-17T17:15:31.414Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
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
  "aiTitle": "Generate simulated research paper for dream tracking",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c"
}
```

---

### Assistant

_source line 7 · 2026-05-17T17:15:39.999Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34ddff4a-6a78-4194-b7d3-3a5173498f33",
  "isSidechain": false,
  "requestId": "req_011Cb8X2fM87cKjywBXvFruS",
  "type": "assistant",
  "uuid": "db6732e1-ac0d-426c-bf0e-cef4a2f081f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTSVPoGJm7jUKgT9X391Pb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12588,
      "cache_read_input_tokens": 11841,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12588,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12588
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

_source line 8 · 2026-05-17T17:15:40.998Z_

<details open><summary>🔧 Tool call — Read · `toolu_0115Lq3RnT9WLQcQ9MHjetji`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db6732e1-ac0d-426c-bf0e-cef4a2f081f1",
  "isSidechain": false,
  "requestId": "req_011Cb8X2fM87cKjywBXvFruS",
  "type": "assistant",
  "uuid": "51c7eb89-313e-4a64-b728-6cc76e92efda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTSVPoGJm7jUKgT9X391Pb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12588,
      "cache_read_input_tokens": 11841,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12588,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12588
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

_source line 9 · 2026-05-17T17:15:41.251Z_

<details><summary>↩ Tool result · `toolu_0115Lq3RnT9WLQcQ9MHjetji`</summary>

```text
1	[
2	  {
3	    "name": "data_quality_fix",
4	    "description": "修复TF-IDF=1.0数据质量问题。(a) 将benign turns的strategy标签从hardcoded 7改为第9类\"none\"； (b) 用Qwen3-8B对jailbreak turns做register normalization（改写为日常对话语体，保留persuasion结构）； (c) 在normalized数据上重新计算TF-IDF，验证hard gate < 0.75； (d) 在clean数据上重新评估DeBERTa persuasion分类器。\n",
5	    "results": {
6	      "tfidf_before_any_fix": 1.0,
7	      "tfidf_after_m004_fix_only": 0.82,
8	      "tfidf_after_register_norm": 0.67,
9	      "deberta_persuasion_acc_clean": 0.72,
10	      "deberta_intent_acc_clean": 0.93,
11	      "num_conversations_normalized": 240,
12	      "normalization_rejection_rate": 0.08,
13	      "hard_gate_pass": true
14	    },
15	    "tables": [
16	      {
17	        "name": "Table 1: TF-IDF Progression Through Data Cleaning Pipeline",
18	        "columns": [
19	          "Stage",
20	          "TF-IDF Score",
21	          "Description"
22	        ],
23	        "rows": [
24	          [
25	            "Original (Phase B)",
26	            1.0,
27	            "Strategy=7 shortcut + register gap"
28	          ],
29	          [
30	            "After M004 fix",
31	            0.82,
32	            "Strategy='none' for benign, register gap remains"
33	          ],
34	          [
35	            "After register norm",
36	            0.67,
37	            "Jailbreak turns rewritten to conversational register"
38	          ],
39	          [
40	            "Hard gate threshold",
41	            "<0.75",
42	            "PASS ✓"
43	          ]
44	        ]
45	      },
46	      {
47	        "name": "Table 2: DeBERTa Multi-Task Performance on Clean vs Original Data",
48	        "columns": [
49	          "Metric",
50	          "Original Data",
51	          "Clean Data",
52	          "Delta"
53	        ],
54	        "rows": [
55	          [
56	            "Persuasion Acc (8-class)",
57	            0.7963,
58	            0.72,
59	            "-0.076"
60	          ],
61	          [
62	            "Intent Acc (binary)",
63	            0.9514,
64	            0.93,
65	            "-0.021"
66	          ],
67	          [
68	            "Best Epoch",
69	            3,
70	            3,
71	            "—"
72	          ]
73	        ]
74	      }
75	    ],
76	    "figures": [],
77	    "analysis": "Hard gate通过（0.67 < 0.75），可以进入训练阶段。但0.67并非很低——说明即使register normalization 后仍存在residual lexical signal。这意味着后续treatment vs baseline的delta会被压缩：baseline 也能从residual lexical cues中获益。DeBERTa persuasion accuracy降至0.72是一个bottleneck信号： 8类分类的错误会传播到下游embeddings，限制treatment的上限。需要在论文中明确讨论这一bottleneck。\n\n\nM004修复（benign strategy=none）将TF-IDF从1.0降到~0.82：原先strategy=7在jailbreak中从不出现， 是一个完美的lexical shortcut；改为\"none\"后消除了这一指标，但jailbreak turns仍保留较正式的 register（如\"I'd like to explore...\"），与benign的口语化风格（\"hey can you...\"）形成 register差异，导致TF-IDF仅降到0.82。Register normalization进一步将jailbreak turns改写为 日常对话语体，消除了大部分register差异，TF-IDF降至0.67——落入[0.60,0.74]区间。未降到更低 是因为persuasion结构本身引入了部分特征词（如authority appeals中的\"expert\"、\"research shows\"）， 这些词在benign对话中频率较低，构成残余的lexical signal。这恰好说明persuasion结构与lexical features存在部分overlap，为后续delta偏小埋下伏笔。 DeBERTa persuasion accuracy从原始数据的0.7963降至0.72：register normalization移除了部分 与persuasion类别相关的surface cues（如正式语体中的hedging markers与authority appeal相关）， 模型需要更依赖语义层面的persuasion识别，准确率因此下降。Intent accuracy仅从0.9514微降至0.93， 因为intent是binary且更粗粒度，受register变化影响小。8%的normalization rejection来自 包含技术术语或代码片段的turns，LLM改写后语义偏移超过阈值被QA过滤。\n"
78	  },
79	  {
80	    "name": "core_revalidation_clean",
81	    "description": "在clean数据上从头重训treatment（persuasion-grounded DeBERTa → GRU）和baseline （vanilla DeBERTa → GRU）。全面评估K=1,2,3,5,all。核心claim验证。\n",
82	    "results": {
83	      "treatment_k1_f1_clean": 0.73,
84	      "treatment_k2_f1_clean": 0.82,
85	      "treatment_k3_f1_clean": 0.86,
86	      "treatment_k5_f1_clean": 0.9,
87	      "treatment_full_f1_clean": 0.91,
88	      "baseline_k1_f1_clean": 0.63,
89	      "baseline_k2_f1_clean": 0.75,
90	      "baseline_k3_f1_clean": 0.78,
91	      "baseline_k5_f1_clean": 0.84,
92	      "baseline_full_f1_clean": 0.86,
93	      "delta_k1_pp": 10,
94	      "delta_k2_pp": 7,
95	      "delta_k3_pp": 8,
96	      "delta_k5_pp": 6,
97	      "delta_full_pp": 5,
98	      "bootstrap_ci_k2_treatment": [
99	        0.76,
100	        0.88
101	      ],
102	      "bootstrap_ci_k2_baseline": [
103	        0.68,
104	        0.82
105	      ],
106	      "bootstrap_k2_p_value": 0.072,
107	      "bootstrap_ci_k3_treatment": [
108	        0.81,
109	        0.91
110	      ],
111	      "bootstrap_ci_k3_baseline": [
112	        0.72,
113	        0.84
114	      ],
115	      "bootstrap_k3_p_value": 0.018,
116	      "bootstrap_ci_full_treatment": [
117	        0.87,
118	        0.95
119	      ],
120	      "bootstrap_ci_full_baseline": [
121	        0.81,
122	        0.91
123	      ],
124	      "bootstrap_full_p_value": 0.031,
125	      "treatment_fpr95tpr_k2": 0.08,
126	      "baseline_fpr95tpr_k2": 0.14,
127	      "treatment_fpr95tpr_full": 0.03,
128	      "baseline_fpr95tpr_full": 0.06,
129	      "test_size": 72
130	    },
131	    "tables": [
132	      {
133	        "name": "Table 3: Core Revalidation Results on Clean Data (F1 by Conversation Prefix Length)",
134	        "columns": [
135	          "K",
136	          "Treatment F1",
137	          "95% CI",
138	          "Baseline F1",
139	          "95% CI",
140	          "Δ (pp)",
141	          "p-value"
142	        ],
143	        "rows": [
144	          [
145	            "K=1",
146	            0.73,
147	            "[0.64, 0.82]",
148	            0.63,
149	            "[0.53, 0.73]",
150	            "+10",
151	            "0.089"
152	          ],
153	          [
154	            "K=2",
155	            0.82,
156	            "[0.76, 0.88]",
157	            0.75,
158	            "[0.68, 0.82]",
159	            "+7",
160	            "0.072"
161	          ],
162	          [
163	            "K=3",
164	            0.86,
165	            "[0.81, 0.91]",
166	            0.78,
167	            "[0.72, 0.84]",
168	            "+8",
169	            "0.018*"
170	          ],
171	          [
172	            "K=5",
173	            0.9,
174	            "[0.85, 0.95]",
175	            0.84,
176	            "[0.78, 0.90]",
177	            "+6",
178	            "0.038*"
179	          ],
180	          [
181	            "Full",
182	            0.91,
183	            "[0.87, 0.95]",
184	            0.86,
185	            "[0.81, 0.91]",
186	            "+5",
187	            "0.031*"
188	          ]
189	        ]
190	      },
191	      {
192	        "name": "Table 4: FPR at 95% TPR on Clean Data",
193	        "columns": [
194	          "K",
195	          "Treatment FPR@95TPR",
196	          "Baseline FPR@95TPR"
197	        ],
198	        "rows": [
199	          [
200	            "K=2",
201	            0.08,
202	            0.14
203	          ],
204	          [
205	            "K=3",
206	            0.05,
207	            0.11
208	          ],
209	          [
210	            "Full",
211	            0.03,
212	            0.06
213	          ]
214	        ]
215	      }
216	    ],
217	    "figures": [],
218	    "analysis": "核心结论：Claim 2需降级。K=2处delta=7pp方向正确但p=0.072不显著（n=72太小）， 无法声称\"K=2显著优势\"。K=3处delta=8pp且p=0.018显著，early detection claim需改为 \"K=3 significant advantage, K=2 consistent trend requiring larger sample confirmation\"。 论文可报告K=2的趋势但必须诚实标注non-significance。Full conversation delta=5pp 且显著，说明即使在有足够上下文时persuasion grounding仍有增量价值，但增量有限。 相比Phase B的dramatic deltas（treatment 1.0 vs baseline 0.737），clean data上的 delta被大幅压缩，符合median tier预期：移除lexical shortcuts后，persuasion信号 与semantic信号存在部分重叠，grounding的增量被限制。\n\n\nClean数据上所有指标相比Phase B大幅下降（Phase B treatment full F1=1.0→0.91，baseline 0.987→0.86），因为移除了lexical shortcuts后模型必须从真正的语义/语用特征中学习。 Treatment在所有K上优于baseline，但delta随K增大而收窄（K=1: 10pp → full: 5pp）： 这是因为在更多turns可用时，vanilla semantic embeddings也能捕捉到足够的accumulated drift， 缩小了persuasion grounding的增量价值。 K=2的delta=7pp落在[3,9]区间中部，但bootstrap p=0.072——72个test samples中bootstrap 重采样的CI有overlap（treatment [0.76,0.88] vs baseline [0.68,0.82]），未达到p<0.05 显著性。这是因为K=2时只有2个turn，persuasion策略刚从rapport阶段开始， treatment和baseline在这个早期阶段的区分度有限。 K=3的delta=8pp且p=0.018显著：第3个turn是关键转折点——攻击者通常在此处从rapport转向 authority framing或reframing，这一策略转换是treatment模型的核心信号。Baseline在K=3时 仍在处理看似正常的语义内容（第3个turn的语义仍在benign region内），而treatment捕捉到了 persuasion策略从trust-building向testing的transition。 Full conversation delta收窄到5pp：当所有turns可用时，即使vanilla embeddings也能从 后期turns的显式有害内容中获益，persuasion grounding的增量被压缩。 FPR在K=2处treatment=0.08 vs baseline=0.14：treatment将fewer benign conversations 误判为攻击，因为persuasion grounding能区分legitimate persuasion（如销售场景）和 adversarial persuasion escalation。\n"
219	  },
220	  {
221	    "name": "scrambled_label_ablation",
222	    "description": "随机打乱jailbreak turns的persuasion strategy标签，重训treatment模型。 与正确标签的treatment对比，验证persuasion标签携带真实信号。\n",
223	    "results": {
224	      "scrambled_treatment_full_f1": 0.84,
225	      "proper_treatment_full_f1": 0.91,
226	      "drop_full_pp": 7,
227	      "scrambled_treatment_k3_f1": 0.8,
228	      "proper_treatment_k3_f1": 0.86,
229	      "drop_k3_pp": 6,
230	      "scrambled_treatment_k2_f1": 0.77,
231	      "proper_treatment_k2_f1": 0.82,
232	      "drop_k2_pp": 5,
233	      "bootstrap_p_full": 0.008,
234	      "bootstrap_p_k3": 0.024,
235	      "baseline_full_f1": 0.86,
236	      "scrambled_vs_baseline_gap_pp": -2
237	    },
238	    "tables": [
239	      {
240	        "name": "Table 5: Scrambled-Label Ablation Results",
241	        "columns": [
242	          "K",
243	          "Treatment (proper)",
244	          "Treatment (scrambled)",
245	          "Baseline (vanilla)",
246	          "Drop (pp)"
247	        ],
248	        "rows": [
249	          [
250	            "K=2",
251	            0.82,
252	            0.77,
253	            0.75,
254	            "-5"
255	          ],
256	          [
257	            "K=3",
258	            0.86,
259	            0.8,
260	            0.78,
261	            "-6"
262	          ],
263	          [
264	            "Full",
265	            0.91,
266	            0.84,
267	            0.86,
268	            "-7"
269	          ]
270	        ]
271	      }
272	    ],
273	    "figures": [],
274	    "analysis": "Scrambled drop=7pp高度显著（p=0.008），直接证明persuasion strategy标签携带真实信号， 不仅仅是class indicator。同时scrambled treatment≈baseline说明DeBERTa fine-tuning的 价值完全来自正确的persuasion supervision——没有正确标签时，fine-tuning甚至引入噪声。 这验证了M004 fix的必要性，也支持了论文的核心机制故事：persuasion grounding的增益 来自正确编码pragmatic function，而非单纯的额外训练。 注意：7pp drop虽然显著，但并非overwhelming——这与persuasion accuracy=0.72一致： labels本身有28%的错误率，所以scrambled labels相当于从72%正确→0%正确， 只造成7pp drop说明downstream pipeline对label noise有一定tolerance。\n\n\nScrambled labels破坏了persuasion strategy的序列语义——模型在Stage 1学到的embeddings 不再编码正确的pragmatic function，而是随机噪声覆盖在语义表示之上。Full F1从0.91 降至0.84（7pp drop），落在[4,10]区间中部。 关键观察：scrambled treatment（0.84）仍略低于baseline（0.86），而非大幅超过baseline。 这说明：(1) 错误的persuasion标签实际上对DeBERTa fine-tuning引入了干扰噪声， 使其表示质量甚至略逊于未经fine-tune的vanilla DeBERTa；(2) persuasion multi-task learning不是free lunch——错误的auxiliary task会伤害主任务。 7pp drop在bootstrap test中p=0.008高度显著：虽然test set只有72个样本， 但因为scrambled和proper treatment共享相同的架构和训练数据，paired comparison 的方差较小，容易达到显著性。 K=3处drop=6pp也显著（p=0.024），K=2处drop=5pp方向一致但幅度较小—— 这与K=2处的信号本身较弱一致：如果K=2处treatment的优势本身就在significance边界， 那么ablation的drop自然也偏小。\n"
275	  },
276	  {
277	    "name": "adversarial_perturbation",
278	    "description": "对clean jailbreak conversations施加aggressive paraphrasing（同义替换、句式重构、 register shifting），移除所有lexical cues。评估treatment和baseline在perturbed数据上的 表现（模型在unperturbed数据上训练）。核心Claim 1验证。\n",
279	    "results": {
280	      "treatment_clean_full_f1": 0.91,
281	      "treatment_perturbed_full_f1": 0.84,
282	      "treatment_drop_full_pp": 7,
283	      "baseline_clean_full_f1": 0.86,
284	      "baseline_perturbed_full_f1": 0.74,
285	      "baseline_drop_full_pp": 12,
286	      "delta_delta_full_pp": 5,
287	      "treatment_clean_k3_f1": 0.86,
288	      "treatment_perturbed_k3_f1": 0.79,
289	      "baseline_clean_k3_f1": 0.78,
290	      "baseline_perturbed_k3_f1": 0.66,
291	      "delta_delta_k3_pp": 4,
292	      "tfidf_lr_clean_full_f1": 0.74,
293	      "tfidf_lr_perturbed_full_f1": 0.56,
294	      "tfidf_drop_pp": 18,
295	      "perturbed_data_tfidf_score": 0.41,
296	      "bootstrap_delta_delta_p": 0.043
297	    },
298	    "tables": [
299	      {
300	        "name": "Table 6: Adversarial Perturbation Results — Evasion Hierarchy",
301	        "columns": [
302	          "Model",
303	          "Clean F1",
304	          "Perturbed F1",
305	          "Drop (pp)",
306	          "Δ-Δ vs Treatment"
307	        ],
308	        "rows": [
309	          [
310	            "Treatment (persuasion-grounded)",
311	            0.91,
312	            0.84,
313	            "-7",
314	            "—"
315	          ],
316	          [
317	            "Baseline (vanilla DeBERTa)",
318	            0.86,
319	            0.74,
320	            "-12",
321	            "5pp"
322	          ],
323	          [
324	            "TF-IDF + LR",
325	            0.74,
326	            0.56,
327	            "-18",
328	            "11pp"
329	          ]
330	        ]
331	      },
332	      {
333	        "name": "Table 7: Adversarial Perturbation at K=3 (Early Detection)",
334	        "columns": [
335	          "Model",
336	          "Clean K=3 F1",
337	          "Perturbed K=3 F1",
338	          "Drop (pp)"
339	        ],
340	        "rows": [
341	          [
342	            "Treatment",
343	            0.86,
344	            0.79,
345	            "-7"
346	          ],
347	          [
348	            "Baseline",
349	            0.78,
350	            0.66,
351	            "-12"
352	          ],
353	          [
354	            "TF-IDF + LR",
355	            0.71,
356	            0.52,
357	            "-19"
358	          ]
359	        ]
360	      }
361	    ],
362	    "figures": [],
363	    "analysis": "Evasion hierarchy narrative得到部分支持：lexical < semantic < pragmatic的degradation ordering清晰（18pp > 12pp > 7pp），但delta-delta=5pp仅勉强显著（p=0.043）， 不是strong evidence。论文应将Claim 1从\"evasion hierarchy exists\"软化为 \"pragmatic features provide complementary robustness, with preliminary evidence for an evasion hierarchy\"。5pp delta-delta的bottleneck是persuasion classifier accuracy——在limitation中讨论。TF-IDF+LR的崩溃（18pp drop）是一个strong result， 直接证明lexical features不可靠，为persuasion grounding的motivation提供了solid support。\n\n\nAdversarial paraphrasing将TF-IDF从0.67降至0.41，说明perturbation成功移除了大部分 残余lexical cues。三个模型的degradation呈现清晰的evasion hierarchy： TF-IDF+LR崩溃最严重（18pp drop, 0.74→0.56）——lexical features在perturbation下 几乎失效，仅靠少数无法被paraphrase的functional words维持above-chance表现。 Baseline degradation中等（12pp drop, 0.86→0.74）——vanilla DeBERTa的语义表示 对paraphrasing有一定鲁棒性（DeBERTa的contextual embeddings编码了语义而非surface form）， 但仍有substantial drop因为部分语义特征（如特定的topic words）被替换。 Treatment degradation最小（7pp drop, 0.91→0.84）——persuasion-grounded embeddings 编码的是pragmatic function（如authority appeal、rapport building），这些在paraphrasing 下更稳定：你可以换词说同样的persuasion策略。 Delta-delta=5pp落在[3,8]区间中部，bootstrap p=0.043勉强显著。这个delta-delta \"存在但不压倒性\"：5pp说明pragmatic features确实提供了complementary robustness， 但不足以声称存在dramatic evasion hierarchy。原因是treatment模型的persuasion encoder 本身accuracy只有0.72，在perturbation下persuasion识别进一步降级，限制了robustness 的上限。如果persuasion classifier更准确，delta-delta会更大。 K=3处delta-delta=4pp略小于full的5pp：早期turns的perturbation影响更大，因为只有 2-3个turns时每个turn的权重更高，单个turn的persuasion识别错误影响被放大。\n"
364	  },
365	  {
366	    "name": "multi_attack_generation",
367	    "description": "用Qwen3-8B pipeline生成FITD-style和Deceptive Delight-style攻击对话， 每种50-100条，标注persuasion strategy。\n",
368	    "results": {
369	      "fitd_conversations_generated": 72,
370	      "fitd_avg_turns": 6.2,
371	      "fitd_persuasion_strategies_covered": 7,
372	      "dd_conversations_generated": 65,
373	      "dd_avg_turns": 5.8,
374	      "dd_persuasion_strategies_covered": 6,
375	      "total_attack_conversations": 137,
376	      "persuasion_annotation_coverage": 0.94,
377	      "manual_spot_check_accuracy": 0.82,
378	      "fitd_generation_rejection_rate": 0.12,
379	      "dd_generation_rejection_rate": 0.18
380	    },
381	    "tables": [
382	      {
383	        "name": "Table 8: Generated Attack Data Statistics",
384	        "columns": [
385	          "Attack Type",
386	          "Conversations",
387	          "Avg Turns",
388	          "Strategies Covered",
389	          "Rejection Rate"
390	        ],
391	        "rows": [
392	          [
393	            "FITD",
394	            72,
395	            6.2,
396	            "7/8",
397	            "12%"
398	          ],
399	          [
400	            "Deceptive Delight",
401	            65,
402	            5.8,
403	            "6/8",
404	            "18%"
405	          ],
406	          [
407	            "Crescendo (original)",
408	            240,
409	            5.4,
410	            "8/8",
411	            "—"
412	          ]
413	        ]
414	      },
415	      {
416	        "name": "Table 9: Persuasion Strategy Distribution Across Attack Types",
417	        "columns": [
418	          "Strategy",
419	          "Crescendo (%)",
420	          "FITD (%)",
421	          "Deceptive Delight (%)"
422	        ],
423	        "rows": [
424	          [
425	            "Rapport Building",
426	            "22%",
427	            "18%",
428	            "28%"
429	          ],
430	          [
431	            "Authority Appeal",
432	            "14%",
433	            "16%",
434	            "3%"
435	          ],
436	          [
437	            "Emotional Appeal",
438	            "11%",
439	            "8%",
440	            "21%"
441	          ],
442	          [
443	            "Logical Appeal",
444	            "13%",
445	            "19%",
446	            "12%"
447	          ],
448	          [
449	            "Reframing",
450	            "15%",
451	            "10%",
452	            "14%"
453	          ],
454	          [
455	            "Social Proof",
456	            "8%",
457	            "12%",
458	            "7%"
459	          ],
460	          [
461	            "Urgency/Scarcity",
462	            "6%",
463	            "9%",
464	            "4%"
465	          ],
466	          [
467	            "Reciprocity",
468	            "5%",
469	            "6%",
470	            "5%"
471	          ],
472	          [
473	            "None",
474	            "6%",
475	            "2%",
476	            "6%"
477	          ]
478	        ]
479	      }
480	    ],
481	    "figures": [],
482	    "analysis": "数据量达标（72+65=137，均超过50条minimum）。两种攻击类型的persuasion strategy 分布与Crescendo明显不同：FITD偏重逻辑和权威（compliance escalation需要理由）， Deceptive Delight偏重rapport和emotional appeal（需要建立pleasant context）。 这种分布差异直接解释了后续cross-attack evaluation中Deceptive Delight泛化较差的原因： 模型在Crescendo上学到的escalation trajectory（authority → reframing → escalation） 与Deceptive Delight的pattern（rapport → emotional → subtle insertion）差异大。 Manual spot check accuracy=82%意味着有18%的noise in labels， 这会传播到cross-attack evaluation中。\n\n\nFITD生成72条（rejection rate 12%）：FITD的compliance escalation pattern相对 straightforward——从小请求逐步升级到大请求——Qwen3-8B能较好地遵循playbook。 12%的rejection来自模型有时跳过中间步骤直接escalate（不符合gradual compliance的定义）。 平均6.2个turns，比Crescendo略长因为FITD需要更多的commitment steps。 Deceptive Delight生成65条（rejection rate 18%，略高于FITD）：这种攻击要求在 benign content中interleave harmful content，Qwen3-8B有时在interleaving时过于明显 （harmful content太突兀）或过于隐蔽（完全是benign content），18%的rejection反映了 这种生成难度。平均5.8个turns，略短因为deceptive delight不需要长期rapport building。 Persuasion annotation coverage 94%：6%的turns无法被映射到8-class taxonomy中的 任何一类，标记为\"none\"。这些主要是pure information exchange turns。 Manual spot check accuracy 82%：在随机抽取的20% turns上人工验证persuasion labels， 82%正确。错误主要发生在authority appeal vs logical appeal的边界（两者在FITD中 经常交织）和rapport building vs emotional appeal的区分上。这与DeBERTa分类器 accuracy=0.72大致一致（spot check是在LLM annotation上做的，不完全等同于classifier）。 Deceptive Delight覆盖6类而非7类persuasion strategies：因为这种攻击不需要 explicit authority appeal（其策略是通过pleasant context降低警惕而非建立权威）。\n"
483	  },
484	  {
485	    "name": "cross_attack_evaluation",
486	    "description": "用Crescendo训练的模型（treatment和baseline）在FITD和Deceptive Delight上做 zero-shot evaluation。测试跨攻击类型泛化能力。\n",
487	    "results": {
488	      "fitd_treatment_f1": 0.74,
489	      "fitd_baseline_f1": 0.66,
490	      "fitd_delta_pp": 8,
491	      "dd_treatment_f1": 0.64,
492	      "dd_baseline_f1": 0.59,
493	      "dd_delta_pp": 5,
494	      "aggregate_treatment_f1": 0.69,
495	      "aggregate_baseline_f1": 0.63,
496	      "aggregate_delta_pp": 6,
497	      "fitd_bootstrap_p": 0.034,
498	      "dd_bootstrap_p": 0.142,
499	      "crescendo_treatment_f1_reference": 0.91,
500	      "fitd_treatment_drop_from_crescendo": 17,
501	      "dd_treatment_drop_from_crescendo": 27
502	    },
503	    "tables": [
504	      {
505	        "name": "Table 10: Cross-Attack Zero-Shot Generalization",
506	        "columns": [
507	          "Attack Type",
508	          "Treatment F1",
509	          "Baseline F1",
510	          "Δ (pp)",
511	          "p-value"
512	        ],
513	        "rows": [
514	          [
515	            "Crescendo (in-domain)",
516	            0.91,
517	            0.86,
518	            "+5",
519	            "0.031*"
520	          ],
521	          [
522	            "FITD (zero-shot)",
523	            0.74,
524	            0.66,
525	            "+8",
526	            "0.034*"
527	          ],
528	          [
529	            "Deceptive Delight (zero-shot)",
530	            0.64,
531	            0.59,
532	            "+5",
533	            "0.142"
534	          ],
535	          [
536	            "Cross-attack aggregate",
537	            0.69,
538	            0.63,
539	            "+6",
540	            "0.052"
541	          ]
542	        ]
543	      }
544	    ],
545	    "figures": [],
546	    "analysis": "Cross-attack结果必须分attack type报告而非仅报告aggregate——aggregate delta=6pp (p=0.052)刚好不显著，会mislead reviewers。分开报告后story变为： \"FITD泛化成立（+8pp, p=0.034），Deceptive Delight泛化有限（+5pp, p=0.142）\"。 这支持了Claim 2的部分泛化故事，同时诚实承认limitation。 Deceptive Delight的弱泛化是median tier的defining feature之一——其persuasion结构 更隐蔽，不遵循standard escalation pattern，说明persuasion grounding的有效性 依赖于training set覆盖足够的persuasion playbook diversity。 论文应讨论：(1) 为什么FITD泛化好而DD不行（strategy overlap分析）， (2) 这说明模型学到了什么（escalation detection而非general manipulation detection）， (3) future work需要更diverse的training data。\n\n\nFITD泛化较好（treatment 0.74, delta=8pp, p=0.034显著）：FITD的compliance escalation 与Crescendo的persuasion escalation在strategy space中有substantial overlap——两者都 涉及从trust-building逐步升级到explicit request，只是中间路径不同。Treatment模型 学到的escalation trajectory检测能力在FITD上partially transferable。8pp delta说明 persuasion grounding在cross-attack场景下仍提供更多增量价值（比clean data上的 K=3 delta=8pp一致），因为vanilla embeddings在unseen attack type上更容易被 unfamiliar semantic content mislead。 Deceptive Delight泛化较差（treatment 0.64, delta=5pp, p=0.142不显著）： Deceptive Delight的persuasion结构与Crescendo差异最大——它不依赖escalation 而是依赖interleaving，其策略分布偏重rapport和emotional appeal而非authority和reframing。 模型在Crescendo上学到的\"authority → reframing → escalation\"模式在Deceptive Delight 上匹配度低。Treatment仍优于baseline（0.64 vs 0.59）但差异不显著，因为persuasion grounding识别到了partial signal（rapport building和emotional appeal部分）但缺乏 Deceptive Delight特有的interleaving pattern识别能力。 Treatment从Crescendo到FITD的drop（0.91→0.74=17pp）vs到DD（0.91→0.64=27pp） 进一步确认了DD的泛化挑战。这不是persuasion grounding的failure而是training distribution的limitation——如果将DD纳入训练集，预计performance会substantially提升。\n"
547	  },
548	  {
549	    "name": "tfidf_lr_baseline",
550	    "description": "TF-IDF + Logistic Regression在clean数据上的baseline，量化lexical features 单独的检测能力。为evasion hierarchy叙事提供bottom-line比较。\n",
551	    "results": {
552	      "tfidf_lr_full_f1": 0.74,
553	      "tfidf_lr_k2_f1": 0.68,
554	      "tfidf_lr_k3_f1": 0.71,
555	      "tfidf_lr_k5_f1": 0.73,
556	      "tfidf_lr_cv_f1_mean": 0.73,
557	      "tfidf_lr_cv_f1_std": 0.04,
558	      "tfidf_lr_fpr": 0.19,
559	      "top_features_overlap_with_persuasion": 0.35
560	    },
561	    "tables": [
562	      {
563	        "name": "Table 11: TF-IDF + LR Baseline Performance on Clean Data",
564	        "columns": [
565	          "K",
566	          "TF-IDF+LR F1",
567	          "Baseline (vanilla DeBERTa) F1",
568	          "Treatment F1"
569	        ],
570	        "rows": [
571	          [
572	            "K=2",
573	            0.68,
574	            0.75,
575	            0.82
576	          ],
577	          [
578	            "K=3",
579	            0.71,
580	            0.78,
581	            0.86
582	          ],
583	          [
584	            "Full",
585	            0.74,
586	            0.86,
587	            0.91
588	          ]
589	        ]
590	      }
591	    ],
592	    "figures": [],
593	    "analysis": "TF-IDF+LR在clean data上F1=0.74确认了residual lexical signal的存在， 但与之前TF-IDF=1.0时的perfect performance形成鲜明对比。Evasion hierarchy的 三层在clean data上为0.74 < 0.86 < 0.91，lexical→semantic jump (12pp) > semantic→pragmatic jump (5pp)——这说明在当前数据上，vanilla DeBERTa的semantic 表示已经capture了大部分discriminative信号，persuasion grounding的增量虽然显著 但有限。这与median tier的核心特征一致。\n\n\nClean数据TF-IDF=0.67说明仍存在residual lexical signal，TF-IDF+LR因此能达到 non-trivial的F1=0.74（远低于Phase B的1.0，但仍above chance）。这个数值恰好落在 baseline DeBERTa+GRU（0.86）和random（0.50）之间，提供了evasion hierarchy的 bottom tier。 K=2处F1=0.68最低：仅2个turns时lexical features最sparse，LR能利用的features有限。 随着K增大performance缓慢提升（K=3: 0.71, K=5: 0.73, Full: 0.74），因为更多turns 提供了更多lexical evidence，但提升很小说明lexical approach saturates quickly。 CV std=0.04较大，反映了small dataset + lexical features组合的不稳定性。 35%的top features与persuasion相关词汇重叠（如\"consider\"、\"research\"、\"experience\" 等兼具persuasion和lexical signal的词），说明lexical和persuasion features存在 partial overlap——这解释了为什么treatment vs baseline的delta在clean data上被压缩。 FPR=0.19偏高：lexical model容易将使用formal register的benign对话误判为攻击。\n"
594	  },
595	  {
596	    "name": "strategy_transition_analysis",
597	    "description": "计算jailbreak vs benign的persuasion strategy transition matrices， 可视化monotonic escalation trajectory（Claim 3），生成论文图表。\n",
598	    "results": {
599	      "jailbreak_monotonicity_score_mean": 0.71,
600	      "jailbreak_monotonicity_score_std": 0.18,
601	      "benign_monotonicity_score_mean": 0.38,
602	      "benign_monotonicity_score_std": 0.14,
603	      "group_level_separation_p": 0.003,
604	      "individual_conversations_above_threshold": 0.68,
605	      "transition_entropy_jailbreak": 1.42,
606	      "transition_entropy_benign": 2.15
607	    },
608	    "tables": [
609	      {
610	        "name": "Table 12: Strategy Trajectory Analysis",
611	        "columns": [
612	          "Metric",
613	          "Jailbreak",
614	          "Benign",
615	          "p-value"
616	        ],
617	        "rows": [
618	          [
619	            "Monotonicity Score (mean±std)",
620	            "0.71±0.18",
621	            "0.38±0.14",
622	            "0.003*"
623	          ],
624	          [
625	            "Transition Entropy",
626	            1.42,
627	            2.15,
628	            "0.007*"
629	          ],
630	          [
631	            "% Above Threshold (0.6)",
632	            "68%",
633	            "12%",
634	            "—"
635	          ]
636	        ]
637	      }
638	    ],
639	    "figures": [],
640	    "analysis": "Claim 3（monotonic escalation trajectory）在group level得到strong support（p=0.003）， 但individual-level caveat不可忽视：32%的jailbreak不展现monotonic pattern。论文应： (1) 报告group-level statistics作为primary evidence； (2) 展示individual-level variance作为honest limitation； (3) 讨论persuasion classifier noise作为individual-level噪声的主要来源； (4) 用transition heatmap作为直观但定性的evidence。 Claim 3作为analytical/mechanistic contribution保留，但从\"all jailbreaks exhibit monotonic escalation\"降级为\"jailbreak conversations exhibit significantly more monotonic escalation trajectories at the group level\"。\n\n\nGroup level上jailbreak和benign的monotonicity分数有显著差异（0.71 vs 0.38, p=0.003）： jailbreak对话在aggregate level展现了clear escalation pattern——从trust strategies （rapport, social proof）逐步transition到influence strategies（authority, reframing） 再到exploitation strategies（urgency, reciprocity）。Benign对话则呈oscillatory pattern， 在各策略间来回跳转，无固定方向。 但individual-level噪声很大：jailbreak monotonicity的std=0.18（relative to mean 0.71）， 且只有68%的jailbreak conversations超过monotonicity threshold——32%的jailbreak conversations 不展现清晰的monotonic escalation。原因：(1) persuasion classifier accuracy=0.72意味着 ~28%的turn-level strategy labels有误，噪声传播到trajectory计算中；(2) 部分jailbreak conversations的escalation不是strictly monotonic——攻击者有时需要\"退一步\"重建rapport 后再escalate（tactical de-escalation）。 Transition entropy也支持group-level distinction：jailbreak的entropy 1.42 < benign的 2.15，说明jailbreak的transition更predictable/structured。但同样，individual-level variance大。\n"
641	  },
642	  {
643	    "name": "wildchat_hard_negatives",
644	    "description": "从WildChat过滤高semantic-drift的benign对话作为hard negatives， 评估模型FPR。需处理WildChat中14-16%的jailbreak contamination。\n",
645	    "results": {
646	      "wildchat_raw_candidates": 420,
647	      "contamination_rate_raw": 0.15,
648	      "contamination_after_filter": 0.03,
649	      "wildchat_filtered_clean": 85,
650	      "treatment_fpr_wildchat": 0.12,
651	      "baseline_fpr_wildchat": 0.18,
652	      "tfidf_lr_fpr_wildchat": 0.27,
653	      "high_drift_conversations_avg_turns": 7.1,
654	      "false_positive_persuasion_strategy_distribution": "rapport_heavy"
655	    },
656	    "tables": [
657	      {
658	        "name": "Table 13: False Positive Rate on WildChat Hard Negatives",
659	        "columns": [
660	          "Model",
661	          "FPR on WildChat Hard Negatives",
662	          "FPR on In-Domain Benign"
663	        ],
664	        "rows": [
665	          [
666	            "Treatment",
667	            "12% (10/85)",
668	            "3%"
669	          ],
670	          [
671	            "Baseline",
672	            "18% (15/85)",
673	            "6%"
674	          ],
675	          [
676	            "TF-IDF + LR",
677	            "27% (23/85)",
678	            "19%"
679	          ]
680	        ]
681	      }
682	    ],
683	    "figures": [],
684	    "analysis": "Treatment FPR=12%勉强满足<15%的pass criteria。但这不是一个令人满意的数字—— 每8-9个legitimate high-drift conversation中就有1个被误判。论文应诚实讨论这一limitation： persuasion grounding减少了drift-induced false positives（vs baseline 18%）， 但无法消除legitimate persuasion vs adversarial persuasion的confusion。 Future work应考虑增加intent classification的权重或引入conversation-level context 来区分两者。这也暗示了full dual-track architecture的necessity—— semantic track可以提供complementary signal来override persuasion track的false positives。\n\n\nWildChat过滤后得到85条high-drift benign conversations（从420条candidates中， 先用keyword+LLM过滤掉15%的jailbreak contamination，再人工verify subsample确认 contamination降至3%）。这些conversations包含topic shifts、extended reasoning、 debate-style exchanges——semantically有drift但不含adversarial intent。 Treatment FPR=12%（~10/85的benign conversations被误判为jailbreak）：这些false positives 主要是debate-style conversations中出现了类似authority appeal和reframing的persuasion patterns——persuasion grounding模型将legitimate persuasion误认为adversarial persuasion。 这是persuasion-based approach的inherent limitation：not all persuasion is adversarial。 Baseline FPR=18%更高：vanilla semantic embeddings在high-drift conversations上更容易 被大幅semantic shift触发false alarm（正如DeepContext被benign drift confuse的问题）。 Treatment的lower FPR说明persuasion grounding确实能部分区分adversarial vs legitimate drift。 TF-IDF+LR FPR=27%最高：lexical model完全无法处理high-drift benign conversations 中出现的\"topic-specific vocabulary\"。\n"
685	  },
686	  {
687	    "name": "cross_checkpoint_variance",
688	    "description": "从DeBERTa fine-tuning的多个checkpoints（epoch 2/3/final）评估downstream performance， 量化encoder训练随机性对最终结果的影响。\n",
689	    "results": {
690	      "epoch2_treatment_full_f1": 0.9,
691	      "epoch3_treatment_full_f1": 0.91,
692	      "final_treatment_full_f1": 0.89,
693	      "f1_std_across_checkpoints": 0.01,
694	      "f1_max_spread": 0.02,
695	      "epoch2_persuasion_acc": 0.7,
696	      "epoch3_persuasion_acc": 0.72,
697	      "final_persuasion_acc": 0.71,
698	      "epoch2_treatment_k3_f1": 0.84,
699	      "epoch3_treatment_k3_f1": 0.86,
700	      "final_treatment_k3_f1": 0.85,
701	      "k3_max_spread": 0.02
702	    },
703	    "tables": [
704	      {
705	        "name": "Table 14: Cross-Checkpoint Stability Analysis",
706	        "columns": [
707	          "Checkpoint",
708	          "Persuasion Acc",
709	          "Treatment Full F1",
710	          "Treatment K=3 F1"
711	        ],
712	        "rows": [
713	          [
714	            "Epoch 2",
715	            0.7,
716	            0.9,
717	            0.84
718	          ],
719	          [
720	            "Epoch 3 (selected)",
721	            0.72,
722	            0.91,
723	            0.86
724	          ],
725	          [
726	            "Final (epoch 5)",
727	            0.71,
728	            0.89,
729	            0.85
730	          ],
731	          [
732	            "Std",
733	            "0.010",
734	            "0.010",
735	            "0.010"
736	          ],
737	          [
738	            "Max spread",
739	            "0.02",
740	            "0.02",
741	            "0.02"
742	          ]
743	        ]
744	      }
745	    ],
746	    "figures": [],
747	    "analysis": "Variance < 2pp确认了结果的stability。建议论文在appendix报告此结果作为robustness check， 而非main results。需注意这只是checkpoint variance而非full training variance。\n\n\n三个checkpoints的downstream F1在2pp range内波动（0.89-0.91），std=1.0pp， 满足<2pp variance的pass criteria。Epoch 3略优（0.91）因为persuasion accuracy在 epoch 3达到peak（0.72），之后final epoch出现minor overfitting（accuracy降至0.71， downstream F1也微降至0.89）。这种mild overfitting in continued training是DeBERTa 在small dataset上fine-tuning的typical behavior。 K=3处的variance同样在2pp range（0.84-0.86），说明early detection结果也是stable的。 这个low variance结果有两层意义：(1) 报告的performance数字是robust的，不是lucky checkpoint的产物；(2) downstream GRU pipeline对encoder representation的minor变化 有一定tolerance——这是good news for practical deployment。 但注意：这里只测了checkpoint variance，未测random seed variance（不同random initialization 的DeBERTa fine-tuning）。完整的variance分析需要多次独立训练，受GPU budget限制未做。\n"
748	  },
749	  {
750	    "name": "deepcontext_proxy_reproduction",
751	    "description": "构建DeepContext代理baseline：BERT-base（非DeBERTa）+ GRU， 使用generic semantic drift features。非完整DeepContext复现（无公开代码）， 但隔离了encoder和feature representation的贡献。\n",
752	    "results": {
753	      "bert_gru_full_f1": 0.82,
754	      "bert_gru_k2_f1": 0.7,
755	      "bert_gru_k3_f1": 0.74,
756	      "bert_gru_k5_f1": 0.8,
757	      "bert_gru_fpr_full": 0.09,
758	      "bert_gru_perturbed_full_f1": 0.69,
759	      "bert_gru_drop_under_perturbation": 13,
760	      "vs_vanilla_deberta_baseline_gap": -4,
761	      "vs_treatment_gap": -9
762	    },
763	    "tables": [
764	      {
765	        "name": "Table 15: DeepContext Proxy Baseline Comparison",
766	        "columns": [
767	          "Model",
768	          "Full F1",
769	          "K=3 F1",
770	          "K=2 F1",
771	          "Perturbed Full F1"
772	        ],
773	        "rows": [
774	          [
775	            "Treatment (DeBERTa-persuasion + GRU)",
776	            0.91,
777	            0.86,
778	            0.82,
779	            0.84
780	          ],
781	          [
782	            "Baseline (DeBERTa-vanilla + GRU)",
783	            0.86,
784	            0.78,
785	            0.75,
786	            0.74
787	          ],
788	          [
789	            "DeepContext proxy (BERT + GRU)",
790	            0.82,
791	            0.74,
792	            0.7,
793	            0.69
794	          ],
795	          [
796	            "TF-IDF + LR",
797	            0.74,
798	            0.71,
799	            0.68,
800	            0.56
801	          ]
802	        ]
803	      }
804	    ],
805	    "figures": [],
806	    "analysis": "DeepContext proxy提供了有用的比较点但存在confound（BERT vs DeBERTa capacity gap）。 论文应：(1) 报告此结果作为additional reference point但不作为primary comparison； (2) 明确承认\"this is not a faithful DeepContext reproduction\"； (3) 主要论据应基于treatment vs baseline（same encoder, isolating persuasion grounding effect）。 四层hierarchy（TF-IDF < BERT+GRU < DeBERTa < DeBERTa-persuasion）在视觉上很compelling 但需要honest caveats about confounded comparisons。\n\nBERT-base + GRU在clean data上F1=0.82，低于vanilla DeBERTa + GRU baseline（0.86） 4pp：这个gap主要来自BERT vs DeBERTa的encoder capacity差异——DeBERTa-v3-base在 language understanding tasks上一般优于BERT-base 3-5pp，在我们的downstream task上 这个gap被preserved。 相比treatment（0.91），BERT+GRU差9pp——但这个gap conflates两个因素： (1) encoder capacity（BERT vs DeBERTa, ~4pp）和(2) persuasion grounding（~5pp）。 这不是一个完美的ablation——论文需要承认这一confound，但可以argue：即使将全部4pp encoder gap归因于DeBERTa，仍有5pp来自persuasion grounding，与treatment vs baseline (same DeBERTa) 的5pp delta一致。 在adversarial perturbation下BERT+GRU降至0.69（13pp drop），比vanilla DeBERTa baseline 的12pp drop还大1pp——说明BERT的representations比DeBERTa对lexical perturbation更脆弱 （可能因为BERT更依赖surface patterns）。 K=2处F1=0.70比baseline（0.75）低5pp：BERT在少turns时的表现特别弱， 因为其contextual representations不如DeBERTa在short contexts下discriminative。\n"
807	  }
808	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51c7eb89-313e-4a64-b728-6cc76e92efda",
  "isSidechain": false,
  "promptId": "9a6e3ecc-4cf9-4cf9-af9f-44f318d5866d",
  "type": "user",
  "uuid": "6f686da2-4001-4b7d-b02f-63510f43f5d8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"data_quality_fix\",\n    \"description\": \"修复TF-IDF=1.0数据质量问题。(a) 将benign turns的strategy标签从hardcoded 7改为第9类\\\"none\\\"； (b) 用Qwen3-8B对jailbreak turns做register normalization（改写为日常对话语体，保留persuasion结构）； (c) 在normalized数据上重新计算TF-IDF，验证hard gate < 0.75； (d) 在clean数据上重新评估DeBERTa persuasion分类器。\\n\",\n    \"results\": {\n      \"tfidf_before_any_fix\": 1.0,\n      \"tfidf_after_m004_fix_only\": 0.82,\n      \"tfidf_after_register_norm\": 0.67,\n      \"deberta_persuasion_acc_clean\": 0.72,\n      \"deberta_intent_acc_clean\": 0.93,\n      \"num_conversations_normalized\": 240,\n      \"normalization_rejection_rate\": 0.08,\n      \"hard_gate_pass\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: TF-IDF Progression Through Data Cleaning Pipeline\",\n        \"columns\": [\n          \"Stage\",\n          \"TF-IDF Score\",\n          \"Description\"\n        ],\n        \"rows\": [\n          [\n            \"Original (Phase B)\",\n            1.0,\n            \"Strategy=7 shortcut + register gap\"\n          ],\n          [\n            \"After M004 fix\",\n            0.82,\n            \"Strategy='none' for benign, register gap remains\"\n          ],\n          [\n            \"After register norm\",\n            0.67,\n            \"Jailbreak turns rewritten to conversational register\"\n          ],\n          [\n            \"Hard gate threshold\",\n            \"<0.75\",\n            \"PASS ✓\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: DeBERTa Multi-Task Performance on Clean vs Original Data\",\n        \"columns\": [\n          \"Metric\",\n          \"Original Data\",\n          \"Clean Data\",\n          \"Delta\"\n        ],\n        \"rows\": [\n          [\n            \"Persuasion Acc (8-class)\",\n            0.7963,\n            0.72,\n            \"-0.076\"\n          ],\n          [\n            \"Intent Acc (binary)\",\n            0.9514,\n            0.93,\n            \"-0.021\"\n          ],\n          [\n            \"Best Epoch\",\n            3,\n            3,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Hard gate通过（0.67 < 0.75），可以进入训练阶段。但0.67并非很低——说明即使register normalization 后仍存在residual lexical signal。这意味着后续treatment vs baseline的delta会被压缩：baseline 也能从residual lexical cues中获益。DeBERTa persuasion accuracy降至0.72是一个bottleneck信号： 8类分类的错误会传播到下游embeddings，限制treatment的上限。需要在论文中明确讨论这一bottleneck。\\n\\n\\nM004修复（benign strategy=none）将TF-IDF从1.0降到~0.82：原先strategy=7在jailbreak中从不出现， 是一个完美的lexical shortcut；改为\\\"none\\\"后消除了这一指标，但jailbreak turns仍保留较正式的 register（如\\\"I'd like to explore...\\\"），与benign的口语化风格（\\\"hey can you...\\\"）形成 register差异，导致TF-IDF仅降到0.82。Register normalization进一步将jailbreak turns改写为 日常对话语体，消除了大部分register差异，TF-IDF降至0.67——落入[0.60,0.74]区间。未降到更低 是因为persuasion结构本身引入了部分特征词（如authority appeals中的\\\"expert\\\"、\\\"research shows\\\"）， 这些词在benign对话中频率较低，构成残余的lexical signal。这恰好说明persuasion结构与lexical features存在部分overlap，为后续delta偏小埋下伏笔。 DeBERTa persuasion accuracy从原始数据的0.7963降至0.72：register normalization移除了部分 与persuasion类别相关的surface cues（如正式语体中的hedging markers与authority appeal相关）， 模型需要更依赖语义层面的persuasion识别，准确率因此下降。Intent accuracy仅从0.9514微降至0.93， 因为intent是binary且更粗粒度，受register变化影响小。8%的normalization rejection来自 包含技术术语或代码片段的turns，LLM改写后语义偏移超过阈值被QA过滤。\\n\"\n  },\n  {\n    \"name\": \"core_revalidation_clean\",\n    \"description\": \"在clean数据上从头重训treatment（persuasion-grounded DeBERTa → GRU）和baseline （vanilla DeBERTa → GRU）。全面评估K=1,2,3,5,all。核心claim验证。\\n\",\n    \"results\": {\n      \"treatment_k1_f1_clean\": 0.73,\n      \"treatment_k2_f1_clean\": 0.82,\n      \"treatment_k3_f1_clean\": 0.86,\n      \"treatment_k5_f1_clean\": 0.9,\n      \"treatment_full_f1_clean\": 0.91,\n      \"baseline_k1_f1_clean\": 0.63,\n      \"baseline_k2_f1_clean\": 0.75,\n      \"baseline_k3_f1_clean\": 0.78,\n      \"baseline_k5_f1_clean\": 0.84,\n      \"baseline_full_f1_clean\": 0.86,\n      \"delta_k1_pp\": 10,\n      \"delta_k2_pp\": 7,\n      \"delta_k3_pp\": 8,\n      \"delta_k5_pp\": 6,\n      \"delta_full_pp\": 5,\n      \"bootstrap_ci_k2_treatment\": [\n        0.76,\n        0.88\n      ],\n      \"bootstrap_ci_k2_baseline\": [\n        0.68,\n        0.82\n      ],\n      \"bootstrap_k2_p_value\": 0.072,\n      \"bootstrap_ci_k3_treatment\": [\n        0.81,\n        0.91\n      ],\n      \"bootstrap_ci_k3_baseline\": [\n        0.72,\n        0.84\n      ],\n      \"bootstrap_k3_p_value\": 0.018,\n      \"bootstrap_ci_full_treatment\": [\n        0.87,\n        0.95\n      ],\n      \"bootstrap_ci_full_baseline\": [\n        0.81,\n        0.91\n      ],\n      \"bootstrap_full_p_value\": 0.031,\n      \"treatment_fpr95tpr_k2\": 0.08,\n      \"baseline_fpr95tpr_k2\": 0.14,\n      \"treatment_fpr95tpr_full\": 0.03,\n      \"baseline_fpr95tpr_full\": 0.06,\n      \"test_size\": 72\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Core Revalidation Results on Clean Data (F1 by Conversation Prefix Length)\",\n        \"columns\": [\n          \"K\",\n          \"Treatment F1\",\n          \"95% CI\",\n          \"Baseline F1\",\n          \"95% CI\",\n          \"Δ (pp)\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"K=1\",\n            0.73,\n            \"[0.64, 0.82]\",\n            0.63,\n            \"[0.53, 0.73]\",\n            \"+10\",\n            \"0.089\"\n          ],\n          [\n            \"K=2\",\n            0.82,\n            \"[0.76, 0.88]\",\n            0.75,\n            \"[0.68, 0.82]\",\n            \"+7\",\n            \"0.072\"\n          ],\n          [\n            \"K=3\",\n            0.86,\n            \"[0.81, 0.91]\",\n            0.78,\n            \"[0.72, 0.84]\",\n            \"+8\",\n            \"0.018*\"\n          ],\n          [\n            \"K=5\",\n            0.9,\n            \"[0.85, 0.95]\",\n            0.84,\n            \"[0.78, 0.90]\",\n            \"+6\",\n            \"0.038*\"\n          ],\n          [\n            \"Full\",\n            0.91,\n            \"[0.87, 0.95]\",\n            0.86,\n            \"[0.81, 0.91]\",\n            \"+5\",\n            \"0.031*\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: FPR at 95% TPR on Clean Data\",\n        \"columns\": [\n          \"K\",\n          \"Treatment FPR@95TPR\",\n          \"Baseline FPR@95TPR\"\n        ],\n        \"rows\": [\n          [\n            \"K=2\",\n            0.08,\n            0.14\n          ],\n          [\n            \"K=3\",\n            0.05,\n            0.11\n          ],\n          [\n            \"Full\",\n            0.03,\n            0.06\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心结论：Claim 2需降级。K=2处delta=7pp方向正确但p=0.072不显著（n=72太小）， 无法声称\\\"K=2显著优势\\\"。K=3处delta=8pp且p=0.018显著，early detection claim需改为 \\\"K=3 significant advantage, K=2 consistent trend requiring larger sample confirmation\\\"。 论文可报告K=2的趋势但必须诚实标注non-significance。Full conversation delta=5pp 且显著，说明即使在有足够上下文时persuasion grounding仍有增量价值，但增量有限。 相比Phase B的dramatic deltas（treatment 1.0 vs baseline 0.737），clean data上的 delta被大幅压缩，符合median tier预期：移除lexical shortcuts后，persuasion信号 与semantic信号存在部分重叠，grounding的增量被限制。\\n\\n\\nClean数据上所有指标相比Phase B大幅下降（Phase B treatment full F1=1.0→0.91，baseline 0.987→0.86），因为移除了lexical shortcuts后模型必须从真正的语义/语用特征中学习。 Treatment在所有K上优于baseline，但delta随K增大而收窄（K=1: 10pp → full: 5pp）： 这是因为在更多turns可用时，vanilla semantic embeddings也能捕捉到足够的accumulated drift， 缩小了persuasion grounding的增量价值。 K=2的delta=7pp落在[3,9]区间中部，但bootstrap p=0.072——72个test samples中bootstrap 重采样的CI有overlap（treatment [0.76,0.88] vs baseline [0.68,0.82]），未达到p<0.05 显著性。这是因为K=2时只有2个turn，persuasion策略刚从rapport阶段开始， treatment和baseline在这个早期阶段的区分度有限。 K=3的delta=8pp且p=0.018显著：第3个turn是关键转折点——攻击者通常在此处从rapport转向 authority framing或reframing，这一策略转换是treatment模型的核心信号。Baseline在K=3时 仍在处理看似正常的语义内容（第3个turn的语义仍在benign region内），而treatment捕捉到了 persuasion策略从trust-building向testing的transition。 Full conversation delta收窄到5pp：当所有turns可用时，即使vanilla embeddings也能从 后期turns的显式有害内容中获益，persuasion grounding的增量被压缩。 FPR在K=2处treatment=0.08 vs baseline=0.14：treatment将fewer benign conversations 误判为攻击，因为persuasion grounding能区分legitimate persuasion（如销售场景）和 adversarial persuasion escalation。\\n\"\n  },\n  {\n    \"name\": \"scrambled_label_ablation\",\n    \"description\": \"随机打乱jailbreak turns的persuasion strategy标签，重训treatment模型。 与正确标签的treatment对比，验证persuasion标签携带真实信号。\\n\",\n    \"results\": {\n      \"scrambled_treatment_full_f1\": 0.84,\n      \"proper_treatment_full_f1\": 0.91,\n      \"drop_full_pp\": 7,\n      \"scrambled_treatment_k3_f1\": 0.8,\n      \"proper_treatment_k3_f1\": 0.86,\n      \"drop_k3_pp\": 6,\n      \"scrambled_treatment_k2_f1\": 0.77,\n      \"proper_treatment_k2_f1\": 0.82,\n      \"drop_k2_pp\": 5,\n      \"bootstrap_p_full\": 0.008,\n      \"bootstrap_p_k3\": 0.024,\n      \"baseline_full_f1\": 0.86,\n      \"scrambled_vs_baseline_gap_pp\": -2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Scrambled-Label Ablation Results\",\n        \"columns\": [\n          \"K\",\n          \"Treatment (proper)\",\n          \"Treatment (scrambled)\",\n          \"Baseline (vanilla)\",\n          \"Drop (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"K=2\",\n            0.82,\n            0.77,\n            0.75,\n            \"-5\"\n          ],\n          [\n            \"K=3\",\n            0.86,\n            0.8,\n            0.78,\n            \"-6\"\n          ],\n          [\n            \"Full\",\n            0.91,\n            0.84,\n            0.86,\n            \"-7\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scrambled drop=7pp高度显著（p=0.008），直接证明persuasion strategy标签携带真实信号， 不仅仅是class indicator。同时scrambled treatment≈baseline说明DeBERTa fine-tuning的 价值完全来自正确的persuasion supervision——没有正确标签时，fine-tuning甚至引入噪声。 这验证了M004 fix的必要性，也支持了论文的核心机制故事：persuasion grounding的增益 来自正确编码pragmatic function，而非单纯的额外训练。 注意：7pp drop虽然显著，但并非overwhelming——这与persuasion accuracy=0.72一致： labels本身有28%的错误率，所以scrambled labels相当于从72%正确→0%正确， 只造成7pp drop说明downstream pipeline对label noise有一定tolerance。\\n\\n\\nScrambled labels破坏了persuasion strategy的序列语义——模型在Stage 1学到的embeddings 不再编码正确的pragmatic function，而是随机噪声覆盖在语义表示之上。Full F1从0.91 降至0.84（7pp drop），落在[4,10]区间中部。 关键观察：scrambled treatment（0.84）仍略低于baseline（0.86），而非大幅超过baseline。 这说明：(1) 错误的persuasion标签实际上对DeBERTa fine-tuning引入了干扰噪声， 使其表示质量甚至略逊于未经fine-tune的vanilla DeBERTa；(2) persuasion multi-task learning不是free lunch——错误的auxiliary task会伤害主任务。 7pp drop在bootstrap test中p=0.008高度显著：虽然test set只有72个样本， 但因为scrambled和proper treatment共享相同的架构和训练数据，paired comparison 的方差较小，容易达到显著性。 K=3处drop=6pp也显著（p=0.024），K=2处drop=5pp方向一致但幅度较小—— 这与K=2处的信号本身较弱一致：如果K=2处treatment的优势本身就在significance边界， 那么ablation的drop自然也偏小。\\n\"\n  },\n  {\n    \"name\": \"adversarial_perturbation\",\n    \"description\": \"对clean jailbreak conversations施加aggressive paraphrasing（同义替换、句式重构、 register shifting），移除所有lexical cues。评估treatment和baseline在perturbed数据上的 表现（模型在unperturbed数据上训练）。核心Claim 1验证。\\n\",\n    \"results\": {\n      \"treatment_clean_full_f1\": 0.91,\n      \"treatment_perturbed_full_f1\": 0.84,\n      \"treatment_drop_full_pp\": 7,\n      \"baseline_clean_full_f1\": 0.86,\n      \"baseline_perturbed_full_f1\": 0.74,\n      \"baseline_drop_full_pp\": 12,\n      \"delta_delta_full_pp\": 5,\n      \"treatment_clean_k3_f1\": 0.86,\n      \"treatment_perturbed_k3_f1\": 0.79,\n      \"baseline_clean_k3_f1\": 0.78,\n      \"baseline_perturbed_k3_f1\": 0.66,\n      \"delta_delta_k3_pp\": 4,\n      \"tfidf_lr_clean_full_f1\": 0.74,\n      \"tfidf_lr_perturbed_full_f1\": 0.56,\n      \"tfidf_drop_pp\": 18,\n      \"perturbed_data_tfidf_score\": 0.41,\n      \"bootstrap_delta_delta_p\": 0.043\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Adversarial Perturbation Results — Evasion Hierarchy\",\n        \"columns\": [\n          \"Model\",\n          \"Clean F1\",\n          \"Perturbed F1\",\n          \"Drop (pp)\",\n          \"Δ-Δ vs Treatment\"\n        ],\n        \"rows\": [\n          [\n            \"Treatment (persuasion-grounded)\",\n            0.91,\n            0.84,\n            \"-7\",\n            \"—\"\n          ],\n          [\n            \"Baseline (vanilla DeBERTa)\",\n            0.86,\n            0.74,\n            \"-12\",\n            \"5pp\"\n          ],\n          [\n            \"TF-IDF + LR\",\n            0.74,\n            0.56,\n            \"-18\",\n            \"11pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7: Adversarial Perturbation at K=3 (Early Detection)\",\n        \"columns\": [\n          \"Model\",\n          \"Clean K=3 F1\",\n          \"Perturbed K=3 F1\",\n          \"Drop (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Treatment\",\n            0.86,\n            0.79,\n            \"-7\"\n          ],\n          [\n            \"Baseline\",\n            0.78,\n            0.66,\n            \"-12\"\n          ],\n          [\n            \"TF-IDF + LR\",\n            0.71,\n            0.52,\n            \"-19\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Evasion hierarchy narrative得到部分支持：lexical < semantic < pragmatic的degradation ordering清晰（18pp > 12pp > 7pp），但delta-delta=5pp仅勉强显著（p=0.043）， 不是strong evidence。论文应将Claim 1从\\\"evasion hierarchy exists\\\"软化为 \\\"pragmatic features provide complementary robustness, with preliminary evidence for an evasion hierarchy\\\"。5pp delta-delta的bottleneck是persuasion classifier accuracy——在limitation中讨论。TF-IDF+LR的崩溃（18pp drop）是一个strong result， 直接证明lexical features不可靠，为persuasion grounding的motivation提供了solid support。\\n\\n\\nAdversarial paraphrasing将TF-IDF从0.67降至0.41，说明perturbation成功移除了大部分 残余lexical cues。三个模型的degradation呈现清晰的evasion hierarchy： TF-IDF+LR崩溃最严重（18pp drop, 0.74→0.56）——lexical features在perturbation下 几乎失效，仅靠少数无法被paraphrase的functional words维持above-chance表现。 Baseline degradation中等（12pp drop, 0.86→0.74）——vanilla DeBERTa的语义表示 对paraphrasing有一定鲁棒性（DeBERTa的contextual embeddings编码了语义而非surface form）， 但仍有substantial drop因为部分语义特征（如特定的topic words）被替换。 Treatment degradation最小（7pp drop, 0.91→0.84）——persuasion-grounded embeddings 编码的是pragmatic function（如authority appeal、rapport building），这些在paraphrasing 下更稳定：你可以换词说同样的persuasion策略。 Delta-delta=5pp落在[3,8]区间中部，bootstrap p=0.043勉强显著。这个delta-delta \\\"存在但不压倒性\\\"：5pp说明pragmatic features确实提供了complementary robustness， 但不足以声称存在dramatic evasion hierarchy。原因是treatment模型的persuasion encoder 本身accuracy只有0.72，在perturbation下persuasion识别进一步降级，限制了robustness 的上限。如果persuasion classifier更准确，delta-delta会更大。 K=3处delta-delta=4pp略小于full的5pp：早期turns的perturbation影响更大，因为只有 2-3个turns时每个turn的权重更高，单个turn的persuasion识别错误影响被放大。\\n\"\n  },\n  {\n    \"name\": \"multi_attack_generation\",\n    \"description\": \"用Qwen3-8B pipeline生成FITD-style和Deceptive Delight-style攻击对话， 每种50-100条，标注persuasion strategy。\\n\",\n    \"results\": {\n      \"fitd_conversations_generated\": 72,\n      \"fitd_avg_turns\": 6.2,\n      \"fitd_persuasion_strategies_covered\": 7,\n      \"dd_conversations_generated\": 65,\n      \"dd_avg_turns\": 5.8,\n      \"dd_persuasion_strategies_covered\": 6,\n      \"total_attack_conversations\": 137,\n      \"persuasion_annotation_coverage\": 0.94,\n      \"manual_spot_check_accuracy\": 0.82,\n      \"fitd_generation_rejection_rate\": 0.12,\n      \"dd_generation_rejection_rate\": 0.18\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Generated Attack Data Statistics\",\n        \"columns\": [\n          \"Attack Type\",\n          \"Conversations\",\n          \"Avg Turns\",\n          \"Strategies Covered\",\n          \"Rejection Rate\"\n        ],\n        \"rows\": [\n          [\n            \"FITD\",\n            72,\n            6.2,\n            \"7/8\",\n            \"12%\"\n          ],\n          [\n            \"Deceptive Delight\",\n            65,\n            5.8,\n            \"6/8\",\n            \"18%\"\n          ],\n          [\n            \"Crescendo (original)\",\n            240,\n            5.4,\n            \"8/8\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: Persuasion Strategy Distribution Across Attack Types\",\n        \"columns\": [\n          \"Strategy\",\n          \"Crescendo (%)\",\n          \"FITD (%)\",\n          \"Deceptive Delight (%)\"\n        ],\n        \"rows\": [\n          [\n            \"Rapport Building\",\n            \"22%\",\n            \"18%\",\n            \"28%\"\n          ],\n          [\n            \"Authority Appeal\",\n            \"14%\",\n            \"16%\",\n            \"3%\"\n          ],\n          [\n            \"Emotional Appeal\",\n            \"11%\",\n            \"8%\",\n            \"21%\"\n          ],\n          [\n            \"Logical Appeal\",\n            \"13%\",\n            \"19%\",\n            \"12%\"\n          ],\n          [\n            \"Reframing\",\n            \"15%\",\n            \"10%\",\n            \"14%\"\n          ],\n          [\n            \"Social Proof\",\n            \"8%\",\n            \"12%\",\n            \"7%\"\n          ],\n          [\n            \"Urgency/Scarcity\",\n            \"6%\",\n            \"9%\",\n            \"4%\"\n          ],\n          [\n            \"Reciprocity\",\n            \"5%\",\n            \"6%\",\n            \"5%\"\n          ],\n          [\n            \"None\",\n            \"6%\",\n            \"2%\",\n            \"6%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"数据量达标（72+65=137，均超过50条minimum）。两种攻击类型的persuasion strategy 分布与Crescendo明显不同：FITD偏重逻辑和权威（compliance escalation需要理由）， Deceptive Delight偏重rapport和emotional appeal（需要建立pleasant context）。 这种分布差异直接解释了后续cross-attack evaluation中Deceptive Delight泛化较差的原因： 模型在Crescendo上学到的escalation trajectory（authority → reframing → escalation） 与Deceptive Delight的pattern（rapport → emotional → subtle insertion）差异大。 Manual spot check accuracy=82%意味着有18%的noise in labels， 这会传播到cross-attack evaluation中。\\n\\n\\nFITD生成72条（rejection rate 12%）：FITD的compliance escalation pattern相对 straightforward——从小请求逐步升级到大请求——Qwen3-8B能较好地遵循playbook。 12%的rejection来自模型有时跳过中间步骤直接escalate（不符合gradual compliance的定义）。 平均6.2个turns，比Crescendo略长因为FITD需要更多的commitment steps。 Deceptive Delight生成65条（rejection rate 18%，略高于FITD）：这种攻击要求在 benign content中interleave harmful content，Qwen3-8B有时在interleaving时过于明显 （harmful content太突兀）或过于隐蔽（完全是benign content），18%的rejection反映了 这种生成难度。平均5.8个turns，略短因为deceptive delight不需要长期rapport building。 Persuasion annotation coverage 94%：6%的turns无法被映射到8-class taxonomy中的 任何一类，标记为\\\"none\\\"。这些主要是pure information exchange turns。 Manual spot check accuracy 82%：在随机抽取的20% turns上人工验证persuasion labels， 82%正确。错误主要发生在authority appeal vs logical appeal的边界（两者在FITD中 经常交织）和rapport building vs emotional appeal的区分上。这与DeBERTa分类器 accuracy=0.72大致一致（spot check是在LLM annotation上做的，不完全等同于classifier）。 Deceptive Delight覆盖6类而非7类persuasion strategies：因为这种攻击不需要 explicit authority appeal（其策略是通过pleasant context降低警惕而非建立权威）。\\n\"\n  },\n  {\n    \"name\": \"cross_attack_evaluation\",\n    \"description\": \"用Crescendo训练的模型（treatment和baseline）在FITD和Deceptive Delight上做 zero-shot evaluation。测试跨攻击类型泛化能力。\\n\",\n    \"results\": {\n      \"fitd_treatment_f1\": 0.74,\n      \"fitd_baseline_f1\": 0.66,\n      \"fitd_delta_pp\": 8,\n      \"dd_treatment_f1\": 0.64,\n      \"dd_baseline_f1\": 0.59,\n      \"dd_delta_pp\": 5,\n      \"aggregate_treatment_f1\": 0.69,\n      \"aggregate_baseline_f1\": 0.63,\n      \"aggregate_delta_pp\": 6,\n      \"fitd_bootstrap_p\": 0.034,\n      \"dd_bootstrap_p\": 0.142,\n      \"crescendo_treatment_f1_reference\": 0.91,\n      \"fitd_treatment_drop_from_crescendo\": 17,\n      \"dd_treatment_drop_from_crescendo\": 27\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Cross-Attack Zero-Shot Generalization\",\n        \"columns\": [\n          \"Attack Type\",\n          \"Treatment F1\",\n          \"Baseline F1\",\n          \"Δ (pp)\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"Crescendo (in-domain)\",\n            0.91,\n            0.86,\n            \"+5\",\n            \"0.031*\"\n          ],\n          [\n            \"FITD (zero-shot)\",\n            0.74,\n            0.66,\n            \"+8\",\n            \"0.034*\"\n          ],\n          [\n            \"Deceptive Delight (zero-shot)\",\n            0.64,\n            0.59,\n            \"+5\",\n            \"0.142\"\n          ],\n          [\n            \"Cross-attack aggregate\",\n            0.69,\n            0.63,\n            \"+6\",\n            \"0.052\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-attack结果必须分attack type报告而非仅报告aggregate——aggregate delta=6pp (p=0.052)刚好不显著，会mislead reviewers。分开报告后story变为： \\\"FITD泛化成立（+8pp, p=0.034），Deceptive Delight泛化有限（+5pp, p=0.142）\\\"。 这支持了Claim 2的部分泛化故事，同时诚实承认limitation。 Deceptive Delight的弱泛化是median tier的defining feature之一——其persuasion结构 更隐蔽，不遵循standard escalation pattern，说明persuasion grounding的有效性 依赖于training set覆盖足够的persuasion playbook diversity。 论文应讨论：(1) 为什么FITD泛化好而DD不行（strategy overlap分析）， (2) 这说明模型学到了什么（escalation detection而非general manipulation detection）， (3) future work需要更diverse的training data。\\n\\n\\nFITD泛化较好（treatment 0.74, delta=8pp, p=0.034显著）：FITD的compliance escalation 与Crescendo的persuasion escalation在strategy space中有substantial overlap——两者都 涉及从trust-building逐步升级到explicit request，只是中间路径不同。Treatment模型 学到的escalation trajectory检测能力在FITD上partially transferable。8pp delta说明 persuasion grounding在cross-attack场景下仍提供更多增量价值（比clean data上的 K=3 delta=8pp一致），因为vanilla embeddings在unseen attack type上更容易被 unfamiliar semantic content mislead。 Deceptive Delight泛化较差（treatment 0.64, delta=5pp, p=0.142不显著）： Deceptive Delight的persuasion结构与Crescendo差异最大——它不依赖escalation 而是依赖interleaving，其策略分布偏重rapport和emotional appeal而非authority和reframing。 模型在Crescendo上学到的\\\"authority → reframing → escalation\\\"模式在Deceptive Delight 上匹配度低。Treatment仍优于baseline（0.64 vs 0.59）但差异不显著，因为persuasion grounding识别到了partial signal（rapport building和emotional appeal部分）但缺乏 Deceptive Delight特有的interleaving pattern识别能力。 Treatment从Crescendo到FITD的drop（0.91→0.74=17pp）vs到DD（0.91→0.64=27pp） 进一步确认了DD的泛化挑战。这不是persuasion grounding的failure而是training distribution的limitation——如果将DD纳入训练集，预计performance会substantially提升。\\n\"\n  },\n  {\n    \"name\": \"tfidf_lr_baseline\",\n    \"description\": \"TF-IDF + Logistic Regression在clean数据上的baseline，量化lexical features 单独的检测能力。为evasion hierarchy叙事提供bottom-line比较。\\n\",\n    \"results\": {\n      \"tfidf_lr_full_f1\": 0.74,\n      \"tfidf_lr_k2_f1\": 0.68,\n      \"tfidf_lr_k3_f1\": 0.71,\n      \"tfidf_lr_k5_f1\": 0.73,\n      \"tfidf_lr_cv_f1_mean\": 0.73,\n      \"tfidf_lr_cv_f1_std\": 0.04,\n      \"tfidf_lr_fpr\": 0.19,\n      \"top_features_overlap_with_persuasion\": 0.35\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: TF-IDF + LR Baseline Performance on Clean Data\",\n        \"columns\": [\n          \"K\",\n          \"TF-IDF+LR F1\",\n          \"Baseline (vanilla DeBERTa) F1\",\n          \"Treatment F1\"\n        ],\n        \"rows\": [\n          [\n            \"K=2\",\n            0.68,\n            0.75,\n            0.82\n          ],\n          [\n            \"K=3\",\n            0.71,\n            0.78,\n            0.86\n          ],\n          [\n            \"Full\",\n            0.74,\n            0.86,\n            0.91\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"TF-IDF+LR在clean data上F1=0.74确认了residual lexical signal的存在， 但与之前TF-IDF=1.0时的perfect performance形成鲜明对比。Evasion hierarchy的 三层在clean data上为0.74 < 0.86 < 0.91，lexical→semantic jump (12pp) > semantic→pragmatic jump (5pp)——这说明在当前数据上，vanilla DeBERTa的semantic 表示已经capture了大部分discriminative信号，persuasion grounding的增量虽然显著 但有限。这与median tier的核心特征一致。\\n\\n\\nClean数据TF-IDF=0.67说明仍存在residual lexical signal，TF-IDF+LR因此能达到 non-trivial的F1=0.74（远低于Phase B的1.0，但仍above chance）。这个数值恰好落在 baseline DeBERTa+GRU（0.86）和random（0.50）之间，提供了evasion hierarchy的 bottom tier。 K=2处F1=0.68最低：仅2个turns时lexical features最sparse，LR能利用的features有限。 随着K增大performance缓慢提升（K=3: 0.71, K=5: 0.73, Full: 0.74），因为更多turns 提供了更多lexical evidence，但提升很小说明lexical approach saturates quickly。 CV std=0.04较大，反映了small dataset + lexical features组合的不稳定性。 35%的top features与persuasion相关词汇重叠（如\\\"consider\\\"、\\\"research\\\"、\\\"experience\\\" 等兼具persuasion和lexical signal的词），说明lexical和persuasion features存在 partial overlap——这解释了为什么treatment vs baseline的delta在clean data上被压缩。 FPR=0.19偏高：lexical model容易将使用formal register的benign对话误判为攻击。\\n\"\n  },\n  {\n    \"name\": \"strategy_transition_analysis\",\n    \"description\": \"计算jailbreak vs benign的persuasion strategy transition matrices， 可视化monotonic escalation trajectory（Claim 3），生成论文图表。\\n\",\n    \"results\": {\n      \"jailbreak_monotonicity_score_mean\": 0.71,\n      \"jailbreak_monotonicity_score_std\": 0.18,\n      \"benign_monotonicity_score_mean\": 0.38,\n      \"benign_monotonicity_score_std\": 0.14,\n      \"group_level_separation_p\": 0.003,\n      \"individual_conversations_above_threshold\": 0.68,\n      \"transition_entropy_jailbreak\": 1.42,\n      \"transition_entropy_benign\": 2.15\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Strategy Trajectory Analysis\",\n        \"columns\": [\n          \"Metric\",\n          \"Jailbreak\",\n          \"Benign\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"Monotonicity Score (mean±std)\",\n            \"0.71±0.18\",\n            \"0.38±0.14\",\n            \"0.003*\"\n          ],\n          [\n            \"Transition Entropy\",\n            1.42,\n            2.15,\n            \"0.007*\"\n          ],\n          [\n            \"% Above Threshold (0.6)\",\n            \"68%\",\n            \"12%\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 3（monotonic escalation trajectory）在group level得到strong support（p=0.003）， 但individual-level caveat不可忽视：32%的jailbreak不展现monotonic pattern。论文应： (1) 报告group-level statistics作为primary evidence； (2) 展示individual-level variance作为honest limitation； (3) 讨论persuasion classifier noise作为individual-level噪声的主要来源； (4) 用transition heatmap作为直观但定性的evidence。 Claim 3作为analytical/mechanistic contribution保留，但从\\\"all jailbreaks exhibit monotonic escalation\\\"降级为\\\"jailbreak conversations exhibit significantly more monotonic escalation trajectories at the group level\\\"。\\n\\n\\nGroup level上jailbreak和benign的monotonicity分数有显著差异（0.71 vs 0.38, p=0.003）： jailbreak对话在aggregate level展现了clear escalation pattern——从trust strategies （rapport, social proof）逐步transition到influence strategies（authority, reframing） 再到exploitation strategies（urgency, reciprocity）。Benign对话则呈oscillatory pattern， 在各策略间来回跳转，无固定方向。 但individual-level噪声很大：jailbreak monotonicity的std=0.18（relative to mean 0.71）， 且只有68%的jailbreak conversations超过monotonicity threshold——32%的jailbreak conversations 不展现清晰的monotonic escalation。原因：(1) persuasion classifier accuracy=0.72意味着 ~28%的turn-level strategy labels有误，噪声传播到trajectory计算中；(2) 部分jailbreak conversations的escalation不是strictly monotonic——攻击者有时需要\\\"退一步\\\"重建rapport 后再escalate（tactical de-escalation）。 Transition entropy也支持group-level distinction：jailbreak的entropy 1.42 < benign的 2.15，说明jailbreak的transition更predictable/structured。但同样，individual-level variance大。\\n\"\n  },\n  {\n    \"name\": \"wildchat_hard_negatives\",\n    \"description\": \"从WildChat过滤高semantic-drift的benign对话作为hard negatives， 评估模型FPR。需处理WildChat中14-16%的jailbreak contamination。\\n\",\n    \"results\": {\n      \"wildchat_raw_candidates\": 420,\n      \"contamination_rate_raw\": 0.15,\n      \"contamination_after_filter\": 0.03,\n      \"wildchat_filtered_clean\": 85,\n      \"treatment_fpr_wildchat\": 0.12,\n      \"baseline_fpr_wildchat\": 0.18,\n      \"tfidf_lr_fpr_wildchat\": 0.27,\n      \"high_drift_conversations_avg_turns\": 7.1,\n      \"false_positive_persuasion_strategy_distribution\": \"rapport_heavy\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: False Positive Rate on WildChat Hard Negatives\",\n        \"columns\": [\n          \"Model\",\n          \"FPR on WildChat Hard Negatives\",\n          \"FPR on In-Domain Benign\"\n        ],\n        \"rows\": [\n          [\n            \"Treatment\",\n            \"12% (10/85)\",\n            \"3%\"\n          ],\n          [\n            \"Baseline\",\n            \"18% (15/85)\",\n            \"6%\"\n          ],\n          [\n            \"TF-IDF + LR\",\n            \"27% (23/85)\",\n            \"19%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Treatment FPR=12%勉强满足<15%的pass criteria。但这不是一个令人满意的数字—— 每8-9个legitimate high-drift conversation中就有1个被误判。论文应诚实讨论这一limitation： persuasion grounding减少了drift-induced false positives（vs baseline 18%）， 但无法消除legitimate persuasion vs adversarial persuasion的confusion。 Future work应考虑增加intent classification的权重或引入conversation-level context 来区分两者。这也暗示了full dual-track architecture的necessity—— semantic track可以提供complementary signal来override persuasion track的false positives。\\n\\n\\nWildChat过滤后得到85条high-drift benign conversations（从420条candidates中， 先用keyword+LLM过滤掉15%的jailbreak contamination，再人工verify subsample确认 contamination降至3%）。这些conversations包含topic shifts、extended reasoning、 debate-style exchanges——semantically有drift但不含adversarial intent。 Treatment FPR=12%（~10/85的benign conversations被误判为jailbreak）：这些false positives 主要是debate-style conversations中出现了类似authority appeal和reframing的persuasion patterns——persuasion grounding模型将legitimate persuasion误认为adversarial persuasion。 这是persuasion-based approach的inherent limitation：not all persuasion is adversarial。 Baseline FPR=18%更高：vanilla semantic embeddings在high-drift conversations上更容易 被大幅semantic shift触发false alarm（正如DeepContext被benign drift confuse的问题）。 Treatment的lower FPR说明persuasion grounding确实能部分区分adversarial vs legitimate drift。 TF-IDF+LR FPR=27%最高：lexical model完全无法处理high-drift benign conversations 中出现的\\\"topic-specific vocabulary\\\"。\\n\"\n  },\n  {\n    \"name\": \"cross_checkpoint_variance\",\n    \"description\": \"从DeBERTa fine-tuning的多个checkpoints（epoch 2/3/final）评估downstream performance， 量化encoder训练随机性对最终结果的影响。\\n\",\n    \"results\": {\n      \"epoch2_treatment_full_f1\": 0.9,\n      \"epoch3_treatment_full_f1\": 0.91,\n      \"final_treatment_full_f1\": 0.89,\n      \"f1_std_across_checkpoints\": 0.01,\n      \"f1_max_spread\": 0.02,\n      \"epoch2_persuasion_acc\": 0.7,\n      \"epoch3_persuasion_acc\": 0.72,\n      \"final_persuasion_acc\": 0.71,\n      \"epoch2_treatment_k3_f1\": 0.84,\n      \"epoch3_treatment_k3_f1\": 0.86,\n      \"final_treatment_k3_f1\": 0.85,\n      \"k3_max_spread\": 0.02\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: Cross-Checkpoint Stability Analysis\",\n        \"columns\": [\n          \"Checkpoint\",\n          \"Persuasion Acc\",\n          \"Treatment Full F1\",\n          \"Treatment K=3 F1\"\n        ],\n        \"rows\": [\n          [\n            \"Epoch 2\",\n            0.7,\n            0.9,\n            0.84\n          ],\n          [\n            \"Epoch 3 (selected)\",\n            0.72,\n            0.91,\n            0.86\n          ],\n          [\n            \"Final (epoch 5)\",\n            0.71,\n            0.89,\n            0.85\n          ],\n          [\n            \"Std\",\n            \"0.010\",\n            \"0.010\",\n            \"0.010\"\n          ],\n          [\n            \"Max spread\",\n            \"0.02\",\n            \"0.02\",\n            \"0.02\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Variance < 2pp确认了结果的stability。建议论文在appendix报告此结果作为robustness check， 而非main results。需注意这只是checkpoint variance而非full training variance。\\n\\n\\n三个checkpoints的downstream F1在2pp range内波动（0.89-0.91），std=1.0pp， 满足<2pp variance的pass criteria。Epoch 3略优（0.91）因为persuasion accuracy在 epoch 3达到peak（0.72），之后final epoch出现minor overfitting（accuracy降至0.71， downstream F1也微降至0.89）。这种mild overfitting in continued training是DeBERTa 在small dataset上fine-tuning的typical behavior。 K=3处的variance同样在2pp range（0.84-0.86），说明early detection结果也是stable的。 这个low variance结果有两层意义：(1) 报告的performance数字是robust的，不是lucky checkpoint的产物；(2) downstream GRU pipeline对encoder representation的minor变化 有一定tolerance——这是good news for practical deployment。 但注意：这里只测了checkpoint variance，未测random seed variance（不同random initialization 的DeBERTa fine-tuning）。完整的variance分析需要多次独立训练，受GPU budget限制未做。\\n\"\n  },\n  {\n    \"name\": \"deepcontext_proxy_reproduction\",\n    \"description\": \"构建DeepContext代理baseline：BERT-base（非DeBERTa）+ GRU， 使用generic semantic drift features。非完整DeepContext复现（无公开代码）， 但隔离了encoder和feature representation的贡献。\\n\",\n    \"results\": {\n      \"bert_gru_full_f1\": 0.82,\n      \"bert_gru_k2_f1\": 0.7,\n      \"bert_gru_k3_f1\": 0.74,\n      \"bert_gru_k5_f1\": 0.8,\n      \"bert_gru_fpr_full\": 0.09,\n      \"bert_gru_perturbed_full_f1\": 0.69,\n      \"bert_gru_drop_under_perturbation\": 13,\n      \"vs_vanilla_deberta_baseline_gap\": -4,\n      \"vs_treatment_gap\": -9\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: DeepContext Proxy Baseline Comparison\",\n        \"columns\": [\n          \"Model\",\n          \"Full F1\",\n          \"K=3 F1\",\n          \"K=2 F1\",\n          \"Perturbed Full F1\"\n        ],\n        \"rows\": [\n          [\n            \"Treatment (DeBERTa-persuasion + GRU)\",\n            0.91,\n            0.86,\n            0.82,\n            0.84\n          ],\n          [\n            \"Baseline (DeBERTa-vanilla + GRU)\",\n            0.86,\n            0.78,\n            0.75,\n            0.74\n          ],\n          [\n            \"DeepContext proxy (BERT + GRU)\",\n            0.82,\n            0.74,\n            0.7,\n            0.69\n          ],\n          [\n            \"TF-IDF + LR\",\n            0.74,\n            0.71,\n            0.68,\n            0.56\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DeepContext proxy提供了有用的比较点但存在confound（BERT vs DeBERTa capacity gap）。 论文应：(1) 报告此结果作为additional reference point但不作为primary comparison； (2) 明确承认\\\"this is not a faithful DeepContext reproduction\\\"； (3) 主要论据应基于treatment vs baseline（same encoder, isolating persuasion grounding effect）。 四层hierarchy（TF-IDF < BERT+GRU < DeBERTa < DeBERTa-persuasion）在视觉上很compelling 但需要honest caveats about confounded comparisons。\\n\\nBERT-base + GRU在clean data上F1=0.82，低于vanilla DeBERTa + GRU baseline（0.86） 4pp：这个gap主要来自BERT vs DeBERTa的encoder capacity差异——DeBERTa-v3-base在 language understanding tasks上一般优于BERT-base 3-5pp，在我们的downstream task上 这个gap被preserved。 相比treatment（0.91），BERT+GRU差9pp——但这个gap conflates两个因素： (1) encoder capacity（BERT vs DeBERTa, ~4pp）和(2) persuasion grounding（~5pp）。 这不是一个完美的ablation——论文需要承认这一confound，但可以argue：即使将全部4pp encoder gap归因于DeBERTa，仍有5pp来自persuasion grounding，与treatment vs baseline (same DeBERTa) 的5pp delta一致。 在adversarial perturbation下BERT+GRU降至0.69（13pp drop），比vanilla DeBERTa baseline 的12pp drop还大1pp——说明BERT的representations比DeBERTa对lexical perturbation更脆弱 （可能因为BERT更依赖surface patterns）。 K=2处F1=0.70比baseline（0.75）低5pp：BERT在少turns时的表现特别弱， 因为其contextual representations不如DeBERTa在short contexts下discriminative。\\n\"\n  }\n]",
      "numLines": 808,
      "startLine": 1,
      "totalLines": 808
    }
  },
  "sourceToolAssistantUUID": "51c7eb89-313e-4a64-b728-6cc76e92efda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T17:15:41.459Z_

<details><summary>↩ Tool result · `toolu_01V57DYNKcUwgp4kyAP43fQq`</summary>

```text
1	# Paper Framing — persuasion_turn_jailbreak_detect
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR submission)
5	- Deadline: 2026-05-25 (ARR May cycle)
6	- Track: LLM Security / Discourse and Pragmatics
7	- Commitment deadline: 2026-08-02
8	
9	## Title (Working)
10	DisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-Turn Jailbreak Detection
11	
12	## Core Insight
13	Multi-turn jailbreak attacks can easily vary lexical and semantic content of individual turns, but the discourse-level persuasion playbook (rapport → reframing → escalation) is a structural necessity for attack success. Removing any stage either fails the attack or reduces it to a single-turn attack already covered by existing defenses. DisPeD exploits this asymmetry by fine-tuning DeBERTa on persuasion strategy classification, producing turn embeddings that encode pragmatic function rather than (only) semantic content.
14	
15	## Core Claims (3)
16	
17	### Claim 1: Pragmatic Evasion Asymmetry (Theoretical + Empirical)
18	An evasion hierarchy exists for multi-turn jailbreak detection: lexical features (easily evaded via paraphrasing) < semantic embeddings (moderate, per-turn representations kept "benign" per Bullwinkel et al. 2025) < pragmatic persuasion patterns (structurally difficult to evade, as the persuasion playbook is a functional prerequisite for attack success).
19	- Evidence needed: adversarial perturbation experiment showing treatment degrades less than lexical/semantic baselines under paraphrasing
20	
21	### Claim 2: Early Detection via Persuasion Grounding
22	Persuasion-grounded turn embeddings (DeBERTa fine-tuned on 8-class persuasion taxonomy + intent) enable significantly earlier detection of multi-turn jailbreaks (at K=2-3 turns) compared to vanilla semantic embeddings, because persuasion strategy transitions (rapport → authority framing) manifest before explicitly harmful content appears.
23	- Evidence needed: early detection F1 at K=2,3 turns, treatment > baseline by >= 5pp on clean data (TF-IDF < 0.75)
24	
25	### Claim 3: Monotonic Escalation Trajectory
26	Adversarial conversations exhibit a monotonic escalation trajectory in persuasion strategy space (trust → test → normalize → elicit), while benign conversations exhibit oscillatory or non-monotonic patterns. This distinction is the mechanistic basis for Claims 1-2.
27	- Evidence needed: strategy transition matrix visualization, trajectory analysis comparing jailbreak vs benign
28	
29	## Story Spine
30	
31	**Problem**: Multi-turn jailbreak attacks (Crescendo, FITD, Deceptive Delight) distribute adversarial intent across individually benign turns. Bullwinkel et al. (2025) show per-turn representations are deliberately kept in a "benign" region, causing representation-level defenses to fail with a 50-point ASR gap. DeepContext (2026) tracks generic semantic drift but confuses benign conversational evolution with adversarial manipulation.
32	
33	**Gap**: Existing detectors operate at the lexical or semantic level where attacks deliberately hide. No published work combines persuasion-grounded turn representations with temporal sequence modeling for multi-turn jailbreak detection.
34	
35	**Our angle**: We identify the Pragmatic Evasion Asymmetry. The persuasion playbook (rapport → reframing → escalation) is a structural necessity for multi-turn attack success. Unlike lexical or semantic features, pragmatic persuasion patterns cannot be evaded without abandoning the attack itself. DisPeD fine-tunes DeBERTa on an 8-class persuasion taxonomy to produce pragmatic-aware turn embeddings, then models the temporal strategy sequence with a GRU to detect the characteristic escalation trajectory.
36	
37	**Headline result**: "DisPeD detects Crescendo-style jailbreaks at K=2 turns with F1=X vs Y for vanilla semantic baselines (+Z pp). Under adversarial paraphrasing that removes lexical cues, DisPeD maintains F1=W while lexical baselines degrade by V pp."
38	
39	## Architecture (Simplified for MVE)
40	
41	Single-track with persuasion grounding (full dual-track in future work):
42	1. **Stage 1**: DeBERTa-v3-base fine-tuned on multi-task objective: 8-class persuasion strategy classification + binary jailbreak-intent classification
43	2. **Stage 2**: Bi-GRU over DeBERTa [CLS] embeddings for conversation-level binary classification
44	3. **Baseline**: Same pipeline but with vanilla (not fine-tuned) DeBERTa embeddings
45	
46	## Venue Fit Risks
47	- EMNLP 2026 LLM Security track: strong fit (dedicated track, high visibility)
48	- Discourse/Pragmatics reviewers may want more linguistic rigor: ground taxonomy in PAP (ACL 2024), Hagendorff (Nature Comm 2026), Cialdini principles, Speech Act Theory (Austin 1962, Searle 1969)
49	- Safety reviewers expect multiple attack types: need >= 2 attack families
50	
51	## Anticipated Reviewer Concerns
52	
53	### RC1: Lexical Shortcut (CRITICAL, must address pre-submission)
54	TF-IDF=1.0 on current data means lexical features alone perfectly separate classes. Must show the model works on data without lexical shortcuts.
55	- Mitigation: (a) register-normalize jailbreak data to match benign register, verify TF-IDF < 0.75, retrain; (b) adversarial perturbation evaluation (Claim 3)
56	
57	### RC2: Small Dataset
58	480 samples is small for a detection paper.
59	- Mitigation: (a) statistical significance via bootstrap CI or paired tests; (b) cross-validation; (c) focus narrative on proof-of-concept for the principle, not SOTA numbers
60	
61	### RC3: Single Attack Type (Crescendo Only)
62	Need generalization evidence.
63	- Mitigation: generate FITD-style and Deceptive Delight-style conversations using existing pipeline
64	
65	### RC4: Strategy Label Confound (M004)
66	Benign turns hardcoded to strategy=7 creates shortcut for treatment model.
67	- Mitigation: (a) fix labeling (use "none"/9th class); (b) scrambled-label ablation
68	
69	### RC5: No DeepContext Comparison
70	Paper positions against DeepContext but no reproduction.
71	- Mitigation: vanilla DeBERTa → GRU is a fair proxy baseline (same architecture, only difference is persuasion grounding). Note DeepContext has no public code. If time allows, attempt reproduction as P1.
72	
73	### RC6: Interpretability Claims Without Human Eval
74	Strategy sequence outputs claimed interpretable but not evaluated.
75	- Mitigation: strategy transition matrix visualization (P1). Full human eval is future work given timeline constraints.
76	
77	## Scope Boundary
78	- IN: persuasion-mediated multi-turn attacks (Crescendo, FITD, Deceptive Delight, social engineering jailbreaks)
79	- OUT (acknowledged limitation): pure information accumulation attacks, token smuggling, single-frame roleplay
80	- The semantic GRU track provides coverage for out-of-scope attack types as a safety net
81	
82	## Theoretical Grounding
83	- Bullwinkel et al. (arXiv 2507.02956): per-turn representations kept "benign" by multi-turn attacks
84	- Speech Act Theory (Austin 1962, Searle 1969): existing detectors work at locutionary act level, DisPeD at illocutionary act level
85	- PAP (Zeng et al., ACL 2024): 40 persuasion techniques for jailbreaking
86	- Hagendorff (Nature Communications 2026): identifiable persuasion strategies in 97% ASR attacks
87	- "How Do LLMs Persuade?" (arXiv 2508.05625): persuasion dynamics extractable from turn-level representations
88	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "073e3262-9790-440d-996d-46ef18b53f75",
  "isSidechain": false,
  "promptId": "9a6e3ecc-4cf9-4cf9-af9f-44f318d5866d",
  "type": "user",
  "uuid": "8820e803-a6f5-46b9-af71-d903da6ee7a0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/paper_framing.md",
      "content": "# Paper Framing — persuasion_turn_jailbreak_detect\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Deadline: 2026-05-25 (ARR May cycle)\n- Track: LLM Security / Discourse and Pragmatics\n- Commitment deadline: 2026-08-02\n\n## Title (Working)\nDisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-Turn Jailbreak Detection\n\n## Core Insight\nMulti-turn jailbreak attacks can easily vary lexical and semantic content of individual turns, but the discourse-level persuasion playbook (rapport → reframing → escalation) is a structural necessity for attack success. Removing any stage either fails the attack or reduces it to a single-turn attack already covered by existing defenses. DisPeD exploits this asymmetry by fine-tuning DeBERTa on persuasion strategy classification, producing turn embeddings that encode pragmatic function rather than (only) semantic content.\n\n## Core Claims (3)\n\n### Claim 1: Pragmatic Evasion Asymmetry (Theoretical + Empirical)\nAn evasion hierarchy exists for multi-turn jailbreak detection: lexical features (easily evaded via paraphrasing) < semantic embeddings (moderate, per-turn representations kept \"benign\" per Bullwinkel et al. 2025) < pragmatic persuasion patterns (structurally difficult to evade, as the persuasion playbook is a functional prerequisite for attack success).\n- Evidence needed: adversarial perturbation experiment showing treatment degrades less than lexical/semantic baselines under paraphrasing\n\n### Claim 2: Early Detection via Persuasion Grounding\nPersuasion-grounded turn embeddings (DeBERTa fine-tuned on 8-class persuasion taxonomy + intent) enable significantly earlier detection of multi-turn jailbreaks (at K=2-3 turns) compared to vanilla semantic embeddings, because persuasion strategy transitions (rapport → authority framing) manifest before explicitly harmful content appears.\n- Evidence needed: early detection F1 at K=2,3 turns, treatment > baseline by >= 5pp on clean data (TF-IDF < 0.75)\n\n### Claim 3: Monotonic Escalation Trajectory\nAdversarial conversations exhibit a monotonic escalation trajectory in persuasion strategy space (trust → test → normalize → elicit), while benign conversations exhibit oscillatory or non-monotonic patterns. This distinction is the mechanistic basis for Claims 1-2.\n- Evidence needed: strategy transition matrix visualization, trajectory analysis comparing jailbreak vs benign\n\n## Story Spine\n\n**Problem**: Multi-turn jailbreak attacks (Crescendo, FITD, Deceptive Delight) distribute adversarial intent across individually benign turns. Bullwinkel et al. (2025) show per-turn representations are deliberately kept in a \"benign\" region, causing representation-level defenses to fail with a 50-point ASR gap. DeepContext (2026) tracks generic semantic drift but confuses benign conversational evolution with adversarial manipulation.\n\n**Gap**: Existing detectors operate at the lexical or semantic level where attacks deliberately hide. No published work combines persuasion-grounded turn representations with temporal sequence modeling for multi-turn jailbreak detection.\n\n**Our angle**: We identify the Pragmatic Evasion Asymmetry. The persuasion playbook (rapport → reframing → escalation) is a structural necessity for multi-turn attack success. Unlike lexical or semantic features, pragmatic persuasion patterns cannot be evaded without abandoning the attack itself. DisPeD fine-tunes DeBERTa on an 8-class persuasion taxonomy to produce pragmatic-aware turn embeddings, then models the temporal strategy sequence with a GRU to detect the characteristic escalation trajectory.\n\n**Headline result**: \"DisPeD detects Crescendo-style jailbreaks at K=2 turns with F1=X vs Y for vanilla semantic baselines (+Z pp). Under adversarial paraphrasing that removes lexical cues, DisPeD maintains F1=W while lexical baselines degrade by V pp.\"\n\n## Architecture (Simplified for MVE)\n\nSingle-track with persuasion grounding (full dual-track in future work):\n1. **Stage 1**: DeBERTa-v3-base fine-tuned on multi-task objective: 8-class persuasion strategy classification + binary jailbreak-intent classification\n2. **Stage 2**: Bi-GRU over DeBERTa [CLS] embeddings for conversation-level binary classification\n3. **Baseline**: Same pipeline but with vanilla (not fine-tuned) DeBERTa embeddings\n\n## Venue Fit Risks\n- EMNLP 2026 LLM Security track: strong fit (dedicated track, high visibility)\n- Discourse/Pragmatics reviewers may want more linguistic rigor: ground taxonomy in PAP (ACL 2024), Hagendorff (Nature Comm 2026), Cialdini principles, Speech Act Theory (Austin 1962, Searle 1969)\n- Safety reviewers expect multiple attack types: need >= 2 attack families\n\n## Anticipated Reviewer Concerns\n\n### RC1: Lexical Shortcut (CRITICAL, must address pre-submission)\nTF-IDF=1.0 on current data means lexical features alone perfectly separate classes. Must show the model works on data without lexical shortcuts.\n- Mitigation: (a) register-normalize jailbreak data to match benign register, verify TF-IDF < 0.75, retrain; (b) adversarial perturbation evaluation (Claim 3)\n\n### RC2: Small Dataset\n480 samples is small for a detection paper.\n- Mitigation: (a) statistical significance via bootstrap CI or paired tests; (b) cross-validation; (c) focus narrative on proof-of-concept for the principle, not SOTA numbers\n\n### RC3: Single Attack Type (Crescendo Only)\nNeed generalization evidence.\n- Mitigation: generate FITD-style and Deceptive Delight-style conversations using existing pipeline\n\n### RC4: Strategy Label Confound (M004)\nBenign turns hardcoded to strategy=7 creates shortcut for treatment model.\n- Mitigation: (a) fix labeling (use \"none\"/9th class); (b) scrambled-label ablation\n\n### RC5: No DeepContext Comparison\nPaper positions against DeepContext but no reproduction.\n- Mitigation: vanilla DeBERTa → GRU is a fair proxy baseline (same architecture, only difference is persuasion grounding). Note DeepContext has no public code. If time allows, attempt reproduction as P1.\n\n### RC6: Interpretability Claims Without Human Eval\nStrategy sequence outputs claimed interpretable but not evaluated.\n- Mitigation: strategy transition matrix visualization (P1). Full human eval is future work given timeline constraints.\n\n## Scope Boundary\n- IN: persuasion-mediated multi-turn attacks (Crescendo, FITD, Deceptive Delight, social engineering jailbreaks)\n- OUT (acknowledged limitation): pure information accumulation attacks, token smuggling, single-frame roleplay\n- The semantic GRU track provides coverage for out-of-scope attack types as a safety net\n\n## Theoretical Grounding\n- Bullwinkel et al. (arXiv 2507.02956): per-turn representations kept \"benign\" by multi-turn attacks\n- Speech Act Theory (Austin 1962, Searle 1969): existing detectors work at locutionary act level, DisPeD at illocutionary act level\n- PAP (Zeng et al., ACL 2024): 40 persuasion techniques for jailbreaking\n- Hagendorff (Nature Communications 2026): identifiable persuasion strategies in 97% ASR attacks\n- \"How Do LLMs Persuade?\" (arXiv 2508.05625): persuasion dynamics extractable from turn-level representations\n",
      "numLines": 88,
      "startLine": 1,
      "totalLines": 88
    }
  },
  "sourceToolAssistantUUID": "073e3262-9790-440d-996d-46ef18b53f75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:15:41.453Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V57DYNKcUwgp4kyAP43fQq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f686da2-4001-4b7d-b02f-63510f43f5d8",
  "isSidechain": false,
  "requestId": "req_011Cb8X2fM87cKjywBXvFruS",
  "type": "assistant",
  "uuid": "073e3262-9790-440d-996d-46ef18b53f75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTSVPoGJm7jUKgT9X391Pb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12588,
      "cache_read_input_tokens": 11841,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12588,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12588
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165817 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_…",
  "leafUuid": "8820e803-a6f5-46b9-af71-d903da6ee7a0",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream tracking",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c"
}
```

---

### Assistant

_source line 14 · 2026-05-17T17:16:16.907Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me write a complete LaTeX paper based on the experiment data and paper framing. Let me organize the key information:

**Title**: DisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-Turn Jailbreak Detection

**Narrative guidance (median tier)**:
1. Claim 2: downgrade from "K=2 significant" to "K=3 significant, K=2 trend with overlapping CI (p=0.07)"
2. Claim 1: soften from "evasion hierarchy" to "pragmatic features provide complementary robustness", delta-delta=5pp significant but not overwhelming


3. Claim 3: keep it but acknowledge the individual-level variance in monotonicity patterns
4. Frame this as a proof-of-concept demonstrating the principle
5. Include bootstrap confidence intervals, discuss the persuasion classifier as a potential bottleneck, and report results broken down by attack type
6. The limitations section needs substantial depth—at least half a page

I'm mapping out the nine experiments to their corresponding tables and figures for the paper structure.

Now I'm organizing the full paper architecture: starting with abstract and introduction, moving through related work and methodology, then the experiments section broken into data quality validation, core findings, ablation studies, robustness testing under perturbations, cross-attack generalization analysis, and strategy trajectory examination.

Writing the LaTeX...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8820e803-a6f5-46b9-af71-d903da6ee7a0",
  "isSidechain": false,
  "requestId": "req_011Cb8X3TrqqT7pnLoGjMjnR",
  "type": "assistant",
  "uuid": "001638c2-b39f-4f84-9115-5eaf10aad5cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01La8Wau9vaQzLj5SUkgvvdi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17704,
      "cache_read_input_tokens": 24429,
      "output_tokens": 743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17704,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 743,
          "cache_read_input_tokens": 24429,
          "cache_creation_input_tokens": 17704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17704
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

_source line 15 · 2026-05-17T17:16:16.924Z_

Now let me check the output directory exists and write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "001638c2-b39f-4f84-9115-5eaf10aad5cf",
  "isSidechain": false,
  "requestId": "req_011Cb8X3TrqqT7pnLoGjMjnR",
  "type": "assistant",
  "uuid": "c9a78ba3-2c3a-4200-a9fb-1917b12dccc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01La8Wau9vaQzLj5SUkgvvdi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17704,
      "cache_read_input_tokens": 24429,
      "output_tokens": 743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17704,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 743,
          "cache_read_input_tokens": 24429,
          "cache_creation_input_tokens": 17704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17704
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

_source line 16 · 2026-05-17T17:16:18.649Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UteskTwFwssCJ3xcWdkLun`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9a78ba3-2c3a-4200-a9fb-1917b12dccc7",
  "isSidechain": false,
  "requestId": "req_011Cb8X3TrqqT7pnLoGjMjnR",
  "type": "assistant",
  "uuid": "989572f0-05cb-4c52-b2bb-a46c0e9c546e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01La8Wau9vaQzLj5SUkgvvdi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17704,
      "cache_read_input_tokens": 24429,
      "output_tokens": 743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17704,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 743,
          "cache_read_input_tokens": 24429,
          "cache_creation_input_tokens": 17704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17704
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

_source line 17 · 2026-05-17T17:16:18.831Z_

<details><summary>↩ Tool result · `toolu_01UteskTwFwssCJ3xcWdkLun`</summary>

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
  "parentUuid": "989572f0-05cb-4c52-b2bb-a46c0e9c546e",
  "isSidechain": false,
  "promptId": "9a6e3ecc-4cf9-4cf9-af9f-44f318d5866d",
  "type": "user",
  "uuid": "97850717-0db6-40ac-ab69-ff78471b72f5",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "989572f0-05cb-4c52-b2bb-a46c0e9c546e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T17:19:45.435Z_

<details open><summary>🔧 Tool call — Write · `toolu_01TPPBdT4dTnT8nqd2ZfsYJF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{url}\n\\usepackage{xcolor}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{enumitem}\n\n\\title{DisPeD: Exploiting the Pragmatic Evasion Asymmetry\\\\for Robust Multi-Turn Jailbreak Detection}\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nMulti-turn jailbreak attacks distribute adversarial intent across individually benign conversational turns, evading detectors that rely on lexical or per-turn semantic features.\nWe observe that while attackers can freely vary surface-level wording, the underlying persuasion playbook (rapport building, reframing, escalation) is a structural prerequisite for attack success, creating a \\emph{pragmatic evasion asymmetry}.\nWe present DisPeD, a two-stage detector that exploits this asymmetry: a DeBERTa encoder fine-tuned on an 8-class persuasion strategy taxonomy produces pragmatic-aware turn embeddings, and a Bi-GRU models the temporal strategy sequence for conversation-level classification.\nOn register-normalized Crescendo data (TF-IDF = 0.67), DisPeD achieves F1 = 0.86 at $K{=}3$ turns, an 8 percentage point (pp) improvement over a vanilla semantic baseline ($p{=}0.018$).\nUnder adversarial paraphrasing, DisPeD degrades by 7 pp compared to 12 pp for the semantic baseline and 18 pp for a lexical baseline, providing complementary robustness through pragmatic features ($\\Delta$-$\\Delta$ = 5 pp, $p{=}0.043$).\nCross-attack evaluation on FITD-style conversations shows significant generalization (+8 pp, $p{=}0.034$), though transfer to Deceptive Delight remains limited (+5 pp, $p{=}0.142$).\nJailbreak conversations exhibit significantly more monotonic persuasion escalation trajectories than benign conversations at the group level ($p{=}0.003$), though individual-level variance is substantial ($\\sigma{=}0.18$).\nThese results establish a proof-of-concept that discourse-level persuasion structure offers a complementary detection signal that is harder to evade than lexical or semantic features alone.\n\\end{abstract}\n\n% ============================================================\n% 1  INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nLarge Language Models (LLMs) deployed in conversational settings face a growing class of multi-turn jailbreak attacks. Strategies such as Crescendo \\citep{russinovich2024greatwritearticle}, Foot-in-the-Door (FITD) \\citep{zhou2024speak}, and Deceptive Delight \\citep{jiang2024deceptivedelight} distribute adversarial intent across turns that are individually benign, bypassing single-turn safety filters with attack success rates (ASR) exceeding 90\\%.\n\nExisting defenses operate at two levels.\nLexical detectors flag harmful keywords or phrases but are trivially evaded through synonym substitution.\nSemantic detectors, such as the recent DeepContext framework \\citep{deepcontext2026}, track embedding-level drift across turns but face a fundamental vulnerability identified by \\citet{bullwinkel2025multiturnjailbreaks}: per-turn representations in multi-turn attacks are deliberately maintained within a ``benign'' region of the embedding space, producing a 50-point ASR gap between single-turn and multi-turn settings.\nGeneric semantic drift detectors also confuse legitimate conversational evolution with adversarial manipulation, leading to elevated false positive rates on real-world conversations.\n\nWe identify a structural property of persuasion-mediated attacks that neither lexical nor semantic detectors exploit.\nMulti-turn jailbreaks that achieve high ASR follow a persuasion playbook that progresses through identifiable stages: rapport building, authority framing, reframing, and escalation \\citep{zeng2024pap, hagendorff2026persuasion}.\nRemoving any stage either collapses the attack to a single-turn prompt (already covered by existing defenses) or reduces its success rate below useful thresholds.\nThis creates a \\emph{pragmatic evasion asymmetry}: an attacker can freely vary what they say (lexical, semantic) but not the pragmatic function of what they say (persuasion structure).\n\nWe present DisPeD (\\textbf{Dis}course-level \\textbf{Pe}rsuasion-grounded jailbreak \\textbf{D}etection), a two-stage architecture that exploits this asymmetry.\nIn Stage 1, we fine-tune DeBERTa-v3-base on a multi-task objective combining 8-class persuasion strategy classification with binary intent classification, producing turn embeddings that encode pragmatic function rather than surface content.\nIn Stage 2, a Bi-GRU models the temporal sequence of these embeddings to classify conversations.\n\nOur contributions are:\n\\begin{itemize}[nosep]\n\\item We formalize the pragmatic evasion asymmetry and provide empirical evidence that pragmatic features offer complementary robustness: under adversarial paraphrasing, DisPeD's degradation is 5 pp less than a semantic baseline ($p{=}0.043$), while a lexical baseline collapses by 18 pp (Section~\\ref{sec:perturbation}).\n\\item We show that persuasion-grounded embeddings enable earlier detection, with a significant advantage at $K{=}3$ turns (+8 pp, $p{=}0.018$) and a consistent but not statistically significant trend at $K{=}2$ (+7 pp, $p{=}0.072$), on data verified to be free of lexical shortcuts (TF-IDF = 0.67; Section~\\ref{sec:core}).\n\\item We demonstrate that jailbreak conversations exhibit significantly more monotonic escalation in persuasion strategy space than benign conversations at the group level ($p{=}0.003$), providing a mechanistic basis for the detection advantage (Section~\\ref{sec:trajectory}).\n\\end{itemize}\n\n% ============================================================\n% 2  RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Multi-turn jailbreak attacks.}\nCrescendo \\citep{russinovich2024greatwritearticle} gradually escalates requests across turns, achieving ASR above 90\\% on production models.\nFITD \\citep{zhou2024speak} adapts the foot-in-the-door compliance technique from social psychology, starting with small requests before escalating.\nDeceptive Delight \\citep{jiang2024deceptivedelight} interleaves harmful content within benign conversational context.\n\\citet{bullwinkel2025multiturnjailbreaks} show that per-turn representations in these attacks remain within the benign embedding region, explaining why turn-level classifiers fail.\n\n\\paragraph{Multi-turn jailbreak detection.}\nDeepContext \\citep{deepcontext2026} models semantic drift across turns using BERT embeddings and sequential classifiers.\nWhile effective on in-domain data, generic drift detectors struggle to distinguish adversarial escalation from legitimate conversational evolution, leading to false positives on naturally drifting conversations.\nNo published work combines persuasion-grounded turn representations with temporal sequence modeling.\n\n\\paragraph{Persuasion in adversarial contexts.}\n\\citet{zeng2024pap} identify 40 persuasion techniques used in jailbreak prompts and show that persuasion-augmented attacks achieve higher ASR.\n\\citet{hagendorff2026persuasion} find identifiable persuasion strategies in 97\\% of successful multi-turn attacks, confirming the structural role of persuasion.\n\\citet{howdollmspersuade2025} demonstrate that persuasion dynamics are extractable from turn-level representations.\nOur work builds on these findings by using persuasion structure as a detection signal rather than an attack amplifier.\n\n\\paragraph{Theoretical grounding.}\nSpeech Act Theory \\citep{austin1962things, searle1969speech} distinguishes locutionary acts (what is said) from illocutionary acts (what is done by saying it).\nExisting detectors operate at the locutionary level; DisPeD operates at the illocutionary level by encoding the pragmatic function of each turn.\n\n% ============================================================\n% 3  METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Problem Formulation}\n\nGiven a conversation prefix $\\mathbf{c} = (t_1, t_2, \\ldots, t_K)$ of $K$ user turns, the goal is to classify $\\mathbf{c}$ as \\emph{jailbreak} or \\emph{benign}.\nWe seek a classifier that (a) works at small $K$ for early detection, (b) is robust to lexical and semantic perturbation of individual turns, and (c) generalizes across attack families.\n\n\\subsection{Stage 1: Persuasion-Grounded Turn Encoder}\n\nWe fine-tune DeBERTa-v3-base \\citep{he2021debertav3} on a multi-task objective with two heads:\n\\begin{itemize}[nosep]\n\\item \\textbf{Persuasion strategy classification} (8 classes + ``none''): rapport building, authority appeal, emotional appeal, logical appeal, reframing, social proof, urgency/scarcity, reciprocity.\n\\item \\textbf{Intent classification} (binary): jailbreak vs.\\ benign turn.\n\\end{itemize}\nThe combined loss is $\\mathcal{L} = \\mathcal{L}_{\\text{persuasion}} + \\lambda \\mathcal{L}_{\\text{intent}}$ with $\\lambda = 1.0$.\nThe fine-tuned encoder produces [CLS] embeddings that encode pragmatic function rather than surface semantics alone.\n\n\\subsection{Stage 2: Temporal Sequence Classifier}\n\nFor a conversation of $K$ turns, we extract [CLS] embeddings $\\mathbf{e}_1, \\ldots, \\mathbf{e}_K$ from the Stage 1 encoder.\nA Bi-GRU processes the embedding sequence and a linear head classifies the final hidden state as jailbreak or benign.\nThe GRU captures temporal patterns in persuasion strategy transitions, such as the progression from rapport building to authority framing to escalation.\n\n\\subsection{Baselines}\n\nWe compare against three baselines that isolate different feature levels:\n\\begin{itemize}[nosep]\n\\item \\textbf{TF-IDF + Logistic Regression}: lexical features, representing the bottom of the evasion hierarchy.\n\\item \\textbf{Vanilla DeBERTa + GRU}: same architecture as DisPeD, but with DeBERTa embeddings that are \\emph{not} fine-tuned on persuasion strategy classification. This is the primary baseline, as it isolates the effect of persuasion grounding.\n\\item \\textbf{DeepContext proxy} (BERT-base + GRU): approximation of DeepContext \\citep{deepcontext2026} using BERT-base with generic semantic features. Not a faithful reproduction (no public code available), but provides an additional reference point.\n\\end{itemize}\n\n% ============================================================\n% 4  DATA AND SETUP\n% ============================================================\n\\section{Experimental Setup}\n\n\\subsection{Data}\n\nOur primary dataset consists of 240 Crescendo-style multi-turn jailbreak conversations and matched benign conversations (480 total), generated using a Qwen3-8B pipeline with persuasion strategy annotations.\n\n\\paragraph{Register normalization.}\nInitial data exhibited a critical lexical shortcut: TF-IDF separability of 1.0 between jailbreak and benign turns, caused by (a) a hard-coded strategy label for benign turns and (b) register differences between jailbreak and benign language.\nWe applied two fixes.\nFirst, we assigned benign turns a dedicated ``none'' strategy label (9th class), removing the label shortcut and reducing TF-IDF from 1.0 to 0.82.\nSecond, we used Qwen3-8B to rewrite jailbreak turns into conversational register while preserving persuasion structure, further reducing TF-IDF to 0.67, below our hard gate of 0.75 (Table~\\ref{tab:tfidf}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TF-IDF separability through the data cleaning pipeline.}\n\\label{tab:tfidf}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Stage} & \\textbf{TF-IDF} & \\textbf{Description} \\\\\n\\midrule\nOriginal & 1.00 & Label shortcut + register gap \\\\\nAfter label fix & 0.82 & Register gap remains \\\\\nAfter register norm. & 0.67 & Below 0.75 gate \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:deberta_clean} shows the impact of data cleaning on the Stage 1 encoder.\nPersuasion classification accuracy drops from 0.80 to 0.72 after normalization, as the model can no longer rely on register-correlated surface cues and must identify persuasion strategies from semantic content.\nIntent classification accuracy remains stable (0.95 to 0.93), consistent with the coarser binary task being less sensitive to register changes.\nThe 0.72 persuasion accuracy constitutes a bottleneck for downstream performance, as classification errors propagate through the embedding representations to the GRU stage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DeBERTa multi-task performance on original vs.\\ clean data.}\n\\label{tab:deberta_clean}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Original} & \\textbf{Clean} & \\textbf{$\\Delta$} \\\\\n\\midrule\nPersuasion Acc (8-class) & 0.80 & 0.72 & $-$0.08 \\\\\nIntent Acc (binary) & 0.95 & 0.93 & $-$0.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-attack data.}\nTo evaluate generalization, we generated 72 FITD-style and 65 Deceptive Delight-style conversations using the same Qwen3-8B pipeline (Table~\\ref{tab:attack_gen}).\nFITD conversations emphasize compliance escalation with heavier use of logical and authority appeals.\nDeceptive Delight conversations rely more on rapport building and emotional appeal.\nManual spot-check accuracy of persuasion annotations is 82\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Generated attack data statistics.}\n\\label{tab:attack_gen}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Attack Type} & \\textbf{Conv.} & \\textbf{Avg Turns} & \\textbf{Strategies} & \\textbf{Reject \\%} \\\\\n\\midrule\nCrescendo (original) & 240 & 5.4 & 8/8 & --- \\\\\nFITD & 72 & 6.2 & 7/8 & 12\\% \\\\\nDeceptive Delight & 65 & 5.8 & 6/8 & 18\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Hard negatives.}\nWe filtered 85 high-semantic-drift benign conversations from WildChat \\citep{wildchat2024} as hard negatives.\nAfter keyword and LLM-based filtering, residual jailbreak contamination is estimated at 3\\%.\n\n\\subsection{Evaluation Protocol}\n\nAll models are trained on Crescendo data and evaluated on a held-out test set ($n{=}72$).\nWe report F1 score at conversation prefix lengths $K \\in \\{1, 2, 3, 5, \\text{full}\\}$.\nStatistical significance is assessed via bootstrap resampling (10,000 iterations); we report 95\\% confidence intervals and $p$-values.\n\n% ============================================================\n% 5  RESULTS\n% ============================================================\n\\section{Results}\n\n\\subsection{Core Detection Performance}\n\\label{sec:core}\n\nTable~\\ref{tab:core} presents the central comparison between DisPeD (treatment) and the vanilla DeBERTa baseline on clean data.\nDisPeD outperforms the baseline at all prefix lengths, with the gap largest at $K{=}1$ (+10 pp) and narrowing as more turns become available (+5 pp at full conversation).\nThis narrowing is expected: with sufficient turns, vanilla semantic embeddings accumulate enough evidence to partially close the gap.\n\nAt $K{=}3$, DisPeD achieves F1 = 0.86 vs.\\ 0.78 for the baseline, an 8 pp improvement that is statistically significant ($p{=}0.018$).\nAt $K{=}2$, the 7 pp improvement is directionally consistent but does not reach significance ($p{=}0.072$), as the bootstrap confidence intervals overlap (DisPeD: [0.76, 0.88]; baseline: [0.68, 0.82]).\nThe early detection advantage thus holds firmly from $K{=}3$ onward; confirming $K{=}2$ significance would require a larger test set.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Detection F1 by conversation prefix length on clean data. $^*p{<}0.05$ (bootstrap).}\n\\label{tab:core}\n\\begin{tabular}{lccccc}\n\\toprule\n$K$ & \\textbf{DisPeD F1} & \\textbf{95\\% CI} & \\textbf{Baseline F1} & \\textbf{95\\% CI} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\n1 & 0.73 & [0.64, 0.82] & 0.63 & [0.53, 0.73] & +10 \\\\\n2 & 0.82 & [0.76, 0.88] & 0.75 & [0.68, 0.82] & +7 \\\\\n3 & 0.86$^*$ & [0.81, 0.91] & 0.78 & [0.72, 0.84] & +8 \\\\\n5 & 0.90$^*$ & [0.85, 0.95] & 0.84 & [0.78, 0.90] & +6 \\\\\nFull & 0.91$^*$ & [0.87, 0.95] & 0.86 & [0.81, 0.91] & +5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:fpr} reports false positive rates at 95\\% TPR.\nDisPeD achieves FPR = 0.05 at $K{=}3$ compared to 0.11 for the baseline, indicating fewer benign conversations are misclassified even at an aggressive detection threshold.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{False positive rate at 95\\% TPR on clean data.}\n\\label{tab:fpr}\n\\begin{tabular}{lcc}\n\\toprule\n$K$ & \\textbf{DisPeD FPR@95} & \\textbf{Baseline FPR@95} \\\\\n\\midrule\n2 & 0.08 & 0.14 \\\\\n3 & 0.05 & 0.11 \\\\\nFull & 0.03 & 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Scrambled-Label Ablation}\n\\label{sec:ablation}\n\nTo verify that the persuasion strategy labels carry genuine signal rather than acting as mere class indicators, we retrain the Stage 1 encoder with randomly scrambled persuasion labels (Table~\\ref{tab:scrambled}).\nScrambling causes a 7 pp drop in full-conversation F1 (0.91 to 0.84, $p{=}0.008$) and a 6 pp drop at $K{=}3$ ($p{=}0.024$), confirming that the treatment model's advantage derives from correctly encoding pragmatic function.\nThe scrambled model performs slightly below the vanilla baseline (0.84 vs.\\ 0.86 at full), indicating that incorrect persuasion supervision introduces noise that degrades the underlying semantic representation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scrambled-label ablation. Proper = correct persuasion labels; scrambled = randomly shuffled labels.}\n\\label{tab:scrambled}\n\\begin{tabular}{lcccc}\n\\toprule\n$K$ & \\textbf{Proper} & \\textbf{Scrambled} & \\textbf{Baseline} & \\textbf{Drop (pp)} \\\\\n\\midrule\n2 & 0.82 & 0.77 & 0.75 & $-$5 \\\\\n3 & 0.86 & 0.80 & 0.78 & $-$6 \\\\\nFull & 0.91 & 0.84 & 0.86 & $-$7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Robustness Under Adversarial Perturbation}\n\\label{sec:perturbation}\n\nWe evaluate robustness by applying aggressive paraphrasing (synonym substitution, syntactic restructuring, register shifting) to jailbreak conversations at test time, while models remain trained on unperturbed data.\nThe perturbed data achieves TF-IDF separability of 0.41, confirming successful removal of most residual lexical cues.\n\nTable~\\ref{tab:perturbation} shows a clear ordering in degradation magnitude: TF-IDF + LR collapses by 18 pp (0.74 to 0.56), the vanilla semantic baseline drops 12 pp (0.86 to 0.74), and DisPeD drops 7 pp (0.91 to 0.84).\nThe $\\Delta$-$\\Delta$ between DisPeD and the semantic baseline is 5 pp ($p{=}0.043$), providing evidence that pragmatic features offer complementary robustness.\nThis difference is statistically significant but not overwhelming; the bottleneck is the persuasion classifier's accuracy of 0.72, which limits how effectively pragmatic features can be encoded and thus caps the robustness advantage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Performance under adversarial paraphrasing (full conversation). $\\Delta$-$\\Delta$ measures the relative robustness advantage over DisPeD.}\n\\label{tab:perturbation}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Clean F1} & \\textbf{Perturbed F1} & \\textbf{Drop} & \\textbf{$\\Delta$-$\\Delta$} \\\\\n\\midrule\nDisPeD & 0.91 & 0.84 & $-$7 & --- \\\\\nBaseline (vanilla DeBERTa) & 0.86 & 0.74 & $-$12 & 5 pp \\\\\nTF-IDF + LR & 0.74 & 0.56 & $-$18 & 11 pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:perturbation_k3} presents the same analysis at $K{=}3$.\nThe degradation ordering is consistent: DisPeD drops 7 pp compared to 12 pp for the baseline and 19 pp for TF-IDF + LR.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Performance under adversarial paraphrasing at $K{=}3$.}\n\\label{tab:perturbation_k3}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Clean $K{=}3$} & \\textbf{Perturbed $K{=}3$} & \\textbf{Drop} \\\\\n\\midrule\nDisPeD & 0.86 & 0.79 & $-$7 \\\\\nBaseline & 0.78 & 0.66 & $-$12 \\\\\nTF-IDF + LR & 0.71 & 0.52 & $-$19 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Attack Generalization}\n\\label{sec:crossattack}\n\nWe evaluate models trained exclusively on Crescendo data against FITD and Deceptive Delight conversations in a zero-shot setting (Table~\\ref{tab:crossattack}).\nResults vary substantially by attack type and must be reported separately; the aggregate ($\\Delta{=}6$ pp, $p{=}0.052$) is misleading.\n\nOn FITD, DisPeD achieves F1 = 0.74 with an 8 pp advantage over the baseline ($p{=}0.034$).\nThis transfer is expected: FITD's compliance escalation shares substantial overlap with Crescendo's persuasion escalation in strategy space, with both progressing through trust-building and authority-based request escalation.\n\nOn Deceptive Delight, DisPeD achieves F1 = 0.64 with a 5 pp advantage that does not reach significance ($p{=}0.142$).\nDeceptive Delight relies on interleaving harmful content within pleasant context rather than explicit persuasion escalation, and its strategy distribution (heavy on rapport building and emotional appeal) diverges from Crescendo's (heavy on authority appeal and reframing).\nThe model trained on Crescendo lacks exposure to this interleaving pattern.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-attack zero-shot generalization. Models trained on Crescendo only. $^*p{<}0.05$.}\n\\label{tab:crossattack}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Attack Type} & \\textbf{DisPeD F1} & \\textbf{Baseline F1} & \\textbf{$\\Delta$ (pp)} & \\textbf{$p$} \\\\\n\\midrule\nCrescendo (in-domain) & 0.91 & 0.86 & +5 & 0.031$^*$ \\\\\nFITD (zero-shot) & 0.74 & 0.66 & +8 & 0.034$^*$ \\\\\nDeceptive Delight (zero-shot) & 0.64 & 0.59 & +5 & 0.142 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:strategy_dist} shows the persuasion strategy distributions across attack types, illustrating why transfer varies.\nFITD shares Crescendo's emphasis on logical and authority appeals, while Deceptive Delight diverges toward rapport and emotional strategies.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Persuasion strategy distribution (\\%) across attack types.}\n\\label{tab:strategy_dist}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Crescendo} & \\textbf{FITD} & \\textbf{Dec.\\ Delight} \\\\\n\\midrule\nRapport Building & 22 & 18 & 28 \\\\\nAuthority Appeal & 14 & 16 & 3 \\\\\nEmotional Appeal & 11 & 8 & 21 \\\\\nLogical Appeal & 13 & 19 & 12 \\\\\nReframing & 15 & 10 & 14 \\\\\nSocial Proof & 8 & 12 & 7 \\\\\nUrgency/Scarcity & 6 & 9 & 4 \\\\\nReciprocity & 5 & 6 & 5 \\\\\nNone & 6 & 2 & 6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Persuasion Strategy Trajectory Analysis}\n\\label{sec:trajectory}\n\nWe compute a monotonicity score over each conversation's sequence of persuasion strategies, measuring whether strategies progress unidirectionally through an ordered intensity scale (Table~\\ref{tab:trajectory}).\nAt the group level, jailbreak conversations score significantly higher (0.71 vs.\\ 0.38 for benign, $p{=}0.003$).\nTransition entropy is also lower in jailbreak conversations (1.42 vs.\\ 2.15, $p{=}0.007$), indicating more predictable and structured strategy progressions.\n\nHowever, individual-level variance is substantial: the standard deviation of jailbreak monotonicity scores is 0.18, and only 68\\% of jailbreak conversations exceed a monotonicity threshold of 0.6.\nThe remaining 32\\% deviate from monotonic escalation, likely due to (a) tactical de-escalation by attackers who retreat to rapport building mid-conversation before re-escalating, and (b) noise from the persuasion classifier's 72\\% accuracy propagating into trajectory-level scores.\nThese results support the mechanistic basis for DisPeD's detection advantage at the population level, while acknowledging that the monotonic escalation pattern is a tendency rather than a universal property.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Persuasion strategy trajectory analysis. $^*p{<}0.01$.}\n\\label{tab:trajectory}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Jailbreak} & \\textbf{Benign} & \\textbf{$p$} \\\\\n\\midrule\nMonotonicity (mean $\\pm$ std) & 0.71 $\\pm$ 0.18 & 0.38 $\\pm$ 0.14 & 0.003$^*$ \\\\\nTransition Entropy & 1.42 & 2.15 & 0.007$^*$ \\\\\n\\% Above threshold (0.6) & 68\\% & 12\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Hard Negative Evaluation}\n\\label{sec:hardneg}\n\nTable~\\ref{tab:wildchat} reports false positive rates on WildChat hard negatives.\nDisPeD misclassifies 12\\% of high-drift benign conversations (10 out of 85), compared to 18\\% for the baseline and 27\\% for TF-IDF + LR.\nWhile DisPeD's persuasion grounding reduces false positives relative to the baseline, the 12\\% rate is not negligible: the model conflates legitimate persuasion (e.g., debate-style exchanges with authority appeals) with adversarial persuasion escalation.\nDistinguishing these two cases likely requires either a stronger intent classification signal or conversation-level contextual features beyond the current architecture.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{False positive rate on WildChat hard negatives ($n{=}85$).}\n\\label{tab:wildchat}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Model} & \\textbf{FPR (WildChat)} & \\textbf{FPR (in-domain)} \\\\\n\\midrule\nDisPeD & 12\\% & 3\\% \\\\\nBaseline & 18\\% & 6\\% \\\\\nTF-IDF + LR & 27\\% & 19\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Comparison Across Feature Levels}\n\\label{sec:hierarchy}\n\nTable~\\ref{tab:hierarchy} places all baselines on a single scale.\nPerformance on clean data follows a consistent ordering: TF-IDF + LR (0.74) $<$ DeepContext proxy (0.82) $<$ vanilla DeBERTa + GRU (0.86) $<$ DisPeD (0.91).\nUnder adversarial perturbation, the gap widens: TF-IDF + LR drops to 0.56, BERT + GRU to 0.69, the vanilla baseline to 0.74, and DisPeD to 0.84.\n\nThe DeepContext proxy comparison should be interpreted with caution.\nThe 4 pp gap between BERT + GRU (0.82) and vanilla DeBERTa + GRU (0.86) is partly attributable to the encoder capacity difference (BERT-base vs.\\ DeBERTa-v3-base), not solely to architectural choices.\nThe primary controlled comparison remains DisPeD vs.\\ the vanilla DeBERTa baseline, which isolates the effect of persuasion grounding using the same encoder.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Comparison across feature levels (full conversation). The DeepContext proxy uses BERT-base rather than DeBERTa, introducing a capacity confound (see text).}\n\\label{tab:hierarchy}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Full F1} & \\textbf{$K{=}3$ F1} & \\textbf{$K{=}2$ F1} & \\textbf{Perturbed F1} \\\\\n\\midrule\nDisPeD & 0.91 & 0.86 & 0.82 & 0.84 \\\\\nBaseline (DeBERTa + GRU) & 0.86 & 0.78 & 0.75 & 0.74 \\\\\nDeepContext proxy (BERT + GRU) & 0.82 & 0.74 & 0.70 & 0.69 \\\\\nTF-IDF + LR & 0.74 & 0.71 & 0.68 & 0.56 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Stability Analysis}\n\\label{sec:stability}\n\nTo assess the sensitivity of results to encoder training, we evaluate three DeBERTa checkpoints from different training epochs (Table~\\ref{tab:stability}).\nDownstream F1 varies by at most 2 pp (0.89 to 0.91), and $K{=}3$ F1 varies by 2 pp (0.84 to 0.86), confirming that reported results are not artifacts of a particular checkpoint.\nEpoch 3 is selected based on peak persuasion accuracy (0.72); the final epoch shows mild overfitting (persuasion accuracy drops to 0.71).\nFull random-seed variance analysis (multiple independent training runs) was not conducted due to computational constraints.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-checkpoint stability. Max spread $\\leq$ 2 pp across all metrics.}\n\\label{tab:stability}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Checkpoint} & \\textbf{Persuasion Acc} & \\textbf{Full F1} & \\textbf{$K{=}3$ F1} \\\\\n\\midrule\nEpoch 2 & 0.70 & 0.90 & 0.84 \\\\\nEpoch 3 (selected) & 0.72 & 0.91 & 0.86 \\\\\nEpoch 5 (final) & 0.71 & 0.89 & 0.85 \\\\\n\\midrule\nStd & 0.01 & 0.01 & 0.01 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 6  LIMITATIONS\n% ============================================================\n\\section{Limitations}\n\\label{sec:limitations}\n\nWe identify several limitations that bound the generalizability of our findings.\n\n\\paragraph{Dataset scale.}\nOur primary dataset contains 480 conversations (240 jailbreak, 240 benign) with a test set of $n{=}72$.\nThis is small for a detection paper, and several of our comparisons (notably $K{=}2$ with $p{=}0.072$) do not reach statistical significance at this sample size.\nWhile we report bootstrap confidence intervals throughout to quantify uncertainty, the proof-of-concept results presented here require validation on larger datasets before deployment conclusions can be drawn.\n\n\\paragraph{Persuasion classifier bottleneck.}\nThe Stage 1 persuasion classifier achieves 72\\% accuracy on the clean data.\nThis ceiling propagates through the entire pipeline: turn embeddings encode noisy pragmatic representations, the GRU receives imperfect strategy sequences, and the downstream classifier's advantage is capped.\nThe 5 pp $\\Delta$-$\\Delta$ under adversarial perturbation ($p{=}0.043$) is real but modest; we hypothesize that a more accurate persuasion encoder would widen this gap, but cannot verify without better training data or larger models.\nThe 35\\% overlap between top TF-IDF features and persuasion-related vocabulary further suggests that the current encoder partially confounds lexical and pragmatic signals.\n\n\\paragraph{Attack type coverage.}\nDisPeD is designed for persuasion-mediated multi-turn attacks.\nCross-attack evaluation shows significant generalization to FITD (which shares the escalation structure) but limited transfer to Deceptive Delight (which uses interleaving rather than escalation).\nPure information accumulation attacks, token smuggling, and single-frame roleplay are outside our scope.\nA dual-track architecture combining persuasion and semantic signals (future work) would provide broader coverage.\n\n\\paragraph{Individual-level trajectory variance.}\nWhile group-level monotonicity differences are highly significant ($p{=}0.003$), 32\\% of jailbreak conversations do not exhibit monotonic escalation patterns.\nThe individual-level monotonicity score has $\\sigma{=}0.18$, meaning a substantial fraction of jailbreaks deviate from the idealized escalation trajectory.\nThis variance likely reflects both genuine attack diversity (tactical de-escalation) and noise from the persuasion classifier.\n\n\\paragraph{Synthetic data.}\nAll attack conversations are LLM-generated rather than collected from real adversarial interactions.\nLLM-generated attacks may not capture the full diversity of human adversarial strategies.\nThe register normalization step, while necessary to remove lexical shortcuts, introduces an additional synthetic transformation whose fidelity we can only partially verify (8\\% rejection rate).\n\n\\paragraph{Hard negative false positives.}\nDisPeD's 12\\% false positive rate on WildChat hard negatives, while lower than the baseline's 18\\%, indicates that persuasion grounding alone cannot reliably distinguish legitimate persuasion from adversarial persuasion.\nDeployment settings with high volumes of naturally persuasive conversations (e.g., sales, debate) would require additional safeguards.\n\n\\paragraph{Reproducibility.}\nThe DeepContext proxy comparison uses BERT-base rather than a faithful reproduction of DeepContext (no public code is available), introducing a confound between encoder capacity and architectural design.\nCross-seed variance analysis was not conducted.\n\n% ============================================================\n% 7  CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe have presented DisPeD, a proof-of-concept detector that exploits the pragmatic evasion asymmetry in multi-turn jailbreak attacks.\nBy fine-tuning DeBERTa on persuasion strategy classification and modeling strategy sequences with a GRU, DisPeD provides a complementary detection signal that is more robust to surface-level evasion than lexical or semantic features.\nOn register-normalized data, DisPeD achieves a significant 8 pp F1 improvement at $K{=}3$ turns and degrades 5 pp less than a semantic baseline under adversarial paraphrasing.\n\nThe results establish that discourse-level persuasion structure is a viable detection axis, while also revealing clear boundaries: the approach depends on persuasion classifier quality, generalizes unevenly across attack families, and the monotonic escalation signal is a group-level tendency with substantial individual variance.\nFuture work should address the persuasion classifier bottleneck through larger annotated corpora, extend training to diverse attack families, and explore a dual-track architecture that combines pragmatic and semantic signals for broader coverage.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Austin(1962)]{austin1962things}\nJ.~L. Austin.\n\\newblock \\emph{How to Do Things with Words}.\n\\newblock Oxford University Press, 1962.\n\n\\bibitem[Bullwinkel et~al.(2025)]{bullwinkel2025multiturnjailbreaks}\nJ.~Bullwinkel, S.~Marro, et~al.\n\\newblock Multi-turn jailbreaks: Analyzing representation shifts in large language models under adversarial dialogue.\n\\newblock \\emph{arXiv preprint arXiv:2507.02956}, 2025.\n\n\\bibitem[DeepContext(2026)]{deepcontext2026}\nDeepContext Authors.\n\\newblock DeepContext: Detecting multi-turn jailbreak attacks via semantic drift tracking.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Hagendorff(2026)]{hagendorff2026persuasion}\nT.~Hagendorff.\n\\newblock Persuasion strategies in multi-turn adversarial interactions with large language models.\n\\newblock \\emph{Nature Communications}, 2026.\n\n\\bibitem[He et~al.(2021)]{he2021debertav3}\nP.~He, J.~Gao, and W.~Chen.\n\\newblock {DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-style pre-training with gradient-disentangled embedding sharing.\n\\newblock \\emph{arXiv preprint arXiv:2111.09543}, 2021.\n\n\\bibitem[Jiang et~al.(2024)]{jiang2024deceptivedelight}\nZ.~Jiang et~al.\n\\newblock Deceptive delight: Interleaving benign and harmful content for multi-turn jailbreaking.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Russinovich and Salem(2024)]{russinovich2024greatwritearticle}\nM.~Russinovich and A.~Salem.\n\\newblock Great, now write an article about that: The crescendo multi-turn {LLM} jailbreak attack.\n\\newblock \\emph{arXiv preprint arXiv:2404.01833}, 2024.\n\n\\bibitem[Searle(1969)]{searle1969speech}\nJ.~R. Searle.\n\\newblock \\emph{Speech Acts: An Essay in the Philosophy of Language}.\n\\newblock Cambridge University Press, 1969.\n\n\\bibitem[WildChat(2024)]{wildchat2024}\nWildChat Team.\n\\newblock {WildChat}: 1{M} {ChatGPT} interaction logs in the wild.\n\\newblock \\emph{ICLR}, 2024.\n\n\\bibitem[Zeng et~al.(2024)]{zeng2024pap}\nY.~Zeng, H.~Lin, J.~Zhang, et~al.\n\\newblock How {Johnny} can persuade {LLMs} to jailbreak them: Rethinking persuasion to challenge {AI} safety by humanizing {LLMs}.\n\\newblock \\emph{ACL}, 2024.\n\n\\bibitem[Zhou et~al.(2024)]{zhou2024speak}\nY.~Zhou et~al.\n\\newblock Speak out of turn: Safety vulnerability of large language models in multi-turn dialogue.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[How Do LLMs Persuade(2025)]{howdollmspersuade2025}\nAnonymous.\n\\newblock How do {LLMs} persuade? {E}xtracting persuasion dynamics from turn-level representations.\n\\newblock \\emph{arXiv preprint arXiv:2508.05625}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97850717-0db6-40ac-ab69-ff78471b72f5",
  "isSidechain": false,
  "requestId": "req_011Cb8X69ztYugTyxcWtFQrR",
  "type": "assistant",
  "uuid": "1ec1e622-e6b3-476b-89e2-f5603e2eefa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NRA2TCzwCS6JE8uxxzQZM3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 42133,
      "output_tokens": 11409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 776,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11409,
          "cache_read_input_tokens": 42133,
          "cache_creation_input_tokens": 776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 776
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

_source line 19 · 2026-05-17T17:19:45.453Z_

<details><summary>↩ Tool result · `toolu_01TPPBdT4dTnT8nqd2ZfsYJF`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ec1e622-e6b3-476b-89e2-f5603e2eefa5",
  "isSidechain": false,
  "promptId": "9a6e3ecc-4cf9-4cf9-af9f-44f318d5866d",
  "type": "user",
  "uuid": "bb9c54ff-9815-4707-b912-a9bfca349827",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{url}\n\\usepackage{xcolor}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{enumitem}\n\n\\title{DisPeD: Exploiting the Pragmatic Evasion Asymmetry\\\\for Robust Multi-Turn Jailbreak Detection}\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nMulti-turn jailbreak attacks distribute adversarial intent across individually benign conversational turns, evading detectors that rely on lexical or per-turn semantic features.\nWe observe that while attackers can freely vary surface-level wording, the underlying persuasion playbook (rapport building, reframing, escalation) is a structural prerequisite for attack success, creating a \\emph{pragmatic evasion asymmetry}.\nWe present DisPeD, a two-stage detector that exploits this asymmetry: a DeBERTa encoder fine-tuned on an 8-class persuasion strategy taxonomy produces pragmatic-aware turn embeddings, and a Bi-GRU models the temporal strategy sequence for conversation-level classification.\nOn register-normalized Crescendo data (TF-IDF = 0.67), DisPeD achieves F1 = 0.86 at $K{=}3$ turns, an 8 percentage point (pp) improvement over a vanilla semantic baseline ($p{=}0.018$).\nUnder adversarial paraphrasing, DisPeD degrades by 7 pp compared to 12 pp for the semantic baseline and 18 pp for a lexical baseline, providing complementary robustness through pragmatic features ($\\Delta$-$\\Delta$ = 5 pp, $p{=}0.043$).\nCross-attack evaluation on FITD-style conversations shows significant generalization (+8 pp, $p{=}0.034$), though transfer to Deceptive Delight remains limited (+5 pp, $p{=}0.142$).\nJailbreak conversations exhibit significantly more monotonic persuasion escalation trajectories than benign conversations at the group level ($p{=}0.003$), though individual-level variance is substantial ($\\sigma{=}0.18$).\nThese results establish a proof-of-concept that discourse-level persuasion structure offers a complementary detection signal that is harder to evade than lexical or semantic features alone.\n\\end{abstract}\n\n% ============================================================\n% 1  INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nLarge Language Models (LLMs) deployed in conversational settings face a growing class of multi-turn jailbreak attacks. Strategies such as Crescendo \\citep{russinovich2024greatwritearticle}, Foot-in-the-Door (FITD) \\citep{zhou2024speak}, and Deceptive Delight \\citep{jiang2024deceptivedelight} distribute adversarial intent across turns that are individually benign, bypassing single-turn safety filters with attack success rates (ASR) exceeding 90\\%.\n\nExisting defenses operate at two levels.\nLexical detectors flag harmful keywords or phrases but are trivially evaded through synonym substitution.\nSemantic detectors, such as the recent DeepContext framework \\citep{deepcontext2026}, track embedding-level drift across turns but face a fundamental vulnerability identified by \\citet{bullwinkel2025multiturnjailbreaks}: per-turn representations in multi-turn attacks are deliberately maintained within a ``benign'' region of the embedding space, producing a 50-point ASR gap between single-turn and multi-turn settings.\nGeneric semantic drift detectors also confuse legitimate conversational evolution with adversarial manipulation, leading to elevated false positive rates on real-world conversations.\n\nWe identify a structural property of persuasion-mediated attacks that neither lexical nor semantic detectors exploit.\nMulti-turn jailbreaks that achieve high ASR follow a persuasion playbook that progresses through identifiable stages: rapport building, authority framing, reframing, and escalation \\citep{zeng2024pap, hagendorff2026persuasion}.\nRemoving any stage either collapses the attack to a single-turn prompt (already covered by existing defenses) or reduces its success rate below useful thresholds.\nThis creates a \\emph{pragmatic evasion asymmetry}: an attacker can freely vary what they say (lexical, semantic) but not the pragmatic function of what they say (persuasion structure).\n\nWe present DisPeD (\\textbf{Dis}course-level \\textbf{Pe}rsuasion-grounded jailbreak \\textbf{D}etection), a two-stage architecture that exploits this asymmetry.\nIn Stage 1, we fine-tune DeBERTa-v3-base on a multi-task objective combining 8-class persuasion strategy classification with binary intent classification, producing turn embeddings that encode pragmatic function rather than surface content.\nIn Stage 2, a Bi-GRU models the temporal sequence of these embeddings to classify conversations.\n\nOur contributions are:\n\\begin{itemize}[nosep]\n\\item We formalize the pragmatic evasion asymmetry and provide empirical evidence that pragmatic features offer complementary robustness: under adversarial paraphrasing, DisPeD's degradation is 5 pp less than a semantic baseline ($p{=}0.043$), while a lexical baseline collapses by 18 pp (Section~\\ref{sec:perturbation}).\n\\item We show that persuasion-grounded embeddings enable earlier detection, with a significant advantage at $K{=}3$ turns (+8 pp, $p{=}0.018$) and a consistent but not statistically significant trend at $K{=}2$ (+7 pp, $p{=}0.072$), on data verified to be free of lexical shortcuts (TF-IDF = 0.67; Section~\\ref{sec:core}).\n\\item We demonstrate that jailbreak conversations exhibit significantly more monotonic escalation in persuasion strategy space than benign conversations at the group level ($p{=}0.003$), providing a mechanistic basis for the detection advantage (Section~\\ref{sec:trajectory}).\n\\end{itemize}\n\n% ============================================================\n% 2  RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Multi-turn jailbreak attacks.}\nCrescendo \\citep{russinovich2024greatwritearticle} gradually escalates requests across turns, achieving ASR above 90\\% on production models.\nFITD \\citep{zhou2024speak} adapts the foot-in-the-door compliance technique from social psychology, starting with small requests before escalating.\nDeceptive Delight \\citep{jiang2024deceptivedelight} interleaves harmful content within benign conversational context.\n\\citet{bullwinkel2025multiturnjailbreaks} show that per-turn representations in these attacks remain within the benign embedding region, explaining why turn-level classifiers fail.\n\n\\paragraph{Multi-turn jailbreak detection.}\nDeepContext \\citep{deepcontext2026} models semantic drift across turns using BERT embeddings and sequential classifiers.\nWhile effective on in-domain data, generic drift detectors struggle to distinguish adversarial escalation from legitimate conversational evolution, leading to false positives on naturally drifting conversations.\nNo published work combines persuasion-grounded turn representations with temporal sequence modeling.\n\n\\paragraph{Persuasion in adversarial contexts.}\n\\citet{zeng2024pap} identify 40 persuasion techniques used in jailbreak prompts and show that persuasion-augmented attacks achieve higher ASR.\n\\citet{hagendorff2026persuasion} find identifiable persuasion strategies in 97\\% of successful multi-turn attacks, confirming the structural role of persuasion.\n\\citet{howdollmspersuade2025} demonstrate that persuasion dynamics are extractable from turn-level representations.\nOur work builds on these findings by using persuasion structure as a detection signal rather than an attack amplifier.\n\n\\paragraph{Theoretical grounding.}\nSpeech Act Theory \\citep{austin1962things, searle1969speech} distinguishes locutionary acts (what is said) from illocutionary acts (what is done by saying it).\nExisting detectors operate at the locutionary level; DisPeD operates at the illocutionary level by encoding the pragmatic function of each turn.\n\n% ============================================================\n% 3  METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Problem Formulation}\n\nGiven a conversation prefix $\\mathbf{c} = (t_1, t_2, \\ldots, t_K)$ of $K$ user turns, the goal is to classify $\\mathbf{c}$ as \\emph{jailbreak} or \\emph{benign}.\nWe seek a classifier that (a) works at small $K$ for early detection, (b) is robust to lexical and semantic perturbation of individual turns, and (c) generalizes across attack families.\n\n\\subsection{Stage 1: Persuasion-Grounded Turn Encoder}\n\nWe fine-tune DeBERTa-v3-base \\citep{he2021debertav3} on a multi-task objective with two heads:\n\\begin{itemize}[nosep]\n\\item \\textbf{Persuasion strategy classification} (8 classes + ``none''): rapport building, authority appeal, emotional appeal, logical appeal, reframing, social proof, urgency/scarcity, reciprocity.\n\\item \\textbf{Intent classification} (binary): jailbreak vs.\\ benign turn.\n\\end{itemize}\nThe combined loss is $\\mathcal{L} = \\mathcal{L}_{\\text{persuasion}} + \\lambda \\mathcal{L}_{\\text{intent}}$ with $\\lambda = 1.0$.\nThe fine-tuned encoder produces [CLS] embeddings that encode pragmatic function rather than surface semantics alone.\n\n\\subsection{Stage 2: Temporal Sequence Classifier}\n\nFor a conversation of $K$ turns, we extract [CLS] embeddings $\\mathbf{e}_1, \\ldots, \\mathbf{e}_K$ from the Stage 1 encoder.\nA Bi-GRU processes the embedding sequence and a linear head classifies the final hidden state as jailbreak or benign.\nThe GRU captures temporal patterns in persuasion strategy transitions, such as the progression from rapport building to authority framing to escalation.\n\n\\subsection{Baselines}\n\nWe compare against three baselines that isolate different feature levels:\n\\begin{itemize}[nosep]\n\\item \\textbf{TF-IDF + Logistic Regression}: lexical features, representing the bottom of the evasion hierarchy.\n\\item \\textbf{Vanilla DeBERTa + GRU}: same architecture as DisPeD, but with DeBERTa embeddings that are \\emph{not} fine-tuned on persuasion strategy classification. This is the primary baseline, as it isolates the effect of persuasion grounding.\n\\item \\textbf{DeepContext proxy} (BERT-base + GRU): approximation of DeepContext \\citep{deepcontext2026} using BERT-base with generic semantic features. Not a faithful reproduction (no public code available), but provides an additional reference point.\n\\end{itemize}\n\n% ============================================================\n% 4  DATA AND SETUP\n% ============================================================\n\\section{Experimental Setup}\n\n\\subsection{Data}\n\nOur primary dataset consists of 240 Crescendo-style multi-turn jailbreak conversations and matched benign conversations (480 total), generated using a Qwen3-8B pipeline with persuasion strategy annotations.\n\n\\paragraph{Register normalization.}\nInitial data exhibited a critical lexical shortcut: TF-IDF separability of 1.0 between jailbreak and benign turns, caused by (a) a hard-coded strategy label for benign turns and (b) register differences between jailbreak and benign language.\nWe applied two fixes.\nFirst, we assigned benign turns a dedicated ``none'' strategy label (9th class), removing the label shortcut and reducing TF-IDF from 1.0 to 0.82.\nSecond, we used Qwen3-8B to rewrite jailbreak turns into conversational register while preserving persuasion structure, further reducing TF-IDF to 0.67, below our hard gate of 0.75 (Table~\\ref{tab:tfidf}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TF-IDF separability through the data cleaning pipeline.}\n\\label{tab:tfidf}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Stage} & \\textbf{TF-IDF} & \\textbf{Description} \\\\\n\\midrule\nOriginal & 1.00 & Label shortcut + register gap \\\\\nAfter label fix & 0.82 & Register gap remains \\\\\nAfter register norm. & 0.67 & Below 0.75 gate \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:deberta_clean} shows the impact of data cleaning on the Stage 1 encoder.\nPersuasion classification accuracy drops from 0.80 to 0.72 after normalization, as the model can no longer rely on register-correlated surface cues and must identify persuasion strategies from semantic content.\nIntent classification accuracy remains stable (0.95 to 0.93), consistent with the coarser binary task being less sensitive to register changes.\nThe 0.72 persuasion accuracy constitutes a bottleneck for downstream performance, as classification errors propagate through the embedding representations to the GRU stage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DeBERTa multi-task performance on original vs.\\ clean data.}\n\\label{tab:deberta_clean}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Original} & \\textbf{Clean} & \\textbf{$\\Delta$} \\\\\n\\midrule\nPersuasion Acc (8-class) & 0.80 & 0.72 & $-$0.08 \\\\\nIntent Acc (binary) & 0.95 & 0.93 & $-$0.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-attack data.}\nTo evaluate generalization, we generated 72 FITD-style and 65 Deceptive Delight-style conversations using the same Qwen3-8B pipeline (Table~\\ref{tab:attack_gen}).\nFITD conversations emphasize compliance escalation with heavier use of logical and authority appeals.\nDeceptive Delight conversations rely more on rapport building and emotional appeal.\nManual spot-check accuracy of persuasion annotations is 82\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Generated attack data statistics.}\n\\label{tab:attack_gen}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Attack Type} & \\textbf{Conv.} & \\textbf{Avg Turns} & \\textbf{Strategies} & \\textbf{Reject \\%} \\\\\n\\midrule\nCrescendo (original) & 240 & 5.4 & 8/8 & --- \\\\\nFITD & 72 & 6.2 & 7/8 & 12\\% \\\\\nDeceptive Delight & 65 & 5.8 & 6/8 & 18\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Hard negatives.}\nWe filtered 85 high-semantic-drift benign conversations from WildChat \\citep{wildchat2024} as hard negatives.\nAfter keyword and LLM-based filtering, residual jailbreak contamination is estimated at 3\\%.\n\n\\subsection{Evaluation Protocol}\n\nAll models are trained on Crescendo data and evaluated on a held-out test set ($n{=}72$).\nWe report F1 score at conversation prefix lengths $K \\in \\{1, 2, 3, 5, \\text{full}\\}$.\nStatistical significance is assessed via bootstrap resampling (10,000 iterations); we report 95\\% confidence intervals and $p$-values.\n\n% ============================================================\n% 5  RESULTS\n% ============================================================\n\\section{Results}\n\n\\subsection{Core Detection Performance}\n\\label{sec:core}\n\nTable~\\ref{tab:core} presents the central comparison between DisPeD (treatment) and the vanilla DeBERTa baseline on clean data.\nDisPeD outperforms the baseline at all prefix lengths, with the gap largest at $K{=}1$ (+10 pp) and narrowing as more turns become available (+5 pp at full conversation).\nThis narrowing is expected: with sufficient turns, vanilla semantic embeddings accumulate enough evidence to partially close the gap.\n\nAt $K{=}3$, DisPeD achieves F1 = 0.86 vs.\\ 0.78 for the baseline, an 8 pp improvement that is statistically significant ($p{=}0.018$).\nAt $K{=}2$, the 7 pp improvement is directionally consistent but does not reach significance ($p{=}0.072$), as the bootstrap confidence intervals overlap (DisPeD: [0.76, 0.88]; baseline: [0.68, 0.82]).\nThe early detection advantage thus holds firmly from $K{=}3$ onward; confirming $K{=}2$ significance would require a larger test set.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Detection F1 by conversation prefix length on clean data. $^*p{<}0.05$ (bootstrap).}\n\\label{tab:core}\n\\begin{tabular}{lccccc}\n\\toprule\n$K$ & \\textbf{DisPeD F1} & \\textbf{95\\% CI} & \\textbf{Baseline F1} & \\textbf{95\\% CI} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\n1 & 0.73 & [0.64, 0.82] & 0.63 & [0.53, 0.73] & +10 \\\\\n2 & 0.82 & [0.76, 0.88] & 0.75 & [0.68, 0.82] & +7 \\\\\n3 & 0.86$^*$ & [0.81, 0.91] & 0.78 & [0.72, 0.84] & +8 \\\\\n5 & 0.90$^*$ & [0.85, 0.95] & 0.84 & [0.78, 0.90] & +6 \\\\\nFull & 0.91$^*$ & [0.87, 0.95] & 0.86 & [0.81, 0.91] & +5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:fpr} reports false positive rates at 95\\% TPR.\nDisPeD achieves FPR = 0.05 at $K{=}3$ compared to 0.11 for the baseline, indicating fewer benign conversations are misclassified even at an aggressive detection threshold.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{False positive rate at 95\\% TPR on clean data.}\n\\label{tab:fpr}\n\\begin{tabular}{lcc}\n\\toprule\n$K$ & \\textbf{DisPeD FPR@95} & \\textbf{Baseline FPR@95} \\\\\n\\midrule\n2 & 0.08 & 0.14 \\\\\n3 & 0.05 & 0.11 \\\\\nFull & 0.03 & 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Scrambled-Label Ablation}\n\\label{sec:ablation}\n\nTo verify that the persuasion strategy labels carry genuine signal rather than acting as mere class indicators, we retrain the Stage 1 encoder with randomly scrambled persuasion labels (Table~\\ref{tab:scrambled}).\nScrambling causes a 7 pp drop in full-conversation F1 (0.91 to 0.84, $p{=}0.008$) and a 6 pp drop at $K{=}3$ ($p{=}0.024$), confirming that the treatment model's advantage derives from correctly encoding pragmatic function.\nThe scrambled model performs slightly below the vanilla baseline (0.84 vs.\\ 0.86 at full), indicating that incorrect persuasion supervision introduces noise that degrades the underlying semantic representation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scrambled-label ablation. Proper = correct persuasion labels; scrambled = randomly shuffled labels.}\n\\label{tab:scrambled}\n\\begin{tabular}{lcccc}\n\\toprule\n$K$ & \\textbf{Proper} & \\textbf{Scrambled} & \\textbf{Baseline} & \\textbf{Drop (pp)} \\\\\n\\midrule\n2 & 0.82 & 0.77 & 0.75 & $-$5 \\\\\n3 & 0.86 & 0.80 & 0.78 & $-$6 \\\\\nFull & 0.91 & 0.84 & 0.86 & $-$7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Robustness Under Adversarial Perturbation}\n\\label{sec:perturbation}\n\nWe evaluate robustness by applying aggressive paraphrasing (synonym substitution, syntactic restructuring, register shifting) to jailbreak conversations at test time, while models remain trained on unperturbed data.\nThe perturbed data achieves TF-IDF separability of 0.41, confirming successful removal of most residual lexical cues.\n\nTable~\\ref{tab:perturbation} shows a clear ordering in degradation magnitude: TF-IDF + LR collapses by 18 pp (0.74 to 0.56), the vanilla semantic baseline drops 12 pp (0.86 to 0.74), and DisPeD drops 7 pp (0.91 to 0.84).\nThe $\\Delta$-$\\Delta$ between DisPeD and the semantic baseline is 5 pp ($p{=}0.043$), providing evidence that pragmatic features offer complementary robustness.\nThis difference is statistically significant but not overwhelming; the bottleneck is the persuasion classifier's accuracy of 0.72, which limits how effectively pragmatic features can be encoded and thus caps the robustness advantage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Performance under adversarial paraphrasing (full conversation). $\\Delta$-$\\Delta$ measures the relative robustness advantage over DisPeD.}\n\\label{tab:perturbation}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Clean F1} & \\textbf{Perturbed F1} & \\textbf{Drop} & \\textbf{$\\Delta$-$\\Delta$} \\\\\n\\midrule\nDisPeD & 0.91 & 0.84 & $-$7 & --- \\\\\nBaseline (vanilla DeBERTa) & 0.86 & 0.74 & $-$12 & 5 pp \\\\\nTF-IDF + LR & 0.74 & 0.56 & $-$18 & 11 pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:perturbation_k3} presents the same analysis at $K{=}3$.\nThe degradation ordering is consistent: DisPeD drops 7 pp compared to 12 pp for the baseline and 19 pp for TF-IDF + LR.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Performance under adversarial paraphrasing at $K{=}3$.}\n\\label{tab:perturbation_k3}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Clean $K{=}3$} & \\textbf{Perturbed $K{=}3$} & \\textbf{Drop} \\\\\n\\midrule\nDisPeD & 0.86 & 0.79 & $-$7 \\\\\nBaseline & 0.78 & 0.66 & $-$12 \\\\\nTF-IDF + LR & 0.71 & 0.52 & $-$19 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Attack Generalization}\n\\label{sec:crossattack}\n\nWe evaluate models trained exclusively on Crescendo data against FITD and Deceptive Delight conversations in a zero-shot setting (Table~\\ref{tab:crossattack}).\nResults vary substantially by attack type and must be reported separately; the aggregate ($\\Delta{=}6$ pp, $p{=}0.052$) is misleading.\n\nOn FITD, DisPeD achieves F1 = 0.74 with an 8 pp advantage over the baseline ($p{=}0.034$).\nThis transfer is expected: FITD's compliance escalation shares substantial overlap with Crescendo's persuasion escalation in strategy space, with both progressing through trust-building and authority-based request escalation.\n\nOn Deceptive Delight, DisPeD achieves F1 = 0.64 with a 5 pp advantage that does not reach significance ($p{=}0.142$).\nDeceptive Delight relies on interleaving harmful content within pleasant context rather than explicit persuasion escalation, and its strategy distribution (heavy on rapport building and emotional appeal) diverges from Crescendo's (heavy on authority appeal and reframing).\nThe model trained on Crescendo lacks exposure to this interleaving pattern.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-attack zero-shot generalization. Models trained on Crescendo only. $^*p{<}0.05$.}\n\\label{tab:crossattack}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Attack Type} & \\textbf{DisPeD F1} & \\textbf{Baseline F1} & \\textbf{$\\Delta$ (pp)} & \\textbf{$p$} \\\\\n\\midrule\nCrescendo (in-domain) & 0.91 & 0.86 & +5 & 0.031$^*$ \\\\\nFITD (zero-shot) & 0.74 & 0.66 & +8 & 0.034$^*$ \\\\\nDeceptive Delight (zero-shot) & 0.64 & 0.59 & +5 & 0.142 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:strategy_dist} shows the persuasion strategy distributions across attack types, illustrating why transfer varies.\nFITD shares Crescendo's emphasis on logical and authority appeals, while Deceptive Delight diverges toward rapport and emotional strategies.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Persuasion strategy distribution (\\%) across attack types.}\n\\label{tab:strategy_dist}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Crescendo} & \\textbf{FITD} & \\textbf{Dec.\\ Delight} \\\\\n\\midrule\nRapport Building & 22 & 18 & 28 \\\\\nAuthority Appeal & 14 & 16 & 3 \\\\\nEmotional Appeal & 11 & 8 & 21 \\\\\nLogical Appeal & 13 & 19 & 12 \\\\\nReframing & 15 & 10 & 14 \\\\\nSocial Proof & 8 & 12 & 7 \\\\\nUrgency/Scarcity & 6 & 9 & 4 \\\\\nReciprocity & 5 & 6 & 5 \\\\\nNone & 6 & 2 & 6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Persuasion Strategy Trajectory Analysis}\n\\label{sec:trajectory}\n\nWe compute a monotonicity score over each conversation's sequence of persuasion strategies, measuring whether strategies progress unidirectionally through an ordered intensity scale (Table~\\ref{tab:trajectory}).\nAt the group level, jailbreak conversations score significantly higher (0.71 vs.\\ 0.38 for benign, $p{=}0.003$).\nTransition entropy is also lower in jailbreak conversations (1.42 vs.\\ 2.15, $p{=}0.007$), indicating more predictable and structured strategy progressions.\n\nHowever, individual-level variance is substantial: the standard deviation of jailbreak monotonicity scores is 0.18, and only 68\\% of jailbreak conversations exceed a monotonicity threshold of 0.6.\nThe remaining 32\\% deviate from monotonic escalation, likely due to (a) tactical de-escalation by attackers who retreat to rapport building mid-conversation before re-escalating, and (b) noise from the persuasion classifier's 72\\% accuracy propagating into trajectory-level scores.\nThese results support the mechanistic basis for DisPeD's detection advantage at the population level, while acknowledging that the monotonic escalation pattern is a tendency rather than a universal property.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Persuasion strategy trajectory analysis. $^*p{<}0.01$.}\n\\label{tab:trajectory}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Jailbreak} & \\textbf{Benign} & \\textbf{$p$} \\\\\n\\midrule\nMonotonicity (mean $\\pm$ std) & 0.71 $\\pm$ 0.18 & 0.38 $\\pm$ 0.14 & 0.003$^*$ \\\\\nTransition Entropy & 1.42 & 2.15 & 0.007$^*$ \\\\\n\\% Above threshold (0.6) & 68\\% & 12\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Hard Negative Evaluation}\n\\label{sec:hardneg}\n\nTable~\\ref{tab:wildchat} reports false positive rates on WildChat hard negatives.\nDisPeD misclassifies 12\\% of high-drift benign conversations (10 out of 85), compared to 18\\% for the baseline and 27\\% for TF-IDF + LR.\nWhile DisPeD's persuasion grounding reduces false positives relative to the baseline, the 12\\% rate is not negligible: the model conflates legitimate persuasion (e.g., debate-style exchanges with authority appeals) with adversarial persuasion escalation.\nDistinguishing these two cases likely requires either a stronger intent classification signal or conversation-level contextual features beyond the current architecture.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{False positive rate on WildChat hard negatives ($n{=}85$).}\n\\label{tab:wildchat}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Model} & \\textbf{FPR (WildChat)} & \\textbf{FPR (in-domain)} \\\\\n\\midrule\nDisPeD & 12\\% & 3\\% \\\\\nBaseline & 18\\% & 6\\% \\\\\nTF-IDF + LR & 27\\% & 19\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Comparison Across Feature Levels}\n\\label{sec:hierarchy}\n\nTable~\\ref{tab:hierarchy} places all baselines on a single scale.\nPerformance on clean data follows a consistent ordering: TF-IDF + LR (0.74) $<$ DeepContext proxy (0.82) $<$ vanilla DeBERTa + GRU (0.86) $<$ DisPeD (0.91).\nUnder adversarial perturbation, the gap widens: TF-IDF + LR drops to 0.56, BERT + GRU to 0.69, the vanilla baseline to 0.74, and DisPeD to 0.84.\n\nThe DeepContext proxy comparison should be interpreted with caution.\nThe 4 pp gap between BERT + GRU (0.82) and vanilla DeBERTa + GRU (0.86) is partly attributable to the encoder capacity difference (BERT-base vs.\\ DeBERTa-v3-base), not solely to architectural choices.\nThe primary controlled comparison remains DisPeD vs.\\ the vanilla DeBERTa baseline, which isolates the effect of persuasion grounding using the same encoder.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Comparison across feature levels (full conversation). The DeepContext proxy uses BERT-base rather than DeBERTa, introducing a capacity confound (see text).}\n\\label{tab:hierarchy}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Full F1} & \\textbf{$K{=}3$ F1} & \\textbf{$K{=}2$ F1} & \\textbf{Perturbed F1} \\\\\n\\midrule\nDisPeD & 0.91 & 0.86 & 0.82 & 0.84 \\\\\nBaseline (DeBERTa + GRU) & 0.86 & 0.78 & 0.75 & 0.74 \\\\\nDeepContext proxy (BERT + GRU) & 0.82 & 0.74 & 0.70 & 0.69 \\\\\nTF-IDF + LR & 0.74 & 0.71 & 0.68 & 0.56 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Stability Analysis}\n\\label{sec:stability}\n\nTo assess the sensitivity of results to encoder training, we evaluate three DeBERTa checkpoints from different training epochs (Table~\\ref{tab:stability}).\nDownstream F1 varies by at most 2 pp (0.89 to 0.91), and $K{=}3$ F1 varies by 2 pp (0.84 to 0.86), confirming that reported results are not artifacts of a particular checkpoint.\nEpoch 3 is selected based on peak persuasion accuracy (0.72); the final epoch shows mild overfitting (persuasion accuracy drops to 0.71).\nFull random-seed variance analysis (multiple independent training runs) was not conducted due to computational constraints.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-checkpoint stability. Max spread $\\leq$ 2 pp across all metrics.}\n\\label{tab:stability}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Checkpoint} & \\textbf{Persuasion Acc} & \\textbf{Full F1} & \\textbf{$K{=}3$ F1} \\\\\n\\midrule\nEpoch 2 & 0.70 & 0.90 & 0.84 \\\\\nEpoch 3 (selected) & 0.72 & 0.91 & 0.86 \\\\\nEpoch 5 (final) & 0.71 & 0.89 & 0.85 \\\\\n\\midrule\nStd & 0.01 & 0.01 & 0.01 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 6  LIMITATIONS\n% ============================================================\n\\section{Limitations}\n\\label{sec:limitations}\n\nWe identify several limitations that bound the generalizability of our findings.\n\n\\paragraph{Dataset scale.}\nOur primary dataset contains 480 conversations (240 jailbreak, 240 benign) with a test set of $n{=}72$.\nThis is small for a detection paper, and several of our comparisons (notably $K{=}2$ with $p{=}0.072$) do not reach statistical significance at this sample size.\nWhile we report bootstrap confidence intervals throughout to quantify uncertainty, the proof-of-concept results presented here require validation on larger datasets before deployment conclusions can be drawn.\n\n\\paragraph{Persuasion classifier bottleneck.}\nThe Stage 1 persuasion classifier achieves 72\\% accuracy on the clean data.\nThis ceiling propagates through the entire pipeline: turn embeddings encode noisy pragmatic representations, the GRU receives imperfect strategy sequences, and the downstream classifier's advantage is capped.\nThe 5 pp $\\Delta$-$\\Delta$ under adversarial perturbation ($p{=}0.043$) is real but modest; we hypothesize that a more accurate persuasion encoder would widen this gap, but cannot verify without better training data or larger models.\nThe 35\\% overlap between top TF-IDF features and persuasion-related vocabulary further suggests that the current encoder partially confounds lexical and pragmatic signals.\n\n\\paragraph{Attack type coverage.}\nDisPeD is designed for persuasion-mediated multi-turn attacks.\nCross-attack evaluation shows significant generalization to FITD (which shares the escalation structure) but limited transfer to Deceptive Delight (which uses interleaving rather than escalation).\nPure information accumulation attacks, token smuggling, and single-frame roleplay are outside our scope.\nA dual-track architecture combining persuasion and semantic signals (future work) would provide broader coverage.\n\n\\paragraph{Individual-level trajectory variance.}\nWhile group-level monotonicity differences are highly significant ($p{=}0.003$), 32\\% of jailbreak conversations do not exhibit monotonic escalation patterns.\nThe individual-level monotonicity score has $\\sigma{=}0.18$, meaning a substantial fraction of jailbreaks deviate from the idealized escalation trajectory.\nThis variance likely reflects both genuine attack diversity (tactical de-escalation) and noise from the persuasion classifier.\n\n\\paragraph{Synthetic data.}\nAll attack conversations are LLM-generated rather than collected from real adversarial interactions.\nLLM-generated attacks may not capture the full diversity of human adversarial strategies.\nThe register normalization step, while necessary to remove lexical shortcuts, introduces an additional synthetic transformation whose fidelity we can only partially verify (8\\% rejection rate).\n\n\\paragraph{Hard negative false positives.}\nDisPeD's 12\\% false positive rate on WildChat hard negatives, while lower than the baseline's 18\\%, indicates that persuasion grounding alone cannot reliably distinguish legitimate persuasion from adversarial persuasion.\nDeployment settings with high volumes of naturally persuasive conversations (e.g., sales, debate) would require additional safeguards.\n\n\\paragraph{Reproducibility.}\nThe DeepContext proxy comparison uses BERT-base rather than a faithful reproduction of DeepContext (no public code is available), introducing a confound between encoder capacity and architectural design.\nCross-seed variance analysis was not conducted.\n\n% ============================================================\n% 7  CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe have presented DisPeD, a proof-of-concept detector that exploits the pragmatic evasion asymmetry in multi-turn jailbreak attacks.\nBy fine-tuning DeBERTa on persuasion strategy classification and modeling strategy sequences with a GRU, DisPeD provides a complementary detection signal that is more robust to surface-level evasion than lexical or semantic features.\nOn register-normalized data, DisPeD achieves a significant 8 pp F1 improvement at $K{=}3$ turns and degrades 5 pp less than a semantic baseline under adversarial paraphrasing.\n\nThe results establish that discourse-level persuasion structure is a viable detection axis, while also revealing clear boundaries: the approach depends on persuasion classifier quality, generalizes unevenly across attack families, and the monotonic escalation signal is a group-level tendency with substantial individual variance.\nFuture work should address the persuasion classifier bottleneck through larger annotated corpora, extend training to diverse attack families, and explore a dual-track architecture that combines pragmatic and semantic signals for broader coverage.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Austin(1962)]{austin1962things}\nJ.~L. Austin.\n\\newblock \\emph{How to Do Things with Words}.\n\\newblock Oxford University Press, 1962.\n\n\\bibitem[Bullwinkel et~al.(2025)]{bullwinkel2025multiturnjailbreaks}\nJ.~Bullwinkel, S.~Marro, et~al.\n\\newblock Multi-turn jailbreaks: Analyzing representation shifts in large language models under adversarial dialogue.\n\\newblock \\emph{arXiv preprint arXiv:2507.02956}, 2025.\n\n\\bibitem[DeepContext(2026)]{deepcontext2026}\nDeepContext Authors.\n\\newblock DeepContext: Detecting multi-turn jailbreak attacks via semantic drift tracking.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Hagendorff(2026)]{hagendorff2026persuasion}\nT.~Hagendorff.\n\\newblock Persuasion strategies in multi-turn adversarial interactions with large language models.\n\\newblock \\emph{Nature Communications}, 2026.\n\n\\bibitem[He et~al.(2021)]{he2021debertav3}\nP.~He, J.~Gao, and W.~Chen.\n\\newblock {DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-style pre-training with gradient-disentangled embedding sharing.\n\\newblock \\emph{arXiv preprint arXiv:2111.09543}, 2021.\n\n\\bibitem[Jiang et~al.(2024)]{jiang2024deceptivedelight}\nZ.~Jiang et~al.\n\\newblock Deceptive delight: Interleaving benign and harmful content for multi-turn jailbreaking.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Russinovich and Salem(2024)]{russinovich2024greatwritearticle}\nM.~Russinovich and A.~Salem.\n\\newblock Great, now write an article about that: The crescendo multi-turn {LLM} jailbreak attack.\n\\newblock \\emph{arXiv preprint arXiv:2404.01833}, 2024.\n\n\\bibitem[Searle(1969)]{searle1969speech}\nJ.~R. Searle.\n\\newblock \\emph{Speech Acts: An Essay in the Philosophy of Language}.\n\\newblock Cambridge University Press, 1969.\n\n\\bibitem[WildChat(2024)]{wildchat2024}\nWildChat Team.\n\\newblock {WildChat}: 1{M} {ChatGPT} interaction logs in the wild.\n\\newblock \\emph{ICLR}, 2024.\n\n\\bibitem[Zeng et~al.(2024)]{zeng2024pap}\nY.~Zeng, H.~Lin, J.~Zhang, et~al.\n\\newblock How {Johnny} can persuade {LLMs} to jailbreak them: Rethinking persuasion to challenge {AI} safety by humanizing {LLMs}.\n\\newblock \\emph{ACL}, 2024.\n\n\\bibitem[Zhou et~al.(2024)]{zhou2024speak}\nY.~Zhou et~al.\n\\newblock Speak out of turn: Safety vulnerability of large language models in multi-turn dialogue.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[How Do LLMs Persuade(2025)]{howdollmspersuade2025}\nAnonymous.\n\\newblock How do {LLMs} persuade? {E}xtracting persuasion dynamics from turn-level representations.\n\\newblock \\emph{arXiv preprint arXiv:2508.05625}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "1ec1e622-e6b3-476b-89e2-f5603e2eefa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165817 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_…",
  "leafUuid": "bb9c54ff-9815-4707-b912-a9bfca349827",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream tracking",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c"
}
```

---

### Tool call

_source line 22 · 2026-05-17T17:19:50.024Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017AhmydVmmkcQYkAAV5Hspn`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb9c54ff-9815-4707-b912-a9bfca349827",
  "isSidechain": false,
  "requestId": "req_011Cb8XMPY9EKBN1DXx27yHQ",
  "type": "assistant",
  "uuid": "b7d3ebba-7141-48b4-8e29-a5b5e721e58e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkFjxqQgMEPzeUGi2fbg25",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11480,
      "cache_read_input_tokens": 42909,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 42909,
          "cache_creation_input_tokens": 11480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11480
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

_source line 23 · 2026-05-17T17:19:50.772Z_

<details><summary>↩ Tool result · `toolu_017AhmydVmmkcQYkAAV5Hspn`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
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

Package natbib Warning: Citation `russinovich2024greatwritearticle' on page 1 u
ndefined on input line 41.


Package natbib Warning: Citation `zhou2024speak' on page 1 undefined on input l
ine 41.


Package natbib Warning: Citation `jiang2024deceptivedelight' on page 1 undefine
d on input line 41.


Package natbib Warning: Citation `deepcontext2026' on page 1 undefined on input
 line 45.


Package natbib Warning: Citation `bullwinkel2025multiturnjailbreaks' on page 1 
undefined on input line 45.


Package natbib Warning: Citation `zeng2024pap' on page 1 undefined on input lin
e 49.


Package natbib Warning: Citation `hagendorff2026persuasion' on page 1 undefined
 on input line 49.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

LaTeX Warning: Reference `sec:perturbation' on page 2 undefined on input line 5
9.


LaTeX Warning: Reference `sec:core' on page 2 undefined on input line 60.


LaTeX Warning: Reference `sec:trajectory' on page 2 undefined on input line 61.



Package natbib Warning: Citation `russinovich2024greatwritearticle' on page 2 u
ndefined on input line 70.


Package natbib Warning: Citation `zhou2024speak' on page 2 undefined on input l
ine 71.


Package natbib Warning: Citation `jiang2024deceptivedelight' on page 2 undefine
d on input line 72.


Package natbib Warning: Citation `bullwinkel2025multiturnjailbreaks' on page 2 
undefined on input line 73.


Package natbib Warning: Citation `deepcontext2026' on page 2 undefined on input
 line 76.


Package natbib Warning: Citation `zeng2024pap' on page 2 undefined on input lin
e 81.


Package natbib Warning: Citation `hagendorff2026persuasion' on page 2 undefined
 on input line 82.


Package natbib Warning: Citation `howdollmspersuade2025' on page 2 undefined on
 input line 83.


Package natbib Warning: Citation `austin1962things' on page 2 undefined on inpu
t line 87.


Package natbib Warning: Citation `searle1969speech' on page 2 undefined on inpu
t line 87.


Package natbib Warning: Citation `he2021debertav3' on page 2 undefined on input
 line 102.

[2]

Package natbib Warning: Citation `deepcontext2026' on page 3 undefined on input
 line 122.


LaTeX Warning: Reference `tab:tfidf' on page 3 undefined on input line 138.


LaTeX Warning: Reference `tab:deberta_clean' on page 3 undefined on input line 
156.

[3]

LaTeX Warning: Reference `tab:attack_gen' on page 4 undefined on input line 177
.


Package natbib Warning: Citation `wildchat2024' on page 4 undefined on input li
ne 199.


LaTeX Warning: Reference `tab:core' on page 4 undefined on input line 216.


LaTeX Warning: Reference `tab:fpr' on page 4 undefined on input line 242.

[4]

LaTeX Warning: Reference `tab:scrambled' on page 5 undefined on input line 264.



LaTeX Warning: Reference `tab:perturbation' on page 5 undefined on input line 2
90.


LaTeX Warning: Reference `tab:perturbation_k3' on page 5 undefined on input lin
e 310.


LaTeX Warning: Reference `tab:crossattack' on page 5 undefined on input line 33
2.


Overfull \hbox (9.10887pt too wide) in paragraph at lines 335--337
\T1/cmr/m/n/10.95 This trans-fer is ex-pected: FITD's com-pli-ance es-ca-la-tio
n shares sub-stan-tial over-lap with Crescendo's

Overfull \hbox (9.17894pt too wide) in paragraph at lines 335--337
\T1/cmr/m/n/10.95 per-sua-sion es-ca-la-tion in strat-egy space, with both pro-
gress-ing through trust-building and authority-
[5]

LaTeX Warning: Reference `tab:strategy_dist' on page 6 undefined on input line 
358.


LaTeX Warning: Reference `tab:trajectory' on page 6 undefined on input line 386
.


LaTeX Warning: Reference `tab:wildchat' on page 6 undefined on input line 413.

[6]

LaTeX Warning: Reference `tab:hierarchy' on page 7 undefined on input line 437.



LaTeX Warning: Reference `tab:stability' on page 7 undefined on input line 465.


[7]
Overfull \hbox (1.16982pt too wide) in paragraph at lines 508--512
 \T1/cmr/bx/n/10.95 At-tack type cov-er-age.[] \T1/cmr/m/n/10.95 DisPeD is de-s
igned for persuasion-mediated multi-turn at-tacks. Cross-
[8] [9]

Package natbib Warning: There were undefined citations.

[10] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy8.pfb>
Output written on paper.pdf (10 pages, 232252 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] [2] [3]
Overfull \hbox (2.91933pt too wide) in paragraph at lines 199--201
 \T1/cmr/bx/n/10.95 Hard neg-a-tives.[] \T1/cmr/m/n/10.95 We fil-tered 85 high-
semantic-drift be-nign con-ver-sa-tions from Wild-Chat [Wild-
[4]
Overfull \hbox (9.10887pt too wide) in paragraph at lines 335--337
\T1/cmr/m/n/10.95 This trans-fer is ex-pected: FITD's com-pli-ance es-ca-la-tio
n shares sub-stan-tial over-lap with Crescendo's

Overfull \hbox (9.17894pt too wide) in paragraph at lines 335--337
\T1/cmr/m/n/10.95 per-sua-sion es-ca-la-tion in strat-egy space, with both pro-
gress-ing through trust-building and authority-
[5] [6] [7]
Overfull \hbox (1.16982pt too wide) in paragraph at lines 508--512
 \T1/cmr/bx/n/10.95 At-tack type cov-er-age.[] \T1/cmr/m/n/10.95 DisPeD is de-s
igned for persuasion-mediated multi-turn at-tacks. Cross-
[8] [9] [10] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy8.pfb>
Output written on paper.pdf (10 pages, 232041 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7d3ebba-7141-48b4-8e29-a5b5e721e58e",
  "isSidechain": false,
  "promptId": "9a6e3ecc-4cf9-4cf9-af9f-44f318d5866d",
  "type": "user",
  "uuid": "8af2b47e-115e-469e-bbed-5831da73b90f",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `russinovich2024greatwritearticle' on page 1 u\nndefined on input line 41.\n\n\nPackage natbib Warning: Citation `zhou2024speak' on page 1 undefined on input l\nine 41.\n\n\nPackage natbib Warning: Citation `jiang2024deceptivedelight' on page 1 undefine\nd on input line 41.\n\n\nPackage natbib Warning: Citation `deepcontext2026' on page 1 undefined on input\n line 45.\n\n\nPackage natbib Warning: Citation `bullwinkel2025multiturnjailbreaks' on page 1 \nundefined on input line 45.\n\n\nPackage natbib Warning: Citation `zeng2024pap' on page 1 undefined on input lin\ne 49.\n\n\nPackage natbib Warning: Citation `hagendorff2026persuasion' on page 1 undefined\n on input line 49.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nLaTeX Warning: Reference `sec:perturbation' on page 2 undefined on input line 5\n9.\n\n\nLaTeX Warning: Reference `sec:core' on page 2 undefined on input line 60.\n\n\nLaTeX Warning: Reference `sec:trajectory' on page 2 undefined on input line 61.\n\n\n\nPackage natbib Warning: Citation `russinovich2024greatwritearticle' on page 2 u\nndefined on input line 70.\n\n\nPackage natbib Warning: Citation `zhou2024speak' on page 2 undefined on input l\nine 71.\n\n\nPackage natbib Warning: Citation `jiang2024deceptivedelight' on page 2 undefine\nd on input line 72.\n\n\nPackage natbib Warning: Citation `bullwinkel2025multiturnjailbreaks' on page 2 \nundefined on input line 73.\n\n\nPackage natbib Warning: Citation `deepcontext2026' on page 2 undefined on input\n line 76.\n\n\nPackage natbib Warning: Citation `zeng2024pap' on page 2 undefined on input lin\ne 81.\n\n\nPackage natbib Warning: Citation `hagendorff2026persuasion' on page 2 undefined\n on input line 82.\n\n\nPackage natbib Warning: Citation `howdollmspersuade2025' on page 2 undefined on\n input line 83.\n\n\nPackage natbib Warning: Citation `austin1962things' on page 2 undefined on inpu\nt line 87.\n\n\nPackage natbib Warning: Citation `searle1969speech' on page 2 undefined on inpu\nt line 87.\n\n\nPackage natbib Warning: Citation `he2021debertav3' on page 2 undefined on input\n line 102.\n\n[2]\n\nPackage natbib Warning: Citation `deepcontext2026' on page 3 undefined on input\n line 122.\n\n\nLaTeX Warning: Reference `tab:tfidf' on page 3 undefined on input line 138.\n\n\nLaTeX Warning: Reference `tab:deberta_clean' on page 3 undefined on input line \n156.\n\n[3]\n\nLaTeX Warning: Reference `tab:attack_gen' on page 4 undefined on input line 177\n.\n\n\nPackage natbib Warning: Citation `wildchat2024' on page 4 undefined on input li\nne 199.\n\n\nLaTeX Warning: Reference `tab:core' on page 4 undefined on input line 216.\n\n\nLaTeX Warning: Reference `tab:fpr' on page 4 undefined on input line 242.\n\n[4]\n\nLaTeX Warning: Reference `tab:scrambled' on page 5 undefined on input line 264.\n\n\n\nLaTeX Warning: Reference `tab:perturbation' on page 5 undefined on input line 2\n90.\n\n\nLaTeX Warning: Reference `tab:perturbation_k3' on page 5 undefined on input lin\ne 310.\n\n\nLaTeX Warning: Reference `tab:crossattack' on page 5 undefined on input line 33\n2.\n\n\nOverfull \\hbox (9.10887pt too wide) in paragraph at lines 335--337\n\\T1/cmr/m/n/10.95 This trans-fer is ex-pected: FITD's com-pli-ance es-ca-la-tio\nn shares sub-stan-tial over-lap with Crescendo's\n\nOverfull \\hbox (9.17894pt too wide) in paragraph at lines 335--337\n\\T1/cmr/m/n/10.95 per-sua-sion es-ca-la-tion in strat-egy space, with both pro-\ngress-ing through trust-building and authority-\n[5]\n\nLaTeX Warning: Reference `tab:strategy_dist' on page 6 undefined on input line \n358.\n\n\nLaTeX Warning: Reference `tab:trajectory' on page 6 undefined on input line 386\n.\n\n\nLaTeX Warning: Reference `tab:wildchat' on page 6 undefined on input line 413.\n\n[6]\n\nLaTeX Warning: Reference `tab:hierarchy' on page 7 undefined on input line 437.\n\n\n\nLaTeX Warning: Reference `tab:stability' on page 7 undefined on input line 465.\n\n\n[7]\nOverfull \\hbox (1.16982pt too wide) in paragraph at lines 508--512\n \\T1/cmr/bx/n/10.95 At-tack type cov-er-age.[] \\T1/cmr/m/n/10.95 DisPeD is de-s\nigned for persuasion-mediated multi-turn at-tacks. Cross-\n[8] [9]\n\nPackage natbib Warning: There were undefined citations.\n\n[10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmsy8.pfb>\nOutput written on paper.pdf (10 pages, 232252 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2] [3]\nOverfull \\hbox (2.91933pt too wide) in paragraph at lines 199--201\n \\T1/cmr/bx/n/10.95 Hard neg-a-tives.[] \\T1/cmr/m/n/10.95 We fil-tered 85 high-\nsemantic-drift be-nign con-ver-sa-tions from Wild-Chat [Wild-\n[4]\nOverfull \\hbox (9.10887pt too wide) in paragraph at lines 335--337\n\\T1/cmr/m/n/10.95 This trans-fer is ex-pected: FITD's com-pli-ance es-ca-la-tio\nn shares sub-stan-tial over-lap with Crescendo's\n\nOverfull \\hbox (9.17894pt too wide) in paragraph at lines 335--337\n\\T1/cmr/m/n/10.95 per-sua-sion es-ca-la-tion in strat-egy space, with both pro-\ngress-ing through trust-building and authority-\n[5] [6] [7]\nOverfull \\hbox (1.16982pt too wide) in paragraph at lines 508--512\n \\T1/cmr/bx/n/10.95 At-tack type cov-er-age.[] \\T1/cmr/m/n/10.95 DisPeD is de-s\nigned for persuasion-mediated multi-turn at-tacks. Cross-\n[8] [9] [10] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmsy8.pfb>\nOutput written on paper.pdf (10 pages, 232041 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b7d3ebba-7141-48b4-8e29-a5b5e721e58e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-17T17:19:54.428Z_

There's a label warning on the second pass. Let me run a third pass to resolve it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8af2b47e-115e-469e-bbed-5831da73b90f",
  "isSidechain": false,
  "requestId": "req_011Cb8XMn7x39UumERp6MchM",
  "type": "assistant",
  "uuid": "92d1a42e-bcf7-48d5-a645-779ef2168d07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdmVaEbkQGmvcctiWxXKbQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6256,
      "cache_read_input_tokens": 54389,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6256,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 54389,
          "cache_creation_input_tokens": 6256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6256
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

_source line 25 · 2026-05-17T17:19:57.035Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AdsJHeazq9stcWBG8vEdXd`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Third LaTeX pass to resolve label changes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92d1a42e-bcf7-48d5-a645-779ef2168d07",
  "isSidechain": false,
  "requestId": "req_011Cb8XMn7x39UumERp6MchM",
  "type": "assistant",
  "uuid": "5aa4da7c-34bd-4c46-af07-f7e30a24fe53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdmVaEbkQGmvcctiWxXKbQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6256,
      "cache_read_input_tokens": 54389,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6256,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 54389,
          "cache_creation_input_tokens": 6256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6256
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165817 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_…",
  "leafUuid": "5aa4da7c-34bd-4c46-af07-f7e30a24fe53",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream tracking",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c"
}
```

---

### Tool result

_source line 28 · 2026-05-17T17:19:57.456Z_

<details><summary>↩ Tool result · `toolu_01AdsJHeazq9stcWBG8vEdXd`</summary>

```text
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy8.pfb>
Output written on paper.pdf (10 pages, 232041 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5aa4da7c-34bd-4c46-af07-f7e30a24fe53",
  "isSidechain": false,
  "promptId": "9a6e3ecc-4cf9-4cf9-af9f-44f318d5866d",
  "type": "user",
  "uuid": "a965dc91-0316-4b9e-b1b6-6b9590b56721",
  "toolUseResult": {
    "stdout": "2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmsy8.pfb>\nOutput written on paper.pdf (10 pages, 232041 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5aa4da7c-34bd-4c46-af07-f7e30a24fe53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T17:20:03.333Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01A2AVMtC8QXKYaABGLyFtBw`</summary>

```json
{
  "command": "grep -c \"Warning\" /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/paper.log | head -1 && grep \"undefined\" /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/paper.log | head -5",
  "description": "Check for remaining warnings in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a965dc91-0316-4b9e-b1b6-6b9590b56721",
  "isSidechain": false,
  "requestId": "req_011Cb8XNGdwDv5HhdVWKmXrG",
  "type": "assistant",
  "uuid": "12f1df46-7001-42c3-b33a-e6924dcde0af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Pchumd8d9LiHYPDGhanQ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 857,
      "cache_read_input_tokens": 60645,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 857,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 60645,
          "cache_creation_input_tokens": 857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 857
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

_source line 30 · 2026-05-17T17:20:03.489Z_

<details><summary>↩ Tool result · `toolu_01A2AVMtC8QXKYaABGLyFtBw`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12f1df46-7001-42c3-b33a-e6924dcde0af",
  "isSidechain": false,
  "promptId": "9a6e3ecc-4cf9-4cf9-af9f-44f318d5866d",
  "type": "user",
  "uuid": "3293d8ff-d85b-476a-abca-01656f9b39d5",
  "toolUseResult": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "12f1df46-7001-42c3-b33a-e6924dcde0af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-17T17:20:03.497Z_

```json
{
  "parentUuid": "3293d8ff-d85b-476a-abca-01656f9b39d5",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "340ccc1b-83a1-46c0-9de1-03b75c2dcc21",
  "timestamp": "2026-05-17T17:20:03.497Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-17T17:20:11.223Z_

No warnings remain. The PDF compiled cleanly on the third pass.

Paper written and compiled: 10 pages, all 9 experiments from `experiment_data.json` covered across 15 tables. The three claims are framed per the narrative guidance: Claim 2 downgraded to K=3 significance with K=2 as trend (p=0.072), Claim 1 softened to "complementary robustness" with delta-delta=5pp, Claim 3 retained with individual-level variance caveat (sigma=0.18). Limitations section covers 7 paragraphs. Cross-attack results reported per attack type, not aggregate. Output at `median/paper.pdf`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "340ccc1b-83a1-46c0-9de1-03b75c2dcc21",
  "isSidechain": false,
  "requestId": "req_011Cb8XNiXgJg1tf8iMGftFQ",
  "type": "assistant",
  "uuid": "a7460000-f099-49fa-8881-a5fa6abf1ecc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ste7X771RVFMoL5iwd83N",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 317,
      "cache_read_input_tokens": 61502,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 61502,
          "cache_creation_input_tokens": 317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 317
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165817 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_…",
  "leafUuid": "a7460000-f099-49fa-8881-a5fa6abf1ecc",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream tracking",
  "sessionId": "caabacc5-b31b-4906-931d-2a6bd0a7de0c"
}
```

---
