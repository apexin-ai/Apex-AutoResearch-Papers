# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T113255 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1.jsonl`
- **Structured JSON:** [`31ac227c207f4dddf040.json`](../../sessions/31/31ac227c207f4dddf040.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T11:51:13.111Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T11:51:13.111Z",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T113255 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/experiment_data.json`（先 Read 此文件）\n- Venue：EMNLP 2026 Main Conference\n- Narrative guidance：Abandon dual-contribution framing. Reframe around the SINGLE most defensible novel insight: the QE-selection decoupling as a general warning for TTS scaling. New angle — position paper flavor: 'Not All Correlations Transfer: When Population-Level Quality Signals Fail at Instance-Level Selection.' Shift emphasis from IE-specific findings to general TTS methodology critique. Frame degeneracy not as IE-specific phenomenon but as inevitable consequence of any high-performance system (connect to reward hacking, mode collapse literature). Lean into free-form ablation + rank=8 as controlled experimental methodology contribution. Target same venue (Main Conference) by arguing methodological contribution to TTS evaluation paradigm rather than IE-specific empirical contribution. This requires rewriting intro/framing to lead with 'TTS promises are overfit to discrete-answer tasks' rather than 'structured IE needs confidence estimation.'\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T11:51:13.114Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T11:51:13.114Z",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1"
}
```

---

## Round 1

38 recorded events

### User

_source line 3 · 2026-05-16T11:51:13.135Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T113255 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/experiment_data.json`（先 Read 此文件）
- Venue：EMNLP 2026 Main Conference
- Narrative guidance：Abandon dual-contribution framing. Reframe around the SINGLE most defensible novel insight: the QE-selection decoupling as a general warning for TTS scaling. New angle — position paper flavor: 'Not All Correlations Transfer: When Population-Level Quality Signals Fail at Instance-Level Selection.' Shift emphasis from IE-specific findings to general TTS methodology critique. Frame degeneracy not as IE-specific phenomenon but as inevitable consequence of any high-performance system (connect to reward hacking, mode collapse literature). Lean into free-form ablation + rank=8 as controlled experimental methodology contribution. Target same venue (Main Conference) by arguing methodological contribution to TTS evaluation paradigm rather than IE-specific empirical contribution. This requires rewriting intro/framing to lead with 'TTS promises are overfit to discrete-answer tasks' rather than 'structured IE needs confidence estimation.'
- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "213d3fd3-ae42-4274-a194-17aa7930521a",
  "type": "user",
  "uuid": "1ff82f38-db45-4222-b915-4e1383826fe3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T11:51:13.134Z_

```json
{
  "parentUuid": "1ff82f38-db45-4222-b915-4e1383826fe3",
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
  "uuid": "87839214-f346-4ca8-85d2-7bcf93133060",
  "timestamp": "2026-05-16T11:51:13.134Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T11:51:13.134Z_

```json
{
  "parentUuid": "87839214-f346-4ca8-85d2-7bcf93133060",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "48c03db6-b766-412f-8e9e-c2eb927fc666",
  "timestamp": "2026-05-16T11:51:13.134Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
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
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1"
}
```

---

### Assistant

_source line 7 · 2026-05-16T11:51:16.373Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the experiment data and paper framing files to understand what I need to write.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48c03db6-b766-412f-8e9e-c2eb927fc666",
  "isSidechain": false,
  "requestId": "req_011Cb6CVPiowNDFDXbxTb6oS",
  "type": "assistant",
  "uuid": "6432e3c4-f05e-4306-a64d-4a0bc32245f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUTGTXPDePx6We8ZwHvWLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11266,
      "cache_read_input_tokens": 11841,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11266,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11266,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11266
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

_source line 8 · 2026-05-16T11:51:16.865Z_

<details open><summary>🔧 Tool call — Read · `toolu_0152VWWHoo85Rai6kewGQBxn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6432e3c4-f05e-4306-a64d-4a0bc32245f3",
  "isSidechain": false,
  "requestId": "req_011Cb6CVPiowNDFDXbxTb6oS",
  "type": "assistant",
  "uuid": "5dcf8ab9-abdb-496c-a518-0ab7fa51a1db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUTGTXPDePx6We8ZwHvWLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11266,
      "cache_read_input_tokens": 11841,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11266,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11266,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11266
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

_source line 9 · 2026-05-16T11:51:16.883Z_

<details><summary>↩ Tool result · `toolu_0152VWWHoo85Rai6kewGQBxn`</summary>

```text
1	[
2	  {
3	    "name": "ner_llama_conll",
4	    "description": "LLaMA-3.1-8B fine-tuned on CoNLL-2003 NER, N=8, T=1.0. Cross-model validation for model-agnostic claim.",
5	    "results": {
6	      "greedy_f1": 0.924,
7	      "oracle_f1": 0.945,
8	      "oracle_headroom_pp": 2.1,
9	      "SJ_rho_full": 0.43,
10	      "FK_rho_full": 0.42,
11	      "LP_rho_full": 0.31,
12	      "EM_rho_full": 0.43,
13	      "EM_AUROC": 0.71,
14	      "SJ_AUROC": 0.7,
15	      "LP_AUROC": 0.76,
16	      "selection_best_vs_greedy_pp": 0.1,
17	      "degeneracy_rate": 0.56
18	    },
19	    "tables": [
20	      {
21	        "name": "Table: LLaMA CoNLL Cross-Model Results",
22	        "columns": [
23	          "Signal",
24	          "ρ_full",
25	          "AUROC",
26	          "Selection F1",
27	          "Δ vs Greedy"
28	        ],
29	        "rows": [
30	          [
31	            "SJ",
32	            0.43,
33	            0.7,
34	            0.925,
35	            "+0.1pp"
36	          ],
37	          [
38	            "FK",
39	            0.42,
40	            0.7,
41	            0.924,
42	            "0.0pp"
43	          ],
44	          [
45	            "EM",
46	            0.43,
47	            0.71,
48	            0.924,
49	            "0.0pp"
50	          ],
51	          [
52	            "LP",
53	            0.31,
54	            0.76,
55	            0.925,
56	            "+0.1pp"
57	          ],
58	          [
59	            "VC",
60	            0.43,
61	            0.71,
62	            0.926,
63	            "+0.2pp"
64	          ],
65	          [
66	            "Oracle",
67	            "—",
68	            "—",
69	            0.945,
70	            "+2.1pp"
71	          ]
72	        ]
73	      }
74	    ],
75	    "figures": [],
76	    "analysis": "Reviewer argument: 'Two 8B decoder-only models trained with identical LoRA rank on the same data showing similar behavior is not model-agnostic validation — it's confirmation that your experimental setup is internally consistent, which we already assumed. Show me an encoder model, a 70B model, or an API-only model without logprob access.' This neutralizes R2/R14 mitigation entirely. The high CoNLL degeneracy (56%) makes the cross-model comparison on selection MOOT — there's nothing to select from regardless of model.\n\nLLaMA-3.1-8B 在 CoNLL 上表现与 Qwen3-8B 高度一致（SJ ρ≈0.43 vs Qwen 0.436），这在 worst 档被 reviewer 解读为：同体量 decoder-only 模型 + 同 LoRA recipe → 相似行为是 trivially expected，不构成 'model-agnostic' 证据。Reviewer 会要求 encoder-based (DeBERTa) 或 70B+ 规模模型。AUROC 0.70-0.76 被认为是 majority-vote 在高 F1 数据集上的 trivial baseline 表现。CoNLL 高 degeneracy (56%) 使 selection headroom 仅 2pp，selection 结果 indistinguishable from greedy，进一步佐证 reviewer 的 'predictable for fine-tuned models' 评价。"
77	  },
78	  {
79	    "name": "simple_verifier_baseline",
80	    "description": "Logistic regression on 5 unsupervised signals (SJ, FK, EM, VC, LP) as supervised verifier. Train on existing (input, output, F1) triplets. 5-fold CV on SciERC.",
81	    "results": {
82	      "oracle_gap_closure_pct": 3.2,
83	      "verifier_selection_f1_ner": 0.648,
84	      "verifier_vs_greedy_pp_ner": 0.4,
85	      "verifier_vs_best_single_pp_ner": -0.2,
86	      "verifier_auroc_ner": 0.76,
87	      "best_single_auroc_ner": 0.749,
88	      "verifier_selection_f1_re": 0.395,
89	      "verifier_vs_greedy_pp_re": -0.9,
90	      "feature_importance_top": "EM (0.42), VC (0.31), SJ (0.18), LP (0.06), FK (0.03)",
91	      "cross_val_std": 0.045,
92	      "training_time_minutes": 12,
93	      "status": "completed but inconclusive"
94	    },
95	    "tables": [
96	      {
97	        "name": "Table: Supervised Verifier vs Unsupervised Signals (SciERC NER, 5-fold CV)",
98	        "columns": [
99	          "Method",
100	          "Selection F1",
101	          "Δ vs Greedy",
102	          "AUROC",
103	          "Oracle Gap Closed"
104	        ],
105	        "rows": [
106	          [
107	            "Greedy (T=0)",
108	            0.644,
109	            "—",
110	            "—",
111	            "0%"
112	          ],
113	          [
114	            "Best single (EM)",
115	            0.65,
116	            "+0.6pp",
117	            0.749,
118	            "4.6%"
119	          ],
120	          [
121	            "LR Verifier (5-signal)",
122	            0.648,
123	            "+0.4pp",
124	            0.76,
125	            "3.2%"
126	          ],
127	          [
128	            "Oracle",
129	            0.776,
130	            "+13.2pp",
131	            "—",
132	            "100%"
133	          ]
134	        ]
135	      },
136	      {
137	        "name": "Table: Feature Importance & Correlation",
138	        "columns": [
139	          "Feature",
140	          "LR Coefficient",
141	          "Pairwise ρ with others (mean)"
142	        ],
143	        "rows": [
144	          [
145	            "EM",
146	            0.42,
147	            0.61
148	          ],
149	          [
150	            "VC",
151	            0.31,
152	            0.72
153	          ],
154	          [
155	            "SJ",
156	            0.18,
157	            0.68
158	          ],
159	          [
160	            "LP",
161	            0.06,
162	            0.45
163	          ],
164	          [
165	            "FK",
166	            0.03,
167	            0.59
168	          ]
169	        ]
170	      }
171	    ],
172	    "figures": [],
173	    "analysis": "Worst-tier reviewer response: 'The supervised verifier closes 3% of the oracle gap using the same signals that individually close <5%. This is expected — linear combinations of correlated weak signals yield a correlated weak signal. The real question is whether a verifier with access to input representations (not just output statistics) can close the gap. You haven't tested this, and your 'path forward' remains speculative.' The result actively HURTS the paper because it demonstrates the 5 signals collectively contain negligible selection-relevant information beyond what any single signal provides. This undercuts Contribution B's 'constructive implications' framing — there's no evidence the gap IS closable.\n\n在 worst 档，A5 的核心假设是 'path forward is entirely speculative'。即使 exp-019 完成（实际已被 killed），logistic regression 仅做 5 signal 的线性组合 — 与 exp-016 的 ensemble 本质相同。exp-016 已显示 ensemble AUROC (0.666) < best single EM (0.749)，因为 5 信号高度相关 (SJ-LP Pearson=0.57, SJ-VC 更高)。LR 在高相关特征上 overfit 导致 CV variance 大、泛化差。关键问题：LR 只能做信号的加权组合，不能学到 instance-level nonlinear interaction — 而 oracle gap 的信息恰恰存在于这些 interaction 中。Reviewer 判定：'A logistic regression on the same 5 signals you already showed don't work individually is not a trained verifier — it's a weighted average. A real verifier would use the input text, predicted output, and intermediate representations. This doesn't address the gap.'  oracle_gap_closure 3.2% 落在 worst 档 [0,5] 范围内。"
174	  },
175	  {
176	    "name": "claim_audit",
177	    "description": "Systematic cross-chapter numerical consistency audit. Check all quantitative claims against source data. Resolve known contradictions.",
178	    "results": {
179	      "contradictions_found": 7,
180	      "contradictions_resolved": 4,
181	      "contradictions_remaining": 3,
182	      "sections_with_stale_numbers": [
183	        "Abstract",
184	        "Introduction",
185	        "Discussion"
186	      ],
187	      "critical_issues": [
188	        "Abstract claims AUROC 0.82 but max observed is 0.749 (EM NER) from 1024-token data; 0.82 only achievable with EM on CoNLL which has 58% degeneracy",
189	        "Discussion '+0.2pp over greedy' uses Table 2 macro but intro cites sample-level delta",
190	        "Capability trap R²=0.94 on n=3 still referenced in Conclusion despite downgrade to 'qualitative'"
191	      ],
192	      "greedy_f1_inconsistency": "3 different greedy F1 values cited for SciERC NER (0.618, 0.644, 0.667) from different max_tokens/seeds",
193	      "table2_audit_clean": true
194	    },
195	    "tables": [
196	      {
197	        "name": "Audit Result Summary",
198	        "columns": [
199	          "Section",
200	          "Claim",
201	          "Cited Value",
202	          "Source Value",
203	          "Status"
204	        ],
205	        "rows": [
206	          [
207	            "Abstract",
208	            "AUROC up to 0.82",
209	            0.82,
210	            "0.749 (SciERC) / 0.816 (CoNLL)",
211	            "MISMATCH — needs scope qualifier"
212	          ],
213	          [
214	            "Intro",
215	            "selection ≈ greedy (+0.2pp)",
216	            "+0.2pp",
217	            "+0.6pp (NER LP) / -0.9pp (RE)",
218	            "MISMATCH — task-dependent sign"
219	          ],
220	          [
221	            "Discussion",
222	            "R²=0.94 monotone relationship",
223	            "R²=0.94",
224	            "n=3, qualitative only",
225	            "STALE — acknowledged but still cited"
226	          ],
227	          [
228	            "Table 2",
229	            "Macro F1 unified",
230	            "LP 0.647, Greedy 0.645",
231	            "exp_016_rerun_1024",
232	            "CLEAN"
233	          ],
234	          [
235	            "Section 5.2",
236	            "ρ up to 0.45",
237	            0.45,
238	            "0.4497 (CoNLL SJ N=16 cond)",
239	            "OK — rounded"
240	          ],
241	          [
242	            "Conclusion",
243	            "58% degeneracy for high-cap models",
244	            "58%",
245	            "CoNLL tied fraction",
246	            "OK"
247	          ],
248	          [
249	            "Section 4.1",
250	            "greedy F1 0.644",
251	            0.644,
252	            "0.6439 (exp_016) vs 0.6647 (1024-token)",
253	            "MISMATCH — max_tokens version"
254	          ]
255	        ]
256	      }
257	    ],
258	    "figures": [],
259	    "analysis": "Worst-tier impact: 审计本身不产生新证据，但暴露的不一致被 reviewer 用作 'insufficient care in reporting' 的证据。关键问题是 AUROC 0.82 — 这是论文最显眼的数字（Abstract 第一句），但无法用单一实验直接支撑。如果 0.82 来自 CoNLL EM AUROC 0.84，reviewer 会指出 CoNLL 58% degeneracy 使该数字 misleading（模型已 saturated，高 AUROC 只是在区分'全对' vs '差一两个 entity'）。如果来自 voting_conf 在某个 seed 的 AUROC，则不 reproducible。Worst-tier reviewer 会写：'The authors claim AUROC 0.82 in the abstract but I cannot find this exact number in any table. The closest is 0.749 (Table 3, SciERC EM) or 0.816 (Table 4, CoNLL EM). This kind of discrepancy undermines confidence in the reported results.' Soundness score: 3 (low end of worst range).\n\n在 worst 档下，claim audit 暴露出论文内部数值混乱的根本原因：实验跨越多个月、多次 rerun (512→1024 token, gold-empty filtering pipeline change, 3 seeds)，导致同一指标在不同章节引用不同来源。Abstract 的 AUROC 0.82 来自 paper_framing 的 Claim 1 描述 ('AUROC up to 0.82')，但实际最高值是 CoNLL EM AUROC 0.8156 (exp_002 registry) 或 SciERC EM AUROC 0.749 (exp_012_rerun_1024)。0.82 可能是 exp_002_conll_n16 的 EM AUROC 0.8409 四舍五入后的 legacy 值，但该数据集 degeneracy 58%。Reviewer 注意到数值不一致时会扣 soundness 分 — 从 4 降到 3。3 个未解决矛盾会被标注为 'careless writing' 或 'claims not fully supported by evidence'，直接影响 reviewer confidence。这不影响科学结论但影响 accept probability — worst 档 reviewer 已经倾向 reject，数值不一致提供了具体依据。"
260	  }
261	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5dcf8ab9-abdb-496c-a518-0ab7fa51a1db",
  "isSidechain": false,
  "promptId": "213d3fd3-ae42-4274-a194-17aa7930521a",
  "type": "user",
  "uuid": "800b9966-bfba-4e64-8eaa-7872fc06d60b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"ner_llama_conll\",\n    \"description\": \"LLaMA-3.1-8B fine-tuned on CoNLL-2003 NER, N=8, T=1.0. Cross-model validation for model-agnostic claim.\",\n    \"results\": {\n      \"greedy_f1\": 0.924,\n      \"oracle_f1\": 0.945,\n      \"oracle_headroom_pp\": 2.1,\n      \"SJ_rho_full\": 0.43,\n      \"FK_rho_full\": 0.42,\n      \"LP_rho_full\": 0.31,\n      \"EM_rho_full\": 0.43,\n      \"EM_AUROC\": 0.71,\n      \"SJ_AUROC\": 0.7,\n      \"LP_AUROC\": 0.76,\n      \"selection_best_vs_greedy_pp\": 0.1,\n      \"degeneracy_rate\": 0.56\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: LLaMA CoNLL Cross-Model Results\",\n        \"columns\": [\n          \"Signal\",\n          \"ρ_full\",\n          \"AUROC\",\n          \"Selection F1\",\n          \"Δ vs Greedy\"\n        ],\n        \"rows\": [\n          [\n            \"SJ\",\n            0.43,\n            0.7,\n            0.925,\n            \"+0.1pp\"\n          ],\n          [\n            \"FK\",\n            0.42,\n            0.7,\n            0.924,\n            \"0.0pp\"\n          ],\n          [\n            \"EM\",\n            0.43,\n            0.71,\n            0.924,\n            \"0.0pp\"\n          ],\n          [\n            \"LP\",\n            0.31,\n            0.76,\n            0.925,\n            \"+0.1pp\"\n          ],\n          [\n            \"VC\",\n            0.43,\n            0.71,\n            0.926,\n            \"+0.2pp\"\n          ],\n          [\n            \"Oracle\",\n            \"—\",\n            \"—\",\n            0.945,\n            \"+2.1pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Reviewer argument: 'Two 8B decoder-only models trained with identical LoRA rank on the same data showing similar behavior is not model-agnostic validation — it's confirmation that your experimental setup is internally consistent, which we already assumed. Show me an encoder model, a 70B model, or an API-only model without logprob access.' This neutralizes R2/R14 mitigation entirely. The high CoNLL degeneracy (56%) makes the cross-model comparison on selection MOOT — there's nothing to select from regardless of model.\\n\\nLLaMA-3.1-8B 在 CoNLL 上表现与 Qwen3-8B 高度一致（SJ ρ≈0.43 vs Qwen 0.436），这在 worst 档被 reviewer 解读为：同体量 decoder-only 模型 + 同 LoRA recipe → 相似行为是 trivially expected，不构成 'model-agnostic' 证据。Reviewer 会要求 encoder-based (DeBERTa) 或 70B+ 规模模型。AUROC 0.70-0.76 被认为是 majority-vote 在高 F1 数据集上的 trivial baseline 表现。CoNLL 高 degeneracy (56%) 使 selection headroom 仅 2pp，selection 结果 indistinguishable from greedy，进一步佐证 reviewer 的 'predictable for fine-tuned models' 评价。\"\n  },\n  {\n    \"name\": \"simple_verifier_baseline\",\n    \"description\": \"Logistic regression on 5 unsupervised signals (SJ, FK, EM, VC, LP) as supervised verifier. Train on existing (input, output, F1) triplets. 5-fold CV on SciERC.\",\n    \"results\": {\n      \"oracle_gap_closure_pct\": 3.2,\n      \"verifier_selection_f1_ner\": 0.648,\n      \"verifier_vs_greedy_pp_ner\": 0.4,\n      \"verifier_vs_best_single_pp_ner\": -0.2,\n      \"verifier_auroc_ner\": 0.76,\n      \"best_single_auroc_ner\": 0.749,\n      \"verifier_selection_f1_re\": 0.395,\n      \"verifier_vs_greedy_pp_re\": -0.9,\n      \"feature_importance_top\": \"EM (0.42), VC (0.31), SJ (0.18), LP (0.06), FK (0.03)\",\n      \"cross_val_std\": 0.045,\n      \"training_time_minutes\": 12,\n      \"status\": \"completed but inconclusive\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Supervised Verifier vs Unsupervised Signals (SciERC NER, 5-fold CV)\",\n        \"columns\": [\n          \"Method\",\n          \"Selection F1\",\n          \"Δ vs Greedy\",\n          \"AUROC\",\n          \"Oracle Gap Closed\"\n        ],\n        \"rows\": [\n          [\n            \"Greedy (T=0)\",\n            0.644,\n            \"—\",\n            \"—\",\n            \"0%\"\n          ],\n          [\n            \"Best single (EM)\",\n            0.65,\n            \"+0.6pp\",\n            0.749,\n            \"4.6%\"\n          ],\n          [\n            \"LR Verifier (5-signal)\",\n            0.648,\n            \"+0.4pp\",\n            0.76,\n            \"3.2%\"\n          ],\n          [\n            \"Oracle\",\n            0.776,\n            \"+13.2pp\",\n            \"—\",\n            \"100%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Feature Importance & Correlation\",\n        \"columns\": [\n          \"Feature\",\n          \"LR Coefficient\",\n          \"Pairwise ρ with others (mean)\"\n        ],\n        \"rows\": [\n          [\n            \"EM\",\n            0.42,\n            0.61\n          ],\n          [\n            \"VC\",\n            0.31,\n            0.72\n          ],\n          [\n            \"SJ\",\n            0.18,\n            0.68\n          ],\n          [\n            \"LP\",\n            0.06,\n            0.45\n          ],\n          [\n            \"FK\",\n            0.03,\n            0.59\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Worst-tier reviewer response: 'The supervised verifier closes 3% of the oracle gap using the same signals that individually close <5%. This is expected — linear combinations of correlated weak signals yield a correlated weak signal. The real question is whether a verifier with access to input representations (not just output statistics) can close the gap. You haven't tested this, and your 'path forward' remains speculative.' The result actively HURTS the paper because it demonstrates the 5 signals collectively contain negligible selection-relevant information beyond what any single signal provides. This undercuts Contribution B's 'constructive implications' framing — there's no evidence the gap IS closable.\\n\\n在 worst 档，A5 的核心假设是 'path forward is entirely speculative'。即使 exp-019 完成（实际已被 killed），logistic regression 仅做 5 signal 的线性组合 — 与 exp-016 的 ensemble 本质相同。exp-016 已显示 ensemble AUROC (0.666) < best single EM (0.749)，因为 5 信号高度相关 (SJ-LP Pearson=0.57, SJ-VC 更高)。LR 在高相关特征上 overfit 导致 CV variance 大、泛化差。关键问题：LR 只能做信号的加权组合，不能学到 instance-level nonlinear interaction — 而 oracle gap 的信息恰恰存在于这些 interaction 中。Reviewer 判定：'A logistic regression on the same 5 signals you already showed don't work individually is not a trained verifier — it's a weighted average. A real verifier would use the input text, predicted output, and intermediate representations. This doesn't address the gap.'  oracle_gap_closure 3.2% 落在 worst 档 [0,5] 范围内。\"\n  },\n  {\n    \"name\": \"claim_audit\",\n    \"description\": \"Systematic cross-chapter numerical consistency audit. Check all quantitative claims against source data. Resolve known contradictions.\",\n    \"results\": {\n      \"contradictions_found\": 7,\n      \"contradictions_resolved\": 4,\n      \"contradictions_remaining\": 3,\n      \"sections_with_stale_numbers\": [\n        \"Abstract\",\n        \"Introduction\",\n        \"Discussion\"\n      ],\n      \"critical_issues\": [\n        \"Abstract claims AUROC 0.82 but max observed is 0.749 (EM NER) from 1024-token data; 0.82 only achievable with EM on CoNLL which has 58% degeneracy\",\n        \"Discussion '+0.2pp over greedy' uses Table 2 macro but intro cites sample-level delta\",\n        \"Capability trap R²=0.94 on n=3 still referenced in Conclusion despite downgrade to 'qualitative'\"\n      ],\n      \"greedy_f1_inconsistency\": \"3 different greedy F1 values cited for SciERC NER (0.618, 0.644, 0.667) from different max_tokens/seeds\",\n      \"table2_audit_clean\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Audit Result Summary\",\n        \"columns\": [\n          \"Section\",\n          \"Claim\",\n          \"Cited Value\",\n          \"Source Value\",\n          \"Status\"\n        ],\n        \"rows\": [\n          [\n            \"Abstract\",\n            \"AUROC up to 0.82\",\n            0.82,\n            \"0.749 (SciERC) / 0.816 (CoNLL)\",\n            \"MISMATCH — needs scope qualifier\"\n          ],\n          [\n            \"Intro\",\n            \"selection ≈ greedy (+0.2pp)\",\n            \"+0.2pp\",\n            \"+0.6pp (NER LP) / -0.9pp (RE)\",\n            \"MISMATCH — task-dependent sign\"\n          ],\n          [\n            \"Discussion\",\n            \"R²=0.94 monotone relationship\",\n            \"R²=0.94\",\n            \"n=3, qualitative only\",\n            \"STALE — acknowledged but still cited\"\n          ],\n          [\n            \"Table 2\",\n            \"Macro F1 unified\",\n            \"LP 0.647, Greedy 0.645\",\n            \"exp_016_rerun_1024\",\n            \"CLEAN\"\n          ],\n          [\n            \"Section 5.2\",\n            \"ρ up to 0.45\",\n            0.45,\n            \"0.4497 (CoNLL SJ N=16 cond)\",\n            \"OK — rounded\"\n          ],\n          [\n            \"Conclusion\",\n            \"58% degeneracy for high-cap models\",\n            \"58%\",\n            \"CoNLL tied fraction\",\n            \"OK\"\n          ],\n          [\n            \"Section 4.1\",\n            \"greedy F1 0.644\",\n            0.644,\n            \"0.6439 (exp_016) vs 0.6647 (1024-token)\",\n            \"MISMATCH — max_tokens version\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Worst-tier impact: 审计本身不产生新证据，但暴露的不一致被 reviewer 用作 'insufficient care in reporting' 的证据。关键问题是 AUROC 0.82 — 这是论文最显眼的数字（Abstract 第一句），但无法用单一实验直接支撑。如果 0.82 来自 CoNLL EM AUROC 0.84，reviewer 会指出 CoNLL 58% degeneracy 使该数字 misleading（模型已 saturated，高 AUROC 只是在区分'全对' vs '差一两个 entity'）。如果来自 voting_conf 在某个 seed 的 AUROC，则不 reproducible。Worst-tier reviewer 会写：'The authors claim AUROC 0.82 in the abstract but I cannot find this exact number in any table. The closest is 0.749 (Table 3, SciERC EM) or 0.816 (Table 4, CoNLL EM). This kind of discrepancy undermines confidence in the reported results.' Soundness score: 3 (low end of worst range).\\n\\n在 worst 档下，claim audit 暴露出论文内部数值混乱的根本原因：实验跨越多个月、多次 rerun (512→1024 token, gold-empty filtering pipeline change, 3 seeds)，导致同一指标在不同章节引用不同来源。Abstract 的 AUROC 0.82 来自 paper_framing 的 Claim 1 描述 ('AUROC up to 0.82')，但实际最高值是 CoNLL EM AUROC 0.8156 (exp_002 registry) 或 SciERC EM AUROC 0.749 (exp_012_rerun_1024)。0.82 可能是 exp_002_conll_n16 的 EM AUROC 0.8409 四舍五入后的 legacy 值，但该数据集 degeneracy 58%。Reviewer 注意到数值不一致时会扣 soundness 分 — 从 4 降到 3。3 个未解决矛盾会被标注为 'careless writing' 或 'claims not fully supported by evidence'，直接影响 reviewer confidence。这不影响科学结论但影响 accept probability — worst 档 reviewer 已经倾向 reject，数值不一致提供了具体依据。\"\n  }\n]",
      "numLines": 261,
      "startLine": 1,
      "totalLines": 261
    }
  },
  "sourceToolAssistantUUID": "5dcf8ab9-abdb-496c-a518-0ab7fa51a1db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T11:51:17.389Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ly8MXioHmTtzre25BEaNuW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "800b9966-bfba-4e64-8eaa-7872fc06d60b",
  "isSidechain": false,
  "requestId": "req_011Cb6CVPiowNDFDXbxTb6oS",
  "type": "assistant",
  "uuid": "908f34a1-2ddf-40f1-99d7-bbce8ac16a26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUTGTXPDePx6We8ZwHvWLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11266,
      "cache_read_input_tokens": 11841,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11266,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11266,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11266
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T113255 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consi…",
  "leafUuid": "908f34a1-2ddf-40f1-99d7-bbce8ac16a26",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1"
}
```

---

### Tool result

_source line 13 · 2026-05-16T11:51:17.681Z_

<details><summary>↩ Tool result · `toolu_01Ly8MXioHmTtzre25BEaNuW`</summary>

```text
1	# Paper Framing — struct_self_consist_ie
2	
3	> Updated 2026-05-16 — D116: Dream full review feedback → Reframe to DUAL CONTRIBUTION (QE positive + selection diagnostic). D113: Table 2 macro F1 unified (Greedy=0.645, LP=0.647, all p>0.05). exp-023: LoRA rank=8 degeneracy 7.2% vs 21% but selection still fails → multi-causal (not just degeneracy). Trained verifier baseline (logistic regression on 5 signals) in progress. R² on n=3 must be caveated as qualitative only.
4	
5	## Target Venue
6	- Primary: EMNLP 2026 **Main Conference** (via ARR May 2026)
7	- Deadline: ARR May cycle, 2026-05-25
8	
9	## Core Claims (D116 updated — DUAL CONTRIBUTION: QE positive + selection diagnostic)
10	
11	### Claim 1 (PRIMARY — Dual Contribution: QE Framework + Selection Diagnostic)
12	**Positive contribution (A)**: Confidence signals reliably predict structured IE output quality at the population level (AUROC up to 0.82, ρ up to 0.45), enabling practical QE/selective prediction.
13	**Diagnostic contribution (B)**: These same signals universally fail to select better candidates from multiple samples. We diagnose the multi-causal failure: (1) instance degeneracy eliminates headroom for 4/5 signals; (2) LP compression eliminates it for the remaining one; (3) reducing degeneracy (LoRA rank=8: 7.2% vs 21%) increases oracle headroom but signals STILL cannot exploit it → low degeneracy is necessary but not sufficient → trained verifiers are the natural next step.
14	
15	The framing is NOT "selection fails" (pure negative) but "we show WHEN, WHY, and WHAT WOULD BE NEEDED for selection to work" (diagnostic with constructive implications).
16	
17	**Three-layer argument + Capability Trap**:
18	- Layer A (design property, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification — the "methodological premise" — not an empirical finding.
19	- Layer B (empirical — instance degeneracy): 21-58% of instances produce identical F1 across all N samples, eliminating selection headroom. Within-instance ρ=0.524 (SciERC) and 0.994 (CoNLL) — signals ARE correlated within instances, but degeneracy makes this irrelevant. Non-degenerate instances show MBR closing 23-41% of oracle gap. Selection recovers T=1.0 sampling degradation (LP 0.647 vs Random 0.610, +3.7pp) but only matches T=0 greedy (0.645 macro) at 8× inference cost — zero marginal gain.
20	- Layer C (empirical — LP compression): Logprob — the only per-sample signal — fails due to intrinsic score compression (median within-instance LP range = 0.041 nats). Entity-token LP shows 4× variance but WORSE selection (-2.0pp). Free-form ablation confirms compression is model/task intrinsic (std ratio 0.97).
21	- **Capability Trap** (unifying insight, D111): Model capability → output convergence → instance degeneracy → vanishing selection headroom. Evidence: CoNLL (91% F1) → 58% degeneracy, SciERC (66% F1) → 21%, WNUT (48% F1) → ~0%. Scale dimension: 8B → 21% degen vs 4B → 10.4% on SciERC. This is NOT an "artifact" — it is a **consequence of capability**, a structural inevitability. The better the model, the less test-time scaling can help via unsupervised selection.
22	
23	**Distinction from MBR literature**: Eikema et al.'s MBR failure = utility function misalignment. Our failure = utility IS aligned (within-instance ρ=0.524) but headroom eliminated by degeneracy — qualitatively novel mechanism.
24	
25	**Key evidence (score compression)**:
26	- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ: 0.08→0.39
27	- Full set: logprob +0.6pp, bootstrap p=0.39, Cohen's d=0.038 (negligible), 95% CI [-3.0, +4.2]pp
28	- Oracle headroom: NER +13pp, RE +18pp → information exists but signals can't access it
29	
30	**Key evidence (free-form ablation)** [DONE — exp_freeform_ablation, NEGATIVE]:
31	- LP distribution: constrained std=0.0206, free-form std=0.0199 (ratio 0.97, virtually unchanged)
32	- Tied fraction: 59.7% → 57.7% (-2.0pp, negligible)
33	- NER selection: +0.59pp → +0.18pp (both negligible vs greedy)
34	- RE selection: -0.68pp → +1.69pp (flipped positive — secondary finding)
35	- NER VC rho: 0.379 → 0.409 (slight QE improvement, selection still fails)
36	- Parse rate: 99.95% (fine-tuned model retains JSON format without grammar)
37	- **Conclusion**: Score compression is model/task intrinsic. The gap is universal.
38	
39	**Key evidence (scale ablation)** [DONE — 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}]:
40	- CoNLL NER: 4B greedy_f1=0.9234 (>8B 0.9123, +1.11pp), SJ_ρ=0.4217 (≈8B 0.4357, −1.4pp), FK_ρ=0.4181 (>8B 0.3998, +1.83pp)
41	- SciERC NER: 4B SJ_ρ=0.4221 (>8B 0.3825, +3.96pp), FK_ρ=0.3258 (>8B 0.2590, +6.68pp)
42	- SciERC RE: 4B SJ_ρ=0.2673 (>8B 0.2441, +2.32pp), FK_ρ=0.3593 (>8B 0.2782, +8.11pp); struct>surface ✗ at both scales
43	- **Conclusion**: Correlation strength maintained or improved at 4B across all 4 cells. The gap originates from within-instance signal misalignment, not model capacity. Task difficulty (SciERC RE zero-F1 rate) remains the primary driver, consistent across scales.
44	- CoNLL 4B headroom: 1.70pp (vs 8B 4.20pp) → MARGINAL for selection power, but QE correlations robust
45	- SciERC RE 4B: 47.6% zero-F1, RE LP_ρ_cond=0.1135 (p=0.074, n.s.) → confirms binary dominance at 4B
46	- **4B selection results** (correlation-selection gap at 4B):
47	  - CoNLL NER 4B (n=2756): SJ +0.07pp, FK +0.03pp, LP +0.09pp vs greedy 0.9213. All ≤0.1pp — MARGINAL (headroom 1.70pp)
48	  - SciERC NER 4B (n=529): SJ **-1.49pp**, FK -1.56pp, LP -2.23pp vs greedy 0.6622. Oracle 0.7925 (+13.02pp). **All signals WORSE than greedy despite 13pp oracle headroom — gap confirmed at 4B**
49	  - SciERC NER 4B gap demonstration: SJ-FK ρ gap = +0.096 (strong correlation advantage), SJ-FK selection F1 gap = +0.0007 (zero selection advantage) → correlation-selection gap quantified at 4B
50	- **n_samples confound control**: Qwen3-8B n=8 data exists as control. CoNLL SJ: n8 ρ=0.4389 → n16 ρ=0.4496 (Δ=0.011, CI crosses zero). SciERC SJ: n8→n16 Δ=0.066, CI=[0.004, 0.128] weak effect. n_samples not a confound for 4B-8B comparison.
51	- **Paper framing**: "Scale ablation shows the gap is not an artifact of a particular model size; correlation strength is maintained at 4B, confirming that the gap originates from within-instance signal misalignment rather than model capacity."
52	
53	**exp-019 supervised verifier**: IN PROGRESS (D116 Dream feedback — all 3 tiers flagged as critical gap). Simplified to logistic regression on 5 signals (scikit-learn, CPU, ~30min). If supervised verifier partially closes oracle gap → proves gap IS closable, signals carry information but unsupervised heuristics are too weak. Grounds the "what would be needed" part of Contribution B.
54	
55	**exp-023 LoRA rank=8 ablation** [DONE]: rank=8 vs rank=32 on SciERC. Degeneracy: 7.2% vs 21% (3× reduction). Oracle headroom: 16.0pp vs 13.3pp. But ALL selection methods still fail to beat greedy (LP -0.5pp, SJ -0.9pp). QE correlation preserved (VC ρ=0.394, SJ ρ=0.365). **Key insight**: Reducing degeneracy is NECESSARY but NOT SUFFICIENT — signals themselves lack the discriminative power to exploit increased headroom. Strengthens multi-causal argument and points to trained verifiers as the path forward. Dream 三档公认最强实验。
56	
57	**Bonus finding (parse rate)**: Free-form parse rate 99.95% (4406/4408) — fine-tuned 8B model generates valid JSON without grammar constraints. Challenges intro:19 claim about constrained decoding necessity for format compliance.
58	
59	**Implications**: Not just "signals don't work" but "here's WHY they don't work (intrinsic score compression), here's proof it's universal (controlled ablation via elimination), and here's the forward direction (breaking LP compression requires fundamentally different approaches — trained verifiers, multi-round refinement — not simply relaxing decoding constraints)."
60	
61	### Claim 2 (METHODOLOGY — QE Evaluation Framework)
62	Systematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. This is the methodological infrastructure, not a primary contribution.
63	
64	**Key results**:
65	- NER: EM AUROC 0.749, voting_conf ρ=0.379, SJ ρ=0.360 — all >> logprob (AUROC 0.578, ρ=0.205). 3-seed consistent: SJ > FK delta=0.093~0.122
66	- RE (3-seed confirmed): **LP > SJ > FK** (mean ρ: LP 0.302, SJ 0.265, FK 0.254). Signal ranking reverses vs NER — structural signals lose advantage when 43-45% of RE samples have F1=0 (binary signal dominance). LP's coarse but stable generation-confidence signal captures "did the model get any relations right" better than structural overlap measures.
67	- Difficulty-dependent signal ranking: WNUT-17 conditional collapse (ρ significant → n.s.) + logprob ρ=−0.410 (non-obvious: overconfidence on OOD)
68	- Temperature robustness: SJ Δρ=±0.01 vs FK Δρ=±0.06-0.09. T=0.7: LP full ρ improves 0.205→0.249, LP cond ρ 0.154→0.185; FK 0.267→0.289 despite more compression → concentrated signal hypothesis (non-tied instances at lower T carry more informative variance). **Paper citation rule**: robustness/temperature tables use full ρ; score compression analysis uses cond ρ. Always annotate which variant.
69	- **Task-dependent signal effectiveness** (new finding from RE 3-seed): The optimal signal family depends on task structure. NER (token-level, graded F1) → structural agreement captures quality gradients. RE (relation-level, binary-dominated F1) → logprob captures generation confidence better. This is NOT a weakness — it's a nuanced finding that enriches the diagnostic framework.
70	
71	**Evidence preserved from original Claim 1** (SciERC, N=8, T=1.0, exp_012_rerun_1024):
72	- NER full (n=529): ρ — voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205; AUROC — EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578
73	- RE full (n=397): AUROC — EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601
74	- ECE (NER): EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706
75	
76	### Claim 2b (Selection evidence)
77	**exp_016_rerun_1024 evidence** (SciERC 8B, N=8, T=1.0):
78	- NER best-of-N (n=529): logprob 0.6501 > sj 0.6450 = ensemble 0.6450 > greedy 0.6439 > voting 0.6337 > random 0.6077 (oracle 0.7758)
79	- RE best-of-N (n=397): greedy 0.4042 > logprob 0.3948 > sj 0.3855 = ensemble 0.3855 > voting 0.3592 > random 0.3544 (oracle 0.5850)
80	
81	**4B selection evidence** (N=8, T=1.0):
82	- CoNLL NER 4B (n=2756): greedy 0.9213, SJ 0.9220 (+0.07pp), FK 0.9215, LP 0.9221 (+0.09pp), oracle 0.9382. Headroom 1.70pp → selection indistinguishable
83	- SciERC NER 4B (n=529): greedy 0.6622, SJ 0.6473 (-1.49pp), FK 0.6466 (-1.56pp), LP 0.6399 (-2.23pp), oracle 0.7925 (+13.02pp). **All signals worse than greedy** → correlation-selection gap at 4B confirmed
84	
85	**exp_016_rerun_1024_bootstrap evidence** (3-seed bootstrap, 1000 iterations):
86	- NER logprob vs greedy: bootstrap 95% CI [−0.030, +0.042], permutation p=0.39
87	- Effect size: Cohen's d=0.038 (negligible), sign test win rate=0.466
88	
89	### Claim 3 (Diagnostic — task-complexity boundary + task-dependent signal effectiveness)
90	The effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.
91	
92	**RE 3-seed mechanism** (D073, confirmed at 4B): 43-47% of RE samples have F1=0 (8B: 43-45%, 4B: 47.6%), creating binary-dominated signal distributions where structural overlap (SJ/FK) cannot differentiate quality gradients. Pattern consistent across model scales — confirming task difficulty, not model capacity, drives this boundary. LP's generation confidence captures "complete failure vs partial success" more reliably. 3-seed RE QE: LP ρ=0.302 > SJ 0.265 > FK 0.254. **Definitive binary dominance evidence**: RE LP full ρ=0.266 but cond ρ=0.011 (p=0.86, completely n.s.) — LP's entire RE signal comes from the zero/nonzero F1 split; once conditioned on samples where the model extracts at least one relation, LP has zero predictive power for RE quality gradients. In contrast, NER LP cond ρ remains informative (0.154–0.185). This provides the concrete mechanism for Claim 3's task-complexity boundary: it's not just "compound error" in the abstract — it's specifically the high zero-F1 rate that shifts the optimal signal family from structural to probabilistic, and LP's RE advantage is entirely a binary classification effect, not genuine quality estimation.
93	
94	**MVP evidence**: RE full vs cond AUROC lift — EM: 0.706→0.752 (+4.6pp), SJ: 0.670→0.646 (−2.4pp, 待确认), voting_conf: 0.694→0.642 (−5.2pp, 待确认). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.
95	
96	**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.
97	
98	**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):
99	- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10
100	- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392
101	- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.
102	- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.
103	
104	## Story Spine (D116 — Dual Contribution: QE Positive + Selection Diagnostic, Main Conference)
105	
106	**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured information extraction is unclear. Practitioners need to know: (1) can confidence signals estimate output quality? (2) can they select better outputs?
107	
108	**Existing approaches & gaps**: Self-consistency (Wang et al. 2023) succeeds for discrete-answer reasoning. MBR decoding succeeds for MT. But structured IE outputs (entity sets, relation triples) present a fundamentally different challenge — prior work conflates quality estimation with selection. We decouple these and show they are governed by different factors.
109	
110	**Our framing (D116 — DUAL CONTRIBUTION)**:
111	
112	**Contribution A (Positive — QE Framework)**: Five confidence signals across four families reliably predict structured IE output quality (AUROC 0.82, ρ 0.45). Signal ranking is task-dependent: structural > probabilistic for NER, reversed for RE. This QE framework has practical value for selective prediction / error flagging regardless of selection effectiveness.
113	
114	**Contribution B (Diagnostic — Why Selection Fails + What Would Fix It)**:
115	1. **Design property**: 4/5 signals are instance-level aggregates → cannot rank candidates by construction.
116	2. **Instance Degeneracy**: 21-58% of instances produce identical F1 across all N samples, eliminating selection headroom.
117	3. **LP Compression**: Logprob within-instance range compressed (0.041 nats). Free-form ablation confirms intrinsic (std ratio 0.97).
118	4. **Multi-causal** (key D116 update): LoRA rank=8 reduces degeneracy 3× (7.2% vs 21%) and increases oracle headroom (+2.7pp), but ALL selection methods still fail to beat greedy → low degeneracy is NECESSARY but NOT SUFFICIENT. Signals lack discriminative power even when headroom exists.
119	5. **Capability-degeneracy tradeoff** (renamed from "trap"): Higher capability → more convergence → more degeneracy. Qualitative monotone relationship across datasets (CoNLL 91%→58% degen, SciERC 66%→21%). R² on n=3 is illustrative only, not statistically reliable.
120	6. **Path forward**: Non-tied subset +2.9pp (p=0.004) proves signals carry information. Trained verifier baseline (logistic regression on 5 signals, in progress) tests whether the gap is closable with supervision. If so → unsupervised signals are weak, not uninformative.
121	
122	**QE-vs-Selection Decoupling** (Dream-identified most novel insight): QE correlation (SJ ρ) is stable across LoRA rank configurations (0.360→0.378) while selection gap changes dramatically. Signals are ALWAYS useful for flagging uncertain instances, even when they cannot improve selection. This distinction has practical implications beyond IE.
123	
124	**Headline**: "We present a dual contribution for structured IE: (1) a QE framework showing confidence signals reliably predict output quality (AUROC 0.82), and (2) a diagnostic analysis revealing why these same signals fail at selection — instance degeneracy and logprob compression create a multi-causal gap that persists even when degeneracy is reduced. Selection approximately matches greedy decoding (Δ<0.3pp, all p>0.05) despite 13pp oracle headroom."
125	
126	**Title**: "Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction"
127	
128	## Anticipated Reviewer Concerns
129	
130	### R1: "Only one NER dataset — generalization unclear"
131	- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.
132	- **Priority**: P0
133	
134	### R2: "Only one model family (Qwen3-8B)"
135	- **Mitigation**: LLaMA-3.1-8B shows model-agnostic effect. ⚠️ **exp-007 数据被污染 (test data leakage)**，LLaMA SciERC 正确值来自 exp_018 (clean rerun)。unified_rho_full.json 的 LLaMA SciERC 条目必须替换为 exp_018 数据。正确 LLaMA SciERC N=8 3-seed mean: SJ 0.325, FK 0.256, VC 0.384, EM 0.279, LP 0.162。
136	- **Priority**: P0
137	
138	### R3: "FK is a strawman baseline — what about log-prob, USC, exact-match?"
139	- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (EM+SJ+voting) >> log-prob >> FK. USC discussed in related work (LLM-as-judge, orthogonal approach).
140	- **Priority**: P0, RESOLVED — results decisive
141	
142	### R3b: "EM beats voting_conf and SJ on AUROC — why present SJ/voting_conf?"
143	- **Mitigation**: EM is a strict binary signal (all-or-nothing match); SJ captures partial agreement and generalizes to arbitrary structured outputs (relations, events). Voting_conf provides granular entity-level scores. NER full AUROC: EM 0.749 > SJ 0.692 > voting_conf 0.684, but ρ: voting_conf 0.379 > SJ 0.360 > EM 0.295. EM excels at binary discrimination but underperforms on rank ordering. SJ is also more temperature-robust (Δρ=±0.01). Paper presents all three as complementary instantiations of the structural consistency principle: EM for go/no-go filtering, voting_conf for ranking, SJ for generalizability.
144	- **Priority**: P1 — narrative adjusted for 1024-token results
145	
146	### R4: "No actual TTS improvement demonstrated"
147	- **Status**: ✅ CONFIRMED by exp_016_rerun_1024_bootstrap. No signal significantly outperforms greedy on either task. NER logprob +0.6pp not significant (bootstrap p=0.39, 95% CI [−0.030, +0.042], Cohen's d=0.038). RE: greedy > all signals.
148	- **Mitigation**: Paper PIVOTS to "confidence estimation + correlation-selection gap analysis." exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.
149	- **Priority**: P0 — narrative pivot complete, bootstrap confirms
150	
151	### R5: "Sample size N=8 may be too small for reliable SJ estimation"
152	- **Mitigation**: exp-001 (N=16) with multi-seed robustness
153	- **Priority**: P0
154	
155	### R6: "Conditional analysis cherry-picks favorable instances"
156	- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.
157	- **Priority**: P0 (add sensitivity analysis)
158	
159	### R7: "Only ρ as evaluation metric"
160	- **Mitigation**: Add AUROC, calibration plots (ECE), Kendall's τ for all experiments. ECE data now available: NER best calibrated = EM (0.353), RE best = voting (0.272). Logprob worst calibrated (NER 0.706, RE 0.769).
161	- **Priority**: P0
162	
163	### R8: "Formula-implementation discrepancy"
164	- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)
165	- **Priority**: P0, paper writing fix
166	
167	### R9: "Evaluation circularity (T>0 consistency vs T=0 F1)"
168	- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).
169	- **Priority**: P0
170	
171	### R10: "Insufficient related work" (三档一致 [B][M][W])
172	- **Mitigation**: Expand to 35+ references. Must cite:
173	  - USC (Chen 2024) — empirical differentiation, not just citation
174	  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)
175	  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021
176	  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020
177	  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016
178	  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023
179	  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024
180	  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022
181	  - **IE confidence**: Culotta & McCallum 2004
182	  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)
183	  - **[2025-2026 新颖性自查补充 — 必引]**:
184	    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出
185	    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap
186	    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案
187	    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量
188	    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承"overlooks semantically consistent outputs"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机
189	  - **[2025-2026 新颖性自查补充 — 应引]**:
190	    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述
191	    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述
192	    - Semantic Entropy Probes (2024) — 低成本不确定性估计
193	    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性
194	    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务
195	    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关
196	    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位
197	    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE
198	    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE
199	  - **需新增 Related Work 小节**:
200	    - "Test-Time Scaling & Sample Selection" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap
201	    - "Consistency for Structured IE" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation
202	- **Priority**: P0, Paper Agent handles
203	
204	### R11: "SJ+logprob ensemble missing" (Dream 2 — both reviewers)
205	- **Status**: ⚠️ REVISED by exp_016_rerun_1024. Results:
206	  - Ensemble AUROC (5-fold CV LR): NER 0.666 ± 0.070, RE 0.662 ± 0.078
207	  - Best single signal EM: NER AUROC 0.749, RE AUROC 0.706
208	  - **Ensemble has NO advantage over best single signal** — EM alone outperforms the 5-signal logistic regression ensemble by +8.3pp (NER) and +4.4pp (RE)
209	  - **Interpretation**: With 1024-token clean data, EM captures nearly all discriminative information. The ensemble's inferior performance likely reflects overfitting in the 5-fold CV LR with correlated features. This further supports presenting EM as a simple, strong baseline within the structural consistency family.
210	- **Priority**: DONE — write into paper with honest interpretation (no ensemble advantage claim)
211	
212	### R12: "No supervised upper bound / reward model comparison" (Dream 2)
213	- **Mitigation**: exp-016 LR ensemble (5-signal, 5-fold CV) underperforms best single signal EM (AUROC 0.666 vs 0.749), suggesting feature redundancy. exp-019 supervised verifier SKIPPED (DDL risk + scope creep). Free-form ablation provides the "so what": gap is fundamental → closing it requires fundamentally different approaches (trained verifiers, not just better unsupervised signals). Positioned as future work with explicit motivation from ablation evidence.
214	- **Priority**: P1, addressed via framing (future work motivated by ablation)
215	
216	### R13: "Headroom capture rate low" (Dream 2)
217	- **Mitigation**: NER oracle 0.7758, greedy 0.6439, best signal (logprob) 0.6501 → captures 0.5% of headroom. RE oracle 0.5850, greedy 0.4042, best signal (greedy itself) → 0% capture. Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline and documents the gap.
218	- **Priority**: P0, paper writing
219	
220	### R14: "Cross-model validation thin — need more than 2×8B" (Dream 2)
221	- **Status**: ✅ RESOLVED by 4B scale ablation. 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}. All correlation metrics maintained or improved at 4B (e.g. SciERC NER SJ_ρ: 0.3825→0.4221, +3.96pp). Combined with LLaMA-3.1-8B cross-architecture data, now have 3 model configurations (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B). 70B infeasible — acknowledge as limitation.
222	- **Priority**: P0, RESOLVED
223	
224	### R15: "Log-prob definition ambiguity — Eq.1 vs best-of-N ranking" (Dream 2 cross-tier, [W])
225	- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state "all best-of-N require N forward passes; log-prob adds zero ranking overhead."
226	- **Priority**: P0, Paper Agent handles
227	
228	### R16: "Zero figures — data-rich paper with only tables" (Dream 2 cross-tier, [W])
229	- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.
230	- **Priority**: P0, Paper Agent handles
231	
232	### R17: "Diagnostic framework overclaimed — descriptive not prescriptive" (Dream 2 cross-tier, [M][W])
233	- **Mitigation**: Soften "diagnostic framework" to "diagnostic analysis" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.
234	- **Priority**: P0, Paper Agent handles
235	
236	### R18: "No discussion of when consistency WOULD help" (Dream 2 cross-tier, [W])
237	- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.
238	- **Priority**: P1, Paper Agent handles
239	
240	### R19: "Negative result partially predictable for fine-tuned models" (Dream 2 cross-tier, [W])
241	- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.
242	- **Priority**: P1, Paper Agent handles
243	
244	## Venue Fit
245	
246	EMNLP **Main Conference** target. Strengths:
247	- Systematic empirical comparison with mechanistic diagnosis (not just "signals don't work" but "here's exactly why")
248	- Two novel failure mechanisms (instance degeneracy + LP compression) + unifying capability trap insight
249	- Controlled ablation (free-form decoding) providing causal evidence
250	- Cross-model (Qwen3-8B/4B + LLaMA-3.1-8B), cross-dataset (SciERC + CoNLL + WNUT), cross-task (NER + RE) validation
251	
252	Main Conference gap vs Findings:
253	- **Need**: 3rd NER dataset (Few-NERD) to close "only 2 NER datasets" concern
254	- **Need**: 3rd seed for Fisher p-value power on key claims
255	- **Need**: LoRA rank=8 ablation to confirm fine-tuning degree doesn't drive degeneracy
256	- **Need**: Systematic claim audit resolving numerical contradictions
257	
258	Risk assessment:
259	- **Strongest asset**: Capability trap is a genuinely novel insight — no prior work connects model capability to vanishing TTS headroom via degeneracy
260	- **Weakest flank**: Dataset breadth (2 NER + 1 RE → 3 NER + 1 RE with Few-NERD)
261	- **Critical path**: Few-NERD + 3rd seed experiments must complete before DDL (2026-05-25, 9 days)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "908f34a1-2ddf-40f1-99d7-bbce8ac16a26",
  "isSidechain": false,
  "promptId": "213d3fd3-ae42-4274-a194-17aa7930521a",
  "type": "user",
  "uuid": "74d7184c-ca25-46c9-8cba-f1d6d5bc3e98",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/paper_framing.md",
      "content": "# Paper Framing — struct_self_consist_ie\n\n> Updated 2026-05-16 — D116: Dream full review feedback → Reframe to DUAL CONTRIBUTION (QE positive + selection diagnostic). D113: Table 2 macro F1 unified (Greedy=0.645, LP=0.647, all p>0.05). exp-023: LoRA rank=8 degeneracy 7.2% vs 21% but selection still fails → multi-causal (not just degeneracy). Trained verifier baseline (logistic regression on 5 signals) in progress. R² on n=3 must be caveated as qualitative only.\n\n## Target Venue\n- Primary: EMNLP 2026 **Main Conference** (via ARR May 2026)\n- Deadline: ARR May cycle, 2026-05-25\n\n## Core Claims (D116 updated — DUAL CONTRIBUTION: QE positive + selection diagnostic)\n\n### Claim 1 (PRIMARY — Dual Contribution: QE Framework + Selection Diagnostic)\n**Positive contribution (A)**: Confidence signals reliably predict structured IE output quality at the population level (AUROC up to 0.82, ρ up to 0.45), enabling practical QE/selective prediction.\n**Diagnostic contribution (B)**: These same signals universally fail to select better candidates from multiple samples. We diagnose the multi-causal failure: (1) instance degeneracy eliminates headroom for 4/5 signals; (2) LP compression eliminates it for the remaining one; (3) reducing degeneracy (LoRA rank=8: 7.2% vs 21%) increases oracle headroom but signals STILL cannot exploit it → low degeneracy is necessary but not sufficient → trained verifiers are the natural next step.\n\nThe framing is NOT \"selection fails\" (pure negative) but \"we show WHEN, WHY, and WHAT WOULD BE NEEDED for selection to work\" (diagnostic with constructive implications).\n\n**Three-layer argument + Capability Trap**:\n- Layer A (design property, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification — the \"methodological premise\" — not an empirical finding.\n- Layer B (empirical — instance degeneracy): 21-58% of instances produce identical F1 across all N samples, eliminating selection headroom. Within-instance ρ=0.524 (SciERC) and 0.994 (CoNLL) — signals ARE correlated within instances, but degeneracy makes this irrelevant. Non-degenerate instances show MBR closing 23-41% of oracle gap. Selection recovers T=1.0 sampling degradation (LP 0.647 vs Random 0.610, +3.7pp) but only matches T=0 greedy (0.645 macro) at 8× inference cost — zero marginal gain.\n- Layer C (empirical — LP compression): Logprob — the only per-sample signal — fails due to intrinsic score compression (median within-instance LP range = 0.041 nats). Entity-token LP shows 4× variance but WORSE selection (-2.0pp). Free-form ablation confirms compression is model/task intrinsic (std ratio 0.97).\n- **Capability Trap** (unifying insight, D111): Model capability → output convergence → instance degeneracy → vanishing selection headroom. Evidence: CoNLL (91% F1) → 58% degeneracy, SciERC (66% F1) → 21%, WNUT (48% F1) → ~0%. Scale dimension: 8B → 21% degen vs 4B → 10.4% on SciERC. This is NOT an \"artifact\" — it is a **consequence of capability**, a structural inevitability. The better the model, the less test-time scaling can help via unsupervised selection.\n\n**Distinction from MBR literature**: Eikema et al.'s MBR failure = utility function misalignment. Our failure = utility IS aligned (within-instance ρ=0.524) but headroom eliminated by degeneracy — qualitatively novel mechanism.\n\n**Key evidence (score compression)**:\n- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ: 0.08→0.39\n- Full set: logprob +0.6pp, bootstrap p=0.39, Cohen's d=0.038 (negligible), 95% CI [-3.0, +4.2]pp\n- Oracle headroom: NER +13pp, RE +18pp → information exists but signals can't access it\n\n**Key evidence (free-form ablation)** [DONE — exp_freeform_ablation, NEGATIVE]:\n- LP distribution: constrained std=0.0206, free-form std=0.0199 (ratio 0.97, virtually unchanged)\n- Tied fraction: 59.7% → 57.7% (-2.0pp, negligible)\n- NER selection: +0.59pp → +0.18pp (both negligible vs greedy)\n- RE selection: -0.68pp → +1.69pp (flipped positive — secondary finding)\n- NER VC rho: 0.379 → 0.409 (slight QE improvement, selection still fails)\n- Parse rate: 99.95% (fine-tuned model retains JSON format without grammar)\n- **Conclusion**: Score compression is model/task intrinsic. The gap is universal.\n\n**Key evidence (scale ablation)** [DONE — 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}]:\n- CoNLL NER: 4B greedy_f1=0.9234 (>8B 0.9123, +1.11pp), SJ_ρ=0.4217 (≈8B 0.4357, −1.4pp), FK_ρ=0.4181 (>8B 0.3998, +1.83pp)\n- SciERC NER: 4B SJ_ρ=0.4221 (>8B 0.3825, +3.96pp), FK_ρ=0.3258 (>8B 0.2590, +6.68pp)\n- SciERC RE: 4B SJ_ρ=0.2673 (>8B 0.2441, +2.32pp), FK_ρ=0.3593 (>8B 0.2782, +8.11pp); struct>surface ✗ at both scales\n- **Conclusion**: Correlation strength maintained or improved at 4B across all 4 cells. The gap originates from within-instance signal misalignment, not model capacity. Task difficulty (SciERC RE zero-F1 rate) remains the primary driver, consistent across scales.\n- CoNLL 4B headroom: 1.70pp (vs 8B 4.20pp) → MARGINAL for selection power, but QE correlations robust\n- SciERC RE 4B: 47.6% zero-F1, RE LP_ρ_cond=0.1135 (p=0.074, n.s.) → confirms binary dominance at 4B\n- **4B selection results** (correlation-selection gap at 4B):\n  - CoNLL NER 4B (n=2756): SJ +0.07pp, FK +0.03pp, LP +0.09pp vs greedy 0.9213. All ≤0.1pp — MARGINAL (headroom 1.70pp)\n  - SciERC NER 4B (n=529): SJ **-1.49pp**, FK -1.56pp, LP -2.23pp vs greedy 0.6622. Oracle 0.7925 (+13.02pp). **All signals WORSE than greedy despite 13pp oracle headroom — gap confirmed at 4B**\n  - SciERC NER 4B gap demonstration: SJ-FK ρ gap = +0.096 (strong correlation advantage), SJ-FK selection F1 gap = +0.0007 (zero selection advantage) → correlation-selection gap quantified at 4B\n- **n_samples confound control**: Qwen3-8B n=8 data exists as control. CoNLL SJ: n8 ρ=0.4389 → n16 ρ=0.4496 (Δ=0.011, CI crosses zero). SciERC SJ: n8→n16 Δ=0.066, CI=[0.004, 0.128] weak effect. n_samples not a confound for 4B-8B comparison.\n- **Paper framing**: \"Scale ablation shows the gap is not an artifact of a particular model size; correlation strength is maintained at 4B, confirming that the gap originates from within-instance signal misalignment rather than model capacity.\"\n\n**exp-019 supervised verifier**: IN PROGRESS (D116 Dream feedback — all 3 tiers flagged as critical gap). Simplified to logistic regression on 5 signals (scikit-learn, CPU, ~30min). If supervised verifier partially closes oracle gap → proves gap IS closable, signals carry information but unsupervised heuristics are too weak. Grounds the \"what would be needed\" part of Contribution B.\n\n**exp-023 LoRA rank=8 ablation** [DONE]: rank=8 vs rank=32 on SciERC. Degeneracy: 7.2% vs 21% (3× reduction). Oracle headroom: 16.0pp vs 13.3pp. But ALL selection methods still fail to beat greedy (LP -0.5pp, SJ -0.9pp). QE correlation preserved (VC ρ=0.394, SJ ρ=0.365). **Key insight**: Reducing degeneracy is NECESSARY but NOT SUFFICIENT — signals themselves lack the discriminative power to exploit increased headroom. Strengthens multi-causal argument and points to trained verifiers as the path forward. Dream 三档公认最强实验。\n\n**Bonus finding (parse rate)**: Free-form parse rate 99.95% (4406/4408) — fine-tuned 8B model generates valid JSON without grammar constraints. Challenges intro:19 claim about constrained decoding necessity for format compliance.\n\n**Implications**: Not just \"signals don't work\" but \"here's WHY they don't work (intrinsic score compression), here's proof it's universal (controlled ablation via elimination), and here's the forward direction (breaking LP compression requires fundamentally different approaches — trained verifiers, multi-round refinement — not simply relaxing decoding constraints).\"\n\n### Claim 2 (METHODOLOGY — QE Evaluation Framework)\nSystematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. This is the methodological infrastructure, not a primary contribution.\n\n**Key results**:\n- NER: EM AUROC 0.749, voting_conf ρ=0.379, SJ ρ=0.360 — all >> logprob (AUROC 0.578, ρ=0.205). 3-seed consistent: SJ > FK delta=0.093~0.122\n- RE (3-seed confirmed): **LP > SJ > FK** (mean ρ: LP 0.302, SJ 0.265, FK 0.254). Signal ranking reverses vs NER — structural signals lose advantage when 43-45% of RE samples have F1=0 (binary signal dominance). LP's coarse but stable generation-confidence signal captures \"did the model get any relations right\" better than structural overlap measures.\n- Difficulty-dependent signal ranking: WNUT-17 conditional collapse (ρ significant → n.s.) + logprob ρ=−0.410 (non-obvious: overconfidence on OOD)\n- Temperature robustness: SJ Δρ=±0.01 vs FK Δρ=±0.06-0.09. T=0.7: LP full ρ improves 0.205→0.249, LP cond ρ 0.154→0.185; FK 0.267→0.289 despite more compression → concentrated signal hypothesis (non-tied instances at lower T carry more informative variance). **Paper citation rule**: robustness/temperature tables use full ρ; score compression analysis uses cond ρ. Always annotate which variant.\n- **Task-dependent signal effectiveness** (new finding from RE 3-seed): The optimal signal family depends on task structure. NER (token-level, graded F1) → structural agreement captures quality gradients. RE (relation-level, binary-dominated F1) → logprob captures generation confidence better. This is NOT a weakness — it's a nuanced finding that enriches the diagnostic framework.\n\n**Evidence preserved from original Claim 1** (SciERC, N=8, T=1.0, exp_012_rerun_1024):\n- NER full (n=529): ρ — voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205; AUROC — EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578\n- RE full (n=397): AUROC — EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601\n- ECE (NER): EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706\n\n### Claim 2b (Selection evidence)\n**exp_016_rerun_1024 evidence** (SciERC 8B, N=8, T=1.0):\n- NER best-of-N (n=529): logprob 0.6501 > sj 0.6450 = ensemble 0.6450 > greedy 0.6439 > voting 0.6337 > random 0.6077 (oracle 0.7758)\n- RE best-of-N (n=397): greedy 0.4042 > logprob 0.3948 > sj 0.3855 = ensemble 0.3855 > voting 0.3592 > random 0.3544 (oracle 0.5850)\n\n**4B selection evidence** (N=8, T=1.0):\n- CoNLL NER 4B (n=2756): greedy 0.9213, SJ 0.9220 (+0.07pp), FK 0.9215, LP 0.9221 (+0.09pp), oracle 0.9382. Headroom 1.70pp → selection indistinguishable\n- SciERC NER 4B (n=529): greedy 0.6622, SJ 0.6473 (-1.49pp), FK 0.6466 (-1.56pp), LP 0.6399 (-2.23pp), oracle 0.7925 (+13.02pp). **All signals worse than greedy** → correlation-selection gap at 4B confirmed\n\n**exp_016_rerun_1024_bootstrap evidence** (3-seed bootstrap, 1000 iterations):\n- NER logprob vs greedy: bootstrap 95% CI [−0.030, +0.042], permutation p=0.39\n- Effect size: Cohen's d=0.038 (negligible), sign test win rate=0.466\n\n### Claim 3 (Diagnostic — task-complexity boundary + task-dependent signal effectiveness)\nThe effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.\n\n**RE 3-seed mechanism** (D073, confirmed at 4B): 43-47% of RE samples have F1=0 (8B: 43-45%, 4B: 47.6%), creating binary-dominated signal distributions where structural overlap (SJ/FK) cannot differentiate quality gradients. Pattern consistent across model scales — confirming task difficulty, not model capacity, drives this boundary. LP's generation confidence captures \"complete failure vs partial success\" more reliably. 3-seed RE QE: LP ρ=0.302 > SJ 0.265 > FK 0.254. **Definitive binary dominance evidence**: RE LP full ρ=0.266 but cond ρ=0.011 (p=0.86, completely n.s.) — LP's entire RE signal comes from the zero/nonzero F1 split; once conditioned on samples where the model extracts at least one relation, LP has zero predictive power for RE quality gradients. In contrast, NER LP cond ρ remains informative (0.154–0.185). This provides the concrete mechanism for Claim 3's task-complexity boundary: it's not just \"compound error\" in the abstract — it's specifically the high zero-F1 rate that shifts the optimal signal family from structural to probabilistic, and LP's RE advantage is entirely a binary classification effect, not genuine quality estimation.\n\n**MVP evidence**: RE full vs cond AUROC lift — EM: 0.706→0.752 (+4.6pp), SJ: 0.670→0.646 (−2.4pp, 待确认), voting_conf: 0.694→0.642 (−5.2pp, 待确认). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.\n\n**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.\n\n**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):\n- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10\n- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392\n- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.\n- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.\n\n## Story Spine (D116 — Dual Contribution: QE Positive + Selection Diagnostic, Main Conference)\n\n**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured information extraction is unclear. Practitioners need to know: (1) can confidence signals estimate output quality? (2) can they select better outputs?\n\n**Existing approaches & gaps**: Self-consistency (Wang et al. 2023) succeeds for discrete-answer reasoning. MBR decoding succeeds for MT. But structured IE outputs (entity sets, relation triples) present a fundamentally different challenge — prior work conflates quality estimation with selection. We decouple these and show they are governed by different factors.\n\n**Our framing (D116 — DUAL CONTRIBUTION)**:\n\n**Contribution A (Positive — QE Framework)**: Five confidence signals across four families reliably predict structured IE output quality (AUROC 0.82, ρ 0.45). Signal ranking is task-dependent: structural > probabilistic for NER, reversed for RE. This QE framework has practical value for selective prediction / error flagging regardless of selection effectiveness.\n\n**Contribution B (Diagnostic — Why Selection Fails + What Would Fix It)**:\n1. **Design property**: 4/5 signals are instance-level aggregates → cannot rank candidates by construction.\n2. **Instance Degeneracy**: 21-58% of instances produce identical F1 across all N samples, eliminating selection headroom.\n3. **LP Compression**: Logprob within-instance range compressed (0.041 nats). Free-form ablation confirms intrinsic (std ratio 0.97).\n4. **Multi-causal** (key D116 update): LoRA rank=8 reduces degeneracy 3× (7.2% vs 21%) and increases oracle headroom (+2.7pp), but ALL selection methods still fail to beat greedy → low degeneracy is NECESSARY but NOT SUFFICIENT. Signals lack discriminative power even when headroom exists.\n5. **Capability-degeneracy tradeoff** (renamed from \"trap\"): Higher capability → more convergence → more degeneracy. Qualitative monotone relationship across datasets (CoNLL 91%→58% degen, SciERC 66%→21%). R² on n=3 is illustrative only, not statistically reliable.\n6. **Path forward**: Non-tied subset +2.9pp (p=0.004) proves signals carry information. Trained verifier baseline (logistic regression on 5 signals, in progress) tests whether the gap is closable with supervision. If so → unsupervised signals are weak, not uninformative.\n\n**QE-vs-Selection Decoupling** (Dream-identified most novel insight): QE correlation (SJ ρ) is stable across LoRA rank configurations (0.360→0.378) while selection gap changes dramatically. Signals are ALWAYS useful for flagging uncertain instances, even when they cannot improve selection. This distinction has practical implications beyond IE.\n\n**Headline**: \"We present a dual contribution for structured IE: (1) a QE framework showing confidence signals reliably predict output quality (AUROC 0.82), and (2) a diagnostic analysis revealing why these same signals fail at selection — instance degeneracy and logprob compression create a multi-causal gap that persists even when degeneracy is reduced. Selection approximately matches greedy decoding (Δ<0.3pp, all p>0.05) despite 13pp oracle headroom.\"\n\n**Title**: \"Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction\"\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Only one NER dataset — generalization unclear\"\n- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.\n- **Priority**: P0\n\n### R2: \"Only one model family (Qwen3-8B)\"\n- **Mitigation**: LLaMA-3.1-8B shows model-agnostic effect. ⚠️ **exp-007 数据被污染 (test data leakage)**，LLaMA SciERC 正确值来自 exp_018 (clean rerun)。unified_rho_full.json 的 LLaMA SciERC 条目必须替换为 exp_018 数据。正确 LLaMA SciERC N=8 3-seed mean: SJ 0.325, FK 0.256, VC 0.384, EM 0.279, LP 0.162。\n- **Priority**: P0\n\n### R3: \"FK is a strawman baseline — what about log-prob, USC, exact-match?\"\n- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (EM+SJ+voting) >> log-prob >> FK. USC discussed in related work (LLM-as-judge, orthogonal approach).\n- **Priority**: P0, RESOLVED — results decisive\n\n### R3b: \"EM beats voting_conf and SJ on AUROC — why present SJ/voting_conf?\"\n- **Mitigation**: EM is a strict binary signal (all-or-nothing match); SJ captures partial agreement and generalizes to arbitrary structured outputs (relations, events). Voting_conf provides granular entity-level scores. NER full AUROC: EM 0.749 > SJ 0.692 > voting_conf 0.684, but ρ: voting_conf 0.379 > SJ 0.360 > EM 0.295. EM excels at binary discrimination but underperforms on rank ordering. SJ is also more temperature-robust (Δρ=±0.01). Paper presents all three as complementary instantiations of the structural consistency principle: EM for go/no-go filtering, voting_conf for ranking, SJ for generalizability.\n- **Priority**: P1 — narrative adjusted for 1024-token results\n\n### R4: \"No actual TTS improvement demonstrated\"\n- **Status**: ✅ CONFIRMED by exp_016_rerun_1024_bootstrap. No signal significantly outperforms greedy on either task. NER logprob +0.6pp not significant (bootstrap p=0.39, 95% CI [−0.030, +0.042], Cohen's d=0.038). RE: greedy > all signals.\n- **Mitigation**: Paper PIVOTS to \"confidence estimation + correlation-selection gap analysis.\" exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.\n- **Priority**: P0 — narrative pivot complete, bootstrap confirms\n\n### R5: \"Sample size N=8 may be too small for reliable SJ estimation\"\n- **Mitigation**: exp-001 (N=16) with multi-seed robustness\n- **Priority**: P0\n\n### R6: \"Conditional analysis cherry-picks favorable instances\"\n- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.\n- **Priority**: P0 (add sensitivity analysis)\n\n### R7: \"Only ρ as evaluation metric\"\n- **Mitigation**: Add AUROC, calibration plots (ECE), Kendall's τ for all experiments. ECE data now available: NER best calibrated = EM (0.353), RE best = voting (0.272). Logprob worst calibrated (NER 0.706, RE 0.769).\n- **Priority**: P0\n\n### R8: \"Formula-implementation discrepancy\"\n- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)\n- **Priority**: P0, paper writing fix\n\n### R9: \"Evaluation circularity (T>0 consistency vs T=0 F1)\"\n- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).\n- **Priority**: P0\n\n### R10: \"Insufficient related work\" (三档一致 [B][M][W])\n- **Mitigation**: Expand to 35+ references. Must cite:\n  - USC (Chen 2024) — empirical differentiation, not just citation\n  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)\n  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021\n  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020\n  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016\n  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023\n  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024\n  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022\n  - **IE confidence**: Culotta & McCallum 2004\n  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)\n  - **[2025-2026 新颖性自查补充 — 必引]**:\n    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出\n    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap\n    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案\n    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量\n    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction\"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承\"overlooks semantically consistent outputs\"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机\n  - **[2025-2026 新颖性自查补充 — 应引]**:\n    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述\n    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述\n    - Semantic Entropy Probes (2024) — 低成本不确定性估计\n    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性\n    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务\n    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关\n    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位\n    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE\n    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE\n  - **需新增 Related Work 小节**:\n    - \"Test-Time Scaling & Sample Selection\" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap\n    - \"Consistency for Structured IE\" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation\n- **Priority**: P0, Paper Agent handles\n\n### R11: \"SJ+logprob ensemble missing\" (Dream 2 — both reviewers)\n- **Status**: ⚠️ REVISED by exp_016_rerun_1024. Results:\n  - Ensemble AUROC (5-fold CV LR): NER 0.666 ± 0.070, RE 0.662 ± 0.078\n  - Best single signal EM: NER AUROC 0.749, RE AUROC 0.706\n  - **Ensemble has NO advantage over best single signal** — EM alone outperforms the 5-signal logistic regression ensemble by +8.3pp (NER) and +4.4pp (RE)\n  - **Interpretation**: With 1024-token clean data, EM captures nearly all discriminative information. The ensemble's inferior performance likely reflects overfitting in the 5-fold CV LR with correlated features. This further supports presenting EM as a simple, strong baseline within the structural consistency family.\n- **Priority**: DONE — write into paper with honest interpretation (no ensemble advantage claim)\n\n### R12: \"No supervised upper bound / reward model comparison\" (Dream 2)\n- **Mitigation**: exp-016 LR ensemble (5-signal, 5-fold CV) underperforms best single signal EM (AUROC 0.666 vs 0.749), suggesting feature redundancy. exp-019 supervised verifier SKIPPED (DDL risk + scope creep). Free-form ablation provides the \"so what\": gap is fundamental → closing it requires fundamentally different approaches (trained verifiers, not just better unsupervised signals). Positioned as future work with explicit motivation from ablation evidence.\n- **Priority**: P1, addressed via framing (future work motivated by ablation)\n\n### R13: \"Headroom capture rate low\" (Dream 2)\n- **Mitigation**: NER oracle 0.7758, greedy 0.6439, best signal (logprob) 0.6501 → captures 0.5% of headroom. RE oracle 0.5850, greedy 0.4042, best signal (greedy itself) → 0% capture. Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline and documents the gap.\n- **Priority**: P0, paper writing\n\n### R14: \"Cross-model validation thin — need more than 2×8B\" (Dream 2)\n- **Status**: ✅ RESOLVED by 4B scale ablation. 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}. All correlation metrics maintained or improved at 4B (e.g. SciERC NER SJ_ρ: 0.3825→0.4221, +3.96pp). Combined with LLaMA-3.1-8B cross-architecture data, now have 3 model configurations (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B). 70B infeasible — acknowledge as limitation.\n- **Priority**: P0, RESOLVED\n\n### R15: \"Log-prob definition ambiguity — Eq.1 vs best-of-N ranking\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state \"all best-of-N require N forward passes; log-prob adds zero ranking overhead.\"\n- **Priority**: P0, Paper Agent handles\n\n### R16: \"Zero figures — data-rich paper with only tables\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.\n- **Priority**: P0, Paper Agent handles\n\n### R17: \"Diagnostic framework overclaimed — descriptive not prescriptive\" (Dream 2 cross-tier, [M][W])\n- **Mitigation**: Soften \"diagnostic framework\" to \"diagnostic analysis\" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.\n- **Priority**: P0, Paper Agent handles\n\n### R18: \"No discussion of when consistency WOULD help\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.\n- **Priority**: P1, Paper Agent handles\n\n### R19: \"Negative result partially predictable for fine-tuned models\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.\n- **Priority**: P1, Paper Agent handles\n\n## Venue Fit\n\nEMNLP **Main Conference** target. Strengths:\n- Systematic empirical comparison with mechanistic diagnosis (not just \"signals don't work\" but \"here's exactly why\")\n- Two novel failure mechanisms (instance degeneracy + LP compression) + unifying capability trap insight\n- Controlled ablation (free-form decoding) providing causal evidence\n- Cross-model (Qwen3-8B/4B + LLaMA-3.1-8B), cross-dataset (SciERC + CoNLL + WNUT), cross-task (NER + RE) validation\n\nMain Conference gap vs Findings:\n- **Need**: 3rd NER dataset (Few-NERD) to close \"only 2 NER datasets\" concern\n- **Need**: 3rd seed for Fisher p-value power on key claims\n- **Need**: LoRA rank=8 ablation to confirm fine-tuning degree doesn't drive degeneracy\n- **Need**: Systematic claim audit resolving numerical contradictions\n\nRisk assessment:\n- **Strongest asset**: Capability trap is a genuinely novel insight — no prior work connects model capability to vanishing TTS headroom via degeneracy\n- **Weakest flank**: Dataset breadth (2 NER + 1 RE → 3 NER + 1 RE with Few-NERD)\n- **Critical path**: Few-NERD + 3rd seed experiments must complete before DDL (2026-05-25, 9 days)",
      "numLines": 261,
      "startLine": 1,
      "totalLines": 261
    }
  },
  "sourceToolAssistantUUID": "908f34a1-2ddf-40f1-99d7-bbce8ac16a26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T113255 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consi…",
  "leafUuid": "74d7184c-ca25-46c9-8cba-f1d6d5bc3e98",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1"
}
```

---

### Assistant

_source line 16 · 2026-05-16T11:51:44.837Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both files. Let me understand the task:

1. This is a "worst" tier dream paper, meaning it should reflect the weakest possible framing/reception of the research
2. The narrative guidance says to reframe around a SINGLE insight: the QE-selection decoupling as a general warning for TTS scaling
3. I need to create a complete LaTeX paper based on the experiment data
4. The experiments are:
   - ner_llama_conll: Cross-model validation with LLaMA on CoNLL
   - simple_verifier_baseline: Logistic regression verifier on 5 signals
   - claim_audit: Numerical consistency audit that informs how I present the data

So I'm working with three data sources total, where the audit serves as a validation layer for the numbers I'll report in the main experimental sections. The "worst" tier framing means I should focus narrowly on the QE-selection decoupling as a cautionary finding rather than trying to position multiple contributions.

I'm reconsidering the paper's angle: instead of IE-specific results, I can frame this as a methodological critique of how quality signals fail to transfer from population-level to instance-level selection in TTS systems. The degeneracy I'm seeing becomes a case study in how high-performance systems can develop spurious correlations. My ablation work and the rank=8 constraint become the controlled experimental methodology that supports this broader claim about TTS evaluation paradigms.

Now I'm cross-referencing the actual numbers from the data—the SciERC greedy baseline at 0.644 F1 and the oracle performance ceiling—to make sure I'm using the correct values throughout the paper.

Looking at the selection results across different signals, they all cluster near the greedy baseline with no meaningful improvement, and even with LoRA rank=8 reducing degeneracy from 21% to 7.2%, the selection mechanism still fails to outperform. The free-form ablation shows compression is intrinsic to the system, and the cross-model analysis reveals the signals don't generalize—LLaMA and Qwen produce nearly identical rankings on CoNLL despite different architectures. The supervised verifier barely closes the gap to oracle performance, which reinforces that the problem isn't fixable with more supervision.

For the AUROC claims, I need to be precise: the maximum I observed is 0.749 on SciERC EM, with CoNLL reaching 0.816, so I'll report these separately rather than overstating with a single number.

Now I'm structuring this as a position paper with the title framing transfer-to-selection as a fundamental failure mode. I'll organize it as a full ACL-format paper covering the abstract, introduction positioning this against TTS scaling claims, related work, method definitions, comprehensive experiments, and analysis of why these signals break down at the instance level.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74d7184c-ca25-46c9-8cba-f1d6d5bc3e98",
  "isSidechain": false,
  "requestId": "req_011Cb6CVj5eDR9MtjjehVWDA",
  "type": "assistant",
  "uuid": "3137fa8a-ebdb-4e6d-8449-ec5bca180df2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mftcMRSYSozJBjK6vEtns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14930,
      "cache_read_input_tokens": 23107,
      "output_tokens": 1031,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1031,
          "cache_read_input_tokens": 23107,
          "cache_creation_input_tokens": 14930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14930
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

_source line 17 · 2026-05-16T11:51:44.840Z_

Now I have the data. Let me write the paper with the "worst" tier framing — position paper flavor focused on QE-selection decoupling as a general TTS methodology warning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3137fa8a-ebdb-4e6d-8449-ec5bca180df2",
  "isSidechain": false,
  "requestId": "req_011Cb6CVj5eDR9MtjjehVWDA",
  "type": "assistant",
  "uuid": "a93427eb-012d-40ac-ab8b-3b269f4af25c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mftcMRSYSozJBjK6vEtns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14930,
      "cache_read_input_tokens": 23107,
      "output_tokens": 1031,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1031,
          "cache_read_input_tokens": 23107,
          "cache_creation_input_tokens": 14930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14930
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

_source line 18 · 2026-05-16T11:51:47.257Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01G4nokXdY8UgKDSJ2E7iMvQ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a93427eb-012d-40ac-ab8b-3b269f4af25c",
  "isSidechain": false,
  "requestId": "req_011Cb6CVj5eDR9MtjjehVWDA",
  "type": "assistant",
  "uuid": "691a2737-d9ec-4cc4-827e-d16a02e806d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mftcMRSYSozJBjK6vEtns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14930,
      "cache_read_input_tokens": 23107,
      "output_tokens": 1031,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1031,
          "cache_read_input_tokens": 23107,
          "cache_creation_input_tokens": 14930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14930
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

_source line 19 · 2026-05-16T11:51:47.428Z_

<details><summary>↩ Tool result · `toolu_01G4nokXdY8UgKDSJ2E7iMvQ`</summary>

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
  "parentUuid": "691a2737-d9ec-4cc4-827e-d16a02e806d1",
  "isSidechain": false,
  "promptId": "213d3fd3-ae42-4274-a194-17aa7930521a",
  "type": "user",
  "uuid": "fc82ba68-4a5d-4844-96e9-79bd5ebf0143",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "691a2737-d9ec-4cc4-827e-d16a02e806d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-16T11:54:13.936Z_

<details open><summary>🔧 Tool call — Write · `toolu_01K3UdTPEPdPLoHJzJbrNQv2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\n\\title{Not All Correlations Transfer: When Population-Level Quality Signals\\\\Fail at Instance-Level Selection}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nTest-time scaling (TTS) via multi-sample generation assumes that confidence signals which correlate with output quality at the population level can also select better candidates at the instance level. We demonstrate that this assumption fails for structured information extraction. Across three datasets (SciERC, CoNLL-2003, WNUT-17), three models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B), and five confidence signal families, we find a consistent \\emph{correlation--selection gap}: signals achieve moderate quality estimation performance (Spearman $\\rho$ up to 0.45, AUROC up to 0.75) yet fail to select outputs that improve over greedy decoding ($\\Delta < 0.3$pp, all $p > 0.05$) despite 13pp oracle headroom. We identify two causal mechanisms---instance degeneracy (21--58\\% of instances yield identical quality across samples) and logprob score compression (within-instance range 0.041 nats)---and show via controlled ablations that neither is an artifact of decoding constraints or model capacity. A supervised verifier combining all five signals closes only 3.2\\% of the oracle gap, confirming that the information deficit is fundamental. We argue this gap is an inevitable consequence of high model capability and constitutes a general warning for TTS scaling beyond discrete-answer tasks.\n\\end{abstract}\n\n\\section{Introduction}\n\nTest-time scaling (TTS) has emerged as a powerful paradigm for improving language model outputs: generate multiple candidates, then select the best one using a quality signal. This approach yields consistent gains for mathematical reasoning \\cite{wang2023selfconsistency}, code generation \\cite{chen2021codex}, and machine translation \\cite{eikema2022sampling}. The implicit promise is general---if a signal correlates with quality, it should enable selection.\n\nWe show this promise is fundamentally overfit to discrete-answer tasks. For structured information extraction (IE)---where outputs are entity sets or relation triples rather than single tokens---the correlation between confidence signals and output quality does \\emph{not} transfer from population-level estimation to instance-level selection.\n\nThis finding matters beyond IE. Any task where a capable model produces near-deterministic outputs will exhibit the same phenomenon: quality signals that work for estimation become useless for selection because there is nothing meaningfully different to select \\emph{from}. We term this the \\textbf{correlation--selection gap} and argue it represents a structural limitation of unsupervised TTS scaling for high-performance systems.\n\nOur contribution is methodological: we formalize the distinction between quality estimation (QE) and candidate selection, demonstrate that conflating them leads to incorrect conclusions about TTS effectiveness, and provide controlled experimental evidence for the causal mechanisms. Specifically:\n\n\\begin{enumerate}\n\\item We show that five confidence signals across four families achieve moderate QE performance ($\\rho$ up to 0.45, AUROC up to 0.75) but uniformly fail at selection ($\\Delta < 0.3$pp vs.\\ greedy, all $p > 0.05$).\n\\item We identify two mechanisms: \\emph{instance degeneracy} (model capability $\\rightarrow$ output convergence $\\rightarrow$ vanishing headroom) and \\emph{logprob compression} (within-instance score range too narrow for discrimination).\n\\item We demonstrate via LoRA rank ablation that reducing degeneracy is necessary but not sufficient---signals still cannot exploit increased headroom---establishing the gap as multi-causal.\n\\item A supervised verifier baseline closing only 3.2\\% of oracle gap confirms the information deficit is not merely a threshold problem but a fundamental limitation of these signal families.\n\\end{enumerate}\n\nThe correlation--selection gap connects to broader phenomena in machine learning: reward hacking in RLHF (where reward signals correlate with quality at the population level but fail to improve individual outputs), mode collapse in generative models, and the diminishing returns of best-of-N sampling as model capability increases. Our work provides the first controlled experimental documentation of this gap in a structured prediction setting.\n\n\\section{Related Work}\n\n\\paragraph{Test-Time Scaling.} Self-consistency \\cite{wang2023selfconsistency} demonstrates that majority voting over chain-of-thought samples improves reasoning accuracy. Recent extensions include CISC \\cite{cisc2025} (confidence-weighted voting), Self-Certainty Best-of-N \\cite{selfcertainty2026} (KL-divergence selection), and ReASC \\cite{reasc2026} (reliability-aware adaptive sampling). All target discrete-answer tasks where selection is well-defined. Snell et al.\\ (\\citeyear{snell2024scaling}) and Brown et al.\\ (\\citeyear{brown2024tts}) formalize TTS scaling laws but assume monotone selection improvement with sample count---an assumption we show fails for structured outputs.\n\n\\paragraph{Confidence and Uncertainty Estimation.} Semantic entropy \\cite{kuhn2023semantic}, calibration methods \\cite{kadavath2022language,guo2017calibration}, and LLM confidence surveys \\cite{uqsurvey2025,confsurvey2024} focus on population-level quality estimation. SelfCheckGPT \\cite{manakul2023selfcheckgpt} uses consistency for hallucination detection (a QE task). CoCoA \\cite{cocoa2025} combines confidence and consistency for uncertainty quantification in QA/summarization. None distinguish QE from selection or test whether population-level correlations transfer to instance-level ranking.\n\n\\paragraph{Structured IE Confidence.} Culotta \\& McCallum (\\citeyear{culotta2004confidence}) study confidence for CRF-based extraction. N\\'{e}dellec \\& Xia (\\citeyear{nedellec2026}) examine consistency--accuracy correlations for hard-prompted LLMs on entity/relation extraction, finding moderate correlations with surface-level string matching. Their work does not study best-of-N selection or multiple signal families, and their surface matching limitation (acknowledged as missing semantically consistent outputs) motivates our structural Jaccard metric.\n\n\\paragraph{MBR Decoding.} Eikema et al.\\ (\\citeyear{eikema2022sampling}) document MBR failure modes in MT. Their mechanism (utility function misalignment) differs from ours: in our setting, the utility \\emph{is} aligned at the instance level ($\\rho = 0.52$ within instances) but headroom is eliminated by output convergence.\n\n\\paragraph{Verifiers and Reward Models.} Cobbe et al.\\ (\\citeyear{cobbe2021training}) and Lightman et al.\\ (\\citeyear{lightman2023lets}) train verifiers for mathematical reasoning. Our supervised baseline tests whether a simple verifier on unsupervised signals can close the gap, finding it cannot---suggesting the gap requires access to input representations, not just output statistics.\n\n\\section{Method}\n\n\\subsection{Problem Formulation}\n\nGiven a structured IE task with input $x$ and a language model $M$, we generate $N$ candidate outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$. We define two distinct objectives:\n\n\\textbf{Quality Estimation (QE):} Assign a score $s(y_i)$ such that $\\text{rank}(s(y_i))$ correlates with $\\text{rank}(F_1(y_i, y^*))$ across the test population.\n\n\\textbf{Candidate Selection:} Choose $\\hat{y} = \\arg\\max_i s(y_i)$ such that $F_1(\\hat{y}, y^*) > F_1(y_{\\text{greedy}}, y^*)$.\n\nThese objectives are related but not equivalent. QE requires only \\emph{population-level} rank correlation; selection requires \\emph{instance-level} discrimination among near-identical candidates. We argue that conflating them has led to overoptimistic conclusions about TTS for structured tasks.\n\n\\subsection{Confidence Signals}\n\nWe evaluate five signals spanning four families:\n\n\\paragraph{Structural Consistency.} \\textbf{Structural Jaccard (SJ):} Mean pairwise Jaccard similarity over predicted entity/relation sets using type-grouped Hungarian matching. \\textbf{Fuzzy-match Kendall (FK):} Kendall correlation over soft entity alignments.\n\n\\paragraph{Probabilistic.} \\textbf{Log-probability (LP):} Mean token-level log-probability of the generation.\n\n\\paragraph{Voting-based.} \\textbf{Voting Confidence (VC):} Entity-level frequency across $N$ samples.\n\n\\paragraph{Agreement-based.} \\textbf{Exact Match (EM):} Fraction of $N$ samples producing identical output.\n\n\\subsection{Datasets and Models}\n\n\\textbf{Datasets:} SciERC \\cite{luan2018scierc} (NER + RE), CoNLL-2003 \\cite{sang2003conll} (NER), WNUT-17 (NER, OOD setting).\n\n\\textbf{Models:} Qwen3-8B (primary), Qwen3-4B (scale ablation), LLaMA-3.1-8B (cross-architecture validation). All fine-tuned with LoRA (rank 32 default, rank 8 for ablation) on task-specific training splits.\n\n\\textbf{Generation:} $N = 8$ samples at $T = 1.0$ (default), with $N = 16$ for scaling analysis. Greedy decoding ($T = 0$) as selection baseline.\n\n\\subsection{Evaluation Protocol}\n\n\\textbf{QE metrics:} Spearman $\\rho$ (full population and conditional on non-degenerate instances), AUROC (binary: above/below median $F_1$), ECE.\n\n\\textbf{Selection metrics:} Best-of-N $F_1$ for each signal vs.\\ greedy $F_1$. Statistical significance via 1000-iteration bootstrap with permutation $p$-values.\n\n\\textbf{Oracle:} $\\max_i F_1(y_i, y^*)$ --- the best achievable selection from the candidate set.\n\n\\section{Experiments}\n\n\\subsection{Quality Estimation Results}\n\nTable~\\ref{tab:qe_main} shows QE performance on SciERC (primary evaluation set, $N = 8$, $T = 1.0$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\rho$ (NER) & AUROC (NER) & $\\rho$ (RE) & AUROC (RE) \\\\\n\\midrule\nVC & 0.379 & 0.684 & --- & 0.694 \\\\\nSJ & 0.360 & 0.692 & 0.265 & 0.670 \\\\\nEM & 0.295 & 0.749 & --- & 0.706 \\\\\nFK & 0.267 & 0.629 & 0.254 & 0.609 \\\\\nLP & 0.205 & 0.578 & 0.302 & 0.601 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Quality estimation on SciERC ($n=529$ NER, $n=397$ RE). All $\\rho$ values $p < 0.001$. Structural signals dominate for NER; LP dominates for RE---signal ranking is task-dependent.}\n\\label{tab:qe_main}\n\\end{table}\n\nAll signals achieve statistically significant QE correlations. EM achieves the highest AUROC (0.749 NER, 0.706 RE) while VC achieves the highest $\\rho$ for NER (0.379). Notably, signal ranking reverses between tasks: structural signals (SJ, FK) dominate NER while LP dominates RE, explained by the 43--45\\% zero-$F_1$ rate in RE creating binary-dominated distributions where generation confidence outperforms structural overlap.\n\n\\subsection{Selection Results: The Correlation--Selection Gap}\n\nDespite moderate QE performance, no signal achieves statistically significant selection improvement over greedy decoding (Table~\\ref{tab:selection}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & NER $F_1$ & $\\Delta$ & RE $F_1$ & $\\Delta$ \\\\\n\\midrule\nGreedy ($T=0$) & 0.644 & --- & 0.404 & --- \\\\\n\\midrule\nLP (best-of-8) & 0.650 & +0.6 & 0.395 & $-$0.9 \\\\\nSJ (best-of-8) & 0.645 & +0.1 & 0.386 & $-$1.9 \\\\\nEM (best-of-8) & 0.645 & +0.1 & 0.386 & $-$1.9 \\\\\nVC (best-of-8) & 0.634 & $-$1.0 & 0.359 & $-$4.5 \\\\\nRandom & 0.608 & $-$3.6 & 0.354 & $-$5.0 \\\\\n\\midrule\nOracle & 0.776 & +13.2 & 0.585 & +18.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selection results on SciERC ($N=8$, $T=1.0$). $\\Delta$ in percentage points vs.\\ greedy. NER LP: bootstrap $p = 0.39$, 95\\% CI $[-3.0, +4.2]$pp, Cohen's $d = 0.038$. Oracle headroom is 13--18pp but no signal captures more than 0.6pp.}\n\\label{tab:selection}\n\\end{table}\n\nThe gap is stark: 13.2pp oracle headroom exists for NER, yet the best signal (LP) captures only 0.6pp---0.5\\% of available headroom, not statistically significant ($p = 0.39$). For RE, all signals perform \\emph{worse} than greedy. This is not a statistical power issue: the 95\\% CI for the best signal excludes gains beyond 4.2pp, while 13pp is available.\n\n\\subsection{Cross-Model Validation}\n\nTo test whether the gap is model-specific, we evaluate LLaMA-3.1-8B on CoNLL-2003 (Table~\\ref{tab:llama_conll}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\rho$ & AUROC & Sel.\\ $F_1$ & $\\Delta$ vs Greedy \\\\\n\\midrule\nSJ & 0.43 & 0.70 & 0.925 & +0.1pp \\\\\nFK & 0.42 & 0.70 & 0.924 & 0.0pp \\\\\nEM & 0.43 & 0.71 & 0.924 & 0.0pp \\\\\nLP & 0.31 & 0.76 & 0.925 & +0.1pp \\\\\nVC & 0.43 & 0.71 & 0.926 & +0.2pp \\\\\n\\midrule\nOracle & --- & --- & 0.945 & +2.1pp \\\\\nGreedy & --- & --- & 0.924 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LLaMA-3.1-8B on CoNLL-2003 ($N=8$, $T=1.0$). QE correlations ($\\rho = 0.31$--$0.43$) match Qwen3-8B ($\\rho = 0.44$), confirming model-agnostic QE. Selection gains $\\leq 0.2$pp with 2.1pp oracle headroom. Instance degeneracy: 56\\%.}\n\\label{tab:llama_conll}\n\\end{table}\n\nLLaMA-3.1-8B replicates the pattern: moderate QE correlations ($\\rho$ up to 0.43, AUROC up to 0.76) with negligible selection gains ($\\leq 0.2$pp). The high degeneracy rate (56\\%) on CoNLL---where greedy $F_1 = 0.924$---exemplifies the capability--degeneracy mechanism: high model capability compresses the candidate space.\n\n\\subsection{Supervised Verifier Baseline}\n\nIf unsupervised signals fail individually, can their combination succeed? We train a logistic regression verifier on all five signals with 5-fold cross-validation on SciERC (Table~\\ref{tab:verifier}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Sel.\\ $F_1$ & $\\Delta$ & AUROC & Gap Closed \\\\\n\\midrule\nGreedy & 0.644 & --- & --- & 0\\% \\\\\nBest single (EM) & 0.650 & +0.6pp & 0.749 & 4.6\\% \\\\\nLR Verifier (5-sig) & 0.648 & +0.4pp & 0.760 & 3.2\\% \\\\\nOracle & 0.776 & +13.2pp & --- & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Supervised verifier (logistic regression on 5 signals, 5-fold CV, SciERC NER). The verifier achieves marginally higher AUROC (0.760 vs 0.749) but \\emph{lower} selection $F_1$ than the best single signal, closing only 3.2\\% of oracle gap.}\n\\label{tab:verifier}\n\\end{table}\n\nThe supervised verifier closes 3.2\\% of the oracle gap---\\emph{less} than the best single signal (EM, 4.6\\%). Feature importance analysis reveals high inter-signal correlation (mean pairwise $\\rho = 0.45$--$0.72$), explaining why linear combination provides no advantage. The signals collectively contain negligible selection-relevant information beyond what any individual signal provides.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nFeature & LR Coeff. & Mean $\\rho$ w/ others \\\\\n\\midrule\nEM & 0.42 & 0.61 \\\\\nVC & 0.31 & 0.72 \\\\\nSJ & 0.18 & 0.68 \\\\\nLP & 0.06 & 0.45 \\\\\nFK & 0.03 & 0.59 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature importance and inter-signal correlation. High pairwise correlations explain why the ensemble cannot outperform the best single signal.}\n\\label{tab:feature_importance}\n\\end{table}\n\n\\subsection{Mechanism 1: Instance Degeneracy}\n\nWe define \\emph{instance degeneracy} as the fraction of test instances where all $N$ samples produce identical $F_1$ scores (within rounding). Across configurations:\n\n\\begin{itemize}\n\\item CoNLL-2003 (greedy $F_1 = 0.924$): 56--58\\% degeneracy\n\\item SciERC (greedy $F_1 = 0.644$): 21\\% degeneracy\n\\item WNUT-17 (greedy $F_1 \\approx 0.48$): $\\sim$0\\% degeneracy\n\\end{itemize}\n\nThe monotone relationship between model capability and degeneracy connects to mode collapse: as models improve, their outputs converge, eliminating the variation that selection requires. This is not a bug but a \\emph{structural consequence of capability}.\n\n\\paragraph{LoRA Rank Ablation.} To test whether degeneracy is an artifact of over-fitting (high LoRA rank), we compare rank 8 vs.\\ rank 32 on SciERC:\n\n\\begin{itemize}\n\\item Degeneracy: 7.2\\% (rank 8) vs.\\ 21\\% (rank 32) --- 3$\\times$ reduction\n\\item Oracle headroom: 16.0pp (rank 8) vs.\\ 13.3pp (rank 32)\n\\item Selection: LP $-$0.5pp, SJ $-$0.9pp vs.\\ greedy (rank 8)\n\\item QE preserved: VC $\\rho = 0.394$, SJ $\\rho = 0.365$ (rank 8)\n\\end{itemize}\n\nReducing degeneracy increases oracle headroom but signals \\emph{still} cannot exploit it. This establishes the multi-causal nature of the gap: low degeneracy is necessary but not sufficient for successful selection.\n\n\\subsection{Mechanism 2: Logprob Score Compression}\n\nLP---the only per-sample signal (others are instance-level aggregates)---fails due to extreme score compression: median within-instance LP range is 0.041 nats across SciERC instances.\n\n\\paragraph{Free-Form Ablation.} To test whether compression is an artifact of constrained JSON decoding, we compare LP distributions with and without format constraints:\n\n\\begin{itemize}\n\\item Constrained LP std: 0.0206\n\\item Free-form LP std: 0.0199 (ratio 0.97)\n\\item Tied fraction: 59.7\\% $\\rightarrow$ 57.7\\% ($-$2.0pp, negligible)\n\\item NER selection: +0.59pp $\\rightarrow$ +0.18pp (both negligible)\n\\item Parse rate: 99.95\\% (format retained without grammar)\n\\end{itemize}\n\nThe near-unity std ratio (0.97) confirms compression is \\emph{intrinsic} to the model/task combination, not an artifact of decoding constraints. Fine-tuned models produce similarly compressed logprob distributions regardless of output format.\n\n\\subsection{Scale Ablation}\n\nTo rule out model capacity as confound, we replicate on Qwen3-4B ($N = 8$, $T = 1.0$):\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nDataset & Metric & 4B & 8B \\\\\n\\midrule\n\\multirow{3}{*}{CoNLL} & Greedy $F_1$ & 0.923 & 0.912 \\\\\n& SJ $\\rho$ & 0.422 & 0.436 \\\\\n& Best sel.\\ $\\Delta$ & +0.09pp & +0.2pp \\\\\n\\midrule\n\\multirow{4}{*}{SciERC NER} & Greedy $F_1$ & 0.662 & 0.644 \\\\\n& SJ $\\rho$ & 0.422 & 0.383 \\\\\n& Best sel.\\ $\\Delta$ & $-$1.49pp & +0.6pp \\\\\n& Oracle $\\Delta$ & +13.0pp & +13.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Scale ablation. QE correlations maintained or improved at 4B (SJ $\\rho$: 0.383$\\rightarrow$0.422 on SciERC). Selection fails at both scales despite 13pp oracle headroom. On SciERC 4B, all signals perform \\emph{worse} than greedy.}\n\\label{tab:scale}\n\\end{table}\n\nAt 4B, SciERC NER shows a dramatic correlation--selection gap: SJ $\\rho = 0.422$ (strong QE) yet SJ selection $= -1.49$pp (worse than greedy). The oracle headroom (13.0pp) confirms the information exists in the candidate set---signals simply cannot access it at either scale.\n\n\\section{Discussion}\n\n\\subsection{The Correlation--Selection Gap as a General Phenomenon}\n\nOur findings extend beyond structured IE. The gap arises whenever:\n\\begin{enumerate}\n\\item A model is capable enough that most instances produce near-optimal outputs (high degeneracy);\n\\item Quality signals operate on output statistics rather than input--output interaction;\n\\item The candidate set contains the information (oracle headroom exists) but unsupervised signals cannot rank within the narrow quality band.\n\\end{enumerate}\n\nThis pattern connects to known phenomena:\n\\begin{itemize}\n\\item \\textbf{Reward hacking} in RLHF: reward models correlate with quality at the population level but fail to improve individual outputs beyond a capability threshold.\n\\item \\textbf{Mode collapse}: high-capability models converge to similar outputs, reducing the diversity that selection exploits.\n\\item \\textbf{Diminishing returns of best-of-N}: documented empirically for reasoning tasks as $N$ increases, but not previously explained mechanistically.\n\\end{itemize}\n\n\\subsection{When Would Consistency-Based Selection Succeed?}\n\nOur analysis predicts selection success requires: (a) sufficient output diversity (low degeneracy, $< 10\\%$), (b) meaningful quality variation within instances, and (c) signals that capture this variation. Concretely, consistency should outperform logprob when model calibration is poor (e.g., in-context learning without fine-tuning), when logprobs are unavailable (closed-source APIs), or in ensemble settings where agreement across heterogeneous models carries signal.\n\n\\subsection{Implications for TTS Evaluation}\n\nWe advocate that TTS evaluations must separately report QE metrics (population-level $\\rho$, AUROC) and selection metrics (instance-level $\\Delta F_1$ with significance tests). Claims of ``strong correlation'' must not be interpreted as ``effective selection.'' The 13pp oracle gap we document---information that exists but cannot be accessed by unsupervised signals---motivates trained verifiers with access to input representations as the path forward.\n\n\\subsection{Limitations}\n\nOur study has several limitations: (1) All models are decoder-only 4--8B parameters; encoder models and 70B+ scales remain untested. (2) Two NER datasets and one RE dataset limit domain generalization claims. (3) The supervised verifier uses only output statistics; a verifier with access to hidden states might close more of the oracle gap. (4) We study $N \\leq 16$; larger sample budgets may enable different selection strategies.\n\n\\section{Conclusion}\n\nWe demonstrate a fundamental \\emph{correlation--selection gap} in test-time scaling for structured information extraction: confidence signals that reliably predict output quality at the population level ($\\rho$ up to 0.45, AUROC up to 0.75) uniformly fail to select better candidates at the instance level ($\\Delta < 0.3$pp, all $p > 0.05$) despite 13--18pp oracle headroom. Through controlled ablations---free-form decoding, LoRA rank variation, scale comparison, and supervised combination---we establish this gap as multi-causal and intrinsic rather than artifactual. A supervised verifier closing only 3.2\\% of the oracle gap confirms the deficit is fundamental to these signal families.\n\nWe argue this gap is not IE-specific but a general consequence of model capability: as systems improve, output convergence eliminates the variation that unsupervised selection requires. TTS evaluations must decouple quality estimation from selection claims, and future work should focus on trained verifiers with input--output interaction rather than output-only statistics.\n\n\\bibliography{custom}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\\section{Numerical Consistency Notes}\n\nAll quantitative claims reference the following source experiments: SciERC results from exp\\_016\\_rerun\\_1024 (Qwen3-8B, $N=8$, $T=1.0$, max\\_tokens=1024). CoNLL results from LLaMA-3.1-8B ($N=8$, $T=1.0$). Scale ablation from Qwen3-4B ($N=8$, $T=1.0$). Greedy $F_1$ for SciERC NER is 0.644 (512-token pipeline filtered).\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc82ba68-4a5d-4844-96e9-79bd5ebf0143",
  "isSidechain": false,
  "requestId": "req_011Cb6CXvEuXipFck6mdebKq",
  "type": "assistant",
  "uuid": "6cb384f5-37c3-4520-aac6-9e81324c6fdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMVMT1Qm6tmMbzhpFjmbQK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 38037,
      "output_tokens": 7295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1059,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7295,
          "cache_read_input_tokens": 38037,
          "cache_creation_input_tokens": 1059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1059
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

_source line 21 · 2026-05-16T11:54:13.973Z_

<details><summary>↩ Tool result · `toolu_01K3UdTPEPdPLoHJzJbrNQv2`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cb384f5-37c3-4520-aac6-9e81324c6fdb",
  "isSidechain": false,
  "promptId": "213d3fd3-ae42-4274-a194-17aa7930521a",
  "type": "user",
  "uuid": "d720b14a-68ca-4198-a243-8e511e70c5e3",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\n\\title{Not All Correlations Transfer: When Population-Level Quality Signals\\\\Fail at Instance-Level Selection}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nTest-time scaling (TTS) via multi-sample generation assumes that confidence signals which correlate with output quality at the population level can also select better candidates at the instance level. We demonstrate that this assumption fails for structured information extraction. Across three datasets (SciERC, CoNLL-2003, WNUT-17), three models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B), and five confidence signal families, we find a consistent \\emph{correlation--selection gap}: signals achieve moderate quality estimation performance (Spearman $\\rho$ up to 0.45, AUROC up to 0.75) yet fail to select outputs that improve over greedy decoding ($\\Delta < 0.3$pp, all $p > 0.05$) despite 13pp oracle headroom. We identify two causal mechanisms---instance degeneracy (21--58\\% of instances yield identical quality across samples) and logprob score compression (within-instance range 0.041 nats)---and show via controlled ablations that neither is an artifact of decoding constraints or model capacity. A supervised verifier combining all five signals closes only 3.2\\% of the oracle gap, confirming that the information deficit is fundamental. We argue this gap is an inevitable consequence of high model capability and constitutes a general warning for TTS scaling beyond discrete-answer tasks.\n\\end{abstract}\n\n\\section{Introduction}\n\nTest-time scaling (TTS) has emerged as a powerful paradigm for improving language model outputs: generate multiple candidates, then select the best one using a quality signal. This approach yields consistent gains for mathematical reasoning \\cite{wang2023selfconsistency}, code generation \\cite{chen2021codex}, and machine translation \\cite{eikema2022sampling}. The implicit promise is general---if a signal correlates with quality, it should enable selection.\n\nWe show this promise is fundamentally overfit to discrete-answer tasks. For structured information extraction (IE)---where outputs are entity sets or relation triples rather than single tokens---the correlation between confidence signals and output quality does \\emph{not} transfer from population-level estimation to instance-level selection.\n\nThis finding matters beyond IE. Any task where a capable model produces near-deterministic outputs will exhibit the same phenomenon: quality signals that work for estimation become useless for selection because there is nothing meaningfully different to select \\emph{from}. We term this the \\textbf{correlation--selection gap} and argue it represents a structural limitation of unsupervised TTS scaling for high-performance systems.\n\nOur contribution is methodological: we formalize the distinction between quality estimation (QE) and candidate selection, demonstrate that conflating them leads to incorrect conclusions about TTS effectiveness, and provide controlled experimental evidence for the causal mechanisms. Specifically:\n\n\\begin{enumerate}\n\\item We show that five confidence signals across four families achieve moderate QE performance ($\\rho$ up to 0.45, AUROC up to 0.75) but uniformly fail at selection ($\\Delta < 0.3$pp vs.\\ greedy, all $p > 0.05$).\n\\item We identify two mechanisms: \\emph{instance degeneracy} (model capability $\\rightarrow$ output convergence $\\rightarrow$ vanishing headroom) and \\emph{logprob compression} (within-instance score range too narrow for discrimination).\n\\item We demonstrate via LoRA rank ablation that reducing degeneracy is necessary but not sufficient---signals still cannot exploit increased headroom---establishing the gap as multi-causal.\n\\item A supervised verifier baseline closing only 3.2\\% of oracle gap confirms the information deficit is not merely a threshold problem but a fundamental limitation of these signal families.\n\\end{enumerate}\n\nThe correlation--selection gap connects to broader phenomena in machine learning: reward hacking in RLHF (where reward signals correlate with quality at the population level but fail to improve individual outputs), mode collapse in generative models, and the diminishing returns of best-of-N sampling as model capability increases. Our work provides the first controlled experimental documentation of this gap in a structured prediction setting.\n\n\\section{Related Work}\n\n\\paragraph{Test-Time Scaling.} Self-consistency \\cite{wang2023selfconsistency} demonstrates that majority voting over chain-of-thought samples improves reasoning accuracy. Recent extensions include CISC \\cite{cisc2025} (confidence-weighted voting), Self-Certainty Best-of-N \\cite{selfcertainty2026} (KL-divergence selection), and ReASC \\cite{reasc2026} (reliability-aware adaptive sampling). All target discrete-answer tasks where selection is well-defined. Snell et al.\\ (\\citeyear{snell2024scaling}) and Brown et al.\\ (\\citeyear{brown2024tts}) formalize TTS scaling laws but assume monotone selection improvement with sample count---an assumption we show fails for structured outputs.\n\n\\paragraph{Confidence and Uncertainty Estimation.} Semantic entropy \\cite{kuhn2023semantic}, calibration methods \\cite{kadavath2022language,guo2017calibration}, and LLM confidence surveys \\cite{uqsurvey2025,confsurvey2024} focus on population-level quality estimation. SelfCheckGPT \\cite{manakul2023selfcheckgpt} uses consistency for hallucination detection (a QE task). CoCoA \\cite{cocoa2025} combines confidence and consistency for uncertainty quantification in QA/summarization. None distinguish QE from selection or test whether population-level correlations transfer to instance-level ranking.\n\n\\paragraph{Structured IE Confidence.} Culotta \\& McCallum (\\citeyear{culotta2004confidence}) study confidence for CRF-based extraction. N\\'{e}dellec \\& Xia (\\citeyear{nedellec2026}) examine consistency--accuracy correlations for hard-prompted LLMs on entity/relation extraction, finding moderate correlations with surface-level string matching. Their work does not study best-of-N selection or multiple signal families, and their surface matching limitation (acknowledged as missing semantically consistent outputs) motivates our structural Jaccard metric.\n\n\\paragraph{MBR Decoding.} Eikema et al.\\ (\\citeyear{eikema2022sampling}) document MBR failure modes in MT. Their mechanism (utility function misalignment) differs from ours: in our setting, the utility \\emph{is} aligned at the instance level ($\\rho = 0.52$ within instances) but headroom is eliminated by output convergence.\n\n\\paragraph{Verifiers and Reward Models.} Cobbe et al.\\ (\\citeyear{cobbe2021training}) and Lightman et al.\\ (\\citeyear{lightman2023lets}) train verifiers for mathematical reasoning. Our supervised baseline tests whether a simple verifier on unsupervised signals can close the gap, finding it cannot---suggesting the gap requires access to input representations, not just output statistics.\n\n\\section{Method}\n\n\\subsection{Problem Formulation}\n\nGiven a structured IE task with input $x$ and a language model $M$, we generate $N$ candidate outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$. We define two distinct objectives:\n\n\\textbf{Quality Estimation (QE):} Assign a score $s(y_i)$ such that $\\text{rank}(s(y_i))$ correlates with $\\text{rank}(F_1(y_i, y^*))$ across the test population.\n\n\\textbf{Candidate Selection:} Choose $\\hat{y} = \\arg\\max_i s(y_i)$ such that $F_1(\\hat{y}, y^*) > F_1(y_{\\text{greedy}}, y^*)$.\n\nThese objectives are related but not equivalent. QE requires only \\emph{population-level} rank correlation; selection requires \\emph{instance-level} discrimination among near-identical candidates. We argue that conflating them has led to overoptimistic conclusions about TTS for structured tasks.\n\n\\subsection{Confidence Signals}\n\nWe evaluate five signals spanning four families:\n\n\\paragraph{Structural Consistency.} \\textbf{Structural Jaccard (SJ):} Mean pairwise Jaccard similarity over predicted entity/relation sets using type-grouped Hungarian matching. \\textbf{Fuzzy-match Kendall (FK):} Kendall correlation over soft entity alignments.\n\n\\paragraph{Probabilistic.} \\textbf{Log-probability (LP):} Mean token-level log-probability of the generation.\n\n\\paragraph{Voting-based.} \\textbf{Voting Confidence (VC):} Entity-level frequency across $N$ samples.\n\n\\paragraph{Agreement-based.} \\textbf{Exact Match (EM):} Fraction of $N$ samples producing identical output.\n\n\\subsection{Datasets and Models}\n\n\\textbf{Datasets:} SciERC \\cite{luan2018scierc} (NER + RE), CoNLL-2003 \\cite{sang2003conll} (NER), WNUT-17 (NER, OOD setting).\n\n\\textbf{Models:} Qwen3-8B (primary), Qwen3-4B (scale ablation), LLaMA-3.1-8B (cross-architecture validation). All fine-tuned with LoRA (rank 32 default, rank 8 for ablation) on task-specific training splits.\n\n\\textbf{Generation:} $N = 8$ samples at $T = 1.0$ (default), with $N = 16$ for scaling analysis. Greedy decoding ($T = 0$) as selection baseline.\n\n\\subsection{Evaluation Protocol}\n\n\\textbf{QE metrics:} Spearman $\\rho$ (full population and conditional on non-degenerate instances), AUROC (binary: above/below median $F_1$), ECE.\n\n\\textbf{Selection metrics:} Best-of-N $F_1$ for each signal vs.\\ greedy $F_1$. Statistical significance via 1000-iteration bootstrap with permutation $p$-values.\n\n\\textbf{Oracle:} $\\max_i F_1(y_i, y^*)$ --- the best achievable selection from the candidate set.\n\n\\section{Experiments}\n\n\\subsection{Quality Estimation Results}\n\nTable~\\ref{tab:qe_main} shows QE performance on SciERC (primary evaluation set, $N = 8$, $T = 1.0$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\rho$ (NER) & AUROC (NER) & $\\rho$ (RE) & AUROC (RE) \\\\\n\\midrule\nVC & 0.379 & 0.684 & --- & 0.694 \\\\\nSJ & 0.360 & 0.692 & 0.265 & 0.670 \\\\\nEM & 0.295 & 0.749 & --- & 0.706 \\\\\nFK & 0.267 & 0.629 & 0.254 & 0.609 \\\\\nLP & 0.205 & 0.578 & 0.302 & 0.601 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Quality estimation on SciERC ($n=529$ NER, $n=397$ RE). All $\\rho$ values $p < 0.001$. Structural signals dominate for NER; LP dominates for RE---signal ranking is task-dependent.}\n\\label{tab:qe_main}\n\\end{table}\n\nAll signals achieve statistically significant QE correlations. EM achieves the highest AUROC (0.749 NER, 0.706 RE) while VC achieves the highest $\\rho$ for NER (0.379). Notably, signal ranking reverses between tasks: structural signals (SJ, FK) dominate NER while LP dominates RE, explained by the 43--45\\% zero-$F_1$ rate in RE creating binary-dominated distributions where generation confidence outperforms structural overlap.\n\n\\subsection{Selection Results: The Correlation--Selection Gap}\n\nDespite moderate QE performance, no signal achieves statistically significant selection improvement over greedy decoding (Table~\\ref{tab:selection}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & NER $F_1$ & $\\Delta$ & RE $F_1$ & $\\Delta$ \\\\\n\\midrule\nGreedy ($T=0$) & 0.644 & --- & 0.404 & --- \\\\\n\\midrule\nLP (best-of-8) & 0.650 & +0.6 & 0.395 & $-$0.9 \\\\\nSJ (best-of-8) & 0.645 & +0.1 & 0.386 & $-$1.9 \\\\\nEM (best-of-8) & 0.645 & +0.1 & 0.386 & $-$1.9 \\\\\nVC (best-of-8) & 0.634 & $-$1.0 & 0.359 & $-$4.5 \\\\\nRandom & 0.608 & $-$3.6 & 0.354 & $-$5.0 \\\\\n\\midrule\nOracle & 0.776 & +13.2 & 0.585 & +18.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selection results on SciERC ($N=8$, $T=1.0$). $\\Delta$ in percentage points vs.\\ greedy. NER LP: bootstrap $p = 0.39$, 95\\% CI $[-3.0, +4.2]$pp, Cohen's $d = 0.038$. Oracle headroom is 13--18pp but no signal captures more than 0.6pp.}\n\\label{tab:selection}\n\\end{table}\n\nThe gap is stark: 13.2pp oracle headroom exists for NER, yet the best signal (LP) captures only 0.6pp---0.5\\% of available headroom, not statistically significant ($p = 0.39$). For RE, all signals perform \\emph{worse} than greedy. This is not a statistical power issue: the 95\\% CI for the best signal excludes gains beyond 4.2pp, while 13pp is available.\n\n\\subsection{Cross-Model Validation}\n\nTo test whether the gap is model-specific, we evaluate LLaMA-3.1-8B on CoNLL-2003 (Table~\\ref{tab:llama_conll}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\rho$ & AUROC & Sel.\\ $F_1$ & $\\Delta$ vs Greedy \\\\\n\\midrule\nSJ & 0.43 & 0.70 & 0.925 & +0.1pp \\\\\nFK & 0.42 & 0.70 & 0.924 & 0.0pp \\\\\nEM & 0.43 & 0.71 & 0.924 & 0.0pp \\\\\nLP & 0.31 & 0.76 & 0.925 & +0.1pp \\\\\nVC & 0.43 & 0.71 & 0.926 & +0.2pp \\\\\n\\midrule\nOracle & --- & --- & 0.945 & +2.1pp \\\\\nGreedy & --- & --- & 0.924 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LLaMA-3.1-8B on CoNLL-2003 ($N=8$, $T=1.0$). QE correlations ($\\rho = 0.31$--$0.43$) match Qwen3-8B ($\\rho = 0.44$), confirming model-agnostic QE. Selection gains $\\leq 0.2$pp with 2.1pp oracle headroom. Instance degeneracy: 56\\%.}\n\\label{tab:llama_conll}\n\\end{table}\n\nLLaMA-3.1-8B replicates the pattern: moderate QE correlations ($\\rho$ up to 0.43, AUROC up to 0.76) with negligible selection gains ($\\leq 0.2$pp). The high degeneracy rate (56\\%) on CoNLL---where greedy $F_1 = 0.924$---exemplifies the capability--degeneracy mechanism: high model capability compresses the candidate space.\n\n\\subsection{Supervised Verifier Baseline}\n\nIf unsupervised signals fail individually, can their combination succeed? We train a logistic regression verifier on all five signals with 5-fold cross-validation on SciERC (Table~\\ref{tab:verifier}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Sel.\\ $F_1$ & $\\Delta$ & AUROC & Gap Closed \\\\\n\\midrule\nGreedy & 0.644 & --- & --- & 0\\% \\\\\nBest single (EM) & 0.650 & +0.6pp & 0.749 & 4.6\\% \\\\\nLR Verifier (5-sig) & 0.648 & +0.4pp & 0.760 & 3.2\\% \\\\\nOracle & 0.776 & +13.2pp & --- & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Supervised verifier (logistic regression on 5 signals, 5-fold CV, SciERC NER). The verifier achieves marginally higher AUROC (0.760 vs 0.749) but \\emph{lower} selection $F_1$ than the best single signal, closing only 3.2\\% of oracle gap.}\n\\label{tab:verifier}\n\\end{table}\n\nThe supervised verifier closes 3.2\\% of the oracle gap---\\emph{less} than the best single signal (EM, 4.6\\%). Feature importance analysis reveals high inter-signal correlation (mean pairwise $\\rho = 0.45$--$0.72$), explaining why linear combination provides no advantage. The signals collectively contain negligible selection-relevant information beyond what any individual signal provides.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nFeature & LR Coeff. & Mean $\\rho$ w/ others \\\\\n\\midrule\nEM & 0.42 & 0.61 \\\\\nVC & 0.31 & 0.72 \\\\\nSJ & 0.18 & 0.68 \\\\\nLP & 0.06 & 0.45 \\\\\nFK & 0.03 & 0.59 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature importance and inter-signal correlation. High pairwise correlations explain why the ensemble cannot outperform the best single signal.}\n\\label{tab:feature_importance}\n\\end{table}\n\n\\subsection{Mechanism 1: Instance Degeneracy}\n\nWe define \\emph{instance degeneracy} as the fraction of test instances where all $N$ samples produce identical $F_1$ scores (within rounding). Across configurations:\n\n\\begin{itemize}\n\\item CoNLL-2003 (greedy $F_1 = 0.924$): 56--58\\% degeneracy\n\\item SciERC (greedy $F_1 = 0.644$): 21\\% degeneracy\n\\item WNUT-17 (greedy $F_1 \\approx 0.48$): $\\sim$0\\% degeneracy\n\\end{itemize}\n\nThe monotone relationship between model capability and degeneracy connects to mode collapse: as models improve, their outputs converge, eliminating the variation that selection requires. This is not a bug but a \\emph{structural consequence of capability}.\n\n\\paragraph{LoRA Rank Ablation.} To test whether degeneracy is an artifact of over-fitting (high LoRA rank), we compare rank 8 vs.\\ rank 32 on SciERC:\n\n\\begin{itemize}\n\\item Degeneracy: 7.2\\% (rank 8) vs.\\ 21\\% (rank 32) --- 3$\\times$ reduction\n\\item Oracle headroom: 16.0pp (rank 8) vs.\\ 13.3pp (rank 32)\n\\item Selection: LP $-$0.5pp, SJ $-$0.9pp vs.\\ greedy (rank 8)\n\\item QE preserved: VC $\\rho = 0.394$, SJ $\\rho = 0.365$ (rank 8)\n\\end{itemize}\n\nReducing degeneracy increases oracle headroom but signals \\emph{still} cannot exploit it. This establishes the multi-causal nature of the gap: low degeneracy is necessary but not sufficient for successful selection.\n\n\\subsection{Mechanism 2: Logprob Score Compression}\n\nLP---the only per-sample signal (others are instance-level aggregates)---fails due to extreme score compression: median within-instance LP range is 0.041 nats across SciERC instances.\n\n\\paragraph{Free-Form Ablation.} To test whether compression is an artifact of constrained JSON decoding, we compare LP distributions with and without format constraints:\n\n\\begin{itemize}\n\\item Constrained LP std: 0.0206\n\\item Free-form LP std: 0.0199 (ratio 0.97)\n\\item Tied fraction: 59.7\\% $\\rightarrow$ 57.7\\% ($-$2.0pp, negligible)\n\\item NER selection: +0.59pp $\\rightarrow$ +0.18pp (both negligible)\n\\item Parse rate: 99.95\\% (format retained without grammar)\n\\end{itemize}\n\nThe near-unity std ratio (0.97) confirms compression is \\emph{intrinsic} to the model/task combination, not an artifact of decoding constraints. Fine-tuned models produce similarly compressed logprob distributions regardless of output format.\n\n\\subsection{Scale Ablation}\n\nTo rule out model capacity as confound, we replicate on Qwen3-4B ($N = 8$, $T = 1.0$):\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nDataset & Metric & 4B & 8B \\\\\n\\midrule\n\\multirow{3}{*}{CoNLL} & Greedy $F_1$ & 0.923 & 0.912 \\\\\n& SJ $\\rho$ & 0.422 & 0.436 \\\\\n& Best sel.\\ $\\Delta$ & +0.09pp & +0.2pp \\\\\n\\midrule\n\\multirow{4}{*}{SciERC NER} & Greedy $F_1$ & 0.662 & 0.644 \\\\\n& SJ $\\rho$ & 0.422 & 0.383 \\\\\n& Best sel.\\ $\\Delta$ & $-$1.49pp & +0.6pp \\\\\n& Oracle $\\Delta$ & +13.0pp & +13.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Scale ablation. QE correlations maintained or improved at 4B (SJ $\\rho$: 0.383$\\rightarrow$0.422 on SciERC). Selection fails at both scales despite 13pp oracle headroom. On SciERC 4B, all signals perform \\emph{worse} than greedy.}\n\\label{tab:scale}\n\\end{table}\n\nAt 4B, SciERC NER shows a dramatic correlation--selection gap: SJ $\\rho = 0.422$ (strong QE) yet SJ selection $= -1.49$pp (worse than greedy). The oracle headroom (13.0pp) confirms the information exists in the candidate set---signals simply cannot access it at either scale.\n\n\\section{Discussion}\n\n\\subsection{The Correlation--Selection Gap as a General Phenomenon}\n\nOur findings extend beyond structured IE. The gap arises whenever:\n\\begin{enumerate}\n\\item A model is capable enough that most instances produce near-optimal outputs (high degeneracy);\n\\item Quality signals operate on output statistics rather than input--output interaction;\n\\item The candidate set contains the information (oracle headroom exists) but unsupervised signals cannot rank within the narrow quality band.\n\\end{enumerate}\n\nThis pattern connects to known phenomena:\n\\begin{itemize}\n\\item \\textbf{Reward hacking} in RLHF: reward models correlate with quality at the population level but fail to improve individual outputs beyond a capability threshold.\n\\item \\textbf{Mode collapse}: high-capability models converge to similar outputs, reducing the diversity that selection exploits.\n\\item \\textbf{Diminishing returns of best-of-N}: documented empirically for reasoning tasks as $N$ increases, but not previously explained mechanistically.\n\\end{itemize}\n\n\\subsection{When Would Consistency-Based Selection Succeed?}\n\nOur analysis predicts selection success requires: (a) sufficient output diversity (low degeneracy, $< 10\\%$), (b) meaningful quality variation within instances, and (c) signals that capture this variation. Concretely, consistency should outperform logprob when model calibration is poor (e.g., in-context learning without fine-tuning), when logprobs are unavailable (closed-source APIs), or in ensemble settings where agreement across heterogeneous models carries signal.\n\n\\subsection{Implications for TTS Evaluation}\n\nWe advocate that TTS evaluations must separately report QE metrics (population-level $\\rho$, AUROC) and selection metrics (instance-level $\\Delta F_1$ with significance tests). Claims of ``strong correlation'' must not be interpreted as ``effective selection.'' The 13pp oracle gap we document---information that exists but cannot be accessed by unsupervised signals---motivates trained verifiers with access to input representations as the path forward.\n\n\\subsection{Limitations}\n\nOur study has several limitations: (1) All models are decoder-only 4--8B parameters; encoder models and 70B+ scales remain untested. (2) Two NER datasets and one RE dataset limit domain generalization claims. (3) The supervised verifier uses only output statistics; a verifier with access to hidden states might close more of the oracle gap. (4) We study $N \\leq 16$; larger sample budgets may enable different selection strategies.\n\n\\section{Conclusion}\n\nWe demonstrate a fundamental \\emph{correlation--selection gap} in test-time scaling for structured information extraction: confidence signals that reliably predict output quality at the population level ($\\rho$ up to 0.45, AUROC up to 0.75) uniformly fail to select better candidates at the instance level ($\\Delta < 0.3$pp, all $p > 0.05$) despite 13--18pp oracle headroom. Through controlled ablations---free-form decoding, LoRA rank variation, scale comparison, and supervised combination---we establish this gap as multi-causal and intrinsic rather than artifactual. A supervised verifier closing only 3.2\\% of the oracle gap confirms the deficit is fundamental to these signal families.\n\nWe argue this gap is not IE-specific but a general consequence of model capability: as systems improve, output convergence eliminates the variation that unsupervised selection requires. TTS evaluations must decouple quality estimation from selection claims, and future work should focus on trained verifiers with input--output interaction rather than output-only statistics.\n\n\\bibliography{custom}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\\section{Numerical Consistency Notes}\n\nAll quantitative claims reference the following source experiments: SciERC results from exp\\_016\\_rerun\\_1024 (Qwen3-8B, $N=8$, $T=1.0$, max\\_tokens=1024). CoNLL results from LLaMA-3.1-8B ($N=8$, $T=1.0$). Scale ablation from Qwen3-4B ($N=8$, $T=1.0$). Greedy $F_1$ for SciERC NER is 0.644 (512-token pipeline filtered).\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "6cb384f5-37c3-4520-aac6-9e81324c6fdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T113255 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consi…",
  "leafUuid": "d720b14a-68ca-4198-a243-8e511e70c5e3",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1"
}
```

---

### Assistant

_source line 24 · 2026-05-16T11:54:17.959Z_

Now let me compile it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d720b14a-68ca-4198-a243-8e511e70c5e3",
  "isSidechain": false,
  "requestId": "req_011Cb6Cij32D8ASiFtSBCeZZ",
  "type": "assistant",
  "uuid": "4839ce58-facf-46d4-b536-375c68c34015",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJ3wWBenvd5BwzoPNMDnrK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7362,
      "cache_read_input_tokens": 39096,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 39096,
          "cache_creation_input_tokens": 7362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7362
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

_source line 25 · 2026-05-16T11:54:18.978Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JWnyXzBoeqtTovFUJwX7F7`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4839ce58-facf-46d4-b536-375c68c34015",
  "isSidechain": false,
  "requestId": "req_011Cb6Cij32D8ASiFtSBCeZZ",
  "type": "assistant",
  "uuid": "10cde0ac-e83e-45e2-86a7-a36f95718a3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJ3wWBenvd5BwzoPNMDnrK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7362,
      "cache_read_input_tokens": 39096,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 39096,
          "cache_creation_input_tokens": 7362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7362
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

_source line 26 · 2026-05-16T11:54:19.203Z_

<details><summary>↩ Tool result · `toolu_01JWnyXzBoeqtTovFUJwX7F7`</summary>

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

! LaTeX Error: File `acl.sty' not found.

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
  "parentUuid": "10cde0ac-e83e-45e2-86a7-a36f95718a3f",
  "isSidechain": false,
  "promptId": "213d3fd3-ae42-4274-a194-17aa7930521a",
  "type": "user",
  "uuid": "8cb43913-5b4f-4159-b8bd-df832d55c4c4",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "10cde0ac-e83e-45e2-86a7-a36f95718a3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-16T11:54:23.229Z_

<details><summary>Logged reasoning block</summary>

```text
Need to find or substitute the ACL style file. Let me check what's available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cb43913-5b4f-4159-b8bd-df832d55c4c4",
  "isSidechain": false,
  "requestId": "req_011Cb6Cj7E1hrJzxc56f3CNb",
  "type": "assistant",
  "uuid": "28f217c1-aaa4-4b6c-8476-45895f9e5945",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFjMrDRwrknmuWExeK54nv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 432,
      "cache_read_input_tokens": 46458,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 46458,
          "cache_creation_input_tokens": 432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 432
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

_source line 28 · 2026-05-16T11:54:23.721Z_

ACL style not available. Let me switch to a standard format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28f217c1-aaa4-4b6c-8476-45895f9e5945",
  "isSidechain": false,
  "requestId": "req_011Cb6Cj7E1hrJzxc56f3CNb",
  "type": "assistant",
  "uuid": "90f98567-58b0-4c06-8fdf-41ba01f893d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFjMrDRwrknmuWExeK54nv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 432,
      "cache_read_input_tokens": 46458,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 46458,
          "cache_creation_input_tokens": 432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 432
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

_source line 29 · 2026-05-16T11:54:25.211Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MLT54MHKdU41SrFu7g29ZY`</summary>

```json
{
  "command": "ls /usr/share/texlive/texmf-dist/tex/latex/ | grep -iE \"acl|emnlp|naa\" 2>/dev/null; find /home/ubuntu -name \"acl*.sty\" -o -name \"emnlp*.sty\" 2>/dev/null | head -5",
  "description": "Search for ACL/EMNLP style files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90f98567-58b0-4c06-8fdf-41ba01f893d9",
  "isSidechain": false,
  "requestId": "req_011Cb6Cj7E1hrJzxc56f3CNb",
  "type": "assistant",
  "uuid": "c66329b9-661d-4de6-b82a-74a76ce6ffb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFjMrDRwrknmuWExeK54nv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 432,
      "cache_read_input_tokens": 46458,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 46458,
          "cache_creation_input_tokens": 432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 432
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

_source line 30 · 2026-05-16T11:54:25.569Z_

<details><summary>↩ Tool result · `toolu_01MLT54MHKdU41SrFu7g29ZY`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/worst/acl.sty
/home/ubuntu/agent-ml-research/templates/latex/acl/acl.sty
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c66329b9-661d-4de6-b82a-74a76ce6ffb8",
  "isSidechain": false,
  "promptId": "213d3fd3-ae42-4274-a194-17aa7930521a",
  "type": "user",
  "uuid": "24371327-f91d-4370-abb2-eac0c7821e1a",
  "toolUseResult": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl.sty\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/acl.sty\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/worst/acl.sty\n/home/ubuntu/agent-ml-research/templates/latex/acl/acl.sty",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c66329b9-661d-4de6-b82a-74a76ce6ffb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T11:54:28.659Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TyzeynyVq2EfB55zchyH3v`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl.sty /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/acl.sty",
  "description": "Copy ACL style file to target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24371327-f91d-4370-abb2-eac0c7821e1a",
  "isSidechain": false,
  "requestId": "req_011Cb6CjaP9gV7E9PKQ7b1uX",
  "type": "assistant",
  "uuid": "d6923718-5ff3-459f-a6b9-10c677b3490b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BsSvDzoUQA7cHzTAvgGLYa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 388,
      "cache_read_input_tokens": 46890,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 46890,
          "cache_creation_input_tokens": 388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 388
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

_source line 32 · 2026-05-16T11:54:28.736Z_

<details><summary>↩ Tool result · `toolu_01TyzeynyVq2EfB55zchyH3v`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6923718-5ff3-459f-a6b9-10c677b3490b",
  "isSidechain": false,
  "promptId": "213d3fd3-ae42-4274-a194-17aa7930521a",
  "type": "user",
  "uuid": "b2f7fdf5-8e43-4f84-9718-ac8f4236cac7",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "d6923718-5ff3-459f-a6b9-10c677b3490b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-16T11:54:28.742Z_

```json
{
  "parentUuid": "b2f7fdf5-8e43-4f84-9718-ac8f4236cac7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4c03a1cb-ce34-4647-ad98-64e9f2f5443e",
  "timestamp": "2026-05-16T11:54:28.742Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 34 · 2026-05-16T11:54:31.931Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019whynREmGyDmzYnhdBm6rT`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass with ACL style"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c03a1cb-ce34-4647-ad98-64e9f2f5443e",
  "isSidechain": false,
  "requestId": "req_011Cb6CjoxDoCA4misr1uBh5",
  "type": "assistant",
  "uuid": "cc8c2cc2-507c-47c6-8340-591cd3cca13e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYyaxurcrJE4oJHnNqoaFH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 289,
      "cache_read_input_tokens": 47278,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 289,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 47278,
          "cache_creation_input_tokens": 289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 289
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

_source line 35 · 2026-05-16T11:54:32.647Z_

<details><summary>↩ Tool result · `toolu_019whynREmGyDmzYnhdBm6rT`</summary>

```text
[6] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr
i8a.pfb>
Output written on paper.pdf (6 pages, 172457 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc8c2cc2-507c-47c6-8340-591cd3cca13e",
  "isSidechain": false,
  "promptId": "213d3fd3-ae42-4274-a194-17aa7930521a",
  "type": "user",
  "uuid": "ef18a178-b256-4b34-a29b-5db6c60335b0",
  "toolUseResult": {
    "stdout": "[6] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr\ni8a.pfb>\nOutput written on paper.pdf (6 pages, 172457 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "cc8c2cc2-507c-47c6-8340-591cd3cca13e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-16T11:54:36.334Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0166Q6dnSehCD2VJexNBwHjD`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -10",
  "description": "Second pdflatex pass for cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef18a178-b256-4b34-a29b-5db6c60335b0",
  "isSidechain": false,
  "requestId": "req_011Cb6Ck6bbCQhLAiCCCBr8B",
  "type": "assistant",
  "uuid": "4d784efa-96f4-4550-ad50-796bdbba70c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSeyi6sdkmcQdn5NUZoyt5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 748,
      "cache_read_input_tokens": 47567,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 47567,
          "cache_creation_input_tokens": 748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 748
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

_source line 37 · 2026-05-16T11:54:37.086Z_

<details><summary>↩ Tool result · `toolu_0166Q6dnSehCD2VJexNBwHjD`</summary>

```text
cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr
i8a.pfb>
Output written on paper.pdf (6 pages, 174121 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d784efa-96f4-4550-ad50-796bdbba70c5",
  "isSidechain": false,
  "promptId": "213d3fd3-ae42-4274-a194-17aa7930521a",
  "type": "user",
  "uuid": "b6addcb2-f856-42b9-a5d8-848c6805f40a",
  "toolUseResult": {
    "stdout": "cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr\ni8a.pfb>\nOutput written on paper.pdf (6 pages, 174121 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4d784efa-96f4-4550-ad50-796bdbba70c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-16T11:54:47.138Z_

编译成功，6 页 PDF。

论文已写入 `worst/paper.tex` 并编译为 `worst/paper.pdf`（6页）。按 narrative guidance 重新定位为方法论警示型论文：

- **标题**：*Not All Correlations Transfer: When Population-Level Quality Signals Fail at Instance-Level Selection*
- **核心论点**：QE-selection decoupling 是 TTS scaling 的通用陷阱，非 IE 特有
- **覆盖全部 3 个实验数据**：LLaMA CoNLL 跨模型验证（Table 3）、监督 verifier baseline（Table 4-5）、claim audit 的数值修正已融入全文（AUROC 降至 0.75 而非 0.82）
- **两个因果机制**：instance degeneracy + logprob compression，加 LoRA rank=8 / free-form / scale ablation 作为控制实验
- **连接 reward hacking、mode collapse 文献**，将 degeneracy 框定为高性能系统的必然后果

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6addcb2-f856-42b9-a5d8-848c6805f40a",
  "isSidechain": false,
  "requestId": "req_011Cb6CkRg44B8qhby6JQMi1",
  "type": "assistant",
  "uuid": "40059f13-8cdf-4ff3-b523-1b6428e33081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cy16ibZRA3hwRQ2BSoASSz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 431,
      "cache_read_input_tokens": 48315,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 298,
          "cache_read_input_tokens": 48315,
          "cache_creation_input_tokens": 431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 431
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

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T113255 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consi…",
  "leafUuid": "40059f13-8cdf-4ff3-b523-1b6428e33081",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "bbd9fe72-6aeb-4e6a-8501-079fbb07a3e1"
}
```

---
