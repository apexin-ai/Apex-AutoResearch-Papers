# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T075732 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/6681349e-5f13-4463-9075-814ffc4d8599.jsonl`
- **Structured JSON:** [`38f2f678e22229bf154f.json`](../../sessions/38/38f2f678e22229bf154f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T08:19:08.432Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T08:19:08.432Z",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T075732 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始三条 claim 全部不成立。Pilot 阶段观察到的 embedding benefit (+2.0pp Qwen, +1.6pp StarCoder) 在 full-scale 多种子实验中未复现——策略间差异被种子方差淹没，bootstrap p 值远离显著。 Dataflow benefit 在所有条件下消失。论文需完全 reframe 为 negative result paper： \"A Cautionary Tale: Scale, Seeds, and the Fragility of Hard Negative Mining for Code Retrieval\"。 核心贡献转为：(1) 证明 pilot-scale 结论在 HN mining for code 领域普遍不可靠， (2) representation saturation index 作为独立诊断工具， (3) CodeQL pipeline 作为开源 infrastructure。 在展开实验前必须先排查 data pipeline bug（full-scale 训练数据分布 vs pilot 是否存在 覆盖率/难度/repo 组成的系统性偏移），确认是真实 negative result 而非工程错误。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T08:19:08.436Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T08:19:08.436Z",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599"
}
```

---

## Round 1

37 recorded events

### User

_source line 3 · 2026-05-14T08:19:08.456Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T075732 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始三条 claim 全部不成立。Pilot 阶段观察到的 embedding benefit (+2.0pp Qwen, +1.6pp StarCoder) 在 full-scale 多种子实验中未复现——策略间差异被种子方差淹没，bootstrap p 值远离显著。 Dataflow benefit 在所有条件下消失。论文需完全 reframe 为 negative result paper： "A Cautionary Tale: Scale, Seeds, and the Fragility of Hard Negative Mining for Code Retrieval"。 核心贡献转为：(1) 证明 pilot-scale 结论在 HN mining for code 领域普遍不可靠， (2) representation saturation index 作为独立诊断工具， (3) CodeQL pipeline 作为开源 infrastructure。 在展开实验前必须先排查 data pipeline bug（full-scale 训练数据分布 vs pilot 是否存在 覆盖率/难度/repo 组成的系统性偏移），确认是真实 negative result 而非工程错误。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f67db5d7-4662-48a7-ba27-d130d41b7555",
  "type": "user",
  "uuid": "5baaad1f-7d5b-4bc5-a097-ecb5c3c2cdab",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T08:19:08.455Z_

```json
{
  "parentUuid": "5baaad1f-7d5b-4bc5-a097-ecb5c3c2cdab",
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
  "uuid": "b5411d39-6e10-49ee-ad03-595f6871f35f",
  "timestamp": "2026-05-14T08:19:08.455Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T08:19:08.455Z_

```json
{
  "parentUuid": "b5411d39-6e10-49ee-ad03-595f6871f35f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c83ebd43-887f-4319-a07e-79d2c4714b02",
  "timestamp": "2026-05-14T08:19:08.455Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
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
  "aiTitle": "Generate negative result paper on hard negative mining",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599"
}
```

---

### Assistant

_source line 7 · 2026-05-14T08:19:12.044Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c83ebd43-887f-4319-a07e-79d2c4714b02",
  "isSidechain": false,
  "requestId": "req_011Cb28ha4WobXrdeBTXfwqS",
  "type": "assistant",
  "uuid": "c5d5c0c4-7430-417e-97d4-d85407af94b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXcAf1H4nk4QeESnXQMTgq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11316,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11316,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11316
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

_source line 8 · 2026-05-14T08:19:12.637Z_

<details open><summary>🔧 Tool call — Read · `toolu_012q1EeQX6DLJXWBJMcJpuBA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5d5c0c4-7430-417e-97d4-d85407af94b0",
  "isSidechain": false,
  "requestId": "req_011Cb28ha4WobXrdeBTXfwqS",
  "type": "assistant",
  "uuid": "dfb8bfff-dc7f-4dc3-b974-42fb0d52dc95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXcAf1H4nk4QeESnXQMTgq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11316,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11316,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11316
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

_source line 9 · 2026-05-14T08:19:12.980Z_

<details open><summary>🔧 Tool call — Read · `toolu_017y4vVS4NnTPYRWnHfS4vp8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfb8bfff-dc7f-4dc3-b974-42fb0d52dc95",
  "isSidechain": false,
  "requestId": "req_011Cb28ha4WobXrdeBTXfwqS",
  "type": "assistant",
  "uuid": "12405788-5a91-4b9f-8d9b-2ecf1e6819d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXcAf1H4nk4QeESnXQMTgq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11316,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11316,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11316
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

_source line 10 · 2026-05-14T08:19:13.033Z_

<details><summary>↩ Tool result · `toolu_012q1EeQX6DLJXWBJMcJpuBA`</summary>

```text
1	[
2	  {
3	    "name": "M2 Full Qwen — 9 seeds × 3 strategies 最终结果",
4	    "description": "Qwen2.5-Coder-3B 在 full-scale 数据上完成全部 27 runs (9 seeds × 3 strategies)。 当前仅 random_s42 完成（R@1=0.553 at step 1000），预测全部完成后的汇总。\n",
5	    "results": {
6	      "random_mean_R1": 0.523,
7	      "random_std_R1": 0.031,
8	      "embedding_distance_mean_R1": 0.521,
9	      "embedding_distance_std_R1": 0.035,
10	      "dataflow_aware_mean_R1": 0.515,
11	      "dataflow_aware_std_R1": 0.038,
12	      "embed_vs_random_delta_pp": -0.2,
13	      "dataflow_vs_random_delta_pp": -0.8,
14	      "best_single_run_R1": 0.553,
15	      "worst_single_run_R1": 0.478,
16	      "cross_seed_R1_std_pp": 3.1,
17	      "best_strategy_by_seed_count": {
18	        "random_wins": 4,
19	        "embedding_wins": 3,
20	        "dataflow_wins": 2
21	      },
22	      "overfitting_step_median": 1000
23	    },
24	    "tables": [
25	      {
26	        "name": "Table 2: Qwen Full-Scale R@1 by Strategy × Seed",
27	        "columns": [
28	          "seed",
29	          "random",
30	          "embedding",
31	          "dataflow"
32	        ],
33	        "rows": [
34	          [
35	            42,
36	            0.553,
37	            0.547,
38	            0.538
39	          ],
40	          [
41	            123,
42	            0.528,
43	            0.534,
44	            0.521
45	          ],
46	          [
47	            456,
48	            0.512,
49	            0.498,
50	            0.503
51	          ],
52	          [
53	            789,
54	            0.541,
55	            0.543,
56	            0.53
57	          ],
58	          [
59	            1024,
60	            0.498,
61	            0.51,
62	            0.496
63	          ],
64	          [
65	            2048,
66	            0.519,
67	            0.522,
68	            0.512
69	          ],
70	          [
71	            3000,
72	            0.505,
73	            0.503,
74	            0.478
75	          ],
76	          [
77	            4096,
78	            0.53,
79	            0.517,
80	            0.525
81	          ],
82	          [
83	            5000,
84	            0.523,
85	            0.515,
86	            0.532
87	          ]
88	        ],
89	        "footer": "Mean±std: random 0.523±0.031, embed 0.521±0.035, dataflow 0.515±0.038"
90	      }
91	    ],
92	    "figures": [],
93	    "analysis": "策略间 delta (<1pp) 远小于种子间方差 (std~3pp)。Pilot 单种子结果是方差范围内的 正常波动。这是 worst 档的核心发现：embedding benefit 是 pilot-scale 的统计幻觉。\n\n\nPilot 的 +2.0pp embed benefit 来自单种子（s42）在小规模数据上的幸运波动。 Full-scale 数据量从 ~2K 增至 ~15K instances，数据分布发生系统性变化： (1) large/xlarge repos 占比从 pilot 的 ~30% 升至 ~60%，这些 repos 的 structural_data_rate 仅 0.31-0.34，embedding negatives 的质量下降； (2) 训练集难度分布更均匀，pilot 中 embedding mining 选出的\"难\"样本在 full-scale 中不再难于 random——因为 random pool 本身已足够难； (3) Qwen 的 pos_sim=0.9855 表征饱和在 full-scale 下更严重，所有策略都面临 margin 过小的问题（embedding margin=0.017, 但 random margin 也仅 0.074）， 导致策略间差异被优化噪声覆盖。9 个种子的 std~3pp 远大于策略间 delta~0.2pp。\n"
94	  },
95	  {
96	    "name": "M2 Full StarCoder — 9 seeds × 3 strategies 最终结果",
97	    "description": "StarCoder2-3B full-scale 27 runs。当前 random_s42 R@1=0.454 at step 1000。\n",
98	    "results": {
99	      "random_mean_R1": 0.443,
100	      "random_std_R1": 0.028,
101	      "embedding_distance_mean_R1": 0.435,
102	      "embedding_distance_std_R1": 0.033,
103	      "dataflow_aware_mean_R1": 0.428,
104	      "dataflow_aware_std_R1": 0.04,
105	      "embed_vs_random_delta_pp": -0.8,
106	      "dataflow_vs_random_delta_pp": -1.5,
107	      "cross_seed_R1_std_pp": 3.4
108	    },
109	    "tables": [
110	      {
111	        "name": "Table 3: StarCoder Full-Scale R@1 by Strategy × Seed",
112	        "columns": [
113	          "seed",
114	          "random",
115	          "embedding",
116	          "dataflow"
117	        ],
118	        "rows": [
119	          [
120	            42,
121	            0.454,
122	            0.448,
123	            0.442
124	          ],
125	          [
126	            123,
127	            0.44,
128	            0.425,
129	            0.418
130	          ],
131	          [
132	            456,
133	            0.462,
134	            0.456,
135	            0.44
136	          ],
137	          [
138	            789,
139	            0.435,
140	            0.43,
141	            0.412
142	          ],
143	          [
144	            1024,
145	            0.448,
146	            0.442,
147	            0.435
148	          ],
149	          [
150	            2048,
151	            0.425,
152	            0.418,
153	            0.398
154	          ],
155	          [
156	            3000,
157	            0.458,
158	            0.45,
159	            0.448
160	          ],
161	          [
162	            4096,
163	            0.43,
164	            0.422,
165	            0.425
166	          ],
167	          [
168	            5000,
169	            0.438,
170	            0.428,
171	            0.43
172	          ]
173	        ],
174	        "footer": "Mean±std: random 0.443±0.028, embed 0.435±0.033, dataflow 0.428±0.040"
175	      }
176	    ],
177	    "figures": [],
178	    "analysis": "StarCoder 上 dataflow 甚至表现最差（-1.5pp vs random），方向与 pilot 一致但 幅度更大。Embedding 也未能帮助。结论：两编码器在 full-scale 下均不支持任何 非 random 策略的优势。\n\n\nStarCoder pilot 已经是 negative conclusion（dataflow R@1=0.487 < random 0.492）。 Full-scale 放大了这个趋势：(1) StarCoder 表征空间 \"healthy\"（pos_sim=0.80）， random negatives 已提供足够梯度（margin=0.194），embedding/dataflow 引入的更难 negatives 反而导致训练不稳定——loss landscape 更尖锐，不同种子落入不同局部最优； (2) dataflow negatives 在 StarCoder 上 margin=0.119 vs embedding 0.067， dataflow 实际上更\"容易\"，但 full-scale 下这个 margin 差异未能转化为性能优势， 因为 StarCoder 的问题不是 negative difficulty 而是编码器容量限制（3B 参数 + LoRA rank 受限时，更难 negatives 导致梯度冲突）。Cross-seed std 3.4pp 进一步 确认策略差异 (<1.5pp) 不可靠。\n"
179	  },
180	  {
181	    "name": "M3a SWE-bench Lite End-to-End Evaluation",
182	    "description": "SWE-bench Lite (300 instances) end-to-end evaluation，使用 Qwen3.6-27B agent， 对比 3 个 strategy 的 best checkpoint 作为 retriever。\n",
183	    "results": {
184	      "random_resolve_rate": 0.187,
185	      "embedding_resolve_rate": 0.19,
186	      "dataflow_resolve_rate": 0.183,
187	      "embed_vs_random_delta_pp": 0.3,
188	      "dataflow_vs_random_delta_pp": -0.4,
189	      "swebench_resolve_delta_pp": 0.3,
190	      "retrieval_R1_on_swebench": {
191	        "random": 0.42,
192	        "embedding": 0.43,
193	        "dataflow": 0.41
194	      },
195	      "n_instances_evaluated": 287,
196	      "n_instances_failed": 13
197	    },
198	    "tables": [
199	      {
200	        "name": "Table 5: SWE-bench Lite Resolve Rates",
201	        "columns": [
202	          "strategy",
203	          "resolve_rate",
204	          "retrieval_R1",
205	          "n_resolved",
206	          "n_total"
207	        ],
208	        "rows": [
209	          [
210	            "random",
211	            0.187,
212	            0.42,
213	            54,
214	            287
215	          ],
216	          [
217	            "embedding_distance",
218	            0.19,
219	            0.43,
220	            55,
221	            287
222	          ],
223	          [
224	            "dataflow_aware",
225	            0.183,
226	            0.41,
227	            53,
228	            287
229	          ]
230	        ],
231	        "footer": "Best delta: +0.3pp (embed vs random), not significant (p=0.89 McNemar)"
232	      }
233	    ],
234	    "figures": [],
235	    "analysis": "SWE-bench 结果不仅不支持 embedding/dataflow 策略的优势，甚至所有策略的 resolve rate 都低于 SweRank baseline。这暗示 full-scale 训练可能引入了某种 regression（数据分布 偏移？）。需排查训练数据与 SWE-bench 的 domain overlap。\n\n\nSWE-bench Lite 的 resolve rate 由 retrieval → agent pipeline 多阶段组成， retriever 差异被下游 agent 的 stochasticity 大幅稀释。即使 retrieval R@1 差异 存在 1pp，经过 agent 的 code generation + apply patch + test 环节后，resolve rate 差异被压缩到 <0.5pp。具体原因： (1) SWE-bench 中很多 \"easy\" instances（~30%）任何 retriever 都能找到正确文件， 策略差异为零； (2) \"hard\" instances（~25%）任何 retriever 都找不到，agent 依赖推理能力而非检索； (3) 只有 ~45% 的中间难度 instances 中 retrieval 策略可能产生差异，但 agent 的 code generation variance（温度、context window 限制）进一步模糊了信号； (4) 300 instances 中有效差异空间 ~135 个，0.3pp delta 对应仅 ~1 个额外解决的 instance，完全在噪声范围内。此外 full-scale retriever 本身策略间差异已消失， SWE-bench 只是进一步确认。\n"
236	  },
237	  {
238	    "name": "M3b RepoBench-R Cross-File Retrieval",
239	    "description": "RepoBench-R 作为第二基准，retrieval-only 评估，无 LLM agent。\n",
240	    "results": {
241	      "random_R1": 0.312,
242	      "embedding_R1": 0.308,
243	      "dataflow_R1": 0.295,
244	      "embed_vs_random_delta_pp": -0.4,
245	      "dataflow_vs_random_delta_pp": -1.7,
246	      "random_R5": 0.58,
247	      "embedding_R5": 0.57,
248	      "dataflow_R5": 0.56,
249	      "pretrained_baseline_R1": 0.285
250	    },
251	    "tables": [
252	      {
253	        "name": "Table 6: RepoBench-R Results (Qwen encoder)",
254	        "columns": [
255	          "strategy",
256	          "R@1",
257	          "R@5",
258	          "R@10",
259	          "MRR"
260	        ],
261	        "rows": [
262	          [
263	            "pretrained",
264	            0.285,
265	            0.52,
266	            0.68,
267	            0.401
268	          ],
269	          [
270	            "random",
271	            0.312,
272	            0.58,
273	            0.73,
274	            0.438
275	          ],
276	          [
277	            "embedding_distance",
278	            0.308,
279	            0.57,
280	            0.72,
281	            0.432
282	          ],
283	          [
284	            "dataflow_aware",
285	            0.295,
286	            0.56,
287	            0.71,
288	            0.418
289	          ]
290	        ]
291	      }
292	    ],
293	    "figures": [],
294	    "analysis": "RepoBench-R 进一步证明策略差异不稳定且 domain-dependent。Dataflow 策略的负迁移 尤其严重（-1.7pp），支持 negative result 叙事中 \"structural negatives 不 generalize\" 的论点。\n\n\nRepoBench-R 是 cross-file completion 任务，与 SWE-smith 的 bug localization 分布差异更大。Full-scale 训练在 SWE-smith 上 overfit 的模型在 RepoBench 上 表现出不同的行为模式： (1) 所有策略都优于 pretrained baseline（+2-3pp），说明 contrastive fine-tuning 本身有效，但策略间差异在 domain shift 下被进一步压缩； (2) Dataflow negatives 在 RepoBench 上表现最差，因为 SWE-smith 的 dataflow 结构 （bug-fix oriented）与 RepoBench 的 completion-oriented 代码结构不匹配—— SWE-smith 中 disconnected = irrelevant 的假设在 completion 场景中不成立； (3) Embedding negatives 略低于 random 是因为 full-scale embedding mining 选出的 negatives 过度 fit 到 SWE-smith 的相似性分布，domain shift 后反而损害泛化。\n"
295	  },
296	  {
297	    "name": "Embedding vs Random Deep Stratified Analysis",
298	    "description": "按 repo size、code complexity、neg_difficulty 分层分析 embedding negatives 的效果。\n",
299	    "results": {
300	      "by_repo_size": {
301	        "small_lt50": {
302	          "random_R1": 0.61,
303	          "embedding_R1": 0.59,
304	          "delta_pp": -2.0
305	        },
306	        "medium_50_200": {
307	          "random_R1": 0.54,
308	          "embedding_R1": 0.55,
309	          "delta_pp": 1.0
310	        },
311	        "large_200_500": {
312	          "random_R1": 0.51,
313	          "embedding_R1": 0.5,
314	          "delta_pp": -1.0
315	        },
316	        "xlarge_500plus": {
317	          "random_R1": 0.48,
318	          "embedding_R1": 0.48,
319	          "delta_pp": 0.0
320	        }
321	      },
322	      "by_neg_difficulty_quartile": {
323	        "easy_q1_delta_pp": 0.5,
324	        "medium_q2_delta_pp": -0.3,
325	        "hard_q3_delta_pp": -1.2,
326	        "hardest_q4_delta_pp": -2.1
327	      },
328	      "correlation_margin_vs_benefit": -0.15,
329	      "correlation_repo_size_vs_benefit": -0.08
330	    },
331	    "tables": [
332	      {
333	        "name": "Table 7: Embedding Benefit by Repo Size",
334	        "columns": [
335	          "repo_tier",
336	          "n_instances",
337	          "random_R1",
338	          "embed_R1",
339	          "delta_pp"
340	        ],
341	        "rows": [
342	          [
343	            "small (<50)",
344	            500,
345	            0.61,
346	            0.59,
347	            -2.0
348	          ],
349	          [
350	            "medium (50-200)",
351	            4096,
352	            0.54,
353	            0.55,
354	            1.0
355	          ],
356	          [
357	            "large (200-500)",
358	            13628,
359	            0.51,
360	            0.5,
361	            -1.0
362	          ],
363	          [
364	            "xlarge (500+)",
365	            25949,
366	            0.48,
367	            0.48,
368	            0.0
369	          ]
370	        ]
371	      }
372	    ],
373	    "figures": [],
374	    "analysis": "核心发现：embedding benefit 是 repo size 和 negative difficulty 的函数， 在 pilot 的 data composition 下恰好为正，在 full-scale 的 data composition 下 恰好为零或负。这不是方法失败，而是 pilot evaluation bias——小规模评估 over-represents 中等 repo，恰好是 embedding mining 的 sweet spot。\n\n\n分层分析揭示 embedding benefit 不是\"消失\"而是\"抵消\"——在某些 strata 正向、 其他 strata 负向，总和接近零： (1) Small repos 上 embedding mining 实际有害（-2pp），因为小 repo 的 file pool 只有 ~10-50 个文件，embedding mining 选出的 \"nearest\" negative 往往就是 gold file 的近邻（同一个 module），形成 false hard negatives 损害训练信号； (2) Medium repos 上 embedding 略有优势（+1pp），因为 pool 足够大使 mining 选到 真正的 hard negatives，且难度梯度合理； (3) Large/xlarge repos 上差异消失，因为 random sampling 在大 pool 中已经有合理 概率采到 moderately hard negatives，embedding mining 的额外选择性优势被稀释； (4) 按 neg_difficulty 分层更清晰：最难 quartile（margin 最小）中 embedding 有害 （-2.1pp），因为过难的 negatives 导致梯度冲突/训练不稳定。这解释了为什么 full-scale（更多 large repos → 更多 hard quartile instances）中 benefit 消失。\n"
375	  },
376	  {
377	    "name": "Hop-Distance Call-Graph Bounding Ablation",
378	    "description": "1-hop vs 2-hop vs 3-hop call-graph bounding 对 dataflow negative 质量的影响。\n",
379	    "results": {
380	      "hop_1": {
381	        "connected_pct": 0.12,
382	        "disconnected_neg_margin": 0.035,
383	        "training_R1": 0.513
384	      },
385	      "hop_2": {
386	        "connected_pct": 0.34,
387	        "disconnected_neg_margin": 0.029,
388	        "training_R1": 0.515
389	      },
390	      "hop_3": {
391	        "connected_pct": 0.58,
392	        "disconnected_neg_margin": 0.022,
393	        "training_R1": 0.51
394	      },
395	      "delta_1hop_vs_2hop_pp": -0.2,
396	      "delta_2hop_vs_3hop_pp": 0.5,
397	      "all_vs_random_best_pp": -0.8
398	    },
399	    "tables": [
400	      {
401	        "name": "Table 8: Hop-Distance Ablation (Qwen, seed 42)",
402	        "columns": [
403	          "hops",
404	          "connected_pct",
405	          "disconn_margin",
406	          "R@1",
407	          "vs_random_pp"
408	        ],
409	        "rows": [
410	          [
411	            1,
412	            0.12,
413	            0.035,
414	            0.513,
415	            -1.0
416	          ],
417	          [
418	            2,
419	            0.34,
420	            0.029,
421	            0.515,
422	            -0.8
423	          ],
424	          [
425	            3,
426	            0.58,
427	            0.022,
428	            0.51,
429	            -1.3
430	          ],
431	          [
432	            "random",
433	            "-",
434	            "-",
435	            0.523,
436	            0.0
437	          ]
438	        ]
439	      }
440	    ],
441	    "figures": [],
442	    "analysis": "Hop distance 是 second-order 参数——当 first-order 效应（结构断开作为 hardness proxy） 本身无效时，调节粒度无法改变结论。\n\n\nHop distance 改变 connected/disconnected 的划分粒度，但在 worst 档下无法拯救 dataflow 策略： (1) 1-hop 过于严格（仅 12% connected），大量 gold-relevant files 被错误标记为 disconnected，产生大量 false hard negatives → 训练信号受损； (2) 2-hop（当前设置）是 pilot 中的最优，但 full-scale 下效果与 random 无异； (3) 3-hop 过于宽泛（58% connected），disconnected pool 缩小到几乎只剩 truly unrelated files，这些 negatives 太容易（margin=0.022），训练信号退化为 接近 random sampling 的效果但 pool 更小； (4) 三种 hop 设置的 R@1 范围仅 0.510-0.515，都低于 random baseline 0.523， 说明 structural bounding 本身在 full-scale 下不是一个有效的 negative selection 维度——问题出在 \"结构断开≠语义无关\" 这个核心假设。\n"
443	  },
444	  {
445	    "name": "Training Data Size Scaling Ablation",
446	    "description": "1K vs 3K vs 5K（当前 full-scale ~15K instances 中子采样）对策略差异的影响。\n",
447	    "results": {
448	      "size_1k": {
449	        "random_R1": 0.505,
450	        "embedding_R1": 0.518,
451	        "dataflow_R1": 0.512,
452	        "embed_delta_pp": 1.3
453	      },
454	      "size_3k": {
455	        "random_R1": 0.515,
456	        "embedding_R1": 0.52,
457	        "dataflow_R1": 0.513,
458	        "embed_delta_pp": 0.5
459	      },
460	      "size_5k": {
461	        "random_R1": 0.52,
462	        "embedding_R1": 0.521,
463	        "dataflow_R1": 0.516,
464	        "embed_delta_pp": 0.1
465	      },
466	      "size_15k_full": {
467	        "random_R1": 0.523,
468	        "embedding_R1": 0.521,
469	        "dataflow_R1": 0.515,
470	        "embed_delta_pp": -0.2
471	      },
472	      "embed_benefit_slope_per_1k": -0.11
473	    },
474	    "tables": [
475	      {
476	        "name": "Table 9: Data Size × Strategy Interaction",
477	        "columns": [
478	          "data_size",
479	          "random_R1",
480	          "embed_R1",
481	          "dataflow_R1",
482	          "embed_delta"
483	        ],
484	        "rows": [
485	          [
486	            "1K",
487	            0.505,
488	            0.518,
489	            0.512,
490	            1.3
491	          ],
492	          [
493	            "3K",
494	            0.515,
495	            0.52,
496	            0.513,
497	            0.5
498	          ],
499	          [
500	            "5K",
501	            0.52,
502	            0.521,
503	            0.516,
504	            0.1
505	          ],
506	          [
507	            "15K (full)",
508	            0.523,
509	            0.521,
510	            0.515,
511	            -0.2
512	          ]
513	        ]
514	      }
515	    ],
516	    "figures": [],
517	    "analysis": "这张图是论文的核心 figure——直观展示 \"hard negative mining 的收益随数据规模递减 并最终消失\" 的 scaling law。对 negative result paper 的贡献极大，因为它提供了 可预测的量化关系，而非仅仅 \"结果没复现\" 的定性陈述。\n\n\n这个 ablation 精确解释了 pilot-to-full-scale discrepancy 的机制： (1) 1K instances（≈pilot 规模）复现了 pilot 的 embedding benefit（+1.3pp）， 确认 pilot 结果本身没有 bug——在小规模下 embedding mining 确实有效； (2) 随数据量增长，benefit 单调递减（斜率≈-0.11pp per 1K instances）； (3) 原因是 data scaling 改变了有效 negative difficulty 分布——1K 时 random pool 中真正 hard 的 negatives 极少（小 pool → 大多是 easy negatives），embedding mining 通过选择 nearest neighbors 提供了必要的 difficulty gradient。但随着 pool 增大， random sampling 的\"命中率\"自然上升，embedding mining 的增量价值趋零； (4) 5K 处 delta 已缩至 0.1pp（不显著），15K 处反转为 -0.2pp； (5) 这是 negative result paper 的关键证据：small-scale evaluation 系统性高估 hard negative mining 的收益，因为 scale 本身就是一种隐性的 negative difficulty 调节器。\n"
518	  },
519	  {
520	    "name": "Fusion Head Architecture Ablation",
521	    "description": "Embedding-only vs structural-features-only vs combined fusion head， 测试结构特征是否通过不同 fusion 方式提供价值。\n",
522	    "results": {
523	      "embedding_only_R1": 0.523,
524	      "structural_only_R1": 0.385,
525	      "combined_R1": 0.519,
526	      "embed_only_vs_combined_pp": 0.4
527	    },
528	    "tables": [
529	      {
530	        "name": "Table 10: Fusion Head Ablation (Qwen, seed 42)",
531	        "columns": [
532	          "head_type",
533	          "R@1",
534	          "R@5",
535	          "val_loss"
536	        ],
537	        "rows": [
538	          [
539	            "embedding_only",
540	            0.523,
541	            0.955,
542	            0.486
543	          ],
544	          [
545	            "structural_features",
546	            0.385,
547	            0.78,
548	            0.812
549	          ],
550	          [
551	            "combined",
552	            0.519,
553	            0.95,
554	            0.495
555	          ]
556	        ]
557	      }
558	    ],
559	    "figures": [],
560	    "analysis": "结构特征作为独立信号维度不足，作为辅助信号有害。这排除了 \"也许 dataflow 信号有用 但 negative mining 不是正确的注入方式\" 的替代假设。\n\n\nFusion head 架构无法从无到有创造 structural signal 的价值： (1) Embedding-only head 与 random strategy 性能相当（0.523），因为 LoRA fine-tuned embeddings 本身已捕获了足够的 code similarity 信息； (2) Structural-features-only head 大幅下降至 0.385——结构特征（is_connected, dataflow_distance, call_graph_hops）单独不足以判断 relevance，因为大部分 file pairs 的结构特征是 sparse 的（structural_data_rate=0.34，66% pairs 无结构信息）； (3) Combined head 反而略低于 embedding-only（-0.4pp），因为 noisy structural features 干扰了 embedding signal——当 66% instances 的结构特征为 null/zero 时， fusion layer 必须学会忽略结构维度，但 LoRA 的低秩约束使这个 \"ignore\" 信号 不够干净； (4) 这进一步支持了 structural signal 在 full-scale 下无效的结论。\n"
561	  },
562	  {
563	    "name": "Dataflow-Distance Weighted vs Binary Negatives",
564	    "description": "连续 dataflow distance 加权 vs 二元 connected/disconnected 的 negative selection。\n",
565	    "results": {
566	      "binary_disconnected_R1": 0.515,
567	      "distance_weighted_R1": 0.517,
568	      "delta_pp": 0.2,
569	      "vs_random_pp": -0.6
570	    },
571	    "tables": [],
572	    "figures": [],
573	    "analysis": "细化无效信号的粒度不改善性能。这是对 \"也许我们只需要更好的结构度量\" 假设的反驳。\n\n\nDistance weighting 是对 binary disconnected 的细化——用 shortest dataflow path length 作为权重偏好更远的（更 disconnected）negatives。但在 worst 档下改进微乎其微 （+0.2pp vs binary），因为： (1) 核心问题不是 negative selection 的粒度，而是 structural disconnection 作为 hardness proxy 本身的有效性——weighted 版本在一个无效信号上做更精细的选择， 不改变根本问题； (2) 距离信息 noisy——CodeQL 的 dataflow path 是 approximation，real shortest path 与 estimated path 的相关性仅 ~0.6（由于 scope bounding），weighting 基于 noisy distance 引入额外噪声； (3) 两个版本都低于 random baseline（-0.6pp），进一步确认结构信号无效。\n"
574	  },
575	  {
576	    "name": "Failure Analysis: 50 SweRank/BM25 Failures",
577	    "description": "对 50 个 SweRank/BM25 检索失败的 SWE-bench instances 进行手动分类， 分析 dataflow 信号是否能帮助。\n",
578	    "results": {
579	      "n_analyzed": 50,
580	      "categories": {
581	        "cross_file_dependency": 18,
582	        "naming_ambiguity": 12,
583	        "scattered_changes": 9,
584	        "test_file_confusion": 7,
585	        "other": 4
586	      },
587	      "dataflow_could_help": 6,
588	      "dataflow_actually_helped": 2,
589	      "dataflow_hurt": 3,
590	      "dataflow_neutral": 39
591	    },
592	    "tables": [
593	      {
594	        "name": "Table 11: Failure Category Analysis",
595	        "columns": [
596	          "category",
597	          "count",
598	          "df_could_help",
599	          "df_actually_helped",
600	          "df_hurt"
601	        ],
602	        "rows": [
603	          [
604	            "cross_file_dep",
605	            18,
606	            4,
607	            1,
608	            1
609	          ],
610	          [
611	            "naming_ambiguity",
612	            12,
613	            0,
614	            0,
615	            1
616	          ],
617	          [
618	            "scattered_changes",
619	            9,
620	            2,
621	            1,
622	            1
623	          ],
624	          [
625	            "test_confusion",
626	            7,
627	            0,
628	            0,
629	            0
630	          ],
631	          [
632	            "other",
633	            4,
634	            0,
635	            0,
636	            0
637	          ],
638	          [
639	            "total",
640	            50,
641	            6,
642	            2,
643	            3
644	          ]
645	        ]
646	      }
647	    ],
648	    "figures": [],
649	    "analysis": "Dataflow 的理论覆盖面（12% = 6/50 可能帮助）和实际有效率（4% = 2/50 实际帮助） 远低于立论所需。对 negative result paper 的贡献：提供 error taxonomy 证明 structural signal 的适用范围窄于预期。\n\n\n手动分析 50 个失败案例后发现 dataflow 信号能帮助的场景远少于预期： (1) Cross-file dependency（18 cases）是 dataflow 理论上的 sweet spot，但实际 仅 4/18 有可用的 CodeQL dataflow 路径——其余 14 个的 dependency 是通过 import、 type reference 或 configuration 而非 data flow，CodeQL 的 inter-procedural analysis 未覆盖这些； (2) Naming ambiguity（12 cases）中 dataflow 无法帮助——问题是同名函数/类在 不同 module 中，structural 和 textual signal 同时失效； (3) 6 个理论上 dataflow 可帮助的 cases 中，仅 2 个实际在 dataflow-trained model 中被正确检索——另 4 个因训练不稳定/过拟合而性能退化抵消了理论优势； (4) 3 个 cases 中 dataflow 实际有害——将结构上相关但 gold set 外的文件排入 top-1，挤掉了正确答案。\n"
650	  },
651	  {
652	    "name": "Qualitative Examples: Structural Negatives Impact",
653	    "description": "挑选 5-10 个 structural negatives 改变检索结果的定性案例。\n",
654	    "results": {
655	      "positive_examples_found": 3,
656	      "negative_examples_found": 4,
657	      "neutral_examples": 3,
658	      "net_narrative": "negative"
659	    },
660	    "tables": [],
661	    "figures": [],
662	    "analysis": "定性证据反而支持 negative result 叙事。典型 failure mode（structural proximity ≠ task relevance）是重要的methodological insight。\n\n\n在 worst 档下，能找到的正面案例数量与负面案例相当甚至更少： (1) 3 个正面案例：dataflow training 将结构相关文件从 top-5 提升到 top-1， 但这些改善也出现在 embedding strategy 的部分种子中，不能归因于 dataflow； (2) 4 个负面案例：dataflow training 将结构上相近但 gold set 外的文件推高排名， 挤掉了正确答案。典型模式：文件 A 通过 data flow 连接到 gold file B， dataflow 策略错误地将 A 排在 B 之前； (3) 3 个中性案例：dataflow 改变了 top-10 内的排序但不影响 top-1/top-5； (4) 定性分析 net negative，无法支撑 paper 中的正面叙事。对 negative result paper 可用——展示 structural negatives 的 failure modes。\n"
663	  },
664	  {
665	    "name": "Temperature Ablation: τ ∈ {0.05, 0.1, 0.2}",
666	    "description": "三个温度 × 三个策略，测试 embedding benefit 是否是温度 regime-specific。\n",
667	    "results": {
668	      "tau_005": {
669	        "random_R1": 0.498,
670	        "embedding_R1": 0.485,
671	        "dataflow_R1": 0.475,
672	        "embed_delta_pp": -1.3
673	      },
674	      "tau_010": {
675	        "random_R1": 0.523,
676	        "embedding_R1": 0.521,
677	        "dataflow_R1": 0.515,
678	        "embed_delta_pp": -0.2
679	      },
680	      "tau_020": {
681	        "random_R1": 0.51,
682	        "embedding_R1": 0.508,
683	        "dataflow_R1": 0.502,
684	        "embed_delta_pp": -0.2
685	      },
686	      "best_overall_tau": 0.1,
687	      "any_tau_with_significant_embed_benefit": false
688	    },
689	    "tables": [
690	      {
691	        "name": "Table 12: Temperature × Strategy Interaction (Qwen, mean of 3 seeds)",
692	        "columns": [
693	          "tau",
694	          "random",
695	          "embedding",
696	          "dataflow",
697	          "best_strategy"
698	        ],
699	        "rows": [
700	          [
701	            0.05,
702	            0.498,
703	            0.485,
704	            0.475,
705	            "random"
706	          ],
707	          [
708	            0.1,
709	            0.523,
710	            0.521,
711	            0.515,
712	            "random"
713	          ],
714	          [
715	            0.2,
716	            0.51,
717	            0.508,
718	            0.502,
719	            "random"
720	          ]
721	        ]
722	      }
723	    ],
724	    "figures": [],
725	    "analysis": "Temperature 不是 confound——在所有温度 regime 下，random 策略都是最优或并列最优。 排除了 \"pilot 的 embedding benefit 是因为 τ=0.1 恰好适合 embedding mining\" 的假设。\n\n\n温度调节改变 contrastive loss 对 similarity margin 的敏感度，但无法拯救无效的 mining strategy： (1) τ=0.05 使 loss 对 margin 极其敏感——在 Qwen 的 saturated space （pos_sim=0.9855, embedding neg_sim=0.9685, margin=0.017）中，如此小的 margin 在 τ=0.05 下产生几乎相同的 loss 贡献，embedding negatives 等于 random。 但更严重的是 τ=0.05 放大了个别 extreme negative 的梯度，导致训练不稳定， 所有策略性能下降（尤其 dataflow，因为 dataflow negatives 的 margin distribution 更 heavy-tailed）； (2) τ=0.10（当前默认）是最优温度，但策略间无显著差异； (3) τ=0.20 使 loss 对 margin 不够敏感——hard negatives 的额外 difficulty 被 soft temperature 压缩，embedding/dataflow mining 的理论优势被进一步稀释； (4) 没有任何温度 regime 能让 embedding benefit 达到统计显著，因为 full-scale 下策略间的 \"信号\" 本身不存在（是 pilot 的噪声），温度只是调节 loss landscape 的曲率，不能创造信号。\n"
726	  },
727	  {
728	    "name": "Dynamic Embedding Mining vs Static",
729	    "description": "Per-epoch 重新 mining embedding negatives vs 一次性从 pretrained model mining。\n",
730	    "results": {
731	      "static_embedding_R1": 0.521,
732	      "dynamic_epoch1_R1": 0.521,
733	      "dynamic_epoch2_R1": 0.519,
734	      "dynamic_epoch3_R1": 0.515,
735	      "dynamic_mean_R1": 0.518,
736	      "dynamic_vs_static_pp": -0.3,
737	      "dynamic_vs_random_pp": -0.5
738	    },
739	    "tables": [
740	      {
741	        "name": "Table 13: Static vs Dynamic Mining (Qwen, seed 42)",
742	        "columns": [
743	          "method",
744	          "epoch1_R1",
745	          "epoch2_R1",
746	          "epoch3_R1",
747	          "best_R1"
748	        ],
749	        "rows": [
750	          [
751	            "static",
752	            0.54,
753	            0.53,
754	            0.512,
755	            0.54
756	          ],
757	          [
758	            "dynamic",
759	            0.54,
760	            0.525,
761	            0.505,
762	            0.54
763	          ],
764	          [
765	            "random",
766	            0.535,
767	            0.528,
768	            0.51,
769	            0.535
770	          ]
771	        ]
772	      }
773	    ],
774	    "figures": [],
775	    "analysis": "Dynamic mining 排除了 \"staleness\" 作为 embedding mining 失效的解释。 Mining 策略本身在大规模下不提供增量价值。\n\n\nDynamic mining 理论上解决 \"pretrained embedding 与 fine-tuned embedding 偏移导致 negatives 过时\" 的问题。但在 worst 档下非但不改善，反而略有下降： (1) Epoch 1 dynamic ≈ static（因为 epoch 1 开始时 model 就是 pretrained， mining 结果相同）； (2) Epoch 2-3 的 re-mining 产生了 curriculum shift 效应——随着 model 改善， nearest neighbors 改变，新选出的 negatives 更难但也更 noisy（因为 fine-tuned model 的 embedding space 在 LoRA 下只部分更新，re-mining 的 nearest neighbors 可能是 LoRA 的 artifacts 而非真正的 hard negatives）； (3) Re-mining 引入的计算开销显著（每 epoch 需重新编码全部 ~44K instances， ~2h per re-mining），cost-benefit 明显不值得； (4) Dynamic mining 的失败进一步证明问题不是 \"mining 过时\" 而是 \"mining 本身 在大规模下无效\"。\n"
776	  },
777	  {
778	    "name": "Bootstrap CI for SWE-bench Resolve Rates",
779	    "description": "10,000 bootstrap resamples 计算 SWE-bench resolve rate 的 95% CI。\n",
780	    "results": {
781	      "random_resolve_rate": 0.187,
782	      "random_95ci": [
783	        0.143,
784	        0.232
785	      ],
786	      "embedding_resolve_rate": 0.19,
787	      "embedding_95ci": [
788	        0.147,
789	        0.235
790	      ],
791	      "dataflow_resolve_rate": 0.183,
792	      "dataflow_95ci": [
793	        0.14,
794	        0.228
795	      ],
796	      "embed_vs_random_delta": 0.003,
797	      "embed_vs_random_delta_95ci": [
798	        -0.038,
799	        0.045
800	      ],
801	      "embed_benefit_bootstrap_p": 0.78,
802	      "dataflow_vs_random_delta": -0.004,
803	      "dataflow_vs_random_delta_95ci": [
804	        -0.048,
805	        0.038
806	      ]
807	    },
808	    "tables": [
809	      {
810	        "name": "Table 14: SWE-bench Bootstrap Statistics",
811	        "columns": [
812	          "comparison",
813	          "delta_pp",
814	          "95%_CI",
815	          "p_value",
816	          "interpretation"
817	        ],
818	        "rows": [
819	          [
820	            "embed vs random",
821	            0.3,
822	            "[-3.8, +4.5]",
823	            0.78,
824	            "not significant"
825	          ],
826	          [
827	            "dataflow vs random",
828	            -0.4,
829	            "[-4.8, +3.8]",
830	            0.68,
831	            "not significant"
832	          ],
833	          [
834	            "dataflow vs embed",
835	            -0.7,
836	            "[-5.2, +3.5]",
837	            0.55,
838	            "not significant"
839	          ]
840	        ]
841	      }
842	    ],
843	    "figures": [],
844	    "analysis": "统计分析确认 SWE-bench 差异不显著。Power analysis 证明 SWE-bench Lite 的 n=300 本质上无法 detect <5pp 的 retriever 差异——这本身是一个 methodological contribution for the negative result paper。\n\n\nBootstrap CI 极宽（±4-5pp），因为 SWE-bench Lite 仅 300 instances， 有效样本更少（~287 after failures）： (1) 单策略 CI 宽度 ~9pp（±4.5pp），策略间 delta（0.3pp）远小于 CI 宽度； (2) Paired delta CI [-3.8pp, +4.5pp] 包含零且两侧几乎对称——没有任何方向性信号； (3) Bootstrap p=0.78 远高于任何合理显著性阈值，确认 delta 不显著； (4) 即使使用 pilot 阶段的 +2.0pp delta，在 n=287 下的 power analysis 显示 需要 ~2000 instances 才能在 α=0.05 下 detect 2pp 的差异——SWE-bench Lite 本质上 underpowered for 这个效应量； (5) 对 negative result paper 有力：不仅 point estimate 接近零，统计检验也 确认无法拒绝零假设。\n"
845	  },
846	  {
847	    "name": "Inference-Time Graph Method Discussion",
848	    "description": "与 CodexGraph, LocAgent 等 inference-time graph 方法的定性比较讨论。\n",
849	    "results": {
850	      "locagent_reported_resolve_rate": 0.262,
851	      "our_best_resolve_rate": 0.19,
852	      "codexgraph_reported_R1": 0.48,
853	      "our_best_R1": 0.523,
854	      "complementarity_evidence": "none"
855	    },
856	    "tables": [
857	      {
858	        "name": "Table 15: Training-Time vs Inference-Time Structure Utilization",
859	        "columns": [
860	          "method",
861	          "structure_usage",
862	          "SWE_bench_resolve",
863	          "retrieval_R1"
864	        ],
865	        "rows": [
866	          [
867	            "ours (random)",
868	            "training negatives",
869	            0.187,
870	            0.523
871	          ],
872	          [
873	            "ours (dataflow)",
874	            "training negatives",
875	            0.183,
876	            0.515
877	          ],
878	          [
879	            "LocAgent",
880	            "inference navigation",
881	            0.262,
882	            "-"
883	          ],
884	          [
885	            "CodexGraph",
886	            "inference navigation",
887	            "-",
888	            "0.48*"
889	          ]
890	        ],
891	        "footer": "*CodexGraph R@1 on different benchmark, not directly comparable"
892	      }
893	    ],
894	    "figures": [],
895	    "analysis": "这个比较将 negative result 升华为 positive insight：结构信息的价值在于 query-adaptive navigation，而非 static negative mining。这为 related work section 提供了 coherent narrative。\n\n\nInference-time graph methods 在 SWE-bench 上的表现远优于我们的 training-time structural mining approach： (1) LocAgent 报告 26.2% resolve rate（vs 我们的 ~19%），差距主要来自 LocAgent 使用 runtime graph navigation（动态探索 call graph at inference）， 而我们的 structural signal 仅用于 static training-time negative selection—— 本质是两种完全不同的信息利用方式； (2) 在 worst 档下我们无法证明 \"training-time structural mining 与 inference-time graph navigation 互补\"——因为 training-time mining 本身无效，所以无互补可言； (3) 这个比较反而支持 inference-time graph methods 是更有效的结构信息利用范式—— structural signal 的价值在 navigation（决定下一步看什么文件）而非 mining （决定训练用什么负样本）； (4) 对 negative result paper 的 framing 有帮助：可以用 inference-time methods 的成功来反衬 training-time mining 的失败，论证 \"structural information 有价值 但应在 inference time 使用\" 这一 insight。\n"
896	  },
897	  {
898	    "name": "Data Pipeline Distribution Audit",
899	    "description": "排查 full-scale 训练数据与 pilot 数据的分布差异，确认 negative result 是真实的 而非工程错误。\n",
900	    "results": {
901	      "pilot_vs_full_repo_overlap": 0.85,
902	      "pilot_mean_files_per_repo": 45,
903	      "full_mean_files_per_repo": 185,
904	      "pilot_difficulty_distribution_ks_p": 0.003,
905	      "pilot_structural_rate": 0.58,
906	      "full_structural_rate": 0.34,
907	      "data_bug_found": false,
908	      "distribution_shift_confirmed": true,
909	      "shift_severity": "moderate"
910	    },
911	    "tables": [
912	      {
913	        "name": "Table A1: Pilot vs Full-Scale Data Distribution",
914	        "columns": [
915	          "metric",
916	          "pilot",
917	          "full_scale",
918	          "p_value"
919	        ],
920	        "rows": [
921	          [
922	            "n_instances",
923	            "~2000",
924	            15133,
925	            "-"
926	          ],
927	          [
928	            "n_repos",
929	            8,
930	            123,
931	            "-"
932	          ],
933	          [
934	            "structural_rate",
935	            0.58,
936	            0.34,
937	            "<0.001"
938	          ],
939	          [
940	            "mean_files_per_repo",
941	            45,
942	            185,
943	            "<0.001"
944	          ],
945	          [
946	            "median_neg_margin_embed",
947	            0.025,
948	            0.017,
949	            0.003
950	          ],
951	          [
952	            "pct_large_repos",
953	            0.3,
954	            0.56,
955	            "<0.001"
956	          ]
957	        ]
958	      }
959	    ],
960	    "figures": [],
961	    "analysis": "Distribution audit 确认 negative result 是真实的——pilot selection bias 导致了 不可复现的初始结论。这个 audit 是 negative result paper 的必要组成部分， 否则 reviewer 会质疑 \"是不是你代码有 bug\"。\n\nFull-scale 数据没有 pipeline bug，但存在明确的分布偏移： (1) Pilot 用了 ~2K instances 从 8-10 个 medium-size repos，structural_data_rate=0.58 （大部分 instances 有结构信息）。Full-scale 15K instances 来自 123 repos， dominated by large/xlarge repos（69/123），structural_data_rate=0.34—— 几乎一半 instances 在 full-scale 中没有结构信息，dataflow strategy 只能 fallback 到 random selection； (2) KS test 确认难度分布显著不同（p=0.003）——full-scale 中 easy instances （大 repo 中的 trivially locatable bugs）比例更高，被所有策略轻松解决， 稀释了策略间差异； (3) 这不是 \"bug\" 而是 \"pilot selection bias\"——pilot repos 被挑选为 CodeQL-friendly （high structural coverage），不代表真实分布。这个 audit 本身是重要的 methodological contribution，论证了 pilot evaluation 的 sampling bias 问题。\n"
962	  }
963	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfb8bfff-dc7f-4dc3-b974-42fb0d52dc95",
  "isSidechain": false,
  "promptId": "f67db5d7-4662-48a7-ba27-d130d41b7555",
  "type": "user",
  "uuid": "1d750658-a06b-45ee-acf2-bcbdcb8d367c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"M2 Full Qwen — 9 seeds × 3 strategies 最终结果\",\n    \"description\": \"Qwen2.5-Coder-3B 在 full-scale 数据上完成全部 27 runs (9 seeds × 3 strategies)。 当前仅 random_s42 完成（R@1=0.553 at step 1000），预测全部完成后的汇总。\\n\",\n    \"results\": {\n      \"random_mean_R1\": 0.523,\n      \"random_std_R1\": 0.031,\n      \"embedding_distance_mean_R1\": 0.521,\n      \"embedding_distance_std_R1\": 0.035,\n      \"dataflow_aware_mean_R1\": 0.515,\n      \"dataflow_aware_std_R1\": 0.038,\n      \"embed_vs_random_delta_pp\": -0.2,\n      \"dataflow_vs_random_delta_pp\": -0.8,\n      \"best_single_run_R1\": 0.553,\n      \"worst_single_run_R1\": 0.478,\n      \"cross_seed_R1_std_pp\": 3.1,\n      \"best_strategy_by_seed_count\": {\n        \"random_wins\": 4,\n        \"embedding_wins\": 3,\n        \"dataflow_wins\": 2\n      },\n      \"overfitting_step_median\": 1000\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2: Qwen Full-Scale R@1 by Strategy × Seed\",\n        \"columns\": [\n          \"seed\",\n          \"random\",\n          \"embedding\",\n          \"dataflow\"\n        ],\n        \"rows\": [\n          [\n            42,\n            0.553,\n            0.547,\n            0.538\n          ],\n          [\n            123,\n            0.528,\n            0.534,\n            0.521\n          ],\n          [\n            456,\n            0.512,\n            0.498,\n            0.503\n          ],\n          [\n            789,\n            0.541,\n            0.543,\n            0.53\n          ],\n          [\n            1024,\n            0.498,\n            0.51,\n            0.496\n          ],\n          [\n            2048,\n            0.519,\n            0.522,\n            0.512\n          ],\n          [\n            3000,\n            0.505,\n            0.503,\n            0.478\n          ],\n          [\n            4096,\n            0.53,\n            0.517,\n            0.525\n          ],\n          [\n            5000,\n            0.523,\n            0.515,\n            0.532\n          ]\n        ],\n        \"footer\": \"Mean±std: random 0.523±0.031, embed 0.521±0.035, dataflow 0.515±0.038\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"策略间 delta (<1pp) 远小于种子间方差 (std~3pp)。Pilot 单种子结果是方差范围内的 正常波动。这是 worst 档的核心发现：embedding benefit 是 pilot-scale 的统计幻觉。\\n\\n\\nPilot 的 +2.0pp embed benefit 来自单种子（s42）在小规模数据上的幸运波动。 Full-scale 数据量从 ~2K 增至 ~15K instances，数据分布发生系统性变化： (1) large/xlarge repos 占比从 pilot 的 ~30% 升至 ~60%，这些 repos 的 structural_data_rate 仅 0.31-0.34，embedding negatives 的质量下降； (2) 训练集难度分布更均匀，pilot 中 embedding mining 选出的\\\"难\\\"样本在 full-scale 中不再难于 random——因为 random pool 本身已足够难； (3) Qwen 的 pos_sim=0.9855 表征饱和在 full-scale 下更严重，所有策略都面临 margin 过小的问题（embedding margin=0.017, 但 random margin 也仅 0.074）， 导致策略间差异被优化噪声覆盖。9 个种子的 std~3pp 远大于策略间 delta~0.2pp。\\n\"\n  },\n  {\n    \"name\": \"M2 Full StarCoder — 9 seeds × 3 strategies 最终结果\",\n    \"description\": \"StarCoder2-3B full-scale 27 runs。当前 random_s42 R@1=0.454 at step 1000。\\n\",\n    \"results\": {\n      \"random_mean_R1\": 0.443,\n      \"random_std_R1\": 0.028,\n      \"embedding_distance_mean_R1\": 0.435,\n      \"embedding_distance_std_R1\": 0.033,\n      \"dataflow_aware_mean_R1\": 0.428,\n      \"dataflow_aware_std_R1\": 0.04,\n      \"embed_vs_random_delta_pp\": -0.8,\n      \"dataflow_vs_random_delta_pp\": -1.5,\n      \"cross_seed_R1_std_pp\": 3.4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: StarCoder Full-Scale R@1 by Strategy × Seed\",\n        \"columns\": [\n          \"seed\",\n          \"random\",\n          \"embedding\",\n          \"dataflow\"\n        ],\n        \"rows\": [\n          [\n            42,\n            0.454,\n            0.448,\n            0.442\n          ],\n          [\n            123,\n            0.44,\n            0.425,\n            0.418\n          ],\n          [\n            456,\n            0.462,\n            0.456,\n            0.44\n          ],\n          [\n            789,\n            0.435,\n            0.43,\n            0.412\n          ],\n          [\n            1024,\n            0.448,\n            0.442,\n            0.435\n          ],\n          [\n            2048,\n            0.425,\n            0.418,\n            0.398\n          ],\n          [\n            3000,\n            0.458,\n            0.45,\n            0.448\n          ],\n          [\n            4096,\n            0.43,\n            0.422,\n            0.425\n          ],\n          [\n            5000,\n            0.438,\n            0.428,\n            0.43\n          ]\n        ],\n        \"footer\": \"Mean±std: random 0.443±0.028, embed 0.435±0.033, dataflow 0.428±0.040\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"StarCoder 上 dataflow 甚至表现最差（-1.5pp vs random），方向与 pilot 一致但 幅度更大。Embedding 也未能帮助。结论：两编码器在 full-scale 下均不支持任何 非 random 策略的优势。\\n\\n\\nStarCoder pilot 已经是 negative conclusion（dataflow R@1=0.487 < random 0.492）。 Full-scale 放大了这个趋势：(1) StarCoder 表征空间 \\\"healthy\\\"（pos_sim=0.80）， random negatives 已提供足够梯度（margin=0.194），embedding/dataflow 引入的更难 negatives 反而导致训练不稳定——loss landscape 更尖锐，不同种子落入不同局部最优； (2) dataflow negatives 在 StarCoder 上 margin=0.119 vs embedding 0.067， dataflow 实际上更\\\"容易\\\"，但 full-scale 下这个 margin 差异未能转化为性能优势， 因为 StarCoder 的问题不是 negative difficulty 而是编码器容量限制（3B 参数 + LoRA rank 受限时，更难 negatives 导致梯度冲突）。Cross-seed std 3.4pp 进一步 确认策略差异 (<1.5pp) 不可靠。\\n\"\n  },\n  {\n    \"name\": \"M3a SWE-bench Lite End-to-End Evaluation\",\n    \"description\": \"SWE-bench Lite (300 instances) end-to-end evaluation，使用 Qwen3.6-27B agent， 对比 3 个 strategy 的 best checkpoint 作为 retriever。\\n\",\n    \"results\": {\n      \"random_resolve_rate\": 0.187,\n      \"embedding_resolve_rate\": 0.19,\n      \"dataflow_resolve_rate\": 0.183,\n      \"embed_vs_random_delta_pp\": 0.3,\n      \"dataflow_vs_random_delta_pp\": -0.4,\n      \"swebench_resolve_delta_pp\": 0.3,\n      \"retrieval_R1_on_swebench\": {\n        \"random\": 0.42,\n        \"embedding\": 0.43,\n        \"dataflow\": 0.41\n      },\n      \"n_instances_evaluated\": 287,\n      \"n_instances_failed\": 13\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: SWE-bench Lite Resolve Rates\",\n        \"columns\": [\n          \"strategy\",\n          \"resolve_rate\",\n          \"retrieval_R1\",\n          \"n_resolved\",\n          \"n_total\"\n        ],\n        \"rows\": [\n          [\n            \"random\",\n            0.187,\n            0.42,\n            54,\n            287\n          ],\n          [\n            \"embedding_distance\",\n            0.19,\n            0.43,\n            55,\n            287\n          ],\n          [\n            \"dataflow_aware\",\n            0.183,\n            0.41,\n            53,\n            287\n          ]\n        ],\n        \"footer\": \"Best delta: +0.3pp (embed vs random), not significant (p=0.89 McNemar)\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SWE-bench 结果不仅不支持 embedding/dataflow 策略的优势，甚至所有策略的 resolve rate 都低于 SweRank baseline。这暗示 full-scale 训练可能引入了某种 regression（数据分布 偏移？）。需排查训练数据与 SWE-bench 的 domain overlap。\\n\\n\\nSWE-bench Lite 的 resolve rate 由 retrieval → agent pipeline 多阶段组成， retriever 差异被下游 agent 的 stochasticity 大幅稀释。即使 retrieval R@1 差异 存在 1pp，经过 agent 的 code generation + apply patch + test 环节后，resolve rate 差异被压缩到 <0.5pp。具体原因： (1) SWE-bench 中很多 \\\"easy\\\" instances（~30%）任何 retriever 都能找到正确文件， 策略差异为零； (2) \\\"hard\\\" instances（~25%）任何 retriever 都找不到，agent 依赖推理能力而非检索； (3) 只有 ~45% 的中间难度 instances 中 retrieval 策略可能产生差异，但 agent 的 code generation variance（温度、context window 限制）进一步模糊了信号； (4) 300 instances 中有效差异空间 ~135 个，0.3pp delta 对应仅 ~1 个额外解决的 instance，完全在噪声范围内。此外 full-scale retriever 本身策略间差异已消失， SWE-bench 只是进一步确认。\\n\"\n  },\n  {\n    \"name\": \"M3b RepoBench-R Cross-File Retrieval\",\n    \"description\": \"RepoBench-R 作为第二基准，retrieval-only 评估，无 LLM agent。\\n\",\n    \"results\": {\n      \"random_R1\": 0.312,\n      \"embedding_R1\": 0.308,\n      \"dataflow_R1\": 0.295,\n      \"embed_vs_random_delta_pp\": -0.4,\n      \"dataflow_vs_random_delta_pp\": -1.7,\n      \"random_R5\": 0.58,\n      \"embedding_R5\": 0.57,\n      \"dataflow_R5\": 0.56,\n      \"pretrained_baseline_R1\": 0.285\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: RepoBench-R Results (Qwen encoder)\",\n        \"columns\": [\n          \"strategy\",\n          \"R@1\",\n          \"R@5\",\n          \"R@10\",\n          \"MRR\"\n        ],\n        \"rows\": [\n          [\n            \"pretrained\",\n            0.285,\n            0.52,\n            0.68,\n            0.401\n          ],\n          [\n            \"random\",\n            0.312,\n            0.58,\n            0.73,\n            0.438\n          ],\n          [\n            \"embedding_distance\",\n            0.308,\n            0.57,\n            0.72,\n            0.432\n          ],\n          [\n            \"dataflow_aware\",\n            0.295,\n            0.56,\n            0.71,\n            0.418\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RepoBench-R 进一步证明策略差异不稳定且 domain-dependent。Dataflow 策略的负迁移 尤其严重（-1.7pp），支持 negative result 叙事中 \\\"structural negatives 不 generalize\\\" 的论点。\\n\\n\\nRepoBench-R 是 cross-file completion 任务，与 SWE-smith 的 bug localization 分布差异更大。Full-scale 训练在 SWE-smith 上 overfit 的模型在 RepoBench 上 表现出不同的行为模式： (1) 所有策略都优于 pretrained baseline（+2-3pp），说明 contrastive fine-tuning 本身有效，但策略间差异在 domain shift 下被进一步压缩； (2) Dataflow negatives 在 RepoBench 上表现最差，因为 SWE-smith 的 dataflow 结构 （bug-fix oriented）与 RepoBench 的 completion-oriented 代码结构不匹配—— SWE-smith 中 disconnected = irrelevant 的假设在 completion 场景中不成立； (3) Embedding negatives 略低于 random 是因为 full-scale embedding mining 选出的 negatives 过度 fit 到 SWE-smith 的相似性分布，domain shift 后反而损害泛化。\\n\"\n  },\n  {\n    \"name\": \"Embedding vs Random Deep Stratified Analysis\",\n    \"description\": \"按 repo size、code complexity、neg_difficulty 分层分析 embedding negatives 的效果。\\n\",\n    \"results\": {\n      \"by_repo_size\": {\n        \"small_lt50\": {\n          \"random_R1\": 0.61,\n          \"embedding_R1\": 0.59,\n          \"delta_pp\": -2.0\n        },\n        \"medium_50_200\": {\n          \"random_R1\": 0.54,\n          \"embedding_R1\": 0.55,\n          \"delta_pp\": 1.0\n        },\n        \"large_200_500\": {\n          \"random_R1\": 0.51,\n          \"embedding_R1\": 0.5,\n          \"delta_pp\": -1.0\n        },\n        \"xlarge_500plus\": {\n          \"random_R1\": 0.48,\n          \"embedding_R1\": 0.48,\n          \"delta_pp\": 0.0\n        }\n      },\n      \"by_neg_difficulty_quartile\": {\n        \"easy_q1_delta_pp\": 0.5,\n        \"medium_q2_delta_pp\": -0.3,\n        \"hard_q3_delta_pp\": -1.2,\n        \"hardest_q4_delta_pp\": -2.1\n      },\n      \"correlation_margin_vs_benefit\": -0.15,\n      \"correlation_repo_size_vs_benefit\": -0.08\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Embedding Benefit by Repo Size\",\n        \"columns\": [\n          \"repo_tier\",\n          \"n_instances\",\n          \"random_R1\",\n          \"embed_R1\",\n          \"delta_pp\"\n        ],\n        \"rows\": [\n          [\n            \"small (<50)\",\n            500,\n            0.61,\n            0.59,\n            -2.0\n          ],\n          [\n            \"medium (50-200)\",\n            4096,\n            0.54,\n            0.55,\n            1.0\n          ],\n          [\n            \"large (200-500)\",\n            13628,\n            0.51,\n            0.5,\n            -1.0\n          ],\n          [\n            \"xlarge (500+)\",\n            25949,\n            0.48,\n            0.48,\n            0.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心发现：embedding benefit 是 repo size 和 negative difficulty 的函数， 在 pilot 的 data composition 下恰好为正，在 full-scale 的 data composition 下 恰好为零或负。这不是方法失败，而是 pilot evaluation bias——小规模评估 over-represents 中等 repo，恰好是 embedding mining 的 sweet spot。\\n\\n\\n分层分析揭示 embedding benefit 不是\\\"消失\\\"而是\\\"抵消\\\"——在某些 strata 正向、 其他 strata 负向，总和接近零： (1) Small repos 上 embedding mining 实际有害（-2pp），因为小 repo 的 file pool 只有 ~10-50 个文件，embedding mining 选出的 \\\"nearest\\\" negative 往往就是 gold file 的近邻（同一个 module），形成 false hard negatives 损害训练信号； (2) Medium repos 上 embedding 略有优势（+1pp），因为 pool 足够大使 mining 选到 真正的 hard negatives，且难度梯度合理； (3) Large/xlarge repos 上差异消失，因为 random sampling 在大 pool 中已经有合理 概率采到 moderately hard negatives，embedding mining 的额外选择性优势被稀释； (4) 按 neg_difficulty 分层更清晰：最难 quartile（margin 最小）中 embedding 有害 （-2.1pp），因为过难的 negatives 导致梯度冲突/训练不稳定。这解释了为什么 full-scale（更多 large repos → 更多 hard quartile instances）中 benefit 消失。\\n\"\n  },\n  {\n    \"name\": \"Hop-Distance Call-Graph Bounding Ablation\",\n    \"description\": \"1-hop vs 2-hop vs 3-hop call-graph bounding 对 dataflow negative 质量的影响。\\n\",\n    \"results\": {\n      \"hop_1\": {\n        \"connected_pct\": 0.12,\n        \"disconnected_neg_margin\": 0.035,\n        \"training_R1\": 0.513\n      },\n      \"hop_2\": {\n        \"connected_pct\": 0.34,\n        \"disconnected_neg_margin\": 0.029,\n        \"training_R1\": 0.515\n      },\n      \"hop_3\": {\n        \"connected_pct\": 0.58,\n        \"disconnected_neg_margin\": 0.022,\n        \"training_R1\": 0.51\n      },\n      \"delta_1hop_vs_2hop_pp\": -0.2,\n      \"delta_2hop_vs_3hop_pp\": 0.5,\n      \"all_vs_random_best_pp\": -0.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Hop-Distance Ablation (Qwen, seed 42)\",\n        \"columns\": [\n          \"hops\",\n          \"connected_pct\",\n          \"disconn_margin\",\n          \"R@1\",\n          \"vs_random_pp\"\n        ],\n        \"rows\": [\n          [\n            1,\n            0.12,\n            0.035,\n            0.513,\n            -1.0\n          ],\n          [\n            2,\n            0.34,\n            0.029,\n            0.515,\n            -0.8\n          ],\n          [\n            3,\n            0.58,\n            0.022,\n            0.51,\n            -1.3\n          ],\n          [\n            \"random\",\n            \"-\",\n            \"-\",\n            0.523,\n            0.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Hop distance 是 second-order 参数——当 first-order 效应（结构断开作为 hardness proxy） 本身无效时，调节粒度无法改变结论。\\n\\n\\nHop distance 改变 connected/disconnected 的划分粒度，但在 worst 档下无法拯救 dataflow 策略： (1) 1-hop 过于严格（仅 12% connected），大量 gold-relevant files 被错误标记为 disconnected，产生大量 false hard negatives → 训练信号受损； (2) 2-hop（当前设置）是 pilot 中的最优，但 full-scale 下效果与 random 无异； (3) 3-hop 过于宽泛（58% connected），disconnected pool 缩小到几乎只剩 truly unrelated files，这些 negatives 太容易（margin=0.022），训练信号退化为 接近 random sampling 的效果但 pool 更小； (4) 三种 hop 设置的 R@1 范围仅 0.510-0.515，都低于 random baseline 0.523， 说明 structural bounding 本身在 full-scale 下不是一个有效的 negative selection 维度——问题出在 \\\"结构断开≠语义无关\\\" 这个核心假设。\\n\"\n  },\n  {\n    \"name\": \"Training Data Size Scaling Ablation\",\n    \"description\": \"1K vs 3K vs 5K（当前 full-scale ~15K instances 中子采样）对策略差异的影响。\\n\",\n    \"results\": {\n      \"size_1k\": {\n        \"random_R1\": 0.505,\n        \"embedding_R1\": 0.518,\n        \"dataflow_R1\": 0.512,\n        \"embed_delta_pp\": 1.3\n      },\n      \"size_3k\": {\n        \"random_R1\": 0.515,\n        \"embedding_R1\": 0.52,\n        \"dataflow_R1\": 0.513,\n        \"embed_delta_pp\": 0.5\n      },\n      \"size_5k\": {\n        \"random_R1\": 0.52,\n        \"embedding_R1\": 0.521,\n        \"dataflow_R1\": 0.516,\n        \"embed_delta_pp\": 0.1\n      },\n      \"size_15k_full\": {\n        \"random_R1\": 0.523,\n        \"embedding_R1\": 0.521,\n        \"dataflow_R1\": 0.515,\n        \"embed_delta_pp\": -0.2\n      },\n      \"embed_benefit_slope_per_1k\": -0.11\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Data Size × Strategy Interaction\",\n        \"columns\": [\n          \"data_size\",\n          \"random_R1\",\n          \"embed_R1\",\n          \"dataflow_R1\",\n          \"embed_delta\"\n        ],\n        \"rows\": [\n          [\n            \"1K\",\n            0.505,\n            0.518,\n            0.512,\n            1.3\n          ],\n          [\n            \"3K\",\n            0.515,\n            0.52,\n            0.513,\n            0.5\n          ],\n          [\n            \"5K\",\n            0.52,\n            0.521,\n            0.516,\n            0.1\n          ],\n          [\n            \"15K (full)\",\n            0.523,\n            0.521,\n            0.515,\n            -0.2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这张图是论文的核心 figure——直观展示 \\\"hard negative mining 的收益随数据规模递减 并最终消失\\\" 的 scaling law。对 negative result paper 的贡献极大，因为它提供了 可预测的量化关系，而非仅仅 \\\"结果没复现\\\" 的定性陈述。\\n\\n\\n这个 ablation 精确解释了 pilot-to-full-scale discrepancy 的机制： (1) 1K instances（≈pilot 规模）复现了 pilot 的 embedding benefit（+1.3pp）， 确认 pilot 结果本身没有 bug——在小规模下 embedding mining 确实有效； (2) 随数据量增长，benefit 单调递减（斜率≈-0.11pp per 1K instances）； (3) 原因是 data scaling 改变了有效 negative difficulty 分布——1K 时 random pool 中真正 hard 的 negatives 极少（小 pool → 大多是 easy negatives），embedding mining 通过选择 nearest neighbors 提供了必要的 difficulty gradient。但随着 pool 增大， random sampling 的\\\"命中率\\\"自然上升，embedding mining 的增量价值趋零； (4) 5K 处 delta 已缩至 0.1pp（不显著），15K 处反转为 -0.2pp； (5) 这是 negative result paper 的关键证据：small-scale evaluation 系统性高估 hard negative mining 的收益，因为 scale 本身就是一种隐性的 negative difficulty 调节器。\\n\"\n  },\n  {\n    \"name\": \"Fusion Head Architecture Ablation\",\n    \"description\": \"Embedding-only vs structural-features-only vs combined fusion head， 测试结构特征是否通过不同 fusion 方式提供价值。\\n\",\n    \"results\": {\n      \"embedding_only_R1\": 0.523,\n      \"structural_only_R1\": 0.385,\n      \"combined_R1\": 0.519,\n      \"embed_only_vs_combined_pp\": 0.4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Fusion Head Ablation (Qwen, seed 42)\",\n        \"columns\": [\n          \"head_type\",\n          \"R@1\",\n          \"R@5\",\n          \"val_loss\"\n        ],\n        \"rows\": [\n          [\n            \"embedding_only\",\n            0.523,\n            0.955,\n            0.486\n          ],\n          [\n            \"structural_features\",\n            0.385,\n            0.78,\n            0.812\n          ],\n          [\n            \"combined\",\n            0.519,\n            0.95,\n            0.495\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"结构特征作为独立信号维度不足，作为辅助信号有害。这排除了 \\\"也许 dataflow 信号有用 但 negative mining 不是正确的注入方式\\\" 的替代假设。\\n\\n\\nFusion head 架构无法从无到有创造 structural signal 的价值： (1) Embedding-only head 与 random strategy 性能相当（0.523），因为 LoRA fine-tuned embeddings 本身已捕获了足够的 code similarity 信息； (2) Structural-features-only head 大幅下降至 0.385——结构特征（is_connected, dataflow_distance, call_graph_hops）单独不足以判断 relevance，因为大部分 file pairs 的结构特征是 sparse 的（structural_data_rate=0.34，66% pairs 无结构信息）； (3) Combined head 反而略低于 embedding-only（-0.4pp），因为 noisy structural features 干扰了 embedding signal——当 66% instances 的结构特征为 null/zero 时， fusion layer 必须学会忽略结构维度，但 LoRA 的低秩约束使这个 \\\"ignore\\\" 信号 不够干净； (4) 这进一步支持了 structural signal 在 full-scale 下无效的结论。\\n\"\n  },\n  {\n    \"name\": \"Dataflow-Distance Weighted vs Binary Negatives\",\n    \"description\": \"连续 dataflow distance 加权 vs 二元 connected/disconnected 的 negative selection。\\n\",\n    \"results\": {\n      \"binary_disconnected_R1\": 0.515,\n      \"distance_weighted_R1\": 0.517,\n      \"delta_pp\": 0.2,\n      \"vs_random_pp\": -0.6\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"细化无效信号的粒度不改善性能。这是对 \\\"也许我们只需要更好的结构度量\\\" 假设的反驳。\\n\\n\\nDistance weighting 是对 binary disconnected 的细化——用 shortest dataflow path length 作为权重偏好更远的（更 disconnected）negatives。但在 worst 档下改进微乎其微 （+0.2pp vs binary），因为： (1) 核心问题不是 negative selection 的粒度，而是 structural disconnection 作为 hardness proxy 本身的有效性——weighted 版本在一个无效信号上做更精细的选择， 不改变根本问题； (2) 距离信息 noisy——CodeQL 的 dataflow path 是 approximation，real shortest path 与 estimated path 的相关性仅 ~0.6（由于 scope bounding），weighting 基于 noisy distance 引入额外噪声； (3) 两个版本都低于 random baseline（-0.6pp），进一步确认结构信号无效。\\n\"\n  },\n  {\n    \"name\": \"Failure Analysis: 50 SweRank/BM25 Failures\",\n    \"description\": \"对 50 个 SweRank/BM25 检索失败的 SWE-bench instances 进行手动分类， 分析 dataflow 信号是否能帮助。\\n\",\n    \"results\": {\n      \"n_analyzed\": 50,\n      \"categories\": {\n        \"cross_file_dependency\": 18,\n        \"naming_ambiguity\": 12,\n        \"scattered_changes\": 9,\n        \"test_file_confusion\": 7,\n        \"other\": 4\n      },\n      \"dataflow_could_help\": 6,\n      \"dataflow_actually_helped\": 2,\n      \"dataflow_hurt\": 3,\n      \"dataflow_neutral\": 39\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Failure Category Analysis\",\n        \"columns\": [\n          \"category\",\n          \"count\",\n          \"df_could_help\",\n          \"df_actually_helped\",\n          \"df_hurt\"\n        ],\n        \"rows\": [\n          [\n            \"cross_file_dep\",\n            18,\n            4,\n            1,\n            1\n          ],\n          [\n            \"naming_ambiguity\",\n            12,\n            0,\n            0,\n            1\n          ],\n          [\n            \"scattered_changes\",\n            9,\n            2,\n            1,\n            1\n          ],\n          [\n            \"test_confusion\",\n            7,\n            0,\n            0,\n            0\n          ],\n          [\n            \"other\",\n            4,\n            0,\n            0,\n            0\n          ],\n          [\n            \"total\",\n            50,\n            6,\n            2,\n            3\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Dataflow 的理论覆盖面（12% = 6/50 可能帮助）和实际有效率（4% = 2/50 实际帮助） 远低于立论所需。对 negative result paper 的贡献：提供 error taxonomy 证明 structural signal 的适用范围窄于预期。\\n\\n\\n手动分析 50 个失败案例后发现 dataflow 信号能帮助的场景远少于预期： (1) Cross-file dependency（18 cases）是 dataflow 理论上的 sweet spot，但实际 仅 4/18 有可用的 CodeQL dataflow 路径——其余 14 个的 dependency 是通过 import、 type reference 或 configuration 而非 data flow，CodeQL 的 inter-procedural analysis 未覆盖这些； (2) Naming ambiguity（12 cases）中 dataflow 无法帮助——问题是同名函数/类在 不同 module 中，structural 和 textual signal 同时失效； (3) 6 个理论上 dataflow 可帮助的 cases 中，仅 2 个实际在 dataflow-trained model 中被正确检索——另 4 个因训练不稳定/过拟合而性能退化抵消了理论优势； (4) 3 个 cases 中 dataflow 实际有害——将结构上相关但 gold set 外的文件排入 top-1，挤掉了正确答案。\\n\"\n  },\n  {\n    \"name\": \"Qualitative Examples: Structural Negatives Impact\",\n    \"description\": \"挑选 5-10 个 structural negatives 改变检索结果的定性案例。\\n\",\n    \"results\": {\n      \"positive_examples_found\": 3,\n      \"negative_examples_found\": 4,\n      \"neutral_examples\": 3,\n      \"net_narrative\": \"negative\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"定性证据反而支持 negative result 叙事。典型 failure mode（structural proximity ≠ task relevance）是重要的methodological insight。\\n\\n\\n在 worst 档下，能找到的正面案例数量与负面案例相当甚至更少： (1) 3 个正面案例：dataflow training 将结构相关文件从 top-5 提升到 top-1， 但这些改善也出现在 embedding strategy 的部分种子中，不能归因于 dataflow； (2) 4 个负面案例：dataflow training 将结构上相近但 gold set 外的文件推高排名， 挤掉了正确答案。典型模式：文件 A 通过 data flow 连接到 gold file B， dataflow 策略错误地将 A 排在 B 之前； (3) 3 个中性案例：dataflow 改变了 top-10 内的排序但不影响 top-1/top-5； (4) 定性分析 net negative，无法支撑 paper 中的正面叙事。对 negative result paper 可用——展示 structural negatives 的 failure modes。\\n\"\n  },\n  {\n    \"name\": \"Temperature Ablation: τ ∈ {0.05, 0.1, 0.2}\",\n    \"description\": \"三个温度 × 三个策略，测试 embedding benefit 是否是温度 regime-specific。\\n\",\n    \"results\": {\n      \"tau_005\": {\n        \"random_R1\": 0.498,\n        \"embedding_R1\": 0.485,\n        \"dataflow_R1\": 0.475,\n        \"embed_delta_pp\": -1.3\n      },\n      \"tau_010\": {\n        \"random_R1\": 0.523,\n        \"embedding_R1\": 0.521,\n        \"dataflow_R1\": 0.515,\n        \"embed_delta_pp\": -0.2\n      },\n      \"tau_020\": {\n        \"random_R1\": 0.51,\n        \"embedding_R1\": 0.508,\n        \"dataflow_R1\": 0.502,\n        \"embed_delta_pp\": -0.2\n      },\n      \"best_overall_tau\": 0.1,\n      \"any_tau_with_significant_embed_benefit\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Temperature × Strategy Interaction (Qwen, mean of 3 seeds)\",\n        \"columns\": [\n          \"tau\",\n          \"random\",\n          \"embedding\",\n          \"dataflow\",\n          \"best_strategy\"\n        ],\n        \"rows\": [\n          [\n            0.05,\n            0.498,\n            0.485,\n            0.475,\n            \"random\"\n          ],\n          [\n            0.1,\n            0.523,\n            0.521,\n            0.515,\n            \"random\"\n          ],\n          [\n            0.2,\n            0.51,\n            0.508,\n            0.502,\n            \"random\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Temperature 不是 confound——在所有温度 regime 下，random 策略都是最优或并列最优。 排除了 \\\"pilot 的 embedding benefit 是因为 τ=0.1 恰好适合 embedding mining\\\" 的假设。\\n\\n\\n温度调节改变 contrastive loss 对 similarity margin 的敏感度，但无法拯救无效的 mining strategy： (1) τ=0.05 使 loss 对 margin 极其敏感——在 Qwen 的 saturated space （pos_sim=0.9855, embedding neg_sim=0.9685, margin=0.017）中，如此小的 margin 在 τ=0.05 下产生几乎相同的 loss 贡献，embedding negatives 等于 random。 但更严重的是 τ=0.05 放大了个别 extreme negative 的梯度，导致训练不稳定， 所有策略性能下降（尤其 dataflow，因为 dataflow negatives 的 margin distribution 更 heavy-tailed）； (2) τ=0.10（当前默认）是最优温度，但策略间无显著差异； (3) τ=0.20 使 loss 对 margin 不够敏感——hard negatives 的额外 difficulty 被 soft temperature 压缩，embedding/dataflow mining 的理论优势被进一步稀释； (4) 没有任何温度 regime 能让 embedding benefit 达到统计显著，因为 full-scale 下策略间的 \\\"信号\\\" 本身不存在（是 pilot 的噪声），温度只是调节 loss landscape 的曲率，不能创造信号。\\n\"\n  },\n  {\n    \"name\": \"Dynamic Embedding Mining vs Static\",\n    \"description\": \"Per-epoch 重新 mining embedding negatives vs 一次性从 pretrained model mining。\\n\",\n    \"results\": {\n      \"static_embedding_R1\": 0.521,\n      \"dynamic_epoch1_R1\": 0.521,\n      \"dynamic_epoch2_R1\": 0.519,\n      \"dynamic_epoch3_R1\": 0.515,\n      \"dynamic_mean_R1\": 0.518,\n      \"dynamic_vs_static_pp\": -0.3,\n      \"dynamic_vs_random_pp\": -0.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Static vs Dynamic Mining (Qwen, seed 42)\",\n        \"columns\": [\n          \"method\",\n          \"epoch1_R1\",\n          \"epoch2_R1\",\n          \"epoch3_R1\",\n          \"best_R1\"\n        ],\n        \"rows\": [\n          [\n            \"static\",\n            0.54,\n            0.53,\n            0.512,\n            0.54\n          ],\n          [\n            \"dynamic\",\n            0.54,\n            0.525,\n            0.505,\n            0.54\n          ],\n          [\n            \"random\",\n            0.535,\n            0.528,\n            0.51,\n            0.535\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Dynamic mining 排除了 \\\"staleness\\\" 作为 embedding mining 失效的解释。 Mining 策略本身在大规模下不提供增量价值。\\n\\n\\nDynamic mining 理论上解决 \\\"pretrained embedding 与 fine-tuned embedding 偏移导致 negatives 过时\\\" 的问题。但在 worst 档下非但不改善，反而略有下降： (1) Epoch 1 dynamic ≈ static（因为 epoch 1 开始时 model 就是 pretrained， mining 结果相同）； (2) Epoch 2-3 的 re-mining 产生了 curriculum shift 效应——随着 model 改善， nearest neighbors 改变，新选出的 negatives 更难但也更 noisy（因为 fine-tuned model 的 embedding space 在 LoRA 下只部分更新，re-mining 的 nearest neighbors 可能是 LoRA 的 artifacts 而非真正的 hard negatives）； (3) Re-mining 引入的计算开销显著（每 epoch 需重新编码全部 ~44K instances， ~2h per re-mining），cost-benefit 明显不值得； (4) Dynamic mining 的失败进一步证明问题不是 \\\"mining 过时\\\" 而是 \\\"mining 本身 在大规模下无效\\\"。\\n\"\n  },\n  {\n    \"name\": \"Bootstrap CI for SWE-bench Resolve Rates\",\n    \"description\": \"10,000 bootstrap resamples 计算 SWE-bench resolve rate 的 95% CI。\\n\",\n    \"results\": {\n      \"random_resolve_rate\": 0.187,\n      \"random_95ci\": [\n        0.143,\n        0.232\n      ],\n      \"embedding_resolve_rate\": 0.19,\n      \"embedding_95ci\": [\n        0.147,\n        0.235\n      ],\n      \"dataflow_resolve_rate\": 0.183,\n      \"dataflow_95ci\": [\n        0.14,\n        0.228\n      ],\n      \"embed_vs_random_delta\": 0.003,\n      \"embed_vs_random_delta_95ci\": [\n        -0.038,\n        0.045\n      ],\n      \"embed_benefit_bootstrap_p\": 0.78,\n      \"dataflow_vs_random_delta\": -0.004,\n      \"dataflow_vs_random_delta_95ci\": [\n        -0.048,\n        0.038\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: SWE-bench Bootstrap Statistics\",\n        \"columns\": [\n          \"comparison\",\n          \"delta_pp\",\n          \"95%_CI\",\n          \"p_value\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"embed vs random\",\n            0.3,\n            \"[-3.8, +4.5]\",\n            0.78,\n            \"not significant\"\n          ],\n          [\n            \"dataflow vs random\",\n            -0.4,\n            \"[-4.8, +3.8]\",\n            0.68,\n            \"not significant\"\n          ],\n          [\n            \"dataflow vs embed\",\n            -0.7,\n            \"[-5.2, +3.5]\",\n            0.55,\n            \"not significant\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"统计分析确认 SWE-bench 差异不显著。Power analysis 证明 SWE-bench Lite 的 n=300 本质上无法 detect <5pp 的 retriever 差异——这本身是一个 methodological contribution for the negative result paper。\\n\\n\\nBootstrap CI 极宽（±4-5pp），因为 SWE-bench Lite 仅 300 instances， 有效样本更少（~287 after failures）： (1) 单策略 CI 宽度 ~9pp（±4.5pp），策略间 delta（0.3pp）远小于 CI 宽度； (2) Paired delta CI [-3.8pp, +4.5pp] 包含零且两侧几乎对称——没有任何方向性信号； (3) Bootstrap p=0.78 远高于任何合理显著性阈值，确认 delta 不显著； (4) 即使使用 pilot 阶段的 +2.0pp delta，在 n=287 下的 power analysis 显示 需要 ~2000 instances 才能在 α=0.05 下 detect 2pp 的差异——SWE-bench Lite 本质上 underpowered for 这个效应量； (5) 对 negative result paper 有力：不仅 point estimate 接近零，统计检验也 确认无法拒绝零假设。\\n\"\n  },\n  {\n    \"name\": \"Inference-Time Graph Method Discussion\",\n    \"description\": \"与 CodexGraph, LocAgent 等 inference-time graph 方法的定性比较讨论。\\n\",\n    \"results\": {\n      \"locagent_reported_resolve_rate\": 0.262,\n      \"our_best_resolve_rate\": 0.19,\n      \"codexgraph_reported_R1\": 0.48,\n      \"our_best_R1\": 0.523,\n      \"complementarity_evidence\": \"none\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Training-Time vs Inference-Time Structure Utilization\",\n        \"columns\": [\n          \"method\",\n          \"structure_usage\",\n          \"SWE_bench_resolve\",\n          \"retrieval_R1\"\n        ],\n        \"rows\": [\n          [\n            \"ours (random)\",\n            \"training negatives\",\n            0.187,\n            0.523\n          ],\n          [\n            \"ours (dataflow)\",\n            \"training negatives\",\n            0.183,\n            0.515\n          ],\n          [\n            \"LocAgent\",\n            \"inference navigation\",\n            0.262,\n            \"-\"\n          ],\n          [\n            \"CodexGraph\",\n            \"inference navigation\",\n            \"-\",\n            \"0.48*\"\n          ]\n        ],\n        \"footer\": \"*CodexGraph R@1 on different benchmark, not directly comparable\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这个比较将 negative result 升华为 positive insight：结构信息的价值在于 query-adaptive navigation，而非 static negative mining。这为 related work section 提供了 coherent narrative。\\n\\n\\nInference-time graph methods 在 SWE-bench 上的表现远优于我们的 training-time structural mining approach： (1) LocAgent 报告 26.2% resolve rate（vs 我们的 ~19%），差距主要来自 LocAgent 使用 runtime graph navigation（动态探索 call graph at inference）， 而我们的 structural signal 仅用于 static training-time negative selection—— 本质是两种完全不同的信息利用方式； (2) 在 worst 档下我们无法证明 \\\"training-time structural mining 与 inference-time graph navigation 互补\\\"——因为 training-time mining 本身无效，所以无互补可言； (3) 这个比较反而支持 inference-time graph methods 是更有效的结构信息利用范式—— structural signal 的价值在 navigation（决定下一步看什么文件）而非 mining （决定训练用什么负样本）； (4) 对 negative result paper 的 framing 有帮助：可以用 inference-time methods 的成功来反衬 training-time mining 的失败，论证 \\\"structural information 有价值 但应在 inference time 使用\\\" 这一 insight。\\n\"\n  },\n  {\n    \"name\": \"Data Pipeline Distribution Audit\",\n    \"description\": \"排查 full-scale 训练数据与 pilot 数据的分布差异，确认 negative result 是真实的 而非工程错误。\\n\",\n    \"results\": {\n      \"pilot_vs_full_repo_overlap\": 0.85,\n      \"pilot_mean_files_per_repo\": 45,\n      \"full_mean_files_per_repo\": 185,\n      \"pilot_difficulty_distribution_ks_p\": 0.003,\n      \"pilot_structural_rate\": 0.58,\n      \"full_structural_rate\": 0.34,\n      \"data_bug_found\": false,\n      \"distribution_shift_confirmed\": true,\n      \"shift_severity\": \"moderate\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table A1: Pilot vs Full-Scale Data Distribution\",\n        \"columns\": [\n          \"metric\",\n          \"pilot\",\n          \"full_scale\",\n          \"p_value\"\n        ],\n        \"rows\": [\n          [\n            \"n_instances\",\n            \"~2000\",\n            15133,\n            \"-\"\n          ],\n          [\n            \"n_repos\",\n            8,\n            123,\n            \"-\"\n          ],\n          [\n            \"structural_rate\",\n            0.58,\n            0.34,\n            \"<0.001\"\n          ],\n          [\n            \"mean_files_per_repo\",\n            45,\n            185,\n            \"<0.001\"\n          ],\n          [\n            \"median_neg_margin_embed\",\n            0.025,\n            0.017,\n            0.003\n          ],\n          [\n            \"pct_large_repos\",\n            0.3,\n            0.56,\n            \"<0.001\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Distribution audit 确认 negative result 是真实的——pilot selection bias 导致了 不可复现的初始结论。这个 audit 是 negative result paper 的必要组成部分， 否则 reviewer 会质疑 \\\"是不是你代码有 bug\\\"。\\n\\nFull-scale 数据没有 pipeline bug，但存在明确的分布偏移： (1) Pilot 用了 ~2K instances 从 8-10 个 medium-size repos，structural_data_rate=0.58 （大部分 instances 有结构信息）。Full-scale 15K instances 来自 123 repos， dominated by large/xlarge repos（69/123），structural_data_rate=0.34—— 几乎一半 instances 在 full-scale 中没有结构信息，dataflow strategy 只能 fallback 到 random selection； (2) KS test 确认难度分布显著不同（p=0.003）——full-scale 中 easy instances （大 repo 中的 trivially locatable bugs）比例更高，被所有策略轻松解决， 稀释了策略间差异； (3) 这不是 \\\"bug\\\" 而是 \\\"pilot selection bias\\\"——pilot repos 被挑选为 CodeQL-friendly （high structural coverage），不代表真实分布。这个 audit 本身是重要的 methodological contribution，论证了 pilot evaluation 的 sampling bias 问题。\\n\"\n  }\n]",
      "numLines": 963,
      "startLine": 1,
      "totalLines": 963
    }
  },
  "sourceToolAssistantUUID": "dfb8bfff-dc7f-4dc3-b974-42fb0d52dc95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T08:19:12.986Z_

<details><summary>↩ Tool result · `toolu_017y4vVS4NnTPYRWnHfS4vp8`</summary>

```text
1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3)
8	
9	1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported "harm" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).
10	
11	2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.
12	
13	3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).
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
62	| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |
63	| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |
64	| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |
65	| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |
66	| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |
67	| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |
68	| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |
69	| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |
70	| "Complementary signal" overstatement | Temper: "conditionally beneficial" not "always complementary" | Writing discipline |
71	| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |
72	
73	## Evidence Status
74	
75	### Confirmed findings (basis for claims):
76	- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact
77	- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction
78	- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)
79	- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only
80	- plan_006: CodeQL scalability confirmed at 123-repo scale
81	
82	### In progress:
83	- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)
84	- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)
85	- m1_reextract_v2: expanded extraction for higher coverage
86	
87	### Planned (priority order):
88	- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
89	- plan_014: Temperature ablation (Dream reviewer concern)
90	- plan_004: RepoBench-R second benchmark
91	- plan_015: Dynamic mining baseline
92	- plan_007/008/009: Additional ablations
93	
94	## Contingency (if full M2 results weaken claims)
95	
96	### All 18 runs confirm pilot pattern: Best case
97	- Full statistical power, paper as framed above
98	- Target: EMNLP Main
99	
100	### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
101	- Drop Claim 2 to analysis observation
102	- Paper becomes: "True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions"
103	- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main
104	
105	### Embedding mining also loses advantage at full scale: Major reassessment needed
106	- Recheck data pipeline for bugs (full-scale data may have distribution differences)
107	- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
108	- Discuss with user before committing direction
109	
110	## Deprecated Claims (with reason)
111	
112	- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12405788-5a91-4b9f-8d9b-2ecf1e6819d0",
  "isSidechain": false,
  "promptId": "f67db5d7-4662-48a7-ba27-d130d41b7555",
  "type": "user",
  "uuid": "36f2585c-e215-49f2-826c-f64cf88f4807",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper_framing.md",
      "content": "# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \"harm\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).\n\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\n\n- **Headline result template**: \"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\"\n\n## Core Insight\n\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\"\n- Backup: \"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\n- m1_reextract_v2: expanded extraction for higher coverage\n\n### Planned (priority order):\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark\n- plan_015: Dynamic mining baseline\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n",
      "numLines": 113,
      "startLine": 1,
      "totalLines": 113
    }
  },
  "sourceToolAssistantUUID": "12405788-5a91-4b9f-8d9b-2ecf1e6819d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T075732 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-contex…",
  "leafUuid": "1d750658-a06b-45ee-acf2-bcbdcb8d367c",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate negative result paper on hard negative mining",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599"
}
```

---

### Assistant

_source line 14 · 2026-05-14T08:19:25.344Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the data and framing. This is a "worst" tier paper — all original claims failed. The paper needs to be reframed as a negative result paper: "A Cautionary Tale: Scale, Seeds, and the Fragility of Hard Negative Mining for Code Retrieval."

Let me now write the complete LaTeX paper. I need to cover all experiments from the JSON data:

1. M2 Full Qwen — 9 seeds × 3 strategies (Table 2)


2. M2 Full StarCoder — 9 seeds × 3 strategies (Table 3)
3. M3a SWE-bench Lite End-to-End (Table 5)
4. M3b RepoBench-R Cross-File Retrieval (Table 6)
5. Embedding vs Random Deep Stratified Analysis (Table 7)
6. Hop-Distance Call-Graph Bounding Ablation (Table 8)
7. Training Data Size Scaling Ablation (Table 9)
8. Fusion Head Architecture Ablation (Table 10)
9. Dataflow-Distance Weighted vs Binary Negatives
10. Failure Analysis: 50 SweRank/BM25 Failures (Table 11)
11. Qualitative Examples
12. Temperature Ablation (Table 12)
13. Dynamic Embedding Mining vs Static (Table 13)
14. Bootstrap CI for SWE-bench (Table 14)
15. Inference-Time Graph Method Discussion (Table 15)
16. Data Pipeline Distribution Audit (Table A1)

Now I'm ready to write the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36f2585c-e215-49f2-826c-f64cf88f4807",
  "isSidechain": false,
  "requestId": "req_011Cb28hua2UNBUBgLFDwntw",
  "type": "assistant",
  "uuid": "c52c90d5-6a59-4588-b8c3-ff03224e90a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vgq8Zi3jbVP8U3VDZXsQX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18611,
      "cache_read_input_tokens": 23157,
      "output_tokens": 532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18611,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 532,
          "cache_read_input_tokens": 23157,
          "cache_creation_input_tokens": 18611,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18611
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

_source line 15 · 2026-05-14T08:19:25.348Z_

Now I'll write the full LaTeX paper as a negative result paper, covering all experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c52c90d5-6a59-4588-b8c3-ff03224e90a6",
  "isSidechain": false,
  "requestId": "req_011Cb28hua2UNBUBgLFDwntw",
  "type": "assistant",
  "uuid": "a382ed7d-55ba-46a8-8a47-eb987943db4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vgq8Zi3jbVP8U3VDZXsQX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18611,
      "cache_read_input_tokens": 23157,
      "output_tokens": 532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18611,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 532,
          "cache_read_input_tokens": 23157,
          "cache_creation_input_tokens": 18611,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18611
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

_source line 16 · 2026-05-14T08:19:27.520Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018ZSN3Sw6PEQeB64VPZWfm8`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a382ed7d-55ba-46a8-8a47-eb987943db4c",
  "isSidechain": false,
  "requestId": "req_011Cb28hua2UNBUBgLFDwntw",
  "type": "assistant",
  "uuid": "1e456245-2590-4c84-a6a4-459d3c9c16e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vgq8Zi3jbVP8U3VDZXsQX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18611,
      "cache_read_input_tokens": 23157,
      "output_tokens": 532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18611,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 532,
          "cache_read_input_tokens": 23157,
          "cache_creation_input_tokens": 18611,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18611
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

_source line 17 · 2026-05-14T08:19:27.763Z_

<details><summary>↩ Tool result · `toolu_018ZSN3Sw6PEQeB64VPZWfm8`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e456245-2590-4c84-a6a4-459d3c9c16e2",
  "isSidechain": false,
  "promptId": "f67db5d7-4662-48a7-ba27-d130d41b7555",
  "type": "user",
  "uuid": "85e86508-b12d-4ad5-8a24-ab8210d52fb9",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "1e456245-2590-4c84-a6a4-459d3c9c16e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T08:22:35.207Z_

<details open><summary>🔧 Tool call — Write · `toolu_01TP7UARmA5VGV3VacttUfZx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{subcaption}\n\n\\title{A Cautionary Tale: Scale, Seeds, and the Fragility of\\\\Hard Negative Mining for Code Retrieval}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nHard negative mining is widely assumed to improve contrastive retrieval models, yet controlled studies for code retrieval remain scarce.\nWe present a systematic comparison of three negative sampling strategies---random, embedding-distance, and dataflow-aware---for training contrastive code retrievers on SWE-smith data, using two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B) across 54 full-scale training runs (9 seeds $\\times$ 3 strategies $\\times$ 2 encoders).\nOur pilot experiments ({\\raise.17ex\\hbox{$\\scriptstyle\\sim$}}2K instances, single seed) suggested that embedding-distance mining improves Recall@1 by +1.6--2.0pp over random baselines.\nHowever, these gains \\emph{do not replicate} at full scale (15K instances, 9 seeds): strategy-level deltas ($<$1pp) are dwarfed by cross-seed variance (std $\\approx$ 3pp), and no strategy achieves statistically significant improvement over random sampling on either retrieval benchmarks or downstream SWE-bench Lite evaluation (bootstrap $p \\geq 0.68$).\nWe trace the discrepancy to a data-size--benefit scaling law: embedding mining benefit decays at $-0.11$pp per 1K additional training instances, crossing zero near 5K.\nWe further show that structural (dataflow) negatives suffer from domain-dependent negative transfer and that fusion architectures incorporating structural features slightly degrade performance.\nOur findings contribute: (1) empirical evidence that pilot-scale conclusions about hard negative mining for code are unreliable, (2) a quantitative scaling law relating data size to mining benefit, and (3) open-source CodeQL-based infrastructure for computing inter-procedural dataflow connectivity across repositories.\n\\end{abstract}\n\n%% ============================================================\n%% 1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nContrastive learning has become the dominant paradigm for training dense code retrievers~\\cite{li2023swerank,yang2024swefixer}.\nA core design choice is how to select \\emph{negative examples}---code snippets the model should learn to distinguish from the relevant file.\nHard negative mining, which preferentially selects negatives that are difficult for the current model, is a standard technique in information retrieval and has been applied to code search with mixed results.\n\\citet{gao2024cocohanere} report that embedding-distance negatives \\emph{harm} code retrieval by $-27$pp R@1, but their study used BM25-proxy negatives mislabeled as embedding-distance, confounding the analysis.\n\nWe set out to answer three questions: (1) Does true embedding-distance mining help? (2) Do structure-grounded (dataflow) negatives provide additional benefit? (3) How do these effects interact with encoder architecture and data scale?\n\nOur pilot experiments on ${\\sim}$2K training instances from 8 repositories were encouraging: embedding mining yielded +2.0pp R@1 on Qwen2.5-Coder-3B and +1.6pp on StarCoder2-3B relative to random baselines. Dataflow-aware negatives provided conditional further gains on the saturated Qwen encoder.\nHowever, when we scaled to 15,133 instances from 123 repositories and repeated each configuration across 9 random seeds, \\textbf{all strategy-level effects vanished}.\nThe mean delta between embedding and random strategies was $-0.2$pp for Qwen (std across seeds: 3.1pp) and $-0.8$pp for StarCoder (std: 3.4pp).\nDownstream SWE-bench Lite evaluation confirmed the null result: resolve rates differed by $<$0.5pp across strategies (bootstrap $p = 0.78$).\n\nThis paper presents these negative results and analyzes \\emph{why} pilot-scale conclusions failed to generalize.\nOur contributions are:\n\n\\begin{enumerate}\n\\item \\textbf{Empirical evidence of pilot-scale unreliability.} We show that hard negative mining benefits for code retrieval are an artifact of small-scale evaluation, with embedding benefit decaying at $-0.11$pp per 1K additional training instances (\\S\\ref{sec:scaling}).\n\n\\item \\textbf{Comprehensive ablation.} We systematically vary temperature, hop distance, fusion architecture, dynamic vs.\\ static mining, and data composition, ruling out confounds and identifying the mechanism: at scale, random sampling provides sufficient negative difficulty, making curated mining redundant (\\S\\ref{sec:ablations}).\n\n\\item \\textbf{Open infrastructure.} Our CodeQL-based pipeline for inter-procedural dataflow analysis achieves 0\\% timeout rate across 123 repositories and is released as a general-purpose structural negative generator (\\S\\ref{sec:method}).\n\\end{enumerate}\n\n\n%% ============================================================\n%% 2  RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Hard negative mining for retrieval.}\nANCE~\\cite{xiong2021ance} demonstrated the value of periodically refreshed hard negatives for open-domain QA.\nCurriculum-based mining schedules negative difficulty during training.\nFor code, CoCoHaNeRe~\\cite{gao2024cocohanere} studied negative strategies but conflated BM25-proxy with true embedding-distance negatives.\n\n\\paragraph{Code retrieval.}\nSweRank~\\cite{li2023swerank} and SWE-Fixer~\\cite{yang2024swefixer} use contrastive learning for repo-level file retrieval.\nGraphCodeBERT~\\cite{guo2021graphcodebert} incorporates data flow edges as pre-training signal but not as negative selection criterion.\nRepoFusion~\\cite{shrivastava2023repofusion} fuses cross-file context for code completion.\n\n\\paragraph{Structure-guided code understanding.}\nLocAgent~\\cite{qin2024locagent} and CodexGraph~\\cite{liu2024codexgraph} use structural graphs at \\emph{inference time} for repository navigation.\nARISE~\\cite{wu2024arise} uses intra-procedural data flow for code repair but does not cross call boundaries.\nOur work differs by using inter-procedural dataflow at \\emph{training time} for negative selection---and by demonstrating that this approach does not improve retrieval.\n\n\n%% ============================================================\n%% 3  METHOD\n%% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task and Training Setup}\n\nGiven a bug report (issue text) as query $q$ and a repository with files $\\{f_1, \\ldots, f_N\\}$, the retriever must rank the gold file(s) $f^*$ above all others.\nWe train bi-encoder retrievers using InfoNCE loss with temperature $\\tau$:\n\\begin{equation}\n\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(q, f^+)/\\tau)}{\\exp(\\text{sim}(q, f^+)/\\tau) + \\sum_{j} \\exp(\\text{sim}(q, f^-_j)/\\tau)}\n\\end{equation}\nwhere $f^+$ is the gold file and $\\{f^-_j\\}$ are negatives selected by the strategy under study.\n\n\\paragraph{Encoders.}\nWe use two architecturally distinct code LLMs as bi-encoder backbones:\n(1) \\textbf{Qwen2.5-Coder-3B}, which exhibits representation saturation (pretrained $\\text{pos\\_sim} = 0.9855$, embedding negative margin $= 0.017$);\n(2) \\textbf{StarCoder2-3B}, with a healthier representation space ($\\text{pos\\_sim} = 0.7985$, margin $= 0.194$).\nBoth are fine-tuned with LoRA (rank 16).\n\n\\paragraph{Training data.}\nWe use SWE-smith instances. The pilot dataset comprises ${\\sim}$2K instances from 8 medium-sized repositories (mean 45 files/repo, structural data rate 0.58). The full-scale dataset comprises 15,133 instances from 123 repositories (mean 185 files/repo, structural data rate 0.34).\n\n\\subsection{Negative Mining Strategies}\n\n\\paragraph{Random.}\nSample negatives uniformly from the repository's non-gold files.\n\n\\paragraph{Embedding-distance.}\nRank non-gold files by cosine similarity to the query in the pretrained encoder's embedding space; select the top-$k$ nearest as hard negatives.\n\n\\paragraph{Dataflow-aware.}\nUsing inter-procedural dataflow analysis via CodeQL, we construct a call-graph--bounded connectivity map.\nFiles \\emph{not} reachable from any gold file within $h$ hops ($h=2$ by default) are considered structurally disconnected.\nAmong disconnected files, we select those with highest embedding similarity as negatives---combining structural irrelevance with surface-level confusability.\n\n\\subsection{CodeQL Pipeline}\n\nWe implement scope-bounded inter-procedural dataflow analysis using CodeQL.\nFor each repository, we extract call-graph edges and data-flow paths, then compute pairwise file connectivity within a hop budget.\nThe pipeline achieves 0\\% timeout rate and produces output for 123/131 attempted repositories.\n\n\n%% ============================================================\n%% 4  EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Full-Scale Multi-Seed Results}\n\\label{sec:fullscale}\n\nWe train 27 runs per encoder (9 seeds $\\times$ 3 strategies) at full scale (15K instances).\n\n\\paragraph{Qwen2.5-Coder-3B.}\nTable~\\ref{tab:qwen_full} reports R@1 for each seed--strategy combination.\nThe mean R@1 across seeds is $0.523 \\pm 0.031$ (random), $0.521 \\pm 0.035$ (embedding), and $0.515 \\pm 0.038$ (dataflow).\nThe embedding-vs-random delta is $-0.2$pp; the dataflow-vs-random delta is $-0.8$pp.\nNeither is significant given cross-seed standard deviation of 3.1pp.\nExamining per-seed winners, random wins in 4/9 seeds, embedding in 3/9, and dataflow in 2/9---consistent with chance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Qwen2.5-Coder-3B full-scale R@1 by strategy and seed. Mean$\\pm$std: random $0.523 \\pm 0.031$, embedding $0.521 \\pm 0.035$, dataflow $0.515 \\pm 0.038$.}\n\\label{tab:qwen_full}\n\\begin{tabular}{lccc}\n\\toprule\nSeed & Random & Embedding & Dataflow \\\\\n\\midrule\n42   & 0.553 & 0.547 & 0.538 \\\\\n123  & 0.528 & 0.534 & 0.521 \\\\\n456  & 0.512 & 0.498 & 0.503 \\\\\n789  & 0.541 & 0.543 & 0.530 \\\\\n1024 & 0.498 & 0.510 & 0.496 \\\\\n2048 & 0.519 & 0.522 & 0.512 \\\\\n3000 & 0.505 & 0.503 & 0.478 \\\\\n4096 & 0.530 & 0.517 & 0.525 \\\\\n5000 & 0.523 & 0.515 & 0.532 \\\\\n\\midrule\nMean & 0.523 & 0.521 & 0.515 \\\\\nStd  & 0.017 & 0.016 & 0.019 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{StarCoder2-3B.}\nTable~\\ref{tab:starcoder_full} shows analogous results.\nMean R@1: random $0.443 \\pm 0.028$, embedding $0.435 \\pm 0.033$, dataflow $0.428 \\pm 0.040$.\nThe embedding-vs-random delta is $-0.8$pp and dataflow-vs-random is $-1.5$pp.\nCross-seed std (3.4pp) again dwarfs strategy-level differences.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{StarCoder2-3B full-scale R@1 by strategy and seed. Dataflow performs worst ($-1.5$pp vs.\\ random).}\n\\label{tab:starcoder_full}\n\\begin{tabular}{lccc}\n\\toprule\nSeed & Random & Embedding & Dataflow \\\\\n\\midrule\n42   & 0.454 & 0.448 & 0.442 \\\\\n123  & 0.440 & 0.425 & 0.418 \\\\\n456  & 0.462 & 0.456 & 0.440 \\\\\n789  & 0.435 & 0.430 & 0.412 \\\\\n1024 & 0.448 & 0.442 & 0.435 \\\\\n2048 & 0.425 & 0.418 & 0.398 \\\\\n3000 & 0.458 & 0.450 & 0.448 \\\\\n4096 & 0.430 & 0.422 & 0.425 \\\\\n5000 & 0.438 & 0.428 & 0.430 \\\\\n\\midrule\nMean & 0.443 & 0.435 & 0.428 \\\\\nStd  & 0.013 & 0.014 & 0.017 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Downstream Evaluation: SWE-bench Lite}\n\\label{sec:swebench}\n\nWe evaluate the best checkpoint from each strategy as a retriever in an end-to-end SWE-bench Lite pipeline (300 instances, 287 successfully evaluated) using a Qwen3.6-27B agent for patch generation.\n\nTable~\\ref{tab:swebench} shows resolve rates.\nThe best strategy (embedding, 19.0\\%) exceeds random (18.7\\%) by only +0.3pp.\nMcNemar's test yields $p = 0.89$; bootstrap 95\\% CIs for the embedding-vs-random delta span $[-3.8, +4.5]$pp (Table~\\ref{tab:bootstrap}).\nThe difference corresponds to a single additional resolved instance (55 vs.\\ 54 out of 287).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SWE-bench Lite resolve rates and retrieval R@1. No strategy achieves significant improvement.}\n\\label{tab:swebench}\n\\begin{tabular}{lcccc}\n\\toprule\nStrategy & Resolve & R@1 & Resolved & Total \\\\\n\\midrule\nRandom           & 0.187 & 0.42 & 54 & 287 \\\\\nEmbedding        & 0.190 & 0.43 & 55 & 287 \\\\\nDataflow         & 0.183 & 0.41 & 53 & 287 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap statistics (10,000 resamples) for SWE-bench Lite resolve rate comparisons.}\n\\label{tab:bootstrap}\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$pp & 95\\% CI & $p$ \\\\\n\\midrule\nembed vs.\\ random   & +0.3 & [$-$3.8, +4.5] & 0.78 \\\\\ndataflow vs.\\ random & $-$0.4 & [$-$4.8, +3.8] & 0.68 \\\\\ndataflow vs.\\ embed  & $-$0.7 & [$-$5.2, +3.5] & 0.55 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Domain Evaluation: RepoBench-R}\n\\label{sec:repobench}\n\nWe evaluate on RepoBench-R (cross-file code completion retrieval) using the Qwen encoder to test generalization beyond SWE-smith's bug-localization distribution (Table~\\ref{tab:repobench}).\n\nAll fine-tuned strategies improve over the pretrained baseline (+2--3pp R@1), confirming that contrastive fine-tuning itself is effective.\nHowever, dataflow negatives exhibit negative transfer ($-1.7$pp vs.\\ random), likely because SWE-smith's ``structurally disconnected $=$ irrelevant'' assumption does not hold for completion-oriented code.\nEmbedding negatives are also slightly below random ($-0.4$pp).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RepoBench-R results (Qwen encoder). Fine-tuning helps, but mining strategies do not outperform random.}\n\\label{tab:repobench}\n\\begin{tabular}{lcccc}\n\\toprule\nStrategy & R@1 & R@5 & R@10 & MRR \\\\\n\\midrule\nPretrained        & 0.285 & 0.520 & 0.680 & 0.401 \\\\\nRandom            & 0.312 & 0.580 & 0.730 & 0.438 \\\\\nEmbedding         & 0.308 & 0.570 & 0.720 & 0.432 \\\\\nDataflow          & 0.295 & 0.560 & 0.710 & 0.418 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Comparison with Inference-Time Graph Methods}\n\\label{sec:inference_graph}\n\nTable~\\ref{tab:inference_compare} contextualizes our results against inference-time structural methods.\nLocAgent (26.2\\% resolve rate on SWE-bench) substantially outperforms all our training-time strategies (${\\sim}$19\\%).\nThis suggests that structural information is valuable when applied adaptively at inference---navigating the call graph per query---rather than statically during training.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training-time vs.\\ inference-time structure utilization. Inference-time methods substantially outperform training-time mining. ($^*$Different benchmark, not directly comparable.)}\n\\label{tab:inference_compare}\n\\begin{tabular}{llcc}\n\\toprule\nMethod & Structure Use & Resolve & R@1 \\\\\n\\midrule\nOurs (random)   & training neg.  & 0.187 & 0.523 \\\\\nOurs (dataflow) & training neg.  & 0.183 & 0.515 \\\\\nLocAgent        & inference nav. & 0.262 & --- \\\\\nCodexGraph      & inference nav. & ---   & 0.48$^*$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%% ============================================================\n%% 5  ANALYSIS: WHY PILOT RESULTS DON'T SCALE\n%% ============================================================\n\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Data Size Scaling Law}\n\\label{sec:scaling}\n\nThe key to understanding the pilot-to-full-scale discrepancy is a data-size--benefit interaction.\nTable~\\ref{tab:scaling} reports R@1 for sub-sampled training sets of 1K, 3K, 5K, and the full 15K instances.\n\nAt 1K instances (approximating pilot scale), embedding mining yields +1.3pp over random, replicating the pilot finding and confirming that the pilot was not a bug.\nThe benefit decays monotonically with a slope of $-0.11$pp per 1K additional instances, crossing zero between 3K and 5K.\nAt 15K, the delta inverts to $-0.2$pp.\n\nThe mechanism is straightforward: at small scale, the random negative pool contains few truly hard negatives; embedding mining provides a necessary difficulty gradient.\nAs the pool grows, random sampling increasingly hits moderately hard negatives by chance, eroding the marginal value of curated mining.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Data size $\\times$ strategy interaction (Qwen). Embedding benefit decays at $-0.11$pp/1K instances.}\n\\label{tab:scaling}\n\\begin{tabular}{lcccc}\n\\toprule\nSize & Random & Embed & Dataflow & $\\Delta_\\text{embed}$ \\\\\n\\midrule\n1K         & 0.505 & 0.518 & 0.512 & +1.3 \\\\\n3K         & 0.515 & 0.520 & 0.513 & +0.5 \\\\\n5K         & 0.520 & 0.521 & 0.516 & +0.1 \\\\\n15K (full) & 0.523 & 0.521 & 0.515 & $-$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Stratified Analysis of Embedding Benefit}\n\\label{sec:stratified}\n\nTo understand \\emph{where} embedding mining helps or hurts, we stratify by repository size and negative difficulty quartile (Table~\\ref{tab:stratified}).\n\nEmbedding mining is harmful for small repositories ($-2.0$pp), where the file pool (${\\sim}$10--50 files) is so small that nearest-neighbor negatives are often near-duplicates of gold files, creating false hard negatives.\nIt provides a slight advantage for medium repositories (+1.0pp) but no benefit for large/xlarge repositories, where random sampling already provides sufficient difficulty.\n\nStratifying by negative difficulty quartile reveals a complementary pattern: embedding mining helps in the easiest quartile (+0.5pp) but hurts in the hardest ($-2.1$pp), where overly difficult negatives cause gradient conflicts.\n\nThe pilot dataset over-represented medium-sized repositories (the ``sweet spot''), explaining the apparent benefit.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Embedding benefit by repository size tier. Pilot data over-represented medium repos.}\n\\label{tab:stratified}\n\\begin{tabular}{lrrrr}\n\\toprule\nRepo Tier & $n$ & Rand & Embed & $\\Delta$pp \\\\\n\\midrule\nSmall ($<$50)    & 500   & 0.610 & 0.590 & $-$2.0 \\\\\nMedium (50--200) & 4,096 & 0.540 & 0.550 & +1.0 \\\\\nLarge (200--500) & 13,628 & 0.510 & 0.500 & $-$1.0 \\\\\nXLarge (500+)    & 25,949 & 0.480 & 0.480 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Data Pipeline Audit}\n\\label{sec:audit}\n\nTo rule out engineering errors, we audited the full-scale data pipeline against the pilot (Table~\\ref{tab:audit}).\nNo bugs were found, but significant distributional shift was confirmed:\nthe full-scale data draws from 123 repositories (vs.\\ 8 in pilot), with large/xlarge repos comprising 56\\% (vs.\\ 30\\%), mean files per repo of 185 (vs.\\ 45), and structural data rate of 0.34 (vs.\\ 0.58).\nA KS test on negative difficulty distributions rejects equivalence ($p = 0.003$).\n\nThis shift is not a bug but a consequence of realistic scaling---the pilot's repository selection was biased toward CodeQL-friendly, medium-sized repos with high structural coverage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pilot vs.\\ full-scale data distribution. Shift is systematic but not a pipeline bug.}\n\\label{tab:audit}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Pilot & Full & $p$ \\\\\n\\midrule\nInstances       & ${\\sim}$2,000 & 15,133 & --- \\\\\nRepositories    & 8         & 123   & --- \\\\\nStructural rate & 0.58      & 0.34  & $<$0.001 \\\\\nFiles/repo      & 45        & 185   & $<$0.001 \\\\\nEmbed margin    & 0.025     & 0.017 & 0.003 \\\\\n\\% large repos  & 0.30      & 0.56  & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Failure Taxonomy}\n\\label{sec:failure}\n\nWe manually analyzed 50 instances where both SweRank and BM25 fail to retrieve the gold file, asking whether dataflow signals could theoretically help (Table~\\ref{tab:failure}).\n\nOf 50 failures, only 6 (12\\%) involve cross-file dependencies where dataflow information could plausibly assist.\nOf these, dataflow-trained models actually helped in only 2 cases (4\\%) while actively hurting in 3 (6\\%)---the structural proximity signal elevated structurally related but incorrect files above the gold file.\nThe dominant failure modes (naming ambiguity, scattered changes, test file confusion) are orthogonal to structural connectivity.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Failure category analysis (50 SweRank/BM25 failures). Dataflow's theoretical coverage (12\\%) and actual help rate (4\\%) are both low.}\n\\label{tab:failure}\n\\begin{tabular}{lcccc}\n\\toprule\nCategory & $n$ & Could Help & Helped & Hurt \\\\\n\\midrule\nCross-file dep.     & 18 & 4 & 1 & 1 \\\\\nNaming ambiguity    & 12 & 0 & 0 & 1 \\\\\nScattered changes   &  9 & 2 & 1 & 1 \\\\\nTest confusion      &  7 & 0 & 0 & 0 \\\\\nOther               &  4 & 0 & 0 & 0 \\\\\n\\midrule\nTotal               & 50 & 6 & 2 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%% ============================================================\n%% 6  ABLATIONS\n%% ============================================================\n\\section{Ablations}\n\\label{sec:ablations}\n\n\\subsection{Temperature}\n\nWe test whether the null result is regime-specific by varying $\\tau \\in \\{0.05, 0.1, 0.2\\}$ (Table~\\ref{tab:temperature}).\nRandom is the best or tied-best strategy at all temperatures.\nAt $\\tau = 0.05$, all strategies degrade (the loss becomes hypersensitive to the already-small margins in Qwen's saturated space), with dataflow suffering most ($-2.3$pp vs.\\ $\\tau = 0.1$).\nNo temperature makes embedding benefit significant.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temperature $\\times$ strategy interaction (Qwen, mean of 3 seeds). Random is best at every $\\tau$.}\n\\label{tab:temperature}\n\\begin{tabular}{lcccc}\n\\toprule\n$\\tau$ & Random & Embed & Dataflow & Best \\\\\n\\midrule\n0.05 & 0.498 & 0.485 & 0.475 & random \\\\\n0.10 & 0.523 & 0.521 & 0.515 & random \\\\\n0.20 & 0.510 & 0.508 & 0.502 & random \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Hop-Distance for Dataflow Negatives}\n\nWe vary the call-graph hop budget $h \\in \\{1, 2, 3\\}$ for defining structural disconnection (Table~\\ref{tab:hops}).\nAll hop settings underperform random ($-0.8$ to $-1.3$pp).\nAt $h=1$, only 12\\% of file pairs are connected, creating many false hard negatives.\nAt $h=3$, 58\\% are connected, leaving a small disconnected pool with trivially easy negatives.\nThe intermediate $h=2$ (our default) is the best among dataflow variants but still inferior to random.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Hop-distance ablation (Qwen, seed 42). No hop setting matches random.}\n\\label{tab:hops}\n\\begin{tabular}{lcccc}\n\\toprule\nHops & Connected\\% & Margin & R@1 & vs.\\ Random \\\\\n\\midrule\n1      & 0.12 & 0.035 & 0.513 & $-$1.0 \\\\\n2      & 0.34 & 0.029 & 0.515 & $-$0.8 \\\\\n3      & 0.58 & 0.022 & 0.510 & $-$1.3 \\\\\nRandom & ---  & ---   & 0.523 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Fusion Head Architecture}\n\nTo test whether structural features help through a different mechanism than negative mining, we compare embedding-only, structural-features-only, and combined fusion heads (Table~\\ref{tab:fusion}).\n\nStructural features alone (binary connectivity, dataflow distance, call-graph hops) achieve only R@1 = 0.385, as 66\\% of instances lack structural data.\nThe combined fusion head slightly \\emph{degrades} performance ($-0.4$pp vs.\\ embedding-only), as noisy structural features interfere with the embedding signal under LoRA's low-rank constraint.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fusion head ablation (Qwen, seed 42). Structural features add noise, not signal.}\n\\label{tab:fusion}\n\\begin{tabular}{lccc}\n\\toprule\nHead Type & R@1 & R@5 & Val Loss \\\\\n\\midrule\nEmbedding only    & 0.523 & 0.955 & 0.486 \\\\\nStructural only   & 0.385 & 0.780 & 0.812 \\\\\nCombined          & 0.519 & 0.950 & 0.495 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Dynamic vs.\\ Static Mining}\n\nWe test whether mining negatives from a stale pretrained model (static) explains the null result by re-mining after each epoch (dynamic).\nTable~\\ref{tab:dynamic} shows dynamic mining does not help ($-0.3$pp vs.\\ static, $-0.5$pp vs.\\ random).\nRe-mining with a partially fine-tuned model introduces curriculum shifts and LoRA artifacts without improving negative quality.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Static vs.\\ dynamic embedding mining (Qwen, seed 42). Dynamic mining slightly degrades performance.}\n\\label{tab:dynamic}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Ep.1 & Ep.2 & Ep.3 & Best \\\\\n\\midrule\nStatic  & 0.540 & 0.530 & 0.512 & 0.540 \\\\\nDynamic & 0.540 & 0.525 & 0.505 & 0.540 \\\\\nRandom  & 0.535 & 0.528 & 0.510 & 0.535 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Dataflow Distance Weighting}\n\nInstead of binary connected/disconnected classification, we weight negative selection by continuous dataflow distance.\nThis yields R@1 = 0.517 (+0.2pp over binary, $-0.6$pp vs.\\ random).\nRefining the granularity of an ineffective signal does not rescue it.\n\n%% ============================================================\n%% 7  DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why do pilot results mislead?}\nOur scaling analysis (\\S\\ref{sec:scaling}) identifies two interacting factors:\n(1) \\emph{Data composition bias}: pilot repos were selected for CodeQL compatibility, over-representing medium-sized repos where embedding mining's sweet spot lies (\\S\\ref{sec:stratified}).\n(2) \\emph{Scale-dependent difficulty}: at small scale, random negative pools are too easy; curated mining fills a genuine gap.\nAs data grows, random sampling naturally encounters harder negatives, making curated selection redundant.\n\n\\paragraph{Structural information: training vs.\\ inference.}\nOur negative results for training-time structural mining contrast sharply with the success of inference-time graph methods (LocAgent: 26.2\\% resolve rate vs.\\ our 18.7\\%).\nThe key difference is \\emph{adaptivity}: inference-time methods select structural information conditioned on the specific query, while training-time mining applies a fixed structural criterion across all queries.\nThis suggests that structural signal is query-dependent---a file's structural relevance varies by bug type---and cannot be captured by a static negative selection policy.\n\n\\paragraph{Implications for practitioners.}\nOur findings suggest that for code retrieval with $>$5K training instances, investing in hard negative mining (embedding or structural) does not improve over random sampling.\nEffort is better spent on data scaling and inference-time retrieval augmentation.\nFor small-scale settings ($<$3K instances), embedding mining remains beneficial (+0.5--1.3pp).\n\n\\paragraph{Limitations.}\nOur study uses two 3B-parameter encoders with LoRA; larger encoders or full fine-tuning may behave differently.\nThe structural analysis is limited to CodeQL-supported languages (primarily Python).\nSWE-bench Lite's 300 instances provide limited statistical power for downstream evaluation (detectable effect size $>$5pp at $\\alpha = 0.05$).\n\n\n%% ============================================================\n%% 8  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe presented a large-scale systematic study of hard negative mining strategies for contrastive code retrieval, spanning 54 training runs across two encoders, three strategies, and nine seeds.\nOur initially promising pilot results---embedding mining improves R@1 by +1.6--2.0pp---failed to replicate at full scale, where strategy-level differences were dwarfed by seed variance and no strategy achieved statistically significant improvement over random sampling.\n\nWe traced this failure to a data-size--benefit scaling law ($-0.11$pp per 1K instances) and pilot data composition bias.\nOur ablations ruled out temperature regime, mining staleness, hop distance, and fusion architecture as confounds.\nFailure analysis showed that structural (dataflow) signals have narrow applicability (4\\% actual help rate) and can cause negative transfer on out-of-distribution benchmarks.\n\nThese results carry a methodological warning: single-seed, small-scale evaluations of hard negative mining can produce convincingly positive but ultimately unreliable conclusions.\nMulti-seed, multi-scale evaluation should be standard practice before concluding that a mining strategy provides genuine benefit.\n\nWe release our CodeQL-based dataflow analysis pipeline as open-source infrastructure for future research on structural code understanding.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\n\\section{Full Data Distribution Audit}\n\\label{app:audit}\n\nTable~\\ref{tab:audit} in the main text summarizes the pilot-vs-full distributional comparison.\nThe pilot dataset was drawn from 8 repositories selected for high CodeQL coverage, resulting in a structural data rate of 0.58 (fraction of instances with non-trivial dataflow information).\nAt full scale, coverage drops to 0.34 as larger repositories with sparser structural annotations dominate.\nThis shift is confirmed by a KS test on negative difficulty distributions ($p = 0.003$).\nNo data pipeline bugs were identified: repo overlap between pilot and full-scale is 85\\%, and the shift arises naturally from including repositories spanning the full size distribution.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85e86508-b12d-4ad5-8a24-ab8210d52fb9",
  "isSidechain": false,
  "requestId": "req_011Cb28izUj8SCqaBSQjLtah",
  "type": "assistant",
  "uuid": "f210797d-4fcd-48ce-91d2-f7cf02210fc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FAGoRnnE7YSGcZhXM8FTkV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 548,
      "cache_read_input_tokens": 41768,
      "output_tokens": 9520,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9520,
          "cache_read_input_tokens": 41768,
          "cache_creation_input_tokens": 548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 548
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

_source line 19 · 2026-05-14T08:22:35.232Z_

<details><summary>↩ Tool result · `toolu_01TP7UARmA5VGV3VacttUfZx`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f210797d-4fcd-48ce-91d2-f7cf02210fc0",
  "isSidechain": false,
  "promptId": "f67db5d7-4662-48a7-ba27-d130d41b7555",
  "type": "user",
  "uuid": "e1005da3-336b-4422-bc0a-beeafe8ec163",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{subcaption}\n\n\\title{A Cautionary Tale: Scale, Seeds, and the Fragility of\\\\Hard Negative Mining for Code Retrieval}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nHard negative mining is widely assumed to improve contrastive retrieval models, yet controlled studies for code retrieval remain scarce.\nWe present a systematic comparison of three negative sampling strategies---random, embedding-distance, and dataflow-aware---for training contrastive code retrievers on SWE-smith data, using two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B) across 54 full-scale training runs (9 seeds $\\times$ 3 strategies $\\times$ 2 encoders).\nOur pilot experiments ({\\raise.17ex\\hbox{$\\scriptstyle\\sim$}}2K instances, single seed) suggested that embedding-distance mining improves Recall@1 by +1.6--2.0pp over random baselines.\nHowever, these gains \\emph{do not replicate} at full scale (15K instances, 9 seeds): strategy-level deltas ($<$1pp) are dwarfed by cross-seed variance (std $\\approx$ 3pp), and no strategy achieves statistically significant improvement over random sampling on either retrieval benchmarks or downstream SWE-bench Lite evaluation (bootstrap $p \\geq 0.68$).\nWe trace the discrepancy to a data-size--benefit scaling law: embedding mining benefit decays at $-0.11$pp per 1K additional training instances, crossing zero near 5K.\nWe further show that structural (dataflow) negatives suffer from domain-dependent negative transfer and that fusion architectures incorporating structural features slightly degrade performance.\nOur findings contribute: (1) empirical evidence that pilot-scale conclusions about hard negative mining for code are unreliable, (2) a quantitative scaling law relating data size to mining benefit, and (3) open-source CodeQL-based infrastructure for computing inter-procedural dataflow connectivity across repositories.\n\\end{abstract}\n\n%% ============================================================\n%% 1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nContrastive learning has become the dominant paradigm for training dense code retrievers~\\cite{li2023swerank,yang2024swefixer}.\nA core design choice is how to select \\emph{negative examples}---code snippets the model should learn to distinguish from the relevant file.\nHard negative mining, which preferentially selects negatives that are difficult for the current model, is a standard technique in information retrieval and has been applied to code search with mixed results.\n\\citet{gao2024cocohanere} report that embedding-distance negatives \\emph{harm} code retrieval by $-27$pp R@1, but their study used BM25-proxy negatives mislabeled as embedding-distance, confounding the analysis.\n\nWe set out to answer three questions: (1) Does true embedding-distance mining help? (2) Do structure-grounded (dataflow) negatives provide additional benefit? (3) How do these effects interact with encoder architecture and data scale?\n\nOur pilot experiments on ${\\sim}$2K training instances from 8 repositories were encouraging: embedding mining yielded +2.0pp R@1 on Qwen2.5-Coder-3B and +1.6pp on StarCoder2-3B relative to random baselines. Dataflow-aware negatives provided conditional further gains on the saturated Qwen encoder.\nHowever, when we scaled to 15,133 instances from 123 repositories and repeated each configuration across 9 random seeds, \\textbf{all strategy-level effects vanished}.\nThe mean delta between embedding and random strategies was $-0.2$pp for Qwen (std across seeds: 3.1pp) and $-0.8$pp for StarCoder (std: 3.4pp).\nDownstream SWE-bench Lite evaluation confirmed the null result: resolve rates differed by $<$0.5pp across strategies (bootstrap $p = 0.78$).\n\nThis paper presents these negative results and analyzes \\emph{why} pilot-scale conclusions failed to generalize.\nOur contributions are:\n\n\\begin{enumerate}\n\\item \\textbf{Empirical evidence of pilot-scale unreliability.} We show that hard negative mining benefits for code retrieval are an artifact of small-scale evaluation, with embedding benefit decaying at $-0.11$pp per 1K additional training instances (\\S\\ref{sec:scaling}).\n\n\\item \\textbf{Comprehensive ablation.} We systematically vary temperature, hop distance, fusion architecture, dynamic vs.\\ static mining, and data composition, ruling out confounds and identifying the mechanism: at scale, random sampling provides sufficient negative difficulty, making curated mining redundant (\\S\\ref{sec:ablations}).\n\n\\item \\textbf{Open infrastructure.} Our CodeQL-based pipeline for inter-procedural dataflow analysis achieves 0\\% timeout rate across 123 repositories and is released as a general-purpose structural negative generator (\\S\\ref{sec:method}).\n\\end{enumerate}\n\n\n%% ============================================================\n%% 2  RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Hard negative mining for retrieval.}\nANCE~\\cite{xiong2021ance} demonstrated the value of periodically refreshed hard negatives for open-domain QA.\nCurriculum-based mining schedules negative difficulty during training.\nFor code, CoCoHaNeRe~\\cite{gao2024cocohanere} studied negative strategies but conflated BM25-proxy with true embedding-distance negatives.\n\n\\paragraph{Code retrieval.}\nSweRank~\\cite{li2023swerank} and SWE-Fixer~\\cite{yang2024swefixer} use contrastive learning for repo-level file retrieval.\nGraphCodeBERT~\\cite{guo2021graphcodebert} incorporates data flow edges as pre-training signal but not as negative selection criterion.\nRepoFusion~\\cite{shrivastava2023repofusion} fuses cross-file context for code completion.\n\n\\paragraph{Structure-guided code understanding.}\nLocAgent~\\cite{qin2024locagent} and CodexGraph~\\cite{liu2024codexgraph} use structural graphs at \\emph{inference time} for repository navigation.\nARISE~\\cite{wu2024arise} uses intra-procedural data flow for code repair but does not cross call boundaries.\nOur work differs by using inter-procedural dataflow at \\emph{training time} for negative selection---and by demonstrating that this approach does not improve retrieval.\n\n\n%% ============================================================\n%% 3  METHOD\n%% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task and Training Setup}\n\nGiven a bug report (issue text) as query $q$ and a repository with files $\\{f_1, \\ldots, f_N\\}$, the retriever must rank the gold file(s) $f^*$ above all others.\nWe train bi-encoder retrievers using InfoNCE loss with temperature $\\tau$:\n\\begin{equation}\n\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(q, f^+)/\\tau)}{\\exp(\\text{sim}(q, f^+)/\\tau) + \\sum_{j} \\exp(\\text{sim}(q, f^-_j)/\\tau)}\n\\end{equation}\nwhere $f^+$ is the gold file and $\\{f^-_j\\}$ are negatives selected by the strategy under study.\n\n\\paragraph{Encoders.}\nWe use two architecturally distinct code LLMs as bi-encoder backbones:\n(1) \\textbf{Qwen2.5-Coder-3B}, which exhibits representation saturation (pretrained $\\text{pos\\_sim} = 0.9855$, embedding negative margin $= 0.017$);\n(2) \\textbf{StarCoder2-3B}, with a healthier representation space ($\\text{pos\\_sim} = 0.7985$, margin $= 0.194$).\nBoth are fine-tuned with LoRA (rank 16).\n\n\\paragraph{Training data.}\nWe use SWE-smith instances. The pilot dataset comprises ${\\sim}$2K instances from 8 medium-sized repositories (mean 45 files/repo, structural data rate 0.58). The full-scale dataset comprises 15,133 instances from 123 repositories (mean 185 files/repo, structural data rate 0.34).\n\n\\subsection{Negative Mining Strategies}\n\n\\paragraph{Random.}\nSample negatives uniformly from the repository's non-gold files.\n\n\\paragraph{Embedding-distance.}\nRank non-gold files by cosine similarity to the query in the pretrained encoder's embedding space; select the top-$k$ nearest as hard negatives.\n\n\\paragraph{Dataflow-aware.}\nUsing inter-procedural dataflow analysis via CodeQL, we construct a call-graph--bounded connectivity map.\nFiles \\emph{not} reachable from any gold file within $h$ hops ($h=2$ by default) are considered structurally disconnected.\nAmong disconnected files, we select those with highest embedding similarity as negatives---combining structural irrelevance with surface-level confusability.\n\n\\subsection{CodeQL Pipeline}\n\nWe implement scope-bounded inter-procedural dataflow analysis using CodeQL.\nFor each repository, we extract call-graph edges and data-flow paths, then compute pairwise file connectivity within a hop budget.\nThe pipeline achieves 0\\% timeout rate and produces output for 123/131 attempted repositories.\n\n\n%% ============================================================\n%% 4  EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Full-Scale Multi-Seed Results}\n\\label{sec:fullscale}\n\nWe train 27 runs per encoder (9 seeds $\\times$ 3 strategies) at full scale (15K instances).\n\n\\paragraph{Qwen2.5-Coder-3B.}\nTable~\\ref{tab:qwen_full} reports R@1 for each seed--strategy combination.\nThe mean R@1 across seeds is $0.523 \\pm 0.031$ (random), $0.521 \\pm 0.035$ (embedding), and $0.515 \\pm 0.038$ (dataflow).\nThe embedding-vs-random delta is $-0.2$pp; the dataflow-vs-random delta is $-0.8$pp.\nNeither is significant given cross-seed standard deviation of 3.1pp.\nExamining per-seed winners, random wins in 4/9 seeds, embedding in 3/9, and dataflow in 2/9---consistent with chance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Qwen2.5-Coder-3B full-scale R@1 by strategy and seed. Mean$\\pm$std: random $0.523 \\pm 0.031$, embedding $0.521 \\pm 0.035$, dataflow $0.515 \\pm 0.038$.}\n\\label{tab:qwen_full}\n\\begin{tabular}{lccc}\n\\toprule\nSeed & Random & Embedding & Dataflow \\\\\n\\midrule\n42   & 0.553 & 0.547 & 0.538 \\\\\n123  & 0.528 & 0.534 & 0.521 \\\\\n456  & 0.512 & 0.498 & 0.503 \\\\\n789  & 0.541 & 0.543 & 0.530 \\\\\n1024 & 0.498 & 0.510 & 0.496 \\\\\n2048 & 0.519 & 0.522 & 0.512 \\\\\n3000 & 0.505 & 0.503 & 0.478 \\\\\n4096 & 0.530 & 0.517 & 0.525 \\\\\n5000 & 0.523 & 0.515 & 0.532 \\\\\n\\midrule\nMean & 0.523 & 0.521 & 0.515 \\\\\nStd  & 0.017 & 0.016 & 0.019 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{StarCoder2-3B.}\nTable~\\ref{tab:starcoder_full} shows analogous results.\nMean R@1: random $0.443 \\pm 0.028$, embedding $0.435 \\pm 0.033$, dataflow $0.428 \\pm 0.040$.\nThe embedding-vs-random delta is $-0.8$pp and dataflow-vs-random is $-1.5$pp.\nCross-seed std (3.4pp) again dwarfs strategy-level differences.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{StarCoder2-3B full-scale R@1 by strategy and seed. Dataflow performs worst ($-1.5$pp vs.\\ random).}\n\\label{tab:starcoder_full}\n\\begin{tabular}{lccc}\n\\toprule\nSeed & Random & Embedding & Dataflow \\\\\n\\midrule\n42   & 0.454 & 0.448 & 0.442 \\\\\n123  & 0.440 & 0.425 & 0.418 \\\\\n456  & 0.462 & 0.456 & 0.440 \\\\\n789  & 0.435 & 0.430 & 0.412 \\\\\n1024 & 0.448 & 0.442 & 0.435 \\\\\n2048 & 0.425 & 0.418 & 0.398 \\\\\n3000 & 0.458 & 0.450 & 0.448 \\\\\n4096 & 0.430 & 0.422 & 0.425 \\\\\n5000 & 0.438 & 0.428 & 0.430 \\\\\n\\midrule\nMean & 0.443 & 0.435 & 0.428 \\\\\nStd  & 0.013 & 0.014 & 0.017 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Downstream Evaluation: SWE-bench Lite}\n\\label{sec:swebench}\n\nWe evaluate the best checkpoint from each strategy as a retriever in an end-to-end SWE-bench Lite pipeline (300 instances, 287 successfully evaluated) using a Qwen3.6-27B agent for patch generation.\n\nTable~\\ref{tab:swebench} shows resolve rates.\nThe best strategy (embedding, 19.0\\%) exceeds random (18.7\\%) by only +0.3pp.\nMcNemar's test yields $p = 0.89$; bootstrap 95\\% CIs for the embedding-vs-random delta span $[-3.8, +4.5]$pp (Table~\\ref{tab:bootstrap}).\nThe difference corresponds to a single additional resolved instance (55 vs.\\ 54 out of 287).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SWE-bench Lite resolve rates and retrieval R@1. No strategy achieves significant improvement.}\n\\label{tab:swebench}\n\\begin{tabular}{lcccc}\n\\toprule\nStrategy & Resolve & R@1 & Resolved & Total \\\\\n\\midrule\nRandom           & 0.187 & 0.42 & 54 & 287 \\\\\nEmbedding        & 0.190 & 0.43 & 55 & 287 \\\\\nDataflow         & 0.183 & 0.41 & 53 & 287 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap statistics (10,000 resamples) for SWE-bench Lite resolve rate comparisons.}\n\\label{tab:bootstrap}\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$pp & 95\\% CI & $p$ \\\\\n\\midrule\nembed vs.\\ random   & +0.3 & [$-$3.8, +4.5] & 0.78 \\\\\ndataflow vs.\\ random & $-$0.4 & [$-$4.8, +3.8] & 0.68 \\\\\ndataflow vs.\\ embed  & $-$0.7 & [$-$5.2, +3.5] & 0.55 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Domain Evaluation: RepoBench-R}\n\\label{sec:repobench}\n\nWe evaluate on RepoBench-R (cross-file code completion retrieval) using the Qwen encoder to test generalization beyond SWE-smith's bug-localization distribution (Table~\\ref{tab:repobench}).\n\nAll fine-tuned strategies improve over the pretrained baseline (+2--3pp R@1), confirming that contrastive fine-tuning itself is effective.\nHowever, dataflow negatives exhibit negative transfer ($-1.7$pp vs.\\ random), likely because SWE-smith's ``structurally disconnected $=$ irrelevant'' assumption does not hold for completion-oriented code.\nEmbedding negatives are also slightly below random ($-0.4$pp).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RepoBench-R results (Qwen encoder). Fine-tuning helps, but mining strategies do not outperform random.}\n\\label{tab:repobench}\n\\begin{tabular}{lcccc}\n\\toprule\nStrategy & R@1 & R@5 & R@10 & MRR \\\\\n\\midrule\nPretrained        & 0.285 & 0.520 & 0.680 & 0.401 \\\\\nRandom            & 0.312 & 0.580 & 0.730 & 0.438 \\\\\nEmbedding         & 0.308 & 0.570 & 0.720 & 0.432 \\\\\nDataflow          & 0.295 & 0.560 & 0.710 & 0.418 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Comparison with Inference-Time Graph Methods}\n\\label{sec:inference_graph}\n\nTable~\\ref{tab:inference_compare} contextualizes our results against inference-time structural methods.\nLocAgent (26.2\\% resolve rate on SWE-bench) substantially outperforms all our training-time strategies (${\\sim}$19\\%).\nThis suggests that structural information is valuable when applied adaptively at inference---navigating the call graph per query---rather than statically during training.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training-time vs.\\ inference-time structure utilization. Inference-time methods substantially outperform training-time mining. ($^*$Different benchmark, not directly comparable.)}\n\\label{tab:inference_compare}\n\\begin{tabular}{llcc}\n\\toprule\nMethod & Structure Use & Resolve & R@1 \\\\\n\\midrule\nOurs (random)   & training neg.  & 0.187 & 0.523 \\\\\nOurs (dataflow) & training neg.  & 0.183 & 0.515 \\\\\nLocAgent        & inference nav. & 0.262 & --- \\\\\nCodexGraph      & inference nav. & ---   & 0.48$^*$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%% ============================================================\n%% 5  ANALYSIS: WHY PILOT RESULTS DON'T SCALE\n%% ============================================================\n\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Data Size Scaling Law}\n\\label{sec:scaling}\n\nThe key to understanding the pilot-to-full-scale discrepancy is a data-size--benefit interaction.\nTable~\\ref{tab:scaling} reports R@1 for sub-sampled training sets of 1K, 3K, 5K, and the full 15K instances.\n\nAt 1K instances (approximating pilot scale), embedding mining yields +1.3pp over random, replicating the pilot finding and confirming that the pilot was not a bug.\nThe benefit decays monotonically with a slope of $-0.11$pp per 1K additional instances, crossing zero between 3K and 5K.\nAt 15K, the delta inverts to $-0.2$pp.\n\nThe mechanism is straightforward: at small scale, the random negative pool contains few truly hard negatives; embedding mining provides a necessary difficulty gradient.\nAs the pool grows, random sampling increasingly hits moderately hard negatives by chance, eroding the marginal value of curated mining.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Data size $\\times$ strategy interaction (Qwen). Embedding benefit decays at $-0.11$pp/1K instances.}\n\\label{tab:scaling}\n\\begin{tabular}{lcccc}\n\\toprule\nSize & Random & Embed & Dataflow & $\\Delta_\\text{embed}$ \\\\\n\\midrule\n1K         & 0.505 & 0.518 & 0.512 & +1.3 \\\\\n3K         & 0.515 & 0.520 & 0.513 & +0.5 \\\\\n5K         & 0.520 & 0.521 & 0.516 & +0.1 \\\\\n15K (full) & 0.523 & 0.521 & 0.515 & $-$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Stratified Analysis of Embedding Benefit}\n\\label{sec:stratified}\n\nTo understand \\emph{where} embedding mining helps or hurts, we stratify by repository size and negative difficulty quartile (Table~\\ref{tab:stratified}).\n\nEmbedding mining is harmful for small repositories ($-2.0$pp), where the file pool (${\\sim}$10--50 files) is so small that nearest-neighbor negatives are often near-duplicates of gold files, creating false hard negatives.\nIt provides a slight advantage for medium repositories (+1.0pp) but no benefit for large/xlarge repositories, where random sampling already provides sufficient difficulty.\n\nStratifying by negative difficulty quartile reveals a complementary pattern: embedding mining helps in the easiest quartile (+0.5pp) but hurts in the hardest ($-2.1$pp), where overly difficult negatives cause gradient conflicts.\n\nThe pilot dataset over-represented medium-sized repositories (the ``sweet spot''), explaining the apparent benefit.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Embedding benefit by repository size tier. Pilot data over-represented medium repos.}\n\\label{tab:stratified}\n\\begin{tabular}{lrrrr}\n\\toprule\nRepo Tier & $n$ & Rand & Embed & $\\Delta$pp \\\\\n\\midrule\nSmall ($<$50)    & 500   & 0.610 & 0.590 & $-$2.0 \\\\\nMedium (50--200) & 4,096 & 0.540 & 0.550 & +1.0 \\\\\nLarge (200--500) & 13,628 & 0.510 & 0.500 & $-$1.0 \\\\\nXLarge (500+)    & 25,949 & 0.480 & 0.480 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Data Pipeline Audit}\n\\label{sec:audit}\n\nTo rule out engineering errors, we audited the full-scale data pipeline against the pilot (Table~\\ref{tab:audit}).\nNo bugs were found, but significant distributional shift was confirmed:\nthe full-scale data draws from 123 repositories (vs.\\ 8 in pilot), with large/xlarge repos comprising 56\\% (vs.\\ 30\\%), mean files per repo of 185 (vs.\\ 45), and structural data rate of 0.34 (vs.\\ 0.58).\nA KS test on negative difficulty distributions rejects equivalence ($p = 0.003$).\n\nThis shift is not a bug but a consequence of realistic scaling---the pilot's repository selection was biased toward CodeQL-friendly, medium-sized repos with high structural coverage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pilot vs.\\ full-scale data distribution. Shift is systematic but not a pipeline bug.}\n\\label{tab:audit}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Pilot & Full & $p$ \\\\\n\\midrule\nInstances       & ${\\sim}$2,000 & 15,133 & --- \\\\\nRepositories    & 8         & 123   & --- \\\\\nStructural rate & 0.58      & 0.34  & $<$0.001 \\\\\nFiles/repo      & 45        & 185   & $<$0.001 \\\\\nEmbed margin    & 0.025     & 0.017 & 0.003 \\\\\n\\% large repos  & 0.30      & 0.56  & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Failure Taxonomy}\n\\label{sec:failure}\n\nWe manually analyzed 50 instances where both SweRank and BM25 fail to retrieve the gold file, asking whether dataflow signals could theoretically help (Table~\\ref{tab:failure}).\n\nOf 50 failures, only 6 (12\\%) involve cross-file dependencies where dataflow information could plausibly assist.\nOf these, dataflow-trained models actually helped in only 2 cases (4\\%) while actively hurting in 3 (6\\%)---the structural proximity signal elevated structurally related but incorrect files above the gold file.\nThe dominant failure modes (naming ambiguity, scattered changes, test file confusion) are orthogonal to structural connectivity.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Failure category analysis (50 SweRank/BM25 failures). Dataflow's theoretical coverage (12\\%) and actual help rate (4\\%) are both low.}\n\\label{tab:failure}\n\\begin{tabular}{lcccc}\n\\toprule\nCategory & $n$ & Could Help & Helped & Hurt \\\\\n\\midrule\nCross-file dep.     & 18 & 4 & 1 & 1 \\\\\nNaming ambiguity    & 12 & 0 & 0 & 1 \\\\\nScattered changes   &  9 & 2 & 1 & 1 \\\\\nTest confusion      &  7 & 0 & 0 & 0 \\\\\nOther               &  4 & 0 & 0 & 0 \\\\\n\\midrule\nTotal               & 50 & 6 & 2 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%% ============================================================\n%% 6  ABLATIONS\n%% ============================================================\n\\section{Ablations}\n\\label{sec:ablations}\n\n\\subsection{Temperature}\n\nWe test whether the null result is regime-specific by varying $\\tau \\in \\{0.05, 0.1, 0.2\\}$ (Table~\\ref{tab:temperature}).\nRandom is the best or tied-best strategy at all temperatures.\nAt $\\tau = 0.05$, all strategies degrade (the loss becomes hypersensitive to the already-small margins in Qwen's saturated space), with dataflow suffering most ($-2.3$pp vs.\\ $\\tau = 0.1$).\nNo temperature makes embedding benefit significant.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temperature $\\times$ strategy interaction (Qwen, mean of 3 seeds). Random is best at every $\\tau$.}\n\\label{tab:temperature}\n\\begin{tabular}{lcccc}\n\\toprule\n$\\tau$ & Random & Embed & Dataflow & Best \\\\\n\\midrule\n0.05 & 0.498 & 0.485 & 0.475 & random \\\\\n0.10 & 0.523 & 0.521 & 0.515 & random \\\\\n0.20 & 0.510 & 0.508 & 0.502 & random \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Hop-Distance for Dataflow Negatives}\n\nWe vary the call-graph hop budget $h \\in \\{1, 2, 3\\}$ for defining structural disconnection (Table~\\ref{tab:hops}).\nAll hop settings underperform random ($-0.8$ to $-1.3$pp).\nAt $h=1$, only 12\\% of file pairs are connected, creating many false hard negatives.\nAt $h=3$, 58\\% are connected, leaving a small disconnected pool with trivially easy negatives.\nThe intermediate $h=2$ (our default) is the best among dataflow variants but still inferior to random.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Hop-distance ablation (Qwen, seed 42). No hop setting matches random.}\n\\label{tab:hops}\n\\begin{tabular}{lcccc}\n\\toprule\nHops & Connected\\% & Margin & R@1 & vs.\\ Random \\\\\n\\midrule\n1      & 0.12 & 0.035 & 0.513 & $-$1.0 \\\\\n2      & 0.34 & 0.029 & 0.515 & $-$0.8 \\\\\n3      & 0.58 & 0.022 & 0.510 & $-$1.3 \\\\\nRandom & ---  & ---   & 0.523 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Fusion Head Architecture}\n\nTo test whether structural features help through a different mechanism than negative mining, we compare embedding-only, structural-features-only, and combined fusion heads (Table~\\ref{tab:fusion}).\n\nStructural features alone (binary connectivity, dataflow distance, call-graph hops) achieve only R@1 = 0.385, as 66\\% of instances lack structural data.\nThe combined fusion head slightly \\emph{degrades} performance ($-0.4$pp vs.\\ embedding-only), as noisy structural features interfere with the embedding signal under LoRA's low-rank constraint.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fusion head ablation (Qwen, seed 42). Structural features add noise, not signal.}\n\\label{tab:fusion}\n\\begin{tabular}{lccc}\n\\toprule\nHead Type & R@1 & R@5 & Val Loss \\\\\n\\midrule\nEmbedding only    & 0.523 & 0.955 & 0.486 \\\\\nStructural only   & 0.385 & 0.780 & 0.812 \\\\\nCombined          & 0.519 & 0.950 & 0.495 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Dynamic vs.\\ Static Mining}\n\nWe test whether mining negatives from a stale pretrained model (static) explains the null result by re-mining after each epoch (dynamic).\nTable~\\ref{tab:dynamic} shows dynamic mining does not help ($-0.3$pp vs.\\ static, $-0.5$pp vs.\\ random).\nRe-mining with a partially fine-tuned model introduces curriculum shifts and LoRA artifacts without improving negative quality.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Static vs.\\ dynamic embedding mining (Qwen, seed 42). Dynamic mining slightly degrades performance.}\n\\label{tab:dynamic}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Ep.1 & Ep.2 & Ep.3 & Best \\\\\n\\midrule\nStatic  & 0.540 & 0.530 & 0.512 & 0.540 \\\\\nDynamic & 0.540 & 0.525 & 0.505 & 0.540 \\\\\nRandom  & 0.535 & 0.528 & 0.510 & 0.535 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Dataflow Distance Weighting}\n\nInstead of binary connected/disconnected classification, we weight negative selection by continuous dataflow distance.\nThis yields R@1 = 0.517 (+0.2pp over binary, $-0.6$pp vs.\\ random).\nRefining the granularity of an ineffective signal does not rescue it.\n\n%% ============================================================\n%% 7  DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why do pilot results mislead?}\nOur scaling analysis (\\S\\ref{sec:scaling}) identifies two interacting factors:\n(1) \\emph{Data composition bias}: pilot repos were selected for CodeQL compatibility, over-representing medium-sized repos where embedding mining's sweet spot lies (\\S\\ref{sec:stratified}).\n(2) \\emph{Scale-dependent difficulty}: at small scale, random negative pools are too easy; curated mining fills a genuine gap.\nAs data grows, random sampling naturally encounters harder negatives, making curated selection redundant.\n\n\\paragraph{Structural information: training vs.\\ inference.}\nOur negative results for training-time structural mining contrast sharply with the success of inference-time graph methods (LocAgent: 26.2\\% resolve rate vs.\\ our 18.7\\%).\nThe key difference is \\emph{adaptivity}: inference-time methods select structural information conditioned on the specific query, while training-time mining applies a fixed structural criterion across all queries.\nThis suggests that structural signal is query-dependent---a file's structural relevance varies by bug type---and cannot be captured by a static negative selection policy.\n\n\\paragraph{Implications for practitioners.}\nOur findings suggest that for code retrieval with $>$5K training instances, investing in hard negative mining (embedding or structural) does not improve over random sampling.\nEffort is better spent on data scaling and inference-time retrieval augmentation.\nFor small-scale settings ($<$3K instances), embedding mining remains beneficial (+0.5--1.3pp).\n\n\\paragraph{Limitations.}\nOur study uses two 3B-parameter encoders with LoRA; larger encoders or full fine-tuning may behave differently.\nThe structural analysis is limited to CodeQL-supported languages (primarily Python).\nSWE-bench Lite's 300 instances provide limited statistical power for downstream evaluation (detectable effect size $>$5pp at $\\alpha = 0.05$).\n\n\n%% ============================================================\n%% 8  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe presented a large-scale systematic study of hard negative mining strategies for contrastive code retrieval, spanning 54 training runs across two encoders, three strategies, and nine seeds.\nOur initially promising pilot results---embedding mining improves R@1 by +1.6--2.0pp---failed to replicate at full scale, where strategy-level differences were dwarfed by seed variance and no strategy achieved statistically significant improvement over random sampling.\n\nWe traced this failure to a data-size--benefit scaling law ($-0.11$pp per 1K instances) and pilot data composition bias.\nOur ablations ruled out temperature regime, mining staleness, hop distance, and fusion architecture as confounds.\nFailure analysis showed that structural (dataflow) signals have narrow applicability (4\\% actual help rate) and can cause negative transfer on out-of-distribution benchmarks.\n\nThese results carry a methodological warning: single-seed, small-scale evaluations of hard negative mining can produce convincingly positive but ultimately unreliable conclusions.\nMulti-seed, multi-scale evaluation should be standard practice before concluding that a mining strategy provides genuine benefit.\n\nWe release our CodeQL-based dataflow analysis pipeline as open-source infrastructure for future research on structural code understanding.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\n\\section{Full Data Distribution Audit}\n\\label{app:audit}\n\nTable~\\ref{tab:audit} in the main text summarizes the pilot-vs-full distributional comparison.\nThe pilot dataset was drawn from 8 repositories selected for high CodeQL coverage, resulting in a structural data rate of 0.58 (fraction of instances with non-trivial dataflow information).\nAt full scale, coverage drops to 0.34 as larger repositories with sparser structural annotations dominate.\nThis shift is confirmed by a KS test on negative difficulty distributions ($p = 0.003$).\nNo data pipeline bugs were identified: repo overlap between pilot and full-scale is 85\\%, and the shift arises naturally from including repositories spanning the full size distribution.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "f210797d-4fcd-48ce-91d2-f7cf02210fc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T075732 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-contex…",
  "leafUuid": "e1005da3-336b-4422-bc0a-beeafe8ec163",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate negative result paper on hard negative mining",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599"
}
```

---

### Assistant

_source line 22 · 2026-05-14T08:22:37.839Z_

Now compile the LaTeX.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1005da3-336b-4422-bc0a-beeafe8ec163",
  "isSidechain": false,
  "requestId": "req_011Cb28xpAkeGTgs65EEN6tj",
  "type": "assistant",
  "uuid": "0b49f6fd-ea60-4096-b521-f5f1ff91610c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mRySEvaXRh4MbpJuypRZy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9585,
      "cache_read_input_tokens": 42316,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 42316,
          "cache_creation_input_tokens": 9585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9585
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

_source line 23 · 2026-05-14T08:22:39.434Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RPMP6DmXhmhRdBGCeGfSW3`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b49f6fd-ea60-4096-b521-f5f1ff91610c",
  "isSidechain": false,
  "requestId": "req_011Cb28xpAkeGTgs65EEN6tj",
  "type": "assistant",
  "uuid": "c1f355e2-2c55-4536-9302-9f1734776fd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mRySEvaXRh4MbpJuypRZy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9585,
      "cache_read_input_tokens": 42316,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 42316,
          "cache_creation_input_tokens": 9585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9585
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

_source line 24 · 2026-05-14T08:22:39.593Z_

<details><summary>↩ Tool result · reported error · `toolu_01RPMP6DmXhmhRdBGCeGfSW3`</summary>

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
  "parentUuid": "c1f355e2-2c55-4536-9302-9f1734776fd8",
  "isSidechain": false,
  "promptId": "f67db5d7-4662-48a7-ba27-d130d41b7555",
  "type": "user",
  "uuid": "2e839b2b-319c-42d4-8c2f-19f1049e0a9a",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "c1f355e2-2c55-4536-9302-9f1734776fd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-14T08:22:43.690Z_

<details><summary>Logged reasoning block</summary>

```text
The `acl.sty` file is not available. Let me switch to a simpler document class that's available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e839b2b-319c-42d4-8c2f-19f1049e0a9a",
  "isSidechain": false,
  "requestId": "req_011Cb28y8ekSwAhgyKQUhm7H",
  "type": "assistant",
  "uuid": "9f534de1-4f35-4367-b8b4-66391e9aab64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ta65cnadaJN86TMREWA84",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 480,
      "cache_read_input_tokens": 51901,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 490,
          "cache_read_input_tokens": 51901,
          "cache_creation_input_tokens": 480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 480
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

_source line 26 · 2026-05-14T08:22:44.308Z_

ACL style not available. I'll switch to a standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f534de1-4f35-4367-b8b4-66391e9aab64",
  "isSidechain": false,
  "requestId": "req_011Cb28y8ekSwAhgyKQUhm7H",
  "type": "assistant",
  "uuid": "3fb047ec-06d0-49b3-b59d-018b517b8e96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ta65cnadaJN86TMREWA84",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 480,
      "cache_read_input_tokens": 51901,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 490,
          "cache_read_input_tokens": 51901,
          "cache_creation_input_tokens": 480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 480
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

_source line 27 · 2026-05-14T08:22:48.663Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01M3orP1wzqcreyWWgktKH28`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{subcaption}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{subcaption}\n\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}\n\\usepackage{natbib}\n\\renewcommand{\\bibsection}{\\section*{References}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fb047ec-06d0-49b3-b59d-018b517b8e96",
  "isSidechain": false,
  "requestId": "req_011Cb28y8ekSwAhgyKQUhm7H",
  "type": "assistant",
  "uuid": "81f8e65a-9cca-4a62-8dab-ee95529c1c55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ta65cnadaJN86TMREWA84",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 480,
      "cache_read_input_tokens": 51901,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 490,
          "cache_read_input_tokens": 51901,
          "cache_creation_input_tokens": 480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 480
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

_source line 28 · 2026-05-14T08:22:48.684Z_

<details><summary>↩ Tool result · `toolu_01M3orP1wzqcreyWWgktKH28`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81f8e65a-9cca-4a62-8dab-ee95529c1c55",
  "isSidechain": false,
  "promptId": "f67db5d7-4662-48a7-ba27-d130d41b7555",
  "type": "user",
  "uuid": "57a71059-ffb2-41e6-94be-465233b34189",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{subcaption}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{subcaption}\n\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}\n\\usepackage{natbib}\n\\renewcommand{\\bibsection}{\\section*{References}}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\documentclass[11pt,a4paper]{article}",
          "-\\usepackage[hyperref]{acl}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{graphicx}"
        ]
      },
      {
        "oldStart": 10,
        "oldLines": 6,
        "newStart": 10,
        "newLines": 9,
        "lines": [
          " \\usepackage{xcolor}",
          " \\usepackage{tabularx}",
          " \\usepackage{subcaption}",
          "+\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}",
          "+\\usepackage{natbib}",
          "+\\renewcommand{\\bibsection}{\\section*{References}}",
          " ",
          " \\title{A Cautionary Tale: Scale, Seeds, and the Fragility of\\\\Hard Negative Mining for Code Retrieval}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "81f8e65a-9cca-4a62-8dab-ee95529c1c55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-14T08:22:48.716Z_

```json
{
  "parentUuid": "57a71059-ffb2-41e6-94be-465233b34189",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9ac5d423-e689-47b4-84a1-475ca715958d",
  "timestamp": "2026-05-14T08:22:48.716Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 30 · 2026-05-14T08:22:53.127Z_

Also need to replace the bibliography command since we don't have a .bib file. I'll use inline references instead.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ac5d423-e689-47b4-84a1-475ca715958d",
  "isSidechain": false,
  "requestId": "req_011Cb28yod3D5HZDe97954qM",
  "type": "assistant",
  "uuid": "0a212a2b-a984-472f-b6c0-409bfb2f6136",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7jR9v3x19XdwD5UWon8iB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 52381,
      "output_tokens": 948,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 948,
          "cache_read_input_tokens": 52381,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 31 · 2026-05-14T08:23:07.022Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01KVYzMgPKp2aCqP2zKPwtFs`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\begin{thebibliography}{10}\n\n\\bibitem[Xiong et~al.(2021)]{xiong2021ance}\nLee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, and Arnold Overwijk.\n\\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Li et~al.(2023)]{li2023swerank}\nRaymond Li et~al.\n\\newblock SweRank: contrastive learning for repository-level code retrieval.\n\\newblock \\emph{arXiv preprint}, 2023.\n\n\\bibitem[Yang et~al.(2024)]{yang2024swefixer}\nChao Yang et~al.\n\\newblock SWE-Fixer: training open-source LLMs for effective and efficient GitHub issue resolution.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Gao et~al.(2024)]{gao2024cocohanere}\nXinyu Gao et~al.\n\\newblock CoCoHaNeRe: contrastive code hard negative retrieval.\n\\newblock In \\emph{EMNLP}, 2024.\n\n\\bibitem[Guo et~al.(2021)]{guo2021graphcodebert}\nDaya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, et~al.\n\\newblock GraphCodeBERT: pre-training code representations with data flow.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Shrivastava et~al.(2023)]{shrivastava2023repofusion}\nDisha Shrivastava, Hugo Larochelle, and Daniel Tarlow.\n\\newblock RepoFusion: training code models to understand your repository.\n\\newblock \\emph{arXiv preprint}, 2023.\n\n\\bibitem[Qin et~al.(2024)]{qin2024locagent}\nKechi Qin et~al.\n\\newblock LocAgent: graph-guided LLM agents for code localization.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Liu et~al.(2024)]{liu2024codexgraph}\nXiangyan Liu et~al.\n\\newblock CodexGraph: bridging large language models and code repositories via code graph databases.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Wu et~al.(2024)]{wu2024arise}\nJiaheng Wu et~al.\n\\newblock ARISE: autonomous repair with intra-procedural static execution.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\end{thebibliography}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a212a2b-a984-472f-b6c0-409bfb2f6136",
  "isSidechain": false,
  "requestId": "req_011Cb28yod3D5HZDe97954qM",
  "type": "assistant",
  "uuid": "0622443a-fc2d-4d84-9c53-1f119fb3a879",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7jR9v3x19XdwD5UWon8iB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 52381,
      "output_tokens": 948,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 948,
          "cache_read_input_tokens": 52381,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 32 · 2026-05-14T08:23:07.045Z_

<details><summary>↩ Tool result · `toolu_01KVYzMgPKp2aCqP2zKPwtFs`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0622443a-fc2d-4d84-9c53-1f119fb3a879",
  "isSidechain": false,
  "promptId": "f67db5d7-4662-48a7-ba27-d130d41b7555",
  "type": "user",
  "uuid": "1921b9f2-a150-45c5-b385-0b617445887e",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "newString": "\\begin{thebibliography}{10}\n\n\\bibitem[Xiong et~al.(2021)]{xiong2021ance}\nLee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, and Arnold Overwijk.\n\\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Li et~al.(2023)]{li2023swerank}\nRaymond Li et~al.\n\\newblock SweRank: contrastive learning for repository-level code retrieval.\n\\newblock \\emph{arXiv preprint}, 2023.\n\n\\bibitem[Yang et~al.(2024)]{yang2024swefixer}\nChao Yang et~al.\n\\newblock SWE-Fixer: training open-source LLMs for effective and efficient GitHub issue resolution.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Gao et~al.(2024)]{gao2024cocohanere}\nXinyu Gao et~al.\n\\newblock CoCoHaNeRe: contrastive code hard negative retrieval.\n\\newblock In \\emph{EMNLP}, 2024.\n\n\\bibitem[Guo et~al.(2021)]{guo2021graphcodebert}\nDaya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, et~al.\n\\newblock GraphCodeBERT: pre-training code representations with data flow.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Shrivastava et~al.(2023)]{shrivastava2023repofusion}\nDisha Shrivastava, Hugo Larochelle, and Daniel Tarlow.\n\\newblock RepoFusion: training code models to understand your repository.\n\\newblock \\emph{arXiv preprint}, 2023.\n\n\\bibitem[Qin et~al.(2024)]{qin2024locagent}\nKechi Qin et~al.\n\\newblock LocAgent: graph-guided LLM agents for code localization.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Liu et~al.(2024)]{liu2024codexgraph}\nXiangyan Liu et~al.\n\\newblock CodexGraph: bridging large language models and code repositories via code graph databases.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Wu et~al.(2024)]{wu2024arise}\nJiaheng Wu et~al.\n\\newblock ARISE: autonomous repair with intra-procedural static execution.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\end{thebibliography}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 568,
        "oldLines": 9,
        "newStart": 568,
        "newLines": 55,
        "lines": [
          " ",
          " We release our CodeQL-based dataflow analysis pipeline as open-source infrastructure for future research on structural code understanding.",
          " ",
          "-\\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          "+\\begin{thebibliography}{10}",
          " ",
          "+\\bibitem[Xiong et~al.(2021)]{xiong2021ance}",
          "+Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, and Arnold Overwijk.",
          "+\\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.",
          "+\\newblock In \\emph{ICLR}, 2021.",
          "+",
          "+\\bibitem[Li et~al.(2023)]{li2023swerank}",
          "+Raymond Li et~al.",
          "+\\newblock SweRank: contrastive learning for repository-level code retrieval.",
          "+\\newblock \\emph{arXiv preprint}, 2023.",
          "+",
          "+\\bibitem[Yang et~al.(2024)]{yang2024swefixer}",
          "+Chao Yang et~al.",
          "+\\newblock SWE-Fixer: training open-source LLMs for effective and efficient GitHub issue resolution.",
          "+\\newblock \\emph{arXiv preprint}, 2024.",
          "+",
          "+\\bibitem[Gao et~al.(2024)]{gao2024cocohanere}",
          "+Xinyu Gao et~al.",
          "+\\newblock CoCoHaNeRe: contrastive code hard negative retrieval.",
          "+\\newblock In \\emph{EMNLP}, 2024.",
          "+",
          "+\\bibitem[Guo et~al.(2021)]{guo2021graphcodebert}",
          "+Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, et~al.",
          "+\\newblock GraphCodeBERT: pre-training code representations with data flow.",
          "+\\newblock In \\emph{ICLR}, 2021.",
          "+",
          "+\\bibitem[Shrivastava et~al.(2023)]{shrivastava2023repofusion}",
          "+Disha Shrivastava, Hugo Larochelle, and Daniel Tarlow.",
          "+\\newblock RepoFusion: training code models to understand your repository.",
          "+\\newblock \\emph{arXiv preprint}, 2023.",
          "+",
          "+\\bibitem[Qin et~al.(2024)]{qin2024locagent}",
          "+Kechi Qin et~al.",
          "+\\newblock LocAgent: graph-guided LLM agents for code localization.",
          "+\\newblock \\emph{arXiv preprint}, 2024.",
          "+",
          "+\\bibitem[Liu et~al.(2024)]{liu2024codexgraph}",
          "+Xiangyan Liu et~al.",
          "+\\newblock CodexGraph: bridging large language models and code repositories via code graph databases.",
          "+\\newblock \\emph{arXiv preprint}, 2024.",
          "+",
          "+\\bibitem[Wu et~al.(2024)]{wu2024arise}",
          "+Jiaheng Wu et~al.",
          "+\\newblock ARISE: autonomous repair with intra-procedural static execution.",
          "+\\newblock \\emph{arXiv preprint}, 2024.",
          "+",
          "+\\end{thebibliography}",
          "+",
          " \\appendix",
          " ",
          " \\section{Full Data Distribution Audit}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "0622443a-fc2d-4d84-9c53-1f119fb3a879",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T08:23:10.872Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AC7mAHgp9vceoAK9mBq8qg`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1921b9f2-a150-45c5-b385-0b617445887e",
  "isSidechain": false,
  "requestId": "req_011Cb291A6cfbGsxe8f4vQGU",
  "type": "assistant",
  "uuid": "6b656c31-5bf3-43fc-9381-4f46672c7886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwP4jYk1rZbmVmZNT6b2Lr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1033,
      "cache_read_input_tokens": 53060,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 53060,
          "cache_creation_input_tokens": 1033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1033
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

_source line 34 · 2026-05-14T08:23:12.086Z_

<details><summary>↩ Tool result · `toolu_01AC7mAHgp9vceoAK9mBq8qg`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
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
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `li2023swerank' on page 1 undefined on input l
ine 42.


Package natbib Warning: Citation `yang2024swefixer' on page 1 undefined on inpu
t line 42.


Package natbib Warning: Citation `gao2024cocohanere' on page 1 undefined on inp
ut line 45.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)

LaTeX Warning: Reference `sec:scaling' on page 1 undefined on input line 58.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

LaTeX Warning: Reference `sec:ablations' on page 2 undefined on input line 60.


LaTeX Warning: Reference `sec:method' on page 2 undefined on input line 62.


Overfull \hbox (0.28061pt too wide) in paragraph at lines 62--63
[]\OT1/ptm/b/n/10.95 Open in-fras-truc-ture. \OT1/ptm/m/n/10.95 Our CodeQL-base
d pipeline for inter-procedural dataflow anal-y-sis achieves

Package natbib Warning: Citation `xiong2021ance' on page 2 undefined on input l
ine 72.


Package natbib Warning: Citation `gao2024cocohanere' on page 2 undefined on inp
ut line 74.


Package natbib Warning: Citation `li2023swerank' on page 2 undefined on input l
ine 77.


Package natbib Warning: Citation `yang2024swefixer' on page 2 undefined on inpu
t line 77.


Package natbib Warning: Citation `guo2021graphcodebert' on page 2 undefined on 
input line 78.


Package natbib Warning: Citation `shrivastava2023repofusion' on page 2 undefine
d on input line 79.


Package natbib Warning: Citation `qin2024locagent' on page 2 undefined on input
 line 82.


Package natbib Warning: Citation `liu2024codexgraph' on page 2 undefined on inp
ut line 82.


Package natbib Warning: Citation `wu2024arise' on page 2 undefined on input lin
e 83.

[2]

LaTeX Warning: Reference `tab:qwen_full' on page 3 undefined on input line 143.



LaTeX Warning: Reference `tab:starcoder_full' on page 3 undefined on input line
 175.

[3]

LaTeX Warning: Reference `tab:swebench' on page 4 undefined on input line 210.


LaTeX Warning: Reference `tab:bootstrap' on page 4 undefined on input line 212.



LaTeX Warning: Reference `tab:repobench' on page 4 undefined on input line 250.



LaTeX Warning: Reference `tab:inference_compare' on page 4 undefined on input l
ine 276.


LaTeX Warning: Reference `tab:scaling' on page 4 undefined on input line 308.

[4]

LaTeX Warning: Reference `tab:stratified' on page 5 undefined on input line 337
.


LaTeX Warning: Reference `tab:audit' on page 5 undefined on input line 366.

[5]

LaTeX Warning: Reference `tab:failure' on page 6 undefined on input line 395.


LaTeX Warning: Reference `tab:temperature' on page 6 undefined on input line 43
0.


LaTeX Warning: Reference `tab:hops' on page 6 undefined on input line 453.


LaTeX Warning: Reference `tab:fusion' on page 6 undefined on input line 478.

[6]

LaTeX Warning: Reference `tab:dynamic' on page 7 undefined on input line 502.


LaTeX Warning: Reference `sec:scaling' on page 7 undefined on input line 533.


LaTeX Warning: Reference `sec:stratified' on page 7 undefined on input line 534
.

[7] [8]

LaTeX Warning: Reference `tab:audit' on page 9 undefined on input line 625.


Package natbib Warning: There were undefined citations.

[9] [10] (./paper.aux

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
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 154153 bytes).
Transcript written on paper.log.
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]
Overfull \hbox (0.28061pt too wide) in paragraph at lines 62--63
[]\OT1/ptm/b/n/10.95 Open in-fras-truc-ture. \OT1/ptm/m/n/10.95 Our CodeQL-base
d pipeline for inter-procedural dataflow anal-y-sis achieves
[2] [3] [4] [5] [6] [7] [8] [9] [10] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 158146 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b656c31-5bf3-43fc-9381-4f46672c7886",
  "isSidechain": false,
  "promptId": "f67db5d7-4662-48a7-ba27-d130d41b7555",
  "type": "user",
  "uuid": "7fb9df12-3fc8-416a-a2f5-6f5bc3afcfe4",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `li2023swerank' on page 1 undefined on input l\nine 42.\n\n\nPackage natbib Warning: Citation `yang2024swefixer' on page 1 undefined on inpu\nt line 42.\n\n\nPackage natbib Warning: Citation `gao2024cocohanere' on page 1 undefined on inp\nut line 45.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n\nLaTeX Warning: Reference `sec:scaling' on page 1 undefined on input line 58.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nLaTeX Warning: Reference `sec:ablations' on page 2 undefined on input line 60.\n\n\nLaTeX Warning: Reference `sec:method' on page 2 undefined on input line 62.\n\n\nOverfull \\hbox (0.28061pt too wide) in paragraph at lines 62--63\n[]\\OT1/ptm/b/n/10.95 Open in-fras-truc-ture. \\OT1/ptm/m/n/10.95 Our CodeQL-base\nd pipeline for inter-procedural dataflow anal-y-sis achieves\n\nPackage natbib Warning: Citation `xiong2021ance' on page 2 undefined on input l\nine 72.\n\n\nPackage natbib Warning: Citation `gao2024cocohanere' on page 2 undefined on inp\nut line 74.\n\n\nPackage natbib Warning: Citation `li2023swerank' on page 2 undefined on input l\nine 77.\n\n\nPackage natbib Warning: Citation `yang2024swefixer' on page 2 undefined on inpu\nt line 77.\n\n\nPackage natbib Warning: Citation `guo2021graphcodebert' on page 2 undefined on \ninput line 78.\n\n\nPackage natbib Warning: Citation `shrivastava2023repofusion' on page 2 undefine\nd on input line 79.\n\n\nPackage natbib Warning: Citation `qin2024locagent' on page 2 undefined on input\n line 82.\n\n\nPackage natbib Warning: Citation `liu2024codexgraph' on page 2 undefined on inp\nut line 82.\n\n\nPackage natbib Warning: Citation `wu2024arise' on page 2 undefined on input lin\ne 83.\n\n[2]\n\nLaTeX Warning: Reference `tab:qwen_full' on page 3 undefined on input line 143.\n\n\n\nLaTeX Warning: Reference `tab:starcoder_full' on page 3 undefined on input line\n 175.\n\n[3]\n\nLaTeX Warning: Reference `tab:swebench' on page 4 undefined on input line 210.\n\n\nLaTeX Warning: Reference `tab:bootstrap' on page 4 undefined on input line 212.\n\n\n\nLaTeX Warning: Reference `tab:repobench' on page 4 undefined on input line 250.\n\n\n\nLaTeX Warning: Reference `tab:inference_compare' on page 4 undefined on input l\nine 276.\n\n\nLaTeX Warning: Reference `tab:scaling' on page 4 undefined on input line 308.\n\n[4]\n\nLaTeX Warning: Reference `tab:stratified' on page 5 undefined on input line 337\n.\n\n\nLaTeX Warning: Reference `tab:audit' on page 5 undefined on input line 366.\n\n[5]\n\nLaTeX Warning: Reference `tab:failure' on page 6 undefined on input line 395.\n\n\nLaTeX Warning: Reference `tab:temperature' on page 6 undefined on input line 43\n0.\n\n\nLaTeX Warning: Reference `tab:hops' on page 6 undefined on input line 453.\n\n\nLaTeX Warning: Reference `tab:fusion' on page 6 undefined on input line 478.\n\n[6]\n\nLaTeX Warning: Reference `tab:dynamic' on page 7 undefined on input line 502.\n\n\nLaTeX Warning: Reference `sec:scaling' on page 7 undefined on input line 533.\n\n\nLaTeX Warning: Reference `sec:stratified' on page 7 undefined on input line 534\n.\n\n[7] [8]\n\nLaTeX Warning: Reference `tab:audit' on page 9 undefined on input line 625.\n\n\nPackage natbib Warning: There were undefined citations.\n\n[9] [10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 154153 bytes).\nTranscript written on paper.log.\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\nOverfull \\hbox (0.28061pt too wide) in paragraph at lines 62--63\n[]\\OT1/ptm/b/n/10.95 Open in-fras-truc-ture. \\OT1/ptm/m/n/10.95 Our CodeQL-base\nd pipeline for inter-procedural dataflow anal-y-sis achieves\n[2] [3] [4] [5] [6] [7] [8] [9] [10] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 158146 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6b656c31-5bf3-43fc-9381-4f46672c7886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T075732 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-contex…",
  "leafUuid": "7fb9df12-3fc8-416a-a2f5-6f5bc3afcfe4",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate negative result paper on hard negative mining",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599"
}
```

---

### Assistant

_source line 37 · 2026-05-14T08:23:26.921Z_

编译成功，生成 10 页 PDF。

输出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper.pdf`

论文结构覆盖了 `experiment_data.json` 中全部 15 个实验：
- **Table 1–2**: Qwen/StarCoder 9-seed × 3-strategy 全量结果
- **Table 3–4**: SWE-bench Lite resolve rates + bootstrap CI
- **Table 5**: RepoBench-R 跨域评估
- **Table 6**: Inference-time graph 方法对比
- **Table 7**: Data size scaling law（核心发现）
- **Table 8**: Embedding benefit 按 repo size 分层分析
- **Table 9**: Data pipeline 分布审计
- **Table 10**: Failure taxonomy（50 case 手动分析）
- **Table 11–14**: Ablation（温度、hop distance、fusion head、dynamic mining）
- Dataflow distance weighting 和 qualitative examples 以文字形式纳入

叙事按 narrative guidance 完全 reframe 为 negative result paper："A Cautionary Tale: Scale, Seeds, and the Fragility of Hard Negative Mining for Code Retrieval"。所有数字直接来自 JSON，未编造。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fb9df12-3fc8-416a-a2f5-6f5bc3afcfe4",
  "isSidechain": false,
  "requestId": "req_011Cb291XagrJcLhnwBeiday",
  "type": "assistant",
  "uuid": "f85097c6-a165-4b0d-bbd0-5f3376753044",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F11hSBYs1t5zW5rAXmR162",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4527,
      "cache_read_input_tokens": 54093,
      "output_tokens": 370,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4527,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 370,
          "cache_read_input_tokens": 54093,
          "cache_creation_input_tokens": 4527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4527
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

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T075732 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-contex…",
  "leafUuid": "f85097c6-a165-4b0d-bbd0-5f3376753044",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate negative result paper on hard negative mining",
  "sessionId": "6681349e-5f13-4463-9075-814ffc4d8599"
}
```

---
