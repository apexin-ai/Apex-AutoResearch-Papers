# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/e980fe00-e836-45ed-a34e-5c568fc8e9eb.jsonl`
- **Structured JSON:** [`d8f53adb74cdf5c1eeeb.json`](../../sessions/d8/d8f53adb74cdf5c1eeeb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T23:12:09.547Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T23:12:09.547Z",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Cross-benchmark gradient是primary finding且远比第一版dream更陡峭： MMLU(56%) > ARC(42%) > HellaSwag(34%) > GSM8K(25%)，spread 31pp。 reasoning tasks的CoT stochasticity将massive方差从item_id转移到seed×item和temp×item（各15-25%）， 这解释了为什么prior single-benchmark studies得出看似矛盾的结论。\n核心升级：\"optimal evaluation protocol reverses across task types\"—— MMLU是item-limited（需420 items for G≥0.90），GSM8K是seed-limited（需10+ seeds for G≥0.90）。 \"Universal reproducibility recipe is illusory\"被数据完全支持，且比预期更强。\nModel-as-facet分析cleanly提取model×item（~10%），item_id降至49%但仍为最大单一组分。 Bootstrap CIs tight（4-6pp宽度）且benchmark间不重叠——gradient具有full statistical significance。 Separability是clean confirmatory null（hardware×methodology <0.3%）。\n三条claim全部成立无需弱化。AAAI \"evaluation methodology\" track投稿正常推进。 Lead figure: 4-benchmark stacked bars展示variance structure的系统性迁移， signature visual直接支撑\"no universal recipe\"叙事。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T23:12:09.550Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T23:12:09.550Z",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb"
}
```

---

## Round 1

34 recorded events

### User

_source line 3 · 2026-05-20T23:12:09.576Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Cross-benchmark gradient是primary finding且远比第一版dream更陡峭： MMLU(56%) > ARC(42%) > HellaSwag(34%) > GSM8K(25%)，spread 31pp。 reasoning tasks的CoT stochasticity将massive方差从item_id转移到seed×item和temp×item（各15-25%）， 这解释了为什么prior single-benchmark studies得出看似矛盾的结论。
核心升级："optimal evaluation protocol reverses across task types"—— MMLU是item-limited（需420 items for G≥0.90），GSM8K是seed-limited（需10+ seeds for G≥0.90）。 "Universal reproducibility recipe is illusory"被数据完全支持，且比预期更强。
Model-as-facet分析cleanly提取model×item（~10%），item_id降至49%但仍为最大单一组分。 Bootstrap CIs tight（4-6pp宽度）且benchmark间不重叠——gradient具有full statistical significance。 Separability是clean confirmatory null（hardware×methodology <0.3%）。
三条claim全部成立无需弱化。AAAI "evaluation methodology" track投稿正常推进。 Lead figure: 4-benchmark stacked bars展示variance structure的系统性迁移， signature visual直接支撑"no universal recipe"叙事。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a34885db-cab9-4548-bc00-3fd0d7d7db63",
  "type": "user",
  "uuid": "7e5c1e8e-e718-4dc6-b499-5f97d0a2afb5",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T23:12:09.575Z_

```json
{
  "parentUuid": "7e5c1e8e-e718-4dc6-b499-5f97d0a2afb5",
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
  "uuid": "e5642c81-648f-4fae-93de-e3bf4b2de456",
  "timestamp": "2026-05-20T23:12:09.575Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T23:12:09.575Z_

```json
{
  "parentUuid": "e5642c81-648f-4fae-93de-e3bf4b2de456",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e5221117-9338-4f80-aca8-3a6ba242bd5b",
  "timestamp": "2026-05-20T23:12:09.575Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
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
  "aiTitle": "Generate NLP variance theory paper with gradient analysis",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb"
}
```

---

### Assistant

_source line 7 · 2026-05-20T23:12:12.112Z_

Let me start by reading the input files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5221117-9338-4f80-aca8-3a6ba242bd5b",
  "isSidechain": false,
  "requestId": "req_011CbEfekxRrbC8eksjag75K",
  "type": "assistant",
  "uuid": "7b1ad98d-d325-4e21-8da1-43b12965ff35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012nagMgvtbwpiyfRgr3hkZL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11689,
      "cache_read_input_tokens": 11841,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11689
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

_source line 8 · 2026-05-20T23:12:12.740Z_

<details open><summary>🔧 Tool call — Read · `toolu_019UgXWNMh3hvxLNKrtF7q5i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b1ad98d-d325-4e21-8da1-43b12965ff35",
  "isSidechain": false,
  "requestId": "req_011CbEfekxRrbC8eksjag75K",
  "type": "assistant",
  "uuid": "f3200d6c-e5ea-4033-bf2f-a3d0dd6ffcf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012nagMgvtbwpiyfRgr3hkZL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11689,
      "cache_read_input_tokens": 11841,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11689
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

_source line 9 · 2026-05-20T23:12:13.008Z_

<details><summary>↩ Tool result · `toolu_019UgXWNMh3hvxLNKrtF7q5i`</summary>

```text
1	[
2	  {
3	    "name": "Full-scale MMLU precision study with confound fix",
4	    "description": "4 models (Qwen3-8B, Llama-3.1-8B, Gemma-2-9B-IT, Mistral-7B-v0.3) × 3 precisions (FP32/BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items (stratified), 全部使用vLLM V0 enforce_eager消除engine confound。 总条件数 4×3×6×6×3×4 = 5,184 per item，总记录 5,184×200 = 1,036,800。\n",
5	    "results": {
6	      "total_records": 1036800,
7	      "conditions_per_model": 1296,
8	      "overall_accuracy": 0.667,
9	      "accuracy_fp32": 0.664,
10	      "accuracy_bf16": 0.669,
11	      "accuracy_fp16": 0.667,
12	      "accuracy_spread_across_precisions_pp": 0.5,
13	      "item_id": 0.56,
14	      "residual": 0.207,
15	      "prompt_template_x_item_id": 0.062,
16	      "temperature_x_item_id": 0.059,
17	      "seed_x_item_id": 0.03,
18	      "precision_x_item_id": 0.018,
19	      "ordering_x_item_id": 0.015,
20	      "prompt_template": 0.018,
21	      "temperature": 0.014,
22	      "ordering": 0.008,
23	      "precision": 0.003,
24	      "seed": 0.002,
25	      "direct_infra_x_method_total": 0.004,
26	      "models_with_item_id_rank1": 4,
27	      "item_id_range_across_models": [
28	        0.516,
29	        0.602
30	      ],
31	      "qwen3_8b_item_id": 0.578,
32	      "llama31_8b_item_id": 0.554,
33	      "gemma2_9b_item_id": 0.602,
34	      "mistral_7b_item_id": 0.516,
35	      "precision_main_before_fix_mvp": 0.0087,
36	      "precision_main_after_fix": 0.003,
37	      "precision_x_item_before_fix_mvp": 0.0724,
38	      "precision_x_item_after_fix": 0.018,
39	      "fp32_bf16_gap_before_fix_pp": 8.5,
40	      "fp32_bf16_gap_after_fix_pp": 0.5,
41	      "g_coefficient_correct": 0.36,
42	      "g_text_exact_match": 0.94,
43	      "text_match_prompt_x_item": 0.362,
44	      "text_match_item_id": 0.218,
45	      "text_match_precision_x_temperature": 0.014
46	    },
47	    "tables": [
48	      {
49	        "name": "Table 1: Variance Components — MMLU 200 items, 4 models pooled (binary_correct)",
50	        "columns": [
51	          "Component",
52	          "% Variance",
53	          "SE",
54	          "95% CI Lower",
55	          "95% CI Upper",
56	          "MVP (50 items)"
57	        ],
58	        "rows": [
59	          [
60	            "item_id",
61	            56.0,
62	            1.8,
63	            52.5,
64	            59.5,
65	            "58.4"
66	          ],
67	          [
68	            "residual",
69	            20.7,
70	            0.8,
71	            19.1,
72	            22.3,
73	            "17.6"
74	          ],
75	          [
76	            "prompt×item",
77	            6.2,
78	            0.6,
79	            5.0,
80	            7.4,
81	            "5.7"
82	          ],
83	          [
84	            "temp×item",
85	            5.9,
86	            0.5,
87	            4.9,
88	            6.9,
89	            "6.9"
90	          ],
91	          [
92	            "seed×item",
93	            3.0,
94	            0.3,
95	            2.4,
96	            3.6,
97	            "2.7"
98	          ],
99	          [
100	            "precision×item",
101	            1.8,
102	            0.2,
103	            1.4,
104	            2.2,
105	            "7.2*"
106	          ],
107	          [
108	            "ordering×item",
109	            1.5,
110	            0.2,
111	            1.1,
112	            1.9,
113	            "—"
114	          ],
115	          [
116	            "prompt",
117	            1.8,
118	            0.3,
119	            1.2,
120	            2.4,
121	            "—"
122	          ],
123	          [
124	            "temperature",
125	            1.4,
126	            0.2,
127	            1.0,
128	            1.8,
129	            "—"
130	          ],
131	          [
132	            "ordering",
133	            0.8,
134	            0.2,
135	            0.4,
136	            1.2,
137	            "—"
138	          ],
139	          [
140	            "precision",
141	            0.3,
142	            0.1,
143	            0.1,
144	            0.5,
145	            "0.87*"
146	          ],
147	          [
148	            "seed",
149	            0.2,
150	            0.05,
151	            0.1,
152	            0.3,
153	            "—"
154	          ],
155	          [
156	            "infra×method (all)",
157	            0.4,
158	            0.1,
159	            0.2,
160	            0.6,
161	            "<0.02"
162	          ]
163	        ]
164	      },
165	      {
166	        "name": "Table 2: Per-Model item_id Variance Share (MMLU)",
167	        "columns": [
168	          "Model",
169	          "item_id %",
170	          "Next Largest",
171	          "Next %",
172	          "Accuracy"
173	        ],
174	        "rows": [
175	          [
176	            "Gemma-2-9B-IT",
177	            60.2,
178	            "residual",
179	            17.1,
180	            0.691
181	          ],
182	          [
183	            "Qwen3-8B",
184	            57.8,
185	            "residual",
186	            18.3,
187	            0.672
188	          ],
189	          [
190	            "Llama-3.1-8B",
191	            55.4,
192	            "residual",
193	            19.8,
194	            0.658
195	          ],
196	          [
197	            "Mistral-7B-v0.3",
198	            51.6,
199	            "residual",
200	            22.4,
201	            0.641
202	          ]
203	        ]
204	      }
205	    ],
206	    "figures": [],
207	    "analysis": "核心发现：engine confound fix后item dominance完全稳健（56.0% vs MVP 58.4%，差异在SE范围内）， precision主效应从0.87%坍缩至0.3%。这同时验证了Claim 1和提供了方法论贡献 （vLLM engine配置对variance attribution的系统性影响）。 4个模型一致性消除了\"单模型特例\"concern。text-match指标复现MVP的dual-metric pattern。 Ordering facet新增后占比很小（~2.3% total），不是major concern。 该实验为所有后续benchmark比较建立了MMLU baseline。\n\n\nMVP的precision主效应(0.87%)和precision×item(7.24%)源于float32使用不同vLLM engine路径（V1 CUDA graph vs V0 eager）， 导致FP32准确率系统性偏低5.7pp。统一V0 enforce_eager后三种精度走同一compute path， FP32/BF16/FP16准确率差收敛至0.5pp内（纯numerical noise水平，符合IEEE 754 rounding差异预期）。\nPrecision释放的~6%方差重新分配：precision×item从7.2%→1.8%（剩余为genuine numerical sensitivity on boundary items）， precision主效应从0.87%→0.3%，释放的份额主要回流到residual（+3.1pp）和小量到item_id（+0.2pp）， 因为之前被precision confound扭曲的item-level patterns现在归入正确组分。\n4个模型均以item_id为rank-1（51.6%-60.2%），因为MMLU的item difficulty分布（从trivial factual recall到 expert-level reasoning）在所有7-9B instruction-tuned模型上产生类似的accuracy ceiling/floor效应。 Gemma-2最高(60.2%)因其instruction-tuning使easy items更稳定（floor更高）， Mistral最低(51.6%)因其在部分domain上accuracy分布更平坦（difficulty gradient被压缩）。\n200 items分层采样比MVP的50 items提供更稳定的方差估计，SE减半，CI收窄~50%。\nText-exact-match指标复现MVP pattern：prompt×item主导(36.2%)而非item_id(21.8%)， 因为不同prompt template导致model生成不同格式的答案字符串（\"A\"/\"(A)\"/\"The answer is A\"）， 这种格式变异是item-specific的（有些items的答案format更鲁棒）。 precision×temperature在text-match下仍检出1.4%（CI不含零），确认floating-point non-associativity效应。\n"
208	  },
209	  {
210	    "name": "Item resampling stability test",
211	    "description": "3 independent stratified 200-item MMLU samples (stratification seeds 0, 7, 99) × 1 model (Llama-3.1-8B) × 3 precisions × 3 prompts × 3 seeds × 2 orderings = 54 conditions per sample。 每sample 54×200 = 10,800记录，总计 32,400记录。 测试item_id dominance是否对specific item selection稳定。\n",
212	    "results": {
213	      "total_records": 32400,
214	      "conditions_per_sample": 54,
215	      "sample_a_item_id": 0.528,
216	      "sample_b_item_id": 0.572,
217	      "sample_c_item_id": 0.561,
218	      "item_id_mean": 0.554,
219	      "item_id_sd": 0.023,
220	      "item_id_cv": 0.041,
221	      "item_id_rank1_all_samples": true,
222	      "sample_a_residual": 0.224,
223	      "sample_b_residual": 0.198,
224	      "sample_c_residual": 0.21,
225	      "sample_a_accuracy": 0.651,
226	      "sample_b_accuracy": 0.664,
227	      "sample_c_accuracy": 0.657,
228	      "prompt_x_item_range": [
229	        0.054,
230	        0.072
231	      ],
232	      "temp_x_item_range": [
233	        0.048,
234	        0.067
235	      ],
236	      "max_component_cv": 0.14
237	    },
238	    "tables": [
239	      {
240	        "name": "Table 3: Item Resampling Stability (Llama-3.1-8B, MMLU)",
241	        "columns": [
242	          "Component",
243	          "Sample A",
244	          "Sample B",
245	          "Sample C",
246	          "Mean",
247	          "CV"
248	        ],
249	        "rows": [
250	          [
251	            "item_id",
252	            52.8,
253	            57.2,
254	            55.6,
255	            55.2,
256	            "4.1%"
257	          ],
258	          [
259	            "residual",
260	            22.4,
261	            19.8,
262	            21.0,
263	            21.1,
264	            "6.2%"
265	          ],
266	          [
267	            "prompt×item",
268	            5.4,
269	            7.2,
270	            6.1,
271	            6.2,
272	            "14.5%"
273	          ],
274	          [
275	            "temp×item",
276	            4.8,
277	            6.7,
278	            5.6,
279	            5.7,
280	            "16.7%"
281	          ],
282	          [
283	            "seed×item",
284	            2.8,
285	            3.2,
286	            3.0,
287	            3.0,
288	            "6.7%"
289	          ],
290	          [
291	            "precision×item",
292	            1.6,
293	            2.0,
294	            1.8,
295	            1.8,
296	            "11.1%"
297	          ],
298	          [
299	            "Accuracy",
300	            0.651,
301	            0.664,
302	            0.657,
303	            0.657,
304	            "—"
305	          ]
306	        ]
307	      }
308	    ],
309	    "figures": [],
310	    "analysis": "CV=4.1%的稳定性为headline claim提供了strong defense against \"specific item selection artifact\"。 即使用不同的200-item子集，variance structure qualitatively不变。 这为exp-002的cross-benchmark比较提供了基线——任何跨benchmark的item_id差异 只要超过~5pp就不能归因于item sampling variability。\n\n\nItem_id across 3 samples: 52.8%, 57.2%, 55.6%（mean=55.4%, CV=4.1%）。 所有sample均在50-60%范围内，item_id均为rank-1。CV远低于15%阈值。\nSample间变异源于MMLU 14K item pool中不同difficulty strata的adoption—— 不同随机种子抽到的items在difficulty distribution上略有差异（例如sample B可能 包含更多extreme-difficulty items，拉大item variance）。但由于分层采样保证了 subject-level比例一致，这种变异被有效控制。\n关键：即使是\"worst\"的sample A（52.8%），item_id仍远超第二名residual（22.4%）， headline claim \"item selection is the largest variance source\"对任意200-item MMLU子集稳健。\n非item组分的CV也可控（max 14%），说明variance structure本身是item-robust的， 不会因特定item选择而qualitatively改变。\n"
311	  },
312	  {
313	    "name": "Multi-benchmark variance gradient",
314	    "description": "4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 items，在GSM8K、ARC-Challenge、HellaSwag上分别运行。 每benchmark 4×2×6×6×2×4×200 = 460,800记录，3 benchmarks总计 1,382,400记录。 核心目标：建立cross-benchmark variance gradient，验证item dominance的benchmark-dependence。\n",
315	    "results": {
316	      "total_records_per_benchmark": 460800,
317	      "total_records_all": 1382400,
318	      "gsm8k_overall_accuracy": 0.574,
319	      "gsm8k_item_id": 0.25,
320	      "gsm8k_temperature_x_item": 0.182,
321	      "gsm8k_seed_x_item": 0.158,
322	      "gsm8k_prompt_x_item": 0.103,
323	      "gsm8k_residual": 0.159,
324	      "gsm8k_ordering_x_item": 0.032,
325	      "gsm8k_precision_x_item": 0.011,
326	      "gsm8k_temperature": 0.036,
327	      "gsm8k_prompt": 0.028,
328	      "gsm8k_seed": 0.024,
329	      "gsm8k_ordering": 0.012,
330	      "gsm8k_precision": 0.002,
331	      "gsm8k_infra_x_method": 0.003,
332	      "gsm8k_g_full_design": 0.55,
333	      "arc_overall_accuracy": 0.592,
334	      "arc_item_id": 0.42,
335	      "arc_temperature_x_item": 0.086,
336	      "arc_seed_x_item": 0.062,
337	      "arc_prompt_x_item": 0.092,
338	      "arc_residual": 0.174,
339	      "arc_ordering_x_item": 0.034,
340	      "arc_precision_x_item": 0.015,
341	      "arc_temperature": 0.02,
342	      "arc_prompt": 0.022,
343	      "arc_seed": 0.014,
344	      "arc_ordering": 0.012,
345	      "arc_precision": 0.002,
346	      "arc_infra_x_method": 0.003,
347	      "arc_g_full_design": 0.42,
348	      "hellaswag_overall_accuracy": 0.708,
349	      "hellaswag_item_id": 0.34,
350	      "hellaswag_temperature_x_item": 0.132,
351	      "hellaswag_seed_x_item": 0.108,
352	      "hellaswag_prompt_x_item": 0.094,
353	      "hellaswag_residual": 0.158,
354	      "hellaswag_ordering_x_item": 0.036,
355	      "hellaswag_precision_x_item": 0.013,
356	      "hellaswag_temperature": 0.028,
357	      "hellaswag_prompt": 0.024,
358	      "hellaswag_seed": 0.02,
359	      "hellaswag_ordering": 0.014,
360	      "hellaswag_precision": 0.002,
361	      "hellaswag_infra_x_method": 0.003,
362	      "hellaswag_g_full_design": 0.47,
363	      "gradient_monotonic": true,
364	      "gradient_order": "MMLU > ARC > HellaSwag > GSM8K",
365	      "gradient_spread_pp": 31.0,
366	      "all_benchmarks_item_id_rank1": true,
367	      "item_id_range_across_benchmarks": [
368	        0.25,
369	        0.56
370	      ],
371	      "models_showing_consistent_gradient": 4,
372	      "precision_main_under_0_5pct_all_benchmarks": true
373	    },
374	    "tables": [
375	      {
376	        "name": "Table 4: Cross-Benchmark Variance Gradient (binary_correct, 4 models pooled)",
377	        "columns": [
378	          "Benchmark",
379	          "Task Type",
380	          "item_id %",
381	          "temp×item %",
382	          "seed×item %",
383	          "prompt×item %",
384	          "Residual %",
385	          "G (full)"
386	        ],
387	        "rows": [
388	          [
389	            "MMLU",
390	            "Knowledge",
391	            56.0,
392	            5.9,
393	            3.0,
394	            6.2,
395	            20.7,
396	            0.36
397	          ],
398	          [
399	            "ARC-Chal.",
400	            "Science",
401	            42.0,
402	            8.6,
403	            6.2,
404	            9.2,
405	            17.4,
406	            0.42
407	          ],
408	          [
409	            "HellaSwag",
410	            "Commonsense",
411	            34.0,
412	            13.2,
413	            10.8,
414	            9.4,
415	            15.8,
416	            0.47
417	          ],
418	          [
419	            "GSM8K",
420	            "Math",
421	            25.0,
422	            18.2,
423	            15.8,
424	            10.3,
425	            15.9,
426	            0.55
427	          ]
428	        ]
429	      },
430	      {
431	        "name": "Table 5: GSM8K Per-Model Variance Breakdown",
432	        "columns": [
433	          "Model",
434	          "item_id %",
435	          "temp×item %",
436	          "seed×item %",
437	          "prompt×item %",
438	          "Residual %"
439	        ],
440	        "rows": [
441	          [
442	            "Qwen3-8B",
443	            28.4,
444	            16.8,
445	            14.2,
446	            9.6,
447	            14.8
448	          ],
449	          [
450	            "Llama-3.1-8B",
451	            24.1,
452	            19.4,
453	            16.8,
454	            10.8,
455	            15.2
456	          ],
457	          [
458	            "Gemma-2-9B-IT",
459	            27.6,
460	            17.2,
461	            14.8,
462	            9.8,
463	            14.6
464	          ],
465	          [
466	            "Mistral-7B-v0.3",
467	            21.2,
468	            20.6,
469	            18.4,
470	            11.6,
471	            16.4
472	          ]
473	        ]
474	      },
475	      {
476	        "name": "Table 6: Interaction Term Gradient (benchmark × interaction type)",
477	        "columns": [
478	          "Benchmark",
479	          "temp×item",
480	          "seed×item",
481	          "Σ(interaction×item)",
482	          "Main Effects Σ"
483	        ],
484	        "rows": [
485	          [
486	            "MMLU",
487	            5.9,
488	            3.0,
489	            18.4,
490	            4.5
491	          ],
492	          [
493	            "ARC-Chal.",
494	            8.6,
495	            6.2,
496	            28.9,
497	            7.0
498	          ],
499	          [
500	            "HellaSwag",
501	            13.2,
502	            10.8,
503	            38.3,
504	            8.8
505	          ],
506	          [
507	            "GSM8K",
508	            18.2,
509	            15.8,
510	            48.6,
511	            10.2
512	          ]
513	        ]
514	      }
515	    ],
516	    "figures": [],
517	    "analysis": "这是paper的headline experiment。31pp的gradient spread（MMLU 56% → GSM8K 25%） 是primary novel finding。比第一版dream预测的~10pp gradient（旧预测GSM8K在~49%） 大3×，说明reasoning tasks的variance structure与knowledge tasks qualitatively不同。\n核心发现可总结为一句话： \"On knowledge benchmarks, WHICH items you select determines your result;\n on reasoning benchmarks, HOW you generate answers matters equally.\"\n\n4/4 benchmarks的item_id仍为rank-1，但GSM8K的item_id(25%)仅微弱领先temp×item(18.2%)， 说明在extreme reasoning tasks上，item dominance可能不再成立—— 这为MATH benchmark（exp-008）设置了预期。\nG coefficient的反直觉pattern：knowledge benchmarks的G更低（MMLU 0.36 vs GSM8K 0.55）。 这是因为high item_id意味着item sampling是measurement reliability的bottleneck—— 在MMLU上即使用全部facet levels，200-item的item sampling error仍然dominant。 GSM8K的low item_id意味着item sampling error小，多seed/temp averaging后G更高。\n\n\nCross-benchmark gradient的机制：MMLU(56%) > ARC(42%) > HellaSwag(34%) > GSM8K(25%)。\nMMLU是knowledge-retrieval：item difficulty是intrinsic属性——你要么知道，要么不知道。 不同temperature/seed对答案选择的影响很小，因为在logit space中correct answer的probability 要么远高于threshold（easy items）要么远低于（hard items）。只有narrow difficulty band 内的items对generation parameters敏感。结果：item_id dominates at 56%。\nGSM8K是multi-step math reasoning：同一item在不同seeds/temperatures下产生qualitatively不同的 推理链。具体地：(1) 每个推理步骤是independently sampled，温度直接影响每步的token distribution， 多步累积效应使temperature×item达到18.2%——对比MMLU的5.9%，涨幅3×； (2) random seed决定了initial token choice，不同seed走不同reasoning path， 某些items（multi-step word problems）对seed极度敏感而simple arithmetic几乎不受影响， 故seed×item达到15.8%——对比MMLU的3.0%，涨幅5×； (3) item_id降至25%不是因为items不重要，而是因为\"intrinsic difficulty\"只是total difficulty的一部分—— 在reasoning tasks中，difficulty = intrinsic complexity + generation path stochasticity。\nARC-Challenge混合了factual recall（类似MMLU）和multi-hop reasoning（类似GSM8K）， 所以item_id(42%)落在两者之间。具体来说，ARC的science questions中factual questions （\"What is the boiling point of water?\"）贡献高item_id，而multi-hop questions （\"Which of these would happen if...\"）贡献高interaction terms。\nHellaSwag是commonsense completion：需要生成continuation的判断涉及implicit reasoning 但步骤较少（通常1-2步推理），介于knowledge和full reasoning之间。 Distractor quality的item-level variation是item_id的主要贡献（有些items的wrong answers显而易见，有些极难区分），但generation sensitivity高于MMLU。\n所有benchmark上precision主效应均<0.3%（均为engine confound fix后的clean estimates）， infra×method<0.3%，确认separability across benchmarks。\n4/4 models在每个benchmark上都展示相同的gradient pattern，排除了model-specific artifact。\n"
518	  },
519	  {
520	    "name": "Multi-hardware separability test",
521	    "description": "4 models × 2 GPU types (RTX PRO 6000 + second GPU) × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。 总记录 4×2×2×6×6×3×4×200 = 691,200。 核心目标：量化hardware主效应和hardware×methodology交互，验证single-GPU separability。\n",
522	    "results": {
523	      "total_records": 691200,
524	      "hardware_main_effect": 0.004,
525	      "hardware_x_item": 0.016,
526	      "hardware_x_prompt": 0.0006,
527	      "hardware_x_temperature": 0.0005,
528	      "hardware_x_seed": 0.0004,
529	      "hardware_x_ordering": 0.0002,
530	      "hardware_x_methodology_total": 0.0017,
531	      "precision_x_prompt": 0.0006,
532	      "precision_x_temperature": 0.0005,
533	      "precision_x_seed": 0.0003,
534	      "precision_x_ordering": 0.0002,
535	      "direct_infra_x_method_total": 0.003,
536	      "item_id": 0.554,
537	      "residual": 0.164,
538	      "prompt_x_item": 0.06,
539	      "temperature_x_item": 0.057,
540	      "seed_x_item": 0.029,
541	      "precision_x_item": 0.017,
542	      "ordering_x_item": 0.014,
543	      "infra_x_item_total": 0.033,
544	      "method_x_item_total": 0.16,
545	      "gpu1_gpu2_accuracy_correlation": 0.9992,
546	      "max_accuracy_difference_any_condition": 0.014,
547	      "mean_accuracy_difference": 0.003,
548	      "model_rankings_preserved": true,
549	      "g_full_design": 0.35
550	    },
551	    "tables": [
552	      {
553	        "name": "Table 7: Separability Test — Direct vs Item-Conditional Interactions",
554	        "columns": [
555	          "Interaction Type",
556	          "Components",
557	          "Total %",
558	          "Interpretation"
559	        ],
560	        "rows": [
561	          [
562	            "Direct Infra×Method",
563	            "hw×prompt, hw×temp, hw×seed, hw×ord, prec×prompt, prec×temp, prec×seed, prec×ord",
564	            0.3,
565	            "Negligible — aggregate separability holds"
566	          ],
567	          [
568	            "Infra×Item",
569	            "hw×item, prec×item",
570	            3.3,
571	            "Small — hardware/precision effects are item-conditional"
572	          ],
573	          [
574	            "Method×Item",
575	            "prompt×item, temp×item, seed×item, ord×item",
576	            16.0,
577	            "Substantial — methodology effects are strongly item-conditional"
578	          ],
579	          [
580	            "Item Main",
581	            "item_id",
582	            55.4,
583	            "Dominant — item selection is the primary variance source"
584	          ]
585	        ]
586	      },
587	      {
588	        "name": "Table 8: Hardware Agreement (per-model mean accuracy)",
589	        "columns": [
590	          "Model",
591	          "GPU1 (RTX PRO 6000)",
592	          "GPU2",
593	          "Δ (pp)",
594	          "Rank Preserved"
595	        ],
596	        "rows": [
597	          [
598	            "Qwen3-8B",
599	            0.672,
600	            0.669,
601	            0.3,
602	            "Yes"
603	          ],
604	          [
605	            "Llama-3.1-8B",
606	            0.658,
607	            0.655,
608	            0.3,
609	            "Yes"
610	          ],
611	          [
612	            "Gemma-2-9B-IT",
613	            0.691,
614	            0.687,
615	            0.4,
616	            "Yes"
617	          ],
618	          [
619	            "Mistral-7B-v0.3",
620	            0.641,
621	            0.638,
622	            0.3,
623	            "Yes"
624	          ]
625	        ]
626	      }
627	    ],
628	    "figures": [],
629	    "analysis": "Separability confirmed: direct infra×method total 0.3%，远低于1%阈值。 这是Claim 2的核心evidence。但不是trivial null—— item-conditional interactions提供了mechanistic insight： infra和method不是completely independent，而是通过item difficulty间接耦合。 这解释了为什么prior isolated-factor studies在某些specific items上不generalize 而在aggregate level是valid的。\nNote：当前\"infrastructure\"限于precision facet + 2 GPU types。 更广泛的hardware diversity（datacenter GPU、不同CUDA versions）是future work。\n\n\nHardware主效应0.4%反映两块GPU的微架构差异（不同SM count、memory bandwidth、kernel scheduling）， 但这些差异是systematic fixed offset，不是random——同一model在GPU2上一致性地偏低0.3pp。\nhardware×methodology total仅0.17%，远低于1%阈值。原理：hardware层影响numerical computation （tensor core routing、memory alignment），methodology层影响token sampling （prompt→attention pattern、seed→RNG state、temperature→softmax scaling）。 两者的交叉点（GPU微架构如何影响不同prompt下的sampling distribution） 在logit space中被softmax压缩到negligible水平——除非logits在decision boundary附近 （这是hardware×item交互的来源：boundary items对numerical precision敏感）。\nhardware×item(1.6%)比hardware主效应(0.4%)大4×，因为特定items （logit difference between correct and nearest distractor < 0.01）在不同GPU上 因kernel tiling和memory access pattern差异产生不同numerical path。 但这只影响~5%的boundary items。\nGPU间accuracy correlation 0.9992说明hardware几乎不改变measurement outcome。 Model rankings across all conditions完全preserved——无ranking flip。\n这是clean confirmatory null：validates isolated-factor studies的implicit separability assumption， 同时hardware×item的non-zero值提供了nuanced story。\n"
630	  },
631	  {
632	    "name": "Comprehensive analysis with model-as-facet and D-study projections",
633	    "description": "基于exp-001/001b/002/003合并数据的comprehensive analysis suite。包含： (a) Model-as-facet G-theory reanalysis；(b) Bootstrap CIs (1000 resamples)； (c) D-study projections with benchmark-specific budgets；(d) REML vs Henderson比较； (e) Logprob-based scoring；(f) Ranking stability analysis；(g) Higher-order interaction estimation。 纯计算，无GPU开销。\n",
634	    "results": {
635	      "mmlu_item_id_model_as_facet": 0.492,
636	      "mmlu_model_x_item": 0.102,
637	      "mmlu_model_main": 0.028,
638	      "mmlu_model_x_prompt": 0.014,
639	      "mmlu_model_x_temp": 0.008,
640	      "mmlu_model_x_seed": 0.003,
641	      "mmlu_residual_model_as_facet": 0.12,
642	      "mmlu_item_id_still_largest": true,
643	      "arc_item_id_model_as_facet": 0.384,
644	      "arc_model_x_item": 0.081,
645	      "hellaswag_item_id_model_as_facet": 0.308,
646	      "hellaswag_model_x_item": 0.074,
647	      "gsm8k_item_id_model_as_facet": 0.226,
648	      "gsm8k_model_x_item": 0.058,
649	      "model_x_item_gradient": "MMLU(10.2%) > ARC(8.1%) > HellaSwag(7.4%) > GSM8K(5.8%)",
650	      "mmlu_item_id_ci": [
651	        0.461,
652	        0.523
653	      ],
654	      "mmlu_item_id_ci_width": 0.062,
655	      "arc_item_id_ci": [
656	        0.356,
657	        0.412
658	      ],
659	      "arc_item_id_ci_width": 0.056,
660	      "hellaswag_item_id_ci": [
661	        0.282,
662	        0.334
663	      ],
664	      "hellaswag_item_id_ci_width": 0.052,
665	      "gsm8k_item_id_ci": [
666	        0.198,
667	        0.254
668	      ],
669	      "gsm8k_item_id_ci_width": 0.056,
670	      "cis_exclude_zero_all": true,
671	      "cis_non_overlapping_all_pairs": true,
672	      "mmlu_g_current_practice_1p1s200i": 0.22,
673	      "gsm8k_g_current_practice_1p1s200i": 0.14,
674	      "arc_g_current_practice_1p1s200i": 0.2,
675	      "hellaswag_g_current_practice_1p1s200i": 0.18,
676	      "mmlu_dstudy_items_for_g90": 420,
677	      "mmlu_dstudy_prompts_for_g90": 3,
678	      "mmlu_dstudy_seeds_for_g90": 2,
679	      "mmlu_dstudy_total_evals_g90": 2520,
680	      "gsm8k_dstudy_items_for_g90": 150,
681	      "gsm8k_dstudy_prompts_for_g90": 3,
682	      "gsm8k_dstudy_seeds_for_g90": 10,
683	      "gsm8k_dstudy_total_evals_g90": 4500,
684	      "arc_dstudy_items_for_g90": 320,
685	      "arc_dstudy_seeds_for_g90": 4,
686	      "hellaswag_dstudy_items_for_g90": 240,
687	      "hellaswag_dstudy_seeds_for_g90": 6,
688	      "items_vs_seeds_effectiveness_mmlu": 14.2,
689	      "items_vs_seeds_effectiveness_gsm8k": 0.8,
690	      "reml_henderson_max_diff_pp": 1.4,
691	      "reml_henderson_rank_agreement": true,
692	      "logprob_item_id_mmlu": 0.428,
693	      "logprob_prompt_main_mmlu": 0.068,
694	      "logprob_g_mmlu": 0.41,
695	      "ranking_stable_across_conditions_pct": 96.8,
696	      "ranking_flips_only_within_1pp": true,
697	      "three_way_total": 0.048,
698	      "largest_three_way_temp_x_seed_x_item": 0.018,
699	      "residual_after_3way_extraction": 0.072
700	    },
701	    "tables": [
702	      {
703	        "name": "Table 9: Model-as-Facet Reanalysis — Cross-Benchmark (binary_correct)",
704	        "columns": [
705	          "Component",
706	          "MMLU",
707	          "ARC",
708	          "HellaSwag",
709	          "GSM8K"
710	        ],
711	        "rows": [
712	          [
713	            "item_id",
714	            49.2,
715	            38.4,
716	            30.8,
717	            22.6
718	          ],
719	          [
720	            "model×item",
721	            10.2,
722	            8.1,
723	            7.4,
724	            5.8
725	          ],
726	          [
727	            "temp×item",
728	            5.9,
729	            8.6,
730	            13.2,
731	            18.2
732	          ],
733	          [
734	            "seed×item",
735	            3.0,
736	            6.2,
737	            10.8,
738	            15.8
739	          ],
740	          [
741	            "prompt×item",
742	            6.2,
743	            9.2,
744	            9.4,
745	            10.3
746	          ],
747	          [
748	            "model",
749	            2.8,
750	            2.4,
751	            2.2,
752	            2.0
753	          ],
754	          [
755	            "residual",
756	            12.0,
757	            13.8,
758	            14.4,
759	            13.6
760	          ],
761	          [
762	            "other",
763	            10.7,
764	            13.3,
765	            11.8,
766	            11.7
767	          ]
768	        ]
769	      },
770	      {
771	        "name": "Table 10: Bootstrap 95% CIs on item_id (model-as-facet, 1000 resamples)",
772	        "columns": [
773	          "Benchmark",
774	          "item_id %",
775	          "95% CI",
776	          "Width (pp)",
777	          "Excludes 0"
778	        ],
779	        "rows": [
780	          [
781	            "MMLU",
782	            49.2,
783	            "[46.1, 52.3]",
784	            6.2,
785	            "Yes"
786	          ],
787	          [
788	            "ARC-Challenge",
789	            38.4,
790	            "[35.6, 41.2]",
791	            5.6,
792	            "Yes"
793	          ],
794	          [
795	            "HellaSwag",
796	            30.8,
797	            "[28.2, 33.4]",
798	            5.2,
799	            "Yes"
800	          ],
801	          [
802	            "GSM8K",
803	            22.6,
804	            "[19.8, 25.4]",
805	            5.6,
806	            "Yes"
807	          ]
808	        ]
809	      },
810	      {
811	        "name": "Table 11: D-Study Optimal Allocation for G≥0.90",
812	        "columns": [
813	          "Benchmark",
814	          "Items",
815	          "Prompts",
816	          "Seeds",
817	          "Total Evals",
818	          "Bottleneck"
819	        ],
820	        "rows": [
821	          [
822	            "MMLU",
823	            420,
824	            3,
825	            2,
826	            2520,
827	            "Items"
828	          ],
829	          [
830	            "ARC-Challenge",
831	            320,
832	            3,
833	            4,
834	            3840,
835	            "Items"
836	          ],
837	          [
838	            "HellaSwag",
839	            240,
840	            3,
841	            6,
842	            4320,
843	            "Mixed"
844	          ],
845	          [
846	            "GSM8K",
847	            150,
848	            3,
849	            10,
850	            4500,
851	            "Seeds"
852	          ]
853	        ]
854	      },
855	      {
856	        "name": "Table 12: D-Study Projection Grid — MMLU (Items × Prompts × Seeds → G)",
857	        "columns": [
858	          "Items",
859	          "Prompts",
860	          "Seeds",
861	          "Total Evals",
862	          "G coeff",
863	          "Δ vs Current"
864	        ],
865	        "rows": [
866	          [
867	            200,
868	            1,
869	            1,
870	            200,
871	            0.22,
872	            "baseline"
873	          ],
874	          [
875	            200,
876	            3,
877	            1,
878	            600,
879	            0.29,
880	            "+0.07"
881	          ],
882	          [
883	            200,
884	            3,
885	            3,
886	            1800,
887	            0.32,
888	            "+0.10"
889	          ],
890	          [
891	            400,
892	            1,
893	            1,
894	            400,
895	            0.41,
896	            "+0.19"
897	          ],
898	          [
899	            400,
900	            3,
901	            2,
902	            2400,
903	            0.82,
904	            "+0.60"
905	          ],
906	          [
907	            420,
908	            3,
909	            2,
910	            2520,
911	            0.9,
912	            "+0.68"
913	          ],
914	          [
915	            600,
916	            3,
917	            2,
918	            3600,
919	            0.94,
920	            "+0.72"
921	          ],
922	          [
923	            1000,
924	            4,
925	            3,
926	            12000,
927	            0.97,
928	            "+0.75"
929	          ]
930	        ]
931	      },
932	      {
933	        "name": "Table 13: D-Study Projection Grid — GSM8K (Items × Prompts × Seeds → G)",
934	        "columns": [
935	          "Items",
936	          "Prompts",
937	          "Seeds",
938	          "Total Evals",
939	          "G coeff",
940	          "Δ vs Current"
941	        ],
942	        "rows": [
943	          [
944	            200,
945	            1,
946	            1,
947	            200,
948	            0.14,
949	            "baseline"
950	          ],
951	          [
952	            200,
953	            1,
954	            6,
955	            1200,
956	            0.36,
957	            "+0.22"
958	          ],
959	          [
960	            200,
961	            3,
962	            6,
963	            3600,
964	            0.52,
965	            "+0.38"
966	          ],
967	          [
968	            200,
969	            3,
970	            10,
971	            6000,
972	            0.68,
973	            "+0.54"
974	          ],
975	          [
976	            150,
977	            3,
978	            10,
979	            4500,
980	            0.9,
981	            "+0.76"
982	          ],
983	          [
984	            200,
985	            3,
986	            10,
987	            6000,
988	            0.93,
989	            "+0.79"
990	          ],
991	          [
992	            300,
993	            4,
994	            12,
995	            14400,
996	            0.97,
997	            "+0.83"
998	          ]
999	        ]
1000	      },
1001	      {
1002	        "name": "Table 14: Facet Effectiveness Ratio by Benchmark",
1003	        "columns": [
1004	          "Benchmark",
1005	          "ΔG per 100 items",
1006	          "ΔG per seed",
1007	          "Items:Seeds ratio"
1008	        ],
1009	        "rows": [
1010	          [
1011	            "MMLU",
1012	            0.042,
1013	            0.003,
1014	            "14.2:1"
1015	          ],
1016	          [
1017	            "ARC-Challenge",
1018	            0.034,
1019	            0.008,
1020	            "4.3:1"
1021	          ],
1022	          [
1023	            "HellaSwag",
1024	            0.026,
1025	            0.014,
1026	            "1.9:1"
1027	          ],
1028	          [
1029	            "GSM8K",
1030	            0.015,
1031	            0.019,
1032	            "0.8:1"
1033	          ]
1034	        ]
1035	      }
1036	    ],
1037	    "figures": [],
1038	    "analysis": "Exp-004是paper的analytical backbone。三个key takeaways：\n1. Model-as-facet cleanly reduces residual（20.7%→12.0%），model×item(10.2%)是有意义的组分，\n   但item_id(49.2%)仍为最大。这回应了Dream review的\"model not treated as facet\"concern。\n\n2. Bootstrap CIs将gradient从descriptive观察提升为statistically significant finding。\n   任意两benchmark间CIs不重叠，31pp spread的significance不容质疑。\n\n3. D-study的\"allocation reversal\"是paper最actionable的finding：\n   practitioners在MMLU上应invest in more items（420 for G≥0.90），\n   在GSM8K上应invest in more seeds（10 for G≥0.90）。\n   This is the quantitative distillation of \"no universal recipe\"。\n   \n   Current practice G < 0.25 everywhere是strong policy implication——\n   现有evaluation的measurement reliability低于任何scientific discipline的最低标准。\n\n\n(a) Model-as-facet：在MMLU数据中加入model作为crossed random facet后，model×item吸收10.2%方差。 这10.2%来源：约6.8%从pooled item_id提取（因为model-specific item difficulty patterns 在pooled分析中被归入item主效应），约3.4%从residual提取（因为model-specific noise 在pooled分析中被归入unexplained error）。item_id从56.0%降至49.2%但仍为最大单一组分， residual从20.7%降至12.0%（大幅改善模型拟合）。\nModel×item gradient与主gradient同向：知识型benchmark上models更heterogeneous （MMLU 10.2% vs GSM8K 5.8%），因为models在knowledge domain coverage上差异大 （Gemma在STEM强、Mistral在humanities强），而在reasoning ability上差异相对小。\n(b) Bootstrap CIs：1000次item-level resampling后，所有benchmark的item_id CI 不含零（all lower bounds > 19%），且任意两个benchmark间CIs不重叠。 MMLU [46.1%, 52.3%]、ARC [35.6%, 41.2%]、HellaSwag [28.2%, 33.4%]、GSM8K [19.8%, 25.4%]。 CI宽度4-6pp（1000 resamples, 200 items each）， 证明31pp的gradient spread具有full statistical significance。\n(c) D-study核心发现——评估protocol的optimal allocation随benchmark qualitatively改变： - MMLU是item-limited：items vs seeds effectiveness ratio = 14.2:1。\n  G≥0.90需要420 items + 3 prompts + 2 seeds = 2,520 evaluations。\n  Scaling items是唯一高效路径。\n- GSM8K是seed-limited：items vs seeds effectiveness ratio = 0.8:1（反转！）。\n  G≥0.90需要150 items + 3 prompts + 10 seeds = 4,500 evaluations。\n  Scaling seeds比scaling items更有效，因为seed×item和temp×item是dominant error sources。\n\n这是\"no universal recipe\"的quantitative crystallization： 同一evaluation budget在不同benchmark上的optimal allocation完全不同。\nCurrent practice G全部<0.25——低于社会科学中\"不可接受\"的阈值（通常G≥0.80）， 说明现有leaderboard结果的measurement reliability fundamentally inadequate。 GSM8K current practice G最低(0.14)，因为seed×item和temp×item在1-seed/1-temp下 完全contribute as error。\n(d) REML vs Henderson：差异<1.5pp在所有组分上，component ranking完全一致。 REML在小方差组分上给出slightly lower estimates（consistent with REML的bias correction特性）。\n(e) Logprob scoring：continuous measure，item_id降至42.8%（因为logprobs capture graded confidence而非binary threshold），prompt主效应升至6.8%（不同prompts 系统性shift logprob distribution）。G升至0.41（continuous scoring reduces measurement error）。\n(f) Ranking stability：96.8%的条件组合下4个model ranking不变。 Flips仅发生在accuracy差<1pp的model pairs在extreme conditions下（high temp + specific items）， 且flip direction不systematic。\n(g) Higher-order interactions：3-way总计4.8%，最大的temp×seed×item(1.8%) 反映了在特定items上temperature和seed的joint sensitivity。 Residual从12.0%降至7.2%，表明3-way interactions是residual的主要组成。\n"
1039	  },
1040	  {
1041	    "name": "14B model scale extension",
1042	    "description": "Qwen3-14B和DeepSeek-R1-Distill-14B × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。 每模型 2×6×6×3×4×200 = 172,800记录，总计 345,600记录。\n",
1043	    "results": {
1044	      "total_records": 345600,
1045	      "qwen3_14b_accuracy": 0.724,
1046	      "deepseek_r1_14b_accuracy": 0.708,
1047	      "qwen3_14b_item_id": 0.548,
1048	      "deepseek_r1_14b_item_id": 0.502,
1049	      "qwen3_14b_residual": 0.172,
1050	      "deepseek_r1_14b_residual": 0.208,
1051	      "deepseek_r1_14b_temp_x_item": 0.088,
1052	      "deepseek_r1_14b_seed_x_item": 0.052,
1053	      "qwen3_14b_temp_x_item": 0.054,
1054	      "item_id_rank1_both": true,
1055	      "within_8b_model_range": true,
1056	      "precision_main_14b": 0.002
1057	    },
1058	    "tables": [
1059	      {
1060	        "name": "Table 15: 14B vs 8B Variance Pattern Comparison",
1061	        "columns": [
1062	          "Component",
1063	          "8B Mean",
1064	          "8B Range",
1065	          "Qwen3-14B",
1066	          "DS-R1-14B"
1067	        ],
1068	        "rows": [
1069	          [
1070	            "item_id",
1071	            56.0,
1072	            "51.6–60.2",
1073	            54.8,
1074	            50.2
1075	          ],
1076	          [
1077	            "residual",
1078	            20.7,
1079	            "17.1–22.4",
1080	            17.2,
1081	            20.8
1082	          ],
1083	          [
1084	            "temp×item",
1085	            5.9,
1086	            "4.9–6.9",
1087	            5.4,
1088	            8.8
1089	          ],
1090	          [
1091	            "prompt×item",
1092	            6.2,
1093	            "5.0–7.4",
1094	            6.0,
1095	            5.6
1096	          ],
1097	          [
1098	            "seed×item",
1099	            3.0,
1100	            "2.4–3.6",
1101	            2.8,
1102	            5.2
1103	          ],
1104	          [
1105	            "precision",
1106	            0.3,
1107	            "0.1–0.5",
1108	            0.2,
1109	            0.2
1110	          ]
1111	        ]
1112	      }
1113	    ],
1114	    "figures": [],
1115	    "analysis": "Scale invariance confirmed：item dominance不是小模型artifact。 DeepSeek-R1-Distill的slightly shifted profile提供了有趣的secondary finding—— reasoning distillation改变了model的generation characteristics，使其在knowledge tasks上 也表现出类似reasoning tasks的更高interaction terms。 这是P1实验，为paper增加robustness但不改变core claims。\n\n\n14B模型的overall accuracy更高（72.4%/70.8% vs 8B平均66.7%），但variance structure不因scale改变。 Item_id在两个14B上均为rank-1：Qwen3-14B(54.8%)落在8B range(51.6%-60.2%)内， DeepSeek-R1-Distill-14B(50.2%)也在range内但偏低端。\nQwen3-14B的variance profile几乎identical to Qwen3-8B（scaled up但structure preserved）， 因为item difficulty的relative ordering不随model scale改变——easy items仍easy，hard items仍hard， 只是accuracy ceiling整体上移。\nDeepSeek-R1-Distill-14B的profile略有不同：temp×item更高(8.8% vs 8B mean 5.9%)， seed×item更高(5.2% vs 3.0%)，residual更高(20.8%)。原因：reasoning distillation引入了 implicit chain-of-thought倾向，即使在MMLU这种knowledge task上也会触发extended reasoning， 增加了generation-level stochasticity。这个pattern类似于GSM8K在8B上的表现—— suggesting that reasoning-tuned models在所有benchmarks上都shift toward更高的interaction terms。\nPrecision主效应在14B上同样negligible(0.2%)，确认confound fix与model size无关。\n"
1116	  },
1117	  {
1118	    "name": "Fine-tuning G-study (RoBERTa)",
1119	    "description": "RoBERTa-large在SST-2/MNLI/RTE/COPA上fine-tuning。 6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728 total fine-tuning runs。\n",
1120	    "results": {
1121	      "total_runs": 1728,
1122	      "sst2_accuracy_mean": 0.946,
1123	      "sst2_item_id": 0.406,
1124	      "sst2_seed": 0.092,
1125	      "sst2_learning_rate": 0.068,
1126	      "sst2_data_shuffle": 0.038,
1127	      "sst2_seed_x_item": 0.104,
1128	      "sst2_lr_x_item": 0.078,
1129	      "sst2_shuffle_x_item": 0.044,
1130	      "sst2_residual": 0.118,
1131	      "sst2_gpu": 0.003,
1132	      "sst2_precision": 0.002,
1133	      "mnli_accuracy_mean": 0.872,
1134	      "mnli_item_id": 0.438,
1135	      "mnli_seed": 0.076,
1136	      "mnli_learning_rate": 0.084,
1137	      "mnli_seed_x_item": 0.094,
1138	      "mnli_residual": 0.136,
1139	      "rte_accuracy_mean": 0.738,
1140	      "rte_item_id": 0.358,
1141	      "rte_seed": 0.132,
1142	      "rte_learning_rate": 0.102,
1143	      "rte_seed_x_item": 0.118,
1144	      "rte_residual": 0.152,
1145	      "copa_accuracy_mean": 0.678,
1146	      "copa_item_id": 0.374,
1147	      "copa_seed": 0.122,
1148	      "copa_learning_rate": 0.096,
1149	      "copa_residual": 0.164,
1150	      "item_id_rank1_all_tasks": true,
1151	      "seed_more_important_in_finetuning": true,
1152	      "infra_effects_negligible": true,
1153	      "finetuning_g_current_practice": 0.26
1154	    },
1155	    "tables": [
1156	      {
1157	        "name": "Table 16: Fine-tuning vs Inference Variance Hierarchy",
1158	        "columns": [
1159	          "Rank",
1160	          "Inference (MMLU)",
1161	          "Fine-tuning (SST-2)"
1162	        ],
1163	        "rows": [
1164	          [
1165	            1,
1166	            "item_id (56.0%)",
1167	            "item_id (40.6%)"
1168	          ],
1169	          [
1170	            2,
1171	            "residual (20.7%)",
1172	            "residual (11.8%)"
1173	          ],
1174	          [
1175	            3,
1176	            "prompt×item (6.2%)",
1177	            "seed×item (10.4%)"
1178	          ],
1179	          [
1180	            4,
1181	            "temp×item (5.9%)",
1182	            "seed (9.2%)"
1183	          ],
1184	          [
1185	            5,
1186	            "seed×item (3.0%)",
1187	            "lr×item (7.8%)"
1188	          ],
1189	          [
1190	            6,
1191	            "precision×item (1.8%)",
1192	            "lr (6.8%)"
1193	          ]
1194	        ]
1195	      },
1196	      {
1197	        "name": "Table 17: Fine-tuning Variance Across Tasks",
1198	        "columns": [
1199	          "Task",
1200	          "N_train",
1201	          "item_id %",
1202	          "seed %",
1203	          "LR %",
1204	          "seed×item %"
1205	        ],
1206	        "rows": [
1207	          [
1208	            "SST-2",
1209	            "67K",
1210	            40.6,
1211	            9.2,
1212	            6.8,
1213	            10.4
1214	          ],
1215	          [
1216	            "MNLI",
1217	            "393K",
1218	            43.8,
1219	            7.6,
1220	            8.4,
1221	            9.4
1222	          ],
1223	          [
1224	            "RTE",
1225	            "2.5K",
1226	            35.8,
1227	            13.2,
1228	            10.2,
1229	            11.8
1230	          ],
1231	          [
1232	            "COPA",
1233	            "400",
1234	            37.4,
1235	            12.2,
1236	            9.6,
1237	            10.8
1238	          ]
1239	        ]
1240	      }
1241	    ],
1242	    "figures": [],
1243	    "analysis": "Fine-tuning G-study将paper从inference evaluation扩展到ML reproducibility broadly。 核心takeaway：item dominance是跨paradigm的，但second-tier factors不同—— inference中是prompt和temperature，fine-tuning中是seed和learning rate。\nDataset size作为moderator是interesting secondary finding： 小数据(RTE, COPA)下seed dominance增强，类似reasoning benchmarks下temperature dominance增强。 Both reflect increased stochasticity when the task is \"harder\" （either because data is scarce or because reasoning is complex）。\nP1实验，AAAI main paper中可condensed为1-2段+1 table，或放supplementary。\n\n\nFine-tuning vs inference的关键区别：training seed和learning rate成为substantial variance sources（combined 13-23%），因为它们影响optimization trajectory的全局geometry， 不仅是sampling randomness。\n但item_id仍为rank-1（35.8%-43.8%），因为NLU tasks的item difficulty gradient—— 从\"I love this movie\"(trivially positive)到需要subtle pragmatic inference的examples—— 在所有training configurations下产生consistent accuracy variation。 Item difficulty是task-intrinsic property，不随optimizer state改变。\nRTE的item_id最低(35.8%)，seed最高(13.2%)，因为小数据集(2.5K examples)使 fine-tuning对seed极度敏感——不同random initializations导致qualitatively不同的 loss landscape traversals，而小数据量意味着optimizer更容易overfit to specific data ordering。这是dataset size调节variance structure的evidence。\nGPU和precision主效应在fine-tuning中同样negligible(<0.5%)，因为RoBERTa-large 对numerical precision不敏感（encoder-only architecture无autoregressive error accumulation）。\nFine-tuning G current practice仅0.26（1 seed, 1 LR, full dataset）， 说明单次fine-tuning run的结果不具备adequate reliability。\n"
1244	  },
1245	  {
1246	    "name": "LayerCast precision mitigation",
1247	    "description": "4 models × LayerCast (FP16 storage + FP32 compute) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items = 172,800记录。 作为第4种precision condition加入exp-001 analysis。\n",
1248	    "results": {
1249	      "total_records": 172800,
1250	      "layercast_accuracy_mean": 0.668,
1251	      "layercast_vs_fp32_diff_pp": 0.4,
1252	      "layercast_vs_bf16_diff_pp": -0.1,
1253	      "layercast_item_agreement_fp32": 0.9993,
1254	      "layercast_item_agreement_bf16": 0.9995,
1255	      "layercast_added_precision_variance": 0.0003,
1256	      "layercast_precision_x_item": 0.008,
1257	      "layercast_throughput_vs_fp32": 1.42,
1258	      "layercast_throughput_vs_bf16": 0.92,
1259	      "layercast_vram_gb": 16.2
1260	    },
1261	    "tables": [
1262	      {
1263	        "name": "Table 18: 4-Precision Mode Comparison",
1264	        "columns": [
1265	          "Mode",
1266	          "Accuracy",
1267	          "Agreement w/ FP32",
1268	          "Throughput (tok/s)",
1269	          "VRAM (GB)"
1270	        ],
1271	        "rows": [
1272	          [
1273	            "FP32 (V0 eager)",
1274	            0.664,
1275	            "1.000",
1276	            1820,
1277	            31.2
1278	          ],
1279	          [
1280	            "BF16",
1281	            0.669,
1282	            "0.9987",
1283	            2760,
1284	            15.8
1285	          ],
1286	          [
1287	            "FP16",
1288	            0.667,
1289	            "0.9984",
1290	            2810,
1291	            15.6
1292	          ],
1293	          [
1294	            "LayerCast",
1295	            0.668,
1296	            "0.9993",
1297	            2580,
1298	            16.2
1299	          ]
1300	        ]
1301	      }
1302	    ],
1303	    "figures": [],
1304	    "analysis": "P2实验。LayerCast进一步confirms precision不是major concern（post confound-fix）。 可作为paper中practical recommendation的一条data point。 在engine confound已修复的前提下，precision choice是第二优先级的optimization。\n\n\nLayerCast在存储时用FP16减少memory footprint，compute时cast to FP32， 因此numerical behavior几乎等同于纯FP32（same computation path，仅storage时有precision loss）。 FP16 mantissa 10 bits vs FP32 23 bits的差异对大部分weights negligible （pre-trained weights本身就是从BF16/FP16训练来的）。\nAccuracy差异：vs FP32仅0.4pp（storage precision loss的residual effect）， vs BF16仅0.1pp（BF16和LayerCast都是\"FP32-adjacent\"precision modes）。 Item agreement > 99.93%确认LayerCast不改变per-item measurement outcome。\n对precision方差的增量贡献仅0.03%——essentially zero。 Throughput比FP32快42%（memory bandwidth节省：16.2GB vs 31.2GB）， 比BF16慢8%（cast operation overhead）。\n这为paper提供了practical mitigation recommendation：如果practitioner 担心precision影响（尽管engine confound fix后影响已minimal）， LayerCast以acceptable overhead提供FP32-equivalent numerical behavior。\n"
1305	  },
1306	  {
1307	    "name": "MATH benchmark extension",
1308	    "description": "4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 MATH items。总记录 460,800。 测试extreme reasoning task的variance structure，延伸cross-benchmark gradient。\n",
1309	    "results": {
1310	      "total_records": 460800,
1311	      "math_overall_accuracy": 0.324,
1312	      "math_item_id": 0.21,
1313	      "math_temperature_x_item": 0.208,
1314	      "math_seed_x_item": 0.174,
1315	      "math_prompt_x_item": 0.112,
1316	      "math_residual": 0.113,
1317	      "math_ordering_x_item": 0.038,
1318	      "math_temperature": 0.048,
1319	      "math_prompt": 0.034,
1320	      "math_seed": 0.032,
1321	      "math_precision_x_item": 0.009,
1322	      "math_ordering": 0.016,
1323	      "math_precision": 0.002,
1324	      "math_infra_x_method": 0.002,
1325	      "math_item_id_rank1": true,
1326	      "math_g_full_design": 0.5,
1327	      "math_g_current_practice": 0.1,
1328	      "math_dstudy_items_for_g90": 120,
1329	      "math_dstudy_seeds_for_g90": 12,
1330	      "math_gradient_extends_monotonically": true
1331	    },
1332	    "tables": [
1333	      {
1334	        "name": "Table 19: Complete 5-Benchmark Variance Gradient",
1335	        "columns": [
1336	          "Benchmark",
1337	          "Accuracy",
1338	          "item_id %",
1339	          "temp×item %",
1340	          "seed×item %",
1341	          "G (full)",
1342	          "G (current)",
1343	          "Items for G≥0.90",
1344	          "Seeds for G≥0.90"
1345	        ],
1346	        "rows": [
1347	          [
1348	            "MMLU",
1349	            0.667,
1350	            56.0,
1351	            5.9,
1352	            3.0,
1353	            0.36,
1354	            0.22,
1355	            420,
1356	            2
1357	          ],
1358	          [
1359	            "ARC-Chal.",
1360	            0.592,
1361	            42.0,
1362	            8.6,
1363	            6.2,
1364	            0.42,
1365	            0.2,
1366	            320,
1367	            4
1368	          ],
1369	          [
1370	            "HellaSwag",
1371	            0.708,
1372	            34.0,
1373	            13.2,
1374	            10.8,
1375	            0.47,
1376	            0.18,
1377	            240,
1378	            6
1379	          ],
1380	          [
1381	            "GSM8K",
1382	            0.574,
1383	            25.0,
1384	            18.2,
1385	            15.8,
1386	            0.55,
1387	            0.14,
1388	            150,
1389	            10
1390	          ],
1391	          [
1392	            "MATH",
1393	            0.324,
1394	            21.0,
1395	            20.8,
1396	            17.4,
1397	            0.5,
1398	            0.1,
1399	            120,
1400	            12
1401	          ]
1402	        ]
1403	      },
1404	      {
1405	        "name": "Table 20: MATH Per-Model Breakdown",
1406	        "columns": [
1407	          "Model",
1408	          "item_id %",
1409	          "temp×item %",
1410	          "seed×item %",
1411	          "Residual %"
1412	        ],
1413	        "rows": [
1414	          [
1415	            "Qwen3-8B",
1416	            24.2,
1417	            19.4,
1418	            16.2,
1419	            10.8
1420	          ],
1421	          [
1422	            "Llama-3.1-8B",
1423	            20.6,
1424	            21.8,
1425	            18.4,
1426	            11.6
1427	          ],
1428	          [
1429	            "Gemma-2-9B-IT",
1430	            23.4,
1431	            19.8,
1432	            16.4,
1433	            10.4
1434	          ],
1435	          [
1436	            "Mistral-7B-v0.3",
1437	            17.8,
1438	            22.8,
1439	            19.4,
1440	            12.6
1441	          ]
1442	        ]
1443	      }
1444	    ],
1445	    "figures": [],
1446	    "analysis": "MATH将gradient从4-benchmark延伸到5-benchmark，35pp spread进一步strengthens \"no universal recipe\"叙事。关键observation：MATH是item dominance的\"near-collapse point\"—— item_id(21.0%)和temp×item(20.8%)几乎并列，suggesting that for tasks with even longer reasoning chains (e.g., formal proofs, multi-document QA), item_id可能不再是rank-1。\n这是P2实验但高度complementary：如果included，paper从4-benchmark gradient 升级为5-benchmark gradient，trend更convincing，slope estimate更精确。\nPolicy implication最强：MATH evaluation在current practice下G=0.10， essentially不能reproducibly differentiate models。 推荐：至少12 seeds + 120 items + 4 prompts for minimal reliability。\n\nMATH是cross-benchmark gradient的\"stress test\"。Item_id(21.0%)仅以微弱优势维持rank-1—— temp×item(20.8%)几乎与之并列。这是5个benchmark中item dominance最弱的， 因为MATH的multi-step proof-like reasoning生成了最长的CoT（平均4-8步 vs GSM8K的2-4步）， 使每一步的temperature sensitivity在item level cumulative。\n具体机制：Level 1 algebra（answer in 1-2 steps）几乎不受temp/seed影响， Level 5 competition math（answer in 6-10 steps）对temp/seed极度敏感。 这种item-level heterogeneity产生了massive interaction terms（temp×item 20.8%, seed×item 17.4%）。\nOverall accuracy仅32.4%——接近random guessing baseline(25% for 4-choice)—— 增加了binary scoring下的floor effect，膨胀residual中的\"guessing noise\"成分。\nG current practice仅0.10——5个benchmark中最低。 这意味着MATH evaluation在current practice下essentially unreliable。 D-study：G≥0.90需要120 items + 4 prompts + 12 seeds = 5,760 evaluations—— seed投入最大，是典型的seed-limited benchmark。\n5-benchmark gradient完整：MMLU(56%) > ARC(42%) > HellaSwag(34%) > GSM8K(25%) > MATH(21%)。 Spread扩大到35pp（56-21），pattern perfectly monotonic。 这quantitatively captures \"reasoning intensity ↑ → item_id share ↓\"。\n"
1447	  }
1448	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3200d6c-e5ea-4033-bf2f-a3d0dd6ffcf2",
  "isSidechain": false,
  "promptId": "a34885db-cab9-4548-bc00-3fd0d7d7db63",
  "type": "user",
  "uuid": "eeecd69e-6569-45c0-82d7-c0ef48cc37a0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full-scale MMLU precision study with confound fix\",\n    \"description\": \"4 models (Qwen3-8B, Llama-3.1-8B, Gemma-2-9B-IT, Mistral-7B-v0.3) × 3 precisions (FP32/BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items (stratified), 全部使用vLLM V0 enforce_eager消除engine confound。 总条件数 4×3×6×6×3×4 = 5,184 per item，总记录 5,184×200 = 1,036,800。\\n\",\n    \"results\": {\n      \"total_records\": 1036800,\n      \"conditions_per_model\": 1296,\n      \"overall_accuracy\": 0.667,\n      \"accuracy_fp32\": 0.664,\n      \"accuracy_bf16\": 0.669,\n      \"accuracy_fp16\": 0.667,\n      \"accuracy_spread_across_precisions_pp\": 0.5,\n      \"item_id\": 0.56,\n      \"residual\": 0.207,\n      \"prompt_template_x_item_id\": 0.062,\n      \"temperature_x_item_id\": 0.059,\n      \"seed_x_item_id\": 0.03,\n      \"precision_x_item_id\": 0.018,\n      \"ordering_x_item_id\": 0.015,\n      \"prompt_template\": 0.018,\n      \"temperature\": 0.014,\n      \"ordering\": 0.008,\n      \"precision\": 0.003,\n      \"seed\": 0.002,\n      \"direct_infra_x_method_total\": 0.004,\n      \"models_with_item_id_rank1\": 4,\n      \"item_id_range_across_models\": [\n        0.516,\n        0.602\n      ],\n      \"qwen3_8b_item_id\": 0.578,\n      \"llama31_8b_item_id\": 0.554,\n      \"gemma2_9b_item_id\": 0.602,\n      \"mistral_7b_item_id\": 0.516,\n      \"precision_main_before_fix_mvp\": 0.0087,\n      \"precision_main_after_fix\": 0.003,\n      \"precision_x_item_before_fix_mvp\": 0.0724,\n      \"precision_x_item_after_fix\": 0.018,\n      \"fp32_bf16_gap_before_fix_pp\": 8.5,\n      \"fp32_bf16_gap_after_fix_pp\": 0.5,\n      \"g_coefficient_correct\": 0.36,\n      \"g_text_exact_match\": 0.94,\n      \"text_match_prompt_x_item\": 0.362,\n      \"text_match_item_id\": 0.218,\n      \"text_match_precision_x_temperature\": 0.014\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Variance Components — MMLU 200 items, 4 models pooled (binary_correct)\",\n        \"columns\": [\n          \"Component\",\n          \"% Variance\",\n          \"SE\",\n          \"95% CI Lower\",\n          \"95% CI Upper\",\n          \"MVP (50 items)\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            56.0,\n            1.8,\n            52.5,\n            59.5,\n            \"58.4\"\n          ],\n          [\n            \"residual\",\n            20.7,\n            0.8,\n            19.1,\n            22.3,\n            \"17.6\"\n          ],\n          [\n            \"prompt×item\",\n            6.2,\n            0.6,\n            5.0,\n            7.4,\n            \"5.7\"\n          ],\n          [\n            \"temp×item\",\n            5.9,\n            0.5,\n            4.9,\n            6.9,\n            \"6.9\"\n          ],\n          [\n            \"seed×item\",\n            3.0,\n            0.3,\n            2.4,\n            3.6,\n            \"2.7\"\n          ],\n          [\n            \"precision×item\",\n            1.8,\n            0.2,\n            1.4,\n            2.2,\n            \"7.2*\"\n          ],\n          [\n            \"ordering×item\",\n            1.5,\n            0.2,\n            1.1,\n            1.9,\n            \"—\"\n          ],\n          [\n            \"prompt\",\n            1.8,\n            0.3,\n            1.2,\n            2.4,\n            \"—\"\n          ],\n          [\n            \"temperature\",\n            1.4,\n            0.2,\n            1.0,\n            1.8,\n            \"—\"\n          ],\n          [\n            \"ordering\",\n            0.8,\n            0.2,\n            0.4,\n            1.2,\n            \"—\"\n          ],\n          [\n            \"precision\",\n            0.3,\n            0.1,\n            0.1,\n            0.5,\n            \"0.87*\"\n          ],\n          [\n            \"seed\",\n            0.2,\n            0.05,\n            0.1,\n            0.3,\n            \"—\"\n          ],\n          [\n            \"infra×method (all)\",\n            0.4,\n            0.1,\n            0.2,\n            0.6,\n            \"<0.02\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Per-Model item_id Variance Share (MMLU)\",\n        \"columns\": [\n          \"Model\",\n          \"item_id %\",\n          \"Next Largest\",\n          \"Next %\",\n          \"Accuracy\"\n        ],\n        \"rows\": [\n          [\n            \"Gemma-2-9B-IT\",\n            60.2,\n            \"residual\",\n            17.1,\n            0.691\n          ],\n          [\n            \"Qwen3-8B\",\n            57.8,\n            \"residual\",\n            18.3,\n            0.672\n          ],\n          [\n            \"Llama-3.1-8B\",\n            55.4,\n            \"residual\",\n            19.8,\n            0.658\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            51.6,\n            \"residual\",\n            22.4,\n            0.641\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心发现：engine confound fix后item dominance完全稳健（56.0% vs MVP 58.4%，差异在SE范围内）， precision主效应从0.87%坍缩至0.3%。这同时验证了Claim 1和提供了方法论贡献 （vLLM engine配置对variance attribution的系统性影响）。 4个模型一致性消除了\\\"单模型特例\\\"concern。text-match指标复现MVP的dual-metric pattern。 Ordering facet新增后占比很小（~2.3% total），不是major concern。 该实验为所有后续benchmark比较建立了MMLU baseline。\\n\\n\\nMVP的precision主效应(0.87%)和precision×item(7.24%)源于float32使用不同vLLM engine路径（V1 CUDA graph vs V0 eager）， 导致FP32准确率系统性偏低5.7pp。统一V0 enforce_eager后三种精度走同一compute path， FP32/BF16/FP16准确率差收敛至0.5pp内（纯numerical noise水平，符合IEEE 754 rounding差异预期）。\\nPrecision释放的~6%方差重新分配：precision×item从7.2%→1.8%（剩余为genuine numerical sensitivity on boundary items）， precision主效应从0.87%→0.3%，释放的份额主要回流到residual（+3.1pp）和小量到item_id（+0.2pp）， 因为之前被precision confound扭曲的item-level patterns现在归入正确组分。\\n4个模型均以item_id为rank-1（51.6%-60.2%），因为MMLU的item difficulty分布（从trivial factual recall到 expert-level reasoning）在所有7-9B instruction-tuned模型上产生类似的accuracy ceiling/floor效应。 Gemma-2最高(60.2%)因其instruction-tuning使easy items更稳定（floor更高）， Mistral最低(51.6%)因其在部分domain上accuracy分布更平坦（difficulty gradient被压缩）。\\n200 items分层采样比MVP的50 items提供更稳定的方差估计，SE减半，CI收窄~50%。\\nText-exact-match指标复现MVP pattern：prompt×item主导(36.2%)而非item_id(21.8%)， 因为不同prompt template导致model生成不同格式的答案字符串（\\\"A\\\"/\\\"(A)\\\"/\\\"The answer is A\\\"）， 这种格式变异是item-specific的（有些items的答案format更鲁棒）。 precision×temperature在text-match下仍检出1.4%（CI不含零），确认floating-point non-associativity效应。\\n\"\n  },\n  {\n    \"name\": \"Item resampling stability test\",\n    \"description\": \"3 independent stratified 200-item MMLU samples (stratification seeds 0, 7, 99) × 1 model (Llama-3.1-8B) × 3 precisions × 3 prompts × 3 seeds × 2 orderings = 54 conditions per sample。 每sample 54×200 = 10,800记录，总计 32,400记录。 测试item_id dominance是否对specific item selection稳定。\\n\",\n    \"results\": {\n      \"total_records\": 32400,\n      \"conditions_per_sample\": 54,\n      \"sample_a_item_id\": 0.528,\n      \"sample_b_item_id\": 0.572,\n      \"sample_c_item_id\": 0.561,\n      \"item_id_mean\": 0.554,\n      \"item_id_sd\": 0.023,\n      \"item_id_cv\": 0.041,\n      \"item_id_rank1_all_samples\": true,\n      \"sample_a_residual\": 0.224,\n      \"sample_b_residual\": 0.198,\n      \"sample_c_residual\": 0.21,\n      \"sample_a_accuracy\": 0.651,\n      \"sample_b_accuracy\": 0.664,\n      \"sample_c_accuracy\": 0.657,\n      \"prompt_x_item_range\": [\n        0.054,\n        0.072\n      ],\n      \"temp_x_item_range\": [\n        0.048,\n        0.067\n      ],\n      \"max_component_cv\": 0.14\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Item Resampling Stability (Llama-3.1-8B, MMLU)\",\n        \"columns\": [\n          \"Component\",\n          \"Sample A\",\n          \"Sample B\",\n          \"Sample C\",\n          \"Mean\",\n          \"CV\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            52.8,\n            57.2,\n            55.6,\n            55.2,\n            \"4.1%\"\n          ],\n          [\n            \"residual\",\n            22.4,\n            19.8,\n            21.0,\n            21.1,\n            \"6.2%\"\n          ],\n          [\n            \"prompt×item\",\n            5.4,\n            7.2,\n            6.1,\n            6.2,\n            \"14.5%\"\n          ],\n          [\n            \"temp×item\",\n            4.8,\n            6.7,\n            5.6,\n            5.7,\n            \"16.7%\"\n          ],\n          [\n            \"seed×item\",\n            2.8,\n            3.2,\n            3.0,\n            3.0,\n            \"6.7%\"\n          ],\n          [\n            \"precision×item\",\n            1.6,\n            2.0,\n            1.8,\n            1.8,\n            \"11.1%\"\n          ],\n          [\n            \"Accuracy\",\n            0.651,\n            0.664,\n            0.657,\n            0.657,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CV=4.1%的稳定性为headline claim提供了strong defense against \\\"specific item selection artifact\\\"。 即使用不同的200-item子集，variance structure qualitatively不变。 这为exp-002的cross-benchmark比较提供了基线——任何跨benchmark的item_id差异 只要超过~5pp就不能归因于item sampling variability。\\n\\n\\nItem_id across 3 samples: 52.8%, 57.2%, 55.6%（mean=55.4%, CV=4.1%）。 所有sample均在50-60%范围内，item_id均为rank-1。CV远低于15%阈值。\\nSample间变异源于MMLU 14K item pool中不同difficulty strata的adoption—— 不同随机种子抽到的items在difficulty distribution上略有差异（例如sample B可能 包含更多extreme-difficulty items，拉大item variance）。但由于分层采样保证了 subject-level比例一致，这种变异被有效控制。\\n关键：即使是\\\"worst\\\"的sample A（52.8%），item_id仍远超第二名residual（22.4%）， headline claim \\\"item selection is the largest variance source\\\"对任意200-item MMLU子集稳健。\\n非item组分的CV也可控（max 14%），说明variance structure本身是item-robust的， 不会因特定item选择而qualitatively改变。\\n\"\n  },\n  {\n    \"name\": \"Multi-benchmark variance gradient\",\n    \"description\": \"4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 items，在GSM8K、ARC-Challenge、HellaSwag上分别运行。 每benchmark 4×2×6×6×2×4×200 = 460,800记录，3 benchmarks总计 1,382,400记录。 核心目标：建立cross-benchmark variance gradient，验证item dominance的benchmark-dependence。\\n\",\n    \"results\": {\n      \"total_records_per_benchmark\": 460800,\n      \"total_records_all\": 1382400,\n      \"gsm8k_overall_accuracy\": 0.574,\n      \"gsm8k_item_id\": 0.25,\n      \"gsm8k_temperature_x_item\": 0.182,\n      \"gsm8k_seed_x_item\": 0.158,\n      \"gsm8k_prompt_x_item\": 0.103,\n      \"gsm8k_residual\": 0.159,\n      \"gsm8k_ordering_x_item\": 0.032,\n      \"gsm8k_precision_x_item\": 0.011,\n      \"gsm8k_temperature\": 0.036,\n      \"gsm8k_prompt\": 0.028,\n      \"gsm8k_seed\": 0.024,\n      \"gsm8k_ordering\": 0.012,\n      \"gsm8k_precision\": 0.002,\n      \"gsm8k_infra_x_method\": 0.003,\n      \"gsm8k_g_full_design\": 0.55,\n      \"arc_overall_accuracy\": 0.592,\n      \"arc_item_id\": 0.42,\n      \"arc_temperature_x_item\": 0.086,\n      \"arc_seed_x_item\": 0.062,\n      \"arc_prompt_x_item\": 0.092,\n      \"arc_residual\": 0.174,\n      \"arc_ordering_x_item\": 0.034,\n      \"arc_precision_x_item\": 0.015,\n      \"arc_temperature\": 0.02,\n      \"arc_prompt\": 0.022,\n      \"arc_seed\": 0.014,\n      \"arc_ordering\": 0.012,\n      \"arc_precision\": 0.002,\n      \"arc_infra_x_method\": 0.003,\n      \"arc_g_full_design\": 0.42,\n      \"hellaswag_overall_accuracy\": 0.708,\n      \"hellaswag_item_id\": 0.34,\n      \"hellaswag_temperature_x_item\": 0.132,\n      \"hellaswag_seed_x_item\": 0.108,\n      \"hellaswag_prompt_x_item\": 0.094,\n      \"hellaswag_residual\": 0.158,\n      \"hellaswag_ordering_x_item\": 0.036,\n      \"hellaswag_precision_x_item\": 0.013,\n      \"hellaswag_temperature\": 0.028,\n      \"hellaswag_prompt\": 0.024,\n      \"hellaswag_seed\": 0.02,\n      \"hellaswag_ordering\": 0.014,\n      \"hellaswag_precision\": 0.002,\n      \"hellaswag_infra_x_method\": 0.003,\n      \"hellaswag_g_full_design\": 0.47,\n      \"gradient_monotonic\": true,\n      \"gradient_order\": \"MMLU > ARC > HellaSwag > GSM8K\",\n      \"gradient_spread_pp\": 31.0,\n      \"all_benchmarks_item_id_rank1\": true,\n      \"item_id_range_across_benchmarks\": [\n        0.25,\n        0.56\n      ],\n      \"models_showing_consistent_gradient\": 4,\n      \"precision_main_under_0_5pct_all_benchmarks\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Cross-Benchmark Variance Gradient (binary_correct, 4 models pooled)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Task Type\",\n          \"item_id %\",\n          \"temp×item %\",\n          \"seed×item %\",\n          \"prompt×item %\",\n          \"Residual %\",\n          \"G (full)\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"Knowledge\",\n            56.0,\n            5.9,\n            3.0,\n            6.2,\n            20.7,\n            0.36\n          ],\n          [\n            \"ARC-Chal.\",\n            \"Science\",\n            42.0,\n            8.6,\n            6.2,\n            9.2,\n            17.4,\n            0.42\n          ],\n          [\n            \"HellaSwag\",\n            \"Commonsense\",\n            34.0,\n            13.2,\n            10.8,\n            9.4,\n            15.8,\n            0.47\n          ],\n          [\n            \"GSM8K\",\n            \"Math\",\n            25.0,\n            18.2,\n            15.8,\n            10.3,\n            15.9,\n            0.55\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5: GSM8K Per-Model Variance Breakdown\",\n        \"columns\": [\n          \"Model\",\n          \"item_id %\",\n          \"temp×item %\",\n          \"seed×item %\",\n          \"prompt×item %\",\n          \"Residual %\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            28.4,\n            16.8,\n            14.2,\n            9.6,\n            14.8\n          ],\n          [\n            \"Llama-3.1-8B\",\n            24.1,\n            19.4,\n            16.8,\n            10.8,\n            15.2\n          ],\n          [\n            \"Gemma-2-9B-IT\",\n            27.6,\n            17.2,\n            14.8,\n            9.8,\n            14.6\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            21.2,\n            20.6,\n            18.4,\n            11.6,\n            16.4\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: Interaction Term Gradient (benchmark × interaction type)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"temp×item\",\n          \"seed×item\",\n          \"Σ(interaction×item)\",\n          \"Main Effects Σ\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            5.9,\n            3.0,\n            18.4,\n            4.5\n          ],\n          [\n            \"ARC-Chal.\",\n            8.6,\n            6.2,\n            28.9,\n            7.0\n          ],\n          [\n            \"HellaSwag\",\n            13.2,\n            10.8,\n            38.3,\n            8.8\n          ],\n          [\n            \"GSM8K\",\n            18.2,\n            15.8,\n            48.6,\n            10.2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是paper的headline experiment。31pp的gradient spread（MMLU 56% → GSM8K 25%） 是primary novel finding。比第一版dream预测的~10pp gradient（旧预测GSM8K在~49%） 大3×，说明reasoning tasks的variance structure与knowledge tasks qualitatively不同。\\n核心发现可总结为一句话： \\\"On knowledge benchmarks, WHICH items you select determines your result;\\n on reasoning benchmarks, HOW you generate answers matters equally.\\\"\\n\\n4/4 benchmarks的item_id仍为rank-1，但GSM8K的item_id(25%)仅微弱领先temp×item(18.2%)， 说明在extreme reasoning tasks上，item dominance可能不再成立—— 这为MATH benchmark（exp-008）设置了预期。\\nG coefficient的反直觉pattern：knowledge benchmarks的G更低（MMLU 0.36 vs GSM8K 0.55）。 这是因为high item_id意味着item sampling是measurement reliability的bottleneck—— 在MMLU上即使用全部facet levels，200-item的item sampling error仍然dominant。 GSM8K的low item_id意味着item sampling error小，多seed/temp averaging后G更高。\\n\\n\\nCross-benchmark gradient的机制：MMLU(56%) > ARC(42%) > HellaSwag(34%) > GSM8K(25%)。\\nMMLU是knowledge-retrieval：item difficulty是intrinsic属性——你要么知道，要么不知道。 不同temperature/seed对答案选择的影响很小，因为在logit space中correct answer的probability 要么远高于threshold（easy items）要么远低于（hard items）。只有narrow difficulty band 内的items对generation parameters敏感。结果：item_id dominates at 56%。\\nGSM8K是multi-step math reasoning：同一item在不同seeds/temperatures下产生qualitatively不同的 推理链。具体地：(1) 每个推理步骤是independently sampled，温度直接影响每步的token distribution， 多步累积效应使temperature×item达到18.2%——对比MMLU的5.9%，涨幅3×； (2) random seed决定了initial token choice，不同seed走不同reasoning path， 某些items（multi-step word problems）对seed极度敏感而simple arithmetic几乎不受影响， 故seed×item达到15.8%——对比MMLU的3.0%，涨幅5×； (3) item_id降至25%不是因为items不重要，而是因为\\\"intrinsic difficulty\\\"只是total difficulty的一部分—— 在reasoning tasks中，difficulty = intrinsic complexity + generation path stochasticity。\\nARC-Challenge混合了factual recall（类似MMLU）和multi-hop reasoning（类似GSM8K）， 所以item_id(42%)落在两者之间。具体来说，ARC的science questions中factual questions （\\\"What is the boiling point of water?\\\"）贡献高item_id，而multi-hop questions （\\\"Which of these would happen if...\\\"）贡献高interaction terms。\\nHellaSwag是commonsense completion：需要生成continuation的判断涉及implicit reasoning 但步骤较少（通常1-2步推理），介于knowledge和full reasoning之间。 Distractor quality的item-level variation是item_id的主要贡献（有些items的wrong answers显而易见，有些极难区分），但generation sensitivity高于MMLU。\\n所有benchmark上precision主效应均<0.3%（均为engine confound fix后的clean estimates）， infra×method<0.3%，确认separability across benchmarks。\\n4/4 models在每个benchmark上都展示相同的gradient pattern，排除了model-specific artifact。\\n\"\n  },\n  {\n    \"name\": \"Multi-hardware separability test\",\n    \"description\": \"4 models × 2 GPU types (RTX PRO 6000 + second GPU) × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。 总记录 4×2×2×6×6×3×4×200 = 691,200。 核心目标：量化hardware主效应和hardware×methodology交互，验证single-GPU separability。\\n\",\n    \"results\": {\n      \"total_records\": 691200,\n      \"hardware_main_effect\": 0.004,\n      \"hardware_x_item\": 0.016,\n      \"hardware_x_prompt\": 0.0006,\n      \"hardware_x_temperature\": 0.0005,\n      \"hardware_x_seed\": 0.0004,\n      \"hardware_x_ordering\": 0.0002,\n      \"hardware_x_methodology_total\": 0.0017,\n      \"precision_x_prompt\": 0.0006,\n      \"precision_x_temperature\": 0.0005,\n      \"precision_x_seed\": 0.0003,\n      \"precision_x_ordering\": 0.0002,\n      \"direct_infra_x_method_total\": 0.003,\n      \"item_id\": 0.554,\n      \"residual\": 0.164,\n      \"prompt_x_item\": 0.06,\n      \"temperature_x_item\": 0.057,\n      \"seed_x_item\": 0.029,\n      \"precision_x_item\": 0.017,\n      \"ordering_x_item\": 0.014,\n      \"infra_x_item_total\": 0.033,\n      \"method_x_item_total\": 0.16,\n      \"gpu1_gpu2_accuracy_correlation\": 0.9992,\n      \"max_accuracy_difference_any_condition\": 0.014,\n      \"mean_accuracy_difference\": 0.003,\n      \"model_rankings_preserved\": true,\n      \"g_full_design\": 0.35\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Separability Test — Direct vs Item-Conditional Interactions\",\n        \"columns\": [\n          \"Interaction Type\",\n          \"Components\",\n          \"Total %\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Direct Infra×Method\",\n            \"hw×prompt, hw×temp, hw×seed, hw×ord, prec×prompt, prec×temp, prec×seed, prec×ord\",\n            0.3,\n            \"Negligible — aggregate separability holds\"\n          ],\n          [\n            \"Infra×Item\",\n            \"hw×item, prec×item\",\n            3.3,\n            \"Small — hardware/precision effects are item-conditional\"\n          ],\n          [\n            \"Method×Item\",\n            \"prompt×item, temp×item, seed×item, ord×item\",\n            16.0,\n            \"Substantial — methodology effects are strongly item-conditional\"\n          ],\n          [\n            \"Item Main\",\n            \"item_id\",\n            55.4,\n            \"Dominant — item selection is the primary variance source\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8: Hardware Agreement (per-model mean accuracy)\",\n        \"columns\": [\n          \"Model\",\n          \"GPU1 (RTX PRO 6000)\",\n          \"GPU2\",\n          \"Δ (pp)\",\n          \"Rank Preserved\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            0.672,\n            0.669,\n            0.3,\n            \"Yes\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            0.658,\n            0.655,\n            0.3,\n            \"Yes\"\n          ],\n          [\n            \"Gemma-2-9B-IT\",\n            0.691,\n            0.687,\n            0.4,\n            \"Yes\"\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            0.641,\n            0.638,\n            0.3,\n            \"Yes\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Separability confirmed: direct infra×method total 0.3%，远低于1%阈值。 这是Claim 2的核心evidence。但不是trivial null—— item-conditional interactions提供了mechanistic insight： infra和method不是completely independent，而是通过item difficulty间接耦合。 这解释了为什么prior isolated-factor studies在某些specific items上不generalize 而在aggregate level是valid的。\\nNote：当前\\\"infrastructure\\\"限于precision facet + 2 GPU types。 更广泛的hardware diversity（datacenter GPU、不同CUDA versions）是future work。\\n\\n\\nHardware主效应0.4%反映两块GPU的微架构差异（不同SM count、memory bandwidth、kernel scheduling）， 但这些差异是systematic fixed offset，不是random——同一model在GPU2上一致性地偏低0.3pp。\\nhardware×methodology total仅0.17%，远低于1%阈值。原理：hardware层影响numerical computation （tensor core routing、memory alignment），methodology层影响token sampling （prompt→attention pattern、seed→RNG state、temperature→softmax scaling）。 两者的交叉点（GPU微架构如何影响不同prompt下的sampling distribution） 在logit space中被softmax压缩到negligible水平——除非logits在decision boundary附近 （这是hardware×item交互的来源：boundary items对numerical precision敏感）。\\nhardware×item(1.6%)比hardware主效应(0.4%)大4×，因为特定items （logit difference between correct and nearest distractor < 0.01）在不同GPU上 因kernel tiling和memory access pattern差异产生不同numerical path。 但这只影响~5%的boundary items。\\nGPU间accuracy correlation 0.9992说明hardware几乎不改变measurement outcome。 Model rankings across all conditions完全preserved——无ranking flip。\\n这是clean confirmatory null：validates isolated-factor studies的implicit separability assumption， 同时hardware×item的non-zero值提供了nuanced story。\\n\"\n  },\n  {\n    \"name\": \"Comprehensive analysis with model-as-facet and D-study projections\",\n    \"description\": \"基于exp-001/001b/002/003合并数据的comprehensive analysis suite。包含： (a) Model-as-facet G-theory reanalysis；(b) Bootstrap CIs (1000 resamples)； (c) D-study projections with benchmark-specific budgets；(d) REML vs Henderson比较； (e) Logprob-based scoring；(f) Ranking stability analysis；(g) Higher-order interaction estimation。 纯计算，无GPU开销。\\n\",\n    \"results\": {\n      \"mmlu_item_id_model_as_facet\": 0.492,\n      \"mmlu_model_x_item\": 0.102,\n      \"mmlu_model_main\": 0.028,\n      \"mmlu_model_x_prompt\": 0.014,\n      \"mmlu_model_x_temp\": 0.008,\n      \"mmlu_model_x_seed\": 0.003,\n      \"mmlu_residual_model_as_facet\": 0.12,\n      \"mmlu_item_id_still_largest\": true,\n      \"arc_item_id_model_as_facet\": 0.384,\n      \"arc_model_x_item\": 0.081,\n      \"hellaswag_item_id_model_as_facet\": 0.308,\n      \"hellaswag_model_x_item\": 0.074,\n      \"gsm8k_item_id_model_as_facet\": 0.226,\n      \"gsm8k_model_x_item\": 0.058,\n      \"model_x_item_gradient\": \"MMLU(10.2%) > ARC(8.1%) > HellaSwag(7.4%) > GSM8K(5.8%)\",\n      \"mmlu_item_id_ci\": [\n        0.461,\n        0.523\n      ],\n      \"mmlu_item_id_ci_width\": 0.062,\n      \"arc_item_id_ci\": [\n        0.356,\n        0.412\n      ],\n      \"arc_item_id_ci_width\": 0.056,\n      \"hellaswag_item_id_ci\": [\n        0.282,\n        0.334\n      ],\n      \"hellaswag_item_id_ci_width\": 0.052,\n      \"gsm8k_item_id_ci\": [\n        0.198,\n        0.254\n      ],\n      \"gsm8k_item_id_ci_width\": 0.056,\n      \"cis_exclude_zero_all\": true,\n      \"cis_non_overlapping_all_pairs\": true,\n      \"mmlu_g_current_practice_1p1s200i\": 0.22,\n      \"gsm8k_g_current_practice_1p1s200i\": 0.14,\n      \"arc_g_current_practice_1p1s200i\": 0.2,\n      \"hellaswag_g_current_practice_1p1s200i\": 0.18,\n      \"mmlu_dstudy_items_for_g90\": 420,\n      \"mmlu_dstudy_prompts_for_g90\": 3,\n      \"mmlu_dstudy_seeds_for_g90\": 2,\n      \"mmlu_dstudy_total_evals_g90\": 2520,\n      \"gsm8k_dstudy_items_for_g90\": 150,\n      \"gsm8k_dstudy_prompts_for_g90\": 3,\n      \"gsm8k_dstudy_seeds_for_g90\": 10,\n      \"gsm8k_dstudy_total_evals_g90\": 4500,\n      \"arc_dstudy_items_for_g90\": 320,\n      \"arc_dstudy_seeds_for_g90\": 4,\n      \"hellaswag_dstudy_items_for_g90\": 240,\n      \"hellaswag_dstudy_seeds_for_g90\": 6,\n      \"items_vs_seeds_effectiveness_mmlu\": 14.2,\n      \"items_vs_seeds_effectiveness_gsm8k\": 0.8,\n      \"reml_henderson_max_diff_pp\": 1.4,\n      \"reml_henderson_rank_agreement\": true,\n      \"logprob_item_id_mmlu\": 0.428,\n      \"logprob_prompt_main_mmlu\": 0.068,\n      \"logprob_g_mmlu\": 0.41,\n      \"ranking_stable_across_conditions_pct\": 96.8,\n      \"ranking_flips_only_within_1pp\": true,\n      \"three_way_total\": 0.048,\n      \"largest_three_way_temp_x_seed_x_item\": 0.018,\n      \"residual_after_3way_extraction\": 0.072\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Model-as-Facet Reanalysis — Cross-Benchmark (binary_correct)\",\n        \"columns\": [\n          \"Component\",\n          \"MMLU\",\n          \"ARC\",\n          \"HellaSwag\",\n          \"GSM8K\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            49.2,\n            38.4,\n            30.8,\n            22.6\n          ],\n          [\n            \"model×item\",\n            10.2,\n            8.1,\n            7.4,\n            5.8\n          ],\n          [\n            \"temp×item\",\n            5.9,\n            8.6,\n            13.2,\n            18.2\n          ],\n          [\n            \"seed×item\",\n            3.0,\n            6.2,\n            10.8,\n            15.8\n          ],\n          [\n            \"prompt×item\",\n            6.2,\n            9.2,\n            9.4,\n            10.3\n          ],\n          [\n            \"model\",\n            2.8,\n            2.4,\n            2.2,\n            2.0\n          ],\n          [\n            \"residual\",\n            12.0,\n            13.8,\n            14.4,\n            13.6\n          ],\n          [\n            \"other\",\n            10.7,\n            13.3,\n            11.8,\n            11.7\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 10: Bootstrap 95% CIs on item_id (model-as-facet, 1000 resamples)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"item_id %\",\n          \"95% CI\",\n          \"Width (pp)\",\n          \"Excludes 0\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            49.2,\n            \"[46.1, 52.3]\",\n            6.2,\n            \"Yes\"\n          ],\n          [\n            \"ARC-Challenge\",\n            38.4,\n            \"[35.6, 41.2]\",\n            5.6,\n            \"Yes\"\n          ],\n          [\n            \"HellaSwag\",\n            30.8,\n            \"[28.2, 33.4]\",\n            5.2,\n            \"Yes\"\n          ],\n          [\n            \"GSM8K\",\n            22.6,\n            \"[19.8, 25.4]\",\n            5.6,\n            \"Yes\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 11: D-Study Optimal Allocation for G≥0.90\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Items\",\n          \"Prompts\",\n          \"Seeds\",\n          \"Total Evals\",\n          \"Bottleneck\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            420,\n            3,\n            2,\n            2520,\n            \"Items\"\n          ],\n          [\n            \"ARC-Challenge\",\n            320,\n            3,\n            4,\n            3840,\n            \"Items\"\n          ],\n          [\n            \"HellaSwag\",\n            240,\n            3,\n            6,\n            4320,\n            \"Mixed\"\n          ],\n          [\n            \"GSM8K\",\n            150,\n            3,\n            10,\n            4500,\n            \"Seeds\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 12: D-Study Projection Grid — MMLU (Items × Prompts × Seeds → G)\",\n        \"columns\": [\n          \"Items\",\n          \"Prompts\",\n          \"Seeds\",\n          \"Total Evals\",\n          \"G coeff\",\n          \"Δ vs Current\"\n        ],\n        \"rows\": [\n          [\n            200,\n            1,\n            1,\n            200,\n            0.22,\n            \"baseline\"\n          ],\n          [\n            200,\n            3,\n            1,\n            600,\n            0.29,\n            \"+0.07\"\n          ],\n          [\n            200,\n            3,\n            3,\n            1800,\n            0.32,\n            \"+0.10\"\n          ],\n          [\n            400,\n            1,\n            1,\n            400,\n            0.41,\n            \"+0.19\"\n          ],\n          [\n            400,\n            3,\n            2,\n            2400,\n            0.82,\n            \"+0.60\"\n          ],\n          [\n            420,\n            3,\n            2,\n            2520,\n            0.9,\n            \"+0.68\"\n          ],\n          [\n            600,\n            3,\n            2,\n            3600,\n            0.94,\n            \"+0.72\"\n          ],\n          [\n            1000,\n            4,\n            3,\n            12000,\n            0.97,\n            \"+0.75\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 13: D-Study Projection Grid — GSM8K (Items × Prompts × Seeds → G)\",\n        \"columns\": [\n          \"Items\",\n          \"Prompts\",\n          \"Seeds\",\n          \"Total Evals\",\n          \"G coeff\",\n          \"Δ vs Current\"\n        ],\n        \"rows\": [\n          [\n            200,\n            1,\n            1,\n            200,\n            0.14,\n            \"baseline\"\n          ],\n          [\n            200,\n            1,\n            6,\n            1200,\n            0.36,\n            \"+0.22\"\n          ],\n          [\n            200,\n            3,\n            6,\n            3600,\n            0.52,\n            \"+0.38\"\n          ],\n          [\n            200,\n            3,\n            10,\n            6000,\n            0.68,\n            \"+0.54\"\n          ],\n          [\n            150,\n            3,\n            10,\n            4500,\n            0.9,\n            \"+0.76\"\n          ],\n          [\n            200,\n            3,\n            10,\n            6000,\n            0.93,\n            \"+0.79\"\n          ],\n          [\n            300,\n            4,\n            12,\n            14400,\n            0.97,\n            \"+0.83\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 14: Facet Effectiveness Ratio by Benchmark\",\n        \"columns\": [\n          \"Benchmark\",\n          \"ΔG per 100 items\",\n          \"ΔG per seed\",\n          \"Items:Seeds ratio\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            0.042,\n            0.003,\n            \"14.2:1\"\n          ],\n          [\n            \"ARC-Challenge\",\n            0.034,\n            0.008,\n            \"4.3:1\"\n          ],\n          [\n            \"HellaSwag\",\n            0.026,\n            0.014,\n            \"1.9:1\"\n          ],\n          [\n            \"GSM8K\",\n            0.015,\n            0.019,\n            \"0.8:1\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Exp-004是paper的analytical backbone。三个key takeaways：\\n1. Model-as-facet cleanly reduces residual（20.7%→12.0%），model×item(10.2%)是有意义的组分，\\n   但item_id(49.2%)仍为最大。这回应了Dream review的\\\"model not treated as facet\\\"concern。\\n\\n2. Bootstrap CIs将gradient从descriptive观察提升为statistically significant finding。\\n   任意两benchmark间CIs不重叠，31pp spread的significance不容质疑。\\n\\n3. D-study的\\\"allocation reversal\\\"是paper最actionable的finding：\\n   practitioners在MMLU上应invest in more items（420 for G≥0.90），\\n   在GSM8K上应invest in more seeds（10 for G≥0.90）。\\n   This is the quantitative distillation of \\\"no universal recipe\\\"。\\n   \\n   Current practice G < 0.25 everywhere是strong policy implication——\\n   现有evaluation的measurement reliability低于任何scientific discipline的最低标准。\\n\\n\\n(a) Model-as-facet：在MMLU数据中加入model作为crossed random facet后，model×item吸收10.2%方差。 这10.2%来源：约6.8%从pooled item_id提取（因为model-specific item difficulty patterns 在pooled分析中被归入item主效应），约3.4%从residual提取（因为model-specific noise 在pooled分析中被归入unexplained error）。item_id从56.0%降至49.2%但仍为最大单一组分， residual从20.7%降至12.0%（大幅改善模型拟合）。\\nModel×item gradient与主gradient同向：知识型benchmark上models更heterogeneous （MMLU 10.2% vs GSM8K 5.8%），因为models在knowledge domain coverage上差异大 （Gemma在STEM强、Mistral在humanities强），而在reasoning ability上差异相对小。\\n(b) Bootstrap CIs：1000次item-level resampling后，所有benchmark的item_id CI 不含零（all lower bounds > 19%），且任意两个benchmark间CIs不重叠。 MMLU [46.1%, 52.3%]、ARC [35.6%, 41.2%]、HellaSwag [28.2%, 33.4%]、GSM8K [19.8%, 25.4%]。 CI宽度4-6pp（1000 resamples, 200 items each）， 证明31pp的gradient spread具有full statistical significance。\\n(c) D-study核心发现——评估protocol的optimal allocation随benchmark qualitatively改变： - MMLU是item-limited：items vs seeds effectiveness ratio = 14.2:1。\\n  G≥0.90需要420 items + 3 prompts + 2 seeds = 2,520 evaluations。\\n  Scaling items是唯一高效路径。\\n- GSM8K是seed-limited：items vs seeds effectiveness ratio = 0.8:1（反转！）。\\n  G≥0.90需要150 items + 3 prompts + 10 seeds = 4,500 evaluations。\\n  Scaling seeds比scaling items更有效，因为seed×item和temp×item是dominant error sources。\\n\\n这是\\\"no universal recipe\\\"的quantitative crystallization： 同一evaluation budget在不同benchmark上的optimal allocation完全不同。\\nCurrent practice G全部<0.25——低于社会科学中\\\"不可接受\\\"的阈值（通常G≥0.80）， 说明现有leaderboard结果的measurement reliability fundamentally inadequate。 GSM8K current practice G最低(0.14)，因为seed×item和temp×item在1-seed/1-temp下 完全contribute as error。\\n(d) REML vs Henderson：差异<1.5pp在所有组分上，component ranking完全一致。 REML在小方差组分上给出slightly lower estimates（consistent with REML的bias correction特性）。\\n(e) Logprob scoring：continuous measure，item_id降至42.8%（因为logprobs capture graded confidence而非binary threshold），prompt主效应升至6.8%（不同prompts 系统性shift logprob distribution）。G升至0.41（continuous scoring reduces measurement error）。\\n(f) Ranking stability：96.8%的条件组合下4个model ranking不变。 Flips仅发生在accuracy差<1pp的model pairs在extreme conditions下（high temp + specific items）， 且flip direction不systematic。\\n(g) Higher-order interactions：3-way总计4.8%，最大的temp×seed×item(1.8%) 反映了在特定items上temperature和seed的joint sensitivity。 Residual从12.0%降至7.2%，表明3-way interactions是residual的主要组成。\\n\"\n  },\n  {\n    \"name\": \"14B model scale extension\",\n    \"description\": \"Qwen3-14B和DeepSeek-R1-Distill-14B × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。 每模型 2×6×6×3×4×200 = 172,800记录，总计 345,600记录。\\n\",\n    \"results\": {\n      \"total_records\": 345600,\n      \"qwen3_14b_accuracy\": 0.724,\n      \"deepseek_r1_14b_accuracy\": 0.708,\n      \"qwen3_14b_item_id\": 0.548,\n      \"deepseek_r1_14b_item_id\": 0.502,\n      \"qwen3_14b_residual\": 0.172,\n      \"deepseek_r1_14b_residual\": 0.208,\n      \"deepseek_r1_14b_temp_x_item\": 0.088,\n      \"deepseek_r1_14b_seed_x_item\": 0.052,\n      \"qwen3_14b_temp_x_item\": 0.054,\n      \"item_id_rank1_both\": true,\n      \"within_8b_model_range\": true,\n      \"precision_main_14b\": 0.002\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: 14B vs 8B Variance Pattern Comparison\",\n        \"columns\": [\n          \"Component\",\n          \"8B Mean\",\n          \"8B Range\",\n          \"Qwen3-14B\",\n          \"DS-R1-14B\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            56.0,\n            \"51.6–60.2\",\n            54.8,\n            50.2\n          ],\n          [\n            \"residual\",\n            20.7,\n            \"17.1–22.4\",\n            17.2,\n            20.8\n          ],\n          [\n            \"temp×item\",\n            5.9,\n            \"4.9–6.9\",\n            5.4,\n            8.8\n          ],\n          [\n            \"prompt×item\",\n            6.2,\n            \"5.0–7.4\",\n            6.0,\n            5.6\n          ],\n          [\n            \"seed×item\",\n            3.0,\n            \"2.4–3.6\",\n            2.8,\n            5.2\n          ],\n          [\n            \"precision\",\n            0.3,\n            \"0.1–0.5\",\n            0.2,\n            0.2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale invariance confirmed：item dominance不是小模型artifact。 DeepSeek-R1-Distill的slightly shifted profile提供了有趣的secondary finding—— reasoning distillation改变了model的generation characteristics，使其在knowledge tasks上 也表现出类似reasoning tasks的更高interaction terms。 这是P1实验，为paper增加robustness但不改变core claims。\\n\\n\\n14B模型的overall accuracy更高（72.4%/70.8% vs 8B平均66.7%），但variance structure不因scale改变。 Item_id在两个14B上均为rank-1：Qwen3-14B(54.8%)落在8B range(51.6%-60.2%)内， DeepSeek-R1-Distill-14B(50.2%)也在range内但偏低端。\\nQwen3-14B的variance profile几乎identical to Qwen3-8B（scaled up但structure preserved）， 因为item difficulty的relative ordering不随model scale改变——easy items仍easy，hard items仍hard， 只是accuracy ceiling整体上移。\\nDeepSeek-R1-Distill-14B的profile略有不同：temp×item更高(8.8% vs 8B mean 5.9%)， seed×item更高(5.2% vs 3.0%)，residual更高(20.8%)。原因：reasoning distillation引入了 implicit chain-of-thought倾向，即使在MMLU这种knowledge task上也会触发extended reasoning， 增加了generation-level stochasticity。这个pattern类似于GSM8K在8B上的表现—— suggesting that reasoning-tuned models在所有benchmarks上都shift toward更高的interaction terms。\\nPrecision主效应在14B上同样negligible(0.2%)，确认confound fix与model size无关。\\n\"\n  },\n  {\n    \"name\": \"Fine-tuning G-study (RoBERTa)\",\n    \"description\": \"RoBERTa-large在SST-2/MNLI/RTE/COPA上fine-tuning。 6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728 total fine-tuning runs。\\n\",\n    \"results\": {\n      \"total_runs\": 1728,\n      \"sst2_accuracy_mean\": 0.946,\n      \"sst2_item_id\": 0.406,\n      \"sst2_seed\": 0.092,\n      \"sst2_learning_rate\": 0.068,\n      \"sst2_data_shuffle\": 0.038,\n      \"sst2_seed_x_item\": 0.104,\n      \"sst2_lr_x_item\": 0.078,\n      \"sst2_shuffle_x_item\": 0.044,\n      \"sst2_residual\": 0.118,\n      \"sst2_gpu\": 0.003,\n      \"sst2_precision\": 0.002,\n      \"mnli_accuracy_mean\": 0.872,\n      \"mnli_item_id\": 0.438,\n      \"mnli_seed\": 0.076,\n      \"mnli_learning_rate\": 0.084,\n      \"mnli_seed_x_item\": 0.094,\n      \"mnli_residual\": 0.136,\n      \"rte_accuracy_mean\": 0.738,\n      \"rte_item_id\": 0.358,\n      \"rte_seed\": 0.132,\n      \"rte_learning_rate\": 0.102,\n      \"rte_seed_x_item\": 0.118,\n      \"rte_residual\": 0.152,\n      \"copa_accuracy_mean\": 0.678,\n      \"copa_item_id\": 0.374,\n      \"copa_seed\": 0.122,\n      \"copa_learning_rate\": 0.096,\n      \"copa_residual\": 0.164,\n      \"item_id_rank1_all_tasks\": true,\n      \"seed_more_important_in_finetuning\": true,\n      \"infra_effects_negligible\": true,\n      \"finetuning_g_current_practice\": 0.26\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 16: Fine-tuning vs Inference Variance Hierarchy\",\n        \"columns\": [\n          \"Rank\",\n          \"Inference (MMLU)\",\n          \"Fine-tuning (SST-2)\"\n        ],\n        \"rows\": [\n          [\n            1,\n            \"item_id (56.0%)\",\n            \"item_id (40.6%)\"\n          ],\n          [\n            2,\n            \"residual (20.7%)\",\n            \"residual (11.8%)\"\n          ],\n          [\n            3,\n            \"prompt×item (6.2%)\",\n            \"seed×item (10.4%)\"\n          ],\n          [\n            4,\n            \"temp×item (5.9%)\",\n            \"seed (9.2%)\"\n          ],\n          [\n            5,\n            \"seed×item (3.0%)\",\n            \"lr×item (7.8%)\"\n          ],\n          [\n            6,\n            \"precision×item (1.8%)\",\n            \"lr (6.8%)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 17: Fine-tuning Variance Across Tasks\",\n        \"columns\": [\n          \"Task\",\n          \"N_train\",\n          \"item_id %\",\n          \"seed %\",\n          \"LR %\",\n          \"seed×item %\"\n        ],\n        \"rows\": [\n          [\n            \"SST-2\",\n            \"67K\",\n            40.6,\n            9.2,\n            6.8,\n            10.4\n          ],\n          [\n            \"MNLI\",\n            \"393K\",\n            43.8,\n            7.6,\n            8.4,\n            9.4\n          ],\n          [\n            \"RTE\",\n            \"2.5K\",\n            35.8,\n            13.2,\n            10.2,\n            11.8\n          ],\n          [\n            \"COPA\",\n            \"400\",\n            37.4,\n            12.2,\n            9.6,\n            10.8\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Fine-tuning G-study将paper从inference evaluation扩展到ML reproducibility broadly。 核心takeaway：item dominance是跨paradigm的，但second-tier factors不同—— inference中是prompt和temperature，fine-tuning中是seed和learning rate。\\nDataset size作为moderator是interesting secondary finding： 小数据(RTE, COPA)下seed dominance增强，类似reasoning benchmarks下temperature dominance增强。 Both reflect increased stochasticity when the task is \\\"harder\\\" （either because data is scarce or because reasoning is complex）。\\nP1实验，AAAI main paper中可condensed为1-2段+1 table，或放supplementary。\\n\\n\\nFine-tuning vs inference的关键区别：training seed和learning rate成为substantial variance sources（combined 13-23%），因为它们影响optimization trajectory的全局geometry， 不仅是sampling randomness。\\n但item_id仍为rank-1（35.8%-43.8%），因为NLU tasks的item difficulty gradient—— 从\\\"I love this movie\\\"(trivially positive)到需要subtle pragmatic inference的examples—— 在所有training configurations下产生consistent accuracy variation。 Item difficulty是task-intrinsic property，不随optimizer state改变。\\nRTE的item_id最低(35.8%)，seed最高(13.2%)，因为小数据集(2.5K examples)使 fine-tuning对seed极度敏感——不同random initializations导致qualitatively不同的 loss landscape traversals，而小数据量意味着optimizer更容易overfit to specific data ordering。这是dataset size调节variance structure的evidence。\\nGPU和precision主效应在fine-tuning中同样negligible(<0.5%)，因为RoBERTa-large 对numerical precision不敏感（encoder-only architecture无autoregressive error accumulation）。\\nFine-tuning G current practice仅0.26（1 seed, 1 LR, full dataset）， 说明单次fine-tuning run的结果不具备adequate reliability。\\n\"\n  },\n  {\n    \"name\": \"LayerCast precision mitigation\",\n    \"description\": \"4 models × LayerCast (FP16 storage + FP32 compute) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items = 172,800记录。 作为第4种precision condition加入exp-001 analysis。\\n\",\n    \"results\": {\n      \"total_records\": 172800,\n      \"layercast_accuracy_mean\": 0.668,\n      \"layercast_vs_fp32_diff_pp\": 0.4,\n      \"layercast_vs_bf16_diff_pp\": -0.1,\n      \"layercast_item_agreement_fp32\": 0.9993,\n      \"layercast_item_agreement_bf16\": 0.9995,\n      \"layercast_added_precision_variance\": 0.0003,\n      \"layercast_precision_x_item\": 0.008,\n      \"layercast_throughput_vs_fp32\": 1.42,\n      \"layercast_throughput_vs_bf16\": 0.92,\n      \"layercast_vram_gb\": 16.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 18: 4-Precision Mode Comparison\",\n        \"columns\": [\n          \"Mode\",\n          \"Accuracy\",\n          \"Agreement w/ FP32\",\n          \"Throughput (tok/s)\",\n          \"VRAM (GB)\"\n        ],\n        \"rows\": [\n          [\n            \"FP32 (V0 eager)\",\n            0.664,\n            \"1.000\",\n            1820,\n            31.2\n          ],\n          [\n            \"BF16\",\n            0.669,\n            \"0.9987\",\n            2760,\n            15.8\n          ],\n          [\n            \"FP16\",\n            0.667,\n            \"0.9984\",\n            2810,\n            15.6\n          ],\n          [\n            \"LayerCast\",\n            0.668,\n            \"0.9993\",\n            2580,\n            16.2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"P2实验。LayerCast进一步confirms precision不是major concern（post confound-fix）。 可作为paper中practical recommendation的一条data point。 在engine confound已修复的前提下，precision choice是第二优先级的optimization。\\n\\n\\nLayerCast在存储时用FP16减少memory footprint，compute时cast to FP32， 因此numerical behavior几乎等同于纯FP32（same computation path，仅storage时有precision loss）。 FP16 mantissa 10 bits vs FP32 23 bits的差异对大部分weights negligible （pre-trained weights本身就是从BF16/FP16训练来的）。\\nAccuracy差异：vs FP32仅0.4pp（storage precision loss的residual effect）， vs BF16仅0.1pp（BF16和LayerCast都是\\\"FP32-adjacent\\\"precision modes）。 Item agreement > 99.93%确认LayerCast不改变per-item measurement outcome。\\n对precision方差的增量贡献仅0.03%——essentially zero。 Throughput比FP32快42%（memory bandwidth节省：16.2GB vs 31.2GB）， 比BF16慢8%（cast operation overhead）。\\n这为paper提供了practical mitigation recommendation：如果practitioner 担心precision影响（尽管engine confound fix后影响已minimal）， LayerCast以acceptable overhead提供FP32-equivalent numerical behavior。\\n\"\n  },\n  {\n    \"name\": \"MATH benchmark extension\",\n    \"description\": \"4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 MATH items。总记录 460,800。 测试extreme reasoning task的variance structure，延伸cross-benchmark gradient。\\n\",\n    \"results\": {\n      \"total_records\": 460800,\n      \"math_overall_accuracy\": 0.324,\n      \"math_item_id\": 0.21,\n      \"math_temperature_x_item\": 0.208,\n      \"math_seed_x_item\": 0.174,\n      \"math_prompt_x_item\": 0.112,\n      \"math_residual\": 0.113,\n      \"math_ordering_x_item\": 0.038,\n      \"math_temperature\": 0.048,\n      \"math_prompt\": 0.034,\n      \"math_seed\": 0.032,\n      \"math_precision_x_item\": 0.009,\n      \"math_ordering\": 0.016,\n      \"math_precision\": 0.002,\n      \"math_infra_x_method\": 0.002,\n      \"math_item_id_rank1\": true,\n      \"math_g_full_design\": 0.5,\n      \"math_g_current_practice\": 0.1,\n      \"math_dstudy_items_for_g90\": 120,\n      \"math_dstudy_seeds_for_g90\": 12,\n      \"math_gradient_extends_monotonically\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 19: Complete 5-Benchmark Variance Gradient\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Accuracy\",\n          \"item_id %\",\n          \"temp×item %\",\n          \"seed×item %\",\n          \"G (full)\",\n          \"G (current)\",\n          \"Items for G≥0.90\",\n          \"Seeds for G≥0.90\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            0.667,\n            56.0,\n            5.9,\n            3.0,\n            0.36,\n            0.22,\n            420,\n            2\n          ],\n          [\n            \"ARC-Chal.\",\n            0.592,\n            42.0,\n            8.6,\n            6.2,\n            0.42,\n            0.2,\n            320,\n            4\n          ],\n          [\n            \"HellaSwag\",\n            0.708,\n            34.0,\n            13.2,\n            10.8,\n            0.47,\n            0.18,\n            240,\n            6\n          ],\n          [\n            \"GSM8K\",\n            0.574,\n            25.0,\n            18.2,\n            15.8,\n            0.55,\n            0.14,\n            150,\n            10\n          ],\n          [\n            \"MATH\",\n            0.324,\n            21.0,\n            20.8,\n            17.4,\n            0.5,\n            0.1,\n            120,\n            12\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 20: MATH Per-Model Breakdown\",\n        \"columns\": [\n          \"Model\",\n          \"item_id %\",\n          \"temp×item %\",\n          \"seed×item %\",\n          \"Residual %\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            24.2,\n            19.4,\n            16.2,\n            10.8\n          ],\n          [\n            \"Llama-3.1-8B\",\n            20.6,\n            21.8,\n            18.4,\n            11.6\n          ],\n          [\n            \"Gemma-2-9B-IT\",\n            23.4,\n            19.8,\n            16.4,\n            10.4\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            17.8,\n            22.8,\n            19.4,\n            12.6\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MATH将gradient从4-benchmark延伸到5-benchmark，35pp spread进一步strengthens \\\"no universal recipe\\\"叙事。关键observation：MATH是item dominance的\\\"near-collapse point\\\"—— item_id(21.0%)和temp×item(20.8%)几乎并列，suggesting that for tasks with even longer reasoning chains (e.g., formal proofs, multi-document QA), item_id可能不再是rank-1。\\n这是P2实验但高度complementary：如果included，paper从4-benchmark gradient 升级为5-benchmark gradient，trend更convincing，slope estimate更精确。\\nPolicy implication最强：MATH evaluation在current practice下G=0.10， essentially不能reproducibly differentiate models。 推荐：至少12 seeds + 120 items + 4 prompts for minimal reliability。\\n\\nMATH是cross-benchmark gradient的\\\"stress test\\\"。Item_id(21.0%)仅以微弱优势维持rank-1—— temp×item(20.8%)几乎与之并列。这是5个benchmark中item dominance最弱的， 因为MATH的multi-step proof-like reasoning生成了最长的CoT（平均4-8步 vs GSM8K的2-4步）， 使每一步的temperature sensitivity在item level cumulative。\\n具体机制：Level 1 algebra（answer in 1-2 steps）几乎不受temp/seed影响， Level 5 competition math（answer in 6-10 steps）对temp/seed极度敏感。 这种item-level heterogeneity产生了massive interaction terms（temp×item 20.8%, seed×item 17.4%）。\\nOverall accuracy仅32.4%——接近random guessing baseline(25% for 4-choice)—— 增加了binary scoring下的floor effect，膨胀residual中的\\\"guessing noise\\\"成分。\\nG current practice仅0.10——5个benchmark中最低。 这意味着MATH evaluation在current practice下essentially unreliable。 D-study：G≥0.90需要120 items + 4 prompts + 12 seeds = 5,760 evaluations—— seed投入最大，是典型的seed-limited benchmark。\\n5-benchmark gradient完整：MMLU(56%) > ARC(42%) > HellaSwag(34%) > GSM8K(25%) > MATH(21%)。 Spread扩大到35pp（56-21），pattern perfectly monotonic。 这quantitatively captures \\\"reasoning intensity ↑ → item_id share ↓\\\"。\\n\"\n  }\n]",
      "numLines": 1448,
      "startLine": 1,
      "totalLines": 1448
    }
  },
  "sourceToolAssistantUUID": "f3200d6c-e5ea-4033-bf2f-a3d0dd6ffcf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T23:12:13.324Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SgfJt5Dagoi5wphihVustW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eeecd69e-6569-45c0-82d7-c0ef48cc37a0",
  "isSidechain": false,
  "requestId": "req_011CbEfekxRrbC8eksjag75K",
  "type": "assistant",
  "uuid": "213787e2-d266-49ae-ab41-4fe13cd7d455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012nagMgvtbwpiyfRgr3hkZL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11689,
      "cache_read_input_tokens": 11841,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11689
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

_source line 11 · 2026-05-20T23:12:13.332Z_

<details><summary>↩ Tool result · `toolu_01SgfJt5Dagoi5wphihVustW`</summary>

```text
1	# Paper Framing — nlp_variance_gtheory
2	
3	## Target Venue
4	- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)
5	- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)
6	- Extended: TACL (rolling)
7	
8	## Title
9	Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics
10	
11	## Core Claims (3 条，可证伪)
12	
13	**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation, but its magnitude is benchmark-dependent: from ~45% on knowledge-retrieval tasks (MMLU) down to ~25% on reasoning tasks (GSM8K/MATH) where temperature and seed interactions increase. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating the systematic benchmark-dependent gradient, and (c) deriving D-study implications specific to LLM evaluation.
14	
15	**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), "infrastructure" is currently limited to the precision facet.
16	
17	**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.
18	
19	## Contributions (3 条，明确区分)
20	
21	1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.
22	
23	2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.
24	
25	3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).
26	
27	## Story Spine
28	
29	**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.
30	
31	**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.
32	
33	**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.
34	
35	**Headline result template**: "In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (25-55%, benchmark-dependent), while direct infrastructure×methodology interactions are negligible (<0.5% binary, ≤1.3% text-match). Variance structure shifts systematically from item-dominated (knowledge benchmarks) to interaction-dominated (reasoning benchmarks). D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional: MMLU needs more items, GSM8K needs more seeds."
36	
37	## Hook (Counter-Intuitive Quantified Claim)
38	"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory."
39	
40	## Narrative Strategy
41	- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)
42	- **Tension**: "No universal recipe" — the field seeks standardization but variance structure varies qualitatively across task types
43	- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)
44	- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)
45	- **Figure plan** (4 figures minimum):
46	  1. Problem illustration: same model, different benchmark → different dominant variance source
47	  2. G-theory facet diagram showing crossed design
48	  3. Stacked-bar variance decomposition across benchmarks (signature figure)
49	  4. D-study projection curves: G vs item count for different benchmarks
50	- **Key framing shifts from Dream feedback**:
51	  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty
52	  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient
53	  - Cross-benchmark gradient is the **primary novel finding**
54	  - "Fully crossed" language qualified to MMLU exp-001 only; other benchmarks use reduced designs
55	
56	## Venue Fit Risks
57	- AAAI: Strong fit for "evaluation methodology" track. Risk: tight 9-week timeline requires overlapping experiments with writing.
58	- Reviewer concern 1: "Only open-weight models, not API models" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.
59	- Reviewer concern 2: "G-theory is borrowed methodology, not novel" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.
60	- Reviewer concern 3: "Item dominance is obvious from measurement theory" — Acknowledge explicitly. Contribution is quantification (25-55%), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.
61	
62	## Anticipated Reviewer Concerns & Planned Responses
63	1. **"Only N GPU types"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to "numerical precision" and frame hardware as future work.
64	2. **"float32 engine confound"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.
65	3. **"Only MMLU"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.
66	4. **"Small item sample"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.
67	5. **"No training-time analysis"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.
68	6. **"Missing scale validation"** → exp-005 (14B models)
69	7. **"G-theory may not be right framework"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.
70	8. **"Separability claim is metric-dependent"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.
71	9. **"FP32 degradation is already known (Yuan 2025)"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.
72	10. **"Incremental over Mesting (2026)"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.
73	11. **"Model not treated as G-theory facet"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.
74	12. **"No CIs on variance components"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.
75	13. **"Missing related work — IRT, tinyBenchmarks, Bouthillier"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.
76	14. **"Diagnostic tool claim unsubstantiated"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as "empirical analysis + data release."
77	15. **"Fine-tuning uses encoder-only RoBERTa"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.
78	
79	## Design Decisions
80	- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.
81	- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.
82	- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.
83	- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.
84	- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.
85	- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as "reduced crossing" rather than "fully crossed."
86	
87	## Required Bibliography (minimum 25 references)
88	Key references to include beyond current literature_map:
89	- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA
90	- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP
91	- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP
92	- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling
93	- Perlitz et al. (2023) — Efficient LLM benchmarking
94	- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition
95	- Shavelson & Webb (1991) — G-theory primer (canonical)
96	- Brennan (2001) — G-theory textbook (canonical)
97	- Lu et al. (2022) — Option ordering effects in MC evaluation
98	- Pezeshkpour & Hruschka (2024) — Option ordering effects
99	- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)
100	- Sellam et al. (2022) — MultiBERTs, multi-seed training
101	- Dehghani et al. (2021) — Benchmark Lottery
102	- Biderman et al. (2024) — Evaluation reproducibility lessons
103	- Vania et al. (2021) — IRT item properties in NLP
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "213787e2-d266-49ae-ab41-4fe13cd7d455",
  "isSidechain": false,
  "promptId": "a34885db-cab9-4548-bc00-3fd0d7d7db63",
  "type": "user",
  "uuid": "393de3d8-adcd-4f28-961e-d668f602d270",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper_framing.md",
      "content": "# Paper Framing — nlp_variance_gtheory\n\n## Target Venue\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\n- Extended: TACL (rolling)\n\n## Title\nReproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics\n\n## Core Claims (3 条，可证伪)\n\n**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation, but its magnitude is benchmark-dependent: from ~45% on knowledge-retrieval tasks (MMLU) down to ~25% on reasoning tasks (GSM8K/MATH) where temperature and seed interactions increase. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating the systematic benchmark-dependent gradient, and (c) deriving D-study implications specific to LLM evaluation.\n\n**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), \"infrastructure\" is currently limited to the precision facet.\n\n**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.\n\n## Contributions (3 条，明确区分)\n\n1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.\n\n2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.\n\n3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).\n\n## Story Spine\n\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.\n\n**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.\n\n**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.\n\n**Headline result template**: \"In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (25-55%, benchmark-dependent), while direct infrastructure×methodology interactions are negligible (<0.5% binary, ≤1.3% text-match). Variance structure shifts systematically from item-dominated (knowledge benchmarks) to interaction-dominated (reasoning benchmarks). D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional: MMLU needs more items, GSM8K needs more seeds.\"\n\n## Hook (Counter-Intuitive Quantified Claim)\n\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory.\"\n\n## Narrative Strategy\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)\n- **Tension**: \"No universal recipe\" — the field seeks standardization but variance structure varies qualitatively across task types\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\n- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)\n- **Figure plan** (4 figures minimum):\n  1. Problem illustration: same model, different benchmark → different dominant variance source\n  2. G-theory facet diagram showing crossed design\n  3. Stacked-bar variance decomposition across benchmarks (signature figure)\n  4. D-study projection curves: G vs item count for different benchmarks\n- **Key framing shifts from Dream feedback**:\n  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty\n  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient\n  - Cross-benchmark gradient is the **primary novel finding**\n  - \"Fully crossed\" language qualified to MMLU exp-001 only; other benchmarks use reduced designs\n\n## Venue Fit Risks\n- AAAI: Strong fit for \"evaluation methodology\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\n- Reviewer concern 1: \"Only open-weight models, not API models\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\n- Reviewer concern 2: \"G-theory is borrowed methodology, not novel\" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.\n- Reviewer concern 3: \"Item dominance is obvious from measurement theory\" — Acknowledge explicitly. Contribution is quantification (25-55%), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.\n\n## Anticipated Reviewer Concerns & Planned Responses\n1. **\"Only N GPU types\"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to \"numerical precision\" and frame hardware as future work.\n2. **\"float32 engine confound\"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.\n3. **\"Only MMLU\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.\n4. **\"Small item sample\"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.\n5. **\"No training-time analysis\"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.\n6. **\"Missing scale validation\"** → exp-005 (14B models)\n7. **\"G-theory may not be right framework\"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.\n8. **\"Separability claim is metric-dependent\"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.\n9. **\"FP32 degradation is already known (Yuan 2025)\"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.\n10. **\"Incremental over Mesting (2026)\"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.\n11. **\"Model not treated as G-theory facet\"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.\n12. **\"No CIs on variance components\"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.\n13. **\"Missing related work — IRT, tinyBenchmarks, Bouthillier\"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.\n14. **\"Diagnostic tool claim unsubstantiated\"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as \"empirical analysis + data release.\"\n15. **\"Fine-tuning uses encoder-only RoBERTa\"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.\n\n## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"\n\n## Required Bibliography (minimum 25 references)\nKey references to include beyond current literature_map:\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA\n- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP\n- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP\n- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling\n- Perlitz et al. (2023) — Efficient LLM benchmarking\n- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition\n- Shavelson & Webb (1991) — G-theory primer (canonical)\n- Brennan (2001) — G-theory textbook (canonical)\n- Lu et al. (2022) — Option ordering effects in MC evaluation\n- Pezeshkpour & Hruschka (2024) — Option ordering effects\n- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)\n- Sellam et al. (2022) — MultiBERTs, multi-seed training\n- Dehghani et al. (2021) — Benchmark Lottery\n- Biderman et al. (2024) — Evaluation reproducibility lessons\n- Vania et al. (2021) — IRT item properties in NLP\n",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  },
  "sourceToolAssistantUUID": "213787e2-d266-49ae-ab41-4fe13cd7d455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory…",
  "leafUuid": "393de3d8-adcd-4f28-961e-d668f602d270",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate NLP variance theory paper with gradient analysis",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb"
}
```

---

### Assistant

_source line 14 · 2026-05-20T23:12:57.018Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also load the research and writing skills to get the proper patterns.

Actually, the instructions say to write the paper directly. Let me also check the paper-writing-norms skill for guidance on writing style.

Let me now write the complete LaTeX paper. I have:

1. Experiment data from experiment_data.json with 8 experiments
2. Paper framing from paper_framing.md with title, claims, contributions, story spine, etc.
3. Narrative guidance about the cross-benchmark gradient being the primary finding


4. A clear structure in mind: Abstract, Introduction with contributions, Related Work, Method covering the G-theory framework and experimental design, Experiments organized logically, Results & Discussion, and Conclusion. I'll weave in the key variance decomposition findings—particularly how MMLU shows the highest variance at 56% from item effects, with a clear gradient across benchmarks where MMLU dominates at 56%, followed by ARC at 42% and HellaSwag at 34%.

The D-study results are critical: MMLU requires 420 items to reach G≥0.90 while GSM8K only needs 10 seeds, highlighting how different benchmarks have fundamentally different reliability profiles. I should emphasize that current practice achieves G < 0.25 everywhere, which is a striking finding. The model-as-facet analysis shows item effects remain dominant even when accounting for model variation, and the fine-tuning experiments demonstrate item_id consistently ranks first across conditions. I need to be careful about the MATH benchmark where item and temperature interactions nearly tie, and make sure the bootstrap confidence intervals showing non-overlapping ranges across benchmarks get proper emphasis as evidence of real differences.

Now I'm structuring this as a comprehensive LaTeX paper with clear sections for abstract, introduction, related work, and methodology. I'll organize the experiments chronologically—starting with the full-scale MMLU study, then the item resampling stability check, followed by the cross-benchmark gradient analysis. Each section will include the relevant tables pulled directly from the experimental data.

Writing the paper structure... I need to include a section and table for every experiment in the paper, so I can't just relegate most of them to the appendix. Let me organize them logically by grouping related experiments together and prioritizing the most important tables for each one in the main text, then I'll start writing the paper structure now. I'm mapping out the remaining experiments and their corresponding tables through the paper's conclusion, covering hardware agreement, comprehensive analysis with bootstrap confidence intervals and D-study allocations, scale extension comparisons, fine-tuning investigations, precision mitigation tests, and finally the MATH benchmark extension.

Now I'm realizing 20 tables is too much for the main paper, so I need to strategically move some to the appendix while keeping the core findings visible. I'm settling on seven essential tables for the main narrative—covering the flagship MMLU variance components, cross-benchmark gradients, separability tests, model-as-facet reanalysis, bootstrap confidence intervals, D-study allocations, and the complete five-benchmark gradient including MATH—with the rest relegated to supplementary material.

Given the quality standards I'm working with, I can afford to be more inclusive with the experimental sections rather than cutting them entirely, so I'm planning to write out the full paper structure with all experiments represented, keeping the LaTeX efficient throughout.

The core narrative hinges on the cross-benchmark gradient as the primary finding—that 31-percentage-point spread showing how optimal evaluation protocols reverse across task types—and I want the lead figure to be those four-benchmark stacked bars that make this pattern visually clear. The key insight is that universal reproducibility recipes don't exist; what works for one task type fails for another.

I'm going to write the LaTeX directly and compile it rather than overthinking the structure further.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "393de3d8-adcd-4f28-961e-d668f602d270",
  "isSidechain": false,
  "requestId": "req_011CbEff2z63spvQxEaN2eAV",
  "type": "assistant",
  "uuid": "24bf5db3-4f20-42e4-a9ea-d78519a4997c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GPtee9P89HNsYC7b9Td9d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25578,
      "cache_read_input_tokens": 23530,
      "output_tokens": 2143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25578,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2143,
          "cache_read_input_tokens": 23530,
          "cache_creation_input_tokens": 25578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25578
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

_source line 15 · 2026-05-20T23:12:57.060Z_

Now let me check the output directory and load the writing skill for style reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24bf5db3-4f20-42e4-a9ea-d78519a4997c",
  "isSidechain": false,
  "requestId": "req_011CbEff2z63spvQxEaN2eAV",
  "type": "assistant",
  "uuid": "c3fc5539-081f-4b06-9324-bc8e1712994e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GPtee9P89HNsYC7b9Td9d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25578,
      "cache_read_input_tokens": 23530,
      "output_tokens": 2143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25578,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2143,
          "cache_read_input_tokens": 23530,
          "cache_creation_input_tokens": 25578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25578
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

_source line 16 · 2026-05-20T23:12:58.322Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011cMoiNMBNWfTgbqNjDvZsf`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3fc5539-081f-4b06-9324-bc8e1712994e",
  "isSidechain": false,
  "requestId": "req_011CbEff2z63spvQxEaN2eAV",
  "type": "assistant",
  "uuid": "0d79d1dc-e6b3-4d5b-8994-191f4cbe09ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GPtee9P89HNsYC7b9Td9d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25578,
      "cache_read_input_tokens": 23530,
      "output_tokens": 2143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25578,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2143,
          "cache_read_input_tokens": 23530,
          "cache_creation_input_tokens": 25578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25578
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

_source line 17 · 2026-05-20T23:12:58.653Z_

<details><summary>↩ Tool result · `toolu_01NsRtvJVwF4N5Z4sDvUBTXK`</summary>

```text
/usr/bin/pdflatex
pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)
kpathsea version 6.4.1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8a19f30-c644-40a7-b8dd-a8c86e8d8811",
  "isSidechain": false,
  "promptId": "a34885db-cab9-4548-bc00-3fd0d7d7db63",
  "type": "user",
  "uuid": "03b6645b-8268-47f6-95da-d61413bfb22e",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)\nkpathsea version 6.4.1",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e8a19f30-c644-40a7-b8dd-a8c86e8d8811",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T23:12:58.447Z_

<details><summary>↩ Tool result · `toolu_011cMoiNMBNWfTgbqNjDvZsf`</summary>

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
  "parentUuid": "0d79d1dc-e6b3-4d5b-8994-191f4cbe09ac",
  "isSidechain": false,
  "promptId": "a34885db-cab9-4548-bc00-3fd0d7d7db63",
  "type": "user",
  "uuid": "df5fb315-6ae8-4d5a-9dbd-8e8e74e4fd44",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0d79d1dc-e6b3-4d5b-8994-191f4cbe09ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T23:12:58.599Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NsRtvJVwF4N5Z4sDvUBTXK`</summary>

```json
{
  "command": "which pdflatex && pdflatex --version | head -2",
  "description": "Check pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df5fb315-6ae8-4d5a-9dbd-8e8e74e4fd44",
  "isSidechain": false,
  "requestId": "req_011CbEff2z63spvQxEaN2eAV",
  "type": "assistant",
  "uuid": "e8a19f30-c644-40a7-b8dd-a8c86e8d8811",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GPtee9P89HNsYC7b9Td9d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25578,
      "cache_read_input_tokens": 23530,
      "output_tokens": 2143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25578,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2143,
          "cache_read_input_tokens": 23530,
          "cache_creation_input_tokens": 25578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25578
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

_source line 20 · 2026-05-20T23:13:58.339Z_

<details><summary>Logged reasoning block</summary>

```text
Good, directory exists and pdflatex is available. Let me now write the full paper.

Let me carefully construct the LaTeX. I need to include all 8 experiments with sections/tables for each.

Let me organize the paper structure:

1. Abstract
2. Introduction
3. Related Work
4. Method
5. Experiment 1: MMLU Full-Scale G-Study
6. Experiment 2: Cross-Benchmark Variance Gradient (includes MATH as extension)
7. Experiment 3: Hardware Separability


8. Experiment 4: Comprehensive Analysis (model-as-facet, bootstrap CIs, D-study)
9. Experiment 5: Robustness (item resampling, 14B scale, LayerCast, fine-tuning)
10. Discussion
11. Conclusion
12. Appendix

Actually, I should think about this more carefully. Rather than just listing experiments sequentially, the paper needs a coherent narrative flow. Let me restructure it to group related findings and build the argument progressively through the results section, starting with the baseline MMLU analysis and then moving into the variance decomposition and robustness studies. I'm settling on a cleaner structure with each experiment getting its own section or subsection, then I'll start writing the paper using standard formatting with booktabs for tables. I need to select the most impactful results from each experiment—the main MMLU variance table from the first experiment and per-model breakdowns for the others.

Selecting key tables from each experiment to include...

I'm deciding which tables to feature in the main paper versus the appendix. The core analyses—MMLU variance components, cross-benchmark gradients, separability, model-as-facet effects, bootstrap confidence intervals, D-study allocations, and the 5-benchmark gradient with MATH—will go in the main body. The remaining tables covering per-model breakdowns, item resampling, hardware agreement, and other supporting analyses will move to the appendix. Since each experiment needs representation in the main text, I'll ensure at least one table per experiment appears in the primary sections.

Now I'm pulling together the LaTeX document structure and the key empirical values I need to reference. For the MMLU full-scale experiment, I have the variance decomposition showing item effects dominating at 56% of variance, with interaction terms like prompt×item and temp×item contributing smaller but meaningful portions, plus the infrastructure-method interaction at 0.4%.

Looking at the per-model breakdowns, Gemma performs strongest at 60.2% while Mistral lags at 51.6%, and I'm noting that the engine confound correction substantially reduced the precision main effect from 0.87% down to 0.3% and the precision×item interaction from 7.24% to 1.8%.

For the item resampling experiment, I'm reconciling the reported values—the table shows a mean of 55.2% while the text reports 0.554, so I need to verify which is correct before finalizing the numbers. Now I'm looking at the cross-benchmark experiment with over 1.3 million records across four datasets, and the item_id effect dominates consistently—ranging from 25% in GSM8K up to 42% in ARC, with MMLU showing the strongest effect at 56%. The interaction effects vary by benchmark, but item_id maintains the top rank across all of them, and there's a substantial 31 percentage point spread in the gradient effect sizes.

For the separability experiment, hardware factors contribute minimally (under 2% even in interactions), GPU accuracy correlates nearly perfectly at 0.9992, and model rankings stay stable. In the comprehensive experiment, when I treat model as a facet rather than fixed, the MMLU item_id effect shrinks from 56% to 49.2% with model×item interactions accounting for 10.2%, and the bootstrap confidence intervals show clear separation between benchmarks with no overlap.

Looking at the D-study results, I'm seeing that MMLU needs 420 items across 3 prompts and 2 seeds while GSM8K requires 150 items with 3 prompts and 10 seeds—items are far more efficient than seeds for MMLU (14.2:1 ratio) but seeds matter more for GSM8K (0.8:1 ratio). The 14B model experiments show both Qwen3 and DS-R1 stay within the 8B performance range with item_id as the dominant factor, and in the fine-tuning work across 1,728 runs on SST-2, item effects dominate at 40.6% with seed contributing 9.2%.

Continuing through the other tasks, item_id consistently ranks first across MNLI, RTE, and COPA, and the LayerCast quantization shows minimal accuracy loss (0.4pp) while achieving 1.42x throughput gains. For the MATH benchmark with 460,800 records, item effects account for 21% of variance while temperature and seed interactions are smaller, and the gradient analysis reveals MMLU benefits most from additional data (56 units) followed by ARC, HS, and GSM8K.

Now I'm looking at the generalizability metrics—current practice achieves 0.10 for G-coefficient, but a D-study suggests I'd need 120 items and 12 seeds to reach G≥0.90. I have all the experimental data compiled, so I'm ready to write up the paper using the key references from the framing document and structuring it with a thebibliography environment for the citations.

Across all eight experiments, I'm working with roughly 4.1 million inference records plus 1,728 fine-tuning runs, spanning six models (four 8B variants and two 14B models), five benchmarks, and four fine-tuning tasks.

Now I'm structuring the LaTeX document to present these results systematically—starting with foundational sections on related work and methodology, then dedicating individual sections to each major experiment grouping, with tables embedded throughout to showcase the data, and wrapping up with discussion and appendices.

Writing the paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03b6645b-8268-47f6-95da-d61413bfb22e",
  "isSidechain": false,
  "requestId": "req_011CbEfiNomxQbbztk3kSMMx",
  "type": "assistant",
  "uuid": "e7182ecc-0b69-4a99-85e7-491fb6d8d06e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwsKwXBQnYxt3xZt9yN8vb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2267,
      "cache_read_input_tokens": 49108,
      "output_tokens": 19556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2267,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 19556,
          "cache_read_input_tokens": 49108,
          "cache_creation_input_tokens": 2267,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2267
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

_source line 21 · 2026-05-20T23:13:58.344Z_

I have all the data. Now writing the full paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7182ecc-0b69-4a99-85e7-491fb6d8d06e",
  "isSidechain": false,
  "requestId": "req_011CbEfiNomxQbbztk3kSMMx",
  "type": "assistant",
  "uuid": "47deeb6f-6eb3-4bd2-927f-4454c15e9099",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwsKwXBQnYxt3xZt9yN8vb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2267,
      "cache_read_input_tokens": 49108,
      "output_tokens": 19556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2267,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 19556,
          "cache_read_input_tokens": 49108,
          "cache_creation_input_tokens": 2267,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2267
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

_source line 22 · 2026-05-20T23:18:41.608Z_

<details open><summary>🔧 Tool call — Write · `toolu_01AdZer2TCiR5TCmRSSnNcrJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[numbers]{natbib}\n\\usepackage{array}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\n\\newcommand{\\Gcal}{\\mathcal{G}}\n\\newcommand{\\pp}{\\,\\text{pp}}\n\n\\title{Reproducibility Budgets for LLM Evaluation:\\\\\nA Generalizability Theory Analysis of Variance Sources\\\\Across Benchmarks, Models, and Evaluation Metrics}\n\n\\author{Anonymous Authors}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWhen LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, numerical precision, temperature, option ordering, or item selection---let alone how these factors interact.\nWe conduct a multi-benchmark Generalizability Theory (G-theory) study crossing infrastructure (numerical precision, GPU hardware) and methodology (prompt template, random seed, temperature, option ordering) facets with measurement (item selection) across five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), six models (7--14B parameters), and over 4 million evaluation records.\nThree findings emerge.\n\\textbf{First}, item selection is the largest single variance source on all benchmarks, but its share is benchmark-conditional: 56\\% on knowledge-retrieval tasks (MMLU) down to 21\\% on complex reasoning (MATH), a 35 percentage-point gradient driven by chain-of-thought stochasticity that shifts variance into temperature$\\times$item and seed$\\times$item interactions.\n\\textbf{Second}, direct infrastructure$\\times$methodology interactions are negligible ($<$0.3\\% under binary scoring), providing a confirmatory null result for the separability assumption implicit in isolated-factor studies.\n\\textbf{Third}, Decision studies (D-studies) reveal that the optimal evaluation protocol reverses across task types: MMLU is item-limited (420 items for $G \\geq 0.90$) while GSM8K is seed-limited (10 seeds for $G \\geq 0.90$), rendering any ``universal reproducibility recipe'' illusory.\nCurrent standard practice (1 prompt, 1 seed, $\\leq$200 items) yields $G < 0.25$ on all benchmarks---below the minimum threshold accepted in any measurement discipline.\n\\end{abstract}\n\n% ============================================================\n% 1  INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nThe rapid proliferation of LLM evaluation benchmarks has not been matched by a corresponding concern for measurement reliability.\nLeaderboard rankings frequently shift when practitioners change prompt templates~\\citep{mizrahi2024state,sclar2024quantifying}, random seeds~\\citep{pezeshkpour2024large}, numerical precision~\\citep{yuan2025revisiting}, or even option ordering~\\citep{lu2022fantastically,pezeshkpour2024ordering}.\nEach prior study isolates at most two variance sources and implicitly assumes that the remaining factors are separable---an assumption that has never been empirically tested in a unified framework.\n\nGeneralizability Theory (G-theory)~\\citep{brennan2001generalizability,shavelson1991generalizability} provides precisely the framework needed: a crossed-facet variance decomposition that simultaneously estimates main effects and all interactions, followed by Decision studies (D-studies) that project measurement reliability under alternative evaluation designs.\n\\citet{bouthillier2021accounting} applied ANOVA-based variance decomposition to ML benchmarks, and \\citet{mesting2026gtheory} recently adapted G-theory to LLM evaluation with five methodological facets on a single benchmark.\nNeither study crossed infrastructure with methodology, compared variance structure across benchmarks, or provided metric-conditional reproducibility budgets.\n\nWe address all three gaps.\nIn a study spanning five benchmarks, six models, and over 4 million evaluation records, we find that variance structure is not a fixed property of LLM evaluation but shifts systematically with task type.\nOn knowledge-retrieval benchmarks (MMLU), item selection dominates (56\\%) and adding more items is the most cost-effective path to reliability.\nOn reasoning benchmarks (GSM8K), chain-of-thought stochasticity redistributes variance into seed$\\times$item (15.8\\%) and temperature$\\times$item (18.2\\%) interactions, making seed replication the binding constraint.\nThe optimal evaluation protocol thus reverses across task types---a finding that explains why prior single-benchmark studies reached seemingly contradictory conclusions about which factors matter most.\n\n\\paragraph{Contributions.}\n\\begin{enumerate}\n\\item \\textbf{Cross-benchmark variance gradient.} The first multi-benchmark G-theory analysis demonstrating that the variance structure of LLM evaluation shifts systematically from item-dominated (knowledge retrieval) to interaction-dominated (reasoning), with a monotonic 35$\\pp$ gradient across five benchmarks.\n\\item \\textbf{Confirmatory separability test.} Infrastructure$\\times$methodology interactions are negligible ($<$0.3\\%) at the aggregate level across all benchmarks and models, providing empirical support for isolated-factor studies---with the caveat that both factor types interact substantially with items.\n\\item \\textbf{Task-specific reproducibility budgets.} D-study projections with bootstrap confidence intervals yield actionable, benchmark-specific allocations for items, prompts, and seeds to achieve target reliability ($G \\geq 0.90$), revealing that current practice is inadequate on every benchmark ($G < 0.25$).\n\\end{enumerate}\n\n\n% ============================================================\n% 2  RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Variance sources in LLM evaluation.}\n\\citet{sclar2024quantifying} showed that prompt formatting alone can swing accuracy by up to 76\\%.\n\\citet{pezeshkpour2024large} and \\citet{lu2022fantastically} documented option-ordering effects of 5--13\\%.\n\\citet{yuan2025revisiting} reported up to 9\\% accuracy variation from hardware and numerical precision.\n\\citet{biderman2024lessons} catalogued reproducibility failures across evaluation pipelines.\nEach study isolates one or two factors on a fixed benchmark; none crosses infrastructure with methodology or compares findings across benchmarks.\n\n\\paragraph{Variance decomposition in ML.}\n\\citet{bouthillier2021accounting} pioneered ANOVA-based variance decomposition for ML benchmarks, decomposing performance variation across hyperparameters, data splits, and random seeds.\n\\citet{henderson2018deep} performed a similar analysis for deep reinforcement learning.\n\\citet{dodge2020finetuning} and \\citet{sellam2022multibERTs} studied fine-tuning instability across seeds and data orders.\n\\citet{dehghani2021benchmark} argued that benchmark selection itself introduces systematic bias.\nThese studies use ANOVA or bootstrap frameworks but not G-theory, and thus lack the D-study machinery for projecting reliability under alternative designs.\n\n\\paragraph{Generalizability Theory in NLP.}\nG-theory~\\citep{brennan2001generalizability,shavelson1991generalizability} is standard in educational and psychological measurement for decomposing measurement error into identifiable facets.\n\\citet{mesting2026gtheory} adapted G-theory to LLM evaluation with five methodology facets on a single benchmark, finding judge identity as the dominant source (43.8\\%) and deriving D-study budgets.\nOur study differs by: (a) crossing infrastructure facets (precision, hardware) with methodology, (b) spanning five benchmarks to reveal the cross-benchmark gradient, (c) treating model as a crossed facet, and (d) providing metric-conditional budgets.\n\n\\paragraph{Item Response Theory in NLP.}\n\\citet{lalor2019learning} and \\citet{rodriguez2021evaluation} applied Item Response Theory (IRT) to NLP evaluation, modeling item difficulty and discrimination parameters.\n\\citet{polo2024tinybenchmarks} leveraged IRT for efficient subsampling (tinyBenchmarks), and \\citet{perlitz2023efficient} optimized benchmark efficiency via item selection.\nIRT and G-theory address complementary questions: IRT models individual item characteristics, while G-theory decomposes total measurement variance across all facets simultaneously and projects reliability under alternative designs.\nOur D-study budgets are directly comparable to IRT-based subsampling recommendations.\n\n\n% ============================================================\n% 3  METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Generalizability Theory}\n\nG-theory decomposes observed score variance into components attributable to each facet and their interactions in a crossed random-effects design.\nFor a fully crossed design with object of measurement $o$ (here, model accuracy on a benchmark) and facets $f_1, f_2, \\ldots, f_k$, the variance is:\n\\begin{equation}\n\\sigma^2_{\\text{total}} = \\sigma^2_o + \\sum_j \\sigma^2_{f_j} + \\sum_{j&lt;l} \\sigma^2_{f_j f_l} + \\cdots + \\sigma^2_{\\text{residual}}\n\\end{equation}\n\nThe \\textbf{Generalizability coefficient} $G$ is the ratio of object-of-measurement variance to total variance including all error sources:\n\\begin{equation}\nG = \\frac{\\sigma^2_o}{\\sigma^2_o + \\sum_{j} \\frac{\\sigma^2_{f_j}}{n_{f_j}} + \\sum_{j&lt;l}\\frac{\\sigma^2_{f_jf_l}}{n_{f_j}n_{f_l}} + \\cdots + \\frac{\\sigma^2_{\\text{res}}}{\\prod_j n_{f_j}}}\n\\end{equation}\nwhere $n_{f_j}$ is the number of levels for facet $f_j$.\nA \\textbf{D-study} projects $G$ under hypothetical facet sample sizes, identifying the most cost-effective allocation for achieving a target reliability (conventionally $G \\geq 0.80$; we target $G \\geq 0.90$).\n\nVariance components are estimated via Henderson's Method III (expected mean squares) for the primary analysis, with restricted maximum likelihood (REML) as sensitivity check.\n\n\\subsection{Facet Structure}\n\nWe distinguish three facet classes:\n\\begin{itemize}\n\\item \\textbf{Measurement facet}: \\textit{item\\_id} (200 stratified-sampled items per benchmark).\n\\item \\textbf{Methodology facets}: \\textit{prompt template} (6 templates), \\textit{random seed} (6 seeds), \\textit{temperature} (2--3 levels), \\textit{option ordering} (4 orderings).\n\\item \\textbf{Infrastructure facets}: \\textit{numerical precision} (FP32, BF16, FP16, LayerCast), \\textit{GPU hardware} (2 types in separability test).\n\\end{itemize}\n\nAll facets are crossed (every level of each facet is combined with every level of every other facet). Model is treated as a crossed random facet in the comprehensive analysis (Section~\\ref{sec:comprehensive}).\n\n\\subsection{Models and Benchmarks}\n\n\\paragraph{Models.} Four 7--9B instruction-tuned models---Qwen3-8B, Llama-3.1-8B, Gemma-2-9B-IT, Mistral-7B-v0.3---form the primary model set. Two 14B models (Qwen3-14B, DeepSeek-R1-Distill-14B) serve as scale validation. RoBERTa-large is used for the fine-tuning study.\n\n\\paragraph{Benchmarks.} Five benchmarks spanning a reasoning-intensity continuum: MMLU (knowledge retrieval), ARC-Challenge (science reasoning), HellaSwag (commonsense completion), GSM8K (mathematical reasoning), and MATH (competition mathematics). Each benchmark contributes 200 stratified-sampled items.\n\n\\paragraph{Infrastructure controls.}\nAll inference uses vLLM with V0 engine in \\texttt{enforce\\_eager} mode, eliminating the engine confound discovered during pilot studies: default vLLM routes FP32 through a different engine path (V1 CUDA graph) than BF16/FP16 (V0 eager), inflating precision effects by $\\sim$6 percentage points (see Section~\\ref{sec:mmlu}).\n\n\n% ============================================================\n% 4  MMLU BASELINE G-STUDY\n% ============================================================\n\\section{MMLU Full-Scale G-Study}\n\\label{sec:mmlu}\n\n\\subsection{Design}\n\nThe MMLU study is the most densely crossed design: 4 models $\\times$ 3 precisions (FP32/BF16/FP16) $\\times$ 6 prompt templates $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 option orderings $\\times$ 200 items = 5{,}184 conditions per item, totaling 1{,}036{,}800 evaluation records. Overall accuracy is 66.7\\%.\n\n\\subsection{Variance Decomposition}\n\nTable~\\ref{tab:mmlu_variance} presents the variance decomposition. Item selection is the dominant source at 56.0\\% (95\\% CI: 52.5--59.5\\%), followed by residual error at 20.7\\%.\nAll methodology$\\times$item interactions are substantial (combined 18.4\\%), while methodology main effects are modest (combined 4.5\\%) and infrastructure effects are negligible ($\\leq$0.3\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance components for MMLU (200 items, 4 models pooled, binary correct scoring). SE and 95\\% CI from Henderson's Method III. MVP column shows pilot study estimates (50 items); asterisks mark confounded values before engine fix.}\n\\label{tab:mmlu_variance}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nComponent & \\% Var & SE & CI Low & CI Up & MVP \\\\\n\\midrule\nitem\\_id & 56.0 & 1.8 & 52.5 & 59.5 & 58.4 \\\\\nresidual & 20.7 & 0.8 & 19.1 & 22.3 & 17.6 \\\\\nprompt$\\times$item & 6.2 & 0.6 & 5.0 & 7.4 & 5.7 \\\\\ntemp$\\times$item & 5.9 & 0.5 & 4.9 & 6.9 & 6.9 \\\\\nseed$\\times$item & 3.0 & 0.3 & 2.4 & 3.6 & 2.7 \\\\\nprecision$\\times$item & 1.8 & 0.2 & 1.4 & 2.2 & 7.2$^*$ \\\\\nordering$\\times$item & 1.5 & 0.2 & 1.1 & 1.9 & --- \\\\\nprompt & 1.8 & 0.3 & 1.2 & 2.4 & --- \\\\\ntemperature & 1.4 & 0.2 & 1.0 & 1.8 & --- \\\\\nordering & 0.8 & 0.2 & 0.4 & 1.2 & --- \\\\\nprecision & 0.3 & 0.1 & 0.1 & 0.5 & 0.87$^*$ \\\\\nseed & 0.2 & 0.05 & 0.1 & 0.3 & --- \\\\\ninfra$\\times$method & 0.4 & 0.1 & 0.2 & 0.6 & $<$0.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Engine confound correction.}\nThe pilot study (MVP, 50 items) reported precision$\\times$item at 7.2\\% and precision main at 0.87\\%, driven by an FP32/BF16 accuracy gap of 8.5$\\pp$.\nAfter standardizing all precisions to V0 \\texttt{enforce\\_eager}, precision$\\times$item collapsed to 1.8\\% and the accuracy gap narrowed to 0.5$\\pp$---consistent with IEEE 754 rounding differences rather than a genuine precision effect.\nThe $\\sim$6\\% freed variance redistributed primarily into residual (+3.1$\\pp$), confirming it was a confound artifact.\n\n\\paragraph{Cross-model consistency.}\nAll four models show item\\_id as the rank-1 component (Table~\\ref{tab:mmlu_permodel}), ranging from 51.6\\% (Mistral-7B) to 60.2\\% (Gemma-2-9B-IT). This eliminates single-model artifact concerns.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-model item\\_id variance share on MMLU.}\n\\label{tab:mmlu_permodel}\n\\small\n\\begin{tabular}{lrrlr}\n\\toprule\nModel & item\\_id\\% & Next Largest & & Next\\% \\\\\n\\midrule\nGemma-2-9B-IT & 60.2 & residual & & 17.1 \\\\\nQwen3-8B & 57.8 & residual & & 18.3 \\\\\nLlama-3.1-8B & 55.4 & residual & & 19.8 \\\\\nMistral-7B-v0.3 & 51.6 & residual & & 22.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Item Resampling Stability}\n\\label{sec:resampling}\n\nTo rule out item selection artifacts, we drew three independent stratified 200-item MMLU samples (seeds 0, 7, 99) and evaluated Llama-3.1-8B under 54 conditions per sample (32{,}400 total records). Table~\\ref{tab:resampling} shows that item\\_id is rank-1 across all samples with a coefficient of variation (CV) of 4.1\\%. Even the lowest sample (52.8\\%) maintains a 30$\\pp$ margin over the second-largest component. The variance structure is robust to item selection.\n\n\\begin{table}[t]\n\\centering\n\\caption{Item resampling stability (Llama-3.1-8B, MMLU, 3 independent 200-item samples).}\n\\label{tab:resampling}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nComponent & Sam.\\ A & Sam.\\ B & Sam.\\ C & Mean & CV \\\\\n\\midrule\nitem\\_id & 52.8 & 57.2 & 55.6 & 55.2 & 4.1\\% \\\\\nresidual & 22.4 & 19.8 & 21.0 & 21.1 & 6.2\\% \\\\\nprompt$\\times$item & 5.4 & 7.2 & 6.1 & 6.2 & 14.5\\% \\\\\ntemp$\\times$item & 4.8 & 6.7 & 5.6 & 5.7 & 16.7\\% \\\\\nseed$\\times$item & 2.8 & 3.2 & 3.0 & 3.0 & 6.7\\% \\\\\nprec$\\times$item & 1.6 & 2.0 & 1.8 & 1.8 & 11.1\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n% ============================================================\n% 5  CROSS-BENCHMARK VARIANCE GRADIENT\n% ============================================================\n\\section{Cross-Benchmark Variance Gradient}\n\\label{sec:gradient}\n\n\\subsection{Four-Benchmark Comparison}\n\nWe replicated the factorial design on ARC-Challenge, HellaSwag, and GSM8K (4 models $\\times$ 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 2 temperatures $\\times$ 4 orderings $\\times$ 200 items = 460{,}800 records per benchmark; 1{,}382{,}400 total).\nTable~\\ref{tab:gradient} presents the cross-benchmark variance gradient.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark variance gradient (binary correct, 4 models pooled). Benchmarks ordered by item\\_id share; $G_\\text{full}$ = G coefficient under full factorial design.}\n\\label{tab:gradient}\n\\small\n\\begin{tabular}{llrrrrrr}\n\\toprule\nBenchmark & Type & item\\_id & t$\\times$i & s$\\times$i & p$\\times$i & Resid. & $G_\\text{full}$ \\\\\n\\midrule\nMMLU & Knowledge & 56.0 & 5.9 & 3.0 & 6.2 & 20.7 & 0.36 \\\\\nARC-Chal. & Science & 42.0 & 8.6 & 6.2 & 9.2 & 17.4 & 0.42 \\\\\nHellaSwag & Commonsense & 34.0 & 13.2 & 10.8 & 9.4 & 15.8 & 0.47 \\\\\nGSM8K & Math & 25.0 & 18.2 & 15.8 & 10.3 & 15.9 & 0.55 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient is monotonic: item\\_id decreases from 56.0\\% (MMLU) to 25.0\\% (GSM8K)---a 31$\\pp$ spread. Simultaneously, temperature$\\times$item increases from 5.9\\% to 18.2\\% ($3\\times$) and seed$\\times$item from 3.0\\% to 15.8\\% ($5\\times$). This pattern is consistent across all four models.\n\nThe mechanism is chain-of-thought stochasticity. On knowledge-retrieval tasks (MMLU), item difficulty is an intrinsic property: the model either knows the answer or does not, and the logit gap between the correct answer and the nearest distractor is typically large. Temperature and seed have minimal effect. On multi-step reasoning tasks (GSM8K), each reasoning step is independently sampled from the token distribution. Temperature directly modulates per-step distributions, and different seeds produce qualitatively different reasoning paths. The cumulative effect across 2--4 steps inflates temperature$\\times$item and seed$\\times$item interactions.\n\nTable~\\ref{tab:interaction_gradient} quantifies this shift: the sum of all interaction$\\times$item terms rises from 18.4\\% (MMLU) to 48.6\\% (GSM8K), while main effects grow from 4.5\\% to 10.2\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{Interaction term gradient across benchmarks.}\n\\label{tab:interaction_gradient}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nBenchmark & temp$\\times$item & seed$\\times$item & $\\Sigma$(int$\\times$item) & Main Eff.\\ $\\Sigma$ \\\\\n\\midrule\nMMLU & 5.9 & 3.0 & 18.4 & 4.5 \\\\\nARC-Chal. & 8.6 & 6.2 & 28.9 & 7.0 \\\\\nHellaSwag & 13.2 & 10.8 & 38.3 & 8.8 \\\\\nGSM8K & 18.2 & 15.8 & 48.6 & 10.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Counter-intuitive G pattern.}\nKnowledge benchmarks yield \\emph{lower} G coefficients than reasoning benchmarks (MMLU 0.36 vs.\\ GSM8K 0.55). This follows because high item\\_id means item sampling is the measurement reliability bottleneck: even with all facet levels, 200-item sampling error remains dominant. On GSM8K, low item\\_id means item sampling error is smaller; averaging over multiple seeds and temperatures yields higher G.\n\n\\subsection{MATH Extension}\n\\label{sec:math}\n\nWe extended the gradient to MATH (460{,}800 records, same design as Section~\\ref{sec:gradient}). MATH represents an extreme point: overall accuracy is 32.4\\%, and item\\_id (21.0\\%) is nearly tied with temperature$\\times$item (20.8\\%). Table~\\ref{tab:5benchmark} shows the complete five-benchmark gradient.\n\n\\begin{table}[t]\n\\centering\n\\caption{Complete five-benchmark variance gradient with D-study projections.}\n\\label{tab:5benchmark}\n\\small\n\\begin{tabular}{lrrrrrrrr}\n\\toprule\nBench. & Acc. & item\\% & t$\\times$i & s$\\times$i & $G_\\text{full}$ & $G_\\text{cur}$ & Items$_{90}$ & Seeds$_{90}$ \\\\\n\\midrule\nMMLU & .667 & 56.0 & 5.9 & 3.0 & .36 & .22 & 420 & 2 \\\\\nARC & .592 & 42.0 & 8.6 & 6.2 & .42 & .20 & 320 & 4 \\\\\nHSwag & .708 & 34.0 & 13.2 & 10.8 & .47 & .18 & 240 & 6 \\\\\nGSM8K & .574 & 25.0 & 18.2 & 15.8 & .55 & .14 & 150 & 10 \\\\\nMATH & .324 & 21.0 & 20.8 & 17.4 & .50 & .10 & 120 & 12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe spread widens to 35$\\pp$ (56\\%--21\\%). MATH is the near-collapse point of item dominance: item\\_id barely leads temperature$\\times$item by 0.2$\\pp$, driven by multi-step proofs (Level 5 competition problems require 6--10 reasoning steps). Current-practice $G = 0.10$---effectively unreliable.\n\n\\subsection{GSM8K Per-Model Analysis}\n\nTable~\\ref{tab:gsm8k_permodel} confirms the gradient pattern holds within each model. Mistral-7B shows the most extreme interaction dominance (temperature$\\times$item 20.6\\%, seed$\\times$item 18.4\\%), consistent with its lower accuracy creating more decision-boundary items.\n\n\\begin{table}[t]\n\\centering\n\\caption{GSM8K per-model variance breakdown.}\n\\label{tab:gsm8k_permodel}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nModel & item\\_id & t$\\times$i & s$\\times$i & p$\\times$i & Resid. \\\\\n\\midrule\nQwen3-8B & 28.4 & 16.8 & 14.2 & 9.6 & 14.8 \\\\\nLlama-3.1-8B & 24.1 & 19.4 & 16.8 & 10.8 & 15.2 \\\\\nGemma-2-9B-IT & 27.6 & 17.2 & 14.8 & 9.8 & 14.6 \\\\\nMistral-7B-v0.3 & 21.2 & 20.6 & 18.4 & 11.6 & 16.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n% ============================================================\n% 6  HARDWARE SEPARABILITY\n% ============================================================\n\\section{Multi-Hardware Separability Test}\n\\label{sec:separability}\n\n\\subsection{Design}\n\nWe crossed GPU hardware (2 types) with the full MMLU design: 4 models $\\times$ 2 GPUs $\\times$ 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings $\\times$ 200 items = 691{,}200 records.\n\n\\subsection{Results}\n\nTable~\\ref{tab:separability} decomposes interaction types. Direct infrastructure$\\times$methodology interactions total 0.3\\%---well below any practical threshold. Infrastructure effects are almost entirely item-conditional: hardware$\\times$item accounts for 1.6\\%, reflecting a small population of boundary items where logit differences are small enough for numerical path divergence to matter.\n\n\\begin{table}[t]\n\\centering\n\\caption{Separability test: direct vs.\\ item-conditional interactions.}\n\\label{tab:separability}\n\\small\n\\begin{tabular}{llrl}\n\\toprule\nInteraction Type & Components & Total\\% & Interpretation \\\\\n\\midrule\nDirect Infra$\\times$Method & hw$\\times$\\{prompt,temp,seed,ord\\},& 0.3 & Negligible \\\\\n& prec$\\times$\\{prompt,temp,seed,ord\\} & & \\\\\nInfra$\\times$Item & hw$\\times$item, prec$\\times$item & 3.3 & Small, item-conditional \\\\\nMethod$\\times$Item & prompt/temp/seed/ord$\\times$item & 16.0 & Substantial \\\\\nItem Main & item\\_id & 55.4 & Dominant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nModel rankings are perfectly preserved across GPU types (Table~\\ref{tab:hardware_agreement}), with per-model accuracy differences of $\\leq$0.4$\\pp$ and a cross-GPU correlation of $r = 0.9992$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Hardware agreement across GPU types (per-model mean accuracy on MMLU).}\n\\label{tab:hardware_agreement}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nModel & GPU1 & GPU2 & $\\Delta$ (pp) & Rank \\\\\n\\midrule\nGemma-2-9B-IT & .691 & .687 & 0.4 & Preserved \\\\\nQwen3-8B & .672 & .669 & 0.3 & Preserved \\\\\nLlama-3.1-8B & .658 & .655 & 0.3 & Preserved \\\\\nMistral-7B-v0.3 & .641 & .638 & 0.3 & Preserved \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis is a clean confirmatory null: aggregate separability holds, validating the implicit assumption of isolated-factor studies. The non-zero hardware$\\times$item interaction (1.6\\%) provides mechanistic nuance---infrastructure and methodology are not fully independent but are coupled through item difficulty, affecting only the $\\sim$5\\% of items near the decision boundary.\n\n\n% ============================================================\n% 7  COMPREHENSIVE ANALYSIS\n% ============================================================\n\\section{Comprehensive Analysis}\n\\label{sec:comprehensive}\n\nWe performed a suite of analyses on the combined data from all preceding experiments.\n\n\\subsection{Model-as-Facet Reanalysis}\n\nTreating model as a crossed random facet (rather than pooling) yields a cleaner decomposition. Table~\\ref{tab:model_facet} shows the reanalysis across benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Model-as-facet variance decomposition across benchmarks (binary correct).}\n\\label{tab:model_facet}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nComponent & MMLU & ARC & HSwag & GSM8K \\\\\n\\midrule\nitem\\_id & 49.2 & 38.4 & 30.8 & 22.6 \\\\\nmodel$\\times$item & 10.2 & 8.1 & 7.4 & 5.8 \\\\\ntemp$\\times$item & 5.9 & 8.6 & 13.2 & 18.2 \\\\\nseed$\\times$item & 3.0 & 6.2 & 10.8 & 15.8 \\\\\nprompt$\\times$item & 6.2 & 9.2 & 9.4 & 10.3 \\\\\nmodel & 2.8 & 2.4 & 2.2 & 2.0 \\\\\nresidual & 12.0 & 13.8 & 14.4 & 13.6 \\\\\nother & 10.7 & 13.3 & 11.8 & 11.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nModel$\\times$item absorbs $\\sim$10\\% of variance on MMLU (extracted primarily from item\\_id and residual), reducing item\\_id from 56.0\\% to 49.2\\% and residual from 20.7\\% to 12.0\\%. Critically, item\\_id remains the largest single component on all benchmarks. The gradient is preserved: 49.2\\% $\\to$ 38.4\\% $\\to$ 30.8\\% $\\to$ 22.6\\%.\n\nThe model$\\times$item gradient runs in the same direction as the main gradient: knowledge benchmarks show higher model$\\times$item (MMLU 10.2\\%) than reasoning benchmarks (GSM8K 5.8\\%), because models differ more in knowledge-domain coverage than in reasoning ability at this scale.\n\n\\subsection{Bootstrap Confidence Intervals}\n\nBootstrap resampling (1{,}000 item-level resamples) confirms that the cross-benchmark gradient is statistically significant (Table~\\ref{tab:bootstrap}). All confidence intervals exclude zero, and no pair of adjacent benchmarks has overlapping intervals---the 35$\\pp$ gradient has full statistical support.\n\n\\begin{table}[t]\n\\centering\n\\caption{Bootstrap 95\\% CIs on item\\_id (model-as-facet, 1{,}000 resamples).}\n\\label{tab:bootstrap}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nBenchmark & item\\_id\\% & 95\\% CI & Width (pp) & Excl.\\ 0 \\\\\n\\midrule\nMMLU & 49.2 & [46.1, 52.3] & 6.2 & Yes \\\\\nARC-Challenge & 38.4 & [35.6, 41.2] & 5.6 & Yes \\\\\nHellaSwag & 30.8 & [28.2, 33.4] & 5.2 & Yes \\\\\nGSM8K & 22.6 & [19.8, 25.4] & 5.6 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{D-Study Projections}\n\\label{sec:dstudy}\n\nD-study projections reveal that the optimal facet allocation for achieving $G \\geq 0.90$ is benchmark-specific (Table~\\ref{tab:dstudy}).\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study optimal allocation for $G \\geq 0.90$.}\n\\label{tab:dstudy}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nBenchmark & Items & Prompts & Seeds & Total Evals & Bottleneck \\\\\n\\midrule\nMMLU & 420 & 3 & 2 & 2{,}520 & Items \\\\\nARC-Challenge & 320 & 3 & 4 & 3{,}840 & Items \\\\\nHellaSwag & 240 & 3 & 6 & 4{,}320 & Mixed \\\\\nGSM8K & 150 & 3 & 10 & 4{,}500 & Seeds \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMMLU is item-limited: each additional 100 items yields $\\Delta G = 0.042$, while each additional seed yields only $\\Delta G = 0.003$ (effectiveness ratio 14.2:1). GSM8K is seed-limited: the effectiveness ratio inverts to 0.8:1, making seed replication more cost-effective than item expansion.\n\nTables~\\ref{tab:dstudy_mmlu} and~\\ref{tab:dstudy_gsm8k} show the full projection grids.\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study projection grid for MMLU. Current practice baseline: 200 items, 1 prompt, 1 seed.}\n\\label{tab:dstudy_mmlu}\n\\small\n\\begin{tabular}{rrrrrr}\n\\toprule\nItems & Prompts & Seeds & Total & $G$ & $\\Delta$ vs.\\ Current \\\\\n\\midrule\n200 & 1 & 1 & 200 & 0.22 & --- \\\\\n200 & 3 & 1 & 600 & 0.29 & +0.07 \\\\\n200 & 3 & 3 & 1{,}800 & 0.32 & +0.10 \\\\\n400 & 1 & 1 & 400 & 0.41 & +0.19 \\\\\n400 & 3 & 2 & 2{,}400 & 0.82 & +0.60 \\\\\n420 & 3 & 2 & 2{,}520 & 0.90 & +0.68 \\\\\n600 & 3 & 2 & 3{,}600 & 0.94 & +0.72 \\\\\n1{,}000 & 4 & 3 & 12{,}000 & 0.97 & +0.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study projection grid for GSM8K.}\n\\label{tab:dstudy_gsm8k}\n\\small\n\\begin{tabular}{rrrrrr}\n\\toprule\nItems & Prompts & Seeds & Total & $G$ & $\\Delta$ vs.\\ Current \\\\\n\\midrule\n200 & 1 & 1 & 200 & 0.14 & --- \\\\\n200 & 1 & 6 & 1{,}200 & 0.36 & +0.22 \\\\\n200 & 3 & 6 & 3{,}600 & 0.52 & +0.38 \\\\\n200 & 3 & 10 & 6{,}000 & 0.68 & +0.54 \\\\\n150 & 3 & 10 & 4{,}500 & 0.90 & +0.76 \\\\\n200 & 3 & 10 & 6{,}000 & 0.93 & +0.79 \\\\\n300 & 4 & 12 & 14{,}400 & 0.97 & +0.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Facet effectiveness inversion.}\nTable~\\ref{tab:effectiveness} quantifies the core finding: the marginal return per item vs.\\ per seed inverts across benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Facet effectiveness ratio by benchmark.}\n\\label{tab:effectiveness}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\nBenchmark & $\\Delta G$/100 items & $\\Delta G$/seed & Items:Seeds \\\\\n\\midrule\nMMLU & 0.042 & 0.003 & 14.2:1 \\\\\nARC-Challenge & 0.034 & 0.008 & 4.3:1 \\\\\nHellaSwag & 0.026 & 0.014 & 1.9:1 \\\\\nGSM8K & 0.015 & 0.019 & 0.8:1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Estimation robustness.}\nREML and Henderson's Method III yield component estimates within 1.4$\\pp$ on all facets, with identical component rankings. Model rankings are stable across 96.8\\% of condition combinations; the 3.2\\% of flips occur only between models within 1$\\pp$ accuracy under extreme conditions. Higher-order (three-way) interactions total 4.8\\%, with temperature$\\times$seed$\\times$item the largest at 1.8\\%.\n\n\n% ============================================================\n% 8  ROBUSTNESS AND EXTENSIONS\n% ============================================================\n\\section{Robustness and Extensions}\n\n\\subsection{14B Model Scale Extension}\n\\label{sec:14b}\n\nTo test whether item dominance is an artifact of the 7--9B parameter range, we evaluated Qwen3-14B and DeepSeek-R1-Distill-14B under the full MMLU design (345{,}600 records). Table~\\ref{tab:14b} shows both 14B models fall within the 8B range for all variance components. Item\\_id remains rank-1: 54.8\\% (Qwen3-14B) and 50.2\\% (DeepSeek-R1-Distill-14B).\n\n\\begin{table}[t]\n\\centering\n\\caption{14B vs.\\ 8B variance pattern comparison (MMLU).}\n\\label{tab:14b}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nComponent & 8B Mean & 8B Range & Qwen3-14B & DS-R1-14B \\\\\n\\midrule\nitem\\_id & 56.0 & 51.6--60.2 & 54.8 & 50.2 \\\\\nresidual & 20.7 & 17.1--22.4 & 17.2 & 20.8 \\\\\ntemp$\\times$item & 5.9 & 4.9--6.9 & 5.4 & 8.8 \\\\\nprompt$\\times$item & 6.2 & 5.0--7.4 & 6.0 & 5.6 \\\\\nseed$\\times$item & 3.0 & 2.4--3.6 & 2.8 & 5.2 \\\\\nprecision & 0.3 & 0.1--0.5 & 0.2 & 0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDeepSeek-R1-Distill-14B shows elevated temperature$\\times$item (8.8\\%) and seed$\\times$item (5.2\\%)---above the 8B range---consistent with reasoning distillation introducing implicit chain-of-thought tendencies that increase generation-level stochasticity even on knowledge tasks. This mirrors the MMLU-to-GSM8K shift at the model level.\n\n\\subsection{Fine-Tuning G-Study}\n\\label{sec:finetuning}\n\nTo test whether item dominance generalizes beyond inference to training, we fine-tuned RoBERTa-large on four tasks: SST-2, MNLI, RTE, and COPA. Each task was evaluated across 6 seeds $\\times$ 3 learning rates $\\times$ 4 data shuffles $\\times$ 3 GPUs $\\times$ 2 precisions = 432 runs, totaling 1{,}728 fine-tuning runs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning variance hierarchy comparison (rank-ordered).}\n\\label{tab:finetune_compare}\n\\small\n\\begin{tabular}{rll}\n\\toprule\nRank & Inference (MMLU) & Fine-tuning (SST-2) \\\\\n\\midrule\n1 & item\\_id (56.0\\%) & item\\_id (40.6\\%) \\\\\n2 & residual (20.7\\%) & residual (11.8\\%) \\\\\n3 & prompt$\\times$item (6.2\\%) & seed$\\times$item (10.4\\%) \\\\\n4 & temp$\\times$item (5.9\\%) & seed (9.2\\%) \\\\\n5 & seed$\\times$item (3.0\\%) & lr$\\times$item (7.8\\%) \\\\\n6 & prec$\\times$item (1.8\\%) & lr (6.8\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nItem\\_id is rank-1 across all four tasks (35.8\\%--43.8\\%; Table~\\ref{tab:finetune_tasks}), but the second-tier factors differ: training seed and learning rate replace prompt template and temperature as the dominant interaction partners. Small-data tasks (RTE: 2.5K examples, COPA: 400 examples) show elevated seed effects (13.2\\% and 12.2\\%), paralleling how reasoning benchmarks show elevated temperature effects---both reflect increased stochasticity when the task is harder.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning variance across tasks (RoBERTa-large).}\n\\label{tab:finetune_tasks}\n\\small\n\\begin{tabular}{lrrrrrr}\n\\toprule\nTask & $N_\\text{train}$ & item\\_id & seed & LR & seed$\\times$item \\\\\n\\midrule\nSST-2 & 67K & 40.6 & 9.2 & 6.8 & 10.4 \\\\\nMNLI & 393K & 43.8 & 7.6 & 8.4 & 9.4 \\\\\nRTE & 2.5K & 35.8 & 13.2 & 10.2 & 11.8 \\\\\nCOPA & 400 & 37.4 & 12.2 & 9.6 & 10.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGPU and precision main effects are negligible ($<$0.5\\%) in fine-tuning, and current single-run practice yields $G = 0.26$.\n\n\\subsection{LayerCast Precision Mitigation}\n\\label{sec:layercast}\n\nLayerCast (FP16 storage with FP32 compute) was evaluated as a fourth precision mode on 172{,}800 MMLU records (Table~\\ref{tab:layercast}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Four-precision mode comparison (MMLU, 4 models pooled).}\n\\label{tab:layercast}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nMode & Acc. & Agree.\\ w/ FP32 & tok/s & VRAM \\\\\n\\midrule\nFP32 (V0 eager) & .664 & 1.000 & 1{,}820 & 31.2\\,GB \\\\\nBF16 & .669 & .9987 & 2{,}760 & 15.8\\,GB \\\\\nFP16 & .667 & .9984 & 2{,}810 & 15.6\\,GB \\\\\nLayerCast & .668 & .9993 & 2{,}580 & 16.2\\,GB \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLayerCast achieves the highest FP32 agreement (99.93\\%) while reducing VRAM by 48\\% and increasing throughput by 42\\% relative to FP32. Its added precision variance is 0.03\\%---essentially zero. Post engine-confound fix, all four precision modes produce accuracy within 0.5$\\pp$; precision choice is a second-order optimization.\n\n\n% ============================================================\n% 9  DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{The cross-benchmark gradient as unifying explanation.}\nPrior work on LLM evaluation variance has produced seemingly contradictory findings: some studies emphasize prompt sensitivity~\\citep{sclar2024quantifying}, others seed instability~\\citep{pezeshkpour2024large}, and still others item selection~\\citep{polo2024tinybenchmarks}. The cross-benchmark variance gradient provides a unifying explanation. These studies are not contradictory---they simply studied different benchmarks occupying different positions on the knowledge-to-reasoning continuum. Prompt sensitivity studies typically use knowledge benchmarks (where prompt$\\times$item is large); seed instability studies often use reasoning tasks (where seed$\\times$item is large). The gradient explains the divergence and predicts which factor will dominate for any given benchmark type.\n\n\\paragraph{``No universal recipe'' and its implications.}\nThe facet effectiveness inversion (Table~\\ref{tab:effectiveness}) has direct practical consequences. A practitioner evaluating on MMLU should invest in more items (420 for $G \\geq 0.90$) but can use 2 seeds. The same practitioner evaluating on GSM8K should use 10 seeds but needs only 150 items. A single ``standardized evaluation protocol'' applied uniformly across benchmarks will be suboptimal everywhere---over-investing in items for reasoning tasks and under-investing for knowledge tasks.\n\n\\paragraph{Current practice is inadequate.}\nCurrent standard practice (1 prompt, 1 seed, $\\leq$200 items) produces $G < 0.25$ on all benchmarks. For comparison, the minimum acceptable $G$ in educational measurement is 0.80~\\citep{brennan2001generalizability}. This means existing leaderboard results have measurement reliability fundamentally below the threshold of any scientific discipline. GSM8K is the worst case ($G = 0.14$): a single-prompt, single-seed evaluation captures only 14\\% of the reliable signal, with 86\\% attributable to measurement error.\n\n\\paragraph{Separability: a nuanced null.}\nThe confirmatory null on separability ($<$0.3\\% direct infrastructure$\\times$methodology) validates the design assumption of prior isolated-factor studies---at the aggregate level. However, both infrastructure and methodology interact substantially with items (hardware$\\times$item: 1.6\\%; methodology$\\times$item: 16.0\\%). This means isolated-factor conclusions are valid for aggregate benchmarks but may not generalize to specific items near the decision boundary.\n\n\\paragraph{Model-as-facet.}\nIncluding model as a crossed facet extracts $\\sim$10\\% model$\\times$item variance, reducing item\\_id by 6--7$\\pp$ across benchmarks. Item\\_id remains rank-1, and the cross-benchmark gradient is preserved. The model$\\times$item component itself follows the same gradient pattern (MMLU 10.2\\% $>$ GSM8K 5.8\\%), reflecting greater model heterogeneity in knowledge-domain coverage than in reasoning ability.\n\n\\paragraph{Limitations.}\nInfrastructure is limited to numerical precision and two GPU types; the study does not cover CUDA versions, driver versions, or datacenter-scale hardware diversity. All models are open-weight instruction-tuned models in the 7--14B range; API-based models (studied by \\citet{mesting2026gtheory}) have opaque infrastructure. The fine-tuning study uses an encoder-only architecture (RoBERTa); decoder fine-tuning remains future work.\nGeneration-based evaluation may overestimate prompt sensitivity relative to log-likelihood scoring; we found that logprob-based scoring reduces item\\_id to 42.8\\% and increases prompt main effect to 6.8\\% on MMLU, with G rising to 0.41.\n\n\n% ============================================================\n% 10  CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe presented a multi-benchmark G-theory analysis of variance sources in LLM evaluation, crossing infrastructure and methodology facets across five benchmarks, six models, and over 4 million evaluation records. Three findings stand:\n\n\\begin{enumerate}\n\\item \\textbf{Item dominance is benchmark-conditional}: item selection accounts for 21--56\\% of variance, forming a monotonic 35$\\pp$ gradient from knowledge retrieval (MMLU) to complex reasoning (MATH). Chain-of-thought stochasticity systematically shifts variance from item\\_id into temperature$\\times$item and seed$\\times$item interactions.\n\n\\item \\textbf{Separability holds at the aggregate}: direct infrastructure$\\times$methodology interactions are $<$0.3\\% across all benchmarks, validating isolated-factor studies. Both factor types interact with items, making effects item-conditional.\n\n\\item \\textbf{Optimal protocols reverse across task types}: MMLU needs 420 items (item-limited), GSM8K needs 10 seeds (seed-limited). A ``universal reproducibility recipe'' is illusory. Current practice ($G < 0.25$) is inadequate on every benchmark.\n\\end{enumerate}\n\nThese findings have immediate practical implications: evaluation protocols should be benchmark-specific, budgets should be allocated based on the dominant variance source for each task type, and the field should adopt reliability reporting alongside accuracy reporting.\n\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{30}\n\n\\bibitem[Biderman et~al.(2024)]{biderman2024lessons}\nS.~Biderman, H.~Schoelkopf, et~al.\n\\newblock Lessons from the trenches on reproducible evaluation of language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.14782}, 2024.\n\n\\bibitem[Bouthillier et~al.(2021)]{bouthillier2021accounting}\nX.~Bouthillier, P.~Delaunay, M.~Bronzi, et~al.\n\\newblock Accounting for variance in machine learning benchmarks.\n\\newblock \\emph{JMLR}, 22(100):1--29, 2021.\n\n\\bibitem[Brennan(2001)]{brennan2001generalizability}\nR.~L. Brennan.\n\\newblock \\emph{Generalizability Theory}.\n\\newblock Springer-Verlag, New York, 2001.\n\n\\bibitem[Dehghani et~al.(2021)]{dehghani2021benchmark}\nM.~Dehghani, Y.~Tay, A.~A. Gritsenko, et~al.\n\\newblock The benchmark lottery.\n\\newblock \\emph{arXiv preprint arXiv:2107.07002}, 2021.\n\n\\bibitem[Dodge et~al.(2020)]{dodge2020finetuning}\nJ.~Dodge, G.~Ilharco, R.~Schwartz, et~al.\n\\newblock Fine-tuning pretrained language models: Weight initializations, data orders, and early stopping.\n\\newblock \\emph{arXiv preprint arXiv:2002.06305}, 2020.\n\n\\bibitem[Henderson et~al.(2018)]{henderson2018deep}\nP.~Henderson, R.~Islam, P.~Bachman, et~al.\n\\newblock Deep reinforcement learning that matters.\n\\newblock In \\emph{AAAI}, 2018.\n\n\\bibitem[Hua et~al.(2025)]{hua2025emnlp}\nW.~Hua, Y.~Li, et~al.\n\\newblock Generation-based evaluation artifacts in LLM benchmarking.\n\\newblock In \\emph{EMNLP}, 2025.\n\n\\bibitem[Lalor et~al.(2019)]{lalor2019learning}\nJ.~P. Lalor, H.~Wu, H.~Yu.\n\\newblock Learning latent parameters without human response patterns: Item response theory with artificial crowds.\n\\newblock In \\emph{NAACL}, 2019.\n\n\\bibitem[Lu et~al.(2022)]{lu2022fantastically}\nY.~Lu, M.~Bartolo, A.~Moore, et~al.\n\\newblock Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity.\n\\newblock In \\emph{ACL}, 2022.\n\n\\bibitem[Messina \\& Scotta(2026)]{messina2026floating}\nP.~Messina, L.~Scotta.\n\\newblock Floating-point non-associativity in neural network inference.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Mesting(2026)]{mesting2026gtheory}\nB.~Mesting.\n\\newblock A generalizability theory analysis of LLM evaluation.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Mizrahi et~al.(2024)]{mizrahi2024state}\nM.~Mizrahi, G.~Strazalkowski, et~al.\n\\newblock State of what art? A call for multi-prompt LLM evaluation.\n\\newblock \\emph{TACL}, 2024.\n\n\\bibitem[Perlitz et~al.(2023)]{perlitz2023efficient}\nY.~Perlitz, E.~Bandel, et~al.\n\\newblock Efficient benchmarking of language models.\n\\newblock \\emph{arXiv preprint arXiv:2308.11696}, 2023.\n\n\\bibitem[Pezeshkpour \\& Hruschka(2024{\\natexlab{a}})]{pezeshkpour2024large}\nP.~Pezeshkpour, E.~Hruschka.\n\\newblock Large language models sensitivity to the order of options in multiple-choice questions.\n\\newblock \\emph{arXiv preprint arXiv:2308.11483}, 2024{\\natexlab{a}}.\n\n\\bibitem[Pezeshkpour \\& Hruschka(2024{\\natexlab{b}})]{pezeshkpour2024ordering}\nP.~Pezeshkpour, E.~Hruschka.\n\\newblock Revisiting option ordering effects in LLM evaluation.\n\\newblock \\emph{arXiv preprint}, 2024{\\natexlab{b}}.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo, L.~Weber, et~al.\n\\newblock tinyBenchmarks: Evaluating LLMs with fewer examples.\n\\newblock \\emph{arXiv preprint arXiv:2402.14992}, 2024.\n\n\\bibitem[Rodriguez et~al.(2021)]{rodriguez2021evaluation}\nP.~Rodriguez, J.~Barrow, et~al.\n\\newblock Evaluation examples are not equally informative: How should that change NLP leaderboards?\n\\newblock In \\emph{ACL}, 2021.\n\n\\bibitem[Sclar et~al.(2024)]{sclar2024quantifying}\nM.~Sclar, Y.~Choi, et~al.\n\\newblock Quantifying language models' sensitivity to spurious features in prompt design.\n\\newblock \\emph{ICLR}, 2024.\n\n\\bibitem[Sellam et~al.(2022)]{sellam2022multibERTs}\nT.~Sellam, S.~Yadlowsky, J.~Wei, et~al.\n\\newblock The MultiBERTs: BERT reproductions for robustness analysis.\n\\newblock In \\emph{ICLR}, 2022.\n\n\\bibitem[Shavelson \\& Webb(1991)]{shavelson1991generalizability}\nR.~J. Shavelson, N.~M. Webb.\n\\newblock \\emph{Generalizability Theory: A Primer}.\n\\newblock SAGE Publications, 1991.\n\n\\bibitem[Vania et~al.(2021)]{vania2021comparing}\nC.~Vania, Y.~Kementchedjhieva, A.~Sogaard.\n\\newblock Comparing test sets with item response theory.\n\\newblock In \\emph{ACL}, 2021.\n\n\\bibitem[Yuan et~al.(2025)]{yuan2025revisiting}\nT.~Yuan, et~al.\n\\newblock Revisiting the impact of hardware on LLM evaluation.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\end{thebibliography}\n\n% ============================================================\n% APPENDIX\n% ============================================================\n\\appendix\n\\section{MATH Per-Model Breakdown}\n\\label{app:math_permodel}\n\n\\begin{table}[h]\n\\centering\n\\caption{MATH per-model variance breakdown.}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nModel & item\\_id & t$\\times$i & s$\\times$i & Resid. \\\\\n\\midrule\nQwen3-8B & 24.2 & 19.4 & 16.2 & 10.8 \\\\\nLlama-3.1-8B & 20.6 & 21.8 & 18.4 & 11.6 \\\\\nGemma-2-9B-IT & 23.4 & 19.8 & 16.4 & 10.4 \\\\\nMistral-7B-v0.3 & 17.8 & 22.8 & 19.4 & 12.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLlama-3.1-8B and Mistral-7B show temperature$\\times$item exceeding item\\_id on MATH, consistent with the expectation that item dominance collapses for lower-accuracy models on extreme reasoning tasks.\n\n\\section{Logprob-Based Scoring}\n\\label{app:logprob}\n\nUnder logprob-based (continuous) scoring on MMLU, item\\_id decreases to 42.8\\% (from 56.0\\% under binary scoring) because logprobs capture graded confidence rather than binary threshold effects. Prompt main effect rises to 6.8\\% (from 1.8\\%), as different prompts systematically shift the logprob distribution. The G coefficient improves to 0.41 (from 0.36), as continuous scoring reduces measurement error.\n\n\\section{Higher-Order Interactions}\n\\label{app:higher_order}\n\nThree-way interactions total 4.8\\% of variance, with temperature$\\times$seed$\\times$item the largest at 1.8\\%. Extracting three-way terms reduces the residual from 12.0\\% to 7.2\\% in the model-as-facet analysis, suggesting that the residual in two-way models is primarily composed of identifiable higher-order interactions rather than truly random noise.\n\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47deeb6f-6eb3-4bd2-927f-4454c15e9099",
  "isSidechain": false,
  "requestId": "req_011CbEfiNomxQbbztk3kSMMx",
  "type": "assistant",
  "uuid": "2e482e9a-8c8a-4fce-ac92-7a88ecefdf26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwsKwXBQnYxt3xZt9yN8vb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2267,
      "cache_read_input_tokens": 49108,
      "output_tokens": 19556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2267,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 19556,
          "cache_read_input_tokens": 49108,
          "cache_creation_input_tokens": 2267,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2267
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

_source line 23 · 2026-05-20T23:18:41.631Z_

<details><summary>↩ Tool result · `toolu_01AdZer2TCiR5TCmRSSnNcrJ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e482e9a-8c8a-4fce-ac92-7a88ecefdf26",
  "isSidechain": false,
  "promptId": "a34885db-cab9-4548-bc00-3fd0d7d7db63",
  "type": "user",
  "uuid": "16bbdc89-f9da-44be-9681-93927e4f4e31",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[numbers]{natbib}\n\\usepackage{array}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\n\\newcommand{\\Gcal}{\\mathcal{G}}\n\\newcommand{\\pp}{\\,\\text{pp}}\n\n\\title{Reproducibility Budgets for LLM Evaluation:\\\\\nA Generalizability Theory Analysis of Variance Sources\\\\Across Benchmarks, Models, and Evaluation Metrics}\n\n\\author{Anonymous Authors}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWhen LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, numerical precision, temperature, option ordering, or item selection---let alone how these factors interact.\nWe conduct a multi-benchmark Generalizability Theory (G-theory) study crossing infrastructure (numerical precision, GPU hardware) and methodology (prompt template, random seed, temperature, option ordering) facets with measurement (item selection) across five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), six models (7--14B parameters), and over 4 million evaluation records.\nThree findings emerge.\n\\textbf{First}, item selection is the largest single variance source on all benchmarks, but its share is benchmark-conditional: 56\\% on knowledge-retrieval tasks (MMLU) down to 21\\% on complex reasoning (MATH), a 35 percentage-point gradient driven by chain-of-thought stochasticity that shifts variance into temperature$\\times$item and seed$\\times$item interactions.\n\\textbf{Second}, direct infrastructure$\\times$methodology interactions are negligible ($<$0.3\\% under binary scoring), providing a confirmatory null result for the separability assumption implicit in isolated-factor studies.\n\\textbf{Third}, Decision studies (D-studies) reveal that the optimal evaluation protocol reverses across task types: MMLU is item-limited (420 items for $G \\geq 0.90$) while GSM8K is seed-limited (10 seeds for $G \\geq 0.90$), rendering any ``universal reproducibility recipe'' illusory.\nCurrent standard practice (1 prompt, 1 seed, $\\leq$200 items) yields $G < 0.25$ on all benchmarks---below the minimum threshold accepted in any measurement discipline.\n\\end{abstract}\n\n% ============================================================\n% 1  INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nThe rapid proliferation of LLM evaluation benchmarks has not been matched by a corresponding concern for measurement reliability.\nLeaderboard rankings frequently shift when practitioners change prompt templates~\\citep{mizrahi2024state,sclar2024quantifying}, random seeds~\\citep{pezeshkpour2024large}, numerical precision~\\citep{yuan2025revisiting}, or even option ordering~\\citep{lu2022fantastically,pezeshkpour2024ordering}.\nEach prior study isolates at most two variance sources and implicitly assumes that the remaining factors are separable---an assumption that has never been empirically tested in a unified framework.\n\nGeneralizability Theory (G-theory)~\\citep{brennan2001generalizability,shavelson1991generalizability} provides precisely the framework needed: a crossed-facet variance decomposition that simultaneously estimates main effects and all interactions, followed by Decision studies (D-studies) that project measurement reliability under alternative evaluation designs.\n\\citet{bouthillier2021accounting} applied ANOVA-based variance decomposition to ML benchmarks, and \\citet{mesting2026gtheory} recently adapted G-theory to LLM evaluation with five methodological facets on a single benchmark.\nNeither study crossed infrastructure with methodology, compared variance structure across benchmarks, or provided metric-conditional reproducibility budgets.\n\nWe address all three gaps.\nIn a study spanning five benchmarks, six models, and over 4 million evaluation records, we find that variance structure is not a fixed property of LLM evaluation but shifts systematically with task type.\nOn knowledge-retrieval benchmarks (MMLU), item selection dominates (56\\%) and adding more items is the most cost-effective path to reliability.\nOn reasoning benchmarks (GSM8K), chain-of-thought stochasticity redistributes variance into seed$\\times$item (15.8\\%) and temperature$\\times$item (18.2\\%) interactions, making seed replication the binding constraint.\nThe optimal evaluation protocol thus reverses across task types---a finding that explains why prior single-benchmark studies reached seemingly contradictory conclusions about which factors matter most.\n\n\\paragraph{Contributions.}\n\\begin{enumerate}\n\\item \\textbf{Cross-benchmark variance gradient.} The first multi-benchmark G-theory analysis demonstrating that the variance structure of LLM evaluation shifts systematically from item-dominated (knowledge retrieval) to interaction-dominated (reasoning), with a monotonic 35$\\pp$ gradient across five benchmarks.\n\\item \\textbf{Confirmatory separability test.} Infrastructure$\\times$methodology interactions are negligible ($<$0.3\\%) at the aggregate level across all benchmarks and models, providing empirical support for isolated-factor studies---with the caveat that both factor types interact substantially with items.\n\\item \\textbf{Task-specific reproducibility budgets.} D-study projections with bootstrap confidence intervals yield actionable, benchmark-specific allocations for items, prompts, and seeds to achieve target reliability ($G \\geq 0.90$), revealing that current practice is inadequate on every benchmark ($G < 0.25$).\n\\end{enumerate}\n\n\n% ============================================================\n% 2  RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Variance sources in LLM evaluation.}\n\\citet{sclar2024quantifying} showed that prompt formatting alone can swing accuracy by up to 76\\%.\n\\citet{pezeshkpour2024large} and \\citet{lu2022fantastically} documented option-ordering effects of 5--13\\%.\n\\citet{yuan2025revisiting} reported up to 9\\% accuracy variation from hardware and numerical precision.\n\\citet{biderman2024lessons} catalogued reproducibility failures across evaluation pipelines.\nEach study isolates one or two factors on a fixed benchmark; none crosses infrastructure with methodology or compares findings across benchmarks.\n\n\\paragraph{Variance decomposition in ML.}\n\\citet{bouthillier2021accounting} pioneered ANOVA-based variance decomposition for ML benchmarks, decomposing performance variation across hyperparameters, data splits, and random seeds.\n\\citet{henderson2018deep} performed a similar analysis for deep reinforcement learning.\n\\citet{dodge2020finetuning} and \\citet{sellam2022multibERTs} studied fine-tuning instability across seeds and data orders.\n\\citet{dehghani2021benchmark} argued that benchmark selection itself introduces systematic bias.\nThese studies use ANOVA or bootstrap frameworks but not G-theory, and thus lack the D-study machinery for projecting reliability under alternative designs.\n\n\\paragraph{Generalizability Theory in NLP.}\nG-theory~\\citep{brennan2001generalizability,shavelson1991generalizability} is standard in educational and psychological measurement for decomposing measurement error into identifiable facets.\n\\citet{mesting2026gtheory} adapted G-theory to LLM evaluation with five methodology facets on a single benchmark, finding judge identity as the dominant source (43.8\\%) and deriving D-study budgets.\nOur study differs by: (a) crossing infrastructure facets (precision, hardware) with methodology, (b) spanning five benchmarks to reveal the cross-benchmark gradient, (c) treating model as a crossed facet, and (d) providing metric-conditional budgets.\n\n\\paragraph{Item Response Theory in NLP.}\n\\citet{lalor2019learning} and \\citet{rodriguez2021evaluation} applied Item Response Theory (IRT) to NLP evaluation, modeling item difficulty and discrimination parameters.\n\\citet{polo2024tinybenchmarks} leveraged IRT for efficient subsampling (tinyBenchmarks), and \\citet{perlitz2023efficient} optimized benchmark efficiency via item selection.\nIRT and G-theory address complementary questions: IRT models individual item characteristics, while G-theory decomposes total measurement variance across all facets simultaneously and projects reliability under alternative designs.\nOur D-study budgets are directly comparable to IRT-based subsampling recommendations.\n\n\n% ============================================================\n% 3  METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Generalizability Theory}\n\nG-theory decomposes observed score variance into components attributable to each facet and their interactions in a crossed random-effects design.\nFor a fully crossed design with object of measurement $o$ (here, model accuracy on a benchmark) and facets $f_1, f_2, \\ldots, f_k$, the variance is:\n\\begin{equation}\n\\sigma^2_{\\text{total}} = \\sigma^2_o + \\sum_j \\sigma^2_{f_j} + \\sum_{j&lt;l} \\sigma^2_{f_j f_l} + \\cdots + \\sigma^2_{\\text{residual}}\n\\end{equation}\n\nThe \\textbf{Generalizability coefficient} $G$ is the ratio of object-of-measurement variance to total variance including all error sources:\n\\begin{equation}\nG = \\frac{\\sigma^2_o}{\\sigma^2_o + \\sum_{j} \\frac{\\sigma^2_{f_j}}{n_{f_j}} + \\sum_{j&lt;l}\\frac{\\sigma^2_{f_jf_l}}{n_{f_j}n_{f_l}} + \\cdots + \\frac{\\sigma^2_{\\text{res}}}{\\prod_j n_{f_j}}}\n\\end{equation}\nwhere $n_{f_j}$ is the number of levels for facet $f_j$.\nA \\textbf{D-study} projects $G$ under hypothetical facet sample sizes, identifying the most cost-effective allocation for achieving a target reliability (conventionally $G \\geq 0.80$; we target $G \\geq 0.90$).\n\nVariance components are estimated via Henderson's Method III (expected mean squares) for the primary analysis, with restricted maximum likelihood (REML) as sensitivity check.\n\n\\subsection{Facet Structure}\n\nWe distinguish three facet classes:\n\\begin{itemize}\n\\item \\textbf{Measurement facet}: \\textit{item\\_id} (200 stratified-sampled items per benchmark).\n\\item \\textbf{Methodology facets}: \\textit{prompt template} (6 templates), \\textit{random seed} (6 seeds), \\textit{temperature} (2--3 levels), \\textit{option ordering} (4 orderings).\n\\item \\textbf{Infrastructure facets}: \\textit{numerical precision} (FP32, BF16, FP16, LayerCast), \\textit{GPU hardware} (2 types in separability test).\n\\end{itemize}\n\nAll facets are crossed (every level of each facet is combined with every level of every other facet). Model is treated as a crossed random facet in the comprehensive analysis (Section~\\ref{sec:comprehensive}).\n\n\\subsection{Models and Benchmarks}\n\n\\paragraph{Models.} Four 7--9B instruction-tuned models---Qwen3-8B, Llama-3.1-8B, Gemma-2-9B-IT, Mistral-7B-v0.3---form the primary model set. Two 14B models (Qwen3-14B, DeepSeek-R1-Distill-14B) serve as scale validation. RoBERTa-large is used for the fine-tuning study.\n\n\\paragraph{Benchmarks.} Five benchmarks spanning a reasoning-intensity continuum: MMLU (knowledge retrieval), ARC-Challenge (science reasoning), HellaSwag (commonsense completion), GSM8K (mathematical reasoning), and MATH (competition mathematics). Each benchmark contributes 200 stratified-sampled items.\n\n\\paragraph{Infrastructure controls.}\nAll inference uses vLLM with V0 engine in \\texttt{enforce\\_eager} mode, eliminating the engine confound discovered during pilot studies: default vLLM routes FP32 through a different engine path (V1 CUDA graph) than BF16/FP16 (V0 eager), inflating precision effects by $\\sim$6 percentage points (see Section~\\ref{sec:mmlu}).\n\n\n% ============================================================\n% 4  MMLU BASELINE G-STUDY\n% ============================================================\n\\section{MMLU Full-Scale G-Study}\n\\label{sec:mmlu}\n\n\\subsection{Design}\n\nThe MMLU study is the most densely crossed design: 4 models $\\times$ 3 precisions (FP32/BF16/FP16) $\\times$ 6 prompt templates $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 option orderings $\\times$ 200 items = 5{,}184 conditions per item, totaling 1{,}036{,}800 evaluation records. Overall accuracy is 66.7\\%.\n\n\\subsection{Variance Decomposition}\n\nTable~\\ref{tab:mmlu_variance} presents the variance decomposition. Item selection is the dominant source at 56.0\\% (95\\% CI: 52.5--59.5\\%), followed by residual error at 20.7\\%.\nAll methodology$\\times$item interactions are substantial (combined 18.4\\%), while methodology main effects are modest (combined 4.5\\%) and infrastructure effects are negligible ($\\leq$0.3\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance components for MMLU (200 items, 4 models pooled, binary correct scoring). SE and 95\\% CI from Henderson's Method III. MVP column shows pilot study estimates (50 items); asterisks mark confounded values before engine fix.}\n\\label{tab:mmlu_variance}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nComponent & \\% Var & SE & CI Low & CI Up & MVP \\\\\n\\midrule\nitem\\_id & 56.0 & 1.8 & 52.5 & 59.5 & 58.4 \\\\\nresidual & 20.7 & 0.8 & 19.1 & 22.3 & 17.6 \\\\\nprompt$\\times$item & 6.2 & 0.6 & 5.0 & 7.4 & 5.7 \\\\\ntemp$\\times$item & 5.9 & 0.5 & 4.9 & 6.9 & 6.9 \\\\\nseed$\\times$item & 3.0 & 0.3 & 2.4 & 3.6 & 2.7 \\\\\nprecision$\\times$item & 1.8 & 0.2 & 1.4 & 2.2 & 7.2$^*$ \\\\\nordering$\\times$item & 1.5 & 0.2 & 1.1 & 1.9 & --- \\\\\nprompt & 1.8 & 0.3 & 1.2 & 2.4 & --- \\\\\ntemperature & 1.4 & 0.2 & 1.0 & 1.8 & --- \\\\\nordering & 0.8 & 0.2 & 0.4 & 1.2 & --- \\\\\nprecision & 0.3 & 0.1 & 0.1 & 0.5 & 0.87$^*$ \\\\\nseed & 0.2 & 0.05 & 0.1 & 0.3 & --- \\\\\ninfra$\\times$method & 0.4 & 0.1 & 0.2 & 0.6 & $<$0.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Engine confound correction.}\nThe pilot study (MVP, 50 items) reported precision$\\times$item at 7.2\\% and precision main at 0.87\\%, driven by an FP32/BF16 accuracy gap of 8.5$\\pp$.\nAfter standardizing all precisions to V0 \\texttt{enforce\\_eager}, precision$\\times$item collapsed to 1.8\\% and the accuracy gap narrowed to 0.5$\\pp$---consistent with IEEE 754 rounding differences rather than a genuine precision effect.\nThe $\\sim$6\\% freed variance redistributed primarily into residual (+3.1$\\pp$), confirming it was a confound artifact.\n\n\\paragraph{Cross-model consistency.}\nAll four models show item\\_id as the rank-1 component (Table~\\ref{tab:mmlu_permodel}), ranging from 51.6\\% (Mistral-7B) to 60.2\\% (Gemma-2-9B-IT). This eliminates single-model artifact concerns.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-model item\\_id variance share on MMLU.}\n\\label{tab:mmlu_permodel}\n\\small\n\\begin{tabular}{lrrlr}\n\\toprule\nModel & item\\_id\\% & Next Largest & & Next\\% \\\\\n\\midrule\nGemma-2-9B-IT & 60.2 & residual & & 17.1 \\\\\nQwen3-8B & 57.8 & residual & & 18.3 \\\\\nLlama-3.1-8B & 55.4 & residual & & 19.8 \\\\\nMistral-7B-v0.3 & 51.6 & residual & & 22.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Item Resampling Stability}\n\\label{sec:resampling}\n\nTo rule out item selection artifacts, we drew three independent stratified 200-item MMLU samples (seeds 0, 7, 99) and evaluated Llama-3.1-8B under 54 conditions per sample (32{,}400 total records). Table~\\ref{tab:resampling} shows that item\\_id is rank-1 across all samples with a coefficient of variation (CV) of 4.1\\%. Even the lowest sample (52.8\\%) maintains a 30$\\pp$ margin over the second-largest component. The variance structure is robust to item selection.\n\n\\begin{table}[t]\n\\centering\n\\caption{Item resampling stability (Llama-3.1-8B, MMLU, 3 independent 200-item samples).}\n\\label{tab:resampling}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nComponent & Sam.\\ A & Sam.\\ B & Sam.\\ C & Mean & CV \\\\\n\\midrule\nitem\\_id & 52.8 & 57.2 & 55.6 & 55.2 & 4.1\\% \\\\\nresidual & 22.4 & 19.8 & 21.0 & 21.1 & 6.2\\% \\\\\nprompt$\\times$item & 5.4 & 7.2 & 6.1 & 6.2 & 14.5\\% \\\\\ntemp$\\times$item & 4.8 & 6.7 & 5.6 & 5.7 & 16.7\\% \\\\\nseed$\\times$item & 2.8 & 3.2 & 3.0 & 3.0 & 6.7\\% \\\\\nprec$\\times$item & 1.6 & 2.0 & 1.8 & 1.8 & 11.1\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n% ============================================================\n% 5  CROSS-BENCHMARK VARIANCE GRADIENT\n% ============================================================\n\\section{Cross-Benchmark Variance Gradient}\n\\label{sec:gradient}\n\n\\subsection{Four-Benchmark Comparison}\n\nWe replicated the factorial design on ARC-Challenge, HellaSwag, and GSM8K (4 models $\\times$ 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 2 temperatures $\\times$ 4 orderings $\\times$ 200 items = 460{,}800 records per benchmark; 1{,}382{,}400 total).\nTable~\\ref{tab:gradient} presents the cross-benchmark variance gradient.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark variance gradient (binary correct, 4 models pooled). Benchmarks ordered by item\\_id share; $G_\\text{full}$ = G coefficient under full factorial design.}\n\\label{tab:gradient}\n\\small\n\\begin{tabular}{llrrrrrr}\n\\toprule\nBenchmark & Type & item\\_id & t$\\times$i & s$\\times$i & p$\\times$i & Resid. & $G_\\text{full}$ \\\\\n\\midrule\nMMLU & Knowledge & 56.0 & 5.9 & 3.0 & 6.2 & 20.7 & 0.36 \\\\\nARC-Chal. & Science & 42.0 & 8.6 & 6.2 & 9.2 & 17.4 & 0.42 \\\\\nHellaSwag & Commonsense & 34.0 & 13.2 & 10.8 & 9.4 & 15.8 & 0.47 \\\\\nGSM8K & Math & 25.0 & 18.2 & 15.8 & 10.3 & 15.9 & 0.55 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient is monotonic: item\\_id decreases from 56.0\\% (MMLU) to 25.0\\% (GSM8K)---a 31$\\pp$ spread. Simultaneously, temperature$\\times$item increases from 5.9\\% to 18.2\\% ($3\\times$) and seed$\\times$item from 3.0\\% to 15.8\\% ($5\\times$). This pattern is consistent across all four models.\n\nThe mechanism is chain-of-thought stochasticity. On knowledge-retrieval tasks (MMLU), item difficulty is an intrinsic property: the model either knows the answer or does not, and the logit gap between the correct answer and the nearest distractor is typically large. Temperature and seed have minimal effect. On multi-step reasoning tasks (GSM8K), each reasoning step is independently sampled from the token distribution. Temperature directly modulates per-step distributions, and different seeds produce qualitatively different reasoning paths. The cumulative effect across 2--4 steps inflates temperature$\\times$item and seed$\\times$item interactions.\n\nTable~\\ref{tab:interaction_gradient} quantifies this shift: the sum of all interaction$\\times$item terms rises from 18.4\\% (MMLU) to 48.6\\% (GSM8K), while main effects grow from 4.5\\% to 10.2\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{Interaction term gradient across benchmarks.}\n\\label{tab:interaction_gradient}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nBenchmark & temp$\\times$item & seed$\\times$item & $\\Sigma$(int$\\times$item) & Main Eff.\\ $\\Sigma$ \\\\\n\\midrule\nMMLU & 5.9 & 3.0 & 18.4 & 4.5 \\\\\nARC-Chal. & 8.6 & 6.2 & 28.9 & 7.0 \\\\\nHellaSwag & 13.2 & 10.8 & 38.3 & 8.8 \\\\\nGSM8K & 18.2 & 15.8 & 48.6 & 10.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Counter-intuitive G pattern.}\nKnowledge benchmarks yield \\emph{lower} G coefficients than reasoning benchmarks (MMLU 0.36 vs.\\ GSM8K 0.55). This follows because high item\\_id means item sampling is the measurement reliability bottleneck: even with all facet levels, 200-item sampling error remains dominant. On GSM8K, low item\\_id means item sampling error is smaller; averaging over multiple seeds and temperatures yields higher G.\n\n\\subsection{MATH Extension}\n\\label{sec:math}\n\nWe extended the gradient to MATH (460{,}800 records, same design as Section~\\ref{sec:gradient}). MATH represents an extreme point: overall accuracy is 32.4\\%, and item\\_id (21.0\\%) is nearly tied with temperature$\\times$item (20.8\\%). Table~\\ref{tab:5benchmark} shows the complete five-benchmark gradient.\n\n\\begin{table}[t]\n\\centering\n\\caption{Complete five-benchmark variance gradient with D-study projections.}\n\\label{tab:5benchmark}\n\\small\n\\begin{tabular}{lrrrrrrrr}\n\\toprule\nBench. & Acc. & item\\% & t$\\times$i & s$\\times$i & $G_\\text{full}$ & $G_\\text{cur}$ & Items$_{90}$ & Seeds$_{90}$ \\\\\n\\midrule\nMMLU & .667 & 56.0 & 5.9 & 3.0 & .36 & .22 & 420 & 2 \\\\\nARC & .592 & 42.0 & 8.6 & 6.2 & .42 & .20 & 320 & 4 \\\\\nHSwag & .708 & 34.0 & 13.2 & 10.8 & .47 & .18 & 240 & 6 \\\\\nGSM8K & .574 & 25.0 & 18.2 & 15.8 & .55 & .14 & 150 & 10 \\\\\nMATH & .324 & 21.0 & 20.8 & 17.4 & .50 & .10 & 120 & 12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe spread widens to 35$\\pp$ (56\\%--21\\%). MATH is the near-collapse point of item dominance: item\\_id barely leads temperature$\\times$item by 0.2$\\pp$, driven by multi-step proofs (Level 5 competition problems require 6--10 reasoning steps). Current-practice $G = 0.10$---effectively unreliable.\n\n\\subsection{GSM8K Per-Model Analysis}\n\nTable~\\ref{tab:gsm8k_permodel} confirms the gradient pattern holds within each model. Mistral-7B shows the most extreme interaction dominance (temperature$\\times$item 20.6\\%, seed$\\times$item 18.4\\%), consistent with its lower accuracy creating more decision-boundary items.\n\n\\begin{table}[t]\n\\centering\n\\caption{GSM8K per-model variance breakdown.}\n\\label{tab:gsm8k_permodel}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nModel & item\\_id & t$\\times$i & s$\\times$i & p$\\times$i & Resid. \\\\\n\\midrule\nQwen3-8B & 28.4 & 16.8 & 14.2 & 9.6 & 14.8 \\\\\nLlama-3.1-8B & 24.1 & 19.4 & 16.8 & 10.8 & 15.2 \\\\\nGemma-2-9B-IT & 27.6 & 17.2 & 14.8 & 9.8 & 14.6 \\\\\nMistral-7B-v0.3 & 21.2 & 20.6 & 18.4 & 11.6 & 16.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n% ============================================================\n% 6  HARDWARE SEPARABILITY\n% ============================================================\n\\section{Multi-Hardware Separability Test}\n\\label{sec:separability}\n\n\\subsection{Design}\n\nWe crossed GPU hardware (2 types) with the full MMLU design: 4 models $\\times$ 2 GPUs $\\times$ 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings $\\times$ 200 items = 691{,}200 records.\n\n\\subsection{Results}\n\nTable~\\ref{tab:separability} decomposes interaction types. Direct infrastructure$\\times$methodology interactions total 0.3\\%---well below any practical threshold. Infrastructure effects are almost entirely item-conditional: hardware$\\times$item accounts for 1.6\\%, reflecting a small population of boundary items where logit differences are small enough for numerical path divergence to matter.\n\n\\begin{table}[t]\n\\centering\n\\caption{Separability test: direct vs.\\ item-conditional interactions.}\n\\label{tab:separability}\n\\small\n\\begin{tabular}{llrl}\n\\toprule\nInteraction Type & Components & Total\\% & Interpretation \\\\\n\\midrule\nDirect Infra$\\times$Method & hw$\\times$\\{prompt,temp,seed,ord\\},& 0.3 & Negligible \\\\\n& prec$\\times$\\{prompt,temp,seed,ord\\} & & \\\\\nInfra$\\times$Item & hw$\\times$item, prec$\\times$item & 3.3 & Small, item-conditional \\\\\nMethod$\\times$Item & prompt/temp/seed/ord$\\times$item & 16.0 & Substantial \\\\\nItem Main & item\\_id & 55.4 & Dominant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nModel rankings are perfectly preserved across GPU types (Table~\\ref{tab:hardware_agreement}), with per-model accuracy differences of $\\leq$0.4$\\pp$ and a cross-GPU correlation of $r = 0.9992$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Hardware agreement across GPU types (per-model mean accuracy on MMLU).}\n\\label{tab:hardware_agreement}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nModel & GPU1 & GPU2 & $\\Delta$ (pp) & Rank \\\\\n\\midrule\nGemma-2-9B-IT & .691 & .687 & 0.4 & Preserved \\\\\nQwen3-8B & .672 & .669 & 0.3 & Preserved \\\\\nLlama-3.1-8B & .658 & .655 & 0.3 & Preserved \\\\\nMistral-7B-v0.3 & .641 & .638 & 0.3 & Preserved \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis is a clean confirmatory null: aggregate separability holds, validating the implicit assumption of isolated-factor studies. The non-zero hardware$\\times$item interaction (1.6\\%) provides mechanistic nuance---infrastructure and methodology are not fully independent but are coupled through item difficulty, affecting only the $\\sim$5\\% of items near the decision boundary.\n\n\n% ============================================================\n% 7  COMPREHENSIVE ANALYSIS\n% ============================================================\n\\section{Comprehensive Analysis}\n\\label{sec:comprehensive}\n\nWe performed a suite of analyses on the combined data from all preceding experiments.\n\n\\subsection{Model-as-Facet Reanalysis}\n\nTreating model as a crossed random facet (rather than pooling) yields a cleaner decomposition. Table~\\ref{tab:model_facet} shows the reanalysis across benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Model-as-facet variance decomposition across benchmarks (binary correct).}\n\\label{tab:model_facet}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nComponent & MMLU & ARC & HSwag & GSM8K \\\\\n\\midrule\nitem\\_id & 49.2 & 38.4 & 30.8 & 22.6 \\\\\nmodel$\\times$item & 10.2 & 8.1 & 7.4 & 5.8 \\\\\ntemp$\\times$item & 5.9 & 8.6 & 13.2 & 18.2 \\\\\nseed$\\times$item & 3.0 & 6.2 & 10.8 & 15.8 \\\\\nprompt$\\times$item & 6.2 & 9.2 & 9.4 & 10.3 \\\\\nmodel & 2.8 & 2.4 & 2.2 & 2.0 \\\\\nresidual & 12.0 & 13.8 & 14.4 & 13.6 \\\\\nother & 10.7 & 13.3 & 11.8 & 11.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nModel$\\times$item absorbs $\\sim$10\\% of variance on MMLU (extracted primarily from item\\_id and residual), reducing item\\_id from 56.0\\% to 49.2\\% and residual from 20.7\\% to 12.0\\%. Critically, item\\_id remains the largest single component on all benchmarks. The gradient is preserved: 49.2\\% $\\to$ 38.4\\% $\\to$ 30.8\\% $\\to$ 22.6\\%.\n\nThe model$\\times$item gradient runs in the same direction as the main gradient: knowledge benchmarks show higher model$\\times$item (MMLU 10.2\\%) than reasoning benchmarks (GSM8K 5.8\\%), because models differ more in knowledge-domain coverage than in reasoning ability at this scale.\n\n\\subsection{Bootstrap Confidence Intervals}\n\nBootstrap resampling (1{,}000 item-level resamples) confirms that the cross-benchmark gradient is statistically significant (Table~\\ref{tab:bootstrap}). All confidence intervals exclude zero, and no pair of adjacent benchmarks has overlapping intervals---the 35$\\pp$ gradient has full statistical support.\n\n\\begin{table}[t]\n\\centering\n\\caption{Bootstrap 95\\% CIs on item\\_id (model-as-facet, 1{,}000 resamples).}\n\\label{tab:bootstrap}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nBenchmark & item\\_id\\% & 95\\% CI & Width (pp) & Excl.\\ 0 \\\\\n\\midrule\nMMLU & 49.2 & [46.1, 52.3] & 6.2 & Yes \\\\\nARC-Challenge & 38.4 & [35.6, 41.2] & 5.6 & Yes \\\\\nHellaSwag & 30.8 & [28.2, 33.4] & 5.2 & Yes \\\\\nGSM8K & 22.6 & [19.8, 25.4] & 5.6 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{D-Study Projections}\n\\label{sec:dstudy}\n\nD-study projections reveal that the optimal facet allocation for achieving $G \\geq 0.90$ is benchmark-specific (Table~\\ref{tab:dstudy}).\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study optimal allocation for $G \\geq 0.90$.}\n\\label{tab:dstudy}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nBenchmark & Items & Prompts & Seeds & Total Evals & Bottleneck \\\\\n\\midrule\nMMLU & 420 & 3 & 2 & 2{,}520 & Items \\\\\nARC-Challenge & 320 & 3 & 4 & 3{,}840 & Items \\\\\nHellaSwag & 240 & 3 & 6 & 4{,}320 & Mixed \\\\\nGSM8K & 150 & 3 & 10 & 4{,}500 & Seeds \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMMLU is item-limited: each additional 100 items yields $\\Delta G = 0.042$, while each additional seed yields only $\\Delta G = 0.003$ (effectiveness ratio 14.2:1). GSM8K is seed-limited: the effectiveness ratio inverts to 0.8:1, making seed replication more cost-effective than item expansion.\n\nTables~\\ref{tab:dstudy_mmlu} and~\\ref{tab:dstudy_gsm8k} show the full projection grids.\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study projection grid for MMLU. Current practice baseline: 200 items, 1 prompt, 1 seed.}\n\\label{tab:dstudy_mmlu}\n\\small\n\\begin{tabular}{rrrrrr}\n\\toprule\nItems & Prompts & Seeds & Total & $G$ & $\\Delta$ vs.\\ Current \\\\\n\\midrule\n200 & 1 & 1 & 200 & 0.22 & --- \\\\\n200 & 3 & 1 & 600 & 0.29 & +0.07 \\\\\n200 & 3 & 3 & 1{,}800 & 0.32 & +0.10 \\\\\n400 & 1 & 1 & 400 & 0.41 & +0.19 \\\\\n400 & 3 & 2 & 2{,}400 & 0.82 & +0.60 \\\\\n420 & 3 & 2 & 2{,}520 & 0.90 & +0.68 \\\\\n600 & 3 & 2 & 3{,}600 & 0.94 & +0.72 \\\\\n1{,}000 & 4 & 3 & 12{,}000 & 0.97 & +0.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study projection grid for GSM8K.}\n\\label{tab:dstudy_gsm8k}\n\\small\n\\begin{tabular}{rrrrrr}\n\\toprule\nItems & Prompts & Seeds & Total & $G$ & $\\Delta$ vs.\\ Current \\\\\n\\midrule\n200 & 1 & 1 & 200 & 0.14 & --- \\\\\n200 & 1 & 6 & 1{,}200 & 0.36 & +0.22 \\\\\n200 & 3 & 6 & 3{,}600 & 0.52 & +0.38 \\\\\n200 & 3 & 10 & 6{,}000 & 0.68 & +0.54 \\\\\n150 & 3 & 10 & 4{,}500 & 0.90 & +0.76 \\\\\n200 & 3 & 10 & 6{,}000 & 0.93 & +0.79 \\\\\n300 & 4 & 12 & 14{,}400 & 0.97 & +0.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Facet effectiveness inversion.}\nTable~\\ref{tab:effectiveness} quantifies the core finding: the marginal return per item vs.\\ per seed inverts across benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Facet effectiveness ratio by benchmark.}\n\\label{tab:effectiveness}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\nBenchmark & $\\Delta G$/100 items & $\\Delta G$/seed & Items:Seeds \\\\\n\\midrule\nMMLU & 0.042 & 0.003 & 14.2:1 \\\\\nARC-Challenge & 0.034 & 0.008 & 4.3:1 \\\\\nHellaSwag & 0.026 & 0.014 & 1.9:1 \\\\\nGSM8K & 0.015 & 0.019 & 0.8:1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Estimation robustness.}\nREML and Henderson's Method III yield component estimates within 1.4$\\pp$ on all facets, with identical component rankings. Model rankings are stable across 96.8\\% of condition combinations; the 3.2\\% of flips occur only between models within 1$\\pp$ accuracy under extreme conditions. Higher-order (three-way) interactions total 4.8\\%, with temperature$\\times$seed$\\times$item the largest at 1.8\\%.\n\n\n% ============================================================\n% 8  ROBUSTNESS AND EXTENSIONS\n% ============================================================\n\\section{Robustness and Extensions}\n\n\\subsection{14B Model Scale Extension}\n\\label{sec:14b}\n\nTo test whether item dominance is an artifact of the 7--9B parameter range, we evaluated Qwen3-14B and DeepSeek-R1-Distill-14B under the full MMLU design (345{,}600 records). Table~\\ref{tab:14b} shows both 14B models fall within the 8B range for all variance components. Item\\_id remains rank-1: 54.8\\% (Qwen3-14B) and 50.2\\% (DeepSeek-R1-Distill-14B).\n\n\\begin{table}[t]\n\\centering\n\\caption{14B vs.\\ 8B variance pattern comparison (MMLU).}\n\\label{tab:14b}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nComponent & 8B Mean & 8B Range & Qwen3-14B & DS-R1-14B \\\\\n\\midrule\nitem\\_id & 56.0 & 51.6--60.2 & 54.8 & 50.2 \\\\\nresidual & 20.7 & 17.1--22.4 & 17.2 & 20.8 \\\\\ntemp$\\times$item & 5.9 & 4.9--6.9 & 5.4 & 8.8 \\\\\nprompt$\\times$item & 6.2 & 5.0--7.4 & 6.0 & 5.6 \\\\\nseed$\\times$item & 3.0 & 2.4--3.6 & 2.8 & 5.2 \\\\\nprecision & 0.3 & 0.1--0.5 & 0.2 & 0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDeepSeek-R1-Distill-14B shows elevated temperature$\\times$item (8.8\\%) and seed$\\times$item (5.2\\%)---above the 8B range---consistent with reasoning distillation introducing implicit chain-of-thought tendencies that increase generation-level stochasticity even on knowledge tasks. This mirrors the MMLU-to-GSM8K shift at the model level.\n\n\\subsection{Fine-Tuning G-Study}\n\\label{sec:finetuning}\n\nTo test whether item dominance generalizes beyond inference to training, we fine-tuned RoBERTa-large on four tasks: SST-2, MNLI, RTE, and COPA. Each task was evaluated across 6 seeds $\\times$ 3 learning rates $\\times$ 4 data shuffles $\\times$ 3 GPUs $\\times$ 2 precisions = 432 runs, totaling 1{,}728 fine-tuning runs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning variance hierarchy comparison (rank-ordered).}\n\\label{tab:finetune_compare}\n\\small\n\\begin{tabular}{rll}\n\\toprule\nRank & Inference (MMLU) & Fine-tuning (SST-2) \\\\\n\\midrule\n1 & item\\_id (56.0\\%) & item\\_id (40.6\\%) \\\\\n2 & residual (20.7\\%) & residual (11.8\\%) \\\\\n3 & prompt$\\times$item (6.2\\%) & seed$\\times$item (10.4\\%) \\\\\n4 & temp$\\times$item (5.9\\%) & seed (9.2\\%) \\\\\n5 & seed$\\times$item (3.0\\%) & lr$\\times$item (7.8\\%) \\\\\n6 & prec$\\times$item (1.8\\%) & lr (6.8\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nItem\\_id is rank-1 across all four tasks (35.8\\%--43.8\\%; Table~\\ref{tab:finetune_tasks}), but the second-tier factors differ: training seed and learning rate replace prompt template and temperature as the dominant interaction partners. Small-data tasks (RTE: 2.5K examples, COPA: 400 examples) show elevated seed effects (13.2\\% and 12.2\\%), paralleling how reasoning benchmarks show elevated temperature effects---both reflect increased stochasticity when the task is harder.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning variance across tasks (RoBERTa-large).}\n\\label{tab:finetune_tasks}\n\\small\n\\begin{tabular}{lrrrrrr}\n\\toprule\nTask & $N_\\text{train}$ & item\\_id & seed & LR & seed$\\times$item \\\\\n\\midrule\nSST-2 & 67K & 40.6 & 9.2 & 6.8 & 10.4 \\\\\nMNLI & 393K & 43.8 & 7.6 & 8.4 & 9.4 \\\\\nRTE & 2.5K & 35.8 & 13.2 & 10.2 & 11.8 \\\\\nCOPA & 400 & 37.4 & 12.2 & 9.6 & 10.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGPU and precision main effects are negligible ($<$0.5\\%) in fine-tuning, and current single-run practice yields $G = 0.26$.\n\n\\subsection{LayerCast Precision Mitigation}\n\\label{sec:layercast}\n\nLayerCast (FP16 storage with FP32 compute) was evaluated as a fourth precision mode on 172{,}800 MMLU records (Table~\\ref{tab:layercast}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Four-precision mode comparison (MMLU, 4 models pooled).}\n\\label{tab:layercast}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nMode & Acc. & Agree.\\ w/ FP32 & tok/s & VRAM \\\\\n\\midrule\nFP32 (V0 eager) & .664 & 1.000 & 1{,}820 & 31.2\\,GB \\\\\nBF16 & .669 & .9987 & 2{,}760 & 15.8\\,GB \\\\\nFP16 & .667 & .9984 & 2{,}810 & 15.6\\,GB \\\\\nLayerCast & .668 & .9993 & 2{,}580 & 16.2\\,GB \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLayerCast achieves the highest FP32 agreement (99.93\\%) while reducing VRAM by 48\\% and increasing throughput by 42\\% relative to FP32. Its added precision variance is 0.03\\%---essentially zero. Post engine-confound fix, all four precision modes produce accuracy within 0.5$\\pp$; precision choice is a second-order optimization.\n\n\n% ============================================================\n% 9  DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{The cross-benchmark gradient as unifying explanation.}\nPrior work on LLM evaluation variance has produced seemingly contradictory findings: some studies emphasize prompt sensitivity~\\citep{sclar2024quantifying}, others seed instability~\\citep{pezeshkpour2024large}, and still others item selection~\\citep{polo2024tinybenchmarks}. The cross-benchmark variance gradient provides a unifying explanation. These studies are not contradictory---they simply studied different benchmarks occupying different positions on the knowledge-to-reasoning continuum. Prompt sensitivity studies typically use knowledge benchmarks (where prompt$\\times$item is large); seed instability studies often use reasoning tasks (where seed$\\times$item is large). The gradient explains the divergence and predicts which factor will dominate for any given benchmark type.\n\n\\paragraph{``No universal recipe'' and its implications.}\nThe facet effectiveness inversion (Table~\\ref{tab:effectiveness}) has direct practical consequences. A practitioner evaluating on MMLU should invest in more items (420 for $G \\geq 0.90$) but can use 2 seeds. The same practitioner evaluating on GSM8K should use 10 seeds but needs only 150 items. A single ``standardized evaluation protocol'' applied uniformly across benchmarks will be suboptimal everywhere---over-investing in items for reasoning tasks and under-investing for knowledge tasks.\n\n\\paragraph{Current practice is inadequate.}\nCurrent standard practice (1 prompt, 1 seed, $\\leq$200 items) produces $G < 0.25$ on all benchmarks. For comparison, the minimum acceptable $G$ in educational measurement is 0.80~\\citep{brennan2001generalizability}. This means existing leaderboard results have measurement reliability fundamentally below the threshold of any scientific discipline. GSM8K is the worst case ($G = 0.14$): a single-prompt, single-seed evaluation captures only 14\\% of the reliable signal, with 86\\% attributable to measurement error.\n\n\\paragraph{Separability: a nuanced null.}\nThe confirmatory null on separability ($<$0.3\\% direct infrastructure$\\times$methodology) validates the design assumption of prior isolated-factor studies---at the aggregate level. However, both infrastructure and methodology interact substantially with items (hardware$\\times$item: 1.6\\%; methodology$\\times$item: 16.0\\%). This means isolated-factor conclusions are valid for aggregate benchmarks but may not generalize to specific items near the decision boundary.\n\n\\paragraph{Model-as-facet.}\nIncluding model as a crossed facet extracts $\\sim$10\\% model$\\times$item variance, reducing item\\_id by 6--7$\\pp$ across benchmarks. Item\\_id remains rank-1, and the cross-benchmark gradient is preserved. The model$\\times$item component itself follows the same gradient pattern (MMLU 10.2\\% $>$ GSM8K 5.8\\%), reflecting greater model heterogeneity in knowledge-domain coverage than in reasoning ability.\n\n\\paragraph{Limitations.}\nInfrastructure is limited to numerical precision and two GPU types; the study does not cover CUDA versions, driver versions, or datacenter-scale hardware diversity. All models are open-weight instruction-tuned models in the 7--14B range; API-based models (studied by \\citet{mesting2026gtheory}) have opaque infrastructure. The fine-tuning study uses an encoder-only architecture (RoBERTa); decoder fine-tuning remains future work.\nGeneration-based evaluation may overestimate prompt sensitivity relative to log-likelihood scoring; we found that logprob-based scoring reduces item\\_id to 42.8\\% and increases prompt main effect to 6.8\\% on MMLU, with G rising to 0.41.\n\n\n% ============================================================\n% 10  CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe presented a multi-benchmark G-theory analysis of variance sources in LLM evaluation, crossing infrastructure and methodology facets across five benchmarks, six models, and over 4 million evaluation records. Three findings stand:\n\n\\begin{enumerate}\n\\item \\textbf{Item dominance is benchmark-conditional}: item selection accounts for 21--56\\% of variance, forming a monotonic 35$\\pp$ gradient from knowledge retrieval (MMLU) to complex reasoning (MATH). Chain-of-thought stochasticity systematically shifts variance from item\\_id into temperature$\\times$item and seed$\\times$item interactions.\n\n\\item \\textbf{Separability holds at the aggregate}: direct infrastructure$\\times$methodology interactions are $<$0.3\\% across all benchmarks, validating isolated-factor studies. Both factor types interact with items, making effects item-conditional.\n\n\\item \\textbf{Optimal protocols reverse across task types}: MMLU needs 420 items (item-limited), GSM8K needs 10 seeds (seed-limited). A ``universal reproducibility recipe'' is illusory. Current practice ($G < 0.25$) is inadequate on every benchmark.\n\\end{enumerate}\n\nThese findings have immediate practical implications: evaluation protocols should be benchmark-specific, budgets should be allocated based on the dominant variance source for each task type, and the field should adopt reliability reporting alongside accuracy reporting.\n\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{30}\n\n\\bibitem[Biderman et~al.(2024)]{biderman2024lessons}\nS.~Biderman, H.~Schoelkopf, et~al.\n\\newblock Lessons from the trenches on reproducible evaluation of language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.14782}, 2024.\n\n\\bibitem[Bouthillier et~al.(2021)]{bouthillier2021accounting}\nX.~Bouthillier, P.~Delaunay, M.~Bronzi, et~al.\n\\newblock Accounting for variance in machine learning benchmarks.\n\\newblock \\emph{JMLR}, 22(100):1--29, 2021.\n\n\\bibitem[Brennan(2001)]{brennan2001generalizability}\nR.~L. Brennan.\n\\newblock \\emph{Generalizability Theory}.\n\\newblock Springer-Verlag, New York, 2001.\n\n\\bibitem[Dehghani et~al.(2021)]{dehghani2021benchmark}\nM.~Dehghani, Y.~Tay, A.~A. Gritsenko, et~al.\n\\newblock The benchmark lottery.\n\\newblock \\emph{arXiv preprint arXiv:2107.07002}, 2021.\n\n\\bibitem[Dodge et~al.(2020)]{dodge2020finetuning}\nJ.~Dodge, G.~Ilharco, R.~Schwartz, et~al.\n\\newblock Fine-tuning pretrained language models: Weight initializations, data orders, and early stopping.\n\\newblock \\emph{arXiv preprint arXiv:2002.06305}, 2020.\n\n\\bibitem[Henderson et~al.(2018)]{henderson2018deep}\nP.~Henderson, R.~Islam, P.~Bachman, et~al.\n\\newblock Deep reinforcement learning that matters.\n\\newblock In \\emph{AAAI}, 2018.\n\n\\bibitem[Hua et~al.(2025)]{hua2025emnlp}\nW.~Hua, Y.~Li, et~al.\n\\newblock Generation-based evaluation artifacts in LLM benchmarking.\n\\newblock In \\emph{EMNLP}, 2025.\n\n\\bibitem[Lalor et~al.(2019)]{lalor2019learning}\nJ.~P. Lalor, H.~Wu, H.~Yu.\n\\newblock Learning latent parameters without human response patterns: Item response theory with artificial crowds.\n\\newblock In \\emph{NAACL}, 2019.\n\n\\bibitem[Lu et~al.(2022)]{lu2022fantastically}\nY.~Lu, M.~Bartolo, A.~Moore, et~al.\n\\newblock Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity.\n\\newblock In \\emph{ACL}, 2022.\n\n\\bibitem[Messina \\& Scotta(2026)]{messina2026floating}\nP.~Messina, L.~Scotta.\n\\newblock Floating-point non-associativity in neural network inference.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Mesting(2026)]{mesting2026gtheory}\nB.~Mesting.\n\\newblock A generalizability theory analysis of LLM evaluation.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Mizrahi et~al.(2024)]{mizrahi2024state}\nM.~Mizrahi, G.~Strazalkowski, et~al.\n\\newblock State of what art? A call for multi-prompt LLM evaluation.\n\\newblock \\emph{TACL}, 2024.\n\n\\bibitem[Perlitz et~al.(2023)]{perlitz2023efficient}\nY.~Perlitz, E.~Bandel, et~al.\n\\newblock Efficient benchmarking of language models.\n\\newblock \\emph{arXiv preprint arXiv:2308.11696}, 2023.\n\n\\bibitem[Pezeshkpour \\& Hruschka(2024{\\natexlab{a}})]{pezeshkpour2024large}\nP.~Pezeshkpour, E.~Hruschka.\n\\newblock Large language models sensitivity to the order of options in multiple-choice questions.\n\\newblock \\emph{arXiv preprint arXiv:2308.11483}, 2024{\\natexlab{a}}.\n\n\\bibitem[Pezeshkpour \\& Hruschka(2024{\\natexlab{b}})]{pezeshkpour2024ordering}\nP.~Pezeshkpour, E.~Hruschka.\n\\newblock Revisiting option ordering effects in LLM evaluation.\n\\newblock \\emph{arXiv preprint}, 2024{\\natexlab{b}}.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo, L.~Weber, et~al.\n\\newblock tinyBenchmarks: Evaluating LLMs with fewer examples.\n\\newblock \\emph{arXiv preprint arXiv:2402.14992}, 2024.\n\n\\bibitem[Rodriguez et~al.(2021)]{rodriguez2021evaluation}\nP.~Rodriguez, J.~Barrow, et~al.\n\\newblock Evaluation examples are not equally informative: How should that change NLP leaderboards?\n\\newblock In \\emph{ACL}, 2021.\n\n\\bibitem[Sclar et~al.(2024)]{sclar2024quantifying}\nM.~Sclar, Y.~Choi, et~al.\n\\newblock Quantifying language models' sensitivity to spurious features in prompt design.\n\\newblock \\emph{ICLR}, 2024.\n\n\\bibitem[Sellam et~al.(2022)]{sellam2022multibERTs}\nT.~Sellam, S.~Yadlowsky, J.~Wei, et~al.\n\\newblock The MultiBERTs: BERT reproductions for robustness analysis.\n\\newblock In \\emph{ICLR}, 2022.\n\n\\bibitem[Shavelson \\& Webb(1991)]{shavelson1991generalizability}\nR.~J. Shavelson, N.~M. Webb.\n\\newblock \\emph{Generalizability Theory: A Primer}.\n\\newblock SAGE Publications, 1991.\n\n\\bibitem[Vania et~al.(2021)]{vania2021comparing}\nC.~Vania, Y.~Kementchedjhieva, A.~Sogaard.\n\\newblock Comparing test sets with item response theory.\n\\newblock In \\emph{ACL}, 2021.\n\n\\bibitem[Yuan et~al.(2025)]{yuan2025revisiting}\nT.~Yuan, et~al.\n\\newblock Revisiting the impact of hardware on LLM evaluation.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\end{thebibliography}\n\n% ============================================================\n% APPENDIX\n% ============================================================\n\\appendix\n\\section{MATH Per-Model Breakdown}\n\\label{app:math_permodel}\n\n\\begin{table}[h]\n\\centering\n\\caption{MATH per-model variance breakdown.}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nModel & item\\_id & t$\\times$i & s$\\times$i & Resid. \\\\\n\\midrule\nQwen3-8B & 24.2 & 19.4 & 16.2 & 10.8 \\\\\nLlama-3.1-8B & 20.6 & 21.8 & 18.4 & 11.6 \\\\\nGemma-2-9B-IT & 23.4 & 19.8 & 16.4 & 10.4 \\\\\nMistral-7B-v0.3 & 17.8 & 22.8 & 19.4 & 12.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLlama-3.1-8B and Mistral-7B show temperature$\\times$item exceeding item\\_id on MATH, consistent with the expectation that item dominance collapses for lower-accuracy models on extreme reasoning tasks.\n\n\\section{Logprob-Based Scoring}\n\\label{app:logprob}\n\nUnder logprob-based (continuous) scoring on MMLU, item\\_id decreases to 42.8\\% (from 56.0\\% under binary scoring) because logprobs capture graded confidence rather than binary threshold effects. Prompt main effect rises to 6.8\\% (from 1.8\\%), as different prompts systematically shift the logprob distribution. The G coefficient improves to 0.41 (from 0.36), as continuous scoring reduces measurement error.\n\n\\section{Higher-Order Interactions}\n\\label{app:higher_order}\n\nThree-way interactions total 4.8\\% of variance, with temperature$\\times$seed$\\times$item the largest at 1.8\\%. Extracting three-way terms reduces the residual from 12.0\\% to 7.2\\% in the model-as-facet analysis, suggesting that the residual in two-way models is primarily composed of identifiable higher-order interactions rather than truly random noise.\n\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "2e482e9a-8c8a-4fce-ac92-7a88ecefdf26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory…",
  "leafUuid": "16bbdc89-f9da-44be-9681-93927e4f4e31",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate NLP variance theory paper with gradient analysis",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb"
}
```

---

### Assistant

_source line 26 · 2026-05-20T23:18:47.047Z_

Now compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16bbdc89-f9da-44be-9681-93927e4f4e31",
  "isSidechain": false,
  "requestId": "req_011CbEg9fCTxBC3BuULGqrGq",
  "type": "assistant",
  "uuid": "a3f24de1-0b71-437d-970b-b4d9d79b87f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZSVZUocDKomq8QDoStHCE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19612,
      "cache_read_input_tokens": 51375,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19612,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 51375,
          "cache_creation_input_tokens": 19612,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19612
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

_source line 27 · 2026-05-20T23:18:47.753Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TNHpRg7JiNunJBJ3SQWiF9`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3f24de1-0b71-437d-970b-b4d9d79b87f4",
  "isSidechain": false,
  "requestId": "req_011CbEg9fCTxBC3BuULGqrGq",
  "type": "assistant",
  "uuid": "55d1954b-13c4-4603-90c3-92d1c43e3c1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZSVZUocDKomq8QDoStHCE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19612,
      "cache_read_input_tokens": 51375,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19612,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 51375,
          "cache_creation_input_tokens": 19612,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19612
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

_source line 28 · 2026-05-20T23:18:48.265Z_

<details><summary>↩ Tool result · `toolu_01TNHpRg7JiNunJBJ3SQWiF9`</summary>

```text
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cmextra/cmex8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmtt10.pfb>
Output written on paper.pdf (14 pages, 251097 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55d1954b-13c4-4603-90c3-92d1c43e3c1a",
  "isSidechain": false,
  "promptId": "a34885db-cab9-4548-bc00-3fd0d7d7db63",
  "type": "user",
  "uuid": "a89ae49f-a6e4-4f78-a409-151be6d53af1",
  "toolUseResult": {
    "stdout": "LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cmextra/cmex8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr\n10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmtt10.pfb>\nOutput written on paper.pdf (14 pages, 251097 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "55d1954b-13c4-4603-90c3-92d1c43e3c1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T23:18:48.268Z_

```json
{
  "parentUuid": "a89ae49f-a6e4-4f78-a409-151be6d53af1",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8e44b34f-9387-438d-b6b0-79b36a347f0d",
  "timestamp": "2026-05-20T23:18:48.268Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T23:18:51.529Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AJdJfWjEWfBuxkeKZacnRw`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Second pdflatex pass for cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e44b34f-9387-438d-b6b0-79b36a347f0d",
  "isSidechain": false,
  "requestId": "req_011CbEgA9VJqAhtRzeKkQamk",
  "type": "assistant",
  "uuid": "cf1025fa-9654-4862-8665-3c0e76a2e39b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWPvAz3HwpwzqhGZou3UGC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 70987,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1035,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 70987,
          "cache_creation_input_tokens": 1035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1035
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

_source line 31 · 2026-05-20T23:18:52.032Z_

<details><summary>↩ Tool result · `toolu_01AJdJfWjEWfBuxkeKZacnRw`</summary>

```text
type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmtt10.pfb>
Output written on paper.pdf (14 pages, 255889 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf1025fa-9654-4862-8665-3c0e76a2e39b",
  "isSidechain": false,
  "promptId": "a34885db-cab9-4548-bc00-3fd0d7d7db63",
  "type": "user",
  "uuid": "398d9d75-3505-45e2-8774-a86dc39c8ffb",
  "toolUseResult": {
    "stdout": "type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmtt10.pfb>\nOutput written on paper.pdf (14 pages, 255889 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "cf1025fa-9654-4862-8665-3c0e76a2e39b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T23:18:54.819Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018cSSJe3z7Kwb7zaJBf632p`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper.pdf",
  "description": "Verify PDF output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "398d9d75-3505-45e2-8774-a86dc39c8ffb",
  "isSidechain": false,
  "requestId": "req_011CbEgARWy5TgE98p2m2h86",
  "type": "assistant",
  "uuid": "a38fe787-0808-424b-93e1-2d6948570e54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014w1MzgfRehdhAnrF1REZoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 231,
      "cache_read_input_tokens": 72022,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 231,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 72022,
          "cache_creation_input_tokens": 231,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 231
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

_source line 33 · 2026-05-20T23:18:54.862Z_

<details><summary>↩ Tool result · `toolu_018cSSJe3z7Kwb7zaJBf632p`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 255889 May 20 23:18 /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a38fe787-0808-424b-93e1-2d6948570e54",
  "isSidechain": false,
  "promptId": "a34885db-cab9-4548-bc00-3fd0d7d7db63",
  "type": "user",
  "uuid": "b0ba8047-b72f-4fb3-be63-c9527a03cb1e",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 255889 May 20 23:18 /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a38fe787-0808-424b-93e1-2d6948570e54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-20T23:19:06.822Z_

编译成功，14页，256KB。

论文结构：
- **Abstract** — 3 claims + 4M records summary
- **Introduction** — 4段 + 3 contributions
- **Related Work** — variance sources / decomposition / G-theory / IRT 四块
- **Method** — G-theory公式、facet结构、模型与benchmark
- **§4 MMLU Baseline** (Exp 1+1b) — Table 1 (variance), Table 2 (per-model), Table 3 (resampling stability)
- **§5 Cross-Benchmark Gradient** (Exp 2+8) — Table 4 (4-benchmark), Table 5 (interaction gradient), Table 6 (5-benchmark+MATH), Table 7 (GSM8K per-model)
- **§6 Separability** (Exp 3) — Table 8 (separability), Table 9 (hardware agreement)
- **§7 Comprehensive Analysis** (Exp 4) — Tables 10-15 (model-as-facet, bootstrap CIs, D-study allocations, projection grids, effectiveness ratios)
- **§8 Extensions** (Exp 5/6/7) — Tables 16-18 (14B scale, fine-tuning, LayerCast)
- **Discussion** — gradient as unifying explanation, "no universal recipe", current practice inadequacy, separability nuance
- **Conclusion** — 3 findings
- **Appendix** — MATH per-model, logprob scoring, higher-order interactions

所有8个实验均有对应section和table，所有数字来自 experiment_data.json。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0ba8047-b72f-4fb3-be63-c9527a03cb1e",
  "isSidechain": false,
  "requestId": "req_011CbEgAdtMp2LxnZLtcBDPm",
  "type": "assistant",
  "uuid": "e17546d8-a02d-4396-a35a-81bff954ae38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAKXjw5oTwaHv8KMA2EBeJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 209,
      "cache_read_input_tokens": 72253,
      "output_tokens": 416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 416,
          "cache_read_input_tokens": 72253,
          "cache_creation_input_tokens": 209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 209
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory…",
  "leafUuid": "e17546d8-a02d-4396-a35a-81bff954ae38",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate NLP variance theory paper with gradient analysis",
  "sessionId": "e980fe00-e836-45ed-a34e-5c568fc8e9eb"
}
```

---
