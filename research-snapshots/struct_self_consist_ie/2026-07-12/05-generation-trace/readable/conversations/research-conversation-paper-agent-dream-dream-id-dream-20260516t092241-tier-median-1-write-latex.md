# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/c8502501-34ec-4d3f-9eb5-b04016e60696.jsonl`
- **Structured JSON:** [`ea8c07877c7a5d9ca5dd.json`](../../sessions/ea/ea8c07877c7a5d9ca5dd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T09:54:19.044Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T09:54:19.044Z",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/experiment_data.json`（先 Read 此文件）\n- Venue：EMNLP 2026 Main Conference\n- Narrative guidance：将 'capability trap' 从 'structural inevitability' 弱化为 'primary contributing factor alongside fine-tuning regime'。两个 failure mechanisms (degeneracy + LP compression) 仍完全成立——它们的证据全部来自已完成实验，不受新实验影响。调整 claims 强度：'universally fail' → 'predominantly fail across tested configurations'。LoRA ablation 变为 nuanced finding：'output convergence is driven by capability AND fine-tuning intensity, with capability as the dominant factor.' 将 QE evaluation framework (Claim 2) 提升为 co-primary contribution。标题微调为 'Strong Predictors, Weak Selectors: Diagnosing Why...' 强调诊断而非绝对性。目标：EMNLP Main（adjusted claims）或 strong Findings。\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T09:54:19.048Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T09:54:19.048Z",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696"
}
```

---

## Round 1

38 recorded events

### User

_source line 3 · 2026-05-16T09:54:19.071Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/experiment_data.json`（先 Read 此文件）
- Venue：EMNLP 2026 Main Conference
- Narrative guidance：将 'capability trap' 从 'structural inevitability' 弱化为 'primary contributing factor alongside fine-tuning regime'。两个 failure mechanisms (degeneracy + LP compression) 仍完全成立——它们的证据全部来自已完成实验，不受新实验影响。调整 claims 强度：'universally fail' → 'predominantly fail across tested configurations'。LoRA ablation 变为 nuanced finding：'output convergence is driven by capability AND fine-tuning intensity, with capability as the dominant factor.' 将 QE evaluation framework (Claim 2) 提升为 co-primary contribution。标题微调为 'Strong Predictors, Weak Selectors: Diagnosing Why...' 强调诊断而非绝对性。目标：EMNLP Main（adjusted claims）或 strong Findings。
- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "1cdd1fca-2b73-4d1a-a515-3ada1bf62a4e",
  "type": "user",
  "uuid": "ff4d6e1e-d6f4-4ba8-9424-eba801fac817",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T09:54:19.071Z_

```json
{
  "parentUuid": "ff4d6e1e-d6f4-4ba8-9424-eba801fac817",
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
  "uuid": "7f609f35-6d99-499d-b291-0e48ca59b9c9",
  "timestamp": "2026-05-16T09:54:19.071Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T09:54:19.071Z_

```json
{
  "parentUuid": "7f609f35-6d99-499d-b291-0e48ca59b9c9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0e06f51d-5187-4769-8c53-343abb01297a",
  "timestamp": "2026-05-16T09:54:19.071Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
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
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696"
}
```

---

### Assistant

_source line 7 · 2026-05-16T09:54:22.056Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the experiment data and paper framing files to understand what I need to write.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e06f51d-5187-4769-8c53-343abb01297a",
  "isSidechain": false,
  "requestId": "req_011Cb63aMcePcS9PjUALeAAb",
  "type": "assistant",
  "uuid": "b0277e17-a59a-418b-bfaa-899796e7f149",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5cnLB4vUXy3mwjoPLLjrk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11285,
      "cache_read_input_tokens": 11841,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11285
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

_source line 8 · 2026-05-16T09:54:22.684Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BeQBnpV28qqWC4686XC2jx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0277e17-a59a-418b-bfaa-899796e7f149",
  "isSidechain": false,
  "requestId": "req_011Cb63aMcePcS9PjUALeAAb",
  "type": "assistant",
  "uuid": "afdf4272-8dd2-4cde-8332-27a5ddb39d54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5cnLB4vUXy3mwjoPLLjrk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11285,
      "cache_read_input_tokens": 11841,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11285
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

_source line 9 · 2026-05-16T09:54:22.958Z_

<details><summary>↩ Tool result · `toolu_01BeQBnpV28qqWC4686XC2jx`</summary>

```text
1	[
2	  {
3	    "name": "fewnerd_smoke",
4	    "description": "Few-NERD INTRA coarse 8-type, 1-epoch LoRA fine-tune + 200-instance N=8 pilot. Gate for full run.",
5	    "results": {
6	      "train_loss_1epoch": 0.15,
7	      "eval_loss_1epoch": 0.12,
8	      "greedy_f1_200inst": 0.78,
9	      "parse_rate": 0.998,
10	      "pilot_sj_rho_full": 0.3,
11	      "pilot_degeneracy_rate": 0.22,
12	      "pilot_oracle_f1": 0.86,
13	      "pilot_headroom_pp": 8.0,
14	      "inference_time_200inst_minutes": 12,
15	      "n_entity_types": 8,
16	      "sample_f1_pct_zero": 8.5
17	    },
18	    "tables": [
19	      {
20	        "name": "Table: Few-NERD Smoke Test Summary",
21	        "columns": [
22	          "Metric",
23	          "Value"
24	        ],
25	        "rows": [
26	          [
27	            "Training loss (1 epoch)",
28	            "0.150"
29	          ],
30	          [
31	            "Greedy NER F1 (200 inst)",
32	            "0.780"
33	          ],
34	          [
35	            "Oracle NER F1",
36	            "0.860"
37	          ],
38	          [
39	            "Headroom",
40	            "8.0pp"
41	          ],
42	          [
43	            "Parse rate",
44	            "99.8%"
45	          ],
46	          [
47	            "Degeneracy rate (pilot)",
48	            "22%"
49	          ],
50	          [
51	            "SJ ρ (pilot)",
52	            "0.30"
53	          ]
54	        ]
55	      }
56	    ],
57	    "figures": [],
58	    "analysis": "Smoke test PASS。模型成功学会 Few-NERD 格式和 8 类实体标注。Greedy F1=0.78 介于 SciERC（0.66）和 CoNLL（0.91）之间，符合 Few-NERD 的中等难度定位。Degeneracy 初步估计 ~22%，低于 capability trap 线性外推的预测值（~35-40%），暗示 median tier 的'部分确认但不完美拟合'结论。Pipeline validated，proceed to exp-021。\n\nFew-NERD INTRA coarse（8类通用实体：Person, Organization, Location, Building, Product, Event, Art, Other）比 SciERC 更标准化但比 CoNLL 更细粒度。1-epoch LoRA 已足够让 Qwen3-8B 学会格式和基本类型映射（类似 SciERC ft_001 在 1 epoch 后 NER F1=0.60）。Few-NERD 训练集大（~66K samples），1 epoch 足以收敛基本模式。Greedy F1=0.78 符合 median 范围 [0.75, 0.85] 的下半段，因为只有 1 epoch。Degeneracy 0.22 在 pilot（200 inst）上初步可见但 CI 宽——这个 pilot 主要验证 pipeline 可行性，不做结论。"
59	  },
60	  {
61	    "name": "fewnerd_full",
62	    "description": "Few-NERD 3-epoch LoRA + full test set N=8, 3 seeds. 5 signals + degeneracy + selection.",
63	    "results": {
64	      "train_loss_3epoch": 0.065,
65	      "eval_loss_3epoch": 0.078,
66	      "greedy_f1": 0.812,
67	      "oracle_f1": 0.895,
68	      "oracle_headroom_pp": 8.3,
69	      "n_test_instances": 1500,
70	      "n_valid_after_gold_filter": 1380,
71	      "parse_rate": 0.999,
72	      "degeneracy_rate": 0.26,
73	      "degeneracy_rate_3seed_mean": 0.25,
74	      "degeneracy_rate_3seed_sd": 0.018,
75	      "sj_rho_full": 0.33,
76	      "fk_rho_full": 0.28,
77	      "logprob_rho_full": 0.25,
78	      "em_rho_full": 0.35,
79	      "voting_conf_rho_full": 0.36,
80	      "sj_auroc_full": 0.72,
81	      "em_auroc_full": 0.78,
82	      "voting_conf_auroc_full": 0.73,
83	      "logprob_auroc_full": 0.68,
84	      "sj_rho_cond": 0.31,
85	      "em_rho_cond": 0.38,
86	      "voting_conf_rho_cond": 0.33,
87	      "sj_rho_3seed_mean": 0.32,
88	      "sj_rho_3seed_sd": 0.025,
89	      "selection_f1_greedy": 0.812,
90	      "selection_f1_sj": 0.813,
91	      "selection_f1_logprob": 0.814,
92	      "selection_f1_voting_conf": 0.811,
93	      "selection_f1_random": 0.798,
94	      "selection_f1_oracle": 0.895,
95	      "selection_gap_best_minus_greedy_pp": 0.2,
96	      "selection_bootstrap_ci_95_low": -0.8,
97	      "selection_bootstrap_ci_95_high": 1.2,
98	      "selection_permutation_p": 0.42,
99	      "capability_trap_f1_vs_degeneracy_r2_with_fewnerd": 0.72,
100	      "capability_trap_monotonicity": true,
101	      "lp_within_instance_range_median": 0.038,
102	      "lp_tied_fraction": 0.31,
103	      "sample_f1_pct_zero": 6.2
104	    },
105	    "tables": [
106	      {
107	        "name": "Table: Few-NERD Full Results — QE Correlation (ρ, 3-seed mean±sd)",
108	        "columns": [
109	          "Signal",
110	          "NER ρ (full)",
111	          "NER ρ (cond)",
112	          "AUROC"
113	        ],
114	        "rows": [
115	          [
116	            "Voting_conf",
117	            "0.360±0.022",
118	            "0.330±0.028",
119	            "0.730"
120	          ],
121	          [
122	            "EM",
123	            "0.350±0.019",
124	            "0.380±0.024",
125	            "0.780"
126	          ],
127	          [
128	            "SJ",
129	            "0.320±0.025",
130	            "0.310±0.030",
131	            "0.720"
132	          ],
133	          [
134	            "FK",
135	            "0.280±0.020",
136	            "0.260±0.025",
137	            "0.660"
138	          ],
139	          [
140	            "Logprob",
141	            "0.250±0.018",
142	            "0.220±0.022",
143	            "0.680"
144	          ]
145	        ]
146	      },
147	      {
148	        "name": "Table: Few-NERD Selection F1 (N=8, T=1.0)",
149	        "columns": [
150	          "Method",
151	          "F1",
152	          "Δ vs greedy (pp)"
153	        ],
154	        "rows": [
155	          [
156	            "Oracle",
157	            "0.895",
158	            "+8.3"
159	          ],
160	          [
161	            "Logprob",
162	            "0.814",
163	            "+0.2"
164	          ],
165	          [
166	            "SJ",
167	            "0.813",
168	            "+0.1"
169	          ],
170	          [
171	            "Greedy (T=0)",
172	            "0.812",
173	            "—"
174	          ],
175	          [
176	            "Voting_conf",
177	            "0.811",
178	            "-0.1"
179	          ],
180	          [
181	            "Random",
182	            "0.798",
183	            "-1.4"
184	          ]
185	        ]
186	      },
187	      {
188	        "name": "Table: Capability Trap — Cross-Dataset Degeneracy",
189	        "columns": [
190	          "Dataset",
191	          "Greedy F1",
192	          "Degeneracy %",
193	          "Predicted %",
194	          "Residual"
195	        ],
196	        "rows": [
197	          [
198	            "CoNLL-2003",
199	            "0.912",
200	            "58%",
201	            "—",
202	            "—"
203	          ],
204	          [
205	            "Few-NERD",
206	            "0.812",
207	            "26%",
208	            "38%",
209	            "-12pp"
210	          ],
211	          [
212	            "SciERC",
213	            "0.663",
214	            "21%",
215	            "—",
216	            "—"
217	          ],
218	          [
219	            "WNUT-17",
220	            "0.523",
221	            "~0%",
222	            "—",
223	            "—"
224	          ]
225	        ]
226	      }
227	    ],
228	    "figures": [],
229	    "analysis": "Few-NERD 为 capability trap 提供 partial confirmation：degeneracy 单调性成立（F1 越高，degeneracy 越高），但 R² 从 3-point 的 0.95+ 下降到 4-point 的 0.72。这要求将 capability trap 从 'structural inevitability' 调整为 'primary contributing factor'，因为 task structure（类型数量、实体密度）引入了不可忽略的 residual。Selection 结果（+0.2pp, p=0.42）处于 median 定义的模糊区间——不显著优于 greedy，但也没有像 SciERC 那样 greedy 明确 dominate。这使得 'universally fail' 需弱化为 'predominantly fail'。QE signals 仍然有效（SJ ρ=0.32 > LP ρ=0.25），支撑 Claim 2 的 QE framework contribution。\n\n3-epoch fine-tune 使 greedy F1 从 smoke 的 0.78 提升到 0.812，对应 median 范围 [0.75,0.85] 的中部。Degeneracy rate 0.26 的关键逻辑：capability trap 预测在 F1=0.81 时 degeneracy 应~38%（CoNLL 0.91→58%, SciERC 0.66→21% 的线性外推），但实际只有 26%。原因：(1) Few-NERD 有 8 种实体类型（vs CoNLL 的 4 种），类型多样性提供更多变异维度，使得即使 overall F1 高，individual spans 仍有组合空间；(2) Few-NERD 实例更长/实体更密，per-instance 的 combinatorial space 抑制了完全 convergence。这就是 median 的核心信号：monotonicity 成立（F1 越高 degeneracy 越高），但 R²=0.72 而非 0.95——task structure（类型数、实体密度）是 residual variance 的来源。Selection gap +0.2pp 的逻辑：degeneracy 26% 介于 SciERC（21%，gap≈0）和 CoNLL（58%，gap≈0）之间，bootstrap p=0.42 说明完全不显著。信号排序 VC>EM>SJ>FK>LP 与 CoNLL 类似但 SJ-LP gap 更小（0.08 vs SciERC 的 0.15），因为 8 类系统的 LP 信号比 6 类科学文本更 informative。"
230	  },
231	  {
232	    "name": "3rd_seed_scierc",
233	    "description": "SciERC NER+RE N=8, seed=789. 第3个 seed 用于 Fisher combined p-value。",
234	    "results": {
235	      "ner_greedy_f1": 0.661,
236	      "ner_oracle_f1": 0.779,
237	      "ner_headroom_pp": 11.8,
238	      "ner_sj_rho_full": 0.372,
239	      "ner_fk_rho_full": 0.258,
240	      "ner_logprob_rho_full": 0.218,
241	      "ner_em_rho_full": 0.305,
242	      "ner_voting_conf_rho_full": 0.388,
243	      "ner_sj_auroc": 0.698,
244	      "ner_em_auroc": 0.755,
245	      "re_greedy_f1": 0.415,
246	      "re_oracle_f1": 0.582,
247	      "re_headroom_pp": 16.7,
248	      "re_sj_rho_full": 0.258,
249	      "re_fk_rho_full": 0.285,
250	      "re_logprob_rho_full": 0.242,
251	      "re_voting_conf_rho_full": 0.34,
252	      "re_sample_f1_pct_zero": 44.8,
253	      "re_lp_gt_sj": false,
254	      "re_sj_minus_lp_rho": 0.016,
255	      "ner_sj_rho_3seed_mean": 0.381,
256	      "ner_sj_rho_3seed_sd": 0.032,
257	      "re_sj_rho_3seed_mean": 0.261,
258	      "re_sj_rho_3seed_sd": 0.012,
259	      "re_lp_rho_3seed_mean": 0.268,
260	      "re_lp_rho_3seed_sd": 0.038,
261	      "fisher_combined_p_sj_gt_lp_ner": 0.028,
262	      "fisher_combined_p_sj_gt_lp_ner_significant": true,
263	      "fisher_combined_p_lp_gt_sj_re": 0.085,
264	      "fisher_combined_p_lp_gt_sj_re_significant": false,
265	      "selection_f1_greedy": 0.661,
266	      "selection_f1_logprob": 0.654,
267	      "selection_f1_sj": 0.651,
268	      "selection_f1_oracle": 0.779,
269	      "degeneracy_rate_ner": 0.23,
270	      "n_instances": 529,
271	      "parse_rate": 1.0
272	    },
273	    "tables": [
274	      {
275	        "name": "Table: 3-Seed SciERC NER ρ Stability",
276	        "columns": [
277	          "Signal",
278	          "Seed 42",
279	          "Seed 123",
280	          "Seed 789",
281	          "Mean",
282	          "SD"
283	        ],
284	        "rows": [
285	          [
286	            "SJ",
287	            "0.383",
288	            "0.384",
289	            "0.372",
290	            "0.381",
291	            "0.032"
292	          ],
293	          [
294	            "FK",
295	            "0.259",
296	            "0.266",
297	            "0.258",
298	            "0.261",
299	            "0.004"
300	          ],
301	          [
302	            "LP",
303	            "0.205",
304	            "0.226",
305	            "0.218",
306	            "0.216",
307	            "0.011"
308	          ],
309	          [
310	            "VC",
311	            "0.379",
312	            "0.407",
313	            "0.388",
314	            "0.391",
315	            "0.014"
316	          ],
317	          [
318	            "EM",
319	            "0.295",
320	            "0.299",
321	            "0.305",
322	            "0.300",
323	            "0.005"
324	          ]
325	        ]
326	      },
327	      {
328	        "name": "Table: 3-Seed SciERC RE ρ — LP vs SJ Ranking",
329	        "columns": [
330	          "Signal",
331	          "Seed 42",
332	          "Seed 123",
333	          "Seed 789",
334	          "Mean",
335	          "SD"
336	        ],
337	        "rows": [
338	          [
339	            "LP",
340	            "0.267",
341	            "0.300",
342	            "0.242",
343	            "0.270",
344	            "0.029"
345	          ],
346	          [
347	            "SJ",
348	            "0.250",
349	            "0.283",
350	            "0.258",
351	            "0.264",
352	            "0.017"
353	          ],
354	          [
355	            "LP>SJ?",
356	            "Yes (+0.017)",
357	            "Yes (+0.017)",
358	            "No (-0.016)",
359	            "—",
360	            "—"
361	          ]
362	        ]
363	      },
364	      {
365	        "name": "Table: Fisher Combined p-values (3 seeds)",
366	        "columns": [
367	          "Hypothesis",
368	          "Fisher χ²",
369	          "df",
370	          "p",
371	          "Significant?"
372	        ],
373	        "rows": [
374	          [
375	            "NER: SJ > LP",
376	            "14.2",
377	            "6",
378	            "0.028",
379	            "Yes (p<0.05)"
380	          ],
381	          [
382	            "RE: LP > SJ",
383	            "10.8",
384	            "6",
385	            "0.085",
386	            "No"
387	          ]
388	        ]
389	      }
390	    ],
391	    "figures": [],
392	    "analysis": "第3个 seed 确认 NER 结论完全稳定（SJ > LP, Fisher p=0.028）。RE 上 LP>SJ 的 ranking 在 seed 789 翻转（SJ 0.258 > LP 0.242），使得 3-seed Fisher p=0.085 未达显著水平。这是 median tier 的核心特征之一：RE signal ranking 不够 robust 以做 definitive claim。Paper 中需表述为 'LP tends to outperform structural signals on RE (2/3 seeds), likely due to binary dominance mechanism, though this advantage does not reach statistical significance across all random seeds (Fisher p=0.085).' Primary claims（capability trap、NER structural>surface、selection fails）在 3-seed 下完全稳定。\n\nSeed=789 的 NER 结果高度稳定（SJ ρ=0.372 vs 已有 seeds 0.383/0.384/0.360，3-seed SD=0.032 落入 median 范围 [0.02, 0.045]）。关键 median 特征在 RE：seed 789 上 SJ ρ=0.258 略高于 LP ρ=0.242，打破了 seeds 42/123 上 LP>SJ 的 pattern（seed42: LP 0.267 > SJ 0.250; seed123: LP 0.300 > SJ 0.283）。这使得 Fisher combined p for LP>SJ on RE = 0.085（不显著）。翻转原因：RE 的 zero-F1 rate 在不同 seeds 间波动（43-45%），seed=789 恰好有较少的 'complete failure' instances 进入 high-LP bin，削弱了 LP 的 binary classification 优势。NER 上 SJ>LP 的 Fisher p=0.028 仍然显著，支撑 'structural signals dominate for NER' 的结论。但 RE signal ranking 的不稳定性要求将 'LP>SJ for RE' 从 'definitive finding' 降级为 'tendency across most seeds'。"
393	  },
394	  {
395	    "name": "lora_rank8_ablation",
396	    "description": "LoRA rank=8 (vs baseline rank=16) fine-tune on SciERC + N=8 inference. Tests fine-tuning intensity vs capability as degeneracy driver.",
397	    "results": {
398	      "train_loss_5epoch": 0.095,
399	      "eval_loss_5epoch": 0.105,
400	      "ner_greedy_f1": 0.641,
401	      "ner_oracle_f1": 0.782,
402	      "ner_headroom_pp": 14.1,
403	      "degeneracy_rate_r8": 0.12,
404	      "degeneracy_rate_r16_baseline": 0.21,
405	      "degeneracy_delta_pp": 9.0,
406	      "ner_sj_rho_full": 0.365,
407	      "ner_fk_rho_full": 0.27,
408	      "ner_logprob_rho_full": 0.195,
409	      "ner_voting_conf_rho_full": 0.39,
410	      "ner_sj_auroc": 0.69,
411	      "selection_f1_greedy_r8": 0.641,
412	      "selection_f1_logprob_r8": 0.644,
413	      "selection_f1_sj_r8": 0.642,
414	      "selection_f1_oracle_r8": 0.782,
415	      "selection_gap_logprob_minus_greedy_pp": 0.3,
416	      "lp_within_instance_range_median_r8": 0.048,
417	      "lp_tied_fraction_r8": 0.14,
418	      "re_greedy_f1": 0.385,
419	      "re_oracle_f1": 0.568,
420	      "re_degeneracy_rate_r8": 0.08,
421	      "re_sample_f1_pct_zero": 48.2,
422	      "greedy_f1_delta_r8_minus_r16": -0.022,
423	      "sj_rho_delta_r8_minus_r16": 0.005,
424	      "headroom_delta_r8_minus_r16_pp": 3.0,
425	      "non_degen_selection_gap_pp": 2.1,
426	      "n_instances": 529,
427	      "parse_rate": 0.995
428	    },
429	    "tables": [
430	      {
431	        "name": "Table: LoRA Rank Ablation — Degeneracy & Performance",
432	        "columns": [
433	          "Metric",
434	          "Rank=16 (baseline)",
435	          "Rank=8",
436	          "Δ"
437	        ],
438	        "rows": [
439	          [
440	            "NER Greedy F1",
441	            "0.663",
442	            "0.641",
443	            "-2.2pp"
444	          ],
445	          [
446	            "NER Oracle F1",
447	            "0.776",
448	            "0.782",
449	            "+0.6pp"
450	          ],
451	          [
452	            "NER Headroom",
453	            "11.3pp",
454	            "14.1pp",
455	            "+2.8pp"
456	          ],
457	          [
458	            "NER Degeneracy %",
459	            "21%",
460	            "12%",
461	            "-9pp"
462	          ],
463	          [
464	            "LP range (median nats)",
465	            "0.041",
466	            "0.048",
467	            "+17%"
468	          ],
469	          [
470	            "LP tied fraction",
471	            "0.21",
472	            "0.14",
473	            "-7pp"
474	          ],
475	          [
476	            "NER SJ ρ",
477	            "0.383",
478	            "0.365",
479	            "-0.018"
480	          ],
481	          [
482	            "Best selection F1",
483	            "0.650 (LP)",
484	            "0.644 (LP)",
485	            "-0.6pp"
486	          ]
487	        ]
488	      },
489	      {
490	        "name": "Table: Degeneracy Attribution (NER)",
491	        "columns": [
492	          "Driver",
493	          "Predicted Δ degen",
494	          "Actual Δ degen",
495	          "Attribution %"
496	        ],
497	        "rows": [
498	          [
499	            "Capability (F1 drop 0.66→0.64)",
500	            "-2pp",
501	            "—",
502	            "22%"
503	          ],
504	          [
505	            "Fine-tuning intensity (rank 16→8)",
506	            "—",
507	            "-7pp",
508	            "78%"
509	          ],
510	          [
511	            "Total observed",
512	            "—",
513	            "-9pp",
514	            "100%"
515	          ]
516	        ]
517	      },
518	      {
519	        "name": "Table: Non-degenerate Subset Analysis (rank=8)",
520	        "columns": [
521	          "Subset",
522	          "n",
523	          "LP selection gap",
524	          "SJ selection gap"
525	        ],
526	        "rows": [
527	          [
528	            "All instances",
529	            "529",
530	            "+0.3pp",
531	            "+0.1pp"
532	          ],
533	          [
534	            "Non-degenerate only",
535	            "465",
536	            "+2.1pp",
537	            "+1.5pp"
538	          ],
539	          [
540	            "Non-degen, rank=16 baseline",
541	            "418",
542	            "+2.9pp (p=0.01)",
543	            "+1.8pp"
544	          ]
545	        ]
546	      }
547	    ],
548	    "figures": [],
549	    "analysis": "LoRA rank=8 ablation 是 median tier 的 defining experiment。Degeneracy 下降 9pp（从 21% 到 12%）中，capability drop（F1 -2.2pp）仅能解释约 2pp，剩余 7pp 必须归因于 fine-tuning intensity itself。这迫使论文承认 capability trap 不是 sole driver——fine-tuning regime 是 independent contributing factor。但关键上下文是：跨 dataset 的 degeneracy variation（CoNLL 58% vs SciERC 21% = 37pp range）远大于 rank ablation 的 9pp，所以 capability 仍是 'dominant factor'。Paper framing 调整为：'Output convergence is driven by model capability (primary, explaining cross-dataset variance) AND fine-tuning intensity (secondary, contributing 5-15pp within-dataset). The capability trap remains the unifying explanation for why test-time scaling provides diminishing returns as model quality improves.' Selection 仍然 fails 即使 degeneracy 降低，因为 LP compression 是 independent bottleneck（不随 LoRA rank 改变）。\n\nLoRA rank=8 的参数容量是 rank=16 的一半，模型 fine-tuning 强度更低。这导致两个效果：(1) greedy F1 略降（0.641 vs 0.663，-2.2pp），因为模型对 SciERC schema 的记忆不如 rank=16 完整；(2) 输出多样性更高，因为 lower-rank adaptation 保留了更多 base model 的 stochastic behavior，degeneracy 从 21% 降到 12%（-9pp，落入 median 范围 [5,15]）。关键逻辑：如果 degeneracy 纯粹由 capability 驱动，则 F1 降低应该已经自动解释 degeneracy 下降（按 capability trap curve：F1 从 0.66 降到 0.64 预测 degeneracy 从 21% 降到 ~19%，仅 -2pp）。但实际下降 9pp >> 2pp 的 capability-predicted 下降，说明 fine-tuning intensity 本身是 independent contributing factor。Median 解读：capability trap 解释了约 22% 的 degeneracy reduction（2/9），fine-tuning intensity 解释了剩余 78%。但 capability 仍是跨 dataset 的 primary driver（CoNLL 58% vs SciERC 21% 的差异远大于 rank ablation 的 9pp）。LP compression 也略微缓解（range median 0.048 vs 0.041），因为 lower fine-tuning 保留了更多 generation-level diversity。Selection 仍不显著（+0.3pp），因为即使 degeneracy 降低，LP compression 仍存在。"
550	  },
551	  {
552	    "name": "claim_audit",
553	    "description": "Cross-chapter numerical consistency audit. 检查所有定量 claims vs source data。",
554	    "results": {
555	      "contradictions_found": 3,
556	      "contradiction_1": {
557	        "location": "Discussion vs Limitations",
558	        "issue": "Discussion says '+0.1pp over single-sample', Limitations says '+0.4pp over greedy'",
559	        "resolution": "Both refer to different comparisons: +0.1pp = best signal vs random single, +0.4pp (incorrect) should be +0.6pp = LP vs greedy (from exp_016_rerun_1024). Standardize to LP vs greedy +0.6pp throughout."
560	      },
561	      "contradiction_2": {
562	        "location": "Abstract vs Results",
563	        "issue": "Abstract claims 'AUROC up to 0.82' but Results table shows max 0.749 (EM on NER)",
564	        "resolution": "0.82 comes from CoNLL (SJ AUROC=0.8008 in exp_002, EM AUROC=0.8156). Must specify which dataset in Abstract or use max across all: CoNLL EM AUROC 0.82."
565	      },
566	      "contradiction_3": {
567	        "location": "Intro vs Section 5",
568	        "issue": "Intro claims '21-58% of instances produce identical F1' — percentages are from 1024-token data but cited numbers use mixed sources",
569	        "resolution": "Verify degeneracy rates from consistent 1024-token runs. SciERC (1024): ~21% (from exp_012_rerun_1024 tied fraction). CoNLL: derive from exp_002 data."
570	      },
571	      "minor_issues_found": 4,
572	      "total_resolution_time_hours": 2
573	    },
574	    "tables": [
575	      {
576	        "name": "Table: Claim Audit Summary",
577	        "columns": [
578	          "Issue Type",
579	          "Count",
580	          "Severity"
581	        ],
582	        "rows": [
583	          [
584	            "Major numerical contradiction",
585	            "3",
586	            "Must fix before submission"
587	          ],
588	          [
589	            "Minor rounding/precision inconsistency",
590	            "4",
591	            "Fix in final pass"
592	          ],
593	          [
594	            "Stale reference to old experiment",
595	            "2",
596	            "Update citation"
597	          ],
598	          [
599	            "Missing CI/p-value for claimed significance",
600	            "1",
601	            "Add from bootstrap data"
602	          ]
603	        ]
604	      }
605	    ],
606	    "figures": [],
607	    "analysis": "Audit 发现 3 个需要修正的矛盾，均为 presentation-level 问题。最关键的是 Discussion/Limitations 中对 selection gap magnitude 的不一致引用——这在 median tier 下尤其敏感，因为 adjusted claims 要求精确措辞（'predominantly fail' 而非 'universally fail'）。所有矛盾均可通过引用正确的 source experiment（exp_012_rerun_1024 为 SciERC 的 canonical source，exp_002 为 CoNLL）解决。无 methodological 问题。建议统一使用 1024-token pipeline 数据作为 paper 中所有 SciERC metrics 的来源。\n\nNumerical inconsistencies 是 paper 在多轮实验迭代中积累的必然结果。本项目经历了 512→1024 token 数据迁移、gold-empty filtering pipeline 修正、多 seed 数值更新等，每次都有部分 claims 未同步更新。Median tier 假设找到 3 个显著矛盾（realistic for a ~8-page paper with dense quantitative claims）而非 catastrophic level（>5）的问题。这些都是 presentational issues 而非 methodological problems——底层实验数据一致。"
608	  }
609	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afdf4272-8dd2-4cde-8332-27a5ddb39d54",
  "isSidechain": false,
  "promptId": "1cdd1fca-2b73-4d1a-a515-3ada1bf62a4e",
  "type": "user",
  "uuid": "4d0e3499-b35d-486c-9dae-40ccb3667a36",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"fewnerd_smoke\",\n    \"description\": \"Few-NERD INTRA coarse 8-type, 1-epoch LoRA fine-tune + 200-instance N=8 pilot. Gate for full run.\",\n    \"results\": {\n      \"train_loss_1epoch\": 0.15,\n      \"eval_loss_1epoch\": 0.12,\n      \"greedy_f1_200inst\": 0.78,\n      \"parse_rate\": 0.998,\n      \"pilot_sj_rho_full\": 0.3,\n      \"pilot_degeneracy_rate\": 0.22,\n      \"pilot_oracle_f1\": 0.86,\n      \"pilot_headroom_pp\": 8.0,\n      \"inference_time_200inst_minutes\": 12,\n      \"n_entity_types\": 8,\n      \"sample_f1_pct_zero\": 8.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Few-NERD Smoke Test Summary\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\"\n        ],\n        \"rows\": [\n          [\n            \"Training loss (1 epoch)\",\n            \"0.150\"\n          ],\n          [\n            \"Greedy NER F1 (200 inst)\",\n            \"0.780\"\n          ],\n          [\n            \"Oracle NER F1\",\n            \"0.860\"\n          ],\n          [\n            \"Headroom\",\n            \"8.0pp\"\n          ],\n          [\n            \"Parse rate\",\n            \"99.8%\"\n          ],\n          [\n            \"Degeneracy rate (pilot)\",\n            \"22%\"\n          ],\n          [\n            \"SJ ρ (pilot)\",\n            \"0.30\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Smoke test PASS。模型成功学会 Few-NERD 格式和 8 类实体标注。Greedy F1=0.78 介于 SciERC（0.66）和 CoNLL（0.91）之间，符合 Few-NERD 的中等难度定位。Degeneracy 初步估计 ~22%，低于 capability trap 线性外推的预测值（~35-40%），暗示 median tier 的'部分确认但不完美拟合'结论。Pipeline validated，proceed to exp-021。\\n\\nFew-NERD INTRA coarse（8类通用实体：Person, Organization, Location, Building, Product, Event, Art, Other）比 SciERC 更标准化但比 CoNLL 更细粒度。1-epoch LoRA 已足够让 Qwen3-8B 学会格式和基本类型映射（类似 SciERC ft_001 在 1 epoch 后 NER F1=0.60）。Few-NERD 训练集大（~66K samples），1 epoch 足以收敛基本模式。Greedy F1=0.78 符合 median 范围 [0.75, 0.85] 的下半段，因为只有 1 epoch。Degeneracy 0.22 在 pilot（200 inst）上初步可见但 CI 宽——这个 pilot 主要验证 pipeline 可行性，不做结论。\"\n  },\n  {\n    \"name\": \"fewnerd_full\",\n    \"description\": \"Few-NERD 3-epoch LoRA + full test set N=8, 3 seeds. 5 signals + degeneracy + selection.\",\n    \"results\": {\n      \"train_loss_3epoch\": 0.065,\n      \"eval_loss_3epoch\": 0.078,\n      \"greedy_f1\": 0.812,\n      \"oracle_f1\": 0.895,\n      \"oracle_headroom_pp\": 8.3,\n      \"n_test_instances\": 1500,\n      \"n_valid_after_gold_filter\": 1380,\n      \"parse_rate\": 0.999,\n      \"degeneracy_rate\": 0.26,\n      \"degeneracy_rate_3seed_mean\": 0.25,\n      \"degeneracy_rate_3seed_sd\": 0.018,\n      \"sj_rho_full\": 0.33,\n      \"fk_rho_full\": 0.28,\n      \"logprob_rho_full\": 0.25,\n      \"em_rho_full\": 0.35,\n      \"voting_conf_rho_full\": 0.36,\n      \"sj_auroc_full\": 0.72,\n      \"em_auroc_full\": 0.78,\n      \"voting_conf_auroc_full\": 0.73,\n      \"logprob_auroc_full\": 0.68,\n      \"sj_rho_cond\": 0.31,\n      \"em_rho_cond\": 0.38,\n      \"voting_conf_rho_cond\": 0.33,\n      \"sj_rho_3seed_mean\": 0.32,\n      \"sj_rho_3seed_sd\": 0.025,\n      \"selection_f1_greedy\": 0.812,\n      \"selection_f1_sj\": 0.813,\n      \"selection_f1_logprob\": 0.814,\n      \"selection_f1_voting_conf\": 0.811,\n      \"selection_f1_random\": 0.798,\n      \"selection_f1_oracle\": 0.895,\n      \"selection_gap_best_minus_greedy_pp\": 0.2,\n      \"selection_bootstrap_ci_95_low\": -0.8,\n      \"selection_bootstrap_ci_95_high\": 1.2,\n      \"selection_permutation_p\": 0.42,\n      \"capability_trap_f1_vs_degeneracy_r2_with_fewnerd\": 0.72,\n      \"capability_trap_monotonicity\": true,\n      \"lp_within_instance_range_median\": 0.038,\n      \"lp_tied_fraction\": 0.31,\n      \"sample_f1_pct_zero\": 6.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Few-NERD Full Results — QE Correlation (ρ, 3-seed mean±sd)\",\n        \"columns\": [\n          \"Signal\",\n          \"NER ρ (full)\",\n          \"NER ρ (cond)\",\n          \"AUROC\"\n        ],\n        \"rows\": [\n          [\n            \"Voting_conf\",\n            \"0.360±0.022\",\n            \"0.330±0.028\",\n            \"0.730\"\n          ],\n          [\n            \"EM\",\n            \"0.350±0.019\",\n            \"0.380±0.024\",\n            \"0.780\"\n          ],\n          [\n            \"SJ\",\n            \"0.320±0.025\",\n            \"0.310±0.030\",\n            \"0.720\"\n          ],\n          [\n            \"FK\",\n            \"0.280±0.020\",\n            \"0.260±0.025\",\n            \"0.660\"\n          ],\n          [\n            \"Logprob\",\n            \"0.250±0.018\",\n            \"0.220±0.022\",\n            \"0.680\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Few-NERD Selection F1 (N=8, T=1.0)\",\n        \"columns\": [\n          \"Method\",\n          \"F1\",\n          \"Δ vs greedy (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Oracle\",\n            \"0.895\",\n            \"+8.3\"\n          ],\n          [\n            \"Logprob\",\n            \"0.814\",\n            \"+0.2\"\n          ],\n          [\n            \"SJ\",\n            \"0.813\",\n            \"+0.1\"\n          ],\n          [\n            \"Greedy (T=0)\",\n            \"0.812\",\n            \"—\"\n          ],\n          [\n            \"Voting_conf\",\n            \"0.811\",\n            \"-0.1\"\n          ],\n          [\n            \"Random\",\n            \"0.798\",\n            \"-1.4\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Capability Trap — Cross-Dataset Degeneracy\",\n        \"columns\": [\n          \"Dataset\",\n          \"Greedy F1\",\n          \"Degeneracy %\",\n          \"Predicted %\",\n          \"Residual\"\n        ],\n        \"rows\": [\n          [\n            \"CoNLL-2003\",\n            \"0.912\",\n            \"58%\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Few-NERD\",\n            \"0.812\",\n            \"26%\",\n            \"38%\",\n            \"-12pp\"\n          ],\n          [\n            \"SciERC\",\n            \"0.663\",\n            \"21%\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"WNUT-17\",\n            \"0.523\",\n            \"~0%\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Few-NERD 为 capability trap 提供 partial confirmation：degeneracy 单调性成立（F1 越高，degeneracy 越高），但 R² 从 3-point 的 0.95+ 下降到 4-point 的 0.72。这要求将 capability trap 从 'structural inevitability' 调整为 'primary contributing factor'，因为 task structure（类型数量、实体密度）引入了不可忽略的 residual。Selection 结果（+0.2pp, p=0.42）处于 median 定义的模糊区间——不显著优于 greedy，但也没有像 SciERC 那样 greedy 明确 dominate。这使得 'universally fail' 需弱化为 'predominantly fail'。QE signals 仍然有效（SJ ρ=0.32 > LP ρ=0.25），支撑 Claim 2 的 QE framework contribution。\\n\\n3-epoch fine-tune 使 greedy F1 从 smoke 的 0.78 提升到 0.812，对应 median 范围 [0.75,0.85] 的中部。Degeneracy rate 0.26 的关键逻辑：capability trap 预测在 F1=0.81 时 degeneracy 应~38%（CoNLL 0.91→58%, SciERC 0.66→21% 的线性外推），但实际只有 26%。原因：(1) Few-NERD 有 8 种实体类型（vs CoNLL 的 4 种），类型多样性提供更多变异维度，使得即使 overall F1 高，individual spans 仍有组合空间；(2) Few-NERD 实例更长/实体更密，per-instance 的 combinatorial space 抑制了完全 convergence。这就是 median 的核心信号：monotonicity 成立（F1 越高 degeneracy 越高），但 R²=0.72 而非 0.95——task structure（类型数、实体密度）是 residual variance 的来源。Selection gap +0.2pp 的逻辑：degeneracy 26% 介于 SciERC（21%，gap≈0）和 CoNLL（58%，gap≈0）之间，bootstrap p=0.42 说明完全不显著。信号排序 VC>EM>SJ>FK>LP 与 CoNLL 类似但 SJ-LP gap 更小（0.08 vs SciERC 的 0.15），因为 8 类系统的 LP 信号比 6 类科学文本更 informative。\"\n  },\n  {\n    \"name\": \"3rd_seed_scierc\",\n    \"description\": \"SciERC NER+RE N=8, seed=789. 第3个 seed 用于 Fisher combined p-value。\",\n    \"results\": {\n      \"ner_greedy_f1\": 0.661,\n      \"ner_oracle_f1\": 0.779,\n      \"ner_headroom_pp\": 11.8,\n      \"ner_sj_rho_full\": 0.372,\n      \"ner_fk_rho_full\": 0.258,\n      \"ner_logprob_rho_full\": 0.218,\n      \"ner_em_rho_full\": 0.305,\n      \"ner_voting_conf_rho_full\": 0.388,\n      \"ner_sj_auroc\": 0.698,\n      \"ner_em_auroc\": 0.755,\n      \"re_greedy_f1\": 0.415,\n      \"re_oracle_f1\": 0.582,\n      \"re_headroom_pp\": 16.7,\n      \"re_sj_rho_full\": 0.258,\n      \"re_fk_rho_full\": 0.285,\n      \"re_logprob_rho_full\": 0.242,\n      \"re_voting_conf_rho_full\": 0.34,\n      \"re_sample_f1_pct_zero\": 44.8,\n      \"re_lp_gt_sj\": false,\n      \"re_sj_minus_lp_rho\": 0.016,\n      \"ner_sj_rho_3seed_mean\": 0.381,\n      \"ner_sj_rho_3seed_sd\": 0.032,\n      \"re_sj_rho_3seed_mean\": 0.261,\n      \"re_sj_rho_3seed_sd\": 0.012,\n      \"re_lp_rho_3seed_mean\": 0.268,\n      \"re_lp_rho_3seed_sd\": 0.038,\n      \"fisher_combined_p_sj_gt_lp_ner\": 0.028,\n      \"fisher_combined_p_sj_gt_lp_ner_significant\": true,\n      \"fisher_combined_p_lp_gt_sj_re\": 0.085,\n      \"fisher_combined_p_lp_gt_sj_re_significant\": false,\n      \"selection_f1_greedy\": 0.661,\n      \"selection_f1_logprob\": 0.654,\n      \"selection_f1_sj\": 0.651,\n      \"selection_f1_oracle\": 0.779,\n      \"degeneracy_rate_ner\": 0.23,\n      \"n_instances\": 529,\n      \"parse_rate\": 1.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: 3-Seed SciERC NER ρ Stability\",\n        \"columns\": [\n          \"Signal\",\n          \"Seed 42\",\n          \"Seed 123\",\n          \"Seed 789\",\n          \"Mean\",\n          \"SD\"\n        ],\n        \"rows\": [\n          [\n            \"SJ\",\n            \"0.383\",\n            \"0.384\",\n            \"0.372\",\n            \"0.381\",\n            \"0.032\"\n          ],\n          [\n            \"FK\",\n            \"0.259\",\n            \"0.266\",\n            \"0.258\",\n            \"0.261\",\n            \"0.004\"\n          ],\n          [\n            \"LP\",\n            \"0.205\",\n            \"0.226\",\n            \"0.218\",\n            \"0.216\",\n            \"0.011\"\n          ],\n          [\n            \"VC\",\n            \"0.379\",\n            \"0.407\",\n            \"0.388\",\n            \"0.391\",\n            \"0.014\"\n          ],\n          [\n            \"EM\",\n            \"0.295\",\n            \"0.299\",\n            \"0.305\",\n            \"0.300\",\n            \"0.005\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: 3-Seed SciERC RE ρ — LP vs SJ Ranking\",\n        \"columns\": [\n          \"Signal\",\n          \"Seed 42\",\n          \"Seed 123\",\n          \"Seed 789\",\n          \"Mean\",\n          \"SD\"\n        ],\n        \"rows\": [\n          [\n            \"LP\",\n            \"0.267\",\n            \"0.300\",\n            \"0.242\",\n            \"0.270\",\n            \"0.029\"\n          ],\n          [\n            \"SJ\",\n            \"0.250\",\n            \"0.283\",\n            \"0.258\",\n            \"0.264\",\n            \"0.017\"\n          ],\n          [\n            \"LP>SJ?\",\n            \"Yes (+0.017)\",\n            \"Yes (+0.017)\",\n            \"No (-0.016)\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Fisher Combined p-values (3 seeds)\",\n        \"columns\": [\n          \"Hypothesis\",\n          \"Fisher χ²\",\n          \"df\",\n          \"p\",\n          \"Significant?\"\n        ],\n        \"rows\": [\n          [\n            \"NER: SJ > LP\",\n            \"14.2\",\n            \"6\",\n            \"0.028\",\n            \"Yes (p<0.05)\"\n          ],\n          [\n            \"RE: LP > SJ\",\n            \"10.8\",\n            \"6\",\n            \"0.085\",\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"第3个 seed 确认 NER 结论完全稳定（SJ > LP, Fisher p=0.028）。RE 上 LP>SJ 的 ranking 在 seed 789 翻转（SJ 0.258 > LP 0.242），使得 3-seed Fisher p=0.085 未达显著水平。这是 median tier 的核心特征之一：RE signal ranking 不够 robust 以做 definitive claim。Paper 中需表述为 'LP tends to outperform structural signals on RE (2/3 seeds), likely due to binary dominance mechanism, though this advantage does not reach statistical significance across all random seeds (Fisher p=0.085).' Primary claims（capability trap、NER structural>surface、selection fails）在 3-seed 下完全稳定。\\n\\nSeed=789 的 NER 结果高度稳定（SJ ρ=0.372 vs 已有 seeds 0.383/0.384/0.360，3-seed SD=0.032 落入 median 范围 [0.02, 0.045]）。关键 median 特征在 RE：seed 789 上 SJ ρ=0.258 略高于 LP ρ=0.242，打破了 seeds 42/123 上 LP>SJ 的 pattern（seed42: LP 0.267 > SJ 0.250; seed123: LP 0.300 > SJ 0.283）。这使得 Fisher combined p for LP>SJ on RE = 0.085（不显著）。翻转原因：RE 的 zero-F1 rate 在不同 seeds 间波动（43-45%），seed=789 恰好有较少的 'complete failure' instances 进入 high-LP bin，削弱了 LP 的 binary classification 优势。NER 上 SJ>LP 的 Fisher p=0.028 仍然显著，支撑 'structural signals dominate for NER' 的结论。但 RE signal ranking 的不稳定性要求将 'LP>SJ for RE' 从 'definitive finding' 降级为 'tendency across most seeds'。\"\n  },\n  {\n    \"name\": \"lora_rank8_ablation\",\n    \"description\": \"LoRA rank=8 (vs baseline rank=16) fine-tune on SciERC + N=8 inference. Tests fine-tuning intensity vs capability as degeneracy driver.\",\n    \"results\": {\n      \"train_loss_5epoch\": 0.095,\n      \"eval_loss_5epoch\": 0.105,\n      \"ner_greedy_f1\": 0.641,\n      \"ner_oracle_f1\": 0.782,\n      \"ner_headroom_pp\": 14.1,\n      \"degeneracy_rate_r8\": 0.12,\n      \"degeneracy_rate_r16_baseline\": 0.21,\n      \"degeneracy_delta_pp\": 9.0,\n      \"ner_sj_rho_full\": 0.365,\n      \"ner_fk_rho_full\": 0.27,\n      \"ner_logprob_rho_full\": 0.195,\n      \"ner_voting_conf_rho_full\": 0.39,\n      \"ner_sj_auroc\": 0.69,\n      \"selection_f1_greedy_r8\": 0.641,\n      \"selection_f1_logprob_r8\": 0.644,\n      \"selection_f1_sj_r8\": 0.642,\n      \"selection_f1_oracle_r8\": 0.782,\n      \"selection_gap_logprob_minus_greedy_pp\": 0.3,\n      \"lp_within_instance_range_median_r8\": 0.048,\n      \"lp_tied_fraction_r8\": 0.14,\n      \"re_greedy_f1\": 0.385,\n      \"re_oracle_f1\": 0.568,\n      \"re_degeneracy_rate_r8\": 0.08,\n      \"re_sample_f1_pct_zero\": 48.2,\n      \"greedy_f1_delta_r8_minus_r16\": -0.022,\n      \"sj_rho_delta_r8_minus_r16\": 0.005,\n      \"headroom_delta_r8_minus_r16_pp\": 3.0,\n      \"non_degen_selection_gap_pp\": 2.1,\n      \"n_instances\": 529,\n      \"parse_rate\": 0.995\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: LoRA Rank Ablation — Degeneracy & Performance\",\n        \"columns\": [\n          \"Metric\",\n          \"Rank=16 (baseline)\",\n          \"Rank=8\",\n          \"Δ\"\n        ],\n        \"rows\": [\n          [\n            \"NER Greedy F1\",\n            \"0.663\",\n            \"0.641\",\n            \"-2.2pp\"\n          ],\n          [\n            \"NER Oracle F1\",\n            \"0.776\",\n            \"0.782\",\n            \"+0.6pp\"\n          ],\n          [\n            \"NER Headroom\",\n            \"11.3pp\",\n            \"14.1pp\",\n            \"+2.8pp\"\n          ],\n          [\n            \"NER Degeneracy %\",\n            \"21%\",\n            \"12%\",\n            \"-9pp\"\n          ],\n          [\n            \"LP range (median nats)\",\n            \"0.041\",\n            \"0.048\",\n            \"+17%\"\n          ],\n          [\n            \"LP tied fraction\",\n            \"0.21\",\n            \"0.14\",\n            \"-7pp\"\n          ],\n          [\n            \"NER SJ ρ\",\n            \"0.383\",\n            \"0.365\",\n            \"-0.018\"\n          ],\n          [\n            \"Best selection F1\",\n            \"0.650 (LP)\",\n            \"0.644 (LP)\",\n            \"-0.6pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Degeneracy Attribution (NER)\",\n        \"columns\": [\n          \"Driver\",\n          \"Predicted Δ degen\",\n          \"Actual Δ degen\",\n          \"Attribution %\"\n        ],\n        \"rows\": [\n          [\n            \"Capability (F1 drop 0.66→0.64)\",\n            \"-2pp\",\n            \"—\",\n            \"22%\"\n          ],\n          [\n            \"Fine-tuning intensity (rank 16→8)\",\n            \"—\",\n            \"-7pp\",\n            \"78%\"\n          ],\n          [\n            \"Total observed\",\n            \"—\",\n            \"-9pp\",\n            \"100%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Non-degenerate Subset Analysis (rank=8)\",\n        \"columns\": [\n          \"Subset\",\n          \"n\",\n          \"LP selection gap\",\n          \"SJ selection gap\"\n        ],\n        \"rows\": [\n          [\n            \"All instances\",\n            \"529\",\n            \"+0.3pp\",\n            \"+0.1pp\"\n          ],\n          [\n            \"Non-degenerate only\",\n            \"465\",\n            \"+2.1pp\",\n            \"+1.5pp\"\n          ],\n          [\n            \"Non-degen, rank=16 baseline\",\n            \"418\",\n            \"+2.9pp (p=0.01)\",\n            \"+1.8pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LoRA rank=8 ablation 是 median tier 的 defining experiment。Degeneracy 下降 9pp（从 21% 到 12%）中，capability drop（F1 -2.2pp）仅能解释约 2pp，剩余 7pp 必须归因于 fine-tuning intensity itself。这迫使论文承认 capability trap 不是 sole driver——fine-tuning regime 是 independent contributing factor。但关键上下文是：跨 dataset 的 degeneracy variation（CoNLL 58% vs SciERC 21% = 37pp range）远大于 rank ablation 的 9pp，所以 capability 仍是 'dominant factor'。Paper framing 调整为：'Output convergence is driven by model capability (primary, explaining cross-dataset variance) AND fine-tuning intensity (secondary, contributing 5-15pp within-dataset). The capability trap remains the unifying explanation for why test-time scaling provides diminishing returns as model quality improves.' Selection 仍然 fails 即使 degeneracy 降低，因为 LP compression 是 independent bottleneck（不随 LoRA rank 改变）。\\n\\nLoRA rank=8 的参数容量是 rank=16 的一半，模型 fine-tuning 强度更低。这导致两个效果：(1) greedy F1 略降（0.641 vs 0.663，-2.2pp），因为模型对 SciERC schema 的记忆不如 rank=16 完整；(2) 输出多样性更高，因为 lower-rank adaptation 保留了更多 base model 的 stochastic behavior，degeneracy 从 21% 降到 12%（-9pp，落入 median 范围 [5,15]）。关键逻辑：如果 degeneracy 纯粹由 capability 驱动，则 F1 降低应该已经自动解释 degeneracy 下降（按 capability trap curve：F1 从 0.66 降到 0.64 预测 degeneracy 从 21% 降到 ~19%，仅 -2pp）。但实际下降 9pp >> 2pp 的 capability-predicted 下降，说明 fine-tuning intensity 本身是 independent contributing factor。Median 解读：capability trap 解释了约 22% 的 degeneracy reduction（2/9），fine-tuning intensity 解释了剩余 78%。但 capability 仍是跨 dataset 的 primary driver（CoNLL 58% vs SciERC 21% 的差异远大于 rank ablation 的 9pp）。LP compression 也略微缓解（range median 0.048 vs 0.041），因为 lower fine-tuning 保留了更多 generation-level diversity。Selection 仍不显著（+0.3pp），因为即使 degeneracy 降低，LP compression 仍存在。\"\n  },\n  {\n    \"name\": \"claim_audit\",\n    \"description\": \"Cross-chapter numerical consistency audit. 检查所有定量 claims vs source data。\",\n    \"results\": {\n      \"contradictions_found\": 3,\n      \"contradiction_1\": {\n        \"location\": \"Discussion vs Limitations\",\n        \"issue\": \"Discussion says '+0.1pp over single-sample', Limitations says '+0.4pp over greedy'\",\n        \"resolution\": \"Both refer to different comparisons: +0.1pp = best signal vs random single, +0.4pp (incorrect) should be +0.6pp = LP vs greedy (from exp_016_rerun_1024). Standardize to LP vs greedy +0.6pp throughout.\"\n      },\n      \"contradiction_2\": {\n        \"location\": \"Abstract vs Results\",\n        \"issue\": \"Abstract claims 'AUROC up to 0.82' but Results table shows max 0.749 (EM on NER)\",\n        \"resolution\": \"0.82 comes from CoNLL (SJ AUROC=0.8008 in exp_002, EM AUROC=0.8156). Must specify which dataset in Abstract or use max across all: CoNLL EM AUROC 0.82.\"\n      },\n      \"contradiction_3\": {\n        \"location\": \"Intro vs Section 5\",\n        \"issue\": \"Intro claims '21-58% of instances produce identical F1' — percentages are from 1024-token data but cited numbers use mixed sources\",\n        \"resolution\": \"Verify degeneracy rates from consistent 1024-token runs. SciERC (1024): ~21% (from exp_012_rerun_1024 tied fraction). CoNLL: derive from exp_002 data.\"\n      },\n      \"minor_issues_found\": 4,\n      \"total_resolution_time_hours\": 2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Claim Audit Summary\",\n        \"columns\": [\n          \"Issue Type\",\n          \"Count\",\n          \"Severity\"\n        ],\n        \"rows\": [\n          [\n            \"Major numerical contradiction\",\n            \"3\",\n            \"Must fix before submission\"\n          ],\n          [\n            \"Minor rounding/precision inconsistency\",\n            \"4\",\n            \"Fix in final pass\"\n          ],\n          [\n            \"Stale reference to old experiment\",\n            \"2\",\n            \"Update citation\"\n          ],\n          [\n            \"Missing CI/p-value for claimed significance\",\n            \"1\",\n            \"Add from bootstrap data\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Audit 发现 3 个需要修正的矛盾，均为 presentation-level 问题。最关键的是 Discussion/Limitations 中对 selection gap magnitude 的不一致引用——这在 median tier 下尤其敏感，因为 adjusted claims 要求精确措辞（'predominantly fail' 而非 'universally fail'）。所有矛盾均可通过引用正确的 source experiment（exp_012_rerun_1024 为 SciERC 的 canonical source，exp_002 为 CoNLL）解决。无 methodological 问题。建议统一使用 1024-token pipeline 数据作为 paper 中所有 SciERC metrics 的来源。\\n\\nNumerical inconsistencies 是 paper 在多轮实验迭代中积累的必然结果。本项目经历了 512→1024 token 数据迁移、gold-empty filtering pipeline 修正、多 seed 数值更新等，每次都有部分 claims 未同步更新。Median tier 假设找到 3 个显著矛盾（realistic for a ~8-page paper with dense quantitative claims）而非 catastrophic level（>5）的问题。这些都是 presentational issues 而非 methodological problems——底层实验数据一致。\"\n  }\n]",
      "numLines": 609,
      "startLine": 1,
      "totalLines": 609
    }
  },
  "sourceToolAssistantUUID": "afdf4272-8dd2-4cde-8332-27a5ddb39d54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T09:54:23.195Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XThuG2AVRzNirzvFNgsF4g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d0e3499-b35d-486c-9dae-40ccb3667a36",
  "isSidechain": false,
  "requestId": "req_011Cb63aMcePcS9PjUALeAAb",
  "type": "assistant",
  "uuid": "585434f4-9337-45ab-8fd4-4ea97d718529",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5cnLB4vUXy3mwjoPLLjrk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11285,
      "cache_read_input_tokens": 11841,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11285
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_cons…",
  "leafUuid": "585434f4-9337-45ab-8fd4-4ea97d718529",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696"
}
```

---

### Tool result

_source line 13 · 2026-05-16T09:54:23.445Z_

<details><summary>↩ Tool result · `toolu_01XThuG2AVRzNirzvFNgsF4g`</summary>

```text
1	# Paper Framing — struct_self_consist_ie
2	
3	> Updated 2026-05-15 — D098: 4B scale ablation 2×2 矩阵完成。4B ≈ 8B（多数 correlation 4B 反而更高），gap 与 model capacity 无关，task difficulty 是信号退化主驱动。Scale ablation 证明 universality across scales。R14 RESOLVED。
4	
5	## Target Venue
6	- Primary: EMNLP 2026 **Main Conference** (via ARR May 2026)
7	- Deadline: ARR May cycle, 2026-05-25
8	
9	## Core Claims (4 layers, D112 updated — Main Conference framing with capability trap + degeneracy)
10	
11	### Claim 1 (PRIMARY — Diagnosing Two Failure Mechanisms + Capability Trap)
12	Confidence signals reliably predict output quality across instances (AUROC up to 0.82, ρ up to 0.45) but universally fail to select better candidates from multiple samples. We diagnose **two failure mechanisms** and a unifying **capability trap** that explains why the gap is structurally inevitable for capable models.
13	
14	**Three-layer argument + Capability Trap**:
15	- Layer A (design property, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification — the "methodological premise" — not an empirical finding.
16	- Layer B (empirical — instance degeneracy): 21-58% of instances produce identical F1 across all N samples, eliminating selection headroom. Within-instance ρ=0.524 (SciERC) and 0.994 (CoNLL) — signals ARE correlated within instances, but degeneracy makes this irrelevant. Non-degenerate instances show MBR closing 23-41% of oracle gap. T=0 greedy dominates all signals (greedy F1=0.663 > best LP selection 0.647 on SciERC) — zero-cost strongest argument.
17	- Layer C (empirical — LP compression): Logprob — the only per-sample signal — fails due to intrinsic score compression (median within-instance LP range = 0.041 nats). Entity-token LP shows 4× variance but WORSE selection (-2.0pp). Free-form ablation confirms compression is model/task intrinsic (std ratio 0.97).
18	- **Capability Trap** (unifying insight, D111): Model capability → output convergence → instance degeneracy → vanishing selection headroom. Evidence: CoNLL (91% F1) → 58% degeneracy, SciERC (66% F1) → 21%, WNUT (48% F1) → ~0%. Scale dimension: 8B → 21% degen vs 4B → 10.4% on SciERC. This is NOT an "artifact" — it is a **consequence of capability**, a structural inevitability. The better the model, the less test-time scaling can help via unsupervised selection.
19	
20	**Distinction from MBR literature**: Eikema et al.'s MBR failure = utility function misalignment. Our failure = utility IS aligned (within-instance ρ=0.524) but headroom eliminated by degeneracy — qualitatively novel mechanism.
21	
22	**Key evidence (score compression)**:
23	- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ: 0.08→0.39
24	- Full set: logprob +0.6pp, bootstrap p=0.39, Cohen's d=0.038 (negligible), 95% CI [-3.0, +4.2]pp
25	- Oracle headroom: NER +13pp, RE +18pp → information exists but signals can't access it
26	
27	**Key evidence (free-form ablation)** [DONE — exp_freeform_ablation, NEGATIVE]:
28	- LP distribution: constrained std=0.0206, free-form std=0.0199 (ratio 0.97, virtually unchanged)
29	- Tied fraction: 59.7% → 57.7% (-2.0pp, negligible)
30	- NER selection: +0.59pp → +0.18pp (both negligible vs greedy)
31	- RE selection: -0.68pp → +1.69pp (flipped positive — secondary finding)
32	- NER VC rho: 0.379 → 0.409 (slight QE improvement, selection still fails)
33	- Parse rate: 99.95% (fine-tuned model retains JSON format without grammar)
34	- **Conclusion**: Score compression is model/task intrinsic. The gap is universal.
35	
36	**Key evidence (scale ablation)** [DONE — 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}]:
37	- CoNLL NER: 4B greedy_f1=0.9234 (>8B 0.9123, +1.11pp), SJ_ρ=0.4217 (≈8B 0.4357, −1.4pp), FK_ρ=0.4181 (>8B 0.3998, +1.83pp)
38	- SciERC NER: 4B SJ_ρ=0.4221 (>8B 0.3825, +3.96pp), FK_ρ=0.3258 (>8B 0.2590, +6.68pp)
39	- SciERC RE: 4B SJ_ρ=0.2673 (>8B 0.2441, +2.32pp), FK_ρ=0.3593 (>8B 0.2782, +8.11pp); struct>surface ✗ at both scales
40	- **Conclusion**: Correlation strength maintained or improved at 4B across all 4 cells. The gap originates from within-instance signal misalignment, not model capacity. Task difficulty (SciERC RE zero-F1 rate) remains the primary driver, consistent across scales.
41	- CoNLL 4B headroom: 1.70pp (vs 8B 4.20pp) → MARGINAL for selection power, but QE correlations robust
42	- SciERC RE 4B: 47.6% zero-F1, RE LP_ρ_cond=0.1135 (p=0.074, n.s.) → confirms binary dominance at 4B
43	- **4B selection results** (correlation-selection gap at 4B):
44	  - CoNLL NER 4B (n=2756): SJ +0.07pp, FK +0.03pp, LP +0.09pp vs greedy 0.9213. All ≤0.1pp — MARGINAL (headroom 1.70pp)
45	  - SciERC NER 4B (n=529): SJ **-1.49pp**, FK -1.56pp, LP -2.23pp vs greedy 0.6622. Oracle 0.7925 (+13.02pp). **All signals WORSE than greedy despite 13pp oracle headroom — gap confirmed at 4B**
46	  - SciERC NER 4B gap demonstration: SJ-FK ρ gap = +0.096 (strong correlation advantage), SJ-FK selection F1 gap = +0.0007 (zero selection advantage) → correlation-selection gap quantified at 4B
47	- **n_samples confound control**: Qwen3-8B n=8 data exists as control. CoNLL SJ: n8 ρ=0.4389 → n16 ρ=0.4496 (Δ=0.011, CI crosses zero). SciERC SJ: n8→n16 Δ=0.066, CI=[0.004, 0.128] weak effect. n_samples not a confound for 4B-8B comparison.
48	- **Paper framing**: "Scale ablation shows the gap is not an artifact of a particular model size; correlation strength is maintained at 4B, confirming that the gap originates from within-instance signal misalignment rather than model capacity."
49	
50	**exp-019 supervised verifier**: SKIPPED (Reviewer recommendation). Reasons: DDL 10 days, scope creep risk (analytical paper + solution = type mismatch), exp-016 LR ensemble already underperforms EM (0.666 vs 0.749). Verifier is follow-up paper material.
51	
52	**Bonus finding (parse rate)**: Free-form parse rate 99.95% (4406/4408) — fine-tuned 8B model generates valid JSON without grammar constraints. Challenges intro:19 claim about constrained decoding necessity for format compliance.
53	
54	**Implications**: Not just "signals don't work" but "here's WHY they don't work (intrinsic score compression), here's proof it's universal (controlled ablation via elimination), and here's the forward direction (breaking LP compression requires fundamentally different approaches — trained verifiers, multi-round refinement — not simply relaxing decoding constraints)."
55	
56	### Claim 2 (METHODOLOGY — QE Evaluation Framework)
57	Systematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. This is the methodological infrastructure, not a primary contribution.
58	
59	**Key results**:
60	- NER: EM AUROC 0.749, voting_conf ρ=0.379, SJ ρ=0.360 — all >> logprob (AUROC 0.578, ρ=0.205). 3-seed consistent: SJ > FK delta=0.093~0.122
61	- RE (3-seed confirmed): **LP > SJ > FK** (mean ρ: LP 0.302, SJ 0.265, FK 0.254). Signal ranking reverses vs NER — structural signals lose advantage when 43-45% of RE samples have F1=0 (binary signal dominance). LP's coarse but stable generation-confidence signal captures "did the model get any relations right" better than structural overlap measures.
62	- Difficulty-dependent signal ranking: WNUT-17 conditional collapse (ρ significant → n.s.) + logprob ρ=−0.410 (non-obvious: overconfidence on OOD)
63	- Temperature robustness: SJ Δρ=±0.01 vs FK Δρ=±0.06-0.09. T=0.7: LP full ρ improves 0.205→0.249, LP cond ρ 0.154→0.185; FK 0.267→0.289 despite more compression → concentrated signal hypothesis (non-tied instances at lower T carry more informative variance). **Paper citation rule**: robustness/temperature tables use full ρ; score compression analysis uses cond ρ. Always annotate which variant.
64	- **Task-dependent signal effectiveness** (new finding from RE 3-seed): The optimal signal family depends on task structure. NER (token-level, graded F1) → structural agreement captures quality gradients. RE (relation-level, binary-dominated F1) → logprob captures generation confidence better. This is NOT a weakness — it's a nuanced finding that enriches the diagnostic framework.
65	
66	**Evidence preserved from original Claim 1** (SciERC, N=8, T=1.0, exp_012_rerun_1024):
67	- NER full (n=529): ρ — voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205; AUROC — EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578
68	- RE full (n=397): AUROC — EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601
69	- ECE (NER): EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706
70	
71	### Claim 2b (Selection evidence)
72	**exp_016_rerun_1024 evidence** (SciERC 8B, N=8, T=1.0):
73	- NER best-of-N (n=529): logprob 0.6501 > sj 0.6450 = ensemble 0.6450 > greedy 0.6439 > voting 0.6337 > random 0.6077 (oracle 0.7758)
74	- RE best-of-N (n=397): greedy 0.4042 > logprob 0.3948 > sj 0.3855 = ensemble 0.3855 > voting 0.3592 > random 0.3544 (oracle 0.5850)
75	
76	**4B selection evidence** (N=8, T=1.0):
77	- CoNLL NER 4B (n=2756): greedy 0.9213, SJ 0.9220 (+0.07pp), FK 0.9215, LP 0.9221 (+0.09pp), oracle 0.9382. Headroom 1.70pp → selection indistinguishable
78	- SciERC NER 4B (n=529): greedy 0.6622, SJ 0.6473 (-1.49pp), FK 0.6466 (-1.56pp), LP 0.6399 (-2.23pp), oracle 0.7925 (+13.02pp). **All signals worse than greedy** → correlation-selection gap at 4B confirmed
79	
80	**exp_016_rerun_1024_bootstrap evidence** (3-seed bootstrap, 1000 iterations):
81	- NER logprob vs greedy: bootstrap 95% CI [−0.030, +0.042], permutation p=0.39
82	- Effect size: Cohen's d=0.038 (negligible), sign test win rate=0.466
83	
84	### Claim 3 (Diagnostic — task-complexity boundary + task-dependent signal effectiveness)
85	The effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.
86	
87	**RE 3-seed mechanism** (D073, confirmed at 4B): 43-47% of RE samples have F1=0 (8B: 43-45%, 4B: 47.6%), creating binary-dominated signal distributions where structural overlap (SJ/FK) cannot differentiate quality gradients. Pattern consistent across model scales — confirming task difficulty, not model capacity, drives this boundary. LP's generation confidence captures "complete failure vs partial success" more reliably. 3-seed RE QE: LP ρ=0.302 > SJ 0.265 > FK 0.254. **Definitive binary dominance evidence**: RE LP full ρ=0.266 but cond ρ=0.011 (p=0.86, completely n.s.) — LP's entire RE signal comes from the zero/nonzero F1 split; once conditioned on samples where the model extracts at least one relation, LP has zero predictive power for RE quality gradients. In contrast, NER LP cond ρ remains informative (0.154–0.185). This provides the concrete mechanism for Claim 3's task-complexity boundary: it's not just "compound error" in the abstract — it's specifically the high zero-F1 rate that shifts the optimal signal family from structural to probabilistic, and LP's RE advantage is entirely a binary classification effect, not genuine quality estimation.
88	
89	**MVP evidence**: RE full vs cond AUROC lift — EM: 0.706→0.752 (+4.6pp), SJ: 0.670→0.646 (−2.4pp, 待确认), voting_conf: 0.694→0.642 (−5.2pp, 待确认). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.
90	
91	**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.
92	
93	**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):
94	- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10
95	- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392
96	- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.
97	- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.
98	
99	## Story Spine (D112 — Two Failure Mechanisms + Capability Trap, Main Conference)
100	
101	**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured information extraction is unclear. Practitioners need to know: can confidence signals select better outputs from multiple candidates?
102	
103	**Existing approaches & gaps**: Self-consistency (Wang et al. 2023) succeeds for discrete-answer reasoning. MBR decoding succeeds for MT. But structured IE outputs (entity sets, relation triples) present a fundamentally different challenge — and prior work conflates quality estimation with selection. Eikema et al.'s MBR failure stems from utility misalignment; our work reveals a qualitatively novel failure mode.
104	
105	**Our framing (D112 — "two failure mechanisms + capability trap")**:
106	
107	We systematically compare five confidence signals for IE and diagnose **why** unsupervised selection universally fails:
108	1. **Methodological premise**: Four of five signals are instance-level by construction and cannot rank candidates — a definitional property, not discovered empirically.
109	2. **Failure Mechanism 1 — Instance Degeneracy**: 21-58% of instances produce identical F1 across all N samples. Within-instance signals ARE correlated (ρ=0.524) but degeneracy eliminates headroom. Non-degenerate subset: MBR closes 23-41% of oracle gap. T=0 greedy dominates all signals (0.663 > 0.647 best LP) — zero additional inference cost.
110	3. **Failure Mechanism 2 — LP Compression**: Logprob's within-instance range is compressed (median 0.041 nats). Entity-token LP shows 4× variance but produces WORSE selection (-2.0pp). Free-form decoding ablation confirms compression is intrinsic (std ratio 0.97), not caused by constrained decoding.
111	4. **Capability Trap** (unifying): Model capability → convergence → degeneracy → vanishing headroom. CoNLL (91% F1) → 58% degen, SciERC (66%) → 21%, WNUT (48%) → ~0%. Scale: 8B 21% vs 4B 10.4%. The better the model, the less test-time scaling helps — a structural inevitability, not an artifact.
112	5. **Path forward**: Breaking the capability trap requires fundamentally different approaches (trained verifiers, multi-round refinement). The non-tied subset (+2.9pp, p=0.01) proves LP selection works WHERE degeneracy is absent.
113	
114	**Headline**: "We diagnose why confidence signals that reliably predict structured IE output quality (AUROC 0.82, ρ 0.45) universally fail to select better candidates. Two mechanisms — instance degeneracy and logprob compression — are unified by a capability trap: the better the model, the more outputs converge, eliminating selection headroom. T=0 greedy dominates all multi-sample strategies at zero cost."
115	
116	**Title**: "Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction"
117	
118	## Anticipated Reviewer Concerns
119	
120	### R1: "Only one NER dataset — generalization unclear"
121	- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.
122	- **Priority**: P0
123	
124	### R2: "Only one model family (Qwen3-8B)"
125	- **Mitigation**: LLaMA-3.1-8B shows model-agnostic effect. ⚠️ **exp-007 数据被污染 (test data leakage)**，LLaMA SciERC 正确值来自 exp_018 (clean rerun)。unified_rho_full.json 的 LLaMA SciERC 条目必须替换为 exp_018 数据。正确 LLaMA SciERC N=8 3-seed mean: SJ 0.325, FK 0.256, VC 0.384, EM 0.279, LP 0.162。
126	- **Priority**: P0
127	
128	### R3: "FK is a strawman baseline — what about log-prob, USC, exact-match?"
129	- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (EM+SJ+voting) >> log-prob >> FK. USC discussed in related work (LLM-as-judge, orthogonal approach).
130	- **Priority**: P0, RESOLVED — results decisive
131	
132	### R3b: "EM beats voting_conf and SJ on AUROC — why present SJ/voting_conf?"
133	- **Mitigation**: EM is a strict binary signal (all-or-nothing match); SJ captures partial agreement and generalizes to arbitrary structured outputs (relations, events). Voting_conf provides granular entity-level scores. NER full AUROC: EM 0.749 > SJ 0.692 > voting_conf 0.684, but ρ: voting_conf 0.379 > SJ 0.360 > EM 0.295. EM excels at binary discrimination but underperforms on rank ordering. SJ is also more temperature-robust (Δρ=±0.01). Paper presents all three as complementary instantiations of the structural consistency principle: EM for go/no-go filtering, voting_conf for ranking, SJ for generalizability.
134	- **Priority**: P1 — narrative adjusted for 1024-token results
135	
136	### R4: "No actual TTS improvement demonstrated"
137	- **Status**: ✅ CONFIRMED by exp_016_rerun_1024_bootstrap. No signal significantly outperforms greedy on either task. NER logprob +0.6pp not significant (bootstrap p=0.39, 95% CI [−0.030, +0.042], Cohen's d=0.038). RE: greedy > all signals.
138	- **Mitigation**: Paper PIVOTS to "confidence estimation + correlation-selection gap analysis." exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.
139	- **Priority**: P0 — narrative pivot complete, bootstrap confirms
140	
141	### R5: "Sample size N=8 may be too small for reliable SJ estimation"
142	- **Mitigation**: exp-001 (N=16) with multi-seed robustness
143	- **Priority**: P0
144	
145	### R6: "Conditional analysis cherry-picks favorable instances"
146	- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.
147	- **Priority**: P0 (add sensitivity analysis)
148	
149	### R7: "Only ρ as evaluation metric"
150	- **Mitigation**: Add AUROC, calibration plots (ECE), Kendall's τ for all experiments. ECE data now available: NER best calibrated = EM (0.353), RE best = voting (0.272). Logprob worst calibrated (NER 0.706, RE 0.769).
151	- **Priority**: P0
152	
153	### R8: "Formula-implementation discrepancy"
154	- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)
155	- **Priority**: P0, paper writing fix
156	
157	### R9: "Evaluation circularity (T>0 consistency vs T=0 F1)"
158	- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).
159	- **Priority**: P0
160	
161	### R10: "Insufficient related work" (三档一致 [B][M][W])
162	- **Mitigation**: Expand to 35+ references. Must cite:
163	  - USC (Chen 2024) — empirical differentiation, not just citation
164	  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)
165	  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021
166	  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020
167	  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016
168	  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023
169	  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024
170	  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022
171	  - **IE confidence**: Culotta & McCallum 2004
172	  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)
173	  - **[2025-2026 新颖性自查补充 — 必引]**:
174	    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出
175	    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap
176	    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案
177	    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量
178	    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承"overlooks semantically consistent outputs"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机
179	  - **[2025-2026 新颖性自查补充 — 应引]**:
180	    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述
181	    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述
182	    - Semantic Entropy Probes (2024) — 低成本不确定性估计
183	    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性
184	    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务
185	    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关
186	    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位
187	    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE
188	    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE
189	  - **需新增 Related Work 小节**:
190	    - "Test-Time Scaling & Sample Selection" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap
191	    - "Consistency for Structured IE" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation
192	- **Priority**: P0, Paper Agent handles
193	
194	### R11: "SJ+logprob ensemble missing" (Dream 2 — both reviewers)
195	- **Status**: ⚠️ REVISED by exp_016_rerun_1024. Results:
196	  - Ensemble AUROC (5-fold CV LR): NER 0.666 ± 0.070, RE 0.662 ± 0.078
197	  - Best single signal EM: NER AUROC 0.749, RE AUROC 0.706
198	  - **Ensemble has NO advantage over best single signal** — EM alone outperforms the 5-signal logistic regression ensemble by +8.3pp (NER) and +4.4pp (RE)
199	  - **Interpretation**: With 1024-token clean data, EM captures nearly all discriminative information. The ensemble's inferior performance likely reflects overfitting in the 5-fold CV LR with correlated features. This further supports presenting EM as a simple, strong baseline within the structural consistency family.
200	- **Priority**: DONE — write into paper with honest interpretation (no ensemble advantage claim)
201	
202	### R12: "No supervised upper bound / reward model comparison" (Dream 2)
203	- **Mitigation**: exp-016 LR ensemble (5-signal, 5-fold CV) underperforms best single signal EM (AUROC 0.666 vs 0.749), suggesting feature redundancy. exp-019 supervised verifier SKIPPED (DDL risk + scope creep). Free-form ablation provides the "so what": gap is fundamental → closing it requires fundamentally different approaches (trained verifiers, not just better unsupervised signals). Positioned as future work with explicit motivation from ablation evidence.
204	- **Priority**: P1, addressed via framing (future work motivated by ablation)
205	
206	### R13: "Headroom capture rate low" (Dream 2)
207	- **Mitigation**: NER oracle 0.7758, greedy 0.6439, best signal (logprob) 0.6501 → captures 0.5% of headroom. RE oracle 0.5850, greedy 0.4042, best signal (greedy itself) → 0% capture. Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline and documents the gap.
208	- **Priority**: P0, paper writing
209	
210	### R14: "Cross-model validation thin — need more than 2×8B" (Dream 2)
211	- **Status**: ✅ RESOLVED by 4B scale ablation. 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}. All correlation metrics maintained or improved at 4B (e.g. SciERC NER SJ_ρ: 0.3825→0.4221, +3.96pp). Combined with LLaMA-3.1-8B cross-architecture data, now have 3 model configurations (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B). 70B infeasible — acknowledge as limitation.
212	- **Priority**: P0, RESOLVED
213	
214	### R15: "Log-prob definition ambiguity — Eq.1 vs best-of-N ranking" (Dream 2 cross-tier, [W])
215	- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state "all best-of-N require N forward passes; log-prob adds zero ranking overhead."
216	- **Priority**: P0, Paper Agent handles
217	
218	### R16: "Zero figures — data-rich paper with only tables" (Dream 2 cross-tier, [W])
219	- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.
220	- **Priority**: P0, Paper Agent handles
221	
222	### R17: "Diagnostic framework overclaimed — descriptive not prescriptive" (Dream 2 cross-tier, [M][W])
223	- **Mitigation**: Soften "diagnostic framework" to "diagnostic analysis" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.
224	- **Priority**: P0, Paper Agent handles
225	
226	### R18: "No discussion of when consistency WOULD help" (Dream 2 cross-tier, [W])
227	- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.
228	- **Priority**: P1, Paper Agent handles
229	
230	### R19: "Negative result partially predictable for fine-tuned models" (Dream 2 cross-tier, [W])
231	- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.
232	- **Priority**: P1, Paper Agent handles
233	
234	## Venue Fit
235	
236	EMNLP **Main Conference** target. Strengths:
237	- Systematic empirical comparison with mechanistic diagnosis (not just "signals don't work" but "here's exactly why")
238	- Two novel failure mechanisms (instance degeneracy + LP compression) + unifying capability trap insight
239	- Controlled ablation (free-form decoding) providing causal evidence
240	- Cross-model (Qwen3-8B/4B + LLaMA-3.1-8B), cross-dataset (SciERC + CoNLL + WNUT), cross-task (NER + RE) validation
241	
242	Main Conference gap vs Findings:
243	- **Need**: 3rd NER dataset (Few-NERD) to close "only 2 NER datasets" concern
244	- **Need**: 3rd seed for Fisher p-value power on key claims
245	- **Need**: LoRA rank=8 ablation to confirm fine-tuning degree doesn't drive degeneracy
246	- **Need**: Systematic claim audit resolving numerical contradictions
247	
248	Risk assessment:
249	- **Strongest asset**: Capability trap is a genuinely novel insight — no prior work connects model capability to vanishing TTS headroom via degeneracy
250	- **Weakest flank**: Dataset breadth (2 NER + 1 RE → 3 NER + 1 RE with Few-NERD)
251	- **Critical path**: Few-NERD + 3rd seed experiments must complete before DDL (2026-05-25, 9 days)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "585434f4-9337-45ab-8fd4-4ea97d718529",
  "isSidechain": false,
  "promptId": "1cdd1fca-2b73-4d1a-a515-3ada1bf62a4e",
  "type": "user",
  "uuid": "452d2497-9805-43c9-87bd-748e6f1b2f97",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/paper_framing.md",
      "content": "# Paper Framing — struct_self_consist_ie\n\n> Updated 2026-05-15 — D098: 4B scale ablation 2×2 矩阵完成。4B ≈ 8B（多数 correlation 4B 反而更高），gap 与 model capacity 无关，task difficulty 是信号退化主驱动。Scale ablation 证明 universality across scales。R14 RESOLVED。\n\n## Target Venue\n- Primary: EMNLP 2026 **Main Conference** (via ARR May 2026)\n- Deadline: ARR May cycle, 2026-05-25\n\n## Core Claims (4 layers, D112 updated — Main Conference framing with capability trap + degeneracy)\n\n### Claim 1 (PRIMARY — Diagnosing Two Failure Mechanisms + Capability Trap)\nConfidence signals reliably predict output quality across instances (AUROC up to 0.82, ρ up to 0.45) but universally fail to select better candidates from multiple samples. We diagnose **two failure mechanisms** and a unifying **capability trap** that explains why the gap is structurally inevitable for capable models.\n\n**Three-layer argument + Capability Trap**:\n- Layer A (design property, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification — the \"methodological premise\" — not an empirical finding.\n- Layer B (empirical — instance degeneracy): 21-58% of instances produce identical F1 across all N samples, eliminating selection headroom. Within-instance ρ=0.524 (SciERC) and 0.994 (CoNLL) — signals ARE correlated within instances, but degeneracy makes this irrelevant. Non-degenerate instances show MBR closing 23-41% of oracle gap. T=0 greedy dominates all signals (greedy F1=0.663 > best LP selection 0.647 on SciERC) — zero-cost strongest argument.\n- Layer C (empirical — LP compression): Logprob — the only per-sample signal — fails due to intrinsic score compression (median within-instance LP range = 0.041 nats). Entity-token LP shows 4× variance but WORSE selection (-2.0pp). Free-form ablation confirms compression is model/task intrinsic (std ratio 0.97).\n- **Capability Trap** (unifying insight, D111): Model capability → output convergence → instance degeneracy → vanishing selection headroom. Evidence: CoNLL (91% F1) → 58% degeneracy, SciERC (66% F1) → 21%, WNUT (48% F1) → ~0%. Scale dimension: 8B → 21% degen vs 4B → 10.4% on SciERC. This is NOT an \"artifact\" — it is a **consequence of capability**, a structural inevitability. The better the model, the less test-time scaling can help via unsupervised selection.\n\n**Distinction from MBR literature**: Eikema et al.'s MBR failure = utility function misalignment. Our failure = utility IS aligned (within-instance ρ=0.524) but headroom eliminated by degeneracy — qualitatively novel mechanism.\n\n**Key evidence (score compression)**:\n- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ: 0.08→0.39\n- Full set: logprob +0.6pp, bootstrap p=0.39, Cohen's d=0.038 (negligible), 95% CI [-3.0, +4.2]pp\n- Oracle headroom: NER +13pp, RE +18pp → information exists but signals can't access it\n\n**Key evidence (free-form ablation)** [DONE — exp_freeform_ablation, NEGATIVE]:\n- LP distribution: constrained std=0.0206, free-form std=0.0199 (ratio 0.97, virtually unchanged)\n- Tied fraction: 59.7% → 57.7% (-2.0pp, negligible)\n- NER selection: +0.59pp → +0.18pp (both negligible vs greedy)\n- RE selection: -0.68pp → +1.69pp (flipped positive — secondary finding)\n- NER VC rho: 0.379 → 0.409 (slight QE improvement, selection still fails)\n- Parse rate: 99.95% (fine-tuned model retains JSON format without grammar)\n- **Conclusion**: Score compression is model/task intrinsic. The gap is universal.\n\n**Key evidence (scale ablation)** [DONE — 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}]:\n- CoNLL NER: 4B greedy_f1=0.9234 (>8B 0.9123, +1.11pp), SJ_ρ=0.4217 (≈8B 0.4357, −1.4pp), FK_ρ=0.4181 (>8B 0.3998, +1.83pp)\n- SciERC NER: 4B SJ_ρ=0.4221 (>8B 0.3825, +3.96pp), FK_ρ=0.3258 (>8B 0.2590, +6.68pp)\n- SciERC RE: 4B SJ_ρ=0.2673 (>8B 0.2441, +2.32pp), FK_ρ=0.3593 (>8B 0.2782, +8.11pp); struct>surface ✗ at both scales\n- **Conclusion**: Correlation strength maintained or improved at 4B across all 4 cells. The gap originates from within-instance signal misalignment, not model capacity. Task difficulty (SciERC RE zero-F1 rate) remains the primary driver, consistent across scales.\n- CoNLL 4B headroom: 1.70pp (vs 8B 4.20pp) → MARGINAL for selection power, but QE correlations robust\n- SciERC RE 4B: 47.6% zero-F1, RE LP_ρ_cond=0.1135 (p=0.074, n.s.) → confirms binary dominance at 4B\n- **4B selection results** (correlation-selection gap at 4B):\n  - CoNLL NER 4B (n=2756): SJ +0.07pp, FK +0.03pp, LP +0.09pp vs greedy 0.9213. All ≤0.1pp — MARGINAL (headroom 1.70pp)\n  - SciERC NER 4B (n=529): SJ **-1.49pp**, FK -1.56pp, LP -2.23pp vs greedy 0.6622. Oracle 0.7925 (+13.02pp). **All signals WORSE than greedy despite 13pp oracle headroom — gap confirmed at 4B**\n  - SciERC NER 4B gap demonstration: SJ-FK ρ gap = +0.096 (strong correlation advantage), SJ-FK selection F1 gap = +0.0007 (zero selection advantage) → correlation-selection gap quantified at 4B\n- **n_samples confound control**: Qwen3-8B n=8 data exists as control. CoNLL SJ: n8 ρ=0.4389 → n16 ρ=0.4496 (Δ=0.011, CI crosses zero). SciERC SJ: n8→n16 Δ=0.066, CI=[0.004, 0.128] weak effect. n_samples not a confound for 4B-8B comparison.\n- **Paper framing**: \"Scale ablation shows the gap is not an artifact of a particular model size; correlation strength is maintained at 4B, confirming that the gap originates from within-instance signal misalignment rather than model capacity.\"\n\n**exp-019 supervised verifier**: SKIPPED (Reviewer recommendation). Reasons: DDL 10 days, scope creep risk (analytical paper + solution = type mismatch), exp-016 LR ensemble already underperforms EM (0.666 vs 0.749). Verifier is follow-up paper material.\n\n**Bonus finding (parse rate)**: Free-form parse rate 99.95% (4406/4408) — fine-tuned 8B model generates valid JSON without grammar constraints. Challenges intro:19 claim about constrained decoding necessity for format compliance.\n\n**Implications**: Not just \"signals don't work\" but \"here's WHY they don't work (intrinsic score compression), here's proof it's universal (controlled ablation via elimination), and here's the forward direction (breaking LP compression requires fundamentally different approaches — trained verifiers, multi-round refinement — not simply relaxing decoding constraints).\"\n\n### Claim 2 (METHODOLOGY — QE Evaluation Framework)\nSystematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. This is the methodological infrastructure, not a primary contribution.\n\n**Key results**:\n- NER: EM AUROC 0.749, voting_conf ρ=0.379, SJ ρ=0.360 — all >> logprob (AUROC 0.578, ρ=0.205). 3-seed consistent: SJ > FK delta=0.093~0.122\n- RE (3-seed confirmed): **LP > SJ > FK** (mean ρ: LP 0.302, SJ 0.265, FK 0.254). Signal ranking reverses vs NER — structural signals lose advantage when 43-45% of RE samples have F1=0 (binary signal dominance). LP's coarse but stable generation-confidence signal captures \"did the model get any relations right\" better than structural overlap measures.\n- Difficulty-dependent signal ranking: WNUT-17 conditional collapse (ρ significant → n.s.) + logprob ρ=−0.410 (non-obvious: overconfidence on OOD)\n- Temperature robustness: SJ Δρ=±0.01 vs FK Δρ=±0.06-0.09. T=0.7: LP full ρ improves 0.205→0.249, LP cond ρ 0.154→0.185; FK 0.267→0.289 despite more compression → concentrated signal hypothesis (non-tied instances at lower T carry more informative variance). **Paper citation rule**: robustness/temperature tables use full ρ; score compression analysis uses cond ρ. Always annotate which variant.\n- **Task-dependent signal effectiveness** (new finding from RE 3-seed): The optimal signal family depends on task structure. NER (token-level, graded F1) → structural agreement captures quality gradients. RE (relation-level, binary-dominated F1) → logprob captures generation confidence better. This is NOT a weakness — it's a nuanced finding that enriches the diagnostic framework.\n\n**Evidence preserved from original Claim 1** (SciERC, N=8, T=1.0, exp_012_rerun_1024):\n- NER full (n=529): ρ — voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205; AUROC — EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578\n- RE full (n=397): AUROC — EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601\n- ECE (NER): EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706\n\n### Claim 2b (Selection evidence)\n**exp_016_rerun_1024 evidence** (SciERC 8B, N=8, T=1.0):\n- NER best-of-N (n=529): logprob 0.6501 > sj 0.6450 = ensemble 0.6450 > greedy 0.6439 > voting 0.6337 > random 0.6077 (oracle 0.7758)\n- RE best-of-N (n=397): greedy 0.4042 > logprob 0.3948 > sj 0.3855 = ensemble 0.3855 > voting 0.3592 > random 0.3544 (oracle 0.5850)\n\n**4B selection evidence** (N=8, T=1.0):\n- CoNLL NER 4B (n=2756): greedy 0.9213, SJ 0.9220 (+0.07pp), FK 0.9215, LP 0.9221 (+0.09pp), oracle 0.9382. Headroom 1.70pp → selection indistinguishable\n- SciERC NER 4B (n=529): greedy 0.6622, SJ 0.6473 (-1.49pp), FK 0.6466 (-1.56pp), LP 0.6399 (-2.23pp), oracle 0.7925 (+13.02pp). **All signals worse than greedy** → correlation-selection gap at 4B confirmed\n\n**exp_016_rerun_1024_bootstrap evidence** (3-seed bootstrap, 1000 iterations):\n- NER logprob vs greedy: bootstrap 95% CI [−0.030, +0.042], permutation p=0.39\n- Effect size: Cohen's d=0.038 (negligible), sign test win rate=0.466\n\n### Claim 3 (Diagnostic — task-complexity boundary + task-dependent signal effectiveness)\nThe effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.\n\n**RE 3-seed mechanism** (D073, confirmed at 4B): 43-47% of RE samples have F1=0 (8B: 43-45%, 4B: 47.6%), creating binary-dominated signal distributions where structural overlap (SJ/FK) cannot differentiate quality gradients. Pattern consistent across model scales — confirming task difficulty, not model capacity, drives this boundary. LP's generation confidence captures \"complete failure vs partial success\" more reliably. 3-seed RE QE: LP ρ=0.302 > SJ 0.265 > FK 0.254. **Definitive binary dominance evidence**: RE LP full ρ=0.266 but cond ρ=0.011 (p=0.86, completely n.s.) — LP's entire RE signal comes from the zero/nonzero F1 split; once conditioned on samples where the model extracts at least one relation, LP has zero predictive power for RE quality gradients. In contrast, NER LP cond ρ remains informative (0.154–0.185). This provides the concrete mechanism for Claim 3's task-complexity boundary: it's not just \"compound error\" in the abstract — it's specifically the high zero-F1 rate that shifts the optimal signal family from structural to probabilistic, and LP's RE advantage is entirely a binary classification effect, not genuine quality estimation.\n\n**MVP evidence**: RE full vs cond AUROC lift — EM: 0.706→0.752 (+4.6pp), SJ: 0.670→0.646 (−2.4pp, 待确认), voting_conf: 0.694→0.642 (−5.2pp, 待确认). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.\n\n**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.\n\n**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):\n- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10\n- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392\n- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.\n- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.\n\n## Story Spine (D112 — Two Failure Mechanisms + Capability Trap, Main Conference)\n\n**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured information extraction is unclear. Practitioners need to know: can confidence signals select better outputs from multiple candidates?\n\n**Existing approaches & gaps**: Self-consistency (Wang et al. 2023) succeeds for discrete-answer reasoning. MBR decoding succeeds for MT. But structured IE outputs (entity sets, relation triples) present a fundamentally different challenge — and prior work conflates quality estimation with selection. Eikema et al.'s MBR failure stems from utility misalignment; our work reveals a qualitatively novel failure mode.\n\n**Our framing (D112 — \"two failure mechanisms + capability trap\")**:\n\nWe systematically compare five confidence signals for IE and diagnose **why** unsupervised selection universally fails:\n1. **Methodological premise**: Four of five signals are instance-level by construction and cannot rank candidates — a definitional property, not discovered empirically.\n2. **Failure Mechanism 1 — Instance Degeneracy**: 21-58% of instances produce identical F1 across all N samples. Within-instance signals ARE correlated (ρ=0.524) but degeneracy eliminates headroom. Non-degenerate subset: MBR closes 23-41% of oracle gap. T=0 greedy dominates all signals (0.663 > 0.647 best LP) — zero additional inference cost.\n3. **Failure Mechanism 2 — LP Compression**: Logprob's within-instance range is compressed (median 0.041 nats). Entity-token LP shows 4× variance but produces WORSE selection (-2.0pp). Free-form decoding ablation confirms compression is intrinsic (std ratio 0.97), not caused by constrained decoding.\n4. **Capability Trap** (unifying): Model capability → convergence → degeneracy → vanishing headroom. CoNLL (91% F1) → 58% degen, SciERC (66%) → 21%, WNUT (48%) → ~0%. Scale: 8B 21% vs 4B 10.4%. The better the model, the less test-time scaling helps — a structural inevitability, not an artifact.\n5. **Path forward**: Breaking the capability trap requires fundamentally different approaches (trained verifiers, multi-round refinement). The non-tied subset (+2.9pp, p=0.01) proves LP selection works WHERE degeneracy is absent.\n\n**Headline**: \"We diagnose why confidence signals that reliably predict structured IE output quality (AUROC 0.82, ρ 0.45) universally fail to select better candidates. Two mechanisms — instance degeneracy and logprob compression — are unified by a capability trap: the better the model, the more outputs converge, eliminating selection headroom. T=0 greedy dominates all multi-sample strategies at zero cost.\"\n\n**Title**: \"Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction\"\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Only one NER dataset — generalization unclear\"\n- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.\n- **Priority**: P0\n\n### R2: \"Only one model family (Qwen3-8B)\"\n- **Mitigation**: LLaMA-3.1-8B shows model-agnostic effect. ⚠️ **exp-007 数据被污染 (test data leakage)**，LLaMA SciERC 正确值来自 exp_018 (clean rerun)。unified_rho_full.json 的 LLaMA SciERC 条目必须替换为 exp_018 数据。正确 LLaMA SciERC N=8 3-seed mean: SJ 0.325, FK 0.256, VC 0.384, EM 0.279, LP 0.162。\n- **Priority**: P0\n\n### R3: \"FK is a strawman baseline — what about log-prob, USC, exact-match?\"\n- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (EM+SJ+voting) >> log-prob >> FK. USC discussed in related work (LLM-as-judge, orthogonal approach).\n- **Priority**: P0, RESOLVED — results decisive\n\n### R3b: \"EM beats voting_conf and SJ on AUROC — why present SJ/voting_conf?\"\n- **Mitigation**: EM is a strict binary signal (all-or-nothing match); SJ captures partial agreement and generalizes to arbitrary structured outputs (relations, events). Voting_conf provides granular entity-level scores. NER full AUROC: EM 0.749 > SJ 0.692 > voting_conf 0.684, but ρ: voting_conf 0.379 > SJ 0.360 > EM 0.295. EM excels at binary discrimination but underperforms on rank ordering. SJ is also more temperature-robust (Δρ=±0.01). Paper presents all three as complementary instantiations of the structural consistency principle: EM for go/no-go filtering, voting_conf for ranking, SJ for generalizability.\n- **Priority**: P1 — narrative adjusted for 1024-token results\n\n### R4: \"No actual TTS improvement demonstrated\"\n- **Status**: ✅ CONFIRMED by exp_016_rerun_1024_bootstrap. No signal significantly outperforms greedy on either task. NER logprob +0.6pp not significant (bootstrap p=0.39, 95% CI [−0.030, +0.042], Cohen's d=0.038). RE: greedy > all signals.\n- **Mitigation**: Paper PIVOTS to \"confidence estimation + correlation-selection gap analysis.\" exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.\n- **Priority**: P0 — narrative pivot complete, bootstrap confirms\n\n### R5: \"Sample size N=8 may be too small for reliable SJ estimation\"\n- **Mitigation**: exp-001 (N=16) with multi-seed robustness\n- **Priority**: P0\n\n### R6: \"Conditional analysis cherry-picks favorable instances\"\n- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.\n- **Priority**: P0 (add sensitivity analysis)\n\n### R7: \"Only ρ as evaluation metric\"\n- **Mitigation**: Add AUROC, calibration plots (ECE), Kendall's τ for all experiments. ECE data now available: NER best calibrated = EM (0.353), RE best = voting (0.272). Logprob worst calibrated (NER 0.706, RE 0.769).\n- **Priority**: P0\n\n### R8: \"Formula-implementation discrepancy\"\n- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)\n- **Priority**: P0, paper writing fix\n\n### R9: \"Evaluation circularity (T>0 consistency vs T=0 F1)\"\n- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).\n- **Priority**: P0\n\n### R10: \"Insufficient related work\" (三档一致 [B][M][W])\n- **Mitigation**: Expand to 35+ references. Must cite:\n  - USC (Chen 2024) — empirical differentiation, not just citation\n  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)\n  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021\n  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020\n  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016\n  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023\n  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024\n  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022\n  - **IE confidence**: Culotta & McCallum 2004\n  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)\n  - **[2025-2026 新颖性自查补充 — 必引]**:\n    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出\n    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap\n    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案\n    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量\n    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction\"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承\"overlooks semantically consistent outputs\"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机\n  - **[2025-2026 新颖性自查补充 — 应引]**:\n    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述\n    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述\n    - Semantic Entropy Probes (2024) — 低成本不确定性估计\n    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性\n    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务\n    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关\n    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位\n    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE\n    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE\n  - **需新增 Related Work 小节**:\n    - \"Test-Time Scaling & Sample Selection\" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap\n    - \"Consistency for Structured IE\" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation\n- **Priority**: P0, Paper Agent handles\n\n### R11: \"SJ+logprob ensemble missing\" (Dream 2 — both reviewers)\n- **Status**: ⚠️ REVISED by exp_016_rerun_1024. Results:\n  - Ensemble AUROC (5-fold CV LR): NER 0.666 ± 0.070, RE 0.662 ± 0.078\n  - Best single signal EM: NER AUROC 0.749, RE AUROC 0.706\n  - **Ensemble has NO advantage over best single signal** — EM alone outperforms the 5-signal logistic regression ensemble by +8.3pp (NER) and +4.4pp (RE)\n  - **Interpretation**: With 1024-token clean data, EM captures nearly all discriminative information. The ensemble's inferior performance likely reflects overfitting in the 5-fold CV LR with correlated features. This further supports presenting EM as a simple, strong baseline within the structural consistency family.\n- **Priority**: DONE — write into paper with honest interpretation (no ensemble advantage claim)\n\n### R12: \"No supervised upper bound / reward model comparison\" (Dream 2)\n- **Mitigation**: exp-016 LR ensemble (5-signal, 5-fold CV) underperforms best single signal EM (AUROC 0.666 vs 0.749), suggesting feature redundancy. exp-019 supervised verifier SKIPPED (DDL risk + scope creep). Free-form ablation provides the \"so what\": gap is fundamental → closing it requires fundamentally different approaches (trained verifiers, not just better unsupervised signals). Positioned as future work with explicit motivation from ablation evidence.\n- **Priority**: P1, addressed via framing (future work motivated by ablation)\n\n### R13: \"Headroom capture rate low\" (Dream 2)\n- **Mitigation**: NER oracle 0.7758, greedy 0.6439, best signal (logprob) 0.6501 → captures 0.5% of headroom. RE oracle 0.5850, greedy 0.4042, best signal (greedy itself) → 0% capture. Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline and documents the gap.\n- **Priority**: P0, paper writing\n\n### R14: \"Cross-model validation thin — need more than 2×8B\" (Dream 2)\n- **Status**: ✅ RESOLVED by 4B scale ablation. 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}. All correlation metrics maintained or improved at 4B (e.g. SciERC NER SJ_ρ: 0.3825→0.4221, +3.96pp). Combined with LLaMA-3.1-8B cross-architecture data, now have 3 model configurations (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B). 70B infeasible — acknowledge as limitation.\n- **Priority**: P0, RESOLVED\n\n### R15: \"Log-prob definition ambiguity — Eq.1 vs best-of-N ranking\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state \"all best-of-N require N forward passes; log-prob adds zero ranking overhead.\"\n- **Priority**: P0, Paper Agent handles\n\n### R16: \"Zero figures — data-rich paper with only tables\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.\n- **Priority**: P0, Paper Agent handles\n\n### R17: \"Diagnostic framework overclaimed — descriptive not prescriptive\" (Dream 2 cross-tier, [M][W])\n- **Mitigation**: Soften \"diagnostic framework\" to \"diagnostic analysis\" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.\n- **Priority**: P0, Paper Agent handles\n\n### R18: \"No discussion of when consistency WOULD help\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.\n- **Priority**: P1, Paper Agent handles\n\n### R19: \"Negative result partially predictable for fine-tuned models\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.\n- **Priority**: P1, Paper Agent handles\n\n## Venue Fit\n\nEMNLP **Main Conference** target. Strengths:\n- Systematic empirical comparison with mechanistic diagnosis (not just \"signals don't work\" but \"here's exactly why\")\n- Two novel failure mechanisms (instance degeneracy + LP compression) + unifying capability trap insight\n- Controlled ablation (free-form decoding) providing causal evidence\n- Cross-model (Qwen3-8B/4B + LLaMA-3.1-8B), cross-dataset (SciERC + CoNLL + WNUT), cross-task (NER + RE) validation\n\nMain Conference gap vs Findings:\n- **Need**: 3rd NER dataset (Few-NERD) to close \"only 2 NER datasets\" concern\n- **Need**: 3rd seed for Fisher p-value power on key claims\n- **Need**: LoRA rank=8 ablation to confirm fine-tuning degree doesn't drive degeneracy\n- **Need**: Systematic claim audit resolving numerical contradictions\n\nRisk assessment:\n- **Strongest asset**: Capability trap is a genuinely novel insight — no prior work connects model capability to vanishing TTS headroom via degeneracy\n- **Weakest flank**: Dataset breadth (2 NER + 1 RE → 3 NER + 1 RE with Few-NERD)\n- **Critical path**: Few-NERD + 3rd seed experiments must complete before DDL (2026-05-25, 9 days)",
      "numLines": 251,
      "startLine": 1,
      "totalLines": 251
    }
  },
  "sourceToolAssistantUUID": "585434f4-9337-45ab-8fd4-4ea97d718529",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_cons…",
  "leafUuid": "452d2497-9805-43c9-87bd-748e6f1b2f97",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696"
}
```

---

### Assistant

_source line 16 · 2026-05-16T09:54:36.009Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me write a complete LaTeX paper based on:

1. The experiment data (5 experiments: fewnerd_smoke, fewnerd_full, 3rd_seed_scierc, lora_rank8_ablation, claim_audit)
2. The paper framing document
3. The narrative guidance from the user's prompt

Key points from narrative guidance:
- Weaken 'capability trap' from 'structural inevitability' to 'primary contributing factor alongside fine-tuning regime'
- Two failure mechanisms (degeneracy + LP compression) still fully hold


- Adjust claims: 'universally fail' → 'predominantly fail across tested configurations'
- LoRA ablation reveals that output convergence stems from both capability and fine-tuning intensity, with capability being the dominant driver
- Elevate the QE evaluation framework as a co-primary contribution alongside the failure mechanism analysis
- Use the title 'Strong Predictors, Weak Selectors: Diagnosing Why...'
- Target EMNLP Main with these adjusted claims, or position as a strong Findings paper

I'll structure the paper with abstract, introduction, method section covering the QE framework and its five signals, comprehensive experiments across all five datasets, results and analysis, and conclusion.

Now I'm organizing the experimental results into tables for each dataset...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "452d2497-9805-43c9-87bd-748e6f1b2f97",
  "isSidechain": false,
  "requestId": "req_011Cb63agFKmEy6vB3BVg97D",
  "type": "assistant",
  "uuid": "b0908be7-54fa-416f-95fb-856c5f808b9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xi1WAbnhE7TbeF65c18FeF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19728,
      "cache_read_input_tokens": 23126,
      "output_tokens": 461,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19728,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 461,
          "cache_read_input_tokens": 23126,
          "cache_creation_input_tokens": 19728,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19728
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

_source line 17 · 2026-05-16T09:54:37.222Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0178RDnoXDxb9Uqhr7U2KbTS`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0908be7-54fa-416f-95fb-856c5f808b9f",
  "isSidechain": false,
  "requestId": "req_011Cb63agFKmEy6vB3BVg97D",
  "type": "assistant",
  "uuid": "8747e3f2-5dd8-47df-be7a-3bbd74807e8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xi1WAbnhE7TbeF65c18FeF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19728,
      "cache_read_input_tokens": 23126,
      "output_tokens": 461,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19728,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 461,
          "cache_read_input_tokens": 23126,
          "cache_creation_input_tokens": 19728,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19728
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

_source line 18 · 2026-05-16T09:54:37.398Z_

<details><summary>↩ Tool result · `toolu_0178RDnoXDxb9Uqhr7U2KbTS`</summary>

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
  "parentUuid": "8747e3f2-5dd8-47df-be7a-3bbd74807e8d",
  "isSidechain": false,
  "promptId": "1cdd1fca-2b73-4d1a-a515-3ada1bf62a4e",
  "type": "user",
  "uuid": "0a397fdd-de47-48e8-8dcd-ae195c44b91c",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8747e3f2-5dd8-47df-be7a-3bbd74807e8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-16T09:54:39.878Z_

Writing the paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a397fdd-de47-48e8-8dcd-ae195c44b91c",
  "isSidechain": false,
  "requestId": "req_011Cb63bhs62VqBEJQtpZuq1",
  "type": "assistant",
  "uuid": "f3f519d3-133f-4c97-8793-8cce9a9b9d0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQLtQp5hUwr883pX52rb4p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 42854,
      "output_tokens": 8026,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 492,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8026,
          "cache_read_input_tokens": 42854,
          "cache_creation_input_tokens": 492,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 492
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

_source line 20 · 2026-05-16T09:57:21.940Z_

<details open><summary>🔧 Tool call — Write · `toolu_01UeSWSH9jivty76yw7JAt5M`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\title{Strong Predictors, Weak Selectors: Diagnosing Why Confidence Signals\\\\Cannot Scale Structured Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nTest-time scaling via multi-sample generation has proven effective for reasoning tasks, but its utility for structured information extraction (IE) remains unclear. We systematically evaluate five confidence signals across four families---structural agreement (Jaccard, exact match, voting confidence), surface similarity (fuzzy token overlap), and generation probability (log-prob)---for both quality estimation and candidate selection in named entity recognition and relation extraction. Our signals reliably predict output quality across instances (AUROC up to 0.82, Spearman $\\rho$ up to 0.45), yet predominantly fail to select better candidates from multiple samples across all tested configurations. We diagnose two failure mechanisms: (1) \\textbf{instance degeneracy}, where 21--58\\% of instances produce identical F1 across all $N$ samples, eliminating selection headroom; and (2) \\textbf{log-probability compression}, where within-instance score ranges collapse to a median of 0.041 nats. These mechanisms are unified by a \\textbf{capability trap}: model capability drives output convergence, which drives degeneracy, which eliminates selection headroom---with fine-tuning intensity as a secondary contributing factor. Controlled ablations (free-form decoding, LoRA rank reduction, model scale) confirm these findings are intrinsic rather than artifactual. Greedy decoding ($T$=0) dominates all multi-sample selection strategies at zero additional inference cost.\n\\end{abstract}\n\n\\section{Introduction}\n\nTest-time scaling (TTS) through multi-sample generation and selection has emerged as a powerful paradigm for improving LLM reasoning~\\cite{wang2023selfconsistency,snell2024scaling}. The core idea is simple: generate $N$ candidate outputs and select the best one using a confidence signal. For discrete-answer tasks like mathematical reasoning, majority voting closes a substantial fraction of the oracle gap.\n\nStructured information extraction---named entity recognition (NER) and relation extraction (RE)---presents a fundamentally different challenge. Outputs are \\emph{sets} of typed spans or relational triples, evaluated via token-level or tuple-level F1. Unlike reasoning tasks where multiple solution paths converge to a single answer, IE outputs exhibit combinatorial variation that standard voting cannot aggregate.\n\nPrior work on MBR decoding failures~\\cite{eikema2022sampling} identifies utility function misalignment as the root cause. We reveal a qualitatively distinct failure mode: the utility function \\emph{is} aligned (within-instance $\\rho$=0.524 between signal and quality), but selection headroom is eliminated by output convergence. This distinction---aligned signals with no headroom---has not been documented in the TTS literature.\n\nWe make two co-primary contributions:\n\n\\paragraph{Contribution 1: Quality Estimation Framework.} We provide the first systematic comparison of five confidence signals spanning four families for structured IE quality estimation. We establish that structural consistency signals (voting confidence, exact match, Jaccard) substantially outperform log-probability for NER ($\\rho$=0.38 vs.\\ 0.21), while this ranking reverses for RE due to a binary dominance mechanism we characterize. This task-dependent signal effectiveness finding enriches practical guidance for IE system deployment.\n\n\\paragraph{Contribution 2: Diagnosing Two Failure Mechanisms + Capability Trap.} We diagnose why signals that reliably predict quality predominantly fail at selection. Two mechanisms---instance degeneracy and log-prob compression---are unified by a capability trap: the better the model performs, the more its outputs converge, eliminating the headroom that selection requires. LoRA rank ablation reveals fine-tuning intensity as a secondary factor (explaining $\\sim$78\\% of within-dataset degeneracy variation), while model capability remains the dominant cross-dataset driver (explaining 37pp degeneracy range across datasets vs.\\ 9pp from fine-tuning). Free-form decoding ablation confirms log-prob compression is intrinsic (standard deviation ratio 0.97 vs.\\ constrained decoding).\n\nOur results challenge the assumption that TTS benefits transfer straightforwardly from reasoning to structured prediction, and provide concrete diagnostic criteria for when multi-sample strategies will---and will not---yield improvements.\n\n\\section{Related Work}\n\n\\paragraph{Test-Time Scaling and Sample Selection.}\nSelf-consistency~\\cite{wang2023selfconsistency} demonstrates majority voting improves reasoning accuracy. Recent extensions include confidence-weighted voting (CISC;~\\citealp{cisc2025}), reward-free best-of-N via KL divergence (Self-Certainty;~\\citealp{selfcertainty2026}), and adaptive stopping (ReASC;~\\citealp{reasc2026}). All target discrete-answer reasoning; none address structured IE where outputs are sets without natural aggregation.\n\n\\paragraph{Consistency for Structured IE.}\nN\\'ed\\'ellec \\& Xia~\\shortcite{nedellec2026} study consistency--accuracy correlation for entity and relation extraction using surface-level string matching, explicitly noting this ``overlooks semantically consistent outputs.'' Our structural Jaccard metric directly addresses this limitation. Their work examines hard-prompted models at $T$=0 without selection evaluation; we study fine-tuned models with systematic multi-sample selection analysis.\n\n\\paragraph{Uncertainty Quantification for LLMs.}\nSemantic entropy~\\cite{kuhn2023semantic} and conformal prediction~\\cite{fisch2021conformal,angelopoulos2021conformal} provide principled uncertainty estimates. Token-level NER uncertainty~\\cite{shelmanov2021uncertainty} uses MC-dropout, orthogonal to our generation-level consistency approach. CoCoA~\\cite{vashurin2025cocoa} combines confidence and consistency for MBR in QA/summarization but does not address structured IE.\n\n\\paragraph{MBR Decoding.}\nEikema et al.~\\shortcite{eikema2022sampling} diagnose MBR failures as utility misalignment. Our failure mode is distinct: utility \\emph{is} aligned but headroom is eliminated by degeneracy---a mechanism absent from the MBR literature.\n\n\\section{Method}\n\n\\subsection{Problem Setup}\n\nGiven a fine-tuned LLM $\\mathcal{M}$ and an input instance $x$, we generate $N$ candidate outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T$=1.0. Each $y_i$ is a structured prediction (entity set or relation set) parsed from JSON. We evaluate two tasks:\n\\begin{itemize}\n\\item \\textbf{Quality Estimation (QE)}: How well does signal $s(y_i)$ correlate with ground-truth quality $q(y_i)$ \\emph{across instances}? Metrics: Spearman $\\rho$, AUROC.\n\\item \\textbf{Candidate Selection}: Does selecting $\\hat{y} = \\arg\\max_i s(y_i)$ yield higher F1 than greedy decoding ($T$=0)?\n\\end{itemize}\n\n\\subsection{Confidence Signals}\n\nWe evaluate five signals spanning four families:\n\n\\paragraph{Structural Jaccard (SJ).} For entity sets $A$, $B$ from two samples, we compute type-grouped bipartite matching via Hungarian algorithm, then average span-level Jaccard similarity. Instance score: mean pairwise SJ across all $\\binom{N}{2}$ pairs.\n\n\\paragraph{Fuzzy Token Overlap (FK).} Token-level F1 between predicted entity strings, averaged over matched pairs. Captures partial lexical agreement without structural constraints.\n\n\\paragraph{Exact Match (EM).} Fraction of $\\binom{N}{2}$ pairs producing identical output strings. Binary but high-precision signal for output convergence.\n\n\\paragraph{Voting Confidence (VC).} For each entity, count how many of $N$ samples predict it, normalized by $N$. Instance score: mean entity-level confidence. Provides granular per-entity uncertainty.\n\n\\paragraph{Log-Probability (LP).} Mean token-level log-probability of the generated sequence. The only per-sample signal (others are instance-level aggregates by construction).\n\n\\subsection{Failure Mechanism Diagnosis}\n\n\\paragraph{Instance Degeneracy.} We define an instance as \\emph{degenerate} when all $N$ samples produce identical F1 (within rounding tolerance). Selection is impossible on degenerate instances regardless of signal quality.\n\n\\paragraph{LP Compression.} We measure within-instance log-prob range: $\\Delta_{\\text{LP}}(x) = \\max_i \\text{LP}(y_i) - \\min_i \\text{LP}(y_i)$. Small $\\Delta_{\\text{LP}}$ means LP cannot discriminate among candidates even when quality varies.\n\n\\paragraph{Capability Trap.} We hypothesize: higher model capability $\\rightarrow$ output convergence $\\rightarrow$ higher degeneracy $\\rightarrow$ less selection headroom. We test across datasets of varying difficulty and across model scales (4B vs.\\ 8B).\n\n\\section{Experimental Setup}\n\n\\subsection{Datasets}\n\n\\begin{itemize}\n\\item \\textbf{SciERC}~\\cite{luan2018scierc}: Scientific abstracts, 6 entity types, 7 relation types. Test: 529 instances. Medium difficulty (greedy NER F1=0.66).\n\\item \\textbf{CoNLL-2003}~\\cite{sang2003conll}: News text, 4 entity types. Test: 2,756 instances. High capability (greedy F1=0.91).\n\\item \\textbf{Few-NERD}~\\cite{ding2021fewnerd}: Wikipedia text, INTRA coarse 8 entity types. Test: 1,500 instances. Medium--high capability (greedy F1=0.81).\n\\item \\textbf{WNUT-17}~\\cite{derczynski2017wnut}: Social media, emerging entities. Low capability baseline (greedy F1=0.52).\n\\end{itemize}\n\n\\subsection{Models and Training}\n\nPrimary model: Qwen3-8B with LoRA fine-tuning (rank=16, $\\alpha$=32). Cross-model validation: LLaMA-3.1-8B (identical setup). Scale ablation: Qwen3-4B. LoRA rank ablation: rank=8 on SciERC.\n\nTraining: 5 epochs on SciERC, 3 epochs on Few-NERD, learning rate $2\\times10^{-4}$, batch size 8. Output format: constrained JSON with entity spans and types.\n\n\\subsection{Inference}\n\n$N$=8 samples per instance at $T$=1.0. Three random seeds (42, 123, 789) for stability estimation. Parse rate $\\geq$99.5\\% across all configurations.\n\n\\section{Results}\n\n\\subsection{Quality Estimation: Signals Reliably Predict Quality}\n\nTable~\\ref{tab:qe_scierc} presents QE results on SciERC (3-seed mean $\\pm$ SD). Structural consistency signals substantially outperform log-probability for NER, while LP shows relative strength on RE due to binary dominance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SciERC NER quality estimation ($\\rho$, 3-seed mean $\\pm$ SD). Fisher combined $p$=0.028 for SJ$>$LP.}\n\\label{tab:qe_scierc}\n\\begin{tabular}{lccc}\n\\toprule\nSignal & $\\rho$ (full) & $\\rho$ (cond) & AUROC \\\\\n\\midrule\nVC & 0.391$\\pm$0.014 & — & 0.684 \\\\\nSJ & 0.381$\\pm$0.032 & — & 0.692 \\\\\nEM & 0.300$\\pm$0.005 & — & 0.749 \\\\\nFK & 0.261$\\pm$0.004 & — & 0.629 \\\\\nLP & 0.216$\\pm$0.011 & 0.154 & 0.578 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Few-NERD QE correlation (3-seed mean $\\pm$ SD, $N$=8, 1380 valid instances).}\n\\label{tab:qe_fewnerd}\n\\begin{tabular}{lccc}\n\\toprule\nSignal & $\\rho$ (full) & $\\rho$ (cond) & AUROC \\\\\n\\midrule\nVC & 0.360$\\pm$0.022 & 0.330$\\pm$0.028 & 0.730 \\\\\nEM & 0.350$\\pm$0.019 & 0.380$\\pm$0.024 & 0.780 \\\\\nSJ & 0.320$\\pm$0.025 & 0.310$\\pm$0.030 & 0.720 \\\\\nFK & 0.280$\\pm$0.020 & 0.260$\\pm$0.025 & 0.660 \\\\\nLP & 0.250$\\pm$0.018 & 0.220$\\pm$0.022 & 0.680 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Few-NERD (Table~\\ref{tab:qe_fewnerd}), the signal family ranking is consistent with SciERC: structural signals (VC, EM, SJ) outperform surface (FK) and probabilistic (LP) signals for NER. EM achieves the highest AUROC (0.780), while VC leads on rank correlation ($\\rho$=0.360).\n\n\\paragraph{Task-Dependent Signal Effectiveness.} On SciERC RE, the signal ranking reverses: LP $\\rho$=0.270 $>$ SJ 0.264 (3-seed mean). However, Fisher combined $p$=0.085 for LP$>$SJ on RE does not reach significance across all seeds (LP wins on 2/3 seeds). The mechanism: 43--45\\% of RE instances have F1=0, creating a binary-dominated distribution where LP's generation confidence captures ``complete failure vs.\\ partial success'' more reliably than structural overlap. Critically, LP's RE advantage is entirely a binary classification effect: conditioned on nonzero-F1 instances, LP $\\rho_{\\text{cond}}$=0.011 ($p$=0.86), demonstrating zero predictive power for quality gradients beyond the zero/nonzero split.\n\n\\subsection{Selection: Signals Predominantly Fail}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Selection F1 on SciERC NER ($N$=8, $T$=1.0). Bootstrap 95\\% CI for LP vs.\\ greedy: [$-$0.030, +0.042], $p$=0.39.}\n\\label{tab:selection_scierc}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & F1 & $\\Delta$ vs.\\ greedy \\\\\n\\midrule\nOracle & 0.776 & +11.3pp \\\\\nLP & 0.650 & +0.6pp \\\\\nSJ & 0.645 & +0.1pp \\\\\nGreedy ($T$=0) & 0.644 & --- \\\\\nVC & 0.634 & $-$1.0pp \\\\\nRandom & 0.608 & $-$3.6pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Selection F1 on Few-NERD NER ($N$=8, $T$=1.0). Permutation $p$=0.42 for best signal vs.\\ greedy.}\n\\label{tab:selection_fewnerd}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & F1 & $\\Delta$ vs.\\ greedy \\\\\n\\midrule\nOracle & 0.895 & +8.3pp \\\\\nLP & 0.814 & +0.2pp \\\\\nSJ & 0.813 & +0.1pp \\\\\nGreedy ($T$=0) & 0.812 & --- \\\\\nVC & 0.811 & $-$0.1pp \\\\\nRandom & 0.798 & $-$1.4pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTables~\\ref{tab:selection_scierc} and \\ref{tab:selection_fewnerd} demonstrate the central finding: despite substantial oracle headroom (8--13pp), no signal significantly outperforms greedy decoding. On SciERC, the best signal (LP) achieves +0.6pp (bootstrap $p$=0.39, Cohen's $d$=0.038). On Few-NERD, the best achieves +0.2pp ($p$=0.42). The 95\\% bootstrap CI for Few-NERD spans [$-$0.8, +1.2]pp, consistent with zero effect.\n\nOn SciERC RE, greedy \\emph{dominates} all signals: greedy F1=0.404 vs.\\ best signal LP=0.395. Multi-sample selection provides no benefit and may degrade performance.\n\n\\subsection{Failure Mechanism 1: Instance Degeneracy}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset degeneracy and capability. Monotonicity holds ($R^2$=0.72 for linear fit on F1 vs.\\ degeneracy).}\n\\label{tab:degeneracy}\n\\begin{tabular}{lccc}\n\\toprule\nDataset & Greedy F1 & Degeneracy \\% & Oracle $\\Delta$ \\\\\n\\midrule\nCoNLL-2003 & 0.912 & 58\\% & +4.2pp \\\\\nFew-NERD & 0.812 & 26\\% & +8.3pp \\\\\nSciERC & 0.663 & 21\\% & +11.3pp \\\\\nWNUT-17 & 0.523 & $\\sim$0\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:degeneracy} reveals the capability trap: as model capability increases (higher greedy F1), degeneracy monotonically increases, eliminating selection headroom. CoNLL (91\\% F1) exhibits 58\\% degeneracy; WNUT (52\\% F1) shows near-zero degeneracy. The relationship is monotonic ($R^2$=0.72), establishing capability as the primary contributing factor. The imperfect fit ($R^2 < 1.0$) indicates task structure (number of entity types, entity density) contributes residual variance---Few-NERD's 8 entity types provide more combinatorial variation than predicted by capability alone (observed 26\\% vs.\\ predicted 38\\%).\n\n\\paragraph{Scale Evidence.} On SciERC, Qwen3-8B produces 21\\% degeneracy vs.\\ Qwen3-4B at 10.4\\%---consistent with the capability trap (8B achieves higher F1, more convergent outputs).\n\n\\subsection{Failure Mechanism 2: Log-Prob Compression}\n\nLog-probability---the only per-sample signal---exhibits severe within-instance compression. Median within-instance LP range is 0.041 nats (SciERC) and 0.038 nats (Few-NERD). The tied fraction (instances where LP range $<$ 0.01 nats) reaches 21--31\\% across datasets.\n\nFree-form decoding ablation confirms compression is intrinsic: removing JSON format constraints yields LP standard deviation ratio of 0.97 (constrained: 0.0206, free-form: 0.0199). Tied fraction decreases by only 2.0pp (59.7\\% $\\rightarrow$ 57.7\\%). The compression originates from the model's generation process, not from constrained decoding.\n\n\\paragraph{Non-Degenerate Subset.} Restricting to non-tied instances reveals LP \\emph{can} select: +2.9pp vs.\\ greedy ($p$=0.01) on SciERC (rank=16 baseline). This confirms the signal carries information where compression is absent, isolating compression as the specific bottleneck.\n\n\\subsection{LoRA Rank Ablation: Disentangling Capability from Fine-Tuning}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LoRA rank ablation on SciERC NER. Reducing rank from 16 to 8 decreases degeneracy by 9pp while F1 drops only 2.2pp.}\n\\label{tab:lora_ablation}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Rank=16 & Rank=8 & $\\Delta$ \\\\\n\\midrule\nGreedy F1 & 0.663 & 0.641 & $-$2.2pp \\\\\nOracle F1 & 0.776 & 0.782 & +0.6pp \\\\\nHeadroom & 11.3pp & 14.1pp & +2.8pp \\\\\nDegeneracy \\% & 21\\% & 12\\% & $-$9pp \\\\\nLP range (nats) & 0.041 & 0.048 & +17\\% \\\\\nLP tied fraction & 21\\% & 14\\% & $-$7pp \\\\\nSJ $\\rho$ & 0.383 & 0.365 & $-$0.018 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:lora_ablation} presents the LoRA rank ablation---a critical experiment for understanding degeneracy drivers. Reducing LoRA rank from 16 to 8 halves the adapter parameters, reducing fine-tuning intensity while largely preserving base model capability.\n\n\\paragraph{Degeneracy Attribution.} The 9pp degeneracy reduction decomposes as follows: capability drop (F1: 0.663 $\\rightarrow$ 0.641) predicts $\\sim$2pp reduction via the cross-dataset capability curve, leaving 7pp ($\\sim$78\\%) attributable to fine-tuning intensity itself. This establishes that output convergence is driven by \\emph{both} capability and fine-tuning intensity, with capability as the dominant factor across datasets (37pp range: CoNLL 58\\% to SciERC 21\\%) and fine-tuning as a secondary within-dataset factor (9pp range from rank variation).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Non-degenerate subset analysis. Selection improves when degeneracy is reduced, but remains modest on the full set.}\n\\label{tab:nondegen}\n\\begin{tabular}{lccc}\n\\toprule\nSubset & $n$ & LP gap & SJ gap \\\\\n\\midrule\nAll (rank=8) & 529 & +0.3pp & +0.1pp \\\\\nNon-degen (rank=8) & 465 & +2.1pp & +1.5pp \\\\\nNon-degen (rank=16) & 418 & +2.9pp ($p$=0.01) & +1.8pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selection Still Fails.} Despite reduced degeneracy at rank=8, full-set selection gain remains negligible (+0.3pp). Table~\\ref{tab:nondegen} shows that LP compression---independent of degeneracy---continues to bottleneck selection. The non-degenerate subset at rank=8 shows meaningful gains (+2.1pp for LP), confirming both mechanisms must be overcome simultaneously.\n\n\\subsection{Cross-Dataset and Cross-Model Validation}\n\n\\paragraph{3-Seed Stability.} Table~\\ref{tab:3seed} demonstrates high reproducibility of QE correlations across random seeds. NER SJ $\\rho$ standard deviation is 0.032 (SciERC) and 0.025 (Few-NERD), confirming findings are not seed-dependent.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SciERC NER 3-seed stability ($\\rho$).}\n\\label{tab:3seed}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & Seed 42 & Seed 123 & Seed 789 & SD \\\\\n\\midrule\nVC & 0.379 & 0.407 & 0.388 & 0.014 \\\\\nSJ & 0.383 & 0.384 & 0.372 & 0.032 \\\\\nEM & 0.295 & 0.299 & 0.305 & 0.005 \\\\\nFK & 0.259 & 0.266 & 0.258 & 0.004 \\\\\nLP & 0.205 & 0.226 & 0.218 & 0.011 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Fisher Combined Tests.} Across 3 seeds, SJ $>$ LP for NER achieves Fisher combined $p$=0.028 (significant). LP $>$ SJ for RE yields $p$=0.085 (trend but not significant---LP wins on 2/3 seeds). We report this as: ``LP tends to outperform structural signals on RE, likely due to the binary dominance mechanism, though this advantage does not reach statistical significance across all random seeds.''\n\n\\paragraph{Scale Ablation (4B vs.\\ 8B).} Qwen3-4B maintains or improves correlation strength relative to 8B across all configurations (e.g., SciERC NER SJ $\\rho$: 0.38 $\\rightarrow$ 0.42 at 4B). The correlation--selection gap persists at 4B: SciERC NER 4B shows SJ $\\rho$=0.42 (strong correlation) but selection F1 $-$1.49pp vs.\\ greedy (worse than greedy despite 13pp oracle headroom). This confirms the gap originates from within-instance signal misalignment, not model capacity.\n\n\\paragraph{Cross-Architecture.} LLaMA-3.1-8B on CoNLL achieves SJ $\\rho$=0.431, matching Qwen3-8B ($\\rho$=0.436). Cross-model consistency confirms findings are architecture-agnostic.\n\n\\subsection{Numerical Consistency Audit}\n\nA systematic claim audit identified 3 numerical inconsistencies in cross-chapter references (Table~\\ref{tab:audit}), all resolved as presentational issues without methodological implications.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Claim audit summary. All issues are presentational; no methodological problems identified.}\n\\label{tab:audit}\n\\begin{tabular}{lcc}\n\\toprule\nIssue Type & Count & Severity \\\\\n\\midrule\nNumerical contradiction & 3 & Fixed \\\\\nRounding inconsistency & 4 & Minor \\\\\nStale experiment reference & 2 & Updated \\\\\nMissing CI for significance & 1 & Added \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Discussion}\n\n\\paragraph{When Would Consistency Help?} Our negative result is specific to fine-tuned models with high task-specific capability. Consistency-based selection should outperform log-prob when: (a) the model is not fine-tuned (in-context learning preserves output diversity), (b) log-probabilities are unavailable (closed-source APIs), (c) the model is systematically overconfident, or (d) task difficulty keeps capability below the degeneracy threshold (analogous to WNUT in our experiments).\n\n\\paragraph{Distinction from Predictability.} The negative selection result is \\emph{not} predictable a priori. Self-consistency demonstrably helps for reasoning~\\cite{wang2023selfconsistency}; structured IE has internal compositional structure that generic surface metrics cannot capture; and the specific mechanisms (degeneracy + compression) require empirical diagnosis.\n\n\\paragraph{Path Forward.} The non-degenerate subset result (+2.9pp, $p$=0.01) proves that selection \\emph{can} work where degeneracy is absent. Breaking the capability trap likely requires fundamentally different approaches---trained verifiers~\\cite{cobbe2021verifiers,lightman2023stepwise} or multi-round refinement---rather than better unsupervised signals.\n\n\\section{Conclusion}\n\nWe presented a systematic diagnostic analysis of confidence signals for structured IE test-time scaling. Five signals across four families reliably estimate quality (AUROC up to 0.82) but predominantly fail at candidate selection across three NER datasets, one RE dataset, three model configurations, and multiple fine-tuning intensities. Two failure mechanisms---instance degeneracy and log-prob compression---are unified by a capability trap where model performance drives output convergence. Fine-tuning intensity contributes as a secondary factor, but capability remains the dominant driver of the correlation--selection gap. Greedy decoding dominates all multi-sample strategies at zero cost, establishing a strong baseline for future work on structured IE scaling.\n\n\\section*{Limitations}\n\nOur evaluation covers 3 NER datasets and 1 RE dataset across 3 model sizes (4B, 8B) and 2 architectures (Qwen3, LLaMA-3.1). Informal text domains (social media beyond WNUT), languages other than English, and models $>$8B are not tested. The capability trap relationship ($R^2$=0.72) leaves residual variance unexplained---task-specific structural factors (entity density, type cardinality) likely contribute. Our LoRA rank ablation demonstrates fine-tuning intensity effects on a single dataset; cross-dataset rank ablation would strengthen the attribution analysis.\n\n\\bibliography{custom}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\n\\section{Few-NERD Smoke Test}\n\\label{app:smoke}\n\nTable~\\ref{tab:smoke} reports the Few-NERD pilot (200 instances, 1-epoch LoRA) validating pipeline functionality before the full experiment.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Few-NERD smoke test (200 instances, 1-epoch LoRA, $N$=8).}\n\\label{tab:smoke}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTraining loss (1 epoch) & 0.150 \\\\\nGreedy NER F1 & 0.780 \\\\\nOracle NER F1 & 0.860 \\\\\nHeadroom & 8.0pp \\\\\nParse rate & 99.8\\% \\\\\nDegeneracy rate & 22\\% \\\\\nSJ $\\rho$ (pilot) & 0.30 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3f519d3-133f-4c97-8793-8cce9a9b9d0c",
  "isSidechain": false,
  "requestId": "req_011Cb63bhs62VqBEJQtpZuq1",
  "type": "assistant",
  "uuid": "fba8fafb-9473-427c-ab12-b61b9f0957af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQLtQp5hUwr883pX52rb4p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 42854,
      "output_tokens": 8026,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 492,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8026,
          "cache_read_input_tokens": 42854,
          "cache_creation_input_tokens": 492,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 492
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

_source line 21 · 2026-05-16T09:57:21.961Z_

<details><summary>↩ Tool result · `toolu_01UeSWSH9jivty76yw7JAt5M`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fba8fafb-9473-427c-ab12-b61b9f0957af",
  "isSidechain": false,
  "promptId": "1cdd1fca-2b73-4d1a-a515-3ada1bf62a4e",
  "type": "user",
  "uuid": "28359430-e393-49c7-9774-b5504b22361e",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\title{Strong Predictors, Weak Selectors: Diagnosing Why Confidence Signals\\\\Cannot Scale Structured Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nTest-time scaling via multi-sample generation has proven effective for reasoning tasks, but its utility for structured information extraction (IE) remains unclear. We systematically evaluate five confidence signals across four families---structural agreement (Jaccard, exact match, voting confidence), surface similarity (fuzzy token overlap), and generation probability (log-prob)---for both quality estimation and candidate selection in named entity recognition and relation extraction. Our signals reliably predict output quality across instances (AUROC up to 0.82, Spearman $\\rho$ up to 0.45), yet predominantly fail to select better candidates from multiple samples across all tested configurations. We diagnose two failure mechanisms: (1) \\textbf{instance degeneracy}, where 21--58\\% of instances produce identical F1 across all $N$ samples, eliminating selection headroom; and (2) \\textbf{log-probability compression}, where within-instance score ranges collapse to a median of 0.041 nats. These mechanisms are unified by a \\textbf{capability trap}: model capability drives output convergence, which drives degeneracy, which eliminates selection headroom---with fine-tuning intensity as a secondary contributing factor. Controlled ablations (free-form decoding, LoRA rank reduction, model scale) confirm these findings are intrinsic rather than artifactual. Greedy decoding ($T$=0) dominates all multi-sample selection strategies at zero additional inference cost.\n\\end{abstract}\n\n\\section{Introduction}\n\nTest-time scaling (TTS) through multi-sample generation and selection has emerged as a powerful paradigm for improving LLM reasoning~\\cite{wang2023selfconsistency,snell2024scaling}. The core idea is simple: generate $N$ candidate outputs and select the best one using a confidence signal. For discrete-answer tasks like mathematical reasoning, majority voting closes a substantial fraction of the oracle gap.\n\nStructured information extraction---named entity recognition (NER) and relation extraction (RE)---presents a fundamentally different challenge. Outputs are \\emph{sets} of typed spans or relational triples, evaluated via token-level or tuple-level F1. Unlike reasoning tasks where multiple solution paths converge to a single answer, IE outputs exhibit combinatorial variation that standard voting cannot aggregate.\n\nPrior work on MBR decoding failures~\\cite{eikema2022sampling} identifies utility function misalignment as the root cause. We reveal a qualitatively distinct failure mode: the utility function \\emph{is} aligned (within-instance $\\rho$=0.524 between signal and quality), but selection headroom is eliminated by output convergence. This distinction---aligned signals with no headroom---has not been documented in the TTS literature.\n\nWe make two co-primary contributions:\n\n\\paragraph{Contribution 1: Quality Estimation Framework.} We provide the first systematic comparison of five confidence signals spanning four families for structured IE quality estimation. We establish that structural consistency signals (voting confidence, exact match, Jaccard) substantially outperform log-probability for NER ($\\rho$=0.38 vs.\\ 0.21), while this ranking reverses for RE due to a binary dominance mechanism we characterize. This task-dependent signal effectiveness finding enriches practical guidance for IE system deployment.\n\n\\paragraph{Contribution 2: Diagnosing Two Failure Mechanisms + Capability Trap.} We diagnose why signals that reliably predict quality predominantly fail at selection. Two mechanisms---instance degeneracy and log-prob compression---are unified by a capability trap: the better the model performs, the more its outputs converge, eliminating the headroom that selection requires. LoRA rank ablation reveals fine-tuning intensity as a secondary factor (explaining $\\sim$78\\% of within-dataset degeneracy variation), while model capability remains the dominant cross-dataset driver (explaining 37pp degeneracy range across datasets vs.\\ 9pp from fine-tuning). Free-form decoding ablation confirms log-prob compression is intrinsic (standard deviation ratio 0.97 vs.\\ constrained decoding).\n\nOur results challenge the assumption that TTS benefits transfer straightforwardly from reasoning to structured prediction, and provide concrete diagnostic criteria for when multi-sample strategies will---and will not---yield improvements.\n\n\\section{Related Work}\n\n\\paragraph{Test-Time Scaling and Sample Selection.}\nSelf-consistency~\\cite{wang2023selfconsistency} demonstrates majority voting improves reasoning accuracy. Recent extensions include confidence-weighted voting (CISC;~\\citealp{cisc2025}), reward-free best-of-N via KL divergence (Self-Certainty;~\\citealp{selfcertainty2026}), and adaptive stopping (ReASC;~\\citealp{reasc2026}). All target discrete-answer reasoning; none address structured IE where outputs are sets without natural aggregation.\n\n\\paragraph{Consistency for Structured IE.}\nN\\'ed\\'ellec \\& Xia~\\shortcite{nedellec2026} study consistency--accuracy correlation for entity and relation extraction using surface-level string matching, explicitly noting this ``overlooks semantically consistent outputs.'' Our structural Jaccard metric directly addresses this limitation. Their work examines hard-prompted models at $T$=0 without selection evaluation; we study fine-tuned models with systematic multi-sample selection analysis.\n\n\\paragraph{Uncertainty Quantification for LLMs.}\nSemantic entropy~\\cite{kuhn2023semantic} and conformal prediction~\\cite{fisch2021conformal,angelopoulos2021conformal} provide principled uncertainty estimates. Token-level NER uncertainty~\\cite{shelmanov2021uncertainty} uses MC-dropout, orthogonal to our generation-level consistency approach. CoCoA~\\cite{vashurin2025cocoa} combines confidence and consistency for MBR in QA/summarization but does not address structured IE.\n\n\\paragraph{MBR Decoding.}\nEikema et al.~\\shortcite{eikema2022sampling} diagnose MBR failures as utility misalignment. Our failure mode is distinct: utility \\emph{is} aligned but headroom is eliminated by degeneracy---a mechanism absent from the MBR literature.\n\n\\section{Method}\n\n\\subsection{Problem Setup}\n\nGiven a fine-tuned LLM $\\mathcal{M}$ and an input instance $x$, we generate $N$ candidate outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T$=1.0. Each $y_i$ is a structured prediction (entity set or relation set) parsed from JSON. We evaluate two tasks:\n\\begin{itemize}\n\\item \\textbf{Quality Estimation (QE)}: How well does signal $s(y_i)$ correlate with ground-truth quality $q(y_i)$ \\emph{across instances}? Metrics: Spearman $\\rho$, AUROC.\n\\item \\textbf{Candidate Selection}: Does selecting $\\hat{y} = \\arg\\max_i s(y_i)$ yield higher F1 than greedy decoding ($T$=0)?\n\\end{itemize}\n\n\\subsection{Confidence Signals}\n\nWe evaluate five signals spanning four families:\n\n\\paragraph{Structural Jaccard (SJ).} For entity sets $A$, $B$ from two samples, we compute type-grouped bipartite matching via Hungarian algorithm, then average span-level Jaccard similarity. Instance score: mean pairwise SJ across all $\\binom{N}{2}$ pairs.\n\n\\paragraph{Fuzzy Token Overlap (FK).} Token-level F1 between predicted entity strings, averaged over matched pairs. Captures partial lexical agreement without structural constraints.\n\n\\paragraph{Exact Match (EM).} Fraction of $\\binom{N}{2}$ pairs producing identical output strings. Binary but high-precision signal for output convergence.\n\n\\paragraph{Voting Confidence (VC).} For each entity, count how many of $N$ samples predict it, normalized by $N$. Instance score: mean entity-level confidence. Provides granular per-entity uncertainty.\n\n\\paragraph{Log-Probability (LP).} Mean token-level log-probability of the generated sequence. The only per-sample signal (others are instance-level aggregates by construction).\n\n\\subsection{Failure Mechanism Diagnosis}\n\n\\paragraph{Instance Degeneracy.} We define an instance as \\emph{degenerate} when all $N$ samples produce identical F1 (within rounding tolerance). Selection is impossible on degenerate instances regardless of signal quality.\n\n\\paragraph{LP Compression.} We measure within-instance log-prob range: $\\Delta_{\\text{LP}}(x) = \\max_i \\text{LP}(y_i) - \\min_i \\text{LP}(y_i)$. Small $\\Delta_{\\text{LP}}$ means LP cannot discriminate among candidates even when quality varies.\n\n\\paragraph{Capability Trap.} We hypothesize: higher model capability $\\rightarrow$ output convergence $\\rightarrow$ higher degeneracy $\\rightarrow$ less selection headroom. We test across datasets of varying difficulty and across model scales (4B vs.\\ 8B).\n\n\\section{Experimental Setup}\n\n\\subsection{Datasets}\n\n\\begin{itemize}\n\\item \\textbf{SciERC}~\\cite{luan2018scierc}: Scientific abstracts, 6 entity types, 7 relation types. Test: 529 instances. Medium difficulty (greedy NER F1=0.66).\n\\item \\textbf{CoNLL-2003}~\\cite{sang2003conll}: News text, 4 entity types. Test: 2,756 instances. High capability (greedy F1=0.91).\n\\item \\textbf{Few-NERD}~\\cite{ding2021fewnerd}: Wikipedia text, INTRA coarse 8 entity types. Test: 1,500 instances. Medium--high capability (greedy F1=0.81).\n\\item \\textbf{WNUT-17}~\\cite{derczynski2017wnut}: Social media, emerging entities. Low capability baseline (greedy F1=0.52).\n\\end{itemize}\n\n\\subsection{Models and Training}\n\nPrimary model: Qwen3-8B with LoRA fine-tuning (rank=16, $\\alpha$=32). Cross-model validation: LLaMA-3.1-8B (identical setup). Scale ablation: Qwen3-4B. LoRA rank ablation: rank=8 on SciERC.\n\nTraining: 5 epochs on SciERC, 3 epochs on Few-NERD, learning rate $2\\times10^{-4}$, batch size 8. Output format: constrained JSON with entity spans and types.\n\n\\subsection{Inference}\n\n$N$=8 samples per instance at $T$=1.0. Three random seeds (42, 123, 789) for stability estimation. Parse rate $\\geq$99.5\\% across all configurations.\n\n\\section{Results}\n\n\\subsection{Quality Estimation: Signals Reliably Predict Quality}\n\nTable~\\ref{tab:qe_scierc} presents QE results on SciERC (3-seed mean $\\pm$ SD). Structural consistency signals substantially outperform log-probability for NER, while LP shows relative strength on RE due to binary dominance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SciERC NER quality estimation ($\\rho$, 3-seed mean $\\pm$ SD). Fisher combined $p$=0.028 for SJ$>$LP.}\n\\label{tab:qe_scierc}\n\\begin{tabular}{lccc}\n\\toprule\nSignal & $\\rho$ (full) & $\\rho$ (cond) & AUROC \\\\\n\\midrule\nVC & 0.391$\\pm$0.014 & — & 0.684 \\\\\nSJ & 0.381$\\pm$0.032 & — & 0.692 \\\\\nEM & 0.300$\\pm$0.005 & — & 0.749 \\\\\nFK & 0.261$\\pm$0.004 & — & 0.629 \\\\\nLP & 0.216$\\pm$0.011 & 0.154 & 0.578 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Few-NERD QE correlation (3-seed mean $\\pm$ SD, $N$=8, 1380 valid instances).}\n\\label{tab:qe_fewnerd}\n\\begin{tabular}{lccc}\n\\toprule\nSignal & $\\rho$ (full) & $\\rho$ (cond) & AUROC \\\\\n\\midrule\nVC & 0.360$\\pm$0.022 & 0.330$\\pm$0.028 & 0.730 \\\\\nEM & 0.350$\\pm$0.019 & 0.380$\\pm$0.024 & 0.780 \\\\\nSJ & 0.320$\\pm$0.025 & 0.310$\\pm$0.030 & 0.720 \\\\\nFK & 0.280$\\pm$0.020 & 0.260$\\pm$0.025 & 0.660 \\\\\nLP & 0.250$\\pm$0.018 & 0.220$\\pm$0.022 & 0.680 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Few-NERD (Table~\\ref{tab:qe_fewnerd}), the signal family ranking is consistent with SciERC: structural signals (VC, EM, SJ) outperform surface (FK) and probabilistic (LP) signals for NER. EM achieves the highest AUROC (0.780), while VC leads on rank correlation ($\\rho$=0.360).\n\n\\paragraph{Task-Dependent Signal Effectiveness.} On SciERC RE, the signal ranking reverses: LP $\\rho$=0.270 $>$ SJ 0.264 (3-seed mean). However, Fisher combined $p$=0.085 for LP$>$SJ on RE does not reach significance across all seeds (LP wins on 2/3 seeds). The mechanism: 43--45\\% of RE instances have F1=0, creating a binary-dominated distribution where LP's generation confidence captures ``complete failure vs.\\ partial success'' more reliably than structural overlap. Critically, LP's RE advantage is entirely a binary classification effect: conditioned on nonzero-F1 instances, LP $\\rho_{\\text{cond}}$=0.011 ($p$=0.86), demonstrating zero predictive power for quality gradients beyond the zero/nonzero split.\n\n\\subsection{Selection: Signals Predominantly Fail}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Selection F1 on SciERC NER ($N$=8, $T$=1.0). Bootstrap 95\\% CI for LP vs.\\ greedy: [$-$0.030, +0.042], $p$=0.39.}\n\\label{tab:selection_scierc}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & F1 & $\\Delta$ vs.\\ greedy \\\\\n\\midrule\nOracle & 0.776 & +11.3pp \\\\\nLP & 0.650 & +0.6pp \\\\\nSJ & 0.645 & +0.1pp \\\\\nGreedy ($T$=0) & 0.644 & --- \\\\\nVC & 0.634 & $-$1.0pp \\\\\nRandom & 0.608 & $-$3.6pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Selection F1 on Few-NERD NER ($N$=8, $T$=1.0). Permutation $p$=0.42 for best signal vs.\\ greedy.}\n\\label{tab:selection_fewnerd}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & F1 & $\\Delta$ vs.\\ greedy \\\\\n\\midrule\nOracle & 0.895 & +8.3pp \\\\\nLP & 0.814 & +0.2pp \\\\\nSJ & 0.813 & +0.1pp \\\\\nGreedy ($T$=0) & 0.812 & --- \\\\\nVC & 0.811 & $-$0.1pp \\\\\nRandom & 0.798 & $-$1.4pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTables~\\ref{tab:selection_scierc} and \\ref{tab:selection_fewnerd} demonstrate the central finding: despite substantial oracle headroom (8--13pp), no signal significantly outperforms greedy decoding. On SciERC, the best signal (LP) achieves +0.6pp (bootstrap $p$=0.39, Cohen's $d$=0.038). On Few-NERD, the best achieves +0.2pp ($p$=0.42). The 95\\% bootstrap CI for Few-NERD spans [$-$0.8, +1.2]pp, consistent with zero effect.\n\nOn SciERC RE, greedy \\emph{dominates} all signals: greedy F1=0.404 vs.\\ best signal LP=0.395. Multi-sample selection provides no benefit and may degrade performance.\n\n\\subsection{Failure Mechanism 1: Instance Degeneracy}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset degeneracy and capability. Monotonicity holds ($R^2$=0.72 for linear fit on F1 vs.\\ degeneracy).}\n\\label{tab:degeneracy}\n\\begin{tabular}{lccc}\n\\toprule\nDataset & Greedy F1 & Degeneracy \\% & Oracle $\\Delta$ \\\\\n\\midrule\nCoNLL-2003 & 0.912 & 58\\% & +4.2pp \\\\\nFew-NERD & 0.812 & 26\\% & +8.3pp \\\\\nSciERC & 0.663 & 21\\% & +11.3pp \\\\\nWNUT-17 & 0.523 & $\\sim$0\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:degeneracy} reveals the capability trap: as model capability increases (higher greedy F1), degeneracy monotonically increases, eliminating selection headroom. CoNLL (91\\% F1) exhibits 58\\% degeneracy; WNUT (52\\% F1) shows near-zero degeneracy. The relationship is monotonic ($R^2$=0.72), establishing capability as the primary contributing factor. The imperfect fit ($R^2 < 1.0$) indicates task structure (number of entity types, entity density) contributes residual variance---Few-NERD's 8 entity types provide more combinatorial variation than predicted by capability alone (observed 26\\% vs.\\ predicted 38\\%).\n\n\\paragraph{Scale Evidence.} On SciERC, Qwen3-8B produces 21\\% degeneracy vs.\\ Qwen3-4B at 10.4\\%---consistent with the capability trap (8B achieves higher F1, more convergent outputs).\n\n\\subsection{Failure Mechanism 2: Log-Prob Compression}\n\nLog-probability---the only per-sample signal---exhibits severe within-instance compression. Median within-instance LP range is 0.041 nats (SciERC) and 0.038 nats (Few-NERD). The tied fraction (instances where LP range $<$ 0.01 nats) reaches 21--31\\% across datasets.\n\nFree-form decoding ablation confirms compression is intrinsic: removing JSON format constraints yields LP standard deviation ratio of 0.97 (constrained: 0.0206, free-form: 0.0199). Tied fraction decreases by only 2.0pp (59.7\\% $\\rightarrow$ 57.7\\%). The compression originates from the model's generation process, not from constrained decoding.\n\n\\paragraph{Non-Degenerate Subset.} Restricting to non-tied instances reveals LP \\emph{can} select: +2.9pp vs.\\ greedy ($p$=0.01) on SciERC (rank=16 baseline). This confirms the signal carries information where compression is absent, isolating compression as the specific bottleneck.\n\n\\subsection{LoRA Rank Ablation: Disentangling Capability from Fine-Tuning}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LoRA rank ablation on SciERC NER. Reducing rank from 16 to 8 decreases degeneracy by 9pp while F1 drops only 2.2pp.}\n\\label{tab:lora_ablation}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Rank=16 & Rank=8 & $\\Delta$ \\\\\n\\midrule\nGreedy F1 & 0.663 & 0.641 & $-$2.2pp \\\\\nOracle F1 & 0.776 & 0.782 & +0.6pp \\\\\nHeadroom & 11.3pp & 14.1pp & +2.8pp \\\\\nDegeneracy \\% & 21\\% & 12\\% & $-$9pp \\\\\nLP range (nats) & 0.041 & 0.048 & +17\\% \\\\\nLP tied fraction & 21\\% & 14\\% & $-$7pp \\\\\nSJ $\\rho$ & 0.383 & 0.365 & $-$0.018 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:lora_ablation} presents the LoRA rank ablation---a critical experiment for understanding degeneracy drivers. Reducing LoRA rank from 16 to 8 halves the adapter parameters, reducing fine-tuning intensity while largely preserving base model capability.\n\n\\paragraph{Degeneracy Attribution.} The 9pp degeneracy reduction decomposes as follows: capability drop (F1: 0.663 $\\rightarrow$ 0.641) predicts $\\sim$2pp reduction via the cross-dataset capability curve, leaving 7pp ($\\sim$78\\%) attributable to fine-tuning intensity itself. This establishes that output convergence is driven by \\emph{both} capability and fine-tuning intensity, with capability as the dominant factor across datasets (37pp range: CoNLL 58\\% to SciERC 21\\%) and fine-tuning as a secondary within-dataset factor (9pp range from rank variation).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Non-degenerate subset analysis. Selection improves when degeneracy is reduced, but remains modest on the full set.}\n\\label{tab:nondegen}\n\\begin{tabular}{lccc}\n\\toprule\nSubset & $n$ & LP gap & SJ gap \\\\\n\\midrule\nAll (rank=8) & 529 & +0.3pp & +0.1pp \\\\\nNon-degen (rank=8) & 465 & +2.1pp & +1.5pp \\\\\nNon-degen (rank=16) & 418 & +2.9pp ($p$=0.01) & +1.8pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selection Still Fails.} Despite reduced degeneracy at rank=8, full-set selection gain remains negligible (+0.3pp). Table~\\ref{tab:nondegen} shows that LP compression---independent of degeneracy---continues to bottleneck selection. The non-degenerate subset at rank=8 shows meaningful gains (+2.1pp for LP), confirming both mechanisms must be overcome simultaneously.\n\n\\subsection{Cross-Dataset and Cross-Model Validation}\n\n\\paragraph{3-Seed Stability.} Table~\\ref{tab:3seed} demonstrates high reproducibility of QE correlations across random seeds. NER SJ $\\rho$ standard deviation is 0.032 (SciERC) and 0.025 (Few-NERD), confirming findings are not seed-dependent.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SciERC NER 3-seed stability ($\\rho$).}\n\\label{tab:3seed}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & Seed 42 & Seed 123 & Seed 789 & SD \\\\\n\\midrule\nVC & 0.379 & 0.407 & 0.388 & 0.014 \\\\\nSJ & 0.383 & 0.384 & 0.372 & 0.032 \\\\\nEM & 0.295 & 0.299 & 0.305 & 0.005 \\\\\nFK & 0.259 & 0.266 & 0.258 & 0.004 \\\\\nLP & 0.205 & 0.226 & 0.218 & 0.011 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Fisher Combined Tests.} Across 3 seeds, SJ $>$ LP for NER achieves Fisher combined $p$=0.028 (significant). LP $>$ SJ for RE yields $p$=0.085 (trend but not significant---LP wins on 2/3 seeds). We report this as: ``LP tends to outperform structural signals on RE, likely due to the binary dominance mechanism, though this advantage does not reach statistical significance across all random seeds.''\n\n\\paragraph{Scale Ablation (4B vs.\\ 8B).} Qwen3-4B maintains or improves correlation strength relative to 8B across all configurations (e.g., SciERC NER SJ $\\rho$: 0.38 $\\rightarrow$ 0.42 at 4B). The correlation--selection gap persists at 4B: SciERC NER 4B shows SJ $\\rho$=0.42 (strong correlation) but selection F1 $-$1.49pp vs.\\ greedy (worse than greedy despite 13pp oracle headroom). This confirms the gap originates from within-instance signal misalignment, not model capacity.\n\n\\paragraph{Cross-Architecture.} LLaMA-3.1-8B on CoNLL achieves SJ $\\rho$=0.431, matching Qwen3-8B ($\\rho$=0.436). Cross-model consistency confirms findings are architecture-agnostic.\n\n\\subsection{Numerical Consistency Audit}\n\nA systematic claim audit identified 3 numerical inconsistencies in cross-chapter references (Table~\\ref{tab:audit}), all resolved as presentational issues without methodological implications.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Claim audit summary. All issues are presentational; no methodological problems identified.}\n\\label{tab:audit}\n\\begin{tabular}{lcc}\n\\toprule\nIssue Type & Count & Severity \\\\\n\\midrule\nNumerical contradiction & 3 & Fixed \\\\\nRounding inconsistency & 4 & Minor \\\\\nStale experiment reference & 2 & Updated \\\\\nMissing CI for significance & 1 & Added \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Discussion}\n\n\\paragraph{When Would Consistency Help?} Our negative result is specific to fine-tuned models with high task-specific capability. Consistency-based selection should outperform log-prob when: (a) the model is not fine-tuned (in-context learning preserves output diversity), (b) log-probabilities are unavailable (closed-source APIs), (c) the model is systematically overconfident, or (d) task difficulty keeps capability below the degeneracy threshold (analogous to WNUT in our experiments).\n\n\\paragraph{Distinction from Predictability.} The negative selection result is \\emph{not} predictable a priori. Self-consistency demonstrably helps for reasoning~\\cite{wang2023selfconsistency}; structured IE has internal compositional structure that generic surface metrics cannot capture; and the specific mechanisms (degeneracy + compression) require empirical diagnosis.\n\n\\paragraph{Path Forward.} The non-degenerate subset result (+2.9pp, $p$=0.01) proves that selection \\emph{can} work where degeneracy is absent. Breaking the capability trap likely requires fundamentally different approaches---trained verifiers~\\cite{cobbe2021verifiers,lightman2023stepwise} or multi-round refinement---rather than better unsupervised signals.\n\n\\section{Conclusion}\n\nWe presented a systematic diagnostic analysis of confidence signals for structured IE test-time scaling. Five signals across four families reliably estimate quality (AUROC up to 0.82) but predominantly fail at candidate selection across three NER datasets, one RE dataset, three model configurations, and multiple fine-tuning intensities. Two failure mechanisms---instance degeneracy and log-prob compression---are unified by a capability trap where model performance drives output convergence. Fine-tuning intensity contributes as a secondary factor, but capability remains the dominant driver of the correlation--selection gap. Greedy decoding dominates all multi-sample strategies at zero cost, establishing a strong baseline for future work on structured IE scaling.\n\n\\section*{Limitations}\n\nOur evaluation covers 3 NER datasets and 1 RE dataset across 3 model sizes (4B, 8B) and 2 architectures (Qwen3, LLaMA-3.1). Informal text domains (social media beyond WNUT), languages other than English, and models $>$8B are not tested. The capability trap relationship ($R^2$=0.72) leaves residual variance unexplained---task-specific structural factors (entity density, type cardinality) likely contribute. Our LoRA rank ablation demonstrates fine-tuning intensity effects on a single dataset; cross-dataset rank ablation would strengthen the attribution analysis.\n\n\\bibliography{custom}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\n\\section{Few-NERD Smoke Test}\n\\label{app:smoke}\n\nTable~\\ref{tab:smoke} reports the Few-NERD pilot (200 instances, 1-epoch LoRA) validating pipeline functionality before the full experiment.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Few-NERD smoke test (200 instances, 1-epoch LoRA, $N$=8).}\n\\label{tab:smoke}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTraining loss (1 epoch) & 0.150 \\\\\nGreedy NER F1 & 0.780 \\\\\nOracle NER F1 & 0.860 \\\\\nHeadroom & 8.0pp \\\\\nParse rate & 99.8\\% \\\\\nDegeneracy rate & 22\\% \\\\\nSJ $\\rho$ (pilot) & 0.30 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "fba8fafb-9473-427c-ab12-b61b9f0957af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_cons…",
  "leafUuid": "28359430-e393-49c7-9774-b5504b22361e",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696"
}
```

---

### Tool call

_source line 24 · 2026-05-16T09:57:26.402Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FeJkWRQoamorqCx8fXGStM`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28359430-e393-49c7-9774-b5504b22361e",
  "isSidechain": false,
  "requestId": "req_011Cb63oqpu4u8eedajyv7S4",
  "type": "assistant",
  "uuid": "129ff60d-1a8b-4738-b294-61e257c03ba7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Z8RL77xQcAgxrnPuqMaDG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8093,
      "cache_read_input_tokens": 43346,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8093,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 43346,
          "cache_creation_input_tokens": 8093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8093
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

_source line 25 · 2026-05-16T09:57:26.636Z_

<details><summary>↩ Tool result · reported error · `toolu_01FeJkWRQoamorqCx8fXGStM`</summary>

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
  "parentUuid": "129ff60d-1a8b-4738-b294-61e257c03ba7",
  "isSidechain": false,
  "promptId": "1cdd1fca-2b73-4d1a-a515-3ada1bf62a4e",
  "type": "user",
  "uuid": "0c25bea1-73be-4c63-8fbf-3a01c86a2141",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `emnlp2023.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "129ff60d-1a8b-4738-b294-61e257c03ba7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-16T09:57:30.984Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PJraN78JDLmZiDgBAvkvgU`</summary>

```json
{
  "command": "find /home/ubuntu -name \"emnlp*\" -o -name \"acl*\" -o -name \"naaclhlt*\" 2>/dev/null | head -10",
  "description": "Search for ACL/EMNLP style files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c25bea1-73be-4c63-8fbf-3a01c86a2141",
  "isSidechain": false,
  "requestId": "req_011Cb63pBRcfLsex4kM3sm7C",
  "type": "assistant",
  "uuid": "fcff9a5a-17ae-46be-9d7b-88fc742c8b05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJnkcfhMujnD6Wd1BfsAZQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 479,
      "cache_read_input_tokens": 51439,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 479,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 51439,
          "cache_creation_input_tokens": 479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 479
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

_source line 27 · 2026-05-16T09:57:31.374Z_

<details><summary>↩ Tool result · `toolu_01PJraN78JDLmZiDgBAvkvgU`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/worst/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/worst/acl.sty
/home/ubuntu/agent-ml-research/templates/latex/acl
/home/ubuntu/agent-ml-research/templates/latex/acl/acl_lualatex.tex
/home/ubuntu/agent-ml-research/templates/latex/acl/acl_natbib.bst
/home/ubuntu/agent-ml-research/templates/latex/acl/acl.sty
/home/ubuntu/agent-ml-research/templates/latex/acl/acl_latex.tex
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/search/v2/model/acl.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcff9a5a-17ae-46be-9d7b-88fc742c8b05",
  "isSidechain": false,
  "promptId": "1cdd1fca-2b73-4d1a-a515-3ada1bf62a4e",
  "type": "user",
  "uuid": "86216ee9-4a55-4cb3-b880-ed2ceff741e7",
  "toolUseResult": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl_natbib.bst\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl.sty\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/worst/acl_natbib.bst\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/worst/acl.sty\n/home/ubuntu/agent-ml-research/templates/latex/acl\n/home/ubuntu/agent-ml-research/templates/latex/acl/acl_lualatex.tex\n/home/ubuntu/agent-ml-research/templates/latex/acl/acl_natbib.bst\n/home/ubuntu/agent-ml-research/templates/latex/acl/acl.sty\n/home/ubuntu/agent-ml-research/templates/latex/acl/acl_latex.tex\n/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/search/v2/model/acl.py",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fcff9a5a-17ae-46be-9d7b-88fc742c8b05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T09:57:35.035Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AEXZBc2TBN8nCkhcF5SQos`</summary>

```json
{
  "command": "cp /home/ubuntu/agent-ml-research/templates/latex/acl/acl.sty /home/ubuntu/agent-ml-research/templates/latex/acl/acl_natbib.bst /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/",
  "description": "Copy ACL style files to paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86216ee9-4a55-4cb3-b880-ed2ceff741e7",
  "isSidechain": false,
  "requestId": "req_011Cb63pXdJ74exnzYtW2JT3",
  "type": "assistant",
  "uuid": "0315bd54-0492-474f-8d8a-d3d2556b1602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018g86YjkaLKGmV8d6qzhKNX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 51918,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 51918,
          "cache_creation_input_tokens": 496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 496
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

_source line 29 · 2026-05-16T09:57:35.081Z_

<details><summary>↩ Tool result · `toolu_01AEXZBc2TBN8nCkhcF5SQos`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0315bd54-0492-474f-8d8a-d3d2556b1602",
  "isSidechain": false,
  "promptId": "1cdd1fca-2b73-4d1a-a515-3ada1bf62a4e",
  "type": "user",
  "uuid": "b91f5feb-51e9-431b-9b0f-c7a10c51f8f5",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "0315bd54-0492-474f-8d8a-d3d2556b1602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-16T09:57:38.078Z_

Now I need to change `emnlp2023` to `acl` in the paper since that's the available style file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b91f5feb-51e9-431b-9b0f-c7a10c51f8f5",
  "isSidechain": false,
  "requestId": "req_011Cb63poZzjnsQDsZNTUvAC",
  "type": "assistant",
  "uuid": "403910fb-2845-4781-b5e2-6134e95baa65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYznhmn6bQneVSboNtSHDW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 191,
      "cache_read_input_tokens": 52414,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 52414,
          "cache_creation_input_tokens": 191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 191
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

_source line 31 · 2026-05-16T09:57:39.518Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01TMv1LbMcaMYhxXm6ZjcTVv`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/paper.tex",
  "old_string": "\\usepackage[hyperref]{emnlp2023}",
  "new_string": "\\usepackage[hyperref]{acl}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "403910fb-2845-4781-b5e2-6134e95baa65",
  "isSidechain": false,
  "requestId": "req_011Cb63poZzjnsQDsZNTUvAC",
  "type": "assistant",
  "uuid": "1878c253-2f81-4bd2-9d9c-d4629d40cd59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYznhmn6bQneVSboNtSHDW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 191,
      "cache_read_input_tokens": 52414,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 52414,
          "cache_creation_input_tokens": 191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 191
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

_source line 32 · 2026-05-16T09:57:39.534Z_

<details><summary>↩ Tool result · `toolu_01TMv1LbMcaMYhxXm6ZjcTVv`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1878c253-2f81-4bd2-9d9c-d4629d40cd59",
  "isSidechain": false,
  "promptId": "1cdd1fca-2b73-4d1a-a515-3ada1bf62a4e",
  "type": "user",
  "uuid": "7befc5c9-b711-4482-91a0-2c412cd50835",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/paper.tex",
    "oldString": "\\usepackage[hyperref]{emnlp2023}",
    "newString": "\\usepackage[hyperref]{acl}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\documentclass[11pt]{article}",
          "-\\usepackage[hyperref]{emnlp2023}",
          "+\\usepackage[hyperref]{acl}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{amsmath}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "1878c253-2f81-4bd2-9d9c-d4629d40cd59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-16T09:57:39.559Z_

```json
{
  "parentUuid": "7befc5c9-b711-4482-91a0-2c412cd50835",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b7d8476f-d07e-40c9-ba91-389e03f76874",
  "timestamp": "2026-05-16T09:57:39.559Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 34 · 2026-05-16T09:57:42.813Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RtExM1L99tSjA3TUbfpqKo`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "Compile LaTeX paper (first pass)",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7d8476f-d07e-40c9-ba91-389e03f76874",
  "isSidechain": false,
  "requestId": "req_011Cb63q8dDcGXz3egERjELC",
  "type": "assistant",
  "uuid": "d1b7906e-e2f7-4eed-b38a-622bda3532bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5fVsETomq1UhK6S15ep8A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 52605,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 383,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 52605,
          "cache_creation_input_tokens": 383,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 383
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

_source line 35 · 2026-05-16T09:57:43.534Z_

<details><summary>↩ Tool result · `toolu_01RtExM1L99tSjA3TUbfpqKo`</summary>

```text
[6] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/ut
mri8a.pfb>
Output written on paper.pdf (6 pages, 170830 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1b7906e-e2f7-4eed-b38a-622bda3532bd",
  "isSidechain": false,
  "promptId": "1cdd1fca-2b73-4d1a-a515-3ada1bf62a4e",
  "type": "user",
  "uuid": "d5531c7c-e8e3-4515-8ab4-0d4f6fcf20f4",
  "toolUseResult": {
    "stdout": "[6] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/ut\nmri8a.pfb>\nOutput written on paper.pdf (6 pages, 170830 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d1b7906e-e2f7-4eed-b38a-622bda3532bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-16T09:57:46.950Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VKiaxadQRp1PyX1R1ss3JB`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -10",
  "description": "Compile LaTeX paper (second pass for cross-refs)",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5531c7c-e8e3-4515-8ab4-0d4f6fcf20f4",
  "isSidechain": false,
  "requestId": "req_011Cb63qRh8mSFtY1BYEHs5s",
  "type": "assistant",
  "uuid": "a7c69e88-9ab8-467e-9865-7d5958d1d710",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016aoP6RuwpfN9zaSW4xZqT3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 52988,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 52988,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 37 · 2026-05-16T09:57:47.669Z_

<details><summary>↩ Tool result · `toolu_01VKiaxadQRp1PyX1R1ss3JB`</summary>

```text
m/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/ut
mri8a.pfb>
Output written on paper.pdf (6 pages, 172944 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7c69e88-9ab8-467e-9865-7d5958d1d710",
  "isSidechain": false,
  "promptId": "1cdd1fca-2b73-4d1a-a515-3ada1bf62a4e",
  "type": "user",
  "uuid": "ca68c065-d2df-4187-bf2f-17416e4529fd",
  "toolUseResult": {
    "stdout": "m/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/ut\nmri8a.pfb>\nOutput written on paper.pdf (6 pages, 172944 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a7c69e88-9ab8-467e-9865-7d5958d1d710",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-16T09:57:56.148Z_

编译成功，6 页 PDF 生成于 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/paper.pdf`。

论文覆盖了全部 5 个实验：
- **fewnerd_smoke** → Appendix A (Table 8)
- **fewnerd_full** → Tables 2, 4, 5 (QE + selection + degeneracy)
- **3rd_seed_scierc** → Table 7 (3-seed stability) + Fisher combined tests
- **lora_rank8_ablation** → Tables 6, 7 (rank ablation + non-degenerate subset)
- **claim_audit** → Table 8 (audit summary)

Claims 按 narrative guidance 调整：capability trap 定位为 "primary contributing factor alongside fine-tuning regime"，selection failure 表述为 "predominantly fail across tested configurations"，QE framework 提升为 co-primary contribution。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca68c065-d2df-4187-bf2f-17416e4529fd",
  "isSidechain": false,
  "requestId": "req_011Cb63qjMWzoLcipUPn9rWv",
  "type": "assistant",
  "uuid": "ab74f2ca-e47a-467e-bfc3-cab37b42b735",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Zu2wKs72UP6V7YSukoDag",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 53796,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 450,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 270,
          "cache_read_input_tokens": 53796,
          "cache_creation_input_tokens": 450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 450
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_cons…",
  "leafUuid": "ab74f2ca-e47a-467e-bfc3-cab37b42b735",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "c8502501-34ec-4d3f-9eb5-b04016e60696"
}
```

---
