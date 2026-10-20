# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/9303450c-67a8-42e0-bab2-dba2fc96a15c.jsonl`
- **Structured JSON:** [`ee9c2072d6067fc1c824.json`](../../sessions/ee/ee9c2072d6067fc1c824.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T13:44:23.730Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T13:44:23.730Z",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Claim 2 从 'phase transition in trace informativeness' 改为 'diagnostic signal concentrates in trace tail with diminishing returns; information density — not gradient dilution — is the primary bottleneck'。tail-384 在四模型上均落在 256→512 的 43-53% 位置（83-88%）， 确认 smooth gradient 而非 sharp boundary。Budget curve 四模型趋势一致（log-shaped  diminishing returns），但无共同拐点——每个模型的 steepest gain 区间长度和位置略有不同。 Budget curve 从 standalone finding 降为 supporting figure，label_only 26/74 分解升为  Claim 2 sole quantitative evidence。补偿措施: (a) tail-512≫head-2048（~94% vs ~79%,  Δ≈15pp）作为 information locality 的 strong evidence；(b) exception_only scale invariance （1.5B=7B=13B=99.83%）提升至更高叙事位置；(c) cross-model calibration (plan_019, 1h) +  error analysis (plan_018, 0h) 增加独立 evidence 维度。cross-seed σ~1-3pp 不否定趋势但 削弱 point estimate 精度，所有 budget curve 数字需附 uncertainty band。仍冲 Main， Findings 作 fallback。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-18T13:44:23.734Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T13:44:23.734Z",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c"
}
```

---

## Round 1

29 recorded events

### User

_source line 3 · 2026-05-18T13:44:23.756Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Claim 2 从 'phase transition in trace informativeness' 改为 'diagnostic signal concentrates in trace tail with diminishing returns; information density — not gradient dilution — is the primary bottleneck'。tail-384 在四模型上均落在 256→512 的 43-53% 位置（83-88%）， 确认 smooth gradient 而非 sharp boundary。Budget curve 四模型趋势一致（log-shaped  diminishing returns），但无共同拐点——每个模型的 steepest gain 区间长度和位置略有不同。 Budget curve 从 standalone finding 降为 supporting figure，label_only 26/74 分解升为  Claim 2 sole quantitative evidence。补偿措施: (a) tail-512≫head-2048（~94% vs ~79%,  Δ≈15pp）作为 information locality 的 strong evidence；(b) exception_only scale invariance （1.5B=7B=13B=99.83%）提升至更高叙事位置；(c) cross-model calibration (plan_019, 1h) +  error analysis (plan_018, 0h) 增加独立 evidence 维度。cross-seed σ~1-3pp 不否定趋势但 削弱 point estimate 精度，所有 budget curve 数字需附 uncertainty band。仍冲 Main， Findings 作 fallback。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "26dc48b8-83e6-4c7b-83d0-0a6fb6e0b0fa",
  "type": "user",
  "uuid": "15aa85e3-bfa8-4799-9f26-6c87f789345d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T13:44:23.756Z_

```json
{
  "parentUuid": "15aa85e3-bfa8-4799-9f26-6c87f789345d",
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
  "uuid": "4e55ee11-8838-42b5-8389-27a7aac728ee",
  "timestamp": "2026-05-18T13:44:23.756Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T13:44:23.756Z_

```json
{
  "parentUuid": "4e55ee11-8838-42b5-8389-27a7aac728ee",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ebfc945e-7b1c-40b7-80e5-259f65dde6b7",
  "timestamp": "2026-05-18T13:44:23.756Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
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
  "aiTitle": "Generate simulated research paper from experiment data",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c"
}
```

---

### Assistant

_source line 7 · 2026-05-18T13:44:27.500Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebfc945e-7b1c-40b7-80e5-259f65dde6b7",
  "isSidechain": false,
  "requestId": "req_011CbA8jnmaiF9tjNxuT7Ho9",
  "type": "assistant",
  "uuid": "42ecd2e3-4498-45f3-88d0-f58966723c6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hwn5VcuYpuSLxAMabALAMa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12940,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12940
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

_source line 8 · 2026-05-18T13:44:28.004Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JqWivcRyZ61iRCufdZvMX7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42ecd2e3-4498-45f3-88d0-f58966723c6b",
  "isSidechain": false,
  "requestId": "req_011CbA8jnmaiF9tjNxuT7Ho9",
  "type": "assistant",
  "uuid": "d126892a-1813-41c5-96d8-411385b00018",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hwn5VcuYpuSLxAMabALAMa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12940,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12940
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

_source line 9 · 2026-05-18T13:44:28.391Z_

<details><summary>↩ Tool result · `toolu_01JqWivcRyZ61iRCufdZvMX7`</summary>

```text
1	[
2	  {
3	    "name": "fine_grained_phase_transition_tail384",
4	    "description": "tail-384 × 4 models，精确定位 256→512 区间 transition 形态",
5	    "results": {
6	      "qwen7b_tail384_accuracy": 0.856,
7	      "qwen7b_tail384_ci": [
8	        0.835,
9	        0.877
10	      ],
11	      "qwen7b_sharpness_index": 0.52,
12	      "deepseek_tail384_accuracy": 0.843,
13	      "deepseek_tail384_ci": [
14	        0.821,
15	        0.865
16	      ],
17	      "deepseek_sharpness_index": 0.46,
18	      "qwen15b_tail384_accuracy": 0.832,
19	      "qwen15b_tail384_ci": [
20	        0.808,
21	        0.854
22	      ],
23	      "qwen15b_sharpness_index": 0.44,
24	      "codellama13b_tail384_accuracy": 0.883,
25	      "codellama13b_tail384_ci": [
26	        0.863,
27	        0.903
28	      ],
29	      "codellama13b_sharpness_index": 0.54,
30	      "four_model_mean": 0.854,
31	      "four_model_std_pp": 2.23,
32	      "mean_sharpness_index": 0.49,
33	      "all_models_gradual": true
34	    },
35	    "tables": [
36	      {
37	        "name": "Budget Curve with tail-384 新数据点",
38	        "columns": [
39	          "Model",
40	          "tail-256",
41	          "tail-384",
42	          "tail-512",
43	          "tail-1024",
44	          "tail-2048",
45	          "Δ(256→384)",
46	          "Δ(384→512)",
47	          "sharpness_index"
48	        ],
49	        "rows": [
50	          [
51	            "Qwen-2.5-Coder-7B",
52	            "77.5%",
53	            "85.6%",
54	            "93.6%",
55	            "96.5%",
56	            "97.3%",
57	            "+8.1pp",
58	            "+8.0pp",
59	            0.52
60	          ],
61	          [
62	            "DeepSeek-Coder-6.7B",
63	            "76.4%",
64	            "84.3%",
65	            "93.9%",
66	            "96.5%",
67	            "95.0%",
68	            "+7.9pp",
69	            "+9.6pp",
70	            0.46
71	          ],
72	          [
73	            "Qwen-2.5-Coder-1.5B",
74	            "72.6%",
75	            "83.2%",
76	            "95.6%",
77	            "96.6%",
78	            "97.9%",
79	            "+10.6pp",
80	            "+12.4pp",
81	            0.44
82	          ],
83	          [
84	            "CodeLlama-13B-Instruct",
85	            "77.9%",
86	            "88.3%",
87	            "97.5%",
88	            "98.2%",
89	            "collapsed",
90	            "+10.4pp",
91	            "+9.2pp",
92	            0.54
93	          ]
94	        ]
95	      },
96	      {
97	        "name": "Sharpness index 汇总",
98	        "columns": [
99	          "Metric",
100	          "Value",
101	          "Interpretation"
102	        ],
103	        "rows": [
104	          [
105	            "Mean sharpness",
106	            0.49,
107	            "几乎完美 midpoint → gradual transition"
108	          ],
109	          [
110	            "Range",
111	            "[0.44, 0.54]",
112	            "所有模型 within [0.35, 0.65] → 无 outlier"
113	          ],
114	          [
115	            "Cross-model std",
116	            "2.23pp",
117	            "moderate variation, within [2.0, 5.0]"
118	          ],
119	          [
120	            "All > head-2048",
121	            "Yes (Δ 4-9pp)",
122	            "information locality confirmed"
123	          ]
124	        ]
125	      }
126	    ],
127	    "figures": [],
128	    "analysis": "tail-384 数据明确排除 sharp phase transition 假说。四模型 sharpness  index 集中在 0.44-0.54（mean=0.49），指向 transition 恰好在 midpoint  附近——信息是随 token budget 线性累积的，不存在 critical threshold。 关键影响：(1) Claim 2 措辞从 \"phase transition\" 改为 \"diminishing  returns with steepest gains in 256-512 range\"；(2) budget curve 的  核心价值是展示 tail >> head（information locality），不是定位拐点； (3) 四模型形态一致（all gradual）简化了叙事——不需要 model-dependent  transition 的 caveat，可以统一说 \"all models show consistent  log-shaped diminishing returns\"。这比 mixed sharp/gradual 结果  更有利于论文叙事清晰度。budget curve 降为 supporting figure  （1/3 page），label_only 26/74 分解保持 Claim 2 核心地位。\n\n\nmedian 档定义 tail-384 在多数模型上 83-89%，transition 为 smooth gradient。 推导逻辑：exception events 集中在 trace 末尾（crash point + stack trace）， tail-256 捕获 assertion 结果和 traceback 尾部但常截断中段 context；tail-384  额外覆盖约 128 tokens 的 traceback context（调用栈前几帧、变量快照），提供  incremental 而非 step-function 式的信息增益。四模型 sharpness index 均在  0.44-0.54 范围（center 0.49，几乎正好 midpoint），没有模型出现 <0.3（sharp  stay at 256 level）或 >0.7（sharp jump to 512 level）。CodeLlama-13B 略高  （0.54）因 13B 参数量更有效利用 partial exception context；Qwen-1.5B 略低  （0.44）因小模型从 partial signal 中提取信息的效率较低。但差异幅度仅 0.10， 不足以形成 \"strong vs weak model\" 的分组叙事——所有模型的 transition 形态  qualitatively 一致（gradual）。cross_model_std=2.23pp 说明模型间存在  absolute level 差异但 transition 形态 homogeneous。tail-384 四模型均远高于  head-2048 (~79%, Δ≈6-9pp)，information locality 发现 robust。\n"
129	  },
130	  {
131	    "name": "cross_seed_budget_curve_tail512",
132	    "description": "tail-512 × 4 models × 3 seeds，验证 convergence band robustness",
133	    "results": {
134	      "qwen7b": {
135	        "seed42": 0.936,
136	        "seed123": 0.919,
137	        "seed456": 0.947,
138	        "mean": 0.934,
139	        "std_pp": 1.41
140	      },
141	      "deepseek": {
142	        "seed42": 0.939,
143	        "seed123": 0.892,
144	        "seed456": 0.935,
145	        "mean": 0.922,
146	        "std_pp": 2.63
147	      },
148	      "qwen15b": {
149	        "seed42": 0.956,
150	        "seed123": 0.932,
151	        "seed456": 0.949,
152	        "mean": 0.946,
153	        "std_pp": 1.24
154	      },
155	      "codellama13b": {
156	        "seed42": 0.975,
157	        "seed123": 0.958,
158	        "seed456": 0.971,
159	        "mean": 0.968,
160	        "std_pp": 0.89
161	      },
162	      "cross_model_avg_std_pp": 1.54,
163	      "worst_seed_still_above_head2048": true,
164	      "rank_ordering_preserved_all_seeds": true
165	    },
166	    "tables": [
167	      {
168	        "name": "Cross-seed tail-512 Robustness (3 seeds × 4 models)",
169	        "columns": [
170	          "Model",
171	          "Seed42",
172	          "Seed123",
173	          "Seed456",
174	          "Mean",
175	          "Std",
176	          "Min-Max Band",
177	          "Min > head-2048?"
178	        ],
179	        "rows": [
180	          [
181	            "Qwen-7B",
182	            "93.6%",
183	            "91.9%",
184	            "94.7%",
185	            "93.4%",
186	            "1.4pp",
187	            "2.8pp",
188	            "Yes (91.9>81.0)"
189	          ],
190	          [
191	            "DeepSeek-6.7B",
192	            "93.9%",
193	            "89.2%",
194	            "93.5%",
195	            "92.2%",
196	            "2.6pp",
197	            "4.7pp",
198	            "Yes (89.2>79.2)"
199	          ],
200	          [
201	            "Qwen-1.5B",
202	            "95.6%",
203	            "93.2%",
204	            "94.9%",
205	            "94.6%",
206	            "1.2pp",
207	            "2.4pp",
208	            "Yes (93.2>75.3)"
209	          ],
210	          [
211	            "CodeLlama-13B",
212	            "97.5%",
213	            "95.8%",
214	            "97.1%",
215	            "96.8%",
216	            "0.9pp",
217	            "1.7pp",
218	            "Yes (95.8>79.9)"
219	          ]
220	        ]
221	      },
222	      {
223	        "name": "Convergence band vs model capability",
224	        "columns": [
225	          "Group",
226	          "Models",
227	          "Avg_Std",
228	          "Interpretation"
229	        ],
230	        "rows": [
231	          [
232	            "Lower variance",
233	            "Qwen-1.5B, CodeLlama-13B",
234	            "1.1pp",
235	            "Capacity extremes (very small/very large) → deterministic convergence"
236	          ],
237	          [
238	            "Higher variance",
239	            "Qwen-7B, DeepSeek-6.7B",
240	            "2.0pp",
241	            "Mid-scale models with more complex LoRA landscapes"
242	          ]
243	        ]
244	      }
245	    ],
246	    "figures": [],
247	    "analysis": "cross-seed 数据确认：(1) tail >> head 趋势在所有 seeds 上稳健—— worst-case tail-512 (DeepSeek seed123=89.2%) 仍比 best-case head-2048  (~81%) 高 8pp；(2) point estimate 精度有限，单 seed 结果应附 ±2pp  uncertainty；(3) rank ordering 完全 preserved（所有 3 seeds 上  CodeLlama > Qwen-1.5B > Qwen-7B ≈ DeepSeek），model capability  对 absolute level 的影响 consistent。对论文的操作建议：budget curve  figure 中为 tail-512 标注 3-seed error bar，caption 注明 \"typical  σ ≈ 1-3pp across models\"。不需要报告 all 12 individual numbers  in main text——mean ± std 足够。审稿人问 \"single seed?\" 时可指向  appendix full table。24 GPU-hours 投入较大，但回应审稿人的  single-seed concern 是高优先级需求，值得。\n\n\nmedian 档定义 cross-seed variance σ 1-3pp at tail-512，noise 不否定趋势但 削弱 point estimate 精度。tail-512 位于 budget curve 的 steep gain 段终点， LoRA 初始化对此 regime 的影响比 plateau 段（1024/2048）更大。DeepSeek 方差  最高（σ≈2.6pp），与已知 LoRA sensitivity 一致——exception_only 上 DeepSeek  σ=4.8pp（seed123 outlier 91.09%），tail-512 输入更复杂（包含非 exception 的  Tier 2 noise tokens），seed123 的 LoRA 初始化弱点在噪声更多的 input 下被放大。 但 DeepSeek seed123 的 89.2% 仍远高于 head-2048（~79%），information locality  结论不受影响。Qwen-7B σ=1.4pp，高于 exception_only 的 0pp，因为 tail-512  包含更多需要学习的 non-trivial mapping（loop fragments 等），training  stochasticity 有更大 impact。CodeLlama-13B σ 最小（0.9pp），13B 参数量  提供最平滑的 LoRA landscape。Qwen-1.5B σ=1.2pp，比预期低——可能因 1.5B  模型的 LoRA 虽然 rugged 但 capacity 限制使得所有 seed 都收敛到 similar  capacity-bounded solution。关键：rank ordering（CodeLlama > Qwen-1.5B >  Qwen-7B > DeepSeek）在所有 3 seeds 上保持一致，trend robust。\n"
248	  },
249	  {
250	    "name": "error_analysis_failure_modes",
251	    "description": "用已有 predictions.jsonl 分析各条件 failure modes 差异",
252	    "results": {
253	      "exception_only_errors": 2,
254	      "exception_only_categories": {
255	        "GeneratorExit_irreducible": 2
256	      },
257	      "exception_only_direction": "100% pass→fail FN",
258	      "vota_errors": 7,
259	      "vota_overlap_with_exception": 2,
260	      "vota_unique_errors": 5,
261	      "vota_dominant_pattern": "Tier 2 noise: loop artifact (3) + attention dilution (2)",
262	      "full_trace_errors": 217,
263	      "full_trace_overlap_with_no_trace_pct": 0.63,
264	      "full_trace_unique_errors_pct": 0.37,
265	      "full_trace_length_error_correlation_r": 0.41,
266	      "full_trace_long_trace_error_rate": 0.33,
267	      "full_trace_short_trace_error_rate": 0.09,
268	      "no_trace_errors": 296,
269	      "no_trace_dominant_pattern": "majority class bias + code complexity correlation",
270	      "loop_only_errors": 171,
271	      "tier1_tier2_error_jaccard": 0.01,
272	      "cross_model_irreducible_overlap_jaccard": 0.85
273	    },
274	    "tables": [
275	      {
276	        "name": "Error mode distribution by condition (Qwen-7B seed42)",
277	        "columns": [
278	          "Condition",
279	          "Total Errors",
280	          "Error Rate",
281	          "fail→pass (%)",
282	          "pass→fail (%)",
283	          "Dominant Failure Mode"
284	        ],
285	        "rows": [
286	          [
287	            "exception_only",
288	            2,
289	            "0.17%",
290	            "0%",
291	            "100%",
292	            "GeneratorExit irreducible"
293	          ],
294	          [
295	            "ae_only",
296	            1,
297	            "0.08%",
298	            "0%",
299	            "100%",
300	            "GeneratorExit variant"
301	          ],
302	          [
303	            "VOTA",
304	            7,
305	            "0.59%",
306	            "57%",
307	            "43%",
308	            "Tier 2 noise conflict"
309	          ],
310	          [
311	            "loop_only",
312	            171,
313	            "14.4%",
314	            "36%",
315	            "64%",
316	            "Insufficient diagnostic signal"
317	          ],
318	          [
319	            "full_trace",
320	            217,
321	            "18.2%",
322	            "47%",
323	            "53%",
324	            "Information overload (length-correlated)"
325	          ],
326	          [
327	            "label_only",
328	            164,
329	            "13.8%",
330	            "65%",
331	            "35%",
332	            "Gradient dilution residual"
333	          ],
334	          [
335	            "no_trace",
336	            296,
337	            "24.9%",
338	            "70%",
339	            "30%",
340	            "Majority class bias"
341	          ]
342	        ]
343	      },
344	      {
345	        "name": "Error rate by trace length bucket (full_trace)",
346	        "columns": [
347	          "Length_Bucket",
348	          "N_Samples",
349	          "Errors",
350	          "Error_Rate"
351	        ],
352	        "rows": [
353	          [
354	            "<500 tok",
355	            "~190",
356	            "~17",
357	            "~9%"
358	          ],
359	          [
360	            "500-1000 tok",
361	            "~340",
362	            "~54",
363	            "~16%"
364	          ],
365	          [
366	            "1000-1500 tok",
367	            "~370",
368	            "~72",
369	            "~19%"
370	          ],
371	          [
372	            ">1500 tok",
373	            "~290",
374	            "~96",
375	            "~33%"
376	          ]
377	        ]
378	      },
379	      {
380	        "name": "Cross-condition error overlap (Jaccard, Qwen-7B)",
381	        "columns": [
382	          "Pair",
383	          "Jaccard",
384	          "Shared_Errors",
385	          "Interpretation"
386	        ],
387	        "rows": [
388	          [
389	            "exception_only ∩ VOTA",
390	            0.29,
391	            2,
392	            "VOTA superset includes Tier 1 irreducible"
393	          ],
394	          [
395	            "full_trace ∩ no_trace",
396	            0.36,
397	            137,
398	            "63% of full_trace errors also in no_trace"
399	          ],
400	          [
401	            "loop_only ∩ label_only",
402	            0.4,
403	            95,
404	            "Similar difficulty: trace-as-context conditions"
405	          ],
406	          [
407	            "Tier 1 ∩ Tier 2 errors",
408	            0.01,
409	            0,
410	            "Qualitatively different failure modes"
411	          ]
412	        ]
413	      }
414	    ],
415	    "figures": [],
416	    "analysis": "Error analysis 为 3 个 Claims 提供 converging evidence：(1) exception_only  的 irreducible 2/1190 errors 跨模型重叠（Jaccard 0.85）确认是 data/ representation property（Claim 1 \"ceiling\" 论点）；(2) full_trace  error-length correlation r=0.41 是 information overload 的 direct  evidence（Claim 2）；(3) VOTA 的 5 个 Tier 2-attributable errors  quantify \"noise from combining tiers\"（Claim 3）。在 median 档下  这些发现 expected 但 useful——审稿人会 appreciate 对 error 的  systematic analysis，但不会视为 independent contribution。建议作为  Appendix B（~1 page: 1 table + 2 case studies + correlation plot）， main text 中引用关键数字（\"full_trace error rate correlates with  trace length, r=0.41, confirming information overload hypothesis\"）。 0 GPU-hours，纯分析，ROI 极高。\n\n\nError analysis 在 median 档下揭示条件间 qualitatively different failure modes， 为现有 claims 提供 supporting evidence 但不产生新发现。推理链：\n(1) exception_only 的 2 个 error (id=901, 905) 已被完全解释——GeneratorExit 是  Python all() 短路的 BaseException，tracer 统一标 [ERROR]。模型看到 7 行  [ERROR] GeneratorExit 合理预测 fail。这是 representation-inherent error， 非模型不足。跨 Qwen 3 seeds 完全重合确认是 data property。\n(2) VOTA 额外 5 个 error 源自 Tier 2 noise：3 例中 loop compression 产生  正常行为摘要但同时存在 exception（矛盾信号让模型犹豫，confidence 下降）； 2 例中 Tier 2 tokens 稀释了对 exception 的 attention（输入更长，exception  信号占比更低）。这直接 quantify \"combining tiers introduces noise\" (Claim 3)。\n(3) full_trace 的 217 个 error 中 ~63% 也是 no_trace 的错误——这些是  intrinsically hard cases，trace 未提供 accessible 的额外信号（signal  buried in thousands of tokens）。剩余 37% 是 full_trace unique errors—— trace 信息 actively misleading（长 trace 中的 intermediate exception  被 caught 但 trace 仍包含 [ERROR]，模型误判）或 attention 被长 context  分散。error rate 与 trace length 正相关 (r≈0.41)：>1500 tokens 的 trace  error rate ~33% vs <500 tokens ~9%，information overload 的 dose-response。\n(4) Tier 1 和 Tier 2 的 error sets 几乎不重叠 (Jaccard=0.01)：Tier 1  fails 在 representation ambiguity (GeneratorExit)，Tier 2 fails 在  reasoning complexity (loop behavior interpretation)。\n"
417	  },
418	  {
419	    "name": "cross_model_calibration_exception_only",
420	    "description": "4 models × exception_only ECE/Brier 对比",
421	    "results": {
422	      "qwen7b": {
423	        "accuracy": 0.9983,
424	        "ece": 0.0027,
425	        "brier": 0.0013,
426	        "mce": 0.835
427	      },
428	      "deepseek_seed42": {
429	        "accuracy": 0.9933,
430	        "ece": 0.012,
431	        "brier": 0.006,
432	        "mce": 0.45
433	      },
434	      "qwen15b": {
435	        "accuracy": 0.9983,
436	        "ece": 0.005,
437	        "brier": 0.003,
438	        "mce": 0.62
439	      },
440	      "codellama13b": {
441	        "accuracy": 0.9983,
442	        "ece": 0.003,
443	        "brier": 0.002,
444	        "mce": 0.75
445	      },
446	      "all_nonoutlier_ece_below": 0.015,
447	      "ece_range": [
448	        0.0027,
449	        0.012
450	      ],
451	      "ece_ratio_vs_notrace_range": [
452	        14,
453	        63
454	      ]
455	    },
456	    "tables": [
457	      {
458	        "name": "Cross-model calibration for exception_only",
459	        "columns": [
460	          "Model",
461	          "Accuracy",
462	          "ECE",
463	          "Brier",
464	          "ECE ratio vs no_trace (0.171)"
465	        ],
466	        "rows": [
467	          [
468	            "Qwen-2.5-Coder-7B",
469	            "99.83%",
470	            0.0027,
471	            0.0013,
472	            "63×"
473	          ],
474	          [
475	            "CodeLlama-13B-Instruct",
476	            "99.83%",
477	            0.003,
478	            0.002,
479	            "57×"
480	          ],
481	          [
482	            "Qwen-2.5-Coder-1.5B",
483	            "99.83%",
484	            0.005,
485	            0.003,
486	            "34×"
487	          ],
488	          [
489	            "DeepSeek-Coder-6.7B",
490	            "99.33%",
491	            0.012,
492	            0.006,
493	            "14×"
494	          ]
495	        ]
496	      }
497	    ],
498	    "figures": [],
499	    "analysis": "Cross-model calibration 证实 exception signal 的 calibration 优势  不限于 Qwen-7B——所有 4 模型 ECE ≤ 0.012，与 no_trace ECE 0.171  相比 14-63× improvement。论文可 claim \"exception_only achieves  near-perfect calibration (ECE ≤ 0.012) across all tested models,  regardless of architecture and scale\"。这是独立于 accuracy 的  evidence dimension：即使审稿人质疑 99.83% 是 saturation，ECE/Brier  数据证明模型 \"knows what it knows\"——confidence 与 correctness  高度一致。DeepSeek 的略高 ECE (0.012) 与其更多 errors (8 vs 2)  一致，不 undermine overall finding。建议作为 main text Table  （与 accuracy table 并列或合并为一张大表），1 GPU-hour  investment，cost-effective。\n\n\nCalibration 直接跟随 accuracy 和 error 数量。三个 99.83% 模型（Qwen-7B,  Qwen-1.5B, CodeLlama-13B）仅有 2 个相同 error（GeneratorExit），calibration  差异仅来自 confidence distribution 的模型间差异：\nQwen-7B (ECE=0.0027, 已有数据): 基准。2 个 misclassified samples 的  confidence 贡献几乎全部 ECE。\nCodeLlama-13B (ECE≈0.003): 13B 参数量产生更 peaked softmax distribution， correct predictions 的 confidence 更接近 1.0。2 个 error 的 confidence  也偏高（模型更 \"确定\"），但 overall 因 correct predictions 的 near-perfect  calibration 而 ECE 极低。略高于 Qwen-7B 因为 CodeLlama 的 chat template  与训练数据的 alignment 略有差异。\nQwen-1.5B (ECE≈0.005): 同 Qwen tokenizer，same 2 errors。但 1.5B 模型的  softmax entropy 更高（small model less confident），correct predictions  的 mean confidence 可能在 ~0.95 而非 ~0.99，造成 systematic slight  under-confidence → ECE 略高。\nDeepSeek seed42 (ECE≈0.012): 8 个 errors（vs others 的 2 个），4× 更多  misclassified bins 贡献 ECE。其中部分 fail samples 被高 confidence 预测为  pass（LoRA 训练不完全映射 exception→fail），这些 high-confidence wrong  predictions 是 ECE 的主要 contributor。但 0.012 仍远低于 no_trace 的 0.171  （14× improvement）。\n总体：所有模型 ECE < 0.015，exception signal 的 calibration 优势跨模型  robust。magnitude 差异主要由 error count 驱动，非 signal quality 差异。\n"
500	  },
501	  {
502	    "name": "few_shot_frontier_baseline",
503	    "description": "GPT-4o/Claude 0-shot + 3-shot verdict prediction baseline",
504	    "results": {
505	      "gpt4o_0shot_exception": 0.952,
506	      "gpt4o_0shot_exception_ci": [
507	        0.937,
508	        0.965
509	      ],
510	      "gpt4o_3shot_exception": 0.966,
511	      "gpt4o_3shot_exception_ci": [
512	        0.953,
513	        0.977
514	      ],
515	      "claude_0shot_exception": 0.958,
516	      "claude_0shot_exception_ci": [
517	        0.944,
518	        0.971
519	      ],
520	      "claude_3shot_exception": 0.972,
521	      "claude_3shot_exception_ci": [
522	        0.959,
523	        0.982
524	      ],
525	      "gpt4o_0shot_no_trace": 0.805,
526	      "claude_0shot_no_trace": 0.821,
527	      "sft_qwen7b_exception_only": 0.9983,
528	      "sft_advantage_vs_best_frontier_pp": 2.6,
529	      "sft_qwen15b_advantage_vs_gpt4o_pp": 2.6,
530	      "api_cost_total_usd": 18,
531	      "sft_inference_cost_usd": 0.01
532	    },
533	    "tables": [
534	      {
535	        "name": "SFT vs frontier few-shot comparison",
536	        "columns": [
537	          "Method",
538	          "Model",
539	          "Input",
540	          "Shots",
541	          "Accuracy",
542	          "Errors/1190",
543	          "Approx Cost"
544	        ],
545	        "rows": [
546	          [
547	            "SFT",
548	            "Qwen-2.5-Coder-7B",
549	            "exception_only",
550	            "—",
551	            "99.83%",
552	            2,
553	            "$0.01"
554	          ],
555	          [
556	            "SFT",
557	            "Qwen-2.5-Coder-1.5B",
558	            "exception_only",
559	            "—",
560	            "99.83%",
561	            2,
562	            "$0.005"
563	          ],
564	          [
565	            "SFT",
566	            "CodeLlama-13B",
567	            "exception_only",
568	            "—",
569	            "99.83%",
570	            2,
571	            "$0.02"
572	          ],
573	          [
574	            "Few-shot",
575	            "GPT-4o",
576	            "exception_only",
577	            3,
578	            "96.6%",
579	            "~40",
580	            "$8"
581	          ],
582	          [
583	            "Few-shot",
584	            "Claude-3.5",
585	            "exception_only",
586	            3,
587	            "97.2%",
588	            "~33",
589	            "$10"
590	          ],
591	          [
592	            "Few-shot",
593	            "GPT-4o",
594	            "exception_only",
595	            0,
596	            "95.2%",
597	            "~57",
598	            "$5"
599	          ],
600	          [
601	            "Few-shot",
602	            "Claude-3.5",
603	            "exception_only",
604	            0,
605	            "95.8%",
606	            "~50",
607	            "$7"
608	          ],
609	          [
610	            "Few-shot",
611	            "GPT-4o",
612	            "no_trace",
613	            0,
614	            "80.5%",
615	            "~232",
616	            "$3"
617	          ],
618	          [
619	            "Few-shot",
620	            "Claude-3.5",
621	            "no_trace",
622	            0,
623	            "82.1%",
624	            "~213",
625	            "$5"
626	          ],
627	          [
628	            "SFT",
629	            "Qwen-7B",
630	            "no_trace",
631	            "—",
632	            "75.1%",
633	            296,
634	            "$0.01"
635	          ]
636	        ]
637	      },
638	      {
639	        "name": "Error count perspective (补充审稿人 'gap only 2-3pp' 的 concern)",
640	        "columns": [
641	          "Model",
642	          "Accuracy",
643	          "Errors",
644	          "Error Reduction vs frontier best"
645	        ],
646	        "rows": [
647	          [
648	            "SFT Qwen-7B exception_only",
649	            "99.83%",
650	            2,
651	            "baseline"
652	          ],
653	          [
654	            "Claude 3-shot exception_only",
655	            "97.2%",
656	            "~33",
657	            "16.5× more errors"
658	          ],
659	          [
660	            "GPT-4o 3-shot exception_only",
661	            "96.6%",
662	            "~40",
663	            "20× more errors"
664	          ]
665	        ]
666	      }
667	    ],
668	    "figures": [],
669	    "analysis": "Frontier baseline 在 median 档下提供 solid but not overwhelming  evidence：SFT beats frontier 3-shot by ~2.6pp (error count 16-20×  reduction)。这足以 claim \"task-specific SFT on 7B model surpasses  frontier few-shot\" 但审稿人可能视 2.6pp 为 modest。Rebuttal 策略： (a) 强调 error count 而非 pp——\"from ~33 errors to 2 irreducible  errors\" 更有冲击力；(b) cost perspective——1800× cheaper；(c)  offline deployability。最有价值的发现：frontier models 也从  exception traces 大幅获益 (no_trace→exception: +14-15pp)， independent confirm Claim 1/2。建议 main text 用 1 paragraph +  1 table 呈现，full results 放 appendix。0 GPU-hours，仅 API  cost ~$18。如果 deadline 紧张可 deprioritize——核心 claims  不依赖此数据。\n\n\nFrontier models 的 exception_only 0-shot 能达 95-96% 因为 task 在  exception_only 格式下高度 interpretable：有 [ERROR] → fail，无 [ERROR] →  pass。已有 local model zero-shot 数据（Qwen-1.5B 93.45%, DeepSeek 90.59%） 证明不需要 SFT 就能达到 ~90%+。Frontier models 更强的 instruction following  + 更广的 code knowledge 在此基础上再提升 ~3-5pp：\n(1) GPT-4o 0-shot 95.2%：比 local Qwen-1.5B zero-shot (93.45%) 仅高 1.8pp ——exception task 对 model scale 的 marginal return 很低（进一步证明是  signal-limited not capacity-limited）。剩余 4.8% error 来自：GeneratorExit  等 non-fatal exceptions（同 SFT 模型）、format marker 的不一致解读、 边缘 case 的 conservative \"fail\" 偏好。\n(2) 3-shot 额外 +1.4-1.4pp：exemplars 帮助建立 consistent decision  boundary，特别是处理 [No exception data in trace] marker 的一致性。 但 3 个 exemplars 无法覆盖 exception type 的 long-tail distribution。\n(3) SFT Qwen-7B (99.83%) 仍高于 best frontier 3-shot (Claude 97.2%)  2.6pp。虽然 pp gap 不大，但 error count 差异显著：2 vs ~33 errors， 16.5× fewer mistakes。且 SFT inference cost 是 frontier API 的 ~1/1800。\n(4) Frontier no_trace (80-82%) >> SFT no_trace (75.1%)：frontier model  的 code reasoning 能力可部分替代 trace 信息，但仍远低于 SFT +  exception_only (99.83%)——exception signal + SFT 的组合效果不可被  单纯 model scale 替代。\n"
670	  },
671	  {
672	    "name": "ood_generalization_cross_language",
673	    "description": "不同编程语言/项目的 trace 上测试 exception_only 泛化性",
674	    "results": {
675	      "python_ood_exception_only": 0.963,
676	      "python_ood_degradation_pp": -3.5,
677	      "java_exception_only": 0.918,
678	      "java_degradation_pp": -8.0,
679	      "javascript_exception_only": 0.902,
680	      "javascript_degradation_pp": -9.6,
681	      "cross_lang_mean": 0.928,
682	      "cross_lang_mean_degradation_pp": -7.0,
683	      "python_ood_no_trace": 0.715,
684	      "java_no_trace": 0.68,
685	      "javascript_no_trace": 0.665,
686	      "exception_lift_over_notrace_ood_mean_pp": 24.1,
687	      "ood_test_set_size_per_lang": 500
688	    },
689	    "tables": [
690	      {
691	        "name": "In-distribution vs OOD accuracy by language",
692	        "columns": [
693	          "Language",
694	          "Setting",
695	          "exception_only",
696	          "no_trace",
697	          "Lift",
698	          "Degradation vs ID"
699	        ],
700	        "rows": [
701	          [
702	            "Python",
703	            "ID (HumanEval+MBPP)",
704	            "99.83%",
705	            "75.1%",
706	            "+24.7pp",
707	            "baseline"
708	          ],
709	          [
710	            "Python",
711	            "OOD (new projects)",
712	            "96.3%",
713	            "71.5%",
714	            "+24.8pp",
715	            "-3.5pp"
716	          ],
717	          [
718	            "Java",
719	            "OOD",
720	            "91.8%",
721	            "68.0%",
722	            "+23.8pp",
723	            "-8.0pp"
724	          ],
725	          [
726	            "JavaScript",
727	            "OOD",
728	            "90.2%",
729	            "66.5%",
730	            "+23.7pp",
731	            "-9.6pp"
732	          ]
733	        ]
734	      }
735	    ],
736	    "figures": [],
737	    "analysis": "OOD 实验在 median 档下是最大 risk/reward 投资。如果完成，可 claim  \"exception signal advantage transfers across languages with preserved  lift (~24pp) despite moderate absolute degradation (7pp mean)\"—— 部分回应 single-task scope criticism。但 risk factors：(1) 需要  构建 3 个语言的 OOD 数据集（trace 生成 + 人工验证），timeline  紧张；(2) tracer 对 Java/JS 的 implementation 可能有 quality  issues，影响实验可控性；(3) 如果某语言降到 <85%，审稿人可能  反向 argue \"not robust enough\"。在 ARR May 25 deadline (7天后)  前几乎不可能完成——建议 deprioritize，标注为 camera-ready  supplement 或 future work。如果有余力，优先做 Python OOD  （无需新 tracer，仅需新测试集），~4 GPU-hours 即可。\n\n\nOOD 泛化性取决于 exception signal 的 cross-language structural similarity。 [ERROR] type: ... message: ... 格式是 tracer 的统一输出规范，但 exception  type 名称和 error message 惯例跨语言不同，造成 token-level distribution shift。\nPython OOD (-3.5pp, 96.3%): 同语言不同项目，exception type 分布与训练集  高度重叠（TypeError, ValueError, IndexError 是 universal），仅 project-specific  custom exception classes 造成少量降级。测试集项目的 test structure（pytest  fixtures、多文件 import）可能引入不同的 exception context，但 [ERROR] tag  的 binary signal 不受影响。\nJava (-8.0pp, 91.8%): NullPointerException, ArrayIndexOutOfBoundsException 等  Java-specific type names 训练集未出现——模型无法利用 type-level semantics， 退化到依赖 [ERROR] tag presence 的 binary heuristic。但 binary heuristic  本身在 Qwen-7B zero-shot 上已达 ~89%，SFT 的 fine-tuned decision boundary  在新 type names 上部分失效。\nJavaScript (-9.6pp, 90.2%): 最大降级。JS 的 error handling 更独特（Promise  rejection → UnhandledPromiseRejection, async TypeError），且 error message  格式与 Python 差异最大。tracer 对 JS 的 [ERROR] 标注可能不如 Python  consistent（implementation difference）。\n关键：所有语言上 exception_only lift over no_trace ≈ 24pp（与 in-domain  24.7pp 几乎相同），证明 exception signal 的 fault detection mechanism  跨语言 transferable。Absolute degradation 来自 token vocabulary shift  而非 mechanism failure。\n"
738	  },
739	  {
740	    "name": "training_dynamics_learning_curves",
741	    "description": "exception_only vs full_trace 的 learning curve（每 ~50 steps eval）",
742	    "results": {
743	      "exception_only_frac_to_90pct": 0.05,
744	      "exception_only_frac_to_95pct": 0.08,
745	      "exception_only_frac_to_99pct": 0.2,
746	      "exception_only_curve_shape": "monotonic_rapid_saturation",
747	      "vota_frac_to_90pct": 0.1,
748	      "vota_frac_to_95pct": 0.15,
749	      "vota_frac_to_99pct": 0.3,
750	      "vota_curve_shape": "monotonic_moderate_saturation",
751	      "full_trace_frac_to_80pct": 0.3,
752	      "full_trace_peak": {
753	        "accuracy": 0.83,
754	        "epoch": 1
755	      },
756	      "full_trace_final": 0.8176,
757	      "full_trace_curve_shape": "non_monotonic_epoch2_dip",
758	      "no_trace_plateau_frac": 0.15,
759	      "no_trace_plateau_accuracy": 0.751,
760	      "no_trace_curve_shape": "rapid_plateau_low_ceiling",
761	      "convergence_ratio_exception_vs_vota": 1.9,
762	      "convergence_ratio_exception_vs_fulltrace": 3.8,
763	      "learning_efficiency_exception_samples_per_pp": 9.2,
764	      "learning_efficiency_fulltrace_samples_per_pp": 68.5,
765	      "efficiency_ratio": 7.4
766	    },
767	    "tables": [
768	      {
769	        "name": "Convergence milestones (fraction of total training)",
770	        "columns": [
771	          "Condition",
772	          "To 80%",
773	          "To 90%",
774	          "To 95%",
775	          "To 99%",
776	          "Final Accuracy",
777	          "Curve Shape"
778	        ],
779	        "rows": [
780	          [
781	            "exception_only",
782	            "~3%",
783	            "~5%",
784	            "~8%",
785	            "~20%",
786	            "99.83%",
787	            "Rapid saturation"
788	          ],
789	          [
790	            "VOTA",
791	            "~5%",
792	            "~10%",
793	            "~15%",
794	            "~30%",
795	            "99.41%",
796	            "Moderate saturation"
797	          ],
798	          [
799	            "full_trace",
800	            "~30%",
801	            "never",
802	            "never",
803	            "never",
804	            "81.76%",
805	            "Non-monotonic (epoch2 dip)"
806	          ],
807	          [
808	            "loop_only",
809	            "~12%",
810	            "never",
811	            "never",
812	            "never",
813	            "85.63%",
814	            "Slow saturation"
815	          ],
816	          [
817	            "no_trace",
818	            "never",
819	            "never",
820	            "never",
821	            "never",
822	            "75.13%",
823	            "Low-ceiling plateau"
824	          ]
825	        ]
826	      },
827	      {
828	        "name": "Learning efficiency comparison",
829	        "columns": [
830	          "Condition",
831	          "Effective Unique Samples",
832	          "Lift (pp)",
833	          "Samples per pp",
834	          "Efficiency (relative)"
835	        ],
836	        "rows": [
837	          [
838	            "exception_only",
839	            2858,
840	            24.7,
841	            9.2,
842	            "1.0× (ref)"
843	          ],
844	          [
845	            "VOTA",
846	            "~5800",
847	            24.3,
848	            17.5,
849	            "0.53×"
850	          ],
851	          [
852	            "full_trace",
853	            "~5800",
854	            6.6,
855	            72.1,
856	            "0.13×"
857	          ],
858	          [
859	            "no_trace",
860	            "~5800",
861	            3.6,
862	            132.8,
863	            "0.07×"
864	          ]
865	        ]
866	      }
867	    ],
868	    "figures": [],
869	    "analysis": "Training dynamics 为 Claim 2 提供 process-level evidence（补充已有  outcome-level evidence）。核心 finding：exception_only 不仅 final  accuracy 最高，learning efficiency 也 7.4× higher——denser signal  → faster and better learning。full_trace 的 non-monotonic curve  （epoch2 dip from 83% to 76%）是 information overload 的 dynamic  manifestation：模型先学到 some useful trace patterns (epoch1 peak)， 然后 overfits to noise (epoch2 collapse)，部分恢复 (epoch3)。 这呼应 D1 (eval_loss vs accuracy decoupling)。\n审稿人可能 challenge: \"faster convergence is trivially expected  for shorter sequences\"。Rebuttal: shorter sequences + diagnostic  signal concentration 共同作用——loop_only 的 sequence 长度与  full_trace 相当但 efficiency 5× higher (因 loop 信号 denser than  raw trace)，证明不只是 length effect。\n建议作为 Figure in main text（visual impact 强）但不升为  standalone claim。需修改 train_sft.py 添加 intermediate eval  callback，8 GPU-hours。如果 deadline 紧张，可引用现有  epoch-level 数据（epoch1 vs epoch3）作为 coarse-grained proxy  代替 fine-grained learning curve。\n\nTraining dynamics 直接测量 information density 对 learning efficiency 的  影响。所有数值表示为 training fraction（0=start, 1.0=end of 3 epochs）， 因 absolute step count 取决于 batch size 等 hyperparameters。\nexception_only 收敛最快（~5% training 达 90%, ~8% 达 95%）：input 极短  （mean <100 tokens），gradient 完全集中在 verdict signal 上；effective  unique 样本仅 2858，但 binary structure（有 exception→fail, 无→pass） 极其 learnable。已有 epoch-level 数据佐证：Qwen-7B exception_only 3  seeds 均在 epoch1 结束时已达 99.83%（之后 epochs 无提升）——暗示  实际在 epoch1 早期就已收敛。\nfull_trace 收敛最慢且 non-monotonic：已有 epoch-level 数据  （epoch1=83.03%, epoch2=76.30%, epoch3=81.76%）展示 epoch2 坍塌。 中间 eval 应能捕获更 fine-grained 的 oscillation pattern。峰值在  ~30% training（epoch1 中后段），之后 overfitting 到 trace patterns  而非 verdict signal 导致 epoch2 下降。epoch3 partial recovery 可能  是 random fluctuation。\nVOTA 介于两者之间：含 Tier 1 (fast learning) + Tier 2 (slow learning)  信号，combined curve 的前段被 Tier 1 驱动（快速上升到 >95%），后段  Tier 2 贡献边际提升。已有 epoch-level (epoch1=99.33%, epoch2-3=99.41%)  确认 epoch1 几乎完成所有学习。\nno_trace 快速 plateau：无 trace signal 可学习，模型在 ~15% training  后耗尽 code→verdict 的弱 statistical correlation，之后 flat。\nLearning efficiency ratio: exception_only 每 pp 需 ~9.2 个 effective  training samples（2858 unique / (99.83-75.13) pp），full_trace 需 ~68.5  （~5800 / (81.76-75.13) pp），7.4× 差距直接 quantify information  density 的 learning advantage。\n"
870	  }
871	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d126892a-1813-41c5-96d8-411385b00018",
  "isSidechain": false,
  "promptId": "26dc48b8-83e6-4c7b-83d0-0a6fb6e0b0fa",
  "type": "user",
  "uuid": "cfccf144-7a99-4571-acf7-663a52367b6a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"fine_grained_phase_transition_tail384\",\n    \"description\": \"tail-384 × 4 models，精确定位 256→512 区间 transition 形态\",\n    \"results\": {\n      \"qwen7b_tail384_accuracy\": 0.856,\n      \"qwen7b_tail384_ci\": [\n        0.835,\n        0.877\n      ],\n      \"qwen7b_sharpness_index\": 0.52,\n      \"deepseek_tail384_accuracy\": 0.843,\n      \"deepseek_tail384_ci\": [\n        0.821,\n        0.865\n      ],\n      \"deepseek_sharpness_index\": 0.46,\n      \"qwen15b_tail384_accuracy\": 0.832,\n      \"qwen15b_tail384_ci\": [\n        0.808,\n        0.854\n      ],\n      \"qwen15b_sharpness_index\": 0.44,\n      \"codellama13b_tail384_accuracy\": 0.883,\n      \"codellama13b_tail384_ci\": [\n        0.863,\n        0.903\n      ],\n      \"codellama13b_sharpness_index\": 0.54,\n      \"four_model_mean\": 0.854,\n      \"four_model_std_pp\": 2.23,\n      \"mean_sharpness_index\": 0.49,\n      \"all_models_gradual\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Budget Curve with tail-384 新数据点\",\n        \"columns\": [\n          \"Model\",\n          \"tail-256\",\n          \"tail-384\",\n          \"tail-512\",\n          \"tail-1024\",\n          \"tail-2048\",\n          \"Δ(256→384)\",\n          \"Δ(384→512)\",\n          \"sharpness_index\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen-2.5-Coder-7B\",\n            \"77.5%\",\n            \"85.6%\",\n            \"93.6%\",\n            \"96.5%\",\n            \"97.3%\",\n            \"+8.1pp\",\n            \"+8.0pp\",\n            0.52\n          ],\n          [\n            \"DeepSeek-Coder-6.7B\",\n            \"76.4%\",\n            \"84.3%\",\n            \"93.9%\",\n            \"96.5%\",\n            \"95.0%\",\n            \"+7.9pp\",\n            \"+9.6pp\",\n            0.46\n          ],\n          [\n            \"Qwen-2.5-Coder-1.5B\",\n            \"72.6%\",\n            \"83.2%\",\n            \"95.6%\",\n            \"96.6%\",\n            \"97.9%\",\n            \"+10.6pp\",\n            \"+12.4pp\",\n            0.44\n          ],\n          [\n            \"CodeLlama-13B-Instruct\",\n            \"77.9%\",\n            \"88.3%\",\n            \"97.5%\",\n            \"98.2%\",\n            \"collapsed\",\n            \"+10.4pp\",\n            \"+9.2pp\",\n            0.54\n          ]\n        ]\n      },\n      {\n        \"name\": \"Sharpness index 汇总\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Mean sharpness\",\n            0.49,\n            \"几乎完美 midpoint → gradual transition\"\n          ],\n          [\n            \"Range\",\n            \"[0.44, 0.54]\",\n            \"所有模型 within [0.35, 0.65] → 无 outlier\"\n          ],\n          [\n            \"Cross-model std\",\n            \"2.23pp\",\n            \"moderate variation, within [2.0, 5.0]\"\n          ],\n          [\n            \"All > head-2048\",\n            \"Yes (Δ 4-9pp)\",\n            \"information locality confirmed\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"tail-384 数据明确排除 sharp phase transition 假说。四模型 sharpness  index 集中在 0.44-0.54（mean=0.49），指向 transition 恰好在 midpoint  附近——信息是随 token budget 线性累积的，不存在 critical threshold。 关键影响：(1) Claim 2 措辞从 \\\"phase transition\\\" 改为 \\\"diminishing  returns with steepest gains in 256-512 range\\\"；(2) budget curve 的  核心价值是展示 tail >> head（information locality），不是定位拐点； (3) 四模型形态一致（all gradual）简化了叙事——不需要 model-dependent  transition 的 caveat，可以统一说 \\\"all models show consistent  log-shaped diminishing returns\\\"。这比 mixed sharp/gradual 结果  更有利于论文叙事清晰度。budget curve 降为 supporting figure  （1/3 page），label_only 26/74 分解保持 Claim 2 核心地位。\\n\\n\\nmedian 档定义 tail-384 在多数模型上 83-89%，transition 为 smooth gradient。 推导逻辑：exception events 集中在 trace 末尾（crash point + stack trace）， tail-256 捕获 assertion 结果和 traceback 尾部但常截断中段 context；tail-384  额外覆盖约 128 tokens 的 traceback context（调用栈前几帧、变量快照），提供  incremental 而非 step-function 式的信息增益。四模型 sharpness index 均在  0.44-0.54 范围（center 0.49，几乎正好 midpoint），没有模型出现 <0.3（sharp  stay at 256 level）或 >0.7（sharp jump to 512 level）。CodeLlama-13B 略高  （0.54）因 13B 参数量更有效利用 partial exception context；Qwen-1.5B 略低  （0.44）因小模型从 partial signal 中提取信息的效率较低。但差异幅度仅 0.10， 不足以形成 \\\"strong vs weak model\\\" 的分组叙事——所有模型的 transition 形态  qualitatively 一致（gradual）。cross_model_std=2.23pp 说明模型间存在  absolute level 差异但 transition 形态 homogeneous。tail-384 四模型均远高于  head-2048 (~79%, Δ≈6-9pp)，information locality 发现 robust。\\n\"\n  },\n  {\n    \"name\": \"cross_seed_budget_curve_tail512\",\n    \"description\": \"tail-512 × 4 models × 3 seeds，验证 convergence band robustness\",\n    \"results\": {\n      \"qwen7b\": {\n        \"seed42\": 0.936,\n        \"seed123\": 0.919,\n        \"seed456\": 0.947,\n        \"mean\": 0.934,\n        \"std_pp\": 1.41\n      },\n      \"deepseek\": {\n        \"seed42\": 0.939,\n        \"seed123\": 0.892,\n        \"seed456\": 0.935,\n        \"mean\": 0.922,\n        \"std_pp\": 2.63\n      },\n      \"qwen15b\": {\n        \"seed42\": 0.956,\n        \"seed123\": 0.932,\n        \"seed456\": 0.949,\n        \"mean\": 0.946,\n        \"std_pp\": 1.24\n      },\n      \"codellama13b\": {\n        \"seed42\": 0.975,\n        \"seed123\": 0.958,\n        \"seed456\": 0.971,\n        \"mean\": 0.968,\n        \"std_pp\": 0.89\n      },\n      \"cross_model_avg_std_pp\": 1.54,\n      \"worst_seed_still_above_head2048\": true,\n      \"rank_ordering_preserved_all_seeds\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Cross-seed tail-512 Robustness (3 seeds × 4 models)\",\n        \"columns\": [\n          \"Model\",\n          \"Seed42\",\n          \"Seed123\",\n          \"Seed456\",\n          \"Mean\",\n          \"Std\",\n          \"Min-Max Band\",\n          \"Min > head-2048?\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen-7B\",\n            \"93.6%\",\n            \"91.9%\",\n            \"94.7%\",\n            \"93.4%\",\n            \"1.4pp\",\n            \"2.8pp\",\n            \"Yes (91.9>81.0)\"\n          ],\n          [\n            \"DeepSeek-6.7B\",\n            \"93.9%\",\n            \"89.2%\",\n            \"93.5%\",\n            \"92.2%\",\n            \"2.6pp\",\n            \"4.7pp\",\n            \"Yes (89.2>79.2)\"\n          ],\n          [\n            \"Qwen-1.5B\",\n            \"95.6%\",\n            \"93.2%\",\n            \"94.9%\",\n            \"94.6%\",\n            \"1.2pp\",\n            \"2.4pp\",\n            \"Yes (93.2>75.3)\"\n          ],\n          [\n            \"CodeLlama-13B\",\n            \"97.5%\",\n            \"95.8%\",\n            \"97.1%\",\n            \"96.8%\",\n            \"0.9pp\",\n            \"1.7pp\",\n            \"Yes (95.8>79.9)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Convergence band vs model capability\",\n        \"columns\": [\n          \"Group\",\n          \"Models\",\n          \"Avg_Std\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Lower variance\",\n            \"Qwen-1.5B, CodeLlama-13B\",\n            \"1.1pp\",\n            \"Capacity extremes (very small/very large) → deterministic convergence\"\n          ],\n          [\n            \"Higher variance\",\n            \"Qwen-7B, DeepSeek-6.7B\",\n            \"2.0pp\",\n            \"Mid-scale models with more complex LoRA landscapes\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"cross-seed 数据确认：(1) tail >> head 趋势在所有 seeds 上稳健—— worst-case tail-512 (DeepSeek seed123=89.2%) 仍比 best-case head-2048  (~81%) 高 8pp；(2) point estimate 精度有限，单 seed 结果应附 ±2pp  uncertainty；(3) rank ordering 完全 preserved（所有 3 seeds 上  CodeLlama > Qwen-1.5B > Qwen-7B ≈ DeepSeek），model capability  对 absolute level 的影响 consistent。对论文的操作建议：budget curve  figure 中为 tail-512 标注 3-seed error bar，caption 注明 \\\"typical  σ ≈ 1-3pp across models\\\"。不需要报告 all 12 individual numbers  in main text——mean ± std 足够。审稿人问 \\\"single seed?\\\" 时可指向  appendix full table。24 GPU-hours 投入较大，但回应审稿人的  single-seed concern 是高优先级需求，值得。\\n\\n\\nmedian 档定义 cross-seed variance σ 1-3pp at tail-512，noise 不否定趋势但 削弱 point estimate 精度。tail-512 位于 budget curve 的 steep gain 段终点， LoRA 初始化对此 regime 的影响比 plateau 段（1024/2048）更大。DeepSeek 方差  最高（σ≈2.6pp），与已知 LoRA sensitivity 一致——exception_only 上 DeepSeek  σ=4.8pp（seed123 outlier 91.09%），tail-512 输入更复杂（包含非 exception 的  Tier 2 noise tokens），seed123 的 LoRA 初始化弱点在噪声更多的 input 下被放大。 但 DeepSeek seed123 的 89.2% 仍远高于 head-2048（~79%），information locality  结论不受影响。Qwen-7B σ=1.4pp，高于 exception_only 的 0pp，因为 tail-512  包含更多需要学习的 non-trivial mapping（loop fragments 等），training  stochasticity 有更大 impact。CodeLlama-13B σ 最小（0.9pp），13B 参数量  提供最平滑的 LoRA landscape。Qwen-1.5B σ=1.2pp，比预期低——可能因 1.5B  模型的 LoRA 虽然 rugged 但 capacity 限制使得所有 seed 都收敛到 similar  capacity-bounded solution。关键：rank ordering（CodeLlama > Qwen-1.5B >  Qwen-7B > DeepSeek）在所有 3 seeds 上保持一致，trend robust。\\n\"\n  },\n  {\n    \"name\": \"error_analysis_failure_modes\",\n    \"description\": \"用已有 predictions.jsonl 分析各条件 failure modes 差异\",\n    \"results\": {\n      \"exception_only_errors\": 2,\n      \"exception_only_categories\": {\n        \"GeneratorExit_irreducible\": 2\n      },\n      \"exception_only_direction\": \"100% pass→fail FN\",\n      \"vota_errors\": 7,\n      \"vota_overlap_with_exception\": 2,\n      \"vota_unique_errors\": 5,\n      \"vota_dominant_pattern\": \"Tier 2 noise: loop artifact (3) + attention dilution (2)\",\n      \"full_trace_errors\": 217,\n      \"full_trace_overlap_with_no_trace_pct\": 0.63,\n      \"full_trace_unique_errors_pct\": 0.37,\n      \"full_trace_length_error_correlation_r\": 0.41,\n      \"full_trace_long_trace_error_rate\": 0.33,\n      \"full_trace_short_trace_error_rate\": 0.09,\n      \"no_trace_errors\": 296,\n      \"no_trace_dominant_pattern\": \"majority class bias + code complexity correlation\",\n      \"loop_only_errors\": 171,\n      \"tier1_tier2_error_jaccard\": 0.01,\n      \"cross_model_irreducible_overlap_jaccard\": 0.85\n    },\n    \"tables\": [\n      {\n        \"name\": \"Error mode distribution by condition (Qwen-7B seed42)\",\n        \"columns\": [\n          \"Condition\",\n          \"Total Errors\",\n          \"Error Rate\",\n          \"fail→pass (%)\",\n          \"pass→fail (%)\",\n          \"Dominant Failure Mode\"\n        ],\n        \"rows\": [\n          [\n            \"exception_only\",\n            2,\n            \"0.17%\",\n            \"0%\",\n            \"100%\",\n            \"GeneratorExit irreducible\"\n          ],\n          [\n            \"ae_only\",\n            1,\n            \"0.08%\",\n            \"0%\",\n            \"100%\",\n            \"GeneratorExit variant\"\n          ],\n          [\n            \"VOTA\",\n            7,\n            \"0.59%\",\n            \"57%\",\n            \"43%\",\n            \"Tier 2 noise conflict\"\n          ],\n          [\n            \"loop_only\",\n            171,\n            \"14.4%\",\n            \"36%\",\n            \"64%\",\n            \"Insufficient diagnostic signal\"\n          ],\n          [\n            \"full_trace\",\n            217,\n            \"18.2%\",\n            \"47%\",\n            \"53%\",\n            \"Information overload (length-correlated)\"\n          ],\n          [\n            \"label_only\",\n            164,\n            \"13.8%\",\n            \"65%\",\n            \"35%\",\n            \"Gradient dilution residual\"\n          ],\n          [\n            \"no_trace\",\n            296,\n            \"24.9%\",\n            \"70%\",\n            \"30%\",\n            \"Majority class bias\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Error rate by trace length bucket (full_trace)\",\n        \"columns\": [\n          \"Length_Bucket\",\n          \"N_Samples\",\n          \"Errors\",\n          \"Error_Rate\"\n        ],\n        \"rows\": [\n          [\n            \"<500 tok\",\n            \"~190\",\n            \"~17\",\n            \"~9%\"\n          ],\n          [\n            \"500-1000 tok\",\n            \"~340\",\n            \"~54\",\n            \"~16%\"\n          ],\n          [\n            \"1000-1500 tok\",\n            \"~370\",\n            \"~72\",\n            \"~19%\"\n          ],\n          [\n            \">1500 tok\",\n            \"~290\",\n            \"~96\",\n            \"~33%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Cross-condition error overlap (Jaccard, Qwen-7B)\",\n        \"columns\": [\n          \"Pair\",\n          \"Jaccard\",\n          \"Shared_Errors\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"exception_only ∩ VOTA\",\n            0.29,\n            2,\n            \"VOTA superset includes Tier 1 irreducible\"\n          ],\n          [\n            \"full_trace ∩ no_trace\",\n            0.36,\n            137,\n            \"63% of full_trace errors also in no_trace\"\n          ],\n          [\n            \"loop_only ∩ label_only\",\n            0.4,\n            95,\n            \"Similar difficulty: trace-as-context conditions\"\n          ],\n          [\n            \"Tier 1 ∩ Tier 2 errors\",\n            0.01,\n            0,\n            \"Qualitatively different failure modes\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Error analysis 为 3 个 Claims 提供 converging evidence：(1) exception_only  的 irreducible 2/1190 errors 跨模型重叠（Jaccard 0.85）确认是 data/ representation property（Claim 1 \\\"ceiling\\\" 论点）；(2) full_trace  error-length correlation r=0.41 是 information overload 的 direct  evidence（Claim 2）；(3) VOTA 的 5 个 Tier 2-attributable errors  quantify \\\"noise from combining tiers\\\"（Claim 3）。在 median 档下  这些发现 expected 但 useful——审稿人会 appreciate 对 error 的  systematic analysis，但不会视为 independent contribution。建议作为  Appendix B（~1 page: 1 table + 2 case studies + correlation plot）， main text 中引用关键数字（\\\"full_trace error rate correlates with  trace length, r=0.41, confirming information overload hypothesis\\\"）。 0 GPU-hours，纯分析，ROI 极高。\\n\\n\\nError analysis 在 median 档下揭示条件间 qualitatively different failure modes， 为现有 claims 提供 supporting evidence 但不产生新发现。推理链：\\n(1) exception_only 的 2 个 error (id=901, 905) 已被完全解释——GeneratorExit 是  Python all() 短路的 BaseException，tracer 统一标 [ERROR]。模型看到 7 行  [ERROR] GeneratorExit 合理预测 fail。这是 representation-inherent error， 非模型不足。跨 Qwen 3 seeds 完全重合确认是 data property。\\n(2) VOTA 额外 5 个 error 源自 Tier 2 noise：3 例中 loop compression 产生  正常行为摘要但同时存在 exception（矛盾信号让模型犹豫，confidence 下降）； 2 例中 Tier 2 tokens 稀释了对 exception 的 attention（输入更长，exception  信号占比更低）。这直接 quantify \\\"combining tiers introduces noise\\\" (Claim 3)。\\n(3) full_trace 的 217 个 error 中 ~63% 也是 no_trace 的错误——这些是  intrinsically hard cases，trace 未提供 accessible 的额外信号（signal  buried in thousands of tokens）。剩余 37% 是 full_trace unique errors—— trace 信息 actively misleading（长 trace 中的 intermediate exception  被 caught 但 trace 仍包含 [ERROR]，模型误判）或 attention 被长 context  分散。error rate 与 trace length 正相关 (r≈0.41)：>1500 tokens 的 trace  error rate ~33% vs <500 tokens ~9%，information overload 的 dose-response。\\n(4) Tier 1 和 Tier 2 的 error sets 几乎不重叠 (Jaccard=0.01)：Tier 1  fails 在 representation ambiguity (GeneratorExit)，Tier 2 fails 在  reasoning complexity (loop behavior interpretation)。\\n\"\n  },\n  {\n    \"name\": \"cross_model_calibration_exception_only\",\n    \"description\": \"4 models × exception_only ECE/Brier 对比\",\n    \"results\": {\n      \"qwen7b\": {\n        \"accuracy\": 0.9983,\n        \"ece\": 0.0027,\n        \"brier\": 0.0013,\n        \"mce\": 0.835\n      },\n      \"deepseek_seed42\": {\n        \"accuracy\": 0.9933,\n        \"ece\": 0.012,\n        \"brier\": 0.006,\n        \"mce\": 0.45\n      },\n      \"qwen15b\": {\n        \"accuracy\": 0.9983,\n        \"ece\": 0.005,\n        \"brier\": 0.003,\n        \"mce\": 0.62\n      },\n      \"codellama13b\": {\n        \"accuracy\": 0.9983,\n        \"ece\": 0.003,\n        \"brier\": 0.002,\n        \"mce\": 0.75\n      },\n      \"all_nonoutlier_ece_below\": 0.015,\n      \"ece_range\": [\n        0.0027,\n        0.012\n      ],\n      \"ece_ratio_vs_notrace_range\": [\n        14,\n        63\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Cross-model calibration for exception_only\",\n        \"columns\": [\n          \"Model\",\n          \"Accuracy\",\n          \"ECE\",\n          \"Brier\",\n          \"ECE ratio vs no_trace (0.171)\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen-2.5-Coder-7B\",\n            \"99.83%\",\n            0.0027,\n            0.0013,\n            \"63×\"\n          ],\n          [\n            \"CodeLlama-13B-Instruct\",\n            \"99.83%\",\n            0.003,\n            0.002,\n            \"57×\"\n          ],\n          [\n            \"Qwen-2.5-Coder-1.5B\",\n            \"99.83%\",\n            0.005,\n            0.003,\n            \"34×\"\n          ],\n          [\n            \"DeepSeek-Coder-6.7B\",\n            \"99.33%\",\n            0.012,\n            0.006,\n            \"14×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-model calibration 证实 exception signal 的 calibration 优势  不限于 Qwen-7B——所有 4 模型 ECE ≤ 0.012，与 no_trace ECE 0.171  相比 14-63× improvement。论文可 claim \\\"exception_only achieves  near-perfect calibration (ECE ≤ 0.012) across all tested models,  regardless of architecture and scale\\\"。这是独立于 accuracy 的  evidence dimension：即使审稿人质疑 99.83% 是 saturation，ECE/Brier  数据证明模型 \\\"knows what it knows\\\"——confidence 与 correctness  高度一致。DeepSeek 的略高 ECE (0.012) 与其更多 errors (8 vs 2)  一致，不 undermine overall finding。建议作为 main text Table  （与 accuracy table 并列或合并为一张大表），1 GPU-hour  investment，cost-effective。\\n\\n\\nCalibration 直接跟随 accuracy 和 error 数量。三个 99.83% 模型（Qwen-7B,  Qwen-1.5B, CodeLlama-13B）仅有 2 个相同 error（GeneratorExit），calibration  差异仅来自 confidence distribution 的模型间差异：\\nQwen-7B (ECE=0.0027, 已有数据): 基准。2 个 misclassified samples 的  confidence 贡献几乎全部 ECE。\\nCodeLlama-13B (ECE≈0.003): 13B 参数量产生更 peaked softmax distribution， correct predictions 的 confidence 更接近 1.0。2 个 error 的 confidence  也偏高（模型更 \\\"确定\\\"），但 overall 因 correct predictions 的 near-perfect  calibration 而 ECE 极低。略高于 Qwen-7B 因为 CodeLlama 的 chat template  与训练数据的 alignment 略有差异。\\nQwen-1.5B (ECE≈0.005): 同 Qwen tokenizer，same 2 errors。但 1.5B 模型的  softmax entropy 更高（small model less confident），correct predictions  的 mean confidence 可能在 ~0.95 而非 ~0.99，造成 systematic slight  under-confidence → ECE 略高。\\nDeepSeek seed42 (ECE≈0.012): 8 个 errors（vs others 的 2 个），4× 更多  misclassified bins 贡献 ECE。其中部分 fail samples 被高 confidence 预测为  pass（LoRA 训练不完全映射 exception→fail），这些 high-confidence wrong  predictions 是 ECE 的主要 contributor。但 0.012 仍远低于 no_trace 的 0.171  （14× improvement）。\\n总体：所有模型 ECE < 0.015，exception signal 的 calibration 优势跨模型  robust。magnitude 差异主要由 error count 驱动，非 signal quality 差异。\\n\"\n  },\n  {\n    \"name\": \"few_shot_frontier_baseline\",\n    \"description\": \"GPT-4o/Claude 0-shot + 3-shot verdict prediction baseline\",\n    \"results\": {\n      \"gpt4o_0shot_exception\": 0.952,\n      \"gpt4o_0shot_exception_ci\": [\n        0.937,\n        0.965\n      ],\n      \"gpt4o_3shot_exception\": 0.966,\n      \"gpt4o_3shot_exception_ci\": [\n        0.953,\n        0.977\n      ],\n      \"claude_0shot_exception\": 0.958,\n      \"claude_0shot_exception_ci\": [\n        0.944,\n        0.971\n      ],\n      \"claude_3shot_exception\": 0.972,\n      \"claude_3shot_exception_ci\": [\n        0.959,\n        0.982\n      ],\n      \"gpt4o_0shot_no_trace\": 0.805,\n      \"claude_0shot_no_trace\": 0.821,\n      \"sft_qwen7b_exception_only\": 0.9983,\n      \"sft_advantage_vs_best_frontier_pp\": 2.6,\n      \"sft_qwen15b_advantage_vs_gpt4o_pp\": 2.6,\n      \"api_cost_total_usd\": 18,\n      \"sft_inference_cost_usd\": 0.01\n    },\n    \"tables\": [\n      {\n        \"name\": \"SFT vs frontier few-shot comparison\",\n        \"columns\": [\n          \"Method\",\n          \"Model\",\n          \"Input\",\n          \"Shots\",\n          \"Accuracy\",\n          \"Errors/1190\",\n          \"Approx Cost\"\n        ],\n        \"rows\": [\n          [\n            \"SFT\",\n            \"Qwen-2.5-Coder-7B\",\n            \"exception_only\",\n            \"—\",\n            \"99.83%\",\n            2,\n            \"$0.01\"\n          ],\n          [\n            \"SFT\",\n            \"Qwen-2.5-Coder-1.5B\",\n            \"exception_only\",\n            \"—\",\n            \"99.83%\",\n            2,\n            \"$0.005\"\n          ],\n          [\n            \"SFT\",\n            \"CodeLlama-13B\",\n            \"exception_only\",\n            \"—\",\n            \"99.83%\",\n            2,\n            \"$0.02\"\n          ],\n          [\n            \"Few-shot\",\n            \"GPT-4o\",\n            \"exception_only\",\n            3,\n            \"96.6%\",\n            \"~40\",\n            \"$8\"\n          ],\n          [\n            \"Few-shot\",\n            \"Claude-3.5\",\n            \"exception_only\",\n            3,\n            \"97.2%\",\n            \"~33\",\n            \"$10\"\n          ],\n          [\n            \"Few-shot\",\n            \"GPT-4o\",\n            \"exception_only\",\n            0,\n            \"95.2%\",\n            \"~57\",\n            \"$5\"\n          ],\n          [\n            \"Few-shot\",\n            \"Claude-3.5\",\n            \"exception_only\",\n            0,\n            \"95.8%\",\n            \"~50\",\n            \"$7\"\n          ],\n          [\n            \"Few-shot\",\n            \"GPT-4o\",\n            \"no_trace\",\n            0,\n            \"80.5%\",\n            \"~232\",\n            \"$3\"\n          ],\n          [\n            \"Few-shot\",\n            \"Claude-3.5\",\n            \"no_trace\",\n            0,\n            \"82.1%\",\n            \"~213\",\n            \"$5\"\n          ],\n          [\n            \"SFT\",\n            \"Qwen-7B\",\n            \"no_trace\",\n            \"—\",\n            \"75.1%\",\n            296,\n            \"$0.01\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Error count perspective (补充审稿人 'gap only 2-3pp' 的 concern)\",\n        \"columns\": [\n          \"Model\",\n          \"Accuracy\",\n          \"Errors\",\n          \"Error Reduction vs frontier best\"\n        ],\n        \"rows\": [\n          [\n            \"SFT Qwen-7B exception_only\",\n            \"99.83%\",\n            2,\n            \"baseline\"\n          ],\n          [\n            \"Claude 3-shot exception_only\",\n            \"97.2%\",\n            \"~33\",\n            \"16.5× more errors\"\n          ],\n          [\n            \"GPT-4o 3-shot exception_only\",\n            \"96.6%\",\n            \"~40\",\n            \"20× more errors\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Frontier baseline 在 median 档下提供 solid but not overwhelming  evidence：SFT beats frontier 3-shot by ~2.6pp (error count 16-20×  reduction)。这足以 claim \\\"task-specific SFT on 7B model surpasses  frontier few-shot\\\" 但审稿人可能视 2.6pp 为 modest。Rebuttal 策略： (a) 强调 error count 而非 pp——\\\"from ~33 errors to 2 irreducible  errors\\\" 更有冲击力；(b) cost perspective——1800× cheaper；(c)  offline deployability。最有价值的发现：frontier models 也从  exception traces 大幅获益 (no_trace→exception: +14-15pp)， independent confirm Claim 1/2。建议 main text 用 1 paragraph +  1 table 呈现，full results 放 appendix。0 GPU-hours，仅 API  cost ~$18。如果 deadline 紧张可 deprioritize——核心 claims  不依赖此数据。\\n\\n\\nFrontier models 的 exception_only 0-shot 能达 95-96% 因为 task 在  exception_only 格式下高度 interpretable：有 [ERROR] → fail，无 [ERROR] →  pass。已有 local model zero-shot 数据（Qwen-1.5B 93.45%, DeepSeek 90.59%） 证明不需要 SFT 就能达到 ~90%+。Frontier models 更强的 instruction following  + 更广的 code knowledge 在此基础上再提升 ~3-5pp：\\n(1) GPT-4o 0-shot 95.2%：比 local Qwen-1.5B zero-shot (93.45%) 仅高 1.8pp ——exception task 对 model scale 的 marginal return 很低（进一步证明是  signal-limited not capacity-limited）。剩余 4.8% error 来自：GeneratorExit  等 non-fatal exceptions（同 SFT 模型）、format marker 的不一致解读、 边缘 case 的 conservative \\\"fail\\\" 偏好。\\n(2) 3-shot 额外 +1.4-1.4pp：exemplars 帮助建立 consistent decision  boundary，特别是处理 [No exception data in trace] marker 的一致性。 但 3 个 exemplars 无法覆盖 exception type 的 long-tail distribution。\\n(3) SFT Qwen-7B (99.83%) 仍高于 best frontier 3-shot (Claude 97.2%)  2.6pp。虽然 pp gap 不大，但 error count 差异显著：2 vs ~33 errors， 16.5× fewer mistakes。且 SFT inference cost 是 frontier API 的 ~1/1800。\\n(4) Frontier no_trace (80-82%) >> SFT no_trace (75.1%)：frontier model  的 code reasoning 能力可部分替代 trace 信息，但仍远低于 SFT +  exception_only (99.83%)——exception signal + SFT 的组合效果不可被  单纯 model scale 替代。\\n\"\n  },\n  {\n    \"name\": \"ood_generalization_cross_language\",\n    \"description\": \"不同编程语言/项目的 trace 上测试 exception_only 泛化性\",\n    \"results\": {\n      \"python_ood_exception_only\": 0.963,\n      \"python_ood_degradation_pp\": -3.5,\n      \"java_exception_only\": 0.918,\n      \"java_degradation_pp\": -8.0,\n      \"javascript_exception_only\": 0.902,\n      \"javascript_degradation_pp\": -9.6,\n      \"cross_lang_mean\": 0.928,\n      \"cross_lang_mean_degradation_pp\": -7.0,\n      \"python_ood_no_trace\": 0.715,\n      \"java_no_trace\": 0.68,\n      \"javascript_no_trace\": 0.665,\n      \"exception_lift_over_notrace_ood_mean_pp\": 24.1,\n      \"ood_test_set_size_per_lang\": 500\n    },\n    \"tables\": [\n      {\n        \"name\": \"In-distribution vs OOD accuracy by language\",\n        \"columns\": [\n          \"Language\",\n          \"Setting\",\n          \"exception_only\",\n          \"no_trace\",\n          \"Lift\",\n          \"Degradation vs ID\"\n        ],\n        \"rows\": [\n          [\n            \"Python\",\n            \"ID (HumanEval+MBPP)\",\n            \"99.83%\",\n            \"75.1%\",\n            \"+24.7pp\",\n            \"baseline\"\n          ],\n          [\n            \"Python\",\n            \"OOD (new projects)\",\n            \"96.3%\",\n            \"71.5%\",\n            \"+24.8pp\",\n            \"-3.5pp\"\n          ],\n          [\n            \"Java\",\n            \"OOD\",\n            \"91.8%\",\n            \"68.0%\",\n            \"+23.8pp\",\n            \"-8.0pp\"\n          ],\n          [\n            \"JavaScript\",\n            \"OOD\",\n            \"90.2%\",\n            \"66.5%\",\n            \"+23.7pp\",\n            \"-9.6pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"OOD 实验在 median 档下是最大 risk/reward 投资。如果完成，可 claim  \\\"exception signal advantage transfers across languages with preserved  lift (~24pp) despite moderate absolute degradation (7pp mean)\\\"—— 部分回应 single-task scope criticism。但 risk factors：(1) 需要  构建 3 个语言的 OOD 数据集（trace 生成 + 人工验证），timeline  紧张；(2) tracer 对 Java/JS 的 implementation 可能有 quality  issues，影响实验可控性；(3) 如果某语言降到 <85%，审稿人可能  反向 argue \\\"not robust enough\\\"。在 ARR May 25 deadline (7天后)  前几乎不可能完成——建议 deprioritize，标注为 camera-ready  supplement 或 future work。如果有余力，优先做 Python OOD  （无需新 tracer，仅需新测试集），~4 GPU-hours 即可。\\n\\n\\nOOD 泛化性取决于 exception signal 的 cross-language structural similarity。 [ERROR] type: ... message: ... 格式是 tracer 的统一输出规范，但 exception  type 名称和 error message 惯例跨语言不同，造成 token-level distribution shift。\\nPython OOD (-3.5pp, 96.3%): 同语言不同项目，exception type 分布与训练集  高度重叠（TypeError, ValueError, IndexError 是 universal），仅 project-specific  custom exception classes 造成少量降级。测试集项目的 test structure（pytest  fixtures、多文件 import）可能引入不同的 exception context，但 [ERROR] tag  的 binary signal 不受影响。\\nJava (-8.0pp, 91.8%): NullPointerException, ArrayIndexOutOfBoundsException 等  Java-specific type names 训练集未出现——模型无法利用 type-level semantics， 退化到依赖 [ERROR] tag presence 的 binary heuristic。但 binary heuristic  本身在 Qwen-7B zero-shot 上已达 ~89%，SFT 的 fine-tuned decision boundary  在新 type names 上部分失效。\\nJavaScript (-9.6pp, 90.2%): 最大降级。JS 的 error handling 更独特（Promise  rejection → UnhandledPromiseRejection, async TypeError），且 error message  格式与 Python 差异最大。tracer 对 JS 的 [ERROR] 标注可能不如 Python  consistent（implementation difference）。\\n关键：所有语言上 exception_only lift over no_trace ≈ 24pp（与 in-domain  24.7pp 几乎相同），证明 exception signal 的 fault detection mechanism  跨语言 transferable。Absolute degradation 来自 token vocabulary shift  而非 mechanism failure。\\n\"\n  },\n  {\n    \"name\": \"training_dynamics_learning_curves\",\n    \"description\": \"exception_only vs full_trace 的 learning curve（每 ~50 steps eval）\",\n    \"results\": {\n      \"exception_only_frac_to_90pct\": 0.05,\n      \"exception_only_frac_to_95pct\": 0.08,\n      \"exception_only_frac_to_99pct\": 0.2,\n      \"exception_only_curve_shape\": \"monotonic_rapid_saturation\",\n      \"vota_frac_to_90pct\": 0.1,\n      \"vota_frac_to_95pct\": 0.15,\n      \"vota_frac_to_99pct\": 0.3,\n      \"vota_curve_shape\": \"monotonic_moderate_saturation\",\n      \"full_trace_frac_to_80pct\": 0.3,\n      \"full_trace_peak\": {\n        \"accuracy\": 0.83,\n        \"epoch\": 1\n      },\n      \"full_trace_final\": 0.8176,\n      \"full_trace_curve_shape\": \"non_monotonic_epoch2_dip\",\n      \"no_trace_plateau_frac\": 0.15,\n      \"no_trace_plateau_accuracy\": 0.751,\n      \"no_trace_curve_shape\": \"rapid_plateau_low_ceiling\",\n      \"convergence_ratio_exception_vs_vota\": 1.9,\n      \"convergence_ratio_exception_vs_fulltrace\": 3.8,\n      \"learning_efficiency_exception_samples_per_pp\": 9.2,\n      \"learning_efficiency_fulltrace_samples_per_pp\": 68.5,\n      \"efficiency_ratio\": 7.4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Convergence milestones (fraction of total training)\",\n        \"columns\": [\n          \"Condition\",\n          \"To 80%\",\n          \"To 90%\",\n          \"To 95%\",\n          \"To 99%\",\n          \"Final Accuracy\",\n          \"Curve Shape\"\n        ],\n        \"rows\": [\n          [\n            \"exception_only\",\n            \"~3%\",\n            \"~5%\",\n            \"~8%\",\n            \"~20%\",\n            \"99.83%\",\n            \"Rapid saturation\"\n          ],\n          [\n            \"VOTA\",\n            \"~5%\",\n            \"~10%\",\n            \"~15%\",\n            \"~30%\",\n            \"99.41%\",\n            \"Moderate saturation\"\n          ],\n          [\n            \"full_trace\",\n            \"~30%\",\n            \"never\",\n            \"never\",\n            \"never\",\n            \"81.76%\",\n            \"Non-monotonic (epoch2 dip)\"\n          ],\n          [\n            \"loop_only\",\n            \"~12%\",\n            \"never\",\n            \"never\",\n            \"never\",\n            \"85.63%\",\n            \"Slow saturation\"\n          ],\n          [\n            \"no_trace\",\n            \"never\",\n            \"never\",\n            \"never\",\n            \"never\",\n            \"75.13%\",\n            \"Low-ceiling plateau\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Learning efficiency comparison\",\n        \"columns\": [\n          \"Condition\",\n          \"Effective Unique Samples\",\n          \"Lift (pp)\",\n          \"Samples per pp\",\n          \"Efficiency (relative)\"\n        ],\n        \"rows\": [\n          [\n            \"exception_only\",\n            2858,\n            24.7,\n            9.2,\n            \"1.0× (ref)\"\n          ],\n          [\n            \"VOTA\",\n            \"~5800\",\n            24.3,\n            17.5,\n            \"0.53×\"\n          ],\n          [\n            \"full_trace\",\n            \"~5800\",\n            6.6,\n            72.1,\n            \"0.13×\"\n          ],\n          [\n            \"no_trace\",\n            \"~5800\",\n            3.6,\n            132.8,\n            \"0.07×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Training dynamics 为 Claim 2 提供 process-level evidence（补充已有  outcome-level evidence）。核心 finding：exception_only 不仅 final  accuracy 最高，learning efficiency 也 7.4× higher——denser signal  → faster and better learning。full_trace 的 non-monotonic curve  （epoch2 dip from 83% to 76%）是 information overload 的 dynamic  manifestation：模型先学到 some useful trace patterns (epoch1 peak)， 然后 overfits to noise (epoch2 collapse)，部分恢复 (epoch3)。 这呼应 D1 (eval_loss vs accuracy decoupling)。\\n审稿人可能 challenge: \\\"faster convergence is trivially expected  for shorter sequences\\\"。Rebuttal: shorter sequences + diagnostic  signal concentration 共同作用——loop_only 的 sequence 长度与  full_trace 相当但 efficiency 5× higher (因 loop 信号 denser than  raw trace)，证明不只是 length effect。\\n建议作为 Figure in main text（visual impact 强）但不升为  standalone claim。需修改 train_sft.py 添加 intermediate eval  callback，8 GPU-hours。如果 deadline 紧张，可引用现有  epoch-level 数据（epoch1 vs epoch3）作为 coarse-grained proxy  代替 fine-grained learning curve。\\n\\nTraining dynamics 直接测量 information density 对 learning efficiency 的  影响。所有数值表示为 training fraction（0=start, 1.0=end of 3 epochs）， 因 absolute step count 取决于 batch size 等 hyperparameters。\\nexception_only 收敛最快（~5% training 达 90%, ~8% 达 95%）：input 极短  （mean <100 tokens），gradient 完全集中在 verdict signal 上；effective  unique 样本仅 2858，但 binary structure（有 exception→fail, 无→pass） 极其 learnable。已有 epoch-level 数据佐证：Qwen-7B exception_only 3  seeds 均在 epoch1 结束时已达 99.83%（之后 epochs 无提升）——暗示  实际在 epoch1 早期就已收敛。\\nfull_trace 收敛最慢且 non-monotonic：已有 epoch-level 数据  （epoch1=83.03%, epoch2=76.30%, epoch3=81.76%）展示 epoch2 坍塌。 中间 eval 应能捕获更 fine-grained 的 oscillation pattern。峰值在  ~30% training（epoch1 中后段），之后 overfitting 到 trace patterns  而非 verdict signal 导致 epoch2 下降。epoch3 partial recovery 可能  是 random fluctuation。\\nVOTA 介于两者之间：含 Tier 1 (fast learning) + Tier 2 (slow learning)  信号，combined curve 的前段被 Tier 1 驱动（快速上升到 >95%），后段  Tier 2 贡献边际提升。已有 epoch-level (epoch1=99.33%, epoch2-3=99.41%)  确认 epoch1 几乎完成所有学习。\\nno_trace 快速 plateau：无 trace signal 可学习，模型在 ~15% training  后耗尽 code→verdict 的弱 statistical correlation，之后 flat。\\nLearning efficiency ratio: exception_only 每 pp 需 ~9.2 个 effective  training samples（2858 unique / (99.83-75.13) pp），full_trace 需 ~68.5  （~5800 / (81.76-75.13) pp），7.4× 差距直接 quantify information  density 的 learning advantage。\\n\"\n  }\n]",
      "numLines": 871,
      "startLine": 1,
      "totalLines": 871
    }
  },
  "sourceToolAssistantUUID": "d126892a-1813-41c5-96d8-411385b00018",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T13:44:28.662Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UVsHSLc2RFiQkB83mqr79C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfccf144-7a99-4571-acf7-663a52367b6a",
  "isSidechain": false,
  "requestId": "req_011CbA8jnmaiF9tjNxuT7Ho9",
  "type": "assistant",
  "uuid": "f71b8fcb-c00b-4895-a98c-b1bda9210b88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hwn5VcuYpuSLxAMabALAMa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12940,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12940
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-st…",
  "leafUuid": "f71b8fcb-c00b-4895-a98c-b1bda9210b88",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper from experiment data",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c"
}
```

---

### Tool result

_source line 13 · 2026-05-18T13:44:29.008Z_

<details><summary>↩ Tool result · `toolu_01UVsHSLc2RFiQkB83mqr79C`</summary>

```text
1	# Paper Framing — trace-verdict-study
2	
3	> v3.0 — [UPDATED 2026-05-15] D030 CLOSED: DeepSeek VOTA 84.45% confirmed correct (confirmatory re-eval). **Critical narrative fix**: to_chat_text() preserves labels → VOTA 训练时 verdict label 未被截断 → 论文中 "label truncation/corruption" 措辞对 VOTA 不成立。正确叙事: trace INPUT content 被截断 (91.7% samples), 84.45% 反映 trace information loss。新增 D11: VOTA cross-model gap confounded by training-time truncation。数据集来源：HumanEval (164) + MBPP-sanitized (427) = 591 problems × 10 LLM-generated solutions = 5910 samples。
4	
5	## Target Venue
6	- Primary: EMNLP 2026 Main (ARR submission)
7	- Fallback: EMNLP 2026 Findings
8	- Deadline: ARR May 25, 2026
9	
10	## Core Insight
11	
12	Verdict prediction (pass/fail) is fundamentally a **fault detection** task. The most effective signal is the **exception event** — a compact, structured diagnostic moment that consistently outperforms all other trace representations across models (Qwen 99.83% ± 0.00 across 3 seeds; DeepSeek 91-99% depending on seed, but always > VOTA 84.45% and no_trace 73.36%). In contrast, richer trace representations that require deeper execution reasoning show model-dependent effectiveness: VOTA gap = 14.96pp, no_trace gap = 1.77pp. Information density — not training signal distribution — is the primary bottleneck: even oracle loss masking (label-only) cannot close the 13pp gap between full traces and targeted extraction. The design principle: **extract the highest-specificity diagnostic signal; discard everything else.** Cross-model absolute performance depends on LoRA initialization stability, but exception_only's relative dominance over other components is robust.
13	
14	VOTA's primary contribution is **fault indicator isolation** — automatically extracting exception events from noisy full traces — rather than generic trace compression. The "compression helps" narrative was a stepping stone; the real mechanism is diagnostic signal extraction.
15	
16	## Core Claims (3)
17	
18	### Claim 1: Exception events are the most effective trace component for verdict prediction
19	
20	Exception summaries consistently achieve the highest verdict prediction accuracy across both models tested, outperforming all other trace representations in every seed. On Qwen-2.5-Coder-7B, performance is perfectly robust: 99.83% ± 0.00 (3 seeds). On DeepSeek-Coder-6.7B, absolute accuracy is seed-dependent (seed42=99.83% epoch1, seed123=91.43% epoch1; Δ=8.40pp), consistent with LoRA initialization sensitivity — but exception_only still dominates VOTA (84.45%) and no_trace (73.36%) in all seeds. This contrasts with VOTA (cross-model gap = 14.96pp) and no_trace (gap = 1.77pp). Exception events are structurally simple (`[ERROR] type: ... message: ...`) and do not require deep trace reasoning.
21	
22	**Supporting evidence:**
23	- `vota_exception_only_seed42_v2`: Qwen 99.83%, ECE=0.0027
24	- `deepseek_exception_only_seed42`: DeepSeek 99.83% (epoch1) / 99.33% (epoch3)
25	- `deepseek_exception_only_seed456`: DeepSeek 99.33% (epoch3), CI [98.82, 99.75] — 与 seed42 完全一致
26	- `deepseek_exception_only_seed123`: DeepSeek 91.43% (epoch1) / 91.09% (epoch3) — LoRA init sensitivity outlier
27	- `deepseek_vota_seed42`: DeepSeek VOTA 84.45% (gap = 14.96pp vs Qwen)
28	- `deepseek_no_trace_seed42`: DeepSeek no_trace 73.36% (gap = 1.77pp vs Qwen)
29	- `vota_no_ae_seed42`: 99.41% — actual/expected removal 不降，非 trivial string comparison
30	
31	**DeepSeek seed analysis** ✅ (FINALIZED, D029):
32	
33	| Seed | Epoch 3 (final) | fail_recall | pass_recall | train_loss | Errors | CI |
34	|------|-----------------|-------------|-------------|------------|--------|-----|
35	| 42   | 99.33%          | 1.0         | 0.9906      | —          | 8/1190 | — |
36	| 456  | 99.33%          | 1.0         | 0.9906      | 0.1225     | 8/1190 | [98.82, 99.75] |
37	| 123  | 91.09%          | 0.705       | 0.993       | 0.122      | —      | [89.4, 92.6] |
38	
39	seed42 与 seed456 结果**完全一致**（均 8/1190 错误，99.33%），seed123 为离群值。seed123 的 fail_recall 仅 0.705 — LoRA 初始化落入差的局部最优，未充分学到 exception→fail 映射。**关键发现**: seed456 和 seed123 的 train_loss 几乎相同（0.1225 vs 0.122），但 accuracy 差 8.2pp — token-level loss 掩盖了 sample-level 分类能力的巨大差异（详见 D10）。
40	
41	**Irreducible error analysis** ✅: 3 seeds 错误的 2 个样本 (id=901, 905) 均来自 HumanEval/95 (`check_dict_case`)，根因为 Python `all()` 对 generator expression 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误）。tracer 将其标记为 `[ERROR]`，exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。整个 1190 条测试集仅这 2 条含 `GeneratorExit`，模型无训练信号学习其良性本质。**这确认 99.83% 是 exception_only 表征的理论上限，剩余 0.17% 是 representation-inherent irreducible error，而非模型不足。**
42	
43	**Seed robustness** ✅: Qwen exception_only 3-seed 完全一致，构成本文最强 robustness 证据：
44	
45	| Seed | Accuracy | 95% CI | Errors |
46	|------|----------|--------|--------|
47	| 42 | 99.83% | [99.58, 100] | 2/1190 |
48	| 123 | 99.83% | [99.58, 100] | 2/1190 |
49	| 456 | 99.83% | [99.58, 100] | 2/1190 |
50	
51	3 seeds 错误样本 100% 重叠（id=901, 905, 均为 `check_dict_case` 函数, label=pass → pred=fail）。**Irreducible samples**: 模型已达数据集理论上限，variance = 0。
52	
53	**DeepSeek cross-model** ✅ (D029): 3-seed 完整数据 — seed42/456=99.33%, seed123=91.09%。2/3 seeds 鲁棒，seed123 为 LoRA 初始化离群值（fail_recall 仅 0.705）。Qwen 3-seed 完美稳定 (99.83% ± 0.00) vs DeepSeek 高方差（σ≈4.8pp），暗示 exception signal 的 learnability 与模型 LoRA 训练稳定性相关。但即使最差 seed (91.09%) 仍优于 VOTA (84.45%) 和 no_trace (73.36%)，relative dominance robust。
54	
55	### Claim 2: Information density, not gradient dilution, drives trace compression benefit
56	
57	Full traces help verdict prediction (81.76% [`full_trace_seed42_v5`], +6.6pp over baseline), but VOTA achieves 99.41% [`vota_seed42_v5`] (+24.3pp) — a +17.6pp advantage. Label-only loss ablation (plan_002) quantifies the causal decomposition: **gradient dilution contributes ~26% of the gap** (4.5pp; label-only full_trace = 86.22% [`full_trace_label_only_seed42`]), **information overload contributes ~74%** (13.0pp; only trace compression resolves this). Even with oracle loss masking that eliminates gradient dilution, full traces still underperform VOTA by 13pp.
58	
59	Cross-model evidence reinforces this: VOTA gap (14.96pp) partly tracks base model execution reasoning capability (Qwen CRUXEval-I 56.5% vs DeepSeek 39.0%, Δ=17.5pp), though **confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated to ~2048 tokens; see D11). The two factors cannot be disentangled in the current design. Exception signal partially bypasses both bottlenecks (token-short, no truncation; consistently best component on both models), though DeepSeek shows seed-dependent absolute performance (91-99%).
60	
61	**Supporting evidence:**
62	- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (gradient dilution fix, +4.5pp over standard full_trace)
63	- `full_trace_seed42_v5`: 81.76%, ECE=0.0958 (standard full_trace)
64	- `vota_seed42_v5`: 99.41%, ECE=0.0054
65	- `deepseek_vota_seed42`: 84.45% (VOTA model-dependent)
66	- CRUXEval literature data (Wang et al.)
67	
68	### Claim 3: Two-tier diagnostic hierarchy for verdict prediction
69	
70	Component ablation reveals verdict-relevant trace information has a strict two-tier hierarchy:
71	- **Tier 1 — diagnostic moment signals**: exception summaries (99.83% [`vota_exception_only_seed42_v2`]) and assertion-point information (99.92% [`vota_ae_only_seed42`]) are individually near-perfect and sufficient for verdict prediction on Qwen. These signals are structurally simple and consistently the most effective component on both models, though DeepSeek absolute performance is seed-dependent.
72	- **Tier 2 — behavioral patterns**: loop compression (85.63% [`vota_loop_only_seed42`]) carries substantial signal but is model-dependent and fully subsumed by Tier 1.
73	
74	Combining tiers introduces noise rather than helping: exception_only (99.83%) > VOTA full (99.41%), p=0.01. Loop_only ≈ full_trace_label_only (85.63% vs 86.22%) confirms VOTA's loop compression precisely extracts the useful behavioral signal from full traces.
75	
76	**Supporting evidence:**
77	- `vota_exception_only_seed42_v2`: 99.83%, ECE=0.0027 (Tier 1 exception)
78	- `vota_ae_only_seed42`: 99.92%, ECE=0.0004 (Tier 1 assertion-point, 与 exception 统计等价 p=0.80)
79	- `vota_loop_only_seed42`: 85.63%, ECE=0.0831 (Tier 2 behavioral)
80	- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (≈ loop_only, confirming extraction equivalence)
81	- `deepseek_exception_only_seed42`: 99.83% epoch1 / 99.33% epoch3 (Tier 1 cross-model validation)
82	- `deepseek_vota_seed42`: 84.45% (Tier 1+2 cross-model: Tier 2 introduces model-dependent degradation)
83	
84	**Calibration**: 完整 calibration 数据确认 Tier 1 信号不仅 accuracy 近完美，置信度校准也近完美：
85	
86	| Condition | Accuracy | ECE | Brier | 解读 |
87	|-----------|----------|-----|-------|------|
88	| ae_only | 99.92% | 0.0004 | 0.0008 | 近乎完美校准 |
89	| exception_only | 99.83% | 0.0027 | 0.0013 | 近乎完美校准 |
90	| VOTA | 99.41% | 0.0054 | 0.005 | 优秀，但 Tier 2 引入轻微 noise |
91	| loop_only | 85.63% | 0.0831 | — | Tier 2 单独校准中等 |
92	| label_only | 86.22% | 0.1107 | — | gradient dilution fix 仍 miscalibrated |
93	| full_trace | 81.76% | 0.0958 | — | 中度 miscalibrated |
94	| no_trace | 75.13% | 0.1715 | 0.1972 | 严重 miscalibrated |
95	
96	no_trace ECE 是 exception_only 的 **~63x**（0.1715/0.0027），Brier 是 **~150x**（0.1972/0.0013）。Trace signal（尤其 Tier 1）不仅提升 accuracy，更从根本上改善模型 calibration。
97	
98	**Design principle**: verdict-optimized traces should extract highest-specificity diagnostic signals; lower-specificity signals are redundant and may introduce noise.
99	
100	## Cross-Model Evidence Summary
101	
102	| Condition | Qwen-2.5-Coder-7B | DeepSeek-Coder-6.7B | Cross-model gap | Interpretation |
103	|-----------|-------------------|---------------------|-----------------|----------------|
104	| exception_only | 99.83% ± 0.00 (3 seeds) | seed42/456: 99.33%; seed123: 91.09% | 0.50-8.74pp (seed-dependent) | **Best component on both models**; 2/3 DeepSeek seeds match Qwen-level; 1 outlier still > VOTA |
105	| VOTA | 99.41% | 84.45% | -14.96pp | Model-dependent — requires execution reasoning; **also confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated from mean 2626 to ~2048 tokens; labels preserved via to_chat_text(), see D11) |
106	| no_trace | 75.13% | 73.36% | -1.77pp | Baseline gap tracks general capability |
107	| full_trace | 81.76% | collapsed (v3 pending) | N/A | DeepSeek v1 label truncation bug |
108	
109	**Key insight**: Exception_only is consistently the best component on both models (even worst DeepSeek seed 91.09% > VOTA 84.45%). Cross-model gap 与 signal complexity 正相关, but exception signal's absolute effectiveness also depends on LoRA training stability. Qwen: perfectly robust (3 seeds identical). DeepSeek: 2/3 seeds at 99.33% (matching Qwen-level), 1 outlier at 91.09% (LoRA initialization). Median performance robust; seed sensitivity suggests smaller/weaker models may need training stabilization (multi-seed selection, warmup tuning) for optimal exception signal utilization.
110	
111	## VOTA Repositioning
112	
113	**旧叙事**: VOTA 是 trace compression 方法，价值在于"压缩使 trace 更有效"。
114	
115	**新叙事**: VOTA 是 **fault indicator isolation** 方法，核心价值在于自动从 noisy execution traces 中提取 exception events 等 diagnostic signals。
116	
117	**证据链**:
118	1. exception_only (99.83%) ≥ VOTA full (99.41%) — 压缩后的其他组件（loop, ae）不仅无益，反而引入 noise
119	2. VOTA 跨模型 gap = 14.96pp — 因为 VOTA 包含 model-dependent 的 Tier 2 组件（loop compression 需要 execution reasoning）
120	3. exception_only 在两个模型上均为最优组件 — isolate 出 Tier 1 后，相对优势 robust（虽然 DeepSeek 绝对值 seed-dependent）
121	4. vota_no_ae (99.41%) = VOTA (99.41%) — actual/expected 移除无影响，exception 是真正的 active ingredient
122	
123	**论文中的表述**: "VOTA's trace compression pipeline incidentally isolates exception events — the minimal sufficient diagnostic signal. Its value lies not in making traces shorter, but in separating high-specificity fault indicators from low-specificity behavioral patterns."
124	
125	**对 Method section 的影响**: VOTA 仍然完整描述（loop compression + exception + actual/expected），但 Results/Discussion 明确指出 exception isolation 是核心机制，其他组件是 model-capability-dependent bonus。
126	
127	## Story Spine
128	
129	- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited, model-dependent benefit. No prior work has tested trace SFT on verdict tasks (binary pass/fail), nor identified what trace components drive classification performance.
130	
131	- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding that "no single trace representation consistently outperforms others." TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. TRACED (ICSE 2024) showed traces help encoder-based classification. All existing trace formats are designed for execution simulation, not fault detection.
132	
133	- **Our framing**: We reframe verdict prediction as **fault detection** and ask: what is the minimal sufficient diagnostic signal? Through systematic component ablation across two architecturally distinct models, we discover that exception events — compact, structured error summaries — are consistently the most effective trace component, achieving near-perfect accuracy on Qwen (99.83% ± 0.00, 3 seeds) and outperforming all alternatives on DeepSeek (91-99% vs VOTA 84.45%). Richer trace representations work only when the base model has sufficient execution reasoning capability, making them unreliable for general deployment.
134	
135	- **Headline result**: "Exception events consistently achieve the highest verdict accuracy across models (Qwen 99.83%, DeepSeek 91-99%), outperforming VOTA traces (84.45% on DeepSeek, -14.96pp gap) — demonstrating that fault indicator isolation, not trace reasoning, is the robust mechanism for verdict prediction. DeepSeek seed sensitivity reveals LoRA training stability as a secondary factor for smaller models."
136	
137	## Story Arc
138	
139	1. **Setup**: Trace SFT for code tasks — promising but inconsistent in prior work (DCSH, TracePile). Unknown whether traces help verdict tasks and what trace design matters.
140	
141	2. **First result — traces help, compression helps more** (single model): no_trace 75.13% → full_trace 81.76% → VOTA 99.41%. Label-only loss ablation decomposes the gap: 26% gradient dilution, 74% information overload. Compression improves accuracy through higher information density, not just cost savings.
142	
143	3. **Twist — what component actually drives VOTA?** Component ablation reveals exception_only (99.83%) ≥ full VOTA (99.41%). The "trace reasoning" narrative is wrong — verdict prediction is fault detection. Tier 1 (exceptions + assertion-point) subsumes Tier 2 (loops). Actual/expected removal doesn't hurt (99.41%).
144	
145	4. **Cross-model stress test — consistent dominance, not universal perfection**: Exception_only is the best component on both models (even DeepSeek worst seed 91.09% > VOTA 84.45%), but absolute performance is seed-dependent on DeepSeek (91-99% vs Qwen's perfectly stable 99.83%). VOTA degrades by 14.96pp. The structurally simplest component is the most robust, but LoRA initialization sensitivity introduces variance on weaker models. Qwen seed robustness (3-seed variance = 0) + calibration (ECE=0.0027) 确认 exception signal 在强模型上的 reliability。DeepSeek seed sensitivity 揭示 training stability 作为 secondary bottleneck。
146	
147	5. **Design principle**: For verdict tasks, identify the highest-specificity diagnostic signal (exception events) and discard everything else. VOTA's value is fault indicator isolation — automatically extracting exceptions from noisy traces — not generic compression. Simpler signals are more robust; complexity tolerance depends on model capability.
148	
149	## Dataset Characteristics
150	
151	### Data duplication analysis
152	
153	| Condition | Total | Unique | Duplication rate | Cause |
154	|-----------|-------|--------|------------------|-------|
155	| exception_only_train | 4720 | 2858 | 39.45% | 同题多个 passing 解映射为相同 (input, output) — 无异常 → 同一 trace |
156	| exception_only_test | 1190 | 607 | 48.99% | 同上 |
157	| raw_traces | 5910 | 5803 | 1.81% | 完整 trace 含行号/变量值/内存地址，几乎不重复 |
158	
159	**Train-test input overlap: 0（无数据泄漏）**
160	
161	**解读**: exception_only 高重复率是 representation 的自然属性，非数据问题。多个正确解对同一测试用例执行时若均无异常，exception_only 表征退化为相同的空/无异常标记。这恰好说明 exception signal 的 compactness — 它仅编码 fault presence，不编码 solution identity。raw_traces 重复率极低 (1.81%) 因为完整 trace 包含 solution-specific 信息（变量值、内存地址）。尽管高重复率意味着有效训练样本少于名义数量，模型仍达 99.83% — 进一步确认 exception signal 的 learnability。
162	
163	## DeepSeek full_trace 处理
164	
165	**现状**: v1 坍塌（28.5%, 100% 预测 fail, 根因: 训练端 label 截断）。v2 重训启动但被 kill（Loop #6 ops worker 腾 GPU 给 vota_seed456）。v3 RUNNING（label-preserving truncation fix）。
166	
167	**处理方案**: v3 正在 cuda:0 上训练，预计 5/16 完成。
168	
169	**VOTA vs full_trace 截断机制区分** (D030 token analysis 确认):
170	- **full_trace v1**: SFTTrainer right-truncation 切掉了 verdict **label** → 100% predict fail → 坍塌。根因: DeepSeek tokenizer 对 full_trace 产生 >2048 tokens, label 在截断窗口外。
171	- **VOTA**: `to_chat_text()` 保留 verdict label（label 完整），但 91.7% 的样本 **trace content（input）被截断**（mean 2626 → ~2048 tokens）。84.45% 是真实结果，反映 trace 信息损失对模型学习的影响，**不是** label corruption。
172	- **exception_only**: token 长度远低于 2048，不受截断影响，跨模型对比 clean。
173	
174	**对论文叙事的影响**: 论文中所有 "right-truncation corrupts/removes the verdict label" 措辞**对 VOTA 不成立**——label 完整保留，被截断的是 trace input。正确表述: "trace content truncation causes information loss"。VOTA cross-model gap (14.96pp) 有两个贡献因素: (1) model capability, (2) training-time trace truncation on DeepSeek (see D11)。
175	
176	## External Benchmark (DebugBench) Positioning
177	
178	**DebugBench 仅作泛化性验证，不作 trace importance 证据。**
179	
180	| Condition | Main Dataset | DebugBench | Δ interpretation |
181	|-----------|-------------|------------|------------------|
182	| no_trace | 75.13% | 96.71% | DebugBench 天花板高，baseline 已强 |
183	| VOTA | 99.41% | 99.77% | +3.06pp lift — 边际 |
184	| exception_only | 99.83% | 100.00% | +3.29pp lift — 边际 |
185	
186	**主数据集 trace lift = 24.70pp**（no_trace → exception_only），DebugBench trace lift 不到其 1/7。
187	
188	**论文定位规则**：
189	- DebugBench → 泛化性证据（exception_only 100% = 跨数据集鲁棒性）
190	- Trace importance 论证 → 仅依赖主数据集（24.7pp lift）
191	- 禁止用 DebugBench 的 3.29pp lift 论证 "trace 的核心价值"——审稿人会攻击天花板效应
192	
193	## Venue Fit Risks
194	
195	| Risk | Assessment | Mitigation |
196	|------|-----------|------------|
197	| 单任务 | 仍然只在 test verdict prediction 上验证 | 跨模型验证部分弥补; Discussion 中讨论 generalization |
198	| 单数据集 | HumanEval + MBPP-sanitized 是唯一数据源 (591 problems × 10 solutions) | 定位为 empirical study, 深度优于广度; 两个标准 benchmark 组合覆盖多样编程题型; exception_only 有效训练样本仅 2858 unique 即达 99.83%, 暗示 signal 的 simplicity 降低对数据量的依赖 |
199	| "只是 feature engineering" | exception extraction 不复杂 | simplicity 本身是 contribution — 最简信号最 robust |
200	| Negative result 味道 | VOTA 跨模型不 robust | Reframe: 识别 robust vs non-robust 组件边界是 positive |
201	| Seed robustness (Qwen) | ✅ 已解决: 99.83% ± 0.00 (3 seeds), irreducible samples 确认 | — |
202	| Seed robustness (DeepSeek) | ✅ 3-seed 完整: 2/3 at 99.33%, 1 at 91.09% | LoRA initialization sensitivity — median robust, worst still > all alternatives; 转化为 training stability finding (D9/D10) |
203	| Calibration | ✅ 完整数据: Tier 1 ECE≤0.003, no_trace ECE=0.171 (~63x gap) | Brier ~150x gap 进一步确认 |
204	| 只用 2 个模型 | 有限但有意义的 diversity | Architecture + pretraining data (5.5T vs 2T) + CRUXEval gap (17.5pp) 构成充分差异 |
205	| 数据重复率 | exception_only 训练集 39.45% 重复 | 非数据泄漏（train-test overlap = 0）；是 representation compactness 的自然结果；有效样本仍足够学习 |
206	
207	## Anticipated Reviewer Concerns
208	
209	| Concern | Planned Response |
210	|---------|-----------------|
211	| "exception_only 99.83% 是不是 trivial pattern matching [ERROR] 有无？" | full_trace 也包含 [ERROR] 但仅 81.76%——模型需要从 trace context 中 extract 和 utilize exception signal, 不是简单 keyword detection. no_trace 无 exception, 75.13%. |
212	| "为什么 exception_only > VOTA? adding info 反而降?" | 非 exception 组件 (loop/ae tokens) 稀释 attention 对 exception 信号的聚焦. Calibration: exception_only ECE=0.0027 vs VOTA ECE=0.0054. 部分样本 loop 正常但有 exception, 引入矛盾信号. |
213	| "CRUXEval gap 与 VOTA gap 的相关性可能是 coincidence" | 明确标注为 hypothesis. 列出 alternatives (tokenizer efficiency, pretraining scale 2.75x, chat template). 不 overclaim. |
214	| "只有 2 个模型，universality claim 太强" | 同意是 limitation. 两模型在 architecture (RoPE vs ALiBi), pretraining data (5.5T vs 2T), execution reasoning (CRUXEval 17.5pp gap) 上有充分差异, 不是 trivial replication. Exception signal 的 structural simplicity 提供 inductive argument for broader generalization. |
215	| "99.83% 可能 saturated, 看不出 exception 到底学了什么" | Calibration 双指标: exception_only ECE=0.0027, Brier=0.0013 (近完美校准). 对比 no_trace ECE=0.1715, Brier=0.1972 (~63x/~150x gap). **Irreducible error 根因已明确**: 2/1190 errors 均因 Python `all()` 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误），tracer 将其标记为 `[ERROR]`。模型看到 7 行 `[ERROR] GeneratorExit` 合理预测 fail，但代码实际正确。整个测试集仅这 2 条含 `GeneratorExit`，无训练信号可学习其良性本质。99.83% 是 representation 的理论上限，非 saturation artifact。 |
216	| "只用了 1 个 seed" | Qwen ✅: 3 seeds 99.83% ± 0.00. DeepSeek ✅: 3 seeds 完整 — seed42/456=99.33%, seed123=91.09%。2/3 鲁棒，1 离群。median=99.33%, worst=91.09% (仍 > VOTA 84.45%)。论文透明报告所有 seeds，将 seed sensitivity 转化为 LoRA training stability 的 finding（D9）。 |
217	| "eval_loss 上升但 accuracy 提升——checkpoint selection 有问题?" | Discussion D1: token-level loss 与 binary verdict accuracy 解耦. 推荐 verdict-specific metric. Methodological contribution. |
218	| "DeepSeek full_trace 坍塌是 bug 不是 finding" | 诚实披露根因 (训练端 label 截断). 其他 3 条件不受影响. 修复版本如就绪则补入. |
219	| "calibration 数据只有 1 个 seed" | Seed robustness 已证明 accuracy variance=0 (3 seeds), calibration 在 accuracy 完全一致的前提下 expected 也一致. ECE/Brier 的极小值 (0.0027/0.0013) 留有极小 variance 空间. |
220	| "DeepSeek epoch1 > epoch3, 为什么用 epoch3 报告?" | 正文报告所有 seeds 的 final + best checkpoint。seed42: epoch1=99.83%, epoch3=99.33%。seed123: epoch1=91.43%, epoch3=91.09%。D7 讨论 early stopping + D9 讨论 LoRA initialization sensitivity。不 cherry-pick best seed。 |
221	| "DeepSeek seed sensitivity 说明 exception signal 不 robust" | Exception_only 在所有 seeds 上仍优于其他条件（worst seed 91.09% > VOTA 84.45%）。Seed sensitivity 是 LoRA training 问题而非 signal 问题——Qwen 3 seeds 完美证明 signal 本身 robust。D9 讨论 training stabilization 作为 practical recommendation。 |
222	| "exception_only 数据集 ~40-49% 重复，有效训练样本不足？" | 重复源自 representation compactness：同题多个 passing 解均无异常 → 相同 trace。**非数据泄漏**（train-test input overlap = 0）。raw_traces 仅 1.81% 重复，确认重复是 exception_only 表征特性而非数据收集问题。模型在有效样本仅 2858 unique 的条件下仍达 99.83%，反而说明 exception signal 的高 learnability — 少量 unique 样本即可充分学习 fault detection pattern。 |
223	
224	## Discussion 要点
225	
226	### D1: eval_loss vs verdict accuracy 解耦
227	DeepSeek VOTA: eval_loss epoch1→3 从 0.068 升至 0.112 (+65%), 但 accuracy 从 78.15% 升至 84.45% (+6.3pp). Token-level calibration 与 binary classification accuracy 方向相反. **Implication**: verdict tasks 应用 task-specific metric (accuracy/F1) 做 checkpoint selection, 非 eval_loss.
228	
229	### D2: CRUXEval gap 假说 (revised — D030 confound)
230	VOTA 跨模型 gap (14.96pp) 与 CRUXEval execution reasoning gap (15-17.5pp) 数值吻合. 假说: trace utilization effectiveness 受 base model "execution reasoning readiness" 约束. **标注**: hypothesis, N=2, 列出 alternatives. 不 overclaim. **注意**: 我们的训练/测试数据来自 HumanEval + MBPP-sanitized（非 CRUXEval），CRUXEval-I 分数仅作为衡量两个模型 execution reasoning 能力差异的外部参照。论文中必须明确区分数据来源与外部基准引用。**D030/D034 truncation evidence**: 14.96pp gap 中截断效应有因果证据: group_analysis 显示 train-truncated 83.04% vs train-intact 100% (Fisher p≈0, 推理时无截断)。截断因果方向可 claim，模型能力差异是 residual confound。CRUXEval gap 数值吻合可能部分巧合。论文中截断效应应作为 established factor 讨论（有 group_analysis 因果证据），模型能力假说标注为 residual confound hypothesis。
231	
232	### D3: Simplicity as robustness (revised)
233	Exception signal 在两模型上均为最优组件，其结构简单性确保了相对优势的跨模型 robustness。但 DeepSeek seed sensitivity 揭示：simplicity 确保 signal 本身 robust，但 LoRA 训练过程是否稳定收敛到正确映射取决于模型。**trace design 应匹配 deployment model 的能力下界**，且需关注 training stability（建议：多 seed 验证 + 考虑 training stabilization 技巧如 warmup、learning rate schedule）。
234	
235	### D4: Checkpoint selection 与 gap 报告 (revised)
236	正文报告所有 seeds 的 final checkpoint 结果 + best checkpoint 结果，不 cherry-pick。DeepSeek seed42: epoch1=99.83%, epoch3=99.33%（退化 0.50pp）。DeepSeek seed123: epoch1=91.43%, epoch3=91.09%（退化 0.34pp）。两个 seed 均显示轻微 epoch 退化，但核心差异在 epoch1 起点（8.40pp gap），不是训练过程。
237	
238	### D5: Irreducible samples — GeneratorExit 根因分析
239	3 seeds 的 2/1190 errors 完全相同（id=901, 905, 均来自 HumanEval/95 `check_dict_case`），方向一致（pass→fail false negatives）。
240	
241	**根因**: Python `all()` 对 generator expression 短路时丢弃未耗尽的 generator，触发 `GeneratorExit`。`GeneratorExit` 继承自 `BaseException`（非 `Exception`），是 Python 内部控制流机制而非真正错误。但 tracer 对所有 caught exceptions 统一标记 `[ERROR]`，导致 exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。
242	
243	**为何不可约**:
244	1. **表征局限**: exception_only 条件下模型仅见异常数据，无法访问控制流、返回值或 assertion 结果。`GeneratorExit` 在此表征中与真正错误不可区分。
245	2. **跨 seed 确定性**: 3 个 random seeds 产生完全相同的 errors，确认这是 data/representation 属性而非模型初始化随机性。
246	3. **训练集无信号**: 整个 1190 条测试集仅这 2 条含 `GeneratorExit`，训练集中也缺乏足够的 `GeneratorExit` 良性样本供模型学习。
247	4. **人类也会犯错**: 仅看 exception trace（7 行 `[ERROR]`），人类审查者在不了解 Python generator protocol 的情况下也会预测 fail。
248	
249	**对论文的意义**: (1) 99.83% 是 exception_only representation 在此数据集上的理论 ceiling，非 saturation artifact；(2) 揭示 tracer 设计的改进方向——区分 `BaseException` 子类（如 `GeneratorExit`, `KeyboardInterrupt`）与 `Exception` 子类（真正的程序错误）可消除此类 irreducible error；(3) 提供 concrete evidence 说明 exception_only 模型"理解"的是 `[ERROR]` tag 的 fault indicator 语义，而非 exception type 的 fine-grained 含义。
250	
251	### D6: Calibration as secondary evidence
252	Calibration 数据提供独立于 accuracy 的 evidence dimension。no_trace Brier=0.1972 说明模型无 trace 时不仅预测错，且对错误预测过度自信。exception_only Brier=0.0013 说明模型在有 exception signal 时几乎完美区分确定性和不确定性。这支持 Claim 1 的 "sufficient signal" 论点——exception 不仅让模型预测对，还让模型 "知道自己对"。
253	
254	### D7: Early stopping for exception signal (revised — D030 epoch1 data complete)
255	3-seed epoch1 完整数据：seed42 epoch1=99.83% → epoch3=99.33%（-0.50pp）；**seed456 epoch1=99.33% → epoch3=99.33%（0.00pp）**；seed123 epoch1=91.43% → epoch3=91.09%（-0.34pp）。**seed42 的 epoch1=99.83%（匹配 Qwen）是该 seed 独有的 LoRA 初始化运气，不是 DeepSeek epoch1 的通用属性。** seed456 epoch1=epoch3 说明 epoch 退化非普遍现象。核心差异仍是 LoRA 初始化（epoch1 起点差 8.40pp），不是 overfitting。Early stopping 无法挽救差的初始化（seed123）。**Implication**: (1) 报告 DeepSeek 结果时应使用 median/2-of-3 (99.33%)，不应以 seed42 epoch1=99.83% 作为 headline；(2) epoch1 peak 是 LoRA 初始化运气的副产物，不具推广性。对比: VOTA 在 DeepSeek 上 84.45% **已确认正确**（D030 关闭: confirmatory re-eval max_length=16384 → 84.45%，与原始训练评估精确一致；D030 根因是 evaluate.py v2 的 max_length=2048 eval-time 截断 bug 导致 82.6% 预测为 garbage tokens）。
256	
257	### D9: LoRA initialization sensitivity as secondary bottleneck [NEW — D028]
258	DeepSeek exception_only seed42=99.83% vs seed123=91.43% (epoch1), 8.40pp gap。Qwen 3 seeds 完全一致。假说：exception signal 的 learnability 取决于 (1) signal 本身的结构简单性（cross-model robust）+ (2) LoRA 初始化是否落入能正确映射 exception→verdict 的 basin。Qwen-7B 可能因模型更强/LoRA landscape 更平滑而对初始化不敏感。DeepSeek-6.7B（CRUXEval-I 39% vs Qwen 56.5%）的 loss landscape 可能更 rugged，LoRA 初始化更易陷入 suboptimal basin（seed123 的 fail_recall 仅 70-72% 说明模型未学到 exception→fail 映射的关键部分）。**论文角度**: 这不是 negative result——它揭示了 trace SFT 的 practical consideration（training stability），可作为 contribution 的一部分。建议 Discussion 讨论 training stabilization 策略（warmup, lr schedule, LoRA rank 调整, multi-seed selection）。
259	
260	### D10: Train loss ≈ but accuracy ≠ across seeds [NEW — D029]
261	DeepSeek exception_only seed456 (train_loss=0.1225) 与 seed123 (train_loss=0.122) 训练损失几乎相同，但 accuracy 差 8.2pp（99.33% vs 91.09%）。关键差异集中在 fail_recall（1.0 vs 0.705）——token-level loss 在所有 tokens 上平均，掩盖了 fail 类少数样本的 sample-level 分类能力差异。**Implication**: (1) 扩展 D1 (eval_loss vs accuracy decoupling) 到训练阶段：train_loss 同样不是 verdict task accuracy 的可靠代理指标；(2) 对 checkpoint selection 的实际建议更强：必须用 task-specific metric (accuracy/F1)，甚至 train_loss 收敛也不保证 task performance；(3) fail 类作为少数类（28.5%），其学习质量被平均 loss 稀释——这在 class-imbalanced 设置下是 general pattern，可推广到其他 verdict/detection 任务。
262	
263	### D11: VOTA cross-model gap: training-time trace truncation as causal factor [NEW — D030 token analysis + group_analysis]
264	D030 token analysis 确认: `to_chat_text()` 保留 labels（verdict label 在训练时未被截断），但 91.7% 的 DeepSeek VOTA 训练样本的 **trace content** 从 mean 2626 tokens 被截断到 ~2048 tokens。
265	
266	**Group analysis 提供因果证据**: 将测试集按训练截断状态分组（推理时无截断, max_length=16384），train-truncated 组 accuracy=83.04% vs train-intact 组 accuracy=100%, Fisher exact p≈0。**截断的因果方向可以 claim**: 训练时 trace 被截断导致模型学到的信息不完整 → 推理时即使看到完整 trace 也无法正确判断。模型能力差异是残余 confound（无法完全分离）。
267	
268	**Implications**: (1) 论文中所有 "right-truncation corrupts/removes the verdict label" 措辞对 VOTA 不成立——label 完整保留，被截断的是 trace INPUT content；(2) 14.96pp gap 中截断效应有因果证据（group_analysis），模型能力差异是 residual confound；(3) exception_only 因 token 长度短（远低于 2048）不受截断影响，其跨模型对比更 clean——进一步强化 Claim 1 "most robust component" 叙事；(4) 论文应讨论 max_length 的影响作为 limitation/future work；(5) group_analysis 数据可作为 Table/Figure 纳入论文——展示截断的因果效应。
269	
270	### D8: Data duplication as representation signature
271	exception_only 训练集 39.45% 重复（4720→2858 unique），测试集 48.99%（1190→607 unique），而 raw_traces 仅 1.81%（5910→5803 unique）。重复源自 exception_only 表征的 design-by-intent compactness：同一编程题的多个 passing 解执行时均无异常，exception_only 表征退化为相同的空标记。这一数据特征本身就是 Claim 3 two-tier hierarchy 的佐证——Tier 1 信号仅编码 fault presence/absence，不编码 solution-level details，因此天然高重复。Train-test input overlap = 0 排除数据泄漏。
272	
273	## Contingency Framing (已解决, 留存档)
274	
275	### Claim 1 — RESOLVED (D029: seed456=99.33% confirms "consistently best component")
276	seed456 与 seed42 完全一致（均 99.33%），seed123 为孤立离群值。Claim 1 定稿为 "exception events consistently best component across models; absolute performance seed-dependent on DeepSeek (2/3 seeds robust, 1 outlier from LoRA init sensitivity); relative dominance over all alternatives robust across all seeds"。"0pp universal gap" 叙事已放弃，转为数据驱动的 nuanced framing。
277	
278	### Claim 2 — RESOLVED (D006 + D009)
279	v5 full_trace 81.76%. plan_002 label-only 86.22%, gradient dilution = minor (26%). 跨模型 VOTA gap 补充证据.
280	
281	## 与 v1 Framing 的关键差异
282	
283	| 维度 | v1 | v2.9 |
284	|------|----|----|
285	| Headline | VOTA compression 优于 full trace | Exception events are the most effective diagnostic signal |
286	| Primary claim | VOTA +24pp through fault indicator preservation | Exception signal consistently best across models; absolute performance seed-dependent on DeepSeek |
287	| Claim 2 | Compression > full trace (只有 gradient dilution) | Information density primary + gradient dilution quantification + cross-model reinforcement |
288	| Claim 3 Tier 1 | exception_only only | exception + assertion-point (co-Tier 1, D020) |
289	| VOTA 定位 | 核心方法 — trace compression | **Fault indicator isolation** — 价值在于提取 exception, 非 generic compression |
290	| Model scope | 单模型 (Qwen) | 双模型, 跨模型对比是核心贡献 |
291	| DeepSeek full_trace | N/A | v1 collapsed (label truncation), v3 pending |
292	| Seed robustness | 未验证 | Qwen ✅ 99.83% ± 0.00 (3 seeds); DeepSeek ⚠️ seed-dependent (91-99%, D028) |
293	| Irreducible error | 未分析 | ✅ GeneratorExit 根因明确，99.83% = representation ceiling |
294	| Calibration | 未验证 | ✅ 完整 ECE+Brier, ~63x/~150x gap vs no_trace |
295	| Data duplication | 未分析 | ✅ exception_only ~40% 重复（representation compactness），train-test overlap = 0 |
296	| Early stopping | 未讨论 | DeepSeek epoch1→epoch3 轻微退化 (0.3-0.5pp); 核心问题是 LoRA 初始化 (seed123 epoch1=91.43%), 非 overfitting |
297	| Narrative arc | "VOTA helps" | "Exception events are consistently best; VOTA's value is isolating them; training stability matters" |
298	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f71b8fcb-c00b-4895-a98c-b1bda9210b88",
  "isSidechain": false,
  "promptId": "26dc48b8-83e6-4c7b-83d0-0a6fb6e0b0fa",
  "type": "user",
  "uuid": "d109ed3c-6c8d-4cf9-a991-5f935ab1a25a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/paper_framing.md",
      "content": "# Paper Framing — trace-verdict-study\n\n> v3.0 — [UPDATED 2026-05-15] D030 CLOSED: DeepSeek VOTA 84.45% confirmed correct (confirmatory re-eval). **Critical narrative fix**: to_chat_text() preserves labels → VOTA 训练时 verdict label 未被截断 → 论文中 \"label truncation/corruption\" 措辞对 VOTA 不成立。正确叙事: trace INPUT content 被截断 (91.7% samples), 84.45% 反映 trace information loss。新增 D11: VOTA cross-model gap confounded by training-time truncation。数据集来源：HumanEval (164) + MBPP-sanitized (427) = 591 problems × 10 LLM-generated solutions = 5910 samples。\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Insight\n\nVerdict prediction (pass/fail) is fundamentally a **fault detection** task. The most effective signal is the **exception event** — a compact, structured diagnostic moment that consistently outperforms all other trace representations across models (Qwen 99.83% ± 0.00 across 3 seeds; DeepSeek 91-99% depending on seed, but always > VOTA 84.45% and no_trace 73.36%). In contrast, richer trace representations that require deeper execution reasoning show model-dependent effectiveness: VOTA gap = 14.96pp, no_trace gap = 1.77pp. Information density — not training signal distribution — is the primary bottleneck: even oracle loss masking (label-only) cannot close the 13pp gap between full traces and targeted extraction. The design principle: **extract the highest-specificity diagnostic signal; discard everything else.** Cross-model absolute performance depends on LoRA initialization stability, but exception_only's relative dominance over other components is robust.\n\nVOTA's primary contribution is **fault indicator isolation** — automatically extracting exception events from noisy full traces — rather than generic trace compression. The \"compression helps\" narrative was a stepping stone; the real mechanism is diagnostic signal extraction.\n\n## Core Claims (3)\n\n### Claim 1: Exception events are the most effective trace component for verdict prediction\n\nException summaries consistently achieve the highest verdict prediction accuracy across both models tested, outperforming all other trace representations in every seed. On Qwen-2.5-Coder-7B, performance is perfectly robust: 99.83% ± 0.00 (3 seeds). On DeepSeek-Coder-6.7B, absolute accuracy is seed-dependent (seed42=99.83% epoch1, seed123=91.43% epoch1; Δ=8.40pp), consistent with LoRA initialization sensitivity — but exception_only still dominates VOTA (84.45%) and no_trace (73.36%) in all seeds. This contrasts with VOTA (cross-model gap = 14.96pp) and no_trace (gap = 1.77pp). Exception events are structurally simple (`[ERROR] type: ... message: ...`) and do not require deep trace reasoning.\n\n**Supporting evidence:**\n- `vota_exception_only_seed42_v2`: Qwen 99.83%, ECE=0.0027\n- `deepseek_exception_only_seed42`: DeepSeek 99.83% (epoch1) / 99.33% (epoch3)\n- `deepseek_exception_only_seed456`: DeepSeek 99.33% (epoch3), CI [98.82, 99.75] — 与 seed42 完全一致\n- `deepseek_exception_only_seed123`: DeepSeek 91.43% (epoch1) / 91.09% (epoch3) — LoRA init sensitivity outlier\n- `deepseek_vota_seed42`: DeepSeek VOTA 84.45% (gap = 14.96pp vs Qwen)\n- `deepseek_no_trace_seed42`: DeepSeek no_trace 73.36% (gap = 1.77pp vs Qwen)\n- `vota_no_ae_seed42`: 99.41% — actual/expected removal 不降，非 trivial string comparison\n\n**DeepSeek seed analysis** ✅ (FINALIZED, D029):\n\n| Seed | Epoch 3 (final) | fail_recall | pass_recall | train_loss | Errors | CI |\n|------|-----------------|-------------|-------------|------------|--------|-----|\n| 42   | 99.33%          | 1.0         | 0.9906      | —          | 8/1190 | — |\n| 456  | 99.33%          | 1.0         | 0.9906      | 0.1225     | 8/1190 | [98.82, 99.75] |\n| 123  | 91.09%          | 0.705       | 0.993       | 0.122      | —      | [89.4, 92.6] |\n\nseed42 与 seed456 结果**完全一致**（均 8/1190 错误，99.33%），seed123 为离群值。seed123 的 fail_recall 仅 0.705 — LoRA 初始化落入差的局部最优，未充分学到 exception→fail 映射。**关键发现**: seed456 和 seed123 的 train_loss 几乎相同（0.1225 vs 0.122），但 accuracy 差 8.2pp — token-level loss 掩盖了 sample-level 分类能力的巨大差异（详见 D10）。\n\n**Irreducible error analysis** ✅: 3 seeds 错误的 2 个样本 (id=901, 905) 均来自 HumanEval/95 (`check_dict_case`)，根因为 Python `all()` 对 generator expression 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误）。tracer 将其标记为 `[ERROR]`，exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。整个 1190 条测试集仅这 2 条含 `GeneratorExit`，模型无训练信号学习其良性本质。**这确认 99.83% 是 exception_only 表征的理论上限，剩余 0.17% 是 representation-inherent irreducible error，而非模型不足。**\n\n**Seed robustness** ✅: Qwen exception_only 3-seed 完全一致，构成本文最强 robustness 证据：\n\n| Seed | Accuracy | 95% CI | Errors |\n|------|----------|--------|--------|\n| 42 | 99.83% | [99.58, 100] | 2/1190 |\n| 123 | 99.83% | [99.58, 100] | 2/1190 |\n| 456 | 99.83% | [99.58, 100] | 2/1190 |\n\n3 seeds 错误样本 100% 重叠（id=901, 905, 均为 `check_dict_case` 函数, label=pass → pred=fail）。**Irreducible samples**: 模型已达数据集理论上限，variance = 0。\n\n**DeepSeek cross-model** ✅ (D029): 3-seed 完整数据 — seed42/456=99.33%, seed123=91.09%。2/3 seeds 鲁棒，seed123 为 LoRA 初始化离群值（fail_recall 仅 0.705）。Qwen 3-seed 完美稳定 (99.83% ± 0.00) vs DeepSeek 高方差（σ≈4.8pp），暗示 exception signal 的 learnability 与模型 LoRA 训练稳定性相关。但即使最差 seed (91.09%) 仍优于 VOTA (84.45%) 和 no_trace (73.36%)，relative dominance robust。\n\n### Claim 2: Information density, not gradient dilution, drives trace compression benefit\n\nFull traces help verdict prediction (81.76% [`full_trace_seed42_v5`], +6.6pp over baseline), but VOTA achieves 99.41% [`vota_seed42_v5`] (+24.3pp) — a +17.6pp advantage. Label-only loss ablation (plan_002) quantifies the causal decomposition: **gradient dilution contributes ~26% of the gap** (4.5pp; label-only full_trace = 86.22% [`full_trace_label_only_seed42`]), **information overload contributes ~74%** (13.0pp; only trace compression resolves this). Even with oracle loss masking that eliminates gradient dilution, full traces still underperform VOTA by 13pp.\n\nCross-model evidence reinforces this: VOTA gap (14.96pp) partly tracks base model execution reasoning capability (Qwen CRUXEval-I 56.5% vs DeepSeek 39.0%, Δ=17.5pp), though **confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated to ~2048 tokens; see D11). The two factors cannot be disentangled in the current design. Exception signal partially bypasses both bottlenecks (token-short, no truncation; consistently best component on both models), though DeepSeek shows seed-dependent absolute performance (91-99%).\n\n**Supporting evidence:**\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (gradient dilution fix, +4.5pp over standard full_trace)\n- `full_trace_seed42_v5`: 81.76%, ECE=0.0958 (standard full_trace)\n- `vota_seed42_v5`: 99.41%, ECE=0.0054\n- `deepseek_vota_seed42`: 84.45% (VOTA model-dependent)\n- CRUXEval literature data (Wang et al.)\n\n### Claim 3: Two-tier diagnostic hierarchy for verdict prediction\n\nComponent ablation reveals verdict-relevant trace information has a strict two-tier hierarchy:\n- **Tier 1 — diagnostic moment signals**: exception summaries (99.83% [`vota_exception_only_seed42_v2`]) and assertion-point information (99.92% [`vota_ae_only_seed42`]) are individually near-perfect and sufficient for verdict prediction on Qwen. These signals are structurally simple and consistently the most effective component on both models, though DeepSeek absolute performance is seed-dependent.\n- **Tier 2 — behavioral patterns**: loop compression (85.63% [`vota_loop_only_seed42`]) carries substantial signal but is model-dependent and fully subsumed by Tier 1.\n\nCombining tiers introduces noise rather than helping: exception_only (99.83%) > VOTA full (99.41%), p=0.01. Loop_only ≈ full_trace_label_only (85.63% vs 86.22%) confirms VOTA's loop compression precisely extracts the useful behavioral signal from full traces.\n\n**Supporting evidence:**\n- `vota_exception_only_seed42_v2`: 99.83%, ECE=0.0027 (Tier 1 exception)\n- `vota_ae_only_seed42`: 99.92%, ECE=0.0004 (Tier 1 assertion-point, 与 exception 统计等价 p=0.80)\n- `vota_loop_only_seed42`: 85.63%, ECE=0.0831 (Tier 2 behavioral)\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (≈ loop_only, confirming extraction equivalence)\n- `deepseek_exception_only_seed42`: 99.83% epoch1 / 99.33% epoch3 (Tier 1 cross-model validation)\n- `deepseek_vota_seed42`: 84.45% (Tier 1+2 cross-model: Tier 2 introduces model-dependent degradation)\n\n**Calibration**: 完整 calibration 数据确认 Tier 1 信号不仅 accuracy 近完美，置信度校准也近完美：\n\n| Condition | Accuracy | ECE | Brier | 解读 |\n|-----------|----------|-----|-------|------|\n| ae_only | 99.92% | 0.0004 | 0.0008 | 近乎完美校准 |\n| exception_only | 99.83% | 0.0027 | 0.0013 | 近乎完美校准 |\n| VOTA | 99.41% | 0.0054 | 0.005 | 优秀，但 Tier 2 引入轻微 noise |\n| loop_only | 85.63% | 0.0831 | — | Tier 2 单独校准中等 |\n| label_only | 86.22% | 0.1107 | — | gradient dilution fix 仍 miscalibrated |\n| full_trace | 81.76% | 0.0958 | — | 中度 miscalibrated |\n| no_trace | 75.13% | 0.1715 | 0.1972 | 严重 miscalibrated |\n\nno_trace ECE 是 exception_only 的 **~63x**（0.1715/0.0027），Brier 是 **~150x**（0.1972/0.0013）。Trace signal（尤其 Tier 1）不仅提升 accuracy，更从根本上改善模型 calibration。\n\n**Design principle**: verdict-optimized traces should extract highest-specificity diagnostic signals; lower-specificity signals are redundant and may introduce noise.\n\n## Cross-Model Evidence Summary\n\n| Condition | Qwen-2.5-Coder-7B | DeepSeek-Coder-6.7B | Cross-model gap | Interpretation |\n|-----------|-------------------|---------------------|-----------------|----------------|\n| exception_only | 99.83% ± 0.00 (3 seeds) | seed42/456: 99.33%; seed123: 91.09% | 0.50-8.74pp (seed-dependent) | **Best component on both models**; 2/3 DeepSeek seeds match Qwen-level; 1 outlier still > VOTA |\n| VOTA | 99.41% | 84.45% | -14.96pp | Model-dependent — requires execution reasoning; **also confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated from mean 2626 to ~2048 tokens; labels preserved via to_chat_text(), see D11) |\n| no_trace | 75.13% | 73.36% | -1.77pp | Baseline gap tracks general capability |\n| full_trace | 81.76% | collapsed (v3 pending) | N/A | DeepSeek v1 label truncation bug |\n\n**Key insight**: Exception_only is consistently the best component on both models (even worst DeepSeek seed 91.09% > VOTA 84.45%). Cross-model gap 与 signal complexity 正相关, but exception signal's absolute effectiveness also depends on LoRA training stability. Qwen: perfectly robust (3 seeds identical). DeepSeek: 2/3 seeds at 99.33% (matching Qwen-level), 1 outlier at 91.09% (LoRA initialization). Median performance robust; seed sensitivity suggests smaller/weaker models may need training stabilization (multi-seed selection, warmup tuning) for optimal exception signal utilization.\n\n## VOTA Repositioning\n\n**旧叙事**: VOTA 是 trace compression 方法，价值在于\"压缩使 trace 更有效\"。\n\n**新叙事**: VOTA 是 **fault indicator isolation** 方法，核心价值在于自动从 noisy execution traces 中提取 exception events 等 diagnostic signals。\n\n**证据链**:\n1. exception_only (99.83%) ≥ VOTA full (99.41%) — 压缩后的其他组件（loop, ae）不仅无益，反而引入 noise\n2. VOTA 跨模型 gap = 14.96pp — 因为 VOTA 包含 model-dependent 的 Tier 2 组件（loop compression 需要 execution reasoning）\n3. exception_only 在两个模型上均为最优组件 — isolate 出 Tier 1 后，相对优势 robust（虽然 DeepSeek 绝对值 seed-dependent）\n4. vota_no_ae (99.41%) = VOTA (99.41%) — actual/expected 移除无影响，exception 是真正的 active ingredient\n\n**论文中的表述**: \"VOTA's trace compression pipeline incidentally isolates exception events — the minimal sufficient diagnostic signal. Its value lies not in making traces shorter, but in separating high-specificity fault indicators from low-specificity behavioral patterns.\"\n\n**对 Method section 的影响**: VOTA 仍然完整描述（loop compression + exception + actual/expected），但 Results/Discussion 明确指出 exception isolation 是核心机制，其他组件是 model-capability-dependent bonus。\n\n## Story Spine\n\n- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited, model-dependent benefit. No prior work has tested trace SFT on verdict tasks (binary pass/fail), nor identified what trace components drive classification performance.\n\n- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding that \"no single trace representation consistently outperforms others.\" TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. TRACED (ICSE 2024) showed traces help encoder-based classification. All existing trace formats are designed for execution simulation, not fault detection.\n\n- **Our framing**: We reframe verdict prediction as **fault detection** and ask: what is the minimal sufficient diagnostic signal? Through systematic component ablation across two architecturally distinct models, we discover that exception events — compact, structured error summaries — are consistently the most effective trace component, achieving near-perfect accuracy on Qwen (99.83% ± 0.00, 3 seeds) and outperforming all alternatives on DeepSeek (91-99% vs VOTA 84.45%). Richer trace representations work only when the base model has sufficient execution reasoning capability, making them unreliable for general deployment.\n\n- **Headline result**: \"Exception events consistently achieve the highest verdict accuracy across models (Qwen 99.83%, DeepSeek 91-99%), outperforming VOTA traces (84.45% on DeepSeek, -14.96pp gap) — demonstrating that fault indicator isolation, not trace reasoning, is the robust mechanism for verdict prediction. DeepSeek seed sensitivity reveals LoRA training stability as a secondary factor for smaller models.\"\n\n## Story Arc\n\n1. **Setup**: Trace SFT for code tasks — promising but inconsistent in prior work (DCSH, TracePile). Unknown whether traces help verdict tasks and what trace design matters.\n\n2. **First result — traces help, compression helps more** (single model): no_trace 75.13% → full_trace 81.76% → VOTA 99.41%. Label-only loss ablation decomposes the gap: 26% gradient dilution, 74% information overload. Compression improves accuracy through higher information density, not just cost savings.\n\n3. **Twist — what component actually drives VOTA?** Component ablation reveals exception_only (99.83%) ≥ full VOTA (99.41%). The \"trace reasoning\" narrative is wrong — verdict prediction is fault detection. Tier 1 (exceptions + assertion-point) subsumes Tier 2 (loops). Actual/expected removal doesn't hurt (99.41%).\n\n4. **Cross-model stress test — consistent dominance, not universal perfection**: Exception_only is the best component on both models (even DeepSeek worst seed 91.09% > VOTA 84.45%), but absolute performance is seed-dependent on DeepSeek (91-99% vs Qwen's perfectly stable 99.83%). VOTA degrades by 14.96pp. The structurally simplest component is the most robust, but LoRA initialization sensitivity introduces variance on weaker models. Qwen seed robustness (3-seed variance = 0) + calibration (ECE=0.0027) 确认 exception signal 在强模型上的 reliability。DeepSeek seed sensitivity 揭示 training stability 作为 secondary bottleneck。\n\n5. **Design principle**: For verdict tasks, identify the highest-specificity diagnostic signal (exception events) and discard everything else. VOTA's value is fault indicator isolation — automatically extracting exceptions from noisy traces — not generic compression. Simpler signals are more robust; complexity tolerance depends on model capability.\n\n## Dataset Characteristics\n\n### Data duplication analysis\n\n| Condition | Total | Unique | Duplication rate | Cause |\n|-----------|-------|--------|------------------|-------|\n| exception_only_train | 4720 | 2858 | 39.45% | 同题多个 passing 解映射为相同 (input, output) — 无异常 → 同一 trace |\n| exception_only_test | 1190 | 607 | 48.99% | 同上 |\n| raw_traces | 5910 | 5803 | 1.81% | 完整 trace 含行号/变量值/内存地址，几乎不重复 |\n\n**Train-test input overlap: 0（无数据泄漏）**\n\n**解读**: exception_only 高重复率是 representation 的自然属性，非数据问题。多个正确解对同一测试用例执行时若均无异常，exception_only 表征退化为相同的空/无异常标记。这恰好说明 exception signal 的 compactness — 它仅编码 fault presence，不编码 solution identity。raw_traces 重复率极低 (1.81%) 因为完整 trace 包含 solution-specific 信息（变量值、内存地址）。尽管高重复率意味着有效训练样本少于名义数量，模型仍达 99.83% — 进一步确认 exception signal 的 learnability。\n\n## DeepSeek full_trace 处理\n\n**现状**: v1 坍塌（28.5%, 100% 预测 fail, 根因: 训练端 label 截断）。v2 重训启动但被 kill（Loop #6 ops worker 腾 GPU 给 vota_seed456）。v3 RUNNING（label-preserving truncation fix）。\n\n**处理方案**: v3 正在 cuda:0 上训练，预计 5/16 完成。\n\n**VOTA vs full_trace 截断机制区分** (D030 token analysis 确认):\n- **full_trace v1**: SFTTrainer right-truncation 切掉了 verdict **label** → 100% predict fail → 坍塌。根因: DeepSeek tokenizer 对 full_trace 产生 >2048 tokens, label 在截断窗口外。\n- **VOTA**: `to_chat_text()` 保留 verdict label（label 完整），但 91.7% 的样本 **trace content（input）被截断**（mean 2626 → ~2048 tokens）。84.45% 是真实结果，反映 trace 信息损失对模型学习的影响，**不是** label corruption。\n- **exception_only**: token 长度远低于 2048，不受截断影响，跨模型对比 clean。\n\n**对论文叙事的影响**: 论文中所有 \"right-truncation corrupts/removes the verdict label\" 措辞**对 VOTA 不成立**——label 完整保留，被截断的是 trace input。正确表述: \"trace content truncation causes information loss\"。VOTA cross-model gap (14.96pp) 有两个贡献因素: (1) model capability, (2) training-time trace truncation on DeepSeek (see D11)。\n\n## External Benchmark (DebugBench) Positioning\n\n**DebugBench 仅作泛化性验证，不作 trace importance 证据。**\n\n| Condition | Main Dataset | DebugBench | Δ interpretation |\n|-----------|-------------|------------|------------------|\n| no_trace | 75.13% | 96.71% | DebugBench 天花板高，baseline 已强 |\n| VOTA | 99.41% | 99.77% | +3.06pp lift — 边际 |\n| exception_only | 99.83% | 100.00% | +3.29pp lift — 边际 |\n\n**主数据集 trace lift = 24.70pp**（no_trace → exception_only），DebugBench trace lift 不到其 1/7。\n\n**论文定位规则**：\n- DebugBench → 泛化性证据（exception_only 100% = 跨数据集鲁棒性）\n- Trace importance 论证 → 仅依赖主数据集（24.7pp lift）\n- 禁止用 DebugBench 的 3.29pp lift 论证 \"trace 的核心价值\"——审稿人会攻击天花板效应\n\n## Venue Fit Risks\n\n| Risk | Assessment | Mitigation |\n|------|-----------|------------|\n| 单任务 | 仍然只在 test verdict prediction 上验证 | 跨模型验证部分弥补; Discussion 中讨论 generalization |\n| 单数据集 | HumanEval + MBPP-sanitized 是唯一数据源 (591 problems × 10 solutions) | 定位为 empirical study, 深度优于广度; 两个标准 benchmark 组合覆盖多样编程题型; exception_only 有效训练样本仅 2858 unique 即达 99.83%, 暗示 signal 的 simplicity 降低对数据量的依赖 |\n| \"只是 feature engineering\" | exception extraction 不复杂 | simplicity 本身是 contribution — 最简信号最 robust |\n| Negative result 味道 | VOTA 跨模型不 robust | Reframe: 识别 robust vs non-robust 组件边界是 positive |\n| Seed robustness (Qwen) | ✅ 已解决: 99.83% ± 0.00 (3 seeds), irreducible samples 确认 | — |\n| Seed robustness (DeepSeek) | ✅ 3-seed 完整: 2/3 at 99.33%, 1 at 91.09% | LoRA initialization sensitivity — median robust, worst still > all alternatives; 转化为 training stability finding (D9/D10) |\n| Calibration | ✅ 完整数据: Tier 1 ECE≤0.003, no_trace ECE=0.171 (~63x gap) | Brier ~150x gap 进一步确认 |\n| 只用 2 个模型 | 有限但有意义的 diversity | Architecture + pretraining data (5.5T vs 2T) + CRUXEval gap (17.5pp) 构成充分差异 |\n| 数据重复率 | exception_only 训练集 39.45% 重复 | 非数据泄漏（train-test overlap = 0）；是 representation compactness 的自然结果；有效样本仍足够学习 |\n\n## Anticipated Reviewer Concerns\n\n| Concern | Planned Response |\n|---------|-----------------|\n| \"exception_only 99.83% 是不是 trivial pattern matching [ERROR] 有无？\" | full_trace 也包含 [ERROR] 但仅 81.76%——模型需要从 trace context 中 extract 和 utilize exception signal, 不是简单 keyword detection. no_trace 无 exception, 75.13%. |\n| \"为什么 exception_only > VOTA? adding info 反而降?\" | 非 exception 组件 (loop/ae tokens) 稀释 attention 对 exception 信号的聚焦. Calibration: exception_only ECE=0.0027 vs VOTA ECE=0.0054. 部分样本 loop 正常但有 exception, 引入矛盾信号. |\n| \"CRUXEval gap 与 VOTA gap 的相关性可能是 coincidence\" | 明确标注为 hypothesis. 列出 alternatives (tokenizer efficiency, pretraining scale 2.75x, chat template). 不 overclaim. |\n| \"只有 2 个模型，universality claim 太强\" | 同意是 limitation. 两模型在 architecture (RoPE vs ALiBi), pretraining data (5.5T vs 2T), execution reasoning (CRUXEval 17.5pp gap) 上有充分差异, 不是 trivial replication. Exception signal 的 structural simplicity 提供 inductive argument for broader generalization. |\n| \"99.83% 可能 saturated, 看不出 exception 到底学了什么\" | Calibration 双指标: exception_only ECE=0.0027, Brier=0.0013 (近完美校准). 对比 no_trace ECE=0.1715, Brier=0.1972 (~63x/~150x gap). **Irreducible error 根因已明确**: 2/1190 errors 均因 Python `all()` 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误），tracer 将其标记为 `[ERROR]`。模型看到 7 行 `[ERROR] GeneratorExit` 合理预测 fail，但代码实际正确。整个测试集仅这 2 条含 `GeneratorExit`，无训练信号可学习其良性本质。99.83% 是 representation 的理论上限，非 saturation artifact。 |\n| \"只用了 1 个 seed\" | Qwen ✅: 3 seeds 99.83% ± 0.00. DeepSeek ✅: 3 seeds 完整 — seed42/456=99.33%, seed123=91.09%。2/3 鲁棒，1 离群。median=99.33%, worst=91.09% (仍 > VOTA 84.45%)。论文透明报告所有 seeds，将 seed sensitivity 转化为 LoRA training stability 的 finding（D9）。 |\n| \"eval_loss 上升但 accuracy 提升——checkpoint selection 有问题?\" | Discussion D1: token-level loss 与 binary verdict accuracy 解耦. 推荐 verdict-specific metric. Methodological contribution. |\n| \"DeepSeek full_trace 坍塌是 bug 不是 finding\" | 诚实披露根因 (训练端 label 截断). 其他 3 条件不受影响. 修复版本如就绪则补入. |\n| \"calibration 数据只有 1 个 seed\" | Seed robustness 已证明 accuracy variance=0 (3 seeds), calibration 在 accuracy 完全一致的前提下 expected 也一致. ECE/Brier 的极小值 (0.0027/0.0013) 留有极小 variance 空间. |\n| \"DeepSeek epoch1 > epoch3, 为什么用 epoch3 报告?\" | 正文报告所有 seeds 的 final + best checkpoint。seed42: epoch1=99.83%, epoch3=99.33%。seed123: epoch1=91.43%, epoch3=91.09%。D7 讨论 early stopping + D9 讨论 LoRA initialization sensitivity。不 cherry-pick best seed。 |\n| \"DeepSeek seed sensitivity 说明 exception signal 不 robust\" | Exception_only 在所有 seeds 上仍优于其他条件（worst seed 91.09% > VOTA 84.45%）。Seed sensitivity 是 LoRA training 问题而非 signal 问题——Qwen 3 seeds 完美证明 signal 本身 robust。D9 讨论 training stabilization 作为 practical recommendation。 |\n| \"exception_only 数据集 ~40-49% 重复，有效训练样本不足？\" | 重复源自 representation compactness：同题多个 passing 解均无异常 → 相同 trace。**非数据泄漏**（train-test input overlap = 0）。raw_traces 仅 1.81% 重复，确认重复是 exception_only 表征特性而非数据收集问题。模型在有效样本仅 2858 unique 的条件下仍达 99.83%，反而说明 exception signal 的高 learnability — 少量 unique 样本即可充分学习 fault detection pattern。 |\n\n## Discussion 要点\n\n### D1: eval_loss vs verdict accuracy 解耦\nDeepSeek VOTA: eval_loss epoch1→3 从 0.068 升至 0.112 (+65%), 但 accuracy 从 78.15% 升至 84.45% (+6.3pp). Token-level calibration 与 binary classification accuracy 方向相反. **Implication**: verdict tasks 应用 task-specific metric (accuracy/F1) 做 checkpoint selection, 非 eval_loss.\n\n### D2: CRUXEval gap 假说 (revised — D030 confound)\nVOTA 跨模型 gap (14.96pp) 与 CRUXEval execution reasoning gap (15-17.5pp) 数值吻合. 假说: trace utilization effectiveness 受 base model \"execution reasoning readiness\" 约束. **标注**: hypothesis, N=2, 列出 alternatives. 不 overclaim. **注意**: 我们的训练/测试数据来自 HumanEval + MBPP-sanitized（非 CRUXEval），CRUXEval-I 分数仅作为衡量两个模型 execution reasoning 能力差异的外部参照。论文中必须明确区分数据来源与外部基准引用。**D030/D034 truncation evidence**: 14.96pp gap 中截断效应有因果证据: group_analysis 显示 train-truncated 83.04% vs train-intact 100% (Fisher p≈0, 推理时无截断)。截断因果方向可 claim，模型能力差异是 residual confound。CRUXEval gap 数值吻合可能部分巧合。论文中截断效应应作为 established factor 讨论（有 group_analysis 因果证据），模型能力假说标注为 residual confound hypothesis。\n\n### D3: Simplicity as robustness (revised)\nException signal 在两模型上均为最优组件，其结构简单性确保了相对优势的跨模型 robustness。但 DeepSeek seed sensitivity 揭示：simplicity 确保 signal 本身 robust，但 LoRA 训练过程是否稳定收敛到正确映射取决于模型。**trace design 应匹配 deployment model 的能力下界**，且需关注 training stability（建议：多 seed 验证 + 考虑 training stabilization 技巧如 warmup、learning rate schedule）。\n\n### D4: Checkpoint selection 与 gap 报告 (revised)\n正文报告所有 seeds 的 final checkpoint 结果 + best checkpoint 结果，不 cherry-pick。DeepSeek seed42: epoch1=99.83%, epoch3=99.33%（退化 0.50pp）。DeepSeek seed123: epoch1=91.43%, epoch3=91.09%（退化 0.34pp）。两个 seed 均显示轻微 epoch 退化，但核心差异在 epoch1 起点（8.40pp gap），不是训练过程。\n\n### D5: Irreducible samples — GeneratorExit 根因分析\n3 seeds 的 2/1190 errors 完全相同（id=901, 905, 均来自 HumanEval/95 `check_dict_case`），方向一致（pass→fail false negatives）。\n\n**根因**: Python `all()` 对 generator expression 短路时丢弃未耗尽的 generator，触发 `GeneratorExit`。`GeneratorExit` 继承自 `BaseException`（非 `Exception`），是 Python 内部控制流机制而非真正错误。但 tracer 对所有 caught exceptions 统一标记 `[ERROR]`，导致 exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。\n\n**为何不可约**:\n1. **表征局限**: exception_only 条件下模型仅见异常数据，无法访问控制流、返回值或 assertion 结果。`GeneratorExit` 在此表征中与真正错误不可区分。\n2. **跨 seed 确定性**: 3 个 random seeds 产生完全相同的 errors，确认这是 data/representation 属性而非模型初始化随机性。\n3. **训练集无信号**: 整个 1190 条测试集仅这 2 条含 `GeneratorExit`，训练集中也缺乏足够的 `GeneratorExit` 良性样本供模型学习。\n4. **人类也会犯错**: 仅看 exception trace（7 行 `[ERROR]`），人类审查者在不了解 Python generator protocol 的情况下也会预测 fail。\n\n**对论文的意义**: (1) 99.83% 是 exception_only representation 在此数据集上的理论 ceiling，非 saturation artifact；(2) 揭示 tracer 设计的改进方向——区分 `BaseException` 子类（如 `GeneratorExit`, `KeyboardInterrupt`）与 `Exception` 子类（真正的程序错误）可消除此类 irreducible error；(3) 提供 concrete evidence 说明 exception_only 模型\"理解\"的是 `[ERROR]` tag 的 fault indicator 语义，而非 exception type 的 fine-grained 含义。\n\n### D6: Calibration as secondary evidence\nCalibration 数据提供独立于 accuracy 的 evidence dimension。no_trace Brier=0.1972 说明模型无 trace 时不仅预测错，且对错误预测过度自信。exception_only Brier=0.0013 说明模型在有 exception signal 时几乎完美区分确定性和不确定性。这支持 Claim 1 的 \"sufficient signal\" 论点——exception 不仅让模型预测对，还让模型 \"知道自己对\"。\n\n### D7: Early stopping for exception signal (revised — D030 epoch1 data complete)\n3-seed epoch1 完整数据：seed42 epoch1=99.83% → epoch3=99.33%（-0.50pp）；**seed456 epoch1=99.33% → epoch3=99.33%（0.00pp）**；seed123 epoch1=91.43% → epoch3=91.09%（-0.34pp）。**seed42 的 epoch1=99.83%（匹配 Qwen）是该 seed 独有的 LoRA 初始化运气，不是 DeepSeek epoch1 的通用属性。** seed456 epoch1=epoch3 说明 epoch 退化非普遍现象。核心差异仍是 LoRA 初始化（epoch1 起点差 8.40pp），不是 overfitting。Early stopping 无法挽救差的初始化（seed123）。**Implication**: (1) 报告 DeepSeek 结果时应使用 median/2-of-3 (99.33%)，不应以 seed42 epoch1=99.83% 作为 headline；(2) epoch1 peak 是 LoRA 初始化运气的副产物，不具推广性。对比: VOTA 在 DeepSeek 上 84.45% **已确认正确**（D030 关闭: confirmatory re-eval max_length=16384 → 84.45%，与原始训练评估精确一致；D030 根因是 evaluate.py v2 的 max_length=2048 eval-time 截断 bug 导致 82.6% 预测为 garbage tokens）。\n\n### D9: LoRA initialization sensitivity as secondary bottleneck [NEW — D028]\nDeepSeek exception_only seed42=99.83% vs seed123=91.43% (epoch1), 8.40pp gap。Qwen 3 seeds 完全一致。假说：exception signal 的 learnability 取决于 (1) signal 本身的结构简单性（cross-model robust）+ (2) LoRA 初始化是否落入能正确映射 exception→verdict 的 basin。Qwen-7B 可能因模型更强/LoRA landscape 更平滑而对初始化不敏感。DeepSeek-6.7B（CRUXEval-I 39% vs Qwen 56.5%）的 loss landscape 可能更 rugged，LoRA 初始化更易陷入 suboptimal basin（seed123 的 fail_recall 仅 70-72% 说明模型未学到 exception→fail 映射的关键部分）。**论文角度**: 这不是 negative result——它揭示了 trace SFT 的 practical consideration（training stability），可作为 contribution 的一部分。建议 Discussion 讨论 training stabilization 策略（warmup, lr schedule, LoRA rank 调整, multi-seed selection）。\n\n### D10: Train loss ≈ but accuracy ≠ across seeds [NEW — D029]\nDeepSeek exception_only seed456 (train_loss=0.1225) 与 seed123 (train_loss=0.122) 训练损失几乎相同，但 accuracy 差 8.2pp（99.33% vs 91.09%）。关键差异集中在 fail_recall（1.0 vs 0.705）——token-level loss 在所有 tokens 上平均，掩盖了 fail 类少数样本的 sample-level 分类能力差异。**Implication**: (1) 扩展 D1 (eval_loss vs accuracy decoupling) 到训练阶段：train_loss 同样不是 verdict task accuracy 的可靠代理指标；(2) 对 checkpoint selection 的实际建议更强：必须用 task-specific metric (accuracy/F1)，甚至 train_loss 收敛也不保证 task performance；(3) fail 类作为少数类（28.5%），其学习质量被平均 loss 稀释——这在 class-imbalanced 设置下是 general pattern，可推广到其他 verdict/detection 任务。\n\n### D11: VOTA cross-model gap: training-time trace truncation as causal factor [NEW — D030 token analysis + group_analysis]\nD030 token analysis 确认: `to_chat_text()` 保留 labels（verdict label 在训练时未被截断），但 91.7% 的 DeepSeek VOTA 训练样本的 **trace content** 从 mean 2626 tokens 被截断到 ~2048 tokens。\n\n**Group analysis 提供因果证据**: 将测试集按训练截断状态分组（推理时无截断, max_length=16384），train-truncated 组 accuracy=83.04% vs train-intact 组 accuracy=100%, Fisher exact p≈0。**截断的因果方向可以 claim**: 训练时 trace 被截断导致模型学到的信息不完整 → 推理时即使看到完整 trace 也无法正确判断。模型能力差异是残余 confound（无法完全分离）。\n\n**Implications**: (1) 论文中所有 \"right-truncation corrupts/removes the verdict label\" 措辞对 VOTA 不成立——label 完整保留，被截断的是 trace INPUT content；(2) 14.96pp gap 中截断效应有因果证据（group_analysis），模型能力差异是 residual confound；(3) exception_only 因 token 长度短（远低于 2048）不受截断影响，其跨模型对比更 clean——进一步强化 Claim 1 \"most robust component\" 叙事；(4) 论文应讨论 max_length 的影响作为 limitation/future work；(5) group_analysis 数据可作为 Table/Figure 纳入论文——展示截断的因果效应。\n\n### D8: Data duplication as representation signature\nexception_only 训练集 39.45% 重复（4720→2858 unique），测试集 48.99%（1190→607 unique），而 raw_traces 仅 1.81%（5910→5803 unique）。重复源自 exception_only 表征的 design-by-intent compactness：同一编程题的多个 passing 解执行时均无异常，exception_only 表征退化为相同的空标记。这一数据特征本身就是 Claim 3 two-tier hierarchy 的佐证——Tier 1 信号仅编码 fault presence/absence，不编码 solution-level details，因此天然高重复。Train-test input overlap = 0 排除数据泄漏。\n\n## Contingency Framing (已解决, 留存档)\n\n### Claim 1 — RESOLVED (D029: seed456=99.33% confirms \"consistently best component\")\nseed456 与 seed42 完全一致（均 99.33%），seed123 为孤立离群值。Claim 1 定稿为 \"exception events consistently best component across models; absolute performance seed-dependent on DeepSeek (2/3 seeds robust, 1 outlier from LoRA init sensitivity); relative dominance over all alternatives robust across all seeds\"。\"0pp universal gap\" 叙事已放弃，转为数据驱动的 nuanced framing。\n\n### Claim 2 — RESOLVED (D006 + D009)\nv5 full_trace 81.76%. plan_002 label-only 86.22%, gradient dilution = minor (26%). 跨模型 VOTA gap 补充证据.\n\n## 与 v1 Framing 的关键差异\n\n| 维度 | v1 | v2.9 |\n|------|----|----|\n| Headline | VOTA compression 优于 full trace | Exception events are the most effective diagnostic signal |\n| Primary claim | VOTA +24pp through fault indicator preservation | Exception signal consistently best across models; absolute performance seed-dependent on DeepSeek |\n| Claim 2 | Compression > full trace (只有 gradient dilution) | Information density primary + gradient dilution quantification + cross-model reinforcement |\n| Claim 3 Tier 1 | exception_only only | exception + assertion-point (co-Tier 1, D020) |\n| VOTA 定位 | 核心方法 — trace compression | **Fault indicator isolation** — 价值在于提取 exception, 非 generic compression |\n| Model scope | 单模型 (Qwen) | 双模型, 跨模型对比是核心贡献 |\n| DeepSeek full_trace | N/A | v1 collapsed (label truncation), v3 pending |\n| Seed robustness | 未验证 | Qwen ✅ 99.83% ± 0.00 (3 seeds); DeepSeek ⚠️ seed-dependent (91-99%, D028) |\n| Irreducible error | 未分析 | ✅ GeneratorExit 根因明确，99.83% = representation ceiling |\n| Calibration | 未验证 | ✅ 完整 ECE+Brier, ~63x/~150x gap vs no_trace |\n| Data duplication | 未分析 | ✅ exception_only ~40% 重复（representation compactness），train-test overlap = 0 |\n| Early stopping | 未讨论 | DeepSeek epoch1→epoch3 轻微退化 (0.3-0.5pp); 核心问题是 LoRA 初始化 (seed123 epoch1=91.43%), 非 overfitting |\n| Narrative arc | \"VOTA helps\" | \"Exception events are consistently best; VOTA's value is isolating them; training stability matters\" |\n",
      "numLines": 298,
      "startLine": 1,
      "totalLines": 298
    }
  },
  "sourceToolAssistantUUID": "f71b8fcb-c00b-4895-a98c-b1bda9210b88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-st…",
  "leafUuid": "d109ed3c-6c8d-4cf9-a991-5f935ab1a25a",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper from experiment data",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c"
}
```

---

### Assistant

_source line 16 · 2026-05-18T13:44:43.740Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me synthesize this into a complete LaTeX paper.

Key information:
- This is about trace-based verdict prediction (pass/fail) for code
- Core finding: exception events are the most effective trace component
- Three claims: (1) exception events best, (2) information density not gradient dilution, (3) two-tier diagnostic hierarchy
- Multiple experiments: tail-384 phase transition, cross-seed robustness, error analysis, cross-model calibration, frontier baselines, OOD generalization, training dynamics


- I'll use a standard article class and structure the paper with abstract, introduction, related work, method, experiments mapped to the data, discussion, and conclusion, following the narrative guidance to deliver publication-quality work.

Now I'm mapping each experiment to its corresponding section—information locality and budget curves, robustness across seeds, error analysis, calibration behavior, frontier comparisons, cross-language generalization, and training dynamics—then writing out the complete paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d109ed3c-6c8d-4cf9-a991-5f935ab1a25a",
  "isSidechain": false,
  "requestId": "req_011CbA8kB9yqTbYhx5bunNXY",
  "type": "assistant",
  "uuid": "bb97069d-d56d-4403-9839-1509c79092ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BP2yVoGuVGEPKsdpUYuhsy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28336,
      "cache_read_input_tokens": 24781,
      "output_tokens": 585,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 585,
          "cache_read_input_tokens": 24781,
          "cache_creation_input_tokens": 28336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28336
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

_source line 17 · 2026-05-18T13:44:43.742Z_

Now let me check the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb97069d-d56d-4403-9839-1509c79092ab",
  "isSidechain": false,
  "requestId": "req_011CbA8kB9yqTbYhx5bunNXY",
  "type": "assistant",
  "uuid": "9aac51d0-7fdc-4810-8741-132e9dbb2d43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BP2yVoGuVGEPKsdpUYuhsy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28336,
      "cache_read_input_tokens": 24781,
      "output_tokens": 585,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 585,
          "cache_read_input_tokens": 24781,
          "cache_creation_input_tokens": 28336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28336
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

_source line 18 · 2026-05-18T13:44:45.152Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FPs4MDipqnRu3vGBdqKqaE`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/",
  "description": "List median output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9aac51d0-7fdc-4810-8741-132e9dbb2d43",
  "isSidechain": false,
  "requestId": "req_011CbA8kB9yqTbYhx5bunNXY",
  "type": "assistant",
  "uuid": "4c41ddc3-b0cd-414a-b8f6-9574912f3068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BP2yVoGuVGEPKsdpUYuhsy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28336,
      "cache_read_input_tokens": 24781,
      "output_tokens": 585,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 585,
          "cache_read_input_tokens": 24781,
          "cache_creation_input_tokens": 28336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28336
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

_source line 19 · 2026-05-18T13:44:45.331Z_

<details><summary>↩ Tool result · `toolu_01FPs4MDipqnRu3vGBdqKqaE`</summary>

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
  "parentUuid": "4c41ddc3-b0cd-414a-b8f6-9574912f3068",
  "isSidechain": false,
  "promptId": "26dc48b8-83e6-4c7b-83d0-0a6fb6e0b0fa",
  "type": "user",
  "uuid": "54596161-a287-4920-b5ff-d445d71d5b42",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4c41ddc3-b0cd-414a-b8f6-9574912f3068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-18T13:44:47.931Z_

Writing the full paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54596161-a287-4920-b5ff-d445d71d5b42",
  "isSidechain": false,
  "requestId": "req_011CbA8mNwRe2LaVRNiW8DJa",
  "type": "assistant",
  "uuid": "1db5366b-19af-48ed-a5fe-47774d5f05c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZntXcMCHWvAQASGdM9NMq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 53117,
      "output_tokens": 9454,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 616,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9454,
          "cache_read_input_tokens": 53117,
          "cache_creation_input_tokens": 616,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 616
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

_source line 21 · 2026-05-18T13:47:59.899Z_

<details open><summary>🔧 Tool call — Write · `toolu_01GRpMJgGpDW3dTWRCmk17eV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\newcommand{\\etal}{\\textit{et al.}}\n\\newcommand{\\ie}{\\textit{i.e.}}\n\\newcommand{\\eg}{\\textit{e.g.}}\n\\newcommand{\\pp}{\\,pp}\n\n\\title{Exception Events Are All You Need:\\\\Diagnostic Signal Extraction for Verdict Prediction}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\n% ============================================================\nExecution traces are increasingly used to improve code understanding in language models, yet prior work on trace-based supervised fine-tuning (SFT) reports inconsistent benefits across models and tasks. We study verdict prediction, the binary classification of whether a code solution passes or fails its test suite, and ask: \\emph{what is the minimal sufficient diagnostic signal in an execution trace?} Through systematic component ablation across four architecturally distinct models (1.5B to 13B parameters), we find that exception events, compact structured records of runtime errors, consistently achieve the highest accuracy (99.83\\% on Qwen-2.5-Coder-7B, $\\pm$0.00 across three seeds) while richer trace representations degrade under information overload. A label-only loss ablation decomposes the full-trace-to-compressed-trace gap: 26\\% is attributable to gradient dilution, while 74\\% stems from information density loss that only signal extraction resolves. Cross-model calibration confirms near-perfect confidence alignment (Expected Calibration Error $\\leq$ 0.012) for exception-trained models, a 14--63$\\times$ improvement over no-trace baselines. Task-specific SFT on a 1.5B model matches frontier few-shot performance (GPT-4o, Claude-3.5) at 1/1800th the inference cost. Our results establish a two-tier diagnostic hierarchy for verdict-relevant trace information and demonstrate that fault indicator isolation, not generic trace compression, is the robust mechanism for verdict prediction.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n% ============================================================\n\nExecution traces record the runtime behavior of programs and carry rich information about control flow, variable states, and error conditions. Recent work has explored trace-augmented SFT to improve code generation~\\cite{dcsh2025,tracepile2025} and trace-based classification for bug detection~\\cite{traced2024}. However, a consistent finding across these studies is that trace benefit is model-dependent and format-sensitive: DCSH~\\cite{dcsh2025} tested five trace formats and concluded that ``no single trace representation consistently outperforms others.''\n\nThese prior studies share a common framing: they treat traces as context for \\emph{execution simulation}, asking models to reason about program behavior from detailed step-by-step records. We argue that for verdict prediction, the binary pass/fail classification of test outcomes, this framing is misaligned. Verdict prediction is fundamentally a \\textbf{fault detection} task. The question is not ``what did the program do?'' but ``did the program fail, and why?''\n\nThis reframing motivates a different design principle: instead of providing rich execution context and hoping the model extracts the relevant signal, we should \\emph{identify and isolate the highest-specificity diagnostic signal directly}. Through systematic ablation across four models spanning 1.5B to 13B parameters, we discover that exception events, compact structured records consisting of error type and message, are consistently the most effective trace component. On Qwen-2.5-Coder-7B, exception-only SFT achieves 99.83\\% accuracy with zero variance across three random seeds, and the two remaining errors are traceable to an irreducible representation ambiguity (Python's \\texttt{GeneratorExit} mechanism). Richer representations that include loop behavior or full execution traces suffer from information overload: accuracy degrades and calibration worsens despite containing strictly more information.\n\nA label-only loss ablation quantifies the bottleneck: when gradient dilution is eliminated by masking loss on non-verdict tokens, full-trace accuracy improves by only 4.5\\pp{} (from 81.76\\% to 86.22\\%), leaving a 13\\pp{} gap to compressed traces. Information density, not gradient dilution, is the primary constraint. Budget curve analysis across four models confirms that diagnostic signal concentrates in the trace tail with diminishing returns: tail-512 tokens ($\\sim$94\\%) outperform head-2048 tokens ($\\sim$79\\%) by $\\sim$15\\pp, and all models exhibit smooth log-shaped curves without a shared critical threshold.\n\nOur contributions are:\n\\begin{itemize}\n    \\item We establish that exception events are the most effective and robust trace component for verdict prediction, achieving near-perfect accuracy across four models (99.83\\% on three models, 92--99\\% on DeepSeek) with near-perfect calibration (ECE $\\leq$ 0.012).\n    \\item We quantify the information density bottleneck through label-only loss ablation (26\\% gradient dilution vs.\\ 74\\% information overload) and budget curve analysis showing smooth diminishing returns concentrated in trace tails.\n    \\item We identify a two-tier diagnostic hierarchy: Tier~1 signals (exception events, assertion outcomes) are individually near-perfect and sufficient; Tier~2 signals (loop behavior) carry moderate signal but introduce noise when combined with Tier~1.\n    \\item We demonstrate that task-specific SFT on models as small as 1.5B surpasses frontier few-shot baselines (GPT-4o, Claude-3.5) with 16--20$\\times$ fewer errors at 1/1800th the cost, and that exception-based training generalizes across programming languages with preserved lift ($\\sim$24\\pp) over no-trace baselines.\n\\end{itemize}\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n% ============================================================\n\n\\paragraph{Trace-augmented code models.}\nDCSH~\\cite{dcsh2025} evaluated five trace representations for code generation via SFT on models up to 16B parameters, finding no universally superior format. TracePile~\\cite{tracepile2025} scaled trace-augmented pretraining to 2.6M samples but evaluated only generative tasks. Both studies frame traces as execution simulation context. TRACED~\\cite{traced2024} showed that traces improve encoder-based bug classification, providing the closest precedent to our work, though they did not perform component ablation or test decoder-based models. Our work differs by reframing verdict prediction as fault detection, performing fine-grained signal decomposition, and testing across multiple decoder architectures.\n\n\\paragraph{Verdict and test outcome prediction.}\nPredicting whether code passes tests has been studied as a filtering mechanism for code generation~\\cite{coderanker2023,codet2023}. These approaches typically use the generated code as input without execution information. We show that adding even minimal execution signals (exception events) transforms this task from a moderately difficult classification problem (75\\%) to a near-solved one (99.83\\%).\n\n\\paragraph{Calibration in code models.}\nModel calibration, the alignment between predicted confidence and actual correctness, has received limited attention in code tasks. We provide the first systematic calibration analysis across trace conditions, showing that exception signals improve ECE by 14--63$\\times$ over no-trace baselines.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n% ============================================================\n\n\\subsection{Task Definition}\n\nGiven a code solution $s$ and its test suite $T$, verdict prediction is the binary classification: $f(s, c) \\rightarrow \\{pass, fail\\}$, where $c$ is an optional execution context derived from running $s$ against $T$. We study how the choice of $c$ affects prediction accuracy and calibration.\n\n\\subsection{Trace Representations}\n\nWe define seven trace conditions spanning a spectrum from no execution information to full traces:\n\n\\begin{itemize}\n    \\item \\textbf{no\\_trace}: Code only, no execution information ($c = \\emptyset$).\n    \\item \\textbf{full\\_trace}: Complete execution trace including all control flow, variable states, and exception information.\n    \\item \\textbf{label\\_only}: Full trace input with loss computed only on the verdict token, eliminating gradient dilution.\n    \\item \\textbf{VOTA} (Verdict-Optimized Trace Abstraction): Compressed trace retaining three components: loop summaries, exception events, and assertion outcomes.\n    \\item \\textbf{exception\\_only}: Only structured exception records (\\texttt{[ERROR] type: ... message: ...}).\n    \\item \\textbf{loop\\_only}: Only loop behavior summaries from VOTA compression.\n    \\item \\textbf{ae\\_only}: Only assertion/expected-value comparison outcomes.\n\\end{itemize}\n\n\\subsection{VOTA Trace Compression}\n\nVOTA applies three extraction operations to raw traces: (1) \\textbf{Loop compression} summarizes repetitive loop iterations into structured summaries capturing iteration count, representative values, and termination conditions. (2) \\textbf{Exception extraction} isolates structured error records in the format \\texttt{[ERROR] type: message}. (3) \\textbf{Assertion-point extraction} captures actual vs.\\ expected value comparisons at assertion sites. The key finding of this work is that VOTA's primary value lies in operation (2), fault indicator isolation, rather than generic compression.\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Dataset.} We construct a verdict prediction dataset from HumanEval (164 problems) and MBPP-sanitized (427 problems), generating 10 LLM-produced solutions per problem for a total of 5,910 samples. Training uses 4,720 samples (2,858 unique for exception\\_only due to representation compactness); testing uses 1,190 samples. Train-test input overlap is zero.\n\n\\paragraph{Models.} We evaluate four models: Qwen-2.5-Coder-7B, Qwen-2.5-Coder-1.5B, DeepSeek-Coder-6.7B, and CodeLlama-13B-Instruct. These span three architecture families, parameter scales from 1.5B to 13B, and pretraining corpora from 2T to 5.5T tokens.\n\n\\paragraph{Training.} All models are fine-tuned with LoRA (rank 16, $\\alpha$=32) for 3 epochs with learning rate $2\\times10^{-4}$ and batch size 4. Multi-seed evaluation (seeds 42, 123, 456) is performed for robustness assessment.\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:exp}\n% ============================================================\n\n\\subsection{Information Locality: Budget Curve Analysis}\n\\label{sec:budget}\n\nTo understand where diagnostic information resides within traces, we evaluate tail-$k$ and head-$k$ truncation across four models. Table~\\ref{tab:budget} presents accuracy at six budget points including a new tail-384 measurement that probes the 256--512 token transition region.\n\n\\begin{table}[t]\n\\centering\n\\caption{Budget curve with tail-384 interpolation across four models. Accuracy (\\%) at each token budget. $\\Delta$ columns show per-step gains. Sharpness index measures the position of tail-384 within the 256--512 interval (0 = stays at 256 level, 1 = jumps to 512 level, 0.5 = exact midpoint).}\n\\label{tab:budget}\n\\small\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nModel & tail-256 & tail-384 & tail-512 & tail-1024 & tail-2048 & $\\Delta_{256 \\to 384}$ & $\\Delta_{384 \\to 512}$ & Sharpness \\\\\n\\midrule\nQwen-7B     & 77.5 & 85.6 & 93.6 & 96.5 & 97.3 & +8.1 & +8.0 & 0.52 \\\\\nDeepSeek-6.7B & 76.4 & 84.3 & 93.9 & 96.5 & 95.0 & +7.9 & +9.6 & 0.46 \\\\\nQwen-1.5B   & 72.6 & 83.2 & 95.6 & 96.6 & 97.9 & +10.6 & +12.4 & 0.44 \\\\\nCodeLlama-13B & 77.9 & 88.3 & 97.5 & 98.2 & --- & +10.4 & +9.2 & 0.54 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mean sharpness index across models is 0.49 (range: 0.44--0.54), indicating that tail-384 falls almost exactly at the midpoint of the 256--512 transition. This rules out a sharp phase transition: information accumulates gradually with token budget, following a log-shaped diminishing returns curve. Each model's steepest gain region differs slightly in position and magnitude, but no model exhibits a discrete threshold.\n\nTwo key findings emerge. First, \\textbf{information concentrates in trace tails}: all four models achieve tail-384 accuracy (83--88\\%) that exceeds head-2048 accuracy ($\\sim$79\\%) by 4--9\\pp, confirming that the final tokens of an execution trace, which contain crash points and stack traces, carry more diagnostic value than the first 2,048 tokens. Second, \\textbf{tail-512 substantially outperforms head-2048} ($\\sim$94\\% vs.\\ $\\sim$79\\%, $\\Delta \\approx 15$\\pp), providing strong evidence for information locality: a quarter of the tokens from the trace tail carry more verdict-relevant signal than eight times as many tokens from the head.\n\n\\subsection{Cross-Seed Robustness}\n\\label{sec:seeds}\n\nPoint estimates from single training runs may be unreliable due to LoRA initialization sensitivity. Table~\\ref{tab:crossseed} reports tail-512 accuracy across three seeds and four models.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed tail-512 robustness (3 seeds $\\times$ 4 models). All worst-seed results exceed head-2048 baselines ($\\sim$79--81\\%).}\n\\label{tab:crossseed}\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nModel & Seed 42 & Seed 123 & Seed 456 & Mean & $\\sigma$ & Band \\\\\n\\midrule\nQwen-7B       & 93.6 & 91.9 & 94.7 & 93.4 & 1.4\\pp & 2.8\\pp \\\\\nDeepSeek-6.7B & 93.9 & 89.2 & 93.5 & 92.2 & 2.6\\pp & 4.7\\pp \\\\\nQwen-1.5B     & 95.6 & 93.2 & 94.9 & 94.6 & 1.2\\pp & 2.4\\pp \\\\\nCodeLlama-13B & 97.5 & 95.8 & 97.1 & 96.8 & 0.9\\pp & 1.7\\pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-seed standard deviation ranges from 0.9\\pp{} (CodeLlama-13B) to 2.6\\pp{} (DeepSeek-6.7B), with a cross-model average of 1.54\\pp. The worst single-seed result (DeepSeek seed 123, 89.2\\%) still exceeds the best head-2048 baseline ($\\sim$81\\%) by 8\\pp. Rank ordering is perfectly preserved across all seeds: CodeLlama-13B $>$ Qwen-1.5B $>$ Qwen-7B $\\geq$ DeepSeek-6.7B. Models at capacity extremes (1.5B and 13B) show lower variance ($\\overline{\\sigma}$ = 1.1\\pp), while mid-scale models exhibit higher variance ($\\overline{\\sigma}$ = 2.0\\pp), possibly reflecting more complex LoRA optimization landscapes at intermediate scales.\n\n\\subsection{Cross-Model Calibration}\n\\label{sec:calibration}\n\nBeyond accuracy, we assess whether models trained on exception signals produce well-calibrated confidence estimates. Table~\\ref{tab:calibration} reports Expected Calibration Error (ECE) and Brier score for exception\\_only across four models.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model calibration for exception\\_only. ECE ratio compares against no\\_trace baseline (ECE = 0.171).}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & Accuracy & ECE & Brier & ECE ratio vs.\\ no\\_trace \\\\\n\\midrule\nQwen-2.5-Coder-7B     & 99.83\\% & 0.0027 & 0.0013 & 63$\\times$ \\\\\nCodeLlama-13B-Instruct & 99.83\\% & 0.003  & 0.002  & 57$\\times$ \\\\\nQwen-2.5-Coder-1.5B   & 99.83\\% & 0.005  & 0.003  & 34$\\times$ \\\\\nDeepSeek-Coder-6.7B    & 99.33\\% & 0.012  & 0.006  & 14$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll four models achieve ECE $\\leq$ 0.012 when trained on exception signals, representing a 14--63$\\times$ improvement over the no\\_trace baseline (ECE = 0.171). Three of four models reach identical accuracy (99.83\\%) with only two errors each, both attributable to the same irreducible representation ambiguity (\\texttt{GeneratorExit}; see Section~\\ref{sec:error}). DeepSeek's slightly higher ECE (0.012) correlates with its higher error count (8 vs.\\ 2) rather than signal quality differences. The near-perfect calibration means exception-trained models not only predict correctly but produce confidence scores that faithfully reflect their certainty, a property valuable for deployment in CI/CD pipelines where abstention on uncertain cases can prevent false signals.\n\n\\subsection{Error Analysis}\n\\label{sec:error}\n\nWe analyze failure modes across all seven trace conditions on Qwen-7B (seed 42) to understand what each representation gets wrong and why. Table~\\ref{tab:errors} presents the error distribution.\n\n\\begin{table}[t]\n\\centering\n\\caption{Error mode distribution by condition (Qwen-7B, seed 42). Directions indicate whether errors are fail$\\to$pass (false positives) or pass$\\to$fail (false negatives).}\n\\label{tab:errors}\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nCondition & Errors & Rate & fail$\\to$pass & pass$\\to$fail & Dominant mode \\\\\n\\midrule\nexception\\_only & 2   & 0.17\\% & 0\\%  & 100\\% & GeneratorExit irreducible \\\\\nae\\_only        & 1   & 0.08\\% & 0\\%  & 100\\% & GeneratorExit variant \\\\\nVOTA            & 7   & 0.59\\% & 57\\% & 43\\%  & Tier~2 noise conflict \\\\\nloop\\_only      & 171 & 14.4\\% & 36\\% & 64\\%  & Insufficient diagnostic signal \\\\\nfull\\_trace     & 217 & 18.2\\% & 47\\% & 53\\%  & Information overload \\\\\nlabel\\_only     & 164 & 13.8\\% & 65\\% & 35\\%  & Gradient dilution residual \\\\\nno\\_trace       & 296 & 24.9\\% & 70\\% & 30\\%  & Majority class bias \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Tier~1 errors are irreducible.} Exception\\_only's two errors (samples 901 and 905, both from \\texttt{check\\_dict\\_case} in HumanEval/95) stem from Python's \\texttt{all()} short-circuiting on generator expressions, which triggers \\texttt{GeneratorExit} (a \\texttt{BaseException} subclass used for internal control flow, not a real error). The tracer labels this as \\texttt{[ERROR]}, making it indistinguishable from genuine failures in the exception\\_only representation. These same two errors appear identically across all three seeds (Jaccard overlap = 0.85 across models), confirming they are a data/representation property rather than a model artifact. The 99.83\\% accuracy is thus the theoretical ceiling for this representation.\n\n\\paragraph{Full-trace errors correlate with length.} Table~\\ref{tab:length_errors} shows that error rate in the full\\_trace condition increases with trace length (Pearson $r$ = 0.41), from $\\sim$9\\% for traces under 500 tokens to $\\sim$33\\% for traces over 1,500 tokens. This length-error correlation is direct evidence of information overload: longer traces bury diagnostic signals in irrelevant execution details.\n\n\\begin{table}[t]\n\\centering\n\\caption{Error rate by trace length (full\\_trace condition, Qwen-7B).}\n\\label{tab:length_errors}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nLength bucket & Samples & Errors & Error rate \\\\\n\\midrule\n$<$500 tokens   & $\\sim$190 & $\\sim$17 & $\\sim$9\\% \\\\\n500--1000 tokens & $\\sim$340 & $\\sim$54 & $\\sim$16\\% \\\\\n1000--1500 tokens & $\\sim$370 & $\\sim$72 & $\\sim$19\\% \\\\\n$>$1500 tokens  & $\\sim$290 & $\\sim$96 & $\\sim$33\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Tier~1 and Tier~2 fail differently.} Cross-condition error overlap analysis reveals that Tier~1 (exception/ae) and Tier~2 (loop/full\\_trace) error sets are nearly disjoint (Jaccard = 0.01). Tier~1 failures stem from representation ambiguity (the \\texttt{GeneratorExit} cases), while Tier~2 failures involve reasoning complexity (interpreting loop behavior patterns). VOTA's five unique errors beyond the two shared with exception\\_only arise from Tier~2 noise: three cases where loop summaries present normal behavior alongside exceptions (conflicting signals) and two cases where Tier~2 tokens dilute attention to exception signals.\n\n\\subsection{Frontier Model Comparison}\n\\label{sec:frontier}\n\nTo contextualize SFT performance, we compare against frontier models in few-shot settings. Table~\\ref{tab:frontier} presents the comparison.\n\n\\begin{table}[t]\n\\centering\n\\caption{SFT vs.\\ frontier few-shot comparison. Cost is approximate per-run inference cost for the 1,190-sample test set.}\n\\label{tab:frontier}\n\\small\n\\begin{tabular}{@{}llccccc@{}}\n\\toprule\nMethod & Model & Input & Shots & Accuracy & Errors & Cost \\\\\n\\midrule\nSFT & Qwen-7B        & exception & --- & 99.83\\% & 2    & \\$0.01 \\\\\nSFT & Qwen-1.5B      & exception & --- & 99.83\\% & 2    & \\$0.005 \\\\\nSFT & CodeLlama-13B  & exception & --- & 99.83\\% & 2    & \\$0.02 \\\\\n\\midrule\nFew-shot & Claude-3.5 & exception & 3   & 97.2\\%  & $\\sim$33 & \\$10 \\\\\nFew-shot & GPT-4o     & exception & 3   & 96.6\\%  & $\\sim$40 & \\$8 \\\\\nFew-shot & Claude-3.5 & exception & 0   & 95.8\\%  & $\\sim$50 & \\$7 \\\\\nFew-shot & GPT-4o     & exception & 0   & 95.2\\%  & $\\sim$57 & \\$5 \\\\\n\\midrule\nFew-shot & Claude-3.5 & no\\_trace & 0   & 82.1\\%  & $\\sim$213 & \\$5 \\\\\nFew-shot & GPT-4o     & no\\_trace & 0   & 80.5\\%  & $\\sim$232 & \\$3 \\\\\nSFT      & Qwen-7B    & no\\_trace & --- & 75.1\\%  & 296  & \\$0.01 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWhile the accuracy gap between SFT and frontier 3-shot appears modest (2.6\\pp{} vs.\\ Claude-3.5), the error count perspective is revealing: SFT produces 2 errors versus $\\sim$33 for the best frontier model, a 16.5$\\times$ reduction. GPT-4o 3-shot makes 20$\\times$ more errors. Inference cost differs by approximately 1,800$\\times$. Frontier models also benefit substantially from exception signals: GPT-4o improves from 80.5\\% (no\\_trace) to 95.2\\% (exception, 0-shot), a 14.7\\pp{} lift that independently confirms the diagnostic value of exception events.\n\n\\subsection{Out-of-Distribution Generalization}\n\\label{sec:ood}\n\nWe evaluate whether exception-based training transfers to unseen projects and programming languages using 500-sample test sets per language. Table~\\ref{tab:ood} reports results.\n\n\\begin{table}[t]\n\\centering\n\\caption{In-distribution vs.\\ OOD accuracy by language (Qwen-7B, exception\\_only SFT).}\n\\label{tab:ood}\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nLanguage & Setting & exception\\_only & no\\_trace & Lift & Deg.\\ vs.\\ ID \\\\\n\\midrule\nPython & ID (HumanEval+MBPP)  & 99.83\\% & 75.1\\% & +24.7\\pp & baseline \\\\\nPython & OOD (new projects)   & 96.3\\%  & 71.5\\% & +24.8\\pp & $-$3.5\\pp \\\\\nJava   & OOD                  & 91.8\\%  & 68.0\\% & +23.8\\pp & $-$8.0\\pp \\\\\nJavaScript & OOD              & 90.2\\%  & 66.5\\% & +23.7\\pp & $-$9.6\\pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAbsolute accuracy degrades by 3.5--9.6\\pp{} on OOD data, with cross-language transfer showing larger drops than within-language generalization, as expected from token vocabulary shift in exception type names and error messages. The lift of exception\\_only over no\\_trace, however, is remarkably preserved across all settings: 23.7--24.8\\pp{} compared to 24.7\\pp{} in-distribution. This stability indicates that the fault detection mechanism (presence/absence of structured error records) transfers across languages, even though the specific exception vocabulary differs. JavaScript shows the largest absolute degradation ($-$9.6\\pp), consistent with its more distinctive error handling patterns (Promise rejections, async TypeErrors) relative to the Python training distribution.\n\n\\subsection{Training Dynamics}\n\\label{sec:dynamics}\n\nLearning curves reveal how efficiently each trace representation conveys verdict-relevant information during training. Table~\\ref{tab:dynamics} reports convergence milestones.\n\n\\begin{table}[t]\n\\centering\n\\caption{Convergence milestones as fraction of total training. ``Never'' indicates the threshold was not reached.}\n\\label{tab:dynamics}\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nCondition & To 80\\% & To 90\\% & To 95\\% & To 99\\% & Final & Shape \\\\\n\\midrule\nexception\\_only & $\\sim$3\\% & $\\sim$5\\% & $\\sim$8\\%  & $\\sim$20\\% & 99.83\\% & Rapid saturation \\\\\nVOTA            & $\\sim$5\\% & $\\sim$10\\% & $\\sim$15\\% & $\\sim$30\\% & 99.41\\% & Moderate saturation \\\\\nfull\\_trace     & $\\sim$30\\% & never & never & never & 81.76\\% & Non-monotonic \\\\\nloop\\_only      & $\\sim$12\\% & never & never & never & 85.63\\% & Slow saturation \\\\\nno\\_trace       & never & never & never & never & 75.13\\% & Low-ceiling plateau \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nException\\_only reaches 90\\% accuracy after just $\\sim$5\\% of training, requiring only 9.2 effective samples per percentage point of improvement. Full\\_trace requires 72.1 samples per percentage point, a 7.4$\\times$ efficiency gap. This difference is not purely a sequence length effect: loop\\_only has similar sequence length to full\\_trace but achieves 5$\\times$ higher learning efficiency, because loop compression extracts denser behavioral signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{Learning efficiency by condition. Lift is measured over the no\\_trace baseline (75.13\\%).}\n\\label{tab:efficiency}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nCondition & Effective samples & Lift (\\pp) & Samples/\\pp & Relative eff. \\\\\n\\midrule\nexception\\_only & 2,858  & 24.7 & 9.2   & 1.0$\\times$ \\\\\nVOTA            & $\\sim$5,800 & 24.3 & 17.5  & 0.53$\\times$ \\\\\nfull\\_trace     & $\\sim$5,800 & 6.6  & 72.1  & 0.13$\\times$ \\\\\nno\\_trace       & $\\sim$5,800 & 3.6  & 132.8 & 0.07$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFull\\_trace exhibits a distinctive non-monotonic learning curve: accuracy peaks at $\\sim$83\\% during epoch 1, drops to $\\sim$76\\% in epoch 2 as the model overfits to trace-specific patterns rather than verdict signals, then partially recovers to 81.76\\% by epoch 3. This oscillation is a dynamic manifestation of information overload, absent from the monotonically saturating exception\\_only and VOTA curves.\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n% ============================================================\n\n\\paragraph{Exception signal as theoretical ceiling.}\nThe two irreducible errors in exception\\_only across all tested models stem from \\texttt{GeneratorExit}, a \\texttt{BaseException} subclass triggered by Python's generator protocol. Because the tracer uniformly labels caught exceptions as \\texttt{[ERROR]}, this control flow mechanism becomes indistinguishable from genuine runtime errors. Improving the tracer to distinguish \\texttt{BaseException} subclasses from \\texttt{Exception} subclasses would likely eliminate these errors, suggesting that the 99.83\\% ceiling is a property of the current trace representation, not a fundamental limit of the approach.\n\n\\paragraph{Scale invariance of exception signal.}\nThree of four models (Qwen-7B, Qwen-1.5B, CodeLlama-13B) achieve identical accuracy (99.83\\%) on exception\\_only despite spanning 1.5B to 13B parameters. This scale invariance is notable: it suggests that exception-based fault detection does not require large model capacity, consistent with the structural simplicity of the signal (presence/absence of \\texttt{[ERROR]} tags combined with minimal type/message context). DeepSeek's lower median (99.33\\%) correlates with its LoRA training sensitivity rather than signal complexity.\n\n\\paragraph{Training-time truncation as confound.}\nDeepSeek's VOTA accuracy (84.45\\%) is partially attributable to training-time trace truncation: 91.7\\% of VOTA training samples exceeded the 2,048-token context window, causing information loss in trace content (though verdict labels were preserved). Group analysis shows train-truncated samples achieve 83.04\\% accuracy vs.\\ 100\\% for intact samples (Fisher exact $p \\approx 0$), establishing truncation as a causal factor. This confounds the cross-model VOTA comparison but does not affect exception\\_only, whose token length falls well below the truncation threshold, further strengthening its position as the most robust signal.\n\n\\paragraph{LoRA initialization sensitivity.}\nDeepSeek exception\\_only shows seed-dependent performance (seed42/456: 99.33\\%, seed123: 91.09\\%), while Qwen exhibits zero variance across seeds. Notably, train loss is nearly identical across DeepSeek seeds (0.1225 vs.\\ 0.122) despite an 8.2\\pp{} accuracy gap, concentrated in fail recall (1.0 vs.\\ 0.705). Token-level loss masks sample-level classification quality, especially for the minority fail class (28.5\\% of data). This finding generalizes beyond our setting: for verdict and detection tasks with class imbalance, train loss convergence does not guarantee task performance, and checkpoint selection must use task-specific metrics.\n\n\\paragraph{Limitations.}\nOur evaluation is limited to a single task (verdict prediction) on a single primary dataset (HumanEval + MBPP-sanitized). While OOD results show preserved lift across languages, the training data covers only Python. The two-model cross-architecture validation, though meaningfully diverse (different architectures, pretraining data, and execution reasoning capability), falls short of a comprehensive universality claim. Exception\\_only's high data duplication rate ($\\sim$40\\% in training) is a natural consequence of representation compactness rather than a data quality issue, but it means effective training diversity is lower than nominal sample counts suggest.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n% ============================================================\n\nWe reframed verdict prediction as fault detection and identified exception events as the minimal sufficient diagnostic signal. Through systematic ablation across four models, we showed that this compact representation (1) achieves near-perfect accuracy with near-perfect calibration, (2) is robust across model scales from 1.5B to 13B parameters, (3) surpasses frontier few-shot baselines at a fraction of the cost, and (4) transfers across programming languages with preserved diagnostic lift. The information density bottleneck, not gradient dilution, is the primary constraint on trace-based verdict prediction, and the solution is signal extraction, not richer context. These findings suggest a general principle for trace-augmented code tasks: identify the task-specific diagnostic signal and isolate it, rather than providing comprehensive execution context and relying on the model to find the needle.\n\n% ============================================================\n% References (placeholder entries for review purposes)\n% ============================================================\n\\begin{thebibliography}{10}\n\n\\bibitem{dcsh2025}\nDCSH Authors.\n\\newblock Execution trace representations for code generation: A comparative study.\n\\newblock In \\emph{EMNLP Findings}, 2025.\n\n\\bibitem{tracepile2025}\nTracePile Authors.\n\\newblock TracePile: Scaling trace-augmented pretraining for code understanding.\n\\newblock In \\emph{NeurIPS}, 2025.\n\n\\bibitem{traced2024}\nTRACED Authors.\n\\newblock TRACED: Execution trace-guided bug detection with encoder models.\n\\newblock In \\emph{ICSE}, 2024.\n\n\\bibitem{coderanker2023}\nCodeRanker Authors.\n\\newblock Ranking code solutions with learned verifiers.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem{codet2023}\nCodeT Authors.\n\\newblock CodeT: Code generation with generated tests.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1db5366b-19af-48ed-a5fe-47774d5f05c7",
  "isSidechain": false,
  "requestId": "req_011CbA8mNwRe2LaVRNiW8DJa",
  "type": "assistant",
  "uuid": "779eed27-3a84-4582-87a8-397d23ceefd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZntXcMCHWvAQASGdM9NMq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 53117,
      "output_tokens": 9454,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 616,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9454,
          "cache_read_input_tokens": 53117,
          "cache_creation_input_tokens": 616,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 616
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

_source line 22 · 2026-05-18T13:47:59.922Z_

<details><summary>↩ Tool result · `toolu_01GRpMJgGpDW3dTWRCmk17eV`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "779eed27-3a84-4582-87a8-397d23ceefd5",
  "isSidechain": false,
  "promptId": "26dc48b8-83e6-4c7b-83d0-0a6fb6e0b0fa",
  "type": "user",
  "uuid": "001f1270-ca62-4b9d-b3ff-d306b9856902",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\newcommand{\\etal}{\\textit{et al.}}\n\\newcommand{\\ie}{\\textit{i.e.}}\n\\newcommand{\\eg}{\\textit{e.g.}}\n\\newcommand{\\pp}{\\,pp}\n\n\\title{Exception Events Are All You Need:\\\\Diagnostic Signal Extraction for Verdict Prediction}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\n% ============================================================\nExecution traces are increasingly used to improve code understanding in language models, yet prior work on trace-based supervised fine-tuning (SFT) reports inconsistent benefits across models and tasks. We study verdict prediction, the binary classification of whether a code solution passes or fails its test suite, and ask: \\emph{what is the minimal sufficient diagnostic signal in an execution trace?} Through systematic component ablation across four architecturally distinct models (1.5B to 13B parameters), we find that exception events, compact structured records of runtime errors, consistently achieve the highest accuracy (99.83\\% on Qwen-2.5-Coder-7B, $\\pm$0.00 across three seeds) while richer trace representations degrade under information overload. A label-only loss ablation decomposes the full-trace-to-compressed-trace gap: 26\\% is attributable to gradient dilution, while 74\\% stems from information density loss that only signal extraction resolves. Cross-model calibration confirms near-perfect confidence alignment (Expected Calibration Error $\\leq$ 0.012) for exception-trained models, a 14--63$\\times$ improvement over no-trace baselines. Task-specific SFT on a 1.5B model matches frontier few-shot performance (GPT-4o, Claude-3.5) at 1/1800th the inference cost. Our results establish a two-tier diagnostic hierarchy for verdict-relevant trace information and demonstrate that fault indicator isolation, not generic trace compression, is the robust mechanism for verdict prediction.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n% ============================================================\n\nExecution traces record the runtime behavior of programs and carry rich information about control flow, variable states, and error conditions. Recent work has explored trace-augmented SFT to improve code generation~\\cite{dcsh2025,tracepile2025} and trace-based classification for bug detection~\\cite{traced2024}. However, a consistent finding across these studies is that trace benefit is model-dependent and format-sensitive: DCSH~\\cite{dcsh2025} tested five trace formats and concluded that ``no single trace representation consistently outperforms others.''\n\nThese prior studies share a common framing: they treat traces as context for \\emph{execution simulation}, asking models to reason about program behavior from detailed step-by-step records. We argue that for verdict prediction, the binary pass/fail classification of test outcomes, this framing is misaligned. Verdict prediction is fundamentally a \\textbf{fault detection} task. The question is not ``what did the program do?'' but ``did the program fail, and why?''\n\nThis reframing motivates a different design principle: instead of providing rich execution context and hoping the model extracts the relevant signal, we should \\emph{identify and isolate the highest-specificity diagnostic signal directly}. Through systematic ablation across four models spanning 1.5B to 13B parameters, we discover that exception events, compact structured records consisting of error type and message, are consistently the most effective trace component. On Qwen-2.5-Coder-7B, exception-only SFT achieves 99.83\\% accuracy with zero variance across three random seeds, and the two remaining errors are traceable to an irreducible representation ambiguity (Python's \\texttt{GeneratorExit} mechanism). Richer representations that include loop behavior or full execution traces suffer from information overload: accuracy degrades and calibration worsens despite containing strictly more information.\n\nA label-only loss ablation quantifies the bottleneck: when gradient dilution is eliminated by masking loss on non-verdict tokens, full-trace accuracy improves by only 4.5\\pp{} (from 81.76\\% to 86.22\\%), leaving a 13\\pp{} gap to compressed traces. Information density, not gradient dilution, is the primary constraint. Budget curve analysis across four models confirms that diagnostic signal concentrates in the trace tail with diminishing returns: tail-512 tokens ($\\sim$94\\%) outperform head-2048 tokens ($\\sim$79\\%) by $\\sim$15\\pp, and all models exhibit smooth log-shaped curves without a shared critical threshold.\n\nOur contributions are:\n\\begin{itemize}\n    \\item We establish that exception events are the most effective and robust trace component for verdict prediction, achieving near-perfect accuracy across four models (99.83\\% on three models, 92--99\\% on DeepSeek) with near-perfect calibration (ECE $\\leq$ 0.012).\n    \\item We quantify the information density bottleneck through label-only loss ablation (26\\% gradient dilution vs.\\ 74\\% information overload) and budget curve analysis showing smooth diminishing returns concentrated in trace tails.\n    \\item We identify a two-tier diagnostic hierarchy: Tier~1 signals (exception events, assertion outcomes) are individually near-perfect and sufficient; Tier~2 signals (loop behavior) carry moderate signal but introduce noise when combined with Tier~1.\n    \\item We demonstrate that task-specific SFT on models as small as 1.5B surpasses frontier few-shot baselines (GPT-4o, Claude-3.5) with 16--20$\\times$ fewer errors at 1/1800th the cost, and that exception-based training generalizes across programming languages with preserved lift ($\\sim$24\\pp) over no-trace baselines.\n\\end{itemize}\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n% ============================================================\n\n\\paragraph{Trace-augmented code models.}\nDCSH~\\cite{dcsh2025} evaluated five trace representations for code generation via SFT on models up to 16B parameters, finding no universally superior format. TracePile~\\cite{tracepile2025} scaled trace-augmented pretraining to 2.6M samples but evaluated only generative tasks. Both studies frame traces as execution simulation context. TRACED~\\cite{traced2024} showed that traces improve encoder-based bug classification, providing the closest precedent to our work, though they did not perform component ablation or test decoder-based models. Our work differs by reframing verdict prediction as fault detection, performing fine-grained signal decomposition, and testing across multiple decoder architectures.\n\n\\paragraph{Verdict and test outcome prediction.}\nPredicting whether code passes tests has been studied as a filtering mechanism for code generation~\\cite{coderanker2023,codet2023}. These approaches typically use the generated code as input without execution information. We show that adding even minimal execution signals (exception events) transforms this task from a moderately difficult classification problem (75\\%) to a near-solved one (99.83\\%).\n\n\\paragraph{Calibration in code models.}\nModel calibration, the alignment between predicted confidence and actual correctness, has received limited attention in code tasks. We provide the first systematic calibration analysis across trace conditions, showing that exception signals improve ECE by 14--63$\\times$ over no-trace baselines.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n% ============================================================\n\n\\subsection{Task Definition}\n\nGiven a code solution $s$ and its test suite $T$, verdict prediction is the binary classification: $f(s, c) \\rightarrow \\{pass, fail\\}$, where $c$ is an optional execution context derived from running $s$ against $T$. We study how the choice of $c$ affects prediction accuracy and calibration.\n\n\\subsection{Trace Representations}\n\nWe define seven trace conditions spanning a spectrum from no execution information to full traces:\n\n\\begin{itemize}\n    \\item \\textbf{no\\_trace}: Code only, no execution information ($c = \\emptyset$).\n    \\item \\textbf{full\\_trace}: Complete execution trace including all control flow, variable states, and exception information.\n    \\item \\textbf{label\\_only}: Full trace input with loss computed only on the verdict token, eliminating gradient dilution.\n    \\item \\textbf{VOTA} (Verdict-Optimized Trace Abstraction): Compressed trace retaining three components: loop summaries, exception events, and assertion outcomes.\n    \\item \\textbf{exception\\_only}: Only structured exception records (\\texttt{[ERROR] type: ... message: ...}).\n    \\item \\textbf{loop\\_only}: Only loop behavior summaries from VOTA compression.\n    \\item \\textbf{ae\\_only}: Only assertion/expected-value comparison outcomes.\n\\end{itemize}\n\n\\subsection{VOTA Trace Compression}\n\nVOTA applies three extraction operations to raw traces: (1) \\textbf{Loop compression} summarizes repetitive loop iterations into structured summaries capturing iteration count, representative values, and termination conditions. (2) \\textbf{Exception extraction} isolates structured error records in the format \\texttt{[ERROR] type: message}. (3) \\textbf{Assertion-point extraction} captures actual vs.\\ expected value comparisons at assertion sites. The key finding of this work is that VOTA's primary value lies in operation (2), fault indicator isolation, rather than generic compression.\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Dataset.} We construct a verdict prediction dataset from HumanEval (164 problems) and MBPP-sanitized (427 problems), generating 10 LLM-produced solutions per problem for a total of 5,910 samples. Training uses 4,720 samples (2,858 unique for exception\\_only due to representation compactness); testing uses 1,190 samples. Train-test input overlap is zero.\n\n\\paragraph{Models.} We evaluate four models: Qwen-2.5-Coder-7B, Qwen-2.5-Coder-1.5B, DeepSeek-Coder-6.7B, and CodeLlama-13B-Instruct. These span three architecture families, parameter scales from 1.5B to 13B, and pretraining corpora from 2T to 5.5T tokens.\n\n\\paragraph{Training.} All models are fine-tuned with LoRA (rank 16, $\\alpha$=32) for 3 epochs with learning rate $2\\times10^{-4}$ and batch size 4. Multi-seed evaluation (seeds 42, 123, 456) is performed for robustness assessment.\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:exp}\n% ============================================================\n\n\\subsection{Information Locality: Budget Curve Analysis}\n\\label{sec:budget}\n\nTo understand where diagnostic information resides within traces, we evaluate tail-$k$ and head-$k$ truncation across four models. Table~\\ref{tab:budget} presents accuracy at six budget points including a new tail-384 measurement that probes the 256--512 token transition region.\n\n\\begin{table}[t]\n\\centering\n\\caption{Budget curve with tail-384 interpolation across four models. Accuracy (\\%) at each token budget. $\\Delta$ columns show per-step gains. Sharpness index measures the position of tail-384 within the 256--512 interval (0 = stays at 256 level, 1 = jumps to 512 level, 0.5 = exact midpoint).}\n\\label{tab:budget}\n\\small\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nModel & tail-256 & tail-384 & tail-512 & tail-1024 & tail-2048 & $\\Delta_{256 \\to 384}$ & $\\Delta_{384 \\to 512}$ & Sharpness \\\\\n\\midrule\nQwen-7B     & 77.5 & 85.6 & 93.6 & 96.5 & 97.3 & +8.1 & +8.0 & 0.52 \\\\\nDeepSeek-6.7B & 76.4 & 84.3 & 93.9 & 96.5 & 95.0 & +7.9 & +9.6 & 0.46 \\\\\nQwen-1.5B   & 72.6 & 83.2 & 95.6 & 96.6 & 97.9 & +10.6 & +12.4 & 0.44 \\\\\nCodeLlama-13B & 77.9 & 88.3 & 97.5 & 98.2 & --- & +10.4 & +9.2 & 0.54 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mean sharpness index across models is 0.49 (range: 0.44--0.54), indicating that tail-384 falls almost exactly at the midpoint of the 256--512 transition. This rules out a sharp phase transition: information accumulates gradually with token budget, following a log-shaped diminishing returns curve. Each model's steepest gain region differs slightly in position and magnitude, but no model exhibits a discrete threshold.\n\nTwo key findings emerge. First, \\textbf{information concentrates in trace tails}: all four models achieve tail-384 accuracy (83--88\\%) that exceeds head-2048 accuracy ($\\sim$79\\%) by 4--9\\pp, confirming that the final tokens of an execution trace, which contain crash points and stack traces, carry more diagnostic value than the first 2,048 tokens. Second, \\textbf{tail-512 substantially outperforms head-2048} ($\\sim$94\\% vs.\\ $\\sim$79\\%, $\\Delta \\approx 15$\\pp), providing strong evidence for information locality: a quarter of the tokens from the trace tail carry more verdict-relevant signal than eight times as many tokens from the head.\n\n\\subsection{Cross-Seed Robustness}\n\\label{sec:seeds}\n\nPoint estimates from single training runs may be unreliable due to LoRA initialization sensitivity. Table~\\ref{tab:crossseed} reports tail-512 accuracy across three seeds and four models.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed tail-512 robustness (3 seeds $\\times$ 4 models). All worst-seed results exceed head-2048 baselines ($\\sim$79--81\\%).}\n\\label{tab:crossseed}\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nModel & Seed 42 & Seed 123 & Seed 456 & Mean & $\\sigma$ & Band \\\\\n\\midrule\nQwen-7B       & 93.6 & 91.9 & 94.7 & 93.4 & 1.4\\pp & 2.8\\pp \\\\\nDeepSeek-6.7B & 93.9 & 89.2 & 93.5 & 92.2 & 2.6\\pp & 4.7\\pp \\\\\nQwen-1.5B     & 95.6 & 93.2 & 94.9 & 94.6 & 1.2\\pp & 2.4\\pp \\\\\nCodeLlama-13B & 97.5 & 95.8 & 97.1 & 96.8 & 0.9\\pp & 1.7\\pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-seed standard deviation ranges from 0.9\\pp{} (CodeLlama-13B) to 2.6\\pp{} (DeepSeek-6.7B), with a cross-model average of 1.54\\pp. The worst single-seed result (DeepSeek seed 123, 89.2\\%) still exceeds the best head-2048 baseline ($\\sim$81\\%) by 8\\pp. Rank ordering is perfectly preserved across all seeds: CodeLlama-13B $>$ Qwen-1.5B $>$ Qwen-7B $\\geq$ DeepSeek-6.7B. Models at capacity extremes (1.5B and 13B) show lower variance ($\\overline{\\sigma}$ = 1.1\\pp), while mid-scale models exhibit higher variance ($\\overline{\\sigma}$ = 2.0\\pp), possibly reflecting more complex LoRA optimization landscapes at intermediate scales.\n\n\\subsection{Cross-Model Calibration}\n\\label{sec:calibration}\n\nBeyond accuracy, we assess whether models trained on exception signals produce well-calibrated confidence estimates. Table~\\ref{tab:calibration} reports Expected Calibration Error (ECE) and Brier score for exception\\_only across four models.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model calibration for exception\\_only. ECE ratio compares against no\\_trace baseline (ECE = 0.171).}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & Accuracy & ECE & Brier & ECE ratio vs.\\ no\\_trace \\\\\n\\midrule\nQwen-2.5-Coder-7B     & 99.83\\% & 0.0027 & 0.0013 & 63$\\times$ \\\\\nCodeLlama-13B-Instruct & 99.83\\% & 0.003  & 0.002  & 57$\\times$ \\\\\nQwen-2.5-Coder-1.5B   & 99.83\\% & 0.005  & 0.003  & 34$\\times$ \\\\\nDeepSeek-Coder-6.7B    & 99.33\\% & 0.012  & 0.006  & 14$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll four models achieve ECE $\\leq$ 0.012 when trained on exception signals, representing a 14--63$\\times$ improvement over the no\\_trace baseline (ECE = 0.171). Three of four models reach identical accuracy (99.83\\%) with only two errors each, both attributable to the same irreducible representation ambiguity (\\texttt{GeneratorExit}; see Section~\\ref{sec:error}). DeepSeek's slightly higher ECE (0.012) correlates with its higher error count (8 vs.\\ 2) rather than signal quality differences. The near-perfect calibration means exception-trained models not only predict correctly but produce confidence scores that faithfully reflect their certainty, a property valuable for deployment in CI/CD pipelines where abstention on uncertain cases can prevent false signals.\n\n\\subsection{Error Analysis}\n\\label{sec:error}\n\nWe analyze failure modes across all seven trace conditions on Qwen-7B (seed 42) to understand what each representation gets wrong and why. Table~\\ref{tab:errors} presents the error distribution.\n\n\\begin{table}[t]\n\\centering\n\\caption{Error mode distribution by condition (Qwen-7B, seed 42). Directions indicate whether errors are fail$\\to$pass (false positives) or pass$\\to$fail (false negatives).}\n\\label{tab:errors}\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nCondition & Errors & Rate & fail$\\to$pass & pass$\\to$fail & Dominant mode \\\\\n\\midrule\nexception\\_only & 2   & 0.17\\% & 0\\%  & 100\\% & GeneratorExit irreducible \\\\\nae\\_only        & 1   & 0.08\\% & 0\\%  & 100\\% & GeneratorExit variant \\\\\nVOTA            & 7   & 0.59\\% & 57\\% & 43\\%  & Tier~2 noise conflict \\\\\nloop\\_only      & 171 & 14.4\\% & 36\\% & 64\\%  & Insufficient diagnostic signal \\\\\nfull\\_trace     & 217 & 18.2\\% & 47\\% & 53\\%  & Information overload \\\\\nlabel\\_only     & 164 & 13.8\\% & 65\\% & 35\\%  & Gradient dilution residual \\\\\nno\\_trace       & 296 & 24.9\\% & 70\\% & 30\\%  & Majority class bias \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Tier~1 errors are irreducible.} Exception\\_only's two errors (samples 901 and 905, both from \\texttt{check\\_dict\\_case} in HumanEval/95) stem from Python's \\texttt{all()} short-circuiting on generator expressions, which triggers \\texttt{GeneratorExit} (a \\texttt{BaseException} subclass used for internal control flow, not a real error). The tracer labels this as \\texttt{[ERROR]}, making it indistinguishable from genuine failures in the exception\\_only representation. These same two errors appear identically across all three seeds (Jaccard overlap = 0.85 across models), confirming they are a data/representation property rather than a model artifact. The 99.83\\% accuracy is thus the theoretical ceiling for this representation.\n\n\\paragraph{Full-trace errors correlate with length.} Table~\\ref{tab:length_errors} shows that error rate in the full\\_trace condition increases with trace length (Pearson $r$ = 0.41), from $\\sim$9\\% for traces under 500 tokens to $\\sim$33\\% for traces over 1,500 tokens. This length-error correlation is direct evidence of information overload: longer traces bury diagnostic signals in irrelevant execution details.\n\n\\begin{table}[t]\n\\centering\n\\caption{Error rate by trace length (full\\_trace condition, Qwen-7B).}\n\\label{tab:length_errors}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nLength bucket & Samples & Errors & Error rate \\\\\n\\midrule\n$<$500 tokens   & $\\sim$190 & $\\sim$17 & $\\sim$9\\% \\\\\n500--1000 tokens & $\\sim$340 & $\\sim$54 & $\\sim$16\\% \\\\\n1000--1500 tokens & $\\sim$370 & $\\sim$72 & $\\sim$19\\% \\\\\n$>$1500 tokens  & $\\sim$290 & $\\sim$96 & $\\sim$33\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Tier~1 and Tier~2 fail differently.} Cross-condition error overlap analysis reveals that Tier~1 (exception/ae) and Tier~2 (loop/full\\_trace) error sets are nearly disjoint (Jaccard = 0.01). Tier~1 failures stem from representation ambiguity (the \\texttt{GeneratorExit} cases), while Tier~2 failures involve reasoning complexity (interpreting loop behavior patterns). VOTA's five unique errors beyond the two shared with exception\\_only arise from Tier~2 noise: three cases where loop summaries present normal behavior alongside exceptions (conflicting signals) and two cases where Tier~2 tokens dilute attention to exception signals.\n\n\\subsection{Frontier Model Comparison}\n\\label{sec:frontier}\n\nTo contextualize SFT performance, we compare against frontier models in few-shot settings. Table~\\ref{tab:frontier} presents the comparison.\n\n\\begin{table}[t]\n\\centering\n\\caption{SFT vs.\\ frontier few-shot comparison. Cost is approximate per-run inference cost for the 1,190-sample test set.}\n\\label{tab:frontier}\n\\small\n\\begin{tabular}{@{}llccccc@{}}\n\\toprule\nMethod & Model & Input & Shots & Accuracy & Errors & Cost \\\\\n\\midrule\nSFT & Qwen-7B        & exception & --- & 99.83\\% & 2    & \\$0.01 \\\\\nSFT & Qwen-1.5B      & exception & --- & 99.83\\% & 2    & \\$0.005 \\\\\nSFT & CodeLlama-13B  & exception & --- & 99.83\\% & 2    & \\$0.02 \\\\\n\\midrule\nFew-shot & Claude-3.5 & exception & 3   & 97.2\\%  & $\\sim$33 & \\$10 \\\\\nFew-shot & GPT-4o     & exception & 3   & 96.6\\%  & $\\sim$40 & \\$8 \\\\\nFew-shot & Claude-3.5 & exception & 0   & 95.8\\%  & $\\sim$50 & \\$7 \\\\\nFew-shot & GPT-4o     & exception & 0   & 95.2\\%  & $\\sim$57 & \\$5 \\\\\n\\midrule\nFew-shot & Claude-3.5 & no\\_trace & 0   & 82.1\\%  & $\\sim$213 & \\$5 \\\\\nFew-shot & GPT-4o     & no\\_trace & 0   & 80.5\\%  & $\\sim$232 & \\$3 \\\\\nSFT      & Qwen-7B    & no\\_trace & --- & 75.1\\%  & 296  & \\$0.01 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWhile the accuracy gap between SFT and frontier 3-shot appears modest (2.6\\pp{} vs.\\ Claude-3.5), the error count perspective is revealing: SFT produces 2 errors versus $\\sim$33 for the best frontier model, a 16.5$\\times$ reduction. GPT-4o 3-shot makes 20$\\times$ more errors. Inference cost differs by approximately 1,800$\\times$. Frontier models also benefit substantially from exception signals: GPT-4o improves from 80.5\\% (no\\_trace) to 95.2\\% (exception, 0-shot), a 14.7\\pp{} lift that independently confirms the diagnostic value of exception events.\n\n\\subsection{Out-of-Distribution Generalization}\n\\label{sec:ood}\n\nWe evaluate whether exception-based training transfers to unseen projects and programming languages using 500-sample test sets per language. Table~\\ref{tab:ood} reports results.\n\n\\begin{table}[t]\n\\centering\n\\caption{In-distribution vs.\\ OOD accuracy by language (Qwen-7B, exception\\_only SFT).}\n\\label{tab:ood}\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nLanguage & Setting & exception\\_only & no\\_trace & Lift & Deg.\\ vs.\\ ID \\\\\n\\midrule\nPython & ID (HumanEval+MBPP)  & 99.83\\% & 75.1\\% & +24.7\\pp & baseline \\\\\nPython & OOD (new projects)   & 96.3\\%  & 71.5\\% & +24.8\\pp & $-$3.5\\pp \\\\\nJava   & OOD                  & 91.8\\%  & 68.0\\% & +23.8\\pp & $-$8.0\\pp \\\\\nJavaScript & OOD              & 90.2\\%  & 66.5\\% & +23.7\\pp & $-$9.6\\pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAbsolute accuracy degrades by 3.5--9.6\\pp{} on OOD data, with cross-language transfer showing larger drops than within-language generalization, as expected from token vocabulary shift in exception type names and error messages. The lift of exception\\_only over no\\_trace, however, is remarkably preserved across all settings: 23.7--24.8\\pp{} compared to 24.7\\pp{} in-distribution. This stability indicates that the fault detection mechanism (presence/absence of structured error records) transfers across languages, even though the specific exception vocabulary differs. JavaScript shows the largest absolute degradation ($-$9.6\\pp), consistent with its more distinctive error handling patterns (Promise rejections, async TypeErrors) relative to the Python training distribution.\n\n\\subsection{Training Dynamics}\n\\label{sec:dynamics}\n\nLearning curves reveal how efficiently each trace representation conveys verdict-relevant information during training. Table~\\ref{tab:dynamics} reports convergence milestones.\n\n\\begin{table}[t]\n\\centering\n\\caption{Convergence milestones as fraction of total training. ``Never'' indicates the threshold was not reached.}\n\\label{tab:dynamics}\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nCondition & To 80\\% & To 90\\% & To 95\\% & To 99\\% & Final & Shape \\\\\n\\midrule\nexception\\_only & $\\sim$3\\% & $\\sim$5\\% & $\\sim$8\\%  & $\\sim$20\\% & 99.83\\% & Rapid saturation \\\\\nVOTA            & $\\sim$5\\% & $\\sim$10\\% & $\\sim$15\\% & $\\sim$30\\% & 99.41\\% & Moderate saturation \\\\\nfull\\_trace     & $\\sim$30\\% & never & never & never & 81.76\\% & Non-monotonic \\\\\nloop\\_only      & $\\sim$12\\% & never & never & never & 85.63\\% & Slow saturation \\\\\nno\\_trace       & never & never & never & never & 75.13\\% & Low-ceiling plateau \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nException\\_only reaches 90\\% accuracy after just $\\sim$5\\% of training, requiring only 9.2 effective samples per percentage point of improvement. Full\\_trace requires 72.1 samples per percentage point, a 7.4$\\times$ efficiency gap. This difference is not purely a sequence length effect: loop\\_only has similar sequence length to full\\_trace but achieves 5$\\times$ higher learning efficiency, because loop compression extracts denser behavioral signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{Learning efficiency by condition. Lift is measured over the no\\_trace baseline (75.13\\%).}\n\\label{tab:efficiency}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nCondition & Effective samples & Lift (\\pp) & Samples/\\pp & Relative eff. \\\\\n\\midrule\nexception\\_only & 2,858  & 24.7 & 9.2   & 1.0$\\times$ \\\\\nVOTA            & $\\sim$5,800 & 24.3 & 17.5  & 0.53$\\times$ \\\\\nfull\\_trace     & $\\sim$5,800 & 6.6  & 72.1  & 0.13$\\times$ \\\\\nno\\_trace       & $\\sim$5,800 & 3.6  & 132.8 & 0.07$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFull\\_trace exhibits a distinctive non-monotonic learning curve: accuracy peaks at $\\sim$83\\% during epoch 1, drops to $\\sim$76\\% in epoch 2 as the model overfits to trace-specific patterns rather than verdict signals, then partially recovers to 81.76\\% by epoch 3. This oscillation is a dynamic manifestation of information overload, absent from the monotonically saturating exception\\_only and VOTA curves.\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n% ============================================================\n\n\\paragraph{Exception signal as theoretical ceiling.}\nThe two irreducible errors in exception\\_only across all tested models stem from \\texttt{GeneratorExit}, a \\texttt{BaseException} subclass triggered by Python's generator protocol. Because the tracer uniformly labels caught exceptions as \\texttt{[ERROR]}, this control flow mechanism becomes indistinguishable from genuine runtime errors. Improving the tracer to distinguish \\texttt{BaseException} subclasses from \\texttt{Exception} subclasses would likely eliminate these errors, suggesting that the 99.83\\% ceiling is a property of the current trace representation, not a fundamental limit of the approach.\n\n\\paragraph{Scale invariance of exception signal.}\nThree of four models (Qwen-7B, Qwen-1.5B, CodeLlama-13B) achieve identical accuracy (99.83\\%) on exception\\_only despite spanning 1.5B to 13B parameters. This scale invariance is notable: it suggests that exception-based fault detection does not require large model capacity, consistent with the structural simplicity of the signal (presence/absence of \\texttt{[ERROR]} tags combined with minimal type/message context). DeepSeek's lower median (99.33\\%) correlates with its LoRA training sensitivity rather than signal complexity.\n\n\\paragraph{Training-time truncation as confound.}\nDeepSeek's VOTA accuracy (84.45\\%) is partially attributable to training-time trace truncation: 91.7\\% of VOTA training samples exceeded the 2,048-token context window, causing information loss in trace content (though verdict labels were preserved). Group analysis shows train-truncated samples achieve 83.04\\% accuracy vs.\\ 100\\% for intact samples (Fisher exact $p \\approx 0$), establishing truncation as a causal factor. This confounds the cross-model VOTA comparison but does not affect exception\\_only, whose token length falls well below the truncation threshold, further strengthening its position as the most robust signal.\n\n\\paragraph{LoRA initialization sensitivity.}\nDeepSeek exception\\_only shows seed-dependent performance (seed42/456: 99.33\\%, seed123: 91.09\\%), while Qwen exhibits zero variance across seeds. Notably, train loss is nearly identical across DeepSeek seeds (0.1225 vs.\\ 0.122) despite an 8.2\\pp{} accuracy gap, concentrated in fail recall (1.0 vs.\\ 0.705). Token-level loss masks sample-level classification quality, especially for the minority fail class (28.5\\% of data). This finding generalizes beyond our setting: for verdict and detection tasks with class imbalance, train loss convergence does not guarantee task performance, and checkpoint selection must use task-specific metrics.\n\n\\paragraph{Limitations.}\nOur evaluation is limited to a single task (verdict prediction) on a single primary dataset (HumanEval + MBPP-sanitized). While OOD results show preserved lift across languages, the training data covers only Python. The two-model cross-architecture validation, though meaningfully diverse (different architectures, pretraining data, and execution reasoning capability), falls short of a comprehensive universality claim. Exception\\_only's high data duplication rate ($\\sim$40\\% in training) is a natural consequence of representation compactness rather than a data quality issue, but it means effective training diversity is lower than nominal sample counts suggest.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n% ============================================================\n\nWe reframed verdict prediction as fault detection and identified exception events as the minimal sufficient diagnostic signal. Through systematic ablation across four models, we showed that this compact representation (1) achieves near-perfect accuracy with near-perfect calibration, (2) is robust across model scales from 1.5B to 13B parameters, (3) surpasses frontier few-shot baselines at a fraction of the cost, and (4) transfers across programming languages with preserved diagnostic lift. The information density bottleneck, not gradient dilution, is the primary constraint on trace-based verdict prediction, and the solution is signal extraction, not richer context. These findings suggest a general principle for trace-augmented code tasks: identify the task-specific diagnostic signal and isolate it, rather than providing comprehensive execution context and relying on the model to find the needle.\n\n% ============================================================\n% References (placeholder entries for review purposes)\n% ============================================================\n\\begin{thebibliography}{10}\n\n\\bibitem{dcsh2025}\nDCSH Authors.\n\\newblock Execution trace representations for code generation: A comparative study.\n\\newblock In \\emph{EMNLP Findings}, 2025.\n\n\\bibitem{tracepile2025}\nTracePile Authors.\n\\newblock TracePile: Scaling trace-augmented pretraining for code understanding.\n\\newblock In \\emph{NeurIPS}, 2025.\n\n\\bibitem{traced2024}\nTRACED Authors.\n\\newblock TRACED: Execution trace-guided bug detection with encoder models.\n\\newblock In \\emph{ICSE}, 2024.\n\n\\bibitem{coderanker2023}\nCodeRanker Authors.\n\\newblock Ranking code solutions with learned verifiers.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem{codet2023}\nCodeT Authors.\n\\newblock CodeT: Code generation with generated tests.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "779eed27-3a84-4582-87a8-397d23ceefd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-st…",
  "leafUuid": "001f1270-ca62-4b9d-b3ff-d306b9856902",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper from experiment data",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c"
}
```

---

### Tool call

_source line 25 · 2026-05-18T13:48:04.521Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NpGLR3rADwEhSpoWTZQ77p`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "001f1270-ca62-4b9d-b3ff-d306b9856902",
  "isSidechain": false,
  "requestId": "req_011CbA91jP8iKJu33G2F6jzP",
  "type": "assistant",
  "uuid": "a27e7d77-037c-4fd6-8778-f6a12d58435c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F7J5qS176tPxZY57Ch2NbT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9519,
      "cache_read_input_tokens": 53733,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9519,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 53733,
          "cache_creation_input_tokens": 9519,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9519
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

_source line 26 · 2026-05-18T13:48:05.582Z_

<details><summary>↩ Tool result · `toolu_01NpGLR3rADwEhSpoWTZQ77p`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
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

LaTeX Warning: Citation `dcsh2025' on page 1 undefined on input line 41.


LaTeX Warning: Citation `tracepile2025' on page 1 undefined on input line 41.


LaTeX Warning: Citation `traced2024' on page 1 undefined on input line 41.


LaTeX Warning: Citation `dcsh2025' on page 1 undefined on input line 41.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

LaTeX Warning: Citation `dcsh2025' on page 2 undefined on input line 63.


LaTeX Warning: Citation `tracepile2025' on page 2 undefined on input line 63.


LaTeX Warning: Citation `traced2024' on page 2 undefined on input line 63.


LaTeX Warning: Citation `coderanker2023' on page 2 undefined on input line 66.


LaTeX Warning: Citation `codet2023' on page 2 undefined on input line 66.

[2]
Overfull \hbox (7.48201pt too wide) in paragraph at lines 102--103
 []\T1/cmr/bx/n/10.95 Models.[] \T1/cmr/m/n/10.95 We eval-u-ate four mod-els: Q
wen-2.5-Coder-7B, Qwen-2.5-Coder-1.5B, DeepSeek-Coder-

LaTeX Warning: Reference `tab:budget' on page 3 undefined on input line 114.

[3]
Overfull \hbox (9.76945pt too wide) in paragraph at lines 121--131
 [][] 

LaTeX Warning: Reference `tab:crossseed' on page 4 undefined on input line 140.



LaTeX Warning: Reference `tab:calibration' on page 4 undefined on input line 16
4.

[4]

LaTeX Warning: Reference `sec:error' on page 5 undefined on input line 183.


LaTeX Warning: Reference `tab:errors' on page 5 undefined on input line 188.


LaTeX Warning: Reference `tab:length_errors' on page 5 undefined on input line 
212.

[5]

LaTeX Warning: Reference `tab:frontier' on page 6 undefined on input line 236.


LaTeX Warning: Reference `tab:ood' on page 6 undefined on input line 268.

[6]

LaTeX Warning: Reference `tab:dynamics' on page 7 undefined on input line 292.


Overfull \hbox (13.62108pt too wide) in paragraph at lines 342--343
 []\T1/cmr/bx/n/10.95 Scale in-vari-ance of ex-cep-tion sig-nal.[] \T1/cmr/m/n/
10.95 Three of four mod-els (Qwen-7B, Qwen-1.5B, CodeLlama-
[7] [8] [9] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmsy8.pfb>
Output written on paper.pdf (9 pages, 211978 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] [2]
Overfull \hbox (7.48201pt too wide) in paragraph at lines 102--103
 []\T1/cmr/bx/n/10.95 Models.[] \T1/cmr/m/n/10.95 We eval-u-ate four mod-els: Q
wen-2.5-Coder-7B, Qwen-2.5-Coder-1.5B, DeepSeek-Coder-
[3]
Overfull \hbox (9.76945pt too wide) in paragraph at lines 121--131
 [][] 
[4] [5] [6]
Overfull \hbox (13.62108pt too wide) in paragraph at lines 342--343
 []\T1/cmr/bx/n/10.95 Scale in-vari-ance of ex-cep-tion sig-nal.[] \T1/cmr/m/n/
10.95 Three of four mod-els (Qwen-7B, Qwen-1.5B, CodeLlama-
[7] [8] [9] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmsy8.pfb>
Output written on paper.pdf (9 pages, 213386 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a27e7d77-037c-4fd6-8778-f6a12d58435c",
  "isSidechain": false,
  "promptId": "26dc48b8-83e6-4c7b-83d0-0a6fb6e0b0fa",
  "type": "user",
  "uuid": "24727cf0-525f-4ce5-b5cc-3e2ea3cfdfe7",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nLaTeX Warning: Citation `dcsh2025' on page 1 undefined on input line 41.\n\n\nLaTeX Warning: Citation `tracepile2025' on page 1 undefined on input line 41.\n\n\nLaTeX Warning: Citation `traced2024' on page 1 undefined on input line 41.\n\n\nLaTeX Warning: Citation `dcsh2025' on page 1 undefined on input line 41.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nLaTeX Warning: Citation `dcsh2025' on page 2 undefined on input line 63.\n\n\nLaTeX Warning: Citation `tracepile2025' on page 2 undefined on input line 63.\n\n\nLaTeX Warning: Citation `traced2024' on page 2 undefined on input line 63.\n\n\nLaTeX Warning: Citation `coderanker2023' on page 2 undefined on input line 66.\n\n\nLaTeX Warning: Citation `codet2023' on page 2 undefined on input line 66.\n\n[2]\nOverfull \\hbox (7.48201pt too wide) in paragraph at lines 102--103\n []\\T1/cmr/bx/n/10.95 Models.[] \\T1/cmr/m/n/10.95 We eval-u-ate four mod-els: Q\nwen-2.5-Coder-7B, Qwen-2.5-Coder-1.5B, DeepSeek-Coder-\n\nLaTeX Warning: Reference `tab:budget' on page 3 undefined on input line 114.\n\n[3]\nOverfull \\hbox (9.76945pt too wide) in paragraph at lines 121--131\n [][] \n\nLaTeX Warning: Reference `tab:crossseed' on page 4 undefined on input line 140.\n\n\n\nLaTeX Warning: Reference `tab:calibration' on page 4 undefined on input line 16\n4.\n\n[4]\n\nLaTeX Warning: Reference `sec:error' on page 5 undefined on input line 183.\n\n\nLaTeX Warning: Reference `tab:errors' on page 5 undefined on input line 188.\n\n\nLaTeX Warning: Reference `tab:length_errors' on page 5 undefined on input line \n212.\n\n[5]\n\nLaTeX Warning: Reference `tab:frontier' on page 6 undefined on input line 236.\n\n\nLaTeX Warning: Reference `tab:ood' on page 6 undefined on input line 268.\n\n[6]\n\nLaTeX Warning: Reference `tab:dynamics' on page 7 undefined on input line 292.\n\n\nOverfull \\hbox (13.62108pt too wide) in paragraph at lines 342--343\n []\\T1/cmr/bx/n/10.95 Scale in-vari-ance of ex-cep-tion sig-nal.[] \\T1/cmr/m/n/\n10.95 Three of four mod-els (Qwen-7B, Qwen-1.5B, CodeLlama-\n[7] [8] [9] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmsy8.pfb>\nOutput written on paper.pdf (9 pages, 211978 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2]\nOverfull \\hbox (7.48201pt too wide) in paragraph at lines 102--103\n []\\T1/cmr/bx/n/10.95 Models.[] \\T1/cmr/m/n/10.95 We eval-u-ate four mod-els: Q\nwen-2.5-Coder-7B, Qwen-2.5-Coder-1.5B, DeepSeek-Coder-\n[3]\nOverfull \\hbox (9.76945pt too wide) in paragraph at lines 121--131\n [][] \n[4] [5] [6]\nOverfull \\hbox (13.62108pt too wide) in paragraph at lines 342--343\n []\\T1/cmr/bx/n/10.95 Scale in-vari-ance of ex-cep-tion sig-nal.[] \\T1/cmr/m/n/\n10.95 Three of four mod-els (Qwen-7B, Qwen-1.5B, CodeLlama-\n[7] [8] [9] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmsy8.pfb>\nOutput written on paper.pdf (9 pages, 213386 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a27e7d77-037c-4fd6-8778-f6a12d58435c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-18T13:48:12.408Z_

编译成功，9 页 PDF 已生成。论文覆盖了 `experiment_data.json` 中全部 6 个实验（budget curve / cross-seed robustness / cross-model calibration / error analysis / frontier comparison / OOD generalization / training dynamics），每个实验对应独立的 subsection 和 table。所有定量数据来自实验数据文件，narrative 遵循 paper\_framing.md 的三条 claim 结构和 narrative guidance 中对 Claim 2 的修订方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24727cf0-525f-4ce5-b5cc-3e2ea3cfdfe7",
  "isSidechain": false,
  "requestId": "req_011CbA9294RJECfH7ij3wcaD",
  "type": "assistant",
  "uuid": "b5360e71-b513-465f-932b-7c518518ed8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/median",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrEigJkFGqp2Dgi6KddLhd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6844,
      "cache_read_input_tokens": 63252,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6844,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 63252,
          "cache_creation_input_tokens": 6844,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6844
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-st…",
  "leafUuid": "b5360e71-b513-465f-932b-7c518518ed8d",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper from experiment data",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-st…",
  "leafUuid": "b5360e71-b513-465f-932b-7c518518ed8d",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper from experiment data",
  "sessionId": "9303450c-67a8-42e0-bab2-dba2fc96a15c"
}
```

---
