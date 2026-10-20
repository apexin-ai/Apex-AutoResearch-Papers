# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194223 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea.jsonl`
- **Structured JSON:** [`1e462e650b1db471347f.json`](../../sessions/1e/1e462e650b1db471347f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T20:03:02.998Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T20:03:02.998Z",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194223 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Claim 1 调整为 \"DIF provides a complementary contamination signal with unique RL-robustness properties\"， 强调程度差异而非 binary 生存。Claim 2 从三信号降级为双信号 + DVD failure mode analysis。 Claim 3 限定为 within-subject equating pilot，讨论 acceptable degradation bounds。 核心叙事从 \"self-healing benchmark\" 转向 \"psychometric monitoring framework with contamination-aware recalibration\"。 需补充 2-3 个 ablation 实验填补 reviewer 攻击面。仍投 ICLR，但 related work 和 limitation 需加厚。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T20:03:03.002Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T20:03:03.002Z",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-20T20:03:03.024Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194223 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Claim 1 调整为 "DIF provides a complementary contamination signal with unique RL-robustness properties"， 强调程度差异而非 binary 生存。Claim 2 从三信号降级为双信号 + DVD failure mode analysis。 Claim 3 限定为 within-subject equating pilot，讨论 acceptable degradation bounds。 核心叙事从 "self-healing benchmark" 转向 "psychometric monitoring framework with contamination-aware recalibration"。 需补充 2-3 个 ablation 实验填补 reviewer 攻击面。仍投 ICLR，但 related work 和 limitation 需加厚。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b7ed4b5f-18d3-49c6-9368-69e76c0c1e3f",
  "type": "user",
  "uuid": "44941a77-6584-484c-a286-03e91f1df8bc",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T20:03:03.023Z_

```json
{
  "parentUuid": "44941a77-6584-484c-a286-03e91f1df8bc",
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
  "uuid": "0c504535-1b0c-4663-b97c-1101a18a4dc1",
  "timestamp": "2026-05-20T20:03:03.023Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T20:03:03.023Z_

```json
{
  "parentUuid": "0c504535-1b0c-4663-b97c-1101a18a4dc1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a7616e53-7f00-4f82-8742-f67cdfa4f844",
  "timestamp": "2026-05-20T20:03:03.023Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
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
  "aiTitle": "Generate simulated paper for IRT equated benchmark",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea"
}
```

---

### Assistant

_source line 7 · 2026-05-20T20:03:05.476Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7616e53-7f00-4f82-8742-f67cdfa4f844",
  "isSidechain": false,
  "requestId": "req_011CbEREMo6hPjPqx28qFqCd",
  "type": "assistant",
  "uuid": "8a8614b0-c510-4f22-b5b3-c6eeb328fb32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEuXD1Bt4K7StZjsvRpnXN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11367,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11367,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11367
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

_source line 8 · 2026-05-20T20:03:05.993Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KXkwhZeTBE1EbzQWfLj5JJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a8614b0-c510-4f22-b5b3-c6eeb328fb32",
  "isSidechain": false,
  "requestId": "req_011CbEREMo6hPjPqx28qFqCd",
  "type": "assistant",
  "uuid": "7212d8b9-62d3-4a2b-a6b5-b07ad49d747f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEuXD1Bt4K7StZjsvRpnXN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11367,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11367,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11367
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

_source line 9 · 2026-05-20T20:03:06.375Z_

<details><summary>↩ Tool result · `toolu_01KXkwhZeTBE1EbzQWfLj5JJ`</summary>

```text
1	[
2	  {
3	    "name": "real_data_dif_mmlu",
4	    "description": "在 METABENCH MMLU 响应矩阵（5,055 models × 12,508 items）上执行 DIF 分析。 按 release date 划分 temporal cohorts（pre-2024 vs post-2024，以及更细的年度分割）。 对所有 items 运行 ETS C DIF 检测，以 MMLU-CF 为部分 ground truth 做交叉验证。\n",
5	    "results": {
6	      "n_models_after_quality_filter": 4312,
7	      "n_items_analyzable": 11847,
8	      "cohort_pre2024_size": 2876,
9	      "cohort_post2024_size": 1436,
10	      "n_items_flagged_ets_c": 743,
11	      "pct_items_flagged": 0.0627,
12	      "dif_tpr_delta_ge_1.4_vs_mmlu_cf": 0.58,
13	      "dif_tpr_delta_ge_1.0": 0.41,
14	      "dif_fpr_clean_items": 0.062,
15	      "mmlu_cf_correlation_spearman": 0.21,
16	      "mmlu_cf_correlation_p_value": 0.003,
17	      "n_items_delta_ge_1.4_estimated": 187,
18	      "n_items_delta_1.0_to_1.4_estimated": 412,
19	      "n_items_delta_lt_1.0_estimated": 144,
20	      "ets_c_auc_vs_mmlu_cf_binary": 0.71,
21	      "sensitivity_cohort_split_annual_tpr_range": "0.52-0.63",
22	      "sensitivity_threshold_sweep_tpr_range": "0.44-0.67"
23	    },
24	    "tables": [
25	      {
26	        "name": "Table 1: DIF Detection Performance on MMLU by Effect Size Band",
27	        "columns": [
28	          "effect_size_band",
29	          "n_items_estimated",
30	          "ets_c_tpr",
31	          "ets_c_fpr",
32	          "mh_tpr",
33	          "lr_tpr"
34	        ],
35	        "rows": [
36	          [
37	            "δ ≥ 1.6",
38	            68,
39	            0.69,
40	            0.058,
41	            0.54,
42	            0.61
43	          ],
44	          [
45	            "δ ∈ [1.4, 1.6)",
46	            119,
47	            0.52,
48	            0.065,
49	            0.38,
50	            0.44
51	          ],
52	          [
53	            "δ ∈ [1.0, 1.4)",
54	            412,
55	            0.41,
56	            0.063,
57	            0.27,
58	            0.33
59	          ],
60	          [
61	            "δ ∈ [0.6, 1.0)",
62	            144,
63	            0.18,
64	            0.061,
65	            0.11,
66	            0.14
67	          ],
68	          [
69	            "Clean (no contamination evidence)",
70	            "~10400",
71	            "—",
72	            0.062,
73	            "—",
74	            "—"
75	          ]
76	        ]
77	      },
78	      {
79	        "name": "Table 2: Sensitivity to Cohort Definition",
80	        "columns": [
81	          "cohort_split",
82	          "focal_n",
83	          "reference_n",
84	          "tpr_delta_ge_1.4",
85	          "fpr",
86	          "n_flagged"
87	        ],
88	        "rows": [
89	          [
90	            "pre-2024 vs post-2024",
91	            1436,
92	            2876,
93	            0.58,
94	            0.062,
95	            743
96	          ],
97	          [
98	            "pre-2023 vs post-2023",
99	            1891,
100	            2421,
101	            0.54,
102	            0.071,
103	            812
104	          ],
105	          [
106	            "Annual (2022 vs 2024+)",
107	            987,
108	            1436,
109	            0.63,
110	            0.057,
111	            691
112	          ],
113	          [
114	            "Quarterly (Q1-Q2 2023 vs Q3-Q4 2024)",
115	            623,
116	            718,
117	            0.52,
118	            0.084,
119	            658
120	          ]
121	        ]
122	      },
123	      {
124	        "name": "Table 3: MMLU-CF Cross-Validation",
125	        "columns": [
126	          "metric",
127	          "value",
128	          "95% CI"
129	        ],
130	        "rows": [
131	          [
132	            "Spearman ρ (DIF effect size vs CF accuracy gap)",
133	            0.21,
134	            "[0.09, 0.33]"
135	          ],
136	          [
137	            "Items flagged by both DIF and CF",
138	            47,
139	            "—"
140	          ],
141	          [
142	            "Items flagged by DIF only",
143	            696,
144	            "—"
145	          ],
146	          [
147	            "Items flagged by CF only",
148	            83,
149	            "—"
150	          ],
151	          [
152	            "Cohen's κ (binary agreement)",
153	            0.14,
154	            "[0.06, 0.22]"
155	          ]
156	        ]
157	      }
158	    ],
159	    "figures": [],
160	    "analysis": "核心发现：DIF 在真实数据上有统计显著的 contamination 信号，但 power 比 simulation 低约 12-18pp。 主要瓶颈是 real contamination effect sizes 分布——δ≥1.4 的 items 仅占约 25%， 而 DIF 在 δ<1.0 区间的 power 不足以独立检测。 MMLU-CF 交叉验证提供了 directional support（p=0.003）但 agreement 较低（κ=0.14）， 这既反映 DIF 的 imperfect power，也反映 CF 本身作为 ground truth 的局限性。 Cohort split sensitivity 分析显示：focal group 越小，FPR 升高（quarterly split 达 0.084）， 建议使用年度或更粗的 cohort 划分。 对 Claim 1 的影响：TPR=0.58 低于 paper framing 中承诺的 0.72-0.85 range， 需要将 claim 调整为 \"practical detection of large effects\" 并明确 medium effect 的 coverage gap。 这个 gap 恰好为 ensemble（Claim 2）提供了动机。\n\n\nSimulation 在 N=100, δ=1.4 下得到 TPR=0.758，但真实数据有三个系统性降级因素： (1) 真实 contamination effect sizes 不是均匀的 δ=1.4，多数 flagged items 落在 δ=1.0-1.4 的中间地带， 拉低了 aggregate TPR；(2) METABENCH 数据的 model heterogeneity（不同架构、不同 training recipe） 引入 DIF 分析假设之外的 noise，使得 IRT ability estimation 精度下降； (3) contamination 不是 binary uniform 的——部分 models 只接触了 partial benchmark subsets， 创造了 fuzzy group boundaries 而非 simulation 中的 clean reference/focal split。 MMLU-CF correlation 为正但弱（ρ=0.21），因为 MMLU-CF 的 modification 并非针对 DIF 设计—— 它改变了 item 内容以消除记忆优势，但有些 modification 也改变了 difficulty， 引入了 false negatives（item 有 DIF 但 CF 版本 too different to count as same construct）。 FPR 从 simulation 的 0.036-0.042 升至 0.062，因为 real data 中存在 non-contamination 来源的 DIF（如 certain model families 对特定 domain 有 architecture-driven advantages）。 δ≥1.4 的 items 仅占 flagged items 的约 25%，大部分 contamination signal 在 medium effect 区间。\n"
161	  },
162	  {
163	    "name": "rl_robustness_validation",
164	    "description": "实证验证 DIF 的 RL-robustness。构建 SFT-only 和 SFT+RL 两种 cohort， 在两种场景下运行 DIF 和传统 detectors，量化 RL 对各方法的影响。\n",
165	    "results": {
166	      "n_rl_models_identified_in_metabench": 23,
167	      "n_rl_models_added_via_inference": 12,
168	      "total_rl_models": 35,
169	      "total_sft_only_models": 187,
170	      "dif_tpr_sft_cohort_delta_ge_1.4": 0.61,
171	      "dif_tpr_rl_cohort_delta_ge_1.4": 0.54,
172	      "dif_power_retention_ratio": 0.885,
173	      "mink_auroc_sft": 0.74,
174	      "mink_auroc_rl": 0.51,
175	      "mink_power_retention": 0.689,
176	      "constat_auroc_sft": 0.69,
177	      "constat_auroc_rl": 0.58,
178	      "constat_power_retention": 0.841,
179	      "dvd_auroc_sft": 0.62,
180	      "dvd_auroc_rl": 0.56,
181	      "dvd_power_retention": 0.903,
182	      "dif_vs_best_traditional_gap_under_rl": 0.08,
183	      "gpu_hours_used": 87
184	    },
185	    "tables": [
186	      {
187	        "name": "Table 4: Detection Power Under SFT vs RL Training",
188	        "columns": [
189	          "method",
190	          "auroc_sft",
191	          "auroc_rl",
192	          "retention_ratio",
193	          "Δ_auroc"
194	        ],
195	        "rows": [
196	          [
197	            "DIF (ETS C)",
198	            0.73,
199	            0.68,
200	            0.885,
201	            -0.05
202	          ],
203	          [
204	            "Min-K%",
205	            0.74,
206	            0.51,
207	            0.689,
208	            -0.23
209	          ],
210	          [
211	            "Min-K%++",
212	            0.71,
213	            0.53,
214	            0.746,
215	            -0.18
216	          ],
217	          [
218	            "ConStat (perturbation)",
219	            0.69,
220	            0.58,
221	            0.841,
222	            -0.11
223	          ],
224	          [
225	            "DVD (generation variance)",
226	            0.62,
227	            0.56,
228	            0.903,
229	            -0.06
230	          ],
231	          [
232	            "Perplexity ratio",
233	            0.67,
234	            0.49,
235	            0.731,
236	            -0.18
237	          ],
238	          [
239	            "Zlib ratio",
240	            0.59,
241	            0.52,
242	            0.881,
243	            -0.07
244	          ]
245	        ]
246	      },
247	      {
248	        "name": "Table 5: DIF TPR Breakdown by RL Intensity",
249	        "columns": [
250	          "rl_category",
251	          "n_models",
252	          "dif_tpr_delta_ge_1.4",
253	          "mink_auroc"
254	        ],
255	        "rows": [
256	          [
257	            "SFT only",
258	            187,
259	            0.61,
260	            0.74
261	          ],
262	          [
263	            "Light RL (< 200 steps)",
264	            14,
265	            0.57,
266	            0.59
267	          ],
268	          [
269	            "Heavy RL (≥ 200 steps)",
270	            21,
271	            0.51,
272	            0.47
273	          ]
274	        ]
275	      }
276	    ],
277	    "figures": [],
278	    "analysis": "RL-robustness 存在但不 dramatic。DIF 的 retention ratio (0.885) 在所有方法中排名靠前， 但 ConStat (0.841) 也保持了 reasonable power，DVD retention 高但 baseline 低。 Median tier 下的故事不是 \"DIF 是唯一幸存者\"， 而是 \"DIF 提供了 RL-robust 且 complementary 的信号\"。 传统方法中 Min-K% 退化最严重（AUROC 0.51，接近 random）， 这与 Wang et al. 一致——output-distribution-based 方法对 RL 最脆弱。 但 performance-based 方法（ConStat）退化幅度小于预期。 Reviewer 可能攻击：(1) RL models 样本量小（n=35），统计 power 有限； (2) \"RL intensity\" 是 proxy 而非精确度量。 需在 paper 中 acknowledge 这些 limitations 并建议 future work 用 controlled RL fine-tuning 验证。\n\n\nDIF 的 power retention ratio (0.885) 高于传统方法平均值，但 gap 不如理论预期那么 dramatic。 原因：(1) RL 训练确实平滑了 output distribution（Min-K% AUROC 从 0.74 降至 0.51， 与 Wang et al. 的 14-20pp degradation 一致），但 DIF 也受到了轻微影响—— RL 不仅平滑 output，还改变了 response 的 confidence calibration， 这通过 ability estimation 间接影响 DIF（IRT θ estimates 在 RL models 上 less stable）。 (2) 传统方法在 RL 下并未完全退化到 random：ConStat AUROC=0.58（不是 0.50）， 因为 perturbation sensitivity 虽然降低但未完全消失——RL 训练通常在 original format 上做 PPO， paraphrased items 仍能 trip up 部分 RL models。 DVD 在 RL 下 AUROC=0.56，看似 retention 高（0.903），但 baseline 本身就低（0.62）， 说明 DVD 对这个 scenario 本身就不敏感而非 RL-robust。 最终 DIF vs best traditional 的 gap（在 RL 下 DIF TPR=0.54 vs ConStat AUROC=0.58） 不是 \"DIF 独活\" 的故事，而是 \"DIF 保持了 reasonable power 且是 RL-robustness 最好的之一\"。 这要求将 narrative 从 \"only survivor\" 调整为 \"most robust complement\"。\n"
279	  },
280	  {
281	    "name": "constat_perturbation_eval",
282	    "description": "独立评估 ConStat-style perturbation testing 在 MMLU 上的 contamination 检测能力。\n",
283	    "results": {
284	      "n_items_reformulated": 248,
285	      "n_models_tested": 42,
286	      "reformulation_semantic_similarity_mean": 0.91,
287	      "constat_tpr_non_rl_delta_ge_0.6": 0.47,
288	      "constat_tpr_non_rl_delta_ge_1.0": 0.58,
289	      "constat_tpr_non_rl_delta_ge_1.4": 0.64,
290	      "constat_tpr_rl_models_delta_ge_0.6": 0.23,
291	      "constat_tpr_rl_models_delta_ge_1.0": 0.31,
292	      "constat_fdr_controlled_alpha_0.05": 0.048,
293	      "constat_fdr_controlled_alpha_0.10": 0.087,
294	      "n_items_detected_fdr_0.10": 89,
295	      "overlap_with_dif_flags": 0.34,
296	      "gpu_hours_used": 72
297	    },
298	    "tables": [
299	      {
300	        "name": "Table 6: ConStat Detection Power by Effect Size and Model Type",
301	        "columns": [
302	          "effect_size_band",
303	          "tpr_non_rl",
304	          "tpr_rl",
305	          "tpr_all_models"
306	        ],
307	        "rows": [
308	          [
309	            "δ ≥ 1.4",
310	            0.64,
311	            0.31,
312	            0.53
313	          ],
314	          [
315	            "δ ∈ [1.0, 1.4)",
316	            0.58,
317	            0.28,
318	            0.48
319	          ],
320	          [
321	            "δ ∈ [0.6, 1.0)",
322	            0.47,
323	            0.23,
324	            0.39
325	          ],
326	          [
327	            "δ < 0.6",
328	            0.12,
329	            0.08,
330	            0.1
331	          ]
332	        ]
333	      },
334	      {
335	        "name": "Table 7: ConStat vs DIF Signal Overlap Analysis",
336	        "columns": [
337	          "category",
338	          "n_items",
339	          "pct_of_flagged"
340	        ],
341	        "rows": [
342	          [
343	            "Flagged by both DIF and ConStat",
344	            31,
345	            "34%"
346	          ],
347	          [
348	            "Flagged by DIF only",
349	            58,
350	            "64%"
351	          ],
352	          [
353	            "Flagged by ConStat only",
354	            52,
355	            "57%"
356	          ],
357	          [
358	            "Union (either method)",
359	            141,
360	            "—"
361	          ]
362	        ]
363	      }
364	    ],
365	    "figures": [],
366	    "analysis": "ConStat 是 ensemble 中可用的第二个信号。它在 non-RL 场景下提供了 DIF 的 complementary coverage， 尤其在 medium effect sizes（δ=0.6-1.4）——这恰好是 DIF 的 weak spot。 但 ConStat 在 RL 下 degradation 明显（TPR 从 0.47 降至 0.23）， 形成了与 DIF 的互补关系：DIF RL-robust 但需大 effect sizes，ConStat 覆盖 medium effects 但 RL-fragile。 两者 overlap 仅 34%，支持 ensemble 而非 redundancy。\n\n\nConStat 在 non-RL models 上表现 reasonable（TPR=0.47 at δ≥0.6）， 因为 perturbation sensitivity 是 memorization 的 direct signal—— memorized items 的 reformulated 版本会导致 accuracy drop， 而 genuinely understood items 不会。这在 SFT models 上工作良好。 但 TPR 未达到 ConStat 原论文 claimed 的水平，原因是： (1) MMLU 是 multiple-choice，perturbation space 受限—— 改变 stem wording 可能改变 difficulty 而非仅测 memorization； (2) LLM reformulation 质量不均匀，部分 paraphrases 引入了 subtle meaning shifts， 增加了 noise。在 RL models 上 TPR 下降到 0.23（δ≥0.6）， 因为 RL 训练增强了 models 对 input perturbation 的 robustness（PPO reward hacking 的副效应）， 使得 perturbation sensitivity 信号被 masked。 与 DIF flags 的 overlap 为 0.34——两种方法检测不同的 contamination facets， DIF 捕捉 group-level behavioral shift，ConStat 捕捉 item-level perturbation sensitivity， 这正好支持 ensemble 的 complementarity 论点。\n"
367	  },
368	  {
369	    "name": "dvd_generation_variance_eval",
370	    "description": "独立评估 DVD generation variance 在 MMLU contamination detection 上的表现。\n",
371	    "results": {
372	      "n_models_with_inference_access": 14,
373	      "n_items_tested": 248,
374	      "responses_per_item": 50,
375	      "dvd_tpr_variant_contamination": 0.38,
376	      "dvd_tpr_verbatim_contamination": 0.16,
377	      "dvd_tpr_non_variant_all": 0.19,
378	      "dvd_fpr": 0.094,
379	      "dvd_auroc_overall": 0.57,
380	      "bimodal_distribution_pct_items": 0.078,
381	      "generation_variance_mean_clean": 0.42,
382	      "generation_variance_mean_contaminated": 0.31,
383	      "generation_variance_separation_cohens_d": 0.38,
384	      "gpu_hours_used": 64
385	    },
386	    "tables": [
387	      {
388	        "name": "Table 8: DVD Detection Performance on MMLU",
389	        "columns": [
390	          "contamination_type",
391	          "n_items",
392	          "tpr",
393	          "auroc",
394	          "cohen_d"
395	        ],
396	        "rows": [
397	          [
398	            "Variant contamination",
399	            34,
400	            0.38,
401	            0.62,
402	            0.51
403	          ],
404	          [
405	            "Verbatim contamination",
406	            89,
407	            0.16,
408	            0.54,
409	            0.29
410	          ],
411	          [
412	            "Mixed/unknown",
413	            125,
414	            0.19,
415	            0.57,
416	            0.38
417	          ],
418	          [
419	            "Clean items",
420	            "~11600",
421	            "—(FPR=0.094)",
422	            "—",
423	            "—"
424	          ]
425	        ]
426	      },
427	      {
428	        "name": "Table 9: Generation Variance Statistics",
429	        "columns": [
430	          "item_category",
431	          "mean_variance",
432	          "std",
433	          "median"
434	        ],
435	        "rows": [
436	          [
437	            "Clean items",
438	            0.42,
439	            0.18,
440	            0.39
441	          ],
442	          [
443	            "Contaminated (verbatim)",
444	            0.31,
445	            0.21,
446	            0.28
447	          ],
448	          [
449	            "Contaminated (variant)",
450	            0.27,
451	            0.19,
452	            0.24
453	          ]
454	        ]
455	      }
456	    ],
457	    "figures": [],
458	    "analysis": "DVD 是 ensemble 中 failed signal。Multiple-choice format 从根本上限制了 generation variance 的信息量。 这不是 DVD method 本身的缺陷，而是 application domain mismatch。 Paper 中需要：(1) 清楚报告 DVD 的 failure 及 root cause analysis； (2) 讨论 DVD 可能在 open-ended benchmarks（如 HumanEval、MATH with free-form answers）上有效； (3) 作为 ablation study 之一，分析 format dependence 对 detection signal 的影响。 这个 negative result 反而增强 paper 的 intellectual honesty，reviewer 会 appreciate  对 failure mode 的 transparent analysis 而非 cherry-picking。\n\n\nDVD 在 median tier 下是表现最弱的信号，降级 ensemble 从 3-signal 到 2-signal 的主要原因。 核心问题：MMLU 是 multiple-choice format，generation variance 的 signal 天然被压缩—— 即使 model 记忆了答案，其 generation 仍然只是 output 一个 letter (A/B/C/D)， variance 空间极为有限。DVD 原设计针对 open-ended generation tasks， 在那里 memorized 内容会导致 deterministic long-form output（低 variance）， 但 MMLU 的 forced-choice format 使得这个信号几乎消失。 Variant contamination（model 见过 rephrased version）确实产生了 slightly higher detection（TPR=0.38）， 因为 model 在 seen variants 上的 confidence distribution 有异常—— 但这个 TPR 仍然不足以作为 reliable signal。 Verbatim contamination 的 TPR 仅 0.16，因为 correct 答案的 generation variance 在 clean 和 contaminated items 之间差异太小（Cohen's d=0.38）。 FPR=0.094 偏高，接近 actionable threshold。 这些结果表明 DVD 在 MMLU-like benchmarks 上不适用， 但需在 paper 中分析 failure mode 并讨论其在 open-ended benchmarks 上的 potential。\n"
459	  },
460	  {
461	    "name": "ensemble_fusion",
462	    "description": "将 DIF + ConStat 融合为双信号 ensemble（DVD 降级为 ablation analysis）。\n",
463	    "results": {
464	      "ensemble_type": "2-signal (DIF + ConStat)",
465	      "ensemble_tpr_delta_ge_1.4_all": 0.73,
466	      "ensemble_tpr_delta_ge_1.0_all": 0.61,
467	      "ensemble_tpr_delta_ge_0.6_all": 0.48,
468	      "ensemble_tpr_full_spectrum": 0.68,
469	      "ensemble_fpr": 0.082,
470	      "ensemble_tpr_rl_only_delta_ge_1.4": 0.59,
471	      "ensemble_tpr_non_rl_delta_ge_0.6": 0.55,
472	      "majority_voting_2of2_tpr": 0.34,
473	      "majority_voting_1of2_tpr": 0.79,
474	      "majority_voting_1of2_fpr": 0.11,
475	      "weighted_fusion_optimal_tpr": 0.73,
476	      "weighted_fusion_optimal_fpr": 0.082,
477	      "dif_weight_in_fusion": 0.58,
478	      "constat_weight_in_fusion": 0.42,
479	      "ablation_dif_only_tpr": 0.58,
480	      "ablation_constat_only_tpr": 0.47,
481	      "ablation_add_dvd_tpr_gain": 0.02,
482	      "coverage_analysis_dif_unique": 0.21,
483	      "coverage_analysis_constat_unique": 0.18,
484	      "coverage_analysis_overlap": 0.29
485	    },
486	    "tables": [
487	      {
488	        "name": "Table 10: Ensemble Fusion Strategy Comparison",
489	        "columns": [
490	          "strategy",
491	          "tpr_δ≥1.4",
492	          "tpr_δ≥0.6",
493	          "fpr",
494	          "f1"
495	        ],
496	        "rows": [
497	          [
498	            "DIF only",
499	            0.58,
500	            0.38,
501	            0.062,
502	            0.47
503	          ],
504	          [
505	            "ConStat only",
506	            0.64,
507	            0.47,
508	            0.087,
509	            0.51
510	          ],
511	          [
512	            "1-of-2 (union)",
513	            0.79,
514	            0.61,
515	            0.11,
516	            0.54
517	          ],
518	          [
519	            "2-of-2 (intersection)",
520	            0.34,
521	            0.24,
522	            0.031,
523	            0.37
524	          ],
525	          [
526	            "Weighted fusion (optimal)",
527	            0.73,
528	            0.48,
529	            0.082,
530	            0.56
531	          ]
532	        ]
533	      },
534	      {
535	        "name": "Table 11: Coverage Analysis — What Each Signal Uniquely Detects",
536	        "columns": [
537	          "scenario",
538	          "dif_alone_detects",
539	          "constat_alone_detects",
540	          "both_detect",
541	          "neither_detects"
542	        ],
543	        "rows": [
544	          [
545	            "Large effect + RL model",
546	            "✓",
547	            "✗",
548	            "—",
549	            "—"
550	          ],
551	          [
552	            "Medium effect + SFT model",
553	            "✗",
554	            "✓",
555	            "—",
556	            "—"
557	          ],
558	          [
559	            "Large effect + SFT model",
560	            "—",
561	            "—",
562	            "✓",
563	            "—"
564	          ],
565	          [
566	            "Small effect (δ<0.6)",
567	            "—",
568	            "—",
569	            "—",
570	            "✓"
571	          ]
572	        ]
573	      },
574	      {
575	        "name": "Table 12: Ablation — Value of Each Signal in Ensemble",
576	        "columns": [
577	          "configuration",
578	          "tpr_full_spectrum",
579	          "Δ_vs_full_ensemble"
580	        ],
581	        "rows": [
582	          [
583	            "DIF + ConStat (full)",
584	            0.68,
585	            "baseline"
586	          ],
587	          [
588	            "DIF only",
589	            0.58,
590	            -0.1
591	          ],
592	          [
593	            "ConStat only",
594	            0.47,
595	            -0.21
596	          ],
597	          [
598	            "DIF + ConStat + DVD",
599	            0.7,
600	            0.02
601	          ]
602	        ]
603	      }
604	    ],
605	    "figures": [],
606	    "analysis": "2-signal ensemble 在 median tier 下是 pragmatic best result： full spectrum TPR=0.68 说明 coverage 有显著 gaps（尤其 small effects + RL）， 但比任一单信号提升 10-21pp。 Paper narrative 需强调 complementarity mechanism 而非 absolute performance， 并 honestly 报告 coverage holes。 DVD ablation 提供了 principled argument for 2-signal design， 同时 DVD failure analysis 作为 Section 5.3 的 content。 Reviewer concern：FPR=0.082 接近 0.10 boundary，需讨论 false alarm cost 和 threshold tuning。\n\n\n2-signal ensemble 通过 complementarity 实现了比任一单信号更好的 coverage： DIF 覆盖 large effects + RL-robust，ConStat 覆盖 medium effects + non-RL， union coverage 高于单独使用任一方法。 Weighted fusion（DIF 0.58, ConStat 0.42）优于 simple voting， 因为 DIF 的 RL-robustness 使其在 mixed model population 中更 reliable。 2-of-2 voting 过于保守（TPR=0.34），因为两种方法检测的 contamination facet 不同—— 要求两者同时 flag 等于取 intersection 而非 union。 1-of-2 voting FPR 偏高（0.11），因为 ConStat 的 FPR contribution。 Weighted fusion 在 TPR=0.73 / FPR=0.082 处取得最佳平衡。 加入 DVD 仅带来 +0.02 TPR gain，不值得增加 pipeline 复杂度， 证实了 2-signal 降级的合理性。 Ensemble TPR=0.68（full spectrum）落在 median tier 指标范围 [0.6, 0.8] 内。\n"
607	  },
608	  {
609	    "name": "cross_benchmark_gsm8k",
610	    "description": "在 GSM8K 上复制 DIF 分析，使用 GSM1K 作为 contamination ground truth。\n",
611	    "results": {
612	      "n_models_gsm8k": 68,
613	      "n_items_gsm8k": 1319,
614	      "n_items_gsm1k": 1250,
615	      "cohort_split": "pre-2024 vs post-2024",
616	      "focal_n": 31,
617	      "reference_n": 37,
618	      "n_items_dif_flagged_gsm8k": 127,
619	      "pct_items_flagged_gsm8k": 0.096,
620	      "gsm8k_gsm1k_gap_mean_all_models": 0.073,
621	      "gsm8k_gsm1k_gap_mean_flagged_models": 0.118,
622	      "gsm8k_gsm1k_gap_dif_correlation": 0.22,
623	      "gsm8k_gsm1k_gap_correlation_p_value": 0.014,
624	      "dif_tpr_vs_gsm1k_proxy": 0.49,
625	      "dif_fpr_vs_gsm1k_proxy": 0.071,
626	      "per_model_dif_flag_count_vs_gap_r": 0.31,
627	      "gpu_hours_used": 83
628	    },
629	    "tables": [
630	      {
631	        "name": "Table 13: GSM8K DIF Results Summary",
632	        "columns": [
633	          "metric",
634	          "value",
635	          "95% CI"
636	        ],
637	        "rows": [
638	          [
639	            "Items flagged by DIF",
640	            127,
641	            "—"
642	          ],
643	          [
644	            "Mean GSM8K-GSM1K gap (all models)",
645	            "7.3%",
646	            "[5.1%, 9.5%]"
647	          ],
648	          [
649	            "Mean gap (high DIF-flag-count models)",
650	            "11.8%",
651	            "[8.2%, 15.4%]"
652	          ],
653	          [
654	            "Item-level DIF-gap correlation (ρ)",
655	            0.22,
656	            "[0.06, 0.37]"
657	          ],
658	          [
659	            "Model-level flag-count-gap correlation (r)",
660	            0.31,
661	            "[0.14, 0.47]"
662	          ]
663	        ]
664	      },
665	      {
666	        "name": "Table 14: Cross-Benchmark Comparison",
667	        "columns": [
668	          "benchmark",
669	          "n_models",
670	          "n_items",
671	          "dif_tpr",
672	          "ground_truth_correlation",
673	          "fpr"
674	        ],
675	        "rows": [
676	          [
677	            "MMLU",
678	            4312,
679	            11847,
680	            0.58,
681	            "ρ=0.21 (MMLU-CF)",
682	            0.062
683	          ],
684	          [
685	            "GSM8K",
686	            68,
687	            1319,
688	            0.49,
689	            "ρ=0.22 (GSM1K)",
690	            0.071
691	          ]
692	        ]
693	      }
694	    ],
695	    "figures": [],
696	    "analysis": "GSM8K 结果提供了 complementary 但非 decisive 的验证。 ρ=0.22 是 statistically significant 但 practically weak 的 correlation。 主要价值是证明 DIF 在不同 benchmark domain（factual vs reasoning）上都有 signal， 但 power 更低。Paper 中需讨论 math reasoning benchmarks 上 contamination 形态不同 （pattern memorization vs item memorization）作为 DIF power 下降的 explanation。 这个实验作为 supporting evidence 而非 standalone result。\n\n\nGSM8K 上的 DIF 分析面临更大挑战：(1) model sample size 更小（N=68 vs MMLU 的 4312）， 直接降低 statistical power；(2) GSM8K 是 math reasoning 而非 factual recall， contamination pattern 不同——models 可能记忆了 solution patterns 而非 specific items， DIF 对 pattern-level contamination 不如 item-level 敏感。 GSM8K-GSM1K gap correlation (ρ=0.22, p=0.014) 提供了独立验证 DIF 有 contamination 信号的证据， 但 correlation 弱于 MMLU-CF（ρ=0.21 对 ρ=0.22 看似接近，但 GSM1K 是更 clean 的 ground truth）， 反映了 math reasoning benchmark 上 contamination 形态的不同。 Per-model analysis（每个 model 被 flag 的 item count vs 其 GSM8K-GSM1K gap，r=0.31） 比 item-level correlation 更强，说明 DIF 在 model-level 上更有 discriminative power。 TPR=0.49 低于 MMLU 的 0.58，主要因为 sample size 和 effect size distribution 差异。\n"
697	  },
698	  {
699	    "name": "bifactor_irt_equating_pilot",
700	    "description": "在 MMLU 上 pilot bifactor IRT equating：拟合 bifactor model，选择 anchor items， 通过 fixed-parameter calibration 校准 replacement items。\n",
701	    "results": {
702	      "bifactor_model_converged": true,
703	      "n_general_factor_loadings_gt_0.3": 9847,
704	      "n_subject_factors": 57,
705	      "subject_factor_variance_explained_range": "0.04-0.18",
706	      "general_factor_variance_explained": 0.41,
707	      "n_anchor_items_selected": 2340,
708	      "anchor_item_dif_stability": 0.96,
709	      "within_subject_equating_spearman_rho_mean": 0.93,
710	      "within_subject_equating_rho_range": "0.89-0.97",
711	      "cross_subject_equating_spearman_rho": 0.87,
712	      "cross_subject_factor_instability_pct": 0.23,
713	      "score_reliability_original": 0.89,
714	      "score_reliability_equated_5pct_replaced": 0.87,
715	      "score_reliability_equated_20pct_replaced": 0.82,
716	      "equating_bias_mean": 0.003,
717	      "equating_rmse": 0.047
718	    },
719	    "tables": [
720	      {
721	        "name": "Table 15: Bifactor Model Fit Statistics",
722	        "columns": [
723	          "metric",
724	          "value"
725	        ],
726	        "rows": [
727	          [
728	            "General factor variance explained",
729	            0.41
730	          ],
731	          [
732	            "Mean subject-factor variance",
733	            0.09
734	          ],
735	          [
736	            "RMSEA",
737	            0.038
738	          ],
739	          [
740	            "CFI",
741	            0.94
742	          ],
743	          [
744	            "TLI",
745	            0.92
746	          ],
747	          [
748	            "Subjects with stable factor structure",
749	            "44/57 (77%)"
750	          ]
751	        ]
752	      },
753	      {
754	        "name": "Table 16: Equating Performance by Scope",
755	        "columns": [
756	          "scope",
757	          "spearman_rho",
758	          "equating_bias",
759	          "rmse",
760	          "n_items_replaced"
761	        ],
762	        "rows": [
763	          [
764	            "Within-subject (STEM avg)",
765	            0.95,
766	            0.002,
767	            0.038,
768	            47
769	          ],
770	          [
771	            "Within-subject (Humanities avg)",
772	            0.91,
773	            0.004,
774	            0.052,
775	            39
776	          ],
777	          [
778	            "Within-subject (overall)",
779	            0.93,
780	            0.003,
781	            0.047,
782	            86
783	          ],
784	          [
785	            "Cross-subject (full MMLU)",
786	            0.87,
787	            0.011,
788	            0.073,
789	            86
790	          ]
791	        ]
792	      },
793	      {
794	        "name": "Table 17: Score Reliability Under Progressive Replacement",
795	        "columns": [
796	          "pct_items_replaced",
797	          "reliability_α",
798	          "ranking_τ",
799	          "rho"
800	        ],
801	        "rows": [
802	          [
803	            "0% (baseline)",
804	            0.89,
805	            1.0,
806	            1.0
807	          ],
808	          [
809	            "5%",
810	            0.87,
811	            0.98,
812	            0.97
813	          ],
814	          [
815	            "10%",
816	            0.85,
817	            0.96,
818	            0.95
819	          ],
820	          [
821	            "20%",
822	            0.82,
823	            0.93,
824	            0.91
825	          ],
826	          [
827	            "50%",
828	            0.74,
829	            0.84,
830	            0.82
831	          ]
832	        ]
833	      }
834	    ],
835	    "figures": [],
836	    "analysis": "Within-subject equating 是 viable（ρ=0.93），但 cross-subject 不稳定（ρ=0.87） 限制了 full-benchmark equating 的 claim。 Paper 中需要：(1) 明确 scope 限制——Claim 3 rewrite 为 \"within-subject equating pilot\"； (2) 讨论 factor instability 的 root cause（model capability evolution 非 uniform across domains）； (3) 提出 subject-specific equating 作为 practical deployment strategy。 Progressive replacement 结果提供了 practical guideline：5-10% 替换安全，20% 是 borderline， 50% 不可接受。这是有用的 contribution 即使 full equating 不完美。\n\n\nBifactor model 在 MMLU 上 converges 但 reveals structural heterogeneity： general factor 仅解释 41% variance（低于典型 educational test 的 50-60%）， 因为 MMLU 覆盖 57 个 diverse subjects，跨 subject variance 大。 Within-subject equating 表现良好（mean ρ=0.93），因为 same-subject items 共享 factor structure， anchor items 稳定性高（stability=0.96）。 但 cross-subject equating（ρ=0.87）低于 within-subject，因为 23% 的 subjects 的 factor structure 在不同 model cohorts 间不稳定—— 即 model evolution 不仅改变了 ability level，也改变了 ability structure （某些 model families 在 STEM 上进步远快于 humanities）， violating bifactor model 的 factorial invariance 假设。 ρ=0.93 在 within-subject 内可行但 ρ=0.87 cross-subject 不足以支持 \"全 benchmark 等值\" 的 claim。 这迫使 Claim 3 限定 scope 为 within-subject equating pilot。 Progressive replacement 分析显示 5% 替换下 reliability 可接受（0.87）， 但 20% 替换时 reliability 降至 0.82，接近 practical minimum。\n"
837	  },
838	  {
839	    "name": "item_generation_calibration",
840	    "description": "为 DIF-flagged 的 MMLU items 生成替换 items，通过 student simulation 校准 difficulty。\n",
841	    "results": {
842	      "n_items_generated": 150,
843	      "n_items_passing_quality_filter": 118,
844	      "quality_filter_pass_rate": 0.787,
845	      "difficulty_rho_prompt_based": 0.32,
846	      "difficulty_rho_student_sim": 0.63,
847	      "difficulty_rho_student_sim_within_subject": 0.68,
848	      "discrimination_correlation": 0.41,
849	      "construct_validity_factor_loading_mean": 0.38,
850	      "construct_validity_factor_loading_original_mean": 0.47,
851	      "difficulty_mae_prompt_based": 0.34,
852	      "difficulty_mae_student_sim": 0.19,
853	      "n_items_within_0.5_logit_of_target": 74,
854	      "pct_items_within_0.5_logit": 0.627,
855	      "gpu_hours_used": 178
856	    },
857	    "tables": [
858	      {
859	        "name": "Table 18: Difficulty Calibration Comparison",
860	        "columns": [
861	          "method",
862	          "ρ_overall",
863	          "ρ_within_subject",
864	          "mae",
865	          "n_within_0.5_logit"
866	        ],
867	        "rows": [
868	          [
869	            "Prompt-based targeting",
870	            0.32,
871	            0.39,
872	            0.34,
873	            "41/118 (35%)"
874	          ],
875	          [
876	            "Student simulation",
877	            0.63,
878	            0.68,
879	            0.19,
880	            "74/118 (63%)"
881	          ],
882	          [
883	            "Student sim + iterative refinement",
884	            0.66,
885	            0.71,
886	            0.17,
887	            "79/118 (67%)"
888	          ]
889	        ]
890	      },
891	      {
892	        "name": "Table 19: Generated Item Quality Metrics",
893	        "columns": [
894	          "metric",
895	          "generated_items",
896	          "original_items",
897	          "gap"
898	        ],
899	        "rows": [
900	          [
901	            "Mean difficulty (IRT b)",
902	            -0.62,
903	            -0.84,
904	            "+0.22 (easier)"
905	          ],
906	          [
907	            "Mean discrimination (IRT a)",
908	            0.93,
909	            1.2,
910	            "-0.27"
911	          ],
912	          [
913	            "Factor loading (general)",
914	            0.38,
915	            0.47,
916	            "-0.09"
917	          ],
918	          [
919	            "Distractor effectiveness",
920	            0.61,
921	            0.78,
922	            "-0.17"
923	          ]
924	        ]
925	      }
926	    ],
927	    "figures": [],
928	    "analysis": "Student simulation calibration 是 viable 但 imperfect 的 difficulty estimation method。 ρ=0.63 的 practical implication：about 2/3 of items 在 acceptable difficulty range 内， 足够 support \"empirical calibration dramatically outperforms prompt-based\" 的 claim， 但不足以 claim \"precise psychometric replacement\"。 Construct validity gap（factor loading 0.38 vs 0.47）是 paper 需要 honestly address 的 limitation—— generated items 测量了 approximately same construct 但不 identical。 Combined with equating results (plan_005)，Claim 3 的叙事应为 \"pilot demonstration of calibrated regeneration with known quality bounds\"。\n\n\nStudent simulation calibration（ρ=0.63）显著优于 prompt-based targeting（ρ=0.32）， 因为 student simulation 通过实际 \"model population\" 响应来 estimate difficulty， 绕过了 LLM self-assessment 的 calibration 问题。 但 ρ=0.63 低于 arXiv 2601.09953 reported 的 r=0.75-0.82，原因有二： (1) 那篇论文的 evaluation 是 within-domain（同类型题目）， 而这里的 generated items 跨越了 57 subjects，domain diversity 降低了 aggregate correlation； (2) MMLU items 的 difficulty 部分来自 distractor quality， LLM generation 的 distractors 往往不如 human-crafted 的 effective， 导致 generated items systematically easier（difficulty MAE=0.19 with slight easy-bias）。 Within-subject ρ=0.68 高于 overall 的 0.63，说明 domain-specific generation 更 reliable。 Construct validity 是 soft spot：generated items 的 factor loadings（mean=0.38） 低于 original items（0.47），表明 generated items 与 underlying construct 的 alignment 较弱。 这 limits claim 强度——replacement items 在 difficulty 上校准 acceptable， 但 construct validity 有 degradation。\n"
929	  },
930	  {
931	    "name": "cumulative_bayesian_dif",
932	    "description": "实现 cumulative Bayesian DIF priors，模拟 4 次连续 benchmark administrations， 展示 evidence accumulation 带来的 power improvement。\n",
933	    "results": {
934	      "n_administrations_simulated": 4,
935	      "n_models_per_administration": 80,
936	      "power_admin_1_medium_delta_1.0": 0.33,
937	      "power_admin_2_cumulative": 0.48,
938	      "power_admin_3_cumulative": 0.59,
939	      "power_admin_4_cumulative": 0.66,
940	      "power_admin_1_large_delta_1.4": 0.55,
941	      "power_admin_4_large_delta_1.4_cumulative": 0.78,
942	      "false_positive_rate_cumulative": 0.053,
943	      "bayes_factor_threshold": 3.0,
944	      "pct_items_reaching_bf_threshold_by_admin_4": 0.71
945	    },
946	    "tables": [
947	      {
948	        "name": "Table 20: Cumulative Bayesian DIF Power Over Successive Administrations",
949	        "columns": [
950	          "administration",
951	          "n_models_cumulative",
952	          "power_δ=1.0",
953	          "power_δ=1.4",
954	          "fpr"
955	        ],
956	        "rows": [
957	          [
958	            "1",
959	            80,
960	            0.33,
961	            0.55,
962	            0.048
963	          ],
964	          [
965	            "2",
966	            160,
967	            0.48,
968	            0.67,
969	            0.051
970	          ],
971	          [
972	            "3",
973	            240,
974	            0.59,
975	            0.74,
976	            0.052
977	          ],
978	          [
979	            "4",
980	            320,
981	            0.66,
982	            0.78,
983	            0.053
984	          ]
985	        ]
986	      }
987	    ],
988	    "figures": [],
989	    "analysis": "Bayesian accumulation 是 DIF power 不足问题的 temporal solution。 核心 message：单次检测 power 有限（0.33-0.55），但 monitoring framework  通过时间积累达到 useful power（0.66-0.78 at 4 administrations）。 这 directly supports \"psychometric monitoring framework\" 的 narrative reframing—— 不是 one-shot detection 而是 continuous monitoring。 但需要注意 practical caveat：4 administrations 可能需要 1-2 年， 在此期间 contamination 已经对 benchmark validity 造成了 damage。\n\n\nBayesian accumulation 从 real-data 的 lower baseline 开始（而非 simulation 的 higher baseline）， 所以 single administration power 为 0.33（medium effect），低于 simulation 的 ~0.40。 但 accumulation dynamic 仍然 works：每次 administration 增加约 0.10-0.15 power， 到第 4 次达到 0.66——接近但未达到 simulation 预期的 0.70。 Gap 来自 real data 的 prior mis-specification：Bayesian prior 假设 DIF effects  follow specific distribution，但真实 contamination 的 temporal dynamics 不 stationary （某些 items 的 contamination 随时间变化，violating prior assumptions）。 FPR 保持在 0.053，说明 Bayesian framework 的 false alarm control 合理。 For large effects（δ=1.4），cumulative power 达到 0.78（4 administrations）， 这是 paper 中值得 highlight 的 positive result——说明 \"patience pays off\"。\n"
990	  },
991	  {
992	    "name": "graceful_degradation_analysis",
993	    "description": "分析 benchmark validity 在 progressive item replacement 下的 graceful degradation。\n",
994	    "results": {
995	      "replacement_rates_tested": [
996	        0.05,
997	        0.1,
998	        0.15,
999	        0.2,
1000	        0.3,
1001	        0.5
1002	      ],
1003	      "ranking_stability_kendall_tau_5pct": 0.97,
1004	      "ranking_stability_kendall_tau_10pct": 0.95,
1005	      "ranking_stability_kendall_tau_20pct": 0.91,
1006	      "ranking_stability_kendall_tau_50pct": 0.81,
1007	      "score_reliability_cronbach_5pct": 0.87,
1008	      "score_reliability_cronbach_10pct": 0.85,
1009	      "score_reliability_cronbach_20pct": 0.82,
1010	      "score_reliability_cronbach_50pct": 0.74,
1011	      "construct_coverage_jaccard_5pct": 0.97,
1012	      "construct_coverage_jaccard_20pct": 0.89,
1013	      "construct_coverage_jaccard_50pct": 0.76,
1014	      "theoretical_upper_bound_replacement_rate": 0.25,
1015	      "practical_recommended_max": 0.15,
1016	      "equating_error_propagation_rmse_10pct": 0.041,
1017	      "equating_error_propagation_rmse_20pct": 0.068
1018	    },
1019	    "tables": [
1020	      {
1021	        "name": "Table 21: Validity Metrics Under Progressive Replacement",
1022	        "columns": [
1023	          "replacement_rate",
1024	          "kendall_τ",
1025	          "cronbach_α",
1026	          "construct_jaccard",
1027	          "equating_rmse"
1028	        ],
1029	        "rows": [
1030	          [
1031	            "0% (baseline)",
1032	            1.0,
1033	            0.89,
1034	            1.0,
1035	            0.0
1036	          ],
1037	          [
1038	            "5%",
1039	            0.97,
1040	            0.87,
1041	            0.97,
1042	            0.029
1043	          ],
1044	          [
1045	            "10%",
1046	            0.95,
1047	            0.85,
1048	            0.94,
1049	            0.041
1050	          ],
1051	          [
1052	            "15%",
1053	            0.93,
1054	            0.84,
1055	            0.91,
1056	            0.054
1057	          ],
1058	          [
1059	            "20%",
1060	            0.91,
1061	            0.82,
1062	            0.89,
1063	            0.068
1064	          ],
1065	          [
1066	            "30%",
1067	            0.87,
1068	            0.78,
1069	            0.83,
1070	            0.091
1071	          ],
1072	          [
1073	            "50%",
1074	            0.81,
1075	            0.74,
1076	            0.76,
1077	            0.132
1078	          ]
1079	        ]
1080	      }
1081	    ],
1082	    "figures": [],
1083	    "analysis": "This experiment 提供了 Claim 3 最重要的 practical guideline： up to 15% item replacement 维持 acceptable validity，这足以处理大部分 contamination。 Paper 应将此 frame 为 \"known operating envelope\" 而非 limitation—— psychometric maturity 在于知道方法的 validity bounds，而非声称无限 scalability。 Theoretical vs practical bound gap（25% vs 15%）由 item generation quality 驱动， 指向 future work：improve generation quality → expand operating envelope。\n\n\nGraceful degradation 分析显示 benchmark validity 在 low replacement rates 下 well-preserved， 但在 >20% 时快速衰退。这符合 psychometric theory：test reliability 近似为 Spearman-Brown 函数， each replaced item 引入 calibration error（plan_006 显示 difficulty ρ=0.63）， error 随 replacement rate 线性累积但 validity impact 呈 nonlinear degradation。 15% replacement 是 practical sweet spot：ranking stability (τ=0.93) 和 reliability (α=0.84)  都在 acceptable range，且涵盖了 plan_001 中约 80% 的 δ≥1.0 flagged items。 50% replacement 的 reliability 降至 0.74，低于 psychometric 标准的 0.80 threshold—— 这是 \"benchmark 不再可比\" 的 hard boundary。 Theoretical analysis 给出 upper bound 25%（在 perfect calibration 假设下）， 但 plan_006 的 imperfect calibration 将实际 limit 压到 15%。\n"
1084	  },
1085	  {
1086	    "name": "item_focused_trees",
1087	    "description": "实现 Item-Focused Trees 作为 categorical cohort DIF 的替代方案， 将 model release date 作为连续 covariate。\n",
1088	    "results": {
1089	      "n_items_analyzed": 11847,
1090	      "n_items_significant_ift": 891,
1091	      "ift_tpr_delta_ge_1.4": 0.62,
1092	      "ift_tpr_delta_ge_1.0": 0.46,
1093	      "ift_fpr": 0.058,
1094	      "ift_vs_ets_c_tpr_gain": 0.04,
1095	      "ift_vs_ets_c_fpr_reduction": 0.004,
1096	      "ift_detected_gradual_contamination_items": 134,
1097	      "ift_split_point_mode_month": "2023-09",
1098	      "ift_computational_time_minutes": 47
1099	    },
1100	    "tables": [
1101	      {
1102	        "name": "Table 22: IFT vs Categorical DIF Comparison",
1103	        "columns": [
1104	          "method",
1105	          "tpr_δ≥1.4",
1106	          "tpr_δ≥1.0",
1107	          "fpr",
1108	          "unique_detections"
1109	        ],
1110	        "rows": [
1111	          [
1112	            "ETS C (categorical)",
1113	            0.58,
1114	            0.41,
1115	            0.062,
1116	            47
1117	          ],
1118	          [
1119	            "IFT (continuous)",
1120	            0.62,
1121	            0.46,
1122	            0.058,
1123	            134
1124	          ],
1125	          [
1126	            "Overlap (both detect)",
1127	            "—",
1128	            "—",
1129	            "—",
1130	            612
1131	          ]
1132	        ]
1133	      }
1134	    ],
1135	    "figures": [],
1136	    "analysis": "IFT 是 useful methodological extension 但非 game-changer。 Paper 中作为 robustness check 和 methodological contribution（Section 4.x）。 Gradual contamination finding 是 interesting insight， 可作为 discussion point 关于 contamination dynamics。 Reviewer 可能认为 +0.04 TPR 不值得 additional complexity； response 是 IFT 的价值在 qualitative insight（gradual contamination）而非 quantitative gain。\n\nItem-Focused Trees 提供了 modest improvement over categorical DIF（TPR +0.04, FPR -0.004）， 因为它避免了 arbitrary cohort splits 导致的 information loss—— 连续 covariate 保留了 release date 的 full ordering information。 但 improvement 幅度有限，因为 contamination 在时间上确实是 roughly step-function-like （一旦 benchmark 被 widely available，contamination 快速 saturates）， 使得 continuous treatment 的 marginal benefit 小。 IFT 的独特贡献是发现了 134 个 \"gradual contamination\" items—— 这些 items 的 DIF effect size 随时间平滑增长而非 suddenly appear， 对应 incremental leakage pattern。这在 categorical DIF 中不可见。 Split point mode 在 2023-09，大致对应 MMLU 进入 mainstream LLM training data 的时间点。\n"
1137	  }
1138	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7212d8b9-62d3-4a2b-a6b5-b07ad49d747f",
  "isSidechain": false,
  "promptId": "b7ed4b5f-18d3-49c6-9368-69e76c0c1e3f",
  "type": "user",
  "uuid": "d5e683dd-e8f3-4f2c-8cf7-40d2c776ca02",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"real_data_dif_mmlu\",\n    \"description\": \"在 METABENCH MMLU 响应矩阵（5,055 models × 12,508 items）上执行 DIF 分析。 按 release date 划分 temporal cohorts（pre-2024 vs post-2024，以及更细的年度分割）。 对所有 items 运行 ETS C DIF 检测，以 MMLU-CF 为部分 ground truth 做交叉验证。\\n\",\n    \"results\": {\n      \"n_models_after_quality_filter\": 4312,\n      \"n_items_analyzable\": 11847,\n      \"cohort_pre2024_size\": 2876,\n      \"cohort_post2024_size\": 1436,\n      \"n_items_flagged_ets_c\": 743,\n      \"pct_items_flagged\": 0.0627,\n      \"dif_tpr_delta_ge_1.4_vs_mmlu_cf\": 0.58,\n      \"dif_tpr_delta_ge_1.0\": 0.41,\n      \"dif_fpr_clean_items\": 0.062,\n      \"mmlu_cf_correlation_spearman\": 0.21,\n      \"mmlu_cf_correlation_p_value\": 0.003,\n      \"n_items_delta_ge_1.4_estimated\": 187,\n      \"n_items_delta_1.0_to_1.4_estimated\": 412,\n      \"n_items_delta_lt_1.0_estimated\": 144,\n      \"ets_c_auc_vs_mmlu_cf_binary\": 0.71,\n      \"sensitivity_cohort_split_annual_tpr_range\": \"0.52-0.63\",\n      \"sensitivity_threshold_sweep_tpr_range\": \"0.44-0.67\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: DIF Detection Performance on MMLU by Effect Size Band\",\n        \"columns\": [\n          \"effect_size_band\",\n          \"n_items_estimated\",\n          \"ets_c_tpr\",\n          \"ets_c_fpr\",\n          \"mh_tpr\",\n          \"lr_tpr\"\n        ],\n        \"rows\": [\n          [\n            \"δ ≥ 1.6\",\n            68,\n            0.69,\n            0.058,\n            0.54,\n            0.61\n          ],\n          [\n            \"δ ∈ [1.4, 1.6)\",\n            119,\n            0.52,\n            0.065,\n            0.38,\n            0.44\n          ],\n          [\n            \"δ ∈ [1.0, 1.4)\",\n            412,\n            0.41,\n            0.063,\n            0.27,\n            0.33\n          ],\n          [\n            \"δ ∈ [0.6, 1.0)\",\n            144,\n            0.18,\n            0.061,\n            0.11,\n            0.14\n          ],\n          [\n            \"Clean (no contamination evidence)\",\n            \"~10400\",\n            \"—\",\n            0.062,\n            \"—\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Sensitivity to Cohort Definition\",\n        \"columns\": [\n          \"cohort_split\",\n          \"focal_n\",\n          \"reference_n\",\n          \"tpr_delta_ge_1.4\",\n          \"fpr\",\n          \"n_flagged\"\n        ],\n        \"rows\": [\n          [\n            \"pre-2024 vs post-2024\",\n            1436,\n            2876,\n            0.58,\n            0.062,\n            743\n          ],\n          [\n            \"pre-2023 vs post-2023\",\n            1891,\n            2421,\n            0.54,\n            0.071,\n            812\n          ],\n          [\n            \"Annual (2022 vs 2024+)\",\n            987,\n            1436,\n            0.63,\n            0.057,\n            691\n          ],\n          [\n            \"Quarterly (Q1-Q2 2023 vs Q3-Q4 2024)\",\n            623,\n            718,\n            0.52,\n            0.084,\n            658\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 3: MMLU-CF Cross-Validation\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"Spearman ρ (DIF effect size vs CF accuracy gap)\",\n            0.21,\n            \"[0.09, 0.33]\"\n          ],\n          [\n            \"Items flagged by both DIF and CF\",\n            47,\n            \"—\"\n          ],\n          [\n            \"Items flagged by DIF only\",\n            696,\n            \"—\"\n          ],\n          [\n            \"Items flagged by CF only\",\n            83,\n            \"—\"\n          ],\n          [\n            \"Cohen's κ (binary agreement)\",\n            0.14,\n            \"[0.06, 0.22]\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心发现：DIF 在真实数据上有统计显著的 contamination 信号，但 power 比 simulation 低约 12-18pp。 主要瓶颈是 real contamination effect sizes 分布——δ≥1.4 的 items 仅占约 25%， 而 DIF 在 δ<1.0 区间的 power 不足以独立检测。 MMLU-CF 交叉验证提供了 directional support（p=0.003）但 agreement 较低（κ=0.14）， 这既反映 DIF 的 imperfect power，也反映 CF 本身作为 ground truth 的局限性。 Cohort split sensitivity 分析显示：focal group 越小，FPR 升高（quarterly split 达 0.084）， 建议使用年度或更粗的 cohort 划分。 对 Claim 1 的影响：TPR=0.58 低于 paper framing 中承诺的 0.72-0.85 range， 需要将 claim 调整为 \\\"practical detection of large effects\\\" 并明确 medium effect 的 coverage gap。 这个 gap 恰好为 ensemble（Claim 2）提供了动机。\\n\\n\\nSimulation 在 N=100, δ=1.4 下得到 TPR=0.758，但真实数据有三个系统性降级因素： (1) 真实 contamination effect sizes 不是均匀的 δ=1.4，多数 flagged items 落在 δ=1.0-1.4 的中间地带， 拉低了 aggregate TPR；(2) METABENCH 数据的 model heterogeneity（不同架构、不同 training recipe） 引入 DIF 分析假设之外的 noise，使得 IRT ability estimation 精度下降； (3) contamination 不是 binary uniform 的——部分 models 只接触了 partial benchmark subsets， 创造了 fuzzy group boundaries 而非 simulation 中的 clean reference/focal split。 MMLU-CF correlation 为正但弱（ρ=0.21），因为 MMLU-CF 的 modification 并非针对 DIF 设计—— 它改变了 item 内容以消除记忆优势，但有些 modification 也改变了 difficulty， 引入了 false negatives（item 有 DIF 但 CF 版本 too different to count as same construct）。 FPR 从 simulation 的 0.036-0.042 升至 0.062，因为 real data 中存在 non-contamination 来源的 DIF（如 certain model families 对特定 domain 有 architecture-driven advantages）。 δ≥1.4 的 items 仅占 flagged items 的约 25%，大部分 contamination signal 在 medium effect 区间。\\n\"\n  },\n  {\n    \"name\": \"rl_robustness_validation\",\n    \"description\": \"实证验证 DIF 的 RL-robustness。构建 SFT-only 和 SFT+RL 两种 cohort， 在两种场景下运行 DIF 和传统 detectors，量化 RL 对各方法的影响。\\n\",\n    \"results\": {\n      \"n_rl_models_identified_in_metabench\": 23,\n      \"n_rl_models_added_via_inference\": 12,\n      \"total_rl_models\": 35,\n      \"total_sft_only_models\": 187,\n      \"dif_tpr_sft_cohort_delta_ge_1.4\": 0.61,\n      \"dif_tpr_rl_cohort_delta_ge_1.4\": 0.54,\n      \"dif_power_retention_ratio\": 0.885,\n      \"mink_auroc_sft\": 0.74,\n      \"mink_auroc_rl\": 0.51,\n      \"mink_power_retention\": 0.689,\n      \"constat_auroc_sft\": 0.69,\n      \"constat_auroc_rl\": 0.58,\n      \"constat_power_retention\": 0.841,\n      \"dvd_auroc_sft\": 0.62,\n      \"dvd_auroc_rl\": 0.56,\n      \"dvd_power_retention\": 0.903,\n      \"dif_vs_best_traditional_gap_under_rl\": 0.08,\n      \"gpu_hours_used\": 87\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Detection Power Under SFT vs RL Training\",\n        \"columns\": [\n          \"method\",\n          \"auroc_sft\",\n          \"auroc_rl\",\n          \"retention_ratio\",\n          \"Δ_auroc\"\n        ],\n        \"rows\": [\n          [\n            \"DIF (ETS C)\",\n            0.73,\n            0.68,\n            0.885,\n            -0.05\n          ],\n          [\n            \"Min-K%\",\n            0.74,\n            0.51,\n            0.689,\n            -0.23\n          ],\n          [\n            \"Min-K%++\",\n            0.71,\n            0.53,\n            0.746,\n            -0.18\n          ],\n          [\n            \"ConStat (perturbation)\",\n            0.69,\n            0.58,\n            0.841,\n            -0.11\n          ],\n          [\n            \"DVD (generation variance)\",\n            0.62,\n            0.56,\n            0.903,\n            -0.06\n          ],\n          [\n            \"Perplexity ratio\",\n            0.67,\n            0.49,\n            0.731,\n            -0.18\n          ],\n          [\n            \"Zlib ratio\",\n            0.59,\n            0.52,\n            0.881,\n            -0.07\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5: DIF TPR Breakdown by RL Intensity\",\n        \"columns\": [\n          \"rl_category\",\n          \"n_models\",\n          \"dif_tpr_delta_ge_1.4\",\n          \"mink_auroc\"\n        ],\n        \"rows\": [\n          [\n            \"SFT only\",\n            187,\n            0.61,\n            0.74\n          ],\n          [\n            \"Light RL (< 200 steps)\",\n            14,\n            0.57,\n            0.59\n          ],\n          [\n            \"Heavy RL (≥ 200 steps)\",\n            21,\n            0.51,\n            0.47\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RL-robustness 存在但不 dramatic。DIF 的 retention ratio (0.885) 在所有方法中排名靠前， 但 ConStat (0.841) 也保持了 reasonable power，DVD retention 高但 baseline 低。 Median tier 下的故事不是 \\\"DIF 是唯一幸存者\\\"， 而是 \\\"DIF 提供了 RL-robust 且 complementary 的信号\\\"。 传统方法中 Min-K% 退化最严重（AUROC 0.51，接近 random）， 这与 Wang et al. 一致——output-distribution-based 方法对 RL 最脆弱。 但 performance-based 方法（ConStat）退化幅度小于预期。 Reviewer 可能攻击：(1) RL models 样本量小（n=35），统计 power 有限； (2) \\\"RL intensity\\\" 是 proxy 而非精确度量。 需在 paper 中 acknowledge 这些 limitations 并建议 future work 用 controlled RL fine-tuning 验证。\\n\\n\\nDIF 的 power retention ratio (0.885) 高于传统方法平均值，但 gap 不如理论预期那么 dramatic。 原因：(1) RL 训练确实平滑了 output distribution（Min-K% AUROC 从 0.74 降至 0.51， 与 Wang et al. 的 14-20pp degradation 一致），但 DIF 也受到了轻微影响—— RL 不仅平滑 output，还改变了 response 的 confidence calibration， 这通过 ability estimation 间接影响 DIF（IRT θ estimates 在 RL models 上 less stable）。 (2) 传统方法在 RL 下并未完全退化到 random：ConStat AUROC=0.58（不是 0.50）， 因为 perturbation sensitivity 虽然降低但未完全消失——RL 训练通常在 original format 上做 PPO， paraphrased items 仍能 trip up 部分 RL models。 DVD 在 RL 下 AUROC=0.56，看似 retention 高（0.903），但 baseline 本身就低（0.62）， 说明 DVD 对这个 scenario 本身就不敏感而非 RL-robust。 最终 DIF vs best traditional 的 gap（在 RL 下 DIF TPR=0.54 vs ConStat AUROC=0.58） 不是 \\\"DIF 独活\\\" 的故事，而是 \\\"DIF 保持了 reasonable power 且是 RL-robustness 最好的之一\\\"。 这要求将 narrative 从 \\\"only survivor\\\" 调整为 \\\"most robust complement\\\"。\\n\"\n  },\n  {\n    \"name\": \"constat_perturbation_eval\",\n    \"description\": \"独立评估 ConStat-style perturbation testing 在 MMLU 上的 contamination 检测能力。\\n\",\n    \"results\": {\n      \"n_items_reformulated\": 248,\n      \"n_models_tested\": 42,\n      \"reformulation_semantic_similarity_mean\": 0.91,\n      \"constat_tpr_non_rl_delta_ge_0.6\": 0.47,\n      \"constat_tpr_non_rl_delta_ge_1.0\": 0.58,\n      \"constat_tpr_non_rl_delta_ge_1.4\": 0.64,\n      \"constat_tpr_rl_models_delta_ge_0.6\": 0.23,\n      \"constat_tpr_rl_models_delta_ge_1.0\": 0.31,\n      \"constat_fdr_controlled_alpha_0.05\": 0.048,\n      \"constat_fdr_controlled_alpha_0.10\": 0.087,\n      \"n_items_detected_fdr_0.10\": 89,\n      \"overlap_with_dif_flags\": 0.34,\n      \"gpu_hours_used\": 72\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: ConStat Detection Power by Effect Size and Model Type\",\n        \"columns\": [\n          \"effect_size_band\",\n          \"tpr_non_rl\",\n          \"tpr_rl\",\n          \"tpr_all_models\"\n        ],\n        \"rows\": [\n          [\n            \"δ ≥ 1.4\",\n            0.64,\n            0.31,\n            0.53\n          ],\n          [\n            \"δ ∈ [1.0, 1.4)\",\n            0.58,\n            0.28,\n            0.48\n          ],\n          [\n            \"δ ∈ [0.6, 1.0)\",\n            0.47,\n            0.23,\n            0.39\n          ],\n          [\n            \"δ < 0.6\",\n            0.12,\n            0.08,\n            0.1\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7: ConStat vs DIF Signal Overlap Analysis\",\n        \"columns\": [\n          \"category\",\n          \"n_items\",\n          \"pct_of_flagged\"\n        ],\n        \"rows\": [\n          [\n            \"Flagged by both DIF and ConStat\",\n            31,\n            \"34%\"\n          ],\n          [\n            \"Flagged by DIF only\",\n            58,\n            \"64%\"\n          ],\n          [\n            \"Flagged by ConStat only\",\n            52,\n            \"57%\"\n          ],\n          [\n            \"Union (either method)\",\n            141,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ConStat 是 ensemble 中可用的第二个信号。它在 non-RL 场景下提供了 DIF 的 complementary coverage， 尤其在 medium effect sizes（δ=0.6-1.4）——这恰好是 DIF 的 weak spot。 但 ConStat 在 RL 下 degradation 明显（TPR 从 0.47 降至 0.23）， 形成了与 DIF 的互补关系：DIF RL-robust 但需大 effect sizes，ConStat 覆盖 medium effects 但 RL-fragile。 两者 overlap 仅 34%，支持 ensemble 而非 redundancy。\\n\\n\\nConStat 在 non-RL models 上表现 reasonable（TPR=0.47 at δ≥0.6）， 因为 perturbation sensitivity 是 memorization 的 direct signal—— memorized items 的 reformulated 版本会导致 accuracy drop， 而 genuinely understood items 不会。这在 SFT models 上工作良好。 但 TPR 未达到 ConStat 原论文 claimed 的水平，原因是： (1) MMLU 是 multiple-choice，perturbation space 受限—— 改变 stem wording 可能改变 difficulty 而非仅测 memorization； (2) LLM reformulation 质量不均匀，部分 paraphrases 引入了 subtle meaning shifts， 增加了 noise。在 RL models 上 TPR 下降到 0.23（δ≥0.6）， 因为 RL 训练增强了 models 对 input perturbation 的 robustness（PPO reward hacking 的副效应）， 使得 perturbation sensitivity 信号被 masked。 与 DIF flags 的 overlap 为 0.34——两种方法检测不同的 contamination facets， DIF 捕捉 group-level behavioral shift，ConStat 捕捉 item-level perturbation sensitivity， 这正好支持 ensemble 的 complementarity 论点。\\n\"\n  },\n  {\n    \"name\": \"dvd_generation_variance_eval\",\n    \"description\": \"独立评估 DVD generation variance 在 MMLU contamination detection 上的表现。\\n\",\n    \"results\": {\n      \"n_models_with_inference_access\": 14,\n      \"n_items_tested\": 248,\n      \"responses_per_item\": 50,\n      \"dvd_tpr_variant_contamination\": 0.38,\n      \"dvd_tpr_verbatim_contamination\": 0.16,\n      \"dvd_tpr_non_variant_all\": 0.19,\n      \"dvd_fpr\": 0.094,\n      \"dvd_auroc_overall\": 0.57,\n      \"bimodal_distribution_pct_items\": 0.078,\n      \"generation_variance_mean_clean\": 0.42,\n      \"generation_variance_mean_contaminated\": 0.31,\n      \"generation_variance_separation_cohens_d\": 0.38,\n      \"gpu_hours_used\": 64\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: DVD Detection Performance on MMLU\",\n        \"columns\": [\n          \"contamination_type\",\n          \"n_items\",\n          \"tpr\",\n          \"auroc\",\n          \"cohen_d\"\n        ],\n        \"rows\": [\n          [\n            \"Variant contamination\",\n            34,\n            0.38,\n            0.62,\n            0.51\n          ],\n          [\n            \"Verbatim contamination\",\n            89,\n            0.16,\n            0.54,\n            0.29\n          ],\n          [\n            \"Mixed/unknown\",\n            125,\n            0.19,\n            0.57,\n            0.38\n          ],\n          [\n            \"Clean items\",\n            \"~11600\",\n            \"—(FPR=0.094)\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: Generation Variance Statistics\",\n        \"columns\": [\n          \"item_category\",\n          \"mean_variance\",\n          \"std\",\n          \"median\"\n        ],\n        \"rows\": [\n          [\n            \"Clean items\",\n            0.42,\n            0.18,\n            0.39\n          ],\n          [\n            \"Contaminated (verbatim)\",\n            0.31,\n            0.21,\n            0.28\n          ],\n          [\n            \"Contaminated (variant)\",\n            0.27,\n            0.19,\n            0.24\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DVD 是 ensemble 中 failed signal。Multiple-choice format 从根本上限制了 generation variance 的信息量。 这不是 DVD method 本身的缺陷，而是 application domain mismatch。 Paper 中需要：(1) 清楚报告 DVD 的 failure 及 root cause analysis； (2) 讨论 DVD 可能在 open-ended benchmarks（如 HumanEval、MATH with free-form answers）上有效； (3) 作为 ablation study 之一，分析 format dependence 对 detection signal 的影响。 这个 negative result 反而增强 paper 的 intellectual honesty，reviewer 会 appreciate  对 failure mode 的 transparent analysis 而非 cherry-picking。\\n\\n\\nDVD 在 median tier 下是表现最弱的信号，降级 ensemble 从 3-signal 到 2-signal 的主要原因。 核心问题：MMLU 是 multiple-choice format，generation variance 的 signal 天然被压缩—— 即使 model 记忆了答案，其 generation 仍然只是 output 一个 letter (A/B/C/D)， variance 空间极为有限。DVD 原设计针对 open-ended generation tasks， 在那里 memorized 内容会导致 deterministic long-form output（低 variance）， 但 MMLU 的 forced-choice format 使得这个信号几乎消失。 Variant contamination（model 见过 rephrased version）确实产生了 slightly higher detection（TPR=0.38）， 因为 model 在 seen variants 上的 confidence distribution 有异常—— 但这个 TPR 仍然不足以作为 reliable signal。 Verbatim contamination 的 TPR 仅 0.16，因为 correct 答案的 generation variance 在 clean 和 contaminated items 之间差异太小（Cohen's d=0.38）。 FPR=0.094 偏高，接近 actionable threshold。 这些结果表明 DVD 在 MMLU-like benchmarks 上不适用， 但需在 paper 中分析 failure mode 并讨论其在 open-ended benchmarks 上的 potential。\\n\"\n  },\n  {\n    \"name\": \"ensemble_fusion\",\n    \"description\": \"将 DIF + ConStat 融合为双信号 ensemble（DVD 降级为 ablation analysis）。\\n\",\n    \"results\": {\n      \"ensemble_type\": \"2-signal (DIF + ConStat)\",\n      \"ensemble_tpr_delta_ge_1.4_all\": 0.73,\n      \"ensemble_tpr_delta_ge_1.0_all\": 0.61,\n      \"ensemble_tpr_delta_ge_0.6_all\": 0.48,\n      \"ensemble_tpr_full_spectrum\": 0.68,\n      \"ensemble_fpr\": 0.082,\n      \"ensemble_tpr_rl_only_delta_ge_1.4\": 0.59,\n      \"ensemble_tpr_non_rl_delta_ge_0.6\": 0.55,\n      \"majority_voting_2of2_tpr\": 0.34,\n      \"majority_voting_1of2_tpr\": 0.79,\n      \"majority_voting_1of2_fpr\": 0.11,\n      \"weighted_fusion_optimal_tpr\": 0.73,\n      \"weighted_fusion_optimal_fpr\": 0.082,\n      \"dif_weight_in_fusion\": 0.58,\n      \"constat_weight_in_fusion\": 0.42,\n      \"ablation_dif_only_tpr\": 0.58,\n      \"ablation_constat_only_tpr\": 0.47,\n      \"ablation_add_dvd_tpr_gain\": 0.02,\n      \"coverage_analysis_dif_unique\": 0.21,\n      \"coverage_analysis_constat_unique\": 0.18,\n      \"coverage_analysis_overlap\": 0.29\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Ensemble Fusion Strategy Comparison\",\n        \"columns\": [\n          \"strategy\",\n          \"tpr_δ≥1.4\",\n          \"tpr_δ≥0.6\",\n          \"fpr\",\n          \"f1\"\n        ],\n        \"rows\": [\n          [\n            \"DIF only\",\n            0.58,\n            0.38,\n            0.062,\n            0.47\n          ],\n          [\n            \"ConStat only\",\n            0.64,\n            0.47,\n            0.087,\n            0.51\n          ],\n          [\n            \"1-of-2 (union)\",\n            0.79,\n            0.61,\n            0.11,\n            0.54\n          ],\n          [\n            \"2-of-2 (intersection)\",\n            0.34,\n            0.24,\n            0.031,\n            0.37\n          ],\n          [\n            \"Weighted fusion (optimal)\",\n            0.73,\n            0.48,\n            0.082,\n            0.56\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 11: Coverage Analysis — What Each Signal Uniquely Detects\",\n        \"columns\": [\n          \"scenario\",\n          \"dif_alone_detects\",\n          \"constat_alone_detects\",\n          \"both_detect\",\n          \"neither_detects\"\n        ],\n        \"rows\": [\n          [\n            \"Large effect + RL model\",\n            \"✓\",\n            \"✗\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Medium effect + SFT model\",\n            \"✗\",\n            \"✓\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Large effect + SFT model\",\n            \"—\",\n            \"—\",\n            \"✓\",\n            \"—\"\n          ],\n          [\n            \"Small effect (δ<0.6)\",\n            \"—\",\n            \"—\",\n            \"—\",\n            \"✓\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 12: Ablation — Value of Each Signal in Ensemble\",\n        \"columns\": [\n          \"configuration\",\n          \"tpr_full_spectrum\",\n          \"Δ_vs_full_ensemble\"\n        ],\n        \"rows\": [\n          [\n            \"DIF + ConStat (full)\",\n            0.68,\n            \"baseline\"\n          ],\n          [\n            \"DIF only\",\n            0.58,\n            -0.1\n          ],\n          [\n            \"ConStat only\",\n            0.47,\n            -0.21\n          ],\n          [\n            \"DIF + ConStat + DVD\",\n            0.7,\n            0.02\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"2-signal ensemble 在 median tier 下是 pragmatic best result： full spectrum TPR=0.68 说明 coverage 有显著 gaps（尤其 small effects + RL）， 但比任一单信号提升 10-21pp。 Paper narrative 需强调 complementarity mechanism 而非 absolute performance， 并 honestly 报告 coverage holes。 DVD ablation 提供了 principled argument for 2-signal design， 同时 DVD failure analysis 作为 Section 5.3 的 content。 Reviewer concern：FPR=0.082 接近 0.10 boundary，需讨论 false alarm cost 和 threshold tuning。\\n\\n\\n2-signal ensemble 通过 complementarity 实现了比任一单信号更好的 coverage： DIF 覆盖 large effects + RL-robust，ConStat 覆盖 medium effects + non-RL， union coverage 高于单独使用任一方法。 Weighted fusion（DIF 0.58, ConStat 0.42）优于 simple voting， 因为 DIF 的 RL-robustness 使其在 mixed model population 中更 reliable。 2-of-2 voting 过于保守（TPR=0.34），因为两种方法检测的 contamination facet 不同—— 要求两者同时 flag 等于取 intersection 而非 union。 1-of-2 voting FPR 偏高（0.11），因为 ConStat 的 FPR contribution。 Weighted fusion 在 TPR=0.73 / FPR=0.082 处取得最佳平衡。 加入 DVD 仅带来 +0.02 TPR gain，不值得增加 pipeline 复杂度， 证实了 2-signal 降级的合理性。 Ensemble TPR=0.68（full spectrum）落在 median tier 指标范围 [0.6, 0.8] 内。\\n\"\n  },\n  {\n    \"name\": \"cross_benchmark_gsm8k\",\n    \"description\": \"在 GSM8K 上复制 DIF 分析，使用 GSM1K 作为 contamination ground truth。\\n\",\n    \"results\": {\n      \"n_models_gsm8k\": 68,\n      \"n_items_gsm8k\": 1319,\n      \"n_items_gsm1k\": 1250,\n      \"cohort_split\": \"pre-2024 vs post-2024\",\n      \"focal_n\": 31,\n      \"reference_n\": 37,\n      \"n_items_dif_flagged_gsm8k\": 127,\n      \"pct_items_flagged_gsm8k\": 0.096,\n      \"gsm8k_gsm1k_gap_mean_all_models\": 0.073,\n      \"gsm8k_gsm1k_gap_mean_flagged_models\": 0.118,\n      \"gsm8k_gsm1k_gap_dif_correlation\": 0.22,\n      \"gsm8k_gsm1k_gap_correlation_p_value\": 0.014,\n      \"dif_tpr_vs_gsm1k_proxy\": 0.49,\n      \"dif_fpr_vs_gsm1k_proxy\": 0.071,\n      \"per_model_dif_flag_count_vs_gap_r\": 0.31,\n      \"gpu_hours_used\": 83\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: GSM8K DIF Results Summary\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"Items flagged by DIF\",\n            127,\n            \"—\"\n          ],\n          [\n            \"Mean GSM8K-GSM1K gap (all models)\",\n            \"7.3%\",\n            \"[5.1%, 9.5%]\"\n          ],\n          [\n            \"Mean gap (high DIF-flag-count models)\",\n            \"11.8%\",\n            \"[8.2%, 15.4%]\"\n          ],\n          [\n            \"Item-level DIF-gap correlation (ρ)\",\n            0.22,\n            \"[0.06, 0.37]\"\n          ],\n          [\n            \"Model-level flag-count-gap correlation (r)\",\n            0.31,\n            \"[0.14, 0.47]\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 14: Cross-Benchmark Comparison\",\n        \"columns\": [\n          \"benchmark\",\n          \"n_models\",\n          \"n_items\",\n          \"dif_tpr\",\n          \"ground_truth_correlation\",\n          \"fpr\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            4312,\n            11847,\n            0.58,\n            \"ρ=0.21 (MMLU-CF)\",\n            0.062\n          ],\n          [\n            \"GSM8K\",\n            68,\n            1319,\n            0.49,\n            \"ρ=0.22 (GSM1K)\",\n            0.071\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"GSM8K 结果提供了 complementary 但非 decisive 的验证。 ρ=0.22 是 statistically significant 但 practically weak 的 correlation。 主要价值是证明 DIF 在不同 benchmark domain（factual vs reasoning）上都有 signal， 但 power 更低。Paper 中需讨论 math reasoning benchmarks 上 contamination 形态不同 （pattern memorization vs item memorization）作为 DIF power 下降的 explanation。 这个实验作为 supporting evidence 而非 standalone result。\\n\\n\\nGSM8K 上的 DIF 分析面临更大挑战：(1) model sample size 更小（N=68 vs MMLU 的 4312）， 直接降低 statistical power；(2) GSM8K 是 math reasoning 而非 factual recall， contamination pattern 不同——models 可能记忆了 solution patterns 而非 specific items， DIF 对 pattern-level contamination 不如 item-level 敏感。 GSM8K-GSM1K gap correlation (ρ=0.22, p=0.014) 提供了独立验证 DIF 有 contamination 信号的证据， 但 correlation 弱于 MMLU-CF（ρ=0.21 对 ρ=0.22 看似接近，但 GSM1K 是更 clean 的 ground truth）， 反映了 math reasoning benchmark 上 contamination 形态的不同。 Per-model analysis（每个 model 被 flag 的 item count vs 其 GSM8K-GSM1K gap，r=0.31） 比 item-level correlation 更强，说明 DIF 在 model-level 上更有 discriminative power。 TPR=0.49 低于 MMLU 的 0.58，主要因为 sample size 和 effect size distribution 差异。\\n\"\n  },\n  {\n    \"name\": \"bifactor_irt_equating_pilot\",\n    \"description\": \"在 MMLU 上 pilot bifactor IRT equating：拟合 bifactor model，选择 anchor items， 通过 fixed-parameter calibration 校准 replacement items。\\n\",\n    \"results\": {\n      \"bifactor_model_converged\": true,\n      \"n_general_factor_loadings_gt_0.3\": 9847,\n      \"n_subject_factors\": 57,\n      \"subject_factor_variance_explained_range\": \"0.04-0.18\",\n      \"general_factor_variance_explained\": 0.41,\n      \"n_anchor_items_selected\": 2340,\n      \"anchor_item_dif_stability\": 0.96,\n      \"within_subject_equating_spearman_rho_mean\": 0.93,\n      \"within_subject_equating_rho_range\": \"0.89-0.97\",\n      \"cross_subject_equating_spearman_rho\": 0.87,\n      \"cross_subject_factor_instability_pct\": 0.23,\n      \"score_reliability_original\": 0.89,\n      \"score_reliability_equated_5pct_replaced\": 0.87,\n      \"score_reliability_equated_20pct_replaced\": 0.82,\n      \"equating_bias_mean\": 0.003,\n      \"equating_rmse\": 0.047\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Bifactor Model Fit Statistics\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"General factor variance explained\",\n            0.41\n          ],\n          [\n            \"Mean subject-factor variance\",\n            0.09\n          ],\n          [\n            \"RMSEA\",\n            0.038\n          ],\n          [\n            \"CFI\",\n            0.94\n          ],\n          [\n            \"TLI\",\n            0.92\n          ],\n          [\n            \"Subjects with stable factor structure\",\n            \"44/57 (77%)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 16: Equating Performance by Scope\",\n        \"columns\": [\n          \"scope\",\n          \"spearman_rho\",\n          \"equating_bias\",\n          \"rmse\",\n          \"n_items_replaced\"\n        ],\n        \"rows\": [\n          [\n            \"Within-subject (STEM avg)\",\n            0.95,\n            0.002,\n            0.038,\n            47\n          ],\n          [\n            \"Within-subject (Humanities avg)\",\n            0.91,\n            0.004,\n            0.052,\n            39\n          ],\n          [\n            \"Within-subject (overall)\",\n            0.93,\n            0.003,\n            0.047,\n            86\n          ],\n          [\n            \"Cross-subject (full MMLU)\",\n            0.87,\n            0.011,\n            0.073,\n            86\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 17: Score Reliability Under Progressive Replacement\",\n        \"columns\": [\n          \"pct_items_replaced\",\n          \"reliability_α\",\n          \"ranking_τ\",\n          \"rho\"\n        ],\n        \"rows\": [\n          [\n            \"0% (baseline)\",\n            0.89,\n            1.0,\n            1.0\n          ],\n          [\n            \"5%\",\n            0.87,\n            0.98,\n            0.97\n          ],\n          [\n            \"10%\",\n            0.85,\n            0.96,\n            0.95\n          ],\n          [\n            \"20%\",\n            0.82,\n            0.93,\n            0.91\n          ],\n          [\n            \"50%\",\n            0.74,\n            0.84,\n            0.82\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Within-subject equating 是 viable（ρ=0.93），但 cross-subject 不稳定（ρ=0.87） 限制了 full-benchmark equating 的 claim。 Paper 中需要：(1) 明确 scope 限制——Claim 3 rewrite 为 \\\"within-subject equating pilot\\\"； (2) 讨论 factor instability 的 root cause（model capability evolution 非 uniform across domains）； (3) 提出 subject-specific equating 作为 practical deployment strategy。 Progressive replacement 结果提供了 practical guideline：5-10% 替换安全，20% 是 borderline， 50% 不可接受。这是有用的 contribution 即使 full equating 不完美。\\n\\n\\nBifactor model 在 MMLU 上 converges 但 reveals structural heterogeneity： general factor 仅解释 41% variance（低于典型 educational test 的 50-60%）， 因为 MMLU 覆盖 57 个 diverse subjects，跨 subject variance 大。 Within-subject equating 表现良好（mean ρ=0.93），因为 same-subject items 共享 factor structure， anchor items 稳定性高（stability=0.96）。 但 cross-subject equating（ρ=0.87）低于 within-subject，因为 23% 的 subjects 的 factor structure 在不同 model cohorts 间不稳定—— 即 model evolution 不仅改变了 ability level，也改变了 ability structure （某些 model families 在 STEM 上进步远快于 humanities）， violating bifactor model 的 factorial invariance 假设。 ρ=0.93 在 within-subject 内可行但 ρ=0.87 cross-subject 不足以支持 \\\"全 benchmark 等值\\\" 的 claim。 这迫使 Claim 3 限定 scope 为 within-subject equating pilot。 Progressive replacement 分析显示 5% 替换下 reliability 可接受（0.87）， 但 20% 替换时 reliability 降至 0.82，接近 practical minimum。\\n\"\n  },\n  {\n    \"name\": \"item_generation_calibration\",\n    \"description\": \"为 DIF-flagged 的 MMLU items 生成替换 items，通过 student simulation 校准 difficulty。\\n\",\n    \"results\": {\n      \"n_items_generated\": 150,\n      \"n_items_passing_quality_filter\": 118,\n      \"quality_filter_pass_rate\": 0.787,\n      \"difficulty_rho_prompt_based\": 0.32,\n      \"difficulty_rho_student_sim\": 0.63,\n      \"difficulty_rho_student_sim_within_subject\": 0.68,\n      \"discrimination_correlation\": 0.41,\n      \"construct_validity_factor_loading_mean\": 0.38,\n      \"construct_validity_factor_loading_original_mean\": 0.47,\n      \"difficulty_mae_prompt_based\": 0.34,\n      \"difficulty_mae_student_sim\": 0.19,\n      \"n_items_within_0.5_logit_of_target\": 74,\n      \"pct_items_within_0.5_logit\": 0.627,\n      \"gpu_hours_used\": 178\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 18: Difficulty Calibration Comparison\",\n        \"columns\": [\n          \"method\",\n          \"ρ_overall\",\n          \"ρ_within_subject\",\n          \"mae\",\n          \"n_within_0.5_logit\"\n        ],\n        \"rows\": [\n          [\n            \"Prompt-based targeting\",\n            0.32,\n            0.39,\n            0.34,\n            \"41/118 (35%)\"\n          ],\n          [\n            \"Student simulation\",\n            0.63,\n            0.68,\n            0.19,\n            \"74/118 (63%)\"\n          ],\n          [\n            \"Student sim + iterative refinement\",\n            0.66,\n            0.71,\n            0.17,\n            \"79/118 (67%)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 19: Generated Item Quality Metrics\",\n        \"columns\": [\n          \"metric\",\n          \"generated_items\",\n          \"original_items\",\n          \"gap\"\n        ],\n        \"rows\": [\n          [\n            \"Mean difficulty (IRT b)\",\n            -0.62,\n            -0.84,\n            \"+0.22 (easier)\"\n          ],\n          [\n            \"Mean discrimination (IRT a)\",\n            0.93,\n            1.2,\n            \"-0.27\"\n          ],\n          [\n            \"Factor loading (general)\",\n            0.38,\n            0.47,\n            \"-0.09\"\n          ],\n          [\n            \"Distractor effectiveness\",\n            0.61,\n            0.78,\n            \"-0.17\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Student simulation calibration 是 viable 但 imperfect 的 difficulty estimation method。 ρ=0.63 的 practical implication：about 2/3 of items 在 acceptable difficulty range 内， 足够 support \\\"empirical calibration dramatically outperforms prompt-based\\\" 的 claim， 但不足以 claim \\\"precise psychometric replacement\\\"。 Construct validity gap（factor loading 0.38 vs 0.47）是 paper 需要 honestly address 的 limitation—— generated items 测量了 approximately same construct 但不 identical。 Combined with equating results (plan_005)，Claim 3 的叙事应为 \\\"pilot demonstration of calibrated regeneration with known quality bounds\\\"。\\n\\n\\nStudent simulation calibration（ρ=0.63）显著优于 prompt-based targeting（ρ=0.32）， 因为 student simulation 通过实际 \\\"model population\\\" 响应来 estimate difficulty， 绕过了 LLM self-assessment 的 calibration 问题。 但 ρ=0.63 低于 arXiv 2601.09953 reported 的 r=0.75-0.82，原因有二： (1) 那篇论文的 evaluation 是 within-domain（同类型题目）， 而这里的 generated items 跨越了 57 subjects，domain diversity 降低了 aggregate correlation； (2) MMLU items 的 difficulty 部分来自 distractor quality， LLM generation 的 distractors 往往不如 human-crafted 的 effective， 导致 generated items systematically easier（difficulty MAE=0.19 with slight easy-bias）。 Within-subject ρ=0.68 高于 overall 的 0.63，说明 domain-specific generation 更 reliable。 Construct validity 是 soft spot：generated items 的 factor loadings（mean=0.38） 低于 original items（0.47），表明 generated items 与 underlying construct 的 alignment 较弱。 这 limits claim 强度——replacement items 在 difficulty 上校准 acceptable， 但 construct validity 有 degradation。\\n\"\n  },\n  {\n    \"name\": \"cumulative_bayesian_dif\",\n    \"description\": \"实现 cumulative Bayesian DIF priors，模拟 4 次连续 benchmark administrations， 展示 evidence accumulation 带来的 power improvement。\\n\",\n    \"results\": {\n      \"n_administrations_simulated\": 4,\n      \"n_models_per_administration\": 80,\n      \"power_admin_1_medium_delta_1.0\": 0.33,\n      \"power_admin_2_cumulative\": 0.48,\n      \"power_admin_3_cumulative\": 0.59,\n      \"power_admin_4_cumulative\": 0.66,\n      \"power_admin_1_large_delta_1.4\": 0.55,\n      \"power_admin_4_large_delta_1.4_cumulative\": 0.78,\n      \"false_positive_rate_cumulative\": 0.053,\n      \"bayes_factor_threshold\": 3.0,\n      \"pct_items_reaching_bf_threshold_by_admin_4\": 0.71\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 20: Cumulative Bayesian DIF Power Over Successive Administrations\",\n        \"columns\": [\n          \"administration\",\n          \"n_models_cumulative\",\n          \"power_δ=1.0\",\n          \"power_δ=1.4\",\n          \"fpr\"\n        ],\n        \"rows\": [\n          [\n            \"1\",\n            80,\n            0.33,\n            0.55,\n            0.048\n          ],\n          [\n            \"2\",\n            160,\n            0.48,\n            0.67,\n            0.051\n          ],\n          [\n            \"3\",\n            240,\n            0.59,\n            0.74,\n            0.052\n          ],\n          [\n            \"4\",\n            320,\n            0.66,\n            0.78,\n            0.053\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bayesian accumulation 是 DIF power 不足问题的 temporal solution。 核心 message：单次检测 power 有限（0.33-0.55），但 monitoring framework  通过时间积累达到 useful power（0.66-0.78 at 4 administrations）。 这 directly supports \\\"psychometric monitoring framework\\\" 的 narrative reframing—— 不是 one-shot detection 而是 continuous monitoring。 但需要注意 practical caveat：4 administrations 可能需要 1-2 年， 在此期间 contamination 已经对 benchmark validity 造成了 damage。\\n\\n\\nBayesian accumulation 从 real-data 的 lower baseline 开始（而非 simulation 的 higher baseline）， 所以 single administration power 为 0.33（medium effect），低于 simulation 的 ~0.40。 但 accumulation dynamic 仍然 works：每次 administration 增加约 0.10-0.15 power， 到第 4 次达到 0.66——接近但未达到 simulation 预期的 0.70。 Gap 来自 real data 的 prior mis-specification：Bayesian prior 假设 DIF effects  follow specific distribution，但真实 contamination 的 temporal dynamics 不 stationary （某些 items 的 contamination 随时间变化，violating prior assumptions）。 FPR 保持在 0.053，说明 Bayesian framework 的 false alarm control 合理。 For large effects（δ=1.4），cumulative power 达到 0.78（4 administrations）， 这是 paper 中值得 highlight 的 positive result——说明 \\\"patience pays off\\\"。\\n\"\n  },\n  {\n    \"name\": \"graceful_degradation_analysis\",\n    \"description\": \"分析 benchmark validity 在 progressive item replacement 下的 graceful degradation。\\n\",\n    \"results\": {\n      \"replacement_rates_tested\": [\n        0.05,\n        0.1,\n        0.15,\n        0.2,\n        0.3,\n        0.5\n      ],\n      \"ranking_stability_kendall_tau_5pct\": 0.97,\n      \"ranking_stability_kendall_tau_10pct\": 0.95,\n      \"ranking_stability_kendall_tau_20pct\": 0.91,\n      \"ranking_stability_kendall_tau_50pct\": 0.81,\n      \"score_reliability_cronbach_5pct\": 0.87,\n      \"score_reliability_cronbach_10pct\": 0.85,\n      \"score_reliability_cronbach_20pct\": 0.82,\n      \"score_reliability_cronbach_50pct\": 0.74,\n      \"construct_coverage_jaccard_5pct\": 0.97,\n      \"construct_coverage_jaccard_20pct\": 0.89,\n      \"construct_coverage_jaccard_50pct\": 0.76,\n      \"theoretical_upper_bound_replacement_rate\": 0.25,\n      \"practical_recommended_max\": 0.15,\n      \"equating_error_propagation_rmse_10pct\": 0.041,\n      \"equating_error_propagation_rmse_20pct\": 0.068\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 21: Validity Metrics Under Progressive Replacement\",\n        \"columns\": [\n          \"replacement_rate\",\n          \"kendall_τ\",\n          \"cronbach_α\",\n          \"construct_jaccard\",\n          \"equating_rmse\"\n        ],\n        \"rows\": [\n          [\n            \"0% (baseline)\",\n            1.0,\n            0.89,\n            1.0,\n            0.0\n          ],\n          [\n            \"5%\",\n            0.97,\n            0.87,\n            0.97,\n            0.029\n          ],\n          [\n            \"10%\",\n            0.95,\n            0.85,\n            0.94,\n            0.041\n          ],\n          [\n            \"15%\",\n            0.93,\n            0.84,\n            0.91,\n            0.054\n          ],\n          [\n            \"20%\",\n            0.91,\n            0.82,\n            0.89,\n            0.068\n          ],\n          [\n            \"30%\",\n            0.87,\n            0.78,\n            0.83,\n            0.091\n          ],\n          [\n            \"50%\",\n            0.81,\n            0.74,\n            0.76,\n            0.132\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This experiment 提供了 Claim 3 最重要的 practical guideline： up to 15% item replacement 维持 acceptable validity，这足以处理大部分 contamination。 Paper 应将此 frame 为 \\\"known operating envelope\\\" 而非 limitation—— psychometric maturity 在于知道方法的 validity bounds，而非声称无限 scalability。 Theoretical vs practical bound gap（25% vs 15%）由 item generation quality 驱动， 指向 future work：improve generation quality → expand operating envelope。\\n\\n\\nGraceful degradation 分析显示 benchmark validity 在 low replacement rates 下 well-preserved， 但在 >20% 时快速衰退。这符合 psychometric theory：test reliability 近似为 Spearman-Brown 函数， each replaced item 引入 calibration error（plan_006 显示 difficulty ρ=0.63）， error 随 replacement rate 线性累积但 validity impact 呈 nonlinear degradation。 15% replacement 是 practical sweet spot：ranking stability (τ=0.93) 和 reliability (α=0.84)  都在 acceptable range，且涵盖了 plan_001 中约 80% 的 δ≥1.0 flagged items。 50% replacement 的 reliability 降至 0.74，低于 psychometric 标准的 0.80 threshold—— 这是 \\\"benchmark 不再可比\\\" 的 hard boundary。 Theoretical analysis 给出 upper bound 25%（在 perfect calibration 假设下）， 但 plan_006 的 imperfect calibration 将实际 limit 压到 15%。\\n\"\n  },\n  {\n    \"name\": \"item_focused_trees\",\n    \"description\": \"实现 Item-Focused Trees 作为 categorical cohort DIF 的替代方案， 将 model release date 作为连续 covariate。\\n\",\n    \"results\": {\n      \"n_items_analyzed\": 11847,\n      \"n_items_significant_ift\": 891,\n      \"ift_tpr_delta_ge_1.4\": 0.62,\n      \"ift_tpr_delta_ge_1.0\": 0.46,\n      \"ift_fpr\": 0.058,\n      \"ift_vs_ets_c_tpr_gain\": 0.04,\n      \"ift_vs_ets_c_fpr_reduction\": 0.004,\n      \"ift_detected_gradual_contamination_items\": 134,\n      \"ift_split_point_mode_month\": \"2023-09\",\n      \"ift_computational_time_minutes\": 47\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 22: IFT vs Categorical DIF Comparison\",\n        \"columns\": [\n          \"method\",\n          \"tpr_δ≥1.4\",\n          \"tpr_δ≥1.0\",\n          \"fpr\",\n          \"unique_detections\"\n        ],\n        \"rows\": [\n          [\n            \"ETS C (categorical)\",\n            0.58,\n            0.41,\n            0.062,\n            47\n          ],\n          [\n            \"IFT (continuous)\",\n            0.62,\n            0.46,\n            0.058,\n            134\n          ],\n          [\n            \"Overlap (both detect)\",\n            \"—\",\n            \"—\",\n            \"—\",\n            612\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"IFT 是 useful methodological extension 但非 game-changer。 Paper 中作为 robustness check 和 methodological contribution（Section 4.x）。 Gradual contamination finding 是 interesting insight， 可作为 discussion point 关于 contamination dynamics。 Reviewer 可能认为 +0.04 TPR 不值得 additional complexity； response 是 IFT 的价值在 qualitative insight（gradual contamination）而非 quantitative gain。\\n\\nItem-Focused Trees 提供了 modest improvement over categorical DIF（TPR +0.04, FPR -0.004）， 因为它避免了 arbitrary cohort splits 导致的 information loss—— 连续 covariate 保留了 release date 的 full ordering information。 但 improvement 幅度有限，因为 contamination 在时间上确实是 roughly step-function-like （一旦 benchmark 被 widely available，contamination 快速 saturates）， 使得 continuous treatment 的 marginal benefit 小。 IFT 的独特贡献是发现了 134 个 \\\"gradual contamination\\\" items—— 这些 items 的 DIF effect size 随时间平滑增长而非 suddenly appear， 对应 incremental leakage pattern。这在 categorical DIF 中不可见。 Split point mode 在 2023-09，大致对应 MMLU 进入 mainstream LLM training data 的时间点。\\n\"\n  }\n]",
      "numLines": 1138,
      "startLine": 1,
      "totalLines": 1138
    }
  },
  "sourceToolAssistantUUID": "7212d8b9-62d3-4a2b-a6b5-b07ad49d747f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T20:03:06.493Z_

<details><summary>↩ Tool result · `toolu_01Nv9nhxaLNuCscZKwyH4PCp`</summary>

```text
1	# Paper Framing — irt_equated_bench_regen
2	
3	## Target Venue
4	- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)
5	- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)
6	- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)
7	
8	## Core Claims (3 条, 可证伪)
9	
10	**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.
11	
12	**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.
13	
14	**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.
15	
16	## Story Spine
17	
18	**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.
19	
20	**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.
21	
22	**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates the first self-healing benchmark framework.
23	
24	**Headline result template**: "On MMLU with 5,000+ models spanning 3 years of releases, DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026)."
25	
26	## Venue Fit Risks
27	
28	- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ "fairness testing for items").
29	- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: "examinees" → "models", "test items" → "benchmark questions", "DIF" → "item-level contamination signal", "equating" → "score comparability across benchmark versions".
30	- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as "bringing mature psychometric tools to solve an urgent ML problem" rather than "inventing new statistics."
31	
32	## Anticipated Reviewer Concerns
33	
34	1. **"DIF power is only sufficient for large effects (δ≥1.4)"**
35	   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.
36	   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)
37	
38	2. **"Model cohort sample sizes are too small for classical DIF"**
39	   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.
40	   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)
41	
42	3. **"Only validated in simulation"**
43	   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.
44	   - Evidence needed: plan_001, plan_004
45	
46	4. **"Item regeneration quality — how do you ensure replacements measure the same construct?"**
47	   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.
48	   - Evidence needed: plan_005, plan_006
49	
50	5. **"RL robustness is only theoretical — where's the empirical evidence?"**
51	   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.
52	   - Evidence needed: plan_002
53	
54	6. **"Computational cost of the full pipeline"**
55	   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "455f65b9-f734-4c9e-97fa-2ffee5daa10f",
  "isSidechain": false,
  "promptId": "b7ed4b5f-18d3-49c6-9368-69e76c0c1e3f",
  "type": "user",
  "uuid": "522940f9-4c75-43b4-8f46-b7cf3b3e88f0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/paper_framing.md",
      "content": "# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)\n- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)\n- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)\n\n## Core Claims (3 条, 可证伪)\n\n**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.\n\n**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.\n\n**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.\n\n**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\n\n**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates the first self-healing benchmark framework.\n\n**Headline result template**: \"On MMLU with 5,000+ models spanning 3 years of releases, DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026).\"\n\n## Venue Fit Risks\n\n- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ \"fairness testing for items\").\n- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: \"examinees\" → \"models\", \"test items\" → \"benchmark questions\", \"DIF\" → \"item-level contamination signal\", \"equating\" → \"score comparability across benchmark versions\".\n- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as \"bringing mature psychometric tools to solve an urgent ML problem\" rather than \"inventing new statistics.\"\n\n## Anticipated Reviewer Concerns\n\n1. **\"DIF power is only sufficient for large effects (δ≥1.4)\"**\n   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.\n   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)\n\n2. **\"Model cohort sample sizes are too small for classical DIF\"**\n   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.\n   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)\n\n3. **\"Only validated in simulation\"**\n   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.\n   - Evidence needed: plan_001, plan_004\n\n4. **\"Item regeneration quality — how do you ensure replacements measure the same construct?\"**\n   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.\n   - Evidence needed: plan_005, plan_006\n\n5. **\"RL robustness is only theoretical — where's the empirical evidence?\"**\n   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.\n   - Evidence needed: plan_002\n\n6. **\"Computational cost of the full pipeline\"**\n   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.\n",
      "numLines": 56,
      "startLine": 1,
      "totalLines": 56
    }
  },
  "sourceToolAssistantUUID": "455f65b9-f734-4c9e-97fa-2ffee5daa10f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T20:03:06.487Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Nv9nhxaLNuCscZKwyH4PCp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5e683dd-e8f3-4f2c-8cf7-40d2c776ca02",
  "isSidechain": false,
  "requestId": "req_011CbEREMo6hPjPqx28qFqCd",
  "type": "assistant",
  "uuid": "455f65b9-f734-4c9e-97fa-2ffee5daa10f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEuXD1Bt4K7StZjsvRpnXN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11367,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11367,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11367
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194223 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "522940f9-4c75-43b4-8f46-b7cf3b3e88f0",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for IRT equated benchmark",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea"
}
```

---

### Assistant

_source line 14 · 2026-05-20T20:03:26.383Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also read the paper-writing-norms skill for guidance on paper quality.

Actually, the instructions say I should write a "够审" (good enough for review) paper, not a publication-quality one. Let me proceed directly with writing the LaTeX paper.

Let me organize the paper structure based on the experiment data and narrative guidance:

1. **Abstract** - Psychometric monitoring framework with contamination-aware recalibration
2. **Introduction** - Problem, existing gaps, our approach
3. **Related Work** (thickened per narrative guidance)
4. **Method** - DIF analysis, ensemble detection, bifactor IRT equating


5. **Experiments** - Five subsections covering DIF detection on MMLU, RL robustness validation, contamination perturbation evaluation, variance analysis of detection failures, and ensemble fusion results, with corresponding tables for each.

Then I'm mapping out the remaining experimental sections: cross-benchmark validation on GSM8K, bifactor IRT equating, item generation and calibration, cumulative Bayesian DIF, graceful degradation analysis, and item-focused trees, each with their associated tables.

Finally, I'm structuring the discussion and limitations section with thickened narrative guidance, followed by the conclusion.

The key narrative shifts I need to make are reframing DIF as a complementary contamination signal rather than the sole solution, reducing from three signals to two with DVD failure mode analysis, piloting within-subject equating with acceptable degradation bounds, and positioning this as a psychometric monitoring framework with contamination-aware recalibration instead of a self-healing benchmark. I also need to ensure I have 2-3 ablation experiments and expand the related work and limitations sections.

Now I'm being pragmatic about the table count and starting to structure the LaTeX document to incorporate all the experimental data in a focused way.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "522940f9-4c75-43b4-8f46-b7cf3b3e88f0",
  "isSidechain": false,
  "requestId": "req_011CbEREccLHTt8ckLzL975c",
  "type": "assistant",
  "uuid": "d48c89a5-751f-4669-a64c-e0c54e251500",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018HMTE1qiEfMfAtF73mtrP8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20090,
      "cache_read_input_tokens": 23208,
      "output_tokens": 897,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20090,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 897,
          "cache_read_input_tokens": 23208,
          "cache_creation_input_tokens": 20090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20090
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

_source line 15 · 2026-05-20T20:03:26.391Z_

Now let me check the output directory exists and write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d48c89a5-751f-4669-a64c-e0c54e251500",
  "isSidechain": false,
  "requestId": "req_011CbEREccLHTt8ckLzL975c",
  "type": "assistant",
  "uuid": "42daf4da-a182-4550-ae68-61b8fa8c75d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018HMTE1qiEfMfAtF73mtrP8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20090,
      "cache_read_input_tokens": 23208,
      "output_tokens": 897,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20090,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 897,
          "cache_read_input_tokens": 23208,
          "cache_creation_input_tokens": 20090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20090
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

_source line 16 · 2026-05-20T20:03:28.336Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013S28o3dCb6njFxPbDAhQo8`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42daf4da-a182-4550-ae68-61b8fa8c75d3",
  "isSidechain": false,
  "requestId": "req_011CbEREccLHTt8ckLzL975c",
  "type": "assistant",
  "uuid": "4e107ad2-59e4-4720-b5f3-6ea1a46acd99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018HMTE1qiEfMfAtF73mtrP8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20090,
      "cache_read_input_tokens": 23208,
      "output_tokens": 897,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20090,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 897,
          "cache_read_input_tokens": 23208,
          "cache_creation_input_tokens": 20090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20090
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

_source line 17 · 2026-05-20T20:03:28.541Z_

<details><summary>↩ Tool result · `toolu_013S28o3dCb6njFxPbDAhQo8`</summary>

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
  "parentUuid": "4e107ad2-59e4-4720-b5f3-6ea1a46acd99",
  "isSidechain": false,
  "promptId": "b7ed4b5f-18d3-49c6-9368-69e76c0c1e3f",
  "type": "user",
  "uuid": "7f75e3a3-0aa6-4548-82b9-5381acc953d0",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4e107ad2-59e4-4720-b5f3-6ea1a46acd99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T20:07:47.842Z_

<details open><summary>🔧 Tool call — Write · `toolu_015X4oQW1ZhVETyjLU2epVJF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/paper.tex",
  "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage{caption}\n\n\\title{Psychometric Monitoring for LLM Benchmark Contamination:\\\\A Framework for Detection, Diagnosis, and Contamination-Aware Recalibration}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%===============================================================================\n\\begin{abstract}\n%===============================================================================\nLLM benchmarks implicitly assume temporal score comparability---that scores from models released years apart reflect the same latent ability under the same measurement instrument. Benchmark contamination systematically violates this assumption, and reinforcement learning (RL) training further conceals contamination signals by smoothing output distributions that existing detectors rely on.\nWe propose a psychometric monitoring framework grounded in Item Response Theory (IRT).\nOur first contribution shows that Differential Item Functioning (DIF) analysis provides a complementary contamination signal with unique RL-robustness properties: on MMLU with 4,312 models, DIF achieves a power retention ratio of 0.885 under RL training, compared to 0.689 for Min-K\\%.\nSecond, we construct a dual-signal ensemble combining DIF (RL-robust, large-effect coverage) with ConStat-style perturbation testing (medium-effect, non-RL coverage), achieving full-spectrum TPR of 0.68 versus 0.58 (DIF alone) and 0.47 (ConStat alone). We report DVD generation variance as a failure mode on multiple-choice formats, providing transparent analysis of its limitations.\nThird, we pilot within-subject bifactor IRT equating for contamination-aware item replacement, demonstrating that up to 15\\% of items can be replaced while maintaining ranking stability ($\\tau = 0.93$) and score reliability ($\\alpha = 0.84$).\nCross-benchmark validation on GSM8K with GSM1K ground truth confirms generalization.\nOur framework reframes benchmark maintenance from periodic manual curation to continuous psychometric monitoring with known operating bounds.\n\\end{abstract}\n\n%===============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%===============================================================================\n\nWhen we claim ``Model B outperforms Model A on MMLU,'' we implicitly assume both scores reflect the same latent ability measured under comparable conditions. Benchmark contamination---the inclusion of test items in training data---systematically erodes this comparability. The problem is compounded by the shift toward RL-trained reasoning models (o1, o3, DeepSeek-R1): Wang et al.\\ (2026) demonstrate 14--20 percentage point AUROC degradation for all reference-free contamination detectors after approximately 156 GRPO steps, reducing most methods to near-random performance ($\\sim$50\\% AUROC).\n\nExisting responses to contamination fall into three categories, each with critical gaps.\n\\emph{Dynamic benchmarks} such as LiveBench update items from recent sources but apply no psychometric calibration across versions, making temporal comparisons unreliable.\n\\emph{Performance-based detectors} such as ConStat provide FDR-controlled detection through perturbation sensitivity but rely on signals that RL training can mask.\n\\emph{Output-distribution detectors} (Min-K\\%, perplexity ratios) are the most vulnerable to RL smoothing.\nNo existing approach closes the full loop from RL-robust detection through diagnosis to psychometrically calibrated recalibration.\n\nWe argue that contamination is fundamentally a psychometric problem. When a model has memorized a benchmark item, it must answer that item correctly regardless of its general ability level---creating a detectable anomaly in the item's response pattern across model populations. This anomaly is precisely what Differential Item Functioning (DIF) measures: differential easiness of an item for one group (exposed models) relative to another (unexposed models), \\emph{after controlling for overall ability}. Because DIF operates on group-level behavioral patterns (correct/incorrect conditional on ability), not within-model output distributions, it is structurally robust to RL training---RL smooths output distributions but cannot eliminate the behavioral consequence of memorization without negating the benefit of contamination itself.\n\nThis paper makes three contributions:\n\\begin{enumerate}\n    \\item We demonstrate that DIF provides a \\textbf{complementary contamination signal with unique RL-robustness properties}. On MMLU with 4,312 models, ETS C DIF detection achieves TPR = 0.58 for large effects ($\\delta \\geq 1.4$) with FPR = 0.062, and retains 88.5\\% of its power under RL training---the highest retention ratio among all methods tested.\n    \\item We construct a \\textbf{dual-signal ensemble} (DIF + ConStat) that achieves full-spectrum TPR = 0.68, and provide a \\textbf{failure mode analysis of DVD} on multiple-choice formats explaining why generation variance is ineffective in this setting.\n    \\item We pilot \\textbf{within-subject bifactor IRT equating} for contamination-aware item replacement, establishing that up to 15\\% item replacement maintains acceptable validity ($\\tau \\geq 0.93$, $\\alpha \\geq 0.84$), with student-simulation calibration achieving difficulty correlation $\\rho = 0.68$ within subjects.\n\\end{enumerate}\n\nThe core narrative is not ``self-healing benchmarks'' but rather a \\textbf{psychometric monitoring framework with contamination-aware recalibration}---one that provides known operating bounds, transparent failure modes, and principled degradation guarantees.\n\n%===============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%===============================================================================\n\n\\paragraph{Benchmark contamination detection.}\nEarly contamination detection focused on $n$-gram overlap between training corpora and test sets (Brown et al., 2020; Dodge et al., 2021). As training data became less transparent, reference-free methods emerged. Min-K\\% (Shi et al., 2024) uses token-level log-probability statistics; ConStat (Dekoninck et al., 2024) tests whether models are more sensitive to paraphrased versions of contaminated items; DVD (Dong et al., 2024) leverages generation variance across multiple samplings. However, Wang et al.\\ (2026) show that RL training (GRPO/PPO) degrades all these methods by 14--20 pp AUROC after $\\sim$156 steps, because RL smooths the output distributions these methods rely on.\n\n\\paragraph{Dynamic and evolving benchmarks.}\nLiveBench (White et al., 2024) refreshes items monthly from recent sources. DyVal (Zhu et al., 2024) generates evaluation samples dynamically. However, neither applies psychometric calibration to ensure cross-version comparability. Growing Pains (Polo et al., 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability rather than contamination detection or remediation.\n\n\\paragraph{Psychometric methods in NLP evaluation.}\nIRT has been applied to NLP evaluation for efficiency (Lalor et al., 2019; Rodriguez et al., 2021), adaptive testing (Zhuang et al., 2023), and understanding benchmark difficulty structure (Vania et al., 2021). Bifactor models have been used to disentangle general and domain-specific abilities (Gibbons \\& Hedeker, 1992). However, DIF analysis---the standard psychometric tool for detecting item bias across groups---has not been systematically applied to LLM benchmark contamination. Our work bridges this gap.\n\n\\paragraph{DIF methodology.}\nDIF analysis originated in educational testing to detect item bias across demographic groups (Holland \\& Thayer, 1988; Swaminathan \\& Rogers, 1990). The ETS classification system (Zieky, 1993) categorizes items by DIF effect size into A (negligible), B (moderate), and C (large) categories. Item-Focused Trees (Tutz \\& Berger, 2016) extend DIF to continuous covariates. We adapt these methods to the LLM evaluation setting, where ``groups'' are defined by model release cohorts and ``ability'' is estimated via IRT.\n\n\\paragraph{Test equating.}\nTest equating ensures score comparability across different test forms (Kolen \\& Brennan, 2014). Common-item nonequivalent groups designs use anchor items to link scores. We apply fixed-parameter calibration with bifactor IRT to the benchmark regeneration setting, where contaminated items are replaced and scores must remain comparable.\n\n%===============================================================================\n\\section{Method}\n\\label{sec:method}\n%===============================================================================\n\nOur framework consists of three components: (1) DIF-based contamination detection, (2) multi-signal ensemble fusion, and (3) bifactor IRT equating for calibrated item replacement.\n\n\\subsection{DIF-Based Contamination Detection}\n\\label{sec:method-dif}\n\nLet $X_{ij} \\in \\{0,1\\}$ denote the binary response of model $i$ to item $j$, where 1 indicates a correct response. Under a 2PL IRT model, the probability of correct response is:\n\\begin{equation}\n    P(X_{ij} = 1 \\mid \\theta_i) = \\frac{1}{1 + \\exp(-a_j(\\theta_i - b_j))}\n\\end{equation}\nwhere $\\theta_i$ is the ability of model $i$, $a_j$ is the discrimination parameter, and $b_j$ is the difficulty parameter of item $j$.\n\nDIF occurs when an item has different parameters for different groups after controlling for ability. For contamination detection, we define groups by model release cohorts (e.g., pre-2024 vs.\\ post-2024). Under uniform DIF, the difficulty parameter differs between groups:\n\\begin{equation}\n    b_j^{\\text{focal}} \\neq b_j^{\\text{reference}}\n\\end{equation}\nThe DIF effect size is $\\delta_j = b_j^{\\text{reference}} - b_j^{\\text{focal}}$, with positive values indicating the item is easier for the focal (potentially contaminated) group.\n\nWe use the ETS C classification: items with $|\\delta_j| \\geq 1.0$ and statistically significant DIF are classified as C-level (large DIF), indicating potential contamination.\n\n\\paragraph{RL-robustness argument.}\nDIF operates on the Item Characteristic Curve (ICC)---the relationship between ability $\\theta$ and response probability---at the \\emph{population} level. RL training modifies a model's output distribution (token probabilities, generation diversity) but cannot eliminate the behavioral consequence that a memorized item is answered correctly. As long as contaminated models systematically outperform on specific items beyond what their ability predicts, DIF will detect the anomaly. This is structurally different from output-distribution-based methods (Min-K\\%, perplexity ratio) where RL directly degrades the signal.\n\n\\paragraph{Item-Focused Trees (IFT).}\nAs a methodological extension, we implement Item-Focused Trees that treat model release date as a continuous covariate rather than requiring categorical cohort splits. IFT recursively partitions the covariate space to identify regions where DIF is most pronounced, avoiding information loss from arbitrary temporal boundaries.\n\n\\subsection{Dual-Signal Ensemble}\n\\label{sec:method-ensemble}\n\nDIF excels at detecting large contamination effects ($\\delta \\geq 1.4$) and is RL-robust, but has limited power for medium effects ($\\delta \\in [0.6, 1.0)$). ConStat-style perturbation testing detects medium effects in non-RL models but degrades under RL training. These complementary profiles motivate a dual-signal ensemble.\n\nWe evaluate three fusion strategies:\n\\begin{itemize}\n    \\item \\textbf{Union (1-of-2)}: Flag if either signal fires. Maximizes TPR but increases FPR.\n    \\item \\textbf{Intersection (2-of-2)}: Flag only if both signals fire. Minimizes FPR but sacrifices TPR.\n    \\item \\textbf{Weighted fusion}: Combine calibrated scores with optimized weights $w_{\\text{DIF}} = 0.58$, $w_{\\text{ConStat}} = 0.42$, reflecting DIF's higher reliability under mixed model populations.\n\\end{itemize}\n\nDVD generation variance is excluded from the ensemble based on empirical evidence of its failure on multiple-choice formats (Section~\\ref{sec:dvd-failure}), but included as an ablation to justify this design decision.\n\n\\subsection{Bifactor IRT Equating}\n\\label{sec:method-equating}\n\nFor item replacement, we fit a bifactor IRT model:\n\\begin{equation}\n    P(X_{ij} = 1 \\mid \\theta_i^G, \\theta_i^{s_j}) = \\frac{1}{1 + \\exp(-[a_j^G \\theta_i^G + a_j^{s_j} \\theta_i^{s_j} - d_j])}\n\\end{equation}\nwhere $\\theta^G$ is the general ability factor, $\\theta^{s_j}$ is the subject-specific factor for item $j$'s domain, $a_j^G$ and $a_j^{s_j}$ are factor loadings, and $d_j$ is the intercept.\n\nAnchor items---those with stable DIF parameters across cohorts---are used for fixed-parameter calibration. Replacement items are generated via LLM with difficulty targeting through student simulation, then calibrated against anchor items within the same subject domain.\n\n\\paragraph{Student simulation calibration.}\nRather than relying on prompt-based difficulty estimation (which yields weak correlation with empirical difficulty, $\\rho = 0.32$), we simulate a population of ``student models'' spanning the ability spectrum to estimate replacement item difficulty empirically, achieving $\\rho = 0.63$ overall and $\\rho = 0.68$ within-subject.\n\n%===============================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%===============================================================================\n\n\\paragraph{MMLU data.}\nWe use the METABENCH response matrix containing 5,055 models and 12,508 MMLU items. After quality filtering (removing models with $<$50\\% item coverage), we retain 4,312 models and 11,847 analyzable items. Temporal cohorts: pre-2024 ($n=2{,}876$) vs.\\ post-2024 ($n=1{,}436$).\n\n\\paragraph{Ground truth.}\nFor MMLU, we use MMLU-CF (contamination-free variant) as partial ground truth. For GSM8K, we use the GSM1K accuracy gap as a proxy for contamination severity.\n\n\\paragraph{RL model identification.}\nWe identify 35 RL-trained models in METABENCH: 23 with explicit RL training documentation and 12 inferred from training pipeline descriptions. These are further categorized by RL intensity: light RL ($<$200 steps, $n=14$) and heavy RL ($\\geq$200 steps, $n=21$). SFT-only comparison group: $n=187$.\n\n\\paragraph{Baselines.}\nWe compare DIF against: Min-K\\%, Min-K\\%++, ConStat (perturbation), DVD (generation variance), perplexity ratio, and zlib ratio. We also compare ETS C categorical DIF against Mantel--Haenszel (MH) and logistic regression (LR) DIF methods.\n\n%===============================================================================\n\\section{Results}\n\\label{sec:results}\n%===============================================================================\n\n\\subsection{DIF Detection on Real MMLU Data}\n\\label{sec:dif-mmlu}\n\nTable~\\ref{tab:dif-by-effect} presents DIF detection performance stratified by contamination effect size. ETS C achieves TPR = 0.69 for items with $\\delta \\geq 1.6$ and TPR = 0.52 for $\\delta \\in [1.4, 1.6)$, with FPR controlled at 0.058--0.065 across bands. Overall, 743 items (6.3\\%) are flagged as ETS C-level DIF.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF detection performance on MMLU by effect size band (pre-2024 vs.\\ post-2024 cohorts).}\n\\label{tab:dif-by-effect}\n\\begin{tabular}{lrcccc}\n\\toprule\nEffect Size Band & $n$ (est.) & ETS C TPR & ETS C FPR & MH TPR & LR TPR \\\\\n\\midrule\n$\\delta \\geq 1.6$ & 68 & 0.69 & 0.058 & 0.54 & 0.61 \\\\\n$\\delta \\in [1.4, 1.6)$ & 119 & 0.52 & 0.065 & 0.38 & 0.44 \\\\\n$\\delta \\in [1.0, 1.4)$ & 412 & 0.41 & 0.063 & 0.27 & 0.33 \\\\\n$\\delta \\in [0.6, 1.0)$ & 144 & 0.18 & 0.061 & 0.11 & 0.14 \\\\\nClean & $\\sim$10,400 & --- & 0.062 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe aggregate TPR for $\\delta \\geq 1.4$ is 0.58, notably lower than simulation-based estimates ($\\sim$0.76). Three systematic factors explain this gap: (1) real contamination effects are not uniformly distributed at $\\delta = 1.4$---most flagged items fall in the $\\delta = 1.0$--$1.4$ range; (2) model heterogeneity in METABENCH introduces noise beyond IRT model assumptions; (3) contamination is not binary---partial benchmark exposure creates fuzzy group boundaries.\n\n\\paragraph{Cohort sensitivity.}\nTable~\\ref{tab:cohort-sensitivity} shows that DIF results are moderately sensitive to cohort definition. Annual splits (2022 vs.\\ 2024+) yield the highest TPR (0.63) with the lowest FPR (0.057), while finer quarterly splits inflate FPR to 0.084 due to small focal group sizes.\n\n\\begin{table}[h]\n\\centering\n\\caption{Sensitivity of DIF detection to cohort definition.}\n\\label{tab:cohort-sensitivity}\n\\begin{tabular}{lccccc}\n\\toprule\nCohort Split & Focal $n$ & Ref.\\ $n$ & TPR ($\\delta \\geq 1.4$) & FPR & Flagged \\\\\n\\midrule\nPre-2024 vs.\\ post-2024 & 1,436 & 2,876 & 0.58 & 0.062 & 743 \\\\\nPre-2023 vs.\\ post-2023 & 1,891 & 2,421 & 0.54 & 0.071 & 812 \\\\\nAnnual (2022 vs.\\ 2024+) & 987 & 1,436 & 0.63 & 0.057 & 691 \\\\\nQuarterly & 623 & 718 & 0.52 & 0.084 & 658 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{MMLU-CF cross-validation.}\nCross-validation against MMLU-CF yields Spearman $\\rho = 0.21$ ($p = 0.003$, 95\\% CI $[0.09, 0.33]$) between DIF effect sizes and CF accuracy gaps. Cohen's $\\kappa = 0.14$ for binary agreement reflects that DIF and CF capture different contamination facets: DIF detects group-level behavioral shifts while CF tests item-level memorization through content modification. Of flagged items, 47 are flagged by both methods, 696 by DIF only, and 83 by CF only.\n\n\\subsection{RL-Robustness Validation}\n\\label{sec:rl-robustness}\n\nTable~\\ref{tab:rl-robustness} presents detection performance under SFT-only versus RL-trained model cohorts. DIF achieves the highest power retention ratio (0.885) among all methods, with AUROC declining only from 0.73 to 0.68 under RL. In contrast, Min-K\\% degrades from 0.74 to 0.51 (retention 0.689), consistent with Wang et al.'s finding that output-distribution methods are most vulnerable to RL smoothing.\n\n\\begin{table}[h]\n\\centering\n\\caption{Contamination detection power under SFT vs.\\ RL training regimes.}\n\\label{tab:rl-robustness}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & AUROC (SFT) & AUROC (RL) & Retention & $\\Delta$ AUROC \\\\\n\\midrule\nDIF (ETS C) & 0.73 & 0.68 & 0.885 & $-0.05$ \\\\\nMin-K\\% & 0.74 & 0.51 & 0.689 & $-0.23$ \\\\\nMin-K\\%++ & 0.71 & 0.53 & 0.746 & $-0.18$ \\\\\nConStat (perturbation) & 0.69 & 0.58 & 0.841 & $-0.11$ \\\\\nDVD (generation variance) & 0.62 & 0.56 & 0.903 & $-0.06$ \\\\\nPerplexity ratio & 0.67 & 0.49 & 0.731 & $-0.18$ \\\\\nZlib ratio & 0.59 & 0.52 & 0.881 & $-0.07$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe RL-robustness story is one of \\emph{degree}, not binary survival. DIF retains the most power, but ConStat (retention 0.841) also maintains reasonable performance. DVD's high retention (0.903) is misleading---its baseline AUROC (0.62) is already low, so ``retaining'' a weak signal provides little practical value.\n\nTable~\\ref{tab:rl-intensity} breaks down DIF performance by RL intensity. Heavy RL ($\\geq$200 steps) reduces DIF TPR from 0.61 to 0.51, while light RL ($<$200 steps) has a more modest impact (TPR = 0.57). Min-K\\% degrades more steeply: from 0.74 (SFT) to 0.47 (heavy RL).\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF and Min-K\\% TPR breakdown by RL training intensity.}\n\\label{tab:rl-intensity}\n\\begin{tabular}{lccc}\n\\toprule\nRL Category & $n$ Models & DIF TPR ($\\delta \\geq 1.4$) & Min-K\\% AUROC \\\\\n\\midrule\nSFT only & 187 & 0.61 & 0.74 \\\\\nLight RL ($<$200 steps) & 14 & 0.57 & 0.59 \\\\\nHeavy RL ($\\geq$200 steps) & 21 & 0.51 & 0.47 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Limitations:} The RL model sample ($n = 35$) is small, and RL intensity is a proxy measure. We acknowledge these limitations and recommend future validation with controlled RL fine-tuning experiments.\n\n\\subsection{ConStat Perturbation Evaluation}\n\\label{sec:constat}\n\nWe independently evaluate ConStat-style perturbation testing on 248 reformulated MMLU items across 42 models (mean semantic similarity of reformulations: 0.91). Table~\\ref{tab:constat-detail} presents detection power stratified by effect size and model type.\n\n\\begin{table}[h]\n\\centering\n\\caption{ConStat detection power by effect size band and model type.}\n\\label{tab:constat-detail}\n\\begin{tabular}{lccc}\n\\toprule\nEffect Size Band & TPR (non-RL) & TPR (RL) & TPR (all) \\\\\n\\midrule\n$\\delta \\geq 1.4$ & 0.64 & 0.31 & 0.53 \\\\\n$\\delta \\in [1.0, 1.4)$ & 0.58 & 0.28 & 0.48 \\\\\n$\\delta \\in [0.6, 1.0)$ & 0.47 & 0.23 & 0.39 \\\\\n$\\delta < 0.6$ & 0.12 & 0.08 & 0.10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConStat provides complementary coverage to DIF, particularly for medium effects ($\\delta \\in [0.6, 1.0)$) where DIF TPR is only 0.18 but ConStat achieves 0.47 on non-RL models. However, ConStat degrades substantially under RL training (TPR drops from 0.47 to 0.23 at $\\delta \\geq 0.6$), because RL-trained models develop robustness to input perturbations as a side effect of PPO reward hacking.\n\nSignal overlap between DIF and ConStat is low: only 34\\% of flagged items are detected by both methods (31 items), with 58 items detected by DIF only and 52 by ConStat only. This low overlap supports ensemble construction rather than indicating redundancy.\n\n\\subsection{DVD Failure Mode Analysis}\n\\label{sec:dvd-failure}\n\nDVD generation variance performs poorly on MMLU, achieving overall AUROC of only 0.57 with FPR = 0.094. Table~\\ref{tab:dvd-performance} breaks down performance by contamination type.\n\n\\begin{table}[h]\n\\centering\n\\caption{DVD detection performance on MMLU by contamination type.}\n\\label{tab:dvd-performance}\n\\begin{tabular}{lcccc}\n\\toprule\nContamination Type & $n$ Items & TPR & AUROC & Cohen's $d$ \\\\\n\\midrule\nVariant contamination & 34 & 0.38 & 0.62 & 0.51 \\\\\nVerbatim contamination & 89 & 0.16 & 0.54 & 0.29 \\\\\nMixed/unknown & 125 & 0.19 & 0.57 & 0.38 \\\\\nClean items & $\\sim$11,600 & ---\\,(FPR=0.094) & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe root cause is format mismatch. DVD was designed for open-ended generation tasks where memorized content produces deterministic long-form output (low variance). In MMLU's forced-choice format, even memorized items produce minimal variance---the output is a single letter (A/B/C/D) regardless of whether the model memorized the answer. Generation variance between clean and contaminated items is small (mean 0.42 vs.\\ 0.31, $d = 0.38$), insufficient for reliable detection.\n\nThis negative result motivates excluding DVD from our ensemble. Adding DVD to the DIF+ConStat ensemble yields only +0.02 TPR gain (Section~\\ref{sec:ensemble}), confirming that its signal is largely redundant with or inferior to the other two methods on multiple-choice benchmarks. We note that DVD may be effective on open-ended benchmarks (e.g., HumanEval, free-form MATH) where generation variance has greater dynamic range.\n\n\\subsection{Ensemble Fusion}\n\\label{sec:ensemble}\n\nTable~\\ref{tab:ensemble-strategies} compares fusion strategies for the DIF+ConStat dual-signal ensemble.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ensemble fusion strategy comparison.}\n\\label{tab:ensemble-strategies}\n\\begin{tabular}{lcccc}\n\\toprule\nStrategy & TPR ($\\delta \\geq 1.4$) & TPR ($\\delta \\geq 0.6$) & FPR & $F_1$ \\\\\n\\midrule\nDIF only & 0.58 & 0.38 & 0.062 & 0.47 \\\\\nConStat only & 0.64 & 0.47 & 0.087 & 0.51 \\\\\n1-of-2 (union) & 0.79 & 0.61 & 0.110 & 0.54 \\\\\n2-of-2 (intersection) & 0.34 & 0.24 & 0.031 & 0.37 \\\\\nWeighted fusion (optimal) & 0.73 & 0.48 & 0.082 & 0.56 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWeighted fusion achieves the best $F_1$ (0.56) at TPR = 0.73 / FPR = 0.082, with DIF weight 0.58 and ConStat weight 0.42. The 2-of-2 intersection is overly conservative (TPR = 0.34) because the two signals detect different contamination facets---requiring both to agree takes the intersection rather than the union of their coverage.\n\n\\paragraph{Ablation: value of each signal.}\nTable~\\ref{tab:ablation} quantifies each signal's contribution. Removing ConStat reduces full-spectrum TPR by 0.10; removing DIF reduces it by 0.21, confirming DIF as the more informative signal overall. Adding DVD yields only +0.02 TPR, justifying the 2-signal design.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ablation study: contribution of each signal to ensemble TPR.}\n\\label{tab:ablation}\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & TPR (full spectrum) & $\\Delta$ vs.\\ full ensemble \\\\\n\\midrule\nDIF + ConStat (full) & 0.68 & baseline \\\\\nDIF only & 0.58 & $-0.10$ \\\\\nConStat only & 0.47 & $-0.21$ \\\\\nDIF + ConStat + DVD & 0.70 & $+0.02$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Coverage analysis.}\nThe two signals have complementary coverage profiles. DIF uniquely detects large effects in RL-trained models (21\\% of detected items), while ConStat uniquely detects medium effects in SFT models (18\\%). Both detect large effects in SFT models (29\\% overlap). Neither signal detects small effects ($\\delta < 0.6$), which is an inherent coverage gap.\n\n\\subsection{Cross-Benchmark Validation: GSM8K}\n\\label{sec:gsm8k}\n\nTo test generalization beyond factual recall benchmarks, we apply DIF analysis to GSM8K (1,319 items, 68 models) using the GSM8K--GSM1K accuracy gap as a contamination proxy (Table~\\ref{tab:gsm8k-results}).\n\n\\begin{table}[h]\n\\centering\n\\caption{GSM8K DIF analysis results.}\n\\label{tab:gsm8k-results}\n\\begin{tabular}{lcc}\n\\toprule\nMetric & Value & 95\\% CI \\\\\n\\midrule\nItems flagged by DIF & 127 & --- \\\\\nMean GSM8K--GSM1K gap (all models) & 7.3\\% & [5.1\\%, 9.5\\%] \\\\\nMean gap (high DIF-flag-count models) & 11.8\\% & [8.2\\%, 15.4\\%] \\\\\nItem-level DIF-gap correlation ($\\rho$) & 0.22 & [0.06, 0.37] \\\\\nModel-level flag-count-gap correlation ($r$) & 0.31 & [0.14, 0.47] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDIF detects contamination signal on GSM8K ($\\rho = 0.22$, $p = 0.014$), though with lower power than MMLU (TPR = 0.49 vs.\\ 0.58). The model-level correlation ($r = 0.31$) is stronger, suggesting DIF has more discriminative power at identifying contaminated \\emph{models} than contaminated \\emph{items} in this setting. Table~\\ref{tab:cross-benchmark} compares results across benchmarks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-benchmark comparison of DIF detection.}\n\\label{tab:cross-benchmark}\n\\begin{tabular}{lccccc}\n\\toprule\nBenchmark & $n$ Models & $n$ Items & DIF TPR & Ground Truth $\\rho$ & FPR \\\\\n\\midrule\nMMLU & 4,312 & 11,847 & 0.58 & 0.21 (MMLU-CF) & 0.062 \\\\\nGSM8K & 68 & 1,319 & 0.49 & 0.22 (GSM1K) & 0.071 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe lower TPR on GSM8K reflects both smaller sample size ($n = 68$ vs.\\ 4,312) and different contamination patterns: math reasoning benchmarks involve pattern memorization rather than item memorization, which DIF is less sensitive to.\n\n\\subsection{Bifactor IRT Equating Pilot}\n\\label{sec:equating}\n\nWe fit a bifactor IRT model to the MMLU response matrix, extracting one general factor and 57 subject-specific factors. Table~\\ref{tab:bifactor-fit} presents model fit statistics.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bifactor model fit statistics for MMLU.}\n\\label{tab:bifactor-fit}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nGeneral factor variance explained & 0.41 \\\\\nMean subject-factor variance & 0.09 \\\\\nRMSEA & 0.038 \\\\\nCFI & 0.94 \\\\\nTLI & 0.92 \\\\\nSubjects with stable factor structure & 44/57 (77\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe general factor explains 41\\% of variance---lower than typical educational tests (50--60\\%)---reflecting MMLU's coverage of 57 diverse subjects. Model fit (RMSEA = 0.038, CFI = 0.94) is adequate.\n\nTable~\\ref{tab:equating-scope} compares within-subject and cross-subject equating performance. Within-subject equating achieves mean $\\rho = 0.93$ with low bias (0.003) and RMSE (0.047). Cross-subject equating is weaker ($\\rho = 0.87$, RMSE = 0.073) because 23\\% of subjects have unstable factor structures across model cohorts---model evolution changes not just ability levels but ability \\emph{structure} across domains.\n\n\\begin{table}[h]\n\\centering\n\\caption{Equating performance by scope.}\n\\label{tab:equating-scope}\n\\begin{tabular}{lcccc}\n\\toprule\nScope & $\\rho$ & Bias & RMSE & $n$ Replaced \\\\\n\\midrule\nWithin-subject (STEM avg) & 0.95 & 0.002 & 0.038 & 47 \\\\\nWithin-subject (Humanities avg) & 0.91 & 0.004 & 0.052 & 39 \\\\\nWithin-subject (overall) & 0.93 & 0.003 & 0.047 & 86 \\\\\nCross-subject (full MMLU) & 0.87 & 0.011 & 0.073 & 86 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe therefore scope our equating claim to within-subject replacement and present cross-subject results as an area for future improvement.\n\n\\subsection{Item Generation and Calibration}\n\\label{sec:item-gen}\n\nWe generate 150 replacement items for DIF-flagged MMLU items, of which 118 pass quality filters (pass rate 78.7\\%). Table~\\ref{tab:calibration} compares difficulty calibration methods.\n\n\\begin{table}[h]\n\\centering\n\\caption{Difficulty calibration: prompt-based vs.\\ student simulation.}\n\\label{tab:calibration}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & $\\rho$ (overall) & $\\rho$ (within-subj.) & MAE & Within 0.5 logit \\\\\n\\midrule\nPrompt-based targeting & 0.32 & 0.39 & 0.34 & 41/118 (35\\%) \\\\\nStudent simulation & 0.63 & 0.68 & 0.19 & 74/118 (63\\%) \\\\\nStudent sim + iterative & 0.66 & 0.71 & 0.17 & 79/118 (67\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStudent simulation dramatically outperforms prompt-based targeting ($\\rho = 0.63$ vs.\\ 0.32), confirming that empirical calibration through model population responses is essential. However, generated items show systematic quality gaps relative to originals: lower discrimination ($a = 0.93$ vs.\\ 1.20), lower factor loadings (0.38 vs.\\ 0.47), and less effective distractors (0.61 vs.\\ 0.78). These gaps constrain the practical replacement rate.\n\n\\begin{table}[h]\n\\centering\n\\caption{Generated vs.\\ original item quality metrics.}\n\\label{tab:item-quality}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Generated & Original & Gap \\\\\n\\midrule\nMean difficulty (IRT $b$) & $-0.62$ & $-0.84$ & $+0.22$ \\\\\nMean discrimination (IRT $a$) & 0.93 & 1.20 & $-0.27$ \\\\\nFactor loading (general) & 0.38 & 0.47 & $-0.09$ \\\\\nDistractor effectiveness & 0.61 & 0.78 & $-0.17$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cumulative Bayesian DIF}\n\\label{sec:bayesian}\n\nSingle-administration DIF power is limited, particularly for medium effects (TPR = 0.33 at $\\delta = 1.0$). We implement cumulative Bayesian DIF priors that accumulate evidence across successive benchmark administrations. Table~\\ref{tab:bayesian-power} shows power growth over four simulated administrations of 80 models each.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cumulative Bayesian DIF power over successive administrations.}\n\\label{tab:bayesian-power}\n\\begin{tabular}{lcccc}\n\\toprule\nAdmin. & $n$ Models (cumul.) & Power ($\\delta=1.0$) & Power ($\\delta=1.4$) & FPR \\\\\n\\midrule\n1 & 80 & 0.33 & 0.55 & 0.048 \\\\\n2 & 160 & 0.48 & 0.67 & 0.051 \\\\\n3 & 240 & 0.59 & 0.74 & 0.052 \\\\\n4 & 320 & 0.66 & 0.78 & 0.053 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAfter four administrations, power for large effects reaches 0.78 and for medium effects 0.66, while FPR remains controlled at 0.053. This supports the ``monitoring framework'' narrative: single-shot detection has limited power, but continuous monitoring with evidence accumulation achieves useful detection rates. The practical caveat is that four administrations may require 1--2 years, during which contamination has already impacted benchmark validity.\n\n\\subsection{Graceful Degradation Analysis}\n\\label{sec:degradation}\n\nTable~\\ref{tab:degradation} characterizes benchmark validity under progressive item replacement.\n\n\\begin{table}[h]\n\\centering\n\\caption{Validity metrics under progressive item replacement.}\n\\label{tab:degradation}\n\\begin{tabular}{lcccc}\n\\toprule\nReplacement Rate & Kendall's $\\tau$ & Cronbach's $\\alpha$ & Construct Jaccard & Equating RMSE \\\\\n\\midrule\n0\\% (baseline) & 1.00 & 0.89 & 1.00 & 0.000 \\\\\n5\\% & 0.97 & 0.87 & 0.97 & 0.029 \\\\\n10\\% & 0.95 & 0.85 & 0.94 & 0.041 \\\\\n15\\% & 0.93 & 0.84 & 0.91 & 0.054 \\\\\n20\\% & 0.91 & 0.82 & 0.89 & 0.068 \\\\\n30\\% & 0.87 & 0.78 & 0.83 & 0.091 \\\\\n50\\% & 0.81 & 0.74 & 0.76 & 0.132 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe identify 15\\% replacement as the practical maximum: ranking stability ($\\tau = 0.93$), reliability ($\\alpha = 0.84$), and construct coverage (Jaccard = 0.91) all remain in acceptable ranges. At 20\\%, reliability drops to 0.82---near the psychometric threshold of 0.80. At 50\\%, reliability falls to 0.74, below any acceptable standard.\n\nThe theoretical upper bound under perfect calibration is 25\\%, but imperfect item generation quality (Section~\\ref{sec:item-gen}) compresses this to a practical limit of 15\\%. This constraint covers approximately 80\\% of items with $\\delta \\geq 1.0$, sufficient for most contamination remediation scenarios.\n\n\\subsection{Item-Focused Trees}\n\\label{sec:ift}\n\nAs a methodological robustness check, we compare Item-Focused Trees (continuous covariate) against categorical ETS C DIF (Table~\\ref{tab:ift-comparison}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Item-Focused Trees vs.\\ categorical DIF.}\n\\label{tab:ift-comparison}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & TPR ($\\delta \\geq 1.4$) & TPR ($\\delta \\geq 1.0$) & FPR & Unique Detections \\\\\n\\midrule\nETS C (categorical) & 0.58 & 0.41 & 0.062 & 47 \\\\\nIFT (continuous) & 0.62 & 0.46 & 0.058 & 134 \\\\\nOverlap (both detect) & --- & --- & --- & 612 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIFT provides a modest improvement (+0.04 TPR, $-$0.004 FPR) by avoiding information loss from arbitrary cohort boundaries. Its primary qualitative contribution is identifying 134 items with \\emph{gradual} contamination---items whose DIF effect sizes increase smoothly over time rather than appearing suddenly. The modal split point (September 2023) approximately corresponds to when MMLU entered mainstream LLM training pipelines.\n\n%===============================================================================\n\\section{Discussion and Limitations}\n\\label{sec:discussion}\n%===============================================================================\n\n\\paragraph{Summary of the framework.}\nOur results support a psychometric monitoring framework for benchmark contamination. DIF provides a complementary contamination signal that is uniquely RL-robust among detection methods (retention 0.885), though it is not the sole survivor---ConStat (0.841) and even DVD (0.903, from a low baseline) retain meaningful power. The dual-signal ensemble (DIF + ConStat) achieves TPR = 0.68 across the effect-size spectrum, and within-subject IRT equating enables contamination-aware item replacement up to 15\\% with acceptable validity degradation.\n\n\\paragraph{What DIF cannot detect.}\nDIF requires sufficient contamination effect sizes ($\\delta \\geq 1.0$) and adequate cohort sizes for statistical power. Small effects ($\\delta < 0.6$) are undetectable by our current framework, though these have minimal impact on model rankings. Pattern-level contamination (memorizing solution strategies rather than specific items) also partially evades DIF, as demonstrated by lower power on GSM8K.\n\n\\paragraph{DVD failure: a format dependency.}\nDVD's failure on MMLU is instructive. Generation variance is a valid contamination signal for open-ended benchmarks where memorization produces deterministic long-form output. On multiple-choice formats, the signal is compressed to near-zero by the forced-choice response structure. This highlights that no single contamination detector is format-universal, reinforcing the need for benchmark-specific ensemble design.\n\n\\paragraph{Equating scope limitations.}\nOur equating results are limited to within-subject replacement ($\\rho = 0.93$). Cross-subject equating ($\\rho = 0.87$) is insufficient for full-benchmark score comparability because model evolution changes ability structure, not just ability level---23\\% of MMLU subjects show unstable factor structures across cohorts. Practical deployment should use subject-specific equating rather than full-benchmark equating.\n\n\\paragraph{Generated item quality.}\nReplacement items show systematic quality gaps: lower discrimination ($-0.27$), lower factor loadings ($-0.09$), and weaker distractors ($-0.17$). These gaps constrain the replacement rate to $\\leq$15\\% and indicate that improving item generation quality is the primary bottleneck for expanding the framework's operating envelope.\n\n\\paragraph{RL robustness caveats.}\nOur RL validation uses $n = 35$ models with proxy RL intensity measures. The finding that DIF is RL-robust should be interpreted as ``DIF degrades less than alternatives'' rather than ``DIF is immune to RL.'' Heavy RL ($\\geq$200 steps) reduces DIF TPR from 0.61 to 0.51---a meaningful decline. Controlled RL fine-tuning experiments with known contamination status are needed for definitive validation.\n\n\\paragraph{Temporal monitoring tradeoffs.}\nCumulative Bayesian DIF achieves useful power (0.66--0.78) after four administrations, but this requires 1--2 years of data accumulation. During this period, contamination may have already degraded benchmark validity. The framework is better suited for ongoing monitoring and historical analysis than for rapid real-time detection.\n\n\\paragraph{FPR considerations.}\nThe ensemble FPR of 0.082 approaches the 0.10 threshold for practical concern. On MMLU's 11,847 items, this implies $\\sim$970 false alarms, which could trigger unnecessary item replacement. Threshold tuning and FPR-controlled procedures are important for deployment.\n\n%===============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%===============================================================================\n\nWe have presented a psychometric monitoring framework for LLM benchmark contamination that provides three contributions: (1) empirical evidence that DIF is a complementary contamination signal with the strongest RL-robustness among tested methods (retention ratio 0.885); (2) a dual-signal ensemble (DIF + ConStat) achieving 0.68 full-spectrum TPR with transparent failure mode analysis of DVD on multiple-choice formats; and (3) a within-subject bifactor IRT equating pilot establishing 15\\% item replacement as the practical operating bound ($\\tau \\geq 0.93$, $\\alpha \\geq 0.84$).\n\nThe framework's value lies not in claiming benchmarks can ``self-heal,'' but in providing known operating bounds for contamination-aware recalibration. Key limitations---moderate detection power for medium effects, small RL validation sample, cross-subject equating instability, and generated item quality gaps---define a clear path for future work: larger-scale RL validation, improved item generation, and extension to open-ended benchmarks where DVD may contribute effectively.\n\n%===============================================================================\n% References\n%===============================================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{99}\n\n\\bibitem[Brown et al.(2020)]{brown2020gpt3}\nBrown, T., Mann, B., Ryder, N., et al. (2020).\nLanguage models are few-shot learners.\n\\emph{NeurIPS}.\n\n\\bibitem[Dekoninck et al.(2024)]{dekoninck2024constat}\nDekoninck, J., Lunardi, L., Tsitsulin, A., et al. (2024).\nConStat: Performance-based contamination detection in large language models.\n\\emph{NeurIPS}.\n\n\\bibitem[Dodge et al.(2021)]{dodge2021documenting}\nDodge, J., Sap, M., Marasovic, A., et al. (2021).\nDocumenting large webtext corpora: A case study on the Colossal Clean Crawled Corpus.\n\\emph{EMNLP}.\n\n\\bibitem[Dong et al.(2024)]{dong2024dvd}\nDong, Y., et al. (2024).\nGeneralization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\emph{ACL}.\n\n\\bibitem[Gibbons \\& Hedeker(1992)]{gibbons1992bifactor}\nGibbons, R.~D. \\& Hedeker, D.~R. (1992).\nFull-information item bifactor analysis.\n\\emph{Psychometrika}, 57(3), 423--436.\n\n\\bibitem[Holland \\& Thayer(1988)]{holland1988dif}\nHolland, P.~W. \\& Thayer, D.~T. (1988).\nDifferential item performance and the Mantel--Haenszel procedure.\nIn \\emph{Test Validity}. Erlbaum.\n\n\\bibitem[Kolen \\& Brennan(2014)]{kolen2014equating}\nKolen, M.~J. \\& Brennan, R.~L. (2014).\n\\emph{Test Equating, Scaling, and Linking}. Springer.\n\n\\bibitem[Lalor et al.(2019)]{lalor2019irt}\nLalor, J.~P., Wu, H., \\& Yu, H. (2019).\nLearning latent parameters without human response patterns: Item response theory with artificial crowds.\n\\emph{EMNLP}.\n\n\\bibitem[Polo et al.(2026)]{polo2026growing}\nPolo, F.~M., et al. (2026).\nGrowing pains: Understanding the limitations of scalable evaluation.\n\\emph{arXiv preprint}.\n\n\\bibitem[Rodriguez et al.(2021)]{rodriguez2021irt}\nRodriguez, P., Barrow, J., Hoyle, A.~M., et al. (2021).\nEvaluation examples are not equally informative: How should that change NLP leaderboards?\n\\emph{ACL}.\n\n\\bibitem[Shi et al.(2024)]{shi2024mink}\nShi, W., Ajith, A., Xia, M., et al. (2024).\nDetecting pretraining data from large language models.\n\\emph{ICLR}.\n\n\\bibitem[Swaminathan \\& Rogers(1990)]{swaminathan1990dif}\nSwaminathan, H. \\& Rogers, H.~J. (1990).\nDetecting differential item functioning using logistic regression procedures.\n\\emph{Journal of Educational Measurement}, 27(4), 361--370.\n\n\\bibitem[Tutz \\& Berger(2016)]{tutz2016ift}\nTutz, G. \\& Berger, M. (2016).\nItem-focused trees for the identification of items in differential item functioning.\n\\emph{Psychometrika}, 81(3), 727--750.\n\n\\bibitem[Vania et al.(2021)]{vania2021irt}\nVania, C., et al. (2021).\nComparing test sets with item response theory.\n\\emph{ACL}.\n\n\\bibitem[Wang et al.(2026)]{wang2026rl}\nWang, Y., et al. (2026).\nReinforcement learning conceals benchmark contamination.\n\\emph{ICLR}.\n\n\\bibitem[White et al.(2024)]{white2024livebench}\nWhite, C., et al. (2024).\nLiveBench: A challenging, contamination-free LLM benchmark.\n\\emph{arXiv preprint}.\n\n\\bibitem[Zhu et al.(2024)]{zhu2024dyval}\nZhu, K., et al. (2024).\nDyVal: Dynamic evaluation of large language models for reasoning tasks.\n\\emph{ICLR}.\n\n\\bibitem[Zhuang et al.(2023)]{zhuang2023cat}\nZhuang, Y., et al. (2023).\nEfficiently measuring the cognitive ability of LLMs: An adaptive testing perspective.\n\\emph{arXiv preprint}.\n\n\\bibitem[Zieky(1993)]{zieky1993ets}\nZieky, M.~J. (1993).\nPractical questions in the use of DIF statistics in test development.\nIn \\emph{Differential Item Functioning}. Erlbaum.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f75e3a3-0aa6-4548-82b9-5381acc953d0",
  "isSidechain": false,
  "requestId": "req_011CbERGEcoK3kAiw5EpiRtq",
  "type": "assistant",
  "uuid": "48cd84d0-ba42-4f5c-a1b8-a9ad81626b5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVCygydjkxuhJsmaiEWbia",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 924,
      "cache_read_input_tokens": 43298,
      "output_tokens": 13801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13801,
          "cache_read_input_tokens": 43298,
          "cache_creation_input_tokens": 924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 924
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

_source line 19 · 2026-05-20T20:07:47.888Z_

<details><summary>↩ Tool result · `toolu_015X4oQW1ZhVETyjLU2epVJF`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48cd84d0-ba42-4f5c-a1b8-a9ad81626b5f",
  "isSidechain": false,
  "promptId": "b7ed4b5f-18d3-49c6-9368-69e76c0c1e3f",
  "type": "user",
  "uuid": "b8f038ad-f856-4748-bf57-d9978adb5318",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/paper.tex",
    "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage{caption}\n\n\\title{Psychometric Monitoring for LLM Benchmark Contamination:\\\\A Framework for Detection, Diagnosis, and Contamination-Aware Recalibration}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%===============================================================================\n\\begin{abstract}\n%===============================================================================\nLLM benchmarks implicitly assume temporal score comparability---that scores from models released years apart reflect the same latent ability under the same measurement instrument. Benchmark contamination systematically violates this assumption, and reinforcement learning (RL) training further conceals contamination signals by smoothing output distributions that existing detectors rely on.\nWe propose a psychometric monitoring framework grounded in Item Response Theory (IRT).\nOur first contribution shows that Differential Item Functioning (DIF) analysis provides a complementary contamination signal with unique RL-robustness properties: on MMLU with 4,312 models, DIF achieves a power retention ratio of 0.885 under RL training, compared to 0.689 for Min-K\\%.\nSecond, we construct a dual-signal ensemble combining DIF (RL-robust, large-effect coverage) with ConStat-style perturbation testing (medium-effect, non-RL coverage), achieving full-spectrum TPR of 0.68 versus 0.58 (DIF alone) and 0.47 (ConStat alone). We report DVD generation variance as a failure mode on multiple-choice formats, providing transparent analysis of its limitations.\nThird, we pilot within-subject bifactor IRT equating for contamination-aware item replacement, demonstrating that up to 15\\% of items can be replaced while maintaining ranking stability ($\\tau = 0.93$) and score reliability ($\\alpha = 0.84$).\nCross-benchmark validation on GSM8K with GSM1K ground truth confirms generalization.\nOur framework reframes benchmark maintenance from periodic manual curation to continuous psychometric monitoring with known operating bounds.\n\\end{abstract}\n\n%===============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%===============================================================================\n\nWhen we claim ``Model B outperforms Model A on MMLU,'' we implicitly assume both scores reflect the same latent ability measured under comparable conditions. Benchmark contamination---the inclusion of test items in training data---systematically erodes this comparability. The problem is compounded by the shift toward RL-trained reasoning models (o1, o3, DeepSeek-R1): Wang et al.\\ (2026) demonstrate 14--20 percentage point AUROC degradation for all reference-free contamination detectors after approximately 156 GRPO steps, reducing most methods to near-random performance ($\\sim$50\\% AUROC).\n\nExisting responses to contamination fall into three categories, each with critical gaps.\n\\emph{Dynamic benchmarks} such as LiveBench update items from recent sources but apply no psychometric calibration across versions, making temporal comparisons unreliable.\n\\emph{Performance-based detectors} such as ConStat provide FDR-controlled detection through perturbation sensitivity but rely on signals that RL training can mask.\n\\emph{Output-distribution detectors} (Min-K\\%, perplexity ratios) are the most vulnerable to RL smoothing.\nNo existing approach closes the full loop from RL-robust detection through diagnosis to psychometrically calibrated recalibration.\n\nWe argue that contamination is fundamentally a psychometric problem. When a model has memorized a benchmark item, it must answer that item correctly regardless of its general ability level---creating a detectable anomaly in the item's response pattern across model populations. This anomaly is precisely what Differential Item Functioning (DIF) measures: differential easiness of an item for one group (exposed models) relative to another (unexposed models), \\emph{after controlling for overall ability}. Because DIF operates on group-level behavioral patterns (correct/incorrect conditional on ability), not within-model output distributions, it is structurally robust to RL training---RL smooths output distributions but cannot eliminate the behavioral consequence of memorization without negating the benefit of contamination itself.\n\nThis paper makes three contributions:\n\\begin{enumerate}\n    \\item We demonstrate that DIF provides a \\textbf{complementary contamination signal with unique RL-robustness properties}. On MMLU with 4,312 models, ETS C DIF detection achieves TPR = 0.58 for large effects ($\\delta \\geq 1.4$) with FPR = 0.062, and retains 88.5\\% of its power under RL training---the highest retention ratio among all methods tested.\n    \\item We construct a \\textbf{dual-signal ensemble} (DIF + ConStat) that achieves full-spectrum TPR = 0.68, and provide a \\textbf{failure mode analysis of DVD} on multiple-choice formats explaining why generation variance is ineffective in this setting.\n    \\item We pilot \\textbf{within-subject bifactor IRT equating} for contamination-aware item replacement, establishing that up to 15\\% item replacement maintains acceptable validity ($\\tau \\geq 0.93$, $\\alpha \\geq 0.84$), with student-simulation calibration achieving difficulty correlation $\\rho = 0.68$ within subjects.\n\\end{enumerate}\n\nThe core narrative is not ``self-healing benchmarks'' but rather a \\textbf{psychometric monitoring framework with contamination-aware recalibration}---one that provides known operating bounds, transparent failure modes, and principled degradation guarantees.\n\n%===============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%===============================================================================\n\n\\paragraph{Benchmark contamination detection.}\nEarly contamination detection focused on $n$-gram overlap between training corpora and test sets (Brown et al., 2020; Dodge et al., 2021). As training data became less transparent, reference-free methods emerged. Min-K\\% (Shi et al., 2024) uses token-level log-probability statistics; ConStat (Dekoninck et al., 2024) tests whether models are more sensitive to paraphrased versions of contaminated items; DVD (Dong et al., 2024) leverages generation variance across multiple samplings. However, Wang et al.\\ (2026) show that RL training (GRPO/PPO) degrades all these methods by 14--20 pp AUROC after $\\sim$156 steps, because RL smooths the output distributions these methods rely on.\n\n\\paragraph{Dynamic and evolving benchmarks.}\nLiveBench (White et al., 2024) refreshes items monthly from recent sources. DyVal (Zhu et al., 2024) generates evaluation samples dynamically. However, neither applies psychometric calibration to ensure cross-version comparability. Growing Pains (Polo et al., 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability rather than contamination detection or remediation.\n\n\\paragraph{Psychometric methods in NLP evaluation.}\nIRT has been applied to NLP evaluation for efficiency (Lalor et al., 2019; Rodriguez et al., 2021), adaptive testing (Zhuang et al., 2023), and understanding benchmark difficulty structure (Vania et al., 2021). Bifactor models have been used to disentangle general and domain-specific abilities (Gibbons \\& Hedeker, 1992). However, DIF analysis---the standard psychometric tool for detecting item bias across groups---has not been systematically applied to LLM benchmark contamination. Our work bridges this gap.\n\n\\paragraph{DIF methodology.}\nDIF analysis originated in educational testing to detect item bias across demographic groups (Holland \\& Thayer, 1988; Swaminathan \\& Rogers, 1990). The ETS classification system (Zieky, 1993) categorizes items by DIF effect size into A (negligible), B (moderate), and C (large) categories. Item-Focused Trees (Tutz \\& Berger, 2016) extend DIF to continuous covariates. We adapt these methods to the LLM evaluation setting, where ``groups'' are defined by model release cohorts and ``ability'' is estimated via IRT.\n\n\\paragraph{Test equating.}\nTest equating ensures score comparability across different test forms (Kolen \\& Brennan, 2014). Common-item nonequivalent groups designs use anchor items to link scores. We apply fixed-parameter calibration with bifactor IRT to the benchmark regeneration setting, where contaminated items are replaced and scores must remain comparable.\n\n%===============================================================================\n\\section{Method}\n\\label{sec:method}\n%===============================================================================\n\nOur framework consists of three components: (1) DIF-based contamination detection, (2) multi-signal ensemble fusion, and (3) bifactor IRT equating for calibrated item replacement.\n\n\\subsection{DIF-Based Contamination Detection}\n\\label{sec:method-dif}\n\nLet $X_{ij} \\in \\{0,1\\}$ denote the binary response of model $i$ to item $j$, where 1 indicates a correct response. Under a 2PL IRT model, the probability of correct response is:\n\\begin{equation}\n    P(X_{ij} = 1 \\mid \\theta_i) = \\frac{1}{1 + \\exp(-a_j(\\theta_i - b_j))}\n\\end{equation}\nwhere $\\theta_i$ is the ability of model $i$, $a_j$ is the discrimination parameter, and $b_j$ is the difficulty parameter of item $j$.\n\nDIF occurs when an item has different parameters for different groups after controlling for ability. For contamination detection, we define groups by model release cohorts (e.g., pre-2024 vs.\\ post-2024). Under uniform DIF, the difficulty parameter differs between groups:\n\\begin{equation}\n    b_j^{\\text{focal}} \\neq b_j^{\\text{reference}}\n\\end{equation}\nThe DIF effect size is $\\delta_j = b_j^{\\text{reference}} - b_j^{\\text{focal}}$, with positive values indicating the item is easier for the focal (potentially contaminated) group.\n\nWe use the ETS C classification: items with $|\\delta_j| \\geq 1.0$ and statistically significant DIF are classified as C-level (large DIF), indicating potential contamination.\n\n\\paragraph{RL-robustness argument.}\nDIF operates on the Item Characteristic Curve (ICC)---the relationship between ability $\\theta$ and response probability---at the \\emph{population} level. RL training modifies a model's output distribution (token probabilities, generation diversity) but cannot eliminate the behavioral consequence that a memorized item is answered correctly. As long as contaminated models systematically outperform on specific items beyond what their ability predicts, DIF will detect the anomaly. This is structurally different from output-distribution-based methods (Min-K\\%, perplexity ratio) where RL directly degrades the signal.\n\n\\paragraph{Item-Focused Trees (IFT).}\nAs a methodological extension, we implement Item-Focused Trees that treat model release date as a continuous covariate rather than requiring categorical cohort splits. IFT recursively partitions the covariate space to identify regions where DIF is most pronounced, avoiding information loss from arbitrary temporal boundaries.\n\n\\subsection{Dual-Signal Ensemble}\n\\label{sec:method-ensemble}\n\nDIF excels at detecting large contamination effects ($\\delta \\geq 1.4$) and is RL-robust, but has limited power for medium effects ($\\delta \\in [0.6, 1.0)$). ConStat-style perturbation testing detects medium effects in non-RL models but degrades under RL training. These complementary profiles motivate a dual-signal ensemble.\n\nWe evaluate three fusion strategies:\n\\begin{itemize}\n    \\item \\textbf{Union (1-of-2)}: Flag if either signal fires. Maximizes TPR but increases FPR.\n    \\item \\textbf{Intersection (2-of-2)}: Flag only if both signals fire. Minimizes FPR but sacrifices TPR.\n    \\item \\textbf{Weighted fusion}: Combine calibrated scores with optimized weights $w_{\\text{DIF}} = 0.58$, $w_{\\text{ConStat}} = 0.42$, reflecting DIF's higher reliability under mixed model populations.\n\\end{itemize}\n\nDVD generation variance is excluded from the ensemble based on empirical evidence of its failure on multiple-choice formats (Section~\\ref{sec:dvd-failure}), but included as an ablation to justify this design decision.\n\n\\subsection{Bifactor IRT Equating}\n\\label{sec:method-equating}\n\nFor item replacement, we fit a bifactor IRT model:\n\\begin{equation}\n    P(X_{ij} = 1 \\mid \\theta_i^G, \\theta_i^{s_j}) = \\frac{1}{1 + \\exp(-[a_j^G \\theta_i^G + a_j^{s_j} \\theta_i^{s_j} - d_j])}\n\\end{equation}\nwhere $\\theta^G$ is the general ability factor, $\\theta^{s_j}$ is the subject-specific factor for item $j$'s domain, $a_j^G$ and $a_j^{s_j}$ are factor loadings, and $d_j$ is the intercept.\n\nAnchor items---those with stable DIF parameters across cohorts---are used for fixed-parameter calibration. Replacement items are generated via LLM with difficulty targeting through student simulation, then calibrated against anchor items within the same subject domain.\n\n\\paragraph{Student simulation calibration.}\nRather than relying on prompt-based difficulty estimation (which yields weak correlation with empirical difficulty, $\\rho = 0.32$), we simulate a population of ``student models'' spanning the ability spectrum to estimate replacement item difficulty empirically, achieving $\\rho = 0.63$ overall and $\\rho = 0.68$ within-subject.\n\n%===============================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%===============================================================================\n\n\\paragraph{MMLU data.}\nWe use the METABENCH response matrix containing 5,055 models and 12,508 MMLU items. After quality filtering (removing models with $<$50\\% item coverage), we retain 4,312 models and 11,847 analyzable items. Temporal cohorts: pre-2024 ($n=2{,}876$) vs.\\ post-2024 ($n=1{,}436$).\n\n\\paragraph{Ground truth.}\nFor MMLU, we use MMLU-CF (contamination-free variant) as partial ground truth. For GSM8K, we use the GSM1K accuracy gap as a proxy for contamination severity.\n\n\\paragraph{RL model identification.}\nWe identify 35 RL-trained models in METABENCH: 23 with explicit RL training documentation and 12 inferred from training pipeline descriptions. These are further categorized by RL intensity: light RL ($<$200 steps, $n=14$) and heavy RL ($\\geq$200 steps, $n=21$). SFT-only comparison group: $n=187$.\n\n\\paragraph{Baselines.}\nWe compare DIF against: Min-K\\%, Min-K\\%++, ConStat (perturbation), DVD (generation variance), perplexity ratio, and zlib ratio. We also compare ETS C categorical DIF against Mantel--Haenszel (MH) and logistic regression (LR) DIF methods.\n\n%===============================================================================\n\\section{Results}\n\\label{sec:results}\n%===============================================================================\n\n\\subsection{DIF Detection on Real MMLU Data}\n\\label{sec:dif-mmlu}\n\nTable~\\ref{tab:dif-by-effect} presents DIF detection performance stratified by contamination effect size. ETS C achieves TPR = 0.69 for items with $\\delta \\geq 1.6$ and TPR = 0.52 for $\\delta \\in [1.4, 1.6)$, with FPR controlled at 0.058--0.065 across bands. Overall, 743 items (6.3\\%) are flagged as ETS C-level DIF.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF detection performance on MMLU by effect size band (pre-2024 vs.\\ post-2024 cohorts).}\n\\label{tab:dif-by-effect}\n\\begin{tabular}{lrcccc}\n\\toprule\nEffect Size Band & $n$ (est.) & ETS C TPR & ETS C FPR & MH TPR & LR TPR \\\\\n\\midrule\n$\\delta \\geq 1.6$ & 68 & 0.69 & 0.058 & 0.54 & 0.61 \\\\\n$\\delta \\in [1.4, 1.6)$ & 119 & 0.52 & 0.065 & 0.38 & 0.44 \\\\\n$\\delta \\in [1.0, 1.4)$ & 412 & 0.41 & 0.063 & 0.27 & 0.33 \\\\\n$\\delta \\in [0.6, 1.0)$ & 144 & 0.18 & 0.061 & 0.11 & 0.14 \\\\\nClean & $\\sim$10,400 & --- & 0.062 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe aggregate TPR for $\\delta \\geq 1.4$ is 0.58, notably lower than simulation-based estimates ($\\sim$0.76). Three systematic factors explain this gap: (1) real contamination effects are not uniformly distributed at $\\delta = 1.4$---most flagged items fall in the $\\delta = 1.0$--$1.4$ range; (2) model heterogeneity in METABENCH introduces noise beyond IRT model assumptions; (3) contamination is not binary---partial benchmark exposure creates fuzzy group boundaries.\n\n\\paragraph{Cohort sensitivity.}\nTable~\\ref{tab:cohort-sensitivity} shows that DIF results are moderately sensitive to cohort definition. Annual splits (2022 vs.\\ 2024+) yield the highest TPR (0.63) with the lowest FPR (0.057), while finer quarterly splits inflate FPR to 0.084 due to small focal group sizes.\n\n\\begin{table}[h]\n\\centering\n\\caption{Sensitivity of DIF detection to cohort definition.}\n\\label{tab:cohort-sensitivity}\n\\begin{tabular}{lccccc}\n\\toprule\nCohort Split & Focal $n$ & Ref.\\ $n$ & TPR ($\\delta \\geq 1.4$) & FPR & Flagged \\\\\n\\midrule\nPre-2024 vs.\\ post-2024 & 1,436 & 2,876 & 0.58 & 0.062 & 743 \\\\\nPre-2023 vs.\\ post-2023 & 1,891 & 2,421 & 0.54 & 0.071 & 812 \\\\\nAnnual (2022 vs.\\ 2024+) & 987 & 1,436 & 0.63 & 0.057 & 691 \\\\\nQuarterly & 623 & 718 & 0.52 & 0.084 & 658 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{MMLU-CF cross-validation.}\nCross-validation against MMLU-CF yields Spearman $\\rho = 0.21$ ($p = 0.003$, 95\\% CI $[0.09, 0.33]$) between DIF effect sizes and CF accuracy gaps. Cohen's $\\kappa = 0.14$ for binary agreement reflects that DIF and CF capture different contamination facets: DIF detects group-level behavioral shifts while CF tests item-level memorization through content modification. Of flagged items, 47 are flagged by both methods, 696 by DIF only, and 83 by CF only.\n\n\\subsection{RL-Robustness Validation}\n\\label{sec:rl-robustness}\n\nTable~\\ref{tab:rl-robustness} presents detection performance under SFT-only versus RL-trained model cohorts. DIF achieves the highest power retention ratio (0.885) among all methods, with AUROC declining only from 0.73 to 0.68 under RL. In contrast, Min-K\\% degrades from 0.74 to 0.51 (retention 0.689), consistent with Wang et al.'s finding that output-distribution methods are most vulnerable to RL smoothing.\n\n\\begin{table}[h]\n\\centering\n\\caption{Contamination detection power under SFT vs.\\ RL training regimes.}\n\\label{tab:rl-robustness}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & AUROC (SFT) & AUROC (RL) & Retention & $\\Delta$ AUROC \\\\\n\\midrule\nDIF (ETS C) & 0.73 & 0.68 & 0.885 & $-0.05$ \\\\\nMin-K\\% & 0.74 & 0.51 & 0.689 & $-0.23$ \\\\\nMin-K\\%++ & 0.71 & 0.53 & 0.746 & $-0.18$ \\\\\nConStat (perturbation) & 0.69 & 0.58 & 0.841 & $-0.11$ \\\\\nDVD (generation variance) & 0.62 & 0.56 & 0.903 & $-0.06$ \\\\\nPerplexity ratio & 0.67 & 0.49 & 0.731 & $-0.18$ \\\\\nZlib ratio & 0.59 & 0.52 & 0.881 & $-0.07$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe RL-robustness story is one of \\emph{degree}, not binary survival. DIF retains the most power, but ConStat (retention 0.841) also maintains reasonable performance. DVD's high retention (0.903) is misleading---its baseline AUROC (0.62) is already low, so ``retaining'' a weak signal provides little practical value.\n\nTable~\\ref{tab:rl-intensity} breaks down DIF performance by RL intensity. Heavy RL ($\\geq$200 steps) reduces DIF TPR from 0.61 to 0.51, while light RL ($<$200 steps) has a more modest impact (TPR = 0.57). Min-K\\% degrades more steeply: from 0.74 (SFT) to 0.47 (heavy RL).\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF and Min-K\\% TPR breakdown by RL training intensity.}\n\\label{tab:rl-intensity}\n\\begin{tabular}{lccc}\n\\toprule\nRL Category & $n$ Models & DIF TPR ($\\delta \\geq 1.4$) & Min-K\\% AUROC \\\\\n\\midrule\nSFT only & 187 & 0.61 & 0.74 \\\\\nLight RL ($<$200 steps) & 14 & 0.57 & 0.59 \\\\\nHeavy RL ($\\geq$200 steps) & 21 & 0.51 & 0.47 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Limitations:} The RL model sample ($n = 35$) is small, and RL intensity is a proxy measure. We acknowledge these limitations and recommend future validation with controlled RL fine-tuning experiments.\n\n\\subsection{ConStat Perturbation Evaluation}\n\\label{sec:constat}\n\nWe independently evaluate ConStat-style perturbation testing on 248 reformulated MMLU items across 42 models (mean semantic similarity of reformulations: 0.91). Table~\\ref{tab:constat-detail} presents detection power stratified by effect size and model type.\n\n\\begin{table}[h]\n\\centering\n\\caption{ConStat detection power by effect size band and model type.}\n\\label{tab:constat-detail}\n\\begin{tabular}{lccc}\n\\toprule\nEffect Size Band & TPR (non-RL) & TPR (RL) & TPR (all) \\\\\n\\midrule\n$\\delta \\geq 1.4$ & 0.64 & 0.31 & 0.53 \\\\\n$\\delta \\in [1.0, 1.4)$ & 0.58 & 0.28 & 0.48 \\\\\n$\\delta \\in [0.6, 1.0)$ & 0.47 & 0.23 & 0.39 \\\\\n$\\delta < 0.6$ & 0.12 & 0.08 & 0.10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConStat provides complementary coverage to DIF, particularly for medium effects ($\\delta \\in [0.6, 1.0)$) where DIF TPR is only 0.18 but ConStat achieves 0.47 on non-RL models. However, ConStat degrades substantially under RL training (TPR drops from 0.47 to 0.23 at $\\delta \\geq 0.6$), because RL-trained models develop robustness to input perturbations as a side effect of PPO reward hacking.\n\nSignal overlap between DIF and ConStat is low: only 34\\% of flagged items are detected by both methods (31 items), with 58 items detected by DIF only and 52 by ConStat only. This low overlap supports ensemble construction rather than indicating redundancy.\n\n\\subsection{DVD Failure Mode Analysis}\n\\label{sec:dvd-failure}\n\nDVD generation variance performs poorly on MMLU, achieving overall AUROC of only 0.57 with FPR = 0.094. Table~\\ref{tab:dvd-performance} breaks down performance by contamination type.\n\n\\begin{table}[h]\n\\centering\n\\caption{DVD detection performance on MMLU by contamination type.}\n\\label{tab:dvd-performance}\n\\begin{tabular}{lcccc}\n\\toprule\nContamination Type & $n$ Items & TPR & AUROC & Cohen's $d$ \\\\\n\\midrule\nVariant contamination & 34 & 0.38 & 0.62 & 0.51 \\\\\nVerbatim contamination & 89 & 0.16 & 0.54 & 0.29 \\\\\nMixed/unknown & 125 & 0.19 & 0.57 & 0.38 \\\\\nClean items & $\\sim$11,600 & ---\\,(FPR=0.094) & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe root cause is format mismatch. DVD was designed for open-ended generation tasks where memorized content produces deterministic long-form output (low variance). In MMLU's forced-choice format, even memorized items produce minimal variance---the output is a single letter (A/B/C/D) regardless of whether the model memorized the answer. Generation variance between clean and contaminated items is small (mean 0.42 vs.\\ 0.31, $d = 0.38$), insufficient for reliable detection.\n\nThis negative result motivates excluding DVD from our ensemble. Adding DVD to the DIF+ConStat ensemble yields only +0.02 TPR gain (Section~\\ref{sec:ensemble}), confirming that its signal is largely redundant with or inferior to the other two methods on multiple-choice benchmarks. We note that DVD may be effective on open-ended benchmarks (e.g., HumanEval, free-form MATH) where generation variance has greater dynamic range.\n\n\\subsection{Ensemble Fusion}\n\\label{sec:ensemble}\n\nTable~\\ref{tab:ensemble-strategies} compares fusion strategies for the DIF+ConStat dual-signal ensemble.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ensemble fusion strategy comparison.}\n\\label{tab:ensemble-strategies}\n\\begin{tabular}{lcccc}\n\\toprule\nStrategy & TPR ($\\delta \\geq 1.4$) & TPR ($\\delta \\geq 0.6$) & FPR & $F_1$ \\\\\n\\midrule\nDIF only & 0.58 & 0.38 & 0.062 & 0.47 \\\\\nConStat only & 0.64 & 0.47 & 0.087 & 0.51 \\\\\n1-of-2 (union) & 0.79 & 0.61 & 0.110 & 0.54 \\\\\n2-of-2 (intersection) & 0.34 & 0.24 & 0.031 & 0.37 \\\\\nWeighted fusion (optimal) & 0.73 & 0.48 & 0.082 & 0.56 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWeighted fusion achieves the best $F_1$ (0.56) at TPR = 0.73 / FPR = 0.082, with DIF weight 0.58 and ConStat weight 0.42. The 2-of-2 intersection is overly conservative (TPR = 0.34) because the two signals detect different contamination facets---requiring both to agree takes the intersection rather than the union of their coverage.\n\n\\paragraph{Ablation: value of each signal.}\nTable~\\ref{tab:ablation} quantifies each signal's contribution. Removing ConStat reduces full-spectrum TPR by 0.10; removing DIF reduces it by 0.21, confirming DIF as the more informative signal overall. Adding DVD yields only +0.02 TPR, justifying the 2-signal design.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ablation study: contribution of each signal to ensemble TPR.}\n\\label{tab:ablation}\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & TPR (full spectrum) & $\\Delta$ vs.\\ full ensemble \\\\\n\\midrule\nDIF + ConStat (full) & 0.68 & baseline \\\\\nDIF only & 0.58 & $-0.10$ \\\\\nConStat only & 0.47 & $-0.21$ \\\\\nDIF + ConStat + DVD & 0.70 & $+0.02$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Coverage analysis.}\nThe two signals have complementary coverage profiles. DIF uniquely detects large effects in RL-trained models (21\\% of detected items), while ConStat uniquely detects medium effects in SFT models (18\\%). Both detect large effects in SFT models (29\\% overlap). Neither signal detects small effects ($\\delta < 0.6$), which is an inherent coverage gap.\n\n\\subsection{Cross-Benchmark Validation: GSM8K}\n\\label{sec:gsm8k}\n\nTo test generalization beyond factual recall benchmarks, we apply DIF analysis to GSM8K (1,319 items, 68 models) using the GSM8K--GSM1K accuracy gap as a contamination proxy (Table~\\ref{tab:gsm8k-results}).\n\n\\begin{table}[h]\n\\centering\n\\caption{GSM8K DIF analysis results.}\n\\label{tab:gsm8k-results}\n\\begin{tabular}{lcc}\n\\toprule\nMetric & Value & 95\\% CI \\\\\n\\midrule\nItems flagged by DIF & 127 & --- \\\\\nMean GSM8K--GSM1K gap (all models) & 7.3\\% & [5.1\\%, 9.5\\%] \\\\\nMean gap (high DIF-flag-count models) & 11.8\\% & [8.2\\%, 15.4\\%] \\\\\nItem-level DIF-gap correlation ($\\rho$) & 0.22 & [0.06, 0.37] \\\\\nModel-level flag-count-gap correlation ($r$) & 0.31 & [0.14, 0.47] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDIF detects contamination signal on GSM8K ($\\rho = 0.22$, $p = 0.014$), though with lower power than MMLU (TPR = 0.49 vs.\\ 0.58). The model-level correlation ($r = 0.31$) is stronger, suggesting DIF has more discriminative power at identifying contaminated \\emph{models} than contaminated \\emph{items} in this setting. Table~\\ref{tab:cross-benchmark} compares results across benchmarks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-benchmark comparison of DIF detection.}\n\\label{tab:cross-benchmark}\n\\begin{tabular}{lccccc}\n\\toprule\nBenchmark & $n$ Models & $n$ Items & DIF TPR & Ground Truth $\\rho$ & FPR \\\\\n\\midrule\nMMLU & 4,312 & 11,847 & 0.58 & 0.21 (MMLU-CF) & 0.062 \\\\\nGSM8K & 68 & 1,319 & 0.49 & 0.22 (GSM1K) & 0.071 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe lower TPR on GSM8K reflects both smaller sample size ($n = 68$ vs.\\ 4,312) and different contamination patterns: math reasoning benchmarks involve pattern memorization rather than item memorization, which DIF is less sensitive to.\n\n\\subsection{Bifactor IRT Equating Pilot}\n\\label{sec:equating}\n\nWe fit a bifactor IRT model to the MMLU response matrix, extracting one general factor and 57 subject-specific factors. Table~\\ref{tab:bifactor-fit} presents model fit statistics.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bifactor model fit statistics for MMLU.}\n\\label{tab:bifactor-fit}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nGeneral factor variance explained & 0.41 \\\\\nMean subject-factor variance & 0.09 \\\\\nRMSEA & 0.038 \\\\\nCFI & 0.94 \\\\\nTLI & 0.92 \\\\\nSubjects with stable factor structure & 44/57 (77\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe general factor explains 41\\% of variance---lower than typical educational tests (50--60\\%)---reflecting MMLU's coverage of 57 diverse subjects. Model fit (RMSEA = 0.038, CFI = 0.94) is adequate.\n\nTable~\\ref{tab:equating-scope} compares within-subject and cross-subject equating performance. Within-subject equating achieves mean $\\rho = 0.93$ with low bias (0.003) and RMSE (0.047). Cross-subject equating is weaker ($\\rho = 0.87$, RMSE = 0.073) because 23\\% of subjects have unstable factor structures across model cohorts---model evolution changes not just ability levels but ability \\emph{structure} across domains.\n\n\\begin{table}[h]\n\\centering\n\\caption{Equating performance by scope.}\n\\label{tab:equating-scope}\n\\begin{tabular}{lcccc}\n\\toprule\nScope & $\\rho$ & Bias & RMSE & $n$ Replaced \\\\\n\\midrule\nWithin-subject (STEM avg) & 0.95 & 0.002 & 0.038 & 47 \\\\\nWithin-subject (Humanities avg) & 0.91 & 0.004 & 0.052 & 39 \\\\\nWithin-subject (overall) & 0.93 & 0.003 & 0.047 & 86 \\\\\nCross-subject (full MMLU) & 0.87 & 0.011 & 0.073 & 86 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe therefore scope our equating claim to within-subject replacement and present cross-subject results as an area for future improvement.\n\n\\subsection{Item Generation and Calibration}\n\\label{sec:item-gen}\n\nWe generate 150 replacement items for DIF-flagged MMLU items, of which 118 pass quality filters (pass rate 78.7\\%). Table~\\ref{tab:calibration} compares difficulty calibration methods.\n\n\\begin{table}[h]\n\\centering\n\\caption{Difficulty calibration: prompt-based vs.\\ student simulation.}\n\\label{tab:calibration}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & $\\rho$ (overall) & $\\rho$ (within-subj.) & MAE & Within 0.5 logit \\\\\n\\midrule\nPrompt-based targeting & 0.32 & 0.39 & 0.34 & 41/118 (35\\%) \\\\\nStudent simulation & 0.63 & 0.68 & 0.19 & 74/118 (63\\%) \\\\\nStudent sim + iterative & 0.66 & 0.71 & 0.17 & 79/118 (67\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStudent simulation dramatically outperforms prompt-based targeting ($\\rho = 0.63$ vs.\\ 0.32), confirming that empirical calibration through model population responses is essential. However, generated items show systematic quality gaps relative to originals: lower discrimination ($a = 0.93$ vs.\\ 1.20), lower factor loadings (0.38 vs.\\ 0.47), and less effective distractors (0.61 vs.\\ 0.78). These gaps constrain the practical replacement rate.\n\n\\begin{table}[h]\n\\centering\n\\caption{Generated vs.\\ original item quality metrics.}\n\\label{tab:item-quality}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Generated & Original & Gap \\\\\n\\midrule\nMean difficulty (IRT $b$) & $-0.62$ & $-0.84$ & $+0.22$ \\\\\nMean discrimination (IRT $a$) & 0.93 & 1.20 & $-0.27$ \\\\\nFactor loading (general) & 0.38 & 0.47 & $-0.09$ \\\\\nDistractor effectiveness & 0.61 & 0.78 & $-0.17$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cumulative Bayesian DIF}\n\\label{sec:bayesian}\n\nSingle-administration DIF power is limited, particularly for medium effects (TPR = 0.33 at $\\delta = 1.0$). We implement cumulative Bayesian DIF priors that accumulate evidence across successive benchmark administrations. Table~\\ref{tab:bayesian-power} shows power growth over four simulated administrations of 80 models each.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cumulative Bayesian DIF power over successive administrations.}\n\\label{tab:bayesian-power}\n\\begin{tabular}{lcccc}\n\\toprule\nAdmin. & $n$ Models (cumul.) & Power ($\\delta=1.0$) & Power ($\\delta=1.4$) & FPR \\\\\n\\midrule\n1 & 80 & 0.33 & 0.55 & 0.048 \\\\\n2 & 160 & 0.48 & 0.67 & 0.051 \\\\\n3 & 240 & 0.59 & 0.74 & 0.052 \\\\\n4 & 320 & 0.66 & 0.78 & 0.053 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAfter four administrations, power for large effects reaches 0.78 and for medium effects 0.66, while FPR remains controlled at 0.053. This supports the ``monitoring framework'' narrative: single-shot detection has limited power, but continuous monitoring with evidence accumulation achieves useful detection rates. The practical caveat is that four administrations may require 1--2 years, during which contamination has already impacted benchmark validity.\n\n\\subsection{Graceful Degradation Analysis}\n\\label{sec:degradation}\n\nTable~\\ref{tab:degradation} characterizes benchmark validity under progressive item replacement.\n\n\\begin{table}[h]\n\\centering\n\\caption{Validity metrics under progressive item replacement.}\n\\label{tab:degradation}\n\\begin{tabular}{lcccc}\n\\toprule\nReplacement Rate & Kendall's $\\tau$ & Cronbach's $\\alpha$ & Construct Jaccard & Equating RMSE \\\\\n\\midrule\n0\\% (baseline) & 1.00 & 0.89 & 1.00 & 0.000 \\\\\n5\\% & 0.97 & 0.87 & 0.97 & 0.029 \\\\\n10\\% & 0.95 & 0.85 & 0.94 & 0.041 \\\\\n15\\% & 0.93 & 0.84 & 0.91 & 0.054 \\\\\n20\\% & 0.91 & 0.82 & 0.89 & 0.068 \\\\\n30\\% & 0.87 & 0.78 & 0.83 & 0.091 \\\\\n50\\% & 0.81 & 0.74 & 0.76 & 0.132 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe identify 15\\% replacement as the practical maximum: ranking stability ($\\tau = 0.93$), reliability ($\\alpha = 0.84$), and construct coverage (Jaccard = 0.91) all remain in acceptable ranges. At 20\\%, reliability drops to 0.82---near the psychometric threshold of 0.80. At 50\\%, reliability falls to 0.74, below any acceptable standard.\n\nThe theoretical upper bound under perfect calibration is 25\\%, but imperfect item generation quality (Section~\\ref{sec:item-gen}) compresses this to a practical limit of 15\\%. This constraint covers approximately 80\\% of items with $\\delta \\geq 1.0$, sufficient for most contamination remediation scenarios.\n\n\\subsection{Item-Focused Trees}\n\\label{sec:ift}\n\nAs a methodological robustness check, we compare Item-Focused Trees (continuous covariate) against categorical ETS C DIF (Table~\\ref{tab:ift-comparison}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Item-Focused Trees vs.\\ categorical DIF.}\n\\label{tab:ift-comparison}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & TPR ($\\delta \\geq 1.4$) & TPR ($\\delta \\geq 1.0$) & FPR & Unique Detections \\\\\n\\midrule\nETS C (categorical) & 0.58 & 0.41 & 0.062 & 47 \\\\\nIFT (continuous) & 0.62 & 0.46 & 0.058 & 134 \\\\\nOverlap (both detect) & --- & --- & --- & 612 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIFT provides a modest improvement (+0.04 TPR, $-$0.004 FPR) by avoiding information loss from arbitrary cohort boundaries. Its primary qualitative contribution is identifying 134 items with \\emph{gradual} contamination---items whose DIF effect sizes increase smoothly over time rather than appearing suddenly. The modal split point (September 2023) approximately corresponds to when MMLU entered mainstream LLM training pipelines.\n\n%===============================================================================\n\\section{Discussion and Limitations}\n\\label{sec:discussion}\n%===============================================================================\n\n\\paragraph{Summary of the framework.}\nOur results support a psychometric monitoring framework for benchmark contamination. DIF provides a complementary contamination signal that is uniquely RL-robust among detection methods (retention 0.885), though it is not the sole survivor---ConStat (0.841) and even DVD (0.903, from a low baseline) retain meaningful power. The dual-signal ensemble (DIF + ConStat) achieves TPR = 0.68 across the effect-size spectrum, and within-subject IRT equating enables contamination-aware item replacement up to 15\\% with acceptable validity degradation.\n\n\\paragraph{What DIF cannot detect.}\nDIF requires sufficient contamination effect sizes ($\\delta \\geq 1.0$) and adequate cohort sizes for statistical power. Small effects ($\\delta < 0.6$) are undetectable by our current framework, though these have minimal impact on model rankings. Pattern-level contamination (memorizing solution strategies rather than specific items) also partially evades DIF, as demonstrated by lower power on GSM8K.\n\n\\paragraph{DVD failure: a format dependency.}\nDVD's failure on MMLU is instructive. Generation variance is a valid contamination signal for open-ended benchmarks where memorization produces deterministic long-form output. On multiple-choice formats, the signal is compressed to near-zero by the forced-choice response structure. This highlights that no single contamination detector is format-universal, reinforcing the need for benchmark-specific ensemble design.\n\n\\paragraph{Equating scope limitations.}\nOur equating results are limited to within-subject replacement ($\\rho = 0.93$). Cross-subject equating ($\\rho = 0.87$) is insufficient for full-benchmark score comparability because model evolution changes ability structure, not just ability level---23\\% of MMLU subjects show unstable factor structures across cohorts. Practical deployment should use subject-specific equating rather than full-benchmark equating.\n\n\\paragraph{Generated item quality.}\nReplacement items show systematic quality gaps: lower discrimination ($-0.27$), lower factor loadings ($-0.09$), and weaker distractors ($-0.17$). These gaps constrain the replacement rate to $\\leq$15\\% and indicate that improving item generation quality is the primary bottleneck for expanding the framework's operating envelope.\n\n\\paragraph{RL robustness caveats.}\nOur RL validation uses $n = 35$ models with proxy RL intensity measures. The finding that DIF is RL-robust should be interpreted as ``DIF degrades less than alternatives'' rather than ``DIF is immune to RL.'' Heavy RL ($\\geq$200 steps) reduces DIF TPR from 0.61 to 0.51---a meaningful decline. Controlled RL fine-tuning experiments with known contamination status are needed for definitive validation.\n\n\\paragraph{Temporal monitoring tradeoffs.}\nCumulative Bayesian DIF achieves useful power (0.66--0.78) after four administrations, but this requires 1--2 years of data accumulation. During this period, contamination may have already degraded benchmark validity. The framework is better suited for ongoing monitoring and historical analysis than for rapid real-time detection.\n\n\\paragraph{FPR considerations.}\nThe ensemble FPR of 0.082 approaches the 0.10 threshold for practical concern. On MMLU's 11,847 items, this implies $\\sim$970 false alarms, which could trigger unnecessary item replacement. Threshold tuning and FPR-controlled procedures are important for deployment.\n\n%===============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%===============================================================================\n\nWe have presented a psychometric monitoring framework for LLM benchmark contamination that provides three contributions: (1) empirical evidence that DIF is a complementary contamination signal with the strongest RL-robustness among tested methods (retention ratio 0.885); (2) a dual-signal ensemble (DIF + ConStat) achieving 0.68 full-spectrum TPR with transparent failure mode analysis of DVD on multiple-choice formats; and (3) a within-subject bifactor IRT equating pilot establishing 15\\% item replacement as the practical operating bound ($\\tau \\geq 0.93$, $\\alpha \\geq 0.84$).\n\nThe framework's value lies not in claiming benchmarks can ``self-heal,'' but in providing known operating bounds for contamination-aware recalibration. Key limitations---moderate detection power for medium effects, small RL validation sample, cross-subject equating instability, and generated item quality gaps---define a clear path for future work: larger-scale RL validation, improved item generation, and extension to open-ended benchmarks where DVD may contribute effectively.\n\n%===============================================================================\n% References\n%===============================================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{99}\n\n\\bibitem[Brown et al.(2020)]{brown2020gpt3}\nBrown, T., Mann, B., Ryder, N., et al. (2020).\nLanguage models are few-shot learners.\n\\emph{NeurIPS}.\n\n\\bibitem[Dekoninck et al.(2024)]{dekoninck2024constat}\nDekoninck, J., Lunardi, L., Tsitsulin, A., et al. (2024).\nConStat: Performance-based contamination detection in large language models.\n\\emph{NeurIPS}.\n\n\\bibitem[Dodge et al.(2021)]{dodge2021documenting}\nDodge, J., Sap, M., Marasovic, A., et al. (2021).\nDocumenting large webtext corpora: A case study on the Colossal Clean Crawled Corpus.\n\\emph{EMNLP}.\n\n\\bibitem[Dong et al.(2024)]{dong2024dvd}\nDong, Y., et al. (2024).\nGeneralization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\emph{ACL}.\n\n\\bibitem[Gibbons \\& Hedeker(1992)]{gibbons1992bifactor}\nGibbons, R.~D. \\& Hedeker, D.~R. (1992).\nFull-information item bifactor analysis.\n\\emph{Psychometrika}, 57(3), 423--436.\n\n\\bibitem[Holland \\& Thayer(1988)]{holland1988dif}\nHolland, P.~W. \\& Thayer, D.~T. (1988).\nDifferential item performance and the Mantel--Haenszel procedure.\nIn \\emph{Test Validity}. Erlbaum.\n\n\\bibitem[Kolen \\& Brennan(2014)]{kolen2014equating}\nKolen, M.~J. \\& Brennan, R.~L. (2014).\n\\emph{Test Equating, Scaling, and Linking}. Springer.\n\n\\bibitem[Lalor et al.(2019)]{lalor2019irt}\nLalor, J.~P., Wu, H., \\& Yu, H. (2019).\nLearning latent parameters without human response patterns: Item response theory with artificial crowds.\n\\emph{EMNLP}.\n\n\\bibitem[Polo et al.(2026)]{polo2026growing}\nPolo, F.~M., et al. (2026).\nGrowing pains: Understanding the limitations of scalable evaluation.\n\\emph{arXiv preprint}.\n\n\\bibitem[Rodriguez et al.(2021)]{rodriguez2021irt}\nRodriguez, P., Barrow, J., Hoyle, A.~M., et al. (2021).\nEvaluation examples are not equally informative: How should that change NLP leaderboards?\n\\emph{ACL}.\n\n\\bibitem[Shi et al.(2024)]{shi2024mink}\nShi, W., Ajith, A., Xia, M., et al. (2024).\nDetecting pretraining data from large language models.\n\\emph{ICLR}.\n\n\\bibitem[Swaminathan \\& Rogers(1990)]{swaminathan1990dif}\nSwaminathan, H. \\& Rogers, H.~J. (1990).\nDetecting differential item functioning using logistic regression procedures.\n\\emph{Journal of Educational Measurement}, 27(4), 361--370.\n\n\\bibitem[Tutz \\& Berger(2016)]{tutz2016ift}\nTutz, G. \\& Berger, M. (2016).\nItem-focused trees for the identification of items in differential item functioning.\n\\emph{Psychometrika}, 81(3), 727--750.\n\n\\bibitem[Vania et al.(2021)]{vania2021irt}\nVania, C., et al. (2021).\nComparing test sets with item response theory.\n\\emph{ACL}.\n\n\\bibitem[Wang et al.(2026)]{wang2026rl}\nWang, Y., et al. (2026).\nReinforcement learning conceals benchmark contamination.\n\\emph{ICLR}.\n\n\\bibitem[White et al.(2024)]{white2024livebench}\nWhite, C., et al. (2024).\nLiveBench: A challenging, contamination-free LLM benchmark.\n\\emph{arXiv preprint}.\n\n\\bibitem[Zhu et al.(2024)]{zhu2024dyval}\nZhu, K., et al. (2024).\nDyVal: Dynamic evaluation of large language models for reasoning tasks.\n\\emph{ICLR}.\n\n\\bibitem[Zhuang et al.(2023)]{zhuang2023cat}\nZhuang, Y., et al. (2023).\nEfficiently measuring the cognitive ability of LLMs: An adaptive testing perspective.\n\\emph{arXiv preprint}.\n\n\\bibitem[Zieky(1993)]{zieky1993ets}\nZieky, M.~J. (1993).\nPractical questions in the use of DIF statistics in test development.\nIn \\emph{Differential Item Functioning}. Erlbaum.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "48cd84d0-ba42-4f5c-a1b8-a9ad81626b5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194223 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "b8f038ad-f856-4748-bf57-d9978adb5318",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for IRT equated benchmark",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea"
}
```

---

### Tool call

_source line 22 · 2026-05-20T20:07:52.518Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KF6c5hRRkzzUF4YPk5nCSg`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8f038ad-f856-4748-bf57-d9978adb5318",
  "isSidechain": false,
  "requestId": "req_011CbERbMTqpXEySF3Azoczz",
  "type": "assistant",
  "uuid": "b32ba967-6ccb-43f5-82d0-238a4b98799c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018CTFN7MYwaX2h14VYtJewY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13871,
      "cache_read_input_tokens": 44222,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13871,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 44222,
          "cache_creation_input_tokens": 13871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13871
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

_source line 23 · 2026-05-20T20:07:53.535Z_

<details><summary>↩ Tool result · `toolu_01KF6c5hRRkzzUF4YPk5nCSg`</summary>

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] [2]

LaTeX Warning: Reference `sec:dvd-failure' on page 3 undefined on input line 12
1.

[3]

LaTeX Warning: Reference `tab:dif-by-effect' on page 4 undefined on input line 
162.

[4]

LaTeX Warning: Reference `tab:cohort-sensitivity' on page 5 undefined on input 
line 184.


LaTeX Warning: Reference `tab:rl-robustness' on page 5 undefined on input line 
208.


LaTeX Warning: Reference `tab:rl-intensity' on page 5 undefined on input line 2
31.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:constat-detail' on page 5 undefined on input line
 253.

[5]

LaTeX Warning: Reference `tab:dvd-performance' on page 6 undefined on input lin
e 278.


LaTeX Warning: Reference `sec:ensemble' on page 6 undefined on input line 298.


LaTeX Warning: Reference `tab:ensemble-strategies' on page 6 undefined on input
 line 303.

[6]

LaTeX Warning: Reference `tab:ablation' on page 7 undefined on input line 325.


LaTeX Warning: Reference `tab:gsm8k-results' on page 7 undefined on input line 
349.


LaTeX Warning: Reference `tab:cross-benchmark' on page 7 undefined on input lin
e 368.

[7]

LaTeX Warning: Reference `tab:bifactor-fit' on page 8 undefined on input line 3
89.


LaTeX Warning: Reference `tab:equating-scope' on page 8 undefined on input line
 411.


LaTeX Warning: Reference `tab:calibration' on page 8 undefined on input line 43
4.


LaTeX Warning: `h' float specifier changed to `ht'.

[8]

LaTeX Warning: Reference `tab:bayesian-power' on page 9 undefined on input line
 472.


LaTeX Warning: Reference `tab:degradation' on page 9 undefined on input line 49
5.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `sec:item-gen' on page 9 undefined on input line 518.


LaTeX Warning: Reference `tab:ift-comparison' on page 9 undefined on input line
 523.

[9] [10] [11] [12] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.60
0pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (12 pages, 233928 bytes).
Transcript written on paper.log.
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] [2] [3] [4]

LaTeX Warning: `h' float specifier changed to `ht'.

[5] [6] [7]

LaTeX Warning: `h' float specifier changed to `ht'.

[8]

LaTeX Warning: `h' float specifier changed to `ht'.

[9] [10] [11] [12] (./paper.aux) ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/p
k/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi5.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmti10.pfb>
Output written on paper.pdf (12 pages, 236005 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b32ba967-6ccb-43f5-82d0-238a4b98799c",
  "isSidechain": false,
  "promptId": "b7ed4b5f-18d3-49c6-9368-69e76c0c1e3f",
  "type": "user",
  "uuid": "6a62c78c-14d0-455a-9127-b71134a7e5f8",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2]\n\nLaTeX Warning: Reference `sec:dvd-failure' on page 3 undefined on input line 12\n1.\n\n[3]\n\nLaTeX Warning: Reference `tab:dif-by-effect' on page 4 undefined on input line \n162.\n\n[4]\n\nLaTeX Warning: Reference `tab:cohort-sensitivity' on page 5 undefined on input \nline 184.\n\n\nLaTeX Warning: Reference `tab:rl-robustness' on page 5 undefined on input line \n208.\n\n\nLaTeX Warning: Reference `tab:rl-intensity' on page 5 undefined on input line 2\n31.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:constat-detail' on page 5 undefined on input line\n 253.\n\n[5]\n\nLaTeX Warning: Reference `tab:dvd-performance' on page 6 undefined on input lin\ne 278.\n\n\nLaTeX Warning: Reference `sec:ensemble' on page 6 undefined on input line 298.\n\n\nLaTeX Warning: Reference `tab:ensemble-strategies' on page 6 undefined on input\n line 303.\n\n[6]\n\nLaTeX Warning: Reference `tab:ablation' on page 7 undefined on input line 325.\n\n\nLaTeX Warning: Reference `tab:gsm8k-results' on page 7 undefined on input line \n349.\n\n\nLaTeX Warning: Reference `tab:cross-benchmark' on page 7 undefined on input lin\ne 368.\n\n[7]\n\nLaTeX Warning: Reference `tab:bifactor-fit' on page 8 undefined on input line 3\n89.\n\n\nLaTeX Warning: Reference `tab:equating-scope' on page 8 undefined on input line\n 411.\n\n\nLaTeX Warning: Reference `tab:calibration' on page 8 undefined on input line 43\n4.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8]\n\nLaTeX Warning: Reference `tab:bayesian-power' on page 9 undefined on input line\n 472.\n\n\nLaTeX Warning: Reference `tab:degradation' on page 9 undefined on input line 49\n5.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `sec:item-gen' on page 9 undefined on input line 518.\n\n\nLaTeX Warning: Reference `tab:ift-comparison' on page 9 undefined on input line\n 523.\n\n[9] [10] [11] [12] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.60\n0pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (12 pages, 233928 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2] [3] [4]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5] [6] [7]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9] [10] [11] [12] (./paper.aux) ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/p\nk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi5.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (12 pages, 236005 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b32ba967-6ccb-43f5-82d0-238a4b98799c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-20T20:08:01.156Z_

编译成功，12 页 PDF，无错误。

论文已写入 `paper.tex` 并编译为 `paper.pdf`（12 页）。覆盖了全部 10 个实验的 22 张表（合并为 18 张表呈现），按 narrative guidance 调整了三个 claim 的措辞：DIF 定位为"complementary signal with RL-robustness"而非唯一幸存者，ensemble 从三信号降为双信号并附 DVD failure mode analysis，equating 限定为 within-subject pilot 并给出 15% 替换上限的 degradation bounds。Related work 和 limitations 均已加厚。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a62c78c-14d0-455a-9127-b71134a7e5f8",
  "isSidechain": false,
  "requestId": "req_011CbERbmafnq4zLYB5CpgHh",
  "type": "assistant",
  "uuid": "87435271-6006-451d-9c55-2efe74fed9c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Y8mpbP12nSjhcpNsuC4qL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6055,
      "cache_read_input_tokens": 58093,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6055,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 58093,
          "cache_creation_input_tokens": 6055,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6055
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194223 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "87435271-6006-451d-9c55-2efe74fed9c9",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for IRT equated benchmark",
  "sessionId": "9ff65e0e-85d0-45d4-aed0-0e9fe9bbd8ea"
}
```

---
