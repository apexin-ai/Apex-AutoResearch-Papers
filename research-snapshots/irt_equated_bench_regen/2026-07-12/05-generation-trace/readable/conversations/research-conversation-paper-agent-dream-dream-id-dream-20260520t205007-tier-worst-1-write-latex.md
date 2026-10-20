# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T205007 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/14a5cd0b-7880-4b7c-a2e7-09d9a70e7731.jsonl`
- **Structured JSON:** [`de315e7ab6fec6c8d1a6.json`](../../sessions/de/de315e7ab6fec6c8d1a6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T21:21:35.706Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T21:21:35.706Z",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T205007 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：核心检测Claim不成立。IRT单维假设在LLM全群体上严重违反（RMSEA>0.12），架构分层后仅部分改善（RMSEA~0.10）。 DIF标记与能力增长高度混淆——within-family分析显示>60%的标记在已知无差异污染的家族内也出现， 因果归因不可靠。Semi-synthetic验证揭示检测power远低于simulation预期（TPR~0.40 at δ≥1.4）， 因真实response matrix的噪声结构（缺失模式、ceiling/floor效应、架构聚类）压制了信号。 Reframe方向：放弃\"DIF是污染检测器\"的叙事，转向(1)心理测量诊断——首个大规模实证证据说明 经典IRT为什么不能直接用于LLM评估，(2)混淆分离框架——量化污染与能力混淆程度的方法论贡献， (3)semi-synthetic评估基准——为任何污染检测器提供controlled ground truth。 仍为ICLR级贡献，但claim从\"我们能检测污染\"变为\"我们证明了为什么检测污染比社区认为的更难，并提供了正确的工具链\"。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T21:21:35.709Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T21:21:35.709Z",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-20T21:21:35.730Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T205007 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：核心检测Claim不成立。IRT单维假设在LLM全群体上严重违反（RMSEA>0.12），架构分层后仅部分改善（RMSEA~0.10）。 DIF标记与能力增长高度混淆——within-family分析显示>60%的标记在已知无差异污染的家族内也出现， 因果归因不可靠。Semi-synthetic验证揭示检测power远低于simulation预期（TPR~0.40 at δ≥1.4）， 因真实response matrix的噪声结构（缺失模式、ceiling/floor效应、架构聚类）压制了信号。 Reframe方向：放弃"DIF是污染检测器"的叙事，转向(1)心理测量诊断——首个大规模实证证据说明 经典IRT为什么不能直接用于LLM评估，(2)混淆分离框架——量化污染与能力混淆程度的方法论贡献， (3)semi-synthetic评估基准——为任何污染检测器提供controlled ground truth。 仍为ICLR级贡献，但claim从"我们能检测污染"变为"我们证明了为什么检测污染比社区认为的更难，并提供了正确的工具链"。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "7a9370c0-2bc7-4d59-8649-7bea7feea208",
  "type": "user",
  "uuid": "d266019a-46a1-4e1e-a68d-859a3d73c771",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T21:21:35.730Z_

```json
{
  "parentUuid": "d266019a-46a1-4e1e-a68d-859a3d73c771",
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
  "uuid": "82124188-ede5-44c3-a8aa-dd83ea63a4da",
  "timestamp": "2026-05-20T21:21:35.730Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T21:21:35.730Z_

```json
{
  "parentUuid": "82124188-ede5-44c3-a8aa-dd83ea63a4da",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ba77a755-ffd3-41af-9534-bc76a18c035a",
  "timestamp": "2026-05-20T21:21:35.730Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
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
  "aiTitle": "Generate simulated paper for dream_20260520T205007",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731"
}
```

---

### Assistant

_source line 7 · 2026-05-20T21:21:38.132Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba77a755-ffd3-41af-9534-bc76a18c035a",
  "isSidechain": false,
  "requestId": "req_011CbEXDkbxiBfuMyP82UfZ3",
  "type": "assistant",
  "uuid": "49e64e00-f8b5-441a-bf99-2eda40321eb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgKrJUzrDVv7Xat3ybEvxZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11564,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11564,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11564
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

_source line 8 · 2026-05-20T21:21:39.120Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GVFmn3ZYncNR977HyqvMQB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49e64e00-f8b5-441a-bf99-2eda40321eb1",
  "isSidechain": false,
  "requestId": "req_011CbEXDkbxiBfuMyP82UfZ3",
  "type": "assistant",
  "uuid": "810741e1-e9f5-4eff-a3a6-f35970140db8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgKrJUzrDVv7Xat3ybEvxZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11564,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11564,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11564
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

_source line 9 · 2026-05-20T21:21:39.385Z_

<details><summary>↩ Tool result · `toolu_01GVFmn3ZYncNR977HyqvMQB`</summary>

```text
1	[
2	  {
3	    "name": "real_data_dif_mmlu",
4	    "description": "对METABENCH MMLU全量数据（5,219模型×12,508题）运行DIF分析， 含时间队列划分、能力五分位划分、负区分度过滤敏感性分析、 within-family混淆控制、domain-specificity分析。\n",
5	    "results": {
6	      "irt_2pl_rmsea_full_population": 0.14,
7	      "irt_2pl_cfi_full_population": 0.72,
8	      "irt_2pl_rmsea_filtered_no_neg_disc": 0.11,
9	      "temporal_cohort_dif_flags_ets_c_count": 1850,
10	      "temporal_cohort_dif_flags_ets_c_rate": 0.148,
11	      "quintile_cohort_dif_flags_ets_c_count": 2300,
12	      "quintile_cohort_dif_flags_ets_c_rate": 0.184,
13	      "dif_flag_overlap_temporal_vs_quintile": 0.41,
14	      "mmlu_cf_validation_precision": 0.18,
15	      "mmlu_cf_validation_recall": 0.34,
16	      "mmlu_cf_cohen_kappa_vs_dif": 0.07,
17	      "within_family_confound_overlap_llama": 0.68,
18	      "within_family_confound_overlap_qwen": 0.61,
19	      "within_family_confound_overlap_mistral": 0.55,
20	      "within_family_confound_overlap_avg": 0.62,
21	      "domain_specificity_chi2_p": 0.23,
22	      "negative_disc_item_dif_rate": 0.31,
23	      "filtered_vs_unfiltered_flag_jaccard": 0.63
24	    },
25	    "tables": [
26	      {
27	        "title": "Table 1: IRT Model Fit Diagnostics (Full Population)",
28	        "columns": [
29	          "metric",
30	          "full_population",
31	          "neg_disc_filtered",
32	          "decoder_only_ref"
33	        ],
34	        "rows": [
35	          [
36	            "RMSEA",
37	            0.14,
38	            0.11,
39	            "see plan_010"
40	          ],
41	          [
42	            "CFI",
43	            0.72,
44	            0.79,
45	            "see plan_010"
46	          ],
47	          [
48	            "TLI",
49	            0.69,
50	            0.76,
51	            "see plan_010"
52	          ],
53	          [
54	            "SRMR",
55	            0.09,
56	            0.07,
57	            "see plan_010"
58	          ]
59	        ]
60	      },
61	      {
62	        "title": "Table 2: DIF Detection Summary by Cohort Definition",
63	        "columns": [
64	          "cohort_type",
65	          "n_ref",
66	          "n_focal",
67	          "dif_flags",
68	          "flag_rate",
69	          "overlap_w_other"
70	        ],
71	        "rows": [
72	          [
73	            "temporal_2023v2024",
74	            1253,
75	            656,
76	            1850,
77	            0.148,
78	            0.41
79	          ],
80	          [
81	            "quintile_Q1vQ5",
82	            1044,
83	            1044,
84	            2300,
85	            0.184,
86	            0.41
87	          ]
88	        ]
89	      },
90	      {
91	        "title": "Table 3: Within-Family Confound Analysis",
92	        "columns": [
93	          "family",
94	          "n_models",
95	          "cross_cohort_flags",
96	          "within_family_flags",
97	          "overlap_rate"
98	        ],
99	        "rows": [
100	          [
101	            "Llama-2/3/3.1",
102	            47,
103	            312,
104	            213,
105	            0.68
106	          ],
107	          [
108	            "Qwen-1.5/2/2.5",
109	            38,
110	            289,
111	            176,
112	            0.61
113	          ],
114	          [
115	            "Mistral/Mixtral",
116	            29,
117	            198,
118	            109,
119	            0.55
120	          ],
121	          [
122	            "weighted_avg",
123	            114,
124	            "—",
125	            "—",
126	            0.62
127	          ]
128	        ]
129	      }
130	    ],
131	    "figures": [],
132	    "analysis": "IRT模型拟合灾难性失败(RMSEA=0.14)是worst档的核心信号。这不是技术问题而是理论问题—— LLM群体的架构异质性使单维能力假设不成立。Within-family confound overlap 62%是致命发现： 如果Llama-2→3的DIF flag中2/3在已知无差异污染的升级路径中也出现， 那么DIF本质上在测量\"模型变好了\"而非\"模型被污染了\"。 MMLU-CF验证完全失败(κ=0.07)，但这可归因于MMLU-CF自身质量而非DIF—— 这为reframe提供了空间：MMLU-CF不适合做ground truth，需要semi-synthetic方法(plan_011)。 叙事转向：这些结果本身就是重要的负面发现——首次大规模实证证明DIF在LLM场景下的失效模式。\n\n\nRMSEA=0.14远超可接受阈值(0.08)，因LLM群体包含encoder-decoder、MoE、dense decoder-only等 异质架构，violate单维IRT的局部独立性假设。15.4%负区分度项进一步拉高misfit。 DIF检出率~15%看似合理，但within-family分析揭示致命问题：Llama-2→3→3.1系列中， 68%的cross-cohort DIF flag在family内也被标记——这些family内不存在差异污染（同一训练pipeline）， 说明DIF捕获的主要是能力增长而非污染。Qwen和Mistral系列类似(61%/55%)。 MMLU-CF验证极弱(κ=0.07)，因MMLU-CF自身标注一致性仅κ=0.14，无法作为可靠ground truth。 Domain-specificity分析未发现DIF flag在已知污染域vs已知能力提升域之间的显著聚类差异(p=0.23)， 混淆不可分离。两种cohort划分的flag overlap仅0.41，说明DIF结果对分组策略高度敏感。\n"
133	  },
134	  {
135	    "name": "rl_robustness_validation",
136	    "description": "验证DIF对RL训练的鲁棒性。含SFT基线队列、alignment-RL队列(DPO/ORPO)、 reasoning-RL队列(GRPO/PPO 10-15模型)的DIF分析，以及partial exploitation power分析。\n",
137	    "results": {
138	      "dif_flag_retention_sft_vs_alignrl": 0.82,
139	      "dif_flag_retention_sft_vs_reasonrl_mixed": 0.71,
140	      "rl_retention_ratio": 0.71,
141	      "constat_auroc_sft": 0.73,
142	      "constat_auroc_align_rl": 0.61,
143	      "constat_auroc_reason_rl": 0.48,
144	      "mink_auroc_sft": 0.68,
145	      "mink_auroc_reason_rl": 0.44,
146	      "dif_auroc_sft_cohort": 0.62,
147	      "dif_auroc_alignrl_cohort": 0.58,
148	      "dif_auroc_reasonrl_mixed_cohort": 0.55,
149	      "delong_dif_vs_constat_p": 0.31,
150	      "tost_equivalence_p": 0.18,
151	      "partial_exploit_tpr_p1_0": 0.42,
152	      "partial_exploit_tpr_p0_8": 0.33,
153	      "partial_exploit_tpr_p0_6": 0.24,
154	      "partial_exploit_tpr_p0_4": 0.15,
155	      "partial_exploit_ensemble_coverage_p0_6": 0.38,
156	      "bootstrap_ci_dif_auroc_95": [
157	        0.48,
158	        0.62
159	      ],
160	      "n_reasoning_rl_models_available": 12
161	    },
162	    "tables": [
163	      {
164	        "title": "Table 4: DIF vs Traditional Detectors Across RL Types",
165	        "columns": [
166	          "detector",
167	          "sft_auroc",
168	          "align_rl_auroc",
169	          "reason_rl_auroc",
170	          "retention_ratio"
171	        ],
172	        "rows": [
173	          [
174	            "DIF_ETS_C",
175	            0.62,
176	            0.58,
177	            0.55,
178	            0.71
179	          ],
180	          [
181	            "ConStat",
182	            0.73,
183	            0.61,
184	            0.48,
185	            0.66
186	          ],
187	          [
188	            "Min-K%",
189	            0.68,
190	            0.55,
191	            0.44,
192	            0.65
193	          ],
194	          [
195	            "Min-K%++",
196	            0.71,
197	            0.59,
198	            0.46,
199	            0.65
200	          ]
201	        ]
202	      },
203	      {
204	        "title": "Table 5: Partial Exploitation Power Curve",
205	        "columns": [
206	          "exploitation_rate_p",
207	          "dif_tpr",
208	          "dif_fpr",
209	          "ensemble_tpr",
210	          "ensemble_fpr"
211	        ],
212	        "rows": [
213	          [
214	            1.0,
215	            0.42,
216	            0.14,
217	            0.48,
218	            0.16
219	          ],
220	          [
221	            0.8,
222	            0.33,
223	            0.13,
224	            0.41,
225	            0.15
226	          ],
227	          [
228	            0.6,
229	            0.24,
230	            0.12,
231	            0.38,
232	            0.14
233	          ],
234	          [
235	            0.4,
236	            0.15,
237	            0.11,
238	            0.28,
239	            0.13
240	          ]
241	        ]
242	      }
243	    ],
244	    "figures": [],
245	    "analysis": "RL鲁棒性论证在worst档下变成了一个pyrrhic victory：DIF确实比ConStat/Min-K%更稳定， 但稳定在一个接近随机的水平。根本原因是plan_001的IRT misfit传导—— 如果item parameters估计不准（因为模型异质性违反假设），那么DIF统计量本身就是噪声的。 Reasoning-RL模型数量(N=12)不足以做统计推断，这一点在worst档下无法弥补。 Partial exploitation分析的simulation-to-real gap（0.72→0.42 at p=1.0）是关键发现—— 说明real response matrix的噪声结构（非随机缺失、ceiling效应、架构聚类）远比i.i.d. simulation假设的恶劣。 Reframe价值：这个gap本身就是方法论贡献——量化了simulation与现实的差距，为未来work设定了realistic expectations。\n\n\nDIF retention ratio 0.71表面上看\"还行\"，但置于worst语境下：(1)基线DIF AUROC本身就只有0.62 （因plan_001揭示的IRT misfit和confound问题），所以0.71的retention是在一个已经很弱的基线上， 实际AUROC≈0.55，接近随机。(2)仅12个reasoning-RL模型可用，统计power极低， bootstrap CI宽达[0.48,0.62]，跨过0.5随机线。(3)TOST等价性检验p=0.18>0.05， 无法声称DIF与ConStat\"等效\"——也无法声称DIF\"更好\"。DeLong检验p=0.31说明差异不显著， 但这是因为两者都很差而非两者都好。(4)Partial exploitation分析是worst档最具破坏性的发现： 真实response matrix噪声下，即使p=1.0的full exploitation，TPR也只有0.42（远低于simulation的0.72）， p=0.6时降至0.24。Ensemble在p=0.6时也仅0.38。结论：RL鲁棒性名义上成立（DIF不像ConStat 那样急剧下降），但在一个本身就不work的检测器上谈鲁棒性毫无意义。\n"
246	  },
247	  {
248	    "name": "constat_perturbation_eval",
249	    "description": "独立评估ConStat式perturbation testing在MMLU上的检测力， 含200+题的语义等价改写、原始vs改写性能比较、FDR控制检测。\n",
250	    "results": {
251	      "constat_auroc_non_rl": 0.54,
252	      "constat_auroc_sft_only": 0.62,
253	      "constat_auroc_rl_models": 0.43,
254	      "constat_fdr_controlled_tpr_alpha_0_05": 0.28,
255	      "constat_fdr_controlled_tpr_alpha_0_10": 0.36,
256	      "perturbation_quality_semantic_sim": 0.87,
257	      "perturbation_quality_human_eval": 0.79,
258	      "n_items_reformulated": 220,
259	      "reformulation_difficulty_shift_mean": 0.35,
260	      "reformulation_difficulty_shift_std": 0.41,
261	      "constat_detection_by_effect_size_small": 0.12,
262	      "constat_detection_by_effect_size_medium": 0.31,
263	      "constat_detection_by_effect_size_large": 0.52
264	    },
265	    "tables": [
266	      {
267	        "title": "Table 6: ConStat Detection Power by Model Type",
268	        "columns": [
269	          "model_type",
270	          "n_models",
271	          "auroc",
272	          "fdr_tpr_0_05",
273	          "fdr_tpr_0_10"
274	        ],
275	        "rows": [
276	          [
277	            "SFT-only",
278	            85,
279	            0.62,
280	            0.34,
281	            0.42
282	          ],
283	          [
284	            "Align-RL(DPO/ORPO)",
285	            65,
286	            0.51,
287	            0.22,
288	            0.31
289	          ],
290	          [
291	            "Reason-RL(GRPO)",
292	            12,
293	            0.43,
294	            0.15,
295	            0.24
296	          ],
297	          [
298	            "All",
299	            162,
300	            0.54,
301	            0.28,
302	            0.36
303	          ]
304	        ]
305	      },
306	      {
307	        "title": "Table 7: Perturbation Quality Assessment",
308	        "columns": [
309	          "metric",
310	          "mean",
311	          "std",
312	          "min",
313	          "max"
314	        ],
315	        "rows": [
316	          [
317	            "semantic_similarity",
318	            0.87,
319	            0.06,
320	            0.71,
321	            0.97
322	          ],
323	          [
324	            "difficulty_shift_logit",
325	            0.35,
326	            0.41,
327	            -0.52,
328	            1.83
329	          ],
330	          [
331	            "distractor_attractiveness_change",
332	            0.22,
333	            0.31,
334	            -0.18,
335	            1.12
336	          ]
337	        ]
338	      }
339	    ],
340	    "figures": [],
341	    "analysis": "ConStat失败的核心原因是perturbation-difficulty confound：改写不可避免地改变题目难度， 而这与contamination signal混淆。在worst档下这不意外——原ConStat论文在controlled setting 下work，但MMLU的选择题格式放大了perturbation artifact。RL AUROC<0.5说明信号反转， 不是ConStat的fault而是RL训练机制的必然结果。 Reframe价值：这些结果量化了perturbation-based方法的fundamental limitation， 为\"为什么需要新方法\"提供了实证论据。\n\n\nConStat在non-RL模型上AUROC=0.54，远低于原论文报告水平。原因：(1)perturbation本身引入 非平凡的难度偏移(mean=0.35 logit, std=0.41)——语义等价的改写不是心理测量等价的改写， contamination-free的项也会表现出原始vs改写差异。(2)MMLU的multiple-choice格式使 perturbation空间受限——改写选项措辞几乎不可避免地改变干扰项吸引力。(3)在RL模型上 AUROC=0.43<0.5，说明RL训练导致的output distribution平滑使perturbation sensitivity 方向反转——RL模型对改写更稳定（不是因为不污染，而是因为GRPO clipping压制了敏感性变化）。 FDR控制后TPR仅0.28(α=0.05)，大量真阳性在多重检验校正中被消除。 Worst档结论：ConStat作为standalone检测器在MMLU场景下不可靠。\n"
342	  },
343	  {
344	    "name": "dvd_generation_variance_eval",
345	    "description": "独立评估DVD generation variance在MMLU上的检测力， 含10-15个开源模型、每题50次temperature采样、方差分析。\n",
346	    "results": {
347	      "dvd_variant_detection_tpr": 0.23,
348	      "dvd_verbatim_detection_tpr": 0.31,
349	      "dvd_fpr": 0.14,
350	      "dvd_auroc_overall": 0.58,
351	      "n_models_evaluated": 13,
352	      "n_items_evaluated": 500,
353	      "generation_variance_contaminated_mean": 0.34,
354	      "generation_variance_clean_mean": 0.29,
355	      "generation_variance_overlap_coefficient": 0.72,
356	      "bimodal_detection_rate_contaminated": 0.18,
357	      "bimodal_detection_rate_clean": 0.11,
358	      "gpu_hours_used": 62
359	    },
360	    "tables": [
361	      {
362	        "title": "Table 8: DVD Detection Power",
363	        "columns": [
364	          "contamination_type",
365	          "tpr",
366	          "fpr",
367	          "auroc",
368	          "n_items"
369	        ],
370	        "rows": [
371	          [
372	            "verbatim",
373	            0.31,
374	            0.14,
375	            0.62,
376	            150
377	          ],
378	          [
379	            "variant",
380	            0.23,
381	            0.14,
382	            0.56,
383	            150
384	          ],
385	          [
386	            "overall",
387	            0.27,
388	            0.14,
389	            0.58,
390	            300
391	          ]
392	        ]
393	      },
394	      {
395	        "title": "Table 9: Generation Variance Distribution",
396	        "columns": [
397	          "item_status",
398	          "variance_mean",
399	          "variance_std",
400	          "bimodal_rate"
401	        ],
402	        "rows": [
403	          [
404	            "contaminated",
405	            0.34,
406	            0.18,
407	            0.18
408	          ],
409	          [
410	            "clean",
411	            0.29,
412	            0.16,
413	            0.11
414	          ],
415	          [
416	            "effect_size_d",
417	            0.3,
418	            "—",
419	            "—"
420	          ]
421	        ]
422	      }
423	    ],
424	    "figures": [],
425	    "analysis": "DVD在MCQ场景下的failure是structural的——output space太小，variance信号被compressed。 Effect size d=0.30属于small effect，在N=13模型×500题的规模下不足以支撑检测。 Reframe价值：这是MCQ format的fundamental limitation的实证证明， 推动社区思考format-aware的检测方法设计。\n\n\nDVD在worst档下表现差，原因：(1)MMLU是选择题——模型输出方差本身就很低（输出空间只有A/B/C/D）， generation variance的区分力受限于这个compressed output space。(2)Contaminated vs clean项 的方差分布高度重叠(overlap=0.72)——污染项不一定方差低（模型可能memorize了错误答案pattern）， clean项不一定方差高（能力足够的模型在easy项上也方差低）。(3)Bimodal detection在两类项上 差异不大(0.18 vs 0.11)，信噪比不足。(4)Multiple-choice格式下temperature采样的多样性 被logit差异主导而非memorization——高confidence的非污染回答也呈现低方差。 DVD更适合open-ended generation场景，在MCQ上fundamental limitation明显。\n"
426	  },
427	  {
428	    "name": "ensemble_fusion",
429	    "description": "将DIF+ConStat+DVD融合为多信号集成，含阈值校准、投票策略、覆盖分析。\n",
430	    "results": {
431	      "ensemble_tpr_delta_ge_0_8": 0.38,
432	      "ensemble_tpr_delta_ge_1_4": 0.48,
433	      "ensemble_fpr": 0.16,
434	      "majority_vote_tpr": 0.32,
435	      "majority_vote_fpr": 0.11,
436	      "weighted_fusion_tpr": 0.43,
437	      "weighted_fusion_fpr": 0.16,
438	      "uniform_weight_tpr": 0.39,
439	      "uniform_weight_fpr": 0.14,
440	      "cross_val_weight_stability_cv": 0.35,
441	      "dif_unique_contribution": 0.08,
442	      "constat_unique_contribution": 0.11,
443	      "dvd_unique_contribution": 0.05,
444	      "signal_correlation_dif_constat": 0.22,
445	      "signal_correlation_dif_dvd": 0.14,
446	      "signal_correlation_constat_dvd": 0.18
447	    },
448	    "tables": [
449	      {
450	        "title": "Table 10: Ensemble Fusion Strategy Comparison",
451	        "columns": [
452	          "strategy",
453	          "tpr_delta_ge_0_8",
454	          "tpr_delta_ge_1_4",
455	          "fpr",
456	          "f1"
457	        ],
458	        "rows": [
459	          [
460	            "DIF_only",
461	            0.28,
462	            0.42,
463	            0.14,
464	            0.33
465	          ],
466	          [
467	            "ConStat_only",
468	            0.31,
469	            0.36,
470	            0.12,
471	            0.34
472	          ],
473	          [
474	            "DVD_only",
475	            0.2,
476	            0.27,
477	            0.14,
478	            0.24
479	          ],
480	          [
481	            "majority_2of3",
482	            0.32,
483	            0.4,
484	            0.11,
485	            0.37
486	          ],
487	          [
488	            "weighted_fusion",
489	            0.43,
490	            0.48,
491	            0.16,
492	            0.4
493	          ],
494	          [
495	            "uniform_weight",
496	            0.39,
497	            0.45,
498	            0.14,
499	            0.39
500	          ]
501	        ]
502	      },
503	      {
504	        "title": "Table 11: Signal Correlation Matrix",
505	        "columns": [
506	          "signal_pair",
507	          "pearson_r",
508	          "overlap_flags"
509	        ],
510	        "rows": [
511	          [
512	            "DIF-ConStat",
513	            0.22,
514	            0.28
515	          ],
516	          [
517	            "DIF-DVD",
518	            0.14,
519	            0.19
520	          ],
521	          [
522	            "ConStat-DVD",
523	            0.18,
524	            0.23
525	          ]
526	        ]
527	      }
528	    ],
529	    "figures": [],
530	    "analysis": "Ensemble未能rescue单信号的weakness。\"互补覆盖\"的叙事在worst档下不成立—— 三个信号各自太弱，合并后仍太弱。但信号独立性分析(低相关)有方法论价值： 它说明DIF/ConStat/DVD确实capture不同的contamination facets， 只是每个facet上的power都不足。 Reframe：ensemble框架作为evaluation protocol有贡献——未来更强的单信号检测器 可以插入这个框架获得覆盖分析。\n\n\n三个弱检测器的ensemble不会产生强检测器——这是worst档的核心推论。 (1)每个信号AUROC都在0.54-0.62范围，信号间相关性低(0.14-0.22)看似有利于ensemble， 但低相关性在这里反映的是\"各自捕获不同的噪声\"而非\"各自捕获不同的信号\"。 (2)Weighted fusion优于majority vote(0.43 vs 0.32 TPR)，但FPR也更高(0.16 vs 0.11)。 Cross-validation显示权重不稳定(CV=0.35)，说明过拟合风险高。 (3)Ensemble TPR@δ≥1.4仅0.48——即使是大效应也有超过一半漏检。FPR=0.16意味着 每6个flag中有1个是误报，在12,508题的MMLU上产生~2000个false alarm。 (4)各信号unique contribution很小(5-11%)，说明重叠区域不是\"强化\"而是\"共同噪声\"。\n"
531	  },
532	  {
533	    "name": "cross_benchmark_gsm8k",
534	    "description": "在GSM8K上复制DIF分析，用GSM1K作为独立ground truth。 收集50+模型的per-item response，做temporal cohort DIF， 将DIF flag与per-model GSM8K-GSM1K accuracy gap关联。\n",
535	    "results": {
536	      "gsm8k_dif_flag_rate": 0.11,
537	      "gsm8k_gsm1k_gap_mean": 0.062,
538	      "gsm8k_gsm1k_gap_std": 0.078,
539	      "gsm8k_dif_gap_correlation_r": 0.14,
540	      "gsm8k_dif_gap_correlation_p": 0.32,
541	      "gsm8k_irt_rmsea": 0.1,
542	      "n_models_collected": 58,
543	      "n_gsm8k_items": 1319,
544	      "dif_tpr_against_gsm1k_proxy": 0.22,
545	      "dif_fpr_against_gsm1k_proxy": 0.09
546	    },
547	    "tables": [
548	      {
549	        "title": "Table 12: GSM8K Cross-Validation Results",
550	        "columns": [
551	          "metric",
552	          "value",
553	          "ci_95_lower",
554	          "ci_95_upper"
555	        ],
556	        "rows": [
557	          [
558	            "dif_gap_correlation_r",
559	            0.14,
560	            -0.12,
561	            0.38
562	          ],
563	          [
564	            "dif_tpr_vs_gsm1k",
565	            0.22,
566	            0.1,
567	            0.36
568	          ],
569	          [
570	            "dif_fpr_vs_gsm1k",
571	            0.09,
572	            0.04,
573	            0.16
574	          ],
575	          [
576	            "irt_rmsea",
577	            0.1,
578	            0.08,
579	            0.12
580	          ]
581	        ]
582	      }
583	    ],
584	    "figures": [],
585	    "analysis": "GSM8K验证失败彻底——r=0.14的95% CI包含零，无统计显著性。 这削弱了DIF作为跨benchmark通用检测器的claim。但分析揭示了一个有用的insight： model-level gap与item-level DIF的granularity mismatch是根本问题， 未来验证需要item-level ground truth（指向plan_011 semi-synthetic方法的必要性）。\n\n\nGSM8K交叉验证产出极弱相关(r=0.14, p=0.32)，原因：(1)GSM8K→GSM1K accuracy gap 是model-level指标，DIF flag是item-level指标，两者度量不同granularity的contamination， 对齐需要强假设（污染是均匀的across items）。(2)GSM8K的math reasoning性质使能力增长 与contamination更难分离——新模型genuinely更擅长数学，gap可能反映的是eval methodology差异 而非contamination。(3)GSM8K仅1,319题，N=58模型，统计power不足。(4)IRT fit在GSM8K上 好于MMLU(RMSEA=0.10)因为数学题更unidimensional，但仍在边界区间。 DIF在GSM1K proxy ground truth上的TPR=0.22极低，说明DIF flag与已知ground truth不对齐。\n"
586	  },
587	  {
588	    "name": "bifactor_irt_equating_pilot",
589	    "description": "在METABENCH MMLU上拟合bifactor IRT模型（通用因子+学科因子）， 选锚题，做固定参数校准，验证等值分数等效性。\n",
590	    "results": {
591	      "bifactor_convergence": false,
592	      "bifactor_convergence_subset_n_subjects": 8,
593	      "bifactor_rmsea_subset": 0.09,
594	      "bifactor_general_factor_variance_explained": 0.38,
595	      "bifactor_subject_factor_variance_explained": 0.31,
596	      "bifactor_residual_variance": 0.31,
597	      "anchor_item_count": 145,
598	      "anchor_item_stability_criterion_met_rate": 0.12,
599	      "equated_score_spearman_rho": 0.84,
600	      "equated_vs_original_rank_displacement_mean": 23,
601	      "equated_vs_original_rank_displacement_max": 312,
602	      "fixed_param_calibration_convergence_rate": 0.71
603	    },
604	    "tables": [
605	      {
606	        "title": "Table 13: Bifactor Model Fit",
607	        "columns": [
608	          "scope",
609	          "convergence",
610	          "rmsea",
611	          "gen_var",
612	          "subj_var",
613	          "resid_var"
614	        ],
615	        "rows": [
616	          [
617	            "full_57_subjects",
618	            false,
619	            "—",
620	            "—",
621	            "—",
622	            "—"
623	          ],
624	          [
625	            "subset_8_subjects",
626	            true,
627	            0.09,
628	            0.38,
629	            0.31,
630	            0.31
631	          ],
632	          [
633	            "subset_4_stem",
634	            true,
635	            0.07,
636	            0.44,
637	            0.28,
638	            0.28
639	          ]
640	        ]
641	      },
642	      {
643	        "title": "Table 14: Equating Quality",
644	        "columns": [
645	          "metric",
646	          "value",
647	          "target",
648	          "met"
649	        ],
650	        "rows": [
651	          [
652	            "anchor_items",
653	            145,
654	            ">500",
655	            false
656	          ],
657	          [
658	            "anchor_stability_rate",
659	            0.12,
660	            ">0.80",
661	            false
662	          ],
663	          [
664	            "spearman_rho",
665	            0.84,
666	            ">0.95",
667	            false
668	          ],
669	          [
670	            "rank_displacement_mean",
671	            23,
672	            "<5",
673	            false
674	          ],
675	          [
676	            "fixed_param_convergence",
677	            0.71,
678	            ">0.90",
679	            false
680	          ]
681	        ]
682	      }
683	    ],
684	    "figures": [],
685	    "analysis": "Bifactor不收敛直接否定Claim 3。子集上的勉强收敛不足以支撑full-scale regeneration。 核心问题是LLM能力的multidimensionality——38%通用因子方差说明超过60%的variance是 domain-specific或residual的，单一等值框架不适用。 但这个负面结果本身有价值：它是首个大规模实证证据说明bifactor IRT在LLM评估中的失效模式。 Reframe：砍掉Claim 3，或将其降格为\"在homogeneous subdomain内可行的局部等值\"。\n\n\nBifactor模型在完整57学科上不收敛——这是worst档的defining prediction。原因： (1)12,508题×5,219模型的response matrix过于稀疏（many models没做完全部MMLU）， bifactor需要估计的参数量(2×12508 + 57个学科因子loading)远超有效sample size。 (2)学科因子间不正交——STEM学科高度相关，humanities学科高度相关，违反bifactor的 近似正交假设。(3)通用因子仅解释38%方差——LLM能力高度multidimensional， 单一g-factor模型不适用。退而求其次在8个大学科子集上可以收敛(RMSEA=0.09)， 但这意味着跨学科等值不可行。锚题仅145个（<1.2%的题），稳定性达标率仅12%—— 大多数\"稳定\"题在不同cohort下参数也在漂移，因为IRT参数估计本身就不稳定。 Spearman ρ=0.84看似可接受但低于0.95目标，且mean rank displacement=23意味着 约5%的模型排名变动超过1个百分位——对leaderboard而言不可接受。\n"
686	  },
687	  {
688	    "name": "item_generation_calibration",
689	    "description": "为DIF-flagged MMLU题生成替代项，用student simulation校准难度， 比较prompt-based vs empirical calibration。\n",
690	    "results": {
691	      "n_items_generated": 300,
692	      "prompt_difficulty_correlation_rho": 0.21,
693	      "student_sim_difficulty_correlation_rho": 0.58,
694	      "student_sim_discrimination_correlation_rho": 0.41,
695	      "construct_validity_factor_loading_mean": 0.52,
696	      "construct_validity_factor_loading_target": 0.7,
697	      "replacement_item_acceptance_rate": 0.34,
698	      "difficulty_rmse_vs_original": 1.12,
699	      "discrimination_rmse_vs_original": 0.48
700	    },
701	    "tables": [
702	      {
703	        "title": "Table 15: Item Generation Calibration Quality",
704	        "columns": [
705	          "calibration_method",
706	          "difficulty_rho",
707	          "discrimination_rho",
708	          "construct_loading"
709	        ],
710	        "rows": [
711	          [
712	            "prompt_based",
713	            0.21,
714	            0.14,
715	            0.48
716	          ],
717	          [
718	            "student_simulation",
719	            0.58,
720	            0.41,
721	            0.52
722	          ],
723	          [
724	            "target",
725	            ">0.75",
726	            ">0.60",
727	            ">0.70"
728	          ]
729	        ]
730	      }
731	    ],
732	    "figures": [],
733	    "analysis": "Item generation在worst档下quality insufficient for regeneration。 Student simulation的partial success (ρ=0.58)相比prompt-based (ρ=0.21)是有意义的improvement， 但距离psychometrically equivalent replacement还有大gap。 Reframe：student simulation方法论贡献仍在，但regeneration pipeline需要更多研发。\n\n\nPrompt-based difficulty targeting一如文献预期地差(ρ=0.21)。Student simulation 改善显著(ρ=0.58)但仍低于文献报告的0.75-0.82——因为MMLU的多学科异质性使得 单一student simulation模型难以同时校准STEM和humanities。 Construct validity是biggest failure：生成项的平均factor loading=0.52 vs 目标0.70， 说明LLM生成的替代题虽然表面上在同一学科、同一认知水平，但测量的实际construct有偏移。 仅34%的生成项满足acceptance criteria（难度、区分度、factor loading全部达标）， 意味着要替换100个flagged题需要生成~300个candidate——成本和质量控制问题突出。\n"
734	  },
735	  {
736	    "name": "cumulative_bayesian_dif",
737	    "description": "实现累积Bayesian DIF prior (Sinharay et al., 2006)， 模拟4次连续benchmark administration，展示累积power改善。\n",
738	    "results": {
739	      "single_admin_power_medium_delta_1_0": 0.22,
740	      "cumulative_2_admin_power": 0.31,
741	      "cumulative_3_admin_power": 0.39,
742	      "cumulative_4_admin_power": 0.45,
743	      "simulation_single_admin_power": 0.4,
744	      "power_improvement_factor_4_admin": 2.05,
745	      "bayes_factor_threshold_sensitivity": "BF>3 at 4th admin for 45% of truly contaminated items"
746	    },
747	    "tables": [
748	      {
749	        "title": "Table 16: Cumulative Bayesian DIF Power",
750	        "columns": [
751	          "n_administrations",
752	          "power_real",
753	          "power_simulation",
754	          "ratio"
755	        ],
756	        "rows": [
757	          [
758	            1,
759	            0.22,
760	            0.4,
761	            0.55
762	          ],
763	          [
764	            2,
765	            0.31,
766	            0.54,
767	            0.57
768	          ],
769	          [
770	            3,
771	            0.39,
772	            0.64,
773	            0.61
774	          ],
775	          [
776	            4,
777	            0.45,
778	            0.7,
779	            0.64
780	          ]
781	        ]
782	      }
783	    ],
784	    "figures": [],
785	    "analysis": "Bayesian accumulation帮助但不足以rescue。Simulation-to-real gap从0.55扩大到0.64 说明累积过程在amplify real data的systematic bias。方法论仍有价值但需要加入 item parameter drift correction。\n\n\n起点power=0.22（非simulation的0.40）——因为base DIF检测power在real data上已经degraded （plan_001的发现传导到这里）。累积后达到0.45——2x improvement看似decent，但绝对水平 仍不足以做可靠检测。原因：Bayesian prior accumulation假设item parameters在administrations 间是stable的，但LLM evaluation的\"administrations\"是不同时期的模型群体， item parameters本身可能在drift（因为新模型能力profile不同）。Prior可能在accumulate 过时信息而非strengthen信号。\n"
786	  },
787	  {
788	    "name": "graceful_degradation_analysis",
789	    "description": "分析benchmark在不同替换率下的validity退化：排名稳定性、分数信度、construct覆盖。\n",
790	    "results": {
791	      "ranking_stability_5pct_replace": 0.96,
792	      "ranking_stability_10pct_replace": 0.91,
793	      "ranking_stability_20pct_replace": 0.82,
794	      "ranking_stability_50pct_replace": 0.63,
795	      "score_reliability_5pct": 0.94,
796	      "score_reliability_10pct": 0.89,
797	      "score_reliability_20pct": 0.78,
798	      "score_reliability_50pct": 0.55,
799	      "construct_coverage_20pct": 0.85,
800	      "construct_coverage_50pct": 0.61,
801	      "acceptable_replacement_threshold": "5-10%"
802	    },
803	    "tables": [
804	      {
805	        "title": "Table 17: Graceful Degradation Curves",
806	        "columns": [
807	          "replace_rate",
808	          "rank_stability",
809	          "score_reliability",
810	          "construct_coverage"
811	        ],
812	        "rows": [
813	          [
814	            0.05,
815	            0.96,
816	            0.94,
817	            0.97
818	          ],
819	          [
820	            0.1,
821	            0.91,
822	            0.89,
823	            0.93
824	          ],
825	          [
826	            0.2,
827	            0.82,
828	            0.78,
829	            0.85
830	          ],
831	          [
832	            0.5,
833	            0.63,
834	            0.55,
835	            0.61
836	          ]
837	        ]
838	      }
839	    ],
840	    "figures": [],
841	    "analysis": "Degradation analysis在worst档下更像一个cautionary tale：它量化了low-quality replacement 的代价，为\"为什么item generation需要更好的calibration\"提供实证。 独立贡献是degradation framework本身——可用于任何benchmark regeneration方案的evaluation。\n\n\n在worst档下，替换项质量低(plan_006的factor loading=0.52)导致退化速度快于理论预期。 10%替换时ranking stability=0.91，低于通常acceptable的0.95——因为替换项不仅改变难度 还改变construct coverage。20%替换时信度降至0.78，50%时本质上是一个不同的test。 可接受阈值仅5-10%，意味着如果DIF flags 15%的题为contaminated， 即使全部替换也只有勉强够用。但如果contamination更广泛，regeneration不可行。\n"
842	  },
843	  {
844	    "name": "item_focused_trees",
845	    "description": "实现Item-Focused Trees (Tutz & Berger, 2016)作为categorical cohort DIF的替代， 将模型release date作为连续协变量。\n",
846	    "results": {
847	      "ift_auroc": 0.57,
848	      "ift_vs_categorical_dif_flag_overlap": 0.48,
849	      "ift_tpr_delta_ge_1_4": 0.39,
850	      "ift_fpr": 0.12,
851	      "ift_rmsea_improvement": 0.01,
852	      "ift_tree_depth_mean": 2.3,
853	      "ift_overfitting_cv_gap": 0.09
854	    },
855	    "tables": [
856	      {
857	        "title": "Table 18: IFT vs Categorical DIF Comparison",
858	        "columns": [
859	          "method",
860	          "auroc",
861	          "tpr_delta_ge_1_4",
862	          "fpr",
863	          "flag_count"
864	        ],
865	        "rows": [
866	          [
867	            "categorical_temporal",
868	            0.55,
869	            0.42,
870	            0.14,
871	            1850
872	          ],
873	          [
874	            "categorical_quintile",
875	            0.53,
876	            0.38,
877	            0.16,
878	            2300
879	          ],
880	          [
881	            "item_focused_tree",
882	            0.57,
883	            0.39,
884	            0.12,
885	            1620
886	          ]
887	        ]
888	      }
889	    ],
890	    "figures": [],
891	    "analysis": "IFT不能rescue DIF——问题在上游(IRT假设违反)，不在cohort定义。 但IFT vs categorical的disagreement是有用的diagnostic： 它量化了DIF结果对分析选择的敏感性，支撑\"DIF不适合做检测器\"的conclusion。\n\n\nIFT避免了arbitrary cohort划分，理论上更flexible。但worst档下： (1)AUROC=0.57仅marginal improvement over categorical DIF(~0.55)——因为底层IRT misfit 不是cohort定义的问题，而是模型异质性的问题，IFT不能修复这个。 (2)与categorical DIF的flag overlap仅0.48——两种方法不同意一半的flag， 说明DIF结果fundamentally unstable，不取决于\"真正的contamination\"而取决于方法选择。 (3)Overfitting gap=0.09说明tree在capture noise而非signal。\n"
892	  },
893	  {
894	    "name": "architecture_stratified_dif",
895	    "description": "在decoder-only同质子群体上运行DIF，测试IRT拟合是否改善、spurious DIF是否减少。\n",
896	    "results": {
897	      "decoder_only_n_models": 3420,
898	      "decoder_only_rmsea": 0.1,
899	      "decoder_only_cfi": 0.82,
900	      "decoder_only_tli": 0.79,
901	      "full_pop_rmsea_ref": 0.14,
902	      "rmsea_improvement": 0.04,
903	      "dif_flag_rate_decoder_only": 0.12,
904	      "dif_flag_rate_full_pop_ref": 0.148,
905	      "fpr_decoder_only": 0.11,
906	      "fpr_full_pop_ref": 0.14,
907	      "tpr_decoder_only_delta_ge_1_4": 0.45,
908	      "within_family_confound_overlap_decoder_only": 0.55,
909	      "moe_vs_dense_subanalysis_rmsea_dense": 0.08,
910	      "moe_vs_dense_subanalysis_rmsea_moe": 0.12
911	    },
912	    "tables": [
913	      {
914	        "title": "Table 19: Architecture Stratification Effect",
915	        "columns": [
916	          "population",
917	          "n_models",
918	          "rmsea",
919	          "cfi",
920	          "dif_flag_rate",
921	          "fpr",
922	          "within_fam_overlap"
923	        ],
924	        "rows": [
925	          [
926	            "full_population",
927	            5219,
928	            0.14,
929	            0.72,
930	            0.148,
931	            0.14,
932	            0.62
933	          ],
934	          [
935	            "decoder_only",
936	            3420,
937	            0.1,
938	            0.82,
939	            0.12,
940	            0.11,
941	            0.55
942	          ],
943	          [
944	            "decoder_dense_only",
945	            1850,
946	            0.08,
947	            0.88,
948	            0.098,
949	            0.08,
950	            0.47
951	          ],
952	          [
953	            "decoder_moe_only",
954	            380,
955	            0.12,
956	            0.78,
957	            0.135,
958	            0.13,
959	            0.58
960	          ]
961	        ]
962	      },
963	      {
964	        "title": "Table 20: Fit Diagnostic Breakdown",
965	        "columns": [
966	          "subgroup",
967	          "rmsea",
968	          "n",
969	          "effective_power_at_d_1_4"
970	        ],
971	        "rows": [
972	          [
973	            "all_decoder",
974	            0.1,
975	            3420,
976	            0.45
977	          ],
978	          [
979	            "dense_small_1B_7B",
980	            0.07,
981	            1200,
982	            0.38
983	          ],
984	          [
985	            "dense_large_13B_70B",
986	            0.09,
987	            650,
988	            0.42
989	          ],
990	          [
991	            "moe_all",
992	            0.12,
993	            380,
994	            0.3
995	          ]
996	        ]
997	      }
998	    ],
999	    "figures": [],
1000	    "analysis": "Plan_010是worst档最有价值的实验——它精确量化了IRT misfit的来源和修复成本。 结论：\"DIF要work需要architecture-homogeneous populations\"是一个actionable finding， 但代价是严重的power loss。这直接支撑reframe angle (1)—— \"为什么经典心理测量不能直接用于LLM\"的诊断性贡献。 Dense-only RMSEA=0.08是一个hope signal，但N=1850+within-family overlap=0.47 说明即使在最favorable condition下confounding仍是dominant problem。\n\n\nArchitecture stratification帮助但不够——这是worst档的关键特征。 RMSEA从0.14降到0.10：improvement是real的(Δ=0.04)但0.10仍在borderline-to-poor区间 (acceptable threshold是0.08)。原因：decoder-only内部仍有substantial heterogeneity—— MoE vs dense, 不同parameter scales (1B-70B), 不同tokenizer, 不同training data。 去除architecture heterogeneity是necessary but not sufficient。 DIF flag rate降低(0.12 vs 0.148)和FPR降低(0.11 vs 0.14)说明部分spurious DIF 确实来自architecture差异，但幅度有限。Within-family confound overlap从0.62降到0.55—— 仍然>50%的flag是confounded。Dense-only进一步分析(RMSEA=0.08)暗示如果进一步 subset到完全homogeneous群体，fit会acceptable——但代价是N大幅缩小，power更低。\n"
1001	  },
1002	  {
1003	    "name": "semi_synthetic_contamination_validation",
1004	    "description": "在真实METABENCH response matrix中注入已知contamination， 测量DIF检测power under controlled ground truth。\n",
1005	    "results": {
1006	      "semi_synthetic_tpr_delta_ge_1_4": 0.41,
1007	      "semi_synthetic_tpr_delta_ge_1_0": 0.28,
1008	      "semi_synthetic_tpr_delta_ge_0_6": 0.15,
1009	      "semi_synthetic_fpr": 0.14,
1010	      "prevalence_5pct_tpr": 0.48,
1011	      "prevalence_15pct_tpr": 0.39,
1012	      "prevalence_30pct_tpr": 0.33,
1013	      "exploit_rate_1_0_tpr": 0.41,
1014	      "exploit_rate_0_8_tpr": 0.33,
1015	      "exploit_rate_0_6_tpr": 0.24,
1016	      "exploit_rate_0_4_tpr": 0.14,
1017	      "focal_n_40_tpr": 0.29,
1018	      "focal_n_100_tpr": 0.41,
1019	      "focal_n_200_tpr": 0.47,
1020	      "simulation_vs_semi_synthetic_gap_tpr": 0.31,
1021	      "simulation_tpr_reference_delta_1_4": 0.72
1022	    },
1023	    "tables": [
1024	      {
1025	        "title": "Table 21: Semi-Synthetic Detection Power Matrix",
1026	        "columns": [
1027	          "delta",
1028	          "prevalence",
1029	          "exploit_rate",
1030	          "tpr",
1031	          "fpr",
1032	          "auroc"
1033	        ],
1034	        "rows": [
1035	          [
1036	            1.4,
1037	            0.15,
1038	            1.0,
1039	            0.41,
1040	            0.14,
1041	            0.68
1042	          ],
1043	          [
1044	            1.4,
1045	            0.15,
1046	            0.6,
1047	            0.24,
1048	            0.13,
1049	            0.59
1050	          ],
1051	          [
1052	            1.0,
1053	            0.15,
1054	            1.0,
1055	            0.28,
1056	            0.14,
1057	            0.6
1058	          ],
1059	          [
1060	            1.0,
1061	            0.15,
1062	            0.6,
1063	            0.17,
1064	            0.13,
1065	            0.54
1066	          ],
1067	          [
1068	            0.6,
1069	            0.15,
1070	            1.0,
1071	            0.15,
1072	            0.14,
1073	            0.52
1074	          ]
1075	        ]
1076	      },
1077	      {
1078	        "title": "Table 22: Simulation vs Semi-Synthetic Gap",
1079	        "columns": [
1080	          "condition",
1081	          "sim_tpr",
1082	          "semi_syn_tpr",
1083	          "gap",
1084	          "gap_pct"
1085	        ],
1086	        "rows": [
1087	          [
1088	            "N100_d1.4_p1.0",
1089	            0.72,
1090	            0.41,
1091	            0.31,
1092	            "43%"
1093	          ],
1094	          [
1095	            "N100_d1.0_p1.0",
1096	            0.52,
1097	            0.28,
1098	            0.24,
1099	            "46%"
1100	          ],
1101	          [
1102	            "N80_d1.4_p1.0",
1103	            0.68,
1104	            0.38,
1105	            0.3,
1106	            "44%"
1107	          ]
1108	        ]
1109	      },
1110	      {
1111	        "title": "Table 23: Focal Group Size Effect",
1112	        "columns": [
1113	          "focal_n",
1114	          "tpr_d1_4",
1115	          "fpr",
1116	          "power_gain_per_10_models"
1117	        ],
1118	        "rows": [
1119	          [
1120	            40,
1121	            0.29,
1122	            0.15,
1123	            "—"
1124	          ],
1125	          [
1126	            60,
1127	            0.34,
1128	            0.14,
1129	            0.025
1130	          ],
1131	          [
1132	            80,
1133	            0.38,
1134	            0.14,
1135	            0.02
1136	          ],
1137	          [
1138	            100,
1139	            0.41,
1140	            0.14,
1141	            0.015
1142	          ],
1143	          [
1144	            200,
1145	            0.47,
1146	            0.13,
1147	            0.006
1148	          ]
1149	        ]
1150	      }
1151	    ],
1152	    "figures": [],
1153	    "analysis": "Plan_011是worst档的cornerstone experiment。它做了三件事： (1)Definitively证明simulation结果不能translate to real data（~40% gap），为社区设定realistic expectations。 (2)量化了real response matrix的noise sources——missing pattern, ceiling/floor, architecture clustering—— 这些是任何基于IRT的检测方法都会面对的，不仅限于DIF。 (3)Semi-synthetic框架本身是方法论贡献——它是MMLU-CF(κ=0.14)和GSM1K的superior alternative， 因为它提供item-level controlled ground truth。 即使DIF作为检测器fails，semi-synthetic validation framework对评估未来任何检测器都有价值。 这直接支撑reframe angle (3)。 关键insight：仅δ≥2.0的极大效应可检测(TPR>0.5)——对应~20pp accuracy inflation， 即只有最严重的contamination能被任何方法可靠检测。\n\nSemi-synthetic验证是worst档的smoking gun。TPR@δ≥1.4=0.41，远低于pure simulation的0.72。 Gap=0.31(0.72-0.41)量化了simulation与现实的差距。原因清晰： (1)真实response matrix有non-random missing pattern——不是所有模型都做了全部题， missingness与model capability相关，biases IRT parameter estimation。 (2)Ceiling/floor效应——easy题上所有模型都对，hard题上所有模型都错， 这些题的DIF无法检测（因为没有ability-conditional variation）。 (3)Architecture clustering——同family模型response pattern高度相关， violate DIF的independent observations假设。 (4)Injection本身可能\"太干净\"——real contamination不是uniform probability flip， 而是pattern-dependent（模型倾向于memorize特定类型的题）， 但这个bias direction使semi-synthetic结果成为optimistic estimate。 Prevalence依赖反直觉(5%>15%>30%)——因为高prevalence时injected signal淹没在 baseline noise中，DIF的focal-reference contrast被稀释。 FPR=0.14>>0.05目标，因为real matrix中的existing contamination （我们不知道的ground truth）产生false positive contamination。\n"
1154	  }
1155	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "810741e1-e9f5-4eff-a3a6-f35970140db8",
  "isSidechain": false,
  "promptId": "7a9370c0-2bc7-4d59-8649-7bea7feea208",
  "type": "user",
  "uuid": "930269c4-8f63-4ddd-92ec-903aee23453d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"real_data_dif_mmlu\",\n    \"description\": \"对METABENCH MMLU全量数据（5,219模型×12,508题）运行DIF分析， 含时间队列划分、能力五分位划分、负区分度过滤敏感性分析、 within-family混淆控制、domain-specificity分析。\\n\",\n    \"results\": {\n      \"irt_2pl_rmsea_full_population\": 0.14,\n      \"irt_2pl_cfi_full_population\": 0.72,\n      \"irt_2pl_rmsea_filtered_no_neg_disc\": 0.11,\n      \"temporal_cohort_dif_flags_ets_c_count\": 1850,\n      \"temporal_cohort_dif_flags_ets_c_rate\": 0.148,\n      \"quintile_cohort_dif_flags_ets_c_count\": 2300,\n      \"quintile_cohort_dif_flags_ets_c_rate\": 0.184,\n      \"dif_flag_overlap_temporal_vs_quintile\": 0.41,\n      \"mmlu_cf_validation_precision\": 0.18,\n      \"mmlu_cf_validation_recall\": 0.34,\n      \"mmlu_cf_cohen_kappa_vs_dif\": 0.07,\n      \"within_family_confound_overlap_llama\": 0.68,\n      \"within_family_confound_overlap_qwen\": 0.61,\n      \"within_family_confound_overlap_mistral\": 0.55,\n      \"within_family_confound_overlap_avg\": 0.62,\n      \"domain_specificity_chi2_p\": 0.23,\n      \"negative_disc_item_dif_rate\": 0.31,\n      \"filtered_vs_unfiltered_flag_jaccard\": 0.63\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 1: IRT Model Fit Diagnostics (Full Population)\",\n        \"columns\": [\n          \"metric\",\n          \"full_population\",\n          \"neg_disc_filtered\",\n          \"decoder_only_ref\"\n        ],\n        \"rows\": [\n          [\n            \"RMSEA\",\n            0.14,\n            0.11,\n            \"see plan_010\"\n          ],\n          [\n            \"CFI\",\n            0.72,\n            0.79,\n            \"see plan_010\"\n          ],\n          [\n            \"TLI\",\n            0.69,\n            0.76,\n            \"see plan_010\"\n          ],\n          [\n            \"SRMR\",\n            0.09,\n            0.07,\n            \"see plan_010\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 2: DIF Detection Summary by Cohort Definition\",\n        \"columns\": [\n          \"cohort_type\",\n          \"n_ref\",\n          \"n_focal\",\n          \"dif_flags\",\n          \"flag_rate\",\n          \"overlap_w_other\"\n        ],\n        \"rows\": [\n          [\n            \"temporal_2023v2024\",\n            1253,\n            656,\n            1850,\n            0.148,\n            0.41\n          ],\n          [\n            \"quintile_Q1vQ5\",\n            1044,\n            1044,\n            2300,\n            0.184,\n            0.41\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 3: Within-Family Confound Analysis\",\n        \"columns\": [\n          \"family\",\n          \"n_models\",\n          \"cross_cohort_flags\",\n          \"within_family_flags\",\n          \"overlap_rate\"\n        ],\n        \"rows\": [\n          [\n            \"Llama-2/3/3.1\",\n            47,\n            312,\n            213,\n            0.68\n          ],\n          [\n            \"Qwen-1.5/2/2.5\",\n            38,\n            289,\n            176,\n            0.61\n          ],\n          [\n            \"Mistral/Mixtral\",\n            29,\n            198,\n            109,\n            0.55\n          ],\n          [\n            \"weighted_avg\",\n            114,\n            \"—\",\n            \"—\",\n            0.62\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"IRT模型拟合灾难性失败(RMSEA=0.14)是worst档的核心信号。这不是技术问题而是理论问题—— LLM群体的架构异质性使单维能力假设不成立。Within-family confound overlap 62%是致命发现： 如果Llama-2→3的DIF flag中2/3在已知无差异污染的升级路径中也出现， 那么DIF本质上在测量\\\"模型变好了\\\"而非\\\"模型被污染了\\\"。 MMLU-CF验证完全失败(κ=0.07)，但这可归因于MMLU-CF自身质量而非DIF—— 这为reframe提供了空间：MMLU-CF不适合做ground truth，需要semi-synthetic方法(plan_011)。 叙事转向：这些结果本身就是重要的负面发现——首次大规模实证证明DIF在LLM场景下的失效模式。\\n\\n\\nRMSEA=0.14远超可接受阈值(0.08)，因LLM群体包含encoder-decoder、MoE、dense decoder-only等 异质架构，violate单维IRT的局部独立性假设。15.4%负区分度项进一步拉高misfit。 DIF检出率~15%看似合理，但within-family分析揭示致命问题：Llama-2→3→3.1系列中， 68%的cross-cohort DIF flag在family内也被标记——这些family内不存在差异污染（同一训练pipeline）， 说明DIF捕获的主要是能力增长而非污染。Qwen和Mistral系列类似(61%/55%)。 MMLU-CF验证极弱(κ=0.07)，因MMLU-CF自身标注一致性仅κ=0.14，无法作为可靠ground truth。 Domain-specificity分析未发现DIF flag在已知污染域vs已知能力提升域之间的显著聚类差异(p=0.23)， 混淆不可分离。两种cohort划分的flag overlap仅0.41，说明DIF结果对分组策略高度敏感。\\n\"\n  },\n  {\n    \"name\": \"rl_robustness_validation\",\n    \"description\": \"验证DIF对RL训练的鲁棒性。含SFT基线队列、alignment-RL队列(DPO/ORPO)、 reasoning-RL队列(GRPO/PPO 10-15模型)的DIF分析，以及partial exploitation power分析。\\n\",\n    \"results\": {\n      \"dif_flag_retention_sft_vs_alignrl\": 0.82,\n      \"dif_flag_retention_sft_vs_reasonrl_mixed\": 0.71,\n      \"rl_retention_ratio\": 0.71,\n      \"constat_auroc_sft\": 0.73,\n      \"constat_auroc_align_rl\": 0.61,\n      \"constat_auroc_reason_rl\": 0.48,\n      \"mink_auroc_sft\": 0.68,\n      \"mink_auroc_reason_rl\": 0.44,\n      \"dif_auroc_sft_cohort\": 0.62,\n      \"dif_auroc_alignrl_cohort\": 0.58,\n      \"dif_auroc_reasonrl_mixed_cohort\": 0.55,\n      \"delong_dif_vs_constat_p\": 0.31,\n      \"tost_equivalence_p\": 0.18,\n      \"partial_exploit_tpr_p1_0\": 0.42,\n      \"partial_exploit_tpr_p0_8\": 0.33,\n      \"partial_exploit_tpr_p0_6\": 0.24,\n      \"partial_exploit_tpr_p0_4\": 0.15,\n      \"partial_exploit_ensemble_coverage_p0_6\": 0.38,\n      \"bootstrap_ci_dif_auroc_95\": [\n        0.48,\n        0.62\n      ],\n      \"n_reasoning_rl_models_available\": 12\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 4: DIF vs Traditional Detectors Across RL Types\",\n        \"columns\": [\n          \"detector\",\n          \"sft_auroc\",\n          \"align_rl_auroc\",\n          \"reason_rl_auroc\",\n          \"retention_ratio\"\n        ],\n        \"rows\": [\n          [\n            \"DIF_ETS_C\",\n            0.62,\n            0.58,\n            0.55,\n            0.71\n          ],\n          [\n            \"ConStat\",\n            0.73,\n            0.61,\n            0.48,\n            0.66\n          ],\n          [\n            \"Min-K%\",\n            0.68,\n            0.55,\n            0.44,\n            0.65\n          ],\n          [\n            \"Min-K%++\",\n            0.71,\n            0.59,\n            0.46,\n            0.65\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 5: Partial Exploitation Power Curve\",\n        \"columns\": [\n          \"exploitation_rate_p\",\n          \"dif_tpr\",\n          \"dif_fpr\",\n          \"ensemble_tpr\",\n          \"ensemble_fpr\"\n        ],\n        \"rows\": [\n          [\n            1.0,\n            0.42,\n            0.14,\n            0.48,\n            0.16\n          ],\n          [\n            0.8,\n            0.33,\n            0.13,\n            0.41,\n            0.15\n          ],\n          [\n            0.6,\n            0.24,\n            0.12,\n            0.38,\n            0.14\n          ],\n          [\n            0.4,\n            0.15,\n            0.11,\n            0.28,\n            0.13\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RL鲁棒性论证在worst档下变成了一个pyrrhic victory：DIF确实比ConStat/Min-K%更稳定， 但稳定在一个接近随机的水平。根本原因是plan_001的IRT misfit传导—— 如果item parameters估计不准（因为模型异质性违反假设），那么DIF统计量本身就是噪声的。 Reasoning-RL模型数量(N=12)不足以做统计推断，这一点在worst档下无法弥补。 Partial exploitation分析的simulation-to-real gap（0.72→0.42 at p=1.0）是关键发现—— 说明real response matrix的噪声结构（非随机缺失、ceiling效应、架构聚类）远比i.i.d. simulation假设的恶劣。 Reframe价值：这个gap本身就是方法论贡献——量化了simulation与现实的差距，为未来work设定了realistic expectations。\\n\\n\\nDIF retention ratio 0.71表面上看\\\"还行\\\"，但置于worst语境下：(1)基线DIF AUROC本身就只有0.62 （因plan_001揭示的IRT misfit和confound问题），所以0.71的retention是在一个已经很弱的基线上， 实际AUROC≈0.55，接近随机。(2)仅12个reasoning-RL模型可用，统计power极低， bootstrap CI宽达[0.48,0.62]，跨过0.5随机线。(3)TOST等价性检验p=0.18>0.05， 无法声称DIF与ConStat\\\"等效\\\"——也无法声称DIF\\\"更好\\\"。DeLong检验p=0.31说明差异不显著， 但这是因为两者都很差而非两者都好。(4)Partial exploitation分析是worst档最具破坏性的发现： 真实response matrix噪声下，即使p=1.0的full exploitation，TPR也只有0.42（远低于simulation的0.72）， p=0.6时降至0.24。Ensemble在p=0.6时也仅0.38。结论：RL鲁棒性名义上成立（DIF不像ConStat 那样急剧下降），但在一个本身就不work的检测器上谈鲁棒性毫无意义。\\n\"\n  },\n  {\n    \"name\": \"constat_perturbation_eval\",\n    \"description\": \"独立评估ConStat式perturbation testing在MMLU上的检测力， 含200+题的语义等价改写、原始vs改写性能比较、FDR控制检测。\\n\",\n    \"results\": {\n      \"constat_auroc_non_rl\": 0.54,\n      \"constat_auroc_sft_only\": 0.62,\n      \"constat_auroc_rl_models\": 0.43,\n      \"constat_fdr_controlled_tpr_alpha_0_05\": 0.28,\n      \"constat_fdr_controlled_tpr_alpha_0_10\": 0.36,\n      \"perturbation_quality_semantic_sim\": 0.87,\n      \"perturbation_quality_human_eval\": 0.79,\n      \"n_items_reformulated\": 220,\n      \"reformulation_difficulty_shift_mean\": 0.35,\n      \"reformulation_difficulty_shift_std\": 0.41,\n      \"constat_detection_by_effect_size_small\": 0.12,\n      \"constat_detection_by_effect_size_medium\": 0.31,\n      \"constat_detection_by_effect_size_large\": 0.52\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 6: ConStat Detection Power by Model Type\",\n        \"columns\": [\n          \"model_type\",\n          \"n_models\",\n          \"auroc\",\n          \"fdr_tpr_0_05\",\n          \"fdr_tpr_0_10\"\n        ],\n        \"rows\": [\n          [\n            \"SFT-only\",\n            85,\n            0.62,\n            0.34,\n            0.42\n          ],\n          [\n            \"Align-RL(DPO/ORPO)\",\n            65,\n            0.51,\n            0.22,\n            0.31\n          ],\n          [\n            \"Reason-RL(GRPO)\",\n            12,\n            0.43,\n            0.15,\n            0.24\n          ],\n          [\n            \"All\",\n            162,\n            0.54,\n            0.28,\n            0.36\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 7: Perturbation Quality Assessment\",\n        \"columns\": [\n          \"metric\",\n          \"mean\",\n          \"std\",\n          \"min\",\n          \"max\"\n        ],\n        \"rows\": [\n          [\n            \"semantic_similarity\",\n            0.87,\n            0.06,\n            0.71,\n            0.97\n          ],\n          [\n            \"difficulty_shift_logit\",\n            0.35,\n            0.41,\n            -0.52,\n            1.83\n          ],\n          [\n            \"distractor_attractiveness_change\",\n            0.22,\n            0.31,\n            -0.18,\n            1.12\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ConStat失败的核心原因是perturbation-difficulty confound：改写不可避免地改变题目难度， 而这与contamination signal混淆。在worst档下这不意外——原ConStat论文在controlled setting 下work，但MMLU的选择题格式放大了perturbation artifact。RL AUROC<0.5说明信号反转， 不是ConStat的fault而是RL训练机制的必然结果。 Reframe价值：这些结果量化了perturbation-based方法的fundamental limitation， 为\\\"为什么需要新方法\\\"提供了实证论据。\\n\\n\\nConStat在non-RL模型上AUROC=0.54，远低于原论文报告水平。原因：(1)perturbation本身引入 非平凡的难度偏移(mean=0.35 logit, std=0.41)——语义等价的改写不是心理测量等价的改写， contamination-free的项也会表现出原始vs改写差异。(2)MMLU的multiple-choice格式使 perturbation空间受限——改写选项措辞几乎不可避免地改变干扰项吸引力。(3)在RL模型上 AUROC=0.43<0.5，说明RL训练导致的output distribution平滑使perturbation sensitivity 方向反转——RL模型对改写更稳定（不是因为不污染，而是因为GRPO clipping压制了敏感性变化）。 FDR控制后TPR仅0.28(α=0.05)，大量真阳性在多重检验校正中被消除。 Worst档结论：ConStat作为standalone检测器在MMLU场景下不可靠。\\n\"\n  },\n  {\n    \"name\": \"dvd_generation_variance_eval\",\n    \"description\": \"独立评估DVD generation variance在MMLU上的检测力， 含10-15个开源模型、每题50次temperature采样、方差分析。\\n\",\n    \"results\": {\n      \"dvd_variant_detection_tpr\": 0.23,\n      \"dvd_verbatim_detection_tpr\": 0.31,\n      \"dvd_fpr\": 0.14,\n      \"dvd_auroc_overall\": 0.58,\n      \"n_models_evaluated\": 13,\n      \"n_items_evaluated\": 500,\n      \"generation_variance_contaminated_mean\": 0.34,\n      \"generation_variance_clean_mean\": 0.29,\n      \"generation_variance_overlap_coefficient\": 0.72,\n      \"bimodal_detection_rate_contaminated\": 0.18,\n      \"bimodal_detection_rate_clean\": 0.11,\n      \"gpu_hours_used\": 62\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 8: DVD Detection Power\",\n        \"columns\": [\n          \"contamination_type\",\n          \"tpr\",\n          \"fpr\",\n          \"auroc\",\n          \"n_items\"\n        ],\n        \"rows\": [\n          [\n            \"verbatim\",\n            0.31,\n            0.14,\n            0.62,\n            150\n          ],\n          [\n            \"variant\",\n            0.23,\n            0.14,\n            0.56,\n            150\n          ],\n          [\n            \"overall\",\n            0.27,\n            0.14,\n            0.58,\n            300\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 9: Generation Variance Distribution\",\n        \"columns\": [\n          \"item_status\",\n          \"variance_mean\",\n          \"variance_std\",\n          \"bimodal_rate\"\n        ],\n        \"rows\": [\n          [\n            \"contaminated\",\n            0.34,\n            0.18,\n            0.18\n          ],\n          [\n            \"clean\",\n            0.29,\n            0.16,\n            0.11\n          ],\n          [\n            \"effect_size_d\",\n            0.3,\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DVD在MCQ场景下的failure是structural的——output space太小，variance信号被compressed。 Effect size d=0.30属于small effect，在N=13模型×500题的规模下不足以支撑检测。 Reframe价值：这是MCQ format的fundamental limitation的实证证明， 推动社区思考format-aware的检测方法设计。\\n\\n\\nDVD在worst档下表现差，原因：(1)MMLU是选择题——模型输出方差本身就很低（输出空间只有A/B/C/D）， generation variance的区分力受限于这个compressed output space。(2)Contaminated vs clean项 的方差分布高度重叠(overlap=0.72)——污染项不一定方差低（模型可能memorize了错误答案pattern）， clean项不一定方差高（能力足够的模型在easy项上也方差低）。(3)Bimodal detection在两类项上 差异不大(0.18 vs 0.11)，信噪比不足。(4)Multiple-choice格式下temperature采样的多样性 被logit差异主导而非memorization——高confidence的非污染回答也呈现低方差。 DVD更适合open-ended generation场景，在MCQ上fundamental limitation明显。\\n\"\n  },\n  {\n    \"name\": \"ensemble_fusion\",\n    \"description\": \"将DIF+ConStat+DVD融合为多信号集成，含阈值校准、投票策略、覆盖分析。\\n\",\n    \"results\": {\n      \"ensemble_tpr_delta_ge_0_8\": 0.38,\n      \"ensemble_tpr_delta_ge_1_4\": 0.48,\n      \"ensemble_fpr\": 0.16,\n      \"majority_vote_tpr\": 0.32,\n      \"majority_vote_fpr\": 0.11,\n      \"weighted_fusion_tpr\": 0.43,\n      \"weighted_fusion_fpr\": 0.16,\n      \"uniform_weight_tpr\": 0.39,\n      \"uniform_weight_fpr\": 0.14,\n      \"cross_val_weight_stability_cv\": 0.35,\n      \"dif_unique_contribution\": 0.08,\n      \"constat_unique_contribution\": 0.11,\n      \"dvd_unique_contribution\": 0.05,\n      \"signal_correlation_dif_constat\": 0.22,\n      \"signal_correlation_dif_dvd\": 0.14,\n      \"signal_correlation_constat_dvd\": 0.18\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 10: Ensemble Fusion Strategy Comparison\",\n        \"columns\": [\n          \"strategy\",\n          \"tpr_delta_ge_0_8\",\n          \"tpr_delta_ge_1_4\",\n          \"fpr\",\n          \"f1\"\n        ],\n        \"rows\": [\n          [\n            \"DIF_only\",\n            0.28,\n            0.42,\n            0.14,\n            0.33\n          ],\n          [\n            \"ConStat_only\",\n            0.31,\n            0.36,\n            0.12,\n            0.34\n          ],\n          [\n            \"DVD_only\",\n            0.2,\n            0.27,\n            0.14,\n            0.24\n          ],\n          [\n            \"majority_2of3\",\n            0.32,\n            0.4,\n            0.11,\n            0.37\n          ],\n          [\n            \"weighted_fusion\",\n            0.43,\n            0.48,\n            0.16,\n            0.4\n          ],\n          [\n            \"uniform_weight\",\n            0.39,\n            0.45,\n            0.14,\n            0.39\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 11: Signal Correlation Matrix\",\n        \"columns\": [\n          \"signal_pair\",\n          \"pearson_r\",\n          \"overlap_flags\"\n        ],\n        \"rows\": [\n          [\n            \"DIF-ConStat\",\n            0.22,\n            0.28\n          ],\n          [\n            \"DIF-DVD\",\n            0.14,\n            0.19\n          ],\n          [\n            \"ConStat-DVD\",\n            0.18,\n            0.23\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ensemble未能rescue单信号的weakness。\\\"互补覆盖\\\"的叙事在worst档下不成立—— 三个信号各自太弱，合并后仍太弱。但信号独立性分析(低相关)有方法论价值： 它说明DIF/ConStat/DVD确实capture不同的contamination facets， 只是每个facet上的power都不足。 Reframe：ensemble框架作为evaluation protocol有贡献——未来更强的单信号检测器 可以插入这个框架获得覆盖分析。\\n\\n\\n三个弱检测器的ensemble不会产生强检测器——这是worst档的核心推论。 (1)每个信号AUROC都在0.54-0.62范围，信号间相关性低(0.14-0.22)看似有利于ensemble， 但低相关性在这里反映的是\\\"各自捕获不同的噪声\\\"而非\\\"各自捕获不同的信号\\\"。 (2)Weighted fusion优于majority vote(0.43 vs 0.32 TPR)，但FPR也更高(0.16 vs 0.11)。 Cross-validation显示权重不稳定(CV=0.35)，说明过拟合风险高。 (3)Ensemble TPR@δ≥1.4仅0.48——即使是大效应也有超过一半漏检。FPR=0.16意味着 每6个flag中有1个是误报，在12,508题的MMLU上产生~2000个false alarm。 (4)各信号unique contribution很小(5-11%)，说明重叠区域不是\\\"强化\\\"而是\\\"共同噪声\\\"。\\n\"\n  },\n  {\n    \"name\": \"cross_benchmark_gsm8k\",\n    \"description\": \"在GSM8K上复制DIF分析，用GSM1K作为独立ground truth。 收集50+模型的per-item response，做temporal cohort DIF， 将DIF flag与per-model GSM8K-GSM1K accuracy gap关联。\\n\",\n    \"results\": {\n      \"gsm8k_dif_flag_rate\": 0.11,\n      \"gsm8k_gsm1k_gap_mean\": 0.062,\n      \"gsm8k_gsm1k_gap_std\": 0.078,\n      \"gsm8k_dif_gap_correlation_r\": 0.14,\n      \"gsm8k_dif_gap_correlation_p\": 0.32,\n      \"gsm8k_irt_rmsea\": 0.1,\n      \"n_models_collected\": 58,\n      \"n_gsm8k_items\": 1319,\n      \"dif_tpr_against_gsm1k_proxy\": 0.22,\n      \"dif_fpr_against_gsm1k_proxy\": 0.09\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 12: GSM8K Cross-Validation Results\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"ci_95_lower\",\n          \"ci_95_upper\"\n        ],\n        \"rows\": [\n          [\n            \"dif_gap_correlation_r\",\n            0.14,\n            -0.12,\n            0.38\n          ],\n          [\n            \"dif_tpr_vs_gsm1k\",\n            0.22,\n            0.1,\n            0.36\n          ],\n          [\n            \"dif_fpr_vs_gsm1k\",\n            0.09,\n            0.04,\n            0.16\n          ],\n          [\n            \"irt_rmsea\",\n            0.1,\n            0.08,\n            0.12\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"GSM8K验证失败彻底——r=0.14的95% CI包含零，无统计显著性。 这削弱了DIF作为跨benchmark通用检测器的claim。但分析揭示了一个有用的insight： model-level gap与item-level DIF的granularity mismatch是根本问题， 未来验证需要item-level ground truth（指向plan_011 semi-synthetic方法的必要性）。\\n\\n\\nGSM8K交叉验证产出极弱相关(r=0.14, p=0.32)，原因：(1)GSM8K→GSM1K accuracy gap 是model-level指标，DIF flag是item-level指标，两者度量不同granularity的contamination， 对齐需要强假设（污染是均匀的across items）。(2)GSM8K的math reasoning性质使能力增长 与contamination更难分离——新模型genuinely更擅长数学，gap可能反映的是eval methodology差异 而非contamination。(3)GSM8K仅1,319题，N=58模型，统计power不足。(4)IRT fit在GSM8K上 好于MMLU(RMSEA=0.10)因为数学题更unidimensional，但仍在边界区间。 DIF在GSM1K proxy ground truth上的TPR=0.22极低，说明DIF flag与已知ground truth不对齐。\\n\"\n  },\n  {\n    \"name\": \"bifactor_irt_equating_pilot\",\n    \"description\": \"在METABENCH MMLU上拟合bifactor IRT模型（通用因子+学科因子）， 选锚题，做固定参数校准，验证等值分数等效性。\\n\",\n    \"results\": {\n      \"bifactor_convergence\": false,\n      \"bifactor_convergence_subset_n_subjects\": 8,\n      \"bifactor_rmsea_subset\": 0.09,\n      \"bifactor_general_factor_variance_explained\": 0.38,\n      \"bifactor_subject_factor_variance_explained\": 0.31,\n      \"bifactor_residual_variance\": 0.31,\n      \"anchor_item_count\": 145,\n      \"anchor_item_stability_criterion_met_rate\": 0.12,\n      \"equated_score_spearman_rho\": 0.84,\n      \"equated_vs_original_rank_displacement_mean\": 23,\n      \"equated_vs_original_rank_displacement_max\": 312,\n      \"fixed_param_calibration_convergence_rate\": 0.71\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 13: Bifactor Model Fit\",\n        \"columns\": [\n          \"scope\",\n          \"convergence\",\n          \"rmsea\",\n          \"gen_var\",\n          \"subj_var\",\n          \"resid_var\"\n        ],\n        \"rows\": [\n          [\n            \"full_57_subjects\",\n            false,\n            \"—\",\n            \"—\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"subset_8_subjects\",\n            true,\n            0.09,\n            0.38,\n            0.31,\n            0.31\n          ],\n          [\n            \"subset_4_stem\",\n            true,\n            0.07,\n            0.44,\n            0.28,\n            0.28\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 14: Equating Quality\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"target\",\n          \"met\"\n        ],\n        \"rows\": [\n          [\n            \"anchor_items\",\n            145,\n            \">500\",\n            false\n          ],\n          [\n            \"anchor_stability_rate\",\n            0.12,\n            \">0.80\",\n            false\n          ],\n          [\n            \"spearman_rho\",\n            0.84,\n            \">0.95\",\n            false\n          ],\n          [\n            \"rank_displacement_mean\",\n            23,\n            \"<5\",\n            false\n          ],\n          [\n            \"fixed_param_convergence\",\n            0.71,\n            \">0.90\",\n            false\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bifactor不收敛直接否定Claim 3。子集上的勉强收敛不足以支撑full-scale regeneration。 核心问题是LLM能力的multidimensionality——38%通用因子方差说明超过60%的variance是 domain-specific或residual的，单一等值框架不适用。 但这个负面结果本身有价值：它是首个大规模实证证据说明bifactor IRT在LLM评估中的失效模式。 Reframe：砍掉Claim 3，或将其降格为\\\"在homogeneous subdomain内可行的局部等值\\\"。\\n\\n\\nBifactor模型在完整57学科上不收敛——这是worst档的defining prediction。原因： (1)12,508题×5,219模型的response matrix过于稀疏（many models没做完全部MMLU）， bifactor需要估计的参数量(2×12508 + 57个学科因子loading)远超有效sample size。 (2)学科因子间不正交——STEM学科高度相关，humanities学科高度相关，违反bifactor的 近似正交假设。(3)通用因子仅解释38%方差——LLM能力高度multidimensional， 单一g-factor模型不适用。退而求其次在8个大学科子集上可以收敛(RMSEA=0.09)， 但这意味着跨学科等值不可行。锚题仅145个（<1.2%的题），稳定性达标率仅12%—— 大多数\\\"稳定\\\"题在不同cohort下参数也在漂移，因为IRT参数估计本身就不稳定。 Spearman ρ=0.84看似可接受但低于0.95目标，且mean rank displacement=23意味着 约5%的模型排名变动超过1个百分位——对leaderboard而言不可接受。\\n\"\n  },\n  {\n    \"name\": \"item_generation_calibration\",\n    \"description\": \"为DIF-flagged MMLU题生成替代项，用student simulation校准难度， 比较prompt-based vs empirical calibration。\\n\",\n    \"results\": {\n      \"n_items_generated\": 300,\n      \"prompt_difficulty_correlation_rho\": 0.21,\n      \"student_sim_difficulty_correlation_rho\": 0.58,\n      \"student_sim_discrimination_correlation_rho\": 0.41,\n      \"construct_validity_factor_loading_mean\": 0.52,\n      \"construct_validity_factor_loading_target\": 0.7,\n      \"replacement_item_acceptance_rate\": 0.34,\n      \"difficulty_rmse_vs_original\": 1.12,\n      \"discrimination_rmse_vs_original\": 0.48\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 15: Item Generation Calibration Quality\",\n        \"columns\": [\n          \"calibration_method\",\n          \"difficulty_rho\",\n          \"discrimination_rho\",\n          \"construct_loading\"\n        ],\n        \"rows\": [\n          [\n            \"prompt_based\",\n            0.21,\n            0.14,\n            0.48\n          ],\n          [\n            \"student_simulation\",\n            0.58,\n            0.41,\n            0.52\n          ],\n          [\n            \"target\",\n            \">0.75\",\n            \">0.60\",\n            \">0.70\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Item generation在worst档下quality insufficient for regeneration。 Student simulation的partial success (ρ=0.58)相比prompt-based (ρ=0.21)是有意义的improvement， 但距离psychometrically equivalent replacement还有大gap。 Reframe：student simulation方法论贡献仍在，但regeneration pipeline需要更多研发。\\n\\n\\nPrompt-based difficulty targeting一如文献预期地差(ρ=0.21)。Student simulation 改善显著(ρ=0.58)但仍低于文献报告的0.75-0.82——因为MMLU的多学科异质性使得 单一student simulation模型难以同时校准STEM和humanities。 Construct validity是biggest failure：生成项的平均factor loading=0.52 vs 目标0.70， 说明LLM生成的替代题虽然表面上在同一学科、同一认知水平，但测量的实际construct有偏移。 仅34%的生成项满足acceptance criteria（难度、区分度、factor loading全部达标）， 意味着要替换100个flagged题需要生成~300个candidate——成本和质量控制问题突出。\\n\"\n  },\n  {\n    \"name\": \"cumulative_bayesian_dif\",\n    \"description\": \"实现累积Bayesian DIF prior (Sinharay et al., 2006)， 模拟4次连续benchmark administration，展示累积power改善。\\n\",\n    \"results\": {\n      \"single_admin_power_medium_delta_1_0\": 0.22,\n      \"cumulative_2_admin_power\": 0.31,\n      \"cumulative_3_admin_power\": 0.39,\n      \"cumulative_4_admin_power\": 0.45,\n      \"simulation_single_admin_power\": 0.4,\n      \"power_improvement_factor_4_admin\": 2.05,\n      \"bayes_factor_threshold_sensitivity\": \"BF>3 at 4th admin for 45% of truly contaminated items\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 16: Cumulative Bayesian DIF Power\",\n        \"columns\": [\n          \"n_administrations\",\n          \"power_real\",\n          \"power_simulation\",\n          \"ratio\"\n        ],\n        \"rows\": [\n          [\n            1,\n            0.22,\n            0.4,\n            0.55\n          ],\n          [\n            2,\n            0.31,\n            0.54,\n            0.57\n          ],\n          [\n            3,\n            0.39,\n            0.64,\n            0.61\n          ],\n          [\n            4,\n            0.45,\n            0.7,\n            0.64\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bayesian accumulation帮助但不足以rescue。Simulation-to-real gap从0.55扩大到0.64 说明累积过程在amplify real data的systematic bias。方法论仍有价值但需要加入 item parameter drift correction。\\n\\n\\n起点power=0.22（非simulation的0.40）——因为base DIF检测power在real data上已经degraded （plan_001的发现传导到这里）。累积后达到0.45——2x improvement看似decent，但绝对水平 仍不足以做可靠检测。原因：Bayesian prior accumulation假设item parameters在administrations 间是stable的，但LLM evaluation的\\\"administrations\\\"是不同时期的模型群体， item parameters本身可能在drift（因为新模型能力profile不同）。Prior可能在accumulate 过时信息而非strengthen信号。\\n\"\n  },\n  {\n    \"name\": \"graceful_degradation_analysis\",\n    \"description\": \"分析benchmark在不同替换率下的validity退化：排名稳定性、分数信度、construct覆盖。\\n\",\n    \"results\": {\n      \"ranking_stability_5pct_replace\": 0.96,\n      \"ranking_stability_10pct_replace\": 0.91,\n      \"ranking_stability_20pct_replace\": 0.82,\n      \"ranking_stability_50pct_replace\": 0.63,\n      \"score_reliability_5pct\": 0.94,\n      \"score_reliability_10pct\": 0.89,\n      \"score_reliability_20pct\": 0.78,\n      \"score_reliability_50pct\": 0.55,\n      \"construct_coverage_20pct\": 0.85,\n      \"construct_coverage_50pct\": 0.61,\n      \"acceptable_replacement_threshold\": \"5-10%\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 17: Graceful Degradation Curves\",\n        \"columns\": [\n          \"replace_rate\",\n          \"rank_stability\",\n          \"score_reliability\",\n          \"construct_coverage\"\n        ],\n        \"rows\": [\n          [\n            0.05,\n            0.96,\n            0.94,\n            0.97\n          ],\n          [\n            0.1,\n            0.91,\n            0.89,\n            0.93\n          ],\n          [\n            0.2,\n            0.82,\n            0.78,\n            0.85\n          ],\n          [\n            0.5,\n            0.63,\n            0.55,\n            0.61\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Degradation analysis在worst档下更像一个cautionary tale：它量化了low-quality replacement 的代价，为\\\"为什么item generation需要更好的calibration\\\"提供实证。 独立贡献是degradation framework本身——可用于任何benchmark regeneration方案的evaluation。\\n\\n\\n在worst档下，替换项质量低(plan_006的factor loading=0.52)导致退化速度快于理论预期。 10%替换时ranking stability=0.91，低于通常acceptable的0.95——因为替换项不仅改变难度 还改变construct coverage。20%替换时信度降至0.78，50%时本质上是一个不同的test。 可接受阈值仅5-10%，意味着如果DIF flags 15%的题为contaminated， 即使全部替换也只有勉强够用。但如果contamination更广泛，regeneration不可行。\\n\"\n  },\n  {\n    \"name\": \"item_focused_trees\",\n    \"description\": \"实现Item-Focused Trees (Tutz & Berger, 2016)作为categorical cohort DIF的替代， 将模型release date作为连续协变量。\\n\",\n    \"results\": {\n      \"ift_auroc\": 0.57,\n      \"ift_vs_categorical_dif_flag_overlap\": 0.48,\n      \"ift_tpr_delta_ge_1_4\": 0.39,\n      \"ift_fpr\": 0.12,\n      \"ift_rmsea_improvement\": 0.01,\n      \"ift_tree_depth_mean\": 2.3,\n      \"ift_overfitting_cv_gap\": 0.09\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 18: IFT vs Categorical DIF Comparison\",\n        \"columns\": [\n          \"method\",\n          \"auroc\",\n          \"tpr_delta_ge_1_4\",\n          \"fpr\",\n          \"flag_count\"\n        ],\n        \"rows\": [\n          [\n            \"categorical_temporal\",\n            0.55,\n            0.42,\n            0.14,\n            1850\n          ],\n          [\n            \"categorical_quintile\",\n            0.53,\n            0.38,\n            0.16,\n            2300\n          ],\n          [\n            \"item_focused_tree\",\n            0.57,\n            0.39,\n            0.12,\n            1620\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"IFT不能rescue DIF——问题在上游(IRT假设违反)，不在cohort定义。 但IFT vs categorical的disagreement是有用的diagnostic： 它量化了DIF结果对分析选择的敏感性，支撑\\\"DIF不适合做检测器\\\"的conclusion。\\n\\n\\nIFT避免了arbitrary cohort划分，理论上更flexible。但worst档下： (1)AUROC=0.57仅marginal improvement over categorical DIF(~0.55)——因为底层IRT misfit 不是cohort定义的问题，而是模型异质性的问题，IFT不能修复这个。 (2)与categorical DIF的flag overlap仅0.48——两种方法不同意一半的flag， 说明DIF结果fundamentally unstable，不取决于\\\"真正的contamination\\\"而取决于方法选择。 (3)Overfitting gap=0.09说明tree在capture noise而非signal。\\n\"\n  },\n  {\n    \"name\": \"architecture_stratified_dif\",\n    \"description\": \"在decoder-only同质子群体上运行DIF，测试IRT拟合是否改善、spurious DIF是否减少。\\n\",\n    \"results\": {\n      \"decoder_only_n_models\": 3420,\n      \"decoder_only_rmsea\": 0.1,\n      \"decoder_only_cfi\": 0.82,\n      \"decoder_only_tli\": 0.79,\n      \"full_pop_rmsea_ref\": 0.14,\n      \"rmsea_improvement\": 0.04,\n      \"dif_flag_rate_decoder_only\": 0.12,\n      \"dif_flag_rate_full_pop_ref\": 0.148,\n      \"fpr_decoder_only\": 0.11,\n      \"fpr_full_pop_ref\": 0.14,\n      \"tpr_decoder_only_delta_ge_1_4\": 0.45,\n      \"within_family_confound_overlap_decoder_only\": 0.55,\n      \"moe_vs_dense_subanalysis_rmsea_dense\": 0.08,\n      \"moe_vs_dense_subanalysis_rmsea_moe\": 0.12\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 19: Architecture Stratification Effect\",\n        \"columns\": [\n          \"population\",\n          \"n_models\",\n          \"rmsea\",\n          \"cfi\",\n          \"dif_flag_rate\",\n          \"fpr\",\n          \"within_fam_overlap\"\n        ],\n        \"rows\": [\n          [\n            \"full_population\",\n            5219,\n            0.14,\n            0.72,\n            0.148,\n            0.14,\n            0.62\n          ],\n          [\n            \"decoder_only\",\n            3420,\n            0.1,\n            0.82,\n            0.12,\n            0.11,\n            0.55\n          ],\n          [\n            \"decoder_dense_only\",\n            1850,\n            0.08,\n            0.88,\n            0.098,\n            0.08,\n            0.47\n          ],\n          [\n            \"decoder_moe_only\",\n            380,\n            0.12,\n            0.78,\n            0.135,\n            0.13,\n            0.58\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 20: Fit Diagnostic Breakdown\",\n        \"columns\": [\n          \"subgroup\",\n          \"rmsea\",\n          \"n\",\n          \"effective_power_at_d_1_4\"\n        ],\n        \"rows\": [\n          [\n            \"all_decoder\",\n            0.1,\n            3420,\n            0.45\n          ],\n          [\n            \"dense_small_1B_7B\",\n            0.07,\n            1200,\n            0.38\n          ],\n          [\n            \"dense_large_13B_70B\",\n            0.09,\n            650,\n            0.42\n          ],\n          [\n            \"moe_all\",\n            0.12,\n            380,\n            0.3\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Plan_010是worst档最有价值的实验——它精确量化了IRT misfit的来源和修复成本。 结论：\\\"DIF要work需要architecture-homogeneous populations\\\"是一个actionable finding， 但代价是严重的power loss。这直接支撑reframe angle (1)—— \\\"为什么经典心理测量不能直接用于LLM\\\"的诊断性贡献。 Dense-only RMSEA=0.08是一个hope signal，但N=1850+within-family overlap=0.47 说明即使在最favorable condition下confounding仍是dominant problem。\\n\\n\\nArchitecture stratification帮助但不够——这是worst档的关键特征。 RMSEA从0.14降到0.10：improvement是real的(Δ=0.04)但0.10仍在borderline-to-poor区间 (acceptable threshold是0.08)。原因：decoder-only内部仍有substantial heterogeneity—— MoE vs dense, 不同parameter scales (1B-70B), 不同tokenizer, 不同training data。 去除architecture heterogeneity是necessary but not sufficient。 DIF flag rate降低(0.12 vs 0.148)和FPR降低(0.11 vs 0.14)说明部分spurious DIF 确实来自architecture差异，但幅度有限。Within-family confound overlap从0.62降到0.55—— 仍然>50%的flag是confounded。Dense-only进一步分析(RMSEA=0.08)暗示如果进一步 subset到完全homogeneous群体，fit会acceptable——但代价是N大幅缩小，power更低。\\n\"\n  },\n  {\n    \"name\": \"semi_synthetic_contamination_validation\",\n    \"description\": \"在真实METABENCH response matrix中注入已知contamination， 测量DIF检测power under controlled ground truth。\\n\",\n    \"results\": {\n      \"semi_synthetic_tpr_delta_ge_1_4\": 0.41,\n      \"semi_synthetic_tpr_delta_ge_1_0\": 0.28,\n      \"semi_synthetic_tpr_delta_ge_0_6\": 0.15,\n      \"semi_synthetic_fpr\": 0.14,\n      \"prevalence_5pct_tpr\": 0.48,\n      \"prevalence_15pct_tpr\": 0.39,\n      \"prevalence_30pct_tpr\": 0.33,\n      \"exploit_rate_1_0_tpr\": 0.41,\n      \"exploit_rate_0_8_tpr\": 0.33,\n      \"exploit_rate_0_6_tpr\": 0.24,\n      \"exploit_rate_0_4_tpr\": 0.14,\n      \"focal_n_40_tpr\": 0.29,\n      \"focal_n_100_tpr\": 0.41,\n      \"focal_n_200_tpr\": 0.47,\n      \"simulation_vs_semi_synthetic_gap_tpr\": 0.31,\n      \"simulation_tpr_reference_delta_1_4\": 0.72\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 21: Semi-Synthetic Detection Power Matrix\",\n        \"columns\": [\n          \"delta\",\n          \"prevalence\",\n          \"exploit_rate\",\n          \"tpr\",\n          \"fpr\",\n          \"auroc\"\n        ],\n        \"rows\": [\n          [\n            1.4,\n            0.15,\n            1.0,\n            0.41,\n            0.14,\n            0.68\n          ],\n          [\n            1.4,\n            0.15,\n            0.6,\n            0.24,\n            0.13,\n            0.59\n          ],\n          [\n            1.0,\n            0.15,\n            1.0,\n            0.28,\n            0.14,\n            0.6\n          ],\n          [\n            1.0,\n            0.15,\n            0.6,\n            0.17,\n            0.13,\n            0.54\n          ],\n          [\n            0.6,\n            0.15,\n            1.0,\n            0.15,\n            0.14,\n            0.52\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 22: Simulation vs Semi-Synthetic Gap\",\n        \"columns\": [\n          \"condition\",\n          \"sim_tpr\",\n          \"semi_syn_tpr\",\n          \"gap\",\n          \"gap_pct\"\n        ],\n        \"rows\": [\n          [\n            \"N100_d1.4_p1.0\",\n            0.72,\n            0.41,\n            0.31,\n            \"43%\"\n          ],\n          [\n            \"N100_d1.0_p1.0\",\n            0.52,\n            0.28,\n            0.24,\n            \"46%\"\n          ],\n          [\n            \"N80_d1.4_p1.0\",\n            0.68,\n            0.38,\n            0.3,\n            \"44%\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 23: Focal Group Size Effect\",\n        \"columns\": [\n          \"focal_n\",\n          \"tpr_d1_4\",\n          \"fpr\",\n          \"power_gain_per_10_models\"\n        ],\n        \"rows\": [\n          [\n            40,\n            0.29,\n            0.15,\n            \"—\"\n          ],\n          [\n            60,\n            0.34,\n            0.14,\n            0.025\n          ],\n          [\n            80,\n            0.38,\n            0.14,\n            0.02\n          ],\n          [\n            100,\n            0.41,\n            0.14,\n            0.015\n          ],\n          [\n            200,\n            0.47,\n            0.13,\n            0.006\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Plan_011是worst档的cornerstone experiment。它做了三件事： (1)Definitively证明simulation结果不能translate to real data（~40% gap），为社区设定realistic expectations。 (2)量化了real response matrix的noise sources——missing pattern, ceiling/floor, architecture clustering—— 这些是任何基于IRT的检测方法都会面对的，不仅限于DIF。 (3)Semi-synthetic框架本身是方法论贡献——它是MMLU-CF(κ=0.14)和GSM1K的superior alternative， 因为它提供item-level controlled ground truth。 即使DIF作为检测器fails，semi-synthetic validation framework对评估未来任何检测器都有价值。 这直接支撑reframe angle (3)。 关键insight：仅δ≥2.0的极大效应可检测(TPR>0.5)——对应~20pp accuracy inflation， 即只有最严重的contamination能被任何方法可靠检测。\\n\\nSemi-synthetic验证是worst档的smoking gun。TPR@δ≥1.4=0.41，远低于pure simulation的0.72。 Gap=0.31(0.72-0.41)量化了simulation与现实的差距。原因清晰： (1)真实response matrix有non-random missing pattern——不是所有模型都做了全部题， missingness与model capability相关，biases IRT parameter estimation。 (2)Ceiling/floor效应——easy题上所有模型都对，hard题上所有模型都错， 这些题的DIF无法检测（因为没有ability-conditional variation）。 (3)Architecture clustering——同family模型response pattern高度相关， violate DIF的independent observations假设。 (4)Injection本身可能\\\"太干净\\\"——real contamination不是uniform probability flip， 而是pattern-dependent（模型倾向于memorize特定类型的题）， 但这个bias direction使semi-synthetic结果成为optimistic estimate。 Prevalence依赖反直觉(5%>15%>30%)——因为高prevalence时injected signal淹没在 baseline noise中，DIF的focal-reference contrast被稀释。 FPR=0.14>>0.05目标，因为real matrix中的existing contamination （我们不知道的ground truth）产生false positive contamination。\\n\"\n  }\n]",
      "numLines": 1155,
      "startLine": 1,
      "totalLines": 1155
    }
  },
  "sourceToolAssistantUUID": "810741e1-e9f5-4eff-a3a6-f35970140db8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T21:21:39.540Z_

<details><summary>↩ Tool result · `toolu_01SjS46YY7BdnVaZL2G9goWK`</summary>

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
22	**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. A nuance: partial exploitation (model memorizes but answers correctly only p<1 of the time) shrinks DIF effect size proportionally — we formally characterize detection power as a function of exploitation rate. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates a psychometric monitoring and regeneration framework — applying mature, validated psychometric tools to solve an urgent ML evaluation problem.
23	
24	**Headline result template**: "On MMLU with 5,000+ models spanning a capability range from near-random (46% accuracy) to near-saturation (60%), DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026). Leveraging the unprecedented scale of METABENCH (5,219 models), we conduct the largest DIF analysis in LLM evaluation literature."
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
57	7. **"DIF flags may reflect capability improvement, not contamination"**
58	   - Response: Post-2024 models are both more capable and more contaminated. We control for this via (a) within-family DIF analysis (same architecture at different training stages, e.g., Llama-2→3→3.1), where capability trajectory is known, isolating contamination-specific DIF; (b) domain-specificity analysis of DIF flags vs known capability trajectories; (c) bifactor model's subject-specific factors as covariates to absorb domain-specific capability gains.
59	   - Evidence needed: plan_001 (within-family sub-analysis), plan_005 (bifactor covariates)
60	
61	8. **"Ground truth is too noisy to validate DIF — MMLU-CF κ=0.14 is near-random"**
62	   - Response: (a) We supplement MMLU-CF with semi-synthetic validation: inject known contamination signals into the real METABENCH response matrix and measure DIF detection power under controlled conditions. (b) GSM8K/GSM1K provides independent cross-benchmark ground truth. (c) We explicitly characterize MMLU-CF's own reliability limitations before using it as validation.
63	   - Evidence needed: plan_011 (semi-synthetic validation), plan_004 (GSM8K cross-validation)
64	
65	9. **"Partial exploitation defeats DIF — RL models may only exploit p<1 of memorized items"**
66	   - Response: Formal power analysis as function of exploitation rate p shows: at p=1.0 DIF detects with TPR=0.72-0.85; at p=0.6 effect size shrinks ~0.6×, falling to medium range where ensemble's ConStat signal provides coverage. DIF + ensemble jointly cover p≥0.4. Below p=0.4, contamination impact on rankings is minimal.
67	   - Evidence needed: plan_002 (partial exploitation analysis)
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8869c2de-0e9c-4905-b8a9-b9b305f3ee9d",
  "isSidechain": false,
  "promptId": "7a9370c0-2bc7-4d59-8649-7bea7feea208",
  "type": "user",
  "uuid": "8080e6a7-8c4c-4d63-a23c-f8227709fac4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/paper_framing.md",
      "content": "# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)\n- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)\n- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)\n\n## Core Claims (3 条, 可证伪)\n\n**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.\n\n**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.\n\n**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.\n\n**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\n\n**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. A nuance: partial exploitation (model memorizes but answers correctly only p<1 of the time) shrinks DIF effect size proportionally — we formally characterize detection power as a function of exploitation rate. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates a psychometric monitoring and regeneration framework — applying mature, validated psychometric tools to solve an urgent ML evaluation problem.\n\n**Headline result template**: \"On MMLU with 5,000+ models spanning a capability range from near-random (46% accuracy) to near-saturation (60%), DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026). Leveraging the unprecedented scale of METABENCH (5,219 models), we conduct the largest DIF analysis in LLM evaluation literature.\"\n\n## Venue Fit Risks\n\n- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ \"fairness testing for items\").\n- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: \"examinees\" → \"models\", \"test items\" → \"benchmark questions\", \"DIF\" → \"item-level contamination signal\", \"equating\" → \"score comparability across benchmark versions\".\n- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as \"bringing mature psychometric tools to solve an urgent ML problem\" rather than \"inventing new statistics.\"\n\n## Anticipated Reviewer Concerns\n\n1. **\"DIF power is only sufficient for large effects (δ≥1.4)\"**\n   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.\n   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)\n\n2. **\"Model cohort sample sizes are too small for classical DIF\"**\n   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.\n   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)\n\n3. **\"Only validated in simulation\"**\n   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.\n   - Evidence needed: plan_001, plan_004\n\n4. **\"Item regeneration quality — how do you ensure replacements measure the same construct?\"**\n   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.\n   - Evidence needed: plan_005, plan_006\n\n5. **\"RL robustness is only theoretical — where's the empirical evidence?\"**\n   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.\n   - Evidence needed: plan_002\n\n6. **\"Computational cost of the full pipeline\"**\n   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.\n\n7. **\"DIF flags may reflect capability improvement, not contamination\"**\n   - Response: Post-2024 models are both more capable and more contaminated. We control for this via (a) within-family DIF analysis (same architecture at different training stages, e.g., Llama-2→3→3.1), where capability trajectory is known, isolating contamination-specific DIF; (b) domain-specificity analysis of DIF flags vs known capability trajectories; (c) bifactor model's subject-specific factors as covariates to absorb domain-specific capability gains.\n   - Evidence needed: plan_001 (within-family sub-analysis), plan_005 (bifactor covariates)\n\n8. **\"Ground truth is too noisy to validate DIF — MMLU-CF κ=0.14 is near-random\"**\n   - Response: (a) We supplement MMLU-CF with semi-synthetic validation: inject known contamination signals into the real METABENCH response matrix and measure DIF detection power under controlled conditions. (b) GSM8K/GSM1K provides independent cross-benchmark ground truth. (c) We explicitly characterize MMLU-CF's own reliability limitations before using it as validation.\n   - Evidence needed: plan_011 (semi-synthetic validation), plan_004 (GSM8K cross-validation)\n\n9. **\"Partial exploitation defeats DIF — RL models may only exploit p<1 of memorized items\"**\n   - Response: Formal power analysis as function of exploitation rate p shows: at p=1.0 DIF detects with TPR=0.72-0.85; at p=0.6 effect size shrinks ~0.6×, falling to medium range where ensemble's ConStat signal provides coverage. DIF + ensemble jointly cover p≥0.4. Below p=0.4, contamination impact on rankings is minimal.\n   - Evidence needed: plan_002 (partial exploitation analysis)\n",
      "numLines": 68,
      "startLine": 1,
      "totalLines": 68
    }
  },
  "sourceToolAssistantUUID": "8869c2de-0e9c-4905-b8a9-b9b305f3ee9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T21:21:39.534Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SjS46YY7BdnVaZL2G9goWK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "930269c4-8f63-4ddd-92ec-903aee23453d",
  "isSidechain": false,
  "requestId": "req_011CbEXDkbxiBfuMyP82UfZ3",
  "type": "assistant",
  "uuid": "8869c2de-0e9c-4905-b8a9-b9b305f3ee9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgKrJUzrDVv7Xat3ybEvxZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11564,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11564,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11564
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T205007 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "8080e6a7-8c4c-4d63-a23c-f8227709fac4",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream_20260520T205007",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731"
}
```

---

### Assistant

_source line 14 · 2026-05-20T21:21:59.552Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of both the experiment data and the paper framing. Let me also read the paper-writing-norms skill to ensure quality, and then write the full LaTeX paper.

Let me synthesize the key points from the narrative guidance and experiment data:

1. The core detection claim doesn't hold - IRT unidimensionality assumption is severely violated (RMSEA>0.12), architecture stratification only partially helps (RMSEA~0.10)
2. DIF flags are highly confounded with ability growth - within-family analysis shows >60% of flags appear within families with no differential contamination


3. Semi-synthetic validation reveals detection power far below simulation expectations (TPR~0.40 at δ≥1.4)
4. The paper should reframe: abandon "DIF is a contamination detector" narrative, shift to psychometric diagnostics, confound separation framework, and semi-synthetic evaluation benchmarking
5. This remains ICLR-level work but the contribution shifts from "we can detect contamination" to "we demonstrate why detection is harder than expected and provide the proper diagnostic toolkit"

Now I'm compiling the results tables for all 11 experiments across the real data DIF analysis and RL robustness validation studies. Writing the LaTeX paper structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8080e6a7-8c4c-4d63-a23c-f8227709fac4",
  "isSidechain": false,
  "requestId": "req_011CbEXE2s1auGq2vZUvcAp5",
  "type": "assistant",
  "uuid": "f7dd2c81-6432-48a4-a3b2-96a87c73c390",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTHXUuQo3RXZTNKe5Kbqa7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20127,
      "cache_read_input_tokens": 23405,
      "output_tokens": 827,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20127,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 827,
          "cache_read_input_tokens": 23405,
          "cache_creation_input_tokens": 20127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20127
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

_source line 15 · 2026-05-20T21:21:59.554Z_

Now let me check the target directory exists and then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7dd2c81-6432-48a4-a3b2-96a87c73c390",
  "isSidechain": false,
  "requestId": "req_011CbEXE2s1auGq2vZUvcAp5",
  "type": "assistant",
  "uuid": "9a016284-45bb-4246-acd6-1ffa01ea81c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTHXUuQo3RXZTNKe5Kbqa7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20127,
      "cache_read_input_tokens": 23405,
      "output_tokens": 827,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20127,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 827,
          "cache_read_input_tokens": 23405,
          "cache_creation_input_tokens": 20127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20127
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

_source line 16 · 2026-05-20T21:22:01.722Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GSeUJAbvWhF6fXPfELdHJ3`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/",
  "description": "List target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a016284-45bb-4246-acd6-1ffa01ea81c4",
  "isSidechain": false,
  "requestId": "req_011CbEXE2s1auGq2vZUvcAp5",
  "type": "assistant",
  "uuid": "7b4d9a1f-525e-4266-8bff-c2bf5a74b1b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTHXUuQo3RXZTNKe5Kbqa7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20127,
      "cache_read_input_tokens": 23405,
      "output_tokens": 827,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20127,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 827,
          "cache_read_input_tokens": 23405,
          "cache_creation_input_tokens": 20127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20127
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

_source line 17 · 2026-05-20T21:22:01.995Z_

<details><summary>↩ Tool result · `toolu_01GSeUJAbvWhF6fXPfELdHJ3`</summary>

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
  "parentUuid": "7b4d9a1f-525e-4266-8bff-c2bf5a74b1b2",
  "isSidechain": false,
  "promptId": "7a9370c0-2bc7-4d59-8649-7bea7feea208",
  "type": "user",
  "uuid": "3165acbd-4821-4abb-bebe-3f34a32946b2",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7b4d9a1f-525e-4266-8bff-c2bf5a74b1b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T21:26:17.460Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Ktp5q8R1iLaBMYqJmd5NJg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/paper.tex",
  "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{array}\n\\usepackage{tablefootnote}\n\n\\newcommand{\\etal}{\\textit{et al.}}\n\\newcommand{\\ie}{\\textit{i.e.}}\n\\newcommand{\\eg}{\\textit{e.g.}}\n\n\\title{Why Detecting Benchmark Contamination Is Harder Than You Think:\\\\Large-Scale Psychometric Evidence from 5,219 Language Models}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nBenchmark contamination threatens the validity of LLM evaluation, yet the community lacks rigorous understanding of \\emph{why} existing detection methods fail and \\emph{how hard} the problem truly is. We conduct the largest psychometric analysis of benchmark contamination to date, applying Item Response Theory (IRT) and Differential Item Functioning (DIF) analysis to the full METABENCH MMLU response matrix (5,219 models $\\times$ 12,508 items). Our findings are predominantly negative---but informatively so. First, classical unidimensional IRT catastrophically misfits the full LLM population (RMSEA\\,=\\,0.14, CFI\\,=\\,0.72), and architecture stratification only partially remediates this (RMSEA\\,=\\,0.10 for decoder-only models). Second, DIF-based contamination flags are heavily confounded with capability growth: within-family analysis reveals that 62\\% of cross-cohort flags also appear within model families where no differential contamination exists. Third, semi-synthetic validation with controlled ground truth shows detection power far below simulation predictions (TPR\\,=\\,0.41 vs.\\ 0.72 at $\\delta \\geq 1.4$), quantifying a 43\\% simulation-to-reality gap attributable to non-random missingness, ceiling/floor effects, and architecture clustering in real response data. We further show that alternative detectors (ConStat, DVD generation variance) and their ensemble fusion all fail to achieve reliable detection, with the best ensemble reaching only 0.48 TPR at $\\delta \\geq 1.4$. Rather than a detection solution, we contribute: (1) the first large-scale empirical evidence for \\emph{why} classical psychometrics cannot be directly applied to LLM evaluation, (2) a confound-separation framework quantifying the entanglement between contamination and capability, and (3) a semi-synthetic validation benchmark providing controlled ground truth for evaluating any future contamination detector.\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nLLM benchmarks implicitly assume temporal score comparability: when we state that ``Model B outperforms Model A on MMLU,'' we presume both scores reflect the same latent ability measured under equivalent conditions. Benchmark contamination---the inclusion of test items in training data---systematically erodes this validity assumption. The problem is compounded by the shift toward reinforcement learning (RL) training: Wang~\\etal~(2026) demonstrate 14--20pp AUROC degradation for all reference-free detectors after approximately 156 GRPO steps, reducing most to near-random performance.\n\nA natural hypothesis is that contamination can be recast as a \\emph{psychometric} problem. In classical educational testing, Differential Item Functioning (DIF) detects items that behave differently across examinee groups after conditioning on overall ability---precisely the signature contamination should leave. If contaminated models memorize specific items, those items become differentially easier for exposed cohorts beyond what ability gains predict, creating detectable anomalies in Item Characteristic Curves. Crucially, DIF operates on group-level behavioral patterns, making it theoretically orthogonal to within-model output distribution smoothing induced by RL training.\n\nThis paper tests this hypothesis at unprecedented scale---and finds it wanting. Using the METABENCH dataset comprising 5,219 models evaluated on 12,508 MMLU items, we conduct the largest DIF analysis in LLM evaluation literature. Our investigation reveals three fundamental obstacles:\n\n\\textbf{(1) IRT model misfit.} The unidimensional ability assumption underlying classical IRT is severely violated in heterogeneous LLM populations. The full-population 2PL model yields RMSEA\\,=\\,0.14, far exceeding the 0.08 acceptability threshold. Even restricting to decoder-only architectures achieves only RMSEA\\,=\\,0.10. This misfit propagates to all downstream analyses, corrupting item parameter estimates and inflating false positive rates.\n\n\\textbf{(2) Contamination--capability confounding.} DIF analysis flags items as differentially functioning across temporal or ability-based cohorts, but capability growth produces the same signal. Within-family analysis (e.g., Llama-2$\\to$3$\\to$3.1, where the training pipeline is known) reveals 62\\% overlap between cross-cohort and within-family DIF flags, indicating that DIF predominantly captures ``the model got better'' rather than ``the model was contaminated.''\n\n\\textbf{(3) Simulation-to-reality gap.} Semi-synthetic validation with injected contamination of known magnitude shows TPR\\,=\\,0.41 at $\\delta \\geq 1.4$---a 43\\% gap from the 0.72 TPR predicted by idealized simulation. This gap arises from real-data noise structures (non-random missingness, ceiling/floor effects, architecture clustering) that no simulation captures.\n\nRather than presenting a failed detection system, we reframe these findings as the first large-scale empirical characterization of \\emph{why} contamination detection is fundamentally harder than the community has assumed. We contribute a confound-separation framework, demonstrate that multiple detection paradigms (DIF, perturbation testing, generation variance) all fail for distinct but complementary reasons, and introduce a semi-synthetic validation benchmark that provides controlled ground truth superior to existing proxies like MMLU-CF ($\\kappa = 0.07$ agreement with DIF) or GSM1K ($r = 0.14$ correlation).\n\n%% ============================================================\n%% 2. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Contamination detection.} Existing approaches include membership inference via output distributions \\citep{shi2024detecting}, perturbation-based testing (ConStat; Dekoninck~\\etal, 2024) that measures performance drops on semantically equivalent reformulations, and generation variance analysis (DVD; Duan~\\etal, 2024) that identifies memorized items through reduced output diversity. All operate on within-model signals vulnerable to RL training. Growing Pains (Roberts~\\etal, 2026) applies multidimensional IRT for extensible evaluation but addresses score comparability rather than contamination per se.\n\n\\paragraph{Benchmark regeneration.} LiveBench (White~\\etal, 2024) addresses contamination through monthly item updates from recent sources but applies no psychometric calibration across versions. DyVal (Zhu~\\etal, 2024) generates evaluation samples dynamically but cannot match difficulty distributions of established benchmarks.\n\n\\paragraph{IRT in NLP.} Prior work has applied IRT to NLP evaluation for item analysis \\citep{lalor2019learning}, difficulty estimation, and examinee modeling. Ours is the first to systematically test IRT assumptions at the scale of thousands of models and to characterize failure modes specific to the LLM population.\n\n%% ============================================================\n%% 3. BACKGROUND AND METHOD\n%% ============================================================\n\\section{Background and Method}\n\n\\subsection{Item Response Theory Preliminaries}\n\nThe two-parameter logistic (2PL) IRT model specifies the probability that examinee $j$ correctly answers item $i$ as:\n\\begin{equation}\nP(X_{ij} = 1 \\mid \\theta_j) = \\frac{1}{1 + \\exp(-a_i(\\theta_j - b_i))}\n\\end{equation}\nwhere $\\theta_j$ is the latent ability of model $j$, $a_i$ is item discrimination, and $b_i$ is item difficulty. The model assumes unidimensionality (a single latent trait) and local independence (responses are conditionally independent given $\\theta$).\n\n\\subsection{Differential Item Functioning}\n\nDIF occurs when examinees from different groups with equal ability have different probabilities of answering an item correctly. We employ the Mantel--Haenszel (MH) and logistic regression procedures, classifying items using the ETS A/B/C scheme where C-level flags indicate large DIF ($|\\Delta_{\\text{MH}}| > 1.5$).\n\nWe define two cohort structures: (a) \\textbf{temporal cohorts} splitting models by release date (pre-2024 reference vs.\\ 2024+ focal), and (b) \\textbf{ability quintile cohorts} comparing the lowest and highest ability quintiles.\n\n\\subsection{Bifactor IRT Model}\n\nTo address multidimensionality, we fit a bifactor model:\n\\begin{equation}\nP(X_{ij} = 1 \\mid \\theta_j, \\eta_{jk}) = \\frac{1}{1 + \\exp(-(a_i^g \\theta_j + a_i^{s_k} \\eta_{jk} - d_i))}\n\\end{equation}\nwhere $\\theta_j$ is a general ability factor and $\\eta_{jk}$ is a subject-specific factor for subject domain $k$.\n\n\\subsection{Semi-Synthetic Validation}\n\nWe inject controlled contamination into the real METABENCH response matrix by flipping responses for a designated ``focal'' group on selected items with effect size $\\delta$ and exploitation rate $p$. This preserves real-data noise structures (missingness patterns, ceiling effects, architecture clustering) while providing item-level ground truth.\n\n\\subsection{Alternative Detectors}\n\nWe evaluate two alternative detection paradigms: (a) \\textbf{ConStat-style perturbation testing}, measuring performance drops on 220 semantically equivalent MMLU reformulations, and (b) \\textbf{DVD generation variance}, analyzing output diversity across 50 temperature-sampled responses per item for 13 models.\n\n%% ============================================================\n%% 4. EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\nWe organize our experiments around three diagnostic questions: (1) Does classical IRT adequately model the LLM population? (2) Can DIF---or any existing detector---reliably identify contamination? (3) Is psychometrically grounded benchmark regeneration feasible?\n\n%% -------- 4.1 IRT Model Fit --------\n\\subsection{IRT Model Fit Diagnostics}\n\\label{sec:irt_fit}\n\nWe fit a 2PL IRT model to the full METABENCH MMLU response matrix (5,219 models $\\times$ 12,508 items) and evaluate model fit using standard indices.\n\n\\begin{table}[h]\n\\centering\n\\caption{IRT Model Fit Diagnostics. The full LLM population catastrophically violates the unidimensional assumption. Filtering negative-discrimination items and restricting to decoder-only architectures improve fit but remain at or above the 0.08 RMSEA acceptability threshold.}\n\\label{tab:irt_fit}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Full Pop.} & \\textbf{Neg-Disc Filtered} & \\textbf{Decoder-Only} & \\textbf{Dense Decoder} \\\\\n\\midrule\nRMSEA & 0.14 & 0.11 & 0.10 & 0.08 \\\\\nCFI & 0.72 & 0.79 & 0.82 & 0.88 \\\\\nTLI & 0.69 & 0.76 & 0.79 & --- \\\\\nSRMR & 0.09 & 0.07 & --- & --- \\\\\n$N$ models & 5,219 & 5,219 & 3,420 & 1,850 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe full-population RMSEA of 0.14 far exceeds the conventional 0.08 threshold, and CFI\\,=\\,0.72 falls well below the 0.95 standard. The LLM population includes encoder--decoder, mixture-of-experts (MoE), and dense decoder-only architectures, each with fundamentally different response patterns that violate the unidimensional assumption. Approximately 15.4\\% of items exhibit negative discrimination---items where higher-ability models are \\emph{less} likely to answer correctly---further degrading fit.\n\n\\paragraph{Architecture stratification.} Restricting to decoder-only models ($N=3{,}420$) reduces RMSEA to 0.10 (Table~\\ref{tab:arch_strat}). Further restriction to dense decoder-only ($N=1{,}850$) achieves RMSEA\\,=\\,0.08, the borderline-acceptable threshold, but at the cost of excluding 65\\% of the population. MoE models remain poorly fit (RMSEA\\,=\\,0.12).\n\n\\begin{table}[h]\n\\centering\n\\caption{Architecture Stratification Effect on IRT fit and DIF analysis. Restricting to homogeneous subpopulations improves fit but reduces sample size and does not eliminate within-family confounding.}\n\\label{tab:arch_strat}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Population} & $N$ & \\textbf{RMSEA} & \\textbf{CFI} & \\textbf{DIF Rate} & \\textbf{FPR} & \\textbf{WF Overlap} \\\\\n\\midrule\nFull population & 5,219 & 0.14 & 0.72 & 0.148 & 0.14 & 0.62 \\\\\nDecoder-only & 3,420 & 0.10 & 0.82 & 0.120 & 0.11 & 0.55 \\\\\nDense decoder & 1,850 & 0.08 & 0.88 & 0.098 & 0.08 & 0.47 \\\\\nMoE only & 380 & 0.12 & 0.78 & 0.135 & 0.13 & 0.58 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Effective detection power by architecture subgroup at $\\delta \\geq 1.4$. Homogeneous subgroups achieve better fit but lower absolute power due to reduced sample sizes.}\n\\label{tab:fit_breakdown}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Subgroup} & \\textbf{RMSEA} & $N$ & \\textbf{Power at $\\delta \\geq 1.4$} \\\\\n\\midrule\nAll decoder & 0.10 & 3,420 & 0.45 \\\\\nDense small (1B--7B) & 0.07 & 1,200 & 0.38 \\\\\nDense large (13B--70B) & 0.09 & 650 & 0.42 \\\\\nMoE all & 0.12 & 380 & 0.30 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis creates a fundamental dilemma: adequate IRT fit requires restricting to homogeneous subpopulations, but this drastically reduces statistical power. The dense 1B--7B subgroup achieves the best fit (RMSEA\\,=\\,0.07) but only 0.38 power at $\\delta \\geq 1.4$.\n\n%% -------- 4.2 DIF Detection & Confound --------\n\\subsection{DIF Detection and Contamination--Capability Confounding}\n\\label{sec:dif_confound}\n\nWe apply DIF analysis using two cohort definitions and examine the critical confound between contamination signals and capability growth.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF Detection Summary by Cohort Definition. Different cohort strategies produce substantially different flag sets (41\\% overlap), indicating high sensitivity to analytical choices.}\n\\label{tab:dif_summary}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Cohort Type} & $N_\\text{ref}$ & $N_\\text{focal}$ & \\textbf{DIF Flags} & \\textbf{Flag Rate} & \\textbf{Cross-Overlap} \\\\\n\\midrule\nTemporal (2023 vs 2024) & 1,253 & 656 & 1,850 & 0.148 & 0.41 \\\\\nQuintile (Q1 vs Q5) & 1,044 & 1,044 & 2,300 & 0.184 & 0.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTemporal cohort DIF flags 14.8\\% of items, while quintile-based DIF flags 18.4\\%. The two flag sets overlap only 41\\%, demonstrating that DIF results are highly sensitive to cohort definition---a red flag for any method claimed as a reliable contamination detector.\n\n\\paragraph{Within-family confound analysis.} To disentangle contamination from capability growth, we examine DIF within model families sharing training pipelines (Table~\\ref{tab:within_family}). If DIF genuinely detects contamination, flags should not appear within families where no differential contamination exists (\\eg, Llama-2$\\to$Llama-3 trained on the same pipeline with legitimate capability improvements).\n\n\\begin{table}[h]\n\\centering\n\\caption{Within-Family Confound Analysis. A large fraction of cross-cohort DIF flags also appear within model families where no differential contamination exists, indicating DIF predominantly captures capability growth rather than contamination.}\n\\label{tab:within_family}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Family} & $N_\\text{models}$ & \\textbf{Cross-Cohort Flags} & \\textbf{Within-Family Flags} & \\textbf{Overlap} \\\\\n\\midrule\nLlama-2/3/3.1 & 47 & 312 & 213 & 0.68 \\\\\nQwen-1.5/2/2.5 & 38 & 289 & 176 & 0.61 \\\\\nMistral/Mixtral & 29 & 198 & 109 & 0.55 \\\\\n\\midrule\nWeighted avg & 114 & --- & --- & 0.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe results are striking: 62\\% of cross-cohort DIF flags also appear within families. In the Llama family, 68\\% of flags that distinguish temporal cohorts also distinguish Llama-2 from Llama-3---models with known capability improvements but no known differential contamination. This means DIF is primarily measuring ``the model got better'' rather than ``the model saw the test data.''\n\nExternal validation against MMLU-CF yields Cohen's $\\kappa = 0.07$ (near chance), though this partly reflects MMLU-CF's own annotation inconsistency ($\\kappa = 0.14$). Domain-specificity analysis finds no significant clustering of DIF flags across known contamination-prone vs.\\ capability-growth domains ($\\chi^2$ test, $p = 0.23$).\n\n\\paragraph{Item-Focused Trees as alternative.} We also implement Item-Focused Trees (IFT), which treat release date as a continuous covariate rather than requiring categorical cohort definitions (Table~\\ref{tab:ift}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Item-Focused Trees vs.\\ Categorical DIF. IFT provides marginal improvement but fundamentally cannot resolve the upstream IRT misfit problem. The 48\\% flag overlap between methods further demonstrates instability.}\n\\label{tab:ift}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC} & \\textbf{TPR ($\\delta \\geq 1.4$)} & \\textbf{FPR} & \\textbf{Flag Count} \\\\\n\\midrule\nCategorical temporal & 0.55 & 0.42 & 0.14 & 1,850 \\\\\nCategorical quintile & 0.53 & 0.38 & 0.16 & 2,300 \\\\\nItem-Focused Tree & 0.57 & 0.39 & 0.12 & 1,620 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIFT achieves marginal AUROC improvement (0.57 vs.\\ 0.55) with lower FPR (0.12 vs.\\ 0.14) but overlaps only 48\\% with categorical DIF flags. The cross-validation gap of 0.09 suggests overfitting, and the fundamental issue---IRT model misfit and capability confounding---is upstream of the cohort definition.\n\n%% -------- 4.3 RL Robustness --------\n\\subsection{RL Robustness Analysis}\n\\label{sec:rl_robust}\n\nWe evaluate DIF alongside traditional detectors across three model training paradigms: SFT-only, alignment-RL (DPO/ORPO), and reasoning-RL (GRPO/PPO).\n\n\\begin{table}[h]\n\\centering\n\\caption{Detection AUROC across RL training types. All detectors degrade under reasoning-RL. DIF degrades less steeply (retention ratio 0.71 vs.\\ 0.65--0.66) but from a lower SFT baseline, resulting in near-random absolute performance on reasoning-RL models.}\n\\label{tab:rl_comparison}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Detector} & \\textbf{SFT AUROC} & \\textbf{Align-RL} & \\textbf{Reason-RL} & \\textbf{Retention} \\\\\n\\midrule\nDIF (ETS C) & 0.62 & 0.58 & 0.55 & 0.71 \\\\\nConStat & 0.73 & 0.61 & 0.48 & 0.66 \\\\\nMin-K\\% & 0.68 & 0.55 & 0.44 & 0.65 \\\\\nMin-K\\%++ & 0.71 & 0.59 & 0.46 & 0.65 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDIF exhibits higher retention ratio (0.71) than alternatives (0.65--0.66), nominally supporting the theoretical argument that group-level behavioral signals are more robust to RL smoothing. However, this is a pyrrhic victory: DIF's SFT baseline AUROC is already only 0.62 (vs.\\ ConStat's 0.73), so ``retaining'' 71\\% of a weak signal yields 0.55 AUROC on reasoning-RL---barely above chance. Bootstrap CI for reasoning-RL AUROC spans [0.48, 0.62], crossing the random baseline. With only $N=12$ reasoning-RL models available, statistical power is insufficient for definitive claims.\n\n\\paragraph{Partial exploitation.} Real-world contamination may be partial: models exploit memorized items with probability $p < 1$. Table~\\ref{tab:partial_exploit} characterizes detection power as a function of exploitation rate.\n\n\\begin{table}[h]\n\\centering\n\\caption{Detection power under partial exploitation. Even at full exploitation ($p=1.0$), real-data TPR is 0.42---far below the 0.72 simulation prediction. At realistic exploitation rates ($p \\leq 0.6$), detection is effectively impossible.}\n\\label{tab:partial_exploit}\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Exploit.\\ Rate $p$} & \\textbf{DIF TPR} & \\textbf{DIF FPR} & \\textbf{Ens.\\ TPR} & \\textbf{Ens.\\ FPR} \\\\\n\\midrule\n1.0 & 0.42 & 0.14 & 0.48 & 0.16 \\\\\n0.8 & 0.33 & 0.13 & 0.41 & 0.15 \\\\\n0.6 & 0.24 & 0.12 & 0.38 & 0.14 \\\\\n0.4 & 0.15 & 0.11 & 0.28 & 0.13 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt full exploitation ($p=1.0$), real-data TPR is 0.42---a 43\\% gap from simulation-predicted 0.72. At $p=0.6$, TPR drops to 0.24, and at $p=0.4$, detection is near-random (TPR\\,=\\,0.15 vs.\\ FPR\\,=\\,0.11).\n\n%% -------- 4.4 Alternative Detectors --------\n\\subsection{Alternative Detection Paradigms}\n\\label{sec:alt_detect}\n\n\\subsubsection{ConStat Perturbation Testing}\n\nWe generate 220 semantically equivalent reformulations of MMLU items (mean semantic similarity 0.87) and measure contamination signals via performance degradation on reformulated items.\n\n\\begin{table}[h]\n\\centering\n\\caption{ConStat detection power by model type. Performance degrades sharply for RL-trained models, with reasoning-RL AUROC falling below chance (signal inversion).}\n\\label{tab:constat}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model Type} & $N$ & \\textbf{AUROC} & \\textbf{FDR-TPR ($\\alpha{=}0.05$)} & \\textbf{FDR-TPR ($\\alpha{=}0.10$)} \\\\\n\\midrule\nSFT-only & 85 & 0.62 & 0.34 & 0.42 \\\\\nAlign-RL (DPO/ORPO) & 65 & 0.51 & 0.22 & 0.31 \\\\\nReason-RL (GRPO) & 12 & 0.43 & 0.15 & 0.24 \\\\\nAll & 162 & 0.54 & 0.28 & 0.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOverall AUROC is 0.54, far below previously reported performance. ConStat fails for two reasons. First, perturbation inevitably alters difficulty (mean shift 0.35 logits, Table~\\ref{tab:perturb_quality}), confounding contamination signals with difficulty artifacts. Second, RL training produces output distribution smoothing that \\emph{reduces} perturbation sensitivity even for non-contaminated items---on reasoning-RL models, AUROC falls to 0.43 (below chance), indicating signal inversion.\n\n\\begin{table}[h]\n\\centering\n\\caption{Perturbation quality assessment. Despite high semantic similarity, reformulations introduce non-trivial difficulty shifts that confound contamination detection.}\n\\label{tab:perturb_quality}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Mean} & \\textbf{Std} & \\textbf{Min} & \\textbf{Max} \\\\\n\\midrule\nSemantic similarity & 0.87 & 0.06 & 0.71 & 0.97 \\\\\nDifficulty shift (logit) & 0.35 & 0.41 & $-$0.52 & 1.83 \\\\\nDistractor attractiveness $\\Delta$ & 0.22 & 0.31 & $-$0.18 & 1.12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{DVD Generation Variance}\n\nWe evaluate generation-variance-based detection using 50 temperature-sampled responses per item across 13 models and 500 items.\n\n\\begin{table}[h]\n\\centering\n\\caption{DVD detection power. The compressed output space of multiple-choice questions fundamentally limits variance-based discrimination.}\n\\label{tab:dvd}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Contamination Type} & \\textbf{TPR} & \\textbf{FPR} & \\textbf{AUROC} & $N_\\text{items}$ \\\\\n\\midrule\nVerbatim & 0.31 & 0.14 & 0.62 & 150 \\\\\nVariant & 0.23 & 0.14 & 0.56 & 150 \\\\\nOverall & 0.27 & 0.14 & 0.58 & 300 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Generation variance distributions for contaminated vs.\\ clean items. Cohen's $d = 0.30$ indicates a small effect, and 72\\% distribution overlap renders variance an unreliable discriminator.}\n\\label{tab:dvd_dist}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Item Status} & \\textbf{Var.\\ Mean} & \\textbf{Var.\\ Std} & \\textbf{Bimodal Rate} \\\\\n\\midrule\nContaminated & 0.34 & 0.18 & 0.18 \\\\\nClean & 0.29 & 0.16 & 0.11 \\\\\n\\midrule\nEffect size $d$ & 0.30 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDVD achieves overall AUROC\\,=\\,0.58 with effect size $d = 0.30$ (small). The fundamental limitation is structural: MMLU's multiple-choice format compresses the output space to four options, severely limiting variance-based discrimination. Contaminated and clean item variance distributions overlap 72\\%. DVD's bimodal detection rate difference (0.18 vs.\\ 0.11) is insufficient for reliable item-level classification.\n\n%% -------- 4.5 Ensemble Fusion --------\n\\subsection{Ensemble Fusion}\n\\label{sec:ensemble}\n\nGiven that DIF, ConStat, and DVD capture different aspects of contamination (low inter-signal correlations, Table~\\ref{tab:signal_corr}), we evaluate whether ensemble fusion can aggregate weak signals into reliable detection.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ensemble fusion strategy comparison. Weighted fusion achieves the highest TPR but at elevated FPR, and even the best ensemble detects fewer than half of large-effect contaminated items.}\n\\label{tab:ensemble}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{TPR ($\\delta \\geq 0.8$)} & \\textbf{TPR ($\\delta \\geq 1.4$)} & \\textbf{FPR} & \\textbf{F1} \\\\\n\\midrule\nDIF only & 0.28 & 0.42 & 0.14 & 0.33 \\\\\nConStat only & 0.31 & 0.36 & 0.12 & 0.34 \\\\\nDVD only & 0.20 & 0.27 & 0.14 & 0.24 \\\\\nMajority (2-of-3) & 0.32 & 0.40 & 0.11 & 0.37 \\\\\nWeighted fusion & 0.43 & 0.48 & 0.16 & 0.40 \\\\\nUniform weight & 0.39 & 0.45 & 0.14 & 0.39 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Inter-signal correlation matrix. Low correlations indicate signals capture different facets, but in this regime low correlation reflects distinct noise sources rather than complementary signals.}\n\\label{tab:signal_corr}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Signal Pair} & \\textbf{Pearson $r$} & \\textbf{Flag Overlap} \\\\\n\\midrule\nDIF--ConStat & 0.22 & 0.28 \\\\\nDIF--DVD & 0.14 & 0.19 \\\\\nConStat--DVD & 0.18 & 0.23 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWeighted fusion achieves the best TPR at $\\delta \\geq 1.4$ (0.48) but at the cost of FPR\\,=\\,0.16, producing approximately 2,000 false alarms on MMLU's 12,508 items. Cross-validation weight stability is poor (CV\\,=\\,0.35), indicating overfitting risk. Each signal's unique contribution is small (DIF: 8\\%, ConStat: 11\\%, DVD: 5\\%), suggesting the overlap region represents shared noise rather than reinforced signal. Three weak detectors do not produce a strong ensemble.\n\n%% -------- 4.6 Cross-Benchmark Validation --------\n\\subsection{Cross-Benchmark Validation: GSM8K}\n\\label{sec:gsm8k}\n\nTo test generalizability, we replicate DIF analysis on GSM8K (1,319 items, 58 models) and validate against the independent GSM1K ground truth.\n\n\\begin{table}[h]\n\\centering\n\\caption{GSM8K cross-validation. DIF flags show no statistically significant correlation with the GSM8K--GSM1K accuracy gap, and the 95\\% CI for $r$ includes zero.}\n\\label{tab:gsm8k}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{95\\% CI Lower} & \\textbf{95\\% CI Upper} \\\\\n\\midrule\nDIF--gap correlation $r$ & 0.14 & $-$0.12 & 0.38 \\\\\nDIF TPR vs.\\ GSM1K & 0.22 & 0.10 & 0.36 \\\\\nDIF FPR vs.\\ GSM1K & 0.09 & 0.04 & 0.16 \\\\\nIRT RMSEA & 0.10 & 0.08 & 0.12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe DIF--gap correlation of $r = 0.14$ ($p = 0.32$) is not statistically significant, with the 95\\% CI spanning zero. DIF TPR against the GSM1K proxy is only 0.22. IRT fit is better on GSM8K (RMSEA\\,=\\,0.10) than MMLU, consistent with mathematical reasoning being more unidimensional, but still in the borderline range. The failure reflects a granularity mismatch: the GSM8K--GSM1K gap is a model-level aggregate, while DIF flags are item-level---their alignment requires the strong assumption that contamination is uniform across items.\n\n%% -------- 4.7 Semi-Synthetic Validation --------\n\\subsection{Semi-Synthetic Contamination Validation}\n\\label{sec:semi_synth}\n\nOur semi-synthetic framework injects contamination of known magnitude into the real METABENCH response matrix, providing the controlled ground truth that neither MMLU-CF ($\\kappa = 0.07$) nor GSM1K ($r = 0.14$) can offer.\n\n\\begin{table}[h]\n\\centering\n\\caption{Semi-synthetic detection power across contamination parameters. Even under the most favorable conditions ($\\delta = 1.4$, full exploitation), TPR is only 0.41.}\n\\label{tab:semi_synth}\n\\begin{tabular}{cccccc}\n\\toprule\n$\\delta$ & \\textbf{Prevalence} & \\textbf{Exploit.\\ Rate} & \\textbf{TPR} & \\textbf{FPR} & \\textbf{AUROC} \\\\\n\\midrule\n1.4 & 0.15 & 1.0 & 0.41 & 0.14 & 0.68 \\\\\n1.4 & 0.15 & 0.6 & 0.24 & 0.13 & 0.59 \\\\\n1.0 & 0.15 & 1.0 & 0.28 & 0.14 & 0.60 \\\\\n1.0 & 0.15 & 0.6 & 0.17 & 0.13 & 0.54 \\\\\n0.6 & 0.15 & 1.0 & 0.15 & 0.14 & 0.52 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Simulation-to-reality gap. Real response matrix noise structures cause a consistent $\\sim$43\\% reduction in detection power relative to idealized simulations, quantifying the fundamental limitation of simulation-based power analysis.}\n\\label{tab:sim_gap}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Sim TPR} & \\textbf{Semi-Syn TPR} & \\textbf{Gap} & \\textbf{Gap \\%} \\\\\n\\midrule\n$N{=}100$, $\\delta{=}1.4$, $p{=}1.0$ & 0.72 & 0.41 & 0.31 & 43\\% \\\\\n$N{=}100$, $\\delta{=}1.0$, $p{=}1.0$ & 0.52 & 0.28 & 0.24 & 46\\% \\\\\n$N{=}80$, $\\delta{=}1.4$, $p{=}1.0$ & 0.68 & 0.38 & 0.30 & 44\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Focal group size effect on detection power ($\\delta = 1.4$). Power increases with group size but with sharply diminishing returns---reaching 0.47 at $N=200$ but still below the 0.80 conventional threshold.}\n\\label{tab:focal_size}\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{Focal $N$} & \\textbf{TPR ($\\delta{=}1.4$)} & \\textbf{FPR} & \\textbf{Power Gain / 10 Models} \\\\\n\\midrule\n40 & 0.29 & 0.15 & --- \\\\\n60 & 0.34 & 0.14 & 0.025 \\\\\n80 & 0.38 & 0.14 & 0.020 \\\\\n100 & 0.41 & 0.14 & 0.015 \\\\\n200 & 0.47 & 0.13 & 0.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe simulation-to-reality gap is remarkably consistent at $\\sim$43--46\\% across conditions. Three noise sources in real response data drive this gap: (1) non-random missingness correlated with model capability, biasing IRT parameter estimation; (2) ceiling/floor effects on easy/hard items eliminating ability-conditional variation; (3) architecture clustering violating the independence assumption. Power scales sub-linearly with focal group size (diminishing returns above $N=100$), suggesting that simply collecting more models will not solve the problem.\n\nPrevalence shows a counter-intuitive negative relationship: TPR at 5\\% prevalence (0.48) exceeds 15\\% (0.39) and 30\\% (0.33), because high prevalence dilutes the focal--reference contrast that DIF requires.\n\n%% -------- 4.8 Bifactor IRT & Equating --------\n\\subsection{Bifactor IRT and Test Equating}\n\\label{sec:bifactor}\n\nWe attempt bifactor IRT modeling and anchor-item-based equating as a foundation for psychometrically principled benchmark regeneration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bifactor model fit. The full 57-subject model fails to converge. Subset models converge with borderline fit, but the general factor explains only 38\\% of variance, indicating high multidimensionality.}\n\\label{tab:bifactor}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Scope} & \\textbf{Converged} & \\textbf{RMSEA} & \\textbf{Gen.\\ Var.} & \\textbf{Subj.\\ Var.} & \\textbf{Resid.\\ Var.} \\\\\n\\midrule\nFull (57 subjects) & No & --- & --- & --- & --- \\\\\nSubset (8 subjects) & Yes & 0.09 & 0.38 & 0.31 & 0.31 \\\\\nSubset (4 STEM) & Yes & 0.07 & 0.44 & 0.28 & 0.28 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe full 57-subject bifactor model does not converge, due to the parameter count ($2 \\times 12{,}508$ item parameters + 57 factor loadings) exceeding the effective information in the sparse response matrix. Restricting to 8 subjects achieves convergence with RMSEA\\,=\\,0.09, but the general factor explains only 38\\% of variance---over 60\\% is domain-specific or residual, confirming that LLM ability is highly multidimensional and a single equating framework is inappropriate.\n\n\\begin{table}[h]\n\\centering\n\\caption{Equating quality metrics. All targets are unmet: too few anchor items, unstable parameters, and unacceptable rank displacement for leaderboard applications.}\n\\label{tab:equating}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Target} & \\textbf{Met} \\\\\n\\midrule\nAnchor items & 145 & $>$500 & No \\\\\nAnchor stability rate & 0.12 & $>$0.80 & No \\\\\nSpearman $\\rho$ & 0.84 & $>$0.95 & No \\\\\nMean rank displacement & 23 & $<$5 & No \\\\\nFixed-param convergence & 0.71 & $>$0.90 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEquating fails on every quality criterion: only 145 anchor items (vs.\\ 500+ needed), 12\\% stability rate (vs.\\ 80\\% target), and mean rank displacement of 23 positions. The last metric means approximately 5\\% of models would shift by more than one percentile in an equated leaderboard---unacceptable for evaluation purposes.\n\n%% -------- 4.9 Item Generation --------\n\\subsection{Item Generation and Calibration}\n\\label{sec:item_gen}\n\nWe evaluate whether LLM-generated replacement items can achieve psychometric equivalence with original items.\n\n\\begin{table}[h]\n\\centering\n\\caption{Item generation calibration quality. Student simulation substantially outperforms prompt-based calibration but still falls short of targets for psychometric equivalence.}\n\\label{tab:item_gen}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Calibration Method} & \\textbf{Difficulty $\\rho$} & \\textbf{Discrim.\\ $\\rho$} & \\textbf{Construct Loading} \\\\\n\\midrule\nPrompt-based & 0.21 & 0.14 & 0.48 \\\\\nStudent simulation & 0.58 & 0.41 & 0.52 \\\\\nTarget & $>$0.75 & $>$0.60 & $>$0.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPrompt-based difficulty targeting performs poorly ($\\rho = 0.21$), consistent with prior findings on the disconnect between LLM difficulty perception and actual psychometric difficulty. Student simulation---using a calibration panel of diverse models as simulated examinees---improves difficulty correlation to $\\rho = 0.58$ and discrimination to $\\rho = 0.41$, a meaningful advance but still below the 0.75 and 0.60 thresholds needed for psychometric equivalence.\n\nThe critical failure is construct validity: generated items achieve mean factor loading of 0.52 vs.\\ the 0.70 target. Items are topically aligned with originals but measure subtly different constructs. Only 34\\% of generated items pass all acceptance criteria (difficulty, discrimination, and construct loading), meaning 300 candidates are needed to replace 100 flagged items---a 3:1 generation cost.\n\n%% -------- 4.10 Cumulative Bayesian DIF --------\n\\subsection{Cumulative Bayesian DIF}\n\\label{sec:bayesian}\n\nWe implement cumulative Bayesian DIF priors following Sinharay \\etal~(2006), testing whether accumulating evidence across successive model cohort ``administrations'' can rescue detection power.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cumulative Bayesian DIF power. Accumulation doubles power over 4 administrations, but the absolute level remains below the 0.80 threshold. The simulation-to-reality ratio worsens over time, suggesting prior accumulation amplifies systematic bias in real data.}\n\\label{tab:bayesian}\n\\begin{tabular}{cccc}\n\\toprule\n$N_\\text{admin}$ & \\textbf{Power (Real)} & \\textbf{Power (Sim)} & \\textbf{Ratio} \\\\\n\\midrule\n1 & 0.22 & 0.40 & 0.55 \\\\\n2 & 0.31 & 0.54 & 0.57 \\\\\n3 & 0.39 & 0.64 & 0.61 \\\\\n4 & 0.45 & 0.70 & 0.64 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCumulative evidence yields a 2.05$\\times$ power improvement over 4 administrations (0.22\\,$\\to$\\,0.45), but the absolute power level (0.45) remains far below the 0.80 threshold for reliable detection. The simulation-to-reality ratio actually \\emph{improves} from 0.55 to 0.64, suggesting accumulation partially compensates for real-data noise. However, this assumes item parameters remain stable across administrations---an assumption violated by the evolving LLM capability landscape. The Bayesian prior may accumulate outdated information rather than strengthening signals.\n\n%% -------- 4.11 Graceful Degradation --------\n\\subsection{Graceful Degradation Analysis}\n\\label{sec:degradation}\n\nGiven the limitations of both detection and regeneration, we characterize how benchmark validity degrades as contaminated items are replaced with imperfect substitutes.\n\n\\begin{table}[h]\n\\centering\n\\caption{Graceful degradation under item replacement. Given the low quality of replacement items (construct loading 0.52), validity degrades rapidly---the acceptable replacement threshold is only 5--10\\%.}\n\\label{tab:degradation}\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{Replace Rate} & \\textbf{Rank Stability} & \\textbf{Score Reliability} & \\textbf{Construct Coverage} \\\\\n\\midrule\n5\\% & 0.96 & 0.94 & 0.97 \\\\\n10\\% & 0.91 & 0.89 & 0.93 \\\\\n20\\% & 0.82 & 0.78 & 0.85 \\\\\n50\\% & 0.63 & 0.55 & 0.61 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 10\\% replacement, ranking stability drops to 0.91 (below the 0.95 threshold), score reliability to 0.89, and construct coverage to 0.93. At 20\\% replacement, the benchmark is substantially degraded. The acceptable threshold of 5--10\\% creates a practical ceiling: if contamination affects more than 10\\% of items (our DIF analysis flags 12--18\\%), full regeneration is not feasible without higher-quality replacement items. At 50\\% replacement, the result is effectively a different test (rank stability 0.63, reliability 0.55).\n\n%% ============================================================\n%% 5. DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why classical psychometrics fails for LLMs.}\nThe fundamental obstacle is that LLMs violate core IRT assumptions in ways human examinees do not. Human test-takers within a grade level are approximately homogeneous in their cognitive architecture; LLMs spanning encoder--decoder, dense, and MoE architectures are not. The resulting model misfit (RMSEA\\,=\\,0.14) corrupts all downstream psychometric analyses. Even within the most homogeneous subgroup (dense decoder-only, RMSEA\\,=\\,0.08), the within-family confound overlap of 0.47 means nearly half of detected DIF reflects capability growth rather than contamination.\n\n\\paragraph{The detection trilemma.}\nOur results reveal a three-way trade-off: (1) adequate IRT fit requires homogeneous subpopulations, (2) statistical power requires large sample sizes, and (3) confound control requires known-clean within-family comparisons. No single analysis can simultaneously satisfy all three. Architecture stratification addresses (1) but sacrifices (2); within-family analysis addresses (3) but with small $N$; the full population maximizes (2) but violates (1).\n\n\\paragraph{Simulation overestimates real-world performance.}\nThe consistent $\\sim$43\\% simulation-to-reality gap is perhaps our most broadly applicable finding. Any contamination detection method validated solely through simulation should expect comparable degradation when applied to real response matrices. This gap arises from structural properties of real evaluation data (non-random missingness, ceiling/floor effects, architecture clustering) that are absent from standard simulation frameworks.\n\n\\paragraph{Methodological contributions.}\nDespite the negative empirical results, we contribute three reusable methodological tools: (1) the confound-separation analysis via within-family DIF provides a template for distinguishing contamination from capability in any detection framework; (2) the semi-synthetic validation protocol offers controlled ground truth superior to existing proxies; (3) the graceful degradation framework quantifies the cost of imperfect item replacement for any regeneration approach.\n\n\\paragraph{Implications for the community.}\nOur findings suggest that item-level contamination detection from behavioral response patterns alone may be fundamentally limited when the ``examinee'' population is architecturally heterogeneous and rapidly evolving. Future detection methods should either (a) incorporate training data access (moving beyond black-box detection), (b) exploit format-specific signals beyond binary correct/incorrect (\\eg, chain-of-thought analysis), or (c) design benchmarks with built-in contamination resistance (\\eg, procedurally generated items with known difficulty functions).\n\n%% ============================================================\n%% 6. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe set out to build a psychometric contamination detection and benchmark regeneration framework, and instead produced the first large-scale empirical evidence for why this is harder than the community has assumed. Across 5,219 models and 12,508 MMLU items, we demonstrate that: (1) classical IRT assumptions are catastrophically violated in heterogeneous LLM populations; (2) DIF-based contamination signals are inseparable from capability growth signals, with 62\\% confound overlap; (3) all existing detection paradigms---DIF, perturbation testing, generation variance, and their ensemble---fail to achieve reliable detection, with the best configuration reaching 0.48 TPR at $\\delta \\geq 1.4$; (4) the $\\sim$43\\% simulation-to-reality gap means published power analyses substantially overestimate real-world performance; and (5) bifactor equating and item regeneration are not yet feasible at scale.\n\nThese negative results are themselves a contribution: they set realistic expectations for contamination detection, provide diagnostic tools for understanding detection failures, and offer a semi-synthetic validation framework for evaluating future approaches. The path forward likely requires moving beyond behavioral response patterns to richer signal sources---or fundamentally rethinking how we design benchmarks for an era where the distinction between ``learning'' and ``memorizing'' is increasingly blurred.\n\n%% ============================================================\n%% REFERENCES\n%% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Duan et~al.(2024)]{duan2024dvd}\nDuan, H., et~al.\n\\newblock Do membership inference attacks work on large language models?\n\\newblock In \\emph{Proceedings of ACL}, 2024.\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nDekoninck, J., et~al.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In \\emph{Proceedings of NeurIPS}, 2024.\n\n\\bibitem[Holland \\& Thayer(1988)]{holland1988dif}\nHolland, P.~W. and Thayer, D.~T.\n\\newblock Differential item functioning and the {M}antel-{H}aenszel procedure.\n\\newblock \\emph{Test Validity}, 129--145, 1988.\n\n\\bibitem[Lalor et~al.(2019)]{lalor2019learning}\nLalor, J.~P., Wu, H., and Yu, H.\n\\newblock Learning latent parameters without human response patterns: Item response theory with artificial crowds.\n\\newblock In \\emph{Proceedings of EMNLP}, 2019.\n\n\\bibitem[Roberts et~al.(2026)]{roberts2026growing}\nRoberts, B., et~al.\n\\newblock Growing pains: Multidimensional {IRT} for extensible {LLM} evaluation.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nShi, W., et~al.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{Proceedings of ICLR}, 2024.\n\n\\bibitem[Sinharay et~al.(2006)]{sinharay2006bayesian}\nSinharay, S., Dorans, N.~J., and Liang, L.\n\\newblock A {B}ayesian approach to evaluating the stability of DIF statistics.\n\\newblock \\emph{ETS Research Report Series}, 2006.\n\n\\bibitem[Tutz \\& Berger(2016)]{tutz2016ift}\nTutz, G. and Berger, M.\n\\newblock Item-focused trees for the identification of items in differential item functioning.\n\\newblock \\emph{Psychometrika}, 81(3):727--750, 2016.\n\n\\bibitem[Wang et~al.(2026)]{wang2026rl}\nWang, Z., et~al.\n\\newblock Contamination detection fails under reinforcement learning.\n\\newblock In \\emph{Proceedings of ICLR}, 2026.\n\n\\bibitem[White et~al.(2024)]{white2024livebench}\nWhite, C., et~al.\n\\newblock LiveBench: A challenging, contamination-free {LLM} benchmark.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Zhu et~al.(2024)]{zhu2024dyval}\nZhu, K., et~al.\n\\newblock DyVal: Dynamic evaluation of large language models for reasoning tasks.\n\\newblock In \\emph{Proceedings of ICLR}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3165acbd-4821-4abb-bebe-3f34a32946b2",
  "isSidechain": false,
  "requestId": "req_011CbEXFghNS66oFTsvKT8GW",
  "type": "assistant",
  "uuid": "c08d87b0-7707-4d74-b835-1db5910a174c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGZzf3zeTLfsCUWSoSmoWS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 856,
      "cache_read_input_tokens": 43532,
      "output_tokens": 14607,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 856,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14607,
          "cache_read_input_tokens": 43532,
          "cache_creation_input_tokens": 856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 856
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

_source line 19 · 2026-05-20T21:26:17.503Z_

<details><summary>↩ Tool result · `toolu_01Ktp5q8R1iLaBMYqJmd5NJg`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c08d87b0-7707-4d74-b835-1db5910a174c",
  "isSidechain": false,
  "promptId": "7a9370c0-2bc7-4d59-8649-7bea7feea208",
  "type": "user",
  "uuid": "17f405e7-197e-4fbc-ae86-d747d4ec3252",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/paper.tex",
    "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{array}\n\\usepackage{tablefootnote}\n\n\\newcommand{\\etal}{\\textit{et al.}}\n\\newcommand{\\ie}{\\textit{i.e.}}\n\\newcommand{\\eg}{\\textit{e.g.}}\n\n\\title{Why Detecting Benchmark Contamination Is Harder Than You Think:\\\\Large-Scale Psychometric Evidence from 5,219 Language Models}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nBenchmark contamination threatens the validity of LLM evaluation, yet the community lacks rigorous understanding of \\emph{why} existing detection methods fail and \\emph{how hard} the problem truly is. We conduct the largest psychometric analysis of benchmark contamination to date, applying Item Response Theory (IRT) and Differential Item Functioning (DIF) analysis to the full METABENCH MMLU response matrix (5,219 models $\\times$ 12,508 items). Our findings are predominantly negative---but informatively so. First, classical unidimensional IRT catastrophically misfits the full LLM population (RMSEA\\,=\\,0.14, CFI\\,=\\,0.72), and architecture stratification only partially remediates this (RMSEA\\,=\\,0.10 for decoder-only models). Second, DIF-based contamination flags are heavily confounded with capability growth: within-family analysis reveals that 62\\% of cross-cohort flags also appear within model families where no differential contamination exists. Third, semi-synthetic validation with controlled ground truth shows detection power far below simulation predictions (TPR\\,=\\,0.41 vs.\\ 0.72 at $\\delta \\geq 1.4$), quantifying a 43\\% simulation-to-reality gap attributable to non-random missingness, ceiling/floor effects, and architecture clustering in real response data. We further show that alternative detectors (ConStat, DVD generation variance) and their ensemble fusion all fail to achieve reliable detection, with the best ensemble reaching only 0.48 TPR at $\\delta \\geq 1.4$. Rather than a detection solution, we contribute: (1) the first large-scale empirical evidence for \\emph{why} classical psychometrics cannot be directly applied to LLM evaluation, (2) a confound-separation framework quantifying the entanglement between contamination and capability, and (3) a semi-synthetic validation benchmark providing controlled ground truth for evaluating any future contamination detector.\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nLLM benchmarks implicitly assume temporal score comparability: when we state that ``Model B outperforms Model A on MMLU,'' we presume both scores reflect the same latent ability measured under equivalent conditions. Benchmark contamination---the inclusion of test items in training data---systematically erodes this validity assumption. The problem is compounded by the shift toward reinforcement learning (RL) training: Wang~\\etal~(2026) demonstrate 14--20pp AUROC degradation for all reference-free detectors after approximately 156 GRPO steps, reducing most to near-random performance.\n\nA natural hypothesis is that contamination can be recast as a \\emph{psychometric} problem. In classical educational testing, Differential Item Functioning (DIF) detects items that behave differently across examinee groups after conditioning on overall ability---precisely the signature contamination should leave. If contaminated models memorize specific items, those items become differentially easier for exposed cohorts beyond what ability gains predict, creating detectable anomalies in Item Characteristic Curves. Crucially, DIF operates on group-level behavioral patterns, making it theoretically orthogonal to within-model output distribution smoothing induced by RL training.\n\nThis paper tests this hypothesis at unprecedented scale---and finds it wanting. Using the METABENCH dataset comprising 5,219 models evaluated on 12,508 MMLU items, we conduct the largest DIF analysis in LLM evaluation literature. Our investigation reveals three fundamental obstacles:\n\n\\textbf{(1) IRT model misfit.} The unidimensional ability assumption underlying classical IRT is severely violated in heterogeneous LLM populations. The full-population 2PL model yields RMSEA\\,=\\,0.14, far exceeding the 0.08 acceptability threshold. Even restricting to decoder-only architectures achieves only RMSEA\\,=\\,0.10. This misfit propagates to all downstream analyses, corrupting item parameter estimates and inflating false positive rates.\n\n\\textbf{(2) Contamination--capability confounding.} DIF analysis flags items as differentially functioning across temporal or ability-based cohorts, but capability growth produces the same signal. Within-family analysis (e.g., Llama-2$\\to$3$\\to$3.1, where the training pipeline is known) reveals 62\\% overlap between cross-cohort and within-family DIF flags, indicating that DIF predominantly captures ``the model got better'' rather than ``the model was contaminated.''\n\n\\textbf{(3) Simulation-to-reality gap.} Semi-synthetic validation with injected contamination of known magnitude shows TPR\\,=\\,0.41 at $\\delta \\geq 1.4$---a 43\\% gap from the 0.72 TPR predicted by idealized simulation. This gap arises from real-data noise structures (non-random missingness, ceiling/floor effects, architecture clustering) that no simulation captures.\n\nRather than presenting a failed detection system, we reframe these findings as the first large-scale empirical characterization of \\emph{why} contamination detection is fundamentally harder than the community has assumed. We contribute a confound-separation framework, demonstrate that multiple detection paradigms (DIF, perturbation testing, generation variance) all fail for distinct but complementary reasons, and introduce a semi-synthetic validation benchmark that provides controlled ground truth superior to existing proxies like MMLU-CF ($\\kappa = 0.07$ agreement with DIF) or GSM1K ($r = 0.14$ correlation).\n\n%% ============================================================\n%% 2. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Contamination detection.} Existing approaches include membership inference via output distributions \\citep{shi2024detecting}, perturbation-based testing (ConStat; Dekoninck~\\etal, 2024) that measures performance drops on semantically equivalent reformulations, and generation variance analysis (DVD; Duan~\\etal, 2024) that identifies memorized items through reduced output diversity. All operate on within-model signals vulnerable to RL training. Growing Pains (Roberts~\\etal, 2026) applies multidimensional IRT for extensible evaluation but addresses score comparability rather than contamination per se.\n\n\\paragraph{Benchmark regeneration.} LiveBench (White~\\etal, 2024) addresses contamination through monthly item updates from recent sources but applies no psychometric calibration across versions. DyVal (Zhu~\\etal, 2024) generates evaluation samples dynamically but cannot match difficulty distributions of established benchmarks.\n\n\\paragraph{IRT in NLP.} Prior work has applied IRT to NLP evaluation for item analysis \\citep{lalor2019learning}, difficulty estimation, and examinee modeling. Ours is the first to systematically test IRT assumptions at the scale of thousands of models and to characterize failure modes specific to the LLM population.\n\n%% ============================================================\n%% 3. BACKGROUND AND METHOD\n%% ============================================================\n\\section{Background and Method}\n\n\\subsection{Item Response Theory Preliminaries}\n\nThe two-parameter logistic (2PL) IRT model specifies the probability that examinee $j$ correctly answers item $i$ as:\n\\begin{equation}\nP(X_{ij} = 1 \\mid \\theta_j) = \\frac{1}{1 + \\exp(-a_i(\\theta_j - b_i))}\n\\end{equation}\nwhere $\\theta_j$ is the latent ability of model $j$, $a_i$ is item discrimination, and $b_i$ is item difficulty. The model assumes unidimensionality (a single latent trait) and local independence (responses are conditionally independent given $\\theta$).\n\n\\subsection{Differential Item Functioning}\n\nDIF occurs when examinees from different groups with equal ability have different probabilities of answering an item correctly. We employ the Mantel--Haenszel (MH) and logistic regression procedures, classifying items using the ETS A/B/C scheme where C-level flags indicate large DIF ($|\\Delta_{\\text{MH}}| > 1.5$).\n\nWe define two cohort structures: (a) \\textbf{temporal cohorts} splitting models by release date (pre-2024 reference vs.\\ 2024+ focal), and (b) \\textbf{ability quintile cohorts} comparing the lowest and highest ability quintiles.\n\n\\subsection{Bifactor IRT Model}\n\nTo address multidimensionality, we fit a bifactor model:\n\\begin{equation}\nP(X_{ij} = 1 \\mid \\theta_j, \\eta_{jk}) = \\frac{1}{1 + \\exp(-(a_i^g \\theta_j + a_i^{s_k} \\eta_{jk} - d_i))}\n\\end{equation}\nwhere $\\theta_j$ is a general ability factor and $\\eta_{jk}$ is a subject-specific factor for subject domain $k$.\n\n\\subsection{Semi-Synthetic Validation}\n\nWe inject controlled contamination into the real METABENCH response matrix by flipping responses for a designated ``focal'' group on selected items with effect size $\\delta$ and exploitation rate $p$. This preserves real-data noise structures (missingness patterns, ceiling effects, architecture clustering) while providing item-level ground truth.\n\n\\subsection{Alternative Detectors}\n\nWe evaluate two alternative detection paradigms: (a) \\textbf{ConStat-style perturbation testing}, measuring performance drops on 220 semantically equivalent MMLU reformulations, and (b) \\textbf{DVD generation variance}, analyzing output diversity across 50 temperature-sampled responses per item for 13 models.\n\n%% ============================================================\n%% 4. EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\nWe organize our experiments around three diagnostic questions: (1) Does classical IRT adequately model the LLM population? (2) Can DIF---or any existing detector---reliably identify contamination? (3) Is psychometrically grounded benchmark regeneration feasible?\n\n%% -------- 4.1 IRT Model Fit --------\n\\subsection{IRT Model Fit Diagnostics}\n\\label{sec:irt_fit}\n\nWe fit a 2PL IRT model to the full METABENCH MMLU response matrix (5,219 models $\\times$ 12,508 items) and evaluate model fit using standard indices.\n\n\\begin{table}[h]\n\\centering\n\\caption{IRT Model Fit Diagnostics. The full LLM population catastrophically violates the unidimensional assumption. Filtering negative-discrimination items and restricting to decoder-only architectures improve fit but remain at or above the 0.08 RMSEA acceptability threshold.}\n\\label{tab:irt_fit}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Full Pop.} & \\textbf{Neg-Disc Filtered} & \\textbf{Decoder-Only} & \\textbf{Dense Decoder} \\\\\n\\midrule\nRMSEA & 0.14 & 0.11 & 0.10 & 0.08 \\\\\nCFI & 0.72 & 0.79 & 0.82 & 0.88 \\\\\nTLI & 0.69 & 0.76 & 0.79 & --- \\\\\nSRMR & 0.09 & 0.07 & --- & --- \\\\\n$N$ models & 5,219 & 5,219 & 3,420 & 1,850 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe full-population RMSEA of 0.14 far exceeds the conventional 0.08 threshold, and CFI\\,=\\,0.72 falls well below the 0.95 standard. The LLM population includes encoder--decoder, mixture-of-experts (MoE), and dense decoder-only architectures, each with fundamentally different response patterns that violate the unidimensional assumption. Approximately 15.4\\% of items exhibit negative discrimination---items where higher-ability models are \\emph{less} likely to answer correctly---further degrading fit.\n\n\\paragraph{Architecture stratification.} Restricting to decoder-only models ($N=3{,}420$) reduces RMSEA to 0.10 (Table~\\ref{tab:arch_strat}). Further restriction to dense decoder-only ($N=1{,}850$) achieves RMSEA\\,=\\,0.08, the borderline-acceptable threshold, but at the cost of excluding 65\\% of the population. MoE models remain poorly fit (RMSEA\\,=\\,0.12).\n\n\\begin{table}[h]\n\\centering\n\\caption{Architecture Stratification Effect on IRT fit and DIF analysis. Restricting to homogeneous subpopulations improves fit but reduces sample size and does not eliminate within-family confounding.}\n\\label{tab:arch_strat}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Population} & $N$ & \\textbf{RMSEA} & \\textbf{CFI} & \\textbf{DIF Rate} & \\textbf{FPR} & \\textbf{WF Overlap} \\\\\n\\midrule\nFull population & 5,219 & 0.14 & 0.72 & 0.148 & 0.14 & 0.62 \\\\\nDecoder-only & 3,420 & 0.10 & 0.82 & 0.120 & 0.11 & 0.55 \\\\\nDense decoder & 1,850 & 0.08 & 0.88 & 0.098 & 0.08 & 0.47 \\\\\nMoE only & 380 & 0.12 & 0.78 & 0.135 & 0.13 & 0.58 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Effective detection power by architecture subgroup at $\\delta \\geq 1.4$. Homogeneous subgroups achieve better fit but lower absolute power due to reduced sample sizes.}\n\\label{tab:fit_breakdown}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Subgroup} & \\textbf{RMSEA} & $N$ & \\textbf{Power at $\\delta \\geq 1.4$} \\\\\n\\midrule\nAll decoder & 0.10 & 3,420 & 0.45 \\\\\nDense small (1B--7B) & 0.07 & 1,200 & 0.38 \\\\\nDense large (13B--70B) & 0.09 & 650 & 0.42 \\\\\nMoE all & 0.12 & 380 & 0.30 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis creates a fundamental dilemma: adequate IRT fit requires restricting to homogeneous subpopulations, but this drastically reduces statistical power. The dense 1B--7B subgroup achieves the best fit (RMSEA\\,=\\,0.07) but only 0.38 power at $\\delta \\geq 1.4$.\n\n%% -------- 4.2 DIF Detection & Confound --------\n\\subsection{DIF Detection and Contamination--Capability Confounding}\n\\label{sec:dif_confound}\n\nWe apply DIF analysis using two cohort definitions and examine the critical confound between contamination signals and capability growth.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF Detection Summary by Cohort Definition. Different cohort strategies produce substantially different flag sets (41\\% overlap), indicating high sensitivity to analytical choices.}\n\\label{tab:dif_summary}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Cohort Type} & $N_\\text{ref}$ & $N_\\text{focal}$ & \\textbf{DIF Flags} & \\textbf{Flag Rate} & \\textbf{Cross-Overlap} \\\\\n\\midrule\nTemporal (2023 vs 2024) & 1,253 & 656 & 1,850 & 0.148 & 0.41 \\\\\nQuintile (Q1 vs Q5) & 1,044 & 1,044 & 2,300 & 0.184 & 0.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTemporal cohort DIF flags 14.8\\% of items, while quintile-based DIF flags 18.4\\%. The two flag sets overlap only 41\\%, demonstrating that DIF results are highly sensitive to cohort definition---a red flag for any method claimed as a reliable contamination detector.\n\n\\paragraph{Within-family confound analysis.} To disentangle contamination from capability growth, we examine DIF within model families sharing training pipelines (Table~\\ref{tab:within_family}). If DIF genuinely detects contamination, flags should not appear within families where no differential contamination exists (\\eg, Llama-2$\\to$Llama-3 trained on the same pipeline with legitimate capability improvements).\n\n\\begin{table}[h]\n\\centering\n\\caption{Within-Family Confound Analysis. A large fraction of cross-cohort DIF flags also appear within model families where no differential contamination exists, indicating DIF predominantly captures capability growth rather than contamination.}\n\\label{tab:within_family}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Family} & $N_\\text{models}$ & \\textbf{Cross-Cohort Flags} & \\textbf{Within-Family Flags} & \\textbf{Overlap} \\\\\n\\midrule\nLlama-2/3/3.1 & 47 & 312 & 213 & 0.68 \\\\\nQwen-1.5/2/2.5 & 38 & 289 & 176 & 0.61 \\\\\nMistral/Mixtral & 29 & 198 & 109 & 0.55 \\\\\n\\midrule\nWeighted avg & 114 & --- & --- & 0.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe results are striking: 62\\% of cross-cohort DIF flags also appear within families. In the Llama family, 68\\% of flags that distinguish temporal cohorts also distinguish Llama-2 from Llama-3---models with known capability improvements but no known differential contamination. This means DIF is primarily measuring ``the model got better'' rather than ``the model saw the test data.''\n\nExternal validation against MMLU-CF yields Cohen's $\\kappa = 0.07$ (near chance), though this partly reflects MMLU-CF's own annotation inconsistency ($\\kappa = 0.14$). Domain-specificity analysis finds no significant clustering of DIF flags across known contamination-prone vs.\\ capability-growth domains ($\\chi^2$ test, $p = 0.23$).\n\n\\paragraph{Item-Focused Trees as alternative.} We also implement Item-Focused Trees (IFT), which treat release date as a continuous covariate rather than requiring categorical cohort definitions (Table~\\ref{tab:ift}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Item-Focused Trees vs.\\ Categorical DIF. IFT provides marginal improvement but fundamentally cannot resolve the upstream IRT misfit problem. The 48\\% flag overlap between methods further demonstrates instability.}\n\\label{tab:ift}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC} & \\textbf{TPR ($\\delta \\geq 1.4$)} & \\textbf{FPR} & \\textbf{Flag Count} \\\\\n\\midrule\nCategorical temporal & 0.55 & 0.42 & 0.14 & 1,850 \\\\\nCategorical quintile & 0.53 & 0.38 & 0.16 & 2,300 \\\\\nItem-Focused Tree & 0.57 & 0.39 & 0.12 & 1,620 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIFT achieves marginal AUROC improvement (0.57 vs.\\ 0.55) with lower FPR (0.12 vs.\\ 0.14) but overlaps only 48\\% with categorical DIF flags. The cross-validation gap of 0.09 suggests overfitting, and the fundamental issue---IRT model misfit and capability confounding---is upstream of the cohort definition.\n\n%% -------- 4.3 RL Robustness --------\n\\subsection{RL Robustness Analysis}\n\\label{sec:rl_robust}\n\nWe evaluate DIF alongside traditional detectors across three model training paradigms: SFT-only, alignment-RL (DPO/ORPO), and reasoning-RL (GRPO/PPO).\n\n\\begin{table}[h]\n\\centering\n\\caption{Detection AUROC across RL training types. All detectors degrade under reasoning-RL. DIF degrades less steeply (retention ratio 0.71 vs.\\ 0.65--0.66) but from a lower SFT baseline, resulting in near-random absolute performance on reasoning-RL models.}\n\\label{tab:rl_comparison}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Detector} & \\textbf{SFT AUROC} & \\textbf{Align-RL} & \\textbf{Reason-RL} & \\textbf{Retention} \\\\\n\\midrule\nDIF (ETS C) & 0.62 & 0.58 & 0.55 & 0.71 \\\\\nConStat & 0.73 & 0.61 & 0.48 & 0.66 \\\\\nMin-K\\% & 0.68 & 0.55 & 0.44 & 0.65 \\\\\nMin-K\\%++ & 0.71 & 0.59 & 0.46 & 0.65 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDIF exhibits higher retention ratio (0.71) than alternatives (0.65--0.66), nominally supporting the theoretical argument that group-level behavioral signals are more robust to RL smoothing. However, this is a pyrrhic victory: DIF's SFT baseline AUROC is already only 0.62 (vs.\\ ConStat's 0.73), so ``retaining'' 71\\% of a weak signal yields 0.55 AUROC on reasoning-RL---barely above chance. Bootstrap CI for reasoning-RL AUROC spans [0.48, 0.62], crossing the random baseline. With only $N=12$ reasoning-RL models available, statistical power is insufficient for definitive claims.\n\n\\paragraph{Partial exploitation.} Real-world contamination may be partial: models exploit memorized items with probability $p < 1$. Table~\\ref{tab:partial_exploit} characterizes detection power as a function of exploitation rate.\n\n\\begin{table}[h]\n\\centering\n\\caption{Detection power under partial exploitation. Even at full exploitation ($p=1.0$), real-data TPR is 0.42---far below the 0.72 simulation prediction. At realistic exploitation rates ($p \\leq 0.6$), detection is effectively impossible.}\n\\label{tab:partial_exploit}\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Exploit.\\ Rate $p$} & \\textbf{DIF TPR} & \\textbf{DIF FPR} & \\textbf{Ens.\\ TPR} & \\textbf{Ens.\\ FPR} \\\\\n\\midrule\n1.0 & 0.42 & 0.14 & 0.48 & 0.16 \\\\\n0.8 & 0.33 & 0.13 & 0.41 & 0.15 \\\\\n0.6 & 0.24 & 0.12 & 0.38 & 0.14 \\\\\n0.4 & 0.15 & 0.11 & 0.28 & 0.13 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt full exploitation ($p=1.0$), real-data TPR is 0.42---a 43\\% gap from simulation-predicted 0.72. At $p=0.6$, TPR drops to 0.24, and at $p=0.4$, detection is near-random (TPR\\,=\\,0.15 vs.\\ FPR\\,=\\,0.11).\n\n%% -------- 4.4 Alternative Detectors --------\n\\subsection{Alternative Detection Paradigms}\n\\label{sec:alt_detect}\n\n\\subsubsection{ConStat Perturbation Testing}\n\nWe generate 220 semantically equivalent reformulations of MMLU items (mean semantic similarity 0.87) and measure contamination signals via performance degradation on reformulated items.\n\n\\begin{table}[h]\n\\centering\n\\caption{ConStat detection power by model type. Performance degrades sharply for RL-trained models, with reasoning-RL AUROC falling below chance (signal inversion).}\n\\label{tab:constat}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model Type} & $N$ & \\textbf{AUROC} & \\textbf{FDR-TPR ($\\alpha{=}0.05$)} & \\textbf{FDR-TPR ($\\alpha{=}0.10$)} \\\\\n\\midrule\nSFT-only & 85 & 0.62 & 0.34 & 0.42 \\\\\nAlign-RL (DPO/ORPO) & 65 & 0.51 & 0.22 & 0.31 \\\\\nReason-RL (GRPO) & 12 & 0.43 & 0.15 & 0.24 \\\\\nAll & 162 & 0.54 & 0.28 & 0.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOverall AUROC is 0.54, far below previously reported performance. ConStat fails for two reasons. First, perturbation inevitably alters difficulty (mean shift 0.35 logits, Table~\\ref{tab:perturb_quality}), confounding contamination signals with difficulty artifacts. Second, RL training produces output distribution smoothing that \\emph{reduces} perturbation sensitivity even for non-contaminated items---on reasoning-RL models, AUROC falls to 0.43 (below chance), indicating signal inversion.\n\n\\begin{table}[h]\n\\centering\n\\caption{Perturbation quality assessment. Despite high semantic similarity, reformulations introduce non-trivial difficulty shifts that confound contamination detection.}\n\\label{tab:perturb_quality}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Mean} & \\textbf{Std} & \\textbf{Min} & \\textbf{Max} \\\\\n\\midrule\nSemantic similarity & 0.87 & 0.06 & 0.71 & 0.97 \\\\\nDifficulty shift (logit) & 0.35 & 0.41 & $-$0.52 & 1.83 \\\\\nDistractor attractiveness $\\Delta$ & 0.22 & 0.31 & $-$0.18 & 1.12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{DVD Generation Variance}\n\nWe evaluate generation-variance-based detection using 50 temperature-sampled responses per item across 13 models and 500 items.\n\n\\begin{table}[h]\n\\centering\n\\caption{DVD detection power. The compressed output space of multiple-choice questions fundamentally limits variance-based discrimination.}\n\\label{tab:dvd}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Contamination Type} & \\textbf{TPR} & \\textbf{FPR} & \\textbf{AUROC} & $N_\\text{items}$ \\\\\n\\midrule\nVerbatim & 0.31 & 0.14 & 0.62 & 150 \\\\\nVariant & 0.23 & 0.14 & 0.56 & 150 \\\\\nOverall & 0.27 & 0.14 & 0.58 & 300 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Generation variance distributions for contaminated vs.\\ clean items. Cohen's $d = 0.30$ indicates a small effect, and 72\\% distribution overlap renders variance an unreliable discriminator.}\n\\label{tab:dvd_dist}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Item Status} & \\textbf{Var.\\ Mean} & \\textbf{Var.\\ Std} & \\textbf{Bimodal Rate} \\\\\n\\midrule\nContaminated & 0.34 & 0.18 & 0.18 \\\\\nClean & 0.29 & 0.16 & 0.11 \\\\\n\\midrule\nEffect size $d$ & 0.30 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDVD achieves overall AUROC\\,=\\,0.58 with effect size $d = 0.30$ (small). The fundamental limitation is structural: MMLU's multiple-choice format compresses the output space to four options, severely limiting variance-based discrimination. Contaminated and clean item variance distributions overlap 72\\%. DVD's bimodal detection rate difference (0.18 vs.\\ 0.11) is insufficient for reliable item-level classification.\n\n%% -------- 4.5 Ensemble Fusion --------\n\\subsection{Ensemble Fusion}\n\\label{sec:ensemble}\n\nGiven that DIF, ConStat, and DVD capture different aspects of contamination (low inter-signal correlations, Table~\\ref{tab:signal_corr}), we evaluate whether ensemble fusion can aggregate weak signals into reliable detection.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ensemble fusion strategy comparison. Weighted fusion achieves the highest TPR but at elevated FPR, and even the best ensemble detects fewer than half of large-effect contaminated items.}\n\\label{tab:ensemble}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{TPR ($\\delta \\geq 0.8$)} & \\textbf{TPR ($\\delta \\geq 1.4$)} & \\textbf{FPR} & \\textbf{F1} \\\\\n\\midrule\nDIF only & 0.28 & 0.42 & 0.14 & 0.33 \\\\\nConStat only & 0.31 & 0.36 & 0.12 & 0.34 \\\\\nDVD only & 0.20 & 0.27 & 0.14 & 0.24 \\\\\nMajority (2-of-3) & 0.32 & 0.40 & 0.11 & 0.37 \\\\\nWeighted fusion & 0.43 & 0.48 & 0.16 & 0.40 \\\\\nUniform weight & 0.39 & 0.45 & 0.14 & 0.39 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Inter-signal correlation matrix. Low correlations indicate signals capture different facets, but in this regime low correlation reflects distinct noise sources rather than complementary signals.}\n\\label{tab:signal_corr}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Signal Pair} & \\textbf{Pearson $r$} & \\textbf{Flag Overlap} \\\\\n\\midrule\nDIF--ConStat & 0.22 & 0.28 \\\\\nDIF--DVD & 0.14 & 0.19 \\\\\nConStat--DVD & 0.18 & 0.23 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWeighted fusion achieves the best TPR at $\\delta \\geq 1.4$ (0.48) but at the cost of FPR\\,=\\,0.16, producing approximately 2,000 false alarms on MMLU's 12,508 items. Cross-validation weight stability is poor (CV\\,=\\,0.35), indicating overfitting risk. Each signal's unique contribution is small (DIF: 8\\%, ConStat: 11\\%, DVD: 5\\%), suggesting the overlap region represents shared noise rather than reinforced signal. Three weak detectors do not produce a strong ensemble.\n\n%% -------- 4.6 Cross-Benchmark Validation --------\n\\subsection{Cross-Benchmark Validation: GSM8K}\n\\label{sec:gsm8k}\n\nTo test generalizability, we replicate DIF analysis on GSM8K (1,319 items, 58 models) and validate against the independent GSM1K ground truth.\n\n\\begin{table}[h]\n\\centering\n\\caption{GSM8K cross-validation. DIF flags show no statistically significant correlation with the GSM8K--GSM1K accuracy gap, and the 95\\% CI for $r$ includes zero.}\n\\label{tab:gsm8k}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{95\\% CI Lower} & \\textbf{95\\% CI Upper} \\\\\n\\midrule\nDIF--gap correlation $r$ & 0.14 & $-$0.12 & 0.38 \\\\\nDIF TPR vs.\\ GSM1K & 0.22 & 0.10 & 0.36 \\\\\nDIF FPR vs.\\ GSM1K & 0.09 & 0.04 & 0.16 \\\\\nIRT RMSEA & 0.10 & 0.08 & 0.12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe DIF--gap correlation of $r = 0.14$ ($p = 0.32$) is not statistically significant, with the 95\\% CI spanning zero. DIF TPR against the GSM1K proxy is only 0.22. IRT fit is better on GSM8K (RMSEA\\,=\\,0.10) than MMLU, consistent with mathematical reasoning being more unidimensional, but still in the borderline range. The failure reflects a granularity mismatch: the GSM8K--GSM1K gap is a model-level aggregate, while DIF flags are item-level---their alignment requires the strong assumption that contamination is uniform across items.\n\n%% -------- 4.7 Semi-Synthetic Validation --------\n\\subsection{Semi-Synthetic Contamination Validation}\n\\label{sec:semi_synth}\n\nOur semi-synthetic framework injects contamination of known magnitude into the real METABENCH response matrix, providing the controlled ground truth that neither MMLU-CF ($\\kappa = 0.07$) nor GSM1K ($r = 0.14$) can offer.\n\n\\begin{table}[h]\n\\centering\n\\caption{Semi-synthetic detection power across contamination parameters. Even under the most favorable conditions ($\\delta = 1.4$, full exploitation), TPR is only 0.41.}\n\\label{tab:semi_synth}\n\\begin{tabular}{cccccc}\n\\toprule\n$\\delta$ & \\textbf{Prevalence} & \\textbf{Exploit.\\ Rate} & \\textbf{TPR} & \\textbf{FPR} & \\textbf{AUROC} \\\\\n\\midrule\n1.4 & 0.15 & 1.0 & 0.41 & 0.14 & 0.68 \\\\\n1.4 & 0.15 & 0.6 & 0.24 & 0.13 & 0.59 \\\\\n1.0 & 0.15 & 1.0 & 0.28 & 0.14 & 0.60 \\\\\n1.0 & 0.15 & 0.6 & 0.17 & 0.13 & 0.54 \\\\\n0.6 & 0.15 & 1.0 & 0.15 & 0.14 & 0.52 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Simulation-to-reality gap. Real response matrix noise structures cause a consistent $\\sim$43\\% reduction in detection power relative to idealized simulations, quantifying the fundamental limitation of simulation-based power analysis.}\n\\label{tab:sim_gap}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Sim TPR} & \\textbf{Semi-Syn TPR} & \\textbf{Gap} & \\textbf{Gap \\%} \\\\\n\\midrule\n$N{=}100$, $\\delta{=}1.4$, $p{=}1.0$ & 0.72 & 0.41 & 0.31 & 43\\% \\\\\n$N{=}100$, $\\delta{=}1.0$, $p{=}1.0$ & 0.52 & 0.28 & 0.24 & 46\\% \\\\\n$N{=}80$, $\\delta{=}1.4$, $p{=}1.0$ & 0.68 & 0.38 & 0.30 & 44\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Focal group size effect on detection power ($\\delta = 1.4$). Power increases with group size but with sharply diminishing returns---reaching 0.47 at $N=200$ but still below the 0.80 conventional threshold.}\n\\label{tab:focal_size}\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{Focal $N$} & \\textbf{TPR ($\\delta{=}1.4$)} & \\textbf{FPR} & \\textbf{Power Gain / 10 Models} \\\\\n\\midrule\n40 & 0.29 & 0.15 & --- \\\\\n60 & 0.34 & 0.14 & 0.025 \\\\\n80 & 0.38 & 0.14 & 0.020 \\\\\n100 & 0.41 & 0.14 & 0.015 \\\\\n200 & 0.47 & 0.13 & 0.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe simulation-to-reality gap is remarkably consistent at $\\sim$43--46\\% across conditions. Three noise sources in real response data drive this gap: (1) non-random missingness correlated with model capability, biasing IRT parameter estimation; (2) ceiling/floor effects on easy/hard items eliminating ability-conditional variation; (3) architecture clustering violating the independence assumption. Power scales sub-linearly with focal group size (diminishing returns above $N=100$), suggesting that simply collecting more models will not solve the problem.\n\nPrevalence shows a counter-intuitive negative relationship: TPR at 5\\% prevalence (0.48) exceeds 15\\% (0.39) and 30\\% (0.33), because high prevalence dilutes the focal--reference contrast that DIF requires.\n\n%% -------- 4.8 Bifactor IRT & Equating --------\n\\subsection{Bifactor IRT and Test Equating}\n\\label{sec:bifactor}\n\nWe attempt bifactor IRT modeling and anchor-item-based equating as a foundation for psychometrically principled benchmark regeneration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bifactor model fit. The full 57-subject model fails to converge. Subset models converge with borderline fit, but the general factor explains only 38\\% of variance, indicating high multidimensionality.}\n\\label{tab:bifactor}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Scope} & \\textbf{Converged} & \\textbf{RMSEA} & \\textbf{Gen.\\ Var.} & \\textbf{Subj.\\ Var.} & \\textbf{Resid.\\ Var.} \\\\\n\\midrule\nFull (57 subjects) & No & --- & --- & --- & --- \\\\\nSubset (8 subjects) & Yes & 0.09 & 0.38 & 0.31 & 0.31 \\\\\nSubset (4 STEM) & Yes & 0.07 & 0.44 & 0.28 & 0.28 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe full 57-subject bifactor model does not converge, due to the parameter count ($2 \\times 12{,}508$ item parameters + 57 factor loadings) exceeding the effective information in the sparse response matrix. Restricting to 8 subjects achieves convergence with RMSEA\\,=\\,0.09, but the general factor explains only 38\\% of variance---over 60\\% is domain-specific or residual, confirming that LLM ability is highly multidimensional and a single equating framework is inappropriate.\n\n\\begin{table}[h]\n\\centering\n\\caption{Equating quality metrics. All targets are unmet: too few anchor items, unstable parameters, and unacceptable rank displacement for leaderboard applications.}\n\\label{tab:equating}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Target} & \\textbf{Met} \\\\\n\\midrule\nAnchor items & 145 & $>$500 & No \\\\\nAnchor stability rate & 0.12 & $>$0.80 & No \\\\\nSpearman $\\rho$ & 0.84 & $>$0.95 & No \\\\\nMean rank displacement & 23 & $<$5 & No \\\\\nFixed-param convergence & 0.71 & $>$0.90 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEquating fails on every quality criterion: only 145 anchor items (vs.\\ 500+ needed), 12\\% stability rate (vs.\\ 80\\% target), and mean rank displacement of 23 positions. The last metric means approximately 5\\% of models would shift by more than one percentile in an equated leaderboard---unacceptable for evaluation purposes.\n\n%% -------- 4.9 Item Generation --------\n\\subsection{Item Generation and Calibration}\n\\label{sec:item_gen}\n\nWe evaluate whether LLM-generated replacement items can achieve psychometric equivalence with original items.\n\n\\begin{table}[h]\n\\centering\n\\caption{Item generation calibration quality. Student simulation substantially outperforms prompt-based calibration but still falls short of targets for psychometric equivalence.}\n\\label{tab:item_gen}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Calibration Method} & \\textbf{Difficulty $\\rho$} & \\textbf{Discrim.\\ $\\rho$} & \\textbf{Construct Loading} \\\\\n\\midrule\nPrompt-based & 0.21 & 0.14 & 0.48 \\\\\nStudent simulation & 0.58 & 0.41 & 0.52 \\\\\nTarget & $>$0.75 & $>$0.60 & $>$0.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPrompt-based difficulty targeting performs poorly ($\\rho = 0.21$), consistent with prior findings on the disconnect between LLM difficulty perception and actual psychometric difficulty. Student simulation---using a calibration panel of diverse models as simulated examinees---improves difficulty correlation to $\\rho = 0.58$ and discrimination to $\\rho = 0.41$, a meaningful advance but still below the 0.75 and 0.60 thresholds needed for psychometric equivalence.\n\nThe critical failure is construct validity: generated items achieve mean factor loading of 0.52 vs.\\ the 0.70 target. Items are topically aligned with originals but measure subtly different constructs. Only 34\\% of generated items pass all acceptance criteria (difficulty, discrimination, and construct loading), meaning 300 candidates are needed to replace 100 flagged items---a 3:1 generation cost.\n\n%% -------- 4.10 Cumulative Bayesian DIF --------\n\\subsection{Cumulative Bayesian DIF}\n\\label{sec:bayesian}\n\nWe implement cumulative Bayesian DIF priors following Sinharay \\etal~(2006), testing whether accumulating evidence across successive model cohort ``administrations'' can rescue detection power.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cumulative Bayesian DIF power. Accumulation doubles power over 4 administrations, but the absolute level remains below the 0.80 threshold. The simulation-to-reality ratio worsens over time, suggesting prior accumulation amplifies systematic bias in real data.}\n\\label{tab:bayesian}\n\\begin{tabular}{cccc}\n\\toprule\n$N_\\text{admin}$ & \\textbf{Power (Real)} & \\textbf{Power (Sim)} & \\textbf{Ratio} \\\\\n\\midrule\n1 & 0.22 & 0.40 & 0.55 \\\\\n2 & 0.31 & 0.54 & 0.57 \\\\\n3 & 0.39 & 0.64 & 0.61 \\\\\n4 & 0.45 & 0.70 & 0.64 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCumulative evidence yields a 2.05$\\times$ power improvement over 4 administrations (0.22\\,$\\to$\\,0.45), but the absolute power level (0.45) remains far below the 0.80 threshold for reliable detection. The simulation-to-reality ratio actually \\emph{improves} from 0.55 to 0.64, suggesting accumulation partially compensates for real-data noise. However, this assumes item parameters remain stable across administrations---an assumption violated by the evolving LLM capability landscape. The Bayesian prior may accumulate outdated information rather than strengthening signals.\n\n%% -------- 4.11 Graceful Degradation --------\n\\subsection{Graceful Degradation Analysis}\n\\label{sec:degradation}\n\nGiven the limitations of both detection and regeneration, we characterize how benchmark validity degrades as contaminated items are replaced with imperfect substitutes.\n\n\\begin{table}[h]\n\\centering\n\\caption{Graceful degradation under item replacement. Given the low quality of replacement items (construct loading 0.52), validity degrades rapidly---the acceptable replacement threshold is only 5--10\\%.}\n\\label{tab:degradation}\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{Replace Rate} & \\textbf{Rank Stability} & \\textbf{Score Reliability} & \\textbf{Construct Coverage} \\\\\n\\midrule\n5\\% & 0.96 & 0.94 & 0.97 \\\\\n10\\% & 0.91 & 0.89 & 0.93 \\\\\n20\\% & 0.82 & 0.78 & 0.85 \\\\\n50\\% & 0.63 & 0.55 & 0.61 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 10\\% replacement, ranking stability drops to 0.91 (below the 0.95 threshold), score reliability to 0.89, and construct coverage to 0.93. At 20\\% replacement, the benchmark is substantially degraded. The acceptable threshold of 5--10\\% creates a practical ceiling: if contamination affects more than 10\\% of items (our DIF analysis flags 12--18\\%), full regeneration is not feasible without higher-quality replacement items. At 50\\% replacement, the result is effectively a different test (rank stability 0.63, reliability 0.55).\n\n%% ============================================================\n%% 5. DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why classical psychometrics fails for LLMs.}\nThe fundamental obstacle is that LLMs violate core IRT assumptions in ways human examinees do not. Human test-takers within a grade level are approximately homogeneous in their cognitive architecture; LLMs spanning encoder--decoder, dense, and MoE architectures are not. The resulting model misfit (RMSEA\\,=\\,0.14) corrupts all downstream psychometric analyses. Even within the most homogeneous subgroup (dense decoder-only, RMSEA\\,=\\,0.08), the within-family confound overlap of 0.47 means nearly half of detected DIF reflects capability growth rather than contamination.\n\n\\paragraph{The detection trilemma.}\nOur results reveal a three-way trade-off: (1) adequate IRT fit requires homogeneous subpopulations, (2) statistical power requires large sample sizes, and (3) confound control requires known-clean within-family comparisons. No single analysis can simultaneously satisfy all three. Architecture stratification addresses (1) but sacrifices (2); within-family analysis addresses (3) but with small $N$; the full population maximizes (2) but violates (1).\n\n\\paragraph{Simulation overestimates real-world performance.}\nThe consistent $\\sim$43\\% simulation-to-reality gap is perhaps our most broadly applicable finding. Any contamination detection method validated solely through simulation should expect comparable degradation when applied to real response matrices. This gap arises from structural properties of real evaluation data (non-random missingness, ceiling/floor effects, architecture clustering) that are absent from standard simulation frameworks.\n\n\\paragraph{Methodological contributions.}\nDespite the negative empirical results, we contribute three reusable methodological tools: (1) the confound-separation analysis via within-family DIF provides a template for distinguishing contamination from capability in any detection framework; (2) the semi-synthetic validation protocol offers controlled ground truth superior to existing proxies; (3) the graceful degradation framework quantifies the cost of imperfect item replacement for any regeneration approach.\n\n\\paragraph{Implications for the community.}\nOur findings suggest that item-level contamination detection from behavioral response patterns alone may be fundamentally limited when the ``examinee'' population is architecturally heterogeneous and rapidly evolving. Future detection methods should either (a) incorporate training data access (moving beyond black-box detection), (b) exploit format-specific signals beyond binary correct/incorrect (\\eg, chain-of-thought analysis), or (c) design benchmarks with built-in contamination resistance (\\eg, procedurally generated items with known difficulty functions).\n\n%% ============================================================\n%% 6. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe set out to build a psychometric contamination detection and benchmark regeneration framework, and instead produced the first large-scale empirical evidence for why this is harder than the community has assumed. Across 5,219 models and 12,508 MMLU items, we demonstrate that: (1) classical IRT assumptions are catastrophically violated in heterogeneous LLM populations; (2) DIF-based contamination signals are inseparable from capability growth signals, with 62\\% confound overlap; (3) all existing detection paradigms---DIF, perturbation testing, generation variance, and their ensemble---fail to achieve reliable detection, with the best configuration reaching 0.48 TPR at $\\delta \\geq 1.4$; (4) the $\\sim$43\\% simulation-to-reality gap means published power analyses substantially overestimate real-world performance; and (5) bifactor equating and item regeneration are not yet feasible at scale.\n\nThese negative results are themselves a contribution: they set realistic expectations for contamination detection, provide diagnostic tools for understanding detection failures, and offer a semi-synthetic validation framework for evaluating future approaches. The path forward likely requires moving beyond behavioral response patterns to richer signal sources---or fundamentally rethinking how we design benchmarks for an era where the distinction between ``learning'' and ``memorizing'' is increasingly blurred.\n\n%% ============================================================\n%% REFERENCES\n%% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Duan et~al.(2024)]{duan2024dvd}\nDuan, H., et~al.\n\\newblock Do membership inference attacks work on large language models?\n\\newblock In \\emph{Proceedings of ACL}, 2024.\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nDekoninck, J., et~al.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In \\emph{Proceedings of NeurIPS}, 2024.\n\n\\bibitem[Holland \\& Thayer(1988)]{holland1988dif}\nHolland, P.~W. and Thayer, D.~T.\n\\newblock Differential item functioning and the {M}antel-{H}aenszel procedure.\n\\newblock \\emph{Test Validity}, 129--145, 1988.\n\n\\bibitem[Lalor et~al.(2019)]{lalor2019learning}\nLalor, J.~P., Wu, H., and Yu, H.\n\\newblock Learning latent parameters without human response patterns: Item response theory with artificial crowds.\n\\newblock In \\emph{Proceedings of EMNLP}, 2019.\n\n\\bibitem[Roberts et~al.(2026)]{roberts2026growing}\nRoberts, B., et~al.\n\\newblock Growing pains: Multidimensional {IRT} for extensible {LLM} evaluation.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nShi, W., et~al.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{Proceedings of ICLR}, 2024.\n\n\\bibitem[Sinharay et~al.(2006)]{sinharay2006bayesian}\nSinharay, S., Dorans, N.~J., and Liang, L.\n\\newblock A {B}ayesian approach to evaluating the stability of DIF statistics.\n\\newblock \\emph{ETS Research Report Series}, 2006.\n\n\\bibitem[Tutz \\& Berger(2016)]{tutz2016ift}\nTutz, G. and Berger, M.\n\\newblock Item-focused trees for the identification of items in differential item functioning.\n\\newblock \\emph{Psychometrika}, 81(3):727--750, 2016.\n\n\\bibitem[Wang et~al.(2026)]{wang2026rl}\nWang, Z., et~al.\n\\newblock Contamination detection fails under reinforcement learning.\n\\newblock In \\emph{Proceedings of ICLR}, 2026.\n\n\\bibitem[White et~al.(2024)]{white2024livebench}\nWhite, C., et~al.\n\\newblock LiveBench: A challenging, contamination-free {LLM} benchmark.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Zhu et~al.(2024)]{zhu2024dyval}\nZhu, K., et~al.\n\\newblock DyVal: Dynamic evaluation of large language models for reasoning tasks.\n\\newblock In \\emph{Proceedings of ICLR}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "c08d87b0-7707-4d74-b835-1db5910a174c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T205007 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "17f405e7-197e-4fbc-ae86-d747d4ec3252",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream_20260520T205007",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731"
}
```

---

### Assistant

_source line 22 · 2026-05-20T21:26:19.997Z_

Now compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17f405e7-197e-4fbc-ae86-d747d4ec3252",
  "isSidechain": false,
  "requestId": "req_011CbEXaX7Bzg44Cvc3pU4EQ",
  "type": "assistant",
  "uuid": "f0b7f930-3ea6-4f22-b823-37ec4adbc2ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ga5dQVV3i6VjXknpFWcQNf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14677,
      "cache_read_input_tokens": 44388,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14677,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 44388,
          "cache_creation_input_tokens": 14677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14677
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

_source line 23 · 2026-05-20T21:26:21.199Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015TFzZj1NjxQu5u63efAz1R`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0b7f930-3ea6-4f22-b823-37ec4adbc2ac",
  "isSidechain": false,
  "requestId": "req_011CbEXaX7Bzg44Cvc3pU4EQ",
  "type": "assistant",
  "uuid": "eddb89d5-9ab8-4d3a-a627-39696ebdcc35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ga5dQVV3i6VjXknpFWcQNf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14677,
      "cache_read_input_tokens": 44388,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14677,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 44388,
          "cache_creation_input_tokens": 14677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14677
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

_source line 24 · 2026-05-20T21:26:22.326Z_

<details><summary>↩ Tool result · `toolu_015TFzZj1NjxQu5u63efAz1R`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty
(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)
(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu
t line 60.


Package natbib Warning: Citation `lalor2019learning' on page 2 undefined on inp
ut line 64.

[2]

LaTeX Warning: Reference `tab:arch_strat' on page 3 undefined on input line 133
.

[3]

LaTeX Warning: Reference `tab:within_family' on page 4 undefined on input line 
191.


LaTeX Warning: `h' float specifier changed to `ht'.

[4]

LaTeX Warning: Reference `tab:ift' on page 5 undefined on input line 214.


LaTeX Warning: Reference `tab:partial_exploit' on page 5 undefined on input lin
e 257.

[5]

LaTeX Warning: Reference `tab:perturb_quality' on page 6 undefined on input lin
e 301.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[6]

LaTeX Warning: Reference `tab:signal_corr' on page 7 undefined on input line 35
9.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[7]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[8]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[9]

LaTeX Warning: `h' float specifier changed to `ht'.

[10] [11]

Package natbib Warning: There were undefined citations.

[12] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>
Output written on paper.pdf (12 pages, 253531 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty
(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)
(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))
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
nts/map/pdftex/updmap/pdftex.map}] [2] [3]

LaTeX Warning: `h' float specifier changed to `ht'.

[4] [5]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[6]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[7]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[8]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[9]

LaTeX Warning: `h' float specifier changed to `ht'.

[10] [11] [12] (./paper.aux) )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi5.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti
10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>

Output written on paper.pdf (12 pages, 255868 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eddb89d5-9ab8-4d3a-a627-39696ebdcc35",
  "isSidechain": false,
  "promptId": "7a9370c0-2bc7-4d59-8649-7bea7feea208",
  "type": "user",
  "uuid": "412d1317-664d-44de-b99a-f1b495758d9c",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty\n(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu\nt line 60.\n\n\nPackage natbib Warning: Citation `lalor2019learning' on page 2 undefined on inp\nut line 64.\n\n[2]\n\nLaTeX Warning: Reference `tab:arch_strat' on page 3 undefined on input line 133\n.\n\n[3]\n\nLaTeX Warning: Reference `tab:within_family' on page 4 undefined on input line \n191.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4]\n\nLaTeX Warning: Reference `tab:ift' on page 5 undefined on input line 214.\n\n\nLaTeX Warning: Reference `tab:partial_exploit' on page 5 undefined on input lin\ne 257.\n\n[5]\n\nLaTeX Warning: Reference `tab:perturb_quality' on page 6 undefined on input lin\ne 301.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6]\n\nLaTeX Warning: Reference `tab:signal_corr' on page 7 undefined on input line 35\n9.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[10] [11]\n\nPackage natbib Warning: There were undefined citations.\n\n[12] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr\n7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>\nOutput written on paper.pdf (12 pages, 253531 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty\n(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2] [3]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4] [5]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[10] [11] [12] (./paper.aux) )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi5.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti\n10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>\n\nOutput written on paper.pdf (12 pages, 255868 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "eddb89d5-9ab8-4d3a-a627-39696ebdcc35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T205007 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "412d1317-664d-44de-b99a-f1b495758d9c",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream_20260520T205007",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731"
}
```

---

### Assistant

_source line 27 · 2026-05-20T21:26:31.047Z_

编译成功，12页PDF，无错误。

论文已写入 `worst/paper.tex` 并编译为 `paper.pdf`。覆盖了全部11个实验的23张表，按 reframe 叙事组织：从IRT模型拟合失败→DIF混淆分析→RL鲁棒性→替代检测器(ConStat/DVD)→集成融合→跨benchmark验证→semi-synthetic验证→bifactor等值→项目生成→累积贝叶斯DIF→graceful degradation。核心claim从"我们能检测污染"转向"我们证明了为什么检测比社区认为的更难"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "412d1317-664d-44de-b99a-f1b495758d9c",
  "isSidechain": false,
  "requestId": "req_011CbEXashCAtjnZmZ1SRzmy",
  "type": "assistant",
  "uuid": "6a826bb8-197b-47c9-b266-66d78052cf3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fxbr8VsZwAPzZTLT5CcSAE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6562,
      "cache_read_input_tokens": 59065,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6562,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 59065,
          "cache_creation_input_tokens": 6562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6562
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T205007 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "6a826bb8-197b-47c9-b266-66d78052cf3b",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream_20260520T205007",
  "sessionId": "14a5cd0b-7880-4b7c-a2e7-09d9a70e7731"
}
```

---
