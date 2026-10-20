# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T165710 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/2139658a-dd10-4943-bdfb-7044b07d629e.jsonl`
- **Structured JSON:** [`09d93e537e5d296fbb0b.json`](../../sessions/09/09d93e537e5d296fbb0b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T17:28:37.542Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T17:28:37.542Z",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T165710 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：放弃psychometric measurement drift framing。Reframe为纯empirical characterization paper： 'Large-Scale Item-Level Stability Analysis of LLM Benchmarks'。MH statistic降级为nonparametric group-comparison test，不依赖latent trait interpretation。Semi-synthetic framework成为anchor contribution。Item-level stability定位为benchmark maintenance的operational metric。 Permutation null揭示temporal label assignment本身引入12-20%的spurious C%，31%中大量来自 cohort composition而非genuine item drift。RL robustness失败进一步削弱DIF作为stable detector 的叙事。8页内必须同时容纳reframing叙事和精简后的实验——需重构论文结构。 审稿人collective rejection预期：98% IRT misfit + unidimensional assumption on 57-subject benchmark = 'MH-DIF results are uninterpretable without multidimensional IRT'。 Ground truth meta-critique被驳为straw man。Ability confound的2.4pp被认为低估。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T17:28:37.545Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T17:28:37.545Z",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-21T17:28:37.567Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T165710 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：放弃psychometric measurement drift framing。Reframe为纯empirical characterization paper： 'Large-Scale Item-Level Stability Analysis of LLM Benchmarks'。MH statistic降级为nonparametric group-comparison test，不依赖latent trait interpretation。Semi-synthetic framework成为anchor contribution。Item-level stability定位为benchmark maintenance的operational metric。 Permutation null揭示temporal label assignment本身引入12-20%的spurious C%，31%中大量来自 cohort composition而非genuine item drift。RL robustness失败进一步削弱DIF作为stable detector 的叙事。8页内必须同时容纳reframing叙事和精简后的实验——需重构论文结构。 审稿人collective rejection预期：98% IRT misfit + unidimensional assumption on 57-subject benchmark = 'MH-DIF results are uninterpretable without multidimensional IRT'。 Ground truth meta-critique被驳为straw man。Ability confound的2.4pp被认为低估。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9377956b-ace9-4b16-82d2-21e10f437ea9",
  "type": "user",
  "uuid": "1ac0360c-abaa-4432-bcd4-d306665b499f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T17:28:37.566Z_

```json
{
  "parentUuid": "1ac0360c-abaa-4432-bcd4-d306665b499f",
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
  "uuid": "33a7734a-5b4d-4555-8d80-c0aaf7441439",
  "timestamp": "2026-05-21T17:28:37.566Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T17:28:37.566Z_

```json
{
  "parentUuid": "33a7734a-5b4d-4555-8d80-c0aaf7441439",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "34393cc0-0c1f-417e-b623-1656f7d2ca7b",
  "timestamp": "2026-05-21T17:28:37.566Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream benchmark analysis",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e"
}
```

---

### Assistant

_source line 7 · 2026-05-21T17:28:40.484Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34393cc0-0c1f-417e-b623-1656f7d2ca7b",
  "isSidechain": false,
  "requestId": "req_011CbG7GH15mc1WvkoytLM4k",
  "type": "assistant",
  "uuid": "2d53ba11-b34a-4fc2-a9e0-3f22409f8fa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELNmHyYPyneLSFSQJfhgiw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12411,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12411,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12411
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

_source line 8 · 2026-05-21T17:28:41.434Z_

<details open><summary>🔧 Tool call — Read · `toolu_014dvsFKv5PGFGvyWV2sRD5m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d53ba11-b34a-4fc2-a9e0-3f22409f8fa0",
  "isSidechain": false,
  "requestId": "req_011CbG7GH15mc1WvkoytLM4k",
  "type": "assistant",
  "uuid": "010fc2ec-8285-48a3-824c-92a9612a9a3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELNmHyYPyneLSFSQJfhgiw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12411,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12411,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12411
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

_source line 9 · 2026-05-21T17:28:41.733Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MJPwY7nMUevAJJ6MX4v6LX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "010fc2ec-8285-48a3-824c-92a9612a9a3d",
  "isSidechain": false,
  "requestId": "req_011CbG7GH15mc1WvkoytLM4k",
  "type": "assistant",
  "uuid": "9dd1829e-4203-4d8b-b70c-ae1fec16e090",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELNmHyYPyneLSFSQJfhgiw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12411,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12411,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12411
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

_source line 10 · 2026-05-21T17:28:41.795Z_

<details><summary>↩ Tool result · `toolu_014dvsFKv5PGFGvyWV2sRD5m`</summary>

```text
1	[
2	  {
3	    "name": "real_data_dif_mmlu",
4	    "description": "Apply MH-DIF to METABENCH MMLU response matrix (5,219 models × 12,508 items). Temporal cohort (2023 vs 2024-H1), ability-quintile cohort, within-family confound control, domain-specificity analysis.\n",
5	    "results": {
6	      "temporal_ets_c_pct": 31.3,
7	      "temporal_fpr_li_clean": 0.322,
8	      "temporal_enrichment": 0.96,
9	      "ability_ets_c_pct": 2.9,
10	      "ability_enrichment": 1.19,
11	      "within_family_llama2v3_c_pct": 61.3,
12	      "within_family_mistral_mixtral_c_pct": 38.7,
13	      "domain_spearman_rho": 0.307,
14	      "domain_spearman_p": 0.02,
15	      "sanity_random_split_c_pct": 0.18,
16	      "temporal_ability_jaccard": 0.014,
17	      "irt_misfit_pct_lz_gt2": 98.2,
18	      "permutation_null_c_pct_posterior": 16.4,
19	      "effective_c_pct_after_permutation_control": 14.9,
20	      "domain_specificity_chi2_p": 0.78,
21	      "negative_disc_items_sensitivity": "removing 15.4% neg-disc items reduces C% by only 1.2pp"
22	    },
23	    "tables": [
24	      {
25	        "title": "Table 1: Temporal DIF Summary (Worst-Tier Interpretation)",
26	        "columns": [
27	          "metric",
28	          "raw_value",
29	          "after_permutation_control",
30	          "reviewer_interpretation"
31	        ],
32	        "rows": [
33	          [
34	            "C%",
35	            "31.3%",
36	            "14.9% (31.3 - 16.4 null)",
37	            "inflated by cohort composition"
38	          ],
39	          [
40	            "enrichment_vs_Li",
41	            0.96,
42	            0.96,
43	            "trivially expected, not informative"
44	          ],
45	          [
46	            "IRT_misfit",
47	            "98% |Lz|>2",
48	            "N/A",
49	            "renders MH conditioning unreliable"
50	          ],
51	          [
52	            "domain_rho",
53	            0.307,
54	            "N/A",
55	            "ecological fallacy on N=57"
56	          ],
57	          [
58	            "within_family_C%",
59	            "38.7-61.3%",
60	            "N/A",
61	            "confounded by architecture change"
62	          ]
63	        ]
64	      },
65	      {
66	        "title": "Table 2: Cohort Definition × Item Filtering Sensitivity",
67	        "columns": [
68	          "cohort",
69	          "filter",
70	          "c_pct",
71	          "effective_c_pct"
72	        ],
73	        "rows": [
74	          [
75	            "temporal",
76	            "all_items",
77	            31.3,
78	            14.9
79	          ],
80	          [
81	            "temporal",
82	            "no_neg_disc",
83	            30.1,
84	            13.7
85	          ],
86	          [
87	            "ability",
88	            "all_items",
89	            2.9,
90	            "N/A"
91	          ],
92	          [
93	            "ability",
94	            "no_neg_disc",
95	            2.7,
96	            "N/A"
97	          ]
98	        ]
99	      }
100	    ],
101	    "figures": [],
102	    "analysis": "在worst档下，plan_001的核心结果从\"31% instability is genuine and robust\"变为 \"31% raw C%中约一半来自cohort composition artifacts\"。这不是statistical artifact （random split仍为0.18%），而是temporal label本身proxy了多个未控制confound。 Reframing策略：不再claim \"31% items show genuine measurement drift\"，而是 \"we observe 31% item-level behavioral heterogeneity between temporal cohorts, of which 10-18% persists after permutation controls — we characterize this heterogeneity without claiming psychometric interpretation\"。\n\n\n表面数字与registry一致（31.3% C%），但在worst档下，plan_029的permutation null将揭示 temporal label assignment本身产生~16.4%的spurious C%——即随机打乱2023/2024标签后， 仅因cohort composition差异（ability distribution shift d=-0.17, model family结构差异, training data vintage差异）就能产生大量MH-DIF flags。这意味着31.3%中仅约14.9% 可归因于genuine item-level behavioral change。Within-family分析（Llama-2v3 C%=61.3%） 本应作为confound control，但在worst档下审稿人指出：Llama-2→3不是单纯temporal shift， 而是architecture+data+training全面重构，within-family DIF不能isolate contamination。 Domain specificity的ρ=0.307被审稿人dismisses为ecological correlation on N=57 subjects， 无item-level causal interpretation。98%的IRT misfit（|Lz|>2）在worst档下不再被接受为 \"reflects multidimensionality, discuss in limitations\"——审稿人要求multidimensional IRT 作为前提条件，否则MH-DIF结果uninterpretable。Enrichment≈1.0依然成立但被重新解读： \"当然web-overlap和DIF不相关，这不是discovery而是trivially expected\"。\n"
103	  },
104	  {
105	    "name": "rl_robustness_validation",
106	    "description": "Validate DIF robustness to reasoning-RL models. Add 10-15 GRPO/PPO models to focal cohort; measure DIF flag stability. Compare traditional detectors (Min-K%, ConStat) on RL models individually.\n",
107	    "results": {
108	      "baseline_temporal_c_pct": 31.3,
109	      "with_alignment_rl_c_pct": 29.8,
110	      "with_reasoning_rl_c_pct": 24.1,
111	      "jaccard_baseline_vs_alignment_rl": 0.82,
112	      "jaccard_baseline_vs_reasoning_rl": 0.43,
113	      "jaccard_alignment_vs_reasoning_rl": 0.48,
114	      "traditional_mink_auroc_base": 0.71,
115	      "traditional_mink_auroc_rl": 0.68,
116	      "traditional_constat_auroc_base": 0.65,
117	      "traditional_constat_auroc_rl": 0.62,
118	      "auroc_drop_mink": 0.03,
119	      "auroc_drop_constat": 0.03,
120	      "delong_p_mink": 0.34,
121	      "delong_p_constat": 0.41,
122	      "tost_equivalence_p": 0.08,
123	      "n_reasoning_rl_models": 13,
124	      "power_analysis_delta_boundary": 1.8,
125	      "bootstrap_ci_jaccard_rl": [
126	        0.31,
127	        0.54
128	      ]
129	    },
130	    "tables": [
131	      {
132	        "title": "Table 3: DIF Flag Stability Under Cohort Composition Changes",
133	        "columns": [
134	          "comparison",
135	          "jaccard",
136	          "c_pct_shift",
137	          "interpretation"
138	        ],
139	        "rows": [
140	          [
141	            "baseline vs +alignment-RL",
142	            0.82,
143	            "-1.5pp",
144	            "stable (DPO/ORPO不影响)"
145	          ],
146	          [
147	            "baseline vs +reasoning-RL",
148	            0.43,
149	            "-7.2pp",
150	            "UNSTABLE — flags shift fundamentally"
151	          ],
152	          [
153	            "alignment-RL vs reasoning-RL",
154	            0.48,
155	            "-5.7pp",
156	            "RL type matters more than temporal split"
157	          ]
158	        ]
159	      },
160	      {
161	        "title": "Table 4: Traditional Detector AUROC Comparison",
162	        "columns": [
163	          "detector",
164	          "auroc_base",
165	          "auroc_rl",
166	          "delta",
167	          "delong_p"
168	        ],
169	        "rows": [
170	          [
171	            "Min-K%",
172	            0.71,
173	            0.68,
174	            -0.03,
175	            0.34
176	          ],
177	          [
178	            "ConStat",
179	            0.65,
180	            0.62,
181	            -0.03,
182	            0.41
183	          ],
184	          [
185	            "MH-DIF",
186	            "N/A",
187	            "N/A",
188	            "Jaccard=0.43",
189	            "N/A"
190	          ]
191	        ]
192	      }
193	    ],
194	    "figures": [],
195	    "analysis": "RL robustness实验在worst档下彻底失败。Jaccard<0.55意味着DIF不能被视为cohort-invariant detector。审稿人的解读：\"如果改变cohort中13个模型就导致43%的flag翻转，那DIF测量的 不是item property而是cohort property——这与psychometric DIF的理论前提矛盾\"。 Reframing下这变为：\"we acknowledge DIF flags are cohort-dependent — our characterization is specific to the 2023-vs-2024 temporal split and should not be extrapolated to arbitrary cohort definitions\"。这大幅削弱了generalizability claim。\n\n\n在worst档下，reasoning-RL模型加入focal cohort后，DIF flags大幅shift（Jaccard=0.43, 远低于0.8的stability阈值）。原因：reasoning-RL模型（DeepSeek-R1, Qwen2.5-RL等） 的response pattern与标准decoder-only模型本质不同——它们在chain-of-thought后达到答案， item difficulty profile完全改变。MH-DIF的ability conditioning基于total score， 但reasoning-RL模型的total score来源（deliberate reasoning vs memorization）与 传统模型不同，导致conditioning variable被confound。C%从31.3%降至24.1%——不是因为 RL模型\"更干净\"，而是因为cohort composition shift改变了哪些items被flag。 传统detectors的AUROC drop很小（0.03），审稿人据此argue：\"DIF对cohort composition 敏感而传统方法不敏感，说明DIF的sensitivity实际上是instability的体现\"。 TOST equivalence test borderline不通过（p=0.08），无法claim DIF和传统方法等效。 N=13 reasoning-RL模型本身就是underpowered的——worst档下这被视为fatal flaw， 不是\"supplementary\"而是\"insufficient to support any RL robustness claim\"。\n"
196	  },
197	  {
198	    "name": "constat_perturbation_eval",
199	    "description": "Independent evaluation of ConStat perturbation testing on MMLU: generate reformulations for 200+ items, compare performance, apply FDR-controlled detection.\n",
200	    "results": {
201	      "n_items_reformulated": 237,
202	      "constat_detection_rate_non_rl": 0.24,
203	      "constat_detection_rate_rl": 0.09,
204	      "constat_fpr": 0.06,
205	      "constat_auroc_non_rl": 0.72,
206	      "constat_auroc_rl": 0.54,
207	      "reformulation_quality_score": 0.83,
208	      "semantic_equivalence_verified": 0.91,
209	      "fdr_threshold_q005": 0.048,
210	      "constat_vs_dif_overlap_jaccard": 0.15,
211	      "constat_unique_detections": 47,
212	      "dif_unique_detections": 312
213	    },
214	    "tables": [
215	      {
216	        "title": "Table 5: ConStat Detection Performance",
217	        "columns": [
218	          "model_type",
219	          "n_models",
220	          "detection_rate",
221	          "auroc",
222	          "fpr"
223	        ],
224	        "rows": [
225	          [
226	            "non-RL",
227	            50,
228	            0.24,
229	            0.72,
230	            0.06
231	          ],
232	          [
233	            "alignment-RL",
234	            30,
235	            0.18,
236	            0.64,
237	            0.07
238	          ],
239	          [
240	            "reasoning-RL",
241	            13,
242	            0.09,
243	            0.54,
244	            0.05
245	          ]
246	        ]
247	      }
248	    ],
249	    "figures": [],
250	    "analysis": "ConStat实验结果本身是informative的，但在worst档下strengthens审稿人argument： item-level contamination detection整个领域缺乏construct validity——不同方法测量 不同东西，没有ground truth能判断谁对。这支持reframe到pure characterization paper。\n\n\nConStat在non-RL模型上表现合理（AUROC=0.72），在RL模型上大幅衰减（0.54，接近random）。 但在worst档下，关键问题不是ConStat表现如何，而是ConStat和DIF的detection overlap极低 （Jaccard=0.15）。审稿人解读：\"两个声称检测同一现象的方法几乎不flag同一批items， 说明它们测量的是不同东西——或者至少一个在测量artifact\"。ConStat的47个unique detections 中包含一些DIF完全miss的真实contamination cases（通过reformulation验证）， 削弱了DIF作为primary detector的positioning。在reframed paper中，ConStat结果 降级为appendix baseline comparison，不再用于ensemble narrative（已dropped）。\n"
251	  },
252	  {
253	    "name": "dvd_generation_variance_eval",
254	    "description": "Independent evaluation of DVD generation variance on MMLU: 50 responses per item via temperature sampling on 10-15 models, detect bimodal distributions.\n",
255	    "results": {
256	      "n_models_tested": 12,
257	      "n_items_sampled": 500,
258	      "responses_per_item": 50,
259	      "temperature": 0.8,
260	      "dvd_detection_rate": 0.18,
261	      "dvd_auroc": 0.61,
262	      "dvd_fpr": 0.08,
263	      "bimodal_items_detected": 43,
264	      "dvd_vs_dif_jaccard": 0.11,
265	      "dvd_vs_constat_jaccard": 0.19,
266	      "variant_contamination_coverage": 0.31,
267	      "verbatim_contamination_coverage": 0.07,
268	      "gpu_hours_used": 58
269	    },
270	    "tables": [
271	      {
272	        "title": "Table 6: DVD Detection Summary",
273	        "columns": [
274	          "metric",
275	          "value"
276	        ],
277	        "rows": [
278	          [
279	            "AUROC",
280	            0.61
281	          ],
282	          [
283	            "detection_rate",
284	            0.18
285	          ],
286	          [
287	            "FPR",
288	            0.08
289	          ],
290	          [
291	            "bimodal_items",
292	            43
293	          ],
294	          [
295	            "overlap_with_DIF (Jaccard)",
296	            0.11
297	          ],
298	          [
299	            "overlap_with_ConStat (Jaccard)",
300	            0.19
301	          ]
302	        ]
303	      }
304	    ],
305	    "figures": [],
306	    "analysis": "DVD结果在worst档下直接支持Claim 2的meta-critique（不同方法测量不同东西）， 但ironically也削弱了paper自身的DIF-centric positioning。Reframed paper中， DVD和ConStat结果用一段话提及作为\"multiple lenses on item heterogeneity\"的evidence， 不再pursuit ensemble fusion。\n\n\nDVD在worst档下表现中等偏弱（AUROC=0.61）。Generation variance信号在LLM上比human testing更noisy——temperature sampling的response分布本身就是multimodal的（model confidence varies by item type, not just contamination）。DVD与DIF的overlap更低 （Jaccard=0.11），三个方法三个不同的item set。在worst档下，这个三方disagreement 成为审稿人最强的论据之一：\"when three independent detectors flag almost entirely different items, the field has a construct validity crisis, not a contamination detection toolbox\"。DVD的variant contamination coverage（0.31）比verbatim（0.07） 好得多，确认它确实测量不同phenomenon，但这恰恰支持meta-critique而非ensemble narrative。\n"
307	  },
308	  {
309	    "name": "ensemble_fusion",
310	    "description": "Fuse DIF + ConStat + DVD into multi-signal ensemble. Calibrate thresholds, evaluate voting and weighted fusion, report coverage and precision.\n",
311	    "results": {
312	      "ensemble_attempted": true,
313	      "ensemble_viable": false,
314	      "majority_vote_auroc": 0.58,
315	      "weighted_fusion_auroc": 0.63,
316	      "ensemble_fpr": 0.14,
317	      "cross_val_weight_instability": "weights flip sign across folds",
318	      "uniform_weight_auroc": 0.6,
319	      "pairwise_signal_correlation_dif_constat": 0.09,
320	      "pairwise_signal_correlation_dif_dvd": 0.06,
321	      "pairwise_signal_correlation_constat_dvd": 0.13,
322	      "coverage_analysis": "DIF covers 31%, ConStat 24%, DVD 18% — but only 4% in all three",
323	      "decision": "killed"
324	    },
325	    "tables": [],
326	    "figures": [],
327	    "analysis": "Ensemble killed。在reframed paper中不提及。三方法disagreement作为meta-critique的 additional evidence在Discussion一句话提及。\n\n\nEnsemble fusion在worst档下被kill。三个信号之间的correlation极低（0.06-0.13）， 意味着它们不是measuring同一construct的noisy estimators，而是measuring不同constructs。 Majority vote AUROC（0.58）甚至低于单个最佳detector（ConStat 0.72 on non-RL）， 因为vote要求agreement但signals几乎不agree。Weighted fusion cross-validation 显示权重在folds间高度不稳定（某些fold中DIF权重为负），表明没有stable fusion function。 FPR=0.14 borderline超过0.10 target。在worst档下，ensemble failure不是简单的 \"negative result\"——它是对整个contamination detection paradigm的existential challenge。 Paper中完全删除ensemble narrative，连appendix都不保留。\n"
328	  },
329	  {
330	    "name": "cross_benchmark_gsm8k",
331	    "description": "Replicate DIF analysis on GSM8K using GSM1K as ground truth. Temporal DIF, semi-synthetic validation, GSM1K contamination gap correlation.\n",
332	    "results": {
333	      "gsm8k_n_items": 1319,
334	      "gsm8k_n_ref": 1017,
335	      "gsm8k_n_foc": 804,
336	      "gsm8k_temporal_c_pct": 12.4,
337	      "gsm8k_external_c_pct": 38.1,
338	      "gsm8k_sanity_c_pct": 0.3,
339	      "gsm8k_permutation_null_c_pct": 8.7,
340	      "gsm8k_effective_c_pct": 3.7,
341	      "semi_synthetic_delta_tpr_standard_p10": 0.38,
342	      "semi_synthetic_delta_tpr_external_p10": 0.27,
343	      "gsm1k_correlation_n": 33,
344	      "gsm1k_pearson_r": -0.29,
345	      "gsm1k_pearson_p": 0.1,
346	      "gsm1k_spearman_rho": -0.22,
347	      "gsm1k_spearman_p": 0.21,
348	      "gsm1k_partial_r": -0.18,
349	      "gsm1k_partial_p": 0.32,
350	      "gsm1k_ci_upper": 0.06,
351	      "direction": "still negative but non-significant"
352	    },
353	    "tables": [
354	      {
355	        "title": "Table 7: Cross-Benchmark DIF Comparison (Worst Tier)",
356	        "columns": [
357	          "benchmark",
358	          "raw_c_pct",
359	          "permutation_null",
360	          "effective_c_pct",
361	          "interpretation"
362	        ],
363	        "rows": [
364	          [
365	            "MMLU",
366	            31.3,
367	            16.4,
368	            14.9,
369	            "moderate signal after controls"
370	          ],
371	          [
372	            "GSM8K",
373	            12.4,
374	            8.7,
375	            3.7,
376	            "near noise floor"
377	          ]
378	        ]
379	      },
380	      {
381	        "title": "Table 8: GSM1K Correlation Under Worst Tier",
382	        "columns": [
383	          "metric",
384	          "value",
385	          "ci_95",
386	          "p_value"
387	        ],
388	        "rows": [
389	          [
390	            "Pearson r",
391	            -0.29,
392	            "[-0.58, 0.06]",
393	            0.1
394	          ],
395	          [
396	            "Spearman ρ",
397	            -0.22,
398	            "[-0.53, 0.14]",
399	            0.21
400	          ],
401	          [
402	            "Partial r",
403	            -0.18,
404	            "[-0.50, 0.19]",
405	            0.32
406	          ]
407	        ]
408	      }
409	    ],
410	    "figures": [],
411	    "analysis": "GSM8K结果在worst档下严重削弱cross-benchmark generalizability claim。Effective C%=3.7% 意味着GSM8K上几乎没有genuine item-level DIF。Reframed paper中，GSM8K从\"cross-benchmark validation\"降级为\"the method produces different results on different benchmarks — this heterogeneity itself is worth characterizing\"。GSM1K correlation完全dropped from claims。\n\n\nGSM8K在worst档下表现远弱于MMLU。Temporal C%仅12.4%（worst档cross_benchmark_c_pct_min 范围8-14%），扣除permutation null（8.7%）后effective C%仅3.7%——接近noise floor。 原因：GSM8K是single-domain math benchmark，items之间homogeneity更高，temporal cohort间的ability差异更直接映射到item difficulty（math能力提升→所有items变容易）， MH的ability conditioning更有效地absorb了这个effect。但也可能是GSM8K确实更stable。 Semi-synthetic ΔTPR显著降低（worst档0.25-0.4范围），因为smaller item pool（1319 vs 12508） 导致power降低，且single-domain matching variable更noisy。 GSM1K correlation从registry的-0.478(p=0.005)恶化到-0.29(p=0.10)——在worst档下 N=33太小，置信区间覆盖zero。审稿人判定：\"N=33 with CI crossing zero is not evidence for anything\"。Direction仍为negative（与contamination hypothesis相反）， 但在worst档下这被视为\"noise, not signal\"。GSM1K分析降级为appendix exploratory。\n"
412	  },
413	  {
414	    "name": "bifactor_irt_equating_pilot",
415	    "description": "Pilot bifactor IRT equating on MMLU: fit bifactor model, select anchor items, fixed-parameter calibration of replacements, demonstrate equated score equivalence.\n",
416	    "results": {
417	      "bifactor_convergence": false,
418	      "bifactor_attempts": 3,
419	      "bifactor_rmsea": 0.089,
420	      "bifactor_cfi": 0.72,
421	      "bifactor_tli": 0.69,
422	      "bifactor_srmr": 0.11,
423	      "fallback_2pl_rmsea": 0.094,
424	      "fallback_2pl_cfi": 0.68,
425	      "anchor_item_selection_possible": false,
426	      "equated_rho": null,
427	      "decision": "killed",
428	      "reason": "bifactor model fails to converge on 12508×5219 matrix; even when forced, fit indices far below acceptable thresholds"
429	    },
430	    "tables": [
431	      {
432	        "title": "Table 9: IRT Model Fit Comparison",
433	        "columns": [
434	          "model",
435	          "rmsea",
436	          "cfi",
437	          "tli",
438	          "srmr",
439	          "converged"
440	        ],
441	        "rows": [
442	          [
443	            "unidimensional 2PL",
444	            0.094,
445	            0.68,
446	            0.65,
447	            0.12,
448	            "yes (poor fit)"
449	          ],
450	          [
451	            "bifactor (57 specific)",
452	            0.089,
453	            0.72,
454	            0.69,
455	            0.11,
456	            "no (forced)"
457	          ],
458	          [
459	            "acceptable thresholds",
460	            "<0.06",
461	            ">0.95",
462	            ">0.95",
463	            "<0.08",
464	            "N/A"
465	          ]
466	        ]
467	      }
468	    ],
469	    "figures": [],
470	    "analysis": "Bifactor failure是worst档的defining event之一。它证实了审稿人的核心concern： MMLU的57-subject structure使得any IRT model都是misspecified的。但在reframed paper中， 这反而成为strength：我们explicitly acknowledge IRT assumptions violated， 所以我们不依赖IRT interpretation——MH作为nonparametric χ² test不需要IRT model fit。 Bifactor结果在limitations section作为\"we attempted and it failed\"报告。\n\n\nBifactor IRT在worst档下完全失败。12,508 items × 57 subjects的bifactor model （1 general + 57 specific factors）有>25,000 parameters，在5,219 models上 severely overparameterized。Convergence failure after 3 attempts with different starting values和estimation methods（MHRM, EM, QN）。即使forced convergence 的fit indices（RMSEA=0.089, CFI=0.72）远低于acceptable thresholds（RMSEA<0.06, CFI>0.95）。这directly confirms审稿人的核心concern：\"unidimensional IRT assumption severely violated, and bifactor doesn't rescue it because the item-to-model ratio is too small for the factor structure\"。Anchor item selection不可能——没有reliable parameter estimates。Equating pilot killed。在worst档下这是paper最致命的finding之一： 不仅unidimensional IRT不work，连multidimensional IRT也不work on this data。 Reframing response：完全放弃IRT-based interpretation，将MH当作nonparametric test。\n"
471	  },
472	  {
473	    "name": "item_generation_calibration",
474	    "description": "Generate replacement items for DIF-flagged MMLU questions via LLM generation with construct constraints. Calibrate via student simulation.\n",
475	    "results": {
476	      "n_items_generated": 200,
477	      "n_items_quality_filtered": 142,
478	      "difficulty_correlation_prompt_based": 0.18,
479	      "difficulty_correlation_student_sim": 0.41,
480	      "difficulty_correlation_target": 0.75,
481	      "construct_alignment_score": 0.64,
482	      "replacement_equating_rho": 0.88,
483	      "replacement_equating_target": 0.95,
484	      "student_sim_correlation_with_actual": 0.52,
485	      "decision": "killed_from_main_body"
486	    },
487	    "tables": [
488	      {
489	        "title": "Table 10: Difficulty Calibration Methods Comparison",
490	        "columns": [
491	          "method",
492	          "rho",
493	          "target",
494	          "verdict"
495	        ],
496	        "rows": [
497	          [
498	            "prompt-based",
499	            0.18,
500	            0.75,
501	            "FAIL"
502	          ],
503	          [
504	            "student simulation",
505	            0.41,
506	            0.75,
507	            "FAIL"
508	          ],
509	          [
510	            "combined",
511	            0.47,
512	            0.75,
513	            "FAIL"
514	          ]
515	        ]
516	      }
517	    ],
518	    "figures": [],
519	    "analysis": "Item generation failure在worst档下是expected的——它依赖于IRT calibration （plan_005已失败）和accurate difficulty prediction（both methods underperform）。 从paper中完全删除。\n\n\nItem generation在worst档下表现远低于target。Prompt-based difficulty targeting 几乎无效（ρ=0.18，consistent with literature的0.10-0.45 range低端）。Student simulation calibration有所改善（ρ=0.41）但远低于target 0.75——student simulation on MMLU的multi-domain knowledge items比single-domain math items（arXiv报告的 r=0.75-0.82）困难得多。Generated items的construct alignment也不足（0.64）， 因为MMLU items涵盖highly specialized domain knowledge，LLM generation的semantic equivalence不保证psychometric equivalence。Equating rho=0.88低于0.95 target。 在worst档下，整个regeneration pipeline不可行。但这与reframing一致—— reframed paper不claim regeneration，而是characterization + toolkit for monitoring。 Item generation结果完全dropped，不进appendix（避免给审稿人攻击面）。\n"
520	  },
521	  {
522	    "name": "cumulative_bayesian_dif",
523	    "description": "Implement cumulative Bayesian DIF priors (Sinharay et al., 2006). Simulate 4 successive administrations. Show cumulative power improvement.\n",
524	    "results": {
525	      "n_simulated_administrations": 4,
526	      "individual_admin_power": 0.4,
527	      "cumulative_2_admin_power": 0.49,
528	      "cumulative_3_admin_power": 0.56,
529	      "cumulative_4_admin_power": 0.61,
530	      "target_cumulative_3_power": 0.7,
531	      "prior_specification_sensitivity": "results vary 0.48-0.64 across 3 prior choices",
532	      "simulation_n_per_admin": 200,
533	      "delta_simulated": 1.0,
534	      "decision": "appendix_only"
535	    },
536	    "tables": [
537	      {
538	        "title": "Table 11: Cumulative DIF Power by Administration Count",
539	        "columns": [
540	          "n_administrations",
541	          "power",
542	          "target",
543	          "gap"
544	        ],
545	        "rows": [
546	          [
547	            1,
548	            0.4,
549	            0.7,
550	            -0.3
551	          ],
552	          [
553	            2,
554	            0.49,
555	            0.7,
556	            -0.21
557	          ],
558	          [
559	            3,
560	            0.56,
561	            0.7,
562	            -0.14
563	          ],
564	          [
565	            4,
566	            0.61,
567	            0.7,
568	            -0.09
569	          ]
570	        ]
571	      }
572	    ],
573	    "figures": [],
574	    "analysis": "Cumulative Bayesian DIF不达标，但不是blocking issue——reframed paper不依赖 longitudinal monitoring power。移至appendix作为future work motivation。\n\n\nCumulative Bayesian DIF在worst档下power improvement不达标。3次administration 后power仅0.56（target 0.70），4次仅0.61。原因：Sinharay et al.的方法假设successive administrations的examinee populations来自same distribution（exchangeable）， 但LLM benchmarks中successive cohorts的ability distribution系统性shift（新模型 systematically stronger）。Prior accumulation被ability drift corrupted—— previous administrations的DIF evidence可能来自ability confound而非genuine item change， 累积这些evidence amplifies bias而非reduces noise。Prior specification sensitivity 也高（0.48-0.64 range），意味着结果依赖于subjective prior choice。 在worst档下，这是simulation-only结果，没有real data validation，审稿人视为 underdeveloped。Reframed paper中作为appendix \"future direction\" sketch保留， 但不占main body任何空间。\n"
575	  },
576	  {
577	    "name": "graceful_degradation_analysis",
578	    "description": "Formal analysis of benchmark validity under progressive item replacement. Simulate 5%-50% replacement, measure ranking stability and construct coverage.\n",
579	    "results": {
580	      "replacement_5pct_rho": 0.998,
581	      "replacement_10pct_rho": 0.994,
582	      "replacement_20pct_rho": 0.981,
583	      "replacement_50pct_rho": 0.937,
584	      "construct_coverage_5pct": 0.97,
585	      "construct_coverage_20pct": 0.88,
586	      "construct_coverage_50pct": 0.71,
587	      "reliability_alpha_original": 0.94,
588	      "reliability_alpha_20pct_replaced": 0.86,
589	      "reliability_alpha_50pct_replaced": 0.74,
590	      "theoretical_bound_rho_at_31pct": 0.969,
591	      "decision": "appendix_supplementary"
592	    },
593	    "tables": [
594	      {
595	        "title": "Table 12: Graceful Degradation Under Replacement",
596	        "columns": [
597	          "replacement_pct",
598	          "ranking_rho",
599	          "reliability_alpha",
600	          "coverage"
601	        ],
602	        "rows": [
603	          [
604	            0,
605	            1.0,
606	            0.94,
607	            1.0
608	          ],
609	          [
610	            5,
611	            0.998,
612	            0.93,
613	            0.97
614	          ],
615	          [
616	            10,
617	            0.994,
618	            0.91,
619	            0.93
620	          ],
621	          [
622	            20,
623	            0.981,
624	            0.86,
625	            0.88
626	          ],
627	          [
628	            31,
629	            0.969,
630	            0.85,
631	            0.82
632	          ],
633	          [
634	            50,
635	            0.937,
636	            0.74,
637	            0.71
638	          ]
639	        ]
640	      }
641	    ],
642	    "figures": [],
643	    "analysis": "结果支持\"monitoring over remediation\"的operational message。在worst档下， 直接item removal/replacement不是viable strategy for 31% instability。 Reframed paper中作为operational guidance的evidence basis。\n\n\nGraceful degradation分析在worst档下显示replacement不如预期robust。20% replacement 时rho=0.981尚可接受，但reliability从0.94降到0.86——接近educational testing的 minimum threshold（0.85）。50% replacement时reliability=0.74，clearly unacceptable。 Construct coverage也rapidly degrades——替换items无法maintain MMLU的57-subject knowledge structure。这组结果在worst档下strengthens \"instability ≠ invalidity\" narrative的另一面：removing unstable items 不是好的remediation strategy（at 31%, reliability drops to ~0.85 boundary）。但它也意味着DIF-based benchmark maintenance （audit protocol的\"act\" tier at C%>25）在operational上是risky的。 Reframed paper中，这个结果支持\"characterize, don't fix\"的message—— 用一段话在Discussion中提及，详细数据移appendix。\n"
644	  },
645	  {
646	    "name": "item_focused_trees",
647	    "description": "Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative to categorical cohort DIF. Treat model release date as continuous covariate.\n",
648	    "results": {
649	      "ift_implemented": true,
650	      "ift_n_items_flagged": 2847,
651	      "ift_dif_pct": 22.8,
652	      "ift_vs_mh_jaccard": 0.52,
653	      "ift_vs_mh_concordance": 0.71,
654	      "ift_split_points_temporal": "majority split at 2023-Q3 to 2024-Q1",
655	      "ift_nonlinear_dif_detected": 312,
656	      "ift_rmsea_improvement": null,
657	      "ift_advantage": "avoids arbitrary cohort splits",
658	      "ift_disadvantage": "tree instability — different random seeds yield different splits",
659	      "tree_stability_jaccard_across_seeds": 0.63,
660	      "decision": "appendix_robustness_check"
661	    },
662	    "tables": [
663	      {
664	        "title": "Table 13: IFT vs MH-DIF Comparison",
665	        "columns": [
666	          "method",
667	          "c_pct",
668	          "unique_flags",
669	          "overlap_jaccard"
670	        ],
671	        "rows": [
672	          [
673	            "MH-DIF",
674	            31.3,
675	            1583,
676	            0.52
677	          ],
678	          [
679	            "IFT",
680	            22.8,
681	            512,
682	            0.52
683	          ]
684	        ]
685	      }
686	    ],
687	    "figures": [],
688	    "analysis": "IFT结果在worst档下是double-edged：支持temporal split的合理性，但method disagreement （Jaccard=0.52）加入审稿人的\"method-dependent results\"narrative。Appendix only。\n\n\nIFT在worst档下给出与MH partially concordant但不fully consistent的结果。 C%=22.8%（低于MH的31.3%），Jaccard=0.52——meaning approximately half the items flagged by each method are unique to that method。IFT的优势（continuous covariate, no arbitrary split）被tree instability抵消——across random seeds的Jaccard仅0.63， 意味着IFT结果本身不reproducible。IFT发现312个nonlinear DIF items（difficulty change is non-monotonic over time），这是MH无法detect的，但在worst档下审稿人视为 \"additional evidence that the signal is noisy and method-dependent, not that nonlinear DIF is a real phenomenon\"。IFT的split points集中在2023-Q3到2024-Q1， 与temporal cohort split大致对齐——这验证了temporal split的合理性，但也意味着 IFT没有提供fundamentally new information。在reframed paper中作为appendix robustness check保留，main body一句话提及\"results qualitatively consistent with continuous-covariate alternative\"。\n"
689	  },
690	  {
691	    "name": "architecture_stratified_dif",
692	    "description": "Run DIF within architecture-homogeneous decoder-only subpopulation. Report IRT fit diagnostics. Compare C% and detection power vs full population.\n",
693	    "results": {
694	      "n_decoder_only": 5226,
695	      "n_non_decoder": 1,
696	      "pct_decoder_only": 99.98,
697	      "decoder_only_c_pct": 31.3,
698	      "decoder_only_jaccard_vs_full": 1.0,
699	      "irt_rmsea_full": 0.094,
700	      "irt_rmsea_decoder_only": 0.094,
701	      "irt_cfi_full": 0.68,
702	      "irt_cfi_decoder_only": 0.68,
703	      "fit_improvement": "none — removing 1 model changes nothing",
704	      "conclusion": "architecture heterogeneity is not the source of IRT misfit",
705	      "real_source_of_misfit": "57-subject multidimensionality + non-normal ability distribution"
706	    },
707	    "tables": [
708	      {
709	        "title": "Table 14: Architecture Stratification (Moot)",
710	        "columns": [
711	          "population",
712	          "n_models",
713	          "c_pct",
714	          "rmsea",
715	          "cfi"
716	        ],
717	        "rows": [
718	          [
719	            "full",
720	            5227,
721	            31.3,
722	            0.094,
723	            0.68
724	          ],
725	          [
726	            "decoder-only",
727	            5226,
728	            31.3,
729	            0.094,
730	            0.68
731	          ],
732	          [
733	            "delta",
734	            1,
735	            0.0,
736	            0.0,
737	            0.0
738	          ]
739	        ]
740	      }
741	    ],
742	    "figures": [],
743	    "analysis": "实验本身结论正确（architecture不是问题），但在worst档下被视为wasted space。 Reframed paper中压缩为半句话。\n\n\nArchitecture stratification在worst档下确认了一个重要但trivial的finding： METABENCH MMLU是99.98% decoder-only（5226/5227），removing 1个non-decoder model changes absolutely nothing。C%不变（31.3%），Jaccard=1.0，IRT fit不变。 这experiment本身是correct（排除architecture heterogeneity作为concern）， 但在worst档下审稿人说：\"我们从未argue architecture heterogeneity是问题——问题是 57-subject multidimensionality + 非正态ability distribution + model non-independence。 你们排除了一个straw man concern\"。IRT fit仍然terrible（RMSEA=0.094, CFI=0.68）， 因为真正的misfit来源（multidimensionality）没有被addressed。 在reframed paper中，architecture homogeneity作为一句话fact（\"METABENCH MMLU is 99.98% decoder-only\"）报告，不需要单独实验。\n"
744	  },
745	  {
746	    "name": "semi_synthetic_contamination_validation",
747	    "description": "Inject known contamination into real METABENCH response matrix. Measure DIF detection power under controlled ground truth. Vary injection parameters.\n",
748	    "results": {
749	      "n_clean_items_selected": 500,
750	      "n_injected_items": 150,
751	      "temporal_external_tpr_p03": 0.39,
752	      "temporal_external_tpr_p05": 0.58,
753	      "temporal_external_tpr_p07": 0.74,
754	      "temporal_external_tpr_p10": 0.87,
755	      "temporal_external_fpr": 0.318,
756	      "temporal_external_delta_tpr_p03": 0.07,
757	      "temporal_external_delta_tpr_p05": 0.26,
758	      "temporal_external_delta_tpr_p07": 0.42,
759	      "temporal_external_delta_tpr_p10": 0.55,
760	      "ability_external_tpr_p10": 0.62,
761	      "ability_external_delta_tpr_p10": 0.19,
762	      "fpr_inflation_at_p10_standard": "0.298_to_0.58",
763	      "matching_variable_contamination": true,
764	      "cross_subject_matching_delta_fpr": 0.003,
765	      "replication_delta_tpr_range": "[0.25, 0.40]"
766	    },
767	    "tables": [
768	      {
769	        "title": "Table 15: Semi-Synthetic ΔTPR Under Worst Tier",
770	        "columns": [
771	          "injection_p",
772	          "tpr",
773	          "baseline_fpr",
774	          "delta_tpr",
775	          "registry_delta_tpr"
776	        ],
777	        "rows": [
778	          [
779	            0.3,
780	            0.39,
781	            0.318,
782	            0.07,
783	            0.222
784	          ],
785	          [
786	            0.5,
787	            0.58,
788	            0.318,
789	            0.26,
790	            0.508
791	          ],
792	          [
793	            0.7,
794	            0.74,
795	            0.318,
796	            0.42,
797	            0.664
798	          ],
799	          [
800	            1.0,
801	            0.87,
802	            0.318,
803	            0.55,
804	            0.674
805	          ]
806	        ]
807	      },
808	      {
809	        "title": "Table 16: Cross-Subject vs Within-Subject Matching",
810	        "columns": [
811	          "matching",
812	          "delta_fpr",
813	          "delta_tpr_p05",
814	          "verdict"
815	        ],
816	        "rows": [
817	          [
818	            "within-subject",
819	            "+0.186",
820	            0.34,
821	            "FPR inflation — contaminated matching var"
822	          ],
823	          [
824	            "cross-subject",
825	            "+0.003",
826	            0.26,
827	            "FPR stable — anchor finding preserved"
828	          ]
829	        ]
830	      }
831	    ],
832	    "figures": [],
833	    "analysis": "Semi-synthetic framework在worst档下power减弱但core innovation（cross-subject matching, ΔFPR≈0）preserved。这成为reframed paper的anchor contribution——framework本身 不依赖IRT assumptions，是portable的method contribution。Power limitations honestly reported。\n\n\nSemi-synthetic在worst档下ΔTPR显著低于registry记录。P=0.5时ΔTPR=0.26（registry为 0.508），p=1.0时ΔTPR=0.55（registry为0.674）。差异来源：worst档下的injection 使用更conservative的parameter choices——injected items选自difficulty分布中间段 （避免easy items的ceiling effect），focal group size更接近minimum（N≈100 vs registry的N=807），exploitation rate的effective signal更小（因为\"clean\" baseline items本身已有31%被flag为C-class，diluting the injection signal）。 关键问题：baseline FPR=0.318意味着没有injection时就有31.8%的items被flag—— ΔTPR必须在这个high baseline上demonstrate增量，signal-to-noise ratio差。 Cross-subject matching仍然有效（ΔFPR≈0.003，接近zero），这是anchor finding。 但ΔTPR的magnitude（worst档0.25-0.40）审稿人判定为\"moderate at best — the framework works but detection power is underwhelming\"。 在reframed paper中，semi-synthetic framework仍是anchor contribution—— 但framing从\"powerful detection tool\"变为\"principled validation infrastructure with known power limitations\"。\n"
834	  },
835	  {
836	    "name": "multi_benchmark_temporal_dif",
837	    "description": "Run temporal DIF on additional benchmarks from METABENCH (ARC, HellaSwag, WinoGrande, TruthfulQA, MMLU-Pro). Address \"only MMLU\" concern.\n",
838	    "results": {
839	      "mmlu_c_pct": 31.3,
840	      "mmlu_permutation_null": 16.4,
841	      "mmlu_effective": 14.9,
842	      "arc_c_pct": 13.8,
843	      "arc_permutation_null": 9.2,
844	      "arc_effective": 4.6,
845	      "hellaswag_c_pct": 10.1,
846	      "hellaswag_permutation_null": 7.8,
847	      "hellaswag_effective": 2.3,
848	      "winogrande_c_pct": 14.7,
849	      "winogrande_permutation_null": 10.1,
850	      "winogrande_effective": 4.6,
851	      "truthfulqa_c_pct": 22.4,
852	      "truthfulqa_permutation_null": 14.8,
853	      "truthfulqa_effective": 7.6,
854	      "gsm8k_c_pct": 12.4,
855	      "gsm8k_permutation_null": 8.7,
856	      "gsm8k_effective": 3.7,
857	      "cross_benchmark_raw_range": "10.1-31.3%",
858	      "cross_benchmark_effective_range": "2.3-14.9%",
859	      "all_random_controls_below_1pct": true,
860	      "mmlu_pro_not_available": true
861	    },
862	    "tables": [
863	      {
864	        "title": "Table 17: Multi-Benchmark DIF Summary (Worst Tier)",
865	        "columns": [
866	          "benchmark",
867	          "n_items",
868	          "raw_c_pct",
869	          "permutation_null",
870	          "effective_c_pct",
871	          "random_control"
872	        ],
873	        "rows": [
874	          [
875	            "MMLU",
876	            12508,
877	            31.3,
878	            16.4,
879	            14.9,
880	            0.18
881	          ],
882	          [
883	            "TruthfulQA",
884	            817,
885	            22.4,
886	            14.8,
887	            7.6,
888	            0.37
889	          ],
890	          [
891	            "WinoGrande",
892	            1267,
893	            14.7,
894	            10.1,
895	            4.6,
896	            0.32
897	          ],
898	          [
899	            "ARC",
900	            1172,
901	            13.8,
902	            9.2,
903	            4.6,
904	            0.6
905	          ],
906	          [
907	            "GSM8K",
908	            1319,
909	            12.4,
910	            8.7,
911	            3.7,
912	            0.3
913	          ],
914	          [
915	            "HellaSwag",
916	            10042,
917	            10.1,
918	            7.8,
919	            2.3,
920	            0.28
921	          ]
922	        ]
923	      }
924	    ],
925	    "figures": [],
926	    "analysis": "Multi-benchmark结果在worst档下是mixed news。好消息：all benchmarks show above-chance DIF（random controls <1%）。坏消息：effective signal after permutation controls 很小for most benchmarks。Reframed paper必须honest about这个range。\n\n\nMulti-benchmark分析在worst档下揭示一个devastating pattern：raw C%在所有benchmarks 上都>10%（range 10.1-31.3%），但permutation null也consistently高（7.8-16.4%）， 扣除后effective C%范围仅2.3-14.9%。MMLU的effective C%最高（14.9%）因为它有最多subjects （57）和最大item pool（12508），提供更多opportunities for heterogeneity。 HellaSwag effective C%最低（2.3%），因为it's a relatively homogeneous task （sentence completion）——item-level behavioral heterogeneity genuinely lower。 Cross-benchmark heterogeneity本身是informative的（\"different benchmarks have different stability profiles\"），但审稿人concern是：\"if after permutation controls some benchmarks show <5% effective C%, your '31% instability' headline is MMLU-specific and cannot be generalized\"。在worst档下，\"31%\"的headline number必须qualified with \"before permutation controls; effective rate 10-18% depending on benchmark\"。 Reframed paper中，cross-benchmark heterogeneity成为characterization的一部分： \"benchmark stability varies from 2% (HellaSwag) to 15% (MMLU) — we provide benchmark-specific profiles\"。\n"
927	  },
928	  {
929	    "name": "permutation_null_c_rate",
930	    "description": "1000× permutation test: randomly reassign 2023/2024 temporal labels, run MH-DIF each time. Establish null distribution for C%.\n",
931	    "results": {
932	      "n_permutations": 1000,
933	      "null_c_pct_mean": 16.4,
934	      "null_c_pct_sd": 2.1,
935	      "null_c_pct_95ci": [
936	        12.6,
937	        20.3
938	      ],
939	      "null_c_pct_min": 10.8,
940	      "null_c_pct_max": 22.7,
941	      "observed_c_pct": 31.3,
942	      "z_score": 7.1,
943	      "p_value": "<1e-12",
944	      "effective_c_pct": 14.9,
945	      "fraction_spurious": 0.524,
946	      "null_mechanism": "cohort composition differences (ability, family structure, training vintage) generate substantial DIF even without temporal signal",
947	      "random_split_within_cohort_c_pct": 0.18,
948	      "permutation_vs_random_split_gap": "16.4 vs 0.18 — temporal label permutation preserves between-cohort structure"
949	    },
950	    "tables": [
951	      {
952	        "title": "Table 18: Permutation Null Distribution",
953	        "columns": [
954	          "statistic",
955	          "value"
956	        ],
957	        "rows": [
958	          [
959	            "null_mean_c_pct",
960	            16.4
961	          ],
962	          [
963	            "null_sd",
964	            2.1
965	          ],
966	          [
967	            "null_95_ci",
968	            "[12.6, 20.3]"
969	          ],
970	          [
971	            "observed_c_pct",
972	            31.3
973	          ],
974	          [
975	            "z_score",
976	            7.1
977	          ],
978	          [
979	            "effective_c_pct",
980	            14.9
981	          ],
982	          [
983	            "fraction_spurious",
984	            "52.4%"
985	          ],
986	          [
987	            "random_split_c_pct",
988	            0.18
989	          ]
990	        ]
991	      },
992	      {
993	        "title": "Table 19: Decomposition of Observed C%",
994	        "columns": [
995	          "source",
996	          "contribution_pct",
997	          "mechanism"
998	        ],
999	        "rows": [
1000	          [
1001	            "genuine_temporal_signal",
1002	            14.9,
1003	            "item-level behavioral change across model generations"
1004	          ],
1005	          [
1006	            "cohort_composition",
1007	            16.4,
1008	            "ability distribution + family structure + training vintage differences"
1009	          ],
1010	          [
1011	            "total",
1012	            31.3,
1013	            "N/A"
1014	          ]
1015	        ]
1016	      }
1017	    ],
1018	    "figures": [],
1019	    "analysis": "Permutation null是worst档论文的central finding。它将31%的headline number decompose为 ~15% genuine + ~16% spurious。Reframed paper必须lead with这个decomposition： \"we observe 31% raw behavioral heterogeneity, of which approximately half persists after permutation controls — the remainder reflects cohort composition differences that MH-DIF's total-score conditioning cannot absorb\"。这honest framing比 原来的\"31% instability\"更defensible，但也更modest。\n\n\nPermutation null是worst档的defining experiment。1000次permutation（保持group sizes N_ref=1080, N_foc=807不变，但随机打乱temporal labels）产生mean C%=16.4%（SD=2.1%）， 95% range [12.6, 20.3]。这意味着即使temporal labels是random的，仅因为两组models 的composition差异（ability distribution overlap=76.4%, 不同model families的比例差异, 不同training data vintages的representation差异），MH-DIF就会flag 12-20%的items。\n关键区分：这不是与random-split control（0.18%）矛盾。Random split是within-cohort的 （same time period, same family composition），而permutation null是between-cohort的 （preserves the actual model composition, just shuffles temporal labels）。 The 16.4% null arises because models from 2023 and 2024 genuinely differ in ways beyond temporal signal — model families, training approaches, scale distributions all differ between cohorts. MH's ability conditioning (total score) cannot absorb all these confounds.\nObserved 31.3% is still z=7.1 above null（p<1e-12），so temporal signal EXISTS beyond cohort composition. But 52.4% of the raw C% is attributable to cohort composition effects, not temporal item-level change. Effective C%=14.9%。\n在worst档下，审稿人的reaction： \"这证实了我们的concern——31%中一半以上是cohort composition artifact。MH-DIF 在LLM context下的conditioning is fundamentally insufficient。14.9%可能也包含 未被permutation null capture的confounds（tokenizer changes, training data composition within families）。The genuine temporal item-level signal may be even smaller。\"\n"
1020	  },
1021	  {
1022	    "name": "odds_ratio_regression_transparency",
1023	    "description": "Supplement pseudo R² with odds ratio, CI, McFadden/Nagelkerke R², deviance ratio. Add item-level accuracy change as predictor.\n",
1024	    "results": {
1025	      "model1_domain_delta": {
1026	        "mcfadden_r2": 0.0007,
1027	        "nagelkerke_r2": 0.0012,
1028	        "or_per_010": 1.55,
1029	        "or_ci": [
1030	          1.19,
1031	          2.03
1032	        ]
1033	      },
1034	      "model2_domain_plus_items": {
1035	        "mcfadden_r2": 0.0423,
1036	        "nagelkerke_r2": 0.072,
1037	        "or_domain_per_010": 0.73,
1038	        "or_difficulty_per_010": 0.78,
1039	        "or_discrimination_per_010": 1.51
1040	      },
1041	      "model3_item_delta": {
1042	        "mcfadden_r2": 0.0012,
1043	        "nagelkerke_r2": 0.0021,
1044	        "or_item_change_per_010": 1.08,
1045	        "or_item_ci": [
1046	          1.51,
1047	          2.96
1048	        ]
1049	      },
1050	      "model4_full": {
1051	        "mcfadden_r2": 0.0434,
1052	        "nagelkerke_r2": 0.0737,
1053	        "or_item_change_per_010": 0.92,
1054	        "or_difficulty_per_010": 0.77,
1055	        "or_discrimination_per_010": 1.54
1056	      },
1057	      "simpsons_paradox": true,
1058	      "simpsons_direction": "item accuracy change OR flips from 1.08 to 0.92 when controlling for item properties",
1059	      "deviance_explained_by_item_props": "96% of model variance from difficulty + discrimination, not accuracy change",
1060	      "lr_test_m1_vs_m2_chi2": 647,
1061	      "lr_test_m3_vs_m4_chi2": 656
1062	    },
1063	    "tables": [
1064	      {
1065	        "title": "Table 20: Logistic Regression Hierarchy",
1066	        "columns": [
1067	          "model",
1068	          "predictors",
1069	          "mcfadden_r2",
1070	          "nagelkerke_r2",
1071	          "key_or"
1072	        ],
1073	        "rows": [
1074	          [
1075	            "M1",
1076	            "domain_Δacc",
1077	            0.0007,
1078	            0.0012,
1079	            "1.55 [1.19-2.03]"
1080	          ],
1081	          [
1082	            "M2",
1083	            "domain_Δacc + item_props",
1084	            0.0423,
1085	            0.072,
1086	            "0.73 (Δacc flips)"
1087	          ],
1088	          [
1089	            "M3",
1090	            "item_Δacc",
1091	            0.0012,
1092	            0.0021,
1093	            "1.08"
1094	          ],
1095	          [
1096	            "M4",
1097	            "item_Δacc + item_props",
1098	            0.0434,
1099	            0.0737,
1100	            "0.92 (Δacc flips)"
1101	          ]
1102	        ]
1103	      }
1104	    ],
1105	    "figures": [],
1106	    "analysis": "Regression transparency strengthens honest framing但也gives审稿人ammunition： \"item properties explain 50× more variance than accuracy change — DIF may be a statistical artifact of item difficulty/discrimination structure\"。 Reframed paper must address this directly。\n\nOdds ratio regression在worst档下confirms并extends原有findings。Domain-level accuracy change（Model 1）是significant但tiny predictor（R²=0.0007）。Item-level accuracy change（Model 3）marginally better（R²=0.0012）但still near zero。 Simpson's paradox preserved：item accuracy change OR从1.08降到0.92 when controlling for item properties——meaning higher-accuracy-change items are actually LESS likely to be DIF after controlling for difficulty and discrimination。\n在worst档下，审稿人的worst-case解读：\"item difficulty和discrimination explains 7% of DIF variance（Model 4 R²=0.0737）。这虽然不高in absolute terms，但比accuracy change高50倍。DIF flags与item properties相关——harder, more discriminating items 更likely被flag。这可能是MH statistic的statistical property（高discrimination items 产生更大的α_MH estimates），而非genuine item-level behavioral change\"。\nPlan_027的d=-0.17被审稿人认为是marginal的ability gap，但temporal label可能proxy 其他未控制confound（training data composition, tokenizer changes, RLHF procedures）。 这些confounds不会被total score matching absorb。\n在reframed paper中，regression transparency section支持honest framing：\"DIF flags are weakly predicted by accuracy change but moderately predicted by item properties — we report this transparently as part of our characterization\"。\n"
1107	  }
1108	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "010fc2ec-8285-48a3-824c-92a9612a9a3d",
  "isSidechain": false,
  "promptId": "9377956b-ace9-4b16-82d2-21e10f437ea9",
  "type": "user",
  "uuid": "499e88ab-0b0d-4bfb-8ff7-d41c4cabd390",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"real_data_dif_mmlu\",\n    \"description\": \"Apply MH-DIF to METABENCH MMLU response matrix (5,219 models × 12,508 items). Temporal cohort (2023 vs 2024-H1), ability-quintile cohort, within-family confound control, domain-specificity analysis.\\n\",\n    \"results\": {\n      \"temporal_ets_c_pct\": 31.3,\n      \"temporal_fpr_li_clean\": 0.322,\n      \"temporal_enrichment\": 0.96,\n      \"ability_ets_c_pct\": 2.9,\n      \"ability_enrichment\": 1.19,\n      \"within_family_llama2v3_c_pct\": 61.3,\n      \"within_family_mistral_mixtral_c_pct\": 38.7,\n      \"domain_spearman_rho\": 0.307,\n      \"domain_spearman_p\": 0.02,\n      \"sanity_random_split_c_pct\": 0.18,\n      \"temporal_ability_jaccard\": 0.014,\n      \"irt_misfit_pct_lz_gt2\": 98.2,\n      \"permutation_null_c_pct_posterior\": 16.4,\n      \"effective_c_pct_after_permutation_control\": 14.9,\n      \"domain_specificity_chi2_p\": 0.78,\n      \"negative_disc_items_sensitivity\": \"removing 15.4% neg-disc items reduces C% by only 1.2pp\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 1: Temporal DIF Summary (Worst-Tier Interpretation)\",\n        \"columns\": [\n          \"metric\",\n          \"raw_value\",\n          \"after_permutation_control\",\n          \"reviewer_interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"C%\",\n            \"31.3%\",\n            \"14.9% (31.3 - 16.4 null)\",\n            \"inflated by cohort composition\"\n          ],\n          [\n            \"enrichment_vs_Li\",\n            0.96,\n            0.96,\n            \"trivially expected, not informative\"\n          ],\n          [\n            \"IRT_misfit\",\n            \"98% |Lz|>2\",\n            \"N/A\",\n            \"renders MH conditioning unreliable\"\n          ],\n          [\n            \"domain_rho\",\n            0.307,\n            \"N/A\",\n            \"ecological fallacy on N=57\"\n          ],\n          [\n            \"within_family_C%\",\n            \"38.7-61.3%\",\n            \"N/A\",\n            \"confounded by architecture change\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 2: Cohort Definition × Item Filtering Sensitivity\",\n        \"columns\": [\n          \"cohort\",\n          \"filter\",\n          \"c_pct\",\n          \"effective_c_pct\"\n        ],\n        \"rows\": [\n          [\n            \"temporal\",\n            \"all_items\",\n            31.3,\n            14.9\n          ],\n          [\n            \"temporal\",\n            \"no_neg_disc\",\n            30.1,\n            13.7\n          ],\n          [\n            \"ability\",\n            \"all_items\",\n            2.9,\n            \"N/A\"\n          ],\n          [\n            \"ability\",\n            \"no_neg_disc\",\n            2.7,\n            \"N/A\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"在worst档下，plan_001的核心结果从\\\"31% instability is genuine and robust\\\"变为 \\\"31% raw C%中约一半来自cohort composition artifacts\\\"。这不是statistical artifact （random split仍为0.18%），而是temporal label本身proxy了多个未控制confound。 Reframing策略：不再claim \\\"31% items show genuine measurement drift\\\"，而是 \\\"we observe 31% item-level behavioral heterogeneity between temporal cohorts, of which 10-18% persists after permutation controls — we characterize this heterogeneity without claiming psychometric interpretation\\\"。\\n\\n\\n表面数字与registry一致（31.3% C%），但在worst档下，plan_029的permutation null将揭示 temporal label assignment本身产生~16.4%的spurious C%——即随机打乱2023/2024标签后， 仅因cohort composition差异（ability distribution shift d=-0.17, model family结构差异, training data vintage差异）就能产生大量MH-DIF flags。这意味着31.3%中仅约14.9% 可归因于genuine item-level behavioral change。Within-family分析（Llama-2v3 C%=61.3%） 本应作为confound control，但在worst档下审稿人指出：Llama-2→3不是单纯temporal shift， 而是architecture+data+training全面重构，within-family DIF不能isolate contamination。 Domain specificity的ρ=0.307被审稿人dismisses为ecological correlation on N=57 subjects， 无item-level causal interpretation。98%的IRT misfit（|Lz|>2）在worst档下不再被接受为 \\\"reflects multidimensionality, discuss in limitations\\\"——审稿人要求multidimensional IRT 作为前提条件，否则MH-DIF结果uninterpretable。Enrichment≈1.0依然成立但被重新解读： \\\"当然web-overlap和DIF不相关，这不是discovery而是trivially expected\\\"。\\n\"\n  },\n  {\n    \"name\": \"rl_robustness_validation\",\n    \"description\": \"Validate DIF robustness to reasoning-RL models. Add 10-15 GRPO/PPO models to focal cohort; measure DIF flag stability. Compare traditional detectors (Min-K%, ConStat) on RL models individually.\\n\",\n    \"results\": {\n      \"baseline_temporal_c_pct\": 31.3,\n      \"with_alignment_rl_c_pct\": 29.8,\n      \"with_reasoning_rl_c_pct\": 24.1,\n      \"jaccard_baseline_vs_alignment_rl\": 0.82,\n      \"jaccard_baseline_vs_reasoning_rl\": 0.43,\n      \"jaccard_alignment_vs_reasoning_rl\": 0.48,\n      \"traditional_mink_auroc_base\": 0.71,\n      \"traditional_mink_auroc_rl\": 0.68,\n      \"traditional_constat_auroc_base\": 0.65,\n      \"traditional_constat_auroc_rl\": 0.62,\n      \"auroc_drop_mink\": 0.03,\n      \"auroc_drop_constat\": 0.03,\n      \"delong_p_mink\": 0.34,\n      \"delong_p_constat\": 0.41,\n      \"tost_equivalence_p\": 0.08,\n      \"n_reasoning_rl_models\": 13,\n      \"power_analysis_delta_boundary\": 1.8,\n      \"bootstrap_ci_jaccard_rl\": [\n        0.31,\n        0.54\n      ]\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 3: DIF Flag Stability Under Cohort Composition Changes\",\n        \"columns\": [\n          \"comparison\",\n          \"jaccard\",\n          \"c_pct_shift\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"baseline vs +alignment-RL\",\n            0.82,\n            \"-1.5pp\",\n            \"stable (DPO/ORPO不影响)\"\n          ],\n          [\n            \"baseline vs +reasoning-RL\",\n            0.43,\n            \"-7.2pp\",\n            \"UNSTABLE — flags shift fundamentally\"\n          ],\n          [\n            \"alignment-RL vs reasoning-RL\",\n            0.48,\n            \"-5.7pp\",\n            \"RL type matters more than temporal split\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 4: Traditional Detector AUROC Comparison\",\n        \"columns\": [\n          \"detector\",\n          \"auroc_base\",\n          \"auroc_rl\",\n          \"delta\",\n          \"delong_p\"\n        ],\n        \"rows\": [\n          [\n            \"Min-K%\",\n            0.71,\n            0.68,\n            -0.03,\n            0.34\n          ],\n          [\n            \"ConStat\",\n            0.65,\n            0.62,\n            -0.03,\n            0.41\n          ],\n          [\n            \"MH-DIF\",\n            \"N/A\",\n            \"N/A\",\n            \"Jaccard=0.43\",\n            \"N/A\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RL robustness实验在worst档下彻底失败。Jaccard<0.55意味着DIF不能被视为cohort-invariant detector。审稿人的解读：\\\"如果改变cohort中13个模型就导致43%的flag翻转，那DIF测量的 不是item property而是cohort property——这与psychometric DIF的理论前提矛盾\\\"。 Reframing下这变为：\\\"we acknowledge DIF flags are cohort-dependent — our characterization is specific to the 2023-vs-2024 temporal split and should not be extrapolated to arbitrary cohort definitions\\\"。这大幅削弱了generalizability claim。\\n\\n\\n在worst档下，reasoning-RL模型加入focal cohort后，DIF flags大幅shift（Jaccard=0.43, 远低于0.8的stability阈值）。原因：reasoning-RL模型（DeepSeek-R1, Qwen2.5-RL等） 的response pattern与标准decoder-only模型本质不同——它们在chain-of-thought后达到答案， item difficulty profile完全改变。MH-DIF的ability conditioning基于total score， 但reasoning-RL模型的total score来源（deliberate reasoning vs memorization）与 传统模型不同，导致conditioning variable被confound。C%从31.3%降至24.1%——不是因为 RL模型\\\"更干净\\\"，而是因为cohort composition shift改变了哪些items被flag。 传统detectors的AUROC drop很小（0.03），审稿人据此argue：\\\"DIF对cohort composition 敏感而传统方法不敏感，说明DIF的sensitivity实际上是instability的体现\\\"。 TOST equivalence test borderline不通过（p=0.08），无法claim DIF和传统方法等效。 N=13 reasoning-RL模型本身就是underpowered的——worst档下这被视为fatal flaw， 不是\\\"supplementary\\\"而是\\\"insufficient to support any RL robustness claim\\\"。\\n\"\n  },\n  {\n    \"name\": \"constat_perturbation_eval\",\n    \"description\": \"Independent evaluation of ConStat perturbation testing on MMLU: generate reformulations for 200+ items, compare performance, apply FDR-controlled detection.\\n\",\n    \"results\": {\n      \"n_items_reformulated\": 237,\n      \"constat_detection_rate_non_rl\": 0.24,\n      \"constat_detection_rate_rl\": 0.09,\n      \"constat_fpr\": 0.06,\n      \"constat_auroc_non_rl\": 0.72,\n      \"constat_auroc_rl\": 0.54,\n      \"reformulation_quality_score\": 0.83,\n      \"semantic_equivalence_verified\": 0.91,\n      \"fdr_threshold_q005\": 0.048,\n      \"constat_vs_dif_overlap_jaccard\": 0.15,\n      \"constat_unique_detections\": 47,\n      \"dif_unique_detections\": 312\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 5: ConStat Detection Performance\",\n        \"columns\": [\n          \"model_type\",\n          \"n_models\",\n          \"detection_rate\",\n          \"auroc\",\n          \"fpr\"\n        ],\n        \"rows\": [\n          [\n            \"non-RL\",\n            50,\n            0.24,\n            0.72,\n            0.06\n          ],\n          [\n            \"alignment-RL\",\n            30,\n            0.18,\n            0.64,\n            0.07\n          ],\n          [\n            \"reasoning-RL\",\n            13,\n            0.09,\n            0.54,\n            0.05\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ConStat实验结果本身是informative的，但在worst档下strengthens审稿人argument： item-level contamination detection整个领域缺乏construct validity——不同方法测量 不同东西，没有ground truth能判断谁对。这支持reframe到pure characterization paper。\\n\\n\\nConStat在non-RL模型上表现合理（AUROC=0.72），在RL模型上大幅衰减（0.54，接近random）。 但在worst档下，关键问题不是ConStat表现如何，而是ConStat和DIF的detection overlap极低 （Jaccard=0.15）。审稿人解读：\\\"两个声称检测同一现象的方法几乎不flag同一批items， 说明它们测量的是不同东西——或者至少一个在测量artifact\\\"。ConStat的47个unique detections 中包含一些DIF完全miss的真实contamination cases（通过reformulation验证）， 削弱了DIF作为primary detector的positioning。在reframed paper中，ConStat结果 降级为appendix baseline comparison，不再用于ensemble narrative（已dropped）。\\n\"\n  },\n  {\n    \"name\": \"dvd_generation_variance_eval\",\n    \"description\": \"Independent evaluation of DVD generation variance on MMLU: 50 responses per item via temperature sampling on 10-15 models, detect bimodal distributions.\\n\",\n    \"results\": {\n      \"n_models_tested\": 12,\n      \"n_items_sampled\": 500,\n      \"responses_per_item\": 50,\n      \"temperature\": 0.8,\n      \"dvd_detection_rate\": 0.18,\n      \"dvd_auroc\": 0.61,\n      \"dvd_fpr\": 0.08,\n      \"bimodal_items_detected\": 43,\n      \"dvd_vs_dif_jaccard\": 0.11,\n      \"dvd_vs_constat_jaccard\": 0.19,\n      \"variant_contamination_coverage\": 0.31,\n      \"verbatim_contamination_coverage\": 0.07,\n      \"gpu_hours_used\": 58\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 6: DVD Detection Summary\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"AUROC\",\n            0.61\n          ],\n          [\n            \"detection_rate\",\n            0.18\n          ],\n          [\n            \"FPR\",\n            0.08\n          ],\n          [\n            \"bimodal_items\",\n            43\n          ],\n          [\n            \"overlap_with_DIF (Jaccard)\",\n            0.11\n          ],\n          [\n            \"overlap_with_ConStat (Jaccard)\",\n            0.19\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DVD结果在worst档下直接支持Claim 2的meta-critique（不同方法测量不同东西）， 但ironically也削弱了paper自身的DIF-centric positioning。Reframed paper中， DVD和ConStat结果用一段话提及作为\\\"multiple lenses on item heterogeneity\\\"的evidence， 不再pursuit ensemble fusion。\\n\\n\\nDVD在worst档下表现中等偏弱（AUROC=0.61）。Generation variance信号在LLM上比human testing更noisy——temperature sampling的response分布本身就是multimodal的（model confidence varies by item type, not just contamination）。DVD与DIF的overlap更低 （Jaccard=0.11），三个方法三个不同的item set。在worst档下，这个三方disagreement 成为审稿人最强的论据之一：\\\"when three independent detectors flag almost entirely different items, the field has a construct validity crisis, not a contamination detection toolbox\\\"。DVD的variant contamination coverage（0.31）比verbatim（0.07） 好得多，确认它确实测量不同phenomenon，但这恰恰支持meta-critique而非ensemble narrative。\\n\"\n  },\n  {\n    \"name\": \"ensemble_fusion\",\n    \"description\": \"Fuse DIF + ConStat + DVD into multi-signal ensemble. Calibrate thresholds, evaluate voting and weighted fusion, report coverage and precision.\\n\",\n    \"results\": {\n      \"ensemble_attempted\": true,\n      \"ensemble_viable\": false,\n      \"majority_vote_auroc\": 0.58,\n      \"weighted_fusion_auroc\": 0.63,\n      \"ensemble_fpr\": 0.14,\n      \"cross_val_weight_instability\": \"weights flip sign across folds\",\n      \"uniform_weight_auroc\": 0.6,\n      \"pairwise_signal_correlation_dif_constat\": 0.09,\n      \"pairwise_signal_correlation_dif_dvd\": 0.06,\n      \"pairwise_signal_correlation_constat_dvd\": 0.13,\n      \"coverage_analysis\": \"DIF covers 31%, ConStat 24%, DVD 18% — but only 4% in all three\",\n      \"decision\": \"killed\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Ensemble killed。在reframed paper中不提及。三方法disagreement作为meta-critique的 additional evidence在Discussion一句话提及。\\n\\n\\nEnsemble fusion在worst档下被kill。三个信号之间的correlation极低（0.06-0.13）， 意味着它们不是measuring同一construct的noisy estimators，而是measuring不同constructs。 Majority vote AUROC（0.58）甚至低于单个最佳detector（ConStat 0.72 on non-RL）， 因为vote要求agreement但signals几乎不agree。Weighted fusion cross-validation 显示权重在folds间高度不稳定（某些fold中DIF权重为负），表明没有stable fusion function。 FPR=0.14 borderline超过0.10 target。在worst档下，ensemble failure不是简单的 \\\"negative result\\\"——它是对整个contamination detection paradigm的existential challenge。 Paper中完全删除ensemble narrative，连appendix都不保留。\\n\"\n  },\n  {\n    \"name\": \"cross_benchmark_gsm8k\",\n    \"description\": \"Replicate DIF analysis on GSM8K using GSM1K as ground truth. Temporal DIF, semi-synthetic validation, GSM1K contamination gap correlation.\\n\",\n    \"results\": {\n      \"gsm8k_n_items\": 1319,\n      \"gsm8k_n_ref\": 1017,\n      \"gsm8k_n_foc\": 804,\n      \"gsm8k_temporal_c_pct\": 12.4,\n      \"gsm8k_external_c_pct\": 38.1,\n      \"gsm8k_sanity_c_pct\": 0.3,\n      \"gsm8k_permutation_null_c_pct\": 8.7,\n      \"gsm8k_effective_c_pct\": 3.7,\n      \"semi_synthetic_delta_tpr_standard_p10\": 0.38,\n      \"semi_synthetic_delta_tpr_external_p10\": 0.27,\n      \"gsm1k_correlation_n\": 33,\n      \"gsm1k_pearson_r\": -0.29,\n      \"gsm1k_pearson_p\": 0.1,\n      \"gsm1k_spearman_rho\": -0.22,\n      \"gsm1k_spearman_p\": 0.21,\n      \"gsm1k_partial_r\": -0.18,\n      \"gsm1k_partial_p\": 0.32,\n      \"gsm1k_ci_upper\": 0.06,\n      \"direction\": \"still negative but non-significant\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 7: Cross-Benchmark DIF Comparison (Worst Tier)\",\n        \"columns\": [\n          \"benchmark\",\n          \"raw_c_pct\",\n          \"permutation_null\",\n          \"effective_c_pct\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            31.3,\n            16.4,\n            14.9,\n            \"moderate signal after controls\"\n          ],\n          [\n            \"GSM8K\",\n            12.4,\n            8.7,\n            3.7,\n            \"near noise floor\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 8: GSM1K Correlation Under Worst Tier\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"ci_95\",\n          \"p_value\"\n        ],\n        \"rows\": [\n          [\n            \"Pearson r\",\n            -0.29,\n            \"[-0.58, 0.06]\",\n            0.1\n          ],\n          [\n            \"Spearman ρ\",\n            -0.22,\n            \"[-0.53, 0.14]\",\n            0.21\n          ],\n          [\n            \"Partial r\",\n            -0.18,\n            \"[-0.50, 0.19]\",\n            0.32\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"GSM8K结果在worst档下严重削弱cross-benchmark generalizability claim。Effective C%=3.7% 意味着GSM8K上几乎没有genuine item-level DIF。Reframed paper中，GSM8K从\\\"cross-benchmark validation\\\"降级为\\\"the method produces different results on different benchmarks — this heterogeneity itself is worth characterizing\\\"。GSM1K correlation完全dropped from claims。\\n\\n\\nGSM8K在worst档下表现远弱于MMLU。Temporal C%仅12.4%（worst档cross_benchmark_c_pct_min 范围8-14%），扣除permutation null（8.7%）后effective C%仅3.7%——接近noise floor。 原因：GSM8K是single-domain math benchmark，items之间homogeneity更高，temporal cohort间的ability差异更直接映射到item difficulty（math能力提升→所有items变容易）， MH的ability conditioning更有效地absorb了这个effect。但也可能是GSM8K确实更stable。 Semi-synthetic ΔTPR显著降低（worst档0.25-0.4范围），因为smaller item pool（1319 vs 12508） 导致power降低，且single-domain matching variable更noisy。 GSM1K correlation从registry的-0.478(p=0.005)恶化到-0.29(p=0.10)——在worst档下 N=33太小，置信区间覆盖zero。审稿人判定：\\\"N=33 with CI crossing zero is not evidence for anything\\\"。Direction仍为negative（与contamination hypothesis相反）， 但在worst档下这被视为\\\"noise, not signal\\\"。GSM1K分析降级为appendix exploratory。\\n\"\n  },\n  {\n    \"name\": \"bifactor_irt_equating_pilot\",\n    \"description\": \"Pilot bifactor IRT equating on MMLU: fit bifactor model, select anchor items, fixed-parameter calibration of replacements, demonstrate equated score equivalence.\\n\",\n    \"results\": {\n      \"bifactor_convergence\": false,\n      \"bifactor_attempts\": 3,\n      \"bifactor_rmsea\": 0.089,\n      \"bifactor_cfi\": 0.72,\n      \"bifactor_tli\": 0.69,\n      \"bifactor_srmr\": 0.11,\n      \"fallback_2pl_rmsea\": 0.094,\n      \"fallback_2pl_cfi\": 0.68,\n      \"anchor_item_selection_possible\": false,\n      \"equated_rho\": null,\n      \"decision\": \"killed\",\n      \"reason\": \"bifactor model fails to converge on 12508×5219 matrix; even when forced, fit indices far below acceptable thresholds\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 9: IRT Model Fit Comparison\",\n        \"columns\": [\n          \"model\",\n          \"rmsea\",\n          \"cfi\",\n          \"tli\",\n          \"srmr\",\n          \"converged\"\n        ],\n        \"rows\": [\n          [\n            \"unidimensional 2PL\",\n            0.094,\n            0.68,\n            0.65,\n            0.12,\n            \"yes (poor fit)\"\n          ],\n          [\n            \"bifactor (57 specific)\",\n            0.089,\n            0.72,\n            0.69,\n            0.11,\n            \"no (forced)\"\n          ],\n          [\n            \"acceptable thresholds\",\n            \"<0.06\",\n            \">0.95\",\n            \">0.95\",\n            \"<0.08\",\n            \"N/A\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bifactor failure是worst档的defining event之一。它证实了审稿人的核心concern： MMLU的57-subject structure使得any IRT model都是misspecified的。但在reframed paper中， 这反而成为strength：我们explicitly acknowledge IRT assumptions violated， 所以我们不依赖IRT interpretation——MH作为nonparametric χ² test不需要IRT model fit。 Bifactor结果在limitations section作为\\\"we attempted and it failed\\\"报告。\\n\\n\\nBifactor IRT在worst档下完全失败。12,508 items × 57 subjects的bifactor model （1 general + 57 specific factors）有>25,000 parameters，在5,219 models上 severely overparameterized。Convergence failure after 3 attempts with different starting values和estimation methods（MHRM, EM, QN）。即使forced convergence 的fit indices（RMSEA=0.089, CFI=0.72）远低于acceptable thresholds（RMSEA<0.06, CFI>0.95）。这directly confirms审稿人的核心concern：\\\"unidimensional IRT assumption severely violated, and bifactor doesn't rescue it because the item-to-model ratio is too small for the factor structure\\\"。Anchor item selection不可能——没有reliable parameter estimates。Equating pilot killed。在worst档下这是paper最致命的finding之一： 不仅unidimensional IRT不work，连multidimensional IRT也不work on this data。 Reframing response：完全放弃IRT-based interpretation，将MH当作nonparametric test。\\n\"\n  },\n  {\n    \"name\": \"item_generation_calibration\",\n    \"description\": \"Generate replacement items for DIF-flagged MMLU questions via LLM generation with construct constraints. Calibrate via student simulation.\\n\",\n    \"results\": {\n      \"n_items_generated\": 200,\n      \"n_items_quality_filtered\": 142,\n      \"difficulty_correlation_prompt_based\": 0.18,\n      \"difficulty_correlation_student_sim\": 0.41,\n      \"difficulty_correlation_target\": 0.75,\n      \"construct_alignment_score\": 0.64,\n      \"replacement_equating_rho\": 0.88,\n      \"replacement_equating_target\": 0.95,\n      \"student_sim_correlation_with_actual\": 0.52,\n      \"decision\": \"killed_from_main_body\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 10: Difficulty Calibration Methods Comparison\",\n        \"columns\": [\n          \"method\",\n          \"rho\",\n          \"target\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"prompt-based\",\n            0.18,\n            0.75,\n            \"FAIL\"\n          ],\n          [\n            \"student simulation\",\n            0.41,\n            0.75,\n            \"FAIL\"\n          ],\n          [\n            \"combined\",\n            0.47,\n            0.75,\n            \"FAIL\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Item generation failure在worst档下是expected的——它依赖于IRT calibration （plan_005已失败）和accurate difficulty prediction（both methods underperform）。 从paper中完全删除。\\n\\n\\nItem generation在worst档下表现远低于target。Prompt-based difficulty targeting 几乎无效（ρ=0.18，consistent with literature的0.10-0.45 range低端）。Student simulation calibration有所改善（ρ=0.41）但远低于target 0.75——student simulation on MMLU的multi-domain knowledge items比single-domain math items（arXiv报告的 r=0.75-0.82）困难得多。Generated items的construct alignment也不足（0.64）， 因为MMLU items涵盖highly specialized domain knowledge，LLM generation的semantic equivalence不保证psychometric equivalence。Equating rho=0.88低于0.95 target。 在worst档下，整个regeneration pipeline不可行。但这与reframing一致—— reframed paper不claim regeneration，而是characterization + toolkit for monitoring。 Item generation结果完全dropped，不进appendix（避免给审稿人攻击面）。\\n\"\n  },\n  {\n    \"name\": \"cumulative_bayesian_dif\",\n    \"description\": \"Implement cumulative Bayesian DIF priors (Sinharay et al., 2006). Simulate 4 successive administrations. Show cumulative power improvement.\\n\",\n    \"results\": {\n      \"n_simulated_administrations\": 4,\n      \"individual_admin_power\": 0.4,\n      \"cumulative_2_admin_power\": 0.49,\n      \"cumulative_3_admin_power\": 0.56,\n      \"cumulative_4_admin_power\": 0.61,\n      \"target_cumulative_3_power\": 0.7,\n      \"prior_specification_sensitivity\": \"results vary 0.48-0.64 across 3 prior choices\",\n      \"simulation_n_per_admin\": 200,\n      \"delta_simulated\": 1.0,\n      \"decision\": \"appendix_only\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 11: Cumulative DIF Power by Administration Count\",\n        \"columns\": [\n          \"n_administrations\",\n          \"power\",\n          \"target\",\n          \"gap\"\n        ],\n        \"rows\": [\n          [\n            1,\n            0.4,\n            0.7,\n            -0.3\n          ],\n          [\n            2,\n            0.49,\n            0.7,\n            -0.21\n          ],\n          [\n            3,\n            0.56,\n            0.7,\n            -0.14\n          ],\n          [\n            4,\n            0.61,\n            0.7,\n            -0.09\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cumulative Bayesian DIF不达标，但不是blocking issue——reframed paper不依赖 longitudinal monitoring power。移至appendix作为future work motivation。\\n\\n\\nCumulative Bayesian DIF在worst档下power improvement不达标。3次administration 后power仅0.56（target 0.70），4次仅0.61。原因：Sinharay et al.的方法假设successive administrations的examinee populations来自same distribution（exchangeable）， 但LLM benchmarks中successive cohorts的ability distribution系统性shift（新模型 systematically stronger）。Prior accumulation被ability drift corrupted—— previous administrations的DIF evidence可能来自ability confound而非genuine item change， 累积这些evidence amplifies bias而非reduces noise。Prior specification sensitivity 也高（0.48-0.64 range），意味着结果依赖于subjective prior choice。 在worst档下，这是simulation-only结果，没有real data validation，审稿人视为 underdeveloped。Reframed paper中作为appendix \\\"future direction\\\" sketch保留， 但不占main body任何空间。\\n\"\n  },\n  {\n    \"name\": \"graceful_degradation_analysis\",\n    \"description\": \"Formal analysis of benchmark validity under progressive item replacement. Simulate 5%-50% replacement, measure ranking stability and construct coverage.\\n\",\n    \"results\": {\n      \"replacement_5pct_rho\": 0.998,\n      \"replacement_10pct_rho\": 0.994,\n      \"replacement_20pct_rho\": 0.981,\n      \"replacement_50pct_rho\": 0.937,\n      \"construct_coverage_5pct\": 0.97,\n      \"construct_coverage_20pct\": 0.88,\n      \"construct_coverage_50pct\": 0.71,\n      \"reliability_alpha_original\": 0.94,\n      \"reliability_alpha_20pct_replaced\": 0.86,\n      \"reliability_alpha_50pct_replaced\": 0.74,\n      \"theoretical_bound_rho_at_31pct\": 0.969,\n      \"decision\": \"appendix_supplementary\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 12: Graceful Degradation Under Replacement\",\n        \"columns\": [\n          \"replacement_pct\",\n          \"ranking_rho\",\n          \"reliability_alpha\",\n          \"coverage\"\n        ],\n        \"rows\": [\n          [\n            0,\n            1.0,\n            0.94,\n            1.0\n          ],\n          [\n            5,\n            0.998,\n            0.93,\n            0.97\n          ],\n          [\n            10,\n            0.994,\n            0.91,\n            0.93\n          ],\n          [\n            20,\n            0.981,\n            0.86,\n            0.88\n          ],\n          [\n            31,\n            0.969,\n            0.85,\n            0.82\n          ],\n          [\n            50,\n            0.937,\n            0.74,\n            0.71\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"结果支持\\\"monitoring over remediation\\\"的operational message。在worst档下， 直接item removal/replacement不是viable strategy for 31% instability。 Reframed paper中作为operational guidance的evidence basis。\\n\\n\\nGraceful degradation分析在worst档下显示replacement不如预期robust。20% replacement 时rho=0.981尚可接受，但reliability从0.94降到0.86——接近educational testing的 minimum threshold（0.85）。50% replacement时reliability=0.74，clearly unacceptable。 Construct coverage也rapidly degrades——替换items无法maintain MMLU的57-subject knowledge structure。这组结果在worst档下strengthens \\\"instability ≠ invalidity\\\" narrative的另一面：removing unstable items 不是好的remediation strategy（at 31%, reliability drops to ~0.85 boundary）。但它也意味着DIF-based benchmark maintenance （audit protocol的\\\"act\\\" tier at C%>25）在operational上是risky的。 Reframed paper中，这个结果支持\\\"characterize, don't fix\\\"的message—— 用一段话在Discussion中提及，详细数据移appendix。\\n\"\n  },\n  {\n    \"name\": \"item_focused_trees\",\n    \"description\": \"Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative to categorical cohort DIF. Treat model release date as continuous covariate.\\n\",\n    \"results\": {\n      \"ift_implemented\": true,\n      \"ift_n_items_flagged\": 2847,\n      \"ift_dif_pct\": 22.8,\n      \"ift_vs_mh_jaccard\": 0.52,\n      \"ift_vs_mh_concordance\": 0.71,\n      \"ift_split_points_temporal\": \"majority split at 2023-Q3 to 2024-Q1\",\n      \"ift_nonlinear_dif_detected\": 312,\n      \"ift_rmsea_improvement\": null,\n      \"ift_advantage\": \"avoids arbitrary cohort splits\",\n      \"ift_disadvantage\": \"tree instability — different random seeds yield different splits\",\n      \"tree_stability_jaccard_across_seeds\": 0.63,\n      \"decision\": \"appendix_robustness_check\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 13: IFT vs MH-DIF Comparison\",\n        \"columns\": [\n          \"method\",\n          \"c_pct\",\n          \"unique_flags\",\n          \"overlap_jaccard\"\n        ],\n        \"rows\": [\n          [\n            \"MH-DIF\",\n            31.3,\n            1583,\n            0.52\n          ],\n          [\n            \"IFT\",\n            22.8,\n            512,\n            0.52\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"IFT结果在worst档下是double-edged：支持temporal split的合理性，但method disagreement （Jaccard=0.52）加入审稿人的\\\"method-dependent results\\\"narrative。Appendix only。\\n\\n\\nIFT在worst档下给出与MH partially concordant但不fully consistent的结果。 C%=22.8%（低于MH的31.3%），Jaccard=0.52——meaning approximately half the items flagged by each method are unique to that method。IFT的优势（continuous covariate, no arbitrary split）被tree instability抵消——across random seeds的Jaccard仅0.63， 意味着IFT结果本身不reproducible。IFT发现312个nonlinear DIF items（difficulty change is non-monotonic over time），这是MH无法detect的，但在worst档下审稿人视为 \\\"additional evidence that the signal is noisy and method-dependent, not that nonlinear DIF is a real phenomenon\\\"。IFT的split points集中在2023-Q3到2024-Q1， 与temporal cohort split大致对齐——这验证了temporal split的合理性，但也意味着 IFT没有提供fundamentally new information。在reframed paper中作为appendix robustness check保留，main body一句话提及\\\"results qualitatively consistent with continuous-covariate alternative\\\"。\\n\"\n  },\n  {\n    \"name\": \"architecture_stratified_dif\",\n    \"description\": \"Run DIF within architecture-homogeneous decoder-only subpopulation. Report IRT fit diagnostics. Compare C% and detection power vs full population.\\n\",\n    \"results\": {\n      \"n_decoder_only\": 5226,\n      \"n_non_decoder\": 1,\n      \"pct_decoder_only\": 99.98,\n      \"decoder_only_c_pct\": 31.3,\n      \"decoder_only_jaccard_vs_full\": 1.0,\n      \"irt_rmsea_full\": 0.094,\n      \"irt_rmsea_decoder_only\": 0.094,\n      \"irt_cfi_full\": 0.68,\n      \"irt_cfi_decoder_only\": 0.68,\n      \"fit_improvement\": \"none — removing 1 model changes nothing\",\n      \"conclusion\": \"architecture heterogeneity is not the source of IRT misfit\",\n      \"real_source_of_misfit\": \"57-subject multidimensionality + non-normal ability distribution\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 14: Architecture Stratification (Moot)\",\n        \"columns\": [\n          \"population\",\n          \"n_models\",\n          \"c_pct\",\n          \"rmsea\",\n          \"cfi\"\n        ],\n        \"rows\": [\n          [\n            \"full\",\n            5227,\n            31.3,\n            0.094,\n            0.68\n          ],\n          [\n            \"decoder-only\",\n            5226,\n            31.3,\n            0.094,\n            0.68\n          ],\n          [\n            \"delta\",\n            1,\n            0.0,\n            0.0,\n            0.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"实验本身结论正确（architecture不是问题），但在worst档下被视为wasted space。 Reframed paper中压缩为半句话。\\n\\n\\nArchitecture stratification在worst档下确认了一个重要但trivial的finding： METABENCH MMLU是99.98% decoder-only（5226/5227），removing 1个non-decoder model changes absolutely nothing。C%不变（31.3%），Jaccard=1.0，IRT fit不变。 这experiment本身是correct（排除architecture heterogeneity作为concern）， 但在worst档下审稿人说：\\\"我们从未argue architecture heterogeneity是问题——问题是 57-subject multidimensionality + 非正态ability distribution + model non-independence。 你们排除了一个straw man concern\\\"。IRT fit仍然terrible（RMSEA=0.094, CFI=0.68）， 因为真正的misfit来源（multidimensionality）没有被addressed。 在reframed paper中，architecture homogeneity作为一句话fact（\\\"METABENCH MMLU is 99.98% decoder-only\\\"）报告，不需要单独实验。\\n\"\n  },\n  {\n    \"name\": \"semi_synthetic_contamination_validation\",\n    \"description\": \"Inject known contamination into real METABENCH response matrix. Measure DIF detection power under controlled ground truth. Vary injection parameters.\\n\",\n    \"results\": {\n      \"n_clean_items_selected\": 500,\n      \"n_injected_items\": 150,\n      \"temporal_external_tpr_p03\": 0.39,\n      \"temporal_external_tpr_p05\": 0.58,\n      \"temporal_external_tpr_p07\": 0.74,\n      \"temporal_external_tpr_p10\": 0.87,\n      \"temporal_external_fpr\": 0.318,\n      \"temporal_external_delta_tpr_p03\": 0.07,\n      \"temporal_external_delta_tpr_p05\": 0.26,\n      \"temporal_external_delta_tpr_p07\": 0.42,\n      \"temporal_external_delta_tpr_p10\": 0.55,\n      \"ability_external_tpr_p10\": 0.62,\n      \"ability_external_delta_tpr_p10\": 0.19,\n      \"fpr_inflation_at_p10_standard\": \"0.298_to_0.58\",\n      \"matching_variable_contamination\": true,\n      \"cross_subject_matching_delta_fpr\": 0.003,\n      \"replication_delta_tpr_range\": \"[0.25, 0.40]\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 15: Semi-Synthetic ΔTPR Under Worst Tier\",\n        \"columns\": [\n          \"injection_p\",\n          \"tpr\",\n          \"baseline_fpr\",\n          \"delta_tpr\",\n          \"registry_delta_tpr\"\n        ],\n        \"rows\": [\n          [\n            0.3,\n            0.39,\n            0.318,\n            0.07,\n            0.222\n          ],\n          [\n            0.5,\n            0.58,\n            0.318,\n            0.26,\n            0.508\n          ],\n          [\n            0.7,\n            0.74,\n            0.318,\n            0.42,\n            0.664\n          ],\n          [\n            1.0,\n            0.87,\n            0.318,\n            0.55,\n            0.674\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 16: Cross-Subject vs Within-Subject Matching\",\n        \"columns\": [\n          \"matching\",\n          \"delta_fpr\",\n          \"delta_tpr_p05\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"within-subject\",\n            \"+0.186\",\n            0.34,\n            \"FPR inflation — contaminated matching var\"\n          ],\n          [\n            \"cross-subject\",\n            \"+0.003\",\n            0.26,\n            \"FPR stable — anchor finding preserved\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Semi-synthetic framework在worst档下power减弱但core innovation（cross-subject matching, ΔFPR≈0）preserved。这成为reframed paper的anchor contribution——framework本身 不依赖IRT assumptions，是portable的method contribution。Power limitations honestly reported。\\n\\n\\nSemi-synthetic在worst档下ΔTPR显著低于registry记录。P=0.5时ΔTPR=0.26（registry为 0.508），p=1.0时ΔTPR=0.55（registry为0.674）。差异来源：worst档下的injection 使用更conservative的parameter choices——injected items选自difficulty分布中间段 （避免easy items的ceiling effect），focal group size更接近minimum（N≈100 vs registry的N=807），exploitation rate的effective signal更小（因为\\\"clean\\\" baseline items本身已有31%被flag为C-class，diluting the injection signal）。 关键问题：baseline FPR=0.318意味着没有injection时就有31.8%的items被flag—— ΔTPR必须在这个high baseline上demonstrate增量，signal-to-noise ratio差。 Cross-subject matching仍然有效（ΔFPR≈0.003，接近zero），这是anchor finding。 但ΔTPR的magnitude（worst档0.25-0.40）审稿人判定为\\\"moderate at best — the framework works but detection power is underwhelming\\\"。 在reframed paper中，semi-synthetic framework仍是anchor contribution—— 但framing从\\\"powerful detection tool\\\"变为\\\"principled validation infrastructure with known power limitations\\\"。\\n\"\n  },\n  {\n    \"name\": \"multi_benchmark_temporal_dif\",\n    \"description\": \"Run temporal DIF on additional benchmarks from METABENCH (ARC, HellaSwag, WinoGrande, TruthfulQA, MMLU-Pro). Address \\\"only MMLU\\\" concern.\\n\",\n    \"results\": {\n      \"mmlu_c_pct\": 31.3,\n      \"mmlu_permutation_null\": 16.4,\n      \"mmlu_effective\": 14.9,\n      \"arc_c_pct\": 13.8,\n      \"arc_permutation_null\": 9.2,\n      \"arc_effective\": 4.6,\n      \"hellaswag_c_pct\": 10.1,\n      \"hellaswag_permutation_null\": 7.8,\n      \"hellaswag_effective\": 2.3,\n      \"winogrande_c_pct\": 14.7,\n      \"winogrande_permutation_null\": 10.1,\n      \"winogrande_effective\": 4.6,\n      \"truthfulqa_c_pct\": 22.4,\n      \"truthfulqa_permutation_null\": 14.8,\n      \"truthfulqa_effective\": 7.6,\n      \"gsm8k_c_pct\": 12.4,\n      \"gsm8k_permutation_null\": 8.7,\n      \"gsm8k_effective\": 3.7,\n      \"cross_benchmark_raw_range\": \"10.1-31.3%\",\n      \"cross_benchmark_effective_range\": \"2.3-14.9%\",\n      \"all_random_controls_below_1pct\": true,\n      \"mmlu_pro_not_available\": true\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 17: Multi-Benchmark DIF Summary (Worst Tier)\",\n        \"columns\": [\n          \"benchmark\",\n          \"n_items\",\n          \"raw_c_pct\",\n          \"permutation_null\",\n          \"effective_c_pct\",\n          \"random_control\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            12508,\n            31.3,\n            16.4,\n            14.9,\n            0.18\n          ],\n          [\n            \"TruthfulQA\",\n            817,\n            22.4,\n            14.8,\n            7.6,\n            0.37\n          ],\n          [\n            \"WinoGrande\",\n            1267,\n            14.7,\n            10.1,\n            4.6,\n            0.32\n          ],\n          [\n            \"ARC\",\n            1172,\n            13.8,\n            9.2,\n            4.6,\n            0.6\n          ],\n          [\n            \"GSM8K\",\n            1319,\n            12.4,\n            8.7,\n            3.7,\n            0.3\n          ],\n          [\n            \"HellaSwag\",\n            10042,\n            10.1,\n            7.8,\n            2.3,\n            0.28\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Multi-benchmark结果在worst档下是mixed news。好消息：all benchmarks show above-chance DIF（random controls <1%）。坏消息：effective signal after permutation controls 很小for most benchmarks。Reframed paper必须honest about这个range。\\n\\n\\nMulti-benchmark分析在worst档下揭示一个devastating pattern：raw C%在所有benchmarks 上都>10%（range 10.1-31.3%），但permutation null也consistently高（7.8-16.4%）， 扣除后effective C%范围仅2.3-14.9%。MMLU的effective C%最高（14.9%）因为它有最多subjects （57）和最大item pool（12508），提供更多opportunities for heterogeneity。 HellaSwag effective C%最低（2.3%），因为it's a relatively homogeneous task （sentence completion）——item-level behavioral heterogeneity genuinely lower。 Cross-benchmark heterogeneity本身是informative的（\\\"different benchmarks have different stability profiles\\\"），但审稿人concern是：\\\"if after permutation controls some benchmarks show <5% effective C%, your '31% instability' headline is MMLU-specific and cannot be generalized\\\"。在worst档下，\\\"31%\\\"的headline number必须qualified with \\\"before permutation controls; effective rate 10-18% depending on benchmark\\\"。 Reframed paper中，cross-benchmark heterogeneity成为characterization的一部分： \\\"benchmark stability varies from 2% (HellaSwag) to 15% (MMLU) — we provide benchmark-specific profiles\\\"。\\n\"\n  },\n  {\n    \"name\": \"permutation_null_c_rate\",\n    \"description\": \"1000× permutation test: randomly reassign 2023/2024 temporal labels, run MH-DIF each time. Establish null distribution for C%.\\n\",\n    \"results\": {\n      \"n_permutations\": 1000,\n      \"null_c_pct_mean\": 16.4,\n      \"null_c_pct_sd\": 2.1,\n      \"null_c_pct_95ci\": [\n        12.6,\n        20.3\n      ],\n      \"null_c_pct_min\": 10.8,\n      \"null_c_pct_max\": 22.7,\n      \"observed_c_pct\": 31.3,\n      \"z_score\": 7.1,\n      \"p_value\": \"<1e-12\",\n      \"effective_c_pct\": 14.9,\n      \"fraction_spurious\": 0.524,\n      \"null_mechanism\": \"cohort composition differences (ability, family structure, training vintage) generate substantial DIF even without temporal signal\",\n      \"random_split_within_cohort_c_pct\": 0.18,\n      \"permutation_vs_random_split_gap\": \"16.4 vs 0.18 — temporal label permutation preserves between-cohort structure\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 18: Permutation Null Distribution\",\n        \"columns\": [\n          \"statistic\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"null_mean_c_pct\",\n            16.4\n          ],\n          [\n            \"null_sd\",\n            2.1\n          ],\n          [\n            \"null_95_ci\",\n            \"[12.6, 20.3]\"\n          ],\n          [\n            \"observed_c_pct\",\n            31.3\n          ],\n          [\n            \"z_score\",\n            7.1\n          ],\n          [\n            \"effective_c_pct\",\n            14.9\n          ],\n          [\n            \"fraction_spurious\",\n            \"52.4%\"\n          ],\n          [\n            \"random_split_c_pct\",\n            0.18\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 19: Decomposition of Observed C%\",\n        \"columns\": [\n          \"source\",\n          \"contribution_pct\",\n          \"mechanism\"\n        ],\n        \"rows\": [\n          [\n            \"genuine_temporal_signal\",\n            14.9,\n            \"item-level behavioral change across model generations\"\n          ],\n          [\n            \"cohort_composition\",\n            16.4,\n            \"ability distribution + family structure + training vintage differences\"\n          ],\n          [\n            \"total\",\n            31.3,\n            \"N/A\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Permutation null是worst档论文的central finding。它将31%的headline number decompose为 ~15% genuine + ~16% spurious。Reframed paper必须lead with这个decomposition： \\\"we observe 31% raw behavioral heterogeneity, of which approximately half persists after permutation controls — the remainder reflects cohort composition differences that MH-DIF's total-score conditioning cannot absorb\\\"。这honest framing比 原来的\\\"31% instability\\\"更defensible，但也更modest。\\n\\n\\nPermutation null是worst档的defining experiment。1000次permutation（保持group sizes N_ref=1080, N_foc=807不变，但随机打乱temporal labels）产生mean C%=16.4%（SD=2.1%）， 95% range [12.6, 20.3]。这意味着即使temporal labels是random的，仅因为两组models 的composition差异（ability distribution overlap=76.4%, 不同model families的比例差异, 不同training data vintages的representation差异），MH-DIF就会flag 12-20%的items。\\n关键区分：这不是与random-split control（0.18%）矛盾。Random split是within-cohort的 （same time period, same family composition），而permutation null是between-cohort的 （preserves the actual model composition, just shuffles temporal labels）。 The 16.4% null arises because models from 2023 and 2024 genuinely differ in ways beyond temporal signal — model families, training approaches, scale distributions all differ between cohorts. MH's ability conditioning (total score) cannot absorb all these confounds.\\nObserved 31.3% is still z=7.1 above null（p<1e-12），so temporal signal EXISTS beyond cohort composition. But 52.4% of the raw C% is attributable to cohort composition effects, not temporal item-level change. Effective C%=14.9%。\\n在worst档下，审稿人的reaction： \\\"这证实了我们的concern——31%中一半以上是cohort composition artifact。MH-DIF 在LLM context下的conditioning is fundamentally insufficient。14.9%可能也包含 未被permutation null capture的confounds（tokenizer changes, training data composition within families）。The genuine temporal item-level signal may be even smaller。\\\"\\n\"\n  },\n  {\n    \"name\": \"odds_ratio_regression_transparency\",\n    \"description\": \"Supplement pseudo R² with odds ratio, CI, McFadden/Nagelkerke R², deviance ratio. Add item-level accuracy change as predictor.\\n\",\n    \"results\": {\n      \"model1_domain_delta\": {\n        \"mcfadden_r2\": 0.0007,\n        \"nagelkerke_r2\": 0.0012,\n        \"or_per_010\": 1.55,\n        \"or_ci\": [\n          1.19,\n          2.03\n        ]\n      },\n      \"model2_domain_plus_items\": {\n        \"mcfadden_r2\": 0.0423,\n        \"nagelkerke_r2\": 0.072,\n        \"or_domain_per_010\": 0.73,\n        \"or_difficulty_per_010\": 0.78,\n        \"or_discrimination_per_010\": 1.51\n      },\n      \"model3_item_delta\": {\n        \"mcfadden_r2\": 0.0012,\n        \"nagelkerke_r2\": 0.0021,\n        \"or_item_change_per_010\": 1.08,\n        \"or_item_ci\": [\n          1.51,\n          2.96\n        ]\n      },\n      \"model4_full\": {\n        \"mcfadden_r2\": 0.0434,\n        \"nagelkerke_r2\": 0.0737,\n        \"or_item_change_per_010\": 0.92,\n        \"or_difficulty_per_010\": 0.77,\n        \"or_discrimination_per_010\": 1.54\n      },\n      \"simpsons_paradox\": true,\n      \"simpsons_direction\": \"item accuracy change OR flips from 1.08 to 0.92 when controlling for item properties\",\n      \"deviance_explained_by_item_props\": \"96% of model variance from difficulty + discrimination, not accuracy change\",\n      \"lr_test_m1_vs_m2_chi2\": 647,\n      \"lr_test_m3_vs_m4_chi2\": 656\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 20: Logistic Regression Hierarchy\",\n        \"columns\": [\n          \"model\",\n          \"predictors\",\n          \"mcfadden_r2\",\n          \"nagelkerke_r2\",\n          \"key_or\"\n        ],\n        \"rows\": [\n          [\n            \"M1\",\n            \"domain_Δacc\",\n            0.0007,\n            0.0012,\n            \"1.55 [1.19-2.03]\"\n          ],\n          [\n            \"M2\",\n            \"domain_Δacc + item_props\",\n            0.0423,\n            0.072,\n            \"0.73 (Δacc flips)\"\n          ],\n          [\n            \"M3\",\n            \"item_Δacc\",\n            0.0012,\n            0.0021,\n            \"1.08\"\n          ],\n          [\n            \"M4\",\n            \"item_Δacc + item_props\",\n            0.0434,\n            0.0737,\n            \"0.92 (Δacc flips)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Regression transparency strengthens honest framing但也gives审稿人ammunition： \\\"item properties explain 50× more variance than accuracy change — DIF may be a statistical artifact of item difficulty/discrimination structure\\\"。 Reframed paper must address this directly。\\n\\nOdds ratio regression在worst档下confirms并extends原有findings。Domain-level accuracy change（Model 1）是significant但tiny predictor（R²=0.0007）。Item-level accuracy change（Model 3）marginally better（R²=0.0012）但still near zero。 Simpson's paradox preserved：item accuracy change OR从1.08降到0.92 when controlling for item properties——meaning higher-accuracy-change items are actually LESS likely to be DIF after controlling for difficulty and discrimination。\\n在worst档下，审稿人的worst-case解读：\\\"item difficulty和discrimination explains 7% of DIF variance（Model 4 R²=0.0737）。这虽然不高in absolute terms，但比accuracy change高50倍。DIF flags与item properties相关——harder, more discriminating items 更likely被flag。这可能是MH statistic的statistical property（高discrimination items 产生更大的α_MH estimates），而非genuine item-level behavioral change\\\"。\\nPlan_027的d=-0.17被审稿人认为是marginal的ability gap，但temporal label可能proxy 其他未控制confound（training data composition, tokenizer changes, RLHF procedures）。 这些confounds不会被total score matching absorb。\\n在reframed paper中，regression transparency section支持honest framing：\\\"DIF flags are weakly predicted by accuracy change but moderately predicted by item properties — we report this transparently as part of our characterization\\\"。\\n\"\n  }\n]",
      "numLines": 1108,
      "startLine": 1,
      "totalLines": 1108
    }
  },
  "sourceToolAssistantUUID": "010fc2ec-8285-48a3-824c-92a9612a9a3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T17:28:41.740Z_

<details><summary>↩ Tool result · `toolu_01MJPwY7nMUevAJJ6MX4v6LX`</summary>

```text
1	# Paper Framing — irt_equated_bench_regen
2	
3	## Target Venue
4	- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)
5	- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)
6	
7	## Paper Type
8	Empirical analysis / psychometric characterization. Discovery paper, not methods paper. "DIF reveals benchmark structural problems," not "DIF detects contamination."
9	
10	## Core Claims (4 条, 可证伪)
11	
12	**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).
13	- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)
14	- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.
15	- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.
16	
17	**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).
18	- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)
19	- Framing: aggressive — "the field's standard validation approach is fundamentally mismatched for item-level detection" — now with direct empirical evidence, not just conceptual argument
20	
21	**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).
22	- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)
23	- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks
24	- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability
25	
26	**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:
27	1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.
28	2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies "items that changed across generations," not "good items."
29	3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not "find bad items and remove" but "understand what changed and why." Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.
30	4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.
31	- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)
32	- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.
33	- Growing Pains互补: "Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading"
34	- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed
35	
36	## Story Spine (v2 — no-pivot narrative)
37	
38	**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.
39	
40	**Key narrative principle**: "Instability ≠ invalidity." DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**
41	
42	**What we find** (4 contributions, focused):
43	
44	1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for "models got better."
45	
46	2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.
47	
48	3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.
49	
50	4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).
51	
52	**Headline result**: "Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance."
53	
54	## Scope Control (main body vs appendix)
55	
56	**MAIN BODY (4 claims + robustness)**:
57	- §1 Introduction (problem + "instability ≠ invalidity" framing upfront)
58	- §2 Related Work (45 papers, 5 clusters)
59	- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)
60	- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)
61	- §5 Discussion + Limitations
62	- §6 Conclusion
63	
64	**APPENDIX (pruned from main body)**:
65	- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped
66	- RL robustness (plan_002) — N=13, underpowered
67	- Ensemble fusion (plan_003a/b/c) — negative, not executed
68	- Bifactor equating pilot — below target fit
69	- Item generation pilot — below benchmarks
70	- Graceful degradation — clean but supplementary
71	- Item-Focused Trees — robustness check, supplementary
72	- ConStat/DVD comparisons — complementary baselines
73	
74	## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks
75	
76	Systematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.
77	
78	## Venue Fit
79	
80	- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. "Empirical, not algorithmic" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.
81	
82	## Novelty Articulation (三层，显式化)
83	
84	MH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:
85	
86	1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.
87	
88	2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).
89	
90	3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).
91	
92	**Framing**: "We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm."
93	
94	## Anticipated Reviewer Concerns (updated for pivot)
95	
96	1. **"31% could just mean models got better / ability confound inflates C%"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.
97	
98	2. **"Ground truth critique is obvious — of course web labels don't capture differential effects"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.
99	
100	3. **"Semi-synthetic injection is artificial"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.
101	
102	4. **"DIF power is only sufficient for large effects"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.
103	
104	5. **"Only validated on MMLU"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.
105	
106	6. **"Higher methods (MIMIC, propensity-score) could solve the confounding"** — Acknowledged as future work. We frame our three-attempt negative results as "empirical observation" that motivates these directions, not as impossibility.
107	
108	7. **"ETS threshold is uncalibrated for LLM populations"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: "finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF." Do NOT claim ">15% at all thresholds" — be honest that 2.5 drops below.
109	
110	8. **"Multiple testing: 12,508 simultaneous tests without correction"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.
111	
112	9. **"Only uniform DIF — non-uniform DIF plausible for LLMs"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: "our 31% uniform-only estimate is conservative."
113	
114	10. **"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.
115	
116	11. **"Ranking disruption result is tautological"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.
117	
118	## Dropped from Original Framing
119	
120	- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.
121	- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.
122	- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.
123	- **Detection as primary contribution**: Pivoted from "we detect contamination" to "we characterize benchmark properties."
124	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9dd1829e-4203-4d8b-b70c-ae1fec16e090",
  "isSidechain": false,
  "promptId": "9377956b-ace9-4b16-82d2-21e10f437ea9",
  "type": "user",
  "uuid": "e17293e0-af6f-4334-92df-06fe2f8e5fd5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/paper_framing.md",
      "content": "# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n",
      "numLines": 124,
      "startLine": 1,
      "totalLines": 124
    }
  },
  "sourceToolAssistantUUID": "9dd1829e-4203-4d8b-b70c-ae1fec16e090",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T165710 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "499e88ab-0b0d-4bfb-8ff7-d41c4cabd390",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream benchmark analysis",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e"
}
```

---

### Assistant

_source line 14 · 2026-05-21T17:29:26.532Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me write a complete LaTeX paper for the "worst" tier dream. The narrative guidance says:

1. Reframe as pure empirical characterization: "Large-Scale Item-Level Stability Analysis of LLM Benchmarks"
2. MH statistic downgraded to nonparametric group-comparison test, no latent trait interpretation
3. Semi-synthetic framework as anchor contribution
4. Item-level stability as operational metric for benchmark maintenance
5. Permutation null reveals 12-20% spurious C%, meaning ~half of the 31% is from cohort composition


6. RL robustness failure further weakens DIF as stable detector
7. 98% IRT misfit plus unidimensional assumption on 57-subject benchmark makes reviewers question whether MH-DIF results are even interpretable without multidimensional IRT
8. Ground truth meta-critique gets dismissed as straw man
9. Ability confound at 2.4pp likely underestimated

I need to honestly present all the weaknesses and reviewer criticisms while keeping the paper coherent and readable, letting the worst-case interpretation guide how results are framed. Now I'm structuring the paper with Abstract, Introduction, Related Work, and Method sections.

For the experiments, I'm laying out the full empirical evaluation across multiple dimensions: temporal DIF patterns on MMLU, permutation null tests, multi-benchmark comparisons, RL robustness checks, semi-synthetic validation, alternative detector comparisons like ConStat and DVD, IRT model fit diagnostics, regression analyses, cross-benchmark results on GSM8K, and graceful degradation tests.

Now I'm realizing the page constraint forces me to be ruthless about what goes in the main body versus appendix. The core narrative needs to center on temporal DIF with permutation null decomposition as the anchor finding, then multi-benchmark evidence showing this is MMLU-specific, semi-synthetic validation proving the effect is real, RL robustness failure demonstrating cohort-dependence, and alternative detector disagreement revealing the detection challenge. The IRT model fit failure, regression transparency, cross-benchmark GSM8K results, and graceful degradation can move to supplementary material, though I should still include odds ratio analysis for completeness. I'm seeing that I've listed too many subsections—I need to consolidate these experiments more efficiently. Let me map out which tables correspond to which core experiments and group related analyses together rather than giving each its own section. I'm mapping out the paper structure with four main experiments highlighted in the results section—temporal stability on MMLU, permutation null decomposition, multi-benchmark profiles, and cross-benchmark validation on GSM8K—plus the semi-synthetic validation framework and RL robustness analysis. Writing the LaTeX paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e17293e0-af6f-4334-92df-06fe2f8e5fd5",
  "isSidechain": false,
  "requestId": "req_011CbG7Gb1Jtzncckh7Mdfp6",
  "type": "assistant",
  "uuid": "d3f5c0b3-2888-4b45-a309-df3af4775692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNHbJjXp4zR9Pg9uMMgTJj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24820,
      "cache_read_input_tokens": 24252,
      "output_tokens": 2271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2271,
          "cache_read_input_tokens": 24252,
          "cache_creation_input_tokens": 24820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24820
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

_source line 15 · 2026-05-21T17:29:26.571Z_

Now let me check the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3f5c0b3-2888-4b45-a309-df3af4775692",
  "isSidechain": false,
  "requestId": "req_011CbG7Gb1Jtzncckh7Mdfp6",
  "type": "assistant",
  "uuid": "7e78c26d-6bbb-4b27-894f-bcd0778afb44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNHbJjXp4zR9Pg9uMMgTJj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24820,
      "cache_read_input_tokens": 24252,
      "output_tokens": 2271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2271,
          "cache_read_input_tokens": 24252,
          "cache_creation_input_tokens": 24820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24820
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

_source line 16 · 2026-05-21T17:29:28.706Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01X3p4fYDSM8uGUDHciVaDWL`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/",
  "description": "List worst-tier output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e78c26d-6bbb-4b27-894f-bcd0778afb44",
  "isSidechain": false,
  "requestId": "req_011CbG7Gb1Jtzncckh7Mdfp6",
  "type": "assistant",
  "uuid": "f2129a08-1cf4-4dc7-be39-9c10e522d207",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNHbJjXp4zR9Pg9uMMgTJj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24820,
      "cache_read_input_tokens": 24252,
      "output_tokens": 2271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2271,
          "cache_read_input_tokens": 24252,
          "cache_creation_input_tokens": 24820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24820
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

_source line 17 · 2026-05-21T17:29:28.899Z_

<details><summary>↩ Tool result · `toolu_01X3p4fYDSM8uGUDHciVaDWL`</summary>

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
  "parentUuid": "f2129a08-1cf4-4dc7-be39-9c10e522d207",
  "isSidechain": false,
  "promptId": "9377956b-ace9-4b16-82d2-21e10f437ea9",
  "type": "user",
  "uuid": "c6993246-73f6-4c36-939f-947b8616940d",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f2129a08-1cf4-4dc7-be39-9c10e522d207",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-21T17:29:32.122Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6993246-73f6-4c36-939f-947b8616940d",
  "isSidechain": false,
  "requestId": "req_011CbG7L4KD4DuhGGqFFJARU",
  "type": "assistant",
  "uuid": "8f00525a-f82c-455f-8e8e-bfcce5743806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136tdaxG37zuP9jsqfksb9f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2298,
      "cache_read_input_tokens": 49072,
      "output_tokens": 12293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12293,
          "cache_read_input_tokens": 49072,
          "cache_creation_input_tokens": 2298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2298
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

_source line 19 · 2026-05-21T17:33:22.869Z_

<details open><summary>🔧 Tool call — Write · `toolu_017wceqdjiTpJzivqhkQpUjX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{geometry}\n\\geometry{margin=1in}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{array}\n\\usepackage{caption}\n\\captionsetup{font=small}\n\n\\title{Large-Scale Item-Level Stability Analysis of LLM Benchmarks}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nLLM benchmarks implicitly assume that item difficulty is stable across model generations, yet this assumption has never been tested at scale. We apply the Mantel-Haenszel (MH) statistic---a nonparametric group-comparison test---to the METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items) and find that 31.3\\% of items exhibit large behavioral heterogeneity between 2023 and 2024-H1 model cohorts (ETS C class, $|\\Delta_{\\text{MH}}| \\geq 1.5$). However, a 1,000-iteration permutation null reveals that approximately 16.4\\% of this rate is attributable to cohort composition differences rather than genuine temporal change, yielding an effective rate of 14.9\\%. Replication across five additional benchmarks shows effective rates ranging from 2.3\\% (HellaSwag) to 7.6\\% (TruthfulQA), with MMLU as an outlier. We introduce a semi-synthetic validation framework with cross-subject matching that eliminates false-positive inflation ($\\Delta$FPR $= 0.003$), providing reusable infrastructure for validating any item-level detector. We further show that reasoning-RL models destabilize DIF flags (Jaccard $= 0.43$), that three independent detection methods (MH-DIF, ConStat, DVD) flag nearly disjoint item sets (pairwise Jaccard $0.11$--$0.19$), and that both unidimensional and bifactor IRT models are severely misspecified for MMLU (CFI $< 0.72$, RMSEA $> 0.08$). These findings collectively characterize item-level stability as a benchmark-specific, method-dependent, and cohort-sensitive property, motivating monitoring-over-remediation approaches to benchmark maintenance.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nWhen we report that a 2024 model scores 78\\% on MMLU while a 2023 model scores 65\\%, we implicitly assume both scores reflect the same measurement construct---that item difficulty is stable across model generations. Psychometrics calls violations of this assumption \\textit{differential item functioning} (DIF): an item exhibits DIF when examinees of equal ability from different groups have different probabilities of answering correctly.\n\nWe apply the Mantel-Haenszel (MH) statistic \\citep{mantel1959statistical,holland1988differential} to characterize item-level behavioral stability in the METABENCH repository \\citep{perlitz2024metabench}---5,227 models evaluated on 12,508 MMLU items. We treat MH strictly as a nonparametric $\\chi^2$ test for group$\\times$item interaction, without claiming latent-trait interpretation, since unidimensional IRT is fundamentally misspecified for MMLU's 57-subject structure (98\\% of models show $|L_z| > 2$; bifactor IRT also fails to converge with acceptable fit).\n\nOur central finding: 31.3\\% of MMLU items show large behavioral heterogeneity between temporal cohorts. A permutation null decomposes this into $\\sim$16.4\\% attributable to cohort composition differences and $\\sim$14.9\\% that persists after controls. We characterize this heterogeneity without claiming psychometric interpretation---it is an empirical property of how item response patterns differ across model generations.\n\nThree further findings shape the interpretation: (1)~reasoning-RL models fundamentally destabilize DIF flags (Jaccard~$= 0.43$), showing that flags are cohort-dependent; (2)~three independent detection methods flag nearly disjoint item sets (pairwise Jaccard $0.11$--$0.19$), suggesting a construct validity challenge across the field; (3)~a semi-synthetic validation framework with cross-subject matching provides principled infrastructure for evaluating any item-level detector, with known power limitations.\n\nWe frame item-level stability as an operational metric for benchmark maintenance: characterize, monitor, but do not remediate---removing 31\\% of items degrades reliability below acceptable thresholds.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{LLM Benchmark Contamination.} \\citet{li2024task} and \\citet{oren2024proving} document web-overlap as a proxy for benchmark contamination. Min-K\\% \\citep{shi2024detecting} and ConStat \\citep{dekoninck2024constat} detect contamination via model-internal signals. DVD \\citep{oren2024proving} uses generation variance. All validate against web-overlap labels, which measure global exposure rather than item-level differential effects.\n\n\\paragraph{Differential Item Functioning.} MH-DIF \\citep{holland1988differential} is the standard nonparametric method in educational testing. \\citet{sinharay2006bayesian} extend it to cumulative Bayesian frameworks. Item-Focused Trees \\citep{tutz2016item} treat covariates continuously. DIF has not previously been applied to LLM benchmark evaluation at scale.\n\n\\paragraph{Benchmark Stability.} \\citet{raju2024growing} identify ``growing pains'' in LLM evaluation via anchor-item methods. Our DIF analysis complements their work by identifying \\emph{which} items are degrading. \\citet{polo2024tinybenchmarks} show benchmark redundancy enables subsampling---consistent with our finding that ranking stability is maintained despite 31\\% item instability.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{MH-DIF as Nonparametric Group-Comparison Test}\n\nGiven a binary response matrix $\\mathbf{X} \\in \\{0,1\\}^{N \\times I}$ and a grouping variable $G \\in \\{\\text{ref}, \\text{foc}\\}$, the MH statistic tests whether the odds of a correct response differ between groups after stratifying by total score. The common odds ratio $\\alpha_{\\text{MH}}$ is converted to the ETS delta scale:\n\\begin{equation}\n\\Delta_{\\text{MH}} = -2.35 \\ln(\\alpha_{\\text{MH}})\n\\end{equation}\nItems are classified as A ($|\\Delta_{\\text{MH}}| < 1.0$), B ($1.0 \\leq |\\Delta_{\\text{MH}}| < 1.5$), or C ($|\\Delta_{\\text{MH}}| \\geq 1.5$) per ETS guidelines. We report C-class percentage (C\\%) as the primary instability metric.\n\nWe use MH strictly as a nonparametric test. Total-score stratification controls for overall ability without requiring a latent-trait model. This is critical: MMLU's 57-subject structure makes unidimensional IRT misspecified (Section~\\ref{sec:irt_fit}), and we do not claim that MH conditioning fully absorbs all confounds.\n\n\\subsection{Semi-Synthetic Validation Framework}\n\nTo validate detection power under controlled ground truth, we inject known differential contamination into real METABENCH response matrices. For selected ``clean'' items in the focal cohort, we flip incorrect$\\to$correct responses with probability $p \\in \\{0.3, 0.5, 0.7, 1.0\\}$ for a random subset of focal models, simulating contamination that differentially benefits newer models.\n\nThe key innovation is \\textbf{cross-subject matching}: when testing items from subject $s$, we use total score on all \\emph{other} subjects as the MH matching variable. This prevents the injected contamination from corrupting the conditioning variable. Detection power is measured as $\\Delta$TPR $=$ TPR$_{\\text{injected}}$ $-$ TPR$_{\\text{baseline}}$, and false-positive control as $\\Delta$FPR.\n\n\\subsection{Permutation Null}\n\nWe establish a null distribution for C\\% via 1,000 permutations: temporal labels (2023 vs.\\ 2024) are randomly reassigned while preserving group sizes, and MH-DIF is recomputed each time. The null mean C\\% quantifies how much behavioral heterogeneity arises from cohort composition alone (ability distribution, family structure, training vintage) rather than temporal signal.\n\n%==============================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n%==============================================================================\n\n\\subsection{Temporal DIF on MMLU}\n\\label{sec:temporal_dif}\n\nWe partition the 5,227 METABENCH MMLU models into reference (2023, $N = 1{,}080$) and focal (2024-H1, $N = 807$) cohorts. MH-DIF identifies 31.3\\% of 12,508 items as C-class. A random-split sanity check yields C\\% $= 0.18\\%$, confirming the signal is not a statistical artifact.\n\nWithin-family analysis shows elevated C\\%: Llama-2$\\to$3 at 61.3\\% and Mistral$\\to$Mixtral at 38.7\\%. However, these comparisons confound temporal change with architecture, data, and training procedure changes. Domain-level accuracy improvement correlates weakly with DIF rates ($\\rho = 0.307$, $p = 0.02$), but this ecological correlation on $N = 57$ subjects has limited item-level interpretability. Removing 15.4\\% negative-discrimination items reduces C\\% by only 1.2pp.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temporal DIF summary on MMLU.}\n\\label{tab:temporal_dif}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMetric & Raw & After Perm.\\ Control & Interpretation \\\\\n\\midrule\nC\\% & 31.3\\% & 14.9\\% & Inflated by cohort comp. \\\\\nEnrichment vs.\\ Li & 0.96 & 0.96 & Trivially expected \\\\\nIRT misfit & 98\\% $|L_z|{>}2$ & N/A & MH conditioning unreliable \\\\\nDomain $\\rho$ & 0.307 & N/A & Ecol.\\ fallacy on $N{=}57$ \\\\\nWithin-family C\\% & 38.7--61.3\\% & N/A & Architecture confounded \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cohort definition $\\times$ item filtering sensitivity.}\n\\label{tab:cohort_filtering}\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nCohort & Filter & C\\% & Effective C\\% \\\\\n\\midrule\nTemporal & All items & 31.3 & 14.9 \\\\\nTemporal & No neg-disc & 30.1 & 13.7 \\\\\nAbility & All items & 2.9 & N/A \\\\\nAbility & No neg-disc & 2.7 & N/A \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Permutation Null Decomposition}\n\\label{sec:permutation}\n\nThe 1,000-iteration permutation null yields mean C\\% $= 16.4\\%$ (SD $= 2.1\\%$, 95\\% CI $[12.6, 20.3]$). The observed 31.3\\% exceeds this null ($z = 7.1$, $p < 10^{-12}$), so temporal signal exists beyond cohort composition. However, 52.4\\% of the raw C\\% is attributable to cohort composition effects---ability distribution shift ($d = -0.17$), model family structure differences, and training data vintage variation---that MH's total-score conditioning cannot fully absorb.\n\nThe random-split control (C\\% $= 0.18\\%$) is not contradictory: random splits preserve within-cohort structure, while permutation preserves between-cohort composition differences. The 16.4\\% null arises specifically because 2023 and 2024 models differ in ways beyond temporal signal.\n\nEffective C\\% after permutation control is 14.9\\%: this represents item-level behavioral change that cannot be attributed to cohort composition alone. Even this figure may include residual confounds (tokenizer changes, training data composition within families) not captured by the permutation procedure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Permutation null distribution ($B = 1{,}000$).}\n\\label{tab:perm_null}\n\\begin{tabular}{@{}lr@{}}\n\\toprule\nStatistic & Value \\\\\n\\midrule\nNull mean C\\% & 16.4 \\\\\nNull SD & 2.1 \\\\\nNull 95\\% CI & $[12.6, 20.3]$ \\\\\nObserved C\\% & 31.3 \\\\\n$z$-score & 7.1 \\\\\nEffective C\\% & 14.9 \\\\\nFraction spurious & 52.4\\% \\\\\nRandom-split C\\% & 0.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Decomposition of observed C\\%.}\n\\label{tab:decomposition}\n\\begin{tabular}{@{}lrl@{}}\n\\toprule\nSource & C\\% & Mechanism \\\\\n\\midrule\nGenuine temporal & 14.9 & Item-level behavioral change \\\\\nCohort composition & 16.4 & Ability + family + vintage \\\\\n\\midrule\nTotal & 31.3 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Benchmark Stability Profiles}\n\\label{sec:multi_bench}\n\nWe replicate temporal DIF on five additional METABENCH benchmarks (Table~\\ref{tab:multi_bench}). Raw C\\% ranges from 10.1\\% (HellaSwag) to 31.3\\% (MMLU). After permutation controls, effective C\\% ranges from 2.3\\% to 14.9\\%. All random-split controls remain below 1\\%, confirming genuine between-cohort signal across benchmarks. MMLU's outlier status (14.9\\% effective) likely reflects its 57-subject structure providing more opportunities for heterogeneity. HellaSwag's low effective rate (2.3\\%) is consistent with its relatively homogeneous task structure (sentence completion).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-benchmark DIF summary.}\n\\label{tab:multi_bench}\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nBenchmark & $N_{\\text{items}}$ & Raw C\\% & Perm.\\ Null & Eff.\\ C\\% \\\\\n\\midrule\nMMLU & 12{,}508 & 31.3 & 16.4 & 14.9 \\\\\nTruthfulQA & 817 & 22.4 & 14.8 & 7.6 \\\\\nWinoGrande & 1{,}267 & 14.7 & 10.1 & 4.6 \\\\\nARC & 1{,}172 & 13.8 & 9.2 & 4.6 \\\\\nGSM8K & 1{,}319 & 12.4 & 8.7 & 3.7 \\\\\nHellaSwag & 10{,}042 & 10.1 & 7.8 & 2.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Benchmark Replication: GSM8K}\n\\label{sec:gsm8k}\n\nGSM8K (1,319 items, $N_{\\text{ref}} = 1{,}017$, $N_{\\text{foc}} = 804$) shows raw temporal C\\% $= 12.4\\%$, with a permutation null of 8.7\\% yielding effective C\\% $= 3.7\\%$---near the noise floor. The lower rate likely reflects GSM8K's single-domain structure: math ability improvement maps more uniformly across items, and MH's total-score conditioning absorbs this effect more effectively.\n\nSemi-synthetic $\\Delta$TPR on GSM8K is also reduced: 0.38 at $p = 0.3$ (standard injection) and 0.27 (external injection), reflecting lower power from the smaller item pool.\n\nWe attempted to correlate DIF flags with the GSM1K contamination gap \\citep{zhang2024careful} as external validation. On $N = 33$ matched models, the correlation is negative (Pearson $r = -0.29$, $p = 0.10$; Spearman $\\rho = -0.22$, $p = 0.21$; partial $r = -0.18$, $p = 0.32$) but non-significant, with confidence intervals crossing zero. At this sample size, we cannot draw conclusions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-benchmark DIF comparison.}\n\\label{tab:cross_bench}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nBenchmark & Raw C\\% & Perm.\\ Null & Eff.\\ C\\% & Interpretation \\\\\n\\midrule\nMMLU & 31.3 & 16.4 & 14.9 & Moderate signal \\\\\nGSM8K & 12.4 & 8.7 & 3.7 & Near noise floor \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{GSM1K correlation analysis ($N = 33$).}\n\\label{tab:gsm1k}\n\\begin{tabular}{@{}lrcc@{}}\n\\toprule\nMetric & Value & 95\\% CI & $p$ \\\\\n\\midrule\nPearson $r$ & $-0.29$ & $[-0.58, 0.06]$ & 0.10 \\\\\nSpearman $\\rho$ & $-0.22$ & $[-0.53, 0.14]$ & 0.21 \\\\\nPartial $r$ & $-0.18$ & $[-0.50, 0.19]$ & 0.32 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Semi-Synthetic Validation}\n\\label{sec:semi_synthetic}\n\nWe inject differential contamination into 150 of 500 selected clean items at four exploitation rates. Table~\\ref{tab:semi_synth} shows $\\Delta$TPR under the worst-case parameterization. At $p = 0.5$, $\\Delta$TPR $= 0.26$---moderate detection power, substantially below the registry's optimistic estimate of 0.508, because the high baseline FPR (0.318) compresses the available signal range.\n\nCross-subject matching remains effective: $\\Delta$FPR $= 0.003$ (Table~\\ref{tab:matching}), confirming that using scores from other subjects as the conditioning variable prevents contamination from corrupting the matching. Within-subject matching, by contrast, inflates FPR by 0.186.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Semi-synthetic $\\Delta$TPR under worst-tier parameterization.}\n\\label{tab:semi_synth}\n\\begin{tabular}{@{}rcccc@{}}\n\\toprule\nInjection $p$ & TPR & Baseline FPR & $\\Delta$TPR & Registry $\\Delta$TPR \\\\\n\\midrule\n0.3 & 0.39 & 0.318 & 0.07 & 0.222 \\\\\n0.5 & 0.58 & 0.318 & 0.26 & 0.508 \\\\\n0.7 & 0.74 & 0.318 & 0.42 & 0.664 \\\\\n1.0 & 0.87 & 0.318 & 0.55 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-subject vs.\\ within-subject matching.}\n\\label{tab:matching}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMatching & $\\Delta$FPR & $\\Delta$TPR ($p{=}0.5$) & Verdict \\\\\n\\midrule\nWithin-subject & +0.186 & 0.34 & FPR inflated \\\\\nCross-subject & +0.003 & 0.26 & FPR stable \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{RL Robustness}\n\\label{sec:rl_robustness}\n\nAdding 13 reasoning-RL models (DeepSeek-R1, Qwen2.5-RL, etc.) to the focal cohort reduces C\\% from 31.3\\% to 24.1\\% and shifts 57\\% of individual item flags (Jaccard $= 0.43$ vs.\\ baseline; Table~\\ref{tab:rl_stability}). Alignment-RL models (DPO/ORPO) are benign (Jaccard $= 0.82$). This demonstrates that DIF flags are cohort-dependent properties, not stable item characteristics. Our characterization is specific to the 2023-vs-2024 temporal split and should not be extrapolated to arbitrary cohort definitions.\n\nTraditional detectors show minimal sensitivity to RL composition: Min-K\\% AUROC drops 0.03 ($p = 0.34$, DeLong test), ConStat drops 0.03 ($p = 0.41$). TOST equivalence is borderline ($p = 0.08$). The power analysis boundary ($\\delta = 1.8$) with $N = 13$ reasoning-RL models is insufficient to support robust conclusions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DIF flag stability under cohort composition changes.}\n\\label{tab:rl_stability}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nComparison & Jaccard & C\\% shift & Interpretation \\\\\n\\midrule\nBaseline vs.\\ +align-RL & 0.82 & $-1.5$pp & Stable \\\\\nBaseline vs.\\ +reason-RL & 0.43 & $-7.2$pp & Unstable \\\\\nAlign-RL vs.\\ reason-RL & 0.48 & $-5.7$pp & RL type dominant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Traditional detector AUROC comparison.}\n\\label{tab:trad_detectors}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nDetector & AUROC (base) & AUROC (RL) & $\\Delta$ & DeLong $p$ \\\\\n\\midrule\nMin-K\\% & 0.71 & 0.68 & $-0.03$ & 0.34 \\\\\nConStat & 0.65 & 0.62 & $-0.03$ & 0.41 \\\\\nMH-DIF & N/A & N/A & Jacc.\\ 0.43 & N/A \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Alternative Detection Methods}\n\\label{sec:alternatives}\n\n\\paragraph{ConStat Perturbation Testing.} We generate reformulations for 237 MMLU items (91\\% semantic equivalence verified) and apply ConStat's FDR-controlled detection. ConStat achieves AUROC $= 0.72$ on non-RL models but degrades to 0.54 on reasoning-RL models (Table~\\ref{tab:constat}). The overlap between ConStat and DIF flags is minimal (Jaccard $= 0.15$): ConStat identifies 47 items missed by DIF, while DIF flags 312 items missed by ConStat.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{ConStat detection performance by model type.}\n\\label{tab:constat}\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nModel type & $N$ & Det.\\ rate & AUROC & FPR \\\\\n\\midrule\nNon-RL & 50 & 0.24 & 0.72 & 0.06 \\\\\nAlignment-RL & 30 & 0.18 & 0.64 & 0.07 \\\\\nReasoning-RL & 13 & 0.09 & 0.54 & 0.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{DVD Generation Variance.} We sample 50 responses per item at temperature 0.8 across 12 models on 500 items. DVD achieves AUROC $= 0.61$ with detection rate 0.18 and identifies 43 bimodal items (Table~\\ref{tab:dvd}). Overlap with DIF is even lower (Jaccard $= 0.11$), and with ConStat marginally higher (Jaccard $= 0.19$). The three-way disagreement---DIF, ConStat, and DVD flag nearly disjoint item sets---suggests each method measures a different construct, raising a field-wide validity concern.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DVD detection summary.}\n\\label{tab:dvd}\n\\begin{tabular}{@{}lr@{}}\n\\toprule\nMetric & Value \\\\\n\\midrule\nAUROC & 0.61 \\\\\nDetection rate & 0.18 \\\\\nFPR & 0.08 \\\\\nBimodal items & 43 \\\\\nOverlap with DIF (Jaccard) & 0.11 \\\\\nOverlap with ConStat (Jaccard) & 0.19 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Ensemble Fusion}\n\\label{sec:ensemble}\n\nWe attempted to fuse DIF, ConStat, and DVD into a multi-signal ensemble. Pairwise signal correlations are extremely low (DIF--ConStat: 0.09, DIF--DVD: 0.06, ConStat--DVD: 0.13), indicating the methods do not measure the same underlying construct. Majority-vote AUROC ($0.58$) is lower than the best individual detector (ConStat: 0.72 on non-RL). Weighted fusion cross-validation shows weight instability across folds (sign flips). Only 4\\% of items are flagged by all three methods. We consider this experiment a negative result: ensemble fusion is not viable when constituent signals are effectively orthogonal.\n\n\\subsection{IRT Model Fit}\n\\label{sec:irt_fit}\n\nWe fit both unidimensional 2PL and bifactor (1 general + 57 specific factors) IRT models to the $12{,}508 \\times 5{,}219$ response matrix (Table~\\ref{tab:irt_fit}). The unidimensional 2PL converges but with poor fit (RMSEA $= 0.094$, CFI $= 0.68$). The bifactor model fails to converge after three attempts with different estimation methods; forced estimates yield RMSEA $= 0.089$, CFI $= 0.72$---still far below acceptable thresholds (RMSEA $< 0.06$, CFI $> 0.95$). With $> 25{,}000$ parameters and the 57-subject factor structure, the bifactor model is severely overparameterized relative to the sample. Anchor item selection for equating is impossible without reliable parameter estimates.\n\nThis confirms that IRT-based interpretation of MH-DIF results is not warranted for MMLU. Our use of MH as a nonparametric test does not require IRT model fit, but the inability to fit any IRT model means the total-score conditioning may not adequately control for ability differences.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{IRT model fit comparison.}\n\\label{tab:irt_fit}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nModel & RMSEA & CFI & TLI & SRMR & Converged \\\\\n\\midrule\nUnidim.\\ 2PL & 0.094 & 0.68 & 0.65 & 0.12 & Yes (poor) \\\\\nBifactor (57) & 0.089 & 0.72 & 0.69 & 0.11 & No (forced) \\\\\nAcceptable & ${<}0.06$ & ${>}0.95$ & ${>}0.95$ & ${<}0.08$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Architecture Stratification}\n\\label{sec:arch}\n\nMETABENCH MMLU is 99.98\\% decoder-only (5,226/5,227 models). Removing the single non-decoder model changes nothing: C\\% $= 31.3\\%$, Jaccard $= 1.0$, IRT fit identical (Table~\\ref{tab:arch}). Architecture heterogeneity is not the source of IRT misfit; the real source is MMLU's 57-subject multidimensionality combined with non-normal ability distributions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Architecture stratification.}\n\\label{tab:arch}\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nPopulation & $N$ & C\\% & RMSEA & CFI \\\\\n\\midrule\nFull & 5{,}227 & 31.3 & 0.094 & 0.68 \\\\\nDecoder-only & 5{,}226 & 31.3 & 0.094 & 0.68 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Regression Transparency}\n\\label{sec:regression}\n\nWe examine what predicts DIF flags via logistic regression (Table~\\ref{tab:regression}). Domain-level accuracy change alone explains almost nothing (McFadden $R^2 = 0.0007$). Adding item properties (difficulty, discrimination) raises $R^2$ to 0.0423---a 60$\\times$ increase, but still modest in absolute terms. A Simpson's paradox emerges: item accuracy change OR flips from 1.08 (bivariate) to 0.92 (controlling for item properties), meaning higher-accuracy-change items are \\textit{less} likely to show DIF after adjusting for difficulty and discrimination. Deviance analysis shows 96\\% of model variance comes from item properties, not accuracy change. DIF flags are more associated with item structural properties (harder, more discriminating items) than with temporal accuracy shifts.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Logistic regression hierarchy.}\n\\label{tab:regression}\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nModel & Predictors & McF.\\ $R^2$ & Key OR \\\\\n\\midrule\nM1 & Domain $\\Delta$acc & 0.0007 & 1.55 [1.19--2.03] \\\\\nM2 & $+$ item props & 0.0423 & 0.73 ($\\Delta$acc flips) \\\\\nM3 & Item $\\Delta$acc & 0.0012 & 1.08 \\\\\nM4 & $+$ item props & 0.0434 & 0.92 ($\\Delta$acc flips) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Graceful Degradation Under Replacement}\n\\label{sec:degradation}\n\nWe simulate progressive item replacement (5\\%--50\\%) to assess whether removing unstable items is a viable remediation strategy (Table~\\ref{tab:degradation}). Ranking stability ($\\rho$) degrades gracefully: 0.981 at 20\\% replacement. However, reliability (Cronbach's $\\alpha$) drops from 0.94 to 0.86 at 20\\%---approaching the educational testing minimum (0.85)---and to 0.74 at 50\\%, which is unacceptable. Construct coverage falls to 0.82 at 31\\% replacement. This demonstrates that item removal is not a viable response to instability at the 31\\% level.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Graceful degradation under item replacement.}\n\\label{tab:degradation}\n\\begin{tabular}{@{}rccc@{}}\n\\toprule\nReplaced & Ranking $\\rho$ & Reliability $\\alpha$ & Coverage \\\\\n\\midrule\n0\\% & 1.000 & 0.94 & 1.00 \\\\\n5\\% & 0.998 & 0.93 & 0.97 \\\\\n10\\% & 0.994 & 0.91 & 0.93 \\\\\n20\\% & 0.981 & 0.86 & 0.88 \\\\\n31\\% & 0.969 & 0.85 & 0.82 \\\\\n50\\% & 0.937 & 0.74 & 0.71 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Item-Focused Trees}\n\\label{sec:ift}\n\nAs a robustness check, we apply Item-Focused Trees (IFT), which treat model release date as a continuous covariate rather than requiring a binary cohort split. IFT flags 22.8\\% of items (vs.\\ MH's 31.3\\%), with moderate overlap (Jaccard $= 0.52$; Table~\\ref{tab:ift}). Split points concentrate around 2023-Q3 to 2024-Q1, broadly validating the temporal split. However, IFT itself is unstable: across random seeds, Jaccard $= 0.63$, indicating that the tree structure is sensitive to initialization. IFT detects 312 nonlinear DIF items (non-monotonic difficulty change over time) that MH cannot identify, though this may reflect noise rather than genuine nonlinear effects.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{IFT vs.\\ MH-DIF comparison.}\n\\label{tab:ift}\n\\begin{tabular}{@{}lrrc@{}}\n\\toprule\nMethod & C\\% & Unique flags & Overlap (Jacc.) \\\\\n\\midrule\nMH-DIF & 31.3 & 1{,}583 & 0.52 \\\\\nIFT & 22.8 & 512 & 0.52 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Difficulty Calibration for Item Generation}\n\\label{sec:item_gen}\n\nWe generated 200 replacement items for DIF-flagged MMLU questions (142 passing quality filters) and evaluated difficulty calibration via two methods (Table~\\ref{tab:calibration}). Both fail to reach the target correlation of 0.75: prompt-based targeting achieves $\\rho = 0.18$, student simulation reaches $\\rho = 0.41$, and the combination yields $\\rho = 0.47$. MMLU's multi-domain knowledge items make difficulty prediction substantially harder than for single-domain math benchmarks where similar methods achieve $r = 0.75$--$0.82$. Equating correlation ($\\rho = 0.88$) falls short of the 0.95 target. Item regeneration is not viable with current methods.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Difficulty calibration methods.}\n\\label{tab:calibration}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & $\\rho$ & Target & Verdict \\\\\n\\midrule\nPrompt-based & 0.18 & 0.75 & Fail \\\\\nStudent sim. & 0.41 & 0.75 & Fail \\\\\nCombined & 0.47 & 0.75 & Fail \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cumulative Bayesian DIF}\n\\label{sec:bayesian}\n\nWe implement cumulative Bayesian DIF priors \\citep{sinharay2006bayesian} and simulate four successive administrations (Table~\\ref{tab:bayesian_dif}). Cumulative power improves from 0.40 (single administration) to 0.61 (four administrations), but remains below the target of 0.70. The method assumes exchangeable examinee populations across administrations, which is violated in LLM benchmarks where successive cohorts are systematically stronger. Prior specification sensitivity is high (power ranges 0.48--0.64 across three prior choices), indicating that results depend on subjective modeling decisions. This remains a simulation-only exploration without real-data validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cumulative DIF power by administration count.}\n\\label{tab:bayesian_dif}\n\\begin{tabular}{@{}rccc@{}}\n\\toprule\n$N_{\\text{admin}}$ & Power & Target & Gap \\\\\n\\midrule\n1 & 0.40 & 0.70 & $-0.30$ \\\\\n2 & 0.49 & 0.70 & $-0.21$ \\\\\n3 & 0.56 & 0.70 & $-0.14$ \\\\\n4 & 0.61 & 0.70 & $-0.09$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{The 31\\% Headline, Decomposed.} Our central finding is not that 31\\% of MMLU items are ``contaminated'' or ``broken,'' but that 31\\% exhibit behavioral heterogeneity between temporal cohorts. Approximately half (16.4\\%) is attributable to cohort composition differences that MH's total-score conditioning cannot absorb. The remaining $\\sim$15\\% represents genuine item-level behavioral change---substantial, but more modest than the raw headline suggests. Across benchmarks, effective rates range from 2.3\\% to 14.9\\%, making MMLU an outlier rather than representative.\n\n\\paragraph{Method Disagreement as Field-Wide Challenge.} The near-orthogonality of DIF, ConStat, and DVD flags (pairwise Jaccard $0.06$--$0.19$) is perhaps our most provocative finding. If three independent methods claiming to detect item-level anomalies flag almost entirely different items, the field faces a construct validity crisis: either these methods measure genuinely different phenomena, or at least some are measuring artifacts. The ensemble failure (majority-vote AUROC $= 0.58$) confirms that simple aggregation cannot resolve this disagreement.\n\n\\paragraph{Cohort Dependence.} The RL robustness experiment (Jaccard $= 0.43$ when adding 13 reasoning-RL models) demonstrates that DIF flags are properties of the cohort definition, not stable item attributes. Our characterization is specific to the 2023-vs-2024 temporal split. Benchmark maintainers should not treat DIF results as fixed item labels but as cohort-specific diagnostics.\n\n\\paragraph{Monitoring Over Remediation.} Graceful degradation analysis shows that removing 31\\% of items would reduce reliability from 0.94 to $\\sim$0.85 and construct coverage to 0.82. Item generation cannot yet produce calibrated replacements ($\\rho = 0.47$ vs.\\ target 0.75). Together, these findings argue for monitoring stability over time rather than acting on individual flags.\n\n%==============================================================================\n\\section{Limitations}\n\\label{sec:limitations}\n%==============================================================================\n\nFirst, MH's total-score conditioning is a limited ability proxy. With 98\\% IRT misfit and failed bifactor convergence, the conditioning may not adequately control for multidimensional ability differences between cohorts. Multidimensional IRT or propensity-score methods may yield different results.\n\nSecond, our characterization is cohort-specific. The 14.9\\% effective rate depends on the 2023-vs-2024 split; different temporal boundaries, different benchmarks, or the inclusion of reasoning-RL models produce substantially different results (effective C\\% ranges from 2.3\\% to 14.9\\% across benchmarks; Jaccard $= 0.43$ with RL models).\n\nThird, the semi-synthetic framework uses a simplified contamination mechanism (incorrect$\\to$correct flipping). Real contamination may involve subtler changes in response distributions that our injection does not capture. Detection power under worst-case parameterization is moderate ($\\Delta$TPR $= 0.26$ at $p = 0.5$).\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe present the first large-scale item-level stability analysis of LLM benchmarks, applying nonparametric MH analysis to 5,227 models across 12,508 MMLU items and five additional benchmarks. The observed 31\\% raw behavioral heterogeneity decomposes into approximately 15\\% genuine temporal signal and 16\\% cohort composition artifact. This signal is benchmark-specific (2--15\\% effective rate across benchmarks), method-dependent (three detectors produce near-disjoint flags), and cohort-sensitive (reasoning-RL models destabilize flags). We contribute a semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR $\\approx 0$) as reusable infrastructure. Our findings motivate treating item-level stability as an ongoing monitoring metric rather than a one-time diagnostic.\n\n%==============================================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nJasper Dekoninck, Mark Niklas M{\\\"u}ller, and Martin Vechev.\n\\newblock Con{S}tat: Statistical testing for {LLM} contamination detection.\n\\newblock In \\textit{Proceedings of NeurIPS}, 2024.\n\n\\bibitem[Holland and Thayer(1988)]{holland1988differential}\nPaul~W. Holland and Dorothy~T. Thayer.\n\\newblock Differential item performance and the {M}antel-{H}aenszel procedure.\n\\newblock In \\textit{Test Validity}, pages 129--145. Lawrence Erlbaum, 1988.\n\n\\bibitem[Li et~al.(2024)]{li2024task}\nYucheng Li, Frank Guerin, and Chenghua Lin.\n\\newblock Task contamination: Language models may not be few-shot anymore.\n\\newblock In \\textit{Proceedings of AAAI}, 2024.\n\n\\bibitem[Mantel and Haenszel(1959)]{mantel1959statistical}\nNathan Mantel and William Haenszel.\n\\newblock Statistical aspects of the analysis of data from retrospective studies of disease.\n\\newblock \\textit{Journal of the National Cancer Institute}, 22(4):719--748, 1959.\n\n\\bibitem[Oren et~al.(2024)]{oren2024proving}\nYonatan Oren, Nicole Meister, Niladri Chatterji, Faisal Ladhak, and Tatsunori~B. Hashimoto.\n\\newblock Proving test set contamination in black box language models.\n\\newblock In \\textit{Proceedings of ICLR}, 2024.\n\n\\bibitem[Perlitz et~al.(2024)]{perlitz2024metabench}\nYotam Perlitz, Elron Bandel, Ariel Gera, Ofir Arviv, Liat Ein-Dor, Eyal Shnarch, Noam Slonim, Michal Shmueli-Scheuer, and Leshem Choshen.\n\\newblock Efficient benchmarking (of language models).\n\\newblock \\textit{arXiv preprint arXiv:2308.11696}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nFelipe~Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin.\n\\newblock tiny{B}enchmarks: evaluating {LLM}s with fewer examples.\n\\newblock In \\textit{Proceedings of ICML}, 2024.\n\n\\bibitem[Raju et~al.(2024)]{raju2024growing}\nAnirudh Raju, Harish Kamath, and Heather Lent.\n\\newblock Growing pains: Understanding the limitations of {LLM} evaluation benchmarks.\n\\newblock \\textit{arXiv preprint arXiv:2410.08455}, 2024.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nWeijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\textit{Proceedings of ICLR}, 2024.\n\n\\bibitem[Sinharay et~al.(2006)]{sinharay2006bayesian}\nSandip Sinharay, Matthew~S. Johnson, and H.~Swaminathan.\n\\newblock Bayesian estimation of differential item functioning.\n\\newblock \\textit{Psychometrika}, 71(1):145--168, 2006.\n\n\\bibitem[Tutz and Berger(2016)]{tutz2016item}\nGerhard Tutz and Moritz Berger.\n\\newblock Item-focused trees for the identification of items in differential item functioning.\n\\newblock \\textit{Psychometrika}, 81(3):727--750, 2016.\n\n\\bibitem[Zhang et~al.(2024)]{zhang2024careful}\nHugh Zhang, Jeff Da, Dean Lee, Vaughn Robinson, Catherine Wu, Will Song, Tiffany Zhao, Pranav Raja, Dylan Slack, Qin Lv, Sean Hendryx, Summer Yue, and others.\n\\newblock A careful examination of large language model performance on grade school math.\n\\newblock \\textit{arXiv preprint arXiv:2405.00332}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f00525a-f82c-455f-8e8e-bfcce5743806",
  "isSidechain": false,
  "requestId": "req_011CbG7L4KD4DuhGGqFFJARU",
  "type": "assistant",
  "uuid": "f842f265-41d2-415c-91c9-bddac96e75fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136tdaxG37zuP9jsqfksb9f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2298,
      "cache_read_input_tokens": 49072,
      "output_tokens": 12293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12293,
          "cache_read_input_tokens": 49072,
          "cache_creation_input_tokens": 2298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2298
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

_source line 20 · 2026-05-21T17:33:22.913Z_

<details><summary>↩ Tool result · `toolu_017wceqdjiTpJzivqhkQpUjX`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f842f265-41d2-415c-91c9-bddac96e75fb",
  "isSidechain": false,
  "promptId": "9377956b-ace9-4b16-82d2-21e10f437ea9",
  "type": "user",
  "uuid": "c16d10f6-d22f-4f4f-b4d6-d1211c88cd3a",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{geometry}\n\\geometry{margin=1in}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{array}\n\\usepackage{caption}\n\\captionsetup{font=small}\n\n\\title{Large-Scale Item-Level Stability Analysis of LLM Benchmarks}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nLLM benchmarks implicitly assume that item difficulty is stable across model generations, yet this assumption has never been tested at scale. We apply the Mantel-Haenszel (MH) statistic---a nonparametric group-comparison test---to the METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items) and find that 31.3\\% of items exhibit large behavioral heterogeneity between 2023 and 2024-H1 model cohorts (ETS C class, $|\\Delta_{\\text{MH}}| \\geq 1.5$). However, a 1,000-iteration permutation null reveals that approximately 16.4\\% of this rate is attributable to cohort composition differences rather than genuine temporal change, yielding an effective rate of 14.9\\%. Replication across five additional benchmarks shows effective rates ranging from 2.3\\% (HellaSwag) to 7.6\\% (TruthfulQA), with MMLU as an outlier. We introduce a semi-synthetic validation framework with cross-subject matching that eliminates false-positive inflation ($\\Delta$FPR $= 0.003$), providing reusable infrastructure for validating any item-level detector. We further show that reasoning-RL models destabilize DIF flags (Jaccard $= 0.43$), that three independent detection methods (MH-DIF, ConStat, DVD) flag nearly disjoint item sets (pairwise Jaccard $0.11$--$0.19$), and that both unidimensional and bifactor IRT models are severely misspecified for MMLU (CFI $< 0.72$, RMSEA $> 0.08$). These findings collectively characterize item-level stability as a benchmark-specific, method-dependent, and cohort-sensitive property, motivating monitoring-over-remediation approaches to benchmark maintenance.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nWhen we report that a 2024 model scores 78\\% on MMLU while a 2023 model scores 65\\%, we implicitly assume both scores reflect the same measurement construct---that item difficulty is stable across model generations. Psychometrics calls violations of this assumption \\textit{differential item functioning} (DIF): an item exhibits DIF when examinees of equal ability from different groups have different probabilities of answering correctly.\n\nWe apply the Mantel-Haenszel (MH) statistic \\citep{mantel1959statistical,holland1988differential} to characterize item-level behavioral stability in the METABENCH repository \\citep{perlitz2024metabench}---5,227 models evaluated on 12,508 MMLU items. We treat MH strictly as a nonparametric $\\chi^2$ test for group$\\times$item interaction, without claiming latent-trait interpretation, since unidimensional IRT is fundamentally misspecified for MMLU's 57-subject structure (98\\% of models show $|L_z| > 2$; bifactor IRT also fails to converge with acceptable fit).\n\nOur central finding: 31.3\\% of MMLU items show large behavioral heterogeneity between temporal cohorts. A permutation null decomposes this into $\\sim$16.4\\% attributable to cohort composition differences and $\\sim$14.9\\% that persists after controls. We characterize this heterogeneity without claiming psychometric interpretation---it is an empirical property of how item response patterns differ across model generations.\n\nThree further findings shape the interpretation: (1)~reasoning-RL models fundamentally destabilize DIF flags (Jaccard~$= 0.43$), showing that flags are cohort-dependent; (2)~three independent detection methods flag nearly disjoint item sets (pairwise Jaccard $0.11$--$0.19$), suggesting a construct validity challenge across the field; (3)~a semi-synthetic validation framework with cross-subject matching provides principled infrastructure for evaluating any item-level detector, with known power limitations.\n\nWe frame item-level stability as an operational metric for benchmark maintenance: characterize, monitor, but do not remediate---removing 31\\% of items degrades reliability below acceptable thresholds.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{LLM Benchmark Contamination.} \\citet{li2024task} and \\citet{oren2024proving} document web-overlap as a proxy for benchmark contamination. Min-K\\% \\citep{shi2024detecting} and ConStat \\citep{dekoninck2024constat} detect contamination via model-internal signals. DVD \\citep{oren2024proving} uses generation variance. All validate against web-overlap labels, which measure global exposure rather than item-level differential effects.\n\n\\paragraph{Differential Item Functioning.} MH-DIF \\citep{holland1988differential} is the standard nonparametric method in educational testing. \\citet{sinharay2006bayesian} extend it to cumulative Bayesian frameworks. Item-Focused Trees \\citep{tutz2016item} treat covariates continuously. DIF has not previously been applied to LLM benchmark evaluation at scale.\n\n\\paragraph{Benchmark Stability.} \\citet{raju2024growing} identify ``growing pains'' in LLM evaluation via anchor-item methods. Our DIF analysis complements their work by identifying \\emph{which} items are degrading. \\citet{polo2024tinybenchmarks} show benchmark redundancy enables subsampling---consistent with our finding that ranking stability is maintained despite 31\\% item instability.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{MH-DIF as Nonparametric Group-Comparison Test}\n\nGiven a binary response matrix $\\mathbf{X} \\in \\{0,1\\}^{N \\times I}$ and a grouping variable $G \\in \\{\\text{ref}, \\text{foc}\\}$, the MH statistic tests whether the odds of a correct response differ between groups after stratifying by total score. The common odds ratio $\\alpha_{\\text{MH}}$ is converted to the ETS delta scale:\n\\begin{equation}\n\\Delta_{\\text{MH}} = -2.35 \\ln(\\alpha_{\\text{MH}})\n\\end{equation}\nItems are classified as A ($|\\Delta_{\\text{MH}}| < 1.0$), B ($1.0 \\leq |\\Delta_{\\text{MH}}| < 1.5$), or C ($|\\Delta_{\\text{MH}}| \\geq 1.5$) per ETS guidelines. We report C-class percentage (C\\%) as the primary instability metric.\n\nWe use MH strictly as a nonparametric test. Total-score stratification controls for overall ability without requiring a latent-trait model. This is critical: MMLU's 57-subject structure makes unidimensional IRT misspecified (Section~\\ref{sec:irt_fit}), and we do not claim that MH conditioning fully absorbs all confounds.\n\n\\subsection{Semi-Synthetic Validation Framework}\n\nTo validate detection power under controlled ground truth, we inject known differential contamination into real METABENCH response matrices. For selected ``clean'' items in the focal cohort, we flip incorrect$\\to$correct responses with probability $p \\in \\{0.3, 0.5, 0.7, 1.0\\}$ for a random subset of focal models, simulating contamination that differentially benefits newer models.\n\nThe key innovation is \\textbf{cross-subject matching}: when testing items from subject $s$, we use total score on all \\emph{other} subjects as the MH matching variable. This prevents the injected contamination from corrupting the conditioning variable. Detection power is measured as $\\Delta$TPR $=$ TPR$_{\\text{injected}}$ $-$ TPR$_{\\text{baseline}}$, and false-positive control as $\\Delta$FPR.\n\n\\subsection{Permutation Null}\n\nWe establish a null distribution for C\\% via 1,000 permutations: temporal labels (2023 vs.\\ 2024) are randomly reassigned while preserving group sizes, and MH-DIF is recomputed each time. The null mean C\\% quantifies how much behavioral heterogeneity arises from cohort composition alone (ability distribution, family structure, training vintage) rather than temporal signal.\n\n%==============================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n%==============================================================================\n\n\\subsection{Temporal DIF on MMLU}\n\\label{sec:temporal_dif}\n\nWe partition the 5,227 METABENCH MMLU models into reference (2023, $N = 1{,}080$) and focal (2024-H1, $N = 807$) cohorts. MH-DIF identifies 31.3\\% of 12,508 items as C-class. A random-split sanity check yields C\\% $= 0.18\\%$, confirming the signal is not a statistical artifact.\n\nWithin-family analysis shows elevated C\\%: Llama-2$\\to$3 at 61.3\\% and Mistral$\\to$Mixtral at 38.7\\%. However, these comparisons confound temporal change with architecture, data, and training procedure changes. Domain-level accuracy improvement correlates weakly with DIF rates ($\\rho = 0.307$, $p = 0.02$), but this ecological correlation on $N = 57$ subjects has limited item-level interpretability. Removing 15.4\\% negative-discrimination items reduces C\\% by only 1.2pp.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temporal DIF summary on MMLU.}\n\\label{tab:temporal_dif}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMetric & Raw & After Perm.\\ Control & Interpretation \\\\\n\\midrule\nC\\% & 31.3\\% & 14.9\\% & Inflated by cohort comp. \\\\\nEnrichment vs.\\ Li & 0.96 & 0.96 & Trivially expected \\\\\nIRT misfit & 98\\% $|L_z|{>}2$ & N/A & MH conditioning unreliable \\\\\nDomain $\\rho$ & 0.307 & N/A & Ecol.\\ fallacy on $N{=}57$ \\\\\nWithin-family C\\% & 38.7--61.3\\% & N/A & Architecture confounded \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cohort definition $\\times$ item filtering sensitivity.}\n\\label{tab:cohort_filtering}\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nCohort & Filter & C\\% & Effective C\\% \\\\\n\\midrule\nTemporal & All items & 31.3 & 14.9 \\\\\nTemporal & No neg-disc & 30.1 & 13.7 \\\\\nAbility & All items & 2.9 & N/A \\\\\nAbility & No neg-disc & 2.7 & N/A \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Permutation Null Decomposition}\n\\label{sec:permutation}\n\nThe 1,000-iteration permutation null yields mean C\\% $= 16.4\\%$ (SD $= 2.1\\%$, 95\\% CI $[12.6, 20.3]$). The observed 31.3\\% exceeds this null ($z = 7.1$, $p < 10^{-12}$), so temporal signal exists beyond cohort composition. However, 52.4\\% of the raw C\\% is attributable to cohort composition effects---ability distribution shift ($d = -0.17$), model family structure differences, and training data vintage variation---that MH's total-score conditioning cannot fully absorb.\n\nThe random-split control (C\\% $= 0.18\\%$) is not contradictory: random splits preserve within-cohort structure, while permutation preserves between-cohort composition differences. The 16.4\\% null arises specifically because 2023 and 2024 models differ in ways beyond temporal signal.\n\nEffective C\\% after permutation control is 14.9\\%: this represents item-level behavioral change that cannot be attributed to cohort composition alone. Even this figure may include residual confounds (tokenizer changes, training data composition within families) not captured by the permutation procedure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Permutation null distribution ($B = 1{,}000$).}\n\\label{tab:perm_null}\n\\begin{tabular}{@{}lr@{}}\n\\toprule\nStatistic & Value \\\\\n\\midrule\nNull mean C\\% & 16.4 \\\\\nNull SD & 2.1 \\\\\nNull 95\\% CI & $[12.6, 20.3]$ \\\\\nObserved C\\% & 31.3 \\\\\n$z$-score & 7.1 \\\\\nEffective C\\% & 14.9 \\\\\nFraction spurious & 52.4\\% \\\\\nRandom-split C\\% & 0.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Decomposition of observed C\\%.}\n\\label{tab:decomposition}\n\\begin{tabular}{@{}lrl@{}}\n\\toprule\nSource & C\\% & Mechanism \\\\\n\\midrule\nGenuine temporal & 14.9 & Item-level behavioral change \\\\\nCohort composition & 16.4 & Ability + family + vintage \\\\\n\\midrule\nTotal & 31.3 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Benchmark Stability Profiles}\n\\label{sec:multi_bench}\n\nWe replicate temporal DIF on five additional METABENCH benchmarks (Table~\\ref{tab:multi_bench}). Raw C\\% ranges from 10.1\\% (HellaSwag) to 31.3\\% (MMLU). After permutation controls, effective C\\% ranges from 2.3\\% to 14.9\\%. All random-split controls remain below 1\\%, confirming genuine between-cohort signal across benchmarks. MMLU's outlier status (14.9\\% effective) likely reflects its 57-subject structure providing more opportunities for heterogeneity. HellaSwag's low effective rate (2.3\\%) is consistent with its relatively homogeneous task structure (sentence completion).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-benchmark DIF summary.}\n\\label{tab:multi_bench}\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nBenchmark & $N_{\\text{items}}$ & Raw C\\% & Perm.\\ Null & Eff.\\ C\\% \\\\\n\\midrule\nMMLU & 12{,}508 & 31.3 & 16.4 & 14.9 \\\\\nTruthfulQA & 817 & 22.4 & 14.8 & 7.6 \\\\\nWinoGrande & 1{,}267 & 14.7 & 10.1 & 4.6 \\\\\nARC & 1{,}172 & 13.8 & 9.2 & 4.6 \\\\\nGSM8K & 1{,}319 & 12.4 & 8.7 & 3.7 \\\\\nHellaSwag & 10{,}042 & 10.1 & 7.8 & 2.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Benchmark Replication: GSM8K}\n\\label{sec:gsm8k}\n\nGSM8K (1,319 items, $N_{\\text{ref}} = 1{,}017$, $N_{\\text{foc}} = 804$) shows raw temporal C\\% $= 12.4\\%$, with a permutation null of 8.7\\% yielding effective C\\% $= 3.7\\%$---near the noise floor. The lower rate likely reflects GSM8K's single-domain structure: math ability improvement maps more uniformly across items, and MH's total-score conditioning absorbs this effect more effectively.\n\nSemi-synthetic $\\Delta$TPR on GSM8K is also reduced: 0.38 at $p = 0.3$ (standard injection) and 0.27 (external injection), reflecting lower power from the smaller item pool.\n\nWe attempted to correlate DIF flags with the GSM1K contamination gap \\citep{zhang2024careful} as external validation. On $N = 33$ matched models, the correlation is negative (Pearson $r = -0.29$, $p = 0.10$; Spearman $\\rho = -0.22$, $p = 0.21$; partial $r = -0.18$, $p = 0.32$) but non-significant, with confidence intervals crossing zero. At this sample size, we cannot draw conclusions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-benchmark DIF comparison.}\n\\label{tab:cross_bench}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nBenchmark & Raw C\\% & Perm.\\ Null & Eff.\\ C\\% & Interpretation \\\\\n\\midrule\nMMLU & 31.3 & 16.4 & 14.9 & Moderate signal \\\\\nGSM8K & 12.4 & 8.7 & 3.7 & Near noise floor \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{GSM1K correlation analysis ($N = 33$).}\n\\label{tab:gsm1k}\n\\begin{tabular}{@{}lrcc@{}}\n\\toprule\nMetric & Value & 95\\% CI & $p$ \\\\\n\\midrule\nPearson $r$ & $-0.29$ & $[-0.58, 0.06]$ & 0.10 \\\\\nSpearman $\\rho$ & $-0.22$ & $[-0.53, 0.14]$ & 0.21 \\\\\nPartial $r$ & $-0.18$ & $[-0.50, 0.19]$ & 0.32 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Semi-Synthetic Validation}\n\\label{sec:semi_synthetic}\n\nWe inject differential contamination into 150 of 500 selected clean items at four exploitation rates. Table~\\ref{tab:semi_synth} shows $\\Delta$TPR under the worst-case parameterization. At $p = 0.5$, $\\Delta$TPR $= 0.26$---moderate detection power, substantially below the registry's optimistic estimate of 0.508, because the high baseline FPR (0.318) compresses the available signal range.\n\nCross-subject matching remains effective: $\\Delta$FPR $= 0.003$ (Table~\\ref{tab:matching}), confirming that using scores from other subjects as the conditioning variable prevents contamination from corrupting the matching. Within-subject matching, by contrast, inflates FPR by 0.186.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Semi-synthetic $\\Delta$TPR under worst-tier parameterization.}\n\\label{tab:semi_synth}\n\\begin{tabular}{@{}rcccc@{}}\n\\toprule\nInjection $p$ & TPR & Baseline FPR & $\\Delta$TPR & Registry $\\Delta$TPR \\\\\n\\midrule\n0.3 & 0.39 & 0.318 & 0.07 & 0.222 \\\\\n0.5 & 0.58 & 0.318 & 0.26 & 0.508 \\\\\n0.7 & 0.74 & 0.318 & 0.42 & 0.664 \\\\\n1.0 & 0.87 & 0.318 & 0.55 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-subject vs.\\ within-subject matching.}\n\\label{tab:matching}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMatching & $\\Delta$FPR & $\\Delta$TPR ($p{=}0.5$) & Verdict \\\\\n\\midrule\nWithin-subject & +0.186 & 0.34 & FPR inflated \\\\\nCross-subject & +0.003 & 0.26 & FPR stable \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{RL Robustness}\n\\label{sec:rl_robustness}\n\nAdding 13 reasoning-RL models (DeepSeek-R1, Qwen2.5-RL, etc.) to the focal cohort reduces C\\% from 31.3\\% to 24.1\\% and shifts 57\\% of individual item flags (Jaccard $= 0.43$ vs.\\ baseline; Table~\\ref{tab:rl_stability}). Alignment-RL models (DPO/ORPO) are benign (Jaccard $= 0.82$). This demonstrates that DIF flags are cohort-dependent properties, not stable item characteristics. Our characterization is specific to the 2023-vs-2024 temporal split and should not be extrapolated to arbitrary cohort definitions.\n\nTraditional detectors show minimal sensitivity to RL composition: Min-K\\% AUROC drops 0.03 ($p = 0.34$, DeLong test), ConStat drops 0.03 ($p = 0.41$). TOST equivalence is borderline ($p = 0.08$). The power analysis boundary ($\\delta = 1.8$) with $N = 13$ reasoning-RL models is insufficient to support robust conclusions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DIF flag stability under cohort composition changes.}\n\\label{tab:rl_stability}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nComparison & Jaccard & C\\% shift & Interpretation \\\\\n\\midrule\nBaseline vs.\\ +align-RL & 0.82 & $-1.5$pp & Stable \\\\\nBaseline vs.\\ +reason-RL & 0.43 & $-7.2$pp & Unstable \\\\\nAlign-RL vs.\\ reason-RL & 0.48 & $-5.7$pp & RL type dominant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Traditional detector AUROC comparison.}\n\\label{tab:trad_detectors}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nDetector & AUROC (base) & AUROC (RL) & $\\Delta$ & DeLong $p$ \\\\\n\\midrule\nMin-K\\% & 0.71 & 0.68 & $-0.03$ & 0.34 \\\\\nConStat & 0.65 & 0.62 & $-0.03$ & 0.41 \\\\\nMH-DIF & N/A & N/A & Jacc.\\ 0.43 & N/A \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Alternative Detection Methods}\n\\label{sec:alternatives}\n\n\\paragraph{ConStat Perturbation Testing.} We generate reformulations for 237 MMLU items (91\\% semantic equivalence verified) and apply ConStat's FDR-controlled detection. ConStat achieves AUROC $= 0.72$ on non-RL models but degrades to 0.54 on reasoning-RL models (Table~\\ref{tab:constat}). The overlap between ConStat and DIF flags is minimal (Jaccard $= 0.15$): ConStat identifies 47 items missed by DIF, while DIF flags 312 items missed by ConStat.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{ConStat detection performance by model type.}\n\\label{tab:constat}\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nModel type & $N$ & Det.\\ rate & AUROC & FPR \\\\\n\\midrule\nNon-RL & 50 & 0.24 & 0.72 & 0.06 \\\\\nAlignment-RL & 30 & 0.18 & 0.64 & 0.07 \\\\\nReasoning-RL & 13 & 0.09 & 0.54 & 0.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{DVD Generation Variance.} We sample 50 responses per item at temperature 0.8 across 12 models on 500 items. DVD achieves AUROC $= 0.61$ with detection rate 0.18 and identifies 43 bimodal items (Table~\\ref{tab:dvd}). Overlap with DIF is even lower (Jaccard $= 0.11$), and with ConStat marginally higher (Jaccard $= 0.19$). The three-way disagreement---DIF, ConStat, and DVD flag nearly disjoint item sets---suggests each method measures a different construct, raising a field-wide validity concern.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DVD detection summary.}\n\\label{tab:dvd}\n\\begin{tabular}{@{}lr@{}}\n\\toprule\nMetric & Value \\\\\n\\midrule\nAUROC & 0.61 \\\\\nDetection rate & 0.18 \\\\\nFPR & 0.08 \\\\\nBimodal items & 43 \\\\\nOverlap with DIF (Jaccard) & 0.11 \\\\\nOverlap with ConStat (Jaccard) & 0.19 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Ensemble Fusion}\n\\label{sec:ensemble}\n\nWe attempted to fuse DIF, ConStat, and DVD into a multi-signal ensemble. Pairwise signal correlations are extremely low (DIF--ConStat: 0.09, DIF--DVD: 0.06, ConStat--DVD: 0.13), indicating the methods do not measure the same underlying construct. Majority-vote AUROC ($0.58$) is lower than the best individual detector (ConStat: 0.72 on non-RL). Weighted fusion cross-validation shows weight instability across folds (sign flips). Only 4\\% of items are flagged by all three methods. We consider this experiment a negative result: ensemble fusion is not viable when constituent signals are effectively orthogonal.\n\n\\subsection{IRT Model Fit}\n\\label{sec:irt_fit}\n\nWe fit both unidimensional 2PL and bifactor (1 general + 57 specific factors) IRT models to the $12{,}508 \\times 5{,}219$ response matrix (Table~\\ref{tab:irt_fit}). The unidimensional 2PL converges but with poor fit (RMSEA $= 0.094$, CFI $= 0.68$). The bifactor model fails to converge after three attempts with different estimation methods; forced estimates yield RMSEA $= 0.089$, CFI $= 0.72$---still far below acceptable thresholds (RMSEA $< 0.06$, CFI $> 0.95$). With $> 25{,}000$ parameters and the 57-subject factor structure, the bifactor model is severely overparameterized relative to the sample. Anchor item selection for equating is impossible without reliable parameter estimates.\n\nThis confirms that IRT-based interpretation of MH-DIF results is not warranted for MMLU. Our use of MH as a nonparametric test does not require IRT model fit, but the inability to fit any IRT model means the total-score conditioning may not adequately control for ability differences.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{IRT model fit comparison.}\n\\label{tab:irt_fit}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nModel & RMSEA & CFI & TLI & SRMR & Converged \\\\\n\\midrule\nUnidim.\\ 2PL & 0.094 & 0.68 & 0.65 & 0.12 & Yes (poor) \\\\\nBifactor (57) & 0.089 & 0.72 & 0.69 & 0.11 & No (forced) \\\\\nAcceptable & ${<}0.06$ & ${>}0.95$ & ${>}0.95$ & ${<}0.08$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Architecture Stratification}\n\\label{sec:arch}\n\nMETABENCH MMLU is 99.98\\% decoder-only (5,226/5,227 models). Removing the single non-decoder model changes nothing: C\\% $= 31.3\\%$, Jaccard $= 1.0$, IRT fit identical (Table~\\ref{tab:arch}). Architecture heterogeneity is not the source of IRT misfit; the real source is MMLU's 57-subject multidimensionality combined with non-normal ability distributions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Architecture stratification.}\n\\label{tab:arch}\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nPopulation & $N$ & C\\% & RMSEA & CFI \\\\\n\\midrule\nFull & 5{,}227 & 31.3 & 0.094 & 0.68 \\\\\nDecoder-only & 5{,}226 & 31.3 & 0.094 & 0.68 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Regression Transparency}\n\\label{sec:regression}\n\nWe examine what predicts DIF flags via logistic regression (Table~\\ref{tab:regression}). Domain-level accuracy change alone explains almost nothing (McFadden $R^2 = 0.0007$). Adding item properties (difficulty, discrimination) raises $R^2$ to 0.0423---a 60$\\times$ increase, but still modest in absolute terms. A Simpson's paradox emerges: item accuracy change OR flips from 1.08 (bivariate) to 0.92 (controlling for item properties), meaning higher-accuracy-change items are \\textit{less} likely to show DIF after adjusting for difficulty and discrimination. Deviance analysis shows 96\\% of model variance comes from item properties, not accuracy change. DIF flags are more associated with item structural properties (harder, more discriminating items) than with temporal accuracy shifts.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Logistic regression hierarchy.}\n\\label{tab:regression}\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nModel & Predictors & McF.\\ $R^2$ & Key OR \\\\\n\\midrule\nM1 & Domain $\\Delta$acc & 0.0007 & 1.55 [1.19--2.03] \\\\\nM2 & $+$ item props & 0.0423 & 0.73 ($\\Delta$acc flips) \\\\\nM3 & Item $\\Delta$acc & 0.0012 & 1.08 \\\\\nM4 & $+$ item props & 0.0434 & 0.92 ($\\Delta$acc flips) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Graceful Degradation Under Replacement}\n\\label{sec:degradation}\n\nWe simulate progressive item replacement (5\\%--50\\%) to assess whether removing unstable items is a viable remediation strategy (Table~\\ref{tab:degradation}). Ranking stability ($\\rho$) degrades gracefully: 0.981 at 20\\% replacement. However, reliability (Cronbach's $\\alpha$) drops from 0.94 to 0.86 at 20\\%---approaching the educational testing minimum (0.85)---and to 0.74 at 50\\%, which is unacceptable. Construct coverage falls to 0.82 at 31\\% replacement. This demonstrates that item removal is not a viable response to instability at the 31\\% level.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Graceful degradation under item replacement.}\n\\label{tab:degradation}\n\\begin{tabular}{@{}rccc@{}}\n\\toprule\nReplaced & Ranking $\\rho$ & Reliability $\\alpha$ & Coverage \\\\\n\\midrule\n0\\% & 1.000 & 0.94 & 1.00 \\\\\n5\\% & 0.998 & 0.93 & 0.97 \\\\\n10\\% & 0.994 & 0.91 & 0.93 \\\\\n20\\% & 0.981 & 0.86 & 0.88 \\\\\n31\\% & 0.969 & 0.85 & 0.82 \\\\\n50\\% & 0.937 & 0.74 & 0.71 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Item-Focused Trees}\n\\label{sec:ift}\n\nAs a robustness check, we apply Item-Focused Trees (IFT), which treat model release date as a continuous covariate rather than requiring a binary cohort split. IFT flags 22.8\\% of items (vs.\\ MH's 31.3\\%), with moderate overlap (Jaccard $= 0.52$; Table~\\ref{tab:ift}). Split points concentrate around 2023-Q3 to 2024-Q1, broadly validating the temporal split. However, IFT itself is unstable: across random seeds, Jaccard $= 0.63$, indicating that the tree structure is sensitive to initialization. IFT detects 312 nonlinear DIF items (non-monotonic difficulty change over time) that MH cannot identify, though this may reflect noise rather than genuine nonlinear effects.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{IFT vs.\\ MH-DIF comparison.}\n\\label{tab:ift}\n\\begin{tabular}{@{}lrrc@{}}\n\\toprule\nMethod & C\\% & Unique flags & Overlap (Jacc.) \\\\\n\\midrule\nMH-DIF & 31.3 & 1{,}583 & 0.52 \\\\\nIFT & 22.8 & 512 & 0.52 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Difficulty Calibration for Item Generation}\n\\label{sec:item_gen}\n\nWe generated 200 replacement items for DIF-flagged MMLU questions (142 passing quality filters) and evaluated difficulty calibration via two methods (Table~\\ref{tab:calibration}). Both fail to reach the target correlation of 0.75: prompt-based targeting achieves $\\rho = 0.18$, student simulation reaches $\\rho = 0.41$, and the combination yields $\\rho = 0.47$. MMLU's multi-domain knowledge items make difficulty prediction substantially harder than for single-domain math benchmarks where similar methods achieve $r = 0.75$--$0.82$. Equating correlation ($\\rho = 0.88$) falls short of the 0.95 target. Item regeneration is not viable with current methods.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Difficulty calibration methods.}\n\\label{tab:calibration}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & $\\rho$ & Target & Verdict \\\\\n\\midrule\nPrompt-based & 0.18 & 0.75 & Fail \\\\\nStudent sim. & 0.41 & 0.75 & Fail \\\\\nCombined & 0.47 & 0.75 & Fail \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cumulative Bayesian DIF}\n\\label{sec:bayesian}\n\nWe implement cumulative Bayesian DIF priors \\citep{sinharay2006bayesian} and simulate four successive administrations (Table~\\ref{tab:bayesian_dif}). Cumulative power improves from 0.40 (single administration) to 0.61 (four administrations), but remains below the target of 0.70. The method assumes exchangeable examinee populations across administrations, which is violated in LLM benchmarks where successive cohorts are systematically stronger. Prior specification sensitivity is high (power ranges 0.48--0.64 across three prior choices), indicating that results depend on subjective modeling decisions. This remains a simulation-only exploration without real-data validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cumulative DIF power by administration count.}\n\\label{tab:bayesian_dif}\n\\begin{tabular}{@{}rccc@{}}\n\\toprule\n$N_{\\text{admin}}$ & Power & Target & Gap \\\\\n\\midrule\n1 & 0.40 & 0.70 & $-0.30$ \\\\\n2 & 0.49 & 0.70 & $-0.21$ \\\\\n3 & 0.56 & 0.70 & $-0.14$ \\\\\n4 & 0.61 & 0.70 & $-0.09$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{The 31\\% Headline, Decomposed.} Our central finding is not that 31\\% of MMLU items are ``contaminated'' or ``broken,'' but that 31\\% exhibit behavioral heterogeneity between temporal cohorts. Approximately half (16.4\\%) is attributable to cohort composition differences that MH's total-score conditioning cannot absorb. The remaining $\\sim$15\\% represents genuine item-level behavioral change---substantial, but more modest than the raw headline suggests. Across benchmarks, effective rates range from 2.3\\% to 14.9\\%, making MMLU an outlier rather than representative.\n\n\\paragraph{Method Disagreement as Field-Wide Challenge.} The near-orthogonality of DIF, ConStat, and DVD flags (pairwise Jaccard $0.06$--$0.19$) is perhaps our most provocative finding. If three independent methods claiming to detect item-level anomalies flag almost entirely different items, the field faces a construct validity crisis: either these methods measure genuinely different phenomena, or at least some are measuring artifacts. The ensemble failure (majority-vote AUROC $= 0.58$) confirms that simple aggregation cannot resolve this disagreement.\n\n\\paragraph{Cohort Dependence.} The RL robustness experiment (Jaccard $= 0.43$ when adding 13 reasoning-RL models) demonstrates that DIF flags are properties of the cohort definition, not stable item attributes. Our characterization is specific to the 2023-vs-2024 temporal split. Benchmark maintainers should not treat DIF results as fixed item labels but as cohort-specific diagnostics.\n\n\\paragraph{Monitoring Over Remediation.} Graceful degradation analysis shows that removing 31\\% of items would reduce reliability from 0.94 to $\\sim$0.85 and construct coverage to 0.82. Item generation cannot yet produce calibrated replacements ($\\rho = 0.47$ vs.\\ target 0.75). Together, these findings argue for monitoring stability over time rather than acting on individual flags.\n\n%==============================================================================\n\\section{Limitations}\n\\label{sec:limitations}\n%==============================================================================\n\nFirst, MH's total-score conditioning is a limited ability proxy. With 98\\% IRT misfit and failed bifactor convergence, the conditioning may not adequately control for multidimensional ability differences between cohorts. Multidimensional IRT or propensity-score methods may yield different results.\n\nSecond, our characterization is cohort-specific. The 14.9\\% effective rate depends on the 2023-vs-2024 split; different temporal boundaries, different benchmarks, or the inclusion of reasoning-RL models produce substantially different results (effective C\\% ranges from 2.3\\% to 14.9\\% across benchmarks; Jaccard $= 0.43$ with RL models).\n\nThird, the semi-synthetic framework uses a simplified contamination mechanism (incorrect$\\to$correct flipping). Real contamination may involve subtler changes in response distributions that our injection does not capture. Detection power under worst-case parameterization is moderate ($\\Delta$TPR $= 0.26$ at $p = 0.5$).\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe present the first large-scale item-level stability analysis of LLM benchmarks, applying nonparametric MH analysis to 5,227 models across 12,508 MMLU items and five additional benchmarks. The observed 31\\% raw behavioral heterogeneity decomposes into approximately 15\\% genuine temporal signal and 16\\% cohort composition artifact. This signal is benchmark-specific (2--15\\% effective rate across benchmarks), method-dependent (three detectors produce near-disjoint flags), and cohort-sensitive (reasoning-RL models destabilize flags). We contribute a semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR $\\approx 0$) as reusable infrastructure. Our findings motivate treating item-level stability as an ongoing monitoring metric rather than a one-time diagnostic.\n\n%==============================================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nJasper Dekoninck, Mark Niklas M{\\\"u}ller, and Martin Vechev.\n\\newblock Con{S}tat: Statistical testing for {LLM} contamination detection.\n\\newblock In \\textit{Proceedings of NeurIPS}, 2024.\n\n\\bibitem[Holland and Thayer(1988)]{holland1988differential}\nPaul~W. Holland and Dorothy~T. Thayer.\n\\newblock Differential item performance and the {M}antel-{H}aenszel procedure.\n\\newblock In \\textit{Test Validity}, pages 129--145. Lawrence Erlbaum, 1988.\n\n\\bibitem[Li et~al.(2024)]{li2024task}\nYucheng Li, Frank Guerin, and Chenghua Lin.\n\\newblock Task contamination: Language models may not be few-shot anymore.\n\\newblock In \\textit{Proceedings of AAAI}, 2024.\n\n\\bibitem[Mantel and Haenszel(1959)]{mantel1959statistical}\nNathan Mantel and William Haenszel.\n\\newblock Statistical aspects of the analysis of data from retrospective studies of disease.\n\\newblock \\textit{Journal of the National Cancer Institute}, 22(4):719--748, 1959.\n\n\\bibitem[Oren et~al.(2024)]{oren2024proving}\nYonatan Oren, Nicole Meister, Niladri Chatterji, Faisal Ladhak, and Tatsunori~B. Hashimoto.\n\\newblock Proving test set contamination in black box language models.\n\\newblock In \\textit{Proceedings of ICLR}, 2024.\n\n\\bibitem[Perlitz et~al.(2024)]{perlitz2024metabench}\nYotam Perlitz, Elron Bandel, Ariel Gera, Ofir Arviv, Liat Ein-Dor, Eyal Shnarch, Noam Slonim, Michal Shmueli-Scheuer, and Leshem Choshen.\n\\newblock Efficient benchmarking (of language models).\n\\newblock \\textit{arXiv preprint arXiv:2308.11696}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nFelipe~Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin.\n\\newblock tiny{B}enchmarks: evaluating {LLM}s with fewer examples.\n\\newblock In \\textit{Proceedings of ICML}, 2024.\n\n\\bibitem[Raju et~al.(2024)]{raju2024growing}\nAnirudh Raju, Harish Kamath, and Heather Lent.\n\\newblock Growing pains: Understanding the limitations of {LLM} evaluation benchmarks.\n\\newblock \\textit{arXiv preprint arXiv:2410.08455}, 2024.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nWeijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\textit{Proceedings of ICLR}, 2024.\n\n\\bibitem[Sinharay et~al.(2006)]{sinharay2006bayesian}\nSandip Sinharay, Matthew~S. Johnson, and H.~Swaminathan.\n\\newblock Bayesian estimation of differential item functioning.\n\\newblock \\textit{Psychometrika}, 71(1):145--168, 2006.\n\n\\bibitem[Tutz and Berger(2016)]{tutz2016item}\nGerhard Tutz and Moritz Berger.\n\\newblock Item-focused trees for the identification of items in differential item functioning.\n\\newblock \\textit{Psychometrika}, 81(3):727--750, 2016.\n\n\\bibitem[Zhang et~al.(2024)]{zhang2024careful}\nHugh Zhang, Jeff Da, Dean Lee, Vaughn Robinson, Catherine Wu, Will Song, Tiffany Zhao, Pranav Raja, Dylan Slack, Qin Lv, Sean Hendryx, Summer Yue, and others.\n\\newblock A careful examination of large language model performance on grade school math.\n\\newblock \\textit{arXiv preprint arXiv:2405.00332}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "f842f265-41d2-415c-91c9-bddac96e75fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T165710 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "c16d10f6-d22f-4f4f-b4d6-d1211c88cd3a",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream benchmark analysis",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e"
}
```

---

### Tool call

_source line 23 · 2026-05-21T17:33:27.074Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RH93mk7jvkw7mhVPKdB3o6`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c16d10f6-d22f-4f4f-b4d6-d1211c88cd3a",
  "isSidechain": false,
  "requestId": "req_011CbG7dJnaSEJZnyyPwjcj8",
  "type": "assistant",
  "uuid": "0560a7f2-12c9-4d1c-a1f1-03e80c0c50da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUAGhC549uStv8L2vGoH2j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12363,
      "cache_read_input_tokens": 51370,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12363,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 51370,
          "cache_creation_input_tokens": 12363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12363
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

_source line 24 · 2026-05-21T17:33:28.108Z_

<details><summary>↩ Tool result · `toolu_01RH93mk7jvkw7mhVPKdB3o6`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
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

Package natbib Warning: Citation `mantel1959statistical' on page 1 undefined on
 input line 41.


Package natbib Warning: Citation `holland1988differential' on page 1 undefined 
on input line 41.


Package natbib Warning: Citation `perlitz2024metabench' on page 1 undefined on 
input line 41.


Package natbib Warning: Citation `li2024task' on page 1 undefined on input line
 54.


Package natbib Warning: Citation `oren2024proving' on page 1 undefined on input
 line 54.


Package natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu
t line 54.


Package natbib Warning: Citation `dekoninck2024constat' on page 1 undefined on 
input line 54.


Package natbib Warning: Citation `oren2024proving' on page 1 undefined on input
 line 54.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `holland1988differential' on page 2 undefined 
on input line 56.


Package natbib Warning: Citation `sinharay2006bayesian' on page 2 undefined on 
input line 56.


Package natbib Warning: Citation `tutz2016item' on page 2 undefined on input li
ne 56.


Package natbib Warning: Citation `raju2024growing' on page 2 undefined on input
 line 58.


Package natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o
n input line 58.


LaTeX Warning: Reference `sec:irt_fit' on page 2 undefined on input line 73.

[2]

LaTeX Warning: Reference `tab:multi_bench' on page 3 undefined on input line 18
2.

[3]

Package natbib Warning: Citation `zhang2024careful' on page 4 undefined on inpu
t line 210.


LaTeX Warning: Reference `tab:semi_synth' on page 4 undefined on input line 246
.


LaTeX Warning: Reference `tab:matching' on page 4 undefined on input line 248.


LaTeX Warning: Reference `tab:rl_stability' on page 4 undefined on input line 2
85.

[4]

LaTeX Warning: Reference `tab:constat' on page 5 undefined on input line 324.


LaTeX Warning: Reference `tab:dvd' on page 5 undefined on input line 342.


LaTeX Warning: Reference `tab:irt_fit' on page 5 undefined on input line 371.

[5]

LaTeX Warning: Reference `tab:arch' on page 6 undefined on input line 394.


Overfull \hbox (2.43774pt too wide) in paragraph at lines 394--395
\T1/ptm/m/n/10.95 METABENCH MMLU is 99.98% decoder-only (5,226/5,227 mod-els). 
Re-mov-ing the sin-gle non-decoder

LaTeX Warning: Reference `tab:regression' on page 6 undefined on input line 414
.


LaTeX Warning: Reference `tab:degradation' on page 6 undefined on input line 43
6.


LaTeX Warning: Reference `tab:ift' on page 6 undefined on input line 460.

[6]

LaTeX Warning: Reference `tab:calibration' on page 7 undefined on input line 48
0.


Package natbib Warning: Citation `sinharay2006bayesian' on page 7 undefined on 
input line 501.


LaTeX Warning: Reference `tab:bayesian_dif' on page 7 undefined on input line 5
01.

[7] [8] [9]

Package natbib Warning: There were undefined citations.

[10] [11] (./paper.aux

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
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 170067 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
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
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}] [2] [3] [4] [5]
Overfull \hbox (2.43774pt too wide) in paragraph at lines 394--395
\T1/ptm/m/n/10.95 METABENCH MMLU is 99.98% decoder-only (5,226/5,227 mod-els). 
Re-mov-ing the sin-gle non-decoder
[6] [7] [8] [9] [10] [11] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 173537 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0560a7f2-12c9-4d1c-a1f1-03e80c0c50da",
  "isSidechain": false,
  "promptId": "9377956b-ace9-4b16-82d2-21e10f437ea9",
  "type": "user",
  "uuid": "07aaee90-bd36-4df8-93e0-ca5092255bf1",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `mantel1959statistical' on page 1 undefined on\n input line 41.\n\n\nPackage natbib Warning: Citation `holland1988differential' on page 1 undefined \non input line 41.\n\n\nPackage natbib Warning: Citation `perlitz2024metabench' on page 1 undefined on \ninput line 41.\n\n\nPackage natbib Warning: Citation `li2024task' on page 1 undefined on input line\n 54.\n\n\nPackage natbib Warning: Citation `oren2024proving' on page 1 undefined on input\n line 54.\n\n\nPackage natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu\nt line 54.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 1 undefined on \ninput line 54.\n\n\nPackage natbib Warning: Citation `oren2024proving' on page 1 undefined on input\n line 54.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `holland1988differential' on page 2 undefined \non input line 56.\n\n\nPackage natbib Warning: Citation `sinharay2006bayesian' on page 2 undefined on \ninput line 56.\n\n\nPackage natbib Warning: Citation `tutz2016item' on page 2 undefined on input li\nne 56.\n\n\nPackage natbib Warning: Citation `raju2024growing' on page 2 undefined on input\n line 58.\n\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o\nn input line 58.\n\n\nLaTeX Warning: Reference `sec:irt_fit' on page 2 undefined on input line 73.\n\n[2]\n\nLaTeX Warning: Reference `tab:multi_bench' on page 3 undefined on input line 18\n2.\n\n[3]\n\nPackage natbib Warning: Citation `zhang2024careful' on page 4 undefined on inpu\nt line 210.\n\n\nLaTeX Warning: Reference `tab:semi_synth' on page 4 undefined on input line 246\n.\n\n\nLaTeX Warning: Reference `tab:matching' on page 4 undefined on input line 248.\n\n\nLaTeX Warning: Reference `tab:rl_stability' on page 4 undefined on input line 2\n85.\n\n[4]\n\nLaTeX Warning: Reference `tab:constat' on page 5 undefined on input line 324.\n\n\nLaTeX Warning: Reference `tab:dvd' on page 5 undefined on input line 342.\n\n\nLaTeX Warning: Reference `tab:irt_fit' on page 5 undefined on input line 371.\n\n[5]\n\nLaTeX Warning: Reference `tab:arch' on page 6 undefined on input line 394.\n\n\nOverfull \\hbox (2.43774pt too wide) in paragraph at lines 394--395\n\\T1/ptm/m/n/10.95 METABENCH MMLU is 99.98% decoder-only (5,226/5,227 mod-els). \nRe-mov-ing the sin-gle non-decoder\n\nLaTeX Warning: Reference `tab:regression' on page 6 undefined on input line 414\n.\n\n\nLaTeX Warning: Reference `tab:degradation' on page 6 undefined on input line 43\n6.\n\n\nLaTeX Warning: Reference `tab:ift' on page 6 undefined on input line 460.\n\n[6]\n\nLaTeX Warning: Reference `tab:calibration' on page 7 undefined on input line 48\n0.\n\n\nPackage natbib Warning: Citation `sinharay2006bayesian' on page 7 undefined on \ninput line 501.\n\n\nLaTeX Warning: Reference `tab:bayesian_dif' on page 7 undefined on input line 5\n01.\n\n[7] [8] [9]\n\nPackage natbib Warning: There were undefined citations.\n\n[10] [11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 170067 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}] [2] [3] [4] [5]\nOverfull \\hbox (2.43774pt too wide) in paragraph at lines 394--395\n\\T1/ptm/m/n/10.95 METABENCH MMLU is 99.98% decoder-only (5,226/5,227 mod-els). \nRe-mov-ing the sin-gle non-decoder\n[6] [7] [8] [9] [10] [11] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 173537 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0560a7f2-12c9-4d1c-a1f1-03e80c0c50da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-21T17:33:43.284Z_

PDF compiled successfully (11 pages, no errors). The paper covers all 16 experiments from `experiment_data.json`, each with its corresponding section and table(s):

- **Tables 1--2**: Temporal DIF on MMLU (real_data_dif_mmlu)
- **Tables 18--19**: Permutation null decomposition (permutation_null_c_rate)
- **Table 17**: Multi-benchmark stability profiles (multi_benchmark_temporal_dif)
- **Tables 7--8**: Cross-benchmark GSM8K + GSM1K correlation (cross_benchmark_gsm8k)
- **Tables 15--16**: Semi-synthetic validation (semi_synthetic_contamination_validation)
- **Tables 3--4**: RL robustness failure (rl_robustness_validation)
- **Tables 5--6**: ConStat + DVD alternative detectors (constat_perturbation_eval, dvd_generation_variance_eval)
- **Ensemble fusion**: text-only negative result (ensemble_fusion, killed)
- **Table 9**: IRT model fit failure (bifactor_irt_equating_pilot)
- **Table 14**: Architecture stratification (architecture_stratified_dif)
- **Table 20**: Regression transparency with Simpson's paradox (odds_ratio_regression_transparency)
- **Table 12**: Graceful degradation (graceful_degradation_analysis)
- **Table 13**: Item-Focused Trees (item_focused_trees)
- **Table 10**: Difficulty calibration failure (item_generation_calibration)
- **Table 11**: Cumulative Bayesian DIF (cumulative_bayesian_dif)

Output at `artifacts/dream_reports/dream_20260521T165710/worst/paper.pdf`. The worst-tier framing leads with the permutation null decomposition (52.4% of raw C% is spurious), honestly reports all negative results (bifactor failure, RL instability, method disagreement, ensemble killed, item generation failure), and reframes the paper as pure empirical characterization without psychometric claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07aaee90-bd36-4df8-93e0-ca5092255bf1",
  "isSidechain": false,
  "requestId": "req_011CbG7dh2Hjqo5GLcqoLau8",
  "type": "assistant",
  "uuid": "5989d713-107d-49bf-a634-8b6770acef5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/worst",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrTgU7dSYYQur45sR3ytPU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6407,
      "cache_read_input_tokens": 63733,
      "output_tokens": 496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 496,
          "cache_read_input_tokens": 63733,
          "cache_creation_input_tokens": 6407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6407
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T165710 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "5989d713-107d-49bf-a634-8b6770acef5f",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream benchmark analysis",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T165710 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "5989d713-107d-49bf-a634-8b6770acef5f",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream benchmark analysis",
  "sessionId": "2139658a-dd10-4943-bdfb-7044b07d629e"
}
```

---
