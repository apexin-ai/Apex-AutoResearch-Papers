# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/a7bb3824-6271-4640-950f-c2fc0148d5eb.jsonl`
- **Structured JSON:** [`98a959d9e089c6df5f2e.json`](../../sessions/98/98a959d9e089c6df5f2e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T17:26:04.136Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T17:26:04.136Z",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：KL categorically dominates. Headline: 'Output-distribution distillation makes compensation networks obsolete for SwiGLU sparsity.' 三线汇聚——理论（gradient coupling解释joint interaction）、 实验（KL-only vs BCE+comp gap 9+ PPL points）、实践（省256MB compensation weights + per-layer GEMV）。 所有planned实验均确认三条claims原样成立，无需调整framing。投EMNLP Efficient Methods。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T17:26:04.139Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T17:26:04.139Z",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb"
}
```

---

## Round 1

36 recorded events

### User

_source line 3 · 2026-05-15T17:26:04.162Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：KL categorically dominates. Headline: 'Output-distribution distillation makes compensation networks obsolete for SwiGLU sparsity.' 三线汇聚——理论（gradient coupling解释joint interaction）、 实验（KL-only vs BCE+comp gap 9+ PPL points）、实践（省256MB compensation weights + per-layer GEMV）。 所有planned实验均确认三条claims原样成立，无需调整framing。投EMNLP Efficient Methods。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4324b22a-92db-42ef-a974-2006388d7cce",
  "type": "user",
  "uuid": "1e92c719-575a-4781-acc5-4ba5a04d3cb3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T17:26:04.161Z_

```json
{
  "parentUuid": "1e92c719-575a-4781-acc5-4ba5a04d3cb3",
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
  "uuid": "dee29508-54b8-456f-bd4e-63046d3977aa",
  "timestamp": "2026-05-15T17:26:04.161Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T17:26:04.161Z_

```json
{
  "parentUuid": "dee29508-54b8-456f-bd4e-63046d3977aa",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f76ca7ba-4cb1-4832-9546-54f393117f14",
  "timestamp": "2026-05-15T17:26:04.161Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
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
  "aiTitle": "Generate distillation sparse SwiGLU research paper",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb"
}
```

---

### Assistant

_source line 7 · 2026-05-15T17:26:06.597Z_

Let me start by reading the input files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f76ca7ba-4cb1-4832-9546-54f393117f14",
  "isSidechain": false,
  "requestId": "req_011Cb4kDUS6i8qgN9Jzs3ieC",
  "type": "assistant",
  "uuid": "e0b8a3b1-db44-4705-96b0-d5b5e4e7bdc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PeJUX3e7uQhLzqcJtgB4cL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11188,
      "cache_read_input_tokens": 11841,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11188,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11188
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

_source line 8 · 2026-05-15T17:26:07.048Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YP6eeDzxAhHJyv4mGa5s5A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0b8a3b1-db44-4705-96b0-d5b5e4e7bdc7",
  "isSidechain": false,
  "requestId": "req_011Cb4kDUS6i8qgN9Jzs3ieC",
  "type": "assistant",
  "uuid": "c3d6e483-48d6-4f3c-8eb0-b72b58ceec95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PeJUX3e7uQhLzqcJtgB4cL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11188,
      "cache_read_input_tokens": 11841,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11188,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11188
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

_source line 9 · 2026-05-15T17:26:07.425Z_

<details><summary>↩ Tool result · `toolu_01YP6eeDzxAhHJyv4mGa5s5A`</summary>

```text
1	[
2	  {
3	    "name": "Four-Condition Ablation @ 50% Sparsity",
4	    "description": "KL-only扩展到5 seeds（新增s0, s1），BCE+comp 5 seeds，KL+comp 3 seeds。 已有数据：KL-only 3 seeds (s42/s123/s456)均~9.2 PPL；BCE-only 3 seeds均~28.2 PPL。\n",
5	    "results": {
6	      "kl_only_s42_ppl": 9.2142,
7	      "kl_only_s123_ppl": 9.2474,
8	      "kl_only_s456_ppl": 9.14,
9	      "kl_only_s0_ppl": 9.19,
10	      "kl_only_s1_ppl": 9.23,
11	      "kl_only_mean_ppl": 9.2,
12	      "kl_only_std_ppl": 0.04,
13	      "kl_only_model_sparsity": 0.498,
14	      "bce_comp_s42_ppl": 18.22,
15	      "bce_comp_s123_ppl": 18.91,
16	      "bce_comp_s456_ppl": 18.38,
17	      "bce_comp_s0_ppl": 18.65,
18	      "bce_comp_s1_ppl": 19.05,
19	      "bce_comp_mean_ppl": 18.64,
20	      "bce_comp_std_ppl": 0.33,
21	      "bce_comp_model_sparsity": 0.496,
22	      "kl_comp_s42_ppl": 9.05,
23	      "kl_comp_s123_ppl": 9.08,
24	      "kl_comp_s456_ppl": 8.92,
25	      "kl_comp_mean_ppl": 9.02,
26	      "kl_comp_std_ppl": 0.07,
27	      "bce_only_mean_ppl": 28.16,
28	      "bce_only_std_ppl": 0.17,
29	      "kl_only_vs_bce_comp_gap": 9.44,
30	      "kl_only_vs_dense_increase_pct": 50.3,
31	      "bce_comp_vs_dense_increase_pct": 204.6,
32	      "comp_benefit_for_bce_ppl": 9.52,
33	      "comp_benefit_for_kl_ppl": 0.18
34	    },
35	    "tables": [
36	      {
37	        "name": "Table 1: Four-Condition Ablation Results (WikiText-2 PPL, Llama 3.1 8B, 50% sparsity)",
38	        "columns": [
39	          "Condition",
40	          "Seeds",
41	          "PPL (mean±std)",
42	          "Δ vs Dense",
43	          "Comp Benefit"
44	        ],
45	        "rows": [
46	          [
47	            "Dense",
48	            "-",
49	            "6.12",
50	            "-",
51	            "-"
52	          ],
53	          [
54	            "BCE-only",
55	            3,
56	            "28.16±0.17",
57	            "+360%",
58	            "-"
59	          ],
60	          [
61	            "BCE+comp",
62	            5,
63	            "18.64±0.33",
64	            "+205%",
65	            "−9.52"
66	          ],
67	          [
68	            "KL-only",
69	            5,
70	            "9.20±0.04",
71	            "+50%",
72	            "-"
73	          ],
74	          [
75	            "KL+comp",
76	            3,
77	            "9.02±0.07",
78	            "+47%",
79	            "−0.18"
80	          ]
81	        ]
82	      }
83	    ],
84	    "figures": [],
85	    "analysis": "KL-only以9.20 PPL大幅碾压BCE+comp的18.64 PPL（gap 9.44 points），且compensation对KL仅贡献 0.18 PPL改善（vs对BCE贡献9.52），证明compensation网络对KL训练的predictor完全不必要。 5-seed std=0.04证明高度可复现。Headline claim直接成立：output-distribution distillation eliminates the need for compensation networks.\n\n\nKL的gradient dL_KL/ds_j通过d_logits/dh * dh/dm耦合所有active neurons，天然捕获joint interaction effects。因此KL-only已将output distribution对齐到接近dense水平（PPL 9.2 vs 6.12）， compensation网络能额外修正的residual极小（仅0.18 PPL），大部分interaction已被KL loss消化。 反观BCE的per-neuron factorized gradient只优化每个neuron独立的on/off decision，完全忽略joint effects——这在50% sparsity下产生巨大误差（PPL 28.2）。Compensation网络虽然能回收~40%的 质量gap（28.2→18.6），但其capacity有限，无法弥补BCE从根源上丢失的coupling information。 5-seed KL-only的极低std（0.04）证明s456不是outlier，训练高度稳定。 核心结论：compensation对KL是冗余的（0.18 PPL改善 vs 9.44 PPL gap），claims 1成立。\n"
86	  },
87	  {
88	    "name": "STE Baseline — Isolating Loss vs Relaxation",
89	    "description": "用Straight-Through Estimator替换Gumbel-sigmoid，保持KL loss不变。3 seeds。 目的：确认KL优势来自loss function而非Gumbel relaxation。\n",
90	    "results": {
91	      "ste_kl_s42_ppl": 9.72,
92	      "ste_kl_s123_ppl": 9.85,
93	      "ste_kl_s456_ppl": 9.64,
94	      "ste_kl_mean_ppl": 9.74,
95	      "ste_kl_std_ppl": 0.09,
96	      "ste_kl_model_sparsity": 0.497,
97	      "ste_kl_vs_gumbel_kl_gap": 0.54,
98	      "ste_kl_vs_bce_only_gap": 18.42,
99	      "gumbel_contribution_pct": 2.8
100	    },
101	    "tables": [
102	      {
103	        "name": "Table 2: Relaxation Method Ablation",
104	        "columns": [
105	          "Condition",
106	          "Relaxation",
107	          "Loss",
108	          "PPL (mean±std)"
109	        ],
110	        "rows": [
111	          [
112	            "Gumbel+KL (ours)",
113	            "Gumbel-sigmoid",
114	            "KL",
115	            "9.20±0.04"
116	          ],
117	          [
118	            "STE+KL",
119	            "Straight-Through",
120	            "KL",
121	            "9.74±0.09"
122	          ],
123	          [
124	            "Gumbel+BCE",
125	            "Gumbel-sigmoid",
126	            "BCE",
127	            "28.16±0.17"
128	          ]
129	        ]
130	      }
131	    ],
132	    "figures": [],
133	    "analysis": "STE实验明确归因：KL的gradient coupling是优势的几乎全部来源（97%），Gumbel relaxation是 锦上添花的minor optimization trick。这为理论narrative提供clean experimental support， 且预防了reviewer的alternative explanation attack。\n\n\nSTE用biased but unbiased-in-expectation的梯度直通传播，丢失了Gumbel relaxation提供的 smooth gradient landscape。因此STE+KL比Gumbel+KL略差（+0.54 PPL），对应predictor在 decision boundary附近的optimization稍差。但关键是STE+KL（9.74）仍远优于Gumbel+BCE（28.16）， 说明KL-BCE的18.96 point gap中97%以上来自loss function的gradient coupling property， Gumbel relaxation仅贡献~3%的marginal improvement。这直接排除了reviewer concern \"Gumbel-sigmoid relaxation, not KL, explains gains\"。\n"
134	  },
135	  {
136	    "name": "Iso-Compute BCE vs KL",
137	    "description": "KL每步需full forward pass计算logit targets（~3.2x BCE per-step FLOPs）。 给BCE同等total FLOPs预算（3.2x steps），排除compute advantage。3 seeds。\n",
138	    "results": {
139	      "kl_steps": 1000,
140	      "kl_flops_per_step_ratio": 3.2,
141	      "kl_total_flops_ratio": 3200,
142	      "bce_standard_steps": 1000,
143	      "bce_extended_steps": 3200,
144	      "bce_extended_total_flops_ratio": 3200,
145	      "bce_extended_s42_ppl": 25.28,
146	      "bce_extended_s123_ppl": 25.83,
147	      "bce_extended_s456_ppl": 25.12,
148	      "bce_extended_mean_ppl": 25.41,
149	      "bce_extended_std_ppl": 0.31,
150	      "bce_standard_mean_ppl": 28.16,
151	      "improvement_from_extended_training": 2.75,
152	      "remaining_gap_vs_kl": 16.21,
153	      "training_wall_clock_kl_hours": 4.2,
154	      "training_wall_clock_bce_extended_hours": 4.1
155	    },
156	    "tables": [
157	      {
158	        "name": "Table 3: Iso-Compute Comparison",
159	        "columns": [
160	          "Condition",
161	          "Steps",
162	          "Total FLOPs (relative)",
163	          "PPL (mean±std)"
164	        ],
165	        "rows": [
166	          [
167	            "KL (Gumbel)",
168	            1000,
169	            "3200x",
170	            "9.20±0.04"
171	          ],
172	          [
173	            "BCE (standard)",
174	            1000,
175	            "1000x",
176	            "28.16±0.17"
177	          ],
178	          [
179	            "BCE (extended)",
180	            3200,
181	            "3200x",
182	            "25.41±0.31"
183	          ]
184	        ]
185	      }
186	    ],
187	    "figures": [],
188	    "analysis": "即使给BCE 3.2x的training budget，PPL只从28.16降到25.41，distance to KL-only（16.21） 几乎未缩小。BCE的information bottleneck在loss function级别，无法通过更多compute突破。\n\n\nBCE的梯度dL_BCE/ds_j = (σ(s_j) - t_j) * σ'(s_j)仅依赖neuron j自身的target， 更多training steps只能更精确地拟合这个per-neuron target——但target本身就是次优的 （忽略joint interaction）。因此extended training让BCE-only从28.16降到25.41（降2.75）， 收益递减明显（loss curve在~2000步后plateau），而与KL的gap仍有16.21 points。 这证明KL的优势是information-theoretic的（loss function的gradient structure差异）， 不是compute-driven的，直接回应reviewer concern \"KL wins only because more compute\"。\n"
189	  },
190	  {
191	    "name": "SPON Reimplementation & Validation",
192	    "description": "在Llama 3.1 8B上重新实现SPON（learnable per-layer bias vectors + KL training）， 在5个QA benchmarks上验证质量以确认实现正确性。\n",
193	    "results": {
194	      "spon_wikitext2_ppl": 10.82,
195	      "spon_model_sparsity": 0.501,
196	      "spon_ppl_increase_vs_dense_pct": 76.9,
197	      "spon_arc_c": 51.2,
198	      "spon_arc_e": 74.5,
199	      "spon_boolq": 79.3,
200	      "spon_piqa": 78.1,
201	      "spon_winogrande": 74.8,
202	      "spon_params_bytes": 1048576,
203	      "spon_training_time_minutes": 12,
204	      "dense_arc_c": 55.2,
205	      "dense_arc_e": 79.4,
206	      "dense_boolq": 83.1,
207	      "dense_piqa": 81.3,
208	      "dense_winogrande": 77.8
209	    },
210	    "tables": [
211	      {
212	        "name": "Table 4: SPON Validation on QA Benchmarks",
213	        "columns": [
214	          "Benchmark",
215	          "Dense",
216	          "SPON",
217	          "Δ (abs)"
218	        ],
219	        "rows": [
220	          [
221	            "ARC-c",
222	            55.2,
223	            51.2,
224	            "−4.0"
225	          ],
226	          [
227	            "ARC-e",
228	            79.4,
229	            74.5,
230	            "−4.9"
231	          ],
232	          [
233	            "BoolQ",
234	            83.1,
235	            79.3,
236	            "−3.8"
237	          ],
238	          [
239	            "PIQA",
240	            81.3,
241	            78.1,
242	            "−3.2"
243	          ],
244	          [
245	            "WinoGrande",
246	            77.8,
247	            74.8,
248	            "−3.0"
249	          ]
250	        ]
251	      }
252	    ],
253	    "figures": [],
254	    "analysis": "SPON实现通过QA benchmark验证，drops幅度与原论文一致（3-5 points），确认实现正确性。 PPL 10.82定位在training-free（12-13）和contextual-KL（9.2）之间，为claim 2 的additivity实验提供可靠的static correction baseline。\n\n\nSPON使用input-independent的bias correction——本质上是per-layer calibration，矫正average-case 下sparsity引入的activation drift。由于是static的，它只能修正E[Δh]（期望偏移），无法处理 per-input variation Var[Δh|x]。因此SPON将PPL从training-free水平（~12-13）压到10.82， 是一个meaningful but limited的improvement。QA benchmarks上drops 3-6%符合PPL改善幅度。 SPON的主要价值不在于standalone quality，而是作为composition实验的building block—— 它修正的orthogonal component（average drift）与contextual predictor修正的component（per-input variation） 应当可加。\n"
255	  },
256	  {
257	    "name": "SPON + KL Predictor Composition",
258	    "description": "同时应用SPON bias correction和KL contextual prediction。 测试output-space linearity（interaction residual）和per-layer orthogonality。3 seeds。\n",
259	    "results": {
260	      "spon_kl_s42_ppl": 7.95,
261	      "spon_kl_s123_ppl": 8.12,
262	      "spon_kl_s456_ppl": 7.88,
263	      "spon_kl_mean_ppl": 7.98,
264	      "spon_kl_std_ppl": 0.1,
265	      "spon_kl_model_sparsity": 0.499,
266	      "spon_kl_ppl_increase_vs_dense_pct": 30.4,
267	      "spon_alone_ppl_recovery": 1.68,
268	      "kl_alone_ppl_recovery": 3.3,
269	      "combined_ppl_recovery": 4.52,
270	      "predicted_additive_recovery": 4.98,
271	      "interaction_residual_pct": 6.8,
272	      "logit_interaction_residual_l2_norm": 0.042,
273	      "logit_spon_correction_l2_norm": 0.38,
274	      "logit_kl_correction_l2_norm": 0.61,
275	      "logit_interaction_ratio_pct": 6.8,
276	      "mean_cosine_similarity_spon_kl": 0.11,
277	      "max_cosine_similarity_spon_kl": 0.23,
278	      "layers_with_cosine_gt_0_2": 4
279	    },
280	    "tables": [
281	      {
282	        "name": "Table 5: Composition Additivity Analysis",
283	        "columns": [
284	          "Component",
285	          "PPL Recovery (from TEAL baseline)",
286	          "Predicted Additive",
287	          "Actual",
288	          "Interaction Residual"
289	        ],
290	        "rows": [
291	          [
292	            "SPON only",
293	            1.68,
294	            "-",
295	            "-",
296	            "-"
297	          ],
298	          [
299	            "KL only",
300	            3.3,
301	            "-",
302	            "-",
303	            "-"
304	          ],
305	          [
306	            "SPON+KL",
307	            "-",
308	            4.98,
309	            4.52,
310	            "9.2%"
311	          ]
312	        ]
313	      },
314	      {
315	        "name": "Table 5b: Per-Layer Cosine Similarity Statistics",
316	        "columns": [
317	          "Statistic",
318	          "Value"
319	        ],
320	        "rows": [
321	          [
322	            "Mean cosine",
323	            0.11
324	          ],
325	          [
326	            "Median cosine",
327	            0.08
328	          ],
329	          [
330	            "Max cosine",
331	            0.23
332	          ],
333	          [
334	            "Layers > 0.2",
335	            "4/32"
336	          ]
337	        ]
338	      }
339	    ],
340	    "figures": [],
341	    "analysis": "SPON+KL组合将PPL压到7.98（仅比dense高30%），interaction residual 6.8% < 10%阈值， per-layer cosine similarity平均0.11。c = c_s + c_θ(x)的modular decomposition experimentally validated。两种correction address不同error sources的理论预测被定量确认。\n\n\nSPON修正c_s = E[Δh]（average activation drift），KL predictor修正c_θ(x) = Δh(x) - E[Δh] （per-input residual variation）。两者在correction space中近似正交——SPON的correction是 constant vector，KL的correction是zero-mean（训练过程中自然去中心化）。因此组合 c = c_s + c_θ(x)的interaction residual很小（6.8%）。PPL从KL-only的9.20进一步压到7.98， 接近dense的6.12。mean cosine similarity仅0.11，证明两种correction确实address不同的 error components。少数layers（4/32）cosine > 0.2，是因为某些layers的average drift 和per-input variation方向部分对齐（如early layers的token-independent patterns）， 但这不影响整体additivity。Claim 2（modular decomposition）直接成立。\n"
342	  },
343	  {
344	    "name": "Training-Free Baselines (TEAL, WINA, R-Sparse)",
345	    "description": "三种training-free方法在Llama 3.1 8B @ 50% model-level sparsity下的质量。 建立三级hierarchy: training-free < static-learned < contextual-learned。\n",
346	    "results": {
347	      "teal_wikitext2_ppl": 12.48,
348	      "wina_wikitext2_ppl": 14.76,
349	      "rsparse_wikitext2_ppl": 13.62,
350	      "teal_model_sparsity": 0.5,
351	      "wina_model_sparsity": 0.5,
352	      "rsparse_model_sparsity": 0.5,
353	      "teal_ppl_increase_vs_dense_pct": 103.9,
354	      "wina_ppl_increase_vs_dense_pct": 141.3,
355	      "rsparse_ppl_increase_vs_dense_pct": 122.6
356	    },
357	    "tables": [
358	      {
359	        "name": "Table 6: Training-Free Baseline Comparison",
360	        "columns": [
361	          "Method",
362	          "Type",
363	          "WikiText-2 PPL",
364	          "Δ vs Dense"
365	        ],
366	        "rows": [
367	          [
368	            "Dense",
369	            "-",
370	            6.12,
371	            "-"
372	          ],
373	          [
374	            "TEAL",
375	            "Magnitude + greedy",
376	            12.48,
377	            "+104%"
378	          ],
379	          [
380	            "R-Sparse",
381	            "Rank-aware",
382	            13.62,
383	            "+123%"
384	          ],
385	          [
386	            "WINA",
387	            "Weight-informed",
388	            14.76,
389	            "+141%"
390	          ],
391	          [
392	            "SPON",
393	            "Static learned (KL)",
394	            10.82,
395	            "+77%"
396	          ],
397	          [
398	            "KL-only",
399	            "Contextual learned (KL)",
400	            9.2,
401	            "+50%"
402	          ]
403	        ]
404	      }
405	    ],
406	    "figures": [],
407	    "analysis": "三级hierarchy清晰：training-free (12.5-14.8) < static-learned (10.8) < contextual-learned (9.2)。 每级提升对应information quality的提高：heuristic → average-case calibration → per-input optimization。 TEAL作为最强training-free baseline仍比KL-only差3.28 PPL points（+36%），justifies learned approach的overhead。\n\n\nTEAL使用magnitude pruning + greedy per-layer allocation，在training-free中最优，因为 magnitude直接反映activation contribution。R-Sparse加入rank-aware scoring，理论上更好但 实现中的approximation引入noise，实际略逊于TEAL。WINA的weight-informed scoring虽然 考虑了weight magnitude，但在SwiGLU的gated结构下，weight和activation importance的 correlation比standard FFN更弱（gate和up projection交互），因此表现最差。 所有三种方法PPL都在12-15范围，远逊于learned methods（KL-only 9.2、SPON 10.8）， 建立clean的三级hierarchy。Training-free方法的根本限制是它们无法learn per-input neuron importance patterns，只能依赖固定heuristic。\n"
408	  },
409	  {
410	    "name": "Full Benchmark Suite + Latency Profiling",
411	    "description": "所有conditions在WikiText-2/C4 PPL、5个discriminative tasks、wall-clock profiling上的 完整evaluation。构建efficiency-accuracy Pareto frontier。\n",
412	    "results": {
413	      "dense_wikitext2_ppl": 6.12,
414	      "teal_wikitext2_ppl": 12.48,
415	      "wina_wikitext2_ppl": 14.76,
416	      "rsparse_wikitext2_ppl": 13.62,
417	      "spon_wikitext2_ppl": 10.82,
418	      "bce_only_wikitext2_ppl": 28.16,
419	      "bce_comp_wikitext2_ppl": 18.64,
420	      "kl_only_wikitext2_ppl": 9.2,
421	      "kl_comp_wikitext2_ppl": 9.02,
422	      "spon_kl_wikitext2_ppl": 7.98,
423	      "dense_c4_ppl": 7.85,
424	      "teal_c4_ppl": 15.12,
425	      "wina_c4_ppl": 17.88,
426	      "rsparse_c4_ppl": 16.31,
427	      "spon_c4_ppl": 13.24,
428	      "bce_only_c4_ppl": 33.42,
429	      "bce_comp_c4_ppl": 22.15,
430	      "kl_only_c4_ppl": 11.38,
431	      "kl_comp_c4_ppl": 11.12,
432	      "spon_kl_c4_ppl": 9.81,
433	      "dense_arc_c": 55.2,
434	      "teal_arc_c": 48.1,
435	      "wina_arc_c": 46.3,
436	      "rsparse_arc_c": 47.2,
437	      "spon_arc_c": 51.2,
438	      "bce_comp_arc_c": 44.8,
439	      "kl_only_arc_c": 54.3,
440	      "spon_kl_arc_c": 54.8,
441	      "dense_winogrande": 77.8,
442	      "teal_winogrande": 72.4,
443	      "wina_winogrande": 70.8,
444	      "rsparse_winogrande": 71.5,
445	      "spon_winogrande": 74.8,
446	      "bce_comp_winogrande": 68.3,
447	      "kl_only_winogrande": 76.9,
448	      "spon_kl_winogrande": 77.2,
449	      "dense_mmlu": 65.8,
450	      "teal_mmlu": 58.2,
451	      "wina_mmlu": 56.4,
452	      "rsparse_mmlu": 57.1,
453	      "spon_mmlu": 60.3,
454	      "bce_comp_mmlu": 54.9,
455	      "kl_only_mmlu": 65.0,
456	      "spon_kl_mmlu": 65.4,
457	      "dense_gsm8k": 53.8,
458	      "teal_gsm8k": 44.2,
459	      "wina_gsm8k": 41.8,
460	      "rsparse_gsm8k": 43.1,
461	      "spon_gsm8k": 46.5,
462	      "bce_comp_gsm8k": 39.7,
463	      "kl_only_gsm8k": 52.8,
464	      "spon_kl_gsm8k": 53.2,
465	      "dense_humaneval": 32.9,
466	      "teal_humaneval": 26.2,
467	      "wina_humaneval": 24.4,
468	      "rsparse_humaneval": 25.6,
469	      "spon_humaneval": 28.1,
470	      "bce_comp_humaneval": 23.8,
471	      "kl_only_humaneval": 32.3,
472	      "spon_kl_humaneval": 32.5,
473	      "kl_only_avg_acc_drop_pct": 1.3,
474	      "spon_kl_avg_acc_drop_pct": 0.7,
475	      "bce_comp_avg_acc_drop_pct": 12.8,
476	      "dense_latency_ms": 16.8,
477	      "teal_latency_ms": 11.2,
478	      "spon_latency_ms": 10.9,
479	      "bce_only_latency_ms": 12.0,
480	      "bce_comp_latency_ms": 13.8,
481	      "kl_only_latency_ms": 12.0,
482	      "kl_comp_latency_ms": 13.8,
483	      "spon_kl_latency_ms": 12.1,
484	      "predictor_params_mb": 24,
485	      "compensation_params_mb": 256,
486	      "spon_params_mb": 1,
487	      "kl_only_speedup_vs_dense_pct": 28.6,
488	      "bce_comp_speedup_vs_dense_pct": 17.9,
489	      "kl_only_speedup_vs_bce_comp_pct": 13.0
490	    },
491	    "tables": [
492	      {
493	        "name": "Table 7: Comprehensive Benchmark Results (Llama 3.1 8B, 50% sparsity)",
494	        "columns": [
495	          "Method",
496	          "Wiki PPL↓",
497	          "C4 PPL↓",
498	          "ARC-c↑",
499	          "WinoG↑",
500	          "MMLU↑",
501	          "GSM8K↑",
502	          "HumanE↑",
503	          "Avg Δ↓"
504	        ],
505	        "rows": [
506	          [
507	            "Dense",
508	            6.12,
509	            7.85,
510	            55.2,
511	            77.8,
512	            65.8,
513	            53.8,
514	            32.9,
515	            "—"
516	          ],
517	          [
518	            "TEAL",
519	            12.48,
520	            15.12,
521	            48.1,
522	            72.4,
523	            58.2,
524	            44.2,
525	            26.2,
526	            "−7.8"
527	          ],
528	          [
529	            "WINA",
530	            14.76,
531	            17.88,
532	            46.3,
533	            70.8,
534	            56.4,
535	            41.8,
536	            24.4,
537	            "−9.9"
538	          ],
539	          [
540	            "R-Sparse",
541	            13.62,
542	            16.31,
543	            47.2,
544	            71.5,
545	            57.1,
546	            43.1,
547	            25.6,
548	            "−8.8"
549	          ],
550	          [
551	            "SPON",
552	            10.82,
553	            13.24,
554	            51.2,
555	            74.8,
556	            60.3,
557	            46.5,
558	            28.1,
559	            "−5.3"
560	          ],
561	          [
562	            "BCE+comp",
563	            18.64,
564	            22.15,
565	            44.8,
566	            68.3,
567	            54.9,
568	            39.7,
569	            23.8,
570	            "−12.8"
571	          ],
572	          [
573	            "KL-only",
574	            9.2,
575	            11.38,
576	            54.3,
577	            76.9,
578	            65.0,
579	            52.8,
580	            32.3,
581	            "−1.3"
582	          ],
583	          [
584	            "SPON+KL",
585	            7.98,
586	            9.81,
587	            54.8,
588	            77.2,
589	            65.4,
590	            53.2,
591	            32.5,
592	            "−0.7"
593	          ]
594	        ]
595	      },
596	      {
597	        "name": "Table 8: Inference Efficiency Comparison",
598	        "columns": [
599	          "Method",
600	          "Latency (ms/tok)",
601	          "Speedup vs Dense",
602	          "Extra Params (MB)",
603	          "PPL"
604	        ],
605	        "rows": [
606	          [
607	            "Dense",
608	            16.8,
609	            "1.00×",
610	            0,
611	            6.12
612	          ],
613	          [
614	            "TEAL",
615	            11.2,
616	            "1.50×",
617	            0,
618	            12.48
619	          ],
620	          [
621	            "SPON",
622	            10.9,
623	            "1.54×",
624	            1,
625	            10.82
626	          ],
627	          [
628	            "KL-only",
629	            12.0,
630	            "1.40×",
631	            24,
632	            9.2
633	          ],
634	          [
635	            "BCE+comp",
636	            13.8,
637	            "1.22×",
638	            280,
639	            18.64
640	          ],
641	          [
642	            "SPON+KL",
643	            12.1,
644	            "1.39×",
645	            25,
646	            7.98
647	          ]
648	        ]
649	      }
650	    ],
651	    "figures": [],
652	    "analysis": "KL-only在quality-efficiency Pareto frontier上strictly dominates BCE+comp：更低PPL（9.20 vs 18.64）， 更低latency（12.0 vs 13.8），更少参数（24MB vs 280MB）。Downstream tasks确认PPL gains transfer：KL-only平均仅drop 1.3%（best tier阈值2%以内），BCE+comp drop 12.8%。 SPON+KL作为our best configuration达到7.98 PPL和0.7%平均drop，接近free lunch。 Taxonomy table的每个cell都有实验数据支撑。\n\n\nDownstream tasks与PPL高度correlated——KL-only的低PPL (9.20)直接转化为downstream任务上 接近dense的accuracy（平均drop仅1.3%）。这是因为KL优化output distribution matching， 保留了token-level的prediction quality，而downstream tasks本质上都依赖model的next-token prediction能力。BCE+comp虽然有compensation，但其PPL (18.64)反映的distribution mismatch 在需要precise reasoning的任务上（GSM8K, HumanEval）伤害更大（drop 26-28%），因为 这些任务对error compounding更敏感。 Wall-clock方面，KL-only和BCE-only的predictor开销相同（同架构），但KL-only不需要 compensation，因此比BCE+comp省1.8ms/token（13.8→12.0）。SPON+KL仅比KL-only多0.1ms （bias add几乎免费），但PPL进一步降到7.98。KL-only在Pareto frontier上dominates BCE+comp——更快、更好、更小。\n"
653	  },
654	  {
655	    "name": "7-Level Sparsity Sweep — Quadratic Scaling Test",
656	    "description": "在30/35/40/45/50/55/60%七个sparsity level下训练KL-only和BCE-only（各1 seed）， 测试KL-BCE delta ∝ s²的理论预测。50%复用plan_001。每个level做Taylor expansion accuracy test。\n",
657	    "results": {
658	      "sparsity_levels": [
659	        0.3,
660	        0.35,
661	        0.4,
662	        0.45,
663	        0.5,
664	        0.55,
665	        0.6
666	      ],
667	      "kl_ppls": [
668	        7.05,
669	        7.42,
670	        7.98,
671	        8.51,
672	        9.2,
673	        10.82,
674	        13.15
675	      ],
676	      "bce_ppls": [
677	        14.55,
678	        17.82,
679	        19.98,
680	        24.71,
681	        28.2,
682	        33.62,
683	        42.65
684	      ],
685	      "kl_bce_deltas": [
686	        7.5,
687	        10.4,
688	        12.0,
689	        16.2,
690	        19.0,
691	        22.8,
692	        29.5
693	      ],
694	      "s2_fit_coefficient_a": 79.2,
695	      "s2_fit_r_squared": 0.97,
696	      "s2_plus_linear_fit_r_squared": 0.99,
697	      "taylor_accuracy_pct": [
698	        96.8,
699	        95.4,
700	        94.1,
701	        92.5,
702	        89.8,
703	        85.6,
704	        80.2
705	      ],
706	      "predicted_deltas_s2_only": [
707	        7.13,
708	        9.7,
709	        12.67,
710	        16.03,
711	        19.8,
712	        23.96,
713	        28.51
714	      ]
715	    },
716	    "tables": [
717	      {
718	        "name": "Table 9: Sparsity Sweep Results",
719	        "columns": [
720	          "Sparsity s",
721	          "s²",
722	          "KL PPL",
723	          "BCE PPL",
724	          "Δ (BCE−KL)",
725	          "Predicted Δ (as²)",
726	          "Taylor Acc %"
727	        ],
728	        "rows": [
729	          [
730	            0.3,
731	            0.09,
732	            7.05,
733	            14.55,
734	            7.5,
735	            7.13,
736	            96.8
737	          ],
738	          [
739	            0.35,
740	            0.123,
741	            7.42,
742	            17.82,
743	            10.4,
744	            9.7,
745	            95.4
746	          ],
747	          [
748	            0.4,
749	            0.16,
750	            7.98,
751	            19.98,
752	            12.0,
753	            12.67,
754	            94.1
755	          ],
756	          [
757	            0.45,
758	            0.203,
759	            8.51,
760	            24.71,
761	            16.2,
762	            16.03,
763	            92.5
764	          ],
765	          [
766	            0.5,
767	            0.25,
768	            9.2,
769	            28.2,
770	            19.0,
771	            19.8,
772	            89.8
773	          ],
774	          [
775	            0.55,
776	            0.303,
777	            10.82,
778	            33.62,
779	            22.8,
780	            23.96,
781	            85.6
782	          ],
783	          [
784	            0.6,
785	            0.36,
786	            13.15,
787	            42.65,
788	            29.5,
789	            28.51,
790	            80.2
791	          ]
792	        ]
793	      },
794	      {
795	        "name": "Table 9b: Scaling Fit Statistics",
796	        "columns": [
797	          "Model",
798	          "R²",
799	          "Parameters"
800	        ],
801	        "rows": [
802	          [
803	            "Δ = as²",
804	            0.97,
805	            "a=79.2"
806	          ],
807	          [
808	            "Δ = as² + bs",
809	            0.99,
810	            "a=68.1, b=5.8"
811	          ],
812	          [
813	            "Δ = as² + bs + c",
814	            0.99,
815	            "a=65.3, b=7.2, c=−0.4"
816	          ]
817	        ]
818	      }
819	    ],
820	    "figures": [],
821	    "analysis": "KL-BCE delta与s²的R²=0.97，定量验证了gradient coupling theory的核心预测。 Quadratic scaling意味着在高sparsity regime（>50%），KL的优势accelerates—— 这提供了一个可检验的、非trivial的理论预测，不仅描述已有数据，也predicts extrapolation behavior。Taylor accuracy的graceful degradation pattern进一步 增强理论credibility。Claim 3直接成立。\n\n\nKL的梯度dL_KL/ds_j通过Jacobian d_logits/dh耦合所有active neurons。当sparsity为s时， 每个pruned neuron的interaction涉及O(sD)个其他pruned neurons，total interaction scale为 O(s²D²)。BCE的factorized gradient完全忽略这些interactions。因此KL-BCE quality delta 应当scale as s²（leading term来自pairwise neuron interaction）。 实验数据R²=0.97证实quadratic scaling dominates。Taylor expansion在低sparsity（30-40%） 下accuracy > 94%是因为higher-order terms（s³等）negligible；在高sparsity（55-60%） accuracy降到80-86%是因为三体及更高阶interaction开始significant——这本身也是consistent with the theory（Taylor展开在远离展开点时精度下降）。 加入linear term后R²=0.99，说明residual主要是one lower-order correction。 Claim 3（quadratic scaling）定量验证通过。\n"
822	  },
823	  {
824	    "name": "Mistral-7B-v0.3 Cross-Architecture Validation",
825	    "description": "在Mistral-7B-v0.3（GQA + sliding window attention，不同于Llama的GQA-only）上 复现KL-only vs BCE+comp comparison。Core benchmarks: WikiText-2 PPL, ARC-c, MMLU。3 seeds each。\n",
826	    "results": {
827	      "mistral_dense_wikitext2_ppl": 5.48,
828	      "mistral_dense_arc_c": 58.1,
829	      "mistral_dense_mmlu": 62.8,
830	      "mistral_kl_s42_ppl": 8.12,
831	      "mistral_kl_s123_ppl": 8.35,
832	      "mistral_kl_s456_ppl": 8.18,
833	      "mistral_kl_mean_ppl": 8.22,
834	      "mistral_kl_std_ppl": 0.1,
835	      "mistral_kl_model_sparsity": 0.498,
836	      "mistral_kl_ppl_increase_vs_dense_pct": 50.0,
837	      "mistral_kl_arc_c": 56.4,
838	      "mistral_kl_mmlu": 61.3,
839	      "mistral_bce_comp_s42_ppl": 12.81,
840	      "mistral_bce_comp_s123_ppl": 13.24,
841	      "mistral_bce_comp_s456_ppl": 12.53,
842	      "mistral_bce_comp_mean_ppl": 12.86,
843	      "mistral_bce_comp_std_ppl": 0.29,
844	      "mistral_bce_comp_model_sparsity": 0.497,
845	      "mistral_bce_comp_arc_c": 50.8,
846	      "mistral_bce_comp_mmlu": 55.9,
847	      "mistral_kl_vs_bce_comp_ppl_gap": 4.64,
848	      "mistral_kl_vs_bce_comp_ppl_gap_pct": 36.1
849	    },
850	    "tables": [
851	      {
852	        "name": "Table 10: Mistral-7B-v0.3 Cross-Architecture Validation",
853	        "columns": [
854	          "Condition",
855	          "Wiki PPL↓",
856	          "ARC-c↑",
857	          "MMLU↑"
858	        ],
859	        "rows": [
860	          [
861	            "Dense",
862	            5.48,
863	            58.1,
864	            62.8
865	          ],
866	          [
867	            "KL-only",
868	            "8.22±0.10",
869	            56.4,
870	            61.3
871	          ],
872	          [
873	            "BCE+comp",
874	            "12.86±0.29",
875	            50.8,
876	            55.9
877	          ],
878	          [
879	            "Gap (KL vs BCE+comp)",
880	            "−4.64",
881	            "+5.6",
882	            "+5.4"
883	          ]
884	        ]
885	      },
886	      {
887	        "name": "Table 10b: Cross-Architecture Consistency",
888	        "columns": [
889	          "Metric",
890	          "Llama 3.1 8B",
891	          "Mistral-7B-v0.3"
892	        ],
893	        "rows": [
894	          [
895	            "KL PPL increase vs dense",
896	            "50.3%",
897	            "50.0%"
898	          ],
899	          [
900	            "KL vs BCE+comp gap (PPL)",
901	            9.44,
902	            4.64
903	          ],
904	          [
905	            "KL vs BCE+comp gap (%)",
906	            "50.6%",
907	            "36.1%"
908	          ]
909	        ]
910	      }
911	    ],
912	    "figures": [],
913	    "analysis": "Mistral-7B-v0.3成功复现KL dominance：KL-only (8.22) vs BCE+comp (12.86)，gap 36%。 KL PPL increase vs dense（50%）与Llama（50.3%）惊人一致，证明KL的优势是loss function 的universal property而非architecture-specific artifact。排除reviewer concern \"Single model / limited generalization\"。\n\n\nMistral-7B-v0.3使用GQA + sliding window attention，SwiGLU FFN结构与Llama相同但 attention pattern不同，导致不同的activation sparsity distribution。KL的gradient coupling property是loss function的数学性质，与architecture无关——只要model有SwiGLU FFN且sparsity 在hidden states上操作，KL就能捕获joint interactions。因此KL优势在Mistral上同方向复现。 PPL increase 50%（vs Llama的50.3%）高度一致。Gap绝对值（4.64 vs 9.44）较小是因为 Mistral的dense PPL更低（5.48 vs 6.12），两个model的relative gap pattern一致。 Sliding window attention可能使某些layers的neuron importance更localized，略微 降低BCE+comp的absolute PPL（12.86 vs Llama的18.64），但不改变KL dominance。\n"
914	  },
915	  {
916	    "name": "LongBench Long-Context Evaluation",
917	    "description": "LongBench English subset（4K-32K tokens），所有conditions。 Per-task-type breakdown: single-doc QA, multi-doc QA, summarization, few-shot, code。\n",
918	    "results": {
919	      "dense_longbench_avg": 43.5,
920	      "teal_longbench_avg": 35.4,
921	      "wina_longbench_avg": 33.8,
922	      "rsparse_longbench_avg": 34.6,
923	      "spon_longbench_avg": 39.8,
924	      "bce_comp_longbench_avg": 32.1,
925	      "kl_only_longbench_avg": 42.1,
926	      "spon_kl_longbench_avg": 42.8,
927	      "kl_single_doc_qa": 44.8,
928	      "kl_multi_doc_qa": 38.2,
929	      "kl_summarization": 42.5,
930	      "kl_few_shot": 47.1,
931	      "kl_code": 38.0,
932	      "bce_comp_single_doc_qa": 35.2,
933	      "bce_comp_multi_doc_qa": 28.4,
934	      "bce_comp_summarization": 33.8,
935	      "bce_comp_few_shot": 34.6,
936	      "bce_comp_code": 28.5,
937	      "dense_single_doc_qa": 46.2,
938	      "dense_multi_doc_qa": 39.5,
939	      "dense_summarization": 43.8,
940	      "dense_few_shot": 48.3,
941	      "dense_code": 39.6,
942	      "kl_only_avg_drop_vs_dense": 1.4,
943	      "bce_comp_avg_drop_vs_dense": 11.4,
944	      "kl_worst_task_type": "multi-doc QA",
945	      "kl_worst_task_drop": 3.3
946	    },
947	    "tables": [
948	      {
949	        "name": "Table 11: LongBench Per-Task-Type Breakdown",
950	        "columns": [
951	          "Task Type",
952	          "Dense",
953	          "TEAL",
954	          "SPON",
955	          "BCE+comp",
956	          "KL-only",
957	          "SPON+KL"
958	        ],
959	        "rows": [
960	          [
961	            "Single-doc QA",
962	            46.2,
963	            38.1,
964	            42.0,
965	            35.2,
966	            44.8,
967	            45.3
968	          ],
969	          [
970	            "Multi-doc QA",
971	            39.5,
972	            31.2,
973	            36.1,
974	            28.4,
975	            38.2,
976	            38.8
977	          ],
978	          [
979	            "Summarization",
980	            43.8,
981	            35.8,
982	            40.2,
983	            33.8,
984	            42.5,
985	            43.1
986	          ],
987	          [
988	            "Few-shot",
989	            48.3,
990	            39.5,
991	            44.3,
992	            34.6,
993	            47.1,
994	            47.8
995	          ],
996	          [
997	            "Code",
998	            39.6,
999	            32.4,
1000	            36.5,
1001	            28.5,
1002	            38.0,
1003	            38.9
1004	          ],
1005	          [
1006	            "**Average**",
1007	            "**43.5**",
1008	            "**35.4**",
1009	            "**39.8**",
1010	            "**32.1**",
1011	            "**42.1**",
1012	            "**42.8**"
1013	          ]
1014	        ]
1015	      }
1016	    ],
1017	    "figures": [],
1018	    "analysis": "LongBench结果证明KL predictor在长序列（4K-32K）下generalization良好（avg drop 1.4）， 无需长序列finetune。BCE+comp在long-context下进一步恶化（avg drop 11.4 vs short-context的12.8%）， 可能因为compensation网络对error accumulation的correction在长序列下saturate。 增强了EMNLP venue fit（NLP-specific long-context evaluation）。\n\n\n长序列evaluation测试predictor是否generalize beyond短训练序列。KL的output-distribution matching objective在长序列下仍然有效，因为它不依赖specific sequence length——predictor 看到的是per-token hidden states，length主要影响attention pattern。KL-only的drop（1.4 avg） 与short-context evaluation一致。Multi-doc QA是最challenging的任务类型（需要cross-document reasoning），因此KL-only在此处drop最大（3.3 points）。BCE+comp在长序列下degradation 更严重（11.4 avg drop）——因为BCE的per-neuron error在长序列中accumulates without compensation fully correcting the compounding effect。SPON+KL以42.8接近dense的43.5， 进一步确认composition在长序列下仍然有效。\n"
1019	  },
1020	  {
1021	    "name": "MT-Bench Multi-Turn Instruction Following",
1022	    "description": "MT-Bench 80题 × 8 categories，GPT-4o judge。测试sparsity对instruction following quality的影响。\n",
1023	    "results": {
1024	      "dense_mtbench_avg": 7.21,
1025	      "teal_mtbench_avg": 6.18,
1026	      "spon_mtbench_avg": 6.78,
1027	      "bce_comp_mtbench_avg": 6.42,
1028	      "kl_only_mtbench_avg": 7.05,
1029	      "spon_kl_mtbench_avg": 7.12,
1030	      "kl_writing": 7.35,
1031	      "kl_roleplay": 7.15,
1032	      "kl_reasoning": 6.65,
1033	      "kl_math": 6.55,
1034	      "kl_coding": 6.85,
1035	      "kl_extraction": 7.45,
1036	      "kl_stem": 7.1,
1037	      "kl_humanities": 7.3,
1038	      "bce_comp_writing": 6.8,
1039	      "bce_comp_reasoning": 5.85,
1040	      "bce_comp_math": 5.65,
1041	      "bce_comp_coding": 5.9
1042	    },
1043	    "tables": [
1044	      {
1045	        "name": "Table 12: MT-Bench Results",
1046	        "columns": [
1047	          "Method",
1048	          "Avg Score",
1049	          "Writing",
1050	          "Reasoning",
1051	          "Math",
1052	          "Coding"
1053	        ],
1054	        "rows": [
1055	          [
1056	            "Dense",
1057	            7.21,
1058	            7.5,
1059	            6.85,
1060	            6.8,
1061	            7.1
1062	          ],
1063	          [
1064	            "TEAL",
1065	            6.18,
1066	            6.45,
1067	            5.6,
1068	            5.4,
1069	            5.8
1070	          ],
1071	          [
1072	            "SPON",
1073	            6.78,
1074	            7.1,
1075	            6.35,
1076	            6.15,
1077	            6.55
1078	          ],
1079	          [
1080	            "BCE+comp",
1081	            6.42,
1082	            6.8,
1083	            5.85,
1084	            5.65,
1085	            5.9
1086	          ],
1087	          [
1088	            "KL-only",
1089	            7.05,
1090	            7.35,
1091	            6.65,
1092	            6.55,
1093	            6.85
1094	          ],
1095	          [
1096	            "SPON+KL",
1097	            7.12,
1098	            7.4,
1099	            6.75,
1100	            6.65,
1101	            6.95
1102	          ]
1103	        ]
1104	      }
1105	    ],
1106	    "figures": [],
1107	    "analysis": "MT-Bench进一步确认KL-only在generation quality上接近dense。GPT-4o judge评分差异 KL-only vs dense仅0.16——在judge的noise floor以内。BCE+comp在math/reasoning上 severe degradation（-1.15/-1.00 vs dense），而KL-only仅-0.25/-0.20。 Strengthens EMNLP NLP evaluation story。\n\n\nMT-Bench测试multi-turn instruction following——一个对output quality高度敏感的setting。 KL-only（7.05）与dense（7.21）差距仅0.16（GPT-4o judge的scoring granularity内）， 说明KL的output distribution matching直接保留了instruction following能力。 Math和reasoning categories drop略大（KL-only 6.55/6.65 vs dense ~6.8/6.85），因为 这些tasks需要precise multi-step reasoning，对任何distribution shift更敏感。 BCE+comp（6.42）在reasoning-heavy categories下degradation严重（5.85/5.65），因为 BCE的imprecise sparsity mask在需要所有neurons correctly participate的reasoning chain上 产生compounding errors，compensation无法fully recover。\n"
1108	  },
1109	  {
1110	    "name": "RULER Synthetic Long-Context Diagnostics",
1111	    "description": "RULER synthetic evaluation at 4K and 16K context，3 representative task types (needle-in-a-haystack, multi-key retrieval, variable tracking)。 Fine-grained diagnostics complementing LongBench。\n",
1112	    "results": {
1113	      "dense_ruler_4k_avg": 95.2,
1114	      "kl_only_ruler_4k_avg": 93.8,
1115	      "bce_comp_ruler_4k_avg": 87.4,
1116	      "spon_kl_ruler_4k_avg": 94.5,
1117	      "dense_ruler_16k_avg": 88.5,
1118	      "kl_only_ruler_16k_avg": 86.1,
1119	      "bce_comp_ruler_16k_avg": 78.3,
1120	      "spon_kl_ruler_16k_avg": 87.2,
1121	      "kl_needle_4k": 98.0,
1122	      "kl_needle_16k": 94.5,
1123	      "kl_multikey_4k": 91.2,
1124	      "kl_multikey_16k": 82.4,
1125	      "kl_vartrack_4k": 92.1,
1126	      "kl_vartrack_16k": 81.3,
1127	      "bce_comp_needle_4k": 94.5,
1128	      "bce_comp_needle_16k": 86.2,
1129	      "bce_comp_multikey_4k": 83.8,
1130	      "bce_comp_multikey_16k": 72.1,
1131	      "bce_comp_vartrack_4k": 83.9,
1132	      "bce_comp_vartrack_16k": 76.5,
1133	      "kl_only_4k_to_16k_drop": 7.7,
1134	      "bce_comp_4k_to_16k_drop": 9.1,
1135	      "dense_4k_to_16k_drop": 6.7
1136	    },
1137	    "tables": [
1138	      {
1139	        "name": "Table 13: RULER Synthetic Evaluation",
1140	        "columns": [
1141	          "Task",
1142	          "Context",
1143	          "Dense",
1144	          "KL-only",
1145	          "BCE+comp",
1146	          "SPON+KL"
1147	        ],
1148	        "rows": [
1149	          [
1150	            "Needle",
1151	            "4K",
1152	            99.2,
1153	            98.0,
1154	            94.5,
1155	            98.5
1156	          ],
1157	          [
1158	            "Needle",
1159	            "16K",
1160	            96.8,
1161	            94.5,
1162	            86.2,
1163	            95.8
1164	          ],
1165	          [
1166	            "Multi-key",
1167	            "4K",
1168	            93.5,
1169	            91.2,
1170	            83.8,
1171	            92.4
1172	          ],
1173	          [
1174	            "Multi-key",
1175	            "16K",
1176	            84.1,
1177	            82.4,
1178	            72.1,
1179	            83.5
1180	          ],
1181	          [
1182	            "Var-track",
1183	            "4K",
1184	            92.8,
1185	            92.1,
1186	            83.9,
1187	            92.5
1188	          ],
1189	          [
1190	            "Var-track",
1191	            "16K",
1192	            84.5,
1193	            81.3,
1194	            76.5,
1195	            83.2
1196	          ],
1197	          [
1198	            "**Average**",
1199	            "**4K**",
1200	            "**95.2**",
1201	            "**93.8**",
1202	            "**87.4**",
1203	            "**94.5**"
1204	          ],
1205	          [
1206	            "**Average**",
1207	            "**16K**",
1208	            "**88.5**",
1209	            "**86.1**",
1210	            "**78.3**",
1211	            "**87.2**"
1212	          ]
1213	        ]
1214	      }
1215	    ],
1216	    "figures": [],
1217	    "analysis": "RULER诊断补充LongBench：KL-only的context-length degradation pattern与dense一致 (4K→16K drop差仅1 point)，而BCE+comp多drop 2.4 points。Multi-key retrieval 是differentiation最大的task（KL 82.4 vs BCE+comp 72.1 at 16K），这与理论一致—— multi-key需要FFN准确处理多个simultaneously relevant positions，joint neuron interaction quality直接影响结果。\n\nRULER的synthetic tasks提供controlled diagnostics——每个task isolate一种capability (retrieval precision, multi-hop tracking等)。KL-only在4K下接近dense（93.8 vs 95.2）， 在16K下gracefully degrade（86.1 vs 88.5）——4K→16K drop (7.7)接近dense pattern (6.7)， 说明KL predictor不会随context length引入额外的degradation。BCE+comp的4K→16K drop更大 (9.1)，在multi-key retrieval（需要同时attend to多个scattered positions）和variable tracking（需要maintain state across distance）上degradation尤其严重——因为这些tasks 对sparse mask quality最敏感，BCE的imprecise masks在长距离dependency上compounding。 Needle-in-a-haystack是最简单的task（单点retrieval），所有methods都表现好。\n"
1218	  }
1219	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3d6e483-48d6-4f3c-8eb0-b72b58ceec95",
  "isSidechain": false,
  "promptId": "4324b22a-92db-42ef-a974-2006388d7cce",
  "type": "user",
  "uuid": "d01a10c7-ab9b-4b01-815d-4faec0bfa629",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Four-Condition Ablation @ 50% Sparsity\",\n    \"description\": \"KL-only扩展到5 seeds（新增s0, s1），BCE+comp 5 seeds，KL+comp 3 seeds。 已有数据：KL-only 3 seeds (s42/s123/s456)均~9.2 PPL；BCE-only 3 seeds均~28.2 PPL。\\n\",\n    \"results\": {\n      \"kl_only_s42_ppl\": 9.2142,\n      \"kl_only_s123_ppl\": 9.2474,\n      \"kl_only_s456_ppl\": 9.14,\n      \"kl_only_s0_ppl\": 9.19,\n      \"kl_only_s1_ppl\": 9.23,\n      \"kl_only_mean_ppl\": 9.2,\n      \"kl_only_std_ppl\": 0.04,\n      \"kl_only_model_sparsity\": 0.498,\n      \"bce_comp_s42_ppl\": 18.22,\n      \"bce_comp_s123_ppl\": 18.91,\n      \"bce_comp_s456_ppl\": 18.38,\n      \"bce_comp_s0_ppl\": 18.65,\n      \"bce_comp_s1_ppl\": 19.05,\n      \"bce_comp_mean_ppl\": 18.64,\n      \"bce_comp_std_ppl\": 0.33,\n      \"bce_comp_model_sparsity\": 0.496,\n      \"kl_comp_s42_ppl\": 9.05,\n      \"kl_comp_s123_ppl\": 9.08,\n      \"kl_comp_s456_ppl\": 8.92,\n      \"kl_comp_mean_ppl\": 9.02,\n      \"kl_comp_std_ppl\": 0.07,\n      \"bce_only_mean_ppl\": 28.16,\n      \"bce_only_std_ppl\": 0.17,\n      \"kl_only_vs_bce_comp_gap\": 9.44,\n      \"kl_only_vs_dense_increase_pct\": 50.3,\n      \"bce_comp_vs_dense_increase_pct\": 204.6,\n      \"comp_benefit_for_bce_ppl\": 9.52,\n      \"comp_benefit_for_kl_ppl\": 0.18\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Four-Condition Ablation Results (WikiText-2 PPL, Llama 3.1 8B, 50% sparsity)\",\n        \"columns\": [\n          \"Condition\",\n          \"Seeds\",\n          \"PPL (mean±std)\",\n          \"Δ vs Dense\",\n          \"Comp Benefit\"\n        ],\n        \"rows\": [\n          [\n            \"Dense\",\n            \"-\",\n            \"6.12\",\n            \"-\",\n            \"-\"\n          ],\n          [\n            \"BCE-only\",\n            3,\n            \"28.16±0.17\",\n            \"+360%\",\n            \"-\"\n          ],\n          [\n            \"BCE+comp\",\n            5,\n            \"18.64±0.33\",\n            \"+205%\",\n            \"−9.52\"\n          ],\n          [\n            \"KL-only\",\n            5,\n            \"9.20±0.04\",\n            \"+50%\",\n            \"-\"\n          ],\n          [\n            \"KL+comp\",\n            3,\n            \"9.02±0.07\",\n            \"+47%\",\n            \"−0.18\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"KL-only以9.20 PPL大幅碾压BCE+comp的18.64 PPL（gap 9.44 points），且compensation对KL仅贡献 0.18 PPL改善（vs对BCE贡献9.52），证明compensation网络对KL训练的predictor完全不必要。 5-seed std=0.04证明高度可复现。Headline claim直接成立：output-distribution distillation eliminates the need for compensation networks.\\n\\n\\nKL的gradient dL_KL/ds_j通过d_logits/dh * dh/dm耦合所有active neurons，天然捕获joint interaction effects。因此KL-only已将output distribution对齐到接近dense水平（PPL 9.2 vs 6.12）， compensation网络能额外修正的residual极小（仅0.18 PPL），大部分interaction已被KL loss消化。 反观BCE的per-neuron factorized gradient只优化每个neuron独立的on/off decision，完全忽略joint effects——这在50% sparsity下产生巨大误差（PPL 28.2）。Compensation网络虽然能回收~40%的 质量gap（28.2→18.6），但其capacity有限，无法弥补BCE从根源上丢失的coupling information。 5-seed KL-only的极低std（0.04）证明s456不是outlier，训练高度稳定。 核心结论：compensation对KL是冗余的（0.18 PPL改善 vs 9.44 PPL gap），claims 1成立。\\n\"\n  },\n  {\n    \"name\": \"STE Baseline — Isolating Loss vs Relaxation\",\n    \"description\": \"用Straight-Through Estimator替换Gumbel-sigmoid，保持KL loss不变。3 seeds。 目的：确认KL优势来自loss function而非Gumbel relaxation。\\n\",\n    \"results\": {\n      \"ste_kl_s42_ppl\": 9.72,\n      \"ste_kl_s123_ppl\": 9.85,\n      \"ste_kl_s456_ppl\": 9.64,\n      \"ste_kl_mean_ppl\": 9.74,\n      \"ste_kl_std_ppl\": 0.09,\n      \"ste_kl_model_sparsity\": 0.497,\n      \"ste_kl_vs_gumbel_kl_gap\": 0.54,\n      \"ste_kl_vs_bce_only_gap\": 18.42,\n      \"gumbel_contribution_pct\": 2.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2: Relaxation Method Ablation\",\n        \"columns\": [\n          \"Condition\",\n          \"Relaxation\",\n          \"Loss\",\n          \"PPL (mean±std)\"\n        ],\n        \"rows\": [\n          [\n            \"Gumbel+KL (ours)\",\n            \"Gumbel-sigmoid\",\n            \"KL\",\n            \"9.20±0.04\"\n          ],\n          [\n            \"STE+KL\",\n            \"Straight-Through\",\n            \"KL\",\n            \"9.74±0.09\"\n          ],\n          [\n            \"Gumbel+BCE\",\n            \"Gumbel-sigmoid\",\n            \"BCE\",\n            \"28.16±0.17\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"STE实验明确归因：KL的gradient coupling是优势的几乎全部来源（97%），Gumbel relaxation是 锦上添花的minor optimization trick。这为理论narrative提供clean experimental support， 且预防了reviewer的alternative explanation attack。\\n\\n\\nSTE用biased but unbiased-in-expectation的梯度直通传播，丢失了Gumbel relaxation提供的 smooth gradient landscape。因此STE+KL比Gumbel+KL略差（+0.54 PPL），对应predictor在 decision boundary附近的optimization稍差。但关键是STE+KL（9.74）仍远优于Gumbel+BCE（28.16）， 说明KL-BCE的18.96 point gap中97%以上来自loss function的gradient coupling property， Gumbel relaxation仅贡献~3%的marginal improvement。这直接排除了reviewer concern \\\"Gumbel-sigmoid relaxation, not KL, explains gains\\\"。\\n\"\n  },\n  {\n    \"name\": \"Iso-Compute BCE vs KL\",\n    \"description\": \"KL每步需full forward pass计算logit targets（~3.2x BCE per-step FLOPs）。 给BCE同等total FLOPs预算（3.2x steps），排除compute advantage。3 seeds。\\n\",\n    \"results\": {\n      \"kl_steps\": 1000,\n      \"kl_flops_per_step_ratio\": 3.2,\n      \"kl_total_flops_ratio\": 3200,\n      \"bce_standard_steps\": 1000,\n      \"bce_extended_steps\": 3200,\n      \"bce_extended_total_flops_ratio\": 3200,\n      \"bce_extended_s42_ppl\": 25.28,\n      \"bce_extended_s123_ppl\": 25.83,\n      \"bce_extended_s456_ppl\": 25.12,\n      \"bce_extended_mean_ppl\": 25.41,\n      \"bce_extended_std_ppl\": 0.31,\n      \"bce_standard_mean_ppl\": 28.16,\n      \"improvement_from_extended_training\": 2.75,\n      \"remaining_gap_vs_kl\": 16.21,\n      \"training_wall_clock_kl_hours\": 4.2,\n      \"training_wall_clock_bce_extended_hours\": 4.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Iso-Compute Comparison\",\n        \"columns\": [\n          \"Condition\",\n          \"Steps\",\n          \"Total FLOPs (relative)\",\n          \"PPL (mean±std)\"\n        ],\n        \"rows\": [\n          [\n            \"KL (Gumbel)\",\n            1000,\n            \"3200x\",\n            \"9.20±0.04\"\n          ],\n          [\n            \"BCE (standard)\",\n            1000,\n            \"1000x\",\n            \"28.16±0.17\"\n          ],\n          [\n            \"BCE (extended)\",\n            3200,\n            \"3200x\",\n            \"25.41±0.31\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"即使给BCE 3.2x的training budget，PPL只从28.16降到25.41，distance to KL-only（16.21） 几乎未缩小。BCE的information bottleneck在loss function级别，无法通过更多compute突破。\\n\\n\\nBCE的梯度dL_BCE/ds_j = (σ(s_j) - t_j) * σ'(s_j)仅依赖neuron j自身的target， 更多training steps只能更精确地拟合这个per-neuron target——但target本身就是次优的 （忽略joint interaction）。因此extended training让BCE-only从28.16降到25.41（降2.75）， 收益递减明显（loss curve在~2000步后plateau），而与KL的gap仍有16.21 points。 这证明KL的优势是information-theoretic的（loss function的gradient structure差异）， 不是compute-driven的，直接回应reviewer concern \\\"KL wins only because more compute\\\"。\\n\"\n  },\n  {\n    \"name\": \"SPON Reimplementation & Validation\",\n    \"description\": \"在Llama 3.1 8B上重新实现SPON（learnable per-layer bias vectors + KL training）， 在5个QA benchmarks上验证质量以确认实现正确性。\\n\",\n    \"results\": {\n      \"spon_wikitext2_ppl\": 10.82,\n      \"spon_model_sparsity\": 0.501,\n      \"spon_ppl_increase_vs_dense_pct\": 76.9,\n      \"spon_arc_c\": 51.2,\n      \"spon_arc_e\": 74.5,\n      \"spon_boolq\": 79.3,\n      \"spon_piqa\": 78.1,\n      \"spon_winogrande\": 74.8,\n      \"spon_params_bytes\": 1048576,\n      \"spon_training_time_minutes\": 12,\n      \"dense_arc_c\": 55.2,\n      \"dense_arc_e\": 79.4,\n      \"dense_boolq\": 83.1,\n      \"dense_piqa\": 81.3,\n      \"dense_winogrande\": 77.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: SPON Validation on QA Benchmarks\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Dense\",\n          \"SPON\",\n          \"Δ (abs)\"\n        ],\n        \"rows\": [\n          [\n            \"ARC-c\",\n            55.2,\n            51.2,\n            \"−4.0\"\n          ],\n          [\n            \"ARC-e\",\n            79.4,\n            74.5,\n            \"−4.9\"\n          ],\n          [\n            \"BoolQ\",\n            83.1,\n            79.3,\n            \"−3.8\"\n          ],\n          [\n            \"PIQA\",\n            81.3,\n            78.1,\n            \"−3.2\"\n          ],\n          [\n            \"WinoGrande\",\n            77.8,\n            74.8,\n            \"−3.0\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SPON实现通过QA benchmark验证，drops幅度与原论文一致（3-5 points），确认实现正确性。 PPL 10.82定位在training-free（12-13）和contextual-KL（9.2）之间，为claim 2 的additivity实验提供可靠的static correction baseline。\\n\\n\\nSPON使用input-independent的bias correction——本质上是per-layer calibration，矫正average-case 下sparsity引入的activation drift。由于是static的，它只能修正E[Δh]（期望偏移），无法处理 per-input variation Var[Δh|x]。因此SPON将PPL从training-free水平（~12-13）压到10.82， 是一个meaningful but limited的improvement。QA benchmarks上drops 3-6%符合PPL改善幅度。 SPON的主要价值不在于standalone quality，而是作为composition实验的building block—— 它修正的orthogonal component（average drift）与contextual predictor修正的component（per-input variation） 应当可加。\\n\"\n  },\n  {\n    \"name\": \"SPON + KL Predictor Composition\",\n    \"description\": \"同时应用SPON bias correction和KL contextual prediction。 测试output-space linearity（interaction residual）和per-layer orthogonality。3 seeds。\\n\",\n    \"results\": {\n      \"spon_kl_s42_ppl\": 7.95,\n      \"spon_kl_s123_ppl\": 8.12,\n      \"spon_kl_s456_ppl\": 7.88,\n      \"spon_kl_mean_ppl\": 7.98,\n      \"spon_kl_std_ppl\": 0.1,\n      \"spon_kl_model_sparsity\": 0.499,\n      \"spon_kl_ppl_increase_vs_dense_pct\": 30.4,\n      \"spon_alone_ppl_recovery\": 1.68,\n      \"kl_alone_ppl_recovery\": 3.3,\n      \"combined_ppl_recovery\": 4.52,\n      \"predicted_additive_recovery\": 4.98,\n      \"interaction_residual_pct\": 6.8,\n      \"logit_interaction_residual_l2_norm\": 0.042,\n      \"logit_spon_correction_l2_norm\": 0.38,\n      \"logit_kl_correction_l2_norm\": 0.61,\n      \"logit_interaction_ratio_pct\": 6.8,\n      \"mean_cosine_similarity_spon_kl\": 0.11,\n      \"max_cosine_similarity_spon_kl\": 0.23,\n      \"layers_with_cosine_gt_0_2\": 4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Composition Additivity Analysis\",\n        \"columns\": [\n          \"Component\",\n          \"PPL Recovery (from TEAL baseline)\",\n          \"Predicted Additive\",\n          \"Actual\",\n          \"Interaction Residual\"\n        ],\n        \"rows\": [\n          [\n            \"SPON only\",\n            1.68,\n            \"-\",\n            \"-\",\n            \"-\"\n          ],\n          [\n            \"KL only\",\n            3.3,\n            \"-\",\n            \"-\",\n            \"-\"\n          ],\n          [\n            \"SPON+KL\",\n            \"-\",\n            4.98,\n            4.52,\n            \"9.2%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5b: Per-Layer Cosine Similarity Statistics\",\n        \"columns\": [\n          \"Statistic\",\n          \"Value\"\n        ],\n        \"rows\": [\n          [\n            \"Mean cosine\",\n            0.11\n          ],\n          [\n            \"Median cosine\",\n            0.08\n          ],\n          [\n            \"Max cosine\",\n            0.23\n          ],\n          [\n            \"Layers > 0.2\",\n            \"4/32\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SPON+KL组合将PPL压到7.98（仅比dense高30%），interaction residual 6.8% < 10%阈值， per-layer cosine similarity平均0.11。c = c_s + c_θ(x)的modular decomposition experimentally validated。两种correction address不同error sources的理论预测被定量确认。\\n\\n\\nSPON修正c_s = E[Δh]（average activation drift），KL predictor修正c_θ(x) = Δh(x) - E[Δh] （per-input residual variation）。两者在correction space中近似正交——SPON的correction是 constant vector，KL的correction是zero-mean（训练过程中自然去中心化）。因此组合 c = c_s + c_θ(x)的interaction residual很小（6.8%）。PPL从KL-only的9.20进一步压到7.98， 接近dense的6.12。mean cosine similarity仅0.11，证明两种correction确实address不同的 error components。少数layers（4/32）cosine > 0.2，是因为某些layers的average drift 和per-input variation方向部分对齐（如early layers的token-independent patterns）， 但这不影响整体additivity。Claim 2（modular decomposition）直接成立。\\n\"\n  },\n  {\n    \"name\": \"Training-Free Baselines (TEAL, WINA, R-Sparse)\",\n    \"description\": \"三种training-free方法在Llama 3.1 8B @ 50% model-level sparsity下的质量。 建立三级hierarchy: training-free < static-learned < contextual-learned。\\n\",\n    \"results\": {\n      \"teal_wikitext2_ppl\": 12.48,\n      \"wina_wikitext2_ppl\": 14.76,\n      \"rsparse_wikitext2_ppl\": 13.62,\n      \"teal_model_sparsity\": 0.5,\n      \"wina_model_sparsity\": 0.5,\n      \"rsparse_model_sparsity\": 0.5,\n      \"teal_ppl_increase_vs_dense_pct\": 103.9,\n      \"wina_ppl_increase_vs_dense_pct\": 141.3,\n      \"rsparse_ppl_increase_vs_dense_pct\": 122.6\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Training-Free Baseline Comparison\",\n        \"columns\": [\n          \"Method\",\n          \"Type\",\n          \"WikiText-2 PPL\",\n          \"Δ vs Dense\"\n        ],\n        \"rows\": [\n          [\n            \"Dense\",\n            \"-\",\n            6.12,\n            \"-\"\n          ],\n          [\n            \"TEAL\",\n            \"Magnitude + greedy\",\n            12.48,\n            \"+104%\"\n          ],\n          [\n            \"R-Sparse\",\n            \"Rank-aware\",\n            13.62,\n            \"+123%\"\n          ],\n          [\n            \"WINA\",\n            \"Weight-informed\",\n            14.76,\n            \"+141%\"\n          ],\n          [\n            \"SPON\",\n            \"Static learned (KL)\",\n            10.82,\n            \"+77%\"\n          ],\n          [\n            \"KL-only\",\n            \"Contextual learned (KL)\",\n            9.2,\n            \"+50%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三级hierarchy清晰：training-free (12.5-14.8) < static-learned (10.8) < contextual-learned (9.2)。 每级提升对应information quality的提高：heuristic → average-case calibration → per-input optimization。 TEAL作为最强training-free baseline仍比KL-only差3.28 PPL points（+36%），justifies learned approach的overhead。\\n\\n\\nTEAL使用magnitude pruning + greedy per-layer allocation，在training-free中最优，因为 magnitude直接反映activation contribution。R-Sparse加入rank-aware scoring，理论上更好但 实现中的approximation引入noise，实际略逊于TEAL。WINA的weight-informed scoring虽然 考虑了weight magnitude，但在SwiGLU的gated结构下，weight和activation importance的 correlation比standard FFN更弱（gate和up projection交互），因此表现最差。 所有三种方法PPL都在12-15范围，远逊于learned methods（KL-only 9.2、SPON 10.8）， 建立clean的三级hierarchy。Training-free方法的根本限制是它们无法learn per-input neuron importance patterns，只能依赖固定heuristic。\\n\"\n  },\n  {\n    \"name\": \"Full Benchmark Suite + Latency Profiling\",\n    \"description\": \"所有conditions在WikiText-2/C4 PPL、5个discriminative tasks、wall-clock profiling上的 完整evaluation。构建efficiency-accuracy Pareto frontier。\\n\",\n    \"results\": {\n      \"dense_wikitext2_ppl\": 6.12,\n      \"teal_wikitext2_ppl\": 12.48,\n      \"wina_wikitext2_ppl\": 14.76,\n      \"rsparse_wikitext2_ppl\": 13.62,\n      \"spon_wikitext2_ppl\": 10.82,\n      \"bce_only_wikitext2_ppl\": 28.16,\n      \"bce_comp_wikitext2_ppl\": 18.64,\n      \"kl_only_wikitext2_ppl\": 9.2,\n      \"kl_comp_wikitext2_ppl\": 9.02,\n      \"spon_kl_wikitext2_ppl\": 7.98,\n      \"dense_c4_ppl\": 7.85,\n      \"teal_c4_ppl\": 15.12,\n      \"wina_c4_ppl\": 17.88,\n      \"rsparse_c4_ppl\": 16.31,\n      \"spon_c4_ppl\": 13.24,\n      \"bce_only_c4_ppl\": 33.42,\n      \"bce_comp_c4_ppl\": 22.15,\n      \"kl_only_c4_ppl\": 11.38,\n      \"kl_comp_c4_ppl\": 11.12,\n      \"spon_kl_c4_ppl\": 9.81,\n      \"dense_arc_c\": 55.2,\n      \"teal_arc_c\": 48.1,\n      \"wina_arc_c\": 46.3,\n      \"rsparse_arc_c\": 47.2,\n      \"spon_arc_c\": 51.2,\n      \"bce_comp_arc_c\": 44.8,\n      \"kl_only_arc_c\": 54.3,\n      \"spon_kl_arc_c\": 54.8,\n      \"dense_winogrande\": 77.8,\n      \"teal_winogrande\": 72.4,\n      \"wina_winogrande\": 70.8,\n      \"rsparse_winogrande\": 71.5,\n      \"spon_winogrande\": 74.8,\n      \"bce_comp_winogrande\": 68.3,\n      \"kl_only_winogrande\": 76.9,\n      \"spon_kl_winogrande\": 77.2,\n      \"dense_mmlu\": 65.8,\n      \"teal_mmlu\": 58.2,\n      \"wina_mmlu\": 56.4,\n      \"rsparse_mmlu\": 57.1,\n      \"spon_mmlu\": 60.3,\n      \"bce_comp_mmlu\": 54.9,\n      \"kl_only_mmlu\": 65.0,\n      \"spon_kl_mmlu\": 65.4,\n      \"dense_gsm8k\": 53.8,\n      \"teal_gsm8k\": 44.2,\n      \"wina_gsm8k\": 41.8,\n      \"rsparse_gsm8k\": 43.1,\n      \"spon_gsm8k\": 46.5,\n      \"bce_comp_gsm8k\": 39.7,\n      \"kl_only_gsm8k\": 52.8,\n      \"spon_kl_gsm8k\": 53.2,\n      \"dense_humaneval\": 32.9,\n      \"teal_humaneval\": 26.2,\n      \"wina_humaneval\": 24.4,\n      \"rsparse_humaneval\": 25.6,\n      \"spon_humaneval\": 28.1,\n      \"bce_comp_humaneval\": 23.8,\n      \"kl_only_humaneval\": 32.3,\n      \"spon_kl_humaneval\": 32.5,\n      \"kl_only_avg_acc_drop_pct\": 1.3,\n      \"spon_kl_avg_acc_drop_pct\": 0.7,\n      \"bce_comp_avg_acc_drop_pct\": 12.8,\n      \"dense_latency_ms\": 16.8,\n      \"teal_latency_ms\": 11.2,\n      \"spon_latency_ms\": 10.9,\n      \"bce_only_latency_ms\": 12.0,\n      \"bce_comp_latency_ms\": 13.8,\n      \"kl_only_latency_ms\": 12.0,\n      \"kl_comp_latency_ms\": 13.8,\n      \"spon_kl_latency_ms\": 12.1,\n      \"predictor_params_mb\": 24,\n      \"compensation_params_mb\": 256,\n      \"spon_params_mb\": 1,\n      \"kl_only_speedup_vs_dense_pct\": 28.6,\n      \"bce_comp_speedup_vs_dense_pct\": 17.9,\n      \"kl_only_speedup_vs_bce_comp_pct\": 13.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Comprehensive Benchmark Results (Llama 3.1 8B, 50% sparsity)\",\n        \"columns\": [\n          \"Method\",\n          \"Wiki PPL↓\",\n          \"C4 PPL↓\",\n          \"ARC-c↑\",\n          \"WinoG↑\",\n          \"MMLU↑\",\n          \"GSM8K↑\",\n          \"HumanE↑\",\n          \"Avg Δ↓\"\n        ],\n        \"rows\": [\n          [\n            \"Dense\",\n            6.12,\n            7.85,\n            55.2,\n            77.8,\n            65.8,\n            53.8,\n            32.9,\n            \"—\"\n          ],\n          [\n            \"TEAL\",\n            12.48,\n            15.12,\n            48.1,\n            72.4,\n            58.2,\n            44.2,\n            26.2,\n            \"−7.8\"\n          ],\n          [\n            \"WINA\",\n            14.76,\n            17.88,\n            46.3,\n            70.8,\n            56.4,\n            41.8,\n            24.4,\n            \"−9.9\"\n          ],\n          [\n            \"R-Sparse\",\n            13.62,\n            16.31,\n            47.2,\n            71.5,\n            57.1,\n            43.1,\n            25.6,\n            \"−8.8\"\n          ],\n          [\n            \"SPON\",\n            10.82,\n            13.24,\n            51.2,\n            74.8,\n            60.3,\n            46.5,\n            28.1,\n            \"−5.3\"\n          ],\n          [\n            \"BCE+comp\",\n            18.64,\n            22.15,\n            44.8,\n            68.3,\n            54.9,\n            39.7,\n            23.8,\n            \"−12.8\"\n          ],\n          [\n            \"KL-only\",\n            9.2,\n            11.38,\n            54.3,\n            76.9,\n            65.0,\n            52.8,\n            32.3,\n            \"−1.3\"\n          ],\n          [\n            \"SPON+KL\",\n            7.98,\n            9.81,\n            54.8,\n            77.2,\n            65.4,\n            53.2,\n            32.5,\n            \"−0.7\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8: Inference Efficiency Comparison\",\n        \"columns\": [\n          \"Method\",\n          \"Latency (ms/tok)\",\n          \"Speedup vs Dense\",\n          \"Extra Params (MB)\",\n          \"PPL\"\n        ],\n        \"rows\": [\n          [\n            \"Dense\",\n            16.8,\n            \"1.00×\",\n            0,\n            6.12\n          ],\n          [\n            \"TEAL\",\n            11.2,\n            \"1.50×\",\n            0,\n            12.48\n          ],\n          [\n            \"SPON\",\n            10.9,\n            \"1.54×\",\n            1,\n            10.82\n          ],\n          [\n            \"KL-only\",\n            12.0,\n            \"1.40×\",\n            24,\n            9.2\n          ],\n          [\n            \"BCE+comp\",\n            13.8,\n            \"1.22×\",\n            280,\n            18.64\n          ],\n          [\n            \"SPON+KL\",\n            12.1,\n            \"1.39×\",\n            25,\n            7.98\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"KL-only在quality-efficiency Pareto frontier上strictly dominates BCE+comp：更低PPL（9.20 vs 18.64）， 更低latency（12.0 vs 13.8），更少参数（24MB vs 280MB）。Downstream tasks确认PPL gains transfer：KL-only平均仅drop 1.3%（best tier阈值2%以内），BCE+comp drop 12.8%。 SPON+KL作为our best configuration达到7.98 PPL和0.7%平均drop，接近free lunch。 Taxonomy table的每个cell都有实验数据支撑。\\n\\n\\nDownstream tasks与PPL高度correlated——KL-only的低PPL (9.20)直接转化为downstream任务上 接近dense的accuracy（平均drop仅1.3%）。这是因为KL优化output distribution matching， 保留了token-level的prediction quality，而downstream tasks本质上都依赖model的next-token prediction能力。BCE+comp虽然有compensation，但其PPL (18.64)反映的distribution mismatch 在需要precise reasoning的任务上（GSM8K, HumanEval）伤害更大（drop 26-28%），因为 这些任务对error compounding更敏感。 Wall-clock方面，KL-only和BCE-only的predictor开销相同（同架构），但KL-only不需要 compensation，因此比BCE+comp省1.8ms/token（13.8→12.0）。SPON+KL仅比KL-only多0.1ms （bias add几乎免费），但PPL进一步降到7.98。KL-only在Pareto frontier上dominates BCE+comp——更快、更好、更小。\\n\"\n  },\n  {\n    \"name\": \"7-Level Sparsity Sweep — Quadratic Scaling Test\",\n    \"description\": \"在30/35/40/45/50/55/60%七个sparsity level下训练KL-only和BCE-only（各1 seed）， 测试KL-BCE delta ∝ s²的理论预测。50%复用plan_001。每个level做Taylor expansion accuracy test。\\n\",\n    \"results\": {\n      \"sparsity_levels\": [\n        0.3,\n        0.35,\n        0.4,\n        0.45,\n        0.5,\n        0.55,\n        0.6\n      ],\n      \"kl_ppls\": [\n        7.05,\n        7.42,\n        7.98,\n        8.51,\n        9.2,\n        10.82,\n        13.15\n      ],\n      \"bce_ppls\": [\n        14.55,\n        17.82,\n        19.98,\n        24.71,\n        28.2,\n        33.62,\n        42.65\n      ],\n      \"kl_bce_deltas\": [\n        7.5,\n        10.4,\n        12.0,\n        16.2,\n        19.0,\n        22.8,\n        29.5\n      ],\n      \"s2_fit_coefficient_a\": 79.2,\n      \"s2_fit_r_squared\": 0.97,\n      \"s2_plus_linear_fit_r_squared\": 0.99,\n      \"taylor_accuracy_pct\": [\n        96.8,\n        95.4,\n        94.1,\n        92.5,\n        89.8,\n        85.6,\n        80.2\n      ],\n      \"predicted_deltas_s2_only\": [\n        7.13,\n        9.7,\n        12.67,\n        16.03,\n        19.8,\n        23.96,\n        28.51\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Sparsity Sweep Results\",\n        \"columns\": [\n          \"Sparsity s\",\n          \"s²\",\n          \"KL PPL\",\n          \"BCE PPL\",\n          \"Δ (BCE−KL)\",\n          \"Predicted Δ (as²)\",\n          \"Taylor Acc %\"\n        ],\n        \"rows\": [\n          [\n            0.3,\n            0.09,\n            7.05,\n            14.55,\n            7.5,\n            7.13,\n            96.8\n          ],\n          [\n            0.35,\n            0.123,\n            7.42,\n            17.82,\n            10.4,\n            9.7,\n            95.4\n          ],\n          [\n            0.4,\n            0.16,\n            7.98,\n            19.98,\n            12.0,\n            12.67,\n            94.1\n          ],\n          [\n            0.45,\n            0.203,\n            8.51,\n            24.71,\n            16.2,\n            16.03,\n            92.5\n          ],\n          [\n            0.5,\n            0.25,\n            9.2,\n            28.2,\n            19.0,\n            19.8,\n            89.8\n          ],\n          [\n            0.55,\n            0.303,\n            10.82,\n            33.62,\n            22.8,\n            23.96,\n            85.6\n          ],\n          [\n            0.6,\n            0.36,\n            13.15,\n            42.65,\n            29.5,\n            28.51,\n            80.2\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9b: Scaling Fit Statistics\",\n        \"columns\": [\n          \"Model\",\n          \"R²\",\n          \"Parameters\"\n        ],\n        \"rows\": [\n          [\n            \"Δ = as²\",\n            0.97,\n            \"a=79.2\"\n          ],\n          [\n            \"Δ = as² + bs\",\n            0.99,\n            \"a=68.1, b=5.8\"\n          ],\n          [\n            \"Δ = as² + bs + c\",\n            0.99,\n            \"a=65.3, b=7.2, c=−0.4\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"KL-BCE delta与s²的R²=0.97，定量验证了gradient coupling theory的核心预测。 Quadratic scaling意味着在高sparsity regime（>50%），KL的优势accelerates—— 这提供了一个可检验的、非trivial的理论预测，不仅描述已有数据，也predicts extrapolation behavior。Taylor accuracy的graceful degradation pattern进一步 增强理论credibility。Claim 3直接成立。\\n\\n\\nKL的梯度dL_KL/ds_j通过Jacobian d_logits/dh耦合所有active neurons。当sparsity为s时， 每个pruned neuron的interaction涉及O(sD)个其他pruned neurons，total interaction scale为 O(s²D²)。BCE的factorized gradient完全忽略这些interactions。因此KL-BCE quality delta 应当scale as s²（leading term来自pairwise neuron interaction）。 实验数据R²=0.97证实quadratic scaling dominates。Taylor expansion在低sparsity（30-40%） 下accuracy > 94%是因为higher-order terms（s³等）negligible；在高sparsity（55-60%） accuracy降到80-86%是因为三体及更高阶interaction开始significant——这本身也是consistent with the theory（Taylor展开在远离展开点时精度下降）。 加入linear term后R²=0.99，说明residual主要是one lower-order correction。 Claim 3（quadratic scaling）定量验证通过。\\n\"\n  },\n  {\n    \"name\": \"Mistral-7B-v0.3 Cross-Architecture Validation\",\n    \"description\": \"在Mistral-7B-v0.3（GQA + sliding window attention，不同于Llama的GQA-only）上 复现KL-only vs BCE+comp comparison。Core benchmarks: WikiText-2 PPL, ARC-c, MMLU。3 seeds each。\\n\",\n    \"results\": {\n      \"mistral_dense_wikitext2_ppl\": 5.48,\n      \"mistral_dense_arc_c\": 58.1,\n      \"mistral_dense_mmlu\": 62.8,\n      \"mistral_kl_s42_ppl\": 8.12,\n      \"mistral_kl_s123_ppl\": 8.35,\n      \"mistral_kl_s456_ppl\": 8.18,\n      \"mistral_kl_mean_ppl\": 8.22,\n      \"mistral_kl_std_ppl\": 0.1,\n      \"mistral_kl_model_sparsity\": 0.498,\n      \"mistral_kl_ppl_increase_vs_dense_pct\": 50.0,\n      \"mistral_kl_arc_c\": 56.4,\n      \"mistral_kl_mmlu\": 61.3,\n      \"mistral_bce_comp_s42_ppl\": 12.81,\n      \"mistral_bce_comp_s123_ppl\": 13.24,\n      \"mistral_bce_comp_s456_ppl\": 12.53,\n      \"mistral_bce_comp_mean_ppl\": 12.86,\n      \"mistral_bce_comp_std_ppl\": 0.29,\n      \"mistral_bce_comp_model_sparsity\": 0.497,\n      \"mistral_bce_comp_arc_c\": 50.8,\n      \"mistral_bce_comp_mmlu\": 55.9,\n      \"mistral_kl_vs_bce_comp_ppl_gap\": 4.64,\n      \"mistral_kl_vs_bce_comp_ppl_gap_pct\": 36.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Mistral-7B-v0.3 Cross-Architecture Validation\",\n        \"columns\": [\n          \"Condition\",\n          \"Wiki PPL↓\",\n          \"ARC-c↑\",\n          \"MMLU↑\"\n        ],\n        \"rows\": [\n          [\n            \"Dense\",\n            5.48,\n            58.1,\n            62.8\n          ],\n          [\n            \"KL-only\",\n            \"8.22±0.10\",\n            56.4,\n            61.3\n          ],\n          [\n            \"BCE+comp\",\n            \"12.86±0.29\",\n            50.8,\n            55.9\n          ],\n          [\n            \"Gap (KL vs BCE+comp)\",\n            \"−4.64\",\n            \"+5.6\",\n            \"+5.4\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 10b: Cross-Architecture Consistency\",\n        \"columns\": [\n          \"Metric\",\n          \"Llama 3.1 8B\",\n          \"Mistral-7B-v0.3\"\n        ],\n        \"rows\": [\n          [\n            \"KL PPL increase vs dense\",\n            \"50.3%\",\n            \"50.0%\"\n          ],\n          [\n            \"KL vs BCE+comp gap (PPL)\",\n            9.44,\n            4.64\n          ],\n          [\n            \"KL vs BCE+comp gap (%)\",\n            \"50.6%\",\n            \"36.1%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Mistral-7B-v0.3成功复现KL dominance：KL-only (8.22) vs BCE+comp (12.86)，gap 36%。 KL PPL increase vs dense（50%）与Llama（50.3%）惊人一致，证明KL的优势是loss function 的universal property而非architecture-specific artifact。排除reviewer concern \\\"Single model / limited generalization\\\"。\\n\\n\\nMistral-7B-v0.3使用GQA + sliding window attention，SwiGLU FFN结构与Llama相同但 attention pattern不同，导致不同的activation sparsity distribution。KL的gradient coupling property是loss function的数学性质，与architecture无关——只要model有SwiGLU FFN且sparsity 在hidden states上操作，KL就能捕获joint interactions。因此KL优势在Mistral上同方向复现。 PPL increase 50%（vs Llama的50.3%）高度一致。Gap绝对值（4.64 vs 9.44）较小是因为 Mistral的dense PPL更低（5.48 vs 6.12），两个model的relative gap pattern一致。 Sliding window attention可能使某些layers的neuron importance更localized，略微 降低BCE+comp的absolute PPL（12.86 vs Llama的18.64），但不改变KL dominance。\\n\"\n  },\n  {\n    \"name\": \"LongBench Long-Context Evaluation\",\n    \"description\": \"LongBench English subset（4K-32K tokens），所有conditions。 Per-task-type breakdown: single-doc QA, multi-doc QA, summarization, few-shot, code。\\n\",\n    \"results\": {\n      \"dense_longbench_avg\": 43.5,\n      \"teal_longbench_avg\": 35.4,\n      \"wina_longbench_avg\": 33.8,\n      \"rsparse_longbench_avg\": 34.6,\n      \"spon_longbench_avg\": 39.8,\n      \"bce_comp_longbench_avg\": 32.1,\n      \"kl_only_longbench_avg\": 42.1,\n      \"spon_kl_longbench_avg\": 42.8,\n      \"kl_single_doc_qa\": 44.8,\n      \"kl_multi_doc_qa\": 38.2,\n      \"kl_summarization\": 42.5,\n      \"kl_few_shot\": 47.1,\n      \"kl_code\": 38.0,\n      \"bce_comp_single_doc_qa\": 35.2,\n      \"bce_comp_multi_doc_qa\": 28.4,\n      \"bce_comp_summarization\": 33.8,\n      \"bce_comp_few_shot\": 34.6,\n      \"bce_comp_code\": 28.5,\n      \"dense_single_doc_qa\": 46.2,\n      \"dense_multi_doc_qa\": 39.5,\n      \"dense_summarization\": 43.8,\n      \"dense_few_shot\": 48.3,\n      \"dense_code\": 39.6,\n      \"kl_only_avg_drop_vs_dense\": 1.4,\n      \"bce_comp_avg_drop_vs_dense\": 11.4,\n      \"kl_worst_task_type\": \"multi-doc QA\",\n      \"kl_worst_task_drop\": 3.3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: LongBench Per-Task-Type Breakdown\",\n        \"columns\": [\n          \"Task Type\",\n          \"Dense\",\n          \"TEAL\",\n          \"SPON\",\n          \"BCE+comp\",\n          \"KL-only\",\n          \"SPON+KL\"\n        ],\n        \"rows\": [\n          [\n            \"Single-doc QA\",\n            46.2,\n            38.1,\n            42.0,\n            35.2,\n            44.8,\n            45.3\n          ],\n          [\n            \"Multi-doc QA\",\n            39.5,\n            31.2,\n            36.1,\n            28.4,\n            38.2,\n            38.8\n          ],\n          [\n            \"Summarization\",\n            43.8,\n            35.8,\n            40.2,\n            33.8,\n            42.5,\n            43.1\n          ],\n          [\n            \"Few-shot\",\n            48.3,\n            39.5,\n            44.3,\n            34.6,\n            47.1,\n            47.8\n          ],\n          [\n            \"Code\",\n            39.6,\n            32.4,\n            36.5,\n            28.5,\n            38.0,\n            38.9\n          ],\n          [\n            \"**Average**\",\n            \"**43.5**\",\n            \"**35.4**\",\n            \"**39.8**\",\n            \"**32.1**\",\n            \"**42.1**\",\n            \"**42.8**\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LongBench结果证明KL predictor在长序列（4K-32K）下generalization良好（avg drop 1.4）， 无需长序列finetune。BCE+comp在long-context下进一步恶化（avg drop 11.4 vs short-context的12.8%）， 可能因为compensation网络对error accumulation的correction在长序列下saturate。 增强了EMNLP venue fit（NLP-specific long-context evaluation）。\\n\\n\\n长序列evaluation测试predictor是否generalize beyond短训练序列。KL的output-distribution matching objective在长序列下仍然有效，因为它不依赖specific sequence length——predictor 看到的是per-token hidden states，length主要影响attention pattern。KL-only的drop（1.4 avg） 与short-context evaluation一致。Multi-doc QA是最challenging的任务类型（需要cross-document reasoning），因此KL-only在此处drop最大（3.3 points）。BCE+comp在长序列下degradation 更严重（11.4 avg drop）——因为BCE的per-neuron error在长序列中accumulates without compensation fully correcting the compounding effect。SPON+KL以42.8接近dense的43.5， 进一步确认composition在长序列下仍然有效。\\n\"\n  },\n  {\n    \"name\": \"MT-Bench Multi-Turn Instruction Following\",\n    \"description\": \"MT-Bench 80题 × 8 categories，GPT-4o judge。测试sparsity对instruction following quality的影响。\\n\",\n    \"results\": {\n      \"dense_mtbench_avg\": 7.21,\n      \"teal_mtbench_avg\": 6.18,\n      \"spon_mtbench_avg\": 6.78,\n      \"bce_comp_mtbench_avg\": 6.42,\n      \"kl_only_mtbench_avg\": 7.05,\n      \"spon_kl_mtbench_avg\": 7.12,\n      \"kl_writing\": 7.35,\n      \"kl_roleplay\": 7.15,\n      \"kl_reasoning\": 6.65,\n      \"kl_math\": 6.55,\n      \"kl_coding\": 6.85,\n      \"kl_extraction\": 7.45,\n      \"kl_stem\": 7.1,\n      \"kl_humanities\": 7.3,\n      \"bce_comp_writing\": 6.8,\n      \"bce_comp_reasoning\": 5.85,\n      \"bce_comp_math\": 5.65,\n      \"bce_comp_coding\": 5.9\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: MT-Bench Results\",\n        \"columns\": [\n          \"Method\",\n          \"Avg Score\",\n          \"Writing\",\n          \"Reasoning\",\n          \"Math\",\n          \"Coding\"\n        ],\n        \"rows\": [\n          [\n            \"Dense\",\n            7.21,\n            7.5,\n            6.85,\n            6.8,\n            7.1\n          ],\n          [\n            \"TEAL\",\n            6.18,\n            6.45,\n            5.6,\n            5.4,\n            5.8\n          ],\n          [\n            \"SPON\",\n            6.78,\n            7.1,\n            6.35,\n            6.15,\n            6.55\n          ],\n          [\n            \"BCE+comp\",\n            6.42,\n            6.8,\n            5.85,\n            5.65,\n            5.9\n          ],\n          [\n            \"KL-only\",\n            7.05,\n            7.35,\n            6.65,\n            6.55,\n            6.85\n          ],\n          [\n            \"SPON+KL\",\n            7.12,\n            7.4,\n            6.75,\n            6.65,\n            6.95\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MT-Bench进一步确认KL-only在generation quality上接近dense。GPT-4o judge评分差异 KL-only vs dense仅0.16——在judge的noise floor以内。BCE+comp在math/reasoning上 severe degradation（-1.15/-1.00 vs dense），而KL-only仅-0.25/-0.20。 Strengthens EMNLP NLP evaluation story。\\n\\n\\nMT-Bench测试multi-turn instruction following——一个对output quality高度敏感的setting。 KL-only（7.05）与dense（7.21）差距仅0.16（GPT-4o judge的scoring granularity内）， 说明KL的output distribution matching直接保留了instruction following能力。 Math和reasoning categories drop略大（KL-only 6.55/6.65 vs dense ~6.8/6.85），因为 这些tasks需要precise multi-step reasoning，对任何distribution shift更敏感。 BCE+comp（6.42）在reasoning-heavy categories下degradation严重（5.85/5.65），因为 BCE的imprecise sparsity mask在需要所有neurons correctly participate的reasoning chain上 产生compounding errors，compensation无法fully recover。\\n\"\n  },\n  {\n    \"name\": \"RULER Synthetic Long-Context Diagnostics\",\n    \"description\": \"RULER synthetic evaluation at 4K and 16K context，3 representative task types (needle-in-a-haystack, multi-key retrieval, variable tracking)。 Fine-grained diagnostics complementing LongBench。\\n\",\n    \"results\": {\n      \"dense_ruler_4k_avg\": 95.2,\n      \"kl_only_ruler_4k_avg\": 93.8,\n      \"bce_comp_ruler_4k_avg\": 87.4,\n      \"spon_kl_ruler_4k_avg\": 94.5,\n      \"dense_ruler_16k_avg\": 88.5,\n      \"kl_only_ruler_16k_avg\": 86.1,\n      \"bce_comp_ruler_16k_avg\": 78.3,\n      \"spon_kl_ruler_16k_avg\": 87.2,\n      \"kl_needle_4k\": 98.0,\n      \"kl_needle_16k\": 94.5,\n      \"kl_multikey_4k\": 91.2,\n      \"kl_multikey_16k\": 82.4,\n      \"kl_vartrack_4k\": 92.1,\n      \"kl_vartrack_16k\": 81.3,\n      \"bce_comp_needle_4k\": 94.5,\n      \"bce_comp_needle_16k\": 86.2,\n      \"bce_comp_multikey_4k\": 83.8,\n      \"bce_comp_multikey_16k\": 72.1,\n      \"bce_comp_vartrack_4k\": 83.9,\n      \"bce_comp_vartrack_16k\": 76.5,\n      \"kl_only_4k_to_16k_drop\": 7.7,\n      \"bce_comp_4k_to_16k_drop\": 9.1,\n      \"dense_4k_to_16k_drop\": 6.7\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: RULER Synthetic Evaluation\",\n        \"columns\": [\n          \"Task\",\n          \"Context\",\n          \"Dense\",\n          \"KL-only\",\n          \"BCE+comp\",\n          \"SPON+KL\"\n        ],\n        \"rows\": [\n          [\n            \"Needle\",\n            \"4K\",\n            99.2,\n            98.0,\n            94.5,\n            98.5\n          ],\n          [\n            \"Needle\",\n            \"16K\",\n            96.8,\n            94.5,\n            86.2,\n            95.8\n          ],\n          [\n            \"Multi-key\",\n            \"4K\",\n            93.5,\n            91.2,\n            83.8,\n            92.4\n          ],\n          [\n            \"Multi-key\",\n            \"16K\",\n            84.1,\n            82.4,\n            72.1,\n            83.5\n          ],\n          [\n            \"Var-track\",\n            \"4K\",\n            92.8,\n            92.1,\n            83.9,\n            92.5\n          ],\n          [\n            \"Var-track\",\n            \"16K\",\n            84.5,\n            81.3,\n            76.5,\n            83.2\n          ],\n          [\n            \"**Average**\",\n            \"**4K**\",\n            \"**95.2**\",\n            \"**93.8**\",\n            \"**87.4**\",\n            \"**94.5**\"\n          ],\n          [\n            \"**Average**\",\n            \"**16K**\",\n            \"**88.5**\",\n            \"**86.1**\",\n            \"**78.3**\",\n            \"**87.2**\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RULER诊断补充LongBench：KL-only的context-length degradation pattern与dense一致 (4K→16K drop差仅1 point)，而BCE+comp多drop 2.4 points。Multi-key retrieval 是differentiation最大的task（KL 82.4 vs BCE+comp 72.1 at 16K），这与理论一致—— multi-key需要FFN准确处理多个simultaneously relevant positions，joint neuron interaction quality直接影响结果。\\n\\nRULER的synthetic tasks提供controlled diagnostics——每个task isolate一种capability (retrieval precision, multi-hop tracking等)。KL-only在4K下接近dense（93.8 vs 95.2）， 在16K下gracefully degrade（86.1 vs 88.5）——4K→16K drop (7.7)接近dense pattern (6.7)， 说明KL predictor不会随context length引入额外的degradation。BCE+comp的4K→16K drop更大 (9.1)，在multi-key retrieval（需要同时attend to多个scattered positions）和variable tracking（需要maintain state across distance）上degradation尤其严重——因为这些tasks 对sparse mask quality最敏感，BCE的imprecise masks在长距离dependency上compounding。 Needle-in-a-haystack是最简单的task（单点retrieval），所有methods都表现好。\\n\"\n  }\n]",
      "numLines": 1219,
      "startLine": 1,
      "totalLines": 1219
    }
  },
  "sourceToolAssistantUUID": "c3d6e483-48d6-4f3c-8eb0-b72b58ceec95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T17:26:07.728Z_

<details><summary>↩ Tool result · `toolu_01HopPv58Adhiird95AxQP8D`</summary>

```text
1	# Paper Framing — distill_sparse_swiglu
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 2026 cycle)
5	- Deadline: 2026-05-25 (ARR submission)
6	- Track: Efficient Methods for NLP
7	
8	## Core Claims
9	
10	1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating ~256MB of inference-time compensation weights and per-layer GEMV overhead. (Headline claim)
11	
12	2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.
13	
14	3. **KL advantage scales quadratically with sparsity**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). Testable prediction: KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.
15	
16	## Story Spine
17	
18	- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).
19	
20	- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.
21	
22	- **Our framing / headline question**: "Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.
23	
24	- **Headline result template**: "On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] — demonstrating that output-distribution distillation subsumes error compensation and enabling a simpler, lighter inference pipeline."
25	
26	## Two-Dimensional Taxonomy (Conceptual Contribution)
27	
28	|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |
29	|--------------------------|:-----------------:|:-------------------:|:-------------:|
30	| Static                   | —                 | —                   | SPON          |
31	| Per-layer                | —                 | ShadowLLM           | —             |
32	| Per-token contextual     | FastForward       | —                   | **Ours**      |
33	
34	Positions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.
35	
36	## Anticipated Reviewer Concerns
37	
38	1. **"Incremental / no new algorithm"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.
39	
40	2. **"KL wins only because more compute"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.
41	
42	3. **"Gumbel-sigmoid relaxation, not KL, explains gains"**: Addressed by STE baseline (plan_002) isolating loss function contribution.
43	
44	4. **"Single model / limited generalization"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).
45	
46	5. **"Effect size may not hold on downstream tasks"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.
47	
48	## Venue Fit
49	- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation
50	- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue
51	- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c0b4861-4c95-4ba6-a891-6eae173e30f3",
  "isSidechain": false,
  "promptId": "4324b22a-92db-42ef-a974-2006388d7cce",
  "type": "user",
  "uuid": "835f3f15-805f-4e24-9c7a-1eaceab59925",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper_framing.md",
      "content": "# Paper Framing — distill_sparse_swiglu\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\n- Deadline: 2026-05-25 (ARR submission)\n- Track: Efficient Methods for NLP\n\n## Core Claims\n\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating ~256MB of inference-time compensation weights and per-layer GEMV overhead. (Headline claim)\n\n2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.\n\n3. **KL advantage scales quadratically with sparsity**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). Testable prediction: KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.\n\n## Story Spine\n\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\n\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.\n\n- **Our framing / headline question**: \"Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?\" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.\n\n- **Headline result template**: \"On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] — demonstrating that output-distribution distillation subsumes error compensation and enabling a simpler, lighter inference pipeline.\"\n\n## Two-Dimensional Taxonomy (Conceptual Contribution)\n\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\n| Static                   | —                 | —                   | SPON          |\n| Per-layer                | —                 | ShadowLLM           | —             |\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\n\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Incremental / no new algorithm\"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.\n\n2. **\"KL wins only because more compute\"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.\n\n3. **\"Gumbel-sigmoid relaxation, not KL, explains gains\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\n\n4. **\"Single model / limited generalization\"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).\n\n5. **\"Effect size may not hold on downstream tasks\"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.\n\n## Venue Fit\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\n- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  },
  "sourceToolAssistantUUID": "7c0b4861-4c95-4ba6-a891-6eae173e30f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T17:26:07.722Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HopPv58Adhiird95AxQP8D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d01a10c7-ab9b-4b01-815d-4faec0bfa629",
  "isSidechain": false,
  "requestId": "req_011Cb4kDUS6i8qgN9Jzs3ieC",
  "type": "assistant",
  "uuid": "7c0b4861-4c95-4ba6-a891-6eae173e30f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PeJUX3e7uQhLzqcJtgB4cL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11188,
      "cache_read_input_tokens": 11841,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11188,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11188
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_sw…",
  "leafUuid": "835f3f15-805f-4e24-9c7a-1eaceab59925",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate distillation sparse SwiGLU research paper",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb"
}
```

---

### Assistant

_source line 14 · 2026-05-15T17:26:15.827Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me write the full LaTeX paper. I need to cover all 11 experiments in the data, organized into proper sections. Let me plan the structure:

1. Abstract
2. Introduction
3. Related Work
4. Method
   - Problem Setup
   - Gradient Coupling Analysis (KL vs BCE)
   - Modular Decomposition Framework
5. Experiments
   - Setup
   - Four-Condition Ablation (Exp 1, Table 1)
   - STE Baseline (Exp 2, Table 2)
   - Iso-Compute Comparison (Exp 3, Table 3)
   - Training-Free Baselines (Exp 6, Table 6)
   - SPON Validation (Exp 4, Table 4)
   - SPON + KL Composition (Exp 5, Tables 5, 5b)
   - Full Benchmark Suite (Exp 7, Tables 7, 8)
   - Sparsity Sweep (Exp 8, Tables 9, 9b)
   - Cross-Architecture Validation (Exp 9, Tables 10, 11)
   - LongBench (Exp 10, Table 12)
   - MT-Bench (Exp 11, Table 13)
   - RULER (Exp 12, Table 14)

Now I'm ready to write out the full paper with all these experimental results and validation studies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "835f3f15-805f-4e24-9c7a-1eaceab59925",
  "isSidechain": false,
  "requestId": "req_011Cb4kDjjMUc4KZZTL4N8GJ",
  "type": "assistant",
  "uuid": "9da82549-f06b-43c3-a183-bb7999fe7ba9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rxh1VYyfXmAjTmMJub3KJP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19715,
      "cache_read_input_tokens": 23029,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 488,
          "cache_read_input_tokens": 23029,
          "cache_creation_input_tokens": 19715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19715
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

_source line 15 · 2026-05-15T17:26:15.838Z_

Now I'll write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9da82549-f06b-43c3-a183-bb7999fe7ba9",
  "isSidechain": false,
  "requestId": "req_011Cb4kDjjMUc4KZZTL4N8GJ",
  "type": "assistant",
  "uuid": "5f734e34-df63-4729-a7b0-281315fdb1c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rxh1VYyfXmAjTmMJub3KJP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19715,
      "cache_read_input_tokens": 23029,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 488,
          "cache_read_input_tokens": 23029,
          "cache_creation_input_tokens": 19715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19715
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

_source line 16 · 2026-05-15T17:26:17.252Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EC6YTJpT9Y26r5udvYkFz8`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f734e34-df63-4729-a7b0-281315fdb1c6",
  "isSidechain": false,
  "requestId": "req_011Cb4kDjjMUc4KZZTL4N8GJ",
  "type": "assistant",
  "uuid": "a8e8b622-2c56-4364-83fd-3eb10507b5af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rxh1VYyfXmAjTmMJub3KJP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19715,
      "cache_read_input_tokens": 23029,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 488,
          "cache_read_input_tokens": 23029,
          "cache_creation_input_tokens": 19715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19715
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

_source line 17 · 2026-05-15T17:26:17.487Z_

<details><summary>↩ Tool result · `toolu_01EC6YTJpT9Y26r5udvYkFz8`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8e8b622-2c56-4364-83fd-3eb10507b5af",
  "isSidechain": false,
  "promptId": "4324b22a-92db-42ef-a974-2006388d7cce",
  "type": "user",
  "uuid": "d100d5b3-4778-403c-9d54-12a8e1ed5a02",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "a8e8b622-2c56-4364-83fd-3eb10507b5af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T17:29:54.614Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Ls3c6RLfrE5oF368qCLDGZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{array}\n\\usepackage{xcolor}\n\n\\title{Output-Distribution Distillation Makes Compensation Networks Obsolete\\\\for SwiGLU Activation Sparsity}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nActivation sparsity in SwiGLU-based large language models enables significant inference speedups by dynamically pruning neurons, but existing learned approaches (e.g., FastForward) train per-neuron binary predictors with BCE loss and require auxiliary compensation networks ($\\sim$256\\,MB) to recover quality---adding latency and memory overhead.\nWe show that replacing BCE with KL-divergence distillation on the output distribution \\emph{eliminates the need for compensation entirely}.\nOn Llama~3.1~8B at 50\\% model-level sparsity, a KL-trained contextual predictor without compensation achieves 9.20 perplexity on WikiText-2 (within 50\\% of the dense 6.12 baseline), while BCE with compensation reaches only 18.64---a gap of 9.44 PPL points.\nThe advantage stems from KL's gradient structure, which couples all active neurons through the output Jacobian, capturing joint interaction effects that BCE's factorized per-neuron gradient misses.\nWe formalize a modular decomposition $\\mathbf{c} = \\mathbf{c}_s + \\mathbf{c}_\\theta(\\mathbf{x})$ combining SPON's static bias correction with KL contextual prediction, achieving 7.98 PPL with only 6.8\\% interaction residual.\nA seven-level sparsity sweep confirms the theoretically predicted quadratic scaling of the KL--BCE quality gap ($R^2 = 0.97$).\nCross-architecture validation on Mistral-7B-v0.3, comprehensive downstream benchmarks (MMLU, GSM8K, HumanEval, LongBench, MT-Bench, RULER), and latency profiling demonstrate that KL-only Pareto-dominates BCE+compensation: better quality, lower latency (12.0 vs.\\ 13.8\\,ms/token), and 10$\\times$ fewer additional parameters (24\\,MB vs.\\ 280\\,MB).\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nSwiGLU feed-forward networks~\\cite{shazeer2020glu} in modern LLMs exhibit substantial contextual activation sparsity: at any given input, a large fraction of intermediate neurons contribute negligibly to the output.\nExploiting this sparsity at inference time by dynamically skipping inactive neurons can yield wall-clock speedups of $1.3$--$1.5\\times$, a practically significant reduction for latency-sensitive deployment.\n\nThree tiers of approaches have emerged.\n\\emph{Training-free} methods (TEAL, WINA, R-Sparse) apply static heuristics---magnitude thresholds, weight-informed scores---to select neurons.\nWhile requiring no training, these methods incur a 6--9 PPL point gap at 50\\% sparsity on Llama~3.1~8B.\n\\emph{Static learned} approaches such as SPON learn input-independent per-layer bias corrections via KL distillation, recovering average-case activation drift but unable to adapt to per-input variation.\n\\emph{Contextual learned} methods, exemplified by FastForward, train a lightweight MLP to predict per-token neuron importance.\nHowever, FastForward uses binary cross-entropy (BCE) to train this predictor independently per neuron, then attaches a compensation network to correct the residual error---adding $\\sim$256\\,MB of parameters and a per-layer GEMV at inference time.\n\nWe ask: \\emph{does the compensation network compensate for a fundamental limitation of the predictor, or for a limitation of the training objective?}\nThe answer hinges on gradient structure.\nThe BCE gradient $\\partial\\mathcal{L}_{\\mathrm{BCE}}/\\partial s_j = (\\sigma(s_j) - t_j)\\sigma'(s_j)$ depends only on neuron $j$'s own target, factorizing across neurons.\nIn contrast, the KL gradient $\\partial\\mathcal{L}_{\\mathrm{KL}}/\\partial s_j$ propagates through the full Jacobian $\\partial\\mathbf{z}/\\partial\\mathbf{h} \\cdot \\partial\\mathbf{h}/\\partial\\mathbf{m}$, coupling all active neurons.\nThis coupling captures joint interaction effects that scale as $O(s^2 D^2)$ with sparsity level $s$ and hidden dimension $D$---precisely the effects that compensation networks attempt to correct post hoc.\n\nOur contributions:\n\\begin{enumerate}\n    \\item We demonstrate that KL-trained contextual sparsity predictors categorically dominate BCE+compensation: 9.20 vs.\\ 18.64 PPL on Llama~3.1~8B at 50\\% sparsity, with lower latency and 10$\\times$ fewer parameters (\\S\\ref{sec:ablation}, \\S\\ref{sec:fullbench}).\n    \\item We formalize a modular decomposition $\\mathbf{c} = \\mathbf{c}_s + \\mathbf{c}_\\theta(\\mathbf{x})$ combining static (SPON) and contextual (KL) corrections, achieving 7.98 PPL with near-additive composition (6.8\\% interaction residual; \\S\\ref{sec:composition}).\n    \\item We provide a testable theoretical prediction---the KL--BCE quality gap scales quadratically with sparsity---and confirm it empirically ($R^2 = 0.97$ across seven sparsity levels; \\S\\ref{sec:scaling}).\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Training-free activation sparsity.}\nTEAL~\\cite{liu2024teal} uses magnitude-based thresholding with greedy per-layer budget allocation.\nWINA~\\cite{shen2024wina} incorporates weight magnitudes into the scoring criterion.\nR-Sparse~\\cite{zhang2024rsparse} introduces rank-aware scoring.\nAll three operate without any parameter training but suffer quality gaps of 6--9 PPL points at 50\\% sparsity.\n\n\\paragraph{Learned sparsity prediction.}\nFastForward~\\cite{wang2024fastforward} trains a small MLP per layer to predict binary neuron masks using BCE, then adds a compensation MLP to correct residual errors.\nSPON~\\cite{zhou2024spon} takes a different approach: learning input-independent per-layer bias vectors via KL distillation of the teacher's output distribution.\nShadowLLM~\\cite{chen2024shadowllm} uses MSE on intermediate representations for per-layer correction.\n\n\\paragraph{Knowledge distillation for sparsity.}\nOutput-distribution matching via KL divergence is standard in knowledge distillation~\\cite{hinton2015distilling} but has not been applied to train \\emph{contextual} sparsity predictors.\nThe key distinction is that we distill the \\emph{sparsity decision} (which neurons to activate) rather than the model weights, and the KL gradient structure provides a principled advantage over per-neuron objectives.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\nConsider a SwiGLU FFN layer with gate projection $\\mathbf{g} = \\sigma_{\\mathrm{SiLU}}(\\mathbf{W}_g \\mathbf{x})$, up projection $\\mathbf{u} = \\mathbf{W}_u \\mathbf{x}$, and element-wise product $\\mathbf{h} = \\mathbf{g} \\odot \\mathbf{u}$.\nA binary mask $\\mathbf{m} \\in \\{0,1\\}^D$ selects a subset of neurons, yielding sparse output $\\mathbf{y}_{\\mathrm{sparse}} = \\mathbf{W}_d (\\mathbf{m} \\odot \\mathbf{h})$.\nWe seek a predictor $f_\\theta(\\mathbf{x}): \\mathbb{R}^{d} \\to [0,1]^D$ that produces soft scores, relaxed to masks via Gumbel-sigmoid sampling during training and hard thresholding at inference.\n\n\\subsection{Gradient Coupling: KL vs.\\ BCE}\n\n\\paragraph{BCE objective.}\nGiven oracle mask $\\mathbf{t}$ (e.g., top-$k$ by activation magnitude), the BCE loss is:\n\\begin{equation}\n\\mathcal{L}_{\\mathrm{BCE}} = -\\sum_{j=1}^{D} \\big[ t_j \\log \\sigma(s_j) + (1-t_j)\\log(1-\\sigma(s_j)) \\big]\n\\end{equation}\nwhere $s_j = f_\\theta(\\mathbf{x})_j$.\nThe gradient $\\partial\\mathcal{L}_{\\mathrm{BCE}}/\\partial s_j = \\sigma(s_j) - t_j$ depends only on neuron $j$---the loss \\emph{factorizes} across neurons.\n\n\\paragraph{KL objective.}\nWe instead minimize the KL divergence between the dense and sparse model output distributions:\n\\begin{equation}\n\\mathcal{L}_{\\mathrm{KL}} = \\mathrm{KL}\\!\\left(p_{\\mathrm{dense}}(\\cdot|\\mathbf{x}) \\;\\|\\; p_{\\mathrm{sparse}}(\\cdot|\\mathbf{x}, \\mathbf{m})\\right)\n\\end{equation}\nThe gradient with respect to score $s_j$ is:\n\\begin{equation}\n\\frac{\\partial\\mathcal{L}_{\\mathrm{KL}}}{\\partial s_j} = \\underbrace{\\frac{\\partial\\mathcal{L}_{\\mathrm{KL}}}{\\partial \\mathbf{z}}}_{\\text{output error}} \\cdot \\underbrace{\\frac{\\partial \\mathbf{z}}{\\partial \\mathbf{h}}}_{\\text{down proj}} \\cdot \\underbrace{\\frac{\\partial \\mathbf{h}}{\\partial m_j}}_{\\text{neuron }j} \\cdot \\frac{\\partial m_j}{\\partial s_j}\n\\end{equation}\nCritically, $\\partial\\mathbf{z}/\\partial\\mathbf{h} = \\mathbf{W}_d$ and $\\partial\\mathcal{L}_{\\mathrm{KL}}/\\partial\\mathbf{z}$ depend on the \\emph{full} sparse output, which in turn depends on \\emph{all} active neurons.\nThus the gradient for neuron $j$ is \\emph{coupled} to all other neurons' mask decisions through the shared output space.\n\n\\paragraph{Quadratic scaling prediction.}\nWhen sparsity is $s$, each pruned neuron interacts with $O(sD)$ other pruned neurons.\nThe total pairwise interaction effects scale as $O(s^2 D^2)$.\nBCE's factorized gradient ignores all such interactions, while KL captures them through the Jacobian.\nThis yields the testable prediction that the KL--BCE quality gap $\\Delta(s) \\approx a s^2$ for some constant $a$.\n\n\\subsection{Modular Decomposition}\n\\label{sec:decomposition}\n\nWe decompose the total correction to the sparse hidden states as:\n\\begin{equation}\n\\mathbf{c} = \\mathbf{c}_s + \\mathbf{c}_\\theta(\\mathbf{x})\n\\end{equation}\nwhere $\\mathbf{c}_s = \\mathbb{E}[\\Delta\\mathbf{h}]$ is the static, input-independent bias correction (as in SPON), and $\\mathbf{c}_\\theta(\\mathbf{x}) = \\Delta\\mathbf{h}(\\mathbf{x}) - \\mathbb{E}[\\Delta\\mathbf{h}]$ is the per-input residual variation captured by the KL contextual predictor.\nSince $\\mathbf{c}_s$ is constant and $\\mathbf{c}_\\theta(\\mathbf{x})$ is zero-mean by construction, the two corrections are approximately orthogonal.\nWe measure the interaction residual as:\n\\begin{equation}\n\\rho = \\frac{\\|\\mathbf{c} - (\\mathbf{c}_s + \\mathbf{c}_\\theta(\\mathbf{x}))\\|_2}{\\|\\mathbf{c}_s\\|_2 + \\|\\mathbf{c}_\\theta(\\mathbf{x})\\|_2}\n\\end{equation}\nand predict $\\rho \\ll 1$ when SPON and the KL predictor address different error components.\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Models.}\nWe evaluate on Llama~3.1~8B (primary) and Mistral-7B-v0.3 (cross-architecture validation).\nBoth use SwiGLU FFN layers with intermediate dimension $D = 14336$ (Llama) and $D = 14336$ (Mistral).\n\n\\paragraph{Sparsity target.}\nUnless otherwise noted, we target 50\\% model-level sparsity with per-layer budget allocation following TEAL's greedy algorithm.\n\n\\paragraph{Training.}\nKL and BCE predictors share identical architecture (2-layer MLP, $\\sim$24\\,MB per model).\nTraining uses 1000 steps on a 10M-token calibration subset of C4.\nGumbel-sigmoid relaxation ($\\tau = 1.0 \\to 0.1$ cosine anneal) enables gradient flow through discrete masks during training; hard thresholds are used at inference.\nWe report WikiText-2 perplexity as the primary metric.\n\n\\paragraph{Baselines.}\nWe compare against: (1)~Dense (no sparsity), (2)~TEAL, WINA, R-Sparse (training-free), (3)~SPON (static learned), (4)~BCE-only, BCE+compensation (contextual learned, FastForward-style), and (5)~our KL-only, KL+compensation, and SPON+KL variants.\n\n% ------------------------------------------------------------\n\\subsection{Four-Condition Ablation}\n\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} presents the core ablation at 50\\% sparsity on Llama~3.1~8B.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Four-condition ablation on WikiText-2 (Llama~3.1~8B, 50\\% sparsity). KL-only outperforms BCE+compensation by 9.44 PPL points without any compensation network.}\n\\label{tab:ablation}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Seeds} & \\textbf{PPL} & \\textbf{$\\Delta$ Dense} & \\textbf{Comp.\\ Benefit} \\\\\n\\midrule\nDense & -- & 6.12 & -- & -- \\\\\nBCE-only & 3 & 28.16\\small{$\\pm$0.17} & +360\\% & -- \\\\\nBCE+comp & 5 & 18.64\\small{$\\pm$0.33} & +205\\% & $-$9.52 \\\\\nKL-only & 5 & 9.20\\small{$\\pm$0.04} & +50\\% & -- \\\\\nKL+comp & 3 & 9.02\\small{$\\pm$0.07} & +47\\% & $-$0.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only achieves 9.20$\\pm$0.04 PPL, surpassing BCE+compensation (18.64$\\pm$0.33) by 9.44 points.\nAdding compensation to KL yields only 0.18 PPL improvement (9.02 vs.\\ 9.20), compared to 9.52 for BCE.\nThe extremely low standard deviation across 5 seeds (0.04) confirms high reproducibility.\nThe compensation network is made redundant by KL's gradient coupling---it corrects at training time what compensation would correct at inference time.\n\n% ------------------------------------------------------------\n\\subsection{Isolating Loss vs.\\ Relaxation (STE Baseline)}\n\\label{sec:ste}\n\nA natural concern is whether the advantage comes from the KL loss function or from Gumbel-sigmoid relaxation.\nWe replace Gumbel-sigmoid with Straight-Through Estimation (STE) while keeping KL loss, shown in Table~\\ref{tab:ste}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Relaxation method ablation. STE+KL still dominates Gumbel+BCE, confirming the loss function drives $>$97\\% of the advantage.}\n\\label{tab:ste}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Relaxation} & \\textbf{Loss} & \\textbf{PPL} \\\\\n\\midrule\nGumbel+KL (ours) & Gumbel-sigmoid & KL & 9.20\\small{$\\pm$0.04} \\\\\nSTE+KL & Straight-Through & KL & 9.74\\small{$\\pm$0.09} \\\\\nGumbel+BCE & Gumbel-sigmoid & BCE & 28.16\\small{$\\pm$0.17} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSTE+KL (9.74) is slightly worse than Gumbel+KL (9.20, $\\Delta = 0.54$) but dramatically better than Gumbel+BCE (28.16).\nThe Gumbel relaxation accounts for only 2.8\\% of the total KL advantage over BCE (0.54 out of 18.96 PPL points), confirming that the gradient coupling property of KL---not the relaxation method---drives the quality improvement.\n\n% ------------------------------------------------------------\n\\subsection{Iso-Compute Comparison}\n\\label{sec:isocompute}\n\nKL requires a full forward pass per step to compute logit targets ($\\sim$3.2$\\times$ BCE per-step FLOPs).\nTo control for this, we train BCE for 3200 steps (equal total FLOPs), shown in Table~\\ref{tab:isocompute}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Iso-compute comparison. Extended BCE training (3.2$\\times$ steps) barely closes the gap.}\n\\label{tab:isocompute}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Steps} & \\textbf{Total FLOPs} & \\textbf{PPL} \\\\\n\\midrule\nKL (Gumbel) & 1000 & 3200$\\times$ & 9.20\\small{$\\pm$0.04} \\\\\nBCE (standard) & 1000 & 1000$\\times$ & 28.16\\small{$\\pm$0.17} \\\\\nBCE (extended) & 3200 & 3200$\\times$ & 25.41\\small{$\\pm$0.31} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nExtended BCE training reduces PPL from 28.16 to 25.41 ($-$2.75), but the remaining gap to KL is 16.21 points.\nBCE's information bottleneck is at the loss function level: more compute cannot overcome a factorized gradient that ignores joint neuron interactions.\n\n% ------------------------------------------------------------\n\\subsection{Training-Free Baselines and Quality Hierarchy}\n\\label{sec:baselines}\n\nTable~\\ref{tab:hierarchy} establishes the three-tier quality hierarchy across all method categories.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality hierarchy at 50\\% sparsity (Llama~3.1~8B, WikiText-2).}\n\\label{tab:hierarchy}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Type} & \\textbf{PPL} & \\textbf{$\\Delta$ Dense} \\\\\n\\midrule\nDense & -- & 6.12 & -- \\\\\nTEAL & Training-free & 12.48 & +104\\% \\\\\nR-Sparse & Training-free & 13.62 & +123\\% \\\\\nWINA & Training-free & 14.76 & +141\\% \\\\\nSPON & Static learned & 10.82 & +77\\% \\\\\nKL-only & Contextual learned & 9.20 & +50\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe hierarchy is clean: training-free methods (12.5--14.8 PPL) $<$ static learned (10.82) $<$ contextual learned with KL (9.20).\nEach tier corresponds to increasing information quality: heuristic scoring $\\to$ average-case calibration $\\to$ per-input output-distribution optimization.\nTEAL, the best training-free method, is still 3.28 PPL points worse than KL-only, justifying the overhead of learned prediction.\n\n% ------------------------------------------------------------\n\\subsection{SPON Validation}\n\\label{sec:spon}\n\nWe reimplement SPON on Llama~3.1~8B to serve as the static correction component.\nTable~\\ref{tab:spon} validates correctness via QA benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SPON reimplementation validation (Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:spon}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{Dense} & \\textbf{SPON} & $\\boldsymbol{\\Delta}$ \\\\\n\\midrule\nARC-c & 55.2 & 51.2 & $-$4.0 \\\\\nARC-e & 79.4 & 74.5 & $-$4.9 \\\\\nBoolQ & 83.1 & 79.3 & $-$3.8 \\\\\nPIQA & 81.3 & 78.1 & $-$3.2 \\\\\nWinoGrande & 77.8 & 74.8 & $-$3.0 \\\\\n\\midrule\nWikiText-2 PPL & 6.12 & 10.82 & +77\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSPON achieves 10.82 PPL with accuracy drops of 3--5 points, consistent with the original paper's reported ranges.\nAs a static correction, SPON recovers the expected activation drift $\\mathbb{E}[\\Delta\\mathbf{h}]$ but cannot adapt to per-input variation.\n\n% ------------------------------------------------------------\n\\subsection{SPON + KL Composition}\n\\label{sec:composition}\n\nWe test the modular decomposition $\\mathbf{c} = \\mathbf{c}_s + \\mathbf{c}_\\theta(\\mathbf{x})$ by applying SPON bias correction jointly with the KL predictor.\nTable~\\ref{tab:composition} reports the additivity analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Composition additivity analysis. SPON and KL corrections compose near-additively (6.8\\% interaction residual in logit space).}\n\\label{tab:composition}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Component} & \\textbf{PPL Recovery} & \\textbf{Pred.\\ Additive} & \\textbf{Actual} & \\textbf{Residual} \\\\\n\\midrule\nSPON only & 1.68 & -- & -- & -- \\\\\nKL only & 3.30 & -- & -- & -- \\\\\nSPON+KL & -- & 4.98 & 4.52 & 9.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSPON alone recovers 1.68 PPL points (from the TEAL baseline), KL alone recovers 3.30, and the combination recovers 4.52---close to the predicted additive 4.98 (9.2\\% shortfall in PPL-space, 6.8\\% in logit $L_2$ norm).\nThe resulting SPON+KL achieves 7.98$\\pm$0.10 PPL, only 30.4\\% above dense.\n\nPer-layer cosine similarity between SPON and KL corrections confirms approximate orthogonality: mean cosine 0.11, median 0.08, with only 4 of 32 layers exceeding 0.20.\nThis validates the decomposition: SPON corrects the constant drift component, and KL corrects the per-input residual, with minimal interference.\n\n% ------------------------------------------------------------\n\\subsection{Full Benchmark Suite}\n\\label{sec:fullbench}\n\nTable~\\ref{tab:fullbench} presents comprehensive results across perplexity and downstream tasks.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Comprehensive benchmark results (Llama~3.1~8B, 50\\% sparsity). KL-only averages only 1.3\\% accuracy drop from dense across five tasks; SPON+KL achieves 0.7\\%.}\n\\label{tab:fullbench}\n\\begin{tabular}{lcccccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Wiki$\\downarrow$} & \\textbf{C4$\\downarrow$} & \\textbf{ARC-c$\\uparrow$} & \\textbf{WinoG$\\uparrow$} & \\textbf{MMLU$\\uparrow$} & \\textbf{GSM8K$\\uparrow$} & \\textbf{HumanE$\\uparrow$} & \\textbf{Avg $\\Delta\\downarrow$} \\\\\n\\midrule\nDense & 6.12 & 7.85 & 55.2 & 77.8 & 65.8 & 53.8 & 32.9 & --- \\\\\nTEAL & 12.48 & 15.12 & 48.1 & 72.4 & 58.2 & 44.2 & 26.2 & $-$7.8 \\\\\nWINA & 14.76 & 17.88 & 46.3 & 70.8 & 56.4 & 41.8 & 24.4 & $-$9.9 \\\\\nR-Sparse & 13.62 & 16.31 & 47.2 & 71.5 & 57.1 & 43.1 & 25.6 & $-$8.8 \\\\\nSPON & 10.82 & 13.24 & 51.2 & 74.8 & 60.3 & 46.5 & 28.1 & $-$5.3 \\\\\nBCE+comp & 18.64 & 22.15 & 44.8 & 68.3 & 54.9 & 39.7 & 23.8 & $-$12.8 \\\\\nKL-only & 9.20 & 11.38 & 54.3 & 76.9 & 65.0 & 52.8 & 32.3 & $-$1.3 \\\\\nSPON+KL & 7.98 & 9.81 & 54.8 & 77.2 & 65.4 & 53.2 & 32.5 & $-$0.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nKL-only's low perplexity (9.20 WikiText-2, 11.38 C4) transfers directly to downstream accuracy: the average drop across five tasks is only 1.3\\%, compared to 12.8\\% for BCE+compensation.\nTasks requiring precise multi-step reasoning (GSM8K, HumanEval) show the largest relative advantage for KL---BCE+compensation drops 26--28\\% from dense on these tasks, while KL-only drops less than 2\\%.\nSPON+KL further closes the gap to 0.7\\% average drop.\n\n\\paragraph{Inference efficiency.}\nTable~\\ref{tab:latency} presents the latency--quality Pareto analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Inference efficiency comparison. KL-only Pareto-dominates BCE+comp on all axes.}\n\\label{tab:latency}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{ms/tok} & \\textbf{Speedup} & \\textbf{Extra MB} & \\textbf{PPL} \\\\\n\\midrule\nDense & 16.8 & 1.00$\\times$ & 0 & 6.12 \\\\\nTEAL & 11.2 & 1.50$\\times$ & 0 & 12.48 \\\\\nSPON & 10.9 & 1.54$\\times$ & 1 & 10.82 \\\\\nKL-only & 12.0 & 1.40$\\times$ & 24 & 9.20 \\\\\nBCE+comp & 13.8 & 1.22$\\times$ & 280 & 18.64 \\\\\nSPON+KL & 12.1 & 1.39$\\times$ & 25 & 7.98 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only strictly Pareto-dominates BCE+compensation: better quality (9.20 vs.\\ 18.64 PPL), lower latency (12.0 vs.\\ 13.8\\,ms/token), and 10$\\times$ fewer additional parameters (24 vs.\\ 280\\,MB).\nThe 1.8\\,ms/token savings come from eliminating the per-layer compensation GEMV.\nSPON+KL adds only 0.1\\,ms (bias addition is nearly free) while further improving quality to 7.98 PPL.\n\n% ------------------------------------------------------------\n\\subsection{Quadratic Scaling of KL--BCE Gap}\n\\label{sec:scaling}\n\nWe train KL-only and BCE-only at seven sparsity levels (30--60\\%) with single seeds.\nTable~\\ref{tab:sweep} reports the results and fit statistics.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Sparsity sweep: KL--BCE quality gap $\\Delta$ follows $as^2$ with $R^2 = 0.97$.}\n\\label{tab:sweep}\n\\begin{tabular}{ccccccc}\n\\toprule\n$s$ & $s^2$ & \\textbf{KL} & \\textbf{BCE} & $\\boldsymbol{\\Delta}$ & \\textbf{Pred.}\\ $as^2$ & \\textbf{Taylor \\%} \\\\\n\\midrule\n0.30 & 0.09 & 7.05 & 14.55 & 7.50 & 7.13 & 96.8 \\\\\n0.35 & 0.12 & 7.42 & 17.82 & 10.40 & 9.70 & 95.4 \\\\\n0.40 & 0.16 & 7.98 & 19.98 & 12.00 & 12.67 & 94.1 \\\\\n0.45 & 0.20 & 8.51 & 24.71 & 16.20 & 16.03 & 92.5 \\\\\n0.50 & 0.25 & 9.20 & 28.20 & 19.00 & 19.80 & 89.8 \\\\\n0.55 & 0.30 & 10.82 & 33.62 & 22.80 & 23.96 & 85.6 \\\\\n0.60 & 0.36 & 13.15 & 42.65 & 29.50 & 28.51 & 80.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scaling fit statistics for $\\Delta_{\\mathrm{BCE-KL}}(s)$.}\n\\label{tab:fitstat}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Model} & $\\boldsymbol{R^2}$ & \\textbf{Parameters} \\\\\n\\midrule\n$\\Delta = as^2$ & 0.97 & $a = 79.2$ \\\\\n$\\Delta = as^2 + bs$ & 0.99 & $a = 68.1, b = 5.8$ \\\\\n$\\Delta = as^2 + bs + c$ & 0.99 & $a = 65.3, b = 7.2, c = -0.4$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe pure quadratic model $\\Delta = as^2$ achieves $R^2 = 0.97$, confirming that pairwise neuron interactions dominate the KL--BCE gap.\nAdding a linear term yields $R^2 = 0.99$, consistent with the theoretical expectation that lower-order corrections (single-neuron boundary effects) provide a minor residual.\nThe Taylor expansion accuracy degrades gracefully from 96.8\\% at $s = 0.30$ to 80.2\\% at $s = 0.60$, as expected when higher-order ($s^3$) interaction terms become non-negligible at extreme sparsity.\n\nThis provides a \\emph{testable, non-trivial} prediction beyond our data: the KL advantage will accelerate at sparsity levels above 60\\%, while new developments in BCE-based training (e.g., auxiliary losses) would need to address the fundamental factorization bottleneck to change the scaling law.\n\n% ------------------------------------------------------------\n\\subsection{Cross-Architecture Validation}\n\\label{sec:crossarch}\n\nWe replicate the KL-only vs.\\ BCE+compensation comparison on Mistral-7B-v0.3, which uses GQA with sliding window attention---a different attention architecture from Llama's standard GQA.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture validation on Mistral-7B-v0.3 (50\\% sparsity).}\n\\label{tab:mistral}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Wiki PPL$\\downarrow$} & \\textbf{ARC-c$\\uparrow$} & \\textbf{MMLU$\\uparrow$} \\\\\n\\midrule\nDense & 5.48 & 58.1 & 62.8 \\\\\nKL-only & 8.22\\small{$\\pm$0.10} & 56.4 & 61.3 \\\\\nBCE+comp & 12.86\\small{$\\pm$0.29} & 50.8 & 55.9 \\\\\n\\midrule\nGap (KL vs BCE+comp) & $-$4.64 & +5.6 & +5.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL dominance replicates cleanly: 8.22 vs.\\ 12.86 PPL (36\\% gap).\nThe KL PPL increase over dense is 50.0\\%, strikingly consistent with Llama's 50.3\\%.\nThis consistency across architectures confirms that the advantage is a \\emph{universal property of the loss function}, not an architecture-specific artifact.\nThe absolute gap is smaller than on Llama (4.64 vs.\\ 9.44 PPL) because Mistral's lower dense baseline (5.48 vs.\\ 6.12) and sliding window attention may yield somewhat more localized neuron importance patterns, reducing but not eliminating the interaction effects that BCE misses.\n\n% ------------------------------------------------------------\n\\subsection{Long-Context Evaluation (LongBench)}\n\\label{sec:longbench}\n\nTable~\\ref{tab:longbench} evaluates on LongBench (English subset, 4K--32K tokens) with per-task-type breakdown.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LongBench per-task-type results (Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:longbench}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Task} & \\textbf{Dense} & \\textbf{TEAL} & \\textbf{SPON} & \\textbf{BCE+c} & \\textbf{KL} & \\textbf{S+KL} \\\\\n\\midrule\nSingle-doc QA & 46.2 & 38.1 & 42.0 & 35.2 & 44.8 & 45.3 \\\\\nMulti-doc QA & 39.5 & 31.2 & 36.1 & 28.4 & 38.2 & 38.8 \\\\\nSummarization & 43.8 & 35.8 & 40.2 & 33.8 & 42.5 & 43.1 \\\\\nFew-shot & 48.3 & 39.5 & 44.3 & 34.6 & 47.1 & 47.8 \\\\\nCode & 39.6 & 32.4 & 36.5 & 28.5 & 38.0 & 38.9 \\\\\n\\midrule\n\\textbf{Average} & \\textbf{43.5} & \\textbf{35.4} & \\textbf{39.8} & \\textbf{32.1} & \\textbf{42.1} & \\textbf{42.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only (42.1 average) closely matches dense (43.5, drop 1.4), while BCE+compensation degrades further (32.1, drop 11.4).\nThe KL predictor generalizes well to long contexts despite being trained on short sequences, since it operates on per-token hidden states rather than sequence-level features.\nMulti-doc QA shows the largest KL drop ($-$3.3), consistent with its requirement for cross-document reasoning---the most challenging setting for any approximation.\n\n% ------------------------------------------------------------\n\\subsection{MT-Bench Multi-Turn Evaluation}\n\\label{sec:mtbench}\n\nTable~\\ref{tab:mtbench} reports GPT-4o-judged MT-Bench scores across 80 multi-turn prompts.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{MT-Bench results (GPT-4o judge). KL-only is within judge noise of dense.}\n\\label{tab:mtbench}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Avg} & \\textbf{Writing} & \\textbf{Reason.} & \\textbf{Math} & \\textbf{Coding} \\\\\n\\midrule\nDense & 7.21 & 7.50 & 6.85 & 6.80 & 7.10 \\\\\nTEAL & 6.18 & 6.45 & 5.60 & 5.40 & 5.80 \\\\\nSPON & 6.78 & 7.10 & 6.35 & 6.15 & 6.55 \\\\\nBCE+comp & 6.42 & 6.80 & 5.85 & 5.65 & 5.90 \\\\\nKL-only & 7.05 & 7.35 & 6.65 & 6.55 & 6.85 \\\\\nSPON+KL & 7.12 & 7.40 & 6.75 & 6.65 & 6.95 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only (7.05) is within 0.16 of dense (7.21)---within the GPT-4o judge's scoring noise floor.\nBCE+compensation (6.42) shows severe degradation on reasoning ($-$1.00) and math ($-$1.15), tasks most sensitive to output distribution fidelity.\nSPON+KL (7.12) nearly recovers dense-level performance across all categories.\n\n% ------------------------------------------------------------\n\\subsection{RULER Synthetic Diagnostics}\n\\label{sec:ruler}\n\nTable~\\ref{tab:ruler} provides fine-grained diagnostics on RULER synthetic tasks at 4K and 16K contexts.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RULER synthetic evaluation at 4K and 16K context lengths.}\n\\label{tab:ruler}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Task} & \\textbf{Ctx} & \\textbf{Dense} & \\textbf{KL} & \\textbf{BCE+c} & \\textbf{S+KL} \\\\\n\\midrule\nNeedle & 4K & 99.2 & 98.0 & 94.5 & 98.5 \\\\\nNeedle & 16K & 96.8 & 94.5 & 86.2 & 95.8 \\\\\nMulti-key & 4K & 93.5 & 91.2 & 83.8 & 92.4 \\\\\nMulti-key & 16K & 84.1 & 82.4 & 72.1 & 83.5 \\\\\nVar-track & 4K & 92.8 & 92.1 & 83.9 & 92.5 \\\\\nVar-track & 16K & 84.5 & 81.3 & 76.5 & 83.2 \\\\\n\\midrule\n\\textbf{Average} & \\textbf{4K} & \\textbf{95.2} & \\textbf{93.8} & \\textbf{87.4} & \\textbf{94.5} \\\\\n\\textbf{Average} & \\textbf{16K} & \\textbf{88.5} & \\textbf{86.1} & \\textbf{78.3} & \\textbf{87.2} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only's context-length degradation pattern (4K$\\to$16K: $-$7.7) closely tracks dense ($-$6.7), while BCE+compensation degrades more steeply ($-$9.1).\nMulti-key retrieval shows the largest differentiation at 16K (KL 82.4 vs.\\ BCE+comp 72.1), consistent with this task's sensitivity to joint neuron interactions---simultaneous retrieval of multiple scattered facts requires precise FFN activation patterns.\n\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Two-dimensional taxonomy.}\nOur results populate a two-axis taxonomy of sparsity correction methods: \\emph{correction granularity} (static $\\to$ per-layer $\\to$ per-token) $\\times$ \\emph{training signal coupling} (decomposed/BCE $\\to$ intermediate/MSE $\\to$ coupled/KL).\nPrior work fills specific cells---SPON (static, KL), ShadowLLM (per-layer, MSE), FastForward (per-token, BCE)---while our KL-only method fills the (per-token, KL) cell, which proves to be the Pareto-optimal configuration.\n\n\\paragraph{Practical implications.}\nEliminating compensation networks simplifies the inference pipeline: no additional parameters to load, no per-layer GEMV, and a smaller memory footprint.\nFor Llama~3.1~8B, this means 256\\,MB fewer parameters and 1.8\\,ms/token lower latency, with strictly better quality.\nThe SPON+KL variant adds only 1\\,MB (static biases) for a further 1.22 PPL improvement.\n\n\\paragraph{Limitations.}\nWe evaluate on 7--8B parameter models; scaling behavior at 70B+ remains to be verified.\nThe quadratic scaling prediction is confirmed over $s \\in [0.3, 0.6]$ but extrapolation beyond 60\\% needs additional data.\nKL training requires a teacher forward pass per step ($3.2\\times$ per-step cost), though the total training time is modest (4.2 hours on a single GPU for 1000 steps).\n\n% ============================================================\n\\section{Conclusion}\n\nWe have shown that output-distribution distillation via KL divergence categorically dominates BCE-based training for contextual activation sparsity prediction in SwiGLU LLMs, eliminating the need for compensation networks.\nThe advantage traces to a fundamental difference in gradient structure: KL's coupled gradients capture joint neuron interactions that BCE's factorized gradients miss, with the quality gap scaling quadratically in sparsity ($R^2 = 0.97$).\nThe resulting method is simultaneously simpler (no compensation network), smaller (24\\,MB vs.\\ 280\\,MB), faster (12.0 vs.\\ 13.8\\,ms/token), and better (9.20 vs.\\ 18.64 PPL) than the BCE+compensation alternative.\nCombined with SPON's static bias correction, the modular decomposition achieves 7.98 PPL---within 30\\% of dense---with near-perfect additivity.\n\n% ============================================================\n\\bibliography{custom}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Shazeer, 2020]{shazeer2020glu}\nNoam Shazeer. 2020.\n\\newblock {GLU} Variants Improve Transformer.\n\\newblock {\\em arXiv preprint arXiv:2002.05202}.\n\n\\bibitem[Liu et~al., 2024]{liu2024teal}\nYixin Liu, Haotian Ye, Lei Li, and Hao Peng. 2024.\n\\newblock {TEAL}: Token-wise Efficient Activation sparsity for {LLM}s.\n\\newblock In {\\em Proceedings of NeurIPS}.\n\n\\bibitem[Shen et~al., 2024]{shen2024wina}\nZhihang Shen, et~al. 2024.\n\\newblock {WINA}: Weight-Informed Neuron Activation for accelerating large language model inference.\n\\newblock {\\em arXiv preprint arXiv:2410.xxxx}.\n\n\\bibitem[Zhang et~al., 2024]{zhang2024rsparse}\nTianyu Zhang, et~al. 2024.\n\\newblock {R-Sparse}: Rank-Aware Activation Sparsity for efficient {LLM} inference.\n\\newblock {\\em arXiv preprint arXiv:2410.xxxx}.\n\n\\bibitem[Wang et~al., 2024]{wang2024fastforward}\nTao Wang, et~al. 2024.\n\\newblock {FastForward}: Learned sparsity prediction with compensation for efficient {LLM} inference.\n\\newblock {\\em arXiv preprint arXiv:2405.xxxx}.\n\n\\bibitem[Zhou et~al., 2024]{zhou2024spon}\nYongqi Zhou, et~al. 2024.\n\\newblock {SPON}: Static-correction-based sparsity optimization for language models via {KL} distillation.\n\\newblock {\\em arXiv preprint arXiv:2406.xxxx}.\n\n\\bibitem[Chen et~al., 2024]{chen2024shadowllm}\nZheng Chen, et~al. 2024.\n\\newblock {ShadowLLM}: Predictor-based contextual sparsity for large language models.\n\\newblock {\\em arXiv preprint arXiv:2406.xxxx}.\n\n\\bibitem[Hinton et~al., 2015]{hinton2015distilling}\nGeoffrey Hinton, Oriol Vinyals, and Jeff Dean. 2015.\n\\newblock Distilling the Knowledge in a Neural Network.\n\\newblock {\\em arXiv preprint arXiv:1503.02531}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d100d5b3-4778-403c-9d54-12a8e1ed5a02",
  "isSidechain": false,
  "requestId": "req_011Cb4kETFvwv1mwfkHWjxuM",
  "type": "assistant",
  "uuid": "cc69d9f4-3c9d-4a57-a485-c27a10fd3317",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TY3c7RXSxLUZHfqSDdr5jS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 42744,
      "output_tokens": 12711,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 506,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12711,
          "cache_read_input_tokens": 42744,
          "cache_creation_input_tokens": 506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 506
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

_source line 19 · 2026-05-15T17:29:54.637Z_

<details><summary>↩ Tool result · `toolu_01Ls3c6RLfrE5oF368qCLDGZ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc69d9f4-3c9d-4a57-a485-c27a10fd3317",
  "isSidechain": false,
  "promptId": "4324b22a-92db-42ef-a974-2006388d7cce",
  "type": "user",
  "uuid": "4ca840d7-2524-45eb-84aa-9ce11a08a1a0",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{array}\n\\usepackage{xcolor}\n\n\\title{Output-Distribution Distillation Makes Compensation Networks Obsolete\\\\for SwiGLU Activation Sparsity}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nActivation sparsity in SwiGLU-based large language models enables significant inference speedups by dynamically pruning neurons, but existing learned approaches (e.g., FastForward) train per-neuron binary predictors with BCE loss and require auxiliary compensation networks ($\\sim$256\\,MB) to recover quality---adding latency and memory overhead.\nWe show that replacing BCE with KL-divergence distillation on the output distribution \\emph{eliminates the need for compensation entirely}.\nOn Llama~3.1~8B at 50\\% model-level sparsity, a KL-trained contextual predictor without compensation achieves 9.20 perplexity on WikiText-2 (within 50\\% of the dense 6.12 baseline), while BCE with compensation reaches only 18.64---a gap of 9.44 PPL points.\nThe advantage stems from KL's gradient structure, which couples all active neurons through the output Jacobian, capturing joint interaction effects that BCE's factorized per-neuron gradient misses.\nWe formalize a modular decomposition $\\mathbf{c} = \\mathbf{c}_s + \\mathbf{c}_\\theta(\\mathbf{x})$ combining SPON's static bias correction with KL contextual prediction, achieving 7.98 PPL with only 6.8\\% interaction residual.\nA seven-level sparsity sweep confirms the theoretically predicted quadratic scaling of the KL--BCE quality gap ($R^2 = 0.97$).\nCross-architecture validation on Mistral-7B-v0.3, comprehensive downstream benchmarks (MMLU, GSM8K, HumanEval, LongBench, MT-Bench, RULER), and latency profiling demonstrate that KL-only Pareto-dominates BCE+compensation: better quality, lower latency (12.0 vs.\\ 13.8\\,ms/token), and 10$\\times$ fewer additional parameters (24\\,MB vs.\\ 280\\,MB).\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nSwiGLU feed-forward networks~\\cite{shazeer2020glu} in modern LLMs exhibit substantial contextual activation sparsity: at any given input, a large fraction of intermediate neurons contribute negligibly to the output.\nExploiting this sparsity at inference time by dynamically skipping inactive neurons can yield wall-clock speedups of $1.3$--$1.5\\times$, a practically significant reduction for latency-sensitive deployment.\n\nThree tiers of approaches have emerged.\n\\emph{Training-free} methods (TEAL, WINA, R-Sparse) apply static heuristics---magnitude thresholds, weight-informed scores---to select neurons.\nWhile requiring no training, these methods incur a 6--9 PPL point gap at 50\\% sparsity on Llama~3.1~8B.\n\\emph{Static learned} approaches such as SPON learn input-independent per-layer bias corrections via KL distillation, recovering average-case activation drift but unable to adapt to per-input variation.\n\\emph{Contextual learned} methods, exemplified by FastForward, train a lightweight MLP to predict per-token neuron importance.\nHowever, FastForward uses binary cross-entropy (BCE) to train this predictor independently per neuron, then attaches a compensation network to correct the residual error---adding $\\sim$256\\,MB of parameters and a per-layer GEMV at inference time.\n\nWe ask: \\emph{does the compensation network compensate for a fundamental limitation of the predictor, or for a limitation of the training objective?}\nThe answer hinges on gradient structure.\nThe BCE gradient $\\partial\\mathcal{L}_{\\mathrm{BCE}}/\\partial s_j = (\\sigma(s_j) - t_j)\\sigma'(s_j)$ depends only on neuron $j$'s own target, factorizing across neurons.\nIn contrast, the KL gradient $\\partial\\mathcal{L}_{\\mathrm{KL}}/\\partial s_j$ propagates through the full Jacobian $\\partial\\mathbf{z}/\\partial\\mathbf{h} \\cdot \\partial\\mathbf{h}/\\partial\\mathbf{m}$, coupling all active neurons.\nThis coupling captures joint interaction effects that scale as $O(s^2 D^2)$ with sparsity level $s$ and hidden dimension $D$---precisely the effects that compensation networks attempt to correct post hoc.\n\nOur contributions:\n\\begin{enumerate}\n    \\item We demonstrate that KL-trained contextual sparsity predictors categorically dominate BCE+compensation: 9.20 vs.\\ 18.64 PPL on Llama~3.1~8B at 50\\% sparsity, with lower latency and 10$\\times$ fewer parameters (\\S\\ref{sec:ablation}, \\S\\ref{sec:fullbench}).\n    \\item We formalize a modular decomposition $\\mathbf{c} = \\mathbf{c}_s + \\mathbf{c}_\\theta(\\mathbf{x})$ combining static (SPON) and contextual (KL) corrections, achieving 7.98 PPL with near-additive composition (6.8\\% interaction residual; \\S\\ref{sec:composition}).\n    \\item We provide a testable theoretical prediction---the KL--BCE quality gap scales quadratically with sparsity---and confirm it empirically ($R^2 = 0.97$ across seven sparsity levels; \\S\\ref{sec:scaling}).\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Training-free activation sparsity.}\nTEAL~\\cite{liu2024teal} uses magnitude-based thresholding with greedy per-layer budget allocation.\nWINA~\\cite{shen2024wina} incorporates weight magnitudes into the scoring criterion.\nR-Sparse~\\cite{zhang2024rsparse} introduces rank-aware scoring.\nAll three operate without any parameter training but suffer quality gaps of 6--9 PPL points at 50\\% sparsity.\n\n\\paragraph{Learned sparsity prediction.}\nFastForward~\\cite{wang2024fastforward} trains a small MLP per layer to predict binary neuron masks using BCE, then adds a compensation MLP to correct residual errors.\nSPON~\\cite{zhou2024spon} takes a different approach: learning input-independent per-layer bias vectors via KL distillation of the teacher's output distribution.\nShadowLLM~\\cite{chen2024shadowllm} uses MSE on intermediate representations for per-layer correction.\n\n\\paragraph{Knowledge distillation for sparsity.}\nOutput-distribution matching via KL divergence is standard in knowledge distillation~\\cite{hinton2015distilling} but has not been applied to train \\emph{contextual} sparsity predictors.\nThe key distinction is that we distill the \\emph{sparsity decision} (which neurons to activate) rather than the model weights, and the KL gradient structure provides a principled advantage over per-neuron objectives.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\nConsider a SwiGLU FFN layer with gate projection $\\mathbf{g} = \\sigma_{\\mathrm{SiLU}}(\\mathbf{W}_g \\mathbf{x})$, up projection $\\mathbf{u} = \\mathbf{W}_u \\mathbf{x}$, and element-wise product $\\mathbf{h} = \\mathbf{g} \\odot \\mathbf{u}$.\nA binary mask $\\mathbf{m} \\in \\{0,1\\}^D$ selects a subset of neurons, yielding sparse output $\\mathbf{y}_{\\mathrm{sparse}} = \\mathbf{W}_d (\\mathbf{m} \\odot \\mathbf{h})$.\nWe seek a predictor $f_\\theta(\\mathbf{x}): \\mathbb{R}^{d} \\to [0,1]^D$ that produces soft scores, relaxed to masks via Gumbel-sigmoid sampling during training and hard thresholding at inference.\n\n\\subsection{Gradient Coupling: KL vs.\\ BCE}\n\n\\paragraph{BCE objective.}\nGiven oracle mask $\\mathbf{t}$ (e.g., top-$k$ by activation magnitude), the BCE loss is:\n\\begin{equation}\n\\mathcal{L}_{\\mathrm{BCE}} = -\\sum_{j=1}^{D} \\big[ t_j \\log \\sigma(s_j) + (1-t_j)\\log(1-\\sigma(s_j)) \\big]\n\\end{equation}\nwhere $s_j = f_\\theta(\\mathbf{x})_j$.\nThe gradient $\\partial\\mathcal{L}_{\\mathrm{BCE}}/\\partial s_j = \\sigma(s_j) - t_j$ depends only on neuron $j$---the loss \\emph{factorizes} across neurons.\n\n\\paragraph{KL objective.}\nWe instead minimize the KL divergence between the dense and sparse model output distributions:\n\\begin{equation}\n\\mathcal{L}_{\\mathrm{KL}} = \\mathrm{KL}\\!\\left(p_{\\mathrm{dense}}(\\cdot|\\mathbf{x}) \\;\\|\\; p_{\\mathrm{sparse}}(\\cdot|\\mathbf{x}, \\mathbf{m})\\right)\n\\end{equation}\nThe gradient with respect to score $s_j$ is:\n\\begin{equation}\n\\frac{\\partial\\mathcal{L}_{\\mathrm{KL}}}{\\partial s_j} = \\underbrace{\\frac{\\partial\\mathcal{L}_{\\mathrm{KL}}}{\\partial \\mathbf{z}}}_{\\text{output error}} \\cdot \\underbrace{\\frac{\\partial \\mathbf{z}}{\\partial \\mathbf{h}}}_{\\text{down proj}} \\cdot \\underbrace{\\frac{\\partial \\mathbf{h}}{\\partial m_j}}_{\\text{neuron }j} \\cdot \\frac{\\partial m_j}{\\partial s_j}\n\\end{equation}\nCritically, $\\partial\\mathbf{z}/\\partial\\mathbf{h} = \\mathbf{W}_d$ and $\\partial\\mathcal{L}_{\\mathrm{KL}}/\\partial\\mathbf{z}$ depend on the \\emph{full} sparse output, which in turn depends on \\emph{all} active neurons.\nThus the gradient for neuron $j$ is \\emph{coupled} to all other neurons' mask decisions through the shared output space.\n\n\\paragraph{Quadratic scaling prediction.}\nWhen sparsity is $s$, each pruned neuron interacts with $O(sD)$ other pruned neurons.\nThe total pairwise interaction effects scale as $O(s^2 D^2)$.\nBCE's factorized gradient ignores all such interactions, while KL captures them through the Jacobian.\nThis yields the testable prediction that the KL--BCE quality gap $\\Delta(s) \\approx a s^2$ for some constant $a$.\n\n\\subsection{Modular Decomposition}\n\\label{sec:decomposition}\n\nWe decompose the total correction to the sparse hidden states as:\n\\begin{equation}\n\\mathbf{c} = \\mathbf{c}_s + \\mathbf{c}_\\theta(\\mathbf{x})\n\\end{equation}\nwhere $\\mathbf{c}_s = \\mathbb{E}[\\Delta\\mathbf{h}]$ is the static, input-independent bias correction (as in SPON), and $\\mathbf{c}_\\theta(\\mathbf{x}) = \\Delta\\mathbf{h}(\\mathbf{x}) - \\mathbb{E}[\\Delta\\mathbf{h}]$ is the per-input residual variation captured by the KL contextual predictor.\nSince $\\mathbf{c}_s$ is constant and $\\mathbf{c}_\\theta(\\mathbf{x})$ is zero-mean by construction, the two corrections are approximately orthogonal.\nWe measure the interaction residual as:\n\\begin{equation}\n\\rho = \\frac{\\|\\mathbf{c} - (\\mathbf{c}_s + \\mathbf{c}_\\theta(\\mathbf{x}))\\|_2}{\\|\\mathbf{c}_s\\|_2 + \\|\\mathbf{c}_\\theta(\\mathbf{x})\\|_2}\n\\end{equation}\nand predict $\\rho \\ll 1$ when SPON and the KL predictor address different error components.\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Models.}\nWe evaluate on Llama~3.1~8B (primary) and Mistral-7B-v0.3 (cross-architecture validation).\nBoth use SwiGLU FFN layers with intermediate dimension $D = 14336$ (Llama) and $D = 14336$ (Mistral).\n\n\\paragraph{Sparsity target.}\nUnless otherwise noted, we target 50\\% model-level sparsity with per-layer budget allocation following TEAL's greedy algorithm.\n\n\\paragraph{Training.}\nKL and BCE predictors share identical architecture (2-layer MLP, $\\sim$24\\,MB per model).\nTraining uses 1000 steps on a 10M-token calibration subset of C4.\nGumbel-sigmoid relaxation ($\\tau = 1.0 \\to 0.1$ cosine anneal) enables gradient flow through discrete masks during training; hard thresholds are used at inference.\nWe report WikiText-2 perplexity as the primary metric.\n\n\\paragraph{Baselines.}\nWe compare against: (1)~Dense (no sparsity), (2)~TEAL, WINA, R-Sparse (training-free), (3)~SPON (static learned), (4)~BCE-only, BCE+compensation (contextual learned, FastForward-style), and (5)~our KL-only, KL+compensation, and SPON+KL variants.\n\n% ------------------------------------------------------------\n\\subsection{Four-Condition Ablation}\n\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} presents the core ablation at 50\\% sparsity on Llama~3.1~8B.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Four-condition ablation on WikiText-2 (Llama~3.1~8B, 50\\% sparsity). KL-only outperforms BCE+compensation by 9.44 PPL points without any compensation network.}\n\\label{tab:ablation}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Seeds} & \\textbf{PPL} & \\textbf{$\\Delta$ Dense} & \\textbf{Comp.\\ Benefit} \\\\\n\\midrule\nDense & -- & 6.12 & -- & -- \\\\\nBCE-only & 3 & 28.16\\small{$\\pm$0.17} & +360\\% & -- \\\\\nBCE+comp & 5 & 18.64\\small{$\\pm$0.33} & +205\\% & $-$9.52 \\\\\nKL-only & 5 & 9.20\\small{$\\pm$0.04} & +50\\% & -- \\\\\nKL+comp & 3 & 9.02\\small{$\\pm$0.07} & +47\\% & $-$0.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only achieves 9.20$\\pm$0.04 PPL, surpassing BCE+compensation (18.64$\\pm$0.33) by 9.44 points.\nAdding compensation to KL yields only 0.18 PPL improvement (9.02 vs.\\ 9.20), compared to 9.52 for BCE.\nThe extremely low standard deviation across 5 seeds (0.04) confirms high reproducibility.\nThe compensation network is made redundant by KL's gradient coupling---it corrects at training time what compensation would correct at inference time.\n\n% ------------------------------------------------------------\n\\subsection{Isolating Loss vs.\\ Relaxation (STE Baseline)}\n\\label{sec:ste}\n\nA natural concern is whether the advantage comes from the KL loss function or from Gumbel-sigmoid relaxation.\nWe replace Gumbel-sigmoid with Straight-Through Estimation (STE) while keeping KL loss, shown in Table~\\ref{tab:ste}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Relaxation method ablation. STE+KL still dominates Gumbel+BCE, confirming the loss function drives $>$97\\% of the advantage.}\n\\label{tab:ste}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Relaxation} & \\textbf{Loss} & \\textbf{PPL} \\\\\n\\midrule\nGumbel+KL (ours) & Gumbel-sigmoid & KL & 9.20\\small{$\\pm$0.04} \\\\\nSTE+KL & Straight-Through & KL & 9.74\\small{$\\pm$0.09} \\\\\nGumbel+BCE & Gumbel-sigmoid & BCE & 28.16\\small{$\\pm$0.17} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSTE+KL (9.74) is slightly worse than Gumbel+KL (9.20, $\\Delta = 0.54$) but dramatically better than Gumbel+BCE (28.16).\nThe Gumbel relaxation accounts for only 2.8\\% of the total KL advantage over BCE (0.54 out of 18.96 PPL points), confirming that the gradient coupling property of KL---not the relaxation method---drives the quality improvement.\n\n% ------------------------------------------------------------\n\\subsection{Iso-Compute Comparison}\n\\label{sec:isocompute}\n\nKL requires a full forward pass per step to compute logit targets ($\\sim$3.2$\\times$ BCE per-step FLOPs).\nTo control for this, we train BCE for 3200 steps (equal total FLOPs), shown in Table~\\ref{tab:isocompute}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Iso-compute comparison. Extended BCE training (3.2$\\times$ steps) barely closes the gap.}\n\\label{tab:isocompute}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Steps} & \\textbf{Total FLOPs} & \\textbf{PPL} \\\\\n\\midrule\nKL (Gumbel) & 1000 & 3200$\\times$ & 9.20\\small{$\\pm$0.04} \\\\\nBCE (standard) & 1000 & 1000$\\times$ & 28.16\\small{$\\pm$0.17} \\\\\nBCE (extended) & 3200 & 3200$\\times$ & 25.41\\small{$\\pm$0.31} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nExtended BCE training reduces PPL from 28.16 to 25.41 ($-$2.75), but the remaining gap to KL is 16.21 points.\nBCE's information bottleneck is at the loss function level: more compute cannot overcome a factorized gradient that ignores joint neuron interactions.\n\n% ------------------------------------------------------------\n\\subsection{Training-Free Baselines and Quality Hierarchy}\n\\label{sec:baselines}\n\nTable~\\ref{tab:hierarchy} establishes the three-tier quality hierarchy across all method categories.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality hierarchy at 50\\% sparsity (Llama~3.1~8B, WikiText-2).}\n\\label{tab:hierarchy}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Type} & \\textbf{PPL} & \\textbf{$\\Delta$ Dense} \\\\\n\\midrule\nDense & -- & 6.12 & -- \\\\\nTEAL & Training-free & 12.48 & +104\\% \\\\\nR-Sparse & Training-free & 13.62 & +123\\% \\\\\nWINA & Training-free & 14.76 & +141\\% \\\\\nSPON & Static learned & 10.82 & +77\\% \\\\\nKL-only & Contextual learned & 9.20 & +50\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe hierarchy is clean: training-free methods (12.5--14.8 PPL) $<$ static learned (10.82) $<$ contextual learned with KL (9.20).\nEach tier corresponds to increasing information quality: heuristic scoring $\\to$ average-case calibration $\\to$ per-input output-distribution optimization.\nTEAL, the best training-free method, is still 3.28 PPL points worse than KL-only, justifying the overhead of learned prediction.\n\n% ------------------------------------------------------------\n\\subsection{SPON Validation}\n\\label{sec:spon}\n\nWe reimplement SPON on Llama~3.1~8B to serve as the static correction component.\nTable~\\ref{tab:spon} validates correctness via QA benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SPON reimplementation validation (Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:spon}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{Dense} & \\textbf{SPON} & $\\boldsymbol{\\Delta}$ \\\\\n\\midrule\nARC-c & 55.2 & 51.2 & $-$4.0 \\\\\nARC-e & 79.4 & 74.5 & $-$4.9 \\\\\nBoolQ & 83.1 & 79.3 & $-$3.8 \\\\\nPIQA & 81.3 & 78.1 & $-$3.2 \\\\\nWinoGrande & 77.8 & 74.8 & $-$3.0 \\\\\n\\midrule\nWikiText-2 PPL & 6.12 & 10.82 & +77\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSPON achieves 10.82 PPL with accuracy drops of 3--5 points, consistent with the original paper's reported ranges.\nAs a static correction, SPON recovers the expected activation drift $\\mathbb{E}[\\Delta\\mathbf{h}]$ but cannot adapt to per-input variation.\n\n% ------------------------------------------------------------\n\\subsection{SPON + KL Composition}\n\\label{sec:composition}\n\nWe test the modular decomposition $\\mathbf{c} = \\mathbf{c}_s + \\mathbf{c}_\\theta(\\mathbf{x})$ by applying SPON bias correction jointly with the KL predictor.\nTable~\\ref{tab:composition} reports the additivity analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Composition additivity analysis. SPON and KL corrections compose near-additively (6.8\\% interaction residual in logit space).}\n\\label{tab:composition}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Component} & \\textbf{PPL Recovery} & \\textbf{Pred.\\ Additive} & \\textbf{Actual} & \\textbf{Residual} \\\\\n\\midrule\nSPON only & 1.68 & -- & -- & -- \\\\\nKL only & 3.30 & -- & -- & -- \\\\\nSPON+KL & -- & 4.98 & 4.52 & 9.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSPON alone recovers 1.68 PPL points (from the TEAL baseline), KL alone recovers 3.30, and the combination recovers 4.52---close to the predicted additive 4.98 (9.2\\% shortfall in PPL-space, 6.8\\% in logit $L_2$ norm).\nThe resulting SPON+KL achieves 7.98$\\pm$0.10 PPL, only 30.4\\% above dense.\n\nPer-layer cosine similarity between SPON and KL corrections confirms approximate orthogonality: mean cosine 0.11, median 0.08, with only 4 of 32 layers exceeding 0.20.\nThis validates the decomposition: SPON corrects the constant drift component, and KL corrects the per-input residual, with minimal interference.\n\n% ------------------------------------------------------------\n\\subsection{Full Benchmark Suite}\n\\label{sec:fullbench}\n\nTable~\\ref{tab:fullbench} presents comprehensive results across perplexity and downstream tasks.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Comprehensive benchmark results (Llama~3.1~8B, 50\\% sparsity). KL-only averages only 1.3\\% accuracy drop from dense across five tasks; SPON+KL achieves 0.7\\%.}\n\\label{tab:fullbench}\n\\begin{tabular}{lcccccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Wiki$\\downarrow$} & \\textbf{C4$\\downarrow$} & \\textbf{ARC-c$\\uparrow$} & \\textbf{WinoG$\\uparrow$} & \\textbf{MMLU$\\uparrow$} & \\textbf{GSM8K$\\uparrow$} & \\textbf{HumanE$\\uparrow$} & \\textbf{Avg $\\Delta\\downarrow$} \\\\\n\\midrule\nDense & 6.12 & 7.85 & 55.2 & 77.8 & 65.8 & 53.8 & 32.9 & --- \\\\\nTEAL & 12.48 & 15.12 & 48.1 & 72.4 & 58.2 & 44.2 & 26.2 & $-$7.8 \\\\\nWINA & 14.76 & 17.88 & 46.3 & 70.8 & 56.4 & 41.8 & 24.4 & $-$9.9 \\\\\nR-Sparse & 13.62 & 16.31 & 47.2 & 71.5 & 57.1 & 43.1 & 25.6 & $-$8.8 \\\\\nSPON & 10.82 & 13.24 & 51.2 & 74.8 & 60.3 & 46.5 & 28.1 & $-$5.3 \\\\\nBCE+comp & 18.64 & 22.15 & 44.8 & 68.3 & 54.9 & 39.7 & 23.8 & $-$12.8 \\\\\nKL-only & 9.20 & 11.38 & 54.3 & 76.9 & 65.0 & 52.8 & 32.3 & $-$1.3 \\\\\nSPON+KL & 7.98 & 9.81 & 54.8 & 77.2 & 65.4 & 53.2 & 32.5 & $-$0.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nKL-only's low perplexity (9.20 WikiText-2, 11.38 C4) transfers directly to downstream accuracy: the average drop across five tasks is only 1.3\\%, compared to 12.8\\% for BCE+compensation.\nTasks requiring precise multi-step reasoning (GSM8K, HumanEval) show the largest relative advantage for KL---BCE+compensation drops 26--28\\% from dense on these tasks, while KL-only drops less than 2\\%.\nSPON+KL further closes the gap to 0.7\\% average drop.\n\n\\paragraph{Inference efficiency.}\nTable~\\ref{tab:latency} presents the latency--quality Pareto analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Inference efficiency comparison. KL-only Pareto-dominates BCE+comp on all axes.}\n\\label{tab:latency}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{ms/tok} & \\textbf{Speedup} & \\textbf{Extra MB} & \\textbf{PPL} \\\\\n\\midrule\nDense & 16.8 & 1.00$\\times$ & 0 & 6.12 \\\\\nTEAL & 11.2 & 1.50$\\times$ & 0 & 12.48 \\\\\nSPON & 10.9 & 1.54$\\times$ & 1 & 10.82 \\\\\nKL-only & 12.0 & 1.40$\\times$ & 24 & 9.20 \\\\\nBCE+comp & 13.8 & 1.22$\\times$ & 280 & 18.64 \\\\\nSPON+KL & 12.1 & 1.39$\\times$ & 25 & 7.98 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only strictly Pareto-dominates BCE+compensation: better quality (9.20 vs.\\ 18.64 PPL), lower latency (12.0 vs.\\ 13.8\\,ms/token), and 10$\\times$ fewer additional parameters (24 vs.\\ 280\\,MB).\nThe 1.8\\,ms/token savings come from eliminating the per-layer compensation GEMV.\nSPON+KL adds only 0.1\\,ms (bias addition is nearly free) while further improving quality to 7.98 PPL.\n\n% ------------------------------------------------------------\n\\subsection{Quadratic Scaling of KL--BCE Gap}\n\\label{sec:scaling}\n\nWe train KL-only and BCE-only at seven sparsity levels (30--60\\%) with single seeds.\nTable~\\ref{tab:sweep} reports the results and fit statistics.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Sparsity sweep: KL--BCE quality gap $\\Delta$ follows $as^2$ with $R^2 = 0.97$.}\n\\label{tab:sweep}\n\\begin{tabular}{ccccccc}\n\\toprule\n$s$ & $s^2$ & \\textbf{KL} & \\textbf{BCE} & $\\boldsymbol{\\Delta}$ & \\textbf{Pred.}\\ $as^2$ & \\textbf{Taylor \\%} \\\\\n\\midrule\n0.30 & 0.09 & 7.05 & 14.55 & 7.50 & 7.13 & 96.8 \\\\\n0.35 & 0.12 & 7.42 & 17.82 & 10.40 & 9.70 & 95.4 \\\\\n0.40 & 0.16 & 7.98 & 19.98 & 12.00 & 12.67 & 94.1 \\\\\n0.45 & 0.20 & 8.51 & 24.71 & 16.20 & 16.03 & 92.5 \\\\\n0.50 & 0.25 & 9.20 & 28.20 & 19.00 & 19.80 & 89.8 \\\\\n0.55 & 0.30 & 10.82 & 33.62 & 22.80 & 23.96 & 85.6 \\\\\n0.60 & 0.36 & 13.15 & 42.65 & 29.50 & 28.51 & 80.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scaling fit statistics for $\\Delta_{\\mathrm{BCE-KL}}(s)$.}\n\\label{tab:fitstat}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Model} & $\\boldsymbol{R^2}$ & \\textbf{Parameters} \\\\\n\\midrule\n$\\Delta = as^2$ & 0.97 & $a = 79.2$ \\\\\n$\\Delta = as^2 + bs$ & 0.99 & $a = 68.1, b = 5.8$ \\\\\n$\\Delta = as^2 + bs + c$ & 0.99 & $a = 65.3, b = 7.2, c = -0.4$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe pure quadratic model $\\Delta = as^2$ achieves $R^2 = 0.97$, confirming that pairwise neuron interactions dominate the KL--BCE gap.\nAdding a linear term yields $R^2 = 0.99$, consistent with the theoretical expectation that lower-order corrections (single-neuron boundary effects) provide a minor residual.\nThe Taylor expansion accuracy degrades gracefully from 96.8\\% at $s = 0.30$ to 80.2\\% at $s = 0.60$, as expected when higher-order ($s^3$) interaction terms become non-negligible at extreme sparsity.\n\nThis provides a \\emph{testable, non-trivial} prediction beyond our data: the KL advantage will accelerate at sparsity levels above 60\\%, while new developments in BCE-based training (e.g., auxiliary losses) would need to address the fundamental factorization bottleneck to change the scaling law.\n\n% ------------------------------------------------------------\n\\subsection{Cross-Architecture Validation}\n\\label{sec:crossarch}\n\nWe replicate the KL-only vs.\\ BCE+compensation comparison on Mistral-7B-v0.3, which uses GQA with sliding window attention---a different attention architecture from Llama's standard GQA.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture validation on Mistral-7B-v0.3 (50\\% sparsity).}\n\\label{tab:mistral}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Wiki PPL$\\downarrow$} & \\textbf{ARC-c$\\uparrow$} & \\textbf{MMLU$\\uparrow$} \\\\\n\\midrule\nDense & 5.48 & 58.1 & 62.8 \\\\\nKL-only & 8.22\\small{$\\pm$0.10} & 56.4 & 61.3 \\\\\nBCE+comp & 12.86\\small{$\\pm$0.29} & 50.8 & 55.9 \\\\\n\\midrule\nGap (KL vs BCE+comp) & $-$4.64 & +5.6 & +5.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL dominance replicates cleanly: 8.22 vs.\\ 12.86 PPL (36\\% gap).\nThe KL PPL increase over dense is 50.0\\%, strikingly consistent with Llama's 50.3\\%.\nThis consistency across architectures confirms that the advantage is a \\emph{universal property of the loss function}, not an architecture-specific artifact.\nThe absolute gap is smaller than on Llama (4.64 vs.\\ 9.44 PPL) because Mistral's lower dense baseline (5.48 vs.\\ 6.12) and sliding window attention may yield somewhat more localized neuron importance patterns, reducing but not eliminating the interaction effects that BCE misses.\n\n% ------------------------------------------------------------\n\\subsection{Long-Context Evaluation (LongBench)}\n\\label{sec:longbench}\n\nTable~\\ref{tab:longbench} evaluates on LongBench (English subset, 4K--32K tokens) with per-task-type breakdown.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LongBench per-task-type results (Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:longbench}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Task} & \\textbf{Dense} & \\textbf{TEAL} & \\textbf{SPON} & \\textbf{BCE+c} & \\textbf{KL} & \\textbf{S+KL} \\\\\n\\midrule\nSingle-doc QA & 46.2 & 38.1 & 42.0 & 35.2 & 44.8 & 45.3 \\\\\nMulti-doc QA & 39.5 & 31.2 & 36.1 & 28.4 & 38.2 & 38.8 \\\\\nSummarization & 43.8 & 35.8 & 40.2 & 33.8 & 42.5 & 43.1 \\\\\nFew-shot & 48.3 & 39.5 & 44.3 & 34.6 & 47.1 & 47.8 \\\\\nCode & 39.6 & 32.4 & 36.5 & 28.5 & 38.0 & 38.9 \\\\\n\\midrule\n\\textbf{Average} & \\textbf{43.5} & \\textbf{35.4} & \\textbf{39.8} & \\textbf{32.1} & \\textbf{42.1} & \\textbf{42.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only (42.1 average) closely matches dense (43.5, drop 1.4), while BCE+compensation degrades further (32.1, drop 11.4).\nThe KL predictor generalizes well to long contexts despite being trained on short sequences, since it operates on per-token hidden states rather than sequence-level features.\nMulti-doc QA shows the largest KL drop ($-$3.3), consistent with its requirement for cross-document reasoning---the most challenging setting for any approximation.\n\n% ------------------------------------------------------------\n\\subsection{MT-Bench Multi-Turn Evaluation}\n\\label{sec:mtbench}\n\nTable~\\ref{tab:mtbench} reports GPT-4o-judged MT-Bench scores across 80 multi-turn prompts.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{MT-Bench results (GPT-4o judge). KL-only is within judge noise of dense.}\n\\label{tab:mtbench}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Avg} & \\textbf{Writing} & \\textbf{Reason.} & \\textbf{Math} & \\textbf{Coding} \\\\\n\\midrule\nDense & 7.21 & 7.50 & 6.85 & 6.80 & 7.10 \\\\\nTEAL & 6.18 & 6.45 & 5.60 & 5.40 & 5.80 \\\\\nSPON & 6.78 & 7.10 & 6.35 & 6.15 & 6.55 \\\\\nBCE+comp & 6.42 & 6.80 & 5.85 & 5.65 & 5.90 \\\\\nKL-only & 7.05 & 7.35 & 6.65 & 6.55 & 6.85 \\\\\nSPON+KL & 7.12 & 7.40 & 6.75 & 6.65 & 6.95 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only (7.05) is within 0.16 of dense (7.21)---within the GPT-4o judge's scoring noise floor.\nBCE+compensation (6.42) shows severe degradation on reasoning ($-$1.00) and math ($-$1.15), tasks most sensitive to output distribution fidelity.\nSPON+KL (7.12) nearly recovers dense-level performance across all categories.\n\n% ------------------------------------------------------------\n\\subsection{RULER Synthetic Diagnostics}\n\\label{sec:ruler}\n\nTable~\\ref{tab:ruler} provides fine-grained diagnostics on RULER synthetic tasks at 4K and 16K contexts.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RULER synthetic evaluation at 4K and 16K context lengths.}\n\\label{tab:ruler}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Task} & \\textbf{Ctx} & \\textbf{Dense} & \\textbf{KL} & \\textbf{BCE+c} & \\textbf{S+KL} \\\\\n\\midrule\nNeedle & 4K & 99.2 & 98.0 & 94.5 & 98.5 \\\\\nNeedle & 16K & 96.8 & 94.5 & 86.2 & 95.8 \\\\\nMulti-key & 4K & 93.5 & 91.2 & 83.8 & 92.4 \\\\\nMulti-key & 16K & 84.1 & 82.4 & 72.1 & 83.5 \\\\\nVar-track & 4K & 92.8 & 92.1 & 83.9 & 92.5 \\\\\nVar-track & 16K & 84.5 & 81.3 & 76.5 & 83.2 \\\\\n\\midrule\n\\textbf{Average} & \\textbf{4K} & \\textbf{95.2} & \\textbf{93.8} & \\textbf{87.4} & \\textbf{94.5} \\\\\n\\textbf{Average} & \\textbf{16K} & \\textbf{88.5} & \\textbf{86.1} & \\textbf{78.3} & \\textbf{87.2} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only's context-length degradation pattern (4K$\\to$16K: $-$7.7) closely tracks dense ($-$6.7), while BCE+compensation degrades more steeply ($-$9.1).\nMulti-key retrieval shows the largest differentiation at 16K (KL 82.4 vs.\\ BCE+comp 72.1), consistent with this task's sensitivity to joint neuron interactions---simultaneous retrieval of multiple scattered facts requires precise FFN activation patterns.\n\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Two-dimensional taxonomy.}\nOur results populate a two-axis taxonomy of sparsity correction methods: \\emph{correction granularity} (static $\\to$ per-layer $\\to$ per-token) $\\times$ \\emph{training signal coupling} (decomposed/BCE $\\to$ intermediate/MSE $\\to$ coupled/KL).\nPrior work fills specific cells---SPON (static, KL), ShadowLLM (per-layer, MSE), FastForward (per-token, BCE)---while our KL-only method fills the (per-token, KL) cell, which proves to be the Pareto-optimal configuration.\n\n\\paragraph{Practical implications.}\nEliminating compensation networks simplifies the inference pipeline: no additional parameters to load, no per-layer GEMV, and a smaller memory footprint.\nFor Llama~3.1~8B, this means 256\\,MB fewer parameters and 1.8\\,ms/token lower latency, with strictly better quality.\nThe SPON+KL variant adds only 1\\,MB (static biases) for a further 1.22 PPL improvement.\n\n\\paragraph{Limitations.}\nWe evaluate on 7--8B parameter models; scaling behavior at 70B+ remains to be verified.\nThe quadratic scaling prediction is confirmed over $s \\in [0.3, 0.6]$ but extrapolation beyond 60\\% needs additional data.\nKL training requires a teacher forward pass per step ($3.2\\times$ per-step cost), though the total training time is modest (4.2 hours on a single GPU for 1000 steps).\n\n% ============================================================\n\\section{Conclusion}\n\nWe have shown that output-distribution distillation via KL divergence categorically dominates BCE-based training for contextual activation sparsity prediction in SwiGLU LLMs, eliminating the need for compensation networks.\nThe advantage traces to a fundamental difference in gradient structure: KL's coupled gradients capture joint neuron interactions that BCE's factorized gradients miss, with the quality gap scaling quadratically in sparsity ($R^2 = 0.97$).\nThe resulting method is simultaneously simpler (no compensation network), smaller (24\\,MB vs.\\ 280\\,MB), faster (12.0 vs.\\ 13.8\\,ms/token), and better (9.20 vs.\\ 18.64 PPL) than the BCE+compensation alternative.\nCombined with SPON's static bias correction, the modular decomposition achieves 7.98 PPL---within 30\\% of dense---with near-perfect additivity.\n\n% ============================================================\n\\bibliography{custom}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Shazeer, 2020]{shazeer2020glu}\nNoam Shazeer. 2020.\n\\newblock {GLU} Variants Improve Transformer.\n\\newblock {\\em arXiv preprint arXiv:2002.05202}.\n\n\\bibitem[Liu et~al., 2024]{liu2024teal}\nYixin Liu, Haotian Ye, Lei Li, and Hao Peng. 2024.\n\\newblock {TEAL}: Token-wise Efficient Activation sparsity for {LLM}s.\n\\newblock In {\\em Proceedings of NeurIPS}.\n\n\\bibitem[Shen et~al., 2024]{shen2024wina}\nZhihang Shen, et~al. 2024.\n\\newblock {WINA}: Weight-Informed Neuron Activation for accelerating large language model inference.\n\\newblock {\\em arXiv preprint arXiv:2410.xxxx}.\n\n\\bibitem[Zhang et~al., 2024]{zhang2024rsparse}\nTianyu Zhang, et~al. 2024.\n\\newblock {R-Sparse}: Rank-Aware Activation Sparsity for efficient {LLM} inference.\n\\newblock {\\em arXiv preprint arXiv:2410.xxxx}.\n\n\\bibitem[Wang et~al., 2024]{wang2024fastforward}\nTao Wang, et~al. 2024.\n\\newblock {FastForward}: Learned sparsity prediction with compensation for efficient {LLM} inference.\n\\newblock {\\em arXiv preprint arXiv:2405.xxxx}.\n\n\\bibitem[Zhou et~al., 2024]{zhou2024spon}\nYongqi Zhou, et~al. 2024.\n\\newblock {SPON}: Static-correction-based sparsity optimization for language models via {KL} distillation.\n\\newblock {\\em arXiv preprint arXiv:2406.xxxx}.\n\n\\bibitem[Chen et~al., 2024]{chen2024shadowllm}\nZheng Chen, et~al. 2024.\n\\newblock {ShadowLLM}: Predictor-based contextual sparsity for large language models.\n\\newblock {\\em arXiv preprint arXiv:2406.xxxx}.\n\n\\bibitem[Hinton et~al., 2015]{hinton2015distilling}\nGeoffrey Hinton, Oriol Vinyals, and Jeff Dean. 2015.\n\\newblock Distilling the Knowledge in a Neural Network.\n\\newblock {\\em arXiv preprint arXiv:1503.02531}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "cc69d9f4-3c9d-4a57-a485-c27a10fd3317",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_sw…",
  "leafUuid": "4ca840d7-2524-45eb-84aa-9ce11a08a1a0",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate distillation sparse SwiGLU research paper",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb"
}
```

---

### Tool call

_source line 22 · 2026-05-15T17:29:58.385Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017wW5PCWycPJ933bQLxq3GC`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ca840d7-2524-45eb-84aa-9ce11a08a1a0",
  "isSidechain": false,
  "requestId": "req_011Cb4kWTqc7yzcaStmNooPF",
  "type": "assistant",
  "uuid": "8831b70b-7563-4441-86a1-19b8d4aa78fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCh6F1TcpE1QnTUbNrTuU2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12779,
      "cache_read_input_tokens": 43250,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 43250,
          "cache_creation_input_tokens": 12779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12779
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

_source line 23 · 2026-05-15T17:29:58.571Z_

<details><summary>↩ Tool result · reported error · `toolu_017wW5PCWycPJ933bQLxq3GC`</summary>

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
  "parentUuid": "8831b70b-7563-4441-86a1-19b8d4aa78fa",
  "isSidechain": false,
  "promptId": "4324b22a-92db-42ef-a974-2006388d7cce",
  "type": "user",
  "uuid": "0f55d8c6-0f7b-4c4c-a06c-838ceb7e4a8f",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `emnlp2023.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "8831b70b-7563-4441-86a1-19b8d4aa78fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-15T17:30:01.509Z_

<details><summary>Logged reasoning block</summary>

```text
The emnlp2023.sty file is not available. Let me switch to a standard article class instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f55d8c6-0f7b-4c4c-a06c-838ceb7e4a8f",
  "isSidechain": false,
  "requestId": "req_011Cb4kWkaRYc51pJvLeLAFF",
  "type": "assistant",
  "uuid": "0747c0a0-75a7-46cd-a22a-aa65924faf9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146rU1nr3QKT9kuqtZM3ZTQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 478,
      "cache_read_input_tokens": 56029,
      "output_tokens": 457,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 478,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 457,
          "cache_read_input_tokens": 56029,
          "cache_creation_input_tokens": 478,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 478
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

_source line 25 · 2026-05-15T17:30:02.505Z_

Need to fix the style package. I'll switch to a standard article class since `emnlp2023.sty` isn't installed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0747c0a0-75a7-46cd-a22a-aa65924faf9f",
  "isSidechain": false,
  "requestId": "req_011Cb4kWkaRYc51pJvLeLAFF",
  "type": "assistant",
  "uuid": "87b4804c-6845-45ac-8953-b02f1ada6063",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146rU1nr3QKT9kuqtZM3ZTQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 478,
      "cache_read_input_tokens": 56029,
      "output_tokens": 457,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 478,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 457,
          "cache_read_input_tokens": 56029,
          "cache_creation_input_tokens": 478,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 478
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

_source line 26 · 2026-05-15T17:30:05.529Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01R84dLMAo1tiL7JqbhGdLqm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper.tex",
  "old_string": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{array}\n\\usepackage{xcolor}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{array}\n\\usepackage{xcolor}\n\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87b4804c-6845-45ac-8953-b02f1ada6063",
  "isSidechain": false,
  "requestId": "req_011Cb4kWkaRYc51pJvLeLAFF",
  "type": "assistant",
  "uuid": "871da314-a817-454e-b845-8d7834ea1e6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146rU1nr3QKT9kuqtZM3ZTQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 478,
      "cache_read_input_tokens": 56029,
      "output_tokens": 457,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 478,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 457,
          "cache_read_input_tokens": 56029,
          "cache_creation_input_tokens": 478,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 478
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

_source line 27 · 2026-05-15T17:30:05.583Z_

<details><summary>↩ Tool result · `toolu_01R84dLMAo1tiL7JqbhGdLqm`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "871da314-a817-454e-b845-8d7834ea1e6e",
  "isSidechain": false,
  "promptId": "4324b22a-92db-42ef-a974-2006388d7cce",
  "type": "user",
  "uuid": "da360cae-776a-432a-8f3a-646f3b49c5ba",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper.tex",
    "oldString": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{array}\n\\usepackage{xcolor}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{array}\n\\usepackage{xcolor}\n\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          "-\\documentclass[11pt]{article}",
          "-\\usepackage[hyperref]{emnlp2023}",
          "+\\documentclass[11pt,a4paper]{article}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{amsmath}"
        ]
      },
      {
        "oldStart": 9,
        "oldLines": 6,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " \\usepackage{graphicx}",
          " \\usepackage{array}",
          " \\usepackage{xcolor}",
          "+\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}",
          " ",
          " \\title{Output-Distribution Distillation Makes Compensation Networks Obsolete\\\\for SwiGLU Activation Sparsity}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "871da314-a817-454e-b845-8d7834ea1e6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T17:30:09.119Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HMNnsc49WwAueNpdVzEP1G`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da360cae-776a-432a-8f3a-646f3b49c5ba",
  "isSidechain": false,
  "requestId": "req_011Cb4kXGWkE1zVYxu9xpghy",
  "type": "assistant",
  "uuid": "354d5596-4c96-4ce2-9a8d-dbc23f82c6ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyeRvB4B2pb9mCVtbdXyfM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 545,
      "cache_read_input_tokens": 56507,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 545,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 56507,
          "cache_creation_input_tokens": 545,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 545
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

_source line 29 · 2026-05-15T17:30:10.297Z_

<details><summary>↩ Tool result · `toolu_01HMNnsc49WwAueNpdVzEP1G`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (8.91808pt too wide) in paragraph at lines 23--30
[]\OT1/ptm/m/n/10 Activation spar-sity in SwiGLU-based large lan-guage mod-els 
en-ables sig-nif-i-cant in-fer-ence speedups

LaTeX Warning: Citation `shazeer2020glu' on page 1 undefined on input line 35.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)

LaTeX Warning: Reference `sec:ablation' on page 2 undefined on input line 53.


LaTeX Warning: Reference `sec:fullbench' on page 2 undefined on input line 53.


Overfull \hbox (37.84915pt too wide) in paragraph at lines 53--54
[]\OT1/ptm/m/n/10.95 We demon-strate that KL-trained con-tex-tual spar-sity pre
-dic-tors cat-e-gor-i-cally dom-i-nate BCE+compensation:

LaTeX Warning: Reference `sec:composition' on page 2 undefined on input line 54
.


LaTeX Warning: Reference `sec:scaling' on page 2 undefined on input line 55.


LaTeX Warning: Citation `liu2024teal' on page 2 undefined on input line 62.


LaTeX Warning: Citation `shen2024wina' on page 2 undefined on input line 63.


LaTeX Warning: Citation `zhang2024rsparse' on page 2 undefined on input line 64
.


LaTeX Warning: Citation `wang2024fastforward' on page 2 undefined on input line
 68.


LaTeX Warning: Citation `zhou2024spon' on page 2 undefined on input line 69.


LaTeX Warning: Citation `chen2024shadowllm' on page 2 undefined on input line 7
0.


LaTeX Warning: Citation `hinton2015distilling' on page 2 undefined on input lin
e 73.

[2]

LaTeX Warning: Reference `tab:ablation' on page 3 undefined on input line 155.

[3]

LaTeX Warning: Reference `tab:ste' on page 4 undefined on input line 185.


LaTeX Warning: Reference `tab:isocompute' on page 4 undefined on input line 211
.


LaTeX Warning: Reference `tab:hierarchy' on page 4 undefined on input line 236.



LaTeX Warning: Reference `tab:spon' on page 4 undefined on input line 266.

[4]

LaTeX Warning: Reference `tab:composition' on page 5 undefined on input line 29
6.


LaTeX Warning: Reference `tab:fullbench' on page 5 undefined on input line 324.



LaTeX Warning: Reference `tab:latency' on page 5 undefined on input line 352.


Overfull \hbox (1.4517pt too wide) in paragraph at lines 373--376
\OT1/ptm/m/n/10.95 la-tency (12.0 vs. 13.8ms/token), and 10$\OMS/cmsy/m/n/10.95
 ^^B$ \OT1/ptm/m/n/10.95 fewer ad-di-tional pa-ram-e-ters (24 vs. 280MB). The 1
.8ms/token

LaTeX Warning: Reference `tab:sweep' on page 5 undefined on input line 382.

[5]

LaTeX Warning: Reference `tab:longbench' on page 6 undefined on input line 459.



LaTeX Warning: Reference `tab:mtbench' on page 6 undefined on input line 489.

[6]

LaTeX Warning: Reference `tab:ruler' on page 7 undefined on input line 518.


Overfull \hbox (10.87776pt too wide) in paragraph at lines 549--551
\OT1/ptm/m/n/10.95 ods: \OT1/ptm/m/it/10.95 cor-rec-tion gran-u-lar-ity \OT1/pt
m/m/n/10.95 (static $\OMS/cmsy/m/n/10.95 !$ \OT1/ptm/m/n/10.95 per-layer $\OMS/
cmsy/m/n/10.95 !$ \OT1/ptm/m/n/10.95 per-token) $\OMS/cmsy/m/n/10.95 ^^B$ \OT1/
ptm/m/it/10.95 train-ing sig-nal cou-pling \OT1/ptm/m/n/10.95 (de-com-posed/BCE

[7]
No file paper.bbl.

Underfull \hbox (badness 1931) in paragraph at lines 576--579
[]\OT1/ptm/m/n/10.95 Noam Shazeer. 2020.  GLU Vari-ants Im-prove Trans-former. 
 \OT1/ptm/m/it/10.95 arXiv preprint
[8] [9] [10] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmbx7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi
b10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/u
rw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8
a.pfb>
Output written on paper.pdf (10 pages, 206118 bytes).
Transcript written on paper.log.
 \OT1/ptm/m/it/10.95 arXiv preprint
[8] [9] [10] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmbx7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi
b10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/u
rw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8
a.pfb>
Output written on paper.pdf (10 pages, 209055 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "354d5596-4c96-4ce2-9a8d-dbc23f82c6ca",
  "isSidechain": false,
  "promptId": "4324b22a-92db-42ef-a974-2006388d7cce",
  "type": "user",
  "uuid": "10752378-5c54-4f3c-a1ad-ed0ee17da26f",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (8.91808pt too wide) in paragraph at lines 23--30\n[]\\OT1/ptm/m/n/10 Activation spar-sity in SwiGLU-based large lan-guage mod-els \nen-ables sig-nif-i-cant in-fer-ence speedups\n\nLaTeX Warning: Citation `shazeer2020glu' on page 1 undefined on input line 35.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n\nLaTeX Warning: Reference `sec:ablation' on page 2 undefined on input line 53.\n\n\nLaTeX Warning: Reference `sec:fullbench' on page 2 undefined on input line 53.\n\n\nOverfull \\hbox (37.84915pt too wide) in paragraph at lines 53--54\n[]\\OT1/ptm/m/n/10.95 We demon-strate that KL-trained con-tex-tual spar-sity pre\n-dic-tors cat-e-gor-i-cally dom-i-nate BCE+compensation:\n\nLaTeX Warning: Reference `sec:composition' on page 2 undefined on input line 54\n.\n\n\nLaTeX Warning: Reference `sec:scaling' on page 2 undefined on input line 55.\n\n\nLaTeX Warning: Citation `liu2024teal' on page 2 undefined on input line 62.\n\n\nLaTeX Warning: Citation `shen2024wina' on page 2 undefined on input line 63.\n\n\nLaTeX Warning: Citation `zhang2024rsparse' on page 2 undefined on input line 64\n.\n\n\nLaTeX Warning: Citation `wang2024fastforward' on page 2 undefined on input line\n 68.\n\n\nLaTeX Warning: Citation `zhou2024spon' on page 2 undefined on input line 69.\n\n\nLaTeX Warning: Citation `chen2024shadowllm' on page 2 undefined on input line 7\n0.\n\n\nLaTeX Warning: Citation `hinton2015distilling' on page 2 undefined on input lin\ne 73.\n\n[2]\n\nLaTeX Warning: Reference `tab:ablation' on page 3 undefined on input line 155.\n\n[3]\n\nLaTeX Warning: Reference `tab:ste' on page 4 undefined on input line 185.\n\n\nLaTeX Warning: Reference `tab:isocompute' on page 4 undefined on input line 211\n.\n\n\nLaTeX Warning: Reference `tab:hierarchy' on page 4 undefined on input line 236.\n\n\n\nLaTeX Warning: Reference `tab:spon' on page 4 undefined on input line 266.\n\n[4]\n\nLaTeX Warning: Reference `tab:composition' on page 5 undefined on input line 29\n6.\n\n\nLaTeX Warning: Reference `tab:fullbench' on page 5 undefined on input line 324.\n\n\n\nLaTeX Warning: Reference `tab:latency' on page 5 undefined on input line 352.\n\n\nOverfull \\hbox (1.4517pt too wide) in paragraph at lines 373--376\n\\OT1/ptm/m/n/10.95 la-tency (12.0 vs. 13.8ms/token), and 10$\\OMS/cmsy/m/n/10.95\n ^^B$ \\OT1/ptm/m/n/10.95 fewer ad-di-tional pa-ram-e-ters (24 vs. 280MB). The 1\n.8ms/token\n\nLaTeX Warning: Reference `tab:sweep' on page 5 undefined on input line 382.\n\n[5]\n\nLaTeX Warning: Reference `tab:longbench' on page 6 undefined on input line 459.\n\n\n\nLaTeX Warning: Reference `tab:mtbench' on page 6 undefined on input line 489.\n\n[6]\n\nLaTeX Warning: Reference `tab:ruler' on page 7 undefined on input line 518.\n\n\nOverfull \\hbox (10.87776pt too wide) in paragraph at lines 549--551\n\\OT1/ptm/m/n/10.95 ods: \\OT1/ptm/m/it/10.95 cor-rec-tion gran-u-lar-ity \\OT1/pt\nm/m/n/10.95 (static $\\OMS/cmsy/m/n/10.95 !$ \\OT1/ptm/m/n/10.95 per-layer $\\OMS/\ncmsy/m/n/10.95 !$ \\OT1/ptm/m/n/10.95 per-token) $\\OMS/cmsy/m/n/10.95 ^^B$ \\OT1/\nptm/m/it/10.95 train-ing sig-nal cou-pling \\OT1/ptm/m/n/10.95 (de-com-posed/BCE\n\n[7]\nNo file paper.bbl.\n\nUnderfull \\hbox (badness 1931) in paragraph at lines 576--579\n[]\\OT1/ptm/m/n/10.95 Noam Shazeer. 2020.  GLU Vari-ants Im-prove Trans-former. \n \\OT1/ptm/m/it/10.95 arXiv preprint\n[8] [9] [10] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmbx7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi\nb10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/u\nrw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8\na.pfb>\nOutput written on paper.pdf (10 pages, 206118 bytes).\nTranscript written on paper.log.\n \\OT1/ptm/m/it/10.95 arXiv preprint\n[8] [9] [10] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmbx7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi\nb10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/u\nrw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8\na.pfb>\nOutput written on paper.pdf (10 pages, 209055 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "354d5596-4c96-4ce2-9a8d-dbc23f82c6ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-15T17:30:10.300Z_

```json
{
  "parentUuid": "10752378-5c54-4f3c-a1ad-ed0ee17da26f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "92e6795e-9525-4d50-89dd-c61f1f3b305d",
  "timestamp": "2026-05-15T17:30:10.300Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_sw…",
  "leafUuid": "92e6795e-9525-4d50-89dd-c61f1f3b305d",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate distillation sparse SwiGLU research paper",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb"
}
```

---

### Assistant

_source line 33 · 2026-05-15T17:30:13.077Z_

PDF compiled successfully (10 pages, 209 KB). Let me verify the output file exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92e6795e-9525-4d50-89dd-c61f1f3b305d",
  "isSidechain": false,
  "requestId": "req_011Cb4kXcbEZeQCK3YmhDDJ8",
  "type": "assistant",
  "uuid": "71f1ea3d-94df-4aa1-b22c-617883a30bdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8L4BPeiJyFVgfcyJSGReT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4945,
      "cache_read_input_tokens": 57052,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4945,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 57052,
          "cache_creation_input_tokens": 4945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4945
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

_source line 34 · 2026-05-15T17:30:15.334Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01S1ZDJX7sG8vggSvyZxuZeg`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper.pdf",
  "description": "Verify PDF output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71f1ea3d-94df-4aa1-b22c-617883a30bdd",
  "isSidechain": false,
  "requestId": "req_011Cb4kXcbEZeQCK3YmhDDJ8",
  "type": "assistant",
  "uuid": "d4d23e34-e935-4191-89fc-30c276d7a36d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8L4BPeiJyFVgfcyJSGReT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4945,
      "cache_read_input_tokens": 57052,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4945,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 57052,
          "cache_creation_input_tokens": 4945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4945
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

_source line 35 · 2026-05-15T17:30:15.381Z_

<details><summary>↩ Tool result · `toolu_01S1ZDJX7sG8vggSvyZxuZeg`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 209055 May 15 17:30 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4d23e34-e935-4191-89fc-30c276d7a36d",
  "isSidechain": false,
  "promptId": "4324b22a-92db-42ef-a974-2006388d7cce",
  "type": "user",
  "uuid": "d6f8aa7b-3b1c-4a08-9643-7dbf2e979b53",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 209055 May 15 17:30 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d4d23e34-e935-4191-89fc-30c276d7a36d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-15T17:30:25.682Z_

论文已生成。

`paper.tex` (10页) 写入 `best/` 目录，PDF编译成功。覆盖了全部11个实验：

- **Table 1**: Four-condition ablation (KL-only 9.20 vs BCE+comp 18.64)
- **Table 2**: STE baseline (loss vs relaxation归因, 97% from KL)
- **Table 3**: Iso-compute comparison (BCE extended仍差16.21 PPL)
- **Table 4**: SPON QA benchmark validation
- **Table 5**: SPON+KL composition additivity (6.8% interaction residual)
- **Table 6**: Training-free baselines hierarchy
- **Table 7**: Full benchmark suite (5 downstream tasks)
- **Table 8**: Inference efficiency Pareto analysis
- **Table 9/9b**: 7-level sparsity sweep (quadratic scaling R²=0.97)
- **Table 10/10b**: Mistral-7B cross-architecture validation
- **Table 11**: LongBench long-context evaluation
- **Table 12**: MT-Bench multi-turn evaluation
- **Table 13**: RULER synthetic diagnostics

所有数字直接取自 `experiment_data.json`，无编造。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6f8aa7b-3b1c-4a08-9643-7dbf2e979b53",
  "isSidechain": false,
  "requestId": "req_011Cb4kXzLByaFqJQAv3n349",
  "type": "assistant",
  "uuid": "a6260d43-35b1-45e9-96de-080fad934c16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016L7BJRjEWbdrZN4RPDJL9F",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 61997,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 235,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 325,
          "cache_read_input_tokens": 61997,
          "cache_creation_input_tokens": 235,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 235
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_sw…",
  "leafUuid": "a6260d43-35b1-45e9-96de-080fad934c16",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate distillation sparse SwiGLU research paper",
  "sessionId": "a7bb3824-6271-4640-950f-c2fc0148d5eb"
}
```

---
