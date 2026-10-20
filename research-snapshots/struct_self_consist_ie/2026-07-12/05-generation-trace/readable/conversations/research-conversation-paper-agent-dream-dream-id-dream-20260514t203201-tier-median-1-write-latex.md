# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T203201 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/2fee5174-c44d-4785-afcc-2a04a2955257.jsonl`
- **Structured JSON:** [`64c6dd8c2d391169c071.json`](../../sessions/64/64c6dd8c2d391169c071.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T21:07:06.997Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T21:07:06.997Z",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T203201 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Claim 1 从 'novel signals' 调整为 'systematic empirical comparison'——贡献在 taxonomy 而非 individual signal。 Claim 2 需补充 concrete practical guidance（decision flowchart：何时用 voting/SJ/logprob）以回应 'so what'。 Claim 3 从 'diagnostic framework' 弱化为 'empirical analysis'。 增加 applicability 讨论：closed-source API 场景（无 logprob）中 structural signals 的独特价值。Target Findings。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T21:07:07.009Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T21:07:07.009Z",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-14T21:07:07.070Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T203201 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Claim 1 从 'novel signals' 调整为 'systematic empirical comparison'——贡献在 taxonomy 而非 individual signal。 Claim 2 需补充 concrete practical guidance（decision flowchart：何时用 voting/SJ/logprob）以回应 'so what'。 Claim 3 从 'diagnostic framework' 弱化为 'empirical analysis'。 增加 applicability 讨论：closed-source API 场景（无 logprob）中 structural signals 的独特价值。Target Findings。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "23021a69-dda5-4b12-987b-ef4578d19bc0",
  "type": "user",
  "uuid": "528ed2ae-76c0-4258-aee4-16f51b5bffc6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T21:07:07.067Z_

```json
{
  "parentUuid": "528ed2ae-76c0-4258-aee4-16f51b5bffc6",
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
  "uuid": "314ed023-0721-475d-bd26-14ebe4fb660c",
  "timestamp": "2026-05-14T21:07:07.067Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T21:07:07.067Z_

```json
{
  "parentUuid": "314ed023-0721-475d-bd26-14ebe4fb660c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9c88f7dd-3332-45f2-9631-40a84afb72ab",
  "timestamp": "2026-05-14T21:07:07.067Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
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
  "aiTitle": "Generate median-tier research paper for dream_20260514T203201",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257"
}
```

---

### Assistant

_source line 7 · 2026-05-14T21:07:10.122Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c88f7dd-3332-45f2-9631-40a84afb72ab",
  "isSidechain": false,
  "requestId": "req_011Cb39GE1SQ52hi4dYwZq1B",
  "type": "assistant",
  "uuid": "476e8882-2ec5-4ffc-9d3c-b6cf407eb58f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQooRyPiByzYdJvWeV7doU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11202
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

_source line 8 · 2026-05-14T21:07:10.987Z_

<details open><summary>🔧 Tool call — Read · `toolu_016hjxaDS6wamgz7xDu4rk6H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "476e8882-2ec5-4ffc-9d3c-b6cf407eb58f",
  "isSidechain": false,
  "requestId": "req_011Cb39GE1SQ52hi4dYwZq1B",
  "type": "assistant",
  "uuid": "48a565c6-ba07-4f52-bf49-720188d4f9c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQooRyPiByzYdJvWeV7doU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11202
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

_source line 9 · 2026-05-14T21:07:11.259Z_

<details><summary>↩ Tool result · `toolu_016hjxaDS6wamgz7xDu4rk6H`</summary>

```text
1	[
2	  {
3	    "name": "baseline_logprob",
4	    "description": "Sequence log-probability baseline for all SciERC NER+RE samples. Make-or-break: SJ must beat logprob to justify 16x cost.",
5	    "results": {
6	      "ner_full_rho_sj": 0.357,
7	      "ner_full_rho_logprob": 0.14,
8	      "ner_full_auroc_sj": 0.689,
9	      "ner_full_auroc_logprob": 0.591,
10	      "ner_sj_vs_logprob_delta_rho": 0.217,
11	      "re_full_rho_sj": 0.211,
12	      "re_full_rho_logprob": 0.247,
13	      "re_cond_rho_sj": 0.368,
14	      "re_cond_rho_logprob": 0.146,
15	      "re_cond_sj_vs_logprob_delta_rho": 0.222,
16	      "ner_n": 529,
17	      "re_n": 397,
18	      "re_cond_n": 296
19	    },
20	    "tables": [
21	      {
22	        "name": "Table 2: 5-Signal Quality Estimation Comparison (SciERC, N=8)",
23	        "columns": [
24	          "Signal",
25	          "NER ρ",
26	          "NER AUROC",
27	          "RE full ρ",
28	          "RE cond ρ"
29	        ],
30	        "rows": [
31	          [
32	            "voting_conf",
33	            "0.502",
34	            "0.728",
35	            "0.422",
36	            "0.463"
37	          ],
38	          [
39	            "SJ",
40	            "0.357",
41	            "0.666",
42	            "0.211",
43	            "0.368"
44	          ],
45	          [
46	            "FK",
47	            "0.265",
48	            "0.624",
49	            "0.253",
50	            "0.317"
51	          ],
52	          [
53	            "EM",
54	            "0.257",
55	            "0.623",
56	            "0.100",
57	            "0.361"
58	          ],
59	          [
60	            "logprob",
61	            "0.140",
62	            "0.559",
63	            "0.247",
64	            "0.146"
65	          ]
66	        ]
67	      }
68	    ],
69	    "figures": [],
70	    "analysis": "Median 档 reviewer 的典型反应：'The logprob result on NER is expected — for structured outputs, token-level log-probability doesn't capture set-level quality. This is not surprising.'  这直接命中核心假设 #1（novelty 受质疑）。但 SJ vs logprob delta 达到 0.217，数值上足够 striking 避免被完全 dismiss。RE full set 上 logprob 略胜的事实会被标记为 W1。\n\n\nNER 上 SJ 大幅碾压 logprob（ρ +0.217），为 Claim 1 提供坚实支撑。但 RE full set 上 logprob 略领先 SJ（0.247 vs 0.211），这一点在 median 档被 reviewer 抓住：'SJ superiority is task-dependent, not universal'。RE cond set 挽回（SJ ρ=0.368 >> logprob 0.146），但 reviewer 会质疑 conditional filtering 是否 cherry-pick。整体看 SJ 的独特价值得到确认（NER + RE cond），但 RE full 的弱势给 median 档 reviewer 留下 'mixed evidence' 的印象。Logprob 在 RE full 上竞争力强 暗示对于 compound error 场景 per-sample signal 有优势，这恰好支撑了 Claim 2 的 correlation-selection gap。\n"
71	  },
72	  {
73	    "name": "baseline_exact_match",
74	    "description": "Exact-match voting rate as Wang et al. 2023 self-consistency baseline.",
75	    "results": {
76	      "ner_full_rho": 0.294,
77	      "ner_full_auroc": 0.64,
78	      "re_full_rho": 0.156,
79	      "re_full_auroc": 0.586
80	    },
81	    "tables": [],
82	    "figures": [],
83	    "analysis": "EM 作为最直接的 self-consistency 迁移失败，证明 structured outputs 需要更精细的比较。 但 median reviewer 不会给这个发现太多 credit——它太 intuitive。\n\n\nEM 处于 SJ 和 FK 之间（NER ρ=0.294），在 RE 上最弱（ρ=0.156）。这符合预期：exact match 对 structured outputs 过于粗粒度，一个 entity span 差异即判定为 mismatch。Median 档 reviewer 认为这是 'correct but unsurprising baseline'——Wang et al. 的 self-consistency 在 structured prediction 上不 work 是 intuitive 的。EM 的弱势反而支撑了引入 SJ 的动机， 但 reviewer 会指出这个动机本身不够 novel（'expected for structured outputs'）。\n"
84	  },
85	  {
86	    "name": "baseline_entity_voting",
87	    "description": "Entity-level majority voting confidence and selection.",
88	    "results": {
89	      "ner_full_rho": 0.392,
90	      "ner_full_auroc": 0.704,
91	      "re_full_rho": 0.34,
92	      "re_full_auroc": 0.667,
93	      "ner_voting_f1": 0.625,
94	      "ner_greedy_f1": 0.648,
95	      "re_voting_f1": 0.358,
96	      "re_greedy_f1": 0.402
97	    },
98	    "tables": [],
99	    "figures": [],
100	    "analysis": "Voting 的出现实际上帮助了论文：它扩大了 structural consistency family 的覆盖面， 同时 voting-as-selection 的失败成为 Claim 2 的证据。Median reviewer 接受这个 framing 但可能仍嫌 '两个信号讲一个故事' 的贡献不够 novel。\n\n\nVoting confidence 在 NER 上 beats SJ（ρ 0.392 vs 0.383），在 RE 上也领先（0.340 vs 0.244）。 这对论文叙事产生压力：如果一个更简单的 entity-level voting 就够了，SJ 的价值在哪？ Median 档 reviewer 的 R3b 质疑被触发。但 voting 作为 selection strategy 输给 greedy （NER 0.625 < 0.648），强化了 Claim 2 的 correlation-selection gap 叙事。 论文需要将 voting 和 SJ 定位为 'structural consistency family 的两个互补成员'： voting 简单高效是实用默认，SJ 可推广到任意 structured output 且温度鲁棒（Δρ=±0.01）。\n"
101	  },
102	  {
103	    "name": "evaluation_metrics_expansion",
104	    "description": "Unified 5-signal evaluation: ρ, τ, AUROC, leave-one-out SJ on all datasets.",
105	    "results": {
106	      "ner_voting_rho_full": 0.502,
107	      "ner_voting_auroc": 0.728,
108	      "ner_sj_rho_full": 0.357,
109	      "ner_sj_auroc": 0.666,
110	      "ner_logprob_auroc": 0.559,
111	      "re_voting_rho_full": 0.422,
112	      "re_voting_auroc": 0.716,
113	      "re_sj_auroc": 0.582,
114	      "re_logprob_auroc": 0.635,
115	      "focal_auroc_gap_ner": 0.107,
116	      "focal_auroc_gap_re": -0.053,
117	      "loo_sj_max_delta_rho": 0.000305
118	    },
119	    "tables": [
120	      {
121	        "name": "Table 1: Unified Quality Estimation (SciERC, N=8, T=1.0)",
122	        "columns": [
123	          "Signal",
124	          "NER ρ",
125	          "NER τ",
126	          "NER AUROC",
127	          "RE ρ",
128	          "RE τ",
129	          "RE AUROC"
130	        ],
131	        "rows": [
132	          [
133	            "voting_conf",
134	            "0.502",
135	            "0.377",
136	            "0.728",
137	            "0.422",
138	            "0.327",
139	            "0.716"
140	          ],
141	          [
142	            "SJ",
143	            "0.357",
144	            "0.266",
145	            "0.666",
146	            "0.211",
147	            "0.162",
148	            "0.582"
149	          ],
150	          [
151	            "FK",
152	            "0.265",
153	            "0.203",
154	            "0.624",
155	            "0.253",
156	            "0.197",
157	            "0.631"
158	          ],
159	          [
160	            "EM",
161	            "0.257",
162	            "0.192",
163	            "0.623",
164	            "0.100",
165	            "0.084",
166	            "0.504"
167	          ],
168	          [
169	            "logprob",
170	            "0.140",
171	            "0.101",
172	            "0.559",
173	            "0.247",
174	            "0.181",
175	            "0.635"
176	          ]
177	        ]
178	      }
179	    ],
180	    "figures": [],
181	    "analysis": "Unified evaluation 是论文 soundness 的基石。Median reviewer 给 soundness 3.5/5 因为方法论正确但 RE 数据不支持 universal claim。\n\n\nUnified evaluation 使 NER 上 structural vs logprob 的 AUROC gap 达到 0.107（voting 0.728 vs logprob 0.559）， 落在 median 档 focal_auroc_gap 范围 [0.05, 0.10] 的上沿。这是论文最强的数字之一。 但 RE full 上 SJ AUROC（0.582）低于 logprob（0.635），gap 为负。Median reviewer 会用这个数据点 argue 'signal superiority is dataset/task-dependent'。 Leave-one-out SJ 无循环性（max Δρ=0.0003），解决了 R9 circularity concern， reviewer 会 acknowledge 这个 robustness check。τ 与 ρ 方向一致增强了 soundness。 整体 perceived_soundness 在 [3.0, 4.0] 范围——方法论扎实但结论受 RE 数据限制。\n"
182	  },
183	  {
184	    "name": "ner_conll2003",
185	    "description": "Qwen3-8B on CoNLL-2003 NER. Cross-dataset generalization.",
186	    "results": {
187	      "sj_rho_full": 0.436,
188	      "sj_auroc_full": 0.801,
189	      "fk_rho_full": 0.4,
190	      "logprob_rho_full": 0.316,
191	      "em_rho_full": 0.451,
192	      "ev_rho_full": 0.424,
193	      "greedy_f1": 0.912,
194	      "oracle_f1": 0.954,
195	      "oracle_headroom": 0.042,
196	      "sj_vs_logprob_delta_rho": 0.12,
197	      "n_valid": 2756
198	    },
199	    "tables": [
200	      {
201	        "name": "Table 3: Cross-Dataset Quality Estimation (CoNLL-2003 NER)",
202	        "columns": [
203	          "Signal",
204	          "ρ",
205	          "τ",
206	          "AUROC"
207	        ],
208	        "rows": [
209	          [
210	            "EM",
211	            "0.451",
212	            "0.400",
213	            "0.816"
214	          ],
215	          [
216	            "SJ",
217	            "0.436",
218	            "0.385",
219	            "0.801"
220	          ],
221	          [
222	            "voting_conf",
223	            "0.424",
224	            "0.378",
225	            "0.789"
226	          ],
227	          [
228	            "FK",
229	            "0.400",
230	            "0.357",
231	            "0.774"
232	          ],
233	          [
234	            "logprob",
235	            "0.316",
236	            "0.247",
237	            "0.753"
238	          ]
239	        ]
240	      }
241	    ],
242	    "figures": [],
243	    "analysis": "CoNLL 数据 confirms structural > logprob cross-dataset，但 EM 抢占 SJ 位置 使 'SJ is best' 的 claim 需要 nuance。论文必须 argue SJ generalizability 而非 SJ dominance。\n\n\nCoNLL 上 SJ ρ=0.436 高于 SciERC（0.357），因为 CoNLL 是简单 flat NER 任务， 模型 greedy F1 已达 0.912，consistency signal 更 reliable。SJ AUROC 0.801 是全实验最高值之一。 但 oracle headroom 仅 0.042（vs SciERC 0.108），意味着 best-of-N selection 的实用价值很小。 Median reviewer 接受 cross-dataset generalization 但注意到：(a) CoNLL 太容易，consistency 高是 trivial 的；(b) headroom 小说明 TTS 本身无意义。这强化了 'quality estimation, not selection' 的 framing 但也让 reviewer 问 'if the model is already 91% F1, who needs confidence estimation?'。 EM 在 CoNLL 上意外地最强（ρ=0.451），因为高准确率下 exact match 率足够区分 easy/hard。\n"
244	  },
245	  {
246	    "name": "ner_wnut17",
247	    "description": "WNUT-17 social media NER. Abandoned due to 54% F1=0.",
248	    "results": {
249	      "sj_rho_full": 0.082,
250	      "fk_rho_full": 0.124,
251	      "logprob_rho_full": -0.414,
252	      "sample_f1_pct_zero": 53.7,
253	      "n_instances": 1287,
254	      "verdict": "FAIL"
255	    },
256	    "tables": [],
257	    "figures": [],
258	    "analysis": "WNUT failure 不进入 main results 但作为 Claim 3 的 negative evidence 在 Discussion 中简述。 Median reviewer 不会因此 reject 但会在 scope concern 中引用。\n\n\nWNUT 失败是 median 档的重要 data point。54% 的 sample F1=0 意味着模型在 social media domain 能力不足——consistency signal 在模型 systematically 失败时无意义。这既是 Claim 3（task-complexity boundary）的证据，也是 limitation：论文无法 claim generalization 到 noisy/informal text。Median reviewer 看到 WNUT 被 orphaned 会标记为 'only tested on well-structured text domains'（R1 concern）。论文选择不报告 WNUT 在 Limitations 中 acknowledge，reviewer 认为 honest 但仍视为 scope 不足。Logprob 出现负相关（ρ=-0.414） 是因为模型对 noisy text 过度自信——生成流畅但错误的 output 有高 logprob。\n"
259	  },
260	  {
261	    "name": "ner_multi_model",
262	    "description": "LLaMA-3.1-8B on SciERC. Model-agnostic validation.",
263	    "results": {
264	      "ner_rho_sj": 0.363,
265	      "ner_rho_fk": 0.327,
266	      "ner_rho_logprob": 0.183,
267	      "ner_sj_beats_surface": true,
268	      "re_rho_sj": 0.299,
269	      "re_rho_logprob": 0.288,
270	      "re_sj_cond": 0.405,
271	      "re_logprob_cond": 0.092,
272	      "re_sample_f1_pct_zero": 41.2
273	    },
274	    "tables": [
275	      {
276	        "name": "Table 4: Cross-Model Validation (LLaMA-3.1-8B, SciERC)",
277	        "columns": [
278	          "Subtask",
279	          "Signal",
280	          "ρ full",
281	          "ρ cond",
282	          "AUROC"
283	        ],
284	        "rows": [
285	          [
286	            "NER",
287	            "SJ",
288	            "0.363",
289	            "0.311",
290	            "—"
291	          ],
292	          [
293	            "NER",
294	            "logprob",
295	            "0.183",
296	            "0.109",
297	            "—"
298	          ],
299	          [
300	            "RE",
301	            "SJ",
302	            "0.299",
303	            "0.405",
304	            "—"
305	          ],
306	          [
307	            "RE",
308	            "logprob",
309	            "0.288",
310	            "0.092",
311	            "—"
312	          ]
313	        ]
314	      }
315	    ],
316	    "figures": [],
317	    "analysis": "Cross-model evidence 足够支撑 'model-agnostic' 在 softened form 下通过 review， 但 median reviewer 会在 major weakness 中写 'limited to 8B parameter scale'。\n\n\nLLaMA NER 上 SJ（0.363）> logprob（0.183），structural > surface 一致成立， 支撑 model-agnostic claim。但 RE full set 上 SJ（0.299）仅微弱领先 logprob（0.288）， 且均 < 0.30。RE cond 上 SJ 大幅反弹（0.405），但 41.2% 的 RE sample F1=0  表明 LLaMA 在 SciERC RE 上同样面临 capability gap。 Median reviewer 接受 2-model validation 但指出：'Both 8B models show similar patterns. A 70B model or a fundamentally different architecture would strengthen the generalization claim.' 这触发 R14（cross-model validation thin），但不致命——reviewer 视为 P1 而非 P0 concern， 因为 2×8B across 2 architectures（Qwen/LLaMA）至少排除了 model-specific artifact。\n"
318	  },
319	  {
320	    "name": "ner_llama_conll",
321	    "description": "LLaMA-3.1-8B on CoNLL-2003 for 2×2 matrix completion.",
322	    "results": {
323	      "sj_rho_full": 0.431,
324	      "fk_rho_full": 0.428,
325	      "logprob_rho_full": 0.307,
326	      "voting_conf_rho_full": 0.426,
327	      "sj_auroc_full": 0.704,
328	      "logprob_auroc_full": 0.761,
329	      "greedy_f1": 0.927,
330	      "n_valid": 2756
331	    },
332	    "tables": [
333	      {
334	        "name": "Table 5: 2×2 Cross-Validation Matrix (NER ρ full)",
335	        "columns": [
336	          "",
337	          "SciERC",
338	          "CoNLL-2003"
339	        ],
340	        "rows": [
341	          [
342	            "Qwen3-8B",
343	            "0.357 (SJ) / 0.140 (lp)",
344	            "0.436 (SJ) / 0.316 (lp)"
345	          ],
346	          [
347	            "LLaMA-3.1-8B",
348	            "0.363 (SJ) / 0.183 (lp)",
349	            "0.431 (SJ) / 0.307 (lp)"
350	          ]
351	        ]
352	      }
353	    ],
354	    "figures": [],
355	    "analysis": "2×2 矩阵是 reviewer R1+R2 的核心回应。4/4 configurations 上 structural ρ > logprob ρ。 Median reviewer 认可但注意到都是 8B 规模和 well-structured text，scope concern 不消。\n\n\nLLaMA×CoNLL 完成 2×2 矩阵（Qwen×LLaMA × SciERC×CoNLL）。SJ ρ=0.431 与 Qwen×CoNLL 的 0.436 高度一致，证明 cross-model consistency。这是论文 generalization 最强论据。 但 AUROC 上 logprob（0.761）反超 SJ（0.704）——CoNLL 高准确率场景下 logprob 的 discriminative power 更强。Median reviewer 注意到 AUROC ranking 与 ρ ranking 不一致 （SJ wins ρ, logprob wins AUROC on CoNLL），这会引发 'which metric matters more?' 的讨论。 论文需要 argue ρ 更 informative 因为它测量 monotonic ordering 而非 binary discrimination。 cross_config_ner_structural_gt_logprob_rate 在 ρ 上为 4/4（100%），在 AUROC 上为 2/4（50%）， 落在 median 档 [0.8, 1.0] 的边缘——取决于论文主推哪个 metric。\n"
356	  },
357	  {
358	    "name": "ner_n16_scierc",
359	    "description": "N=16 with 3-seed robustness on SciERC.",
360	    "results": {
361	      "ner_sj_rho_mean_3seed": 0.412,
362	      "ner_sj_rho_sd_3seed": 0.025,
363	      "ner_voting_conf_rho_s42": 0.399,
364	      "ner_sj_rho_s42": 0.398,
365	      "re_sj_rho_s42": 0.277,
366	      "re_voting_conf_rho_s42": 0.38,
367	      "re_full_verdict": "FAIL"
368	    },
369	    "tables": [
370	      {
371	        "name": "Table 6: N-Scaling & Seed Robustness (SciERC)",
372	        "columns": [
373	          "Config",
374	          "NER SJ ρ",
375	          "RE SJ ρ",
376	          "NER AUROC",
377	          "RE AUROC"
378	        ],
379	        "rows": [
380	          [
381	            "N=8, s42",
382	            "0.383",
383	            "0.244",
384	            "0.689",
385	            "0.592"
386	          ],
387	          [
388	            "N=16, s42",
389	            "0.398",
390	            "0.277",
391	            "0.697",
392	            "—"
393	          ],
394	          [
395	            "N=16, s123",
396	            "0.423",
397	            "0.267",
398	            "—",
399	            "—"
400	          ],
401	          [
402	            "N=16, s456",
403	            "0.414",
404	            "0.268",
405	            "—",
406	            "—"
407	          ],
408	          [
409	            "N=16 mean±SD",
410	            "0.412±0.025",
411	            "0.271±0.006",
412	            "—",
413	            "—"
414	          ]
415	        ]
416	      }
417	    ],
418	    "figures": [],
419	    "analysis": "Seed stability 强（SD=0.025），RE 一致地弱（3 seed 均 < 0.28）。 Median reviewer：'The authors appropriately report multi-seed results. RE weakness  is a real limitation, not a statistical artifact.'\n\n\n3-seed NER SJ ρ 均值 0.412（SD=0.025），稳定性良好。N=16 vs N=8 在 NER 上 marginal improvement（0.412 vs 0.357），说明 N=8 已接近饱和。RE full set SJ ρ=0.277  仍远低于 0.40 阈值，N=16 未能挽救 RE。这是 median 档的关键数据： reviewer 看到 RE rho < 0.30 会 argue 'consistency signals fundamentally limited for  relational tasks'，将 Claim 1 的适用范围限制在 NER。论文通过 conditional analysis 部分挽回（RE cond SJ ρ~0.37-0.40），但这只占 2/3 的实例。 3-seed 稳定性是正面信号——soundness 得分因此在 3.5 左右而非更低。\n"
420	  },
421	  {
422	    "name": "adaptive_compute_demo",
423	    "description": "Best-of-N selection: all signals vs greedy vs oracle.",
424	    "results": {
425	      "ner_scierc_greedy": 0.618,
426	      "ner_scierc_sj": 0.62,
427	      "ner_scierc_logprob": 0.621,
428	      "ner_scierc_oracle": 0.787,
429	      "ner_conll_greedy": 0.725,
430	      "ner_conll_sj": 0.718,
431	      "re_greedy": 0.403,
432	      "re_logprob": 0.41,
433	      "re_sj": 0.397,
434	      "re_oracle": 0.631
435	    },
436	    "tables": [
437	      {
438	        "name": "Table 7: Best-of-N Selection F1 (SciERC, N=16)",
439	        "columns": [
440	          "Signal",
441	          "NER F1",
442	          "Δ vs greedy",
443	          "RE F1",
444	          "Δ vs greedy"
445	        ],
446	        "rows": [
447	          [
448	            "greedy",
449	            "0.618",
450	            "—",
451	            "0.403",
452	            "—"
453	          ],
454	          [
455	            "logprob",
456	            "0.621",
457	            "+0.003",
458	            "0.410",
459	            "+0.007"
460	          ],
461	          [
462	            "SJ",
463	            "0.620",
464	            "+0.002",
465	            "0.397",
466	            "−0.006"
467	          ],
468	          [
469	            "FK",
470	            "0.621",
471	            "+0.003",
472	            "0.396",
473	            "−0.007"
474	          ],
475	          [
476	            "voting_conf",
477	            "0.585",
478	            "−0.033",
479	            "0.408",
480	            "+0.005"
481	          ],
482	          [
483	            "random",
484	            "0.586",
485	            "−0.032",
486	            "0.364",
487	            "−0.039"
488	          ],
489	          [
490	            "oracle",
491	            "0.787",
492	            "+0.169",
493	            "0.631",
494	            "+0.228"
495	          ]
496	        ]
497	      }
498	    ],
499	    "figures": [],
500	    "analysis": "Selection curves figure 是论文最重要的 visualization——它让 correlation-selection gap  一目了然。Median reviewer 评价 Claim 2 为 'interesting observation but unclear practical impact' （核心假设 #2）。需要 actionable guidance 回应 'so what'。\n\n\nNER best-of-N：所有信号 ≤ greedy（SJ 0.620 ≈ greedy 0.618，差异 statistically insignificant）， oracle headroom +16.9pp 完全无法 exploit。这是 Claim 2 的核心负面发现。 RE：仅 logprob（0.410）beat greedy（0.403，+0.7pp），SJ（0.397）反而略低于 greedy。 Median reviewer 的反应两极：一方面 'negative result is interesting and honest'， 另一方面 'if your signals can't improve anything, what's the practical value?'。 NER selection 全面失败在 median 档被至少 1 位 reviewer 视为 significant limitation（核心假设 #6）。 论文必须 pivot 叙事：'These results reveal a fundamental gap between quality estimation  (knowing which INPUTS are reliable) and sample selection (choosing which OUTPUT is best).' Oracle gap 的存在（NER +16pp, RE +23pp）说明 better signals 理论上可行——current unsupervised  signals 还不够。\n"
501	  },
502	  {
503	    "name": "signal_ensemble_analysis",
504	    "description": "SJ+logprob ensemble, linear combination grid search, logistic regression.",
505	    "results": {
506	      "sj_logprob_pearson_ner": 0.57,
507	      "sj_logprob_pearson_re": 0.42,
508	      "best_linear_ner_combo": "SJ+voting_conf α=0.3",
509	      "best_linear_ner_rho": 0.489,
510	      "best_linear_re_combo": "voting_conf+logprob α=0.6",
511	      "best_linear_re_rho": 0.429,
512	      "ensemble_ner_auroc": 0.735,
513	      "ensemble_re_auroc": 0.719,
514	      "ensemble_ner_delta_auroc": 0.035,
515	      "selection_ner_ensemble_f1": 0.604,
516	      "selection_ner_greedy_f1": 0.609,
517	      "selection_re_logprob_f1": 0.397,
518	      "selection_re_greedy_f1": 0.374
519	    },
520	    "tables": [
521	      {
522	        "name": "Table 8: Ensemble Analysis",
523	        "columns": [
524	          "Method",
525	          "NER ρ",
526	          "NER AUROC",
527	          "RE ρ",
528	          "RE AUROC"
529	        ],
530	        "rows": [
531	          [
532	            "Best single (voting_conf)",
533	            "0.502",
534	            "0.728",
535	            "0.422",
536	            "0.716"
537	          ],
538	          [
539	            "Best linear combo",
540	            "0.489",
541	            "—",
542	            "0.429",
543	            "—"
544	          ],
545	          [
546	            "Logistic regression ensemble",
547	            "—",
548	            "0.735",
549	            "—",
550	            "0.719"
551	          ],
552	          [
553	            "Oracle",
554	            "—",
555	            "—",
556	            "—",
557	            "—"
558	          ]
559	        ]
560	      }
561	    ],
562	    "figures": [],
563	    "analysis": "Ensemble 结果 resolves R11 但不改变 paper narrative。 Median reviewer 给 credit for thoroughness，不 penalize。\n\n\nEnsemble NER AUROC 0.735 比 best single 0.700 提升 +0.035——improvement 存在但 marginal。 RE ensemble AUROC 0.719 实际略低于 voting_conf 单独的 0.721，无 improvement。 SJ 和 logprob 的 Pearson 相关 0.57 说明二者 moderately correlated——它们捕获的信息 有 overlap 也有 complement。Linear combo 最佳组合是 SJ+voting（NER）和 voting+logprob（RE）， 而非 SJ+logprob——这暗示同 family 内组合（structural×structural）比跨 family 更有效。 关键 negative：ensemble 也无法 beat greedy on NER selection（0.604 < 0.609）。 Median reviewer 认为 ensemble 分析 comprehensive 但 '强化了 negative result 而非解决它'。 Effective claim count = 2（quality estimation + gap），ensemble 是 supporting evidence 不是独立 claim。\n"
564	  },
565	  {
566	    "name": "selection_curves",
567	    "description": "Best-of-N curves for N=1,2,4,8,16 across all datasets.",
568	    "results": {
569	      "scierc_ner_n16_oracle": 0.787,
570	      "scierc_ner_n16_best_signal": 0.621,
571	      "scierc_ner_n4_oracle": 0.714,
572	      "scierc_re_n16_logprob": 0.41,
573	      "scierc_re_n8_logprob": 0.413,
574	      "conll_ner_n8_sj": 0.718,
575	      "conll_ner_n8_greedy": 0.725
576	    },
577	    "tables": [],
578	    "figures": [],
579	    "analysis": "这个 figure 直接回应 R16（zero figures），是 median 档论文从 table-only 升级的关键。\n\n\nSelection curves 跨 N 值的 pattern 高度一致：NER 上所有信号 flat at greedy level， RE 上仅 logprob 微幅超越。CoNLL NER 上 N=8 所有信号（SJ 0.718）反而低于 greedy（0.725）， 因为 CoNLL 高准确率下 T=1.0 的 stochastic samples 引入 noise 而非 diversity。 Oracle 随 N 单调增长（NER: 0.714→0.787），说明 sample pool 中确实存在更好 output， 但 unsupervised signals 无法识别。这个 gap 的视觉化（Figure 1）是论文最有 impact 的贡献。 Median reviewer 认为这个 figure 比任何 table 更 convincing，但仍可能 comment  'the gap is well-documented but the authors offer no path forward'。\n"
580	  },
581	  {
582	    "name": "re_diagnostic_analysis",
583	    "description": "Per-relation-type breakdown, error propagation, threshold sensitivity, bootstrap CI.",
584	    "results": {
585	      "hyponym_rho_sj": 0.545,
586	      "feature_of_rho_sj": 0.004,
587	      "used_for_rho_sj": 0.236,
588	      "entity_span_error_pct": 55.5,
589	      "fisher_z_ner_vs_re_sj_p": 0.021,
590	      "bootstrap_ci_ner_sj": [
591	        0.295,
592	        0.459
593	      ],
594	      "bootstrap_ci_re_sj": [
595	        0.142,
596	        0.339
597	      ],
598	      "threshold_thr0_rho_sj": 0.316,
599	      "threshold_thr0_n": 313
600	    },
601	    "tables": [
602	      {
603	        "name": "Table 9: Per-Relation-Type Quality Estimation (SciERC RE)",
604	        "columns": [
605	          "Relation Type",
606	          "n",
607	          "ρ_SJ",
608	          "ρ_FK",
609	          "ρ_VC",
610	          "Mean F1"
611	        ],
612	        "rows": [
613	          [
614	            "HYPONYM-OF",
615	            "36",
616	            "0.545",
617	            "0.646",
618	            "0.628",
619	            "0.513"
620	          ],
621	          [
622	            "CONJUNCTION",
623	            "86",
624	            "0.383",
625	            "0.350",
626	            "0.484",
627	            "0.480"
628	          ],
629	          [
630	            "USED-FOR",
631	            "299",
632	            "0.236",
633	            "0.255",
634	            "0.286",
635	            "0.422"
636	          ],
637	          [
638	            "PART-OF",
639	            "44",
640	            "0.239",
641	            "0.348",
642	            "0.283",
643	            "0.297"
644	          ],
645	          [
646	            "EVALUATE-FOR",
647	            "62",
648	            "0.172",
649	            "0.255",
650	            "0.226",
651	            "0.365"
652	          ],
653	          [
654	            "COMPARE",
655	            "35",
656	            "0.168",
657	            "0.184",
658	            "0.180",
659	            "0.453"
660	          ],
661	          [
662	            "FEATURE-OF",
663	            "50",
664	            "0.004",
665	            "0.052",
666	            "0.014",
667	            "0.254"
668	          ]
669	        ]
670	      }
671	    ],
672	    "figures": [],
673	    "analysis": "Diagnostic analysis 最强贡献是 error decomposition 和 per-relation heterogeneity。 Median reviewer 接受这些但要求 soften 'diagnostic framework' → 'empirical analysis'。\n\n\nPer-relation analysis 揭示巨大异质性：HYPONYM-OF ρ_sj=0.545（接近 NER 水平）， FEATURE-OF ρ_sj=0.004（近乎零）。这种 within-task variance 比 NER-vs-RE 的 between-task 差异更有 diagnostic value。Entity span errors 占 RE FN 的 55.5%，说明 RE failure 主要是 entity 识别失败导致的 cascade——compound error propagation 实锤。 Fisher Z-test 确认 NER ρ_sj significantly > RE ρ_sj（p=0.021）。 Median reviewer 视这些为 'solid descriptive analysis' 但不是 'prescriptive framework' （R17 concern）。Bootstrap CI 显示 NER SJ 和 RE SJ 的 95% CI 有 overlap（NER [0.295, 0.459]  vs RE [0.142, 0.339]）——虽然均值差异显著但不是 dramatic separation。 Threshold sensitivity 分析显示 thr=0.00 时 ρ=0.316（n=313），thr=0.05 时 ρ 反降至 0.268（n=239）， 说明 conditional threshold 不是 monotonically beneficial——只是 F1=0 的 extreme cases 拉低了相关。\n"
674	  },
675	  {
676	    "name": "temperature_sensitivity_analysis",
677	    "description": "T=0.7 vs T=1.0 comparison for all signals.",
678	    "results": {
679	      "sj_delta_rho_t07_vs_t10": 0.01,
680	      "fk_delta_rho_t07_vs_t10": 0.06,
681	      "recommendation": "T=1.0 + conditional filtering",
682	      "re_oracle_headroom_t10": 0.167,
683	      "re_oracle_headroom_t07": 0.131,
684	      "re_diversity_1_sj_t10": 0.389,
685	      "re_diversity_1_sj_t07": 0.313
686	    },
687	    "tables": [],
688	    "figures": [],
689	    "analysis": "温度分析作为 Claim 3 的 supporting evidence，不独立贡献 novelty。 SJ 的温度鲁棒性是 reviewer 质疑 R3b 时的防御点。\n\n\nSJ 温度鲁棒性极强（Δρ=±0.01 across T=0.7/1.0），FK 受温度影响更大（Δρ=±0.06-0.09）。 这是 SJ 相对于 FK 的独特优势之一，在 R3b 的回应中有价值。 T=1.0 保留更多 oracle headroom（RE: 0.167 vs 0.131）和多样性（1-SJ: 0.389 vs 0.313）， 但 selection 上无 signal 能 exploit 这个 headroom。 Conditional filtering 的 lift（+0.07~0.14）远大于温度调优（±0.01）， 说明 '智能过滤 > 参数调优' 是一个 practical recommendation。 Median reviewer 认为温度分析 'adequate but not a standalone contribution'。\n"
690	  },
691	  {
692	    "name": "capability_stratification",
693	    "description": "Instance stratification by difficulty and independent proxies.",
694	    "results": {
695	      "ner_sj_rho_overall": 0.398,
696	      "ner_by_ent_count_0_sj_rho": 0.689,
697	      "ner_by_ent_count_3_5_sj_rho": 0.353,
698	      "re_hard_0_25_sj_rho": -0.043,
699	      "re_easy_sj_rho": 0.21,
700	      "inverted_u_confirmed": false,
701	      "proxy_independence_ner_f1_vs_slen": -0.021
702	    },
703	    "tables": [],
704	    "figures": [],
705	    "analysis": "Stratification 支撑 Claim 3 但 inverted-U 不确认意味着 'complexity boundary'  是 monotonic degradation 而非 non-linear pattern。叙事需对应调整。\n\n\nEntity count=0 时 SJ ρ=0.689（最高），因为空实例的 binary judgment 更清晰。 RE hard instances（greedy F1 < 0.25）SJ ρ=-0.043（近乎随机），证明 consistency signal 在模型 capability 之外完全失效。Inverted-U pattern 未确认——这是 honest negative  但也意味着论文不能 claim 'sweet spot' 的存在。Independent proxy（句长、entity count） 与 F1 几乎正交（r=-0.021, 0.007），验证了分层不是 circular。 Median reviewer 视为 solid analysis 但 'descriptive, not actionable'： 知道 hard instances 的 signal 弱不能帮助 practitioner 决定何时 trust。\n"
706	  },
707	  {
708	    "name": "re_n16_confirmation",
709	    "description": "RE N=16 on SciERC — test N-scaling effect on RE.",
710	    "results": {
711	      "re_rho_sj_full": 0.297,
712	      "re_rho_sj_cond": 0.398,
713	      "re_rho_logprob_full": 0.299,
714	      "re_headroom": 0.232,
715	      "ner_rho_sj_full": 0.377,
716	      "verdict": "FAIL"
717	    },
718	    "tables": [],
719	    "figures": [],
720	    "analysis": "RE N=16 的 FAIL verdict 是论文最大的 inconvenient truth。 Median reviewer：'Even with doubled compute budget, RE quality estimation remains weak.'\n\n\nN=16 对 RE 的改善 marginal：SJ ρ 从 N=8 的 0.211 升至 0.297（+0.086）， 仍远低于 0.40。Logprob 在 N=16 上 ρ=0.299 与 SJ 几乎相同——更多 samples 缩小了 SJ 和 logprob 的差距但都没超越 0.30 barrier。Headroom 扩大到 0.232， 但 signal 改善幅度远不够 exploit。Conditional set ρ_sj=0.398 接近 0.40 阈值 但仍 borderline。这确认了 RE consistency signal 的弱势不是 sample budget 问题—— 即使 N=16 也不够。早期在 200 instance subset + T=0.7 上观察到的 N-scaling 'breakthrough' 被证实是 artifact（核心假设 #5：RE ρ < 0.30 限制 claim scope）。\n"
721	  },
722	  {
723	    "name": "ner_ood_robustness",
724	    "description": "NER OOD robustness via cross-domain transfer (e.g., SciERC model on CoNLL or vice versa).",
725	    "results": {
726	      "ood_sj_rho_full": 0.15,
727	      "ood_fk_rho_full": 0.1,
728	      "ood_logprob_rho_full": -0.2,
729	      "ood_sample_f1_pct_zero": 35.0,
730	      "ood_greedy_f1": 0.45,
731	      "structural_beats_surface": true,
732	      "verdict": "MARGINAL"
733	    },
734	    "tables": [
735	      {
736	        "name": "Table (Appendix): OOD Robustness",
737	        "columns": [
738	          "Signal",
739	          "In-Domain ρ",
740	          "OOD ρ",
741	          "Δ"
742	        ],
743	        "rows": [
744	          [
745	            "SJ",
746	            "0.357",
747	            "0.15",
748	            "−0.207"
749	          ],
750	          [
751	            "FK",
752	            "0.265",
753	            "0.10",
754	            "−0.165"
755	          ],
756	          [
757	            "logprob",
758	            "0.140",
759	            "−0.20",
760	            "−0.340"
761	          ]
762	        ]
763	      }
764	    ],
765	    "figures": [],
766	    "analysis": "OOD 实验如果执行会进入 Appendix 而非 main results。Median reviewer 不太可能 要求这个实验作为 acceptance condition，但它回应了 closed-source API applicability 叙事。 实际执行风险：如果 OOD F1 太低（<0.30），consistency analysis 失去意义。 建议：如果 GPU 时间允许，仅作为 supplementary evidence，不影响 main claims。\n\nOOD 场景下模型 greedy F1 大幅下降（~0.45 vs in-domain 0.66），consistency signal  相应退化但 structural 仍优于 surface（SJ ρ~0.15 > FK ρ~0.10）。Logprob 在 OOD 下 出现负相关（ρ~-0.20），因为 domain shift 导致 logprob 与 accuracy 脱钩——模型 对 in-domain-like patterns 过度自信。这是 SJ 在 closed-source API / OOD 场景下 独特价值的支撑：即使绝对 ρ 不高，至少 direction 正确且不会 mislead。 35% F1=0 rate 类似 WNUT，说明 OOD performance 受模型 capability 限制。 Median reviewer 不会 heavily weight 这个实验（P2），但它回应了 R18（when would  consistency help?）——answer：当 logprob 不可用或不可信时。 注意：这是唯一 truly unrun 的 planned 实验，预测有更大不确定性。\n"
767	  }
768	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48a565c6-ba07-4f52-bf49-720188d4f9c6",
  "isSidechain": false,
  "promptId": "23021a69-dda5-4b12-987b-ef4578d19bc0",
  "type": "user",
  "uuid": "250ee0fe-6b3f-4283-b6e4-e0e04ad8ae24",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"baseline_logprob\",\n    \"description\": \"Sequence log-probability baseline for all SciERC NER+RE samples. Make-or-break: SJ must beat logprob to justify 16x cost.\",\n    \"results\": {\n      \"ner_full_rho_sj\": 0.357,\n      \"ner_full_rho_logprob\": 0.14,\n      \"ner_full_auroc_sj\": 0.689,\n      \"ner_full_auroc_logprob\": 0.591,\n      \"ner_sj_vs_logprob_delta_rho\": 0.217,\n      \"re_full_rho_sj\": 0.211,\n      \"re_full_rho_logprob\": 0.247,\n      \"re_cond_rho_sj\": 0.368,\n      \"re_cond_rho_logprob\": 0.146,\n      \"re_cond_sj_vs_logprob_delta_rho\": 0.222,\n      \"ner_n\": 529,\n      \"re_n\": 397,\n      \"re_cond_n\": 296\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2: 5-Signal Quality Estimation Comparison (SciERC, N=8)\",\n        \"columns\": [\n          \"Signal\",\n          \"NER ρ\",\n          \"NER AUROC\",\n          \"RE full ρ\",\n          \"RE cond ρ\"\n        ],\n        \"rows\": [\n          [\n            \"voting_conf\",\n            \"0.502\",\n            \"0.728\",\n            \"0.422\",\n            \"0.463\"\n          ],\n          [\n            \"SJ\",\n            \"0.357\",\n            \"0.666\",\n            \"0.211\",\n            \"0.368\"\n          ],\n          [\n            \"FK\",\n            \"0.265\",\n            \"0.624\",\n            \"0.253\",\n            \"0.317\"\n          ],\n          [\n            \"EM\",\n            \"0.257\",\n            \"0.623\",\n            \"0.100\",\n            \"0.361\"\n          ],\n          [\n            \"logprob\",\n            \"0.140\",\n            \"0.559\",\n            \"0.247\",\n            \"0.146\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档 reviewer 的典型反应：'The logprob result on NER is expected — for structured outputs, token-level log-probability doesn't capture set-level quality. This is not surprising.'  这直接命中核心假设 #1（novelty 受质疑）。但 SJ vs logprob delta 达到 0.217，数值上足够 striking 避免被完全 dismiss。RE full set 上 logprob 略胜的事实会被标记为 W1。\\n\\n\\nNER 上 SJ 大幅碾压 logprob（ρ +0.217），为 Claim 1 提供坚实支撑。但 RE full set 上 logprob 略领先 SJ（0.247 vs 0.211），这一点在 median 档被 reviewer 抓住：'SJ superiority is task-dependent, not universal'。RE cond set 挽回（SJ ρ=0.368 >> logprob 0.146），但 reviewer 会质疑 conditional filtering 是否 cherry-pick。整体看 SJ 的独特价值得到确认（NER + RE cond），但 RE full 的弱势给 median 档 reviewer 留下 'mixed evidence' 的印象。Logprob 在 RE full 上竞争力强 暗示对于 compound error 场景 per-sample signal 有优势，这恰好支撑了 Claim 2 的 correlation-selection gap。\\n\"\n  },\n  {\n    \"name\": \"baseline_exact_match\",\n    \"description\": \"Exact-match voting rate as Wang et al. 2023 self-consistency baseline.\",\n    \"results\": {\n      \"ner_full_rho\": 0.294,\n      \"ner_full_auroc\": 0.64,\n      \"re_full_rho\": 0.156,\n      \"re_full_auroc\": 0.586\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"EM 作为最直接的 self-consistency 迁移失败，证明 structured outputs 需要更精细的比较。 但 median reviewer 不会给这个发现太多 credit——它太 intuitive。\\n\\n\\nEM 处于 SJ 和 FK 之间（NER ρ=0.294），在 RE 上最弱（ρ=0.156）。这符合预期：exact match 对 structured outputs 过于粗粒度，一个 entity span 差异即判定为 mismatch。Median 档 reviewer 认为这是 'correct but unsurprising baseline'——Wang et al. 的 self-consistency 在 structured prediction 上不 work 是 intuitive 的。EM 的弱势反而支撑了引入 SJ 的动机， 但 reviewer 会指出这个动机本身不够 novel（'expected for structured outputs'）。\\n\"\n  },\n  {\n    \"name\": \"baseline_entity_voting\",\n    \"description\": \"Entity-level majority voting confidence and selection.\",\n    \"results\": {\n      \"ner_full_rho\": 0.392,\n      \"ner_full_auroc\": 0.704,\n      \"re_full_rho\": 0.34,\n      \"re_full_auroc\": 0.667,\n      \"ner_voting_f1\": 0.625,\n      \"ner_greedy_f1\": 0.648,\n      \"re_voting_f1\": 0.358,\n      \"re_greedy_f1\": 0.402\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Voting 的出现实际上帮助了论文：它扩大了 structural consistency family 的覆盖面， 同时 voting-as-selection 的失败成为 Claim 2 的证据。Median reviewer 接受这个 framing 但可能仍嫌 '两个信号讲一个故事' 的贡献不够 novel。\\n\\n\\nVoting confidence 在 NER 上 beats SJ（ρ 0.392 vs 0.383），在 RE 上也领先（0.340 vs 0.244）。 这对论文叙事产生压力：如果一个更简单的 entity-level voting 就够了，SJ 的价值在哪？ Median 档 reviewer 的 R3b 质疑被触发。但 voting 作为 selection strategy 输给 greedy （NER 0.625 < 0.648），强化了 Claim 2 的 correlation-selection gap 叙事。 论文需要将 voting 和 SJ 定位为 'structural consistency family 的两个互补成员'： voting 简单高效是实用默认，SJ 可推广到任意 structured output 且温度鲁棒（Δρ=±0.01）。\\n\"\n  },\n  {\n    \"name\": \"evaluation_metrics_expansion\",\n    \"description\": \"Unified 5-signal evaluation: ρ, τ, AUROC, leave-one-out SJ on all datasets.\",\n    \"results\": {\n      \"ner_voting_rho_full\": 0.502,\n      \"ner_voting_auroc\": 0.728,\n      \"ner_sj_rho_full\": 0.357,\n      \"ner_sj_auroc\": 0.666,\n      \"ner_logprob_auroc\": 0.559,\n      \"re_voting_rho_full\": 0.422,\n      \"re_voting_auroc\": 0.716,\n      \"re_sj_auroc\": 0.582,\n      \"re_logprob_auroc\": 0.635,\n      \"focal_auroc_gap_ner\": 0.107,\n      \"focal_auroc_gap_re\": -0.053,\n      \"loo_sj_max_delta_rho\": 0.000305\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Unified Quality Estimation (SciERC, N=8, T=1.0)\",\n        \"columns\": [\n          \"Signal\",\n          \"NER ρ\",\n          \"NER τ\",\n          \"NER AUROC\",\n          \"RE ρ\",\n          \"RE τ\",\n          \"RE AUROC\"\n        ],\n        \"rows\": [\n          [\n            \"voting_conf\",\n            \"0.502\",\n            \"0.377\",\n            \"0.728\",\n            \"0.422\",\n            \"0.327\",\n            \"0.716\"\n          ],\n          [\n            \"SJ\",\n            \"0.357\",\n            \"0.266\",\n            \"0.666\",\n            \"0.211\",\n            \"0.162\",\n            \"0.582\"\n          ],\n          [\n            \"FK\",\n            \"0.265\",\n            \"0.203\",\n            \"0.624\",\n            \"0.253\",\n            \"0.197\",\n            \"0.631\"\n          ],\n          [\n            \"EM\",\n            \"0.257\",\n            \"0.192\",\n            \"0.623\",\n            \"0.100\",\n            \"0.084\",\n            \"0.504\"\n          ],\n          [\n            \"logprob\",\n            \"0.140\",\n            \"0.101\",\n            \"0.559\",\n            \"0.247\",\n            \"0.181\",\n            \"0.635\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Unified evaluation 是论文 soundness 的基石。Median reviewer 给 soundness 3.5/5 因为方法论正确但 RE 数据不支持 universal claim。\\n\\n\\nUnified evaluation 使 NER 上 structural vs logprob 的 AUROC gap 达到 0.107（voting 0.728 vs logprob 0.559）， 落在 median 档 focal_auroc_gap 范围 [0.05, 0.10] 的上沿。这是论文最强的数字之一。 但 RE full 上 SJ AUROC（0.582）低于 logprob（0.635），gap 为负。Median reviewer 会用这个数据点 argue 'signal superiority is dataset/task-dependent'。 Leave-one-out SJ 无循环性（max Δρ=0.0003），解决了 R9 circularity concern， reviewer 会 acknowledge 这个 robustness check。τ 与 ρ 方向一致增强了 soundness。 整体 perceived_soundness 在 [3.0, 4.0] 范围——方法论扎实但结论受 RE 数据限制。\\n\"\n  },\n  {\n    \"name\": \"ner_conll2003\",\n    \"description\": \"Qwen3-8B on CoNLL-2003 NER. Cross-dataset generalization.\",\n    \"results\": {\n      \"sj_rho_full\": 0.436,\n      \"sj_auroc_full\": 0.801,\n      \"fk_rho_full\": 0.4,\n      \"logprob_rho_full\": 0.316,\n      \"em_rho_full\": 0.451,\n      \"ev_rho_full\": 0.424,\n      \"greedy_f1\": 0.912,\n      \"oracle_f1\": 0.954,\n      \"oracle_headroom\": 0.042,\n      \"sj_vs_logprob_delta_rho\": 0.12,\n      \"n_valid\": 2756\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Cross-Dataset Quality Estimation (CoNLL-2003 NER)\",\n        \"columns\": [\n          \"Signal\",\n          \"ρ\",\n          \"τ\",\n          \"AUROC\"\n        ],\n        \"rows\": [\n          [\n            \"EM\",\n            \"0.451\",\n            \"0.400\",\n            \"0.816\"\n          ],\n          [\n            \"SJ\",\n            \"0.436\",\n            \"0.385\",\n            \"0.801\"\n          ],\n          [\n            \"voting_conf\",\n            \"0.424\",\n            \"0.378\",\n            \"0.789\"\n          ],\n          [\n            \"FK\",\n            \"0.400\",\n            \"0.357\",\n            \"0.774\"\n          ],\n          [\n            \"logprob\",\n            \"0.316\",\n            \"0.247\",\n            \"0.753\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CoNLL 数据 confirms structural > logprob cross-dataset，但 EM 抢占 SJ 位置 使 'SJ is best' 的 claim 需要 nuance。论文必须 argue SJ generalizability 而非 SJ dominance。\\n\\n\\nCoNLL 上 SJ ρ=0.436 高于 SciERC（0.357），因为 CoNLL 是简单 flat NER 任务， 模型 greedy F1 已达 0.912，consistency signal 更 reliable。SJ AUROC 0.801 是全实验最高值之一。 但 oracle headroom 仅 0.042（vs SciERC 0.108），意味着 best-of-N selection 的实用价值很小。 Median reviewer 接受 cross-dataset generalization 但注意到：(a) CoNLL 太容易，consistency 高是 trivial 的；(b) headroom 小说明 TTS 本身无意义。这强化了 'quality estimation, not selection' 的 framing 但也让 reviewer 问 'if the model is already 91% F1, who needs confidence estimation?'。 EM 在 CoNLL 上意外地最强（ρ=0.451），因为高准确率下 exact match 率足够区分 easy/hard。\\n\"\n  },\n  {\n    \"name\": \"ner_wnut17\",\n    \"description\": \"WNUT-17 social media NER. Abandoned due to 54% F1=0.\",\n    \"results\": {\n      \"sj_rho_full\": 0.082,\n      \"fk_rho_full\": 0.124,\n      \"logprob_rho_full\": -0.414,\n      \"sample_f1_pct_zero\": 53.7,\n      \"n_instances\": 1287,\n      \"verdict\": \"FAIL\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"WNUT failure 不进入 main results 但作为 Claim 3 的 negative evidence 在 Discussion 中简述。 Median reviewer 不会因此 reject 但会在 scope concern 中引用。\\n\\n\\nWNUT 失败是 median 档的重要 data point。54% 的 sample F1=0 意味着模型在 social media domain 能力不足——consistency signal 在模型 systematically 失败时无意义。这既是 Claim 3（task-complexity boundary）的证据，也是 limitation：论文无法 claim generalization 到 noisy/informal text。Median reviewer 看到 WNUT 被 orphaned 会标记为 'only tested on well-structured text domains'（R1 concern）。论文选择不报告 WNUT 在 Limitations 中 acknowledge，reviewer 认为 honest 但仍视为 scope 不足。Logprob 出现负相关（ρ=-0.414） 是因为模型对 noisy text 过度自信——生成流畅但错误的 output 有高 logprob。\\n\"\n  },\n  {\n    \"name\": \"ner_multi_model\",\n    \"description\": \"LLaMA-3.1-8B on SciERC. Model-agnostic validation.\",\n    \"results\": {\n      \"ner_rho_sj\": 0.363,\n      \"ner_rho_fk\": 0.327,\n      \"ner_rho_logprob\": 0.183,\n      \"ner_sj_beats_surface\": true,\n      \"re_rho_sj\": 0.299,\n      \"re_rho_logprob\": 0.288,\n      \"re_sj_cond\": 0.405,\n      \"re_logprob_cond\": 0.092,\n      \"re_sample_f1_pct_zero\": 41.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Cross-Model Validation (LLaMA-3.1-8B, SciERC)\",\n        \"columns\": [\n          \"Subtask\",\n          \"Signal\",\n          \"ρ full\",\n          \"ρ cond\",\n          \"AUROC\"\n        ],\n        \"rows\": [\n          [\n            \"NER\",\n            \"SJ\",\n            \"0.363\",\n            \"0.311\",\n            \"—\"\n          ],\n          [\n            \"NER\",\n            \"logprob\",\n            \"0.183\",\n            \"0.109\",\n            \"—\"\n          ],\n          [\n            \"RE\",\n            \"SJ\",\n            \"0.299\",\n            \"0.405\",\n            \"—\"\n          ],\n          [\n            \"RE\",\n            \"logprob\",\n            \"0.288\",\n            \"0.092\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-model evidence 足够支撑 'model-agnostic' 在 softened form 下通过 review， 但 median reviewer 会在 major weakness 中写 'limited to 8B parameter scale'。\\n\\n\\nLLaMA NER 上 SJ（0.363）> logprob（0.183），structural > surface 一致成立， 支撑 model-agnostic claim。但 RE full set 上 SJ（0.299）仅微弱领先 logprob（0.288）， 且均 < 0.30。RE cond 上 SJ 大幅反弹（0.405），但 41.2% 的 RE sample F1=0  表明 LLaMA 在 SciERC RE 上同样面临 capability gap。 Median reviewer 接受 2-model validation 但指出：'Both 8B models show similar patterns. A 70B model or a fundamentally different architecture would strengthen the generalization claim.' 这触发 R14（cross-model validation thin），但不致命——reviewer 视为 P1 而非 P0 concern， 因为 2×8B across 2 architectures（Qwen/LLaMA）至少排除了 model-specific artifact。\\n\"\n  },\n  {\n    \"name\": \"ner_llama_conll\",\n    \"description\": \"LLaMA-3.1-8B on CoNLL-2003 for 2×2 matrix completion.\",\n    \"results\": {\n      \"sj_rho_full\": 0.431,\n      \"fk_rho_full\": 0.428,\n      \"logprob_rho_full\": 0.307,\n      \"voting_conf_rho_full\": 0.426,\n      \"sj_auroc_full\": 0.704,\n      \"logprob_auroc_full\": 0.761,\n      \"greedy_f1\": 0.927,\n      \"n_valid\": 2756\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: 2×2 Cross-Validation Matrix (NER ρ full)\",\n        \"columns\": [\n          \"\",\n          \"SciERC\",\n          \"CoNLL-2003\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            \"0.357 (SJ) / 0.140 (lp)\",\n            \"0.436 (SJ) / 0.316 (lp)\"\n          ],\n          [\n            \"LLaMA-3.1-8B\",\n            \"0.363 (SJ) / 0.183 (lp)\",\n            \"0.431 (SJ) / 0.307 (lp)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"2×2 矩阵是 reviewer R1+R2 的核心回应。4/4 configurations 上 structural ρ > logprob ρ。 Median reviewer 认可但注意到都是 8B 规模和 well-structured text，scope concern 不消。\\n\\n\\nLLaMA×CoNLL 完成 2×2 矩阵（Qwen×LLaMA × SciERC×CoNLL）。SJ ρ=0.431 与 Qwen×CoNLL 的 0.436 高度一致，证明 cross-model consistency。这是论文 generalization 最强论据。 但 AUROC 上 logprob（0.761）反超 SJ（0.704）——CoNLL 高准确率场景下 logprob 的 discriminative power 更强。Median reviewer 注意到 AUROC ranking 与 ρ ranking 不一致 （SJ wins ρ, logprob wins AUROC on CoNLL），这会引发 'which metric matters more?' 的讨论。 论文需要 argue ρ 更 informative 因为它测量 monotonic ordering 而非 binary discrimination。 cross_config_ner_structural_gt_logprob_rate 在 ρ 上为 4/4（100%），在 AUROC 上为 2/4（50%）， 落在 median 档 [0.8, 1.0] 的边缘——取决于论文主推哪个 metric。\\n\"\n  },\n  {\n    \"name\": \"ner_n16_scierc\",\n    \"description\": \"N=16 with 3-seed robustness on SciERC.\",\n    \"results\": {\n      \"ner_sj_rho_mean_3seed\": 0.412,\n      \"ner_sj_rho_sd_3seed\": 0.025,\n      \"ner_voting_conf_rho_s42\": 0.399,\n      \"ner_sj_rho_s42\": 0.398,\n      \"re_sj_rho_s42\": 0.277,\n      \"re_voting_conf_rho_s42\": 0.38,\n      \"re_full_verdict\": \"FAIL\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: N-Scaling & Seed Robustness (SciERC)\",\n        \"columns\": [\n          \"Config\",\n          \"NER SJ ρ\",\n          \"RE SJ ρ\",\n          \"NER AUROC\",\n          \"RE AUROC\"\n        ],\n        \"rows\": [\n          [\n            \"N=8, s42\",\n            \"0.383\",\n            \"0.244\",\n            \"0.689\",\n            \"0.592\"\n          ],\n          [\n            \"N=16, s42\",\n            \"0.398\",\n            \"0.277\",\n            \"0.697\",\n            \"—\"\n          ],\n          [\n            \"N=16, s123\",\n            \"0.423\",\n            \"0.267\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"N=16, s456\",\n            \"0.414\",\n            \"0.268\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"N=16 mean±SD\",\n            \"0.412±0.025\",\n            \"0.271±0.006\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Seed stability 强（SD=0.025），RE 一致地弱（3 seed 均 < 0.28）。 Median reviewer：'The authors appropriately report multi-seed results. RE weakness  is a real limitation, not a statistical artifact.'\\n\\n\\n3-seed NER SJ ρ 均值 0.412（SD=0.025），稳定性良好。N=16 vs N=8 在 NER 上 marginal improvement（0.412 vs 0.357），说明 N=8 已接近饱和。RE full set SJ ρ=0.277  仍远低于 0.40 阈值，N=16 未能挽救 RE。这是 median 档的关键数据： reviewer 看到 RE rho < 0.30 会 argue 'consistency signals fundamentally limited for  relational tasks'，将 Claim 1 的适用范围限制在 NER。论文通过 conditional analysis 部分挽回（RE cond SJ ρ~0.37-0.40），但这只占 2/3 的实例。 3-seed 稳定性是正面信号——soundness 得分因此在 3.5 左右而非更低。\\n\"\n  },\n  {\n    \"name\": \"adaptive_compute_demo\",\n    \"description\": \"Best-of-N selection: all signals vs greedy vs oracle.\",\n    \"results\": {\n      \"ner_scierc_greedy\": 0.618,\n      \"ner_scierc_sj\": 0.62,\n      \"ner_scierc_logprob\": 0.621,\n      \"ner_scierc_oracle\": 0.787,\n      \"ner_conll_greedy\": 0.725,\n      \"ner_conll_sj\": 0.718,\n      \"re_greedy\": 0.403,\n      \"re_logprob\": 0.41,\n      \"re_sj\": 0.397,\n      \"re_oracle\": 0.631\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Best-of-N Selection F1 (SciERC, N=16)\",\n        \"columns\": [\n          \"Signal\",\n          \"NER F1\",\n          \"Δ vs greedy\",\n          \"RE F1\",\n          \"Δ vs greedy\"\n        ],\n        \"rows\": [\n          [\n            \"greedy\",\n            \"0.618\",\n            \"—\",\n            \"0.403\",\n            \"—\"\n          ],\n          [\n            \"logprob\",\n            \"0.621\",\n            \"+0.003\",\n            \"0.410\",\n            \"+0.007\"\n          ],\n          [\n            \"SJ\",\n            \"0.620\",\n            \"+0.002\",\n            \"0.397\",\n            \"−0.006\"\n          ],\n          [\n            \"FK\",\n            \"0.621\",\n            \"+0.003\",\n            \"0.396\",\n            \"−0.007\"\n          ],\n          [\n            \"voting_conf\",\n            \"0.585\",\n            \"−0.033\",\n            \"0.408\",\n            \"+0.005\"\n          ],\n          [\n            \"random\",\n            \"0.586\",\n            \"−0.032\",\n            \"0.364\",\n            \"−0.039\"\n          ],\n          [\n            \"oracle\",\n            \"0.787\",\n            \"+0.169\",\n            \"0.631\",\n            \"+0.228\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Selection curves figure 是论文最重要的 visualization——它让 correlation-selection gap  一目了然。Median reviewer 评价 Claim 2 为 'interesting observation but unclear practical impact' （核心假设 #2）。需要 actionable guidance 回应 'so what'。\\n\\n\\nNER best-of-N：所有信号 ≤ greedy（SJ 0.620 ≈ greedy 0.618，差异 statistically insignificant）， oracle headroom +16.9pp 完全无法 exploit。这是 Claim 2 的核心负面发现。 RE：仅 logprob（0.410）beat greedy（0.403，+0.7pp），SJ（0.397）反而略低于 greedy。 Median reviewer 的反应两极：一方面 'negative result is interesting and honest'， 另一方面 'if your signals can't improve anything, what's the practical value?'。 NER selection 全面失败在 median 档被至少 1 位 reviewer 视为 significant limitation（核心假设 #6）。 论文必须 pivot 叙事：'These results reveal a fundamental gap between quality estimation  (knowing which INPUTS are reliable) and sample selection (choosing which OUTPUT is best).' Oracle gap 的存在（NER +16pp, RE +23pp）说明 better signals 理论上可行——current unsupervised  signals 还不够。\\n\"\n  },\n  {\n    \"name\": \"signal_ensemble_analysis\",\n    \"description\": \"SJ+logprob ensemble, linear combination grid search, logistic regression.\",\n    \"results\": {\n      \"sj_logprob_pearson_ner\": 0.57,\n      \"sj_logprob_pearson_re\": 0.42,\n      \"best_linear_ner_combo\": \"SJ+voting_conf α=0.3\",\n      \"best_linear_ner_rho\": 0.489,\n      \"best_linear_re_combo\": \"voting_conf+logprob α=0.6\",\n      \"best_linear_re_rho\": 0.429,\n      \"ensemble_ner_auroc\": 0.735,\n      \"ensemble_re_auroc\": 0.719,\n      \"ensemble_ner_delta_auroc\": 0.035,\n      \"selection_ner_ensemble_f1\": 0.604,\n      \"selection_ner_greedy_f1\": 0.609,\n      \"selection_re_logprob_f1\": 0.397,\n      \"selection_re_greedy_f1\": 0.374\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Ensemble Analysis\",\n        \"columns\": [\n          \"Method\",\n          \"NER ρ\",\n          \"NER AUROC\",\n          \"RE ρ\",\n          \"RE AUROC\"\n        ],\n        \"rows\": [\n          [\n            \"Best single (voting_conf)\",\n            \"0.502\",\n            \"0.728\",\n            \"0.422\",\n            \"0.716\"\n          ],\n          [\n            \"Best linear combo\",\n            \"0.489\",\n            \"—\",\n            \"0.429\",\n            \"—\"\n          ],\n          [\n            \"Logistic regression ensemble\",\n            \"—\",\n            \"0.735\",\n            \"—\",\n            \"0.719\"\n          ],\n          [\n            \"Oracle\",\n            \"—\",\n            \"—\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ensemble 结果 resolves R11 但不改变 paper narrative。 Median reviewer 给 credit for thoroughness，不 penalize。\\n\\n\\nEnsemble NER AUROC 0.735 比 best single 0.700 提升 +0.035——improvement 存在但 marginal。 RE ensemble AUROC 0.719 实际略低于 voting_conf 单独的 0.721，无 improvement。 SJ 和 logprob 的 Pearson 相关 0.57 说明二者 moderately correlated——它们捕获的信息 有 overlap 也有 complement。Linear combo 最佳组合是 SJ+voting（NER）和 voting+logprob（RE）， 而非 SJ+logprob——这暗示同 family 内组合（structural×structural）比跨 family 更有效。 关键 negative：ensemble 也无法 beat greedy on NER selection（0.604 < 0.609）。 Median reviewer 认为 ensemble 分析 comprehensive 但 '强化了 negative result 而非解决它'。 Effective claim count = 2（quality estimation + gap），ensemble 是 supporting evidence 不是独立 claim。\\n\"\n  },\n  {\n    \"name\": \"selection_curves\",\n    \"description\": \"Best-of-N curves for N=1,2,4,8,16 across all datasets.\",\n    \"results\": {\n      \"scierc_ner_n16_oracle\": 0.787,\n      \"scierc_ner_n16_best_signal\": 0.621,\n      \"scierc_ner_n4_oracle\": 0.714,\n      \"scierc_re_n16_logprob\": 0.41,\n      \"scierc_re_n8_logprob\": 0.413,\n      \"conll_ner_n8_sj\": 0.718,\n      \"conll_ner_n8_greedy\": 0.725\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"这个 figure 直接回应 R16（zero figures），是 median 档论文从 table-only 升级的关键。\\n\\n\\nSelection curves 跨 N 值的 pattern 高度一致：NER 上所有信号 flat at greedy level， RE 上仅 logprob 微幅超越。CoNLL NER 上 N=8 所有信号（SJ 0.718）反而低于 greedy（0.725）， 因为 CoNLL 高准确率下 T=1.0 的 stochastic samples 引入 noise 而非 diversity。 Oracle 随 N 单调增长（NER: 0.714→0.787），说明 sample pool 中确实存在更好 output， 但 unsupervised signals 无法识别。这个 gap 的视觉化（Figure 1）是论文最有 impact 的贡献。 Median reviewer 认为这个 figure 比任何 table 更 convincing，但仍可能 comment  'the gap is well-documented but the authors offer no path forward'。\\n\"\n  },\n  {\n    \"name\": \"re_diagnostic_analysis\",\n    \"description\": \"Per-relation-type breakdown, error propagation, threshold sensitivity, bootstrap CI.\",\n    \"results\": {\n      \"hyponym_rho_sj\": 0.545,\n      \"feature_of_rho_sj\": 0.004,\n      \"used_for_rho_sj\": 0.236,\n      \"entity_span_error_pct\": 55.5,\n      \"fisher_z_ner_vs_re_sj_p\": 0.021,\n      \"bootstrap_ci_ner_sj\": [\n        0.295,\n        0.459\n      ],\n      \"bootstrap_ci_re_sj\": [\n        0.142,\n        0.339\n      ],\n      \"threshold_thr0_rho_sj\": 0.316,\n      \"threshold_thr0_n\": 313\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Per-Relation-Type Quality Estimation (SciERC RE)\",\n        \"columns\": [\n          \"Relation Type\",\n          \"n\",\n          \"ρ_SJ\",\n          \"ρ_FK\",\n          \"ρ_VC\",\n          \"Mean F1\"\n        ],\n        \"rows\": [\n          [\n            \"HYPONYM-OF\",\n            \"36\",\n            \"0.545\",\n            \"0.646\",\n            \"0.628\",\n            \"0.513\"\n          ],\n          [\n            \"CONJUNCTION\",\n            \"86\",\n            \"0.383\",\n            \"0.350\",\n            \"0.484\",\n            \"0.480\"\n          ],\n          [\n            \"USED-FOR\",\n            \"299\",\n            \"0.236\",\n            \"0.255\",\n            \"0.286\",\n            \"0.422\"\n          ],\n          [\n            \"PART-OF\",\n            \"44\",\n            \"0.239\",\n            \"0.348\",\n            \"0.283\",\n            \"0.297\"\n          ],\n          [\n            \"EVALUATE-FOR\",\n            \"62\",\n            \"0.172\",\n            \"0.255\",\n            \"0.226\",\n            \"0.365\"\n          ],\n          [\n            \"COMPARE\",\n            \"35\",\n            \"0.168\",\n            \"0.184\",\n            \"0.180\",\n            \"0.453\"\n          ],\n          [\n            \"FEATURE-OF\",\n            \"50\",\n            \"0.004\",\n            \"0.052\",\n            \"0.014\",\n            \"0.254\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Diagnostic analysis 最强贡献是 error decomposition 和 per-relation heterogeneity。 Median reviewer 接受这些但要求 soften 'diagnostic framework' → 'empirical analysis'。\\n\\n\\nPer-relation analysis 揭示巨大异质性：HYPONYM-OF ρ_sj=0.545（接近 NER 水平）， FEATURE-OF ρ_sj=0.004（近乎零）。这种 within-task variance 比 NER-vs-RE 的 between-task 差异更有 diagnostic value。Entity span errors 占 RE FN 的 55.5%，说明 RE failure 主要是 entity 识别失败导致的 cascade——compound error propagation 实锤。 Fisher Z-test 确认 NER ρ_sj significantly > RE ρ_sj（p=0.021）。 Median reviewer 视这些为 'solid descriptive analysis' 但不是 'prescriptive framework' （R17 concern）。Bootstrap CI 显示 NER SJ 和 RE SJ 的 95% CI 有 overlap（NER [0.295, 0.459]  vs RE [0.142, 0.339]）——虽然均值差异显著但不是 dramatic separation。 Threshold sensitivity 分析显示 thr=0.00 时 ρ=0.316（n=313），thr=0.05 时 ρ 反降至 0.268（n=239）， 说明 conditional threshold 不是 monotonically beneficial——只是 F1=0 的 extreme cases 拉低了相关。\\n\"\n  },\n  {\n    \"name\": \"temperature_sensitivity_analysis\",\n    \"description\": \"T=0.7 vs T=1.0 comparison for all signals.\",\n    \"results\": {\n      \"sj_delta_rho_t07_vs_t10\": 0.01,\n      \"fk_delta_rho_t07_vs_t10\": 0.06,\n      \"recommendation\": \"T=1.0 + conditional filtering\",\n      \"re_oracle_headroom_t10\": 0.167,\n      \"re_oracle_headroom_t07\": 0.131,\n      \"re_diversity_1_sj_t10\": 0.389,\n      \"re_diversity_1_sj_t07\": 0.313\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"温度分析作为 Claim 3 的 supporting evidence，不独立贡献 novelty。 SJ 的温度鲁棒性是 reviewer 质疑 R3b 时的防御点。\\n\\n\\nSJ 温度鲁棒性极强（Δρ=±0.01 across T=0.7/1.0），FK 受温度影响更大（Δρ=±0.06-0.09）。 这是 SJ 相对于 FK 的独特优势之一，在 R3b 的回应中有价值。 T=1.0 保留更多 oracle headroom（RE: 0.167 vs 0.131）和多样性（1-SJ: 0.389 vs 0.313）， 但 selection 上无 signal 能 exploit 这个 headroom。 Conditional filtering 的 lift（+0.07~0.14）远大于温度调优（±0.01）， 说明 '智能过滤 > 参数调优' 是一个 practical recommendation。 Median reviewer 认为温度分析 'adequate but not a standalone contribution'。\\n\"\n  },\n  {\n    \"name\": \"capability_stratification\",\n    \"description\": \"Instance stratification by difficulty and independent proxies.\",\n    \"results\": {\n      \"ner_sj_rho_overall\": 0.398,\n      \"ner_by_ent_count_0_sj_rho\": 0.689,\n      \"ner_by_ent_count_3_5_sj_rho\": 0.353,\n      \"re_hard_0_25_sj_rho\": -0.043,\n      \"re_easy_sj_rho\": 0.21,\n      \"inverted_u_confirmed\": false,\n      \"proxy_independence_ner_f1_vs_slen\": -0.021\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Stratification 支撑 Claim 3 但 inverted-U 不确认意味着 'complexity boundary'  是 monotonic degradation 而非 non-linear pattern。叙事需对应调整。\\n\\n\\nEntity count=0 时 SJ ρ=0.689（最高），因为空实例的 binary judgment 更清晰。 RE hard instances（greedy F1 < 0.25）SJ ρ=-0.043（近乎随机），证明 consistency signal 在模型 capability 之外完全失效。Inverted-U pattern 未确认——这是 honest negative  但也意味着论文不能 claim 'sweet spot' 的存在。Independent proxy（句长、entity count） 与 F1 几乎正交（r=-0.021, 0.007），验证了分层不是 circular。 Median reviewer 视为 solid analysis 但 'descriptive, not actionable'： 知道 hard instances 的 signal 弱不能帮助 practitioner 决定何时 trust。\\n\"\n  },\n  {\n    \"name\": \"re_n16_confirmation\",\n    \"description\": \"RE N=16 on SciERC — test N-scaling effect on RE.\",\n    \"results\": {\n      \"re_rho_sj_full\": 0.297,\n      \"re_rho_sj_cond\": 0.398,\n      \"re_rho_logprob_full\": 0.299,\n      \"re_headroom\": 0.232,\n      \"ner_rho_sj_full\": 0.377,\n      \"verdict\": \"FAIL\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"RE N=16 的 FAIL verdict 是论文最大的 inconvenient truth。 Median reviewer：'Even with doubled compute budget, RE quality estimation remains weak.'\\n\\n\\nN=16 对 RE 的改善 marginal：SJ ρ 从 N=8 的 0.211 升至 0.297（+0.086）， 仍远低于 0.40。Logprob 在 N=16 上 ρ=0.299 与 SJ 几乎相同——更多 samples 缩小了 SJ 和 logprob 的差距但都没超越 0.30 barrier。Headroom 扩大到 0.232， 但 signal 改善幅度远不够 exploit。Conditional set ρ_sj=0.398 接近 0.40 阈值 但仍 borderline。这确认了 RE consistency signal 的弱势不是 sample budget 问题—— 即使 N=16 也不够。早期在 200 instance subset + T=0.7 上观察到的 N-scaling 'breakthrough' 被证实是 artifact（核心假设 #5：RE ρ < 0.30 限制 claim scope）。\\n\"\n  },\n  {\n    \"name\": \"ner_ood_robustness\",\n    \"description\": \"NER OOD robustness via cross-domain transfer (e.g., SciERC model on CoNLL or vice versa).\",\n    \"results\": {\n      \"ood_sj_rho_full\": 0.15,\n      \"ood_fk_rho_full\": 0.1,\n      \"ood_logprob_rho_full\": -0.2,\n      \"ood_sample_f1_pct_zero\": 35.0,\n      \"ood_greedy_f1\": 0.45,\n      \"structural_beats_surface\": true,\n      \"verdict\": \"MARGINAL\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table (Appendix): OOD Robustness\",\n        \"columns\": [\n          \"Signal\",\n          \"In-Domain ρ\",\n          \"OOD ρ\",\n          \"Δ\"\n        ],\n        \"rows\": [\n          [\n            \"SJ\",\n            \"0.357\",\n            \"0.15\",\n            \"−0.207\"\n          ],\n          [\n            \"FK\",\n            \"0.265\",\n            \"0.10\",\n            \"−0.165\"\n          ],\n          [\n            \"logprob\",\n            \"0.140\",\n            \"−0.20\",\n            \"−0.340\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"OOD 实验如果执行会进入 Appendix 而非 main results。Median reviewer 不太可能 要求这个实验作为 acceptance condition，但它回应了 closed-source API applicability 叙事。 实际执行风险：如果 OOD F1 太低（<0.30），consistency analysis 失去意义。 建议：如果 GPU 时间允许，仅作为 supplementary evidence，不影响 main claims。\\n\\nOOD 场景下模型 greedy F1 大幅下降（~0.45 vs in-domain 0.66），consistency signal  相应退化但 structural 仍优于 surface（SJ ρ~0.15 > FK ρ~0.10）。Logprob 在 OOD 下 出现负相关（ρ~-0.20），因为 domain shift 导致 logprob 与 accuracy 脱钩——模型 对 in-domain-like patterns 过度自信。这是 SJ 在 closed-source API / OOD 场景下 独特价值的支撑：即使绝对 ρ 不高，至少 direction 正确且不会 mislead。 35% F1=0 rate 类似 WNUT，说明 OOD performance 受模型 capability 限制。 Median reviewer 不会 heavily weight 这个实验（P2），但它回应了 R18（when would  consistency help?）——answer：当 logprob 不可用或不可信时。 注意：这是唯一 truly unrun 的 planned 实验，预测有更大不确定性。\\n\"\n  }\n]",
      "numLines": 768,
      "startLine": 1,
      "totalLines": 768
    }
  },
  "sourceToolAssistantUUID": "48a565c6-ba07-4f52-bf49-720188d4f9c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T21:07:11.340Z_

<details><summary>↩ Tool result · `toolu_01PKGpBNsScygCwyyTwkHshF`</summary>

```text
1	# Paper Framing — struct_self_consist_ie
2	
3	> Updated 2026-05-14 post-exp-016 pivot (D019). CRITICAL NARRATIVE CHANGE: best-of-N selection fails on NER (all signals ≤ greedy). Pivot from "TTS improvement" to "confidence estimation + correlation-selection gap".
4	
5	## Target Venue
6	- Primary: EMNLP 2026 Main (via ARR May 2026)
7	- Fallback: EMNLP 2026 Findings
8	- Deadline: ARR May cycle, 2026-05-25
9	
10	## Core Claims (3 条)
11	
12	### Claim 1 (Positive — Quality Estimation)
13	Structural consistency signals (entity voting confidence, soft Jaccard) are the strongest unsupervised quality estimators for entity-level IE, significantly outperforming model confidence (log-probability) and surface agreement (FK, exact-match) at instance-level quality prediction. Entity voting achieves AUROC 0.73 / ρ=0.50 on NER, SJ achieves AUROC 0.67 / ρ=0.36 — both far above logprob (AUROC 0.56 / ρ=0.14). Voting leads SJ on full set; SJ retains unique strength in conditional evaluation (ρ=0.41) and is temperature-robust (Δρ=±0.01).
14	
15	**Key insight**: The contribution is about a FAMILY of structural consistency signals for QUALITY ESTIMATION (predicting which instances are reliable), not for per-sample selection. SJ and voting_conf both capture entity-across-sample consistency. SJ generalizes to arbitrary structured outputs; voting is simpler.
16	
17	**Evidence** (SciERC, N=8, T=1.0, unified exp_015 evaluation):
18	- NER full (n=529): voting ρ=0.502/τ=0.377/AUROC=0.728, SJ ρ=0.357/τ=0.266/AUROC=0.666, FK ρ=0.265/τ=0.203/AUROC=0.624, EM ρ=0.257/τ=0.192/AUROC=0.623, logprob ρ=0.140/τ=0.101/AUROC=0.559
19	- NER cond (n=501): voting ρ=0.450, SJ ρ=0.412, EM ρ=0.343, FK ρ=0.306, logprob ρ=0.163
20	- RE full (n=397): voting ρ=0.422/AUROC=0.716, FK ρ=0.253/AUROC=0.631, logprob ρ=0.247/AUROC=0.635, SJ ρ=0.211/AUROC=0.582, EM ρ=0.100/AUROC=0.504
21	- RE cond (n=296): voting ρ=0.463, SJ ρ=0.368, EM ρ=0.361, FK ρ=0.317, logprob ρ=0.146
22	- Temperature robustness: SJ Δρ=±0.01 across T=0.7/1.0; FK Δρ=±0.06-0.09 (SJ far more stable)
23	
24	### Claim 2 (Novel Finding — Correlation-Selection Gap)
25	Instance-level quality estimation ≠ per-sample selection ability. Despite strong instance-level correlation (ρ≈0.39-0.43), NO unsupervised confidence signal beats greedy decoding for NER best-of-N selection. On RE, only log-probability (+2.4pp over greedy) enables effective selection. The oracle headroom is large (NER +16pp, RE +18pp) but current signals cannot exploit it.
26	
27	**exp-016 evidence** (SciERC, N=8, T=1.0, n=529):
28	- NER best-of-N: greedy 0.6094 > logprob 0.6087 > ensemble 0.6043 > sj 0.6042 > voting 0.5959 > random 0.5796 (oracle 0.7692)
29	- RE best-of-N: logprob 0.3971 > greedy 0.3735 > sj 0.3680 > voting 0.3379 ≈ random 0.3380 (oracle 0.5610)
30	- Instance-level AUROC: voting_conf 0.700, SJ 0.689, ensemble 0.735 >> logprob 0.591
31	
32	**Key insight**: Consistency signals are INSTANCE-LEVEL aggregates (one score per instance). They predict which inputs are easy/hard, NOT which sample is best. Log-prob is the only PER-SAMPLE signal and uniquely enables selection on uncertain tasks (RE). This distinction between quality estimation and sample selection is the paper's most practically important finding.
33	
34	**Implications**: (a) For selective prediction / abstention → use structural consistency (AUROC 0.70+). (b) For best-of-N selection → use logprob, but only on tasks where greedy is suboptimal (RE). (c) For NER, greedy is near-optimal → TTS offers no advantage with current signals.
35	
36	### Claim 3 (Diagnostic — task-complexity boundary)
37	The effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.
38	
39	**MVP evidence**: RE full rho_sj=0.234, RE cond rho_sj=0.372 (SJ>FK +11.8pp). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.
40	
41	**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.
42	
43	**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):
44	- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10
45	- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392
46	- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.
47	- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.
48	
49	## Story Spine
50	
51	**Problem**: LLM-based structured prediction (IE) increasingly uses multi-sample generation, but practitioners lack guidance on which confidence signals to trust — and for what purpose. Crucially, it is unknown whether signals that predict output quality (instance-level) also enable effective sample selection (per-sample-level).
52	
53	**Existing approaches & gaps**: Self-consistency in reasoning uses exact-match voting (Wang et al. 2023). USC (Chen et al. 2024) uses LLM-as-judge. For structured prediction, no systematic comparison exists across confidence signal families. More importantly, prior work conflates quality estimation with selection — assuming that high correlation with accuracy translates to effective best-of-N selection.
54	
55	**Our framing**: We systematically compare five confidence signals across four families for IE: (1) model confidence (log-probability), (2) surface agreement (FK, exact-match), (3) set-aware structural similarity (SJ), (4) entity-level majority voting. We make three findings:
56	1. Structural consistency (voting_conf/SJ) provides the strongest quality estimation (AUROC 0.73 vs logprob 0.56)
57	2. However, a **correlation-selection gap** exists: despite strong instance-level correlation, NO signal beats greedy decoding for NER selection; only logprob helps for RE (+2.4pp)
58	3. All signals degrade on relational tasks due to compound error propagation
59	
60	**Headline result template**: "On NER, entity voting confidence achieves AUROC 0.73 and ρ=0.50 for quality estimation, significantly outperforming log-probability (AUROC 0.56, ρ=0.14). However, this quality estimation capability does NOT translate to effective best-of-N selection — no signal surpasses greedy decoding on NER (oracle headroom: +16pp). We identify a fundamental correlation-selection gap: instance-level consistency predicts WHICH INPUTS are reliable, not WHICH OUTPUTS are best. On RE, only per-sample log-probability enables selection (+2.4pp), while all consistency signals degrade."
61	
62	## Anticipated Reviewer Concerns
63	
64	### R1: "Only one NER dataset — generalization unclear"
65	- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.
66	- **Priority**: P0
67	
68	### R2: "Only one model family (Qwen3-8B)"
69	- **Mitigation**: exp-007 (LLaMA-3.1-8B) shows model-agnostic effect
70	- **Priority**: P0
71	
72	### R3: "FK is a strawman baseline — what about log-prob, USC, exact-match?"
73	- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (SJ+voting) >> log-prob >> FK ≈ exact-match. USC discussed in related work (LLM-as-judge, orthogonal approach).
74	- **Priority**: P0, RESOLVED — results decisive
75	
76	### R3b: "Voting confidence beats SJ — why use SJ?"
77	- **Mitigation**: SJ generalizes to arbitrary structured outputs (relations, events, any set-structured prediction). Voting is entity-specific. NER full: voting leads (ρ=0.50 vs 0.36), but SJ retains unique strength in conditional evaluation (ρ=0.41 vs voting 0.45) and is more temperature-robust (Δρ=±0.01). RE cond: SJ ρ=0.37 competitive with voting 0.46. SJ is also more interpretable (pairwise similarity). Paper presents both as complementary instantiations of the structural consistency principle, with voting as practical default and SJ as robust/generalizable option.
78	- **Priority**: P1 — narrative adjustment needed given exp_015 unified values
79	
80	### R4: "No actual TTS improvement demonstrated"
81	- **Status**: ⚠️ CONFIRMED NEGATIVE by exp-016. Best-of-N selection DOES NOT beat greedy on NER with any signal. RE: only logprob +2.4pp over greedy.
82	- **Mitigation**: Paper PIVOTS to "confidence estimation + correlation-selection gap analysis." exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.
83	- **Priority**: P0 — narrative pivot required
84	
85	### R5: "Sample size N=8 may be too small for reliable SJ estimation"
86	- **Mitigation**: exp-001 (N=16) with multi-seed robustness
87	- **Priority**: P0
88	
89	### R6: "Conditional analysis cherry-picks favorable instances"
90	- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.
91	- **Priority**: P0 (add sensitivity analysis)
92	
93	### R7: "Only ρ as evaluation metric"
94	- **Mitigation**: Add AUROC, calibration plots, Kendall's τ for all experiments
95	- **Priority**: P0
96	
97	### R8: "Formula-implementation discrepancy"
98	- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)
99	- **Priority**: P0, paper writing fix
100	
101	### R9: "Evaluation circularity (T>0 consistency vs T=0 F1)"
102	- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).
103	- **Priority**: P0
104	
105	### R10: "Insufficient related work" (三档一致 [B][M][W])
106	- **Mitigation**: Expand to 35+ references. Must cite:
107	  - USC (Chen 2024) — empirical differentiation, not just citation
108	  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)
109	  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021
110	  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020
111	  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016
112	  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023
113	  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024
114	  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022
115	  - **IE confidence**: Culotta & McCallum 2004
116	  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)
117	  - **[2025-2026 新颖性自查补充 — 必引]**:
118	    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出
119	    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap
120	    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案
121	    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量
122	    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承"overlooks semantically consistent outputs"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机
123	  - **[2025-2026 新颖性自查补充 — 应引]**:
124	    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述
125	    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述
126	    - Semantic Entropy Probes (2024) — 低成本不确定性估计
127	    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性
128	    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务
129	    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关
130	    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位
131	    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE
132	    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE
133	  - **需新增 Related Work 小节**:
134	    - "Test-Time Scaling & Sample Selection" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap
135	    - "Consistency for Structured IE" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation
136	- **Priority**: P0, Paper Agent handles
137	
138	### R11: "SJ+logprob ensemble missing" (Dream 2 — both reviewers)
139	- **Status**: ✅ RESOLVED by exp-016. Results:
140	  - Ensemble AUROC: NER 0.735 (+3.5pp over best single), RE 0.719 (−0.2pp, no improvement)
141	  - Linear combo: SJ+voting best at α=0.3 (NER ρ=0.489); RE α=0.0 (pure voting)
142	  - FK negative coefficient in logistic regression → surface agreement is net-negative when structural signals present
143	  - **Interpretation**: voting_conf captures nearly all discriminative information; ensemble adds marginal value on NER, none on RE. Supports the "structural consistency family" narrative.
144	- **Priority**: DONE — write into paper with honest interpretation
145	
146	### R12: "No supervised upper bound / reward model comparison" (Dream 2)
147	- **Mitigation**: Simple logistic regression on [SJ, FK, logprob, voting_conf, EM] as proxy for trained verifier (included in exp-016). Full reward model training out of scope for this paper — discuss as future work.
148	- **Priority**: P1 (partially addressed by exp-016 ensemble)
149	
150	### R13: "Headroom capture rate low (37% NER, 11% RE)" (Dream 2)
151	- **Mitigation**: Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline.
152	- **Priority**: P0, paper writing
153	
154	### R14: "Cross-model validation thin — need more than 2×8B" (Dream 2)
155	- **Mitigation**: exp-017 (LLaMA on CoNLL, P1). 70B model infeasible within GPU budget. Acknowledge as limitation.
156	- **Priority**: P1
157	
158	### R15: "Log-prob definition ambiguity — Eq.1 vs best-of-N ranking" (Dream 2 cross-tier, [W])
159	- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state "all best-of-N require N forward passes; log-prob adds zero ranking overhead."
160	- **Priority**: P0, Paper Agent handles
161	
162	### R16: "Zero figures — data-rich paper with only tables" (Dream 2 cross-tier, [W])
163	- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.
164	- **Priority**: P0, Paper Agent handles
165	
166	### R17: "Diagnostic framework overclaimed — descriptive not prescriptive" (Dream 2 cross-tier, [M][W])
167	- **Mitigation**: Soften "diagnostic framework" to "diagnostic analysis" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.
168	- **Priority**: P0, Paper Agent handles
169	
170	### R18: "No discussion of when consistency WOULD help" (Dream 2 cross-tier, [W])
171	- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.
172	- **Priority**: P1, Paper Agent handles
173	
174	### R19: "Negative result partially predictable for fine-tuned models" (Dream 2 cross-tier, [W])
175	- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.
176	- **Priority**: P1, Paper Agent handles
177	
178	## Venue Fit
179	
180	EMNLP is well-suited for:
181	- Systematic empirical comparison of confidence signals for structured prediction
182	- Diagnostic findings with principled explanations
183	- The "comparison + boundary condition" contribution pattern
184	
185	Risk assessment (post-Dream 2, all tiers 3/6):
186	- **Structural risks (三档一致)**: (1) novelty perceived as incremental, (2) related work thin, (3) single RE dataset. These are presentation/positioning issues, NOT data issues — fixable by Paper Agent.
187	- **Data-dependent risks (观察中)**: SJ vs LOGPROB ranking may be dataset-dependent (Dream imagined this; awaiting exp-002/003 real data). If confirmed → reframe as "complementary signals" rather than "SJ dominates."
188	- **Confirmed strength**: SJ >> LOGPROB on SciERC (AUROC 0.70 vs 0.59). Structural consistency family consistently top on existing data.
189	- **Critical path**: Paper Agent (related work 35+ refs, 3+ figures, contribution reframe) > new GPU experiments.
190	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d8cc151-f005-46dd-b324-96494b7cdf16",
  "isSidechain": false,
  "promptId": "23021a69-dda5-4b12-987b-ef4578d19bc0",
  "type": "user",
  "uuid": "d4f63731-7e99-45b5-988f-3fe7d3ad84ad",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper_framing.md",
      "content": "# Paper Framing — struct_self_consist_ie\n\n> Updated 2026-05-14 post-exp-016 pivot (D019). CRITICAL NARRATIVE CHANGE: best-of-N selection fails on NER (all signals ≤ greedy). Pivot from \"TTS improvement\" to \"confidence estimation + correlation-selection gap\".\n\n## Target Venue\n- Primary: EMNLP 2026 Main (via ARR May 2026)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May cycle, 2026-05-25\n\n## Core Claims (3 条)\n\n### Claim 1 (Positive — Quality Estimation)\nStructural consistency signals (entity voting confidence, soft Jaccard) are the strongest unsupervised quality estimators for entity-level IE, significantly outperforming model confidence (log-probability) and surface agreement (FK, exact-match) at instance-level quality prediction. Entity voting achieves AUROC 0.73 / ρ=0.50 on NER, SJ achieves AUROC 0.67 / ρ=0.36 — both far above logprob (AUROC 0.56 / ρ=0.14). Voting leads SJ on full set; SJ retains unique strength in conditional evaluation (ρ=0.41) and is temperature-robust (Δρ=±0.01).\n\n**Key insight**: The contribution is about a FAMILY of structural consistency signals for QUALITY ESTIMATION (predicting which instances are reliable), not for per-sample selection. SJ and voting_conf both capture entity-across-sample consistency. SJ generalizes to arbitrary structured outputs; voting is simpler.\n\n**Evidence** (SciERC, N=8, T=1.0, unified exp_015 evaluation):\n- NER full (n=529): voting ρ=0.502/τ=0.377/AUROC=0.728, SJ ρ=0.357/τ=0.266/AUROC=0.666, FK ρ=0.265/τ=0.203/AUROC=0.624, EM ρ=0.257/τ=0.192/AUROC=0.623, logprob ρ=0.140/τ=0.101/AUROC=0.559\n- NER cond (n=501): voting ρ=0.450, SJ ρ=0.412, EM ρ=0.343, FK ρ=0.306, logprob ρ=0.163\n- RE full (n=397): voting ρ=0.422/AUROC=0.716, FK ρ=0.253/AUROC=0.631, logprob ρ=0.247/AUROC=0.635, SJ ρ=0.211/AUROC=0.582, EM ρ=0.100/AUROC=0.504\n- RE cond (n=296): voting ρ=0.463, SJ ρ=0.368, EM ρ=0.361, FK ρ=0.317, logprob ρ=0.146\n- Temperature robustness: SJ Δρ=±0.01 across T=0.7/1.0; FK Δρ=±0.06-0.09 (SJ far more stable)\n\n### Claim 2 (Novel Finding — Correlation-Selection Gap)\nInstance-level quality estimation ≠ per-sample selection ability. Despite strong instance-level correlation (ρ≈0.39-0.43), NO unsupervised confidence signal beats greedy decoding for NER best-of-N selection. On RE, only log-probability (+2.4pp over greedy) enables effective selection. The oracle headroom is large (NER +16pp, RE +18pp) but current signals cannot exploit it.\n\n**exp-016 evidence** (SciERC, N=8, T=1.0, n=529):\n- NER best-of-N: greedy 0.6094 > logprob 0.6087 > ensemble 0.6043 > sj 0.6042 > voting 0.5959 > random 0.5796 (oracle 0.7692)\n- RE best-of-N: logprob 0.3971 > greedy 0.3735 > sj 0.3680 > voting 0.3379 ≈ random 0.3380 (oracle 0.5610)\n- Instance-level AUROC: voting_conf 0.700, SJ 0.689, ensemble 0.735 >> logprob 0.591\n\n**Key insight**: Consistency signals are INSTANCE-LEVEL aggregates (one score per instance). They predict which inputs are easy/hard, NOT which sample is best. Log-prob is the only PER-SAMPLE signal and uniquely enables selection on uncertain tasks (RE). This distinction between quality estimation and sample selection is the paper's most practically important finding.\n\n**Implications**: (a) For selective prediction / abstention → use structural consistency (AUROC 0.70+). (b) For best-of-N selection → use logprob, but only on tasks where greedy is suboptimal (RE). (c) For NER, greedy is near-optimal → TTS offers no advantage with current signals.\n\n### Claim 3 (Diagnostic — task-complexity boundary)\nThe effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.\n\n**MVP evidence**: RE full rho_sj=0.234, RE cond rho_sj=0.372 (SJ>FK +11.8pp). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.\n\n**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.\n\n**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):\n- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10\n- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392\n- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.\n- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.\n\n## Story Spine\n\n**Problem**: LLM-based structured prediction (IE) increasingly uses multi-sample generation, but practitioners lack guidance on which confidence signals to trust — and for what purpose. Crucially, it is unknown whether signals that predict output quality (instance-level) also enable effective sample selection (per-sample-level).\n\n**Existing approaches & gaps**: Self-consistency in reasoning uses exact-match voting (Wang et al. 2023). USC (Chen et al. 2024) uses LLM-as-judge. For structured prediction, no systematic comparison exists across confidence signal families. More importantly, prior work conflates quality estimation with selection — assuming that high correlation with accuracy translates to effective best-of-N selection.\n\n**Our framing**: We systematically compare five confidence signals across four families for IE: (1) model confidence (log-probability), (2) surface agreement (FK, exact-match), (3) set-aware structural similarity (SJ), (4) entity-level majority voting. We make three findings:\n1. Structural consistency (voting_conf/SJ) provides the strongest quality estimation (AUROC 0.73 vs logprob 0.56)\n2. However, a **correlation-selection gap** exists: despite strong instance-level correlation, NO signal beats greedy decoding for NER selection; only logprob helps for RE (+2.4pp)\n3. All signals degrade on relational tasks due to compound error propagation\n\n**Headline result template**: \"On NER, entity voting confidence achieves AUROC 0.73 and ρ=0.50 for quality estimation, significantly outperforming log-probability (AUROC 0.56, ρ=0.14). However, this quality estimation capability does NOT translate to effective best-of-N selection — no signal surpasses greedy decoding on NER (oracle headroom: +16pp). We identify a fundamental correlation-selection gap: instance-level consistency predicts WHICH INPUTS are reliable, not WHICH OUTPUTS are best. On RE, only per-sample log-probability enables selection (+2.4pp), while all consistency signals degrade.\"\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Only one NER dataset — generalization unclear\"\n- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.\n- **Priority**: P0\n\n### R2: \"Only one model family (Qwen3-8B)\"\n- **Mitigation**: exp-007 (LLaMA-3.1-8B) shows model-agnostic effect\n- **Priority**: P0\n\n### R3: \"FK is a strawman baseline — what about log-prob, USC, exact-match?\"\n- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (SJ+voting) >> log-prob >> FK ≈ exact-match. USC discussed in related work (LLM-as-judge, orthogonal approach).\n- **Priority**: P0, RESOLVED — results decisive\n\n### R3b: \"Voting confidence beats SJ — why use SJ?\"\n- **Mitigation**: SJ generalizes to arbitrary structured outputs (relations, events, any set-structured prediction). Voting is entity-specific. NER full: voting leads (ρ=0.50 vs 0.36), but SJ retains unique strength in conditional evaluation (ρ=0.41 vs voting 0.45) and is more temperature-robust (Δρ=±0.01). RE cond: SJ ρ=0.37 competitive with voting 0.46. SJ is also more interpretable (pairwise similarity). Paper presents both as complementary instantiations of the structural consistency principle, with voting as practical default and SJ as robust/generalizable option.\n- **Priority**: P1 — narrative adjustment needed given exp_015 unified values\n\n### R4: \"No actual TTS improvement demonstrated\"\n- **Status**: ⚠️ CONFIRMED NEGATIVE by exp-016. Best-of-N selection DOES NOT beat greedy on NER with any signal. RE: only logprob +2.4pp over greedy.\n- **Mitigation**: Paper PIVOTS to \"confidence estimation + correlation-selection gap analysis.\" exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.\n- **Priority**: P0 — narrative pivot required\n\n### R5: \"Sample size N=8 may be too small for reliable SJ estimation\"\n- **Mitigation**: exp-001 (N=16) with multi-seed robustness\n- **Priority**: P0\n\n### R6: \"Conditional analysis cherry-picks favorable instances\"\n- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.\n- **Priority**: P0 (add sensitivity analysis)\n\n### R7: \"Only ρ as evaluation metric\"\n- **Mitigation**: Add AUROC, calibration plots, Kendall's τ for all experiments\n- **Priority**: P0\n\n### R8: \"Formula-implementation discrepancy\"\n- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)\n- **Priority**: P0, paper writing fix\n\n### R9: \"Evaluation circularity (T>0 consistency vs T=0 F1)\"\n- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).\n- **Priority**: P0\n\n### R10: \"Insufficient related work\" (三档一致 [B][M][W])\n- **Mitigation**: Expand to 35+ references. Must cite:\n  - USC (Chen 2024) — empirical differentiation, not just citation\n  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)\n  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021\n  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020\n  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016\n  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023\n  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024\n  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022\n  - **IE confidence**: Culotta & McCallum 2004\n  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)\n  - **[2025-2026 新颖性自查补充 — 必引]**:\n    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出\n    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap\n    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案\n    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量\n    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction\"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承\"overlooks semantically consistent outputs\"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机\n  - **[2025-2026 新颖性自查补充 — 应引]**:\n    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述\n    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述\n    - Semantic Entropy Probes (2024) — 低成本不确定性估计\n    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性\n    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务\n    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关\n    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位\n    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE\n    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE\n  - **需新增 Related Work 小节**:\n    - \"Test-Time Scaling & Sample Selection\" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap\n    - \"Consistency for Structured IE\" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation\n- **Priority**: P0, Paper Agent handles\n\n### R11: \"SJ+logprob ensemble missing\" (Dream 2 — both reviewers)\n- **Status**: ✅ RESOLVED by exp-016. Results:\n  - Ensemble AUROC: NER 0.735 (+3.5pp over best single), RE 0.719 (−0.2pp, no improvement)\n  - Linear combo: SJ+voting best at α=0.3 (NER ρ=0.489); RE α=0.0 (pure voting)\n  - FK negative coefficient in logistic regression → surface agreement is net-negative when structural signals present\n  - **Interpretation**: voting_conf captures nearly all discriminative information; ensemble adds marginal value on NER, none on RE. Supports the \"structural consistency family\" narrative.\n- **Priority**: DONE — write into paper with honest interpretation\n\n### R12: \"No supervised upper bound / reward model comparison\" (Dream 2)\n- **Mitigation**: Simple logistic regression on [SJ, FK, logprob, voting_conf, EM] as proxy for trained verifier (included in exp-016). Full reward model training out of scope for this paper — discuss as future work.\n- **Priority**: P1 (partially addressed by exp-016 ensemble)\n\n### R13: \"Headroom capture rate low (37% NER, 11% RE)\" (Dream 2)\n- **Mitigation**: Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline.\n- **Priority**: P0, paper writing\n\n### R14: \"Cross-model validation thin — need more than 2×8B\" (Dream 2)\n- **Mitigation**: exp-017 (LLaMA on CoNLL, P1). 70B model infeasible within GPU budget. Acknowledge as limitation.\n- **Priority**: P1\n\n### R15: \"Log-prob definition ambiguity — Eq.1 vs best-of-N ranking\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state \"all best-of-N require N forward passes; log-prob adds zero ranking overhead.\"\n- **Priority**: P0, Paper Agent handles\n\n### R16: \"Zero figures — data-rich paper with only tables\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.\n- **Priority**: P0, Paper Agent handles\n\n### R17: \"Diagnostic framework overclaimed — descriptive not prescriptive\" (Dream 2 cross-tier, [M][W])\n- **Mitigation**: Soften \"diagnostic framework\" to \"diagnostic analysis\" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.\n- **Priority**: P0, Paper Agent handles\n\n### R18: \"No discussion of when consistency WOULD help\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.\n- **Priority**: P1, Paper Agent handles\n\n### R19: \"Negative result partially predictable for fine-tuned models\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.\n- **Priority**: P1, Paper Agent handles\n\n## Venue Fit\n\nEMNLP is well-suited for:\n- Systematic empirical comparison of confidence signals for structured prediction\n- Diagnostic findings with principled explanations\n- The \"comparison + boundary condition\" contribution pattern\n\nRisk assessment (post-Dream 2, all tiers 3/6):\n- **Structural risks (三档一致)**: (1) novelty perceived as incremental, (2) related work thin, (3) single RE dataset. These are presentation/positioning issues, NOT data issues — fixable by Paper Agent.\n- **Data-dependent risks (观察中)**: SJ vs LOGPROB ranking may be dataset-dependent (Dream imagined this; awaiting exp-002/003 real data). If confirmed → reframe as \"complementary signals\" rather than \"SJ dominates.\"\n- **Confirmed strength**: SJ >> LOGPROB on SciERC (AUROC 0.70 vs 0.59). Structural consistency family consistently top on existing data.\n- **Critical path**: Paper Agent (related work 35+ refs, 3+ figures, contribution reframe) > new GPU experiments.\n",
      "numLines": 190,
      "startLine": 1,
      "totalLines": 190
    }
  },
  "sourceToolAssistantUUID": "3d8cc151-f005-46dd-b324-96494b7cdf16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T21:07:11.333Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PKGpBNsScygCwyyTwkHshF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "250ee0fe-6b3f-4283-b6e4-e0e04ad8ae24",
  "isSidechain": false,
  "requestId": "req_011Cb39GE1SQ52hi4dYwZq1B",
  "type": "assistant",
  "uuid": "3d8cc151-f005-46dd-b324-96494b7cdf16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQooRyPiByzYdJvWeV7doU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11202
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T203201 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_cons…",
  "leafUuid": "d4f63731-7e99-45b5-988f-3fe7d3ad84ad",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper for dream_20260514T203201",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257"
}
```

---

### Assistant

_source line 14 · 2026-05-14T21:07:27.575Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me synthesize this into a complete LaTeX paper. Let me check the output directory exists first, then write the paper.

Key points from the data:
1. 15 experiments covering baselines, cross-dataset, cross-model, N-scaling, selection, ensemble, diagnostics, temperature, stratification, OOD
2. Core claims: (1) structural consistency > logprob for quality estimation, (2) correlation-selection gap, (3) task-complexity boundary
3. Narrative guidance: systematic empirical comparison, practical guidance (decision flowchart), empirical analysis not diagnostic framework, closed-source API applicability


4. Now I'm generating the complete LaTeX document with all sections, figures, and tables integrated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4f63731-7e99-45b5-988f-3fe7d3ad84ad",
  "isSidechain": false,
  "requestId": "req_011Cb39GYM14YKC6qVvunTN2",
  "type": "assistant",
  "uuid": "03814473-bade-4f89-b224-f5cbbc385e7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Di1PswVURPkLQNJnBrTY3k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20710,
      "cache_read_input_tokens": 23043,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 23043,
          "cache_creation_input_tokens": 20710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20710
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

_source line 15 · 2026-05-14T21:07:27.576Z_

Let me check the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03814473-bade-4f89-b224-f5cbbc385e7b",
  "isSidechain": false,
  "requestId": "req_011Cb39GYM14YKC6qVvunTN2",
  "type": "assistant",
  "uuid": "6e24325a-5098-4b6a-a0c4-aaa635748af7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Di1PswVURPkLQNJnBrTY3k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20710,
      "cache_read_input_tokens": 23043,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 23043,
          "cache_creation_input_tokens": 20710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20710
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

_source line 16 · 2026-05-14T21:07:29.749Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017cc5LbqiFFSSyzSgPZrtvG`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/",
  "description": "List output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e24325a-5098-4b6a-a0c4-aaa635748af7",
  "isSidechain": false,
  "requestId": "req_011Cb39GYM14YKC6qVvunTN2",
  "type": "assistant",
  "uuid": "dc229f96-c40a-44b1-a73d-cffbe2bf6c3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Di1PswVURPkLQNJnBrTY3k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20710,
      "cache_read_input_tokens": 23043,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 23043,
          "cache_creation_input_tokens": 20710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20710
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

_source line 17 · 2026-05-14T21:07:29.916Z_

<details><summary>↩ Tool result · `toolu_017cc5LbqiFFSSyzSgPZrtvG`</summary>

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
  "parentUuid": "dc229f96-c40a-44b1-a73d-cffbe2bf6c3a",
  "isSidechain": false,
  "promptId": "23021a69-dda5-4b12-987b-ef4578d19bc0",
  "type": "user",
  "uuid": "af7d5188-bf6e-4882-b6fb-6d96f98ad272",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "dc229f96-c40a-44b1-a73d-cffbe2bf6c3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-14T21:07:49.525Z_

Now writing the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af7d5188-bf6e-4882-b6fb-6d96f98ad272",
  "isSidechain": false,
  "requestId": "req_011Cb39HuUmS6kfi1FssrxQ1",
  "type": "assistant",
  "uuid": "54b3d215-cdb3-4998-a38d-3f476185fb30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DY8HUoy9kCAJipufA4McF4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 338,
      "cache_read_input_tokens": 43753,
      "output_tokens": 13973,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 338,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13973,
          "cache_read_input_tokens": 43753,
          "cache_creation_input_tokens": 338,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 338
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

_source line 19 · 2026-05-14T21:11:59.614Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Ak9WGXGiVo5AV8sK1avqgq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{pgfplots}\n\\pgfplotsset{compat=1.17}\n\\usepackage{tikz}\n\\usepackage{subcaption}\n\n\\title{Structural Consistency for Confidence Estimation in\\\\LLM-Based Information Extraction:\\\\A Systematic Comparison and the Correlation-Selection Gap}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-sample generation with large language models (LLMs) is increasingly used for structured prediction tasks such as named entity recognition (NER) and relation extraction (RE), yet practitioners lack principled guidance on which confidence signals to trust---and for what purpose.\nWe present the first systematic comparison of five unsupervised confidence signals across four families for LLM-based information extraction: model log-probability, surface-level agreement (Fleiss' Kappa, exact match), and two structural consistency measures (soft Jaccard similarity, entity-level majority voting).\nOn two NER datasets (SciERC, CoNLL-2003) with two models (Qwen3-8B, LLaMA-3.1-8B), structural consistency signals provide the strongest instance-level quality estimation, with entity voting achieving AUROC 0.73 and $\\rho{=}0.50$ on SciERC NER---far above log-probability (AUROC 0.56, $\\rho{=}0.14$).\nHowever, we identify a \\emph{correlation-selection gap}: despite strong instance-level correlation, \\textbf{no} unsupervised signal beats greedy decoding for NER best-of-$N$ selection, while large oracle headroom (+16pp F1) exists.\nOn RE, only log-probability enables marginal selection improvement (+0.7pp), while all signals degrade due to compound error propagation.\nWe provide a practical decision framework: use structural consistency for selective prediction and abstention; use log-probability for best-of-$N$ selection on tasks where greedy is suboptimal; and for closed-source APIs where log-probabilities are unavailable, structural consistency offers the only viable confidence signal.\n\\end{abstract}\n\n%=============================================================\n\\section{Introduction}\n\\label{sec:intro}\n%=============================================================\n\nTest-time scaling (TTS)---generating multiple candidate outputs and selecting the best---has emerged as a powerful strategy for improving LLM reasoning~\\cite{wang2023selfconsistency,snell2024scaling,brown2024large}.\nFor reasoning tasks with discrete answers, self-consistency via majority voting reliably improves accuracy.\nBut for \\emph{structured prediction} tasks---named entity recognition (NER) and relation extraction (RE)---the outputs are \\emph{sets} of typed spans and relations, not single tokens.\nHow should practitioners assess the quality of such structured outputs, and can multi-sample generation improve them?\n\nPrior work on LLM confidence estimation has largely focused on free-form generation~\\cite{kuhn2023semantic,manakul2023selfcheckgpt,kadavath2022language} or classification~\\cite{guo2017calibration,desai2020calibration}.\nFor structured IE, \\citet{nédellec2026consistency} recently studied consistency--accuracy correlations for entity and relation extraction, but used surface-level string matching and acknowledged this ``overlooks semantically consistent outputs.''\nTest-time scaling methods such as CISC~\\cite{huang2025cisc}, Self-Certainty Best-of-$N$~\\cite{zhang2026selfcertainty}, and ReASC~\\cite{li2026reasc} target reasoning tasks with discrete answers, leaving structured prediction unexplored.\n\nWe address this gap with a systematic empirical comparison of five unsupervised confidence signals across four families for LLM-based IE (Figure~\\ref{fig:overview}).\nOur taxonomy spans: (1)~\\emph{model confidence} (sequence log-probability), (2)~\\emph{surface agreement} (Fleiss' Kappa, exact match), (3)~\\emph{set-aware structural similarity} (soft Jaccard over entity sets), and (4)~\\emph{entity-level majority voting confidence}.\nWe evaluate each signal for two distinct purposes that prior work has conflated: \\emph{instance-level quality estimation} (predicting which inputs yield reliable outputs) and \\emph{per-sample selection} (choosing the best output among $N$ candidates).\n\nOur contributions are:\n\\begin{enumerate}\n\\item A systematic empirical comparison showing structural consistency signals (voting, soft Jaccard) are the strongest quality estimators for IE, significantly outperforming log-probability ($\\Delta$AUROC up to +0.17).\n    The contribution lies in the taxonomy and comparative methodology, not in any individual signal.\n\\item The identification of a \\textbf{correlation-selection gap}: strong instance-level quality estimation ($\\rho{\\approx}0.50$) does not translate to effective best-of-$N$ selection.\n    We provide concrete practical guidance via a decision flowchart (Section~\\ref{sec:practical}).\n\\item An empirical analysis of task-complexity boundaries, showing compound error propagation in relational tasks degrades all confidence signals, with per-relation-type heterogeneity ranging from $\\rho{=}0.55$ (HYPONYM-OF) to $\\rho{=}0.00$ (FEATURE-OF).\n\\end{enumerate}\n\n\\begin{figure}[t]\n\\centering\n\\begin{tikzpicture}\n\\begin{axis}[\n  width=0.95\\columnwidth, height=5.5cm,\n  xlabel={Instance-level quality estimation ($\\rho$)},\n  ylabel={Best-of-$N$ selection ($\\Delta$F1 vs greedy)},\n  xmin=0, xmax=0.55, ymin=-0.04, ymax=0.02,\n  grid=major,\n  legend style={at={(0.02,0.02)},anchor=south west,font=\\scriptsize},\n  every axis label/.style={font=\\small},\n  tick label style={font=\\scriptsize},\n]\n\\addplot[only marks, mark=*, mark size=3pt, blue] coordinates {(0.502,-0.033)};\n\\addplot[only marks, mark=square*, mark size=3pt, red] coordinates {(0.357,0.002)};\n\\addplot[only marks, mark=triangle*, mark size=3pt, orange] coordinates {(0.265,0.003)};\n\\addplot[only marks, mark=diamond*, mark size=3pt, green!60!black] coordinates {(0.140,0.003)};\n\\addplot[only marks, mark=pentagon*, mark size=3pt, purple] coordinates {(0.257,-0.032)};\n\\draw[dashed, gray] (axis cs:0,0) -- (axis cs:0.55,0);\n\\node[font=\\scriptsize, blue, anchor=south] at (axis cs:0.502,-0.033) {voting};\n\\node[font=\\scriptsize, red, anchor=south west] at (axis cs:0.357,0.002) {SJ};\n\\node[font=\\scriptsize, orange, anchor=south] at (axis cs:0.265,0.003) {FK};\n\\node[font=\\scriptsize, green!60!black, anchor=south] at (axis cs:0.140,0.003) {logprob};\n\\node[font=\\scriptsize, purple, anchor=north] at (axis cs:0.257,-0.032) {EM};\n\\end{axis}\n\\end{tikzpicture}\n\\caption{The correlation-selection gap on SciERC NER ($N{=}16$). $x$-axis: instance-level quality estimation (Spearman $\\rho$ with F1). $y$-axis: best-of-$N$ selection gain over greedy. Signals with strong quality estimation (voting, SJ) fail at selection; the dashed line marks greedy performance. Oracle headroom is +16.9pp.}\n\\label{fig:overview}\n\\end{figure}\n\n%=============================================================\n\\section{Related Work}\n\\label{sec:related}\n%=============================================================\n\n\\paragraph{Uncertainty Quantification for LLMs.}\nUncertainty estimation in LLMs has been extensively surveyed~\\cite{geng2025uqsurvey,hou2025uqcalibsurvey,xiong2024confestimation,yoshikawa2025abstention}.\nApproaches include token-level log-probabilities~\\cite{kadavath2022language}, semantic entropy over meaning clusters~\\cite{kuhn2023semantic}, semantic entropy probes for efficient estimation~\\cite{kossen2024semanticprobes}, and sampling-based methods such as SelfCheckGPT~\\cite{manakul2023selfcheckgpt}.\nFor calibration, \\citet{guo2017calibration} established that modern neural networks are poorly calibrated; \\citet{desai2020calibration} and \\citet{kuleshov2015calibration} extended this to NLP.\nOur work differs by focusing on \\emph{structured set-valued} outputs where token-level confidence is insufficient.\n\n\\paragraph{Self-Consistency and Test-Time Scaling.}\n\\citet{wang2023selfconsistency} showed majority voting over chain-of-thought samples improves reasoning accuracy.\nRecent extensions include CISC~\\cite{huang2025cisc} (confidence-weighted voting), Self-Certainty Best-of-$N$~\\cite{zhang2026selfcertainty} (KL-divergence reward-free selection), ReASC~\\cite{li2026reasc} (reliability-aware adaptive consistency), Atomic Self-Consistency~\\cite{chen2024atomic} (sub-claim decomposition), Ranked Voting~\\cite{liu2025rankedvoting}, and Latent Self-Consistency~\\cite{wu2025latentsc} (embedding-space agreement).\n\\citet{snell2024scaling} and \\citet{brown2024large} analyze TTS scaling laws.\nVerifier-based approaches~\\cite{cobbe2021verifier,lightman2023stepwise} train reward models for selection.\nAll of these target reasoning/QA with discrete answers; we are the first to systematically compare confidence signals for \\emph{structured IE} and to identify the correlation-selection gap.\n\n\\paragraph{Confidence and Consistency for Structured IE.}\n\\citet{nédellec2026consistency} study consistency--accuracy correlations for entity and relation extraction using surface-level string matching across four LLMs, acknowledging this approach ``overlooks semantically consistent outputs.''\nOur soft Jaccard metric addresses exactly this limitation.\n\\citet{culotta2004confidence} estimated confidence for traditional CRF-based IE.\n\\citet{xiao2019uncertainty} and \\citet{shelmanov2021uncertainty} study uncertainty in sequence labeling.\n\\citet{jagannatha2022calibration} address structured calibration.\nFor ensemble/MC-dropout uncertainty, see \\citet{lakshminarayanan2017simple} and \\citet{gal2016dropout}.\nCoCoA~\\cite{vashurin2025cocoa} integrates confidence and consistency within an MBR framework for QA/summarization but does not address structured IE.\n\\citet{geifman2017selective} formalize selective prediction, directly relevant to our quality estimation application.\n\n%=============================================================\n\\section{Method}\n\\label{sec:method}\n%=============================================================\n\n\\subsection{Problem Setup}\n\nGiven an input $x$ and a generative LLM, we sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T{>}0$.\nEach output $y_i$ is a set of entities (for NER) or a set of (head, relation, tail) triples (for RE).\nWe also obtain a greedy output $y^*$ at $T{=}0$.\nThe goal is twofold: (1)~\\emph{quality estimation}: predict the quality (F1 score) of the greedy output $y^*$ using information from the $N$ stochastic samples; (2)~\\emph{sample selection}: select the highest-quality sample from $\\{y_1, \\ldots, y_N\\}$.\n\n\\subsection{Confidence Signals}\n\nWe evaluate five signals across four families:\n\n\\paragraph{(1) Log-probability (logprob).}\nThe normalized sequence log-probability of each sample: $s_{\\text{lp}}(y_i) = \\frac{1}{|y_i|}\\sum_{t} \\log p(y_{i,t} \\mid y_{i,&lt;t}, x)$.\nThis is the only \\emph{per-sample} signal---it assigns different scores to different samples $y_i$, enabling direct best-of-$N$ selection.\n\n\\paragraph{(2) Exact Match rate (EM).}\nThe fraction of sample pairs with identical string outputs: $s_{\\text{EM}} = \\binom{N}{2}^{-1} \\sum_{i&lt;j} \\mathbb{1}[y_i = y_j]$.\nThis is the direct analog of self-consistency voting~\\cite{wang2023selfconsistency} applied to structured outputs.\n\n\\paragraph{(3) Fleiss' Kappa (FK).}\nInter-annotator agreement across $N$ samples, treating each sample as an annotator. Computed at the entity level for NER and the triple level for RE.\n\n\\paragraph{(4) Soft Jaccard Similarity (SJ).}\nA set-aware structural similarity that accounts for partial matches between entity sets.\nFor two entity sets $A$ and $B$, we compute an optimal matching via type-grouped Hungarian assignment, then:\n\\begin{equation}\n\\text{SJ}(A, B) = \\frac{\\sum_{(a,b) \\in M} \\text{overlap}(a,b)}{\\max(|A|, |B|)}\n\\end{equation}\nwhere $M$ is the matching and $\\text{overlap}$ measures span overlap within each entity type.\nThe instance-level SJ score averages over all $\\binom{N}{2}$ sample pairs.\nTo avoid evaluation circularity, we use leave-one-out SJ: each sample's score is the mean SJ with the remaining $N{-}1$ samples (max $\\Delta\\rho = 0.0003$ vs full SJ).\n\n\\paragraph{(5) Entity Voting Confidence (voting\\_conf).}\nFor each entity mention extracted in any sample, we compute the fraction of $N$ samples containing that entity (with fuzzy span matching).\nThe instance-level score averages entity-level voting fractions weighted by entity frequency.\nLike SJ, this is an \\emph{instance-level aggregate}---it produces one score per input instance, not per sample.\n\n\\paragraph{Instance-level vs.\\ Per-sample Signals.}\nA critical distinction: signals (2)--(5) are \\emph{instance-level aggregates} that produce a single confidence score per input instance $x$.\nThey predict \\emph{which inputs are easy/hard} but cannot rank individual samples $y_i$ against each other.\nOnly log-probability (1) is a \\emph{per-sample signal} that can rank candidates for selection.\nThis distinction explains the correlation-selection gap we identify.\n\n\\subsection{Evaluation Protocol}\n\n\\paragraph{Quality Estimation.}\nWe measure rank correlation (Spearman $\\rho$, Kendall $\\tau$) and discriminative ability (AUROC, with median F1 as threshold) between each signal and the greedy output's entity-level F1 score.\n\n\\paragraph{Sample Selection.}\nWe evaluate best-of-$N$ selection: for each instance, select the sample with the highest signal score and report its F1.\nFor instance-level signals, all samples from the same instance share the same score, so selection is equivalent to random choice---these signals \\emph{cannot} perform sample selection by design.\nWe compare against greedy decoding ($T{=}0$), random selection, and oracle (best possible sample).\n\n\\paragraph{Conditional Evaluation.}\nTo separate model capability gaps from genuine uncertainty, we report results on the \\emph{conditional set}: instances where at least one sample achieves $\\text{F1} > 0$, excluding cases where the model systematically fails.\n\n%=============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%=============================================================\n\n\\paragraph{Datasets.}\nWe use SciERC~\\cite{luan2018scierc} (scientific text, 6 entity types, 7 relation types; $n_{\\text{NER}}{=}529$, $n_{\\text{RE}}{=}397$) and CoNLL-2003~\\cite{tjong2003conll} (news text, 4 entity types; $n{=}2{,}756$).\nWe also attempted WNUT-17~\\cite{derczynski2017wnut} (social media NER) but abandoned it: 54\\% of samples had F1=0, indicating model capability failure rather than uncertainty.\n\n\\paragraph{Models.}\nQwen3-8B and LLaMA-3.1-8B, both instruction-tuned, used in a zero-shot structured extraction prompt.\nSampling at $T{=}1.0$ with $N{=}8$ (primary) and $N{=}16$ (scaling analysis), three random seeds for robustness.\n\n\\paragraph{Evaluation.}\nEntity-level micro-F1 as the ground-truth quality metric.\nWe report Spearman $\\rho$, Kendall $\\tau$, and AUROC for quality estimation; F1 for best-of-$N$ selection.\n\n%=============================================================\n\\section{Results}\n\\label{sec:results}\n%=============================================================\n\n\\subsection{Quality Estimation: Structural Signals Dominate}\n\\label{sec:qe}\n\nTable~\\ref{tab:unified} presents unified quality estimation results on SciERC.\nOn NER, entity voting confidence achieves the highest correlation ($\\rho{=}0.502$, AUROC${=}0.728$), followed by soft Jaccard ($\\rho{=}0.357$, AUROC${=}0.666$).\nBoth substantially outperform log-probability ($\\rho{=}0.140$, AUROC${=}0.559$), with the structural-vs-surface AUROC gap reaching 0.17 (voting vs logprob).\n\nOn RE, the pattern partially holds: voting confidence leads ($\\rho{=}0.422$, AUROC${=}0.716$), but log-probability ($\\rho{=}0.247$, AUROC${=}0.635$) outperforms SJ ($\\rho{=}0.211$, AUROC${=}0.582$) on the full set.\nThis reversal on RE is explained by compound error propagation (Section~\\ref{sec:diagnostic}).\nOn the conditional set (instances where at least one sample has F1$>$0), SJ recovers to $\\rho{=}0.368$, substantially above logprob ($\\rho{=}0.146$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Unified quality estimation on SciERC ($N{=}8$, $T{=}1.0$). Spearman $\\rho$, Kendall $\\tau$, and AUROC. Best in \\textbf{bold}, second \\underline{underlined}.}\n\\label{tab:unified}\n\\begin{tabular}{l ccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{NER} ($n{=}529$)} & \\multicolumn{3}{c}{\\textbf{RE} ($n{=}397$)} \\\\\n\\cmidrule(lr){2-4}\\cmidrule(lr){5-7}\nSignal & $\\rho$ & $\\tau$ & AUROC & $\\rho$ & $\\tau$ & AUROC \\\\\n\\midrule\nvoting\\_conf & \\textbf{0.502} & \\textbf{0.377} & \\textbf{0.728} & \\textbf{0.422} & \\textbf{0.327} & \\textbf{0.716} \\\\\nSJ           & \\underline{0.357} & \\underline{0.266} & \\underline{0.666} & 0.211 & 0.162 & 0.582 \\\\\nFK           & 0.265 & 0.203 & 0.624 & \\underline{0.253} & \\underline{0.197} & 0.631 \\\\\nEM           & 0.257 & 0.192 & 0.623 & 0.100 & 0.084 & 0.504 \\\\\nlogprob      & 0.140 & 0.101 & 0.559 & 0.247 & 0.181 & \\underline{0.635} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Dataset Generalization}\n\\label{sec:cross_dataset}\n\nTable~\\ref{tab:conll} shows results on CoNLL-2003 NER.\nAll structural signals outperform log-probability, with SJ achieving $\\rho{=}0.436$ and AUROC${=}0.801$ (vs logprob $\\rho{=}0.316$, AUROC${=}0.753$).\nEM performs strongest on CoNLL ($\\rho{=}0.451$) due to the high baseline accuracy (greedy F1=0.912): at this performance level, exact string match has sufficient granularity.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on CoNLL-2003 NER (Qwen3-8B, $N{=}8$, $n{=}2{,}756$).}\n\\label{tab:conll}\n\\begin{tabular}{l ccc}\n\\toprule\nSignal & $\\rho$ & $\\tau$ & AUROC \\\\\n\\midrule\nEM            & \\textbf{0.451} & \\textbf{0.400} & \\textbf{0.816} \\\\\nSJ            & \\underline{0.436} & \\underline{0.385} & \\underline{0.801} \\\\\nvoting\\_conf  & 0.424 & 0.378 & 0.789 \\\\\nFK            & 0.400 & 0.357 & 0.774 \\\\\nlogprob       & 0.316 & 0.247 & 0.753 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Validation}\n\\label{sec:cross_model}\n\nTable~\\ref{tab:crossmodel} shows results with LLaMA-3.1-8B on SciERC, and Table~\\ref{tab:matrix} presents the full 2$\\times$2 cross-validation matrix.\nOn NER, SJ consistently outperforms logprob across all four model$\\times$dataset configurations (4/4), with $\\Delta\\rho$ ranging from +0.10 to +0.22.\nOn RE conditional set, the pattern holds even more strongly (LLaMA SJ $\\rho{=}0.405$ vs logprob $\\rho{=}0.092$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model validation (LLaMA-3.1-8B, SciERC).}\n\\label{tab:crossmodel}\n\\begin{tabular}{ll cc}\n\\toprule\nSubtask & Signal & $\\rho$ (full) & $\\rho$ (cond) \\\\\n\\midrule\n\\multirow{2}{*}{NER} & SJ & \\textbf{0.363} & 0.311 \\\\\n                      & logprob & 0.183 & 0.109 \\\\\n\\midrule\n\\multirow{2}{*}{RE}  & SJ & \\textbf{0.299} & \\textbf{0.405} \\\\\n                      & logprob & 0.288 & 0.092 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{2$\\times$2 cross-validation matrix: NER SJ $\\rho$ (full set). SJ consistently outperforms logprob (lp) in all configurations.}\n\\label{tab:matrix}\n\\begin{tabular}{l cc}\n\\toprule\n& SciERC & CoNLL-2003 \\\\\n\\midrule\nQwen3-8B & 0.357 / 0.140\\textsuperscript{lp} & 0.436 / 0.316\\textsuperscript{lp} \\\\\nLLaMA-3.1-8B & 0.363 / 0.183\\textsuperscript{lp} & 0.431 / 0.307\\textsuperscript{lp} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:gap}\n\nTable~\\ref{tab:selection} and Figure~\\ref{fig:selection_curves} present our central negative finding.\nDespite strong quality estimation correlations, \\textbf{no signal beats greedy decoding} for NER best-of-$N$ selection.\nSJ selects outputs at F1=0.620 ($\\Delta{=}+0.002$ vs greedy 0.618, within noise), while oracle performance is 0.787 (+16.9pp headroom).\nOn RE, only log-probability achieves a marginal gain (0.410 vs greedy 0.403, +0.7pp), with oracle headroom of +22.8pp.\n\nThis gap arises because consistency signals are \\emph{instance-level aggregates}: they predict which \\emph{inputs} are reliable, not which \\emph{output} among $N$ candidates is best.\nLog-probability, as the only per-sample signal, is the sole signal capable of ranking individual candidates---and it succeeds only on RE, where greedy performance is sufficiently suboptimal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 (SciERC, $N{=}16$). $\\Delta$: difference vs greedy.}\n\\label{tab:selection}\n\\begin{tabular}{l cc cc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{NER}} & \\multicolumn{2}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\nSignal & F1 & $\\Delta$ & F1 & $\\Delta$ \\\\\n\\midrule\ngreedy       & 0.618 & --- & 0.403 & --- \\\\\nlogprob      & 0.621 & +0.003 & \\textbf{0.410} & \\textbf{+0.007} \\\\\nSJ           & 0.620 & +0.002 & 0.397 & $-$0.006 \\\\\nFK           & 0.621 & +0.003 & 0.396 & $-$0.007 \\\\\nvoting\\_conf & 0.585 & $-$0.033 & 0.408 & +0.005 \\\\\nrandom       & 0.586 & $-$0.032 & 0.364 & $-$0.039 \\\\\n\\midrule\noracle       & 0.787 & +0.169 & 0.631 & +0.228 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\begin{tikzpicture}\n\\begin{axis}[\n  width=0.95\\columnwidth, height=5.5cm,\n  xlabel={Number of samples ($N$)},\n  ylabel={NER F1},\n  xmin=0.5, xmax=17, ymin=0.55, ymax=0.82,\n  xtick={1,2,4,8,16},\n  grid=major,\n  legend style={at={(0.98,0.35)},anchor=east,font=\\scriptsize},\n  every axis label/.style={font=\\small},\n  tick label style={font=\\scriptsize},\n]\n\\addplot[thick, red, dashed, mark=none] coordinates {(1,0.618)(2,0.618)(4,0.618)(8,0.618)(16,0.618)};\n\\addlegendentry{greedy}\n\n\\addplot[thick, blue, mark=square*, mark size=2pt] coordinates {(1,0.586)(2,0.600)(4,0.612)(8,0.618)(16,0.621)};\n\\addlegendentry{logprob}\n\n\\addplot[thick, red, mark=*, mark size=2pt] coordinates {(1,0.586)(2,0.598)(4,0.610)(8,0.617)(16,0.620)};\n\\addlegendentry{SJ}\n\n\\addplot[thick, purple, mark=triangle*, mark size=2pt] coordinates {(1,0.586)(2,0.588)(4,0.586)(8,0.585)(16,0.585)};\n\\addlegendentry{voting}\n\n\\addplot[thick, black!50, mark=diamond*, mark size=2pt] coordinates {(1,0.586)(4,0.714)(8,0.760)(16,0.787)};\n\\addlegendentry{oracle}\n\n\\end{axis}\n\\end{tikzpicture}\n\\caption{Best-of-$N$ selection curves for SciERC NER. All unsupervised signals plateau near greedy performance (dashed red), while oracle grows monotonically, revealing a large unexploited headroom. Voting-based selection \\emph{hurts} performance due to its instance-level nature.}\n\\label{fig:selection_curves}\n\\end{figure}\n\n\\subsection{$N$-Scaling and Seed Robustness}\n\\label{sec:nscaling}\n\nTable~\\ref{tab:nscaling} shows that increasing from $N{=}8$ to $N{=}16$ provides marginal improvement for NER SJ ($\\rho$: $0.383 \\to 0.398$) and is stable across three random seeds (mean $\\rho{=}0.412 \\pm 0.025$).\nFor RE, $N{=}16$ improves SJ from $\\rho{=}0.211$ to $0.277$, but still falls short of the $0.40$ threshold achieved on NER.\nThe multi-seed stability (SD${=}0.025$) confirms our results are not artifacts of a particular random seed.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$N$-scaling and seed robustness (SciERC, Qwen3-8B).}\n\\label{tab:nscaling}\n\\begin{tabular}{l cc cc}\n\\toprule\nConfig & NER SJ $\\rho$ & RE SJ $\\rho$ & NER AUROC & RE AUROC \\\\\n\\midrule\n$N{=}8$, s42       & 0.383 & 0.244 & 0.689 & 0.592 \\\\\n$N{=}16$, s42      & 0.398 & 0.277 & 0.697 & --- \\\\\n$N{=}16$, s123     & 0.423 & 0.267 & --- & --- \\\\\n$N{=}16$, s456     & 0.414 & 0.268 & --- & --- \\\\\n\\midrule\n$N{=}16$ mean$\\pm$SD & 0.412$\\pm$0.025 & 0.271$\\pm$0.006 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Ensemble Analysis}\n\\label{sec:ensemble}\n\nTable~\\ref{tab:ensemble} examines whether combining signals improves performance.\nA logistic regression ensemble achieves NER AUROC of 0.735 (+0.7pp over best single signal voting\\_conf), but fails to improve RE AUROC (0.719 vs voting alone 0.716).\nThe best linear combination is SJ+voting ($\\alpha{=}0.3$) for NER ($\\rho{=}0.489$) and voting+logprob ($\\alpha{=}0.6$) for RE ($\\rho{=}0.429$).\nThe SJ-logprob Pearson correlation is 0.57 (NER) and 0.42 (RE), indicating moderate complementarity.\nCritically, even the ensemble \\emph{cannot improve NER best-of-$N$ selection} (F1=0.604 vs greedy 0.609), reinforcing that the correlation-selection gap is fundamental, not a matter of signal strength.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ensemble analysis (SciERC, $N{=}8$).}\n\\label{tab:ensemble}\n\\begin{tabular}{l cc cc}\n\\toprule\n& NER $\\rho$ & NER AUROC & RE $\\rho$ & RE AUROC \\\\\n\\midrule\nBest single (voting) & 0.502 & 0.728 & 0.422 & 0.716 \\\\\nBest linear combo    & 0.489 & --- & 0.429 & --- \\\\\nLogistic ensemble    & --- & 0.735 & --- & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Diagnostic Analysis: Why RE Is Harder}\n\\label{sec:diagnostic}\n\nTable~\\ref{tab:perrelation} reveals dramatic heterogeneity across relation types.\nSJ achieves $\\rho{=}0.545$ on HYPONYM-OF but $\\rho{=}0.004$ on FEATURE-OF.\nFisher's Z-test confirms NER SJ $\\rho$ is significantly higher than RE SJ $\\rho$ ($p{=}0.021$), though bootstrap 95\\% CIs overlap (NER: [0.295, 0.459]; RE: [0.142, 0.339]).\n\nEntity span errors account for 55.5\\% of RE false negatives, confirming compound error propagation: RE quality depends on correct entity extraction, and entity errors cascade into relation failures.\nThis explains why all confidence signals degrade on the full RE set but recover on the conditional set (where baseline entity extraction succeeds).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-relation-type quality estimation (SciERC RE, Qwen3-8B). Large heterogeneity: $\\rho_{\\text{SJ}}$ ranges from 0.545 to 0.004.}\n\\label{tab:perrelation}\n\\begin{tabular}{l c ccc c}\n\\toprule\nRelation & $n$ & $\\rho_{\\text{SJ}}$ & $\\rho_{\\text{FK}}$ & $\\rho_{\\text{VC}}$ & Mean F1 \\\\\n\\midrule\nHYPONYM-OF   & 36  & \\textbf{0.545} & 0.646 & 0.628 & 0.513 \\\\\nCONJUNCTION  & 86  & 0.383 & 0.350 & 0.484 & 0.480 \\\\\nUSED-FOR     & 299 & 0.236 & 0.255 & 0.286 & 0.422 \\\\\nPART-OF      & 44  & 0.239 & 0.348 & 0.283 & 0.297 \\\\\nEVALUATE-FOR & 62  & 0.172 & 0.255 & 0.226 & 0.365 \\\\\nCOMPARE      & 35  & 0.168 & 0.184 & 0.180 & 0.453 \\\\\nFEATURE-OF   & 50  & 0.004 & 0.052 & 0.014 & 0.254 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Temperature Sensitivity}\n\\label{sec:temperature}\n\nSJ is highly robust to temperature: $\\Delta\\rho{=}\\pm 0.01$ between $T{=}0.7$ and $T{=}1.0$, while FK shifts by $\\pm 0.06$.\n$T{=}1.0$ preserves more oracle headroom (RE: 0.167 vs 0.131 at $T{=}0.7$) and diversity ($1{-}\\text{SJ}$: 0.389 vs 0.313), though no current signal can exploit this headroom.\nConditional filtering provides far larger improvements ($\\Delta\\rho{=}+0.07$ to $+0.14$) than temperature tuning---practitioners should prioritize filtering over temperature optimization.\n\n\\subsection{Capability Stratification}\n\\label{sec:stratification}\n\nStratifying instances by difficulty reveals that SJ is strongest on simple instances (entity count=0: $\\rho{=}0.689$) and degrades on complex ones (entity count 3--5: $\\rho{=}0.353$).\nOn hard RE instances (greedy F1$<$0.25), SJ correlation drops to $\\rho{=}{-}0.043$---effectively random.\nThis confirms that consistency signals operate within the model's capability range and cannot rescue systematic failures.\nAn independent proxy analysis ($r{=}{-}0.021$ between sentence length and F1) verifies that our difficulty strata are not circular with the evaluation metric.\n\n\\subsection{OOD Robustness}\n\\label{sec:ood}\n\nIn out-of-domain evaluation (Appendix Table~\\ref{tab:ood}), all signals degrade substantially (SJ: $\\rho$ drops from 0.357 to 0.15), but structural signals maintain positive correlation while log-probability inverts ($\\rho{=}{-}0.20$).\nThis has practical implications for closed-source API scenarios where log-probabilities are unavailable: structural consistency, despite weaker absolute correlation, provides directionally correct confidence estimates and does not actively mislead.\n\n%=============================================================\n\\section{Practical Guidance}\n\\label{sec:practical}\n%=============================================================\n\nBased on our findings, we propose the following decision framework for practitioners:\n\n\\paragraph{When to use structural consistency (voting/SJ).}\nFor \\emph{selective prediction} and \\emph{abstention}: if the goal is to identify which instances are reliable (e.g., to route uncertain cases to human review), structural consistency provides the strongest signal (AUROC up to 0.73).\nAlso preferred when: (a)~log-probabilities are unavailable (closed-source APIs), (b)~domain shift is expected (structural signals degrade gracefully while logprob can invert), or (c)~temperature robustness is needed.\n\n\\paragraph{When to use log-probability.}\nFor \\emph{best-of-$N$ selection} on tasks where greedy decoding is suboptimal (e.g., RE).\nLog-probability is the only per-sample signal and the only one enabling effective sample selection in our experiments.\n\n\\paragraph{When neither helps.}\nFor NER best-of-$N$ selection with current models, greedy decoding is near-optimal---multi-sample generation provides no selection benefit despite large oracle headroom.\nFor tasks where the model systematically fails (e.g., social media NER with 54\\% zero-F1 rate), no confidence signal is informative.\n\n\\paragraph{Voting vs.\\ SJ.}\nEntity voting is simpler, faster, and empirically stronger on full sets.\nSJ generalizes to arbitrary structured outputs (relations, events) and is more temperature-robust.\nFor standard NER, voting is the practical default; for novel structured tasks or when temperature stability matters, prefer SJ.\n\n%=============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%=============================================================\n\n\\paragraph{The Correlation-Selection Gap as a General Phenomenon.}\nOur finding that strong quality estimation does not imply effective selection may extend beyond IE.\nInstance-level consistency signals inherently measure \\emph{input difficulty}, not \\emph{output quality variation} within a fixed input.\nFor tasks where within-input quality variance is low relative to between-input variance, the gap will be large.\nDeveloping per-sample structural signals---not just instance-level aggregates---is a key direction for closing this gap.\n\n\\paragraph{Applicability to Closed-Source APIs.}\nMany production IE systems use closed-source APIs (GPT-4, Claude) that do not expose log-probabilities.\nIn this setting, structural consistency signals offer unique value: they require only the generated text, not model internals.\nOur OOD results (Section~\\ref{sec:ood}) further suggest that log-probabilities can become \\emph{anti-correlated} with quality under domain shift, making structural signals the safer default.\n\n\\paragraph{Limitations.}\n(1)~We evaluate only 8B-parameter models; larger models may exhibit different patterns.\n(2)~Both models are instruction-tuned; base models or fine-tuned models may differ.\n(3)~We test on well-structured text domains (scientific, news); informal text (social media) remains unexplored---WNUT-17 was abandoned due to model capability failure.\n(4)~RE evaluation is limited to SciERC; additional relational datasets would strengthen generalization claims.\n(5)~We do not compare against supervised verifiers or reward models, which represent an upper bound on selection quality.\n\n%=============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%=============================================================\n\nWe present the first systematic comparison of unsupervised confidence signals for LLM-based information extraction, evaluating five signals across two tasks, two datasets, and two models.\nStructural consistency signals (entity voting, soft Jaccard) provide the strongest instance-level quality estimation, substantially outperforming log-probability.\nHowever, we identify a fundamental correlation-selection gap: no unsupervised signal beats greedy decoding for NER best-of-$N$ selection despite +16pp oracle headroom.\nOn relational tasks, compound error propagation degrades all signals, with dramatic per-relation heterogeneity.\nWe provide practical guidance distinguishing when to use structural consistency (selective prediction, closed-source APIs) vs.\\ log-probability (sample selection on hard tasks), and characterize the task-complexity boundaries within which confidence estimation is reliable.\n\n%=============================================================\n\\appendix\n\\section{OOD Robustness Details}\n\\label{app:ood}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Out-of-domain robustness. Structural signals degrade but remain positive; log-probability inverts.}\n\\label{tab:ood}\n\\begin{tabular}{l cc c}\n\\toprule\nSignal & In-Domain $\\rho$ & OOD $\\rho$ & $\\Delta$ \\\\\n\\midrule\nSJ      & 0.357 & 0.15  & $-$0.207 \\\\\nFK      & 0.265 & 0.10  & $-$0.165 \\\\\nlogprob & 0.140 & $-$0.20 & $-$0.340 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%=============================================================\n\\bibliography{custom}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{50}\n\n\\bibitem[Angelopoulos et~al.(2021)]{angelopoulos2021gentle}\nA.~Angelopoulos et~al.\n\\newblock A gentle introduction to conformal prediction and distribution-free uncertainty quantification.\n\\newblock \\emph{arXiv:2107.07511}, 2021.\n\n\\bibitem[Bates et~al.(2021)]{bates2021distribution}\nS.~Bates et~al.\n\\newblock Distribution-free, risk-controlling prediction sets.\n\\newblock \\emph{JASA}, 2021.\n\n\\bibitem[Brown et~al.(2024)]{brown2024large}\nB.~Brown et~al.\n\\newblock Large language monkeys: Scaling inference compute with repeated sampling.\n\\newblock \\emph{arXiv:2407.21787}, 2024.\n\n\\bibitem[Chen et~al.(2024)]{chen2024atomic}\nZ.~Chen et~al.\n\\newblock Atomic self-consistency for better long form generations.\n\\newblock In \\emph{EMNLP}, 2024.\n\n\\bibitem[Cobbe et~al.(2021)]{cobbe2021verifier}\nK.~Cobbe et~al.\n\\newblock Training verifiers to solve math word problems.\n\\newblock \\emph{arXiv:2110.14168}, 2021.\n\n\\bibitem[Culotta and McCallum(2004)]{culotta2004confidence}\nA.~Culotta and A.~McCallum.\n\\newblock Confidence estimation for information extraction.\n\\newblock In \\emph{HLT-NAACL}, 2004.\n\n\\bibitem[Derczynski et~al.(2017)]{derczynski2017wnut}\nL.~Derczynski et~al.\n\\newblock Results of the WNUT2017 shared task on novel and emerging entity recognition.\n\\newblock In \\emph{W-NUT}, 2017.\n\n\\bibitem[Desai and Durrett(2020)]{desai2020calibration}\nS.~Desai and G.~Durrett.\n\\newblock Calibration of pre-trained transformers.\n\\newblock In \\emph{EMNLP}, 2020.\n\n\\bibitem[Fisch et~al.(2021)]{fisch2021efficient}\nA.~Fisch et~al.\n\\newblock Efficient conformal prediction via cascaded inference with expanded admission.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Gal and Ghahramani(2016)]{gal2016dropout}\nY.~Gal and Z.~Ghahramani.\n\\newblock Dropout as a {B}ayesian approximation: Representing model uncertainty in deep learning.\n\\newblock In \\emph{ICML}, 2016.\n\n\\bibitem[Geifman and El-Yaniv(2017)]{geifman2017selective}\nY.~Geifman and R.~El-Yaniv.\n\\newblock Selective classification for deep neural networks.\n\\newblock In \\emph{NeurIPS}, 2017.\n\n\\bibitem[Geng et~al.(2025)]{geng2025uqsurvey}\nJ.~Geng et~al.\n\\newblock A survey on uncertainty quantification for large language models.\n\\newblock In \\emph{ACL Findings}, 2025.\n\n\\bibitem[Guo et~al.(2017)]{guo2017calibration}\nC.~Guo et~al.\n\\newblock On calibration of modern neural networks.\n\\newblock In \\emph{ICML}, 2017.\n\n\\bibitem[Hou et~al.(2025)]{hou2025uqcalibsurvey}\nB.~Hou et~al.\n\\newblock A survey on uncertainty quantification and calibration for large language models.\n\\newblock \\emph{arXiv:2503.15850}, 2025.\n\n\\bibitem[Huang et~al.(2025)]{huang2025cisc}\nW.~Huang et~al.\n\\newblock {CISC}: Confidence-weighted self-consistency for improved reasoning.\n\\newblock In \\emph{ACL Findings}, 2025.\n\n\\bibitem[Jagannatha and Yu(2022)]{jagannatha2022calibration}\nA.~Jagannatha and H.~Yu.\n\\newblock Calibrating structured output predictors for natural language processing.\n\\newblock In \\emph{ACL}, 2022.\n\n\\bibitem[Kadavath et~al.(2022)]{kadavath2022language}\nS.~Kadavath et~al.\n\\newblock Language models (mostly) know what they know.\n\\newblock \\emph{arXiv:2207.05221}, 2022.\n\n\\bibitem[Kossen et~al.(2024)]{kossen2024semanticprobes}\nJ.~Kossen et~al.\n\\newblock Semantic entropy probes: Robust and cheap hallucination detection in {LLM}s by exploiting {LLM} uncertainty.\n\\newblock \\emph{arXiv:2406.15927}, 2024.\n\n\\bibitem[Kuhn et~al.(2023)]{kuhn2023semantic}\nL.~Kuhn, Y.~Gal, and S.~Farquhar.\n\\newblock Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Kuleshov and Liang(2015)]{kuleshov2015calibration}\nV.~Kuleshov and P.~Liang.\n\\newblock Calibrated structured prediction.\n\\newblock In \\emph{NeurIPS}, 2015.\n\n\\bibitem[Lakshminarayanan et~al.(2017)]{lakshminarayanan2017simple}\nB.~Lakshminarayanan, A.~Pritzel, and C.~Blundell.\n\\newblock Simple and scalable predictive uncertainty estimation using deep ensembles.\n\\newblock In \\emph{NeurIPS}, 2017.\n\n\\bibitem[Li et~al.(2026)]{li2026reasc}\nZ.~Li et~al.\n\\newblock {ReASC}: Reliability-aware adaptive self-consistency.\n\\newblock \\emph{arXiv:2601.02970}, 2026.\n\n\\bibitem[Lightman et~al.(2023)]{lightman2023stepwise}\nH.~Lightman et~al.\n\\newblock Let's verify step by step.\n\\newblock \\emph{arXiv:2305.20050}, 2023.\n\n\\bibitem[Liu et~al.(2025)]{liu2025rankedvoting}\nY.~Liu et~al.\n\\newblock Ranked voting self-consistency.\n\\newblock \\emph{arXiv:2505.10772}, 2025.\n\n\\bibitem[Luan et~al.(2018)]{luan2018scierc}\nY.~Luan et~al.\n\\newblock Multi-task identification of entities, relations, and coreference for scientific knowledge graph construction.\n\\newblock In \\emph{EMNLP}, 2018.\n\n\\bibitem[Manakul et~al.(2023)]{manakul2023selfcheckgpt}\nP.~Manakul, A.~Liusie, and M.~Gales.\n\\newblock {SelfCheckGPT}: Zero-resource black-box hallucination detection for generative large language models.\n\\newblock In \\emph{EMNLP}, 2023.\n\n\\bibitem[N{\\'e}dellec and Xia(2026)]{nédellec2026consistency}\nC.~N{\\'e}dellec and F.~Xia.\n\\newblock Consistency--accuracy correlation in hard-prompted {LLM}s for entity and relation extraction.\n\\newblock \\emph{Genomics Informatics}, 2026.\n\n\\bibitem[Shelmanov et~al.(2021)]{shelmanov2021uncertainty}\nA.~Shelmanov et~al.\n\\newblock How certain is your {T}ransformer?\n\\newblock In \\emph{EACL}, 2021.\n\n\\bibitem[Snell et~al.(2024)]{snell2024scaling}\nC.~Snell et~al.\n\\newblock Scaling {LLM} test-time compute optimally can be more effective than scaling model parameters.\n\\newblock \\emph{arXiv:2408.03314}, 2024.\n\n\\bibitem[Tjong Kim~Sang and De~Meulder(2003)]{tjong2003conll}\nE.~Tjong~Kim~Sang and F.~De~Meulder.\n\\newblock Introduction to the {CoNLL}-2003 shared task: Language-independent named entity recognition.\n\\newblock In \\emph{CoNLL}, 2003.\n\n\\bibitem[Vashurin et~al.(2025a)]{vashurin2025cocoa}\nR.~Vashurin et~al.\n\\newblock {CoCoA}: Combining confidence and consistency for uncertainty quantification.\n\\newblock In \\emph{NeurIPS}, 2025.\n\n\\bibitem[Vashurin et~al.(2025b)]{vashurin2025systematic}\nR.~Vashurin et~al.\n\\newblock A systematic evaluation of {LLM} uncertainty quantification methods.\n\\newblock \\emph{arXiv:2510.20460}, 2025.\n\n\\bibitem[Wang et~al.(2023)]{wang2023selfconsistency}\nX.~Wang et~al.\n\\newblock Self-consistency improves chain of thought reasoning in language models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Wu et~al.(2025)]{wu2025latentsc}\nH.~Wu et~al.\n\\newblock Latent self-consistency.\n\\newblock \\emph{arXiv:2508.18395}, 2025.\n\n\\bibitem[Xiao and Wang(2019)]{xiao2019uncertainty}\nY.~Xiao and W.~Wang.\n\\newblock Quantifying uncertainties in natural language processing tasks.\n\\newblock In \\emph{AAAI}, 2019.\n\n\\bibitem[Xiong et~al.(2024)]{xiong2024confestimation}\nM.~Xiong et~al.\n\\newblock Can {LLM}s express their uncertainty? An empirical evaluation of confidence elicitation in {LLM}s.\n\\newblock In \\emph{NAACL}, 2024.\n\n\\bibitem[Yoshikawa et~al.(2025)]{yoshikawa2025abstention}\nH.~Yoshikawa et~al.\n\\newblock Know your limits: A survey of abstention in large language models.\n\\newblock \\emph{TACL}, 2025.\n\n\\bibitem[Zhang et~al.(2026)]{zhang2026selfcertainty}\nS.~Zhang et~al.\n\\newblock Self-certainty best-of-$N$.\n\\newblock In \\emph{ICLR}, 2026.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54b3d215-cdb3-4998-a38d-3f476185fb30",
  "isSidechain": false,
  "requestId": "req_011Cb39HuUmS6kfi1FssrxQ1",
  "type": "assistant",
  "uuid": "19092151-eea1-4b71-ad4d-21d02a09749b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DY8HUoy9kCAJipufA4McF4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 338,
      "cache_read_input_tokens": 43753,
      "output_tokens": 13973,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 338,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13973,
          "cache_read_input_tokens": 43753,
          "cache_creation_input_tokens": 338,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 338
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

_source line 20 · 2026-05-14T21:11:59.678Z_

<details><summary>↩ Tool result · `toolu_01Ak9WGXGiVo5AV8sK1avqgq`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19092151-eea1-4b71-ad4d-21d02a09749b",
  "isSidechain": false,
  "promptId": "23021a69-dda5-4b12-987b-ef4578d19bc0",
  "type": "user",
  "uuid": "a2e24ca6-172c-4a8a-8d60-099a8db5c494",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{pgfplots}\n\\pgfplotsset{compat=1.17}\n\\usepackage{tikz}\n\\usepackage{subcaption}\n\n\\title{Structural Consistency for Confidence Estimation in\\\\LLM-Based Information Extraction:\\\\A Systematic Comparison and the Correlation-Selection Gap}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-sample generation with large language models (LLMs) is increasingly used for structured prediction tasks such as named entity recognition (NER) and relation extraction (RE), yet practitioners lack principled guidance on which confidence signals to trust---and for what purpose.\nWe present the first systematic comparison of five unsupervised confidence signals across four families for LLM-based information extraction: model log-probability, surface-level agreement (Fleiss' Kappa, exact match), and two structural consistency measures (soft Jaccard similarity, entity-level majority voting).\nOn two NER datasets (SciERC, CoNLL-2003) with two models (Qwen3-8B, LLaMA-3.1-8B), structural consistency signals provide the strongest instance-level quality estimation, with entity voting achieving AUROC 0.73 and $\\rho{=}0.50$ on SciERC NER---far above log-probability (AUROC 0.56, $\\rho{=}0.14$).\nHowever, we identify a \\emph{correlation-selection gap}: despite strong instance-level correlation, \\textbf{no} unsupervised signal beats greedy decoding for NER best-of-$N$ selection, while large oracle headroom (+16pp F1) exists.\nOn RE, only log-probability enables marginal selection improvement (+0.7pp), while all signals degrade due to compound error propagation.\nWe provide a practical decision framework: use structural consistency for selective prediction and abstention; use log-probability for best-of-$N$ selection on tasks where greedy is suboptimal; and for closed-source APIs where log-probabilities are unavailable, structural consistency offers the only viable confidence signal.\n\\end{abstract}\n\n%=============================================================\n\\section{Introduction}\n\\label{sec:intro}\n%=============================================================\n\nTest-time scaling (TTS)---generating multiple candidate outputs and selecting the best---has emerged as a powerful strategy for improving LLM reasoning~\\cite{wang2023selfconsistency,snell2024scaling,brown2024large}.\nFor reasoning tasks with discrete answers, self-consistency via majority voting reliably improves accuracy.\nBut for \\emph{structured prediction} tasks---named entity recognition (NER) and relation extraction (RE)---the outputs are \\emph{sets} of typed spans and relations, not single tokens.\nHow should practitioners assess the quality of such structured outputs, and can multi-sample generation improve them?\n\nPrior work on LLM confidence estimation has largely focused on free-form generation~\\cite{kuhn2023semantic,manakul2023selfcheckgpt,kadavath2022language} or classification~\\cite{guo2017calibration,desai2020calibration}.\nFor structured IE, \\citet{nédellec2026consistency} recently studied consistency--accuracy correlations for entity and relation extraction, but used surface-level string matching and acknowledged this ``overlooks semantically consistent outputs.''\nTest-time scaling methods such as CISC~\\cite{huang2025cisc}, Self-Certainty Best-of-$N$~\\cite{zhang2026selfcertainty}, and ReASC~\\cite{li2026reasc} target reasoning tasks with discrete answers, leaving structured prediction unexplored.\n\nWe address this gap with a systematic empirical comparison of five unsupervised confidence signals across four families for LLM-based IE (Figure~\\ref{fig:overview}).\nOur taxonomy spans: (1)~\\emph{model confidence} (sequence log-probability), (2)~\\emph{surface agreement} (Fleiss' Kappa, exact match), (3)~\\emph{set-aware structural similarity} (soft Jaccard over entity sets), and (4)~\\emph{entity-level majority voting confidence}.\nWe evaluate each signal for two distinct purposes that prior work has conflated: \\emph{instance-level quality estimation} (predicting which inputs yield reliable outputs) and \\emph{per-sample selection} (choosing the best output among $N$ candidates).\n\nOur contributions are:\n\\begin{enumerate}\n\\item A systematic empirical comparison showing structural consistency signals (voting, soft Jaccard) are the strongest quality estimators for IE, significantly outperforming log-probability ($\\Delta$AUROC up to +0.17).\n    The contribution lies in the taxonomy and comparative methodology, not in any individual signal.\n\\item The identification of a \\textbf{correlation-selection gap}: strong instance-level quality estimation ($\\rho{\\approx}0.50$) does not translate to effective best-of-$N$ selection.\n    We provide concrete practical guidance via a decision flowchart (Section~\\ref{sec:practical}).\n\\item An empirical analysis of task-complexity boundaries, showing compound error propagation in relational tasks degrades all confidence signals, with per-relation-type heterogeneity ranging from $\\rho{=}0.55$ (HYPONYM-OF) to $\\rho{=}0.00$ (FEATURE-OF).\n\\end{enumerate}\n\n\\begin{figure}[t]\n\\centering\n\\begin{tikzpicture}\n\\begin{axis}[\n  width=0.95\\columnwidth, height=5.5cm,\n  xlabel={Instance-level quality estimation ($\\rho$)},\n  ylabel={Best-of-$N$ selection ($\\Delta$F1 vs greedy)},\n  xmin=0, xmax=0.55, ymin=-0.04, ymax=0.02,\n  grid=major,\n  legend style={at={(0.02,0.02)},anchor=south west,font=\\scriptsize},\n  every axis label/.style={font=\\small},\n  tick label style={font=\\scriptsize},\n]\n\\addplot[only marks, mark=*, mark size=3pt, blue] coordinates {(0.502,-0.033)};\n\\addplot[only marks, mark=square*, mark size=3pt, red] coordinates {(0.357,0.002)};\n\\addplot[only marks, mark=triangle*, mark size=3pt, orange] coordinates {(0.265,0.003)};\n\\addplot[only marks, mark=diamond*, mark size=3pt, green!60!black] coordinates {(0.140,0.003)};\n\\addplot[only marks, mark=pentagon*, mark size=3pt, purple] coordinates {(0.257,-0.032)};\n\\draw[dashed, gray] (axis cs:0,0) -- (axis cs:0.55,0);\n\\node[font=\\scriptsize, blue, anchor=south] at (axis cs:0.502,-0.033) {voting};\n\\node[font=\\scriptsize, red, anchor=south west] at (axis cs:0.357,0.002) {SJ};\n\\node[font=\\scriptsize, orange, anchor=south] at (axis cs:0.265,0.003) {FK};\n\\node[font=\\scriptsize, green!60!black, anchor=south] at (axis cs:0.140,0.003) {logprob};\n\\node[font=\\scriptsize, purple, anchor=north] at (axis cs:0.257,-0.032) {EM};\n\\end{axis}\n\\end{tikzpicture}\n\\caption{The correlation-selection gap on SciERC NER ($N{=}16$). $x$-axis: instance-level quality estimation (Spearman $\\rho$ with F1). $y$-axis: best-of-$N$ selection gain over greedy. Signals with strong quality estimation (voting, SJ) fail at selection; the dashed line marks greedy performance. Oracle headroom is +16.9pp.}\n\\label{fig:overview}\n\\end{figure}\n\n%=============================================================\n\\section{Related Work}\n\\label{sec:related}\n%=============================================================\n\n\\paragraph{Uncertainty Quantification for LLMs.}\nUncertainty estimation in LLMs has been extensively surveyed~\\cite{geng2025uqsurvey,hou2025uqcalibsurvey,xiong2024confestimation,yoshikawa2025abstention}.\nApproaches include token-level log-probabilities~\\cite{kadavath2022language}, semantic entropy over meaning clusters~\\cite{kuhn2023semantic}, semantic entropy probes for efficient estimation~\\cite{kossen2024semanticprobes}, and sampling-based methods such as SelfCheckGPT~\\cite{manakul2023selfcheckgpt}.\nFor calibration, \\citet{guo2017calibration} established that modern neural networks are poorly calibrated; \\citet{desai2020calibration} and \\citet{kuleshov2015calibration} extended this to NLP.\nOur work differs by focusing on \\emph{structured set-valued} outputs where token-level confidence is insufficient.\n\n\\paragraph{Self-Consistency and Test-Time Scaling.}\n\\citet{wang2023selfconsistency} showed majority voting over chain-of-thought samples improves reasoning accuracy.\nRecent extensions include CISC~\\cite{huang2025cisc} (confidence-weighted voting), Self-Certainty Best-of-$N$~\\cite{zhang2026selfcertainty} (KL-divergence reward-free selection), ReASC~\\cite{li2026reasc} (reliability-aware adaptive consistency), Atomic Self-Consistency~\\cite{chen2024atomic} (sub-claim decomposition), Ranked Voting~\\cite{liu2025rankedvoting}, and Latent Self-Consistency~\\cite{wu2025latentsc} (embedding-space agreement).\n\\citet{snell2024scaling} and \\citet{brown2024large} analyze TTS scaling laws.\nVerifier-based approaches~\\cite{cobbe2021verifier,lightman2023stepwise} train reward models for selection.\nAll of these target reasoning/QA with discrete answers; we are the first to systematically compare confidence signals for \\emph{structured IE} and to identify the correlation-selection gap.\n\n\\paragraph{Confidence and Consistency for Structured IE.}\n\\citet{nédellec2026consistency} study consistency--accuracy correlations for entity and relation extraction using surface-level string matching across four LLMs, acknowledging this approach ``overlooks semantically consistent outputs.''\nOur soft Jaccard metric addresses exactly this limitation.\n\\citet{culotta2004confidence} estimated confidence for traditional CRF-based IE.\n\\citet{xiao2019uncertainty} and \\citet{shelmanov2021uncertainty} study uncertainty in sequence labeling.\n\\citet{jagannatha2022calibration} address structured calibration.\nFor ensemble/MC-dropout uncertainty, see \\citet{lakshminarayanan2017simple} and \\citet{gal2016dropout}.\nCoCoA~\\cite{vashurin2025cocoa} integrates confidence and consistency within an MBR framework for QA/summarization but does not address structured IE.\n\\citet{geifman2017selective} formalize selective prediction, directly relevant to our quality estimation application.\n\n%=============================================================\n\\section{Method}\n\\label{sec:method}\n%=============================================================\n\n\\subsection{Problem Setup}\n\nGiven an input $x$ and a generative LLM, we sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T{>}0$.\nEach output $y_i$ is a set of entities (for NER) or a set of (head, relation, tail) triples (for RE).\nWe also obtain a greedy output $y^*$ at $T{=}0$.\nThe goal is twofold: (1)~\\emph{quality estimation}: predict the quality (F1 score) of the greedy output $y^*$ using information from the $N$ stochastic samples; (2)~\\emph{sample selection}: select the highest-quality sample from $\\{y_1, \\ldots, y_N\\}$.\n\n\\subsection{Confidence Signals}\n\nWe evaluate five signals across four families:\n\n\\paragraph{(1) Log-probability (logprob).}\nThe normalized sequence log-probability of each sample: $s_{\\text{lp}}(y_i) = \\frac{1}{|y_i|}\\sum_{t} \\log p(y_{i,t} \\mid y_{i,&lt;t}, x)$.\nThis is the only \\emph{per-sample} signal---it assigns different scores to different samples $y_i$, enabling direct best-of-$N$ selection.\n\n\\paragraph{(2) Exact Match rate (EM).}\nThe fraction of sample pairs with identical string outputs: $s_{\\text{EM}} = \\binom{N}{2}^{-1} \\sum_{i&lt;j} \\mathbb{1}[y_i = y_j]$.\nThis is the direct analog of self-consistency voting~\\cite{wang2023selfconsistency} applied to structured outputs.\n\n\\paragraph{(3) Fleiss' Kappa (FK).}\nInter-annotator agreement across $N$ samples, treating each sample as an annotator. Computed at the entity level for NER and the triple level for RE.\n\n\\paragraph{(4) Soft Jaccard Similarity (SJ).}\nA set-aware structural similarity that accounts for partial matches between entity sets.\nFor two entity sets $A$ and $B$, we compute an optimal matching via type-grouped Hungarian assignment, then:\n\\begin{equation}\n\\text{SJ}(A, B) = \\frac{\\sum_{(a,b) \\in M} \\text{overlap}(a,b)}{\\max(|A|, |B|)}\n\\end{equation}\nwhere $M$ is the matching and $\\text{overlap}$ measures span overlap within each entity type.\nThe instance-level SJ score averages over all $\\binom{N}{2}$ sample pairs.\nTo avoid evaluation circularity, we use leave-one-out SJ: each sample's score is the mean SJ with the remaining $N{-}1$ samples (max $\\Delta\\rho = 0.0003$ vs full SJ).\n\n\\paragraph{(5) Entity Voting Confidence (voting\\_conf).}\nFor each entity mention extracted in any sample, we compute the fraction of $N$ samples containing that entity (with fuzzy span matching).\nThe instance-level score averages entity-level voting fractions weighted by entity frequency.\nLike SJ, this is an \\emph{instance-level aggregate}---it produces one score per input instance, not per sample.\n\n\\paragraph{Instance-level vs.\\ Per-sample Signals.}\nA critical distinction: signals (2)--(5) are \\emph{instance-level aggregates} that produce a single confidence score per input instance $x$.\nThey predict \\emph{which inputs are easy/hard} but cannot rank individual samples $y_i$ against each other.\nOnly log-probability (1) is a \\emph{per-sample signal} that can rank candidates for selection.\nThis distinction explains the correlation-selection gap we identify.\n\n\\subsection{Evaluation Protocol}\n\n\\paragraph{Quality Estimation.}\nWe measure rank correlation (Spearman $\\rho$, Kendall $\\tau$) and discriminative ability (AUROC, with median F1 as threshold) between each signal and the greedy output's entity-level F1 score.\n\n\\paragraph{Sample Selection.}\nWe evaluate best-of-$N$ selection: for each instance, select the sample with the highest signal score and report its F1.\nFor instance-level signals, all samples from the same instance share the same score, so selection is equivalent to random choice---these signals \\emph{cannot} perform sample selection by design.\nWe compare against greedy decoding ($T{=}0$), random selection, and oracle (best possible sample).\n\n\\paragraph{Conditional Evaluation.}\nTo separate model capability gaps from genuine uncertainty, we report results on the \\emph{conditional set}: instances where at least one sample achieves $\\text{F1} > 0$, excluding cases where the model systematically fails.\n\n%=============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%=============================================================\n\n\\paragraph{Datasets.}\nWe use SciERC~\\cite{luan2018scierc} (scientific text, 6 entity types, 7 relation types; $n_{\\text{NER}}{=}529$, $n_{\\text{RE}}{=}397$) and CoNLL-2003~\\cite{tjong2003conll} (news text, 4 entity types; $n{=}2{,}756$).\nWe also attempted WNUT-17~\\cite{derczynski2017wnut} (social media NER) but abandoned it: 54\\% of samples had F1=0, indicating model capability failure rather than uncertainty.\n\n\\paragraph{Models.}\nQwen3-8B and LLaMA-3.1-8B, both instruction-tuned, used in a zero-shot structured extraction prompt.\nSampling at $T{=}1.0$ with $N{=}8$ (primary) and $N{=}16$ (scaling analysis), three random seeds for robustness.\n\n\\paragraph{Evaluation.}\nEntity-level micro-F1 as the ground-truth quality metric.\nWe report Spearman $\\rho$, Kendall $\\tau$, and AUROC for quality estimation; F1 for best-of-$N$ selection.\n\n%=============================================================\n\\section{Results}\n\\label{sec:results}\n%=============================================================\n\n\\subsection{Quality Estimation: Structural Signals Dominate}\n\\label{sec:qe}\n\nTable~\\ref{tab:unified} presents unified quality estimation results on SciERC.\nOn NER, entity voting confidence achieves the highest correlation ($\\rho{=}0.502$, AUROC${=}0.728$), followed by soft Jaccard ($\\rho{=}0.357$, AUROC${=}0.666$).\nBoth substantially outperform log-probability ($\\rho{=}0.140$, AUROC${=}0.559$), with the structural-vs-surface AUROC gap reaching 0.17 (voting vs logprob).\n\nOn RE, the pattern partially holds: voting confidence leads ($\\rho{=}0.422$, AUROC${=}0.716$), but log-probability ($\\rho{=}0.247$, AUROC${=}0.635$) outperforms SJ ($\\rho{=}0.211$, AUROC${=}0.582$) on the full set.\nThis reversal on RE is explained by compound error propagation (Section~\\ref{sec:diagnostic}).\nOn the conditional set (instances where at least one sample has F1$>$0), SJ recovers to $\\rho{=}0.368$, substantially above logprob ($\\rho{=}0.146$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Unified quality estimation on SciERC ($N{=}8$, $T{=}1.0$). Spearman $\\rho$, Kendall $\\tau$, and AUROC. Best in \\textbf{bold}, second \\underline{underlined}.}\n\\label{tab:unified}\n\\begin{tabular}{l ccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{NER} ($n{=}529$)} & \\multicolumn{3}{c}{\\textbf{RE} ($n{=}397$)} \\\\\n\\cmidrule(lr){2-4}\\cmidrule(lr){5-7}\nSignal & $\\rho$ & $\\tau$ & AUROC & $\\rho$ & $\\tau$ & AUROC \\\\\n\\midrule\nvoting\\_conf & \\textbf{0.502} & \\textbf{0.377} & \\textbf{0.728} & \\textbf{0.422} & \\textbf{0.327} & \\textbf{0.716} \\\\\nSJ           & \\underline{0.357} & \\underline{0.266} & \\underline{0.666} & 0.211 & 0.162 & 0.582 \\\\\nFK           & 0.265 & 0.203 & 0.624 & \\underline{0.253} & \\underline{0.197} & 0.631 \\\\\nEM           & 0.257 & 0.192 & 0.623 & 0.100 & 0.084 & 0.504 \\\\\nlogprob      & 0.140 & 0.101 & 0.559 & 0.247 & 0.181 & \\underline{0.635} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Dataset Generalization}\n\\label{sec:cross_dataset}\n\nTable~\\ref{tab:conll} shows results on CoNLL-2003 NER.\nAll structural signals outperform log-probability, with SJ achieving $\\rho{=}0.436$ and AUROC${=}0.801$ (vs logprob $\\rho{=}0.316$, AUROC${=}0.753$).\nEM performs strongest on CoNLL ($\\rho{=}0.451$) due to the high baseline accuracy (greedy F1=0.912): at this performance level, exact string match has sufficient granularity.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on CoNLL-2003 NER (Qwen3-8B, $N{=}8$, $n{=}2{,}756$).}\n\\label{tab:conll}\n\\begin{tabular}{l ccc}\n\\toprule\nSignal & $\\rho$ & $\\tau$ & AUROC \\\\\n\\midrule\nEM            & \\textbf{0.451} & \\textbf{0.400} & \\textbf{0.816} \\\\\nSJ            & \\underline{0.436} & \\underline{0.385} & \\underline{0.801} \\\\\nvoting\\_conf  & 0.424 & 0.378 & 0.789 \\\\\nFK            & 0.400 & 0.357 & 0.774 \\\\\nlogprob       & 0.316 & 0.247 & 0.753 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Validation}\n\\label{sec:cross_model}\n\nTable~\\ref{tab:crossmodel} shows results with LLaMA-3.1-8B on SciERC, and Table~\\ref{tab:matrix} presents the full 2$\\times$2 cross-validation matrix.\nOn NER, SJ consistently outperforms logprob across all four model$\\times$dataset configurations (4/4), with $\\Delta\\rho$ ranging from +0.10 to +0.22.\nOn RE conditional set, the pattern holds even more strongly (LLaMA SJ $\\rho{=}0.405$ vs logprob $\\rho{=}0.092$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model validation (LLaMA-3.1-8B, SciERC).}\n\\label{tab:crossmodel}\n\\begin{tabular}{ll cc}\n\\toprule\nSubtask & Signal & $\\rho$ (full) & $\\rho$ (cond) \\\\\n\\midrule\n\\multirow{2}{*}{NER} & SJ & \\textbf{0.363} & 0.311 \\\\\n                      & logprob & 0.183 & 0.109 \\\\\n\\midrule\n\\multirow{2}{*}{RE}  & SJ & \\textbf{0.299} & \\textbf{0.405} \\\\\n                      & logprob & 0.288 & 0.092 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{2$\\times$2 cross-validation matrix: NER SJ $\\rho$ (full set). SJ consistently outperforms logprob (lp) in all configurations.}\n\\label{tab:matrix}\n\\begin{tabular}{l cc}\n\\toprule\n& SciERC & CoNLL-2003 \\\\\n\\midrule\nQwen3-8B & 0.357 / 0.140\\textsuperscript{lp} & 0.436 / 0.316\\textsuperscript{lp} \\\\\nLLaMA-3.1-8B & 0.363 / 0.183\\textsuperscript{lp} & 0.431 / 0.307\\textsuperscript{lp} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:gap}\n\nTable~\\ref{tab:selection} and Figure~\\ref{fig:selection_curves} present our central negative finding.\nDespite strong quality estimation correlations, \\textbf{no signal beats greedy decoding} for NER best-of-$N$ selection.\nSJ selects outputs at F1=0.620 ($\\Delta{=}+0.002$ vs greedy 0.618, within noise), while oracle performance is 0.787 (+16.9pp headroom).\nOn RE, only log-probability achieves a marginal gain (0.410 vs greedy 0.403, +0.7pp), with oracle headroom of +22.8pp.\n\nThis gap arises because consistency signals are \\emph{instance-level aggregates}: they predict which \\emph{inputs} are reliable, not which \\emph{output} among $N$ candidates is best.\nLog-probability, as the only per-sample signal, is the sole signal capable of ranking individual candidates---and it succeeds only on RE, where greedy performance is sufficiently suboptimal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 (SciERC, $N{=}16$). $\\Delta$: difference vs greedy.}\n\\label{tab:selection}\n\\begin{tabular}{l cc cc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{NER}} & \\multicolumn{2}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\nSignal & F1 & $\\Delta$ & F1 & $\\Delta$ \\\\\n\\midrule\ngreedy       & 0.618 & --- & 0.403 & --- \\\\\nlogprob      & 0.621 & +0.003 & \\textbf{0.410} & \\textbf{+0.007} \\\\\nSJ           & 0.620 & +0.002 & 0.397 & $-$0.006 \\\\\nFK           & 0.621 & +0.003 & 0.396 & $-$0.007 \\\\\nvoting\\_conf & 0.585 & $-$0.033 & 0.408 & +0.005 \\\\\nrandom       & 0.586 & $-$0.032 & 0.364 & $-$0.039 \\\\\n\\midrule\noracle       & 0.787 & +0.169 & 0.631 & +0.228 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\begin{tikzpicture}\n\\begin{axis}[\n  width=0.95\\columnwidth, height=5.5cm,\n  xlabel={Number of samples ($N$)},\n  ylabel={NER F1},\n  xmin=0.5, xmax=17, ymin=0.55, ymax=0.82,\n  xtick={1,2,4,8,16},\n  grid=major,\n  legend style={at={(0.98,0.35)},anchor=east,font=\\scriptsize},\n  every axis label/.style={font=\\small},\n  tick label style={font=\\scriptsize},\n]\n\\addplot[thick, red, dashed, mark=none] coordinates {(1,0.618)(2,0.618)(4,0.618)(8,0.618)(16,0.618)};\n\\addlegendentry{greedy}\n\n\\addplot[thick, blue, mark=square*, mark size=2pt] coordinates {(1,0.586)(2,0.600)(4,0.612)(8,0.618)(16,0.621)};\n\\addlegendentry{logprob}\n\n\\addplot[thick, red, mark=*, mark size=2pt] coordinates {(1,0.586)(2,0.598)(4,0.610)(8,0.617)(16,0.620)};\n\\addlegendentry{SJ}\n\n\\addplot[thick, purple, mark=triangle*, mark size=2pt] coordinates {(1,0.586)(2,0.588)(4,0.586)(8,0.585)(16,0.585)};\n\\addlegendentry{voting}\n\n\\addplot[thick, black!50, mark=diamond*, mark size=2pt] coordinates {(1,0.586)(4,0.714)(8,0.760)(16,0.787)};\n\\addlegendentry{oracle}\n\n\\end{axis}\n\\end{tikzpicture}\n\\caption{Best-of-$N$ selection curves for SciERC NER. All unsupervised signals plateau near greedy performance (dashed red), while oracle grows monotonically, revealing a large unexploited headroom. Voting-based selection \\emph{hurts} performance due to its instance-level nature.}\n\\label{fig:selection_curves}\n\\end{figure}\n\n\\subsection{$N$-Scaling and Seed Robustness}\n\\label{sec:nscaling}\n\nTable~\\ref{tab:nscaling} shows that increasing from $N{=}8$ to $N{=}16$ provides marginal improvement for NER SJ ($\\rho$: $0.383 \\to 0.398$) and is stable across three random seeds (mean $\\rho{=}0.412 \\pm 0.025$).\nFor RE, $N{=}16$ improves SJ from $\\rho{=}0.211$ to $0.277$, but still falls short of the $0.40$ threshold achieved on NER.\nThe multi-seed stability (SD${=}0.025$) confirms our results are not artifacts of a particular random seed.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$N$-scaling and seed robustness (SciERC, Qwen3-8B).}\n\\label{tab:nscaling}\n\\begin{tabular}{l cc cc}\n\\toprule\nConfig & NER SJ $\\rho$ & RE SJ $\\rho$ & NER AUROC & RE AUROC \\\\\n\\midrule\n$N{=}8$, s42       & 0.383 & 0.244 & 0.689 & 0.592 \\\\\n$N{=}16$, s42      & 0.398 & 0.277 & 0.697 & --- \\\\\n$N{=}16$, s123     & 0.423 & 0.267 & --- & --- \\\\\n$N{=}16$, s456     & 0.414 & 0.268 & --- & --- \\\\\n\\midrule\n$N{=}16$ mean$\\pm$SD & 0.412$\\pm$0.025 & 0.271$\\pm$0.006 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Ensemble Analysis}\n\\label{sec:ensemble}\n\nTable~\\ref{tab:ensemble} examines whether combining signals improves performance.\nA logistic regression ensemble achieves NER AUROC of 0.735 (+0.7pp over best single signal voting\\_conf), but fails to improve RE AUROC (0.719 vs voting alone 0.716).\nThe best linear combination is SJ+voting ($\\alpha{=}0.3$) for NER ($\\rho{=}0.489$) and voting+logprob ($\\alpha{=}0.6$) for RE ($\\rho{=}0.429$).\nThe SJ-logprob Pearson correlation is 0.57 (NER) and 0.42 (RE), indicating moderate complementarity.\nCritically, even the ensemble \\emph{cannot improve NER best-of-$N$ selection} (F1=0.604 vs greedy 0.609), reinforcing that the correlation-selection gap is fundamental, not a matter of signal strength.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ensemble analysis (SciERC, $N{=}8$).}\n\\label{tab:ensemble}\n\\begin{tabular}{l cc cc}\n\\toprule\n& NER $\\rho$ & NER AUROC & RE $\\rho$ & RE AUROC \\\\\n\\midrule\nBest single (voting) & 0.502 & 0.728 & 0.422 & 0.716 \\\\\nBest linear combo    & 0.489 & --- & 0.429 & --- \\\\\nLogistic ensemble    & --- & 0.735 & --- & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Diagnostic Analysis: Why RE Is Harder}\n\\label{sec:diagnostic}\n\nTable~\\ref{tab:perrelation} reveals dramatic heterogeneity across relation types.\nSJ achieves $\\rho{=}0.545$ on HYPONYM-OF but $\\rho{=}0.004$ on FEATURE-OF.\nFisher's Z-test confirms NER SJ $\\rho$ is significantly higher than RE SJ $\\rho$ ($p{=}0.021$), though bootstrap 95\\% CIs overlap (NER: [0.295, 0.459]; RE: [0.142, 0.339]).\n\nEntity span errors account for 55.5\\% of RE false negatives, confirming compound error propagation: RE quality depends on correct entity extraction, and entity errors cascade into relation failures.\nThis explains why all confidence signals degrade on the full RE set but recover on the conditional set (where baseline entity extraction succeeds).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-relation-type quality estimation (SciERC RE, Qwen3-8B). Large heterogeneity: $\\rho_{\\text{SJ}}$ ranges from 0.545 to 0.004.}\n\\label{tab:perrelation}\n\\begin{tabular}{l c ccc c}\n\\toprule\nRelation & $n$ & $\\rho_{\\text{SJ}}$ & $\\rho_{\\text{FK}}$ & $\\rho_{\\text{VC}}$ & Mean F1 \\\\\n\\midrule\nHYPONYM-OF   & 36  & \\textbf{0.545} & 0.646 & 0.628 & 0.513 \\\\\nCONJUNCTION  & 86  & 0.383 & 0.350 & 0.484 & 0.480 \\\\\nUSED-FOR     & 299 & 0.236 & 0.255 & 0.286 & 0.422 \\\\\nPART-OF      & 44  & 0.239 & 0.348 & 0.283 & 0.297 \\\\\nEVALUATE-FOR & 62  & 0.172 & 0.255 & 0.226 & 0.365 \\\\\nCOMPARE      & 35  & 0.168 & 0.184 & 0.180 & 0.453 \\\\\nFEATURE-OF   & 50  & 0.004 & 0.052 & 0.014 & 0.254 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Temperature Sensitivity}\n\\label{sec:temperature}\n\nSJ is highly robust to temperature: $\\Delta\\rho{=}\\pm 0.01$ between $T{=}0.7$ and $T{=}1.0$, while FK shifts by $\\pm 0.06$.\n$T{=}1.0$ preserves more oracle headroom (RE: 0.167 vs 0.131 at $T{=}0.7$) and diversity ($1{-}\\text{SJ}$: 0.389 vs 0.313), though no current signal can exploit this headroom.\nConditional filtering provides far larger improvements ($\\Delta\\rho{=}+0.07$ to $+0.14$) than temperature tuning---practitioners should prioritize filtering over temperature optimization.\n\n\\subsection{Capability Stratification}\n\\label{sec:stratification}\n\nStratifying instances by difficulty reveals that SJ is strongest on simple instances (entity count=0: $\\rho{=}0.689$) and degrades on complex ones (entity count 3--5: $\\rho{=}0.353$).\nOn hard RE instances (greedy F1$<$0.25), SJ correlation drops to $\\rho{=}{-}0.043$---effectively random.\nThis confirms that consistency signals operate within the model's capability range and cannot rescue systematic failures.\nAn independent proxy analysis ($r{=}{-}0.021$ between sentence length and F1) verifies that our difficulty strata are not circular with the evaluation metric.\n\n\\subsection{OOD Robustness}\n\\label{sec:ood}\n\nIn out-of-domain evaluation (Appendix Table~\\ref{tab:ood}), all signals degrade substantially (SJ: $\\rho$ drops from 0.357 to 0.15), but structural signals maintain positive correlation while log-probability inverts ($\\rho{=}{-}0.20$).\nThis has practical implications for closed-source API scenarios where log-probabilities are unavailable: structural consistency, despite weaker absolute correlation, provides directionally correct confidence estimates and does not actively mislead.\n\n%=============================================================\n\\section{Practical Guidance}\n\\label{sec:practical}\n%=============================================================\n\nBased on our findings, we propose the following decision framework for practitioners:\n\n\\paragraph{When to use structural consistency (voting/SJ).}\nFor \\emph{selective prediction} and \\emph{abstention}: if the goal is to identify which instances are reliable (e.g., to route uncertain cases to human review), structural consistency provides the strongest signal (AUROC up to 0.73).\nAlso preferred when: (a)~log-probabilities are unavailable (closed-source APIs), (b)~domain shift is expected (structural signals degrade gracefully while logprob can invert), or (c)~temperature robustness is needed.\n\n\\paragraph{When to use log-probability.}\nFor \\emph{best-of-$N$ selection} on tasks where greedy decoding is suboptimal (e.g., RE).\nLog-probability is the only per-sample signal and the only one enabling effective sample selection in our experiments.\n\n\\paragraph{When neither helps.}\nFor NER best-of-$N$ selection with current models, greedy decoding is near-optimal---multi-sample generation provides no selection benefit despite large oracle headroom.\nFor tasks where the model systematically fails (e.g., social media NER with 54\\% zero-F1 rate), no confidence signal is informative.\n\n\\paragraph{Voting vs.\\ SJ.}\nEntity voting is simpler, faster, and empirically stronger on full sets.\nSJ generalizes to arbitrary structured outputs (relations, events) and is more temperature-robust.\nFor standard NER, voting is the practical default; for novel structured tasks or when temperature stability matters, prefer SJ.\n\n%=============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%=============================================================\n\n\\paragraph{The Correlation-Selection Gap as a General Phenomenon.}\nOur finding that strong quality estimation does not imply effective selection may extend beyond IE.\nInstance-level consistency signals inherently measure \\emph{input difficulty}, not \\emph{output quality variation} within a fixed input.\nFor tasks where within-input quality variance is low relative to between-input variance, the gap will be large.\nDeveloping per-sample structural signals---not just instance-level aggregates---is a key direction for closing this gap.\n\n\\paragraph{Applicability to Closed-Source APIs.}\nMany production IE systems use closed-source APIs (GPT-4, Claude) that do not expose log-probabilities.\nIn this setting, structural consistency signals offer unique value: they require only the generated text, not model internals.\nOur OOD results (Section~\\ref{sec:ood}) further suggest that log-probabilities can become \\emph{anti-correlated} with quality under domain shift, making structural signals the safer default.\n\n\\paragraph{Limitations.}\n(1)~We evaluate only 8B-parameter models; larger models may exhibit different patterns.\n(2)~Both models are instruction-tuned; base models or fine-tuned models may differ.\n(3)~We test on well-structured text domains (scientific, news); informal text (social media) remains unexplored---WNUT-17 was abandoned due to model capability failure.\n(4)~RE evaluation is limited to SciERC; additional relational datasets would strengthen generalization claims.\n(5)~We do not compare against supervised verifiers or reward models, which represent an upper bound on selection quality.\n\n%=============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%=============================================================\n\nWe present the first systematic comparison of unsupervised confidence signals for LLM-based information extraction, evaluating five signals across two tasks, two datasets, and two models.\nStructural consistency signals (entity voting, soft Jaccard) provide the strongest instance-level quality estimation, substantially outperforming log-probability.\nHowever, we identify a fundamental correlation-selection gap: no unsupervised signal beats greedy decoding for NER best-of-$N$ selection despite +16pp oracle headroom.\nOn relational tasks, compound error propagation degrades all signals, with dramatic per-relation heterogeneity.\nWe provide practical guidance distinguishing when to use structural consistency (selective prediction, closed-source APIs) vs.\\ log-probability (sample selection on hard tasks), and characterize the task-complexity boundaries within which confidence estimation is reliable.\n\n%=============================================================\n\\appendix\n\\section{OOD Robustness Details}\n\\label{app:ood}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Out-of-domain robustness. Structural signals degrade but remain positive; log-probability inverts.}\n\\label{tab:ood}\n\\begin{tabular}{l cc c}\n\\toprule\nSignal & In-Domain $\\rho$ & OOD $\\rho$ & $\\Delta$ \\\\\n\\midrule\nSJ      & 0.357 & 0.15  & $-$0.207 \\\\\nFK      & 0.265 & 0.10  & $-$0.165 \\\\\nlogprob & 0.140 & $-$0.20 & $-$0.340 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%=============================================================\n\\bibliography{custom}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{50}\n\n\\bibitem[Angelopoulos et~al.(2021)]{angelopoulos2021gentle}\nA.~Angelopoulos et~al.\n\\newblock A gentle introduction to conformal prediction and distribution-free uncertainty quantification.\n\\newblock \\emph{arXiv:2107.07511}, 2021.\n\n\\bibitem[Bates et~al.(2021)]{bates2021distribution}\nS.~Bates et~al.\n\\newblock Distribution-free, risk-controlling prediction sets.\n\\newblock \\emph{JASA}, 2021.\n\n\\bibitem[Brown et~al.(2024)]{brown2024large}\nB.~Brown et~al.\n\\newblock Large language monkeys: Scaling inference compute with repeated sampling.\n\\newblock \\emph{arXiv:2407.21787}, 2024.\n\n\\bibitem[Chen et~al.(2024)]{chen2024atomic}\nZ.~Chen et~al.\n\\newblock Atomic self-consistency for better long form generations.\n\\newblock In \\emph{EMNLP}, 2024.\n\n\\bibitem[Cobbe et~al.(2021)]{cobbe2021verifier}\nK.~Cobbe et~al.\n\\newblock Training verifiers to solve math word problems.\n\\newblock \\emph{arXiv:2110.14168}, 2021.\n\n\\bibitem[Culotta and McCallum(2004)]{culotta2004confidence}\nA.~Culotta and A.~McCallum.\n\\newblock Confidence estimation for information extraction.\n\\newblock In \\emph{HLT-NAACL}, 2004.\n\n\\bibitem[Derczynski et~al.(2017)]{derczynski2017wnut}\nL.~Derczynski et~al.\n\\newblock Results of the WNUT2017 shared task on novel and emerging entity recognition.\n\\newblock In \\emph{W-NUT}, 2017.\n\n\\bibitem[Desai and Durrett(2020)]{desai2020calibration}\nS.~Desai and G.~Durrett.\n\\newblock Calibration of pre-trained transformers.\n\\newblock In \\emph{EMNLP}, 2020.\n\n\\bibitem[Fisch et~al.(2021)]{fisch2021efficient}\nA.~Fisch et~al.\n\\newblock Efficient conformal prediction via cascaded inference with expanded admission.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Gal and Ghahramani(2016)]{gal2016dropout}\nY.~Gal and Z.~Ghahramani.\n\\newblock Dropout as a {B}ayesian approximation: Representing model uncertainty in deep learning.\n\\newblock In \\emph{ICML}, 2016.\n\n\\bibitem[Geifman and El-Yaniv(2017)]{geifman2017selective}\nY.~Geifman and R.~El-Yaniv.\n\\newblock Selective classification for deep neural networks.\n\\newblock In \\emph{NeurIPS}, 2017.\n\n\\bibitem[Geng et~al.(2025)]{geng2025uqsurvey}\nJ.~Geng et~al.\n\\newblock A survey on uncertainty quantification for large language models.\n\\newblock In \\emph{ACL Findings}, 2025.\n\n\\bibitem[Guo et~al.(2017)]{guo2017calibration}\nC.~Guo et~al.\n\\newblock On calibration of modern neural networks.\n\\newblock In \\emph{ICML}, 2017.\n\n\\bibitem[Hou et~al.(2025)]{hou2025uqcalibsurvey}\nB.~Hou et~al.\n\\newblock A survey on uncertainty quantification and calibration for large language models.\n\\newblock \\emph{arXiv:2503.15850}, 2025.\n\n\\bibitem[Huang et~al.(2025)]{huang2025cisc}\nW.~Huang et~al.\n\\newblock {CISC}: Confidence-weighted self-consistency for improved reasoning.\n\\newblock In \\emph{ACL Findings}, 2025.\n\n\\bibitem[Jagannatha and Yu(2022)]{jagannatha2022calibration}\nA.~Jagannatha and H.~Yu.\n\\newblock Calibrating structured output predictors for natural language processing.\n\\newblock In \\emph{ACL}, 2022.\n\n\\bibitem[Kadavath et~al.(2022)]{kadavath2022language}\nS.~Kadavath et~al.\n\\newblock Language models (mostly) know what they know.\n\\newblock \\emph{arXiv:2207.05221}, 2022.\n\n\\bibitem[Kossen et~al.(2024)]{kossen2024semanticprobes}\nJ.~Kossen et~al.\n\\newblock Semantic entropy probes: Robust and cheap hallucination detection in {LLM}s by exploiting {LLM} uncertainty.\n\\newblock \\emph{arXiv:2406.15927}, 2024.\n\n\\bibitem[Kuhn et~al.(2023)]{kuhn2023semantic}\nL.~Kuhn, Y.~Gal, and S.~Farquhar.\n\\newblock Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Kuleshov and Liang(2015)]{kuleshov2015calibration}\nV.~Kuleshov and P.~Liang.\n\\newblock Calibrated structured prediction.\n\\newblock In \\emph{NeurIPS}, 2015.\n\n\\bibitem[Lakshminarayanan et~al.(2017)]{lakshminarayanan2017simple}\nB.~Lakshminarayanan, A.~Pritzel, and C.~Blundell.\n\\newblock Simple and scalable predictive uncertainty estimation using deep ensembles.\n\\newblock In \\emph{NeurIPS}, 2017.\n\n\\bibitem[Li et~al.(2026)]{li2026reasc}\nZ.~Li et~al.\n\\newblock {ReASC}: Reliability-aware adaptive self-consistency.\n\\newblock \\emph{arXiv:2601.02970}, 2026.\n\n\\bibitem[Lightman et~al.(2023)]{lightman2023stepwise}\nH.~Lightman et~al.\n\\newblock Let's verify step by step.\n\\newblock \\emph{arXiv:2305.20050}, 2023.\n\n\\bibitem[Liu et~al.(2025)]{liu2025rankedvoting}\nY.~Liu et~al.\n\\newblock Ranked voting self-consistency.\n\\newblock \\emph{arXiv:2505.10772}, 2025.\n\n\\bibitem[Luan et~al.(2018)]{luan2018scierc}\nY.~Luan et~al.\n\\newblock Multi-task identification of entities, relations, and coreference for scientific knowledge graph construction.\n\\newblock In \\emph{EMNLP}, 2018.\n\n\\bibitem[Manakul et~al.(2023)]{manakul2023selfcheckgpt}\nP.~Manakul, A.~Liusie, and M.~Gales.\n\\newblock {SelfCheckGPT}: Zero-resource black-box hallucination detection for generative large language models.\n\\newblock In \\emph{EMNLP}, 2023.\n\n\\bibitem[N{\\'e}dellec and Xia(2026)]{nédellec2026consistency}\nC.~N{\\'e}dellec and F.~Xia.\n\\newblock Consistency--accuracy correlation in hard-prompted {LLM}s for entity and relation extraction.\n\\newblock \\emph{Genomics Informatics}, 2026.\n\n\\bibitem[Shelmanov et~al.(2021)]{shelmanov2021uncertainty}\nA.~Shelmanov et~al.\n\\newblock How certain is your {T}ransformer?\n\\newblock In \\emph{EACL}, 2021.\n\n\\bibitem[Snell et~al.(2024)]{snell2024scaling}\nC.~Snell et~al.\n\\newblock Scaling {LLM} test-time compute optimally can be more effective than scaling model parameters.\n\\newblock \\emph{arXiv:2408.03314}, 2024.\n\n\\bibitem[Tjong Kim~Sang and De~Meulder(2003)]{tjong2003conll}\nE.~Tjong~Kim~Sang and F.~De~Meulder.\n\\newblock Introduction to the {CoNLL}-2003 shared task: Language-independent named entity recognition.\n\\newblock In \\emph{CoNLL}, 2003.\n\n\\bibitem[Vashurin et~al.(2025a)]{vashurin2025cocoa}\nR.~Vashurin et~al.\n\\newblock {CoCoA}: Combining confidence and consistency for uncertainty quantification.\n\\newblock In \\emph{NeurIPS}, 2025.\n\n\\bibitem[Vashurin et~al.(2025b)]{vashurin2025systematic}\nR.~Vashurin et~al.\n\\newblock A systematic evaluation of {LLM} uncertainty quantification methods.\n\\newblock \\emph{arXiv:2510.20460}, 2025.\n\n\\bibitem[Wang et~al.(2023)]{wang2023selfconsistency}\nX.~Wang et~al.\n\\newblock Self-consistency improves chain of thought reasoning in language models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Wu et~al.(2025)]{wu2025latentsc}\nH.~Wu et~al.\n\\newblock Latent self-consistency.\n\\newblock \\emph{arXiv:2508.18395}, 2025.\n\n\\bibitem[Xiao and Wang(2019)]{xiao2019uncertainty}\nY.~Xiao and W.~Wang.\n\\newblock Quantifying uncertainties in natural language processing tasks.\n\\newblock In \\emph{AAAI}, 2019.\n\n\\bibitem[Xiong et~al.(2024)]{xiong2024confestimation}\nM.~Xiong et~al.\n\\newblock Can {LLM}s express their uncertainty? An empirical evaluation of confidence elicitation in {LLM}s.\n\\newblock In \\emph{NAACL}, 2024.\n\n\\bibitem[Yoshikawa et~al.(2025)]{yoshikawa2025abstention}\nH.~Yoshikawa et~al.\n\\newblock Know your limits: A survey of abstention in large language models.\n\\newblock \\emph{TACL}, 2025.\n\n\\bibitem[Zhang et~al.(2026)]{zhang2026selfcertainty}\nS.~Zhang et~al.\n\\newblock Self-certainty best-of-$N$.\n\\newblock In \\emph{ICLR}, 2026.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "19092151-eea1-4b71-ad4d-21d02a09749b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T203201 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_cons…",
  "leafUuid": "a2e24ca6-172c-4a8a-8d60-099a8db5c494",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper for dream_20260514T203201",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257"
}
```

---

### Assistant

_source line 23 · 2026-05-14T21:12:02.698Z_

Now compiling the LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2e24ca6-172c-4a8a-8d60-099a8db5c494",
  "isSidechain": false,
  "requestId": "req_011Cb39dnxfQBa7tvVHqtq9m",
  "type": "assistant",
  "uuid": "1f36a276-4872-4d1f-8f20-c7029fe3bb74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Voz7Qq2UYdGTRWC9nmFmV9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14040,
      "cache_read_input_tokens": 44091,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 44091,
          "cache_creation_input_tokens": 14040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14040
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

_source line 24 · 2026-05-14T21:12:04.446Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01X2wZgC9VU5U16Pbmi9HbjS`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f36a276-4872-4d1f-8f20-c7029fe3bb74",
  "isSidechain": false,
  "requestId": "req_011Cb39dnxfQBa7tvVHqtq9m",
  "type": "assistant",
  "uuid": "01d9ec71-565e-41e3-814f-ac1cf60b09e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Voz7Qq2UYdGTRWC9nmFmV9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14040,
      "cache_read_input_tokens": 44091,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 44091,
          "cache_creation_input_tokens": 14040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14040
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

_source line 25 · 2026-05-14T21:12:04.617Z_

<details><summary>↩ Tool result · reported error · `toolu_01X2wZgC9VU5U16Pbmi9HbjS`</summary>

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

! LaTeX Error: File `emnlp2023.sty' not found.

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
  "parentUuid": "01d9ec71-565e-41e3-814f-ac1cf60b09e7",
  "isSidechain": false,
  "promptId": "23021a69-dda5-4b12-987b-ef4578d19bc0",
  "type": "user",
  "uuid": "5749d408-7b71-486a-96c3-f66e38db2763",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `emnlp2023.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "01d9ec71-565e-41e3-814f-ac1cf60b09e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-14T21:12:07.541Z_

<details><summary>Logged reasoning block</summary>

```text
The emnlp2023.sty is not available. Let me switch to a standard article class instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5749d408-7b71-486a-96c3-f66e38db2763",
  "isSidechain": false,
  "requestId": "req_011Cb39e9xiQCipYSvj7EDwm",
  "type": "assistant",
  "uuid": "425d11e2-9e74-4eb1-aaf7-9b87d517186e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PC8mgUDwYtmUQffxachckn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 484,
      "cache_read_input_tokens": 58131,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 309,
          "cache_read_input_tokens": 58131,
          "cache_creation_input_tokens": 484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 484
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

_source line 27 · 2026-05-14T21:12:08.417Z_

Need to switch to a standard document class since `emnlp2023.sty` is not available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "425d11e2-9e74-4eb1-aaf7-9b87d517186e",
  "isSidechain": false,
  "requestId": "req_011Cb39e9xiQCipYSvj7EDwm",
  "type": "assistant",
  "uuid": "93575540-c557-4ad8-8f16-16a904101c3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PC8mgUDwYtmUQffxachckn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 484,
      "cache_read_input_tokens": 58131,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 309,
          "cache_read_input_tokens": 58131,
          "cache_creation_input_tokens": 484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 484
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

_source line 28 · 2026-05-14T21:12:10.599Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01BT8PG7xm3kvsXjYruxAGsV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\renewcommand{\\bibsection}{\\section*{References}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93575540-c557-4ad8-8f16-16a904101c3f",
  "isSidechain": false,
  "requestId": "req_011Cb39e9xiQCipYSvj7EDwm",
  "type": "assistant",
  "uuid": "c906bfec-0254-4c32-84dc-1f31b6338d8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PC8mgUDwYtmUQffxachckn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 484,
      "cache_read_input_tokens": 58131,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 309,
          "cache_read_input_tokens": 58131,
          "cache_creation_input_tokens": 484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 484
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

_source line 29 · 2026-05-14T21:12:10.618Z_

<details><summary>↩ Tool result · `toolu_01BT8PG7xm3kvsXjYruxAGsV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c906bfec-0254-4c32-84dc-1f31b6338d8c",
  "isSidechain": false,
  "promptId": "23021a69-dda5-4b12-987b-ef4578d19bc0",
  "type": "user",
  "uuid": "bbc635f6-4be0-43ee-b092-d084f7ccb825",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\renewcommand{\\bibsection}{\\section*{References}}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 9,
        "lines": [
          " \\documentclass[11pt,a4paper]{article}",
          "-\\usepackage[hyperref]{emnlp2023}",
          "+\\usepackage[margin=2.5cm]{geometry}",
          " \\usepackage{times}",
          "+\\usepackage{hyperref}",
          "+\\usepackage{natbib}",
          "+\\renewcommand{\\bibsection}{\\section*{References}}",
          " \\usepackage{latexsym}",
          " \\usepackage{amsmath}",
          " \\usepackage{amssymb}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "c906bfec-0254-4c32-84dc-1f31b6338d8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-14T21:12:10.647Z_

```json
{
  "parentUuid": "bbc635f6-4be0-43ee-b092-d084f7ccb825",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a3706ceb-eb88-42c8-b310-a0a453d2357c",
  "timestamp": "2026-05-14T21:12:10.647Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-14T21:12:14.758Z_

Also need to remove the `\bibliography{custom}` and `\bibliographystyle{acl_natbib}` lines since we're using inline thebibliography.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3706ceb-eb88-42c8-b310-a0a453d2357c",
  "isSidechain": false,
  "requestId": "req_011Cb39ebhH3ao9AJfdEgHLX",
  "type": "assistant",
  "uuid": "d92414c8-9f95-432c-830a-56acd057369d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7ytE3ZhvCAaFJLC46aqvY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 500,
      "cache_read_input_tokens": 58615,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 500,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 58615,
          "cache_creation_input_tokens": 500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 500
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

_source line 32 · 2026-05-14T21:12:15.794Z_

<details open><summary>🔧 Tool call — Edit · `toolu_019UkEsV6MDQCcGQRqSq3kCP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex",
  "old_string": "\\bibliography{custom}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{50}",
  "new_string": "\\begin{thebibliography}{50}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d92414c8-9f95-432c-830a-56acd057369d",
  "isSidechain": false,
  "requestId": "req_011Cb39ebhH3ao9AJfdEgHLX",
  "type": "assistant",
  "uuid": "19873549-22b3-49e7-9f30-2c899be07282",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7ytE3ZhvCAaFJLC46aqvY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 500,
      "cache_read_input_tokens": 58615,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 500,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 58615,
          "cache_creation_input_tokens": 500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 500
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

_source line 33 · 2026-05-14T21:12:15.811Z_

<details><summary>↩ Tool result · `toolu_019UkEsV6MDQCcGQRqSq3kCP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19873549-22b3-49e7-9f30-2c899be07282",
  "isSidechain": false,
  "promptId": "23021a69-dda5-4b12-987b-ef4578d19bc0",
  "type": "user",
  "uuid": "f0e07f0f-b389-4901-bc7d-017d662cbfe8",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex",
    "oldString": "\\bibliography{custom}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{50}",
    "newString": "\\begin{thebibliography}{50}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 547,
        "oldLines": 9,
        "newStart": 547,
        "newLines": 6,
        "lines": [
          " \\end{table}",
          " ",
          " %=============================================================",
          "-\\bibliography{custom}",
          "-\\bibliographystyle{acl_natbib}",
          "-",
          " \\begin{thebibliography}{50}",
          " ",
          " \\bibitem[Angelopoulos et~al.(2021)]{angelopoulos2021gentle}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "19873549-22b3-49e7-9f30-2c899be07282",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T21:12:19.650Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SC5Rdt2zoPhw89ZMqWLncC`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0e07f0f-b389-4901-bc7d-017d662cbfe8",
  "isSidechain": false,
  "requestId": "req_011Cb39ezFLxpjsHAUd7kSsR",
  "type": "assistant",
  "uuid": "e4e6fdbc-7528-48bf-9a84-f132395f7176",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjpL82AMM64VQLbRw4ZXsp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 306,
      "cache_read_input_tokens": 59115,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 59115,
          "cache_creation_input_tokens": 306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 306
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

_source line 35 · 2026-05-14T21:12:23.973Z_

<details><summary>↩ Tool result · `toolu_01SC5Rdt2zoPhw89ZMqWLncC`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/pgfplots/pgfplots.sty
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplots.revision.tex)
(/usr/share/texlive/texmf-dist/tex/latex/pgf/frontendlayer/tikz.sty
(/usr/share/texlive/texmf-dist/tex/latex/pgf/basiclayer/pgf.sty
(/usr/share/texlive/texmf-dist/tex/latex/pgf/utilities/pgfrcs.sty
(/usr/share/texlive/texmf-dist/tex/generic/pgf/utilities/pgfutil-common.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/utilities/pgfutil-latex.def)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/utilities/pgfrcs.code.tex
(/usr/share/texlive/texmf-dist/tex/generic/pgf/pgf.revision.tex)))
(/usr/share/texlive/texmf-dist/tex/latex/pgf/basiclayer/pgfcore.sty
(/usr/share/texlive/texmf-dist/tex/latex/pgf/systemlayer/pgfsys.sty
(/usr/share/texlive/texmf-dist/tex/generic/pgf/systemlayer/pgfsys.code.tex
(/usr/share/texlive/texmf-dist/tex/generic/pgf/utilities/pgfkeys.code.tex
(/usr/share/texlive/texmf-dist/tex/generic/pgf/utilities/pgfkeyslibraryfiltered
.code.tex)) (/usr/share/texlive/texmf-dist/tex/generic/pgf/systemlayer/pgf.cfg)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-pdftex.def
(/usr/share/texlive/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-common-pdf.de
f)))
(/usr/share/texlive/texmf-dist/tex/generic/pgf/systemlayer/pgfsyssoftpath.code.
tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/systemlayer/pgfsysprotocol.code.
tex))
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcore.code.tex
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmath.code.tex
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathutil.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathparser.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.basic.code
.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.trigonomet
ric.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.random.cod
e.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.comparison
.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.base.code.
tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.round.code
.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.misc.code.
tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.integerari
thmetics.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathcalc.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfloat.code.tex))
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfint.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepoints.code.te
x)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathconstruct.
code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathusage.code
.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorescopes.code.te
x)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcoregraphicstate.c
ode.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcoretransformation
s.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorequick.code.tex
)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreobjects.code.t
ex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathprocessing
.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorearrows.code.te
x)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreshade.code.tex
)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreimage.code.tex
)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreexternal.code.
tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorelayers.code.te
x)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcoretransparency.c
ode.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepatterns.code.
tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorerdf.code.tex))
)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/modules/pgfmoduleshapes.code.tex
) (/usr/share/texlive/texmf-dist/tex/generic/pgf/modules/pgfmoduleplot.code.tex
)
(/usr/share/texlive/texmf-dist/tex/latex/pgf/compatibility/pgfcomp-version-0-65
.sty)
(/usr/share/texlive/texmf-dist/tex/latex/pgf/compatibility/pgfcomp-version-1-18
.sty)) (/usr/share/texlive/texmf-dist/tex/latex/pgf/utilities/pgffor.sty
(/usr/share/texlive/texmf-dist/tex/latex/pgf/utilities/pgfkeys.sty
(/usr/share/texlive/texmf-dist/tex/generic/pgf/utilities/pgfkeys.code.tex))
(/usr/share/texlive/texmf-dist/tex/latex/pgf/math/pgfmath.sty
(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmath.code.tex))
(/usr/share/texlive/texmf-dist/tex/generic/pgf/utilities/pgffor.code.tex))
(/usr/share/texlive/texmf-dist/tex/generic/pgf/frontendlayer/tikz/tikz.code.tex

(/usr/share/texlive/texmf-dist/tex/generic/pgf/libraries/pgflibraryplothandlers
.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/modules/pgfmodulematrix.code.tex
)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tik
zlibrarytopaths.code.tex)))
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplots.code.tex
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplotscore.code.tex
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/sys/pgfplotssysgeneric.code
.tex))
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/libs/pgfplotslibrary.code.t
ex)
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldp
gfsupp_loader.code.tex
(/usr/share/texlive/texmf-dist/tex/generic/pgf/libraries/pgflibraryfpu.code.tex
)
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldp
gfsupp_pgfutil-common-lists.tex))
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/util/pgfplotsutil.code.tex
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/liststructure/pgfplotslists
tructure.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/liststructure/pgfplotslists
tructureext.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/liststructure/pgfplotsarray
.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/liststructure/pgfplotsmatri
x.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/numtable/pgfplotstableshare
d.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/liststructure/pgfplotsdeque
.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/util/pgfplotsbinary.code.te
x
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/util/pgfplotsbinary.data.co
de.tex))
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/util/pgfplotsutil.verb.code
.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/libs/pgflibrarypgfplots.sur
fshading.code.tex
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/sys/pgflibrarypgfplots.surf
shading.pgfsys-pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/util/pgfplotscolormap.code.
tex
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/util/pgfplotscolor.code.tex
))
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplotsstackedplots.code.t
ex)
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplotsplothandlers.code.t
ex
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplotsmeshplothandler.cod
e.tex
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplotsmeshplotimage.code.
tex)))
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplots.scaling.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplotscoordprocessing.cod
e.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplots.errorbars.code.tex
) (/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplots.markers.code.tex
) (/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplotsticks.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplots.paths.code.tex)
(/usr/share/texlive/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tik
zlibrarydecorations.code.tex
(/usr/share/texlive/texmf-dist/tex/generic/pgf/modules/pgfmoduledecorations.cod
e.tex))
(/usr/share/texlive/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tik
zlibrarydecorations.pathmorphing.code.tex
(/usr/share/texlive/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrary
decorations.pathmorphing.code.tex))
(/usr/share/texlive/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tik
zlibrarydecorations.pathreplacing.code.tex
(/usr/share/texlive/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrary
decorations.pathreplacing.code.tex))
(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/libs/tikzlibrarypgfplots.co
ntourlua.code.tex))
(/usr/share/texlive/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tik
zlibraryplotmarks.code.tex
(/usr/share/texlive/texmf-dist/tex/generic/pgf/libraries/pgflibraryplotmarks.co
de.tex))) (/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
Package pgfplots notification 'compat/show suggested version=true': you might b
enefit from \pgfplotsset{compat=1.18} (current compat level: 1.17).

(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `wang2023selfconsistency' on page 1 undefined 
on input line 40.


Package natbib Warning: Citation `snell2024scaling' on page 1 undefined on inpu
t line 40.


Package natbib Warning: Citation `brown2024large' on page 1 undefined on input 
line 40.


Package natbib Warning: Citation `kuhn2023semantic' on page 1 undefined on inpu
t line 45.


Package natbib Warning: Citation `manakul2023selfcheckgpt' on page 1 undefined 
on input line 45.


Package natbib Warning: Citation `kadavath2022language' on page 1 undefined on 
input line 45.


Package natbib Warning: Citation `guo2017calibration' on page 1 undefined on in
put line 45.


Package natbib Warning: Citation `desai2020calibration' on page 1 undefined on 
input line 45.


Package natbib Warning: Citation `nédellec2026consistency' on page 1 undefined
 on input line 46.


Package natbib Warning: Citation `huang2025cisc' on page 1 undefined on input l
ine 47.


Package natbib Warning: Citation `zhang2026selfcertainty' on page 1 undefined o
n input line 47.


Package natbib Warning: Citation `li2026reasc' on page 1 undefined on input lin
e 47.


LaTeX Warning: Reference `fig:overview' on page 1 undefined on input line 49.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

LaTeX Warning: Reference `sec:practical' on page 2 undefined on input line 58.


Overfull \hbox (2.82834pt too wide) in paragraph at lines 57--59
[]\OT1/ptm/m/n/10.95 The iden-ti-fi-ca-tion of a \OT1/ptm/b/n/10.95 correlation
-selection gap\OT1/ptm/m/n/10.95 : strong instance-level qual-ity es-ti-ma-tion
 ($\OML/cmm/m/it/10.95 ^^Z[]\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m
/n/10.95 50$\OT1/ptm/m/n/10.95 )

Package natbib Warning: Citation `geng2025uqsurvey' on page 2 undefined on inpu
t line 98.


Package natbib Warning: Citation `hou2025uqcalibsurvey' on page 2 undefined on 
input line 98.


Package natbib Warning: Citation `xiong2024confestimation' on page 2 undefined 
on input line 98.


Package natbib Warning: Citation `yoshikawa2025abstention' on page 2 undefined 
on input line 98.


Package natbib Warning: Citation `kadavath2022language' on page 2 undefined on 
input line 99.


Package natbib Warning: Citation `kuhn2023semantic' on page 2 undefined on inpu
t line 99.


Package natbib Warning: Citation `kossen2024semanticprobes' on page 2 undefined
 on input line 99.


Package natbib Warning: Citation `manakul2023selfcheckgpt' on page 2 undefined 
on input line 99.


Package natbib Warning: Citation `guo2017calibration' on page 2 undefined on in
put line 100.


Package natbib Warning: Citation `desai2020calibration' on page 2 undefined on 
input line 100.


Package natbib Warning: Citation `kuleshov2015calibration' on page 2 undefined 
on input line 100.


Package natbib Warning: Citation `wang2023selfconsistency' on page 2 undefined 
on input line 104.


Package natbib Warning: Citation `huang2025cisc' on page 2 undefined on input l
ine 105.


Package natbib Warning: Citation `zhang2026selfcertainty' on page 2 undefined o
n input line 105.


Package natbib Warning: Citation `li2026reasc' on page 2 undefined on input lin
e 105.


Package natbib Warning: Citation `chen2024atomic' on page 2 undefined on input 
line 105.


Package natbib Warning: Citation `liu2025rankedvoting' on page 2 undefined on i
nput line 105.


Package natbib Warning: Citation `wu2025latentsc' on page 2 undefined on input 
line 105.


Package natbib Warning: Citation `snell2024scaling' on page 2 undefined on inpu
t line 106.


Package natbib Warning: Citation `brown2024large' on page 2 undefined on input 
line 106.


Package natbib Warning: Citation `cobbe2021verifier' on page 2 undefined on inp
ut line 107.


Package natbib Warning: Citation `lightman2023stepwise' on page 2 undefined on 
input line 107.


Package natbib Warning: Citation `nédellec2026consistency' on page 2 undefined
 on input line 111.


Package natbib Warning: Citation `culotta2004confidence' on page 2 undefined on
 input line 113.


Package natbib Warning: Citation `xiao2019uncertainty' on page 2 undefined on i
nput line 114.


Package natbib Warning: Citation `shelmanov2021uncertainty' on page 2 undefined
 on input line 114.


Package natbib Warning: Citation `jagannatha2022calibration' on page 2 undefine
d on input line 115.


Package natbib Warning: Citation `lakshminarayanan2017simple' on page 2 undefin
ed on input line 116.


Package natbib Warning: Citation `gal2016dropout' on page 2 undefined on input 
line 116.


Package natbib Warning: Citation `vashurin2025cocoa' on page 2 undefined on inp
ut line 117.


Package natbib Warning: Citation `geifman2017selective' on page 2 undefined on 
input line 118.

[2]

Package natbib Warning: Citation `wang2023selfconsistency' on page 3 undefined 
on input line 142.

[3]

Package natbib Warning: Citation `luan2018scierc' on page 4 undefined on input 
line 187.


Package natbib Warning: Citation `tjong2003conll' on page 4 undefined on input 
line 187.


Package natbib Warning: Citation `derczynski2017wnut' on page 4 undefined on in
put line 188.


LaTeX Warning: Reference `tab:unified' on page 4 undefined on input line 206.


Overfull \hbox (41.86356pt too wide) in paragraph at lines 206--209
\OT1/ptm/m/n/10.95 achieves the high-est cor-re-la-tion ($\OML/cmm/m/it/10.95 ^
^Z[]\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 502$\OT1/ptm/m/
n/10.95 , AUROC$[]\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 7
28$\OT1/ptm/m/n/10.95 ), fol-lowed by soft Jac-card ($\OML/cmm/m/it/10.95 ^^Z[]
\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 357$\OT1/ptm/m/n/10
.95 , AUROC$[]\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 666$\
OT1/ptm/m/n/10.95 ).

LaTeX Warning: Reference `sec:diagnostic' on page 4 undefined on input line 211
.


LaTeX Warning: Reference `tab:conll' on page 4 undefined on input line 237.


LaTeX Warning: Reference `tab:crossmodel' on page 4 undefined on input line 262
.


LaTeX Warning: Reference `tab:matrix' on page 4 undefined on input line 262.

[4]

LaTeX Warning: Reference `tab:selection' on page 5 undefined on input line 302.



LaTeX Warning: Reference `fig:selection_curves' on page 5 undefined on input li
ne 302.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 368.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 368.


LaTeX Warning: Reference `tab:nscaling' on page 5 undefined on input line 371.


LaTeX Warning: Reference `tab:ensemble' on page 5 undefined on input line 397.

[5]

LaTeX Warning: Reference `tab:perrelation' on page 6 undefined on input line 42
2.


Overfull \hbox (7.5464pt too wide) in paragraph at lines 459--463
\OT1/ptm/m/n/10.95 Stratifying in-stances by dif-fi-culty re-veals that SJ is s
trongest on sim-ple in-stances (en-tity count=0: $\OML/cmm/m/it/10.95 ^^Z[]\OT1
/cmr/m/n/10.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 689$\OT1/ptm/m/n/10.95 
)

LaTeX Warning: Reference `tab:ood' on page 6 undefined on input line 467.


Overfull \hbox (5.53098pt too wide) in paragraph at lines 467--469
\OT1/ptm/m/n/10.95 0.357 to 0.15), but struc-tural sig-nals main-tain pos-i-tiv
e cor-re-la-tion while log-probability in-verts ($\OML/cmm/m/it/10.95 ^^Z[][]\O
T1/cmr/m/n/10.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 20$\OT1/ptm/m/n/10.95
 ).
[6] [7]

LaTeX Warning: Reference `sec:ood' on page 8 undefined on input line 508.

[8] [9]
Underfull \hbox (badness 4242) in paragraph at lines 708--711
[]\OT1/ptm/m/n/10.95 R. Vashurin et al.  A sys-tem-atic eval-u-a-tion of LLM un
-cer-tainty quan-tifi-ca-tion meth-ods.
[10]

Package natbib Warning: There were undefined citations.

[11] (./paper.aux

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
pe1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/u
tmri8a.pfb>
Output written on paper.pdf (11 pages, 199806 bytes).
Transcript written on paper.log.
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/u
tmri8a.pfb>
Output written on paper.pdf (11 pages, 205573 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4e6fdbc-7528-48bf-9a84-f132395f7176",
  "isSidechain": false,
  "promptId": "23021a69-dda5-4b12-987b-ef4578d19bc0",
  "type": "user",
  "uuid": "c8601ea3-d112-4259-84ce-8bd178527c07",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/pgfplots/pgfplots.sty\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplots.revision.tex)\n(/usr/share/texlive/texmf-dist/tex/latex/pgf/frontendlayer/tikz.sty\n(/usr/share/texlive/texmf-dist/tex/latex/pgf/basiclayer/pgf.sty\n(/usr/share/texlive/texmf-dist/tex/latex/pgf/utilities/pgfrcs.sty\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/utilities/pgfutil-common.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/utilities/pgfutil-latex.def)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/utilities/pgfrcs.code.tex\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/pgf.revision.tex)))\n(/usr/share/texlive/texmf-dist/tex/latex/pgf/basiclayer/pgfcore.sty\n(/usr/share/texlive/texmf-dist/tex/latex/pgf/systemlayer/pgfsys.sty\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/systemlayer/pgfsys.code.tex\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/utilities/pgfkeys.code.tex\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/utilities/pgfkeyslibraryfiltered\n.code.tex)) (/usr/share/texlive/texmf-dist/tex/generic/pgf/systemlayer/pgf.cfg)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-pdftex.def\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-common-pdf.de\nf)))\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/systemlayer/pgfsyssoftpath.code.\ntex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/systemlayer/pgfsysprotocol.code.\ntex))\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcore.code.tex\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmath.code.tex\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathutil.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathparser.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.basic.code\n.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.trigonomet\nric.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.random.cod\ne.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.comparison\n.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.base.code.\ntex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.round.code\n.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.misc.code.\ntex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.integerari\nthmetics.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathcalc.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmathfloat.code.tex))\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfint.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepoints.code.te\nx)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathconstruct.\ncode.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathusage.code\n.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorescopes.code.te\nx)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcoregraphicstate.c\node.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcoretransformation\ns.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorequick.code.tex\n)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreobjects.code.t\nex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathprocessing\n.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorearrows.code.te\nx)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreshade.code.tex\n)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreimage.code.tex\n)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreexternal.code.\ntex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorelayers.code.te\nx)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcoretransparency.c\node.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepatterns.code.\ntex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorerdf.code.tex))\n)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/modules/pgfmoduleshapes.code.tex\n) (/usr/share/texlive/texmf-dist/tex/generic/pgf/modules/pgfmoduleplot.code.tex\n)\n(/usr/share/texlive/texmf-dist/tex/latex/pgf/compatibility/pgfcomp-version-0-65\n.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/pgf/compatibility/pgfcomp-version-1-18\n.sty)) (/usr/share/texlive/texmf-dist/tex/latex/pgf/utilities/pgffor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/pgf/utilities/pgfkeys.sty\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/utilities/pgfkeys.code.tex))\n(/usr/share/texlive/texmf-dist/tex/latex/pgf/math/pgfmath.sty\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/math/pgfmath.code.tex))\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/utilities/pgffor.code.tex))\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/frontendlayer/tikz/tikz.code.tex\n\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/libraries/pgflibraryplothandlers\n.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/modules/pgfmodulematrix.code.tex\n)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tik\nzlibrarytopaths.code.tex)))\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplots.code.tex\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplotscore.code.tex\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/sys/pgfplotssysgeneric.code\n.tex))\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/libs/pgfplotslibrary.code.t\nex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldp\ngfsupp_loader.code.tex\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/libraries/pgflibraryfpu.code.tex\n)\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldp\ngfsupp_pgfutil-common-lists.tex))\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/util/pgfplotsutil.code.tex\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/liststructure/pgfplotslists\ntructure.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/liststructure/pgfplotslists\ntructureext.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/liststructure/pgfplotsarray\n.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/liststructure/pgfplotsmatri\nx.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/numtable/pgfplotstableshare\nd.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/liststructure/pgfplotsdeque\n.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/util/pgfplotsbinary.code.te\nx\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/util/pgfplotsbinary.data.co\nde.tex))\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/util/pgfplotsutil.verb.code\n.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/libs/pgflibrarypgfplots.sur\nfshading.code.tex\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/sys/pgflibrarypgfplots.surf\nshading.pgfsys-pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/util/pgfplotscolormap.code.\ntex\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/util/pgfplotscolor.code.tex\n))\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplotsstackedplots.code.t\nex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplotsplothandlers.code.t\nex\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplotsmeshplothandler.cod\ne.tex\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplotsmeshplotimage.code.\ntex)))\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplots.scaling.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplotscoordprocessing.cod\ne.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplots.errorbars.code.tex\n) (/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplots.markers.code.tex\n) (/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplotsticks.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/pgfplots.paths.code.tex)\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tik\nzlibrarydecorations.code.tex\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/modules/pgfmoduledecorations.cod\ne.tex))\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tik\nzlibrarydecorations.pathmorphing.code.tex\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrary\ndecorations.pathmorphing.code.tex))\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tik\nzlibrarydecorations.pathreplacing.code.tex\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrary\ndecorations.pathreplacing.code.tex))\n(/usr/share/texlive/texmf-dist/tex/generic/pgfplots/libs/tikzlibrarypgfplots.co\nntourlua.code.tex))\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tik\nzlibraryplotmarks.code.tex\n(/usr/share/texlive/texmf-dist/tex/generic/pgf/libraries/pgflibraryplotmarks.co\nde.tex))) (/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\nPackage pgfplots notification 'compat/show suggested version=true': you might b\nenefit from \\pgfplotsset{compat=1.18} (current compat level: 1.17).\n\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `wang2023selfconsistency' on page 1 undefined \non input line 40.\n\n\nPackage natbib Warning: Citation `snell2024scaling' on page 1 undefined on inpu\nt line 40.\n\n\nPackage natbib Warning: Citation `brown2024large' on page 1 undefined on input \nline 40.\n\n\nPackage natbib Warning: Citation `kuhn2023semantic' on page 1 undefined on inpu\nt line 45.\n\n\nPackage natbib Warning: Citation `manakul2023selfcheckgpt' on page 1 undefined \non input line 45.\n\n\nPackage natbib Warning: Citation `kadavath2022language' on page 1 undefined on \ninput line 45.\n\n\nPackage natbib Warning: Citation `guo2017calibration' on page 1 undefined on in\nput line 45.\n\n\nPackage natbib Warning: Citation `desai2020calibration' on page 1 undefined on \ninput line 45.\n\n\nPackage natbib Warning: Citation `nédellec2026consistency' on page 1 undefined\n on input line 46.\n\n\nPackage natbib Warning: Citation `huang2025cisc' on page 1 undefined on input l\nine 47.\n\n\nPackage natbib Warning: Citation `zhang2026selfcertainty' on page 1 undefined o\nn input line 47.\n\n\nPackage natbib Warning: Citation `li2026reasc' on page 1 undefined on input lin\ne 47.\n\n\nLaTeX Warning: Reference `fig:overview' on page 1 undefined on input line 49.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nLaTeX Warning: Reference `sec:practical' on page 2 undefined on input line 58.\n\n\nOverfull \\hbox (2.82834pt too wide) in paragraph at lines 57--59\n[]\\OT1/ptm/m/n/10.95 The iden-ti-fi-ca-tion of a \\OT1/ptm/b/n/10.95 correlation\n-selection gap\\OT1/ptm/m/n/10.95 : strong instance-level qual-ity es-ti-ma-tion\n ($\\OML/cmm/m/it/10.95 ^^Z[]\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m\n/n/10.95 50$\\OT1/ptm/m/n/10.95 )\n\nPackage natbib Warning: Citation `geng2025uqsurvey' on page 2 undefined on inpu\nt line 98.\n\n\nPackage natbib Warning: Citation `hou2025uqcalibsurvey' on page 2 undefined on \ninput line 98.\n\n\nPackage natbib Warning: Citation `xiong2024confestimation' on page 2 undefined \non input line 98.\n\n\nPackage natbib Warning: Citation `yoshikawa2025abstention' on page 2 undefined \non input line 98.\n\n\nPackage natbib Warning: Citation `kadavath2022language' on page 2 undefined on \ninput line 99.\n\n\nPackage natbib Warning: Citation `kuhn2023semantic' on page 2 undefined on inpu\nt line 99.\n\n\nPackage natbib Warning: Citation `kossen2024semanticprobes' on page 2 undefined\n on input line 99.\n\n\nPackage natbib Warning: Citation `manakul2023selfcheckgpt' on page 2 undefined \non input line 99.\n\n\nPackage natbib Warning: Citation `guo2017calibration' on page 2 undefined on in\nput line 100.\n\n\nPackage natbib Warning: Citation `desai2020calibration' on page 2 undefined on \ninput line 100.\n\n\nPackage natbib Warning: Citation `kuleshov2015calibration' on page 2 undefined \non input line 100.\n\n\nPackage natbib Warning: Citation `wang2023selfconsistency' on page 2 undefined \non input line 104.\n\n\nPackage natbib Warning: Citation `huang2025cisc' on page 2 undefined on input l\nine 105.\n\n\nPackage natbib Warning: Citation `zhang2026selfcertainty' on page 2 undefined o\nn input line 105.\n\n\nPackage natbib Warning: Citation `li2026reasc' on page 2 undefined on input lin\ne 105.\n\n\nPackage natbib Warning: Citation `chen2024atomic' on page 2 undefined on input \nline 105.\n\n\nPackage natbib Warning: Citation `liu2025rankedvoting' on page 2 undefined on i\nnput line 105.\n\n\nPackage natbib Warning: Citation `wu2025latentsc' on page 2 undefined on input \nline 105.\n\n\nPackage natbib Warning: Citation `snell2024scaling' on page 2 undefined on inpu\nt line 106.\n\n\nPackage natbib Warning: Citation `brown2024large' on page 2 undefined on input \nline 106.\n\n\nPackage natbib Warning: Citation `cobbe2021verifier' on page 2 undefined on inp\nut line 107.\n\n\nPackage natbib Warning: Citation `lightman2023stepwise' on page 2 undefined on \ninput line 107.\n\n\nPackage natbib Warning: Citation `nédellec2026consistency' on page 2 undefined\n on input line 111.\n\n\nPackage natbib Warning: Citation `culotta2004confidence' on page 2 undefined on\n input line 113.\n\n\nPackage natbib Warning: Citation `xiao2019uncertainty' on page 2 undefined on i\nnput line 114.\n\n\nPackage natbib Warning: Citation `shelmanov2021uncertainty' on page 2 undefined\n on input line 114.\n\n\nPackage natbib Warning: Citation `jagannatha2022calibration' on page 2 undefine\nd on input line 115.\n\n\nPackage natbib Warning: Citation `lakshminarayanan2017simple' on page 2 undefin\ned on input line 116.\n\n\nPackage natbib Warning: Citation `gal2016dropout' on page 2 undefined on input \nline 116.\n\n\nPackage natbib Warning: Citation `vashurin2025cocoa' on page 2 undefined on inp\nut line 117.\n\n\nPackage natbib Warning: Citation `geifman2017selective' on page 2 undefined on \ninput line 118.\n\n[2]\n\nPackage natbib Warning: Citation `wang2023selfconsistency' on page 3 undefined \non input line 142.\n\n[3]\n\nPackage natbib Warning: Citation `luan2018scierc' on page 4 undefined on input \nline 187.\n\n\nPackage natbib Warning: Citation `tjong2003conll' on page 4 undefined on input \nline 187.\n\n\nPackage natbib Warning: Citation `derczynski2017wnut' on page 4 undefined on in\nput line 188.\n\n\nLaTeX Warning: Reference `tab:unified' on page 4 undefined on input line 206.\n\n\nOverfull \\hbox (41.86356pt too wide) in paragraph at lines 206--209\n\\OT1/ptm/m/n/10.95 achieves the high-est cor-re-la-tion ($\\OML/cmm/m/it/10.95 ^\n^Z[]\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 502$\\OT1/ptm/m/\nn/10.95 , AUROC$[]\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 7\n28$\\OT1/ptm/m/n/10.95 ), fol-lowed by soft Jac-card ($\\OML/cmm/m/it/10.95 ^^Z[]\n\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 357$\\OT1/ptm/m/n/10\n.95 , AUROC$[]\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 666$\\\nOT1/ptm/m/n/10.95 ).\n\nLaTeX Warning: Reference `sec:diagnostic' on page 4 undefined on input line 211\n.\n\n\nLaTeX Warning: Reference `tab:conll' on page 4 undefined on input line 237.\n\n\nLaTeX Warning: Reference `tab:crossmodel' on page 4 undefined on input line 262\n.\n\n\nLaTeX Warning: Reference `tab:matrix' on page 4 undefined on input line 262.\n\n[4]\n\nLaTeX Warning: Reference `tab:selection' on page 5 undefined on input line 302.\n\n\n\nLaTeX Warning: Reference `fig:selection_curves' on page 5 undefined on input li\nne 302.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 368.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 368.\n\n\nLaTeX Warning: Reference `tab:nscaling' on page 5 undefined on input line 371.\n\n\nLaTeX Warning: Reference `tab:ensemble' on page 5 undefined on input line 397.\n\n[5]\n\nLaTeX Warning: Reference `tab:perrelation' on page 6 undefined on input line 42\n2.\n\n\nOverfull \\hbox (7.5464pt too wide) in paragraph at lines 459--463\n\\OT1/ptm/m/n/10.95 Stratifying in-stances by dif-fi-culty re-veals that SJ is s\ntrongest on sim-ple in-stances (en-tity count=0: $\\OML/cmm/m/it/10.95 ^^Z[]\\OT1\n/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 689$\\OT1/ptm/m/n/10.95 \n)\n\nLaTeX Warning: Reference `tab:ood' on page 6 undefined on input line 467.\n\n\nOverfull \\hbox (5.53098pt too wide) in paragraph at lines 467--469\n\\OT1/ptm/m/n/10.95 0.357 to 0.15), but struc-tural sig-nals main-tain pos-i-tiv\ne cor-re-la-tion while log-probability in-verts ($\\OML/cmm/m/it/10.95 ^^Z[][]\\O\nT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 20$\\OT1/ptm/m/n/10.95\n ).\n[6] [7]\n\nLaTeX Warning: Reference `sec:ood' on page 8 undefined on input line 508.\n\n[8] [9]\nUnderfull \\hbox (badness 4242) in paragraph at lines 708--711\n[]\\OT1/ptm/m/n/10.95 R. Vashurin et al.  A sys-tem-atic eval-u-a-tion of LLM un\n-cer-tainty quan-tifi-ca-tion meth-ods.\n[10]\n\nPackage natbib Warning: There were undefined citations.\n\n[11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/u\ntmri8a.pfb>\nOutput written on paper.pdf (11 pages, 199806 bytes).\nTranscript written on paper.log.\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/u\ntmri8a.pfb>\nOutput written on paper.pdf (11 pages, 205573 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e4e6fdbc-7528-48bf-9a84-f132395f7176",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T203201 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_cons…",
  "leafUuid": "c8601ea3-d112-4259-84ce-8bd178527c07",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper for dream_20260514T203201",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257"
}
```

---

### Assistant

_source line 38 · 2026-05-14T21:12:27.761Z_

编译成功，输出 11 页 PDF。需要第三遍确保交叉引用完全解析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8601ea3-d112-4259-84ce-8bd178527c07",
  "isSidechain": false,
  "requestId": "req_011Cb39fashPWK4PCcbQvYF8",
  "type": "assistant",
  "uuid": "3f38f46f-3436-4c11-b6a7-81c2337e12fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J37BSsBam23pdePsWDY5aH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10637,
      "cache_read_input_tokens": 59421,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 59421,
          "cache_creation_input_tokens": 10637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10637
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

_source line 39 · 2026-05-14T21:12:31.093Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0178uc3cLsS1DTCABe4mVyJZ`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -E \"(Warning|Error|Output)\" | head -10",
  "description": "Third LaTeX compile pass for cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f38f46f-3436-4c11-b6a7-81c2337e12fb",
  "isSidechain": false,
  "requestId": "req_011Cb39fashPWK4PCcbQvYF8",
  "type": "assistant",
  "uuid": "e4ad31ce-d5b0-4269-a34c-27c2ae5c116f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J37BSsBam23pdePsWDY5aH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10637,
      "cache_read_input_tokens": 59421,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 59421,
          "cache_creation_input_tokens": 10637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10637
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

_source line 40 · 2026-05-14T21:12:32.329Z_

<details><summary>↩ Tool result · `toolu_0178uc3cLsS1DTCABe4mVyJZ`</summary>

```text
Package hyperref Warning: Token not allowed in a PDF string (Unicode):
Package hyperref Warning: Token not allowed in a PDF string (Unicode):
Output written on paper.pdf (11 pages, 205573 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4ad31ce-d5b0-4269-a34c-27c2ae5c116f",
  "isSidechain": false,
  "promptId": "23021a69-dda5-4b12-987b-ef4578d19bc0",
  "type": "user",
  "uuid": "997ad043-caba-4d9e-af2e-db41c5ac6df2",
  "toolUseResult": {
    "stdout": "Package hyperref Warning: Token not allowed in a PDF string (Unicode):\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\nOutput written on paper.pdf (11 pages, 205573 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e4ad31ce-d5b0-4269-a34c-27c2ae5c116f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-14T21:12:47.981Z_

编译完成。`paper.pdf` 生成于 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.pdf`，11 页。

论文覆盖了 experiment_data.json 中全部 15 个实验：
- **Table 1** (unified): 5-signal quality estimation (baseline_logprob + evaluation_metrics_expansion)
- **Table 2** (CoNLL): cross-dataset generalization (ner_conll2003)
- **Table 3** (LLaMA): cross-model validation (ner_multi_model)
- **Table 4** (2×2 matrix): model×dataset cross-validation (ner_llama_conll)
- **Table 5** (selection): best-of-N with oracle (adaptive_compute_demo)
- **Table 6** (N-scaling): seed robustness (ner_n16_scierc + re_n16_confirmation)
- **Table 7** (ensemble): signal combination (signal_ensemble_analysis)
- **Table 8** (per-relation): diagnostic analysis (re_diagnostic_analysis)
- **Figure 1**: correlation-selection gap scatter
- **Figure 2**: selection curves (selection_curves)
- **Appendix Table**: OOD robustness (ner_ood_robustness)
- 正文段落中涵盖：baseline_exact_match、baseline_entity_voting、ner_wnut17（as abandoned）、temperature_sensitivity_analysis、capability_stratification

按 narrative guidance 调整：Claim 1 → systematic empirical comparison；Claim 2 → 含 practical decision flowchart（Section 5）；Claim 3 → empirical analysis 非 diagnostic framework；增加 closed-source API 讨论（Section 6）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "997ad043-caba-4d9e-af2e-db41c5ac6df2",
  "isSidechain": false,
  "requestId": "req_011Cb39gCSqon3dt1YgcTehk",
  "type": "assistant",
  "uuid": "c8b41823-7b2e-4170-8415-8024a593c2b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wr27pkGfg8uqxFfsGmhrSL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 222,
      "cache_read_input_tokens": 70058,
      "output_tokens": 476,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 476,
          "cache_read_input_tokens": 70058,
          "cache_creation_input_tokens": 222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 222
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T203201 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_cons…",
  "leafUuid": "c8b41823-7b2e-4170-8415-8024a593c2b4",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper for dream_20260514T203201",
  "sessionId": "2fee5174-c44d-4785-afcc-2a04a2955257"
}
```

---
