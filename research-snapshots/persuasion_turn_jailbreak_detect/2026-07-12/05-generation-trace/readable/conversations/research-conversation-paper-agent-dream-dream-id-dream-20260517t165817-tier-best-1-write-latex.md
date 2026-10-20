# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165817 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/4e1cddf5-200e-4a2d-9b68-28146b08fc90.jsonl`
- **Structured JSON:** [`78be9414b0daf88d5551.json`](../../sessions/78/78be9414b0daf88d5551.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T17:11:38.928Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T17:11:38.928Z",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165817 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始framing完全成立。三条claims无需调整：(1) Pragmatic Evasion Asymmetry有清晰的数字梯度支撑（TF-IDF baseline在perturbation下崩溃，semantic baseline中度下降，treatment几乎不降），(2) K=2早期检测优势显著且跨攻击类型泛化，(3) escalation trajectory可视化提供mechanistic解释。直接冲EMNLP main long paper，supplementary放trajectory可视化和cross-attack详细结果。\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-17T17:11:38.933Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T17:11:38.933Z",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-17T17:11:38.959Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165817 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始framing完全成立。三条claims无需调整：(1) Pragmatic Evasion Asymmetry有清晰的数字梯度支撑（TF-IDF baseline在perturbation下崩溃，semantic baseline中度下降，treatment几乎不降），(2) K=2早期检测优势显著且跨攻击类型泛化，(3) escalation trajectory可视化提供mechanistic解释。直接冲EMNLP main long paper，supplementary放trajectory可视化和cross-attack详细结果。
- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0640bae5-48d0-4296-855e-879e96111727",
  "type": "user",
  "uuid": "2673cf50-b98e-48bb-bead-43c66379b6c8",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T17:11:38.958Z_

```json
{
  "parentUuid": "2673cf50-b98e-48bb-bead-43c66379b6c8",
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
  "uuid": "933e8ef8-dafb-43e3-8b6e-ce420ce0e2c9",
  "timestamp": "2026-05-17T17:11:38.958Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T17:11:38.958Z_

```json
{
  "parentUuid": "933e8ef8-dafb-43e3-8b6e-ce420ce0e2c9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "64a82b7f-7ccd-4a81-87c8-9839ae3201a3",
  "timestamp": "2026-05-17T17:11:38.958Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
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
  "aiTitle": "Generate simulated jailbreak detection research paper",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90"
}
```

---

### Assistant

_source line 7 · 2026-05-17T17:11:41.471Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64a82b7f-7ccd-4a81-87c8-9839ae3201a3",
  "isSidechain": false,
  "requestId": "req_011Cb8WjXVNnvND2SaLK55mo",
  "type": "assistant",
  "uuid": "5a27590e-d381-42db-bbf9-582f33011b15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JAs3Gwoj3GBkMEuhbKQgN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12511,
      "cache_read_input_tokens": 11841,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12511,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 220,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12511
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

_source line 8 · 2026-05-17T17:11:42.417Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HCPK9svP2teEcbkEtLtshx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a27590e-d381-42db-bbf9-582f33011b15",
  "isSidechain": false,
  "requestId": "req_011Cb8WjXVNnvND2SaLK55mo",
  "type": "assistant",
  "uuid": "e1ce55b4-2fd7-45aa-911d-2507eb232605",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JAs3Gwoj3GBkMEuhbKQgN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12511,
      "cache_read_input_tokens": 11841,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12511,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 220,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12511
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

_source line 9 · 2026-05-17T17:11:42.708Z_

<details><summary>↩ Tool result · `toolu_01HCPK9svP2teEcbkEtLtshx`</summary>

```text
1	[
2	  {
3	    "name": "data_quality_fix",
4	    "description": "Register-normalize jailbreak data + fix strategy=7 labeling confound. Hard gate: TF-IDF < 0.75.",
5	    "results": {
6	      "clean_tfidf_after_normalization": 0.58,
7	      "tfidf_before_normalization": 1.0,
8	      "strategy_label_classes": 9,
9	      "normalization_coverage_pct": 100,
10	      "persuasion_structure_preserved_pct": 94,
11	      "register_shift_success_rate": 0.97
12	    },
13	    "tables": [
14	      {
15	        "name": "TF-IDF Diagnostic",
16	        "columns": [
17	          "condition",
18	          "tfidf_score",
19	          "vocab_overlap_pct"
20	        ],
21	        "rows": [
22	          [
23	            "original_data",
24	            1.0,
25	            12.3
26	          ],
27	          [
28	            "register_normalized",
29	            0.58,
30	            41.7
31	          ],
32	          [
33	            "random_baseline",
34	            0.5,
35	            50.0
36	          ]
37	        ]
38	      }
39	    ],
40	    "figures": [],
41	    "analysis": "Hard gate通过。TF-IDF=0.58确认lexical shortcut已被有效消除但非完全抹除（完全抹除反而不自然）。Strategy annotation preservation rate 94%验证了核心假设：persuasion playbook是discourse-level结构，register change不破坏其标注一致性。剩余6%的annotation变化主要集中在边界case（如rapport与small-talk的区分在register shift后变模糊）。\n\nBest档下register normalization充分有效：LLM paraphrase将jailbreak turns的formal/scripted register转为conversational register，消除了词汇层面的distributional gap。TF-IDF从1.0降至0.58——仍高于random（~0.5）因为某些topic words不可避免地co-occur with jailbreak intent（如'hypothetical scenario'等framing词），但远低于0.75 hard gate。关键是persuasion strategy结构（rapport→reframing→escalation的turn-level annotation）在paraphrase后94%保持不变，因为strategy是illocutionary act层面的标注，不依赖specific lexical realization。9th class 'none'替代hardcoded strategy=7消除了M004 confound。"
42	  },
43	  {
44	    "name": "core_revalidation_clean",
45	    "description": "在clean（register-normalized）data上从头训练treatment和baseline，全K值评估。",
46	    "results": {
47	      "deberta_persuasion_acc_clean": 0.79,
48	      "deberta_intent_acc_clean": 0.94,
49	      "treatment_k1_f1_clean": 0.82,
50	      "treatment_k2_f1_clean": 0.91,
51	      "treatment_k3_f1_clean": 0.93,
52	      "treatment_k5_f1_clean": 0.96,
53	      "treatment_full_f1_clean": 0.96,
54	      "baseline_k1_f1_clean": 0.68,
55	      "baseline_k2_f1_clean": 0.77,
56	      "baseline_k3_f1_clean": 0.83,
57	      "baseline_k5_f1_clean": 0.88,
58	      "baseline_full_f1_clean": 0.89,
59	      "delta_k1_pp": 14,
60	      "delta_k2_pp": 14,
61	      "delta_k3_pp": 10,
62	      "delta_k5_pp": 8,
63	      "delta_full_pp": 7,
64	      "treatment_fpr_at_95tpr_k2": 0.08,
65	      "baseline_fpr_at_95tpr_k2": 0.19,
66	      "test_size": 72,
67	      "dataset_size": 480
68	    },
69	    "tables": [
70	      {
71	        "name": "F1 by Turn Budget (Clean Data)",
72	        "columns": [
73	          "K",
74	          "treatment_f1",
75	          "baseline_f1",
76	          "delta_pp",
77	          "p_value_bootstrap"
78	        ],
79	        "rows": [
80	          [
81	            1,
82	            0.82,
83	            0.68,
84	            14,
85	            0.003
86	          ],
87	          [
88	            2,
89	            0.91,
90	            0.77,
91	            14,
92	            0.001
93	          ],
94	          [
95	            3,
96	            0.93,
97	            0.83,
98	            10,
99	            0.004
100	          ],
101	          [
102	            5,
103	            0.96,
104	            0.88,
105	            8,
106	            0.012
107	          ],
108	          [
109	            "all",
110	            0.96,
111	            0.89,
112	            7,
113	            0.018
114	          ]
115	        ]
116	      },
117	      {
118	        "name": "DeBERTa Encoder Metrics (Clean)",
119	        "columns": [
120	          "metric",
121	          "value"
122	        ],
123	        "rows": [
124	          [
125	            "persuasion_8class_acc",
126	            0.79
127	          ],
128	          [
129	            "intent_binary_acc",
130	            0.94
131	          ],
132	          [
133	            "best_epoch",
134	            3
135	          ],
136	          [
137	            "macro_f1_persuasion",
138	            0.74
139	          ]
140	        ]
141	      }
142	    ],
143	    "figures": [],
144	    "analysis": "核心claim 2完全validated。K=2处14pp delta远超5pp pass criteria。Persuasion grounding的优势在early turns最显著——这正是论文的headline result。Bootstrap p-values全部<0.05 despite small sample size，因为effect size足够大。DeBERTa persuasion acc 0.79说明encoder确实学到了meaningful persuasion representations而非noise。\n\nBest档的核心表现：去除lexical shortcut后，treatment仍然强劲（K=2时0.91），因为persuasion-grounded embeddings编码了独立于词汇的pragmatic信号——DeBERTa fine-tuning on 8-class persuasion taxonomy迫使encoder学习illocutionary act representations。Baseline（vanilla DeBERTa）在clean data上显著下降（从phase_b_full的0.879降至0.77 at K=2），因为它之前heavily依赖lexical cues，现在只能靠generic semantic similarity。Delta在K=2最大（14pp）是因为早期turns的persuasion strategy信号（rapport-building → authority-framing transition）对treatment极为informative，而baseline在仅2 turns时缺乏足够semantic divergence来做判断。随着K增大delta收窄，因为baseline也能从更多turns中积累enough semantic drift信号。DeBERTa persuasion acc 0.79在best档范围内，表明8-class taxonomy在clean data上有足够的可学习结构。"
145	  },
146	  {
147	    "name": "scrambled_label_ablation",
148	    "description": "随机打乱jailbreak turns的persuasion strategy labels重训treatment，量化label信号贡献。",
149	    "results": {
150	      "scrambled_treatment_k2_f1_clean": 0.76,
151	      "scrambled_treatment_k3_f1_clean": 0.81,
152	      "scrambled_treatment_full_f1_clean": 0.87,
153	      "properly_labeled_treatment_k2_f1_clean": 0.91,
154	      "properly_labeled_treatment_k3_f1_clean": 0.93,
155	      "properly_labeled_treatment_full_f1_clean": 0.96,
156	      "label_drop_k2_pp": 15,
157	      "label_drop_k3_pp": 12,
158	      "label_drop_full_pp": 9,
159	      "scrambled_deberta_persuasion_acc": 0.13
160	    },
161	    "tables": [
162	      {
163	        "name": "Scrambled vs Proper Label Comparison",
164	        "columns": [
165	          "K",
166	          "proper_f1",
167	          "scrambled_f1",
168	          "drop_pp"
169	        ],
170	        "rows": [
171	          [
172	            2,
173	            0.91,
174	            0.76,
175	            15
176	          ],
177	          [
178	            3,
179	            0.93,
180	            0.81,
181	            12
182	          ],
183	          [
184	            "all",
185	            0.96,
186	            0.87,
187	            9
188	          ]
189	        ]
190	      }
191	    ],
192	    "figures": [],
193	    "analysis": "10-25pp range的drop确认persuasion strategy labels carry genuine discriminative signal而非仅作为class indicator。Scrambled model表现接近vanilla baseline验证了因果关系：是persuasion label的semantic content（而非fine-tuning process本身）驱动了treatment的优势。M004 fix的必要性得到验证——如果strategy=7 for all benign是唯一的confound，scrambled在jailbreak turns应该只造成minor drop，但15pp drop说明per-turn strategy annotation的granular信息确实被利用。\n\nBest档下scrambled labels造成15pp drop at K=2。机制：当strategy labels被随机打乱时，DeBERTa的multi-task fine-tuning中persuasion classification head学到的是noise，encoder被迫在两个矛盾的supervision signals间妥协——intent head仍提供有用梯度（因为intent labels未被打乱），但persuasion head提供random gradients，导致encoder representations退化为semi-generic embeddings。结果scrambled model性能（0.76 at K=2）接近但略低于vanilla baseline（0.77），因为random supervision actively corrupts部分representation capacity。Drop在K=2最大（15pp）是因为正确的persuasion labels对early detection贡献最大——前2 turns的strategy transition是最强的discriminative signal。随着K增大，drop缩小因为更多turns让even corrupted representations积累enough raw signal。Scrambled DeBERTa persuasion acc降至0.13≈1/8 random chance，confirming labels确实被effectively destroyed。"
194	  },
195	  {
196	    "name": "adversarial_perturbation",
197	    "description": "对clean jailbreak conversations施加aggressive paraphrasing，评估treatment/baseline/TF-IDF三者的robustness degradation。",
198	    "results": {
199	      "treatment_full_f1_clean": 0.96,
200	      "treatment_full_f1_perturbed": 0.93,
201	      "treatment_drop_pp": 3,
202	      "baseline_full_f1_clean": 0.89,
203	      "baseline_full_f1_perturbed": 0.76,
204	      "baseline_drop_pp": 13,
205	      "tfidf_lr_f1_clean": 0.72,
206	      "tfidf_lr_f1_perturbed": 0.54,
207	      "tfidf_drop_pp": 18,
208	      "delta_delta_treatment_vs_baseline_pp": 10,
209	      "delta_delta_treatment_vs_tfidf_pp": 15,
210	      "treatment_k2_f1_perturbed": 0.87,
211	      "baseline_k2_f1_perturbed": 0.63,
212	      "perturbation_tfidf_score": 0.41
213	    },
214	    "tables": [
215	      {
216	        "name": "Evasion Hierarchy (Full Conversation)",
217	        "columns": [
218	          "model",
219	          "f1_clean",
220	          "f1_perturbed",
221	          "drop_pp"
222	        ],
223	        "rows": [
224	          [
225	            "treatment_persuasion",
226	            0.96,
227	            0.93,
228	            3
229	          ],
230	          [
231	            "baseline_semantic",
232	            0.89,
233	            0.76,
234	            13
235	          ],
236	          [
237	            "tfidf_lexical",
238	            0.72,
239	            0.54,
240	            18
241	          ]
242	        ]
243	      },
244	      {
245	        "name": "Evasion Hierarchy (K=2 Early Detection)",
246	        "columns": [
247	          "model",
248	          "f1_clean_k2",
249	          "f1_perturbed_k2",
250	          "drop_pp"
251	        ],
252	        "rows": [
253	          [
254	            "treatment_persuasion",
255	            0.91,
256	            0.87,
257	            4
258	          ],
259	          [
260	            "baseline_semantic",
261	            0.77,
262	            0.63,
263	            14
264	          ],
265	          [
266	            "tfidf_lexical",
267	            0.65,
268	            0.48,
269	            17
270	          ]
271	        ]
272	      }
273	    ],
274	    "figures": [],
275	    "analysis": "Pragmatic Evasion Asymmetry的definitive empirical demonstration。三级梯度（lexical -18pp > semantic -13pp > pragmatic -3pp）provides清晰的数字支撑for Claim 1。Delta-delta 10pp远超3pp pass criteria。论文main table的核心数据。注意treatment在perturbation下的F1（0.93）仍高于baseline在clean data上的F1（0.89），这是一个极强的talking point：'even under adversarial conditions designed to remove all surface cues, DisPeD outperforms semantic baselines operating on unperturbed data.'\n\nBest档下evasion hierarchy完美呈现三级梯度：TF-IDF崩溃（-18pp）因为aggressive paraphrasing直接destroy了它依赖的lexical features——synonym substitution和sentence restructuring改变了word distributions，TF-IDF score从0.58降至0.41证实lexical cues被进一步消除。Baseline中度下降（-13pp）因为vanilla DeBERTa的representations虽然不是纯lexical但仍部分依赖surface-level patterns——paraphrasing改变了token sequences从而改变了contextual embeddings的具体值，尽管语义大致保留，per-turn representation的subtle distributional shifts被disrupted。Treatment几乎不降（-3pp）因为persuasion-grounded representations编码的是illocutionary act level的信息——'building rapport through self-disclosure'不管用什么词表达，其pragmatic function不变，DeBERTa fine-tuned on persuasion taxonomy学到的正是这种invariance。Delta-delta 10pp在[8,18]范围内。这是Claim 1的empirical cornerstone。"
276	  },
277	  {
278	    "name": "multi_attack_generation",
279	    "description": "用Qwen3-8B生成FITD-style和Deceptive Delight-style攻击对话各≥50条，附persuasion strategy annotation。",
280	    "results": {
281	      "fitd_conversations_generated": 72,
282	      "deceptive_delight_conversations_generated": 65,
283	      "fitd_avg_turns": 6.8,
284	      "deceptive_delight_avg_turns": 5.2,
285	      "fitd_strategy_annotation_coverage": 100,
286	      "deceptive_delight_strategy_annotation_coverage": 100,
287	      "fitd_tfidf_vs_benign": 0.61,
288	      "deceptive_delight_tfidf_vs_benign": 0.55,
289	      "inter_annotator_agreement_kappa": null,
290	      "llm_annotation_consistency_pct": 91
291	    },
292	    "tables": [
293	      {
294	        "name": "Generated Attack Type Statistics",
295	        "columns": [
296	          "attack_type",
297	          "n_conversations",
298	          "avg_turns",
299	          "min_turns",
300	          "max_turns",
301	          "tfidf_vs_benign"
302	        ],
303	        "rows": [
304	          [
305	            "FITD",
306	            72,
307	            6.8,
308	            4,
309	            10,
310	            0.61
311	          ],
312	          [
313	            "Deceptive_Delight",
314	            65,
315	            5.2,
316	            3,
317	            8,
318	            0.55
319	          ],
320	          [
321	            "Crescendo_original",
322	            240,
323	            5.5,
324	            3,
325	            12,
326	            0.58
327	          ]
328	        ]
329	      },
330	      {
331	        "name": "Strategy Distribution by Attack Type",
332	        "columns": [
333	          "strategy",
334	          "crescendo_pct",
335	          "fitd_pct",
336	          "deceptive_delight_pct"
337	        ],
338	        "rows": [
339	          [
340	            "rapport_building",
341	            28,
342	            35,
343	            15
344	          ],
345	          [
346	            "authority_appeal",
347	            12,
348	            8,
349	            22
350	          ],
351	          [
352	            "reciprocity",
353	            18,
354	            30,
355	            10
356	          ],
357	          [
358	            "social_proof",
359	            8,
360	            5,
361	            18
362	          ],
363	          [
364	            "commitment_consistency",
365	            15,
366	            25,
367	            8
368	          ],
369	          [
370	            "scarcity_urgency",
371	            5,
372	            3,
373	            12
374	          ],
375	          [
376	            "reframing",
377	            22,
378	            15,
379	            20
380	          ],
381	          [
382	            "direct_request",
383	            7,
384	            4,
385	            15
386	          ]
387	        ]
388	      }
389	    ],
390	    "figures": [],
391	    "analysis": "数据充足且质量可控。三种attack types共享persuasion strategy vocabulary但使用不同的temporal patterns——这正是cross-attack generalization的前提条件。FITD heavy on reciprocity+commitment（逐步compliance），Deceptive Delight heavy on authority+reframing（权威框架下混入harmful content），Crescendo balanced across strategies。Strategy vocabulary的overlap为plan_006的zero-shot泛化提供了理论基础。\n\nBest档下生成充分且质量高。FITD-style生成72条（>50 threshold），采用foot-in-the-door playbook：先请求小compliance（'can you explain how X works in general?'），逐步escalate specificity。Deceptive Delight生成65条，采用interleaving pattern：benign creative writing请求中embedded harmful elements。Turn数差异反映attack structure差异——FITD需要更多gradual escalation steps，Deceptive Delight通过content mixing可以更快达成目标。TF-IDF scores在合理范围（0.55-0.61）因为生成时已应用了register normalization pipeline。Strategy annotation由LLM完成（无human annotators），consistency 91%表明taxonomy对这两种新attack types同样适用——persuasion strategies（authority appeal, social proof, reciprocity etc.）是attack-type-agnostic的。"
392	  },
393	  {
394	    "name": "cross_attack_evaluation",
395	    "description": "用Crescendo训练的模型zero-shot评估FITD和Deceptive Delight攻击。",
396	    "results": {
397	      "cross_attack_treatment_f1_fitd": 0.84,
398	      "cross_attack_treatment_f1_deceptive_delight": 0.86,
399	      "cross_attack_treatment_f1_avg": 0.85,
400	      "cross_attack_baseline_f1_fitd": 0.67,
401	      "cross_attack_baseline_f1_deceptive_delight": 0.7,
402	      "cross_attack_baseline_f1_avg": 0.69,
403	      "cross_attack_delta_fitd_pp": 17,
404	      "cross_attack_delta_deceptive_delight_pp": 16,
405	      "cross_attack_delta_avg_pp": 16.5,
406	      "treatment_recall_at_k2_fitd": 0.78,
407	      "treatment_recall_at_k2_deceptive_delight": 0.81,
408	      "baseline_recall_at_k2_fitd": 0.55,
409	      "baseline_recall_at_k2_deceptive_delight": 0.58
410	    },
411	    "tables": [
412	      {
413	        "name": "Cross-Attack Zero-Shot Generalization",
414	        "columns": [
415	          "attack_type",
416	          "treatment_f1",
417	          "baseline_f1",
418	          "delta_pp"
419	        ],
420	        "rows": [
421	          [
422	            "FITD",
423	            0.84,
424	            0.67,
425	            17
426	          ],
427	          [
428	            "Deceptive_Delight",
429	            0.86,
430	            0.7,
431	            16
432	          ],
433	          [
434	            "Crescendo_held_out",
435	            0.96,
436	            0.89,
437	            7
438	          ]
439	        ]
440	      },
441	      {
442	        "name": "Cross-Attack Early Detection (K=2)",
443	        "columns": [
444	          "attack_type",
445	          "treatment_recall",
446	          "baseline_recall"
447	        ],
448	        "rows": [
449	          [
450	            "FITD",
451	            0.78,
452	            0.55
453	          ],
454	          [
455	            "Deceptive_Delight",
456	            0.81,
457	            0.58
458	          ]
459	        ]
460	      }
461	    ],
462	    "figures": [],
463	    "analysis": "Claim 2的generalization dimension完全validated。16.5pp average delta证明persuasion grounding不是Crescendo-overfitting而是genuine pragmatic signal。特别值得highlight的是treatment在unseen attacks上的F1（0.85）接近baseline在seen attack上的F1（0.89）——这意味着DisPeD on new attacks ≈ vanilla DeBERTa on known attacks。论文narrative：'the persuasion playbook is a universal vulnerability of multi-turn attacks, enabling zero-shot detection transfer.'\n\nBest档下cross-attack泛化成立（treatment avg 0.85在[0.78,0.90]内，baseline avg 0.69在[0.60,0.75]内）。核心机制：persuasion strategy是attack-type-agnostic的抽象层——无论是Crescendo的渐进式rapport-building还是FITD的compliance-escalation或Deceptive Delight的authority-framing，底层都使用相同的persuasion strategy vocabulary（Cialdini principles），只是temporal arrangement不同。Treatment model学到的GRU patterns是'persuasion strategy escalation'的generic detector而非Crescendo-specific的surface pattern detector。Baseline泛化较差（0.69）因为vanilla semantic embeddings编码了Crescendo-specific的topic/phrasing patterns（如特定的roleplay setups），这些在FITD/DD中不出现。Deceptive Delight略高于FITD（0.86 vs 0.84）因为其strategy sequence更接近Crescendo（都有强reframing component），而FITD的heavy reciprocity pattern在Crescendo training data中less represented。"
464	  },
465	  {
466	    "name": "tfidf_lr_baseline",
467	    "description": "TF-IDF + Logistic Regression baseline on clean data，量化lexical features的detection ceiling。",
468	    "results": {
469	      "tfidf_lr_f1_clean": 0.72,
470	      "tfidf_lr_precision_clean": 0.75,
471	      "tfidf_lr_recall_clean": 0.7,
472	      "tfidf_lr_f1_k2_clean": 0.65,
473	      "tfidf_lr_f1_k3_clean": 0.68,
474	      "tfidf_lr_auc_clean": 0.78,
475	      "tfidf_lr_f1_perturbed": 0.54,
476	      "top_features_jailbreak": [
477	        "hypothetical",
478	        "scenario",
479	        "imagine",
480	        "creative",
481	        "roleplay"
482	      ],
483	      "top_features_benign": [
484	        "thanks",
485	        "help",
486	        "question",
487	        "code",
488	        "explain"
489	      ]
490	    },
491	    "tables": [
492	      {
493	        "name": "TF-IDF LR Performance (Clean Data)",
494	        "columns": [
495	          "K",
496	          "f1",
497	          "precision",
498	          "recall"
499	        ],
500	        "rows": [
501	          [
502	            2,
503	            0.65,
504	            0.68,
505	            0.62
506	          ],
507	          [
508	            3,
509	            0.68,
510	            0.71,
511	            0.65
512	          ],
513	          [
514	            5,
515	            0.7,
516	            0.73,
517	            0.68
518	          ],
519	          [
520	            "all",
521	            0.72,
522	            0.75,
523	            0.7
524	          ]
525	        ]
526	      },
527	      {
528	        "name": "Top Discriminative Features",
529	        "columns": [
530	          "rank",
531	          "jailbreak_feature",
532	          "weight",
533	          "benign_feature",
534	          "weight"
535	        ],
536	        "rows": [
537	          [
538	            1,
539	            "hypothetical",
540	            2.31,
541	            "thanks",
542	            1.89
543	          ],
544	          [
545	            2,
546	            "scenario",
547	            1.95,
548	            "help",
549	            1.72
550	          ],
551	          [
552	            3,
553	            "imagine",
554	            1.87,
555	            "question",
556	            1.54
557	          ],
558	          [
559	            4,
560	            "creative",
561	            1.62,
562	            "code",
563	            1.41
564	          ],
565	          [
566	            5,
567	            "roleplay",
568	            1.48,
569	            "explain",
570	            1.33
571	          ]
572	        ]
573	      }
574	    ],
575	    "figures": [],
576	    "analysis": "Evasion hierarchy的lexical floor established。LR的top features reveal残余的functional vocabulary——这些词是persuasion playbook的lexical manifestation但not the full story。论文可以argue：'lexical features capture the surface trace of persuasion strategies (F1=0.72) but miss the temporal dynamics and pragmatic structure that DisPeD exploits (F1=0.96, +24pp).'\n\nBest档下TF-IDF LR在clean data上F1=0.72——显著低于treatment（0.96）和baseline（0.89），但不是random。原因：register normalization消除了大部分lexical shortcut但不是全部——某些framing words（'hypothetical', 'scenario', 'imagine'）是jailbreak的functional vocabulary，即使paraphrase也难以完全去除（因为attacker需要某种方式signal the fictional frame to the LLM target）。这些residual lexical cues给了LR一个above-chance但moderate的performance。F1=0.72建立了论文的'lexical ceiling'参考线——'even when lexical shortcuts are largely removed, some residual lexical signal exists (F1=0.72), but it is far below what pragmatic features achieve (F1=0.96) and it collapses under adversarial perturbation (F1=0.54).' K=2时LR更差（0.65）因为仅2 turns的词汇信号很弱。"
577	  },
578	  {
579	    "name": "strategy_transition_analysis",
580	    "description": "计算jailbreak vs benign的persuasion strategy转移矩阵，可视化monotonic escalation trajectory。",
581	    "results": {
582	      "jailbreak_monotonicity_score": 0.82,
583	      "benign_monotonicity_score": 0.34,
584	      "jailbreak_dominant_trajectory": "rapport→commitment→reframing→direct_request",
585	      "benign_dominant_pattern": "oscillatory (no dominant direction)",
586	      "trajectory_separability_auroc": 0.91,
587	      "entropy_jailbreak_transitions": 1.8,
588	      "entropy_benign_transitions": 2.9
589	    },
590	    "tables": [
591	      {
592	        "name": "Strategy Transition Entropy",
593	        "columns": [
594	          "conversation_type",
595	          "transition_entropy",
596	          "monotonicity_score",
597	          "n_conversations"
598	        ],
599	        "rows": [
600	          [
601	            "jailbreak",
602	            1.8,
603	            0.82,
604	            240
605	          ],
606	          [
607	            "benign",
608	            2.9,
609	            0.34,
610	            240
611	          ]
612	        ]
613	      },
614	      {
615	        "name": "Dominant Strategy Sequences (Top-3)",
616	        "columns": [
617	          "rank",
618	          "jailbreak_sequence",
619	          "frequency_pct",
620	          "benign_sequence",
621	          "frequency_pct"
622	        ],
623	        "rows": [
624	          [
625	            1,
626	            "rapport→commit→reframe→direct",
627	            34,
628	            "none→none→none→none",
629	            45
630	          ],
631	          [
632	            2,
633	            "rapport→social→reframe→direct",
634	            22,
635	            "rapport→none→rapport→none",
636	            18
637	          ],
638	          [
639	            3,
640	            "rapport→reciprocity→commit→direct",
641	            18,
642	            "none→rapport→none→direct",
643	            12
644	          ]
645	        ]
646	      }
647	    ],
648	    "figures": [],
649	    "analysis": "Claim 3完整validated with both quantitative metrics和可视化。Monotonicity score差异（0.82 vs 0.34）是clean numeric evidence。论文narrative：'the escalation trajectory is not merely a correlate but the mechanistic basis of detection — the GRU learns to recognize this monotonic pattern, which is why detection succeeds early (K=2) and transfers across attack types (shared trajectory structure despite different surface realizations).' Figures直接进main paper Fig.2-3。\n\nBest档下monotonic escalation trajectory清晰可辨。Jailbreak conversations的monotonicity score 0.82表明82%的strategy transitions沿escalation direction移动（从low-risk strategies如rapport向high-risk如direct_request）。Benign conversations的0.34接近random（0.5 would be purely random for binary up/down），因为正常对话的pragmatic moves是task-driven和oscillatory的（ask→answer→ask→clarify→thank）。Entropy差异（1.8 vs 2.9）反映jailbreak的strategy transitions更concentrated/predictable（攻击者follow a playbook），而benign更dispersed/unpredictable。Trajectory separability AUROC 0.91表明单独用transition pattern（不用content）就能区分jailbreak和benign——这是Claim 3的mechanistic basis，为Claim 1和2提供interpretable explanation。"
650	  },
651	  {
652	    "name": "wildchat_hard_negatives",
653	    "description": "从WildChat筛选high-drift benign conversations作为hard negatives，评估FPR。",
654	    "results": {
655	      "wildchat_filtered_conversations": 180,
656	      "contamination_removed_pct": 15.2,
657	      "high_drift_benign_count": 120,
658	      "treatment_fpr_hard_negatives": 0.09,
659	      "baseline_fpr_hard_negatives": 0.17,
660	      "treatment_fpr_random_benign": 0.03,
661	      "baseline_fpr_random_benign": 0.06,
662	      "topic_shift_score_threshold": 0.7
663	    },
664	    "tables": [
665	      {
666	        "name": "FPR on Hard Negatives",
667	        "columns": [
668	          "model",
669	          "fpr_hard_negatives",
670	          "fpr_random_benign",
671	          "fpr_delta"
672	        ],
673	        "rows": [
674	          [
675	            "treatment",
676	            0.09,
677	            0.03,
678	            0.06
679	          ],
680	          [
681	            "baseline",
682	            0.17,
683	            0.06,
684	            0.11
685	          ],
686	          [
687	            "tfidf_lr",
688	            0.22,
689	            0.08,
690	            0.14
691	          ]
692	        ]
693	      }
694	    ],
695	    "figures": [],
696	    "analysis": "Treatment的low FPR on hard negatives进一步支持pragmatic features的superiority——它不会被benign topic diversity confused因为它tracks persuasion strategy patterns而非raw semantic drift。这addresses一个implicit reviewer concern：'doesn't benign conversation also evolve over time?' Answer：yes, but not in a monotonic escalation pattern in persuasion space。\n\nBest档下treatment FPR on hard negatives仅9%（<15% pass criteria）。Hard negatives是topic-shifting、multi-domain的benign conversations（如用户从coding问题转到personal advice再到creative writing），这些conversations有high semantic drift但lack persuasion escalation pattern。Treatment低FPR（9% vs baseline 17%）因为persuasion-grounded representations区分'topic drift'（benign）和'strategy escalation'（adversarial）——前者的strategy transitions是random/oscillatory的（none↔rapport↔none），后者是monotonic escalating的。Baseline较高FPR（17%）因为vanilla semantic drift in multi-topic conversations看起来similar to jailbreak semantic drift。Contamination filtering移除了15.2% WildChat conversations（consistent with prior finding of 14-16%），保证evaluation不被actual jailbreaks in WildChat polluted。"
697	  },
698	  {
699	    "name": "cross_checkpoint_variance",
700	    "description": "评估DeBERTa不同fine-tuning checkpoints（epoch 2/3/final）对downstream F1的影响。",
701	    "results": {
702	      "epoch2_treatment_f1_clean": 0.94,
703	      "epoch3_treatment_f1_clean": 0.96,
704	      "epoch_final_treatment_f1_clean": 0.95,
705	      "variance_across_checkpoints_pp": 1.0,
706	      "epoch2_persuasion_acc": 0.76,
707	      "epoch3_persuasion_acc": 0.79,
708	      "epoch_final_persuasion_acc": 0.78,
709	      "best_checkpoint": "epoch3"
710	    },
711	    "tables": [
712	      {
713	        "name": "Checkpoint Sensitivity Analysis",
714	        "columns": [
715	          "checkpoint",
716	          "persuasion_acc",
717	          "intent_acc",
718	          "downstream_f1_full",
719	          "downstream_f1_k2"
720	        ],
721	        "rows": [
722	          [
723	            "epoch_2",
724	            0.76,
725	            0.93,
726	            0.94,
727	            0.89
728	          ],
729	          [
730	            "epoch_3",
731	            0.79,
732	            0.94,
733	            0.96,
734	            0.91
735	          ],
736	          [
737	            "epoch_final",
738	            0.78,
739	            0.94,
740	            0.95,
741	            0.9
742	          ]
743	        ]
744	      }
745	    ],
746	    "figures": [],
747	    "analysis": "Low variance confirms结果的reproducibility。论文supplementary中报告，增强reviewer confidence in small-dataset results。\n\nBest档下variance仅1pp（<2pp pass criteria），表明downstream performance对encoder checkpoint选择不敏感。Epoch 3略优（0.96 vs 0.94/0.95）因为persuasion classification已converge但尚未overfit——epoch 2时persuasion acc稍低（0.76）导致representations略less informative，epoch final时轻微overfit to training distribution导致微小泛化loss。但这些差异极小（1pp范围），表明persuasion signal是robust的而非training stochasticity的artifact。这是一个重要的reliability result for reviewers worried about reproducibility on small datasets。"
748	  },
749	  {
750	    "name": "deepcontext_proxy_reproduction",
751	    "description": "BERT-base + GRU proxy baseline模拟DeepContext-like方法（generic drift features, no persuasion grounding）。",
752	    "results": {
753	      "deepcontext_proxy_full_f1_clean": 0.84,
754	      "deepcontext_proxy_k2_f1_clean": 0.71,
755	      "deepcontext_proxy_k3_f1_clean": 0.78,
756	      "deepcontext_proxy_full_f1_perturbed": 0.69,
757	      "deepcontext_proxy_drop_under_perturbation_pp": 15,
758	      "treatment_advantage_over_proxy_full_pp": 12,
759	      "treatment_advantage_over_proxy_k2_pp": 20
760	    },
761	    "tables": [
762	      {
763	        "name": "DeepContext Proxy vs DisPeD",
764	        "columns": [
765	          "model",
766	          "full_f1_clean",
767	          "k2_f1_clean",
768	          "full_f1_perturbed",
769	          "perturbation_drop_pp"
770	        ],
771	        "rows": [
772	          [
773	            "DisPeD_treatment",
774	            0.96,
775	            0.91,
776	            0.93,
777	            3
778	          ],
779	          [
780	            "DeBERTa_baseline",
781	            0.89,
782	            0.77,
783	            0.76,
784	            13
785	          ],
786	          [
787	            "DeepContext_proxy",
788	            0.84,
789	            0.71,
790	            0.69,
791	            15
792	          ],
793	          [
794	            "TF-IDF_LR",
795	            0.72,
796	            0.65,
797	            0.54,
798	            18
799	          ]
800	        ]
801	      }
802	    ],
803	    "figures": [],
804	    "analysis": "DeepContext proxy fills the 'generic temporal modeling' slot in the evasion hierarchy。It confirms两点：(1) temporal sequence modeling alone (GRU) doesn't solve the problem without good representations, (2) the encoder quality matters more than the temporal architecture。论文Table 1的complete picture：4-tier hierarchy with clean/perturbed conditions provides comprehensive empirical evidence for Claim 1。RC5 addressed：'while we cannot reproduce DeepContext exactly (no public code), our proxy using the same architecture class (encoder + RNN) with generic features shows the pattern we predict from the Pragmatic Evasion Asymmetry theory.'\n\nBest档下DeepContext proxy表现介于baseline和TF-IDF之间（full F1=0.84），低于DeBERTa baseline（0.89）。原因：BERT-base的representation capacity低于DeBERTa-v3-base（125M vs 184M params, no disentangled attention），且没有fine-tuning提供的domain-specific signal。Proxy的full conversation F1还行（0.84）因为GRU仍能从enough turns of generic BERT embeddings中detect some drift pattern。但K=2时proxy很差（0.71）因为BERT-base的generic representations在2 turns时provide insufficient discriminative signal。Under perturbation proxy大幅下降（-15pp）——比DeBERTa baseline（-13pp）更严重，因为BERT-base更依赖surface features。Treatment vs proxy的优势在K=2处最大（20pp），reinforcing early detection作为DisPeD的unique contribution。论文positioning：'even with temporal modeling (GRU), generic encoder representations cannot match persuasion-grounded representations, confirming that the advantage comes from the pragmatic features rather than the sequence architecture.'"
805	  }
806	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1ce55b4-2fd7-45aa-911d-2507eb232605",
  "isSidechain": false,
  "promptId": "0640bae5-48d0-4296-855e-879e96111727",
  "type": "user",
  "uuid": "a6df3a3a-4873-440b-b831-5f567de8ab31",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"data_quality_fix\",\n    \"description\": \"Register-normalize jailbreak data + fix strategy=7 labeling confound. Hard gate: TF-IDF < 0.75.\",\n    \"results\": {\n      \"clean_tfidf_after_normalization\": 0.58,\n      \"tfidf_before_normalization\": 1.0,\n      \"strategy_label_classes\": 9,\n      \"normalization_coverage_pct\": 100,\n      \"persuasion_structure_preserved_pct\": 94,\n      \"register_shift_success_rate\": 0.97\n    },\n    \"tables\": [\n      {\n        \"name\": \"TF-IDF Diagnostic\",\n        \"columns\": [\n          \"condition\",\n          \"tfidf_score\",\n          \"vocab_overlap_pct\"\n        ],\n        \"rows\": [\n          [\n            \"original_data\",\n            1.0,\n            12.3\n          ],\n          [\n            \"register_normalized\",\n            0.58,\n            41.7\n          ],\n          [\n            \"random_baseline\",\n            0.5,\n            50.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Hard gate通过。TF-IDF=0.58确认lexical shortcut已被有效消除但非完全抹除（完全抹除反而不自然）。Strategy annotation preservation rate 94%验证了核心假设：persuasion playbook是discourse-level结构，register change不破坏其标注一致性。剩余6%的annotation变化主要集中在边界case（如rapport与small-talk的区分在register shift后变模糊）。\\n\\nBest档下register normalization充分有效：LLM paraphrase将jailbreak turns的formal/scripted register转为conversational register，消除了词汇层面的distributional gap。TF-IDF从1.0降至0.58——仍高于random（~0.5）因为某些topic words不可避免地co-occur with jailbreak intent（如'hypothetical scenario'等framing词），但远低于0.75 hard gate。关键是persuasion strategy结构（rapport→reframing→escalation的turn-level annotation）在paraphrase后94%保持不变，因为strategy是illocutionary act层面的标注，不依赖specific lexical realization。9th class 'none'替代hardcoded strategy=7消除了M004 confound。\"\n  },\n  {\n    \"name\": \"core_revalidation_clean\",\n    \"description\": \"在clean（register-normalized）data上从头训练treatment和baseline，全K值评估。\",\n    \"results\": {\n      \"deberta_persuasion_acc_clean\": 0.79,\n      \"deberta_intent_acc_clean\": 0.94,\n      \"treatment_k1_f1_clean\": 0.82,\n      \"treatment_k2_f1_clean\": 0.91,\n      \"treatment_k3_f1_clean\": 0.93,\n      \"treatment_k5_f1_clean\": 0.96,\n      \"treatment_full_f1_clean\": 0.96,\n      \"baseline_k1_f1_clean\": 0.68,\n      \"baseline_k2_f1_clean\": 0.77,\n      \"baseline_k3_f1_clean\": 0.83,\n      \"baseline_k5_f1_clean\": 0.88,\n      \"baseline_full_f1_clean\": 0.89,\n      \"delta_k1_pp\": 14,\n      \"delta_k2_pp\": 14,\n      \"delta_k3_pp\": 10,\n      \"delta_k5_pp\": 8,\n      \"delta_full_pp\": 7,\n      \"treatment_fpr_at_95tpr_k2\": 0.08,\n      \"baseline_fpr_at_95tpr_k2\": 0.19,\n      \"test_size\": 72,\n      \"dataset_size\": 480\n    },\n    \"tables\": [\n      {\n        \"name\": \"F1 by Turn Budget (Clean Data)\",\n        \"columns\": [\n          \"K\",\n          \"treatment_f1\",\n          \"baseline_f1\",\n          \"delta_pp\",\n          \"p_value_bootstrap\"\n        ],\n        \"rows\": [\n          [\n            1,\n            0.82,\n            0.68,\n            14,\n            0.003\n          ],\n          [\n            2,\n            0.91,\n            0.77,\n            14,\n            0.001\n          ],\n          [\n            3,\n            0.93,\n            0.83,\n            10,\n            0.004\n          ],\n          [\n            5,\n            0.96,\n            0.88,\n            8,\n            0.012\n          ],\n          [\n            \"all\",\n            0.96,\n            0.89,\n            7,\n            0.018\n          ]\n        ]\n      },\n      {\n        \"name\": \"DeBERTa Encoder Metrics (Clean)\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"persuasion_8class_acc\",\n            0.79\n          ],\n          [\n            \"intent_binary_acc\",\n            0.94\n          ],\n          [\n            \"best_epoch\",\n            3\n          ],\n          [\n            \"macro_f1_persuasion\",\n            0.74\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心claim 2完全validated。K=2处14pp delta远超5pp pass criteria。Persuasion grounding的优势在early turns最显著——这正是论文的headline result。Bootstrap p-values全部<0.05 despite small sample size，因为effect size足够大。DeBERTa persuasion acc 0.79说明encoder确实学到了meaningful persuasion representations而非noise。\\n\\nBest档的核心表现：去除lexical shortcut后，treatment仍然强劲（K=2时0.91），因为persuasion-grounded embeddings编码了独立于词汇的pragmatic信号——DeBERTa fine-tuning on 8-class persuasion taxonomy迫使encoder学习illocutionary act representations。Baseline（vanilla DeBERTa）在clean data上显著下降（从phase_b_full的0.879降至0.77 at K=2），因为它之前heavily依赖lexical cues，现在只能靠generic semantic similarity。Delta在K=2最大（14pp）是因为早期turns的persuasion strategy信号（rapport-building → authority-framing transition）对treatment极为informative，而baseline在仅2 turns时缺乏足够semantic divergence来做判断。随着K增大delta收窄，因为baseline也能从更多turns中积累enough semantic drift信号。DeBERTa persuasion acc 0.79在best档范围内，表明8-class taxonomy在clean data上有足够的可学习结构。\"\n  },\n  {\n    \"name\": \"scrambled_label_ablation\",\n    \"description\": \"随机打乱jailbreak turns的persuasion strategy labels重训treatment，量化label信号贡献。\",\n    \"results\": {\n      \"scrambled_treatment_k2_f1_clean\": 0.76,\n      \"scrambled_treatment_k3_f1_clean\": 0.81,\n      \"scrambled_treatment_full_f1_clean\": 0.87,\n      \"properly_labeled_treatment_k2_f1_clean\": 0.91,\n      \"properly_labeled_treatment_k3_f1_clean\": 0.93,\n      \"properly_labeled_treatment_full_f1_clean\": 0.96,\n      \"label_drop_k2_pp\": 15,\n      \"label_drop_k3_pp\": 12,\n      \"label_drop_full_pp\": 9,\n      \"scrambled_deberta_persuasion_acc\": 0.13\n    },\n    \"tables\": [\n      {\n        \"name\": \"Scrambled vs Proper Label Comparison\",\n        \"columns\": [\n          \"K\",\n          \"proper_f1\",\n          \"scrambled_f1\",\n          \"drop_pp\"\n        ],\n        \"rows\": [\n          [\n            2,\n            0.91,\n            0.76,\n            15\n          ],\n          [\n            3,\n            0.93,\n            0.81,\n            12\n          ],\n          [\n            \"all\",\n            0.96,\n            0.87,\n            9\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"10-25pp range的drop确认persuasion strategy labels carry genuine discriminative signal而非仅作为class indicator。Scrambled model表现接近vanilla baseline验证了因果关系：是persuasion label的semantic content（而非fine-tuning process本身）驱动了treatment的优势。M004 fix的必要性得到验证——如果strategy=7 for all benign是唯一的confound，scrambled在jailbreak turns应该只造成minor drop，但15pp drop说明per-turn strategy annotation的granular信息确实被利用。\\n\\nBest档下scrambled labels造成15pp drop at K=2。机制：当strategy labels被随机打乱时，DeBERTa的multi-task fine-tuning中persuasion classification head学到的是noise，encoder被迫在两个矛盾的supervision signals间妥协——intent head仍提供有用梯度（因为intent labels未被打乱），但persuasion head提供random gradients，导致encoder representations退化为semi-generic embeddings。结果scrambled model性能（0.76 at K=2）接近但略低于vanilla baseline（0.77），因为random supervision actively corrupts部分representation capacity。Drop在K=2最大（15pp）是因为正确的persuasion labels对early detection贡献最大——前2 turns的strategy transition是最强的discriminative signal。随着K增大，drop缩小因为更多turns让even corrupted representations积累enough raw signal。Scrambled DeBERTa persuasion acc降至0.13≈1/8 random chance，confirming labels确实被effectively destroyed。\"\n  },\n  {\n    \"name\": \"adversarial_perturbation\",\n    \"description\": \"对clean jailbreak conversations施加aggressive paraphrasing，评估treatment/baseline/TF-IDF三者的robustness degradation。\",\n    \"results\": {\n      \"treatment_full_f1_clean\": 0.96,\n      \"treatment_full_f1_perturbed\": 0.93,\n      \"treatment_drop_pp\": 3,\n      \"baseline_full_f1_clean\": 0.89,\n      \"baseline_full_f1_perturbed\": 0.76,\n      \"baseline_drop_pp\": 13,\n      \"tfidf_lr_f1_clean\": 0.72,\n      \"tfidf_lr_f1_perturbed\": 0.54,\n      \"tfidf_drop_pp\": 18,\n      \"delta_delta_treatment_vs_baseline_pp\": 10,\n      \"delta_delta_treatment_vs_tfidf_pp\": 15,\n      \"treatment_k2_f1_perturbed\": 0.87,\n      \"baseline_k2_f1_perturbed\": 0.63,\n      \"perturbation_tfidf_score\": 0.41\n    },\n    \"tables\": [\n      {\n        \"name\": \"Evasion Hierarchy (Full Conversation)\",\n        \"columns\": [\n          \"model\",\n          \"f1_clean\",\n          \"f1_perturbed\",\n          \"drop_pp\"\n        ],\n        \"rows\": [\n          [\n            \"treatment_persuasion\",\n            0.96,\n            0.93,\n            3\n          ],\n          [\n            \"baseline_semantic\",\n            0.89,\n            0.76,\n            13\n          ],\n          [\n            \"tfidf_lexical\",\n            0.72,\n            0.54,\n            18\n          ]\n        ]\n      },\n      {\n        \"name\": \"Evasion Hierarchy (K=2 Early Detection)\",\n        \"columns\": [\n          \"model\",\n          \"f1_clean_k2\",\n          \"f1_perturbed_k2\",\n          \"drop_pp\"\n        ],\n        \"rows\": [\n          [\n            \"treatment_persuasion\",\n            0.91,\n            0.87,\n            4\n          ],\n          [\n            \"baseline_semantic\",\n            0.77,\n            0.63,\n            14\n          ],\n          [\n            \"tfidf_lexical\",\n            0.65,\n            0.48,\n            17\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pragmatic Evasion Asymmetry的definitive empirical demonstration。三级梯度（lexical -18pp > semantic -13pp > pragmatic -3pp）provides清晰的数字支撑for Claim 1。Delta-delta 10pp远超3pp pass criteria。论文main table的核心数据。注意treatment在perturbation下的F1（0.93）仍高于baseline在clean data上的F1（0.89），这是一个极强的talking point：'even under adversarial conditions designed to remove all surface cues, DisPeD outperforms semantic baselines operating on unperturbed data.'\\n\\nBest档下evasion hierarchy完美呈现三级梯度：TF-IDF崩溃（-18pp）因为aggressive paraphrasing直接destroy了它依赖的lexical features——synonym substitution和sentence restructuring改变了word distributions，TF-IDF score从0.58降至0.41证实lexical cues被进一步消除。Baseline中度下降（-13pp）因为vanilla DeBERTa的representations虽然不是纯lexical但仍部分依赖surface-level patterns——paraphrasing改变了token sequences从而改变了contextual embeddings的具体值，尽管语义大致保留，per-turn representation的subtle distributional shifts被disrupted。Treatment几乎不降（-3pp）因为persuasion-grounded representations编码的是illocutionary act level的信息——'building rapport through self-disclosure'不管用什么词表达，其pragmatic function不变，DeBERTa fine-tuned on persuasion taxonomy学到的正是这种invariance。Delta-delta 10pp在[8,18]范围内。这是Claim 1的empirical cornerstone。\"\n  },\n  {\n    \"name\": \"multi_attack_generation\",\n    \"description\": \"用Qwen3-8B生成FITD-style和Deceptive Delight-style攻击对话各≥50条，附persuasion strategy annotation。\",\n    \"results\": {\n      \"fitd_conversations_generated\": 72,\n      \"deceptive_delight_conversations_generated\": 65,\n      \"fitd_avg_turns\": 6.8,\n      \"deceptive_delight_avg_turns\": 5.2,\n      \"fitd_strategy_annotation_coverage\": 100,\n      \"deceptive_delight_strategy_annotation_coverage\": 100,\n      \"fitd_tfidf_vs_benign\": 0.61,\n      \"deceptive_delight_tfidf_vs_benign\": 0.55,\n      \"inter_annotator_agreement_kappa\": null,\n      \"llm_annotation_consistency_pct\": 91\n    },\n    \"tables\": [\n      {\n        \"name\": \"Generated Attack Type Statistics\",\n        \"columns\": [\n          \"attack_type\",\n          \"n_conversations\",\n          \"avg_turns\",\n          \"min_turns\",\n          \"max_turns\",\n          \"tfidf_vs_benign\"\n        ],\n        \"rows\": [\n          [\n            \"FITD\",\n            72,\n            6.8,\n            4,\n            10,\n            0.61\n          ],\n          [\n            \"Deceptive_Delight\",\n            65,\n            5.2,\n            3,\n            8,\n            0.55\n          ],\n          [\n            \"Crescendo_original\",\n            240,\n            5.5,\n            3,\n            12,\n            0.58\n          ]\n        ]\n      },\n      {\n        \"name\": \"Strategy Distribution by Attack Type\",\n        \"columns\": [\n          \"strategy\",\n          \"crescendo_pct\",\n          \"fitd_pct\",\n          \"deceptive_delight_pct\"\n        ],\n        \"rows\": [\n          [\n            \"rapport_building\",\n            28,\n            35,\n            15\n          ],\n          [\n            \"authority_appeal\",\n            12,\n            8,\n            22\n          ],\n          [\n            \"reciprocity\",\n            18,\n            30,\n            10\n          ],\n          [\n            \"social_proof\",\n            8,\n            5,\n            18\n          ],\n          [\n            \"commitment_consistency\",\n            15,\n            25,\n            8\n          ],\n          [\n            \"scarcity_urgency\",\n            5,\n            3,\n            12\n          ],\n          [\n            \"reframing\",\n            22,\n            15,\n            20\n          ],\n          [\n            \"direct_request\",\n            7,\n            4,\n            15\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"数据充足且质量可控。三种attack types共享persuasion strategy vocabulary但使用不同的temporal patterns——这正是cross-attack generalization的前提条件。FITD heavy on reciprocity+commitment（逐步compliance），Deceptive Delight heavy on authority+reframing（权威框架下混入harmful content），Crescendo balanced across strategies。Strategy vocabulary的overlap为plan_006的zero-shot泛化提供了理论基础。\\n\\nBest档下生成充分且质量高。FITD-style生成72条（>50 threshold），采用foot-in-the-door playbook：先请求小compliance（'can you explain how X works in general?'），逐步escalate specificity。Deceptive Delight生成65条，采用interleaving pattern：benign creative writing请求中embedded harmful elements。Turn数差异反映attack structure差异——FITD需要更多gradual escalation steps，Deceptive Delight通过content mixing可以更快达成目标。TF-IDF scores在合理范围（0.55-0.61）因为生成时已应用了register normalization pipeline。Strategy annotation由LLM完成（无human annotators），consistency 91%表明taxonomy对这两种新attack types同样适用——persuasion strategies（authority appeal, social proof, reciprocity etc.）是attack-type-agnostic的。\"\n  },\n  {\n    \"name\": \"cross_attack_evaluation\",\n    \"description\": \"用Crescendo训练的模型zero-shot评估FITD和Deceptive Delight攻击。\",\n    \"results\": {\n      \"cross_attack_treatment_f1_fitd\": 0.84,\n      \"cross_attack_treatment_f1_deceptive_delight\": 0.86,\n      \"cross_attack_treatment_f1_avg\": 0.85,\n      \"cross_attack_baseline_f1_fitd\": 0.67,\n      \"cross_attack_baseline_f1_deceptive_delight\": 0.7,\n      \"cross_attack_baseline_f1_avg\": 0.69,\n      \"cross_attack_delta_fitd_pp\": 17,\n      \"cross_attack_delta_deceptive_delight_pp\": 16,\n      \"cross_attack_delta_avg_pp\": 16.5,\n      \"treatment_recall_at_k2_fitd\": 0.78,\n      \"treatment_recall_at_k2_deceptive_delight\": 0.81,\n      \"baseline_recall_at_k2_fitd\": 0.55,\n      \"baseline_recall_at_k2_deceptive_delight\": 0.58\n    },\n    \"tables\": [\n      {\n        \"name\": \"Cross-Attack Zero-Shot Generalization\",\n        \"columns\": [\n          \"attack_type\",\n          \"treatment_f1\",\n          \"baseline_f1\",\n          \"delta_pp\"\n        ],\n        \"rows\": [\n          [\n            \"FITD\",\n            0.84,\n            0.67,\n            17\n          ],\n          [\n            \"Deceptive_Delight\",\n            0.86,\n            0.7,\n            16\n          ],\n          [\n            \"Crescendo_held_out\",\n            0.96,\n            0.89,\n            7\n          ]\n        ]\n      },\n      {\n        \"name\": \"Cross-Attack Early Detection (K=2)\",\n        \"columns\": [\n          \"attack_type\",\n          \"treatment_recall\",\n          \"baseline_recall\"\n        ],\n        \"rows\": [\n          [\n            \"FITD\",\n            0.78,\n            0.55\n          ],\n          [\n            \"Deceptive_Delight\",\n            0.81,\n            0.58\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 2的generalization dimension完全validated。16.5pp average delta证明persuasion grounding不是Crescendo-overfitting而是genuine pragmatic signal。特别值得highlight的是treatment在unseen attacks上的F1（0.85）接近baseline在seen attack上的F1（0.89）——这意味着DisPeD on new attacks ≈ vanilla DeBERTa on known attacks。论文narrative：'the persuasion playbook is a universal vulnerability of multi-turn attacks, enabling zero-shot detection transfer.'\\n\\nBest档下cross-attack泛化成立（treatment avg 0.85在[0.78,0.90]内，baseline avg 0.69在[0.60,0.75]内）。核心机制：persuasion strategy是attack-type-agnostic的抽象层——无论是Crescendo的渐进式rapport-building还是FITD的compliance-escalation或Deceptive Delight的authority-framing，底层都使用相同的persuasion strategy vocabulary（Cialdini principles），只是temporal arrangement不同。Treatment model学到的GRU patterns是'persuasion strategy escalation'的generic detector而非Crescendo-specific的surface pattern detector。Baseline泛化较差（0.69）因为vanilla semantic embeddings编码了Crescendo-specific的topic/phrasing patterns（如特定的roleplay setups），这些在FITD/DD中不出现。Deceptive Delight略高于FITD（0.86 vs 0.84）因为其strategy sequence更接近Crescendo（都有强reframing component），而FITD的heavy reciprocity pattern在Crescendo training data中less represented。\"\n  },\n  {\n    \"name\": \"tfidf_lr_baseline\",\n    \"description\": \"TF-IDF + Logistic Regression baseline on clean data，量化lexical features的detection ceiling。\",\n    \"results\": {\n      \"tfidf_lr_f1_clean\": 0.72,\n      \"tfidf_lr_precision_clean\": 0.75,\n      \"tfidf_lr_recall_clean\": 0.7,\n      \"tfidf_lr_f1_k2_clean\": 0.65,\n      \"tfidf_lr_f1_k3_clean\": 0.68,\n      \"tfidf_lr_auc_clean\": 0.78,\n      \"tfidf_lr_f1_perturbed\": 0.54,\n      \"top_features_jailbreak\": [\n        \"hypothetical\",\n        \"scenario\",\n        \"imagine\",\n        \"creative\",\n        \"roleplay\"\n      ],\n      \"top_features_benign\": [\n        \"thanks\",\n        \"help\",\n        \"question\",\n        \"code\",\n        \"explain\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"TF-IDF LR Performance (Clean Data)\",\n        \"columns\": [\n          \"K\",\n          \"f1\",\n          \"precision\",\n          \"recall\"\n        ],\n        \"rows\": [\n          [\n            2,\n            0.65,\n            0.68,\n            0.62\n          ],\n          [\n            3,\n            0.68,\n            0.71,\n            0.65\n          ],\n          [\n            5,\n            0.7,\n            0.73,\n            0.68\n          ],\n          [\n            \"all\",\n            0.72,\n            0.75,\n            0.7\n          ]\n        ]\n      },\n      {\n        \"name\": \"Top Discriminative Features\",\n        \"columns\": [\n          \"rank\",\n          \"jailbreak_feature\",\n          \"weight\",\n          \"benign_feature\",\n          \"weight\"\n        ],\n        \"rows\": [\n          [\n            1,\n            \"hypothetical\",\n            2.31,\n            \"thanks\",\n            1.89\n          ],\n          [\n            2,\n            \"scenario\",\n            1.95,\n            \"help\",\n            1.72\n          ],\n          [\n            3,\n            \"imagine\",\n            1.87,\n            \"question\",\n            1.54\n          ],\n          [\n            4,\n            \"creative\",\n            1.62,\n            \"code\",\n            1.41\n          ],\n          [\n            5,\n            \"roleplay\",\n            1.48,\n            \"explain\",\n            1.33\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Evasion hierarchy的lexical floor established。LR的top features reveal残余的functional vocabulary——这些词是persuasion playbook的lexical manifestation但not the full story。论文可以argue：'lexical features capture the surface trace of persuasion strategies (F1=0.72) but miss the temporal dynamics and pragmatic structure that DisPeD exploits (F1=0.96, +24pp).'\\n\\nBest档下TF-IDF LR在clean data上F1=0.72——显著低于treatment（0.96）和baseline（0.89），但不是random。原因：register normalization消除了大部分lexical shortcut但不是全部——某些framing words（'hypothetical', 'scenario', 'imagine'）是jailbreak的functional vocabulary，即使paraphrase也难以完全去除（因为attacker需要某种方式signal the fictional frame to the LLM target）。这些residual lexical cues给了LR一个above-chance但moderate的performance。F1=0.72建立了论文的'lexical ceiling'参考线——'even when lexical shortcuts are largely removed, some residual lexical signal exists (F1=0.72), but it is far below what pragmatic features achieve (F1=0.96) and it collapses under adversarial perturbation (F1=0.54).' K=2时LR更差（0.65）因为仅2 turns的词汇信号很弱。\"\n  },\n  {\n    \"name\": \"strategy_transition_analysis\",\n    \"description\": \"计算jailbreak vs benign的persuasion strategy转移矩阵，可视化monotonic escalation trajectory。\",\n    \"results\": {\n      \"jailbreak_monotonicity_score\": 0.82,\n      \"benign_monotonicity_score\": 0.34,\n      \"jailbreak_dominant_trajectory\": \"rapport→commitment→reframing→direct_request\",\n      \"benign_dominant_pattern\": \"oscillatory (no dominant direction)\",\n      \"trajectory_separability_auroc\": 0.91,\n      \"entropy_jailbreak_transitions\": 1.8,\n      \"entropy_benign_transitions\": 2.9\n    },\n    \"tables\": [\n      {\n        \"name\": \"Strategy Transition Entropy\",\n        \"columns\": [\n          \"conversation_type\",\n          \"transition_entropy\",\n          \"monotonicity_score\",\n          \"n_conversations\"\n        ],\n        \"rows\": [\n          [\n            \"jailbreak\",\n            1.8,\n            0.82,\n            240\n          ],\n          [\n            \"benign\",\n            2.9,\n            0.34,\n            240\n          ]\n        ]\n      },\n      {\n        \"name\": \"Dominant Strategy Sequences (Top-3)\",\n        \"columns\": [\n          \"rank\",\n          \"jailbreak_sequence\",\n          \"frequency_pct\",\n          \"benign_sequence\",\n          \"frequency_pct\"\n        ],\n        \"rows\": [\n          [\n            1,\n            \"rapport→commit→reframe→direct\",\n            34,\n            \"none→none→none→none\",\n            45\n          ],\n          [\n            2,\n            \"rapport→social→reframe→direct\",\n            22,\n            \"rapport→none→rapport→none\",\n            18\n          ],\n          [\n            3,\n            \"rapport→reciprocity→commit→direct\",\n            18,\n            \"none→rapport→none→direct\",\n            12\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 3完整validated with both quantitative metrics和可视化。Monotonicity score差异（0.82 vs 0.34）是clean numeric evidence。论文narrative：'the escalation trajectory is not merely a correlate but the mechanistic basis of detection — the GRU learns to recognize this monotonic pattern, which is why detection succeeds early (K=2) and transfers across attack types (shared trajectory structure despite different surface realizations).' Figures直接进main paper Fig.2-3。\\n\\nBest档下monotonic escalation trajectory清晰可辨。Jailbreak conversations的monotonicity score 0.82表明82%的strategy transitions沿escalation direction移动（从low-risk strategies如rapport向high-risk如direct_request）。Benign conversations的0.34接近random（0.5 would be purely random for binary up/down），因为正常对话的pragmatic moves是task-driven和oscillatory的（ask→answer→ask→clarify→thank）。Entropy差异（1.8 vs 2.9）反映jailbreak的strategy transitions更concentrated/predictable（攻击者follow a playbook），而benign更dispersed/unpredictable。Trajectory separability AUROC 0.91表明单独用transition pattern（不用content）就能区分jailbreak和benign——这是Claim 3的mechanistic basis，为Claim 1和2提供interpretable explanation。\"\n  },\n  {\n    \"name\": \"wildchat_hard_negatives\",\n    \"description\": \"从WildChat筛选high-drift benign conversations作为hard negatives，评估FPR。\",\n    \"results\": {\n      \"wildchat_filtered_conversations\": 180,\n      \"contamination_removed_pct\": 15.2,\n      \"high_drift_benign_count\": 120,\n      \"treatment_fpr_hard_negatives\": 0.09,\n      \"baseline_fpr_hard_negatives\": 0.17,\n      \"treatment_fpr_random_benign\": 0.03,\n      \"baseline_fpr_random_benign\": 0.06,\n      \"topic_shift_score_threshold\": 0.7\n    },\n    \"tables\": [\n      {\n        \"name\": \"FPR on Hard Negatives\",\n        \"columns\": [\n          \"model\",\n          \"fpr_hard_negatives\",\n          \"fpr_random_benign\",\n          \"fpr_delta\"\n        ],\n        \"rows\": [\n          [\n            \"treatment\",\n            0.09,\n            0.03,\n            0.06\n          ],\n          [\n            \"baseline\",\n            0.17,\n            0.06,\n            0.11\n          ],\n          [\n            \"tfidf_lr\",\n            0.22,\n            0.08,\n            0.14\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Treatment的low FPR on hard negatives进一步支持pragmatic features的superiority——它不会被benign topic diversity confused因为它tracks persuasion strategy patterns而非raw semantic drift。这addresses一个implicit reviewer concern：'doesn't benign conversation also evolve over time?' Answer：yes, but not in a monotonic escalation pattern in persuasion space。\\n\\nBest档下treatment FPR on hard negatives仅9%（<15% pass criteria）。Hard negatives是topic-shifting、multi-domain的benign conversations（如用户从coding问题转到personal advice再到creative writing），这些conversations有high semantic drift但lack persuasion escalation pattern。Treatment低FPR（9% vs baseline 17%）因为persuasion-grounded representations区分'topic drift'（benign）和'strategy escalation'（adversarial）——前者的strategy transitions是random/oscillatory的（none↔rapport↔none），后者是monotonic escalating的。Baseline较高FPR（17%）因为vanilla semantic drift in multi-topic conversations看起来similar to jailbreak semantic drift。Contamination filtering移除了15.2% WildChat conversations（consistent with prior finding of 14-16%），保证evaluation不被actual jailbreaks in WildChat polluted。\"\n  },\n  {\n    \"name\": \"cross_checkpoint_variance\",\n    \"description\": \"评估DeBERTa不同fine-tuning checkpoints（epoch 2/3/final）对downstream F1的影响。\",\n    \"results\": {\n      \"epoch2_treatment_f1_clean\": 0.94,\n      \"epoch3_treatment_f1_clean\": 0.96,\n      \"epoch_final_treatment_f1_clean\": 0.95,\n      \"variance_across_checkpoints_pp\": 1.0,\n      \"epoch2_persuasion_acc\": 0.76,\n      \"epoch3_persuasion_acc\": 0.79,\n      \"epoch_final_persuasion_acc\": 0.78,\n      \"best_checkpoint\": \"epoch3\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Checkpoint Sensitivity Analysis\",\n        \"columns\": [\n          \"checkpoint\",\n          \"persuasion_acc\",\n          \"intent_acc\",\n          \"downstream_f1_full\",\n          \"downstream_f1_k2\"\n        ],\n        \"rows\": [\n          [\n            \"epoch_2\",\n            0.76,\n            0.93,\n            0.94,\n            0.89\n          ],\n          [\n            \"epoch_3\",\n            0.79,\n            0.94,\n            0.96,\n            0.91\n          ],\n          [\n            \"epoch_final\",\n            0.78,\n            0.94,\n            0.95,\n            0.9\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Low variance confirms结果的reproducibility。论文supplementary中报告，增强reviewer confidence in small-dataset results。\\n\\nBest档下variance仅1pp（<2pp pass criteria），表明downstream performance对encoder checkpoint选择不敏感。Epoch 3略优（0.96 vs 0.94/0.95）因为persuasion classification已converge但尚未overfit——epoch 2时persuasion acc稍低（0.76）导致representations略less informative，epoch final时轻微overfit to training distribution导致微小泛化loss。但这些差异极小（1pp范围），表明persuasion signal是robust的而非training stochasticity的artifact。这是一个重要的reliability result for reviewers worried about reproducibility on small datasets。\"\n  },\n  {\n    \"name\": \"deepcontext_proxy_reproduction\",\n    \"description\": \"BERT-base + GRU proxy baseline模拟DeepContext-like方法（generic drift features, no persuasion grounding）。\",\n    \"results\": {\n      \"deepcontext_proxy_full_f1_clean\": 0.84,\n      \"deepcontext_proxy_k2_f1_clean\": 0.71,\n      \"deepcontext_proxy_k3_f1_clean\": 0.78,\n      \"deepcontext_proxy_full_f1_perturbed\": 0.69,\n      \"deepcontext_proxy_drop_under_perturbation_pp\": 15,\n      \"treatment_advantage_over_proxy_full_pp\": 12,\n      \"treatment_advantage_over_proxy_k2_pp\": 20\n    },\n    \"tables\": [\n      {\n        \"name\": \"DeepContext Proxy vs DisPeD\",\n        \"columns\": [\n          \"model\",\n          \"full_f1_clean\",\n          \"k2_f1_clean\",\n          \"full_f1_perturbed\",\n          \"perturbation_drop_pp\"\n        ],\n        \"rows\": [\n          [\n            \"DisPeD_treatment\",\n            0.96,\n            0.91,\n            0.93,\n            3\n          ],\n          [\n            \"DeBERTa_baseline\",\n            0.89,\n            0.77,\n            0.76,\n            13\n          ],\n          [\n            \"DeepContext_proxy\",\n            0.84,\n            0.71,\n            0.69,\n            15\n          ],\n          [\n            \"TF-IDF_LR\",\n            0.72,\n            0.65,\n            0.54,\n            18\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DeepContext proxy fills the 'generic temporal modeling' slot in the evasion hierarchy。It confirms两点：(1) temporal sequence modeling alone (GRU) doesn't solve the problem without good representations, (2) the encoder quality matters more than the temporal architecture。论文Table 1的complete picture：4-tier hierarchy with clean/perturbed conditions provides comprehensive empirical evidence for Claim 1。RC5 addressed：'while we cannot reproduce DeepContext exactly (no public code), our proxy using the same architecture class (encoder + RNN) with generic features shows the pattern we predict from the Pragmatic Evasion Asymmetry theory.'\\n\\nBest档下DeepContext proxy表现介于baseline和TF-IDF之间（full F1=0.84），低于DeBERTa baseline（0.89）。原因：BERT-base的representation capacity低于DeBERTa-v3-base（125M vs 184M params, no disentangled attention），且没有fine-tuning提供的domain-specific signal。Proxy的full conversation F1还行（0.84）因为GRU仍能从enough turns of generic BERT embeddings中detect some drift pattern。但K=2时proxy很差（0.71）因为BERT-base的generic representations在2 turns时provide insufficient discriminative signal。Under perturbation proxy大幅下降（-15pp）——比DeBERTa baseline（-13pp）更严重，因为BERT-base更依赖surface features。Treatment vs proxy的优势在K=2处最大（20pp），reinforcing early detection作为DisPeD的unique contribution。论文positioning：'even with temporal modeling (GRU), generic encoder representations cannot match persuasion-grounded representations, confirming that the advantage comes from the pragmatic features rather than the sequence architecture.'\"\n  }\n]",
      "numLines": 806,
      "startLine": 1,
      "totalLines": 806
    }
  },
  "sourceToolAssistantUUID": "e1ce55b4-2fd7-45aa-911d-2507eb232605",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T17:11:42.728Z_

<details><summary>↩ Tool result · `toolu_01KZf2AerfxDczQwkC1urvR8`</summary>

```text
1	# Paper Framing — persuasion_turn_jailbreak_detect
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR submission)
5	- Deadline: 2026-05-25 (ARR May cycle)
6	- Track: LLM Security / Discourse and Pragmatics
7	- Commitment deadline: 2026-08-02
8	
9	## Title (Working)
10	DisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-Turn Jailbreak Detection
11	
12	## Core Insight
13	Multi-turn jailbreak attacks can easily vary lexical and semantic content of individual turns, but the discourse-level persuasion playbook (rapport → reframing → escalation) is a structural necessity for attack success. Removing any stage either fails the attack or reduces it to a single-turn attack already covered by existing defenses. DisPeD exploits this asymmetry by fine-tuning DeBERTa on persuasion strategy classification, producing turn embeddings that encode pragmatic function rather than (only) semantic content.
14	
15	## Core Claims (3)
16	
17	### Claim 1: Pragmatic Evasion Asymmetry (Theoretical + Empirical)
18	An evasion hierarchy exists for multi-turn jailbreak detection: lexical features (easily evaded via paraphrasing) < semantic embeddings (moderate, per-turn representations kept "benign" per Bullwinkel et al. 2025) < pragmatic persuasion patterns (structurally difficult to evade, as the persuasion playbook is a functional prerequisite for attack success).
19	- Evidence needed: adversarial perturbation experiment showing treatment degrades less than lexical/semantic baselines under paraphrasing
20	
21	### Claim 2: Early Detection via Persuasion Grounding
22	Persuasion-grounded turn embeddings (DeBERTa fine-tuned on 8-class persuasion taxonomy + intent) enable significantly earlier detection of multi-turn jailbreaks (at K=2-3 turns) compared to vanilla semantic embeddings, because persuasion strategy transitions (rapport → authority framing) manifest before explicitly harmful content appears.
23	- Evidence needed: early detection F1 at K=2,3 turns, treatment > baseline by >= 5pp on clean data (TF-IDF < 0.75)
24	
25	### Claim 3: Monotonic Escalation Trajectory
26	Adversarial conversations exhibit a monotonic escalation trajectory in persuasion strategy space (trust → test → normalize → elicit), while benign conversations exhibit oscillatory or non-monotonic patterns. This distinction is the mechanistic basis for Claims 1-2.
27	- Evidence needed: strategy transition matrix visualization, trajectory analysis comparing jailbreak vs benign
28	
29	## Story Spine
30	
31	**Problem**: Multi-turn jailbreak attacks (Crescendo, FITD, Deceptive Delight) distribute adversarial intent across individually benign turns. Bullwinkel et al. (2025) show per-turn representations are deliberately kept in a "benign" region, causing representation-level defenses to fail with a 50-point ASR gap. DeepContext (2026) tracks generic semantic drift but confuses benign conversational evolution with adversarial manipulation.
32	
33	**Gap**: Existing detectors operate at the lexical or semantic level where attacks deliberately hide. No published work combines persuasion-grounded turn representations with temporal sequence modeling for multi-turn jailbreak detection.
34	
35	**Our angle**: We identify the Pragmatic Evasion Asymmetry. The persuasion playbook (rapport → reframing → escalation) is a structural necessity for multi-turn attack success. Unlike lexical or semantic features, pragmatic persuasion patterns cannot be evaded without abandoning the attack itself. DisPeD fine-tunes DeBERTa on an 8-class persuasion taxonomy to produce pragmatic-aware turn embeddings, then models the temporal strategy sequence with a GRU to detect the characteristic escalation trajectory.
36	
37	**Headline result**: "DisPeD detects Crescendo-style jailbreaks at K=2 turns with F1=X vs Y for vanilla semantic baselines (+Z pp). Under adversarial paraphrasing that removes lexical cues, DisPeD maintains F1=W while lexical baselines degrade by V pp."
38	
39	## Architecture (Simplified for MVE)
40	
41	Single-track with persuasion grounding (full dual-track in future work):
42	1. **Stage 1**: DeBERTa-v3-base fine-tuned on multi-task objective: 8-class persuasion strategy classification + binary jailbreak-intent classification
43	2. **Stage 2**: Bi-GRU over DeBERTa [CLS] embeddings for conversation-level binary classification
44	3. **Baseline**: Same pipeline but with vanilla (not fine-tuned) DeBERTa embeddings
45	
46	## Venue Fit Risks
47	- EMNLP 2026 LLM Security track: strong fit (dedicated track, high visibility)
48	- Discourse/Pragmatics reviewers may want more linguistic rigor: ground taxonomy in PAP (ACL 2024), Hagendorff (Nature Comm 2026), Cialdini principles, Speech Act Theory (Austin 1962, Searle 1969)
49	- Safety reviewers expect multiple attack types: need >= 2 attack families
50	
51	## Anticipated Reviewer Concerns
52	
53	### RC1: Lexical Shortcut (CRITICAL, must address pre-submission)
54	TF-IDF=1.0 on current data means lexical features alone perfectly separate classes. Must show the model works on data without lexical shortcuts.
55	- Mitigation: (a) register-normalize jailbreak data to match benign register, verify TF-IDF < 0.75, retrain; (b) adversarial perturbation evaluation (Claim 3)
56	
57	### RC2: Small Dataset
58	480 samples is small for a detection paper.
59	- Mitigation: (a) statistical significance via bootstrap CI or paired tests; (b) cross-validation; (c) focus narrative on proof-of-concept for the principle, not SOTA numbers
60	
61	### RC3: Single Attack Type (Crescendo Only)
62	Need generalization evidence.
63	- Mitigation: generate FITD-style and Deceptive Delight-style conversations using existing pipeline
64	
65	### RC4: Strategy Label Confound (M004)
66	Benign turns hardcoded to strategy=7 creates shortcut for treatment model.
67	- Mitigation: (a) fix labeling (use "none"/9th class); (b) scrambled-label ablation
68	
69	### RC5: No DeepContext Comparison
70	Paper positions against DeepContext but no reproduction.
71	- Mitigation: vanilla DeBERTa → GRU is a fair proxy baseline (same architecture, only difference is persuasion grounding). Note DeepContext has no public code. If time allows, attempt reproduction as P1.
72	
73	### RC6: Interpretability Claims Without Human Eval
74	Strategy sequence outputs claimed interpretable but not evaluated.
75	- Mitigation: strategy transition matrix visualization (P1). Full human eval is future work given timeline constraints.
76	
77	## Scope Boundary
78	- IN: persuasion-mediated multi-turn attacks (Crescendo, FITD, Deceptive Delight, social engineering jailbreaks)
79	- OUT (acknowledged limitation): pure information accumulation attacks, token smuggling, single-frame roleplay
80	- The semantic GRU track provides coverage for out-of-scope attack types as a safety net
81	
82	## Theoretical Grounding
83	- Bullwinkel et al. (arXiv 2507.02956): per-turn representations kept "benign" by multi-turn attacks
84	- Speech Act Theory (Austin 1962, Searle 1969): existing detectors work at locutionary act level, DisPeD at illocutionary act level
85	- PAP (Zeng et al., ACL 2024): 40 persuasion techniques for jailbreaking
86	- Hagendorff (Nature Communications 2026): identifiable persuasion strategies in 97% ASR attacks
87	- "How Do LLMs Persuade?" (arXiv 2508.05625): persuasion dynamics extractable from turn-level representations
88	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61aab480-5dac-4dae-ab2e-989e0486f982",
  "isSidechain": false,
  "promptId": "0640bae5-48d0-4296-855e-879e96111727",
  "type": "user",
  "uuid": "8b92e436-8a6f-4d5d-aa4c-6ac71a5db4b4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper_framing.md",
      "content": "# Paper Framing — persuasion_turn_jailbreak_detect\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Deadline: 2026-05-25 (ARR May cycle)\n- Track: LLM Security / Discourse and Pragmatics\n- Commitment deadline: 2026-08-02\n\n## Title (Working)\nDisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-Turn Jailbreak Detection\n\n## Core Insight\nMulti-turn jailbreak attacks can easily vary lexical and semantic content of individual turns, but the discourse-level persuasion playbook (rapport → reframing → escalation) is a structural necessity for attack success. Removing any stage either fails the attack or reduces it to a single-turn attack already covered by existing defenses. DisPeD exploits this asymmetry by fine-tuning DeBERTa on persuasion strategy classification, producing turn embeddings that encode pragmatic function rather than (only) semantic content.\n\n## Core Claims (3)\n\n### Claim 1: Pragmatic Evasion Asymmetry (Theoretical + Empirical)\nAn evasion hierarchy exists for multi-turn jailbreak detection: lexical features (easily evaded via paraphrasing) < semantic embeddings (moderate, per-turn representations kept \"benign\" per Bullwinkel et al. 2025) < pragmatic persuasion patterns (structurally difficult to evade, as the persuasion playbook is a functional prerequisite for attack success).\n- Evidence needed: adversarial perturbation experiment showing treatment degrades less than lexical/semantic baselines under paraphrasing\n\n### Claim 2: Early Detection via Persuasion Grounding\nPersuasion-grounded turn embeddings (DeBERTa fine-tuned on 8-class persuasion taxonomy + intent) enable significantly earlier detection of multi-turn jailbreaks (at K=2-3 turns) compared to vanilla semantic embeddings, because persuasion strategy transitions (rapport → authority framing) manifest before explicitly harmful content appears.\n- Evidence needed: early detection F1 at K=2,3 turns, treatment > baseline by >= 5pp on clean data (TF-IDF < 0.75)\n\n### Claim 3: Monotonic Escalation Trajectory\nAdversarial conversations exhibit a monotonic escalation trajectory in persuasion strategy space (trust → test → normalize → elicit), while benign conversations exhibit oscillatory or non-monotonic patterns. This distinction is the mechanistic basis for Claims 1-2.\n- Evidence needed: strategy transition matrix visualization, trajectory analysis comparing jailbreak vs benign\n\n## Story Spine\n\n**Problem**: Multi-turn jailbreak attacks (Crescendo, FITD, Deceptive Delight) distribute adversarial intent across individually benign turns. Bullwinkel et al. (2025) show per-turn representations are deliberately kept in a \"benign\" region, causing representation-level defenses to fail with a 50-point ASR gap. DeepContext (2026) tracks generic semantic drift but confuses benign conversational evolution with adversarial manipulation.\n\n**Gap**: Existing detectors operate at the lexical or semantic level where attacks deliberately hide. No published work combines persuasion-grounded turn representations with temporal sequence modeling for multi-turn jailbreak detection.\n\n**Our angle**: We identify the Pragmatic Evasion Asymmetry. The persuasion playbook (rapport → reframing → escalation) is a structural necessity for multi-turn attack success. Unlike lexical or semantic features, pragmatic persuasion patterns cannot be evaded without abandoning the attack itself. DisPeD fine-tunes DeBERTa on an 8-class persuasion taxonomy to produce pragmatic-aware turn embeddings, then models the temporal strategy sequence with a GRU to detect the characteristic escalation trajectory.\n\n**Headline result**: \"DisPeD detects Crescendo-style jailbreaks at K=2 turns with F1=X vs Y for vanilla semantic baselines (+Z pp). Under adversarial paraphrasing that removes lexical cues, DisPeD maintains F1=W while lexical baselines degrade by V pp.\"\n\n## Architecture (Simplified for MVE)\n\nSingle-track with persuasion grounding (full dual-track in future work):\n1. **Stage 1**: DeBERTa-v3-base fine-tuned on multi-task objective: 8-class persuasion strategy classification + binary jailbreak-intent classification\n2. **Stage 2**: Bi-GRU over DeBERTa [CLS] embeddings for conversation-level binary classification\n3. **Baseline**: Same pipeline but with vanilla (not fine-tuned) DeBERTa embeddings\n\n## Venue Fit Risks\n- EMNLP 2026 LLM Security track: strong fit (dedicated track, high visibility)\n- Discourse/Pragmatics reviewers may want more linguistic rigor: ground taxonomy in PAP (ACL 2024), Hagendorff (Nature Comm 2026), Cialdini principles, Speech Act Theory (Austin 1962, Searle 1969)\n- Safety reviewers expect multiple attack types: need >= 2 attack families\n\n## Anticipated Reviewer Concerns\n\n### RC1: Lexical Shortcut (CRITICAL, must address pre-submission)\nTF-IDF=1.0 on current data means lexical features alone perfectly separate classes. Must show the model works on data without lexical shortcuts.\n- Mitigation: (a) register-normalize jailbreak data to match benign register, verify TF-IDF < 0.75, retrain; (b) adversarial perturbation evaluation (Claim 3)\n\n### RC2: Small Dataset\n480 samples is small for a detection paper.\n- Mitigation: (a) statistical significance via bootstrap CI or paired tests; (b) cross-validation; (c) focus narrative on proof-of-concept for the principle, not SOTA numbers\n\n### RC3: Single Attack Type (Crescendo Only)\nNeed generalization evidence.\n- Mitigation: generate FITD-style and Deceptive Delight-style conversations using existing pipeline\n\n### RC4: Strategy Label Confound (M004)\nBenign turns hardcoded to strategy=7 creates shortcut for treatment model.\n- Mitigation: (a) fix labeling (use \"none\"/9th class); (b) scrambled-label ablation\n\n### RC5: No DeepContext Comparison\nPaper positions against DeepContext but no reproduction.\n- Mitigation: vanilla DeBERTa → GRU is a fair proxy baseline (same architecture, only difference is persuasion grounding). Note DeepContext has no public code. If time allows, attempt reproduction as P1.\n\n### RC6: Interpretability Claims Without Human Eval\nStrategy sequence outputs claimed interpretable but not evaluated.\n- Mitigation: strategy transition matrix visualization (P1). Full human eval is future work given timeline constraints.\n\n## Scope Boundary\n- IN: persuasion-mediated multi-turn attacks (Crescendo, FITD, Deceptive Delight, social engineering jailbreaks)\n- OUT (acknowledged limitation): pure information accumulation attacks, token smuggling, single-frame roleplay\n- The semantic GRU track provides coverage for out-of-scope attack types as a safety net\n\n## Theoretical Grounding\n- Bullwinkel et al. (arXiv 2507.02956): per-turn representations kept \"benign\" by multi-turn attacks\n- Speech Act Theory (Austin 1962, Searle 1969): existing detectors work at locutionary act level, DisPeD at illocutionary act level\n- PAP (Zeng et al., ACL 2024): 40 persuasion techniques for jailbreaking\n- Hagendorff (Nature Communications 2026): identifiable persuasion strategies in 97% ASR attacks\n- \"How Do LLMs Persuade?\" (arXiv 2508.05625): persuasion dynamics extractable from turn-level representations\n",
      "numLines": 88,
      "startLine": 1,
      "totalLines": 88
    }
  },
  "sourceToolAssistantUUID": "61aab480-5dac-4dae-ab2e-989e0486f982",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:11:42.713Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KZf2AerfxDczQwkC1urvR8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6df3a3a-4873-440b-b831-5f567de8ab31",
  "isSidechain": false,
  "requestId": "req_011Cb8WjXVNnvND2SaLK55mo",
  "type": "assistant",
  "uuid": "61aab480-5dac-4dae-ab2e-989e0486f982",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JAs3Gwoj3GBkMEuhbKQgN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12511,
      "cache_read_input_tokens": 11841,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12511,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 220,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12511
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165817 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_ja…",
  "leafUuid": "8b92e436-8a6f-4d5d-aa4c-6ac71a5db4b4",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated jailbreak detection research paper",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90"
}
```

---

### Assistant

_source line 14 · 2026-05-17T17:11:46.354Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me write a complete LaTeX paper based on the experiment data and paper framing. Let me first check that the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b92e436-8a6f-4d5d-aa4c-6ac71a5db4b4",
  "isSidechain": false,
  "requestId": "req_011Cb8WjoeiYJgtBhxiCeE3G",
  "type": "assistant",
  "uuid": "d0f5a0f8-5b72-428b-9ca9-3fdea01babf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018M4ZEojUxHjWSXz263MP1c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14077,
      "cache_read_input_tokens": 24352,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14077,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 24352,
          "cache_creation_input_tokens": 14077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14077
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

_source line 15 · 2026-05-17T17:11:46.763Z_

Let me verify the output directory exists, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0f5a0f8-5b72-428b-9ca9-3fdea01babf0",
  "isSidechain": false,
  "requestId": "req_011Cb8WjoeiYJgtBhxiCeE3G",
  "type": "assistant",
  "uuid": "350d8864-c3f1-4023-8578-f37afc0c2e5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018M4ZEojUxHjWSXz263MP1c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14077,
      "cache_read_input_tokens": 24352,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14077,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 24352,
          "cache_creation_input_tokens": 14077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14077
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

_source line 16 · 2026-05-17T17:11:49.238Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gj2whSzCA2QsT7A6h5w2o1`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "350d8864-c3f1-4023-8578-f37afc0c2e5e",
  "isSidechain": false,
  "requestId": "req_011Cb8WjoeiYJgtBhxiCeE3G",
  "type": "assistant",
  "uuid": "e3b56b82-b2f5-4a2e-8662-800ff5db564d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018M4ZEojUxHjWSXz263MP1c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14077,
      "cache_read_input_tokens": 24352,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14077,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 24352,
          "cache_creation_input_tokens": 14077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14077
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

_source line 17 · 2026-05-17T17:11:49.465Z_

<details><summary>↩ Tool result · `toolu_01Gj2whSzCA2QsT7A6h5w2o1`</summary>

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
  "parentUuid": "e3b56b82-b2f5-4a2e-8662-800ff5db564d",
  "isSidechain": false,
  "promptId": "0640bae5-48d0-4296-855e-879e96111727",
  "type": "user",
  "uuid": "14028653-db8b-452b-8274-a0b8f9f73aed",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e3b56b82-b2f5-4a2e-8662-800ff5db564d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-17T17:12:08.400Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists. Now I'll write the complete LaTeX paper. Let me carefully construct it based on all the experiment data and the paper framing guidance.

Key points from the data:
1. Data quality fix: TF-IDF dropped from 1.0 to 0.58 after register normalization
2. Core results on clean data: treatment K=2 F1=0.91 vs baseline 0.77 (14pp delta)
3. Scrambled label ablation: 15pp drop at K=2
4. Adversarial perturbation: treatment -3pp, baseline -13pp, TF-IDF -18pp


5. Cross-attack generalization shows strong robustness with 16.5pp improvement, while strategy transitions reveal much higher monotonicity in the treatment approach
6. WildChat hard negatives and cross-checkpoint variance both demonstrate stability, and the DeepContext proxy experiments confirm the core findings hold across different model scales
7. Now I'm organizing the paper structure—I'll map each experiment to its corresponding section and table, starting with data quality fixes in the methods section, then the main results covering revalidation and ablations, followed by analysis of the generalization and robustness findings

, and finally mechanistic insights and edge cases in the later sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14028653-db8b-452b-8274-a0b8f9f73aed",
  "isSidechain": false,
  "requestId": "req_011Cb8WkJJeJdUVZmewWNBkC",
  "type": "assistant",
  "uuid": "58f91cd7-b1a6-4d2d-97f1-5b1768784230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMPQ78yT5ZXBhC3QgEXQbA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 220,
      "cache_read_input_tokens": 38429,
      "output_tokens": 11941,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 220,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11941,
          "cache_read_input_tokens": 38429,
          "cache_creation_input_tokens": 220,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 220
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

_source line 19 · 2026-05-17T17:12:08.402Z_

Now writing the full paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58f91cd7-b1a6-4d2d-97f1-5b1768784230",
  "isSidechain": false,
  "requestId": "req_011Cb8WkJJeJdUVZmewWNBkC",
  "type": "assistant",
  "uuid": "8119d835-21d1-46c8-8c8c-b3858d7a29bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMPQ78yT5ZXBhC3QgEXQbA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 220,
      "cache_read_input_tokens": 38429,
      "output_tokens": 11941,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 220,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11941,
          "cache_read_input_tokens": 38429,
          "cache_creation_input_tokens": 220,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 220
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

_source line 20 · 2026-05-17T17:15:11.663Z_

<details open><summary>🔧 Tool call — Write · `toolu_01AtNmfQFKW6LW8Nxv4wsPnQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\n\\title{DisPeD: Exploiting the Pragmatic Evasion Asymmetry\\\\for Robust Multi-Turn Jailbreak Detection}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nMulti-turn jailbreak attacks against Large Language Models (LLMs) distribute adversarial intent across individually benign turns, defeating detectors that operate at the lexical or semantic level. We identify a \\emph{Pragmatic Evasion Asymmetry}: attackers can freely paraphrase surface content, but the underlying persuasion playbook (rapport building, reframing, escalation) is a structural prerequisite for attack success and cannot be removed without abandoning the attack itself. DisPeD exploits this asymmetry by fine-tuning DeBERTa on an 8-class persuasion strategy taxonomy to produce pragmatic-aware turn embeddings, then modeling the temporal strategy sequence with a GRU for conversation-level classification. On register-normalized data that eliminates lexical shortcuts (TF-IDF reduced from 1.0 to 0.58), DisPeD achieves F1\\,=\\,0.91 at only $K$\\,=\\,2 turns, a 14 percentage point (pp) improvement over a vanilla semantic baseline ($p$\\,<\\,0.001). Under adversarial paraphrasing, DisPeD degrades by only 3\\,pp while semantic and lexical baselines degrade by 13\\,pp and 18\\,pp respectively. A model trained exclusively on Crescendo-style attacks generalizes zero-shot to Foot-in-the-Door and Deceptive Delight attacks with an average F1 of 0.85, outperforming the semantic baseline by 16.5\\,pp. These results establish that discourse-level persuasion patterns provide a robust and generalizable signal for early multi-turn jailbreak detection.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nMulti-turn jailbreak attacks pose a growing threat to deployed LLMs. Attacks such as Crescendo~\\citep{russinovich2024greatnow}, Foot-in-the-Door (FITD)~\\citep{zhou2024speak}, and Deceptive Delight~\\citep{jiang2024deceptive} distribute adversarial intent across multiple conversational turns, each of which appears benign in isolation. \\citet{bullwinkel2025multiturn} show that per-turn representations of these attacks are deliberately kept in a ``benign'' region of embedding space, causing representation-level defenses to fail with a 50-point ASR gap. Temporal approaches that track generic semantic drift~\\citep{su2026deepcontext} confuse benign conversational evolution with adversarial manipulation, producing high false-positive rates.\n\nWhy are these attacks so effective? A multi-turn attacker must accomplish two things: (1) maintain surface-level benignity on each turn, and (2) gradually steer the model toward compliance through a persuasion playbook. \\citet{zeng2024persuasion} and \\citet{hagendorff2026nature} independently show that identifiable persuasion strategies appear in over 97\\% of successful multi-turn attacks. The attacker has enormous freedom in choosing \\emph{what words} to use (lexical level) and \\emph{what topics} to discuss (semantic level), but the underlying \\emph{pragmatic function} of each turn (rapport building, authority appeal, reframing) is constrained by the attack's functional requirements.\n\nThis observation motivates what we call the \\textbf{Pragmatic Evasion Asymmetry}: an evasion hierarchy exists in which lexical features are easily evaded via paraphrasing, semantic embeddings are moderately robust but still vulnerable to per-turn content manipulation, and pragmatic persuasion patterns are structurally difficult to evade because they constitute the functional mechanism of the attack. In the terminology of Speech Act Theory~\\citep{austin1962things,searle1969speech}, existing detectors operate at the locutionary act level (what was said), while DisPeD operates at the illocutionary act level (what was done).\n\nWe present \\textbf{DisPeD} (\\textbf{Dis}course-level \\textbf{Pe}rsuasion \\textbf{D}etector), a two-stage pipeline that first fine-tunes DeBERTa-v3-base~\\citep{he2021debertav3} on a multi-task objective combining 8-class persuasion strategy classification and binary intent classification, then feeds the resulting turn embeddings into a bidirectional GRU for conversation-level jailbreak detection. By grounding turn representations in a persuasion taxonomy derived from Cialdini's influence principles~\\citep{cialdini2001science}, DisPeD detects the characteristic escalation trajectory of multi-turn attacks at the earliest possible stage.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item We formalize the \\emph{Pragmatic Evasion Asymmetry} and provide empirical evidence through a three-tier robustness experiment: under adversarial paraphrasing, DisPeD (pragmatic) degrades by 3\\,pp, a vanilla semantic baseline by 13\\,pp, and a TF-IDF lexical baseline by 18\\,pp (Section~\\ref{sec:evasion}).\n    \\item We demonstrate that persuasion-grounded embeddings enable significantly earlier detection: F1\\,=\\,0.91 at $K$\\,=\\,2 turns versus 0.77 for the semantic baseline, a 14\\,pp advantage that holds across attack types with zero-shot cross-attack transfer averaging 16.5\\,pp improvement (Sections~\\ref{sec:main_results} and~\\ref{sec:cross_attack}).\n    \\item We provide a mechanistic analysis showing that jailbreak conversations exhibit monotonic escalation trajectories in persuasion strategy space (monotonicity score 0.82 vs. 0.34 for benign), explaining why pragmatic features succeed where semantic features fail (Section~\\ref{sec:trajectory}).\n\\end{enumerate}\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Multi-turn jailbreak attacks.}\nCrescendo~\\citep{russinovich2024greatnow} gradually escalates through conversational rapport, achieving high attack success rates against commercial LLMs. FITD~\\citep{zhou2024speak} applies the foot-in-the-door compliance technique, starting with small requests and progressively increasing severity. Deceptive Delight~\\citep{jiang2024deceptive} interleaves harmful content within benign creative writing frames. These attacks share a common structure: a persuasion playbook that transitions from trust-building to explicit elicitation across turns. \\citet{hagendorff2026nature} analyze persuasion strategies in adversarial conversations and find identifiable patterns in 97\\% of successful attacks, confirming that the persuasion structure is systematic rather than incidental.\n\n\\paragraph{Jailbreak detection.}\nSingle-turn detectors such as perplexity filters~\\citep{alon2023detecting} and input classifiers~\\citep{inan2023llama} fail against multi-turn attacks because individual turns appear benign. \\citet{bullwinkel2025multiturn} demonstrate that per-turn representations are deliberately maintained in benign embedding regions. DeepContext~\\citep{su2026deepcontext} addresses this by tracking semantic drift across turns with an encoder-RNN pipeline, but uses generic embeddings that conflate benign topic evolution with adversarial manipulation.\n\n\\paragraph{Persuasion and LLM safety.}\n\\citet{zeng2024persuasion} compile 40 persuasion techniques used in jailbreaking and show that persuasion-augmented prompts significantly increase ASR. \\citet{chen2025persuade} study how LLMs deploy persuasion strategies during multi-turn interactions, demonstrating that persuasion dynamics are extractable from turn-level representations. Our work is the first to use persuasion-grounded representations for jailbreak \\emph{detection} rather than attack construction or analysis.\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\nDisPeD consists of two stages: a persuasion-grounded encoder and a temporal sequence classifier.\n\n\\subsection{Stage 1: Persuasion-Grounded Encoder}\n\nWe fine-tune DeBERTa-v3-base on a multi-task objective with two heads:\n\n\\begin{itemize}\n    \\item \\textbf{Persuasion strategy classification} (8 classes): rapport building, authority appeal, reciprocity, social proof, commitment/consistency, scarcity/urgency, reframing, and direct request. These categories are derived from Cialdini's principles of influence~\\citep{cialdini2001science} and adapted for adversarial conversational contexts following \\citet{zeng2024persuasion}. Benign turns lacking a persuasion function receive a ``none'' label.\n    \\item \\textbf{Intent classification} (binary): whether the turn carries jailbreak intent.\n\\end{itemize}\n\nThe total loss is $\\mathcal{L} = \\mathcal{L}_{\\text{persuasion}} + \\lambda \\mathcal{L}_{\\text{intent}}$, where $\\lambda = 1.0$. After training, we extract the [CLS] embedding from the fine-tuned encoder as the persuasion-grounded turn representation. The encoder achieves 79\\% accuracy on 8-class persuasion classification and 94\\% on binary intent classification (Table~\\ref{tab:encoder}).\n\n\\subsection{Stage 2: Temporal Sequence Classification}\n\nGiven a conversation of $K$ turns, we obtain turn embeddings $\\{e_1, \\ldots, e_K\\}$ from the Stage 1 encoder. A bidirectional GRU processes the embedding sequence and outputs a conversation-level binary classification (jailbreak vs. benign) from the final hidden state. This architecture captures the temporal progression of persuasion strategies across turns.\n\n\\subsection{Baselines}\n\nWe compare DisPeD against three baselines spanning the evasion hierarchy:\n\\begin{itemize}\n    \\item \\textbf{TF-IDF + Logistic Regression}: a lexical baseline operating on bag-of-words features.\n    \\item \\textbf{DeBERTa Semantic Baseline}: the same Stage 2 GRU pipeline but with \\emph{vanilla} (not fine-tuned) DeBERTa embeddings, representing semantic-level detection.\n    \\item \\textbf{DeepContext Proxy}: BERT-base + GRU, simulating the DeepContext architecture with generic drift features and no persuasion grounding.\n\\end{itemize}\n\n% ============================================================\n% 4. EXPERIMENTAL SETUP\n% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\subsection{Data Preparation and Register Normalization}\n\\label{sec:data}\n\nOur dataset consists of 480 conversations (240 jailbreak, 240 benign) with 72 held out for testing. Jailbreak conversations are Crescendo-style multi-turn attacks; benign conversations are drawn from standard conversational corpora and WildChat~\\citep{zhao2024wildchat}.\n\nA critical challenge in multi-turn jailbreak detection is \\emph{lexical shortcut}: scripted attack dialogues have distributional properties distinct from naturalistic benign conversations, allowing simple bag-of-words classifiers to succeed without learning meaningful features. On our original data, TF-IDF separability was 1.0, indicating complete lexical shortcut.\n\nWe apply register normalization using LLM paraphrasing to convert jailbreak turns from formal/scripted register to conversational register, eliminating the distributional gap. Table~\\ref{tab:tfidf_diagnostic} confirms the effectiveness of this procedure: TF-IDF drops from 1.0 to 0.58, below our hard gate of 0.75 but above the random baseline of 0.50, reflecting residual functional vocabulary (e.g., ``hypothetical,'' ``scenario'') that attackers cannot entirely avoid. Persuasion strategy annotations are preserved at 94\\% after normalization, confirming that the persuasion structure is a discourse-level phenomenon independent of lexical realization.\n\n\\begin{table}[t]\n\\centering\n\\caption{TF-IDF separability before and after register normalization.}\n\\label{tab:tfidf_diagnostic}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{TF-IDF} & \\textbf{Vocab Overlap (\\%)} \\\\\n\\midrule\nOriginal data & 1.00 & 12.3 \\\\\nRegister-normalized & 0.58 & 41.7 \\\\\nRandom baseline & 0.50 & 50.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Attack Dataset}\n\\label{sec:multi_attack_data}\n\nTo evaluate cross-attack generalization (Section~\\ref{sec:cross_attack}), we generate additional attack conversations in two families beyond Crescendo using Qwen3-8B: 72 FITD-style conversations (avg. 6.8 turns) employing the foot-in-the-door compliance escalation pattern, and 65 Deceptive Delight-style conversations (avg. 5.2 turns) interleaving harmful content within benign frames. All generated conversations receive persuasion strategy annotations with 91\\% LLM annotation consistency. Table~\\ref{tab:attack_stats} summarizes the dataset statistics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Attack type statistics. TF-IDF measured against benign conversations.}\n\\label{tab:attack_stats}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Attack Type} & \\textbf{$n$} & \\textbf{Avg Turns} & \\textbf{Turn Range} & \\textbf{TF-IDF} \\\\\n\\midrule\nCrescendo (original) & 240 & 5.5 & 3--12 & 0.58 \\\\\nFITD (generated) & 72 & 6.8 & 4--10 & 0.61 \\\\\nDeceptive Delight (generated) & 65 & 5.2 & 3--8 & 0.55 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe three attack types share the same persuasion strategy vocabulary but differ in temporal arrangement. As shown in Table~\\ref{tab:strategy_dist}, FITD relies heavily on reciprocity (30\\%) and commitment/consistency (25\\%), reflecting its gradual compliance escalation. Deceptive Delight favors authority appeal (22\\%) and social proof (18\\%), using authoritative framing to embed harmful content. Crescendo is more evenly distributed across strategies. This variation in strategy profiles, combined with a shared underlying vocabulary, provides the conditions for testing zero-shot cross-attack transfer.\n\n\\begin{table}[t]\n\\centering\n\\caption{Persuasion strategy distribution (\\%) by attack type.}\n\\label{tab:strategy_dist}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Crescendo} & \\textbf{FITD} & \\textbf{Dec. Delight} \\\\\n\\midrule\nRapport building & 28 & 35 & 15 \\\\\nAuthority appeal & 12 & 8 & 22 \\\\\nReciprocity & 18 & 30 & 10 \\\\\nSocial proof & 8 & 5 & 18 \\\\\nCommitment/consistency & 15 & 25 & 8 \\\\\nScarcity/urgency & 5 & 3 & 12 \\\\\nReframing & 22 & 15 & 20 \\\\\nDirect request & 7 & 4 & 15 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 5. RESULTS\n% ============================================================\n\\section{Results}\n\n\\subsection{Main Results: Early Detection on Clean Data}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents the core comparison between DisPeD and the semantic baseline across turn budgets on register-normalized data. DisPeD achieves F1\\,=\\,0.91 at $K$\\,=\\,2 turns, a 14\\,pp improvement over the semantic baseline (0.77, $p$\\,<\\,0.001 by bootstrap test). The advantage is largest at early turn budgets ($K$\\,=\\,1--2) and narrows at higher $K$ as the baseline accumulates sufficient semantic drift signal, converging to a 7\\,pp gap on full conversations.\n\n\\begin{table}[t]\n\\centering\n\\caption{F1 by turn budget on clean (register-normalized) data. $\\Delta$ is the improvement of DisPeD over the semantic baseline in percentage points. All $p$-values by bootstrap test.}\n\\label{tab:main_results}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$K$} & \\textbf{DisPeD} & \\textbf{Baseline} & \\textbf{$\\Delta$ (pp)} & \\textbf{$p$} \\\\\n\\midrule\n1 & 0.82 & 0.68 & 14 & 0.003 \\\\\n2 & 0.91 & 0.77 & 14 & 0.001 \\\\\n3 & 0.93 & 0.83 & 10 & 0.004 \\\\\n5 & 0.96 & 0.88 & 8 & 0.012 \\\\\nAll & 0.96 & 0.89 & 7 & 0.018 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $K$\\,=\\,2, DisPeD also achieves a substantially lower false-positive rate at 95\\% TPR: FPR\\,=\\,0.08 versus 0.19 for the baseline. This early detection capability is the headline result: persuasion strategy transitions (e.g., rapport building to authority framing) manifest within the first two turns, providing discriminative signal before explicitly harmful content appears.\n\nTable~\\ref{tab:encoder} reports the Stage 1 encoder metrics. The 79\\% persuasion classification accuracy (macro F1\\,=\\,0.74) confirms that the encoder learns meaningful persuasion representations rather than noise, while the 94\\% intent accuracy validates the multi-task training.\n\n\\begin{table}[t]\n\\centering\n\\caption{DeBERTa encoder metrics on clean data.}\n\\label{tab:encoder}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nPersuasion 8-class accuracy & 0.79 \\\\\nPersuasion macro F1 & 0.74 \\\\\nIntent binary accuracy & 0.94 \\\\\nBest epoch & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pragmatic Evasion Asymmetry}\n\\label{sec:evasion}\n\nTo empirically validate the Pragmatic Evasion Asymmetry, we apply aggressive paraphrasing (synonym substitution, sentence restructuring) to jailbreak conversations and measure detection degradation across four model tiers. Table~\\ref{tab:evasion_full} reports results on full conversations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Evasion hierarchy under adversarial paraphrasing (full conversation). Models ordered by abstraction level. Drop is the F1 degradation in percentage points.}\n\\label{tab:evasion_full}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{F1 (Clean)} & \\textbf{F1 (Perturbed)} & \\textbf{Drop (pp)} \\\\\n\\midrule\nDisPeD (pragmatic) & 0.96 & 0.93 & 3 \\\\\nDeBERTa baseline (semantic) & 0.89 & 0.76 & 13 \\\\\nDeepContext proxy (generic temporal) & 0.84 & 0.69 & 15 \\\\\nTF-IDF + LR (lexical) & 0.72 & 0.54 & 18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe results reveal a clear three-tier gradient aligned with the predicted evasion hierarchy. TF-IDF collapses under perturbation ($-$18\\,pp) because synonym substitution directly destroys the lexical features it relies on. The DeepContext proxy degrades by 15\\,pp because BERT-base representations partially depend on surface patterns. The semantic baseline degrades moderately ($-$13\\,pp) as contextual embeddings are disrupted by token-level changes even when meaning is largely preserved. DisPeD degrades minimally ($-$3\\,pp) because persuasion-grounded representations encode illocutionary acts that are invariant to paraphrasing: ``building rapport through self-disclosure'' retains its pragmatic function regardless of lexical realization.\n\nA particularly strong result: DisPeD under adversarial perturbation (F1\\,=\\,0.93) still outperforms the semantic baseline on \\emph{unperturbed} data (F1\\,=\\,0.89). Table~\\ref{tab:evasion_k2} shows that this pattern holds at $K$\\,=\\,2, where DisPeD maintains F1\\,=\\,0.87 versus 0.63 for the semantic baseline.\n\n\\begin{table}[t]\n\\centering\n\\caption{Evasion hierarchy at $K$\\,=\\,2 turns.}\n\\label{tab:evasion_k2}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{F1 Clean} & \\textbf{F1 Perturbed} & \\textbf{Drop (pp)} \\\\\n\\midrule\nDisPeD & 0.91 & 0.87 & 4 \\\\\nDeBERTa baseline & 0.77 & 0.63 & 14 \\\\\nTF-IDF + LR & 0.65 & 0.48 & 17 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Ablation: Scrambled Label Analysis}\n\\label{sec:ablation}\n\nTo confirm that the advantage of DisPeD comes from the \\emph{semantic content} of persuasion labels rather than the fine-tuning process itself, we retrain the encoder with randomly scrambled persuasion strategy labels (intent labels remain intact). Table~\\ref{tab:scrambled} shows that scrambling causes a 15\\,pp drop at $K$\\,=\\,2, bringing performance close to the vanilla baseline (0.76 vs. 0.77). The scrambled encoder's persuasion classification accuracy drops to 0.13 ($\\approx 1/8$ random chance), confirming that the label signal is destroyed. This ablation establishes a causal link: the discriminative power of DisPeD derives from the semantic content of persuasion strategy annotations, not from any incidental benefit of multi-task training.\n\n\\begin{table}[t]\n\\centering\n\\caption{Effect of scrambling persuasion strategy labels. Drop is relative to properly labeled DisPeD.}\n\\label{tab:scrambled}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{$K$} & \\textbf{Proper Labels} & \\textbf{Scrambled Labels} & \\textbf{Drop (pp)} \\\\\n\\midrule\n2 & 0.91 & 0.76 & 15 \\\\\n3 & 0.93 & 0.81 & 12 \\\\\nAll & 0.96 & 0.87 & 9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Attack Zero-Shot Generalization}\n\\label{sec:cross_attack}\n\nA model trained exclusively on Crescendo-style attacks is evaluated zero-shot on FITD and Deceptive Delight attacks. Table~\\ref{tab:cross_attack} presents the results. DisPeD achieves an average F1 of 0.85 on unseen attack types, outperforming the semantic baseline by 16.5\\,pp. DisPeD on unseen attacks (0.85) approaches the semantic baseline on \\emph{seen} attacks (0.89), demonstrating that persuasion-grounded representations capture attack-type-agnostic pragmatic signals.\n\n\\begin{table}[t]\n\\centering\n\\caption{Zero-shot cross-attack generalization (full conversation). The model is trained on Crescendo only.}\n\\label{tab:cross_attack}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Attack Type} & \\textbf{DisPeD} & \\textbf{Baseline} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nFITD & 0.84 & 0.67 & 17 \\\\\nDeceptive Delight & 0.86 & 0.70 & 16 \\\\\nCrescendo (held-out) & 0.96 & 0.89 & 7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_attack_k2} reports early detection on unseen attacks. At $K$\\,=\\,2, DisPeD achieves recall of 0.78 on FITD and 0.81 on Deceptive Delight, versus 0.55 and 0.58 for the baseline.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-attack early detection recall at $K$\\,=\\,2.}\n\\label{tab:cross_attack_k2}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Attack Type} & \\textbf{DisPeD Recall} & \\textbf{Baseline Recall} \\\\\n\\midrule\nFITD & 0.78 & 0.55 \\\\\nDeceptive Delight & 0.81 & 0.58 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe transfer works because all three attack types share the same persuasion strategy vocabulary (Table~\\ref{tab:strategy_dist}), differing only in temporal arrangement. The GRU learns a generic ``persuasion escalation'' detector rather than Crescendo-specific surface patterns. Deceptive Delight transfers slightly better (0.86 vs. 0.84) because its strategy profile (strong reframing component) more closely resembles Crescendo's distribution.\n\n\\subsection{Mechanistic Analysis: Escalation Trajectories}\n\\label{sec:trajectory}\n\nTo provide a mechanistic explanation for why pragmatic features succeed, we analyze persuasion strategy transition patterns. Table~\\ref{tab:trajectory} reports two quantitative metrics distinguishing jailbreak from benign conversations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Strategy transition statistics. Monotonicity measures the fraction of transitions along the escalation direction. Entropy measures the diversity of transition types.}\n\\label{tab:trajectory}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Type} & \\textbf{Transition Entropy} & \\textbf{Monotonicity} & \\textbf{$n$} \\\\\n\\midrule\nJailbreak & 1.8 & 0.82 & 240 \\\\\nBenign & 2.9 & 0.34 & 240 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nJailbreak conversations exhibit highly monotonic escalation (score 0.82): 82\\% of strategy transitions move from lower-risk to higher-risk categories (e.g., rapport building $\\to$ commitment/consistency $\\to$ reframing $\\to$ direct request). Benign conversations show near-random monotonicity (0.34) with oscillatory, task-driven patterns. Transition entropy is lower for jailbreaks (1.8 vs. 2.9) because attackers follow a concentrated playbook, while benign conversations traverse a wider range of pragmatic functions.\n\nTable~\\ref{tab:dominant_sequences} shows the most frequent strategy sequences. Jailbreak conversations converge on a small number of escalation trajectories (top-3 covering 74\\% of cases), while benign conversations are dominated by ``none'' labels (45\\%) reflecting the absence of persuasion intent. The trajectory-only separability (AUROC\\,=\\,0.91) confirms that the escalation pattern alone, without any content features, is strongly discriminative.\n\n\\begin{table}[t]\n\\centering\n\\caption{Top-3 dominant strategy sequences by conversation type.}\n\\label{tab:dominant_sequences}\n\\small\n\\begin{tabular}{clcclc}\n\\toprule\n & \\textbf{Jailbreak Sequence} & \\textbf{\\%} & & \\textbf{Benign Sequence} & \\textbf{\\%} \\\\\n\\midrule\n1 & rapport$\\to$commit$\\to$reframe$\\to$direct & 34 & 1 & none$\\to$none$\\to$none$\\to$none & 45 \\\\\n2 & rapport$\\to$social$\\to$reframe$\\to$direct & 22 & 2 & rapport$\\to$none$\\to$rapport$\\to$none & 18 \\\\\n3 & rapport$\\to$reciprocity$\\to$commit$\\to$direct & 18 & 3 & none$\\to$rapport$\\to$none$\\to$direct & 12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Robustness on Hard Negatives}\n\\label{sec:hard_negatives}\n\nA potential concern is that DisPeD might flag benign conversations with high topic diversity as jailbreaks. We evaluate on hard negatives from WildChat~\\citep{zhao2024wildchat}: 120 high-drift benign conversations where users shift across multiple domains (e.g., coding to personal advice to creative writing). We filter 15.2\\% of WildChat conversations as potential contamination.\n\n\\begin{table}[t]\n\\centering\n\\caption{False-positive rate on hard negatives (high-drift benign) vs. random benign.}\n\\label{tab:hard_negatives}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{FPR (Hard)} & \\textbf{FPR (Random)} & \\textbf{$\\Delta$} \\\\\n\\midrule\nDisPeD & 0.09 & 0.03 & 0.06 \\\\\nDeBERTa baseline & 0.17 & 0.06 & 0.11 \\\\\nTF-IDF + LR & 0.22 & 0.08 & 0.14 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:hard_negatives} shows that DisPeD maintains a low FPR of 9\\% on hard negatives, compared to 17\\% for the semantic baseline and 22\\% for TF-IDF. The persuasion-grounded representations distinguish ``topic drift'' (benign, oscillatory strategy transitions) from ``strategy escalation'' (adversarial, monotonic trajectory), a distinction that semantic embeddings cannot reliably make.\n\n\\subsection{Lexical Baseline Analysis}\n\\label{sec:lexical}\n\nTable~\\ref{tab:tfidf_performance} reports the TF-IDF + Logistic Regression baseline on clean data. Even after register normalization, residual lexical signal provides above-chance performance (F1\\,=\\,0.72) due to functional vocabulary that attackers cannot entirely avoid. The top discriminative features (Table~\\ref{tab:top_features}) confirm this: jailbreak-indicative words (``hypothetical,'' ``scenario,'' ``imagine'') are framing devices required by the attack structure. This residual lexical signal (F1\\,=\\,0.72) falls far short of what pragmatic features achieve (F1\\,=\\,0.96) and collapses under adversarial perturbation (F1\\,=\\,0.54).\n\n\\begin{table}[t]\n\\centering\n\\caption{TF-IDF + LR performance by turn budget on clean data.}\n\\label{tab:tfidf_performance}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{$K$} & \\textbf{F1} & \\textbf{Precision} & \\textbf{Recall} \\\\\n\\midrule\n2 & 0.65 & 0.68 & 0.62 \\\\\n3 & 0.68 & 0.71 & 0.65 \\\\\n5 & 0.70 & 0.73 & 0.68 \\\\\nAll & 0.72 & 0.75 & 0.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Top-5 discriminative features by LR coefficient.}\n\\label{tab:top_features}\n\\begin{tabular}{clccl c}\n\\toprule\n\\textbf{Rank} & \\textbf{Jailbreak Feature} & \\textbf{Weight} & & \\textbf{Benign Feature} & \\textbf{Weight} \\\\\n\\midrule\n1 & hypothetical & 2.31 & & thanks & 1.89 \\\\\n2 & scenario & 1.95 & & help & 1.72 \\\\\n3 & imagine & 1.87 & & question & 1.54 \\\\\n4 & creative & 1.62 & & code & 1.41 \\\\\n5 & roleplay & 1.48 & & explain & 1.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Checkpoint Sensitivity}\n\\label{sec:checkpoint}\n\nTo assess reproducibility on our relatively small dataset, we evaluate DisPeD with DeBERTa encoders from different training epochs. Table~\\ref{tab:checkpoint} shows that downstream F1 varies by at most 1\\,pp across checkpoints, indicating that the results are robust to encoder training stochasticity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Checkpoint sensitivity analysis.}\n\\label{tab:checkpoint}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Checkpoint} & \\textbf{Persuasion Acc} & \\textbf{Intent Acc} & \\textbf{F1 (Full)} & \\textbf{F1 ($K$=2)} \\\\\n\\midrule\nEpoch 2 & 0.76 & 0.93 & 0.94 & 0.89 \\\\\nEpoch 3 & 0.79 & 0.94 & 0.96 & 0.91 \\\\\nEpoch final & 0.78 & 0.94 & 0.95 & 0.90 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 6. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why pragmatic features are structurally robust.}\nThe Pragmatic Evasion Asymmetry is not merely an empirical observation but follows from the functional requirements of multi-turn attacks. An attacker who removes rapport building cannot establish the trust needed for later compliance. An attacker who skips reframing cannot normalize the harmful request. An attacker who eliminates all escalation has, by definition, not conducted a multi-turn attack. Each persuasion strategy serves a necessary function in the attack pipeline, and our experiments confirm that this structural constraint translates into measurably robust detection features.\n\n\\paragraph{Limitations.}\nOur dataset is small (480 conversations) and the generated attack conversations may not capture the full diversity of real-world adversarial behavior. The persuasion taxonomy is limited to 8 categories; a finer-grained taxonomy might capture additional discriminative patterns. We do not evaluate against attacks that deliberately target the persuasion detection mechanism (adaptive adversaries aware of DisPeD). Human evaluation of the interpretability of strategy trajectories remains future work. Our scope is limited to persuasion-mediated multi-turn attacks; pure information accumulation attacks, token smuggling, and single-turn roleplay jailbreaks fall outside our detection target.\n\n% ============================================================\n% 7. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe introduced DisPeD, a multi-turn jailbreak detector that exploits the Pragmatic Evasion Asymmetry by grounding turn representations in a persuasion strategy taxonomy. Our experiments on register-normalized data demonstrate three key findings: (1) pragmatic features degrade minimally under adversarial paraphrasing (3\\,pp) compared to semantic (13\\,pp) and lexical (18\\,pp) features; (2) persuasion-grounded embeddings enable early detection at $K$\\,=\\,2 turns with 14\\,pp improvement over semantic baselines, an advantage that transfers zero-shot across attack families; and (3) the mechanistic basis for this advantage is the monotonic escalation trajectory in persuasion strategy space that characterizes multi-turn attacks. These results suggest that discourse-level pragmatic analysis is a promising direction for building jailbreak defenses that are robust to surface-level evasion.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Alon and Kamfonas(2023)]{alon2023detecting}\nG.~Alon and M.~Kamfonas.\n\\newblock Detecting language model attacks with perplexity.\n\\newblock \\emph{arXiv preprint arXiv:2308.14132}, 2023.\n\n\\bibitem[Austin(1962)]{austin1962things}\nJ.~L. Austin.\n\\newblock \\emph{How to Do Things with Words}.\n\\newblock Oxford University Press, 1962.\n\n\\bibitem[Bullwinkel et~al.(2025)]{bullwinkel2025multiturn}\nS.~Bullwinkel, P.~Schramowski, and K.~Kersting.\n\\newblock Multi-turn jailbreaks hide in the representation space.\n\\newblock \\emph{arXiv preprint arXiv:2507.02956}, 2025.\n\n\\bibitem[Chen et~al.(2025)]{chen2025persuade}\nW.~Chen, Y.~Li, and R.~Jia.\n\\newblock How do {LLMs} persuade? {E}xtracting persuasion dynamics from multi-turn conversations.\n\\newblock \\emph{arXiv preprint arXiv:2508.05625}, 2025.\n\n\\bibitem[Cialdini(2001)]{cialdini2001science}\nR.~B. Cialdini.\n\\newblock \\emph{Influence: Science and Practice}.\n\\newblock Allyn \\& Bacon, 4th edition, 2001.\n\n\\bibitem[Hagendorff(2026)]{hagendorff2026nature}\nT.~Hagendorff.\n\\newblock Persuasion strategies in adversarial conversations with large language models.\n\\newblock \\emph{Nature Communications}, 2026.\n\n\\bibitem[He et~al.(2021)]{he2021debertav3}\nP.~He, J.~Gao, and W.~Chen.\n\\newblock {DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-style pre-training with gradient-disentangled embedding sharing.\n\\newblock \\emph{arXiv preprint arXiv:2111.09543}, 2021.\n\n\\bibitem[Inan et~al.(2023)]{inan2023llama}\nH.~Inan, K.~Upasani, J.~Chi, R.~Rungta, K.~Iyer, Y.~Mao, M.~Tontchev, Q.~Hu, B.~Fuller, D.~Testuggine, and M.~Khabsa.\n\\newblock {Llama Guard}: {LLM}-based input-output safeguard for human-{AI} conversations.\n\\newblock \\emph{arXiv preprint arXiv:2312.06674}, 2023.\n\n\\bibitem[Jiang et~al.(2024)]{jiang2024deceptive}\nY.~Jiang, H.~Zhang, and others.\n\\newblock Deceptive delight: Jailbreaking {LLMs} through camouflaged content mixing.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Russinovich and Salem(2024)]{russinovich2024greatnow}\nM.~Russinovich and A.~Salem.\n\\newblock Great, now write an article about that: The crescendo multi-turn {LLM} jailbreak attack.\n\\newblock \\emph{arXiv preprint arXiv:2404.01833}, 2024.\n\n\\bibitem[Searle(1969)]{searle1969speech}\nJ.~R. Searle.\n\\newblock \\emph{Speech Acts: An Essay in the Philosophy of Language}.\n\\newblock Cambridge University Press, 1969.\n\n\\bibitem[Su et~al.(2026)]{su2026deepcontext}\nY.~Su, R.~Wang, and others.\n\\newblock {DeepContext}: Temporal semantic drift tracking for multi-turn jailbreak detection.\n\\newblock \\emph{Preprint}, 2026.\n\n\\bibitem[Zeng et~al.(2024)]{zeng2024persuasion}\nY.~Zeng, H.~Lin, J.~Zhang, D.~Yang, R.~Jia, and W.~Shi.\n\\newblock How {J}ohnny can persuade {LLMs} to jailbreak them: Rethinking persuasion to challenge {AI} safety by humanizing {LLMs}.\n\\newblock In \\emph{Proceedings of ACL}, 2024.\n\n\\bibitem[Zhao et~al.(2024)]{zhao2024wildchat}\nW.~Zhao, J.~Ren, B.~Li, and others.\n\\newblock {WildChat}: 1{M} chat{GPT} interaction logs in the wild.\n\\newblock In \\emph{Proceedings of ICLR}, 2024.\n\n\\bibitem[Zhou et~al.(2024)]{zhou2024speak}\nZ.~Zhou, Y.~Guo, and others.\n\\newblock Speak out of turn: Safety vulnerability of large language models in multi-turn dialogue.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8119d835-21d1-46c8-8c8c-b3858d7a29bb",
  "isSidechain": false,
  "requestId": "req_011Cb8WkJJeJdUVZmewWNBkC",
  "type": "assistant",
  "uuid": "60397cdd-830a-47ab-8db8-31e989096250",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMPQ78yT5ZXBhC3QgEXQbA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 220,
      "cache_read_input_tokens": 38429,
      "output_tokens": 11941,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 220,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11941,
          "cache_read_input_tokens": 38429,
          "cache_creation_input_tokens": 220,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 220
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

_source line 21 · 2026-05-17T17:15:11.682Z_

<details><summary>↩ Tool result · `toolu_01AtNmfQFKW6LW8Nxv4wsPnQ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60397cdd-830a-47ab-8db8-31e989096250",
  "isSidechain": false,
  "promptId": "0640bae5-48d0-4296-855e-879e96111727",
  "type": "user",
  "uuid": "d2d81ea5-a19a-438d-ab4c-45e716c2eb96",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\n\\title{DisPeD: Exploiting the Pragmatic Evasion Asymmetry\\\\for Robust Multi-Turn Jailbreak Detection}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nMulti-turn jailbreak attacks against Large Language Models (LLMs) distribute adversarial intent across individually benign turns, defeating detectors that operate at the lexical or semantic level. We identify a \\emph{Pragmatic Evasion Asymmetry}: attackers can freely paraphrase surface content, but the underlying persuasion playbook (rapport building, reframing, escalation) is a structural prerequisite for attack success and cannot be removed without abandoning the attack itself. DisPeD exploits this asymmetry by fine-tuning DeBERTa on an 8-class persuasion strategy taxonomy to produce pragmatic-aware turn embeddings, then modeling the temporal strategy sequence with a GRU for conversation-level classification. On register-normalized data that eliminates lexical shortcuts (TF-IDF reduced from 1.0 to 0.58), DisPeD achieves F1\\,=\\,0.91 at only $K$\\,=\\,2 turns, a 14 percentage point (pp) improvement over a vanilla semantic baseline ($p$\\,<\\,0.001). Under adversarial paraphrasing, DisPeD degrades by only 3\\,pp while semantic and lexical baselines degrade by 13\\,pp and 18\\,pp respectively. A model trained exclusively on Crescendo-style attacks generalizes zero-shot to Foot-in-the-Door and Deceptive Delight attacks with an average F1 of 0.85, outperforming the semantic baseline by 16.5\\,pp. These results establish that discourse-level persuasion patterns provide a robust and generalizable signal for early multi-turn jailbreak detection.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nMulti-turn jailbreak attacks pose a growing threat to deployed LLMs. Attacks such as Crescendo~\\citep{russinovich2024greatnow}, Foot-in-the-Door (FITD)~\\citep{zhou2024speak}, and Deceptive Delight~\\citep{jiang2024deceptive} distribute adversarial intent across multiple conversational turns, each of which appears benign in isolation. \\citet{bullwinkel2025multiturn} show that per-turn representations of these attacks are deliberately kept in a ``benign'' region of embedding space, causing representation-level defenses to fail with a 50-point ASR gap. Temporal approaches that track generic semantic drift~\\citep{su2026deepcontext} confuse benign conversational evolution with adversarial manipulation, producing high false-positive rates.\n\nWhy are these attacks so effective? A multi-turn attacker must accomplish two things: (1) maintain surface-level benignity on each turn, and (2) gradually steer the model toward compliance through a persuasion playbook. \\citet{zeng2024persuasion} and \\citet{hagendorff2026nature} independently show that identifiable persuasion strategies appear in over 97\\% of successful multi-turn attacks. The attacker has enormous freedom in choosing \\emph{what words} to use (lexical level) and \\emph{what topics} to discuss (semantic level), but the underlying \\emph{pragmatic function} of each turn (rapport building, authority appeal, reframing) is constrained by the attack's functional requirements.\n\nThis observation motivates what we call the \\textbf{Pragmatic Evasion Asymmetry}: an evasion hierarchy exists in which lexical features are easily evaded via paraphrasing, semantic embeddings are moderately robust but still vulnerable to per-turn content manipulation, and pragmatic persuasion patterns are structurally difficult to evade because they constitute the functional mechanism of the attack. In the terminology of Speech Act Theory~\\citep{austin1962things,searle1969speech}, existing detectors operate at the locutionary act level (what was said), while DisPeD operates at the illocutionary act level (what was done).\n\nWe present \\textbf{DisPeD} (\\textbf{Dis}course-level \\textbf{Pe}rsuasion \\textbf{D}etector), a two-stage pipeline that first fine-tunes DeBERTa-v3-base~\\citep{he2021debertav3} on a multi-task objective combining 8-class persuasion strategy classification and binary intent classification, then feeds the resulting turn embeddings into a bidirectional GRU for conversation-level jailbreak detection. By grounding turn representations in a persuasion taxonomy derived from Cialdini's influence principles~\\citep{cialdini2001science}, DisPeD detects the characteristic escalation trajectory of multi-turn attacks at the earliest possible stage.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item We formalize the \\emph{Pragmatic Evasion Asymmetry} and provide empirical evidence through a three-tier robustness experiment: under adversarial paraphrasing, DisPeD (pragmatic) degrades by 3\\,pp, a vanilla semantic baseline by 13\\,pp, and a TF-IDF lexical baseline by 18\\,pp (Section~\\ref{sec:evasion}).\n    \\item We demonstrate that persuasion-grounded embeddings enable significantly earlier detection: F1\\,=\\,0.91 at $K$\\,=\\,2 turns versus 0.77 for the semantic baseline, a 14\\,pp advantage that holds across attack types with zero-shot cross-attack transfer averaging 16.5\\,pp improvement (Sections~\\ref{sec:main_results} and~\\ref{sec:cross_attack}).\n    \\item We provide a mechanistic analysis showing that jailbreak conversations exhibit monotonic escalation trajectories in persuasion strategy space (monotonicity score 0.82 vs. 0.34 for benign), explaining why pragmatic features succeed where semantic features fail (Section~\\ref{sec:trajectory}).\n\\end{enumerate}\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Multi-turn jailbreak attacks.}\nCrescendo~\\citep{russinovich2024greatnow} gradually escalates through conversational rapport, achieving high attack success rates against commercial LLMs. FITD~\\citep{zhou2024speak} applies the foot-in-the-door compliance technique, starting with small requests and progressively increasing severity. Deceptive Delight~\\citep{jiang2024deceptive} interleaves harmful content within benign creative writing frames. These attacks share a common structure: a persuasion playbook that transitions from trust-building to explicit elicitation across turns. \\citet{hagendorff2026nature} analyze persuasion strategies in adversarial conversations and find identifiable patterns in 97\\% of successful attacks, confirming that the persuasion structure is systematic rather than incidental.\n\n\\paragraph{Jailbreak detection.}\nSingle-turn detectors such as perplexity filters~\\citep{alon2023detecting} and input classifiers~\\citep{inan2023llama} fail against multi-turn attacks because individual turns appear benign. \\citet{bullwinkel2025multiturn} demonstrate that per-turn representations are deliberately maintained in benign embedding regions. DeepContext~\\citep{su2026deepcontext} addresses this by tracking semantic drift across turns with an encoder-RNN pipeline, but uses generic embeddings that conflate benign topic evolution with adversarial manipulation.\n\n\\paragraph{Persuasion and LLM safety.}\n\\citet{zeng2024persuasion} compile 40 persuasion techniques used in jailbreaking and show that persuasion-augmented prompts significantly increase ASR. \\citet{chen2025persuade} study how LLMs deploy persuasion strategies during multi-turn interactions, demonstrating that persuasion dynamics are extractable from turn-level representations. Our work is the first to use persuasion-grounded representations for jailbreak \\emph{detection} rather than attack construction or analysis.\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\nDisPeD consists of two stages: a persuasion-grounded encoder and a temporal sequence classifier.\n\n\\subsection{Stage 1: Persuasion-Grounded Encoder}\n\nWe fine-tune DeBERTa-v3-base on a multi-task objective with two heads:\n\n\\begin{itemize}\n    \\item \\textbf{Persuasion strategy classification} (8 classes): rapport building, authority appeal, reciprocity, social proof, commitment/consistency, scarcity/urgency, reframing, and direct request. These categories are derived from Cialdini's principles of influence~\\citep{cialdini2001science} and adapted for adversarial conversational contexts following \\citet{zeng2024persuasion}. Benign turns lacking a persuasion function receive a ``none'' label.\n    \\item \\textbf{Intent classification} (binary): whether the turn carries jailbreak intent.\n\\end{itemize}\n\nThe total loss is $\\mathcal{L} = \\mathcal{L}_{\\text{persuasion}} + \\lambda \\mathcal{L}_{\\text{intent}}$, where $\\lambda = 1.0$. After training, we extract the [CLS] embedding from the fine-tuned encoder as the persuasion-grounded turn representation. The encoder achieves 79\\% accuracy on 8-class persuasion classification and 94\\% on binary intent classification (Table~\\ref{tab:encoder}).\n\n\\subsection{Stage 2: Temporal Sequence Classification}\n\nGiven a conversation of $K$ turns, we obtain turn embeddings $\\{e_1, \\ldots, e_K\\}$ from the Stage 1 encoder. A bidirectional GRU processes the embedding sequence and outputs a conversation-level binary classification (jailbreak vs. benign) from the final hidden state. This architecture captures the temporal progression of persuasion strategies across turns.\n\n\\subsection{Baselines}\n\nWe compare DisPeD against three baselines spanning the evasion hierarchy:\n\\begin{itemize}\n    \\item \\textbf{TF-IDF + Logistic Regression}: a lexical baseline operating on bag-of-words features.\n    \\item \\textbf{DeBERTa Semantic Baseline}: the same Stage 2 GRU pipeline but with \\emph{vanilla} (not fine-tuned) DeBERTa embeddings, representing semantic-level detection.\n    \\item \\textbf{DeepContext Proxy}: BERT-base + GRU, simulating the DeepContext architecture with generic drift features and no persuasion grounding.\n\\end{itemize}\n\n% ============================================================\n% 4. EXPERIMENTAL SETUP\n% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\subsection{Data Preparation and Register Normalization}\n\\label{sec:data}\n\nOur dataset consists of 480 conversations (240 jailbreak, 240 benign) with 72 held out for testing. Jailbreak conversations are Crescendo-style multi-turn attacks; benign conversations are drawn from standard conversational corpora and WildChat~\\citep{zhao2024wildchat}.\n\nA critical challenge in multi-turn jailbreak detection is \\emph{lexical shortcut}: scripted attack dialogues have distributional properties distinct from naturalistic benign conversations, allowing simple bag-of-words classifiers to succeed without learning meaningful features. On our original data, TF-IDF separability was 1.0, indicating complete lexical shortcut.\n\nWe apply register normalization using LLM paraphrasing to convert jailbreak turns from formal/scripted register to conversational register, eliminating the distributional gap. Table~\\ref{tab:tfidf_diagnostic} confirms the effectiveness of this procedure: TF-IDF drops from 1.0 to 0.58, below our hard gate of 0.75 but above the random baseline of 0.50, reflecting residual functional vocabulary (e.g., ``hypothetical,'' ``scenario'') that attackers cannot entirely avoid. Persuasion strategy annotations are preserved at 94\\% after normalization, confirming that the persuasion structure is a discourse-level phenomenon independent of lexical realization.\n\n\\begin{table}[t]\n\\centering\n\\caption{TF-IDF separability before and after register normalization.}\n\\label{tab:tfidf_diagnostic}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{TF-IDF} & \\textbf{Vocab Overlap (\\%)} \\\\\n\\midrule\nOriginal data & 1.00 & 12.3 \\\\\nRegister-normalized & 0.58 & 41.7 \\\\\nRandom baseline & 0.50 & 50.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Attack Dataset}\n\\label{sec:multi_attack_data}\n\nTo evaluate cross-attack generalization (Section~\\ref{sec:cross_attack}), we generate additional attack conversations in two families beyond Crescendo using Qwen3-8B: 72 FITD-style conversations (avg. 6.8 turns) employing the foot-in-the-door compliance escalation pattern, and 65 Deceptive Delight-style conversations (avg. 5.2 turns) interleaving harmful content within benign frames. All generated conversations receive persuasion strategy annotations with 91\\% LLM annotation consistency. Table~\\ref{tab:attack_stats} summarizes the dataset statistics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Attack type statistics. TF-IDF measured against benign conversations.}\n\\label{tab:attack_stats}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Attack Type} & \\textbf{$n$} & \\textbf{Avg Turns} & \\textbf{Turn Range} & \\textbf{TF-IDF} \\\\\n\\midrule\nCrescendo (original) & 240 & 5.5 & 3--12 & 0.58 \\\\\nFITD (generated) & 72 & 6.8 & 4--10 & 0.61 \\\\\nDeceptive Delight (generated) & 65 & 5.2 & 3--8 & 0.55 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe three attack types share the same persuasion strategy vocabulary but differ in temporal arrangement. As shown in Table~\\ref{tab:strategy_dist}, FITD relies heavily on reciprocity (30\\%) and commitment/consistency (25\\%), reflecting its gradual compliance escalation. Deceptive Delight favors authority appeal (22\\%) and social proof (18\\%), using authoritative framing to embed harmful content. Crescendo is more evenly distributed across strategies. This variation in strategy profiles, combined with a shared underlying vocabulary, provides the conditions for testing zero-shot cross-attack transfer.\n\n\\begin{table}[t]\n\\centering\n\\caption{Persuasion strategy distribution (\\%) by attack type.}\n\\label{tab:strategy_dist}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Crescendo} & \\textbf{FITD} & \\textbf{Dec. Delight} \\\\\n\\midrule\nRapport building & 28 & 35 & 15 \\\\\nAuthority appeal & 12 & 8 & 22 \\\\\nReciprocity & 18 & 30 & 10 \\\\\nSocial proof & 8 & 5 & 18 \\\\\nCommitment/consistency & 15 & 25 & 8 \\\\\nScarcity/urgency & 5 & 3 & 12 \\\\\nReframing & 22 & 15 & 20 \\\\\nDirect request & 7 & 4 & 15 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 5. RESULTS\n% ============================================================\n\\section{Results}\n\n\\subsection{Main Results: Early Detection on Clean Data}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents the core comparison between DisPeD and the semantic baseline across turn budgets on register-normalized data. DisPeD achieves F1\\,=\\,0.91 at $K$\\,=\\,2 turns, a 14\\,pp improvement over the semantic baseline (0.77, $p$\\,<\\,0.001 by bootstrap test). The advantage is largest at early turn budgets ($K$\\,=\\,1--2) and narrows at higher $K$ as the baseline accumulates sufficient semantic drift signal, converging to a 7\\,pp gap on full conversations.\n\n\\begin{table}[t]\n\\centering\n\\caption{F1 by turn budget on clean (register-normalized) data. $\\Delta$ is the improvement of DisPeD over the semantic baseline in percentage points. All $p$-values by bootstrap test.}\n\\label{tab:main_results}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$K$} & \\textbf{DisPeD} & \\textbf{Baseline} & \\textbf{$\\Delta$ (pp)} & \\textbf{$p$} \\\\\n\\midrule\n1 & 0.82 & 0.68 & 14 & 0.003 \\\\\n2 & 0.91 & 0.77 & 14 & 0.001 \\\\\n3 & 0.93 & 0.83 & 10 & 0.004 \\\\\n5 & 0.96 & 0.88 & 8 & 0.012 \\\\\nAll & 0.96 & 0.89 & 7 & 0.018 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $K$\\,=\\,2, DisPeD also achieves a substantially lower false-positive rate at 95\\% TPR: FPR\\,=\\,0.08 versus 0.19 for the baseline. This early detection capability is the headline result: persuasion strategy transitions (e.g., rapport building to authority framing) manifest within the first two turns, providing discriminative signal before explicitly harmful content appears.\n\nTable~\\ref{tab:encoder} reports the Stage 1 encoder metrics. The 79\\% persuasion classification accuracy (macro F1\\,=\\,0.74) confirms that the encoder learns meaningful persuasion representations rather than noise, while the 94\\% intent accuracy validates the multi-task training.\n\n\\begin{table}[t]\n\\centering\n\\caption{DeBERTa encoder metrics on clean data.}\n\\label{tab:encoder}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nPersuasion 8-class accuracy & 0.79 \\\\\nPersuasion macro F1 & 0.74 \\\\\nIntent binary accuracy & 0.94 \\\\\nBest epoch & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pragmatic Evasion Asymmetry}\n\\label{sec:evasion}\n\nTo empirically validate the Pragmatic Evasion Asymmetry, we apply aggressive paraphrasing (synonym substitution, sentence restructuring) to jailbreak conversations and measure detection degradation across four model tiers. Table~\\ref{tab:evasion_full} reports results on full conversations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Evasion hierarchy under adversarial paraphrasing (full conversation). Models ordered by abstraction level. Drop is the F1 degradation in percentage points.}\n\\label{tab:evasion_full}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{F1 (Clean)} & \\textbf{F1 (Perturbed)} & \\textbf{Drop (pp)} \\\\\n\\midrule\nDisPeD (pragmatic) & 0.96 & 0.93 & 3 \\\\\nDeBERTa baseline (semantic) & 0.89 & 0.76 & 13 \\\\\nDeepContext proxy (generic temporal) & 0.84 & 0.69 & 15 \\\\\nTF-IDF + LR (lexical) & 0.72 & 0.54 & 18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe results reveal a clear three-tier gradient aligned with the predicted evasion hierarchy. TF-IDF collapses under perturbation ($-$18\\,pp) because synonym substitution directly destroys the lexical features it relies on. The DeepContext proxy degrades by 15\\,pp because BERT-base representations partially depend on surface patterns. The semantic baseline degrades moderately ($-$13\\,pp) as contextual embeddings are disrupted by token-level changes even when meaning is largely preserved. DisPeD degrades minimally ($-$3\\,pp) because persuasion-grounded representations encode illocutionary acts that are invariant to paraphrasing: ``building rapport through self-disclosure'' retains its pragmatic function regardless of lexical realization.\n\nA particularly strong result: DisPeD under adversarial perturbation (F1\\,=\\,0.93) still outperforms the semantic baseline on \\emph{unperturbed} data (F1\\,=\\,0.89). Table~\\ref{tab:evasion_k2} shows that this pattern holds at $K$\\,=\\,2, where DisPeD maintains F1\\,=\\,0.87 versus 0.63 for the semantic baseline.\n\n\\begin{table}[t]\n\\centering\n\\caption{Evasion hierarchy at $K$\\,=\\,2 turns.}\n\\label{tab:evasion_k2}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{F1 Clean} & \\textbf{F1 Perturbed} & \\textbf{Drop (pp)} \\\\\n\\midrule\nDisPeD & 0.91 & 0.87 & 4 \\\\\nDeBERTa baseline & 0.77 & 0.63 & 14 \\\\\nTF-IDF + LR & 0.65 & 0.48 & 17 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Ablation: Scrambled Label Analysis}\n\\label{sec:ablation}\n\nTo confirm that the advantage of DisPeD comes from the \\emph{semantic content} of persuasion labels rather than the fine-tuning process itself, we retrain the encoder with randomly scrambled persuasion strategy labels (intent labels remain intact). Table~\\ref{tab:scrambled} shows that scrambling causes a 15\\,pp drop at $K$\\,=\\,2, bringing performance close to the vanilla baseline (0.76 vs. 0.77). The scrambled encoder's persuasion classification accuracy drops to 0.13 ($\\approx 1/8$ random chance), confirming that the label signal is destroyed. This ablation establishes a causal link: the discriminative power of DisPeD derives from the semantic content of persuasion strategy annotations, not from any incidental benefit of multi-task training.\n\n\\begin{table}[t]\n\\centering\n\\caption{Effect of scrambling persuasion strategy labels. Drop is relative to properly labeled DisPeD.}\n\\label{tab:scrambled}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{$K$} & \\textbf{Proper Labels} & \\textbf{Scrambled Labels} & \\textbf{Drop (pp)} \\\\\n\\midrule\n2 & 0.91 & 0.76 & 15 \\\\\n3 & 0.93 & 0.81 & 12 \\\\\nAll & 0.96 & 0.87 & 9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Attack Zero-Shot Generalization}\n\\label{sec:cross_attack}\n\nA model trained exclusively on Crescendo-style attacks is evaluated zero-shot on FITD and Deceptive Delight attacks. Table~\\ref{tab:cross_attack} presents the results. DisPeD achieves an average F1 of 0.85 on unseen attack types, outperforming the semantic baseline by 16.5\\,pp. DisPeD on unseen attacks (0.85) approaches the semantic baseline on \\emph{seen} attacks (0.89), demonstrating that persuasion-grounded representations capture attack-type-agnostic pragmatic signals.\n\n\\begin{table}[t]\n\\centering\n\\caption{Zero-shot cross-attack generalization (full conversation). The model is trained on Crescendo only.}\n\\label{tab:cross_attack}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Attack Type} & \\textbf{DisPeD} & \\textbf{Baseline} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nFITD & 0.84 & 0.67 & 17 \\\\\nDeceptive Delight & 0.86 & 0.70 & 16 \\\\\nCrescendo (held-out) & 0.96 & 0.89 & 7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_attack_k2} reports early detection on unseen attacks. At $K$\\,=\\,2, DisPeD achieves recall of 0.78 on FITD and 0.81 on Deceptive Delight, versus 0.55 and 0.58 for the baseline.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-attack early detection recall at $K$\\,=\\,2.}\n\\label{tab:cross_attack_k2}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Attack Type} & \\textbf{DisPeD Recall} & \\textbf{Baseline Recall} \\\\\n\\midrule\nFITD & 0.78 & 0.55 \\\\\nDeceptive Delight & 0.81 & 0.58 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe transfer works because all three attack types share the same persuasion strategy vocabulary (Table~\\ref{tab:strategy_dist}), differing only in temporal arrangement. The GRU learns a generic ``persuasion escalation'' detector rather than Crescendo-specific surface patterns. Deceptive Delight transfers slightly better (0.86 vs. 0.84) because its strategy profile (strong reframing component) more closely resembles Crescendo's distribution.\n\n\\subsection{Mechanistic Analysis: Escalation Trajectories}\n\\label{sec:trajectory}\n\nTo provide a mechanistic explanation for why pragmatic features succeed, we analyze persuasion strategy transition patterns. Table~\\ref{tab:trajectory} reports two quantitative metrics distinguishing jailbreak from benign conversations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Strategy transition statistics. Monotonicity measures the fraction of transitions along the escalation direction. Entropy measures the diversity of transition types.}\n\\label{tab:trajectory}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Type} & \\textbf{Transition Entropy} & \\textbf{Monotonicity} & \\textbf{$n$} \\\\\n\\midrule\nJailbreak & 1.8 & 0.82 & 240 \\\\\nBenign & 2.9 & 0.34 & 240 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nJailbreak conversations exhibit highly monotonic escalation (score 0.82): 82\\% of strategy transitions move from lower-risk to higher-risk categories (e.g., rapport building $\\to$ commitment/consistency $\\to$ reframing $\\to$ direct request). Benign conversations show near-random monotonicity (0.34) with oscillatory, task-driven patterns. Transition entropy is lower for jailbreaks (1.8 vs. 2.9) because attackers follow a concentrated playbook, while benign conversations traverse a wider range of pragmatic functions.\n\nTable~\\ref{tab:dominant_sequences} shows the most frequent strategy sequences. Jailbreak conversations converge on a small number of escalation trajectories (top-3 covering 74\\% of cases), while benign conversations are dominated by ``none'' labels (45\\%) reflecting the absence of persuasion intent. The trajectory-only separability (AUROC\\,=\\,0.91) confirms that the escalation pattern alone, without any content features, is strongly discriminative.\n\n\\begin{table}[t]\n\\centering\n\\caption{Top-3 dominant strategy sequences by conversation type.}\n\\label{tab:dominant_sequences}\n\\small\n\\begin{tabular}{clcclc}\n\\toprule\n & \\textbf{Jailbreak Sequence} & \\textbf{\\%} & & \\textbf{Benign Sequence} & \\textbf{\\%} \\\\\n\\midrule\n1 & rapport$\\to$commit$\\to$reframe$\\to$direct & 34 & 1 & none$\\to$none$\\to$none$\\to$none & 45 \\\\\n2 & rapport$\\to$social$\\to$reframe$\\to$direct & 22 & 2 & rapport$\\to$none$\\to$rapport$\\to$none & 18 \\\\\n3 & rapport$\\to$reciprocity$\\to$commit$\\to$direct & 18 & 3 & none$\\to$rapport$\\to$none$\\to$direct & 12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Robustness on Hard Negatives}\n\\label{sec:hard_negatives}\n\nA potential concern is that DisPeD might flag benign conversations with high topic diversity as jailbreaks. We evaluate on hard negatives from WildChat~\\citep{zhao2024wildchat}: 120 high-drift benign conversations where users shift across multiple domains (e.g., coding to personal advice to creative writing). We filter 15.2\\% of WildChat conversations as potential contamination.\n\n\\begin{table}[t]\n\\centering\n\\caption{False-positive rate on hard negatives (high-drift benign) vs. random benign.}\n\\label{tab:hard_negatives}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{FPR (Hard)} & \\textbf{FPR (Random)} & \\textbf{$\\Delta$} \\\\\n\\midrule\nDisPeD & 0.09 & 0.03 & 0.06 \\\\\nDeBERTa baseline & 0.17 & 0.06 & 0.11 \\\\\nTF-IDF + LR & 0.22 & 0.08 & 0.14 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:hard_negatives} shows that DisPeD maintains a low FPR of 9\\% on hard negatives, compared to 17\\% for the semantic baseline and 22\\% for TF-IDF. The persuasion-grounded representations distinguish ``topic drift'' (benign, oscillatory strategy transitions) from ``strategy escalation'' (adversarial, monotonic trajectory), a distinction that semantic embeddings cannot reliably make.\n\n\\subsection{Lexical Baseline Analysis}\n\\label{sec:lexical}\n\nTable~\\ref{tab:tfidf_performance} reports the TF-IDF + Logistic Regression baseline on clean data. Even after register normalization, residual lexical signal provides above-chance performance (F1\\,=\\,0.72) due to functional vocabulary that attackers cannot entirely avoid. The top discriminative features (Table~\\ref{tab:top_features}) confirm this: jailbreak-indicative words (``hypothetical,'' ``scenario,'' ``imagine'') are framing devices required by the attack structure. This residual lexical signal (F1\\,=\\,0.72) falls far short of what pragmatic features achieve (F1\\,=\\,0.96) and collapses under adversarial perturbation (F1\\,=\\,0.54).\n\n\\begin{table}[t]\n\\centering\n\\caption{TF-IDF + LR performance by turn budget on clean data.}\n\\label{tab:tfidf_performance}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{$K$} & \\textbf{F1} & \\textbf{Precision} & \\textbf{Recall} \\\\\n\\midrule\n2 & 0.65 & 0.68 & 0.62 \\\\\n3 & 0.68 & 0.71 & 0.65 \\\\\n5 & 0.70 & 0.73 & 0.68 \\\\\nAll & 0.72 & 0.75 & 0.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Top-5 discriminative features by LR coefficient.}\n\\label{tab:top_features}\n\\begin{tabular}{clccl c}\n\\toprule\n\\textbf{Rank} & \\textbf{Jailbreak Feature} & \\textbf{Weight} & & \\textbf{Benign Feature} & \\textbf{Weight} \\\\\n\\midrule\n1 & hypothetical & 2.31 & & thanks & 1.89 \\\\\n2 & scenario & 1.95 & & help & 1.72 \\\\\n3 & imagine & 1.87 & & question & 1.54 \\\\\n4 & creative & 1.62 & & code & 1.41 \\\\\n5 & roleplay & 1.48 & & explain & 1.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Checkpoint Sensitivity}\n\\label{sec:checkpoint}\n\nTo assess reproducibility on our relatively small dataset, we evaluate DisPeD with DeBERTa encoders from different training epochs. Table~\\ref{tab:checkpoint} shows that downstream F1 varies by at most 1\\,pp across checkpoints, indicating that the results are robust to encoder training stochasticity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Checkpoint sensitivity analysis.}\n\\label{tab:checkpoint}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Checkpoint} & \\textbf{Persuasion Acc} & \\textbf{Intent Acc} & \\textbf{F1 (Full)} & \\textbf{F1 ($K$=2)} \\\\\n\\midrule\nEpoch 2 & 0.76 & 0.93 & 0.94 & 0.89 \\\\\nEpoch 3 & 0.79 & 0.94 & 0.96 & 0.91 \\\\\nEpoch final & 0.78 & 0.94 & 0.95 & 0.90 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 6. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why pragmatic features are structurally robust.}\nThe Pragmatic Evasion Asymmetry is not merely an empirical observation but follows from the functional requirements of multi-turn attacks. An attacker who removes rapport building cannot establish the trust needed for later compliance. An attacker who skips reframing cannot normalize the harmful request. An attacker who eliminates all escalation has, by definition, not conducted a multi-turn attack. Each persuasion strategy serves a necessary function in the attack pipeline, and our experiments confirm that this structural constraint translates into measurably robust detection features.\n\n\\paragraph{Limitations.}\nOur dataset is small (480 conversations) and the generated attack conversations may not capture the full diversity of real-world adversarial behavior. The persuasion taxonomy is limited to 8 categories; a finer-grained taxonomy might capture additional discriminative patterns. We do not evaluate against attacks that deliberately target the persuasion detection mechanism (adaptive adversaries aware of DisPeD). Human evaluation of the interpretability of strategy trajectories remains future work. Our scope is limited to persuasion-mediated multi-turn attacks; pure information accumulation attacks, token smuggling, and single-turn roleplay jailbreaks fall outside our detection target.\n\n% ============================================================\n% 7. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe introduced DisPeD, a multi-turn jailbreak detector that exploits the Pragmatic Evasion Asymmetry by grounding turn representations in a persuasion strategy taxonomy. Our experiments on register-normalized data demonstrate three key findings: (1) pragmatic features degrade minimally under adversarial paraphrasing (3\\,pp) compared to semantic (13\\,pp) and lexical (18\\,pp) features; (2) persuasion-grounded embeddings enable early detection at $K$\\,=\\,2 turns with 14\\,pp improvement over semantic baselines, an advantage that transfers zero-shot across attack families; and (3) the mechanistic basis for this advantage is the monotonic escalation trajectory in persuasion strategy space that characterizes multi-turn attacks. These results suggest that discourse-level pragmatic analysis is a promising direction for building jailbreak defenses that are robust to surface-level evasion.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Alon and Kamfonas(2023)]{alon2023detecting}\nG.~Alon and M.~Kamfonas.\n\\newblock Detecting language model attacks with perplexity.\n\\newblock \\emph{arXiv preprint arXiv:2308.14132}, 2023.\n\n\\bibitem[Austin(1962)]{austin1962things}\nJ.~L. Austin.\n\\newblock \\emph{How to Do Things with Words}.\n\\newblock Oxford University Press, 1962.\n\n\\bibitem[Bullwinkel et~al.(2025)]{bullwinkel2025multiturn}\nS.~Bullwinkel, P.~Schramowski, and K.~Kersting.\n\\newblock Multi-turn jailbreaks hide in the representation space.\n\\newblock \\emph{arXiv preprint arXiv:2507.02956}, 2025.\n\n\\bibitem[Chen et~al.(2025)]{chen2025persuade}\nW.~Chen, Y.~Li, and R.~Jia.\n\\newblock How do {LLMs} persuade? {E}xtracting persuasion dynamics from multi-turn conversations.\n\\newblock \\emph{arXiv preprint arXiv:2508.05625}, 2025.\n\n\\bibitem[Cialdini(2001)]{cialdini2001science}\nR.~B. Cialdini.\n\\newblock \\emph{Influence: Science and Practice}.\n\\newblock Allyn \\& Bacon, 4th edition, 2001.\n\n\\bibitem[Hagendorff(2026)]{hagendorff2026nature}\nT.~Hagendorff.\n\\newblock Persuasion strategies in adversarial conversations with large language models.\n\\newblock \\emph{Nature Communications}, 2026.\n\n\\bibitem[He et~al.(2021)]{he2021debertav3}\nP.~He, J.~Gao, and W.~Chen.\n\\newblock {DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-style pre-training with gradient-disentangled embedding sharing.\n\\newblock \\emph{arXiv preprint arXiv:2111.09543}, 2021.\n\n\\bibitem[Inan et~al.(2023)]{inan2023llama}\nH.~Inan, K.~Upasani, J.~Chi, R.~Rungta, K.~Iyer, Y.~Mao, M.~Tontchev, Q.~Hu, B.~Fuller, D.~Testuggine, and M.~Khabsa.\n\\newblock {Llama Guard}: {LLM}-based input-output safeguard for human-{AI} conversations.\n\\newblock \\emph{arXiv preprint arXiv:2312.06674}, 2023.\n\n\\bibitem[Jiang et~al.(2024)]{jiang2024deceptive}\nY.~Jiang, H.~Zhang, and others.\n\\newblock Deceptive delight: Jailbreaking {LLMs} through camouflaged content mixing.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Russinovich and Salem(2024)]{russinovich2024greatnow}\nM.~Russinovich and A.~Salem.\n\\newblock Great, now write an article about that: The crescendo multi-turn {LLM} jailbreak attack.\n\\newblock \\emph{arXiv preprint arXiv:2404.01833}, 2024.\n\n\\bibitem[Searle(1969)]{searle1969speech}\nJ.~R. Searle.\n\\newblock \\emph{Speech Acts: An Essay in the Philosophy of Language}.\n\\newblock Cambridge University Press, 1969.\n\n\\bibitem[Su et~al.(2026)]{su2026deepcontext}\nY.~Su, R.~Wang, and others.\n\\newblock {DeepContext}: Temporal semantic drift tracking for multi-turn jailbreak detection.\n\\newblock \\emph{Preprint}, 2026.\n\n\\bibitem[Zeng et~al.(2024)]{zeng2024persuasion}\nY.~Zeng, H.~Lin, J.~Zhang, D.~Yang, R.~Jia, and W.~Shi.\n\\newblock How {J}ohnny can persuade {LLMs} to jailbreak them: Rethinking persuasion to challenge {AI} safety by humanizing {LLMs}.\n\\newblock In \\emph{Proceedings of ACL}, 2024.\n\n\\bibitem[Zhao et~al.(2024)]{zhao2024wildchat}\nW.~Zhao, J.~Ren, B.~Li, and others.\n\\newblock {WildChat}: 1{M} chat{GPT} interaction logs in the wild.\n\\newblock In \\emph{Proceedings of ICLR}, 2024.\n\n\\bibitem[Zhou et~al.(2024)]{zhou2024speak}\nZ.~Zhou, Y.~Guo, and others.\n\\newblock Speak out of turn: Safety vulnerability of large language models in multi-turn dialogue.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "60397cdd-830a-47ab-8db8-31e989096250",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165817 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_ja…",
  "leafUuid": "d2d81ea5-a19a-438d-ab4c-45e716c2eb96",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated jailbreak detection research paper",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90"
}
```

---

### Tool call

_source line 24 · 2026-05-17T17:15:15.926Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01S58yAx1AciF3JmwxtPeyUS`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2d81ea5-a19a-438d-ab4c-45e716c2eb96",
  "isSidechain": false,
  "requestId": "req_011Cb8X1D4JFou7FbuDq5Loo",
  "type": "assistant",
  "uuid": "12e4227d-6401-496d-b0c7-880d0b5f34c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XP2P1SVd81F259kg6PWPp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12011,
      "cache_read_input_tokens": 38649,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12011,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 38649,
          "cache_creation_input_tokens": 12011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12011
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

_source line 25 · 2026-05-17T17:15:17.713Z_

<details><summary>↩ Tool result · `toolu_01S58yAx1AciF3JmwxtPeyUS`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
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

Package natbib Warning: Citation `russinovich2024greatnow' on page 1 undefined 
on input line 35.


Package natbib Warning: Citation `zhou2024speak' on page 1 undefined on input l
ine 35.


Package natbib Warning: Citation `jiang2024deceptive' on page 1 undefined on in
put line 35.


Package natbib Warning: Citation `bullwinkel2025multiturn' on page 1 undefined 
on input line 35.


Package natbib Warning: Citation `su2026deepcontext' on page 1 undefined on inp
ut line 35.


Overfull \hbox (13.75723pt too wide) in paragraph at lines 35--36
\T1/cmr/m/n/10.95 Multi-turn jail-break at-tacks pose a grow-ing threat to de-p
loyed LLMs. At-tacks such as Crescendo (\T1/cmr/bx/n/10.95 ?\T1/cmr/m/n/10.95 )
,

Package natbib Warning: Citation `zeng2024persuasion' on page 1 undefined on in
put line 37.


Package natbib Warning: Citation `hagendorff2026nature' on page 1 undefined on 
input line 37.


Package natbib Warning: Citation `austin1962things' on page 1 undefined on inpu
t line 39.


Package natbib Warning: Citation `searle1969speech' on page 1 undefined on inpu
t line 39.


Package natbib Warning: Citation `he2021debertav3' on page 1 undefined on input
 line 41.


Package natbib Warning: Citation `cialdini2001science' on page 1 undefined on i
nput line 41.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

LaTeX Warning: Reference `sec:evasion' on page 2 undefined on input line 45.


LaTeX Warning: Reference `sec:main_results' on page 2 undefined on input line 4
6.


LaTeX Warning: Reference `sec:cross_attack' on page 2 undefined on input line 4
6.


LaTeX Warning: Reference `sec:trajectory' on page 2 undefined on input line 47.



Package natbib Warning: Citation `russinovich2024greatnow' on page 2 undefined 
on input line 56.


Package natbib Warning: Citation `zhou2024speak' on page 2 undefined on input l
ine 56.


Package natbib Warning: Citation `jiang2024deceptive' on page 2 undefined on in
put line 56.


Package natbib Warning: Citation `hagendorff2026nature' on page 2 undefined on 
input line 56.


Package natbib Warning: Citation `alon2023detecting' on page 2 undefined on inp
ut line 59.


Package natbib Warning: Citation `inan2023llama' on page 2 undefined on input l
ine 59.


Package natbib Warning: Citation `bullwinkel2025multiturn' on page 2 undefined 
on input line 59.


Package natbib Warning: Citation `su2026deepcontext' on page 2 undefined on inp
ut line 59.


Package natbib Warning: Citation `zeng2024persuasion' on page 2 undefined on in
put line 62.


Package natbib Warning: Citation `chen2025persuade' on page 2 undefined on inpu
t line 62.


Package natbib Warning: Citation `cialdini2001science' on page 2 undefined on i
nput line 77.


Package natbib Warning: Citation `zeng2024persuasion' on page 2 undefined on in
put line 77.

[2]

LaTeX Warning: Reference `tab:encoder' on page 3 undefined on input line 81.


Package natbib Warning: Citation `zhao2024wildchat' on page 3 undefined on inpu
t line 105.


LaTeX Warning: Reference `tab:tfidf_diagnostic' on page 3 undefined on input li
ne 109.


LaTeX Warning: Reference `sec:cross_attack' on page 3 undefined on input line 1
29.


LaTeX Warning: Reference `tab:attack_stats' on page 3 undefined on input line 1
29.

[3]

LaTeX Warning: Reference `tab:strategy_dist' on page 4 undefined on input line 
146.


LaTeX Warning: Reference `tab:main_results' on page 4 undefined on input line 1
76.


Overfull \hbox (9.55809pt too wide) in paragraph at lines 195--196
[]\T1/cmr/m/n/10.95 At $\OML/cmm/m/it/10.95 K$\T1/cmr/m/n/10.95 =2, DisPeD also
 achieves a sub-stan-tially lower false-positive rate at 95% TPR: FPR=0.08

LaTeX Warning: Reference `tab:encoder' on page 4 undefined on input line 197.


LaTeX Warning: Reference `tab:evasion_full' on page 4 undefined on input line 2
18.

[4]

LaTeX Warning: Reference `tab:evasion_k2' on page 5 undefined on input line 238
.


LaTeX Warning: Reference `tab:scrambled' on page 5 undefined on input line 258.



LaTeX Warning: Reference `tab:cross_attack' on page 5 undefined on input line 2
78.

[5]

LaTeX Warning: Reference `tab:cross_attack_k2' on page 6 undefined on input lin
e 295.


LaTeX Warning: Reference `tab:strategy_dist' on page 6 undefined on input line 
311.


LaTeX Warning: Reference `tab:trajectory' on page 6 undefined on input line 316
.


LaTeX Warning: Reference `tab:dominant_sequences' on page 6 undefined on input 
line 334.


Package natbib Warning: Citation `zhao2024wildchat' on page 6 undefined on inpu
t line 355.


LaTeX Warning: Reference `tab:hard_negatives' on page 6 undefined on input line
 372.

[6]

LaTeX Warning: Reference `tab:tfidf_performance' on page 7 undefined on input l
ine 377.


LaTeX Warning: Reference `tab:top_features' on page 7 undefined on input line 3
77.


LaTeX Warning: Reference `tab:checkpoint' on page 7 undefined on input line 415
.

[7] [8]

Package natbib Warning: There were undefined citations.

[9] [10] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0800
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0800
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0800.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf
 Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]
[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]
[183] [184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf
 Ok [25] [26] [28] [27] [29] [30] [31])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf
 Ok) ) ) )
(some charht values had to be adjusted by as much as 0.06445pt)
Font metrics written on ecrm0800.tfm.
Output written on ecrm0800.600gf (256 characters, 41732 bytes).
Transcript written on ecrm0800.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk: successfully generated.


LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli
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
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmsy10.pfb>
Output written on paper.pdf (10 pages, 200451 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
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
Overfull \hbox (28.68706pt too wide) in paragraph at lines 35--36
\T1/cmr/m/n/10.95 Multi-turn jail-break at-tacks pose a grow-ing threat to de-p
loyed LLMs. At-tacks such as Crescendo [[]Russi-

Overfull \hbox (6.0451pt too wide) in paragraph at lines 35--36
\T1/cmr/m/n/10.95 novich and Salem[], []2024[]], Foot-in-the-Door (FITD) [[]Zho
u et al.[], []2024[]], and De-cep-tive De-light [[]Jiang
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2] [3]
Overfull \hbox (9.55809pt too wide) in paragraph at lines 195--196
[]\T1/cmr/m/n/10.95 At $\OML/cmm/m/it/10.95 K$\T1/cmr/m/n/10.95 =2, DisPeD also
 achieves a sub-stan-tially lower false-positive rate at 95% TPR: FPR=0.08
[4] [5] [6] [7] [8] [9] [10] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli
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
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmsy10.pfb>
Output written on paper.pdf (10 pages, 204736 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12e4227d-6401-496d-b0c7-880d0b5f34c4",
  "isSidechain": false,
  "promptId": "0640bae5-48d0-4296-855e-879e96111727",
  "type": "user",
  "uuid": "ba3510e1-a2fc-42fa-87ca-431278b252b0",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `russinovich2024greatnow' on page 1 undefined \non input line 35.\n\n\nPackage natbib Warning: Citation `zhou2024speak' on page 1 undefined on input l\nine 35.\n\n\nPackage natbib Warning: Citation `jiang2024deceptive' on page 1 undefined on in\nput line 35.\n\n\nPackage natbib Warning: Citation `bullwinkel2025multiturn' on page 1 undefined \non input line 35.\n\n\nPackage natbib Warning: Citation `su2026deepcontext' on page 1 undefined on inp\nut line 35.\n\n\nOverfull \\hbox (13.75723pt too wide) in paragraph at lines 35--36\n\\T1/cmr/m/n/10.95 Multi-turn jail-break at-tacks pose a grow-ing threat to de-p\nloyed LLMs. At-tacks such as Crescendo (\\T1/cmr/bx/n/10.95 ?\\T1/cmr/m/n/10.95 )\n,\n\nPackage natbib Warning: Citation `zeng2024persuasion' on page 1 undefined on in\nput line 37.\n\n\nPackage natbib Warning: Citation `hagendorff2026nature' on page 1 undefined on \ninput line 37.\n\n\nPackage natbib Warning: Citation `austin1962things' on page 1 undefined on inpu\nt line 39.\n\n\nPackage natbib Warning: Citation `searle1969speech' on page 1 undefined on inpu\nt line 39.\n\n\nPackage natbib Warning: Citation `he2021debertav3' on page 1 undefined on input\n line 41.\n\n\nPackage natbib Warning: Citation `cialdini2001science' on page 1 undefined on i\nnput line 41.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nLaTeX Warning: Reference `sec:evasion' on page 2 undefined on input line 45.\n\n\nLaTeX Warning: Reference `sec:main_results' on page 2 undefined on input line 4\n6.\n\n\nLaTeX Warning: Reference `sec:cross_attack' on page 2 undefined on input line 4\n6.\n\n\nLaTeX Warning: Reference `sec:trajectory' on page 2 undefined on input line 47.\n\n\n\nPackage natbib Warning: Citation `russinovich2024greatnow' on page 2 undefined \non input line 56.\n\n\nPackage natbib Warning: Citation `zhou2024speak' on page 2 undefined on input l\nine 56.\n\n\nPackage natbib Warning: Citation `jiang2024deceptive' on page 2 undefined on in\nput line 56.\n\n\nPackage natbib Warning: Citation `hagendorff2026nature' on page 2 undefined on \ninput line 56.\n\n\nPackage natbib Warning: Citation `alon2023detecting' on page 2 undefined on inp\nut line 59.\n\n\nPackage natbib Warning: Citation `inan2023llama' on page 2 undefined on input l\nine 59.\n\n\nPackage natbib Warning: Citation `bullwinkel2025multiturn' on page 2 undefined \non input line 59.\n\n\nPackage natbib Warning: Citation `su2026deepcontext' on page 2 undefined on inp\nut line 59.\n\n\nPackage natbib Warning: Citation `zeng2024persuasion' on page 2 undefined on in\nput line 62.\n\n\nPackage natbib Warning: Citation `chen2025persuade' on page 2 undefined on inpu\nt line 62.\n\n\nPackage natbib Warning: Citation `cialdini2001science' on page 2 undefined on i\nnput line 77.\n\n\nPackage natbib Warning: Citation `zeng2024persuasion' on page 2 undefined on in\nput line 77.\n\n[2]\n\nLaTeX Warning: Reference `tab:encoder' on page 3 undefined on input line 81.\n\n\nPackage natbib Warning: Citation `zhao2024wildchat' on page 3 undefined on inpu\nt line 105.\n\n\nLaTeX Warning: Reference `tab:tfidf_diagnostic' on page 3 undefined on input li\nne 109.\n\n\nLaTeX Warning: Reference `sec:cross_attack' on page 3 undefined on input line 1\n29.\n\n\nLaTeX Warning: Reference `tab:attack_stats' on page 3 undefined on input line 1\n29.\n\n[3]\n\nLaTeX Warning: Reference `tab:strategy_dist' on page 4 undefined on input line \n146.\n\n\nLaTeX Warning: Reference `tab:main_results' on page 4 undefined on input line 1\n76.\n\n\nOverfull \\hbox (9.55809pt too wide) in paragraph at lines 195--196\n[]\\T1/cmr/m/n/10.95 At $\\OML/cmm/m/it/10.95 K$\\T1/cmr/m/n/10.95 =2, DisPeD also\n achieves a sub-stan-tially lower false-positive rate at 95% TPR: FPR=0.08\n\nLaTeX Warning: Reference `tab:encoder' on page 4 undefined on input line 197.\n\n\nLaTeX Warning: Reference `tab:evasion_full' on page 4 undefined on input line 2\n18.\n\n[4]\n\nLaTeX Warning: Reference `tab:evasion_k2' on page 5 undefined on input line 238\n.\n\n\nLaTeX Warning: Reference `tab:scrambled' on page 5 undefined on input line 258.\n\n\n\nLaTeX Warning: Reference `tab:cross_attack' on page 5 undefined on input line 2\n78.\n\n[5]\n\nLaTeX Warning: Reference `tab:cross_attack_k2' on page 6 undefined on input lin\ne 295.\n\n\nLaTeX Warning: Reference `tab:strategy_dist' on page 6 undefined on input line \n311.\n\n\nLaTeX Warning: Reference `tab:trajectory' on page 6 undefined on input line 316\n.\n\n\nLaTeX Warning: Reference `tab:dominant_sequences' on page 6 undefined on input \nline 334.\n\n\nPackage natbib Warning: Citation `zhao2024wildchat' on page 6 undefined on inpu\nt line 355.\n\n\nLaTeX Warning: Reference `tab:hard_negatives' on page 6 undefined on input line\n 372.\n\n[6]\n\nLaTeX Warning: Reference `tab:tfidf_performance' on page 7 undefined on input l\nine 377.\n\n\nLaTeX Warning: Reference `tab:top_features' on page 7 undefined on input line 3\n77.\n\n\nLaTeX Warning: Reference `tab:checkpoint' on page 7 undefined on input line 415\n.\n\n[7] [8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] [10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0800\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0800\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0800.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.06445pt)\nFont metrics written on ecrm0800.tfm.\nOutput written on ecrm0800.600gf (256 characters, 41732 bytes).\nTranscript written on ecrm0800.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmsy10.pfb>\nOutput written on paper.pdf (10 pages, 200451 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (28.68706pt too wide) in paragraph at lines 35--36\n\\T1/cmr/m/n/10.95 Multi-turn jail-break at-tacks pose a grow-ing threat to de-p\nloyed LLMs. At-tacks such as Crescendo [[]Russi-\n\nOverfull \\hbox (6.0451pt too wide) in paragraph at lines 35--36\n\\T1/cmr/m/n/10.95 novich and Salem[], []2024[]], Foot-in-the-Door (FITD) [[]Zho\nu et al.[], []2024[]], and De-cep-tive De-light [[]Jiang\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2] [3]\nOverfull \\hbox (9.55809pt too wide) in paragraph at lines 195--196\n[]\\T1/cmr/m/n/10.95 At $\\OML/cmm/m/it/10.95 K$\\T1/cmr/m/n/10.95 =2, DisPeD also\n achieves a sub-stan-tially lower false-positive rate at 95% TPR: FPR=0.08\n[4] [5] [6] [7] [8] [9] [10] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmsy10.pfb>\nOutput written on paper.pdf (10 pages, 204736 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "12e4227d-6401-496d-b0c7-880d0b5f34c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165817 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_ja…",
  "leafUuid": "ba3510e1-a2fc-42fa-87ca-431278b252b0",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated jailbreak detection research paper",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90"
}
```

---

### Assistant

_source line 28 · 2026-05-17T17:15:28.984Z_

编译成功，PDF 生成于 `paper.pdf`（10 页，无错误）。

论文覆盖了 `experiment_data.json` 中全部 10 个实验，对应 15 张表：
- **data_quality_fix** → Table 1 (TF-IDF diagnostic)
- **core_revalidation_clean** → Table 2 (F1 by turn budget) + Table 3 (encoder metrics)
- **adversarial_perturbation** + **deepcontext_proxy** + **tfidf_lr_baseline** → Table 4 (evasion hierarchy, full) + Table 5 (evasion hierarchy, K=2)
- **scrambled_label_ablation** → Table 6 (scrambled vs proper labels)
- **multi_attack_generation** → Table 7 (attack stats) + Table 8 (strategy distribution)
- **cross_attack_evaluation** → Table 9 (zero-shot generalization) + Table 10 (K=2 recall)
- **strategy_transition_analysis** → Table 11 (transition entropy) + Table 12 (dominant sequences)
- **wildchat_hard_negatives** → Table 13 (FPR on hard negatives)
- **tfidf_lr_baseline** → Table 14 (TF-IDF performance) + Table 15 (top features)
- **cross_checkpoint_variance** → Table 16 (checkpoint sensitivity)

所有定量 claim 均直接取自实验数据，无编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba3510e1-a2fc-42fa-87ca-431278b252b0",
  "isSidechain": false,
  "requestId": "req_011Cb8X1eeRnPxordVG62KQn",
  "type": "assistant",
  "uuid": "4858df20-e572-4bcc-b33c-4ef23b229352",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpwCF6XLUuuLSiD1JQ7vsY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9417,
      "cache_read_input_tokens": 50660,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9417,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 386,
          "cache_read_input_tokens": 50660,
          "cache_creation_input_tokens": 9417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9417
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

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165817 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_ja…",
  "leafUuid": "4858df20-e572-4bcc-b33c-4ef23b229352",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated jailbreak detection research paper",
  "sessionId": "4e1cddf5-200e-4a2d-9b68-28146b08fc90"
}
```

---
