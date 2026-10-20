# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T181213 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/0e069ccf-54de-4ec0-aafa-7fc5c7e58d13.jsonl`
- **Structured JSON:** [`793f326e00e07a47cf61.json`](../../sessions/79/793f326e00e07a47cf61.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T18:36:58.554Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T18:36:58.554Z",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T181213 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/experiment_data.json`（先 Read 此文件）\n- Venue：AAAI 2027\n- Narrative guidance：Abandon \"distributional fingerprint\" as primary contribution. Surface features (TTR, hapax_ratio) explain nearly all classifier variance; reference-model entropy statistics add negligible independent signal. Cross-generator generalization collapses because surface vocabulary statistics are generator-specific artifacts, not universal depth markers. Reframe paper as an empirical characterization of recursive generation dynamics: \"We tested H₁ vs H₂ and found that non-paraphrastic chains also converge rapidly in distributional space, with detectable differences confined primarily to vocabulary impoverishment.\" Reposition as negative-but-informative result extending attractor cycle theory to non-paraphrastic settings. New angle: vocabulary impoverishment as a universal but shallow fingerprint — theoretically motivated by generation entropy convergence under autoregressive sampling. Target AAAI as empirical science contribution with clear hypothesis-testing framing and boundary conditions for future work.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T18:36:58.558Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T18:36:58.558Z",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-14T18:36:58.575Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T181213 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/experiment_data.json`（先 Read 此文件）
- Venue：AAAI 2027
- Narrative guidance：Abandon "distributional fingerprint" as primary contribution. Surface features (TTR, hapax_ratio) explain nearly all classifier variance; reference-model entropy statistics add negligible independent signal. Cross-generator generalization collapses because surface vocabulary statistics are generator-specific artifacts, not universal depth markers. Reframe paper as an empirical characterization of recursive generation dynamics: "We tested H₁ vs H₂ and found that non-paraphrastic chains also converge rapidly in distributional space, with detectable differences confined primarily to vocabulary impoverishment." Reposition as negative-but-informative result extending attractor cycle theory to non-paraphrastic settings. New angle: vocabulary impoverishment as a universal but shallow fingerprint — theoretically motivated by generation entropy convergence under autoregressive sampling. Target AAAI as empirical science contribution with clear hypothesis-testing framing and boundary conditions for future work.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "00675285-eb7e-4fe5-a2b7-b441582ee0b5",
  "type": "user",
  "uuid": "dba6977a-9a58-4b82-bc12-28c7c721f4e9",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T18:36:58.574Z_

```json
{
  "parentUuid": "dba6977a-9a58-4b82-bc12-28c7c721f4e9",
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
  "uuid": "d87a66ac-a7c6-4061-a810-a163160f4c86",
  "timestamp": "2026-05-14T18:36:58.574Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T18:36:58.574Z_

```json
{
  "parentUuid": "d87a66ac-a7c6-4061-a810-a163160f4c86",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b68a9e3d-717e-46bc-b00e-081d2f0162ea",
  "timestamp": "2026-05-14T18:36:58.574Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
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
  "aiTitle": "Generate simulated research paper for dream ID",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13"
}
```

---

### Assistant

_source line 7 · 2026-05-14T18:37:02.117Z_

I'll start by reading the input files to understand the experimental data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b68a9e3d-717e-46bc-b00e-081d2f0162ea",
  "isSidechain": false,
  "requestId": "req_011Cb2wpAik16kT6Cz45jF7N",
  "type": "assistant",
  "uuid": "16e79489-c732-40c2-ac4a-5e0fc6c05111",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvMzPhXS5jES8XAzLuSt5P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11243,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11243
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

_source line 8 · 2026-05-14T18:37:02.944Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XeNyiogNWH6wFgJh7VWRcy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16e79489-c732-40c2-ac4a-5e0fc6c05111",
  "isSidechain": false,
  "requestId": "req_011Cb2wpAik16kT6Cz45jF7N",
  "type": "assistant",
  "uuid": "2965aa64-3bb8-445b-bebe-22aba79933d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvMzPhXS5jES8XAzLuSt5P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11243,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11243
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

_source line 9 · 2026-05-14T18:37:03.220Z_

<details><summary>↩ Tool result · `toolu_01XeNyiogNWH6wFgJh7VWRcy`</summary>

```text
1	[
2	  {
3	    "name": "feature_ablation",
4	    "description": "Ablation of reference-only, surface-only, and full feature sets on MVP data (Pythia-2.8B generator, Pythia-410M reference, 3-class depth). Ordinal logistic regression + random forest, 5-fold CV.\n",
5	    "results": {
6	      "surface_only_macro_f1": 0.82,
7	      "surface_only_cv_std": 0.015,
8	      "ref_only_macro_f1": 0.47,
9	      "ref_only_cv_std": 0.032,
10	      "full_macro_f1": 0.83,
11	      "full_cv_std": 0.014,
12	      "ref_minus_surface_delta": -0.35,
13	      "full_minus_surface_delta": 0.01,
14	      "permutation_importance_hapax_ratio": 0.31,
15	      "permutation_importance_ttr": 0.24,
16	      "permutation_importance_entropy_mean": 0.04,
17	      "permutation_importance_entropy_std": 0.03,
18	      "permutation_importance_tail_decay": 0.02,
19	      "ref_features_added_significance_p": 0.18
20	    },
21	    "tables": [
22	      {
23	        "name": "Table 2: Feature Ablation Results (3-class, MVP data)",
24	        "columns": [
25	          "Feature_Set",
26	          "Macro_F1",
27	          "Gen0_F1",
28	          "Gen1_F1",
29	          "Gen2plus_F1",
30	          "CV_Std"
31	        ],
32	        "rows": [
33	          [
34	            "surface_only",
35	            0.82,
36	            0.94,
37	            0.75,
38	            0.77,
39	            0.015
40	          ],
41	          [
42	            "ref_only",
43	            0.47,
44	            0.58,
45	            0.38,
46	            0.44,
47	            0.032
48	          ],
49	          [
50	            "full",
51	            0.83,
52	            0.95,
53	            0.76,
54	            0.78,
55	            0.014
56	          ],
57	          [
58	            "chance",
59	            0.33,
60	            0.33,
61	            0.33,
62	            0.33,
63	            "-"
64	          ]
65	        ]
66	      },
67	      {
68	        "name": "Table 3: Permutation Feature Importance (Full Model)",
69	        "columns": [
70	          "Feature",
71	          "Importance",
72	          "Std"
73	        ],
74	        "rows": [
75	          [
76	            "hapax_ratio",
77	            0.31,
78	            0.04
79	          ],
80	          [
81	            "ttr",
82	            0.24,
83	            0.03
84	          ],
85	          [
86	            "entropy_mean",
87	            0.04,
88	            0.02
89	          ],
90	          [
91	            "entropy_std",
92	            0.03,
93	            0.01
94	          ],
95	          [
96	            "entropy_min",
97	            0.02,
98	            0.01
99	          ],
100	          [
101	            "entropy_max",
102	            0.01,
103	            0.01
104	          ],
105	          [
106	            "tail_decay",
107	            0.02,
108	            0.01
109	          ]
110	        ]
111	      }
112	    ],
113	    "figures": [],
114	    "analysis": "Claim 2 is falsified. The ablation decisively shows that reference-model features carry no independent signal. The full model's marginal +0.01 over surface-only is within noise. This result is consistent with the hypothesis that autoregressive generation entropy converges to a near-stationary distribution by gen-1, while vocabulary depletion (a surface-level phenomenon) continues to accumulate. The practical implication: a $0 feature (hapax_ratio) matches the expensive reference-model inference pipeline.\n\n\nSurface features alone recover 97.6% of full-model performance (0.82 vs 0.84 MVP). hapax_ratio and TTR dominate because recursive generation progressively depletes rare vocabulary — a mechanical consequence of autoregressive sampling from a fixed distribution. Reference-model entropy statistics show near-chance 3-class performance (0.47) because the entropy distribution under the reference model converges rapidly across generation depths: by gen-1, the token-level surprise distribution is already close to its stationary form. Adding reference features to surface features yields only +0.01 F1 (not statistically significant, p=0.18 on paired bootstrap), confirming that entropy_mean/std/min/max carry redundant information already captured by vocabulary depletion proxies. The \"distributional fingerprint\" framing collapses — what we detect is vocabulary impoverishment, not a deeper distributional shift.\n"
115	  },
116	  {
117	    "name": "cross_generator_evaluation",
118	    "description": "5 generators (Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, Pythia-1B). 1000 seeds × 5 generators × 5 depths = 25K chains. Leave-one-generator-out CV for cross-generator generalization. 3-class depth classification.\n",
119	    "results": {
120	      "within_generator_avg_macro_f1": 0.81,
121	      "leave_one_out_avg_macro_f1": 0.48,
122	      "leave_one_out_std": 0.07,
123	      "leave_one_out_gen0_f1": 0.68,
124	      "leave_one_out_gen1_f1": 0.38,
125	      "leave_one_out_gen2plus_f1": 0.42,
126	      "loo_held_out_pythia28b_f1": 0.52,
127	      "loo_held_out_olmo_f1": 0.44,
128	      "loo_held_out_qwen2b_f1": 0.43,
129	      "loo_held_out_qwen08b_f1": 0.5,
130	      "loo_held_out_pythia1b_f1": 0.53,
131	      "gen1_vs_gen2plus_binary_loo_f1": 0.54,
132	      "pooled_all_generators_macro_f1": 0.62
133	    },
134	    "tables": [
135	      {
136	        "name": "Table 4: Cross-Generator Generalization (Leave-One-Out)",
137	        "columns": [
138	          "Held_Out_Generator",
139	          "Macro_F1",
140	          "Gen0_F1",
141	          "Gen1_F1",
142	          "Gen2plus_F1"
143	        ],
144	        "rows": [
145	          [
146	            "Pythia-2.8B",
147	            0.52,
148	            0.71,
149	            0.4,
150	            0.45
151	          ],
152	          [
153	            "OLMo-2-1B",
154	            0.44,
155	            0.65,
156	            0.34,
157	            0.38
158	          ],
159	          [
160	            "Qwen3.5-2B",
161	            0.43,
162	            0.64,
163	            0.35,
164	            0.39
165	          ],
166	          [
167	            "Qwen3.5-0.8B",
168	            0.5,
169	            0.7,
170	            0.38,
171	            0.43
172	          ],
173	          [
174	            "Pythia-1B",
175	            0.53,
176	            0.72,
177	            0.42,
178	            0.46
179	          ],
180	          [
181	            "**Average**",
182	            "**0.48**",
183	            "**0.68**",
184	            "**0.38**",
185	            "**0.42**"
186	          ]
187	        ]
188	      },
189	      {
190	        "name": "Table 5: Within- vs Cross-Generator Comparison",
191	        "columns": [
192	          "Setting",
193	          "Macro_F1",
194	          "Δ_vs_Within"
195	        ],
196	        "rows": [
197	          [
198	            "within_generator_avg",
199	            0.81,
200	            "-"
201	          ],
202	          [
203	            "leave_one_out_avg",
204	            0.48,
205	            -0.33
206	          ],
207	          [
208	            "pooled_all_generators",
209	            0.62,
210	            -0.19
211	          ]
212	        ]
213	      }
214	    ],
215	    "figures": [],
216	    "analysis": "Claim 1 fails in its generalization requirement. Cross-generator macro-F1 of 0.48 is barely above chance (0.33). The fundamental problem: surface vocabulary statistics are generator-specific calibration artifacts. A model that learns \"hapax_ratio < 0.30 means gen-2+\" from Pythia data will misclassify Qwen gen-0 text (which may have hapax_ratio ~0.35 vs Pythia gen-0 ~0.45). Without independent reference-model signal (which plan_001 showed is absent), there is no generator-invariant depth feature. The pooled setting (0.62) is inflated by within-generator signal bleeding through the non-held-out generators in training.\n\n\nWithin-generator performance remains strong (~0.81) because each generator has a characteristic vocabulary depletion rate that surface features learn. But leave-one-out drops catastrophically to 0.48 because the absolute levels of hapax_ratio and TTR are generator-specific: Qwen models produce systematically different type-token ratios than Pythia models at every depth. The classifier learns generator-specific thresholds, not universal depth signatures. Gen-0 identification is partially salvaged (0.68) because human-written text has a consistently distinct surface profile regardless of which generator produces the synthetic continuations. Gen-1 vs gen-2+ discrimination is near chance (0.38/0.42) in the cross-generator setting because the vocabulary depletion curves of different generators at depth 1 overlap with other generators at depth 2+. Pythia-family held-out sets perform slightly better (0.52-0.53) due to Pythia-1B sharing vocabulary statistics with Pythia-2.8B in the training fold. Cross- family transfer (Qwen held out) is worst (0.43-0.44). This confirms that surface features are generator-specific, not universal depth markers.\n"
217	  },
218	  {
219	    "name": "cross_family_reference_model",
220	    "description": "Test OLMo-2-1B and Qwen3.5-0.8B as reference models (replacing Pythia-410M) for feature extraction. Full cross of 3 reference models × 5 generators.\n",
221	    "results": {
222	      "pythia_ref_cross_gen_macro_f1": 0.48,
223	      "olmo_ref_cross_gen_macro_f1": 0.45,
224	      "qwen_ref_cross_gen_macro_f1": 0.44,
225	      "best_ref_model": "pythia_410m",
226	      "ref_model_variance_std": 0.02,
227	      "ensemble_3ref_cross_gen_macro_f1": 0.5,
228	      "ref_only_olmo_macro_f1": 0.43,
229	      "ref_only_qwen_macro_f1": 0.41
230	    },
231	    "tables": [
232	      {
233	        "name": "Table 6: Reference Model Comparison (Leave-One-Generator-Out)",
234	        "columns": [
235	          "Reference_Model",
236	          "LOO_Macro_F1",
237	          "Ref_Only_F1",
238	          "Surface_Only_F1"
239	        ],
240	        "rows": [
241	          [
242	            "Pythia-410M",
243	            0.48,
244	            0.47,
245	            0.82
246	          ],
247	          [
248	            "OLMo-2-1B",
249	            0.45,
250	            0.43,
251	            0.82
252	          ],
253	          [
254	            "Qwen3.5-0.8B",
255	            0.44,
256	            0.41,
257	            0.82
258	          ],
259	          [
260	            "Ensemble (3 refs)",
261	            0.5,
262	            0.49,
263	            0.82
264	          ]
265	        ]
266	      }
267	    ],
268	    "figures": [],
269	    "analysis": "Reference model choice is irrelevant because the underlying signal is absent. Surface features remain constant at 0.82 regardless of reference model (they don't use it), confirming surface features as the sole discriminative mechanism. The experiment conclusively addresses RC2 but in a way that undermines the paper: the signal isn't architecture-specific because there is no reference-model signal to be architecture- specific about.\n\n\nChanging the reference model does not rescue cross-generator performance because the bottleneck is not reference model choice — it is the absence of depth-discriminative signal in the entropy statistics themselves. All three reference models produce similarly uninformative entropy distributions because the phenomenon is fundamental: autoregressive generation entropy converges to near-stationary levels by gen-1 regardless of which model measures it. The slight advantage of Pythia-410M (0.48 vs 0.44-0.45) is a minor architectural compatibility effect with the Pythia generators in the training set, not genuine signal. Ensembling three reference models yields only +0.02 over the best single model, confirming the features are redundant across reference architectures. This rules out RC2 concerns as irrelevant — the problem is not architecture-specific artifacts but rather the fundamental convergence of generation entropy.\n"
270	  },
271	  {
272	    "name": "downstream_utility",
273	    "description": "Fine-tune Pythia-410M on depth-stratified data subsets. Measure perplexity degradation as function of training data depth. Compare depth-aware filtering vs binary baselines (FastDetectGPT, LD-Score threshold).\n",
274	    "results": {
275	      "depth_quality_spearman_rho": 0.19,
276	      "depth_quality_spearman_p": 0.04,
277	      "ppl_gen0_only": 18.2,
278	      "ppl_gen1_mixed": 19.1,
279	      "ppl_gen2plus_mixed": 19.8,
280	      "ppl_unfiltered": 19.5,
281	      "depth_filter_top1_ppl": 18.5,
282	      "binary_filter_fastdetect_ppl": 18.4,
283	      "binary_filter_ldscore_ppl": 18.6,
284	      "depth_filter_vs_binary_perf_gap_pct": -0.3,
285	      "depth_filter_data_retained_pct": 38,
286	      "binary_filter_data_retained_pct": 42
287	    },
288	    "tables": [
289	      {
290	        "name": "Table 7: Downstream Fine-tuning Perplexity",
291	        "columns": [
292	          "Training_Data",
293	          "Perplexity",
294	          "Data_Size_pct"
295	        ],
296	        "rows": [
297	          [
298	            "gen-0 only",
299	            18.2,
300	            33
301	          ],
302	          [
303	            "gen-0 + gen-1",
304	            18.8,
305	            67
306	          ],
307	          [
308	            "all depths unfiltered",
309	            19.5,
310	            100
311	          ],
312	          [
313	            "depth-aware filter (≤gen-1)",
314	            18.5,
315	            38
316	          ],
317	          [
318	            "FastDetectGPT binary filter",
319	            18.4,
320	            42
321	          ],
322	          [
323	            "LD-Score binary filter",
324	            18.6,
325	            40
326	          ]
327	        ]
328	      },
329	      {
330	        "name": "Table 8: Depth-Quality Correlation",
331	        "columns": [
332	          "Metric",
333	          "Value"
334	        ],
335	        "rows": [
336	          [
337	            "Spearman ρ (depth vs ppl_degradation)",
338	            0.19
339	          ],
340	          [
341	            "p-value",
342	            0.04
343	          ],
344	          [
345	            "depth_filter vs best_binary gap",
346	            "-0.3%"
347	          ]
348	        ]
349	      }
350	    ],
351	    "figures": [],
352	    "analysis": "Claim 3 fails. While a statistically significant correlation exists (p=0.04), the effect size is negligible (ρ=0.19) and depth-aware filtering underperforms binary baselines by 0.3%. The ordinal depth information adds no practical value over binary classification for data curation. This is the expected consequence of plan_001 and plan_002 results: if depth estimation relies on generator-specific surface features and cross-generator transfer is poor, the depth predictions are too noisy to provide downstream utility beyond what binary detection already offers.\n\n\nA weak positive correlation (ρ=0.19) exists between predicted depth and quality degradation, but it is barely significant and practically meaningless. The perplexity difference between gen-0-only and gen-2+-mixed training is modest (~1.6 points) because vocabulary impoverishment in synthetic text creates a noisy but not catastrophic training signal — the model still learns reasonable language statistics from synthetic text, just with slightly depleted rare-word coverage. Depth-aware filtering performs equivalently to binary baselines (-0.3% gap, within noise) because the depth classifier's cross-generator errors (from plan_002) introduce enough noise to eliminate any advantage over simple binary filtering. FastDetectGPT actually edges out depth-aware filtering by 0.1 ppl because it makes fewer classification errors on the binary task than our system makes on the harder ordinal task. Claim 3 effectively fails — depth-aware filtering provides no practical advantage over binary baselines.\n"
353	  },
354	  {
355	    "name": "prompt_type_comparison",
356	    "description": "Compare continuation vs elaboration vs inspired_rewriting chains. 1000 seeds, Pythia-2.8B, 3 prompt types, 5 depths each.\n",
357	    "results": {
358	      "continuation_within_gen_f1": 0.82,
359	      "elaboration_within_gen_f1": 0.78,
360	      "inspired_rewriting_within_gen_f1": 0.69,
361	      "continuation_cross_prompt_f1": 0.61,
362	      "elaboration_cross_prompt_f1": 0.58,
363	      "inspired_rewriting_cross_prompt_f1": 0.52,
364	      "convergence_speed_continuation_depth": 2,
365	      "convergence_speed_elaboration_depth": 2,
366	      "convergence_speed_rewriting_depth": 1
367	    },
368	    "tables": [
369	      {
370	        "name": "Table 9: Prompt Type Comparison",
371	        "columns": [
372	          "Prompt_Type",
373	          "Within_Gen_F1",
374	          "Cross_Prompt_F1",
375	          "Convergence_Depth"
376	        ],
377	        "rows": [
378	          [
379	            "continuation",
380	            0.82,
381	            0.61,
382	            2
383	          ],
384	          [
385	            "elaboration",
386	            0.78,
387	            0.58,
388	            2
389	          ],
390	          [
391	            "inspired_rewriting",
392	            0.69,
393	            0.52,
394	            1
395	          ]
396	        ]
397	      }
398	    ],
399	    "figures": [],
400	    "analysis": "All prompt types show rapid convergence, supporting H₁. The depth signal ceiling is approximately 2 effective classes (gen-0 vs synthetic) for rewriting and 3 classes (gen-0/gen-1/gen-2+) for continuation — but only within-generator. The prompt type comparison reveals an additional confound: not only is the signal generator-specific, it is prompt-type-specific. This further narrows the practical applicability of depth estimation.\n\n\nContinuation chains show the highest within-generator F1 (0.82) because they preserve the most topic continuity, making vocabulary depletion the dominant signal. Elaboration is slightly lower (0.78) due to topic drift introducing vocabulary variance that partially masks depletion. Inspired rewriting shows the weakest signal (0.69) because each generation step introduces substantially new vocabulary, partially resetting the depletion signal. Cross-prompt transfer is poor across the board because each prompt type induces a different vocabulary depletion rate — the classifier learns prompt- type-specific thresholds. Convergence analysis shows all three types stabilize by depth 2 (rewriting by depth 1), supporting H₁: even non-paraphrastic chains converge rapidly. The rewriting chains converge fastest because the larger semantic jumps quickly exhaust the generator's preferred vocabulary, reaching a \"vocabulary floor\" by gen-1.\n"
401	  },
402	  {
403	    "name": "paraphrastic_comparison",
404	    "description": "Construct parallel paraphrasing chains for direct comparison with continuation chains. Test attractor convergence theory — H₁ vs H₂.\n",
405	    "results": {
406	      "paraphrase_within_gen_f1": 0.64,
407	      "continuation_within_gen_f1": 0.82,
408	      "paraphrase_convergence_depth": 1,
409	      "continuation_convergence_depth": 2,
410	      "paraphrase_gen1_vs_gen2plus_f1": 0.41,
411	      "continuation_gen1_vs_gen2plus_f1": 0.58,
412	      "kl_depth2_vs_depth3_paraphrase": 0.008,
413	      "kl_depth2_vs_depth3_continuation": 0.031
414	    },
415	    "tables": [
416	      {
417	        "name": "Table 10: Paraphrastic vs Non-Paraphrastic Chains",
418	        "columns": [
419	          "Chain_Type",
420	          "Macro_F1_3class",
421	          "Gen1_vs_Gen2plus_F1",
422	          "Convergence_Depth",
423	          "KL_d2_d3"
424	        ],
425	        "rows": [
426	          [
427	            "paraphrasing",
428	            0.64,
429	            0.41,
430	            1,
431	            0.008
432	          ],
433	          [
434	            "continuation",
435	            0.82,
436	            0.58,
437	            2,
438	            0.031
439	          ],
440	          [
441	            "elaboration",
442	            0.78,
443	            0.52,
444	            2,
445	            0.024
446	          ],
447	          [
448	            "inspired_rewriting",
449	            0.69,
450	            0.44,
451	            1,
452	            0.012
453	          ]
454	        ]
455	      }
456	    ],
457	    "figures": [],
458	    "analysis": "H₁ is confirmed: non-paraphrastic chains also converge, just 1 step slower than paraphrastic chains. This extends the ACL 2025 attractor theory to non-paraphrastic settings — arguably the most publishable finding in the worst case. The convergence is driven by autoregressive sampling from a fixed model concentrating probability mass on preferred tokens regardless of prompt type, creating a universal vocabulary attractor. Depth signal is fundamentally bounded at ~2-3 classes.\n\n\nParaphrasing chains converge faster than continuation chains (by depth 1 vs depth 2), consistent with attractor cycle theory from ACL 2025. Paraphrasing F1 is lower (0.64) because the semantic-preservation constraint limits vocabulary variation — paraphrases reuse similar word types, so hapax_ratio depletion is less pronounced. But crucially, continuation chains also converge by depth 2, meaning non-paraphrastic generation does NOT produce the unbounded divergence hypothesized in H₂. Both chain types reach near-stationary distributions within 2-3 steps. The KL divergence between depth-2 and depth-3 is negligible for both types (<0.04 nats). This is the key finding for the worst-case narrative: H₁ (convergence) holds even for non-paraphrastic chains, limiting depth signal to a maximum of ~2-3 discriminable classes and undermining the premise that non-paraphrastic chains produce monotonic divergence.\n"
459	  },
460	  {
461	    "name": "cross_model_chains",
462	    "description": "Cross-model chains (different generator per depth step) vs single-model chains. 5 generators randomly assigned per step. 1000 seeds × 5 depths.\n",
463	    "results": {
464	      "single_model_within_gen_f1": 0.81,
465	      "cross_model_chain_f1": 0.42,
466	      "cross_model_gen0_f1": 0.65,
467	      "cross_model_gen1_f1": 0.32,
468	      "cross_model_gen2plus_f1": 0.35,
469	      "cross_model_binary_gen0_vs_rest_f1": 0.67
470	    },
471	    "tables": [
472	      {
473	        "name": "Table 11: Single-Model vs Cross-Model Chains",
474	        "columns": [
475	          "Setting",
476	          "Macro_F1",
477	          "Gen0_F1",
478	          "Gen1_F1",
479	          "Gen2plus_F1"
480	        ],
481	        "rows": [
482	          [
483	            "single_model_chains",
484	            0.81,
485	            0.94,
486	            0.75,
487	            0.77
488	          ],
489	          [
490	            "cross_model_chains",
491	            0.42,
492	            0.65,
493	            0.32,
494	            0.35
495	          ],
496	          [
497	            "chance",
498	            0.33,
499	            0.33,
500	            0.33,
501	            0.33
502	          ]
503	        ]
504	      }
505	    ],
506	    "figures": [],
507	    "analysis": "The most ecologically valid setting (cross-model chains) produces near-chance depth estimation. This confirms that the MVP result (0.84) was an artifact of single-model evaluation: the classifier learned Pythia-2.8B's specific vocabulary depletion curve, not a universal depth signature. In realistic web contamination scenarios with diverse generators, depth estimation beyond binary (human vs synthetic) is not feasible with current features.\n\n\nCross-model chains are devastating for depth estimation (0.42 macro-F1). When different generators produce each depth step, the vocabulary statistics at any given depth reflect the current-step generator's preferences more than the cumulative depth of the chain. A text generated by Qwen at depth-2 in a chain may have higher hapax_ratio than text generated by Pythia-1B at depth-1, because Qwen has a richer base vocabulary. The generator-switching effectively randomizes the surface features that the classifier depends on. Gen-0 identification survives partially (0.65) because human text is still distinct from any generator, but gen-1/gen-2+ classification is near-chance. This is the most realistic contamination scenario and the most damning result for practical applicability.\n"
508	  },
509	  {
510	    "name": "multi_domain_seeds",
511	    "description": "Expand to 4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC), creative writing (WritingPrompts). 500 seeds per domain × 5 depths, Pythia-2.8B generator.\n",
512	    "results": {
513	      "wikipedia_within_domain_f1": 0.83,
514	      "news_within_domain_f1": 0.8,
515	      "scientific_within_domain_f1": 0.76,
516	      "creative_within_domain_f1": 0.72,
517	      "cross_domain_avg_f1": 0.59,
518	      "pooled_all_domains_f1": 0.74,
519	      "scientific_hapax_ratio_gen0_median": 0.52,
520	      "creative_hapax_ratio_gen0_median": 0.38
521	    },
522	    "tables": [
523	      {
524	        "name": "Table 12: Multi-Domain Results",
525	        "columns": [
526	          "Domain",
527	          "Within_Domain_F1",
528	          "Gen0_hapax_median",
529	          "Gen2plus_hapax_median",
530	          "Δ_hapax"
531	        ],
532	        "rows": [
533	          [
534	            "Wikipedia",
535	            0.83,
536	            0.47,
537	            0.26,
538	            0.21
539	          ],
540	          [
541	            "News",
542	            0.8,
543	            0.44,
544	            0.27,
545	            0.17
546	          ],
547	          [
548	            "Scientific",
549	            0.76,
550	            0.52,
551	            0.35,
552	            0.17
553	          ],
554	          [
555	            "Creative",
556	            0.72,
557	            0.38,
558	            0.28,
559	            0.1
560	          ],
561	          [
562	            "Cross-domain avg",
563	            0.59,
564	            "-",
565	            "-",
566	            "-"
567	          ]
568	        ]
569	      }
570	    ],
571	    "figures": [],
572	    "analysis": "Domain is yet another confound. The depth signal is domain-specific because the magnitude of vocabulary depletion depends on the seed text's lexical richness. Combined with generator-specificity and prompt-type-specificity, this creates a three-way interaction that makes general-purpose depth estimation impractical. A classifier trained on Wikipedia+news will overestimate depth for creative writing (lower base hapax) and underestimate it for scientific text (higher base hapax).\n\n\nWithin-domain performance is reasonable but varies by domain. Wikipedia/news are easiest because their seed texts have high hapax_ratio (specialized proper nouns, rare terms) that generation rapidly depletes. Scientific text starts with high rare-word density (technical terms) but the generator sometimes preserves or regenerates these, creating noise. Creative writing is hardest because its base vocabulary is less specialized — the hapax_ratio gap between gen-0 and gen-1 is smaller. Cross-domain transfer drops to 0.59 because each domain has different baseline vocabulary statistics: scientific gen-0 text (hapax_ratio ~0.52) overlaps with creative gen-0 (~0.38), confounding domain and depth. This adds another axis of non-generalization beyond generator and prompt type.\n"
573	  },
574	  {
575	    "name": "finer_grained_ordinal",
576	    "description": "5-class ordinal classification (gen-0 through gen-4) on non-paraphrastic continuation chains. Tests if more than 3-class depth signal exists.\n",
577	    "results": {
578	      "ordinal_5class_macro_f1": 0.52,
579	      "ordinal_5class_gen0_f1": 0.91,
580	      "ordinal_5class_gen1_f1": 0.58,
581	      "ordinal_5class_gen2_f1": 0.38,
582	      "ordinal_5class_gen3_f1": 0.31,
583	      "ordinal_5class_gen4_f1": 0.33,
584	      "ordinal_3class_macro_f1": 0.82,
585	      "adjacent_class_confusion_rate": 0.44,
586	      "mae_ordinal": 0.72
587	    },
588	    "tables": [
589	      {
590	        "name": "Table 13: 5-Class Ordinal Classification",
591	        "columns": [
592	          "Class",
593	          "Precision",
594	          "Recall",
595	          "F1"
596	        ],
597	        "rows": [
598	          [
599	            "gen-0",
600	            0.93,
601	            0.9,
602	            0.91
603	          ],
604	          [
605	            "gen-1",
606	            0.54,
607	            0.62,
608	            0.58
609	          ],
610	          [
611	            "gen-2",
612	            0.36,
613	            0.4,
614	            0.38
615	          ],
616	          [
617	            "gen-3",
618	            0.29,
619	            0.33,
620	            0.31
621	          ],
622	          [
623	            "gen-4",
624	            0.31,
625	            0.35,
626	            0.33
627	          ]
628	        ]
629	      },
630	      {
631	        "name": "Table 14: 5-Class Confusion Matrix",
632	        "columns": [
633	          "Predicted→",
634	          "gen-0",
635	          "gen-1",
636	          "gen-2",
637	          "gen-3",
638	          "gen-4"
639	        ],
640	        "rows": [
641	          [
642	            "gen-0",
643	            0.9,
644	            0.07,
645	            0.02,
646	            0.01,
647	            0.0
648	          ],
649	          [
650	            "gen-1",
651	            0.09,
652	            0.62,
653	            0.18,
654	            0.07,
655	            0.04
656	          ],
657	          [
658	            "gen-2",
659	            0.03,
660	            0.21,
661	            0.4,
662	            0.22,
663	            0.14
664	          ],
665	          [
666	            "gen-3",
667	            0.02,
668	            0.1,
669	            0.24,
670	            0.33,
671	            0.31
672	          ],
673	          [
674	            "gen-4",
675	            0.01,
676	            0.07,
677	            0.16,
678	            0.28,
679	            0.48
680	          ]
681	        ]
682	      }
683	    ],
684	    "figures": [],
685	    "analysis": "Finer-grained estimation is not feasible. The depth signal has a hard ceiling at ~3 discriminable classes, consistent with convergence by depth 2. The confusion matrix shows a clear diagonal-plus-adjacent pattern typical of ordinal features with limited dynamic range. Gen-3 and gen-4 are essentially exchangeable. This further limits the practical scope of depth estimation.\n\n\n5-class performance drops sharply to 0.52 macro-F1 (from 0.82 for 3-class), with gen-2 through gen-4 collapsing into near-chance mutual confusion. This is the direct consequence of H₁ convergence: by depth 2, the feature distributions have already converged, so gen-2/gen-3/gen-4 are statistically indistinguishable. The confusion is concentrated in adjacent classes (44% of errors are off-by-one), consistent with a smooth convergence rather than discrete depth categories. Gen-0 remains easily identified (0.91) and gen-1 partially (0.58), but beyond gen-1 the signal is gone. This confirms the practical ceiling is 2-3 discriminable depth classes, not finer- grained ordinal estimation.\n"
686	  },
687	  {
688	    "name": "human_edit_robustness",
689	    "description": "Robustness to simulated human edits. (A) Random word replacement at 5%, 10%, 20%. (B) LLM-simulated editing (light rephrasing of random sentences).\n",
690	    "results": {
691	      "baseline_no_edit_f1": 0.82,
692	      "random_replace_5pct_f1": 0.77,
693	      "random_replace_10pct_f1": 0.7,
694	      "random_replace_20pct_f1": 0.58,
695	      "llm_edit_light_f1": 0.63,
696	      "llm_edit_light_gen0_f1": 0.82,
697	      "llm_edit_light_gen1_f1": 0.51,
698	      "llm_edit_light_gen2plus_f1": 0.48
699	    },
700	    "tables": [
701	      {
702	        "name": "Table 15: Robustness to Human Edits",
703	        "columns": [
704	          "Edit_Type",
705	          "Edit_Rate",
706	          "Macro_F1",
707	          "Δ_vs_Baseline"
708	        ],
709	        "rows": [
710	          [
711	            "none",
712	            "0%",
713	            0.82,
714	            "-"
715	          ],
716	          [
717	            "random_replace",
718	            "5%",
719	            0.77,
720	            -0.05
721	          ],
722	          [
723	            "random_replace",
724	            "10%",
725	            0.7,
726	            -0.12
727	          ],
728	          [
729	            "random_replace",
730	            "20%",
731	            0.58,
732	            -0.24
733	          ],
734	          [
735	            "llm_simulated",
736	            "light",
737	            0.63,
738	            -0.19
739	          ]
740	        ]
741	      }
742	    ],
743	    "figures": [],
744	    "analysis": "Surface features are fragile under editing. The crossover point where depth estimation becomes worse than binary detection occurs at approximately 12% word replacement rate. Real-world synthetic text is routinely edited at this level or above, further limiting practical applicability.\n\n\nEditing disrupts the surface features that carry all the signal. Even 5% random word replacement drops F1 by 0.05 because replaced words tend to be common words replaced with less-common alternatives, artificially inflating hapax_ratio and masking vocabulary depletion. At 20%, the editing noise dominates the depth signal. LLM- simulated editing (light rephrasing) is particularly damaging (0.63) because the editing LLM introduces its own vocabulary preferences, adding a second generator's fingerprint on top of the original. Since the classifier relies on vocabulary statistics, any post-hoc vocabulary injection confounds depth estimation. This confirms the fragility of surface-feature-based depth estimation in realistic scenarios where synthetic text is edited before publication.\n"
745	  },
746	  {
747	    "name": "ld_score_feature",
748	    "description": "Add LD-Score (character-distribution signature) as additional feature. Tests whether character-level features provide complementary depth signal.\n",
749	    "results": {
750	      "surface_plus_ld_macro_f1": 0.83,
751	      "ld_only_macro_f1": 0.61,
752	      "full_plus_ld_macro_f1": 0.83,
753	      "ld_cross_gen_loo_f1": 0.46,
754	      "ld_feature_importance": 0.05
755	    },
756	    "tables": [
757	      {
758	        "name": "Table 16: LD-Score Feature Analysis",
759	        "columns": [
760	          "Feature_Set",
761	          "Macro_F1",
762	          "LOO_Cross_Gen_F1"
763	        ],
764	        "rows": [
765	          [
766	            "surface_only",
767	            0.82,
768	            0.48
769	          ],
770	          [
771	            "ld_only",
772	            0.61,
773	            0.46
774	          ],
775	          [
776	            "surface + ld",
777	            0.83,
778	            0.49
779	          ],
780	          [
781	            "full + ld",
782	            0.83,
783	            0.5
784	          ]
785	        ]
786	      }
787	    ],
788	    "figures": [],
789	    "analysis": "LD-Score is a character-level echo of word-level vocabulary depletion — correlated but not complementary. It does not provide a new axis of depth information. Including it in the paper is optional; it addresses a potential reviewer question but doesn't change conclusions.\n\n\nLD-Score as a standalone feature performs moderately (0.61) — better than reference- model features (0.47) but worse than surface features (0.82). This is because character-level distributions partially capture vocabulary depletion through character frequency shifts, providing a smoothed proxy for hapax_ratio. However, adding LD-Score to surface features yields negligible improvement (+0.01) because the character-level signal is redundant with word-level surface statistics. Cross-generator transfer with LD-Score (0.46) is no better than without, confirming that character-level features also suffer from generator-specificity. LD-Score does not rescue the fundamental problem.\n"
790	  },
791	  {
792	    "name": "end_to_end_classifier",
793	    "description": "QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification. Compares learned representations vs handcrafted features.\n",
794	    "results": {
795	      "e2e_within_gen_macro_f1": 0.87,
796	      "e2e_cross_gen_loo_macro_f1": 0.53,
797	      "e2e_cross_gen_gen0_f1": 0.74,
798	      "e2e_cross_gen_gen1_f1": 0.42,
799	      "e2e_cross_gen_gen2plus_f1": 0.45,
800	      "e2e_vs_handcrafted_within_delta": 0.05,
801	      "e2e_vs_handcrafted_cross_delta": 0.05,
802	      "e2e_attention_analysis_top_tokens": [
803	        "the",
804	        "of",
805	        "is",
806	        ".",
807	        ","
808	      ]
809	    },
810	    "tables": [
811	      {
812	        "name": "Table 17: End-to-End vs Handcrafted Features",
813	        "columns": [
814	          "Model",
815	          "Within_Gen_F1",
816	          "Cross_Gen_LOO_F1",
817	          "Δ_Cross_Gen"
818	        ],
819	        "rows": [
820	          [
821	            "handcrafted (surface + ref)",
822	            0.83,
823	            0.48,
824	            "-"
825	          ],
826	          [
827	            "QLoRA Qwen3.5-0.8B",
828	            0.87,
829	            0.53,
830	            0.05
831	          ],
832	          [
833	            "handcrafted surface_only",
834	            0.82,
835	            0.48,
836	            "-"
837	          ]
838	        ]
839	      }
840	    ],
841	    "figures": [],
842	    "analysis": "The end-to-end model confirms the ceiling: even with 0.8B parameters and full sequence access, cross-generator depth estimation barely exceeds chance for gen-1 and gen-2+. The model learns vocabulary impoverishment more efficiently than handcrafted features (+0.05 within-gen) but cannot overcome the fundamental generator-specificity of the signal (+0.05 cross-gen, still at 0.53). This closes the \"maybe a bigger model could find it\" escape hatch — the signal genuinely isn't there for cross-generator depth estimation.\n\nThe end-to-end model achieves marginally higher within-generator F1 (0.87 vs 0.82) by learning soft vocabulary depletion features beyond hapax_ratio and TTR — it implicitly captures the full vocabulary distribution shift through its representations. However, cross-generator transfer shows only modest improvement (0.53 vs 0.48), meaning the learned representations are also predominantly generator-specific. Attention analysis reveals the model focuses on high-frequency function words and punctuation — exactly the tokens whose usage patterns shift under vocabulary impoverishment. The learned model does not discover hidden distributional structure beyond surface statistics; it simply learns a richer encoding of the same surface phenomenon. The 0.05 cross-gen improvement over handcrafted features is the only hint that some generator-invariant signal might exist in deeper representations, but it is not large enough to be practically useful.\n"
843	  }
844	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2965aa64-3bb8-445b-bebe-22aba79933d6",
  "isSidechain": false,
  "promptId": "00675285-eb7e-4fe5-a2b7-b441582ee0b5",
  "type": "user",
  "uuid": "3ce54063-632f-496a-a32c-ff2c6ba8ecc8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"feature_ablation\",\n    \"description\": \"Ablation of reference-only, surface-only, and full feature sets on MVP data (Pythia-2.8B generator, Pythia-410M reference, 3-class depth). Ordinal logistic regression + random forest, 5-fold CV.\\n\",\n    \"results\": {\n      \"surface_only_macro_f1\": 0.82,\n      \"surface_only_cv_std\": 0.015,\n      \"ref_only_macro_f1\": 0.47,\n      \"ref_only_cv_std\": 0.032,\n      \"full_macro_f1\": 0.83,\n      \"full_cv_std\": 0.014,\n      \"ref_minus_surface_delta\": -0.35,\n      \"full_minus_surface_delta\": 0.01,\n      \"permutation_importance_hapax_ratio\": 0.31,\n      \"permutation_importance_ttr\": 0.24,\n      \"permutation_importance_entropy_mean\": 0.04,\n      \"permutation_importance_entropy_std\": 0.03,\n      \"permutation_importance_tail_decay\": 0.02,\n      \"ref_features_added_significance_p\": 0.18\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2: Feature Ablation Results (3-class, MVP data)\",\n        \"columns\": [\n          \"Feature_Set\",\n          \"Macro_F1\",\n          \"Gen0_F1\",\n          \"Gen1_F1\",\n          \"Gen2plus_F1\",\n          \"CV_Std\"\n        ],\n        \"rows\": [\n          [\n            \"surface_only\",\n            0.82,\n            0.94,\n            0.75,\n            0.77,\n            0.015\n          ],\n          [\n            \"ref_only\",\n            0.47,\n            0.58,\n            0.38,\n            0.44,\n            0.032\n          ],\n          [\n            \"full\",\n            0.83,\n            0.95,\n            0.76,\n            0.78,\n            0.014\n          ],\n          [\n            \"chance\",\n            0.33,\n            0.33,\n            0.33,\n            0.33,\n            \"-\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 3: Permutation Feature Importance (Full Model)\",\n        \"columns\": [\n          \"Feature\",\n          \"Importance\",\n          \"Std\"\n        ],\n        \"rows\": [\n          [\n            \"hapax_ratio\",\n            0.31,\n            0.04\n          ],\n          [\n            \"ttr\",\n            0.24,\n            0.03\n          ],\n          [\n            \"entropy_mean\",\n            0.04,\n            0.02\n          ],\n          [\n            \"entropy_std\",\n            0.03,\n            0.01\n          ],\n          [\n            \"entropy_min\",\n            0.02,\n            0.01\n          ],\n          [\n            \"entropy_max\",\n            0.01,\n            0.01\n          ],\n          [\n            \"tail_decay\",\n            0.02,\n            0.01\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 2 is falsified. The ablation decisively shows that reference-model features carry no independent signal. The full model's marginal +0.01 over surface-only is within noise. This result is consistent with the hypothesis that autoregressive generation entropy converges to a near-stationary distribution by gen-1, while vocabulary depletion (a surface-level phenomenon) continues to accumulate. The practical implication: a $0 feature (hapax_ratio) matches the expensive reference-model inference pipeline.\\n\\n\\nSurface features alone recover 97.6% of full-model performance (0.82 vs 0.84 MVP). hapax_ratio and TTR dominate because recursive generation progressively depletes rare vocabulary — a mechanical consequence of autoregressive sampling from a fixed distribution. Reference-model entropy statistics show near-chance 3-class performance (0.47) because the entropy distribution under the reference model converges rapidly across generation depths: by gen-1, the token-level surprise distribution is already close to its stationary form. Adding reference features to surface features yields only +0.01 F1 (not statistically significant, p=0.18 on paired bootstrap), confirming that entropy_mean/std/min/max carry redundant information already captured by vocabulary depletion proxies. The \\\"distributional fingerprint\\\" framing collapses — what we detect is vocabulary impoverishment, not a deeper distributional shift.\\n\"\n  },\n  {\n    \"name\": \"cross_generator_evaluation\",\n    \"description\": \"5 generators (Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, Pythia-1B). 1000 seeds × 5 generators × 5 depths = 25K chains. Leave-one-generator-out CV for cross-generator generalization. 3-class depth classification.\\n\",\n    \"results\": {\n      \"within_generator_avg_macro_f1\": 0.81,\n      \"leave_one_out_avg_macro_f1\": 0.48,\n      \"leave_one_out_std\": 0.07,\n      \"leave_one_out_gen0_f1\": 0.68,\n      \"leave_one_out_gen1_f1\": 0.38,\n      \"leave_one_out_gen2plus_f1\": 0.42,\n      \"loo_held_out_pythia28b_f1\": 0.52,\n      \"loo_held_out_olmo_f1\": 0.44,\n      \"loo_held_out_qwen2b_f1\": 0.43,\n      \"loo_held_out_qwen08b_f1\": 0.5,\n      \"loo_held_out_pythia1b_f1\": 0.53,\n      \"gen1_vs_gen2plus_binary_loo_f1\": 0.54,\n      \"pooled_all_generators_macro_f1\": 0.62\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Cross-Generator Generalization (Leave-One-Out)\",\n        \"columns\": [\n          \"Held_Out_Generator\",\n          \"Macro_F1\",\n          \"Gen0_F1\",\n          \"Gen1_F1\",\n          \"Gen2plus_F1\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-2.8B\",\n            0.52,\n            0.71,\n            0.4,\n            0.45\n          ],\n          [\n            \"OLMo-2-1B\",\n            0.44,\n            0.65,\n            0.34,\n            0.38\n          ],\n          [\n            \"Qwen3.5-2B\",\n            0.43,\n            0.64,\n            0.35,\n            0.39\n          ],\n          [\n            \"Qwen3.5-0.8B\",\n            0.5,\n            0.7,\n            0.38,\n            0.43\n          ],\n          [\n            \"Pythia-1B\",\n            0.53,\n            0.72,\n            0.42,\n            0.46\n          ],\n          [\n            \"**Average**\",\n            \"**0.48**\",\n            \"**0.68**\",\n            \"**0.38**\",\n            \"**0.42**\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5: Within- vs Cross-Generator Comparison\",\n        \"columns\": [\n          \"Setting\",\n          \"Macro_F1\",\n          \"Δ_vs_Within\"\n        ],\n        \"rows\": [\n          [\n            \"within_generator_avg\",\n            0.81,\n            \"-\"\n          ],\n          [\n            \"leave_one_out_avg\",\n            0.48,\n            -0.33\n          ],\n          [\n            \"pooled_all_generators\",\n            0.62,\n            -0.19\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 1 fails in its generalization requirement. Cross-generator macro-F1 of 0.48 is barely above chance (0.33). The fundamental problem: surface vocabulary statistics are generator-specific calibration artifacts. A model that learns \\\"hapax_ratio < 0.30 means gen-2+\\\" from Pythia data will misclassify Qwen gen-0 text (which may have hapax_ratio ~0.35 vs Pythia gen-0 ~0.45). Without independent reference-model signal (which plan_001 showed is absent), there is no generator-invariant depth feature. The pooled setting (0.62) is inflated by within-generator signal bleeding through the non-held-out generators in training.\\n\\n\\nWithin-generator performance remains strong (~0.81) because each generator has a characteristic vocabulary depletion rate that surface features learn. But leave-one-out drops catastrophically to 0.48 because the absolute levels of hapax_ratio and TTR are generator-specific: Qwen models produce systematically different type-token ratios than Pythia models at every depth. The classifier learns generator-specific thresholds, not universal depth signatures. Gen-0 identification is partially salvaged (0.68) because human-written text has a consistently distinct surface profile regardless of which generator produces the synthetic continuations. Gen-1 vs gen-2+ discrimination is near chance (0.38/0.42) in the cross-generator setting because the vocabulary depletion curves of different generators at depth 1 overlap with other generators at depth 2+. Pythia-family held-out sets perform slightly better (0.52-0.53) due to Pythia-1B sharing vocabulary statistics with Pythia-2.8B in the training fold. Cross- family transfer (Qwen held out) is worst (0.43-0.44). This confirms that surface features are generator-specific, not universal depth markers.\\n\"\n  },\n  {\n    \"name\": \"cross_family_reference_model\",\n    \"description\": \"Test OLMo-2-1B and Qwen3.5-0.8B as reference models (replacing Pythia-410M) for feature extraction. Full cross of 3 reference models × 5 generators.\\n\",\n    \"results\": {\n      \"pythia_ref_cross_gen_macro_f1\": 0.48,\n      \"olmo_ref_cross_gen_macro_f1\": 0.45,\n      \"qwen_ref_cross_gen_macro_f1\": 0.44,\n      \"best_ref_model\": \"pythia_410m\",\n      \"ref_model_variance_std\": 0.02,\n      \"ensemble_3ref_cross_gen_macro_f1\": 0.5,\n      \"ref_only_olmo_macro_f1\": 0.43,\n      \"ref_only_qwen_macro_f1\": 0.41\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Reference Model Comparison (Leave-One-Generator-Out)\",\n        \"columns\": [\n          \"Reference_Model\",\n          \"LOO_Macro_F1\",\n          \"Ref_Only_F1\",\n          \"Surface_Only_F1\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-410M\",\n            0.48,\n            0.47,\n            0.82\n          ],\n          [\n            \"OLMo-2-1B\",\n            0.45,\n            0.43,\n            0.82\n          ],\n          [\n            \"Qwen3.5-0.8B\",\n            0.44,\n            0.41,\n            0.82\n          ],\n          [\n            \"Ensemble (3 refs)\",\n            0.5,\n            0.49,\n            0.82\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Reference model choice is irrelevant because the underlying signal is absent. Surface features remain constant at 0.82 regardless of reference model (they don't use it), confirming surface features as the sole discriminative mechanism. The experiment conclusively addresses RC2 but in a way that undermines the paper: the signal isn't architecture-specific because there is no reference-model signal to be architecture- specific about.\\n\\n\\nChanging the reference model does not rescue cross-generator performance because the bottleneck is not reference model choice — it is the absence of depth-discriminative signal in the entropy statistics themselves. All three reference models produce similarly uninformative entropy distributions because the phenomenon is fundamental: autoregressive generation entropy converges to near-stationary levels by gen-1 regardless of which model measures it. The slight advantage of Pythia-410M (0.48 vs 0.44-0.45) is a minor architectural compatibility effect with the Pythia generators in the training set, not genuine signal. Ensembling three reference models yields only +0.02 over the best single model, confirming the features are redundant across reference architectures. This rules out RC2 concerns as irrelevant — the problem is not architecture-specific artifacts but rather the fundamental convergence of generation entropy.\\n\"\n  },\n  {\n    \"name\": \"downstream_utility\",\n    \"description\": \"Fine-tune Pythia-410M on depth-stratified data subsets. Measure perplexity degradation as function of training data depth. Compare depth-aware filtering vs binary baselines (FastDetectGPT, LD-Score threshold).\\n\",\n    \"results\": {\n      \"depth_quality_spearman_rho\": 0.19,\n      \"depth_quality_spearman_p\": 0.04,\n      \"ppl_gen0_only\": 18.2,\n      \"ppl_gen1_mixed\": 19.1,\n      \"ppl_gen2plus_mixed\": 19.8,\n      \"ppl_unfiltered\": 19.5,\n      \"depth_filter_top1_ppl\": 18.5,\n      \"binary_filter_fastdetect_ppl\": 18.4,\n      \"binary_filter_ldscore_ppl\": 18.6,\n      \"depth_filter_vs_binary_perf_gap_pct\": -0.3,\n      \"depth_filter_data_retained_pct\": 38,\n      \"binary_filter_data_retained_pct\": 42\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Downstream Fine-tuning Perplexity\",\n        \"columns\": [\n          \"Training_Data\",\n          \"Perplexity\",\n          \"Data_Size_pct\"\n        ],\n        \"rows\": [\n          [\n            \"gen-0 only\",\n            18.2,\n            33\n          ],\n          [\n            \"gen-0 + gen-1\",\n            18.8,\n            67\n          ],\n          [\n            \"all depths unfiltered\",\n            19.5,\n            100\n          ],\n          [\n            \"depth-aware filter (≤gen-1)\",\n            18.5,\n            38\n          ],\n          [\n            \"FastDetectGPT binary filter\",\n            18.4,\n            42\n          ],\n          [\n            \"LD-Score binary filter\",\n            18.6,\n            40\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8: Depth-Quality Correlation\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\"\n        ],\n        \"rows\": [\n          [\n            \"Spearman ρ (depth vs ppl_degradation)\",\n            0.19\n          ],\n          [\n            \"p-value\",\n            0.04\n          ],\n          [\n            \"depth_filter vs best_binary gap\",\n            \"-0.3%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 3 fails. While a statistically significant correlation exists (p=0.04), the effect size is negligible (ρ=0.19) and depth-aware filtering underperforms binary baselines by 0.3%. The ordinal depth information adds no practical value over binary classification for data curation. This is the expected consequence of plan_001 and plan_002 results: if depth estimation relies on generator-specific surface features and cross-generator transfer is poor, the depth predictions are too noisy to provide downstream utility beyond what binary detection already offers.\\n\\n\\nA weak positive correlation (ρ=0.19) exists between predicted depth and quality degradation, but it is barely significant and practically meaningless. The perplexity difference between gen-0-only and gen-2+-mixed training is modest (~1.6 points) because vocabulary impoverishment in synthetic text creates a noisy but not catastrophic training signal — the model still learns reasonable language statistics from synthetic text, just with slightly depleted rare-word coverage. Depth-aware filtering performs equivalently to binary baselines (-0.3% gap, within noise) because the depth classifier's cross-generator errors (from plan_002) introduce enough noise to eliminate any advantage over simple binary filtering. FastDetectGPT actually edges out depth-aware filtering by 0.1 ppl because it makes fewer classification errors on the binary task than our system makes on the harder ordinal task. Claim 3 effectively fails — depth-aware filtering provides no practical advantage over binary baselines.\\n\"\n  },\n  {\n    \"name\": \"prompt_type_comparison\",\n    \"description\": \"Compare continuation vs elaboration vs inspired_rewriting chains. 1000 seeds, Pythia-2.8B, 3 prompt types, 5 depths each.\\n\",\n    \"results\": {\n      \"continuation_within_gen_f1\": 0.82,\n      \"elaboration_within_gen_f1\": 0.78,\n      \"inspired_rewriting_within_gen_f1\": 0.69,\n      \"continuation_cross_prompt_f1\": 0.61,\n      \"elaboration_cross_prompt_f1\": 0.58,\n      \"inspired_rewriting_cross_prompt_f1\": 0.52,\n      \"convergence_speed_continuation_depth\": 2,\n      \"convergence_speed_elaboration_depth\": 2,\n      \"convergence_speed_rewriting_depth\": 1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Prompt Type Comparison\",\n        \"columns\": [\n          \"Prompt_Type\",\n          \"Within_Gen_F1\",\n          \"Cross_Prompt_F1\",\n          \"Convergence_Depth\"\n        ],\n        \"rows\": [\n          [\n            \"continuation\",\n            0.82,\n            0.61,\n            2\n          ],\n          [\n            \"elaboration\",\n            0.78,\n            0.58,\n            2\n          ],\n          [\n            \"inspired_rewriting\",\n            0.69,\n            0.52,\n            1\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"All prompt types show rapid convergence, supporting H₁. The depth signal ceiling is approximately 2 effective classes (gen-0 vs synthetic) for rewriting and 3 classes (gen-0/gen-1/gen-2+) for continuation — but only within-generator. The prompt type comparison reveals an additional confound: not only is the signal generator-specific, it is prompt-type-specific. This further narrows the practical applicability of depth estimation.\\n\\n\\nContinuation chains show the highest within-generator F1 (0.82) because they preserve the most topic continuity, making vocabulary depletion the dominant signal. Elaboration is slightly lower (0.78) due to topic drift introducing vocabulary variance that partially masks depletion. Inspired rewriting shows the weakest signal (0.69) because each generation step introduces substantially new vocabulary, partially resetting the depletion signal. Cross-prompt transfer is poor across the board because each prompt type induces a different vocabulary depletion rate — the classifier learns prompt- type-specific thresholds. Convergence analysis shows all three types stabilize by depth 2 (rewriting by depth 1), supporting H₁: even non-paraphrastic chains converge rapidly. The rewriting chains converge fastest because the larger semantic jumps quickly exhaust the generator's preferred vocabulary, reaching a \\\"vocabulary floor\\\" by gen-1.\\n\"\n  },\n  {\n    \"name\": \"paraphrastic_comparison\",\n    \"description\": \"Construct parallel paraphrasing chains for direct comparison with continuation chains. Test attractor convergence theory — H₁ vs H₂.\\n\",\n    \"results\": {\n      \"paraphrase_within_gen_f1\": 0.64,\n      \"continuation_within_gen_f1\": 0.82,\n      \"paraphrase_convergence_depth\": 1,\n      \"continuation_convergence_depth\": 2,\n      \"paraphrase_gen1_vs_gen2plus_f1\": 0.41,\n      \"continuation_gen1_vs_gen2plus_f1\": 0.58,\n      \"kl_depth2_vs_depth3_paraphrase\": 0.008,\n      \"kl_depth2_vs_depth3_continuation\": 0.031\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Paraphrastic vs Non-Paraphrastic Chains\",\n        \"columns\": [\n          \"Chain_Type\",\n          \"Macro_F1_3class\",\n          \"Gen1_vs_Gen2plus_F1\",\n          \"Convergence_Depth\",\n          \"KL_d2_d3\"\n        ],\n        \"rows\": [\n          [\n            \"paraphrasing\",\n            0.64,\n            0.41,\n            1,\n            0.008\n          ],\n          [\n            \"continuation\",\n            0.82,\n            0.58,\n            2,\n            0.031\n          ],\n          [\n            \"elaboration\",\n            0.78,\n            0.52,\n            2,\n            0.024\n          ],\n          [\n            \"inspired_rewriting\",\n            0.69,\n            0.44,\n            1,\n            0.012\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"H₁ is confirmed: non-paraphrastic chains also converge, just 1 step slower than paraphrastic chains. This extends the ACL 2025 attractor theory to non-paraphrastic settings — arguably the most publishable finding in the worst case. The convergence is driven by autoregressive sampling from a fixed model concentrating probability mass on preferred tokens regardless of prompt type, creating a universal vocabulary attractor. Depth signal is fundamentally bounded at ~2-3 classes.\\n\\n\\nParaphrasing chains converge faster than continuation chains (by depth 1 vs depth 2), consistent with attractor cycle theory from ACL 2025. Paraphrasing F1 is lower (0.64) because the semantic-preservation constraint limits vocabulary variation — paraphrases reuse similar word types, so hapax_ratio depletion is less pronounced. But crucially, continuation chains also converge by depth 2, meaning non-paraphrastic generation does NOT produce the unbounded divergence hypothesized in H₂. Both chain types reach near-stationary distributions within 2-3 steps. The KL divergence between depth-2 and depth-3 is negligible for both types (<0.04 nats). This is the key finding for the worst-case narrative: H₁ (convergence) holds even for non-paraphrastic chains, limiting depth signal to a maximum of ~2-3 discriminable classes and undermining the premise that non-paraphrastic chains produce monotonic divergence.\\n\"\n  },\n  {\n    \"name\": \"cross_model_chains\",\n    \"description\": \"Cross-model chains (different generator per depth step) vs single-model chains. 5 generators randomly assigned per step. 1000 seeds × 5 depths.\\n\",\n    \"results\": {\n      \"single_model_within_gen_f1\": 0.81,\n      \"cross_model_chain_f1\": 0.42,\n      \"cross_model_gen0_f1\": 0.65,\n      \"cross_model_gen1_f1\": 0.32,\n      \"cross_model_gen2plus_f1\": 0.35,\n      \"cross_model_binary_gen0_vs_rest_f1\": 0.67\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Single-Model vs Cross-Model Chains\",\n        \"columns\": [\n          \"Setting\",\n          \"Macro_F1\",\n          \"Gen0_F1\",\n          \"Gen1_F1\",\n          \"Gen2plus_F1\"\n        ],\n        \"rows\": [\n          [\n            \"single_model_chains\",\n            0.81,\n            0.94,\n            0.75,\n            0.77\n          ],\n          [\n            \"cross_model_chains\",\n            0.42,\n            0.65,\n            0.32,\n            0.35\n          ],\n          [\n            \"chance\",\n            0.33,\n            0.33,\n            0.33,\n            0.33\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The most ecologically valid setting (cross-model chains) produces near-chance depth estimation. This confirms that the MVP result (0.84) was an artifact of single-model evaluation: the classifier learned Pythia-2.8B's specific vocabulary depletion curve, not a universal depth signature. In realistic web contamination scenarios with diverse generators, depth estimation beyond binary (human vs synthetic) is not feasible with current features.\\n\\n\\nCross-model chains are devastating for depth estimation (0.42 macro-F1). When different generators produce each depth step, the vocabulary statistics at any given depth reflect the current-step generator's preferences more than the cumulative depth of the chain. A text generated by Qwen at depth-2 in a chain may have higher hapax_ratio than text generated by Pythia-1B at depth-1, because Qwen has a richer base vocabulary. The generator-switching effectively randomizes the surface features that the classifier depends on. Gen-0 identification survives partially (0.65) because human text is still distinct from any generator, but gen-1/gen-2+ classification is near-chance. This is the most realistic contamination scenario and the most damning result for practical applicability.\\n\"\n  },\n  {\n    \"name\": \"multi_domain_seeds\",\n    \"description\": \"Expand to 4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC), creative writing (WritingPrompts). 500 seeds per domain × 5 depths, Pythia-2.8B generator.\\n\",\n    \"results\": {\n      \"wikipedia_within_domain_f1\": 0.83,\n      \"news_within_domain_f1\": 0.8,\n      \"scientific_within_domain_f1\": 0.76,\n      \"creative_within_domain_f1\": 0.72,\n      \"cross_domain_avg_f1\": 0.59,\n      \"pooled_all_domains_f1\": 0.74,\n      \"scientific_hapax_ratio_gen0_median\": 0.52,\n      \"creative_hapax_ratio_gen0_median\": 0.38\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Multi-Domain Results\",\n        \"columns\": [\n          \"Domain\",\n          \"Within_Domain_F1\",\n          \"Gen0_hapax_median\",\n          \"Gen2plus_hapax_median\",\n          \"Δ_hapax\"\n        ],\n        \"rows\": [\n          [\n            \"Wikipedia\",\n            0.83,\n            0.47,\n            0.26,\n            0.21\n          ],\n          [\n            \"News\",\n            0.8,\n            0.44,\n            0.27,\n            0.17\n          ],\n          [\n            \"Scientific\",\n            0.76,\n            0.52,\n            0.35,\n            0.17\n          ],\n          [\n            \"Creative\",\n            0.72,\n            0.38,\n            0.28,\n            0.1\n          ],\n          [\n            \"Cross-domain avg\",\n            0.59,\n            \"-\",\n            \"-\",\n            \"-\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain is yet another confound. The depth signal is domain-specific because the magnitude of vocabulary depletion depends on the seed text's lexical richness. Combined with generator-specificity and prompt-type-specificity, this creates a three-way interaction that makes general-purpose depth estimation impractical. A classifier trained on Wikipedia+news will overestimate depth for creative writing (lower base hapax) and underestimate it for scientific text (higher base hapax).\\n\\n\\nWithin-domain performance is reasonable but varies by domain. Wikipedia/news are easiest because their seed texts have high hapax_ratio (specialized proper nouns, rare terms) that generation rapidly depletes. Scientific text starts with high rare-word density (technical terms) but the generator sometimes preserves or regenerates these, creating noise. Creative writing is hardest because its base vocabulary is less specialized — the hapax_ratio gap between gen-0 and gen-1 is smaller. Cross-domain transfer drops to 0.59 because each domain has different baseline vocabulary statistics: scientific gen-0 text (hapax_ratio ~0.52) overlaps with creative gen-0 (~0.38), confounding domain and depth. This adds another axis of non-generalization beyond generator and prompt type.\\n\"\n  },\n  {\n    \"name\": \"finer_grained_ordinal\",\n    \"description\": \"5-class ordinal classification (gen-0 through gen-4) on non-paraphrastic continuation chains. Tests if more than 3-class depth signal exists.\\n\",\n    \"results\": {\n      \"ordinal_5class_macro_f1\": 0.52,\n      \"ordinal_5class_gen0_f1\": 0.91,\n      \"ordinal_5class_gen1_f1\": 0.58,\n      \"ordinal_5class_gen2_f1\": 0.38,\n      \"ordinal_5class_gen3_f1\": 0.31,\n      \"ordinal_5class_gen4_f1\": 0.33,\n      \"ordinal_3class_macro_f1\": 0.82,\n      \"adjacent_class_confusion_rate\": 0.44,\n      \"mae_ordinal\": 0.72\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: 5-Class Ordinal Classification\",\n        \"columns\": [\n          \"Class\",\n          \"Precision\",\n          \"Recall\",\n          \"F1\"\n        ],\n        \"rows\": [\n          [\n            \"gen-0\",\n            0.93,\n            0.9,\n            0.91\n          ],\n          [\n            \"gen-1\",\n            0.54,\n            0.62,\n            0.58\n          ],\n          [\n            \"gen-2\",\n            0.36,\n            0.4,\n            0.38\n          ],\n          [\n            \"gen-3\",\n            0.29,\n            0.33,\n            0.31\n          ],\n          [\n            \"gen-4\",\n            0.31,\n            0.35,\n            0.33\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 14: 5-Class Confusion Matrix\",\n        \"columns\": [\n          \"Predicted→\",\n          \"gen-0\",\n          \"gen-1\",\n          \"gen-2\",\n          \"gen-3\",\n          \"gen-4\"\n        ],\n        \"rows\": [\n          [\n            \"gen-0\",\n            0.9,\n            0.07,\n            0.02,\n            0.01,\n            0.0\n          ],\n          [\n            \"gen-1\",\n            0.09,\n            0.62,\n            0.18,\n            0.07,\n            0.04\n          ],\n          [\n            \"gen-2\",\n            0.03,\n            0.21,\n            0.4,\n            0.22,\n            0.14\n          ],\n          [\n            \"gen-3\",\n            0.02,\n            0.1,\n            0.24,\n            0.33,\n            0.31\n          ],\n          [\n            \"gen-4\",\n            0.01,\n            0.07,\n            0.16,\n            0.28,\n            0.48\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Finer-grained estimation is not feasible. The depth signal has a hard ceiling at ~3 discriminable classes, consistent with convergence by depth 2. The confusion matrix shows a clear diagonal-plus-adjacent pattern typical of ordinal features with limited dynamic range. Gen-3 and gen-4 are essentially exchangeable. This further limits the practical scope of depth estimation.\\n\\n\\n5-class performance drops sharply to 0.52 macro-F1 (from 0.82 for 3-class), with gen-2 through gen-4 collapsing into near-chance mutual confusion. This is the direct consequence of H₁ convergence: by depth 2, the feature distributions have already converged, so gen-2/gen-3/gen-4 are statistically indistinguishable. The confusion is concentrated in adjacent classes (44% of errors are off-by-one), consistent with a smooth convergence rather than discrete depth categories. Gen-0 remains easily identified (0.91) and gen-1 partially (0.58), but beyond gen-1 the signal is gone. This confirms the practical ceiling is 2-3 discriminable depth classes, not finer- grained ordinal estimation.\\n\"\n  },\n  {\n    \"name\": \"human_edit_robustness\",\n    \"description\": \"Robustness to simulated human edits. (A) Random word replacement at 5%, 10%, 20%. (B) LLM-simulated editing (light rephrasing of random sentences).\\n\",\n    \"results\": {\n      \"baseline_no_edit_f1\": 0.82,\n      \"random_replace_5pct_f1\": 0.77,\n      \"random_replace_10pct_f1\": 0.7,\n      \"random_replace_20pct_f1\": 0.58,\n      \"llm_edit_light_f1\": 0.63,\n      \"llm_edit_light_gen0_f1\": 0.82,\n      \"llm_edit_light_gen1_f1\": 0.51,\n      \"llm_edit_light_gen2plus_f1\": 0.48\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Robustness to Human Edits\",\n        \"columns\": [\n          \"Edit_Type\",\n          \"Edit_Rate\",\n          \"Macro_F1\",\n          \"Δ_vs_Baseline\"\n        ],\n        \"rows\": [\n          [\n            \"none\",\n            \"0%\",\n            0.82,\n            \"-\"\n          ],\n          [\n            \"random_replace\",\n            \"5%\",\n            0.77,\n            -0.05\n          ],\n          [\n            \"random_replace\",\n            \"10%\",\n            0.7,\n            -0.12\n          ],\n          [\n            \"random_replace\",\n            \"20%\",\n            0.58,\n            -0.24\n          ],\n          [\n            \"llm_simulated\",\n            \"light\",\n            0.63,\n            -0.19\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Surface features are fragile under editing. The crossover point where depth estimation becomes worse than binary detection occurs at approximately 12% word replacement rate. Real-world synthetic text is routinely edited at this level or above, further limiting practical applicability.\\n\\n\\nEditing disrupts the surface features that carry all the signal. Even 5% random word replacement drops F1 by 0.05 because replaced words tend to be common words replaced with less-common alternatives, artificially inflating hapax_ratio and masking vocabulary depletion. At 20%, the editing noise dominates the depth signal. LLM- simulated editing (light rephrasing) is particularly damaging (0.63) because the editing LLM introduces its own vocabulary preferences, adding a second generator's fingerprint on top of the original. Since the classifier relies on vocabulary statistics, any post-hoc vocabulary injection confounds depth estimation. This confirms the fragility of surface-feature-based depth estimation in realistic scenarios where synthetic text is edited before publication.\\n\"\n  },\n  {\n    \"name\": \"ld_score_feature\",\n    \"description\": \"Add LD-Score (character-distribution signature) as additional feature. Tests whether character-level features provide complementary depth signal.\\n\",\n    \"results\": {\n      \"surface_plus_ld_macro_f1\": 0.83,\n      \"ld_only_macro_f1\": 0.61,\n      \"full_plus_ld_macro_f1\": 0.83,\n      \"ld_cross_gen_loo_f1\": 0.46,\n      \"ld_feature_importance\": 0.05\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 16: LD-Score Feature Analysis\",\n        \"columns\": [\n          \"Feature_Set\",\n          \"Macro_F1\",\n          \"LOO_Cross_Gen_F1\"\n        ],\n        \"rows\": [\n          [\n            \"surface_only\",\n            0.82,\n            0.48\n          ],\n          [\n            \"ld_only\",\n            0.61,\n            0.46\n          ],\n          [\n            \"surface + ld\",\n            0.83,\n            0.49\n          ],\n          [\n            \"full + ld\",\n            0.83,\n            0.5\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LD-Score is a character-level echo of word-level vocabulary depletion — correlated but not complementary. It does not provide a new axis of depth information. Including it in the paper is optional; it addresses a potential reviewer question but doesn't change conclusions.\\n\\n\\nLD-Score as a standalone feature performs moderately (0.61) — better than reference- model features (0.47) but worse than surface features (0.82). This is because character-level distributions partially capture vocabulary depletion through character frequency shifts, providing a smoothed proxy for hapax_ratio. However, adding LD-Score to surface features yields negligible improvement (+0.01) because the character-level signal is redundant with word-level surface statistics. Cross-generator transfer with LD-Score (0.46) is no better than without, confirming that character-level features also suffer from generator-specificity. LD-Score does not rescue the fundamental problem.\\n\"\n  },\n  {\n    \"name\": \"end_to_end_classifier\",\n    \"description\": \"QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification. Compares learned representations vs handcrafted features.\\n\",\n    \"results\": {\n      \"e2e_within_gen_macro_f1\": 0.87,\n      \"e2e_cross_gen_loo_macro_f1\": 0.53,\n      \"e2e_cross_gen_gen0_f1\": 0.74,\n      \"e2e_cross_gen_gen1_f1\": 0.42,\n      \"e2e_cross_gen_gen2plus_f1\": 0.45,\n      \"e2e_vs_handcrafted_within_delta\": 0.05,\n      \"e2e_vs_handcrafted_cross_delta\": 0.05,\n      \"e2e_attention_analysis_top_tokens\": [\n        \"the\",\n        \"of\",\n        \"is\",\n        \".\",\n        \",\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 17: End-to-End vs Handcrafted Features\",\n        \"columns\": [\n          \"Model\",\n          \"Within_Gen_F1\",\n          \"Cross_Gen_LOO_F1\",\n          \"Δ_Cross_Gen\"\n        ],\n        \"rows\": [\n          [\n            \"handcrafted (surface + ref)\",\n            0.83,\n            0.48,\n            \"-\"\n          ],\n          [\n            \"QLoRA Qwen3.5-0.8B\",\n            0.87,\n            0.53,\n            0.05\n          ],\n          [\n            \"handcrafted surface_only\",\n            0.82,\n            0.48,\n            \"-\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The end-to-end model confirms the ceiling: even with 0.8B parameters and full sequence access, cross-generator depth estimation barely exceeds chance for gen-1 and gen-2+. The model learns vocabulary impoverishment more efficiently than handcrafted features (+0.05 within-gen) but cannot overcome the fundamental generator-specificity of the signal (+0.05 cross-gen, still at 0.53). This closes the \\\"maybe a bigger model could find it\\\" escape hatch — the signal genuinely isn't there for cross-generator depth estimation.\\n\\nThe end-to-end model achieves marginally higher within-generator F1 (0.87 vs 0.82) by learning soft vocabulary depletion features beyond hapax_ratio and TTR — it implicitly captures the full vocabulary distribution shift through its representations. However, cross-generator transfer shows only modest improvement (0.53 vs 0.48), meaning the learned representations are also predominantly generator-specific. Attention analysis reveals the model focuses on high-frequency function words and punctuation — exactly the tokens whose usage patterns shift under vocabulary impoverishment. The learned model does not discover hidden distributional structure beyond surface statistics; it simply learns a richer encoding of the same surface phenomenon. The 0.05 cross-gen improvement over handcrafted features is the only hint that some generator-invariant signal might exist in deeper representations, but it is not large enough to be practically useful.\\n\"\n  }\n]",
      "numLines": 844,
      "startLine": 1,
      "totalLines": 844
    }
  },
  "sourceToolAssistantUUID": "2965aa64-3bb8-445b-bebe-22aba79933d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T18:37:03.299Z_

<details><summary>↩ Tool result · `toolu_01WJTuCwt53eBqRMTovMCmVW`</summary>

```text
1	# Paper Framing — gen-depth-fingerprint
2	
3	## Target Venue
4	- Primary: AAAI 2027 (deadline: August 2, 2026)
5	- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4
6	- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)
7	
8	## Core Insight
9	Non-paraphrastic LLM generation chains (continuation, elaboration) operate in an unbounded semantic state space — unlike paraphrasing chains that converge to attractor cycles (ACL 2025). This means distributional drift accumulates monotonically with generation depth, leaving detectable "fingerprints" in token-level statistics under a reference model. These fingerprints enable ordinal depth estimation, unlocking risk-stratified data curation beyond binary real/synthetic filtering.
10	
11	## Core Claims (3 条，均可证伪)
12	
13	**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).
14	
15	**Claim 2 — Distributional Fingerprint Independence**: Reference-model-derived features (entropy statistics, tail-distribution decay) carry independent depth signal beyond surface vocabulary statistics (TTR, hapax ratio). Ablation: reference-only features achieve significantly higher F1 than surface-only features, or at minimum provide significant complementary signal.
16	
17	**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.
18	
19	## Story Spine
20	
21	**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).
22	
23	**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.
24	
25	**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation as an empirical phenomenon with practical implications for data governance. We formalize two competing hypotheses — H₁ (convergence: recursive generation tends toward a distributional fixed point even for non-paraphrastic chains) vs H₂ (divergence: non-paraphrastic chains accumulate monotonic drift) — and test them via depth-dependent distributional features under a reference model. Regardless of which hypothesis prevails, the characterization itself provides actionable insight: if H₂, depth estimation enables risk-stratified curation; if H₁, we establish the theoretical ceiling for depth-based approaches.
26	
27	**Headline result template**: "On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines."
28	
29	## Anticipated Reviewer Concerns
30	
31	**RC1 — "Is this just vocabulary impoverishment?"**: If surface features (TTR, hapax) alone match full-feature performance, the "distributional fingerprint" framing is overclaimed. → Ablation experiment (Claim 2) directly addresses this.
32	
33	**RC2 — "Does this generalize beyond Pythia?"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).
34	
35	**RC3 — "Is 3-class sufficient? Why not finer-grained?"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.
36	
37	**RC4 — "How realistic are single-model chains?"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).
38	
39	**RC5 — "What about human editing / post-processing?"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).
40	
41	**RC6 — "Ecological validity — continuation vs real web content"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).
42	
43	## Venue Fit
44	- AAAI 2027: Strong fit — data governance + ML methodology. The H₁/H₂ hypothesis-testing framing positions it as empirical science, not just a classifier paper.
45	- EMNLP 2026: Excellent fit — directly addresses special theme "New Missions for NLP Research" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work.
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "999f4b29-406c-4c77-b300-b68e335cc12e",
  "isSidechain": false,
  "promptId": "00675285-eb7e-4fe5-a2b7-b441582ee0b5",
  "type": "user",
  "uuid": "879dfe50-6373-4e44-bc70-3deba2809feb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/paper_framing.md",
      "content": "# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- Primary: AAAI 2027 (deadline: August 2, 2026)\n- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains (continuation, elaboration) operate in an unbounded semantic state space — unlike paraphrasing chains that converge to attractor cycles (ACL 2025). This means distributional drift accumulates monotonically with generation depth, leaving detectable \"fingerprints\" in token-level statistics under a reference model. These fingerprints enable ordinal depth estimation, unlocking risk-stratified data curation beyond binary real/synthetic filtering.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).\n\n**Claim 2 — Distributional Fingerprint Independence**: Reference-model-derived features (entropy statistics, tail-distribution decay) carry independent depth signal beyond surface vocabulary statistics (TTR, hapax ratio). Ablation: reference-only features achieve significantly higher F1 than surface-only features, or at minimum provide significant complementary signal.\n\n**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.\n\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation as an empirical phenomenon with practical implications for data governance. We formalize two competing hypotheses — H₁ (convergence: recursive generation tends toward a distributional fixed point even for non-paraphrastic chains) vs H₂ (divergence: non-paraphrastic chains accumulate monotonic drift) — and test them via depth-dependent distributional features under a reference model. Regardless of which hypothesis prevails, the characterization itself provides actionable insight: if H₂, depth estimation enables risk-stratified curation; if H₁, we establish the theoretical ceiling for depth-based approaches.\n\n**Headline result template**: \"On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: If surface features (TTR, hapax) alone match full-feature performance, the \"distributional fingerprint\" framing is overclaimed. → Ablation experiment (Claim 2) directly addresses this.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\n\n**RC3 — \"Is 3-class sufficient? Why not finer-grained?\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\n\n**RC4 — \"How realistic are single-model chains?\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\n\n**RC5 — \"What about human editing / post-processing?\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\n\n**RC6 — \"Ecological validity — continuation vs real web content\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\n\n## Venue Fit\n- AAAI 2027: Strong fit — data governance + ML methodology. The H₁/H₂ hypothesis-testing framing positions it as empirical science, not just a classifier paper.\n- EMNLP 2026: Excellent fit — directly addresses special theme \"New Missions for NLP Research\" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work.\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  },
  "sourceToolAssistantUUID": "999f4b29-406c-4c77-b300-b68e335cc12e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T18:37:03.296Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WJTuCwt53eBqRMTovMCmVW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ce54063-632f-496a-a32c-ff2c6ba8ecc8",
  "isSidechain": false,
  "requestId": "req_011Cb2wpAik16kT6Cz45jF7N",
  "type": "assistant",
  "uuid": "999f4b29-406c-4c77-b300-b68e335cc12e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvMzPhXS5jES8XAzLuSt5P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11243,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11243
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T181213 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerp…",
  "leafUuid": "879dfe50-6373-4e44-bc70-3deba2809feb",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream ID",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13"
}
```

---

### Assistant

_source line 14 · 2026-05-14T18:37:32.712Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experimental data and paper framing. Let me synthesize the key findings:

1. **Feature ablation**: Surface features (hapax_ratio, TTR) explain nearly all signal. Reference-model features add negligible independent signal (0.82 vs 0.83 F1, p=0.18).

2. **Cross-generator**: Within-generator F1 = 0.81, leave-one-out F1 = 0.48 (near chance). Surface features are generator-specific.

3. **Cross-family reference**: Changing reference model doesn't help. 

4. **Downstream utility**: Depth-aware filtering underperforms binary baselines by 0.3%. ρ=0.19 is statistically significant but practically negligible.

5. **Prompt type comparison**: All prompt types show rapid convergence. Rewriting converges by depth 1, others by depth 2.

6. **Paraphrastic comparison**: H₁ confirmed — non-paraphrastic chains also converge, just 1 step slower. Key finding for the paper.

7. **Cross-model chains**: Near-chance (0.42) — most ecologically valid and most damning.

8. **Multi-domain**: Domain acts as a confound, with cross-domain F1 dropping to 0.59.

9. **Finer-grained ordinal**: Moving to 5-class classification drops performance to 0.52, suggesting the signal ceiling sits around 2-3 classes.

10. **Human edit robustness**: Surface features prove fragile when edited — just 10% replacement causes F1 to plummet from 0.82 to 0.70.

11. **LD-Score**: Character-level patterns mirror the word-level depletion we saw earlier, so they're not providing complementary information.

12. **End-to-end classifier**: Within-generation performance reaches 0.87, but cross-generation drops sharply to 0.53 — even with 0.8B parameters, the model can't escape generator-specificity.

The framing should emphasize this as an informative negative result that characterizes how recursive generation creates distinctive fingerprints, with H₁ emerging as the stronger hypothesis even across non-paraphrastic chains. Vocabulary impoverishment appears as a universal but shallow marker. Now I'm structuring this as a comprehensive paper targeting AAAI, mapping all 11 experiments into a coherent narrative across methods and results sections, with research questions guiding each analysis.

I need to consolidate these experiments thematically rather than treating each as isolated—grouping them around core questions about signal robustness, generalization, and practical utility to maintain narrative coherence throughout the paper. finishing up the experiment sections, then moving into writing the full LaTeX paper using a standard article class with AAAI-style formatting.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "879dfe50-6373-4e44-bc70-3deba2809feb",
  "isSidechain": false,
  "requestId": "req_011Cb2wpWytcSqFBzVQuCku2",
  "type": "assistant",
  "uuid": "8e9ea89a-1277-4cd2-a649-2f9a62d7da7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lak42fMewDAddA9ehQ37N9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13924,
      "cache_read_input_tokens": 23084,
      "output_tokens": 1552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1552,
          "cache_read_input_tokens": 23084,
          "cache_creation_input_tokens": 13924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13924
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

_source line 15 · 2026-05-14T18:37:32.714Z_

Now I have all the data. Let me write the LaTeX paper — reframed as a negative-but-informative empirical result per the narrative guidance, with H₁ vs H₂ hypothesis testing and all 11 experiments covered.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e9ea89a-1277-4cd2-a649-2f9a62d7da7c",
  "isSidechain": false,
  "requestId": "req_011Cb2wpWytcSqFBzVQuCku2",
  "type": "assistant",
  "uuid": "83bc2195-dc4c-43df-a94a-6c68a4fc9d77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lak42fMewDAddA9ehQ37N9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13924,
      "cache_read_input_tokens": 23084,
      "output_tokens": 1552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1552,
          "cache_read_input_tokens": 23084,
          "cache_creation_input_tokens": 13924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13924
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

_source line 16 · 2026-05-14T18:37:34.939Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TxMzt6X96Ts35aMSzBZqSD`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst && which pdflatex",
  "description": "Ensure output directory exists and check pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83bc2195-dc4c-43df-a94a-6c68a4fc9d77",
  "isSidechain": false,
  "requestId": "req_011Cb2wpWytcSqFBzVQuCku2",
  "type": "assistant",
  "uuid": "4bea05a1-0215-46f0-b787-92d098e7a404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lak42fMewDAddA9ehQ37N9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13924,
      "cache_read_input_tokens": 23084,
      "output_tokens": 1552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1552,
          "cache_read_input_tokens": 23084,
          "cache_creation_input_tokens": 13924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13924
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

_source line 17 · 2026-05-14T18:37:35.063Z_

<details><summary>↩ Tool result · `toolu_01TxMzt6X96Ts35aMSzBZqSD`</summary>

```text
/usr/bin/pdflatex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bea05a1-0215-46f0-b787-92d098e7a404",
  "isSidechain": false,
  "promptId": "00675285-eb7e-4fe5-a2b7-b441582ee0b5",
  "type": "user",
  "uuid": "bed87574-5c68-4087-974c-d44c0b43f1be",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4bea05a1-0215-46f0-b787-92d098e7a404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T18:40:34.090Z_

<details open><summary>🔧 Tool call — Write · `toolu_012ERgHrvF4LrNaaN9RcxAmD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/paper.tex",
  "content": "\\documentclass[letterpaper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{enumitem}\n\n\\title{Vocabulary Impoverishment as a Shallow Fingerprint of Recursive LLM Generation:\\\\An Empirical Characterization of Convergence in Non-Paraphrastic Chains}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nRecursive application of large language models---where model outputs become inputs to subsequent generations---is an increasingly common pathway for web-scale data contamination. We investigate whether the \\emph{generation depth} of such recursively produced text (gen-0 = human, gen-1 = first-pass synthetic, gen-2+ = deeper) can be estimated from distributional features, enabling risk-stratified data curation beyond binary real-vs-synthetic filtering. We formalize two competing hypotheses: \\textbf{H$_1$} (convergence), where recursive generation tends toward a distributional fixed point even for non-paraphrastic chains, and \\textbf{H$_2$} (divergence), where non-paraphrastic chains accumulate monotonic distributional drift. Through systematic experiments across 5 generators, 4 domains, 3 prompt types, and 25K+ generation chains, we find strong evidence for H$_1$: non-paraphrastic chains converge within 2 generation steps, with detectable differences confined primarily to vocabulary impoverishment---a surface-level phenomenon measured by type-token ratio and hapax ratio. Reference-model entropy statistics, hypothesized to capture deeper distributional shifts, carry no independent signal (surface-only F1 = 0.82 vs.\\ full F1 = 0.83, $p = 0.18$). Cross-generator generalization collapses from 0.81 to 0.48 macro-F1, and depth-aware filtering provides no advantage over binary detection baselines. Our results extend attractor cycle theory from paraphrastic to non-paraphrastic settings and establish clear boundary conditions for depth-based approaches to synthetic text governance.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nThe proliferation of LLM-generated text on the web creates a recursive contamination problem: models trained on web data ingest outputs of previous models, and their own outputs re-enter the training pipeline at increasing \\emph{generation depth}. Unlike the binary real-vs-synthetic distinction addressed by existing detectors \\citep{mitchell2023detectgpt,bao2024fastdetectgpt,tulchinskii2024ldscore}, the depth dimension carries additional risk information---deeply recursive text may exhibit compounding distributional artifacts that degrade downstream model quality.\n\nRecent theoretical work on \\emph{attractor cycles} \\citep{anonymous2025attractor} demonstrates that paraphrastic generation chains (where each step paraphrases the previous output) converge to periodic orbits in distributional space within 2--3 steps. This convergence bounds the depth signal available in paraphrastic settings. However, non-paraphrastic chains---continuations, elaborations, and inspired rewrites---operate in an unbounded semantic state space, raising the question: does distributional drift accumulate monotonically in these chains, or does autoregressive sampling impose its own convergence?\n\nWe formalize this as two competing hypotheses:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{H$_1$ (Convergence)}: Recursive non-paraphrastic generation converges to a near-stationary distribution within a small number of steps, driven by autoregressive sampling concentrating probability mass on preferred tokens.\n    \\item \\textbf{H$_2$ (Divergence)}: Non-paraphrastic chains accumulate monotonic distributional drift, producing increasingly distinctive depth fingerprints that enable fine-grained ordinal depth estimation.\n\\end{itemize}\n\nWe test these hypotheses through a comprehensive empirical study spanning 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B), 4 text domains (Wikipedia, news, scientific, creative writing), and 3 non-paraphrastic prompt types (continuation, elaboration, inspired rewriting), generating over 25,000 recursive chains of depth 0--4.\n\nOur findings decisively support H$_1$ and yield a negative-but-informative result: \\textbf{non-paraphrastic chains also converge rapidly in distributional space, with detectable differences confined primarily to vocabulary impoverishment.} Specifically:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item Surface vocabulary features (hapax ratio, type-token ratio) explain 98.8\\% of classifier performance; reference-model entropy statistics add no significant independent signal.\n    \\item Cross-generator depth estimation collapses to near-chance (macro-F1 = 0.48) because vocabulary statistics are generator-specific artifacts, not universal depth markers.\n    \\item Depth-aware data filtering provides no practical advantage over binary real/synthetic baselines for downstream quality preservation.\n\\end{enumerate}\n\nThese results extend attractor cycle theory to non-paraphrastic settings and establish vocabulary impoverishment as a universal but shallow fingerprint of recursive generation---theoretically motivated by entropy convergence under autoregressive sampling, but practically limited by its generator-specificity.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Machine-generated text detection.}\nBinary detection methods assign a real/synthetic label based on statistical signatures. Log-likelihood approaches \\citep{mitchell2023detectgpt,bao2024fastdetectgpt} use perturbation-based curvature estimates under a scoring model. Watermarking methods \\citep{kirchenbauer2023watermark} embed detectable patterns during generation. LD-Score \\citep{tulchinskii2024ldscore} exploits character-level distributional signatures. All these operate at the binary level; none attempt ordinal depth estimation.\n\n\\paragraph{Model collapse and recursive generation.}\nShumailov et al.\\ (\\citeyear{shumailov2024modelcollapse}) demonstrate that iterative training on self-generated data leads to model collapse---progressive loss of distributional tails. Dohmatob et al.\\ (\\citeyear{dohmatob2024tale}) provide theoretical analysis of this phenomenon. Our work examines the \\emph{text-level} distributional changes across generation depth, rather than the model-level degradation from recursive training.\n\n\\paragraph{Attractor cycle theory.}\nRecent work \\citep{anonymous2025attractor} proves that paraphrastic generation chains converge to periodic orbits, bounding depth-discriminable classes to approximately 3 for paraphrasing. We extend this investigation to non-paraphrastic settings, testing whether the convergence phenomenon generalizes beyond the semantic-preservation constraint of paraphrasing.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Chain Construction}\n\\label{sec:chains}\n\nGiven a seed text $x_0$ (human-written, gen-0), we construct recursive generation chains by repeatedly applying a generator $G$:\n\\begin{equation}\n    x_{d+1} = G(x_d; p_\\text{type})\n\\end{equation}\nwhere $p_\\text{type} \\in \\{\\text{continuation, elaboration, inspired\\_rewriting}\\}$ specifies the prompt template. We generate chains of depth 0 through 4, yielding 5-class ordinal labels.\n\n\\paragraph{Generators.} We use 5 autoregressive models spanning 3 families: Pythia-2.8B, Pythia-1B \\citep{biderman2023pythia}, OLMo-2-1B \\citep{groeneveld2024olmo}, Qwen3.5-2B, and Qwen3.5-0.8B \\citep{bai2023qwen}. All generation uses nucleus sampling ($p = 0.95$, $T = 1.0$).\n\n\\paragraph{Seed domains.} We draw 500 seeds per domain from 4 sources: Wikipedia, CNN/DailyMail (news), S2ORC (scientific abstracts), and WritingPrompts (creative writing).\n\n\\paragraph{Cross-model chains.} To simulate realistic web contamination where different generators produce each depth step, we also construct cross-model chains with generators randomly assigned per step.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nWe extract two categories of features from each text $x_d$:\n\n\\paragraph{Surface vocabulary features.}\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Type-token ratio (TTR)}: $|\\mathcal{V}(x)| / |x|$, measuring lexical diversity.\n    \\item \\textbf{Hapax ratio}: fraction of word types appearing exactly once, capturing vocabulary richness at the distributional tail.\n\\end{itemize}\n\n\\paragraph{Reference-model features.}\nGiven a reference model $M_\\text{ref}$ (default: Pythia-410M), we compute the token-level log-probability sequence $\\{-\\log p_{M_\\text{ref}}(t_i \\mid t_{<i})\\}_{i=1}^{|x|}$ and extract:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Entropy statistics}: mean, standard deviation, minimum, and maximum of the token-level surprise distribution.\n    \\item \\textbf{Tail decay}: rate of exponential decay in the sorted surprise values, capturing distributional tail behavior.\n\\end{itemize}\n\nWe additionally evaluate OLMo-2-1B and Qwen3.5-0.8B as alternative reference models, and LD-Score \\citep{tulchinskii2024ldscore} as a character-level feature.\n\n\\subsection{Classification}\n\\label{sec:classifiers}\n\nWe train ordinal logistic regression and random forest classifiers with 5-fold cross-validation, reporting macro-F1 as the primary metric. For cross-generator evaluation, we use leave-one-generator-out (LOO) cross-validation. As an upper bound, we fine-tune Qwen3.5-0.8B with QLoRA for end-to-end depth classification from raw text.\n\n%==============================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n%==============================================================================\n\nWe organize our experiments around the two competing hypotheses and three practical questions: (1) what features carry the depth signal, (2) does the signal generalize, and (3) does it provide downstream utility?\n\n%--- 4.1 Feature Ablation ---\n\\subsection{Feature Ablation: What Carries the Signal?}\n\\label{sec:ablation}\n\nWe compare surface-only, reference-only, and full (surface + reference) feature sets on single-generator data (Pythia-2.8B, Pythia-410M reference, 3-class depth: gen-0/gen-1/gen-2+).\n\n\\begin{table}[h]\n\\centering\n\\caption{Feature ablation results (3-class, Pythia-2.8B generator).}\n\\label{tab:ablation}\n\\begin{tabular}{lcccc}\n\\toprule\nFeature Set & Macro-F1 & Gen-0 F1 & Gen-1 F1 & Gen-2+ F1 \\\\\n\\midrule\nSurface only & 0.82 & 0.94 & 0.75 & 0.77 \\\\\nReference only & 0.47 & 0.58 & 0.38 & 0.44 \\\\\nFull (surface + ref) & 0.83 & 0.95 & 0.76 & 0.78 \\\\\nChance & 0.33 & 0.33 & 0.33 & 0.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Permutation feature importance (full model).}\n\\label{tab:importance}\n\\begin{tabular}{lcc}\n\\toprule\nFeature & Importance & Std \\\\\n\\midrule\nhapax\\_ratio & 0.31 & 0.04 \\\\\nTTR & 0.24 & 0.03 \\\\\nentropy\\_mean & 0.04 & 0.02 \\\\\nentropy\\_std & 0.03 & 0.01 \\\\\nentropy\\_min & 0.02 & 0.01 \\\\\nentropy\\_max & 0.01 & 0.01 \\\\\ntail\\_decay & 0.02 & 0.01 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSurface features alone achieve F1 = 0.82, recovering 98.8\\% of the full model's performance (0.83). Adding reference-model features yields a non-significant improvement of +0.01 ($p = 0.18$, paired bootstrap). Reference-only features perform near chance (0.47). Permutation importance (Table~\\ref{tab:importance}) confirms that hapax ratio (0.31) and TTR (0.24) dominate, while all entropy features combined contribute $< 0.12$. The ``distributional fingerprint'' framing is not supported: what the classifier detects is vocabulary impoverishment, not a deeper distributional shift.\n\n%--- 4.2 Cross-Generator Generalization ---\n\\subsection{Cross-Generator Generalization}\n\\label{sec:crossgen}\n\nWe evaluate generalization across 5 generators using leave-one-generator-out cross-validation on 25K chains (1000 seeds $\\times$ 5 generators $\\times$ 5 depths).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-generator generalization (leave-one-out).}\n\\label{tab:crossgen}\n\\begin{tabular}{lcccc}\n\\toprule\nHeld-Out Generator & Macro-F1 & Gen-0 F1 & Gen-1 F1 & Gen-2+ F1 \\\\\n\\midrule\nPythia-2.8B & 0.52 & 0.71 & 0.40 & 0.45 \\\\\nOLMo-2-1B & 0.44 & 0.65 & 0.34 & 0.38 \\\\\nQwen3.5-2B & 0.43 & 0.64 & 0.35 & 0.39 \\\\\nQwen3.5-0.8B & 0.50 & 0.70 & 0.38 & 0.43 \\\\\nPythia-1B & 0.53 & 0.72 & 0.42 & 0.46 \\\\\n\\midrule\n\\textbf{Average} & \\textbf{0.48} & \\textbf{0.68} & \\textbf{0.38} & \\textbf{0.42} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Within- vs.\\ cross-generator comparison.}\n\\label{tab:within_vs_cross}\n\\begin{tabular}{lcc}\n\\toprule\nSetting & Macro-F1 & $\\Delta$ vs.\\ Within \\\\\n\\midrule\nWithin-generator avg & 0.81 & --- \\\\\nLeave-one-out avg & 0.48 & $-0.33$ \\\\\nPooled all generators & 0.62 & $-0.19$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-generator macro-F1 drops catastrophically from 0.81 to 0.48---barely above chance (0.33). The collapse is most severe for cross-family transfer: holding out Qwen models yields 0.43--0.44, while holding out Pythia-1B yields 0.53 due to shared vocabulary statistics with Pythia-2.8B in the training fold. Gen-0 identification is partially preserved (0.68) because human text maintains a distinct surface profile regardless of generator, but gen-1 vs.\\ gen-2+ discrimination is near chance. The surface vocabulary statistics that carry the depth signal are generator-specific calibration artifacts, not universal depth markers.\n\n%--- 4.3 Reference Model Choice ---\n\\subsection{Reference Model Choice}\n\\label{sec:refmodel}\n\nWe test whether the reference model architecture contributes to the generalization failure by evaluating Pythia-410M, OLMo-2-1B, and Qwen3.5-0.8B as reference models.\n\n\\begin{table}[h]\n\\centering\n\\caption{Reference model comparison (leave-one-generator-out).}\n\\label{tab:refmodel}\n\\begin{tabular}{lccc}\n\\toprule\nReference Model & LOO Macro-F1 & Ref-Only F1 & Surface-Only F1 \\\\\n\\midrule\nPythia-410M & 0.48 & 0.47 & 0.82 \\\\\nOLMo-2-1B & 0.45 & 0.43 & 0.82 \\\\\nQwen3.5-0.8B & 0.44 & 0.41 & 0.82 \\\\\nEnsemble (3 refs) & 0.50 & 0.49 & 0.82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll three reference models produce similarly uninformative entropy distributions for cross-generator depth estimation. The surface-only F1 remains constant at 0.82 regardless of reference model, confirming that surface features are the sole discriminative mechanism. Ensembling three reference models yields only +0.02 over the best single model. The generalization bottleneck is not reference model choice---it is the fundamental convergence of generation entropy to near-stationary levels by gen-1, leaving no depth-discriminative signal for the reference model to capture.\n\n%--- 4.4 H1 vs H2: Convergence Testing ---\n\\subsection{Hypothesis Testing: Convergence vs.\\ Divergence}\n\\label{sec:convergence}\n\nWe directly test H$_1$ vs.\\ H$_2$ by comparing paraphrastic and non-paraphrastic chains on matched seeds (Pythia-2.8B, 1000 seeds, 5 depths).\n\n\\begin{table}[h]\n\\centering\n\\caption{Paraphrastic vs.\\ non-paraphrastic chain comparison.}\n\\label{tab:convergence}\n\\begin{tabular}{lcccc}\n\\toprule\nChain Type & Macro-F1 (3-class) & Gen-1 vs.\\ Gen-2+ F1 & Conv.\\ Depth & KL$_{d2 \\to d3}$ \\\\\n\\midrule\nParaphrasing & 0.64 & 0.41 & 1 & 0.008 \\\\\nContinuation & 0.82 & 0.58 & 2 & 0.031 \\\\\nElaboration & 0.78 & 0.52 & 2 & 0.024 \\\\\nInspired rewriting & 0.69 & 0.44 & 1 & 0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{H$_1$ is confirmed.} All chain types converge within 1--2 generation steps. Paraphrasing chains converge fastest (by depth 1), consistent with attractor cycle theory, while continuation chains converge by depth 2. The KL divergence between depth-2 and depth-3 distributions is negligible across all chain types ($< 0.04$ nats). Non-paraphrastic generation does \\emph{not} produce the unbounded divergence hypothesized in H$_2$; instead, autoregressive sampling from a fixed model concentrates probability mass on preferred tokens regardless of prompt type, creating a universal vocabulary attractor. The depth signal is fundamentally bounded at $\\sim$2--3 discriminable classes.\n\n%--- 4.5 Prompt Type Sensitivity ---\n\\subsection{Prompt Type Sensitivity}\n\\label{sec:prompt}\n\nWe compare three non-paraphrastic prompt types within and across settings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Prompt type comparison (Pythia-2.8B, 1000 seeds).}\n\\label{tab:prompt}\n\\begin{tabular}{lccc}\n\\toprule\nPrompt Type & Within-Gen F1 & Cross-Prompt F1 & Conv.\\ Depth \\\\\n\\midrule\nContinuation & 0.82 & 0.61 & 2 \\\\\nElaboration & 0.78 & 0.58 & 2 \\\\\nInspired rewriting & 0.69 & 0.52 & 1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nContinuation chains yield the highest within-generator F1 (0.82) because they preserve topic continuity, making vocabulary depletion the dominant and cleanest signal. Inspired rewriting shows the weakest signal (0.69) because each generation step introduces substantially new vocabulary, partially resetting the depletion. Cross-prompt transfer is poor (0.52--0.61), revealing that each prompt type induces a different vocabulary depletion rate. This adds a second axis of non-generalization beyond generator specificity: the depth signal is both generator-specific and prompt-type-specific.\n\n%--- 4.6 Ecological Validity ---\n\\subsection{Ecological Validity: Cross-Model Chains and Multi-Domain Seeds}\n\\label{sec:ecological}\n\n\\paragraph{Cross-model chains.}\nWe construct chains where a different generator (randomly selected from 5) produces each depth step, simulating realistic web contamination.\n\n\\begin{table}[h]\n\\centering\n\\caption{Single-model vs.\\ cross-model chains.}\n\\label{tab:crossmodel}\n\\begin{tabular}{lcccc}\n\\toprule\nSetting & Macro-F1 & Gen-0 F1 & Gen-1 F1 & Gen-2+ F1 \\\\\n\\midrule\nSingle-model chains & 0.81 & 0.94 & 0.75 & 0.77 \\\\\nCross-model chains & 0.42 & 0.65 & 0.32 & 0.35 \\\\\nChance & 0.33 & 0.33 & 0.33 & 0.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-model chains produce near-chance depth estimation (0.42). When different generators produce each depth step, the vocabulary statistics at any given depth reflect the current generator's preferences more than cumulative chain depth. Gen-0 identification survives partially (0.65) because human text remains distinct, but gen-1/gen-2+ classification is effectively random.\n\n\\paragraph{Multi-domain seeds.}\nWe expand to 4 domains with 500 seeds each using Pythia-2.8B.\n\n\\begin{table}[h]\n\\centering\n\\caption{Multi-domain results.}\n\\label{tab:domain}\n\\begin{tabular}{lcccc}\n\\toprule\nDomain & Within-Domain F1 & Gen-0 hapax$_\\text{med}$ & Gen-2+ hapax$_\\text{med}$ & $\\Delta$hapax \\\\\n\\midrule\nWikipedia & 0.83 & 0.47 & 0.26 & 0.21 \\\\\nNews & 0.80 & 0.44 & 0.27 & 0.17 \\\\\nScientific & 0.76 & 0.52 & 0.35 & 0.17 \\\\\nCreative & 0.72 & 0.38 & 0.28 & 0.10 \\\\\nCross-domain avg & 0.59 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWithin-domain performance correlates with the hapax ratio gap ($\\Delta$hapax) between gen-0 and gen-2+: Wikipedia/news have the largest gaps (0.21/0.17) and highest F1 (0.83/0.80), while creative writing has the smallest gap (0.10) and lowest F1 (0.72). Cross-domain transfer drops to 0.59 because baseline vocabulary statistics differ across domains---scientific gen-0 text (hapax median 0.52) overlaps with other domains' synthetic ranges, confounding domain and depth.\n\n%--- 4.7 Depth Resolution Ceiling ---\n\\subsection{Depth Resolution Ceiling}\n\\label{sec:ordinal}\n\nWe test 5-class ordinal classification (gen-0 through gen-4) on continuation chains.\n\n\\begin{table}[h]\n\\centering\n\\caption{5-class ordinal classification results.}\n\\label{tab:ordinal}\n\\begin{tabular}{lccc}\n\\toprule\nClass & Precision & Recall & F1 \\\\\n\\midrule\ngen-0 & 0.93 & 0.90 & 0.91 \\\\\ngen-1 & 0.54 & 0.62 & 0.58 \\\\\ngen-2 & 0.36 & 0.40 & 0.38 \\\\\ngen-3 & 0.29 & 0.33 & 0.31 \\\\\ngen-4 & 0.31 & 0.35 & 0.33 \\\\\n\\midrule\n\\multicolumn{3}{l}{5-class macro-F1} & 0.52 \\\\\n\\multicolumn{3}{l}{3-class macro-F1 (same data)} & 0.82 \\\\\n\\multicolumn{3}{l}{Adjacent confusion rate} & 0.44 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{5-class confusion matrix (row = true, column = predicted; values are proportions).}\n\\label{tab:confusion}\n\\begin{tabular}{lccccc}\n\\toprule\n & gen-0 & gen-1 & gen-2 & gen-3 & gen-4 \\\\\n\\midrule\ngen-0 & \\textbf{0.90} & 0.07 & 0.02 & 0.01 & 0.00 \\\\\ngen-1 & 0.09 & \\textbf{0.62} & 0.18 & 0.07 & 0.04 \\\\\ngen-2 & 0.03 & 0.21 & \\textbf{0.40} & 0.22 & 0.14 \\\\\ngen-3 & 0.02 & 0.10 & 0.24 & \\textbf{0.33} & 0.31 \\\\\ngen-4 & 0.01 & 0.07 & 0.16 & 0.28 & \\textbf{0.48} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n5-class macro-F1 drops to 0.52 (from 0.82 for 3-class). Gen-2 through gen-4 collapse into mutual confusion: gen-3 and gen-4 F1 scores (0.31, 0.33) are at chance level. The confusion matrix shows a diagonal-plus-adjacent pattern (44\\% of errors are off-by-one) consistent with a smoothly converging feature distribution rather than discrete depth categories. This directly reflects H$_1$ convergence: by depth 2, the feature distributions have stabilized, making deeper classes statistically indistinguishable. The practical depth resolution ceiling is $\\sim$2--3 classes.\n\n%--- 4.8 Robustness Analysis ---\n\\subsection{Robustness to Human Edits and Character-Level Features}\n\\label{sec:robustness}\n\n\\paragraph{Edit robustness.}\nWe test robustness to simulated human edits via random word replacement (5\\%, 10\\%, 20\\%) and LLM-simulated light rephrasing.\n\n\\begin{table}[h]\n\\centering\n\\caption{Robustness to human edits.}\n\\label{tab:edits}\n\\begin{tabular}{lccc}\n\\toprule\nEdit Type & Edit Rate & Macro-F1 & $\\Delta$ vs.\\ Baseline \\\\\n\\midrule\nNone & 0\\% & 0.82 & --- \\\\\nRandom replace & 5\\% & 0.77 & $-0.05$ \\\\\nRandom replace & 10\\% & 0.70 & $-0.12$ \\\\\nRandom replace & 20\\% & 0.58 & $-0.24$ \\\\\nLLM-simulated & light & 0.63 & $-0.19$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSurface features are fragile under editing. At 10\\% word replacement, F1 drops by 0.12; LLM-simulated light editing causes a 0.19 drop because the editing model introduces its own vocabulary preferences, adding a second generator's fingerprint. The crossover where depth estimation becomes worse than binary detection occurs at approximately 12\\% replacement rate. Real-world synthetic text is routinely edited at or above this level.\n\n\\paragraph{LD-Score features.}\nWe evaluate LD-Score \\citep{tulchinskii2024ldscore} as a character-level complement.\n\n\\begin{table}[h]\n\\centering\n\\caption{LD-Score feature analysis.}\n\\label{tab:ldscore}\n\\begin{tabular}{lcc}\n\\toprule\nFeature Set & Macro-F1 & LOO Cross-Gen F1 \\\\\n\\midrule\nSurface only & 0.82 & 0.48 \\\\\nLD-Score only & 0.61 & 0.46 \\\\\nSurface + LD & 0.83 & 0.49 \\\\\nFull + LD & 0.83 & 0.50 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLD-Score achieves moderate standalone performance (0.61) but provides no complementary signal when combined with surface features (+0.01). Character-level distributions partially capture vocabulary depletion through character frequency shifts but are redundant with word-level statistics. Cross-generator transfer with LD-Score (0.46) remains poor.\n\n%--- 4.9 Learned Representations ---\n\\subsection{End-to-End Learned Representations}\n\\label{sec:e2e}\n\nWe fine-tune Qwen3.5-0.8B with QLoRA for end-to-end depth classification to test whether learned representations can discover depth signal beyond handcrafted features.\n\n\\begin{table}[h]\n\\centering\n\\caption{End-to-end vs.\\ handcrafted features.}\n\\label{tab:e2e}\n\\begin{tabular}{lccc}\n\\toprule\nModel & Within-Gen F1 & Cross-Gen LOO F1 & $\\Delta$ Cross-Gen \\\\\n\\midrule\nHandcrafted (surface + ref) & 0.83 & 0.48 & --- \\\\\nQLoRA Qwen3.5-0.8B & 0.87 & 0.53 & +0.05 \\\\\nHandcrafted surface only & 0.82 & 0.48 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe end-to-end model achieves marginally higher within-generator F1 (0.87 vs.\\ 0.82) by learning soft vocabulary depletion features beyond hapax ratio and TTR. However, cross-generator transfer shows only +0.05 improvement (0.53 vs.\\ 0.48), meaning learned representations are also predominantly generator-specific. Attention analysis reveals the model focuses on high-frequency function words and punctuation---tokens whose usage patterns shift under vocabulary impoverishment. Even with 0.8B parameters and full sequence access, the model does not discover hidden distributional structure beyond surface statistics. This closes the ``bigger model'' escape hatch: the cross-generator signal genuinely is not present.\n\n%--- 4.10 Downstream Utility ---\n\\subsection{Downstream Utility}\n\\label{sec:downstream}\n\nWe test whether depth-aware filtering improves downstream model quality by fine-tuning Pythia-410M on depth-stratified data subsets and comparing against binary detection baselines.\n\n\\begin{table}[h]\n\\centering\n\\caption{Downstream fine-tuning perplexity.}\n\\label{tab:downstream}\n\\begin{tabular}{lcc}\n\\toprule\nTraining Data & Perplexity & Data Size (\\%) \\\\\n\\midrule\nGen-0 only & 18.2 & 33 \\\\\nGen-0 + gen-1 & 18.8 & 67 \\\\\nAll depths unfiltered & 19.5 & 100 \\\\\nDepth-aware filter ($\\leq$gen-1) & 18.5 & 38 \\\\\nFastDetectGPT binary filter & 18.4 & 42 \\\\\nLD-Score binary filter & 18.6 & 40 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth--quality correlation.}\n\\label{tab:correlation}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nSpearman $\\rho$ (depth vs.\\ ppl degradation) & 0.19 \\\\\n$p$-value & 0.04 \\\\\nDepth filter vs.\\ best binary gap & $-0.3\\%$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA weak positive correlation exists between generation depth and quality degradation ($\\rho = 0.19$, $p = 0.04$), but the effect size is negligible. Depth-aware filtering achieves perplexity 18.5, compared to 18.4 for FastDetectGPT binary filtering---a $-0.3\\%$ gap favoring the simpler baseline. The ordinal depth information provides no practical advantage over binary classification for data curation. This is the expected consequence of the preceding results: if depth estimation relies on generator-specific surface features with poor cross-generator transfer, the noisy depth predictions cannot outperform binary detection for downstream filtering.\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Extending attractor cycle theory.}\nOur central finding---that H$_1$ holds for non-paraphrastic chains---extends the attractor cycle theory of \\citet{anonymous2025attractor} beyond its original paraphrastic setting. The convergence mechanism is distinct: paraphrastic chains converge because the semantic-preservation constraint restricts the output space, while non-paraphrastic chains converge because autoregressive sampling from a fixed model concentrates probability mass on preferred tokens regardless of semantic constraints. Both mechanisms produce the same practical outcome: depth-discriminable classes are bounded at $\\sim$2--3.\n\n\\paragraph{Vocabulary impoverishment as a universal but shallow fingerprint.}\nRecursive generation progressively depletes rare vocabulary---a mechanical consequence of sampling from a fixed token distribution. This creates a detectable but shallow fingerprint: type-token ratio and hapax ratio decrease monotonically with depth but stabilize by gen-2, and their absolute values are determined by the generator's vocabulary preferences rather than chain depth per se. The fingerprint is ``universal'' in that all tested generators exhibit vocabulary depletion, but ``shallow'' in that it does not encode generator-invariant depth information.\n\n\\paragraph{Implications for data governance.}\nOur results suggest that binary real-vs-synthetic detection remains the practically optimal granularity for data filtering in the current paradigm. Depth-aware approaches face a three-way non-generalization barrier: the signal is generator-specific, prompt-type-specific, and domain-specific. Until depth features are identified that generalize across these axes, binary filtering with established detectors \\citep{bao2024fastdetectgpt,tulchinskii2024ldscore} is both simpler and more effective.\n\n\\paragraph{Limitations.}\nOur study is limited to 5 open-weight models up to 2.8B parameters; larger or closed-source models may exhibit different vocabulary dynamics. The simulated editing is a lower bound on real-world post-processing. We do not test instruction-tuned or RLHF-aligned models, which may have different distributional properties. Our cross-model chains use random generator assignment; real contamination may have structured patterns.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe tested two hypotheses about distributional dynamics in recursive non-paraphrastic LLM generation chains. Our experiments across 5 generators, 4 domains, and 3 prompt types provide strong evidence for H$_1$ (convergence): non-paraphrastic chains converge to near-stationary distributions within 2 generation steps, extending attractor cycle theory beyond paraphrastic settings. The detectable depth signal is confined to vocabulary impoverishment---surface features (hapax ratio, TTR) that explain 98.8\\% of classifier performance but are generator-specific, prompt-type-specific, and fragile under editing. Cross-generator depth estimation is near chance (macro-F1 = 0.48), and depth-aware filtering provides no advantage over binary baselines.\n\nThese negative results establish clear boundary conditions: vocabulary impoverishment is a universal consequence of autoregressive generation but not a viable basis for general-purpose depth estimation. Future work should investigate whether training-time features (model weights, sampling parameters) or generation-aware watermarking can provide the generator-invariant depth signal that distributional post-hoc analysis cannot.\n\n%==============================================================================\n% References\n%==============================================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Anonymous(2025)]{anonymous2025attractor}\nAnonymous.\n\\newblock Attractor cycles in paraphrastic generation chains.\n\\newblock In \\emph{Proceedings of ACL}, 2025.\n\n\\bibitem[Bai et~al.(2023)]{bai2023qwen}\nJinze Bai et~al.\n\\newblock Qwen technical report.\n\\newblock \\emph{arXiv preprint arXiv:2309.16609}, 2023.\n\n\\bibitem[Bao et~al.(2024)]{bao2024fastdetectgpt}\nGuangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi Yang, and Yue Zhang.\n\\newblock Fast-{D}etect{GPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In \\emph{Proceedings of ICLR}, 2024.\n\n\\bibitem[Biderman et~al.(2023)]{biderman2023pythia}\nStella Biderman et~al.\n\\newblock Pythia: A suite for analyzing large language models across training and scaling.\n\\newblock In \\emph{Proceedings of ICML}, 2023.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024tale}\nElvis Dohmatob, Yunzhen Feng, and Julia Kempe.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In \\emph{Proceedings of ICML}, 2024.\n\n\\bibitem[Groeneveld et~al.(2024)]{groeneveld2024olmo}\nDirk Groeneveld et~al.\n\\newblock {OLMo}: Accelerating the science of language models.\n\\newblock In \\emph{Proceedings of ACL}, 2024.\n\n\\bibitem[Kirchenbauer et~al.(2023)]{kirchenbauer2023watermark}\nJohn Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein.\n\\newblock A watermark for large language models.\n\\newblock In \\emph{Proceedings of ICML}, 2023.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nEric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher~D. Manning, and Chelsea Finn.\n\\newblock {DetectGPT}: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{Proceedings of ICML}, 2023.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024modelcollapse}\nIlia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, and Ross Anderson.\n\\newblock The curse of recursion: Training on generated data makes models forget.\n\\newblock \\emph{Nature}, 2024.\n\n\\bibitem[Tulchinskii et~al.(2024)]{tulchinskii2024ldscore}\nEduard Tulchinskii et~al.\n\\newblock Intrinsic dimension estimation for robust detection of {AI}-generated texts.\n\\newblock In \\emph{Proceedings of NeurIPS}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bed87574-5c68-4087-974c-d44c0b43f1be",
  "isSidechain": false,
  "requestId": "req_011Cb2wrrctoRfbme6cPVUDu",
  "type": "assistant",
  "uuid": "405d7d11-5c36-41db-9d3f-689f61b6b1cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvpMv51tZWskpWRw9kCb6V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1569,
      "cache_read_input_tokens": 37008,
      "output_tokens": 10526,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10526,
          "cache_read_input_tokens": 37008,
          "cache_creation_input_tokens": 1569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1569
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

_source line 19 · 2026-05-14T18:40:34.112Z_

<details><summary>↩ Tool result · `toolu_012ERgHrvF4LrNaaN9RcxAmD`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "405d7d11-5c36-41db-9d3f-689f61b6b1cc",
  "isSidechain": false,
  "promptId": "00675285-eb7e-4fe5-a2b7-b441582ee0b5",
  "type": "user",
  "uuid": "aed6aad0-30e5-40c9-ac41-f133eac832f9",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/paper.tex",
    "content": "\\documentclass[letterpaper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{enumitem}\n\n\\title{Vocabulary Impoverishment as a Shallow Fingerprint of Recursive LLM Generation:\\\\An Empirical Characterization of Convergence in Non-Paraphrastic Chains}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nRecursive application of large language models---where model outputs become inputs to subsequent generations---is an increasingly common pathway for web-scale data contamination. We investigate whether the \\emph{generation depth} of such recursively produced text (gen-0 = human, gen-1 = first-pass synthetic, gen-2+ = deeper) can be estimated from distributional features, enabling risk-stratified data curation beyond binary real-vs-synthetic filtering. We formalize two competing hypotheses: \\textbf{H$_1$} (convergence), where recursive generation tends toward a distributional fixed point even for non-paraphrastic chains, and \\textbf{H$_2$} (divergence), where non-paraphrastic chains accumulate monotonic distributional drift. Through systematic experiments across 5 generators, 4 domains, 3 prompt types, and 25K+ generation chains, we find strong evidence for H$_1$: non-paraphrastic chains converge within 2 generation steps, with detectable differences confined primarily to vocabulary impoverishment---a surface-level phenomenon measured by type-token ratio and hapax ratio. Reference-model entropy statistics, hypothesized to capture deeper distributional shifts, carry no independent signal (surface-only F1 = 0.82 vs.\\ full F1 = 0.83, $p = 0.18$). Cross-generator generalization collapses from 0.81 to 0.48 macro-F1, and depth-aware filtering provides no advantage over binary detection baselines. Our results extend attractor cycle theory from paraphrastic to non-paraphrastic settings and establish clear boundary conditions for depth-based approaches to synthetic text governance.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nThe proliferation of LLM-generated text on the web creates a recursive contamination problem: models trained on web data ingest outputs of previous models, and their own outputs re-enter the training pipeline at increasing \\emph{generation depth}. Unlike the binary real-vs-synthetic distinction addressed by existing detectors \\citep{mitchell2023detectgpt,bao2024fastdetectgpt,tulchinskii2024ldscore}, the depth dimension carries additional risk information---deeply recursive text may exhibit compounding distributional artifacts that degrade downstream model quality.\n\nRecent theoretical work on \\emph{attractor cycles} \\citep{anonymous2025attractor} demonstrates that paraphrastic generation chains (where each step paraphrases the previous output) converge to periodic orbits in distributional space within 2--3 steps. This convergence bounds the depth signal available in paraphrastic settings. However, non-paraphrastic chains---continuations, elaborations, and inspired rewrites---operate in an unbounded semantic state space, raising the question: does distributional drift accumulate monotonically in these chains, or does autoregressive sampling impose its own convergence?\n\nWe formalize this as two competing hypotheses:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{H$_1$ (Convergence)}: Recursive non-paraphrastic generation converges to a near-stationary distribution within a small number of steps, driven by autoregressive sampling concentrating probability mass on preferred tokens.\n    \\item \\textbf{H$_2$ (Divergence)}: Non-paraphrastic chains accumulate monotonic distributional drift, producing increasingly distinctive depth fingerprints that enable fine-grained ordinal depth estimation.\n\\end{itemize}\n\nWe test these hypotheses through a comprehensive empirical study spanning 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B), 4 text domains (Wikipedia, news, scientific, creative writing), and 3 non-paraphrastic prompt types (continuation, elaboration, inspired rewriting), generating over 25,000 recursive chains of depth 0--4.\n\nOur findings decisively support H$_1$ and yield a negative-but-informative result: \\textbf{non-paraphrastic chains also converge rapidly in distributional space, with detectable differences confined primarily to vocabulary impoverishment.} Specifically:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item Surface vocabulary features (hapax ratio, type-token ratio) explain 98.8\\% of classifier performance; reference-model entropy statistics add no significant independent signal.\n    \\item Cross-generator depth estimation collapses to near-chance (macro-F1 = 0.48) because vocabulary statistics are generator-specific artifacts, not universal depth markers.\n    \\item Depth-aware data filtering provides no practical advantage over binary real/synthetic baselines for downstream quality preservation.\n\\end{enumerate}\n\nThese results extend attractor cycle theory to non-paraphrastic settings and establish vocabulary impoverishment as a universal but shallow fingerprint of recursive generation---theoretically motivated by entropy convergence under autoregressive sampling, but practically limited by its generator-specificity.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Machine-generated text detection.}\nBinary detection methods assign a real/synthetic label based on statistical signatures. Log-likelihood approaches \\citep{mitchell2023detectgpt,bao2024fastdetectgpt} use perturbation-based curvature estimates under a scoring model. Watermarking methods \\citep{kirchenbauer2023watermark} embed detectable patterns during generation. LD-Score \\citep{tulchinskii2024ldscore} exploits character-level distributional signatures. All these operate at the binary level; none attempt ordinal depth estimation.\n\n\\paragraph{Model collapse and recursive generation.}\nShumailov et al.\\ (\\citeyear{shumailov2024modelcollapse}) demonstrate that iterative training on self-generated data leads to model collapse---progressive loss of distributional tails. Dohmatob et al.\\ (\\citeyear{dohmatob2024tale}) provide theoretical analysis of this phenomenon. Our work examines the \\emph{text-level} distributional changes across generation depth, rather than the model-level degradation from recursive training.\n\n\\paragraph{Attractor cycle theory.}\nRecent work \\citep{anonymous2025attractor} proves that paraphrastic generation chains converge to periodic orbits, bounding depth-discriminable classes to approximately 3 for paraphrasing. We extend this investigation to non-paraphrastic settings, testing whether the convergence phenomenon generalizes beyond the semantic-preservation constraint of paraphrasing.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Chain Construction}\n\\label{sec:chains}\n\nGiven a seed text $x_0$ (human-written, gen-0), we construct recursive generation chains by repeatedly applying a generator $G$:\n\\begin{equation}\n    x_{d+1} = G(x_d; p_\\text{type})\n\\end{equation}\nwhere $p_\\text{type} \\in \\{\\text{continuation, elaboration, inspired\\_rewriting}\\}$ specifies the prompt template. We generate chains of depth 0 through 4, yielding 5-class ordinal labels.\n\n\\paragraph{Generators.} We use 5 autoregressive models spanning 3 families: Pythia-2.8B, Pythia-1B \\citep{biderman2023pythia}, OLMo-2-1B \\citep{groeneveld2024olmo}, Qwen3.5-2B, and Qwen3.5-0.8B \\citep{bai2023qwen}. All generation uses nucleus sampling ($p = 0.95$, $T = 1.0$).\n\n\\paragraph{Seed domains.} We draw 500 seeds per domain from 4 sources: Wikipedia, CNN/DailyMail (news), S2ORC (scientific abstracts), and WritingPrompts (creative writing).\n\n\\paragraph{Cross-model chains.} To simulate realistic web contamination where different generators produce each depth step, we also construct cross-model chains with generators randomly assigned per step.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nWe extract two categories of features from each text $x_d$:\n\n\\paragraph{Surface vocabulary features.}\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Type-token ratio (TTR)}: $|\\mathcal{V}(x)| / |x|$, measuring lexical diversity.\n    \\item \\textbf{Hapax ratio}: fraction of word types appearing exactly once, capturing vocabulary richness at the distributional tail.\n\\end{itemize}\n\n\\paragraph{Reference-model features.}\nGiven a reference model $M_\\text{ref}$ (default: Pythia-410M), we compute the token-level log-probability sequence $\\{-\\log p_{M_\\text{ref}}(t_i \\mid t_{<i})\\}_{i=1}^{|x|}$ and extract:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Entropy statistics}: mean, standard deviation, minimum, and maximum of the token-level surprise distribution.\n    \\item \\textbf{Tail decay}: rate of exponential decay in the sorted surprise values, capturing distributional tail behavior.\n\\end{itemize}\n\nWe additionally evaluate OLMo-2-1B and Qwen3.5-0.8B as alternative reference models, and LD-Score \\citep{tulchinskii2024ldscore} as a character-level feature.\n\n\\subsection{Classification}\n\\label{sec:classifiers}\n\nWe train ordinal logistic regression and random forest classifiers with 5-fold cross-validation, reporting macro-F1 as the primary metric. For cross-generator evaluation, we use leave-one-generator-out (LOO) cross-validation. As an upper bound, we fine-tune Qwen3.5-0.8B with QLoRA for end-to-end depth classification from raw text.\n\n%==============================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n%==============================================================================\n\nWe organize our experiments around the two competing hypotheses and three practical questions: (1) what features carry the depth signal, (2) does the signal generalize, and (3) does it provide downstream utility?\n\n%--- 4.1 Feature Ablation ---\n\\subsection{Feature Ablation: What Carries the Signal?}\n\\label{sec:ablation}\n\nWe compare surface-only, reference-only, and full (surface + reference) feature sets on single-generator data (Pythia-2.8B, Pythia-410M reference, 3-class depth: gen-0/gen-1/gen-2+).\n\n\\begin{table}[h]\n\\centering\n\\caption{Feature ablation results (3-class, Pythia-2.8B generator).}\n\\label{tab:ablation}\n\\begin{tabular}{lcccc}\n\\toprule\nFeature Set & Macro-F1 & Gen-0 F1 & Gen-1 F1 & Gen-2+ F1 \\\\\n\\midrule\nSurface only & 0.82 & 0.94 & 0.75 & 0.77 \\\\\nReference only & 0.47 & 0.58 & 0.38 & 0.44 \\\\\nFull (surface + ref) & 0.83 & 0.95 & 0.76 & 0.78 \\\\\nChance & 0.33 & 0.33 & 0.33 & 0.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Permutation feature importance (full model).}\n\\label{tab:importance}\n\\begin{tabular}{lcc}\n\\toprule\nFeature & Importance & Std \\\\\n\\midrule\nhapax\\_ratio & 0.31 & 0.04 \\\\\nTTR & 0.24 & 0.03 \\\\\nentropy\\_mean & 0.04 & 0.02 \\\\\nentropy\\_std & 0.03 & 0.01 \\\\\nentropy\\_min & 0.02 & 0.01 \\\\\nentropy\\_max & 0.01 & 0.01 \\\\\ntail\\_decay & 0.02 & 0.01 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSurface features alone achieve F1 = 0.82, recovering 98.8\\% of the full model's performance (0.83). Adding reference-model features yields a non-significant improvement of +0.01 ($p = 0.18$, paired bootstrap). Reference-only features perform near chance (0.47). Permutation importance (Table~\\ref{tab:importance}) confirms that hapax ratio (0.31) and TTR (0.24) dominate, while all entropy features combined contribute $< 0.12$. The ``distributional fingerprint'' framing is not supported: what the classifier detects is vocabulary impoverishment, not a deeper distributional shift.\n\n%--- 4.2 Cross-Generator Generalization ---\n\\subsection{Cross-Generator Generalization}\n\\label{sec:crossgen}\n\nWe evaluate generalization across 5 generators using leave-one-generator-out cross-validation on 25K chains (1000 seeds $\\times$ 5 generators $\\times$ 5 depths).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-generator generalization (leave-one-out).}\n\\label{tab:crossgen}\n\\begin{tabular}{lcccc}\n\\toprule\nHeld-Out Generator & Macro-F1 & Gen-0 F1 & Gen-1 F1 & Gen-2+ F1 \\\\\n\\midrule\nPythia-2.8B & 0.52 & 0.71 & 0.40 & 0.45 \\\\\nOLMo-2-1B & 0.44 & 0.65 & 0.34 & 0.38 \\\\\nQwen3.5-2B & 0.43 & 0.64 & 0.35 & 0.39 \\\\\nQwen3.5-0.8B & 0.50 & 0.70 & 0.38 & 0.43 \\\\\nPythia-1B & 0.53 & 0.72 & 0.42 & 0.46 \\\\\n\\midrule\n\\textbf{Average} & \\textbf{0.48} & \\textbf{0.68} & \\textbf{0.38} & \\textbf{0.42} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Within- vs.\\ cross-generator comparison.}\n\\label{tab:within_vs_cross}\n\\begin{tabular}{lcc}\n\\toprule\nSetting & Macro-F1 & $\\Delta$ vs.\\ Within \\\\\n\\midrule\nWithin-generator avg & 0.81 & --- \\\\\nLeave-one-out avg & 0.48 & $-0.33$ \\\\\nPooled all generators & 0.62 & $-0.19$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-generator macro-F1 drops catastrophically from 0.81 to 0.48---barely above chance (0.33). The collapse is most severe for cross-family transfer: holding out Qwen models yields 0.43--0.44, while holding out Pythia-1B yields 0.53 due to shared vocabulary statistics with Pythia-2.8B in the training fold. Gen-0 identification is partially preserved (0.68) because human text maintains a distinct surface profile regardless of generator, but gen-1 vs.\\ gen-2+ discrimination is near chance. The surface vocabulary statistics that carry the depth signal are generator-specific calibration artifacts, not universal depth markers.\n\n%--- 4.3 Reference Model Choice ---\n\\subsection{Reference Model Choice}\n\\label{sec:refmodel}\n\nWe test whether the reference model architecture contributes to the generalization failure by evaluating Pythia-410M, OLMo-2-1B, and Qwen3.5-0.8B as reference models.\n\n\\begin{table}[h]\n\\centering\n\\caption{Reference model comparison (leave-one-generator-out).}\n\\label{tab:refmodel}\n\\begin{tabular}{lccc}\n\\toprule\nReference Model & LOO Macro-F1 & Ref-Only F1 & Surface-Only F1 \\\\\n\\midrule\nPythia-410M & 0.48 & 0.47 & 0.82 \\\\\nOLMo-2-1B & 0.45 & 0.43 & 0.82 \\\\\nQwen3.5-0.8B & 0.44 & 0.41 & 0.82 \\\\\nEnsemble (3 refs) & 0.50 & 0.49 & 0.82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll three reference models produce similarly uninformative entropy distributions for cross-generator depth estimation. The surface-only F1 remains constant at 0.82 regardless of reference model, confirming that surface features are the sole discriminative mechanism. Ensembling three reference models yields only +0.02 over the best single model. The generalization bottleneck is not reference model choice---it is the fundamental convergence of generation entropy to near-stationary levels by gen-1, leaving no depth-discriminative signal for the reference model to capture.\n\n%--- 4.4 H1 vs H2: Convergence Testing ---\n\\subsection{Hypothesis Testing: Convergence vs.\\ Divergence}\n\\label{sec:convergence}\n\nWe directly test H$_1$ vs.\\ H$_2$ by comparing paraphrastic and non-paraphrastic chains on matched seeds (Pythia-2.8B, 1000 seeds, 5 depths).\n\n\\begin{table}[h]\n\\centering\n\\caption{Paraphrastic vs.\\ non-paraphrastic chain comparison.}\n\\label{tab:convergence}\n\\begin{tabular}{lcccc}\n\\toprule\nChain Type & Macro-F1 (3-class) & Gen-1 vs.\\ Gen-2+ F1 & Conv.\\ Depth & KL$_{d2 \\to d3}$ \\\\\n\\midrule\nParaphrasing & 0.64 & 0.41 & 1 & 0.008 \\\\\nContinuation & 0.82 & 0.58 & 2 & 0.031 \\\\\nElaboration & 0.78 & 0.52 & 2 & 0.024 \\\\\nInspired rewriting & 0.69 & 0.44 & 1 & 0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{H$_1$ is confirmed.} All chain types converge within 1--2 generation steps. Paraphrasing chains converge fastest (by depth 1), consistent with attractor cycle theory, while continuation chains converge by depth 2. The KL divergence between depth-2 and depth-3 distributions is negligible across all chain types ($< 0.04$ nats). Non-paraphrastic generation does \\emph{not} produce the unbounded divergence hypothesized in H$_2$; instead, autoregressive sampling from a fixed model concentrates probability mass on preferred tokens regardless of prompt type, creating a universal vocabulary attractor. The depth signal is fundamentally bounded at $\\sim$2--3 discriminable classes.\n\n%--- 4.5 Prompt Type Sensitivity ---\n\\subsection{Prompt Type Sensitivity}\n\\label{sec:prompt}\n\nWe compare three non-paraphrastic prompt types within and across settings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Prompt type comparison (Pythia-2.8B, 1000 seeds).}\n\\label{tab:prompt}\n\\begin{tabular}{lccc}\n\\toprule\nPrompt Type & Within-Gen F1 & Cross-Prompt F1 & Conv.\\ Depth \\\\\n\\midrule\nContinuation & 0.82 & 0.61 & 2 \\\\\nElaboration & 0.78 & 0.58 & 2 \\\\\nInspired rewriting & 0.69 & 0.52 & 1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nContinuation chains yield the highest within-generator F1 (0.82) because they preserve topic continuity, making vocabulary depletion the dominant and cleanest signal. Inspired rewriting shows the weakest signal (0.69) because each generation step introduces substantially new vocabulary, partially resetting the depletion. Cross-prompt transfer is poor (0.52--0.61), revealing that each prompt type induces a different vocabulary depletion rate. This adds a second axis of non-generalization beyond generator specificity: the depth signal is both generator-specific and prompt-type-specific.\n\n%--- 4.6 Ecological Validity ---\n\\subsection{Ecological Validity: Cross-Model Chains and Multi-Domain Seeds}\n\\label{sec:ecological}\n\n\\paragraph{Cross-model chains.}\nWe construct chains where a different generator (randomly selected from 5) produces each depth step, simulating realistic web contamination.\n\n\\begin{table}[h]\n\\centering\n\\caption{Single-model vs.\\ cross-model chains.}\n\\label{tab:crossmodel}\n\\begin{tabular}{lcccc}\n\\toprule\nSetting & Macro-F1 & Gen-0 F1 & Gen-1 F1 & Gen-2+ F1 \\\\\n\\midrule\nSingle-model chains & 0.81 & 0.94 & 0.75 & 0.77 \\\\\nCross-model chains & 0.42 & 0.65 & 0.32 & 0.35 \\\\\nChance & 0.33 & 0.33 & 0.33 & 0.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-model chains produce near-chance depth estimation (0.42). When different generators produce each depth step, the vocabulary statistics at any given depth reflect the current generator's preferences more than cumulative chain depth. Gen-0 identification survives partially (0.65) because human text remains distinct, but gen-1/gen-2+ classification is effectively random.\n\n\\paragraph{Multi-domain seeds.}\nWe expand to 4 domains with 500 seeds each using Pythia-2.8B.\n\n\\begin{table}[h]\n\\centering\n\\caption{Multi-domain results.}\n\\label{tab:domain}\n\\begin{tabular}{lcccc}\n\\toprule\nDomain & Within-Domain F1 & Gen-0 hapax$_\\text{med}$ & Gen-2+ hapax$_\\text{med}$ & $\\Delta$hapax \\\\\n\\midrule\nWikipedia & 0.83 & 0.47 & 0.26 & 0.21 \\\\\nNews & 0.80 & 0.44 & 0.27 & 0.17 \\\\\nScientific & 0.76 & 0.52 & 0.35 & 0.17 \\\\\nCreative & 0.72 & 0.38 & 0.28 & 0.10 \\\\\nCross-domain avg & 0.59 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWithin-domain performance correlates with the hapax ratio gap ($\\Delta$hapax) between gen-0 and gen-2+: Wikipedia/news have the largest gaps (0.21/0.17) and highest F1 (0.83/0.80), while creative writing has the smallest gap (0.10) and lowest F1 (0.72). Cross-domain transfer drops to 0.59 because baseline vocabulary statistics differ across domains---scientific gen-0 text (hapax median 0.52) overlaps with other domains' synthetic ranges, confounding domain and depth.\n\n%--- 4.7 Depth Resolution Ceiling ---\n\\subsection{Depth Resolution Ceiling}\n\\label{sec:ordinal}\n\nWe test 5-class ordinal classification (gen-0 through gen-4) on continuation chains.\n\n\\begin{table}[h]\n\\centering\n\\caption{5-class ordinal classification results.}\n\\label{tab:ordinal}\n\\begin{tabular}{lccc}\n\\toprule\nClass & Precision & Recall & F1 \\\\\n\\midrule\ngen-0 & 0.93 & 0.90 & 0.91 \\\\\ngen-1 & 0.54 & 0.62 & 0.58 \\\\\ngen-2 & 0.36 & 0.40 & 0.38 \\\\\ngen-3 & 0.29 & 0.33 & 0.31 \\\\\ngen-4 & 0.31 & 0.35 & 0.33 \\\\\n\\midrule\n\\multicolumn{3}{l}{5-class macro-F1} & 0.52 \\\\\n\\multicolumn{3}{l}{3-class macro-F1 (same data)} & 0.82 \\\\\n\\multicolumn{3}{l}{Adjacent confusion rate} & 0.44 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{5-class confusion matrix (row = true, column = predicted; values are proportions).}\n\\label{tab:confusion}\n\\begin{tabular}{lccccc}\n\\toprule\n & gen-0 & gen-1 & gen-2 & gen-3 & gen-4 \\\\\n\\midrule\ngen-0 & \\textbf{0.90} & 0.07 & 0.02 & 0.01 & 0.00 \\\\\ngen-1 & 0.09 & \\textbf{0.62} & 0.18 & 0.07 & 0.04 \\\\\ngen-2 & 0.03 & 0.21 & \\textbf{0.40} & 0.22 & 0.14 \\\\\ngen-3 & 0.02 & 0.10 & 0.24 & \\textbf{0.33} & 0.31 \\\\\ngen-4 & 0.01 & 0.07 & 0.16 & 0.28 & \\textbf{0.48} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n5-class macro-F1 drops to 0.52 (from 0.82 for 3-class). Gen-2 through gen-4 collapse into mutual confusion: gen-3 and gen-4 F1 scores (0.31, 0.33) are at chance level. The confusion matrix shows a diagonal-plus-adjacent pattern (44\\% of errors are off-by-one) consistent with a smoothly converging feature distribution rather than discrete depth categories. This directly reflects H$_1$ convergence: by depth 2, the feature distributions have stabilized, making deeper classes statistically indistinguishable. The practical depth resolution ceiling is $\\sim$2--3 classes.\n\n%--- 4.8 Robustness Analysis ---\n\\subsection{Robustness to Human Edits and Character-Level Features}\n\\label{sec:robustness}\n\n\\paragraph{Edit robustness.}\nWe test robustness to simulated human edits via random word replacement (5\\%, 10\\%, 20\\%) and LLM-simulated light rephrasing.\n\n\\begin{table}[h]\n\\centering\n\\caption{Robustness to human edits.}\n\\label{tab:edits}\n\\begin{tabular}{lccc}\n\\toprule\nEdit Type & Edit Rate & Macro-F1 & $\\Delta$ vs.\\ Baseline \\\\\n\\midrule\nNone & 0\\% & 0.82 & --- \\\\\nRandom replace & 5\\% & 0.77 & $-0.05$ \\\\\nRandom replace & 10\\% & 0.70 & $-0.12$ \\\\\nRandom replace & 20\\% & 0.58 & $-0.24$ \\\\\nLLM-simulated & light & 0.63 & $-0.19$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSurface features are fragile under editing. At 10\\% word replacement, F1 drops by 0.12; LLM-simulated light editing causes a 0.19 drop because the editing model introduces its own vocabulary preferences, adding a second generator's fingerprint. The crossover where depth estimation becomes worse than binary detection occurs at approximately 12\\% replacement rate. Real-world synthetic text is routinely edited at or above this level.\n\n\\paragraph{LD-Score features.}\nWe evaluate LD-Score \\citep{tulchinskii2024ldscore} as a character-level complement.\n\n\\begin{table}[h]\n\\centering\n\\caption{LD-Score feature analysis.}\n\\label{tab:ldscore}\n\\begin{tabular}{lcc}\n\\toprule\nFeature Set & Macro-F1 & LOO Cross-Gen F1 \\\\\n\\midrule\nSurface only & 0.82 & 0.48 \\\\\nLD-Score only & 0.61 & 0.46 \\\\\nSurface + LD & 0.83 & 0.49 \\\\\nFull + LD & 0.83 & 0.50 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLD-Score achieves moderate standalone performance (0.61) but provides no complementary signal when combined with surface features (+0.01). Character-level distributions partially capture vocabulary depletion through character frequency shifts but are redundant with word-level statistics. Cross-generator transfer with LD-Score (0.46) remains poor.\n\n%--- 4.9 Learned Representations ---\n\\subsection{End-to-End Learned Representations}\n\\label{sec:e2e}\n\nWe fine-tune Qwen3.5-0.8B with QLoRA for end-to-end depth classification to test whether learned representations can discover depth signal beyond handcrafted features.\n\n\\begin{table}[h]\n\\centering\n\\caption{End-to-end vs.\\ handcrafted features.}\n\\label{tab:e2e}\n\\begin{tabular}{lccc}\n\\toprule\nModel & Within-Gen F1 & Cross-Gen LOO F1 & $\\Delta$ Cross-Gen \\\\\n\\midrule\nHandcrafted (surface + ref) & 0.83 & 0.48 & --- \\\\\nQLoRA Qwen3.5-0.8B & 0.87 & 0.53 & +0.05 \\\\\nHandcrafted surface only & 0.82 & 0.48 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe end-to-end model achieves marginally higher within-generator F1 (0.87 vs.\\ 0.82) by learning soft vocabulary depletion features beyond hapax ratio and TTR. However, cross-generator transfer shows only +0.05 improvement (0.53 vs.\\ 0.48), meaning learned representations are also predominantly generator-specific. Attention analysis reveals the model focuses on high-frequency function words and punctuation---tokens whose usage patterns shift under vocabulary impoverishment. Even with 0.8B parameters and full sequence access, the model does not discover hidden distributional structure beyond surface statistics. This closes the ``bigger model'' escape hatch: the cross-generator signal genuinely is not present.\n\n%--- 4.10 Downstream Utility ---\n\\subsection{Downstream Utility}\n\\label{sec:downstream}\n\nWe test whether depth-aware filtering improves downstream model quality by fine-tuning Pythia-410M on depth-stratified data subsets and comparing against binary detection baselines.\n\n\\begin{table}[h]\n\\centering\n\\caption{Downstream fine-tuning perplexity.}\n\\label{tab:downstream}\n\\begin{tabular}{lcc}\n\\toprule\nTraining Data & Perplexity & Data Size (\\%) \\\\\n\\midrule\nGen-0 only & 18.2 & 33 \\\\\nGen-0 + gen-1 & 18.8 & 67 \\\\\nAll depths unfiltered & 19.5 & 100 \\\\\nDepth-aware filter ($\\leq$gen-1) & 18.5 & 38 \\\\\nFastDetectGPT binary filter & 18.4 & 42 \\\\\nLD-Score binary filter & 18.6 & 40 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth--quality correlation.}\n\\label{tab:correlation}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nSpearman $\\rho$ (depth vs.\\ ppl degradation) & 0.19 \\\\\n$p$-value & 0.04 \\\\\nDepth filter vs.\\ best binary gap & $-0.3\\%$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA weak positive correlation exists between generation depth and quality degradation ($\\rho = 0.19$, $p = 0.04$), but the effect size is negligible. Depth-aware filtering achieves perplexity 18.5, compared to 18.4 for FastDetectGPT binary filtering---a $-0.3\\%$ gap favoring the simpler baseline. The ordinal depth information provides no practical advantage over binary classification for data curation. This is the expected consequence of the preceding results: if depth estimation relies on generator-specific surface features with poor cross-generator transfer, the noisy depth predictions cannot outperform binary detection for downstream filtering.\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Extending attractor cycle theory.}\nOur central finding---that H$_1$ holds for non-paraphrastic chains---extends the attractor cycle theory of \\citet{anonymous2025attractor} beyond its original paraphrastic setting. The convergence mechanism is distinct: paraphrastic chains converge because the semantic-preservation constraint restricts the output space, while non-paraphrastic chains converge because autoregressive sampling from a fixed model concentrates probability mass on preferred tokens regardless of semantic constraints. Both mechanisms produce the same practical outcome: depth-discriminable classes are bounded at $\\sim$2--3.\n\n\\paragraph{Vocabulary impoverishment as a universal but shallow fingerprint.}\nRecursive generation progressively depletes rare vocabulary---a mechanical consequence of sampling from a fixed token distribution. This creates a detectable but shallow fingerprint: type-token ratio and hapax ratio decrease monotonically with depth but stabilize by gen-2, and their absolute values are determined by the generator's vocabulary preferences rather than chain depth per se. The fingerprint is ``universal'' in that all tested generators exhibit vocabulary depletion, but ``shallow'' in that it does not encode generator-invariant depth information.\n\n\\paragraph{Implications for data governance.}\nOur results suggest that binary real-vs-synthetic detection remains the practically optimal granularity for data filtering in the current paradigm. Depth-aware approaches face a three-way non-generalization barrier: the signal is generator-specific, prompt-type-specific, and domain-specific. Until depth features are identified that generalize across these axes, binary filtering with established detectors \\citep{bao2024fastdetectgpt,tulchinskii2024ldscore} is both simpler and more effective.\n\n\\paragraph{Limitations.}\nOur study is limited to 5 open-weight models up to 2.8B parameters; larger or closed-source models may exhibit different vocabulary dynamics. The simulated editing is a lower bound on real-world post-processing. We do not test instruction-tuned or RLHF-aligned models, which may have different distributional properties. Our cross-model chains use random generator assignment; real contamination may have structured patterns.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe tested two hypotheses about distributional dynamics in recursive non-paraphrastic LLM generation chains. Our experiments across 5 generators, 4 domains, and 3 prompt types provide strong evidence for H$_1$ (convergence): non-paraphrastic chains converge to near-stationary distributions within 2 generation steps, extending attractor cycle theory beyond paraphrastic settings. The detectable depth signal is confined to vocabulary impoverishment---surface features (hapax ratio, TTR) that explain 98.8\\% of classifier performance but are generator-specific, prompt-type-specific, and fragile under editing. Cross-generator depth estimation is near chance (macro-F1 = 0.48), and depth-aware filtering provides no advantage over binary baselines.\n\nThese negative results establish clear boundary conditions: vocabulary impoverishment is a universal consequence of autoregressive generation but not a viable basis for general-purpose depth estimation. Future work should investigate whether training-time features (model weights, sampling parameters) or generation-aware watermarking can provide the generator-invariant depth signal that distributional post-hoc analysis cannot.\n\n%==============================================================================\n% References\n%==============================================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Anonymous(2025)]{anonymous2025attractor}\nAnonymous.\n\\newblock Attractor cycles in paraphrastic generation chains.\n\\newblock In \\emph{Proceedings of ACL}, 2025.\n\n\\bibitem[Bai et~al.(2023)]{bai2023qwen}\nJinze Bai et~al.\n\\newblock Qwen technical report.\n\\newblock \\emph{arXiv preprint arXiv:2309.16609}, 2023.\n\n\\bibitem[Bao et~al.(2024)]{bao2024fastdetectgpt}\nGuangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi Yang, and Yue Zhang.\n\\newblock Fast-{D}etect{GPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In \\emph{Proceedings of ICLR}, 2024.\n\n\\bibitem[Biderman et~al.(2023)]{biderman2023pythia}\nStella Biderman et~al.\n\\newblock Pythia: A suite for analyzing large language models across training and scaling.\n\\newblock In \\emph{Proceedings of ICML}, 2023.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024tale}\nElvis Dohmatob, Yunzhen Feng, and Julia Kempe.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In \\emph{Proceedings of ICML}, 2024.\n\n\\bibitem[Groeneveld et~al.(2024)]{groeneveld2024olmo}\nDirk Groeneveld et~al.\n\\newblock {OLMo}: Accelerating the science of language models.\n\\newblock In \\emph{Proceedings of ACL}, 2024.\n\n\\bibitem[Kirchenbauer et~al.(2023)]{kirchenbauer2023watermark}\nJohn Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein.\n\\newblock A watermark for large language models.\n\\newblock In \\emph{Proceedings of ICML}, 2023.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nEric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher~D. Manning, and Chelsea Finn.\n\\newblock {DetectGPT}: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{Proceedings of ICML}, 2023.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024modelcollapse}\nIlia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, and Ross Anderson.\n\\newblock The curse of recursion: Training on generated data makes models forget.\n\\newblock \\emph{Nature}, 2024.\n\n\\bibitem[Tulchinskii et~al.(2024)]{tulchinskii2024ldscore}\nEduard Tulchinskii et~al.\n\\newblock Intrinsic dimension estimation for robust detection of {AI}-generated texts.\n\\newblock In \\emph{Proceedings of NeurIPS}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "405d7d11-5c36-41db-9d3f-689f61b6b1cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T181213 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerp…",
  "leafUuid": "aed6aad0-30e5-40c9-ac41-f133eac832f9",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream ID",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13"
}
```

---

### Tool call

_source line 22 · 2026-05-14T18:40:37.870Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q7Njd21AfLwamkhx3ZF2X1`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper (two passes for references)",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aed6aad0-30e5-40c9-ac41-f133eac832f9",
  "isSidechain": false,
  "requestId": "req_011Cb2x647orUTeVGMPKY7cL",
  "type": "assistant",
  "uuid": "34365a2e-e5b9-44c5-b8e9-65d941657633",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MgDFhpCbRXntfDnKHW7qNx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10592,
      "cache_read_input_tokens": 38577,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10592,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 38577,
          "cache_creation_input_tokens": 10592,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10592
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

_source line 23 · 2026-05-14T18:40:39.077Z_

<details><summary>↩ Tool result · `toolu_01Q7Njd21AfLwamkhx3ZF2X1`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
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

Package natbib Warning: Citation `mitchell2023detectgpt' on page 1 undefined on
 input line 32.


Package natbib Warning: Citation `bao2024fastdetectgpt' on page 1 undefined on 
input line 32.


Package natbib Warning: Citation `tulchinskii2024ldscore' on page 1 undefined o
n input line 32.


Package natbib Warning: Citation `anonymous2025attractor' on page 1 undefined o
n input line 34.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on
 input line 59.


Package natbib Warning: Citation `bao2024fastdetectgpt' on page 2 undefined on 
input line 59.


Package natbib Warning: Citation `kirchenbauer2023watermark' on page 2 undefine
d on input line 59.


Package natbib Warning: Citation `tulchinskii2024ldscore' on page 2 undefined o
n input line 59.


Package natbib Warning: Citation `shumailov2024modelcollapse' on page 2 undefin
ed on input line 62.


Package natbib Warning: Citation `dohmatob2024tale' on page 2 undefined on inpu
t line 62.


Package natbib Warning: Citation `anonymous2025attractor' on page 2 undefined o
n input line 65.


Package natbib Warning: Citation `biderman2023pythia' on page 2 undefined on in
put line 81.


Package natbib Warning: Citation `groeneveld2024olmo' on page 2 undefined on in
put line 81.


Package natbib Warning: Citation `bai2023qwen' on page 2 undefined on input lin
e 81.

[2]

Package natbib Warning: Citation `tulchinskii2024ldscore' on page 3 undefined o
n input line 105.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:importance' on page 3 undefined on input line 160
.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[3]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[4]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[5]

LaTeX Warning: `h' float specifier changed to `ht'.


Package natbib Warning: Citation `tulchinskii2024ldscore' on page 6 undefined o
n input line 394.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


Package natbib Warning: Citation `anonymous2025attractor' on page 6 undefined o
n input line 484.

[6]

Package natbib Warning: Citation `bao2024fastdetectgpt' on page 7 undefined on 
input line 490.


Package natbib Warning: Citation `tulchinskii2024ldscore' on page 7 undefined o
n input line 490.

[7] [8]

Package natbib Warning: There were undefined citations.

[9] [10] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1000
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1000
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1000.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf
 Ok [100] [109] [98] [99] [108])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf
 Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]
[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]
[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]
[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]
[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]
[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]
[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf
 Ok [185] [178] [179] [170] [186])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf
 Ok [188] [189] [190]) ) ) )
(some charht values had to be adjusted by as much as 0.06943pt)
Font metrics written on tcrm1000.tfm.
Output written on tcrm1000.600gf (128 characters, 23548 bytes).
Transcript written on tcrm1000.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk: successfully generated.


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
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmr5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmti9.pfb>
Output written on paper.pdf (10 pages, 245339 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
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
nts/map/pdftex/updmap/pdftex.map}] [2]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[3]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[4]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[5]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[6] [7] [8] [9] [10] (./paper.aux) ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts
/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi
7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti1
0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>
Output written on paper.pdf (10 pages, 248758 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34365a2e-e5b9-44c5-b8e9-65d941657633",
  "isSidechain": false,
  "promptId": "00675285-eb7e-4fe5-a2b7-b441582ee0b5",
  "type": "user",
  "uuid": "b1286e4d-3836-422f-9d76-7b7cda13a2ab",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `mitchell2023detectgpt' on page 1 undefined on\n input line 32.\n\n\nPackage natbib Warning: Citation `bao2024fastdetectgpt' on page 1 undefined on \ninput line 32.\n\n\nPackage natbib Warning: Citation `tulchinskii2024ldscore' on page 1 undefined o\nn input line 32.\n\n\nPackage natbib Warning: Citation `anonymous2025attractor' on page 1 undefined o\nn input line 34.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on\n input line 59.\n\n\nPackage natbib Warning: Citation `bao2024fastdetectgpt' on page 2 undefined on \ninput line 59.\n\n\nPackage natbib Warning: Citation `kirchenbauer2023watermark' on page 2 undefine\nd on input line 59.\n\n\nPackage natbib Warning: Citation `tulchinskii2024ldscore' on page 2 undefined o\nn input line 59.\n\n\nPackage natbib Warning: Citation `shumailov2024modelcollapse' on page 2 undefin\ned on input line 62.\n\n\nPackage natbib Warning: Citation `dohmatob2024tale' on page 2 undefined on inpu\nt line 62.\n\n\nPackage natbib Warning: Citation `anonymous2025attractor' on page 2 undefined o\nn input line 65.\n\n\nPackage natbib Warning: Citation `biderman2023pythia' on page 2 undefined on in\nput line 81.\n\n\nPackage natbib Warning: Citation `groeneveld2024olmo' on page 2 undefined on in\nput line 81.\n\n\nPackage natbib Warning: Citation `bai2023qwen' on page 2 undefined on input lin\ne 81.\n\n[2]\n\nPackage natbib Warning: Citation `tulchinskii2024ldscore' on page 3 undefined o\nn input line 105.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:importance' on page 3 undefined on input line 160\n.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[3]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nPackage natbib Warning: Citation `tulchinskii2024ldscore' on page 6 undefined o\nn input line 394.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nPackage natbib Warning: Citation `anonymous2025attractor' on page 6 undefined o\nn input line 484.\n\n[6]\n\nPackage natbib Warning: Citation `bao2024fastdetectgpt' on page 7 undefined on \ninput line 490.\n\n\nPackage natbib Warning: Citation `tulchinskii2024ldscore' on page 7 undefined o\nn input line 490.\n\n[7] [8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] [10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1000\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1000\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1000.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf\n Ok [100] [109] [98] [99] [108])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf\n Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]\n[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]\n[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]\n[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]\n[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]\n[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]\n[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf\n Ok [185] [178] [179] [170] [186])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf\n Ok [188] [189] [190]) ) ) )\n(some charht values had to be adjusted by as much as 0.06943pt)\nFont metrics written on tcrm1000.tfm.\nOutput written on tcrm1000.600gf (128 characters, 23548 bytes).\nTranscript written on tcrm1000.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.60\n0pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmr5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmti9.pfb>\nOutput written on paper.pdf (10 pages, 245339 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[3]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6] [7] [8] [9] [10] (./paper.aux) ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts\n/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi\n7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti1\n0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>\nOutput written on paper.pdf (10 pages, 248758 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "34365a2e-e5b9-44c5-b8e9-65d941657633",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T181213 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerp…",
  "leafUuid": "b1286e4d-3836-422f-9d76-7b7cda13a2ab",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream ID",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13"
}
```

---

### Assistant

_source line 26 · 2026-05-14T18:40:46.064Z_

编译成功，10 页 PDF 生成于 `worst/paper.tex`。

论文覆盖全部 11 个实验（对应 Tables 2--17），以 H₁ vs H₂ 假设检验为主线，将结果重构为 negative-but-informative 经验贡献：非释义链也快速收敛，深度信号仅来自词汇贫化（generator-specific），reference-model 熵特征无独立信号，depth-aware filtering 不优于二分类基线。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1286e4d-3836-422f-9d76-7b7cda13a2ab",
  "isSidechain": false,
  "requestId": "req_011Cb2x6RL1poD9u9nbkof4J",
  "type": "assistant",
  "uuid": "bd347a67-360c-470e-a73d-3acd5a710ae4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115rCMRDLk8xBr4QnWz96na",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7662,
      "cache_read_input_tokens": 49169,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7662,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 49169,
          "cache_creation_input_tokens": 7662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7662
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

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T181213 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerp…",
  "leafUuid": "bd347a67-360c-470e-a73d-3acd5a710ae4",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream ID",
  "sessionId": "0e069ccf-54de-4ec0-aafa-7fc5c7e58d13"
}
```

---
