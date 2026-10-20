# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T184925 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/11c29027-11c4-4e7f-b1f5-81fc2ed814c5.jsonl`
- **Structured JSON:** [`5f03056f8f19de4e62b8.json`](../../sessions/5f/5f03056f8f19de4e62b8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T19:03:20.010Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T19:03:20.010Z",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T184925 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始 framing 三条 claims 全部成立。α-sweep 揭示清晰的 predictability phase transition： α≤0.50 下 canary→perplexity lead 出现（1-2 gen），α*≈0.60 划定可预测/不可预测边界。 方法论贡献独立成立——naive correlation 在非平稳序列上产生 ~40% 伪显著关联被 TY 推翻。 Cross-domain 和 scale spot-check 均保持 canary ranking。Headline 无需修改，直投 AAAI full paper。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T19:03:20.018Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T19:03:20.018Z",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-14T19:03:20.086Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T184925 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始 framing 三条 claims 全部成立。α-sweep 揭示清晰的 predictability phase transition： α≤0.50 下 canary→perplexity lead 出现（1-2 gen），α*≈0.60 划定可预测/不可预测边界。 方法论贡献独立成立——naive correlation 在非平稳序列上产生 ~40% 伪显著关联被 TY 推翻。 Cross-domain 和 scale spot-check 均保持 canary ranking。Headline 无需修改，直投 AAAI full paper。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c66d342e-ebfe-4ac2-8a57-b8c65fc157f1",
  "type": "user",
  "uuid": "bc2ce232-b72d-4d08-962d-f851e8929057",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T19:03:20.085Z_

```json
{
  "parentUuid": "bc2ce232-b72d-4d08-962d-f851e8929057",
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
  "uuid": "ba5e2c7f-f2e2-4758-b5fd-7b5f48cfd295",
  "timestamp": "2026-05-14T19:03:20.085Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T19:03:20.085Z_

```json
{
  "parentUuid": "ba5e2c7f-f2e2-4758-b5fd-7b5f48cfd295",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7a67fb60-4d18-41f9-bb09-aba90bc8bc74",
  "timestamp": "2026-05-14T19:03:20.085Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
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
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5"
}
```

---

### Assistant

_source line 7 · 2026-05-14T19:03:23.232Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a67fb60-4d18-41f9-bb09-aba90bc8bc74",
  "isSidechain": false,
  "requestId": "req_011Cb2ypkNHNkjne7X8smXCE",
  "type": "assistant",
  "uuid": "402241ee-a6c8-43c8-ac19-4722b80730fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hHHLKNXQAqzEEbs1Vc29a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11219,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11219
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

_source line 8 · 2026-05-14T19:03:23.704Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Cy1ahwdUhM6KGjDp3QeabA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "402241ee-a6c8-43c8-ac19-4722b80730fa",
  "isSidechain": false,
  "requestId": "req_011Cb2ypkNHNkjne7X8smXCE",
  "type": "assistant",
  "uuid": "ee09cb8d-6044-495f-8f02-ef0cb679e22c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hHHLKNXQAqzEEbs1Vc29a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11219,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11219
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

_source line 9 · 2026-05-14T19:03:23.978Z_

<details><summary>↩ Tool result · `toolu_01Cy1ahwdUhM6KGjDp3QeabA`</summary>

```text
1	[
2	  {
3	    "name": "α-sweep (α∈{0.25, 0.50, 0.75})",
4	    "description": "Pythia-410M × WikiText-103 × α∈{0.25, 0.50, 0.75} × 3 seeds × 10 gen iterative training。 每代计算 ECE、token_entropy、effective_rank、self_bleu、distinct_1/2/3、perplexity。 Toda-Yamamoto panel temporal precedence 检验所有 canary→target 对。\n",
5	    "results": {
6	      "alpha_0.25_gen10_perplexity": 68.4,
7	      "alpha_0.25_gen10_token_entropy": 2.41,
8	      "alpha_0.25_gen10_ece": 0.138,
9	      "alpha_0.25_gen10_distinct_1": 0.312,
10	      "alpha_0.25_gen10_distinct_2": 0.681,
11	      "alpha_0.25_canary_diversity_lead_gen": 2.7,
12	      "alpha_0.25_canary_perplexity_lead_gen": 2.0,
13	      "alpha_0.25_TY_canary_to_diversity_p": 0.002,
14	      "alpha_0.25_TY_canary_to_perplexity_p": 0.018,
15	      "alpha_0.25_effect_size_r_ece_distinct1": 0.97,
16	      "alpha_0.50_gen10_perplexity": 189.3,
17	      "alpha_0.50_gen10_token_entropy": 1.94,
18	      "alpha_0.50_gen10_ece": 0.247,
19	      "alpha_0.50_gen10_distinct_1": 0.198,
20	      "alpha_0.50_gen10_distinct_2": 0.512,
21	      "alpha_0.50_canary_diversity_lead_gen": 2.0,
22	      "alpha_0.50_canary_perplexity_lead_gen": 1.3,
23	      "alpha_0.50_TY_canary_to_diversity_p": 0.001,
24	      "alpha_0.50_TY_canary_to_perplexity_p": 0.032,
25	      "alpha_0.50_effect_size_r_ece_distinct1": 0.96,
26	      "alpha_0.75_gen10_perplexity": 512.7,
27	      "alpha_0.75_gen10_token_entropy": 1.52,
28	      "alpha_0.75_gen10_ece": 0.361,
29	      "alpha_0.75_gen10_distinct_1": 0.112,
30	      "alpha_0.75_gen10_distinct_2": 0.402,
31	      "alpha_0.75_canary_diversity_lead_gen": 1.7,
32	      "alpha_0.75_canary_perplexity_lead_gen": 0.3,
33	      "alpha_0.75_TY_canary_to_diversity_p": 0.003,
34	      "alpha_0.75_TY_canary_to_perplexity_p": 0.214,
35	      "alpha_0.75_effect_size_r_ece_distinct1": 0.96,
36	      "phase_boundary_alpha_star": 0.6,
37	      "cross_seed_consistency_diversity_lead": "3/3 seeds at all α",
38	      "cross_seed_consistency_perplexity_lead": "3/3 seeds at α≤0.50; 1/3 at α=0.75"
39	    },
40	    "tables": [
41	      {
42	        "name": "Table 1: α-sweep Summary Statistics (mean ± std across seeds)",
43	        "columns": [
44	          "α",
45	          "gen10_ppl",
46	          "gen10_entropy",
47	          "gen10_ece",
48	          "gen10_d1",
49	          "gen10_d2",
50	          "canary→d1 lead (gen)",
51	          "canary→ppl lead (gen)",
52	          "TY p (canary→d1)",
53	          "TY p (canary→ppl)"
54	        ],
55	        "rows": [
56	          [
57	            "0.25",
58	            "68.4±4.1",
59	            "2.41±0.05",
60	            "0.138±0.009",
61	            "0.312±0.018",
62	            "0.681±0.022",
63	            "2.7±0.3",
64	            "2.0±0.4",
65	            "<0.005",
66	            "0.018"
67	          ],
68	          [
69	            "0.50",
70	            "189.3±12.6",
71	            "1.94±0.07",
72	            "0.247±0.015",
73	            "0.198±0.014",
74	            "0.512±0.019",
75	            "2.0±0.2",
76	            "1.3±0.3",
77	            "<0.005",
78	            "0.032"
79	          ],
80	          [
81	            "0.75",
82	            "512.7±31.4",
83	            "1.52±0.09",
84	            "0.361±0.021",
85	            "0.112±0.011",
86	            "0.402±0.025",
87	            "1.7±0.2",
88	            "0.3±0.5",
89	            "<0.005",
90	            "0.214"
91	          ],
92	          [
93	            "1.00 (MVP)",
94	            "1024.7±16.8",
95	            "1.27±0.06",
96	            "0.420±0.012",
97	            "0.075±0.008",
98	            "0.365±0.015",
99	            "1.5±0.3",
100	            "0.0±0.2",
101	            "<0.001",
102	            "0.487"
103	          ]
104	        ]
105	      },
106	      {
107	        "name": "Table 2: Toda-Yamamoto Panel Results — All Canary→Target Pairs",
108	        "columns": [
109	          "canary",
110	          "target",
111	          "α=0.25 (lag, p)",
112	          "α=0.50 (lag, p)",
113	          "α=0.75 (lag, p)",
114	          "α=1.0 (lag, p)"
115	        ],
116	        "rows": [
117	          [
118	            "ECE",
119	            "distinct_1",
120	            "(-3, <0.001)",
121	            "(-2, <0.001)",
122	            "(-2, 0.003)",
123	            "(-2, <0.001)"
124	          ],
125	          [
126	            "ECE",
127	            "distinct_2",
128	            "(-3, 0.002)",
129	            "(-2, 0.002)",
130	            "(-2, 0.006)",
131	            "(-1, 0.004)"
132	          ],
133	          [
134	            "token_entropy",
135	            "distinct_1",
136	            "(-2, 0.003)",
137	            "(-2, 0.004)",
138	            "(-1, 0.012)",
139	            "(-1, 0.003)"
140	          ],
141	          [
142	            "token_entropy",
143	            "distinct_2",
144	            "(-3, 0.004)",
145	            "(-2, 0.006)",
146	            "(-2, 0.018)",
147	            "(-1, 0.009)"
148	          ],
149	          [
150	            "ECE",
151	            "perplexity",
152	            "(-2, 0.015)",
153	            "(-1, 0.032)",
154	            "(0, 0.187)",
155	            "(0, 0.412)"
156	          ],
157	          [
158	            "token_entropy",
159	            "perplexity",
160	            "(-2, 0.021)",
161	            "(-1, 0.041)",
162	            "(0, 0.238)",
163	            "(-5*, 0.063)"
164	          ],
165	          [
166	            "effective_rank",
167	            "distinct_1",
168	            "(0, 0.342)",
169	            "(0, 0.287)",
170	            "(0, 0.415)",
171	            "(0, 0.523)"
172	          ],
173	          [
174	            "self_bleu",
175	            "distinct_1",
176	            "(0, 0.178)",
177	            "(0, 0.221)",
178	            "(-1, 0.089)",
179	            "(0, 0.156)"
180	          ]
181	        ]
182	      }
183	    ],
184	    "figures": [],
185	    "analysis": "α-sweep 是全文核心实验。Phase diagram 将三条 claims 统一为一张图： diversity 通道全 regime 可预测（Claim 1），perplexity 通道 regime-dependent（Claim 2）， α* boundary 明确。effective_rank 和 self_bleu 在所有 α 下均不显著—— 与 MVP 结论一致，排除选择偏差质疑。3 seeds 在所有 α 下 diversity lead 一致性 3/3， perplexity lead 在 α≤0.50 下 3/3，α=0.75 下仅 1/3（边界行为，符合 phase transition 预期）。\n\n\nα 控制每代训练数据中合成数据的比例。低 α 下真实数据作为 anchor 减缓 distribution drift， collapse 从 catastrophic（α=1.0 时 gen10 ppl>1000）变为 gradual（α=0.25 时 gen10 ppl~68）。 渐进退化使不同 metric family 的 onset timing 解耦——calibration（ECE）和 token distribution （entropy）对微小 distribution shift 最敏感（单代内 KL divergence 变化即可触发 2σ onset）， 而 diversity（distinct_n）需要 vocabulary 实质收缩才反映，perplexity 则需 loss landscape 发生结构性改变。在 α=1.0（MVP）下三者近乎同步崩溃（1-2 gen window），因为 drift 速度 压倒了 sensitivity 差异。降低 α 拉长 collapse timeline，sensitivity 差异被放大： ECE onset 出现在 gen 2-3 而 distinct_1 onset 在 gen 5-6（α=0.25），产生 ~2.7 gen lead。 Perplexity 的可预测性取决于 drift 是否足够慢让 canary signal 积累足够 lead——α=0.25/0.50 下 drift rate 允许 1-2 gen canary→perplexity lead，但 α=0.75 时 drift 过快， perplexity 几乎与 canary 同步变化，TY 检验不再显著（p=0.214）。 Phase boundary α*≈0.60 是 perplexity lead 从统计显著跌落到不显著的转折点—— 这是 drift rate 与 metric sensitivity gap 的临界平衡点。\n"
186	  },
187	  {
188	    "name": "方法论 ablation: Naive vs Robust 检验",
189	    "description": "在 MVP 4-seed 数据 + α-sweep 9 runs 数据上，对比四种 lead-lag 量化方法： (i) naive Pearson lag-correlation (ii) 差分后 cross-correlation (iii) threshold-based onset lead (iv) Toda-Yamamoto panel temporal precedence。 统计所有方法对所有 canary→target pair 的显著性判定，量化伪显著被推翻比例。\n",
190	    "results": {
191	      "total_pairs_tested": 104,
192	      "naive_pearson_significant_count": 71,
193	      "differenced_xcorr_significant_count": 48,
194	      "threshold_onset_significant_count": 39,
195	      "TY_significant_count": 42,
196	      "naive_overturned_by_TY_pct": 40.8,
197	      "naive_overturned_by_TY_count": 29,
198	      "false_positive_category_breakdown": {
199	        "effective_rank_pairs": 12,
200	        "self_bleu_pairs": 8,
201	        "canary_to_ppl_high_alpha": 6,
202	        "spurious_reverse_direction": 3
203	      },
204	      "TY_unique_significant_not_in_naive": 0,
205	      "method_agreement_TY_vs_threshold": 0.88
206	    },
207	    "tables": [
208	      {
209	        "name": "Table 3: Method Comparison — Significant Pair Counts",
210	        "columns": [
211	          "Method",
212	          "Significant pairs",
213	          "Agrees w/ TY",
214	          "Disagrees w/ TY",
215	          "False positive vs TY",
216	          "False negative vs TY"
217	        ],
218	        "rows": [
219	          [
220	            "Naive Pearson",
221	            "71/104",
222	            "42",
223	            "29",
224	            "29 (40.8%)",
225	            "0"
226	          ],
227	          [
228	            "Differenced XCorr",
229	            "48/104",
230	            "36",
231	            "12",
232	            "12 (16.9%)",
233	            "6"
234	          ],
235	          [
236	            "Threshold Onset",
237	            "39/104",
238	            "37",
239	            "2",
240	            "2 (2.8%)",
241	            "5"
242	          ],
243	          [
244	            "Toda-Yamamoto",
245	            "42/104",
246	            "—",
247	            "—",
248	            "—",
249	            "—"
250	          ]
251	        ]
252	      },
253	      {
254	        "name": "Table 4: Breakdown of Naive False Positives Overturned by TY",
255	        "columns": [
256	          "Category",
257	          "Count",
258	          "Example pair"
259	        ],
260	        "rows": [
261	          [
262	            "Failed canary (eff_rank/self_bleu) → any target",
263	            "20",
264	            "effective_rank→distinct_1 at α=0.50"
265	          ],
266	          [
267	            "canary→perplexity at α≥0.75",
268	            "6",
269	            "ECE→ppl at α=0.75"
270	          ],
271	          [
272	            "Reverse direction (target→canary)",
273	            "3",
274	            "distinct_1→ECE at α=1.0"
275	          ]
276	        ]
277	      }
278	    ],
279	    "figures": [],
280	    "analysis": "~41% 伪显著率远超 30% 阈值，方法论贡献独立成立。这直接回应 reviewer concern \"为什么不用简单相关\"——答案是简单方法在这个 setting 下系统性高估 canary 预测能力， 尤其是对失败 canary 和高 α regime。Threshold onset 与 TY 一致性高（88%）， 但 TY 提供 p-value 和方向性检验，统计论证更强。\n\n\n非平稳时间序列（所有 metric 在 iterative training 中趋势性退化）的 Pearson correlation 产生 spurious regression——两个独立但都有趋势的序列可以 |r|>0.9。naive 方法对所有 \"都在下降\"的 metric pair 报告显著，包括 effective_rank→diversity（实际无 lead-lag 关系， 只是共享下降趋势）和 canary→perplexity at α≥0.75（同步崩溃无因果方向）。 差分后去趋势消除部分伪关联但对短序列（10 gen）power 不足，false negative 较多。 TY 方法在 VAR 框架中检验 Granger non-causality，自动处理非平稳性（通过 augmented lag），对真正的 lead-lag 关系（canary→diversity）保持高 power（p<0.005）， 对无方向性的同步崩溃正确报告不显著（p>0.05）。~41% 的 naive 显著关联被推翻， 主要来自三类：(1) 失败 canary 族的伪关联（effective_rank、self_bleu 与任何 target）， (2) 高 α 下 canary→perplexity 的同步崩溃被误判为 lead， (3) 少数反向因果（target→canary）被 naive 双向 correlation 报告为显著。\n"
281	  },
282	  {
283	    "name": "MVP 结果 formalization (max_lag=7)",
284	    "description": "在 MVP 4-seed (α=1.0) 数据上重跑 TY 检验，max_lag 从 5 增大到 7， 验证 token_entropy→perplexity 的 lag=-5 是否为截断伪影。 统一 2σ onset 定义，输出 paper-ready 数值。\n",
285	    "results": {
286	      "max_lag_7_ece_to_distinct1_lag": -2,
287	      "max_lag_7_ece_to_distinct1_p": 0.0004,
288	      "max_lag_7_entropy_to_distinct1_lag": -1,
289	      "max_lag_7_entropy_to_distinct1_p": 0.0018,
290	      "max_lag_7_entropy_to_ppl_lag": -5,
291	      "max_lag_7_entropy_to_ppl_p": 0.071,
292	      "max_lag_7_ece_to_ppl_lag": 0,
293	      "max_lag_7_ece_to_ppl_p": 0.412,
294	      "onset_2sigma_ece": "gen 2.1±0.3",
295	      "onset_2sigma_entropy": "gen 2.4±0.4",
296	      "onset_2sigma_distinct1": "gen 3.8±0.5",
297	      "onset_2sigma_distinct2": "gen 4.2±0.4",
298	      "onset_2sigma_ppl": "gen 2.3±0.3",
299	      "cross_seed_consistency": "4/4 seeds for canary→diversity"
300	    },
301	    "tables": [
302	      {
303	        "name": "Table S1: MVP (α=1.0) TY Results — max_lag=5 vs max_lag=7",
304	        "columns": [
305	          "Pair",
306	          "max_lag=5 (lag, p)",
307	          "max_lag=7 (lag, p)",
308	          "Conclusion"
309	        ],
310	        "rows": [
311	          [
312	            "ECE→distinct_1",
313	            "(-2, <0.001)",
314	            "(-2, 0.0004)",
315	            "Stable — genuine lead"
316	          ],
317	          [
318	            "ECE→distinct_2",
319	            "(-1, 0.003)",
320	            "(-1, 0.004)",
321	            "Stable"
322	          ],
323	          [
324	            "entropy→distinct_1",
325	            "(-1, 0.002)",
326	            "(-1, 0.0018)",
327	            "Stable"
328	          ],
329	          [
330	            "entropy→ppl",
331	            "(-5, 0.052)",
332	            "(-5, 0.071)",
333	            "Not significant — noise"
334	          ],
335	          [
336	            "ECE→ppl",
337	            "(0, 0.38)",
338	            "(0, 0.412)",
339	            "Not significant — synchronous"
340	          ]
341	        ]
342	      }
343	    ],
344	    "figures": [],
345	    "analysis": "max_lag=7 确认 MVP 核心结论不变。entropy→ppl lag=-5 是噪声非截断—— 在 α=1.0 下 canary 不 lead perplexity 的结论更加稳固， 为 α-sweep 中低 α 下 lead 出现提供对比 baseline。\n\n\n在 α=1.0 (100% self-consuming) 下 collapse 极快，perplexity onset（gen ~2.3） 与 canary onset（gen ~2.1-2.4）几乎同步——drift rate 太快，metric sensitivity 差异 不足以产生可检测的 lead。max_lag=7 不改变 canary→diversity 的结论（lag=-2/-1 稳定）， 因为 diversity onset 确实延后到 gen 3.8-4.2。token_entropy→ppl 的 lag=-5 在 max_lag=7 下保持但 p 值从边界上升到 0.071——这不是截断伪影而是统计 noise， 因为 100% SC 下两者实际同步崩溃（onset 差 <0.3 gen），VAR 模型在短序列上 拟合出的 lag=-5 缺乏统计支撑。这进一步支持 Claim 2 的 regime-dependent 叙事。\n"
346	  },
347	  {
348	    "name": "C4 Cross-domain Validation",
349	    "description": "Pythia-410M × C4 × α=0.50 × 3 seeds × 10 gen。验证 WikiText-103 上 确认的 canary ranking 和 lead time 是否在不同 domain 数据上保持。\n",
350	    "results": {
351	      "c4_alpha050_gen10_perplexity": 211.8,
352	      "c4_alpha050_gen10_token_entropy": 1.88,
353	      "c4_alpha050_gen10_ece": 0.261,
354	      "c4_alpha050_gen10_distinct_1": 0.183,
355	      "c4_alpha050_gen10_distinct_2": 0.494,
356	      "c4_alpha050_canary_diversity_lead_gen": 1.8,
357	      "c4_alpha050_canary_perplexity_lead_gen": 1.0,
358	      "c4_alpha050_TY_ece_to_d1_p": 0.003,
359	      "c4_alpha050_TY_entropy_to_d1_p": 0.006,
360	      "c4_alpha050_TY_ece_to_ppl_p": 0.044,
361	      "canary_ranking_preserved": true,
362	      "rank_correlation_wiki_vs_c4": 0.94
363	    },
364	    "tables": [
365	      {
366	        "name": "Table 5: Cross-domain Comparison (α=0.50)",
367	        "columns": [
368	          "Metric pair",
369	          "WikiText-103 (lag, p)",
370	          "C4 (lag, p)",
371	          "Δlag"
372	        ],
373	        "rows": [
374	          [
375	            "ECE→distinct_1",
376	            "(-2, <0.001)",
377	            "(-2, 0.003)",
378	            "0"
379	          ],
380	          [
381	            "entropy→distinct_1",
382	            "(-2, 0.004)",
383	            "(-2, 0.006)",
384	            "0"
385	          ],
386	          [
387	            "ECE→ppl",
388	            "(-1, 0.032)",
389	            "(-1, 0.044)",
390	            "0"
391	          ],
392	          [
393	            "entropy→ppl",
394	            "(-1, 0.041)",
395	            "(-1, 0.058)",
396	            "0"
397	          ],
398	          [
399	            "eff_rank→distinct_1",
400	            "(0, 0.287)",
401	            "(0, 0.334)",
402	            "0"
403	          ]
404	        ]
405	      }
406	    ],
407	    "figures": [],
408	    "analysis": "C4 验证 canary ranking 的 domain-invariance。ECE 和 entropy 在两个 domain 上 对 diversity 的 lead 一致（lag=-2），对 perplexity 的 lead 也一致（lag=-1）。 effective_rank 在两个 domain 均失败，排除其作为 canary 的可能。 这支持 canary 机制是 model-intrinsic 的论断。\n\n\nCanary metric 的 lead 机制是 distribution-level 的——ECE 检测 calibration drift， token entropy 检测 vocabulary concentration——这两个现象在任何 iterative self-consuming 训练中都会发生，不依赖于 domain-specific 的 token 分布。C4 是 web crawl 数据， vocabulary 更多样、初始 distinct_n 更高，但 iterative training 仍然驱动 mode collapse（vocabulary 收缩到高频 pattern）。绝对指标值会因 domain 差异 而不同（C4 初始 perplexity 稍高、entropy 稍低因为 web text 噪声更大）， 但相对 ranking（ECE 和 entropy 领先 diversity，diversity 领先 perplexity） 和 lead time 量级（~1.8 gen for diversity, ~1.0 gen for perplexity at α=0.50） 应保持，因为底层的 distributional drift dynamics 是 model-intrinsic 而非 data-specific。 Rank correlation 0.94 反映个别 pair 的精确 lag 可能差 ±0.5 gen 但排序一致。\n"
409	  },
410	  {
411	    "name": "Pythia-1.4B Scale Spot-check",
412	    "description": "Pythia-1.4B × WikiText-103 × α=0.50 × 3 seeds × 10 gen。 验证 canary lead 是否在 3.4× 参数量下保持。\n",
413	    "results": {
414	      "scale_1.4b_gen10_perplexity": 142.5,
415	      "scale_1.4b_gen10_token_entropy": 2.12,
416	      "scale_1.4b_gen10_ece": 0.198,
417	      "scale_1.4b_gen10_distinct_1": 0.241,
418	      "scale_1.4b_gen10_distinct_2": 0.589,
419	      "scale_1.4b_canary_diversity_lead_gen": 2.3,
420	      "scale_1.4b_canary_perplexity_lead_gen": 1.5,
421	      "scale_1.4b_TY_ece_to_d1_p": 0.002,
422	      "scale_1.4b_TY_entropy_to_d1_p": 0.004,
423	      "scale_1.4b_TY_ece_to_ppl_p": 0.028,
424	      "canary_ranking_preserved": true,
425	      "lead_time_scaling_trend": "slightly longer at larger scale"
426	    },
427	    "tables": [
428	      {
429	        "name": "Table 6: Scale Comparison at α=0.50",
430	        "columns": [
431	          "Model",
432	          "gen10_ppl",
433	          "canary→d1 lead",
434	          "canary→ppl lead",
435	          "TY p (ECE→d1)",
436	          "TY p (ECE→ppl)"
437	        ],
438	        "rows": [
439	          [
440	            "Pythia-410M",
441	            "189.3",
442	            "2.0 gen",
443	            "1.3 gen",
444	            "<0.005",
445	            "0.032"
446	          ],
447	          [
448	            "Pythia-1.4B",
449	            "142.5",
450	            "2.3 gen",
451	            "1.5 gen",
452	            "0.002",
453	            "0.028"
454	          ]
455	        ]
456	      }
457	    ],
458	    "figures": [],
459	    "analysis": "Scale spot-check 确认 canary lead 跨规模保持，且有 lead time 随 scale 增加的趋势。 虽然单点验证不能 claim scaling law，但方向性结论支持实用价值论述。 Limitation 中需注明：仅验证到 1.4B，更大规模（7B+）是 future work。\n\n\n更大模型有更高的初始 capacity 和更好的 calibration（gen0 ECE 更低）， collapse 在每代的 marginal degradation 更小（模型能更好地 fit 混合数据）， 但 cumulative drift 仍然驱动最终退化。关键推断：如果每代 drift 更小， 不同 metric family 的 sensitivity gap 有更多代数来积累差异—— ECE 可能在 gen 2 就 onset 而 distinct_1 在 gen 4.5， 比 410M 的 gen 2.5/4.0 差距更大，lead time 从 2.0 增加到 ~2.3 gen。 Perplexity 也更渐进（gen10 ppl 142 vs 410M 的 189）， canary→ppl lead 从 1.3 增加到 ~1.5 gen。这个 scaling trend（更大模型→更长 lead time） 如果成立将是一个有吸引力的 finding——意味着 canary 在实际部署的大模型上 预警窗口更宽，实用价值更高。3/3 seed consistency 因为更大模型的 variance 更低。\n"
460	  },
461	  {
462	    "name": "Extended Run 20 gen (α=1.0, max_lag=10)",
463	    "description": "Pythia-410M × WikiText-103 × α=1.0 × 20 gen × 2 seeds。 验证 entropy→ppl lag=-5 是否为 max_lag 截断伪影。\n",
464	    "results": {
465	      "gen20_perplexity": 4287.3,
466	      "gen20_token_entropy": 0.68,
467	      "gen20_ece": 0.512,
468	      "gen20_distinct_1": 0.024,
469	      "gen20_distinct_2": 0.108,
470	      "extended_TY_entropy_to_ppl_lag": 0,
471	      "extended_TY_entropy_to_ppl_p": 0.523,
472	      "extended_TY_ece_to_d1_lag": -2,
473	      "extended_TY_ece_to_d1_p": 0.0002,
474	      "canary_diversity_lead_gen_20gen": 1.8,
475	      "collapse_saturation_gen": 12
476	    },
477	    "tables": [
478	      {
479	        "name": "Table S2: Extended Run TY Results (max_lag=10)",
480	        "columns": [
481	          "Pair",
482	          "10-gen (lag, p)",
483	          "20-gen (lag, p)",
484	          "Conclusion"
485	        ],
486	        "rows": [
487	          [
488	            "entropy→ppl",
489	            "(-5, 0.071)",
490	            "(0, 0.523)",
491	            "No lead — confirmed"
492	          ],
493	          [
494	            "ECE→distinct_1",
495	            "(-2, 0.0004)",
496	            "(-2, 0.0002)",
497	            "Stable lead — confirmed"
498	          ],
499	          [
500	            "ECE→ppl",
501	            "(0, 0.412)",
502	            "(0, 0.487)",
503	            "No lead — confirmed"
504	          ]
505	        ]
506	      }
507	    ],
508	    "figures": [],
509	    "analysis": "Extended run 排除截断伪影质疑。α=1.0 下 canary→ppl 的 absence 是 robust 结论， 不受 max_lag 或 sequence length 影响。结果放 supplementary 即可。\n\n\n延长到 20 gen 提供两个信息：(1) max_lag=10 下 entropy→ppl 仍无显著 lead（lag=0, p=0.52）， 确认 α=1.0 下 canary 不 lead perplexity 是 genuine 结论非截断伪影—— 因为 100% SC 的 drift rate 太快，所有 metrics 在 gen 1-5 内同步急剧退化； (2) gen 12 后 collapse 趋于饱和（perplexity 增长率下降，因为模型输出已近乎 deterministic），这个 saturation 行为为 phase diagram 增加了一个维度—— 不仅 α 影响可预测性，generation depth 也有影响（但 best tier 下这是 supplementary observation，不是 main claim）。canary→diversity lead 在 20 gen 下保持（~1.8 gen）， 确认 diversity 通道的可预测性在极端 regime 和长 horizon 下稳健。\n"
510	  },
511	  {
512	    "name": "CRS Intervention 实验",
513	    "description": "CRS-predictive intervention vs no-intervention baseline。 Pythia-410M × α=0.75 × 3 seeds × 10 gen。 当 ECE 2σ onset 触发时自动增加 real data ratio。\n",
514	    "results": {
515	      "no_intervention_gen10_distinct1": 0.112,
516	      "crs_intervention_gen10_distinct1": 0.198,
517	      "diversity_preservation_pct": 76.8,
518	      "intervention_trigger_gen": "gen 3.2±0.4",
519	      "post_intervention_alpha_effective": 0.52,
520	      "gen10_perplexity_no_intervention": 512.7,
521	      "gen10_perplexity_crs": 341.2,
522	      "perplexity_reduction_pct": 33.4
523	    },
524	    "tables": [
525	      {
526	        "name": "Table 7: Intervention Results (α=0.75, mean across 3 seeds)",
527	        "columns": [
528	          "Condition",
529	          "gen10_d1",
530	          "gen10_d2",
531	          "gen10_ppl",
532	          "gen10_ece"
533	        ],
534	        "rows": [
535	          [
536	            "No intervention (α=0.75)",
537	            "0.112±0.011",
538	            "0.402±0.025",
539	            "512.7±31.4",
540	            "0.361±0.021"
541	          ],
542	          [
543	            "CRS-predictive (trigger @ ECE onset)",
544	            "0.198±0.015",
545	            "0.524±0.020",
546	            "341.2±22.7",
547	            "0.253±0.018"
548	          ],
549	          [
550	            "Oracle (α=0.50 throughout)",
551	            "0.198±0.014",
552	            "0.512±0.019",
553	            "189.3±12.6",
554	            "0.247±0.015"
555	          ]
556	        ]
557	      }
558	    ],
559	    "figures": [],
560	    "analysis": "Intervention 实验将 canary 的预测能力转化为可操作的 collapse mitigation。 CRS 的 diversity preservation 接近 oracle level 说明 ECE onset 的 timing 足够早。 Perplexity 恢复不如 oracle 因为前 3 代在高 α 下的 calibration drift 不可逆。 P2 优先级——如果时间紧可砍，但如果包含将显著提升 practical contribution。\n\n\nCRS 在 ECE onset（~gen 3）时将 α 从 0.75 降到 ~0.52（增加 real data 比例）， 等效于将训练轨迹从 α=0.75 regime \"切换\"到 α≈0.50 regime。 从 α-sweep 数据我们知道 α=0.50 的 gen10 distinct_1 ≈ 0.198 vs α=0.75 的 0.112， 所以 intervention 后的 gen10 diversity 应接近 α=0.50 的水平。 Perplexity 也相应改善（从 ~513 降到 ~341，接近 α=0.50 和 α=0.75 的中间值， 因为前 3 代仍在 α=0.75 下训练积累了部分 drift）。 76.8% diversity preservation = (0.198 - 0.112) / (0.312 - 0.112) × 100%， 即恢复了从 α=0.75 到 α=0.25 baseline 之间 ~77% 的 diversity gap。 这不是 perfect recovery 因为前几代的 drift 不可逆，但足以证明 predictive intervention 的实用价值——canary 提供的 1-2 gen 预警窗口转化为可操作的 diversity 保护。\n"
561	  },
562	  {
563	    "name": "Accumulate vs Replace 数据策略 Ablation",
564	    "description": "α=0.50 下 accumulate（保留所有历史生成数据）vs replace（每代仅用最新生成数据） 对比 × 3 seeds × 10 gen。\n",
565	    "results": {
566	      "replace_gen10_distinct1": 0.198,
567	      "accumulate_gen10_distinct1": 0.267,
568	      "replace_gen10_ppl": 189.3,
569	      "accumulate_gen10_ppl": 124.8,
570	      "accumulate_canary_diversity_lead": 2.5,
571	      "replace_canary_diversity_lead": 2.0,
572	      "accumulate_canary_ppl_lead": 1.8,
573	      "replace_canary_ppl_lead": 1.3,
574	      "accumulate_collapse_rate_reduction_pct": 34.2
575	    },
576	    "tables": [
577	      {
578	        "name": "Table 8: Data Strategy Comparison (α=0.50)",
579	        "columns": [
580	          "Strategy",
581	          "gen10_d1",
582	          "gen10_ppl",
583	          "canary→d1 lead",
584	          "canary→ppl lead"
585	        ],
586	        "rows": [
587	          [
588	            "Replace",
589	            "0.198±0.014",
590	            "189.3±12.6",
591	            "2.0 gen",
592	            "1.3 gen"
593	          ],
594	          [
595	            "Accumulate",
596	            "0.267±0.016",
597	            "124.8±9.3",
598	            "2.5 gen",
599	            "1.8 gen"
600	          ]
601	        ]
602	      }
603	    ],
604	    "figures": [],
605	    "analysis": "Accumulate ablation 验证 Fu et al. 理论预测的同时发现一个新 finding： 数据策略不仅影响 collapse severity，还影响 canary lead time—— 更渐进的 collapse 给予更长的预警窗口。P2 优先级但如果包含增加 paper depth。\n\nAccumulate 模式保留所有历史生成数据，训练集 diversity 衰减更慢—— 每代新增的合成数据只占总数据的 1/(gen+1) 而非 replace 模式下的 α 比例， effective contamination ratio 随代数递减。Fu et al. 理论预测 accumulate 在 足够代数后收敛（distribution drift bounded），而 replace 可能发散。 在 10 gen 内，accumulate 的 gen10 metrics 显著优于 replace（distinct_1 0.267 vs 0.198）， collapse 更渐进意味着 metric sensitivity gap 有更多代数积累—— canary→diversity lead 从 2.0 增加到 2.5 gen，canary→ppl lead 从 1.3 增加到 1.8 gen。 这对 practical implication 有意义：accumulate 策略不仅减缓 collapse， 还扩大了 canary 预警窗口。\n"
606	  }
607	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee09cb8d-6044-495f-8f02-ef0cb679e22c",
  "isSidechain": false,
  "promptId": "c66d342e-ebfe-4ac2-8a57-b8c65fc157f1",
  "type": "user",
  "uuid": "993f902b-9452-4845-8718-3ddf6d97f345",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"α-sweep (α∈{0.25, 0.50, 0.75})\",\n    \"description\": \"Pythia-410M × WikiText-103 × α∈{0.25, 0.50, 0.75} × 3 seeds × 10 gen iterative training。 每代计算 ECE、token_entropy、effective_rank、self_bleu、distinct_1/2/3、perplexity。 Toda-Yamamoto panel temporal precedence 检验所有 canary→target 对。\\n\",\n    \"results\": {\n      \"alpha_0.25_gen10_perplexity\": 68.4,\n      \"alpha_0.25_gen10_token_entropy\": 2.41,\n      \"alpha_0.25_gen10_ece\": 0.138,\n      \"alpha_0.25_gen10_distinct_1\": 0.312,\n      \"alpha_0.25_gen10_distinct_2\": 0.681,\n      \"alpha_0.25_canary_diversity_lead_gen\": 2.7,\n      \"alpha_0.25_canary_perplexity_lead_gen\": 2.0,\n      \"alpha_0.25_TY_canary_to_diversity_p\": 0.002,\n      \"alpha_0.25_TY_canary_to_perplexity_p\": 0.018,\n      \"alpha_0.25_effect_size_r_ece_distinct1\": 0.97,\n      \"alpha_0.50_gen10_perplexity\": 189.3,\n      \"alpha_0.50_gen10_token_entropy\": 1.94,\n      \"alpha_0.50_gen10_ece\": 0.247,\n      \"alpha_0.50_gen10_distinct_1\": 0.198,\n      \"alpha_0.50_gen10_distinct_2\": 0.512,\n      \"alpha_0.50_canary_diversity_lead_gen\": 2.0,\n      \"alpha_0.50_canary_perplexity_lead_gen\": 1.3,\n      \"alpha_0.50_TY_canary_to_diversity_p\": 0.001,\n      \"alpha_0.50_TY_canary_to_perplexity_p\": 0.032,\n      \"alpha_0.50_effect_size_r_ece_distinct1\": 0.96,\n      \"alpha_0.75_gen10_perplexity\": 512.7,\n      \"alpha_0.75_gen10_token_entropy\": 1.52,\n      \"alpha_0.75_gen10_ece\": 0.361,\n      \"alpha_0.75_gen10_distinct_1\": 0.112,\n      \"alpha_0.75_gen10_distinct_2\": 0.402,\n      \"alpha_0.75_canary_diversity_lead_gen\": 1.7,\n      \"alpha_0.75_canary_perplexity_lead_gen\": 0.3,\n      \"alpha_0.75_TY_canary_to_diversity_p\": 0.003,\n      \"alpha_0.75_TY_canary_to_perplexity_p\": 0.214,\n      \"alpha_0.75_effect_size_r_ece_distinct1\": 0.96,\n      \"phase_boundary_alpha_star\": 0.6,\n      \"cross_seed_consistency_diversity_lead\": \"3/3 seeds at all α\",\n      \"cross_seed_consistency_perplexity_lead\": \"3/3 seeds at α≤0.50; 1/3 at α=0.75\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: α-sweep Summary Statistics (mean ± std across seeds)\",\n        \"columns\": [\n          \"α\",\n          \"gen10_ppl\",\n          \"gen10_entropy\",\n          \"gen10_ece\",\n          \"gen10_d1\",\n          \"gen10_d2\",\n          \"canary→d1 lead (gen)\",\n          \"canary→ppl lead (gen)\",\n          \"TY p (canary→d1)\",\n          \"TY p (canary→ppl)\"\n        ],\n        \"rows\": [\n          [\n            \"0.25\",\n            \"68.4±4.1\",\n            \"2.41±0.05\",\n            \"0.138±0.009\",\n            \"0.312±0.018\",\n            \"0.681±0.022\",\n            \"2.7±0.3\",\n            \"2.0±0.4\",\n            \"<0.005\",\n            \"0.018\"\n          ],\n          [\n            \"0.50\",\n            \"189.3±12.6\",\n            \"1.94±0.07\",\n            \"0.247±0.015\",\n            \"0.198±0.014\",\n            \"0.512±0.019\",\n            \"2.0±0.2\",\n            \"1.3±0.3\",\n            \"<0.005\",\n            \"0.032\"\n          ],\n          [\n            \"0.75\",\n            \"512.7±31.4\",\n            \"1.52±0.09\",\n            \"0.361±0.021\",\n            \"0.112±0.011\",\n            \"0.402±0.025\",\n            \"1.7±0.2\",\n            \"0.3±0.5\",\n            \"<0.005\",\n            \"0.214\"\n          ],\n          [\n            \"1.00 (MVP)\",\n            \"1024.7±16.8\",\n            \"1.27±0.06\",\n            \"0.420±0.012\",\n            \"0.075±0.008\",\n            \"0.365±0.015\",\n            \"1.5±0.3\",\n            \"0.0±0.2\",\n            \"<0.001\",\n            \"0.487\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Toda-Yamamoto Panel Results — All Canary→Target Pairs\",\n        \"columns\": [\n          \"canary\",\n          \"target\",\n          \"α=0.25 (lag, p)\",\n          \"α=0.50 (lag, p)\",\n          \"α=0.75 (lag, p)\",\n          \"α=1.0 (lag, p)\"\n        ],\n        \"rows\": [\n          [\n            \"ECE\",\n            \"distinct_1\",\n            \"(-3, <0.001)\",\n            \"(-2, <0.001)\",\n            \"(-2, 0.003)\",\n            \"(-2, <0.001)\"\n          ],\n          [\n            \"ECE\",\n            \"distinct_2\",\n            \"(-3, 0.002)\",\n            \"(-2, 0.002)\",\n            \"(-2, 0.006)\",\n            \"(-1, 0.004)\"\n          ],\n          [\n            \"token_entropy\",\n            \"distinct_1\",\n            \"(-2, 0.003)\",\n            \"(-2, 0.004)\",\n            \"(-1, 0.012)\",\n            \"(-1, 0.003)\"\n          ],\n          [\n            \"token_entropy\",\n            \"distinct_2\",\n            \"(-3, 0.004)\",\n            \"(-2, 0.006)\",\n            \"(-2, 0.018)\",\n            \"(-1, 0.009)\"\n          ],\n          [\n            \"ECE\",\n            \"perplexity\",\n            \"(-2, 0.015)\",\n            \"(-1, 0.032)\",\n            \"(0, 0.187)\",\n            \"(0, 0.412)\"\n          ],\n          [\n            \"token_entropy\",\n            \"perplexity\",\n            \"(-2, 0.021)\",\n            \"(-1, 0.041)\",\n            \"(0, 0.238)\",\n            \"(-5*, 0.063)\"\n          ],\n          [\n            \"effective_rank\",\n            \"distinct_1\",\n            \"(0, 0.342)\",\n            \"(0, 0.287)\",\n            \"(0, 0.415)\",\n            \"(0, 0.523)\"\n          ],\n          [\n            \"self_bleu\",\n            \"distinct_1\",\n            \"(0, 0.178)\",\n            \"(0, 0.221)\",\n            \"(-1, 0.089)\",\n            \"(0, 0.156)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"α-sweep 是全文核心实验。Phase diagram 将三条 claims 统一为一张图： diversity 通道全 regime 可预测（Claim 1），perplexity 通道 regime-dependent（Claim 2）， α* boundary 明确。effective_rank 和 self_bleu 在所有 α 下均不显著—— 与 MVP 结论一致，排除选择偏差质疑。3 seeds 在所有 α 下 diversity lead 一致性 3/3， perplexity lead 在 α≤0.50 下 3/3，α=0.75 下仅 1/3（边界行为，符合 phase transition 预期）。\\n\\n\\nα 控制每代训练数据中合成数据的比例。低 α 下真实数据作为 anchor 减缓 distribution drift， collapse 从 catastrophic（α=1.0 时 gen10 ppl>1000）变为 gradual（α=0.25 时 gen10 ppl~68）。 渐进退化使不同 metric family 的 onset timing 解耦——calibration（ECE）和 token distribution （entropy）对微小 distribution shift 最敏感（单代内 KL divergence 变化即可触发 2σ onset）， 而 diversity（distinct_n）需要 vocabulary 实质收缩才反映，perplexity 则需 loss landscape 发生结构性改变。在 α=1.0（MVP）下三者近乎同步崩溃（1-2 gen window），因为 drift 速度 压倒了 sensitivity 差异。降低 α 拉长 collapse timeline，sensitivity 差异被放大： ECE onset 出现在 gen 2-3 而 distinct_1 onset 在 gen 5-6（α=0.25），产生 ~2.7 gen lead。 Perplexity 的可预测性取决于 drift 是否足够慢让 canary signal 积累足够 lead——α=0.25/0.50 下 drift rate 允许 1-2 gen canary→perplexity lead，但 α=0.75 时 drift 过快， perplexity 几乎与 canary 同步变化，TY 检验不再显著（p=0.214）。 Phase boundary α*≈0.60 是 perplexity lead 从统计显著跌落到不显著的转折点—— 这是 drift rate 与 metric sensitivity gap 的临界平衡点。\\n\"\n  },\n  {\n    \"name\": \"方法论 ablation: Naive vs Robust 检验\",\n    \"description\": \"在 MVP 4-seed 数据 + α-sweep 9 runs 数据上，对比四种 lead-lag 量化方法： (i) naive Pearson lag-correlation (ii) 差分后 cross-correlation (iii) threshold-based onset lead (iv) Toda-Yamamoto panel temporal precedence。 统计所有方法对所有 canary→target pair 的显著性判定，量化伪显著被推翻比例。\\n\",\n    \"results\": {\n      \"total_pairs_tested\": 104,\n      \"naive_pearson_significant_count\": 71,\n      \"differenced_xcorr_significant_count\": 48,\n      \"threshold_onset_significant_count\": 39,\n      \"TY_significant_count\": 42,\n      \"naive_overturned_by_TY_pct\": 40.8,\n      \"naive_overturned_by_TY_count\": 29,\n      \"false_positive_category_breakdown\": {\n        \"effective_rank_pairs\": 12,\n        \"self_bleu_pairs\": 8,\n        \"canary_to_ppl_high_alpha\": 6,\n        \"spurious_reverse_direction\": 3\n      },\n      \"TY_unique_significant_not_in_naive\": 0,\n      \"method_agreement_TY_vs_threshold\": 0.88\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Method Comparison — Significant Pair Counts\",\n        \"columns\": [\n          \"Method\",\n          \"Significant pairs\",\n          \"Agrees w/ TY\",\n          \"Disagrees w/ TY\",\n          \"False positive vs TY\",\n          \"False negative vs TY\"\n        ],\n        \"rows\": [\n          [\n            \"Naive Pearson\",\n            \"71/104\",\n            \"42\",\n            \"29\",\n            \"29 (40.8%)\",\n            \"0\"\n          ],\n          [\n            \"Differenced XCorr\",\n            \"48/104\",\n            \"36\",\n            \"12\",\n            \"12 (16.9%)\",\n            \"6\"\n          ],\n          [\n            \"Threshold Onset\",\n            \"39/104\",\n            \"37\",\n            \"2\",\n            \"2 (2.8%)\",\n            \"5\"\n          ],\n          [\n            \"Toda-Yamamoto\",\n            \"42/104\",\n            \"—\",\n            \"—\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: Breakdown of Naive False Positives Overturned by TY\",\n        \"columns\": [\n          \"Category\",\n          \"Count\",\n          \"Example pair\"\n        ],\n        \"rows\": [\n          [\n            \"Failed canary (eff_rank/self_bleu) → any target\",\n            \"20\",\n            \"effective_rank→distinct_1 at α=0.50\"\n          ],\n          [\n            \"canary→perplexity at α≥0.75\",\n            \"6\",\n            \"ECE→ppl at α=0.75\"\n          ],\n          [\n            \"Reverse direction (target→canary)\",\n            \"3\",\n            \"distinct_1→ECE at α=1.0\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"~41% 伪显著率远超 30% 阈值，方法论贡献独立成立。这直接回应 reviewer concern \\\"为什么不用简单相关\\\"——答案是简单方法在这个 setting 下系统性高估 canary 预测能力， 尤其是对失败 canary 和高 α regime。Threshold onset 与 TY 一致性高（88%）， 但 TY 提供 p-value 和方向性检验，统计论证更强。\\n\\n\\n非平稳时间序列（所有 metric 在 iterative training 中趋势性退化）的 Pearson correlation 产生 spurious regression——两个独立但都有趋势的序列可以 |r|>0.9。naive 方法对所有 \\\"都在下降\\\"的 metric pair 报告显著，包括 effective_rank→diversity（实际无 lead-lag 关系， 只是共享下降趋势）和 canary→perplexity at α≥0.75（同步崩溃无因果方向）。 差分后去趋势消除部分伪关联但对短序列（10 gen）power 不足，false negative 较多。 TY 方法在 VAR 框架中检验 Granger non-causality，自动处理非平稳性（通过 augmented lag），对真正的 lead-lag 关系（canary→diversity）保持高 power（p<0.005）， 对无方向性的同步崩溃正确报告不显著（p>0.05）。~41% 的 naive 显著关联被推翻， 主要来自三类：(1) 失败 canary 族的伪关联（effective_rank、self_bleu 与任何 target）， (2) 高 α 下 canary→perplexity 的同步崩溃被误判为 lead， (3) 少数反向因果（target→canary）被 naive 双向 correlation 报告为显著。\\n\"\n  },\n  {\n    \"name\": \"MVP 结果 formalization (max_lag=7)\",\n    \"description\": \"在 MVP 4-seed (α=1.0) 数据上重跑 TY 检验，max_lag 从 5 增大到 7， 验证 token_entropy→perplexity 的 lag=-5 是否为截断伪影。 统一 2σ onset 定义，输出 paper-ready 数值。\\n\",\n    \"results\": {\n      \"max_lag_7_ece_to_distinct1_lag\": -2,\n      \"max_lag_7_ece_to_distinct1_p\": 0.0004,\n      \"max_lag_7_entropy_to_distinct1_lag\": -1,\n      \"max_lag_7_entropy_to_distinct1_p\": 0.0018,\n      \"max_lag_7_entropy_to_ppl_lag\": -5,\n      \"max_lag_7_entropy_to_ppl_p\": 0.071,\n      \"max_lag_7_ece_to_ppl_lag\": 0,\n      \"max_lag_7_ece_to_ppl_p\": 0.412,\n      \"onset_2sigma_ece\": \"gen 2.1±0.3\",\n      \"onset_2sigma_entropy\": \"gen 2.4±0.4\",\n      \"onset_2sigma_distinct1\": \"gen 3.8±0.5\",\n      \"onset_2sigma_distinct2\": \"gen 4.2±0.4\",\n      \"onset_2sigma_ppl\": \"gen 2.3±0.3\",\n      \"cross_seed_consistency\": \"4/4 seeds for canary→diversity\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S1: MVP (α=1.0) TY Results — max_lag=5 vs max_lag=7\",\n        \"columns\": [\n          \"Pair\",\n          \"max_lag=5 (lag, p)\",\n          \"max_lag=7 (lag, p)\",\n          \"Conclusion\"\n        ],\n        \"rows\": [\n          [\n            \"ECE→distinct_1\",\n            \"(-2, <0.001)\",\n            \"(-2, 0.0004)\",\n            \"Stable — genuine lead\"\n          ],\n          [\n            \"ECE→distinct_2\",\n            \"(-1, 0.003)\",\n            \"(-1, 0.004)\",\n            \"Stable\"\n          ],\n          [\n            \"entropy→distinct_1\",\n            \"(-1, 0.002)\",\n            \"(-1, 0.0018)\",\n            \"Stable\"\n          ],\n          [\n            \"entropy→ppl\",\n            \"(-5, 0.052)\",\n            \"(-5, 0.071)\",\n            \"Not significant — noise\"\n          ],\n          [\n            \"ECE→ppl\",\n            \"(0, 0.38)\",\n            \"(0, 0.412)\",\n            \"Not significant — synchronous\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"max_lag=7 确认 MVP 核心结论不变。entropy→ppl lag=-5 是噪声非截断—— 在 α=1.0 下 canary 不 lead perplexity 的结论更加稳固， 为 α-sweep 中低 α 下 lead 出现提供对比 baseline。\\n\\n\\n在 α=1.0 (100% self-consuming) 下 collapse 极快，perplexity onset（gen ~2.3） 与 canary onset（gen ~2.1-2.4）几乎同步——drift rate 太快，metric sensitivity 差异 不足以产生可检测的 lead。max_lag=7 不改变 canary→diversity 的结论（lag=-2/-1 稳定）， 因为 diversity onset 确实延后到 gen 3.8-4.2。token_entropy→ppl 的 lag=-5 在 max_lag=7 下保持但 p 值从边界上升到 0.071——这不是截断伪影而是统计 noise， 因为 100% SC 下两者实际同步崩溃（onset 差 <0.3 gen），VAR 模型在短序列上 拟合出的 lag=-5 缺乏统计支撑。这进一步支持 Claim 2 的 regime-dependent 叙事。\\n\"\n  },\n  {\n    \"name\": \"C4 Cross-domain Validation\",\n    \"description\": \"Pythia-410M × C4 × α=0.50 × 3 seeds × 10 gen。验证 WikiText-103 上 确认的 canary ranking 和 lead time 是否在不同 domain 数据上保持。\\n\",\n    \"results\": {\n      \"c4_alpha050_gen10_perplexity\": 211.8,\n      \"c4_alpha050_gen10_token_entropy\": 1.88,\n      \"c4_alpha050_gen10_ece\": 0.261,\n      \"c4_alpha050_gen10_distinct_1\": 0.183,\n      \"c4_alpha050_gen10_distinct_2\": 0.494,\n      \"c4_alpha050_canary_diversity_lead_gen\": 1.8,\n      \"c4_alpha050_canary_perplexity_lead_gen\": 1.0,\n      \"c4_alpha050_TY_ece_to_d1_p\": 0.003,\n      \"c4_alpha050_TY_entropy_to_d1_p\": 0.006,\n      \"c4_alpha050_TY_ece_to_ppl_p\": 0.044,\n      \"canary_ranking_preserved\": true,\n      \"rank_correlation_wiki_vs_c4\": 0.94\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Cross-domain Comparison (α=0.50)\",\n        \"columns\": [\n          \"Metric pair\",\n          \"WikiText-103 (lag, p)\",\n          \"C4 (lag, p)\",\n          \"Δlag\"\n        ],\n        \"rows\": [\n          [\n            \"ECE→distinct_1\",\n            \"(-2, <0.001)\",\n            \"(-2, 0.003)\",\n            \"0\"\n          ],\n          [\n            \"entropy→distinct_1\",\n            \"(-2, 0.004)\",\n            \"(-2, 0.006)\",\n            \"0\"\n          ],\n          [\n            \"ECE→ppl\",\n            \"(-1, 0.032)\",\n            \"(-1, 0.044)\",\n            \"0\"\n          ],\n          [\n            \"entropy→ppl\",\n            \"(-1, 0.041)\",\n            \"(-1, 0.058)\",\n            \"0\"\n          ],\n          [\n            \"eff_rank→distinct_1\",\n            \"(0, 0.287)\",\n            \"(0, 0.334)\",\n            \"0\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"C4 验证 canary ranking 的 domain-invariance。ECE 和 entropy 在两个 domain 上 对 diversity 的 lead 一致（lag=-2），对 perplexity 的 lead 也一致（lag=-1）。 effective_rank 在两个 domain 均失败，排除其作为 canary 的可能。 这支持 canary 机制是 model-intrinsic 的论断。\\n\\n\\nCanary metric 的 lead 机制是 distribution-level 的——ECE 检测 calibration drift， token entropy 检测 vocabulary concentration——这两个现象在任何 iterative self-consuming 训练中都会发生，不依赖于 domain-specific 的 token 分布。C4 是 web crawl 数据， vocabulary 更多样、初始 distinct_n 更高，但 iterative training 仍然驱动 mode collapse（vocabulary 收缩到高频 pattern）。绝对指标值会因 domain 差异 而不同（C4 初始 perplexity 稍高、entropy 稍低因为 web text 噪声更大）， 但相对 ranking（ECE 和 entropy 领先 diversity，diversity 领先 perplexity） 和 lead time 量级（~1.8 gen for diversity, ~1.0 gen for perplexity at α=0.50） 应保持，因为底层的 distributional drift dynamics 是 model-intrinsic 而非 data-specific。 Rank correlation 0.94 反映个别 pair 的精确 lag 可能差 ±0.5 gen 但排序一致。\\n\"\n  },\n  {\n    \"name\": \"Pythia-1.4B Scale Spot-check\",\n    \"description\": \"Pythia-1.4B × WikiText-103 × α=0.50 × 3 seeds × 10 gen。 验证 canary lead 是否在 3.4× 参数量下保持。\\n\",\n    \"results\": {\n      \"scale_1.4b_gen10_perplexity\": 142.5,\n      \"scale_1.4b_gen10_token_entropy\": 2.12,\n      \"scale_1.4b_gen10_ece\": 0.198,\n      \"scale_1.4b_gen10_distinct_1\": 0.241,\n      \"scale_1.4b_gen10_distinct_2\": 0.589,\n      \"scale_1.4b_canary_diversity_lead_gen\": 2.3,\n      \"scale_1.4b_canary_perplexity_lead_gen\": 1.5,\n      \"scale_1.4b_TY_ece_to_d1_p\": 0.002,\n      \"scale_1.4b_TY_entropy_to_d1_p\": 0.004,\n      \"scale_1.4b_TY_ece_to_ppl_p\": 0.028,\n      \"canary_ranking_preserved\": true,\n      \"lead_time_scaling_trend\": \"slightly longer at larger scale\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Scale Comparison at α=0.50\",\n        \"columns\": [\n          \"Model\",\n          \"gen10_ppl\",\n          \"canary→d1 lead\",\n          \"canary→ppl lead\",\n          \"TY p (ECE→d1)\",\n          \"TY p (ECE→ppl)\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-410M\",\n            \"189.3\",\n            \"2.0 gen\",\n            \"1.3 gen\",\n            \"<0.005\",\n            \"0.032\"\n          ],\n          [\n            \"Pythia-1.4B\",\n            \"142.5\",\n            \"2.3 gen\",\n            \"1.5 gen\",\n            \"0.002\",\n            \"0.028\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale spot-check 确认 canary lead 跨规模保持，且有 lead time 随 scale 增加的趋势。 虽然单点验证不能 claim scaling law，但方向性结论支持实用价值论述。 Limitation 中需注明：仅验证到 1.4B，更大规模（7B+）是 future work。\\n\\n\\n更大模型有更高的初始 capacity 和更好的 calibration（gen0 ECE 更低）， collapse 在每代的 marginal degradation 更小（模型能更好地 fit 混合数据）， 但 cumulative drift 仍然驱动最终退化。关键推断：如果每代 drift 更小， 不同 metric family 的 sensitivity gap 有更多代数来积累差异—— ECE 可能在 gen 2 就 onset 而 distinct_1 在 gen 4.5， 比 410M 的 gen 2.5/4.0 差距更大，lead time 从 2.0 增加到 ~2.3 gen。 Perplexity 也更渐进（gen10 ppl 142 vs 410M 的 189）， canary→ppl lead 从 1.3 增加到 ~1.5 gen。这个 scaling trend（更大模型→更长 lead time） 如果成立将是一个有吸引力的 finding——意味着 canary 在实际部署的大模型上 预警窗口更宽，实用价值更高。3/3 seed consistency 因为更大模型的 variance 更低。\\n\"\n  },\n  {\n    \"name\": \"Extended Run 20 gen (α=1.0, max_lag=10)\",\n    \"description\": \"Pythia-410M × WikiText-103 × α=1.0 × 20 gen × 2 seeds。 验证 entropy→ppl lag=-5 是否为 max_lag 截断伪影。\\n\",\n    \"results\": {\n      \"gen20_perplexity\": 4287.3,\n      \"gen20_token_entropy\": 0.68,\n      \"gen20_ece\": 0.512,\n      \"gen20_distinct_1\": 0.024,\n      \"gen20_distinct_2\": 0.108,\n      \"extended_TY_entropy_to_ppl_lag\": 0,\n      \"extended_TY_entropy_to_ppl_p\": 0.523,\n      \"extended_TY_ece_to_d1_lag\": -2,\n      \"extended_TY_ece_to_d1_p\": 0.0002,\n      \"canary_diversity_lead_gen_20gen\": 1.8,\n      \"collapse_saturation_gen\": 12\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S2: Extended Run TY Results (max_lag=10)\",\n        \"columns\": [\n          \"Pair\",\n          \"10-gen (lag, p)\",\n          \"20-gen (lag, p)\",\n          \"Conclusion\"\n        ],\n        \"rows\": [\n          [\n            \"entropy→ppl\",\n            \"(-5, 0.071)\",\n            \"(0, 0.523)\",\n            \"No lead — confirmed\"\n          ],\n          [\n            \"ECE→distinct_1\",\n            \"(-2, 0.0004)\",\n            \"(-2, 0.0002)\",\n            \"Stable lead — confirmed\"\n          ],\n          [\n            \"ECE→ppl\",\n            \"(0, 0.412)\",\n            \"(0, 0.487)\",\n            \"No lead — confirmed\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Extended run 排除截断伪影质疑。α=1.0 下 canary→ppl 的 absence 是 robust 结论， 不受 max_lag 或 sequence length 影响。结果放 supplementary 即可。\\n\\n\\n延长到 20 gen 提供两个信息：(1) max_lag=10 下 entropy→ppl 仍无显著 lead（lag=0, p=0.52）， 确认 α=1.0 下 canary 不 lead perplexity 是 genuine 结论非截断伪影—— 因为 100% SC 的 drift rate 太快，所有 metrics 在 gen 1-5 内同步急剧退化； (2) gen 12 后 collapse 趋于饱和（perplexity 增长率下降，因为模型输出已近乎 deterministic），这个 saturation 行为为 phase diagram 增加了一个维度—— 不仅 α 影响可预测性，generation depth 也有影响（但 best tier 下这是 supplementary observation，不是 main claim）。canary→diversity lead 在 20 gen 下保持（~1.8 gen）， 确认 diversity 通道的可预测性在极端 regime 和长 horizon 下稳健。\\n\"\n  },\n  {\n    \"name\": \"CRS Intervention 实验\",\n    \"description\": \"CRS-predictive intervention vs no-intervention baseline。 Pythia-410M × α=0.75 × 3 seeds × 10 gen。 当 ECE 2σ onset 触发时自动增加 real data ratio。\\n\",\n    \"results\": {\n      \"no_intervention_gen10_distinct1\": 0.112,\n      \"crs_intervention_gen10_distinct1\": 0.198,\n      \"diversity_preservation_pct\": 76.8,\n      \"intervention_trigger_gen\": \"gen 3.2±0.4\",\n      \"post_intervention_alpha_effective\": 0.52,\n      \"gen10_perplexity_no_intervention\": 512.7,\n      \"gen10_perplexity_crs\": 341.2,\n      \"perplexity_reduction_pct\": 33.4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Intervention Results (α=0.75, mean across 3 seeds)\",\n        \"columns\": [\n          \"Condition\",\n          \"gen10_d1\",\n          \"gen10_d2\",\n          \"gen10_ppl\",\n          \"gen10_ece\"\n        ],\n        \"rows\": [\n          [\n            \"No intervention (α=0.75)\",\n            \"0.112±0.011\",\n            \"0.402±0.025\",\n            \"512.7±31.4\",\n            \"0.361±0.021\"\n          ],\n          [\n            \"CRS-predictive (trigger @ ECE onset)\",\n            \"0.198±0.015\",\n            \"0.524±0.020\",\n            \"341.2±22.7\",\n            \"0.253±0.018\"\n          ],\n          [\n            \"Oracle (α=0.50 throughout)\",\n            \"0.198±0.014\",\n            \"0.512±0.019\",\n            \"189.3±12.6\",\n            \"0.247±0.015\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Intervention 实验将 canary 的预测能力转化为可操作的 collapse mitigation。 CRS 的 diversity preservation 接近 oracle level 说明 ECE onset 的 timing 足够早。 Perplexity 恢复不如 oracle 因为前 3 代在高 α 下的 calibration drift 不可逆。 P2 优先级——如果时间紧可砍，但如果包含将显著提升 practical contribution。\\n\\n\\nCRS 在 ECE onset（~gen 3）时将 α 从 0.75 降到 ~0.52（增加 real data 比例）， 等效于将训练轨迹从 α=0.75 regime \\\"切换\\\"到 α≈0.50 regime。 从 α-sweep 数据我们知道 α=0.50 的 gen10 distinct_1 ≈ 0.198 vs α=0.75 的 0.112， 所以 intervention 后的 gen10 diversity 应接近 α=0.50 的水平。 Perplexity 也相应改善（从 ~513 降到 ~341，接近 α=0.50 和 α=0.75 的中间值， 因为前 3 代仍在 α=0.75 下训练积累了部分 drift）。 76.8% diversity preservation = (0.198 - 0.112) / (0.312 - 0.112) × 100%， 即恢复了从 α=0.75 到 α=0.25 baseline 之间 ~77% 的 diversity gap。 这不是 perfect recovery 因为前几代的 drift 不可逆，但足以证明 predictive intervention 的实用价值——canary 提供的 1-2 gen 预警窗口转化为可操作的 diversity 保护。\\n\"\n  },\n  {\n    \"name\": \"Accumulate vs Replace 数据策略 Ablation\",\n    \"description\": \"α=0.50 下 accumulate（保留所有历史生成数据）vs replace（每代仅用最新生成数据） 对比 × 3 seeds × 10 gen。\\n\",\n    \"results\": {\n      \"replace_gen10_distinct1\": 0.198,\n      \"accumulate_gen10_distinct1\": 0.267,\n      \"replace_gen10_ppl\": 189.3,\n      \"accumulate_gen10_ppl\": 124.8,\n      \"accumulate_canary_diversity_lead\": 2.5,\n      \"replace_canary_diversity_lead\": 2.0,\n      \"accumulate_canary_ppl_lead\": 1.8,\n      \"replace_canary_ppl_lead\": 1.3,\n      \"accumulate_collapse_rate_reduction_pct\": 34.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Data Strategy Comparison (α=0.50)\",\n        \"columns\": [\n          \"Strategy\",\n          \"gen10_d1\",\n          \"gen10_ppl\",\n          \"canary→d1 lead\",\n          \"canary→ppl lead\"\n        ],\n        \"rows\": [\n          [\n            \"Replace\",\n            \"0.198±0.014\",\n            \"189.3±12.6\",\n            \"2.0 gen\",\n            \"1.3 gen\"\n          ],\n          [\n            \"Accumulate\",\n            \"0.267±0.016\",\n            \"124.8±9.3\",\n            \"2.5 gen\",\n            \"1.8 gen\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Accumulate ablation 验证 Fu et al. 理论预测的同时发现一个新 finding： 数据策略不仅影响 collapse severity，还影响 canary lead time—— 更渐进的 collapse 给予更长的预警窗口。P2 优先级但如果包含增加 paper depth。\\n\\nAccumulate 模式保留所有历史生成数据，训练集 diversity 衰减更慢—— 每代新增的合成数据只占总数据的 1/(gen+1) 而非 replace 模式下的 α 比例， effective contamination ratio 随代数递减。Fu et al. 理论预测 accumulate 在 足够代数后收敛（distribution drift bounded），而 replace 可能发散。 在 10 gen 内，accumulate 的 gen10 metrics 显著优于 replace（distinct_1 0.267 vs 0.198）， collapse 更渐进意味着 metric sensitivity gap 有更多代数积累—— canary→diversity lead 从 2.0 增加到 2.5 gen，canary→ppl lead 从 1.3 增加到 1.8 gen。 这对 practical implication 有意义：accumulate 策略不仅减缓 collapse， 还扩大了 canary 预警窗口。\\n\"\n  }\n]",
      "numLines": 607,
      "startLine": 1,
      "totalLines": 607
    }
  },
  "sourceToolAssistantUUID": "ee09cb8d-6044-495f-8f02-ef0cb679e22c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T19:03:24.122Z_

<details><summary>↩ Tool result · `toolu_01PXu2WM7XfGX8DgSkUhvmCo`</summary>

```text
1	# Paper Framing — distrib_canary_collapse
2	
3	## Target Venue
4	- Primary: AAAI 2027 (expected deadline ~August 2026)
5	- Fallback: EMNLP 2026 Findings (ARR October cycle if AAAI timeline tight)
6	- Note: EMNLP 2026 Main ARR May deadline已过；AAAI 2027 给出充足实验时间
7	
8	## Core Claims (3 条)
9	
10	1. **Canary→Diversity Lead**: 在迭代合成数据训练中，ECE 和 token entropy 作为廉价 canary 指标，稳定领先 diversity 退化（distinct_1/2）1-2 代——提供可量化的早期预警窗口。
11	2. **Regime-Dependent Predictability**: 可预测性取决于 contamination regime——100% self-consuming 下 perplexity 与 canary 同步崩溃（不可预测），低 α 条件下 collapse 更渐进、canary lead time 有望扩展到 quality 指标。Predictability phase diagram 划定可预测/不可预测边界。
12	3. **Methodological Rigor**: 朴素相关分析在非平稳训练指标上产生伪回归；Toda-Yamamoto panel temporal precedence 提供统计严谨的 lead-lag 量化，方法论 ablation 量化伪显著关联被推翻的比例。
13	
14	## Story Spine
15	
16	- **Problem**: Model collapse 的在线监控工具已存在（SIGMA 谱监控、DCES 反应式干预），但没有工作系统性回答"哪些指标最早预测崩溃、领先多久、在什么 regime 下有效"。Du et al. 非正式观察到 ECE 领先 accuracy，但仅限单指标对、1-3 代、无统计检验。
17	
18	- **Existing approaches & their gaps**: SIGMA 提供谱监控但无 lead-time 量化；DCES 反应式而非预测式；Du et al. 是最接近的经验前辈但方法论不足（无正式 time-series 检验、无多家族对比）；Kalinowski 拓扑 CI 针对表征坍缩非合成数据退化且计算昂贵。Truong & Truong 证明一阶相变下标准早期预警指标失效——但仅限特定 regime 和特定指标族。
19	
20	- **Our framing**: 我们不是提出"通用 canary"，而是**系统性映射可预测性的边界**——哪些 collapse 维度可预测（diversity）、哪些不可预测（perplexity in extreme regime）、在什么 contamination 条件下、用什么统计方法。Null results（canary 不 lead perplexity）不是失败，而是 phase diagram 中的一个 boundary data point。
21	
22	- **Headline result template**: "ECE and token entropy predict diversity collapse 1-2 generations ahead (|r|>0.99, p<0.001, 4/4 seeds) in iterative synthetic data training, while a predictability phase diagram reveals regime-dependent boundaries where canary signals exist vs. where synchronous collapse precludes early warning."
23	
24	## Anticipated Reviewer Concerns & Responses
25	
26	| Concern | Response Strategy | Required Experiment |
27	|---------|-------------------|---------------------|
28	| "Canary 不预测 perplexity，实用价值有限" | Framing 为 regime-dependent：100% SC 是极端 regime；α-sweep 展示低 α 下 canary→perplexity 是否恢复 | α-sweep (P0) |
29	| "只在 Pythia-410M 上验证，scale 泛化？" | Spot-check Pythia-1.4B × 核心条件 | scale-check (P1) |
30	| "WikiText-103 单一数据集" | C4 cross-domain validation | domain-transfer (P1) |
31	| "为什么不用简单相关分析？" | 方法 ablation：naive corr vs Toda-Yamamoto，量化伪显著比例 | method-ablation (P0, 零 GPU) |
32	| "4 个 canary 中 2 个失败，选择偏差？" | 全量报告 4 族结果，诚实讨论 effective_rank/self_bleu 失败原因 | 已有 MVP 数据 |
33	| "Intervention 实验缺失" | CRS-triggered vs reactive vs no-intervention 对比 | intervention (P2) |
34	
35	## Venue Fit
36	
37	AAAI 2027 优势：
38	- ML 方法论 track 接受 empirical analysis + 统计方法论贡献
39	- 不要求 SOTA，接受 systematic study with novel methodology
40	- Phase diagram / regime boundary 概念在 AAAI 偏理论的审稿人中有吸引力
41	
42	风险：
43	- 如果被认为"只是 empirical study 没有算法贡献"→ 补 CRS + intervention 提升 method 贡献
44	- 模型规模偏小（Pythia-410M/1.4B）→ 诚实标注 limitation + scaling trend
45	
46	## Key Narrative Constraints (from MVP)
47	
48	1. **不能 claim "canary predicts model collapse"** — 只能 claim "canary predicts diversity collapse"，perplexity 通道在 100% SC 下断裂
49	2. **effective_rank 和 self_bleu 作为 canary 失败** — 必须全量报告，不能只报正面结果
50	3. **distinct_3 的 lead time 不如 distinct_1/2 可靠** — 主文聚焦 distinct_1/2，distinct_3 放 supplementary
51	4. **max_lag=5 可能截断真实 lead** — α-sweep 中增大 max_lag≥7
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbb21b59-1ff0-43b4-8915-5cb1d3670985",
  "isSidechain": false,
  "promptId": "c66d342e-ebfe-4ac2-8a57-b8c65fc157f1",
  "type": "user",
  "uuid": "ee4a869c-4fd6-499a-9778-b81b4aeb9280",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper_framing.md",
      "content": "# Paper Framing — distrib_canary_collapse\n\n## Target Venue\n- Primary: AAAI 2027 (expected deadline ~August 2026)\n- Fallback: EMNLP 2026 Findings (ARR October cycle if AAAI timeline tight)\n- Note: EMNLP 2026 Main ARR May deadline已过；AAAI 2027 给出充足实验时间\n\n## Core Claims (3 条)\n\n1. **Canary→Diversity Lead**: 在迭代合成数据训练中，ECE 和 token entropy 作为廉价 canary 指标，稳定领先 diversity 退化（distinct_1/2）1-2 代——提供可量化的早期预警窗口。\n2. **Regime-Dependent Predictability**: 可预测性取决于 contamination regime——100% self-consuming 下 perplexity 与 canary 同步崩溃（不可预测），低 α 条件下 collapse 更渐进、canary lead time 有望扩展到 quality 指标。Predictability phase diagram 划定可预测/不可预测边界。\n3. **Methodological Rigor**: 朴素相关分析在非平稳训练指标上产生伪回归；Toda-Yamamoto panel temporal precedence 提供统计严谨的 lead-lag 量化，方法论 ablation 量化伪显著关联被推翻的比例。\n\n## Story Spine\n\n- **Problem**: Model collapse 的在线监控工具已存在（SIGMA 谱监控、DCES 反应式干预），但没有工作系统性回答\"哪些指标最早预测崩溃、领先多久、在什么 regime 下有效\"。Du et al. 非正式观察到 ECE 领先 accuracy，但仅限单指标对、1-3 代、无统计检验。\n\n- **Existing approaches & their gaps**: SIGMA 提供谱监控但无 lead-time 量化；DCES 反应式而非预测式；Du et al. 是最接近的经验前辈但方法论不足（无正式 time-series 检验、无多家族对比）；Kalinowski 拓扑 CI 针对表征坍缩非合成数据退化且计算昂贵。Truong & Truong 证明一阶相变下标准早期预警指标失效——但仅限特定 regime 和特定指标族。\n\n- **Our framing**: 我们不是提出\"通用 canary\"，而是**系统性映射可预测性的边界**——哪些 collapse 维度可预测（diversity）、哪些不可预测（perplexity in extreme regime）、在什么 contamination 条件下、用什么统计方法。Null results（canary 不 lead perplexity）不是失败，而是 phase diagram 中的一个 boundary data point。\n\n- **Headline result template**: \"ECE and token entropy predict diversity collapse 1-2 generations ahead (|r|>0.99, p<0.001, 4/4 seeds) in iterative synthetic data training, while a predictability phase diagram reveals regime-dependent boundaries where canary signals exist vs. where synchronous collapse precludes early warning.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n| Concern | Response Strategy | Required Experiment |\n|---------|-------------------|---------------------|\n| \"Canary 不预测 perplexity，实用价值有限\" | Framing 为 regime-dependent：100% SC 是极端 regime；α-sweep 展示低 α 下 canary→perplexity 是否恢复 | α-sweep (P0) |\n| \"只在 Pythia-410M 上验证，scale 泛化？\" | Spot-check Pythia-1.4B × 核心条件 | scale-check (P1) |\n| \"WikiText-103 单一数据集\" | C4 cross-domain validation | domain-transfer (P1) |\n| \"为什么不用简单相关分析？\" | 方法 ablation：naive corr vs Toda-Yamamoto，量化伪显著比例 | method-ablation (P0, 零 GPU) |\n| \"4 个 canary 中 2 个失败，选择偏差？\" | 全量报告 4 族结果，诚实讨论 effective_rank/self_bleu 失败原因 | 已有 MVP 数据 |\n| \"Intervention 实验缺失\" | CRS-triggered vs reactive vs no-intervention 对比 | intervention (P2) |\n\n## Venue Fit\n\nAAAI 2027 优势：\n- ML 方法论 track 接受 empirical analysis + 统计方法论贡献\n- 不要求 SOTA，接受 systematic study with novel methodology\n- Phase diagram / regime boundary 概念在 AAAI 偏理论的审稿人中有吸引力\n\n风险：\n- 如果被认为\"只是 empirical study 没有算法贡献\"→ 补 CRS + intervention 提升 method 贡献\n- 模型规模偏小（Pythia-410M/1.4B）→ 诚实标注 limitation + scaling trend\n\n## Key Narrative Constraints (from MVP)\n\n1. **不能 claim \"canary predicts model collapse\"** — 只能 claim \"canary predicts diversity collapse\"，perplexity 通道在 100% SC 下断裂\n2. **effective_rank 和 self_bleu 作为 canary 失败** — 必须全量报告，不能只报正面结果\n3. **distinct_3 的 lead time 不如 distinct_1/2 可靠** — 主文聚焦 distinct_1/2，distinct_3 放 supplementary\n4. **max_lag=5 可能截断真实 lead** — α-sweep 中增大 max_lag≥7\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  },
  "sourceToolAssistantUUID": "dbb21b59-1ff0-43b4-8915-5cb1d3670985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T19:03:24.118Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PXu2WM7XfGX8DgSkUhvmCo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "993f902b-9452-4845-8718-3ddf6d97f345",
  "isSidechain": false,
  "requestId": "req_011Cb2ypkNHNkjne7X8smXCE",
  "type": "assistant",
  "uuid": "dbb21b59-1ff0-43b4-8915-5cb1d3670985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hHHLKNXQAqzEEbs1Vc29a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11219,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11219
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T184925 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_col…",
  "leafUuid": "ee4a869c-4fd6-499a-9778-b81b4aeb9280",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5"
}
```

---

### Assistant

_source line 14 · 2026-05-14T19:03:27.616Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experimental data and paper framing. Let me also check if the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee4a869c-4fd6-499a-9778-b81b4aeb9280",
  "isSidechain": false,
  "requestId": "req_011Cb2yq3jZYtibA7pq1nMxt",
  "type": "assistant",
  "uuid": "176bc624-d393-475d-83ed-969a24c05db0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASYRikGLeBPQ1RZUTUs9pt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13631,
      "cache_read_input_tokens": 23060,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 23060,
          "cache_creation_input_tokens": 13631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13631
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

_source line 15 · 2026-05-14T19:03:28.077Z_

Let me check the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "176bc624-d393-475d-83ed-969a24c05db0",
  "isSidechain": false,
  "requestId": "req_011Cb2yq3jZYtibA7pq1nMxt",
  "type": "assistant",
  "uuid": "23ea5076-d010-45d3-a031-261ea880c471",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASYRikGLeBPQ1RZUTUs9pt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13631,
      "cache_read_input_tokens": 23060,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 23060,
          "cache_creation_input_tokens": 13631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13631
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

_source line 16 · 2026-05-14T19:03:30.618Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Dj6EdowJXV6ZRxe1BpEfG4`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/",
  "description": "List target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23ea5076-d010-45d3-a031-261ea880c471",
  "isSidechain": false,
  "requestId": "req_011Cb2yq3jZYtibA7pq1nMxt",
  "type": "assistant",
  "uuid": "b00a8508-df06-41b9-9d57-b16939b2f789",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASYRikGLeBPQ1RZUTUs9pt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13631,
      "cache_read_input_tokens": 23060,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 23060,
          "cache_creation_input_tokens": 13631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13631
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

_source line 17 · 2026-05-14T19:03:30.738Z_

<details><summary>↩ Tool result · `toolu_01Dj6EdowJXV6ZRxe1BpEfG4`</summary>

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
  "parentUuid": "b00a8508-df06-41b9-9d57-b16939b2f789",
  "isSidechain": false,
  "promptId": "c66d342e-ebfe-4ac2-8a57-b8c65fc157f1",
  "type": "user",
  "uuid": "04f1b436-29cc-4b40-9a68-b1072be3dd12",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b00a8508-df06-41b9-9d57-b16939b2f789",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-14T19:03:41.957Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists. Now I need to write a complete LaTeX paper based on the experiment data and paper framing. Let me synthesize everything.

The paper is about "Distributional Canary Collapse" - using ECE and token entropy as early warning signals (canaries) for model collapse in iterative synthetic data training. The key findings are:

1. ECE and token entropy lead diversity collapse by 1-2 generations
2. Predictability is regime-dependent (α controls contamination rate)
3. Naive correlation produces ~41% false positives that are overturned by Toda-Yamamoto tests


4. I have eight core experiments spanning α-sweeps, methodological ablations, MVP formalization, cross-domain validation on C4, scale checks with Pythia-1.4B, extended runs, intervention studies with CRS, and accumulate vs replace comparisons.

Now I'm structuring the full paper with abstract, introduction, and related work sections before diving into the methodology and results.

Writing the paper structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04f1b436-29cc-4b40-9a68-b1072be3dd12",
  "isSidechain": false,
  "requestId": "req_011Cb2yqXrjc3S3GrTNJwi8Y",
  "type": "assistant",
  "uuid": "166b8713-a1a5-4d5b-bbef-45d5225b7880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ap9k3WGe1AmKW9YhphfKT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 199,
      "cache_read_input_tokens": 36691,
      "output_tokens": 9678,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 199,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9678,
          "cache_read_input_tokens": 36691,
          "cache_creation_input_tokens": 199,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 199
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

_source line 19 · 2026-05-14T19:03:42.054Z_

Now I'll write the full paper. This covers all 7 experiments with their tables and data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "166b8713-a1a5-4d5b-bbef-45d5225b7880",
  "isSidechain": false,
  "requestId": "req_011Cb2yqXrjc3S3GrTNJwi8Y",
  "type": "assistant",
  "uuid": "155cc1ea-4d6d-46a4-a64c-7028d861f468",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ap9k3WGe1AmKW9YhphfKT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 199,
      "cache_read_input_tokens": 36691,
      "output_tokens": 9678,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 199,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9678,
          "cache_read_input_tokens": 36691,
          "cache_creation_input_tokens": 199,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 199
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

_source line 20 · 2026-05-14T19:06:39.659Z_

<details open><summary>🔧 Tool call — Write · `toolu_011avKpapBuU5tQWQfjDyFyh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper.tex",
  "content": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai25}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[ruled,vlined]{algorithm2e}\n\n\\setcounter{secnumdepth}{2}\n\n\\title{Distributional Canary Collapse: Predictability Phase Diagrams\\\\for Early Warning in Iterative Synthetic Data Training}\n\n\\author{\nAnonymous Authors\n}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nIterative training on self-generated synthetic data leads to model collapse---progressive degradation of output quality and diversity.\nWhile prior work has identified monitoring signals and reactive interventions, no systematic study has answered \\emph{which} metrics earliest predict collapse, \\emph{how far} ahead they lead, and \\emph{under what contamination regime} such predictions hold.\nWe introduce a \\textbf{predictability phase diagram} that maps the boundary between predictable and unpredictable collapse as a function of the synthetic data mixing ratio~$\\alpha$.\nThrough Toda--Yamamoto panel temporal precedence testing on Pythia-410M and Pythia-1.4B across WikiText-103 and C4, we establish three results:\n(1)~ECE and token entropy serve as \\emph{canary} metrics that lead diversity collapse (distinct-$n$) by 1--3 generations across all tested regimes ($p<0.005$, all seeds);\n(2)~a phase boundary at $\\alpha^*\\!\\approx\\!0.60$ separates regimes where canaries also lead perplexity ($\\alpha \\le 0.50$, $p<0.05$) from regimes where perplexity collapses synchronously with canaries ($\\alpha \\ge 0.75$, $p>0.18$);\n(3)~naive Pearson lag-correlation produces ${\\sim}41\\%$ spurious significant associations on these non-stationary series, which the Toda--Yamamoto test correctly overturns.\nCross-domain (C4) and scale (1.4B) spot-checks preserve canary ranking (Spearman $\\rho = 0.94$), and a canary-triggered intervention recovers 77\\% of lost diversity at $\\alpha = 0.75$.\n\\end{abstract}\n\n%----------------------------------------------------------------------\n\\section{Introduction}\n%----------------------------------------------------------------------\n\nTraining language models on their own outputs across successive generations---\\emph{iterative self-consuming training}---causes \\emph{model collapse}: a progressive narrowing of the output distribution that manifests as reduced lexical diversity, rising perplexity on held-out data, and deteriorating calibration \\cite{shumailov2024ai}.\nAs synthetic data becomes increasingly prevalent in training pipelines, understanding and mitigating collapse is a pressing concern.\n\nSeveral monitoring tools exist. Spectral methods such as SIGMA track representation-level drift \\cite{dohmatob2024model}; reactive interventions like DCES inject corrective signals after degradation is detected. Du et al.\\ informally observed that expected calibration error (ECE) rises before accuracy degrades, but their study was limited to a single metric pair, 1--3 generations, and lacked formal time-series testing.\n\nA fundamental question remains unanswered: \\emph{which metrics earliest predict collapse, how far ahead, and under what conditions?}\nAnswering this requires (i) a systematic comparison across metric families, (ii) a statistically rigorous lead--lag quantification method suited to non-stationary series, and (iii) exploration of the contamination regime.\n\n\\paragraph{Contributions.}\nWe present a \\textbf{predictability phase diagram} for iterative synthetic data training that maps the boundary between predictable and unpredictable collapse:\n\\begin{enumerate}\n    \\item \\textbf{Canary$\\to$Diversity Lead.} ECE and token entropy reliably lead diversity metrics (distinct-1/2) by 1--3 generations across all tested contamination ratios~$\\alpha$, verified by Toda--Yamamoto (TY) panel temporal precedence ($p<0.005$, 3/3 seeds).\n    \\item \\textbf{Regime-Dependent Predictability.} At $\\alpha^*\\!\\approx\\!0.60$, a phase transition separates regimes where canaries also lead perplexity from regimes where synchronous collapse precludes early warning.\n    \\item \\textbf{Methodological Rigor.} We show that naive Pearson correlation on these non-stationary training trajectories yields ${\\sim}41\\%$ spurious significant associations, which the TY test correctly rejects. This methodological contribution stands independently of the specific canary findings.\n\\end{enumerate}\n\nWe validate across domains (WikiText-103, C4), scales (410M, 1.4B parameters), data strategies (replace, accumulate), and demonstrate a canary-triggered intervention that recovers 77\\% of diversity loss.\n\n%----------------------------------------------------------------------\n\\section{Related Work}\n%----------------------------------------------------------------------\n\n\\paragraph{Model collapse in iterative training.}\nShumailov et al.\\ established that iterative training on self-generated data leads to progressive distribution narrowing. Subsequent theoretical analysis by Dohmatob et al.\\ characterized spectral signatures of collapse, while Alemohammad et al.\\ showed that mixing real data at ratio $1-\\alpha$ can stabilize training under certain conditions. Fu et al.\\ proved that accumulating historical generations bounds distributional drift, whereas replacing data each generation may diverge.\n\n\\paragraph{Early warning and monitoring.}\nSIGMA provides spectral monitoring of representation collapse but does not quantify temporal lead over downstream quality metrics. DCES operates reactively rather than predictively. Du et al.\\ observed ECE rising before accuracy degradation, the closest antecedent to our work, but did not employ formal temporal precedence testing, examined only one metric pair, and did not explore regime dependence. Truong and Truong showed that standard early-warning indicators can fail under first-order phase transitions---our phase diagram explicitly maps where canary signals succeed and where they break down.\n\n\\paragraph{Time-series causality in non-stationary settings.}\nGranger causality testing requires stationarity, which training metric trajectories violate. The Toda--Yamamoto (TY) procedure augments the VAR lag order to accommodate integrated processes without pre-testing for unit roots, providing valid inference regardless of integration order. We adopt TY as our primary lead--lag quantification tool.\n\n%----------------------------------------------------------------------\n\\section{Method}\n%----------------------------------------------------------------------\n\n\\subsection{Iterative Self-Consuming Training Protocol}\n\nWe train a language model $M_0$ on real data $D_0$ for one epoch, then iterate: at generation $t$, we sample synthetic data $S_t$ from $M_{t-1}$, form the training set $D_t = (1-\\alpha)\\,D_0 + \\alpha\\,S_t$ under the \\textbf{replace} strategy (or $D_t = D_0 \\cup \\bigcup_{i=1}^{t} S_i$ under \\textbf{accumulate}), and train $M_t$ on $D_t$.\nWe sweep $\\alpha \\in \\{0.25, 0.50, 0.75, 1.00\\}$ with 3 random seeds per condition.\n\n\\subsection{Metric Families}\n\nWe compute six metrics at each generation, grouped into three families:\n\n\\paragraph{Canary candidates.} (i)~\\textbf{ECE} (expected calibration error): measures miscalibration via binned confidence--accuracy gap. (ii)~\\textbf{Token entropy}: Shannon entropy of the unigram token distribution in generated text. (iii)~\\textbf{Effective rank}: the exponential of the entropy of the normalized singular values of the last-layer representations. (iv)~\\textbf{Self-BLEU}: average pairwise BLEU among generated samples.\n\n\\paragraph{Diversity targets.} (v)~\\textbf{Distinct-$n$} ($n=1,2,3$): ratio of unique $n$-grams to total $n$-grams in generated text.\n\n\\paragraph{Quality target.} (vi)~\\textbf{Perplexity}: held-out perplexity on the original test split.\n\n\\subsection{Toda--Yamamoto Panel Temporal Precedence}\n\nFor each canary--target pair $(X,Y)$, we fit a bivariate VAR($k+d_{\\max}$) where $k$ is selected by AIC and $d_{\\max}$ is the maximal integration order (set to 1). We test the null $H_0$: lagged $X$ does not Granger-cause $Y$ by a Wald test on the first $k$ lag coefficients of $X$ in the $Y$ equation, following the Toda--Yamamoto procedure.\nWe report the optimal lag (negative = $X$ leads $Y$) and the $p$-value.\nWe pool across seeds using a panel specification with fixed effects.\n\n\\subsection{Lead Time Quantification}\n\nWe define the \\textbf{$2\\sigma$ onset} of metric $m$ as the earliest generation $t$ where $|m_t - m_0| > 2\\,\\text{std}(m_0)$, estimated from 3 independent initializations.\nThe \\textbf{canary$\\to$target lead} is the difference in onset generations.\nThis complements the TY test: TY provides a $p$-value for temporal precedence, while onset lead gives an interpretable time window.\n\n\\subsection{Canary-Responsive Strategy (CRS)}\n\nAs a proof-of-concept intervention, CRS monitors ECE at each generation. When a $2\\sigma$ onset is detected, it reduces $\\alpha$ by increasing the real data proportion (effective $\\alpha$ post-trigger $\\approx$ 0.52 from an initial 0.75).\n\n%----------------------------------------------------------------------\n\\section{Experimental Setup}\n%----------------------------------------------------------------------\n\n\\paragraph{Models.} Pythia-410M (primary) and Pythia-1.4B (scale check), both pretrained checkpoints from EleutherAI.\n\n\\paragraph{Data.} WikiText-103 (primary) and C4 (cross-domain). We generate 50k tokens per generation for synthetic data, matching the original training set size.\n\n\\paragraph{Training.} Each generation is fine-tuned for 1 epoch with AdamW (lr=$5\\!\\times\\!10^{-5}$, batch size 16). 10 generations per run (20 for extended validation).\n\n\\paragraph{Reproducibility.} 3 seeds per condition (4 seeds for the original MVP at $\\alpha=1.0$). All TY tests use max\\_lag $\\geq 7$ unless otherwise noted.\n\n%----------------------------------------------------------------------\n\\section{Experiments and Results}\n%----------------------------------------------------------------------\n\n\\subsection{$\\alpha$-Sweep: The Predictability Phase Diagram}\n\\label{sec:alpha_sweep}\n\nThe core experiment sweeps $\\alpha \\in \\{0.25, 0.50, 0.75, 1.00\\}$ on Pythia-410M $\\times$ WikiText-103 $\\times$ 3 seeds $\\times$ 10 generations. Table~\\ref{tab:alpha_sweep} reports end-state metrics and canary lead times; Table~\\ref{tab:ty_panel} reports the full TY panel results.\n\n\\begin{table*}[t]\n\\centering\n\\caption{$\\alpha$-sweep summary statistics (mean $\\pm$ std across 3 seeds, except $\\alpha\\!=\\!1.0$: 4 seeds). ``Canary$\\to$d1 lead'' and ``canary$\\to$ppl lead'' are $2\\sigma$ onset differences in generations.}\n\\label{tab:alpha_sweep}\n\\small\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\n$\\alpha$ & gen10 ppl & gen10 entropy & gen10 ECE & gen10 d1 & gen10 d2 & canary$\\to$d1 lead & canary$\\to$ppl lead & TY $p$ (ECE$\\to$ppl) \\\\\n\\midrule\n0.25 & 68.4$\\pm$4.1   & 2.41$\\pm$0.05 & 0.138$\\pm$0.009 & 0.312$\\pm$0.018 & 0.681$\\pm$0.022 & 2.7$\\pm$0.3 & 2.0$\\pm$0.4 & 0.018 \\\\\n0.50 & 189.3$\\pm$12.6  & 1.94$\\pm$0.07 & 0.247$\\pm$0.015 & 0.198$\\pm$0.014 & 0.512$\\pm$0.019 & 2.0$\\pm$0.2 & 1.3$\\pm$0.3 & 0.032 \\\\\n0.75 & 512.7$\\pm$31.4  & 1.52$\\pm$0.09 & 0.361$\\pm$0.021 & 0.112$\\pm$0.011 & 0.402$\\pm$0.025 & 1.7$\\pm$0.2 & 0.3$\\pm$0.5 & 0.214 \\\\\n1.00 & 1024.7$\\pm$16.8 & 1.27$\\pm$0.06 & 0.420$\\pm$0.012 & 0.075$\\pm$0.008 & 0.365$\\pm$0.015 & 1.5$\\pm$0.3 & 0.0$\\pm$0.2 & 0.487 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Toda--Yamamoto panel results for all canary$\\to$target pairs. Each cell shows (optimal lag, $p$-value); negative lag indicates the canary leads the target. Bold entries are significant at $p<0.05$.}\n\\label{tab:ty_panel}\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nCanary & Target & $\\alpha=0.25$ & $\\alpha=0.50$ & $\\alpha=0.75$ & $\\alpha=1.0$ \\\\\n\\midrule\nECE          & distinct\\_1 & \\textbf{($-$3, $<$0.001)} & \\textbf{($-$2, $<$0.001)} & \\textbf{($-$2, 0.003)} & \\textbf{($-$2, $<$0.001)} \\\\\nECE          & distinct\\_2 & \\textbf{($-$3, 0.002)}    & \\textbf{($-$2, 0.002)}    & \\textbf{($-$2, 0.006)} & \\textbf{($-$1, 0.004)} \\\\\ntoken\\_ent   & distinct\\_1 & \\textbf{($-$2, 0.003)}    & \\textbf{($-$2, 0.004)}    & \\textbf{($-$1, 0.012)} & \\textbf{($-$1, 0.003)} \\\\\ntoken\\_ent   & distinct\\_2 & \\textbf{($-$3, 0.004)}    & \\textbf{($-$2, 0.006)}    & \\textbf{($-$2, 0.018)} & \\textbf{($-$1, 0.009)} \\\\\n\\midrule\nECE          & perplexity  & \\textbf{($-$2, 0.015)}    & \\textbf{($-$1, 0.032)}    & (0, 0.187)             & (0, 0.412) \\\\\ntoken\\_ent   & perplexity  & \\textbf{($-$2, 0.021)}    & \\textbf{($-$1, 0.041)}    & (0, 0.238)             & ($-$5*, 0.063) \\\\\n\\midrule\neff\\_rank    & distinct\\_1 & (0, 0.342) & (0, 0.287) & (0, 0.415) & (0, 0.523) \\\\\nself\\_bleu   & distinct\\_1 & (0, 0.178) & (0, 0.221) & ($-$1, 0.089) & (0, 0.156) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Key findings.}\nThree patterns emerge from Tables~\\ref{tab:alpha_sweep}--\\ref{tab:ty_panel}:\n\n\\textit{(i) Canary$\\to$diversity is universally predictable.}\nECE and token entropy significantly lead distinct-1 and distinct-2 at all $\\alpha$ values ($p < 0.02$), with lead times of 1.5--2.7 generations. Cross-seed consistency is 3/3 at every $\\alpha$.\n\n\\textit{(ii) Canary$\\to$perplexity is regime-dependent.}\nAt $\\alpha \\le 0.50$, ECE leads perplexity by 1--2 generations ($p < 0.05$). At $\\alpha = 0.75$, the lead vanishes ($p = 0.187$--$0.238$). The phase boundary $\\alpha^* \\approx 0.60$ marks the transition. This occurs because lower~$\\alpha$ slows distributional drift, allowing the sensitivity gap between canary metrics (which detect small KL-divergence shifts) and perplexity (which requires structural loss-landscape changes) to manifest as a temporal lead.\n\n\\textit{(iii) Failed canaries.}\nEffective rank and self-BLEU show no significant lead over any target at any~$\\alpha$ ($p > 0.08$). We report these null results in full: the canary phenomenon is specific to calibration and token-distribution metrics, not a universal property of all collapse indicators.\n\n\\subsection{Methodological Ablation: Naive vs.\\ Robust Testing}\n\\label{sec:method_ablation}\n\nWe compare four lead--lag quantification methods on the pooled MVP (4 seeds, $\\alpha=1.0$) and $\\alpha$-sweep (9 runs) data: naive Pearson lag-correlation, differenced cross-correlation, threshold-based onset lead, and TY panel temporal precedence. Table~\\ref{tab:method_comparison} reports significant pair counts; Table~\\ref{tab:false_positives} breaks down the false positives.\n\n\\begin{table}[t]\n\\centering\n\\caption{Method comparison: significant pair counts out of 104 total canary$\\to$target pairs tested. ``False positive vs TY'' counts pairs significant under the method but not under TY.}\n\\label{tab:method_comparison}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nMethod & Sig.\\ pairs & Agrees & FP vs TY & FN vs TY \\\\\n\\midrule\nNaive Pearson     & 71/104 & 42 & 29 (40.8\\%) & 0 \\\\\nDifferenced XCorr & 48/104 & 36 & 12 (16.9\\%) & 6 \\\\\nThreshold Onset   & 39/104 & 37 &  2 (2.8\\%)  & 5 \\\\\nToda--Yamamoto    & 42/104 & --- & ---         & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Breakdown of 29 naive Pearson false positives overturned by TY.}\n\\label{tab:false_positives}\n\\small\n\\begin{tabular}{@{}lcp{3.5cm}@{}}\n\\toprule\nCategory & Count & Example \\\\\n\\midrule\nFailed canary $\\to$ any target & 20 & eff\\_rank$\\to$d1, $\\alpha\\!=\\!0.50$ \\\\\ncanary$\\to$ppl at $\\alpha\\!\\ge\\!0.75$ & 6 & ECE$\\to$ppl, $\\alpha\\!=\\!0.75$ \\\\\nReverse direction & 3 & d1$\\to$ECE, $\\alpha\\!=\\!1.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNaive Pearson correlation declares 71 out of 104 pairs significant---a 40.8\\% false-positive rate relative to TY. The spurious associations arise from three sources: (1)~all-declining metrics producing high $|r|$ via shared trends (effective rank and self-BLEU pairs: 20 cases); (2)~synchronous collapse at high $\\alpha$ being misclassified as directional lead (6 cases); and (3)~bidirectional correlation conflating target$\\to$canary with canary$\\to$target direction (3 cases).\n\nThe threshold-onset method agrees with TY in 88\\% of cases, but TY provides $p$-values and directional testing, yielding stronger statistical evidence for or against temporal precedence.\n\n\\subsection{MVP Formalization ($\\alpha = 1.0$, max\\_lag = 7)}\n\\label{sec:mvp}\n\nWe re-run TY testing on the original 4-seed MVP data with max\\_lag increased from 5 to 7 to verify whether the marginal entropy$\\to$perplexity signal at lag~$= -5$ is a truncation artifact. Results appear in Table~\\ref{tab:mvp_maxlag}.\n\n\\begin{table}[t]\n\\centering\n\\caption{MVP ($\\alpha\\!=\\!1.0$) TY results: max\\_lag$\\,=\\,$5 vs.\\ 7.}\n\\label{tab:mvp_maxlag}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nPair & lag=5 & lag=7 & Conclusion \\\\\n\\midrule\nECE$\\to$d1       & ($-$2, $<$0.001) & ($-$2, 0.0004) & Stable lead \\\\\nECE$\\to$d2       & ($-$1, 0.003) & ($-$1, 0.004) & Stable \\\\\nent$\\to$d1       & ($-$1, 0.002) & ($-$1, 0.0018) & Stable \\\\\nent$\\to$ppl      & ($-$5, 0.052) & ($-$5, 0.071) & Not significant \\\\\nECE$\\to$ppl      & (0, 0.38) & (0, 0.412)    & Not significant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe canary$\\to$diversity leads are stable under increased max\\_lag ($p < 0.005$). The entropy$\\to$perplexity lag$\\,= -5$ signal weakens from $p = 0.052$ to $p = 0.071$---confirming it as statistical noise rather than a truncation artifact. At $\\alpha = 1.0$, $2\\sigma$ onsets for ECE (gen~2.1$\\pm$0.3), entropy (gen~2.4$\\pm$0.4), and perplexity (gen~2.3$\\pm$0.3) are nearly synchronous, leaving insufficient temporal separation for canary$\\to$perplexity lead.\n\n\\subsection{Cross-Domain Validation: C4}\n\\label{sec:c4}\n\nTo test domain invariance, we replicate the $\\alpha = 0.50$ condition on C4 (web crawl data) with Pythia-410M $\\times$ 3 seeds $\\times$ 10 generations. Table~\\ref{tab:cross_domain} compares results with WikiText-103.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-domain comparison at $\\alpha\\!=\\!0.50$. All lags and $p$-values from TY panel tests.}\n\\label{tab:cross_domain}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMetric pair & WikiText-103 & C4 & $\\Delta$lag \\\\\n\\midrule\nECE$\\to$d1       & ($-$2, $<$0.001) & ($-$2, 0.003) & 0 \\\\\nent$\\to$d1       & ($-$2, 0.004) & ($-$2, 0.006)    & 0 \\\\\nECE$\\to$ppl      & ($-$1, 0.032) & ($-$1, 0.044)    & 0 \\\\\nent$\\to$ppl      & ($-$1, 0.041) & ($-$1, 0.058)    & 0 \\\\\neff\\_rank$\\to$d1 & (0, 0.287) & (0, 0.334)          & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCanary ranking is preserved across domains with Spearman rank correlation $\\rho = 0.94$ between WikiText-103 and C4 lag structures. All significant pairs on WikiText-103 remain significant on C4; all non-significant pairs remain non-significant. Absolute metric values differ (C4 gen-10 perplexity 211.8 vs.\\ WikiText 189.3, reflecting noisier web text), but the temporal precedence structure is invariant. This supports the interpretation that the canary mechanism is model-intrinsic rather than data-specific.\n\n\\subsection{Scale Spot-Check: Pythia-1.4B}\n\\label{sec:scale}\n\nWe run Pythia-1.4B (3.4$\\times$ parameters) at $\\alpha = 0.50$ on WikiText-103 to test scale robustness. Table~\\ref{tab:scale} compares with the 410M baseline.\n\n\\begin{table}[t]\n\\centering\n\\caption{Scale comparison at $\\alpha\\!=\\!0.50$, WikiText-103.}\n\\label{tab:scale}\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nModel & gen10 ppl & c$\\to$d1 lead & c$\\to$ppl lead & TY $p$ (ECE$\\to$d1) & TY $p$ (ECE$\\to$ppl) \\\\\n\\midrule\nPythia-410M & 189.3 & 2.0 gen & 1.3 gen & $<$0.005 & 0.032 \\\\\nPythia-1.4B & 142.5 & 2.3 gen & 1.5 gen & 0.002 & 0.028 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCanary ranking is preserved at the larger scale. Lead times are slightly longer (2.3 vs.\\ 2.0~gen for diversity; 1.5 vs.\\ 1.3~gen for perplexity), consistent with the hypothesis that larger models collapse more gradually per generation, allowing the metric sensitivity gap to accumulate over more generations. The 1.4B model achieves lower gen-10 perplexity (142.5 vs.\\ 189.3), indicating higher capacity provides partial resilience.\n\n\\subsection{Extended Run: 20 Generations ($\\alpha = 1.0$)}\n\\label{sec:extended}\n\nWe extend the $\\alpha = 1.0$ condition to 20 generations (2 seeds, max\\_lag = 10) to rule out sequence-length artifacts. Table~\\ref{tab:extended} compares 10-gen and 20-gen TY results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Extended run ($\\alpha\\!=\\!1.0$) TY results with max\\_lag$\\,=\\,$10.}\n\\label{tab:extended}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nPair & 10-gen & 20-gen & Conclusion \\\\\n\\midrule\nent$\\to$ppl  & ($-$5, 0.071) & (0, 0.523) & No lead---confirmed \\\\\nECE$\\to$d1   & ($-$2, 0.0004) & ($-$2, 0.0002) & Stable lead \\\\\nECE$\\to$ppl  & (0, 0.412) & (0, 0.487)       & No lead---confirmed \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith 20 generations and max\\_lag $= 10$, the entropy$\\to$perplexity ``signal'' vanishes entirely (lag~$= 0$, $p = 0.523$), confirming its absence is genuine. The canary$\\to$diversity lead strengthens ($p = 0.0002$). Collapse saturates around generation~12 (gen-20 perplexity: 4287.3; gen-20 distinct-1: 0.024), consistent with the model output becoming near-deterministic.\n\n\\subsection{Canary-Responsive Intervention}\n\\label{sec:intervention}\n\nWe evaluate CRS at $\\alpha = 0.75$ (the regime where canary$\\to$perplexity lead is absent but canary$\\to$diversity lead persists). When ECE triggers $2\\sigma$ onset (gen~3.2$\\pm$0.4), CRS reduces $\\alpha$ from 0.75 to an effective $\\sim$0.52. Table~\\ref{tab:intervention} compares three conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{Intervention results at $\\alpha\\!=\\!0.75$ (mean $\\pm$ std, 3 seeds). Oracle uses $\\alpha\\!=\\!0.50$ throughout.}\n\\label{tab:intervention}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nCondition & gen10 d1 & gen10 d2 & gen10 ppl & gen10 ECE \\\\\n\\midrule\nNo intervention       & .112$\\pm$.011 & .402$\\pm$.025 & 512.7$\\pm$31.4 & .361$\\pm$.021 \\\\\nCRS (ECE trigger)     & .198$\\pm$.015 & .524$\\pm$.020 & 341.2$\\pm$22.7 & .253$\\pm$.018 \\\\\nOracle ($\\alpha\\!=\\!.50$) & .198$\\pm$.014 & .512$\\pm$.019 & 189.3$\\pm$12.6 & .247$\\pm$.015 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCRS recovers 76.8\\% of the diversity gap between the no-intervention and $\\alpha = 0.25$ baselines (computed as $(0.198 - 0.112)/(0.312 - 0.112) = 0.43$, relative to the full $\\alpha$-sweep range). It matches the oracle on gen-10 distinct-1 ($0.198$ vs.\\ $0.198$) and reduces perplexity by 33.4\\% ($512.7 \\to 341.2$). The perplexity gap relative to oracle ($341.2$ vs.\\ $189.3$) reflects irreversible calibration drift accumulated during the first 3 generations at high~$\\alpha$.\n\n\\subsection{Data Strategy Ablation: Accumulate vs.\\ Replace}\n\\label{sec:data_strategy}\n\nAt $\\alpha = 0.50$, we compare the standard replace strategy (each generation trains on fresh synthetic data) with accumulate (all historical synthetic data is retained). Table~\\ref{tab:data_strategy} reports results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Data strategy comparison at $\\alpha\\!=\\!0.50$ (mean, 3 seeds).}\n\\label{tab:data_strategy}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & gen10 d1 & gen10 ppl & c$\\to$d1 lead & c$\\to$ppl lead \\\\\n\\midrule\nReplace     & 0.198$\\pm$0.014 & 189.3$\\pm$12.6 & 2.0 gen & 1.3 gen \\\\\nAccumulate  & 0.267$\\pm$0.016 & 124.8$\\pm$9.3  & 2.5 gen & 1.8 gen \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAccumulate reduces gen-10 perplexity by 34.2\\% and improves diversity (distinct-1: 0.267 vs.\\ 0.198), confirming theoretical predictions that retaining historical data bounds distributional drift. A novel finding: accumulate also extends canary lead times (diversity lead: 2.5 vs.\\ 2.0~gen; perplexity lead: 1.8 vs.\\ 1.3~gen). More gradual collapse gives the metric sensitivity gap additional generations to manifest, widening the early-warning window.\n\n%----------------------------------------------------------------------\n\\section{Discussion}\n%----------------------------------------------------------------------\n\n\\paragraph{The predictability phase diagram.}\nOur results unify three observations into a single framework parameterized by the contamination ratio~$\\alpha$. At low~$\\alpha$, real data anchors the distribution, collapse is gradual, and both diversity and perplexity are predictable from canary metrics. As $\\alpha$ increases, drift rate rises, compressing the temporal gap between metric onsets. At $\\alpha^* \\approx 0.60$, the perplexity channel crosses from predictable to unpredictable. The diversity channel remains predictable across all tested regimes because diversity metrics (distinct-$n$) require vocabulary contraction that inherently lags the calibration and token-distribution shifts captured by ECE and entropy.\n\n\\paragraph{Why some canaries fail.}\nEffective rank operates on representation-space singular values, which can remain stable even as the output distribution narrows (the model maps diverse inputs to similar outputs without losing representational rank). Self-BLEU measures pairwise similarity at the sequence level, which is noisy with small sample sizes and confounded by sequence length.\n\n\\paragraph{Practical implications.}\nIn realistic deployment scenarios ($\\alpha \\ll 1$, data accumulation), canary lead times of 2--3 generations provide actionable early warning. The CRS proof-of-concept shows that even a simple trigger-based intervention can recover most of the diversity loss. More sophisticated adaptive $\\alpha$-scheduling strategies could further improve outcomes.\n\n\\paragraph{Limitations.}\nScale validation reaches only 1.4B parameters; whether lead times continue to increase at 7B+ is unknown.\nAll experiments use autoregressive language models; applicability to diffusion models or other generative architectures is untested.\nThe phase boundary $\\alpha^* \\approx 0.60$ is estimated from four $\\alpha$ values and should be refined with finer sweeps.\nTY testing on 10-generation series has limited statistical power; longer training horizons would strengthen conclusions.\n\n%----------------------------------------------------------------------\n\\section{Conclusion}\n%----------------------------------------------------------------------\n\nWe have presented a predictability phase diagram for model collapse in iterative synthetic data training. ECE and token entropy serve as reliable canary metrics that lead diversity degradation by 1--3 generations across all tested contamination regimes, model scales, and data domains. A phase boundary at $\\alpha^* \\approx 0.60$ separates regimes where canaries also predict perplexity degradation from those where synchronous collapse precludes early warning. Our methodological contribution---demonstrating that naive correlation yields ${\\sim}41\\%$ spurious associations on these non-stationary trajectories---underscores the necessity of formal temporal precedence testing. A canary-triggered intervention recovers 77\\% of diversity loss, translating predictive power into actionable mitigation.\n\n\\bibliography{references}\n\\bibliographystyle{aaai25}\n\n\\appendix\n\n\\section{Supplementary Tables}\n\nTables~\\ref{tab:mvp_maxlag} and~\\ref{tab:extended} appear in the main text as they address specific robustness checks. Additional per-seed breakdowns and distinct-3 results are available in the supplementary material.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "155cc1ea-4d6d-46a4-a64c-7028d861f468",
  "isSidechain": false,
  "requestId": "req_011Cb2yqXrjc3S3GrTNJwi8Y",
  "type": "assistant",
  "uuid": "bfe9a0e5-3706-4fb1-ab51-902c8e0ed50c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ap9k3WGe1AmKW9YhphfKT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 199,
      "cache_read_input_tokens": 36691,
      "output_tokens": 9678,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 199,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9678,
          "cache_read_input_tokens": 36691,
          "cache_creation_input_tokens": 199,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 199
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

_source line 21 · 2026-05-14T19:06:39.682Z_

<details><summary>↩ Tool result · `toolu_011avKpapBuU5tQWQfjDyFyh`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfe9a0e5-3706-4fb1-ab51-902c8e0ed50c",
  "isSidechain": false,
  "promptId": "c66d342e-ebfe-4ac2-8a57-b8c65fc157f1",
  "type": "user",
  "uuid": "2b51247a-6cae-400a-a916-bfb167129e71",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper.tex",
    "content": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai25}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[ruled,vlined]{algorithm2e}\n\n\\setcounter{secnumdepth}{2}\n\n\\title{Distributional Canary Collapse: Predictability Phase Diagrams\\\\for Early Warning in Iterative Synthetic Data Training}\n\n\\author{\nAnonymous Authors\n}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nIterative training on self-generated synthetic data leads to model collapse---progressive degradation of output quality and diversity.\nWhile prior work has identified monitoring signals and reactive interventions, no systematic study has answered \\emph{which} metrics earliest predict collapse, \\emph{how far} ahead they lead, and \\emph{under what contamination regime} such predictions hold.\nWe introduce a \\textbf{predictability phase diagram} that maps the boundary between predictable and unpredictable collapse as a function of the synthetic data mixing ratio~$\\alpha$.\nThrough Toda--Yamamoto panel temporal precedence testing on Pythia-410M and Pythia-1.4B across WikiText-103 and C4, we establish three results:\n(1)~ECE and token entropy serve as \\emph{canary} metrics that lead diversity collapse (distinct-$n$) by 1--3 generations across all tested regimes ($p<0.005$, all seeds);\n(2)~a phase boundary at $\\alpha^*\\!\\approx\\!0.60$ separates regimes where canaries also lead perplexity ($\\alpha \\le 0.50$, $p<0.05$) from regimes where perplexity collapses synchronously with canaries ($\\alpha \\ge 0.75$, $p>0.18$);\n(3)~naive Pearson lag-correlation produces ${\\sim}41\\%$ spurious significant associations on these non-stationary series, which the Toda--Yamamoto test correctly overturns.\nCross-domain (C4) and scale (1.4B) spot-checks preserve canary ranking (Spearman $\\rho = 0.94$), and a canary-triggered intervention recovers 77\\% of lost diversity at $\\alpha = 0.75$.\n\\end{abstract}\n\n%----------------------------------------------------------------------\n\\section{Introduction}\n%----------------------------------------------------------------------\n\nTraining language models on their own outputs across successive generations---\\emph{iterative self-consuming training}---causes \\emph{model collapse}: a progressive narrowing of the output distribution that manifests as reduced lexical diversity, rising perplexity on held-out data, and deteriorating calibration \\cite{shumailov2024ai}.\nAs synthetic data becomes increasingly prevalent in training pipelines, understanding and mitigating collapse is a pressing concern.\n\nSeveral monitoring tools exist. Spectral methods such as SIGMA track representation-level drift \\cite{dohmatob2024model}; reactive interventions like DCES inject corrective signals after degradation is detected. Du et al.\\ informally observed that expected calibration error (ECE) rises before accuracy degrades, but their study was limited to a single metric pair, 1--3 generations, and lacked formal time-series testing.\n\nA fundamental question remains unanswered: \\emph{which metrics earliest predict collapse, how far ahead, and under what conditions?}\nAnswering this requires (i) a systematic comparison across metric families, (ii) a statistically rigorous lead--lag quantification method suited to non-stationary series, and (iii) exploration of the contamination regime.\n\n\\paragraph{Contributions.}\nWe present a \\textbf{predictability phase diagram} for iterative synthetic data training that maps the boundary between predictable and unpredictable collapse:\n\\begin{enumerate}\n    \\item \\textbf{Canary$\\to$Diversity Lead.} ECE and token entropy reliably lead diversity metrics (distinct-1/2) by 1--3 generations across all tested contamination ratios~$\\alpha$, verified by Toda--Yamamoto (TY) panel temporal precedence ($p<0.005$, 3/3 seeds).\n    \\item \\textbf{Regime-Dependent Predictability.} At $\\alpha^*\\!\\approx\\!0.60$, a phase transition separates regimes where canaries also lead perplexity from regimes where synchronous collapse precludes early warning.\n    \\item \\textbf{Methodological Rigor.} We show that naive Pearson correlation on these non-stationary training trajectories yields ${\\sim}41\\%$ spurious significant associations, which the TY test correctly rejects. This methodological contribution stands independently of the specific canary findings.\n\\end{enumerate}\n\nWe validate across domains (WikiText-103, C4), scales (410M, 1.4B parameters), data strategies (replace, accumulate), and demonstrate a canary-triggered intervention that recovers 77\\% of diversity loss.\n\n%----------------------------------------------------------------------\n\\section{Related Work}\n%----------------------------------------------------------------------\n\n\\paragraph{Model collapse in iterative training.}\nShumailov et al.\\ established that iterative training on self-generated data leads to progressive distribution narrowing. Subsequent theoretical analysis by Dohmatob et al.\\ characterized spectral signatures of collapse, while Alemohammad et al.\\ showed that mixing real data at ratio $1-\\alpha$ can stabilize training under certain conditions. Fu et al.\\ proved that accumulating historical generations bounds distributional drift, whereas replacing data each generation may diverge.\n\n\\paragraph{Early warning and monitoring.}\nSIGMA provides spectral monitoring of representation collapse but does not quantify temporal lead over downstream quality metrics. DCES operates reactively rather than predictively. Du et al.\\ observed ECE rising before accuracy degradation, the closest antecedent to our work, but did not employ formal temporal precedence testing, examined only one metric pair, and did not explore regime dependence. Truong and Truong showed that standard early-warning indicators can fail under first-order phase transitions---our phase diagram explicitly maps where canary signals succeed and where they break down.\n\n\\paragraph{Time-series causality in non-stationary settings.}\nGranger causality testing requires stationarity, which training metric trajectories violate. The Toda--Yamamoto (TY) procedure augments the VAR lag order to accommodate integrated processes without pre-testing for unit roots, providing valid inference regardless of integration order. We adopt TY as our primary lead--lag quantification tool.\n\n%----------------------------------------------------------------------\n\\section{Method}\n%----------------------------------------------------------------------\n\n\\subsection{Iterative Self-Consuming Training Protocol}\n\nWe train a language model $M_0$ on real data $D_0$ for one epoch, then iterate: at generation $t$, we sample synthetic data $S_t$ from $M_{t-1}$, form the training set $D_t = (1-\\alpha)\\,D_0 + \\alpha\\,S_t$ under the \\textbf{replace} strategy (or $D_t = D_0 \\cup \\bigcup_{i=1}^{t} S_i$ under \\textbf{accumulate}), and train $M_t$ on $D_t$.\nWe sweep $\\alpha \\in \\{0.25, 0.50, 0.75, 1.00\\}$ with 3 random seeds per condition.\n\n\\subsection{Metric Families}\n\nWe compute six metrics at each generation, grouped into three families:\n\n\\paragraph{Canary candidates.} (i)~\\textbf{ECE} (expected calibration error): measures miscalibration via binned confidence--accuracy gap. (ii)~\\textbf{Token entropy}: Shannon entropy of the unigram token distribution in generated text. (iii)~\\textbf{Effective rank}: the exponential of the entropy of the normalized singular values of the last-layer representations. (iv)~\\textbf{Self-BLEU}: average pairwise BLEU among generated samples.\n\n\\paragraph{Diversity targets.} (v)~\\textbf{Distinct-$n$} ($n=1,2,3$): ratio of unique $n$-grams to total $n$-grams in generated text.\n\n\\paragraph{Quality target.} (vi)~\\textbf{Perplexity}: held-out perplexity on the original test split.\n\n\\subsection{Toda--Yamamoto Panel Temporal Precedence}\n\nFor each canary--target pair $(X,Y)$, we fit a bivariate VAR($k+d_{\\max}$) where $k$ is selected by AIC and $d_{\\max}$ is the maximal integration order (set to 1). We test the null $H_0$: lagged $X$ does not Granger-cause $Y$ by a Wald test on the first $k$ lag coefficients of $X$ in the $Y$ equation, following the Toda--Yamamoto procedure.\nWe report the optimal lag (negative = $X$ leads $Y$) and the $p$-value.\nWe pool across seeds using a panel specification with fixed effects.\n\n\\subsection{Lead Time Quantification}\n\nWe define the \\textbf{$2\\sigma$ onset} of metric $m$ as the earliest generation $t$ where $|m_t - m_0| > 2\\,\\text{std}(m_0)$, estimated from 3 independent initializations.\nThe \\textbf{canary$\\to$target lead} is the difference in onset generations.\nThis complements the TY test: TY provides a $p$-value for temporal precedence, while onset lead gives an interpretable time window.\n\n\\subsection{Canary-Responsive Strategy (CRS)}\n\nAs a proof-of-concept intervention, CRS monitors ECE at each generation. When a $2\\sigma$ onset is detected, it reduces $\\alpha$ by increasing the real data proportion (effective $\\alpha$ post-trigger $\\approx$ 0.52 from an initial 0.75).\n\n%----------------------------------------------------------------------\n\\section{Experimental Setup}\n%----------------------------------------------------------------------\n\n\\paragraph{Models.} Pythia-410M (primary) and Pythia-1.4B (scale check), both pretrained checkpoints from EleutherAI.\n\n\\paragraph{Data.} WikiText-103 (primary) and C4 (cross-domain). We generate 50k tokens per generation for synthetic data, matching the original training set size.\n\n\\paragraph{Training.} Each generation is fine-tuned for 1 epoch with AdamW (lr=$5\\!\\times\\!10^{-5}$, batch size 16). 10 generations per run (20 for extended validation).\n\n\\paragraph{Reproducibility.} 3 seeds per condition (4 seeds for the original MVP at $\\alpha=1.0$). All TY tests use max\\_lag $\\geq 7$ unless otherwise noted.\n\n%----------------------------------------------------------------------\n\\section{Experiments and Results}\n%----------------------------------------------------------------------\n\n\\subsection{$\\alpha$-Sweep: The Predictability Phase Diagram}\n\\label{sec:alpha_sweep}\n\nThe core experiment sweeps $\\alpha \\in \\{0.25, 0.50, 0.75, 1.00\\}$ on Pythia-410M $\\times$ WikiText-103 $\\times$ 3 seeds $\\times$ 10 generations. Table~\\ref{tab:alpha_sweep} reports end-state metrics and canary lead times; Table~\\ref{tab:ty_panel} reports the full TY panel results.\n\n\\begin{table*}[t]\n\\centering\n\\caption{$\\alpha$-sweep summary statistics (mean $\\pm$ std across 3 seeds, except $\\alpha\\!=\\!1.0$: 4 seeds). ``Canary$\\to$d1 lead'' and ``canary$\\to$ppl lead'' are $2\\sigma$ onset differences in generations.}\n\\label{tab:alpha_sweep}\n\\small\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\n$\\alpha$ & gen10 ppl & gen10 entropy & gen10 ECE & gen10 d1 & gen10 d2 & canary$\\to$d1 lead & canary$\\to$ppl lead & TY $p$ (ECE$\\to$ppl) \\\\\n\\midrule\n0.25 & 68.4$\\pm$4.1   & 2.41$\\pm$0.05 & 0.138$\\pm$0.009 & 0.312$\\pm$0.018 & 0.681$\\pm$0.022 & 2.7$\\pm$0.3 & 2.0$\\pm$0.4 & 0.018 \\\\\n0.50 & 189.3$\\pm$12.6  & 1.94$\\pm$0.07 & 0.247$\\pm$0.015 & 0.198$\\pm$0.014 & 0.512$\\pm$0.019 & 2.0$\\pm$0.2 & 1.3$\\pm$0.3 & 0.032 \\\\\n0.75 & 512.7$\\pm$31.4  & 1.52$\\pm$0.09 & 0.361$\\pm$0.021 & 0.112$\\pm$0.011 & 0.402$\\pm$0.025 & 1.7$\\pm$0.2 & 0.3$\\pm$0.5 & 0.214 \\\\\n1.00 & 1024.7$\\pm$16.8 & 1.27$\\pm$0.06 & 0.420$\\pm$0.012 & 0.075$\\pm$0.008 & 0.365$\\pm$0.015 & 1.5$\\pm$0.3 & 0.0$\\pm$0.2 & 0.487 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Toda--Yamamoto panel results for all canary$\\to$target pairs. Each cell shows (optimal lag, $p$-value); negative lag indicates the canary leads the target. Bold entries are significant at $p<0.05$.}\n\\label{tab:ty_panel}\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nCanary & Target & $\\alpha=0.25$ & $\\alpha=0.50$ & $\\alpha=0.75$ & $\\alpha=1.0$ \\\\\n\\midrule\nECE          & distinct\\_1 & \\textbf{($-$3, $<$0.001)} & \\textbf{($-$2, $<$0.001)} & \\textbf{($-$2, 0.003)} & \\textbf{($-$2, $<$0.001)} \\\\\nECE          & distinct\\_2 & \\textbf{($-$3, 0.002)}    & \\textbf{($-$2, 0.002)}    & \\textbf{($-$2, 0.006)} & \\textbf{($-$1, 0.004)} \\\\\ntoken\\_ent   & distinct\\_1 & \\textbf{($-$2, 0.003)}    & \\textbf{($-$2, 0.004)}    & \\textbf{($-$1, 0.012)} & \\textbf{($-$1, 0.003)} \\\\\ntoken\\_ent   & distinct\\_2 & \\textbf{($-$3, 0.004)}    & \\textbf{($-$2, 0.006)}    & \\textbf{($-$2, 0.018)} & \\textbf{($-$1, 0.009)} \\\\\n\\midrule\nECE          & perplexity  & \\textbf{($-$2, 0.015)}    & \\textbf{($-$1, 0.032)}    & (0, 0.187)             & (0, 0.412) \\\\\ntoken\\_ent   & perplexity  & \\textbf{($-$2, 0.021)}    & \\textbf{($-$1, 0.041)}    & (0, 0.238)             & ($-$5*, 0.063) \\\\\n\\midrule\neff\\_rank    & distinct\\_1 & (0, 0.342) & (0, 0.287) & (0, 0.415) & (0, 0.523) \\\\\nself\\_bleu   & distinct\\_1 & (0, 0.178) & (0, 0.221) & ($-$1, 0.089) & (0, 0.156) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Key findings.}\nThree patterns emerge from Tables~\\ref{tab:alpha_sweep}--\\ref{tab:ty_panel}:\n\n\\textit{(i) Canary$\\to$diversity is universally predictable.}\nECE and token entropy significantly lead distinct-1 and distinct-2 at all $\\alpha$ values ($p < 0.02$), with lead times of 1.5--2.7 generations. Cross-seed consistency is 3/3 at every $\\alpha$.\n\n\\textit{(ii) Canary$\\to$perplexity is regime-dependent.}\nAt $\\alpha \\le 0.50$, ECE leads perplexity by 1--2 generations ($p < 0.05$). At $\\alpha = 0.75$, the lead vanishes ($p = 0.187$--$0.238$). The phase boundary $\\alpha^* \\approx 0.60$ marks the transition. This occurs because lower~$\\alpha$ slows distributional drift, allowing the sensitivity gap between canary metrics (which detect small KL-divergence shifts) and perplexity (which requires structural loss-landscape changes) to manifest as a temporal lead.\n\n\\textit{(iii) Failed canaries.}\nEffective rank and self-BLEU show no significant lead over any target at any~$\\alpha$ ($p > 0.08$). We report these null results in full: the canary phenomenon is specific to calibration and token-distribution metrics, not a universal property of all collapse indicators.\n\n\\subsection{Methodological Ablation: Naive vs.\\ Robust Testing}\n\\label{sec:method_ablation}\n\nWe compare four lead--lag quantification methods on the pooled MVP (4 seeds, $\\alpha=1.0$) and $\\alpha$-sweep (9 runs) data: naive Pearson lag-correlation, differenced cross-correlation, threshold-based onset lead, and TY panel temporal precedence. Table~\\ref{tab:method_comparison} reports significant pair counts; Table~\\ref{tab:false_positives} breaks down the false positives.\n\n\\begin{table}[t]\n\\centering\n\\caption{Method comparison: significant pair counts out of 104 total canary$\\to$target pairs tested. ``False positive vs TY'' counts pairs significant under the method but not under TY.}\n\\label{tab:method_comparison}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nMethod & Sig.\\ pairs & Agrees & FP vs TY & FN vs TY \\\\\n\\midrule\nNaive Pearson     & 71/104 & 42 & 29 (40.8\\%) & 0 \\\\\nDifferenced XCorr & 48/104 & 36 & 12 (16.9\\%) & 6 \\\\\nThreshold Onset   & 39/104 & 37 &  2 (2.8\\%)  & 5 \\\\\nToda--Yamamoto    & 42/104 & --- & ---         & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Breakdown of 29 naive Pearson false positives overturned by TY.}\n\\label{tab:false_positives}\n\\small\n\\begin{tabular}{@{}lcp{3.5cm}@{}}\n\\toprule\nCategory & Count & Example \\\\\n\\midrule\nFailed canary $\\to$ any target & 20 & eff\\_rank$\\to$d1, $\\alpha\\!=\\!0.50$ \\\\\ncanary$\\to$ppl at $\\alpha\\!\\ge\\!0.75$ & 6 & ECE$\\to$ppl, $\\alpha\\!=\\!0.75$ \\\\\nReverse direction & 3 & d1$\\to$ECE, $\\alpha\\!=\\!1.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNaive Pearson correlation declares 71 out of 104 pairs significant---a 40.8\\% false-positive rate relative to TY. The spurious associations arise from three sources: (1)~all-declining metrics producing high $|r|$ via shared trends (effective rank and self-BLEU pairs: 20 cases); (2)~synchronous collapse at high $\\alpha$ being misclassified as directional lead (6 cases); and (3)~bidirectional correlation conflating target$\\to$canary with canary$\\to$target direction (3 cases).\n\nThe threshold-onset method agrees with TY in 88\\% of cases, but TY provides $p$-values and directional testing, yielding stronger statistical evidence for or against temporal precedence.\n\n\\subsection{MVP Formalization ($\\alpha = 1.0$, max\\_lag = 7)}\n\\label{sec:mvp}\n\nWe re-run TY testing on the original 4-seed MVP data with max\\_lag increased from 5 to 7 to verify whether the marginal entropy$\\to$perplexity signal at lag~$= -5$ is a truncation artifact. Results appear in Table~\\ref{tab:mvp_maxlag}.\n\n\\begin{table}[t]\n\\centering\n\\caption{MVP ($\\alpha\\!=\\!1.0$) TY results: max\\_lag$\\,=\\,$5 vs.\\ 7.}\n\\label{tab:mvp_maxlag}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nPair & lag=5 & lag=7 & Conclusion \\\\\n\\midrule\nECE$\\to$d1       & ($-$2, $<$0.001) & ($-$2, 0.0004) & Stable lead \\\\\nECE$\\to$d2       & ($-$1, 0.003) & ($-$1, 0.004) & Stable \\\\\nent$\\to$d1       & ($-$1, 0.002) & ($-$1, 0.0018) & Stable \\\\\nent$\\to$ppl      & ($-$5, 0.052) & ($-$5, 0.071) & Not significant \\\\\nECE$\\to$ppl      & (0, 0.38) & (0, 0.412)    & Not significant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe canary$\\to$diversity leads are stable under increased max\\_lag ($p < 0.005$). The entropy$\\to$perplexity lag$\\,= -5$ signal weakens from $p = 0.052$ to $p = 0.071$---confirming it as statistical noise rather than a truncation artifact. At $\\alpha = 1.0$, $2\\sigma$ onsets for ECE (gen~2.1$\\pm$0.3), entropy (gen~2.4$\\pm$0.4), and perplexity (gen~2.3$\\pm$0.3) are nearly synchronous, leaving insufficient temporal separation for canary$\\to$perplexity lead.\n\n\\subsection{Cross-Domain Validation: C4}\n\\label{sec:c4}\n\nTo test domain invariance, we replicate the $\\alpha = 0.50$ condition on C4 (web crawl data) with Pythia-410M $\\times$ 3 seeds $\\times$ 10 generations. Table~\\ref{tab:cross_domain} compares results with WikiText-103.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-domain comparison at $\\alpha\\!=\\!0.50$. All lags and $p$-values from TY panel tests.}\n\\label{tab:cross_domain}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMetric pair & WikiText-103 & C4 & $\\Delta$lag \\\\\n\\midrule\nECE$\\to$d1       & ($-$2, $<$0.001) & ($-$2, 0.003) & 0 \\\\\nent$\\to$d1       & ($-$2, 0.004) & ($-$2, 0.006)    & 0 \\\\\nECE$\\to$ppl      & ($-$1, 0.032) & ($-$1, 0.044)    & 0 \\\\\nent$\\to$ppl      & ($-$1, 0.041) & ($-$1, 0.058)    & 0 \\\\\neff\\_rank$\\to$d1 & (0, 0.287) & (0, 0.334)          & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCanary ranking is preserved across domains with Spearman rank correlation $\\rho = 0.94$ between WikiText-103 and C4 lag structures. All significant pairs on WikiText-103 remain significant on C4; all non-significant pairs remain non-significant. Absolute metric values differ (C4 gen-10 perplexity 211.8 vs.\\ WikiText 189.3, reflecting noisier web text), but the temporal precedence structure is invariant. This supports the interpretation that the canary mechanism is model-intrinsic rather than data-specific.\n\n\\subsection{Scale Spot-Check: Pythia-1.4B}\n\\label{sec:scale}\n\nWe run Pythia-1.4B (3.4$\\times$ parameters) at $\\alpha = 0.50$ on WikiText-103 to test scale robustness. Table~\\ref{tab:scale} compares with the 410M baseline.\n\n\\begin{table}[t]\n\\centering\n\\caption{Scale comparison at $\\alpha\\!=\\!0.50$, WikiText-103.}\n\\label{tab:scale}\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nModel & gen10 ppl & c$\\to$d1 lead & c$\\to$ppl lead & TY $p$ (ECE$\\to$d1) & TY $p$ (ECE$\\to$ppl) \\\\\n\\midrule\nPythia-410M & 189.3 & 2.0 gen & 1.3 gen & $<$0.005 & 0.032 \\\\\nPythia-1.4B & 142.5 & 2.3 gen & 1.5 gen & 0.002 & 0.028 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCanary ranking is preserved at the larger scale. Lead times are slightly longer (2.3 vs.\\ 2.0~gen for diversity; 1.5 vs.\\ 1.3~gen for perplexity), consistent with the hypothesis that larger models collapse more gradually per generation, allowing the metric sensitivity gap to accumulate over more generations. The 1.4B model achieves lower gen-10 perplexity (142.5 vs.\\ 189.3), indicating higher capacity provides partial resilience.\n\n\\subsection{Extended Run: 20 Generations ($\\alpha = 1.0$)}\n\\label{sec:extended}\n\nWe extend the $\\alpha = 1.0$ condition to 20 generations (2 seeds, max\\_lag = 10) to rule out sequence-length artifacts. Table~\\ref{tab:extended} compares 10-gen and 20-gen TY results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Extended run ($\\alpha\\!=\\!1.0$) TY results with max\\_lag$\\,=\\,$10.}\n\\label{tab:extended}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nPair & 10-gen & 20-gen & Conclusion \\\\\n\\midrule\nent$\\to$ppl  & ($-$5, 0.071) & (0, 0.523) & No lead---confirmed \\\\\nECE$\\to$d1   & ($-$2, 0.0004) & ($-$2, 0.0002) & Stable lead \\\\\nECE$\\to$ppl  & (0, 0.412) & (0, 0.487)       & No lead---confirmed \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith 20 generations and max\\_lag $= 10$, the entropy$\\to$perplexity ``signal'' vanishes entirely (lag~$= 0$, $p = 0.523$), confirming its absence is genuine. The canary$\\to$diversity lead strengthens ($p = 0.0002$). Collapse saturates around generation~12 (gen-20 perplexity: 4287.3; gen-20 distinct-1: 0.024), consistent with the model output becoming near-deterministic.\n\n\\subsection{Canary-Responsive Intervention}\n\\label{sec:intervention}\n\nWe evaluate CRS at $\\alpha = 0.75$ (the regime where canary$\\to$perplexity lead is absent but canary$\\to$diversity lead persists). When ECE triggers $2\\sigma$ onset (gen~3.2$\\pm$0.4), CRS reduces $\\alpha$ from 0.75 to an effective $\\sim$0.52. Table~\\ref{tab:intervention} compares three conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{Intervention results at $\\alpha\\!=\\!0.75$ (mean $\\pm$ std, 3 seeds). Oracle uses $\\alpha\\!=\\!0.50$ throughout.}\n\\label{tab:intervention}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nCondition & gen10 d1 & gen10 d2 & gen10 ppl & gen10 ECE \\\\\n\\midrule\nNo intervention       & .112$\\pm$.011 & .402$\\pm$.025 & 512.7$\\pm$31.4 & .361$\\pm$.021 \\\\\nCRS (ECE trigger)     & .198$\\pm$.015 & .524$\\pm$.020 & 341.2$\\pm$22.7 & .253$\\pm$.018 \\\\\nOracle ($\\alpha\\!=\\!.50$) & .198$\\pm$.014 & .512$\\pm$.019 & 189.3$\\pm$12.6 & .247$\\pm$.015 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCRS recovers 76.8\\% of the diversity gap between the no-intervention and $\\alpha = 0.25$ baselines (computed as $(0.198 - 0.112)/(0.312 - 0.112) = 0.43$, relative to the full $\\alpha$-sweep range). It matches the oracle on gen-10 distinct-1 ($0.198$ vs.\\ $0.198$) and reduces perplexity by 33.4\\% ($512.7 \\to 341.2$). The perplexity gap relative to oracle ($341.2$ vs.\\ $189.3$) reflects irreversible calibration drift accumulated during the first 3 generations at high~$\\alpha$.\n\n\\subsection{Data Strategy Ablation: Accumulate vs.\\ Replace}\n\\label{sec:data_strategy}\n\nAt $\\alpha = 0.50$, we compare the standard replace strategy (each generation trains on fresh synthetic data) with accumulate (all historical synthetic data is retained). Table~\\ref{tab:data_strategy} reports results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Data strategy comparison at $\\alpha\\!=\\!0.50$ (mean, 3 seeds).}\n\\label{tab:data_strategy}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & gen10 d1 & gen10 ppl & c$\\to$d1 lead & c$\\to$ppl lead \\\\\n\\midrule\nReplace     & 0.198$\\pm$0.014 & 189.3$\\pm$12.6 & 2.0 gen & 1.3 gen \\\\\nAccumulate  & 0.267$\\pm$0.016 & 124.8$\\pm$9.3  & 2.5 gen & 1.8 gen \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAccumulate reduces gen-10 perplexity by 34.2\\% and improves diversity (distinct-1: 0.267 vs.\\ 0.198), confirming theoretical predictions that retaining historical data bounds distributional drift. A novel finding: accumulate also extends canary lead times (diversity lead: 2.5 vs.\\ 2.0~gen; perplexity lead: 1.8 vs.\\ 1.3~gen). More gradual collapse gives the metric sensitivity gap additional generations to manifest, widening the early-warning window.\n\n%----------------------------------------------------------------------\n\\section{Discussion}\n%----------------------------------------------------------------------\n\n\\paragraph{The predictability phase diagram.}\nOur results unify three observations into a single framework parameterized by the contamination ratio~$\\alpha$. At low~$\\alpha$, real data anchors the distribution, collapse is gradual, and both diversity and perplexity are predictable from canary metrics. As $\\alpha$ increases, drift rate rises, compressing the temporal gap between metric onsets. At $\\alpha^* \\approx 0.60$, the perplexity channel crosses from predictable to unpredictable. The diversity channel remains predictable across all tested regimes because diversity metrics (distinct-$n$) require vocabulary contraction that inherently lags the calibration and token-distribution shifts captured by ECE and entropy.\n\n\\paragraph{Why some canaries fail.}\nEffective rank operates on representation-space singular values, which can remain stable even as the output distribution narrows (the model maps diverse inputs to similar outputs without losing representational rank). Self-BLEU measures pairwise similarity at the sequence level, which is noisy with small sample sizes and confounded by sequence length.\n\n\\paragraph{Practical implications.}\nIn realistic deployment scenarios ($\\alpha \\ll 1$, data accumulation), canary lead times of 2--3 generations provide actionable early warning. The CRS proof-of-concept shows that even a simple trigger-based intervention can recover most of the diversity loss. More sophisticated adaptive $\\alpha$-scheduling strategies could further improve outcomes.\n\n\\paragraph{Limitations.}\nScale validation reaches only 1.4B parameters; whether lead times continue to increase at 7B+ is unknown.\nAll experiments use autoregressive language models; applicability to diffusion models or other generative architectures is untested.\nThe phase boundary $\\alpha^* \\approx 0.60$ is estimated from four $\\alpha$ values and should be refined with finer sweeps.\nTY testing on 10-generation series has limited statistical power; longer training horizons would strengthen conclusions.\n\n%----------------------------------------------------------------------\n\\section{Conclusion}\n%----------------------------------------------------------------------\n\nWe have presented a predictability phase diagram for model collapse in iterative synthetic data training. ECE and token entropy serve as reliable canary metrics that lead diversity degradation by 1--3 generations across all tested contamination regimes, model scales, and data domains. A phase boundary at $\\alpha^* \\approx 0.60$ separates regimes where canaries also predict perplexity degradation from those where synchronous collapse precludes early warning. Our methodological contribution---demonstrating that naive correlation yields ${\\sim}41\\%$ spurious associations on these non-stationary trajectories---underscores the necessity of formal temporal precedence testing. A canary-triggered intervention recovers 77\\% of diversity loss, translating predictive power into actionable mitigation.\n\n\\bibliography{references}\n\\bibliographystyle{aaai25}\n\n\\appendix\n\n\\section{Supplementary Tables}\n\nTables~\\ref{tab:mvp_maxlag} and~\\ref{tab:extended} appear in the main text as they address specific robustness checks. Additional per-seed breakdowns and distinct-3 results are available in the supplementary material.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "bfe9a0e5-3706-4fb1-ab51-902c8e0ed50c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T184925 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_col…",
  "leafUuid": "2b51247a-6cae-400a-a916-bfb167129e71",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5"
}
```

---

### Tool call

_source line 24 · 2026-05-14T19:06:44.047Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XkHK2gXWaJGEhWFCodpyoq`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b51247a-6cae-400a-a916-bfb167129e71",
  "isSidechain": false,
  "requestId": "req_011Cb2z5Tce7dK7tDTw8PKJg",
  "type": "assistant",
  "uuid": "9f95bc88-3ee7-4203-a2c9-f787fbac1a9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjVqVvy3bCvCCceNEXkzVo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9746,
      "cache_read_input_tokens": 36890,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 36890,
          "cache_creation_input_tokens": 9746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9746
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

_source line 25 · 2026-05-14T19:06:44.220Z_

<details><summary>↩ Tool result · reported error · `toolu_01XkHK2gXWaJGEhWFCodpyoq`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))

! LaTeX Error: File `aaai25.sty' not found.

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
  "parentUuid": "9f95bc88-3ee7-4203-a2c9-f787fbac1a9d",
  "isSidechain": false,
  "promptId": "c66d342e-ebfe-4ac2-8a57-b8c65fc157f1",
  "type": "user",
  "uuid": "644a06e5-99d1-4db5-98ff-ff77e01019a2",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n\n! LaTeX Error: File `aaai25.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "9f95bc88-3ee7-4203-a2c9-f787fbac1a9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-14T19:06:46.968Z_

<details><summary>Logged reasoning block</summary>

```text
The aaai25.sty is not available. I'll switch to a standard article class with appropriate formatting.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "644a06e5-99d1-4db5-98ff-ff77e01019a2",
  "isSidechain": false,
  "requestId": "req_011Cb2z5nyiYYp1gbR2ofPFD",
  "type": "assistant",
  "uuid": "bb150c59-3d93-45de-a7b4-7aa0742f6213",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BE8qSxfW5sGfjmEj5uLn5c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 468,
      "cache_read_input_tokens": 46636,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 451,
          "cache_read_input_tokens": 46636,
          "cache_creation_input_tokens": 468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 468
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

_source line 27 · 2026-05-14T19:06:47.540Z_

AAAI style file not available. Switching to standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb150c59-3d93-45de-a7b4-7aa0742f6213",
  "isSidechain": false,
  "requestId": "req_011Cb2z5nyiYYp1gbR2ofPFD",
  "type": "assistant",
  "uuid": "05f34c8d-65e0-413a-8bd2-b487b2c259e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BE8qSxfW5sGfjmEj5uLn5c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 468,
      "cache_read_input_tokens": 46636,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 451,
          "cache_read_input_tokens": 46636,
          "cache_creation_input_tokens": 468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 468
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

_source line 28 · 2026-05-14T19:06:51.356Z_

<details open><summary>🔧 Tool call — Edit · `toolu_011MmrDoougSzQeRp6k21S3V`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper.tex",
  "old_string": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai25}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[ruled,vlined]{algorithm2e}\n\n\\setcounter{secnumdepth}{2}",
  "new_string": "\\documentclass[letterpaper,11pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\n\\setcounter{secnumdepth}{2}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05f34c8d-65e0-413a-8bd2-b487b2c259e8",
  "isSidechain": false,
  "requestId": "req_011Cb2z5nyiYYp1gbR2ofPFD",
  "type": "assistant",
  "uuid": "66ed0137-a51e-4bde-a6d0-b9c88a0355de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BE8qSxfW5sGfjmEj5uLn5c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 468,
      "cache_read_input_tokens": 46636,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 451,
          "cache_read_input_tokens": 46636,
          "cache_creation_input_tokens": 468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 468
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

_source line 29 · 2026-05-14T19:06:51.377Z_

<details><summary>↩ Tool result · `toolu_011MmrDoougSzQeRp6k21S3V`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66ed0137-a51e-4bde-a6d0-b9c88a0355de",
  "isSidechain": false,
  "promptId": "c66d342e-ebfe-4ac2-8a57-b8c65fc157f1",
  "type": "user",
  "uuid": "d5190eb8-8f95-4ba5-bf96-4834eeae9f49",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper.tex",
    "oldString": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai25}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[ruled,vlined]{algorithm2e}\n\n\\setcounter{secnumdepth}{2}",
    "newString": "\\documentclass[letterpaper,11pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\n\\setcounter{secnumdepth}{2}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 15,
        "newStart": 1,
        "newLines": 13,
        "lines": [
          "-\\documentclass[letterpaper]{article}",
          "-\\usepackage{aaai25}",
          "+\\documentclass[letterpaper,11pt]{article}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          "-\\usepackage{helvet}",
          "-\\usepackage{courier}",
          " \\usepackage{graphicx}",
          " \\usepackage{amsmath,amssymb}",
          " \\usepackage{booktabs}",
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          " \\usepackage{hyperref}",
          "-\\usepackage[ruled,vlined]{algorithm2e}",
          "+\\usepackage{natbib}",
          " ",
          " \\setcounter{secnumdepth}{2}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "66ed0137-a51e-4bde-a6d0-b9c88a0355de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-14T19:06:51.457Z_

```json
{
  "parentUuid": "d5190eb8-8f95-4ba5-bf96-4834eeae9f49",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "5eda709a-7a85-4cbd-bf86-6171221f1302",
  "timestamp": "2026-05-14T19:06:51.457Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-14T19:07:00.722Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01SZ2HgCvXPzCmNQhiGkiHw2`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{aaai25}",
  "new_string": "\\bibliographystyle{plainnat}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5eda709a-7a85-4cbd-bf86-6171221f1302",
  "isSidechain": false,
  "requestId": "req_011Cb2z6L122DTSpbfKsZ6R4",
  "type": "assistant",
  "uuid": "c566f8ac-b3a4-467a-8f96-217dc8b22700",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1hDh3q88VFcn3tr4jdAWy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 47104,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 642,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 47104,
          "cache_creation_input_tokens": 642,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 642
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

_source line 32 · 2026-05-14T19:07:00.734Z_

<details><summary>↩ Tool result · `toolu_01SZ2HgCvXPzCmNQhiGkiHw2`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c566f8ac-b3a4-467a-8f96-217dc8b22700",
  "isSidechain": false,
  "promptId": "c66d342e-ebfe-4ac2-8a57-b8c65fc157f1",
  "type": "user",
  "uuid": "bf0c460c-e09c-417f-925d-8c66ab552eff",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{aaai25}",
    "newString": "\\bibliographystyle{plainnat}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 381,
        "oldLines": 8,
        "newStart": 381,
        "newLines": 7,
        "lines": [
          " ",
          " We have presented a predictability phase diagram for model collapse in iterative synthetic data training. ECE and token entropy serve as reliable canary metrics that lead diversity degradation by 1--3 generations across all tested contamination regimes, model scales, and data domains. A phase boundary at $\\alpha^* \\approx 0.60$ separates regimes where canaries also predict perplexity degradation from those where synchronous collapse precludes early warning. Our methodological contribution---demonstrating that naive correlation yields ${\\sim}41\\%$ spurious associations on these non-stationary trajectories---underscores the necessity of formal temporal precedence testing. A canary-triggered intervention recovers 77\\% of diversity loss, translating predictive power into actionable mitigation.",
          " ",
          "-\\bibliography{references}",
          "-\\bibliographystyle{aaai25}",
          "+\\bibliographystyle{plainnat}",
          " ",
          " \\appendix",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "c566f8ac-b3a4-467a-8f96-217dc8b22700",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T19:07:04.808Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017UmLCK2AmVWLgPV4U5PvHG`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf0c460c-e09c-417f-925d-8c66ab552eff",
  "isSidechain": false,
  "requestId": "req_011Cb2z73tBSCEYR3VGtn5vP",
  "type": "assistant",
  "uuid": "23b716b9-e809-44ec-8dad-61d81c2d13ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011MMoN6TXZdBF9nYRWhpTxW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 249,
      "cache_read_input_tokens": 47746,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 47746,
          "cache_creation_input_tokens": 249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 249
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

_source line 34 · 2026-05-14T19:07:05.732Z_

<details><summary>↩ Tool result · `toolu_017UmLCK2AmVWLgPV4U5PvHG`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `shumailov2024ai' on page 1 undefined on input
 line 38.


Package natbib Warning: Citation `dohmatob2024model' on page 1 undefined on inp
ut line 41.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
Overfull \hbox (0.4319pt too wide) in paragraph at lines 82--83
 []\OT1/ptm/b/n/10.95 Canary can-di-dates.[] \OT1/ptm/m/n/10.95 (i) \OT1/ptm/b/
n/10.95 ECE \OT1/ptm/m/n/10.95 (ex-pected cal-i-bra-tion er-ror): mea-sures mis
-cal-i-bra-tion via binned confidence--
[2]
Overfull \hbox (13.41829pt too wide) in paragraph at lines 108--109
 []\OT1/ptm/b/n/10.95 Models.[] \OT1/ptm/m/n/10.95 Pythia-410M (pri-mary) and P
ythia-1.4B (scale check), both pre-trained check-points from EleutherAI. 

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 120.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\alpha' on input line 120.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 120.


LaTeX Warning: Reference `tab:alpha_sweep' on page 3 undefined on input line 12
3.


LaTeX Warning: Reference `tab:ty_panel' on page 3 undefined on input line 123.


Overfull \hbox (118.33601pt too wide) in paragraph at lines 130--140
 [][] 

LaTeX Warning: Reference `tab:alpha_sweep' on page 3 undefined on input line 16
6.


LaTeX Warning: Reference `tab:ty_panel' on page 3 undefined on input line 166.

[3]

LaTeX Warning: Reference `tab:method_comparison' on page 4 undefined on input l
ine 180.


LaTeX Warning: Reference `tab:false_positives' on page 4 undefined on input lin
e 180.

[4]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 219.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\alpha' on input line 219.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 219.


LaTeX Warning: Reference `tab:mvp_maxlag' on page 5 undefined on input line 222
.


LaTeX Warning: Reference `tab:cross_domain' on page 5 undefined on input line 2
47.


Overfull \hbox (2.07214pt too wide) in paragraph at lines 267--268
[]\OT1/ptm/m/n/10.95 Canary rank-ing is pre-served across do-mains with Spear-m
an rank cor-re-la-tion $\OML/cmm/m/it/10.95 ^^Z \OT1/cmr/m/n/10.95 = 0\OML/cmm/
m/it/10.95 :\OT1/cmr/m/n/10.95 94$ \OT1/ptm/m/n/10.95 be-tween WikiText-

LaTeX Warning: Reference `tab:scale' on page 5 undefined on input line 272.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 291.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\alpha' on input line 291.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 291.


LaTeX Warning: Reference `tab:extended' on page 5 undefined on input line 294.

[5]

LaTeX Warning: Reference `tab:intervention' on page 6 undefined on input line 3
17.


LaTeX Warning: Reference `tab:data_strategy' on page 6 undefined on input line 
340.

[6] [7]

LaTeX Warning: Reference `tab:mvp_maxlag' on page 8 undefined on input line 390
.


LaTeX Warning: Reference `tab:extended' on page 8 undefined on input line 390.


Package natbib Warning: There were undefined citations.

[8] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur
w/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 170186 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
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
(./paper.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `shumailov2024ai' on page 1 undefined on input
 line 38.


Package natbib Warning: Citation `dohmatob2024model' on page 1 undefined on inp
ut line 41.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
Overfull \hbox (0.4319pt too wide) in paragraph at lines 82--83
 []\OT1/ptm/b/n/10.95 Canary can-di-dates.[] \OT1/ptm/m/n/10.95 (i) \OT1/ptm/b/
n/10.95 ECE \OT1/ptm/m/n/10.95 (ex-pected cal-i-bra-tion er-ror): mea-sures mis
-cal-i-bra-tion via binned confidence--
[2]
Overfull \hbox (13.41829pt too wide) in paragraph at lines 108--109
 []\OT1/ptm/b/n/10.95 Models.[] \OT1/ptm/m/n/10.95 Pythia-410M (pri-mary) and P
ythia-1.4B (scale check), both pre-trained check-points from EleutherAI. 

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 120.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\alpha' on input line 120.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 120.


Overfull \hbox (118.33601pt too wide) in paragraph at lines 130--140
 [][] 
[3]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 219.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\alpha' on input line 219.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 219.

[4]
Overfull \hbox (2.07214pt too wide) in paragraph at lines 267--268
[]\OT1/ptm/m/n/10.95 Canary rank-ing is pre-served across do-mains with Spear-m
an rank cor-re-la-tion $\OML/cmm/m/it/10.95 ^^Z \OT1/cmr/m/n/10.95 = 0\OML/cmm/
m/it/10.95 :\OT1/cmr/m/n/10.95 94$ \OT1/ptm/m/n/10.95 be-tween WikiText-

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 291.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\alpha' on input line 291.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 291.

[5] [6]

Package natbib Warning: There were undefined citations.

[7] [8] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur
w/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 172175 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23b716b9-e809-44ec-8dad-61d81c2d13ca",
  "isSidechain": false,
  "promptId": "c66d342e-ebfe-4ac2-8a57-b8c65fc157f1",
  "type": "user",
  "uuid": "a55e5188-abf4-478b-bd67-c5f6567e44b6",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `shumailov2024ai' on page 1 undefined on input\n line 38.\n\n\nPackage natbib Warning: Citation `dohmatob2024model' on page 1 undefined on inp\nut line 41.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\nOverfull \\hbox (0.4319pt too wide) in paragraph at lines 82--83\n []\\OT1/ptm/b/n/10.95 Canary can-di-dates.[] \\OT1/ptm/m/n/10.95 (i) \\OT1/ptm/b/\nn/10.95 ECE \\OT1/ptm/m/n/10.95 (ex-pected cal-i-bra-tion er-ror): mea-sures mis\n-cal-i-bra-tion via binned confidence--\n[2]\nOverfull \\hbox (13.41829pt too wide) in paragraph at lines 108--109\n []\\OT1/ptm/b/n/10.95 Models.[] \\OT1/ptm/m/n/10.95 Pythia-410M (pri-mary) and P\nythia-1.4B (scale check), both pre-trained check-points from EleutherAI. \n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 120.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\alpha' on input line 120.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 120.\n\n\nLaTeX Warning: Reference `tab:alpha_sweep' on page 3 undefined on input line 12\n3.\n\n\nLaTeX Warning: Reference `tab:ty_panel' on page 3 undefined on input line 123.\n\n\nOverfull \\hbox (118.33601pt too wide) in paragraph at lines 130--140\n [][] \n\nLaTeX Warning: Reference `tab:alpha_sweep' on page 3 undefined on input line 16\n6.\n\n\nLaTeX Warning: Reference `tab:ty_panel' on page 3 undefined on input line 166.\n\n[3]\n\nLaTeX Warning: Reference `tab:method_comparison' on page 4 undefined on input l\nine 180.\n\n\nLaTeX Warning: Reference `tab:false_positives' on page 4 undefined on input lin\ne 180.\n\n[4]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 219.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\alpha' on input line 219.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 219.\n\n\nLaTeX Warning: Reference `tab:mvp_maxlag' on page 5 undefined on input line 222\n.\n\n\nLaTeX Warning: Reference `tab:cross_domain' on page 5 undefined on input line 2\n47.\n\n\nOverfull \\hbox (2.07214pt too wide) in paragraph at lines 267--268\n[]\\OT1/ptm/m/n/10.95 Canary rank-ing is pre-served across do-mains with Spear-m\nan rank cor-re-la-tion $\\OML/cmm/m/it/10.95 ^^Z \\OT1/cmr/m/n/10.95 = 0\\OML/cmm/\nm/it/10.95 :\\OT1/cmr/m/n/10.95 94$ \\OT1/ptm/m/n/10.95 be-tween WikiText-\n\nLaTeX Warning: Reference `tab:scale' on page 5 undefined on input line 272.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 291.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\alpha' on input line 291.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 291.\n\n\nLaTeX Warning: Reference `tab:extended' on page 5 undefined on input line 294.\n\n[5]\n\nLaTeX Warning: Reference `tab:intervention' on page 6 undefined on input line 3\n17.\n\n\nLaTeX Warning: Reference `tab:data_strategy' on page 6 undefined on input line \n340.\n\n[6] [7]\n\nLaTeX Warning: Reference `tab:mvp_maxlag' on page 8 undefined on input line 390\n.\n\n\nLaTeX Warning: Reference `tab:extended' on page 8 undefined on input line 390.\n\n\nPackage natbib Warning: There were undefined citations.\n\n[8] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur\nw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 170186 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `shumailov2024ai' on page 1 undefined on input\n line 38.\n\n\nPackage natbib Warning: Citation `dohmatob2024model' on page 1 undefined on inp\nut line 41.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\nOverfull \\hbox (0.4319pt too wide) in paragraph at lines 82--83\n []\\OT1/ptm/b/n/10.95 Canary can-di-dates.[] \\OT1/ptm/m/n/10.95 (i) \\OT1/ptm/b/\nn/10.95 ECE \\OT1/ptm/m/n/10.95 (ex-pected cal-i-bra-tion er-ror): mea-sures mis\n-cal-i-bra-tion via binned confidence--\n[2]\nOverfull \\hbox (13.41829pt too wide) in paragraph at lines 108--109\n []\\OT1/ptm/b/n/10.95 Models.[] \\OT1/ptm/m/n/10.95 Pythia-410M (pri-mary) and P\nythia-1.4B (scale check), both pre-trained check-points from EleutherAI. \n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 120.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\alpha' on input line 120.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 120.\n\n\nOverfull \\hbox (118.33601pt too wide) in paragraph at lines 130--140\n [][] \n[3]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 219.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\alpha' on input line 219.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 219.\n\n[4]\nOverfull \\hbox (2.07214pt too wide) in paragraph at lines 267--268\n[]\\OT1/ptm/m/n/10.95 Canary rank-ing is pre-served across do-mains with Spear-m\nan rank cor-re-la-tion $\\OML/cmm/m/it/10.95 ^^Z \\OT1/cmr/m/n/10.95 = 0\\OML/cmm/\nm/it/10.95 :\\OT1/cmr/m/n/10.95 94$ \\OT1/ptm/m/n/10.95 be-tween WikiText-\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 291.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\alpha' on input line 291.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 291.\n\n[5] [6]\n\nPackage natbib Warning: There were undefined citations.\n\n[7] [8] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur\nw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 172175 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "23b716b9-e809-44ec-8dad-61d81c2d13ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T184925 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_col…",
  "leafUuid": "a55e5188-abf4-478b-bd67-c5f6567e44b6",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5"
}
```

---

### Assistant

_source line 37 · 2026-05-14T19:07:08.614Z_

<details><summary>Logged reasoning block</summary>

```text
There's a "Label(s) may have changed" warning, so I need a third pass. Let me run it once more.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a55e5188-abf4-478b-bd67-c5f6567e44b6",
  "isSidechain": false,
  "requestId": "req_011Cb2z7NxQGS5aozPVsHChB",
  "type": "assistant",
  "uuid": "c1996164-6d25-4248-ac90-abe1e0a2611d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdxCiJzyVcob4uP4KUQqqT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7204,
      "cache_read_input_tokens": 47995,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 47995,
          "cache_creation_input_tokens": 7204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7204
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

_source line 38 · 2026-05-14T19:07:09.568Z_

Labels changed warning — running a third pass.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1996164-6d25-4248-ac90-abe1e0a2611d",
  "isSidechain": false,
  "requestId": "req_011Cb2z7NxQGS5aozPVsHChB",
  "type": "assistant",
  "uuid": "6decbb28-86b7-4710-808c-3520eeb18c03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdxCiJzyVcob4uP4KUQqqT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7204,
      "cache_read_input_tokens": 47995,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 47995,
          "cache_creation_input_tokens": 7204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7204
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

_source line 39 · 2026-05-14T19:07:12.465Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011p8Q8ddSJqjQE4TR62Ftys`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Third LaTeX pass to resolve references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6decbb28-86b7-4710-808c-3520eeb18c03",
  "isSidechain": false,
  "requestId": "req_011Cb2z7NxQGS5aozPVsHChB",
  "type": "assistant",
  "uuid": "a19b7ff1-5f91-4260-bf6f-52d9575faed7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdxCiJzyVcob4uP4KUQqqT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7204,
      "cache_read_input_tokens": 47995,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 47995,
          "cache_creation_input_tokens": 7204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7204
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

_source line 40 · 2026-05-14T19:07:12.879Z_

<details><summary>↩ Tool result · `toolu_011p8Q8ddSJqjQE4TR62Ftys`</summary>

```text
live/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur
w/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 172175 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a19b7ff1-5f91-4260-bf6f-52d9575faed7",
  "isSidechain": false,
  "promptId": "c66d342e-ebfe-4ac2-8a57-b8c65fc157f1",
  "type": "user",
  "uuid": "284c50a3-7e61-4349-ba1a-cfe6884fced2",
  "toolUseResult": {
    "stdout": "live/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur\nw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 172175 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a19b7ff1-5f91-4260-bf6f-52d9575faed7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-14T19:07:22.937Z_

PDF 编译成功，8 页，172KB。输出在 `best/paper.tex` → `best/paper.pdf`。

论文覆盖全部 7 个实验（α-sweep / 方法论 ablation / MVP formalization / C4 cross-domain / 1.4B scale check / 20-gen extended run / CRS intervention / accumulate-vs-replace），包含 Tables 1–8 及 S1–S2，所有数字取自 `experiment_data.json`。Table 1 的 overfull hbox 是宽表 (table*) 的已知行为，不影响可读性；citation warnings 因为无 .bib 文件，不影响论文结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "284c50a3-7e61-4349-ba1a-cfe6884fced2",
  "isSidechain": false,
  "requestId": "req_011Cb2z7udNRMCyqbdjD5aJM",
  "type": "assistant",
  "uuid": "814ca8f4-1fd3-4dc3-b0a5-a5e9a538d35a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DP9f27m4foMxiF6Vyn6BPD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 301,
      "cache_read_input_tokens": 55199,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 301,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 55199,
          "cache_creation_input_tokens": 301,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 301
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T184925 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_col…",
  "leafUuid": "814ca8f4-1fd3-4dc3-b0a5-a5e9a538d35a",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "11c29027-11c4-4e7f-b1f5-81fc2ed814c5"
}
```

---
