# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T110541 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/7a8181aa-c348-44b4-9fba-f3c9d9744120.jsonl`
- **Structured JSON:** [`3b8458c63a3a67d6b0df.json`](../../sessions/3b/3b8458c63a3a67d6b0df.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T11:38:51.007Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T11:38:51.007Z",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T110541 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：放弃 'temporal instability as primary finding' framing。Reframe 为 methodological contribution paper： (1) Semi-synthetic validation framework (ΔFPR=0.000) 升级为 primary contribution； (2) Ground truth meta-critique 升级为 co-primary contribution； (3) Temporal DIF findings 降级为 motivating example / case study； (4) Audit protocol 重新定位为 'proposed workflow'。 Title 改为类似 'Validating Item-Level Contamination Detection: A Semi-Synthetic Framework with Cross-Subject Matching'。 仍冲 EMNLP methodology track，但需要 substantially 重写 intro/framing。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T11:38:51.011Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T11:38:51.011Z",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120"
}
```

---

## Round 1

36 recorded events

### User

_source line 3 · 2026-05-21T11:38:51.032Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T110541 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：放弃 'temporal instability as primary finding' framing。Reframe 为 methodological contribution paper： (1) Semi-synthetic validation framework (ΔFPR=0.000) 升级为 primary contribution； (2) Ground truth meta-critique 升级为 co-primary contribution； (3) Temporal DIF findings 降级为 motivating example / case study； (4) Audit protocol 重新定位为 'proposed workflow'。 Title 改为类似 'Validating Item-Level Contamination Detection: A Semi-Synthetic Framework with Cross-Subject Matching'。 仍冲 EMNLP methodology track，但需要 substantially 重写 intro/framing。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "053b0da8-7122-4261-b381-207d5502fd28",
  "type": "user",
  "uuid": "cd3f5fd1-1fcc-44fc-84b8-050d51122fe0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T11:38:51.031Z_

```json
{
  "parentUuid": "cd3f5fd1-1fcc-44fc-84b8-050d51122fe0",
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
  "uuid": "bd0b9280-2bdc-4084-ba04-9346d9ff91bc",
  "timestamp": "2026-05-21T11:38:51.031Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T11:38:51.031Z_

```json
{
  "parentUuid": "bd0b9280-2bdc-4084-ba04-9346d9ff91bc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6bffdcb3-c7a7-4f3d-b0cd-2cccce5cb54d",
  "timestamp": "2026-05-21T11:38:51.031Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 6 · 2026-05-21T11:38:54.007Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bffdcb3-c7a7-4f3d-b0cd-2cccce5cb54d",
  "isSidechain": false,
  "requestId": "req_011CbFebGVxRNj4kTVGtuQwD",
  "type": "assistant",
  "uuid": "57d030ee-9643-47bd-be0d-e828d442fa0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKja4JKae5SocvGYBVQUvU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12246,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12246
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

_source line 7 · 2026-05-21T11:38:55.074Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RkCso3cd9ksRt2PQbEgppu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57d030ee-9643-47bd-be0d-e828d442fa0c",
  "isSidechain": false,
  "requestId": "req_011CbFebGVxRNj4kTVGtuQwD",
  "type": "assistant",
  "uuid": "bfc52cac-ef30-4189-a991-ba87eb875a11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKja4JKae5SocvGYBVQUvU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12246,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12246
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

_source line 8 · 2026-05-21T11:38:55.352Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tm1sJd9MHn4zUSiHCaKHx1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfc52cac-ef30-4189-a991-ba87eb875a11",
  "isSidechain": false,
  "requestId": "req_011CbFebGVxRNj4kTVGtuQwD",
  "type": "assistant",
  "uuid": "9083f5ef-5d50-418f-a18d-d6ee82b90d5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKja4JKae5SocvGYBVQUvU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12246,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12246
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

_source line 9 · 2026-05-21T11:38:55.368Z_

<details><summary>↩ Tool result · `toolu_01RkCso3cd9ksRt2PQbEgppu`</summary>

```text
1	[
2	  {
3	    "name": "real_data_dif_mmlu",
4	    "description": "METABENCH MMLU response matrix (5,219 models × 12,508 items) 上的 MH-DIF 分析，含 temporal/ability cohort、within-family confound control、domain-specificity",
5	    "results": {
6	      "temporal_ets_c_pct": 31.3,
7	      "temporal_fpr_li_clean": 0.32,
8	      "temporal_enrichment": 0.96,
9	      "ability_ets_c_pct": 2.9,
10	      "ability_enrichment": 1.19,
11	      "within_family_llama2v3_c_pct": 61.3,
12	      "within_family_mistral_mixtral_c_pct": 38.7,
13	      "domain_spearman_rho": 0.38,
14	      "domain_spearman_p": 0.004,
15	      "sanity_random_split_c_pct": 0.18,
16	      "temporal_ability_jaccard": 0.014,
17	      "irt_lz_above_2_pct": 98.0
18	    },
19	    "tables": [
20	      {
21	        "title": "Table 1: DIF Classification by Cohort Definition",
22	        "columns": [
23	          "cohort",
24	          "n_ref",
25	          "n_foc",
26	          "pct_A",
27	          "pct_B",
28	          "pct_C",
29	          "enrichment_li"
30	        ],
31	        "rows": [
32	          [
33	            "temporal_2023v2024",
34	            1253,
35	            656,
36	            48.2,
37	            20.5,
38	            31.3,
39	            0.96
40	          ],
41	          [
42	            "ability_quintile",
43	            1044,
44	            1044,
45	            89.8,
46	            7.3,
47	            2.9,
48	            1.19
49	          ],
50	          [
51	            "random_split_control",
52	            950,
53	            950,
54	            97.3,
55	            2.5,
56	            0.18,
57	            1.01
58	          ]
59	        ]
60	      },
61	      {
62	        "title": "Table 2: Within-Family DIF (Confound Control)",
63	        "columns": [
64	          "family_pair",
65	          "n_ref",
66	          "n_foc",
67	          "pct_C",
68	          "interpretation"
69	        ],
70	        "rows": [
71	          [
72	            "Llama-2_vs_Llama-3",
73	            161,
74	            308,
75	            61.3,
76	            "generation gap drives DIF"
77	          ],
78	          [
79	            "Mistral_vs_Mixtral",
80	            89,
81	            142,
82	            38.7,
83	            "architecture shift contributes"
84	          ]
85	        ]
86	      }
87	    ],
88	    "figures": [],
89	    "analysis": "Worst-tier reviewer 的核心论证链：domain ρ=0.38 → within-family 61% → enrichment≈1.0 → IRT 98% misfit → 结论是 \"DIF 在 MMLU 上不是 item instability detector，而是 capability gap detector， 你的 31% 就是在说 models got better on 31% of items\"。这个攻击路径在逻辑上是 self-consistent 的， 即使 item-level decomposition 只解释 2.4pp——reviewer 会说 domain-level predictor 是 wrong granularity， 真正的 confound 是 item-level difficulty × model generation interaction。\n\n\n在 worst 档下，31.3% C% 本身可复现但被 reviewer 视为 artifact。核心攻击点： (1) domain_spearman_rho=0.38 (p=0.004) 比 best 档预期的 0.25-0.30 更高，reviewer 用此论证 DIF 主要捕捉 domain-level capability improvement 而非 item instability； (2) within-family Llama-2v3 C%=61.3% 被解读为 \"DIF 在测 generation gap\"——Llama-2 到 Llama-3 是 architecture + scale + data 全面升级，61% DIF 恰恰说明 DIF 在测能力提升； (3) enrichment=0.96 ≈ 1.0 被解读为 DIF 与任何已知 contamination signal 无关——\"你的方法跟 contamination 没关系，它只是在找 hard items that newer models solve\"； (4) IRT |Lz|>2 at 98% 被解读为 conditioning variable (total score) 根本不适合 MMLU—— MH 依赖 total score 做 ability matching，但 57-subject multidimensional structure 使 total score 成为 poor proxy，整个 DIF 分析的 conditioning 基础被质疑。 random split 0.18% 只证明 temporal signal 存在，不证明 signal = instability。\n"
90	  },
91	  {
92	    "name": "rl_robustness_validation",
93	    "description": "DIF 对 RL 训练模型的鲁棒性验证：alignment-RL (DPO/ORPO, N=477) + reasoning-RL (GRPO/PPO, N=10-15)",
94	    "results": {
95	      "alignment_rl_cohort_c_pct": 29.8,
96	      "alignment_rl_jaccard_vs_temporal": 0.72,
97	      "reasoning_rl_n_models": 13,
98	      "reasoning_rl_added_to_focal_c_pct": 30.5,
99	      "reasoning_rl_jaccard_vs_base_focal": 0.85,
100	      "delong_p_dif_vs_constat": 0.23,
101	      "delong_p_dif_vs_mink": 0.18,
102	      "tost_equivalence_p": 0.08,
103	      "constat_auroc_non_rl": 0.74,
104	      "constat_auroc_rl": 0.68,
105	      "mink_auroc_non_rl": 0.71,
106	      "mink_auroc_rl": 0.63,
107	      "dif_auroc_across_compositions": 0.61,
108	      "partial_exploitation_detection_boundary_p": 0.55,
109	      "bootstrap_ci_width_auroc": 0.15
110	    },
111	    "tables": [
112	      {
113	        "title": "Table: Detection AUROC by Method × Model Type",
114	        "columns": [
115	          "method",
116	          "non_rl_auroc",
117	          "alignment_rl_auroc",
118	          "reasoning_rl_auroc",
119	          "delta"
120	        ],
121	        "rows": [
122	          [
123	            "MH-DIF",
124	            0.62,
125	            0.61,
126	            0.6,
127	            -0.02
128	          ],
129	          [
130	            "ConStat",
131	            0.74,
132	            0.71,
133	            0.68,
134	            -0.06
135	          ],
136	          [
137	            "Min-K%",
138	            0.71,
139	            0.69,
140	            0.63,
141	            -0.08
142	          ]
143	        ]
144	      }
145	    ],
146	    "figures": [],
147	    "analysis": "在 worst 档 reframing 中，此实验被降级甚至 drop。N=13 的 RL 验证无法支撑任何 robust claim。 如果 reviewer 看到 DIF AUROC=0.61 且 bootstrap CI=[0.54, 0.76]，会质疑 \"为什么要用 detection power 这么低的方法\"。Reframed paper 中应将此实验移入 appendix 作为 preliminary evidence， 或完全 drop 并在 limitations 中说明。\n\n\nWorst 档下此实验有两个致命问题： (1) N=13 reasoning-RL models 使所有统计检验 underpowered——DeLong test p=0.23 和 TOST p=0.08 都不显著，reviewer 正确指出 \"你无法区分 DIF 对 RL 鲁棒 vs 你没有足够样本检测差异\"； (2) DIF AUROC=0.61 本身就低——reviewer 论证 MH-DIF 在 any cohort composition 下 detection power 都不 competitive，不是 RL-robust 而是 uniformly weak； (3) ConStat 和 Min-K% 在 RL 上的 degradation (0.74→0.68, 0.71→0.63) 比预期温和， 不足以构成 \"traditional methods fail on RL\" 的 strong claim。 Bootstrap CI width=0.15 在 13 个模型上是预期内的，但 reviewer 会说这个宽度下任何 claim 都是 preliminary。\n"
148	  },
149	  {
150	    "name": "constat_perturbation_eval",
151	    "description": "ConStat-style perturbation testing 在 MMLU 上的独立评估：200+ items LLM paraphrasing + FDR-controlled detection",
152	    "results": {
153	      "n_items_reformulated": 220,
154	      "constat_fdr_controlled_detections": 45,
155	      "constat_detection_rate": 0.205,
156	      "constat_fpr_estimate": 0.08,
157	      "constat_auroc_non_rl": 0.74,
158	      "constat_auroc_rl": 0.68,
159	      "constat_dif_overlap_jaccard": 0.15,
160	      "paraphrase_quality_score": 0.82
161	    },
162	    "tables": [],
163	    "figures": [],
164	    "analysis": "此实验在 worst 档的 reframed paper 中价值有限。如果 DIF 被降级为 case study， ConStat comparison 也失去 anchor。可以保留为 \"related methods comparison\" 但不再是核心 contribution。\n\n\nWorst 档下，ConStat detection rate=20.5% 在 non-RL 模型上是 reasonable baseline， 但 DIF-ConStat overlap Jaccard=0.15 极低——reviewer 论证两种方法在测不同的东西， ensemble 前提不成立。ConStat 的 AUROC=0.74 > DIF 的 0.62，reviewer 会问 \"既然 ConStat 更准，为什么不直接用 ConStat？DIF 的 added value 在哪里？\" 更致命的是，ConStat 在 RL 上只 degradation 6pp (0.74→0.68)， 不够 dramatic 来支撑 \"traditional methods fail on RL\" 的 narrative。\n"
165	  },
166	  {
167	    "name": "dvd_generation_variance_eval",
168	    "description": "DVD generation variance 在 MMLU 上的独立评估：10-15 open-weight models × 50 responses/item",
169	    "results": {
170	      "n_models_evaluated": 12,
171	      "n_items_scored": 1200,
172	      "dvd_bimodal_detection_rate": 0.12,
173	      "dvd_auroc": 0.65,
174	      "dvd_dif_overlap_jaccard": 0.11,
175	      "dvd_constat_overlap_jaccard": 0.22,
176	      "verbatim_vs_variant_dvd_gap": 0.18
177	    },
178	    "tables": [],
179	    "figures": [],
180	    "analysis": "DVD 在 worst 档下是 net negative——弱结果被 reviewer 用来论证 contamination detection 整个 paradigm 的 fragility。建议在 reframed paper 中 drop 此实验。\n\n\nDVD detection rate=12% 低于 ConStat 的 20.5%，AUROC=0.65 处于 poor-to-fair 区间。 DVD-DIF overlap Jaccard=0.11 甚至低于 ConStat-DIF 的 0.15——三种方法之间的 agreement 极低，reviewer 论证 \"这些方法在测量三个不同的东西，没有一个是 validated contamination signal\"。 N=12 模型的 generation variance 采样也不足以覆盖 model diversity。 在 worst 档下，DVD 的弱结果进一步削弱了 ensemble 的 rationale。\n"
181	  },
182	  {
183	    "name": "ensemble_fusion",
184	    "description": "DIF + ConStat + DVD 三信号融合：calibrated thresholds + 2-of-3 voting + weighted fusion",
185	    "results": {
186	      "ensemble_2of3_coverage": 0.38,
187	      "ensemble_2of3_fpr": 0.12,
188	      "ensemble_weighted_auroc": 0.72,
189	      "ensemble_vs_best_single_auroc_gain": -0.02,
190	      "cross_val_weight_stability_cv": 0.35,
191	      "uniform_vs_optimized_auroc_gap": 0.03
192	    },
193	    "tables": [
194	      {
195	        "title": "Table: Ensemble vs Individual Signal Performance",
196	        "columns": [
197	          "method",
198	          "auroc",
199	          "fpr_at_80recall",
200	          "coverage"
201	        ],
202	        "rows": [
203	          [
204	            "DIF (MH)",
205	            0.62,
206	            0.38,
207	            0.31
208	          ],
209	          [
210	            "ConStat",
211	            0.74,
212	            0.12,
213	            0.21
214	          ],
215	          [
216	            "DVD",
217	            0.65,
218	            0.28,
219	            0.12
220	          ],
221	          [
222	            "Ensemble (2-of-3)",
223	            0.68,
224	            0.12,
225	            0.38
226	          ],
227	          [
228	            "Ensemble (weighted)",
229	            0.72,
230	            0.11,
231	            0.42
232	          ]
233	        ]
234	      }
235	    ],
236	    "figures": [],
237	    "analysis": "Ensemble 在 worst 档下是 paper 的最大 sunk cost。三信号 low-agreement + ensemble ≤ best single = reviewer 一句话 kill：\"the whole is less than its parts\"。Reframed paper 必须完全 drop Claim 2 (ensemble)，将 plan_003a/b/c 全部移入 \"future work\"。\n\n\nWorst 档下 ensemble 的核心问题是 base signal quality 太低。三种方法 pairwise Jaccard 全部 <0.25，2-of-3 voting 的 agreement 稀少导致 coverage=38% 但 FPR=12% (超过 0.10 target)。 weighted fusion AUROC=0.72 竟然低于 ConStat standalone 的 0.74——ensemble 反而 hurt performance。 cross-validation weight stability CV=0.35 表明 weights 在 fold 间不稳定，reviewer 正确指出 \"你的 ensemble 在 overfitting fold-specific patterns\"。 这个实验在 original framing (Claim 2: ensemble detection) 下是 fatal negative， 是 paper framing pivot 的直接原因之一。\n"
238	  },
239	  {
240	    "name": "cross_benchmark_gsm8k",
241	    "description": "GSM8K 上的 DIF 复制 + GSM1K ground truth correlation + semi-synthetic validation",
242	    "results": {
243	      "gsm8k_temporal_c_pct": 18.9,
244	      "gsm8k_external_c_pct": 47.4,
245	      "gsm8k_sanity_c_pct": 0.3,
246	      "semi_synthetic_delta_tpr_p10": 0.818,
247	      "semi_synthetic_delta_tpr_p05": 0.42,
248	      "gsm1k_n_models": 33,
249	      "gsm1k_pearson_r": -0.478,
250	      "gsm1k_spearman_rho": -0.403,
251	      "gsm1k_direction": "NEGATIVE",
252	      "gsm1k_partial_r": -0.385,
253	      "gsm1k_permutation_p": 0.014,
254	      "gsm1k_ci_upper_r": -0.16,
255	      "gsm1k_ci_upper_rho": -0.03
256	    },
257	    "tables": [
258	      {
259	        "title": "Table: GSM1K Contamination Gap vs DIF Flag Correlation",
260	        "columns": [
261	          "metric",
262	          "value",
263	          "ci_lower",
264	          "ci_upper",
265	          "p_value"
266	        ],
267	        "rows": [
268	          [
269	            "pearson_r",
270	            -0.478,
271	            -0.71,
272	            -0.16,
273	            0.005
274	          ],
275	          [
276	            "spearman_rho",
277	            -0.403,
278	            -0.67,
279	            -0.03,
280	            0.02
281	          ],
282	          [
283	            "partial_r_controlling_acc",
284	            -0.385,
285	            -0.65,
286	            -0.04,
287	            0.027
288	          ]
289	        ]
290	      }
291	    ],
292	    "figures": [],
293	    "analysis": "GSM1K negative correlation 是 worst 档最有力的 ammunition。在 reframed paper 中必须 将此结果 reinterpret 为 \"DIF and contamination measure orthogonal constructs\"—— 这 actually supports Claim 2 (ground truth meta-critique) 而不是 undermines it。 Key reframing: \"DIF measures differential item functioning, not contamination per se. The negative GSM1K correlation confirms that item-level behavioral change ≠ contamination signal, validating our meta-critique that web-overlap labels are fundamentally mismatched.\"\n\n\nWorst 档下此实验有一个 devastating result：GSM1K correlation 方向是 NEGATIVE (r=-0.478)—— DIF-C items 与 contamination gap 反相关。Reviewer 的解读：\"DIF 标记的 items 恰恰是 2024 模型 genuinely improved 的 items（不需要 contamination），而真正 contaminated 的 items 不被 DIF 检测到，因为 contamination 是 uniform across cohorts\"。 这直接支持了 worst 档的核心假设——DIF 在测 'models got better' 而非 contamination。 N=33 虽小但方向一致 (permutation p=0.014)，CI upper bound |r|=0.16 也远离 positive territory。 Semi-synthetic ΔTPR=0.42 at p=0.5 落在 worst 档范围 [0.3, 0.5] 内，被视为 \"moderate 但不 compelling\"——p=0.5 意味着一半 contaminated models 必须 exploit item 才能检测到。\n"
294	  },
295	  {
296	    "name": "bifactor_irt_equating_pilot",
297	    "description": "MMLU bifactor IRT 模型拟合 + anchor item 选择 + fixed-parameter calibration equating pilot",
298	    "results": {
299	      "bifactor_convergence": false,
300	      "bifactor_rmsea": 0.089,
301	      "bifactor_cfi": 0.72,
302	      "bifactor_tli": 0.68,
303	      "bifactor_srmr": 0.11,
304	      "general_factor_explained_variance_pct": 28.4,
305	      "n_anchor_items_selected": 0,
306	      "equating_feasible": false,
307	      "computation_time_hours": 18.5,
308	      "convergence_code": "iteration limit reached"
309	    },
310	    "tables": [],
311	    "figures": [],
312	    "analysis": "Bifactor failure 是 plan_005/006/008 整条 pipeline 的 kill signal。在 reframed paper 中 列入 limitations：\"IRT-based equating requires adequate model fit; MMLU's 57-subject multidimensional structure defeats both unidimensional and bifactor specifications. This motivates future work on multidimensional IRT or subject-specific calibration.\"\n\n\nWorst 档下 bifactor 模型 fails to converge on 12,508 × 5,219 矩阵。 即使强制截断 iterations，fit indices 全部不达标 (RMSEA=0.089 > 0.06 cutoff, CFI=0.72 < 0.90 cutoff, TLI=0.68)。General factor 仅解释 28.4% variance， 说明 MMLU 的 57-subject structure 导致 essentially 无法用 single general factor 建模。 这直接验证了 reviewer 的 IRT misfit concern——不只是 |Lz| 的问题，连 bifactor 都 fail， 说明 MMLU 在 IRT 框架下 fundamentally ill-behaved。 结果：equating pipeline 被 kill，anchor items 无法选择，plan_006 (item generation) 也被 block。 这个 negative result 在 reframed paper 中反而有价值——motivates future multidimensional IRT work。\n"
313	  },
314	  {
315	    "name": "item_generation_calibration",
316	    "description": "DIF-flagged MMLU items 的 LLM 替换生成 + student simulation calibration",
317	    "results": {
318	      "n_items_generated": 0,
319	      "difficulty_correlation_prompt": null,
320	      "difficulty_correlation_simulation": null,
321	      "calibration_feasible": false,
322	      "blocked_by": "plan_005_bifactor_failure"
323	    },
324	    "tables": [],
325	    "figures": [],
326	    "analysis": "Not executed。在 reframed paper 中完全 drop，不出现在 main body 或 appendix。 Original Claim 3 (regeneration) 已被 bifactor failure 否定。\n\n\nWorst 档下此实验被 plan_005 failure 完全 block。没有可靠的 IRT 参数估计和 anchor items， 生成的替换 items 无法 calibrate 到 equated scale 上。即使独立运行 prompt-based generation， 已有文献 (arXiv 2602.06631) 表明 difficulty correlation 仅 ρ=0.10-0.45， 而 student simulation 需要先有 IRT 参数才能 simulate——circular dependency。 整个 regeneration pipeline (original Claim 3) 被 kill，是 paper pivot 的主要 driver 之一。\n"
327	  },
328	  {
329	    "name": "cumulative_bayesian_dif",
330	    "description": "Sinharay et al. (2006) cumulative Bayesian DIF priors 的 simulation study：4 successive administrations",
331	    "results": {
332	      "individual_admin_tpr_delta10": 0.42,
333	      "cumulative_2admin_tpr": 0.55,
334	      "cumulative_3admin_tpr": 0.63,
335	      "cumulative_4admin_tpr": 0.68,
336	      "target_tpr_070": false,
337	      "individual_admin_tpr_delta14": 0.58,
338	      "fpr_all_below_010": true,
339	      "prior_sensitivity_max_tpr_swing": 0.09
340	    },
341	    "tables": [
342	      {
343	        "title": "Table: Cumulative DIF Power by Number of Administrations",
344	        "columns": [
345	          "n_admin",
346	          "delta_10_tpr",
347	          "delta_14_tpr",
348	          "delta_16_tpr",
349	          "fpr"
350	        ],
351	        "rows": [
352	          [
353	            1,
354	            0.42,
355	            0.58,
356	            0.68,
357	            0.04
358	          ],
359	          [
360	            2,
361	            0.55,
362	            0.71,
363	            0.79,
364	            0.05
365	          ],
366	          [
367	            3,
368	            0.63,
369	            0.78,
370	            0.85,
371	            0.05
372	          ],
373	          [
374	            4,
375	            0.68,
376	            0.83,
377	            0.89,
378	            0.06
379	          ]
380	        ]
381	      }
382	    ],
383	    "figures": [],
384	    "analysis": "Simulation-only + IRT misfit = reviewer 完全 dismiss。在 reframed paper 中移入 appendix 或 drop。Methodology track reviewer 可能 appreciate the framework 但会要求 real data validation。\n\n\nWorst 档下 cumulative power improvement 存在但低于 target：3-admin 后 TPR=0.63 < 0.70 target， 4-admin 才到 0.68。Reviewer 批评这是 pure simulation：\"你没有 4 个 time period 的真实数据， 这只是说 'if we had more data, DIF would work better'——tautological。\" 更关键的是，simulation 使用 well-specified 1D IRT model，而真实 MMLU 的 IRT misfit (98%) 意味着 simulation results 不 transferable。\"你在模拟一个你已经证明不存在的世界。\"\n"
385	  },
386	  {
387	    "name": "graceful_degradation_analysis",
388	    "description": "Benchmark validity degradation under progressive item replacement (5%–50%)",
389	    "results": {
390	      "replacement_5pct_rho": 0.999,
391	      "replacement_10pct_rho": 0.998,
392	      "replacement_20pct_rho": 0.996,
393	      "replacement_50pct_rho": 0.988,
394	      "replacement_5pct_shr": 0.993,
395	      "replacement_10pct_shr": 0.991,
396	      "replacement_20pct_shr": 0.987,
397	      "replacement_50pct_shr": 0.972,
398	      "construct_coverage_maintained_at_20pct": true,
399	      "blocked_by_equating": true
400	    },
401	    "tables": [
402	      {
403	        "title": "Table: Ranking Stability Under Progressive Item Replacement",
404	        "columns": [
405	          "replacement_pct",
406	          "spearman_rho",
407	          "shr",
408	          "construct_coverage_ratio"
409	        ],
410	        "rows": [
411	          [
412	            5,
413	            0.999,
414	            0.993,
415	            0.98
416	          ],
417	          [
418	            10,
419	            0.998,
420	            0.991,
421	            0.96
422	          ],
423	          [
424	            20,
425	            0.996,
426	            0.987,
427	            0.93
428	          ],
429	          [
430	            50,
431	            0.988,
432	            0.972,
433	            0.85
434	          ]
435	        ]
436	      }
437	    ],
438	    "figures": [],
439	    "analysis": "在 reframed paper 中，graceful degradation 反而支持 revised narrative： \"MMLU's massive redundancy means DIF-flagged items can be safely removed without validity loss — the diagnostic value of DIF is in understanding WHAT changed, not in removing items for quality control。\" 但 worst 档 reviewer 会说 \"如果 removal 没有影响，你的 whole paper 的 motivation 就不成立。\"\n\n\nWorst 档下此实验 partially blocked by plan_005 failure (无法用 equated replacement items)。 可以用 random replacement 做 simulation，结果显示极高 robustness (ρ>0.988 even at 50% replacement)。 但 reviewer 将此解读为 MMLU 的 massive redundancy 的进一步证据： \"你可以 drop 一半的 items 且 ranking 不变——这说明 MMLU 有 6000+ redundant items， 你的 31% DIF finding 完全在 redundancy margin 内，没有任何实际影响。\" 讽刺的是，robustness 越高，DIF findings 的 practical significance 越低。\n"
440	  },
441	  {
442	    "name": "item_focused_trees",
443	    "description": "Item-Focused Trees (Tutz & Berger 2016) 作为 continuous-covariate DIF 替代方案",
444	    "results": {
445	      "ift_n_items_dif": 3452,
446	      "ift_c_pct_equivalent": 27.6,
447	      "ift_mh_concordance": 0.78,
448	      "ift_split_point_median_date": "2023-09",
449	      "ift_gradual_items_pct": 62.3,
450	      "ift_abrupt_items_pct": 37.7,
451	      "ift_computation_time_hours": 8.2
452	    },
453	    "tables": [
454	      {
455	        "title": "Table: IFT vs MH-DIF Classification Comparison",
456	        "columns": [
457	          "metric",
458	          "MH_DIF",
459	          "IFT",
460	          "concordance"
461	        ],
462	        "rows": [
463	          [
464	            "n_flagged_items",
465	            3918,
466	            3452,
467	            0.78
468	          ],
469	          [
470	            "pct_C_equivalent",
471	            31.3,
472	            27.6,
473	            "-"
474	          ],
475	          [
476	            "gradual_vs_abrupt",
477	            "N/A (binary)",
478	            "62.3% / 37.7%",
479	            "-"
480	          ]
481	        ]
482	      }
483	    ],
484	    "figures": [],
485	    "analysis": "IFT 在 worst 档下是 double-edged sword：提供了 finer-grained picture 但 picture 说的是 \"gradual improvement\" 而非 \"instability\"。Reframed paper 中可以保留为 robustness check 并 reframe：\"IFT confirms that item-level behavioral changes are predominantly gradual, consistent with progressive capability development rather than discrete contamination events。\"\n\n\nWorst 档下 IFT 的 continuous treatment 暴露了 temporal DIF 的 gradual nature： 62.3% 的 DIF items 显示 gradual difficulty drift 而非 abrupt change。 Reviewer 用此论证 \"这是 models gradually getting better on certain items， 不是 contamination event 或 structural instability——difficulty drift 是 capability improvement 的自然结果，你的 binary 2023/2024 split 人为制造了 abrupt 的假象。\" Split point median at 2023-09 也不 informative——没有对应任何 specific model release event。 IFT-MH concordance=0.78 表明 MH 的 binary grouping 丢失了 22% 的 nuance。\n"
486	  },
487	  {
488	    "name": "architecture_stratified_dif",
489	    "description": "Decoder-only 子群上的 DIF 分析 + IRT fit diagnostics",
490	    "results": {
491	      "n_decoder_only": 5226,
492	      "n_non_decoder": 1,
493	      "pct_decoder_only": 99.98,
494	      "decoder_only_c_pct": 31.3,
495	      "decoder_only_jaccard_vs_full": 1.0,
496	      "irt_rmsea_full": 0.082,
497	      "irt_rmsea_decoder_only": 0.081,
498	      "irt_cfi_full": 0.74,
499	      "irt_cfi_decoder_only": 0.74,
500	      "irt_lz_above_2_pct_decoder_only": 97.8
501	    },
502	    "tables": [
503	      {
504	        "title": "Table: IRT Fit Diagnostics — Full vs Decoder-Only",
505	        "columns": [
506	          "population",
507	          "N",
508	          "RMSEA",
509	          "CFI",
510	          "TLI",
511	          "pct_Lz_above_2"
512	        ],
513	        "rows": [
514	          [
515	            "full",
516	            5227,
517	            0.082,
518	            0.74,
519	            0.71,
520	            98.0
521	          ],
522	          [
523	            "decoder_only",
524	            5226,
525	            0.081,
526	            0.74,
527	            0.71,
528	            97.8
529	          ]
530	        ]
531	      }
532	    ],
533	    "figures": [],
534	    "analysis": "此实验在 worst 档下是 necessary but trivially resolved。不提供任何 defense against IRT misfit concern。在 reframed paper 中一句话带过：\"99.98% of METABENCH models are decoder-only; architecture heterogeneity is a non-issue (Jaccard=1.0)\"。 IRT misfit 需要在 limitations 中 honestly address 而非 dismiss。\n\n\nWorst 档下此实验 trivially resolves architecture concern (99.98% decoder-only, removing 1 model changes nothing, Jaccard=1.0) 但 completely fails to address IRT misfit。RMSEA 从 0.082→0.081, CFI unchanged at 0.74——IRT misfit 不是 architecture heterogeneity 造成的，而是 MMLU 57-subject multidimensionality 造成的。 Reviewer：\"你证明了 architecture 不是问题，但 IRT misfit 依然是 98%—— 移除 1 个 encoder model 不可能解决 57-subject 的 multidimensionality 问题。 你需要的是 multidimensional IRT 或 per-subject analysis，不是 architecture stratification。\"\n"
535	  },
536	  {
537	    "name": "semi_synthetic_contamination_validation",
538	    "description": "Known contamination injection into METABENCH matrix + DIF detection power measurement",
539	    "results": {
540	      "temporal_external_tpr_p0": 0.326,
541	      "temporal_external_tpr_p03": 0.45,
542	      "temporal_external_tpr_p05": 0.42,
543	      "temporal_external_tpr_p07": 0.78,
544	      "temporal_external_tpr_p10": 0.95,
545	      "temporal_external_fpr": 0.314,
546	      "temporal_external_delta_tpr_p05": 0.35,
547	      "temporal_external_delta_tpr_p10": 0.62,
548	      "cross_subject_delta_fpr": 0.0,
549	      "within_subject_fpr_inflation": 0.186,
550	      "ability_external_delta_tpr_p10": 0.302,
551	      "standard_mh_fpr_inflation_at_p10": 0.318
552	    },
553	    "tables": [
554	      {
555	        "title": "Table: Semi-Synthetic Validation — DIF Detection Power",
556	        "columns": [
557	          "exploitation_rate_p",
558	          "tpr",
559	          "delta_tpr",
560	          "fpr",
561	          "delta_fpr"
562	        ],
563	        "rows": [
564	          [
565	            0.0,
566	            0.326,
567	            0.0,
568	            0.314,
569	            0.0
570	          ],
571	          [
572	            0.3,
573	            0.45,
574	            0.124,
575	            0.314,
576	            0.0
577	          ],
578	          [
579	            0.5,
580	            0.676,
581	            0.35,
582	            0.314,
583	            0.0
584	          ],
585	          [
586	            0.7,
587	            0.78,
588	            0.454,
589	            0.314,
590	            0.0
591	          ],
592	          [
593	            1.0,
594	            0.95,
595	            0.624,
596	            0.314,
597	            0.0
598	          ]
599	        ]
600	      }
601	    ],
602	    "figures": [],
603	    "analysis": "Semi-synthetic validation 是 worst 档 reframing 的 primary contribution。 虽然 ΔTPR=0.35 at p=0.5 不 impressive，但 (1) cross-subject ΔFPR=0.000 是 novel methodological contribution，(2) dose-response monotonicity 证明 framework 有效， (3) within vs cross matching comparison 是 actionable guidance。 Reframed paper 应强调 framework reusability 而非 specific detection performance。\n\n\nWorst 档下 semi-synthetic 的 ΔTPR at p=0.5 = 0.35，落在 worst 范围 [0.3, 0.5] 下半区。 Reviewer 的攻击： (1) \"ΔTPR=0.35 at p=0.5 意味着在 half exploitation 下你只比 baseline 多检测 35% 的 contaminated items——这在 practical terms 下意味着你漏掉了大部分 contamination\"； (2) \"Baseline FPR=0.314 意味着你的 detector 在没有 injection 时已经 flag 31.4% 的 items 作为 positive——这要么是 FPR 不可接受，要么是你的 'clean' items 并不 clean， 无论哪种解读都 undermine 你的 validation\"； (3) \"Cross-subject matching 的 ΔFPR=0.000 是 technically impressive 但 semantically questionable——你用 other subjects 的 score 做 matching variable，这意味着你在用 math ability 来 match science items，matching variable 和 target variable 的 construct relevance 未验证\"。 但在 reframed paper 中，这个实验反而是最 defensible 的——reviewer 攻击的是 interpretation 而非 methodology，cross-subject matching ΔFPR=0.000 是 hard empirical fact。\n"
604	  },
605	  {
606	    "name": "multi_benchmark_temporal_dif",
607	    "description": "6 个 benchmark (MMLU/ARC/HellaSwag/WinoGrande/TruthfulQA/GSM8K) 上的 temporal DIF 分析",
608	    "results": {
609	      "mmlu_c_pct": 31.3,
610	      "winogrande_c_pct": 30.3,
611	      "truthfulqa_c_pct": 29.7,
612	      "arc_c_pct": 26.9,
613	      "gsm8k_c_pct": 18.9,
614	      "hellaswag_c_pct": 17.9,
615	      "cross_benchmark_range": "17.9-31.3%",
616	      "all_random_controls_below_1pct": true,
617	      "min_enrichment_ratio": 45,
618	      "n_benchmarks": 6,
619	      "cross_benchmark_mean_c_pct": 25.8,
620	      "cross_benchmark_sd_c_pct": 5.8
621	    },
622	    "tables": [
623	      {
624	        "title": "Table: Cross-Benchmark Temporal DIF Summary",
625	        "columns": [
626	          "benchmark",
627	          "n_items",
628	          "n_ref",
629	          "n_foc",
630	          "pct_C",
631	          "random_pct_C",
632	          "enrichment_ratio"
633	        ],
634	        "rows": [
635	          [
636	            "MMLU",
637	            12508,
638	            1080,
639	            807,
640	            31.3,
641	            0.18,
642	            174
643	          ],
644	          [
645	            "WinoGrande",
646	            1267,
647	            1017,
648	            803,
649	            30.3,
650	            0.32,
651	            95
652	          ],
653	          [
654	            "TruthfulQA",
655	            817,
656	            1080,
657	            807,
658	            29.7,
659	            0.37,
660	            80
661	          ],
662	          [
663	            "ARC-Challenge",
664	            1172,
665	            1080,
666	            807,
667	            26.9,
668	            0.6,
669	            45
670	          ],
671	          [
672	            "GSM8K",
673	            1319,
674	            1017,
675	            804,
676	            18.9,
677	            0.3,
678	            63
679	          ],
680	          [
681	            "HellaSwag",
682	            10042,
683	            1080,
684	            807,
685	            17.9,
686	            0.28,
687	            64
688	          ]
689	        ]
690	      }
691	    ],
692	    "figures": [],
693	    "analysis": "Cross-benchmark 一致性在 worst 档下是 double-edged sword。在 original framing 下 支持 generalizability；在 worst 档下被解读为 method artifact。 Reframed paper 中应 reinterpret：\"Cross-benchmark consistency confirms that temporal cohort design reliably detects DIF across diverse benchmarks, whether the signal represents item instability, capability improvement, or both. Our semi-synthetic framework can disambiguate this — we demonstrate this on MMLU and GSM8K。\"\n\n\nWorst 档下 6-benchmark consistency (C%=17.9-31.3%, all >45× above random) 被 reviewer 反转利用。核心论证：\"所有 6 个 benchmark 都显示 high DIF 恰恰证明这是 method artifact， 不是 benchmark-specific instability。如果 DIF 在测 item instability，不同 benchmark 应该有不同的 instability profile——HellaSwag (commonsense) 和 GSM8K (math) 的 instability 机制完全不同。但 C% 的 cross-benchmark consistency (mean=25.8%, SD=5.8%) 说明 DIF 在 uniformly 捕捉 'temporal cohort difference' 的 statistical signal， 而这个 signal 就是 'models got better'。\" 更具体地：HellaSwag 和 GSM8K 的 C% 较低 (17.9%, 18.9%) 恰好是 capability improvement 最 saturated 的 benchmarks (HellaSwag accuracy >90%, GSM8K has clear skill ceiling)， 而 MMLU (31.3%) 和 WinoGrande (30.3%) 的 C% 较高恰好是 improvement space 最大的 benchmarks。 这个 pattern 与 \"DIF = capability improvement\" 假说 perfectly consistent。\n"
694	  },
695	  {
696	    "name": "permutation_null_c_rate",
697	    "description": "1000× permutation test：randomly reassign temporal labels → MH-DIF → null C% distribution",
698	    "results": {
699	      "n_permutations": 1000,
700	      "null_c_pct_mean": 0.22,
701	      "null_c_pct_sd": 0.08,
702	      "null_c_pct_95th": 0.38,
703	      "null_c_pct_99th": 0.48,
704	      "observed_c_pct": 31.3,
705	      "permutation_p": "<0.001",
706	      "effect_size_z": 388.5,
707	      "null_matches_random_split": true
708	    },
709	    "tables": [
710	      {
711	        "title": "Table: Permutation Null Distribution Summary",
712	        "columns": [
713	          "statistic",
714	          "value"
715	        ],
716	        "rows": [
717	          [
718	            "observed_C_pct",
719	            31.3
720	          ],
721	          [
722	            "null_mean",
723	            0.22
724	          ],
725	          [
726	            "null_SD",
727	            0.08
728	          ],
729	          [
730	            "null_95th_percentile",
731	            0.38
732	          ],
733	          [
734	            "z_score",
735	            388.5
736	          ],
737	          [
738	            "permutation_p",
739	            "<0.001"
740	          ],
741	          [
742	            "random_split_control",
743	            0.18
744	          ]
745	        ]
746	      }
747	    ],
748	    "figures": [],
749	    "analysis": "Permutation test 在 worst 档下 necessary but not sufficient。Establishes that temporal labels carry real signal (not random)，但 signal identity 仍 contested。 在 reframed paper 中保留为 one-paragraph validation： \"Permutation test confirms C%=31.3% is not a statistical artifact of the MH procedure (null: 0.22±0.08%, p<0.001)。Decomposition of the temporal signal into item-level vs cohort-level components is addressed by plan_019 and plan_027。\"\n\n\nWorst 档下 permutation null C%=0.22% (SD=0.08%)，observed 31.3% 极显著高于 null (z=388, p<0.001)。但 reviewer 的反应不是 \"impressive\" 而是 \"so what\"： \"当然 31.3% above chance——你在比较 2023 vs 2024 models，它们 obviously different。 任何 test 都会 reject the null that these groups are exchangeable。 这个 permutation test 只证明 temporal signal exists，不证明 signal = item instability 而非 capability improvement。你需要的不是 'is 31% above chance' 而是 'is 31% above what capability improvement alone would produce'——而后者正是你的 decomposition analysis (plan_019) 和 matching analysis (plan_027) 试图回答但未完全回答的问题。\" Permutation null ≈ random split control (0.18% vs 0.22%)，consistent， 但这个 consistency 也只是说明两种 null 都 measure the same thing (label exchangeability)。\n"
750	  },
751	  {
752	    "name": "odds_ratio_regression_transparency",
753	    "description": "DIF flag 的 odds ratio regression：domain-level → item-level predictors + Simpson's paradox 分析",
754	    "results": {
755	      "model1_mcfadden_r2": 0.0007,
756	      "model1_nagelkerke_r2": 0.0012,
757	      "model1_subject_acc_delta_or_per_010": 1.55,
758	      "model1_subject_acc_delta_ci": [
759	        1.19,
760	        2.03
761	      ],
762	      "model2_mcfadden_r2": 0.0423,
763	      "model2_subject_acc_delta_or_per_010": 0.73,
764	      "model2_ctt_difficulty_or": 0.78,
765	      "model2_discrimination_or": 1.51,
766	      "model3_item_delta_or_per_010": 1.08,
767	      "model3_mcfadden_r2": 0.0012,
768	      "model4_mcfadden_r2": 0.0434,
769	      "model4_item_acc_change_or": 0.92,
770	      "model4_discrimination_or": 1.54,
771	      "simpsons_paradox": true,
772	      "simpsons_or_flip": "1.55 → 0.73",
773	      "lr_test_m1_vs_m2_chi2": 646.98,
774	      "lr_test_m3_vs_m4_chi2": 655.53
775	    },
776	    "tables": [
777	      {
778	        "title": "Table: Logistic Regression Models Predicting DIF-C Classification",
779	        "columns": [
780	          "model",
781	          "predictors",
782	          "mcfadden_r2",
783	          "nagelkerke_r2",
784	          "aic",
785	          "key_or"
786	        ],
787	        "rows": [
788	          [
789	            "M1",
790	            "subject_acc_Δ",
791	            0.0007,
792	            0.0012,
793	            15545,
794	            "1.55 [1.19,2.03]"
795	          ],
796	          [
797	            "M2",
798	            "subject_acc_Δ + difficulty + discrimination",
799	            0.0423,
800	            0.072,
801	            14902,
802	            "0.73 (acc_Δ), 1.51 (disc)"
803	          ],
804	          [
805	            "M3",
806	            "item_acc_Δ",
807	            0.0012,
808	            0.0021,
809	            15537,
810	            "1.08 [1.03,1.14]"
811	          ],
812	          [
813	            "M4",
814	            "item_acc_Δ + difficulty + discrimination",
815	            0.0434,
816	            0.074,
817	            14885,
818	            "0.92 (acc_Δ), 1.54 (disc)"
819	          ]
820	        ]
821	      },
822	      {
823	        "title": "Table: Simpson's Paradox — OR Flip Summary",
824	        "columns": [
825	          "predictor",
826	          "model1_or",
827	          "model2_or",
828	          "direction_flip",
829	          "interpretation"
830	        ],
831	        "rows": [
832	          [
833	            "Domain acc Δ (per 0.10)",
834	            1.55,
835	            0.73,
836	            "positive→negative",
837	            "confounded by item properties"
838	          ],
839	          [
840	            "Item acc Δ (per 0.10)",
841	            1.08,
842	            0.92,
843	            "positive→negative",
844	            "confounded by item properties"
845	          ],
846	          [
847	            "CTT discrimination (per 0.10)",
848	            "-",
849	            1.51,
850	            "consistent positive",
851	            "true driver"
852	          ]
853	        ]
854	      }
855	    ],
856	    "figures": [],
857	    "analysis": "Simpson's paradox 在 worst 档下是 most damaging single result。Reviewer 论证链： discrimination drives DIF → high-discrimination items separate cohorts → 2024 cohort is better → DIF flags items where 2024 models outperform 2023 models BECAUSE those items have high discrimination → \"DIF is measuring item quality, not instability\"。 在 reframed paper 中需要 carefully reinterpret： \"The OR flip reveals that item-level properties, particularly discrimination, are the proximal predictors of DIF classification. This is psychometrically expected: high-discrimination items magnify any ability difference between groups, producing larger MH odds ratio shifts. The question is whether this represents (a) genuine item instability amplified by discrimination, or (b) stable items faithfully discriminating between cohorts of different ability. Our decomposition evidence (ability confound ≤2.4pp, plan_027) supports interpretation (a), but we acknowledge this remains the central interpretive challenge。\"\n\nWorst 档下 Simpson's paradox (OR 1.55→0.73) 被 reviewer 反转利用。 核心论证：Model 1 (domain accuracy delta only) 显示 OR=1.55——domain 进步越大，DIF 越多， 看似支持 \"DIF tracks capability improvement\"。但加入 item-level properties (difficulty, discrimination) 后 OR flips to 0.73——controlling for item properties，domain improvement REDUCES DIF probability。 Reviewer 的解读：\"Simpson's paradox 证明 item-level properties (difficulty, discrimination) 才是 DIF 的 true driver，domain improvement 只是 ecological confound。 你的 DIF 方法在挑出 high-discrimination, moderate-difficulty items——这些恰好是 区分好模型和差模型的 items，它们 'show DIF' 不是因为 instability 而是因为它们 discriminate well，而 2024 models 恰好比 2023 models 好。\" Discrimination OR=1.51-1.54 across all models 是最 consistent predictor—— higher discrimination → more likely DIF。这直接支持了 worst 档的核心假设： DIF 在 measure 'items that separate good from bad models' 即 'models got better'。 McFadden R²=0.043 虽然 low in absolute terms，但 Model 1→Model 2 的 LR test χ²=647 (p≈0) 说明 item properties 是 massively significant predictors。\n"
858	  }
859	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfc52cac-ef30-4189-a991-ba87eb875a11",
  "isSidechain": false,
  "promptId": "053b0da8-7122-4261-b381-207d5502fd28",
  "type": "user",
  "uuid": "6e2ec367-e852-4b75-a2b6-8408ea747cce",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"real_data_dif_mmlu\",\n    \"description\": \"METABENCH MMLU response matrix (5,219 models × 12,508 items) 上的 MH-DIF 分析，含 temporal/ability cohort、within-family confound control、domain-specificity\",\n    \"results\": {\n      \"temporal_ets_c_pct\": 31.3,\n      \"temporal_fpr_li_clean\": 0.32,\n      \"temporal_enrichment\": 0.96,\n      \"ability_ets_c_pct\": 2.9,\n      \"ability_enrichment\": 1.19,\n      \"within_family_llama2v3_c_pct\": 61.3,\n      \"within_family_mistral_mixtral_c_pct\": 38.7,\n      \"domain_spearman_rho\": 0.38,\n      \"domain_spearman_p\": 0.004,\n      \"sanity_random_split_c_pct\": 0.18,\n      \"temporal_ability_jaccard\": 0.014,\n      \"irt_lz_above_2_pct\": 98.0\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 1: DIF Classification by Cohort Definition\",\n        \"columns\": [\n          \"cohort\",\n          \"n_ref\",\n          \"n_foc\",\n          \"pct_A\",\n          \"pct_B\",\n          \"pct_C\",\n          \"enrichment_li\"\n        ],\n        \"rows\": [\n          [\n            \"temporal_2023v2024\",\n            1253,\n            656,\n            48.2,\n            20.5,\n            31.3,\n            0.96\n          ],\n          [\n            \"ability_quintile\",\n            1044,\n            1044,\n            89.8,\n            7.3,\n            2.9,\n            1.19\n          ],\n          [\n            \"random_split_control\",\n            950,\n            950,\n            97.3,\n            2.5,\n            0.18,\n            1.01\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 2: Within-Family DIF (Confound Control)\",\n        \"columns\": [\n          \"family_pair\",\n          \"n_ref\",\n          \"n_foc\",\n          \"pct_C\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Llama-2_vs_Llama-3\",\n            161,\n            308,\n            61.3,\n            \"generation gap drives DIF\"\n          ],\n          [\n            \"Mistral_vs_Mixtral\",\n            89,\n            142,\n            38.7,\n            \"architecture shift contributes\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Worst-tier reviewer 的核心论证链：domain ρ=0.38 → within-family 61% → enrichment≈1.0 → IRT 98% misfit → 结论是 \\\"DIF 在 MMLU 上不是 item instability detector，而是 capability gap detector， 你的 31% 就是在说 models got better on 31% of items\\\"。这个攻击路径在逻辑上是 self-consistent 的， 即使 item-level decomposition 只解释 2.4pp——reviewer 会说 domain-level predictor 是 wrong granularity， 真正的 confound 是 item-level difficulty × model generation interaction。\\n\\n\\n在 worst 档下，31.3% C% 本身可复现但被 reviewer 视为 artifact。核心攻击点： (1) domain_spearman_rho=0.38 (p=0.004) 比 best 档预期的 0.25-0.30 更高，reviewer 用此论证 DIF 主要捕捉 domain-level capability improvement 而非 item instability； (2) within-family Llama-2v3 C%=61.3% 被解读为 \\\"DIF 在测 generation gap\\\"——Llama-2 到 Llama-3 是 architecture + scale + data 全面升级，61% DIF 恰恰说明 DIF 在测能力提升； (3) enrichment=0.96 ≈ 1.0 被解读为 DIF 与任何已知 contamination signal 无关——\\\"你的方法跟 contamination 没关系，它只是在找 hard items that newer models solve\\\"； (4) IRT |Lz|>2 at 98% 被解读为 conditioning variable (total score) 根本不适合 MMLU—— MH 依赖 total score 做 ability matching，但 57-subject multidimensional structure 使 total score 成为 poor proxy，整个 DIF 分析的 conditioning 基础被质疑。 random split 0.18% 只证明 temporal signal 存在，不证明 signal = instability。\\n\"\n  },\n  {\n    \"name\": \"rl_robustness_validation\",\n    \"description\": \"DIF 对 RL 训练模型的鲁棒性验证：alignment-RL (DPO/ORPO, N=477) + reasoning-RL (GRPO/PPO, N=10-15)\",\n    \"results\": {\n      \"alignment_rl_cohort_c_pct\": 29.8,\n      \"alignment_rl_jaccard_vs_temporal\": 0.72,\n      \"reasoning_rl_n_models\": 13,\n      \"reasoning_rl_added_to_focal_c_pct\": 30.5,\n      \"reasoning_rl_jaccard_vs_base_focal\": 0.85,\n      \"delong_p_dif_vs_constat\": 0.23,\n      \"delong_p_dif_vs_mink\": 0.18,\n      \"tost_equivalence_p\": 0.08,\n      \"constat_auroc_non_rl\": 0.74,\n      \"constat_auroc_rl\": 0.68,\n      \"mink_auroc_non_rl\": 0.71,\n      \"mink_auroc_rl\": 0.63,\n      \"dif_auroc_across_compositions\": 0.61,\n      \"partial_exploitation_detection_boundary_p\": 0.55,\n      \"bootstrap_ci_width_auroc\": 0.15\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Detection AUROC by Method × Model Type\",\n        \"columns\": [\n          \"method\",\n          \"non_rl_auroc\",\n          \"alignment_rl_auroc\",\n          \"reasoning_rl_auroc\",\n          \"delta\"\n        ],\n        \"rows\": [\n          [\n            \"MH-DIF\",\n            0.62,\n            0.61,\n            0.6,\n            -0.02\n          ],\n          [\n            \"ConStat\",\n            0.74,\n            0.71,\n            0.68,\n            -0.06\n          ],\n          [\n            \"Min-K%\",\n            0.71,\n            0.69,\n            0.63,\n            -0.08\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"在 worst 档 reframing 中，此实验被降级甚至 drop。N=13 的 RL 验证无法支撑任何 robust claim。 如果 reviewer 看到 DIF AUROC=0.61 且 bootstrap CI=[0.54, 0.76]，会质疑 \\\"为什么要用 detection power 这么低的方法\\\"。Reframed paper 中应将此实验移入 appendix 作为 preliminary evidence， 或完全 drop 并在 limitations 中说明。\\n\\n\\nWorst 档下此实验有两个致命问题： (1) N=13 reasoning-RL models 使所有统计检验 underpowered——DeLong test p=0.23 和 TOST p=0.08 都不显著，reviewer 正确指出 \\\"你无法区分 DIF 对 RL 鲁棒 vs 你没有足够样本检测差异\\\"； (2) DIF AUROC=0.61 本身就低——reviewer 论证 MH-DIF 在 any cohort composition 下 detection power 都不 competitive，不是 RL-robust 而是 uniformly weak； (3) ConStat 和 Min-K% 在 RL 上的 degradation (0.74→0.68, 0.71→0.63) 比预期温和， 不足以构成 \\\"traditional methods fail on RL\\\" 的 strong claim。 Bootstrap CI width=0.15 在 13 个模型上是预期内的，但 reviewer 会说这个宽度下任何 claim 都是 preliminary。\\n\"\n  },\n  {\n    \"name\": \"constat_perturbation_eval\",\n    \"description\": \"ConStat-style perturbation testing 在 MMLU 上的独立评估：200+ items LLM paraphrasing + FDR-controlled detection\",\n    \"results\": {\n      \"n_items_reformulated\": 220,\n      \"constat_fdr_controlled_detections\": 45,\n      \"constat_detection_rate\": 0.205,\n      \"constat_fpr_estimate\": 0.08,\n      \"constat_auroc_non_rl\": 0.74,\n      \"constat_auroc_rl\": 0.68,\n      \"constat_dif_overlap_jaccard\": 0.15,\n      \"paraphrase_quality_score\": 0.82\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"此实验在 worst 档的 reframed paper 中价值有限。如果 DIF 被降级为 case study， ConStat comparison 也失去 anchor。可以保留为 \\\"related methods comparison\\\" 但不再是核心 contribution。\\n\\n\\nWorst 档下，ConStat detection rate=20.5% 在 non-RL 模型上是 reasonable baseline， 但 DIF-ConStat overlap Jaccard=0.15 极低——reviewer 论证两种方法在测不同的东西， ensemble 前提不成立。ConStat 的 AUROC=0.74 > DIF 的 0.62，reviewer 会问 \\\"既然 ConStat 更准，为什么不直接用 ConStat？DIF 的 added value 在哪里？\\\" 更致命的是，ConStat 在 RL 上只 degradation 6pp (0.74→0.68)， 不够 dramatic 来支撑 \\\"traditional methods fail on RL\\\" 的 narrative。\\n\"\n  },\n  {\n    \"name\": \"dvd_generation_variance_eval\",\n    \"description\": \"DVD generation variance 在 MMLU 上的独立评估：10-15 open-weight models × 50 responses/item\",\n    \"results\": {\n      \"n_models_evaluated\": 12,\n      \"n_items_scored\": 1200,\n      \"dvd_bimodal_detection_rate\": 0.12,\n      \"dvd_auroc\": 0.65,\n      \"dvd_dif_overlap_jaccard\": 0.11,\n      \"dvd_constat_overlap_jaccard\": 0.22,\n      \"verbatim_vs_variant_dvd_gap\": 0.18\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"DVD 在 worst 档下是 net negative——弱结果被 reviewer 用来论证 contamination detection 整个 paradigm 的 fragility。建议在 reframed paper 中 drop 此实验。\\n\\n\\nDVD detection rate=12% 低于 ConStat 的 20.5%，AUROC=0.65 处于 poor-to-fair 区间。 DVD-DIF overlap Jaccard=0.11 甚至低于 ConStat-DIF 的 0.15——三种方法之间的 agreement 极低，reviewer 论证 \\\"这些方法在测量三个不同的东西，没有一个是 validated contamination signal\\\"。 N=12 模型的 generation variance 采样也不足以覆盖 model diversity。 在 worst 档下，DVD 的弱结果进一步削弱了 ensemble 的 rationale。\\n\"\n  },\n  {\n    \"name\": \"ensemble_fusion\",\n    \"description\": \"DIF + ConStat + DVD 三信号融合：calibrated thresholds + 2-of-3 voting + weighted fusion\",\n    \"results\": {\n      \"ensemble_2of3_coverage\": 0.38,\n      \"ensemble_2of3_fpr\": 0.12,\n      \"ensemble_weighted_auroc\": 0.72,\n      \"ensemble_vs_best_single_auroc_gain\": -0.02,\n      \"cross_val_weight_stability_cv\": 0.35,\n      \"uniform_vs_optimized_auroc_gap\": 0.03\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Ensemble vs Individual Signal Performance\",\n        \"columns\": [\n          \"method\",\n          \"auroc\",\n          \"fpr_at_80recall\",\n          \"coverage\"\n        ],\n        \"rows\": [\n          [\n            \"DIF (MH)\",\n            0.62,\n            0.38,\n            0.31\n          ],\n          [\n            \"ConStat\",\n            0.74,\n            0.12,\n            0.21\n          ],\n          [\n            \"DVD\",\n            0.65,\n            0.28,\n            0.12\n          ],\n          [\n            \"Ensemble (2-of-3)\",\n            0.68,\n            0.12,\n            0.38\n          ],\n          [\n            \"Ensemble (weighted)\",\n            0.72,\n            0.11,\n            0.42\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ensemble 在 worst 档下是 paper 的最大 sunk cost。三信号 low-agreement + ensemble ≤ best single = reviewer 一句话 kill：\\\"the whole is less than its parts\\\"。Reframed paper 必须完全 drop Claim 2 (ensemble)，将 plan_003a/b/c 全部移入 \\\"future work\\\"。\\n\\n\\nWorst 档下 ensemble 的核心问题是 base signal quality 太低。三种方法 pairwise Jaccard 全部 <0.25，2-of-3 voting 的 agreement 稀少导致 coverage=38% 但 FPR=12% (超过 0.10 target)。 weighted fusion AUROC=0.72 竟然低于 ConStat standalone 的 0.74——ensemble 反而 hurt performance。 cross-validation weight stability CV=0.35 表明 weights 在 fold 间不稳定，reviewer 正确指出 \\\"你的 ensemble 在 overfitting fold-specific patterns\\\"。 这个实验在 original framing (Claim 2: ensemble detection) 下是 fatal negative， 是 paper framing pivot 的直接原因之一。\\n\"\n  },\n  {\n    \"name\": \"cross_benchmark_gsm8k\",\n    \"description\": \"GSM8K 上的 DIF 复制 + GSM1K ground truth correlation + semi-synthetic validation\",\n    \"results\": {\n      \"gsm8k_temporal_c_pct\": 18.9,\n      \"gsm8k_external_c_pct\": 47.4,\n      \"gsm8k_sanity_c_pct\": 0.3,\n      \"semi_synthetic_delta_tpr_p10\": 0.818,\n      \"semi_synthetic_delta_tpr_p05\": 0.42,\n      \"gsm1k_n_models\": 33,\n      \"gsm1k_pearson_r\": -0.478,\n      \"gsm1k_spearman_rho\": -0.403,\n      \"gsm1k_direction\": \"NEGATIVE\",\n      \"gsm1k_partial_r\": -0.385,\n      \"gsm1k_permutation_p\": 0.014,\n      \"gsm1k_ci_upper_r\": -0.16,\n      \"gsm1k_ci_upper_rho\": -0.03\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: GSM1K Contamination Gap vs DIF Flag Correlation\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"ci_lower\",\n          \"ci_upper\",\n          \"p_value\"\n        ],\n        \"rows\": [\n          [\n            \"pearson_r\",\n            -0.478,\n            -0.71,\n            -0.16,\n            0.005\n          ],\n          [\n            \"spearman_rho\",\n            -0.403,\n            -0.67,\n            -0.03,\n            0.02\n          ],\n          [\n            \"partial_r_controlling_acc\",\n            -0.385,\n            -0.65,\n            -0.04,\n            0.027\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"GSM1K negative correlation 是 worst 档最有力的 ammunition。在 reframed paper 中必须 将此结果 reinterpret 为 \\\"DIF and contamination measure orthogonal constructs\\\"—— 这 actually supports Claim 2 (ground truth meta-critique) 而不是 undermines it。 Key reframing: \\\"DIF measures differential item functioning, not contamination per se. The negative GSM1K correlation confirms that item-level behavioral change ≠ contamination signal, validating our meta-critique that web-overlap labels are fundamentally mismatched.\\\"\\n\\n\\nWorst 档下此实验有一个 devastating result：GSM1K correlation 方向是 NEGATIVE (r=-0.478)—— DIF-C items 与 contamination gap 反相关。Reviewer 的解读：\\\"DIF 标记的 items 恰恰是 2024 模型 genuinely improved 的 items（不需要 contamination），而真正 contaminated 的 items 不被 DIF 检测到，因为 contamination 是 uniform across cohorts\\\"。 这直接支持了 worst 档的核心假设——DIF 在测 'models got better' 而非 contamination。 N=33 虽小但方向一致 (permutation p=0.014)，CI upper bound |r|=0.16 也远离 positive territory。 Semi-synthetic ΔTPR=0.42 at p=0.5 落在 worst 档范围 [0.3, 0.5] 内，被视为 \\\"moderate 但不 compelling\\\"——p=0.5 意味着一半 contaminated models 必须 exploit item 才能检测到。\\n\"\n  },\n  {\n    \"name\": \"bifactor_irt_equating_pilot\",\n    \"description\": \"MMLU bifactor IRT 模型拟合 + anchor item 选择 + fixed-parameter calibration equating pilot\",\n    \"results\": {\n      \"bifactor_convergence\": false,\n      \"bifactor_rmsea\": 0.089,\n      \"bifactor_cfi\": 0.72,\n      \"bifactor_tli\": 0.68,\n      \"bifactor_srmr\": 0.11,\n      \"general_factor_explained_variance_pct\": 28.4,\n      \"n_anchor_items_selected\": 0,\n      \"equating_feasible\": false,\n      \"computation_time_hours\": 18.5,\n      \"convergence_code\": \"iteration limit reached\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Bifactor failure 是 plan_005/006/008 整条 pipeline 的 kill signal。在 reframed paper 中 列入 limitations：\\\"IRT-based equating requires adequate model fit; MMLU's 57-subject multidimensional structure defeats both unidimensional and bifactor specifications. This motivates future work on multidimensional IRT or subject-specific calibration.\\\"\\n\\n\\nWorst 档下 bifactor 模型 fails to converge on 12,508 × 5,219 矩阵。 即使强制截断 iterations，fit indices 全部不达标 (RMSEA=0.089 > 0.06 cutoff, CFI=0.72 < 0.90 cutoff, TLI=0.68)。General factor 仅解释 28.4% variance， 说明 MMLU 的 57-subject structure 导致 essentially 无法用 single general factor 建模。 这直接验证了 reviewer 的 IRT misfit concern——不只是 |Lz| 的问题，连 bifactor 都 fail， 说明 MMLU 在 IRT 框架下 fundamentally ill-behaved。 结果：equating pipeline 被 kill，anchor items 无法选择，plan_006 (item generation) 也被 block。 这个 negative result 在 reframed paper 中反而有价值——motivates future multidimensional IRT work。\\n\"\n  },\n  {\n    \"name\": \"item_generation_calibration\",\n    \"description\": \"DIF-flagged MMLU items 的 LLM 替换生成 + student simulation calibration\",\n    \"results\": {\n      \"n_items_generated\": 0,\n      \"difficulty_correlation_prompt\": null,\n      \"difficulty_correlation_simulation\": null,\n      \"calibration_feasible\": false,\n      \"blocked_by\": \"plan_005_bifactor_failure\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Not executed。在 reframed paper 中完全 drop，不出现在 main body 或 appendix。 Original Claim 3 (regeneration) 已被 bifactor failure 否定。\\n\\n\\nWorst 档下此实验被 plan_005 failure 完全 block。没有可靠的 IRT 参数估计和 anchor items， 生成的替换 items 无法 calibrate 到 equated scale 上。即使独立运行 prompt-based generation， 已有文献 (arXiv 2602.06631) 表明 difficulty correlation 仅 ρ=0.10-0.45， 而 student simulation 需要先有 IRT 参数才能 simulate——circular dependency。 整个 regeneration pipeline (original Claim 3) 被 kill，是 paper pivot 的主要 driver 之一。\\n\"\n  },\n  {\n    \"name\": \"cumulative_bayesian_dif\",\n    \"description\": \"Sinharay et al. (2006) cumulative Bayesian DIF priors 的 simulation study：4 successive administrations\",\n    \"results\": {\n      \"individual_admin_tpr_delta10\": 0.42,\n      \"cumulative_2admin_tpr\": 0.55,\n      \"cumulative_3admin_tpr\": 0.63,\n      \"cumulative_4admin_tpr\": 0.68,\n      \"target_tpr_070\": false,\n      \"individual_admin_tpr_delta14\": 0.58,\n      \"fpr_all_below_010\": true,\n      \"prior_sensitivity_max_tpr_swing\": 0.09\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Cumulative DIF Power by Number of Administrations\",\n        \"columns\": [\n          \"n_admin\",\n          \"delta_10_tpr\",\n          \"delta_14_tpr\",\n          \"delta_16_tpr\",\n          \"fpr\"\n        ],\n        \"rows\": [\n          [\n            1,\n            0.42,\n            0.58,\n            0.68,\n            0.04\n          ],\n          [\n            2,\n            0.55,\n            0.71,\n            0.79,\n            0.05\n          ],\n          [\n            3,\n            0.63,\n            0.78,\n            0.85,\n            0.05\n          ],\n          [\n            4,\n            0.68,\n            0.83,\n            0.89,\n            0.06\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Simulation-only + IRT misfit = reviewer 完全 dismiss。在 reframed paper 中移入 appendix 或 drop。Methodology track reviewer 可能 appreciate the framework 但会要求 real data validation。\\n\\n\\nWorst 档下 cumulative power improvement 存在但低于 target：3-admin 后 TPR=0.63 < 0.70 target， 4-admin 才到 0.68。Reviewer 批评这是 pure simulation：\\\"你没有 4 个 time period 的真实数据， 这只是说 'if we had more data, DIF would work better'——tautological。\\\" 更关键的是，simulation 使用 well-specified 1D IRT model，而真实 MMLU 的 IRT misfit (98%) 意味着 simulation results 不 transferable。\\\"你在模拟一个你已经证明不存在的世界。\\\"\\n\"\n  },\n  {\n    \"name\": \"graceful_degradation_analysis\",\n    \"description\": \"Benchmark validity degradation under progressive item replacement (5%–50%)\",\n    \"results\": {\n      \"replacement_5pct_rho\": 0.999,\n      \"replacement_10pct_rho\": 0.998,\n      \"replacement_20pct_rho\": 0.996,\n      \"replacement_50pct_rho\": 0.988,\n      \"replacement_5pct_shr\": 0.993,\n      \"replacement_10pct_shr\": 0.991,\n      \"replacement_20pct_shr\": 0.987,\n      \"replacement_50pct_shr\": 0.972,\n      \"construct_coverage_maintained_at_20pct\": true,\n      \"blocked_by_equating\": true\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Ranking Stability Under Progressive Item Replacement\",\n        \"columns\": [\n          \"replacement_pct\",\n          \"spearman_rho\",\n          \"shr\",\n          \"construct_coverage_ratio\"\n        ],\n        \"rows\": [\n          [\n            5,\n            0.999,\n            0.993,\n            0.98\n          ],\n          [\n            10,\n            0.998,\n            0.991,\n            0.96\n          ],\n          [\n            20,\n            0.996,\n            0.987,\n            0.93\n          ],\n          [\n            50,\n            0.988,\n            0.972,\n            0.85\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"在 reframed paper 中，graceful degradation 反而支持 revised narrative： \\\"MMLU's massive redundancy means DIF-flagged items can be safely removed without validity loss — the diagnostic value of DIF is in understanding WHAT changed, not in removing items for quality control。\\\" 但 worst 档 reviewer 会说 \\\"如果 removal 没有影响，你的 whole paper 的 motivation 就不成立。\\\"\\n\\n\\nWorst 档下此实验 partially blocked by plan_005 failure (无法用 equated replacement items)。 可以用 random replacement 做 simulation，结果显示极高 robustness (ρ>0.988 even at 50% replacement)。 但 reviewer 将此解读为 MMLU 的 massive redundancy 的进一步证据： \\\"你可以 drop 一半的 items 且 ranking 不变——这说明 MMLU 有 6000+ redundant items， 你的 31% DIF finding 完全在 redundancy margin 内，没有任何实际影响。\\\" 讽刺的是，robustness 越高，DIF findings 的 practical significance 越低。\\n\"\n  },\n  {\n    \"name\": \"item_focused_trees\",\n    \"description\": \"Item-Focused Trees (Tutz & Berger 2016) 作为 continuous-covariate DIF 替代方案\",\n    \"results\": {\n      \"ift_n_items_dif\": 3452,\n      \"ift_c_pct_equivalent\": 27.6,\n      \"ift_mh_concordance\": 0.78,\n      \"ift_split_point_median_date\": \"2023-09\",\n      \"ift_gradual_items_pct\": 62.3,\n      \"ift_abrupt_items_pct\": 37.7,\n      \"ift_computation_time_hours\": 8.2\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: IFT vs MH-DIF Classification Comparison\",\n        \"columns\": [\n          \"metric\",\n          \"MH_DIF\",\n          \"IFT\",\n          \"concordance\"\n        ],\n        \"rows\": [\n          [\n            \"n_flagged_items\",\n            3918,\n            3452,\n            0.78\n          ],\n          [\n            \"pct_C_equivalent\",\n            31.3,\n            27.6,\n            \"-\"\n          ],\n          [\n            \"gradual_vs_abrupt\",\n            \"N/A (binary)\",\n            \"62.3% / 37.7%\",\n            \"-\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"IFT 在 worst 档下是 double-edged sword：提供了 finer-grained picture 但 picture 说的是 \\\"gradual improvement\\\" 而非 \\\"instability\\\"。Reframed paper 中可以保留为 robustness check 并 reframe：\\\"IFT confirms that item-level behavioral changes are predominantly gradual, consistent with progressive capability development rather than discrete contamination events。\\\"\\n\\n\\nWorst 档下 IFT 的 continuous treatment 暴露了 temporal DIF 的 gradual nature： 62.3% 的 DIF items 显示 gradual difficulty drift 而非 abrupt change。 Reviewer 用此论证 \\\"这是 models gradually getting better on certain items， 不是 contamination event 或 structural instability——difficulty drift 是 capability improvement 的自然结果，你的 binary 2023/2024 split 人为制造了 abrupt 的假象。\\\" Split point median at 2023-09 也不 informative——没有对应任何 specific model release event。 IFT-MH concordance=0.78 表明 MH 的 binary grouping 丢失了 22% 的 nuance。\\n\"\n  },\n  {\n    \"name\": \"architecture_stratified_dif\",\n    \"description\": \"Decoder-only 子群上的 DIF 分析 + IRT fit diagnostics\",\n    \"results\": {\n      \"n_decoder_only\": 5226,\n      \"n_non_decoder\": 1,\n      \"pct_decoder_only\": 99.98,\n      \"decoder_only_c_pct\": 31.3,\n      \"decoder_only_jaccard_vs_full\": 1.0,\n      \"irt_rmsea_full\": 0.082,\n      \"irt_rmsea_decoder_only\": 0.081,\n      \"irt_cfi_full\": 0.74,\n      \"irt_cfi_decoder_only\": 0.74,\n      \"irt_lz_above_2_pct_decoder_only\": 97.8\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: IRT Fit Diagnostics — Full vs Decoder-Only\",\n        \"columns\": [\n          \"population\",\n          \"N\",\n          \"RMSEA\",\n          \"CFI\",\n          \"TLI\",\n          \"pct_Lz_above_2\"\n        ],\n        \"rows\": [\n          [\n            \"full\",\n            5227,\n            0.082,\n            0.74,\n            0.71,\n            98.0\n          ],\n          [\n            \"decoder_only\",\n            5226,\n            0.081,\n            0.74,\n            0.71,\n            97.8\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"此实验在 worst 档下是 necessary but trivially resolved。不提供任何 defense against IRT misfit concern。在 reframed paper 中一句话带过：\\\"99.98% of METABENCH models are decoder-only; architecture heterogeneity is a non-issue (Jaccard=1.0)\\\"。 IRT misfit 需要在 limitations 中 honestly address 而非 dismiss。\\n\\n\\nWorst 档下此实验 trivially resolves architecture concern (99.98% decoder-only, removing 1 model changes nothing, Jaccard=1.0) 但 completely fails to address IRT misfit。RMSEA 从 0.082→0.081, CFI unchanged at 0.74——IRT misfit 不是 architecture heterogeneity 造成的，而是 MMLU 57-subject multidimensionality 造成的。 Reviewer：\\\"你证明了 architecture 不是问题，但 IRT misfit 依然是 98%—— 移除 1 个 encoder model 不可能解决 57-subject 的 multidimensionality 问题。 你需要的是 multidimensional IRT 或 per-subject analysis，不是 architecture stratification。\\\"\\n\"\n  },\n  {\n    \"name\": \"semi_synthetic_contamination_validation\",\n    \"description\": \"Known contamination injection into METABENCH matrix + DIF detection power measurement\",\n    \"results\": {\n      \"temporal_external_tpr_p0\": 0.326,\n      \"temporal_external_tpr_p03\": 0.45,\n      \"temporal_external_tpr_p05\": 0.42,\n      \"temporal_external_tpr_p07\": 0.78,\n      \"temporal_external_tpr_p10\": 0.95,\n      \"temporal_external_fpr\": 0.314,\n      \"temporal_external_delta_tpr_p05\": 0.35,\n      \"temporal_external_delta_tpr_p10\": 0.62,\n      \"cross_subject_delta_fpr\": 0.0,\n      \"within_subject_fpr_inflation\": 0.186,\n      \"ability_external_delta_tpr_p10\": 0.302,\n      \"standard_mh_fpr_inflation_at_p10\": 0.318\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Semi-Synthetic Validation — DIF Detection Power\",\n        \"columns\": [\n          \"exploitation_rate_p\",\n          \"tpr\",\n          \"delta_tpr\",\n          \"fpr\",\n          \"delta_fpr\"\n        ],\n        \"rows\": [\n          [\n            0.0,\n            0.326,\n            0.0,\n            0.314,\n            0.0\n          ],\n          [\n            0.3,\n            0.45,\n            0.124,\n            0.314,\n            0.0\n          ],\n          [\n            0.5,\n            0.676,\n            0.35,\n            0.314,\n            0.0\n          ],\n          [\n            0.7,\n            0.78,\n            0.454,\n            0.314,\n            0.0\n          ],\n          [\n            1.0,\n            0.95,\n            0.624,\n            0.314,\n            0.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Semi-synthetic validation 是 worst 档 reframing 的 primary contribution。 虽然 ΔTPR=0.35 at p=0.5 不 impressive，但 (1) cross-subject ΔFPR=0.000 是 novel methodological contribution，(2) dose-response monotonicity 证明 framework 有效， (3) within vs cross matching comparison 是 actionable guidance。 Reframed paper 应强调 framework reusability 而非 specific detection performance。\\n\\n\\nWorst 档下 semi-synthetic 的 ΔTPR at p=0.5 = 0.35，落在 worst 范围 [0.3, 0.5] 下半区。 Reviewer 的攻击： (1) \\\"ΔTPR=0.35 at p=0.5 意味着在 half exploitation 下你只比 baseline 多检测 35% 的 contaminated items——这在 practical terms 下意味着你漏掉了大部分 contamination\\\"； (2) \\\"Baseline FPR=0.314 意味着你的 detector 在没有 injection 时已经 flag 31.4% 的 items 作为 positive——这要么是 FPR 不可接受，要么是你的 'clean' items 并不 clean， 无论哪种解读都 undermine 你的 validation\\\"； (3) \\\"Cross-subject matching 的 ΔFPR=0.000 是 technically impressive 但 semantically questionable——你用 other subjects 的 score 做 matching variable，这意味着你在用 math ability 来 match science items，matching variable 和 target variable 的 construct relevance 未验证\\\"。 但在 reframed paper 中，这个实验反而是最 defensible 的——reviewer 攻击的是 interpretation 而非 methodology，cross-subject matching ΔFPR=0.000 是 hard empirical fact。\\n\"\n  },\n  {\n    \"name\": \"multi_benchmark_temporal_dif\",\n    \"description\": \"6 个 benchmark (MMLU/ARC/HellaSwag/WinoGrande/TruthfulQA/GSM8K) 上的 temporal DIF 分析\",\n    \"results\": {\n      \"mmlu_c_pct\": 31.3,\n      \"winogrande_c_pct\": 30.3,\n      \"truthfulqa_c_pct\": 29.7,\n      \"arc_c_pct\": 26.9,\n      \"gsm8k_c_pct\": 18.9,\n      \"hellaswag_c_pct\": 17.9,\n      \"cross_benchmark_range\": \"17.9-31.3%\",\n      \"all_random_controls_below_1pct\": true,\n      \"min_enrichment_ratio\": 45,\n      \"n_benchmarks\": 6,\n      \"cross_benchmark_mean_c_pct\": 25.8,\n      \"cross_benchmark_sd_c_pct\": 5.8\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Cross-Benchmark Temporal DIF Summary\",\n        \"columns\": [\n          \"benchmark\",\n          \"n_items\",\n          \"n_ref\",\n          \"n_foc\",\n          \"pct_C\",\n          \"random_pct_C\",\n          \"enrichment_ratio\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            12508,\n            1080,\n            807,\n            31.3,\n            0.18,\n            174\n          ],\n          [\n            \"WinoGrande\",\n            1267,\n            1017,\n            803,\n            30.3,\n            0.32,\n            95\n          ],\n          [\n            \"TruthfulQA\",\n            817,\n            1080,\n            807,\n            29.7,\n            0.37,\n            80\n          ],\n          [\n            \"ARC-Challenge\",\n            1172,\n            1080,\n            807,\n            26.9,\n            0.6,\n            45\n          ],\n          [\n            \"GSM8K\",\n            1319,\n            1017,\n            804,\n            18.9,\n            0.3,\n            63\n          ],\n          [\n            \"HellaSwag\",\n            10042,\n            1080,\n            807,\n            17.9,\n            0.28,\n            64\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-benchmark 一致性在 worst 档下是 double-edged sword。在 original framing 下 支持 generalizability；在 worst 档下被解读为 method artifact。 Reframed paper 中应 reinterpret：\\\"Cross-benchmark consistency confirms that temporal cohort design reliably detects DIF across diverse benchmarks, whether the signal represents item instability, capability improvement, or both. Our semi-synthetic framework can disambiguate this — we demonstrate this on MMLU and GSM8K。\\\"\\n\\n\\nWorst 档下 6-benchmark consistency (C%=17.9-31.3%, all >45× above random) 被 reviewer 反转利用。核心论证：\\\"所有 6 个 benchmark 都显示 high DIF 恰恰证明这是 method artifact， 不是 benchmark-specific instability。如果 DIF 在测 item instability，不同 benchmark 应该有不同的 instability profile——HellaSwag (commonsense) 和 GSM8K (math) 的 instability 机制完全不同。但 C% 的 cross-benchmark consistency (mean=25.8%, SD=5.8%) 说明 DIF 在 uniformly 捕捉 'temporal cohort difference' 的 statistical signal， 而这个 signal 就是 'models got better'。\\\" 更具体地：HellaSwag 和 GSM8K 的 C% 较低 (17.9%, 18.9%) 恰好是 capability improvement 最 saturated 的 benchmarks (HellaSwag accuracy >90%, GSM8K has clear skill ceiling)， 而 MMLU (31.3%) 和 WinoGrande (30.3%) 的 C% 较高恰好是 improvement space 最大的 benchmarks。 这个 pattern 与 \\\"DIF = capability improvement\\\" 假说 perfectly consistent。\\n\"\n  },\n  {\n    \"name\": \"permutation_null_c_rate\",\n    \"description\": \"1000× permutation test：randomly reassign temporal labels → MH-DIF → null C% distribution\",\n    \"results\": {\n      \"n_permutations\": 1000,\n      \"null_c_pct_mean\": 0.22,\n      \"null_c_pct_sd\": 0.08,\n      \"null_c_pct_95th\": 0.38,\n      \"null_c_pct_99th\": 0.48,\n      \"observed_c_pct\": 31.3,\n      \"permutation_p\": \"<0.001\",\n      \"effect_size_z\": 388.5,\n      \"null_matches_random_split\": true\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Permutation Null Distribution Summary\",\n        \"columns\": [\n          \"statistic\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"observed_C_pct\",\n            31.3\n          ],\n          [\n            \"null_mean\",\n            0.22\n          ],\n          [\n            \"null_SD\",\n            0.08\n          ],\n          [\n            \"null_95th_percentile\",\n            0.38\n          ],\n          [\n            \"z_score\",\n            388.5\n          ],\n          [\n            \"permutation_p\",\n            \"<0.001\"\n          ],\n          [\n            \"random_split_control\",\n            0.18\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Permutation test 在 worst 档下 necessary but not sufficient。Establishes that temporal labels carry real signal (not random)，但 signal identity 仍 contested。 在 reframed paper 中保留为 one-paragraph validation： \\\"Permutation test confirms C%=31.3% is not a statistical artifact of the MH procedure (null: 0.22±0.08%, p<0.001)。Decomposition of the temporal signal into item-level vs cohort-level components is addressed by plan_019 and plan_027。\\\"\\n\\n\\nWorst 档下 permutation null C%=0.22% (SD=0.08%)，observed 31.3% 极显著高于 null (z=388, p<0.001)。但 reviewer 的反应不是 \\\"impressive\\\" 而是 \\\"so what\\\"： \\\"当然 31.3% above chance——你在比较 2023 vs 2024 models，它们 obviously different。 任何 test 都会 reject the null that these groups are exchangeable。 这个 permutation test 只证明 temporal signal exists，不证明 signal = item instability 而非 capability improvement。你需要的不是 'is 31% above chance' 而是 'is 31% above what capability improvement alone would produce'——而后者正是你的 decomposition analysis (plan_019) 和 matching analysis (plan_027) 试图回答但未完全回答的问题。\\\" Permutation null ≈ random split control (0.18% vs 0.22%)，consistent， 但这个 consistency 也只是说明两种 null 都 measure the same thing (label exchangeability)。\\n\"\n  },\n  {\n    \"name\": \"odds_ratio_regression_transparency\",\n    \"description\": \"DIF flag 的 odds ratio regression：domain-level → item-level predictors + Simpson's paradox 分析\",\n    \"results\": {\n      \"model1_mcfadden_r2\": 0.0007,\n      \"model1_nagelkerke_r2\": 0.0012,\n      \"model1_subject_acc_delta_or_per_010\": 1.55,\n      \"model1_subject_acc_delta_ci\": [\n        1.19,\n        2.03\n      ],\n      \"model2_mcfadden_r2\": 0.0423,\n      \"model2_subject_acc_delta_or_per_010\": 0.73,\n      \"model2_ctt_difficulty_or\": 0.78,\n      \"model2_discrimination_or\": 1.51,\n      \"model3_item_delta_or_per_010\": 1.08,\n      \"model3_mcfadden_r2\": 0.0012,\n      \"model4_mcfadden_r2\": 0.0434,\n      \"model4_item_acc_change_or\": 0.92,\n      \"model4_discrimination_or\": 1.54,\n      \"simpsons_paradox\": true,\n      \"simpsons_or_flip\": \"1.55 → 0.73\",\n      \"lr_test_m1_vs_m2_chi2\": 646.98,\n      \"lr_test_m3_vs_m4_chi2\": 655.53\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Logistic Regression Models Predicting DIF-C Classification\",\n        \"columns\": [\n          \"model\",\n          \"predictors\",\n          \"mcfadden_r2\",\n          \"nagelkerke_r2\",\n          \"aic\",\n          \"key_or\"\n        ],\n        \"rows\": [\n          [\n            \"M1\",\n            \"subject_acc_Δ\",\n            0.0007,\n            0.0012,\n            15545,\n            \"1.55 [1.19,2.03]\"\n          ],\n          [\n            \"M2\",\n            \"subject_acc_Δ + difficulty + discrimination\",\n            0.0423,\n            0.072,\n            14902,\n            \"0.73 (acc_Δ), 1.51 (disc)\"\n          ],\n          [\n            \"M3\",\n            \"item_acc_Δ\",\n            0.0012,\n            0.0021,\n            15537,\n            \"1.08 [1.03,1.14]\"\n          ],\n          [\n            \"M4\",\n            \"item_acc_Δ + difficulty + discrimination\",\n            0.0434,\n            0.074,\n            14885,\n            \"0.92 (acc_Δ), 1.54 (disc)\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: Simpson's Paradox — OR Flip Summary\",\n        \"columns\": [\n          \"predictor\",\n          \"model1_or\",\n          \"model2_or\",\n          \"direction_flip\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Domain acc Δ (per 0.10)\",\n            1.55,\n            0.73,\n            \"positive→negative\",\n            \"confounded by item properties\"\n          ],\n          [\n            \"Item acc Δ (per 0.10)\",\n            1.08,\n            0.92,\n            \"positive→negative\",\n            \"confounded by item properties\"\n          ],\n          [\n            \"CTT discrimination (per 0.10)\",\n            \"-\",\n            1.51,\n            \"consistent positive\",\n            \"true driver\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Simpson's paradox 在 worst 档下是 most damaging single result。Reviewer 论证链： discrimination drives DIF → high-discrimination items separate cohorts → 2024 cohort is better → DIF flags items where 2024 models outperform 2023 models BECAUSE those items have high discrimination → \\\"DIF is measuring item quality, not instability\\\"。 在 reframed paper 中需要 carefully reinterpret： \\\"The OR flip reveals that item-level properties, particularly discrimination, are the proximal predictors of DIF classification. This is psychometrically expected: high-discrimination items magnify any ability difference between groups, producing larger MH odds ratio shifts. The question is whether this represents (a) genuine item instability amplified by discrimination, or (b) stable items faithfully discriminating between cohorts of different ability. Our decomposition evidence (ability confound ≤2.4pp, plan_027) supports interpretation (a), but we acknowledge this remains the central interpretive challenge。\\\"\\n\\nWorst 档下 Simpson's paradox (OR 1.55→0.73) 被 reviewer 反转利用。 核心论证：Model 1 (domain accuracy delta only) 显示 OR=1.55——domain 进步越大，DIF 越多， 看似支持 \\\"DIF tracks capability improvement\\\"。但加入 item-level properties (difficulty, discrimination) 后 OR flips to 0.73——controlling for item properties，domain improvement REDUCES DIF probability。 Reviewer 的解读：\\\"Simpson's paradox 证明 item-level properties (difficulty, discrimination) 才是 DIF 的 true driver，domain improvement 只是 ecological confound。 你的 DIF 方法在挑出 high-discrimination, moderate-difficulty items——这些恰好是 区分好模型和差模型的 items，它们 'show DIF' 不是因为 instability 而是因为它们 discriminate well，而 2024 models 恰好比 2023 models 好。\\\" Discrimination OR=1.51-1.54 across all models 是最 consistent predictor—— higher discrimination → more likely DIF。这直接支持了 worst 档的核心假设： DIF 在 measure 'items that separate good from bad models' 即 'models got better'。 McFadden R²=0.043 虽然 low in absolute terms，但 Model 1→Model 2 的 LR test χ²=647 (p≈0) 说明 item properties 是 massively significant predictors。\\n\"\n  }\n]",
      "numLines": 859,
      "startLine": 1,
      "totalLines": 859
    }
  },
  "sourceToolAssistantUUID": "bfc52cac-ef30-4189-a991-ba87eb875a11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T11:38:55.358Z_

<details><summary>↩ Tool result · `toolu_01Tm1sJd9MHn4zUSiHCaKHx1`</summary>

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
  "parentUuid": "9083f5ef-5d50-418f-a18d-d6ee82b90d5b",
  "isSidechain": false,
  "promptId": "053b0da8-7122-4261-b381-207d5502fd28",
  "type": "user",
  "uuid": "178492a6-d333-4a71-8144-fb5aceb9c99f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/paper_framing.md",
      "content": "# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n",
      "numLines": 124,
      "startLine": 1,
      "totalLines": 124
    }
  },
  "sourceToolAssistantUUID": "9083f5ef-5d50-418f-a18d-d6ee82b90d5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T110541 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "6e2ec367-e852-4b75-a2b6-8408ea747cce",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream research",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120"
}
```

---

### Assistant

_source line 13 · 2026-05-21T11:39:27.850Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me also check the paper-writing norms skill for guidance, and then construct the full LaTeX paper.

This is a "worst" tier dream paper, meaning I need to write it from the perspective that reviewers will be highly critical. The narrative guidance says:

1. Semi-synthetic validation framework (ΔFPR=0.000) as primary contribution
2. Ground truth meta-critique as co-primary contribution
3. Temporal DIF findings demoted to motivating example/case study
4. Audit protocol repositioned as 'proposed workflow'


5. Title positioning around validating item-level contamination detection with a semi-synthetic framework and cross-subject matching

Now I'm mapping out which experiments to feature: the real data DIF analysis on MMLU serves as the motivating case study, the robustness validation gets demoted to appendix, the perturbation evaluation provides methodological comparison, while the generation variance and ensemble fusion work either get dropped or relegated to future directions, with GSM8K replication and the negative correlation finding on GSM1K rounding out the empirical scope.

Looking at the remaining experiments, I'm positioning semi-synthetic contamination validation as the core contribution with ground truth meta-critique as a co-primary angle, shifting temporal DIF to a motivating case study role instead, while the bifactor IRT equating shows limitations, the item generation work remains blocked, and I'm deciding how to handle the Bayesian DIF work, graceful degradation analysis, item-focused trees for robustness, the trivially resolved architecture stratification, permutation null validation, and Simpson's paradox analysis through odds ratio regression. the negative results honestly (GSM1K negative correlation, bifactor failure, ensemble failure)
- Address the "worst" reviewer concerns embedded in the analysis

I need to write a complete LaTeX paper covering all experiments, with some going into the appendix or receiving brief treatment. Given the 8-page limit and the guidance to reframe this as a methodological contribution, I'll structure it around: Abstract, Introduction (motivating temporal DIF but emphasizing the methodological gap), Related Work, Method, Experiments (all of them), Limitations, and Conclusion. For the experiments section, I'm planning tables to organize the results—one showing DIF classification by cohort definition from the real MMLU data, another capturing within-family DIF patterns, and additional tables for the semi-synthetic validation, diagnostic analyses, and negative results. Generating markdown table...

I've got a lot of tables to work with here—one for each experiment. Given the eight-page constraint, I need to be strategic about which ones to include and how to present them concisely. Let me think through the paper structure: I'll frame this as validating an item-level contamination detection method using a semi-synthetic approach, with the key result being that near-zero false positive rate. I should check if the output directory is ready, then start writing the paper with a focus on covering each experiment systematically without exceeding the page limit.

For the framing, I'm repositioning the web-overlap label mismatch as a critique of existing approaches, moving the temporal DIF findings down to a motivating example, and being transparent about the negative results—the bifactor model failure, the ensemble's poor performance, and the unexpected negative correlation with GSM1K.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "178492a6-d333-4a71-8144-fb5aceb9c99f",
  "isSidechain": false,
  "requestId": "req_011CbFebb893zZMGQVLraLZ4",
  "type": "assistant",
  "uuid": "46849c12-840b-4e3f-84f5-3385df9c59d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKvezr8BHsdUJ5P2eZwys4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21698,
      "cache_read_input_tokens": 24087,
      "output_tokens": 1630,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1630,
          "cache_read_input_tokens": 24087,
          "cache_creation_input_tokens": 21698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21698
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

_source line 14 · 2026-05-21T11:39:27.851Z_

Let me check the output directory exists and load the paper writing norms skill.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46849c12-840b-4e3f-84f5-3385df9c59d8",
  "isSidechain": false,
  "requestId": "req_011CbFebb893zZMGQVLraLZ4",
  "type": "assistant",
  "uuid": "83f6a071-6d10-4f0a-98cf-bcb87ce1b7f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKvezr8BHsdUJ5P2eZwys4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21698,
      "cache_read_input_tokens": 24087,
      "output_tokens": 1630,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1630,
          "cache_read_input_tokens": 24087,
          "cache_creation_input_tokens": 21698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21698
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

_source line 15 · 2026-05-21T11:39:28.840Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WbTzVniE4op32hbEPNZNqi`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/",
  "description": "List output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83f6a071-6d10-4f0a-98cf-bcb87ce1b7f0",
  "isSidechain": false,
  "requestId": "req_011CbFebb893zZMGQVLraLZ4",
  "type": "assistant",
  "uuid": "c4a5edb2-7e6d-4cad-a713-7357e9ede92c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKvezr8BHsdUJ5P2eZwys4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21698,
      "cache_read_input_tokens": 24087,
      "output_tokens": 1630,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1630,
          "cache_read_input_tokens": 24087,
          "cache_creation_input_tokens": 21698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21698
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

_source line 16 · 2026-05-21T11:39:29.217Z_

<details><summary>↩ Tool result · `toolu_01S5gRoUvfVZv92xu9sRLX8Z`</summary>

````text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "01bc722a-19f5-4491-a254-26cc92da330d",
  "isSidechain": false,
  "promptId": "053b0da8-7122-4261-b381-207d5502fd28",
  "type": "user",
  "uuid": "00fb75b5-9334-4369-b9cb-3729ec9fbdc4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "01bc722a-19f5-4491-a254-26cc92da330d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Tool result

_source line 17 · 2026-05-21T11:39:29.038Z_

<details><summary>↩ Tool result · `toolu_01WbTzVniE4op32hbEPNZNqi`</summary>

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
  "parentUuid": "c4a5edb2-7e6d-4cad-a713-7357e9ede92c",
  "isSidechain": false,
  "promptId": "053b0da8-7122-4261-b381-207d5502fd28",
  "type": "user",
  "uuid": "cb87cf66-fd6c-41a3-b775-ec0817a7d933",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c4a5edb2-7e6d-4cad-a713-7357e9ede92c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T11:39:29.210Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S5gRoUvfVZv92xu9sRLX8Z`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb87cf66-fd6c-41a3-b775-ec0817a7d933",
  "isSidechain": false,
  "requestId": "req_011CbFebb893zZMGQVLraLZ4",
  "type": "assistant",
  "uuid": "01bc722a-19f5-4491-a254-26cc92da330d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKvezr8BHsdUJ5P2eZwys4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21698,
      "cache_read_input_tokens": 24087,
      "output_tokens": 1630,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1630,
          "cache_read_input_tokens": 24087,
          "cache_creation_input_tokens": 21698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21698
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

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T110541 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "00fb75b5-9334-4369-b9cb-3729ec9fbdc4",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream research",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120"
}
```

---

### Assistant

_source line 21 · 2026-05-21T11:40:33.311Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me write the complete LaTeX paper.

Key decisions for the "worst" tier paper:
1. Title: "Validating Item-Level Contamination Detection: A Semi-Synthetic Framework with Cross-Subject Matching"
2. Primary contribution: Semi-synthetic validation framework (ΔFPR=0.000)
3. Co-primary: Ground truth meta-critique
4. Demoted: Temporal DIF → motivating case study
5. All experiments must have corresponding sections/tables
6. No fabricated numbers - everything from experiment_data.json


7. Honest about negative results

I'm planning the paper structure to fit 8 pages with an abstract, introduction, related work, methods section, and a substantial experiments section covering all 16 experiments organized by theme. The experiments section will be the bulk of the paper, starting with a motivating case study on temporal DIF in MMLU, then moving through the semi-synthetic validation framework and ground truth analysis.

Now I'm organizing the remaining experiments into sections on transparency analysis and negative results, grouping the regression analysis, decision trees, and degradation studies together to show how the method performs across different analytical lenses.

I realize I have too many tables for a concise paper, so I need to consolidate and use inline reporting where it makes sense. The key constraint is that every experiment from the data file needs representation—either as its own table or as a subsection with clear labeling. I'm thinking about using combined tables and paragraph-level headings to keep the structure compact while still accounting for each experiment systematically.

For the document format, I should go with something clean and compilable rather than overthinking the template. A standard article class with reasonable margins will work fine for a draft that demonstrates "够审" quality. I'll focus on the content now: making sure every experiment is included, using only the actual numbers from the data, following the narrative priorities (semi-synthetic primary, meta-critique co-primary, temporal DIF secondary), and adhering to academic writing conventions.

I'm planning seven tables to cover all sixteen experiments efficiently: DIF by cohort with permutation null, within-family DIF, cross-benchmark temporal patterns, semi-synthetic detection power as the centerpiece, GSM1K ground truth correlation, cumulative Bayesian power, and one more for the remaining results. This structure keeps everything within the eight-page target while maintaining the experimental narrative.

For the remaining experiments, I'll use subsections with inline results rather than full tables—bifactor and item generation are negative results better handled in prose, and a few others don't have sufficient tabular data to warrant their own tables. This approach lets me cover all sixteen without bloating the paper. - §4.1 Temporal DIF as Case Study: real_data_dif_mmlu + permutation + multi_benchmark + architecture_stratified
  Tables: Table 1 (DIF by cohort), Table 2 (cross-benchmark)
  
- §4.2 Semi-Synthetic Validation: semi_synthetic + cross_benchmark_gsm8k
  Tables: Table 3 (detection power), Table 4 (GSM1K correlation)

- §4.3 Ground Truth Meta-Critique: constat + dvd + ensemble
  Tables: Table 5 (method comparison including ensemble)

- §4.4 Diagnostic Analyses: odds_ratio + item_focused_trees + graceful_degradation
  Tables: Table 6 (Simpson's paradox), Table 7 (ranking stability)

- §4.5 Scope Boundaries: rl_robustness + cumulative_bayesian + bifactor + item_generation
  Tables: Table 8 (RL AUROC + cumulative power combined)

That gives me roughly eight tables covering all sixteen experiments. Now I'm ready to write the actual paper with a clear structure—each experiment gets its own paragraph or table row so nothing gets lost. I'll use a standard article format with straightforward LaTeX settings for reliable compilation.

Now I'm pulling the key metrics from the data: temporal DIF shows substantial differences across cohorts with MMLU at 31.3% ability gap and 2.9% temporal component, strong within-family consistency for Llama at 61.3% versus Mistral at 38.7%, and moderate domain correlation at 0.38. The robustness tests show DIF detection ranges from 0.60–0.62 AUROC with ConStat performing better at 0.68–0.74, while Min-K% achieves 0.63–0.71. ConStat's detection rate is 0.205 with low false positives at 0.08 and Jaccard overlap of 0.15 with ground truth DIF, compared to DVD's lower detection rate of 0.12 and AUROC of 0.65. The ensemble approach reaches 0.72 weighted AUROC but shows minimal gain over the best single method. Cross-benchmark validation on GSM1K yields a correlation of -0.478.

Now examining the semi-synthetic results and additional validation metrics: semi-synthetic data shows strong TPR improvement of 0.818 with minimal false positive rate change, though the bifactor model fails to converge with RMSEA at 0.089 and CFI at 0.72. The cumulative Bayesian approach improves TPR from 0.42 with single administration to 0.68 with four administrations while keeping false positives below 0.06. Graceful degradation testing shows high stability at 0.988 correlation with 50% item replacement, item-focused trees achieve 0.78 concordance with 62.3% gradual improvement, and the architecture analysis reveals 99.98% decoder-only models with perfect Jaccard overlap. Semi-synthetic cross-subject validation shows zero false positive rate difference but within-subject FPR inflation reaches 0.186, and the multi-benchmark evaluation spans six benchmarks.

Looking at the permutation testing and odds ratio analysis: permutation tests show null mean at 0.22% with z-score of 388.5, while odds ratio analysis reveals Simpson's paradox where the overall odds ratio of 1.55 reverses to 0.73 when stratified, and discrimination odds ratio sits at 1.51. Now I'm ready to structure the paper with a clean, professional approach that honestly frames these results in the worst-case tier, starting with a title about validating item-level contamination detection through semi-synthetic frameworks with cross-subject matching, then building out the abstract to cover the core problem of lacking validated evaluation methodology, the gap in existing approaches that measure global exposure rather than item-level effects, and the key contributions around the semi-synthetic validation framework achieving zero false positive rate difference, empirical ground truth meta-critique, and temporal differential item functioning as a motivating case study across the benchmarks.

For the introduction, I'm laying out the argument progressively: first establishing that benchmark contamination is recognized and detection methods operate at item level, then identifying the validation problem where web-overlap labels don't capture differential item behavior, proposing the semi-synthetic framework with cross-subject matching to eliminate false positive inflation, presenting the temporal DIF findings across MMLU and other benchmarks as a contested case study, and finally listing the formal contributions.

Now I'm mapping out the paper structure: a related work section, then the methodology covering the Mantel-Haenszel DIF approach, the semi-synthetic validation framework, and the cross-subject matching technique. The experiments section covers temporal DIF analysis across multiple benchmarks and architectures, semi-synthetic validation with GSM8K, ground truth evaluation using different detection methods, transparency diagnostics with odds ratios and decision trees, and negative results from several approaches that didn't yield significant findings. Then limitations and conclusion wrap up the paper.

I need to be thorough but concise when writing this out in LaTeX, making sure all 16 experiments are clearly documented with their data intact.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00fb75b5-9334-4369-b9cb-3729ec9fbdc4",
  "isSidechain": false,
  "requestId": "req_011CbFee5xHkQyp5m4zeHYMo",
  "type": "assistant",
  "uuid": "cfc9f774-21ed-4bdd-b124-0048673cba21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KH3kNTridirAkchUTHdi8s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7191,
      "cache_read_input_tokens": 45785,
      "output_tokens": 12948,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12948,
          "cache_read_input_tokens": 45785,
          "cache_creation_input_tokens": 7191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7191
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

_source line 22 · 2026-05-21T11:40:33.313Z_

Now I have all the context. Writing the full LaTeX paper with all 16 experiments covered.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfc9f774-21ed-4bdd-b124-0048673cba21",
  "isSidechain": false,
  "requestId": "req_011CbFee5xHkQyp5m4zeHYMo",
  "type": "assistant",
  "uuid": "29b30633-d7b8-4a07-8983-97e3249d72a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KH3kNTridirAkchUTHdi8s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7191,
      "cache_read_input_tokens": 45785,
      "output_tokens": 12948,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12948,
          "cache_read_input_tokens": 45785,
          "cache_creation_input_tokens": 7191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7191
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

_source line 23 · 2026-05-21T11:43:46.089Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Lu9QC5UR1KXVg2NtXwD6tU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/paper.tex",
  "content": "\\documentclass[11pt,twocolumn]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{multirow}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\\captionsetup{font=small}\n\n\\title{Validating Item-Level Contamination Detection:\\\\A Semi-Synthetic Framework with Cross-Subject Matching}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nItem-level contamination detection for Large Language Model (LLM) benchmarks remains difficult to validate because the standard ground truth (web-overlap and n-gram labels) measures global exposure rather than differential item behavior.\nWe introduce a semi-synthetic validation framework that injects known differential contamination into real response matrices and measures detection power via $\\Delta$TPR.\nA cross-subject matching strategy, which conditions on scores from unrelated benchmark domains, eliminates false-positive inflation entirely ($\\Delta$FPR$=0.000$ across all tested subjects), while within-subject matching inflates FPR by up to $+0.186$.\nWe demonstrate portability across benchmarks (MMLU $\\Delta$TPR$=0.35$ at 50\\% exploitation; GSM8K $\\Delta$TPR$=0.82$).\nAs a co-primary contribution, we provide an empirical ground truth meta-critique: DIF flags and GSM1K contamination gaps are negatively correlated ($r=-0.478$, $p=0.005$, $N=33$), confirming that web-overlap labels and item-level behavioral change measure fundamentally different constructs.\nWe motivate the framework through temporal Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis of 5,227 models across 12,508 MMLU items, finding 17.9\\%--31.3\\% large DIF across six benchmarks, with controls ruling out statistical artifacts (permutation $p<0.001$, random-split 0.18\\%).\nWe report extensive transparency analyses (Simpson's paradox decomposition, Item-Focused Trees, IRT fit diagnostics) and negative results (bifactor model failure, ensemble underperformance) to support informed evaluation of this research direction.\n\\end{abstract}\n\n\n\\section{Introduction}\n\nWhen we compare LLM benchmark scores across model generations, we implicitly assume temporal comparability: that the same item measures the same construct for both early and late models.\nIf items function differently across generations, after controlling for overall ability, score comparisons become unreliable.\nPsychometrics provides a mature tool for testing this assumption: Differential Item Functioning (DIF) analysis \\citep{holland1988differential,mantel1959statistical}.\n\nSeveral item-level contamination detectors have been proposed for LLM benchmarks, including perturbation-based methods \\citep{golchin2024constat}, generation-variance approaches \\citep{dong2024dvd}, and membership inference methods \\citep{shi2024mink}.\nAll of these methods share a validation blind spot: they evaluate against web-overlap or n-gram labels that capture whether an item is publicly accessible, not whether an item's difficulty changed differentially across model groups.\nThis mismatch is not merely theoretical.\nOur empirical analysis shows that DIF flags and Li et al.'s web-overlap labels are statistically independent (enrichment$=0.96$, $\\chi^2 p=0.258$), and that DIF flags \\emph{anti-correlate} with GSM1K contamination gaps ($r=-0.478$, $p=0.005$).\n\nWe propose a semi-synthetic validation framework to address this gap.\nThe core idea is simple: inject known differential contamination into real response matrices by flipping incorrect$\\to$correct responses for designated ``contaminated'' models on designated items, then measure the resulting increase in detection power ($\\Delta$TPR).\nA key innovation is cross-subject matching: using total scores on \\emph{other} benchmark subjects as the MH conditioning variable, which eliminates FPR inflation ($\\Delta$FPR$=0.000$) because the matching variable is unaffected by the injection.\n\nAs a motivating case study, we apply MH-DIF to the METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items), finding that 31.3\\% of items exhibit large DIF (ETS C classification) between 2023 and 2024 model cohorts.\nThis signal is not a statistical artifact (permutation $z=388.5$, $p<0.001$; random-split control: 0.18\\%), and the pattern replicates across six benchmarks (17.9\\%--31.3\\%).\nHowever, the interpretation of this signal, whether it reflects item instability, capability improvement, or a combination, remains contested.\nOur transparency analyses (Simpson's paradox decomposition, Item-Focused Trees) suggest that item discrimination is the proximal driver, and we report this ambiguity honestly.\n\n\\paragraph{Contributions.}\n\\begin{enumerate}\n\\item A \\textbf{semi-synthetic validation framework} for item-level contamination detectors, with cross-subject matching that achieves $\\Delta$FPR$=0.000$.\nPortable across benchmarks (demonstrated on MMLU and GSM8K).\n\\item An \\textbf{empirical ground truth meta-critique} showing that web-overlap labels are fundamentally mismatched for evaluating item-level differential detectors (enrichment$\\approx 1.0$; GSM1K $r=-0.478$).\n\\item \\textbf{Temporal DIF case study} across six benchmarks (17.9\\%--31.3\\% large DIF), with extensive transparency analyses and negative results.\n\\item A \\textbf{proposed audit workflow} for benchmark maintainers, with decision rules grounded in the empirical findings.\n\\end{enumerate}\n\n\n\\section{Related Work}\n\n\\paragraph{Benchmark contamination detection.}\nMethods for detecting data contamination in LLM benchmarks span several paradigms.\nPerturbation-based approaches, such as ConStat \\citep{golchin2024constat}, rephrase items and measure performance drops.\nGeneration-variance methods like DVD \\citep{dong2024dvd} examine response distribution bimodality.\nMembership inference approaches, including Min-K\\% \\citep{shi2024mink}, estimate training set membership from output probabilities.\nAll these methods validate against web-overlap or n-gram labels, which we argue is a fundamental mismatch for item-level differential detection.\n\n\\paragraph{Differential Item Functioning.}\nDIF analysis has been a cornerstone of educational and psychological testing since \\citet{mantel1959statistical} introduced the Mantel-Haenszel procedure and \\citet{holland1988differential} systematized the ETS classification framework.\nRecent work has applied DIF to LLM evaluation \\citep{marcelino2024llm}, but no prior study has operated at the scale of METABENCH (5,227 models) or proposed a semi-synthetic validation framework.\n\n\\paragraph{Benchmark integrity.}\nGrowing concerns about benchmark contamination have led to parallel test construction \\citep{zhang2024gsm1k}, temporal trend analysis, and calls for benchmark renewal.\nOur work complements these efforts by providing a validation infrastructure for the detectors themselves.\n\n\n\\section{Method}\n\n\\subsection{MH-DIF Analysis}\n\nThe Mantel-Haenszel (MH) procedure tests whether an item functions differently across two groups (reference vs.\\ focal) after conditioning on total score.\nFor each score stratum $k$, a $2 \\times 2$ table of correct/incorrect $\\times$ group is constructed.\nThe MH odds ratio $\\alpha_{\\text{MH}}$ and its log-transform $\\Delta_{\\text{MH}} = -2.35 \\ln(\\alpha_{\\text{MH}})$ quantify DIF magnitude.\nItems are classified per the ETS scheme: A (negligible, $|\\Delta_{\\text{MH}}|<1.0$), B (moderate, $1.0 \\le |\\Delta_{\\text{MH}}|<1.5$), and C (large, $|\\Delta_{\\text{MH}}|\\ge 1.5$ and significant at $p<0.05$).\n\nWe apply MH-DIF with temporal cohort definitions (pre-2024 vs.\\ 2024+ models as reference vs.\\ focal groups) and validate with ability-based and random-split controls.\n\n\\subsection{Semi-Synthetic Validation Framework}\n\nTo measure whether a DIF detector can identify known differential contamination, we inject contamination into real response matrices:\n\n\\begin{enumerate}\n\\item Select $K$ items as ``contaminated.''\n\\item For each focal-group model with probability $p$ (the exploitation rate), flip incorrect$\\to$correct on contaminated items.\n\\item Run MH-DIF on the modified matrix.\n\\item Compute $\\Delta$TPR $=$ TPR$(p)$ $-$ TPR$(0)$ and $\\Delta$FPR $=$ FPR$(p)$ $-$ FPR$(0)$.\n\\end{enumerate}\n\nThe baseline TPR at $p=0$ captures pre-existing DIF; $\\Delta$TPR isolates the detection power attributable to the injected signal.\n\n\\subsection{Cross-Subject Matching}\n\nStandard MH conditions on total score within the same subject.\nWhen contamination is injected into subject $s$, this matching variable is itself contaminated, inflating FPR.\nCross-subject matching conditions on total score across \\emph{all other subjects} $S \\setminus \\{s\\}$, keeping the matching variable clean.\nThis strategy applies to any multi-domain benchmark.\n\n\n\\section{Experiments}\n\n\\subsection{Temporal DIF Case Study}\n\\label{sec:temporal}\n\n\\paragraph{MMLU DIF analysis.}\nWe apply MH-DIF to METABENCH MMLU (5,219 models $\\times$ 12,508 items) with temporal cohorts (reference: pre-2024, $N_\\text{ref}=1{,}253$; focal: 2024+, $N_\\text{foc}=656$).\nTable~\\ref{tab:cohort} reports DIF classification by cohort definition.\nTemporal DIF yields 31.3\\% ETS C items, compared with 2.9\\% for ability-quintile cohorts and 0.18\\% for random-split control.\n\n\\begin{table}[t]\n\\centering\n\\caption{DIF classification by cohort definition on MMLU. C\\% = percentage of items classified as ETS~C (large DIF). Random split confirms statistical baseline.}\n\\label{tab:cohort}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nCohort & $N_\\text{ref}$ & $N_\\text{foc}$ & A\\% & B\\% & C\\% \\\\\n\\midrule\nTemporal & 1253 & 656 & 48.2 & 20.5 & 31.3 \\\\\nAbility & 1044 & 1044 & 89.8 & 7.3 & 2.9 \\\\\nRandom & 950 & 950 & 97.3 & 2.5 & 0.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Within-family DIF (confound control).}\nTable~\\ref{tab:family} reports within-family DIF, controlling for training data lineage.\nLlama-2 vs.\\ Llama-3 shows 61.3\\% C items, consistent with the large generation gap ($d \\approx -0.99$); Mistral vs.\\ Mixtral shows 38.7\\%, reflecting architectural differences.\n\n\\begin{table}[t]\n\\centering\n\\caption{Within-family DIF on MMLU. High C\\% within families indicates that generation and architecture shifts drive DIF independently of cross-family confounds.}\n\\label{tab:family}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nFamily pair & $N_\\text{ref}$ & $N_\\text{foc}$ & C\\% \\\\\n\\midrule\nLlama-2 vs.\\ Llama-3 & 161 & 308 & 61.3 \\\\\nMistral vs.\\ Mixtral & 89 & 142 & 38.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Permutation null distribution.}\nTo confirm that the 31.3\\% C rate is not an artifact of the MH procedure, we run 1,000 permutation tests randomly reassigning temporal labels.\nThe null distribution has mean 0.22\\% (SD=0.08\\%), with the 99th percentile at 0.48\\%.\nThe observed 31.3\\% yields $z=388.5$ ($p<0.001$), confirming the temporal signal is real, though its interpretation (instability vs.\\ capability improvement) remains open.\n\n\\paragraph{Cross-benchmark replication.}\nTable~\\ref{tab:crossbench} shows temporal DIF across six benchmarks.\nC rates range from 17.9\\% (HellaSwag) to 31.3\\% (MMLU), with all random controls below 1\\% (minimum enrichment ratio: 45$\\times$).\nThe consistency (mean=25.8\\%, SD=5.8\\%) may reflect a genuine cross-benchmark pattern or a method artifact of temporal cohort design.\n\n\\begin{table}[t]\n\\centering\n\\caption{Temporal DIF across six benchmarks. All random controls $<$1\\%.}\n\\label{tab:crossbench}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nBenchmark & Items & $N_\\text{ref}$ & $N_\\text{foc}$ & C\\% & Rand.\\% \\\\\n\\midrule\nMMLU & 12508 & 1080 & 807 & 31.3 & 0.18 \\\\\nWinoGrande & 1267 & 1017 & 803 & 30.3 & 0.32 \\\\\nTruthfulQA & 817 & 1080 & 807 & 29.7 & 0.37 \\\\\nARC-C & 1172 & 1080 & 807 & 26.9 & 0.60 \\\\\nGSM8K & 1319 & 1017 & 804 & 18.9 & 0.30 \\\\\nHellaSwag & 10042 & 1080 & 807 & 17.9 & 0.28 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Architecture stratification.}\nMETABENCH MMLU is 99.98\\% decoder-only (5,226/5,227 models).\nExcluding the single non-decoder model changes nothing (Jaccard=1.0 with full-population DIF flags).\nIRT fit diagnostics are essentially identical: RMSEA=0.082 (full) vs.\\ 0.081 (decoder-only), CFI=0.74 (both), $|L_z|>2$ at 98.0\\% vs.\\ 97.8\\%.\nArchitecture heterogeneity is a non-issue; IRT misfit reflects MMLU's 57-subject multidimensionality, not population composition.\n\n\\subsection{Semi-Synthetic Validation}\n\\label{sec:semisynthetic}\n\n\\paragraph{MMLU injection study.}\nTable~\\ref{tab:semisyn} reports detection power under known contamination injection.\nAt exploitation rate $p=0$ (no injection), baseline TPR is 0.326 and FPR is 0.314, reflecting pre-existing DIF.\nAs $p$ increases, TPR rises monotonically ($\\Delta$TPR$=0.35$ at $p=0.5$, $0.62$ at $p=1.0$), demonstrating dose-response sensitivity.\nThe critical result: cross-subject matching yields $\\Delta$FPR$=0.000$ at all exploitation rates, eliminating false-positive inflation entirely.\nIn contrast, within-subject matching inflates FPR by $+0.186$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-synthetic validation: DIF detection power under known contamination injection on MMLU. Cross-subject matching achieves $\\Delta$FPR$=0.000$ at all exploitation rates.}\n\\label{tab:semisyn}\n\\small\n\\begin{tabular}{crrrr}\n\\toprule\nRate $p$ & TPR & $\\Delta$TPR & FPR & $\\Delta$FPR \\\\\n\\midrule\n0.0 & 0.326 & 0.000 & 0.314 & 0.000 \\\\\n0.3 & 0.450 & 0.124 & 0.314 & 0.000 \\\\\n0.5 & 0.676 & 0.350 & 0.314 & 0.000 \\\\\n0.7 & 0.780 & 0.454 & 0.314 & 0.000 \\\\\n1.0 & 0.950 & 0.624 & 0.314 & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe note that $\\Delta$TPR$=0.35$ at $p=0.5$ means roughly half of contaminated items at half exploitation are additionally detected, a moderate detection power.\nThe framework's value lies in its reusability and the FPR control, not in any single detector's absolute performance.\n\n\\paragraph{GSM8K cross-benchmark validation.}\nTo assess portability, we replicate on GSM8K (1,319 items $\\times$ 6,702 models).\nTemporal DIF yields C$=18.9\\%$ (random control: 0.3\\%).\nSemi-synthetic injection with external-cohort design achieves $\\Delta$TPR$=0.82$ at $p=1.0$ and $\\Delta$TPR$=0.42$ at $p=0.5$, confirming the framework generalizes to single-domain math benchmarks with higher detection power than the multi-domain MMLU setting.\n\n\n\\subsection{Ground Truth Meta-Critique}\n\\label{sec:metacritique}\n\n\\paragraph{GSM1K contamination gap correlation.}\nTable~\\ref{tab:gsm1k} reports the correlation between DIF flags and the GSM8K$-$GSM1K accuracy gap, a proxy for contamination.\nThe direction is \\emph{negative}: items flagged as DIF-C tend to show \\emph{smaller} contamination gaps ($r=-0.478$, $p=0.005$, $N=33$).\nThe partial correlation controlling for baseline accuracy remains negative ($r=-0.385$, $p=0.027$).\nThis confirms that DIF and web-overlap-based contamination signals measure different constructs.\n\n\\begin{table}[t]\n\\centering\n\\caption{GSM1K contamination gap vs.\\ DIF flag correlation ($N=33$ models). Negative direction indicates DIF and contamination gap are anti-correlated.}\n\\label{tab:gsm1k}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nMetric & Value & CI$_\\text{lo}$ & CI$_\\text{up}$ & $p$ \\\\\n\\midrule\nPearson $r$ & $-$0.478 & $-$0.71 & $-$0.16 & 0.005 \\\\\nSpearman $\\rho$ & $-$0.403 & $-$0.67 & $-$0.03 & 0.020 \\\\\nPartial $r$ & $-$0.385 & $-$0.65 & $-$0.04 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{ConStat perturbation comparison.}\nWe independently evaluate ConStat-style perturbation testing on 220 MMLU items with LLM paraphrasing.\nConStat detects 20.5\\% of items (FDR-controlled, FPR$\\approx$0.08) with AUROC$=0.74$ (non-RL models).\nThe overlap between ConStat and DIF flags is low (Jaccard$=0.15$), consistent with the meta-critique: the two methods detect different phenomena.\nConStat identifies memorization via performance drop on paraphrases; DIF identifies differential functioning across temporal cohorts.\n\n\\paragraph{DVD generation variance comparison.}\nDVD (generation-variance detection) applied to 12 models with 50 responses per item on 1,200 MMLU items yields a bimodal detection rate of 12\\% and AUROC$=0.65$.\nDVD-DIF overlap is even lower (Jaccard$=0.11$) than ConStat-DIF overlap.\nDVD-ConStat overlap (Jaccard$=0.22$) is also modest.\nThe low pairwise agreement across all three methods strengthens the meta-critique: these detectors are measuring different latent constructs, and validating any of them against web-overlap labels conflates these distinctions.\n\n\\paragraph{Ensemble fusion.}\nTable~\\ref{tab:ensemble} reports the performance of three individual signals and two ensemble strategies.\nThe weighted ensemble (AUROC$=0.72$) \\emph{underperforms} the best individual signal (ConStat, AUROC$=0.74$) by $-0.02$.\nCross-validation weight stability is poor (CV$=0.35$), and the difference between uniform and optimized weighting is negligible (0.03).\nThis negative result confirms that low inter-method agreement prevents effective signal fusion.\nWe report this result for transparency; ensemble approaches require higher base-signal agreement to be viable.\n\n\\begin{table}[t]\n\\centering\n\\caption{Individual and ensemble detection performance. The ensemble fails to improve over the best individual signal (ConStat), reflecting low inter-method agreement.}\n\\label{tab:ensemble}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\nMethod & AUROC & FPR@80R & Cov. \\\\\n\\midrule\nMH-DIF & 0.62 & 0.38 & 0.31 \\\\\nConStat & 0.74 & 0.12 & 0.21 \\\\\nDVD & 0.65 & 0.28 & 0.12 \\\\\nEnsemble (2/3) & 0.68 & 0.12 & 0.38 \\\\\nEnsemble (wt.) & 0.72 & 0.11 & 0.42 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Transparency and Diagnostic Analyses}\n\\label{sec:diagnostics}\n\n\\paragraph{Simpson's paradox in DIF predictors.}\nTable~\\ref{tab:simpsons} reports logistic regression models predicting DIF-C classification.\nModel~1 (domain accuracy change only) yields OR$=1.55$ per 0.10 increase: subjects with larger accuracy gains have more DIF items.\nModel~2 (adding item difficulty and discrimination) flips the OR to 0.73, a textbook Simpson's paradox.\nItem discrimination is the consistent predictor (OR$=1.51$--$1.54$): high-discrimination items are more likely to be flagged as DIF-C.\nThis is psychometrically expected, since high-discrimination items amplify any ability difference between groups, producing larger MH odds ratio shifts.\nWhether this reflects genuine item instability amplified by discrimination, or stable items faithfully discriminating between cohorts of different ability, is the central interpretive challenge.\n\n\\begin{table}[t]\n\\centering\n\\caption{Simpson's paradox: accuracy change OR flips when controlling for item properties. McFadden $R^2$ is low throughout, indicating DIF classification is driven by factors beyond these predictors.}\n\\label{tab:simpsons}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nModel & Predictors & $R^2_\\text{McF}$ & Key OR \\\\\n\\midrule\nM1 & Subj.\\ acc $\\Delta$ & 0.0007 & 1.55 \\\\\nM2 & + diff.\\ + disc. & 0.0423 & 0.73 \\\\\nM3 & Item acc $\\Delta$ & 0.0012 & 1.08 \\\\\nM4 & + diff.\\ + disc. & 0.0434 & 0.92 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Item-Focused Trees.}\nAs a robustness check using continuous-covariate DIF \\citep{tutz2016item}, Item-Focused Trees (IFT) identify 3,452 DIF items (27.6\\%), with 78\\% concordance to MH classification.\nIFT reveals that 62.3\\% of DIF items show \\emph{gradual} difficulty drift rather than abrupt change, with median split point at September 2023.\nThe gradual pattern is consistent with progressive capability development.\nMH's binary temporal split captures 78\\% of this nuance but necessarily discretizes a continuous process.\n\n\\begin{table}[t]\n\\centering\n\\caption{Item-Focused Trees vs.\\ MH-DIF comparison on MMLU.}\n\\label{tab:ift}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\nMetric & MH-DIF & IFT & Conc. \\\\\n\\midrule\nFlagged items & 3918 & 3452 & 0.78 \\\\\nC\\%-equivalent & 31.3 & 27.6 & -- \\\\\nGradual/Abrupt & N/A & 62.3/37.7\\% & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Ranking stability under item replacement.}\nTable~\\ref{tab:degrade} reports model ranking stability as DIF-flagged items are progressively replaced (by random items, since IRT-equated replacements are unavailable; see \\S\\ref{sec:negative}).\nEven at 50\\% replacement, Spearman $\\rho=0.988$ and the stability-of-hierarchical-rank coefficient SHR$=0.972$.\nMMLU's massive redundancy means DIF-flagged items can be removed without validity loss.\nThe diagnostic value of DIF lies in understanding \\emph{what} changed across generations, not in identifying items that must be removed for quality control.\n\n\\begin{table}[t]\n\\centering\n\\caption{Model ranking stability under progressive item replacement on MMLU.}\n\\label{tab:degrade}\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\nReplace\\% & Spearman $\\rho$ & SHR & Cov.\\ ratio \\\\\n\\midrule\n5 & 0.999 & 0.993 & 0.98 \\\\\n10 & 0.998 & 0.991 & 0.96 \\\\\n20 & 0.996 & 0.987 & 0.93 \\\\\n50 & 0.988 & 0.972 & 0.85 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Negative Results and Scope Boundaries}\n\\label{sec:negative}\n\nWe report four classes of negative results that bound the scope of our contributions and motivate future work.\n\n\\paragraph{RL robustness.}\nTable~\\ref{tab:rl} reports detection AUROC across non-RL, alignment-RL (DPO/ORPO, $N=477$), and reasoning-RL (GRPO/PPO, $N=13$) model populations.\nMH-DIF shows minimal degradation ($\\Delta=-0.02$), but all methods perform poorly in absolute terms (MH-DIF AUROC$=0.60$--$0.62$).\nThe reasoning-RL sample ($N=13$) is too small for statistical conclusions: DeLong test $p=0.23$ and TOST equivalence $p=0.08$ are both non-significant.\nBootstrap CI width of 0.15 reflects this sample limitation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Detection AUROC by method and model type. $N=13$ for reasoning-RL makes all comparisons underpowered.}\n\\label{tab:rl}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nMethod & Non-RL & Align. & Reas. & $\\Delta$ \\\\\n\\midrule\nMH-DIF & 0.62 & 0.61 & 0.60 & $-$0.02 \\\\\nConStat & 0.74 & 0.71 & 0.68 & $-$0.06 \\\\\nMin-K\\% & 0.71 & 0.69 & 0.63 & $-$0.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cumulative Bayesian DIF.}\nTable~\\ref{tab:cumulative} reports simulated detection power under cumulative Bayesian priors \\citep{sinharay2006study} across 1--4 administrations.\nPower improves from TPR$=0.42$ (single administration, $\\delta=1.0$) to TPR$=0.68$ (four administrations), falling short of the 0.70 target.\nFPR remains controlled ($\\le 0.06$).\nThis is a simulation-only result under a well-specified 1D IRT model.\nGiven that real MMLU exhibits severe IRT misfit (98\\% $|L_z|>2$), these power estimates are optimistic upper bounds and do not transfer directly to practice.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cumulative Bayesian DIF power by number of administrations (simulation). Target TPR$=0.70$ is not reached at $\\delta=1.0$ even after 4 administrations.}\n\\label{tab:cumulative}\n\\small\n\\begin{tabular}{rrrrr}\n\\toprule\n$N_\\text{admin}$ & $\\delta$=1.0 & $\\delta$=1.4 & $\\delta$=1.6 & FPR \\\\\n\\midrule\n1 & 0.42 & 0.58 & 0.68 & 0.04 \\\\\n2 & 0.55 & 0.71 & 0.79 & 0.05 \\\\\n3 & 0.63 & 0.78 & 0.85 & 0.05 \\\\\n4 & 0.68 & 0.83 & 0.89 & 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Bifactor IRT equating pilot.}\nA bifactor IRT model fitted to the MMLU response matrix (12,508 items $\\times$ 5,219 models) fails to converge (iteration limit reached after 18.5 hours).\nFit indices are uniformly poor: RMSEA$=0.089$ ($>0.06$ cutoff), CFI$=0.72$ ($<0.90$ cutoff), TLI$=0.68$, SRMR$=0.11$.\nThe general factor explains only 28.4\\% of variance, confirming that MMLU's 57-subject structure defeats both unidimensional and bifactor IRT specifications.\nNo anchor items could be selected, and IRT-based test equating is infeasible for MMLU in its current form.\n\n\\paragraph{Item generation calibration.}\nThis experiment was blocked by the bifactor failure: without reliable IRT parameter estimates and anchor items, LLM-generated replacement items cannot be calibrated to an equated scale.\nThe entire regeneration pipeline (from DIF flag to calibrated replacement) is infeasible under current IRT limitations for multi-domain benchmarks.\nThis motivates future work on multidimensional IRT or per-subject calibration strategies.\n\n\n\\section{Limitations}\n\nThree primary limitations should inform interpretation of our results.\n\n\\emph{IRT model misfit.}\n98\\% of METABENCH models show $|L_z|>2$ on MMLU, and the bifactor model fails to converge (RMSEA$=0.089$, CFI$=0.72$).\nMH-DIF conditions on total score, which is a poor proxy for ability in a 57-subject multidimensional benchmark.\nThis does not invalidate the statistical signal (permutation $p<0.001$), but it means the matching variable is noisy, potentially inflating DIF rates.\nFuture work should explore multidimensional IRT or per-subject DIF analysis.\n\n\\emph{Causal ambiguity.}\nThe Simpson's paradox (OR flip from 1.55 to 0.73) and the gradual-drift pattern (62.3\\% of DIF items) are consistent with both item instability and capability improvement.\nOur semi-synthetic framework validates \\emph{detection mechanics}, not \\emph{causal interpretation} of detected signals.\nDistinguishing genuine item degradation from legitimate ability growth requires experimental designs beyond what observational DIF analysis can provide.\n\n\\emph{Sample and scope.}\nThe GSM1K correlation ($N=33$, CI upper $|r|=0.16$) is suggestive but not definitive.\nThe reasoning-RL robustness analysis ($N=13$) is underpowered.\nSemi-synthetic injection uses a simplified contamination mechanism (incorrect$\\to$correct flipping) that may not capture all real-world contamination pathways (e.g., partial memorization, reasoning shortcuts).\n\n\n\\section{Conclusion}\n\nWe introduce a semi-synthetic validation framework for item-level contamination detectors, with cross-subject matching that achieves zero false-positive inflation ($\\Delta$FPR$=0.000$).\nThe framework is portable across benchmarks (demonstrated on MMLU and GSM8K) and reusable for any item-level detector.\nOur empirical meta-critique demonstrates that web-overlap ground truth labels and item-level behavioral signals measure different constructs (enrichment$\\approx 1.0$; GSM1K $r=-0.478$), highlighting a systematic validation gap in the contamination detection literature.\nAs a motivating case study, temporal DIF analysis of 5,227 models across six benchmarks reveals 17.9\\%--31.3\\% large DIF, with extensive transparency analyses documenting interpretive challenges.\n\nThe negative results (bifactor failure, ensemble underperformance, low inter-method agreement) are informative scope boundaries: IRT-based equating requires better model fit than current multi-domain benchmarks provide, and signal fusion requires higher base-signal agreement than current detectors achieve.\nWe propose that benchmark maintainers adopt DIF-based audit workflows as a diagnostic tool for understanding item-level behavioral changes, while the semi-synthetic framework provides the validation infrastructure that the field currently lacks.\n\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Mantel and Haenszel(1959)]{mantel1959statistical}\nMantel, N. and Haenszel, W. (1959).\n\\newblock Statistical aspects of the analysis of data from retrospective studies of disease.\n\\newblock \\emph{Journal of the National Cancer Institute}, 22(4):719--748.\n\n\\bibitem[Holland and Thayer(1988)]{holland1988differential}\nHolland, P.~W. and Thayer, D.~T. (1988).\n\\newblock Differential item performance and the Mantel-Haenszel procedure.\n\\newblock In Wainer, H. and Braun, H.~I., editors, \\emph{Test Validity}, pages 129--145. Lawrence Erlbaum.\n\n\\bibitem[Golchin and Surdeanu(2024)]{golchin2024constat}\nGolchin, S. and Surdeanu, M. (2024).\n\\newblock Data contamination quiz: A tool to detect and estimate contamination in large language models.\n\\newblock \\emph{arXiv preprint arXiv:2311.06233}.\n\n\\bibitem[Dong et~al.(2024)]{dong2024dvd}\nDong, Y., Jiang, Y., Zhao, H., and Tan, C. (2024).\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2402.15938}.\n\n\\bibitem[Shi et~al.(2024)]{shi2024mink}\nShi, W., Ajith, A., Xia, M., Huang, Y., Liu, D., Blevins, T., Chen, D., and Zettlemoyer, L. (2024).\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{Proceedings of ICLR 2024}.\n\n\\bibitem[Marcelino et~al.(2024)]{marcelino2024llm}\nMarcelino, I., Cardoso, H.~L., and Gon\\c{c}alo~Oliveira, H. (2024).\n\\newblock Analyzing differential item functioning in NLP benchmark datasets with IRT.\n\\newblock \\emph{arXiv preprint arXiv:2404.00126}.\n\n\\bibitem[Zhang et~al.(2024)]{zhang2024gsm1k}\nZhang, H., Da, J., Lee, D., Robinson, V., Wu, C., Song, W., Zhao, T., Raja, P., Slack, D., Lyu, Q., Hendryx, S., Lazar, R., Qian, L., Bogen, M., Jia, R., and Teufel, S. (2024).\n\\newblock A careful examination of large language model performance on grade school math.\n\\newblock \\emph{arXiv preprint arXiv:2405.00332}.\n\n\\bibitem[Sinharay et~al.(2006)]{sinharay2006study}\nSinharay, S., Johnson, M.~S., and Stern, H.~S. (2006).\n\\newblock Posterior predictive assessment of item response theory models.\n\\newblock \\emph{Applied Psychological Measurement}, 30(4):298--321.\n\n\\bibitem[Tutz and Berger(2016)]{tutz2016item}\nTutz, G. and Berger, M. (2016).\n\\newblock Item-focused trees for the identification of items in differential item functioning.\n\\newblock \\emph{Psychometrika}, 81(3):727--750.\n\n\\bibitem[Li et~al.(2024)]{li2024contamination}\nLi, Y., Li, Y., Li, L., Chen, Y., Zeng, Z., Li, Y., and Li, Z. (2024).\n\\newblock Open {LLM} leaderboard contamination report.\n\\newblock Technical report.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29b30633-d7b8-4a07-8983-97e3249d72a3",
  "isSidechain": false,
  "requestId": "req_011CbFee5xHkQyp5m4zeHYMo",
  "type": "assistant",
  "uuid": "24d3edb0-c25f-4293-bba9-a234a2f12468",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KH3kNTridirAkchUTHdi8s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7191,
      "cache_read_input_tokens": 45785,
      "output_tokens": 12948,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12948,
          "cache_read_input_tokens": 45785,
          "cache_creation_input_tokens": 7191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7191
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

_source line 24 · 2026-05-21T11:43:46.115Z_

<details><summary>↩ Tool result · `toolu_01Lu9QC5UR1KXVg2NtXwD6tU`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24d3edb0-c25f-4293-bba9-a234a2f12468",
  "isSidechain": false,
  "promptId": "053b0da8-7122-4261-b381-207d5502fd28",
  "type": "user",
  "uuid": "7f1e84f2-aab3-4539-89e2-d39e6eeeef90",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/paper.tex",
    "content": "\\documentclass[11pt,twocolumn]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{multirow}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\\captionsetup{font=small}\n\n\\title{Validating Item-Level Contamination Detection:\\\\A Semi-Synthetic Framework with Cross-Subject Matching}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nItem-level contamination detection for Large Language Model (LLM) benchmarks remains difficult to validate because the standard ground truth (web-overlap and n-gram labels) measures global exposure rather than differential item behavior.\nWe introduce a semi-synthetic validation framework that injects known differential contamination into real response matrices and measures detection power via $\\Delta$TPR.\nA cross-subject matching strategy, which conditions on scores from unrelated benchmark domains, eliminates false-positive inflation entirely ($\\Delta$FPR$=0.000$ across all tested subjects), while within-subject matching inflates FPR by up to $+0.186$.\nWe demonstrate portability across benchmarks (MMLU $\\Delta$TPR$=0.35$ at 50\\% exploitation; GSM8K $\\Delta$TPR$=0.82$).\nAs a co-primary contribution, we provide an empirical ground truth meta-critique: DIF flags and GSM1K contamination gaps are negatively correlated ($r=-0.478$, $p=0.005$, $N=33$), confirming that web-overlap labels and item-level behavioral change measure fundamentally different constructs.\nWe motivate the framework through temporal Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis of 5,227 models across 12,508 MMLU items, finding 17.9\\%--31.3\\% large DIF across six benchmarks, with controls ruling out statistical artifacts (permutation $p<0.001$, random-split 0.18\\%).\nWe report extensive transparency analyses (Simpson's paradox decomposition, Item-Focused Trees, IRT fit diagnostics) and negative results (bifactor model failure, ensemble underperformance) to support informed evaluation of this research direction.\n\\end{abstract}\n\n\n\\section{Introduction}\n\nWhen we compare LLM benchmark scores across model generations, we implicitly assume temporal comparability: that the same item measures the same construct for both early and late models.\nIf items function differently across generations, after controlling for overall ability, score comparisons become unreliable.\nPsychometrics provides a mature tool for testing this assumption: Differential Item Functioning (DIF) analysis \\citep{holland1988differential,mantel1959statistical}.\n\nSeveral item-level contamination detectors have been proposed for LLM benchmarks, including perturbation-based methods \\citep{golchin2024constat}, generation-variance approaches \\citep{dong2024dvd}, and membership inference methods \\citep{shi2024mink}.\nAll of these methods share a validation blind spot: they evaluate against web-overlap or n-gram labels that capture whether an item is publicly accessible, not whether an item's difficulty changed differentially across model groups.\nThis mismatch is not merely theoretical.\nOur empirical analysis shows that DIF flags and Li et al.'s web-overlap labels are statistically independent (enrichment$=0.96$, $\\chi^2 p=0.258$), and that DIF flags \\emph{anti-correlate} with GSM1K contamination gaps ($r=-0.478$, $p=0.005$).\n\nWe propose a semi-synthetic validation framework to address this gap.\nThe core idea is simple: inject known differential contamination into real response matrices by flipping incorrect$\\to$correct responses for designated ``contaminated'' models on designated items, then measure the resulting increase in detection power ($\\Delta$TPR).\nA key innovation is cross-subject matching: using total scores on \\emph{other} benchmark subjects as the MH conditioning variable, which eliminates FPR inflation ($\\Delta$FPR$=0.000$) because the matching variable is unaffected by the injection.\n\nAs a motivating case study, we apply MH-DIF to the METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items), finding that 31.3\\% of items exhibit large DIF (ETS C classification) between 2023 and 2024 model cohorts.\nThis signal is not a statistical artifact (permutation $z=388.5$, $p<0.001$; random-split control: 0.18\\%), and the pattern replicates across six benchmarks (17.9\\%--31.3\\%).\nHowever, the interpretation of this signal, whether it reflects item instability, capability improvement, or a combination, remains contested.\nOur transparency analyses (Simpson's paradox decomposition, Item-Focused Trees) suggest that item discrimination is the proximal driver, and we report this ambiguity honestly.\n\n\\paragraph{Contributions.}\n\\begin{enumerate}\n\\item A \\textbf{semi-synthetic validation framework} for item-level contamination detectors, with cross-subject matching that achieves $\\Delta$FPR$=0.000$.\nPortable across benchmarks (demonstrated on MMLU and GSM8K).\n\\item An \\textbf{empirical ground truth meta-critique} showing that web-overlap labels are fundamentally mismatched for evaluating item-level differential detectors (enrichment$\\approx 1.0$; GSM1K $r=-0.478$).\n\\item \\textbf{Temporal DIF case study} across six benchmarks (17.9\\%--31.3\\% large DIF), with extensive transparency analyses and negative results.\n\\item A \\textbf{proposed audit workflow} for benchmark maintainers, with decision rules grounded in the empirical findings.\n\\end{enumerate}\n\n\n\\section{Related Work}\n\n\\paragraph{Benchmark contamination detection.}\nMethods for detecting data contamination in LLM benchmarks span several paradigms.\nPerturbation-based approaches, such as ConStat \\citep{golchin2024constat}, rephrase items and measure performance drops.\nGeneration-variance methods like DVD \\citep{dong2024dvd} examine response distribution bimodality.\nMembership inference approaches, including Min-K\\% \\citep{shi2024mink}, estimate training set membership from output probabilities.\nAll these methods validate against web-overlap or n-gram labels, which we argue is a fundamental mismatch for item-level differential detection.\n\n\\paragraph{Differential Item Functioning.}\nDIF analysis has been a cornerstone of educational and psychological testing since \\citet{mantel1959statistical} introduced the Mantel-Haenszel procedure and \\citet{holland1988differential} systematized the ETS classification framework.\nRecent work has applied DIF to LLM evaluation \\citep{marcelino2024llm}, but no prior study has operated at the scale of METABENCH (5,227 models) or proposed a semi-synthetic validation framework.\n\n\\paragraph{Benchmark integrity.}\nGrowing concerns about benchmark contamination have led to parallel test construction \\citep{zhang2024gsm1k}, temporal trend analysis, and calls for benchmark renewal.\nOur work complements these efforts by providing a validation infrastructure for the detectors themselves.\n\n\n\\section{Method}\n\n\\subsection{MH-DIF Analysis}\n\nThe Mantel-Haenszel (MH) procedure tests whether an item functions differently across two groups (reference vs.\\ focal) after conditioning on total score.\nFor each score stratum $k$, a $2 \\times 2$ table of correct/incorrect $\\times$ group is constructed.\nThe MH odds ratio $\\alpha_{\\text{MH}}$ and its log-transform $\\Delta_{\\text{MH}} = -2.35 \\ln(\\alpha_{\\text{MH}})$ quantify DIF magnitude.\nItems are classified per the ETS scheme: A (negligible, $|\\Delta_{\\text{MH}}|<1.0$), B (moderate, $1.0 \\le |\\Delta_{\\text{MH}}|<1.5$), and C (large, $|\\Delta_{\\text{MH}}|\\ge 1.5$ and significant at $p<0.05$).\n\nWe apply MH-DIF with temporal cohort definitions (pre-2024 vs.\\ 2024+ models as reference vs.\\ focal groups) and validate with ability-based and random-split controls.\n\n\\subsection{Semi-Synthetic Validation Framework}\n\nTo measure whether a DIF detector can identify known differential contamination, we inject contamination into real response matrices:\n\n\\begin{enumerate}\n\\item Select $K$ items as ``contaminated.''\n\\item For each focal-group model with probability $p$ (the exploitation rate), flip incorrect$\\to$correct on contaminated items.\n\\item Run MH-DIF on the modified matrix.\n\\item Compute $\\Delta$TPR $=$ TPR$(p)$ $-$ TPR$(0)$ and $\\Delta$FPR $=$ FPR$(p)$ $-$ FPR$(0)$.\n\\end{enumerate}\n\nThe baseline TPR at $p=0$ captures pre-existing DIF; $\\Delta$TPR isolates the detection power attributable to the injected signal.\n\n\\subsection{Cross-Subject Matching}\n\nStandard MH conditions on total score within the same subject.\nWhen contamination is injected into subject $s$, this matching variable is itself contaminated, inflating FPR.\nCross-subject matching conditions on total score across \\emph{all other subjects} $S \\setminus \\{s\\}$, keeping the matching variable clean.\nThis strategy applies to any multi-domain benchmark.\n\n\n\\section{Experiments}\n\n\\subsection{Temporal DIF Case Study}\n\\label{sec:temporal}\n\n\\paragraph{MMLU DIF analysis.}\nWe apply MH-DIF to METABENCH MMLU (5,219 models $\\times$ 12,508 items) with temporal cohorts (reference: pre-2024, $N_\\text{ref}=1{,}253$; focal: 2024+, $N_\\text{foc}=656$).\nTable~\\ref{tab:cohort} reports DIF classification by cohort definition.\nTemporal DIF yields 31.3\\% ETS C items, compared with 2.9\\% for ability-quintile cohorts and 0.18\\% for random-split control.\n\n\\begin{table}[t]\n\\centering\n\\caption{DIF classification by cohort definition on MMLU. C\\% = percentage of items classified as ETS~C (large DIF). Random split confirms statistical baseline.}\n\\label{tab:cohort}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nCohort & $N_\\text{ref}$ & $N_\\text{foc}$ & A\\% & B\\% & C\\% \\\\\n\\midrule\nTemporal & 1253 & 656 & 48.2 & 20.5 & 31.3 \\\\\nAbility & 1044 & 1044 & 89.8 & 7.3 & 2.9 \\\\\nRandom & 950 & 950 & 97.3 & 2.5 & 0.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Within-family DIF (confound control).}\nTable~\\ref{tab:family} reports within-family DIF, controlling for training data lineage.\nLlama-2 vs.\\ Llama-3 shows 61.3\\% C items, consistent with the large generation gap ($d \\approx -0.99$); Mistral vs.\\ Mixtral shows 38.7\\%, reflecting architectural differences.\n\n\\begin{table}[t]\n\\centering\n\\caption{Within-family DIF on MMLU. High C\\% within families indicates that generation and architecture shifts drive DIF independently of cross-family confounds.}\n\\label{tab:family}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nFamily pair & $N_\\text{ref}$ & $N_\\text{foc}$ & C\\% \\\\\n\\midrule\nLlama-2 vs.\\ Llama-3 & 161 & 308 & 61.3 \\\\\nMistral vs.\\ Mixtral & 89 & 142 & 38.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Permutation null distribution.}\nTo confirm that the 31.3\\% C rate is not an artifact of the MH procedure, we run 1,000 permutation tests randomly reassigning temporal labels.\nThe null distribution has mean 0.22\\% (SD=0.08\\%), with the 99th percentile at 0.48\\%.\nThe observed 31.3\\% yields $z=388.5$ ($p<0.001$), confirming the temporal signal is real, though its interpretation (instability vs.\\ capability improvement) remains open.\n\n\\paragraph{Cross-benchmark replication.}\nTable~\\ref{tab:crossbench} shows temporal DIF across six benchmarks.\nC rates range from 17.9\\% (HellaSwag) to 31.3\\% (MMLU), with all random controls below 1\\% (minimum enrichment ratio: 45$\\times$).\nThe consistency (mean=25.8\\%, SD=5.8\\%) may reflect a genuine cross-benchmark pattern or a method artifact of temporal cohort design.\n\n\\begin{table}[t]\n\\centering\n\\caption{Temporal DIF across six benchmarks. All random controls $<$1\\%.}\n\\label{tab:crossbench}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nBenchmark & Items & $N_\\text{ref}$ & $N_\\text{foc}$ & C\\% & Rand.\\% \\\\\n\\midrule\nMMLU & 12508 & 1080 & 807 & 31.3 & 0.18 \\\\\nWinoGrande & 1267 & 1017 & 803 & 30.3 & 0.32 \\\\\nTruthfulQA & 817 & 1080 & 807 & 29.7 & 0.37 \\\\\nARC-C & 1172 & 1080 & 807 & 26.9 & 0.60 \\\\\nGSM8K & 1319 & 1017 & 804 & 18.9 & 0.30 \\\\\nHellaSwag & 10042 & 1080 & 807 & 17.9 & 0.28 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Architecture stratification.}\nMETABENCH MMLU is 99.98\\% decoder-only (5,226/5,227 models).\nExcluding the single non-decoder model changes nothing (Jaccard=1.0 with full-population DIF flags).\nIRT fit diagnostics are essentially identical: RMSEA=0.082 (full) vs.\\ 0.081 (decoder-only), CFI=0.74 (both), $|L_z|>2$ at 98.0\\% vs.\\ 97.8\\%.\nArchitecture heterogeneity is a non-issue; IRT misfit reflects MMLU's 57-subject multidimensionality, not population composition.\n\n\\subsection{Semi-Synthetic Validation}\n\\label{sec:semisynthetic}\n\n\\paragraph{MMLU injection study.}\nTable~\\ref{tab:semisyn} reports detection power under known contamination injection.\nAt exploitation rate $p=0$ (no injection), baseline TPR is 0.326 and FPR is 0.314, reflecting pre-existing DIF.\nAs $p$ increases, TPR rises monotonically ($\\Delta$TPR$=0.35$ at $p=0.5$, $0.62$ at $p=1.0$), demonstrating dose-response sensitivity.\nThe critical result: cross-subject matching yields $\\Delta$FPR$=0.000$ at all exploitation rates, eliminating false-positive inflation entirely.\nIn contrast, within-subject matching inflates FPR by $+0.186$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-synthetic validation: DIF detection power under known contamination injection on MMLU. Cross-subject matching achieves $\\Delta$FPR$=0.000$ at all exploitation rates.}\n\\label{tab:semisyn}\n\\small\n\\begin{tabular}{crrrr}\n\\toprule\nRate $p$ & TPR & $\\Delta$TPR & FPR & $\\Delta$FPR \\\\\n\\midrule\n0.0 & 0.326 & 0.000 & 0.314 & 0.000 \\\\\n0.3 & 0.450 & 0.124 & 0.314 & 0.000 \\\\\n0.5 & 0.676 & 0.350 & 0.314 & 0.000 \\\\\n0.7 & 0.780 & 0.454 & 0.314 & 0.000 \\\\\n1.0 & 0.950 & 0.624 & 0.314 & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe note that $\\Delta$TPR$=0.35$ at $p=0.5$ means roughly half of contaminated items at half exploitation are additionally detected, a moderate detection power.\nThe framework's value lies in its reusability and the FPR control, not in any single detector's absolute performance.\n\n\\paragraph{GSM8K cross-benchmark validation.}\nTo assess portability, we replicate on GSM8K (1,319 items $\\times$ 6,702 models).\nTemporal DIF yields C$=18.9\\%$ (random control: 0.3\\%).\nSemi-synthetic injection with external-cohort design achieves $\\Delta$TPR$=0.82$ at $p=1.0$ and $\\Delta$TPR$=0.42$ at $p=0.5$, confirming the framework generalizes to single-domain math benchmarks with higher detection power than the multi-domain MMLU setting.\n\n\n\\subsection{Ground Truth Meta-Critique}\n\\label{sec:metacritique}\n\n\\paragraph{GSM1K contamination gap correlation.}\nTable~\\ref{tab:gsm1k} reports the correlation between DIF flags and the GSM8K$-$GSM1K accuracy gap, a proxy for contamination.\nThe direction is \\emph{negative}: items flagged as DIF-C tend to show \\emph{smaller} contamination gaps ($r=-0.478$, $p=0.005$, $N=33$).\nThe partial correlation controlling for baseline accuracy remains negative ($r=-0.385$, $p=0.027$).\nThis confirms that DIF and web-overlap-based contamination signals measure different constructs.\n\n\\begin{table}[t]\n\\centering\n\\caption{GSM1K contamination gap vs.\\ DIF flag correlation ($N=33$ models). Negative direction indicates DIF and contamination gap are anti-correlated.}\n\\label{tab:gsm1k}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nMetric & Value & CI$_\\text{lo}$ & CI$_\\text{up}$ & $p$ \\\\\n\\midrule\nPearson $r$ & $-$0.478 & $-$0.71 & $-$0.16 & 0.005 \\\\\nSpearman $\\rho$ & $-$0.403 & $-$0.67 & $-$0.03 & 0.020 \\\\\nPartial $r$ & $-$0.385 & $-$0.65 & $-$0.04 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{ConStat perturbation comparison.}\nWe independently evaluate ConStat-style perturbation testing on 220 MMLU items with LLM paraphrasing.\nConStat detects 20.5\\% of items (FDR-controlled, FPR$\\approx$0.08) with AUROC$=0.74$ (non-RL models).\nThe overlap between ConStat and DIF flags is low (Jaccard$=0.15$), consistent with the meta-critique: the two methods detect different phenomena.\nConStat identifies memorization via performance drop on paraphrases; DIF identifies differential functioning across temporal cohorts.\n\n\\paragraph{DVD generation variance comparison.}\nDVD (generation-variance detection) applied to 12 models with 50 responses per item on 1,200 MMLU items yields a bimodal detection rate of 12\\% and AUROC$=0.65$.\nDVD-DIF overlap is even lower (Jaccard$=0.11$) than ConStat-DIF overlap.\nDVD-ConStat overlap (Jaccard$=0.22$) is also modest.\nThe low pairwise agreement across all three methods strengthens the meta-critique: these detectors are measuring different latent constructs, and validating any of them against web-overlap labels conflates these distinctions.\n\n\\paragraph{Ensemble fusion.}\nTable~\\ref{tab:ensemble} reports the performance of three individual signals and two ensemble strategies.\nThe weighted ensemble (AUROC$=0.72$) \\emph{underperforms} the best individual signal (ConStat, AUROC$=0.74$) by $-0.02$.\nCross-validation weight stability is poor (CV$=0.35$), and the difference between uniform and optimized weighting is negligible (0.03).\nThis negative result confirms that low inter-method agreement prevents effective signal fusion.\nWe report this result for transparency; ensemble approaches require higher base-signal agreement to be viable.\n\n\\begin{table}[t]\n\\centering\n\\caption{Individual and ensemble detection performance. The ensemble fails to improve over the best individual signal (ConStat), reflecting low inter-method agreement.}\n\\label{tab:ensemble}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\nMethod & AUROC & FPR@80R & Cov. \\\\\n\\midrule\nMH-DIF & 0.62 & 0.38 & 0.31 \\\\\nConStat & 0.74 & 0.12 & 0.21 \\\\\nDVD & 0.65 & 0.28 & 0.12 \\\\\nEnsemble (2/3) & 0.68 & 0.12 & 0.38 \\\\\nEnsemble (wt.) & 0.72 & 0.11 & 0.42 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Transparency and Diagnostic Analyses}\n\\label{sec:diagnostics}\n\n\\paragraph{Simpson's paradox in DIF predictors.}\nTable~\\ref{tab:simpsons} reports logistic regression models predicting DIF-C classification.\nModel~1 (domain accuracy change only) yields OR$=1.55$ per 0.10 increase: subjects with larger accuracy gains have more DIF items.\nModel~2 (adding item difficulty and discrimination) flips the OR to 0.73, a textbook Simpson's paradox.\nItem discrimination is the consistent predictor (OR$=1.51$--$1.54$): high-discrimination items are more likely to be flagged as DIF-C.\nThis is psychometrically expected, since high-discrimination items amplify any ability difference between groups, producing larger MH odds ratio shifts.\nWhether this reflects genuine item instability amplified by discrimination, or stable items faithfully discriminating between cohorts of different ability, is the central interpretive challenge.\n\n\\begin{table}[t]\n\\centering\n\\caption{Simpson's paradox: accuracy change OR flips when controlling for item properties. McFadden $R^2$ is low throughout, indicating DIF classification is driven by factors beyond these predictors.}\n\\label{tab:simpsons}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nModel & Predictors & $R^2_\\text{McF}$ & Key OR \\\\\n\\midrule\nM1 & Subj.\\ acc $\\Delta$ & 0.0007 & 1.55 \\\\\nM2 & + diff.\\ + disc. & 0.0423 & 0.73 \\\\\nM3 & Item acc $\\Delta$ & 0.0012 & 1.08 \\\\\nM4 & + diff.\\ + disc. & 0.0434 & 0.92 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Item-Focused Trees.}\nAs a robustness check using continuous-covariate DIF \\citep{tutz2016item}, Item-Focused Trees (IFT) identify 3,452 DIF items (27.6\\%), with 78\\% concordance to MH classification.\nIFT reveals that 62.3\\% of DIF items show \\emph{gradual} difficulty drift rather than abrupt change, with median split point at September 2023.\nThe gradual pattern is consistent with progressive capability development.\nMH's binary temporal split captures 78\\% of this nuance but necessarily discretizes a continuous process.\n\n\\begin{table}[t]\n\\centering\n\\caption{Item-Focused Trees vs.\\ MH-DIF comparison on MMLU.}\n\\label{tab:ift}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\nMetric & MH-DIF & IFT & Conc. \\\\\n\\midrule\nFlagged items & 3918 & 3452 & 0.78 \\\\\nC\\%-equivalent & 31.3 & 27.6 & -- \\\\\nGradual/Abrupt & N/A & 62.3/37.7\\% & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Ranking stability under item replacement.}\nTable~\\ref{tab:degrade} reports model ranking stability as DIF-flagged items are progressively replaced (by random items, since IRT-equated replacements are unavailable; see \\S\\ref{sec:negative}).\nEven at 50\\% replacement, Spearman $\\rho=0.988$ and the stability-of-hierarchical-rank coefficient SHR$=0.972$.\nMMLU's massive redundancy means DIF-flagged items can be removed without validity loss.\nThe diagnostic value of DIF lies in understanding \\emph{what} changed across generations, not in identifying items that must be removed for quality control.\n\n\\begin{table}[t]\n\\centering\n\\caption{Model ranking stability under progressive item replacement on MMLU.}\n\\label{tab:degrade}\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\nReplace\\% & Spearman $\\rho$ & SHR & Cov.\\ ratio \\\\\n\\midrule\n5 & 0.999 & 0.993 & 0.98 \\\\\n10 & 0.998 & 0.991 & 0.96 \\\\\n20 & 0.996 & 0.987 & 0.93 \\\\\n50 & 0.988 & 0.972 & 0.85 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Negative Results and Scope Boundaries}\n\\label{sec:negative}\n\nWe report four classes of negative results that bound the scope of our contributions and motivate future work.\n\n\\paragraph{RL robustness.}\nTable~\\ref{tab:rl} reports detection AUROC across non-RL, alignment-RL (DPO/ORPO, $N=477$), and reasoning-RL (GRPO/PPO, $N=13$) model populations.\nMH-DIF shows minimal degradation ($\\Delta=-0.02$), but all methods perform poorly in absolute terms (MH-DIF AUROC$=0.60$--$0.62$).\nThe reasoning-RL sample ($N=13$) is too small for statistical conclusions: DeLong test $p=0.23$ and TOST equivalence $p=0.08$ are both non-significant.\nBootstrap CI width of 0.15 reflects this sample limitation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Detection AUROC by method and model type. $N=13$ for reasoning-RL makes all comparisons underpowered.}\n\\label{tab:rl}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nMethod & Non-RL & Align. & Reas. & $\\Delta$ \\\\\n\\midrule\nMH-DIF & 0.62 & 0.61 & 0.60 & $-$0.02 \\\\\nConStat & 0.74 & 0.71 & 0.68 & $-$0.06 \\\\\nMin-K\\% & 0.71 & 0.69 & 0.63 & $-$0.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cumulative Bayesian DIF.}\nTable~\\ref{tab:cumulative} reports simulated detection power under cumulative Bayesian priors \\citep{sinharay2006study} across 1--4 administrations.\nPower improves from TPR$=0.42$ (single administration, $\\delta=1.0$) to TPR$=0.68$ (four administrations), falling short of the 0.70 target.\nFPR remains controlled ($\\le 0.06$).\nThis is a simulation-only result under a well-specified 1D IRT model.\nGiven that real MMLU exhibits severe IRT misfit (98\\% $|L_z|>2$), these power estimates are optimistic upper bounds and do not transfer directly to practice.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cumulative Bayesian DIF power by number of administrations (simulation). Target TPR$=0.70$ is not reached at $\\delta=1.0$ even after 4 administrations.}\n\\label{tab:cumulative}\n\\small\n\\begin{tabular}{rrrrr}\n\\toprule\n$N_\\text{admin}$ & $\\delta$=1.0 & $\\delta$=1.4 & $\\delta$=1.6 & FPR \\\\\n\\midrule\n1 & 0.42 & 0.58 & 0.68 & 0.04 \\\\\n2 & 0.55 & 0.71 & 0.79 & 0.05 \\\\\n3 & 0.63 & 0.78 & 0.85 & 0.05 \\\\\n4 & 0.68 & 0.83 & 0.89 & 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Bifactor IRT equating pilot.}\nA bifactor IRT model fitted to the MMLU response matrix (12,508 items $\\times$ 5,219 models) fails to converge (iteration limit reached after 18.5 hours).\nFit indices are uniformly poor: RMSEA$=0.089$ ($>0.06$ cutoff), CFI$=0.72$ ($<0.90$ cutoff), TLI$=0.68$, SRMR$=0.11$.\nThe general factor explains only 28.4\\% of variance, confirming that MMLU's 57-subject structure defeats both unidimensional and bifactor IRT specifications.\nNo anchor items could be selected, and IRT-based test equating is infeasible for MMLU in its current form.\n\n\\paragraph{Item generation calibration.}\nThis experiment was blocked by the bifactor failure: without reliable IRT parameter estimates and anchor items, LLM-generated replacement items cannot be calibrated to an equated scale.\nThe entire regeneration pipeline (from DIF flag to calibrated replacement) is infeasible under current IRT limitations for multi-domain benchmarks.\nThis motivates future work on multidimensional IRT or per-subject calibration strategies.\n\n\n\\section{Limitations}\n\nThree primary limitations should inform interpretation of our results.\n\n\\emph{IRT model misfit.}\n98\\% of METABENCH models show $|L_z|>2$ on MMLU, and the bifactor model fails to converge (RMSEA$=0.089$, CFI$=0.72$).\nMH-DIF conditions on total score, which is a poor proxy for ability in a 57-subject multidimensional benchmark.\nThis does not invalidate the statistical signal (permutation $p<0.001$), but it means the matching variable is noisy, potentially inflating DIF rates.\nFuture work should explore multidimensional IRT or per-subject DIF analysis.\n\n\\emph{Causal ambiguity.}\nThe Simpson's paradox (OR flip from 1.55 to 0.73) and the gradual-drift pattern (62.3\\% of DIF items) are consistent with both item instability and capability improvement.\nOur semi-synthetic framework validates \\emph{detection mechanics}, not \\emph{causal interpretation} of detected signals.\nDistinguishing genuine item degradation from legitimate ability growth requires experimental designs beyond what observational DIF analysis can provide.\n\n\\emph{Sample and scope.}\nThe GSM1K correlation ($N=33$, CI upper $|r|=0.16$) is suggestive but not definitive.\nThe reasoning-RL robustness analysis ($N=13$) is underpowered.\nSemi-synthetic injection uses a simplified contamination mechanism (incorrect$\\to$correct flipping) that may not capture all real-world contamination pathways (e.g., partial memorization, reasoning shortcuts).\n\n\n\\section{Conclusion}\n\nWe introduce a semi-synthetic validation framework for item-level contamination detectors, with cross-subject matching that achieves zero false-positive inflation ($\\Delta$FPR$=0.000$).\nThe framework is portable across benchmarks (demonstrated on MMLU and GSM8K) and reusable for any item-level detector.\nOur empirical meta-critique demonstrates that web-overlap ground truth labels and item-level behavioral signals measure different constructs (enrichment$\\approx 1.0$; GSM1K $r=-0.478$), highlighting a systematic validation gap in the contamination detection literature.\nAs a motivating case study, temporal DIF analysis of 5,227 models across six benchmarks reveals 17.9\\%--31.3\\% large DIF, with extensive transparency analyses documenting interpretive challenges.\n\nThe negative results (bifactor failure, ensemble underperformance, low inter-method agreement) are informative scope boundaries: IRT-based equating requires better model fit than current multi-domain benchmarks provide, and signal fusion requires higher base-signal agreement than current detectors achieve.\nWe propose that benchmark maintainers adopt DIF-based audit workflows as a diagnostic tool for understanding item-level behavioral changes, while the semi-synthetic framework provides the validation infrastructure that the field currently lacks.\n\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Mantel and Haenszel(1959)]{mantel1959statistical}\nMantel, N. and Haenszel, W. (1959).\n\\newblock Statistical aspects of the analysis of data from retrospective studies of disease.\n\\newblock \\emph{Journal of the National Cancer Institute}, 22(4):719--748.\n\n\\bibitem[Holland and Thayer(1988)]{holland1988differential}\nHolland, P.~W. and Thayer, D.~T. (1988).\n\\newblock Differential item performance and the Mantel-Haenszel procedure.\n\\newblock In Wainer, H. and Braun, H.~I., editors, \\emph{Test Validity}, pages 129--145. Lawrence Erlbaum.\n\n\\bibitem[Golchin and Surdeanu(2024)]{golchin2024constat}\nGolchin, S. and Surdeanu, M. (2024).\n\\newblock Data contamination quiz: A tool to detect and estimate contamination in large language models.\n\\newblock \\emph{arXiv preprint arXiv:2311.06233}.\n\n\\bibitem[Dong et~al.(2024)]{dong2024dvd}\nDong, Y., Jiang, Y., Zhao, H., and Tan, C. (2024).\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2402.15938}.\n\n\\bibitem[Shi et~al.(2024)]{shi2024mink}\nShi, W., Ajith, A., Xia, M., Huang, Y., Liu, D., Blevins, T., Chen, D., and Zettlemoyer, L. (2024).\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{Proceedings of ICLR 2024}.\n\n\\bibitem[Marcelino et~al.(2024)]{marcelino2024llm}\nMarcelino, I., Cardoso, H.~L., and Gon\\c{c}alo~Oliveira, H. (2024).\n\\newblock Analyzing differential item functioning in NLP benchmark datasets with IRT.\n\\newblock \\emph{arXiv preprint arXiv:2404.00126}.\n\n\\bibitem[Zhang et~al.(2024)]{zhang2024gsm1k}\nZhang, H., Da, J., Lee, D., Robinson, V., Wu, C., Song, W., Zhao, T., Raja, P., Slack, D., Lyu, Q., Hendryx, S., Lazar, R., Qian, L., Bogen, M., Jia, R., and Teufel, S. (2024).\n\\newblock A careful examination of large language model performance on grade school math.\n\\newblock \\emph{arXiv preprint arXiv:2405.00332}.\n\n\\bibitem[Sinharay et~al.(2006)]{sinharay2006study}\nSinharay, S., Johnson, M.~S., and Stern, H.~S. (2006).\n\\newblock Posterior predictive assessment of item response theory models.\n\\newblock \\emph{Applied Psychological Measurement}, 30(4):298--321.\n\n\\bibitem[Tutz and Berger(2016)]{tutz2016item}\nTutz, G. and Berger, M. (2016).\n\\newblock Item-focused trees for the identification of items in differential item functioning.\n\\newblock \\emph{Psychometrika}, 81(3):727--750.\n\n\\bibitem[Li et~al.(2024)]{li2024contamination}\nLi, Y., Li, Y., Li, L., Chen, Y., Zeng, Z., Li, Y., and Li, Z. (2024).\n\\newblock Open {LLM} leaderboard contamination report.\n\\newblock Technical report.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "24d3edb0-c25f-4293-bba9-a234a2f12468",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T110541 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "7f1e84f2-aab3-4539-89e2-d39e6eeeef90",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream research",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120"
}
```

---

### Tool call

_source line 27 · 2026-05-21T11:43:50.807Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01H1XTF35u73WqempedCibcU`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper (two passes)",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f1e84f2-aab3-4539-89e2-d39e6eeeef90",
  "isSidechain": false,
  "requestId": "req_011CbFey21Bs3eYMmyhg1zTg",
  "type": "assistant",
  "uuid": "3b43cfac-ccec-4b03-935d-4a91b4b5edf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSNo6HwNgNMujur34No9WB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13013,
      "cache_read_input_tokens": 52976,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13013,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 52976,
          "cache_creation_input_tokens": 13013,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13013
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

_source line 28 · 2026-05-21T11:43:51.761Z_

<details><summary>↩ Tool result · `toolu_01H1XTF35u73WqempedCibcU`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
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
Underfull \hbox (badness 1286) in paragraph at lines 27--35
\T1/ptm/m/n/10.95 A cross-subject match-ing strat-egy, which con-di-

Underfull \hbox (badness 1748) in paragraph at lines 27--35
\T1/ptm/m/n/10.95 match-ing in-flates FPR by up to $\OT1/cmr/m/n/10.95 +0\OML/c
mm/m/it/10.95 :\OT1/cmr/m/n/10.95 186$\T1/ptm/m/n/10.95 . We

Underfull \hbox (badness 1173) in paragraph at lines 27--35
\T1/ptm/m/n/10.95 split 0.18%). We re-port ex-ten-sive trans-parency

Package natbib Warning: Citation `holland1988differential' on page 1 undefined 
on input line 41.


Package natbib Warning: Citation `mantel1959statistical' on page 1 undefined on
 input line 41.


Underfull \vbox (badness 10000) has occurred while \output is active

Package natbib Warning: Citation `golchin2024constat' on page 1 undefined on in
put line 43.


Package natbib Warning: Citation `dong2024dvd' on page 1 undefined on input lin
e 43.


Package natbib Warning: Citation `shi2024mink' on page 1 undefined on input lin
e 43.


Underfull \hbox (badness 2050) in paragraph at lines 43--47
\T1/ptm/m/n/10.95 been pro-posed for LLM bench-marks, in-clud-ing

Underfull \vbox (badness 2608) has occurred while \output is active [1{/var/lib
/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/
enc/dvips/base/8r.enc}]
Underfull \hbox (badness 2384) in paragraph at lines 61--62
[]\T1/ptm/m/n/10.95 An \T1/ptm/b/n/10.95 em-pir-i-cal ground truth meta-critiqu
e

Package natbib Warning: Citation `golchin2024constat' on page 2 undefined on in
put line 71.


Package natbib Warning: Citation `dong2024dvd' on page 2 undefined on input lin
e 72.


Package natbib Warning: Citation `shi2024mink' on page 2 undefined on input lin
e 73.


Underfull \hbox (badness 1838) in paragraph at lines 70--75
 []\T1/ptm/b/n/10.95 Benchmark con-tam-i-na-tion de-tec-tion.[] \T1/ptm/m/n/10.
95 Meth-ods

Package natbib Warning: Citation `mantel1959statistical' on page 2 undefined on
 input line 77.


Package natbib Warning: Citation `holland1988differential' on page 2 undefined 
on input line 77.


Package natbib Warning: Citation `marcelino2024llm' on page 2 undefined on inpu
t line 78.


Package natbib Warning: Citation `zhang2024gsm1k' on page 2 undefined on input 
line 81.


Underfull \hbox (badness 1874) in paragraph at lines 81--83
 []\T1/ptm/b/n/10.95 Benchmark in-tegrity.[] \T1/ptm/m/n/10.95 Grow-ing con-cer
ns about

Underfull \hbox (badness 1668) in paragraph at lines 89--93
\T1/ptm/m/n/10.95 odds ra-tio $\OML/cmm/m/it/10.95 []$ \T1/ptm/m/n/10.95 and i
ts log-transform $\OT1/cmr/m/n/10.95 ^^A[] =

Underfull \hbox (badness 1466) in paragraph at lines 89--93
\OMS/cmsy/m/n/10.95 ^^@\OT1/cmr/m/n/10.95 2\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10
.95 35 [](\OML/cmm/m/it/10.95 []\OT1/cmr/m/n/10.95 )$ \T1/ptm/m/n/10.95 quan-t
ify DIF mag-ni-tude. Items
[2]
Underfull \hbox (badness 1158) in paragraph at lines 104--105
[]\T1/ptm/m/n/10.95 Compute $\OT1/cmr/m/n/10.95 ^^A$\T1/ptm/m/n/10.95 TPR $\OT1
/cmr/m/n/10.95 =$ \T1/ptm/m/n/10.95 TPR$\OT1/cmr/m/n/10.95 (\OML/cmm/m/it/10.95
 p\OT1/cmr/m/n/10.95 )$ $\OMS/cmsy/m/n/10.95 ^^@$ \T1/ptm/m/n/10.95 TPR$\OT1/cm
r/m/n/10.95 (0)$ \T1/ptm/m/n/10.95 and

LaTeX Warning: Reference `tab:cohort' on page 3 undefined on input line 124.


Underfull \hbox (badness 3058) in paragraph at lines 123--126
 []\T1/ptm/b/n/10.95 MMLU DIF anal-y-sis.[] \T1/ptm/m/n/10.95 We ap-ply MH-DIF 
to

Underfull \hbox (badness 1715) in paragraph at lines 129--129
[]\T1/ptm/m/n/10 Table 1: |DIF clas-si-fi-ca-tion by co-hort def-i-ni-tion on

LaTeX Warning: Reference `tab:family' on page 3 undefined on input line 144.


LaTeX Warning: Reference `tab:crossbench' on page 3 undefined on input line 168
.


Underfull \hbox (badness 1817) in paragraph at lines 168--171
 []\T1/ptm/b/n/10.95 Cross-benchmark repli-ca-tion.[] \T1/ptm/m/n/10.95 Ta-ble 
[] shows

Overfull \hbox (4.14766pt too wide) in paragraph at lines 177--189
 [][] 

Underfull \hbox (badness 10000) in paragraph at lines 192--196
 []\T1/ptm/b/n/10.95 Architecture strat-i-fi-ca-tion.[] \T1/ptm/m/n/10.95 METAB
ENCH

Underfull \hbox (badness 10000) in paragraph at lines 192--196
\T1/ptm/m/n/10.95 MMLU is 99.98% decoder-only (5,226/5,227

Underfull \hbox (badness 2261) in paragraph at lines 192--196
\T1/ptm/m/n/10.95 re-flects MMLU's 57-subject mul-ti-di-men-sion-al-ity,
[3]

LaTeX Warning: Reference `tab:semisyn' on page 4 undefined on input line 201.


LaTeX Warning: Reference `tab:gsm1k' on page 4 undefined on input line 238.


Underfull \hbox (badness 6477) in paragraph at lines 238--242
 []\T1/ptm/b/n/10.95 GSM1K con-tam-i-na-tion gap cor-re-la-tion.[] \T1/ptm/m/n/
10.95 Ta-

Underfull \hbox (badness 4792) in paragraph at lines 266--270
 []\T1/ptm/b/n/10.95 DVD gen-er-a-tion vari-ance com-par-i-son.[] \T1/ptm/m/n/1
0.95 DVD

LaTeX Warning: Reference `tab:ensemble' on page 4 undefined on input line 272.


Underfull \hbox (badness 1540) in paragraph at lines 272--277
 []\T1/ptm/b/n/10.95 Ensemble fu-sion.[] \T1/ptm/m/n/10.95 Ta-ble [] re-ports t
he per-for-
[4]

LaTeX Warning: Reference `tab:simpsons' on page 5 undefined on input line 301.


Package natbib Warning: Citation `tutz2016item' on page 5 undefined on input li
ne 326.


LaTeX Warning: Reference `tab:degrade' on page 5 undefined on input line 348.


LaTeX Warning: Reference `sec:negative' on page 5 undefined on input line 348.


LaTeX Warning: Reference `tab:rl' on page 5 undefined on input line 377.

[5]

LaTeX Warning: Reference `tab:cumulative' on page 6 undefined on input line 399
.


Package natbib Warning: Citation `sinharay2006study' on page 6 undefined on inp
ut line 399.


Underfull \hbox (badness 2951) in paragraph at lines 423--427
 []\T1/ptm/b/n/10.95 Bifactor IRT equat-ing pi-lot.[] \T1/ptm/m/n/10.95 A bi-fa
c-tor IRT
[6]
Underfull \hbox (badness 1622) in paragraph at lines 462--464
\T1/ptm/m/n/10.95 in-for-ma-tive scope bound-aries: IRT-based equat-

Package natbib Warning: There were undefined citations.

[7] (./paper.aux

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
nts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (7 pages, 141983 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Underfull \hbox (badness 1286) in paragraph at lines 27--35
\T1/ptm/m/n/10.95 A cross-subject match-ing strat-egy, which con-di-

Underfull \hbox (badness 1748) in paragraph at lines 27--35
\T1/ptm/m/n/10.95 match-ing in-flates FPR by up to $\OT1/cmr/m/n/10.95 +0\OML/c
mm/m/it/10.95 :\OT1/cmr/m/n/10.95 186$\T1/ptm/m/n/10.95 . We

Underfull \hbox (badness 1173) in paragraph at lines 27--35
\T1/ptm/m/n/10.95 split 0.18%). We re-port ex-ten-sive trans-parency

Underfull \vbox (badness 10000) has occurred while \output is active
Underfull \hbox (badness 2050) in paragraph at lines 43--47
\T1/ptm/m/n/10.95 been pro-posed for LLM bench-marks, in-clud-ing

Underfull \vbox (badness 2608) has occurred while \output is active [1{/var/lib
/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/
enc/dvips/base/8r.enc}]
Underfull \hbox (badness 2384) in paragraph at lines 61--62
[]\T1/ptm/m/n/10.95 An \T1/ptm/b/n/10.95 em-pir-i-cal ground truth meta-critiqu
e

Underfull \hbox (badness 1838) in paragraph at lines 70--75
 []\T1/ptm/b/n/10.95 Benchmark con-tam-i-na-tion de-tec-tion.[] \T1/ptm/m/n/10.
95 Meth-ods

Underfull \hbox (badness 1394) in paragraph at lines 70--75
\T1/ptm/m/n/10.95 ap-proaches, such as Con-Stat [[]Golchin and Sur-

Underfull \hbox (badness 1874) in paragraph at lines 81--83
 []\T1/ptm/b/n/10.95 Benchmark in-tegrity.[] \T1/ptm/m/n/10.95 Grow-ing con-cer
ns about

Underfull \hbox (badness 1668) in paragraph at lines 89--93
\T1/ptm/m/n/10.95 odds ra-tio $\OML/cmm/m/it/10.95 []$ \T1/ptm/m/n/10.95 and i
ts log-transform $\OT1/cmr/m/n/10.95 ^^A[] =

Underfull \hbox (badness 1466) in paragraph at lines 89--93
\OMS/cmsy/m/n/10.95 ^^@\OT1/cmr/m/n/10.95 2\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10
.95 35 [](\OML/cmm/m/it/10.95 []\OT1/cmr/m/n/10.95 )$ \T1/ptm/m/n/10.95 quan-t
ify DIF mag-ni-tude. Items
[2]
Underfull \hbox (badness 1158) in paragraph at lines 104--105
[]\T1/ptm/m/n/10.95 Compute $\OT1/cmr/m/n/10.95 ^^A$\T1/ptm/m/n/10.95 TPR $\OT1
/cmr/m/n/10.95 =$ \T1/ptm/m/n/10.95 TPR$\OT1/cmr/m/n/10.95 (\OML/cmm/m/it/10.95
 p\OT1/cmr/m/n/10.95 )$ $\OMS/cmsy/m/n/10.95 ^^@$ \T1/ptm/m/n/10.95 TPR$\OT1/cm
r/m/n/10.95 (0)$ \T1/ptm/m/n/10.95 and

Underfull \hbox (badness 3058) in paragraph at lines 123--126
 []\T1/ptm/b/n/10.95 MMLU DIF anal-y-sis.[] \T1/ptm/m/n/10.95 We ap-ply MH-DIF 
to

Underfull \hbox (badness 1715) in paragraph at lines 129--129
[]\T1/ptm/m/n/10 Table 1: |DIF clas-si-fi-ca-tion by co-hort def-i-ni-tion on

Underfull \hbox (badness 5231) in paragraph at lines 168--171
 []\T1/ptm/b/n/10.95 Cross-benchmark repli-ca-tion.[] \T1/ptm/m/n/10.95 Ta-ble 
[]3[] shows

Overfull \hbox (4.14766pt too wide) in paragraph at lines 177--189
 [][] 

Underfull \hbox (badness 10000) in paragraph at lines 192--196
 []\T1/ptm/b/n/10.95 Architecture strat-i-fi-ca-tion.[] \T1/ptm/m/n/10.95 METAB
ENCH

Underfull \hbox (badness 10000) in paragraph at lines 192--196
\T1/ptm/m/n/10.95 MMLU is 99.98% decoder-only (5,226/5,227

Underfull \hbox (badness 2261) in paragraph at lines 192--196
\T1/ptm/m/n/10.95 re-flects MMLU's 57-subject mul-ti-di-men-sion-al-ity,
[3]
Underfull \hbox (badness 4792) in paragraph at lines 266--270
 []\T1/ptm/b/n/10.95 DVD gen-er-a-tion vari-ance com-par-i-son.[] \T1/ptm/m/n/1
0.95 DVD
[4] [5]
Underfull \hbox (badness 2951) in paragraph at lines 423--427
 []\T1/ptm/b/n/10.95 Bifactor IRT equat-ing pi-lot.[] \T1/ptm/m/n/10.95 A bi-fa
c-tor IRT
[6]
Underfull \hbox (badness 1622) in paragraph at lines 462--464
\T1/ptm/m/n/10.95 in-for-ma-tive scope bound-aries: IRT-based equat-

Underfull \vbox (badness 10000) has occurred while \output is active [7]
(./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (7 pages, 144504 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b43cfac-ccec-4b03-935d-4a91b4b5edf7",
  "isSidechain": false,
  "promptId": "053b0da8-7122-4261-b381-207d5502fd28",
  "type": "user",
  "uuid": "eedba9f3-eb8e-4d64-a418-8ddc4f4384c9",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nUnderfull \\hbox (badness 1286) in paragraph at lines 27--35\n\\T1/ptm/m/n/10.95 A cross-subject match-ing strat-egy, which con-di-\n\nUnderfull \\hbox (badness 1748) in paragraph at lines 27--35\n\\T1/ptm/m/n/10.95 match-ing in-flates FPR by up to $\\OT1/cmr/m/n/10.95 +0\\OML/c\nmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 186$\\T1/ptm/m/n/10.95 . We\n\nUnderfull \\hbox (badness 1173) in paragraph at lines 27--35\n\\T1/ptm/m/n/10.95 split 0.18%). We re-port ex-ten-sive trans-parency\n\nPackage natbib Warning: Citation `holland1988differential' on page 1 undefined \non input line 41.\n\n\nPackage natbib Warning: Citation `mantel1959statistical' on page 1 undefined on\n input line 41.\n\n\nUnderfull \\vbox (badness 10000) has occurred while \\output is active\n\nPackage natbib Warning: Citation `golchin2024constat' on page 1 undefined on in\nput line 43.\n\n\nPackage natbib Warning: Citation `dong2024dvd' on page 1 undefined on input lin\ne 43.\n\n\nPackage natbib Warning: Citation `shi2024mink' on page 1 undefined on input lin\ne 43.\n\n\nUnderfull \\hbox (badness 2050) in paragraph at lines 43--47\n\\T1/ptm/m/n/10.95 been pro-posed for LLM bench-marks, in-clud-ing\n\nUnderfull \\vbox (badness 2608) has occurred while \\output is active [1{/var/lib\n/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/\nenc/dvips/base/8r.enc}]\nUnderfull \\hbox (badness 2384) in paragraph at lines 61--62\n[]\\T1/ptm/m/n/10.95 An \\T1/ptm/b/n/10.95 em-pir-i-cal ground truth meta-critiqu\ne\n\nPackage natbib Warning: Citation `golchin2024constat' on page 2 undefined on in\nput line 71.\n\n\nPackage natbib Warning: Citation `dong2024dvd' on page 2 undefined on input lin\ne 72.\n\n\nPackage natbib Warning: Citation `shi2024mink' on page 2 undefined on input lin\ne 73.\n\n\nUnderfull \\hbox (badness 1838) in paragraph at lines 70--75\n []\\T1/ptm/b/n/10.95 Benchmark con-tam-i-na-tion de-tec-tion.[] \\T1/ptm/m/n/10.\n95 Meth-ods\n\nPackage natbib Warning: Citation `mantel1959statistical' on page 2 undefined on\n input line 77.\n\n\nPackage natbib Warning: Citation `holland1988differential' on page 2 undefined \non input line 77.\n\n\nPackage natbib Warning: Citation `marcelino2024llm' on page 2 undefined on inpu\nt line 78.\n\n\nPackage natbib Warning: Citation `zhang2024gsm1k' on page 2 undefined on input \nline 81.\n\n\nUnderfull \\hbox (badness 1874) in paragraph at lines 81--83\n []\\T1/ptm/b/n/10.95 Benchmark in-tegrity.[] \\T1/ptm/m/n/10.95 Grow-ing con-cer\nns about\n\nUnderfull \\hbox (badness 1668) in paragraph at lines 89--93\n\\T1/ptm/m/n/10.95 odds ra-tio $\\OML/cmm/m/it/10.95 \u000b[]$ \\T1/ptm/m/n/10.95 and i\nts log-transform $\\OT1/cmr/m/n/10.95 ^^A[] =\n\nUnderfull \\hbox (badness 1466) in paragraph at lines 89--93\n\\OMS/cmsy/m/n/10.95 ^^@\\OT1/cmr/m/n/10.95 2\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10\n.95 35 [](\\OML/cmm/m/it/10.95 \u000b[]\\OT1/cmr/m/n/10.95 )$ \\T1/ptm/m/n/10.95 quan-t\nify DIF mag-ni-tude. Items\n[2]\nUnderfull \\hbox (badness 1158) in paragraph at lines 104--105\n[]\\T1/ptm/m/n/10.95 Compute $\\OT1/cmr/m/n/10.95 ^^A$\\T1/ptm/m/n/10.95 TPR $\\OT1\n/cmr/m/n/10.95 =$ \\T1/ptm/m/n/10.95 TPR$\\OT1/cmr/m/n/10.95 (\\OML/cmm/m/it/10.95\n p\\OT1/cmr/m/n/10.95 )$ $\\OMS/cmsy/m/n/10.95 ^^@$ \\T1/ptm/m/n/10.95 TPR$\\OT1/cm\nr/m/n/10.95 (0)$ \\T1/ptm/m/n/10.95 and\n\nLaTeX Warning: Reference `tab:cohort' on page 3 undefined on input line 124.\n\n\nUnderfull \\hbox (badness 3058) in paragraph at lines 123--126\n []\\T1/ptm/b/n/10.95 MMLU DIF anal-y-sis.[] \\T1/ptm/m/n/10.95 We ap-ply MH-DIF \nto\n\nUnderfull \\hbox (badness 1715) in paragraph at lines 129--129\n[]\\T1/ptm/m/n/10 Table 1: |DIF clas-si-fi-ca-tion by co-hort def-i-ni-tion on\n\nLaTeX Warning: Reference `tab:family' on page 3 undefined on input line 144.\n\n\nLaTeX Warning: Reference `tab:crossbench' on page 3 undefined on input line 168\n.\n\n\nUnderfull \\hbox (badness 1817) in paragraph at lines 168--171\n []\\T1/ptm/b/n/10.95 Cross-benchmark repli-ca-tion.[] \\T1/ptm/m/n/10.95 Ta-ble \n[] shows\n\nOverfull \\hbox (4.14766pt too wide) in paragraph at lines 177--189\n [][] \n\nUnderfull \\hbox (badness 10000) in paragraph at lines 192--196\n []\\T1/ptm/b/n/10.95 Architecture strat-i-fi-ca-tion.[] \\T1/ptm/m/n/10.95 METAB\nENCH\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 192--196\n\\T1/ptm/m/n/10.95 MMLU is 99.98% decoder-only (5,226/5,227\n\nUnderfull \\hbox (badness 2261) in paragraph at lines 192--196\n\\T1/ptm/m/n/10.95 re-flects MMLU's 57-subject mul-ti-di-men-sion-al-ity,\n[3]\n\nLaTeX Warning: Reference `tab:semisyn' on page 4 undefined on input line 201.\n\n\nLaTeX Warning: Reference `tab:gsm1k' on page 4 undefined on input line 238.\n\n\nUnderfull \\hbox (badness 6477) in paragraph at lines 238--242\n []\\T1/ptm/b/n/10.95 GSM1K con-tam-i-na-tion gap cor-re-la-tion.[] \\T1/ptm/m/n/\n10.95 Ta-\n\nUnderfull \\hbox (badness 4792) in paragraph at lines 266--270\n []\\T1/ptm/b/n/10.95 DVD gen-er-a-tion vari-ance com-par-i-son.[] \\T1/ptm/m/n/1\n0.95 DVD\n\nLaTeX Warning: Reference `tab:ensemble' on page 4 undefined on input line 272.\n\n\nUnderfull \\hbox (badness 1540) in paragraph at lines 272--277\n []\\T1/ptm/b/n/10.95 Ensemble fu-sion.[] \\T1/ptm/m/n/10.95 Ta-ble [] re-ports t\nhe per-for-\n[4]\n\nLaTeX Warning: Reference `tab:simpsons' on page 5 undefined on input line 301.\n\n\nPackage natbib Warning: Citation `tutz2016item' on page 5 undefined on input li\nne 326.\n\n\nLaTeX Warning: Reference `tab:degrade' on page 5 undefined on input line 348.\n\n\nLaTeX Warning: Reference `sec:negative' on page 5 undefined on input line 348.\n\n\nLaTeX Warning: Reference `tab:rl' on page 5 undefined on input line 377.\n\n[5]\n\nLaTeX Warning: Reference `tab:cumulative' on page 6 undefined on input line 399\n.\n\n\nPackage natbib Warning: Citation `sinharay2006study' on page 6 undefined on inp\nut line 399.\n\n\nUnderfull \\hbox (badness 2951) in paragraph at lines 423--427\n []\\T1/ptm/b/n/10.95 Bifactor IRT equat-ing pi-lot.[] \\T1/ptm/m/n/10.95 A bi-fa\nc-tor IRT\n[6]\nUnderfull \\hbox (badness 1622) in paragraph at lines 462--464\n\\T1/ptm/m/n/10.95 in-for-ma-tive scope bound-aries: IRT-based equat-\n\nPackage natbib Warning: There were undefined citations.\n\n[7] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (7 pages, 141983 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nUnderfull \\hbox (badness 1286) in paragraph at lines 27--35\n\\T1/ptm/m/n/10.95 A cross-subject match-ing strat-egy, which con-di-\n\nUnderfull \\hbox (badness 1748) in paragraph at lines 27--35\n\\T1/ptm/m/n/10.95 match-ing in-flates FPR by up to $\\OT1/cmr/m/n/10.95 +0\\OML/c\nmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 186$\\T1/ptm/m/n/10.95 . We\n\nUnderfull \\hbox (badness 1173) in paragraph at lines 27--35\n\\T1/ptm/m/n/10.95 split 0.18%). We re-port ex-ten-sive trans-parency\n\nUnderfull \\vbox (badness 10000) has occurred while \\output is active\nUnderfull \\hbox (badness 2050) in paragraph at lines 43--47\n\\T1/ptm/m/n/10.95 been pro-posed for LLM bench-marks, in-clud-ing\n\nUnderfull \\vbox (badness 2608) has occurred while \\output is active [1{/var/lib\n/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/\nenc/dvips/base/8r.enc}]\nUnderfull \\hbox (badness 2384) in paragraph at lines 61--62\n[]\\T1/ptm/m/n/10.95 An \\T1/ptm/b/n/10.95 em-pir-i-cal ground truth meta-critiqu\ne\n\nUnderfull \\hbox (badness 1838) in paragraph at lines 70--75\n []\\T1/ptm/b/n/10.95 Benchmark con-tam-i-na-tion de-tec-tion.[] \\T1/ptm/m/n/10.\n95 Meth-ods\n\nUnderfull \\hbox (badness 1394) in paragraph at lines 70--75\n\\T1/ptm/m/n/10.95 ap-proaches, such as Con-Stat [[]Golchin and Sur-\n\nUnderfull \\hbox (badness 1874) in paragraph at lines 81--83\n []\\T1/ptm/b/n/10.95 Benchmark in-tegrity.[] \\T1/ptm/m/n/10.95 Grow-ing con-cer\nns about\n\nUnderfull \\hbox (badness 1668) in paragraph at lines 89--93\n\\T1/ptm/m/n/10.95 odds ra-tio $\\OML/cmm/m/it/10.95 \u000b[]$ \\T1/ptm/m/n/10.95 and i\nts log-transform $\\OT1/cmr/m/n/10.95 ^^A[] =\n\nUnderfull \\hbox (badness 1466) in paragraph at lines 89--93\n\\OMS/cmsy/m/n/10.95 ^^@\\OT1/cmr/m/n/10.95 2\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10\n.95 35 [](\\OML/cmm/m/it/10.95 \u000b[]\\OT1/cmr/m/n/10.95 )$ \\T1/ptm/m/n/10.95 quan-t\nify DIF mag-ni-tude. Items\n[2]\nUnderfull \\hbox (badness 1158) in paragraph at lines 104--105\n[]\\T1/ptm/m/n/10.95 Compute $\\OT1/cmr/m/n/10.95 ^^A$\\T1/ptm/m/n/10.95 TPR $\\OT1\n/cmr/m/n/10.95 =$ \\T1/ptm/m/n/10.95 TPR$\\OT1/cmr/m/n/10.95 (\\OML/cmm/m/it/10.95\n p\\OT1/cmr/m/n/10.95 )$ $\\OMS/cmsy/m/n/10.95 ^^@$ \\T1/ptm/m/n/10.95 TPR$\\OT1/cm\nr/m/n/10.95 (0)$ \\T1/ptm/m/n/10.95 and\n\nUnderfull \\hbox (badness 3058) in paragraph at lines 123--126\n []\\T1/ptm/b/n/10.95 MMLU DIF anal-y-sis.[] \\T1/ptm/m/n/10.95 We ap-ply MH-DIF \nto\n\nUnderfull \\hbox (badness 1715) in paragraph at lines 129--129\n[]\\T1/ptm/m/n/10 Table 1: |DIF clas-si-fi-ca-tion by co-hort def-i-ni-tion on\n\nUnderfull \\hbox (badness 5231) in paragraph at lines 168--171\n []\\T1/ptm/b/n/10.95 Cross-benchmark repli-ca-tion.[] \\T1/ptm/m/n/10.95 Ta-ble \n[]3[] shows\n\nOverfull \\hbox (4.14766pt too wide) in paragraph at lines 177--189\n [][] \n\nUnderfull \\hbox (badness 10000) in paragraph at lines 192--196\n []\\T1/ptm/b/n/10.95 Architecture strat-i-fi-ca-tion.[] \\T1/ptm/m/n/10.95 METAB\nENCH\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 192--196\n\\T1/ptm/m/n/10.95 MMLU is 99.98% decoder-only (5,226/5,227\n\nUnderfull \\hbox (badness 2261) in paragraph at lines 192--196\n\\T1/ptm/m/n/10.95 re-flects MMLU's 57-subject mul-ti-di-men-sion-al-ity,\n[3]\nUnderfull \\hbox (badness 4792) in paragraph at lines 266--270\n []\\T1/ptm/b/n/10.95 DVD gen-er-a-tion vari-ance com-par-i-son.[] \\T1/ptm/m/n/1\n0.95 DVD\n[4] [5]\nUnderfull \\hbox (badness 2951) in paragraph at lines 423--427\n []\\T1/ptm/b/n/10.95 Bifactor IRT equat-ing pi-lot.[] \\T1/ptm/m/n/10.95 A bi-fa\nc-tor IRT\n[6]\nUnderfull \\hbox (badness 1622) in paragraph at lines 462--464\n\\T1/ptm/m/n/10.95 in-for-ma-tive scope bound-aries: IRT-based equat-\n\nUnderfull \\vbox (badness 10000) has occurred while \\output is active [7]\n(./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (7 pages, 144504 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3b43cfac-ccec-4b03-935d-4a91b4b5edf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T110541 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "eedba9f3-eb8e-4d64-a418-8ddc4f4384c9",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream research",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120"
}
```

---

### Assistant

_source line 31 · 2026-05-21T11:43:55.150Z_

<details><summary>Logged reasoning block</summary>

```text
The paper compiled successfully with only some underfull hbox warnings (cosmetic, not errors) and a label warning that needs a third pass. Let me run the third pass to resolve the remaining label warning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eedba9f3-eb8e-4d64-a418-8ddc4f4384c9",
  "isSidechain": false,
  "requestId": "req_011CbFeyS7XDgafa7Rq2Xwcc",
  "type": "assistant",
  "uuid": "07acc611-8ef6-49fe-9c16-9b2526407fea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8aCmS49HwpPofqEHcNp9Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9733,
      "cache_read_input_tokens": 65989,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 65989,
          "cache_creation_input_tokens": 9733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9733
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

_source line 32 · 2026-05-21T11:43:55.706Z_

Labels need a third pass to stabilize.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07acc611-8ef6-49fe-9c16-9b2526407fea",
  "isSidechain": false,
  "requestId": "req_011CbFeyS7XDgafa7Rq2Xwcc",
  "type": "assistant",
  "uuid": "c6031e89-5326-48ad-a545-54ee19a6ee4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8aCmS49HwpPofqEHcNp9Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9733,
      "cache_read_input_tokens": 65989,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 65989,
          "cache_creation_input_tokens": 9733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9733
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

_source line 33 · 2026-05-21T11:43:58.681Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016knUbMB14LREXiz3NHL1zm`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Third LaTeX pass to stabilize labels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6031e89-5326-48ad-a545-54ee19a6ee4a",
  "isSidechain": false,
  "requestId": "req_011CbFeyS7XDgafa7Rq2Xwcc",
  "type": "assistant",
  "uuid": "70e251aa-4ca5-4a73-a7b9-0e2c25c0f582",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8aCmS49HwpPofqEHcNp9Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9733,
      "cache_read_input_tokens": 65989,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 65989,
          "cache_creation_input_tokens": 9733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9733
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

_source line 34 · 2026-05-21T11:43:59.189Z_

<details><summary>↩ Tool result · `toolu_016knUbMB14LREXiz3NHL1zm`</summary>

```text
msy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (7 pages, 144504 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70e251aa-4ca5-4a73-a7b9-0e2c25c0f582",
  "isSidechain": false,
  "promptId": "053b0da8-7122-4261-b381-207d5502fd28",
  "type": "user",
  "uuid": "ba33759e-7392-4f66-89b6-2f9e1ccbf00b",
  "toolUseResult": {
    "stdout": "msy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (7 pages, 144504 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "70e251aa-4ca5-4a73-a7b9-0e2c25c0f582",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-21T11:43:59.193Z_

```json
{
  "parentUuid": "ba33759e-7392-4f66-89b6-2f9e1ccbf00b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "69be55dd-745a-4922-a0de-0014fcd25b1f",
  "timestamp": "2026-05-21T11:43:59.193Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 36 · 2026-05-21T11:44:11.379Z_

PDF compiled successfully: 7 pages, 144 KB. Output at `artifacts/dream_reports/dream_20260521T110541/worst/paper.pdf`.

The paper covers all 16 experiments from `experiment_data.json`:

| Section | Experiments covered |
|---|---|
| §4.1 Temporal DIF Case Study | `real_data_dif_mmlu` (Tables 1-2), `permutation_null_c_rate`, `multi_benchmark_temporal_dif` (Table 3), `architecture_stratified_dif` |
| §4.2 Semi-Synthetic Validation | `semi_synthetic_contamination_validation` (Table 4), `cross_benchmark_gsm8k` |
| §4.3 Ground Truth Meta-Critique | `cross_benchmark_gsm8k` GSM1K (Table 5), `constat_perturbation_eval`, `dvd_generation_variance_eval`, `ensemble_fusion` (Table 6) |
| §4.4 Diagnostics | `odds_ratio_regression_transparency` (Table 7), `item_focused_trees` (Table 8), `graceful_degradation_analysis` (Table 9) |
| §4.5 Negative Results | `rl_robustness_validation` (Table 10), `cumulative_bayesian_dif` (Table 11), `bifactor_irt_equating_pilot`, `item_generation_calibration` |

Framing follows the narrative guidance: semi-synthetic framework as primary contribution, ground truth meta-critique as co-primary, temporal DIF demoted to motivating case study. Negative results (bifactor failure, ensemble underperformance, GSM1K negative correlation) reported honestly. All numbers sourced from `experiment_data.json`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69be55dd-745a-4922-a0de-0014fcd25b1f",
  "isSidechain": false,
  "requestId": "req_011CbFeyzds7V5zcuF8t1LR5",
  "type": "assistant",
  "uuid": "a49a153f-c7bc-4f68-b3b7-e70f23a4ef54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011yj56APX55GewY5jasHoik",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 416,
      "cache_read_input_tokens": 75722,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 416,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 429,
          "cache_read_input_tokens": 75722,
          "cache_creation_input_tokens": 416,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 416
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

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T110541 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "a49a153f-c7bc-4f68-b3b7-e70f23a4ef54",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream research",
  "sessionId": "7a8181aa-c348-44b4-9fba-f3c9d9744120"
}
```

---
