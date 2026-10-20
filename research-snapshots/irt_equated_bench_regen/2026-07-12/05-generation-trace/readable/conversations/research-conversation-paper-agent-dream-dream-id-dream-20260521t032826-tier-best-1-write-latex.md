# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032826 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/58b684cc-c924-4f8f-a187-ebf40a0af69c.jsonl`
- **Structured JSON:** [`5b68e4ffe00f2932d7ec.json`](../../sessions/5b/5b68e4ffe00f2932d7ec.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T03:46:03.322Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:46:03.322Z",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032826 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：All four claims hold as written. Lead with '28-30% instability persists in architecture-homogeneous decoder-only populations with good IRT fit (RMSEA=0.024)' — eliminates the strongest reviewer objection preemptively. Instability decomposition strengthens Claim 1 by showing partial ρ=0.22 (p=0.012) after controlling domain accuracy improvement — DIF captures genuine item function change beyond domain-level capability gains. Non-uniform DIF check confirms MH adequacy (78% overlap with SIBTEST). Paper runs the original framing: 'psychometric analysis reveals structural benchmark problems that existing contamination validation methodology cannot detect.' Architecture stratification (plan_010) and cross-benchmark GSM1K validation (plan_004, already done) are load-bearing complementary evidence. Strongest possible ICLR submission.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T03:46:03.327Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:46:03.327Z",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-21T03:46:03.352Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032826 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：All four claims hold as written. Lead with '28-30% instability persists in architecture-homogeneous decoder-only populations with good IRT fit (RMSEA=0.024)' — eliminates the strongest reviewer objection preemptively. Instability decomposition strengthens Claim 1 by showing partial ρ=0.22 (p=0.012) after controlling domain accuracy improvement — DIF captures genuine item function change beyond domain-level capability gains. Non-uniform DIF check confirms MH adequacy (78% overlap with SIBTEST). Paper runs the original framing: 'psychometric analysis reveals structural benchmark problems that existing contamination validation methodology cannot detect.' Architecture stratification (plan_010) and cross-benchmark GSM1K validation (plan_004, already done) are load-bearing complementary evidence. Strongest possible ICLR submission.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "3d7d344c-5c26-46b4-be58-beb97f0fe115",
  "type": "user",
  "uuid": "04d4cb62-6bf1-4e95-a2ce-0e659c9f5ef6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T03:46:03.351Z_

```json
{
  "parentUuid": "04d4cb62-6bf1-4e95-a2ce-0e659c9f5ef6",
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
  "uuid": "bde1f56d-818e-434b-a76f-5d69219d5cfc",
  "timestamp": "2026-05-21T03:46:03.351Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T03:46:03.351Z_

```json
{
  "parentUuid": "bde1f56d-818e-434b-a76f-5d69219d5cfc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "31fbc9ac-61c0-4780-9014-970392582542",
  "timestamp": "2026-05-21T03:46:03.351Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
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
  "aiTitle": "Generate paper on IRT benchmark instability analysis",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c"
}
```

---

### Assistant

_source line 7 · 2026-05-21T03:46:09.428Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the experiment data and paper framing files to understand what I'm working with.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31fbc9ac-61c0-4780-9014-970392582542",
  "isSidechain": false,
  "requestId": "req_011CbF2YAVXg9aimq63nzZ6i",
  "type": "assistant",
  "uuid": "ed75befa-3322-4352-835a-3c3e12592cb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016G4cyY7zoWXSjohwHMTVDD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11381,
      "cache_read_input_tokens": 11841,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11381,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 235,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11381
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

_source line 8 · 2026-05-21T03:46:09.961Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A8FesTieGMcLYDMTd1p9sD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed75befa-3322-4352-835a-3c3e12592cb1",
  "isSidechain": false,
  "requestId": "req_011CbF2YAVXg9aimq63nzZ6i",
  "type": "assistant",
  "uuid": "217b0464-99ae-429e-8f81-56e28267548b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016G4cyY7zoWXSjohwHMTVDD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11381,
      "cache_read_input_tokens": 11841,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11381,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 235,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11381
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

_source line 9 · 2026-05-21T03:46:10.403Z_

<details><summary>↩ Tool result · `toolu_01A8FesTieGMcLYDMTd1p9sD`</summary>

```text
1	[
2	  {
3	    "name": "architecture_stratified_dif",
4	    "description": "Run DIF within decoder-only subpopulation to test whether IRT model fit improves and temporal DIF persists when architecture heterogeneity is removed. Includes instability decomposition (partial ρ controlling domain accuracy) and non-uniform DIF robustness check (SIBTEST/logistic regression).\n",
5	    "results": {
6	      "decoder_only_n_models": 3487,
7	      "decoder_only_n_ref_2023": 892,
8	      "decoder_only_n_foc_2024h1": 513,
9	      "decoder_only_temporal_c_pct": 29.1,
10	      "decoder_only_sanity_random_c_pct": 0.14,
11	      "full_population_irt_rmsea": 0.067,
12	      "full_population_irt_cfi": 0.874,
13	      "decoder_only_irt_rmsea": 0.024,
14	      "decoder_only_irt_cfi": 0.966,
15	      "decoder_only_irt_tli": 0.958,
16	      "decoder_only_irt_srmr": 0.031,
17	      "rmsea_improvement_pct": 64.2,
18	      "cfi_improvement": 0.092,
19	      "full_vs_decoder_only_flag_jaccard": 0.71,
20	      "partial_rho_controlling_domain_accuracy": 0.22,
21	      "partial_rho_p_value": 0.012,
22	      "zero_order_rho_domain_accuracy": 0.307,
23	      "variance_explained_by_accuracy_alone": 9.4,
24	      "residual_instability_pct": 20.5,
25	      "non_uniform_sibtest_n_subjects_tested": 8,
26	      "non_uniform_sibtest_c_flags": 2814,
27	      "non_uniform_mh_c_flags": 3627,
28	      "non_uniform_mh_overlap_pct": 78,
29	      "non_uniform_only_sibtest_pct": 4.2,
30	      "non_uniform_only_mh_pct": 26.2,
31	      "logistic_regression_r2_interaction_median": 0.008
32	    },
33	    "tables": [
34	      {
35	        "title": "Table: IRT Fit Comparison — Full Population vs Decoder-Only",
36	        "columns": [
37	          "population",
38	          "n_models",
39	          "RMSEA",
40	          "CFI",
41	          "TLI",
42	          "SRMR",
43	          "temporal_C_pct"
44	        ],
45	        "rows": [
46	          [
47	            "full",
48	            5219,
49	            0.067,
50	            0.874,
51	            0.851,
52	            0.058,
53	            31.3
54	          ],
55	          [
56	            "decoder_only",
57	            3487,
58	            0.024,
59	            0.966,
60	            0.958,
61	            0.031,
62	            29.1
63	          ],
64	          [
65	            "encoder_decoder",
66	            412,
67	            0.041,
68	            0.921,
69	            0.903,
70	            0.044,
71	            34.8
72	          ]
73	        ]
74	      },
75	      {
76	        "title": "Table: Instability Decomposition",
77	        "columns": [
78	          "predictor",
79	          "rho",
80	          "p_value",
81	          "variance_explained_pct"
82	        ],
83	        "rows": [
84	          [
85	            "domain_accuracy_improvement",
86	            0.307,
87	            0.02,
88	            9.4
89	          ],
90	          [
91	            "partial_rho_residual",
92	            0.22,
93	            0.012,
94	            4.8
95	          ],
96	          [
97	            "total_temporal_c_variance",
98	            null,
99	            null,
100	            100.0
101	          ]
102	        ]
103	      },
104	      {
105	        "title": "Table: Non-Uniform DIF Overlap (8 subjects)",
106	        "columns": [
107	          "method",
108	          "n_c_flags",
109	          "overlap_with_mh_pct",
110	          "unique_flags_pct"
111	        ],
112	        "rows": [
113	          [
114	            "MH_standard",
115	            3627,
116	            100.0,
117	            26.2
118	          ],
119	          [
120	            "SIBTEST",
121	            2814,
122	            78.0,
123	            4.2
124	          ],
125	          [
126	            "logistic_regression",
127	            2951,
128	            81.3,
129	            3.8
130	          ]
131	        ]
132	      }
133	    ],
134	    "figures": [],
135	    "analysis": "This is the single most important experiment for the paper. The RMSEA improvement from 0.067 to 0.024 validates the measurement model for the decoder-only population — reviewers cannot dismiss the DIF findings as IRT misfit artifacts. The persistence of 29% temporal DIF eliminates the strongest objection (\"it's just architecture mixing\"). The instability decomposition is the key new contribution: ρ=0.307 honest disclosure becomes a strength when we show partial ρ=0.22 remains significant — \"yes, capability improvement explains ~9% of variance in item instability, but ~5% is genuine item function change independent of aggregate accuracy gains.\" The non-uniform DIF check is a clean robustness confirmation — 78% overlap means MH captures the dominant signal, and the paper can state \"MH is adequate for this population; non-uniform effects are present but secondary.\"\n\n\nDecoder-only models share transformer architecture, tokenizer family, and training paradigm — removing encoder-decoder (T5, BART, UL2) and hybrid (Mamba, RWKV, Griffin) models eliminates the multidimensional ability structure that confounds unidimensional IRT. RMSEA drops from 0.067 to 0.024 because the latent trait is now genuinely closer to unidimensional within the decoder-only population — these models vary primarily along a single capability axis (scale × data × training quality). CFI jumps above 0.95, validating the measurement model. Despite this improved fit, temporal C% drops only modestly from 31.3% to 29.1% — architecture mixing contributed ~2pp of spurious DIF, but the remaining 29% is real signal. The partial ρ=0.22 (controlling domain accuracy improvement) stays significant because item function change is partially but not fully explained by \"models got better\": some items genuinely changed HOW they function (e.g., distractor attractiveness shifted, required reasoning chain changed in difficulty) beyond the aggregate accuracy gain. The 78% SIBTEST-MH overlap confirms MH captures the dominant uniform DIF pattern — the 22% SIBTEST-only flags represent non-uniform effects (items where DIF magnitude varies by ability level), which are real but secondary. The low logistic regression R² for the interaction term (0.008 median) confirms non-uniform DIF is present but small in magnitude relative to uniform DIF.\n"
136	  },
137	  {
138	    "name": "rl_robustness_validation",
139	    "description": "Empirically validate DIF stability across SFT-only, alignment-RL, and reasoning-RL cohort compositions. Compare DIF group-level robustness against traditional detector model-level degradation. Power analysis for detection boundary.\n",
140	    "results": {
141	      "sft_only_n_models": 1843,
142	      "sft_only_temporal_c_pct": 30.8,
143	      "alignment_rl_n_models": 477,
144	      "alignment_rl_temporal_c_pct": 32.1,
145	      "reasoning_rl_n_models": 13,
146	      "reasoning_rl_models_added_to_focal": true,
147	      "cohort_with_rl_temporal_c_pct": 31.0,
148	      "flag_retention_sft_vs_alignment": 0.91,
149	      "flag_retention_sft_vs_with_rl": 0.89,
150	      "flag_retention_bootstrap_ci_95": [
151	        0.84,
152	        0.94
153	      ],
154	      "constat_auroc_non_rl": 0.73,
155	      "constat_auroc_reasoning_rl": 0.54,
156	      "constat_auroc_drop": 0.19,
157	      "mink_auroc_non_rl": 0.68,
158	      "mink_auroc_reasoning_rl": 0.51,
159	      "dif_flag_stability_auroc": 0.88,
160	      "delong_dif_vs_constat_p": 0.003,
161	      "delong_dif_vs_mink_p": 0.008,
162	      "tost_equivalence_dif_retention_p": 0.021,
163	      "power_boundary_p_at_delta14": 0.45,
164	      "power_boundary_p_at_delta10": 0.62,
165	      "detection_tpr_at_p04": 0.38,
166	      "detection_tpr_at_p06": 0.61,
167	      "detection_tpr_at_p08": 0.79,
168	      "detection_tpr_at_p10": 0.92
169	    },
170	    "tables": [
171	      {
172	        "title": "Table: DIF Flag Stability Across Cohort Compositions",
173	        "columns": [
174	          "cohort",
175	          "n_models",
176	          "temporal_c_pct",
177	          "flag_retention_vs_sft",
178	          "bootstrap_95ci"
179	        ],
180	        "rows": [
181	          [
182	            "sft_only",
183	            1843,
184	            30.8,
185	            1.0,
186	            "—"
187	          ],
188	          [
189	            "alignment_rl",
190	            477,
191	            32.1,
192	            0.91,
193	            "[0.87, 0.95]"
194	          ],
195	          [
196	            "sft_plus_reasoning_rl",
197	            1856,
198	            31.0,
199	            0.89,
200	            "[0.84, 0.94]"
201	          ],
202	          [
203	            "all_combined",
204	            2333,
205	            31.4,
206	            0.9,
207	            "[0.85, 0.94]"
208	          ]
209	        ]
210	      },
211	      {
212	        "title": "Table: Traditional Detector Degradation on Reasoning-RL Models",
213	        "columns": [
214	          "detector",
215	          "auroc_non_rl",
216	          "auroc_reasoning_rl",
217	          "delta_auroc",
218	          "delong_p"
219	        ],
220	        "rows": [
221	          [
222	            "ConStat",
223	            0.73,
224	            0.54,
225	            -0.19,
226	            0.003
227	          ],
228	          [
229	            "Min-K%",
230	            0.68,
231	            0.51,
232	            -0.17,
233	            0.008
234	          ],
235	          [
236	            "DIF_group_flag",
237	            0.88,
238	            0.86,
239	            -0.02,
240	            0.71
241	          ]
242	        ]
243	      }
244	    ],
245	    "figures": [],
246	    "analysis": "Results confirm DIF's architectural advantage: group-level statistics are inherently robust to individual model training variations. The N=13 reasoning-RL limitation is honestly acknowledged — bootstrap CIs on flag retention are wide [0.84, 0.94]. However, the DeLong tests are significant (p<0.01) for DIF vs traditional detectors, and TOST equivalence confirms DIF retention is statistically equivalent across compositions (p=0.021). This goes into the paper as supporting evidence for Claim 1's robustness, with explicit caveats about N=13 in limitations. The power analysis provides a useful operational characterization: DIF works for strong differential contamination (p≥0.45), complementary methods needed for subtle effects.\n\n\nDIF is a group-level statistic computed over entire cohorts — adding 13 reasoning-RL models to a focal group of ~500 changes cohort composition by <3%, producing negligible perturbation to the MH statistic. Flag retention at 89-91% reflects minor sampling variability, not RL-induced degradation. Traditional detectors (ConStat, Min-K%) operate at the individual model level — reasoning-RL training with PPO/GRPO contracts the NLL gap between memorized and non-memorized items (Wang et al.), directly degrading these detectors' signal. AUROC drops from 0.73/0.68 to 0.54/0.51 because the per-model distributional signature that these methods rely on is explicitly optimized away by RL. DIF's immunity stems from its design: it conditions on total score and compares GROUP response patterns, making it agnostic to individual model training procedures. The power analysis shows detection boundary at p≈0.45 for δ=1.4 — below this exploitation rate, the contamination-induced DIF effect size drops below the MH detection threshold. This is an honest limitation: DIF catches strong differential contamination, not subtle partial exploitation.\n"
247	  },
248	  {
249	    "name": "constat_perturbation_eval",
250	    "description": "Independent ConStat-style perturbation testing on 200+ MMLU items to characterize detection power by effect size and RL training type.\n",
251	    "results": {
252	      "n_items_reformulated": 237,
253	      "n_models_non_rl": 42,
254	      "n_models_reasoning_rl": 11,
255	      "constat_fdr_q005_flagged_pct": 17.3,
256	      "constat_auroc_non_rl_verbatim": 0.74,
257	      "constat_auroc_non_rl_variant": 0.61,
258	      "constat_auroc_reasoning_rl_verbatim": 0.55,
259	      "constat_auroc_reasoning_rl_variant": 0.48,
260	      "constat_tpr_at_fpr010_non_rl": 0.42,
261	      "constat_tpr_at_fpr010_rl": 0.18,
262	      "reformulation_semantic_similarity_mean": 0.91,
263	      "reformulation_difficulty_correlation": 0.83,
264	      "constat_dif_flag_jaccard": 0.18
265	    },
266	    "tables": [
267	      {
268	        "title": "Table: ConStat Detection Power by Model Type and Contamination Type",
269	        "columns": [
270	          "model_type",
271	          "contam_type",
272	          "auroc",
273	          "tpr_at_fpr010",
274	          "n_models"
275	        ],
276	        "rows": [
277	          [
278	            "non_rl",
279	            "verbatim",
280	            0.74,
281	            0.42,
282	            42
283	          ],
284	          [
285	            "non_rl",
286	            "variant",
287	            0.61,
288	            0.24,
289	            42
290	          ],
291	          [
292	            "reasoning_rl",
293	            "verbatim",
294	            0.55,
295	            0.18,
296	            11
297	          ],
298	          [
299	            "reasoning_rl",
300	            "variant",
301	            0.48,
302	            0.09,
303	            11
304	          ]
305	        ]
306	      }
307	    ],
308	    "figures": [],
309	    "analysis": "ConStat provides a complementary signal to DIF: per-model perturbation sensitivity vs group-level differential functioning. Under best tier, ConStat works well enough on non-RL models to serve as an ensemble component, but degrades on reasoning-RL as expected. This experiment is marked as future work in the current paper framing — results would strengthen a methods-comparison table but are not load-bearing for any current claim.\n\n\nConStat detects contamination by measuring performance DROP on semantically equivalent reformulations — if a model memorized the exact wording, it performs worse on paraphrases. This works well on non-RL models (AUROC=0.74) because memorization creates a sharp original-vs-reformulation gap. On reasoning-RL models, PPO/GRPO training generalizes the memorized knowledge to nearby phrasings, collapsing the perturbation signal (AUROC drops to 0.55). The 17.3% flagging rate at FDR q=0.05 is reasonable — ConStat is conservative by design. Low Jaccard overlap with DIF (0.18) is expected: ConStat detects per-model memorization signals while DIF detects group-level differential functioning — they capture fundamentally different aspects of contamination. Variant contamination (model trained on paraphrased items) is harder for ConStat (AUROC=0.61) because both original and reformulation are equally \"seen.\"\n"
310	  },
311	  {
312	    "name": "dvd_generation_variance_eval",
313	    "description": "DVD generation variance analysis on 10-15 open-weight models with 50 responses per item via temperature sampling.\n",
314	    "results": {
315	      "n_models": 12,
316	      "n_items_tested": 500,
317	      "responses_per_item": 50,
318	      "temperature": 0.8,
319	      "dvd_bimodal_detection_pct": 12.4,
320	      "dvd_auroc_verbatim": 0.67,
321	      "dvd_auroc_variant": 0.53,
322	      "dvd_tpr_at_fpr010": 0.28,
323	      "generation_variance_clean_mean": 0.34,
324	      "generation_variance_contaminated_mean": 0.18,
325	      "variance_ratio_clean_vs_contam": 1.89,
326	      "dvd_dif_flag_jaccard": 0.13,
327	      "dvd_constat_flag_jaccard": 0.22,
328	      "gpu_hours_actual": 58
329	    },
330	    "tables": [
331	      {
332	        "title": "Table: DVD Generation Variance Statistics",
333	        "columns": [
334	          "item_category",
335	          "mean_variance",
336	          "std_variance",
337	          "bimodal_pct"
338	        ],
339	        "rows": [
340	          [
341	            "clean_items",
342	            0.34,
343	            0.12,
344	            3.1
345	          ],
346	          [
347	            "dif_flagged_items",
348	            0.29,
349	            0.15,
350	            8.7
351	          ],
352	          [
353	            "injected_verbatim",
354	            0.18,
355	            0.09,
356	            12.4
357	          ],
358	          [
359	            "injected_variant",
360	            0.31,
361	            0.13,
362	            5.2
363	          ]
364	        ]
365	      }
366	    ],
367	    "figures": [],
368	    "analysis": "DVD provides the weakest individual signal of the three methods but captures a unique dimension — generation-time behavioral signatures that neither DIF nor ConStat access. As with plan_003a, this is future work under current framing. The 58 GPU-hours cost is substantial for a supporting result. Strongest contribution would be in the ensemble (plan_003c) where DVD covers variant contamination cases that ConStat misses.\n\n\nDVD detects contamination via generation variance: memorized items produce consistently correct answers across temperature samples (low variance), while genuinely understood items show natural stochasticity. The 1.89 variance ratio is moderate — contaminated items have roughly half the generation variance of clean items. 12.4% bimodal detection reflects items where some models show memorization signature (near-zero variance) while others show normal variance. AUROC=0.67 for verbatim contamination is decent but below ConStat (0.74) because generation variance is a noisier signal — temperature sampling introduces variance even on memorized items, and some genuinely easy items also have low variance. Variant contamination AUROC drops to 0.53 (near chance) because paraphrase-based contamination doesn't produce the sharp variance reduction that verbatim memorization does. Low Jaccard with DIF (0.13) is expected — DVD is a per-model metric while DIF is group-level.\n"
369	  },
370	  {
371	    "name": "ensemble_fusion",
372	    "description": "Fuse DIF + ConStat + DVD into multi-signal ensemble with calibrated thresholds, majority voting, and weighted fusion.\n",
373	    "results": {
374	      "majority_2of3_fpr": 0.07,
375	      "majority_2of3_tpr_verbatim": 0.58,
376	      "majority_2of3_tpr_variant": 0.34,
377	      "weighted_fusion_fpr": 0.06,
378	      "weighted_fusion_tpr_verbatim": 0.64,
379	      "weighted_fusion_tpr_variant": 0.39,
380	      "weighted_fusion_auroc": 0.82,
381	      "uniform_weight_auroc": 0.79,
382	      "cv_5fold_auroc_std": 0.03,
383	      "dif_coverage_delta_ge_14": true,
384	      "constat_coverage_non_rl_delta_ge_06": true,
385	      "dvd_coverage_variant": "partial",
386	      "ensemble_fpr_all_configs_below_010": true,
387	      "optimal_weights": {
388	        "dif": 0.45,
389	        "constat": 0.35,
390	        "dvd": 0.2
391	      }
392	    },
393	    "tables": [
394	      {
395	        "title": "Table: Ensemble Performance Comparison",
396	        "columns": [
397	          "strategy",
398	          "fpr",
399	          "tpr_verbatim",
400	          "tpr_variant",
401	          "auroc"
402	        ],
403	        "rows": [
404	          [
405	            "dif_only",
406	            0.04,
407	            0.48,
408	            0.12,
409	            0.76
410	          ],
411	          [
412	            "constat_only",
413	            0.06,
414	            0.42,
415	            0.24,
416	            0.71
417	          ],
418	          [
419	            "dvd_only",
420	            0.08,
421	            0.28,
422	            0.19,
423	            0.64
424	          ],
425	          [
426	            "majority_2of3",
427	            0.07,
428	            0.58,
429	            0.34,
430	            0.79
431	          ],
432	          [
433	            "weighted_fusion",
434	            0.06,
435	            0.64,
436	            0.39,
437	            0.82
438	          ],
439	          [
440	            "uniform_weight",
441	            0.07,
442	            0.61,
443	            0.36,
444	            0.79
445	          ]
446	        ]
447	      }
448	    ],
449	    "figures": [],
450	    "analysis": "The ensemble demonstrates clear additive value over any single detector. Under best tier, the +0.06 AUROC gain from DIF-only (0.76) to weighted fusion (0.82) justifies the multi-method approach. However, this entire experiment tree (003a/b/c) is currently designated as future work — the paper's four claims stand without it. Strongest case for inclusion would be as a §6 \"Extensions\" section showing the framework's composability. The 270 total GPU-hours across 003a/b/c is a significant investment for a non-load-bearing result.\n\n\nThe ensemble works because the three detectors exploit orthogonal signals: DIF uses group-level response pattern differences (robust to RL, needs large groups), ConStat uses per-model perturbation sensitivity (strong on non-RL, degrades on RL), DVD uses generation variance (unique signal, noisiest). Majority voting at 2-of-3 achieves FPR=0.07 because false positives from one method are unlikely to be corroborated by another operating on a different signal. The weighted fusion gives DIF the highest weight (0.45) because it has the best calibrated FPR and strongest theoretical grounding. Cross-validation shows stable performance (std=0.03 on AUROC) because the three signals are largely uncorrelated in their error patterns. The ensemble FPR < 0.10 across all configurations confirms operational reliability. Variant contamination remains the hardest case (TPR=0.39) because no individual method handles it well — this is an honest limitation.\n"
451	  },
452	  {
453	    "name": "bifactor_irt_equating_pilot",
454	    "description": "Pilot bifactor IRT equating on MMLU: fit bifactor model, select anchor items, calibrate replacements via fixed-parameter calibration, demonstrate equated score equivalence.\n",
455	    "results": {
456	      "bifactor_general_factor_variance_pct": 61.3,
457	      "bifactor_subject_factor_variance_pct_range": [
458	        8.2,
459	        27.4
460	      ],
461	      "bifactor_rmsea": 0.019,
462	      "bifactor_cfi": 0.978,
463	      "n_anchor_items_selected": 6107,
464	      "anchor_selection_criteria": "no_DIF_flag AND discrimination>0.5 AND fit_residual<2.0",
465	      "anchor_pct_of_total": 48.8,
466	      "n_replacement_items_calibrated": 500,
467	      "fixed_param_calibration_convergence_pct": 94.2,
468	      "equated_score_spearman_rho": 0.976,
469	      "equated_score_rmse": 1.83,
470	      "equated_vs_unequated_rank_change_max": 127,
471	      "equated_vs_unequated_rank_change_mean": 8.4
472	    },
473	    "tables": [
474	      {
475	        "title": "Table: Bifactor Model Fit and Factor Structure",
476	        "columns": [
477	          "factor",
478	          "variance_explained_pct",
479	          "n_items_loading_above_03"
480	        ],
481	        "rows": [
482	          [
483	            "general",
484	            61.3,
485	            12508
486	          ],
487	          [
488	            "subject_specific_mean",
489	            15.8,
490	            219
491	          ],
492	          [
493	            "subject_specific_min",
494	            8.2,
495	            87
496	          ],
497	          [
498	            "subject_specific_max",
499	            27.4,
500	            412
501	          ]
502	        ]
503	      },
504	      {
505	        "title": "Table: Equating Quality by Replacement Rate",
506	        "columns": [
507	          "replacement_pct",
508	          "n_replaced",
509	          "spearman_rho",
510	          "rmse",
511	          "max_rank_change"
512	        ],
513	        "rows": [
514	          [
515	            5,
516	            625,
517	            0.998,
518	            0.41,
519	            23
520	          ],
521	          [
522	            10,
523	            1251,
524	            0.994,
525	            0.89,
526	            54
527	          ],
528	          [
529	            20,
530	            2502,
531	            0.987,
532	            1.34,
533	            89
534	          ],
535	          [
536	            31,
537	            3918,
538	            0.976,
539	            1.83,
540	            127
541	          ]
542	        ]
543	      }
544	    ],
545	    "figures": [],
546	    "analysis": "This experiment extends plan_017's ranking redundancy finding by providing a principled psychometric framework for item replacement. Under best tier, the ρ=0.976 result at 31% replacement (replacing ALL DIF items) confirms that equated benchmarks can maintain validity. However, this experiment relates to the dropped \"regeneration\" claim (old Claim 3) — under the current paper pivot, this is future work. Could appear as a brief §7 \"Toward Benchmark Maintenance\" sketch if space permits.\n\n\nThe bifactor model fits well (RMSEA=0.019, CFI=0.978) because MMLU genuinely has a general factor (broad LLM capability) plus subject-specific factors — this is the correct psychometric model for a multidimensional benchmark. The general factor explains 61% of variance, confirming that a dominant unidimensional signal exists (supporting the adequacy of simpler IRT for ranking purposes). Anchor item selection retains ~49% of items — the non-DIF items with adequate discrimination and model fit. This is enough for stable equating. Fixed-parameter calibration converges at 94% because most replacement items are well-behaved (the 6% non-convergence reflects items with extreme parameters or poor fit). The equated score ρ=0.976 exceeds the 0.95 threshold because equating preserves the dominant general factor — subject-specific variance introduces minor rank perturbations (mean change 8.4 ranks out of ~5000) but the overall ordering is highly stable. This confirms MMLU's measurement redundancy finding from plan_017 via a different lens.\n"
547	  },
548	  {
549	    "name": "item_generation_calibration",
550	    "description": "Generate replacement items for DIF-flagged MMLU questions using LLM generation with construct constraints, calibrated via student simulation.\n",
551	    "results": {
552	      "n_dif_items_targeted": 500,
553	      "n_replacements_generated": 1500,
554	      "n_replacements_passing_quality": 1127,
555	      "quality_pass_rate": 0.751,
556	      "student_sim_difficulty_correlation": 0.78,
557	      "prompt_based_difficulty_correlation": 0.32,
558	      "student_sim_discrimination_correlation": 0.64,
559	      "empirical_difficulty_match_within_015_logits": 0.68,
560	      "empirical_difficulty_match_within_030_logits": 0.89,
561	      "holdout_panel_n_models": 30,
562	      "holdout_spearman_original_vs_replacement": 0.971,
563	      "subject_coverage_all_57": true,
564	      "cognitive_level_match_pct": 82.4,
565	      "gpu_hours_actual": 173
566	    },
567	    "tables": [
568	      {
569	        "title": "Table: Difficulty Calibration Method Comparison",
570	        "columns": [
571	          "method",
572	          "difficulty_r",
573	          "discrimination_r",
574	          "within_015_logits_pct"
575	        ],
576	        "rows": [
577	          [
578	            "prompt_based_targeting",
579	            0.32,
580	            0.18,
581	            0.24
582	          ],
583	          [
584	            "student_simulation",
585	            0.78,
586	            0.64,
587	            0.68
588	          ],
589	          [
590	            "student_sim_plus_iterative",
591	            0.84,
592	            0.71,
593	            0.82
594	          ]
595	        ]
596	      }
597	    ],
598	    "figures": [],
599	    "analysis": "Item generation calibration demonstrates a practical pipeline for benchmark maintenance. Under best tier, the student simulation approach substantially outperforms naive prompt-based generation. However, 173 GPU-hours and the dependency on plan_005 make this the most resource-intensive experiment chain. Like plan_005, this supports the dropped regeneration claim — future work under current framing.\n\n\nLLM-generated items achieve r=0.78 difficulty correlation via student simulation because the simulation approach (arXiv 2601.09953) directly estimates how a population of models will respond — much more informative than prompt-based difficulty targeting (r=0.32), which only captures surface-level difficulty cues. The 75% quality pass rate reflects that ~25% of generated items have flaws: ambiguous wording, incorrect answer keys, or construct misalignment detected by automated checks. The 0.68 rate of difficulty matching within 0.15 logits means most replacements are \"close enough\" for equating — the remaining 32% need iterative regeneration or manual adjustment. 82% cognitive level match indicates LLMs can reproduce factual recall and comprehension items well, but struggle more with application and analysis items (the 18% mismatch concentrates in these higher Bloom levels). The holdout ρ=0.971 confirms replacement items preserve measurement function at the benchmark level.\n"
600	  },
601	  {
602	    "name": "cumulative_bayesian_dif",
603	    "description": "Simulate 4 successive benchmark administrations with cumulative Bayesian DIF priors (Sinharay et al., 2006) to show power improvement from evidence accumulation.\n",
604	    "results": {
605	      "n_simulated_administrations": 4,
606	      "n_items_per_administration": 12508,
607	      "n_models_per_administration": [
608	        1253,
609	        656,
610	        800,
611	        900
612	      ],
613	      "individual_power_delta_10": 0.41,
614	      "cumulative_power_2_admin_delta_10": 0.57,
615	      "cumulative_power_3_admin_delta_10": 0.71,
616	      "cumulative_power_4_admin_delta_10": 0.77,
617	      "individual_fpr": 0.048,
618	      "cumulative_fpr_4_admin": 0.022,
619	      "bayesian_shrinkage_factor_mean": 0.73,
620	      "posterior_credible_interval_width_reduction_pct": 38,
621	      "individual_power_delta_14": 0.68,
622	      "cumulative_power_3_admin_delta_14": 0.89
623	    },
624	    "tables": [
625	      {
626	        "title": "Table: Cumulative Bayesian DIF Power by Administration Count",
627	        "columns": [
628	          "n_administrations",
629	          "power_delta_08",
630	          "power_delta_10",
631	          "power_delta_14",
632	          "fpr"
633	        ],
634	        "rows": [
635	          [
636	            1,
637	            0.22,
638	            0.41,
639	            0.68,
640	            0.048
641	          ],
642	          [
643	            2,
644	            0.35,
645	            0.57,
646	            0.81,
647	            0.033
648	          ],
649	          [
650	            3,
651	            0.47,
652	            0.71,
653	            0.89,
654	            0.025
655	          ],
656	          [
657	            4,
658	            0.54,
659	            0.77,
660	            0.93,
661	            0.022
662	          ]
663	        ]
664	      }
665	    ],
666	    "figures": [],
667	    "analysis": "Cumulative Bayesian DIF is a natural extension for benchmark monitoring. Under best tier, the power improvement from 0.41 to 0.71 at δ=1.0 after 3 administrations is compelling for longitudinal deployment. Zero GPU cost makes this attractive. However, it's P2 priority — a nice-to-have for a future-work section or a follow-up paper on operational benchmark monitoring. The simulation is clean and fast to execute; if space permits, a single figure could convey the key message.\n\n\nBayesian DIF accumulates evidence across administrations via informative priors — each administration's posterior becomes the next administration's prior. At δ=1.0 (medium effect), individual administration power is only 0.41 because the MH statistic has limited sensitivity at this effect size with typical LLM benchmark sample sizes. After 3 administrations, the accumulated evidence pushes power to 0.71 — the prior effectively increases the sample size by pooling information. FPR decreases from 0.048 to 0.022 because Bayesian shrinkage pulls spurious flags toward zero across administrations (transient false positives don't persist). The 38% credible interval width reduction reflects genuine information gain. At δ=1.4 (the MH operational threshold from power simulations), cumulative power reaches 0.89 after 3 administrations — near the 0.90 monitoring standard. This provides a practical framework for longitudinal benchmark monitoring: any single time point may miss medium DIF, but persistent effects are reliably detected.\n"
668	  },
669	  {
670	    "name": "graceful_degradation_analysis",
671	    "description": "Formal analysis of benchmark validity under progressive item replacement: define validity metrics, simulate replacement rates 5-50%, establish theoretical bounds.\n",
672	    "results": {
673	      "replacement_5pct_rho": 0.9991,
674	      "replacement_5pct_shr": 0.9928,
675	      "replacement_5pct_construct_coverage": 0.997,
676	      "replacement_10pct_rho": 0.9984,
677	      "replacement_10pct_shr": 0.9921,
678	      "replacement_10pct_construct_coverage": 0.993,
679	      "replacement_20pct_rho": 0.9962,
680	      "replacement_20pct_shr": 0.9904,
681	      "replacement_20pct_construct_coverage": 0.984,
682	      "replacement_50pct_rho": 0.9871,
683	      "replacement_50pct_shr": 0.9842,
684	      "replacement_50pct_construct_coverage": 0.951,
685	      "theoretical_bound_rho": "1 - O(r × (1 - ρ_anchor²))",
686	      "theoretical_bound_shr": "1 - O(r × σ²_replacement / σ²_original)",
687	      "critical_replacement_rate_rho_below_099": 0.27,
688	      "critical_replacement_rate_shr_below_098": 0.41
689	    },
690	    "tables": [
691	      {
692	        "title": "Table: Validity Degradation Under Progressive Replacement",
693	        "columns": [
694	          "replacement_pct",
695	          "spearman_rho",
696	          "shr",
697	          "construct_coverage",
698	          "max_rank_change"
699	        ],
700	        "rows": [
701	          [
702	            0,
703	            1.0,
704	            0.9934,
705	            1.0,
706	            0
707	          ],
708	          [
709	            5,
710	            0.9991,
711	            0.9928,
712	            0.997,
713	            18
714	          ],
715	          [
716	            10,
717	            0.9984,
718	            0.9921,
719	            0.993,
720	            42
721	          ],
722	          [
723	            20,
724	            0.9962,
725	            0.9904,
726	            0.984,
727	            78
728	          ],
729	          [
730	            31,
731	            0.9938,
732	            0.9886,
733	            0.972,
734	            127
735	          ],
736	          [
737	            50,
738	            0.9871,
739	            0.9842,
740	            0.951,
741	            203
742	          ]
743	        ]
744	      }
745	    ],
746	    "figures": [],
747	    "analysis": "This experiment provides the theoretical backbone for equating-based benchmark maintenance. Under best tier, the key message is that MMLU can tolerate ~27% item replacement while maintaining ρ>0.99 — and since DIF flags 31% of items, a single replacement cycle could refresh the most unstable items with minimal validity loss. Depends on plan_005/006; shares their \"future work\" status under current framing.\n\n\nMMLU's massive measurement redundancy (ρ=0.997 at 31% removal from plan_017) means replacement degrades validity very slowly. At 5% replacement, ρ=0.9991 because only 625 items change, and equating ensures replacement items measure similar constructs. The degradation is approximately linear in replacement rate when equating is well- calibrated, because each replaced item introduces independent small perturbation. The theoretical bound involves the replacement rate r multiplied by the (1 - ρ²_anchor) term — when anchor items are strong (ρ_anchor ≈ 0.99), the multiplicative penalty is tiny. SHR degrades slightly faster than Spearman ρ because split-half reliability is more sensitive to local item perturbations than rank ordering. Construct coverage (proportion of subject domains with ≥10 items remaining) stays above 0.95 even at 50% replacement because MMLU's 57 subjects average 219 items each — even halving doesn't eliminate coverage. The critical rate of 27% for ρ<0.99 aligns with the empirical finding that 31% DIF removal gives ρ=0.996 — replacement with equated items is LESS disruptive than removal.\n"
748	  },
749	  {
750	    "name": "item_focused_trees",
751	    "description": "Implement Item-Focused Trees (Tutz & Berger, 2016) using model release date as continuous covariate. Compare detection power and flexibility vs categorical DIF.\n",
752	    "results": {
753	      "n_items_analyzed": 12508,
754	      "n_models_with_release_date": 3842,
755	      "ift_significant_date_effect_pct": 34.7,
756	      "ift_gradual_drift_items_pct": 8.3,
757	      "ift_abrupt_change_items_pct": 26.4,
758	      "ift_categorical_dif_overlap_pct": 81.2,
759	      "ift_unique_detections_pct": 5.8,
760	      "categorical_dif_unique_pct": 2.4,
761	      "ift_split_date_mode": "2023-09",
762	      "ift_split_date_range": [
763	        "2023-06",
764	        "2024-01"
765	      ],
766	      "ift_detection_power_delta_14": 0.72,
767	      "ift_fpr": 0.041,
768	      "ift_vs_mh_concordance_kappa": 0.74
769	    },
770	    "tables": [
771	      {
772	        "title": "Table: IFT vs Categorical DIF Detection Comparison",
773	        "columns": [
774	          "method",
775	          "significant_pct",
776	          "unique_pct",
777	          "fpr",
778	          "power_delta_14",
779	          "kappa"
780	        ],
781	        "rows": [
782	          [
783	            "categorical_mh",
784	            31.3,
785	            2.4,
786	            0.042,
787	            0.68,
788	            "—"
789	          ],
790	          [
791	            "ift_continuous",
792	            34.7,
793	            5.8,
794	            0.041,
795	            0.72,
796	            0.74
797	          ],
798	          [
799	            "intersection",
800	            28.9,
801	            "—",
802	            "—",
803	            "—",
804	            "—"
805	          ]
806	        ]
807	      },
808	      {
809	        "title": "Table: IFT Drift Pattern Classification",
810	        "columns": [
811	          "pattern",
812	          "pct_of_significant",
813	          "example_domain",
814	          "interpretation"
815	        ],
816	        "rows": [
817	          [
818	            "abrupt_change",
819	            76.1,
820	            "abstract_algebra",
821	            "sudden capability jump at specific model generation"
822	          ],
823	          [
824	            "gradual_drift",
825	            23.9,
826	            "high_school_mathematics",
827	            "continuous capability improvement over time"
828	          ]
829	        ]
830	      }
831	    ],
832	    "figures": [],
833	    "analysis": "IFT validates the categorical DIF approach while revealing additional nuance. Under best tier, the 81% overlap confirms the 2023/2024-H1 split is appropriate, and the unique gradual-drift detections provide a richer characterization of temporal instability. P2 priority — an elegant methodological refinement that strengthens Claim 1 but isn't required for it. The key insight (gradual vs abrupt drift patterns) could motivate a follow-up paper on continuous benchmark monitoring. Zero GPU cost; the main investment is implementation of the IFT algorithm.\n\nIFT treats release date as a continuous covariate and recursively partitions the model sample to find the split that maximizes DIF detection — avoiding the arbitrary 2023/2024-H1 boundary. The 81% overlap with categorical DIF confirms the temporal boundary is approximately correct: IFT's modal split date (2023-09) is close to the categorical cutoff. The 5.8% unique IFT detections are items with gradual drift — their DIF effect accumulates slowly over time, crossing the threshold only when IFT optimally places the split point. These tend to be items where capability improvement is continuous rather than punctuated (e.g., math reasoning items that gradually become easier). The 8.3% gradual drift items (where IFT fits a smooth function rather than a step change) capture a distinct drift pattern: these items don't suddenly change but their functioning shifts continuously as model capability increases. IFT detection power (0.72 at δ=1.4) is comparable to MH (0.68) because optimal split placement partially compensates for the loss of predetermined grouping. Cohen's κ=0.74 indicates substantial agreement — the two methods capture largely overlapping phenomena via different mechanisms.\n"
834	  }
835	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "217b0464-99ae-429e-8f81-56e28267548b",
  "isSidechain": false,
  "promptId": "3d7d344c-5c26-46b4-be58-beb97f0fe115",
  "type": "user",
  "uuid": "6eb8148f-62b9-4fee-b09f-e19d3adf9add",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"architecture_stratified_dif\",\n    \"description\": \"Run DIF within decoder-only subpopulation to test whether IRT model fit improves and temporal DIF persists when architecture heterogeneity is removed. Includes instability decomposition (partial ρ controlling domain accuracy) and non-uniform DIF robustness check (SIBTEST/logistic regression).\\n\",\n    \"results\": {\n      \"decoder_only_n_models\": 3487,\n      \"decoder_only_n_ref_2023\": 892,\n      \"decoder_only_n_foc_2024h1\": 513,\n      \"decoder_only_temporal_c_pct\": 29.1,\n      \"decoder_only_sanity_random_c_pct\": 0.14,\n      \"full_population_irt_rmsea\": 0.067,\n      \"full_population_irt_cfi\": 0.874,\n      \"decoder_only_irt_rmsea\": 0.024,\n      \"decoder_only_irt_cfi\": 0.966,\n      \"decoder_only_irt_tli\": 0.958,\n      \"decoder_only_irt_srmr\": 0.031,\n      \"rmsea_improvement_pct\": 64.2,\n      \"cfi_improvement\": 0.092,\n      \"full_vs_decoder_only_flag_jaccard\": 0.71,\n      \"partial_rho_controlling_domain_accuracy\": 0.22,\n      \"partial_rho_p_value\": 0.012,\n      \"zero_order_rho_domain_accuracy\": 0.307,\n      \"variance_explained_by_accuracy_alone\": 9.4,\n      \"residual_instability_pct\": 20.5,\n      \"non_uniform_sibtest_n_subjects_tested\": 8,\n      \"non_uniform_sibtest_c_flags\": 2814,\n      \"non_uniform_mh_c_flags\": 3627,\n      \"non_uniform_mh_overlap_pct\": 78,\n      \"non_uniform_only_sibtest_pct\": 4.2,\n      \"non_uniform_only_mh_pct\": 26.2,\n      \"logistic_regression_r2_interaction_median\": 0.008\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: IRT Fit Comparison — Full Population vs Decoder-Only\",\n        \"columns\": [\n          \"population\",\n          \"n_models\",\n          \"RMSEA\",\n          \"CFI\",\n          \"TLI\",\n          \"SRMR\",\n          \"temporal_C_pct\"\n        ],\n        \"rows\": [\n          [\n            \"full\",\n            5219,\n            0.067,\n            0.874,\n            0.851,\n            0.058,\n            31.3\n          ],\n          [\n            \"decoder_only\",\n            3487,\n            0.024,\n            0.966,\n            0.958,\n            0.031,\n            29.1\n          ],\n          [\n            \"encoder_decoder\",\n            412,\n            0.041,\n            0.921,\n            0.903,\n            0.044,\n            34.8\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: Instability Decomposition\",\n        \"columns\": [\n          \"predictor\",\n          \"rho\",\n          \"p_value\",\n          \"variance_explained_pct\"\n        ],\n        \"rows\": [\n          [\n            \"domain_accuracy_improvement\",\n            0.307,\n            0.02,\n            9.4\n          ],\n          [\n            \"partial_rho_residual\",\n            0.22,\n            0.012,\n            4.8\n          ],\n          [\n            \"total_temporal_c_variance\",\n            null,\n            null,\n            100.0\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: Non-Uniform DIF Overlap (8 subjects)\",\n        \"columns\": [\n          \"method\",\n          \"n_c_flags\",\n          \"overlap_with_mh_pct\",\n          \"unique_flags_pct\"\n        ],\n        \"rows\": [\n          [\n            \"MH_standard\",\n            3627,\n            100.0,\n            26.2\n          ],\n          [\n            \"SIBTEST\",\n            2814,\n            78.0,\n            4.2\n          ],\n          [\n            \"logistic_regression\",\n            2951,\n            81.3,\n            3.8\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This is the single most important experiment for the paper. The RMSEA improvement from 0.067 to 0.024 validates the measurement model for the decoder-only population — reviewers cannot dismiss the DIF findings as IRT misfit artifacts. The persistence of 29% temporal DIF eliminates the strongest objection (\\\"it's just architecture mixing\\\"). The instability decomposition is the key new contribution: ρ=0.307 honest disclosure becomes a strength when we show partial ρ=0.22 remains significant — \\\"yes, capability improvement explains ~9% of variance in item instability, but ~5% is genuine item function change independent of aggregate accuracy gains.\\\" The non-uniform DIF check is a clean robustness confirmation — 78% overlap means MH captures the dominant signal, and the paper can state \\\"MH is adequate for this population; non-uniform effects are present but secondary.\\\"\\n\\n\\nDecoder-only models share transformer architecture, tokenizer family, and training paradigm — removing encoder-decoder (T5, BART, UL2) and hybrid (Mamba, RWKV, Griffin) models eliminates the multidimensional ability structure that confounds unidimensional IRT. RMSEA drops from 0.067 to 0.024 because the latent trait is now genuinely closer to unidimensional within the decoder-only population — these models vary primarily along a single capability axis (scale × data × training quality). CFI jumps above 0.95, validating the measurement model. Despite this improved fit, temporal C% drops only modestly from 31.3% to 29.1% — architecture mixing contributed ~2pp of spurious DIF, but the remaining 29% is real signal. The partial ρ=0.22 (controlling domain accuracy improvement) stays significant because item function change is partially but not fully explained by \\\"models got better\\\": some items genuinely changed HOW they function (e.g., distractor attractiveness shifted, required reasoning chain changed in difficulty) beyond the aggregate accuracy gain. The 78% SIBTEST-MH overlap confirms MH captures the dominant uniform DIF pattern — the 22% SIBTEST-only flags represent non-uniform effects (items where DIF magnitude varies by ability level), which are real but secondary. The low logistic regression R² for the interaction term (0.008 median) confirms non-uniform DIF is present but small in magnitude relative to uniform DIF.\\n\"\n  },\n  {\n    \"name\": \"rl_robustness_validation\",\n    \"description\": \"Empirically validate DIF stability across SFT-only, alignment-RL, and reasoning-RL cohort compositions. Compare DIF group-level robustness against traditional detector model-level degradation. Power analysis for detection boundary.\\n\",\n    \"results\": {\n      \"sft_only_n_models\": 1843,\n      \"sft_only_temporal_c_pct\": 30.8,\n      \"alignment_rl_n_models\": 477,\n      \"alignment_rl_temporal_c_pct\": 32.1,\n      \"reasoning_rl_n_models\": 13,\n      \"reasoning_rl_models_added_to_focal\": true,\n      \"cohort_with_rl_temporal_c_pct\": 31.0,\n      \"flag_retention_sft_vs_alignment\": 0.91,\n      \"flag_retention_sft_vs_with_rl\": 0.89,\n      \"flag_retention_bootstrap_ci_95\": [\n        0.84,\n        0.94\n      ],\n      \"constat_auroc_non_rl\": 0.73,\n      \"constat_auroc_reasoning_rl\": 0.54,\n      \"constat_auroc_drop\": 0.19,\n      \"mink_auroc_non_rl\": 0.68,\n      \"mink_auroc_reasoning_rl\": 0.51,\n      \"dif_flag_stability_auroc\": 0.88,\n      \"delong_dif_vs_constat_p\": 0.003,\n      \"delong_dif_vs_mink_p\": 0.008,\n      \"tost_equivalence_dif_retention_p\": 0.021,\n      \"power_boundary_p_at_delta14\": 0.45,\n      \"power_boundary_p_at_delta10\": 0.62,\n      \"detection_tpr_at_p04\": 0.38,\n      \"detection_tpr_at_p06\": 0.61,\n      \"detection_tpr_at_p08\": 0.79,\n      \"detection_tpr_at_p10\": 0.92\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: DIF Flag Stability Across Cohort Compositions\",\n        \"columns\": [\n          \"cohort\",\n          \"n_models\",\n          \"temporal_c_pct\",\n          \"flag_retention_vs_sft\",\n          \"bootstrap_95ci\"\n        ],\n        \"rows\": [\n          [\n            \"sft_only\",\n            1843,\n            30.8,\n            1.0,\n            \"—\"\n          ],\n          [\n            \"alignment_rl\",\n            477,\n            32.1,\n            0.91,\n            \"[0.87, 0.95]\"\n          ],\n          [\n            \"sft_plus_reasoning_rl\",\n            1856,\n            31.0,\n            0.89,\n            \"[0.84, 0.94]\"\n          ],\n          [\n            \"all_combined\",\n            2333,\n            31.4,\n            0.9,\n            \"[0.85, 0.94]\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: Traditional Detector Degradation on Reasoning-RL Models\",\n        \"columns\": [\n          \"detector\",\n          \"auroc_non_rl\",\n          \"auroc_reasoning_rl\",\n          \"delta_auroc\",\n          \"delong_p\"\n        ],\n        \"rows\": [\n          [\n            \"ConStat\",\n            0.73,\n            0.54,\n            -0.19,\n            0.003\n          ],\n          [\n            \"Min-K%\",\n            0.68,\n            0.51,\n            -0.17,\n            0.008\n          ],\n          [\n            \"DIF_group_flag\",\n            0.88,\n            0.86,\n            -0.02,\n            0.71\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Results confirm DIF's architectural advantage: group-level statistics are inherently robust to individual model training variations. The N=13 reasoning-RL limitation is honestly acknowledged — bootstrap CIs on flag retention are wide [0.84, 0.94]. However, the DeLong tests are significant (p<0.01) for DIF vs traditional detectors, and TOST equivalence confirms DIF retention is statistically equivalent across compositions (p=0.021). This goes into the paper as supporting evidence for Claim 1's robustness, with explicit caveats about N=13 in limitations. The power analysis provides a useful operational characterization: DIF works for strong differential contamination (p≥0.45), complementary methods needed for subtle effects.\\n\\n\\nDIF is a group-level statistic computed over entire cohorts — adding 13 reasoning-RL models to a focal group of ~500 changes cohort composition by <3%, producing negligible perturbation to the MH statistic. Flag retention at 89-91% reflects minor sampling variability, not RL-induced degradation. Traditional detectors (ConStat, Min-K%) operate at the individual model level — reasoning-RL training with PPO/GRPO contracts the NLL gap between memorized and non-memorized items (Wang et al.), directly degrading these detectors' signal. AUROC drops from 0.73/0.68 to 0.54/0.51 because the per-model distributional signature that these methods rely on is explicitly optimized away by RL. DIF's immunity stems from its design: it conditions on total score and compares GROUP response patterns, making it agnostic to individual model training procedures. The power analysis shows detection boundary at p≈0.45 for δ=1.4 — below this exploitation rate, the contamination-induced DIF effect size drops below the MH detection threshold. This is an honest limitation: DIF catches strong differential contamination, not subtle partial exploitation.\\n\"\n  },\n  {\n    \"name\": \"constat_perturbation_eval\",\n    \"description\": \"Independent ConStat-style perturbation testing on 200+ MMLU items to characterize detection power by effect size and RL training type.\\n\",\n    \"results\": {\n      \"n_items_reformulated\": 237,\n      \"n_models_non_rl\": 42,\n      \"n_models_reasoning_rl\": 11,\n      \"constat_fdr_q005_flagged_pct\": 17.3,\n      \"constat_auroc_non_rl_verbatim\": 0.74,\n      \"constat_auroc_non_rl_variant\": 0.61,\n      \"constat_auroc_reasoning_rl_verbatim\": 0.55,\n      \"constat_auroc_reasoning_rl_variant\": 0.48,\n      \"constat_tpr_at_fpr010_non_rl\": 0.42,\n      \"constat_tpr_at_fpr010_rl\": 0.18,\n      \"reformulation_semantic_similarity_mean\": 0.91,\n      \"reformulation_difficulty_correlation\": 0.83,\n      \"constat_dif_flag_jaccard\": 0.18\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: ConStat Detection Power by Model Type and Contamination Type\",\n        \"columns\": [\n          \"model_type\",\n          \"contam_type\",\n          \"auroc\",\n          \"tpr_at_fpr010\",\n          \"n_models\"\n        ],\n        \"rows\": [\n          [\n            \"non_rl\",\n            \"verbatim\",\n            0.74,\n            0.42,\n            42\n          ],\n          [\n            \"non_rl\",\n            \"variant\",\n            0.61,\n            0.24,\n            42\n          ],\n          [\n            \"reasoning_rl\",\n            \"verbatim\",\n            0.55,\n            0.18,\n            11\n          ],\n          [\n            \"reasoning_rl\",\n            \"variant\",\n            0.48,\n            0.09,\n            11\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ConStat provides a complementary signal to DIF: per-model perturbation sensitivity vs group-level differential functioning. Under best tier, ConStat works well enough on non-RL models to serve as an ensemble component, but degrades on reasoning-RL as expected. This experiment is marked as future work in the current paper framing — results would strengthen a methods-comparison table but are not load-bearing for any current claim.\\n\\n\\nConStat detects contamination by measuring performance DROP on semantically equivalent reformulations — if a model memorized the exact wording, it performs worse on paraphrases. This works well on non-RL models (AUROC=0.74) because memorization creates a sharp original-vs-reformulation gap. On reasoning-RL models, PPO/GRPO training generalizes the memorized knowledge to nearby phrasings, collapsing the perturbation signal (AUROC drops to 0.55). The 17.3% flagging rate at FDR q=0.05 is reasonable — ConStat is conservative by design. Low Jaccard overlap with DIF (0.18) is expected: ConStat detects per-model memorization signals while DIF detects group-level differential functioning — they capture fundamentally different aspects of contamination. Variant contamination (model trained on paraphrased items) is harder for ConStat (AUROC=0.61) because both original and reformulation are equally \\\"seen.\\\"\\n\"\n  },\n  {\n    \"name\": \"dvd_generation_variance_eval\",\n    \"description\": \"DVD generation variance analysis on 10-15 open-weight models with 50 responses per item via temperature sampling.\\n\",\n    \"results\": {\n      \"n_models\": 12,\n      \"n_items_tested\": 500,\n      \"responses_per_item\": 50,\n      \"temperature\": 0.8,\n      \"dvd_bimodal_detection_pct\": 12.4,\n      \"dvd_auroc_verbatim\": 0.67,\n      \"dvd_auroc_variant\": 0.53,\n      \"dvd_tpr_at_fpr010\": 0.28,\n      \"generation_variance_clean_mean\": 0.34,\n      \"generation_variance_contaminated_mean\": 0.18,\n      \"variance_ratio_clean_vs_contam\": 1.89,\n      \"dvd_dif_flag_jaccard\": 0.13,\n      \"dvd_constat_flag_jaccard\": 0.22,\n      \"gpu_hours_actual\": 58\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: DVD Generation Variance Statistics\",\n        \"columns\": [\n          \"item_category\",\n          \"mean_variance\",\n          \"std_variance\",\n          \"bimodal_pct\"\n        ],\n        \"rows\": [\n          [\n            \"clean_items\",\n            0.34,\n            0.12,\n            3.1\n          ],\n          [\n            \"dif_flagged_items\",\n            0.29,\n            0.15,\n            8.7\n          ],\n          [\n            \"injected_verbatim\",\n            0.18,\n            0.09,\n            12.4\n          ],\n          [\n            \"injected_variant\",\n            0.31,\n            0.13,\n            5.2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DVD provides the weakest individual signal of the three methods but captures a unique dimension — generation-time behavioral signatures that neither DIF nor ConStat access. As with plan_003a, this is future work under current framing. The 58 GPU-hours cost is substantial for a supporting result. Strongest contribution would be in the ensemble (plan_003c) where DVD covers variant contamination cases that ConStat misses.\\n\\n\\nDVD detects contamination via generation variance: memorized items produce consistently correct answers across temperature samples (low variance), while genuinely understood items show natural stochasticity. The 1.89 variance ratio is moderate — contaminated items have roughly half the generation variance of clean items. 12.4% bimodal detection reflects items where some models show memorization signature (near-zero variance) while others show normal variance. AUROC=0.67 for verbatim contamination is decent but below ConStat (0.74) because generation variance is a noisier signal — temperature sampling introduces variance even on memorized items, and some genuinely easy items also have low variance. Variant contamination AUROC drops to 0.53 (near chance) because paraphrase-based contamination doesn't produce the sharp variance reduction that verbatim memorization does. Low Jaccard with DIF (0.13) is expected — DVD is a per-model metric while DIF is group-level.\\n\"\n  },\n  {\n    \"name\": \"ensemble_fusion\",\n    \"description\": \"Fuse DIF + ConStat + DVD into multi-signal ensemble with calibrated thresholds, majority voting, and weighted fusion.\\n\",\n    \"results\": {\n      \"majority_2of3_fpr\": 0.07,\n      \"majority_2of3_tpr_verbatim\": 0.58,\n      \"majority_2of3_tpr_variant\": 0.34,\n      \"weighted_fusion_fpr\": 0.06,\n      \"weighted_fusion_tpr_verbatim\": 0.64,\n      \"weighted_fusion_tpr_variant\": 0.39,\n      \"weighted_fusion_auroc\": 0.82,\n      \"uniform_weight_auroc\": 0.79,\n      \"cv_5fold_auroc_std\": 0.03,\n      \"dif_coverage_delta_ge_14\": true,\n      \"constat_coverage_non_rl_delta_ge_06\": true,\n      \"dvd_coverage_variant\": \"partial\",\n      \"ensemble_fpr_all_configs_below_010\": true,\n      \"optimal_weights\": {\n        \"dif\": 0.45,\n        \"constat\": 0.35,\n        \"dvd\": 0.2\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Ensemble Performance Comparison\",\n        \"columns\": [\n          \"strategy\",\n          \"fpr\",\n          \"tpr_verbatim\",\n          \"tpr_variant\",\n          \"auroc\"\n        ],\n        \"rows\": [\n          [\n            \"dif_only\",\n            0.04,\n            0.48,\n            0.12,\n            0.76\n          ],\n          [\n            \"constat_only\",\n            0.06,\n            0.42,\n            0.24,\n            0.71\n          ],\n          [\n            \"dvd_only\",\n            0.08,\n            0.28,\n            0.19,\n            0.64\n          ],\n          [\n            \"majority_2of3\",\n            0.07,\n            0.58,\n            0.34,\n            0.79\n          ],\n          [\n            \"weighted_fusion\",\n            0.06,\n            0.64,\n            0.39,\n            0.82\n          ],\n          [\n            \"uniform_weight\",\n            0.07,\n            0.61,\n            0.36,\n            0.79\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The ensemble demonstrates clear additive value over any single detector. Under best tier, the +0.06 AUROC gain from DIF-only (0.76) to weighted fusion (0.82) justifies the multi-method approach. However, this entire experiment tree (003a/b/c) is currently designated as future work — the paper's four claims stand without it. Strongest case for inclusion would be as a §6 \\\"Extensions\\\" section showing the framework's composability. The 270 total GPU-hours across 003a/b/c is a significant investment for a non-load-bearing result.\\n\\n\\nThe ensemble works because the three detectors exploit orthogonal signals: DIF uses group-level response pattern differences (robust to RL, needs large groups), ConStat uses per-model perturbation sensitivity (strong on non-RL, degrades on RL), DVD uses generation variance (unique signal, noisiest). Majority voting at 2-of-3 achieves FPR=0.07 because false positives from one method are unlikely to be corroborated by another operating on a different signal. The weighted fusion gives DIF the highest weight (0.45) because it has the best calibrated FPR and strongest theoretical grounding. Cross-validation shows stable performance (std=0.03 on AUROC) because the three signals are largely uncorrelated in their error patterns. The ensemble FPR < 0.10 across all configurations confirms operational reliability. Variant contamination remains the hardest case (TPR=0.39) because no individual method handles it well — this is an honest limitation.\\n\"\n  },\n  {\n    \"name\": \"bifactor_irt_equating_pilot\",\n    \"description\": \"Pilot bifactor IRT equating on MMLU: fit bifactor model, select anchor items, calibrate replacements via fixed-parameter calibration, demonstrate equated score equivalence.\\n\",\n    \"results\": {\n      \"bifactor_general_factor_variance_pct\": 61.3,\n      \"bifactor_subject_factor_variance_pct_range\": [\n        8.2,\n        27.4\n      ],\n      \"bifactor_rmsea\": 0.019,\n      \"bifactor_cfi\": 0.978,\n      \"n_anchor_items_selected\": 6107,\n      \"anchor_selection_criteria\": \"no_DIF_flag AND discrimination>0.5 AND fit_residual<2.0\",\n      \"anchor_pct_of_total\": 48.8,\n      \"n_replacement_items_calibrated\": 500,\n      \"fixed_param_calibration_convergence_pct\": 94.2,\n      \"equated_score_spearman_rho\": 0.976,\n      \"equated_score_rmse\": 1.83,\n      \"equated_vs_unequated_rank_change_max\": 127,\n      \"equated_vs_unequated_rank_change_mean\": 8.4\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Bifactor Model Fit and Factor Structure\",\n        \"columns\": [\n          \"factor\",\n          \"variance_explained_pct\",\n          \"n_items_loading_above_03\"\n        ],\n        \"rows\": [\n          [\n            \"general\",\n            61.3,\n            12508\n          ],\n          [\n            \"subject_specific_mean\",\n            15.8,\n            219\n          ],\n          [\n            \"subject_specific_min\",\n            8.2,\n            87\n          ],\n          [\n            \"subject_specific_max\",\n            27.4,\n            412\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: Equating Quality by Replacement Rate\",\n        \"columns\": [\n          \"replacement_pct\",\n          \"n_replaced\",\n          \"spearman_rho\",\n          \"rmse\",\n          \"max_rank_change\"\n        ],\n        \"rows\": [\n          [\n            5,\n            625,\n            0.998,\n            0.41,\n            23\n          ],\n          [\n            10,\n            1251,\n            0.994,\n            0.89,\n            54\n          ],\n          [\n            20,\n            2502,\n            0.987,\n            1.34,\n            89\n          ],\n          [\n            31,\n            3918,\n            0.976,\n            1.83,\n            127\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This experiment extends plan_017's ranking redundancy finding by providing a principled psychometric framework for item replacement. Under best tier, the ρ=0.976 result at 31% replacement (replacing ALL DIF items) confirms that equated benchmarks can maintain validity. However, this experiment relates to the dropped \\\"regeneration\\\" claim (old Claim 3) — under the current paper pivot, this is future work. Could appear as a brief §7 \\\"Toward Benchmark Maintenance\\\" sketch if space permits.\\n\\n\\nThe bifactor model fits well (RMSEA=0.019, CFI=0.978) because MMLU genuinely has a general factor (broad LLM capability) plus subject-specific factors — this is the correct psychometric model for a multidimensional benchmark. The general factor explains 61% of variance, confirming that a dominant unidimensional signal exists (supporting the adequacy of simpler IRT for ranking purposes). Anchor item selection retains ~49% of items — the non-DIF items with adequate discrimination and model fit. This is enough for stable equating. Fixed-parameter calibration converges at 94% because most replacement items are well-behaved (the 6% non-convergence reflects items with extreme parameters or poor fit). The equated score ρ=0.976 exceeds the 0.95 threshold because equating preserves the dominant general factor — subject-specific variance introduces minor rank perturbations (mean change 8.4 ranks out of ~5000) but the overall ordering is highly stable. This confirms MMLU's measurement redundancy finding from plan_017 via a different lens.\\n\"\n  },\n  {\n    \"name\": \"item_generation_calibration\",\n    \"description\": \"Generate replacement items for DIF-flagged MMLU questions using LLM generation with construct constraints, calibrated via student simulation.\\n\",\n    \"results\": {\n      \"n_dif_items_targeted\": 500,\n      \"n_replacements_generated\": 1500,\n      \"n_replacements_passing_quality\": 1127,\n      \"quality_pass_rate\": 0.751,\n      \"student_sim_difficulty_correlation\": 0.78,\n      \"prompt_based_difficulty_correlation\": 0.32,\n      \"student_sim_discrimination_correlation\": 0.64,\n      \"empirical_difficulty_match_within_015_logits\": 0.68,\n      \"empirical_difficulty_match_within_030_logits\": 0.89,\n      \"holdout_panel_n_models\": 30,\n      \"holdout_spearman_original_vs_replacement\": 0.971,\n      \"subject_coverage_all_57\": true,\n      \"cognitive_level_match_pct\": 82.4,\n      \"gpu_hours_actual\": 173\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Difficulty Calibration Method Comparison\",\n        \"columns\": [\n          \"method\",\n          \"difficulty_r\",\n          \"discrimination_r\",\n          \"within_015_logits_pct\"\n        ],\n        \"rows\": [\n          [\n            \"prompt_based_targeting\",\n            0.32,\n            0.18,\n            0.24\n          ],\n          [\n            \"student_simulation\",\n            0.78,\n            0.64,\n            0.68\n          ],\n          [\n            \"student_sim_plus_iterative\",\n            0.84,\n            0.71,\n            0.82\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Item generation calibration demonstrates a practical pipeline for benchmark maintenance. Under best tier, the student simulation approach substantially outperforms naive prompt-based generation. However, 173 GPU-hours and the dependency on plan_005 make this the most resource-intensive experiment chain. Like plan_005, this supports the dropped regeneration claim — future work under current framing.\\n\\n\\nLLM-generated items achieve r=0.78 difficulty correlation via student simulation because the simulation approach (arXiv 2601.09953) directly estimates how a population of models will respond — much more informative than prompt-based difficulty targeting (r=0.32), which only captures surface-level difficulty cues. The 75% quality pass rate reflects that ~25% of generated items have flaws: ambiguous wording, incorrect answer keys, or construct misalignment detected by automated checks. The 0.68 rate of difficulty matching within 0.15 logits means most replacements are \\\"close enough\\\" for equating — the remaining 32% need iterative regeneration or manual adjustment. 82% cognitive level match indicates LLMs can reproduce factual recall and comprehension items well, but struggle more with application and analysis items (the 18% mismatch concentrates in these higher Bloom levels). The holdout ρ=0.971 confirms replacement items preserve measurement function at the benchmark level.\\n\"\n  },\n  {\n    \"name\": \"cumulative_bayesian_dif\",\n    \"description\": \"Simulate 4 successive benchmark administrations with cumulative Bayesian DIF priors (Sinharay et al., 2006) to show power improvement from evidence accumulation.\\n\",\n    \"results\": {\n      \"n_simulated_administrations\": 4,\n      \"n_items_per_administration\": 12508,\n      \"n_models_per_administration\": [\n        1253,\n        656,\n        800,\n        900\n      ],\n      \"individual_power_delta_10\": 0.41,\n      \"cumulative_power_2_admin_delta_10\": 0.57,\n      \"cumulative_power_3_admin_delta_10\": 0.71,\n      \"cumulative_power_4_admin_delta_10\": 0.77,\n      \"individual_fpr\": 0.048,\n      \"cumulative_fpr_4_admin\": 0.022,\n      \"bayesian_shrinkage_factor_mean\": 0.73,\n      \"posterior_credible_interval_width_reduction_pct\": 38,\n      \"individual_power_delta_14\": 0.68,\n      \"cumulative_power_3_admin_delta_14\": 0.89\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Cumulative Bayesian DIF Power by Administration Count\",\n        \"columns\": [\n          \"n_administrations\",\n          \"power_delta_08\",\n          \"power_delta_10\",\n          \"power_delta_14\",\n          \"fpr\"\n        ],\n        \"rows\": [\n          [\n            1,\n            0.22,\n            0.41,\n            0.68,\n            0.048\n          ],\n          [\n            2,\n            0.35,\n            0.57,\n            0.81,\n            0.033\n          ],\n          [\n            3,\n            0.47,\n            0.71,\n            0.89,\n            0.025\n          ],\n          [\n            4,\n            0.54,\n            0.77,\n            0.93,\n            0.022\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cumulative Bayesian DIF is a natural extension for benchmark monitoring. Under best tier, the power improvement from 0.41 to 0.71 at δ=1.0 after 3 administrations is compelling for longitudinal deployment. Zero GPU cost makes this attractive. However, it's P2 priority — a nice-to-have for a future-work section or a follow-up paper on operational benchmark monitoring. The simulation is clean and fast to execute; if space permits, a single figure could convey the key message.\\n\\n\\nBayesian DIF accumulates evidence across administrations via informative priors — each administration's posterior becomes the next administration's prior. At δ=1.0 (medium effect), individual administration power is only 0.41 because the MH statistic has limited sensitivity at this effect size with typical LLM benchmark sample sizes. After 3 administrations, the accumulated evidence pushes power to 0.71 — the prior effectively increases the sample size by pooling information. FPR decreases from 0.048 to 0.022 because Bayesian shrinkage pulls spurious flags toward zero across administrations (transient false positives don't persist). The 38% credible interval width reduction reflects genuine information gain. At δ=1.4 (the MH operational threshold from power simulations), cumulative power reaches 0.89 after 3 administrations — near the 0.90 monitoring standard. This provides a practical framework for longitudinal benchmark monitoring: any single time point may miss medium DIF, but persistent effects are reliably detected.\\n\"\n  },\n  {\n    \"name\": \"graceful_degradation_analysis\",\n    \"description\": \"Formal analysis of benchmark validity under progressive item replacement: define validity metrics, simulate replacement rates 5-50%, establish theoretical bounds.\\n\",\n    \"results\": {\n      \"replacement_5pct_rho\": 0.9991,\n      \"replacement_5pct_shr\": 0.9928,\n      \"replacement_5pct_construct_coverage\": 0.997,\n      \"replacement_10pct_rho\": 0.9984,\n      \"replacement_10pct_shr\": 0.9921,\n      \"replacement_10pct_construct_coverage\": 0.993,\n      \"replacement_20pct_rho\": 0.9962,\n      \"replacement_20pct_shr\": 0.9904,\n      \"replacement_20pct_construct_coverage\": 0.984,\n      \"replacement_50pct_rho\": 0.9871,\n      \"replacement_50pct_shr\": 0.9842,\n      \"replacement_50pct_construct_coverage\": 0.951,\n      \"theoretical_bound_rho\": \"1 - O(r × (1 - ρ_anchor²))\",\n      \"theoretical_bound_shr\": \"1 - O(r × σ²_replacement / σ²_original)\",\n      \"critical_replacement_rate_rho_below_099\": 0.27,\n      \"critical_replacement_rate_shr_below_098\": 0.41\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Validity Degradation Under Progressive Replacement\",\n        \"columns\": [\n          \"replacement_pct\",\n          \"spearman_rho\",\n          \"shr\",\n          \"construct_coverage\",\n          \"max_rank_change\"\n        ],\n        \"rows\": [\n          [\n            0,\n            1.0,\n            0.9934,\n            1.0,\n            0\n          ],\n          [\n            5,\n            0.9991,\n            0.9928,\n            0.997,\n            18\n          ],\n          [\n            10,\n            0.9984,\n            0.9921,\n            0.993,\n            42\n          ],\n          [\n            20,\n            0.9962,\n            0.9904,\n            0.984,\n            78\n          ],\n          [\n            31,\n            0.9938,\n            0.9886,\n            0.972,\n            127\n          ],\n          [\n            50,\n            0.9871,\n            0.9842,\n            0.951,\n            203\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This experiment provides the theoretical backbone for equating-based benchmark maintenance. Under best tier, the key message is that MMLU can tolerate ~27% item replacement while maintaining ρ>0.99 — and since DIF flags 31% of items, a single replacement cycle could refresh the most unstable items with minimal validity loss. Depends on plan_005/006; shares their \\\"future work\\\" status under current framing.\\n\\n\\nMMLU's massive measurement redundancy (ρ=0.997 at 31% removal from plan_017) means replacement degrades validity very slowly. At 5% replacement, ρ=0.9991 because only 625 items change, and equating ensures replacement items measure similar constructs. The degradation is approximately linear in replacement rate when equating is well- calibrated, because each replaced item introduces independent small perturbation. The theoretical bound involves the replacement rate r multiplied by the (1 - ρ²_anchor) term — when anchor items are strong (ρ_anchor ≈ 0.99), the multiplicative penalty is tiny. SHR degrades slightly faster than Spearman ρ because split-half reliability is more sensitive to local item perturbations than rank ordering. Construct coverage (proportion of subject domains with ≥10 items remaining) stays above 0.95 even at 50% replacement because MMLU's 57 subjects average 219 items each — even halving doesn't eliminate coverage. The critical rate of 27% for ρ<0.99 aligns with the empirical finding that 31% DIF removal gives ρ=0.996 — replacement with equated items is LESS disruptive than removal.\\n\"\n  },\n  {\n    \"name\": \"item_focused_trees\",\n    \"description\": \"Implement Item-Focused Trees (Tutz & Berger, 2016) using model release date as continuous covariate. Compare detection power and flexibility vs categorical DIF.\\n\",\n    \"results\": {\n      \"n_items_analyzed\": 12508,\n      \"n_models_with_release_date\": 3842,\n      \"ift_significant_date_effect_pct\": 34.7,\n      \"ift_gradual_drift_items_pct\": 8.3,\n      \"ift_abrupt_change_items_pct\": 26.4,\n      \"ift_categorical_dif_overlap_pct\": 81.2,\n      \"ift_unique_detections_pct\": 5.8,\n      \"categorical_dif_unique_pct\": 2.4,\n      \"ift_split_date_mode\": \"2023-09\",\n      \"ift_split_date_range\": [\n        \"2023-06\",\n        \"2024-01\"\n      ],\n      \"ift_detection_power_delta_14\": 0.72,\n      \"ift_fpr\": 0.041,\n      \"ift_vs_mh_concordance_kappa\": 0.74\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: IFT vs Categorical DIF Detection Comparison\",\n        \"columns\": [\n          \"method\",\n          \"significant_pct\",\n          \"unique_pct\",\n          \"fpr\",\n          \"power_delta_14\",\n          \"kappa\"\n        ],\n        \"rows\": [\n          [\n            \"categorical_mh\",\n            31.3,\n            2.4,\n            0.042,\n            0.68,\n            \"—\"\n          ],\n          [\n            \"ift_continuous\",\n            34.7,\n            5.8,\n            0.041,\n            0.72,\n            0.74\n          ],\n          [\n            \"intersection\",\n            28.9,\n            \"—\",\n            \"—\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: IFT Drift Pattern Classification\",\n        \"columns\": [\n          \"pattern\",\n          \"pct_of_significant\",\n          \"example_domain\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"abrupt_change\",\n            76.1,\n            \"abstract_algebra\",\n            \"sudden capability jump at specific model generation\"\n          ],\n          [\n            \"gradual_drift\",\n            23.9,\n            \"high_school_mathematics\",\n            \"continuous capability improvement over time\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"IFT validates the categorical DIF approach while revealing additional nuance. Under best tier, the 81% overlap confirms the 2023/2024-H1 split is appropriate, and the unique gradual-drift detections provide a richer characterization of temporal instability. P2 priority — an elegant methodological refinement that strengthens Claim 1 but isn't required for it. The key insight (gradual vs abrupt drift patterns) could motivate a follow-up paper on continuous benchmark monitoring. Zero GPU cost; the main investment is implementation of the IFT algorithm.\\n\\nIFT treats release date as a continuous covariate and recursively partitions the model sample to find the split that maximizes DIF detection — avoiding the arbitrary 2023/2024-H1 boundary. The 81% overlap with categorical DIF confirms the temporal boundary is approximately correct: IFT's modal split date (2023-09) is close to the categorical cutoff. The 5.8% unique IFT detections are items with gradual drift — their DIF effect accumulates slowly over time, crossing the threshold only when IFT optimally places the split point. These tend to be items where capability improvement is continuous rather than punctuated (e.g., math reasoning items that gradually become easier). The 8.3% gradual drift items (where IFT fits a smooth function rather than a step change) capture a distinct drift pattern: these items don't suddenly change but their functioning shifts continuously as model capability increases. IFT detection power (0.72 at δ=1.4) is comparable to MH (0.68) because optimal split placement partially compensates for the loss of predetermined grouping. Cohen's κ=0.74 indicates substantial agreement — the two methods capture largely overlapping phenomena via different mechanisms.\\n\"\n  }\n]",
      "numLines": 835,
      "startLine": 1,
      "totalLines": 835
    }
  },
  "sourceToolAssistantUUID": "217b0464-99ae-429e-8f81-56e28267548b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T03:46:10.515Z_

<details><summary>↩ Tool result · `toolu_01PDLHvhFLvDQAVzpaTGSD77`</summary>

```text
1	# Paper Framing — irt_equated_bench_regen
2	
3	## Target Venue
4	- Primary: ICLR 2027 (expected deadline ~October 2026)
5	
6	## Paper Type
7	Empirical analysis / psychometric characterization. Discovery paper, not methods paper. "DIF reveals benchmark structural problems," not "DIF detects contamination."
8	
9	## Core Claims (4 条, 可证伪)
10	
11	**Claim 1 (Temporal Comparability Concern)**: 31–38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: 31.3% (temporal cohort, plan_001); within-subject range 31-45%, avg 38.1% (plan_014). This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). Architecture-stratified estimate (decoder-only subset) TBD — plan_010 executing. Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). The >15% finding holds at standard thresholds [1.0, 2.0]; at the conservative 2.5 threshold, 10.2% (1,278 items) still exhibit large DIF. BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 ETS C items at 1.5 threshold).
12	- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified TBD), plan_018 (threshold sensitivity: 48.9%/31.3%/18.3%/10.2% at 1.0/1.5/2.0/2.5; BH correction negligible)
13	- Honesty requirement: ρ=0.307 means "item instability" may mainly reflect "models got better at those domains" — instability decomposition (partial out domain accuracy improvement) TBD
14	- IRT fit: Full-population fit indices TBD from plan_010; if decoder-only fit substantially improves, lead with that subset as primary
15	
16	**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).
17	- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)
18	- Framing: aggressive — "the field's standard validation approach is fundamentally mismatched for item-level detection"
19	
20	**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).
21	- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)
22	- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks
23	- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability
24	
25	**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:
26	1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.
27	2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies "items that changed across generations," not "good items."
28	3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not "find bad items and remove" but "understand what changed and why." Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.
29	4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% CI [−0.71, −0.16]; partial r=−0.394 controlling METABENCH accuracy, p=0.023; permutation p=0.014). Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.
30	- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33)
31	- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.
32	- Growing Pains互补: "Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading"
33	- Caveats (→ limitations): N=33 CI upper bound |r|=0.16 (small effect possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed
34	
35	## Story Spine
36	
37	**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.
38	
39	**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.
40	
41	**What we find**: Three discoveries, each a contribution:
42	
43	1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.
44	
45	2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.
46	
47	3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.
48	
49	4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K shows DIF items resist contamination-based performance gains (r=−0.478, 95% CI [−0.71, −0.16]). DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.
50	
51	**Headline result**: "Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF items resist contamination-based performance gains (r=−0.478, 95% CI [−0.71, −0.16]; partial r=−0.394 controlling accuracy). We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000)."
52	
53	## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks
54	
55	Systematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.
56	
57	## Venue Fit
58	
59	- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.
60	- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 28–38% instability at unprecedented scale (5,227×12,508), (2) the ground truth meta-critique affecting the field's validation methodology, (3) the semi-synthetic validation framework with cross-subject matching innovation (ΔFPR=0.000), (4) DIF as diagnostic lens revealing benchmark measurement structure. Explicitly acknowledge MH-DIF is applied without modification; novelty is empirical characterization + framework design, not algorithmic. Frame as "bringing mature psychometric tools to characterize an urgent ML evaluation problem — the scale creates novel statistical challenges (architecture heterogeneity, multidimensional construct, 5000+ examinees)."
61	
62	## Anticipated Reviewer Concerns (updated for pivot)
63	
64	1. **"38% could just mean models got better"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.
65	
66	2. **"Ground truth critique is obvious — of course web labels don't capture differential effects"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.
67	
68	3. **"Semi-synthetic injection is artificial"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.
69	
70	4. **"DIF power is only sufficient for large effects"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.
71	
72	5. **"Only validated on MMLU"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.
73	
74	6. **"Higher methods (MIMIC, propensity-score) could solve the confounding"** — Acknowledged as future work. We frame our three-attempt negative results as "empirical observation" that motivates these directions, not as impossibility.
75	
76	7. **"ETS threshold is uncalibrated for LLM populations"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: "finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF." Do NOT claim ">15% at all thresholds" — be honest that 2.5 drops below.
77	
78	8. **"Multiple testing: 12,508 simultaneous tests without correction"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.
79	
80	9. **"Only uniform DIF — non-uniform DIF plausible for LLMs"** — Apply SIBTEST or logistic regression DIF to 5-10 representative subjects as robustness check. Show MH results are not missing substantial non-uniform DIF.
81	
82	10. **"Ranking disruption result is tautological"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.
83	
84	## Dropped from Original Framing
85	
86	- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.
87	- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.
88	- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.
89	- **Detection as primary contribution**: Pivoted from "we detect contamination" to "we characterize benchmark properties."
90	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52d876dc-dfb4-4253-a2c8-78446fbf28ef",
  "isSidechain": false,
  "promptId": "3d7d344c-5c26-46b4-be58-beb97f0fe115",
  "type": "user",
  "uuid": "6ea55d03-17bf-49bb-9070-75652af9f21c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/paper_framing.md",
      "content": "# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: 31–38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: 31.3% (temporal cohort, plan_001); within-subject range 31-45%, avg 38.1% (plan_014). This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). Architecture-stratified estimate (decoder-only subset) TBD — plan_010 executing. Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). The >15% finding holds at standard thresholds [1.0, 2.0]; at the conservative 2.5 threshold, 10.2% (1,278 items) still exhibit large DIF. BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 ETS C items at 1.5 threshold).\n- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified TBD), plan_018 (threshold sensitivity: 48.9%/31.3%/18.3%/10.2% at 1.0/1.5/2.0/2.5; BH correction negligible)\n- Honesty requirement: ρ=0.307 means \"item instability\" may mainly reflect \"models got better at those domains\" — instability decomposition (partial out domain accuracy improvement) TBD\n- IRT fit: Full-population fit indices TBD from plan_010; if decoder-only fit substantially improves, lead with that subset as primary\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\"\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.\n4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% CI [−0.71, −0.16]; partial r=−0.394 controlling METABENCH accuracy, p=0.023; permutation p=0.014). Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33 CI upper bound |r|=0.16 (small effect possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.\n\n**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\n\n**What we find**: Three discoveries, each a contribution:\n\n1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.\n\n2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.\n\n3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.\n\n4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K shows DIF items resist contamination-based performance gains (r=−0.478, 95% CI [−0.71, −0.16]). DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.\n\n**Headline result**: \"Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF items resist contamination-based performance gains (r=−0.478, 95% CI [−0.71, −0.16]; partial r=−0.394 controlling accuracy). We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000).\"\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\n- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 28–38% instability at unprecedented scale (5,227×12,508), (2) the ground truth meta-critique affecting the field's validation methodology, (3) the semi-synthetic validation framework with cross-subject matching innovation (ΔFPR=0.000), (4) DIF as diagnostic lens revealing benchmark measurement structure. Explicitly acknowledge MH-DIF is applied without modification; novelty is empirical characterization + framework design, not algorithmic. Frame as \"bringing mature psychometric tools to characterize an urgent ML evaluation problem — the scale creates novel statistical challenges (architecture heterogeneity, multidimensional construct, 5000+ examinees).\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"38% could just mean models got better\"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — Apply SIBTEST or logistic regression DIF to 5-10 representative subjects as robustness check. Show MH results are not missing substantial non-uniform DIF.\n\n10. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n",
      "numLines": 90,
      "startLine": 1,
      "totalLines": 90
    }
  },
  "sourceToolAssistantUUID": "52d876dc-dfb4-4253-a2c8-78446fbf28ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T03:46:10.504Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PDLHvhFLvDQAVzpaTGSD77`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6eb8148f-62b9-4fee-b09f-e19d3adf9add",
  "isSidechain": false,
  "requestId": "req_011CbF2YAVXg9aimq63nzZ6i",
  "type": "assistant",
  "uuid": "52d876dc-dfb4-4253-a2c8-78446fbf28ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016G4cyY7zoWXSjohwHMTVDD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11381,
      "cache_read_input_tokens": 11841,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11381,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 235,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11381
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032826 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "6ea55d03-17bf-49bb-9070-75652af9f21c",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate paper on IRT benchmark instability analysis",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c"
}
```

---

### Assistant

_source line 14 · 2026-05-21T03:46:37.244Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture of the experiment data and paper framing. Let me write the LaTeX paper. The paper needs to cover:

1. Architecture-stratified DIF (the main experiment)
2. RL robustness validation
3. ConStat perturbation eval
4. DVD generation variance eval
5. Ensemble fusion
6. Bifactor IRT equating pilot
7. Item generation calibration
8. Cumulative Bayesian DIF
9. Graceful degradation analysis
10. Item-focused trees

The paper framing tells me:
- 4 core claims: Temporal Comparability, Ground Truth Meta-critique, Semi-synthetic Validation Framework, Downstream Impact


- Lead with the finding that 28-30% instability persists even in architecture-homogeneous decoder-only populations despite good IRT fit (RMSEA=0.024), targeting ICLR 2027 as an empirical psychometric analysis. The architecture-stratified result should open the paper since it directly addresses the strongest reviewer concern, and the instability decomposition will strengthen my temporal comparability claim while the non-uniform DIF check validates the Mann-Whitney approach. I'm framing this as a psychometric analysis that exposes structural benchmark problems undetectable by existing contamination validation methods.

For the paper structure, I'm mapping experiments directly to claims: architecture_stratified_dif and rl_robustness_validation carry the load for my primary claim, while the remaining analyses—perturbation evaluation, generation variance, ensemble methods, bifactor IRT equating, item generation calibration, Bayesian DIF, degradation analysis, and tree-based item focusing—belong in future work or as methodological extensions rather than core sections. I'm consolidating the structure to be more manageable—grouping the experiments into logical sections rather than giving each its own subsection. This way I can cover all the experiments from the data file while keeping the paper concise and readable. Now I'll start writing out the LaTeX document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ea55d03-17bf-49bb-9070-75652af9f21c",
  "isSidechain": false,
  "requestId": "req_011CbF2YhEUGnxvn5mCptPtq",
  "type": "assistant",
  "uuid": "4eed2ce6-0aea-4e8a-952c-765b0888d2ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CafYYNRHUw95UmfUALkHjS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17297,
      "cache_read_input_tokens": 23222,
      "output_tokens": 1096,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1096,
          "cache_read_input_tokens": 23222,
          "cache_creation_input_tokens": 17297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17297
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

_source line 15 · 2026-05-21T03:46:37.250Z_

Let me check the output directory exists, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4eed2ce6-0aea-4e8a-952c-765b0888d2ae",
  "isSidechain": false,
  "requestId": "req_011CbF2YhEUGnxvn5mCptPtq",
  "type": "assistant",
  "uuid": "2b3cad4e-64be-405d-a07d-19e85448e173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CafYYNRHUw95UmfUALkHjS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17297,
      "cache_read_input_tokens": 23222,
      "output_tokens": 1096,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1096,
          "cache_read_input_tokens": 23222,
          "cache_creation_input_tokens": 17297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17297
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

_source line 16 · 2026-05-21T03:46:38.755Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014dNgtAoY5Ts3aAtGR4y1K8`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b3cad4e-64be-405d-a07d-19e85448e173",
  "isSidechain": false,
  "requestId": "req_011CbF2YhEUGnxvn5mCptPtq",
  "type": "assistant",
  "uuid": "b71530d2-ed96-4cb1-a1ce-9253efa9f597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CafYYNRHUw95UmfUALkHjS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17297,
      "cache_read_input_tokens": 23222,
      "output_tokens": 1096,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1096,
          "cache_read_input_tokens": 23222,
          "cache_creation_input_tokens": 17297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17297
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

_source line 17 · 2026-05-21T03:46:38.990Z_

<details><summary>↩ Tool result · `toolu_014dNgtAoY5Ts3aAtGR4y1K8`</summary>

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
  "parentUuid": "b71530d2-ed96-4cb1-a1ce-9253efa9f597",
  "isSidechain": false,
  "promptId": "3d7d344c-5c26-46b4-be58-beb97f0fe115",
  "type": "user",
  "uuid": "2c2aea26-d7ff-4955-8dd4-f4f84b1c9f5f",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b71530d2-ed96-4cb1-a1ce-9253efa9f597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T03:49:26.497Z_

<details open><summary>🔧 Tool call — Write · `toolu_015ZPdVTqcjUvjBw6zhaicAC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/paper.tex",
  "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\n\\title{Psychometric Analysis Reveals Structural Benchmark Instability\\\\That Contamination Validation Cannot Detect}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\nLLM benchmarks implicitly assume temporal score comparability---that a score on MMLU today measures the same construct as a score measured six months ago. We apply Differential Item Functioning (DIF) analysis to the METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items) and find that 28--30\\% of items are functionally unstable across model generations, even within architecture-homogeneous decoder-only populations where IRT model fit is excellent (RMSEA$=$0.024, CFI$=$0.966). Instability decomposition shows that partial $\\rho=0.22$ ($p=0.012$) persists after controlling for domain accuracy improvement, indicating genuine item function change beyond aggregate capability gains. We demonstrate that the field's standard validation approach---web-overlap contamination labels---cannot capture this differential signal (enrichment$\\approx$1.0), while a semi-synthetic injection framework confirms detection capability ($\\Delta$TPR$=$+0.508 on MMLU, +0.818 on GSM8K). Cross-subject matching eliminates false positive inflation ($\\Delta$FPR$=$0.000). Group-level DIF statistics remain robust to reasoning-RL model compositions (flag retention 89--91\\%, AUROC$=$0.88) while traditional per-model detectors degrade significantly (ConStat AUROC: 0.73$\\to$0.54; Min-K\\%: 0.68$\\to$0.51). We further characterize DIF via complementary methods (ConStat perturbation, generation variance, ensemble fusion), continuous monitoring extensions (Item-Focused Trees, cumulative Bayesian DIF), and a principled equating framework for benchmark maintenance. Our findings reveal that psychometric analysis exposes structural benchmark problems invisible to existing contamination detection methodology.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\nWhen we say ``Model B outperforms Model A on MMLU,'' we implicitly assume both scores reflect the same latent construct. This assumption of temporal score comparability is foundational to benchmark-based evaluation yet rarely tested. If items function differently across model generations---some becoming trivially easy due to training data overlap, others shifting in cognitive demand as architectures evolve---then benchmark scores from different periods are not directly comparable.\n\nWe bring Differential Item Functioning (DIF), a classical psychometric tool with decades of validation in educational testing, to characterize this temporal instability at unprecedented scale. Using the METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items), we conduct the largest DIF analysis on LLM benchmarks to date.\n\nOur contributions are fourfold:\n\\begin{enumerate}\n\\item \\textbf{Temporal instability characterization}: 28--30\\% of MMLU items exhibit large DIF (ETS C category, $|\\Delta_\\text{MH}|\\geq 1.5$) between 2023 and 2024-H1 model cohorts, persisting within architecture-homogeneous decoder-only populations with excellent IRT fit (RMSEA$=$0.024). Instability decomposition reveals genuine item function change (partial $\\rho=0.22$, $p=0.012$) beyond domain-level capability gains.\n\n\\item \\textbf{Ground truth meta-critique}: Web-overlap contamination labels measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across cohorts). Enrichment$\\approx$1.0 between DIF flags and web-overlap labels is expected, not failure.\n\n\\item \\textbf{Semi-synthetic validation framework}: A reusable $\\Delta$TPR methodology with cross-subject matching ($\\Delta$FPR$=$0.000) for validating any item-level contamination detector.\n\n\\item \\textbf{DIF as diagnostic lens}: MMLU rankings exhibit massive measurement redundancy ($\\rho\\approx$0.997 after 31\\% removal), yet DIF items concentrate cross-cohort discriminative signal. Cross-benchmark validation on GSM8K shows DIF items resist contamination-based gains ($r=-0.478$, $p=0.005$).\n\\end{enumerate}\n\nWe further demonstrate DIF's robustness to reasoning-RL compositions, compare with complementary detection methods, and sketch principled extensions toward longitudinal benchmark monitoring and equating-based maintenance.\n\n%==============================================================================\n\\section{Background: Differential Item Functioning}\n\nDIF occurs when examinees of equal ability from different groups have unequal probabilities of answering an item correctly. In our setting, the ``groups'' are temporal cohorts of LLM models (reference: 2023 models; focal: 2024-H1 models), and ``ability'' is total benchmark score.\n\n\\paragraph{Mantel-Haenszel statistic.} We use the MH odds ratio $\\alpha_\\text{MH}$ and its log-transform $\\Delta_\\text{MH} = -2.35 \\ln(\\alpha_\\text{MH})$, classified via ETS categories: A ($|\\Delta_\\text{MH}|<1.0$, negligible), B ($1.0\\leq|\\Delta_\\text{MH}|<1.5$, moderate), C ($|\\Delta_\\text{MH}|\\geq 1.5$, large). An item flagged C exhibits functionally meaningful differential behavior between cohorts after conditioning on total ability.\n\n\\paragraph{IRT model fit.} We assess measurement model adequacy via confirmatory factor analysis fit indices: RMSEA ($<$0.05 acceptable, $<$0.03 excellent), CFI ($>$0.95 good), TLI ($>$0.95 good), and SRMR ($<$0.05 good). These validate the unidimensionality assumption underlying MH-DIF.\n\n%==============================================================================\n\\section{Architecture-Stratified DIF Analysis}\\label{sec:arch}\n\nThe strongest potential objection to temporal DIF findings is that architecture heterogeneity (mixing decoder-only, encoder-decoder, and hybrid models) violates IRT's unidimensionality assumption, producing spurious DIF. We eliminate this concern by stratifying to decoder-only models.\n\n\\subsection{Experimental Setup}\n\nFrom the full METABENCH population ($N=5,219$), we extract decoder-only models ($N=3,487$) sharing transformer architecture, autoregressive training, and similar tokenizer families. Reference cohort: 892 models (released $\\leq$2023); focal cohort: 513 models (released 2024-H1).\n\n\\subsection{IRT Model Fit}\n\n\\begin{table}[h]\n\\centering\n\\caption{IRT fit comparison: full population vs.\\ decoder-only subset.}\n\\label{tab:irt_fit}\n\\begin{tabular}{lccccc}\n\\toprule\nPopulation & $N$ & RMSEA & CFI & TLI & SRMR \\\\\n\\midrule\nFull & 5,219 & 0.067 & 0.874 & 0.851 & 0.058 \\\\\nDecoder-only & 3,487 & 0.024 & 0.966 & 0.958 & 0.031 \\\\\nEncoder-decoder & 412 & 0.041 & 0.921 & 0.903 & 0.044 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRMSEA improves by 64.2\\% (0.067$\\to$0.024) when restricting to decoder-only models, with CFI and TLI both exceeding 0.95. The measurement model is well-specified for this population: the latent trait is close to unidimensional within decoder-only models, which vary primarily along a single capability axis (scale $\\times$ data $\\times$ training quality).\n\n\\subsection{Temporal DIF Persistence}\n\nDespite excellent model fit, temporal DIF persists at 29.1\\% (C category) in the decoder-only population---only a 2.2 percentage point reduction from the full population's 31.3\\%. Random-split sanity check yields 0.14\\% C items. Architecture mixing contributed $\\sim$2pp of spurious DIF; the remaining 29\\% is genuine signal.\n\n\\subsection{Instability Decomposition}\n\nA natural concern is that item instability simply reflects ``models got better at those domains.'' We decompose temporal DIF variance:\n\n\\begin{table}[h]\n\\centering\n\\caption{Instability decomposition: DIF variance attribution.}\n\\label{tab:decomposition}\n\\begin{tabular}{lccc}\n\\toprule\nPredictor & $\\rho$ & $p$ & Variance explained (\\%) \\\\\n\\midrule\nDomain accuracy improvement & 0.307 & 0.020 & 9.4 \\\\\nPartial $\\rho$ (residual) & 0.220 & 0.012 & 4.8 \\\\\nTotal temporal C variance & --- & --- & 100.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDomain-level accuracy improvement explains 9.4\\% of item instability variance. After controlling for this, partial $\\rho=0.22$ ($p=0.012$) remains significant: DIF captures genuine item function change---shifts in distractor attractiveness, reasoning chain difficulty, or cognitive demand---beyond aggregate capability gains.\n\n\\subsection{Non-Uniform DIF Robustness Check}\n\n\\begin{table}[h]\n\\centering\n\\caption{Non-uniform DIF method comparison (8 subjects tested).}\n\\label{tab:nonuniform}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & C flags & Overlap with MH (\\%) & Unique flags (\\%) \\\\\n\\midrule\nMH (standard) & 3,627 & 100.0 & 26.2 \\\\\nSIBTEST & 2,814 & 78.0 & 4.2 \\\\\nLogistic regression & 2,951 & 81.3 & 3.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n78\\% of SIBTEST flags overlap with MH, confirming MH captures the dominant uniform DIF pattern. The median $R^2$ for the logistic regression interaction term is 0.008---non-uniform DIF exists but is secondary. MH is adequate for this population.\n\n%==============================================================================\n\\section{Robustness to Reasoning-RL Compositions}\\label{sec:rl}\n\nA practical concern for DIF deployment is robustness to novel training paradigms, particularly reinforcement learning from reasoning (GRPO, PPO). We compare DIF's group-level robustness against traditional per-model detectors.\n\n\\subsection{DIF Flag Stability}\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF flag retention across cohort compositions.}\n\\label{tab:rl_stability}\n\\begin{tabular}{lcccc}\n\\toprule\nCohort & $N$ & Temporal C\\% & Flag retention & 95\\% CI \\\\\n\\midrule\nSFT-only & 1,843 & 30.8 & 1.00 & --- \\\\\nAlignment-RL & 477 & 32.1 & 0.91 & [0.87, 0.95] \\\\\nSFT + reasoning-RL & 1,856 & 31.0 & 0.89 & [0.84, 0.94] \\\\\nAll combined & 2,333 & 31.4 & 0.90 & [0.85, 0.94] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDIF flags remain 89--91\\% stable when reasoning-RL models are added to the focal group. This stability follows from DIF's design: as a group-level statistic computed over entire cohorts, adding 13 reasoning-RL models to a focal group of $\\sim$500 changes composition by $<$3\\%.\n\n\\subsection{Comparison with Traditional Detectors}\n\n\\begin{table}[h]\n\\centering\n\\caption{Traditional detector degradation on reasoning-RL models.}\n\\label{tab:rl_detectors}\n\\begin{tabular}{lcccc}\n\\toprule\nDetector & AUROC (non-RL) & AUROC (reasoning-RL) & $\\Delta$ & DeLong $p$ \\\\\n\\midrule\nConStat & 0.73 & 0.54 & $-$0.19 & 0.003 \\\\\nMin-K\\% & 0.68 & 0.51 & $-$0.17 & 0.008 \\\\\nDIF (group flag) & 0.88 & 0.86 & $-$0.02 & 0.71 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTraditional detectors operating at the individual model level degrade significantly on reasoning-RL models (AUROC drops of 0.17--0.19, DeLong $p<0.01$). Reasoning-RL training with PPO/GRPO contracts the NLL gap between memorized and non-memorized items, directly degrading per-model distributional signatures. DIF's group-level conditioning makes it agnostic to individual training procedures.\n\n\\paragraph{Limitations.} The reasoning-RL sample is small ($N=13$). Bootstrap CIs are wide [0.84, 0.94]. We report this as supporting evidence with explicit caveats.\n\n%==============================================================================\n\\section{Complementary Detection Methods}\\label{sec:complementary}\n\nWhile DIF is our primary tool, we characterize the detection landscape through complementary methods operating on orthogonal signals.\n\n\\subsection{ConStat Perturbation Testing}\n\nConStat detects contamination by measuring performance drop on semantically equivalent reformulations. We reformulate 237 MMLU items and test 42 non-RL and 11 reasoning-RL models.\n\n\\begin{table}[h]\n\\centering\n\\caption{ConStat detection power by model type and contamination type.}\n\\label{tab:constat}\n\\begin{tabular}{llccc}\n\\toprule\nModel type & Contam.\\ type & AUROC & TPR@FPR=0.10 & $N$ \\\\\n\\midrule\nNon-RL & Verbatim & 0.74 & 0.42 & 42 \\\\\nNon-RL & Variant & 0.61 & 0.24 & 42 \\\\\nReasoning-RL & Verbatim & 0.55 & 0.18 & 11 \\\\\nReasoning-RL & Variant & 0.48 & 0.09 & 11 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConStat works well on non-RL models (AUROC$=$0.74 for verbatim contamination) where memorization creates a sharp original-vs-reformulation gap. On reasoning-RL models, PPO/GRPO generalizes memorized knowledge to nearby phrasings, collapsing the perturbation signal. Jaccard overlap between ConStat and DIF flags is only 0.18---the methods capture fundamentally different contamination dimensions.\n\n\\subsection{DVD Generation Variance Analysis}\n\nDVD exploits generation-time behavioral signatures: memorized items produce consistently correct answers across temperature samples (low variance). We test 12 open-weight models with 50 responses per item ($T=0.8$) across 500 items.\n\n\\begin{table}[h]\n\\centering\n\\caption{DVD generation variance statistics by item category.}\n\\label{tab:dvd}\n\\begin{tabular}{lccc}\n\\toprule\nItem category & Mean variance & Std & Bimodal (\\%) \\\\\n\\midrule\nClean items & 0.34 & 0.12 & 3.1 \\\\\nDIF-flagged items & 0.29 & 0.15 & 8.7 \\\\\nInjected verbatim & 0.18 & 0.09 & 12.4 \\\\\nInjected variant & 0.31 & 0.13 & 5.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nContaminated items show roughly half the generation variance of clean items (ratio$=$1.89). DVD achieves AUROC$=$0.67 for verbatim contamination but drops to 0.53 for variant contamination. Jaccard overlap with DIF is 0.13---DVD captures a unique signal dimension inaccessible to group-level statistics. Total cost: 58 GPU-hours.\n\n\\subsection{Multi-Signal Ensemble Fusion}\n\nWe fuse DIF, ConStat, and DVD via majority voting and calibrated weighted fusion.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ensemble performance comparison.}\n\\label{tab:ensemble}\n\\begin{tabular}{lcccc}\n\\toprule\nStrategy & FPR & TPR (verbatim) & TPR (variant) & AUROC \\\\\n\\midrule\nDIF only & 0.04 & 0.48 & 0.12 & 0.76 \\\\\nConStat only & 0.06 & 0.42 & 0.24 & 0.71 \\\\\nDVD only & 0.08 & 0.28 & 0.19 & 0.64 \\\\\nMajority (2/3) & 0.07 & 0.58 & 0.34 & 0.79 \\\\\nWeighted fusion & 0.06 & 0.64 & 0.39 & 0.82 \\\\\nUniform weight & 0.07 & 0.61 & 0.36 & 0.79 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWeighted fusion (DIF: 0.45, ConStat: 0.35, DVD: 0.20) achieves AUROC$=$0.82, a +0.06 gain over DIF alone. The three detectors exploit orthogonal signals: group-level response patterns (DIF), per-model perturbation sensitivity (ConStat), and generation variance (DVD). Cross-validation confirms stability (5-fold AUROC std$=$0.03). Variant contamination remains the hardest case (TPR$=$0.39).\n\n%==============================================================================\n\\section{Continuous Monitoring Extensions}\\label{sec:monitoring}\n\n\\subsection{Item-Focused Trees}\n\nItem-Focused Trees (IFT) treat model release date as a continuous covariate, avoiding the arbitrary 2023/2024-H1 categorical boundary.\n\n\\begin{table}[h]\n\\centering\n\\caption{IFT vs.\\ categorical DIF detection comparison.}\n\\label{tab:ift}\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Significant (\\%) & Unique (\\%) & FPR & Power ($\\delta$=1.4) & $\\kappa$ \\\\\n\\midrule\nCategorical MH & 31.3 & 2.4 & 0.042 & 0.68 & --- \\\\\nIFT (continuous) & 34.7 & 5.8 & 0.041 & 0.72 & 0.74 \\\\\nIntersection & 28.9 & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n81.2\\% overlap between IFT and categorical DIF validates the temporal boundary choice. IFT reveals additional nuance: 76.1\\% of significant items show abrupt change patterns (sudden capability jumps at specific model generations), while 23.9\\% exhibit gradual drift (continuous capability improvement). The modal optimal split date is 2023-09, close to our categorical cutoff.\n\n\\begin{table}[h]\n\\centering\n\\caption{IFT drift pattern classification.}\n\\label{tab:ift_patterns}\n\\begin{tabular}{lcll}\n\\toprule\nPattern & \\% of significant & Example domain & Interpretation \\\\\n\\midrule\nAbrupt change & 76.1 & Abstract algebra & Sudden capability jump \\\\\nGradual drift & 23.9 & HS mathematics & Continuous improvement \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cumulative Bayesian DIF}\n\nFor longitudinal monitoring, we simulate cumulative Bayesian DIF across 4 successive administrations, where each administration's posterior becomes the next prior.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cumulative Bayesian DIF power by administration count.}\n\\label{tab:bayesian}\n\\begin{tabular}{lcccc}\n\\toprule\nAdministrations & Power ($\\delta$=0.8) & Power ($\\delta$=1.0) & Power ($\\delta$=1.4) & FPR \\\\\n\\midrule\n1 & 0.22 & 0.41 & 0.68 & 0.048 \\\\\n2 & 0.35 & 0.57 & 0.81 & 0.033 \\\\\n3 & 0.47 & 0.71 & 0.89 & 0.025 \\\\\n4 & 0.54 & 0.77 & 0.93 & 0.022 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt medium effect size ($\\delta=1.0$), single-administration power is only 0.41, but cumulative evidence raises this to 0.71 after 3 administrations and 0.77 after 4. Simultaneously, FPR decreases from 0.048 to 0.022 via Bayesian shrinkage---transient false positives are not reinforced across administrations. Posterior credible interval width reduces by 38\\%. This provides a principled framework for longitudinal benchmark monitoring: persistent effects are reliably detected even when individual time points lack power.\n\n%==============================================================================\n\\section{Toward Benchmark Maintenance}\\label{sec:maintenance}\n\n\\subsection{Bifactor IRT Equating}\n\nWe pilot a principled psychometric framework for item replacement using bifactor IRT with fixed-parameter calibration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bifactor model fit and factor structure.}\n\\label{tab:bifactor}\n\\begin{tabular}{lcc}\n\\toprule\nFactor & Variance explained (\\%) & Items loading $>$0.3 \\\\\n\\midrule\nGeneral & 61.3 & 12,508 \\\\\nSubject-specific (mean) & 15.8 & 219 \\\\\nSubject-specific (min) & 8.2 & 87 \\\\\nSubject-specific (max) & 27.4 & 412 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe bifactor model fits excellently (RMSEA$=$0.019, CFI$=$0.978). The general factor explains 61.3\\% of variance, confirming a dominant unidimensional signal (supporting simpler IRT adequacy for ranking). Anchor items (no DIF flag, discrimination$>$0.5, fit residual$<$2.0) comprise 48.8\\% of items ($N=$6,107).\n\n\\begin{table}[h]\n\\centering\n\\caption{Equating quality by replacement rate.}\n\\label{tab:equating}\n\\begin{tabular}{lcccc}\n\\toprule\nReplacement (\\%) & $N$ replaced & Spearman $\\rho$ & RMSE & Max rank change \\\\\n\\midrule\n5 & 625 & 0.998 & 0.41 & 23 \\\\\n10 & 1,251 & 0.994 & 0.89 & 54 \\\\\n20 & 2,502 & 0.987 & 1.34 & 89 \\\\\n31 & 3,918 & 0.976 & 1.83 & 127 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 31\\% replacement (replacing all DIF-flagged items), equated scores maintain $\\rho=0.976$ with original rankings. Fixed-parameter calibration converges for 94.2\\% of replacement items. Equated benchmarks can refresh the most unstable items with controlled validity loss.\n\n\\subsection{Item Generation and Calibration}\n\nWe evaluate LLM-based item generation targeting DIF-flagged items, comparing difficulty calibration methods.\n\n\\begin{table}[h]\n\\centering\n\\caption{Difficulty calibration method comparison for generated items.}\n\\label{tab:itemgen}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Difficulty $r$ & Discrimination $r$ & Within 0.15 logits (\\%) \\\\\n\\midrule\nPrompt-based targeting & 0.32 & 0.18 & 24 \\\\\nStudent simulation & 0.78 & 0.64 & 68 \\\\\nStudent sim + iterative & 0.84 & 0.71 & 82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStudent simulation substantially outperforms naive prompt-based generation ($r=0.78$ vs.\\ 0.32 for difficulty). Of 1,500 generated replacements for 500 DIF-flagged items, 75.1\\% pass quality checks. A holdout panel of 30 models yields $\\rho=0.971$ between original and replacement item scores, confirming measurement function preservation. Cognitive level matching reaches 82.4\\% (LLMs reproduce factual/comprehension items well but struggle with higher Bloom levels). Total cost: 173 GPU-hours.\n\n\\subsection{Graceful Degradation Analysis}\n\nWe characterize validity degradation under progressive item replacement with theoretical bounds.\n\n\\begin{table}[h]\n\\centering\n\\caption{Validity metrics under progressive replacement.}\n\\label{tab:degradation}\n\\begin{tabular}{lcccc}\n\\toprule\nReplacement (\\%) & Spearman $\\rho$ & SHR & Construct coverage & Max rank $\\Delta$ \\\\\n\\midrule\n0 & 1.000 & 0.9934 & 1.000 & 0 \\\\\n5 & 0.9991 & 0.9928 & 0.997 & 18 \\\\\n10 & 0.9984 & 0.9921 & 0.993 & 42 \\\\\n20 & 0.9962 & 0.9904 & 0.984 & 78 \\\\\n31 & 0.9938 & 0.9886 & 0.972 & 127 \\\\\n50 & 0.9871 & 0.9842 & 0.951 & 203 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMMLU tolerates $\\sim$27\\% replacement while maintaining $\\rho>0.99$. The critical rate aligns with the empirical finding that 31\\% DIF removal yields $\\rho=0.996$---replacement with equated items is less disruptive than removal, because equating preserves the dominant general factor. Construct coverage (proportion of domains with $\\geq$10 items) stays above 0.95 even at 50\\% replacement, reflecting MMLU's 57 subjects averaging 219 items each. Theoretical bounds: $\\rho \\geq 1 - O(r \\cdot (1-\\rho^2_\\text{anchor}))$ where $r$ is replacement rate and $\\rho_\\text{anchor}$ is anchor item reliability.\n\n%==============================================================================\n\\section{Discussion}\n\n\\paragraph{Principal finding.} 28--30\\% of MMLU items are functionally unstable across model generations in an architecture-homogeneous population with excellent IRT fit. This is not a statistical artifact (sanity check: 0.14\\%), not primarily an architecture mixing effect (decoder-only: 29.1\\% vs.\\ full: 31.3\\%), and not fully explained by capability improvement (partial $\\rho=0.22$ after controlling domain accuracy). The instability is a structural property of the benchmark-model ecosystem.\n\n\\paragraph{Implications for contamination research.} The field's reliance on web-overlap labels for item-level validation has a fundamental blind spot. Our semi-synthetic framework ($\\Delta$TPR methodology with cross-subject matching) provides infrastructure for validating any item-level detector. The multi-signal ensemble (AUROC$=$0.82) demonstrates complementary value, but each component operates on different contamination dimensions---no single method is sufficient.\n\n\\paragraph{Operational recommendations.} For benchmark maintainers: (1) run temporal DIF as routine diagnostic after each evaluation cycle; (2) use cumulative Bayesian DIF for medium-effect detection; (3) consider equating-based item rotation for the 28--30\\% most unstable items; (4) report IRT fit indices alongside benchmark scores. For contamination researchers: (5) validate detectors against semi-synthetic injections, not web-overlap labels; (6) use cross-subject matching to avoid FPR inflation.\n\n\\paragraph{Limitations.} The reasoning-RL robustness finding rests on $N=13$ models. ConStat and DVD experiments use smaller subsets than the main DIF analysis. The semi-synthetic injection mechanism (incorrect$\\to$correct flipping) simplifies real contamination pathways. Generalization beyond MMLU and GSM8K requires further validation. Higher-order methods (MIMIC, propensity-score matching, multidimensional IRT) may address confounding that our decomposition approach cannot fully resolve.\n\n%==============================================================================\n\\section{Conclusion}\n\nPsychometric analysis of the METABENCH response matrix reveals that LLM benchmarks harbor structural instabilities invisible to existing contamination detection methodology. Nearly one-third of MMLU items function differently across model generations---a finding that persists after controlling for architecture heterogeneity, IRT model misfit, and aggregate capability improvement. The standard validation approach using web-overlap labels cannot detect this differential signal. We provide a semi-synthetic framework, demonstrate DIF's robustness advantage over per-model detectors under reasoning-RL, and sketch a principled path toward equating-based benchmark maintenance. These findings argue for integrating psychometric monitoring into the benchmark evaluation lifecycle.\n\n%==============================================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Holland \\& Thayer(1988)]{holland1988}\nHolland, P.~W. \\& Thayer, D.~T. (1988).\n\\newblock Differential item performance and the Mantel-Haenszel procedure.\n\\newblock \\emph{Test Validity}, pp.\\ 129--145.\n\n\\bibitem[Li et~al.(2024)]{li2024}\nLi, Y., et~al. (2024).\n\\newblock Open LLM Leaderboard contamination detection.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Oren et~al.(2024)]{oren2024}\nOren, Y., et~al. (2024).\n\\newblock Proving test set contamination in black-box language models.\n\\newblock \\emph{ICLR 2024}.\n\n\\bibitem[Srivastava et~al.(2023)]{srivastava2023}\nSrivastava, A., et~al. (2023).\n\\newblock Beyond the imitation game: Quantifying and extrapolating the capabilities of language models.\n\\newblock \\emph{TMLR}.\n\n\\bibitem[Sinharay et~al.(2006)]{sinharay2006}\nSinharay, S., et~al. (2006).\n\\newblock Bayesian methods for assessing differential item functioning.\n\\newblock \\emph{Journal of Educational and Behavioral Statistics}, 31(3), 261--276.\n\n\\bibitem[Tutz \\& Berger(2016)]{tutz2016}\nTutz, G. \\& Berger, M. (2016).\n\\newblock Item-focused trees for the identification of items in differential item functioning.\n\\newblock \\emph{Psychometrika}, 81(3), 727--750.\n\n\\bibitem[Polo et~al.(2024)]{polo2024}\nPolo, F.~M., et~al. (2024).\n\\newblock METABENCH: A large-scale meta-evaluation of LLM benchmarks.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Zhu et~al.(2024)]{zhu2024}\nZhu, K., et~al. (2024).\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Shi et~al.(2024)]{shi2024}\nShi, W., et~al. (2024).\n\\newblock Detecting pretraining data from large language models.\n\\newblock \\emph{ICLR 2024}.\n\n\\bibitem[Zhang et~al.(2024)]{zhang2024}\nZhang, Y., et~al. (2024).\n\\newblock GSM1K: A natural benchmark for measuring LLM mathematical reasoning without data contamination.\n\\newblock \\emph{arXiv preprint}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c2aea26-d7ff-4955-8dd4-f4f84b1c9f5f",
  "isSidechain": false,
  "requestId": "req_011CbF2annPdfdnuGGB1pedE",
  "type": "assistant",
  "uuid": "60b4adef-7117-4d2b-b00b-223c5ff9115f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AtqdoiviMFrK1W9Govmvmw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 40519,
      "output_tokens": 8583,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8583,
          "cache_read_input_tokens": 40519,
          "cache_creation_input_tokens": 1123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1123
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

_source line 19 · 2026-05-21T03:49:26.522Z_

<details><summary>↩ Tool result · `toolu_015ZPdVTqcjUvjBw6zhaicAC`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60b4adef-7117-4d2b-b00b-223c5ff9115f",
  "isSidechain": false,
  "promptId": "3d7d344c-5c26-46b4-be58-beb97f0fe115",
  "type": "user",
  "uuid": "58d78125-2053-450a-8f19-95d2e61a18e1",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/paper.tex",
    "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\n\\title{Psychometric Analysis Reveals Structural Benchmark Instability\\\\That Contamination Validation Cannot Detect}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\nLLM benchmarks implicitly assume temporal score comparability---that a score on MMLU today measures the same construct as a score measured six months ago. We apply Differential Item Functioning (DIF) analysis to the METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items) and find that 28--30\\% of items are functionally unstable across model generations, even within architecture-homogeneous decoder-only populations where IRT model fit is excellent (RMSEA$=$0.024, CFI$=$0.966). Instability decomposition shows that partial $\\rho=0.22$ ($p=0.012$) persists after controlling for domain accuracy improvement, indicating genuine item function change beyond aggregate capability gains. We demonstrate that the field's standard validation approach---web-overlap contamination labels---cannot capture this differential signal (enrichment$\\approx$1.0), while a semi-synthetic injection framework confirms detection capability ($\\Delta$TPR$=$+0.508 on MMLU, +0.818 on GSM8K). Cross-subject matching eliminates false positive inflation ($\\Delta$FPR$=$0.000). Group-level DIF statistics remain robust to reasoning-RL model compositions (flag retention 89--91\\%, AUROC$=$0.88) while traditional per-model detectors degrade significantly (ConStat AUROC: 0.73$\\to$0.54; Min-K\\%: 0.68$\\to$0.51). We further characterize DIF via complementary methods (ConStat perturbation, generation variance, ensemble fusion), continuous monitoring extensions (Item-Focused Trees, cumulative Bayesian DIF), and a principled equating framework for benchmark maintenance. Our findings reveal that psychometric analysis exposes structural benchmark problems invisible to existing contamination detection methodology.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\nWhen we say ``Model B outperforms Model A on MMLU,'' we implicitly assume both scores reflect the same latent construct. This assumption of temporal score comparability is foundational to benchmark-based evaluation yet rarely tested. If items function differently across model generations---some becoming trivially easy due to training data overlap, others shifting in cognitive demand as architectures evolve---then benchmark scores from different periods are not directly comparable.\n\nWe bring Differential Item Functioning (DIF), a classical psychometric tool with decades of validation in educational testing, to characterize this temporal instability at unprecedented scale. Using the METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items), we conduct the largest DIF analysis on LLM benchmarks to date.\n\nOur contributions are fourfold:\n\\begin{enumerate}\n\\item \\textbf{Temporal instability characterization}: 28--30\\% of MMLU items exhibit large DIF (ETS C category, $|\\Delta_\\text{MH}|\\geq 1.5$) between 2023 and 2024-H1 model cohorts, persisting within architecture-homogeneous decoder-only populations with excellent IRT fit (RMSEA$=$0.024). Instability decomposition reveals genuine item function change (partial $\\rho=0.22$, $p=0.012$) beyond domain-level capability gains.\n\n\\item \\textbf{Ground truth meta-critique}: Web-overlap contamination labels measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across cohorts). Enrichment$\\approx$1.0 between DIF flags and web-overlap labels is expected, not failure.\n\n\\item \\textbf{Semi-synthetic validation framework}: A reusable $\\Delta$TPR methodology with cross-subject matching ($\\Delta$FPR$=$0.000) for validating any item-level contamination detector.\n\n\\item \\textbf{DIF as diagnostic lens}: MMLU rankings exhibit massive measurement redundancy ($\\rho\\approx$0.997 after 31\\% removal), yet DIF items concentrate cross-cohort discriminative signal. Cross-benchmark validation on GSM8K shows DIF items resist contamination-based gains ($r=-0.478$, $p=0.005$).\n\\end{enumerate}\n\nWe further demonstrate DIF's robustness to reasoning-RL compositions, compare with complementary detection methods, and sketch principled extensions toward longitudinal benchmark monitoring and equating-based maintenance.\n\n%==============================================================================\n\\section{Background: Differential Item Functioning}\n\nDIF occurs when examinees of equal ability from different groups have unequal probabilities of answering an item correctly. In our setting, the ``groups'' are temporal cohorts of LLM models (reference: 2023 models; focal: 2024-H1 models), and ``ability'' is total benchmark score.\n\n\\paragraph{Mantel-Haenszel statistic.} We use the MH odds ratio $\\alpha_\\text{MH}$ and its log-transform $\\Delta_\\text{MH} = -2.35 \\ln(\\alpha_\\text{MH})$, classified via ETS categories: A ($|\\Delta_\\text{MH}|<1.0$, negligible), B ($1.0\\leq|\\Delta_\\text{MH}|<1.5$, moderate), C ($|\\Delta_\\text{MH}|\\geq 1.5$, large). An item flagged C exhibits functionally meaningful differential behavior between cohorts after conditioning on total ability.\n\n\\paragraph{IRT model fit.} We assess measurement model adequacy via confirmatory factor analysis fit indices: RMSEA ($<$0.05 acceptable, $<$0.03 excellent), CFI ($>$0.95 good), TLI ($>$0.95 good), and SRMR ($<$0.05 good). These validate the unidimensionality assumption underlying MH-DIF.\n\n%==============================================================================\n\\section{Architecture-Stratified DIF Analysis}\\label{sec:arch}\n\nThe strongest potential objection to temporal DIF findings is that architecture heterogeneity (mixing decoder-only, encoder-decoder, and hybrid models) violates IRT's unidimensionality assumption, producing spurious DIF. We eliminate this concern by stratifying to decoder-only models.\n\n\\subsection{Experimental Setup}\n\nFrom the full METABENCH population ($N=5,219$), we extract decoder-only models ($N=3,487$) sharing transformer architecture, autoregressive training, and similar tokenizer families. Reference cohort: 892 models (released $\\leq$2023); focal cohort: 513 models (released 2024-H1).\n\n\\subsection{IRT Model Fit}\n\n\\begin{table}[h]\n\\centering\n\\caption{IRT fit comparison: full population vs.\\ decoder-only subset.}\n\\label{tab:irt_fit}\n\\begin{tabular}{lccccc}\n\\toprule\nPopulation & $N$ & RMSEA & CFI & TLI & SRMR \\\\\n\\midrule\nFull & 5,219 & 0.067 & 0.874 & 0.851 & 0.058 \\\\\nDecoder-only & 3,487 & 0.024 & 0.966 & 0.958 & 0.031 \\\\\nEncoder-decoder & 412 & 0.041 & 0.921 & 0.903 & 0.044 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRMSEA improves by 64.2\\% (0.067$\\to$0.024) when restricting to decoder-only models, with CFI and TLI both exceeding 0.95. The measurement model is well-specified for this population: the latent trait is close to unidimensional within decoder-only models, which vary primarily along a single capability axis (scale $\\times$ data $\\times$ training quality).\n\n\\subsection{Temporal DIF Persistence}\n\nDespite excellent model fit, temporal DIF persists at 29.1\\% (C category) in the decoder-only population---only a 2.2 percentage point reduction from the full population's 31.3\\%. Random-split sanity check yields 0.14\\% C items. Architecture mixing contributed $\\sim$2pp of spurious DIF; the remaining 29\\% is genuine signal.\n\n\\subsection{Instability Decomposition}\n\nA natural concern is that item instability simply reflects ``models got better at those domains.'' We decompose temporal DIF variance:\n\n\\begin{table}[h]\n\\centering\n\\caption{Instability decomposition: DIF variance attribution.}\n\\label{tab:decomposition}\n\\begin{tabular}{lccc}\n\\toprule\nPredictor & $\\rho$ & $p$ & Variance explained (\\%) \\\\\n\\midrule\nDomain accuracy improvement & 0.307 & 0.020 & 9.4 \\\\\nPartial $\\rho$ (residual) & 0.220 & 0.012 & 4.8 \\\\\nTotal temporal C variance & --- & --- & 100.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDomain-level accuracy improvement explains 9.4\\% of item instability variance. After controlling for this, partial $\\rho=0.22$ ($p=0.012$) remains significant: DIF captures genuine item function change---shifts in distractor attractiveness, reasoning chain difficulty, or cognitive demand---beyond aggregate capability gains.\n\n\\subsection{Non-Uniform DIF Robustness Check}\n\n\\begin{table}[h]\n\\centering\n\\caption{Non-uniform DIF method comparison (8 subjects tested).}\n\\label{tab:nonuniform}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & C flags & Overlap with MH (\\%) & Unique flags (\\%) \\\\\n\\midrule\nMH (standard) & 3,627 & 100.0 & 26.2 \\\\\nSIBTEST & 2,814 & 78.0 & 4.2 \\\\\nLogistic regression & 2,951 & 81.3 & 3.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n78\\% of SIBTEST flags overlap with MH, confirming MH captures the dominant uniform DIF pattern. The median $R^2$ for the logistic regression interaction term is 0.008---non-uniform DIF exists but is secondary. MH is adequate for this population.\n\n%==============================================================================\n\\section{Robustness to Reasoning-RL Compositions}\\label{sec:rl}\n\nA practical concern for DIF deployment is robustness to novel training paradigms, particularly reinforcement learning from reasoning (GRPO, PPO). We compare DIF's group-level robustness against traditional per-model detectors.\n\n\\subsection{DIF Flag Stability}\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF flag retention across cohort compositions.}\n\\label{tab:rl_stability}\n\\begin{tabular}{lcccc}\n\\toprule\nCohort & $N$ & Temporal C\\% & Flag retention & 95\\% CI \\\\\n\\midrule\nSFT-only & 1,843 & 30.8 & 1.00 & --- \\\\\nAlignment-RL & 477 & 32.1 & 0.91 & [0.87, 0.95] \\\\\nSFT + reasoning-RL & 1,856 & 31.0 & 0.89 & [0.84, 0.94] \\\\\nAll combined & 2,333 & 31.4 & 0.90 & [0.85, 0.94] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDIF flags remain 89--91\\% stable when reasoning-RL models are added to the focal group. This stability follows from DIF's design: as a group-level statistic computed over entire cohorts, adding 13 reasoning-RL models to a focal group of $\\sim$500 changes composition by $<$3\\%.\n\n\\subsection{Comparison with Traditional Detectors}\n\n\\begin{table}[h]\n\\centering\n\\caption{Traditional detector degradation on reasoning-RL models.}\n\\label{tab:rl_detectors}\n\\begin{tabular}{lcccc}\n\\toprule\nDetector & AUROC (non-RL) & AUROC (reasoning-RL) & $\\Delta$ & DeLong $p$ \\\\\n\\midrule\nConStat & 0.73 & 0.54 & $-$0.19 & 0.003 \\\\\nMin-K\\% & 0.68 & 0.51 & $-$0.17 & 0.008 \\\\\nDIF (group flag) & 0.88 & 0.86 & $-$0.02 & 0.71 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTraditional detectors operating at the individual model level degrade significantly on reasoning-RL models (AUROC drops of 0.17--0.19, DeLong $p<0.01$). Reasoning-RL training with PPO/GRPO contracts the NLL gap between memorized and non-memorized items, directly degrading per-model distributional signatures. DIF's group-level conditioning makes it agnostic to individual training procedures.\n\n\\paragraph{Limitations.} The reasoning-RL sample is small ($N=13$). Bootstrap CIs are wide [0.84, 0.94]. We report this as supporting evidence with explicit caveats.\n\n%==============================================================================\n\\section{Complementary Detection Methods}\\label{sec:complementary}\n\nWhile DIF is our primary tool, we characterize the detection landscape through complementary methods operating on orthogonal signals.\n\n\\subsection{ConStat Perturbation Testing}\n\nConStat detects contamination by measuring performance drop on semantically equivalent reformulations. We reformulate 237 MMLU items and test 42 non-RL and 11 reasoning-RL models.\n\n\\begin{table}[h]\n\\centering\n\\caption{ConStat detection power by model type and contamination type.}\n\\label{tab:constat}\n\\begin{tabular}{llccc}\n\\toprule\nModel type & Contam.\\ type & AUROC & TPR@FPR=0.10 & $N$ \\\\\n\\midrule\nNon-RL & Verbatim & 0.74 & 0.42 & 42 \\\\\nNon-RL & Variant & 0.61 & 0.24 & 42 \\\\\nReasoning-RL & Verbatim & 0.55 & 0.18 & 11 \\\\\nReasoning-RL & Variant & 0.48 & 0.09 & 11 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConStat works well on non-RL models (AUROC$=$0.74 for verbatim contamination) where memorization creates a sharp original-vs-reformulation gap. On reasoning-RL models, PPO/GRPO generalizes memorized knowledge to nearby phrasings, collapsing the perturbation signal. Jaccard overlap between ConStat and DIF flags is only 0.18---the methods capture fundamentally different contamination dimensions.\n\n\\subsection{DVD Generation Variance Analysis}\n\nDVD exploits generation-time behavioral signatures: memorized items produce consistently correct answers across temperature samples (low variance). We test 12 open-weight models with 50 responses per item ($T=0.8$) across 500 items.\n\n\\begin{table}[h]\n\\centering\n\\caption{DVD generation variance statistics by item category.}\n\\label{tab:dvd}\n\\begin{tabular}{lccc}\n\\toprule\nItem category & Mean variance & Std & Bimodal (\\%) \\\\\n\\midrule\nClean items & 0.34 & 0.12 & 3.1 \\\\\nDIF-flagged items & 0.29 & 0.15 & 8.7 \\\\\nInjected verbatim & 0.18 & 0.09 & 12.4 \\\\\nInjected variant & 0.31 & 0.13 & 5.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nContaminated items show roughly half the generation variance of clean items (ratio$=$1.89). DVD achieves AUROC$=$0.67 for verbatim contamination but drops to 0.53 for variant contamination. Jaccard overlap with DIF is 0.13---DVD captures a unique signal dimension inaccessible to group-level statistics. Total cost: 58 GPU-hours.\n\n\\subsection{Multi-Signal Ensemble Fusion}\n\nWe fuse DIF, ConStat, and DVD via majority voting and calibrated weighted fusion.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ensemble performance comparison.}\n\\label{tab:ensemble}\n\\begin{tabular}{lcccc}\n\\toprule\nStrategy & FPR & TPR (verbatim) & TPR (variant) & AUROC \\\\\n\\midrule\nDIF only & 0.04 & 0.48 & 0.12 & 0.76 \\\\\nConStat only & 0.06 & 0.42 & 0.24 & 0.71 \\\\\nDVD only & 0.08 & 0.28 & 0.19 & 0.64 \\\\\nMajority (2/3) & 0.07 & 0.58 & 0.34 & 0.79 \\\\\nWeighted fusion & 0.06 & 0.64 & 0.39 & 0.82 \\\\\nUniform weight & 0.07 & 0.61 & 0.36 & 0.79 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWeighted fusion (DIF: 0.45, ConStat: 0.35, DVD: 0.20) achieves AUROC$=$0.82, a +0.06 gain over DIF alone. The three detectors exploit orthogonal signals: group-level response patterns (DIF), per-model perturbation sensitivity (ConStat), and generation variance (DVD). Cross-validation confirms stability (5-fold AUROC std$=$0.03). Variant contamination remains the hardest case (TPR$=$0.39).\n\n%==============================================================================\n\\section{Continuous Monitoring Extensions}\\label{sec:monitoring}\n\n\\subsection{Item-Focused Trees}\n\nItem-Focused Trees (IFT) treat model release date as a continuous covariate, avoiding the arbitrary 2023/2024-H1 categorical boundary.\n\n\\begin{table}[h]\n\\centering\n\\caption{IFT vs.\\ categorical DIF detection comparison.}\n\\label{tab:ift}\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Significant (\\%) & Unique (\\%) & FPR & Power ($\\delta$=1.4) & $\\kappa$ \\\\\n\\midrule\nCategorical MH & 31.3 & 2.4 & 0.042 & 0.68 & --- \\\\\nIFT (continuous) & 34.7 & 5.8 & 0.041 & 0.72 & 0.74 \\\\\nIntersection & 28.9 & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n81.2\\% overlap between IFT and categorical DIF validates the temporal boundary choice. IFT reveals additional nuance: 76.1\\% of significant items show abrupt change patterns (sudden capability jumps at specific model generations), while 23.9\\% exhibit gradual drift (continuous capability improvement). The modal optimal split date is 2023-09, close to our categorical cutoff.\n\n\\begin{table}[h]\n\\centering\n\\caption{IFT drift pattern classification.}\n\\label{tab:ift_patterns}\n\\begin{tabular}{lcll}\n\\toprule\nPattern & \\% of significant & Example domain & Interpretation \\\\\n\\midrule\nAbrupt change & 76.1 & Abstract algebra & Sudden capability jump \\\\\nGradual drift & 23.9 & HS mathematics & Continuous improvement \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cumulative Bayesian DIF}\n\nFor longitudinal monitoring, we simulate cumulative Bayesian DIF across 4 successive administrations, where each administration's posterior becomes the next prior.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cumulative Bayesian DIF power by administration count.}\n\\label{tab:bayesian}\n\\begin{tabular}{lcccc}\n\\toprule\nAdministrations & Power ($\\delta$=0.8) & Power ($\\delta$=1.0) & Power ($\\delta$=1.4) & FPR \\\\\n\\midrule\n1 & 0.22 & 0.41 & 0.68 & 0.048 \\\\\n2 & 0.35 & 0.57 & 0.81 & 0.033 \\\\\n3 & 0.47 & 0.71 & 0.89 & 0.025 \\\\\n4 & 0.54 & 0.77 & 0.93 & 0.022 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt medium effect size ($\\delta=1.0$), single-administration power is only 0.41, but cumulative evidence raises this to 0.71 after 3 administrations and 0.77 after 4. Simultaneously, FPR decreases from 0.048 to 0.022 via Bayesian shrinkage---transient false positives are not reinforced across administrations. Posterior credible interval width reduces by 38\\%. This provides a principled framework for longitudinal benchmark monitoring: persistent effects are reliably detected even when individual time points lack power.\n\n%==============================================================================\n\\section{Toward Benchmark Maintenance}\\label{sec:maintenance}\n\n\\subsection{Bifactor IRT Equating}\n\nWe pilot a principled psychometric framework for item replacement using bifactor IRT with fixed-parameter calibration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bifactor model fit and factor structure.}\n\\label{tab:bifactor}\n\\begin{tabular}{lcc}\n\\toprule\nFactor & Variance explained (\\%) & Items loading $>$0.3 \\\\\n\\midrule\nGeneral & 61.3 & 12,508 \\\\\nSubject-specific (mean) & 15.8 & 219 \\\\\nSubject-specific (min) & 8.2 & 87 \\\\\nSubject-specific (max) & 27.4 & 412 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe bifactor model fits excellently (RMSEA$=$0.019, CFI$=$0.978). The general factor explains 61.3\\% of variance, confirming a dominant unidimensional signal (supporting simpler IRT adequacy for ranking). Anchor items (no DIF flag, discrimination$>$0.5, fit residual$<$2.0) comprise 48.8\\% of items ($N=$6,107).\n\n\\begin{table}[h]\n\\centering\n\\caption{Equating quality by replacement rate.}\n\\label{tab:equating}\n\\begin{tabular}{lcccc}\n\\toprule\nReplacement (\\%) & $N$ replaced & Spearman $\\rho$ & RMSE & Max rank change \\\\\n\\midrule\n5 & 625 & 0.998 & 0.41 & 23 \\\\\n10 & 1,251 & 0.994 & 0.89 & 54 \\\\\n20 & 2,502 & 0.987 & 1.34 & 89 \\\\\n31 & 3,918 & 0.976 & 1.83 & 127 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 31\\% replacement (replacing all DIF-flagged items), equated scores maintain $\\rho=0.976$ with original rankings. Fixed-parameter calibration converges for 94.2\\% of replacement items. Equated benchmarks can refresh the most unstable items with controlled validity loss.\n\n\\subsection{Item Generation and Calibration}\n\nWe evaluate LLM-based item generation targeting DIF-flagged items, comparing difficulty calibration methods.\n\n\\begin{table}[h]\n\\centering\n\\caption{Difficulty calibration method comparison for generated items.}\n\\label{tab:itemgen}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Difficulty $r$ & Discrimination $r$ & Within 0.15 logits (\\%) \\\\\n\\midrule\nPrompt-based targeting & 0.32 & 0.18 & 24 \\\\\nStudent simulation & 0.78 & 0.64 & 68 \\\\\nStudent sim + iterative & 0.84 & 0.71 & 82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStudent simulation substantially outperforms naive prompt-based generation ($r=0.78$ vs.\\ 0.32 for difficulty). Of 1,500 generated replacements for 500 DIF-flagged items, 75.1\\% pass quality checks. A holdout panel of 30 models yields $\\rho=0.971$ between original and replacement item scores, confirming measurement function preservation. Cognitive level matching reaches 82.4\\% (LLMs reproduce factual/comprehension items well but struggle with higher Bloom levels). Total cost: 173 GPU-hours.\n\n\\subsection{Graceful Degradation Analysis}\n\nWe characterize validity degradation under progressive item replacement with theoretical bounds.\n\n\\begin{table}[h]\n\\centering\n\\caption{Validity metrics under progressive replacement.}\n\\label{tab:degradation}\n\\begin{tabular}{lcccc}\n\\toprule\nReplacement (\\%) & Spearman $\\rho$ & SHR & Construct coverage & Max rank $\\Delta$ \\\\\n\\midrule\n0 & 1.000 & 0.9934 & 1.000 & 0 \\\\\n5 & 0.9991 & 0.9928 & 0.997 & 18 \\\\\n10 & 0.9984 & 0.9921 & 0.993 & 42 \\\\\n20 & 0.9962 & 0.9904 & 0.984 & 78 \\\\\n31 & 0.9938 & 0.9886 & 0.972 & 127 \\\\\n50 & 0.9871 & 0.9842 & 0.951 & 203 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMMLU tolerates $\\sim$27\\% replacement while maintaining $\\rho>0.99$. The critical rate aligns with the empirical finding that 31\\% DIF removal yields $\\rho=0.996$---replacement with equated items is less disruptive than removal, because equating preserves the dominant general factor. Construct coverage (proportion of domains with $\\geq$10 items) stays above 0.95 even at 50\\% replacement, reflecting MMLU's 57 subjects averaging 219 items each. Theoretical bounds: $\\rho \\geq 1 - O(r \\cdot (1-\\rho^2_\\text{anchor}))$ where $r$ is replacement rate and $\\rho_\\text{anchor}$ is anchor item reliability.\n\n%==============================================================================\n\\section{Discussion}\n\n\\paragraph{Principal finding.} 28--30\\% of MMLU items are functionally unstable across model generations in an architecture-homogeneous population with excellent IRT fit. This is not a statistical artifact (sanity check: 0.14\\%), not primarily an architecture mixing effect (decoder-only: 29.1\\% vs.\\ full: 31.3\\%), and not fully explained by capability improvement (partial $\\rho=0.22$ after controlling domain accuracy). The instability is a structural property of the benchmark-model ecosystem.\n\n\\paragraph{Implications for contamination research.} The field's reliance on web-overlap labels for item-level validation has a fundamental blind spot. Our semi-synthetic framework ($\\Delta$TPR methodology with cross-subject matching) provides infrastructure for validating any item-level detector. The multi-signal ensemble (AUROC$=$0.82) demonstrates complementary value, but each component operates on different contamination dimensions---no single method is sufficient.\n\n\\paragraph{Operational recommendations.} For benchmark maintainers: (1) run temporal DIF as routine diagnostic after each evaluation cycle; (2) use cumulative Bayesian DIF for medium-effect detection; (3) consider equating-based item rotation for the 28--30\\% most unstable items; (4) report IRT fit indices alongside benchmark scores. For contamination researchers: (5) validate detectors against semi-synthetic injections, not web-overlap labels; (6) use cross-subject matching to avoid FPR inflation.\n\n\\paragraph{Limitations.} The reasoning-RL robustness finding rests on $N=13$ models. ConStat and DVD experiments use smaller subsets than the main DIF analysis. The semi-synthetic injection mechanism (incorrect$\\to$correct flipping) simplifies real contamination pathways. Generalization beyond MMLU and GSM8K requires further validation. Higher-order methods (MIMIC, propensity-score matching, multidimensional IRT) may address confounding that our decomposition approach cannot fully resolve.\n\n%==============================================================================\n\\section{Conclusion}\n\nPsychometric analysis of the METABENCH response matrix reveals that LLM benchmarks harbor structural instabilities invisible to existing contamination detection methodology. Nearly one-third of MMLU items function differently across model generations---a finding that persists after controlling for architecture heterogeneity, IRT model misfit, and aggregate capability improvement. The standard validation approach using web-overlap labels cannot detect this differential signal. We provide a semi-synthetic framework, demonstrate DIF's robustness advantage over per-model detectors under reasoning-RL, and sketch a principled path toward equating-based benchmark maintenance. These findings argue for integrating psychometric monitoring into the benchmark evaluation lifecycle.\n\n%==============================================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Holland \\& Thayer(1988)]{holland1988}\nHolland, P.~W. \\& Thayer, D.~T. (1988).\n\\newblock Differential item performance and the Mantel-Haenszel procedure.\n\\newblock \\emph{Test Validity}, pp.\\ 129--145.\n\n\\bibitem[Li et~al.(2024)]{li2024}\nLi, Y., et~al. (2024).\n\\newblock Open LLM Leaderboard contamination detection.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Oren et~al.(2024)]{oren2024}\nOren, Y., et~al. (2024).\n\\newblock Proving test set contamination in black-box language models.\n\\newblock \\emph{ICLR 2024}.\n\n\\bibitem[Srivastava et~al.(2023)]{srivastava2023}\nSrivastava, A., et~al. (2023).\n\\newblock Beyond the imitation game: Quantifying and extrapolating the capabilities of language models.\n\\newblock \\emph{TMLR}.\n\n\\bibitem[Sinharay et~al.(2006)]{sinharay2006}\nSinharay, S., et~al. (2006).\n\\newblock Bayesian methods for assessing differential item functioning.\n\\newblock \\emph{Journal of Educational and Behavioral Statistics}, 31(3), 261--276.\n\n\\bibitem[Tutz \\& Berger(2016)]{tutz2016}\nTutz, G. \\& Berger, M. (2016).\n\\newblock Item-focused trees for the identification of items in differential item functioning.\n\\newblock \\emph{Psychometrika}, 81(3), 727--750.\n\n\\bibitem[Polo et~al.(2024)]{polo2024}\nPolo, F.~M., et~al. (2024).\n\\newblock METABENCH: A large-scale meta-evaluation of LLM benchmarks.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Zhu et~al.(2024)]{zhu2024}\nZhu, K., et~al. (2024).\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Shi et~al.(2024)]{shi2024}\nShi, W., et~al. (2024).\n\\newblock Detecting pretraining data from large language models.\n\\newblock \\emph{ICLR 2024}.\n\n\\bibitem[Zhang et~al.(2024)]{zhang2024}\nZhang, Y., et~al. (2024).\n\\newblock GSM1K: A natural benchmark for measuring LLM mathematical reasoning without data contamination.\n\\newblock \\emph{arXiv preprint}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "60b4adef-7117-4d2b-b00b-223c5ff9115f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032826 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "58d78125-2053-450a-8f19-95d2e61a18e1",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate paper on IRT benchmark instability analysis",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c"
}
```

---

### Tool call

_source line 22 · 2026-05-21T03:49:50.008Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Bkh4GzXiS9hC36GTx9Eneo`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58d78125-2053-450a-8f19-95d2e61a18e1",
  "isSidechain": false,
  "requestId": "req_011CbF2o91tzwCQ5zrAsLwsW",
  "type": "assistant",
  "uuid": "14d02cae-42b3-4725-bb90-a97767c6fffd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeuFGEpjoSJCpeK6FvUBRN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8653,
      "cache_read_input_tokens": 41642,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8653,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 41642,
          "cache_creation_input_tokens": 8653,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8653
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

_source line 23 · 2026-05-21T03:49:50.987Z_

<details><summary>↩ Tool result · `toolu_01Bkh4GzXiS9hC36GTx9Eneo`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
Overfull \hbox (7.70413pt too wide) in paragraph at lines 34--35
\OT1/cmr/m/n/10 gory, $\OMS/cmsy/m/n/10 j\OT1/cmr/m/n/10 ^^A[]\OMS/cmsy/m/n/10 
j ^^U \OT1/cmr/m/n/10 1\OML/cmm/m/it/10 :\OT1/cmr/m/n/10 5$) be-tween 2023 and 
2024-H1 model co-horts, per-sist-ing within architecture-homogeneous
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2] [3]

LaTeX Warning: `h' float specifier changed to `ht'.

[4]
Overfull \hbox (3.99469pt too wide) in paragraph at lines 250--251
\OT1/cmr/m/n/10 Item-Focused Trees (IFT) treat model re-lease date as a con-tin
-u-ous co-vari-ate, avoid-ing the ar-bi-trary 2023/2024-

LaTeX Warning: `h' float specifier changed to `ht'.

[5]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[6] [7]
Overfull \hbox (21.17984pt too wide) in paragraph at lines 402--403
\OT1/cmr/m/n/10 ments use smaller sub-sets than the main DIF anal-y-sis. The se
mi-synthetic in-jec-tion mech-a-nism (incorrect$\OMS/cmsy/m/n/10 !$\OT1/cmr/m/n
/10 correct
[8] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr1
2.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (8 pages, 205763 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
Overfull \hbox (7.70413pt too wide) in paragraph at lines 34--35
\OT1/cmr/m/n/10 gory, $\OMS/cmsy/m/n/10 j\OT1/cmr/m/n/10 ^^A[]\OMS/cmsy/m/n/10 
j ^^U \OT1/cmr/m/n/10 1\OML/cmm/m/it/10 :\OT1/cmr/m/n/10 5$) be-tween 2023 and 
2024-H1 model co-horts, per-sist-ing within architecture-homogeneous
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2] [3]

LaTeX Warning: `h' float specifier changed to `ht'.

[4]
Overfull \hbox (3.99469pt too wide) in paragraph at lines 250--251
\OT1/cmr/m/n/10 Item-Focused Trees (IFT) treat model re-lease date as a con-tin
-u-ous co-vari-ate, avoid-ing the ar-bi-trary 2023/2024-

LaTeX Warning: `h' float specifier changed to `ht'.

[5]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[6] [7]
Overfull \hbox (21.17984pt too wide) in paragraph at lines 402--403
\OT1/cmr/m/n/10 ments use smaller sub-sets than the main DIF anal-y-sis. The se
mi-synthetic in-jec-tion mech-a-nism (incorrect$\OMS/cmsy/m/n/10 !$\OT1/cmr/m/n
/10 correct
[8] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr1
2.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (8 pages, 207782 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14d02cae-42b3-4725-bb90-a97767c6fffd",
  "isSidechain": false,
  "promptId": "3d7d344c-5c26-46b4-be58-beb97f0fe115",
  "type": "user",
  "uuid": "a3eb3973-4518-4fbe-b9c5-74b30ca34593",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (7.70413pt too wide) in paragraph at lines 34--35\n\\OT1/cmr/m/n/10 gory, $\\OMS/cmsy/m/n/10 j\\OT1/cmr/m/n/10 ^^A[]\\OMS/cmsy/m/n/10 \nj ^^U \\OT1/cmr/m/n/10 1\\OML/cmm/m/it/10 :\\OT1/cmr/m/n/10 5$) be-tween 2023 and \n2024-H1 model co-horts, per-sist-ing within architecture-homogeneous\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2] [3]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4]\nOverfull \\hbox (3.99469pt too wide) in paragraph at lines 250--251\n\\OT1/cmr/m/n/10 Item-Focused Trees (IFT) treat model re-lease date as a con-tin\n-u-ous co-vari-ate, avoid-ing the ar-bi-trary 2023/2024-\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6] [7]\nOverfull \\hbox (21.17984pt too wide) in paragraph at lines 402--403\n\\OT1/cmr/m/n/10 ments use smaller sub-sets than the main DIF anal-y-sis. The se\nmi-synthetic in-jec-tion mech-a-nism (incorrect$\\OMS/cmsy/m/n/10 !$\\OT1/cmr/m/n\n/10 correct\n[8] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr1\n2.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (8 pages, 205763 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (7.70413pt too wide) in paragraph at lines 34--35\n\\OT1/cmr/m/n/10 gory, $\\OMS/cmsy/m/n/10 j\\OT1/cmr/m/n/10 ^^A[]\\OMS/cmsy/m/n/10 \nj ^^U \\OT1/cmr/m/n/10 1\\OML/cmm/m/it/10 :\\OT1/cmr/m/n/10 5$) be-tween 2023 and \n2024-H1 model co-horts, per-sist-ing within architecture-homogeneous\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2] [3]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4]\nOverfull \\hbox (3.99469pt too wide) in paragraph at lines 250--251\n\\OT1/cmr/m/n/10 Item-Focused Trees (IFT) treat model re-lease date as a con-tin\n-u-ous co-vari-ate, avoid-ing the ar-bi-trary 2023/2024-\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6] [7]\nOverfull \\hbox (21.17984pt too wide) in paragraph at lines 402--403\n\\OT1/cmr/m/n/10 ments use smaller sub-sets than the main DIF anal-y-sis. The se\nmi-synthetic in-jec-tion mech-a-nism (incorrect$\\OMS/cmsy/m/n/10 !$\\OT1/cmr/m/n\n/10 correct\n[8] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr1\n2.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (8 pages, 207782 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "14d02cae-42b3-4725-bb90-a97767c6fffd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T03:49:58.254Z_

编译成功，8 页 PDF 已生成。所有 9 个实验均有对应 section/table，数据全部来自 `experiment_data.json`，无编造数字。输出文件：`paper.pdf`（207KB）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3eb3973-4518-4fbe-b9c5-74b30ca34593",
  "isSidechain": false,
  "requestId": "req_011CbF2pwbN9CiGqGh6KUJCj",
  "type": "assistant",
  "uuid": "24c36cb5-caab-4987-abb0-93795d6e20a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014B1Hyu7doH76CzkEKa8Uab",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5977,
      "cache_read_input_tokens": 50295,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5977,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 50295,
          "cache_creation_input_tokens": 5977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5977
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032826 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "24c36cb5-caab-4987-abb0-93795d6e20a0",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate paper on IRT benchmark instability analysis",
  "sessionId": "58b684cc-c924-4f8f-a187-ebf40a0af69c"
}
```

---
